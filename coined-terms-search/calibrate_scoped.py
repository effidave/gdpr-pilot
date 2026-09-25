#!/usr/bin/env python3
"""Style (f): short keywords, results restricted locally to the vocabularies
vocab_jobs.csv lists for the item (deep unfiltered page, filtered client-side)."""
import csv, json, re, sys
from collections import defaultdict
from pathlib import Path
import requests
sys.path.insert(0, ".")
from lov_search import call, UA
OUT = Path("results/calibration_raw")
def norm(i): return re.sub(r"^https://", "http://", i.strip()).rstrip("#/")
s = requests.Session(); s.headers["User-Agent"] = UA
vlist = call(s, "/vocabulary/list", {}, OUT, 1.2)
nsp2pref = defaultdict(list)
for v in vlist: nsp2pref[norm(v.get("nsp",""))].append(v["prefix"])
jobs = list(csv.DictReader(open("context/vocab_jobs.csv")))
item_vocabs = defaultdict(set)
for j in jobs:
    prefs = nsp2pref.get(norm(j["namespace"].split(" ")[0]), [])
    for it in re.findall(r"\d+", j["relevant_items"]):
        for p in prefs: item_vocabs[int(it)].add(p)
known = {int(r["item"]): {norm(x) for x in r["expected_iris"].split(";")} for r in csv.DictReader(open("calibration/known_answers.csv"))}
qs = [r for r in csv.DictReader(open("calibration/calibration_queries.csv")) if r["style"] in ("a","d","e")]
out = []
for i, exp in sorted(known.items()):
    vs = sorted(item_vocabs[i])
    best = None; bq = None; n = 0
    # LOV's vocab= filter silently drops every property (see NOTES.md), so fetch
    # a deep unfiltered page and keep only the item's vocabularies locally.
    for q in [r["query"] for r in qs if int(r["item"]) == i]:
        d = call(s, "/term/search", {"q": q, "page_size": 1000}, OUT, 1.2) or {}
        n += 1
        uris = [norm(r["uri"]) for r in d.get("results") or []
                if (r.get("vocabulary") or {}).get("prefix") in vs]
        rk = [uris.index(e)+1 for e in exp if e in uris]
        if rk and (best is None or min(rk) < best): best, bq = min(rk), q
    out.append({"item": i, "vocabs": vs, "calls": n, "rank": best, "query": bq})
    print(i, vs, n, best, bq)
json.dump(out, open("results/calibration_scoped.json","w"), indent=1)
