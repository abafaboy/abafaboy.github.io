from pathlib import Path
import json,os,copy
B=Path(__file__).resolve().parents[1];config=json.loads((B/'source/layout_config.json').read_text());os.environ['ANIME_ACE_FONT']=config['font_path'];from fit_text import fit
c=json.loads((B/'source/received_candidates.json').read_text());ps={p['panel']:p for p in json.loads((B/'source/lettering_script.json').read_text())['panels']};rp=B/'qa/independent_raw_review.json';reviews=json.loads(rp.read_text());settings={16:([140,0],[([0,0,250,125],[145,270])]),19:([400,0],[([440,0,350,200],[550,690]),([0,210,400,180],[300,500])]),21:([190,0],[([0,0,380,170],[105,350]),([590,30,200,130],[810,160])]),24:([0,0],[]),25:([260,280],[([0,0,790,230],[350,360]),([200,820,590,230],[670,760])]),26:([300,0],[([0,0,350,220],[30,430]),([370,50,420,240],[230,400])])}
for n,(ext,items) in settings.items():
 p=copy.deepcopy(c['panels'][str(n)]);r={'panels':[n],'sha256':p['source_sha256'],'crop_xyxy':p['crop'],'verdict':'pass','evidence':'qa/independent_middle_art_review_v1.md','scope':'Exact crop only; lettering not reviewed'}
 if r not in reviews['reviews']:reviews['reviews'].append(r)
 p['extension']=ext;p['protected_boxes']=[[x,y+ext[0],w,h] for x,y,w,h in p['protected_boxes']];p['protection_reviewed']=True;p['status']='raw_accepted_lettering_unreviewed';p['items']={}
 for i,it in enumerate(ps[n]['items']):
  box,tip=items[i];p['items'][str(i)]={'box':box,'tip':tip,'font_size':31,'lines':fit(it['text'],box[2]-8,box[3]-12,31)}
 if n==19:p['items']['1']['attachment_angle']=2.3
 if n==21:p['items']['0']['attachment_angle']=2.4
 if n==26:p['items']['0']['attachment_angle']=2.5
 config['panels'][str(n)]=p
rp.write_text(json.dumps(reviews,indent=2));(B/'source/layout_config.json').write_text(json.dumps(config,indent=2))
