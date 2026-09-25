#!/usr/bin/env python3
"""Phase 1 calibration: score query styles against known answers."""
import csv, json, re, statistics, sys
from collections import defaultdict
from pathlib import Path
import requests
sys.path.insert(0, ".")
from lov_search import call, parse_result, UA

OUT = Path("results/calibration_raw"); OUT.mkdir(parents=True, exist_ok=True)
TOP = 15

def norm(iri):
    iri = iri.strip()
    iri = re.sub(r"^https://", "http://", iri)
    return iri.rstrip("#/")

s = requests.Session(); s.headers["User-Agent"] = UA
known = {int(r["item"]): r for r in csv.DictReader(open("calibration/known_answers.csv"))}
expected = {i: {norm(x) for x in r["expected_iris"].split(";")} for i, r in known.items()}

# ---- indexing check: is the vocabulary listed, and is each expected IRI a term in it?
vlist = call(s, "/vocabulary/list", {}, OUT, 1.2) or []
by_nsp = defaultdict(list)
for v in vlist:
    by_nsp[norm(v.get("nsp", ""))].append(v["prefix"])
def vocab_for(iri):
    n = norm(iri); best = None
    for nsp, prefs in by_nsp.items():
        if nsp and (n.startswith(nsp + "#") or n.startswith(nsp + "/") or n == nsp):
            if best is None or len(nsp) > len(best[0]): best = (nsp, prefs)
    return best
index = {}
for i, exp in expected.items():
    for iri in sorted(exp):
        vf = vocab_for(iri)
        local = re.split(r"[#/]", iri)[-1]
        found = False
        for pref in (vf[1] if vf else []):
            d = call(s, "/term/search", {"q": local, "vocab": pref, "page_size": 50}, OUT, 1.2) or {}
            if any(norm(r.get("uri", "")) == iri for r in d.get("results") or []):
                found = True
        if not found:  # try unfiltered in case LOV files it under an alias prefix
            d = call(s, "/term/search", {"q": local, "page_size": 50}, OUT, 1.2) or {}
            found = any(norm(r.get("uri", "")) == iri for r in d.get("results") or [])
        index[iri] = {"vocab_prefixes": vf[1] if vf else [], "term_found": found}

# ---- run queries, with and without the type filter
rows = list(csv.DictReader(open("calibration/calibration_queries.csv")))
results = []
for row in rows:
    item = int(row["item"])
    for filt in ([row["type"]] if row["type"] else []) + [""]:
        p = {"q": row["query"], "page_size": TOP}
        if filt: p["type"] = filt
        d = call(s, "/term/search", p, OUT, 1.2) or {}
        uris = [norm(parse_result(r)["uri"]) for r in d.get("results") or []][:TOP]
        ranks = [uris.index(e) + 1 for e in expected[item] if e in uris]
        results.append({**row, "filter": filt or "none", "total": d.get("total_results"),
                        "rank": min(ranks) if ranks else None, "top": uris})
json.dump({"index": index, "results": results}, open("results/calibration_results.json", "w"), indent=1)
print("done", len(results))
