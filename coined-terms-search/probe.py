import requests, json, time, sys, hashlib
from pathlib import Path
B="https://lov.linkeddata.es/dataset/api/v2"
S=requests.Session(); S.headers["User-Agent"]="oht-coined-term-review/0.1 (manual research; low volume)"
raw=Path("probe"); 
def get(path, **p):
    k=raw/(hashlib.sha1(json.dumps([path,p],sort_keys=True).encode()).hexdigest()[:12]+".json")
    if k.exists(): return json.loads(k.read_text())
    r=S.get(B+path,params=p,timeout=30); time.sleep(1.2)
    try: d=r.json()
    except Exception: d={"_status":r.status_code,"_text":r.text[:200]}
    k.write_text(json.dumps(d,indent=1)); return d
def show(label, d, n=8):
    print(f"-- {label}: total={d.get('total_results')} filters={d.get('filters')}")
    for r in (d.get('results') or [])[:n]: print("   ", round(r.get('score',0),2), r.get('type'), r.get('prefixedName'), r.get('uri'))
if __name__=="__main__":
    for t in ["property","propery","class"]:
        show("type="+t, get("/term/search", q="version", type=t, page_size=5),3)
    show("no type", get("/term/search", q="version", page_size=5),3)
    for q in ["catalog record","record catalog","catalog","record",'"catalog record"',"catalog AND record","catalog OR record","+catalog +record","catalogue record"]:
        show(q, get("/term/search", q=q, page_size=10))
    d=get("/term/search", q="version", page_size=2)
    print(json.dumps(d["results"][0],indent=1)[:1500])
    print(json.dumps(get("/vocabulary/info", vocab="dcat"),indent=1)[:2500])
