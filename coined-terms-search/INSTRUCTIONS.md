# Task: find existing RDF terms for the ontology's coined terms

## Background

The ontology `oht` (a schema for a library of online-harms taxonomies) coins 68 terms of its own. `context/COINED-TERMS-REVIEW.md` is an agent's assessment of each one: its meaning, an example, the nearest existing term and a verdict. A second review (a conversation with Claude) has covered items 1-20 and found the agent missed existing terms in about half of them, mostly by never looking at neighbouring standards (DCAT catalogue records, SSN/SOSA, Web Annotation, SSSOM and others). That review is summarised in `context/review-so-far.md`.

Your job is to search systematically for existing terms that could replace or anchor each coined term, using the Linked Open Vocabularies (LOV) API plus direct checks of vocabularies LOV doesn't index. Both earlier reviews relied mostly on recall from memory. This pass should rely on search and on checking definitions at source.

If you are running inside the ontology repository and `ontology/oht.ttl` exists, take each term's definition from there; it is authoritative. Otherwise use `context/COINED-TERMS-REVIEW.md`.

## Files

- `lov_search.py` - queries LOV term search, caches raw responses, merges and ranks candidates per term, looks up vocabulary details, writes `candidates.csv` and `summary.md`. Written against the LOV API docs and tested only against mock responses. Adapt it freely.
- `lov_queries.csv` - first-draft search phrases (short keywords) for all 68 terms.
- `calibration/known_answers.csv` - terms from items 1-20 where the right existing term is already known. Use these to test which query style works.
- `context/review-so-far.md` - verdicts and candidates for items 1-20, the vocabulary tiers, and which claims were verified by search versus recalled from memory.
- `context/vocab_jobs.csv` - vocabularies that should be checked for each job the ontology does. Namespaces marked `memory` must be confirmed.

LOV API documentation: https://lov.linkeddata.es/dataset/lov/api. Term search is `GET /dataset/lov/api/v2/term/search` with parameters `q` (full text), `type` (the docs spell it `propery`; test which spelling works), `vocab`, `page`, `page_size`.

## Rules

1. Proposals only. Do not edit `ontology/`, `MAPPING.md` or any decision record. Write everything to `results/` in this folder.
2. Verify every term you recommend against its defining document in this session (namespace document, specification or dereferenced IRI) and quote its definition briefly, with the URL. Never recommend a term from memory. If you can't verify something, say so explicitly.
3. Be polite to LOV: at least one second between calls, cache everything, keep the descriptive User-Agent, back off on errors or rate limits.
4. Use hyphens, not em dashes or en dashes, in all written output.
5. If something in these instructions turns out to be wrong (an API behaves differently, a namespace has moved), note it in `results/NOTES.md` and adapt rather than stopping.

## Phases

### Phase 0 - smoke test

- `pip install requests` (add `rdflib` when you need to parse vocabularies).
- Run one search (`q=catalog record`, `type=class`) and inspect the raw JSON. Check that the field names in `parse_result()` and `vocab_details()` match what LOV returns, and fix them if not.
- Find out whether `type=property` or `type=propery` works.
- Try to establish how LOV handles multi-word queries (any word, all words, phrase proximity, quoted phrases) by comparing a few result sets.
- Record findings in `results/NOTES.md`.

### Phase 1 - calibration (stop and report after this phase)

For each row in `calibration/known_answers.csv`, write queries in three styles, and in both British and American spelling where they differ:

- (a) short keywords, one to three words
- (b) a descriptive phrase of five to eight words drawn from the coined term's definition
- (c) an exact quoted phrase

Before scoring, check whether each expected vocabulary is indexed in LOV at all, so that "not indexed" is kept separate from "query missed". Score each style by how many expected IRIs appear in the top 15, and by mean rank. Normalise IRIs before comparing (http versus https, trailing `#` or `/`). Try combining styles too.

Write `results/calibration.md` with the table and a recommended query strategy. Then stop and report to the user before going further, unless they have told you to run end to end.

### Phase 2 - LOV coverage of candidate vocabularies

For each row in `context/vocab_jobs.csv`, check whether LOV indexes the vocabulary, and record LOV's latest version date for it. List the vocabularies LOV doesn't cover; they need direct checking in Phase 4.

### Phase 3 - full LOV search

Write `lov_queries_v2.csv` for all 68 terms using the winning strategy, with three to five phrasings per term. Include phrasings aimed at the job the term does, not just its name: "annotation motivation" finds more than "open question", and "catalog record" more than "record". Run the search.

### Phase 4 - direct checks outside LOV

For each vocabulary in the Phase 2 gap list, fetch its specification or namespace document, parse its terms where possible, and look for matches to each coined term's job.

### Phase 5 - judge fit by meaning

Keyword scores measure word overlap, not fit. For each coined term:

- Pool the candidates from Phases 3 and 4.
- Fetch each plausible candidate's definition from its authoritative source. Dereference the IRI with `Accept: text/turtle` and read `rdfs:comment`, `skos:definition` or `dcterms:description`, or read the spec.
- Judge each candidate against the coined term's definition and example as one of: exact fit; fits as superclass or superproperty; related but not a fit; irrelevant. Give a one-line reason. Embedding similarity may be used to order the pool first, but the judgement is yours.
- Assign each vocabulary a tier using the rules in `context/review-so-far.md`, checking status on the specification's own page.

### Phase 6 - report

Write `results/report.md`:

- A summary at the top: counts by proposed verdict; the ten most consequential findings; vocabularies LOV doesn't index; and any errors you found in either earlier review.
- One section per coined term, in item order, containing:
  - the coined definition, in one line
  - the best candidates: IRI, vocabulary, tier, a short quoted definition with source URL, and your fit judgement
  - a proposed verdict: Keep, Keep under a standard superclass or superproperty, Replace, or Drop
  - evidence status: verified at source, or not verified and why
- For items 1-20, compare your findings with `context/review-so-far.md` and state agreements and disagreements explicitly. Don't defer to it; it may be wrong.

Also write `results/candidates.csv` with every candidate considered and its judgement.
