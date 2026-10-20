"""Read-only readiness report; never substitutes for visual review."""
from pathlib import Path
import json,hashlib,os
B=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def inspect():
 s=json.loads((B/'source/lettering_script.json').read_text());c=json.loads((B/'source/layout_config.json').read_text());reviews=json.loads((B/'qa/independent_raw_review.json').read_text())['reviews'];issues=[]
 if sha(B/'source/script_v1.md')!=s['script_sha256']:issues.append('Production script hash changed')
 if (B.parent/'script_v1.md').exists() and sha(B.parent/'script_v1.md')!=s['script_sha256']:issues.append('Parent script hash changed')
 if not Path(os.environ.get('ANIME_ACE_FONT',c['font_path'])).is_file():issues.append('Licensed local Anime Ace missing')
 for r in json.loads((B/'source/reference_lock.json').read_text())['selected']:
  p=Path(r['path']);p=p if p.is_absolute() else B/p
  if not p.is_file() or sha(p)!=r['sha256']:issues.append('Reference changed: '+str(p))
 missing=[];unapproved=[];unplaced=[]
 for panel in s['panels']:
  n=panel['panel'];cfg=c['panels'].get(str(n))
  if not cfg or not cfg.get('source'):missing.append(n);continue
  src=Path(cfg['source']);src=src if src.is_absolute() else B/src
  if not src.is_file():missing.append(n);continue
  matches=[r for r in reviews if r.get('sha256')==sha(src) and n in r.get('panels',[]) and r.get('crop_xyxy')==cfg.get('crop')]
  if not matches or matches[-1].get('verdict')!='pass':unapproved.append(n)
  if not cfg.get('protection_reviewed') or set(cfg.get('items',{}))!={str(i) for i in range(len(panel['items']))}:unplaced.append(n)
  for i,it in enumerate(panel['items']):
   lay=cfg.get('items',{}).get(str(i),{})
   if it.get('native_imagegen_required') and not (lay.get('native_imagegen_text') and lay.get('verified_text')==it['text'] and lay.get('native_visual_qa')=='pass'):issues.append(f'P{n} item {i}: exact native phone UI not verified')
 return {'chapter':6,'expected_units':41,'text_items':sum(len(p['items']) for p in s['panels']),'missing_story_art':missing,'unapproved_raw_art':unapproved,'incomplete_layouts':unplaced,'issues':issues,'ready_to_render':not(missing or unapproved or unplaced or issues)}
if __name__=='__main__':print(json.dumps(inspect(),indent=2))
