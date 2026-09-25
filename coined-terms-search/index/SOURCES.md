# Where each vocabulary comes from

Every vocabulary is fetched from its publisher, not from LOV, so the index holds current versions and named individuals. `sources.csv` lists the URLs tried, in order; `fetch_vocabs.py` fetches with RDF content negotiation, and `build_index.py` merges everything into `terms.csv` (one row per term) and `profiles.csv` (which terms DCAT-AP and RO-Crate name). Fetched 2026-09-25. Raw files are in `cache/`.

Tier is the working guess from `context/review-so-far.md`; Phase 5 checks it against each specification's status page.

| Vocabulary | Prefix | Tier | Terms | Classes/properties/individuals | Without definition | Resolved source |
|---|---|---|---|---|---|---|
| DCAT 3 | `dcat` | 1 | 52 | 9/37/0 | 6 | https://www.w3.org/ns/dcat3.ttl |
| DCAT-AP 3.0.0 (profile) | `dcatap` | 2 | - | SHACL shapes, see `profiles.csv` | - | https://semiceu.github.io/DCAT-AP/releases/3.0.0/html/shacl/shapes.ttl |
| ADMS | `adms` | 2 | 18 | 4/14/0 | 0 | https://uri.semic.eu/w3c/ns/adms.ttl |
| SKOS | `skos` | 1 | 32 | 4/28/0 | 0 | https://www.w3.org/2009/08/skos-reference/skos.rdf |
| SKOS-XL | `skosxl` | 1 | 6 | 1/5/0 | 0 | https://www.w3.org/2009/08/skos-reference/skos-xl.rdf |
| XKOS | `xkos` | 2 | 44 | 4/40/0 | 39 | https://ddi-cv-api.ukdataarchive.co.uk/xkos |
| ISO 25964 SKOS extension | `iso-thes` | 3 | 22 | 6/16/0 | 1 | https://www.dublincore.org/specifications/skos-thes/ns/skos-thes.ttl |
| NKOS Application Profile | `nkos` | 3 | 6 | 0/6/0 | 0 | https://nkos.dublincore.org/nkos-ap.html (RDFa) |
| NKOS KOS Types | `nkostype` | 3 | 14 | 0/0/14 | 0 | https://nkos.dublincore.org/nkos-type.html (scraped HTML) |
| skos-history | `sh` | 3 | 13 | 5/8/0 | 0 | https://raw.githubusercontent.com/jneubert/skos-history/master/skos-history.ttl |
| ISO 25964 dataset versioning | `dsv` | 3 | 0 | - | - | **not available** |
| PAV | `pav` | 2 | 30 | 0/30/0 | 0 | http://pav-ontology.github.io/pav/pav.rdf |
| OBO IAO | `iao` | 2 | 286 | 210/57/19 | 30 | IAO release v2026-03-30 (iao.owl) |
| SSSOM | `sssom` | 2 | 106 | 9/75/22 | 13 | LinkML schema `sssom_schema.yaml` on GitHub (mapping-commons/sssom, master) |
| SEMAPV | `semapv` | 2 | 62 | 56/6/0 | 14 | semapv.owl on GitHub (mapping-commons/semantic-mapping-vocabulary) |
| PROV-O | `prov` | 1 | 170 | 50/83/0 | 47 | https://www.w3.org/ns/prov.ttl |
| Web Annotation | `oa` | 1 | 67 | 21/29/17 | 1 | https://www.w3.org/ns/oa.ttl |
| DQV | `dqv` | 2 | 21 | 10/9/2 | 0 | https://www.w3.org/ns/dqv.ttl |
| DUV | `duv` | 2 | 10 | 4/6/0 | 0 | https://www.w3.org/ns/duv.ttl |
| CiTO | `cito` | 2 | 110 | 9/101/0 | 0 | https://sparontologies.github.io/cito/current/cito.xml |
| BIBO | `bibo` | 2 | 140 | 59/67/14 | 22 | https://www.dublincore.org/specifications/bibo/bibo/bibo.ttl |
| DCMI Terms | `dcterms` | 1 | 98 | 34/55/9 | 0 | dublin_core_terms.ttl at dublincore.org |
| DCMI Type | `dcmitype` | 1 | 12 | 12/0/0 | 0 | dublin_core_type.ttl at dublincore.org |
| ELI | `eli` | 2 | 123 | 21/86/16 | 3 | via http://data.europa.eu/eli/ontology (Publications Office cellar) |
| ODRL | `odrl` | 1 | 231 | 26/58/147 | 25 | https://www.w3.org/ns/odrl/2/ODRL22.ttl |
| EU access-right table | `accessright` | 2 | 7 | untyped concepts | 7 | http://publications.europa.eu/resource/authority/access-right |
| SSN | `ssn` | 1 | 21 | 6/15/0 | 0 | https://www.w3.org/ns/ssn/ |
| SOSA | `sosa` | 1 | 36 | 13/23/0 | 0 | https://www.w3.org/ns/sosa/ |
| ML Schema | `mls` | 2 | 38 | 25/13/0 | 9 | https://www.w3.org/ns/mls |
| RDF Data Cube | `qb` | 1 | 36 | 15/21/0 | 0 | cube.ttl on GitHub (UKGovLD/publishing-statistical-data) |
| DDI Discovery | `disco` | 3 | 57 | 16/41/0 | 0 | https://ddi-cv-api.ukdataarchive.co.uk/discovery |
| FOAF | `foaf` | 2 | 75 | 13/62/0 | 0 | https://xmlns.com/foaf/spec/index.rdf |
| ORG | `org` | 1 | 45 | 9/35/1 | 0 | https://www.w3.org/ns/org.ttl |
| schema.org | `schema` | 2 | 3023 | 939/1538/546 | 0 | schemaorg-current-https.ttl (latest release) |
| OWL-Time | `time` | 1 | 95 | 23/58/14 | 15 | https://www.w3.org/2006/time.ttl |
| DOAP | `doap` | 2 | 56 | 13/43/0 | 0 | doap.rdf on GitHub (ewilderj/doap) |
| RO-Crate 1.2 (profile) | `rocrate` | 2 | - | JSON-LD context, see `profiles.csv` | - | https://www.researchobject.org/ro-crate/specification/1.2/context.jsonld |
| DPV core 2.3 | `dpv` | 2 | 1174 | 972/144/58 | 58 | https://w3c-cg.github.io/dpv/2.3/dpv/dpv.rdf |
| DPV RISK 2.3 | `risk` | 2 | 565 | 507/43/15 | 15 | https://w3c-cg.github.io/dpv/2.3/risk/risk.rdf |
| DPV AI 2.3 | `ai` | 2 | 257 | 231/10/16 | 16 | https://w3c-cg.github.io/dpv/2.3/ai/ai.rdf |
| IPTC Digital Source Type | `iptcdst` | 2 | 20 | 0/0/20 | 0 | https://cv.iptc.org/newscodes/digitalsourcetype/ |
| AIRO | `airo` | 3 | 98 | 46/52/0 | 0 | https://delaramglp.github.io/airo/airo.rdf |
| VAIR | `vair` | 3 | 524 | 424/0/99 | 89 | https://delaramglp.github.io/vair/vair.rdf |

