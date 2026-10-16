"""Export chapters into the GitHub Pages reader (the site repo's manhwa/ folder): py tools/site_export.py N [N ...]"""
import json, os, sys, subprocess
from pathlib import Path
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
ROOT = Path(__file__).resolve().parents[1]
cfg = json.load(open(ROOT / "config.json", encoding="utf-8"))
VID = Path(cfg["videos_root"]); OUT = Path(cfg["site_root"]) / "manhwa"; SEG = 2400
mp = OUT / "data" / "chapters.json"; mp.parent.mkdir(parents=True, exist_ok=True)
meta = json.load(open(mp, encoding="utf-8")) if mp.exists() else {"chapters": []}
byn = {c["n"]: c for c in meta["chapters"]}
for n in map(int, sys.argv[1:]):
    ch = ROOT / "chapters" / f"ch{n:03d}"; sc = json.load(open(ch / "script.json", encoding="utf-8"))
    title = sc["chapter"].split(":", 1)[1].strip()
    od = OUT / "ch" / f"{n:03d}"; od.mkdir(parents=True, exist_ok=True)
    for f in od.iterdir(): f.unlink()
    im = Image.open(ch / "full" / "strip.png").convert("RGB"); W, H = im.size; segs = []
    for k, y in enumerate(range(0, H, SEG)):
        part = im.crop((0, y, W, min(H, y + SEG))); fn = f"{k + 1:03d}.webp"
        part.save(od / fn, "WEBP", quality=80, method=5); segs.append([fn, part.size[1]])
    th = None
    for ln in sc["lines"]:
        c = VID / f"ch{n}" / f"{ln['panel']}.png"
        if c.exists():
            a = Image.open(c).convert("RGB")
            if a.size[0] > a.size[1]: th = a; break
    if th is None: th = im.crop((0, 600, W, 600 + int(W * 0.75)))
    tw, thh = th.size
    if tw / thh > 4 / 3: nw = int(thh * 4 / 3); th = th.crop(((tw - nw) // 2, 0, (tw - nw) // 2 + nw, thh))
    else: nh = int(tw * 3 / 4); th = th.crop((0, (thh - nh) // 2, tw, (thh - nh) // 2 + nh))
    th.resize((480, 360), Image.LANCZOS).save(od / "thumb.webp", "WEBP", quality=80)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(ch / "full" / "mix.wav"), "-c:a", "libmp3lame", "-b:a", "96k", "-ac", "2", str(od / "audio.mp3")], check=True)
    tl = json.load(open(ch / "timeline.json", encoding="utf-8"))["lines"]
    A = json.load(open(ch / "full" / "anchors.json", encoding="utf-8")); keys = []
    for ln in tl:
        i = ln["i"]; d = ln["end"] - ln["start"]
        if f"L{i}" in A: keys.append((max(0, ln["start"] - 0.35), f"L{i}"))
        subs = [x for x in ("b", "c") if f"L{i}{x}" in A]
        for k, x in enumerate(subs): keys.append((ln["start"] + d * (k + 1) / (len(subs) + 1) + 0.1, f"L{i}{x}"))
    keys.sort()
    byn[n] = {"n": n, "title": title, "segments": segs, "width": W, "height": H, "duration": round(tl[-1]["end"], 1),
              "keys": [[round(t, 2), round(A[a]["top"] + A[a]["h"] / 2)] for t, a in keys]}
    print("exported", n, title, len(segs), "segments")
meta["chapters"] = [byn[k] for k in sorted(byn)]
json.dump(meta, open(mp, "w", encoding="utf-8"), indent=1)
