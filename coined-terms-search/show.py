import json,sys
S=json.load(open("results/shortlists.json"))
a,b=int(sys.argv[1]),int(sys.argv[2])
for t in S:
    if not a<=t["item"]<=b: continue
    print(f"## {t['item']} {t['term']}: {t['definition']}")
    for c in [c for c in t["candidates"] if c["found_by"]!="bm25"]+[c for c in t["candidates"] if c["found_by"]=="bm25"][:10]:
        pn=c["iri"].replace("http://www.w3.org/ns/","").replace("http://purl.org/dc/terms/","dcterms:").replace("https://schema.org/","schema:").replace("http://www.w3.org/2004/02/skos/core#","skos:").replace("http://rdf-vocabulary.ddialliance.org/","").replace("https://w3id.org/","")
        if c["prefix"] in ("vair","dpv","risk","ai","airo") and c["found_by"]=="bm25" and c["score"]<99 and "--all" not in sys.argv: 
            if not any(k in c["definition"].lower() for k in sys.argv[3:4]): pass
        print(f"  {c['found_by'][:4]} {pn} [{c['kind'][0]}{c['tier']}{' '+','.join(p.replace('DCAT-AP ','AP-') for p in c['profiles']) if c['profiles'] else ''}{' DEP' if c['deprecated'] else ''}] {c['definition'][:85]}")