Total: 7,725 terms, about 95% with a definition.

## Problems and workarounds

- **ISO 25964 dataset versioning (`dsv`) is gone.** `http://purl.org/iso25964/DataSet/Versioning` now 404s at purl.archive.org, and NISO's ISO 25964 pages don't host it. The only trace found is its description in the ZBW skos-history paper (DC-2015). It was tier 3 and relevant only to item 2, which DCAT 3 covers, so it is dropped. It can be cited but not depended on.
- **NKOS namespaces no longer dereference.** `http://w3id.org/nkos` and `.../nkostype` redirect to the NKOS workshop home page. The AP page carries RDFa (parsed with pyRdfa3: 6 properties). The KOS types page has no machine-readable data and its "RDF/XML" link points to a PDF, so the 14 types were scraped from the HTML list, with IRIs built from the documented pattern `http://w3id.org/nkos/nkostype#<label_with_underscores>`. Those IRIs are unverified by dereference. A broken namespace is also evidence for the tier 3 rating.
- **PROV-O leaves many properties without a comment** (`prov:hadPrimarySource` has only a label). Where a property names a qualified class (`prov:qualifiedForm`), the index uses that class's definition, marked `[definition of prov:PrimarySource]`. The PROV-O and PROV-DM specifications stay the authority for quotes.
- **XKOS has no comments on 39 of 44 terms.** Its definitions are in the XKOS specification text, which Phase 5 reads directly.
- **DPV's `.ttl` URLs 404**; the namespace IRIs negotiate to the 2.3 release.
- **SSSOM is LinkML YAML, not RDF.** Classes and slots come from `classes` and `slots`, and enum values from `permissible_values`. Prefixed names (CURIEs) are expanded with the schema's own prefix map, so `sssom:NoTermFound` becomes `https://w3id.org/sssom/NoTermFound`.
- **The EU access-right table file lists its seven concepts without labels or definitions.** Each concept IRI dereferences on its own (RDF/XML) with `skos:prefLabel` and `skos:definition`; the two values recommended in the report were fetched that way.
- **DCAT-AP adds no terms of its own** here; it is recorded as a profile, meaning which DCAT, DCMI and ADMS properties it makes mandatory or optional per class. RO-Crate likewise maps names onto schema.org and other terms.
