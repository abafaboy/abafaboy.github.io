#!/usr/bin/env python3
"""merge_hands: check or merge a hands-pass file (ledger/hands_pass/chNNN.json) into scripts_v2/chNNN.yaml.

usage:
  merge_hands.py --check 13 14     validate only; changes nothing
  merge_hands.py --merge 13 14     insert `hands:` / `hand_ref:` into each panel, then prove nothing else changed

The JSON has one entry per panel with art: "none", or {"hands": {char_id: text, ...}, "hand_ref": [file, ...]}.
A file with "_partial": true covers only the panels it lists (for chapters that are already partly drawn).
The merge is text-level (the YAML's comments, folding and order stay as they are): the fields go right after the
panel's `acting:` block (or after `art:`, or at the end of the panel). Re-merging replaces earlier hands fields.
"""
import json
import os
import re
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REFS = {"grip_hilt_one_hand.png", "grip_hilt_two_hands.png", "reverse_grip_knives.png", "notebook_and_pencil.png",
        "pointing.png", "hand_on_shoulder.png", "phone_hold.png", "bow_draw.png", "crossbow_hold.png",
        "healing_palms.png", "shield_grip.png", "fists_and_bracing.png", "reaching_grabbing_wrist.png",
        "mouth_and_strap.png", "holding_cup.png", "handshake_and_peace.png", "arms_carry.png", "arms_relaxed.png"}
NONHUMAN = {"nib": "four", "borro": "four", "pim": "three"}
HIDDEN = re.compile(r"out of (the )?frame|below the frame|hidden|behind (his|her|their) back|not visible|out of sight|in (his|her|their) pockets?", re.I)


def art_panels(S):
    out = []
    for p in S["panels"]:
        if p.get("kind") in ("caption", "title"):
            continue
        out.append(str(p.get("id")))
    return out


