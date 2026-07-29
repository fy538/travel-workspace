---
doc_type: working
status: active
owner: founder / eng
created: 2026-07-29
expires: 2026-08-28
why_new: Records the human verdict for the pre-registered Trips Phase 4 Reading swap gate.
source_of_truth_for:
  - trips-phase-4-reading-swap-verdict
---

# Trip Reading swap verdict

## Result

**REFUTE — the swap test failed.**

- Human choice: **Candidate A**
- Sealed-key personalized candidate: **Candidate B**
- Rationale: not supplied
- Confidence: not supplied
- Candidate pair: `blind.md`
- Sealed key opened only after the human choice was recorded:
  `answer-key.json`

The pre-registered rule says that if the traveller cannot identify their
Reading against a generic same-city guide, the feature fails. The choice did
not match the sealed key, so Trips Phase 4 remains gated.

## Consequence

Do not build the collapsed companion card, persistence route, or audio spine
from this generation. The next slice is composer diagnosis and a new,
independently sealed swap run. Do not overwrite this pair or verdict.
