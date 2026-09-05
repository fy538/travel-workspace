---
doc_type: working
status: active
phase_status: complete / awaiting founder review of board 96 and the four F journeys
owner: founder / product / design / research
created: 2026-09-04
last_verified: 2026-09-04
expires: 2026-10-04
why_new: Execution report for V2.3 of the Interaction Kernel Lab — the lightweight-arrangements portfolio (work packages A–D of the September 4 integration brief), its version/authority check, runtime delta, mechanical verification, and the deliverables it returns (journeys, grammar, removals, reuse, owner questions, labeled amendments).
promotes_to: null
supersedes: []
source_of_truth_for:
  - interaction-kernel-lab-v2-3-execution-record
depends_on:
  - docs/working/claude-design-integration-2026-09-04/03-interaction-kernel.md
  - docs/working/claude-design-integration-2026-09-04/00-handoff-index.md
  - docs/working/product-surface-contraction-investigation-2026-09-04.md
  - docs/working/claude-design-interaction-kernel-lab-v2-2-phase-b-execution-report-2026-09-01.md
---

# Interaction Kernel Lab V2.3 — Lightweight Arrangements Portfolio — Execution Report

## 1. Scope and identity

- **Project:** Vesper — Interaction Kernel Lab, extended in place.
  ID `6dd8b450-9686-4814-8db9-667f0e99db2c` ·
  <https://claude.ai/design/p/6dd8b450-9686-4814-8db9-667f0e99db2c>
- **Governing brief:** `03-interaction-kernel.md` (2026-09-04) — work
  packages A–D; deliverables = connected consumer journeys, a minimal
  interaction grammar, legacy ceremonies removed, reused components, explicit
  owner/interface questions, labeled contract amendments.
- **Coordination point:** the Components and Plan task
  (`codex://threads/01a06e71-b35c-7ca0-8307-367db90a8a6a`) owns the
  intention/Plan semantics. Its thread was not readable from this session;
  no PlanItem storage model was adopted (D-52, 96 · Q1).
- No production code, no new project, no analytics/network/personal data.

## 2. Version and authority check (done first)

The reviewed Downloads export (`~/Downloads/vesper-interaction-kernel-lab`)
self-labels **V2.1** (16 V2.1 markers, no E1, no board 95, no
`replays-e1.js`). The live Claude Design project holds **V2.2**: E1, 95,
the Phase A runtime (checkpoints · world events · milestones · replay runner
· re-attach watchdog) and the 26-scenario suite. **Baseline = the live V2.2
project.** The export is preserved untouched; nothing from it was copied over
newer work. Historical V1/V2.0 scores stay retired/suspended; no score is
revived to argue for an interaction style (D-50).

## 3. What was built

**Runtime (`lab-state.js` → V2.3, +1.3 KB):**

- `derive()` — `window.LAB_DERIVE[fixture](state)` returns a patch of derived
  keys, applied after every mutation path and at entry (init, checkpoint,
  reset, world, replay entry). Deterministic code owns every time-fit and
  dollar figure the person reads (`derive-f.js`); recognizers route and never
  produce a number (D-51).
- `when` on `data-intents` entries — AND-composed state condition (same
  grammar as `data-show-if`); entries whose condition fails are skipped, so
  one utterance resolves differently by state without a visible no-op.
- `data-bind-map` fix — keys containing `:` (e.g. `8:30`) now match as a
  `<value>:` prefix instead of splitting on the first colon (a latent bug
  that only surfaced once times became map keys).

**Fixtures (`fixtures.js` V2.3) and pages, one treatment each
(`arrangement`) — no new modality comparison (D-20):**

| Page | Work package | Steps | Replays |
| --- | --- | ---: | ---: |
| `F1 - Saturday Jazz Loose Arrangement` | A · intention without compulsory planning | 14 | 10 |
| `F2 - Ordinary Shared Evening` | B · host / thin guest / contributor (B2 cast reused) | 17 | 9 |
| `F3 - External Reservation Integrated` | C · provider link, forwarded confirmation, change, flight stress case | 18 | 6 |
| `F4 - Expense Help Without a Mini-App` | D · three expense jobs, ordinary non-Trip dinner | 8 | 9 |

