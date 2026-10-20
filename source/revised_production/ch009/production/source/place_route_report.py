from pathlib import Path
import json,os
B=Path(__file__).resolve().parents[1];P=B/'source/layout_config.json';c=json.loads(P.read_text());os.environ['ANIME_ACE_FONT']=c['font_path'];from fit_text import fit
s=json.loads((B/'source/lettering_script.json').read_text())
regions={17:[[0,0,1536,1024]],18:[[230,280,305,330],[225,330,350,370],[210,365,290,480],[340,300,640,470],[100,530,580,680],[910,150,1010,250],[800,280,1130,570]],19:[[20,165,450,730],[315,75,540,675],[530,90,765,770],[790,90,1045,760],[1100,420,1210,495],[1030,490,1240,755],[1235,40,1536,480]],20:[[20,165,450,730],[315,75,540,675],[650,90,760,220],[530,215,765,770],[790,90,1045,760],[1100,420,1210,495],[1100,490,1260,755],[1235,40,1536,480]]}
for n in [17,18,19,20]:
 top={17:0,18:200,19:570,20:350}[n];r=c['panels'][str(n)];r.update(extension=[top,0],protection_reviewed=True,items={},protected_boxes=[[x*800/1536,y*800/1536+top,(xx-x)*800/1536,(yy-y)*800/1536] for x,y,xx,yy in regions[n]],status='provisional_geometry_raw_review_gate_enforced')
 placements={18:[([10,0,320,110],[165,360]),([400,120,390,160],[470,315])],19:[([200,20,580,240],[565,815]),([200,270,580,240],None)],20:[([0,0,400,210],[400,440]),([420,250,380,190],[565,590])]}.get(n,[])
 for i,(box,tip) in enumerate(placements):
  text=s['panels'][n-1]['items'][i]['text'];r['items'][str(i)]={'box':box,'font_size':31,'lines':fit(text,box[2],box[3],31)}
  if tip:r['items'][str(i)]['tip']=tip
 if n==18:r['items']['1']['attachment_angle']=2.3
 if n==19:
  for i in ['0','1']:r['items'][i]['body_box']=[180,0,620,540]
  r['items']['1'].update(shared_balloon=True,tip=[565,815])
  r['items']['0']['attachment_angle']=1.3
 if n==20:r['items']['0'].update(attachment_angle=0.7,tail_waypoints=[[410,250],[410,400]])
P.write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
