#!/usr/bin/env python3
"""import_upscales: put 2x upscales made on the laptop's graphics card into a chapter's letterer cache.

usage: import_upscales.py N STAGED_OUT_DIR [--min-match 0.0]

For chapter N, every STAGED_OUT_DIR/<name>.png (realesrgan-ncnn-vulkan -n realesr-animevideov3 -s 2) is checked
against the art the letterer will use (/home/claude/work/chNNN/art/<name>.png):
  - its size must be exactly twice the art's size;
  - shrunk back by half it must match the art closely (mean absolute difference under 9 levels per channel; a genuine upscale gives about 2-5, a different picture 25 or more), so an
    upscale of a stale or different picture is never used.
A file that passes is copied to /home/claude/work/chNNN/out/_work/up/<stem>_x2.png with a fresh mtime (newer than the
art file, so autostrip2.py takes it as a valid cache entry). Prints one line per file and a summary.
"""
import shutil
import sys
import time
from pathlib import Path

import numpy as np
from PIL import Image

n = int(sys.argv[1])
src = Path(sys.argv[2])
c = f"ch{n:03d}"
ART = Path("/home/claude/work") / c / "art"
UP = Path("/home/claude/work") / c / "out" / "_work" / "up"
UP.mkdir(parents=True, exist_ok=True)
ok = bad = missing = 0
for f in sorted(src.glob("*.png")):
    a = ART / f.name
    if not a.exists():
        print(f"{f.name}: no art file of that name, skipped"); missing += 1; continue
    with Image.open(a) as ia, Image.open(f) as iu:
        if iu.size != (ia.width * 2, ia.height * 2):
            print(f"{f.name}: size {iu.size} is not 2x {ia.size}: REJECTED"); bad += 1; continue
        art = np.asarray(ia.convert("RGB"), dtype=np.float32)
        half = np.asarray(iu.convert("RGB").resize(ia.size, Image.BOX), dtype=np.float32)
    mad = float(np.abs(art - half).mean())
    if mad >= 9.0:
        print(f"{f.name}: does not match the art (mean diff {mad:.1f}): REJECTED"); bad += 1; continue
    dst = UP / (Path(f.name).stem + "_x2.png")
    import os
    if dst.exists() or dst.is_symlink():
        dst.unlink()
    if f.stat().st_mtime > a.stat().st_mtime:
        # a link costs no disk (the staged copy can't be deleted); the letterer follows it and sees a fresh mtime
        os.symlink(f.resolve(), dst)
    else:
        shutil.copyfile(f, dst)
        t = max(time.time(), a.stat().st_mtime + 1)
        os.utime(dst, (t, t))
    ok += 1
print(f"{c}: {ok} upscales imported, {bad} rejected, {missing} without art; cache now {len(list(UP.glob('*_x2.png')))} files")
