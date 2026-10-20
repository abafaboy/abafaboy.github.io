"""Rebuild retained master from source WAVs and verified sample timeline."""
from pathlib import Path
import json,wave,hashlib,subprocess,argparse
p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();assert not a.output.exists(),'Choose a fresh output directory';a.output.mkdir(parents=True)
r=Path(__file__).resolve().parents[1];t=json.loads((r/'assets/timing.private.json').read_text());recs={x['id']:x for x in json.loads((r/'recordings/recordings.json').read_text())['recordings']};out=bytearray(t['duration_samples']*2)
for ln in t['lines']:
 rec=recs[ln['id']];f=r/'recordings'/rec['wav'];assert hashlib.sha256(f.read_bytes()).hexdigest()==ln['sha256']
 with wave.open(str(f)) as w:assert w.getparams()[:3]==(1,2,t['sample_rate']);pcm=w.readframes(w.getnframes())
 assert len(pcm)==(ln['end_sample']-ln['start_sample'])*2;out[ln['start_sample']*2:ln['end_sample']*2]=pcm
with wave.open(str(a.output/'audio.wav'),'wb') as w:w.setparams((1,2,t['sample_rate'],0,'NONE','not compressed'));w.writeframes(out)
subprocess.run(['ffmpeg','-v','error','-i',str(a.output/'audio.wav'),'-codec:a','libmp3lame','-b:a','128k',str(a.output/'audio.mp3')],check=True)
assert (a.output/'audio.wav').read_bytes()==(r/'assets/ch/006/audio.wav').read_bytes();print('Reconstructed PCM matches retained master exactly.')
