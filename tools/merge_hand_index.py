#!/usr/bin/env python3
"""merge_hand_index: merge the per-chat hand reference indexes (INDEX_H1A.md ... INDEX_H2D.md) into INDEX.md.

usage: merge_hand_index.py STAGED_HANDS_DIR OUT_INDEX.md [--approved name.png ...] [--rejected name.png ...]
Reads every INDEX_H*.md in STAGED_HANDS_DIR (staged copies of characters_v2/hands/), keeps their lines in job order
and writes one INDEX.md: a header, then one section per job. Files Claude rejected are marked "(REDO: do not use)".
"""
import re
import sys
from pathlib import Path

src, out = Path(sys.argv[1]), Path(sys.argv[2])
args = sys.argv[3:]
approved, rejected, mode = set(), set(), None
for a in args:
    if a in ("--approved", "--rejected"):
        mode = a
    elif mode == "--approved":
        approved.add(a)
    elif mode == "--rejected":
        rejected.add(a)
files = sorted(src.glob("INDEX_H*.md"), key=lambda p: p.name)
L = ["# Hand and arm references (index)", "",
     "Realistic references for hands and arms (`HANDS_REFERENCE_BRIEF.md`, jobs H1 and H2). Pass the matching file as a hand "
     "reference whenever a hand grips, points, holds or touches (`PANEL_BRIEF_v2.md` 4c). Take anatomy, grip and pose from "
     "them; draw the hand in the house style.", ""]
for f in files:
    job = re.sub(r"^INDEX_|\.md$", "", f.name)
    L.append(f"## {job}")
    for line in f.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        m = re.search(r"`?([a-z0-9_]+\.png)`?", line)
        if m and m.group(1) in rejected:
            line = line + " **(REDO: do not use)**"
        L.append(line)
    L.append("")
out.write_text("\n".join(L) + "\n", encoding="utf-8")
print(f"merged {len(files)} indexes into {out}")
