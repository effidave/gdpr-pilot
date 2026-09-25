#!/usr/bin/env python3
"""
Phase 1 calibration: score query styles against known answers.

Input   calibration/calibration_queries.csv  (item, term, style, spelling, type, query)
        calibration/known_answers.csv         (item, term, ..., expected_iris)
Output  results/raw/                          cached API responses (shared with lov_search.py)
        results/calibration_hits.csv          rank of each expected IRI per query
        results/calibration.md                table by style and style combination

Usage   python calibrate.py [--type-param type|propery] [--page-size 15]

Not yet run against live LOV: the session that wrote it could not reach
lov.linkeddata.es (see results/NOTES.md). Check Phase 0 first.
"""
import argparse
import csv
import itertools
import re
from collections import defaultdict
from pathlib import Path

import requests

from lov_search import UA, call, first

TOP = 15


def norm(iri):
    """Compare IRIs loosely: scheme, trailing separator and case of host."""
    iri = iri.strip()
    iri = re.sub(r"^https?://", "", iri)
    iri = iri.rstrip("#/")
    host, _, rest = iri.partition("/")
    return host.lower() + ("/" + rest if rest else "")


def namespace(iri):
    m = re.match(r"(.*[#/])[^#/]*$", iri)
    return m.group(1) if m else iri


def indexed_namespaces(s, raw, pause):
    """All vocabulary namespaces LOV knows, normalised."""
    data = call(s, "/vocabulary/list", {}, raw, pause) or []
    out = set()
    for v in data if isinstance(data, list) else data.get("results", []):
        ns = first(v.get("nsp") or v.get("namespace") or v.get("uri"))
        if ns:
            out.add(norm(ns))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--queries", default="calibration/calibration_queries.csv")
    ap.add_argument("--answers", default="calibration/known_answers.csv")
    ap.add_argument("--out", default="results")
    ap.add_argument("--type-param", default="type",
                    help="spelling of the type filter that Phase 0 found to work")
    ap.add_argument("--page-size", type=int, default=TOP)
    ap.add_argument("--pause", type=float, default=1.0)
    a = ap.parse_args()

    out = Path(a.out)
    raw = out / "raw"
    raw.mkdir(parents=True, exist_ok=True)
    s = requests.Session()
    s.headers["User-Agent"] = UA

    expected = {}
    for r in csv.DictReader(open(a.answers, newline="", encoding="utf-8")):
        expected[int(r["item"])] = {norm(x) for x in r["expected_iris"].split(";") if x.strip()}

    indexed = indexed_namespaces(s, raw, a.pause)
    coverage = {item: any(norm(namespace(i)) in indexed or
                          any(i.startswith(ns) for ns in indexed) for i in iris)
                for item, iris in expected.items()}

    # best rank of any expected IRI, per (item, style, query)
    rows = []
    for q in csv.DictReader(open(a.queries, newline="", encoding="utf-8")):
        item = int(q["item"])
        params = {"q": q["query"], "page_size": a.page_size}
        if q["type"]:
            params[a.type_param] = q["type"]
        data = call(s, "/term/search", params, raw, a.pause)
        uris = [norm(first(r.get("uri"))) for r in (data or {}).get("results") or []]
        ranks = [n for n, u in enumerate(uris, 1) if u in expected.get(item, set())]
        rows.append({**q, "best_rank": min(ranks) if ranks else "",
                     "n_results": len(uris), "indexed": coverage.get(item)})

    with open(out / "calibration_hits.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    # per item, best rank achieved by each style (min over its queries)
    best = defaultdict(dict)
    for r in rows:
        if r["best_rank"] != "":
            k = r["style"]
            best[int(r["item"])][k] = min(best[int(r["item"])].get(k, 99), r["best_rank"])

    styles = sorted({r["style"] for r in rows})
    combos = [c for n in range(1, len(styles) + 1) for c in itertools.combinations(styles, n)]
    scorable = [i for i in expected if coverage[i]]

    lines = ["# Calibration", "",
             f"Items with an expected vocabulary indexed in LOV: {len(scorable)} of {len(expected)}.",
             "Not indexed (excluded from scores): "
             + (", ".join(str(i) for i in expected if not coverage[i]) or "none"), "",
             "| Styles | Hits in top 15 | Mean rank of hits |", "|---|---|---|"]
    for c in combos:
        found = [min(best[i][k] for k in c if k in best[i]) for i in scorable
                 if any(k in best[i] for k in c)]
        mean = f"{sum(found) / len(found):.1f}" if found else "-"
        lines.append(f"| {' + '.join(c)} | {len(found)} / {len(scorable)} | {mean} |")
    lines += ["", "## Per item", "", "| Item | Indexed | " + " | ".join(styles) + " |",
              "|---" * (len(styles) + 2) + "|"]
    for i in sorted(expected):
        lines.append(f"| {i} | {'yes' if coverage[i] else 'no'} | "
                     + " | ".join(str(best[i].get(k, "-")) for k in styles) + " |")
    (out / "calibration.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {out / 'calibration.md'}")


if __name__ == "__main__":
    main()
