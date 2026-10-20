from pathlib import Path
import json,os
from fit_text import fit
B=Path(__file__).resolve().parents[1];q=json.loads((B/'qa/incoming_v0/Chapter5_Independent_QA/qa_ledger.json').read_text());s=json.loads((B/'source/lettering_script.json').read_text());pmap={p['panel']:p for p in s['panels']}
config={'font_path':os.environ['ANIME_ACE_FONT'],'panels':{}}
settings={32:{'extension':[310,340],'boxes':[[325,14,450,260],[18,600,350,185],[390,635,395,240]],'tips':[[540,300],[202,520],[565,590]]},34:{'extension':[410,10],'boxes':[[10,10,425,350],[445,70,345,310]],'tips':[[289,420],[536,450]]}}
for p in q['panels']:
 n=p['panel'];spec=settings[n];crop=p['source_crop_xyxy'];sc=800/(crop[2]-crop[0]);top=spec['extension'][0]
 prot=[]
 for kind,bs in p['protection_output_xyxy'].items():
  if kind=='mouths':continue
  for x1,y1,x2,y2 in bs:prot.append([x1*sc,y1*sc+top,(x2-x1)*sc,(y2-y1)*sc])
 c={'source':'raw/batch01/'+p['source_native_path'],'crop':crop,'extension':spec['extension'],'protected_boxes':prot,'items':{}}
 for i,it in enumerate(pmap[n]['items']):
  box=spec['boxes'][i];lines=fit(it['text'],box[2]-8,box[3]-12,31)
  c['items'][str(i)]={'box':box,'lines':lines,'font_size':31,'tip':spec['tips'][i]}
 config['panels'][str(n)]=c
(B/'source/layout_config.json').write_text(json.dumps(config,indent=2))
