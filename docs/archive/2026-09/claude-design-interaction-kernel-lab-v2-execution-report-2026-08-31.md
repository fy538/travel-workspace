---
doc_type: archive
status: archived
owner: founder / product / design / research
created: 2026-08-31
last_verified: 2026-09-01
archived: 2026-09-01
why_new: Execution report for the Interaction Kernel Lab V2 controlled-comparison handoff — what was added to the existing project, what was measured, design-time findings by evidence class, limitations, and open founder decisions.
promotes_to: null
supersedes: []
source_of_truth_for:
  - interaction-kernel-lab-v2-execution-record
depends_on:
  - docs/working/claude-design-interaction-kernel-lab-v2-controlled-comparison-handoff-2026-08-31.md
  - docs/working/claude-design-interaction-kernel-lab-execution-report-2026-08-31.md
---

# Interaction Kernel Lab V2 — Execution Report

## 1. Project identity

- **Project:** Vesper — Interaction Kernel Lab (continued; no new project)
- **Project ID:** `6dd8b450-9686-4814-8db9-667f0e99db2c`
- **Durable link:** <https://claude.ai/design/p/6dd8b450-9686-4814-8db9-667f0e99db2c>
- V1 pages (`A`, `B`, `D`, `90`) preserved byte-for-byte; V1 etags recorded at
  Pass 0 and unchanged at close. The source "Vesper - Home & Places" project
  remains untouched.

## 2. Files created and updated

**Created:** `03 Experimental Model` · `04 Artifact and Composition
Compatibility Gate` · `A2 - Solo NYC Controlled Comparison` (direct d0–d10 +
d3b/d5b, language l0–l6 + l2u, hybrid h0–h9 + h4b) · `B2 - Brooklyn Dinner
Controlled Comparison` (direct d0–d11b, language c0–c9 + c4b, hybrid h0–h9 +
h1b/h4b/h7e/h9b) · `D2 - Flight Disruption State Comparison`
(transcript t0–t10 + t2b/t6s, instrument i0–i10 + i3b) · `92 V1 Review and
Corrections` · `93 V2 Findings and Falsification`.

**Updated:** `README.md` (V1/V2 phases, three modes) · `00 Overview` (phase
split, V2 index, honest pass ledger) · `01 Protocol and Scorecard` (§9 study
design, task wording, split measures) · `91 Decision Log` (D-14–D-32 appended;
D-01–D-13 preserved; D-04/D-12 marked superseded, not erased) ·
`lab-state.js` (V2 runtime) · `lab.css` (scalable type, 44-pt targets, modes).

## 3. Runtime verification (all measured in-browser, not asserted)

- **Participant mode:** rail/banner/annotations/research-only chrome absent;
  V1 pages refuse `mode=participant` with a visible error; inputs start
  empty; an empty required composer does not advance; typed text counted
  (5 words / 30 chars measured on a real typed sentence).
- **Real branches:** every declared transition walked by click across all
  eight treatments — A2 33 targets, B2 64 targets (including decline→change,
  constraint withdraw→re-add at a different amount, Edit→save→Undo→re-add,
  noodle-bar→reopen→Georgian, withdrawal→recompile), D2 both treatments ×
  three endings (safe retry / stop / takeover) + hold-off + both refinding
  roads. Zero `__noop` targets exist on V2 pages.
- **Persistence:** refresh restored step stack `d0>d1>d2`, surviving trace,
  and a monotonic session clock (D-21 verified).
- **Controlled delay:** deadline-based gate verified — locked at start,
  blocked click while locked, auto-unlock at the declared time even in a
  throttled hidden tab (D-32).
- **Trace self-check:** six assertions (totals recomputation, required
  fields, monotonic `at_ms`, owner-transition⇒consequence, physical-action
  accounting, reset isolation) — all PASS on every exercised page.
- **Copy semantics:** "Copied" only on clipboard success; failure shows
  "Select trace manually" with the selectable block.
- **Console:** zero errors on every V2 page in research, participant, and
  capture modes.

## 4. Measured accessibility results (§11)

- **Text scaling:** computed sizes at 135%: 14px→18.9px, 13px→17.55px,
  10px kicker→13.5px — the `--tscale` mechanism genuinely rescales V2
  specimen text. (V1's `body.text135` remains broken and is documented as a
  FAIL on board 92; V1 is frozen.)
