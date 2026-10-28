#!/usr/bin/env python3
"""validate_script_v2: mechanical checks of a rebuilt-story chapter script against SCRIPT_FORMAT_v2.md.

usage: validate_script_v2.py scripts_v2/chNNN.yaml [more.yaml ...]
Prints a report per file and exits 1 if any ERROR. Craft rules that need judgement (the hook, the smart move, the
laughs) are not checked here; this catches the countable ones.
"""
import re
import sys

import yaml

SHAPES = {"full", "wide", "strip", "tall", "inset-l", "inset-r", "narrow-l", "narrow-r", "vignette", "bleed"}
GAPS = {"none", "short", "long", "black", "fade-black", "fade-white"}
RECIPES = {"establish", "talk", "reaction", "eyes", "insert", "name-card", "monster-reveal", "anticipation", "impact",
           "aftermath", "tone-flip", "summon-arrival", "link-view", "carry", "system", "plan", "chorus", "silent", "splash",
           "chibi"}
TYPES = {"speech", "shout", "intense", "thought", "float", "nervous", "whisper", "menace", "monster", "phone", "announce",
         "narr", "narr_dark", "tag", "footnote", "inner", "note", "link"}
DIALOGUE = {"speech", "shout", "intense", "thought", "nervous", "whisper", "menace", "monster", "phone", "announce"}
UI = {"system.notice", "system.notice_small", "system.window", "system.summon_card", "system.warning", "system.log",
      "system.glitch", "system.button", "phone.live_stream", "phone.gate_status", "phone.emergency_alert",
      "phone.bank_transfer", "phone.ttok_chat", "phone.ttok_notification", "phone.ttok_call", "phone.ttok_video_call", "phone.camera",
      "phone.info_card", "tv.lowerthird", "label"}
SFX_STYLES = {"impact", "quiet", "comic", "alert", "gate", "summon"}
BGS = {"white", "black", "navy", "paper"}


def words(t):
    return len(re.findall(r"[A-Za-z0-9']+", t))


