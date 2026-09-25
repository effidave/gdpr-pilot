#!/usr/bin/env python3
"""Fetch each vocabulary in sources.csv from its publisher and parse it.

Tries each URL in turn with content negotiation for RDF. Saves the raw file
to cache/ and reports triples and term counts. Non-RDF sources (SSSOM's
LinkML YAML, the RO-Crate JSON-LD context) are saved and parsed separately.
"""
import csv, sys, time
from pathlib import Path
import requests, rdflib

UA = "oht-coined-term-review/0.1 (manual research; low volume)"
ACCEPT = "text/turtle, application/rdf+xml;q=0.9, application/ld+json;q=0.8, application/n-triples;q=0.7, */*;q=0.1"
CACHE = Path("cache"); CACHE.mkdir(exist_ok=True)
FMT = {"turtle": "turtle", "rdf+xml": "xml", "ld+json": "json-ld", "n-triples": "nt", "owl+xml": "xml", "xml": "xml"}

def guess(ct, url, body):
    for k, v in FMT.items():
        if k in ct: return v
    if url.endswith((".ttl",)): return "turtle"
    if url.endswith((".rdf", ".owl")): return "xml"
    head = body[:500].lstrip()
    if head.startswith(b"<?xml") or head.startswith(b"<rdf"): return "xml"
    if head.startswith(b"{"): return "json-ld"
    return "turtle"

s = requests.Session(); s.headers.update({"User-Agent": UA, "Accept": ACCEPT})
rows = list(csv.DictReader(open("sources.csv")))
only = set(sys.argv[1:])
report = []
for r in rows:
    if only and r["prefix"] not in only: continue
    status = "failed"
    for url in r["urls"].split():
        try:
            resp = s.get(url, timeout=60, allow_redirects=True)
        except requests.RequestException as e:
            print(f"{r['prefix']}: {url} -> {e}"); continue
        ct = resp.headers.get("content-type", "")
        print(f"{r['prefix']}: {url} -> {resp.status_code} {ct} {len(resp.content)}B final={resp.url}")
        time.sleep(1)
        if resp.status_code != 200 or "text/html" in ct: continue
        if url.endswith((".yaml", "/context")):
            ext = ".yaml" if url.endswith(".yaml") else ".jsonld"
            (CACHE / f"{r['prefix']}{ext}").write_bytes(resp.content)
            status = f"ok (non-RDF {ext}) from {resp.url}"; break
        fmt = guess(ct, resp.url, resp.content)
        g = rdflib.Graph()
        try:
            g.parse(data=resp.content, format=fmt, publicID=resp.url)
        except Exception as e:
            print(f"   parse error ({fmt}): {str(e)[:150]}"); continue
        if len(g) == 0: continue
        g.serialize(CACHE / f"{r['prefix']}.ttl", format="turtle")
        ns = r["namespace"]
        terms = {x for x in g.subjects() if isinstance(x, rdflib.URIRef) and str(x).startswith(ns.replace("https://", "http://")) or str(x).startswith(ns)}
        status = f"ok {len(g)} triples, {len(terms)} terms in namespace, from {resp.url}"; break
    report.append((r["prefix"], r["vocabulary"], status))
print()
for p, v, st in report: print(f"{p:12} {v:32} {st}")