- **Targets:** measured bounding boxes at 320-pt width + 135% text: all
  participant targets ≥44 pt (e.g. decision buttons 260×44/45).
- **No horizontal overflow** at 320 pt + 135% on the densest B2 state.
- **Keyboard:** V2 actions are native `<button>`/`<input>` elements; Enter
  submits composers; visible gold focus ring; offscreen `aria-live`
  announces steps; `prefers-reduced-motion` honored.
- Not exercised: assistive-technology screen-reader passes (needs a real
  AT session; noted as a limitation, not claimed).

## 5. Design-time findings (no participant evidence exists)

Recorded on `93` with evidence classes. Headline:

- **Strongest:** with intelligence, owner rendering, privacy, and boundary
  review held constant, V1's apparent hybrid lead dissolves into two narrow,
  now-isolated questions — *is a selection cheaper than a referring phrase*
  (A2/B2), and *is truth-at-rest cheaper than truth-on-request* (D2).
- **Strongest counterexample:** B2-language completes the entire social arc,
  including author-owned withdrawal, with nothing hybrid-specific. If the
  referring phrase costs no more than selection for participants, hybrid's
  Q1/Q3 case rests solely on D2's resting-state question.
- Compatibility gate: contract findings only — complete-on-view, one
  identity across roots, admission + three explicit suppression reasons,
  saved-vs-transient distinction, and causal repair (three cases
  fixture-proven via A01/A02/A03, two carried as contract). No universal
  card or UI DSL concluded.
- Falsifiers V2-1…V2-10 all OPEN; V2-3 and V2-4 are now *live* (the
  strengthened direct and language treatments are real contenders, which is
  the point of the correction).

## 6. Founder walkthrough / participant evidence

Neither has occurred. The moderated protocol (01) is ready: participant
mode + task wording + counterbalancing + blocked threshold + delay=60. The
moderator reads traces by reopening the same fixture+treatment in research
mode; the session persists across the mode switch.

## 7. Known limitations

1. **D-31 — deterministic language edges:** without a live model, any
   entered text advances the scripted semantic edge. Words/chars are counted
   honestly, but a divergent utterance gets the scripted response. This is
   the hardest ceiling on the language treatments; moderators must note
   divergences, and it is the main argument for the next harness being
   coded/native.
2. Trace `type` events fire once per input (not per keystroke);
   characters are counted at submit.
3. The B2 direct contribution guard (`data-requires-input`) checks the note
   field, not both fields.
4. Countdown display (not the unlock) can lag in a backgrounded tab;
   unlock time is exact.
5. Screen-reader (AT) pass not run; keyboard-only completion verified
   programmatically, not by hand on every treatment.
6. `04` renders A04/A06 semantics statically (with D2 as the live exercised
   instrument); it does not re-execute the fixture-lab compilers.

## 8. Weakened or falsified hypotheses

None falsified. Weakened at design time: "hybrid's advantage is broad" —
narrowed as described in §5. V1's trace-based comparisons are formally
retired (D-15).

## 9. Unresolved founder decisions

1. **D-08** — modality ownership per interaction moment (now answerable
   against a clean comparison; best made after your own walkthrough).
2. Whether to run moderated participant sessions with this browser lab, or
   treat D-31 as disqualifying and go straight to a coded harness.
3. Whether D2's resting-state question is important enough to be the native
   harness's first target (the design-time analysis says it is the decisive
   remaining question).
4. The `04` follow-on: whether the native semantic-renderer lab (seven
   contracts × three densities) becomes the next lane after the interaction
   question settles.

## 10. Ready for a coded/native harness

The pieces that survive translation as-is: the resolved-interaction command
vocabulary and its trace schema (§10 of the handoff, implemented), the
invariant boundary-review contract, the D2 single-variable design, and the
participant/research/capture mode separation. Recommendation unchanged in
spirit from V1 but sharpened: build the native harness around **D2's two
treatments first** (it is the question the browser lab can least fake —
real latency, notifications, and re-entry), with A2's selection-vs-phrase
moment second. This narrows the research instrument, not the product thesis.

## 11. Compliance

Existing project continued; V1 inspectable and labeled; no production code,
schema, API, or canonical doc changed; no analytics/network/personal data;
no serve URLs in any user-facing text or this report; participant copy
carries no fixture markers, oracles, or treatment labels; QA claims above
are measured or explicitly marked not-run.

