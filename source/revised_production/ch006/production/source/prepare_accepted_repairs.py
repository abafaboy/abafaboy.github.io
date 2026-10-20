from pathlib import Path
import json,os,copy,hashlib
B=Path(__file__).resolve().parents[1];config=json.loads((B/'source/layout_config.json').read_text());os.environ['ANIME_ACE_FONT']=config['font_path'];from fit_text import fit
c=json.loads((B/'source/received_candidates.json').read_text());ps={p['panel']:p for p in json.loads((B/'source/lettering_script.json').read_text())['panels']};rp=B/'qa/independent_raw_review.json';reviews=json.loads(rp.read_text());
p20=copy.deepcopy(c['panels']['20']);p20['source']='repairs/Chapter6_Panel20_RadioHook_Repair_Candidate_v4_QA/originals/p020_repair_v4_native.png';p20['source_sha256']='0f0237ecb851bb2f7427b1fc335593e4d0440296889735a55f8867c87824004a';p20['art_provenance']='Composited imagegen prop repair, unchanged original pixels outside native rectangle [650,295,795,470]. See repair source crop_mapping.json.';c['panels']['20']=p20
p29=copy.deepcopy(c['panels']['29']);p29['source']='repairs/My_Summons_Go_First_CH6_P29_Repair_v11_Handoff/originals/P29_repair_v11_native.png';p29['source_sha256']='c72c5e0176405c603021662e3437b34e0ead55511333eeed4a134ddb9499b5f1';p29['protected_boxes']+=[[365*.78125,325*.78125,170*.78125,250*.78125]];c['panels']['29']=p29
root=B/'raw/My_Summons_Go_First_CH6_Panel40_Source_QA';p=json.loads((root/'panel_manifest.json').read_text())['panels'][0];sc=800/1254;c['panels']['40']={'source':str((root/p['source_original']).relative_to(B)),'source_sha256':p['source_sha256'],'crop':p['crop_xyxy'],'protected_boxes':[[x*sc,y*sc,(xx-x)*sc,(yy-y)*sc] for x,y,xx,yy in p['face_protection_xyxy']+p['prop_and_acting_protection_xyxy']+p['scale_protection_xyxy']],'protected_polygons':[]}
settings={20:([190,0],[([0,0,470,175],[-10,220])]),29:([0,0],[([570,0,220,150],[710,280]),([5,1110,220,80],None)]),40:([300,0],[([0,0,430,240],[380,660]),([470,160,320,150],[780,-20]),([0,370,300,160],[150,700])])}
for n,(ext,items) in settings.items():
 p=copy.deepcopy(c['panels'][str(n)]);assert hashlib.sha256((B/p['source']).read_bytes()).hexdigest()==p['source_sha256'];r={'panels':[n],'sha256':p['source_sha256'],'crop_xyxy':p['crop'],'verdict':'pass','evidence':'qa/independent_p20_v4_and_p41_review.md' if n==20 else 'qa/independent_p29_v11_and_p40_review.md','scope':'Exact crop only; lettering not reviewed'}
 if r not in reviews['reviews']:reviews['reviews'].append(r)
 p['extension']=ext;p['protected_boxes']=[[x,y+ext[0],w,h] for x,y,w,h in p['protected_boxes']];p['protection_reviewed']=True;p['status']='raw_accepted_lettering_unreviewed';p['items']={}
 for i,it in enumerate(ps[n]['items']):
  box,tip=items[i];p['items'][str(i)]={'box':box,'tip':tip,'font_size':31,'lines':fit(it['text'],box[2]-8,box[3]-12,31)}
 if n==40:p['items']['0']['attachment_angle']=0.8;p['items']['1']['attachment_angle']=5.5
 config['panels'][str(n)]=p
rp.write_text(json.dumps(reviews,indent=2));(B/'source/layout_config.json').write_text(json.dumps(config,indent=2))
