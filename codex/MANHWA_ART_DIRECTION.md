# MANHWA ART DIRECTION (v2): how to draw panels that read like a real Korean webtoon

**Who this is for.** Codex, when drawing panels for the rebuilt *My Summons Go First*.

**What it adds.** This brief adds the action and staging grammar our first chapters were missing. Everything in `ART_BIBLE.md` still applies (line art, the flat cel look, chibi rules, the anti-AI checklist), except where this file says it supersedes it.

**Where the rules come from.** Claude read 13 real episodes panel by panel: *Omniscient Reader*, *The Lone Necromancer*, *My S-Class Hunters*, *Eleceed*, *The Greatest Estate Developer* and *Max-Level Newbie*. Claude also read Korean industry sources (see `research/MANHWA_CRAFT_BIBLE.md`). You never see those images, and you must never imitate a specific title's characters or panels. This file describes the *grammar*: shot types, rhythm, effects and colour.

---

## 1. What was wrong with our old panels (so you know what to fix)

- **Too many talking heads.** 69% of panels were people standing or sitting and talking at eye level in shops and offices.
- **Few impact panels.** Few extreme angles, little speed or impact language, and the camera rarely moved.
- **The rebuild changes the scripts.** They now have danger in chapter 1, fights in most chapters and one beat per action panel. Your job is to make each of those panels hit.

## 2. Panel recipes

Scripts now name a `recipe` on each panel. Draw the recipe exactly; the `art` field fills in who, where and what.

| Recipe | Shape | Camera | What it must show | Background | Calm / SFX space |
|---|---|---|---|---|---|
| `establish` | full or wide | high or eye level, wide lens | the place, the time of day, the light source; figures small | fully drawn, detailed | calm at the top |
| `talk` | wide or inset | over the shoulder or two-shot, a different side from the last talk panel | faces ACTING (brows, mouths, hands) | simplified (flat, gradient, soft shapes) | calm region for 2–3 bubbles |
| `reaction` | inset or strip | close-up | one strong emotion; sweat, shine, a gasp | flat colour, gradient, focus lines | small calm corner |
| `eyes` | strip (3:1) | extreme close-up | eyes only; the decision or the dread | black, white or a mood wash | usually none (silent) |
| `insert` | inset or narrow | close-up on hands or an object | the notebook, a core, a knife, a phone (green screen) | plain | small |
| `name-card` | tall or wide | bust or half body, three-quarter view, slight low angle | the character's look and attitude, iconic pose | gradient in the character's signature colour | one clear side (about 35% of the width) for the name card |
| `monster-reveal` | full or tall | low angle from behind the MC | the creature FILLS the frame; the MC is small in the foreground, back to us | dark; one red accent | calm top-left |
| `anticipation` | inset or tall | three-quarter, foreshortened | the wind-up a moment before the hit: coiled body, weapon drawn back | muted, tension lines | small |
| `impact` | wide, tall or bleed, tilted 10–20° | dynamic diagonal | the hit at its peak: speed lines radiating from the contact point, debris, a motion smear on the moving limb | white flash or hot orange or red | **large SFX space along the diagonal** |
| `aftermath` | wide | eye level, still | dust settling, a body on the ground, the winner's back; no motion lines | drawn, quiet | calm at the top |
| `tone-flip` | strip, then tall | extreme close-up, then empty | (a) a glowing eye or hollow on black; (b) a tall panel of streaked dark speed texture with NO figure (the letterer puts a giant SFX there) | black or red | (b) is all SFX space |
| `summon-arrival` | tall or bleed | low angle | a cyan floor circle, a vertical seam of light, the summon stepping through (ART_BIBLE A8); in a fight, the summon blocking a strike mid-motion | dark scene, cyan light on faces | calm at the top |
| `link-view` | wide | split frame | left: Jaeha's face lit in the summon's colour; right: the summon's point of view through a thin vignette in the same colour | as the scene | small |
| `carry` | inset or tall | three-quarter | Jaeha buckling as a translucent impact ring hits his body where the summon was hit; a small nosebleed when the script says so | flat with focus lines | small |
| `system` | wide or tall | the character facing the reader, lit cyan from the front | the character reading something in the air; leave the area the window will cover EMPTY | dark | **a big empty area** for the UI window |
| `plan` | wide | over the shoulder or overhead | Jaeha's eyes or back plus clean cyan tactical lines over the battlefield (arrows, circles, routes) with no text | the battlefield, slightly desaturated | small |
| `chorus` | wide | flat, straight on | 3–5 faces in a row, each with a different reaction; or a phone or monitor (green screen) for a livestream | simplified | one small calm spot per face |
| `silent` | any | any | an emotion carried by face and body alone | as the beat needs | none |
| `splash` | full or tall bleed | dramatic, low or symmetric | the big moment (a seal break, an evolution, VANGUARD): the character large and the effect at full strength | effect light | calm at the top |
| `chibi` | inset | flat | ART_BIBLE A5b | gag pattern | small |

## 3. Action grammar (how a fight reads)

