#!/usr/bin/env python3
"""Score calibration results by style and style combination."""
import json, itertools, statistics
from collections import defaultdict
d = json.load(open("results/calibration_results.json"))
index, res = d["index"], d["results"]
exp_items = defaultdict(set)
import csv, re
def norm(i): return re.sub(r"^https://", "http://", i.strip()).rstrip("#/")
for r in csv.DictReader(open("calibration/known_answers.csv")):
    exp_items[int(r["item"])] = {norm(x) for x in r["expected_iris"].split(";")}
indexed = {i for i, e in exp_items.items() if any(index[x]["term_found"] for x in e)}
items = sorted(exp_items)
STY = {"a": "short keywords", "b": "descriptive phrase", "c": "quoted phrase", "d": "job phrase", "e": "camelCase local name"}

def best(item, styles, filt, spelling=None):
    rs = [r for r in res if int(r["item"]) == item and r["style"] in styles and r["rank"]
          and (filt == "any" or r["filter"] == filt or (filt == "typed" and r["filter"] != "none" or filt=="typed" and not any(x["item"]==r["item"] and x["filter"]!="none" for x in res)))
          and (spelling is None or r["spelling"] in ("", spelling))]
    return min((r["rank"] for r in rs), default=None)

def nq(item, styles, filt):
    return len([r for r in res if int(r["item"]) == item and r["style"] in styles and (filt=="any" or r["filter"]==filt)])

out = []
out.append("| Style | Queries (unfiltered) | Queries that hit | Items hit, top 15 (of %d indexed) | Mean best rank | Items hit |" % len(indexed))
out.append("|---|---|---|---|---|---|")
rows = []
for combo in [("a",),("b",),("c",),("d",),("e",),("a","e"),("a","d"),("a","d","e"),("a","b","c","d","e")]:
    ranks = {i: best(i, combo, "none") for i in items}
    hits = {i: r for i, r in ranks.items() if r}
    qs = [r for r in res if r["style"] in combo and r["filter"] == "none"]
    qh = [r for r in qs if r["rank"]]
    label = " + ".join(f"({c}) {STY[c]}" for c in combo) if len(combo) < 5 else "all styles"
    mr = f"{statistics.mean(hits.values()):.1f}" if hits else "-"
    out.append(f"| {label} | {len(qs)} | {len(qh)} | {len(hits)} | {mr} | {', '.join(str(i) for i in sorted(hits))} |")
print("\n".join(out))
print()
# per item
print("| # | Term | Expected indexed in LOV? | (a) | (b) | (c) | (d) | (e) | Best query |")
print("|---|---|---|---|---|---|---|---|---|")
terms = {int(r["item"]): r["term"] for r in res}
for i in items:
    idx = "; ".join(f"{x.split('/')[-1]}: {'yes' if index[x]['term_found'] else 'no'}" for x in sorted(exp_items[i]))
    cells = [str(best(i, (s,), "none") or "-") for s in "abcde"]
    hits = sorted([r for r in res if int(r["item"]) == i and r["rank"] and r["filter"]=="none"], key=lambda r: r["rank"])
    bq = f"`{hits[0]['query']}` (rank {hits[0]['rank']})" if hits else "none"
    print(f"| {i} | {terms[i]} | {idx} | " + " | ".join(cells) + f" | {bq} |")
print()
# type filter effect
tf = [(r, next((x for x in res if x["item"]==r["item"] and x["query"]==r["query"] and x["filter"]=="none"), None)) for r in res if r["filter"] not in ("none",)]
better = sum(1 for a,b in tf if a["rank"] and (not b["rank"] or a["rank"]<b["rank"]))
worse = sum(1 for a,b in tf if b["rank"] and (not a["rank"] or a["rank"]>b["rank"]))
print(f"type filter: {len(tf)} paired queries; filter improved rank in {better}, worsened in {worse}")
for a,b in tf:
    if a["rank"]!=b["rank"]: print("  ", a["item"], a["query"], "typed", a["rank"], "untyped", b["rank"])
# spelling
for q in ["catalog record","catalogue record","CatalogRecord","CatalogueRecord","expiry date","expiration date"]:
    r=next(x for x in res if x["query"]==q and x["filter"]=="none"); print("spelling", q, r["rank"], r["top"][:2])
