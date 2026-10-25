# L8 / tower_gate

INCOMPLETE / REVIEW REQUIRED. Not approved.

`key.png`: retained interior candidate, first attempt, native 1536×1024. It shows a cracked half-collapsed floor, surviving spanning beams, open dusk facade and two small adults on intact floor. Exact geometry, tiny-figure anatomy and exterior continuity require Claude.

Missing passing file: `outside.png`. Three generated exterior attempts are preserved untouched under `_rejects/`; they repeatedly fail the twelve-storey count / seventh-floor gate, and the third gives the gate a rectangular frame. None was used as a reference. The fourth and final permitted exterior invocation returned HTTP 400 `moderation_blocked` at output stage, category `self-harm`, request ID `774a2cd9-774d-45e4-bdfe-15fde69ef210`. No PNG or output path was returned. This was a tool safety denial, not a pending generation. No retry or alternate route followed it. Full receipt: `TOOL_FAILURE.json`.

Attempts: exterior 4 invocations, 3 returned PNGs plus 1 denied invocation; interior 1 returned PNG. Location brief allows initial plus three redos. Every returned PNG is byte-identical to built-in image_gen output; no resize, conversion, re-save or retouch. Exact prompts/references/hashes are in `prompts.json`; review notes in `REVIEW.json`; layout/light in `notes.md`; design card in `card.json`.

Stop pending Claude verdict and a resolution for the denied exterior generation. No passing exterior or completed-set claim is made, and no generation is in flight.
