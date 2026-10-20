# CHARACTER BRIEF 2: the rest of the Part One cast (method B)

Another Codex session is redoing the first cast (taeo, nib, grandma, haru, eunchae, chae, minho, seoryun, courier, golem, manager, grandpa). This session designs **new** characters, in **method B** (see `STYLE_FIX_BRIEF.md` section 6 and the TECHNIQUE BLOCK in section 3 of that brief).

Read first: `bible/ART_BIBLE.md` (Part A, A5b chibi, Part C), `bible/STORY_BIBLE.md` (the cast, allies, S-ranks and antagonists sections), `style_test/abcd/STUDY_NOTES.md`, and look at `characters/taeo/turnaround.png` and `characters/nib/turnaround.png` so the new designs match their style, line weight and colour treatment.

## Deliverables per character
In `characters/<id>/`:
- `turnaround.png` (1536×1024): front, three-quarter, side, back, full body, neutral pose, plain light-grey background. A small height bar is fine; no other text.
- `expressions.png` (1536×1024): 8 head shots (neutral, smile, anger, fear, grief, surprise, determined, their signature expression).
- `details.png` (1536×1024): props, hands, any locked detail, close-ups.
- `chibi.png` (1536×1024, the 8 gag poses from STYLE_FIX_BRIEF section 4): only for orrin, sera, kesh, dara, dami and granny_moon.
- `card.json`: id, name, age, height, palette hex values, and continuity locks as a list.

No text in any image. Write only inside your characters' own folders and `characters/REPORT_SET2.md`. Do not touch other characters' folders or the shared manifests.

## Order and designs
Do them in this order (first appearance first). Where the bible is silent, design it, and record the decision in `card.json`.

1. **granny_moon** (ch 5). An Old Arrival who has lived in Seoul for decades without papers. Very tall (about 190 cm), grey-skinned, long-limbed, elderly; human-like but clearly not human (long grey ears swept back, pale eyes). Runs a laundromat in Mangwon: cardigan, apron, slippers, reading glasses on a cord. Quiet, watchful, kind.
2. **dr_pyo** (ch 6). Dr. Pyo Jaesung, Kanghan Institute researcher, about 50. Courteous, patient, truly curious; the antagonist of Arc I. Neat grey suit, institute lanyard (blank), thin rimless glasses, a soft voice you can see. Never sinister-cartoon: he is reasonable and that is the danger.
3. **sejin** (ch 10). Im Sejin, 36, B-rank freelance field medic. Practical field gear, a medic's chest rig, cropped hair, tired eyes, dry humour.
4. **dami** (ch 13). Gu Dami, 19, unawakened porter for Dokgo Contracting. Cheap hi-vis porter vest over a hoodie, hard hat, cargo straps, worn gloves, determined small frame. Later she wears the GO FIRST patch.
5. **mansu** (ch 13). Kwak Mansu, 40s, Dami's porter partner: heavy-set, quiet, a back brace over his work clothes.
6. **dokgo** (ch 13). Dokgo Chul, 50s, porter subcontractor squeezed from above. Windbreaker, clipboard tablet, two phones, cigarette he never lights.
7. **orrin** (ch 24). Adult **stoneback carrier**: tortoise-like, about 2.3 m long, a shell like a hill of stacked slate, a slow gentle face, huge spatial memory. Dry humour. He is too big for every door. Draw him with the slate shell, sturdy columnar legs, and expressive eyes. Never a pet, never cute (except chibi).
8. **sunline** (billboards from ch 3; S-rank). Seo Jiwon, "Sunline": celebrity spear user, sponsor patches, a striking white-and-gold battle outfit, confident media smile.
9. **park_doyun** (arc V). "The Cartographer", elite construct summoner, about 30: tailored dark coat, a map-case, precise and cool.
10. **haein** (ch 52). Ryu Haein, 20, engineering student and gearhead, Minho's sister: same family look as Minho (see `characters/_v1/minho/`), overalls, tool belt, safety glasses pushed up, blunt.
11. **bangbang** (ch 51). Bang Seokho, streamer: dyed hair, gimbal and phone rig, loud jacket, ring light.
12. **sera** (ch 46). Adult human archer from a river settlement on the other side: competitive, musical (a bone flute), vain about her skill, honest about liking money and applause. Practical river clothes, a recurve bow, a quiver, bead and bone ornaments.
13. **kesh** (ch 65). Adult **moth-like signal keeper**: tall and slight, soft grey-brown wings folded like a cloak, feathered antennae, large dark eyes, delicate hands. Reads distant pulses; low endurance. Adores crowds and gossip.
14. **dara** (ch 85). Adult **armoured field surgeon** from the other side: blunt, funny, abrasive. Heavy plated armour worn over a surgeon's wrap, scarred forearms, a surgical kit on her belt.
15. **kett** (flashbacks). The younger goblin scout Nib trained: same species as Nib, younger, slighter, eager; carries a carved mark (a little three-line fork).

## Checks
Each character must look like the same artist drew them as Taeo and Nib. Run the ART_BIBLE Part C anti-AI checklist on every sheet. Keep the summons adult (Orrin, Sera, Kesh, Dara, Kett is a young adult) and never cute outside chibi.

When all are done, write `characters/REPORT_SET2.md` listing every file.
