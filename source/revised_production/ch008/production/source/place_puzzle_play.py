from pathlib import Path
import json,os
B=Path(__file__).resolve().parents[1];c=json.loads((B/'source/layout_config.json').read_text());os.environ['ANIME_ACE_FONT']=c['font_path']
from fit_text import fit
s=json.loads((B/'source/lettering_script.json').read_text());ps={p['panel']:p for p in s['panels']};root='raw/B07/Chapter_8_B07'
protected={24:[[300,0,560,290],[920,0,1370,440],[250,340,600,530],[640,435,1000,580],[930,780,1280,925],[10,500,870,1010]],25:[[235,40,460,290],[820,150,1120,425],[1300,40,1536,220],[1250,205,1536,490],[315,430,405,545],[130,490,220,630],[940,550,1060,760],[935,770,1025,910],[5,360,970,990]],26:[[175,35,420,290],[850,175,1100,420],[1280,55,1510,245],[1185,260,1536,515],[245,475,355,565],[1170,315,1305,425],[1060,725,1200,840],[0,430,850,1010]]}
data={24:([550,0],[([350,0,440,210],[450,650]),([0,230,390,150],[220,545]),([470,400,320,140],[600,545])]),25:([230,0],[([10,0,550,220],[180,240])]),26:([590,0],[([0,0,370,150],[430,660]),([410,180,380,220],[700,610]),([0,410,350,180],[150,605])])}
for n,(extension,items) in data.items():
 top=extension[0];p=c['panels'][str(n)];p.update(source=f'{root}/selected/Chapter_8_P{n:02}_REVIEW_native.png',crop=[0,0,1536,1024],extension=extension,protection_reviewed=True,status='independent_raw_pass_lettering_proof',protected_boxes=[[x*800/1536,y*800/1536+top,(xx-x)*800/1536,(yy-y)*800/1536] for x,y,xx,yy in protected[n]],protected_polygons=[],items={})
 for i,(box,tip) in enumerate(items):p['items'][str(i)]={'box':box,'tip':tip,'font_size':31,'lines':fit(ps[n]['items'][i]['text'],box[2],box[3],31)}
c['panels']['24']['items']['0']['attachment_angle']=2.4
c['panels']['26']['items']['0']['attachment_angle']=0.5
(B/'source/layout_config.json').write_text(json.dumps(c,indent=2)+'\n')
