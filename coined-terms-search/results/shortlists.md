# Shortlists (plan step C)

BM25 top 15 plus leads from earlier reviews. Machine output for reading, not judgements.

## 1. oht:Record (P)

a named graph holding one library record; the library's statements are made about this IRI

- bm25+lead 38.94 `http://www.w3.org/ns/dcat#CatalogRecord` [class, tier 1] A record in a data catalog, describing the registration of a single dataset or data service.
- bm25+lead 30.13 `http://www.w3.org/ns/dcat#record` [property, tier 1, DCAT-AP optional/other] A record describing the registration of a single dataset or data service that is part of the catalog.
- bm25 27.5 `http://www.w3.org/ns/dcat#Catalog` [class, tier 1] A curated collection of metadata about resources.
- bm25 26.01 `http://www.w3.org/ns/dqv#QualityMetadata` [class, tier 2] Represents quality metadata, it is defined to group quality certificates, policies, measurements and annotations under a named graph.
- bm25 21.91 `http://www.w3.org/ns/dqv#hasQualityMetadata` [property, tier 2] Refers to a grouping of quality information such as certificates, policies, measurements and annotations as a named graph. Quality information represented in su
- bm25 19.86 `http://purl.org/skos-history/usingNamedGraph` [property, tier 3] The named graph where the data can be queried. (The endpoint should be given as void:sparqlEndpoint property of the version history set.)
- bm25 15.73 `http://www.w3.org/ns/odrl/2/spatial` [individual, tier 1] A named and identified geospatial area with defined borders which is used for exercising the action of the Rule. An IRI MUST be used to represent this value.
- bm25 15.19 `https://schema.org/Library` [class, tier 2, RO-Crate] A library.
- bm25 14.5 `https://w3id.org/dpv#UnknownApplicability` [class, tier 2] Concept indicating information or context availability is unknown i.e. it is not known if the information exists or is applicable and therefore statements about
- bm25 14.45 `http://www.w3.org/ns/dcat#resource` [property, tier 1] A resource that is listed in the catalog.
- bm25 14.41 `https://w3id.org/dpv#ServiceRegistration` [class, tier 2] Purposes associated with registering users and collecting information required for providing a service
- bm25 14.39 `http://purl.org/spar/cito/citesAsMetadataDocument` [property, tier 2] A relation according to which the citing entity cites the cited entity as being the container of metadata describing the citing entity.
- bm25 14.39 `https://w3id.org/vair#Library` [class, tier 3] A collection of pre-written code
- bm25 14.01 `https://schema.org/LibrarySystem` [class, tier 2, RO-Crate] A [[LibrarySystem]] is a collaborative system amongst several libraries.
- bm25 14.0 `http://www.w3.org/2002/07/owl#NamedIndividual` [class, tier 1] The class of named individuals.
- lead 0.0 `http://xmlns.com/foaf/0.1/primaryTopic` [property, tier 2, DCAT-AP mandatory] The primary topic of some page or document.
- lead 0.0 `http://www.w3.org/ns/prov#Entity` [class, tier 1] An entity is a physical, digital, conceptual, or other kind of thing with some fixed aspects; entities may be real or imaginary.
- lead 0.0 `http://www.w3.org/ns/dcat#Dataset` [class, tier 1] A collection of data, published or curated by a single source, and available for access or download in one or more representations.

## 2. oht:Version (P)

one published release of a taxonomy; concept IRIs stay stable across versions

- bm25+lead 27.03 `http://www.w3.org/ns/dcat#previousVersion` [property, tier 1] The previous version of a resource in a lineage [PAV].
- bm25 19.18 `http://usefulinc.com/ns/doap#Version` [class, tier 2] Version information of a project release.
- bm25 18.89 `http://purl.org/pav/previousVersion` [property, tier 2] The previous version of a resource in a lineage. For instance a news article updated to correct factual information would point to the previous version of the a
- bm25 18.6 `https://w3id.org/semapv/vocab/StableMarriageFiltering` [class, tier 2] 
- bm25 17.09 `http://purl.org/skos-history/ConceptVersion` [class, tier 3] (???) A version of a SKOS concept.
- bm25 16.88 `http://purl.org/pav/hasEarlierVersion` [property, tier 2] This versioned resource has an earlier version. Any earlier version of this resource can be indicated with pav:hasEarlierVersion, e.g.: <http://example.com/v4> 
- bm25 16.48 `http://purl.org/ontology/bibo/edition` [property, tier 2] The name defining a special edition of a document. Normally its a literal value composed of a version number and words.
- bm25 16.2 `http://purl.org/dc/terms/isVersionOf` [property, tier 1] A related resource of which the described resource is a version, edition, or adaptation.
- bm25 15.65 `https://schema.org/releaseNotes` [property, tier 2, RO-Crate] Description of what changed in this version.
- bm25 15.52 `http://purl.org/skos-history/ConceptDelta` [class, tier 3] The delta of two versions of a SKOS concept.
- bm25 15.35 `http://data.europa.eu/eli/ontology#Version` [class, tier 2] Formally defined as the set of skos:Concept in concept scheme eli:VersionTable
- bm25 15.2 `http://purl.org/dc/terms/hasVersion` [property, tier 1, DCAT-AP optional/other] A related resource that is a version, edition, or adaptation of the described resource.
- bm25+lead 14.49 `http://www.w3.org/ns/adms#versionNotes` [property, tier 2, DCAT-AP optional/other] A description of changes between this version and the previous version of the Asset.
- bm25+lead 14.23 `http://purl.org/pav/version` [property, tier 2] The version number of a resource. This is a freetext string, typical values are "1.5" or "21". The URI identifying the previous version can be provided using pr
- bm25 13.16 `http://www.w3.org/ns/adms#prev` [property, tier 2] A link to the previous version of the Asset.
- lead 8.53 `http://www.w3.org/ns/dcat#version` [property, tier 1, DCAT-AP optional/other] The version indicator (name or identifier) of a resource.
- lead 7.8 `http://www.w3.org/ns/dcat#hasVersion` [property, tier 1] This resource has a more specific, versioned resource [PAV].
- lead 7.24 `http://www.w3.org/ns/dcat#isVersionOf` [untyped, tier 1] 
- lead 7.38 `http://www.w3.org/ns/dcat#hasCurrentVersion` [property, tier 1] This resource has a more specific, versioned resource with equivalent content [PAV].
- lead 8.0 `http://www.w3.org/2002/07/owl#versionInfo` [property, tier 1] The annotation property that provides version information for an ontology or another OWL construct.
- lead 8.46 `https://schema.org/version` [property, tier 2, RO-Crate] The version of the CreativeWork embodied by a specified resource.
- lead 4.71 `http://www.w3.org/ns/dcat#DatasetSeries` [class, tier 1] A collection of datasets that are published separately, but share some common characteristics that groups them.
- lead 0.0 `http://www.w3.org/ns/adms#Asset` [class, tier 2] An abstract entity that reflects the intellectual content of the asset and represents those characteristics of the asset that are independent of its physical em

## 3. oht:Change (P)

one change a version made (added, removed, renamed, moved and so on)

- bm25+lead 19.97 `http://www.w3.org/ns/prov#Revision` [class, tier 1] A revision is a derivation for which the resulting entity is a revised version of some original. The implication here is that the resulting entity contains subs
- bm25 19.45 `http://purl.org/skos-history/deltaFrom` [property, tier 3] The version from which the delta is taken. The object of the triple may be a dsv:VersionHistoryRecord.
- bm25 18.85 `http://purl.org/skos-history/hasDelta` [property, tier 3] A delta for this version. The subject of the triple may be a dsv:VersionHistoryRecord.
- bm25 17.88 `http://www.w3.org/ns/prov#wasRevisionOf` [property, tier 1] A revision is a derivation that revises an entity into a revised version.
- bm25 17.83 `http://purl.org/skos-history/deltaTo` [property, tier 3] The versions to which the delta is taken. The object of the triple may be a dsv:VersionHistoryRecord.
- bm25 15.54 `http://purl.org/skos-history/ConceptDelta` [class, tier 3] The delta of two versions of a SKOS concept.
- bm25+lead 15.42 `http://purl.org/skos-history/SchemeDelta` [class, tier 3] The delta of two versions of a SKOS concept scheme.
- bm25 15.06 `http://purl.org/skos-history/SchemeDeltaInsertions` [class, tier 3] Should be related to the delta by dcterms:isPartOf.
- bm25 15.06 `http://purl.org/skos-history/SchemeDeltaDeletions` [class, tier 3] Should be related to the delta by dcterms:isPartOf.
- bm25 13.76 `http://usefulinc.com/ns/doap#revision` [property, tier 2] Revision identifier of a software release.
- bm25+lead 13.74 `https://schema.org/UpdateAction` [class, tier 2, RO-Crate] The act of managing by changing/editing the state of the object.
- bm25 13.37 `http://www.w3.org/ns/prov#hadRevision` [untyped, tier 1] 
- bm25 13.36 `https://w3id.org/dpv/ai#UpdateStage` [class, tier 2] The stage in the lifecycle where an AI system is being or has been updated
- bm25 13.32 `https://schema.org/EventMovedOnline` [individual, tier 2, RO-Crate] Indicates that the event was changed to allow online participation. See [[eventAttendanceMode]] for specifics of whether it is now fully or partially online.
- bm25 12.92 `http://www.w3.org/ns/prov#removedKey` [property, tier 1] The key removed in a Removal.
- lead 9.73 `http://www.w3.org/2004/02/skos/core#changeNote` [property, tier 1] A note about a modification to a concept.
- lead 0.0 `http://www.w3.org/ns/prov#Activity` [class, tier 1] An activity is something that occurs over a period of time and acts upon or with entities; it may include consuming, processing, transforming, modifying, reloca

## 4. oht:Axis (P)

a classification dimension other than the hierarchy, as a small concept scheme of values

- bm25 29.54 `http://purl.org/linked-data/cube#HierarchicalCodeList` [class, tier 1] Represents a generalized hierarchy of concepts which can be used for coding. The hierarchy is defined by one or more roots together with a property which relate
- bm25+lead 20.72 `http://rdf-vocabulary.ddialliance.org/xkos#ClassificationLevel` [class, tier 2] 
- bm25 20.69 `http://www.w3.org/ns/org#classification` [property, tier 1] Indicates a classification for this Organization within some classification scheme. Extension vocabularies may wish to specialize this property to have a range 
- bm25 18.97 `http://w3id.org/nkos/nkostype#classification_scheme` [individual, tier 3] schedule of concepts and pre-coordinated combinations of concepts, arranged by classification
- bm25 18.45 `http://www.w3.org/2004/02/skos/core#topConceptOf` [property, tier 1] Relates a concept to the concept scheme that it is a top level concept of.
- bm25 17.13 `http://www.w3.org/2004/02/skos/core#notation` [property, tier 1, DCAT-AP optional/other] A notation, also known as classification code, is a string of characters such as "T58.5" or "303.4833" used to uniquely identify a concept within the scope of a
- bm25 16.91 `http://purl.obolibrary.org/obo/IAO_0000184` [class, tier 2] A scatterplot is a graph which uses Cartesian coordinates to display values for two variables for a set of data. The data is displayed as a collection of points
- bm25+lead 16.78 `http://www.w3.org/2004/02/skos/core#ConceptScheme` [class, tier 1] A set of concepts, optionally including statements about semantic relationships between those concepts.
- bm25 15.6 `http://purl.org/skos-history/SchemeDelta` [class, tier 3] The delta of two versions of a SKOS concept scheme.
- bm25+lead 15.35 `http://purl.org/linked-data/cube#codeList` [property, tier 1] gives the code list associated with a CodedProperty
- bm25 14.79 `http://rdf-vocabulary.ddialliance.org/xkos#levels` [property, tier 2] 
- bm25 14.61 `http://rdf-vocabulary.ddialliance.org/discovery#representation` [property, tier 3] RepresentedVariables and Variables can have a Representation whose individuals are either of the class rdfs:Datatype (to represent values) or skos:ConceptScheme
- bm25 14.59 `http://www.w3.org/2004/02/skos/core#inScheme` [property, tier 1] Relates a resource (for example a concept) to a concept scheme in which it is included.
- bm25 14.43 `http://data.europa.eu/eli/ontology#WorkType` [class, tier 2] 
- bm25 13.77 `http://data.europa.eu/eli/ontology#type_subdivision` [property, tier 2] The type of a document subdivision (e.g. "Article", "Paragraph", "Section", etc.). A subdivision can have only one type. ELI does not specify a list of possible
- lead 11.17 `http://purl.org/linked-data/cube#DimensionProperty` [class, tier 1] The class of components which represent the dimensions of the cube
- lead 0.0 `http://www.w3.org/2004/02/skos/core#Collection` [class, tier 1] A meaningful collection of concepts.
- lead 8.65 `https://schema.org/DefinedTermSet` [class, tier 2, RO-Crate] A set of defined terms, for example a set of categories or a classification scheme, a glossary, dictionary or enumeration. Use the about property to specify wha

## 5. oht:OutputSpec (P)

how a classifier reports a concept (boolean, probability, ordinal, score)

