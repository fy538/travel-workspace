---
doc_type: working
status: active
owner: founder / product / design / research
created: 2026-08-31
last_verified: 2026-08-31
expires: 2026-09-30
why_new: Execution report for the Interaction Kernel Lab handoff — records what was built in the new Claude Design project, what was verified, design-time findings, limitations, and the founder decisions still open.
promotes_to: null
supersedes: []
source_of_truth_for:
  - interaction-kernel-lab-execution-record
depends_on:
  - docs/working/claude-code-design-mcp-interaction-kernel-lab-handoff-2026-08-31.md
---

# Interaction Kernel Lab — Execution Report

## 1. Project identity

- **Title:** Vesper — Interaction Kernel Lab
- **Project ID:** `6dd8b450-9686-4814-8db9-667f0e99db2c`
- **Durable link:** <https://claude.ai/design/p/6dd8b450-9686-4814-8db9-667f0e99db2c>
- **Created:** 2026-08-31, Claude Code session (the same session that closed the
  Home/Places semantic phase and executed the six founder calls earlier that day).
- **Status declared on every page:** `EXPLORATION · INTERACTION RESEARCH · NOT
  CANON · NOT PRODUCTION`.

## 2. Files created

| File | Role |
| --- | --- |
| `README.md` | Reviewer/coding-agent handoff, read order, drive contract, boundary |
| `00 Overview.dc.html` | Purpose, fixture index with step registries, capture contract, fairness, pass ledger |
| `01 Protocol and Scorecard.dc.html` | Task scripts, fairness contract, moderator script, comprehension questions, 8 dimensions |
| `02 Interaction Kernel.dc.html` | Focus→Express→Resolve→Act→Reflect→Repair, four truth planes, boundary ladder, modality division |
| `A - Solo NYC Weekend.dc.html` | form f0–f9 · chat c0–c8 · hybrid h0–h8 (27 steps) |
| `B - Brooklyn Dinner.dc.html` | form f0–f9 · chat c0–c8 · hybrid h0–h11 (31 steps; Nora/Dana/Sam views) |
| `D - Flight Disruption.dc.html` | form f0–f7 · chat c0–c7 · hybrid h0–h10 (27 steps; repair/stop/takeover) |
| `90 Cross-Fixture Findings.dc.html` | Design-time observations per cell + F1–F9 falsification ledger (all OPEN) |
| `91 Decision Log.dc.html` | D-01–D-13 with statuses |
| `fixtures.js` | Fixed evidence/actors/authority/outcomes for A, B, D — data only |
| `lab-state.js` | Deterministic runtime: query routing, step stack, local trace, reset, error specimens |
| `lab.css` | Lab shell + specimen primitives; imports the kit |
| `_kit/board-kit.css` | **Copied** from Vesper - Home & Places (non-authoritative lab copy, provenance noted in lab.css) |
| `support.js` | Claude Design runtime (server-provided via create_support_js) |

Filename note: storage normalized the em-dashes in the handoff's fixture
filenames to hyphens (`A - Solo NYC Weekend.dc.html` etc.).

## 3. Source project — inspected, not modified

Source: **Vesper - Home & Places** (`a26e3228-ffbb-4290-970f-b8d0cf2e83fb`),
semantic phase closed 2026-08-31. Read: Overview, Handoff - Contract, Canon -
Tokens, C2 - The Occasion, Fixture F5 - Disrupted Return, `_kit/board-kit.css`,
full file listing. **No file in that project was modified, deleted, renamed, or
added.** The only cross-project operation was one `copy_files` of
`_kit/board-kit.css` into the new project. Semantic boards were cited, never
copied.

Required reading was completed per the handoff's tiers: all nine Tier A docs in
full; Tier B sections (workbook grammar + A-sections, S1/S2/S4 fixtures,
consequence-arbitration ladder + Brooklyn composite, round-3 §§2–10,
critique-response C1–C3 + §19); Tier C kernel/manifest/source-project files.

## 4. Completed flows

All nine treatments are complete and every declared transition was exercised by
scripted walkthrough in a real browser (click-through, not code review):

- **A** — hybrid canonical path + undo-delta + back-and-reforward + noop
  branches; form including the residue → manual-cleanup ending; chat including
  the clarification turn, truth-check, and undo.
- **B** — hybrid through prepared→preview→send→Dana's guest link→private
  $40→Sam's contribution→group-safe comparison→host decision→settled→withdrawal
  recompilation; form through poll/nudge/attributed-note conventional truths;
  chat through narrated state, 38-message refinding, withdrawal by language.
- **D** — hybrid three endings (safe repair h7→h10, stop h8, takeover h9); form
  through the five-surface integration walk and the timeout; chat through the
  "Do it" bundle upgrade, scoped retry, stop, and 5:40 AM refinding.

## 5. Capture-addressable states

Every state is addressable as the durable project link + `?file=<page>` opened
in the editor, or (for automation) the page served with query string:

```text
<fixture page> + ?treatment=form|chat|hybrid&step=<id>&capture=1
```

