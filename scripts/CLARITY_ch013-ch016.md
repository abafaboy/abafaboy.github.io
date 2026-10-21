# Clarity pass: chapters 013–016

Completed against `SCRIPT_CLARITY_BRIEF.md`, `bible/SCRIPT_FORMAT.md`, `CODEX_SCRIPT_BRIEF.md` section 3, and the cast/foreshadowing in `bible/STORY_BIBLE.md`. Read chapter 012's ending and the assigned scripts in full. Checked the relevant chapter beats and inspected chapter 013's existing dialogue art for speaker placement.

Only the four assigned scripts and this report were edited. No images were generated.

## Counts

“Rewritten” counts final dialogue/narration bubbles whose text changed; a merged bubble counts once. Moves include rewritten lines and are counted separately from text changes. Off-panel counts are newly marked final lines, including voices through phones/radios; `type: phone` is retained. Side corrections count final bubbles whose source position changed, including a moved bubble.

| Chapter | Rewritten | Moved | Newly off-panel | Side corrected | Final panels | Validation |
|---|---:|---:|---:|---:|---:|---|
| 013 | 37 | 3 | 20 | 25 | 59 | OK, no warnings |
| 014 | 37 | 2 | 8 | 4 | 54 | OK, no warnings |
| 015 | 39 | 1 | 4 | 3 | 50 | OK, no warnings |
| 016 | 45 | 3 | 13 | 2 | 62 | OK, no warnings |

## Chapter 013 — The Bottom of the Chain

- Named the contractor, penalty, missing porter, loan, routes and ground sensation where the old wording depended on an unclear pronoun. Preserved Dami's loan figures, both P08 plants, Kwak's asthma/inhaler setup, the three-second link and the final order.
- Corrected tails against existing art, including Minho at P07/P10, Taeo and Dokgo at P13, Nib at P27, Dami at P28, Minho at P47, and the central radio exchange at P52.
- Moved Nib's arrival report P37 → P36 and Dami's roll-call answer P51 → P52. This keeps each radio exchange to two speakers; Dami's answer becomes a phone voice when the view returns outside. Moved the loan footnote P19 → P18, beside its screen.
- Reshaped the unillustrated P20 from `inset-r` to `full`, with Nib left and Dami right. No panels added, merged or renumbered.
- Preserved `id`, `shape`, `camera`, `art`, `calm`, `style` and `silent` for all 56 locked story panels. The existing composition leaves only 4/59 panels tall or bleed; the brief's locked-art restriction prevents broad reshaping here.

### NEEDS REDRAW

None required for clear dialogue after the lettering changes. Locked full-figure framing, including P09, remains as supplied; this pass does not alter that art or shape.

## Chapter 014 — Roll Call

- Clarified why waiting for the boss kill may fail Kwak, whose inhaler Dami carries, the survey-line restriction, and Taeo's decision to stop Nib searching. Preserved the bad instruction, Nib's anger, Kett's mark, and the exact wall-discovery hook.
- Split the radio joke at P14 into P14 and new P14a. Taeo's rewritten reply moves to P14a, avoiding three different speakers when one is a radio voice. Moved the day-rate footnote P21 → P22.
- Reshaped to `tall`: P03, P06, P12, P13, P15, P16, P21, P23, P28, P37, P39, P42, P46, P48. P14a is `wide`, framed at the waist.
- Added explicit speaker positions and waist/knee framing in the remaining conversation shots. Combined multiple off-panel lines in single-person close-ups. Final tall/bleed count: 15/54.
- No existing IDs renumbered; no panels merged.

### NEEDS REDRAW

None. No story art existed for this chapter when checked.

## Chapter 015 — Air Through a Wall

- Clarified the rental deposit, map disagreement, whistle/wheeze evidence, thirty-minute search permission, wedge stone and slab-lifting instructions. Kept the deposit commitment, Nib going first, the unseen scuttler threat, slipping support and exact final warning.
- Moved Haein's rewritten relay promise P18 → P17, where she is visible, so P18 no longer has three different voices with Nib off-panel.
- Reshaped to `tall`: P02, P03, P08, P17, P18, P19, P20, P21, P23, P29, P32, P33, P43.
- Reshaped to `full`: P26 and P34. This gives the seated chibi figures and Nib's entrance silhouette room.
- Added speaker positions and waist/knee framing. Changed P39 to a two-shot showing both faces. Corrected the stray “green jacket” in P23 to the established navy canvas jacket. Final tall/bleed count: 16/50.
- No panels added, merged or renumbered.

### NEEDS REDRAW

None. No story art existed for this chapter when checked.

## Chapter 016 — Out Now

- Clarified who escaped the slab, the three-knock signal, the inhaler handoff, the blocked entrance, the return-mark plan, the false eight-person headcount and the penalty argument. Preserved the half-second rescue, recoil, scuttler fight, shard, delayed clear team, handholding and ceiling-crack hook.
- Moved the contractor's Yeouido/double-pay information P39 → P38, combining it with the headcount request. Folded Taeo's P38 “eight?” reaction into his P44 confrontation. Moved the day-rate footnote P42 → P44.
- Drew Haein into the unillustrated chibi brief at P14 so its three speakers are all visible. Reframed P39 to show Dokgo's face, allowing his protest and one off-panel caller response.
- Reshaped to `tall`: P03, P09, P10, P16, P18, P24, P26, P37, P38, P41, P42, P48, P50, P53, P59.
- Reshaped P14 and P55 to `full`, and P39 to `wide`. Added explicit positions and waist/knee framing elsewhere. Final tall/bleed count: 19/62.
- Corrected the P03 radio description to keep it on the rock established in chapter 015, and P07's camera description to keep Taeo's hand at the folding table.
- No panels added, merged or renumbered.

### NEEDS REDRAW

None. No story art existed for this chapter when checked.

## Verification

Ran `python tools/validate_script.py scripts/chNNN.yaml` after each chapter before starting the next, using the bundled Python executable. Revalidated all later adjustments; each chapter reports OK without warnings.

Additional checks found no panels over three total lettering lines, no speech without a side, no remote phone voice without an off-panel prefix, no three-speaker panel with a missing speaker, no single-person close-up with multiple off-panel lines, and no bubble/inset word-limit violations. Locked chapter 013 protected fields match the originals. Plant/payoff notes and the final hooks remain intact.

