from pathlib import Path
import re,json,hashlib
O=Path(__file__).resolve().parents[1]; s=(O/'source/script_v2.md').read_text()
ps=[]
for m in re.finditer(r'\*\*Panel (\d+)\*\*\n(.*?)(?=\*\*Panel \d+\*\*|\*\*END CHAPTER 2\*\*)',s,re.S):
 n=int(m[1]);body=m[2];items=[]
 for line in body.splitlines():
  speaker=re.fullmatch(r'\*\*([^*]+):\*\* (.+)',line)
  sfx=re.fullmatch(r'SFX: \*\*(.+)\*\*',line)
  ui=re.fullmatch(r'\*\*(.+)\*\*',line)
  if speaker:
   who,words=speaker.groups();kind='phone' if ', TEXT' in who else 'dialogue'
   items.append({'kind':kind,'speaker':who,'text':words,'transmitted':('SIBLING' in who or 'PHONE' in who) and 12<=n<=18,'off_panel':'OFF PANEL' in who or 'OFF PHONE' in who})
  elif sfx:items.append({'kind':'sfx','text':sfx[1]})
  elif ui:items.append({'kind':'ui' if ui[1].startswith('[') else 'phone_info','text':ui[1]})
 ps.append({'panel':n,'direction':body.strip(),'items':items})
assert len(ps)==61
out={'title':'My Summons Go First','chapter':2,'chapter_title':'A Place to Sit','script_sha256':hashlib.sha256(s.encode()).hexdigest(),'panels':ps}
(O/'source/lettering_script.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
print(len(ps),'panels',sum(len(p['items']) for p in ps),'lettering items')
