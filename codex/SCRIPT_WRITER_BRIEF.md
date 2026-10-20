# SCRIPT WRITER BRIEF: one chapter of "My Summons Go First"

You write ONE chapter script as YAML. Many writers work in parallel, one chapter each, so write only your own file.

## 1. Read first, completely
- `/home/claude/msgf-bible/STORY_BIBLE.md`: canon (world rules, cast and voices, motifs, the foreshadowing ledger in section 8, chapter craft rules in section 10).
- `/home/claude/msgf-bible/PART_ONE_BEATS.md`: the sections for your chapter and the chapters immediately before and after it, plus your arc's header. Deliver every beat listed for your chapter, in order.
- `/home/claude/msgf-bible/SCRIPT_FORMAT.md`: the YAML format, including the "Letterer features" section. Follow it exactly.
- `/home/claude/msgf-bible/ART_BIBLE.md`: Part A (art briefs, the A4 colour script, A5b chibi), B3 bubble types, B4 system windows, B5 phones, and Part C.
- `/home/claude/msgf-bible/world/LOCATIONS.md` and `/home/claude/msgf-bible/world/README.md`, if they exist: the canonical places, layouts, travel times and location ids. Use those ids in `locations:` and those layouts in art briefs.
- `/home/claude/msgf-bible/world/keys/<id>/`: the artist's drawn keys (key_wide.jpg, key_reverse.jpg, notes.md) for locations that have them. Look at the keys for every location your chapter uses. They are canonical for how a place looks: describe rooms, furniture and windows as the keys show them, and use the key's camera directions (notes.md) to stay consistent. If LOCATIONS.md and a key disagree, follow the key.
- `/home/claude/msgf-bible/scripts/ch001.yaml`: the gold standard. Match its detail in art briefs and its lettering.
- `/home/claude/msgf-bible/research/STORY_DIGEST.md`: the published edition being remade. Reuse its best lines where the beats keep them.
- The previous chapter's script, `/home/claude/msgf-bible/scripts/ch<N-1>.yaml`, if it exists when you start: read its last 10 panels and its end card. It may still be being written; if it is missing, work from the beats.

## 2. Write `/home/claude/msgf-bible/scripts/chNNN.yaml` (three digits) and no other file

## 3. Requirements (checked)
- 45–65 panels, including the title card (`kind: title`, after a 2–6 panel cold open) and the end card (`kind: end`, with a `chibi_gag` and the next-chapter teaser).
- Every beat for this chapter, with the HOOK as the final story panel (tall or bleed).
- At least 3 `silent: true` panels, 1–3 `style: chibi` panels on comedy beats, at least one extreme close-up, at least one big reaction, never more than two consecutive panels from the same camera position, and a varied mix of shapes.
- Each bubble at most 18 words; split and chain longer lines. All dialogue in CAPS, as in ch001. Taeo's floating narration (`type: float`) at most 6–10 lines per chapter, short and honest, never explaining what the art shows.
- Voices: Nib speaks in short declaratives, deadpan, no small talk. Taeo is polite, tired and dry, and says sorry too much. Every other character keeps the voice STORY_BIBLE gives them. Use the cast ids the bible uses for `who:` (for example taeo, nib, grandma, haru, eunchae, chae, minho, seoryun, courier, manager, grandpa, dr_pyo, granny_moon, sejin, dami, mansu, dokgo, orrin, sunline, park_doyun, haein, bangbang, sera, kesh, dara, kett).
- Art briefs: model-sheet ids and outfits, pose and ACTING (the emotion on the face), location id, light source, palette (A4), props, and what must not appear. NEVER ask for text, bubbles or SFX in the art; signs, tags and boards stay blank (the letterer writes any story-critical word with a `label` ui entry).
- Keep Nib adult and never cute outside chibi: the V-notch in his LEFT ear, one lower fang on the left, brown rope belt, pouch on the RIGHT hip, brown wooden sheath on the LEFT hip, barefoot until he chooses boots (ch 43).
- Screens: write "screen: green" in an art brief ONLY when the same panel has a `ui` entry with `on: screen` that fills it. Any other screen is dark or plain shapes. For a plain "reads his phone" beat, prefer a kit phone hand (`art: "KIT HAND"` plus `hand:` in the ui entry).
- Lettering placement: at most 3 lines per panel (split busy exchanges across more panels). Lines on inset-l, inset-r, narrow-l and narrow-r panels sit in a column beside the panel: keep those at most 12 words and never use shout or intense there.
- Continuity: start where the previous chapter's hook leaves off and end on your chapter's hook. Times, prices, counts and ages must match the bible and earlier chapters.
- System windows use the kit kinds (system.notice, system.notice_small, system.window, system.summon_card, system.warning, system.log, system.glitch). Phone screens use phone.* kinds; TV uses tv.lowerthird.
- Foreshadowing: place every ledger plant due in your chapter and pay off every payoff due (your task message lists them). Log each in that panel's notes as "PLANT Pxx" or "PAYOFF Pxx". Keep the motifs (STORY_BIBLE section 7) alive without explaining them.
- Make it genuinely good: real laughs, real ache, natural dialogue, stakes, and a hook that makes the next chapter unmissable.

## 4. Validate
Run: `python3 -c "import yaml;d=yaml.safe_load(open('/home/claude/msgf-bible/scripts/chNNN.yaml'));print(len(d['panels']))"` and fix any YAML error.

## 5. Report (your final reply)
The panel count; the number of silent and chibi panels; bubble-type counts; any beat you could not fit and why; and every continuity fact the next chapter's writer must know (time, place, props, injuries, money, who is where).
