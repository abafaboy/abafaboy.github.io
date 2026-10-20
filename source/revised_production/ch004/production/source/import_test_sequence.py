from pathlib import Path
import json,hashlib
B=Path(__file__).resolve().parents[1];base=B/'raw/provisional/MSGF_Ch04_Panels15-28_Final_Artwork_Handoff';d=json.loads((B/'raw/provisional/manifest_FINAL_15-28.json').read_text());out=[];cf=B/'source/layout_config.json';cfg=json.loads(cf.read_text())
for p in d['panels']:
 n=p['panel'];src=base/p['accepted_original'];assert hashlib.sha256(src.read_bytes()).hexdigest()==p['source_sha256'];x,y,x2,y2=p['crop_box_xyxy'];pr=p['protection'];boxes=list(pr['faces'].values())+pr.get('critical_hands_pad',[]);boxes=[[a+x,b+y,c+x,e+y] for a,b,c,e in boxes];mouths={k.upper():[v[0]+x,v[1]+y] for k,v in p['mouth_centers_xy'].items()};safe=[[a+x,b+y,c+x,e+y] for a,b,c,e in pr.get('negative_space',[])]
 out.append({'panel_id':n,'source_image':str(src.relative_to(B)),'source_sha256':p['source_sha256'],'crop_xyxy':p['crop_box_xyxy'],'protected_boxes':boxes,'mouths':mouths,'negative_space_boxes':safe,'independent_review':'pending final-source recheck','artist_manifest':'raw/provisional/manifest_FINAL_15-28.json'});cfg['panels'].pop(str(n),None)
# Supersede initial15–18 mapping; retain original artist manifests in raw archives.
(B/'source/manifest_15_18.json').write_text(json.dumps({'panels':[],'status':'superseded by manifest_15_28.json'},indent=2));(B/'source/manifest_15_28.json').write_text(json.dumps({'panels':out,'status':'provisional independent review pending'},indent=2));cf.write_text(json.dumps(cfg,indent=2))
print('All fourteen final test candidates staged; final review gate unchanged.')
