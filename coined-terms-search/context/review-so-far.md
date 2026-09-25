# Review so far (items 1-20)

This is a second opinion on `COINED-TERMS-REVIEW.md`, from a conversation with Claude. It is not authoritative. "Verified" means a search during that conversation confirmed the term exists and what it means; "memory" means it was recalled without checking. Treat memory items as leads to verify.

## Verdicts

| # | Coined term | Agent's verdict | Second review | Candidate terms | Evidence |
|---|---|---|---|---|---|
| 1 | oht:Record | Holds | Replace | `dcat:CatalogRecord` with `foaf:primaryTopic` to the scheme; optionally keep oht:Record as a subclass | verified (DCAT spec) |
| 2 | oht:Version | Holds | Replace | DCAT 3 versioning: `dcat:version`, `dcat:previousVersion`, `dcat:hasVersion` / `dcat:isVersionOf`, `dcat:hasCurrentVersion`; `adms:versionNotes` | verified |
| 3 | oht:Change | Holds | Keep | Prior art: skos-history (`sh:SchemeDelta`, deltas as insertion and deletion graphs), which complements rather than replaces it | verified |
| 4 | oht:Axis | Holds | Keep, as `rdfs:subClassOf skos:ConceptScheme` | Analogue: RDF Data Cube `qb:DimensionProperty` with `qb:codeList` | memory |
| 5 | oht:OutputSpec | Holds | Replace | `ssn:Output`, `ssn:hasOutput`, with the classifier as `sosa:Procedure` (defined to include algorithms). This moves the output onto the classifier, separate from the category scheme | verified |
| 6 | oht:Uptake | Holds | Keep, as a subclass of `duv:Usage` | `duv:Usage`, `duv:hasUsage` (their definitions lean towards usage guidance); CiTO for pure citations; `nkos:usedBy` still to check | verified (DUV); NKOS unchecked |
| 7 | oht:NoMatch | Holds | Replace | SSSOM convention: `sssom:NoTermFound` as the object; `predicate_modifier` Not for negation. It also duplicates the `no_match` value of item 45 | verified (SSSOM issue 245, spec field) |
| 8 | oht:OpenQuestion | Holds | Replace | `oa:Annotation` with `oa:motivatedBy oa:questioning`; resolution as a reply annotation (`oa:replying`); keep `adms:status` | verified only via TEI's rendering of the motivations; check the W3C Web Annotation Vocabulary directly |
| 9 | oht:HumanReview | Weak | Replace | `prov:Activity` plus a `dcterms:type` value. The example asserts a review with status "none", which is a review that never happened | memory |
| 10 | oht:Session | Weak | Replace | `prov:Activity` plus `dcterms:type`, model as `prov:SoftwareAgent`; transcript as `schema:Conversation` with `schema:Message` parts; precedent: RO-Crate `CreateAction` with `instrument`; prior art: PROV-AGENT (research stage) | verified |
| 11 | oht:family | Weak | Replace | `dcterms:type`, with values from both the NKOS KOS Types vocabulary and a local family scheme; SHACL qualified value shapes to require one of each | NKOS verified; SHACL memory |
| 12 | oht:classifies | Holds | Keep | Analogue: DDI `disco:analysisUnit` (its domain is studies and variables, so not a fit) | verified |
| 13 | oht:purpose | Weak | Keep, as `rdfs:subPropertyOf dcterms:description` | | memory |
| 14 | oht:legalStatus | Holds | Keep, but trim values | "commercial" and "academic" describe the publisher, not legal force | reasoning |
| 15 | oht:statusDate | Holds | Keep, as `rdfs:subPropertyOf dcterms:date` | | memory (dcterms:date definition) |
| 16 | oht:sunsetDate | Weak | Replace | `schema:expires` | memory |
| 17 | oht:severityEncoding | Holds | Keep | Add a SHACL check: "on_axis" or "both" requires a severity axis | reasoning |
| 18 | oht:hasConcept | Holds | Drop | JSON-LD `@reverse` of `skos:inScheme` in the context; `schema:hasDefinedTerm` if a stored forward link is ever needed | memory |
| 19 | oht:primarySource | Replace | Replace | `prov:hadPrimarySource` (covers every issuer-produced source), plus `cito:citesAsAuthority` to single out the authoritative text | verified |
| 20 | oht:sourceType | Weak | Drop | Primary versus secondary is relative to the citing scheme, so it belongs on the relation (`prov:hadPrimarySource` versus `prov:wasDerivedFrom`), not on the document as the example has it | verified (PROV definition) |

Tally: keep 8, remove 12.

## Other findings

- `adms:version` does not exist. ADMS uses `owl:versionInfo`; DCAT 3 has `dcat:version`. The review uses `adms:version` in items 2 and 57. Verified.
- NKOS Application Profile (`http://w3id.org/nkos#`) is a DCMI profile for describing knowledge organisation systems. It defines alignedWith, basedOn, serviceOffered, sizeNote, updateFrequency and usedBy, and uses `dcterms:type` with the NKOS KOS Types vocabulary. It is a draft at version 0.2, last modified 2019, so tier 3. Possibly relevant to items 6, 11, 39 and 41. Existence verified; property definitions not checked.
- DPV (W3C Data Privacy Vocabularies and Controls Community Group) has core risk concepts: Risk, Severity, Likelihood, Consequence, Impact, RiskMitigation. It also has a RISK extension and legal extensions. It is not on the W3C standards track, but is actively maintained, so tier 2. Possibly relevant to items 31 and 36. Verified.
- Recurring rule: every coined note-like or date-like property should declare its standard superproperty (`dcterms:description`, `dcterms:date`, `skos:note`), so generic tools still understand it.
- Open modelling question: does `wef:` denote the issuer's scheme or the library's rendering of it? The answer affects whether PROV derivation statements (items 19, 20, 49) are correct.

## Tiers

1. **Depend freely:** W3C Recommendations and equivalent formal standards (SKOS, DCAT, PROV, SSN/SOSA, Web Annotation, ODRL, ORG, OWL-Time, DCMI Terms).
2. **Depend, knowing they are frozen or community-run:** W3C Notes (DUV), SEMIC Recommendations (ADMS 2.0, published February 2024), and actively governed community standards (SSSOM, schema.org, RO-Crate, DPV).
3. **Cite and align, do not require:** drafts and single-maintainer projects (NKOS AP, skos-history, PROV-AGENT). Put the correspondence in a separate alignment file (`rdfs:subPropertyOf`, `skos:closeMatch`) that can be dropped without changing data.

## Criteria for choosing vocabularies to check

1. Coverage of the ontology's jobs: include the leading standard for each job, whether or not it has produced a match yet.
2. Standing: the tiers above. Search every tier; the tier governs adoption, not discovery.
3. Adoption: evidence of real use.
4. Definition quality: terms need usable definitions.
