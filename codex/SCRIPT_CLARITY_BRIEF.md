# SCRIPT CLARITY BRIEF: make every line easy to follow

The owner read chapters 1–4 and said he can't tell who is talking, the dialogue is confusing, and bodies look compressed. You revise the scripts named in your task so that a reader scrolling on a phone always knows who says each line and what it means. Other Codex chats revise other scripts and review panels at the same time: edit only the scripts in your task, plus your report. Do not generate any images.

## 1. Read first
- `bible/SCRIPT_FORMAT.md` (the format, including "Letterer features") and `CODEX_SCRIPT_BRIEF.md` section 3 (the requirements that still apply).
- `bible/STORY_BIBLE.md`: the cast and their voices, and the foreshadowing ledger (section 8), so you keep every plant and payoff.
- Each script in your task, in full, plus the last 10 panels of the chapter before your first one.

## 2. What you may change
- **Locked panels.** A panel is locked when its art exists: `chapters/chNNN/art/<id>.png`. For a locked panel, keep `id`, `shape`, `camera`, `art`, `calm`, `style` and `silent` exactly as they are. You may change its `lines` (text, who, side, type, order) and the text inside its `ui` entries. You may also move a line to a neighbouring locked panel where its speaker is visible.
- **Unlocked panels** (no art yet). You may also change `shape`, `camera`, `art` and `calm`. You may split a panel in two; the new panel gets the old id plus a letter (P12 → P12, P12a). You may also merge two panels. Never renumber existing ids, and keep each chapter at 45–65 panels.
- Never change story events, beats, plants and payoffs, continuity facts or the hook.

## 3. Rules
1. **Who is talking.** Every spoken line is said either by a character drawn in that panel or as an off-panel line. When the speaker is not drawn in that panel (check `camera` and `art`), write `who: "offpanel:<id>"`, and set `side` to the side of the panel where that speaker stands. The letterer gives off-panel lines a tail that points out of the panel.
2. **Sides.** For a drawn speaker, `side` is where the art places them: left third `l`, middle `c`, right third `r`. In unlocked panels, if the art brief doesn't say where each speaker stands, add it ("Chae on the left, Taeo on the right").
3. **Close-ups** (close-up, extreme close-up, insert). Only the character shown speaks, plus at most one off-panel line. Move other people's lines to a panel where those people are visible. In unlocked parts of the chapter you may add a reaction panel instead.
4. **Busy panels.** At most 3 spoken lines per panel. A panel with lines from 3 different people needs all 3 drawn in it.
5. **Plain dialogue that reads at scroll speed.**
   - Each line must make sense on its own. Name the thing: no bare "that one", "it", "this" or "him" when the reader can't tell from the panel what is meant.
   - When a line raises a question, answer it within the next few lines, unless the mystery is obviously on purpose.
   - Cut writerly ellipses and dashes. Use "..." only for a real pause, and never on two lines in a row.
   - Prefer short, natural sentences people actually say. Exposition is fine when it is clear and in character.
   - Keep every voice: Nib speaks in short, deadpan declaratives; Taeo is polite, tired and dry, and says sorry too much; everyone else keeps the voice STORY_BIBLE gives them. Keep the jokes and the emotional beats.
   - Taeo's float narration may say what a moment means to him, in short honest lines, at most 10 per chapter.
6. **Bodies need room** (unlocked panels only).
   - A full-body figure, or two or more standing characters, goes in a `tall`, `bleed` or `full` panel, never in a `strip` or an inset.
   - Use `strip` only for details: eyes, hands, objects, a sign.
   - Aim for at least a quarter of each chapter's panels `tall` or `bleed`.
   - In art briefs for wide panels, frame people from the waist or knees up rather than fitting a whole body in.
7. Every other requirement in CODEX_SCRIPT_BRIEF.md section 3 still holds: at most 18 words per bubble, CAPS, kit kinds, and the rest.

## 4. Validate
Run `python tools/validate_script.py scripts/chNNN.yaml` after each chapter. It must report OK before you start the next chapter.

## 5. Report
Write `scripts/CLARITY_<first>-<last>.md` (for example `CLARITY_ch001-ch004.md`). For each chapter, give:
- how many lines you rewrote, moved, marked off-panel, and corrected `side` on;
- which panels you added, split or reshaped;
- under **NEEDS REDRAW**, any locked panel whose drawing makes clear dialogue impossible (for example, the only person drawn is the wrong one), with the reason.
