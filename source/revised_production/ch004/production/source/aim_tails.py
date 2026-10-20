from pathlib import Path
import json,sys
B=Path(__file__).resolve().parents[1];f=B/'source/layout_config.json';d=json.loads(f.read_text());s={p['panel']:p for p in json.loads((B/'source/lettering_script.json').read_text())['panels']};ids=set(map(int,sys.argv[1].split(',')))
for n in ids:
 c=d['panels'][str(n)]
 for i,item in enumerate(s[n]['items']):
  l=c['items'][str(i)];m=c.get('mouths',{}).get(item['speaker'])
  if not m or 'tip' not in l:continue
  x,y,w,h=l.get('body_box',l['box']);cx=x+w/2;cy=y+h/2;mx,my=m;ty=l['tip'][1]
  if my>ty>cy:l['tip']=[cx+(mx-cx)*(ty-cy)/(my-cy),ty];l['tail_aim']='center-to-mouth projected ray; tip remains outside protected art'
f.write_text(json.dumps(d,indent=2))
