from pathlib import Path
import json,os
B=Path(__file__).resolve().parents[1];c=json.loads((B/'source/layout_config.json').read_text());os.environ['ANIME_ACE_FONT']=c['font_path']
from fit_text import fit
s=json.loads((B/'source/lettering_script.json').read_text());ps={p['panel']:p for p in s['panels']};root='raw/B08_repair/Chapter_8_B08'
protected={27:[[245,55,530,340],[585,0,810,265],[990,325,1210,525],[560,340,790,500],[320,420,525,605],[380,665,545,800],[835,500,1035,630],[1080,440,1380,745],[490,440,1280,1024],[1430,450,1536,590]],28:[[0,0,1536,1024]],29:[[345,25,600,285],[620,30,845,280],[1090,280,1310,470],[555,325,825,510],[150,450,305,560],[370,460,490,600],[1050,470,1390,745],[480,460,1280,1024],[25,580,150,695],[1430,450,1536,600]]}
data={27:([550,0],[([550,0,240,120],[600,715]),([0,150,530,210],[410,540]),([0,380,330,150],[200,570])]),28:([0,0],[]),29:([220,0],[([20,0,600,210],[240,230])])}
for n,(extension,items) in data.items():
 top=extension[0];p=c['panels'][str(n)];p.update(source=f'{root}/selected/Chapter_8_P{n:02}_REVIEW.png',crop=[0,0,1536,1024],extension=extension,protection_reviewed=True,status='independent_raw_gate_required',protected_boxes=[[x*800/1536,y*800/1536+top,(xx-x)*800/1536,(yy-y)*800/1536] for x,y,xx,yy in protected[n]],protected_polygons=[],items={})
 for i,(box,tip) in enumerate(items):p['items'][str(i)]={'box':box,'tip':tip,'font_size':31,'lines':fit(ps[n]['items'][i]['text'],box[2],box[3],31)}
c['panels']['27']['items']['1']['attachment_angle']=0.8
(B/'source/layout_config.json').write_text(json.dumps(c,indent=2)+'\n')
