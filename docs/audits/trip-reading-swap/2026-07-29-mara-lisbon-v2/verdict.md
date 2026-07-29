---
doc_type: working
status: active
owner: founder / eng
created: 2026-07-29
expires: 2026-08-28
why_new: Records why the second Trips Phase 4 Reading swap artifact was invalidated before adjudication.
source_of_truth_for:
  - trips-phase-4-reading-swap-invalid-verdict-v2
---

# Trip Reading swap v2 invalidation

## Result

**INVALID — not shown for human adjudication.**

- The personalized candidate contained truncated section bodies:
  `Day 1 is titled` and `Day 2 is titled`.
- The defect was found by inspecting `blind.md` only.
- `answer-key.json` was not opened.
- No human choice was requested or recorded.

## Consequence

This pair is preserved as failed generator evidence and must not be used as a
swap verdict. The completeness guard was added before generating a new,
independently sealed v3 pair. Do not overwrite this directory.
