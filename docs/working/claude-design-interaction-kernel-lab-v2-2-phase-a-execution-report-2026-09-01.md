---
doc_type: working
status: active
phase_status: complete / Phase B (value-to-collaboration fixture) next
owner: founder / product / design / research
created: 2026-09-01
last_verified: 2026-09-01
expires: 2026-10-01
why_new: Execution report for V2.2 Phase A of the Interaction Kernel Lab — the research-instrument repairs prescribed by the zoomed-out product-philosophy review (IK-* ledger), with per-defect dispositions, replay-suite evidence, and the two ledger items found not-present in the current export.
promotes_to: null
supersedes: []
source_of_truth_for:
  - interaction-kernel-lab-v2-2-phase-a-execution-record
depends_on:
  - docs/working/interaction-kernel-lab-zoomed-out-product-philosophy-review-2026-09-01.md
  - docs/working/claude-design-interaction-kernel-lab-v2-1-execution-report-2026-09-01.md
---

# Interaction Kernel Lab V2.2 Phase A — Execution Report

## 1. Scope and identity

- **Project:** Vesper — Interaction Kernel Lab, repaired in place.
  ID `6dd8b450-9686-4814-8db9-667f0e99db2c` ·
  <https://claude.ai/design/p/6dd8b450-9686-4814-8db9-667f0e99db2c>
- **Governing document:** the 2026-09-01 zoomed-out product-philosophy
  review, §7.1 (Phase A) plus its §4 defect ledger (IK-*).
- The review's philosophical ruling — *keep the kernel, narrow its
  authority, put value return before it* — is adopted across 00/91/94/README;
  the kernel is recorded as the product's Layer 2. Phase B (the NY/Sorrento
  value-to-collaboration fixture) is scoped on 04/00 and not started.
- No production code, no new project, no analytics/network/personal data.
  V1 and the V2.0/V2.1 records preserved.

## 2. What changed

**fixtures.js (v2.2)** — per-fixture `enums` (legal values per enumerable
key), named `checkpoints` (B2: `dana_entry` · `sam_entry` · `decision_entry`
· `withdrawal_entry`; D2: `post_bundle` · `reentry`), and per-step
`requires` preconditions. `advice_active` removed (vestigial). Session key
bumped `lab3:`→`lab4:`.

