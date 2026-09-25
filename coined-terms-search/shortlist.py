#!/usr/bin/env python3
"""Plan step C: shortlist index terms for each coined term.

BM25 over each index term's label (camelCase split, counted three times) and
definition, queried with the coined definition plus job keywords. Same-kind
terms get a small boost. Leads from the earlier reviews are added whether or
not they rank. Writes results/shortlists.json and results/shortlists.md.
"""
import csv, json, math, re
from collections import Counter, defaultdict
from coined_terms import T

STOP = set("a an the of to in on for and or by with as is are be this that its it from at which who whom what how not no any each one".split())
def toks(s):
    s = re.sub(r"([a-z])([A-Z])", r"\1 \2", s or "")
    return [w for w in re.findall(r"[a-z0-9]+", s.lower().replace("_", " ")) if w not in STOP and len(w) > 1]

rows = list(csv.DictReader(open("index/terms.csv", encoding="utf-8")))
ns = {r["prefix"]: r["namespace"] for r in csv.DictReader(open("index/sources.csv"))}
ns["dcterms"] = ns["dct"] = "http://purl.org/dc/terms/"
by_iri = {}
for r in rows: by_iri.setdefault(r["iri"], r)
def expand(pn):
    p, l = pn.split(":", 1)
    base = ns.get(p, "")
    for b in (base, base.replace("https://", "http://"), base.replace("http://", "https://")):
        if b + l in by_iri: return b + l
    return None

prof = defaultdict(set)
for p in csv.DictReader(open("index/profiles.csv", encoding="utf-8")):
    t = p["term"]
    if ":" in t and not t.startswith("http"): t = expand(t) or t
    t = t.replace("http://schema.org/", "https://schema.org/")
    prof[t].add("DCAT-AP " + p["obligation"] if p["profile"].startswith("DCAT") else "RO-Crate")

docs = [toks(r["label"]) * 3 + toks(r["iri"].rsplit("/", 1)[-1].rsplit("#", 1)[-1]) + toks(r["definition"]) for r in rows]
N = len(docs); avg = sum(map(len, docs)) / N
df = Counter(w for d in docs for w in set(d))
tfs = [Counter(d) for d in docs]
def bm25(q, i, k1=1.2, b=0.75):
    tf, L = tfs[i], len(docs[i]); s = 0.0
    for w in q:
        if w in tf:
            idf = math.log(1 + (N - df[w] + 0.5) / (df[w] + 0.5))
            s += idf * tf[w] * (k1 + 1) / (tf[w] + k1 * (1 - b + b * L / avg))
    return s

def entry(r, score, how):
    return {"iri": r["iri"], "prefix": r["prefix"], "tier": r["tier"], "kind": r["kind"], "label": r["label"],
            "definition": r["definition"], "domain": r["domain"], "range": r["range"], "parents": r["parents"],
            "deprecated": r["deprecated"], "status": r["status"], "source": r["source"],
            "profiles": sorted(prof.get(r["iri"], [])), "score": round(score, 2), "found_by": how}

out = []
for item, term, kind, defn, group, kw, leads in T:
    q = list(dict.fromkeys(toks(defn) + toks(kw)))
    scored = []
    for i, r in enumerate(rows):
        s = bm25(q, i)
        if s <= 0: continue
        if r["kind"] == kind: s *= 1.2
        if r["deprecated"]: s *= 0.5
        scored.append((s, i))
    scored.sort(reverse=True)
    cands, seen = [], set()
    for s, i in scored[:15]:
        seen.add(rows[i]["iri"]); cands.append(entry(rows[i], s, "bm25"))
    missing = []
    for pn in leads.split():
        iri = expand(pn)
        if not iri: missing.append(pn); continue
        if iri in seen:
            for c in cands:
                if c["iri"] == iri: c["found_by"] = "bm25+lead"
            continue
        seen.add(iri); cands.append(entry(by_iri[iri], bm25(q, rows.index(by_iri[iri])), "lead"))
    out.append({"item": item, "term": term, "kind": kind, "definition": defn, "group": group, "candidates": cands, "leads_not_in_index": missing})

json.dump(out, open("results/shortlists.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
with open("results/shortlists.md", "w", encoding="utf-8") as f:
    f.write("# Shortlists (plan step C)\n\nBM25 top 15 plus leads from earlier reviews. Machine output for reading, not judgements.\n\n")
    for t in out:
        f.write(f"## {t['item']}. {t['term']} ({t['group']})\n\n{t['definition']}\n\n")
        if t["leads_not_in_index"]: f.write(f"Leads not in index: {', '.join(t['leads_not_in_index'])}\n\n")
        for c in t["candidates"]:
            f.write(f"- {c['found_by']} {c['score']} `{c['iri']}` [{c['kind']}, tier {c['tier']}{', ' + ', '.join(c['profiles']) if c['profiles'] else ''}{', DEPRECATED ' + c['deprecated'] if c['deprecated'] else ''}] {c['definition'][:160]}\n")
        f.write("\n")
print("leads missing:", {t["term"]: t["leads_not_in_index"] for t in out if t["leads_not_in_index"]})
