# How to write a narrator recap (recaps_v2/chNNN.json)

The recap is the voice-over for the YouTube long-form video: one narrator (am_michael, speed 1.2) reads one entry while the camera holds on its panel. Chapters 1 and 2 (`ch001.json`, `ch002.json`) are the approved reference; match their voice.

## Format
- A JSON list, in reading order: `[{"panel": "P01", "text": "..."}, ...]`. Straight ASCII quotes and apostrophes; escape double quotes inside text as `\"` (better: avoid double quotes inside the text).
- **One entry for every panel that has art**, in the script's order: every panel except `kind: title`, `kind: caption` and `kind: end`. Never skip back; never narrate a panel twice.
- Length: about 14 words per entry on average (800–900 words for a 60-panel chapter). Single entries run 4–35 words: a quick silent beat gets a short line; a turning point gets two sentences.
- Check every file with `python3 /home/claude/msgf-tools/validate_recap_v2.py recaps_v2/chNNN.json` (it must print `ok`, ideally with no warnings).

## Voice
- A recap-channel narrator: present tense, third person, clear, punchy, a little wry, never sarcastic about the characters' pain. It tells the story so a listener who never reads the bubbles still follows everything.
- **Paraphrase the dialogue** in indirect or free indirect speech rather than reading the bubbles out word for word ("Nib wants an order. Jaeha has never given one in his life, so he says the only rule he knows."). A short key line can be quoted after a colon, lightly ("The goblin looks up and asks, deadpan: you first?"). Big signature lines may be said in full once ("Everyone comes back.", "Your head is S-rank. Your body is garbage.").
- **System windows:** say what they mean, with the numbers that matter ("A window: Route Alignment jumps from 0 to 60 percent.", "Forty billion won, and no other option").
- **Silent panels:** narrate the action or the feeling, briefly; or let a tiny line breathe ("Nobody moves.").
- Explain stakes and rules the first time a chapter leans on them (CARRY, LINK, field form and rest form, the rim sealing timer), in one plain clause.
- Open each chapter with a short bridge from the last one when it fits ("Right where we left off: ..."), but vary it. End on the hook, so the last entry leaves the listener wanting the next chapter.
- Use the names the script uses: Jaeha, Seoa, Nib, Borro, Lyra, Yerin, Bomi, Choi, Mok, Sora (Han Sora), Moon Ahin, Director Baek, Minseok (his "hyung"), Uncle Pyo, Dami, Woo, Ho, Foreman Gu, Inspector Ryu, Auntie Geum, the Tide Warden. "Husk" stays "husk". Korean words the script uses (hyung, tteokbokki, kimbap) stay.
- Never contradict the script; never add events, names or facts that aren't in it; never spoil later chapters.
- Fan-service panels: describe an entrance or a pose with confidence and taste ("Moon Ahin makes an entrance like she owns the canyon"), never leer or describe bodies. Seoa is 15: never comment on her looks. Yerin is never described as sexy.
- Keep it speakable: short sentences, no parentheses, no lists, no stage directions, no panel numbers.
