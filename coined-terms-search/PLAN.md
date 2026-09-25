# Revised plan (replaces Phases 2 to 6 of INSTRUCTIONS.md)

Agreed 2026-09-25 after Phase 1. The goal is unchanged: find existing terms that could replace or anchor each of the 68 coined terms, **adopting only where there is real adoption and an interoperability advantage**. The method changes because calibration showed LOV searches names only, indexes no individuals, holds old copies of key standards (DCAT 2, schema.org v7.0) and has a broken `vocab=` filter, while its adoption figures are stale (see `results/NOTES.md`).

Phases 0 and 1 are done (`results/NOTES.md`, `results/calibration.md`). The rules in `INSTRUCTIONS.md` still apply: proposals only, verify at source and quote with URL, hyphens only, output to `results/`.

## A. Local index of adoptable vocabularies - done

`index/`: every vocabulary in `context/vocab_jobs.csv`, plus SKOS-XL, DCMI Type and OBO IAO, fetched from its publisher and merged into `index/terms.csv` (7,725 terms with label, definition, domain, range, parents, deprecation, source, tier). `index/profiles.csv` records which terms DCAT-AP 3 and RO-Crate 1.2 name. Sources and problems are in `index/SOURCES.md`.

## B. Triage the 68 coined terms

Sort each term into one of three groups before matching:

1. **Mechanical** - note-like, date-like or type-slot properties. Default proposal: declare the standard parent (`dcterms:description`, `dcterms:date`, `skos:note`) or use `dcterms:type` with a value list. Still checked against the index for an exact standard term, but no deep search.
2. **Pattern** - the term does a job a neighbouring standard already models (catalogue record, versioning, mapping, annotation, provenance, classifier output). Full matching.
3. **Domain** - genuinely about online harms or the library's own editorial model. Checked for prior art (DPV, AIRO/VAIR, IPTC), expected to stay coined.

Output: `results/triage.csv`.

## C. Shortlist candidates per term

For each term, score every index row against the coined definition and example by word overlap (labels and definitions) plus embedding similarity, restricted to the matching kind where that is clear (class, property, individual). Keep the top 10 to 15 for reading. For terms in groups 1 and 2, also add the terms named in `vocab_jobs.csv` for that item.

## D. Judge fit by meaning

Read each shortlist, with the full definition, domain, range and parents from the index. Where the index definition is missing or thin (XKOS, some PROV-O), read the specification text. Judge each candidate as: exact fit; fits as superclass or superproperty; related but not a fit; irrelevant, with a one-line reason.

## E. Weigh adoption and interoperability

For each exact or parent-level fit:

- **Tier** from the specification's own status page (tier rules in `context/review-so-far.md`).
- **Profile weight** - does a consumer profile name it? Defaults while the library's consumers are unknown: DCAT-AP (data portals), schema.org (search engines), SKOS (thesaurus tools), with SSSOM (mapping tools) and RO-Crate as secondary.
- **Adoption numbers only to break close calls** - Web Data Commons usage counts for schema.org terms, or data.europa.eu SPARQL counts for DCAT-AP properties. A handful of lookups at most.

## F. Optional LOV sweep

One camelCase query per term with no good match in the index, to catch an unexpected vocabulary. Anything found only this way is a lead to cite, not to adopt.

## G. Report

As in `INSTRUCTIONS.md` Phase 6: `results/report.md` (summary, ten most consequential findings, uncovered vocabularies, errors in earlier reviews, one section per term with verdict and evidence status, explicit comparison with `context/review-so-far.md` for items 1 to 20) and `results/candidates.csv`.
