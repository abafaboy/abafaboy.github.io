#!/usr/bin/env python3
"""validate_script: check chapter scripts against SCRIPT_FORMAT.md / SCRIPT_WRITER_BRIEF.md rules.

usage: validate_script.py scripts/ch002.yaml [more.yaml ...]   (prints a report per file; exit 1 if any ERROR)
"""
import re
import sys
from collections import Counter

import yaml

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from autostrip2 import load_script  # noqa: E402

SHAPES = {"full", "wide", "strip", "tall", "inset-l", "inset-r", "narrow-l", "narrow-r", "vignette", "bleed"}
GAPS = {"none", "short", "long", "black", "fade-black", "fade-white"}
TYPES = {"speech", "shout", "intense", "thought", "float", "nervous", "whisper", "menace", "monster", "phone", "announce",
         "narr", "narr_dark", "tag", "footnote", "system"}
UI = {"system.notice", "system.notice_small", "system.window", "system.summon_card", "system.warning", "system.log", "system.glitch",
      "system.button", "phone.ttok_chat", "phone.ttok_notification", "phone.ttok_call", "phone.ttok_video_call", "phone.bank_transfer",
      "phone.emergency_alert", "phone.gate_status", "phone.aao_booking", "phone.aao_result", "phone.quickhaul_order",
      "phone.hunterlink_rank", "phone.live_stream", "phone.sumex_ad", "phone.info_card", "tv.lowerthird", "label"}
HANDS = {"taeo_right_front", "taeo_left_tilt", "taeo_thumb_tap", "taeo_pov_ots", "grandma_phone", "chae_tablet", "phone_on_table"}
BESIDE = {"inset-l", "inset-r", "narrow-l", "narrow-r"}


def check(path):
    errs, warns = [], []
    try:
        S = load_script(path)
    except Exception as e:
        return [f"YAML: {e}"], [], {}
    P = S.get("panels") or []
    n = len(P)
    if not 45 <= n <= 65:
        errs.append(f"{n} panels (45–65)")
    kinds = [p.get("kind") for p in P]
    if kinds.count("title") != 1:
        errs.append("needs exactly one kind: title")
    elif not 2 <= kinds.index("title") <= 6:
        warns.append(f"title card at position {kinds.index('title') + 1} (cold open should be 2–6 panels)")
    if kinds[-1:] != ["end"]:
        errs.append("last panel must be kind: end")
    elif not P[-1].get("chibi_gag"):
        errs.append("end card has no chibi_gag")
    ids = [p.get("id") for p in P]
    for i, c in Counter(ids).items():
        if c > 1:
            errs.append(f"duplicate id {i}")
    silent = sum(1 for p in P if p.get("silent"))
    chibi = sum(1 for p in P if p.get("style") == "chibi")
    if silent < 3:
        errs.append(f"{silent} silent panels (≥3)")
    if not 1 <= chibi <= 3:
        errs.append(f"{chibi} chibi panels (1–3)")
    floats = 0
    types = Counter()
    who = Counter()
    plants = []
    story = [p for p in P if p.get("kind") not in ("title", "end")]
    if story and story[-1].get("shape") not in ("tall", "bleed"):
        warns.append(f"hook panel {story[-1].get('id')} is {story[-1].get('shape')} (tall or bleed expected)")
    for p in P:
        pid = p.get("id")
        if p.get("kind") in ("title", "end"):
            continue
        sh = p.get("shape")
        if sh not in SHAPES:
            errs.append(f"{pid}: shape {sh!r}")
        if p.get("gap", "short") not in GAPS:
            errs.append(f"{pid}: gap {p.get('gap')!r}")
        art = str(p.get("art") or "")
        ui = p.get("ui") or []
        on_screen = [u for u in ui if u.get("on") == "screen"]
        if "screen: green" in art.lower() and not on_screen:
            errs.append(f"{pid}: 'screen: green' with no `on: screen` ui")
        if on_screen and "screen: green" not in art.lower() and "kit hand" not in art.lower():
            warns.append(f"{pid}: ui on screen but the art brief has no 'screen: green'")
        for u in ui:
            if u.get("kind") not in UI:
                errs.append(f"{pid}: ui kind {u.get('kind')!r}")
            if u.get("hand") and u["hand"] not in HANDS:
                errs.append(f"{pid}: unknown kit hand {u['hand']!r}")
            if u.get("kind", "").startswith("system.") and u.get("on") not in ("float", None):
                warns.append(f"{pid}: system window with on: {u.get('on')}")
        if re.search(r"\b(text|caption|speech bubble|sfx|lettering)\b.*\b(reads?|says?|written)\b", art, re.I):
            warns.append(f"{pid}: art brief may ask for text in the art")
        lines = p.get("lines") or []
        talk = [l for l in lines if l.get("type", "speech") not in ("tag", "footnote", "system")]
        if len(talk) > 3:
            warns.append(f"{pid}: {len(talk)} lines (≤3 recommended)")
        if p.get("silent") and (talk or p.get("sfx")):
            errs.append(f"{pid}: silent panel has lines or sfx")
        for l in lines:
            t = l.get("type", "speech")
            types[t] += 1
            who[str(l.get("who"))] += 1
            if t not in TYPES:
                errs.append(f"{pid}: line type {t!r}")
            txt = str(l.get("text", ""))
            words = len(txt.split())
            if t not in ("narr", "narr_dark", "footnote") and words > 18:
                errs.append(f"{pid}: {words}-word bubble: {txt[:40]}")
            if sh in BESIDE and t not in ("tag", "footnote"):
                if words > 12:
                    warns.append(f"{pid}: {words} words beside a {sh} panel")
                if t in ("shout", "intense"):
                    warns.append(f"{pid}: {t} beside a {sh} panel")
            if t == "float":
                floats += 1
            letters = re.sub(r"[^A-Za-z]", "", txt)
            if letters and t not in ("tag", "footnote") and sum(c.islower() for c in letters) > len(letters) * 0.3:
                warns.append(f"{pid}: not in caps: {txt[:30]}")
        notes = str(p.get("notes") or "")
        plants += re.findall(r"(PLANT|PAYOFF) (P\d\d)", notes)
    if floats > 10:
        warns.append(f"{floats} float lines (≤10)")
    return errs, warns, {"panels": n, "silent": silent, "chibi": chibi, "types": dict(types), "who": dict(who), "plants": plants}


def main():
    bad = False
    for f in sys.argv[1:]:
        e, w, info = check(f)
        print(f"== {f}: {'OK' if not e else 'ERRORS'} | {info.get('panels')} panels, {info.get('silent')} silent, {info.get('chibi')} chibi")
        if info:
            print("   types:", info["types"])
            print("   who:", info["who"])
            print("   plants:", info["plants"])
        for x in e:
            print("   ERROR", x)
        for x in w:
            print("   warn ", x)
        bad |= bool(e)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
