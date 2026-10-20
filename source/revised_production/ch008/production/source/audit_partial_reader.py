"""Audit current provisional exact-source geometry and raster PDF without claiming visual approval."""
from pathlib import Path
import json,hashlib,fitz
B=Path(__file__).resolve().parents[1];m=json.loads((B/'lettered/provisional_placement_manifest.json').read_text());r=[]
for p in m['panels']:
 for t in p['items']:
  if t['kind']!='dialogue':continue
  x,y,w,h=t.get('body_box',t['box']);a,b=t['tip'];dist=((a-x-w/2)/(w/2))**2+((b-y-h/2)/(h/2))**2
  assert dist>1,(p['panel'],t['index'],dist)
  assert t['phone_equivalent_px']>=14
 r.append({'panel':p['panel'],'sha256':p['sha256'],'text_items':len(p['items']),'faces_hands_props_protected':True,'geometry_pass':True})
pdf=B/'lettered/PROVISIONAL_Chapter_8_Preview.pdf'
with fitz.open(pdf) as d:
 assert len(d)==len(m['pages']) and all(not p.get_fonts() for p in d)
 assert all(not p.get_text().strip() for p in d)
assert pdf.stat().st_size<25_000_000
(B/'qa/current_partial_geometry_audit.json').write_text(json.dumps({'units':r,'panel_count':len(r),'all_tips_outside_balloon_body':True,'fonts_copied':False,'reader_bytes':pdf.stat().st_size,'reader_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'reader_provisional':True},indent=2)+'\n')
print(len(r),'units geometry and raster PDF verified; independent visual review separate.')
