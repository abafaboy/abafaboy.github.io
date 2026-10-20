from pathlib import Path
import json,os,copy
B=Path(__file__).resolve().parents[1];c=json.loads((B/'source/received_candidates.json').read_text());s=json.loads((B/'source/lettering_script.json').read_text());ps={p['panel']:p for p in s['panels']};config=json.loads((B/'source/layout_config.json').read_text());os.environ['ANIME_ACE_FONT']=config['font_path'];from fit_text import fit
accepted=[1,2,3,15,17,32,33,34];rp=B/'qa/independent_raw_review.json';reviews=json.loads(rp.read_text());
for n in accepted:
 p=c['panels'][str(n)]
 r={'panels':[n],'sha256':p['source_sha256'],'crop_xyxy':p['crop'],'verdict':'pass','evidence':'qa/independent_arriving_art_review_v1.md','scope':'Exact crop only; lettering not reviewed'}
 if r not in reviews['reviews']:reviews['reviews'].append(r)
rp.write_text(json.dumps(reviews,indent=2))
settings={1:([0,0],[]),15:([0,0],[]),2:([0,0],[([430,340,355,180],[610,625]),([20,480,390,190],[265,240]),([30,820,360,170],[475,710])]),3:([145,0],[([15,5,280,130],[173,235])]),17:([210,0],[([350,5,440,195],[430,370])]),32:([310,0],[([15,5,770,285],[175,515])]),33:([100,300],[([460,0,330,160],[515,430]),([5,650,770,260],[195,385])]),34:([0,100],[([5,5,390,170],[410,180]),([5,195,280,245],[-10,275]),([5,455,350,150],[405,240])])}
for n in accepted:
 p=copy.deepcopy(c['panels'][str(n)]);ext,items=settings[n];p['extension']=ext;p['protected_boxes']=[[x,y+ext[0],w,h] for x,y,w,h in p['protected_boxes']];p['protection_reviewed']=True;p['status']='raw_accepted_lettering_unreviewed';p['items']={}
 for i,it in enumerate(ps[n]['items']):
  if it.get('native_imagegen_required'):p['items'][str(i)]={'native_imagegen_text':True,'verified_text':it['text'],'native_visual_qa':'pass','evidence':'qa/independent_arriving_art_review_v1.md'};continue
  box,tip=items[i];p['items'][str(i)]={'box':box,'tip':tip,'font_size':31,'lines':fit(it['text'],box[2]-8,box[3]-12,31)}
 if n==33:p['items']['1']['attachment_angle']=4.0
 if n==34:p['items']['2']['attachment_angle']=-0.8
 if n==32:p['items']['0']['attachment_angle']=2.4
 config['panels'][str(n)]=p
(B/'source/layout_config.json').write_text(json.dumps(config,indent=2))
