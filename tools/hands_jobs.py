#!/usr/bin/env python3
"""hands_jobs: turn the hands audit (ledger/hands_audit/chNNN.json) into Codex fix lists (codex/reviews/HANDS_chNNN.md).

usage: hands_jobs.py [--min 1] [--skip ch002:P58,ch003:P45] 2 3
Problems at or above --min (default 2) become fixes (the method and procedure are in codex/HANDS_FIX_BRIEF.md);
lower ones are listed only.
Panels in --skip are being redrawn by another job and are left out (listed at the end).
Also writes ledger/hands_audit/HF_panels.json: {chapter: [panels]} for staging the base images.
The suggested hand reference is a keyword match on each entry's fix sentence: Claude reviews every list before it ships.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ART = "/home/claude/msgf-art/chapters_v2"

HANDREF = [  # first match wins: most specific first
    (r"\bcrossbow", "crossbow_hold.png"),
    (r"\bbow\b|\bbowstring|\barrows?\b|\bdraw(s|ing)? the string", "bow_draw.png"),
    (r"\bknife\b|\bknives\b|\bdaggers?\b", "reverse_grip_knives.png"),
    (r"two[- ]handed|both hands (on|grip|round|around|hold)\w* (the|his|her) (hilt|sword|handle|grip)", "grip_hilt_two_hands.png"),
    (r"\bhilt\b|\bsword\b|\bpommel\b|\bguard\b", "grip_hilt_one_hand.png"),
    (r"\bnotebook\b|\bpencil\b|\bwrit(e|es|ing)\b", "notebook_and_pencil.png"),
    (r"\bpoint(s|ing|ed)?\b", "pointing.png"),
    (r"\bphone\b", "phone_hold.png"),
    (r"\bheal(s|ing)?\b|\bglow(s|ing)? (palm|hand)|palms? (held )?(over|above|toward)", "healing_palms.png"),
    (r"\bshield\b", "shield_grip.png"),
    (r"\bfists?\b|\bbrac(e|es|ed|ing)\b|flat on the (floor|ground|stone|wall|pillar|table)|push(es|ing)? (himself|herself) up", "fists_and_bracing.png"),
    (r"\bcarr(y|ies|ying)\b|over (his|her) shoulder\b|across (his|her) shoulders|help(s|ing)? \w+ (to )?walk", "arms_carry.png"),
    (r"\bwrist\b|\breach(es|ing)?\b|pull(s|ing)? (him|her) (up|back)|\bgrab(s|bing)?\b", "reaching_grabbing_wrist.png"),
    (r"\bmouth\b|\bstrap\b|(on|to|against) (his|her) chest", "mouth_and_strap.png"),
    (r"\bcup\b|\bcoffee\b|\bcanned\b|\bsoda can\b", "holding_cup.png"),
    (r"handshake|shak(e|es|ing) hands|peace sign|\bV sign|two (bloody )?fingertips up|two fingers up", "handshake_and_peace.png"),
    (r"(on|onto|over) (his|her|\w+'s) shoulder|\bcollar\b|\bnape\b|\bscruff\b", "hand_on_shoulder.png"),
    (r"\brelaxed\b|at (his|her) sides?\b|\bcrossed\b|\bhanging\b", "arms_relaxed.png"),
]

SHEETS = [  # who (lower-case substring) -> details sheet
    ("jaeha", "kang_jaeha/details.png"), ("nib", "nib/details.png"), ("yerin", "song_yerin/details.png"),
    ("mok", "mok_hangyu/details.png"), ("bomi", "yoo_bomi/details.png"), ("choi", "choi_dongmin/details.png"),
    ("knight", "knight_commander/details.png"), ("commander", "knight_commander/details.png"),
    ("borro", "borro/details.png"), ("kett", "kett/details.png"), ("hound", "black_hound/lineup.png"),
    ("hunter", "black_hound/lineup.png"), ("lyra", "lyra/details.png"), ("sora", "han_sora/details.png"),
]


def handref(*texts):
    for t in texts:
        t = (t or "").lower()
        for pat, f in HANDREF:
            if re.search(pat, t):
                return f
    return None


def sheets_for(who):
    w = who.lower()
    out = []
    for k, v in SHEETS:
        if k in w and v not in out:
            out.append(v)
    return out


def method(ps):
    fx = [str(p.get("fix", "")).lower() for p in ps]
    if any("redraw" in f for f in fx):
        return "redraw"
    return "edit"


OVP = os.path.join(ROOT, "ledger/hands_audit/ref_overrides.json")
OVERRIDES = json.load(open(OVP)) if os.path.exists(OVP) else {}


def main(argv):
    skip = set()
    smin = 2
    while argv and argv[0].startswith("--"):
        if argv[0] == "--skip":
            skip = set(argv[1].split(","))
        elif argv[0] == "--min":
            smin = int(argv[1])
        argv = argv[2:]
    staged = {}
    for ch in [int(x) for x in argv]:
        cid = f"ch{ch:03d}"
        items = json.load(open(os.path.join(ROOT, f"ledger/hands_audit/{cid}.json")))
        items = [x for x in items if isinstance(x, dict)]
        probs = [x for x in items if (x.get("severity") or 0) >= smin]
        minor = [x for x in items if 0 < (x.get("severity") or 0) < smin]
        clean = sorted({x["panel"] for x in items if x.get("severity") == 0 and x.get("panel") != "none_visible"})
        by = {}
        for p in probs:
            by.setdefault(p["panel"], []).append(p)
        skipped = [pid for pid in by if f"{cid}:{pid}" in skip]
        for pid in skipped:
            by.pop(pid)
        n3 = sum(1 for ps in by.values() for p in ps if p["severity"] == 3)
        n2 = sum(1 for ps in by.values() for p in ps if p["severity"] == 2)
        n1 = sum(1 for ps in by.values() for p in ps if p["severity"] == 1)
        L = [f"# Hands and arms fixes: chapter {ch}", "",
             f"From Claude's audit of 28 October 2026 (`ledger/hands_audit/{cid}.json`). **{len(by)} panels to fix** "
             f"({n3} problems at severity 3, {n2} at severity 2" + (f", {n1} at severity 1" if n1 else "") + "). How to fix them: `codex/HANDS_FIX_BRIEF.md`. "
             f"Base images: `chapters_v2/{cid}/art/hands_fix/base/`.", ""]
        for pid in sorted(by, key=lambda s: (s == "END", s)):
            ps = by[pid]
            who = "; ".join(dict.fromkeys(p.get("who", "") for p in ps))
            refs = []
            ov = OVERRIDES.get(cid, {}).get(pid)
            if ov is not None:
                refs = [f"characters_v2/hands/{r}" for r in ov]
            else:
                for p in ps:
                    r = handref(p.get("redraw_note"), p.get("where"), p.get("problem"))
                    if r and f"characters_v2/hands/{r}" not in refs:
                        refs.append(f"characters_v2/hands/{r}")
            for s in sheets_for(who):
                s = f"characters_v2/{s}"
                if s not in refs:
                    refs.append(s)
            L.append(f"## {pid}: {method(ps)} (severity {max(p['severity'] for p in ps)})")
            for p in ps:
                L.append(f"- **{p.get('who', '')}**, {p.get('where', '')}: {p.get('problem', '')}")
                if p.get("redraw_note"):
                    L.append(f"  - **Fix:** {p['redraw_note']}")
            L.append("- **References:** " + ", ".join(f"`{r}`" for r in refs[:4]))
            L.append("")
        if minor:
            L += [f"## Minor (below severity {smin}: not fixed in this job)"]
            L += [f"- {p['panel']}: {p.get('who', '')}, {p.get('problem', '')}" for p in minor]
            L.append("")
        if skipped:
            L += [f"## Left out (redrawn by another job): {', '.join(skipped)}", ""]
        L.append(f"Panels that passed: {', '.join(clean) if clean else 'none listed'}.")
        out = os.path.join(ROOT, f"codex/reviews/HANDS_{cid}.md")
        open(out, "w").write("\n".join(L) + "\n")
        staged[cid] = sorted(by, key=lambda s: (s == "END", s))
        missing = [pid for pid in staged[cid] if not os.path.exists(f"{ART}/{cid}/art/{pid}.png")]
        print(f"{cid}: {len(by)} panels to fix ({n3} sev3, {n2} sev2, {n1} sev1), {len(minor)} minor, {len(clean)} clean;"
              f" skipped {skipped}; no art file for {missing}")
    hp = os.path.join(ROOT, "ledger/hands_audit/HF_panels.json")
    old = json.load(open(hp)) if os.path.exists(hp) else {}
    old.update(staged)
    json.dump(old, open(hp, "w"), indent=1)


if __name__ == "__main__":
    main(sys.argv[1:])