## 12. Self-review corrections — same day, before any session

An adversarial self-review against §18 found nine defects in the build as
first reported. All were fixed and re-verified in-browser; where the original
§3–§4 claims were overstated, this section is the correction of record.

1. **Capability inequality in language treatments (serious).** A2's Undo and
   B2's withdrawal were research-only chrome — invisible to participants —
   recreating the very capability confound V2 removes (§3.1). Fixed: undo /
   "take it back" are now participant-visible suggested-reply chips on the
   same command layer; B2-hybrid gained the missing post-decision withdrawal
   (h10/h10b). Verified by click-walk.
2. **Fake transcript burden (serious).** `.lab-phone-body` used `min-height`,
   so no step could overflow internally — D2's t5 card was simply visible and
   §18 item 10 was not truly met. Fixed: V2 specimens get a fixed 700-px
   viewport; t5's transcript now overflows by ~400 px, opens at the newest
   message (`data-scroll=bottom`, re-asserted across paint frames, excluded
   from the scroll metric), with the status card off-screen above. Measured.
3. **Fake time controls (moderate).** B2-direct d0's 7:30/8:00 segment and
   B2-hybrid h1b's time sheet didn't change anything (§8.1 violation). Fixed:
   time is an honest suggested default; time-editing is elided and logged as
   a limitation rather than simulated.
4. **State misrepresentation (moderate).** A2-direct's early "Keep Saturday"
   jumped to the venue-chosen state. Fixed: it now lands on d6e, keeping the
   loose shape exactly as it existed, with Undo.
5. **Demand characteristics in participant copy (moderate).** A2's refind
   steps said "treatment" / "refinding measure" inside the specimen. Fixed:
   copy is diegetic; the measure explanation moved to annotations.
6. **93 column headers** mislabeled the D2 row — clarified.
7. **B2 per-actor start steps** for the moderator now listed in the d2/c3/h3
   annotations (01 defers to those).
8. **B2-direct d7 guard** required the note its own placeholder called
   optional — guard moved to the place field.
9. Delay-gate countdown and scroll-event flushing can lag in a *hidden*
   browser tab (test-environment artifact; unlock time and metrics are exact
   in a foreground session — the only kind a moderated session uses).

Re-verification after the fixes: all A2/B2/D2 paths re-walked green,
self-check 6/6 PASS, zero console errors, transcript overflow/bottom-start/
off-screen-card measured true.

## 13. Correction notice — 2026-09-01 (V2.1)

The founder's rendered + source audit of the build this report describes ruled
it **SEMANTIC INTEGRITY AUDIT FAILED**: routes were reachable, but rendered
results were not causally faithful to what the person supplied or chose. This
report's claims are superseded where they conflict with that ruling. In
particular:

- **§3 "Real branches … every declared transition walked"** was true of
  routes, not semantics — the audit's P0.1–P0.11 show several of those walked
  branches invented pacing, replaced a chosen venue, discarded typed
  contributions, or advertised an Undo that did not exist.
- **§5's design-time findings** (the comparison ledger, the "hybrid narrows to
  two questions" analysis, and the "language completes the arc" counterexample)
  are **suspended until re-evidenced** — their evidentiary basis (equal
  checkpoints, state fidelity) did not hold. The suspension ledger is board 94.
- **§6 "the moderated protocol is ready"** was wrong: P1.1–P1.4 (checkpoints,
  fail-open language, research identifiers in accessible announcements,
  undercounted traces) each blocked a defensible pilot.
- **§7 limitation 3** ("the B2 direct contribution guard checks the note
  field, not both fields") described a §12-era intermediate state and was
  stale even for V2.0; in V2.1 the guard sits on the required place field and
  word totals sum both fields.
- **§12's re-verification claim** ("all paths re-walked green") verified step
  reachability only; it did not assert rendered state content — the exact gap
  the audit exposed.

What still stands from this report: the runtime landmine catalog, the
mode/persistence/delay/self-check mechanics (carried into V2.1 and extended),
the accessibility measurements, and the compliance statement.

The repair record is
`docs/working/claude-design-interaction-kernel-lab-v2-1-execution-report-2026-09-01.md`,
governed by
`docs/working/claude-design-code-interaction-kernel-lab-v2-1-integrity-fix-handoff-2026-09-01.md`.
