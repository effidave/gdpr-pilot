#!/usr/bin/env python3
"""Merge the fetched vocabularies into one term table: index/terms.csv.

One row per term (class, property or individual) with label, definition,
domain, range, parents, deprecation, source and tier. Also writes
index/profiles.csv: which properties the DCAT-AP shapes require or
recommend per class, and which terms the RO-Crate context names.
"""
import csv, json, re
from pathlib import Path
import rdflib, yaml
from rdflib.namespace import RDF, RDFS, OWL, SKOS, DCTERMS

C = Path("cache")
SCHEMA = rdflib.Namespace("https://schema.org/")
IAO_DEF = rdflib.URIRef("http://purl.obolibrary.org/obo/IAO_0000115")
VS = rdflib.URIRef("http://www.w3.org/2003/06/sw-vocab-status/ns#term_status")
DC11 = rdflib.Namespace("http://purl.org/dc/elements/1.1/")
PROV_DEF = rdflib.URIRef("http://www.w3.org/ns/prov#definition")
CLASS_T = {OWL.Class, RDFS.Class, RDFS.Datatype}
PROP_T = {RDF.Property, OWL.ObjectProperty, OWL.DatatypeProperty, OWL.AnnotationProperty,
          OWL.FunctionalProperty, OWL.TransitiveProperty, OWL.SymmetricProperty, OWL.InverseFunctionalProperty}
SKIP_T = {OWL.Ontology, OWL.Restriction, OWL.AllDisjointClasses, OWL.Axiom}

def pick(g, s, preds):
    """Prefer English, then untagged, then anything."""
    vals = [o for p in preds for o in g.objects(s, p) if isinstance(o, rdflib.Literal)]
    for want in ("en", None):
        for v in vals:
            if (v.language or None) == want or (want == "en" and (v.language or "").startswith("en")):
                return " ".join(str(v).split())
    return " ".join(str(vals[0]).split()) if vals else ""

def short(g, iris):
    out = []
    for i in iris:
        if isinstance(i, rdflib.URIRef):
            try: out.append(g.namespace_manager.normalizeUri(i))
            except Exception: out.append(str(i))
    return "; ".join(sorted(out))

def qualified_def(g, t):
    """PROV-O defines many properties only on their qualified class."""
    for q in g.objects(t, rdflib.URIRef("http://www.w3.org/ns/prov#qualifiedForm")):
        if (q, RDF.type, OWL.Class) in g:
            d = pick(g, q, [PROV_DEF, RDFS.comment])
            if d: return f"[definition of {g.namespace_manager.normalizeUri(q)}] {d}"
    return ""

src = list(csv.DictReader(open("sources.csv")))
rows = []
for s in src:
    p, ns = s["prefix"], s["namespace"]
    f = C / f"{p}.ttl"
    if not f.exists() or p in ("dcatap",): continue
    g = rdflib.Graph(); g.parse(f)
    nss = {ns, ns.replace("https://", "http://"), ns.replace("http://", "https://")}
    if p == "iao": nss = {"http://purl.obolibrary.org/obo/IAO_"}
    for t in sorted({x for x in g.subjects() if isinstance(x, rdflib.URIRef) and any(str(x).startswith(n) for n in nss) and str(x) not in nss}):
        types = set(g.objects(t, RDF.type))
        if types & SKIP_T: continue
        kind = "class" if types & CLASS_T else "property" if types & PROP_T else "individual" if types else "untyped"
        if p == "schema" and not types: continue
        dep = ""
        if (t, OWL.deprecated, rdflib.Literal(True)) in g: dep = "owl:deprecated"
        st = pick(g, t, [VS])
        if st in ("archaic", "deprecated", "unstable"): dep = f"vs:{st}"
        if list(g.objects(t, SCHEMA.supersededBy)): dep = "schema:supersededBy " + short(g, g.objects(t, SCHEMA.supersededBy))
        part = short(g, g.objects(t, SCHEMA.isPartOf))
        if "attic" in part: dep = (dep + " attic").strip()
        rows.append({
            "iri": str(t), "prefix": p, "vocabulary": s["vocabulary"], "tier": s["tier_guess"], "kind": kind,
            "label": pick(g, t, [RDFS.label, SKOS.prefLabel]),
            "definition": pick(g, t, [SKOS.definition, IAO_DEF, PROV_DEF, RDFS.comment, DCTERMS.description, DC11.description]) or qualified_def(g, t),
            "types": short(g, types),
            "parents": short(g, list(g.objects(t, RDFS.subClassOf)) + list(g.objects(t, RDFS.subPropertyOf))),
            "domain": short(g, list(g.objects(t, RDFS.domain)) + list(g.objects(t, SCHEMA.domainIncludes))),
            "range": short(g, list(g.objects(t, RDFS.range)) + list(g.objects(t, SCHEMA.rangeIncludes))),
            "status": ("pending" if "pending" in part else "") , "deprecated": dep,
            "source": s["urls"].split()[0]})