def check(path):
    errs, warns, info = [], [], []
    S = yaml.safe_load(open(path, encoding="utf-8"))
    P = S.get("panels") or []
    cast = set((S.get("cast") or {}).keys())
    ids = [str(p.get("id")) for p in P]
    if len(set(ids)) != len(ids):
        errs.append("duplicate panel ids")
    seq = [i for i in ids if re.fullmatch(r"P\d\d", i)]
    for a, b in zip(seq, seq[1:]):
        if int(b[1:]) != int(a[1:]) + 1:
            errs.append(f"panel ids jump from {a} to {b}")
    if not P or P[-1].get("kind") != "end" or not P[-1].get("chibi_gag"):
        errs.append("the last entry must be the END card (kind: end) with a chibi_gag")
    body = [p for p in P if p.get("kind") != "end"]
    n = len(body)
    if not 55 <= n <= 90:
        errs.append(f"{n} panels (55–90; 60–75 typical)")
    elif not 60 <= n <= 75:
        warns.append(f"{n} panels (60–75 typical; quiet chapters ≥55, climaxes up to ~90)")
    titles = [i for i, p in enumerate(body) if p.get("kind") == "title"]
    if len(titles) != 1:
        errs.append("needs exactly one kind: title")
    else:
        frac = (titles[0] + 1) / n
        if not 0.15 <= frac <= 0.40:
            errs.append(f"title card at {titles[0] + 1}/{n} ({frac:.0%}); rule: 15–40% of the way in")
    talk_only = silent = eyes = quiet = inner = dialogue = 0
    chibi = 0
    prev_talk = None
    words_all = []
    for i, p in enumerate(body):
        pid = str(p.get("id"))
        kind = p.get("kind")
        lines = p.get("lines") or []
        for ln in lines:
            t = ln.get("type")
            if t not in TYPES:
                errs.append(f"{pid}: unknown line type {t!r}")
            who = str(ln.get("who", ""))
            base = who.split(":", 1)[-1]
            if who and base not in cast and not who.startswith("offpanel:crowd") and base not in ("crowd", "system"):
                warns.append(f"{pid}: speaker {who!r} not in cast")
            if t in DIALOGUE:
                dialogue += 1
                w = words(ln.get("text", ""))
                if w > 1:
                    words_all.append(w)
                if w > 22:
                    warns.append(f"{pid}: long bubble ({w} words)")
            if t == "inner":
                inner += 1
                w = words(ln.get("text", ""))
                if not 3 <= w <= 15:
                    warns.append(f"{pid}: inner line of {w} words (5–15)")
        bubbles = [ln for ln in lines if ln.get("type") in DIALOGUE | {"inner"}]
        if len(bubbles) > 3:
            errs.append(f"{pid}: {len(bubbles)} bubbles (max 3)")
        if not p.get("window_clear") and p.get("shape") in ("wide", "tall", "full", "bleed", "vignette", "strip") and any(ln.get("type") in DIALOGUE | {"inner"} for ln in lines):
            for u in p.get("ui") or []:
                if u.get("on") == "float" and str(u.get("kind", "")).startswith("system.") and (u.get("at") or [0.5, 0.1])[1] < 0.3:
                    errs.append(f"{pid}: a top window and dialogue on one {p.get('shape')} panel (the bubble tails cross the window; rule 20)")
        for u in p.get("ui") or []:
            if u.get("kind") not in UI:
                errs.append(f"{pid}: unknown ui kind {u.get('kind')!r}")
            if str(u.get("kind", "")).startswith("system.") and not (u.get("text") or u.get("headline") or u.get("name")):
                errs.append(f"{pid}: system window without text")
        for s in p.get("sfx") or []:
            if s.get("style") not in SFX_STYLES:
                errs.append(f"{pid}: unknown sfx style {s.get('style')!r}")
            if s.get("style") == "quiet":
                quiet += 1
        if kind in ("title", "caption"):
            prev_talk = None
            continue
        for f in ("recipe", "shape", "camera", "light", "art", "calm"):
            if f not in p:
                errs.append(f"{pid}: missing {f}")
        if p.get("recipe") not in RECIPES:
            errs.append(f"{pid}: unknown recipe {p.get('recipe')!r}")
        if p.get("shape") not in SHAPES:
            errs.append(f"{pid}: unknown shape {p.get('shape')!r}")
        if p.get("gap") not in GAPS:
            errs.append(f"{pid}: unknown gap {p.get('gap')!r}")
        if p.get("bg") not in BGS:
            errs.append(f"{pid}: unknown bg {p.get('bg')!r}")
        if p.get("style") == "chibi" or p.get("recipe") == "chibi":
            chibi += 1
        if p.get("silent"):
            silent += 1
            if any(ln.get("type") in DIALOGUE for ln in lines):
                errs.append(f"{pid}: marked silent but has dialogue")
        if p.get("recipe") in ("eyes",) or "extreme close-up" in str(p.get("camera", "")).lower():
            eyes += 1
        # characters named in the art "(id" or "(id," must have an acting line
        named = set(re.findall(r"\(([a-z_]+)(?:,|\)|;)", str(p.get("art", ""))))
        acting = set((p.get("acting") or {}).keys())
        for c in sorted(named & cast):
            if c not in acting and c not in ("knight_commander", "husk", "stone_lizard"):
                warns.append(f"{pid}: {c} named in the art but has no acting line")
        has_action = bool(p.get("sfx")) and any(s.get("style") != "quiet" for s in p.get("sfx") or [])
        is_talk = any(ln.get("type") in DIALOGUE | {"inner"} for ln in lines) and not has_action and p.get("recipe") not in (
            "impact", "anticipation", "monster-reveal", "summon-arrival", "splash", "carry", "establish")
        if is_talk:
            talk_only += 1
            if prev_talk and p.get("recipe") == "talk" and prev_talk.get("recipe") == "talk" and not p.get("foreground"):
                warns.append(f"{pid}: talk panel after a talk panel without a foreground element")
            if prev_talk and p.get("shape") == prev_talk.get("shape") and p.get("camera") == prev_talk.get("camera"):
                warns.append(f"{pid}: same shape and camera as the previous talk panel")
            prev_talk = p
        else:
            prev_talk = None
    art_panels = sum(1 for p in body if p.get("kind") not in ("title", "caption"))
    avg = sum(words_all) / len(words_all) if words_all else 0
    info.append(f"{n} panels ({art_panels} with art), {dialogue} dialogue lines (avg {avg:.1f} words), {inner} inner, "
                f"{talk_only} talk-only ({talk_only / max(1, art_panels):.0%}), {silent} silent, {eyes} extreme close-ups, "
                f"{quiet} quiet SFX, {chibi} chibi")
    if talk_only / max(1, art_panels) > 0.5:
        errs.append(f"talk-only panels {talk_only}/{art_panels} (> 50%)")
    if not 6.5 <= avg <= 11:
        warns.append(f"average bubble length {avg:.1f} words (7–10)")
    if inner >= dialogue:
        errs.append(f"inner lines ({inner}) must be fewer than dialogue lines ({dialogue})")
    if silent < 3:
        errs.append(f"{silent} silent panels (at least 3)")
    if eyes < 1:
        errs.append("no extreme close-up")
    if quiet < 6:
        warns.append(f"{quiet} quiet SFX (aim for 6+)")
    if not any(p.get("recipe") in ("impact", "splash") for p in body):
        errs.append("no impact or splash panel")
    return errs, warns, info


def main():
    bad = False
    for path in sys.argv[1:]:
        errs, warns, info = check(path)
        print(f"== {path}: {'ERRORS' if errs else 'ok'}")
        for i in info:
            print("  ", i)
        for e in errs:
            print("   ERROR", e)
        for w in warns:
            print("   warn ", w)
        bad |= bool(errs)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
