#!/usr/bin/env python3
"""part_table: draft the PANEL_BRIEF_v2 part table for a v2 chapter script.

usage: part_table.py scripts_v2/chNNN.yaml
Splits the art panels into parts of about 6-9 panels at the script's section headers, and lists each part's notable panels.
"""
import re
import sys

import yaml

LETTERS = "ABCDEFGHIJKLMNOP"


def notable(p):
    pid, r, sh = p["id"], p.get("recipe"), p.get("shape")
    out = []
    if p.get("kind") == "title":
        return [f"No art for {pid} (`title`)."]
    if p.get("kind") == "caption":
        return [f"No art for {pid} (`caption`)."]
    if r == "eyes":
        out.append(f"{pid} ECU strip")
    elif sh == "strip":
        out.append(f"{pid} strip")
    if r == "splash":
        out.append(f"{pid} splash")
    if r == "name-card" or p.get("intro"):
        out.append(f"{pid} name card")
    if r in ("plan", "link-view", "chibi", "carry"):
        out.append(f"{pid} `{r}`")
    if r == "monster-reveal":
        out.append(f"{pid} the reveal")
    for u in p.get("ui", []) or []:
        k = u.get("kind", "")
        at = u.get("at") or [0.5, 0.5]
        if k.startswith("system.") and at[1] < 0.3 and sh in ("wide", "tall", "full"):
            out.append(f"{pid} window (keep the top half calm)")
            break
        if k.startswith("phone.") and u.get("on") == "screen":
            out.append(f"{pid} phone screen #00FF00")
            break
        if k == "tv.lowerthird" and u.get("on") == "panel":
            out.append(f"{pid} TV footage (keep the bottom fifth calm)")
            break
    return out


def main(path):
    s = open(path, encoding="utf-8").read()
    d = yaml.safe_load(s)
    panels = d["panels"]
    ids = [p["id"] for p in panels]
    # section starts from the headers
    starts = []
    for m in re.finditer(r"# =+ .*?\((P\d\d)[–-]?(P\d\d)?\) =+", s):
        starts.append(m.group(1))
    groups, cur = [], []
    for p in panels:
        if p.get("kind") == "end":
            continue
        if p["id"] in starts and cur:
            groups.append(cur)
            cur = []
        cur.append(p)
    if cur:
        groups.append(cur)
    # sub-split long groups (count art panels)
    parts = []
    for g in groups:
        art = [p for p in g if p.get("kind") not in ("title", "caption")]
        if len(art) <= 9:
            parts.append(g)
            continue
        n = (len(art) + 7) // 8
        size = -(-len(g) // n)
        for i in range(0, len(g), size):
            parts.append(g[i:i + size])
    # merge tiny parts (<4 art panels) into the previous part
    merged = []
    for g in parts:
        art = [p for p in g if p.get("kind") not in ("title", "caption")]
        if merged and len(art) < 4:
            merged[-1] = merged[-1] + g
        else:
            merged.append(g)
    print("| Part | Panels to draw | Notes |")
    print("|---|---|---|")
    for k, g in enumerate(merged):
        art = [p["id"] for p in g if p.get("kind") not in ("title", "caption")]
        rng = f"{art[0]}–{art[-1]}" if len(art) > 1 else art[0]
        skipped = [p["id"] for p in g if p.get("kind") in ("title", "caption")]
        if skipped and art[0] < skipped[0] < art[-1]:
            rng = ", ".join(f"{a}–{b}" if a != b else a for a, b in _runs(g))
        if k == len(merged) - 1:
            rng += " and `END.png`"
        notes = []
        for p in g:
            notes += notable(p)
        print(f"| `{LETTERS[k]}` | {rng} | {'; '.join(notes) if notes else '-'} |")


def _runs(g):
    runs, a, b = [], None, None
    for p in g:
        if p.get("kind") in ("title", "caption"):
            if a:
                runs.append((a, b))
            a = b = None
            continue
        if a is None:
            a = p["id"]
        b = p["id"]
    if a:
        runs.append((a, b))
    return runs


if __name__ == "__main__":
    main(sys.argv[1])
