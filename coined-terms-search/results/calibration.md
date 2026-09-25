# Phase 1 calibration: which LOV query style finds the known answers

Inputs: the 11 rows of `calibration/known_answers.csv`. Queries: `calibration/calibration_queries.csv` (83 phrasings). Scripts: `calibrate.py`, `calibrate_scoped.py`, `score_calibration.py`. Raw results: `results/calibration_results.json`, `results/calibration_scoped.json`, cached responses in `results/calibration_raw/`. Background on LOV's behaviour: `NOTES.md`.

IRIs were normalised before comparison (`https` to `http`, trailing `#` and `/` removed). A hit means an expected IRI in the top 15.

## Step 1 - is the expected answer in LOV at all?

Checked by searching each expected IRI's local name, in its vocabulary and unfiltered, and comparing IRIs.

| # | Coined term | Expected IRI(s) | Indexed in LOV? |
|---|---|---|---|
| 1 | oht:Record | dcat:CatalogRecord | yes |
| 2 | oht:Version | dcat:version, previousVersion, hasVersion, isVersionOf | **no** - LOV holds DCAT 2 (2020); these are DCAT 3 terms |
| 5 | oht:OutputSpec | ssn:Output, ssn:hasOutput | yes |
| 6 | oht:Uptake | duv:Usage, duv:hasUsage | yes |
| 7 | oht:NoMatch | sssom:NoTermFound | **no** - SSSOM is not in LOV (as the calibration file predicted) |
| 8 | oht:OpenQuestion | oa:Annotation, oa:questioning | Annotation yes; **questioning no** (LOV indexes no instances) |
| 10 | oht:Session | schema:Conversation | yes |
| 12 | oht:classifies | disco:analysisUnit | yes |
| 16 | oht:sunsetDate | schema:expires | yes |
| 18 | oht:hasConcept | schema:hasDefinedTerm | **no** - LOV holds schema.org v7.0 (2020) |
| 19 | oht:primarySource | cito:citesAsAuthority, prov:hadPrimarySource | yes |

So 8 of 11 rows are findable. Rows 2, 7 and 18 are LOV coverage gaps, not query misses, and their vocabularies go on the Phase 4 list. That is itself a finding: 3 of 11 known answers (27%) are unreachable through LOV, two of them because LOV's copy of a live standard is years out of date.

## Step 2 - styles tested

