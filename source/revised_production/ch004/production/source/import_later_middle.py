from pathlib import Path
import json,hashlib
B=Path(__file__).resolve().parents[1];base=B/'raw/provisional/Chapter4_Panels29_42_Selected_Art_Handoff';originals=B/'raw/provisional/Chapter4_Panels29_42_Originals_Prompts_Audit';out=[]
for p in json.loads((base/'panel_manifest.json').read_text())['panels']:
 n=p['panel']
 if n<35:continue
 src=originals/p['original'];assert hashlib.sha256(src.read_bytes()).hexdigest()==p['sha256'];x,y,x2,y2=p['crop_xyxy'];pc=p['protection_coordinates'];rs=pc.get('faces_xyxy',[])+pc.get('hands_xyxy',[])+pc.get('prop_xyxy',[]);prot=[[a+x,b+y,c+x,e+y] for a,b,c,e in rs]
 names={36:['NIB','TAEO'],37:['CHAE','TAEO'],38:['TAEO','NIB'],39:['NIB'],40:['TAEO','CHAE','NIB'],41:['TAEO','CHAE','NIB'],42:['TAEO','NIB']}.get(n,[])
 mouths={k:[(r[0]+r[2])/2+x,(r[1]+r[3])/2+y] for k,r in zip(names,pc.get('mouths_xyxy',[]))}
 if n==35:mouths['NIB']=[100,400]
 if n==38:mouths['CHAE']=[1470,300]
 if n==39:mouths['CHAE']=[280,390]
 out.append({'panel_id':n,'source_image':str(src.relative_to(B)),'source_sha256':p['sha256'],'crop_xyxy':p['crop_xyxy'],'protected_boxes':prot,'mouths':mouths,'negative_space_boxes':[],'independent_review':'pending','artist_manifest':str((base/'panel_manifest.json').relative_to(B))})
(B/'source/manifest_35_42.json').write_text(json.dumps({'panels':out,'status':'provisional pending independent review'},indent=2))
