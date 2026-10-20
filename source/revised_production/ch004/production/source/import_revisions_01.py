from pathlib import Path
import json,hashlib
B=Path('new_summoner_reset/ch004/production');cfgfile=B/'source/layout_config.json';cfg=json.loads(cfgfile.read_text())
#14 only
base=B/'raw/provisional/My_Summons_Go_First_Ch4_Panel_14_Pad_Repair';p=json.loads((base/'panel14_repair_manifest.json').read_text())['panels'][0];p['source_image']=str((base/p['source_image']).relative_to(B));assert hashlib.sha256((B/p['source_image']).read_bytes()).hexdigest()==p['source_sha256'];f=B/'source/manifest_01_14_new.json';d=json.loads(f.read_text());d['panels']=[p if r['panel_id']==14 else r for r in d['panels']];f.write_text(json.dumps(d,indent=2));cfg['panels'].pop('14',None)
#15-18
base=B/'raw/provisional/MSGF_Ch04_Panels15-18_QA_Revision';d=json.loads((base/'manifest_15-18_revised.json').read_text());out=[]
for p in d['panels']:
 src=base/p['panel_file'];assert hashlib.sha256(src.read_bytes()).hexdigest()==p['sha256'];out.append({'panel_id':p['panel'],'source_image':str(src.relative_to(B)),'source_sha256':p['sha256'],'crop_xyxy':p['crop_box_xyxy'],'protected_boxes':list(p['protection']['faces'].values()),'mouths':{k.upper():[(r[0]+r[2])/2,(r[1]+r[3])/2] for k,r in p['protection']['mouths'].items()},'negative_space_boxes':[],'independent_review':'pending revised source recheck'});cfg['panels'].pop(str(p['panel']),None)
(B/'source/manifest_15_18.json').write_text(json.dumps({'panels':out},indent=2))
#53-54
base=B/'raw/provisional/My_Summons_Go_First_CH4_Panels53-54_Continuity_Revision';rs=json.loads((base/'panels53_54_revision_manifest.json').read_text())['replacement_panels'];f=B/'source/manifest_43_55.json';d=json.loads(f.read_text())
for p in rs:
 r=next(r for r in d['panels'] if r['panel_id']==p['panel']);src=base/p['native_original'];assert hashlib.sha256(src.read_bytes()).hexdigest()==p['native_original_sha256'];x,y,x2,y2=p['crop_rect_xyxy'];r.update(source_image=str(src.relative_to(B)),source_sha256=p['native_original_sha256'],crop_xyxy=p['crop_rect_xyxy'],protected_boxes=[[a+x,b+y,c+x,e+y] for a,b,c,e in p.get('protected_face_rects_xyxy',[])+p.get('protected_prop_rects_xyxy',[])],independent_review='pending revised source recheck');cfg['panels'].pop(str(p['panel']),None)
f.write_text(json.dumps(d,indent=2));cfgfile.write_text(json.dumps(cfg,indent=2));print('7 revised candidates imported; acceptance remains pending.')
