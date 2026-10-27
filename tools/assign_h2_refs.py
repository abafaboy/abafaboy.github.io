#!/usr/bin/env python3
"""assign_h2_refs: give panels the H2 prop and gesture references (HANDS_REFERENCE_BRIEF.md, job H2) where their hands: lines name the action.

usage: assign_h2_refs.py [--dry] 4 5 ... 40
For each panel with a hands: mapping, matches the H2 keywords against the panel's hand lines. Matched H2 files go first
in hand_ref (two at most); the panel's earlier H1 refs fill any room left. Text-level edit; proves nothing but hand_ref
changed. Prints a count per reference and per chapter.
"""
import collections
import json
import os
import re
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H2 = [  # (file, pattern, per-line exclusion)
    ("trooper_carbine.png", r"carbine|stun baton|shock baton|launcher", None),
    ("baton_conducting.png", r"\bbaton\b", r"stun baton|shock baton"),
    ("ladle_grip.png", r"\bladle\b", None),
    ("phone_to_ear.png", r"phone[^;.]{0,40}\bear\b|\bear\b[^;.]{0,25}phone|receiver", None),
    ("arm_in_arm.png", r"\barm (hooked |looped |linked )?through (his|her|jaeha's|the crook)|\barm in arm|crook of (his|her|jaeha's) |hand in hand|holding hands|child's hand|daughter's hand|son's hand|links? (her|his) arm", None),
    ("hug.png", r"\bhug(s|ging|ged)?\b|wrapped round (him|her)self|arms round (him|her)self|hugging herself|hugging himself", None),
    ("steering_wheel.png", r"steering wheel|(on|over|grips?|gripping|holding|holds|draped over|rests on) the wheel\b", r"hatch|valve"),
    ("rail_ladder_rope.png", r"\brails?\b|\brailings?\b|\bhandrails?\b|\bladder\b|\brungs?\b|hand over hand|\brope\b|\bcable\b", None),
    ("megaphone_binoculars_radio.png", r"megaphone|loudhailer|binoculars|\bradio\b|walkie", None),
    ("gestures_face.png", r"\btemple\b|chin (propped|resting) on|chin on (his|her)|propped on (his|her) (hand|fist|palm)|through (his|her) fingers|face in (his|her) hands|hands over (his|her) face", None),
    ("gestures_body.png", r"on (his|her) hip\b|hands on (his|her) hips|palm (held )?(out )?(face )?up\b|palm-up|thumbs?-up", None),
    ("wrists_bound.png", r"wrists? (bound|tied|cuffed)|bound wrists|tied wrists|handcuff|in cuffs|cuffed|\bcane\b|walking stick", None),
    ("tablet_laptop_folder.png", r"\btablet\b|laptop|keyboard|trackpad|\bfolder\b|clipboard", None),
    ("chopsticks_bowl_pinch.png", r"chopsticks|rice bowl|bowl of|soup bowl|thumb and forefinger|between (his|her) thumb", None),
    ("carry_and_handover.png", r"\bcrates?\b|envelope|hard hat (in|held)|the hard hat in", None),
    ("shield_overhead.png", r"overhead like a roof|like a roof|shield (held )?overhead|overhead swing|over (his|her) head in both hands|pushing up against|palms? (pressed )?flat (up )?(on|against) (the|her|his) (ceiling|keystone|slab|arch)|arms locked overhead", None),
    ("arrow_quiver.png", r"quiver|\bnock(s|ing|ed)?\b|parasol|umbrella", None),
]


def h2_for(lines):
    found = []
    for f, pat, excl in H2:
        for t in lines:
            tl = t.lower()
            if excl:
                if f == "steering_wheel.png" and re.search(excl, tl):
                    continue  # a hatch or valve wheel is not a steering wheel
                tl = re.sub(excl, "", tl)  # e.g. a stun baton is not a conductor's baton
            if re.search(pat, tl):
                found.append(f)
                break
    return found


def run(chs, dry):
    tally = collections.Counter()
    for n in chs:
        p = os.path.join(ROOT, f"scripts_v2/ch{n:03d}.yaml")
        text = open(p, encoding="utf-8").read()
        S0 = yaml.safe_load(text)
        L = text.split("\n")
        starts = [i for i, l in enumerate(L) if re.match(r"^  - id: ", l)]
        bounds = list(zip(starts, starts[1:] + [len(L)]))
        byid = {str(x["id"]): x for x in S0["panels"]}
        out = L[:starts[0]]
        changed = 0
        for a, b in bounds:
            blk = L[a:b]
            pid = blk[0].split(":", 1)[1].strip()
            P = byid.get(pid, {})
            hands = P.get("hands")
            if isinstance(hands, dict):
                found = h2_for([str(v) for v in hands.values()])
                if found:
                    old = list(P.get("hand_ref") or [])
                    new = (found + [r for r in old if r not in found])[:2]
                    if new != old:
                        refline = "    hand_ref: [" + ", ".join(new) + "]"
                        hi = [i for i, l in enumerate(blk) if l.startswith("    hand_ref:")]
                        if hi:
                            blk[hi[0]] = refline
                        else:
                            k = [i for i, l in enumerate(blk) if l.startswith("    hands:")][0] + 1
                            while k < len(blk) and blk[k].startswith("      "):
                                k += 1
                            blk = blk[:k] + [refline] + blk[k:]
                        changed += 1
                        for f in found[:2]:
                            tally[f] += 1
            out.extend(blk)
        new = "\n".join(out)
        S1 = yaml.safe_load(new)
        for x, y in zip(S0["panels"], S1["panels"]):
            assert {k: v for k, v in x.items() if k != "hand_ref"} == {k: v for k, v in y.items() if k != "hand_ref"}, (n, x.get("id"))
        assert {k: v for k, v in S0.items() if k != "panels"} == {k: v for k, v in S1.items() if k != "panels"}
        if not dry and changed:
            open(p, "w", encoding="utf-8").write(new)
        print(f"ch{n:03d}: {changed} panels get H2 references")
    print(json.dumps(dict(tally.most_common()), indent=0))


if __name__ == "__main__":
    dry = "--dry" in sys.argv
    chs = [int(x) for x in sys.argv[1:] if not x.startswith("--")]
    run(chs, dry)