1. **One beat per panel.** The script splits every exchange into anticipation → impact → reaction or aftermath. Never draw two actions in one panel.
2. **The angle changes every panel:** low, high, overhead, the MC's eye level, behind the monster. Never two panels in a row from the same position (this tightens ART_BIBLE A7's limit of 2).
3. **Screen direction.** Within one fight, the MC's side attacks left to right unless the script says the momentum has turned. If it turns, the flip is the point.
4. **The summon goes first; the MC reads the fight.** Between hits, the script puts a `reaction` or `eyes` panel of Jaeha watching. His face must show calculation (narrowed eyes, sweat, lips moving as he counts), not just fear.
5. **Effect lines are drawn, never blurred.** Use the ART_BIBLE line art style: crisp, tapered black or white strokes.
   - **Speed lines:** parallel, in the direction of motion.
   - **Focus lines:** radial, toward a face or point.
   - **Impact radials:** short, thick and burst-shaped at the contact point.
   - No airbrush blur and no depth-of-field.
6. **Debris and particles appear only at an impact,** a summon or a gate (ART_BIBLE A8 still applies).
7. **Violence happens between panels.** Show the moment before, then a `tone-flip` or `impact`, then the aftermath.
   - No gore close-ups. Blood is a splash on a wall or a silhouette.
   - The platform-safe version is the only version.
8. **Size means importance.** The biggest or tallest panel in a chapter is its peak beat. Use 1–3 `impact`, `splash` or bleed panels per chapter and spend your best effort there.

## 4. Colour flips (supersedes nothing; extends ART_BIBLE A3 and A4)

| Mood or beat | Palette |
|---|---|
| Daily life | muted, one hue per location (ART_BIBLE A4) |
| Inside a gate | the wrong-coloured sky (lavender noon, green dusk); violet shadows |
| Danger arriving | the scene desaturates, and ONE red accent appears (an eye, a door, a warning) |
| Hit or impact | hot orange or yellow background, or a pure white flash panel |
| Horror (a tone flip) | black and red only |
| System or Operator light | cyan #3FE3F2 on navy #0B1530, lighting faces from the front |
| Flashback | desaturated grey-blue, soft edges, one warm colour for the remembered person |
| Comedy beat | flat pastel or a gag pattern, with chibi (ART_BIBLE A5b) |

## 5. Power and summon signature colours

Each colour is reserved for one thing. Never use it for anything else.

| Thing | Colour | Where it shows |
|---|---|---|
| Operator interface, the CALL circle and seam | cyan #3FE3F2 | system light, summon arrival |
| LINK thread | the linked summon's signature colour | a thin thread or an eye glow in `link-view` |
| CARRY | translucent white impact ring | on Jaeha's body |
| STORE / RELEASE | pale gold rings around his fist or blade, then a white-gold shockwave | from Arc 5 on |
| The Hollow (bosses) | a black-violet hole where the face should be, cracked armour leaking violet ash; it glows red when hostile | every hollowed boss |
| Nib | amber #F2A93B | his eyes and his link |
| Borro | moss green | |
| Lyra | river blue and silver | |
| Pim | moon cream and lilac | |
| Maud | bone white and oxblood | |
| Caldric | ember orange in black ash | |

## 6. Monsters and bosses

- **Silhouette first.** A monster must read at phone size as a black shape. Give it one exaggerated feature (the beak, the tail or the horns), not ten small ones.
- **One weak point that glows.** The script will use it (Jaeha finds tells).
- **Scale is shown, never told.** A person, a door or a car in the same panel gives a big monster its size.
- **Hollowed heroes** keep traces of who they were: a sigil on the armour, a torn banner, a surgeon's apron. The reveal in Arc 6 depends on these being drawn consistently from chapter 1 on.

## 7. Faces and acting (extends ART_BIBLE A5)

- **Jaeha has two faces.**
  - **Public:** a polite, slightly bowed smile with tired eyes.
  - **Private:** narrowed eyes and a small one-sided grin.
  - The script marks which one with `face: public` or `face: private`, and the gap is the character.
- **Grin panels:** a close-up of the private grin, half the face in shadow. Use them sparingly, about once a chapter.
- **Bystanders react with their BODIES:** stepping back, dropping a weapon, freezing, hands over mouths. Draw the body language; the script keeps their lines short.
- **Nib is an adult soldier in a small body.** Deadpan face, a soldier's posture, never cute (except in chibi).

## 8. Panel count and rhythm (supersedes ART_BIBLE A7's 45–65)

- **Panel count.** 60–75 panels per chapter; action climaxes up to about 90.
- **Gaps between panels.** The script sets `gap`:
  - short for fast exchanges;
  - long before a reveal;
  - black stretches for dread.
- **Talk-heavy runs.** At most 4 `talk` panels in a row. The script will break longer conversations with an `insert`, `reaction` or `silent` panel. Draw those with real acting so the conversation never feels like a wall.

## 9. What stays exactly the same

- **No text in the art.** No bubbles, SFX, windows or readable UI. Phones are flat #00FF00 (ART_BIBLE A9). Big SFX are added by the letterer in the space you reserve.
- **Continuity locks and model sheets** (ART_BIBLE A10), and the anti-AI checklist (Part C).
- **Sizes by shape and file naming,** as in `PANEL_BRIEF.md`.
