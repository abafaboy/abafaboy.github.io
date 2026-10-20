from pathlib import Path
import json,hashlib
B=Path(__file__).resolve().parents[1];ev='qa/independent_p14_v5_review.md';assert (B/ev).is_file(),'Await independent P14 raw review'
c=json.loads((B/'source/layout_config.json').read_text());src='repairs/P14_v5_native/raw/p14_v5.png';sha=hashlib.sha256((B/src).read_bytes()).hexdigest();assert sha=='9827b4b02264354c250264a1bc7e4d4379f038c394a710b1fd666a298d306746';crop=[0,0,1024,1536]
c['panels']['14']=dict(source=src,source_sha256=sha,crop=crop,extension=[0,0],protected_boxes=[[0,0,800,1200]],protected_polygons=[],protection_reviewed=True,items={},art_provenance='Native imagegen full-frame v5 cart-handle repair; surrounding pixels resampled and independently re-reviewed, not byte-unchanged from v4.')
rp=B/'qa/independent_raw_review.json';r=json.loads(rp.read_text());rec=dict(panels=[14],sha256=sha,crop_xyxy=crop,verdict='pass',evidence=ev)
if rec not in r['reviews']:r['reviews'].append(rec)
(B/'source/layout_config.json').write_text(json.dumps(c,indent=2));rp.write_text(json.dumps(r,indent=2))
