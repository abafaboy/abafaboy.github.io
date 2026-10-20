from pathlib import Path
import hashlib,json,re
ROOT=Path(__file__).resolve().parent
PROJECT=ROOT.parent
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
source_files=[PROJECT/'planning'/f'PRIVATE_story_architecture_v{i}.md' for i in (1,2,3)]
source_files += [PROJECT/'reconcile_009_015/dispatch_r3'/f'CH{n:03d}'/f'CH{n:03d}_script.md' for n in range(10,16)]
source_files += [PROJECT/'reconcile_009_015/dispatch_r3'/p for p in ('CROSS_CHAPTER_LOCK.md','APPROVAL_STATUS.json','reviews/EXPORT_AND_JOIN_REVIEW.md')]
source_files += [PROJECT/f'ch{n:03d}/script_v1.md' for n in range(3,9)]
sources=[{'path':str(p.relative_to(PROJECT)),'sha256':h(p),'use':'provenance_only' if p.name in ('PRIVATE_story_architecture_v1.md','PRIVATE_story_architecture_v2.md') else 'continuity_or_reference'} for p in source_files if p.exists()]
(ROOT/'SOURCE_HASHES.json').write_text(json.dumps(sources,indent=2)+'\n')
validation=[]
for ch in (16,17):
    d=ROOT/f'CH{ch:03d}'; p=d/f'CH{ch:03d}_script.md'; s=p.read_text(); sha=h(p)
    matches=list(re.finditer(r'^### (U\d{2})\n',s,re.M)); units=[]; dialogue=[]
    for i,m in enumerate(matches):
        end=matches[i+1].start() if i+1<len(matches) else s.index(f'END CHAPTER {ch}')
        body=s[m.end():end].strip()
        body=re.split(r'\n## Scene ',body)[0].strip()
        lines=[{'speaker_and_delivery':x[0],'text':x[1]} for x in re.findall(r'^\*\*([^*]+):\*\* (.+)$',body,re.M)]
        unit={'unit_id':m[1],'source_text':body,'lines':lines}; units.append(unit)
        for j,line in enumerate(lines): dialogue.append({'unit_id':m[1],'line_id':f'CH{ch:03d}-{m[1]}-L{j+1:02d}',**line})
    assert [u['unit_id'] for u in units]==[f'U{i:02d}' for i in range(1,len(units)+1)]
    (d/'EXACT_UNIT_SOURCE.json').write_text(json.dumps({'chapter':ch,'source':p.name,'sha256':sha,'status':'PRIVATE_PLANNING_ONLY','units':units},indent=2,ensure_ascii=False)+'\n')
    (d/'dialogue.json').write_text(json.dumps({'source_sha256':sha,'lines':dialogue},indent=2,ensure_ascii=False)+'\n')
    briefs=d/'batch_briefs'; briefs.mkdir(exist_ok=True)
    for stale in briefs.glob('*.md'): stale.unlink() # r1 retained under provenance_r1 before regeneration
    ranges=([(1,3),(4,6),(7,10),(11,14),(15,18),(19,22)] if ch==16 else [(1,4),(5,8),(9,12),(13,15),(16,18),(19,21)])
    index=[]; assigned=[]
    for num,(a,b) in enumerate(ranges,1):
        batch=units[a-1:b]; ids=[u['unit_id'] for u in batch]; assigned+=ids
        name=f'B{num:02d}_U{a:02d}_U{b:02d}.md'
        content=f'# Chapter {ch} planning batch {num}\n\nPRIVATE; not an art commission. Source: {p.name}\nSHA256: {sha}\n\nRead the full common staging, CONTINUITY_LEDGER.md, REFERENCE_DEPENDENCIES.md and current review status. No new reference/art generation or publication. These {len(batch)} units are small acting beats, not equal pages. Exact source below controls, including dialogue delivery; do not omit quiet actions or introduce tiny mandatory UI text. Preserve complete preceding/following prop states.\n\n'
        content+='\n\n'.join('## '+u['unit_id']+'\n\n'+u['source_text'] for u in batch)+'\n'
        (briefs/name).write_text(content)
        index.append({'batch':f'B{num:02d}','file':'batch_briefs/'+name,'unit_ids':ids,'source_sha256':sha,'status':'PLANNING_NOT_RELEASED'})
    assert assigned==[u['unit_id'] for u in units]
    (d/'batch_index.json').write_text(json.dumps(index,indent=2)+'\n')
    validation.append({'chapter':ch,'script_sha256':sha,'units':len(units),'dialogue_and_caption_lines':len(dialogue),'briefs':len(index),'exact_unit_order':True,'nonoverlapping_complete_batch_coverage':True,'export_status':'MECHANICALLY_VALIDATED_NOT_INDEPENDENTLY_CERTIFIED'})
(ROOT/'EXPORT_VALIDATION.json').write_text(json.dumps(validation,indent=2)+'\n')
# Exclude this changing manifest itself; include all current documents and preserved reviews.
manifest={str(p.relative_to(ROOT)):h(p) for p in sorted(ROOT.rglob('*')) if p.is_file() and p.name!='SHA256_MANIFEST.json'}
(ROOT/'SHA256_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(validation,indent=2))
