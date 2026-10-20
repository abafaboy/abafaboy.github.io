"""Stage B02 provisional lettering, retaining raw-review gate."""
from pathlib import Path
import json,os
B=Path(__file__).resolve().parents[1];P=B/'source/layout_config.json';c=json.loads(P.read_text());os.environ['ANIME_ACE_FONT']=c['font_path']
from fit_text import fit
s=json.loads((B/'source/lettering_script.json').read_text());m=json.loads((B/'raw/B02_recovered/B02/manifest.json').read_text());scale=800/1536
# U06 geography anchor remains separately staged until routing is resolved.
data={5:([270,0],[([180,0,320,140],[250,375]),([440,130,350,150],[545,375])]),7:([600,0],[([400,0,390,210],[615,740]),([410,240,390,180],[410,880]),([0,400,400,190],[480,740])]),8:([230,0],[([350,0,340,120],[310,460]),([400,130,230,100],[530,320])])}
for n,(extension,placements) in data.items():
 if n==7:continue # Repaired U7 is owned by place_survey_repair.py; never reinstate held geometry.
 row=c['panels'][str(n)];top=extension[0];row.update(extension=extension,protection_reviewed=True,status='provisional_geometry_raw_acceptance_gate_enforced',items={},protected_boxes=[[v[0]*scale,v[1]*scale+top,(v[2]-v[0])*scale,(v[3]-v[1])*scale] for v in m['protection_regions'][f'U{n:02}'].values()])
 if n==5:
  row['protected_boxes'][4:]=[[419,top+36,68,445],[670,top+10,65,470],[365,top+115,50,95]]
  row['protection_refinement_note']='Native gatepost/hinge strips and visible unloading worker retained; generating broad passage box included speaking Minho, replaced with actual physical extents.'
 for i,(box,tip) in enumerate(placements):
  text=s['panels'][n-1]['items'][i];row['items'][str(i)]={'box':box,'tip':tip,'font_size':31,'lines':fit(text['text'],box[2],box[3],31)}
c['panels']['5']['items']['1']['attachment_angle']=2.3
c['panels']['8']['items']['0']['attachment_angle']=2.3
P.write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
