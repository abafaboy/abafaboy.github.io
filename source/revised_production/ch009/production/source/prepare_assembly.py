"""Prepare Chapter 9 native assembly. Never approve raw art or alter native pixels."""
from pathlib import Path
import json,hashlib,shutil,re
B=Path(__file__).resolve().parents[1]; C=B.parent; OLD=C.parent/'ch008/production/source'; R=C/'reviewed_source/Chapter9_Reconciled'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,x): p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not (B/'source/layout_config.json').exists(), 'Do not overwrite active geometry'
a=json.loads((R/'acting_units.json').read_text())['units']; d=json.loads((R/'dialogue.json').read_text())['units']
assert [u['unit'] for u in a]==list(range(1,34))==[u['unit'] for u in d]
font=Path('private_fonts/animeace2/animeace2bb_ot/animeace2_reg.otf').resolve();assert font.is_file()
shutil.copy2(R/'CH009_script.md',B/'source/script_v1.md')
assert sha(R/'CH009_script.md')==sha(C/'shared_anchors/provenance/CH009_script.md')
records=[]; layout={}
for unit,dialogue in zip(a,d):
 assert unit['lettering']==[{k:v for k,v in line.items() if k!='order'} for line in dialogue['lines']]
 items=[]
 for line in dialogue['lines']:
  mode=line['mode']; kind=mode if mode in ('caption','sfx') else 'dialogue'
  item={'speaker':line['speaker'],'text':line['text'],'kind':kind,'delivery':mode,'source_order':line['order']}
  if mode in ('phone','radio'): item['transmitted']=True
  items.append(item)
 n=unit['unit'];records.append({'panel':n,'unit':n,'items':items,'acting_and_art_direction':unit})
 layout[str(n)]={'source':None,'crop':None,'art_width':800,'extension':[0,0],'protection_reviewed':False,'protected_boxes':[],'protected_polygons':[],'items':{},'status':'awaiting_art_and_exact_crop_QA'}
raw=B/'raw/B01'; manifest=json.loads((raw/'manifest.json').read_text()); checks=[]
for name,record in json.loads((raw/'SHA256_MANIFEST.json').read_text()).items():
 p=raw/name; assert p.stat().st_size==record['size'] and sha(p)==record['sha256'],name;checks.append(name)
for selected in manifest['selected']:
 n=int(selected['unit'][1:]);p=raw/selected['selected_native'];assert sha(p)==selected['native_sha256']
 crop=selected['crop_xyxy'];scale=800/(crop[2]-crop[0]); layout[str(n)].update(source=str(p.relative_to(B)),crop=crop,status='native_source_staged_independent_QA_pending',source_sha256=sha(p),protected_boxes=[[(v['xyxy'][0]-crop[0])*scale,(v['xyxy'][1]-crop[1])*scale,(v['xyxy'][2]-v['xyxy'][0])*scale,(v['xyxy'][3]-v['xyxy'][1])*scale] for v in selected['protected_regions']],candidate_mouths_native=selected['mouths'],candidate_voice_sources_native=selected.get('voice_source_anchors',{}),native_components=selected.get('components',[]))
write(B/'source/lettering_script.json',{'chapter':9,'title':'The Open Side','script_sha256':sha(R/'CH009_script.md'),'dialogue_json_sha256':sha(R/'dialogue.json'),'panels':records})
write(B/'source/layout_config.json',{'chapter':9,'font_path':str(font),'font_policy':'Local rasterization only. Never copy font programs into deliveries or embed in PDF.','panels':layout})
for name in ('fit_text.py','prepare_text_fit.py'):
 (B/'source'/name).write_text((OLD/name).read_text().replace("'chapter':8","'chapter':9"))
s=(OLD/'build_chapter.py').read_text().replace('range(1,37)','range(1,34)').replace('all36','all33').replace('==36','==33').replace('Chapter 8: The Empty Bit','Chapter 9: The Open Side').replace('END CHAPTER 8','END CHAPTER 9').replace('Chapter_8','Chapter_9').replace("'chapter':8","'chapter':9").replace('(1,9,11,23,35)','(1,5,15,29,33)')
(B/'source/build_chapter.py').write_text(s)
if not (B/'qa/independent_raw_review.json').exists():write(B/'qa/independent_raw_review.json',{'chapter':9,'reviews':[],'required_match':['sha256','panels','crop_xyxy'],'note':'Independent reviewer owns verdicts; assembly never self-approves.'})
write(B/'qa/preparation_preflight.json',{'chapter':9,'exact_text_matches_dialogue':True,'units':33,'text_items':sum(len(p['items']) for p in records),'speech_and_transmitted':sum(i['kind']=='dialogue' for p in records for i in p['items']),'B01_verified_package_files':len(checks),'selected_native_byte_hashes_verified':True,'script_matches_shared_anchor_source':True,'font_file_sha256':sha(font),'font_programs_copied':False,'art_generated':False,'render_started':False})
write(B/'source/preparation_provenance.json',{'renderer_source':str(OLD/'build_chapter.py'),'renderer_source_sha256':sha(OLD/'build_chapter.py'),'reviewed_package_library_id':'libfile_09ee4397a04081919cb49cfb0f47167a','B01_library_id':'libfile_1ca1b04a7d848191ae41399bcf2cd7fd','approved_anchor_package_library_id':'libfile_a28120140f8081919c9d9cbda1f28916','batch_status':{'B01':'staged; independent QA pending','B02':'completed remotely; Library401 unavailable; do not regenerate','B03-B09':'not started due cloud service errors'},'policy':'No duplicate art, no own raw acceptance, no font programs, no publication.'})
print('Prepared 33 acting units and',sum(len(p['items']) for p in records),'exact text items; verified',len(checks),'B01 files.')
