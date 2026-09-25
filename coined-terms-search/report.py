#!/usr/bin/env python3
"""Plan step G: write results/report.md and results/candidates.csv from
judgements.py, the shortlists and the index. Definitions are quoted from
index/terms.csv (fetched from each publisher), or from judgements.QUOTES."""
import csv, json
from collections import Counter, OrderedDict
from coined_terms import T
from judgements import J, QUOTES
from summary_text import SUMMARY

rows = list(csv.DictReader(open("index/terms.csv", encoding="utf-8")))
own = {}
for r in rows:  # prefer the vocabulary's own row over SSSOM's slot rows that reuse an IRI
    if r["iri"] not in own or (own[r["iri"]]["prefix"] == "sssom" and r["prefix"] != "sssom"):
        own[r["iri"]] = r
if "owl:annotatedProperty" in [r["iri"] for r in rows]:
    own["owl:annotatedProperty"] = next(r for r in rows if r["iri"] == "owl:annotatedProperty")
TIER_NOTE = {"1": "tier 1", "2": "tier 2", "3": "tier 3"}
PN = [("http://www.w3.org/ns/dcat#", "dcat:"), ("http://purl.org/dc/terms/", "dcterms:"), ("http://www.w3.org/2004/02/skos/core#", "skos:"),
      ("http://www.w3.org/ns/prov#", "prov:"), ("https://schema.org/", "schema:"), ("https://w3id.org/sssom/", "sssom:"),
      ("http://www.w3.org/ns/oa#", "oa:"), ("http://rdf-vocabulary.ddialliance.org/xkos#", "xkos:"), ("http://www.w3.org/ns/ssn/", "ssn:"),
      ("http://www.w3.org/ns/sosa/", "sosa:"), ("http://purl.org/spar/cito/", "cito:"), ("http://data.europa.eu/eli/ontology#", "eli:"),
      ("http://purl.org/ontology/bibo/", "bibo:"), ("https://w3id.org/semapv/vocab/", "semapv:"), ("http://www.w3.org/ns/duv#", "duv:"),
      ("http://w3id.org/nkos#", "nkos:"), ("http://w3id.org/nkos/nkostype#", "nkostype:"), ("http://www.w3.org/ns/adms#", "adms:"),
      ("http://purl.org/pav/", "pav:"), ("http://purl.obolibrary.org/obo/", "obo:"), ("http://www.w3.org/2002/07/owl#", "owl:"),
      ("http://purl.org/linked-data/cube#", "qb:"), ("http://rdf-vocabulary.ddialliance.org/discovery#", "disco:"), ("http://xmlns.com/foaf/0.1/", "foaf:"),
      ("https://w3id.org/dpv/risk#", "risk:"), ("https://w3id.org/dpv#", "dpv:"), ("http://www.w3.org/ns/dqv#", "dqv:"), ("http://www.w3.org/ns/mls#", "mls:"),
      ("http://purl.org/skos-history/", "sh:"), ("http://usefulinc.com/ns/doap#", "doap:"), ("http://www.w3.org/ns/odrl/2/", "odrl:"),
      ("http://purl.org/dc/dcmitype/", "dcmitype:"), ("http://cv.iptc.org/newscodes/digitalsourcetype/", "iptcdst:"),
      ("http://publications.europa.eu/resource/authority/access-right/", "access-right:")]
def pn(i):
    for a, b in PN:
        if i.startswith(a): return b + i[len(a):]
    return i
FIT = {"exact": "exact fit", "super": "fits as superclass or superproperty", "related": "related but not a fit", "irrelevant": "irrelevant"}

def quote(iri):
    if iri in QUOTES: return QUOTES[iri][0], QUOTES[iri][1], "verified at source (specification text)"
    r = own.get(iri)
    if not r: return "", "", "not in index"
    d = r["definition"]
    if not d: return "", r["source"], "no definition in the source file"
    v = "verified at source"
    if d.startswith("[definition of"): v = "verified at source (definition carried by the qualified class)"
    if r["prefix"] == "nkostype": v = "definition verified in HTML; IRI inferred from the documented pattern"
    return d, r["source"], v

def short(d, n=260):
    d = d.replace("[[", "").replace("]]", "").replace("|", "/")
    return d if len(d) <= n else d[:n].rsplit(" ", 1)[0] + " ..."

