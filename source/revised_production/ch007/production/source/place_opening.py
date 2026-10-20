from pathlib import Path
import json,os
B=Path(__file__).resolve().parents[1];p=B/'source/layout_config.json';c=json.loads(p.read_text());s=json.loads((B/'source/lettering_script.json').read_text());os.environ['ANIME_ACE_FONT']=c['font_path']
from fit_text import fit
intake={r['panel']:r for r in json.loads((B/'qa/B01_intake.json').read_text())}
def setp(n,top,protected,placements):
 cfg=c['panels'][str(n)];cfg.update(source=str(Path(intake[n]['source']).relative_to(B)),crop=intake[n]['crop_xyxy'],extension=[top,0],protected_boxes=[[x*800/1536,y*800/1536+top,w*800/1536,h*800/1536] for x,y,w,h in protected],protection_reviewed=True,status='raw_pass_lettering_proof_pending')
 for i,(box,tip) in enumerate(placements):cfg['items'][str(i)]={'box':box,'tip':tip,'font_size':31,'lines':fit(s['panels'][n-1]['items'][i]['text'],box[2],box[3],31)}
setp(2,310,[(330,0,280,320),(960,25,235,315),(330,430,390,195),(840,560,245,180),(1360,800,120,210),(1200,320,155,180)], [([20,20,440,230],[486,447]),([470,55,320,220],[635,449])])
setp(3,300,[(350,10,165,175),(925,165,150,165),(590,495,150,135),(570,585,260,225),(790,450,130,150),(1290,230,210,100),(220,380,100,180),(460,410,70,155)], [([30,20,670,230],[472,451]),([35,670,260,120],[290,600])])
p.write_text(json.dumps(c,indent=2)+'\n')
