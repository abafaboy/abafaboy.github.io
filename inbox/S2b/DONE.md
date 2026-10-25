# S2b review submission: Nib seal 2/5

Status: complete candidate set for Claude review, NOT APPROVED. Do not use these images for chapter 3 or any downstream entry before Claude gives a verdict.

## Known failures and review caveats

- The full-body human scale comparisons still fail: Nib is about 0.70 of the human height in the unmasked front and about 0.67 in the turnaround, instead of 105/178 = 0.590. Please REDO or otherwise rule on these before approval. The front used one initial generation plus three redos; the turnaround used two attempts. No image was resized to repair scale.
- Bronze trim continues down the front opening in the full-body candidates. The brief expressly names the hem, armhole and hood edges; please judge that extra treatment.
- The small clasp symbols on the full-body sheets are not reliably countable; the large clasp in details_seal2.png has nine countable towers, following the approved knight sigil.

## Files

- front_seal2_nomask.png: native 1536 x 1024 PNG; unmasked front, blue cloak lining, bronze trim and clasp. Four generation attempts.
- turnaround_seal2.png: native 1536 x 1024 PNG; masked front, left three-quarter and back. Two generation attempts.
- details_seal2.png: native 1536 x 1024 PNG; clasp, hood lining, hem and armhole close-ups. One generation attempt.
- card.json: palette, locks and review state.
- prompts.json: exact prompts, original output paths/hashes, all attached approved input paths/hashes and generation history.
- SELF_CHECK.json: format checks and disclosed quality failures.
- _rejects/: four failed earlier images preserved unchanged with their reasons in prompts.json.

## Method and scope

All seven generated images used Codex's built-in image_gen.imagegen, with five original approved local PNG references on every successful call, including the Nib front/mask sheets and one acting house-style anchor. The initial seven-reference invocation failed argument validation before image generation; the runtime maximum is five paths. No third-party model was used. No rejected or retired image was used as a reference. No generated candidate was used as an approved reference.

Every delivered PNG is byte-identical to its native generator output: no resize, conversion, re-save, crop, composite or sharpening. Existing approved Nib images and canonical metadata were not changed. The metadata here is new, per-entry metadata for inbox/S2b/. No T1, S21, chapter panels or other entries were produced.

Stop here for Claude's codex/reviews/S2b.md verdict.
