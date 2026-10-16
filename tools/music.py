"""Tiny sample-based composer: original modal cues rendered with FluidR3 instrument samples."""
import numpy as np, soundfile as sf, functools, os

SF = os.path.join(os.path.dirname(__file__), "..", "sf")
SR = 44100
NAMES = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
PLUCKED = {"orchestral_harp", "acoustic_guitar_nylon", "harpsichord", "pizzicato_strings", "timpani", "tubular_bells"}

def m(note):
    """'D4' / 'F#3' / 'Bb2' -> midi number"""
    n, o = note[:-1], int(note[-1])
    n = {'C#': 'Db', 'D#': 'Eb', 'F#': 'Gb', 'G#': 'Ab', 'A#': 'Bb'}.get(n, n)
    return 12 * (o + 1) + NAMES.index(n)

@functools.lru_cache(maxsize=None)
def sample(inst, midi):
    # nearest available sample, pitch-shifted by resampling if needed
    for d in [0, 1, -1, 2, -2, 3, -3, 12, -12]:
        mm = midi + d
        f = f"{SF}/{inst}/{NAMES[mm % 12]}{mm // 12 - 1}.mp3"
        if os.path.exists(f):
            x, sr = sf.read(f, dtype="float32")
            if x.ndim == 1: x = np.stack([x, x], 1)
            if d:
                ratio = 2 ** (-d / 12)
                idx = np.arange(0, len(x) - 1, 1 / ratio)
                x = np.stack([np.interp(idx, np.arange(len(x)), x[:, c]) for c in range(2)], 1).astype(np.float32)
            return x
    raise FileNotFoundError(f"{inst} {midi}")

class Track:
    def __init__(self, seconds):
        self.buf = np.zeros((int(seconds * SR) + SR * 4, 2), np.float32)

    def note(self, inst, note, t, dur, vel=0.6, pan=0.0):
        midi = m(note) if isinstance(note, str) else note
        x = sample(inst, midi).copy()
        rel = 0.25 if inst not in PLUCKED else 0.6
        n = min(len(x), int((dur + rel) * SR))
        x = x[:n]
        if inst not in PLUCKED:
            # sustain longer notes by crossfading a second copy
            need = int((dur + rel) * SR)
            while len(x) < need:
                seg = sample(inst, midi)[int(0.3 * SR):]
                cf = int(0.4 * SR)
                fade = np.linspace(0, 1, cf)[:, None]
                x[-cf:] = x[-cf:] * (1 - fade) + seg[:cf] * fade
                x = np.concatenate([x, seg[cf:need - len(x) + cf]])
            x = x[:need]
            att = min(int(0.04 * SR), len(x))
            x[:att] *= np.linspace(0, 1, att)[:, None]
        r = min(int(rel * SR), len(x))
        x[-r:] *= np.linspace(1, 0, r)[:, None] ** 2
        l, rr = np.cos((pan + 1) * np.pi / 4), np.sin((pan + 1) * np.pi / 4)
        x = x * np.array([l, rr], np.float32) * 1.41 * vel
        i = int(t * SR)
        if i < 0:
            x = x[-i:]; i = 0
            if len(x) == 0: return
        if i >= len(self.buf): return
        x = x[:len(self.buf) - i]
        self.buf[i:i + len(x)] += x

    def chord(self, inst, notes, t, dur, vel=0.4, spread=0.0):
        for k, nn in enumerate(notes):
            self.note(inst, nn, t + k * spread, dur, vel, pan=(k - len(notes) / 2) * 0.15)

def reverb(x, wet=0.25):
    """cheap hall: a few decaying delayed copies, slightly diffused per channel"""
    out = x.copy()
    for d, g in [(0.031, .5), (0.047, .45), (0.071, .4), (0.113, .33), (0.167, .27), (0.233, .2), (0.331, .14), (0.47, .09)]:
        n = int(d * SR)
        out[n:, 0] += x[:-n, 1] * g * wet
        out[n + 37:, 1] += x[:-n - 37, 0] * g * wet
    return out

def save(x, path, peak=0.9):
    x = x / (np.abs(x).max() + 1e-9) * peak
    sf.write(path, x, SR)
