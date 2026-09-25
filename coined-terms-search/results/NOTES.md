# Notes

## 2026-09-25 - first attempt: blocked at Phase 0

### What happened

This run took place in a Claude Code cloud container. The environment's network policy only allows package registries (PyPI, npm and similar), so:

- `lov.linkeddata.es` - CONNECT refused by the egress proxy (HTTP 403). The WebFetch tool is blocked for the same host too (`EGRESS_BLOCKED`).
- `www.w3.org`, `schema.org` and `w3id.org` - refused as well, so no namespace document or specification can be fetched either.

So none of Phases 0 to 5 can run from here. Nothing has been searched and nothing has been verified. No LOV field names have been checked, and the `type` versus `propery` question is still open.

### What was prepared so it can run as soon as access exists

- `calibration/calibration_queries.csv` - 58 queries for the 11 known-answer items, in styles (a) short keywords, (b) five-to-eight-word descriptive phrases and (c) quoted phrases, with British and American spellings where they differ (only "catalogue/catalog" among these items; the rest are marked `both`).
- `calibrate.py` - runs those queries through `lov_search.call()` (same cache and politeness rules), checks each expected namespace against LOV's `/vocabulary/list` so "not indexed" is kept separate from "query missed", normalises IRIs (http/https, trailing `#` or `/`, host case), and writes `results/calibration.md` (hits in top 15 and mean rank for each style and each combination of styles) plus `results/calibration_hits.csv`. Tested only against mocked responses.
  - `--type-param` sets the spelling of the type filter once Phase 0 settles `type` versus `propery`.
  - The `/vocabulary/list` field for the namespace is a guess (`nsp`, falling back to `namespace` or `uri`); check it in Phase 0.

### Access needed

Add these hosts to the environment's allowed domains (or choose a broader network access level):

- `lov.linkeddata.es` - required for Phases 0 to 3
- `www.w3.org`, `w3id.org`, `schema.org`, `purl.org`, `purl.obolibrary.org`, `data.europa.eu`, `xmlns.com`, `rdf-vocabulary.ddialliance.org`, `usefulinc.com`, `cv.iptc.org`, `mapping-commons.github.io`, `github.com` / `raw.githubusercontent.com` - for Phases 4 and 5 (dereferencing IRIs and reading specifications). `w3id.org` and `purl.org` redirect elsewhere, so the redirect targets must be allowed too.

Alternatively, run this folder on a machine with ordinary internet access.

### Partial fallback found

The npm packages under `@vocabulary/*` (for example `@vocabulary/dcat` 2.0.0 and `@vocabulary/oa` 1.0.6) bundle snapshots of many vocabularies and can be downloaded here. They could supply definitions for Phase 5 but not LOV search. They are third-party copies, so under rule 2 they are not the defining document: a definition taken from them should be labelled "snapshot, not verified at source". There is no `@vocabulary/sssom`. I haven't used them in this run, because the instructions call for stopping after Phase 1 and Phase 1 needs LOV.
