# Chapter script format v2 (the rebuild): `scripts_v2/chNNN.yaml`

v2 keeps every field of `SCRIPT_FORMAT.md`, so the letterer and the video tools still read it. It adds the fields below and replaces the chapter rules. Scripts for the rebuilt story live in `scripts_v2/`; the old `scripts/` folder is retired.

## New panel fields

| Field | Values | Who uses it |
|---|---|---|
| `recipe` | a recipe from `codex/MANHWA_ART_DIRECTION.md` section 2: `establish`, `talk`, `reaction`, `eyes`, `insert`, `name-card`, `monster-reveal`, `anticipation`, `impact`, `aftermath`, `tone-flip`, `summon-arrival`, `link-view`, `carry`, `system`, `plan`, `chorus`, `silent`, `splash`, `chibi` | Codex draws the recipe |
| `light` | the key light (and back light, if any) in a few words | Codex, with style guide table 10.2 |
| `face` | `public` or `private` (Jaeha only) | Codex: the polite mask, or the cold reader underneath |
| `kind` | `title` (title card), `caption` (no art: narration set straight on the page background), `end` (end card with `chibi_gag`) | the letterer |
| `acting` | a map from character id to one sentence each: stance and weight; what each hand is doing; head and eyes; face. Physical facts with verbs caught mid-action, never "natural" or "dynamic". Required for every character whose body or face is readable (not for tiny figures or silhouettes). | Codex, with style guide 6b and 10.5 |
| `eyeline` | who looks at whom: "Mok → Jaeha (down); Jaeha → Mok (up)". "→ camera" only in shock, comedy and `system` panels. | Codex |
| `foreground` | the framing element in front of the subject: a shoulder, the back of a head, a pillar edge, a prop, always cropped. Required on at least every other `talk` panel, and on any `talk` panel that follows another `talk` panel. | Codex |

`caption` panels need no image. The letterer sets their lines on the page colour given in `bg`.

## New line types
- `note`: Jaeha's handwriting in his notebook. The letterer sets it as pencil handwriting on the notebook page drawn in the art.
- `inner`: Jaeha's inner voice (a black box with white text). Use 5–15 words, at most 2–3 per beat, and keep fewer inner lines than dialogue lines in every chapter.
- `chat`: livestream chat lines, inside a `ui` entry of kind `phone.live_stream`.

## Chapter rules (replace the v1 list)

These come from `research/MANHWA_CRAFT_BIBLE.md` section L.
1. 60–75 panels; action climaxes up to about 90; quiet chapters at least 55.
2. Something dangerous, funny or strange happens in the first 5 panels.
3. The title card (`kind: title`) comes after the hook, 15–40% of the way in.
4. The chapter turns at least twice, and ends in a different situation from where it began.
5. Talk-only panels (lines and no action or SFX) are 50% or fewer.
6. Bubbles are complete sentences averaging 7–10 words: 1–2 sentences each, at most 3 bubbles per panel, and the lines make sense without the art. One-word reactions are fine; clipped fragments are not.
7. Every important new character gets a name card (`intro`).
8. Every rule, reward and limit appears as a system window with numbers (`ui`).
9. Every action beat has an SFX. There is at least one `impact` or `splash` panel, and the camera changes every panel in a fight.
10. The last 1–3 panels open a question: a threat, mystery, system message, arrival, power or countdown. The type differs from the last chapter's.
11. Jaeha does something smart on the page.
12. One or two short laughs, in character, never inside a tense beat.
13. A fight adds something new, and the enemy can really win.
14. Bystanders react with their bodies, not with praise speeches.
15. At least 3 silent panels, 1 extreme close-up and 1 big reaction. Chibi appears only on comedy beats, and the end card carries a chibi gag.

**Acting rules,** added 25 October from `research/ACTING_STUDY.md`:

16. Every panel where a character's body or face is readable has an `acting` line for that character, and the hands are named.
17. In a run of talk panels, no two in a row share both the camera side and the shot size. The run moves through wide, two-shot, close-ups, an insert, a reaction and an extreme close-up.
18. Reactions and small movements carry a small `quiet` SFX near the movement: GLANCE, FLINCH, TWITCH, GULP, GRIN, SIGH, STEP STEP, SHAKE SHAKE, TAP TAP, PLOP. Aim for at least six in a chapter.

## Ids
- **Characters:** the ids in `NAME_SHEET.md`, plus these for chapter 1: `bh_spear`, `bh_axe`, `bh_sword`, `bh_mage`, `bh_crossbow`, `bh_shield` (Black Hound hunters 1–6 in `codex/CHARACTER_DESIGNS_v2.md` 2.5).
- **Locations:**

| id | Place |
|---|---|
| `gate0912_site` | the subway construction pit |
| `gate0912_fortress` | inside the gate |
| `boss_room` | the boss room |
| `gwanghwamun` | Gwanghwamun Square |
| `gate_exit` | the gate exit at night |
| `memorial_hall` | the memorial event |
| `rooftop_room` | the rooftop room |
| `kanghan_monitor` | Kanghan Tower's monitoring room |
| `ninth_wall` | the Ninth Wall |
