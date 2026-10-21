# Clarity pass: chapters 9–12

Edited only `scripts/ch009.yaml`, `scripts/ch010.yaml`, `scripts/ch011.yaml`, `scripts/ch012.yaml`, and this report. No images generated.

Read SCRIPT_CLARITY_BRIEF.md, SCRIPT_FORMAT.md (including Letterer features), CODEX_SCRIPT_BRIEF.md section 3, STORY_BIBLE.md (including voices and ledger), the four complete scripts, and ch008's last ten story panels and end card. Also checked the chapter beats, art requirements and continuity rulings. Inspected existing art where attribution or placement was uncertain.

Counts below compare with the scripts at the start of this pass. “Rewritten” counts retained lines whose wording changed, including narration and tags. “Marked off-panel” counts newly applied offpanel prefixes. Counts overlap: a moved line can also be rewritten or have its side corrected. Combined/cut bubbles are listed separately.

| Chapter | Lines rewritten | Lines moved | Newly marked off-panel | Lines with side corrected | Final panels |
|---|---:|---:|---:|---:|---:|
| ch009 | 54 | 2 | 1 | 28 | 64 |
| ch010 | 57 | 2 | 10 | 21 | 58 |
| ch011 | 41 | 2 | 1 | 13 | 55 |
| ch012 | 48 | 1 | 6 | 21 | 63 |

## Chapter 9 — Someone's Relief

Clarified the review countdown, stocker's unrelieved work, arrival filing, Kanghan's petition, witness evidence and renewable status. Named Nib and Kett where pronouns obscured the connection. Kept Nib's fear, “I'M SOMEONE'S RELIEF,” the no-sale choice, the ID-card joke and “I DIDN'T ASK YOU TO.”

- Moved Taeo's reading question and Nib's “SLOWLY” from the P51 card insert to P52, where both are drawn. P51 now has one off-panel reading line.
- Marked the unseen panel chair off-panel in P35.
- Reshaped unlocked P20, P21, P43 and P61 from wide to tall.
- Specified speaker positions in unlocked P20, P21, P22, P43 and P60–P63.
- Added/split panels: none. Removed bubbles: none.

### NEEDS REDRAW

None required to make the revised dialogue attributable. Existing locked P55 still frames Pyo's full figure in a narrow panel; refer that body-framing issue to the panel review.

## Chapter 10 — Day Rates

Made pay, insurance, subcontracting, return-mark activation, the nine-hour wait and the knock code explicit. Kept Sejin's paid terms, Nib's medical and boots jokes, the entry count and the pulse going dark.

- Moved the film's native/no-mark explanation from P37 to P35. P37 now contains only Nib and Sejin's exchange.
- Moved Sejin's barefoot advice from P45 to P46, where she is drawn. P45 has Nib and one off-panel line from Minho.
- Marked all nine unseen safety-film voice lines as offpanel:psa; they retain phone voice bubbles.
- Assigned the clock-start instruction in P53 to visible Minho and named Haein in the instruction.
- Reshaped unlocked P32 and P39 from wide to tall; P35 from wide to full for the cartoon's full figure.
- Specified positions/framing in unlocked P32–P35, P37–P39 and P57.
- Added/split panels: none. Removed bubbles: none.

### NEEDS REDRAW

None required for the revised dialogue. Locked P03 (standing Seonhee in an inset) and P45 (full-body Nib in a narrow panel) remain body-framing flags for the panel review.

## Chapter 11 — Waiting

Clarified the cracked strut, survey endpoint, knock timing, Minho's delayed crossing and Nib's run back. Kept the first “IT'S THE SAME KIND,” the white-bit wording, PLANT P07, full day-rate pay, the cable idea and the missing-porter hook.

- Added tall P51a by splitting the P51 news/reaction exchange: the reporter stays on the news image; Nib's question and Taeo's answer move together to a visible two-shot.
- P51a needs its first illustration; no art was generated.
- Marked Taeo's unseen P07 reply off-panel.
- Reshaped existing panels: none. Removed bubbles: none.

### NEEDS REDRAW

None required for the revised dialogue. The new P51a is an unillustrated addition, not a replacement of locked art.

## Chapter 12 — Three Beams

Made the beam/pin test, left-to-right sequence, three trials, pressure calls, recoil uncertainty, towing fee and Thursday offer explicit. Kept the sleep joke, two correct tests, nosebleed, snail survival, repossession, chalk-line evidence and final “YOU **STAY** OUTSIDE.”

- Added tall P04a by splitting P04: Doyun's recorded line stays on the phone insert; Nib's sleep reply moves to his own visible reaction.
- P04a needs its first illustration; no art was generated.
- Marked Doyun on the phone insert, Taeo on the palm inserts, and unseen Haein prompts off-panel.
- Combined each pair of Taeo's calls in P28 and P35 into one bubble, leaving at most one off-panel spoken line per palm insert.
- Cut Nib's redundant P51 observation that the van is being taken, leaving Haein and off-panel Minho as the two speakers.
- Reshaped existing panels: none. Specified positions and full-height space in unlocked P61.

### NEEDS REDRAW

None required for the revised dialogue. Locked P41 puts the full group/setup in a strip, and P50 puts Haein's full body in an inset; these remain body-framing flags for the panel review. New P04a needs its first illustration.

## Validation and lock audit

Ran `python tools/validate_script.py scripts/ch009.yaml`, then ch010, ch011 and ch012 in order. Each returned **OK before revision of the next chapter began**. Revalidated each after the final placement corrections: all **OK with no warnings**.

| Chapter | Silent panels | Chibi panels | Taeo float lines | Tall/bleed panels |
|---|---:|---:|---:|---:|
| ch009 | 9 | 3 | 8 | 7 |
| ch010 | 6 | 2 | 7 | 7 |
| ch011 | 8 | 2 | 4 | 6 |
| ch012 | 6 | 3 | 4 | 4 |

Compared every initially locked panel's id, shape, camera, art, calm, style and silent value against the starting script: **no changes**. Existing IDs, hooks, prices, dates, plants, payoff timing and silent beats remain in place. Checked bubble limits, close-up off-panel counts and panels with three distinct speakers.

The quarter-tall/bleed target remains constrained by the existing locked compositions. All new panels are tall; unlocked standing group compositions were enlarged where needed. Locked body layouts were preserved and flagged above.
