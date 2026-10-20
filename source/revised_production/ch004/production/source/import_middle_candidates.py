from pathlib import Path
import json,hashlib
B=Path(__file__).resolve().parents[1];out=[]
for name,manifest in [('Chapter4_Panels29_31_FirstUsableBatch','panel_manifest.json'),('Chapter4_Panels30_32_33_34_UsableBatch','batch_B_manifest.json')]:
 base=B/'raw/provisional'/name
 for p in json.loads((base/manifest).read_text())['panels']:
  src=base/p['original'];assert hashlib.sha256(src.read_bytes()).hexdigest()==p['sha256'];x,y,x2,y2=p['crop_xyxy'];prot=p['protection_coordinates'];rs=prot.get('faces_xyxy',[])+prot.get('hands_xyxy',[])+prot.get('prop_xyxy',[]);rs=[[a+x,b+y,c+x,e+y] for a,b,c,e in rs]
  names={29:['TAEO','CHAE'],31:['NIB','CHAE'],33:['TAEO','NIB'],34:['CHAE','NIB']}.get(p['panel'],[])
  mouths={k:[(r[0]+r[2])/2+x,(r[1]+r[3])/2+y] for k,r in zip(names,prot.get('mouths_xyxy',[]))}
  out.append({'panel_id':p['panel'],'source_image':str(src.relative_to(B)),'source_sha256':p['sha256'],'crop_xyxy':p['crop_xyxy'],'protected_boxes':rs,'mouths':mouths,'negative_space_boxes':[],'independent_review':'pending','artist_manifest':str((base/manifest).relative_to(B))})
(B/'source/manifest_29_34.json').write_text(json.dumps({'panels':out,'status':'provisional pending independent acceptance'},indent=2))
