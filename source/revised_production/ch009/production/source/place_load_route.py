from pathlib import Path
import json,os
B=Path(__file__).resolve().parents[1];P=B/'source/layout_config.json';c=json.loads(P.read_text());os.environ['ANIME_ACE_FONT']=c['font_path'];from fit_text import fit
s=json.loads((B/'source/lettering_script.json').read_text())
# Pixel-inspected object bounds in 800px full-native layouts. No art altered.
regions={21:[[0,30,220,275],[240,195,390,245],[360,70,465,145],[485,40,570,150],[520,160,555,195],[495,195,575,370],[425,230,480,340],[0,440,800,533]],22:[[20,155,90,320],[205,95,395,235],[368,235,375,265],[230,260,295,266],[350,260,370,266],[160,240,270,375],[465,120,495,155],[455,155,510,265],[430,170,455,195],[508,185,535,245],[395,260,535,300],[540,135,680,235],[360,5,440,100],[0,420,800,533]],23:[[0,0,800,533]],24:[[0,35,180,390],[180,105,515,460],[505,20,550,85],[435,85,600,380],[575,180,735,440],[730,240,800,420],[590,130,765,200]]}
tops={21:160,22:350,23:0,24:180}
for n in range(21,25):
 r=c['panels'][str(n)];top=tops[n];r.update(extension=[top,120 if n==24 else 0],protection_reviewed=True,items={},protected_boxes=[[x,y+top,xx-x,yy-y] for x,y,xx,yy in regions[n]],protected_polygons=[],status='provisional_geometry_independent_lettering_pending')
 placements={21:[([180,0,320,120],[515,340])],22:[([400,0,390,180],[460,490]),([500,650,280,110],[340,600])],24:[([320,0,380,140],[499,240])]}.get(n,[])
 for i,(box,tip) in enumerate(placements):r['items'][str(i)]={'box':box,'tip':tip,'font_size':31,'lines':fit(s['panels'][n-1]['items'][i]['text'],box[2],box[3],31)}
 if n==21:r['items']['0'].update(attachment_angle=.8,tail_waypoints=[[475,150],[475,310]])
 if n==22:
  r['items']['0'].update(attachment_angle=2.0,tail_waypoints=[[450,300],[450,465]])
  r['items']['1'].update(attachment_angle=-2.0,tail_spread=.035,tail_waypoints=[[450,675],[380,655],[350,620]])
  r['protected_polygons']=[[[x,y+top] for x,y in [(315,235),(330,240),(335,270),(365,300),(350,345),(350,410),(325,420),(312,390),(300,400),(285,390),(295,325),(290,300),(260,295),(260,280),(295,265)]]]
 if n==24:r['items']['0'].update(attachment_angle=2.0,tail_waypoints=[[480,185]]);r['items']['1']={'box':[250,730,280,60],'font_size':40,'lines':['THUNK.']}
P.write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