sl = {t["item"]: t for t in json.load(open("results/shortlists.json", encoding="utf-8"))}
cnt = Counter(J[i]["verdict"] for i in J)

out = ["# Existing terms for the 68 coined oht: terms", "",
       "Proposals only; nothing in the ontology has been changed. Method: `PLAN.md`. Every definition quoted below was read from the publisher's own file or specification in this session (`index/SOURCES.md`); the source is given per candidate. Definitions of the coined terms come from `context/COINED-TERMS-REVIEW.md`, because `ontology/oht.ttl` is not in this repository.", ""]
out += ["## Summary", "", "### Proposed verdicts", "", "| Verdict | Terms |", "|---|---|"]
for v in ["Replace", "Drop", "Keep under standard super", "Keep"]:
    out.append(f"| {v.replace('super', 'superclass or superproperty')} | {cnt[v]} ({', '.join(str(i) for i in sorted(J) if J[i]['verdict'] == v)}) |")
out += ["", f"Replace or drop: {cnt['Replace'] + cnt['Drop']}. Keep, with or without a standard parent: {cnt['Keep'] + cnt['Keep under standard super']}. Taken together, the ontology would shrink from 68 coined terms to {cnt['Keep'] + cnt['Keep under standard super']}, of which {cnt['Keep under standard super']} are anchored to a standard parent.", ""]
out += SUMMARY
out += ["", "## Terms", ""]

cand_rows = []
for item, term, kind, defn, group, _, _ in T:
    j = J[item]
    out += [f"### {item}. `{term}`", "", f"**Coined definition:** {defn}. (Triage group: {dict(M='mechanical', P='pattern', D='domain or editorial')[group]}.)", "",
            f"**Proposed verdict: {j['verdict'].replace('super', 'superclass or superproperty')}.** {j['line']}", "",
            "| Candidate | Tier | Definition at source | Fit |", "|---|---|---|---|"]
    ev = []
    judged = set()
    for iri, fit, reason in j["cands"]:
        judged.add(iri)
        q, src, v = quote(iri)
        r = own.get(iri, {})
        tier = r.get("tier", "")
        prof = ""
        for c in sl[item]["candidates"]:
            if c["iri"] == iri and c["profiles"]: prof = "; named in " + ", ".join(p.replace("DCAT-AP optional/other", "DCAT-AP 3 (not mandatory)").replace("DCAT-AP mandatory", "DCAT-AP 3 (mandatory)").replace("RO-Crate", "the RO-Crate 1.2 context") for p in c["profiles"])
        out.append(f"| `{pn(iri)}` ({r.get('vocabulary', '')}) | {tier} | \"{short(q) if q else '(none in file)'}\" [source]({src.split(' ')[0]}) | **{FIT[fit]}**{prof}. {reason} |")
        if fit in ("exact", "super"): ev.append(f"`{pn(iri)}`: {v}")
        cand_rows.append({"item": item, "term": term, "candidate": iri, "prefixed": pn(iri), "vocabulary": r.get("vocabulary", ""), "tier": tier,
                          "fit": fit, "reason": reason, "definition": q, "source": src, "evidence": v, "found_by": next((c["found_by"] for c in sl[item]["candidates"] if c["iri"] == iri), "reading")})
    out += ["", "**Evidence:** " + ("; ".join(ev) if ev else "no standard term recommended; candidates read at source and judged not to fit.")]
    if j["cmp"]: out += ["", f"**Against the second review:** {j['cmp']}"]
    out.append("")
    for c in sl[item]["candidates"]:
        if c["iri"] in judged: continue
        cand_rows.append({"item": item, "term": term, "candidate": c["iri"], "prefixed": pn(c["iri"]), "vocabulary": own.get(c["iri"], {}).get("vocabulary", c["prefix"]),
                          "tier": c["tier"], "fit": "screened out", "reason": "Read in the shortlist; word overlap only, not a fit for the coined meaning.",
                          "definition": c["definition"], "source": c["source"], "evidence": "definition from source file" if c["definition"] else "no definition in file", "found_by": c["found_by"]})

open("results/report.md", "w", encoding="utf-8").write("\n".join(out) + "\n")
with open("results/candidates.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(cand_rows[0])); w.writeheader(); w.writerows(cand_rows)
print(cnt, len(cand_rows), "candidate rows")
