from pathlib import Path
import os,json
B=Path(__file__).resolve().parents[1];p=B/'source/layout_config.json';c=json.loads(p.read_text());s=json.loads((B/'source/lettering_script.json').read_text());os.environ['ANIME_ACE_FONT']=c['font_path'];from fit_text import fit
rows={r['panel']:r for r in json.loads((B/'qa/B02_B04_B07_B08_intake.json').read_text())}
def place(n,top,protect,placements):
 r=rows[n];cfg=c['panels'][str(n)];cfg.update(source=str(Path(r['source']).relative_to(B)),crop=r['crop_xyxy'],extension=[top,0],protected_boxes=[[x*800/390,y*800/390+top,w*800/390,h*800/390] for x,y,w,h in protect],protection_reviewed=True,status='raw_pass_lettering_proof_pending')
 for i,(box,tip) in enumerate(placements):cfg['items'][str(i)]={'box':box,'tip':tip,'font_size':31,'lines':fit(s['panels'][n-1]['items'][i]['text'],box[2],box[3],31)}
place(4,0,[(18,88,55,142),(128,162,252,55)],[([170,10,600,200],[155,220])])
place(5,200,[(18,90,47,140),(42,125,47,28),(258,101,37,40),(241,150,83,39),(292,157,90,60)],[([430,10,340,120],[616,400]),([10,160,480,220],[137,430])])
place(6,0,[],[])
p.write_text(json.dumps(c,indent=2)+'\n')
