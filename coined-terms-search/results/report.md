# Existing terms for the 68 coined oht: terms

Proposals only; nothing in the ontology has been changed. Method: `PLAN.md`. Every definition quoted below was read from the publisher's own file or specification in this session (`index/SOURCES.md`); the source is given per candidate. Definitions of the coined terms come from `context/COINED-TERMS-REVIEW.md`, because `ontology/oht.ttl` is not in this repository.

## Summary

### Proposed verdicts

| Verdict | Terms |
|---|---|
| Replace | 26 (1, 2, 7, 8, 9, 10, 11, 16, 19, 22, 24, 28, 32, 33, 38, 43, 45, 47, 48, 56, 57, 58, 61, 62, 65, 68) |
| Drop | 10 (18, 20, 40, 50, 54, 55, 60, 64, 66, 67) |
| Keep under standard superclass or superproperty | 10 (4, 5, 13, 15, 21, 27, 30, 31, 52, 59) |
| Keep | 22 (3, 6, 12, 14, 17, 23, 25, 26, 29, 34, 35, 36, 37, 39, 41, 42, 44, 46, 49, 51, 53, 63) |

Replace or drop: 36. Keep, with or without a standard parent: 32. Taken together, the ontology would shrink from 68 coined terms to 32, of which 10 are anchored to a standard parent.

### Ten most consequential findings

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
- **First review, items 36 and 39:** `eli:implements` and `eli:implemented_by` are deprecated in current ELI ("This property is deprecated. Use \"applies\" instead.").
- **First review, item 59:** `dcterms:provenance` is defined as "changes in ownership and custody"; redactions are content edits, so a note-type parent fits better.
- **First review, items 2 and 57:** confirmed that ADMS has no `adms:version` property (its 18 terms include `versionNotes`, `prev`, `next` and `last`, not `version`), as the second review said.
- **Tier list:** the W3C ADMS Note was retired in August 2023, so cite SEMIC's ADMS (as the second review's tier list does), not the W3C Note. The latest W3C edition of OWL-Time is a Candidate Recommendation Draft (2022); the 2017 edition is a Recommendation, so tier 1 still holds.
- **Lead from this review's own seed list:** `pav:createdAt` is not a date (PAV defines it as the geo-location of the creating agent). It was checked and rejected (item 25).

## Terms

### 1. `oht:Record`

**Coined definition:** a named graph holding one library record; the library's statements are made about this IRI. (Triage group: pattern.)

