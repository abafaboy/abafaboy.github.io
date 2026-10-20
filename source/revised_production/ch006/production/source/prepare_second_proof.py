from pathlib import Path
import json,hashlib,copy,os
from PIL import Image,ImageChops
B=Path(__file__).resolve().parents[1];config=json.loads((B/'source/layout_config.json').read_text());os.environ['ANIME_ACE_FONT']=config['font_path'];from fit_text import fit
c=json.loads((B/'source/received_candidates.json').read_text());root=B/'raw/My_Summons_Go_First_CH6_Batch01_Panels30-31/art'
for p in json.loads((root/'panel_manifest.json').read_text())['panels']:
 src=root/p['source_original'];assert hashlib.sha256(src.read_bytes()).hexdigest()==p['source_sha256'];cut=Image.open(src).convert('RGB').crop(p['crop_xyxy']);out=Image.open(root/p['selected_png']).convert('RGB');assert cut.size==out.size and ImageChops.difference(cut,out).getbbox() is None;sc=800/cut.width
 c['panels'][str(p['panel'])]={'source':str(src.relative_to(B)),'source_sha256':p['source_sha256'],'crop':p['crop_xyxy'],'extension':[0,0],'protected_boxes':[[x*sc,y*sc,(xx-x)*sc,(yy-y)*sc] for x,y,xx,yy in p['face_protection_xyxy']+p['prop_and_acting_protection_xyxy']],'protected_polygons':[],'protection_reviewed':False,'status':'received_pending_independent_raw_QA','items':{}}
(B/'source/received_candidates.json').write_text(json.dumps(c,indent=2));ps={p['panel']:p for p in json.loads((B/'source/lettering_script.json').read_text())['panels']};rp=B/'qa/independent_raw_review.json';reviews=json.loads(rp.read_text());evidence='qa/independent_arriving_art_review_addendum_30_31_35_37.md'
settings={31:([220,0],[([5,5,540,200],[210,300])]),35:([210,250],[([410,0,380,190],[642,380]),([10,830,600,200],[145,380])]),36:([260,320],[([5,5,540,230],[220,400]),([575,105,210,120],[715,440]),([5,885,700,220],[430,490])]),37:([230,0],[([0,0,430,200],[150,380]),([450,40,340,180],[640,400])])}
for n,(ext,items) in settings.items():
 p=copy.deepcopy(c['panels'][str(n)]);r={'panels':[n],'sha256':p['source_sha256'],'crop_xyxy':p['crop'],'verdict':'pass','evidence':evidence,'scope':'Exact crop only; lettering not reviewed'}
 if r not in reviews['reviews']:reviews['reviews'].append(r)
 if n==31:p['protected_boxes'].append([65*800/1024,195*800/1024,125*800/1024,80*800/1024])
 p['extension']=ext;p['protected_boxes']=[[x,y+ext[0],w,h] for x,y,w,h in p['protected_boxes']];p['protection_reviewed']=True;p['status']='raw_accepted_lettering_unreviewed';p['items']={}
 for i,it in enumerate(ps[n]['items']):
  box,tip=items[i];p['items'][str(i)]={'box':box,'tip':tip,'font_size':31,'lines':fit(it['text'],box[2]-8,box[3]-12,31)}
 if n==31:p['items']['0']['attachment_angle']=2.3
 if n==35:p['items']['1']['attachment_angle']=4.0;p['items']['0']['attachment_angle']=0.8
 if n==36:p['items']['2']['attachment_angle']=5.5;p['items']['0']['attachment_angle']=2.3;p['items']['1']['attachment_angle']=0.8
 if n==37:p['items']['0']['attachment_angle']=2.3;p['items']['1']['attachment_angle']=0.8
 config['panels'][str(n)]=p
rp.write_text(json.dumps(reviews,indent=2));(B/'source/layout_config.json').write_text(json.dumps(config,indent=2))
