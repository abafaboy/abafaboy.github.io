from pathlib import Path
import json,os
B=Path(__file__).resolve().parents[1];P=B/'source/layout_config.json';c=json.loads(P.read_text());os.environ['ANIME_ACE_FONT']=c['font_path'];from fit_text import fit
s=json.loads((B/'source/lettering_script.json').read_text())
regions={25:[[0,0,800,533]],26:[[0,60,250,260],[235,75,300,255],[285,90,365,245],[390,20,460,105],[350,105,515,295],[375,290,535,490],[280,270,335,310],[280,310,350,455],[258,350,283,390],[520,80,800,335],[0,350,195,500]],27:[[0,0,800,533]],28:[[365,5,435,95],[170,145,340,300],[350,125,375,160],[340,155,380,245],[370,125,405,155],[385,155,423,270],[425,200,452,255],[455,125,540,245],[540,150,680,250],[455,260,575,295],[0,385,800,480]]}
for n in range(25,29):
 top={25:0,26:250,27:300,28:260}[n];r=c['panels'][str(n)];r.update(extension=[top,300 if n==26 else 0],protection_reviewed=True,items={},protected_boxes=[[x,y+top,xx-x,yy-y] for x,y,xx,yy in regions[n]],protected_polygons=[],status='provisional_geometry_independent_lettering_pending')
 placements={26:[([0,0,400,210],[385,330]),([0,820,400,230],[275,545])],27:[([0,0,300,120],None),([500,150,250,110],None)],28:[([0,0,400,180],[345,400])]}.get(n,[])
 for i,(box,tip) in enumerate(placements):
  item={'box':box,'font_size':31,'lines':fit(s['panels'][n-1]['items'][i]['text'],box[2],box[3],31)}
  if tip:item['tip']=tip
  if n==27:item.update(radio_source_reviewed=True,source_anchor_native=[330,230] if i==0 else [1130,215],transmission_style='tailless radio voice; exact native visible handheld and high-left-chest radio retained')
  r['items'][str(i)]=item
 if n==26:
  r['items']['0'].update(attachment_angle=.5,tail_waypoints=[[350,240],[350,300]])
  r['items']['1'].update(attachment_angle=-1.3,tail_waypoints=[[240,780],[240,600]])
 if n==28:r['items']['0'].update(attachment_angle=.7,tail_waypoints=[[330,290],[330,380]])
P.write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
