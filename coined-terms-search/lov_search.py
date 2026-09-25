#!/usr/bin/env python3
"""
Search Linked Open Vocabularies (LOV) for existing terms that could replace
coined oht: terms.

Input   lov_queries.csv with columns: item, term, type, query
        type is "class", "property", or blank for any type.
Output  <out>/raw/            raw JSON of every API call (cached; reruns are free)
        <out>/candidates.csv  one row per coined term and candidate
        <out>/summary.md      top candidates per coined term

Usage   pip install requests
        python lov_search.py lov_queries.csv --out lov_out --top 8

Notes
- Field names checked against live responses on 2026-09-25. If a field comes
  out blank, check a file in <out>/raw/ and adjust parse_result() or
  vocab_details(). Nothing is lost, as raw JSON is kept.
- The docs spell the type filter "propery", but live LOV silently ignores
  that value; "property" works and is what the script sends. If a filtered
  query returns nothing it retries unfiltered and filters locally.
- Be polite: keep --pause at 1 second or more.
"""
import argparse
import csv
import hashlib
import json
import re
import sys
import time
from collections import defaultdict
from pathlib import Path

import requests

# The documented /dataset/lov/api/v2 path now returns 404; the API moved to
# /dataset/api/v2 (checked 2026-09-25, see results/NOTES.md).
BASE = "https://lov.linkeddata.es/dataset/api/v2"
UA = "oht-coined-term-review/0.1 (manual research; low volume)"


def first(v):
    """LOV returns many fields as single-item lists."""
    if isinstance(v, list):
        return v[0] if v else ""
    return "" if v is None else v


def cache_path(raw, path, params):
    """Cache by request content, so editing or reordering queries is safe."""
    key = json.dumps([path, params], sort_keys=True)
    name = path.strip("/").replace("/", "_")
    return raw / f"{name}_{hashlib.sha1(key.encode()).hexdigest()[:12]}.json"


def call(session, path, params, raw, pause):
    cache = cache_path(raw, path, params)
    if cache.exists():
        return json.loads(cache.read_text())
    for attempt in range(3):
        try:
            r = session.get(BASE + path, params=params, timeout=30)
            if r.status_code == 200:
                data = r.json()
                cache.write_text(json.dumps(data, indent=2))
                time.sleep(pause)
                return data
            print(f"  HTTP {r.status_code}: {path} {params}", file=sys.stderr)
        except (requests.RequestException, ValueError) as e:
            print(f"  {e}: {path} {params}", file=sys.stderr)
        time.sleep(2 * (attempt + 1))
    return None


def highlight_text(h):
    if not isinstance(h, dict):
        return ""
    bits = []
    for vals in h.values():
        for s in vals if isinstance(vals, list) else [vals]:
            bits.append(re.sub(r"</?b>", "", str(s)))
    return " | ".join(dict.fromkeys(bits))[:300]


def parse_result(r):
    # Live responses nest vocabulary and metrics as objects and return scalars,
    # not the single-item lists and dotted keys the docs suggested.
    vocab = r.get("vocabulary") or {}
    metrics = r.get("metrics") or {}
    return {
        "uri": first(r.get("uri")),
        "prefixedName": first(r.get("prefixedName")),
        "type": first(r.get("type")),
        "vocab": first(vocab.get("prefix") if isinstance(vocab, dict) else vocab),
        "score": float(r.get("score") or 0),
        "occurrences": metrics.get("occurrencesInDatasets", ""),
        "reused_by_datasets": metrics.get("reusedByDatasets", ""),
        "highlight": highlight_text(r.get("highlight")),
    }


