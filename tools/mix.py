"""Mix voice + scheduled music cues + scheduled SFX, with music ducking under speech."""
import builtins as _b
def open(f, mode='r', *a, **k):  # UTF-8 everywhere (Windows defaults to cp1252)
    if 'b' not in mode and 'encoding' not in k: k['encoding'] = 'utf-8'
    return _b.open(f, mode, *a, **k)
import json, sys, os, subprocess, tempfile, numpy as np, soundfile as sf
sys.path.insert(0, os.path.dirname(__file__))
import cues
from music import SR

B = sys.argv[1]; SFX = sys.argv[2]; OUT = sys.argv[3]; LAST = int(sys.argv[4]); SOUND = sys.argv[5]
if LAST < 0: LAST = 10**6
tl = json.load(open(f"{B}/timeline.json"))["lines"][:LAST + 1]
END = tl[-1]["end"] + 2.0
N = int(END * SR)

def load(path):
    tmp = os.path.join(tempfile.gettempdir(), f"_mix_{os.path.basename(path)}.wav")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", path, "-ar", str(SR), "-ac", "2", tmp], check=True)
    x, _ = sf.read(tmp, dtype="float32"); return x

def at(i, frac=0.0):
    l = tl[i]; return l["start"] + (l["end"] - l["start"]) * frac

def frac_after(i, phrase):
    t = tl[i]["text"]; return (t.index(phrase) + len(phrase)) / len(t)

def place(buf, x, t, gain=1.0, fade_in=0.05, fade_out=0.5, length=None):
    x = x.copy()
    if length: x = x[:int(length * SR)]
    fi, fo = int(fade_in * SR), min(int(fade_out * SR), len(x))
    if fi: x[:fi] *= np.linspace(0, 1, fi)[:, None]
    if fo: x[-fo:] *= np.linspace(1, 0, fo)[:, None]
    i = int(t * SR); j = min(N, i + len(x))
    buf[i:j] += x[:j - i] * gain

# ---------- music ----------
mus = np.zeros((N, 2), np.float32)
def M(cue, t0, t1, gain=1.0, fade_in=0.4, fade_out=1.0, **kw):
    """place cue from t0 to t1 (seconds), rendered to fit"""
    place(mus, getattr(cues, cue)(t1 - t0 + fade_out, **kw), t0, gain, fade_in, fade_out)
SCHED = []
# ---------- sfx ----------
fx = np.zeros((N, 2), np.float32)
def S(name, t, gain, length=None, fade_out=0.6, fade_in=0.05):
    for cand in (f"{SFX}/{name}.wav", f"{SFX}/{name}_1.wav"):
        if os.path.exists(cand):
            x = load(cand)
            if length and len(x) < length * SR:   # loop short beds
                x = np.concatenate([x] * (int(length * SR / len(x)) + 1))
            place(fx, x, t, gain, fade_in, fade_out, length); return True
    print("missing sfx", name); return False

exec(open(SOUND).read(), globals())
mus /= np.abs(mus).max() + 1e-9
# ducking envelope: music at 0.42 in gaps, 0.18 under speech, 0.25 s ramps
env = np.full(N, 0.42, np.float32)
for l in tl:
    a, b = int((l["start"] - 0.15) * SR), int((l["end"] + 0.1) * SR)
    env[max(a, 0):b] = 0.18
k = int(0.25 * SR); # Same zero-padded box filter in linear time, including even-kernel alignment.
padded = np.pad(env, (k // 2, (k - 1) // 2))
integral = np.empty(len(padded) + 1, dtype=np.float64)
integral[0] = 0.0
np.cumsum(padded, dtype=np.float64, out=integral[1:])
env = (integral[k:] - integral[:-k]) / k
del padded, integral
mus *= env[:, None]

# ---------- voice ----------
v = load(f"{B}/voice.wav")[:N]
vo = np.zeros((N, 2), np.float32); vo[:len(v)] = v
vo /= np.abs(vo).max() + 1e-9

mixd = vo * 0.85 + mus + fx
fo = int(1.5 * SR); mixd[-fo:] *= np.linspace(1, 0, fo)[:, None]
peak = np.abs(mixd).max()
if peak > 0.97: mixd *= 0.97 / peak
sf.write(OUT, mixd, SR)
print("mixed", round(END, 2), "peak", round(float(peak), 3))
