SUMMARY = """### Ten most consequential findings

1. **Catalogue records and versions should be DCAT 3 (items 1, 2, 57).** `dcat:CatalogRecord` with `foaf:primaryTopic`, and DCAT 3's `dcat:hasVersion`, `dcat:version`, `dcat:previousVersion` and `dcat:hasCurrentVersion`. This is the single biggest interoperability gain: DCAT-AP 3, which EU data portals harvest, makes `foaf:primaryTopic` and `dcterms:modified` mandatory on a catalogue record and names `dcat:version` on datasets.
2. **Mappings should follow SSSOM (items 7, 45, 46, 47, 48).** The mapping relation should be the SKOS mapping property itself (`skos:exactMatch`, `skos:closeMatch` and so on) rather than a local value list; "no counterpart" is `sssom:NoTermFound`; numeric confidence is `sssom:confidence`; how a crosswalk was made is `sssom:mapping_justification` with SEMAPV values. SEMAPV already has an "LLM-based matching process" value, so the library's `llm_assisted` method has a standard home.
3. **Open questions are Web Annotations (items 8, 55, 56).** `oa:Annotation` motivated by `oa:questioning`, resolved by a reply motivated by `oa:replying`, now verified in the W3C vocabulary file itself.
4. **Nine provenance shortcuts can go (items 9, 10, 20, 50, 54, 60, 64, 66, 67).** Each restates a PROV-O relation read backwards (`prov:used`, `prov:wasAssociatedWith`, `prov:generated`, `prov:wasDerivedFrom`) or a path already in the graph.
5. **Six type slots become `dcterms:type` (items 11, 22, 28, 33, 43, 61),** each being the only type slot on its resource. Local value lists stay, aligned where possible (NKOS KOS types, IAO's "terms merged" and "term split").
6. **Seven note-like or date-like terms stay but get a standard parent (items 13, 15, 21, 27, 31, 52, 59):** `dcterms:description`, `dcterms:date`, `dcterms:hasPart` or `skos:scopeNote`, so generic tools still read them.
7. **`oht:Uptake` should stay coined (items 6, 42).** DUV defines `duv:Usage` as "a helpful description of actions that can be performed on a given dataset", which is guidance for users, not evidence that someone used a scheme. The second review's proposed subclass would misstate the meaning.
8. **New anchors neither review found:** `oht:hasFacetValue` fits under `xkos:classifiedUnder`, which XKOS defines as a generic property to be specialised (item 30); `oht:Axis` can also align to `schema:DefinedTermSet` (item 4); modality values can come from the DCMI Type Vocabulary (item 35); the `llm_drafted` derivation value aligns to IPTC's "Created using Generative AI", which schema.org's `digitalSourceType` uses (item 49); archived excerpts can be typed `bibo:Excerpt` (item 67).
9. **Classifier outputs via SSN/SOSA, as subclasses (items 5, 32).** Type the classifier `sosa:Procedure` (SOSA explicitly includes algorithms), link with `ssn:hasOutput`, and make `oht:OutputSpec` a subclass of `ssn:Output` so the output type and axis still have a home.
10. **Access and redistribution use `dcterms:accessRights` with the EU access-right table (items 58, 65),** as DCAT-AP does, with ODRL's `odrl:distribute` available if exact redistribution terms are needed.

### Adoption weighting

The library's consumers are not yet known, so candidates were weighted towards DCAT-AP (data portals), schema.org (search engines) and SKOS (thesaurus tools), with SSSOM and RO-Crate second. Where a candidate is named in DCAT-AP 3's SHACL shapes or the RO-Crate 1.2 context, the term section says so. No usage counts were needed to break a tie.

### Vocabularies LOV does not index, or holds out of date

- **Not in LOV:** DCAT-AP, NKOS Application Profile and KOS Types, skos-history, ISO 25964 dataset versioning, SSSOM, SEMAPV, the EU access-right table, RO-Crate, DPV's RISK and AI extensions, IPTC Digital Source Type (`results/lov_coverage.csv`).
- **In LOV but stale:** LOV's `dcat` entry is DCAT 2 (2020), so no DCAT 3 versioning terms (the 2025 date in the coverage table belongs to `aerdcat`, a separate entry that reuses the DCAT namespace); schema.org is v7.0 (2020), so `schema:hasDefinedTerm` is missing; no named individuals are indexed anywhere, so `oa:questioning` and every value vocabulary are unsearchable.
- **Not available anywhere:** ISO 25964 dataset versioning (`http://purl.org/iso25964/DataSet/Versioning` returns 404). The NKOS namespaces redirect to a workshop page, so the KOS type IRIs cannot be dereferenced.

### Errors found in the earlier reviews

- **Second review, item 2:** `dcat:isVersionOf` is not a DCAT 3 term. DCAT 3 removed it from the vocabulary specification ("properties dcat:isVersionOf, dcat:next, and dcterms:isReplacedBy have been removed from 6. Vocabulary specification"); use `dcterms:isVersionOf` for a back link.
- **Second review, item 6:** `duv:Usage` is usage guidance, so `oht:Uptake` should not be its subclass (finding 7).
- **Second review, item 16:** `schema:expires` is declared on `CreativeWork` and `Certification`; it fits schemes but not services such as the Perspective API, which the example uses.
- **First review, items 36 and 39:** `eli:implements` and `eli:implemented_by` are deprecated in current ELI ("This property is deprecated. Use \\"applies\\" instead.").
- **First review, item 59:** `dcterms:provenance` is defined as "changes in ownership and custody"; redactions are content edits, so a note-type parent fits better.
- **First review, items 2 and 57:** confirmed that ADMS has no `adms:version` property (its 18 terms include `versionNotes`, `prev`, `next` and `last`, not `version`), as the second review said.
- **Tier list:** the W3C ADMS Note was retired in August 2023, so cite SEMIC's ADMS (as the second review's tier list does), not the W3C Note. The latest W3C edition of OWL-Time is a Candidate Recommendation Draft (2022); the 2017 edition is a Recommendation, so tier 1 still holds.
- **Lead from this review's own seed list:** `pav:createdAt` is not a date (PAV defines it as the geo-location of the creating agent). It was checked and rejected (item 25).
""".splitlines()