**lab-state.js (v2.2)** — checkpoint entry (`&checkpoint=`, valid in every
mode; it is the moderator's mechanism); requires-guard on explicit `step=`
entry (fails visibly, names the valid checkpoints); `data-world-set` world
events (viewer:world, zero physical actions, applied on arrival or at the
participant delay-gate deadline); `data-milestone` first-hit named
timestamps; `data-answer` comprehension chips (incorrect ⇒
`result:incorrect`, state unchanged, diegetic note); AND-composed
`data-show-if*` evaluation; key + enum validation on every mutation path
(loud failure); whole-session discard on stack incoherence; scripted-
recognizer labels auto-injected in research mode; `Lab.runReplays()` — a
deterministic 17-scenario replay suite embedded in the file with state,
step, visible-text, milestone, result, and digest assertions; and a
re-attach watchdog for a **newly discovered dc-runtime landmine** (D-46):
the runtime can re-materialize the template after boot, orphaning the
rendered shell — replays initially ran against the detached tree and its
`innerText` included hidden content, which is why text assertions now use
inline-visibility-aware, whitespace-normalized extraction.

**D2 (v4)** — p3 owner callbacks are a world event and every readback row
binds state (`committed:"booked — awaiting airline confirmation"` until the
world says verified); "Put the phone away" is navigation only; p4's
overnight facts (driver confirms, meeting moves) apply at the gate deadline
— the pickup tap only observes; both refinding roads (scroll-back · ask)
now pass an **identical comprehension gate** ("What is still waiting on
you?" — the correct identification carries `truth_recovered`); the
instrument gets the same gate after its at-rest card ("Take care of what's
waiting"), so its advantage shows up as a faster, surer correct answer,
never as a skipped measurement. `data-useful` removed from re-entry steps;
D2's refinding outcome is `truth_recovered − refinding_started`.

**A2 / B2 pages: untouched** — checkpoints, requires, resolver labels, and
validation all arrive via fixtures + runtime.

**Docs** — 01 (checkpoint entry URLs; route-level authorization; milestones
and incorrect-answers in measures; experimental-unit ruling; v2.2 trace
schema) · 04 (implementation-boundary panel: dark-implemented repo seams vs
honestly-open human questions; sixth evidence class) · 94 (full IK-* Phase A
ledger appended; matrices updated) · 91 (D-43–D-46) · 00 · README.

## 3. Dispositions (ledger on board 94)

- **Fixed and verified:** IK-P0-01…07, IK-P1-02…05, IK-P2-03, IK-P2-04.
- **Addressed with an honest residual:** IK-P1-01 — the self-check is now
  scoped as a trace/state check (9 assertions) beside the replay suite
  (route/state/rendered-truth/milestones); rendered-truth parity with the
  accessibility tree remains a manual pass, not claimed automated.
- **Ruled, on 01:** IK-P1-06 — the experimental unit is the actor job (B2)
  or phase (D2); no cross-unit aggregation; no ranking from cost alone.
- **Not present in the current export (verified before "fixing"):**
  IK-P2-01 — an attribute-boundary scan of the audited
  `~/Downloads/vesper-interaction-kernel-lab/project/` export finds **zero
  duplicate `id=` attributes**; the review's examples (`send-invitation`,
  `dana-im-in`, …) are `data-target-id` values — the deliberate shared
  semantic identity its own correction prescribes. IK-P2-02 — the cited
  duplicated markup (d8 place line, c7 chrome) does not exist in the
  current files (one occurrence each); likely an earlier-revision artifact.
  Both recorded as NOT PRESENT on 94 rather than silently "fixed".

## 4. Verification evidence (all in the live served pages)

- **Replay suite: 17/17 PASS** from the committed files — A2 6 (loose-keep,
  pace persistence, corner-note + exact undo, fail-closed language,
  keep-the-second, hybrid referent), B2 6 (full typed-truth arc incl. $30
  eligibility + deref decision + advice withdrawal; all four checkpoint
  entries; language split/capture/matchState; hybrid exact undo), D2 5
  (world-on-the-clock prelude, scroll road + gate + expiry, ask road,
  instrument gate + stop, full prelude to takeover). Each scenario also
  passes the 9-assertion self-check; zero console errors.
- **Checkpoint guard:** participant `step=d9` without a checkpoint renders
  the visible IK-P0-01 error naming the valid checkpoints; unknown
  checkpoint names fail visibly.
- **World timing (participant, delay=15):** transfer/interview unchanged
  and `pendingWorld` armed while the gate is locked (an early tap is
  blocked); at the deadline the facts land as two viewer:world zero-action
  events; pickup then only navigates. Research mode applies on arrival.
- **Milestones:** `refinding_started` on t5/i5 entry; `truth_recovered`
  only on the correct gate answer and strictly after it; an incorrect
  answer records `result:incorrect`, changes no state, and shows the
  diegetic "take another look" note (participant token scans stay clean on
  the new steps).
- **AND-composed visibility:** with `constraint_active:no` +
  `constraint_amount:50` the eligibility copy stays hidden and "No private
  limits are in play" shows — the exact IK-P1-02 failure case.
- **Validation:** `applySet('bogus:x')` throws and renders the loud
  mutation error; resolver labels present in research, absent in
  participant.

## 5. Known limits of Phase A

1. The comprehension gate is one fixed four-option question; option order
   is static (correct in third position). Counterbalancing it is a
   moderator task until randomized.
2. Checkpoint content for later actor jobs is fixture-seeded by design —
   the authoring segments exercise real typed input only from their own
   entries (annotated on 94/01).
3. The replay suite runs in-browser on demand ("Run replays"); it is not CI.
4. Everything the review said about altitude stands: this instrument still
   tests Layer-2 collaboration after value exists. Contribution quality —
   the harder question — is Phase B's.

## 6. Next

Phase B per review §7.2: the NY/Sorrento generated-Composition fixture
(evidence → substantive return complete on Home → inspect / challenge /
remove-one-claim / reshape / save-exact / ignore-without-debt → exact
return + dependency-scoped invalidation), evaluated at two independent
altitudes (contribution quality vs collaboration quality, §7.3) — not as a
fourth treatment matrix.

## 7. Compliance

Repair in place; records preserved; no serve URLs in user-facing text or
this report; participant surfaces and announcements carry no research
identifiers (re-scanned on the new D2 steps); recognizers are labeled and
scripted-only for participants; no universal schema or component trees; a
keyword recognizer is nowhere presented as evidence about production AI.
