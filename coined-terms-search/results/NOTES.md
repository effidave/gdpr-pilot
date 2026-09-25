# Notes: how LOV actually behaves (Phase 0 and Phase 1)

All checks run on 2026-09-25 against the live service. Raw responses are cached under `probe/` and `results/calibration_raw/`.

## Instructions or docs that turned out to be wrong

1. **The API has moved.** `https://lov.linkeddata.es/dataset/lov/api/v2/...` returns HTTP 404 (an HTML page), as does everything under `/dataset/lov/`. The working base is `https://lov.linkeddata.es/dataset/api/v2`. The API docs page is now `https://lov.linkeddata.es/dataset/api`, and its own examples use the new path. The SPARQL endpoint is at `https://lov.linkeddata.es/dataset/sparql` (the old `/dataset/lov/sparql` redirects there). `lov_search.py` is patched.
2. **`type=propery` does not work.** It is silently ignored: the response echoes `filters: {type: "propery"}` but returns the unfiltered result set (377 results for `q=version`, same as no filter, and classes first). `type=property` works (298 results, all properties). The docs' spelling is a typo. `lov_search.py` already sent `property`; its docstring is corrected.
3. **Field names in `parse_result()` were wrong.** Live results are scalars, not single-item lists, and nest objects rather than using dotted keys:
   `{"type": "class", "uri": ..., "prefixedName": "dcat:CatalogRecord", "tags": [...], "vocabulary": {"prefix": "dcat"}, "metrics": {"occurrencesInDatasets": 0, "reusedByDatasets": 0, ...}, "score": 16.6, "highlight": {"labelsWithoutLang": ["<b>catalog</b>"]}}`.
   `parse_result()` now reads `vocabulary.prefix` and `metrics.*` from the nested objects. `vocab_details()` was already right: `/vocabulary/info` returns `titles: [{value, lang}]` and `versions: [{name, issued, ...}]`.
