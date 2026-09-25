# Coined terms: meaning, example, nearest existing term, verdict

**Status:** review of the 68 terms in `ontology/oht.ttl` at schema set 0.7.0, written 2026-09-25. Companion to `ontology/MAPPING.md` section 9. The verdicts are proposals; adopting them is decision 0009.

Examples are Turtle. These prefixes are declared once so every example is a valid statement:

```
@prefix oht:  <https://w3id.org/oht/ontology#> .
@prefix ohtv: <https://w3id.org/oht/vocab/> .
@prefix wef:  <https://w3id.org/oht/id/taxonomy/wef-typology-online-harms/> .
@prefix oai:  <https://w3id.org/oht/id/taxonomy/openai-moderation/> .
@prefix xw:   <https://w3id.org/oht/id/crosswalk/wef-typology-to-openai-moderation/> .
@prefix src:  <https://w3id.org/oht/id/source/> .
@prefix ag:   <https://w3id.org/oht/id/agent/> .
@prefix g:    <https://w3id.org/oht/graph/> .
@prefix b:    <https://w3id.org/oht/graph/provenance/wef-typology-online-harms/> .
```

plus the standard `skos:`, `xkos:`, `adms:`, `dcterms:`, `prov:`, `xsd:`. `wef:` with no local name means the scheme itself. For each term: meaning, example, the nearest existing term, and whether the coin holds up.

Verdicts: **Holds** = no standard term carries the meaning. **Weak** = a standard term or a generic `dcterms:type` would serve; the coin buys only readability. **Replace** or **Drop** = an existing term fits and was missed.

## Classes

1. `oht:Record` - a named graph holding one library record; the library's statements are made about this IRI.
   `g:taxonomy/wef-typology-online-harms a oht:Record ; oht:verification ohtv:verification/secondary_only .`
   Nearest: `prov:Entity` (its superclass) and `dcat:Dataset`. Neither distinguishes "a graph the library curates" from documents, record states or datasets, and the shapes need a target class. **Holds.**

2. `oht:Version` - one published release of a taxonomy; concept IRIs stay stable across versions.
   `wef:version/2023 a oht:Version ; adms:version "2023" .`
   Nearest: XKOS practice, one `skos:ConceptScheme` per version, and `adms:Asset` per version. The XKOS approach changes every concept IRI on each release; ADMS's Asset implies a distributable asset. **Holds.**

3. `oht:Change` - one change a version made.
   `oai:version/omni-moderation-latest/change/1 a oht:Change ; oht:changeType ohtv:change-type/added .`
   Nearest: `skos:changeNote` (free text, unstructured) and `prov:Activity`. PROV activities in this graph are the library's own process; typing issuer changelog entries as activities would make provenance queries return issuer history. **Holds.**

4. `oht:Axis` - a classification dimension other than the hierarchy, as a small concept scheme of values.
   `wef:axis/route a oht:Axis ; oht:axisKind ohtv:axis-kind/categorical .`
   Nearest: `skos:Collection` (groups concepts of the scheme; carries no "takes a value from" semantics, and axis values are not concepts of the taxonomy) and `xkos:ClassificationLevel` (levels of one hierarchy, not orthogonal dimensions). **Holds.**

5. `oht:OutputSpec` - how a classifier reports a concept.
   `oai: oht:hasOutput [ a oht:OutputSpec ; oht:outputType ohtv:output-type/probability ] .`
   Nearest: `schema:PropertyValueSpecification` (constraints on form inputs) and `qb:MeasureProperty` (statistical observations). Neither describes a classifier's output. **Holds.**

6. `oht:Uptake` - one piece of evidence that someone uses the scheme.
   `wef:uptake/1 a oht:Uptake ; oht:uptakeKind ohtv:uptake-kind/regulatory_citation .`
   Nearest: `dcterms:isReferencedBy` and CiTO. Citation is one kind of uptake; adoption, integration and benchmark use are not citations, and the library's judgement of strength has no home there. **Holds.**

7. `oht:NoMatch` - an association asserting its source has no counterpart.
   `xw:m-008 a oht:NoMatch ; xkos:sourceConcept wef:scams .`
   Nearest: an `xkos:ConceptAssociation` with no target, which XKOS permits but cannot distinguish from an omission. **Holds**, as a marker subclass.

