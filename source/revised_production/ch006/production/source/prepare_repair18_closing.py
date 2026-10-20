from pathlib import Path
import json,os,copy,hashlib
B=Path(__file__).resolve().parents[1];config=json.loads((B/'source/layout_config.json').read_text());os.environ['ANIME_ACE_FONT']=config['font_path'];from fit_text import fit
c=json.loads((B/'source/received_candidates.json').read_text());ps={p['panel']:p for p in json.loads((B/'source/lettering_script.json').read_text())['panels']};rp=B/'qa/independent_raw_review.json';reviews=json.loads(rp.read_text());p18=copy.deepcopy(c['panels']['18']);p18['source']='repairs/Chapter6_Panel18_RadioContact_Repair_PENDING_QA/candidates/p018_repair_v3.png';p18['source_sha256']=hashlib.sha256((B/p18['source']).read_bytes()).hexdigest();assert p18['source_sha256']=='c8b50795cc21257c6817fb0f8ab31619d4bc4a0b88ab58a6abe730a3de6f01f1'
p18['protected_boxes'] += [[x*800/1536,y*800/1536,(xx-x)*800/1536,(yy-y)*800/1536] for x,y,xx,yy in [[180,245,315,420],[1090,375,1335,720],[430,640,630,825]]];c['panels']['18']=p18
settings={18:([190,0],[([0,0,360,175],[82,315])]),38:([170,280],[([470,0,320,180],[550,520]),([0,220,260,140],[265,260]),([300,790,490,220],[550,550])]),39:([230,0],[([0,0,440,220],[275,350]),([460,245,330,250],[550,550])])}
for n,(ext,items) in settings.items():
 p=copy.deepcopy(c['panels'][str(n)]);r={'panels':[n],'sha256':p['source_sha256'],'crop_xyxy':p['crop'],'verdict':'pass','evidence':'qa/independent_repair18_and_closing38_39_review.md','scope':'Exact crop only; lettering not reviewed'}
 if r not in reviews['reviews']:reviews['reviews'].append(r)
 p['extension']=ext;p['protected_boxes']=[[x,y+ext[0],w,h] for x,y,w,h in p['protected_boxes']];p['protection_reviewed']=True;p['status']='raw_accepted_lettering_unreviewed';p['items']={}
 for i,it in enumerate(ps[n]['items']):
  box,tip=items[i];p['items'][str(i)]={'box':box,'tip':tip,'font_size':31,'lines':fit(it['text'],box[2]-8,box[3]-12,31)}
 if n==18:p['items']['0']['attachment_angle']=2.4
 if n==38:p['items']['2']['attachment_angle']=5.5
 if n==39:p['items']['0']['attachment_angle']=2.3
 config['panels'][str(n)]=p
rp.write_text(json.dumps(reviews,indent=2));(B/'source/layout_config.json').write_text(json.dumps(config,indent=2))