# SSSOM (LinkML YAML): classes, slots, enum values
y = yaml.safe_load(open(C / "sssom.yaml"))
base = "https://w3id.org/sssom/"
pfx = {k: (v if isinstance(v, str) else v.get("prefix_reference")) for k, v in (y.get("prefixes") or {}).items()}
def expand(c):
    if c and ":" in c and not c.startswith("http"):
        a, b = c.split(":", 1)
        if a in pfx: return pfx[a] + b
    return c
for kind, sect in (("class", "classes"), ("property", "slots")):
    for name, d in (y.get(sect) or {}).items():
        d = d or {}
        rows.append({"iri": expand(d.get("slot_uri") or d.get("class_uri")) or base + name, "prefix": "sssom", "vocabulary": "SSSOM",
                     "tier": 2, "kind": kind, "label": name, "definition": " ".join(str(d.get("description", "")).split()),
                     "types": "linkml:" + sect, "parents": d.get("is_a", "") or "", "domain": "", "range": d.get("range", "") or "",
                     "status": "", "deprecated": "deprecated" if d.get("deprecated") else "", "source": "https://w3id.org/sssom/"})
for ename, e in (y.get("enums") or {}).items():
    for val, d in ((e or {}).get("permissible_values") or {}).items():
        d = d or {}
        rows.append({"iri": expand(d.get("meaning")) or f"{base}{ename}#{val}", "prefix": "sssom", "vocabulary": "SSSOM",
                     "tier": 2, "kind": "individual", "label": f"{val} ({ename})", "definition": " ".join(str(d.get("description", "")).split()),
                     "types": "enum " + ename, "parents": "", "domain": "", "range": "", "status": "", "deprecated": "",
                     "source": "https://w3id.org/sssom/"})
# NKOS KOS types (scraped from HTML; IRIs follow the documented pattern)
for r in csv.DictReader(open(C / "nkostype.csv")):
    rows.append({"iri": r["iri"], "prefix": "nkostype", "vocabulary": "NKOS KOS Types", "tier": 3, "kind": "individual",
                 "label": r["label"], "definition": r["definition"], "types": "", "parents": "", "domain": "", "range": "",
                 "status": "IRI inferred from documented pattern", "deprecated": "", "source": "https://nkos.dublincore.org/nkos-type.html"})

fields = ["iri", "prefix", "vocabulary", "tier", "kind", "label", "definition", "types", "parents", "domain", "range", "status", "deprecated", "source"]
seen = set(); out = []
for r in rows:
    k = (r["iri"], r["prefix"])
    if k in seen: continue
    seen.add(k); out.append(r)
with open("terms.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(out)

# Profiles: DCAT-AP shapes and RO-Crate context
SH = rdflib.Namespace("http://www.w3.org/ns/shacl#")
g = rdflib.Graph(); g.parse(C / "dcatap.ttl")
prof = []
for shape in set(g.subjects(SH.targetClass, None)) | set(g.subjects(RDF.type, SH.NodeShape)):
    tc = short(g, g.objects(shape, SH.targetClass))
    for ps in g.objects(shape, SH.property):
        for path in g.objects(ps, SH.path):
            mc = next(g.objects(ps, SH.minCount), None)
            sev = short(g, g.objects(ps, SH.severity))
            prof.append({"profile": "DCAT-AP 3.0.0", "context": tc, "term": short(g, [path]) if isinstance(path, rdflib.URIRef) else "(complex path)",
                         "obligation": "mandatory" if mc and int(mc) > 0 else ("recommended" if "Warning" in sev else "optional/other"),
                         "note": sev})
ctx = json.load(open(C / "rocrate.jsonld"))["@context"]
ctx = ctx if isinstance(ctx, dict) else {k: v for c in ctx if isinstance(c, dict) for k, v in c.items()}
for k, v in ctx.items():
    iri = v if isinstance(v, str) else (v or {}).get("@id", "")
    if iri.startswith("http"):
        prof.append({"profile": "RO-Crate 1.2 context", "context": "", "term": iri, "obligation": "named in context", "note": k})
with open("profiles.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["profile", "context", "term", "obligation", "note"]); w.writeheader(); w.writerows(prof)

from collections import Counter
print(len(out), "terms;", Counter(r["prefix"] for r in out).most_common())
print("kinds", Counter(r["kind"] for r in out))
print("no definition", sum(1 for r in out if not r["definition"]))
print("profiles rows", Counter(r["profile"] for r in prof), Counter(r["obligation"] for r in prof if r["profile"].startswith("DCAT")))
