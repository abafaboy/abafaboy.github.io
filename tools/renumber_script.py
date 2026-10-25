#!/usr/bin/env python3
"""renumber_script: renumber a v2 chapter script after inserting panels with suffixed ids (P05a, P05b ...).

Every panel id is renumbered sequentially (P01, P02 ...). Every P-reference anywhere in the file (cast comments,
continuity, plants, notes, header comments) is mapped through the same old->new table, so write references against
the OLD numbering before running this. Section header comments of the form
    # ===== NAME (Pxx–Pyy) =====
get their ranges recomputed from the panels under them, and a title note "Title card at panel N of M (P%)." is
rewritten.

usage: renumber_script.py scripts_v2/chNNN.yaml
"""
import re
import sys

ID_RE = re.compile(r"^  - id: (P\d\d[a-z]?)$", re.M)
TOK_RE = re.compile(r"\bP(\d\d)([a-z]?)\b")


def main(path):
    s = open(path, encoding="utf-8").read()
    ids = ID_RE.findall(s)
    if len(set(ids)) != len(ids):
        sys.exit("duplicate ids: " + ", ".join(sorted({i for i in ids if ids.count(i) > 1})))
    mapping = {old: f"P{i + 1:02d}" for i, old in enumerate(ids)}

    def sub(m):
        tok = m.group(0)
        return mapping.get(tok, tok)

    s = TOK_RE.sub(sub, s)

    # recompute header ranges
    lines = s.split("\n")
    hdr_idx = [i for i, l in enumerate(lines) if re.match(r"^\s*# =+ .* =+\s*$", l)]
    for k, hi in enumerate(hdr_idx):
        end = hdr_idx[k + 1] if k + 1 < len(hdr_idx) else len(lines)
        block = [re.match(r"^  - id: (P\d\d)$", l) for l in lines[hi:end]]
        pids = [m.group(1) for m in block if m]
        if not pids:
            continue
        rng = pids[0] if len(pids) == 1 else f"{pids[0]}–{pids[-1]}"
        l = lines[hi]
        if re.search(r"\(P\d\d(–P\d\d)?\)", l):
            l = re.sub(r"\(P\d\d(–P\d\d)?\)", f"({rng})", l)
        else:
            l = re.sub(r"(# =+ )(.*?)( =+\s*)$", lambda m: f"{m.group(1)}{m.group(2)} ({rng}){m.group(3)}", l)
        lines[hi] = l
    s = "\n".join(lines)

    # title note
    n = len(ids)
    tm = re.search(r"^  - id: (P\d\d)\n    kind: title", s, re.M)
    if tm:
        tp = int(tm.group(1)[1:])
        s = re.sub(r"Title card at panel \d+ of \d+ \(\d+%\)\.", f"Title card at panel {tp} of {n} ({tp / n:.0%}).", s)
    open(path, "w", encoding="utf-8").write(s)
    changed = {o: nw for o, nw in mapping.items() if o != nw}
    print(f"{n} panels; {len(changed)} ids changed" + (f"; title at {tp}" if tm else ""))


if __name__ == "__main__":
    main(sys.argv[1])