- bm25 22.22 `https://w3id.org/vair#Prediction` [class, tier 3] Primary output of an AI system when provided with input data or information.
- bm25+lead 20.56 `http://www.w3.org/ns/ssn/Output` [class, tier 1] Any information that is reported from a Procedure.
- bm25 17.86 `https://w3id.org/airo#AIModel` [class, tier 3] Mathematical construct that generates an inference or prediction, based on input data.
- bm25 16.81 `https://w3id.org/vair#MachineLearningModel` [class, tier 3] Mathematical construct that generates an inference or prediction based on input data or information.
- bm25 16.81 `https://w3id.org/dpv/ai#MachineLearningModel` [class, tier 2] Mathematical construct that generates an inference or prediction based on input data or information
- bm25+lead 16.1 `http://www.w3.org/ns/ssn/hasOutput` [property, tier 1] Relation between a Procedure and an Output of it.
- bm25 15.67 `https://w3id.org/vair#InaccuratePrediction` [class, tier 3] Inaccurate prediction generated by the system.
- bm25 15.53 `https://schema.org/Boolean` [class, tier 2, RO-Crate] Boolean: True or False.
- bm25 15.06 `https://w3id.org/dpv#PersonnelPerformancePrediction` [class, tier 2] Purposes associated with prediction of performance of personnel
- bm25 15.06 `http://www.w3.org/ns/mls#hasOutput` [property, tier 2] A relation between a run and either a model or model evaluation that is produced on it’s output.
- bm25 14.45 `https://w3id.org/vair#DeterminingCreditScore` [class, tier 3] Determining credit score of a person
- bm25 14.21 `https://schema.org/MedicalRiskScore` [class, tier 2, RO-Crate] A simple system that adds up the number of risk factors to yield a score that is associated with prognosis, e.g. CHAD score, TIMI risk score.
- bm25 13.84 `https://w3id.org/vair#BayesianNetwork` [class, tier 3] Probabilistic model that uses Bayesian inference for probability computations using a directed acyclic graph.
- bm25+lead 13.14 `http://www.w3.org/ns/mls#Model` [class, tier 2] Model is a generalization of a set of training data able to predict values for unseen instances. It is an output from an execution of a data mining algorithm im
- bm25 12.41 `https://w3id.org/dpv/risk#IntegrityConcept` [class, tier 2] Indicates a concept is relevant to 'Integrity' in CIA InfoSec model
- lead 8.28 `http://www.w3.org/ns/sosa/Procedure` [class, tier 1] A workflow, protocol, plan, algorithm, or computational method specifying how to make an Observation, create a Sample, or make a change to the state of the worl
- lead 0.0 `http://www.w3.org/ns/mls#Implementation` [class, tier 2] Implementation is an executable implementation of a machine learning algorithm, a script, or a workflow. It is versioned, and sometimes belongs to a library (e.
- lead 0.0 `https://schema.org/PropertyValueSpecification` [class, tier 2, RO-Crate] A Property value specification.
- lead 0.0 `http://purl.org/linked-data/cube#MeasureProperty` [class, tier 1] The class of components which represent the measured value of the phenomenon being observed

## 6. oht:Uptake (P)

one piece of evidence that someone uses the scheme (regulatory citation, platform adoption, benchmark use)

- bm25 17.12 `http://purl.org/spar/cito/Citation` [class, tier 2] A citation is a conceptual directional link from a citing entity to a cited entity, created by a human performative act of making a citation, typically instanti
- bm25 16.69 `http://purl.obolibrary.org/obo/IAO_0000112` [property, tier 2] A phrase describing how a term should be used and/or a citation to a work which uses it. May also include other kinds of examples that facilitate immediate unde
- bm25 15.98 `https://w3id.org/dpv#RegulatorySandbox` [class, tier 2] Mechanism used by regulators and businesses for gauging the compatibility of regulations and innovative products, particularly in the context of digitalisation,
- bm25 15.66 `http://purl.org/dc/terms/bibliographicCitation` [property, tier 1] A bibliographic reference for the resource.
- bm25 14.79 `https://schema.org/citation` [property, tier 2, RO-Crate] A citation or reference to another creative work, such as another publication, web page, scholarly article, etc.
- bm25 14.41 `https://schema.org/usageInfo` [property, tier 2, RO-Crate] The schema.org [[usageInfo]] property indicates further information about a [[CreativeWork]]. This property is applicable both to works that are freely availabl
- bm25 14.39 `http://www.w3.org/ns/duv#UsageTool` [class, tier 2] A synopsis describing the way a tool can use a dataset or distribution.
- bm25 13.63 `https://schema.org/evidenceLevel` [property, tier 2, RO-Crate] Strength of evidence of the data used to formulate the guideline (enumerated).
- bm25 13.02 `https://schema.org/DigitalPlatformEnumeration` [class, tier 2, RO-Crate] Enumerates some common technology platforms, for use with properties such as [[actionPlatform]]. It is not supposed to be comprehensive - when a suitable code i
- bm25 12.88 `https://schema.org/evidenceOrigin` [property, tier 2, RO-Crate] Source of the data used to formulate the guidance, e.g. RCT, consensus opinion, etc.
- bm25 12.87 `https://schema.org/usesDevice` [property, tier 2, RO-Crate] Device used to perform the test.
- bm25 12.49 `https://schema.org/MedicalEvidenceLevel` [class, tier 2, RO-Crate] Level of evidence for a medical guideline. Enumerated type.
- bm25 12.38 `https://w3id.org/airo#usesTechnique` [property, tier 3] Indicates the AI techniques used in an AI system or component.
- bm25 12.29 `http://www.w3.org/ns/sosa/Platform` [class, tier 1] A Platform is an entity that hosts other entities, particularly Sensors, Actuators, Samplers, and other Platforms.
- bm25 12.25 `https://w3id.org/vair#ApplicationPlatform` [class, tier 3] Resource on which an application runs.
- lead 9.14 `http://www.w3.org/ns/duv#Usage` [class, tier 2] A helpful description of actions that can be performed on a given dataset or distribution.
- lead 8.97 `http://www.w3.org/ns/duv#hasUsage` [property, tier 2] Dataset/distribution usage guidance or instructions.
- lead 5.09 `http://w3id.org/nkos#usedBy` [property, tier 3] Agent using the described KOS.
- lead 0.0 `http://purl.org/dc/terms/isReferencedBy` [property, tier 1, DCAT-AP optional/other] A related resource that references, cites, or otherwise points to the described resource.

## 7. oht:NoMatch (P)

a mapping association asserting that its source concept has no counterpart in the target scheme

- bm25 28.13 `https://w3id.org/sssom/mapping_cardinality_enum#0:1` [individual, tier 2] Indicates that the object has no match in the subject vocabulary. This value MUST only be used when the subject_id is sssom:NoTermFound.
- bm25 28.13 `https://w3id.org/sssom/mapping_cardinality_enum#1:0` [individual, tier 2] Indicates that the subject has no match in the object vocabulary. This value MUST only be used when the object_id is sssom:NoTermFound.
- bm25 24.21 `https://w3id.org/sssom/mapping_cardinality_enum#0:0` [individual, tier 2] Indicates that there is no match between the subject vocabulary and the object vocabulary. This value MUST only be used when both the subject_id and the object_
- bm25 19.57 `http://www.w3.org/2004/02/skos/core#relatedMatch` [property, tier 1] skos:relatedMatch is used to state an associative mapping link between two conceptual resources in different concept schemes.
- bm25 19.57 `http://www.w3.org/2004/02/skos/core#narrowMatch` [property, tier 1] skos:narrowMatch is used to state a hierarchical mapping link between two conceptual resources in different concept schemes.
- bm25 19.57 `http://www.w3.org/2004/02/skos/core#broadMatch` [property, tier 1] skos:broadMatch is used to state a hierarchical mapping link between two conceptual resources in different concept schemes.
- bm25+lead 19.33 `http://rdf-vocabulary.ddialliance.org/xkos#ConceptAssociation` [class, tier 2] 
- bm25+lead 17.64 `https://w3id.org/sssom/NoTermFound` [class, tier 2] sssom:NoTermFound can be used in place of a subject_id or object_id when the corresponding entity could not be found. It SHOULD be used in conjunction with a co
- bm25 17.18 `https://w3id.org/sssom/mapping_cardinality_enum#n:1` [individual, tier 2] Indicates the mapping record is about a many-to-one mapping, that is, several different subjects are mapped to the same object.
- bm25 17.18 `https://w3id.org/sssom/mapping_cardinality_enum#1:n` [individual, tier 2] Indicates the mapping record is about a one-to-many mapping, that is, the same subject is mapped to several different objects.
- bm25 16.87 `https://w3id.org/sssom/mapping_cardinality_enum#1:1` [individual, tier 2] Indicates the mapping record is about a one-to-one mapping, that is, the subject and the object are only mapped to each other, exclusive of any other subject or
- bm25 16.78 `http://www.w3.org/2004/02/skos/core#ConceptScheme` [class, tier 1] A set of concepts, optionally including statements about semantic relationships between those concepts.
- bm25 16.56 `https://w3id.org/sssom/cardinality_scope` [property, tier 2] A list of mapping slots that define the scope for the value found in the mapping_cardinality slot. Mappings are considered to belong to the same scope if they h
- bm25 16.5 `https://w3id.org/sssom/mapping_cardinality` [property, tier 2] A value indicating whether the subject (respectively object) of this mapping record is present in other records involving a different object (respectively subje
- bm25 16.42 `https://w3id.org/sssom/mapping_cardinality_enum#n:n` [individual, tier 2] Indicates the mapping record is about a many-to-many mapping, that is, the subject is mapped to several different objects and the object is mapped to several di

## 8. oht:OpenQuestion (P)

an unresolved editorial point about a record, with a status and later a resolution

- bm25+lead 33.36 `http://www.w3.org/ns/oa#questioning` [individual, tier 1] The motivation for when the user intends to ask a question about the Target.
- bm25 26.16 `http://www.w3.org/ns/oa#Motivation` [class, tier 1] The Motivation class is used to record the user's intent or motivation for the creation of the Annotation, or the inclusion of the body or target, that it is as
- bm25 20.32 `https://schema.org/ReplyAction` [class, tier 2, RO-Crate] The act of responding to a question/message asked/sent by the object. Related to [[AskAction]].\n\nRelated actions:\n\n* [[AskAction]]: Appears generally as an 
- bm25+lead 20.07 `http://www.w3.org/ns/oa#replying` [individual, tier 1] The motivation for when the user intends to reply to a previous statement, either an Annotation or another resource.
- bm25+lead 14.77 `http://www.w3.org/ns/oa#motivatedBy` [property, tier 1] The relationship between an Annotation and a Motivation that describes the reason for the Annotation's creation.
- bm25 14.51 `https://schema.org/AskAction` [class, tier 2, RO-Crate] The act of posing a question / favor to someone.\n\nRelated actions:\n\n* [[ReplyAction]]: Appears generally as a response to AskAction.
- bm25 14.29 `https://w3id.org/dpv/risk#ResolutionControl` [class, tier 2] Control that aims to resolve an event's effects with the goal of fixing or recovering from it
- bm25 13.53 `http://purl.org/ontology/bibo/Issue` [class, tier 2] something that is printed or published and distributed, esp. a given number of a periodical
- bm25 13.32 `https://schema.org/replyToUrl` [property, tier 2, RO-Crate] The URL at which a reply may be posted to the specified UserComment.
- bm25 13.23 `http://www.w3.org/ns/dqv#QualityAnnotation` [class, tier 2] Represents quality annotations, including ratings, quality certificates or feedback that can be associated to datasets or distributions. Quality annotations mus
- bm25 13.21 `http://purl.org/spar/cito/hasReplyFrom` [property, tier 2] A relation according to which the cited entity evokes a reply from the citing entity.
- bm25 13.18 `https://w3id.org/dpv#ContractDisputeResolutionClause` [class, tier 2] A provision detailing the methods and procedures for resolving disagreements or conflicts arising from the contract
- bm25 12.92 `http://www.w3.org/ns/odrl/2/resolution` [individual, tier 1] Resolution of the rendition of the target Asset.
- bm25 12.67 `http://www.w3.org/ns/oa#annotationService` [property, tier 1] The object of the relationship is the end point of a service that conforms to the annotation-protocol, and it may be associated with any resource. The expectati
- bm25 12.64 `https://schema.org/ComicIssue` [class, tier 2, RO-Crate] Individual comic issues are serially published as part of a larger series. For the sake of consistency, even one-shot issues belong to a series comprised of a s
- lead 9.42 `http://www.w3.org/ns/oa#Annotation` [class, tier 1] The class for Web Annotations.
- lead 11.87 `http://www.w3.org/2004/02/skos/core#editorialNote` [property, tier 1] A note for an editor, translator or maintainer of the vocabulary.
- lead 10.1 `https://schema.org/Question` [class, tier 2, RO-Crate] A specific question - e.g. from a user seeking answers online, or collected in a Frequently Asked Questions (FAQ) document.
- lead 6.71 `http://www.w3.org/ns/adms#status` [property, tier 2, DCAT-AP optional/other] The status of the Asset in the context of a particular workflow process.

## 9. oht:HumanReview (P)

a person's review of a record

- bm25 17.39 `https://w3id.org/semapv/vocab/MappingActivity` [class, tier 2] A process that relates to the creation, confirmation, rejection or curation of a mapping.
- bm25 17.35 `https://w3id.org/vair#AssessingRiskOfOffending` [class, tier 3] Assessing the risk of a natural person offending
- bm25 17.35 `https://w3id.org/vair#AssessingHealthRisk` [class, tier 3] Assessing health risk posed by a person
- bm25 17.16 `https://w3id.org/vair#AssessingRiskOfReoffending` [class, tier 3] Assessing the risk of a natural person re-offending
- bm25 16.79 `https://w3id.org/vair#AssessingSecurityRisk` [class, tier 3] Assess security risk posed by a person
- bm25 16.61 `https://w3id.org/dpv#hasRecordOfActivity` [property, tier 2] Indicates a relevant record of activity
- bm25 16.43 `https://w3id.org/vair#AssessingRiskOfIrregularImmigration` [class, tier 3] Assessing risk of irregular immigration posed by a person
- bm25 15.91 `https://schema.org/MediaReviewItem` [class, tier 2, RO-Crate] Represents an item or group of closely related items treated as a unit for the sake of evaluation in a [[MediaReview]]. Authorship etc. apply to the items rathe
- bm25 15.48 `https://w3id.org/vair#AssessingPeopleRelatedRisk` [class, tier 3] Assessing a risk, e.g. a security risk, a risk of irregular migration, or a health risk, posed by a natural person
- bm25 15.45 `https://w3id.org/dpv#ActivityMonitoring` [class, tier 2] Monitoring of activities including assessing whether they have been successfully initiated and completed
- bm25 15.05 `https://w3id.org/vair#AssessingRiskOfBecomingVictimOfCrime` [class, tier 3] Assessing risk of a natural person becoming the victim of criminal offences
- bm25 13.31 `https://w3id.org/semapv/vocab/ManualMappingCuration` [class, tier 2] A matching process that is performed by a human agent and is based on human judgement and domain knowledge.
- bm25 12.99 `https://w3id.org/vair#AssessingPersonalityTraits` [class, tier 3] Assessing personality of natural persons or groups
- bm25 12.8 `https://w3id.org/vair#AssessingLevelOfEducation` [class, tier 3] Assessing the appropriate level of education that an individual will receive
- bm25 12.78 `https://w3id.org/vair#PerformingBackgroundCheck` [class, tier 3] Performing background checks
- lead 6.97 `http://www.w3.org/ns/prov#Activity` [class, tier 1] An activity is something that occurs over a period of time and acts upon or with entities; it may include consuming, processing, transforming, modifying, reloca
- lead 10.76 `http://www.w3.org/ns/oa#assessing` [individual, tier 1] The motivation for when the user intends to provide an assessment about the Target resource.
- lead 0.0 `http://www.w3.org/ns/oa#moderating` [individual, tier 1] The motivation for when the user intends to assign some value or quality to the Target.
- lead 9.75 `https://schema.org/Review` [class, tier 2, RO-Crate] A review of an item - for example, of a restaurant, movie, or store.
- lead 0.0 `http://www.w3.org/ns/dqv#QualityAnnotation` [class, tier 2] Represents quality annotations, including ratings, quality certificates or feedback that can be associated to datasets or distributions. Quality annotations mus

## 10. oht:Session (P)

a drafting session with a language model, as an activity, and the transcript it produced

- bm25+lead 20.17 `http://www.w3.org/ns/prov#SoftwareAgent` [class, tier 1] A software agent is running software.
- bm25 16.61 `https://w3id.org/dpv/ai#LLM` [class, tier 2] Deep learning model that uses artificial neural networks trained on vast amounts of data to understand and generate natural language and other types of content 
- bm25+lead 16.34 `https://schema.org/Conversation` [class, tier 2, RO-Crate] One or more messages between organizations or people on a particular topic. Individual messages can be linked to the conversation with isPartOf or hasPart prope
- bm25 16.11 `http://xmlns.com/foaf/0.1/Agent` [class, tier 2] An agent (eg. person, group, software or physical artifact).
- bm25 15.66 `http://www.w3.org/ns/prov#Agent` [class, tier 1] An agent is something that bears some form of responsibility for an activity taking place, for the existence of an entity, or for another agent's activity.
- bm25 14.98 `https://w3id.org/dpv/ai#ChatbotCapability` [class, tier 2] Capability to simulate human-like conversation with a user through messaging platforms, websites, mobile apps, or telephone systems, often employing natural lan
- bm25 14.82 `https://w3id.org/dpv/ai#AIAgent` [class, tier 2] An AI Agent, also known as an 'intelligent agent', is a software agent that utilises AI technologies
- bm25 14.6 `http://www.w3.org/ns/prov#Association` [class, tier 1] An activity association is an assignment of responsibility to an agent for an activity, indicating that the agent had a role in the activity. It further allows 
- bm25 14.55 `http://purl.obolibrary.org/obo/IAO_0000025` [class, tier 2] A language in which source code is written that is intended to be executed/run by a software interpreter. Programming languages are ways to write instructions t
- bm25 14.49 `http://www.w3.org/ns/mls#hasOutput` [property, tier 2] A relation between a run and either a model or model evaluation that is produced on it’s output.
- bm25+lead 14.41 `https://schema.org/Message` [class, tier 2, RO-Crate] A single message from a sender to one or more organizations or people.
- bm25 14.41 `https://schema.org/EmailMessage` [class, tier 2, RO-Crate] An email message.
- bm25 14.37 `https://schema.org/transcript` [property, tier 2, RO-Crate] If this MediaObject is an AudioObject or VideoObject, the transcript of that object.
- bm25 12.7 `https://w3id.org/dpv#MessageAuthenticationCodes` [class, tier 2] Use of cryptographic methods to authenticate messages
- bm25 12.35 `http://www.w3.org/ns/prov#Attribution` [class, tier 1] Attribution is the ascribing of an entity to an agent. When an entity e is attributed to agent ag, entity e was generated by some unspecified activity that in t
- lead 6.97 `http://www.w3.org/ns/prov#Activity` [class, tier 1] An activity is something that occurs over a period of time and acts upon or with entities; it may include consuming, processing, transforming, modifying, reloca
- lead 4.19 `https://schema.org/CreateAction` [class, tier 2, RO-Crate] The act of deliberately creating/producing/generating/building a result out of the agent.

## 11. oht:family (M)

what kind of scheme this is (harm taxonomy and so on)

- bm25 30.35 `http://www.w3.org/ns/dcat#themeTaxonomy` [property, tier 1, DCAT-AP optional/other] The knowledge organization system (KOS) used to classify catalog's datasets.
- bm25+lead 23.96 `http://w3id.org/nkos/nkostype#taxonomy` [individual, tier 3] scheme of categories and subcategories that can be used to sort and otherwise organize items of knowledge or information
- bm25+lead 19.11 `http://purl.org/dc/terms/type` [property, tier 1, DCAT-AP optional/other] The nature or genre of the resource.
- bm25 18.79 `https://schema.org/contactType` [property, tier 2, RO-Crate] A person or organization can have different contact points, for different purposes. For example, a sales contact point, a PR contact point and so on. This prope
- bm25 17.66 `https://schema.org/genre` [property, tier 2, RO-Crate] Genre of the creative work, broadcast channel or group.
- bm25 13.82 `https://w3id.org/vair#Harm` [class, tier 3] Harmful impacts associated with an AI system. The types of harms include physical, psychological, financial, and economic harms that may be compound with broade
- bm25 13.27 `https://schema.org/mapType` [property, tier 2, RO-Crate] Indicates the kind of Map, from the MapCategoryType Enumeration.
- bm25 13.03 `https://w3id.org/dpv/risk#Harm` [class, tier 2] Concept representing Harm to humans
- bm25 12.61 `https://w3id.org/dpv/risk#PsychologicalHarm` [class, tier 2] Concept representing Psychological Harm
- bm25 12.44 `https://w3id.org/dpv/ai#ExpertSystem` [class, tier 2] AI system that accumulates, combines and encapsulates knowledge provided by a human expert or experts in a specific domain to infer solutions to problems (ISO/I
- bm25 12.41 `https://w3id.org/dpv/risk#PhysicalHarm` [class, tier 2] Concept representing physical harm to an individual or individual(s)
- bm25 12.4 `https://schema.org/albumReleaseType` [property, tier 2, RO-Crate] The kind of release which this album is: single, EP or album.
- bm25 12.25 `http://purl.org/dc/terms/DCMIType` [individual, tier 1] The set of classes specified by the DCMI Type Vocabulary, used to categorize the nature or genre of the resource.
- bm25 12.13 `https://schema.org/learningResourceType` [property, tier 2, RO-Crate] The predominant type or kind characterizing the learning resource. For example, 'presentation', 'handout'.
- bm25 11.93 `https://w3id.org/vair#PsychologicalHarm` [class, tier 3] Represents negative impacts of AI on psychological health
- lead 3.93 `https://schema.org/additionalType` [property, tier 2, RO-Crate] An additional type for the item, typically used for adding more specific types from external vocabularies in microdata syntax. This is a relationship between so

## 12. oht:classifies (D)

the kind of unit a scheme sorts, such as a harm or a content item

- bm25+lead 21.45 `http://rdf-vocabulary.ddialliance.org/discovery#analysisUnit` [property, tier 3] This property links to the analysis unit of a Study, a StudyGroup, or a Variable.
- bm25 20.08 `http://rdf-vocabulary.ddialliance.org/discovery#AnalysisUnit` [class, tier 3] The process collecting data is focusing on the analysis of a particular type of subject. If, for example, the adult population of Finland is being studied, the 
- bm25 17.44 `http://rdf-vocabulary.ddialliance.org/xkos#classifiedUnder` [property, tier 2] 
- bm25+lead 15.37 `http://rdf-vocabulary.ddialliance.org/xkos#covers` [property, tier 2] 
- bm25 14.75 `http://rdf-vocabulary.ddialliance.org/xkos#coversExhaustively` [property, tier 2] 
- bm25 14.43 `http://w3id.org/nkos/nkostype#subject_heading_scheme` [individual, tier 3] structured vocabulary comprising terms available for subject indexing, plus rules for combining them into pre-coordinated strings of terms where necessary
- bm25 14.18 `http://rdf-vocabulary.ddialliance.org/xkos#coversMutuallyExclusively` [property, tier 2] 
- bm25 13.03 `https://w3id.org/dpv/risk#Harm` [class, tier 2] Concept representing Harm to humans
- bm25 12.61 `https://w3id.org/dpv/risk#PsychologicalHarm` [class, tier 2] Concept representing Psychological Harm
- bm25 12.53 `https://schema.org/ComputerLanguage` [class, tier 2, RO-Crate] This type covers computer programming languages such as Scheme and Lisp, as well as other language-like computer representations. Natural languages are best rep
- bm25 12.44 `https://w3id.org/dpv/risk#hasRiskAnalysis` [property, tier 2] Associates the risk analysis
- bm25 12.41 `https://w3id.org/dpv/risk#PhysicalHarm` [class, tier 2] Concept representing physical harm to an individual or individual(s)
- bm25 12.22 `https://w3id.org/vair#SentimentAnalysis` [class, tier 3] Computationally identifying and categorizing opinions expressed in a piece of text, speech or image, to determine a range of feeling such as from positive to ne
- bm25 12.22 `http://www.w3.org/ns/mls#Study` [class, tier 2] Study is a collection of runs that belong together to do some kind of analysis on its results. This analysis can be general or very specific (e.g. a hypothesis 
- bm25 12.08 `https://w3id.org/dpv/ai#SentimentAnalysis` [class, tier 2] Capability for computationally identifying and categorising opinions expressed in a piece of text, speech or image, to determine a range of feeling such as from
- lead 7.59 `http://purl.org/dc/terms/subject` [property, tier 1] A topic of the resource.

## 13. oht:purpose (M)

what the issuer says the scheme is for

- bm25 15.52 `https://schema.org/UseAction` [class, tier 2, RO-Crate] The act of applying an object to its intended purpose.
- bm25 15.27 `https://schema.org/MedicalDevicePurpose` [class, tier 2, RO-Crate] Categories of medical devices, organized by the purpose or intended use of the device.
- bm25 14.78 `http://xmlns.com/foaf/0.1/aimChatID` [property, tier 2] An AIM chat ID
- bm25 13.96 `https://w3id.org/airo#Misuse` [class, tier 3] The use of an AI system or component in a way that is not in accordance with its intended purpose.
- bm25 13.94 `https://w3id.org/vair#InstructionForUse` [class, tier 3] The information provided by the provider to inform the deployer of, in particular, an AI system’s intended purpose and proper use.
- bm25 13.06 `http://www.w3.org/ns/odrl/2/assigner` [property, tier 1] The Party is the issuer of the Rule.
- bm25 12.23 `https://schema.org/educationalUse` [property, tier 2, RO-Crate] The purpose of a work in the context of education; for example, 'assignment', 'group work'.
- bm25 12.22 `https://schema.org/potentialUse` [property, tier 2, RO-Crate] Intended use of the BioChemEntity by humans.
- bm25 11.87 `https://w3id.org/dpv#AINotice` [class, tier 2] A notice providing information regarding the particulars of an AI system such as its intended purpose and proper use
- bm25 11.7 `http://www.w3.org/2004/02/skos/core#inScheme` [property, tier 1] Relates a resource (for example a concept) to a concept scheme in which it is included.
- bm25 11.17 `https://w3id.org/vair#InformationProvision` [class, tier 3] Providing information to inform the user of in particular an AI system’s intended purpose and proper use, inclusive of the specific geographical, behavioural or
- bm25 10.88 `http://rdf-vocabulary.ddialliance.org/discovery#purpose` [property, tier 3] The purpose of a Study of a StudyGroup.
- bm25 10.61 `https://w3id.org/dpv#hasPurpose` [property, tier 2] Indicates association with Purpose
- bm25 10.58 `http://www.w3.org/2004/02/skos/core#topConceptOf` [property, tier 1] Relates a concept to the concept scheme that it is a top level concept of.
- bm25 10.53 `http://www.w3.org/ns/oa#hasPurpose` [property, tier 1] The purpose served by the resource in the Annotation.
- lead 8.5 `http://purl.org/dc/terms/description` [property, tier 1, DCAT-AP mandatory, DCAT-AP optional/other] An account of the resource.
- lead 0.0 `http://purl.org/dc/terms/abstract` [property, tier 1] A summary of the resource.

## 14. oht:legalStatus (D)

legal force of the scheme: statutory, guidance, voluntary, commercial, academic

- bm25+lead 25.22 `http://data.europa.eu/eli/ontology#in_force` [property, tier 2] A value indicating the legal force of a legal resource or a legal expression. A set of values is defined by ELI in the corresponding concept scheme. These value
- bm25 23.28 `https://schema.org/LegalForceStatus` [class, tier 2, RO-Crate] A list of possible statuses for the legal force of a legislation.
- bm25 20.89 `https://schema.org/legislationLegalForce` [property, tier 2, RO-Crate] Whether the legislation is currently in force, not in force, or partially in force.
- bm25 18.42 `http://purl.org/ontology/bibo/status` [property, tier 2] The publication status of (typically academic) content.
- bm25 16.46 `http://data.europa.eu/eli/ontology#InForce` [class, tier 2] Formally defined as the set of skos:Concept in concept scheme eli:InForceTable
- bm25 16.28 `http://data.europa.eu/eli/ontology#InForce-inForce` [individual, tier 2] Indicates that a legal resource is in force.
- bm25 16.07 `http://data.europa.eu/eli/ontology#InForce-notInForce` [individual, tier 2] Indicates that a legal resource is currently not in force.
- bm25 15.99 `https://schema.org/legalStatus` [property, tier 2, RO-Crate] The drug or supplement's legal status, including any controlled substance schedules that apply.
- bm25 15.89 `http://data.europa.eu/eli/ontology#first_date_entry_in_force` [property, tier 2] The first date any part of the legal resource or legal expression came into force (can be seen as the start date of a dc:valid range for this resource)
- bm25 15.13 `http://data.europa.eu/eli/ontology#InForce-partiallyInForce` [individual, tier 2] Indicates that parts of the legal resource are in force, and parts are not.
- bm25 15.08 `https://w3id.org/dpv#LegalAgreement` [class, tier 2] A legally binding agreement
- bm25 14.84 `https://w3id.org/dpv#LegalCompliance` [class, tier 2] Purposes associated with carrying out data processing to fulfill a legal or statutory obligation
- bm25 14.73 `http://data.europa.eu/eli/ontology#commences` [property, tier 2] Indicates that this legal resource sets another legal resource into force. Note the the date of entry into force of the other resource should be modified accord
- bm25 14.3 `http://data.europa.eu/eli/ontology#InForceTable` [individual, tier 2] A set of values for the legal force of a resource. ELI includes a set of values for this table.
- bm25 14.27 `http://data.europa.eu/eli/ontology#commenced_by` [property, tier 2] Inverse of "commences". Indicates that this legal resource was set in force by another legal resource. Situations where a resource enters into force because of 
- lead 6.71 `http://www.w3.org/ns/adms#status` [property, tier 2, DCAT-AP optional/other] The status of the Asset in the context of a particular workflow process.

## 15. oht:statusDate (M)

when the current adms:status began

- bm25 26.24 `https://schema.org/dateModified` [property, tier 2, RO-Crate] The date on which the CreativeWork was most recently modified or when the item's entry was modified within a DataFeed.
- bm25 24.21 `https://schema.org/validFrom` [property, tier 2, RO-Crate] The date when the item becomes valid.
- bm25+lead 22.95 `http://purl.org/dc/terms/modified` [property, tier 1, DCAT-AP mandatory, DCAT-AP optional/other] Date on which the resource was changed.
- bm25 22.65 `https://schema.org/validUntil` [property, tier 2, RO-Crate] The date when the item is no longer valid.
- bm25+lead 20.41 `http://purl.org/dc/terms/valid` [property, tier 1] Date (often a range) of validity of a resource.
- bm25 20.19 `https://schema.org/validThrough` [property, tier 2, RO-Crate] The date after when the item is not valid. For example the end of an offer, salary period, or a period of opening hours.
- bm25 19.96 `https://schema.org/modifiedTime` [property, tier 2, RO-Crate] The date and time the reservation was modified.
- bm25 16.2 `https://schema.org/priceValidUntil` [property, tier 2, RO-Crate] The date after which the price is no longer available.
- bm25 15.82 `http://data.europa.eu/eli/ontology#version_date` [property, tier 2] The point-in-time at which the provided description of the legislation is valid.
- bm25 15.69 `https://schema.org/purchaseDate` [property, tier 2, RO-Crate] The date the item, e.g. vehicle, was purchased by the current owner.
- bm25 15.59 `https://schema.org/legislationDateVersion` [property, tier 2, RO-Crate] The point-in-time at which the provided description of the legislation is valid (e.g.: when looking at the law on the 2016-04-07 (= dateVersion), I get the cons
- bm25 15.55 `https://schema.org/reservationStatus` [property, tier 2, RO-Crate] The current status of the reservation.
- bm25 15.55 `https://schema.org/orderStatus` [property, tier 2, RO-Crate] The current status of the order.
- bm25 15.01 `https://schema.org/actionStatus` [property, tier 2, RO-Crate] Indicates the current disposition of the Action.
- bm25 14.91 `https://w3id.org/dpv#ConsentStatusValidForProcessing` [class, tier 2] States of consent that can be used as valid justifications for processing data
- lead 7.35 `http://purl.org/dc/terms/date` [property, tier 1] A point or period of time associated with an event in the lifecycle of the resource.

## 16. oht:sunsetDate (M)

the announced date after which a scheme or service ceases

- bm25+lead 34.6 `https://schema.org/expires` [property, tier 2, RO-Crate] Date the content expires and is no longer useful or available. For example a [[VideoObject]] or [[NewsArticle]] whose availability or relevance is time-limited,
- bm25 28.4 `https://schema.org/availableThrough` [property, tier 2, RO-Crate] After this date, the item will no longer be available for pickup.
- bm25+lead 23.97 `http://data.europa.eu/eli/ontology#date_no_longer_in_force` [property, tier 2] The last date any part of the legislation is in force, if the date is known (can be seen as the end date of a dc:valid range for this resource).
- bm25 23.6 `https://schema.org/priceValidUntil` [property, tier 2, RO-Crate] The date after which the price is no longer available.
- bm25 19.39 `http://www.w3.org/ns/dcat#endDate` [property, tier 1, DCAT-AP optional/other] The end of the period.
- bm25+lead 18.12 `https://schema.org/endDate` [property, tier 2, RO-Crate] The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
- bm25 18.03 `http://purl.org/dc/terms/available` [property, tier 1] Date that the resource became or will become available.
- bm25 17.73 `https://schema.org/availableService` [property, tier 2, RO-Crate] A medical service available from this provider.
- bm25 17.38 `http://www.w3.org/ns/oa#sourceDateEnd` [property, tier 1] The end timestamp of the interval over which the Source resource should be interpreted as being applicable to the Annotation.
- bm25 16.93 `http://rdf-vocabulary.ddialliance.org/discovery#endDate` [property, tier 3] Defines the end date of a period of time. Please note that this property is a feature at risk, since the domain is not a class of Disco. Maintainers of the doma
- bm25 16.36 `http://www.w3.org/ns/dcat#endpointDescription` [property, tier 1, DCAT-AP optional/other] A description of the service end-point, including its operations, parameters etc.
- bm25 16.14 `http://www.w3.org/ns/dcat#endpointURL` [property, tier 1, DCAT-AP mandatory] The root location or primary endpoint of the service (a web-resolvable IRI).
- bm25 15.64 `http://www.w3.org/2006/time#after` [property, tier 1] Gives directionality to time. If a temporal entity T1 is after another temporal entity T2, then the beginning of T1 is after the end of T2.
- bm25 15.53 `https://schema.org/validThrough` [property, tier 2, RO-Crate] The date after when the item is not valid. For example the end of an offer, salary period, or a period of opening hours.
- bm25 15.37 `http://www.w3.org/ns/prov#End` [class, tier 1] End is when an activity is deemed to have been ended by an entity, known as trigger. The activity no longer exists after its end. Any usage, generation, or inva
- lead 7.28 `http://purl.org/dc/terms/valid` [property, tier 1] Date (often a range) of validity of a resource.

## 17. oht:severityEncoding (D)

where severity lives in a scheme: nowhere, in the hierarchy, on an axis, both

- bm25 14.19 `https://schema.org/Residence` [class, tier 2, RO-Crate] The place where a person lives.
- bm25 13.54 `https://schema.org/encodingType` [property, tier 2, RO-Crate] The supported encoding type(s) for an EntryPoint request.
- bm25 13.14 `https://schema.org/encoding` [property, tier 2, RO-Crate] A media object that encodes this CreativeWork. This property is a synonym for associatedMedia.
- bm25 12.9 `http://purl.org/linked-data/cube#hierarchyRoot` [property, tier 1] Specifies a root of the hierarchy. A hierarchy may have multiple roots but must have at least one.
- bm25 11.8 `https://w3id.org/dpv/risk#ModerateSeverity` [class, tier 2] Level where Severity is Moderate
- bm25 11.8 `https://w3id.org/dpv/risk#LowSeverity` [class, tier 2] Level where Severity is Low
- bm25 11.8 `https://w3id.org/dpv/risk#HighSeverity` [class, tier 2] Level where Severity is High
- bm25 11.72 `http://www.w3.org/ns/org#classification` [property, tier 1] Indicates a classification for this Organization within some classification scheme. Extension vocabularies may wish to specialize this property to have a range 
- bm25 11.7 `http://www.w3.org/2004/02/skos/core#inScheme` [property, tier 1] Relates a resource (for example a concept) to a concept scheme in which it is included.
- bm25 11.56 `http://purl.org/dc/terms/Period` [class, tier 1] The set of time intervals defined by their limits according to the DCMI Period Encoding Scheme.
- bm25 11.31 `http://purl.org/dc/terms/Point` [class, tier 1] The set of points in space defined by their geographic coordinates according to the DCMI Point Encoding Scheme.
- bm25 11.31 `http://purl.org/dc/terms/Box` [class, tier 1] The set of regions in space defined by their geographic coordinates according to the DCMI Box Encoding Scheme.
- bm25 11.27 `https://schema.org/encodingFormat` [property, tier 2, RO-Crate] Media type typically expressed using a MIME format (see [IANA site](http://www.iana.org/assignments/media-types/media-types.xhtml) and [MDN reference](https://d
- bm25 11.07 `https://w3id.org/dpv/risk#VeryLowSeverity` [class, tier 2] Level where Severity is Very Low
- bm25 11.07 `https://w3id.org/dpv/risk#VeryHighSeverity` [class, tier 2] Level where Severity is Very High
- lead 0.0 `http://www.w3.org/2004/02/skos/core#note` [property, tier 1] A general note, for any purpose.

## 18. oht:hasConcept (P)

links a concept scheme to each concept in it (inverse of skos:inScheme)

- bm25 24.25 `http://data.europa.eu/eli/ontology#WorkType` [class, tier 2] 
- bm25+lead 23.65 `https://schema.org/hasDefinedTerm` [property, tier 2, RO-Crate] A Defined Term contained in this term set.
- bm25 21.33 `http://purl.org/skos-history/isVersionHistoryOf` [property, tier 3] Links the version history set to the skos concept scheme it is about. (Preliminary, may be better located in dsv ontology.)
- bm25 21.0 `http://www.w3.org/ns/org#hasMember` [property, tier 1] Indicates a person who is a member of the subject Organization. Inverse of `org:memberOf`, see that property for further clarification. Provided for compatibili
- bm25 20.91 `http://data.europa.eu/eli/ontology#version` [property, tier 2] A skos concept scheme, could be locally defined? Group proposal is to start with an initial ELI scheme, that might include concepts of "Official Journal" "made"
- bm25 20.69 `http://data.europa.eu/eli/ontology#Version` [class, tier 2] Formally defined as the set of skos:Concept in concept scheme eli:VersionTable
- bm25 20.69 `http://data.europa.eu/eli/ontology#InForce` [class, tier 2] Formally defined as the set of skos:Concept in concept scheme eli:InForceTable
- bm25 19.54 `http://www.w3.org/ns/org#member` [property, tier 1] Indicates the Person (or other Agent including Organization) involved in the Membership relationship. Inverse of `org:hasMembership`
- bm25 19.01 `http://data.europa.eu/eli/ontology#Language` [class, tier 2] Formally defined as the set of skos:Concept in concept scheme http://publications.europa.eu/resource/authority/language
- bm25+lead 18.92 `http://www.w3.org/2004/02/skos/core#hasTopConcept` [property, tier 1] Relates, by convention, a concept scheme to a concept which is topmost in the broader/narrower concept hierarchies for that scheme, providing an entry point to 
- bm25 18.77 `http://purl.org/skos-history/SchemeDelta` [class, tier 3] The delta of two versions of a SKOS concept scheme.
- bm25 18.63 `http://data.europa.eu/eli/ontology#SubdivisionType` [class, tier 2] Formally defined as the set of skos:Concept in concept scheme eli:SubdivisionTypeTable
- bm25 18.63 `http://data.europa.eu/eli/ontology#ResourceType` [class, tier 2] Formally defined as the set of skos:Concept in concept scheme eli:ResourceTypeTable
- bm25 18.63 `http://data.europa.eu/eli/ontology#LegalValue` [class, tier 2] Formally defined as the set of skos:Concept in concept scheme eli:LegalValueTable
- bm25 18.63 `http://data.europa.eu/eli/ontology#FormatType` [class, tier 2] Formally defined as the set of skos:Concept in concept scheme eli:MediaTypeTable.
- lead 14.59 `http://www.w3.org/2004/02/skos/core#inScheme` [property, tier 1] Relates a resource (for example a concept) to a concept scheme in which it is included.
- lead 4.4 `http://purl.org/dc/terms/hasPart` [property, tier 1, DCAT-AP optional/other] A related resource that is included either physically or logically in the described resource.
- lead 13.29 `http://www.w3.org/2004/02/skos/core#member` [property, tier 1] Relates a collection to one of its members.

## 19. oht:primarySource (P)

the authoritative text that defines the scheme

- bm25+lead 29.61 `http://purl.org/spar/cito/citesAsAuthority` [property, tier 2] A relation according to which the citing entity cites the cited entity as one that provides an authoritative description or definition of the subject under disc
- bm25 20.89 `http://purl.org/spar/cito/citesAsDataSource` [property, tier 2] A relation according to which the citing entity cites the cited entity as source of data.
- bm25 19.26 `http://purl.org/spar/cito/citesAsSourceDocument` [property, tier 2] A relation according to which the citing entity cites the cited entity as being the entity from which the citing entity is derived, or about which the citing en
- bm25 19.25 `http://www.w3.org/ns/prov#qualifiedPrimarySource` [property, tier 1] If this Entity prov:hadPrimarySource Entity :e, then it can qualify how using prov:qualifiedPrimarySource [ a prov:PrimarySource; prov:entity :e; :foo :bar ].
- bm25 17.45 `http://purl.org/spar/cito/citesForInformation` [property, tier 2] A relation according to which the citing entity cites the cited entity as a source of information on the subject under discussion.
- bm25 17.45 `http://purl.org/spar/cito/citesAsEvidence` [property, tier 2] A relation according to which the citing entity cites the cited entity as source of factual evidence for statements it contains.
- bm25 16.91 `http://data.europa.eu/eli/ontology#cites` [property, tier 2] Citation in the text of the legislation. This may be at the legal resource or legal expression level, as required by the implementation context. This includes v
- bm25 16.87 `http://purl.org/spar/cito/isCitedAsAuthorityBy` [property, tier 2] A relation according to which the cited entity is cited as providing an authoritative description or definition of the subject under discussion in the citing en
- bm25 16.77 `http://www.w3.org/ns/prov#wasPrimarySourceOf` [untyped, tier 1] 
- bm25 16.67 `https://w3id.org/dpv#ConsultationWithAuthority` [class, tier 2] Consultation with an authority or authoritative entity
- bm25+lead 16.25 `http://www.w3.org/ns/prov#hadPrimarySource` [property, tier 1] [definition of prov:PrimarySource] A primary source for a topic refers to something produced by some agent with direct experience and knowledge about the topic,
- bm25 13.45 `http://data.europa.eu/eli/ontology#LegalValue-authoritative` [individual, tier 2] The publisher gives some special status to the publication of the document. ("The Queens Printer" version of a UK Act of Parliament). This status is specific to
- bm25 13.38 `http://www.w3.org/ns/prov#PrimarySource` [class, tier 1] A primary source for a topic refers to something produced by some agent with direct experience and knowledge about the topic, at the time of the topic's study, 
- bm25 13.33 `http://purl.org/spar/cito/citesAsRelated` [property, tier 2] A relation according to which the citing entity cites the cited entity as one that is related.
- bm25 12.74 `http://purl.org/spar/cito/citesAsRecommendedReading` [property, tier 2] A relation according to which the citing entity cites the cited entity as an item of recommended reading.
- lead 7.15 `http://purl.org/dc/terms/source` [property, tier 1, DCAT-AP optional/other] A related resource from which the described resource is derived.

## 20. oht:sourceType (M)

primary, secondary or tertiary source, relative to the citing scheme

- bm25+lead 22.92 `http://www.w3.org/ns/prov#hadPrimarySource` [property, tier 1] [definition of prov:PrimarySource] A primary source for a topic refers to something produced by some agent with direct experience and knowledge about the topic,
- bm25 19.25 `http://www.w3.org/ns/prov#qualifiedPrimarySource` [property, tier 1] If this Entity prov:hadPrimarySource Entity :e, then it can qualify how using prov:qualifiedPrimarySource [ a prov:PrimarySource; prov:entity :e; :foo :bar ].
- bm25 19.22 `http://www.w3.org/ns/prov#PrimarySource` [class, tier 1] A primary source for a topic refers to something produced by some agent with direct experience and knowledge about the topic, at the time of the topic's study, 
- bm25 16.77 `http://www.w3.org/ns/prov#wasPrimarySourceOf` [untyped, tier 1] 
- bm25 15.55 `http://data.europa.eu/eli/ontology#basis_for` [property, tier 2] Indicates that this work or expression empowers another . Typically primary legislation is the basis for secondary legislation.
- bm25 14.52 `http://purl.org/spar/cito/citesAsSourceDocument` [property, tier 2] A relation according to which the citing entity cites the cited entity as being the entity from which the citing entity is derived, or about which the citing en
- bm25 13.81 `https://schema.org/digitalSourceType` [property, tier 2] Indicates an IPTCDigitalSourceEnumeration code indicating the nature of the digital source(s) for some [[CreativeWork]].
- bm25 13.69 `http://purl.org/spar/cito/isCitedAsSourceDocumentBy` [property, tier 2] A relation according to which the cited entity is cited as being the entity from which the citing entity is derived, or about which the citing entity contains m
- bm25 13.06 `http://purl.org/spar/cito/isCitedAsDataSourceBy` [property, tier 2] A relation according to which the cited entity is cited as a data source by the citing entity.
- bm25 13.06 `http://purl.org/spar/cito/citesAsDataSource` [property, tier 2] A relation according to which the citing entity cites the cited entity as source of data.
- bm25 12.96 `https://schema.org/secondaryPrevention` [property, tier 2, RO-Crate] A preventative therapy used to prevent reoccurrence of the medical condition after an initial episode of the condition.
- bm25 12.23 `http://xmlns.com/foaf/0.1/isPrimaryTopicOf` [property, tier 2] A document that this thing is the primary topic of.
- bm25 12.13 `http://xmlns.com/foaf/0.1/primaryTopic` [property, tier 2, DCAT-AP mandatory] The primary topic of some page or document.
- bm25 11.92 `https://schema.org/legislationPassedBy` [property, tier 2, RO-Crate] The person or organization that originally passed or made the law: typically parliament (for primary legislation) or government (for secondary legislation). Thi
- bm25 11.86 `https://w3id.org/dpv#SecondaryImportance` [class, tier 2] Indication of 'secondary' or 'minor' or 'auxiliary' importance
- lead 0.0 `http://www.w3.org/ns/prov#wasDerivedFrom` [property, tier 1, RO-Crate] A derivation is a transformation of an entity into another, an update of an entity resulting in a new one, or the construction of a new entity based on a pre-ex

## 21. oht:hasChange (M)

a version lists a change

- bm25 15.61 `https://w3id.org/airo#hasVersion` [property, tier 3] Indicates the version of an entity.
- bm25 15.38 `https://w3id.org/airo#hasPreDeterminedChange` [property, tier 3] Indicates the changes that are planned to be applied to the system, components, or context of use.
- bm25 15.08 `http://purl.org/dc/terms/hasVersion` [property, tier 1, DCAT-AP optional/other] A related resource that is a version, edition, or adaptation of the described resource.
- bm25 14.92 `http://www.w3.org/ns/dcat#hasVersion` [property, tier 1] This resource has a more specific, versioned resource [PAV].
- bm25 14.17 `http://www.w3.org/ns/dcat#hasCurrentVersion` [property, tier 1] This resource has a more specific, versioned resource with equivalent content [PAV].
- bm25 14.04 `http://rdf-vocabulary.ddialliance.org/xkos#hasPart` [property, tier 2] 
- bm25 14.03 `http://data.europa.eu/eli/ontology#has_part` [property, tier 2] inverse of "is_part_of"
- bm25 13.46 `http://www.w3.org/ns/mls#hasPart` [property, tier 2] A relation which represents a part-whole relationship holding between an entity and its part.
- bm25 13.11 `https://schema.org/hasPart` [property, tier 2, RO-Crate] Indicates an item or CreativeWork that is part of this item, or CreativeWork (in some sense).
- bm25 13.1 `https://w3id.org/airo#hasFrequency` [property, tier 3] Indicates frequency of an event, e.g. change.
- bm25+lead 12.99 `http://purl.org/dc/terms/hasPart` [property, tier 1, DCAT-AP optional/other] A related resource that is included either physically or logically in the described resource.
- bm25 12.79 `http://purl.org/skos-history/hasDelta` [property, tier 3] A delta for this version. The subject of the triple may be a dsv:VersionHistoryRecord.
- bm25 12.78 `http://purl.org/pav/hasEarlierVersion` [property, tier 2] This versioned resource has an earlier version. Any earlier version of this resource can be indicated with pav:hasEarlierVersion, e.g.: <http://example.com/v4> 
- bm25 12.2 `http://data.europa.eu/eli/ontology#changes` [property, tier 2] Indicates that this work or expression legally changes another. This encompasses the notions of amendment, replacement, repeal, or other types of change. This m
- bm25 12.14 `https://schema.org/hasBioChemEntityPart` [property, tier 2, RO-Crate] Indicates a BioChemEntity that (in some sense) has this BioChemEntity as a part.

## 22. oht:changeType (M)

added, removed, renamed, redefined, moved, merged, split, reclassified

- bm25 15.51 `http://www.w3.org/ns/prov#removedKey` [property, tier 1] The key removed in a Removal.
- bm25 13.53 `http://purl.obolibrary.org/obo/IAO_0000227` [individual, tier 2] The term has been combined with one or more other terms to create a more encompassing (merged) term.
- bm25 13.32 `https://schema.org/EventMovedOnline` [individual, tier 2, RO-Crate] Indicates that the event was changed to allow online participation. See [[eventAttendanceMode]] for specifics of whether it is now fully or partially online.
- bm25 13.27 `https://schema.org/mapType` [property, tier 2, RO-Crate] Indicates the kind of Map, from the MapCategoryType Enumeration.
- bm25 12.62 `https://schema.org/valueAddedTaxIncluded` [property, tier 2, RO-Crate] Specifies whether the applicable value-added tax (VAT) is included in the price specification or not.
- bm25 12.4 `https://schema.org/albumReleaseType` [property, tier 2, RO-Crate] The kind of release which this album is: single, EP or album.
- bm25 12.13 `https://schema.org/learningResourceType` [property, tier 2, RO-Crate] The predominant type or kind characterizing the learning resource. For example, 'presentation', 'handout'.
- bm25 12.01 `http://purl.obolibrary.org/obo/IAO_0000229` [individual, tier 2] The term has been split into two or more new terms.
- bm25 11.82 `http://purl.obolibrary.org/obo/IAO_0000002` [individual, tier 2] 
- bm25 11.67 `http://www.w3.org/2004/02/skos/core#changeNote` [property, tier 1] A note about a modification to a concept.
- bm25 11.26 `http://purl.obolibrary.org/obo/IAO_0006011` [property, tier 2] A annotation relationship between two terms in an ontology that may refer to the same (natural) type but where more evidence is required before terms are merged
- bm25 10.94 `http://purl.org/iso25964/skos-thes#plusUF` [property, tier 3] Definition: ISO 25964-1: UF+ The non preferred term labeling a complex concept. The complex concept will be identified by splitting the non preferred term into 
- bm25 10.55 `http://rdf-vocabulary.ddialliance.org/discovery#kindOfData` [property, tier 3] The general kind of data (e.g. geospatial, register, survey) collected in this study, given either as a skos:Concept, or as a blank node with attached free-text
- bm25 10.46 `https://w3id.org/airo#hasPreDeterminedChange` [property, tier 3] Indicates the changes that are planned to be applied to the system, components, or context of use.
- bm25 10.33 `https://schema.org/contactType` [property, tier 2, RO-Crate] A person or organization can have different contact points, for different purposes. For example, a sales contact point, a PR contact point and so on. This prope
- lead 5.5 `http://purl.org/dc/terms/type` [property, tier 1, DCAT-AP optional/other] The nature or genre of the resource.

## 23. oht:affectsConcept (P)

the concept a change touched

- bm25 20.83 `http://www.w3.org/ns/org#changedBy` [property, tier 1] Indicates a change event which resulted in a change to this organization. Depending on the event the organization may or may not have continued to exist after t
- bm25 19.75 `http://data.europa.eu/eli/ontology#changed_by` [property, tier 2] Inverse of « changes ». Indicates that this work or expression is being legally changed by another. This encompasses the notions of amendment, replacement, repe
- bm25 18.03 `http://rdf-vocabulary.ddialliance.org/xkos#targetConcept` [property, tier 2] 
- bm25 16.16 `http://www.w3.org/ns/odrl/2/target` [property, tier 1] The target property indicates the Asset that is the primary subject to which the Rule action directly applies.
- bm25 16.06 `http://www.w3.org/2004/02/skos/core#changeNote` [property, tier 1] A note about a modification to a concept.
- bm25 14.07 `https://w3id.org/airo#hasChangedEntity` [property, tier 3] Indicates the entity that is being changed.
- bm25 12.19 `http://purl.org/skos-history/concepthistory` [property, tier 3] Collects the concept deltas of a concept (given in the subject of the triple).
- bm25 11.94 `http://www.w3.org/ns/org#originalOrganization` [property, tier 1] Indicates one or more organizations that existed before the change event. Depending on the event they may or may not have continued to exist after the event. In
- bm25 11.82 `http://www.w3.org/ns/oa#editing` [individual, tier 1] The motivation for when the user intends to request a change or edit to the Target resource.
- bm25 11.73 `https://schema.org/object` [property, tier 2, RO-Crate] The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which c
- bm25 11.18 `https://schema.org/target` [property, tier 2, RO-Crate] Indicates a target EntryPoint, or url, for an Action.
- bm25+lead 11.0 `http://www.w3.org/ns/oa#hasTarget` [property, tier 1] The relationship between an Annotation and its Target.
- bm25 10.83 `https://schema.org/targetCollection` [property, tier 2, RO-Crate] A sub property of object. The collection target of the action.
- bm25 10.51 `https://schema.org/targetUrl` [property, tier 2, RO-Crate] The URL of a node in an established educational framework.
- bm25 10.51 `https://schema.org/targetName` [property, tier 2, RO-Crate] The name of a node in an established educational framework.
- lead 7.59 `http://purl.org/dc/terms/subject` [property, tier 1] A topic of the resource.
- lead 0.0 `http://www.w3.org/ns/prov#used` [property, tier 1] A prov:Entity that was used by this prov:Activity. For example, :baking prov:used :spoon, :egg, :oven .

## 24. oht:officialMapping (P)

the issuer's own crosswalk from the previous version

- bm25 22.39 `http://www.w3.org/ns/dcat#previousVersion` [property, tier 1] The previous version of a resource in a lineage [PAV].
- bm25 19.34 `https://w3id.org/sssom/mapping_tool_version` [property, tier 2] Version string that denotes the version of the mapping tool used.
- bm25 19.23 `owl:versionInfo` [property, tier 2] A version string for the mapping.
- bm25 17.39 `http://www.w3.org/ns/adms#versionNotes` [property, tier 2, DCAT-AP optional/other] A description of changes between this version and the previous version of the Asset.
- bm25 17.07 `http://purl.org/pav/version` [property, tier 2] The version number of a resource. This is a freetext string, typical values are "1.5" or "21". The URI identifying the previous version can be provided using pr
- bm25 16.49 `http://purl.org/pav/hasEarlierVersion` [property, tier 2] This versioned resource has an earlier version. Any earlier version of this resource can be indicated with pav:hasEarlierVersion, e.g.: <http://example.com/v4> 
- bm25 16.39 `http://purl.org/pav/previousVersion` [property, tier 2] The previous version of a resource in a lineage. For instance a news article updated to correct factual information would point to the previous version of the a
- bm25 15.89 `https://w3id.org/sssom/sssom_version` [property, tier 2] The version of the SSSOM specification a mapping set is compliant with.
- bm25 15.79 `http://www.w3.org/ns/adms#prev` [property, tier 2] A link to the previous version of the Asset.
- bm25+lead 15.14 `http://rdf-vocabulary.ddialliance.org/xkos#Correspondence` [class, tier 2] 
- bm25 13.06 `http://www.w3.org/ns/odrl/2/assigner` [property, tier 1] The Party is the issuer of the Rule.
- bm25 12.75 `http://rdf-vocabulary.ddialliance.org/xkos#previous` [property, tier 2] immediate predecessor in the sequence
- bm25 12.14 `http://www.w3.org/ns/dcat#prev` [property, tier 1] The previous resource (before the current one) in an ordered collection or series of resources.
- bm25 12.02 `https://schema.org/previousItem` [property, tier 2, RO-Crate] A link to the ListItem that precedes the current one.
- bm25 11.39 `http://purl.org/pav/hasVersion` [property, tier 2] This resource has a more specific, versioned resource. This property is intended for relating a non-versioned or abstract resource to several versioned resource
- lead 0.0 `http://purl.org/dc/terms/relation` [property, tier 1, DCAT-AP mandatory, DCAT-AP optional/other] A related resource.

## 25. oht:introducedIn (P)

the version in which a concept first appeared

- bm25 14.24 `http://purl.org/skos-history/ConceptVersion` [class, tier 3] (???) A version of a SKOS concept.
- bm25 12.79 `http://data.europa.eu/eli/ontology#Version` [class, tier 2] Formally defined as the set of skos:Concept in concept scheme eli:VersionTable
- bm25 12.75 `http://purl.org/skos-history/isVersionHistoryOf` [property, tier 3] Links the version history set to the skos concept scheme it is about. (Preliminary, may be better located in dsv ontology.)
- bm25 11.86 `http://data.europa.eu/eli/ontology#version` [property, tier 2] A skos concept scheme, could be locally defined? Group proposal is to start with an initial ELI scheme, that might include concepts of "Official Journal" "made"
- bm25 11.75 `http://xmlns.com/foaf/0.1/firstName` [property, tier 2] The first name of a person.
- bm25 11.56 `http://www.w3.org/ns/dcat#first` [property, tier 1] The first resource in an ordered collection or series of resources, to which the current resource belongs.
- bm25 11.47 `https://schema.org/firstPerformance` [property, tier 2, RO-Crate] The date and place the work was first performed.
- bm25 11.3 `https://schema.org/firstAppearance` [property, tier 2, RO-Crate] Indicates the first known occurrence of a [[Claim]] in some [[CreativeWork]].
- bm25 10.71 `https://schema.org/dateVehicleFirstRegistered` [property, tier 2, RO-Crate] The date of the first registration of the vehicle with the respective public authorities.
- bm25 10.54 `http://purl.org/dc/terms/created` [property, tier 1] Date of creation of the resource.
- bm25 10.39 `http://usefulinc.com/ns/doap#created` [property, tier 2] Date when something was created, in YYYY-MM-DD form. e.g. 2004-04-05
- bm25 10.36 `http://purl.obolibrary.org/obo/IAO_0000426` [property, tier 2] 
- bm25 10.32 `https://schema.org/printSection` [property, tier 2, RO-Crate] If this NewsArticle appears in print, this field indicates the print section in which the article appeared.
- bm25 10.23 `http://www.w3.org/ns/dcat#version` [property, tier 1, DCAT-AP optional/other] The version indicator (name or identifier) of a resource.
- bm25 10.23 `https://schema.org/dateCreated` [property, tier 2, RO-Crate] The date on which the CreativeWork was created or the item was added to a DataFeed.
- lead 5.23 `http://www.w3.org/ns/prov#generatedAtTime` [property, tier 1] The time at which an entity was completely created and is available for use.
- lead 0.0 `http://purl.org/dc/terms/issued` [property, tier 1, DCAT-AP optional/other] Date of formal issuance of the resource.
- lead 8.33 `http://purl.org/pav/createdAt` [property, tier 2] The geo-location of the agents when creating the resource (pav:createdBy). For instance a photographer takes a picture of the Eiffel Tower while standing in fro

## 26. oht:retiredIn (P)

the version in which a concept was removed; the IRI remains

- bm25 20.41 `http://www.w3.org/2002/07/owl#versionIRI` [individual, tier 1] The property that identifies the version IRI of an ontology.
- bm25 19.59 `http://purl.obolibrary.org/obo/IAO_0100001` [property, tier 2] Use on obsolete terms, relating the term to another term that can be used as a substitute
- bm25 17.63 `https://w3id.org/sssom/object_source_version` [property, tier 2] Version IRI or version string of the source of the object term.
- bm25 17.63 `https://w3id.org/sssom/subject_source_version` [property, tier 2] Version IRI or version string of the source of the subject term.
- bm25 15.51 `http://www.w3.org/ns/prov#removedKey` [property, tier 1] The key removed in a Removal.
- bm25 14.24 `http://purl.org/skos-history/ConceptVersion` [class, tier 3] (???) A version of a SKOS concept.
- bm25 14.16 `https://schema.org/dateDeleted` [property, tier 2, RO-Crate] The datetime the item was removed from the DataFeed.
- bm25+lead 14.14 `http://purl.org/dc/terms/isReplacedBy` [property, tier 1] A related resource that supplants, displaces, or supersedes the described resource.
- bm25 14.13 `https://w3id.org/dpv/ai#RetirementStage` [class, tier 2] The stage in the lifecycle where the AI system is retired and becomes obsolete
- bm25 13.58 `http://purl.obolibrary.org/obo/IAO_0000604` [property, tier 2] relates a class of CRID to the date after which further instances should not be made, according to the central authority
- bm25 13.57 `http://www.w3.org/ns/prov#wasRevisionOf` [property, tier 1] A revision is a derivation that revises an entity into a revised version.
- bm25+lead 13.51 `http://www.w3.org/2002/07/owl#deprecated` [property, tier 1] The annotation property that indicates that a given entity has been deprecated.
- bm25 13.34 `http://purl.obolibrary.org/obo/IAO_0000226` [individual, tier 2] The term was created to temporarily stand in for a semantic purpose, but is no longer needed, typically due to another permanent term being defined.
- bm25 12.79 `http://data.europa.eu/eli/ontology#Version` [class, tier 2] Formally defined as the set of skos:Concept in concept scheme eli:VersionTable
- bm25 12.78 `https://schema.org/IncentiveStatusRetired` [individual, tier 2] This incentive is not longer available.
- lead 4.12 `http://www.w3.org/ns/prov#invalidatedAtTime` [property, tier 1] The time at which an entity was invalidated (i.e., no longer usable).
- lead 0.0 `https://schema.org/supersededBy` [property, tier 2, RO-Crate] Relates a term (i.e. a property, class or enumeration) to one that supersedes it.

## 27. oht:hasAxis (M)

a scheme declares an axis

- bm25 22.58 `http://purl.org/linked-data/cube#dimension` [property, tier 1] An alternative to qb:componentProperty which makes explicit that the component is a dimension
- bm25 21.39 `http://purl.org/linked-data/cube#measureDimension` [property, tier 1] An alternative to qb:componentProperty which makes explicit that the component is a measure dimension
- bm25 20.66 `http://purl.org/linked-data/cube#componentProperty` [property, tier 1] indicates a ComponentProperty (i.e. attribute/dimension) expected on a DataSet, or a dimension fixed in a SliceKey
- bm25 15.82 `https://w3id.org/airo#hasComponent` [property, tier 3] Indicates a component incorporating an AI system or another component.
- bm25 14.69 `http://purl.org/linked-data/cube#ComponentSpecification` [class, tier 1] Used to define properties of a component (attribute, dimension etc) which are specific to its usage in a DSD.
- bm25 14.04 `http://rdf-vocabulary.ddialliance.org/xkos#hasPart` [property, tier 2] 
- bm25 14.03 `http://data.europa.eu/eli/ontology#has_part` [property, tier 2] inverse of "is_part_of"
- bm25 13.97 `http://purl.obolibrary.org/obo/IAO_0000142` [property, tier 2] An information artifact IA mentions an entity E exactly when it has a component/part that denotes E
- bm25 13.68 `https://schema.org/priceComponentType` [property, tier 2, RO-Crate] Identifies a price component (for example, a line item on an invoice), part of the total price for an offer.
- bm25 13.53 `http://www.w3.org/ns/dqv#inDimension` [property, tier 2] Represents the dimensions a quality metric, certificate and annotation allow a measurement of.
- bm25 13.46 `http://www.w3.org/ns/mls#hasPart` [property, tier 2] A relation which represents a part-whole relationship holding between an entity and its part.
- bm25 13.11 `https://schema.org/hasPart` [property, tier 2, RO-Crate] Indicates an item or CreativeWork that is part of this item, or CreativeWork (in some sense).
- bm25+lead 12.99 `http://purl.org/dc/terms/hasPart` [property, tier 1, DCAT-AP optional/other] A related resource that is included either physically or logically in the described resource.
- bm25 12.77 `http://purl.org/skos-history/SchemeDeltaInsertions` [class, tier 3] Should be related to the delta by dcterms:isPartOf.
- bm25 12.77 `http://purl.org/skos-history/SchemeDeltaDeletions` [class, tier 3] Should be related to the delta by dcterms:isPartOf.
- lead 8.63 `http://purl.org/linked-data/cube#component` [property, tier 1] indicates a component specification which is included in the structure of the dataset

## 28. oht:axisKind (M)

whether an axis is ordinal or categorical

- bm25 11.51 `https://w3id.org/dpv#hasScale` [property, tier 2] Indicates the scale of specified concept
- bm25 11.15 `https://w3id.org/dpv#hasProcessingScale` [property, tier 2] Indicates the scale of processing operations
- bm25 10.82 `https://w3id.org/dpv#hasDataSubjectScale` [property, tier 2] Indicates the scale of data subjects
- bm25 10.55 `http://rdf-vocabulary.ddialliance.org/discovery#kindOfData` [property, tier 3] The general kind of data (e.g. geospatial, register, survey) collected in this study, given either as a skos:Concept, or as a blank node with attached free-text
- bm25 9.75 `https://w3id.org/dpv#ProcessingScale` [class, tier 2] Scale of Processing
- bm25 9.62 `https://w3id.org/dpv#Scale` [class, tier 2] A measurement along some dimension
- bm25 9.59 `http://www.w3.org/2006/time#TRS` [class, tier 1] A temporal reference system, such as a temporal coordinate system (with an origin, direction, and scale), a calendar-clock combination, or a (possibly hierarchi
- bm25 9.4 `https://schema.org/energyEfficiencyScaleMin` [property, tier 2, RO-Crate] Specifies the least energy efficient class on the regulated EU energy consumption scale for the product category a product belongs to. For example, energy consu
- bm25 9.4 `https://schema.org/energyEfficiencyScaleMax` [property, tier 2, RO-Crate] Specifies the most energy efficient class on the regulated EU energy consumption scale for the product category a product belongs to. For example, energy consum
- bm25 9.37 `https://w3id.org/dpv#DataSubjectScale` [class, tier 2] Scale of Data Subject(s)
- bm25 9.3 `http://www.w3.org/2006/time#nominalPosition` [property, tier 1] The (nominal) value indicating temporal position in an ordinal reference system
- bm25 9.25 `https://w3id.org/dpv#NationalScale` [class, tier 2] Geographic coverage spanning a nation
- bm25 9.16 `https://w3id.org/dpv#LocalityScale` [class, tier 2] Geographic coverage spanning a specific locality
- bm25 9.16 `https://w3id.org/dpv#GlobalScale` [class, tier 2] Geographic coverage spanning the entire globe
- bm25 9.08 `https://w3id.org/dpv#RegionalScale` [class, tier 2] Geographic coverage spanning a specific region or regions
- lead 0.0 `http://purl.org/dc/terms/type` [property, tier 1, DCAT-AP optional/other] The nature or genre of the resource.

## 29. oht:multiValued (D)

whether a concept may take several values on the axis

- bm25 17.44 `https://w3id.org/sssom/mapping_cardinality` [property, tier 2] A value indicating whether the subject (respectively object) of this mapping record is present in other records involving a different object (respectively subje
- bm25 15.23 `https://w3id.org/sssom/mapping_cardinality_enum#n:n` [individual, tier 2] Indicates the mapping record is about a many-to-many mapping, that is, the subject is mapped to several different objects and the object is mapped to several di
- bm25 14.82 `https://schema.org/multipleValues` [property, tier 2, RO-Crate] Whether multiple values are allowed for the property. Default is false.
- bm25 14.25 `https://w3id.org/sssom/mapping_cardinality_enum#n:1` [individual, tier 2] Indicates the mapping record is about a many-to-one mapping, that is, several different subjects are mapped to the same object.
- bm25 14.25 `https://w3id.org/sssom/mapping_cardinality_enum#1:n` [individual, tier 2] Indicates the mapping record is about a one-to-many mapping, that is, the same subject is mapped to several different objects.
- bm25 14.17 `http://www.w3.org/2002/07/owl#cardinality` [property, tier 1] The property that determines the cardinality of an exact cardinality restriction.
- bm25 13.79 `http://www.w3.org/2002/07/owl#minCardinality` [property, tier 1] The property that determines the cardinality of a minimum cardinality restriction.
- bm25 13.79 `http://www.w3.org/2002/07/owl#maxCardinality` [property, tier 1] The property that determines the cardinality of a maximum cardinality restriction.
- bm25 13.7 `http://www.w3.org/2002/07/owl#qualifiedCardinality` [property, tier 1] The property that determines the cardinality of an exact qualified cardinality restriction.
- bm25 13.34 `http://www.w3.org/2002/07/owl#minQualifiedCardinality` [property, tier 1] The property that determines the cardinality of a minimum qualified cardinality restriction.
- bm25 13.34 `http://www.w3.org/2002/07/owl#maxQualifiedCardinality` [property, tier 1] The property that determines the cardinality of a maximum qualified cardinality restriction.
- bm25 13.31 `https://schema.org/playMode` [property, tier 2, RO-Crate] Indicates whether this game is multi-player, co-op or single-player. The game can be marked as multi-player, co-op and single-player at the same time.
- bm25 11.68 `http://purl.obolibrary.org/obo/IAO_0000184` [class, tier 2] A scatterplot is a graph which uses Cartesian coordinates to display values for two variables for a set of data. The data is displayed as a collection of points
- bm25 11.4 `https://w3id.org/semapv/vocab/CardinalityFiltering` [class, tier 2] 
- bm25 10.76 `http://cv.iptc.org/newscodes/digitalsourcetype/composite` [individual, tier 2] Mix or composite of several elements, any of which may or may not be generative AI
- lead 0.0 `http://www.w3.org/2002/07/owl#FunctionalProperty` [class, tier 1] The class of functional properties.

## 30. oht:hasFacetValue (D)

a concept takes a value from one of its scheme's axes

- bm25 19.55 `http://www.w3.org/ns/org#classification` [property, tier 1] Indicates a classification for this Organization within some classification scheme. Extension vocabularies may wish to specialize this property to have a range 
- bm25 18.97 `http://w3id.org/nkos/nkostype#classification_scheme` [individual, tier 3] schedule of concepts and pre-coordinated combinations of concepts, arranged by classification
- bm25 17.6 `http://www.w3.org/2004/02/skos/core#topConceptOf` [property, tier 1] Relates a concept to the concept scheme that it is a top level concept of.
- bm25 17.5 `http://www.w3.org/2004/02/skos/core#inScheme` [property, tier 1] Relates a resource (for example a concept) to a concept scheme in which it is included.
- bm25 16.35 `http://www.w3.org/2004/02/skos/core#notation` [property, tier 1, DCAT-AP optional/other] A notation, also known as classification code, is a string of characters such as "T58.5" or "303.4833" used to uniquely identify a concept within the scope of a
- bm25 15.47 `http://data.europa.eu/eli/ontology#LegalValue` [class, tier 2] Formally defined as the set of skos:Concept in concept scheme eli:LegalValueTable
- bm25 15.36 `http://www.w3.org/2002/07/owl#withRestrictions` [property, tier 1] The property that determines the collection of facet-value pairs that define a datatype restriction.
- bm25 14.63 `http://purl.org/linked-data/cube#measureType` [property, tier 1] Generic measure dimension, the value of this dimension indicates which measure (from the set of measures in the DSD) is being given by the obsValue (or other pr
- bm25 14.17 `http://www.w3.org/2004/02/skos/core#hasTopConcept` [property, tier 1] Relates, by convention, a concept scheme to a concept which is topmost in the broader/narrower concept hierarchies for that scheme, providing an entry point to 
- bm25 14.03 `http://purl.org/linked-data/cube#dimension` [property, tier 1] An alternative to qb:componentProperty which makes explicit that the component is a dimension
- bm25 13.98 `http://www.w3.org/2004/02/skos/core#ConceptScheme` [class, tier 1] A set of concepts, optionally including statements about semantic relationships between those concepts.
- bm25 13.53 `http://www.w3.org/ns/dqv#inDimension` [property, tier 2] Represents the dimensions a quality metric, certificate and annotation allow a measurement of.
- bm25 13.49 `http://purl.org/linked-data/cube#measureDimension` [property, tier 1] An alternative to qb:componentProperty which makes explicit that the component is a measure dimension
- bm25 13.0 `http://purl.org/skos-history/SchemeDelta` [class, tier 3] The delta of two versions of a SKOS concept scheme.
- bm25 12.42 `http://data.europa.eu/eli/ontology#in_force` [property, tier 2] A value indicating the legal force of a legal resource or a legal expression. A set of values is defined by ELI in the corresponding concept scheme. These value
- lead 4.6 `http://www.w3.org/2004/02/skos/core#related` [property, tier 1] Relates a concept to a concept with which there is an associative semantic relationship.

## 31. oht:consequence (M)

what follows from a concept or value in the scheme (a note users filter on)

- bm25+lead 24.98 `http://www.w3.org/2004/02/skos/core#scopeNote` [property, tier 1] A note that helps to clarify the meaning and/or the use of a concept.
- bm25 17.6 `http://www.w3.org/2004/02/skos/core#topConceptOf` [property, tier 1] Relates a concept to the concept scheme that it is a top level concept of.
- bm25 17.5 `http://www.w3.org/2004/02/skos/core#inScheme` [property, tier 1] Relates a resource (for example a concept) to a concept scheme in which it is included.
- bm25 16.8 `https://w3id.org/dpv#hasConsequence` [property, tier 2] Indicates consequence(s) possible or arising from specified concept
- bm25 16.68 `https://w3id.org/dpv#hasScope` [property, tier 2] Indicates the scope of specified concept or context
- bm25 16.42 `http://www.w3.org/2004/02/skos/core#notation` [property, tier 1, DCAT-AP optional/other] A notation, also known as classification code, is a string of characters such as "T58.5" or "303.4833" used to uniquely identify a concept within the scope of a
- bm25 16.37 `http://rdf-vocabulary.ddialliance.org/xkos#follows` [property, tier 2] 
- bm25 15.72 `https://w3id.org/sssom/cardinality_scope` [property, tier 2] A list of mapping slots that define the scope for the value found in the mapping_cardinality slot. Mappings are considered to belong to the same scope if they h
- bm25 15.47 `http://data.europa.eu/eli/ontology#LegalValue` [class, tier 2] Formally defined as the set of skos:Concept in concept scheme eli:LegalValueTable
- bm25 15.41 `https://schema.org/follows` [property, tier 2, RO-Crate] The most generic uni-directional social relation.
- bm25 14.67 `https://w3id.org/dpv/risk#PotentialConsequence` [class, tier 2] Indicates a concept can potentially be a 'consequence concept within an use-case
- bm25 14.55 `https://w3id.org/airo#followsCodeOfConduct` [property, tier 3] Indicates the code of conduct followed.
- bm25 14.17 `http://www.w3.org/2004/02/skos/core#hasTopConcept` [property, tier 1] Relates, by convention, a concept scheme to a concept which is topmost in the broader/narrower concept hierarchies for that scheme, providing an entry point to 
- bm25 13.98 `http://www.w3.org/2004/02/skos/core#ConceptScheme` [class, tier 1] A set of concepts, optionally including statements about semantic relationships between those concepts.
- bm25 13.97 `https://w3id.org/dpv#Filter` [class, tier 2] to filter or keep data for some criteria
- lead 7.92 `http://www.w3.org/2004/02/skos/core#note` [property, tier 1] A general note, for any purpose.

## 32. oht:hasOutput (P)

attaches an output specification to a scheme or classifier

- bm25+lead 17.3 `http://www.w3.org/ns/ssn/hasOutput` [property, tier 1] Relation between a Procedure and an Output of it.
- bm25 13.92 `https://w3id.org/airo#hasControlOverAIOutput` [property, tier 3] Indicates the level of control a stakeholder has over outputs produced by an AI system.
- bm25 13.51 `http://www.w3.org/ns/mls#hasOutput` [property, tier 2] A relation between a run and either a model or model evaluation that is produced on it’s output.
- bm25 13.34 `http://purl.obolibrary.org/obo/IAO_0000418` [property, tier 2] A relation between a data item and a quality of a material entity where the material entity is the specified output of a material transformation which achieves 
- bm25 12.28 `http://www.w3.org/2004/02/skos/core#hasTopConcept` [property, tier 1] Relates, by convention, a concept scheme to a concept which is topmost in the broader/narrower concept hierarchies for that scheme, providing an entry point to 
- bm25 12.2 `http://www.w3.org/ns/odrl/2/output` [property, tier 1] The output property specifies the Asset which is created from the output of the Action.
- bm25 11.84 `https://w3id.org/airo#hasInput` [property, tier 3] Indicates the input an AI system or componet need to process to generate output.
- bm25 11.7 `http://www.w3.org/2004/02/skos/core#inScheme` [property, tier 1] Relates a resource (for example a concept) to a concept scheme in which it is included.
- bm25 11.63 `https://w3id.org/airo#producesOutput` [property, tier 3] Specifies an output generated by an AI system or component.
- bm25 11.07 `https://schema.org/serviceOutput` [property, tier 2, RO-Crate] The tangible thing generated by the service, e.g. a passport, permit, etc.
- bm25 10.83 `https://schema.org/hasShippingService` [property, tier 2] Specification of a shipping service offered by the organization.
- bm25 10.58 `http://www.w3.org/2004/02/skos/core#topConceptOf` [property, tier 1] Relates a concept to the concept scheme that it is a top level concept of.
- bm25 10.26 `https://w3id.org/airo#Output` [class, tier 3] Output generated by the system.
- bm25 9.98 `http://www.w3.org/ns/ssn/Output` [class, tier 1] Any information that is reported from a Procedure.
- bm25 9.67 `http://w3id.org/nkos/nkostype#categorization_scheme` [individual, tier 3] loosely formed grouping scheme

## 33. oht:outputType (M)

boolean, probability, ordinal, score or none

- bm25 14.88 `http://www.w3.org/ns/odrl/2/isNoneOf` [individual, tier 1] A set-based operator indicating that a given value is none of the right operand of the Constraint.
- bm25 13.28 `https://w3id.org/sssom/similarity_score` [property, tier 2] A score between 0 and 1 to denote the similarity between two entities, where 1 denotes equivalence, and 0 denotes disjointness. The score is meant to be used in
- bm25 13.27 `https://schema.org/mapType` [property, tier 2, RO-Crate] Indicates the kind of Map, from the MapCategoryType Enumeration.
- bm25 13.14 `http://www.w3.org/ns/dqv#expectedDataType` [property, tier 2] Represents the expected data type for metric's observed value (e.g. xsd:boolean, xsd:double etc...)
- bm25 12.94 `https://schema.org/Boolean` [class, tier 2, RO-Crate] Boolean: True or False.
- bm25 12.4 `https://schema.org/albumReleaseType` [property, tier 2, RO-Crate] The kind of release which this album is: single, EP or album.
- bm25 12.2 `http://www.w3.org/ns/odrl/2/output` [property, tier 1] The output property specifies the Asset which is created from the output of the Action.
- bm25 12.13 `https://schema.org/learningResourceType` [property, tier 2, RO-Crate] The predominant type or kind characterizing the learning resource. For example, 'presentation', 'handout'.
- bm25 12.04 `https://w3id.org/vair#DeterminingCreditScore` [class, tier 3] Determining credit score of a person
- bm25 11.84 `https://schema.org/MedicalRiskScore` [class, tier 2, RO-Crate] A simple system that adds up the number of risk factors to yield a score that is associated with prognosis, e.g. CHAD score, TIMI risk score.
- bm25 11.81 `http://www.w3.org/ns/ssn/hasOutput` [property, tier 1] Relation between a Procedure and an Output of it.
- bm25 11.63 `https://w3id.org/airo#producesOutput` [property, tier 3] Specifies an output generated by an AI system or component.
- bm25 11.07 `https://schema.org/serviceOutput` [property, tier 2, RO-Crate] The tangible thing generated by the service, e.g. a passport, permit, etc.
- bm25 10.55 `http://rdf-vocabulary.ddialliance.org/discovery#kindOfData` [property, tier 3] The general kind of data (e.g. geospatial, register, survey) collected in this study, given either as a skos:Concept, or as a blank node with attached free-text
- bm25 10.52 `https://w3id.org/sssom/similarity_measure` [property, tier 2] The measure used for computing a similarity score. This field is meant to be used in conjunction with the similarity_score field, to document, for example, the 
- lead 5.5 `http://purl.org/dc/terms/type` [property, tier 1, DCAT-AP optional/other] The nature or genre of the resource.

## 34. oht:outputAxis (D)

for ordinal outputs, the axis returned

- bm25 15.15 `https://w3id.org/airo#ModeOfOutputControllability` [class, tier 3] The level of control over AI outputs exercised by humans.
- bm25 15.1 `https://w3id.org/airo#hasControlOverAIOutput` [property, tier 3] Indicates the level of control a stakeholder has over outputs produced by an AI system.
- bm25 12.52 `https://schema.org/OrderReturned` [individual, tier 2, RO-Crate] OrderStatus representing that an order has been returned.
- bm25 12.2 `http://www.w3.org/ns/odrl/2/output` [property, tier 1] The output property specifies the Asset which is created from the output of the Action.
- bm25 11.81 `http://www.w3.org/ns/ssn/hasOutput` [property, tier 1] Relation between a Procedure and an Output of it.
- bm25 11.63 `https://w3id.org/airo#producesOutput` [property, tier 3] Specifies an output generated by an AI system or component.
- bm25 11.51 `https://w3id.org/dpv#hasScale` [property, tier 2] Indicates the scale of specified concept
- bm25 11.15 `https://w3id.org/dpv#hasProcessingScale` [property, tier 2] Indicates the scale of processing operations
- bm25 11.07 `https://schema.org/serviceOutput` [property, tier 2, RO-Crate] The tangible thing generated by the service, e.g. a passport, permit, etc.
- bm25 10.82 `https://w3id.org/dpv#hasDataSubjectScale` [property, tier 2] Indicates the scale of data subjects
- bm25 10.26 `https://w3id.org/airo#Output` [class, tier 3] Output generated by the system.
- bm25 9.98 `http://www.w3.org/ns/ssn/Output` [class, tier 1] Any information that is reported from a Procedure.
- bm25 9.84 `http://www.w3.org/ns/mls#hasOutput` [property, tier 2] A relation between a run and either a model or model evaluation that is produced on it’s output.
- bm25 9.75 `https://w3id.org/dpv#ProcessingScale` [class, tier 2] Scale of Processing
- bm25 9.62 `https://w3id.org/dpv#Scale` [class, tier 2] A measurement along some dimension
- lead 0.0 `http://purl.org/linked-data/cube#dimension` [property, tier 1] An alternative to qb:componentProperty which makes explicit that the component is a dimension

## 35. oht:modality (D)

the kind of input a concept applies to (text, image, audio, video)

- bm25 23.4 `https://schema.org/videoFormat` [property, tier 2, RO-Crate] The type of screening or video broadcast used (e.g. IMAX, 3D, SD, HD, etc.).
- bm25 22.63 `https://schema.org/MediaObject` [class, tier 2, RO-Crate] A media object, such as an image, video, audio, or text object embedded in a web page or a downloadable dataset i.e. DataDownload. Note that a creative work may
- bm25 21.44 `http://data.europa.eu/eli/ontology#FormatType` [class, tier 2] Formally defined as the set of skos:Concept in concept scheme eli:MediaTypeTable.
- bm25 19.68 `https://schema.org/transcript` [property, tier 2, RO-Crate] If this MediaObject is an AudioObject or VideoObject, the transcript of that object.
- bm25 19.09 `https://schema.org/musicReleaseFormat` [property, tier 2, RO-Crate] Format of this release (the type of recording media used, i.e. compact disc, digital media, LP, etc.).
- bm25 18.87 `https://schema.org/EditedOrCroppedContent` [individual, tier 2, RO-Crate] Content coded 'edited or cropped content' in a [[MediaReview]], considered in the context of how it was published or shared. For a [[VideoObject]] to be 'edited
- bm25 18.53 `https://schema.org/sharedContent` [property, tier 2, RO-Crate] A CreativeWork such as an image, video, or audio clip shared as part of this posting.
- bm25 18.24 `http://purl.org/dc/terms/MediaType` [class, tier 1] A file format or physical medium.
- bm25 17.92 `http://rdf-vocabulary.ddialliance.org/discovery#kindOfData` [property, tier 3] The general kind of data (e.g. geospatial, register, survey) collected in this study, given either as a skos:Concept, or as a blank node with attached free-text
- bm25 17.79 `https://schema.org/MediaSubscription` [class, tier 2, RO-Crate] A subscription which allows a user to access media including audio, video, books, etc.
- bm25 17.64 `http://data.europa.eu/eli/ontology#media_type` [property, tier 2] The file format of the manifestation. This field is intended to capture the technical file format and will serve as a basis for content negotiation for the serv
- bm25+lead 17.61 `https://schema.org/encodingFormat` [property, tier 2, RO-Crate] Media type typically expressed using a MIME format (see [IANA site](http://www.iana.org/assignments/media-types/media-types.xhtml) and [MDN reference](https://d
- bm25 17.59 `https://schema.org/MusicReleaseFormatType` [class, tier 2, RO-Crate] Format of this release (the type of recording media used, i.e. compact disc, digital media, LP, etc.).
- bm25 17.55 `https://schema.org/contentUrl` [property, tier 2, RO-Crate] Actual bytes of the media object, for example the image file or video file.
- bm25 17.47 `https://schema.org/DigitalAudioTapeFormat` [individual, tier 2, RO-Crate] DigitalAudioTapeFormat.
- lead 8.84 `http://purl.org/dc/terms/format` [property, tier 1, DCAT-AP optional/other] The file format, physical medium, or dimensions of the resource.
- lead 0.0 `http://purl.org/dc/terms/medium` [property, tier 1] The material or physical carrier of the resource.

## 36. oht:legalBasis (D)

the legal provision behind a concept, as an ELI legal resource

- bm25 22.43 `https://w3id.org/dpv#LegalBasis` [class, tier 2] Legal basis used to justify processing of data or use of technology in accordance with a law
- bm25+lead 20.78 `https://w3id.org/dpv#hasLegalBasis` [property, tier 2] Indicates use or applicability of a Legal Basis
- bm25 20.09 `http://data.europa.eu/eli/ontology#cited_by_case_law` [property, tier 2] Indicates that this LegalResource or LegalExpression is being cited in a case law, identified by a suitable URI. If the case law cannot be identified by a suita
- bm25 19.89 `http://data.europa.eu/eli/ontology#cited_by_case_law_reference` [property, tier 2] Indicates that this LegalResource or LegalExpression is being cited in a case law that cannot be identified by a suitable URI and that is indicated by textual r
- bm25 19.74 `http://data.europa.eu/eli/ontology#ensures_implementation_of` [property, tier 2] Indicates that this LegalResource ensures the implementation of another LegalResource. This implies a legal meaning (contrary to eli:applies). This can cover li
- bm25 19.3 `http://data.europa.eu/eli/ontology#implementation_ensured_by` [property, tier 2] Indicates that the implementation of this LegalResource is ensured by another LegalResource. This implies a legal meaning (contrary to eli:applies). See the def
- bm25 19.23 `http://data.europa.eu/eli/ontology#in_force` [property, tier 2] A value indicating the legal force of a legal resource or a legal expression. A set of values is defined by ELI in the corresponding concept scheme. These value
- bm25 16.89 `http://data.europa.eu/eli/ontology#LegalResource` [class, tier 2] A work in a legislative corpus. This applies to acts that have been legally enacted (whether or not they are still in force). For example, the abstract concept 
- bm25 16.65 `http://data.europa.eu/eli/ontology#amends` [property, tier 2] Indicates that this work introduces legal changes in another resource. For modifications that don’t have a legal impact, use eli:corrects.
- bm25 16.4 `http://data.europa.eu/eli/ontology#legal_value` [property, tier 2] The legal value associated with a specific format of a resource. A set of values is defined by ELI in the corresponding concept scheme. These values are : - uno
- bm25 16.39 `http://data.europa.eu/eli/ontology#LegalResourceSubdivision` [class, tier 2] A component of a legal act, at an arbitrary level of precision, like a chapter, an article, an alinea, a paragraph or an list item. A subdivision can be linked 
- bm25 16.35 `http://data.europa.eu/eli/ontology#LegalValue` [class, tier 2] Formally defined as the set of skos:Concept in concept scheme eli:LegalValueTable
- bm25 16.34 `http://data.europa.eu/eli/ontology#amended_by` [property, tier 2] Inverse of "amends". Indicates a work that introduced legal changes in this resource. For modifications that don’t have a legal impact, use eli:corrected_by.
- bm25 16.19 `https://w3id.org/dpv#DataTransferLegalBasis` [class, tier 2] Specific or special categories and instances of legal basis intended for justifying data transfers
- bm25 15.71 `http://data.europa.eu/eli/ontology#LegalExpression` [class, tier 2] The intellectual realisation of a legal resource in the form of a "sequence of signs" (typically alpha-numeric characters in a legal context). For example, any 
- lead 13.01 `http://data.europa.eu/eli/ontology#based_on` [property, tier 2] Inverse of "basis_for". Indicates that thiswork is empowered by another one, typically a constitution, a treaty or an enabling act.
- lead 12.73 `http://data.europa.eu/eli/ontology#implements` [property, tier 2, DEPRECATED owl:deprecated] This property is deprecated. Use "applies" instead.
- lead 5.35 `http://purl.org/dc/terms/source` [property, tier 1, DCAT-AP optional/other] A related resource from which the described resource is derived.

## 37. oht:contextDependent (D)

the scheme says the concept's status depends on deployment context

- bm25 17.6 `http://www.w3.org/2004/02/skos/core#topConceptOf` [property, tier 1] Relates a concept to the concept scheme that it is a top level concept of.
- bm25 17.5 `http://www.w3.org/2004/02/skos/core#inScheme` [property, tier 1] Relates a resource (for example a concept) to a concept scheme in which it is included.
- bm25 14.68 `http://www.w3.org/ns/ssn/inDeployment` [property, tier 1] Relation between a Platform and a Deployment, meaning that the deployedSystems of the Deployment are hosted on the Platform.
- bm25 14.48 `http://www.w3.org/ns/ssn/hasDeployment` [property, tier 1] Relation between a System and a Deployment, recording that the System is deployed in that Deployment.
- bm25 14.17 `http://www.w3.org/2004/02/skos/core#hasTopConcept` [property, tier 1] Relates, by convention, a concept scheme to a concept which is topmost in the broader/narrower concept hierarchies for that scheme, providing an entry point to 
- bm25 13.98 `http://www.w3.org/2004/02/skos/core#ConceptScheme` [class, tier 1] A set of concepts, optionally including statements about semantic relationships between those concepts.
- bm25 13.16 `http://www.w3.org/ns/adms#status` [property, tier 2, DCAT-AP optional/other] The status of the Asset in the context of a particular workflow process.
- bm25 13.0 `http://purl.org/skos-history/SchemeDelta` [class, tier 3] The delta of two versions of a SKOS concept scheme.
- bm25 12.67 `http://purl.org/iso25964/skos-thes#status` [property, tier 3] ISO status - on ThesaurusConcept - on ThesaurusTerm
- bm25 12.31 `https://w3id.org/dpv#hasStatus` [property, tier 2] Indicates the status of specified concept
- bm25 12.23 `http://www.w3.org/ns/ssn/Deployment` [class, tier 1] Describes the Deployment of one or more Systems for a particular purpose. Deployment may be done on a Platform.
- bm25 12.03 `http://data.europa.eu/eli/ontology#WorkType` [class, tier 2] 
- bm25 11.95 `http://data.europa.eu/eli/ontology#legal_value` [property, tier 2] The legal value associated with a specific format of a resource. A set of values is defined by ELI in the corresponding concept scheme. These values are : - uno
- bm25 11.72 `https://w3id.org/vair#Deployment` [class, tier 3] Refers to deployment phase when the AI system is installed, released or configured for operation in a target environment.
- bm25 11.51 `https://w3id.org/dpv#hasComplianceStatus` [property, tier 2] Indicates the status of compliance of specified concept
- lead 0.0 `http://www.w3.org/2004/02/skos/core#note` [property, tier 1] A general note, for any purpose.

## 38. oht:verbatim (P)

on an explanatory note, whether the text is the source's exact words

- bm25 22.2 `http://purl.org/spar/cito/providesQuotationFor` [property, tier 2] A relation according to which the cited entity contains information, usually of a textual nature, that is quoted by (used as a quotation within) the citing enti
- bm25 22.15 `http://rdf-vocabulary.ddialliance.org/xkos#ExplanatoryNote` [class, tier 2] 
- bm25 21.78 `http://www.w3.org/ns/prov#qualifiedQuotation` [property, tier 1] If this Entity prov:wasQuotedFrom Entity :e, then it can qualify how using prov:qualifiedQuotation [ a prov:Quotation; prov:entity :e; :foo :bar ].
- bm25 19.04 `http://www.w3.org/ns/oa#exact` [property, tier 1] The object of the predicate is a copy of the text which is being selected, after normalization.
- bm25 18.55 `http://purl.org/ontology/bibo/annotates` [property, tier 2] Critical or explanatory note for a Document.
- bm25+lead 16.3 `http://www.w3.org/ns/prov#Quotation` [class, tier 1] A quotation is the repeat of (some or all of) an entity, such as text or image, by someone who may or may not be its original author. Quotation is a particular 
- bm25 15.39 `http://purl.org/dc/dcmitype/Text` [class, tier 1] A resource consisting primarily of words for reading.
- bm25+lead 15.2 `http://www.w3.org/ns/prov#wasQuotedFrom` [property, tier 1] An entity is derived from an original entity by copying, or 'quoting', some or all of it.
- bm25 14.45 `https://schema.org/Quotation` [class, tier 2, RO-Crate] A quotation. Often but not necessarily from some written work, attributable to a real world author and - if associated with a fictional character - to any ficti
- bm25 14.25 `http://www.w3.org/ns/prov#quotedAs` [untyped, tier 1] 
- bm25+lead 14.15 `http://purl.org/spar/cito/includesQuotationFrom` [property, tier 2] A relation according to which the citing entity includes one or more quotations from the cited entity.
- bm25 14.07 `http://usefulinc.com/ns/doap#shortdesc` [property, tier 2] Short (8 or 9 words) plain text description of a project.
- bm25 14.01 `http://data.europa.eu/eli/ontology#cites` [property, tier 2] Citation in the text of the legislation. This may be at the legal resource or legal expression level, as required by the implementation context. This includes v
- bm25 12.86 `http://www.w3.org/ns/prov#qualifiedQuotationOf` [untyped, tier 1] 
- bm25 12.81 `https://schema.org/wordCount` [property, tier 2, RO-Crate] The number of words in the text of the CreativeWork such as an Article, Book, etc.

## 39. oht:operationalises (D)

this scheme turns the target's duties or principles into practice

- bm25 25.32 `http://www.w3.org/ns/mls#implements` [property, tier 2] A relation between an information entity and a specification that it conforms to.
- bm25+lead 15.76 `http://purl.org/dc/terms/conformsTo` [property, tier 1, DCAT-AP optional/other, RO-Crate] An established standard to which the described resource conforms.
- bm25 14.91 `http://www.w3.org/ns/ssn/implements` [property, tier 1] Relation between an entity that implements a Procedure in some executable way and the Procedure (an algorithm, procedure or method).
- bm25 14.84 `https://w3id.org/airo#conformsToStandard` [property, tier 3] Indicates conformance of an entity to a standard.
- bm25 14.79 `http://usefulinc.com/ns/doap#implements` [property, tier 2] A specification that a project implements. Could be a standard, API or legally defined level of conformance.
- bm25 14.57 `http://data.europa.eu/eli/ontology#applies` [property, tier 2] Indicates that this legislation (or part of a legislation) somehow conforms with another legislation. This is an informative link, and it has no legal value. Fo
- bm25 13.04 `https://schema.org/publishingPrinciples` [property, tier 2, RO-Crate] The publishingPrinciples property indicates (typically via [[URL]]) a document describing the editorial principles of an [[Organization]] (or individual, e.g. a
- bm25 12.08 `https://schema.org/legislationTransposes` [property, tier 2, RO-Crate] Indicates that this legislation (or part of legislation) fulfills the objectives set by another legislation, by passing appropriate implementation measures. Typ
- bm25 11.91 `http://www.w3.org/ns/odrl/2/#duties` [individual, tier 1] 
- bm25 11.7 `http://www.w3.org/2004/02/skos/core#inScheme` [property, tier 1] Relates a resource (for example a concept) to a concept scheme in which it is included.
- bm25 11.51 `http://w3id.org/nkos/nkostype#subject_heading_scheme` [individual, tier 3] structured vocabulary comprising terms available for subject indexing, plus rules for combining them into pre-coordinated strings of terms where necessary
- bm25 11.18 `https://schema.org/target` [property, tier 2, RO-Crate] Indicates a target EntryPoint, or url, for an Action.
- bm25 11.04 `http://rdf-vocabulary.ddialliance.org/xkos#targetConcept` [property, tier 2] 
- bm25 11.0 `http://www.w3.org/ns/oa#hasTarget` [property, tier 1] The relationship between an Annotation and its Target.
- bm25 10.83 `https://schema.org/targetCollection` [property, tier 2, RO-Crate] A sub property of object. The collection target of the action.
- lead 12.73 `http://data.europa.eu/eli/ontology#implements` [property, tier 2, DEPRECATED owl:deprecated] This property is deprecated. Use "applies" instead.
- lead 7.14 `http://data.europa.eu/eli/ontology#transposes` [property, tier 2] Indicates that this legislation (or part of legislation) fulfills the objectives set by another legislation, by passing appropriate implementation measures. Typ

## 40. oht:operationalisedBy (D)

inverse of operationalises

- bm25 12.68 `https://w3id.org/dpv#isImplementedByEntity` [property, tier 2] Indicates implementation details such as entities or agents
- bm25 12.45 `http://www.w3.org/ns/ssn/implementedBy` [property, tier 1] Relation between a Procedure (an algorithm, procedure or method) and an entity that implements that Procedure in some executable way.
- bm25 12.22 `https://w3id.org/dpv#isImplementedUsingTechnology` [property, tier 2] Indicates implementation details such as technologies or processes
- bm25 11.65 `http://www.w3.org/2002/07/owl#inverseOf` [property, tier 1] The property that determines that two given properties are inverse.
- bm25 11.02 `https://w3id.org/dpv#hasInverseJurisdiction` [property, tier 2] Indicates the inverse jurisdiction for a given jurisdiction
- bm25 10.25 `https://schema.org/inverseOf` [property, tier 2, RO-Crate] Relates a property to a property that is its inverse. Inverse properties relate the same pairs of items to each other, but in reversed direction. For example, t
- bm25 9.26 `http://www.w3.org/2002/07/owl#InverseFunctionalProperty` [class, tier 1] The class of inverse-functional properties.
- bm25 9.05 `https://w3id.org/dpv#InverseJurisdiction` [class, tier 2] An inverse jurisdiction for a specific jurisdiction is the set of all other jurisdictions that are not part of the specific jurisdiction
- bm25 8.48 `http://www.w3.org/ns/prov#inverse` [property, tier 1] PROV-O does not define all property inverses. The directionalities defined in PROV-O should be given preference over those not defined. However, if users wish t
- bm25 8.03 `http://usefulinc.com/ns/doap#programming-language` [property, tier 2] Programming language a project is implemented in or intended for use with.
- bm25 8.02 `http://purl.obolibrary.org/obo/IAO_0000235` [property, tier 2] inverse of the relation 'denotes'
- bm25 8.02 `http://purl.obolibrary.org/obo/IAO_0000143` [property, tier 2] Inverse of the relation 'mentions'
- bm25 7.84 `http://purl.obolibrary.org/obo/IAO_0000113` [property, tier 2] An annotation property indicating which module the terms belong to. This is currently experimental and not implemented yet.
- bm25 7.66 `https://w3id.org/airo#hasCapability` [property, tier 3] Specifies capabilities implemented within an AI system to materialise its purposes.
- bm25 7.6 `http://data.europa.eu/eli/ontology#is_embodied_by` [property, tier 2] Relates an expression to a manifestation of that expression. Inverse of "embodies".
- lead 11.09 `http://data.europa.eu/eli/ontology#implemented_by` [property, tier 2, DEPRECATED owl:deprecated] This property is deprecated. Use "applied_by" instead.
- lead 5.59 `http://data.europa.eu/eli/ontology#transposed_by` [property, tier 2] Inverse of "transposes". Note that this property is expressed on a legal resource, not on one of its language-specific legal expression.

## 41. oht:conflictsWith (D)

two schemes make incompatible claims about the same field

- bm25+lead 21.83 `http://www.w3.org/2002/07/owl#disjointWith` [property, tier 1] The property that determines that two given classes are disjoint.
- bm25 20.71 `http://www.w3.org/2002/07/owl#propertyDisjointWith` [property, tier 1] The property that determines that two given properties are disjoint.
- bm25 18.14 `http://www.w3.org/2002/07/owl#incompatibleWith` [property, tier 1] The annotation property that indicates that a given ontology is incompatible with another ontology.
- bm25+lead 16.97 `http://purl.org/spar/cito/disagreesWith` [property, tier 2] A relation according to which the citing entity disagrees with statements, ideas or conclusions presented in the cited entity.
- bm25 16.68 `http://www.w3.org/2002/07/owl#sameAs` [property, tier 1] The property that determines that two given individuals are equal.
- bm25 16.03 `https://schema.org/geoDisjoint` [property, tier 2, RO-Crate] Represents spatial relations in which two geometries (or the places they represent) are topologically disjoint: "they have no point in common. They form a set o
- bm25+lead 15.58 `http://rdf-vocabulary.ddialliance.org/xkos#disjoint` [property, tier 2] 
- bm25 15.45 `http://www.w3.org/ns/odrl/2/conflict` [property, tier 1] The conflict-resolution strategy for a Policy.
- bm25 14.22 `http://www.w3.org/2002/07/owl#disjointUnionOf` [property, tier 1] The property that determines that a given class is equivalent to the disjoint union of a collection of other classes.
- bm25 13.79 `http://www.w3.org/ns/odrl/2/ConflictTerm` [class, tier 1] Used to establish strategies to resolve conflicts that arise from the merging of Policies or conflicts between Permissions and Prohibitions in the same Policy.
- bm25 13.79 `https://w3id.org/sssom/similarity_measure` [property, tier 2] The measure used for computing a similarity score. This field is meant to be used in conjunction with the similarity_score field, to document, for example, the 
- bm25 13.45 `http://www.w3.org/2004/02/skos/core#mappingRelation` [property, tier 1] Relates two concepts coming, by convention, from different schemes, and that have comparable meanings
- bm25 12.34 `http://www.w3.org/2006/time#intervalDisjoint` [property, tier 1] If a proper interval T1 is intervalDisjoint another proper interval T2, then the beginning of T1 is after the end of T2, or the end of T1 is before the beginnin
- bm25 12.22 `http://www.w3.org/ns/prov#alternateOf` [property, tier 1] Two alternate entities present aspects of the same thing. These aspects may be the same or different, and the alternate entities may or may not overlap in time.
- bm25 11.95 `http://www.w3.org/2002/07/owl#AllDisjointProperties` [class, tier 1] The class of collections of pairwise disjoint properties.

## 42. oht:hasUptake (P)

attaches uptake evidence to a scheme

- bm25 16.3 `http://www.w3.org/ns/duv#hasUsageTool` [property, tier 2] Describes the tool that provides the Usage
- bm25+lead 15.91 `http://www.w3.org/ns/duv#hasUsage` [property, tier 2] Dataset/distribution usage guidance or instructions.
- bm25 12.79 `https://schema.org/evidenceLevel` [property, tier 2, RO-Crate] Strength of evidence of the data used to formulate the guideline (enumerated).
- bm25 12.49 `http://purl.org/spar/cito/isCitedAsEvidenceBy` [property, tier 2] A relation according to which the cited entity is cited for providing factual evidence to the citing entity.
- bm25 12.31 `http://purl.org/spar/cito/citesAsEvidence` [property, tier 2] A relation according to which the citing entity cites the cited entity as source of factual evidence for statements it contains.
- bm25 12.28 `http://www.w3.org/2004/02/skos/core#hasTopConcept` [property, tier 1] Relates, by convention, a concept scheme to a concept which is topmost in the broader/narrower concept hierarchies for that scheme, providing an entry point to 
- bm25 12.05 `https://schema.org/evidenceOrigin` [property, tier 2, RO-Crate] Source of the data used to formulate the guidance, e.g. RCT, consensus opinion, etc.
- bm25 11.7 `http://www.w3.org/2004/02/skos/core#inScheme` [property, tier 1] Relates a resource (for example a concept) to a concept scheme in which it is included.
- bm25 11.28 `https://schema.org/permittedUsage` [property, tier 2, RO-Crate] Indications regarding the permitted usage of the accommodation.
- bm25 11.28 `http://www.w3.org/ns/prov#hadUsage` [property, tier 1] The _optional_ Usage involved in an Entity's Derivation.
- bm25 11.14 `https://schema.org/vehicleSpecialUsage` [property, tier 2, RO-Crate] Indicates whether the vehicle has been used for special purposes, like commercial rental, driving school, or as a taxi. The legislation in many countries requir
- bm25 10.77 `https://schema.org/hasMolecularFunction` [property, tier 2, RO-Crate] Molecular function performed by this BioChemEntity; please use PropertyValue if you want to include any evidence.
- bm25 10.58 `http://www.w3.org/2004/02/skos/core#topConceptOf` [property, tier 1] Relates a concept to the concept scheme that it is a top level concept of.
- bm25 10.57 `http://www.w3.org/ns/prov#qualifiedUsage` [property, tier 1] If this Activity prov:used Entity :e, then it can qualify how it used it using prov:qualifiedUsage [ a prov:Usage; prov:entity :e; :foo :bar ].
- bm25 10.41 `https://schema.org/MedicalEvidenceLevel` [class, tier 2, RO-Crate] Level of evidence for a medical guideline. Enumerated type.

## 43. oht:uptakeKind (M)

regulatory citation, platform adoption, benchmark use and so on

- bm25 15.41 `https://schema.org/contactType` [property, tier 2, RO-Crate] A person or organization can have different contact points, for different purposes. For example, a sales contact point, a PR contact point and so on. This prope
- bm25 15.22 `https://schema.org/targetPlatform` [property, tier 2, RO-Crate] Type of app development: phone, Metro style, desktop, XBox, etc.
- bm25 14.43 `https://schema.org/actionPlatform` [property, tier 2, RO-Crate] The high level platform(s) where the Action can be performed for the given URL. To specify a specific application or operating system instance, use actionApplic
- bm25 13.87 `https://schema.org/substanceOfConcern` [property, tier 2] A substance of concern (SoC) contained within the product, typically based on regulatory lists like REACH or RoHS.
- bm25 13.27 `https://schema.org/mapType` [property, tier 2, RO-Crate] Indicates the kind of Map, from the MapCategoryType Enumeration.
- bm25 12.71 `https://schema.org/bed` [property, tier 2, RO-Crate] The type of bed or beds included in the accommodation. For the single case of just one bed of a certain type, you use bed directly with a text. If you want to i
- bm25 12.68 `https://schema.org/departurePlatform` [property, tier 2, RO-Crate] The platform from which the train departs.
- bm25 12.58 `https://schema.org/arrivalPlatform` [property, tier 2, RO-Crate] The platform where the train arrives.
- bm25 12.53 `http://purl.org/spar/cito/isCitationCharacterizationOf` [property, tier 2] A relation between the characterization of a citation, made by using a CiTO citation characterization property, and that citation.
- bm25 12.4 `https://schema.org/albumReleaseType` [property, tier 2, RO-Crate] The kind of release which this album is: single, EP or album.
- bm25 12.38 `http://usefulinc.com/ns/doap#platform` [property, tier 2] Indicator of software platform (non-OS specific), e.g. Java, Firefox, ECMA CLR
- bm25 12.38 `http://www.w3.org/ns/ssn/deployedOnPlatform` [property, tier 1] Relation between a Deployment and the Platform on which the Systems are deployed.
- bm25 12.18 `http://purl.org/dc/terms/bibliographicCitation` [property, tier 1] A bibliographic reference for the resource.
- bm25 12.13 `https://schema.org/learningResourceType` [property, tier 2, RO-Crate] The predominant type or kind characterizing the learning resource. For example, 'presentation', 'handout'.
- bm25 12.03 `https://schema.org/citation` [property, tier 2, RO-Crate] A citation or reference to another creative work, such as another publication, web page, scholarly article, etc.
- lead 5.5 `http://purl.org/dc/terms/type` [property, tier 1, DCAT-AP optional/other] The nature or genre of the resource.

## 44. oht:strength (D)

strong, moderate, weak, as the library judges evidence

- bm25 21.64 `https://schema.org/evidenceLevel` [property, tier 2, RO-Crate] Strength of evidence of the data used to formulate the guideline (enumerated).
- bm25 15.13 `https://schema.org/recommendationStrength` [property, tier 2, RO-Crate] Strength of the guideline's recommendation (e.g. 'class I').
- bm25 15.13 `https://schema.org/availableStrength` [property, tier 2, RO-Crate] An available dosage strength for the drug.
- bm25 15.01 `https://schema.org/strengthValue` [property, tier 2, RO-Crate] The value of an active ingredient's strength, e.g. 325.
- bm25 15.01 `https://schema.org/strengthUnit` [property, tier 2, RO-Crate] The units of an active ingredient's strength, e.g. mg.
- bm25 14.23 `https://w3id.org/sssom/registry_confidence` [property, tier 2] This value is set by the creator/maintainer of the mapping registry and reflects the confidence the mapping registry has in the correctness (i.e., precision) of
- bm25+lead 14.05 `https://w3id.org/sssom/confidence` [property, tier 2] A value assigned by the creator of the mapping to denote the creator's confidence or estimated probability that the mapping record is correct. A value of 1.0 me
- bm25 13.81 `https://w3id.org/sssom/mapping_set_confidence` [property, tier 2] Mapping-set level confidence is assigned by the creator of the mapping set to indicate their overall confidence in the correctness (i.e., precision) of mappings
- bm25 13.48 `https://schema.org/executableLibraryName` [property, tier 2, RO-Crate] Library file name, e.g., mscorlib.dll, system.web.dll.
- bm25 12.66 `https://schema.org/Library` [class, tier 2, RO-Crate] A library.
- bm25 12.55 `https://w3id.org/dpv/risk#CustomerConfidenceLoss` [class, tier 2] Concept representing Customer Confidence Loss
- bm25 12.49 `http://purl.org/spar/cito/isCitedAsEvidenceBy` [property, tier 2] A relation according to which the cited entity is cited for providing factual evidence to the citing entity.
- bm25 12.32 `https://schema.org/DrugStrength` [class, tier 2, RO-Crate] A specific strength in which a medical drug is available in a specific country.
- bm25 12.31 `http://purl.org/spar/cito/citesAsEvidence` [property, tier 2] A relation according to which the citing entity cites the cited entity as source of factual evidence for statements it contains.
- bm25 12.05 `https://schema.org/evidenceOrigin` [property, tier 2, RO-Crate] Source of the data used to formulate the guidance, e.g. RCT, consensus opinion, etc.
- lead 8.31 `http://www.w3.org/ns/dqv#QualityAnnotation` [class, tier 2] Represents quality annotations, including ratings, quality certificates or feedback that can be associated to datasets or distributions. Quality annotations mus

## 45. oht:mappingRelation (P)

the relation an association asserts, including no_match

Leads not in index: sssom:predicate_id

- bm25 25.41 `https://w3id.org/sssom/predicate_label` [property, tier 2] The label of the predicate/relation of the mapping.
- bm25 24.66 `owl:annotatedProperty` [property, tier 2] The ID of the predicate or relation that relates the subject and object of this match.
- bm25 20.02 `https://w3id.org/sssom/NegatedPredicate` [individual, tier 2] Negating the mapping predicate. The meaning of the triple becomes subject_id is not a predicate_id match to object_id.
- bm25+lead 18.14 `https://w3id.org/sssom/predicate_modifier` [property, tier 2] A modifier for negating the predicate. See https://github.com/mapping-commons/sssom/issues/40 for discussion
- bm25 16.69 `http://www.w3.org/2004/02/skos/core#mappingRelation` [property, tier 1] Relates two concepts coming, by convention, from different schemes, and that have comparable meanings
- bm25 15.82 `http://www.w3.org/2004/02/skos/core#relatedMatch` [property, tier 1] skos:relatedMatch is used to state an associative mapping link between two conceptual resources in different concept schemes.
- bm25 15.82 `http://www.w3.org/2004/02/skos/core#narrowMatch` [property, tier 1] skos:narrowMatch is used to state a hierarchical mapping link between two conceptual resources in different concept schemes.
- bm25 15.82 `http://www.w3.org/2004/02/skos/core#broadMatch` [property, tier 1] skos:broadMatch is used to state a hierarchical mapping link between two conceptual resources in different concept schemes.
- bm25 15.71 `https://w3id.org/semapv/vocab/Mapping` [class, tier 2] A triple <s,p,o> comprising a subject entity s, an object entity o and a mapping predicate p.
- bm25 13.71 `https://w3id.org/sssom/object_match_field` [property, tier 2] A list of properties, annotations or attributes related to the object that was used to establish the match. This property is recommended for use in conjunction 
- bm25 13.71 `https://w3id.org/sssom/subject_match_field` [property, tier 2] A list of properties, annotations or attributes related to the subject that was used to establish the match. This property is recommended for use in conjunction
- bm25 13.56 `https://w3id.org/sssom/predicate_type` [property, tier 2] The type of the predicate used to map the subject and object entities.
- bm25 12.84 `https://w3id.org/semapv/vocab/MappingInversion` [class, tier 2] A matching process based on the inverting or flipping of the subject with the object of a mapping in accordance with the semantics of the mapping predicate.
- bm25 11.86 `https://w3id.org/sssom/match_string` [property, tier 2] String that is shared by subj/obj. It is recommended to indicate the fields for the match using the object and subject_match_field slots.
- bm25 11.71 `https://w3id.org/semapv/vocab/isomorphicMatch` [property, tier 2] A match where the subject is isomorphic to the object, i.e. considered of identical or similar form, shape, or structure.
- lead 8.48 `http://www.w3.org/2004/02/skos/core#closeMatch` [property, tier 1] skos:closeMatch is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications. In 
- lead 9.12 `http://www.w3.org/2004/02/skos/core#exactMatch` [property, tier 1] skos:exactMatch is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of inform

## 46. oht:confidence (P)

issuer_asserted, high, medium, low - categorical confidence in a mapping

- bm25 22.48 `https://w3id.org/sssom/mapping_set_confidence` [property, tier 2] Mapping-set level confidence is assigned by the creator of the mapping set to indicate their overall confidence in the correctness (i.e., precision) of mappings
- bm25 22.08 `https://w3id.org/sssom/registry_confidence` [property, tier 2] This value is set by the creator/maintainer of the mapping registry and reflects the confidence the mapping registry has in the correctness (i.e., precision) of
- bm25+lead 22.0 `https://w3id.org/sssom/confidence` [property, tier 2] A value assigned by the creator of the mapping to denote the creator's confidence or estimated probability that the mapping record is correct. A value of 1.0 me
- bm25+lead 19.73 `https://w3id.org/sssom/mapping_provider` [property, tier 2] URL pointing to the source that provided the mapping, for example an ontology that already contains the mappings, or a database from which it was derived.
- bm25 17.16 `http://purl.org/dc/terms/created` [property, tier 2] The date the mapping was asserted. This is different from the date the mapping was published or compiled in a SSSOM file.
- bm25 15.88 `http://purl.org/dc/terms/issued` [property, tier 2, DCAT-AP optional/other] The date the mapping was published. This is different from the date the mapping was asserted.
- bm25 15.53 `https://w3id.org/sssom/reviewer_agreement` [property, tier 2] A value assigned by the reviewer of the mapping to denote their confidence that the mapping record is correct. A value of 1.0 means the reviewer fully agrees wi
- bm25 13.88 `https://w3id.org/sssom/review_date` [property, tier 2] The date the mapping was reviewed. This is different from the date the mapping was asserted and published. If this field is used in a mapping, reviewer_id and/o
- bm25 13.8 `http://purl.org/dc/terms/medium` [property, tier 1] The material or physical carrier of the resource.
- bm25 13.64 `https://w3id.org/sssom/mapping set reference` [class, tier 2] A reference to a mapping set. It allows to augment mapping set metadata from the perspective of the registry, for example, providing confidence, or a local file
- bm25 13.06 `http://www.w3.org/ns/odrl/2/assigner` [property, tier 1] The Party is the issuer of the Rule.
- bm25 12.55 `https://w3id.org/dpv/risk#CustomerConfidenceLoss` [class, tier 2] Concept representing Customer Confidence Loss
- bm25 12.1 `https://w3id.org/dpv/risk#RM7x7S3L5` [class, tier 2] Node in a 7x7 Risk Matrix with Risk Severity: Low; Likelihood: High; and Risk Level: High
- bm25 11.98 `https://w3id.org/dpv/risk#RM7x7S5L2` [class, tier 2] Node in a 7x7 Risk Matrix with Risk Severity: High; Likelihood: Very Low; and Risk Level: Low
- bm25 11.98 `https://w3id.org/dpv/risk#RM7x7S2L5` [class, tier 2] Node in a 7x7 Risk Matrix with Risk Severity: Very Low; Likelihood: High; and Risk Level: Low

## 47. oht:score (P)

numeric confidence 0 to 1

- bm25+lead 25.92 `https://w3id.org/sssom/similarity_score` [property, tier 2] A score between 0 and 1 to denote the similarity between two entities, where 1 denotes equivalence, and 0 denotes disjointness. The score is meant to be used in
- bm25 20.25 `https://w3id.org/sssom/similarity_measure` [property, tier 2] The measure used for computing a similarity score. This field is meant to be used in conjunction with the similarity_score field, to document, for example, the 
- bm25 18.55 `https://w3id.org/semapv/vocab/SimilarityMeasure` [class, tier 2] A technique for determining a score that characterises the similarity between two entities.
- bm25 15.23 `https://w3id.org/semapv/vocab/SemanticSimilarityThresholdMatching` [class, tier 2] A matching process based on a minimum threshold of a score from a comparison based on a semantic similarity algorithm.
- bm25 15.08 `https://w3id.org/semapv/vocab/LexicalSimilarityThresholdMatching` [class, tier 2] A lexical matching process based on a minimum threshold of a score from a comparison based on a lexical similarity algorithm.
- bm25 14.23 `https://w3id.org/sssom/registry_confidence` [property, tier 2] This value is set by the creator/maintainer of the mapping registry and reflects the confidence the mapping registry has in the correctness (i.e., precision) of
- bm25+lead 14.05 `https://w3id.org/sssom/confidence` [property, tier 2] A value assigned by the creator of the mapping to denote the creator's confidence or estimated probability that the mapping record is correct. A value of 1.0 me
- bm25 13.81 `https://w3id.org/sssom/mapping_set_confidence` [property, tier 2] Mapping-set level confidence is assigned by the creator of the mapping set to indicate their overall confidence in the correctness (i.e., precision) of mappings
- bm25 13.33 `https://schema.org/bioChemSimilarity` [property, tier 2, RO-Crate] A similar BioChemEntity, e.g., obtained by fingerprint similarity algorithms.
- bm25 13.13 `http://www.w3.org/2006/time#numericPosition` [property, tier 1] The (numeric) value indicating position within a temporal coordinate system
- bm25 12.55 `https://w3id.org/dpv/risk#CustomerConfidenceLoss` [class, tier 2] Concept representing Customer Confidence Loss
- bm25 12.36 `http://www.w3.org/2006/time#numericDuration` [property, tier 1] Value of a temporal extent expressed as a decimal number scaled by a temporal unit
- bm25 12.04 `https://w3id.org/vair#DeterminingCreditScore` [class, tier 3] Determining credit score of a person
- bm25 11.86 `https://w3id.org/semapv/vocab/nGramSimilarity` [class, tier 2] 
- bm25 11.86 `https://w3id.org/semapv/vocab/SubstringSimilarity` [class, tier 2] 

## 48. oht:method (P)

how a record or crosswalk was produced

- bm25+lead 25.57 `https://w3id.org/sssom/mapping_justification` [property, tier 2] A mapping justification is an action (or the written representation of that action) of showing a mapping to be right or reasonable.
- bm25+lead 18.5 `https://w3id.org/semapv/vocab/ManualMappingCuration` [class, tier 2] A matching process that is performed by a human agent and is based on human judgement and domain knowledge.
- bm25 18.09 `https://w3id.org/sssom/curation_rule_text` [property, tier 2] A curation rule is a (potentially) complex condition executed by an agent that led to the establishment of a mapping. Curation rules often involve complex domai
- bm25 18.0 `https://w3id.org/sssom/curation_rule` [property, tier 2] A curation rule is a (potentially) complex condition executed by an agent that led to the establishment of a mapping. Curation rules often involve complex domai
- bm25+lead 16.86 `http://www.w3.org/ns/prov#wasGeneratedBy` [property, tier 1, DCAT-AP optional/other] [definition of prov:Generation] Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becom
- bm25 16.23 `https://w3id.org/dpv#hasJustification` [property, tier 2] Indicates a justification for specified concept or context
- bm25 15.85 `http://www.w3.org/ns/prov#generatedAtTime` [property, tier 1] The time at which an entity was completely created and is available for use.
- bm25 15.74 `https://w3id.org/sssom/reviewer_agreement` [property, tier 2] A value assigned by the reviewer of the mapping to denote their confidence that the mapping record is correct. A value of 1.0 means the reviewer fully agrees wi
- bm25 15.65 `http://www.w3.org/ns/prov#wasDerivedFrom` [property, tier 2, RO-Crate] A mapping set or set of mapping set that was used to derive the mapping set.
- bm25 15.63 `http://purl.org/dc/terms/created` [property, tier 2] The date the mapping was asserted. This is different from the date the mapping was published or compiled in a SSSOM file.
- bm25 15.61 `https://w3id.org/semapv/vocab/MappingActivity` [class, tier 2] A process that relates to the creation, confirmation, rejection or curation of a mapping.
- bm25 15.33 `https://w3id.org/sssom/confidence` [property, tier 2] A value assigned by the creator of the mapping to denote the creator's confidence or estimated probability that the mapping record is correct. A value of 1.0 me
- bm25 14.81 `https://w3id.org/sssom/record_id` [property, tier 2] A unique identifier for a mapping record, that is for an instance of the Mapping class (in the SSSOM/TSV serialisation, this corresponds to an individual row af
- bm25 14.11 `http://purl.org/dc/terms/issued` [property, tier 2, DCAT-AP optional/other] The date the mapping was published. This is different from the date the mapping was asserted.
- bm25 13.95 `http://purl.obolibrary.org/obo/IAO_0000114` [property, tier 2] 

## 49. oht:derivationMethod (D)

how an item relates to its source: authored, verbatim, transcribed, paraphrased, translated, converted, inferred, llm_drafted, mixed

- bm25 33.68 `http://purl.org/ontology/bibo/translationOf` [property, tier 2] Relates a translated document to the original document.
- bm25 24.05 `https://schema.org/translationOfWork` [property, tier 2, RO-Crate] The work that this work has been translated from. E.g. 物种起源 is a translationOf “On the Origin of Species”.
- bm25 23.47 `https://schema.org/digitalSourceType` [property, tier 2] Indicates an IPTCDigitalSourceEnumeration code indicating the nature of the digital source(s) for some [[CreativeWork]].
- bm25 23.39 `http://www.w3.org/ns/prov#wasRevisionOf` [property, tier 1] A revision is a derivation that revises an entity into a revised version.
- bm25 22.8 `http://data.europa.eu/eli/ontology#has_translation` [property, tier 2] Inverse of "is_translation_of". Indicates that this expression has been translated into another derived expression. See the definition of "is_translation_of".
- bm25+lead 20.2 `http://www.w3.org/ns/prov#Revision` [class, tier 1] A revision is a derivation for which the resulting entity is a revised version of some original. The implication here is that the resulting entity contains subs
- bm25+lead 18.06 `http://www.w3.org/ns/prov#Quotation` [class, tier 1] A quotation is the repeat of (some or all of) an entity, such as text or image, by someone who may or may not be its original author. Quotation is a particular 
- bm25 16.56 `http://data.europa.eu/eli/ontology#is_translation_of` [property, tier 2] Indicates that this expression has been translated from another original expression; this can be used to distinguish original from derived expressions. Note tha
- bm25 16.52 `http://usefulinc.com/ns/doap#revision` [property, tier 2] Revision identifier of a software release.
- bm25 16.32 `https://schema.org/DigitalCaptureDigitalSource` [individual, tier 2] Content coded as '<a href="https://cv.iptc.org/newscodes/digitalsourcetype/digitalCapture">digital capture</a></a>' using the IPTC <a href="https://cv.iptc.org/
- bm25 16.32 `https://schema.org/DigitalArtDigitalSource` [individual, tier 2] Content coded as '<a href="https://cv.iptc.org/newscodes/digitalsourcetype/digitalArt">digital art</a>' using the IPTC <a href="https://cv.iptc.org/newscodes/di
- bm25 15.56 `https://schema.org/PrintDigitalSource` [individual, tier 2] Content coded as '<a href="https://cv.iptc.org/newscodes/digitalsourcetype/print">print</a>' using the IPTC <a href="https://cv.iptc.org/newscodes/digitalsource
- bm25 15.43 `http://www.w3.org/ns/adms#translation` [property, tier 2] Links Assets that are translations of each other.
- bm25 15.32 `https://schema.org/CompositeDigitalSource` [individual, tier 2] Content coded as '<a href="https://cv.iptc.org/newscodes/digitalsourcetype/algorithmicMedia">algorithmic media</a>' using the IPTC <a href="https://cv.iptc.org/
- bm25 15.15 `http://www.w3.org/ns/prov#qualifiedRevision` [property, tier 1] If this Entity prov:wasRevisionOf Entity :e, then it can qualify how it was revised using prov:qualifiedRevision [ a prov:Revision; prov:entity :e; :foo :bar ].
- lead 7.46 `http://www.w3.org/ns/prov#PrimarySource` [class, tier 1] A primary source for a topic refers to something produced by some agent with direct experience and knowledge about the topic, at the time of the topic's study, 
- lead 4.11 `http://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia` [individual, tier 2] Digital media created algorithmically using an Artificial Intelligence model trained on captured content

## 50. oht:reviewed (M)

a person has checked this item against its source

- bm25 22.3 `https://schema.org/itemReviewed` [property, tier 2, RO-Crate] The item that is being reviewed/rated.
- bm25 14.12 `https://schema.org/itemDefectReturnLabelSource` [property, tier 2, RO-Crate] The method (from an enumeration) by which the customer obtains a return shipping label for a defect product.
- bm25 14.03 `http://purl.org/ontology/bibo/reviewOf` [property, tier 2] Relates a review document to a reviewed thing (resource, item, etc.).
- bm25 13.78 `https://schema.org/reviewedBy` [property, tier 2, RO-Crate] People or organizations that have reviewed the content on this web page for accuracy and/or completeness.
- bm25 13.56 `https://schema.org/claimReviewed` [property, tier 2, RO-Crate] A short summary of the specific claims reviewed in a ClaimReview.
- bm25 13.56 `http://purl.org/spar/cito/isReviewedBy` [property, tier 2] A relation according to which the cited entity presents statements, ideas or conclusions that are reviewed by the citing entity.
- bm25 13.56 `https://w3id.org/dpv/risk#hasThreatSource` [property, tier 2] Indicates the threat (subject) has the indicated source (object)
- bm25 13.46 `https://w3id.org/dpv/risk#hasRiskSource` [property, tier 2] Indicates the risk (subject) has the indicated risk source (object)
- bm25 13.42 `https://w3id.org/dpv#hasDataSource` [property, tier 2] Indicates the source or origin of data being processed
- bm25 13.36 `https://schema.org/lastReviewed` [property, tier 2, RO-Crate] Date on which the content on this web page was last reviewed for accuracy and/or completeness.
- bm25 13.1 `https://schema.org/hasMenuItem` [property, tier 2, RO-Crate] A food or drink item contained in a menu or menu section.
- bm25 13.05 `https://schema.org/reviewAspect` [property, tier 2, RO-Crate] This Review or Rating is relevant to this part or facet of the itemReviewed.
- bm25 11.87 `http://www.w3.org/ns/oa#hasSource` [property, tier 1] The resource that the ResourceSelection, or its subclass SpecificResource, is refined from, or more specific than. Please note that the domain ( oa:ResourceSele
- bm25 11.46 `https://schema.org/hasPart` [property, tier 2, RO-Crate] Indicates an item or CreativeWork that is part of this item, or CreativeWork (in some sense).
- bm25 11.3 `http://purl.org/ontology/bibo/status/nonPeerReviewed` [individual, tier 2] A document that is not peer reviewed
- lead 0.0 `http://www.w3.org/ns/prov#used` [property, tier 1] A prov:Entity that was used by this prov:Activity. For example, :baking prov:used :spoon, :egg, :oven .

## 51. oht:verification (D)

verified_primary, secondary_only, unverified

- bm25 19.33 `https://w3id.org/dpv#UnverifiedData` [class, tier 2] Data that has not been verified in terms of accuracy, inconsistency, or quality
- bm25 18.36 `https://w3id.org/dpv/ai#VerificationStage` [class, tier 2] The stage in the lifecycle where the AI system is being verified to satisfy requirements and meet objectives
- bm25 16.79 `http://www.w3.org/ns/prov#hadPrimarySource` [property, tier 1] [definition of prov:PrimarySource] A primary source for a topic refers to something produced by some agent with direct experience and knowledge about the topic,
- bm25 15.55 `http://data.europa.eu/eli/ontology#basis_for` [property, tier 2] Indicates that this work or expression empowers another . Typically primary legislation is the basis for secondary legislation.
- bm25 14.26 `http://www.w3.org/ns/prov#PrimarySource` [class, tier 1] A primary source for a topic refers to something produced by some agent with direct experience and knowledge about the topic, at the time of the topic's study, 
- bm25 13.21 `https://w3id.org/dpv#VerifiedData` [class, tier 2] Data that has been verified in terms of accuracy, consistency, or quality
- bm25 12.96 `https://schema.org/secondaryPrevention` [property, tier 2, RO-Crate] A preventative therapy used to prevent reoccurrence of the medical condition after an initial episode of the condition.
- bm25 12.94 `https://schema.org/verificationFactCheckingPolicy` [property, tier 2, RO-Crate] Disclosure about verification and fact-checking processes for a [[NewsMediaOrganization]] or other fact-checking [[Organization]].
- bm25 12.45 `https://w3id.org/dpv#Verification` [class, tier 2] Purposes association with verification e.g. information, identity, integrity
- bm25 12.32 `https://w3id.org/dpv/risk#DataUnverified` [class, tier 2] Concept representing data being unverified
- bm25 12.23 `http://xmlns.com/foaf/0.1/isPrimaryTopicOf` [property, tier 2] A document that this thing is the primary topic of.
- bm25 12.13 `http://xmlns.com/foaf/0.1/primaryTopic` [property, tier 2, DCAT-AP mandatory] The primary topic of some page or document.
- bm25 12.13 `https://w3id.org/dpv/risk#RobustnessUnverified` [class, tier 2] Concepts representing risks and issues where Robustness is Unverified
- bm25 12.13 `https://w3id.org/dpv/risk#ResilienceUnverified` [class, tier 2] Concepts representing risks and issues where Resilience is Unverified
- bm25 12.13 `https://w3id.org/dpv/risk#QualityUnverified` [class, tier 2] Concepts representing risks and issues where Quality is Unverified
- lead 0.0 `http://www.w3.org/ns/dqv#QualityAnnotation` [class, tier 2] Represents quality annotations, including ratings, quality certificates or feedback that can be associated to datasets or distributions. Quality annotations mus

## 52. oht:reviewDue (D)

when the record should next be checked

- bm25 20.22 `https://schema.org/paymentDueDate` [property, tier 2, RO-Crate] The date that payment is due.
- bm25 17.85 `https://w3id.org/sssom/review_date` [property, tier 2] The date the mapping was reviewed. This is different from the date the mapping was asserted and published. If this field is used in a mapping, reviewer_id and/o
- bm25 15.94 `https://schema.org/applicationStartDate` [property, tier 2, RO-Crate] The date at which the program begins collecting applications for the next enrollment cycle.
- bm25 14.65 `http://www.w3.org/ns/adms#next` [property, tier 2] A link to the next version of the Asset.
- bm25 14.37 `http://rdf-vocabulary.ddialliance.org/xkos#next` [property, tier 2] immediate successor in the sequence
- bm25 13.55 `https://schema.org/nextItem` [property, tier 2, RO-Crate] A link to the ListItem that follows the current one.
- bm25 13.42 `https://w3id.org/sssom/reviewer_agreement` [property, tier 2] A value assigned by the reviewer of the mapping to denote their confidence that the mapping record is correct. A value of 1.0 means the reviewer fully agrees wi
- bm25 13.37 `http://www.w3.org/ns/oa#sourceDate` [property, tier 1] The timestamp at which the Source resource should be interpreted as being applicable to the Annotation.
- bm25 13.14 `https://w3id.org/sssom/confidence` [property, tier 2] A value assigned by the creator of the mapping to denote the creator's confidence or estimated probability that the mapping record is correct. A value of 1.0 me
- bm25 13.01 `https://schema.org/uploadDate` [property, tier 2, RO-Crate] Date (including time if available) when this media object was uploaded to this site.
- bm25 12.43 `http://data.europa.eu/eli/ontology#commences` [property, tier 2] Indicates that this legal resource sets another legal resource into force. Note the the date of entry into force of the other resource should be modified accord
- bm25 12.41 `https://schema.org/dateModified` [property, tier 2, RO-Crate] The date on which the CreativeWork was most recently modified or when the item's entry was modified within a DataFeed.
- bm25 12.34 `https://schema.org/auditDate` [property, tier 2] Date when a certification was last audited. See also [gs1:certificationAuditDate](https://www.gs1.org/voc/certificationAuditDate).
- bm25 12.23 `http://purl.org/pav/sourceAccessedOn` [property, tier 2] The resource is related to a source which was originally accessed or consulted on the given date as part of creating or authoring the resource. The source(s) sh
- bm25 12.17 `http://www.w3.org/ns/oa#sourceDateStart` [property, tier 1] The start timestamp of the interval over which the Source resource should be interpreted as being applicable to the Annotation.
- lead 7.77 `https://schema.org/expires` [property, tier 2, RO-Crate] Date the content expires and is no longer useful or available. For example a [[VideoObject]] or [[NewsArticle]] whose availability or relevance is time-limited,
- lead 4.22 `https://schema.org/lastReviewed` [property, tier 2, RO-Crate] Date on which the content on this web page was last reviewed for accuracy and/or completeness.

## 53. oht:inclusion (D)

why the library holds the record: core, comparator, adjacent, context

- bm25 16.25 `http://www.w3.org/ns/org#holds` [property, tier 1] Indicates a Post held by some Agent.
- bm25 13.48 `https://schema.org/executableLibraryName` [property, tier 2, RO-Crate] Library file name, e.g., mscorlib.dll, system.web.dll.
- bm25 13.1 `http://rdf-vocabulary.ddialliance.org/xkos#coreContentNote` [property, tier 2] 
- bm25 12.87 `http://purl.obolibrary.org/obo/IAO_0000231` [property, tier 2] Relates an annotation property to an obsolescence reason. The values of obsolescence reasons come from a list of predefined terms, instances of the class obsole
- bm25 12.66 `https://schema.org/Library` [class, tier 2, RO-Crate] A library.
- bm25 12.23 `https://w3id.org/dpv#hasRule` [property, tier 2] Specifies applicability or inclusion of a rule within specified context
- bm25 11.99 `https://w3id.org/vair#Library` [class, tier 3] A collection of pre-written code
- bm25 11.95 `https://w3id.org/dpv#hasRecommendation` [property, tier 2] Specifies applicability or inclusion of a recommendation rule within specified context
- bm25 11.95 `https://w3id.org/dpv#hasProhibition` [property, tier 2] Specifies applicability or inclusion of a prohibition rule within specified context
- bm25 11.95 `https://w3id.org/dpv#hasPermission` [property, tier 2] Specifies applicability or inclusion of a permission rule within specified context
- bm25 11.95 `https://w3id.org/dpv#hasObligation` [property, tier 2] Specifies applicability or inclusion of an obligation rule within specified context
- bm25 11.95 `https://w3id.org/dpv#hasDeterrence` [property, tier 2] Specifies applicability or inclusion of a deterrence rule within specified context
- bm25 11.67 `https://schema.org/LibrarySystem` [class, tier 2, RO-Crate] A [[LibrarySystem]] is a collaborative system amongst several libraries.
- bm25 11.48 `http://www.w3.org/ns/oa#Motivation` [class, tier 1] The Motivation class is used to record the user's intent or motivation for the creation of the Annotation, or the inclusion of the body or target, that it is as
- bm25 11.45 `http://www.w3.org/ns/org#heldBy` [property, tier 1] Indicates an Agent which holds a Post.
- lead 0.0 `http://www.w3.org/2004/02/skos/core#editorialNote` [property, tier 1] A note for an editor, translator or maintainer of the vocabulary.

## 54. oht:humanReview (M)

summary on the record of the review status in its bundle

- bm25 15.51 `http://www.w3.org/ns/prov#asInBundle` [property, tier 1] prov:asInBundle is used to specify which bundle the general entity of a prov:mentionOf property is described. When :x prov:mentionOf :y and :y is described in B
- bm25 14.1 `https://schema.org/claimReviewed` [property, tier 2, RO-Crate] A short summary of the specific claims reviewed in a ClaimReview.
- bm25 13.79 `https://schema.org/accessibilitySummary` [property, tier 2, RO-Crate] A human-readable summary of specific accessibility features or deficiencies, consistent with the other accessibility metadata but expressing subtleties such as 
- bm25 13.54 `http://www.w3.org/ns/prov#mentionOf` [property, tier 1] prov:mentionOf is used to specialize an entity as described in another bundle. It is to be used in conjuction with prov:asInBundle. prov:asInBundle is used to c
- bm25 12.65 `http://www.w3.org/ns/prov#Bundle` [class, tier 1] A bundle is a named set of provenance descriptions, and is itself an Entity, so allowing provenance of provenance to be expressed.
- bm25 12.47 `https://w3id.org/dpv#ContractUnderReview` [class, tier 2] Status representing contract is under review and is being considered for signing
- bm25 12.09 `https://schema.org/review` [property, tier 2, RO-Crate] A review of the item.
- bm25 11.83 `http://rdf-vocabulary.ddialliance.org/discovery#summaryStatisticsType` [property, tier 3] This property points to the summary statistics type of a Questionnaire which is a skos:Concept.
- bm25 11.7 `https://schema.org/associatedReview` [property, tier 2, RO-Crate] An associated [[Review]].
- bm25 11.6 `https://schema.org/reviewBody` [property, tier 2, RO-Crate] The actual body of the review.
- bm25 11.56 `https://schema.org/benefitsSummaryUrl` [property, tier 2, RO-Crate] The URL that goes directly to the summary of benefits and coverage for the specific standard plan or plan variation.
- bm25 11.51 `http://purl.org/ontology/bibo/reviewOf` [property, tier 2] Relates a review document to a reviewed thing (resource, item, etc.).
- bm25 11.37 `http://www.w3.org/ns/dcat#record` [property, tier 1, DCAT-AP optional/other] A record describing the registration of a single dataset or data service that is part of the catalog.
- bm25 11.24 `https://schema.org/reviewAspect` [property, tier 2, RO-Crate] This Review or Rating is relevant to this part or facet of the itemReviewed.
- bm25 11.24 `https://schema.org/resultReview` [property, tier 2, RO-Crate] A sub property of result. The review that resulted in the performing of the action.
- lead 0.0 `http://purl.org/dc/terms/type` [property, tier 1, DCAT-AP optional/other] The nature or genre of the resource.

## 55. oht:hasOpenQuestion (P)

attaches an open question to a record

- bm25+lead 23.51 `http://www.w3.org/ns/oa#hasTarget` [property, tier 1] The relationship between an Annotation and its Target.
- bm25 17.1 `https://schema.org/eduQuestionType` [property, tier 2, RO-Crate] For questions that are part of learning resources (e.g. Quiz), eduQuestionType indicates the format of question being given. Example: "Multiple choice", "Open e
- bm25 16.84 `http://www.w3.org/2002/07/owl#annotatedTarget` [property, tier 1] The property that determines the object of an annotated axiom or annotated annotation.
- bm25 16.39 `https://w3id.org/dpv#hasRecordOfActivity` [property, tier 2] Indicates a relevant record of activity
- bm25 15.66 `http://www.w3.org/ns/oa#Motivation` [class, tier 1] The Motivation class is used to record the user's intent or motivation for the creation of the Annotation, or the inclusion of the body or target, that it is as
- bm25 13.92 `http://www.w3.org/ns/dqv#hasQualityAnnotation` [property, tier 2] Refers to a quality annotation. Quality annotation can be applied to any kind of resource, e.g., a dataset, a linkset, a graph, a set of triples. However, in th
- bm25 13.3 `http://www.w3.org/ns/odrl/2/hasPolicy` [property, tier 1, DCAT-AP optional/other] Identifies an ODRL Policy for which the identified Asset is the target Asset to all the Rules.
- bm25 12.92 `https://schema.org/question` [property, tier 2, RO-Crate] A sub property of object. A question.
- bm25 12.83 `http://purl.obolibrary.org/obo/IAO_0000596` [property, tier 2] Relates an ontology used to record id policy to the number of digits in the URI. The URI is: the 'has ID prefix" annotation property value concatenated with an 
- bm25 12.51 `http://www.w3.org/ns/oa#hasPurpose` [property, tier 1] The purpose served by the resource in the Annotation.
- bm25 12.33 `http://www.w3.org/ns/oa#questioning` [individual, tier 1] The motivation for when the user intends to ask a question about the Target.
- bm25 12.29 `http://www.w3.org/ns/oa#hasBody` [property, tier 1] The object of the relationship is a resource that is a body of the Annotation.
- bm25 12.18 `http://rdf-vocabulary.ddialliance.org/discovery#question` [property, tier 3] This property indicates the Questions associated to Variables or contained in Questionnaires.
- bm25 12.07 `http://www.w3.org/ns/oa#hasScope` [property, tier 1] The scope or context in which the resource is used within the Annotation.
- bm25 12.03 `http://rdf-vocabulary.ddialliance.org/discovery#questionText` [property, tier 3] This property contains the actual text of a question as string. See Section 8.2 for examples.

## 56. oht:resolution (M)

how an open question was resolved

- bm25+lead 22.06 `http://www.w3.org/2004/02/skos/core#historyNote` [property, tier 1] A note about the past state/use/meaning of a concept.
- bm25 17.1 `https://schema.org/eduQuestionType` [property, tier 2, RO-Crate] For questions that are part of learning resources (e.g. Quiz), eduQuestionType indicates the format of question being given. Example: "Multiple choice", "Open e
- bm25 16.93 `https://schema.org/ReplyAction` [class, tier 2, RO-Crate] The act of responding to a question/message asked/sent by the object. Related to [[AskAction]].\n\nRelated actions:\n\n* [[AskAction]]: Appears generally as an 
- bm25 15.98 `https://schema.org/replyToUrl` [property, tier 2, RO-Crate] The URL at which a reply may be posted to the specified UserComment.
- bm25 15.86 `http://purl.org/spar/cito/hasReplyFrom` [property, tier 2] A relation according to which the cited entity evokes a reply from the citing entity.
- bm25 14.7 `http://www.w3.org/ns/dcat#temporalResolution` [property, tier 1, DCAT-AP optional/other] minimum time period resolvable in a dataset.
- bm25 13.9 `http://www.w3.org/ns/dcat#spatialResolutionInMeters` [property, tier 1, DCAT-AP optional/other] minimum spatial separation resolvable in a dataset, measured in metres.
- bm25 12.99 `http://purl.org/skos-history/isVersionHistoryOf` [property, tier 3] Links the version history set to the skos concept scheme it is about. (Preliminary, may be better located in dsv ontology.)
- bm25 12.92 `http://www.w3.org/ns/odrl/2/resolution` [individual, tier 1] Resolution of the rendition of the target Asset.
- bm25 12.92 `https://schema.org/question` [property, tier 2, RO-Crate] A sub property of object. A question.
- bm25 12.47 `http://purl.org/skos-history/concepthistory` [property, tier 3] Collects the concept deltas of a concept (given in the subject of the triple).
- bm25 12.18 `http://rdf-vocabulary.ddialliance.org/discovery#question` [property, tier 3] This property indicates the Questions associated to Variables or contained in Questionnaires.
- bm25 12.09 `https://schema.org/AskAction` [class, tier 2, RO-Crate] The act of posing a question / favor to someone.\n\nRelated actions:\n\n* [[ReplyAction]]: Appears generally as a response to AskAction.
- bm25 12.03 `http://rdf-vocabulary.ddialliance.org/discovery#questionText` [property, tier 3] This property contains the actual text of a question as string. See Section 8.2 for examples.
- bm25 12.02 `https://w3id.org/dpv/risk#resolves` [property, tier 2] Indicates the specified event or action is resolved by this control
- lead 7.98 `http://www.w3.org/ns/oa#replying` [individual, tier 1] The motivation for when the user intends to reply to a previous statement, either an Annotation or another resource.
- lead 0.0 `http://purl.org/dc/terms/description` [property, tier 1, DCAT-AP mandatory, DCAT-AP optional/other] An account of the resource.

## 57. oht:release (P)

the library release label in which a record state was published

- bm25 30.59 `https://schema.org/recordLabel` [property, tier 2, RO-Crate] The label that issued the release.
- bm25 18.78 `https://schema.org/releaseNotes` [property, tier 2, RO-Crate] Description of what changed in this version.
- bm25 15.98 `http://usefulinc.com/ns/doap#Version` [class, tier 2] Version information of a project release.
- bm25 15.26 `https://schema.org/datePublished` [property, tier 2, RO-Crate] Date of first publication or broadcast. For example the date a [[CreativeWork]] was broadcast or a [[Certification]] was issued.
- bm25 14.91 `http://www.w3.org/ns/oa#TimeState` [class, tier 1] A TimeState records the time at which the resource's state is appropriate for the Annotation, typically the time that the Annotation was created and/or a link t
- bm25 14.85 `https://w3id.org/sssom/review_date` [property, tier 2] The date the mapping was reviewed. This is different from the date the mapping was asserted and published. If this field is used in a mapping, reviewer_id and/o
- bm25 14.79 `http://purl.org/skos-history/deltaFrom` [property, tier 3] The version from which the delta is taken. The object of the triple may be a dsv:VersionHistoryRecord.
- bm25 13.97 `http://purl.org/skos-history/hasDelta` [property, tier 3] A delta for this version. The subject of the triple may be a dsv:VersionHistoryRecord.
- bm25 13.57 `http://www.w3.org/ns/prov#wasRevisionOf` [property, tier 1] A revision is a derivation that revises an entity into a revised version.
- bm25 13.48 `https://schema.org/executableLibraryName` [property, tier 2, RO-Crate] Library file name, e.g., mscorlib.dll, system.web.dll.
- bm25 13.47 `https://schema.org/sdDatePublished` [property, tier 2, RO-Crate] Indicates the date on which the current structured data was generated / published. Typically used alongside [[sdPublisher]].
- bm25 13.3 `https://w3id.org/airo#Version` [class, tier 3] A unique number or name that is assigned to a unique state of an AI system.
- bm25 13.3 `http://usefulinc.com/ns/doap#release` [property, tier 2] A project release.
- bm25 13.3 `https://schema.org/releaseOf` [property, tier 2, RO-Crate] The album this is a release of.
- bm25 12.87 `https://schema.org/albumRelease` [property, tier 2, RO-Crate] A release of this album.
- lead 8.53 `http://www.w3.org/ns/dcat#version` [property, tier 1, DCAT-AP optional/other] The version indicator (name or identifier) of a resource.
- lead 7.76 `http://purl.org/pav/version` [property, tier 2] The version number of a resource. This is a freetext string, typical values are "1.5" or "21". The URI identifying the previous version can be provided using pr
- lead 8.0 `http://www.w3.org/2002/07/owl#versionInfo` [property, tier 1] The annotation property that provides version information for an ontology or another OWL construct.

## 58. oht:redistributable (P)

whether the archived copy may be republished

- bm25+lead 21.78 `http://purl.org/dc/terms/accessRights` [property, tier 1, DCAT-AP optional/other] Information about who access the resource or an indication of its security status.
- bm25 20.35 `https://schema.org/archivedAt` [property, tier 2, RO-Crate] Indicates a page or other link involved in archival of a [[CreativeWork]]. In the case of [[MediaReview]], the items in a [[MediaReviewItem]] may often become i
- bm25+lead 14.97 `http://purl.org/dc/terms/license` [property, tier 2, DCAT-AP optional/other] A url to the license of the mapping. In absence of a license we assume no license.
- bm25 14.46 `https://schema.org/license` [property, tier 2, RO-Crate] A license document that applies to this content, typically indicated by URL.
- bm25 14.23 `http://usefulinc.com/ns/doap#license` [property, tier 2] The URI of an RDF description of the license the software is distributed under. E.g. a SPDX reference
- bm25 13.9 `https://schema.org/sdLicense` [property, tier 2, RO-Crate] A license document that applies to this structured data, typically indicated by URL.
- bm25 13.83 `https://w3id.org/airo#hasLicense` [property, tier 3] Indicates licenses associated with a resource.
- bm25+lead 13.83 `http://purl.org/dc/terms/license` [property, tier 1, DCAT-AP optional/other] A legal document giving official permission to do something with the resource.
- bm25 13.64 `https://w3id.org/dpv#DigitalRightsManagement` [class, tier 2] Management of access, use, and other operations associated with digital content
- bm25 13.11 `http://purl.org/dc/terms/RightsStatement` [class, tier 1] A statement about the intellectual property rights (IPR) held in or over a resource, a legal document giving official permission to do something with a resource
- bm25 12.62 `https://schema.org/acquireLicensePage` [property, tier 2, RO-Crate] Indicates a page documenting how licenses can be purchased or otherwise acquired, for the current item.
- bm25 12.6 `https://w3id.org/dpv#UsageControl` [class, tier 2] Management of usage, which is intended to be broader than access control and may cover trust, digital rights, or other relevant controls
- bm25 12.45 `https://w3id.org/airo#License` [class, tier 3] Represents a copyright license.
- bm25 12.26 `https://w3id.org/dpv#ServiceAccessDetermination` [class, tier 2] Purposes associated with the determination of whether specific conditions or criteria are met for accessing, using, or gaining access to a service
- bm25 12.14 `https://w3id.org/dpv#Copy` [class, tier 2] to produce an exact reproduction of the data
- lead 0.0 `http://www.w3.org/ns/odrl/2/distribute` [individual, tier 1] To supply the Asset to third-parties.

## 59. oht:redactions (M)

for a published derived copy, what was removed and kept

- bm25+lead 28.67 `http://purl.org/dc/terms/provenance` [property, tier 1, DCAT-AP optional/other] A statement of any changes in ownership and custody of the resource since its creation that are significant for its authenticity, integrity, and interpretation.
- bm25 26.65 `http://purl.org/dc/terms/ProvenanceStatement` [class, tier 1] Any changes in ownership and custody of a resource since its creation that are significant for its authenticity, integrity, and interpretation.
- bm25 22.05 `http://www.w3.org/ns/prov#derivedByRemovalFrom` [property, tier 1] The dictionary was derived from the other by removal. prov:qualifiedRemoval shows details of the removal, in particular the removed key-entity pairs.
- bm25 17.74 `http://www.w3.org/ns/prov#qualifiedRemoval` [property, tier 1] The dictionary was derived from the other by removal. prov:qualifiedRemoval shows details of the removal, in particular the removed keys.
- bm25 17.2 `http://www.w3.org/ns/prov#wasDerivedFrom` [property, tier 1, RO-Crate] A derivation is a transformation of an entity into another, an update of an entity resulting in a new one, or the construction of a new entity based on a pre-ex
- bm25 15.51 `http://www.w3.org/ns/prov#removedKey` [property, tier 1] The key removed in a Removal.
- bm25 15.36 `https://w3id.org/dpv#DataRedaction` [class, tier 2] Removal of sensitive information from a data or document
- bm25 15.26 `https://schema.org/datePublished` [property, tier 2, RO-Crate] Date of first publication or broadcast. For example the date a [[CreativeWork]] was broadcast or a [[Certification]] was issued.
- bm25 14.62 `http://www.w3.org/ns/prov#derivedByInsertionFrom` [property, tier 1] The dictionary was derived from the other by insertion. prov:qualifiedInsertion shows details of the insertion, in particular the inserted key-entity pairs.
- bm25 14.32 `http://www.w3.org/ns/prov#wasQuotedFrom` [property, tier 1] An entity is derived from an original entity by copying, or 'quoting', some or all of it.
- bm25 14.16 `https://schema.org/dateDeleted` [property, tier 2, RO-Crate] The datetime the item was removed from the DataFeed.
- bm25 13.85 `http://www.w3.org/ns/prov#provenanceUriTemplate` [property, tier 1] Relates a provenance service to a URI template string for constructing provenance-URIs.
- bm25 13.76 `http://www.w3.org/ns/prov#has_provenance` [property, tier 1] Indicates a provenance-URI for a resource; the resource identified by this property presents a provenance record about its subject or anchor resource.
- bm25 13.58 `http://www.w3.org/ns/prov#pingback` [property, tier 1] Relates a resource to a provenance pingback service that may receive additional provenance links about the resource.
- bm25 13.47 `https://schema.org/sdDatePublished` [property, tier 2, RO-Crate] Indicates the date on which the current structured data was generated / published. Typically used alongside [[sdPublisher]].

## 60. oht:hasHumanReview (M)

attaches the review to a record

- bm25 16.39 `https://w3id.org/dpv#hasRecordOfActivity` [property, tier 2] Indicates a relevant record of activity
- bm25+lead 12.09 `https://schema.org/review` [property, tier 2, RO-Crate] A review of the item.
- bm25 11.7 `https://schema.org/associatedReview` [property, tier 2, RO-Crate] An associated [[Review]].
- bm25 11.64 `http://purl.org/skos-history/hasDelta` [property, tier 3] A delta for this version. The subject of the triple may be a dsv:VersionHistoryRecord.
- bm25 11.6 `https://schema.org/reviewBody` [property, tier 2, RO-Crate] The actual body of the review.
- bm25 11.51 `http://purl.org/ontology/bibo/reviewOf` [property, tier 2] Relates a review document to a reviewed thing (resource, item, etc.).
- bm25 11.37 `http://www.w3.org/ns/dcat#record` [property, tier 1, DCAT-AP optional/other] A record describing the registration of a single dataset or data service that is part of the catalog.
- bm25 11.24 `https://schema.org/reviewAspect` [property, tier 2, RO-Crate] This Review or Rating is relevant to this part or facet of the itemReviewed.
- bm25 11.24 `https://schema.org/resultReview` [property, tier 2, RO-Crate] A sub property of result. The review that resulted in the performing of the action.
- bm25 11.16 `https://schema.org/recordLabel` [property, tier 2, RO-Crate] The label that issued the release.
- bm25 11.12 `https://schema.org/reviewRating` [property, tier 2, RO-Crate] The rating given in this review. Note that reviews can themselves be rated. The ```reviewRating``` applies to rating given by the review. The [[aggregateRating]
- bm25 11.1 `https://schema.org/reviewCount` [property, tier 2, RO-Crate] The count of total number of reviews.
- bm25 10.77 `http://www.w3.org/ns/prov#has_provenance` [property, tier 1] Indicates a provenance-URI for a resource; the resource identified by this property presents a provenance record about its subject or anchor resource.
- bm25 10.38 `http://purl.obolibrary.org/obo/IAO_0000598` [property, tier 2] Relating an ontology used to record id policy to the ontology namespace whose policy it manages
- bm25 10.26 `https://schema.org/associatedMediaReview` [property, tier 2, RO-Crate] An associated [[MediaReview]], related by specific common content, topic or claim. The expectation is that this property would be most typically used in cases w
- lead 0.0 `http://www.w3.org/ns/prov#used` [property, tier 1] A prov:Entity that was used by this prov:Activity. For example, :baking prov:used :spoon, :egg, :oven .

## 61. oht:reviewStatus (M)

none, sampled, full, on the review

- bm25 14.88 `http://www.w3.org/ns/odrl/2/isNoneOf` [individual, tier 1] A set-based operator indicating that a given value is none of the right operand of the Constraint.
- bm25 12.67 `https://schema.org/employmentType` [property, tier 2, RO-Crate] Type of employment (e.g. full-time, part-time, contract, temporary, seasonal, internship).
- bm25 12.47 `https://w3id.org/dpv#ContractUnderReview` [class, tier 2] Status representing contract is under review and is being considered for signing
- bm25 12.44 `https://schema.org/OnlineFull` [individual, tier 2, RO-Crate] Game server status: OnlineFull. Server is online but unavailable. The maximum number of players has reached.
- bm25 12.09 `https://schema.org/review` [property, tier 2, RO-Crate] A review of the item.
- bm25 11.7 `https://schema.org/associatedReview` [property, tier 2, RO-Crate] An associated [[Review]].
- bm25 11.65 `https://schema.org/gameAvailabilityType` [property, tier 2, RO-Crate] Indicates the availability type of the game content associated with this action, such as whether it is a full version or a demo.
- bm25 11.64 `https://schema.org/ActionStatusType` [class, tier 2, RO-Crate] The status of an Action.
- bm25 11.6 `https://schema.org/reviewBody` [property, tier 2, RO-Crate] The actual body of the review.
- bm25 11.51 `http://purl.org/ontology/bibo/reviewOf` [property, tier 2] Relates a review document to a reviewed thing (resource, item, etc.).
- bm25 11.5 `https://schema.org/codeSampleType` [property, tier 2, RO-Crate] What type of code sample: full (compile ready) solution, code snippet, inline code, scripts, template.
- bm25 11.44 `https://schema.org/ReservationStatusType` [class, tier 2, RO-Crate] Enumerated status values for Reservation.
- bm25 11.24 `https://schema.org/reviewAspect` [property, tier 2, RO-Crate] This Review or Rating is relevant to this part or facet of the itemReviewed.
- bm25 11.24 `https://schema.org/resultReview` [property, tier 2, RO-Crate] A sub property of result. The review that resulted in the performing of the action.
- bm25 11.2 `https://schema.org/numberOfFullBathrooms` [property, tier 2, RO-Crate] Number of full bathrooms - The total number of full and ¾ bathrooms in an [[Accommodation]]. This corresponds to the [BathroomsFull field in RESO](https://ddwik
- lead 5.5 `http://purl.org/dc/terms/type` [property, tier 1, DCAT-AP optional/other] The nature or genre of the resource.

## 62. oht:toolPath (M)

where a tool lives in the repository

- bm25+lead 24.39 `https://schema.org/codeRepository` [property, tier 2, RO-Crate] Link to the repository where the un-compiled, human readable code and related code is located (SVN, GitHub, CodePlex).
- bm25 23.2 `http://usefulinc.com/ns/doap#location` [property, tier 2] Location of a repository.
- bm25+lead 20.6 `http://usefulinc.com/ns/doap#repository` [property, tier 2] Source code repository.
- bm25 17.16 `http://usefulinc.com/ns/doap#Repository` [class, tier 2] Source code repository.
- bm25 16.03 `http://usefulinc.com/ns/doap#HgRepository` [class, tier 2] Mercurial source code repository.
- bm25 16.03 `http://usefulinc.com/ns/doap#GitRepository` [class, tier 2] Git source code repository.
- bm25 16.03 `http://usefulinc.com/ns/doap#DarcsRepository` [class, tier 2] darcs source code repository.
- bm25 15.85 `http://usefulinc.com/ns/doap#SVNRepository` [class, tier 2] Subversion source code repository.
- bm25 15.85 `http://usefulinc.com/ns/doap#CVSRepository` [class, tier 2] CVS source code repository.
- bm25 15.25 `http://usefulinc.com/ns/doap#ArchRepository` [class, tier 2] GNU Arch source code repository.
- bm25 15.06 `https://schema.org/location` [property, tier 2, RO-Crate] The location of, for example, where an event is happening, where an organization is located, or where an action takes place.
- bm25 14.99 `http://usefulinc.com/ns/doap#BKRepository` [class, tier 2] BitKeeper source code repository.
- bm25 14.33 `http://usefulinc.com/ns/doap#repositoryOf` [property, tier 2] The project that uses a repository.
- bm25 14.19 `https://schema.org/Residence` [class, tier 2, RO-Crate] The place where a person lives.
- bm25 13.6 `http://www.w3.org/ns/duv#hasUsageTool` [property, tier 2] Describes the tool that provides the Usage
- lead 0.0 `http://purl.org/dc/terms/identifier` [property, tier 1, DCAT-AP optional/other] An unambiguous reference to the resource within a given context.

## 63. oht:commit (M)

the git commit of a run or change

- bm25+lead 23.68 `http://usefulinc.com/ns/doap#revision` [property, tier 2] Revision identifier of a software release.
- bm25 15.61 `http://www.w3.org/ns/prov#wasRevisionOf` [property, tier 1] A revision is a derivation that revises an entity into a revised version.
- bm25 15.15 `http://www.w3.org/ns/prov#qualifiedRevision` [property, tier 1] If this Entity prov:wasRevisionOf Entity :e, then it can qualify how it was revised using prov:qualifiedRevision [ a prov:Revision; prov:entity :e; :foo :bar ].
- bm25 14.48 `http://usefulinc.com/ns/doap#GitRepository` [class, tier 2] Git source code repository.
- bm25 14.48 `http://usefulinc.com/ns/doap#GitBranch` [class, tier 2] Git source code branch.
- bm25 13.57 `https://schema.org/specialCommitments` [property, tier 2, RO-Crate] Any special commitments associated with this job posting. Valid entries include VeteranCommit, MilitarySpouseCommit, etc.
- bm25 13.37 `http://www.w3.org/ns/prov#hadRevision` [untyped, tier 1] 
- bm25 12.62 `http://www.w3.org/ns/prov#Revision` [class, tier 1] A revision is a derivation for which the resulting entity is a revised version of some original. The implication here is that the resulting entity contains subs
- bm25 11.85 `http://www.w3.org/ns/mls#executes` [property, tier 2] A relation between a run and an implemantation that is being executed during the run.
- bm25 11.67 `http://www.w3.org/2004/02/skos/core#changeNote` [property, tier 1] A note about a modification to a concept.
- bm25 11.46 `http://www.w3.org/ns/mls#realizes` [property, tier 2] A relation between a run and an algorithm, where the run realizes specifications formulated by the algorithm.
- bm25 11.46 `http://www.w3.org/ns/mls#achieves` [property, tier 2] A relation between a run and a task, where the run achieves specifications formulated by the task.
- bm25 10.74 `http://www.w3.org/ns/mls#hasInput` [property, tier 2] A relation between a run and data that is taken as input to the run.
- bm25 10.49 `http://www.w3.org/ns/adms#identifier` [property, tier 2, DCAT-AP optional/other] Links a resource to an adms:Identifier class.
- bm25 10.46 `https://w3id.org/airo#hasPreDeterminedChange` [property, tier 3] Indicates the changes that are planned to be applied to the system, components, or context of use.
- lead 8.39 `http://purl.org/dc/terms/identifier` [property, tier 1, DCAT-AP optional/other] An unambiguous reference to the resource within a given context.

## 64. oht:session (P)

links a model agent to its session

- bm25 13.92 `https://w3id.org/dpv/ai#hasModel` [property, tier 2] Indicates the use of an AI model for the associated context
- bm25 13.01 `https://w3id.org/dpv/ai#hasGPAIModel` [property, tier 2] Indicates the use of an GPAI model for the associated context
- bm25 11.61 `https://w3id.org/dpv/ai#ModelRisk` [class, tier 2] Risks associated with AI Models
- bm25+lead 11.46 `http://www.w3.org/ns/prov#wasAssociatedWith` [property, tier 1] An prov:Agent that had some (unspecified) responsibility for the occurrence of this prov:Activity.
- bm25 11.21 `http://purl.org/spar/cito/linksTo` [property, tier 2] A relation according to which the citing entity provides a link, in the form of an HTTP Uniform Resource Locator (URL), to the cited entity.
- bm25 11.19 `https://schema.org/publishedBy` [property, tier 2, RO-Crate] An agent associated with the publication event.
- bm25 9.68 `https://schema.org/modelDate` [property, tier 2, RO-Crate] The release date of a vehicle model (often used to differentiate versions of the same make and model).
- bm25 9.65 `https://w3id.org/airo#hasDocumentation` [property, tier 3] Indicates documentation associated with an entity, e.g. AI model, AI system.
- bm25 9.63 `http://purl.org/ontology/bibo/Hearing` [class, tier 2] An instance or a session in which testimony and arguments are presented, esp. before an official, as a judge in a lawsuit.
- bm25 9.47 `https://schema.org/model` [property, tier 2, RO-Crate] The model of the product. Use with the URL of a ProductModel or a textual representation of the model identifier. The URL of the ProductModel can be from an ext
- bm25 9.45 `https://schema.org/programmingModel` [property, tier 2, RO-Crate] Indicates whether API is managed or unmanaged.
- bm25 9.43 `https://schema.org/vehicleModelDate` [property, tier 2, RO-Crate] The release date of a vehicle model (often used to differentiate versions of the same make and model).
- bm25 9.41 `http://www.w3.org/ns/prov#agent` [property, tier 1] 
- bm25 9.27 `https://w3id.org/airo#hasModel` [property, tier 3] Indicates machine learning models used with a system or component.
- bm25 8.86 `https://schema.org/infectiousAgent` [property, tier 2, RO-Crate] The actual infectious agent, such as a specific bacterium.

## 65. oht:archiveStatus (M)

not_archived, private, public

- bm25+lead 26.42 `http://purl.org/dc/terms/accessRights` [property, tier 1, DCAT-AP optional/other] Information about who access the resource or an indication of its security status.
- bm25 20.63 `https://w3id.org/dpv#PrivateSpace` [class, tier 2] A space that is owned or controlled by a private entity and where access to members of the public is restricted
- bm25 18.98 `https://schema.org/publicAccess` [property, tier 2, RO-Crate] A flag to signal that the [[Place]] is open to public visitors. If this property is omitted there is no assumed default boolean value.
- bm25 17.87 `https://w3id.org/dpv#HybridPublicPrivateSpace` [class, tier 2] A space that is a hybrid space i.e it has both public and private components - such as by having part of it be a private space or which is operated privately
- bm25 17.71 `https://w3id.org/dpv#PrivateCommunalSpace` [class, tier 2] A space that is accessible to a group or a community within a private space and where members of the public do not have access to it e.g. society amenities such
- bm25 17.27 `https://schema.org/conditionsOfAccess` [property, tier 2, RO-Crate] Conditions that affect the availability of, or method(s) of access to, an item. Typically used for real world items such as an [[ArchiveComponent]] held by an [
- bm25 16.13 `https://schema.org/ArchiveOrganization` [class, tier 2, RO-Crate] An organization with archival holdings. An organization which keeps and preserves archival material and typically makes it accessible to the public.
- bm25 15.86 `https://schema.org/archivedAt` [property, tier 2, RO-Crate] Indicates a page or other link involved in archival of a [[CreativeWork]]. In the case of [[MediaReview]], the items in a [[MediaReviewItem]] may often become i
- bm25 15.74 `https://schema.org/holdingArchive` [property, tier 2, RO-Crate] [[ArchiveOrganization]] that holds, keeps or maintains the [[ArchiveComponent]].
- bm25 15.69 `https://w3id.org/dpv#PrivateLocation` [class, tier 2] Location that is not or cannot be accessed by the public and is controlled as a private space
- bm25 15.16 `https://w3id.org/vair#EvaluatingEligibilityToAccessPublicAssistanceServices` [individual, tier 3] 
- bm25 14.5 `https://schema.org/archiveHeld` [property, tier 2, RO-Crate] Collection, [fonds](https://en.wikipedia.org/wiki/Fonds), or item held, kept or maintained by an [[ArchiveOrganization]].
- bm25 14.29 `https://w3id.org/dpv#PublicInterestStatus` [class, tier 2] Status associated with use of Public Interest as a legal basis
- bm25 13.64 `https://w3id.org/dpv#DigitalRightsManagement` [class, tier 2] Management of access, use, and other operations associated with digital content
- bm25 13.11 `http://purl.org/dc/terms/RightsStatement` [class, tier 1] A statement about the intellectual property rights (IPR) held in or over a resource, a legal document giving official permission to do something with a resource

## 66. oht:transcript (P)

the archived full transcript of a session

- bm25 17.24 `https://schema.org/transcript` [property, tier 2, RO-Crate] If this MediaObject is an AudioObject or VideoObject, the transcript of that object.
- bm25 15.86 `https://schema.org/archivedAt` [property, tier 2, RO-Crate] Indicates a page or other link involved in archival of a [[CreativeWork]]. In the case of [[MediaReview]], the items in a [[MediaReviewItem]] may often become i
- bm25+lead 12.29 `http://www.w3.org/ns/prov#generated` [property, tier 1] 
- bm25 11.2 `https://schema.org/numberOfFullBathrooms` [property, tier 2, RO-Crate] Number of full bathrooms - The total number of full and ¾ bathrooms in an [[Accommodation]]. This corresponds to the [BathroomsFull field in RESO](https://ddwik
- bm25 11.02 `http://www.w3.org/ns/prov#generatedAtTime` [property, tier 1] The time at which an entity was completely created and is available for use.
- bm25 9.91 `http://www.w3.org/ns/prov#wasGeneratedBy` [property, tier 1, DCAT-AP optional/other] [definition of prov:Generation] Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becom
- bm25 9.83 `http://www.w3.org/ns/prov#generatedAsDerivation` [untyped, tier 1] 
- bm25 9.65 `https://w3id.org/dpv#NoticeGenerated` [class, tier 2] Status indicating the notice has been generated
- bm25 9.63 `http://purl.org/ontology/bibo/Hearing` [class, tier 2] An instance or a session in which testimony and arguments are presented, esp. before an official, as a judge in a lawsuit.
- bm25 9.54 `https://schema.org/FullGameAvailability` [individual, tier 2, RO-Crate] Indicates full game availability.
- bm25 9.47 `https://schema.org/FullRefund` [individual, tier 2, RO-Crate] Specifies that a refund can be done in the full amount the customer paid for the product.
- bm25 9.14 `https://w3id.org/dpv#GeneratedData` [class, tier 2] Data that is generated or brought into existence without relation to existing data i.e. it is not derived or inferred from other data
- bm25 9.12 `https://schema.org/OnlineFull` [individual, tier 2, RO-Crate] Game server status: OnlineFull. Server is online but unavailable. The maximum number of players has reached.
- bm25 8.98 `https://w3id.org/vair#FullAutomation` [class, tier 3] The level of automation where is capable of performing its entire mission without external intervention.
- bm25 8.81 `https://w3id.org/dpv#GeneratedPersonalData` [class, tier 2] Personal Data that is generated or brought into existence without relation to existing data i.e. it is not derived or inferred from other data

## 67. oht:excerpt (P)

the published redacted excerpt of a transcript

- bm25 17.24 `https://schema.org/transcript` [property, tier 2, RO-Crate] If this MediaObject is an AudioObject or VideoObject, the transcript of that object.
- bm25 15.99 `http://purl.org/spar/cito/includesExcerptFrom` [property, tier 2] A relation according to which the citing entity includes one or more excerpts from the cited entity.
- bm25 15.97 `http://purl.org/spar/cito/providesExcerptFor` [property, tier 2] A relation according to which the cited entity contains information, usually of a textual nature, that is excerpted by (used as an excerpt within) the citing en
- bm25 14.53 `http://purl.org/ontology/bibo/Excerpt` [class, tier 2] A passage selected from a larger work.
- bm25 10.64 `http://www.w3.org/ns/prov#derivedByRemovalFrom` [property, tier 1] The dictionary was derived from the other by removal. prov:qualifiedRemoval shows details of the removal, in particular the removed key-entity pairs.
- bm25 10.64 `http://www.w3.org/ns/prov#derivedByInsertionFrom` [property, tier 1] The dictionary was derived from the other by insertion. prov:qualifiedInsertion shows details of the insertion, in particular the inserted key-entity pairs.
- bm25 10.59 `https://schema.org/publishedBy` [property, tier 2, RO-Crate] An agent associated with the publication event.
- bm25 10.49 `https://schema.org/publishedOn` [property, tier 2, RO-Crate] A broadcast service associated with the publication event.
- bm25+lead 10.08 `http://www.w3.org/ns/prov#wasDerivedFrom` [property, tier 1, RO-Crate] A derivation is a transformation of an entity into another, an update of an entity resulting in a new one, or the construction of a new entity based on a pre-ex
- bm25 9.7 `http://data.europa.eu/eli/ontology#published_in` [property, tier 2] Reference to the Official Journal or other publication manifestation in which this format is published. This property should be used when the value cannot be id
- bm25 9.56 `https://schema.org/sdDatePublished` [property, tier 2, RO-Crate] Indicates the date on which the current structured data was generated / published. Typically used alongside [[sdPublisher]].
- bm25 9.41 `http://data.europa.eu/eli/ontology#published_in_format` [property, tier 2] Reference to the Official Journal or other publication manifestation in which this format is published. This property should be used when the value can be ident
- bm25 9.37 `https://schema.org/datePublished` [property, tier 2, RO-Crate] Date of first publication or broadcast. For example the date a [[CreativeWork]] was broadcast or a [[Certification]] was issued.
- bm25 9.27 `https://w3id.org/dpv#DerivedPersonalData` [class, tier 2] Personal Data that is obtained or derived from other data
- bm25 9.24 `http://purl.org/ontology/bibo/status/published` [individual, tier 2] Published document
- lead 0.0 `http://www.w3.org/ns/prov#generated` [property, tier 1] 
- lead 6.42 `http://purl.org/dc/terms/hasPart` [property, tier 1, DCAT-AP optional/other] A related resource that is included either physically or logically in the described resource.

## 68. oht:locator (P)

where in the transcript the agent's work is

- bm25+lead 20.38 `http://purl.org/ontology/bibo/locator` [property, tier 2] A description (often numeric) that locates an item within a containing document or collection.
- bm25 18.73 `https://schema.org/locationCreated` [property, tier 2, RO-Crate] The location where the CreativeWork was created, which may not be the same as the location depicted in the CreativeWork.
- bm25 17.51 `https://schema.org/workLocation` [property, tier 2, RO-Crate] A contact location for a person's place of work.
- bm25 17.24 `https://schema.org/transcript` [property, tier 2, RO-Crate] If this MediaObject is an AudioObject or VideoObject, the transcript of that object.
- bm25 15.06 `https://schema.org/location` [property, tier 2, RO-Crate] The location of, for example, where an event is happening, where an organization is located, or where an action takes place.
- bm25 15.0 `https://schema.org/toLocation` [property, tier 2, RO-Crate] A sub property of location. The final location of the object or the agent after the action.
- bm25 15.0 `https://schema.org/fromLocation` [property, tier 2, RO-Crate] A sub property of location. The original location of the object or the agent before the action.
- bm25 14.87 `http://purl.obolibrary.org/obo/IAO_0000639` [class, tier 2] A part of a document about work in other publications that is relevant to the content of the document.
- bm25 14.85 `https://schema.org/recordedAt` [property, tier 2, RO-Crate] The Event where the CreativeWork was recorded. The CreativeWork may capture all or part of the event.
- bm25 14.79 `https://schema.org/isPartOf` [property, tier 2, RO-Crate] Indicates an item or CreativeWork that this item, or CreativeWork (in some sense), is part of.
- bm25 14.26 `https://schema.org/applicantLocationRequirements` [property, tier 2, RO-Crate] The location(s) applicants can apply from. This is usually used for telecommuting jobs where the applicant does not need to be in a physical office. Note: This 
- bm25 14.15 `https://schema.org/hasPart` [property, tier 2, RO-Crate] Indicates an item or CreativeWork that is part of this item, or CreativeWork (in some sense).
- bm25 14.13 `https://schema.org/gameLocation` [property, tier 2, RO-Crate] Real or fictional location of the game (or part of game).
- bm25 13.23 `http://purl.obolibrary.org/obo/IAO_0000314` [class, tier 2] An information content entity that is part of a document.
- bm25 13.16 `https://schema.org/foundingLocation` [property, tier 2, RO-Crate] The place where the Organization was founded.

