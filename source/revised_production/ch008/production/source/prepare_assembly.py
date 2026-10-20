"""Initialize Chapter 8 exact text and gate-locked renderer; never approve raw art."""
from pathlib import Path
import json,hashlib,shutil
B=Path(__file__).resolve().parents[1]; C=B.parent; OLD=C.parent/'ch007/production/source'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not (B/'source/layout_config.json').exists()
raw=C/'handoff/Chapter_8/panels_and_dialogue.json'; panels=json.loads(raw.read_text())
assert [p['panel'] for p in panels]==list(range(1,37))
font=Path('private_fonts/animeace2/animeace2bb_ot/animeace2_reg.otf').resolve();assert font.is_file()
for name in ('script_v1.md','CONTINUITY_AND_ART_LOCK.md'):shutil.copy2(C/name,B/'source'/name)
shutil.copy2(raw,B/'source/panels_and_dialogue.json')
shutil.copy2(OLD/'fit_text.py',B/'source/fit_text.py')
records=[];layout={}
for p in panels:
 items=[]
 for d in p['dialogue']:
  who,*delivery=d['speaker_delivery'].split(', ',1)
  item={'speaker':who,'text':d['text'],'kind':'caption' if who=='CAPTION' else ('sfx' if who=='SFX' else 'dialogue'),'speaker_delivery':d['speaker_delivery']}
  if delivery:item['delivery']=delivery[0]
  items.append(item)
 assert not p['native_device_text']
 records.append({'panel':p['panel'],'items':items,'acting_and_art_direction':p['full_script']})
 layout[str(p['panel'])]={'source':None,'crop':None,'art_width':800,'extension':[0,0],'protection_reviewed':False,'protected_boxes':[],'protected_polygons':[],'items':{},'status':'awaiting_art_and_exact_crop_QA'}
write(B/'source/lettering_script.json',{'chapter':8,'title':'The Empty Bit','script_sha256':sha(C/'script_v1.md'),'dialogue_json_sha256':sha(raw),'panels':records})
write(B/'source/layout_config.json',{'chapter':8,'font_path':str(font),'font_policy':'Local rasterization only. Never copy font programs into deliveries or embed in PDF.','panels':layout})
if not (B/'qa/independent_raw_review.json').exists():write(B/'qa/independent_raw_review.json',{'chapter':8,'reviews':[],'required_match':['sha256','panels','crop_xyxy'],'note':'Independent reviewer fills verdicts; assembly must never self-approve.'})
s=(OLD/'build_chapter.py').read_text().replace('range(1,35)','range(1,37)').replace('all34','all36').replace('==34','==36').replace('Chapter 7: Twenty Thousand Won','Chapter 8: The Empty Bit').replace('END CHAPTER 7','END CHAPTER 8').replace('Chapter_7','Chapter_8').replace("'chapter':7","'chapter':8")
s=s.replace('gutter=100 if pair[0][0] in (7,19,21,25,27) else 64','gutter=100 if pair[0][0] in (1,9,11,23,35) else 64')
(B/'source/build_chapter.py').write_text(s)
s=(OLD/'prepare_text_fit.py').read_text().replace("'chapter':7","'chapter':8");(B/'source/prepare_text_fit.py').write_text(s)
write(B/'source/preparation_provenance.json',{'renderer_source':str(OLD/'build_chapter.py'),'renderer_source_sha256':sha(OLD/'build_chapter.py'),'font_file_sha256':sha(font),'dialogue_count':sum(x['kind']=='dialogue' for p in records for x in p['items']),'caption_count':sum(x['kind']=='caption' for p in records for x in p['items']),'fonts_copied':False,'art_generated':False,'render_started':False})
print('Prepared',len(records),'units;',sum(len(p['items']) for p in records),'text items.')
