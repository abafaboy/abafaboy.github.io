#!/usr/bin/env python3
"""judge_pack: turn a lettered chapter (autostrip2 output) into a reading pack for the independent chapter judge.

usage: judge_pack.py OUT_DIR RECAP_JSON PACK_DIR [--max 1500]

- Reads OUT_DIR/strip.png and OUT_DIR/layout.json, scales the strip to its layout width (1080 px),
  and cuts it into pages at most --max px tall, cutting in the gutters (never through a balloon if it can help it).
- Writes PACK_DIR/page_NN_Pxx-Pyy.jpg in reading order, PACK_DIR/narration.md (the narrator's lines, panel by panel,
  with the page each panel is on) and PACK_DIR/index.md.
"""
import argparse, json
from pathlib import Path
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

ap = argparse.ArgumentParser()
ap.add_argument("out"); ap.add_argument("recap"); ap.add_argument("pack")
ap.add_argument("--max", type=int, default=1500)
A = ap.parse_args()
out, pack = Path(A.out), Path(A.pack)
pack.mkdir(parents=True, exist_ok=True)
for f in pack.glob("page_*.jpg"): f.unlink()
L = json.loads((out / "layout.json").read_text())
W, H = L["width"], L["height"]
im = Image.open(out / "strip.png").convert("RGB")
if im.width != W:
    im = im.resize((W, round(im.height * W / im.width)), Image.LANCZOS)
panels = sorted(L["panels"], key=lambda p: p["y_top"])
balloons = [(l["y_top"], l["y_bottom"]) for l in L.get("lines", []) if "y_top" in l]
arts = [(p["y_top"], p["y_bottom"]) for p in panels]
def inside(y, spans): return any(a - 6 <= y <= b + 6 for a, b in spans)
def cut_after(start):
    """the lowest y <= start+max that is in a gutter (no art, no balloon); else not in a balloon; else start+max"""
    hi = min(H, start + A.max)
    if hi >= H: return H
    for ok in (lambda y: not inside(y, arts) and not inside(y, balloons), lambda y: not inside(y, balloons)):
        for y in range(hi, start + 300, -4):
            if ok(y): return y
    return hi
where, files = {}, []
y, n = 0, 0
while y < H:
    y2 = cut_after(y)
    ids = [p["id"] for p in panels if p["y_bottom"] > y and p["y_top"] < y2]
    n += 1
    tag = f"{ids[0]}-{ids[-1]}" if ids else "no-art"
    name = f"page_{n:02d}_{tag}.jpg"
    im.crop((0, y, W, y2)).save(pack / name, quality=88)
    files.append((name, ids))
    for i_ in ids: where.setdefault(i_, name)
    y = y2
recap = json.loads(Path(A.recap).read_text())
lines = [f"# Narration, chapter {L['chapter']}: {L['title']}\n",
         "What the YouTube narrator reads aloud while the strip scrolls, panel by panel, in order.\n"]
for e in recap:
    lines.append(f"- **{e['panel']}** (on `{where.get(e['panel'], '?')}`): {e['text']}")
(pack / "narration.md").write_text("\n".join(lines) + "\n")
idx = [f"# Chapter {L['chapter']}: {L['title']}: reading pack\n", f"{len(files)} pages, read them in this order:\n"]
idx += [f"{i+1}. `{f}`: panels {', '.join(ids) if ids else '(no art: captions or gutter only)'}" for i, (f, ids) in enumerate(files)]
(pack / "index.md").write_text("\n".join(idx) + "\n")
print(len(files), "pages ->", pack)