8. `oht:OpenQuestion` - an unresolved editorial point about a record.
   `g:taxonomy/wef-typology-online-harms/question/seventh-category a oht:OpenQuestion ; adms:status ohtv:question-status/open .`
   Nearest: `skos:editorialNote` (no status or resolution) and `schema:Question` (Q&A web pages). **Holds.**

9. `oht:HumanReview` - a person's review of a record.
   `b:review a oht:HumanReview ; oht:reviewStatus ohtv:human-review/none .`
   Nearest: `prov:Activity` with a `dcterms:type`. That works; the class exists for SHACL targeting and readability. **Weak**: replaceable by `prov:Activity` plus a vocabulary value.

10. `oht:Session` - a drafting session with a language model, as an activity.
    `b:session/claude a oht:Session ; oht:archiveStatus ohtv:archive-status/not_archived .`
    Nearest: `prov:Activity` (same argument as 9) and `schema:Conversation`, which is the transcript as a creative work, not the activity, and could additionally type the transcript document. **Weak**, same as 9.

## What kind of scheme, and its standing

11. `oht:family` - what kind of scheme this is.
    `wef: oht:family ohtv:family/harm_taxonomy .`
    Nearest: `dcterms:type`. It would do; a dedicated property was coined so that three classifications of a scheme (family, what it classifies, legal status) were not one generic slot and two specific ones. **Weak**: replaceable by `dcterms:type`.

12. `oht:classifies` - the unit the scheme sorts.
    `oai: oht:classifies ohtv:classifies/content_item .`
    Nearest: `xkos:covers` (the field a classification covers) and `dcterms:subject` (topic). WEF and OpenAI both cover online harms but sort different units, a harm versus a content item; neither term expresses that. **Holds.**

13. `oht:purpose` - what the issuer says the scheme is for.
    `wef: oht:purpose "Common terminology for cross-border discussion of online safety"@en .`
    Nearest: `dcterms:description`. Purpose is a distinct statement readers compare across schemes, but it could live in the description. **Weak.**

14. `oht:legalStatus` - statutory, guidance, voluntary, commercial, academic.
    `wef: oht:legalStatus ohtv:legal-status/voluntary_standard .`
    Nearest: `adms:status`, which is lifecycle (active, deprecated), orthogonal to legal force. **Holds.**

15. `oht:statusDate` - when the current `adms:status` began.
    `src:perspective-api oht:statusDate "2026-02-01"^^xsd:date .`
    Nearest: `dcterms:modified` (last content change, which can differ) and `dcterms:valid` (validity interval, hard to query). ADMS gives status no date. **Holds**, until ADMS reifies status.

16. `oht:sunsetDate` - the announced date after which a scheme or service ceases.
    `src:perspective-api oht:sunsetDate "2026-12-31"^^xsd:date .`
    Nearest: `schema:expires`. Close enough that it should probably be used. **Weak**: replaceable by `schema:expires`.

17. `oht:severityEncoding` - where severity lives: nowhere, in the hierarchy, on an axis, both.
    `oai: oht:severityEncoding ohtv:severity-encoding/in_hierarchy .`
    Nearest: `skos:note`. A structural fact users filter on, not prose. **Holds.**

18. `oht:hasConcept` - declared inverse of `skos:inScheme`.
    `wef: oht:hasConcept wef:csam .`
    Nearest: `skos:hasTopConcept` (top concepts only); SKOS deliberately has no inverse of `inScheme`. **Holds**, as a convenience for JSON-LD framing.

19. `oht:primarySource` - the authoritative text for the scheme.
    `wef: oht:primarySource src:wef-typology-pdf-2023 .`
    Nearest: `prov:hadPrimarySource`, which exists for exactly this and was missed. **Replace.**

20. `oht:sourceType` - primary, secondary, tertiary, relative to the citing scheme.
    `src:wef-explainer-2023-09 oht:sourceType ohtv:source-type/primary .`
    Nearest: `prov:hadPrimarySource` for the primary case; the others are "everything else". **Weak**: drop once 19 is replaced.

## Versions and changes

21. `oht:hasChange` - a version lists a change.
    `oai:version/omni-moderation-latest oht:hasChange oai:version/omni-moderation-latest/change/1 .`
    Nearest: `dcterms:hasPart`. Semantically thin either way; coined only for readability. **Weak.**

22. `oht:changeType` - added, removed, renamed, redefined, moved, merged, split, reclassified.
    `oai:version/omni-moderation-latest/change/1 oht:changeType ohtv:change-type/added .`
    Nearest: `dcterms:type`. **Weak**, as 11.