def check(n, quiet=False):
    errs, warns = [], []
    sp = os.path.join(ROOT, f"scripts_v2/ch{n:03d}.yaml")
    jp = os.path.join(ROOT, f"ledger/hands_pass/ch{n:03d}.json")
    S = yaml.safe_load(open(sp, encoding="utf-8"))
    try:
        H = json.load(open(jp, encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        return [f"cannot read {jp}: {e}"], [], None, None
    partial = bool(H.pop("_partial", False)) if isinstance(H, dict) else False
    want = art_panels(S)
    if partial:
        want = [p for p in want if p in H]
    byid = {str(p.get("id")): p for p in S["panels"]}
    cast = set((S.get("cast") or {}).keys())
    missing = [p for p in want if p not in H]
    extra = [p for p in H if p not in want]
    if missing:
        errs.append(f"panels with art missing from the JSON: {missing}")
    if extra:
        errs.append(f"entries for panels without art or unknown ids: {extra}")
    order = [p for p in H if p in want]
    if order != [p for p in want if p in H]:
        warns.append("entries are not in panel order (merge doesn't care)")
    nhands = nnone = 0
    for pid, v in H.items():
        if v == "none":
            nnone += 1
            continue
        if not isinstance(v, dict) or not isinstance(v.get("hands"), dict) or not v["hands"]:
            errs.append(f"{pid}: must be \"none\" or {{\"hands\": {{...}}, \"hand_ref\": [...]}}")
            continue
        nhands += 1
        bad_keys = set(v) - {"hands", "hand_ref"}
        if bad_keys:
            errs.append(f"{pid}: unknown keys {sorted(bad_keys)}")
        acting = set(((byid.get(pid) or {}).get("acting") or {}).keys())
        for who, text in v["hands"].items():
            if not isinstance(text, str) or not text.strip():
                errs.append(f"{pid}: {who}: empty text")
                continue
            if who != "background" and who not in cast and who not in acting:
                warns.append(f"{pid}: {who!r} is not in the chapter cast or the panel's acting")
            nw = len(text.split())
            if nw > 45:
                warns.append(f"{pid}: {who}: {nw} words (keep it under ~30)")
            base = who.split("_")[0]
            if base in NONHUMAN and not HIDDEN.search(text) and NONHUMAN[base] not in text.lower():
                warns.append(f"{pid}: {who}: say \"{NONHUMAN[base]} fingers and a thumb\" (or four-/three-fingered)")
            if who.startswith("geum") and re.search(r"\bLEFT\b", text) and "three" not in text.lower() and "prosthetic" not in text.lower():
                warns.append(f"{pid}: {who}: her LEFT hand is the prosthetic (three metal fingers and a thumb)")
        refs = v.get("hand_ref", [])
        if not isinstance(refs, list):
            errs.append(f"{pid}: hand_ref must be a list")
            refs = []
        if len(refs) > 2:
            errs.append(f"{pid}: hand_ref has {len(refs)} files (two at most)")
        for r in refs:
            if r not in REFS:
                errs.append(f"{pid}: unknown hand reference {r!r}")
    if not quiet:
        print(f"ch{n:03d}: {len(want)} panels with art; {nhands} with hands, {nnone} none; "
              f"{len(errs)} errors, {len(warns)} warnings")
        for e in errs:
            print("  ERROR", e)
        for w in warns:
            print("  warn ", w)
    return errs, warns, S, H


def yq(s):
    return json.dumps(s, ensure_ascii=False)


def block_for(v):
    if v == "none":
        return ["    hands: none"]
    lines = ["    hands:"]
    for who, text in v["hands"].items():
        lines.append(f"      {who}: {yq(text.strip())}")
    refs = v.get("hand_ref") or []
    if refs:
        lines.append("    hand_ref: [" + ", ".join(refs) + "]")
    return lines


def merge(n):
    errs, warns, S, H = check(n)
    if errs:
        print(f"ch{n:03d}: not merged (fix the errors first)")
        return False
    sp = os.path.join(ROOT, f"scripts_v2/ch{n:03d}.yaml")
    text = open(sp, encoding="utf-8").read()
    L = text.split("\n")
    starts = [i for i, l in enumerate(L) if re.match(r"^  - id: ", l)]
    bounds = list(zip(starts, starts[1:] + [len(L)]))
    out = L[:starts[0]]
    for a, b in bounds:
        blk = L[a:b]
        pid = blk[0].split(":", 1)[1].strip().strip('"\'')
        # drop earlier hands fields
        keep, skip = [], False
        for l in blk:
            if re.match(r"^    (hands|hand_ref):", l):
                skip = l.startswith("    hands:") and l.rstrip().endswith("hands:")
                continue
            if skip and re.match(r"^      \S", l):
                continue
            skip = False
            keep.append(l)
        blk = keep
        if pid in H:
            # where to insert: after the acting block, else after art, else after the last non-blank line
            def end_of(key):
                for i, l in enumerate(blk):
                    if re.match(rf"^    {key}:", l):
                        j = i + 1
                        while j < len(blk) and (blk[j].startswith("      ") or (blk[j].strip() == "" and j + 1 < len(blk) and blk[j + 1].startswith("      "))):
                            j += 1
                        return j
                return None
            at = end_of("acting")
            if at is None:
                at = end_of("art")
            if at is None:
                at = len(blk)
                while at > 1 and blk[at - 1].strip() == "":
                    at -= 1
            blk = blk[:at] + block_for(H[pid]) + blk[at:]
        out.extend(blk)
    new = "\n".join(out)
    S2 = yaml.safe_load(new)
    # prove nothing else changed
    def strip(d):
        return {k: v for k, v in d.items() if k not in ("hands", "hand_ref")}
    S0 = yaml.safe_load(text)
    if {k: v for k, v in S0.items() if k != "panels"} != {k: v for k, v in S2.items() if k != "panels"}:
        print(f"ch{n:03d}: ABORT: top-level fields changed")
        return False
    if len(S0["panels"]) != len(S2["panels"]):
        print(f"ch{n:03d}: ABORT: panel count changed")
        return False
    for p0, p2 in zip(S0["panels"], S2["panels"]):
        if strip(p0) != strip(p2):
            print(f"ch{n:03d}: ABORT: {p0.get('id')} changed beyond the hands fields")
            return False
        pid = str(p2.get("id"))
        if pid in H:
            want = H[pid]
            got = p2.get("hands")
            if want == "none":
                if got != "none":
                    print(f"ch{n:03d}: ABORT: {pid} hands not merged as none")
                    return False
            else:
                if got != {k: t.strip() for k, t in want["hands"].items()} or (p2.get("hand_ref") or []) != (want.get("hand_ref") or []):
                    print(f"ch{n:03d}: ABORT: {pid} hands not merged exactly")
                    return False
    open(sp, "w", encoding="utf-8").write(new)
    print(f"ch{n:03d}: merged {len(H)} panels")
    return True


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "--check"
    chs = [int(x) for x in sys.argv[2:]]
    ok = True
    for c in chs:
        if mode == "--merge":
            ok &= merge(c)
        else:
            e, w, _, _ = check(c)
            ok &= not e
    sys.exit(0 if ok else 1)
