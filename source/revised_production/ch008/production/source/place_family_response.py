from pathlib import Path
import json,os
B=Path(__file__).resolve().parents[1];c=json.loads((B/'source/layout_config.json').read_text());os.environ['ANIME_ACE_FONT']=c['font_path']
from fit_text import fit
s=json.loads((B/'source/lettering_script.json').read_text());ps={p['panel']:p for p in s['panels']};root='raw/B05/Chapter_8_B05'
protected={15:[[195,25,515,415],[875,30,1340,540],[110,535,320,630],[460,525,650,625],[830,690,1150,930],[0,540,1010,1020]],18:[[210,35,550,425],[1020,190,1360,525],[135,530,370,615],[480,530,640,625],[925,600,1120,710],[1120,475,1510,1000],[170,545,1195,930],[700,180,830,400]]}
data={15:([430,0],[([200,0,590,220],[445,610]),([10,240,380,180],[300,500])]),18:([530,0],[([10,0,600,240],[100,650]),([200,265,590,250],[520,750])])}
for n,(extension,items) in data.items():
 top=extension[0];p=c['panels'][str(n)];p.update(source=f'{root}/selected/Chapter_8_P{n:02}_REVIEW.png',crop=[0,0,1536,1024],extension=extension,protection_reviewed=True,status='independent_raw_pass_lettering_proof',protected_boxes=[[x*800/1536,y*800/1536+top,(xx-x)*800/1536,(yy-y)*800/1536] for x,y,xx,yy in protected[n]],protected_polygons=[],items={})
 for i,(box,tip) in enumerate(items):p['items'][str(i)]={'box':box,'tip':tip,'font_size':31,'lines':fit(ps[n]['items'][i]['text'],box[2],box[3],31)}
c['panels']['15']['items']['0']['attachment_angle']=1.8
c['panels']['15']['items']['1']['attachment_angle']=0.7
c['panels']['18']['items']['0']['attachment_angle']=2.4
(B/'source/layout_config.json').write_text(json.dumps(c,indent=2)+'\n')
