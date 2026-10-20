from pathlib import Path
import json,hashlib
from PIL import Image,ImageChops
B=Path(__file__).resolve().parents[1];a=B/'raw/Chapter6_Panels15_28_Selected_Artwork';cp=B/'source/received_candidates.json';c=json.loads(cp.read_text());checks=[]
for p in json.loads((a/'panel_manifest.json').read_text())['panels']:
 n=p['panel'];root=B/'raw'/('Chapter6_Panels15_21_Native_Originals_Audit' if n<=21 else 'Chapter6_Panels22_28_Native_Originals_Audit');src=root/p['original'];h=hashlib.sha256(src.read_bytes()).hexdigest();assert h==p['native_sha256'];cut=Image.open(src).convert('RGB').crop(p['crop_xyxy']);out=Image.open(a/p['file']).convert('RGB');assert cut.size==out.size and ImageChops.difference(cut,out).getbbox() is None
 checks.append({'panel':n,'source':str(src.relative_to(B)),'sha256':h,'crop':p['crop_xyxy'],'exact_selected_pixels':True,'selected':p['selected']})
 if str(n) in c['panels']:
  assert c['panels'][str(n)]['source_sha256']==h and c['panels'][str(n)]['crop']==p['crop_xyxy'];continue
 sc=800/cut.width;c['panels'][str(n)]={'source':str(src.relative_to(B)),'source_sha256':h,'crop':p['crop_xyxy'],'extension':[0,0],'protected_boxes':[[x*sc,y*sc,(xx-x)*sc,(yy-y)*sc] for k,bs in p['protection_coordinates'].items() if k!='mouths_xyxy' for x,y,xx,yy in bs],'protected_polygons':[],'protection_reviewed':False,'status':'received_pending_independent_raw_QA','items':{},'producer_protection_hints_only':True}
cp.write_text(json.dumps(c,indent=2));(B/'qa/middle_incoming_pixel_integrity.json').write_text(json.dumps({'checks':checks,'independent_visual_approval':False},indent=2));print('26 candidate units staged; accepted crop mapping preserved.')
