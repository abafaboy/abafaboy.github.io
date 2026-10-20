from pathlib import Path
import json,os,hashlib
B=Path(__file__).resolve().parents[1];P=B/'source/layout_config.json';c=json.loads(P.read_text());r=c['panels']['7'];src=B/'raw/B02_repair_v1/B02/originals/U07_v4.png';sha=hashlib.sha256(src.read_bytes()).hexdigest();assert sha=='d38c9dcfe24f5fb70b3ef20e923cfd6e60bb22d6d9fe1e134c419809c2ff795c'
reviews=json.loads((B/'qa/independent_raw_review.json').read_text())['reviews'];assert any(x.get('sha256')==sha and x.get('crop_xyxy')==[0,0,1536,1024] and x.get('verdict')=='pass' for x in reviews),'Await repaired source independent acceptance'
os.environ['ANIME_ACE_FONT']=c['font_path'];from fit_text import fit
s=json.loads((B/'source/lettering_script.json').read_text());m=json.loads((B/'raw/B02_repair_v1/B02/manifest.json').read_text());r.update(source=str(src.relative_to(B)),source_sha256=sha,extension=[450,250],protection_reviewed=True,items={},status='repaired_raw_pass_provisional_lettering',protected_boxes=[[v[0]*800/1536,v[1]*800/1536+450,(v[2]-v[0])*800/1536,(v[3]-v[1])*800/1536] for v in m['protection_regions']['U07'].values()])
for i,(box,tip) in enumerate([([400,0,390,210],[615,650]),([0,250,400,180],[415,730]),([0,1000,400,200],[485,660])]):
 text=s['panels'][6]['items'][i]['text'];r['items'][str(i)]={'box':box,'tip':tip,'font_size':31,'lines':fit(text,box[2],box[3],31)}
r['items']['0']['attachment_angle']=1.3
r['items']['1']['attachment_angle']=0.4
r['items']['2']['attachment_angle']=-0.7
r['items']['2']['tail_waypoints']=[[430,940],[430,700],[435,680],[450,665]]
P.write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
