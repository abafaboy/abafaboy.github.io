"""Provisional lettering on independently accepted full-native B01 crops."""
from pathlib import Path
import json,os
B=Path(__file__).resolve().parents[1];p=B/'source/layout_config.json';c=json.loads(p.read_text());os.environ['ANIME_ACE_FONT']=c['font_path']
from fit_text import fit
s=json.loads((B/'source/lettering_script.json').read_text());manifest=json.loads((B/'raw/B01/manifest.json').read_text())
data={
1:([260,0],[([10,0,200,55],None),([380,20,400,220],[475,410]),([10,225,200,100],[175,435]),([610,340,180,100],[599,485])]),
2:([0,200],[([460,20,320,100],None),([450,170,340,360],[403,175]),([300,1220,480,160],None)]),
3:([400,200],[([20,10,600,210],None),([450,230,330,190],[520,600]),([10,950,600,180],None)]),
4:([0,0],[([300,350,480,220],[388,727]),([400,745,400,160],[530,1115])])}
for n,(extension,placements) in data.items():
 row=c['panels'][str(n)];selected=manifest['selected'][n-1];scale=800/selected['source_dimensions'][0];top=extension[0]
 row.update(extension=extension,protection_reviewed=True,status='independent_raw_pass_provisional_lettering',items={},protected_boxes=[[x['xyxy'][0]*scale,x['xyxy'][1]*scale+top,(x['xyxy'][2]-x['xyxy'][0])*scale,(x['xyxy'][3]-x['xyxy'][1])*scale] for x in selected['protected_regions']])
 if n==4:
  row['native_sequence_gutter']={'after_native_y':426,'height_master':300,'reason':'Blank assembly spacing after original address-check divider; native chronological components and pixels preserved'}
  for box in row['protected_boxes']:
   if box[1]>=426*scale:box[1]+=300
  # Actual native inspection: preserve all three hinges and latch, while allowing blank door-face lettering.
  row['protected_boxes']=row['protected_boxes'][:-1]+[[620,698,16,42],[620,910,16,48],[620,1114,16,50],[665,907,73,62]]
  row['protection_refinement_note']='Broad door rectangle replaced by actual three hinge/latch extents after native inspection; blank door face may receive balloon. Independent lettering review required.'
 for i,(box,tip) in enumerate(placements):
  text=s['panels'][n-1]['items'][i]; item={'box':box,'font_size':31,'lines':fit(text['text'],box[2],box[3],31) if text['kind']=='dialogue' else [text['text']]}
  if tip:item['tip']=tip
  if text.get('transmitted'):item.update(radio_source_reviewed=True,source_anchor_native=selected['voice_source_anchors']['CHAE_phone'],transmission_style='tailless phone voice; single visible speakerphone; source anchor preserved')
  row['items'][str(i)]=item
p.write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
