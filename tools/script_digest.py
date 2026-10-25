#!/usr/bin/env python3
"""script_digest: print a compact, narration-oriented view of a v2 chapter script.

usage: script_digest.py scripts_v2/chNNN.yaml
For each panel: id, kind/recipe, the art description, dialogue lines, UI text and SFX. Skips camera, light, acting and layout fields.
"""
import sys
import textwrap

import yaml


def ui_text(u):
    k = u.get("kind", "")
    bits = [u.get(f) for f in ("headline", "body", "text", "title", "name", "caller", "sender", "viewers", "amount", "to", "ticker") if u.get(f)]
    bits += list(u.get("lines", []) or []) + list(u.get("chat", []) or [])
    for m in u.get("messages", []) or []:
        bits.append(f"{m.get('from')}: {m.get('text')}")
    return f"[{k}] " + " | ".join(str(b) for b in bits)


def main(p):
    d = yaml.safe_load(open(p, encoding="utf-8"))
    print(f"# Chapter {d.get('chapter')}: {d.get('title')}  ({d.get('when')})")
    for c in d.get("continuity", []) or []:
        print("  continuity:", c)
    print()
    for pn in d["panels"]:
        pid = pn.get("id")
        if pn.get("kind") in ("title", "caption", "end"):
            print(f"{pid} [{pn.get('kind')}] (no narration) {pn.get('title_card', pn.get('chibi_gag', ''))}")
            continue
        head = f"{pid} [{pn.get('recipe')}{', silent' if pn.get('silent') else ''}]"
        if pn.get("intro"):
            head += f" NAME CARD: {pn['intro']}"
        print(head)
        art = " ".join(str(pn.get("art", "")).split())
        print(textwrap.fill("  art: " + art, 160, subsequent_indent="       "))
        for ln in pn.get("lines", []) or []:
            print(f"  {ln.get('type')} {ln.get('who')}: {ln.get('text')}")
        for u in pn.get("ui", []) or []:
            print("  ui:", ui_text(u))
        for s in pn.get("sfx", []) or []:
            print(f"  sfx: {s.get('text')}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
