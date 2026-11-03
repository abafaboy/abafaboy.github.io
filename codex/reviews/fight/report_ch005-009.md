# Fight audit and re-storyboard: My Summons Go First, ch005–ch009

## 0. Read first

**The main finding changes the fix plan.** In ch006–ch009 the raw art usually draws the hit, and the lettering hides it. I checked this by putting the raw art (`chapters_v2/chNNN/art/PNN.png`) next to the lettered judge pages:

| Panel | What the raw art shows | What the lettered page shows |
|---|---|---|
| ch006 P40 | The sword going into the swarm mother's neck, and three darts in her flank | "SHK SHHUNK" lettered over the hands, the blade, the neck and the darts |
| ch007 P42 | Both fists on the grip, and the blade going through the white T patch | "SHUNK" over the hands and the grip |
| ch008 P38 | The jaws closing on Jaeha's forearm | "CHOMP" over the jaws and the arm |
| ch008 P47 | Nib kneeling on the hound's skull with both knives raised | "WEE-OO WEE-OO" over Nib |
| ch008 P48 | The knife tips at the skull, with a violet spark | "SHHUNK" over the contact point |
| ch009 P39 | The black hand round Jaeha's shin | "GRAB" over the grabbed leg |

- **The scripts put the SFX there.** In four of these panels the script's own `sfx.at` for an XL impact SFX is on, or within a few percent of, the contact point in the raw art: ch006 P40 SHHUNK [0.62, 0.40], ch008 P38 CHOMP [0.52, 0.30], ch008 P48 SHHUNK [0.30, 0.30], ch009 P39 GRAB [0.40, 0.30].
- **XL is too big.** XL lettering spans half the panel width or more, so it covers a fighter wherever it lands.
- **So part of the fix is re-lettering, not redrawing.** The list of panels that only need re-lettering is in section 7.

**Checking the ch011 calibration against ch005–009:**

