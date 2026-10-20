from pathlib import Path
import json,hashlib
B=Path(__file__).resolve().parents[1];cf=B/'source/layout_config.json';cfg=json.loads(cf.read_text())
for name,ids in [('Chapter4_Panels29_30_31_34_35_36_QA_Repairs_R1',[29,30,31,34,35,36]),('Chapter4_Panel40_Pouch_QA_Repair_R2',[40])]:
 base=B/'raw/provisional'/name
 for p in json.loads((base/'panel_manifest.json').read_text())['panels']:
  n=p['panel']
  if n not in ids:continue
  src=base/p['original'];assert hashlib.sha256(src.read_bytes()).hexdigest()==p['sha256'];pc=p['protection_coordinates'];x,y,x2,y2=p['crop_xyxy'];rs=[r for k,v in pc.items() if k.endswith('_xyxy') and k!='mouths_xyxy' for r in v];prot=[[a+x,b+y,c+x,e+y] for a,b,c,e in rs]
  names={29:['TAEO','CHAE'],31:['NIB','CHAE'],34:['CHAE','NIB'],36:['NIB','TAEO'],40:['TAEO','CHAE','NIB']}.get(n,[]);mouths={k:[(r[0]+r[2])/2+x,(r[1]+r[3])/2+y] for k,r in zip(names,pc.get('mouths_xyxy',[]))}
  if n==30:mouths['CHAE']=[35,20]
  if n==35:mouths['NIB']=[100,400]
  r={'panel_id':n,'source_image':str(src.relative_to(B)),'source_sha256':p['sha256'],'crop_xyxy':p['crop_xyxy'],'protected_boxes':prot,'mouths':mouths,'negative_space_boxes':[],'independent_review':'pending repair recheck','artist_manifest':str((base/'panel_manifest.json').relative_to(B))}
  mf=B/('source/manifest_29_34.json' if n<35 else 'source/manifest_35_42.json');d=json.loads(mf.read_text());d['panels']=[r if old['panel_id']==n else old for old in d['panels']];mf.write_text(json.dumps(d,indent=2));cfg['panels'].pop(str(n),None)
cf.write_text(json.dumps(cfg,indent=2));print('Seven office repair candidates staged; approved sources unchanged.')