**Proposed verdict: Replace.** Use dcat:CatalogRecord, with foaf:primaryTopic pointing at the scheme; the named graph can carry the record's IRI.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `dcat:CatalogRecord` (DCAT 3) | 1 | "A record in a data catalog, describing the registration of a single dataset or data service." [source](https://www.w3.org/ns/dcat.ttl) | **exact fit**. A record describing the registration of one resource in a catalogue is exactly what the library's record is; the named-graph mechanism is an implementation choice DCAT does not forbid. |
| `foaf:primaryTopic` (FOAF) | 2 | "The primary topic of some page or document." [source](http://xmlns.com/foaf/spec/index.rdf) | **exact fit**; named in DCAT-AP 3 (mandatory). DCAT-AP 3 makes foaf:primaryTopic mandatory on a catalogue record (along with dcterms:modified), so portals expect it. |
| `prov:Entity` (PROV-O) | 1 | "An entity is a physical, digital, conceptual, or other kind of thing with some fixed aspects; entities may be real or imaginary." [source](https://www.w3.org/ns/prov.ttl) | **fits as superclass or superproperty**. True but too general to help consumers. |
| `dcat:Dataset` (DCAT 3) | 1 | "A collection of data, published or curated by a single source, and available for access or download in one or more representations." [source](https://www.w3.org/ns/dcat.ttl) | **related but not a fit**. Describes the scheme itself, not the library's record about it. |

**Evidence:** `dcat:CatalogRecord`: verified at source; `foaf:primaryTopic`: verified at source; `prov:Entity`: verified at source

**Against the second review:** Agrees with the second review (Replace). The first review's objection that DCAT cannot distinguish 'a graph the library curates' is answered by dcat:CatalogRecord itself. If SHACL needs its own target class, declare oht:Record rdfs:subClassOf dcat:CatalogRecord.

### 2. `oht:Version`

**Coined definition:** one published release of a taxonomy; concept IRIs stay stable across versions. (Triage group: pattern.)

**Proposed verdict: Replace.** Use DCAT 3 versioning: dcat:hasVersion from the abstract scheme, dcat:version for the label, dcat:previousVersion for the chain, dcat:hasCurrentVersion for the latest.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `dcat:hasVersion` (DCAT 3) | 1 | "This resource has a more specific, versioned resource [PAV]." [source](https://www.w3.org/ns/dcat.ttl) | **exact fit**. Links the stable, version-independent scheme to each release, which is the oht:Version pattern. |
| `dcat:version` (DCAT 3) | 1 | "The version indicator (name or identifier) of a resource." [source](https://www.w3.org/ns/dcat.ttl) | **exact fit**; named in DCAT-AP 3 (not mandatory). The release label ("2023"); DCAT-AP 3 names it on dcat:Dataset. |
| `dcat:previousVersion` (DCAT 3) | 1 | "The previous version of a resource in a lineage [PAV]." [source](https://www.w3.org/ns/dcat.ttl) | **exact fit**. Version chain. |
| `dcat:hasCurrentVersion` (DCAT 3) | 1 | "This resource has a more specific, versioned resource with equivalent content [PAV]." [source](https://www.w3.org/ns/dcat.ttl) | **exact fit**. Points at the latest release. |
| `dcat:isVersionOf` (DCAT 3) | 1 | "properties dcat:isVersionOf, dcat:next, and dcterms:isReplacedBy have been removed from 6. Vocabulary specification [it survives only in the informative table of inverses and in section 11 prose]" [source](https://www.w3.org/TR/vocab-dcat-3/) | **related but not a fit**. Removed from the DCAT 3 vocabulary specification; only listed as an informative inverse. Use dcterms:isVersionOf if a back link is stored. |
| `dcterms:isVersionOf` (DCMI Terms) | 1 | "A related resource of which the described resource is a version, edition, or adaptation." [source](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl) | **fits as superclass or superproperty**. The standard back link from a version to the work. |
| `adms:versionNotes` (ADMS) | 2 | "A description of changes between this version and the previous version of the Asset." [source](https://www.w3.org/ns/adms.ttl) | **related but not a fit**; named in DCAT-AP 3 (not mandatory). Change notes between versions; useful alongside, SEMIC ADMS 2.0. |
| `pav:version` (PAV) | 2 | "The version number of a resource. This is a freetext string, typical values are "1.5" or "21". The URI identifying the previous version can be provided using prov:previousVersion. This property is normally used in a functional way, although PAV does not ..." [source](http://purl.org/pav/) | **related but not a fit**. Same idea as dcat:version, tier 2; prefer DCAT. |

**Evidence:** `dcat:hasVersion`: verified at source; `dcat:version`: verified at source; `dcat:previousVersion`: verified at source; `dcat:hasCurrentVersion`: verified at source; `dcterms:isVersionOf`: verified at source

**Against the second review:** Agrees with the second review (Replace) except on dcat:isVersionOf, which DCAT 3 removed from its vocabulary specification (appendix of changes); the second review lists it as a DCAT 3 term. DCAT 3 has no Version class: versions are ordinary resources, so if a class is needed for SHACL, subclass dcat:Resource or dcat:Dataset.

### 3. `oht:Change`

**Coined definition:** one change a version made (added, removed, renamed, moved and so on). (Triage group: pattern.)

**Proposed verdict: Keep.** No standard class for one change in a changelog; cite skos-history as prior art.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `sh:SchemeDelta` (skos-history) | 3 | "The delta of two versions of a SKOS concept scheme." [source](http://purl.org/skos-history/) | **related but not a fit**. A whole delta between two scheme versions, not one change; tier 3. |
| `prov:Revision` (PROV-O) | 1 | "A revision is a derivation for which the resulting entity is a revised version of some original. The implication here is that the resulting entity contains substantial content from the original. Revision is a particular case of derivation." [source](https://www.w3.org/ns/prov.ttl) | **related but not a fit**. A qualified derivation between two entity versions, not a changelog entry. |
| `schema:UpdateAction` (schema.org) | 2 | "The act of managing by changing/editing the state of the object." [source](https://schema.org/version/latest/schemaorg-current-https.ttl) | **related but not a fit**; named in the RO-Crate 1.2 context. An action (activity); typing issuer changelog entries as activities mixes them with the library's own provenance, as the first review argued. |
| `skos:changeNote` (SKOS) | 1 | "A note about a modification to a concept." [source](http://www.w3.org/2004/02/skos/core.rdf) | **related but not a fit**. Free-text note; could carry a human-readable summary of the change. |

**Evidence:** no standard term recommended; candidates read at source and judged not to fit.

**Against the second review:** Agrees with both reviews (Keep, skos-history as prior art).

### 4. `oht:Axis`

**Coined definition:** a classification dimension other than the hierarchy, as a small concept scheme of values. (Triage group: pattern.)

**Proposed verdict: Keep under standard superclass or superproperty.** Declare oht:Axis rdfs:subClassOf skos:ConceptScheme.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `skos:ConceptScheme` (SKOS) | 1 | "A set of concepts, optionally including statements about semantic relationships between those concepts." [source](http://www.w3.org/2004/02/skos/core.rdf) | **fits as superclass or superproperty**. An axis is a small set of values, which is a concept scheme; SKOS tools then read axes. |
| `qb:DimensionProperty` (RDF Data Cube) | 1 | "The class of components which represent the dimensions of the cube" [source](http://purl.org/linked-data/cube) | **related but not a fit**. Analogue from statistics: a dimension with a code list; it is a property class, not a scheme. |
| `xkos:ClassificationLevel` (XKOS) | 2 | "(none in file)" [source](http://rdf-vocabulary.ddialliance.org/xkos) | **related but not a fit**. Levels of one hierarchy, not orthogonal dimensions. |
| `schema:DefinedTermSet` (schema.org) | 2 | "A set of defined terms, for example a set of categories or a classification scheme, a glossary, dictionary or enumeration. Use the about property to specify what the term set is about." [source](https://schema.org/version/latest/schemaorg-current-https.ttl) | **fits as superclass or superproperty**; named in the RO-Crate 1.2 context. schema.org's 'set of categories or a classification scheme'; optional extra alignment for web consumers. |

**Evidence:** `skos:ConceptScheme`: verified at source; `schema:DefinedTermSet`: verified at source

**Against the second review:** Agrees with the second review. qb:DimensionProperty is now verified at source (it was memory).

### 5. `oht:OutputSpec`

**Coined definition:** how a classifier reports a concept (boolean, probability, ordinal, score). (Triage group: pattern.)

**Proposed verdict: Keep under standard superclass or superproperty.** Declare oht:OutputSpec rdfs:subClassOf ssn:Output, with the classifier typed sosa:Procedure.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `ssn:Output` (SSN) | 1 | "Any information that is reported from a Procedure." [source](https://www.w3.org/ns/ssn/) | **fits as superclass or superproperty**. In SSN, Output describes what a Procedure reports; an output specification is a kind of that. The coined class adds the output type and axis. |
| `sosa:Procedure` (SOSA) | 1 | "A workflow, protocol, plan, algorithm, or computational method specifying how to make an Observation, create a Sample, or make a change to the state of the world (via an Actuator). A Procedure is re-usable, and might be involved in many Observations, ..." [source](https://www.w3.org/ns/sosa/) | **exact fit**. SOSA's Procedure explicitly includes algorithms and computational methods, so a classifier fits. |
| `mls:Model` (ML Schema) | 2 | "Model is a generalization of a set of training data able to predict values for unseen instances. It is an output from an execution of a data mining algorithm implementation. Models have a dual nature. They can be treated as data structures and as such ..." [source](http://www.w3.org/ns/mls) | **related but not a fit**. ML Schema models are outputs of runs, not descriptions of a model's output format. |
| `schema:PropertyValueSpecification` (schema.org) | 2 | "A Property value specification." [source](https://schema.org/version/latest/schemaorg-current-https.ttl) | **related but not a fit**; named in the RO-Crate 1.2 context. Constraints on form inputs. |

**Evidence:** `ssn:Output`: verified at source; `sosa:Procedure`: verified at source

**Against the second review:** Partly agrees with the second review: same vocabulary, but I propose a subclass rather than outright replacement, because ssn:Output alone does not say boolean versus probability versus ordinal. This also moves the output onto the classifier, as the second review said.

### 6. `oht:Uptake`

**Coined definition:** one piece of evidence that someone uses the scheme (regulatory citation, platform adoption, benchmark use). (Triage group: pattern.)

**Proposed verdict: Keep.** duv:Usage is usage guidance, not evidence of use; keep oht:Uptake, and optionally assert nkos:usedBy for the simple case.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `duv:Usage` (DUV) | 2 | "A helpful description of actions that can be performed on a given dataset or distribution." [source](https://www.w3.org/ns/duv.ttl) | **related but not a fit**. Defined as 'a helpful description of actions that can be performed on a given dataset': instructions, not evidence that someone used it. |
| `nkos:usedBy` (NKOS Application Profile) | 3 | "Agent using the described KOS." [source](http://w3id.org/nkos) | **related but not a fit**. 'Agent using the described KOS' covers who uses a scheme, not the evidence or its strength; tier 3 and its namespace no longer resolves. |
| `dcterms:isReferencedBy` (DCMI Terms) | 1 | "A related resource that references, cites, or otherwise points to the described resource." [source](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl) | **fits as superclass or superproperty**; named in DCAT-AP 3 (not mandatory). Fits only the regulatory-citation kind of uptake. |
| `cito:Citation` (CiTO) | 2 | "A citation is a conceptual directional link from a citing entity to a cited entity, created by a human performative act of making a citation, typically instantiated by the inclusion of a bibliographic reference (`biro:BibliographicReference`) in the reference ..." [source](http://purl.org/spar/cito) | **related but not a fit**. Citations are one kind of uptake. |

**Evidence:** `dcterms:isReferencedBy`: verified at source

**Against the second review:** Disagrees with the second review, which proposed a subclass of duv:Usage while noting its definitions 'lean towards usage guidance'. Read at source, DUV's Usage is guidance for users, so subclassing would misstate what an Uptake is. NKOS usedBy, unchecked in the second review, is now read: it names the agent only.

### 7. `oht:NoMatch`

**Coined definition:** a mapping association asserting that its source concept has no counterpart in the target scheme. (Triage group: pattern.)

**Proposed verdict: Replace.** Follow SSSOM: use sssom:NoTermFound as the object (with the target scheme as object_source), rather than a marker class.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `sssom:NoTermFound` (SSSOM) | 2 | "sssom:NoTermFound can be used in place of a subject_id or object_id when the corresponding entity could not be found. It SHOULD be used in conjunction with a corresponding subject_source or object_source to signify where the term was not found." [source](https://w3id.org/sssom/) | **exact fit**. SSSOM's own convention for 'the corresponding entity could not be found'. |
| `sssom:mapping_cardinality_enum#1:0` (SSSOM) | 2 | "Indicates that the subject has no match in the object vocabulary. This value MUST only be used when the object_id is sssom:NoTermFound." [source](https://w3id.org/sssom/) | **exact fit**. Alternative SSSOM route: 'the subject has no match in the object vocabulary'. |
| `sssom:NegatedPredicate` (SSSOM) | 2 | "Negating the mapping predicate. The meaning of the triple becomes subject_id is not a predicate_id match to object_id." [source](https://w3id.org/sssom/) | **related but not a fit**. Negates one specific mapping (A is not a close match of B); different from 'no counterpart at all'. |
| `xkos:ConceptAssociation` (XKOS) | 2 | "XKOS defines the xkos:ConceptAssociation class that can be used to represent correspondences between classification items when the SKOS properties are not sufficient." [source](https://rdf-vocabulary.ddialliance.org/xkos.html) | **related but not a fit**. An association with no target cannot be told apart from an omission, as the first review said. |

**Evidence:** `sssom:NoTermFound`: verified at source; `sssom:mapping_cardinality_enum#1:0`: verified at source

**Against the second review:** Agrees with the second review (Replace). Now verified from the SSSOM schema itself, and SSSOM also offers the 1:0 mapping cardinality value. Also agrees that it duplicates the no_match value of item 45.

### 8. `oht:OpenQuestion`

**Coined definition:** an unresolved editorial point about a record, with a status and later a resolution. (Triage group: pattern.)

**Proposed verdict: Replace.** Use oa:Annotation with oa:motivatedBy oa:questioning targeting the record; the resolution is a reply annotation (oa:replying); keep adms:status for open or closed.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `oa:Annotation` (Web Annotation) | 1 | "The class for Web Annotations." [source](https://www.w3.org/ns/oa.ttl) | **exact fit**. A Web Annotation about the record. |
| `oa:questioning` (Web Annotation) | 1 | "The motivation for when the user intends to ask a question about the Target." [source](https://www.w3.org/ns/oa.ttl) | **exact fit**. 'The motivation for when the user intends to ask a question about the Target.' |
| `oa:replying` (Web Annotation) | 1 | "The motivation for when the user intends to reply to a previous statement, either an Annotation or another resource." [source](https://www.w3.org/ns/oa.ttl) | **exact fit**. Motivation for the annotation that resolves it. |
| `adms:status` (ADMS) | 2 | "The status of the Asset in the context of a particular workflow process." [source](https://www.w3.org/ns/adms.ttl) | **related but not a fit**; named in DCAT-AP 3 (not mandatory). Workflow status; carries open/resolved. |
| `skos:editorialNote` (SKOS) | 1 | "A note for an editor, translator or maintainer of the vocabulary." [source](http://www.w3.org/2004/02/skos/core.rdf) | **related but not a fit**. No status or resolution. |
| `schema:Question` (schema.org) | 2 | "A specific question - e.g. from a user seeking answers online, or collected in a Frequently Asked Questions (FAQ) document." [source](https://schema.org/version/latest/schemaorg-current-https.ttl) | **related but not a fit**; named in the RO-Crate 1.2 context. Q&A web content. |

**Evidence:** `oa:Annotation`: verified at source; `oa:questioning`: verified at source; `oa:replying`: verified at source

**Against the second review:** Agrees with the second review, and closes its caveat: oa:questioning and oa:replying are now verified directly in the W3C Web Annotation Vocabulary (oa.ttl), not via TEI.

### 9. `oht:HumanReview`

**Coined definition:** a person's review of a record. (Triage group: pattern.)

**Proposed verdict: Replace.** Use prov:Activity with a dcterms:type value for review; if the review's outcome is recorded, an oa:Annotation motivated by oa:assessing is the standard shape.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `prov:Activity` (PROV-O) | 1 | "An activity is something that occurs over a period of time and acts upon or with entities; it may include consuming, processing, transforming, modifying, relocating, using, or generating entities." [source](https://www.w3.org/ns/prov.ttl) | **fits as superclass or superproperty**. A review is an activity. |
| `oa:assessing` (Web Annotation) | 1 | "The motivation for when the user intends to provide an assessment about the Target resource." [source](https://www.w3.org/ns/oa.ttl) | **related but not a fit**. For recording the review's judgement as an annotation. |
| `schema:Review` (schema.org) | 2 | "A review of an item - for example, of a restaurant, movie, or store." [source](https://schema.org/version/latest/schemaorg-current-https.ttl) | **related but not a fit**; named in the RO-Crate 1.2 context. A review as a creative work (restaurant, film). |
| `dqv:QualityAnnotation` (DQV) | 2 | "Represents quality annotations, including ratings, quality certificates or feedback that can be associated to datasets or distributions. Quality annotations must have one oa:motivatedBy statement with an instance of oa:Motivation (and skos:Concept) that ..." [source](https://www.w3.org/ns/dqv.ttl) | **related but not a fit**. Quality feedback on a dataset; tier 2. |

**Evidence:** `prov:Activity`: verified at source

**Against the second review:** Agrees with the second review (Replace). prov:Activity now verified. Its point that a review with status 'none' is a review that never happened stands.

### 10. `oht:Session`

**Coined definition:** a drafting session with a language model, as an activity, and the transcript it produced. (Triage group: pattern.)

**Proposed verdict: Replace.** prov:Activity with prov:wasAssociatedWith a prov:SoftwareAgent; type the transcript schema:Conversation.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `prov:Activity` (PROV-O) | 1 | "An activity is something that occurs over a period of time and acts upon or with entities; it may include consuming, processing, transforming, modifying, relocating, using, or generating entities." [source](https://www.w3.org/ns/prov.ttl) | **fits as superclass or superproperty**. The session as activity. |
| `prov:SoftwareAgent` (PROV-O) | 1 | "A software agent is running software." [source](https://www.w3.org/ns/prov.ttl) | **exact fit**. The model. |
| `schema:Conversation` (schema.org) | 2 | "One or more messages between organizations or people on a particular topic. Individual messages can be linked to the conversation with isPartOf or hasPart properties." [source](https://schema.org/version/latest/schemaorg-current-https.ttl) | **exact fit**; named in the RO-Crate 1.2 context. The transcript; RO-Crate's context names schema:Conversation. |
| `schema:CreateAction` (schema.org) | 2 | "The act of deliberately creating/producing/generating/building a result out of the agent." [source](https://schema.org/version/latest/schemaorg-current-https.ttl) | **related but not a fit**; named in the RO-Crate 1.2 context. RO-Crate precedent for a tool run; heavier than needed. |

**Evidence:** `prov:Activity`: verified at source; `prov:SoftwareAgent`: verified at source; `schema:Conversation`: verified at source

**Against the second review:** Agrees with the second review.

### 11. `oht:family`

**Coined definition:** what kind of scheme this is (harm taxonomy and so on). (Triage group: mechanical.)

**Proposed verdict: Replace.** Use dcterms:type with values from a local family scheme, aligned to NKOS KOS types (skos:closeMatch) rather than depending on them.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `dcterms:type` (DCMI Terms) | 1 | "The nature or genre of the resource." [source](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl) | **exact fit**; named in DCAT-AP 3 (not mandatory). 'The nature or genre of the resource.' |
| `nkostype:taxonomy` (NKOS KOS Types) | 3 | "scheme of categories and subcategories that can be used to sort and otherwise organize items of knowledge or information" [source](https://nkos.dublincore.org/nkos-type.html) | **related but not a fit**. Useful alignment target; tier 3, the namespace no longer resolves and the values exist only as an HTML list. |
| `schema:additionalType` (schema.org) | 2 | "An additional type for the item, typically used for adding more specific types from external vocabularies in microdata syntax. This is a relationship between something and a class that the thing is in. Typically the value is a URI-identified RDF class, and in ..." [source](https://schema.org/version/latest/schemaorg-current-https.ttl) | **related but not a fit**; named in the RO-Crate 1.2 context. schema.org's equivalent slot; optional. |
| `dcat:themeTaxonomy` (DCAT 3) | 1 | "The knowledge organization system (KOS) used to classify catalog's datasets." [source](https://www.w3.org/ns/dcat.ttl) | **irrelevant**; named in DCAT-AP 3 (not mandatory). Names the KOS a catalogue uses, not a scheme's kind. |

**Evidence:** `dcterms:type`: verified at source

**Against the second review:** Agrees with the second review on dcterms:type. Adds a caution: the NKOS KOS Types namespace now redirects to a workshop page, so depend on a local scheme and align to NKOS in a separate file (tier 3 rule).

### 12. `oht:classifies`

**Coined definition:** the kind of unit a scheme sorts, such as a harm or a content item. (Triage group: domain or editorial.)

**Proposed verdict: Keep.** No standard property for the unit a scheme sorts; xkos:covers is the field, not the unit.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `xkos:covers` (XKOS) | 2 | "A classification covers a defined field: economic activity, occupations, living organisms, etc. ... The field covered should be represented by a skos:Concept" [source](https://rdf-vocabulary.ddialliance.org/xkos.html) | **related but not a fit**. The field a classification covers (online harms), which WEF and OpenAI share; the unit (harm versus content item) is what differs. |
| `disco:analysisUnit` (DDI Discovery) | 3 | "This property links to the analysis unit of a Study, a StudyGroup, or a Variable." [source](http://rdf-vocabulary.ddialliance.org/discovery) | **related but not a fit**. Same idea for studies and variables; tier 3, domain Study/Variable. |
| `dcterms:subject` (DCMI Terms) | 1 | "A topic of the resource." [source](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl) | **irrelevant**. Topic. |

**Evidence:** no standard term recommended; candidates read at source and judged not to fit.

**Against the second review:** Agrees with both reviews (Keep; DDI analogue). xkos:covers now read at source.

### 13. `oht:purpose`

**Coined definition:** what the issuer says the scheme is for. (Triage group: mechanical.)

**Proposed verdict: Keep under standard superclass or superproperty.** Declare oht:purpose rdfs:subPropertyOf dcterms:description.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `dcterms:description` (DCMI Terms) | 1 | "An account of the resource." [source](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl) | **fits as superclass or superproperty**; named in DCAT-AP 3 (mandatory), DCAT-AP 3 (not mandatory). 'An account of the resource'; generic tools will show purpose as description. |
| `disco:purpose` (DDI Discovery) | 3 | "The purpose of a Study of a StudyGroup." [source](http://rdf-vocabulary.ddialliance.org/discovery) | **related but not a fit**. Purpose of a study; tier 3. |
| `dcterms:abstract` (DCMI Terms) | 1 | "A summary of the resource." [source](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl) | **related but not a fit**. A summary, not a purpose. |

**Evidence:** `dcterms:description`: verified at source

**Against the second review:** Agrees with the second review; now verified.

### 14. `oht:legalStatus`

**Coined definition:** legal force of the scheme: statutory, guidance, voluntary, commercial, academic. (Triage group: domain or editorial.)

**Proposed verdict: Keep.** Legal force of a code or standard (statutory, guidance, voluntary) has no standard property; ELI's in_force is whether legislation is in force.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `eli:in_force` (ELI) | 2 | "A value indicating the legal force of a legal resource or a legal expression. A set of values is defined by ELI in the corresponding concept scheme. These values are : - in force - partially in force - not in force" [source](http://data.europa.eu/eli/ontology) | **related but not a fit**. In force / not in force, for legal resources only. |
| `schema:legislationLegalForce` (schema.org) | 2 | "Whether the legislation is currently in force, not in force, or partially in force." [source](https://schema.org/version/latest/schemaorg-current-https.ttl) | **related but not a fit**; named in the RO-Crate 1.2 context. Same as ELI's, for schema.org Legislation. |
| `adms:status` (ADMS) | 2 | "The status of the Asset in the context of a particular workflow process." [source](https://www.w3.org/ns/adms.ttl) | **irrelevant**; named in DCAT-AP 3 (not mandatory). Lifecycle status, orthogonal. |

**Evidence:** no standard term recommended; candidates read at source and judged not to fit.

**Against the second review:** Agrees with both reviews (Keep); the second review's advice to drop 'commercial' and 'academic' as publisher facts is outside term matching but sound.

### 15. `oht:statusDate`

**Coined definition:** when the current adms:status began. (Triage group: mechanical.)

**Proposed verdict: Keep under standard superclass or superproperty.** Declare oht:statusDate rdfs:subPropertyOf dcterms:date.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `dcterms:date` (DCMI Terms) | 1 | "A point or period of time associated with an event in the lifecycle of the resource." [source](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl) | **fits as superclass or superproperty**. 'A point or period of time associated with an event in the lifecycle of the resource.' |
| `dcterms:modified` (DCMI Terms) | 1 | "Date on which the resource was changed." [source](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl) | **related but not a fit**; named in DCAT-AP 3 (mandatory), DCAT-AP 3 (not mandatory). Last content change; can differ from status change. |
| `dcterms:valid` (DCMI Terms) | 1 | "Date (often a range) of validity of a resource." [source](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl) | **related but not a fit**. Validity range. |

**Evidence:** `dcterms:date`: verified at source

**Against the second review:** Agrees with the second review; the dcterms:date definition is now verified.

### 16. `oht:sunsetDate`

**Coined definition:** the announced date after which a scheme or service ceases. (Triage group: mechanical.)

**Proposed verdict: Replace.** Use schema:expires for schemes; for services, keep a coined term under dcterms:date or accept the domain stretch.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `schema:expires` (schema.org) | 2 | "Date the content expires and is no longer useful or available. For example a VideoObject or NewsArticle whose availability or relevance is time-limited, a ClaimReview fact check whose publisher wants to indicate that it may no longer be relevant (or helpful ..." [source](https://schema.org/version/latest/schemaorg-current-https.ttl) | **exact fit**; named in the RO-Crate 1.2 context. 'Date the content expires and is no longer useful or available.' Its domain is CreativeWork (and Certification), which covers a scheme but not a service such as an API. |
| `dcterms:valid` (DCMI Terms) | 1 | "Date (often a range) of validity of a resource." [source](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl) | **related but not a fit**. A validity range; harder to query. |
| `eli:date_no_longer_in_force` (ELI) | 2 | "The last date any part of the legislation is in force, if the date is known (can be seen as the end date of a dc:valid range for this resource)." [source](http://data.europa.eu/eli/ontology) | **related but not a fit**. For legislation only. |
| `schema:endDate` (schema.org) | 2 | "The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601))." [source](https://schema.org/version/latest/schemaorg-current-https.ttl) | **related but not a fit**; named in the RO-Crate 1.2 context. End of an event or period. |

**Evidence:** `schema:expires`: verified at source

**Against the second review:** Agrees with the second review (Replace), now verified, with one caveat it did not raise: schema:expires is declared on CreativeWork, and some sunset examples (Perspective API) are services.

### 17. `oht:severityEncoding`

**Coined definition:** where severity lives in a scheme: nowhere, in the hierarchy, on an axis, both. (Triage group: domain or editorial.)

**Proposed verdict: Keep.** A structural fact about the scheme with no standard home.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `skos:note` (SKOS) | 1 | "A general note, for any purpose." [source](http://www.w3.org/2004/02/skos/core.rdf) | **related but not a fit**. Prose; the value is structured and filtered on. |
| `risk:HighSeverity` (DPV RISK) | 2 | "Level where Severity is High" [source](https://w3id.org/dpv/risk) | **related but not a fit**. DPV has severity levels (values), not where severity is encoded. |

**Evidence:** no standard term recommended; candidates read at source and judged not to fit.

**Against the second review:** Agrees with the second review (Keep). DPV RISK severity levels could supply axis values, a separate question.

### 18. `oht:hasConcept`

**Coined definition:** links a concept scheme to each concept in it (inverse of skos:inScheme). (Triage group: pattern.)

**Proposed verdict: Drop.** Use a JSON-LD @reverse of skos:inScheme; if a stored forward link is ever needed, schema:hasDefinedTerm.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `schema:hasDefinedTerm` (schema.org) | 2 | "A Defined Term contained in this term set." [source](https://schema.org/version/latest/schemaorg-current-https.ttl) | **exact fit**; named in the RO-Crate 1.2 context. 'A Defined Term contained in this term set'; requires typing the scheme schema:DefinedTermSet. In current schema.org core (not pending); absent from LOV's 2020 copy. |
| `skos:inScheme` (SKOS) | 1 | "Relates a resource (for example a concept) to a concept scheme in which it is included." [source](http://www.w3.org/2004/02/skos/core.rdf) | **exact fit**. The standard link, from concept to scheme. |
| `skos:hasTopConcept` (SKOS) | 1 | "Relates, by convention, a concept scheme to a concept which is topmost in the broader/narrower concept hierarchies for that scheme, providing an entry point to these hierarchies." [source](http://www.w3.org/2004/02/skos/core.rdf) | **related but not a fit**. Top concepts only. |

**Evidence:** `schema:hasDefinedTerm`: verified at source; `skos:inScheme`: verified at source

**Against the second review:** Agrees with the second review; schema:hasDefinedTerm now verified at source.

### 19. `oht:primarySource`

**Coined definition:** the authoritative text that defines the scheme. (Triage group: pattern.)

**Proposed verdict: Replace.** Use prov:hadPrimarySource, plus cito:citesAsAuthority to single out the authoritative text.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `prov:hadPrimarySource` (PROV-O) | 1 | "[definition of prov:PrimarySource] A primary source for a topic refers to something produced by some agent with direct experience and knowledge about the topic, at the time of the topic's study, without benefit from hindsight. Because of the directness of ..." [source](https://www.w3.org/ns/prov.ttl) | **exact fit**. A source produced by an agent with direct knowledge; the issuer's PDF is that. |
| `cito:citesAsAuthority` (CiTO) | 2 | "A relation according to which the citing entity cites the cited entity as one that provides an authoritative description or definition of the subject under discussion." [source](http://purl.org/spar/cito) | **exact fit**. 'cites the cited entity as one that provides an authoritative description or definition'. |
| `dcterms:source` (DCMI Terms) | 1 | "A related resource from which the described resource is derived." [source](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl) | **related but not a fit**; named in DCAT-AP 3 (not mandatory). Any source the resource derives from. |

**Evidence:** `prov:hadPrimarySource`: verified at source (definition carried by the qualified class); `cito:citesAsAuthority`: verified at source

**Against the second review:** Agrees with both reviews.

### 20. `oht:sourceType`

**Coined definition:** primary, secondary or tertiary source, relative to the citing scheme. (Triage group: mechanical.)

**Proposed verdict: Drop.** Primary versus secondary belongs on the relation (prov:hadPrimarySource versus prov:wasDerivedFrom).

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `prov:hadPrimarySource` (PROV-O) | 1 | "[definition of prov:PrimarySource] A primary source for a topic refers to something produced by some agent with direct experience and knowledge about the topic, at the time of the topic's study, without benefit from hindsight. Because of the directness of ..." [source](https://www.w3.org/ns/prov.ttl) | **exact fit**. Primary case. |
| `prov:wasDerivedFrom` (PROV-O) | 1 | "A derivation is a transformation of an entity into another, an update of an entity resulting in a new one, or the construction of a new entity based on a pre-existing entity." [source](https://www.w3.org/ns/prov.ttl) | **fits as superclass or superproperty**; named in the RO-Crate 1.2 context. Everything else; RO-Crate names it. |

**Evidence:** `prov:hadPrimarySource`: verified at source (definition carried by the qualified class); `prov:wasDerivedFrom`: verified at source

**Against the second review:** Agrees with the second review.

### 21. `oht:hasChange`

**Coined definition:** a version lists a change. (Triage group: mechanical.)

**Proposed verdict: Keep under standard superclass or superproperty.** Declare oht:hasChange rdfs:subPropertyOf dcterms:hasPart.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `dcterms:hasPart` (DCMI Terms) | 1 | "A related resource that is included either physically or logically in the described resource." [source](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl) | **fits as superclass or superproperty**; named in DCAT-AP 3 (not mandatory). A change entry is logically part of the version's record. |
| `sh:hasDelta` (skos-history) | 3 | "A delta for this version. The subject of the triple may be a dsv:VersionHistoryRecord." [source](http://purl.org/skos-history/) | **related but not a fit**. Version to delta; tier 3. |

**Evidence:** `dcterms:hasPart`: verified at source

### 22. `oht:changeType`

**Coined definition:** added, removed, renamed, redefined, moved, merged, split, reclassified. (Triage group: mechanical.)

**Proposed verdict: Replace.** Use dcterms:type on the change; reuse IAO obsolescence reasons for merged and split where they fit.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `dcterms:type` (DCMI Terms) | 1 | "The nature or genre of the resource." [source](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl) | **exact fit**; named in DCAT-AP 3 (not mandatory). One type slot on a change. |
| `obo:IAO_0000227` (OBO IAO) | 2 | "The term has been combined with one or more other terms to create a more encompassing (merged) term." [source](http://purl.obolibrary.org/obo/iao.owl) | **related but not a fit**. Value alignment: 'terms merged'. |
| `obo:IAO_0000229` (OBO IAO) | 2 | "The term has been split into two or more new terms." [source](http://purl.obolibrary.org/obo/iao.owl) | **related but not a fit**. Value alignment: 'term split'. |
| `skos:changeNote` (SKOS) | 1 | "A note about a modification to a concept." [source](http://www.w3.org/2004/02/skos/core.rdf) | **related but not a fit**. Prose. |

**Evidence:** `dcterms:type`: verified at source

### 23. `oht:affectsConcept`

**Coined definition:** the concept a change touched. (Triage group: pattern.)

**Proposed verdict: Keep.** None of the standard 'target' properties has a changelog entry as its subject.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `dcterms:subject` (DCMI Terms) | 1 | "A topic of the resource." [source](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl) | **related but not a fit**. Topic, odd for an operand. |
| `prov:used` (PROV-O) | 1 | "A prov:Entity that was used by this prov:Activity. For example, :baking prov:used :spoon, :egg, :oven ." [source](https://www.w3.org/ns/prov.ttl) | **related but not a fit**. Requires the change to be an activity (see item 3). |
| `oa:hasTarget` (Web Annotation) | 1 | "The relationship between an Annotation and its Target." [source](https://www.w3.org/ns/oa.ttl) | **related but not a fit**. Domain oa:Annotation. |

**Evidence:** no standard term recommended; candidates read at source and judged not to fit.

### 24. `oht:officialMapping`

**Coined definition:** the issuer's own crosswalk from the previous version. (Triage group: pattern.)

**Proposed verdict: Replace.** Model the issuer's crosswalk as an xkos:Correspondence attributed to the issuer (dcterms:publisher), with the TSV as its source (prov:hadPrimarySource or a dcat:Distribution).

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `xkos:Correspondence` (XKOS) | 2 | "The complete collection of such associations for all the concepts in two SKOS Concept Schemes forms a correspondence and is expressed as an instance of the xkos:Correspondence class." [source](https://rdf-vocabulary.ddialliance.org/xkos.html) | **exact fit**. A correspondence between two concept schemes, which the issuer's crosswalk is. |
| `dcterms:relation` (DCMI Terms) | 1 | "A related resource." [source](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl) | **fits as superclass or superproperty**; named in DCAT-AP 3 (mandatory), DCAT-AP 3 (not mandatory). Too vague to help. |

**Evidence:** `xkos:Correspondence`: verified at source (specification text); `dcterms:relation`: verified at source

### 25. `oht:introducedIn`

**Coined definition:** the version in which a concept first appeared. (Triage group: pattern.)

**Proposed verdict: Keep.** No standard 'first appeared in version' link; dcterms:created and prov:generatedAtTime are dates, not issuer versions.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `dcterms:created` (DCMI Terms) | 1 | "Date of creation of the resource." [source](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl) | **related but not a fit**. Date. |
| `prov:generatedAtTime` (PROV-O) | 1 | "The time at which an entity was completely created and is available for use." [source](https://www.w3.org/ns/prov.ttl) | **related but not a fit**. Timestamp. |
| `pav:createdAt` (PAV) | 2 | "The geo-location of the agents when creating the resource (pav:createdBy). For instance a photographer takes a picture of the Eiffel Tower while standing in front of it." [source](http://purl.org/pav/) | **irrelevant**. Despite its name, PAV defines it as the geo-location of the creating agent. |

**Evidence:** no standard term recommended; candidates read at source and judged not to fit.

### 26. `oht:retiredIn`

**Coined definition:** the version in which a concept was removed; the IRI remains. (Triage group: pattern.)

**Proposed verdict: Keep.** Keep the version link, and also assert owl:deprecated true and dcterms:isReplacedBy so generic tools see the retirement.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `owl:deprecated` (OWL 2) | 1 | "The annotation property that indicates that a given entity has been deprecated." [source](https://www.w3.org/2002/07/owl.ttl) | **related but not a fit**. A flag with no version; add it alongside. |
| `dcterms:isReplacedBy` (DCMI Terms) | 1 | "A related resource that supplants, displaces, or supersedes the described resource." [source](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl) | **related but not a fit**. The successor, where there is one. |
| `obo:IAO_0100001` (OBO IAO) | 2 | "Use on obsolete terms, relating the term to another term that can be used as a substitute" [source](http://purl.obolibrary.org/obo/iao.owl) | **related but not a fit**. OBO's 'term replaced by'; tier 2. |
| `prov:invalidatedAtTime` (PROV-O) | 1 | "The time at which an entity was invalidated (i.e., no longer usable)." [source](https://www.w3.org/ns/prov.ttl) | **related but not a fit**. Timestamp. |

**Evidence:** no standard term recommended; candidates read at source and judged not to fit.

### 27. `oht:hasAxis`

**Coined definition:** a scheme declares an axis. (Triage group: mechanical.)

**Proposed verdict: Keep under standard superclass or superproperty.** Declare oht:hasAxis rdfs:subPropertyOf dcterms:hasPart.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `dcterms:hasPart` (DCMI Terms) | 1 | "A related resource that is included either physically or logically in the described resource." [source](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl) | **fits as superclass or superproperty**; named in DCAT-AP 3 (not mandatory). An axis is logically part of the scheme. |
| `qb:component` (RDF Data Cube) | 1 | "indicates a component specification which is included in the structure of the dataset" [source](http://purl.org/linked-data/cube) | **related but not a fit**. Data Cube structure component; analogue only. |

**Evidence:** `dcterms:hasPart`: verified at source

### 28. `oht:axisKind`

**Coined definition:** whether an axis is ordinal or categorical. (Triage group: mechanical.)

**Proposed verdict: Replace.** Use dcterms:type on the axis with ordinal and categorical values.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `dcterms:type` (DCMI Terms) | 1 | "The nature or genre of the resource." [source](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl) | **exact fit**; named in DCAT-AP 3 (not mandatory). One type slot on an axis. |

**Evidence:** `dcterms:type`: verified at source

### 29. `oht:multiValued`

**Coined definition:** whether a concept may take several values on the axis. (Triage group: domain or editorial.)

**Proposed verdict: Keep.** schema:multipleValues says the same thing but only for form-input specifications.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `schema:multipleValues` (schema.org) | 2 | "Whether multiple values are allowed for the property. Default is false." [source](https://schema.org/version/latest/schemaorg-current-https.ttl) | **related but not a fit**; named in the RO-Crate 1.2 context. 'Whether multiple values are allowed for the property'; domain PropertyValueSpecification. |
| `owl:FunctionalProperty` (OWL 2) | 1 | "The class of functional properties." [source](https://www.w3.org/2002/07/owl.ttl) | **related but not a fit**. Would need one property per axis. |

**Evidence:** no standard term recommended; candidates read at source and judged not to fit.

### 30. `oht:hasFacetValue`

**Coined definition:** a concept takes a value from one of its scheme's axes. (Triage group: domain or editorial.)

**Proposed verdict: Keep under standard superclass or superproperty.** Declare oht:hasFacetValue rdfs:subPropertyOf xkos:classifiedUnder.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `xkos:classifiedUnder` (XKOS) | 2 | "classifying results in the creation of a RDF statement where the resource representing the entity is the subject and the concept representing the classification item is the object. XKOS defines a generic property, xkos:classifiedUnder, that can be used in ..." [source](https://rdf-vocabulary.ddialliance.org/xkos.html) | **fits as superclass or superproperty**. XKOS's generic 'entity classified under a classification item' property, which it expects to be specialised; a concept taking a value on an axis is exactly that. |
| `skos:related` (SKOS) | 1 | "Relates a concept to a concept with which there is an associative semantic relationship." [source](http://www.w3.org/2004/02/skos/core.rdf) | **related but not a fit**. Associative only. |

**Evidence:** `xkos:classifiedUnder`: verified at source (specification text)

### 31. `oht:consequence`

**Coined definition:** what follows from a concept or value in the scheme (a note users filter on). (Triage group: mechanical.)

**Proposed verdict: Keep under standard superclass or superproperty.** Declare oht:consequence rdfs:subPropertyOf skos:scopeNote (or skos:note).

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `skos:scopeNote` (SKOS) | 1 | "A note that helps to clarify the meaning and/or the use of a concept." [source](http://www.w3.org/2004/02/skos/core.rdf) | **fits as superclass or superproperty**. 'A note that helps to clarify the meaning and/or the use of a concept.' |
| `skos:note` (SKOS) | 1 | "A general note, for any purpose." [source](http://www.w3.org/2004/02/skos/core.rdf) | **fits as superclass or superproperty**. Safe general parent. |
| `dpv:hasConsequence` (DPV core) | 2 | "Indicates consequence(s) possible or arising from specified concept" [source](https://w3id.org/dpv) | **related but not a fit**. Links to a dpv:Consequence resource, not a note. |

**Evidence:** `skos:scopeNote`: verified at source; `skos:note`: verified at source

### 32. `oht:hasOutput`

**Coined definition:** attaches an output specification to a scheme or classifier. (Triage group: pattern.)

**Proposed verdict: Replace.** Use ssn:hasOutput from the classifier (sosa:Procedure), if item 5 is adopted.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `ssn:hasOutput` (SSN) | 1 | "Relation between a Procedure and an Output of it." [source](https://www.w3.org/ns/ssn/) | **exact fit**. 'Relation between a Procedure and an Output of it.' |
| `mls:hasOutput` (ML Schema) | 2 | "A relation between a run and either a model or model evaluation that is produced on it’s output." [source](http://www.w3.org/ns/mls) | **related but not a fit**. Run to model. |

**Evidence:** `ssn:hasOutput`: verified at source

### 33. `oht:outputType`

**Coined definition:** boolean, probability, ordinal, score or none. (Triage group: mechanical.)

**Proposed verdict: Replace.** Use dcterms:type on the output specification.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `dcterms:type` (DCMI Terms) | 1 | "The nature or genre of the resource." [source](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl) | **exact fit**; named in DCAT-AP 3 (not mandatory). One type slot on an output. |

**Evidence:** `dcterms:type`: verified at source

### 34. `oht:outputAxis`

**Coined definition:** for ordinal outputs, the axis returned. (Triage group: domain or editorial.)

**Proposed verdict: Keep.** No standard term for the scale a classifier's output is expressed on.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `qb:dimension` (RDF Data Cube) | 1 | "An alternative to qb:componentProperty which makes explicit that the component is a dimension" [source](http://purl.org/linked-data/cube) | **related but not a fit**. Data Cube structure, not classifier output. |

**Evidence:** no standard term recommended; candidates read at source and judged not to fit.

### 35. `oht:modality`

**Coined definition:** the kind of input a concept applies to (text, image, audio, video). (Triage group: domain or editorial.)

**Proposed verdict: Keep.** Keep the property (it describes what a concept applies to, not a resource's format), but take its values from the DCMI Type Vocabulary.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `dcmitype:Text` (DCMI Type) | 1 | "A resource consisting primarily of words for reading." [source](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_type.ttl) | **related but not a fit**. Value reuse: DCMI Type gives Text, StillImage, MovingImage, Sound; tier 1. |
| `dcterms:format` (DCMI Terms) | 1 | "The file format, physical medium, or dimensions of the resource." [source](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl) | **related but not a fit**; named in DCAT-AP 3 (not mandatory). Format of the resource itself. |
| `schema:encodingFormat` (schema.org) | 2 | "Media type typically expressed using a MIME format (see [IANA site](http://www.iana.org/assignments/media-types/media-types.xhtml) and [MDN reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types)), e.g. application/zip for a ..." [source](https://schema.org/version/latest/schemaorg-current-https.ttl) | **related but not a fit**; named in the RO-Crate 1.2 context. MIME type of a media object. |

**Evidence:** no standard term recommended; candidates read at source and judged not to fit.

### 36. `oht:legalBasis`

**Coined definition:** the legal provision behind a concept, as an ELI legal resource. (Triage group: domain or editorial.)

**Proposed verdict: Keep.** DPV's legal basis is about justifying processing; ELI's links run between legal resources.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `dpv:hasLegalBasis` (DPV core) | 2 | "Indicates use or applicability of a Legal Basis" [source](https://w3id.org/dpv) | **related but not a fit**. Range dpv:LegalBasis, 'used to justify processing of data or use of technology'. |
| `eli:based_on` (ELI) | 2 | "Inverse of "basis_for". Indicates that thiswork is empowered by another one, typically a constitution, a treaty or an enabling act." [source](http://data.europa.eu/eli/ontology) | **related but not a fit**. Work empowered by another; legal resources only. |
| `eli:implements` (ELI) | 2 | "This property is deprecated. Use "applies" instead." [source](http://data.europa.eu/eli/ontology) | **irrelevant**. Deprecated in current ELI: 'Use "applies" instead.' |
| `dcterms:source` (DCMI Terms) | 1 | "A related resource from which the described resource is derived." [source](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl) | **related but not a fit**; named in DCAT-AP 3 (not mandatory). Already used for bibliographic sources. |

**Evidence:** no standard term recommended; candidates read at source and judged not to fit.

### 37. `oht:contextDependent`

**Coined definition:** the scheme says the concept's status depends on deployment context. (Triage group: domain or editorial.)

**Proposed verdict: Keep.** A boolean flag with no standard equivalent.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `skos:note` (SKOS) | 1 | "A general note, for any purpose." [source](http://www.w3.org/2004/02/skos/core.rdf) | **related but not a fit**. Prose. |

**Evidence:** no standard term recommended; candidates read at source and judged not to fit.

### 38. `oht:verbatim`

**Coined definition:** on an explanatory note, whether the text is the source's exact words. (Triage group: pattern.)

**Proposed verdict: Replace.** Express verbatim notes with prov:wasQuotedFrom from the note to its source; non-verbatim with prov:wasDerivedFrom. It also overlaps the 'verbatim' value of item 49.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `prov:wasQuotedFrom` (PROV-O) | 1 | "An entity is derived from an original entity by copying, or 'quoting', some or all of it." [source](https://www.w3.org/ns/prov.ttl) | **exact fit**. 'An entity is derived from an original entity by copying, or quoting, some or all of it.' |
| `cito:includesQuotationFrom` (CiTO) | 2 | "A relation according to which the citing entity includes one or more quotations from the cited entity." [source](http://purl.org/spar/cito) | **related but not a fit**. Citation-level; for documents. |
| `oa:exact` (Web Annotation) | 1 | "The object of the predicate is a copy of the text which is being selected, after normalization." [source](https://www.w3.org/ns/oa.ttl) | **irrelevant**. Text selector. |

**Evidence:** `prov:wasQuotedFrom`: verified at source

### 39. `oht:operationalises`

**Coined definition:** this scheme turns the target's duties or principles into practice. (Triage group: domain or editorial.)

**Proposed verdict: Keep.** No standard 'puts duties into practice' relation between non-legal schemes and law; dcterms:conformsTo is conformance, ELI's are between legal resources.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `dcterms:conformsTo` (DCMI Terms) | 1 | "An established standard to which the described resource conforms." [source](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl) | **related but not a fit**; named in DCAT-AP 3 (not mandatory), the RO-Crate 1.2 context. 'An established standard to which the described resource conforms.' |
| `eli:applies` (ELI) | 2 | "Indicates that this legislation (or part of a legislation) somehow conforms with another legislation. This is an informative link, and it has no legal value. For legally-binding links of transposition, use the property transposes. This can be used for example ..." [source](http://data.europa.eu/eli/ontology) | **related but not a fit**. Informative conformity between legislation; range LegalResource. |
| `eli:transposes` (ELI) | 2 | "Indicates that this legislation (or part of legislation) fulfills the objectives set by another legislation, by passing appropriate implementation measures. Typically, some legislations of European Union's member states or regions transpose European ..." [source](http://data.europa.eu/eli/ontology) | **related but not a fit**. Binding, legislation to legislation. |
| `eli:implements` (ELI) | 2 | "This property is deprecated. Use "applies" instead." [source](http://data.europa.eu/eli/ontology) | **irrelevant**. Deprecated in current ELI. |

**Evidence:** no standard term recommended; candidates read at source and judged not to fit.

### 40. `oht:operationalisedBy`

**Coined definition:** inverse of operationalises. (Triage group: domain or editorial.)

**Proposed verdict: Drop.** Same rule as item 18: express the inverse with JSON-LD @reverse, not a second stored property.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `eli:implemented_by` (ELI) | 2 | "This property is deprecated. Use "applied_by" instead." [source](http://data.europa.eu/eli/ontology) | **irrelevant**. Deprecated in current ELI. |

**Evidence:** no standard term recommended; candidates read at source and judged not to fit.

### 41. `oht:conflictsWith`

**Coined definition:** two schemes make incompatible claims about the same field. (Triage group: domain or editorial.)

**Proposed verdict: Keep.** cito:disagreesWith is a citing work disagreeing with a cited one; conflict here is the library's symmetric judgement.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `cito:disagreesWith` (CiTO) | 2 | "A relation according to which the citing entity disagrees with statements, ideas or conclusions presented in the cited entity." [source](http://purl.org/spar/cito) | **related but not a fit**. Directional and authored by the citing work. |
| `xkos:disjoint` (XKOS) | 2 | "(none in file)" [source](http://rdf-vocabulary.ddialliance.org/xkos) | **related but not a fit**. Concepts with no common instances. |
| `owl:disjointWith` (OWL 2) | 1 | "The property that determines that two given classes are disjoint." [source](https://www.w3.org/2002/07/owl.ttl) | **irrelevant**. Classes. |

**Evidence:** no standard term recommended; candidates read at source and judged not to fit.

### 42. `oht:hasUptake`

**Coined definition:** attaches uptake evidence to a scheme. (Triage group: pattern.)

**Proposed verdict: Keep.** Follows item 6.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `duv:hasUsage` (DUV) | 2 | "Dataset/distribution usage guidance or instructions." [source](https://www.w3.org/ns/duv.ttl) | **related but not a fit**. Usage guidance, see item 6. |

**Evidence:** no standard term recommended; candidates read at source and judged not to fit.

### 43. `oht:uptakeKind`

**Coined definition:** regulatory citation, platform adoption, benchmark use and so on. (Triage group: mechanical.)

**Proposed verdict: Replace.** Use dcterms:type on the uptake.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `dcterms:type` (DCMI Terms) | 1 | "The nature or genre of the resource." [source](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl) | **exact fit**; named in DCAT-AP 3 (not mandatory). One type slot on an uptake. |

**Evidence:** `dcterms:type`: verified at source

### 44. `oht:strength`

**Coined definition:** strong, moderate, weak, as the library judges evidence. (Triage group: domain or editorial.)

**Proposed verdict: Keep.** A categorical evidence grade; merge with item 46 into one scale as the first review suggested.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `sssom:confidence` (SSSOM) | 2 | "A value assigned by the creator of the mapping to denote the creator's confidence or estimated probability that the mapping record is correct. A value of 1.0 means the creator has full confidence in the correctness of the mapping record, while a value of 0.0 ..." [source](https://w3id.org/sssom/) | **related but not a fit**. Numeric, and about mappings. |
| `schema:evidenceLevel` (schema.org) | 2 | "Strength of evidence of the data used to formulate the guideline (enumerated)." [source](https://schema.org/version/latest/schemaorg-current-https.ttl) | **related but not a fit**; named in the RO-Crate 1.2 context. Medical guidelines only. |

**Evidence:** no standard term recommended; candidates read at source and judged not to fit.

### 45. `oht:mappingRelation`

**Coined definition:** the relation an association asserts, including no_match. (Triage group: pattern.)

**Proposed verdict: Replace.** Carry the relation as the SKOS mapping property itself (skos:exactMatch, closeMatch, broadMatch, narrowMatch, relatedMatch) in SSSOM's predicate slot, and drop no_match (item 7).

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `owl:annotatedProperty` (SSSOM) | 2 | "predicate_id: The ID of the predicate or relation that relates the subject and object of this match. [SSSOM serialises this slot as owl:annotatedProperty]" [source](https://w3id.org/sssom/) | **exact fit**. SSSOM's predicate_id: the IRI of the relation. |
| `skos:closeMatch` (SKOS) | 1 | "skos:closeMatch is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications. In order to avoid the possibility of "compound errors" when combining mappings across more than two ..." [source](http://www.w3.org/2004/02/skos/core.rdf) | **exact fit**. Value: the mapping relation is itself a standard IRI. |
| `skos:mappingRelation` (SKOS) | 1 | "Relates two concepts coming, by convention, from different schemes, and that have comparable meanings" [source](http://www.w3.org/2004/02/skos/core.rdf) | **fits as superclass or superproperty**. Parent of the SKOS mapping properties. |
| `sssom:predicate_modifier` (SSSOM) | 2 | "A modifier for negating the predicate. See https://github.com/mapping-commons/sssom/issues/40 for discussion" [source](https://w3id.org/sssom/) | **related but not a fit**. For negating a specific mapping. |

**Evidence:** `owl:annotatedProperty`: verified at source (specification text); `skos:closeMatch`: verified at source; `skos:mappingRelation`: verified at source

### 46. `oht:confidence`

**Coined definition:** issuer_asserted, high, medium, low - categorical confidence in a mapping. (Triage group: pattern.)

**Proposed verdict: Keep.** Keep the categorical value, but move 'issuer_asserted' out: who asserted a mapping is sssom:mapping_provider (or the justification), not a confidence level.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `sssom:confidence` (SSSOM) | 2 | "A value assigned by the creator of the mapping to denote the creator's confidence or estimated probability that the mapping record is correct. A value of 1.0 means the creator has full confidence in the correctness of the mapping record, while a value of 0.0 ..." [source](https://w3id.org/sssom/) | **related but not a fit**. Numeric 0 to 1; see item 47. |
| `sssom:mapping_provider` (SSSOM) | 2 | "URL pointing to the source that provided the mapping, for example an ontology that already contains the mappings, or a database from which it was derived." [source](https://w3id.org/sssom/) | **related but not a fit**. Carries the issuer_asserted case. |

**Evidence:** no standard term recommended; candidates read at source and judged not to fit.

### 47. `oht:score`

**Coined definition:** numeric confidence 0 to 1. (Triage group: pattern.)

**Proposed verdict: Replace.** Use sssom:confidence.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `sssom:confidence` (SSSOM) | 2 | "A value assigned by the creator of the mapping to denote the creator's confidence or estimated probability that the mapping record is correct. A value of 1.0 means the creator has full confidence in the correctness of the mapping record, while a value of 0.0 ..." [source](https://w3id.org/sssom/) | **exact fit**. 'the creator's confidence or estimated probability that the mapping record is correct', 0.0 to 1.0. |
| `sssom:similarity_score` (SSSOM) | 2 | "A score between 0 and 1 to denote the similarity between two entities, where 1 denotes equivalence, and 0 denotes disjointness. The score is meant to be used in conjunction with the similarity_measure field, to document, for example, the lexical or semantic ..." [source](https://w3id.org/sssom/) | **related but not a fit**. Similarity, not correctness. |

**Evidence:** `sssom:confidence`: verified at source

### 48. `oht:method`

**Coined definition:** how a record or crosswalk was produced. (Triage group: pattern.)

**Proposed verdict: Replace.** For crosswalks, sssom:mapping_justification with SEMAPV values (manual curation, lexical matching, LLM-based matching); for records, prov:wasGeneratedBy an activity typed with dcterms:type.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `sssom:mapping_justification` (SSSOM) | 2 | "A mapping justification is an action (or the written representation of that action) of showing a mapping to be right or reasonable." [source](https://w3id.org/sssom/) | **exact fit**. How a mapping was shown to be right. |
| `semapv:ManualMappingCuration` (SEMAPV) | 2 | "A matching process that is performed by a human agent and is based on human judgement and domain knowledge." [source](https://w3id.org/semapv/vocab/) | **exact fit**. Value. |
| `semapv:LLMBasedMatching` (SEMAPV) | 2 | "A machine learning-based matching process in which a large language model determines matches between entities, typically through single-step or few-shot prompting, or through fine-tuning the model to judge mapping candidates or generate mappings directly." [source](https://w3id.org/semapv/vocab/) | **exact fit**. Value for llm_assisted crosswalks. |
| `prov:wasGeneratedBy` (PROV-O) | 1 | "[definition of prov:Generation] Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation." [source](https://www.w3.org/ns/prov.ttl) | **exact fit**; named in DCAT-AP 3 (not mandatory). For records; DCAT-AP names it on Dataset. |

**Evidence:** `sssom:mapping_justification`: verified at source; `semapv:ManualMappingCuration`: verified at source; `semapv:LLMBasedMatching`: verified at source; `prov:wasGeneratedBy`: verified at source (definition carried by the qualified class)

### 49. `oht:derivationMethod`

**Coined definition:** how an item relates to its source: authored, verbatim, transcribed, paraphrased, translated, converted, inferred, llm_drafted, mixed. (Triage group: domain or editorial.)

**Proposed verdict: Keep.** Keep the property; align values where standards exist: verbatim to prov:Quotation, translated to bibo:translationOf, llm_drafted to IPTC 'Created using Generative AI' (as schema:digitalSourceType does).

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `prov:Quotation` (PROV-O) | 1 | "A quotation is the repeat of (some or all of) an entity, such as text or image, by someone who may or may not be its original author. Quotation is a particular case of derivation." [source](https://www.w3.org/ns/prov.ttl) | **related but not a fit**. Covers verbatim only. |
| `prov:Revision` (PROV-O) | 1 | "A revision is a derivation for which the resulting entity is a revised version of some original. The implication here is that the resulting entity contains substantial content from the original. Revision is a particular case of derivation." [source](https://www.w3.org/ns/prov.ttl) | **related but not a fit**. Covers revised versions only. |
| `iptcdst:trainedAlgorithmicMedia` (IPTC Digital Source Type) | 2 | "Digital media created algorithmically using an Artificial Intelligence model trained on captured content" [source](http://cv.iptc.org/newscodes/digitalsourcetype/) | **related but not a fit**. Value alignment for llm_drafted; schema.org references this code list. |
| `schema:digitalSourceType` (schema.org) | 2 | "Indicates an IPTCDigitalSourceEnumeration code indicating the nature of the digital source(s) for some CreativeWork." [source](https://schema.org/version/latest/schemaorg-current-https.ttl) | **related but not a fit**. schema.org property for IPTC codes, on creative works. |

**Evidence:** no standard term recommended; candidates read at source and judged not to fit.

### 50. `oht:reviewed`

**Coined definition:** a person has checked this item against its source. (Triage group: mechanical.)

**Proposed verdict: Drop.** A boolean shortcut for a review activity; use the item 9 pattern (a review activity that prov:used the item).

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `prov:used` (PROV-O) | 1 | "A prov:Entity that was used by this prov:Activity. For example, :baking prov:used :spoon, :egg, :oven ." [source](https://www.w3.org/ns/prov.ttl) | **exact fit**. The review activity used the item. |
| `schema:reviewedBy` (schema.org) | 2 | "People or organizations that have reviewed the content on this web page for accuracy and/or completeness." [source](https://schema.org/version/latest/schemaorg-current-https.ttl) | **related but not a fit**; named in the RO-Crate 1.2 context. WebPage only. |

**Evidence:** `prov:used`: verified at source

### 51. `oht:verification`

**Coined definition:** verified_primary, secondary_only, unverified. (Triage group: domain or editorial.)

**Proposed verdict: Keep.** The verification grade has no standard home; PROV can say a check happened, not its grade.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `dpv:VerifiedData` (DPV core) | 2 | "Data that has been verified in terms of accuracy, consistency, or quality" [source](https://w3id.org/dpv) | **related but not a fit**. Data accuracy, not source verification. |
| `dqv:QualityAnnotation` (DQV) | 2 | "Represents quality annotations, including ratings, quality certificates or feedback that can be associated to datasets or distributions. Quality annotations must have one oa:motivatedBy statement with an instance of oa:Motivation (and skos:Concept) that ..." [source](https://www.w3.org/ns/dqv.ttl) | **related but not a fit**. Could carry a grade as an annotation; heavier. |

**Evidence:** no standard term recommended; candidates read at source and judged not to fit.

### 52. `oht:reviewDue`

**Coined definition:** when the record should next be checked. (Triage group: domain or editorial.)

**Proposed verdict: Keep under standard superclass or superproperty.** Declare oht:reviewDue rdfs:subPropertyOf dcterms:date.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `dcterms:date` (DCMI Terms) | 1 | "A point or period of time associated with an event in the lifecycle of the resource." [source](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl) | **fits as superclass or superproperty**. A date in the record's lifecycle. |
| `schema:lastReviewed` (schema.org) | 2 | "Date on which the content on this web page was last reviewed for accuracy and/or completeness." [source](https://schema.org/version/latest/schemaorg-current-https.ttl) | **related but not a fit**; named in the RO-Crate 1.2 context. The past review, not the next. |
| `schema:expires` (schema.org) | 2 | "Date the content expires and is no longer useful or available. For example a VideoObject or NewsArticle whose availability or relevance is time-limited, a ClaimReview fact check whose publisher wants to indicate that it may no longer be relevant (or helpful ..." [source](https://schema.org/version/latest/schemaorg-current-https.ttl) | **irrelevant**; named in the RO-Crate 1.2 context. Content expiry, a different meaning. |

**Evidence:** `dcterms:date`: verified at source

### 53. `oht:inclusion`

**Coined definition:** why the library holds the record: core, comparator, adjacent, context. (Triage group: domain or editorial.)

**Proposed verdict: Keep.** The library's own reason for holding a record.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `skos:editorialNote` (SKOS) | 1 | "A note for an editor, translator or maintainer of the vocabulary." [source](http://www.w3.org/2004/02/skos/core.rdf) | **related but not a fit**. Prose; the value is a filterable category. |

**Evidence:** no standard term recommended; candidates read at source and judged not to fit.

### 54. `oht:humanReview`

**Coined definition:** summary on the record of the review status in its bundle. (Triage group: mechanical.)

**Proposed verdict: Drop.** Duplicates the path through the review.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `dcterms:type` (DCMI Terms) | 1 | "The nature or genre of the resource." [source](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl) | **irrelevant**; named in DCAT-AP 3 (not mandatory). Not needed once dropped. |

**Evidence:** no standard term recommended; candidates read at source and judged not to fit.

### 55. `oht:hasOpenQuestion`

**Coined definition:** attaches an open question to a record. (Triage group: pattern.)

**Proposed verdict: Drop.** With item 8, the annotation points at the record with oa:hasTarget.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `oa:hasTarget` (Web Annotation) | 1 | "The relationship between an Annotation and its Target." [source](https://www.w3.org/ns/oa.ttl) | **exact fit**. 'The relationship between an Annotation and its Target.' |

**Evidence:** `oa:hasTarget`: verified at source

### 56. `oht:resolution`

**Coined definition:** how an open question was resolved. (Triage group: mechanical.)

**Proposed verdict: Replace.** Record the resolution as a reply annotation (oa:replying) whose body is the resolution text.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `oa:replying` (Web Annotation) | 1 | "The motivation for when the user intends to reply to a previous statement, either an Annotation or another resource." [source](https://www.w3.org/ns/oa.ttl) | **exact fit**. Motivation for the reply. |
| `oa:hasBody` (Web Annotation) | 1 | "The object of the relationship is a resource that is a body of the Annotation." [source](https://www.w3.org/ns/oa.ttl) | **exact fit**. The resolution text. |
| `skos:historyNote` (SKOS) | 1 | "A note about the past state/use/meaning of a concept." [source](http://www.w3.org/2004/02/skos/core.rdf) | **related but not a fit**. About past concept states. |

**Evidence:** `oa:replying`: verified at source; `oa:hasBody`: verified at source

### 57. `oht:release`

**Coined definition:** the library release label in which a record state was published. (Triage group: pattern.)

**Proposed verdict: Replace.** Use dcat:version on the record state.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `dcat:version` (DCAT 3) | 1 | "The version indicator (name or identifier) of a resource." [source](https://www.w3.org/ns/dcat.ttl) | **exact fit**; named in DCAT-AP 3 (not mandatory). A release label; DCAT-AP names it. |
| `pav:version` (PAV) | 2 | "The version number of a resource. This is a freetext string, typical values are "1.5" or "21". The URI identifying the previous version can be provided using prov:previousVersion. This property is normally used in a functional way, although PAV does not ..." [source](http://purl.org/pav/) | **related but not a fit**. Tier 2 alternative. |
| `owl:versionInfo` (OWL 2) | 1 | "The annotation property that provides version information for an ontology or another OWL construct." [source](https://www.w3.org/2002/07/owl.ttl) | **related but not a fit**. For ontologies. |

**Evidence:** `dcat:version`: verified at source

### 58. `oht:redistributable`

**Coined definition:** whether the archived copy may be republished. (Triage group: pattern.)

**Proposed verdict: Replace.** Use dcterms:accessRights with the EU access-right table (PUBLIC, RESTRICTED, NON_PUBLIC), as DCAT-AP does; add an ODRL policy only if redistribution terms need to be precise.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `dcterms:accessRights` (DCMI Terms) | 1 | "Information about who access the resource or an indication of its security status." [source](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl) | **exact fit**; named in DCAT-AP 3 (not mandatory). Who may access the archived copy; DCAT-AP harvesters understand it with the EU table. |
| `access-right:NON_PUBLIC` (EU access-right authority table) | 2 | "access status for resources that are not publicly accessible for privacy, security or other reasons" [source](http://publications.europa.eu/resource/authority/access-right/NON_PUBLIC) | **exact fit**. Value. |
| `odrl:distribute` (ODRL) | 1 | "To supply the Asset to third-parties." [source](https://www.w3.org/ns/odrl/2/ODRL22.ttl) | **related but not a fit**. The precise action ('To supply the Asset to third-parties') inside an ODRL policy. |
| `dcterms:license` (DCMI Terms) | 1 | "A legal document giving official permission to do something with the resource." [source](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl) | **related but not a fit**; named in DCAT-AP 3 (not mandatory). The source's licence; complements. |

**Evidence:** `dcterms:accessRights`: verified at source; `access-right:NON_PUBLIC`: verified at source (specification text)

### 59. `oht:redactions`

**Coined definition:** for a published derived copy, what was removed and kept. (Triage group: mechanical.)

**Proposed verdict: Keep under standard superclass or superproperty.** Declare oht:redactions rdfs:subPropertyOf dcterms:description (or skos:note); dcterms:provenance is about custody, not content edits.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `dcterms:provenance` (DCMI Terms) | 1 | "A statement of any changes in ownership and custody of the resource since its creation that are significant for its authenticity, integrity, and interpretation." [source](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl) | **related but not a fit**; named in DCAT-AP 3 (not mandatory). 'changes in ownership and custody'; its usage note allows 'changes successive custodians made', a stretch for redactions. |
| `dpv:DataRedaction` (DPV core) | 2 | "Removal of sensitive information from a data or document" [source](https://w3id.org/dpv) | **related but not a fit**. A technical measure concept, not a statement. |
| `dcterms:description` (DCMI Terms) | 1 | "An account of the resource." [source](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl) | **fits as superclass or superproperty**. Safe parent. |

**Evidence:** `dcterms:description`: verified at source

### 60. `oht:hasHumanReview`

**Coined definition:** attaches the review to a record. (Triage group: mechanical.)

**Proposed verdict: Drop.** The review activity prov:used the record; no forward link needed.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `prov:used` (PROV-O) | 1 | "A prov:Entity that was used by this prov:Activity. For example, :baking prov:used :spoon, :egg, :oven ." [source](https://www.w3.org/ns/prov.ttl) | **exact fit**. Inverse direction. |
| `schema:review` (schema.org) | 2 | "A review of the item." [source](https://schema.org/version/latest/schemaorg-current-https.ttl) | **related but not a fit**; named in the RO-Crate 1.2 context. For schema:Review objects. |

**Evidence:** `prov:used`: verified at source

### 61. `oht:reviewStatus`

**Coined definition:** none, sampled, full, on the review. (Triage group: mechanical.)

**Proposed verdict: Replace.** Use dcterms:type on the review.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `dcterms:type` (DCMI Terms) | 1 | "The nature or genre of the resource." [source](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl) | **exact fit**; named in DCAT-AP 3 (not mandatory). One type slot on a review. |

**Evidence:** `dcterms:type`: verified at source

### 62. `oht:toolPath`

**Coined definition:** where a tool lives in the repository. (Triage group: mechanical.)

**Proposed verdict: Replace.** Type the tool schema:SoftwareSourceCode and give schema:codeRepository a URL to the path in the repository.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `schema:codeRepository` (schema.org) | 2 | "Link to the repository where the un-compiled, human readable code and related code is located (SVN, GitHub, CodePlex)." [source](https://schema.org/version/latest/schemaorg-current-https.ttl) | **exact fit**; named in the RO-Crate 1.2 context. Link to where the code lives; a path URL within the repository is normal practice, and RO-Crate names the property. |
| `doap:repository` (DOAP) | 2 | "Source code repository." [source](http://usefulinc.com/ns/doap) | **related but not a fit**.  Repository object, not a path. |
| `dcterms:identifier` (DCMI Terms) | 1 | "An unambiguous reference to the resource within a given context." [source](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl) | **related but not a fit**; named in DCAT-AP 3 (not mandatory). Too general. |

**Evidence:** `schema:codeRepository`: verified at source

### 63. `oht:commit`

**Coined definition:** the git commit of a run or change. (Triage group: mechanical.)

**Proposed verdict: Keep.** doap:revision is for software releases; a commit hash on a run has no standard property.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `doap:revision` (DOAP) | 2 | "Revision identifier of a software release." [source](http://usefulinc.com/ns/doap) | **related but not a fit**. Domain doap:Version. |
| `dcterms:identifier` (DCMI Terms) | 1 | "An unambiguous reference to the resource within a given context." [source](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl) | **related but not a fit**; named in DCAT-AP 3 (not mandatory). Identifies the resource itself, not the code it ran. |

**Evidence:** no standard term recommended; candidates read at source and judged not to fit.

### 64. `oht:session`

**Coined definition:** links a model agent to its session. (Triage group: pattern.)

**Proposed verdict: Drop.** The session prov:wasAssociatedWith the agent.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `prov:wasAssociatedWith` (PROV-O) | 1 | "An prov:Agent that had some (unspecified) responsibility for the occurrence of this prov:Activity." [source](https://www.w3.org/ns/prov.ttl) | **exact fit**. Inverse direction. |

**Evidence:** `prov:wasAssociatedWith`: verified at source

### 65. `oht:archiveStatus`

**Coined definition:** not_archived, private, public. (Triage group: mechanical.)

**Proposed verdict: Replace.** Split the two facts: whether a transcript exists (its presence), and its dcterms:accessRights (EU table).

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `dcterms:accessRights` (DCMI Terms) | 1 | "Information about who access the resource or an indication of its security status." [source](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl) | **exact fit**; named in DCAT-AP 3 (not mandatory). Private versus public. |
| `access-right:PUBLIC` (EU access-right authority table) | 2 | "access status for resources that are publicly accessible" [source](http://publications.europa.eu/resource/authority/access-right/PUBLIC) | **exact fit**. Value. |

**Evidence:** `dcterms:accessRights`: verified at source; `access-right:PUBLIC`: verified at source (specification text)

### 66. `oht:transcript`

**Coined definition:** the archived full transcript of a session. (Triage group: pattern.)

**Proposed verdict: Drop.** The session prov:generated the transcript.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `prov:generated` (PROV-O) | 1 | "Generation is the completion of production of a new entity by an activity. [prov:generated is listed as the inverse of prov:wasGeneratedBy in DCAT 3, section 7]" [source](https://www.w3.org/TR/prov-o/#Generation) | **exact fit**. Activity to entity it produced. |
| `schema:transcript` (schema.org) | 2 | "If this MediaObject is an AudioObject or VideoObject, the transcript of that object." [source](https://schema.org/version/latest/schemaorg-current-https.ttl) | **related but not a fit**; named in the RO-Crate 1.2 context. Audio and video transcripts. |

**Evidence:** `prov:generated`: verified at source (specification text)

### 67. `oht:excerpt`

**Coined definition:** the published redacted excerpt of a transcript. (Triage group: pattern.)

**Proposed verdict: Drop.** Type the excerpt bibo:Excerpt and link it with prov:wasDerivedFrom to the transcript.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `prov:wasDerivedFrom` (PROV-O) | 1 | "A derivation is a transformation of an entity into another, an update of an entity resulting in a new one, or the construction of a new entity based on a pre-existing entity." [source](https://www.w3.org/ns/prov.ttl) | **exact fit**; named in the RO-Crate 1.2 context. Excerpt derived from transcript. |
| `bibo:Excerpt` (BIBO) | 2 | "A passage selected from a larger work." [source](http://purl.org/ontology/bibo/) | **exact fit**. 'A passage selected from a larger work.' |
| `cito:includesExcerptFrom` (CiTO) | 2 | "A relation according to which the citing entity includes one or more excerpts from the cited entity." [source](http://purl.org/spar/cito) | **related but not a fit**. Citation-level. |
| `dcterms:hasPart` (DCMI Terms) | 1 | "A related resource that is included either physically or logically in the described resource." [source](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl) | **related but not a fit**; named in DCAT-AP 3 (not mandatory). The excerpt is redacted, so not simply a part. |

**Evidence:** `prov:wasDerivedFrom`: verified at source; `bibo:Excerpt`: verified at source

### 68. `oht:locator`

**Coined definition:** where in the transcript the agent's work is. (Triage group: pattern.)

**Proposed verdict: Replace.** Use bibo:locator on a part of the transcript, as elsewhere in the graph.

| Candidate | Tier | Definition at source | Fit |
|---|---|---|---|
| `bibo:locator` (BIBO) | 2 | "A description (often numeric) that locates an item within a containing document or collection." [source](http://purl.org/ontology/bibo/) | **exact fit**. 'A description (often numeric) that locates an item within a containing document'. |

**Evidence:** `bibo:locator`: verified at source

