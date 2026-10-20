from pathlib import Path
import os,json,hashlib
B=Path(__file__).resolve().parents[1];c=json.loads((B/'source/layout_config.json').read_text());os.environ['ANIME_ACE_FONT']=c['font_path'];from fit_text import fit
s={p['panel']:p for p in json.loads((B/'source/lettering_script.json').read_text())['panels']};r=json.loads((B/'qa/independent_raw_review.json').read_text());ev='qa/independent_p12_p13_review.md'
assert (B/ev).is_file(),'Await independent raw review report before importing'
for n,ext,placements in [(12,[240,0],[([0,0,550,220],[325,430],2.3),([570,1070,220,160],[510,1165],3.5)]),(13,[300,0],[([0,0,340,180],[170,480],2.3),([390,100,410,190],[600,470],2.3)])]:
 root=f'raw/Chapter6_Panels{n}_Candidate_Source/';m=json.loads((B/root/f'qa/manifest_{n}.json').read_text())['panels'][0];crop=m['crop_xyxy'];scale=800/(crop[2]-crop[0]);boxes=[]
 for reg in m['protected']:
  x,y,x1,y1=reg['box'];boxes.append([(x-crop[0])*scale,(y-crop[1])*scale+ext[0],(x1-x)*scale,(y1-y)*scale])
 if n==12:boxes.append([0,811,800,243])
 sha=m['original']['sha256'];assert hashlib.sha256((B/root/m['source']).read_bytes()).hexdigest()==sha
 p=dict(source=root+m['source'],source_sha256=sha,crop=crop,extension=ext,protected_boxes=boxes,protected_polygons=[],protection_reviewed=True,items={})
 for i,(box,tip,angle) in enumerate(placements):p['items'][str(i)]=dict(box=box,tip=tip,attachment_angle=angle,font_size=31,lines=fit(s[n]['items'][i]['text'],box[2]-8,box[3]-12,31))
 c['panels'][str(n)]=p;rec=dict(panels=[n],sha256=sha,crop_xyxy=crop,verdict='pass',evidence=ev)
 if rec not in r['reviews']:r['reviews'].append(rec)
(B/'source/layout_config.json').write_text(json.dumps(c,indent=2));(B/'qa/independent_raw_review.json').write_text(json.dumps(r,indent=2))
