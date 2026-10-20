from pathlib import Path
from PIL import Image
import json,shutil,wave,hashlib,subprocess
R=Path(__file__).resolve().parent; P=R.parent/'production'; prep=R/'Chapter_6_Private_Narration_Preparation'; O=R/'Chapter_6_Private_Integration'; O.mkdir(exist_ok=True)
for d in ['tools','timing','qa','assets/ch/006','voices']: (O/d).mkdir(parents=True,exist_ok=True)
def save(p,x): p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
geo=json.loads((P/'lettered/placement_manifest.json').read_text()); lines=json.loads((prep/'timing/dialogue.json').read_text())['lines']; records=json.loads((prep/'recordings/recordings.json').read_text())['recordings']; lookup={r['id']:r for r in records}
shutil.copytree(prep/'recordings',O/'recordings',dirs_exist_ok=True);shutil.copytree(prep/'voices',O/'voices',dirs_exist_ok=True);shutil.copytree(prep/'qa',O/'qa/preparation',dirs_exist_ok=True)
shutil.copy2(P/'lettered/placement_manifest.json',O/'timing/placement_manifest.json');shutil.copy2(R/'final_reuse_mapping.json',O/'qa/final_reuse_mapping.json')
segments=[]; panelmap={}; pages=[]
for pg in geo['pages']:
 n=pg['page']; fn=f'{n:03}.jpg'; im=Image.open(P/f'lettered/reader/page_{n:02}.png').convert('RGB'); assert list(im.size)==pg['size'];im.save(O/f'assets/ch/006/{fn}',quality=95,subsampling=0)
 segments.append([fn,im.height]); pages.append({'page':n,'file':fn,'size_master':pg['size']})
 for p in pg['panels']: panelmap[p['panel']]={**p,'segment':fn,'page':n}
newlines=[]; panels=[]; geomdialog=[]; wrapped=[]
for p in geo['panels']:
 pn=p['panel']; pm=panelmap[pn]; ids=[];prev=pm['offset_y']
 for i,item in enumerate(p['items']):
  if item['kind']!='dialogue':continue
  orig=next(x for x in lines if x['panel']==pn and x['source_item_index']==i); assert orig['text']==item['text'] and orig['speaker']==item['speaker'].split(',')[0]
  x,y,w,h=item['box']; y+=pm['offset_y'];focus=max(prev,y+h);clamped=focus>y+h;prev=focus
  ln={**orig,'segment':pm['segment'],'page':pm['page'],'box':[x,y,w,h],'raw_lower_edge_y':y+h,'focus_y':focus,'monotonic_clamp':clamped};newlines.append(ln);ids.append(ln['id'])
  geomdialog.append({'id':ln['id'],'panel':pn,'line':i+1,'page':pm['page'],'segment':pm['segment'],'box':[x,y,w,h],'line_bounds':[[bx,by+pm['offset_y'],bw,bh] for bx,by,bw,bh in item['line_bounds']],'focus_y':focus,'monotonic_clamp':clamped})
 panels.append({'panel':pn,'segment':pm['segment'],'page':pm['page'],'y_top':pm['offset_y'],'y_bottom':pm['offset_y']+pm['height'],'lines':ids})
assert len(newlines)==65
save(O/'timing/dialogue.json',{'chapter':6,'lines':newlines});save(O/'timing/panels.json',panels);save(O/'qa/geometry.json',{'pages':pages,'panels':panels,'dialogue':geomdialog})
chapter={'n':6,'title':'The Person Outside','width':800,'segments':segments,'framing_height':max(p['output_size'][1] for p in geo['panels'])}
manifest={'schema_version':1,'edition':2,'slug':'my-summons-go-first','title':'My Summons Go First','chapters':[chapter]}
rate=24000;chunks=[];sample=0;cues=[];timeline=[];holds=[];offsets={};total=0
for f,h in segments:offsets[f]=total;total+=h
last=-1
def pause(s):
 global sample
 n=round(s*rate);chunks.append(bytes(n*2));sample+=n