- (a) short keywords, 1 to 3 words (`catalog record`, `usage`, `expires`)
- (b) descriptive phrase, 5 to 8 words from the definition (`how a classifier reports a concept`)
- (c) exact quoted phrase (`"catalog record"`)
- (d) job phrase - what the term does in a neighbouring standard (`dataset usage`, `annotation motivation`, `cites as authority`)
- (e) camelCase local name, as a standard would likely name it (`CatalogRecord`, `hasUsage`, `primarySource`)
- (f) styles a, d and e, but with results kept only from the vocabularies `context/vocab_jobs.csv` lists for the item (fetched as one deep unfiltered page of up to 1000 and filtered locally, because LOV's own `vocab=` filter drops all properties)

British and American spellings were run separately where they differ (catalog/catalogue; expiry/expiration). Each open query (a to e) was run both with the row's type filter and without.

## Step 3 - results

### By style, open search (no type filter)

| Style | Queries | Queries that hit | Items hit (of 8 indexed) | Mean best rank of hits | Items hit |
|---|---|---|---|---|---|
| (a) short keywords | 24 | 7 | 6 | 2.5 | 1, 5, 6, 10, 12, 16 |
| (b) descriptive phrase | 23 | 1 | 1 | 1.0 | 19 |
| (c) quoted phrase | 13 | 3 | 3 | 2.0 | 1, 6, 12 |
| (d) job phrase | 13 | 2 | 2 | 1.5 | 6, 19 |
| (e) camelCase local name | 22 | 8 | 6 | 2.3 | 1, 5, 6, 10, 12, 19 |
| (a) + (e) | 46 | 15 | 7 | 1.9 | 1, 5, 6, 10, 12, 16, 19 |
| (a) + (d) | 37 | 9 | 7 | 2.1 | 1, 5, 6, 10, 12, 16, 19 |
| (a) + (d) + (e) | 59 | 17 | 7 | 1.9 | 1, 5, 6, 10, 12, 16, 19 |
| all open styles | 95 | 21 | 7 | 1.9 | 1, 5, 6, 10, 12, 16, 19 |

### Scoped to the item's job vocabularies (style f)

| Styles inside scope | Items hit (of 8 indexed) | Mean best rank | Items hit |
|---|---|---|---|
| (a) short keywords | 6 | 1.2 | 1, 5, 6, 10, 12, 16 |
| (d) job phrase | 5 | 1.0 | 5, 6, 8, 12, 19 |
| (e) camelCase | 7 | 1.0 | 1, 5, 6, 8, 10, 12, 19 |
| (a) + (d) + (e) | **8** | **1.0** | 1, 5, 6, 8, 10, 12, 16, 19 |

### By item (best rank in open search, unfiltered; "-" = not in top 15)

| # | Term | (a) | (b) | (c) | (d) | (e) | (f) scoped | Best open query |
|---|---|---|---|---|---|---|---|---|
| 1 | oht:Record | 3 | - | 3 | - | 1 | 1 | `CatalogRecord` |
| 2 | oht:Version | not indexed | | | | | | |
| 5 | oht:OutputSpec | 6 | - | - | - | 8 | 1 | `output` |
| 6 | oht:Uptake | 3 | - | 2 | 2 | 2 | 1 | `dataset usage` |
| 7 | oht:NoMatch | not indexed | | | | | | |
| 8 | oht:OpenQuestion | - | - | - | - | - | 1 | none (`annotation` puts oa:Annotation 11th among classes, below 15 unfiltered) |
| 10 | oht:Session | 1 | - | - | - | 1 | 1 | `conversation` |
| 12 | oht:classifies | 1 | - | 1 | - | 1 | 1 | `unit of analysis` |
| 16 | oht:sunsetDate | 1 | - | - | - | - | 1 | `expires` |
| 18 | oht:hasConcept | not indexed | | | | | | |
| 19 | oht:primarySource | - | 1 | - | 1 | 1 | 1 | `primarySource`, `cites as authority` |

### Other effects

- **Type filter:** across 69 paired queries it improved the rank 3 times (item 1, rank 3 to 1; item 19, 2 to 1) and lost the answer 4 times, each time because the expected answer was the other type (`hasOutput` and `hasUsage` are properties, the row was typed class). Several coined terms have a class-plus-property answer (items 5, 6), so filtering by type costs more than it gains. Leave it off.
- **Spelling:** British spelling lost the answer every time. `catalogue record` and `CatalogueRecord` find ArCo's catalogue classes, never DCAT; `expiry date` and `expiration date` both miss `schema:expires`, which only `expires` finds. Standards are overwhelmingly in American spelling and verb-style names; British variants are worth one phrasing per term at most.
- **Quoted phrases** are identical to the unquoted query (LOV strips the quotes), so style (c) adds nothing and has been dropped.
- **Descriptive phrases** (b) hit once, and only because the phrase happened to echo CiTO's label ("cites as authority"). LOV does not index definitions, so definition-derived queries are the wrong tool here; definition matching belongs in Phase 5, done by reading.

## Recommended strategy for Phase 3

1. **No descriptive or quoted queries.** Spend the phrasings on names.
2. **Three to five phrasings per term, mixing:**
   - one or two short keyword phrases in American spelling, naming the job in the words a standard would use (`catalog record`, `usage`, `expires`, `unit of analysis`);
   - one or two camelCase local-name guesses, as class and property forms (`CatalogRecord`, `hasUsage`, `primarySource`, `wasRevisionOf`); the n-gram matching means a shorter core (`primarySource`) also catches prefixed forms (`hadPrimarySource`);
   - at most one British variant where the word differs.
3. **Run every phrasing twice from one call:** request `page_size=1000` unfiltered, then
   - take the open top 15 (for discovery beyond the known vocabularies), and
   - take the top 15 among the item's job vocabularies from `vocab_jobs.csv` plus all tier 1 vocabularies (scoped view).
   The scoped view was the only approach that found all 8 indexed answers, all at rank 1. The open view is kept so that vocabularies not on the list still surface.
4. **No type filter, and never the `vocab=` filter** (it drops properties).
5. **Merge by normalised IRI,** since LOV lists some namespaces under two or three prefixes (dcat/aerdcat, ssn/ssno/w3c-ssn), and rank by best position rather than by raw score, because scores are not comparable across queries of different lengths.
6. **Expect LOV to miss individuals and anything newer than about 2020** (DCAT 3, recent schema.org, SSSOM, the Web Annotation motivations, KOS type values). Those go to Phase 4 direct checks, not to more query tuning.

Caveat: the scoped view's perfect score is partly circular, since `vocab_jobs.csv` was assembled by people who already knew these answers. For items 21 to 68 its value depends on how complete the job-to-vocabulary map is, which is why the open view stays in.

## Changes made to `lov_search.py`

- Base URL corrected to `/dataset/api/v2`.
- `parse_result()` reads the nested `vocabulary` and `metrics` objects.
- Docstring corrected about `propery`.

Not yet done (Phase 3): add the deep-page scoped view and rank-based merging described above.