4. **`type=instance` is ignored**, and LOV appears to index no instances at all: the type facet only ever shows `class`, `property` and `datatype`. `q=questioning` returns 0 results. So named individuals (`oa:questioning` and the other Web Annotation motivations, SKOS concept values such as NKOS KOS types, the EU access-right table, SSSOM's `sssom:NoTermFound`) cannot be found through LOV and must be checked directly. The calibration note on item 8 ("do not filter by type") is moot for this reason: the expected instance is not there to find.
5. **Multi-value type filters (`type=class,property`) are ignored** (response shows `filters: {}`).
6. **The `vocab=` filter silently drops every property.** With `vocab=prov`, `q=hadPrimarySource` returns 0 results, `q=source` returns only the class `prov:PrimarySource`, and `q=source&type=property` returns 0. The same happens for `schema` (`expires`), `cito` (`citesAsAuthority`) and `disco` (`analysisUnit`, only the class `disco:AnalysisUnit` comes back). Workaround: search unfiltered with a large `page_size` (1000 is accepted in one call) and filter by `vocabulary.prefix` locally. One call per query, so it is also politer than one call per vocabulary.
7. `/term/search/metadata` is documented as a lookup of one term, but behaves as a full-text search that tokenises the IRI (`q=http://www.w3.org/ns/dcat#CatalogRecord` returns 33 results, led by `nco:org` and `http:httpVersion`). To test whether an IRI is indexed, search its local name and compare IRIs.

## What LOV searches, and how

- **Only names are indexed, not definitions.** Across about 2,000 results from 160 queries the `highlight` field only ever named `labelsWithoutLang`, `labelsWithoutLang.keyword`, `localName.ngram` and `vocabulary.prefix`. No comment, definition or description field ever matched. Pasting a definition sentence (for example DCAT's own "A record in a catalog, describing the registration of a single resource") does not find the term it defines. This is the single most important fact for query design.
- **Labels are tokenised as written.** PROV's label for `prov:hadPrimarySource` is the camelCase string `hadPrimarySource`, one token, so `q=primary source` misses it entirely (it is not among any of the 494 results), while `q=primarySource` and `q=hadPrimarySource` put it first. Vocabularies with proper English labels ("catalog record") are found by keywords; vocabularies whose labels are local names (PROV, CiTO, much of DUV) are found by camelCase queries.
- **Local names get n-gram matching**, so a camelCase fragment finds longer names: `primarySource` finds `hadPrimarySource` and `qualifiedPrimarySource`; `CatalogRecord` finds `mod:SemanticArtefactCatalogRecord`.
- **Multi-word queries are OR with a proximity or order boost.** `catalog record` returns 122 results, `record catalog` 121, and only the first puts `dcat:CatalogRecord` in the top 3; long queries return thousands of results (6,000+ for a sentence), with stopwords such as "a", "of" and "in" matching labels like "Element A". AND/OR operators are treated as words (`catalog AND record` 278, `catalog OR record` 623).
- **Quotes and `+` are stripped.** `"catalog record"` and `+catalog +record` return exactly the same list as `catalog record`. There is no phrase search.
- **Matching is case-insensitive.**
- **Common words drown the standard term.** `q=annotation` has 180 hits; `oa:Annotation` is 11th among classes and outside the unfiltered top 15, behind a dozen `annotation` and `hasAnnotation` properties from other vocabularies.
- **Spelling matters.** DCAT uses US spelling. `catalogue record` finds ArCo's `ctlog:CatalogueRecord` (Italian cultural heritage) and never DCAT. `expiry date` and `expiration date` both miss `schema:expires`.
- **The same IRI can appear twice under two prefixes.** LOV files the DCAT namespace under both `dcat` and `aerdcat`, and SSN under `ssn`, `ssno` and `w3c-ssn`. Merge candidates by normalised IRI, not by prefixed name.
- **Scores are not comparable across queries.** Single-word queries score about 50 to 70; two-word queries about 15 to 20.

## LOV's copies of key vocabularies are old

From `/vocabulary/info` (latest `issued` date among the versions LOV holds):

| Prefix | Latest version in LOV | Consequence |
|---|---|---|
| dcat | 2020-02-04 (DCAT 2) | DCAT 3 (2024) terms are absent: `dcat:version`, `dcat:previousVersion`, `dcat:hasVersion`, `dcat:isVersionOf`, `dcat:hasCurrentVersion` all return nothing. Item 2's expected answers are "not indexed", not "missed". |
| schema | v7.0, 2020-03-10 | `schema:hasDefinedTerm` is not found (item 18). Newer schema.org terms need direct checking. |
| prov | 2015-01-11 | Fine for PROV-O, which has not changed. |
| oa | 2016-11-12 (W3C Recommendation) | Classes and properties present; its instances (motivations) are not indexed. |
| ssn | 2011-06-20 label, but the namespace listed is `http://www.w3.org/ns/ssn/` and `ssn:Output`, `ssn:hasOutput` are found. Treat LOV's version metadata for SSN as unreliable. |
| duv | 2016-08-30 | Present. |
| cito | 2018-02-16 (v2.8.1) | Present. |
| disco | 2013 (v0.6) | Present. |

`sssom` is not in LOV at all.

## Politeness

Every call goes through the cached `call()` in `lov_search.py` with the descriptive User-Agent, at least 1.2 seconds between live calls, and retries with backoff. No errors or rate limiting were seen. Phase 0 and 1 used roughly 230 live calls.

## Adoption metrics in LOV (checked 2026-09-25)

- The REST API has no adoption ranking. `/vocabulary/list` returns only uri, nsp, prefix, titles, versions and artifacts. `/vocabulary/info` has a `datasets` list (dataset name plus occurrences) and `incomRel*` fields, but the incoming-relation fields were empty for dcat, prov, schema and skos.
- The SPARQL endpoint does carry per-vocabulary figures: `voaf:reusedByVocabularies`, `voaf:reusedByDatasets` and `voaf:occurrencesInDatasets`. One query returns them all (saved to `results/lov_vocab_metrics.json`). 364 of about 1,400 vocabulary rows have a non-zero figure.
- The figures are stale and unusable as an adoption measure for this task. The dataset counts come from old Linked Open Data crawls (datahub.io dataset names). DCAT has no figures at all; schema.org shows 12 reusing datasets; DUV, DQV, DPV and ML Schema show 0; SSSOM, DCAT-AP and NKOS are not in LOV. The ranking is led by rdf, rdfs, dcterms, dc elements, owl, foaf and skos, which is right but already obvious.
- `reusedByVocabularies` (how many other LOV vocabularies import or reuse a vocabulary) is the more meaningful of the two, but measures reuse by ontology authors, not by data publishers or consuming tools.