Support files: `derive-f.js` (F1 time fit; F4 ledger), `replays-f.js`
(34 scenarios, self-check after every op). Board
`96 Lightweight Arrangements Portfolio` carries the deliverables; `00`,
`README`, `91` (D-50–D-56) updated.

## 4. What each journey shows (and proves mechanically)

**F1.** “Maybe jazz Saturday” returns the useful answer complete on view —
which set fits the fixed dinner with Theo (derived: dinner 90 min + 18 min
walk ⇒ 8:30 tight, leave by 8:12; 10:30 fits) — before any container exists.
“Keep that option; don’t build around it” retains an intention with no named
Plan (labeled PRODUCT PROPOSAL). The arrangement (`a1`) is one owner
projection: optional jazz · fixed dinner · the walk between. Direct set
control; “make it less rushed” → the late set, private receipt + Undo; asked
again on the unhurried version → “nothing to loosen”, digest unchanged;
“earlier dinner” reaches Theo → one preview, Not-yet leaves state, Send
applies, no Undo past Send; Let it go → no residue (no “removed”, no
tombstone), Undo exact; unrelated chat then re-entry via a card that binds
the same state; Home mentions jazz only when kept; Sunday carries no “did you
go”.

**F2.** Nora initiates in a sentence → prepared, not sent → one send. Dana’s
link (no app, no account) gives when/where/the F/cost before “I’m in”; her
promenade walk is a personal overlay Nora’s view is asserted not to contain.
Sam’s “I’ll bring dessert” is an attributed line with no task/assignee/due
state. Nora’s 7:30 → 8:00: the tap and the sentence open the same preview;
Dana’s later view is quiet feedthrough with nothing to answer (asserted: no
“respond”, “reply”, “waiting”). “Change time” is mounted on Home, on the Chat
card, and on the arrangement — one owner, exact return. The wine ask is
previewed as optional; ignored by everyone, the host sees “no one yet — fine”
and no name.

**F3.** Places option → “Reserve on their site ↗” drawn as leaving → return:
`reservation` stays `unknown`, no “Booked/Reserved”; the arrangement stays
useful with “time not confirmed”. Forwarding the confirmation is enough (T1
receipt; the record is undoable; the values the recognizer “reads” are fixed
fixture values and labeled so). Telling the others copies the reserved time
(`shared_time:@res_time`), which is what makes “Dana and Sam still have 8:00”
provable after the restaurant’s forwarded change to 8:30. Vesper explains and
adapts; it never cancels/rebooks/holds/calls; “isn’t watching this
reservation” is said. Stress case: a ticket read with “no live status”; an
airline change → a driver-message draft the person sends from Messages.

**F4.** Receipt + question → the 18% line explained ($19.22 on $106.78, in
$126.00), nothing recorded; “Keep the receipt” creates no debt. Explicit
“I paid $126 … me, Maya, and Theo” → $42.00 each, ONLY YOU SEE THIS. “Split
the dinner” without names asks who — never the group by default. “Theo only
had a drink” asks the one missing amount; a non-number fails closed;
$14.00 / $56.00 / $56.00 with the delta stated. “Maya already paid me”
records a report (no money moved) by copying her current share; corrections
compose in order (Maya paid 42, then Theo’s drink ⇒ Maya owes 14.00). “Tell
Maya and Theo” is the shared-effect boundary. Home shows one line or nothing;
Life holds the receipt inside Thursday.

## 5. Verification (all in the live served pages)

- **Replays: 34/34 F-suite PASS** (F1 10 · F2 9 · F3 6 · F4 9), self-check
  after every op. **Regression on the changed runtime: A2 6/6 · B2 6/6 ·
  D2 6/6 · E1 8/8.** Lab-wide **60/60**, zero console errors from the lab
  (the only console line is the host’s CSP `webrtc` notice).
- **Participant mode, 320 pt + 135 % text, every step of every F page
  entered via its checkpoint:** zero research tokens in visible text or
  aria-live; zero visible controls under 44 pt; zero horizontal overflow
  after the fix below.
