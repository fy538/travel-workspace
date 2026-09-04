---
doc_type: working
status: active
phase_status: complete / awaiting founder walkthrough (E1 per board 95)
owner: founder / product / design / research
created: 2026-09-01
last_verified: 2026-09-01
expires: 2026-10-01
why_new: Execution report for V2.2 Phase B — the E1 value-to-collaboration fixture from the zoomed-out review §7.2, its two-altitude protocol (board 95), the mechanically asserted continuity proofs, and its honest limits.
promotes_to: null
supersedes: []
source_of_truth_for:
  - interaction-kernel-lab-v2-2-phase-b-execution-record
depends_on:
  - docs/working/interaction-kernel-lab-zoomed-out-product-philosophy-review-2026-09-01.md
  - docs/working/claude-design-interaction-kernel-lab-v2-2-phase-a-execution-report-2026-09-01.md
---

# Interaction Kernel Lab V2.2 Phase B — Execution Report

## 1. What was built

- **`E1 - Sorrento to New York Value Fixture.dc.html`** — one experience,
  one treatment ("experience"), ten steps across four root postures:
  - **h0 HOME (Layer 1):** the cliff-as-machine composition, complete on
    view — expression-bound lead, two claim-state-derived sentences
    (soft-tuff geology · ferry-as-horizontal-half), Maya's attributed
    Positano juxtaposition, evidence footer, and ONE dismissible
    continuation (the Roosevelt Island tram, a fixture analogy admitted
    because the NY Saturday is live). Two actions only: "Read it properly"
    and "Later". The person's own cue ("Sorrento has cliffs") is
    known_to_person and never echoed as insight.
  - **d1 (no debt):** the next morning carries no mention, badge, or task
    when unsaved; a quiet pointer only when kept. `left_without_debt` is a
    recorded milestone — ignoring is a first-class ending.
  - **f1–f5 (Layer 2, optional):** inspect why (f2 provenance: cue,
    additions, admission reason, Maya's Audience grant) · challenge one
    claim at its own source (f3) and remove it locally · detach Maya's line
    without touching claims · compare in Places (f4, named spatial reason,
    exact return) · reshape in Chat (scripted recognizer — expression +
    revision change, truth untouched) · save exactly (f5, the one boundary,
    previewed once; the manifest snapshot copies live claim states into
    `saved_*`).
  - **l1/w1 (Layer 3):** Life holds admitted Sources always and the
    deliberately saved v1 with lineage; two badges are the continuity
    proofs ("removed from the live note after saving — v1 unchanged";
    "REQUIRES YOUR WORD — Maya withdrew… nothing else in it is touched").
    Maya's withdrawal is a `viewer:world` event whose invalidation is
    dependency-scoped — the A02 doctrine exercised live.
- **`replays-e1.js`** — 7 deterministic scenarios (loaded by E1's helmet,
  merging into the replay registry) encoding every §7.2 continuity proof.
- **`95 Value Fixture Protocol.dc.html`** — the two-altitude evaluation:
  8 contribution-quality questions (asked first, about the return) and
  6 collaboration-quality questions (asked after, about the handling),
  never collapsed into one score; session mechanics; honest limits.
- **fixtures.js** — E1 state (3 claims · maya_status · expression/rev ·
  saved + manifest keys · opening), enums, checkpoints (`post_save`,
  `saved_then_withdrawn`), requires. 00/README updated.

## 2. Verification

- **E1 replays: 7/7 PASS** from the committed files, zero console errors:
  value-complete-on-view + ignore-without-debt (Sunday shows nothing when
  unsaved); claim-local removal with exact-predecessor Back (digest
  equality); reshape changes expression/rev only; save freezes the manifest
  and `saved_exact`/`life_refound` milestones land; live removal after
  saving diverges from v1 without rewriting it; Maya's withdrawal clears
  only the juxtaposition and flags the kept v1; the Places comparison
  returns exactly.
- **Participant mode at 320pt + 135%:** full walk h0→f1→f3→f2→f4→f5→f6→l1 —
  no research tokens in visible text or aria-live (including no [FIXTURE]
  markers, which are research-only spans), seeds cleared, no moderator
  chips, no resolver tags, no horizontal overflow, targets adequate.
- **Regression:** A2 6/6, B2 6/6, D2 5/5 re-run after the fixtures change —
  **24/24 across the lab**, all with 9/9 self-check.

## 3. What E1 can and cannot claim

It can show, mechanically, that the three layers stay coherent around a
good contribution: value first, kernel subordinate, consequence truthful,
continuity exact, leaving free. It cannot say anything about whether a real
model can author that contribution — the composition is fixture-authored
(A04 semantics), and "model-authored composition quality" remains the open
gap on 04. Altitude-1 answers evaluate the fixture's shape of value, not
Vesper's authorship. E1 findings never enter the A2/B2/D2 falsification
ledger; no composite score exists.

## 4. Open items

1. Founder walkthrough — E1 in participant mode per board 95 ("It's
   Saturday morning. Do whatever you'd actually do."), altitude-1 questions
   before any action prompting; A2/B2/D2 per board 01.
2. Participant sessions — not run; nothing validated.
3. The E1 composer is a scripted recognizer route (D-45) — scripted-only.
4. The natural successor, when E1's shape survives your walkthrough: swap
   the fixture-authored composition for a model-authored one behind the
   same claim-state contract — that single substitution turns E1 into the
   first honest test of Layer-1 authorship, and it is exactly the
   CompositionBriefV1 admission seam the repo already holds dark.

## 5. Compliance

Built in place; no new project; all world facts fixture data (the tram is a
fixture analogy; Maya is not a real friend's data); no analytics, network,
or personal data; no serve URLs in user-facing text or this report; no
universal card or schema; participant surfaces diegetic and token-scanned.

## 6. Post-Phase-B self-review (same day, founder: "anything we can review here")

An adversarial pass over Phase A + B, each finding confirmed empirically
in the live pages before fixing. Ledger on board 94 (SR-1..5).

1. **World-step snapshots were stale (SR-1).** On D2's p3 the stack
   snapshot was taken before the owner callbacks applied: the self-check
   failed mid-flow, and Back into p4/p3 re-fired the world events
   (measured 1 → 4). Fix: `applyWorld` re-syncs the top snapshot; Back
   re-applies idempotently (measured 1 → 2, no duplicates).
2. **The replay runner masked SR-1 (SR-2)** by running the self-check only
   at scenario end. It now runs after every op. This corrects §2's "9/9
   self-check" claim above: that was true only at scenario ends.
3. **E1's "← Put it away" lied after an in-place edit (SR-3)** — it undid
   the detach/reshape instead of navigating. Now it goes Home carrying the
   edit; "Undo that" is an explicit chip gated on an `edits` counter. Two
   replay scenarios assert it (8 for E1 now).
4. **Milestone names overclaimed (SR-4):** `value_on_view` and
   `left_without_debt` recorded screen exposure, not outcomes. Renamed
   `home_unit_shown` / `next_morning_shown`; board 95 states what
   milestones can and cannot mean.
5. **D2's boundary still set the global first-useful (SR-5)**,
   contradicting 01. Removed; `firstUsefulAt` verified null on D2.

Re-verification after the fixes: **26/26 replays lab-wide** (A2 6 · B2 6 ·
D2 6 · E1 8) with the self-check after every op, zero console errors.

The lesson is the same one this project keeps re-teaching in new forms:
a suite that checks only at the end, and a label that names one action
while the runtime performs another, both pass every happy-path test.
