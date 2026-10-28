#!/usr/bin/env python3
"""link_art: build a chapter's letterer art folder out of symlinks, so the art is never copied a third time.

usage: link_art.py N [--dry-run]

For chapter N it fills /home/claude/work/chNNN/art/ with one symlink per top-level PNG and REVIEW_*.json:
  - to the file in msgf-art (chapters_v2/chNNN/art/) when Claude has a fixed or approved copy there;
  - otherwise to the copy staged from the laptop (/mnt/user-data/uploads/.../chapters_v2/chNNN/art/).
Real files already in the work folder are replaced by links only when they are byte-identical to the link target
(so nothing Claude made there is lost). Prints what it linked.
From chapter 11 on, msgf-art holds only the panels Claude changed (and the REVIEW files); the laptop holds the rest.
"""
import filecmp
import os
import sys
from pathlib import Path

n = int(sys.argv[1])
dry = "--dry-run" in sys.argv
c = f"ch{n:03d}"
ART = Path("/home/claude/msgf-art/chapters_v2") / c / "art"
UP = Path("/mnt/user-data/uploads/Videos/MySummonsGoFirst/chapters_v2") / c / "art"
DST = Path("/home/claude/work") / c / "art"
DST.mkdir(parents=True, exist_ok=True)

names = set()
for src in (UP, ART):
    if src.is_dir():
        for f in src.iterdir():
            if f.is_file() and (f.suffix == ".png" or (f.name.startswith("REVIEW_") and f.suffix == ".json")):
                names.add(f.name)

linked = kept = 0
for name in sorted(names):
    target = ART / name if (ART / name).exists() else UP / name
    d = DST / name
    if d.is_symlink():
        if os.readlink(d) == str(target):
            continue
        if not dry:
            d.unlink()
    elif d.exists():
        if filecmp.cmp(d, target, shallow=False):
            if not dry:
                d.unlink()
        else:
            print(f"kept real file (differs from {target}): {d}")
            kept += 1
            continue
    if not dry:
        d.symlink_to(target)
    linked += 1
print(f"{c}: {linked} links made or updated, {kept} real files kept, {len(names)} names")
