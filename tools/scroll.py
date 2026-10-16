"""Scroll a webtoon strip in sync with the voice timeline."""
import builtins as _b
def open(f, mode='r', *a, **k):  # UTF-8 everywhere (Windows defaults to cp1252)
    if 'b' not in mode and 'encoding' not in k: k['encoding'] = 'utf-8'
    return _b.open(f, mode, *a, **k)
import json, sys, subprocess, numpy as np
from PIL import Image

D = sys.argv[1]; OUTF = sys.argv[2]; LAST = int(sys.argv[3])
A = json.load(open(f"{D}/anchors.json"))
tl = json.load(open(f"{D}/../timeline.json"))["lines"][:LAST + 1]
strip = Image.open(f"{D}/strip.png").convert("RGB")
W, SH = strip.size
VH = 1920; FPS = 30
END = tl[-1]["end"] + 2.0

# (time, anchor) keyframes: line i -> anchor "L{i}"; "L{i}b" (and "L{i}c") split the line; missing anchors hold position
keys = []
for ln in tl:
    i = ln["i"]; dur = ln["end"] - ln["start"]
    if f"L{i}" in A: keys.append((max(0, ln["start"] - 0.35), f"L{i}"))
    subs = [x for x in ("b", "c") if f"L{i}{x}" in A]
    for k, x in enumerate(subs):
        keys.append((ln["start"] + dur * (k + 1) / (len(subs) + 1) + 0.1, f"L{i}{x}"))
keys.sort(); keys[0] = (0.0, keys[0][1])
def centre(a):
    e = A[a]; c = e["top"] + e["h"] / 2
    return min(max(c - VH / 2, 0), SH - VH)

ys = [(t, centre(a)) for t, a in keys]
MOVE = 1.1
def y_at(t):
    y = ys[0][1]
    for (t0, y0), (t1, y1) in zip(ys, ys[1:]):
        if t < t1: break
        y = y1
    # find active transition
    for k in range(1, len(ys)):
        t1, y1 = ys[k]; y0 = ys[k - 1][1]
        if t1 <= t < t1 + MOVE:
            u = (t - t1) / MOVE; u = u * u * (3 - 2 * u)
            return y0 + (y1 - y0) * u
    return y

n = int(END * FPS)
p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{VH}", "-r", str(FPS), "-i", "-",
                      "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p", f"{D}/scroll_v.mp4"], stdin=subprocess.PIPE)
arr = np.asarray(strip)
for f in range(n):
    y = int(round(y_at(f / FPS)))
    p.stdin.write(arr[y:y + VH].tobytes())
p.stdin.close(); p.wait()

AUD = sys.argv[4]
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", f"{D}/scroll_v.mp4", "-i", AUD, "-map", "0:v", "-map", "1:a",
                "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", "-t", f"{END:.2f}", OUTF], check=True)
print("ok", END, SH)
