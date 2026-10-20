from pathlib import Path
import json,os,hashlib
B=Path(__file__).resolve().parents[1];config=json.loads((B/'source/layout_config.json').read_text());os.environ['ANIME_ACE_FONT']=config['font_path'];from fit_text import fit
src='repairs/My_Summons_Go_First_CH6_P30_Repair_Candidate_QA/native/P30_repair_v4.png';h=hashlib.sha256((B/src).read_bytes()).hexdigest();assert h=='1372bfa4915bb2dbcf6f498726990796f3b3fa9cb67e896cf09c145d065acd6b';p={'source':src,'source_sha256':h,'crop':[0,0,1470,1070],'extension':[220,0],'protected_boxes':[[280,220,100,130],[55,470,235,330],[220,440,70,90],[390,450,60,100],[470,540,110,265]],'protected_polygons':[],'protection_reviewed':True,'items':{},'art_provenance':'Native full-frame v4 source; producer selected file is a whole-frame LANCZOS resize, not exact unscaled crop.'};s=json.loads((B/'source/lettering_script.json').read_text());ps={x['panel']:x for x in s['panels']}
for i,(box,tip) in enumerate([([0,0,430,200],[275,300]),([450,120,340,190],[590,570])]):p['items'][str(i)]={'box':box,'tip':tip,'font_size':31,'lines':fit(ps[30]['items'][i]['text'],box[2]-8,box[3]-12,31)}
config['panels']['30']=p;(B/'source/layout_config.json').write_text(json.dumps(config,indent=2));rp=B/'qa/independent_raw_review.json';r=json.loads(rp.read_text());rec={'panels':[30],'sha256':h,'crop_xyxy':p['crop'],'verdict':'pass','evidence':'qa/independent_p30_v4_review.md'}
if rec not in r['reviews']:r['reviews'].append(rec)
rp.write_text(json.dumps(r,indent=2))