def cue(seg,y,panel=None,line=None):
 global last
 absolute=offsets[seg]+y;assert absolute>=last;last=absolute
 c={'t':sample/rate,'segment':seg,'y':y}
 if panel:c['panel']=panel
 if line:c['line']=line
 if cues and cues[-1]['t']==c['t']:
  assert cues[-1]['segment']==seg and cues[-1]['y']==y
  cues[-1].update(c)
 else:cues.append(c)
byid={l['id']:l for l in newlines}
cue(segments[0][0],0)
for p in panels:
 pn=p['panel'];seg=p['segment'];interrupt=pn==18
 if pn!=1:cue(seg,p['y_top'],pn)
 pause(.05 if interrupt else .35)
 if not p['lines']:
  cue(seg,p['y_bottom'],pn);start=sample;duration=14 if pn==1 else 5 if pn==41 else 3
  pause(duration);cue(seg,p['y_bottom'],pn);holds.append({'panel':pn,'start':start/rate,'end':sample/rate,'duration':duration,'segment':seg,'y':p['y_bottom']})
 else:
  for k,id in enumerate(p['lines']):
   line=byid[id];r=lookup[id];fn=prep/'recordings'/r['wav'];assert hashlib.sha256(fn.read_bytes()).hexdigest()==r['sha256']
   with wave.open(str(fn)) as w:assert w.getparams()[:3]==(1,2,rate); pcm=w.readframes(w.getnframes())
   cue(seg,line['focus_y'],pn,line['line']);start=sample;chunks.append(pcm);sample+=len(pcm)//2;cue(seg,line['focus_y'],pn,line['line'])
   timeline.append({**line,'samples':len(pcm)//2,'sha256':r['sha256'],'start_sample':start,'end_sample':sample,'start':start/rate,'end':sample/rate})
   pause(.45 if k<len(p['lines'])-1 else .04 if pn==17 else 1.1)
  cue(seg,p['y_bottom'],pn)
 pause(.01 if pn==17 else .15)
pause(1.25);cue(panels[-1]['segment'],panels[-1]['y_bottom'],41)
with wave.open(str(O/'assets/ch/006/audio.wav'),'wb') as w:w.setparams((1,2,rate,0,'NONE','not compressed'));w.writeframes(b''.join(chunks))
subprocess.run(['ffmpeg','-v','error','-y','-i',str(O/'assets/ch/006/audio.wav'),'-codec:a','libmp3lame','-b:a','128k',str(O/'assets/ch/006/audio.mp3')],check=True)
chapter['audio']={'file':'audio.mp3','duration':sample/rate,'cues':cues};save(O/'assets/series.json',manifest);save(O/'assets/timing.private.json',{'sample_rate':rate,'duration_samples':sample,'lines':timeline,'test_only':False,'visual_holds':holds,'pacing':{'line_gap_seconds':.45,'panel_tail_seconds':1.1,'panel_gap_seconds':.15,'dialogue_lead_seconds':.35,'P17_to_P18_gap_seconds':.10,'screen_text_policy':'visual-only'}})
ref=R/'reference/Chapter_5_Private_Integration/tools/write_vtt.py';text=ref.read_text().replace('56','65').replace('Chapter 5','Chapter 6');(O/'tools/write_vtt.py').write_text(text)
subprocess.run(['python',str(O/'tools/write_vtt.py'),'--package',str(O),'--timing',str(O/'assets/timing.private.json'),'--output',str(O/'assets/ch/006/captions.vtt')],check=True)
shutil.copy2(__file__,O/'tools/build_final.py')
save(O/'qa/build_summary.json',{'dialogue_records':65,'panels':41,'segments':len(segments),'cues':len(cues),'duration':sample/rate,'framing_height':chapter['framing_height'],'subjective_audition':'not performed','ASR':'retained from preparation; not subjective audition','runtime_Follow_QA':'pending'})
print(json.dumps({'duration':sample/rate,'cues':len(cues),'panels':len(panels),'output':str(O)}))
