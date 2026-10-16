import builtins as _b
def open(f, mode='r', *a, **k):  # UTF-8 everywhere (Windows defaults to cp1252)
    if 'b' not in mode and 'encoding' not in k: k['encoding'] = 'utf-8'
    return _b.open(f, mode, *a, **k)
import json, sys, numpy as np, soundfile as sf
from kokoro_onnx import Kokoro

base = sys.argv[1]
dl = sys.argv[2]
script = json.load(open(f"{base}/script.json"))
k = Kokoro(f"{dl}/kokoro-v1.0.int8.onnx", f"{dl}/voices.bin")
SR = 24000
speeds = {k: 1.0 for k in script["voices"]}

out = [np.zeros(int(SR * 0.8), dtype=np.float32)]
t = 0.8
timeline = []
for i, ln in enumerate(script["lines"]):
    v = script["voices"][ln["who"]]
    audio, sr = k.create(ln["text"], voice=v, speed=speeds[ln["who"]], lang="en-us" if v.startswith("a") else "en-gb")
    assert sr == SR
    dur = len(audio) / SR
    timeline.append({"i": i, "panel": ln["panel"], "who": ln["who"], "start": round(t, 3), "end": round(t + dur, 3), "text": ln["text"]})
    out.append(audio.astype(np.float32))
    gap = ln.get("pause_after", 0.45)
    out.append(np.zeros(int(SR * gap), dtype=np.float32))
    t += dur + gap
    print(i, ln["who"], round(dur, 2), flush=True)

full = np.concatenate(out)
sf.write(f"{base}/voice.wav", full, SR)
json.dump({"total": round(t, 3), "lines": timeline}, open(f"{base}/timeline.json", "w"), indent=1)
print("total", round(t, 1))
