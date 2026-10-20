from pathlib import Path
import json,os
B=Path(__file__).resolve().parents[1];P=B/'source/layout_config.json';c=json.loads(P.read_text());os.environ['ANIME_ACE_FONT']=c['font_path'];from fit_text import fit
s=json.loads((B/'source/lettering_script.json').read_text())
regions={13:[[120,180,390,340],[210,340,390,460],[380,140,510,520],[735,250,880,660],[665,380,760,470],[500,350,605,610],[900,300,1015,610],[530,610,1010,685],[1020,470,1280,610],[1080,330,1265,450],[1300,200,1536,485],[695,0,830,130]],15:[[0,0,1536,1024]],16:[[0,0,1536,1024]]}
for n in [13,15,16]:
 top={13:320,15:440,16:0}[n];r=c['panels'][str(n)];r.update(extension=[top,0],protection_reviewed=True,items={},protected_boxes=[[x*800/1536,y*800/1536+top,(xx-x)*800/1536,(yy-y)*800/1536] for x,y,xx,yy in regions[n]],status='provisional_geometry_independent_lettering_pending')
 placements={13:[([400,0,360,120],[370,465]),([250,700,500,150],[115,565])],15:[([0,0,370,150],[0,160]),([320,180,480,240],[800,430])]}.get(n,[])
 for i,(box,tip) in enumerate(placements):
  r['items'][str(i)]={'box':box,'tip':tip,'font_size':31,'lines':fit(s['panels'][n-1]['items'][i]['text'],box[2],box[3],31)}
 if n==13:
  r['protected_polygons']=[[[x*800/1536,y*800/1536+top] for x,y in [(95,340),(190,340),(192,430),(228,500),(245,700),(235,850),(285,960),(220,990),(35,1005),(20,900),(45,720),(0,600),(15,480),(95,430)]]]
  r['items']['1'].update(attachment_angle=-2.6,tail_waypoints=[[145,610],[130,580]])
  r['items']['0'].update(attachment_angle=2.0,tail_waypoints=[[400,260],[340,315],[340,400],[350,440]])
# Explicitly preserve held B05 geometry without allowing protection-ready status.
for n in [18,20]:c['panels'][str(n)].update(protection_reviewed=False,status='raw_hold_awaiting_parent_repair')
P.write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
