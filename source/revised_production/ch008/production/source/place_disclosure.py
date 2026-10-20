from pathlib import Path
import json,os
B=Path(__file__).resolve().parents[1];c=json.loads((B/'source/layout_config.json').read_text());os.environ['ANIME_ACE_FONT']=c['font_path']
from fit_text import fit
s=json.loads((B/'source/lettering_script.json').read_text());ps={p['panel']:p for p in s['panels']};root='raw/B04_repair/Chapter_8_B04'
protected={11:[[125,195,330,400],[490,90,675,285],[350,400,590,625],[995,195,1225,430],[1310,285,1536,710],[835,405,1000,555],[870,615,980,705],[630,580,720,755],[270,470,410,640],[480,375,720,445],[930,110,1025,260],[290,395,1450,745]],12:[[330,0,730,450],[850,120,1210,545],[180,725,295,790],[690,740,805,790],[35,720,1536,1024],[1220,0,1536,600]],13:[[350,25,665,365],[825,150,1110,480],[0,325,205,780],[1320,140,1536,515],[300,610,390,660],[650,610,760,660],[85,610,1340,1024]],14:[[60,175,310,420],[560,90,790,310],[965,290,1280,575],[1310,300,1536,670],[220,405,515,710],[550,430,670,495],[830,425,945,520],[870,690,960,805],[450,445,1445,835]]}
data={11:([400,0],[([50,20,700,210],[645,560]),([80,220,640,150],[645,560])]),12:([500,0],[([400,0,390,150],[430,650]),([10,170,370,150],[250,495]),([450,340,340,150],[530,550])]),13:([0,0],[([140,210,180,100],[165,190])]),14:([510,0],[([20,0,440,170],[400,550]),([430,180,360,170],[580,650]),([30,365,300,140],[285,640])])}
for n,(extension,items) in data.items():
 top=extension[0];p=c['panels'][str(n)];p.update(source=f'{root}/selected/Chapter_8_B04_P{n:02}_REVIEW.png',crop=[0,0,1536,1024],extension=extension,protection_reviewed=True,status='independent_raw_pass_lettering_proof',protected_boxes=[[x*800/1536,y*800/1536+top,(xx-x)*800/1536,(yy-y)*800/1536] for x,y,xx,yy in protected[n]],protected_polygons=[],items={})
 for i,(box,tip) in enumerate(items):p['items'][str(i)]={'box':box,'tip':tip,'font_size':31,'lines':fit(ps[n]['items'][i]['text'],box[2],box[3],31)}
for i in ('0','1'):c['panels']['11']['items'][i]['body_box']=[10,0,780,400]
c['panels']['11']['items']['0']['attachment_angle']=0.8
c['panels']['11']['items']['1']['shared_balloon']=True
c['panels']['14']['items']['0']['attachment_angle']=0.8
c['panels']['12']['items']['0']['attachment_angle']=2.4
(B/'source/layout_config.json').write_text(json.dumps(c,indent=2)+'\n')