23. `oht:affectsConcept` - the concept a change touched.
    `oai:version/omni-moderation-latest/change/1 oht:affectsConcept oai:illicit .`
    Nearest: `dcterms:subject` (topic, odd for an operand) and `prov:used`, which would require Change to be an Activity (see 3). **Holds.**

24. `oht:officialMapping` - the issuer's own crosswalk from the previous version.
    `<iab-content-taxonomy/version/3.0> oht:officialMapping <https://iabtechlab.com/.../mapping.tsv> .`
    Nearest: an `xkos:Correspondence` attributed to the issuer. Modelling the mapping as a correspondence would make this property unnecessary. **Weak.**

25. `oht:introducedIn` - the version in which a concept first appeared.
    `oai:illicit oht:introducedIn oai:version/omni-moderation-latest .`
    Nearest: `prov:generatedAtTime` (a timestamp, not an issuer's version label) and XKOS's scheme-per-version. **Holds.**

26. `oht:retiredIn` - the version in which a concept was removed; the IRI remains.
    `wef:some-concept oht:retiredIn wef:version/2027 .`
    Nearest: `prov:invalidatedAtTime`, `owl:deprecated` (a flag with no version). **Holds.**

## Axes, facets, outputs

27. `oht:hasAxis` - a scheme declares an axis.
    `wef: oht:hasAxis wef:axis/route .`
    Nearest: `dcterms:hasPart`. **Weak**, as 21.

28. `oht:axisKind` - ordinal or categorical.
    `wef:axis/route oht:axisKind ohtv:axis-kind/categorical .`
    Nearest: `dcterms:type`. **Weak**, as 11.

29. `oht:multiValued` - whether a concept may take several values on the axis.
    `wef:axis/route oht:multiValued true .`
    Nearest: `owl:FunctionalProperty`, which would need one property per axis. **Holds.**

30. `oht:hasFacetValue` - a concept takes a value from one of its scheme's axes.
    `wef:bullying-harassment oht:hasFacetValue wef:axis/route/conduct .`
    Nearest: `skos:related` (associative, no classification semantics) or one property per axis. **Holds.**

31. `oht:consequence` - what follows from a concept or value in the scheme.
    `<garm/axis/risk-level/floor> oht:consequence "Not eligible for monetisation"@en .`
    Nearest: `skos:scopeNote`. A consequence is a kind of note users filter on; the right fix is to keep it and declare it `rdfs:subPropertyOf skos:note`. **Holds**, with that addition.

32. `oht:hasOutput` - attaches an output specification.
    `oai: oht:hasOutput oai:output .`
    Follows 5. **Holds** with 5.

33. `oht:outputType` - boolean, probability, ordinal, score, none.
    `oai:output oht:outputType ohtv:output-type/boolean , ohtv:output-type/probability .`
    Nearest: `dcterms:type`. **Weak**, as 11.

34. `oht:outputAxis` - for ordinal outputs, the axis returned.
    `<azure/output> oht:outputAxis <azure/axis/severity> .`
    No standard term describes a classifier's output scale. **Holds.**

## Concept attributes with no standard home

35. `oht:modality` - the kind of input a concept applies to.
    `oai:harassment oht:modality ohtv:modality/text .`
    Nearest: `dcterms:format`, `dcterms:medium`, `schema:encodingFormat`, all of which describe the resource itself, not what a concept applies to. **Holds.**

36. `oht:legalBasis` - the provision behind a concept, as an ELI legal resource.
    `<ofcom/csam> oht:legalBasis <https://www.legislation.gov.uk/ukpga/2023/50/schedule/6> .`
    Nearest: `eli:based_on` and `eli:implements` (domain restricted to legal resources; a concept is not one) and `dcterms:source` (already used for bibliographic sources; overloading it blurs text origin with legal footing). **Holds.**

37. `oht:contextDependent` - the scheme says the concept's status depends on deployment context.
    `wef:algorithmic-discrimination oht:contextDependent true .`
    Nearest: `skos:note`. **Holds.**

38. `oht:verbatim` - on an explanatory note, whether the text is the source's exact words.
    `[ a xkos:ExplanatoryNote ; xkos:plainText "..."@en ; oht:verbatim false ] .`
    Nearest: `prov:Quotation` (a PROV derivation subclass for repeating an entity's content) and `cito:includesQuotationFrom`. Either expresses "verbatim" as a typed derivation rather than a flag. **Replace.**

## Relations between schemes

39. `oht:operationalises` - this scheme turns the target's duties or principles into practice.
    `<ofcom-icu> oht:operationalises <uk-online-safety-act> .`
    Nearest: `eli:implements` and `eli:transposes` (legal resource to legal resource; a code of practice is a scheme here, not a legal resource) and `dcterms:conformsTo` (conformance, not implementation). **Holds.**

40. `oht:operationalisedBy` - the inverse. **Holds** with 39.

41. `oht:conflictsWith` - the two schemes make incompatible claims about the same field.
    `oai: oht:conflictsWith <google-perspective-api> .`
    Nearest: `xkos:disjoint` (concepts with no common instances) and `owl:disjointWith` (classes). Conflict of categorisation is neither. **Holds.**

## Uptake

42. `oht:hasUptake` - attaches uptake evidence.
    `wef: oht:hasUptake wef:uptake/1 .`
    Follows 6. **Holds** with 6.

43. `oht:uptakeKind` - regulatory citation, platform adoption, benchmark use, and so on.
    `wef:uptake/1 oht:uptakeKind ohtv:uptake-kind/regulatory_citation .`
    Nearest: `dcterms:type`. **Weak**, as 11.

44. `oht:strength` - strong, moderate, weak, as the library judges evidence.
    `wef:uptake/1 oht:strength ohtv:strength/strong .`
    Nearest: `oht:confidence` itself. One judgement scale would do. **Weak**: merge with 46.

## Mappings

45. `oht:mappingRelation` - the relation an association asserts, including no_match.
    `xw:m-001 oht:mappingRelation ohtv:mapping-relation/close_match .`
    Nearest: the SKOS mapping property asserted between the concepts (which cannot say no_match) and `dcterms:type` on the association. **Weak**: `dcterms:type` would serve.

46. `oht:confidence` - issuer_asserted, high, medium, low.
    `xw:m-001 oht:confidence ohtv:confidence/high .`
    Nearest: SSSOM, the Simple Standard for Sharing Ontology Mappings, which has `sssom:confidence` (numeric) and `sssom:mapping_provider`. Who stands behind a mapping and how sure they are is close to SSSOM's model; the categorical value has no SSSOM equivalent. **Holds** for the categorical value; see 47.

47. `oht:score` - numeric confidence 0 to 1.
    `xw:m-001 oht:score 0.85 .`
    Nearest: `sssom:confidence`, which is exactly this. **Replace.**

48. `oht:method` - how a record or crosswalk was produced.
    `g:taxonomy/wef-typology-online-harms oht:method ohtv:production-method/llm_assisted .`
    Nearest: for crosswalks, `sssom:mapping_justification` with the SEMAPV vocabulary (manual curation, lexical matching, and so on); for records, a `prov:wasGeneratedBy` activity of a given type. The property is a shortcut for the PROV pattern. **Weak** for records; **Replace** for crosswalks.

## How things were derived and reviewed

49. `oht:derivationMethod` - how an item relates to its source: authored, verbatim, transcribed, paraphrased, translated, converted, inferred, llm_drafted, mixed.
    `wef:csam prov:qualifiedDerivation [ oht:derivationMethod ohtv:derivation-method/transcribed ; prov:entity src:wef-explainer-2023-09 ] .`
    Nearest: PROV's derivation subclasses (`prov:Quotation`, `prov:Revision`, `prov:PrimarySource`), which cover verbatim and little else. **Holds** for the remaining values.

50. `oht:reviewed` - a person has checked this item against its source.
    `[ oht:derivationMethod ohtv:derivation-method/paraphrased ; oht:reviewed false ] .`
    Nearest: a review activity that `prov:used` the item. The boolean is a shortcut. **Weak.**

51. `oht:verification` - verified_primary, secondary_only, unverified.
    `g:taxonomy/openai-moderation oht:verification ohtv:verification/verified_primary .`
    Nearest: none; PROV can express the checking activity but not the grade. **Holds.**

52. `oht:reviewDue` - when the record should next be checked.
    `g:taxonomy/wef-typology-online-harms oht:reviewDue "2026-12"^^xsd:gYearMonth .`
    Nearest: `schema:expires` (content expiry, a different meaning). **Holds.**

53. `oht:inclusion` - why the library holds the record: core, comparator, adjacent, context.
    `g:taxonomy/cvss oht:inclusion ohtv:inclusion/comparator .`
    Nearest: `skos:editorialNote`. **Holds.**

54. `oht:humanReview` - summary on the record of the review status in its bundle.
    `g:taxonomy/wef-typology-online-harms oht:humanReview ohtv:human-review/none .`
    Nearest: the path `oht:hasHumanReview/oht:reviewStatus`. Pure duplication. **Drop.**

55. `oht:hasOpenQuestion` - attaches an open question. Follows 8. **Holds** with 8.

56. `oht:resolution` - how an open question was resolved.
    `g:taxonomy/wef-typology-online-harms/question/seventh-category oht:resolution "The PDF contents list shows six categories"@en .`
    Nearest: `skos:historyNote` or `dcterms:description` on the question. **Weak.**

57. `oht:release` - the library release label in which a record state was published.
    `b:event/4/state oht:release "2026.10" .`
    Nearest: `dcat:version` (DCAT 3) on the state, and `adms:version`, which is already used for issuers' version labels and must not be conflated. **Weak**: `dcat:version` would serve.

## Archive

58. `oht:redistributable` - whether the archived copy may be republished.
    `src:wef-typology-pdf-2023 oht:redistributable false .`
    Nearest: `dcterms:accessRights` with the EU access-right vocabulary (public, restricted, non-public), which is how DCAT-AP does it. **Replace.**

59. `oht:redactions` - for a published derived copy, what was removed and kept.
    `src:session-excerpt-crosswalk oht:redactions "Account details and copied page text removed; URLs and model turns kept"@en .`
    Nearest: `dcterms:provenance`, defined as a statement of changes significant for authenticity and integrity, and `rdfs:comment` on the derivation. **Weak**: `dcterms:provenance` fits.

## Provenance bundle details

60. `oht:hasHumanReview` - attaches the review.
    `g:taxonomy/wef-typology-online-harms oht:hasHumanReview b:review .`
    Nearest: the review `prov:used` the record, inverted. **Weak**, as 21.

61. `oht:reviewStatus` - none, sampled, full, on the review.
    `b:review oht:reviewStatus ohtv:human-review/sampled .`
    Nearest: `dcterms:type`. **Weak**, as 11.

62. `oht:toolPath` - where a tool lives in the repository.
    `ag:ofcom-converter oht:toolPath "tools/ofcom" .`
    Nearest: `schema:codeRepository` (a URL to the repository, not a path within it) and `dcterms:identifier`. **Weak.**

63. `oht:commit` - the git commit of a run or change.
    `b:event/4 oht:commit "9f3c2ab" .`
    Nearest: `doap:revision` (revision identifier of a release) and `dcterms:identifier`. **Weak.**

64. `oht:session` - links a model agent to its session.
    `ag:claude oht:session b:session/claude .`
    Nearest: the session's own `prov:wasAssociatedWith ag:claude`, read backwards. **Drop.**

65. `oht:archiveStatus` - not_archived, private, public.
    `b:session/claude oht:archiveStatus ohtv:archive-status/private .`
    Nearest: existence of a transcript plus `dcterms:accessRights` on it. The tri-state bundles two facts that the standards keep apart. **Weak**: decompose.

66. `oht:transcript` - the archived full transcript.
    `b:session/claude oht:transcript src:claude-export-2026-09 .`
    Nearest: `prov:generated`, since the session generated its transcript, with the document typed `session_transcript`. **Drop.**

67. `oht:excerpt` - the published redacted excerpt.
    `b:session/claude oht:excerpt src:session-excerpt-crosswalk .`
    Nearest: the path through the transcript, `prov:generated` then `prov:wasDerivedFrom` inverted, or `dcterms:hasPart`. **Drop.**

68. `oht:locator` - where in the transcript the agent's work is.
    `b:session/claude oht:locator "conversation 6RbpUjafyAE5195ovXBZmh" .`
    Nearest: `bibo:locator` on a `bibo:DocumentPart` of the transcript, which is how every other citation in the graph already works. **Replace.**

## Tally

- **Holds:** 33.
- **Weak** (a standard term or a generic `dcterms:type` would serve; the coin buys only readability): 26.
- **Replace or drop** (an existing term fits and was missed): 9 terms plus `method` for crosswalks: `primarySource`, `sourceType`, `verbatim`, `score`, `humanReview`, `redistributable`, `session`, `transcript`, `excerpt`, `locator`.

Doing the replacements and drops, and folding the `dcterms:type` cases, would bring the ontology to about 35 terms, nearer the twenty predicted than the 68 written. Recommendation: run the review now, while nothing has been converted and every change is free, rather than before 1.0.