- **Derive unit checks (node):** F1 7:30/8:30 tight (leave 8:12), 6:30/8:30
  fits, 7:30/10:30 fits; F4 equal 42.00 ×3; drink 14 → 14.00/56.00/56.00;
  paid 42 then drink → Maya owes 14.00; no ledger → blanks.
- **Static lint (python, pre-push):** every `data-go` target exists; every
  `data-set`/`when`/`show-if` key and enum value is legal; every
  `data-intents` JSON parses and every regex compiles; every replay target id,
  step, input and checkpoint exists; participant token scan of page bodies.
- Screenshots taken at phone scale and at 320/135 (F1 a1 both sizes; F2 g3;
  F3 r3; F4 j3 at 320/135) — in the session, not persisted.

## 6. Defects found by the verification and fixed before this report

1. F4 used `receipt_kept:yes|ledger:recorded` as an OR across two keys — the
   show-if grammar only ORs values; split into two elements (lint).
2. `data-bind-map` split on the first colon, so `8:30:8:30` could never
   match — runtime fix (inspection).
3. Eleven inline chips overrode the 44-pt minimum at 36 px — removed
   (D-24; the participant scan then reported zero small targets).
4. Every composer step overflowed the 320-pt phone by 9 px at 135 % (flex
   input kept its intrinsic width) — `min-width:0` on the F pages; re-scan
   clean. The same class of overflow may exist on E1/D2 composers; not
   changed here (shared `lab.css` untouched), noted for the next QA pass.
5. Six replay assertions were case-mismatched against uppercase bands or
   matched text that also appeared in an honest negative sentence (e.g.
   `notext 'rebook'` against “doesn’t rebook”) — assertions corrected, never
   the copy. One (F3 r1) reached the live run before being caught.

## 7. Deliverables returned (on board 96)

- **Where current state rests (D-53):** one owner projection, reachable from
  Home when now-relevant, Life always, and a message-light Chat card that is
  a pointer (same bound state, same mounted action; not a copy or Source).
- **Minimal interaction grammar:** selection for reference/scope/local
  choice; brief language for expressive change (the one missing consequential
  fact may be asked); one exact preview at a material effect regardless of
  modality; world moves by forwarding; leaving Vesper is a link, return sets
  nothing; re-entry is current state. Verbs: Keep · Let go · Change · Loosen
  · Tell · Forward · Correct · Undo. Undo ends at the boundary (D-56).
- **Legacy ceremonies removed** (per package, absent by construction).
- **Reused components** (lab runtime and primitives; B2 cast/place/price;
  A2 venues) and **referenced repo seams** (settlement/receipt extraction,
  reservation attestation, Invitation/Decision receipts, CompositionBriefV1)
  — referenced, not called.
- **Owner/interface questions Q1–Q9** with owners named.
- **Labeled proposed contract amendments:** PCA-1 expense command contract
  (explicit payer + parties + supported allocation; no all-members default);
  PCA-2 reservation attestation without a Trip; PCA-3 Chat
  coordination/current-state rule (shared with the Chat lane); PCA-4 no
  Undo past a send (a clarification). Plus a list of behaviors consistent
  with C&C needing no amendment.
- **Usability hypotheses H1–H8**, honestly open.

## 8. Honest limits

Everything is design-time and scripted: recognizers route, never parse;
the ledger is a lab module mirroring settlement.py’s division of labor, not
settlement.py; no participant or founder has walked F1–F4; the
retained-intention behavior is a rendered proposal, not an adopted model;
non-Trip expense ownership, attestation without a Trip, Life’s anatomy for
kept intentions, and shared-change delivery to a person without the app are
owner questions, not decisions. Nothing native or production was built; the
authorship-eval lane (D-47) still awaits the founder’s explicit go.

## 9. Compliance

Built in place on the V2.2 baseline; the V2.1 export preserved; no new
project; no analytics, network, or personal data; all facts fixture (Theo,
Maya, Dana, Sam, Nora, Corner Note, the Georgian room are fixtures); no serve
URLs in user-facing text or this report; participant surfaces diegetic and
token-scanned; recognizer routes scripted-only (D-45); no universal object
editor, permissions panel, tab, or model-authored component tree; no PlanItem
storage model adopted; no booking execution drawn; the source “Vesper - Home
& Places” project untouched.
