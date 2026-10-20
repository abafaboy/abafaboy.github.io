from pathlib import Path
import json,hashlib,importlib.util
B=Path(__file__).resolve().parents[1];S=B/'source'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
pro=json.loads((B/'qa/preparation_provenance.json').read_text());manifest=pro['locked_manifest_verified']
for name,h in manifest.items():assert sha(S/name)==h,name
assert sha(S/'script_v1.md')==manifest['CH010_script.md']
a=json.loads((S/'lettering_script.json').read_text());d=json.loads((S/'dialogue.json').read_text())
entries=[{'unit_id':p['unit_id'],'speaker_and_delivery':i['speaker_and_delivery'],'text':i['text']} for p in a['panels'] for i in p['items']]
assert entries==d['entries'] and len(entries)==47
assert [p['unit_id'] for p in a['panels'] if not p['items']]==['P08','P10','P12','P19','P25','P28']
f=json.loads((S/'provisional_text_fit.json').read_text());count=0
for p in f['panels']:
 for item in p['items']:
  for opt in item['candidates']:
   assert opt['font_size']==31 and ' '.join(opt['lines'])==' '.join(item['text'].split())
   count+=1
spec=importlib.util.spec_from_file_location('ch010_render',S/'build_chapter.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
try:mod.render_panel(8,{'items':{},'source':'not_present.png','crop':[0,0,1,1]})
except AssertionError as e:assert 'protection' in str(e).lower()
else:raise AssertionError('Missing geometry was not rejected')
result={'status':'PREPARATION_PASS_ONLY','locked_files_verified':len(manifest),'units':32,'spoken_lines':47,'silent_units':['P08','P10','P12','P19','P25','P28'],'fixed_size_fit_options':count,'missing_geometry_gate':'rejects','art_review':'pending','final_layout':'not_attempted','final_export':'not_attempted'}
(B/'qa/preparation_preflight.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
