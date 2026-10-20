from pathlib import Path
import json,os,copy
B=Path(__file__).resolve().parents[1];config=json.loads((B/'source/layout_config.json').read_text());os.environ['ANIME_ACE_FONT']=config['font_path'];from fit_text import fit
c=json.loads((B/'source/received_candidates.json').read_text());ps={p['panel']:p for p in json.loads((B/'source/lettering_script.json').read_text())['panels']};rp=B/'qa/independent_raw_review.json';reviews=json.loads(rp.read_text());settings={4:([450,280],[([420,0,370,180],[470,570]),([0,200,350,200],[100,570]),([200,1090,590,230],[370,580])]),5:([180,0],[([0,0,490,190],[215,490])]),6:([220,0],[([0,0,450,200],[280,390]),([470,120,320,170],[635,510])]),7:([350,290],[([410,0,380,230],[505,440]),([0,160,380,170],[95,425]),([0,940,780,240],[410,465])]),8:([450,230],[([0,0,450,220],[320,555]),([460,130,330,290],[515,830]),([450,1110,330,150],[670,590])]),9:([400,250],[([350,0,440,360],[625,490]),([0,210,340,210],[245,485]),([430,1020,360,170],[525,480])]),10:([0,0],[]),11:([430,0],[([0,0,450,330],[350,510]),([470,180,320,250],[440,510])])}
for n,(ext,items) in settings.items():
 p=copy.deepcopy(c['panels'][str(n)]);r={'panels':[n],'sha256':p['source_sha256'],'crop_xyxy':p['crop'],'verdict':'pass','evidence':'qa/independent_opening04_11_review.md','scope':'Exact crop only; lettering not reviewed'}
 if r not in reviews['reviews']:reviews['reviews'].append(r)
 p['extension']=ext;p['protected_boxes']=[[x,y+ext[0],w,h] for x,y,w,h in p['protected_boxes']];p['protection_reviewed']=True;p['status']='raw_accepted_lettering_unreviewed';p['items']={}
 for i,it in enumerate(ps[n]['items']):
  box,tip=items[i];p['items'][str(i)]={'box':box,'tip':tip,'font_size':31,'lines':fit(it['text'],box[2]-8,box[3]-12,31)}
 if n==4:p['items']['2']['attachment_angle']=4.0;p['items']['1']['attachment_angle']=2.4
 if n==6:p['items']['0']['attachment_angle']=1.3
 if n==7:p['items']['2']['attachment_angle']=4.7;p['items']['1']['attachment_angle']=2.4
 if n==8:p['items']['1']['attachment_angle']=2.2;p['items']['0']['attachment_angle']=2.3;p['items']['2']['attachment_angle']=5.4
 if n==9:p['items']['0']['attachment_angle']=0.8;p['items']['2']['attachment_angle']=4.7;p['items']['1']['attachment_angle']=1.3
 config['panels'][str(n)]=p
rp.write_text(json.dumps(reviews,indent=2));(B/'source/layout_config.json').write_text(json.dumps(config,indent=2))
