from pathlib import Path
import json,hashlib
B=Path(__file__).resolve().parents[1]
a=B/'raw/provisional/My_Summons_Go_First_Ch4_Panels_03_06_Candidate'
b=B/'raw/provisional/MSGF_Ch04_Panels15-18_Artwork_Handoff'
one=json.loads((a/'incremental_03_06_manifest.json').read_text())
for p in one['panels']:
 p['source_image']=str((a/p['source_image']).relative_to(B));assert hashlib.sha256((B/p['source_image']).read_bytes()).hexdigest()==p['source_sha256']
(B/'source/manifest_03_06.json').write_text(json.dumps(one,indent=2))
two=json.loads((B/'raw/provisional/manifest_15-18_with_protection.json').read_text());out=[]
for p in two['panels']:
 source=b/p['panel_file'];assert hashlib.sha256(source.read_bytes()).hexdigest()==p['sha256']
 q={'panel_id':p['panel'],'source_image':str(source.relative_to(B)),'source_sha256':p['sha256'],'crop_xyxy':p['crop_box_xyxy'],'protected_boxes':list(p['protection']['faces'].values()),'mouths':{k.upper():[(r[0]+r[2])/2,(r[1]+r[3])/2] for k,r in p['protection']['mouths'].items()},'negative_space_boxes':[],'independent_review':'pending','artist_manifest':str((B/'raw/provisional/manifest_15-18_with_protection.json').relative_to(B))}
 out.append(q)
(B/'source/manifest_15_18.json').write_text(json.dumps({'panels':out,'status':'provisional pending independent acceptance'},indent=2))
print('Imported eight provisional candidates; review gate stays closed.')