1. **"Bodies are posed."** Confirmed for Nib's strikes and for the set-up panels:
   - ch006 P27: Nib in a front-facing lunge with both arms flung out.
   - ch006 P34: a symmetric T-pose crouch.
   - ch008 P43 and P48: Nib squatting on the hound's head. In P48 he holds the knives like ski poles.
   - ch006 P19: a five-person line-up posed for the camera.
   - ch006 P26: Jaeha with his arms out like a magician's "ta-da".

   It does not hold for the humans and the monsters, who get real lines of action: ch006 P21 (the leader's swing), ch008 P37 raw (Jaeha's sprint has a proper stride), ch008 P44 (Nib flung out like a flag), ch009 P39 (Jaeha thrown off balance) and ch009 P28 (the bell silhouette's full-body swing).
2. **"The camera stays at eye level, medium or wide."** Partly corrected. The angles vary more than in ch011: ch006 P20 is low between the party's boots, P27 is low with a dutch tilt, ch007 P44 looks straight down a chute, ch008 P43 is high and tilted, P48 is a worm's-eye shot. Confirmed that no fight panel foreshortens anything toward the camera (no blade, jaw, claw or bolt coming at the reader; the nearest is ch006 P20's lead rats). There is also no extreme close-up of a weapon, a contact point or a planted foot inside any exchange.
3. **"Hits never visibly land."** Mostly corrected, as shown in the table above. The art itself fails to show contact in only two places:
   - Nib's swarm cuts: in ch006 P27 neither blade touches a rat, and in P28 the rats lie whole inside violet puffs.
   - The hound kill, ch008 P48: a small spark at the back of the skull, the brow crack not visible, and no drive in his body.
4. **"The SFX cover the fighter."** Confirmed. 16 fight panels have an L or XL white impact SFX across a fighter, a hand or the contact point:
   - ch006 P03, P16, P21, P27, P34, P40
   - ch007 P42
   - ch008 P36, P37, P38, P40, P43, P44, P47, P48
   - ch009 P39
5. **"Few speed lines or impact bursts."** Partly corrected. The `impact` panels mostly have a flash background with radial lines (ch006 P21, P34, P40; ch007 P42; ch008 P38, P43; ch009 P39). Confirmed for the swarm whirl (ch006 P28) and for the hound's thrash and kill (ch008 P44, P47, P48 keep the detailed car-park background; P48 is a waterfall texture).
6. **"The choreography doesn't read."**
   - Confirmed for ch006: P28 is an overhead shot in the middle of the fight; P33 says the wave comes from both LEFT tunnels but P34 draws rats on both sides; P40 crams four beats into one panel.
   - Confirmed for ch008's bite: between P37 and P38 the hound swaps sides of the frame, and it is dog-sized in P37 but horse-sized in P40 and P43.
   - Corrected for ch007, where every beat gets its own panel (plan, decoy, stab, lever, torrent, standoff), and for ch008 P45–P47 (arrow, car alarm, the blind hound turns its head).
   - There are no tangles like ch011 P51 in these chapters. The nearest is ch006 P30: three figures doing three different things.
7. **"System windows sit on the action."** Mostly corrected for ch006 and ch008, where the windows sit on system or quiet panels (ch006 P26, P36; ch008 P09, P42, P52, P53). Three exceptions:
   - ch008 P07: the window sits on the yank gag.
   - ch006 P41: two windows overlap, the first one's text is cut to "THE GATE WI… MIN", and together they cover every face, including the leader's "staring at my sword" beat.
   - ch009: the countdown timers are lettered onto the action (P38, P43, P51, P52, P54).

**Rule 7 of `MANHWA_ART_DIRECTION.md` ("violence happens between panels"): drop it as written.**
- In these chapters it is not what hid the hits. The scripts already describe contact (ch006 P40 "drives his sword into its neck"; ch008 P38 "jaws clamp onto Jaeha's LEFT forearm"; P43 "both knives driving down into the violet Hush crack"), and the image model drew it.
- But it contradicts the standard (#5), and it gives permission for "moment before, then aftermath" storyboards.
- Replace it with: **"Contact is shown; gore is not. Draw the blade meeting hide or claw, jaws closing on a sleeve, a sword entering a monster's neck as a burst of violet ash. No wound close-ups, no severed parts; human blood only as a small spray or stain."**

**Grades**

| Ch | Sequence | Panels | Grade |
|---|---|---|---|
| 005 | No fight. Comic sword drop (an action beat, not a fight) | P45–P47 | 5 |
| 006 | 6A Trap walk (action gag) | P02–P03, P16–P17 | 5.5 |
| 006 | 6B Ash-rat swarm | P19–P37 | **4** |
| 006 | 6C Swarm mother | P38–P42 | **4** |
| 007 | 7A Grain-trap ambush | P33–P56 | 6.5 |
| 008 | 8A Rooftop chase (action, not a fight) | P01–P11 | 7 |
| 008 | 8B Drowned hound | P27–P49 | **5.5** |
| 009 | 9A The bell's refusal (dramatic beat) | P25–P29 | 8: no storyboard; the model to copy |
| 009 | 9B The Hush's grip | P38–P54 | **5** |

**Panel budget, checked against the 30% limit:**

| | Panels now | Panels after |
|---|---|---|
| ch006 fights | 28 | 36 (+29%) |
| ch007 | 24 | 25 |
| ch008 hound | 23 | 26 |
| ch009 | 17 | 18 |

**Work in total:** about 42 panels to draw (13 of them new), plus about 13 panels that only need re-lettering.

Marks used in the tables: KEEP, REDRAW, CUT, NEW. "As drawn" means unchanged.

---

## 1. Chapter 5

**No fight sequence.** The chapter is the memorial, the offer, home and Kanghan. The only action beat is the sword gag (P45–P47): the Ninth Wall blade drops out of the slit and its weight yanks Jaeha down. **5/10 as an action beat.**

**What's wrong:** P46's joke is "a weak man pulled down by a sword longer than he is tall". What's drawn is Jaeha on one knee with his RIGHT arm straight up on the grip, chest out, and the blade planted at about 30°. It reads as a hero planting his sword, so the weight never reads. The KRAKK placement beside the point and the white flash with speed lines are right.

| new | replaces | shape | camera | action | effects in the art | SFX | dialogue kept |
|---|---|---|---|---|---|---|---|
| P45 · KEEP | P45 | wide | as drawn | as drawn | as drawn | – | Jaeha: "ALSO, I GOT SOMETHING FROM THE BOSS. WATCH THIS." |
| P46 · REDRAW | P46 | tall | Floor level beside the table, low, dutch tilt 10°, wide lens. | The blade (longer than Jaeha is tall) has just dropped point-first out of the cyan slit and punched straight down through the vinyl into the concrete, vertical. Its weight has yanked Jaeha after it: both knees slammed onto the floor, both hands clamped on the grip at face height, arms straight and dragged down, shoulders hunched to his ears, eyes popping, mouth an O. | White flash. Downward speed lines along the blade. A radial crack burst and flying concrete chips at the point. Ramen bowls hopping in the blurred foreground. | KRAKK, impact L, beside the point on its left (as now). | – |
| P47 · KEEP | P47 | wide | as drawn | as drawn | as drawn | – | Nib: "YOU'RE WEAK." / Jaeha: "I'M AWARE." |

---

## 2. Chapter 6

### 6A. Trap walk (P02–P03, P15–P17): 5.5/10

Nib, playing a husk, walks first and "blunders" through a dart trap and a net trap without looking.

**What's wrong**
- **P03 is a standing portrait, not a dodge.** Nib is upright and square to a low camera with his arms hanging. The darts pass a forearm's length behind his head and his head stays level, so there is nothing to see him dodge. SHK SHK SHK is lettered across his chest and left arm, and FWIP collides with it.
- **P04 references a catch that never happened.** Nib points a dart at the leader's grip that he was never shown catching.
- **P16 reads** (Nib one step past the falling net, Jaeha wincing), but KRASSH is lettered across Jaeha's chest.

| new | replaces | shape | camera | action | effects in the art | SFX | dialogue kept |
|---|---|---|---|---|---|---|---|
| P02 · KEEP | P02 | strip | as drawn | Nib's bare foot presses the brick down. | as drawn | CLICK (as now) | – |
| P03 · REDRAW | P03 | wide | Low at the water's surface, three-quarter front, wide lens, dutch tilt 10°. | Nib walks toward the camera in his stiff husk walk: arms hanging, LEFT foot planted in the water, RIGHT foot lifting. He tips his head a hair toward his LEFT shoulder, so the lead dart (fired from a hole in the brick wall at screen-left) streaks a finger's width above his RIGHT ear, lifting a few strands of hair. His uncovered right eye slides toward it; his face stays deadpan. Two more darts follow behind it. The party is small and blurred far behind. | Speed lines along each dart. Brick dust puffing from the three holes. The background behind the darts darkened to grey speed streaks. | SHK SHK SHK, impact M, along the dart lines between the wall and his head (top-left), never over him. "fwip", quiet S, where the lead dart leaves the frame at the right. | – |
| P03b · NEW | – | inset-r | Extreme close-up beside Nib's head, telephoto. | His long grey-green RIGHT hand snaps up beside his ear and pinches the third dart out of the air between two fingers; the dart's tail still quivers. His eye has not moved. | Speed lines ending at the fingers. A small radial tick at the pinch. Flat dark background. | TAK, quiet S, beside the fingers. | – (sets up P04, where he points with this dart) |
| P16 · KEEP, re-letter | P16 | wide | as drawn | as drawn | as drawn | Move KRASSH (impact L) up over the net into the vault at top centre, rot −6, clear of Jaeha. | – |
| P17 · KEEP | P17 | inset-r | as drawn | as drawn | as drawn | – | Jaeha: "AND THAT'S TRAP NUMBER SEVEN. VERY LUCKY HUSK." |

### 6B. Ash-rat swarm (P19–P37): 4/10

A swarm floods a five-way junction. The clients flail, Bomi's blind arrow drops a brick on a rat, Jaeha sends her drone down an empty tunnel, and Nib in field form shreds the swarm unseen.

**What's wrong**
- **P19: a line-up, not an ambush.** Five people stand facing the camera, Jaeha front and centre with his notebook and Bomi mid-pose. Nib, who walks first, isn't in the panel. The violet eyes in the five tunnel mouths are pin-pricks that vanish at video size. SKRITCH ×3 runs across the tops of everyone's heads.
- **P20 is the best panel in the fight.** Low between the party's boots, the lead rats foreshortened at the camera. KEEP.
- **P21 is lively but crowded.** The leader's swing arc and the white flash work, but the panel carries two actions (his miss and the spearman's fall), and SPLASSH covers both men's legs.
- **P22 packs three beats into one panel:** the release, the arrow in the vault, the brick on the rat. Bomi stands square to the camera instead of in the scripted "wobbly stance".
- **P26:** Jaeha square to the camera with his arms out in a "ta-da"; the rats are a flat band at his waist behind him.
- **P27, the peak, is a poster.** The camera is dynamic (low, tilted, rat silhouettes in the foreground), but Nib is posed: a front-facing lunge with both arms flung out and the knives at arm's length. Neither blade touches a rat, and the rats around him are whole. "SHK SHK SHRAKK" is lettered across his raised arm, between the knife and his head.
- **P28 is a geography shot in the middle of the fight.** From straight overhead, Nib is about a seventh of the panel height, so the spin can't be read. The rats lie whole inside violet puffs, and POF ×4 sits across the lower half.
- **P29 is good.** The rat's teeth are on the calf against a red flash, and CHOMP sits below the bite. KEEP.
- **P30 has three figures doing three things.** Yerin heals, the spearman props himself up, Jaeha kicks. Jaeha's kick is a stiff-legged step, and the rat is already in the air past his boot, so no contact is drawn.
- **P33 has moved to a different place.** The plan is drawn in a straight corridor with two arches, not the round five-way junction of P19 and P28.
- **P34 contradicts the plan.** Nib is a symmetric front-facing T-pose crouch. The rats pour in from BOTH sides of the frame, although P33 has just said "both LEFT tunnels". SHRRAKK covers his legs and his right knife.
- **There is no exchange.** Nib never dodges, never takes a hit and never chains one cut into the next. A reader can't narrate a single cut.

**Storyboard: 19 panels → 24.**
- Screen direction for every Nib panel: the rats come from screen-LEFT (the kept P33 line puts the wave in the left tunnels), and Nib always faces and cuts toward screen-left. Never flip.
- Peaks: P27 and P34, both tall.

| new | replaces | shape | camera | action | effects in the art | SFX | dialogue kept |
|---|---|---|---|---|---|---|---|
| P19 · REDRAW | P19 | wide | High three-quarter (3 m), wide lens. A geography shot, which is allowed at the start. | The round junction of five brick tunnels. The party is bunched back to back in the middle, facing OUTWARD, not at the camera: the leader and the spearman each face a tunnel with their weapons up; Bomi pulls her bow off her back; Yerin is pressed against Jaeha's back; Jaeha holds the notebook up, eyes moving. Nib stands a step ahead of them, crouched low, head turned to the two left tunnels. In every tunnel mouth, a cluster of 6–10 violet eye-pairs, large enough to read at video size. | Dim and desaturated; violet is the only colour. No speed lines. | SKRITCH SKRITCH SKRITCH, quiet M, inside the darkest tunnel mouth (top-left), never over heads. | – |
| P20 · KEEP | P20 | tall | as drawn | as drawn | as drawn | Reduce KREEEEEEE to L and keep it in the vault above the swarm. | – |
| P21 · KEEP, re-letter | P21 | wide | as drawn | The leader's wild miss and the spearman's fall read as one chaos beat. | as drawn | Move SPLASSH (impact M) into the bottom-right corner under the spearman's boot, off both men's legs. | – |
| P22 · REDRAW | P22 (the shot) | inset-l | Chest height, three-quarter from Bomi's left, slight high angle (never below her chest). | Bomi has just loosed blind: eyes squeezed shut, chin tucked, bow in her LEFT hand thrust up at about 60°, her RIGHT hand flung back past her right ear by the release, ponytail whipping. Her weight is on her back (right) foot, knees buckled inward: the wobbly stance. | One speed line along the arrow as it leaves the top of the frame. Tension lines behind her. Muted tunnel. | TWANG, quiet S, beside the string. | – |
| P22b · NEW | P22 (the accident) | tall, narrow (half width) | From high in the vault, looking straight down. | Top: the arrow stuck in the mortar, one brick tipping out of the vault. Middle: the brick falling. Bottom: it lands flat on one rat's head and squashes it into the water; the rats beside it scatter. | A vertical motion trail on the brick. A comic impact star at the head. | BONK, comic M, beside the star, off the rat. | – |
| P23 · KEEP | P23 | inset-r | as drawn | as drawn | as drawn | – | Bomi: "I HIT ONE! DID EVERYONE SEE THAT? I HIT ONE!" |
| P24 · KEEP | P24 | wide | as drawn | as drawn | as drawn | – | Jaeha: "BOMI! THE BIG ONE WENT DOWN THAT TUNNEL! GET IT ON CAMERA!" |
| P25 · KEEP | P25 | strip | as drawn | as drawn | as drawn | VWEEE (as now) | – |
| P26 · REDRAW | P26 | wide | Waist height, three-quarter from Jaeha's right, slightly low. | Jaeha turned three-quarter to the camera, weight on his back foot. The notebook is snapped shut in his LEFT hand at his hip. His RIGHT hand, at shoulder height, flicks two fingers toward Nib off-panel left: a command, not a "ta-da". Eyes cold and narrowed. Behind him, a dark band of rats with violet eye-pairs. | Cyan window light on his face from the front. Upper half: empty dark vault for the window. | none | Window [NIB · FIELD FORM 05:00 · LINKED] (kept). |
| P27a · NEW (anticipation) | – | strip | Extreme close-up from behind Nib's right hip. | Both of his long four-fingered hands whip the two knives out of the crossed sheaths at the small of his back at once. The blades slide out pointing down along his forearms (reverse grip). The amber outline flickers on along his arms. | Speed lines along the draw. Flat black background. Amber rim light. | SHING, quiet S, beside the right blade. | Off-panel Jaeha (intense): "NIB. NOW. NOBODY'S WATCHING." (moved here from P27) |
| P27 · REDRAW (impact, peak 1) | P27 | tall | Low at the water's surface, close, wide lens, dutch tilt 15°. | Nib launches off his planted LEFT foot (bare toes gripping the brick, water spraying back) into a low spinning cut, facing screen-left. His body is coiled in a C-curve, hips leading. His RIGHT arm sweeps the reverse-gripped RIGHT knife across his body in a flat arc at chest height, and its edge meets the throat of a leaping rat: the contact point, left of centre. His LEFT knife is held back along his left forearm, cocked for the next cut. Cloak and scarf whip round behind the spin. The struck rat bursts into violet ash from the cut line. Two more rats leap in behind as blurred dark silhouettes. | A curved motion smear along the RIGHT blade's arc. A radial impact burst at the contact point. Background dropped to curved speed lines following the spin. Water spray. | SHRAKK, impact L, top-right, angled along the arc, clear of his head and both knives. | – |
| P27b · NEW (impact) | – | inset-r | High (45°) over Nib's right shoulder, telephoto, close. | The follow-through. Nib has spun on round and sunk his weight onto his bent RIGHT leg. His LEFT reverse-gripped knife punches straight down into the glowing spine-crack of a rat landing at his feet: the contact point. Violet ash jets up past his face. | Short, thick impact radials at the crack. The ash jet. Flat dark background. | SHK, impact S, beside the jet. | – |
| P28 · REDRAW (impact) | P28 | wide | Eye level (1 m), three-quarter, medium-wide: Nib about 40% of the panel height. | The whirl. Nib is mid-spin on the junction floor, cloak flared flat into a disc, both arms out in one horizontal line, both blades extended. Around his arc, a ring of rats bursts into violet ash one after another, the nearest bursts largest. The rest of the party is not in frame. No afterimages (they risk reading as extra limbs). | One curved amber motion streak along the arc. Ash bursts. Spray. Background reduced to dark curved speed streaks. | POF POF POF, comic M, three small words along the outer edge of the arc. | – |
| P29 · KEEP | P29 | wide | as drawn | as drawn (contact shown) | as drawn | CHOMP (as now, below the bite) | – |
| P30a · NEW (impact) | P30 (the kick) | inset-l | Low, side-on, close, wide lens. | Jaeha kicks the rat off the spearman's leg. His RIGHT boot drives into the rat's ribs (contact at the toe) and the rat folds round it. His LEFT foot is planted ankle-deep. His body leans back for balance, both arms flung out, the notebook clamped under his LEFT arm: clumsy, but it works. | Impact burst at the toe. Speed lines along the kick. Spray. | THWAK, impact M, above the rat's flight path, off the boot. | – |
| P30 · REDRAW (talk) | P30 (the heal) | wide | High three-quarter over Yerin's right shoulder. | Two figures only. Yerin kneels in the water beside the spearman, both palms pressed flat over the bite on his calf, glowing mint; jaw set, eyes steady. The spearman is propped on his elbows, staring at her hands. | Mint glow. Drifting violet ash. Simplified background. | SHIIING, quiet S, beside her hands, not across her. | Yerin: "HOLD STILL. I'VE GOT YOU. YOU'RE NOT DYING IN A SEWER." |
| P31 · KEEP | P31 | inset-l | as drawn | as drawn | as drawn | – | Bomi: "THERE'S NOTHING DOWN HERE! I'M BRINGING IT BACK!" |
| P32 · KEEP | P32 | inset-r | as drawn | as drawn | as drawn | – | Jaeha: "GO DEEPER! IT'S HIDING! BIG ONES ALWAYS HIDE!" |
| P33 · REDRAW (plan) | P33 | wide | Over Jaeha's right shoulder (cropped, right foreground), eye level. | The SAME five-way junction as P19, not a straight corridor. The two tunnel mouths are at screen-left, each with a cyan arrow pouring out; the arrows meet at a cyan circle on the floor. A short dashed cyan path runs from Nib (small, crouched, centre) to the circle. Jaeha's RIGHT index finger taps the closed notebook. | Scene desaturated; clean cyan lines, no text. | none | Jaeha (inner): "THE NEXT WAVE COMES FROM BOTH LEFT TUNNELS. CUT THEM OFF WHERE THEY MEET." |
| P34a · NEW (anticipation) | – | inset-r | Worm's-eye from the water, looking up, wide lens. | Nib is airborne over the circle, dropping toward screen-left: knees tucked to his chest, both reverse-gripped knives cocked back over his shoulders, cloak spread above him like wings. The two rat streams pour in under him from the left edge. | Downward speed lines. Muted background. Amber outline. | none | – |
| P34 · REDRAW (impact, peak 2) | P34 | tall | Low in the water just behind the lead rat of the near stream, so Nib faces us. Wide lens, dutch tilt 12°. | Nib lands in a deep lunge between the two streams: LEFT foot planted forward in a splash, RIGHT leg extended back. The edge of his RIGHT knife passes through the neck of the near stream's lead rat in the immediate foreground; the blade is foreshortened toward the camera and the ash bursts at us (the contact point, lower left). His LEFT arm is swept back, the other knife just through the lead rat of the far stream. The rest of both streams pile into each other, blurred. Far right, in a side-tunnel mouth: the drone's small red light (the plant). | Radial burst at the near contact point. Speed lines along the slash. Background speed streaks. Spray. | SHRRAKK, impact L, top-left corner, along the slash, clear of Nib. | – |
| P35 · KEEP | P35 | inset-l | as drawn | as drawn | as drawn | – | (silent) |
| P36 · KEEP | P36 | wide | as drawn | as drawn | as drawn | – | Window [FIELD FORM ENDED · 01:12 USED · COOLDOWN 01:00] (kept). |
| P37 · KEEP | P37 | wide | as drawn | as drawn | as drawn | – | Bomi: "THERE WAS NOTHING DOWN THERE! WAIT. WHERE DID ALL THE RATS GO?" |

### 6C. Swarm mother (P38–P42): 4/10

With Nib on cooldown, Jaeha has the client leader kill the swarm mother using the dart trap and his corrected grip.

**What's wrong**
- **P38 inverts the monster-reveal recipe.** Jaeha's back fills more than half the panel, and the mother stands small in the lower right instead of squeezing out of a tunnel. She reads as a large dog, not a hip-high, 1.4 m boss.
- **P39 doesn't show the trap.** Jaeha points at the floor in general, so the trap brick can't be told apart from the others, and the mother stands still behind them instead of charging.
- **P40 carries four beats in one panel:** paw on brick, darts, rearing, thrust and burst. The raw art does draw the sword in the neck and three darts in the flank, but "SHK SHHUNK" (XL, at [0.30, 0.30] and [0.62, 0.40]) covers the hands, the blade and both contact points. The payoff of Jaeha's plan is invisible.
- **P41: the windows bury the beat.** Two windows overlap, the first one's text is cut, and together they cover every face, including the leader, whose beat is staring at his own sword.

**Storyboard: 5 panels → 7.** Screen direction: the leader and Jaeha on screen-left, the mother and the dart wall on screen-right.

| new | replaces | shape | camera | action | effects in the art | SFX | dialogue kept |
|---|---|---|---|---|---|---|---|
| P38 · REDRAW (monster-reveal) | P38 | tall | At the water's surface, 2 m in front of the widest tunnel mouth, low, wide lens. | The swarm mother squeezes out of the tunnel toward the camera and FILLS the frame: head low and foreshortened, yellow incisors bared, the ridge of bony spurs scraping sparks and brick dust off the top of the arch, violet ash pouring from the cracks down her spine. For scale: Jaeha's legs from the knee down and his RIGHT hand at hip height in the bottom-left foreground, cropped. Her back is level with his hip. | Dark; the violet ash is the only colour. No speed lines. | HSSSSSK, impact M, in the tunnel's dark top-left, clear of her head. | – |
| P39 · REDRAW (talk) | P39 | wide | Over the leader's left shoulder (cropped, left foreground), eye level. | Jaeha's LEFT hand is on the leader's shoulder. His RIGHT index finger points at one floor brick sunk a finger's width lower than the rest, ripples ringing it. The three dart holes are in the wall at screen-right beside it. The mother charges in the background at screen-right, blurred. | Simplified background; the brick and the holes kept sharp. | none | Jaeha: "SIR, WHEN IT STEPS ON THAT BRICK, THE DARTS FIRE. HIT IT RIGHT AFTER." |
| P40a · NEW (insert) | P40, beat 1 | strip | Extreme close-up at the water's surface, side-on. | The mother's clawed forepaw slaps down onto the sunken brick; the brick drops; a ring of ripples. | none | CLICK, quiet M, above the paw. | – |
| P40b · NEW (impact) | P40, beat 2 | wide | Low, side-on, from the leader's side of the tunnel (the same side as P39). | A volley of iron darts streaks out of the wall holes at screen-right into the mother's flank: three darts sink in with puffs of violet ash (the contact points). She rears onto her hind legs facing screen-left, mouth wide, the pale underside of her neck exposed. | Speed lines along the darts. Small impact radials at each hit. Muted background. | SHK SHK, impact M, at the top, angled along the darts, ahead of them. | – |
| P40 · REDRAW (impact, peak 3) | P40, beat 3 | tall | Low three-quarter from behind the leader's RIGHT hip, wide lens. | The leader lunges screen-right. His body is one straight diagonal from his planted RIGHT (back) foot through his hips and shoulders to the sword point. Both hands are on the grip, RIGHT above LEFT, thumbs along it: the corrected grip. The blade drives into the exposed throat of the rearing mother (the contact point, upper right of centre). Violet ash sprays back past his face. | White flash background. Radial burst at the contact point. Speed lines along the thrust. | SHHUNK, impact L, top-left behind his head, along the thrust line. Blade, hands and contact left clear. | – |
| P41 · REDRAW (system) | P41 | tall | Eye level, medium. | The leader stands in the lower third holding the sword upright before his face with both hands (correct grip), mouth open, staring at it. Violet ash drifts off the blade where the mother was. The others are small and soft behind him. | Cyan window light from above. The upper 60% is empty dark vault. | none | Both windows kept, STACKED one above the other in the upper 60% (they overlap side by side now). |
| P42 · KEEP | P42 | tall | as drawn (the best run in the chapter) | as drawn | as drawn | SPLSH ×3 (as now) | – |

---

## 3. Chapter 7

### 7A. Grain-trap ambush (P33–P56): 6.5/10

Jaeha fakes his death under a grain trap. When two Black Hound saboteurs come back to check, he buries them with a second chute and talks down a crossbow.

This is the clearest sequence in these five chapters: every beat gets its own panel, and P44 (straight down from chute B) and P36 (the decoy vest) are excellent.

**What's wrong**
- **P35, P47, P48: the grain is the wrong scale.** It is drawn coin-sized in P35. In P47 the foreground kernels are the size of a man's hand, and in P48 about as long as a forearm. The grain reads as treasure or almonds, and the buried men look as if they are in a ball pit.
- **P42: the lettering hides a good stab.** The raw art is good (fists on the grip, the blade through the white T patch), but SHUNK at XL is lettered over the hands, the grip and the upper blade.
- **P43:** FLINCH is lettered on Yerin's hands over her mouth, which is the acting.
- **P46:** the trigger beat is a static close-up with interlocking hands (Nib's hands over Jaeha's on the handle), and no weight.
- **P47 shows the result, not the impact.** Both men are already chest-deep and the torrent falls between them. The panel isn't tilted.

**Storyboard: 24 panels → 25.**

| new | replaces | shape | camera | action | effects in the art | SFX | dialogue kept |
|---|---|---|---|---|---|---|---|
| P33 · KEEP | P33 | wide | as drawn | as drawn | as drawn | SHRUG (as now) | Yerin: "WHY ARE YOU TAKING OFF YOUR VEST?" / Jaeha: "BECAUSE I'M LEAVING THEM A BODY." |
| P34 · KEEP | P34 | inset-r | as drawn | as drawn | as drawn | SHOVE, CLICK (as now) | – |
| P35 · REDRAW (splash) | P35 | tall | Low from the edge of the chamber floor, dutch tilt 10°, wide lens. | The ceiling chute's iron hatch bangs open and a column of grain as wide as a car thunders down onto the hidden plate, and the mound swells. Draw the grain at true scale: kernels the size of rice grains, so the column reads as one solid golden torrent with a sand-fine texture, and the dust as a rolling golden cloud. High on the wall stair at the top right, small: Jaeha with one arm over his face and the vest bundled under the other, Yerin cowering, Nib crouched with his scarf whipping. | A dust cloud swallowing the shafts of amber light. | KRRRRRSSHHHHHH, impact L, running vertically down the left edge of the column, not across it. | – |
| P36 · KEEP | P36 | wide | as drawn | as drawn | as drawn | – | (silent) |
| P37 · KEEP | P37 | wide | as drawn | as drawn | as drawn | – | Yerin: "THIS IS THE CREEPIEST THING I'VE EVER SEEN YOU DO." / Jaeha: "WAIT. THEY'LL COME BACK WITHIN THE HOUR." |
| P38 · KEEP | P38 | inset-l | as drawn | as drawn | as drawn | TWITCH | – |
| P39 · KEEP | P39 | wide | as drawn | as drawn | as drawn | CRUNCH CRUNCH | – |
| P40 · KEEP | P40 | wide | as drawn | as drawn | as drawn | KRAK | Trapper: "LOOK AT THAT. THE TRAP RAT FOUND HIS LAST TRAP." / Shield-bearer: "THE BOSS SAID TO MAKE SURE. AND TO BRING BACK HIS PHONE." |
| P41 · KEEP | P41 | inset-r | as drawn | as drawn | as drawn | FLICK | – |
| P42 · REDRAW (impact). If not redrawn, at minimum re-letter the existing art the same way. | P42 | wide | Worm's-eye from the grain beside the vest, wide lens. | The shield-bearer drives his short broad sword straight down through the white T patch toward the camera. The point is foreshortened, punching through the fabric into the grain (the contact point, lower centre), and grain explodes up round it. Above it, both his fists are stacked on the grip (RIGHT above LEFT), arms locked, his weight dropped onto his bent front (LEFT) knee, teeth bared, his face looming at the top. | Dark red flash with radial lines from the blade. Grain spray. | SHUNK, impact L, in the empty red upper-left, angled down along the thrust. Nothing over the hands, the grip or the blade. | Jaeha (inner): "IF I'D WALKED IN HERE FIRST, THAT WOULD HAVE BEEN ME." |
| P43 · KEEP, re-letter | P43 | wide | as drawn | as drawn | as drawn | Move FLINCH (quiet S) onto the stone wall beside her shoulder, off her hands and mouth. | (silent) |
| P44 · KEEP | P44 | wide | as drawn | as drawn | as drawn | SHFF SHFF | – |
| P45 · KEEP | P45 | strip | as drawn | as drawn | as drawn | SNAP | – |
| P46 · REDRAW (insert) | P46 | inset-r | Low, side-on, medium close on the wall stair. | The trigger, with weight. Jaeha hangs his whole weight from the lever's handle with both hands, knees bent, boots braced on the step. Nib squats on the stone rail above him and stamps the handle down with his bare RIGHT foot beside Jaeha's hands: no interlocking fingers. The lever arm swings past 45°. | A motion arc on the lever. Deep shadow with an amber edge light. | KLUNK, quiet M, at the lever's pivot. | – |
| P47 · REDRAW (impact) | P47 | tall | Straight down from the mouth of chute B, the SAME framing as P44 (the square stone rim on all four edges): a deliberate before/after. The whole frame tilted 12°. | The torrent rushes past the camera, down into the frame, and hits the two kneeling men mid-dig. The trapper's head snaps up, both arms fly up and the cigarette flies out of his mouth. The shield-bearer is slammed flat onto his chest. The torches spin away. Kernels at true scale: a sand-fine rush. | Speed lines converging from the frame edges onto the men. Golden dust. | KRRRSSSHHH, impact L, down the left edge, clear of the men. | – |
| P47b · NEW (insert) | P47 (the script's "the sword swallowed") | strip | Extreme close-up at the grain's surface, side-on. | The short broad sword, left standing upright in the mound, is swallowed by the rising grain, the hilt sinking last. | Grain streaming past. | SHFF, quiet S. | – (the threat is disarmed on the page) |
| P48 · REDRAW (scale only) | P48 | wide | as drawn | As drawn (both men buried to the armpits, coughing, faces grey with dust), but with rice-sized kernels, so the surface reads as fine golden sand. | as drawn | Move KOFF KOFF (quiet S) beside the trapper's mouth, off his chest. | Shield-bearer: "I CAN'T MOVE MY ARMS! I CAN'T MOVE ANYTHING!" |
| P49 · KEEP | P49 | tall | as drawn | as drawn | as drawn | – | Jaeha: "GOOD AFTERNOON, GENTLEMEN. WHO SETS A TRAP FOR A TRAP-TESTER?" |
| P50 · REDRAW (anticipation) | P50 | wide | Jaeha's point of view: high, looking straight down past the stone rail, telephoto. | The trapper's freed RIGHT arm thrusts the loaded hand crossbow straight up at the camera. The bolt's tip is foreshortened and in focus at the centre. Behind it, his snarling dusty face and goatee; the rest of him is sunk in the grain. | Focus lines converging on the bolt tip. The grain softened. | KLIK, quiet S, beside the trigger. | Trapper: "I'LL PUT A BOLT THROUGH YOUR EYE, RAT." |
| P51 · KEEP | P51 | inset-l | as drawn | as drawn | as drawn | – | Jaeha: "SIR, IF YOU FIRE THAT, THE THIRD SILO COMES DOWN. IT'S RIGHT ABOVE YOUR HEAD." |
| P52 · KEEP | P52 | wide | as drawn | as drawn | as drawn | TRICKLE | (silent) |
| P53 · KEEP | P53 | inset-r | as drawn | as drawn | as drawn | PLOP | (silent) |
| P54 · KEEP | P54 | wide | as drawn | as drawn | as drawn | – | Jaeha: "NOW. WHO SENT YOU, AND WHY DID HE WANT MY PHONE?" / Shield-bearer: "...THE BOSS SAID YOU RECORDED HIM." |
| P55 · KEEP | P55 | wide | as drawn | as drawn | as drawn | – | Jaeha (phone): "SIR? TWO HUNTERS ARE STUCK IN A SILO IN GATE 2231. YOU'LL NEED SHOVELS." |
| P56 · KEEP | P56 | wide | as drawn | as drawn | as drawn | – | Yerin: "WAS THAT TRUE? ABOUT THE THIRD SILO?" / Jaeha: "I HAVE NO IDEA." |

---

## 4. Chapter 8

### 8A. Rooftop chase (P01–P11): 7/10 (action, not a fight)

During LINK range training, a street cat chases Nib across the rooftops, and the link yanks him back at 160 m until LINK levels up.

**What's wrong**
- **What works:** P02 (the cat's pounce from Nib's point of view) and P03 (the leap against the orange sky) are strong, and P07's yank reads.
- **P03:** HUP is lettered on Nib's hips and cloak.
- **P07:** the strain window sits on the gag beat.
- **P10:** Nib and the cat are specks, but showing the 600 m reach is the point of that panel.

| new | replaces | shape | camera | action | effects | SFX | dialogue kept |
|---|---|---|---|---|---|---|---|
| P01 · KEEP | P01 | full | as drawn | as drawn | as drawn | TAP ×4 | Tag: "MANGWON-DONG. THURSDAY, 6 PM." |
| P02 · KEEP | P02 | wide | as drawn | as drawn | as drawn | MRRROWW | – |
| P03 · KEEP, re-letter | P03 | wide | as drawn | as drawn | as drawn | Move HUP (impact M) into the orange sky between the cat and Nib, off his legs and cloak. | – |
| P04 · KEEP | P04 | wide | as drawn | as drawn | as drawn | – | Jaeha: "SEOA. WHY IS A CAT CHASING MY SUMMON?" / Seoa: "THAT'S GOMI. SHE OWNS THE NEIGHBOURHOOD." |
| P05 · KEEP | P05 | inset-r | as drawn | as drawn | as drawn | – | Seoa: "IF YOU'RE GOING TO KEEP DOING THIS, I'M KEEPING THE NUMBERS." |
| P06 · KEEP, add the window | P06 | inset-l | as drawn | as drawn | as drawn | SNIFF | Window [LINK · RANGE LIMIT 160 M · STRAIN 90%] moved here from P07, at the top of the inset: it explains the nosebleed. |
| P07 · KEEP, window removed | P07 | wide | as drawn | as drawn | as drawn | YANK | – |
| P08 · KEEP | P08 | wide | as drawn | as drawn | as drawn | – | Seoa: "THAT'S TWO NOSEBLEEDS. YOU SAID WE'D STOP AT TWO." / Jaeha: "ONE MORE PUSH. THE CAT IS GAINING ON HIM." |
| P09 · KEEP | P09 | wide | as drawn | as drawn | as drawn | – | Window [LINK LV. 2 → 3] (kept). |
| P10 · KEEP | P10 | tall | as drawn | as drawn | as drawn | TAP ×5 | – |
| P11 · KEEP | P11 | strip | as drawn | as drawn | as drawn | THUD | – |

### 8B. Drowned hound (P27–P49): 5.5/10

Jaeha baits the blind hound up the ramp out of the water. It bites him and drags him back. Nib drops from a pipe onto its head, Bomi's stray arrow sets off a car alarm, and Nib kills the hound when it turns its head toward the noise.

**What's wrong**
- **What works:** the set-up (P27–P36), the reveal (P36), Nib's drop with the contact drawn (P43), and the arrow → alarm → head-turn chain (P45–P47).
- **P37, the hound's size:** it reads as a big dog, its head level with Jaeha's shoulder. The design has its shoulder at a man's eye level and its head a head taller than him, and in P40 and P43 it towers over him.
- **P37, the lettering:** SPLASH SPLASH is lettered over Jaeha's feet.
- **P38, the lettering:** the raw art draws the jaws clamped on his LEFT forearm, but CHOMP (XL at [0.52, 0.30]) covers the jaws and the arm.
- **P38, the staging:** the screen direction flips. In P37 the hound is on the left chasing him right; in P38 Jaeha is on the left and the hound on the right. Jaeha reclines on one hand, so he isn't "yanked off his feet".
- **P40:** the bite shows and the scale is right, but SKRRRRK covers his body, and the hound stands square instead of backing toward the water, so the drag doesn't read.
- **P43** is the best panel of the fight (knives in the brow crack, a violet burst, the jaw springing open), but SHRAKK covers Nib's arms.
- **P44:** a medium-wide side shot with a detailed background, and SKREEEK across the hound's chest.
- **P47:** the raw art shows Nib kneeling with both knives raised, but "WEE-OO WEE-OO" is lettered over him, so the wind-up of the kill is invisible.
- **P48, the kill and the chapter's peak, is the weakest key beat:**
  - Nib squats on the back of the neck holding the knives like ski poles, with no drive in his body.
  - The brow crack isn't visible.
  - The contact is a small spark, and SHHUNK (XL at [0.30, 0.30]) covers it.
  - It reads as "Nib riding a monster in a waterfall".
- **No Jaeha beat between the alarm and the kill.**

**Storyboard: 23 panels → 26.** Geography for the whole fight:
- The water is screen-LEFT; the dry ramp, the upper level and the car are screen-right.
- Jaeha flees left to right.
- The drag back to the water runs right to left: the momentum turns, and that is the one deliberate flip.
- The alarm and the kill face screen-right.

| new | replaces | shape | camera | action | effects in the art | SFX | dialogue kept |
|---|---|---|---|---|---|---|---|
| P27 · KEEP | P27 | wide | as drawn | as drawn | as drawn | BLUB... BLUB..., BUMP | (silent) |
| P28 · KEEP | P28 | wide | as drawn | as drawn | as drawn | – | Nib: "I CAN'T FIGHT IN THAT. IT'S OVER MY HEAD." / Jaeha: "THEN WE DON'T FIGHT IN THE WATER." |
| P29 · KEEP | P29 | inset-r | as drawn | as drawn | as drawn | SNAP | (silent) |
| P30 · KEEP | P30 | wide | as drawn | as drawn | as drawn | PLOP, WHOOSH | (silent) |
| P31 · KEEP | P31 | wide | as drawn | as drawn | as drawn | – | Note: "BLIND. IT HUNTS BY RIPPLES. FAST IN WATER, CLUMSY OUT OF IT." |
| P32 · REDRAW (plan) | P32 | wide | High over the ramp from the ceiling, the ramp running from the water at the left to the dry top at the right. | Clean cyan lines, no text: a cyan dot at the water's edge (Jaeha); a cyan arrow running up the ramp to screen-right into a cyan circle on the dry concrete directly under the thick ceiling pipe; a small cyan chevron on the pipe above the circle (Nib). Yerin and Bomi small at the top right. | Desaturated scene, cyan lines. | none | Jaeha (inner): "I SPLASH, IT COMES, AND I LEAD IT UP THE RAMP, OUT OF THE WATER." |
| P33 · KEEP | P33 | wide | as drawn | as drawn | as drawn | – | Yerin: "YOU'RE THE BAIT? AGAIN?" / Jaeha: "I'M A TRAP-TESTER. BAIT IS WHAT I'M BEST AT." |
| P34 · KEEP | P34 | inset-l | as drawn | as drawn | as drawn | CLANK | (silent) |
| P35 · KEEP | P35 | wide | as drawn | as drawn | as drawn | SPLAP SPLAP | – |
| P36 · KEEP, re-letter | P36 | tall | as drawn | as drawn | as drawn | Move KRAASSHHH (impact L) into the dark ceiling at top-left, off the hound's chest. | – |
| P37 · REDRAW (impact) | P37 | wide | Low at the ramp's surface, side-on, wide lens. | Jaeha sprints screen-right up the wet lower ramp, his body pitched forward in a long diagonal: RIGHT foot planted and slipping (spray off the heel), LEFT knee driving up, arms pumping, head twisted back over his LEFT shoulder at the hound, eyes wide. The hound bounds after him from screen-left at full stretch, its shoulder ABOVE Jaeha's head (1.7 m), forelegs reaching, jaws open. | Horizontal speed lines left to right. Spray off the paws. The lamps streaked. | SPLASH SPLASH, quiet M, along the bottom edge under the hound's paws, off his feet. | – |
| P38a · NEW (anticipation) | – | inset-r | Extreme close-up at Jaeha's eye level, wide lens, very close. | Jaeha's LEFT forearm is thrown up across the foreground to shield his face (gloved fist, hoodie sleeve). Beyond it, the hound's long jaw opens AT the camera: crooked yellow teeth foreshortened and filling the frame, pale clouded eyes above. | Focus lines converging on the throat. Flat black background. | none | (silent) |
| P38 · REDRAW (impact) | P38 | wide | Low, side-on, dutch tilt 15°. | The jaws clamp on Jaeha's LEFT forearm, teeth sunk into the hoodie sleeve (the contact point, centre), as the hound wrenches its head toward screen-left. Jaeha is yanked off his feet: body near-horizontal in the air, both boots off the concrete, RIGHT hand clawing at the ramp below, face twisted. | Red flash. Radial lines from the bite. A short spray of dark droplets as a silhouette; no wound. | CHOMP, impact L, top-right corner along the wrench, clear of the jaws and the arm. | – |
| P39 · KEEP | P39 | inset-r | as drawn | as drawn | as drawn | – | Yerin: "JAEHA!" |
| P40 · REDRAW (impact) | P40 | wide | Low at the ramp's surface, side-on, wide lens. | The momentum turns. The hound backs down the wet ramp toward the black water at screen-LEFT: haunches low, forelegs braced, head down, jaws clamped on Jaeha's LEFT forearm. Jaeha is dragged on his back toward the left, heels scraping, his RIGHT hand clawing at the concrete with splayed fingers, teeth gritted. A wet scrape trail runs back to screen-right. | Speed lines right to left. The scrape trail. Spray. | SKRRRRK, impact M, along the scrape trail behind his heels, off his body. | – |
| P41 · KEEP | P41 | strip | as drawn | as drawn | as drawn | – | Jaeha (intense): "NIB. NOW." |
| P42 · KEEP | P42 | wide | as drawn | as drawn | as drawn | SHING | Window [NIB · FIELD FORM 05:00 · LINKED] (kept). |
| P43a · NEW (anticipation) | – | tall, narrow | From the ceiling beside the pipe, looking straight down. | Nib steps off the pipe with his back to us: both reverse-gripped knives raised overhead, body arched like a drawn bow, cloak opening. Far below and directly under him: the hound's head with its glowing violet brow crack, and Jaeha small beside the jaws. | Downward speed lines. Amber outline. | none | – |
| P43 · KEEP, re-letter | P43 | tall | as drawn (the contact is drawn) | as drawn | as drawn | Move SHRAKK (impact L) into the white flash at the upper right, off Nib's arms. | – |
| P44 · REDRAW (impact) | P44 | wide | Medium close, low, dutch tilt 15°. | The hound whips its head toward screen-left. Nib is flung out horizontally like a flag, hanging by his RIGHT hand from the knife buried in the brow crack, his LEFT arm flung out with the other knife, legs whipping sideways. Violet ash sprays from the crack. Along the bottom edge, its front paws splay and skid on the wet concrete. | Curved speed lines along the whip. Background dropped to streaks. Ash spray. | SKREEEK, impact M, along the bottom edge at the skidding claws. | – |
| P45 · KEEP | P45 | wide | as drawn | as drawn | as drawn | TWANG | Bomi: "GET AWAY FROM MY CO-STAR!" |
| P46 · KEEP | P46 | wide | as drawn | as drawn | as drawn | WEE-OO ×3 | (silent) |
| P46b · NEW (eyes) | – | strip | Extreme close-up on Jaeha's eyes. | His eyes snap toward screen-right at the sound. The orange hazard light flashes across one side of his face; sweat. At the bottom edge, the corner of a small private grin. | Orange flash on one side; flat dark. | none | – (the MC reads the opening the alarm made) |
| P47 · REDRAW | P47 | wide | Low three-quarter from the ramp in front of and to the right of the hound, close: Nib and the hound's head fill the upper two-thirds. | The blind hound swings its whole head toward screen-right, ears pricked, frozen, exposing the brow crack and the underside of its jaw. Kneeling on its skull, Nib raises both reverse-gripped knives high overhead together, the two blades side by side pointing down. In the bottom-left foreground, cropped and darker: Jaeha's shoulder and the back of his head as he sits clutching his bleeding left forearm. | Flashing orange alarm light raking in from screen-right. No speed lines: the held breath. | WEE-OO WEE-OO, alert M, at the far right edge beside the light source, never over Nib. | – |
| P48 · REDRAW (splash, chapter peak) | P48 | tall | Worm's-eye from the ramp just in front of the hound's chest, wide lens. | The hound's head is thrown back toward screen-right, its brow toward the camera. On its skull, Nib drives both knives down into the violet brow crack with his whole weight: his body a compressed vertical C (knees deep, back rounded over the blades, both fists stacked on the two hilts), cloak and scarf flying straight up. The contact point (both blades in the crack) is in the upper third, with a white-violet radial burst. The hound's body starts to burst outward from the crack into a column of violet ash and black water. | Radial burst. Speed lines along the downward drive. Background dropped to flat black-violet. | SHHUNK, impact L, upper right, clear of the blades. KSSSHHHHH, impact M, along the bottom edge in the falling water. | – |
| P49 · KEEP | P49 | wide | as drawn | as drawn | as drawn | PATTER PATTER | (silent) |

---

## 5. Chapter 9

### 9A. The bell's refusal (P25–P29): 8/10, no storyboard needed

The bell-armoured silhouette refuses the Call by striking his bell. P28 is the best-staged action panel in ch005–009, and it is the model to copy:
- a full-body line of action through the swing
- a silhouette that reads at video size
- a shockwave ring at the contact point
- the SFX in clear space

### 9B. The Hush's grip (P38–P54): 5/10

In the Call, a many-jointed Hush hand grabs Jaeha's right ankle and drags him under as the timer runs down, until he tears up the job advert and makes an honest offer.

**What's wrong**
- **P38: the threat isn't drawn.** The raw art has only ripples and a few violet motes, no "long, many-jointed shape rising" under the water. The [00:28] timer is lettered over the lower half, exactly where the shape should be.
- **P39 is the best beat, but the lettering covers it.** The black hand is round his RIGHT shin, his body is thrown off balance, with a white flash and speed lines: contact drawn. But GRAB (XL at [0.40, 0.30]) covers the grabbed leg's thigh and knee, and the scripted frost on the trouser leg isn't drawn.
- **P43: the struggle has nothing to pull against.** In the raw art Jaeha is in a wide lunge with his arms out, and no hand or arm is visible anywhere. The [00:20] timer sits over the water at his legs.
- **P51, P52, P54: the timers cover the clock.** They are lettered over his mouth (P51), his waistline (P52) and his chest line (P54). In the raw art for P52 and P54 the waterline is clear: waist-deep, then chest-deep. That waterline is the reader's only clock for "the hand drags him down", and the timer hides it.
- **The Hush is barely seen:** once in P39, and as a wrist at the bottom of P46. The ch 10 bruise plant needs its fingers drawn clearly once.
- **Keep:** P40 (glitch), P41 (the room), P42 (the cat) and P46–P48 (the honest offer).

**Storyboard: 17 panels → 18.**

| new | replaces | shape | camera | action | effects in the art | SFX | dialogue kept |
|---|---|---|---|---|---|---|---|
| P38 · REDRAW (anticipation) | P38 | wide | At the water's surface, wide lens, looking along it at Jaeha's sneakers. | Under the glassy black water, a long shadow with too many joints (like a folded arm three metres long, edged in faint violet) slides in from screen-left toward his RIGHT ankle. Rings tremble outward; violet motes rise through the surface. | Dark; violet is the only accent. | BLRRRR, quiet S, beside the rings. | Timer [00:28] moved to the top-left over the black sky (y ≤ 0.15). |
| P39 · KEEP, re-letter and touch up | P39 | wide | as drawn (contact drawn) | As drawn. Touch-up: white frost feathers racing up the trouser leg from the fingers. | as drawn | GRAB, impact L (not XL), in the white area at top-left above the hand, angled along the pull, off the leg. | – |
| P40 · KEEP | P40 | wide | as drawn | as drawn | as drawn | BZZRK | Glitch windows (kept). |
| P41 · KEEP | P41 | wide | as drawn | as drawn | as drawn | KRRRKKK | (silent) |
| P42 · KEEP | P42 | inset-l | as drawn | as drawn | as drawn | HSSSSS | (silent) |
| P43 · REDRAW (impact) | P43 | wide | Low at the water's surface, side-on, dutch tilt 12°. | The hand hauls him down. Jaeha faces screen-right, three-quarter to the camera, his body a taut diagonal leaning away from the pull: LEFT foot braced on the surface, RIGHT leg plunged knee-deep and dragged back toward screen-left. Under the clear-black surface, the long black many-jointed arm runs from his RIGHT ankle back to the left edge, violet ash smoking off it. His LEFT fist crushes the notebook, his RIGHT arm is flung out for balance, teeth gritted, his reflection breaking into rings. | Speed lines along the pull toward screen-left. Ash smoke. | SHLRRP, impact M, at the left edge along the arm. | Jaeha (inner): "IF THIS THING DRAGS ME UNDER, I DON'T THINK I COME BACK." Timer [00:20] at the top-right (y ≤ 0.12). |
| P43b · NEW (insert) | – | strip | Extreme close-up under the water at his ankle, side-on. | The long black fingers, five joints each, tighten round his RIGHT ankle over the sock. White frost blooms on the trouser hem; violet ash bleeds up through the water. | Dark; the frost white; violet. | KRRK, quiet S. | – (the finger shapes plant the ch 10 bruise) |
| P44 · KEEP, re-letter | P44 | inset-l | as drawn | as drawn | as drawn | Move RRRIP beside the torn edge. | (silent) |
| P45 · KEEP | P45 | wide | as drawn | as drawn | as drawn | – | (silent) |
| P46 · KEEP | P46 | tall | as drawn | as drawn | as drawn | – | Jaeha: "I CAN'T PAY YOU WHAT YOU'RE WORTH. AND I CAN'T PROMISE WE'LL WIN." |
| P47 · KEEP | P47 | wide | as drawn | as drawn | as drawn | – | Jaeha: "BUT I WON'T SEND YOU IN ALONE. WHATEVER HITS YOU, I'LL CARRY HALF OF IT." |
| P48 · KEEP | P48 | strip | as drawn | as drawn | as drawn | – | Jaeha: "AND EVERYONE COMES BACK. THAT'S THE ONLY RULE I HAVE." |
| P49 · KEEP | P49 | inset-r | as drawn | as drawn | as drawn | TWITCH | (silent) |
| P50 · KEEP | P50 | wide | as drawn | as drawn | as drawn | – | Window [OFFER CHANGED · 00:12] (kept). |
| P51 · KEEP, re-letter | P51 | strip | as drawn | as drawn | as drawn | – | Timer [00:10] moved to the top band; his closed eyes and pressed lips left clear. |
| P52 · KEEP, re-letter (optional touch-up) | P52 | wide | as drawn | As drawn. Optional: the black arm's shadow coiled round his legs under the surface. | as drawn | – | Timer [00:07] moved to the top centre over the sky, so the waist-deep waterline shows. |
| P53 · KEEP | P53 | inset-r | as drawn | as drawn | as drawn | SHIVER | (silent) |
| P54 · KEEP, re-letter | P54 | wide | as drawn | as drawn | as drawn | – | Timer [00:05] moved to the top-left, so the chest-deep waterline and his breath stay clear. |

---

## 6. Patterns across ch005–009

1. **The lettering hides the hits that the art drew.** These are the six panels in the section 0 table: ch006 P40, ch007 P42, ch008 P38, P47, P48 and ch009 P39.
   - The scripts place XL impact SFX on the contact point (the four `at` values in section 0).
   - Script-format chapter rule 9 ("Every action beat has an SFX") and the `impact` recipe's "large SFX space along the diagonal" push toward a big SFX on every beat.
   - This is the cheapest fix of all.
2. **Nib's strikes are poses, not motions.**
   - The strike itself is front-facing and symmetric, with the knives at arm's length (ch006 P27, P34) or a squat on the monster's head (ch008 P43, P48).
   - There is no wind-up panel and no follow-through, and no blade ever comes at the camera.
   - Nib is never closer than a full-figure shot in his own fights.
   - The humans and the monsters get the real lines of action instead (ch006 P21; ch008 P37 raw; ch009 P39). The one Nib exception is ch008 P44.
3. **Several beats are crammed into the payoff panel.** ch006 P40 (paw, darts, rear, thrust, burst), P22 (release, ceiling, brick) and P30 (heal, kick, stare). The payoff of each Jaeha plan needs its own panel.
4. **Geography shots appear in the middle of the action.** ch006 P28 (overhead, Nib about a seventh of the height) and the P19 line-up. Wide shots belong only at the start or the end.
5. **Monster and prop scale drifts.**
   - The hound is dog-sized in ch008 P37 and horse-sized in P40 and P43.
   - The swarm mother is small behind Jaeha's back in ch006 P38, with the reveal recipe inverted.
   - The grain kernels are coin- to hand-sized in ch007 P35, P47 and P48.
6. **The screen direction breaks inside an exchange.** ch008 P37 → P38 (the hound swaps sides) and ch006 P33 → P34 (a "both left tunnels" plan, rats drawn on both sides). Each fight's script should state one screen-direction rule in its header.
7. **Windows are mostly placed correctly, with three failures:**
   - ch006 P41: overlapping windows cover every face.
   - ch008 P07: a window on the gag beat.
   - ch009: the timers are lettered onto the action and the waterline.
8. **Jaeha reading the fight is strong in places and missing between Nib's beats.** Strong: ch008 P41's eyes strip and ch006 P33's plan. Missing: there is no Jaeha beat between ch008's alarm and the kill (P46b fixes this).
9. **Already working, so copy it:**
   - ch006 P20: the low reveal between the boots.
   - ch006 P29: teeth on the calf against a red flash.
   - ch007 P44 and P47: the same chute framing used as a before and after.
   - ch008 P45–P47: the arrow → alarm → head-turn chain.
   - ch009 P28: the silhouette strike with a shockwave.

## 7. Cheapest wins, and rule changes so this doesn't recur

**Re-letter only, no redraw.** Only the lettering is wrong in these 13 panels:
- ch006 P16, P20 (reduce the size), P21
- ch007 P43
- ch008 P03, P06/P07 (move the window), P36, P43
- ch009 P39, P44, P51, P52, P54

These also get better with re-lettering alone, though the full fix is the redraw above: ch006 P40 and P41 (stack the windows), ch007 P42, and ch008 P38, P47 and P48.

**Rule changes I recommend:**
1. **`MANHWA_ART_DIRECTION.md` rule 7.** Replace it with "Contact is shown; gore is not" (the wording is in section 0).
2. **`SCRIPT_FORMAT_v2.md` chapter rule 9.** Replace "Every action beat has an SFX" with: "Every impact gets ONE SFX, size L at most (XL only for the chapter's single peak), in empty space beside the contact point and angled along the motion. Small beats get a small quiet SFX or none."
3. **The `impact` recipe in the art-direction table.** Change "large SFX space along the diagonal" to "SFX space beside the contact point".
4. **A letterer rule.** No SFX or window may overlap a face, a hand, a weapon, the contact point or a waterline or depth cue the panel exists to show. Place SFX after the art is drawn, from where the contact actually is.
5. **Every fight script.** Name the screen direction in the header, and give each action panel a `contact:` field (who touches what, where).

---

**Housekeeping.**
- I made my contact sheets and raw-art comparison tiles in `/tmp/claude-0/-home-claude/74687d11-0cc0-5bfd-9d7d-ad4189ed4d7b/scratchpad/fight/ch005-009/` and deleted them, with my helper scripts; the folder is now empty. Nothing outside it was modified.
- From memory (`/areas/my-summons-go-first.md`) I used only the owner's preference for fast narration and pacing, which is why the new anticipation beats are small strips and insets.
- Nothing new about the user came up.