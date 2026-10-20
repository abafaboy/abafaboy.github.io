from pathlib import Path
import json,os
B=Path(__file__).resolve().parents[1];P=B/'source/layout_config.json';c=json.loads(P.read_text());os.environ['ANIME_ACE_FONT']=c['font_path'];from fit_text import fit
s=json.loads((B/'source/lettering_script.json').read_text());m=json.loads((B/'raw/B08/CH009_B08/manifest.json').read_text())
regions={29:[],30:[[390,55,560,215],[320,390,590,910],[650,530,760,620],[630,620,780,890],[850,60,990,220],[815,210,1100,910],[1100,285,1536,670],[100,30,350,240],[0,620,365,810]],31:[[320,25,800,745],[65,0,245,300],[10,765,295,1430],[330,1025,445,1110],[320,1105,465,1410],[700,910,1024,1220],[500,805,665,965],[285,965,700,1050],[75,1140,625,1290]]}
for n in [29,30,31]:
 row=c['panels'][str(n)];top=250 if n==30 else 0;scale=800/m['selection'][f'U{n}']['dimensions'][0];row.update(extension=[top,220 if n==31 else 0],protection_reviewed=True,items={},protected_boxes=[[x*scale,y*scale+top,(xx-x)*scale,(yy-y)*scale] for x,y,xx,yy in regions[n]],status='staged_threshold_provisional_geometry_raw_gate_enforced')
 if n==29:row['protected_boxes']=[[0,0,800,1200]]
 placements={30:[([300,0,480,190],[400,550]),([600,180,180,100],[525,340])],31:[([400,1220,400,180],[350,850])]}.get(n,[])
 for i,(box,tip) in enumerate(placements):
  text=s['panels'][n-1]['items'][i]['text'];row['items'][str(i)]={'box':box,'tip':tip,'font_size':31,'lines':fit(text,box[2],box[3],31)}
 if n==30:row['items']['0'].update(attachment_angle=2.3,tail_waypoints=[[400,270],[405,500]])
 if n==31:row['items']['0'].update(attachment_angle=-2.0,tail_waypoints=[[500,1100],[500,880],[480,850]])
P.write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