def vocab_details(info):
    if not info:
        return {"vocab_title": "", "vocab_latest_version": ""}
    titles = info.get("titles") or []
    title = ""
    for t in titles if isinstance(titles, list) else [titles]:
        if isinstance(t, dict) and t.get("lang", "en") in ("en", "", None):
            title = t.get("value", "")
            break
    title = title or first(info.get("title")) or ""
    dates = [v.get("issued", "") for v in info.get("versions") or [] if isinstance(v, dict)]
    return {"vocab_title": title, "vocab_latest_version": max(dates) if dates else ""}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("queries")
    ap.add_argument("--out", default="lov_out")
    ap.add_argument("--top", type=int, default=8)
    ap.add_argument("--page-size", type=int, default=15)
    ap.add_argument("--pause", type=float, default=1.0)
    a = ap.parse_args()

    out = Path(a.out)
    raw = out / "raw"
    raw.mkdir(parents=True, exist_ok=True)
    s = requests.Session()
    s.headers["User-Agent"] = UA

    rows = list(csv.DictReader(open(a.queries, newline="", encoding="utf-8")))
    hits = defaultdict(dict)  # (item, term) -> uri -> candidate
    shown_keys = False

    for i, row in enumerate(rows):
        key = (int(row["item"]), row["term"])
        want = (row.get("type") or "").strip()
        params = {"q": row["query"], "page_size": a.page_size}
        if want:
            params["type"] = want
        print(f"[{i + 1}/{len(rows)}] {row['term']}: {row['query']}")
        data = call(s, "/term/search", params, raw, a.pause)
        results = (data or {}).get("results") or []
        if want and not results:
            params.pop("type")
            data = call(s, "/term/search", params, raw, a.pause)
            results = [r for r in (data or {}).get("results") or []
                       if want in str(first(r.get("type"))).lower()]
        if results and not shown_keys:
            print("  result fields:", sorted(results[0].keys()))
            shown_keys = True
        for r in results:
            c = parse_result(r)
            if not c["uri"]:
                continue
            prev = hits[key].get(c["uri"])
            if prev:
                prev["score"] = max(prev["score"], c["score"])
                prev["queries"].add(row["query"])
            else:
                c["queries"] = {row["query"]}
                hits[key][c["uri"]] = c

    ranked = {k: sorted(v.values(), key=lambda c: -c["score"])[: a.top]
              for k, v in hits.items()}
    vocabs = {c["vocab"] for cs in ranked.values() for c in cs if c["vocab"]}
    details = {}
    for p in sorted(vocabs):
        info = call(s, "/vocabulary/info", {"vocab": p}, raw, a.pause)
        details[p] = vocab_details(info)

    fields = ["item", "term", "rank", "prefixedName", "uri", "type", "vocab",
              "vocab_title", "vocab_latest_version", "score", "occurrences",
              "reused_by_datasets", "found_by", "highlight"]
    with open(out / "candidates.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for (item, term), cs in sorted(ranked.items()):
            for n, c in enumerate(cs, 1):
                d = details.get(c["vocab"], {})
                w.writerow({"item": item, "term": term, "rank": n,
                            "prefixedName": c["prefixedName"], "uri": c["uri"],
                            "type": c["type"], "vocab": c["vocab"],
                            "vocab_title": d.get("vocab_title", ""),
                            "vocab_latest_version": d.get("vocab_latest_version", ""),
                            "score": round(c["score"], 2),
                            "occurrences": c["occurrences"],
                            "reused_by_datasets": c["reused_by_datasets"],
                            "found_by": "; ".join(sorted(c["queries"])),
                            "highlight": c["highlight"]})

    with open(out / "summary.md", "w", encoding="utf-8") as f:
        f.write("# LOV candidates for coined oht: terms\n\n")
        for (item, term), cs in sorted(ranked.items()):
            f.write(f"## {item}. {term}\n\n")
            if not cs:
                f.write("No results.\n\n")
                continue
            for c in cs:
                d = details.get(c["vocab"], {})
                f.write(f"- `{c['prefixedName'] or c['uri']}` ({c['type']}; "
                        f"{d.get('vocab_title') or c['vocab']}; latest version "
                        f"{d.get('vocab_latest_version') or 'unknown'}; "
                        f"used in {c['reused_by_datasets'] or '?'} datasets)"
                        f" - {c['highlight']}\n")
            f.write("\n")
    print(f"Done: {out / 'candidates.csv'} and {out / 'summary.md'}")


if __name__ == "__main__":
    main()
