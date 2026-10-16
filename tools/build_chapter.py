"""Build one chapter end to end.
usage:  py tools/build_chapter.py N            # strip check -> voice -> mix -> video -> final folder -> site
        py tools/build_chapter.py N --strip-only   # just render the strip + face/overlap check + preview
Paths come from config.json at the repo root."""
import json, os, sys, shutil, subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; T = ROOT / "tools"
cfg = json.load(open(ROOT / "config.json", encoding="utf-8"))
VID = Path(cfg["videos_root"]); PY = sys.executable
n = int(sys.argv[1]); strip_only = "--strip-only" in sys.argv
ch = ROOT / "chapters" / f"ch{n:03d}"; full = ch / "full"; full.mkdir(exist_ok=True)
art = VID / f"ch{n}"; end = VID / "ch1_v2" / "c33.png"
def run(args, **kw):
    r = subprocess.run([str(a) for a in args], capture_output=True, text=True, **kw)
    if r.returncode: print(r.stdout[-2000:], r.stderr[-3000:]); sys.exit(f"FAILED: {args[1]}")
    return r.stdout
out = run([PY, T / "strip.py", art, ROOT / "assets" / "fonts", full, ch / "layout.py", end], cwd=T)
print(out.strip())
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
im = Image.open(full / "strip.png"); W, H = im.size; k = 4; h = H // k
pv = Image.new("RGB", (k * 270, h // 4), "white")
for i in range(k): pv.paste(im.crop((0, i * h, W, (i + 1) * h)).resize((270, h // 4)), (i * 270, 0))
pv.save(full / "preview.jpg", quality=70); print("preview:", full / "preview.jpg")
if "OVERLAPS: none" not in out: sys.exit("Fix the overlaps listed above, then run again.")
if strip_only: sys.exit(0)
if not (ch / "voice.wav").exists():
    print("voicing..."); run([PY, T / "tts.py", ch, ROOT / "dl"], cwd=T)
print("mixing..."); run([PY, T / "mix.py", ch, VID / "sfx", full / "mix.wav", "-1", ch / "sound.py"], cwd=T)
lines = json.load(open(ch / "script.json", encoding="utf-8"))["lines"]
mp4 = full / f"The_Lord_Who_Measured_Zero_Ch{n}.mp4"
print("rendering..."); run([PY, T / "scroll.py", full, mp4, len(lines) - 1, full / "mix.wav"], cwd=T)
(VID / "final").mkdir(exist_ok=True); shutil.copy(mp4, VID / "final" / mp4.name)
tl = json.load(open(ch / "timeline.json", encoding="utf-8"))["lines"]
cp = VID / "briefs" / "volume_cuts.json"; cuts = json.load(open(cp, encoding="utf-8")) if cp.exists() else {}
cuts[str(n)] = round(tl[-1]["start"] - 0.45, 2); json.dump(cuts, open(cp, "w", encoding="utf-8"), indent=1)
run([PY, T / "site_export.py", n], cwd=T)
(ch / "STATUS_BUILT").write_text("built\n")
print("DONE", mp4.name, round(mp4.stat().st_size / 1e6, 1), "MB -> final, site exported")
