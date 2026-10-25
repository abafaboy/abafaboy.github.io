# MANHWA STYLE GUIDE (v1, 25 October 2026): how the rebuilt *My Summons Go First* should look

**Who this is for.** Codex, for every image in the rebuilt story (lead: Kang Jaeha). Read `README_START_HERE.md` first.

**What this file decides.** The *look*: line, shading, light, colour, backgrounds, effects, faces and monsters.
- `MANHWA_ART_DIRECTION.md` still decides *staging*: panel recipes, camera and action grammar.
- `CHARACTER_DESIGNS_v2.md` decides *who* looks like what.

**What it replaces.**

| `bible/ART_BIBLE.md` | Status |
|---|---|
| Part A: A1 (the look), A3 (colour), A4 (old locations) and A11 (old cast) | Replaced by this file and `CHARACTER_DESIGNS_v2.md` |
| A2 (line), A5 (faces) and A8 (effects) | Refined here; where they differ, this file wins |
| A5b (chibi), A6, A7, A9 (no text in art) and A10 (continuity), and Parts B and C | Still apply |

**The style is chosen: V2 · Cinematic cel.** On 25 October the owner asked Claude to pick, and Claude chose V2 (section 3 says why).
- Use only the V2 STYLE BLOCK.
- V1 and V3 stay in this file as background and never go into a prompt.
- Your first job is `STYLE_TEST_BRIEF.md`: two check panels in V2, then Jaeha's and Nib's sheets.

---

## 1. Where these rules come from

Claude studied real Korean webtoons directly. The evidence is in two files:
- **`bible/VISUAL_SURVEY.md`:** episode 1 of 103 titles (lettering, UI, colour habits).
- **`research/RENDERING_STUDY.md`:** six titles viewed slice by slice, with chosen slices enlarged and zoomed:
  - *The Lone Necromancer* (eps 1, 2, 6);
  - *Omniscient Reader* (eps 0–3);
  - *Eleceed* (ep 1);
  - *My S-Class Hunters* (ep 1);
  - *I'm the Max-Level Newbie* (ep 1);
  - *The Return of the Disaster-Class Hero* (prologue).

The titles are named here so you know what the rules are based on. Three hard rules follow from that:
- You never see those images.
- You never copy their characters, faces, poses, panels or text.
- **You never put a real title, studio, artist or character name into an image prompt.** Prompts describe technique only.

## 2. The six things that make a panel read as real manhwa

Our old panels had clean ink and one hard shadow, and the owner liked that. They still did not feel like manhwa because they lacked these six things. Each one was seen in the real titles.