Step registries (also on 00 Overview and in each page's step nav):

- A: form `f0–f9` · chat `c0–c8` · hybrid `h0–h8`
- B: form `f0–f9` · chat `c0–c8` · hybrid `h0–h11`
- D: form `f0–f7` · chat `c0–c7` · hybrid `h0–h10`

`capture=1` renders exactly one 393-pt specimen, chrome removed, motion frozen.
Unknown `treatment`/`step`/`mode`/`w`/`text` values render an oxblood error
specimen listing the valid registry — verified (e.g. `step=zzz`).

## 6. Runtime and QA checks performed

- Console: zero errors on fixture pages under research and capture modes.
- Full-path walkthroughs of all nine treatments (85 steps total), including
  back, undo, noop-branch, and multi-ending paths.
- 393-pt and 320-pt widths verified on the densest state (D hybrid h4 bundle
  review); 135% text pass verified on the same state — no overflow, targets
  stay ≥44 pt.
- Deterministic capture verified by direct URL (A h3, B h2, D h4 screenshots).
- Trace verified: events, taps, words, backs, confirms, undos, distinct
  screens, owner changes all recorded and rendered; Reset clears exactly the
  current fixture+treatment; Copy has a selectable fallback block.
- Keyboard: every `[data-go]` target gets `tabindex=0`, `role=button`,
  Enter/Space activation, and a visible gold focus ring; an offscreen
  `aria-live` region announces step changes; `prefers-reduced-motion` honored.

## 7. Interaction-trace support and limitations

Local only (in-memory + sessionStorage per fixture+treatment); no analytics, no
network, no real personal data; counts are descriptive, no composite score.
Limitations: `sessionId` is the constant `local` (no participant identity, by
design); `type` events fire once per input; scripted chat words stand in for
free typing (D-04); wall-clock `atMs` resets per page load.

## 8. Substitutions and adaptations (with reasons)

1. **Runtime adaptations to the dc environment** (D-09/D-10/D-11): inline page
   scripts don't execute and `<template>` content is stripped, so init is
   attribute-driven and steps are hidden `div.lab-step` nodes; a load guard
   handles double evaluation of helmet scripts.
2. **Fictional-but-realistic venue names** for A (The Blue Aster · Corner
   Note), all facts `[FIXTURE]`-marked (D-05) — the safe intersection of the
   handoff's "realistic names" instruction and the no-fabricated-world-content
   rule.
3. **Branch collapsing** (D-12): non-canonical branches (Corner Note, Dana's
   "Can't", the noodle bar, "Hold off") record a trace event but do not draw a
   second graph. A participant study needs the real branches.
4. **Viewer switching in B** drawn as explicit "lab control" links (D-13).
5. **Lab QA params** `w=320` / `text=135` added to the query contract (D-06).
6. D's protected commitment is the **interview** (F5's own affected
   commitment), standing in for the handoff's "evening or next-morning
   commitment".

## 9. Provisional findings — design-time only, no participant evidence

**Strongest:** the hybrid advantage concentrates in exactly two places — state
at rest (per-owner truth and current shape never need to be asked for) and
referent cheapness (selection replaces the clarification turn).

**Most important counterevidence:** honest chat matched hybrid on nearly all
safety behavior — undo, author-owned withdrawal, scoped retry, stop, and the
"Do it"→bundle upgrade all worked by language. The shared **command layer**,
not the shared object, did most of the safety work. If participants also
refind comfortably by asking, hybrid's remaining edge narrows to glanceability
(F3), which is untested.

Honest-paradigm costs recorded without caricature: form's container-before-
value, interpretation labor ("less rushed" → 3 manual edits), context-blind
comparison, removal residue, poll/nudge social pressure, attributed-by-
construction constraints, five-surface integration and unreconciled retry;
chat's version accumulation, referent tax, truth-on-demand-only state,
scrollback refinding.

**Falsified/weakened hypotheses so far: none and none claimed** — F1–F9 all
remain OPEN; five are marked NEEDS PARTICIPANTS because they are untestable at
design time.

## 10. Unresolved founder decisions

1. **D-08:** which modality owns each interaction moment — the call the lab
   exists to inform; ruleable only after driving the flows.
2. Whether the six-phase kernel survives as drawn (board 02 is explicitly a
   hypothesis).
3. Whether to run actual moderated sessions with this browser lab (protocol on
   01 is ready) or go straight to a native harness.
4. Whether **Italy reconstruction and post-return Home** should become a second
   lab phase. Recommendation: **not yet** — A/B/D already cover the kernel's
   phases; those fixtures test composition/continuity questions the closed
   semantic canvas already answered, and would add interaction evidence only
   for re-finding at scale, which Life-root work owns.
5. Recommended native-harness scope (after founder review): one RN research
   screen implementing the **hybrid D fixture only** — selection + short
   utterance → localized revision → one bundle review → per-owner truth — with
   real latency, voice input, and device back behavior. It is the smallest
   slice that tests every kernel phase, both modality directions, and the
   execution-honesty laws at once; A and B port later if D survives contact
   with hands.

## 11. Compliance

- Source Home/Places project unchanged; no production code, schema, API, or
  canonical doc touched; the only repository write is this report.
- No analytics, network calls, real personal data, or fake loading delays.
- No serve URLs appear in any user-facing text or in this document.
- The lab is not described as validated, canonical, or native-evidenced
  anywhere; findings are labeled design-time throughout.
