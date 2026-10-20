from pathlib import Path
import json,os
B=Path(__file__).resolve().parents[1];c=json.loads((B/'source/layout_config.json').read_text());os.environ['ANIME_ACE_FONT']=c['font_path']
from fit_text import fit
s=json.loads((B/'source/lettering_script.json').read_text());ps={p['panel']:p for p in s['panels']};root='raw/B06_repair/Chapter_8_B06_Dish_Fix_01'
protected={20:[[255,25,515,325],[705,70,935,330],[1080,210,1380,500],[1330,30,1536,330],[20,440,330,720],[290,440,500,550],[650,395,925,525],[900,365,1150,525],[305,685,450,810],[950,650,1110,830],[215,380,1190,820]],22:[[0,0,1536,1024]]}
data={20:([340,0],[([100,0,450,170],[425,370]),([460,180,330,150],[650,445])]),22:([0,0],[])}
for n,(extension,items) in data.items():
 top=extension[0];p=c['panels'][str(n)];p.update(source=f'{root}/selected/Chapter_8_P{n:02}_B06_REVIEW.png',crop=[0,0,1536,1024],extension=extension,protection_reviewed=True,status='independent_raw_gate_required',protected_boxes=[[x*800/1536,y*800/1536+top,(xx-x)*800/1536,(yy-y)*800/1536] for x,y,xx,yy in protected[n]],protected_polygons=[],items={})
 for i,(box,tip) in enumerate(items):p['items'][str(i)]={'box':box,'tip':tip,'font_size':31,'lines':fit(ps[n]['items'][i]['text'],box[2],box[3],31)}
(B/'source/layout_config.json').write_text(json.dumps(c,indent=2)+'\n')