1. **A stated light source and big value shapes.**
   - **Real:** the panels studied have a key light you can point to (a floodlight, a red lamp, fire, a system window's glow). Dramatic beats add a thin rim on the figure's edge and large near-black shadow masses.
   - **Ours:** even, all-over light; everything in the middle values.
   - **Rule:** name the key light in every prompt. When there is a light behind the figure (a gate, the sky, fire), give the figure a thin rim along the edge that light catches. Let one third or more of a dramatic panel go dark.
2. **The background steps back.**
   - **Real:** establishing shots are detailed. Behind talk and action, the background turns pale, soft, a gradient, flat colour, speed lines, white or black. It is always lower in contrast than the characters.
   - **Ours:** the shop and the flat as detailed as the people.
   - **Rule:** follow the density ladder in section 8.
3. **The camera has a position.**
   - **Real:** a cut-off figure in the foreground, the lead in the middle, depth behind; low angles from behind; extreme close-ups of eyes, mouths and hands; figures cropped by the frame. Centred full figures at eye level were rare in the panels studied.
   - **Ours:** centred, one-point perspective, eye level, nothing in front.
   - **Rule:** every panel except `establish`, `system` and `chorus` has a foreground element or a crop.
4. **One dominant hue, one signature accent, and power in the complementary colour.**
   - **Real:** a lead's saturated uniform in a muted scene; violet power against an orange sky; an icy-blue burst against a red jacket.
   - **Ours:** muted colour everywhere, and the summon light never touches the faces.
   - **Rule:** section 5.
5. **Effects drawn as graphic shapes at the peak beats.**
   - **Real:** radial lines that close in from the frame edges, faceted debris, ink spatter, crackle shapes, flat colour bursts.
   - **Ours:** a thin ring and two motion ticks.
   - **Rule:** section 7.
6. **Faces that act bigger than life.**
   - **Real:** gritted teeth, sweat, blush hatching, a heavy-lidded smirk, a mouth close-up for a swallow.
   - **Ours:** mild expressions.
   - **Rule:** section 6.

## 3. The three style variants, and the choice (V2)

All three keep: drawn ink lines, hard-edged cel shadows on forms, no airbrushed skin and no text. They differ in line weight, how much light and atmosphere is painted on top, and how saturated the colour is.

| | **V1 · Bold ink** | **V2 · Cinematic cel** | **V3 · Painted cinematic** |
|---|---|---|---|
| **Seen in** | *The Lone Necromancer* | *Omniscient Reader*, *I'm the Max-Level Newbie* (close-ups) | *The Return of the Disaster-Class Hero*, *My S-Class Hunters* (action and sky panels) |
| **Line** | Thick black outer contours, tapered; outer to inner about 4:1; angular hair clumps | Crisp black; outer to inner about 3:1; heaviest on the jaw, the hair mass and overlaps | Thin and precise, sometimes scratchy; outer to inner about 2:1; black shadow masses do much of the drawing |
| **Shading** | Flat colour plus 1 hard cel tone; a 2nd only at night | Flat colour plus 1 hard cool cel tone; a smooth light wash from the key light on the lit side; a thin crisp rim from a back light, when the scene has one | 1 hard tone plus large black masses; strong rim and under-light from fire or power |
| **Colour** | Saturated, with hard warm/cool flips | Muted cool base (slate, navy, grey-blue); the light source and signature colours carry the saturation | Near-black plus one intense light colour (ember orange, cold blue or violet) |
| **Backgrounds** | Places in flat colour planes with little detail; flat colour, a two-colour gradient or speed lines behind reactions and action | Drawn and slightly softened in establishing shots; gradient, flat or speed lines elsewhere | Painted skies, smoke and haze with visible brushwork; figures stay sharp |
| **Effects** | Solid white or black speed lines, burst shapes, figures breaking panel borders | Radial lines, faceted debris; glow only around a real light source | Painted motion smears on limbs and weapons, embers, glows |
| **Strengths** | Reads best at phone size; the least "AI" look; easiest to keep consistent | Closest to the hunter titles the genre's readers know; keeps the ink and hard shadows the owner chose on 21 October | The most dramatic and premium-looking |
| **Risks** | Loud and cartoony, which can undercut the real-danger tone | The light wash and rim need discipline, or they turn glossy | Hardest to keep consistent; its haze and soft painting are close to the airbrushed first character sheets the owner called "too AI" in October |

**Chosen: V2.** The owner delegated the pick to Claude on 25 October. Claude chose V2 because:
- It sits closest to the modern hunter titles.
- It keeps method B's ink and hard shadows.
- It adds the light, rim and value that our panels lacked.

Section 4 says when each layer turns on, so peak beats always get more than talk panels.

## 4. The rendering stack

Build every image in these layers, as a webtoon colourist does. The table gives each variant's strength; "—" means the layer is off.

| # | Layer | V1 | V2 | V3 |
|---|---|---|---|---|
| 1 | **Ink:** tapered strokes, heavier on the silhouette, the shadow side and overlaps | heavy | medium | thin |
| 2 | **Flat local colour** from the design sheet's hex codes | saturated | muted base | muted base |
| 3 | **One hard cel shadow per material**, cooler and about 15–25% darker, drawn as a hard-edged shape | yes | yes | yes |
| 4 | **Deep shadow mass:** a second, near-black, hard-edged shape for night, menace and peak beats | night only | night and peak beats | all dramatic beats |
| 5 | **Source light wash:** a smooth gradient in the light's colour across the lit side. The only place a soft gradient is allowed on a figure. | — | yes, from the named key light | strong |
| 6 | **Rim light:** a thin crisp line of light along the silhouette edge, from a back light behind or beside the figure, usually on the side away from the key | — | thin | strong |
| 7 | **Highlights:** one band on hair, one or two catchlights per eye; glossy specular only on metal, glass and wet surfaces | small | small, plus specular on metal | specular on metal and wet surfaces |
| 8 | **Atmosphere:** embers, ash, dust or smoke, ONLY when something in the scene is burning, breaking or glowing | — | particles only | painted smoke and haze; motion smears on limbs and weapons, never on faces |

**Effort follows the beat** (all variants):

| Recipes | Layers |
|---|---|
| `impact`, `splash`, `monster-reveal`, `name-card`, `summon-arrival`, `tone-flip` | Every layer the variant allows |
| `anticipation`, `aftermath`, `link-view`, `carry` | 1–4, plus a light wash (5) from the scene's light or, in `link-view`, the summon's colour |
| `talk`, `reaction`, `eyes`, `plan`, `chorus` | 1–3, plus a light wash (5) when a coloured light source is in the scene |
| `insert`, `system`, `establish` | 1–3. In `establish`, the background gets the detail and the figures stay small. |
| `chibi` | 1–3, flat, gag background (ART_BIBLE A5b) |

## 5. Colour

### 5.1 Mood palettes (extends `MANHWA_ART_DIRECTION.md` section 4)

| Beat | Palette |
|---|---|
| Daily life | Muted, one hue per location (table 5.3) |
| Inside a gate | The wrong-coloured sky; violet shadows #3A2D4F |
| Danger arriving | Desaturate the scene and add ONE red accent #E0322B (an eye, a lamp, a warning) |
| Impact | A hot orange-to-yellow field (#FF8A1F to #FFD34D), or a white flash with ice-blue edges (#BFE9FF) |
| Power shown | The background turns the complementary hue of the power (violet power, orange world; cyan power, red-orange world) |
| Horror | Black and red only |
| System and Operator light | Cyan #3FE3F2 on navy #0B1530, lighting faces from the front |
| Flashback | Desaturated grey-blue, soft edges, ONE warm colour for the remembered person |
| Comedy | Flat pastel or a gag pattern |

### 5.2 Reserved colours

Each of these belongs to one thing **whenever it appears as light**: a glow, a thread, an eye-shine, a beam or a window. Never make anything else glow in these colours.
- Costumes, sets and impact fields may use neighbouring colours, as long as they are not glowing.
- Warning windows in the UI kit use danger red, not amber.

| Colour | Hex | Belongs to |
|---|---|---|
| Operator cyan | #3FE3F2 (navy ground #0B1530) | System windows; the CALL circle and seam; the light of the Operator protocol |
| Nib amber | #F2A93B | Nib's eyes and his LINK |
| The Hush | black-violet core #1A1026; violet ash #6B4C9A | Every hushed boss and Hush-spawn, and the black-violet core of every gate (the gates are the Hush's wounds). When hostile, it glows danger red. |
| Gate rim | cold white-cyan #D8F4FF, much paler than Operator cyan | The edge of every gate and the light spilling from it |
| Danger red | #E0322B | Warnings, red lamps, hostile eyes, the Hush's hostile glow, blood (as a splash or silhouette, never gore) |
| Each summon's signature colour | `MANHWA_ART_DIRECTION.md` section 5 | That summon's LINK and its seal-break light |

**Costume reds are not danger red.** Nib's scarf #B4262F and the Black Hound emblem #B3241E are deeper crimson. Never brighten them toward #E0322B.

### 5.3 Location colour keys, Arc 1

The architecture of each place is described in `CHARACTER_DESIGNS_v2.md` section 5.

| Location | Key light | Shadows | Accent |
|---|---|---|---|
| Gate site: a subway construction pit in Seoul, night | Cold white LED floodlights #E8F0F4 | Wet blue-grey concrete #2E3846 | Jaeha's orange vest; the gate's black-violet slit with a cold white-cyan rim |
| Inside the C-grade gate (ruined fortress halls) | Sickly green-dusk sky #8DB07A through cracks | Violet #3A2D4F | Red only with a threat |
| The boss room | Dim; green-dusk shafts from cracks in the ceiling | Dark grey-violet #2B2833 | The iron door's red lamp #E0322B; later the knight's red face |
| Gwanghwamun flash-forward | Red sky #B3261E fading to near-black #1E0A0C | Black silhouettes | The S-grade gate's cold rim; cyan Operator light on Jaeha |
| Rooftop room in Mangwon-dong, night | Warm lamp orange #F0B064 | Night navy #1B2440 | Green screens, city lights |
| Rooftop room, morning | Cool grey-blue daylight | Soft blue | Yellow sun on the laundry line |
| Gate exit, rescue scene | Red and blue emergency strobes on wet asphalt | Dark navy | Silver reflective stripes; a gold foil blanket |
| Flashback: the Han River gate, 4 years ago | Desaturated grey-blue | Soft | Minseok's orange vest, the one warm colour |
| Flashback: the Ninth Wall (chapter 3, "8 grey panels") | Grey, desaturated | Soft | Kett's mustard scarf, the one warm colour |

**The Hush stays the darkest thing in the panel.** Its black-violet #1A1026 must never sit on a shadow as dark as itself. Keep scene shadows around it at #2B2833 or lighter, and edge the hole with violet ash.

## 6. Faces, bodies and acting (refines ART_BIBLE A5)

- **Proportions.**
  - Adults are about 7.5 heads tall, realistic, with no fashion-model leg stretching.
  - Heights are in `CHARACTER_DESIGNS_v2.md`, and each panel keeps them.
- **Face construction** (method B, kept):
  - a defined brow ridge;
  - one shadow shape along the nose bridge;
  - an angular jaw;
  - a heavy upper lash line with one catchlight;
  - the mouth as one expressive line.
  - Every character has their own face shape (the design sheets give it).
- **Manhwa acting marks:**
  - blush hatching (3–5 short diagonal strokes on the cheek);
  - sweat drops;
  - a pulsing vein mark for anger;
  - shine on bared teeth for a grin;
  - eyes hidden in a dark band for menace or dread;
  - pupils shrunk to dots for shock;
  - a trembling double outline for fear.
- **Jaeha's two faces** (the script marks `face: public` or `face: private`):
  - **public:** a polite, slightly bowed smile with tired eyes;
  - **private:** narrowed eyes, a small one-sided grin, half the face in shadow.
- **Nib** is deadpan: a soldier's posture, mouth a flat line. He is never cute outside chibi panels.
- **Range in every chapter:**
  - one big reaction;
  - one comedic face;
  - one extreme close-up of eyes, a mouth or hands;
  - three or more silent acting panels.
- **Bystanders act with their bodies:** stepping back, dropping a weapon, freezing, hands over mouths.

## 6b. Acting and staging (from `research/ACTING_STUDY.md`, 25 October)

The owner's verdict on the last manhwa was that body positions, emotions and dialogue panels looked unnatural and AI-made. These rules come from a real summoner manhwa he chose. The script now names the acting for every panel (`acting`, `eyeline` and `foreground` in `SCRIPT_FORMAT_v2.md`). Draw exactly that.

**Bodies**
1. **Only husks stand like mannequins.** Everyone else carries their weight on one leg: hips tilted one way, shoulders the other, one knee looser. Never both feet square to the camera with the arms hanging.
2. **Every visible hand has a job.** It holds or touches something (a strap, the notebook, a cup, a weapon, a door frame, their own neck, hair or chin), gestures, or is hidden in a pocket or behind the back. The script's `acting` line names it.
3. **Heads turn and tilt.** No level, centred, front-facing head in a talk panel. The eyes turn a little further than the head.
4. **The body moves first.** A reaction shows in the shoulders, hands and feet (a flinch, a step back, a lean in, shoulders up), not only in the face.
5. **Groups are staggered.** People stand at different depths and overlap, with heads at different heights, each in their own stance. No lineups, except the lineup sheet.
6. **Show height in the frame.**
   - Nib (105 cm) with Jaeha (178 cm): put Nib low in a corner looking up and Jaeha looking down, or put the camera at Nib's eye level and crop Jaeha at the chest.
   - For a longer talk, Jaeha crouches or sits on the floor to Nib's level, as a person does with a small creature.
   - Big figures (Mok, Borro, the knight) are cropped by the top of the panel so their size presses down.
7. **Hands work while the mouth talks.** Give talking characters a small job: holding a door, poking a fire, setting something down, writing in the notebook, checking a weapon, holding a cup.
8. **Contrast postures in one frame:** one bows while the other stands upright; one leans in while the other leans back; an aggressor leans forward and looks down.
9. **Fear takes the whole body:** trembling outline marks, sweat, a hand raised defensively and the other pressed to the chest.
10. **Stopping on the way out.** A character halts at a door, hand on the handle, and looks back over the shoulder for the line that matters.

**Faces**
1. **Use the whole ladder,** from small to big: a sidelong glance; a half-lidded smirk; a strained smile with a sweat drop; wide eyes with small pupils; a scream with the mouth wide open.
2. **Comedy faces are simplified,** not chibi bodies: blank white eyes, dot eyes, an anger vein, a scratch of the cheek on a dotted or flat pattern background. Use them only on comedy beats.
3. **Asymmetry reads as alive:** one brow higher, one corner of the mouth, one eye narrower.
4. **Hide the eyes on purpose:** glasses turned to white glare (Seoa when she is calculating), a dark band of shadow for dread or menace.
5. **Use sweat drops freely** for nerves and strain.
6. **Nib's deadpan beat:** a silent panel of his flat, half-lidded stare with a "......" bubble, straight after someone else overreacts.
7. **Small marks:**
   - question marks floating round a confused head;
   - scratching the back of the head when embarrassed;
   - a sparkling face beside a sweating, darkened face for comic contrast;
   - small hand-lettered asides outside the bubbles (written by the script, set by the letterer).

**Talk panels**
1. **Eyelines go to the other person.** Faces are three-quarter or profile, looking off-panel toward whoever they are talking to. Only shock or comedy reactions and system panels face the camera.
2. **Shoot over the listener's shoulder.** The listener's shoulder, the back of their head, or a big prop fills a corner, cropped and kept simple, while the speaker sits in the middle distance.
   - Stay on the same side of the two people for the whole exchange, so they never swap sides of the frame.
3. **Change the shot size every panel** in an exchange. A typical run: a wide shot of who is where, a two-shot, alternating close-ups, a hand or prop insert, a reaction, and an extreme close-up of an eye or mouth on the line that matters.
4. **Crop boldly.** Cut the top of the head, cut at the chest, push a face to one edge. A full figure centred with even headroom belongs only in `establish` panels.
5. **Frame arrivals and confrontations** between two figures seen from behind in the foreground.
6. **Use high and low cameras:** look down on a desk, a counter or a group; look up at a confident speaker.
7. **Use torso shots:** frame the speaker from neck to waist with the face cut off, and let a hand gesture carry the line.
8. **Overlap figures in group panic:** one shouts and points while another recoils behind him.

**Small sound effects.** Reactions and small movements get a small `quiet` SFX placed near the movement: GLANCE, FLINCH, TWITCH, GULP, GRIN, SIGH, STEP STEP, SHAKE SHAKE, TAP TAP, PLOP. The script writes them; Codex leaves room for them.

**Panel shape follows the shot:** tall and narrow for a full figure or two stacked faces; wide for a two-shot, a walk or a group; small for a reaction.

## 7. Effects (refines ART_BIBLE A8)

| Effect | How it is drawn | Where |
|---|---|---|
| **Focus lines** | Crisp radial black or white strokes closing in from every edge of the frame toward the face or contact point; the centre stays clear | Shock, reveals, impacts |
| **Speed lines** | Parallel tapered strokes in the direction of motion; white on dark, black on light | Dashes, falls, sweeps |
| **Impact burst** | A hard-edged star or jagged shape at the contact point, on a hot or white field; short thick radials | `impact` |
| **Debris** | Faceted polygons with one light edge and one dark side, flying out from the impact; dust as clumped shapes, not fog | Stone, armour, husk shells |
| **Crackle** | Thin jagged white or coloured lines, like broken glass or lightning | Energy, the husk cracking, gate edges |
| **Ink spatter** | Small black flecks and drops thrown off a dark power | Hush power, a heavy blow on a monster |
| **Glow** | A soft gradient ONLY around a real light source (the CALL seam, a red lamp, fire, a core), falling off fast. Never a haze over the whole image. | Sources only |
| **Embers and ash** | Small hard-edged orange flecks and grey flakes | Only where something burns or is destroyed |
| **Motion smear** | A painted streak trailing a fast limb or weapon | V3 only; never on faces |
| **Camera flash** | A white cross-shaped star flare | Only where a real camera flashes |
| **Summon (CALL)** | Unchanged from ART_BIBLE A8: a cyan floor circle, a thin vertical seam of light, the summon stepping through. The new part: cyan light from the circle lights the faces from below. | Every CALL |
| **The husk as a door (chapter 1 only)** | The husk's white shell cracks along glowing cyan lines, glitching at the edges (offset red and blue fringes), and bursts outward in white shards | Chapter 1 |
| **Gate opening** | Unchanged from ART_BIBLE A8: a hairline crack, then a door-height black-violet slit with a cold white-cyan rim and wrong-coloured light inside | Every gate |

## 8. Backgrounds and the page

**The density ladder:**

| Panel | Background |
|---|---|
| `establish` | 100%: drawn, detailed, the light source visible; figures small |
| Medium shots in a known place | About 50%: big shapes and a few telling props; detail fades toward the edges |
| `talk` | About 20%: simplified shapes, a soft gradient, or a pale flat version of the place |
| `reaction`, `eyes`, `impact`, `tone-flip` | 0%: flat colour, a gradient, radial lines, white or black |
| `splash`, `summon-arrival` | 0–20%: the effect owns the panel; the place is only suggested |
| `monster-reveal` | About 20%: the monster is the background |
| `name-card` | A gradient in the card colours (`CHARACTER_DESIGNS_v2.md`), or the scene at about 50% when the brief asks for it |

- **The background is always lower in contrast than the characters,** and paler or darker as a whole. Faces are never the same value as the wall behind them.
- **Use the frame.**
  - Put a foreground element in front of the subject: a pillar edge, a shoulder, a railing, a hand, a silhouette.
  - Let the frame crop figures.
  - Show scale with a tiny figure or a door next to the big thing.
- **Page colour carries mood:** white for daily life, black for dread or grief, navy for system-heavy moments. The script sets this with `gap`, and the letterer joins the panels.

## 9. Monsters and the Hush

- **Silhouette first.** A monster must read as a black shape at phone size. Give it one exaggerated feature.
- **Rougher than the people.** Draw monster hide, stone, feathers and ash with rough dry-brush texture and broken lines. People stay clean. The contrast tells the reader what is not human.
- **One glowing tell or weak point.** The script uses it: Jaeha reads tells.
- **Hushed heroes in human form keep who they were** (the knight-commander; later Maud and Caldric): a sigil, a torn banner, a surgeon's apron.
  - Their face is a black-violet hole with cracked edges leaking violet ash.
  - It glows danger red only when the script says they are hostile.
- **Beast-shaped bosses** (the drowned hound in chapter 8, the serpent in chapter 12, and so on) carry only a small black-violet crack leaking violet ash somewhere on the body. That way the chapter 50 reveal, that they were people too, still lands.
- **Violence happens between panels.** No gore close-ups.

## 10. Prompt kit

**Order of every image prompt:**
1. the V2 STYLE BLOCK (10.1), followed by the CLEAN-UP LINE (10.4);
2. the recipe line: shape, camera, key light and calm zone (10.2);
3. the scene: who, where, the action;
4. the ACTING LINES (10.5): the script's `acting`, `eyeline` and `foreground`, word for word;
5. the prompt snippet of every character in the panel (`CHARACTER_DESIGNS_v2.md` section 8), word for word. Where the scene changes something (a prop in a hand, a hood up, a different outfit), the scene wins: drop or change the clashing words;
6. the NEGATIVE BLOCK (10.3).

Pass the model sheet of every character in the panel as a reference image, once the sheets exist. Never pass real webtoon images, the old cast's sheets (Taeo, the old Nib) or old chapter panels.

### 10.1 STYLE BLOCK (paste the V2 block exactly; V1 and V3 are not used)

**V1 · Bold ink** (not used; kept for reference)
> Korean webtoon panel, digitally inked and cel-coloured by a professional webtoon artist. Bold black G-pen ink: thick tapered outer contours, much thinner inner lines, hair cut into angular clumps. Flat saturated colour with one hard-edged cel shadow per material, no soft blending on skin, hair or clothes. Strong warm-against-cool colour contrast. Places are drawn in flat colour planes with little detail; behind reactions and action, the background drops to flat colour, a two-colour gradient or crisp radial speed lines. Effects are solid graphic shapes: white speed lines, black focus lines, jagged burst shapes. Expressive, exaggerated faces. Reads clearly at phone size.

**V2 · Cinematic cel** (THE style block)
> Korean webtoon panel, digitally inked and coloured by a professional webtoon studio. Crisp black ink with tapered strokes, heavier on the outer silhouette, the jaw, the hair mass and where forms overlap. Flat local colour with one hard-edged cool cel shadow per material. One named key light: its colour washes smoothly over the lit side. If the scene names a back light, it draws a thin crisp rim along the figure's silhouette. Everything else stays flat. Muted cool base palette of slate, navy and grey-blue, so the light source and the character's signature colour carry the saturation. Background simplified and lower in contrast than the characters. Small crisp highlights; glossy specular only on metal and wet surfaces.

**V3 · Painted cinematic** (not used; kept for reference)
> Korean webtoon panel with cinematic painted lighting by a professional webtoon studio. Thin precise ink lines under bold lighting: large hard-edged near-black shadow masses, a strong rim light from behind, under-lighting from fire or power. Painterly sky, smoke and dust with visible brush texture, while the figures stay cel-shaded and sharp. High contrast between near-black shadow and one intense light colour. Painted motion smears only on fast limbs and weapons, never on faces. Floating embers or ash only where something burns.

### 10.2 The recipe line (light and value per recipe)

| Recipe | Key light and value plan (add to the camera and shape from `MANHWA_ART_DIRECTION.md`) |
|---|---|
| `establish` | The location's key light from table 5.3, visible in the frame; full value range; figures small and mid-value |
| `talk` | Key light from one side; faces the lightest values; background one or two steps darker or lighter and simplified |
| `reaction` | Front-side light on the face; a flat or gradient background in the mood colour |
| `eyes` | Light across the eyes only; everything else in shadow or flat colour |
| `insert` | Hard top light on the object; plain background |
| `name-card` | Key light from the side the character faces; a back light draws the rim on the other edge; a gradient background in the card colours (design sheet), or the scene at about 50% when the brief asks for it |
| `monster-reveal` | Back light or rim on the monster; the MC a dark silhouette in the foreground; the scene desaturated; one red accent |
| `anticipation` | Low, tense light; muted; the figure darker than the background |
| `impact` | NO scene light: a hot orange or white field; strongest contrast of the chapter; large SFX space along the diagonal |
| `aftermath` | Low, quiet light; dust settling; no motion lines |
| `tone-flip` | Black and red only |
| `summon-arrival` | Cyan up-light from the floor circle on every face; the seam the brightest point; the rest of the scene darker |
| `link-view` | Jaeha's face lit in the summon's colour; a thin vignette in the same colour on the point-of-view side |
| `carry` | Flat background; a translucent white impact ring on his body; a hard shadow under the brow |
| `system` | Cyan front light on the face; the window area left EMPTY and dark |
| `plan` | The battlefield slightly desaturated; clean cyan lines and arcs only (no text) |
| `chorus` | Even, flat light; every face readable |
| `splash` | The effect is the key light; everything takes its colour; the peak of the chapter's contrast |

### 10.3 NEGATIVE BLOCK (paste exactly, every prompt)
> No text, letters, numbers, speech bubbles, captions, sound-effect lettering, interface windows or readable signs. Emblems without letters are fine; no brand logos or wordmarks. Not a 3D render, not a photograph, no photographic background. No airbrushed skin, no plastic gloss on skin or hair, no haze or bloom over the whole image, no depth-of-field blur, no lens flare unless a real camera flash is in the scene. No watermark or signature. Correct hands with five fingers. No chibi proportions unless the brief says chibi.

### 10.4 CLEAN-UP LINE (paste right after the STYLE BLOCK, every prompt, from 25 October)
> Hand-made webtoon colouring: each garment has only a few large, opaque, clean-edged shadow shapes, placed in its real folds; no scattered translucent streaks, zigzag shards or crumpled-foil folds. Worn cloth shows a few small frayed notches and loose threads, never sawtooth edges along every edge. Plain shoes and clothes with no logos, stripes or brand marks. Every strap, buckle, pocket and seam is attached and has a purpose; no stray stitch marks. Matte skin, hair and stone; no 3D, low-poly or plastic look.

### 10.5 ACTING LINES (every chapter panel with a character in it; not model sheets)
- **Write the acting as physical facts, one sentence per character,** in this order: stance and weight; what each hand is doing; head and eyes; the face. Use verbs caught mid-action ("shifting his weight", "halfway through turning", "mid-step"), not adjectives like "natural" or "dynamic", which do nothing.
- **Then the eyeline** ("Mok looks down at Jaeha; Jaeha looks up at Mok") **and the foreground** ("Jaeha's right shoulder and the back of his head fill the right third, cropped by the frame").
- **Add this sentence to every panel prompt that passes a model sheet:**
  > The reference images show only the characters' design (face, hair, clothes, colours, props). Do not copy their standing poses or front-facing angles: pose, camera and expression come only from the scene text.

## 11. Check every image before you accept it

**From 25 October, the owner's order: be strict.** An image that looks AI-made, or has any weird detail, is a reject even when the locks are right. Run 11b on every image as well as the list below.

Redo it (up to 3 tries) if any answer is no:
1. Can you point to the key light, and does it match the location key? (In `splash` and `impact` panels, the effect or the colour field is the key.)
2. Is there a rim, a value mass or a colour field that separates the subject from the background at thumbnail size? (Shrink the image to 200 px wide to check.)
3. Is the background lower in contrast than the characters, and at the right density for the recipe?
4. Is there a foreground element or a crop, unless the recipe is `establish`, `system` or `chorus`?
5. Is the camera what the recipe says, and different from the panel before?
6. Do the faces act the emotion the script names?
7. Does anything glow in a reserved colour that doesn't own it?
8. Does every character match their design sheet and locks (`CHARACTER_DESIGNS_v2.md`)?
9. Is the calm zone empty and simple?
10. No text, except the T on Jaeha's vest patch when Jaeha is in the image (his snippet asks for it; nobody else ever wears a letter). Correct anatomy (count fingers, check joints). Nobody cute who shouldn't be.
11. Does it look drawn, not rendered? Check for: ink lines, hard shadow edges, no plastic skin, no haze.

### 11b. The strict checks: no AI look, no weird details

Reject the image if any of these show. Look at it full size, then at 200 px wide.
1. **Shard shading.** Shadows broken into many small translucent streaks, zigzags or triangles. A webtoon colourist puts a few large opaque shapes per garment: under the collar and chin, under the arms, along the side away from the light, under pocket flaps and straps, and in the 3–6 folds the garment really has (elbows, waist, where a strap pulls).
2. **Sawtooth wear.** Every edge cut into jagged teeth, or cloth shredded into strips. Worn cloth gets a few small notches and loose threads in two or three places; a scorched hem is uneven and darkened, not shredded.
3. **Brand marks.** A swoosh, three stripes, a checkmark, a wordmark, or a famous branded shoe or bag shape. Shoes are plain.
4. **Nonsense gear.** A strap that starts or ends nowhere, a buckle with no strap, a pocket on top of a pocket, a duplicated prop, stitch or staple marks scattered over cloth, a ring or tag hanging for no reason. Every strap, buckle, pocket and seam has a job.
5. **Template faces.** A generic pretty face that ignores the design. Check the face line by line against the design text: skull, brow, nose, mouth, jaw, eyes.
6. **3D or plastic look.** Glossy skin or hair, airbrushed gradients, bevelled low-poly shapes, a CG sheen on cloth, stone or skin.
7. **Anatomy.** Count the fingers and toes; check every joint bends the right way; eyes level; limbs the same length in every view.
8. **Background.** Sheets: flat #E9E9EC only, no vignette, gradient or texture, and no shadow pool larger than a soft contact shadow under the feet.
9. **Modesty.** Kang Seoa is 15: her skirt reaches the top of her knee, and nothing in her images is styled to show skin. Adults wear exactly the design's clothes.

### 11c. Acting checks (chapter and test panels only)

These do not apply to model sheets, whose turnarounds stand neutral by design. Reject a panel if any of these is true:
1. **Mannequin stance.** Someone other than a husk stands square to the camera with their weight on both feet and their arms hanging.
2. **Idle hands.** A visible hand is limp with no job, floats, is duplicated, or does something the `acting` line did not ask for.
3. **Wrong eyeline.** In a talk panel, the speakers look at the camera instead of at each other, or the eyelines do not match the script's `eyeline`.
4. **Wrong emotion.** The face does not read as the script's emotion within one look at phone size, or a calm, model-like face appears on an emotional beat.
5. **Flat staging.** In a non-`establish` panel, the subject is centred with even headroom and nothing is cropped. Or two talk panels in a row have no foreground element, crop or over-the-shoulder.
6. **Repeated camera.** The same camera angle and shot size as the panel before.
7. **Lineup.** Three or more people side by side at one depth with their heads at the same height.
8. **Copied sheet pose.** A character stands in their model sheet's front-view pose.

## 12. Ours against real, in one line each

The full comparison is in `research/RENDERING_STUDY.md` section 3.
- **`style_test/abcd/compare.png`:** clean ink and hard shadows (keep), but even light and a background as busy as the people (fix with sections 4 and 8).
- **`style_test/p3_nib_reveal.png`:**
  - a centred, eye-level full figure, and the cyan summon light doesn't touch any face (fix with the `summon-arrival` line in 10.2 and the camera rule in section 2);
  - it also shows the OLD Nib design, which is retired.
