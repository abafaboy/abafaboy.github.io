# RECAP BRIEF: write the narrator's recap for chapters of "My Summons Go First"

The owner wants each chapter's video told by ONE narrator, the way manhwa recap channels do it: third person, past tense, over the pages. You write that narration from the chapter scripts. This is a text-only task: do not generate any images. Other Codex chats are working at the same time, so write only the files your task names.

## Read
- `scripts/chNNN.yaml` for each chapter in your task. These are the revised scripts: use their panel ids, lines and art briefs.
- `bible/STORY_BIBLE.md` section 1 (the premise) and the cast section, for names and who people are.

## Write `recap/chNNN.json` for each chapter
A JSON list in reading order. Each entry is `{"panel": "<id>", "text": "<narration>"}`.
- **`panel`** is the id of the panel the reader sees while this narration plays. Give one entry per panel, or one entry for a run of panels that show one beat (use the first panel's id). Skip `kind: title` and `kind: end` panels.
- **Narration.**
  - Third person, past tense, plain spoken English, like a good recap channel: "Taeo had one free draw left, so he spent it just to see what would happen."
  - Say who speaks and what they mean. Quote the best lines briefly ("Nib only said: 'You first.'").
  - Explain anything a listener needs to follow the story: who someone is, what a system window says, what is at stake.
  - Keep the jokes, the warmth and the tension. End each chapter on its hook, so the listener wants the next one.
- **Length.** The owner found the first recaps too slow, so keep recap-channel pace: about 12 words per drawn panel, which is roughly 550–800 words for a 55–60-panel chapter. Aim for 15–25 words per entry and never more than 35. Short sentences. Keep what matters later (names, money, rules, promises, reveals, the hook) and cut blow-by-blow detail. `recaps/ch001.json`–`ch013.json` in this repo are the model.
- **Panels that exist.** Only use panel ids that have a PNG in the chapter's `art/` folder. Panel order must never go backwards.
- **No invention.** Never invent events, names or numbers the script doesn't have. No stage directions, no "in this panel", no emojis.
- Names are written normally (Taeo, Nib, Chae, Minho, Seoryun, Grandma), not in caps.

Validate each file with `python -c "import json;d=json.load(open('recap/chNNN.json',encoding='utf-8'));print(len(d))"`. Then write a one-line `recap/DONE_chNNN.md` with the entry count and the word count.

Do not stop to ask anything; finish every chapter in your task.
