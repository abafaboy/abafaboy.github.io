#!/usr/bin/env python3
"""validate_recap_v2: check a narrator recap (recaps_v2/chNNN.json) against its script (scripts_v2/chNNN.yaml).

usage: validate_recap_v2.py recaps_v2/chNNN.json [scripts_v2/chNNN.yaml]

Checks: valid JSON list of {panel, text}; every panel id exists in the script and has art (not a title, caption or end card);
the order never goes backwards; no panel twice; each entry 3-45 words; the total is about 14 words per narrated art panel
(800-900 words for 60 panels); how many art panels are left without narration.
"""
import json
import re
import sys

import yaml


def main(rp, sp=None):
    if sp is None:
        sp = re.sub(r"recaps_v2/(ch\d+)\.json$", r"scripts_v2/\1.yaml", rp)
    errs, warns = [], []
    try:
        rec = json.load(open(rp, encoding="utf-8"))
    except Exception as e:
        print(f"== {rp}: ERRORS\n   ERROR not valid JSON: {e}")
        return 1
    d = yaml.safe_load(open(sp, encoding="utf-8"))
    panels = [p for p in d["panels"]]
    order = {p["id"]: i for i, p in enumerate(panels)}
    art = {p["id"] for p in panels if p.get("kind") not in ("title", "caption", "end")}
    if not isinstance(rec, list):
        errs.append("not a list")
        rec = []
    seen, last, total = set(), -1, 0
    for k, e in enumerate(rec):
        if not isinstance(e, dict) or set(e) != {"panel", "text"}:
            errs.append(f"entry {k}: must be exactly {{panel, text}}")
            continue
        pid, text = e["panel"], str(e["text"]).strip()
        if pid not in order:
            errs.append(f"entry {k}: {pid} not in the script")
            continue
        if pid not in art:
            errs.append(f"entry {k}: {pid} has no art (title, caption or end card)")
        if pid in seen:
            errs.append(f"entry {k}: {pid} narrated twice")
        seen.add(pid)
        if order[pid] < last:
            errs.append(f"entry {k}: {pid} goes backwards")
        last = max(last, order[pid])
        n = len(text.split())
        total += n
        if n < 3 or n > 45:
            warns.append(f"{pid}: {n} words")
        if re.search(r"[‘’“”]", text) is None and '"' in text:
            pass
    missing = [p["id"] for p in panels if p["id"] in art and p["id"] not in seen]
    n_art = len(art)
    lo, hi = int(12.5 * n_art), int(17 * n_art)
    if not (lo <= total <= hi):
        warns.append(f"{total} words for {n_art} art panels (aim {int(13.3 * n_art)}-{int(15 * n_art)})")
    if len(missing) > max(3, n_art // 10):
        warns.append(f"{len(missing)} art panels without narration: {', '.join(missing)}")
    status = "ERRORS" if errs else "ok"
    print(f"== {rp}: {status}\n   {len(rec)} entries, {total} words, {n_art} art panels, {len(missing)} unnarrated")
    for x in errs:
        print("   ERROR", x)
    for x in warns:
        print("   warn ", x)
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))
