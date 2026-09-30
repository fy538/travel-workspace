---
doc_type: archive
status: archived
owner: founder / Life design
created: 2026-09-26
archived: 2026-09-26
why_new: The September 11 snapshot predates Life boards 04b, 04c, 08, 09 and D0, and a stale export already caused one review to report 08/09 missing. This dated copy gives reviewers and implementation lanes the current Life project without depending on Downloads or a session scratchpad.
source_of_truth_for: []
supersedes: []
---

# Vesper — Life, September 26 snapshot

A dated copy of the live Claude Design project **Vesper — Life, the current
product** (`e72a2fd2-799f-4c3d-861a-d5acaac1cdaf`) after the September 26 pass.
It is a reference, not production source or release acceptance. Keep it
unchanged; capture a new dated folder when the project changes. The
[September 11 snapshot](../design-language-2026-09-11/README.md) stays as it was.

**Start at** [00 — Start here](<project/00 - Start here.dc.html>). Open choices
are gathered, each with a recommendation, on
[D0 — Decisions to rule](<project/D0 - Decisions to rule.dc.html>).
What each board is, where it came from and every pass since September 6:
[the Life manifest](../../working/claude-design-life-current-product-manifest-2026-09-06.md).

## What is here

- **Nineteen boards:** 00 · 01 · 02 · 03 · 03b · 04 · 04b · 04c · 05 · 06 · 07 ·
  08 · 09 · D0 · P1–P4 · R0.
- **Shared components as consumed (vdl-stage1 0.3):** `Ticket`, `Notice`,
  `OriginalReader`, `vdl.css`, the kernel `styles.css` under `_ds/`, and
  `vdl-consumed.json`.
- `before-shared-package/` — the fourteen pre-adoption boards kept as before
  references, with their own `support.js`.
- `fixtures/` — the composition fixtures the boards draw from. People, places,
  dates and photographs added since September 15 are recorded in the shared
  [fixture ledger](../../working/fixtures/shared-fixture-world-2026-09-07.md) §10.

## Identity

`manifest.json` records bytes and sha256 for all 46 files. Top-level boards and
components were checked against the live project listing after the September 26
push; the three subfolders are byte-identical to the September 11 snapshot. The
project thumbnail is not included.

## Limits

Boards open over HTTP (`python3 -m http.server`); `dc-import` components render
empty from `file://`. Static boards do not establish native gestures, scroll
restoration, keyboard or screen-reader order, persistence or real delivery.
Photographs are drawn stand-ins, not anyone's photos.
