from pathlib import Path
import json,hashlib
B=Path(__file__).resolve().parents[1];base=B/'raw/provisional/My_Summons_Go_First_CH4_Panels43-55_Complete_Artwork_Handoff';d=json.loads((base/'panel_manifest.json').read_text())
mouth390={43:{'NIB':[171,142],'TAEO':[246,40]},44:{'TAEO':[273,32],'COWORKER':[120,52]},45:{'COWORKER':[139,70],'TAEO':[267,55]},46:{'COWORKER':[145,72],'TAEO':[90,37]},47:{'TAEO':[273,40],'NIB':[198,165]},48:{'COWORKER':[154,69]},49:{'COWORKER':[315,74]},50:{'NIB':[145,151],'TAEO':[278,43]},52:{'TAEO':[167,85]},53:{'COWORKER':[318,71],'NIB':[130,184]},54:{'TAEO':[316,34],'NIB':[143,146]}}
out=[]
for p in d['panels']:
 n=p['panel'];src=base/p['native_original'];assert hashlib.sha256(src.read_bytes()).hexdigest()==p['native_original_sha256'];x,y,x2,y2=p['crop_rect_xyxy'];sc=(x2-x)/390
 prot=[[a+x,b+y,c+x,e+y] for a,b,c,e in p.get('protected_face_rects_xyxy',[])+p.get('protected_prop_rects_xyxy',[])]
 mouths={name:[xx*sc+x,yy*sc+y] for name,(xx,yy) in mouth390.get(n,{}).items()}
 out.append({'panel_id':n,'source_image':str(src.relative_to(B)),'source_sha256':p['native_original_sha256'],'crop_xyxy':[x,y,x2,y2],'protected_boxes':prot,'mouths':mouths,'negative_space_boxes':[],'independent_review':'pending','mouth_coordinate_note':'Assembler inspected390px; source mouth anchor from scaled preview. Verify after lettering.','artist_manifest':str((base/'panel_manifest.json').relative_to(B))})
(B/'source/manifest_43_55.json').write_text(json.dumps({'panels':out,'status':'provisional; independent review pending; panel51 missing art text'},indent=2))
print('13 provisional shop panels imported. No acceptance recorded.')
