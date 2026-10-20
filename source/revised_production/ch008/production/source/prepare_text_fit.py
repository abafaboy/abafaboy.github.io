"""Text-only fitting candidates. No artwork or final balloon placements are inferred."""
from pathlib import Path
import os,json
B=Path(__file__).resolve().parents[1]
c=json.loads((B/'source/layout_config.json').read_text());os.environ['ANIME_ACE_FONT']=c['font_path']
from fit_text import fit
s=json.loads((B/'source/lettering_script.json').read_text());out=[]
for p in s['panels']:
 items=[]
 for i,it in enumerate(p['items']):
  if it['kind']!='dialogue':continue
  options=[]
  for w in (320,400,480,560,640):
   for h in range(100,501,10):
    try:lines=fit(it['text'],w,h,31)
    except ValueError:continue
    options.append({'width':w,'height':h,'font_size':31,'phone_equivalent_px':15.1125,'lines':lines});break
  assert options,(p['panel'],i)
  items.append({'index':i,'speaker':it['speaker'],'text':it['text'],'candidates':options,'placement_status':'not_placed_requires_art_review'})
 out.append({'panel':p['panel'],'items':items})
(B/'source/provisional_text_fit.json').write_text(json.dumps({'chapter':8,'note':'Candidate dimensions only, not placement or visual approval. No invented text.','panels':out},ensure_ascii=False,indent=2)+'\n')
print('Fit candidate balloons for',sum(len(p['items']) for p in out),'spoken lines.')
