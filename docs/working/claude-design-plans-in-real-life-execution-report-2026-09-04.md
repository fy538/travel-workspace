---
doc_type: working
status: active
phase_status: complete through the §0.4 connected-journey review / awaiting founder review
owner: founder / product / design / Components and Plan
created: 2026-09-04
last_verified: 2026-09-05
expires: 2026-10-04
why_new: Execution report for the new Claude Design project "Vesper — Plans in Real Life" — what was inspected, what was built, what was verified, what the §0.1 review revision changed, and what remains someone else's decision.
promotes_to: null
supersedes: []
source_of_truth_for:
  - plans-in-real-life-execution-record-2026-09-04
depends_on:
  - docs/working/claude-design-plans-in-real-life-handoff-2026-09-04.md
  - docs/working/claude-design-interaction-kernel-lab-v2-3-arrangements-execution-report-2026-09-04.md
  - docs/working/lightweight-arrangements-implementation-handoff-2026-09-04.md
---

# Vesper — Plans in Real Life — Execution Report

## 1. Identity

- **New project:** Vesper — Plans in Real Life · `cd2e1f82-9786-4ae6-993e-c0dfbe8d6302` ·
  <https://claude.ai/design/p/cd2e1f82-9786-4ae6-993e-c0dfbe8d6302> · created 2026-09-04 ·
  bound design system "Vesper · Production Kernel" (`fc85e38a-72e6-4b40-98a7-fb447dd94529`,
  a 2026-07-25 projection of travel-app main; primitives only). Repo tokens re-read on
  2026-09-04 at travel-app main `35c110f47` govern where the two differ.
- **Start board:** `00 Start Here` — <https://claude.ai/design/p/cd2e1f82-9786-4ae6-993e-c0dfbe8d6302?file=00+Start+Here.dc.html>
- **Reference project, untouched:** Vesper — Interaction Kernel Lab `6dd8b450-9686-4814-8db9-667f0e99db2c`,
  inspected live at **V2.3** (F1–F4, board 96, lab-state.js/fixtures.js V2.3). The Downloads export
  `~/Downloads/vesper-interaction-kernel-lab` exists and is the stale V2.1 snapshot; nothing was copied
  from it and nothing was written to the lab.
- **Native evidence:** `travel-app/.maestro/runs/20260904T232754Z-trip-itinerary/screenshots/full/`
  (`plan-day-top.png`, `plan-day-scrolled.png`; iPhone 16 Pro; main @ `47735f406`; Ready-Kyoto mock).
  Embedded downscaled (1100px JPEG) on board 01. Evidence of one build, not an acceptance verdict.
- **Repos:** travel-app on main (196 ahead of origin, clean working tree except pre-existing state);
  travel-agent on main with four pre-existing modified docs not touched by this session. **No production
  code, flag, contract, or token was changed.** Only this report and the memory files were written to disk
  outside the scratchpad.

## 2. What was built (8 boards + kit, all in the live project)

| File | What it holds |
| --- | --- |
| `00 Start Here.dc.html` | Identity, separation from the lab, the recommendation in one paragraph, board map, review-question index, limits |
| `01 Baseline - The Itinerary Today.dc.html` | The two native captures with observed strengths/issues; the first viewport **redrawn from repo tokens** as an equal-scale control; type roles baseline vs proposed; material usage; the recorded type-source conflict |
| `02 A - A Loose Saturday.dc.html` | 7 states + 1 rejected alternative (the intention forced into an itinerary skeleton) |
| `03 B - A Planned Trip, Kyoto.dc.html` | Arrival day full scroll; the loose day (09:02 provider departure beside an open afternoon and a 19:00 reservation); list↔map; inspect+move sheet; one itinerary-aware alternative; compact header naming selected day and day being read, with the italic-vs-Roman opener comparison; 320pt · 135% stress |
| `04 C - A Shared Afternoon and Dinner.dc.html` | Initiate/review/send; thin-guest link; suggestion that changes nothing; non-attending friend's 72pt photo; grant from a sentence with an inspectable who/can/can't/until receipt; Maya's allowed edit; Sam dinner-only; return catch-up + revocation |
| `05 D - The Day Changes While People Move.dc.html` | Rain alternative on an optional stop; Maya asks for eight; preview naming affected people (silence ≠ acceptance); the single reservation mismatch; external link + honest return; forwarded confirmation; stale alternative revalidated; Sam's view on the F |
| `06 E - Overlap and the Four Doors.dc.html` | Lisbon overlap (two horizons, one "elsewhere" line, no swimlanes/subgroup Occasion); Home / Chat / Places / Life doors to the same page |
| `08 Contextual Request - Resting, Active, Resolved.dc.html` | **§0.1 revision.** The one contextual-request pattern (P1 resting · P2 active · P5/P6 resolved) and the six stress cases (P3 Wednesday clarification · P4 scope question · P5 whole outing + reservation boundary · P6 loose Tuesday morning · P7 arrive-at-10 · P8 skipping while Ben goes · P9a/b owner-editor-contributor), plus dismissal, an unsupported ask (P10) and Continue-in-Chat with clean return (P11); coverage panel |
| `09 Journeys - Value, Adapt, Coordinate.dc.html` | **§0.3.** J1 orientation without a prompt (Monday departure visit with one justified “Next” line vs Sunday browse; inspect for experience; close with nothing kept) · J2 ask with context shown → free follow-up → answer-vs-memory-vs-plan → slow / failed / interrupted save → intervening change with offscreen destination → resume with recovered draft and the four resume rules · J3 exact outgoing message → identical recipient view → outcome read from the plan → authorized-editor contrast · journey-friction log |
| `07 Decisions, Mapping, Reuse.dc.html` | The eight §7 decisions answered; decision log (B-1..7 preserved, R-1..8 recommended); type/material mapping with exact tokens and proposed exceptions; reuse/contraction map; Q1–Q11 with owners; PCA position |
| `10 Interactive - Saturday, Shared.dc.html` | Scripted prototype on the C→D fixture: three viewpoints, recognizers, undo boundary, re-entry |
| `kit/plans.css`, `kit/proto.js`, `evidence/*.jpg`, `support.js` | Shared tokens (each marked `[REPO]` or `[PROPOSED]`), phone frame, board chrome; prototype runtime; captures; DC runtime |

Local source mirror (this session only): `scratchpad/pirl/` — not committed anywhere; the live project is
the artifact of record.

## 3. The recommendation (one composition family)

Every arrangement is the same editorial document: identity block (kicker · 31pt serif title · one thesis
line) → rows with a hanging 44pt mono time gutter and a 17.5pt serif title → temporal chapters only when a
day has real parts → a date rail only when there are several days. Four small changes, all proposed:

1. **Times 12/14** (proposed role `itineraryEntryTimeReadable`; baseline `itineraryEntryTime` 10.5/13). Bold for
   provider/agreed times, regular for planned, a muted caps word for loose intervals; the source of a bold
   time named in signature gold in the supporting line.
2. **Chapter opener 15/20 Roman, complete** (proposed `itineraryChapterOpener`), replacing the 13/18 italic
   clipped at two lines that the native capture renders.
3. **Stamps/kickers 11pt** (Apple 11pt minimum) and the supporting line on `bodySm` 13/17 instead of `caption` 12.
4. **Preview card** = `quietPanel` + dashed planning-ink edge, for every not-yet-real alternative; the only
   new material. Raised paper stays limited to the map's selected-place card.

People appear in three places only (header avatars · one "with …" phrase on the row where participation
differs · attributed material under a row). Change is a row moving in place plus a one-line receipt with
Undo where Undo is true. A single loose intention gets the identity block and rows and nothing else (02 A2
vs the rejected A8).

## 3b. §0.1 review revision (same day, after the founder reviewed the export)

The revised brief (§0.1, 20:50) superseded the first pass's "direct controls for every relevant property".
Live project, Downloads export (`~/Downloads/vesper-plans-in-real-life/project`) and local sources were
byte-identical before editing (no concurrent edits). Changes, all in the existing project:

- **New board 08** — the one pattern: the page rests with a floating "Change something…" pill (text/voice)
  and **no composer**; the pill or a tapped row opens the existing half-sheet with the **target carried**,
  a **private / shared kicker**, direct chips only where the choice is genuinely bounded, and the request
  field. Resolution happens in the sheet: clear + authorized + private → applies with a receipt, no preview
  (P6, P7); exploratory → an alternative returned, not applied (02 A4, 03 B5); consequential ambiguity →
  **one** question with the known implication (P3, P4); material effect → the existing preview (05 D3);
  unsupported → words kept, state untouched, "Continue in Chat" (P10); "Not now" → no mutation. Resolved =
  the clean page with one transient time-stamped receipt (P5); longer discussion → Chat with object +
  unresolved words carried, returning clean (P11). Header "CHAT" slot renamed **ASK** (private, Vesper);
  shared discussion is the visibly separate "Say something to …" door inside the sheet.
- **02 A3/A4/A5 rewritten**: the two real sets stay as chips inside the request sheet (finite, real);
  "arrive at 10 for the 10:30 show" goes through the field and resolves as arrival ≠ performance (08 P7);
  the exploratory alternative is returned inside the sheet; A5 is the clean page with a transient receipt.
  Composer and user bubbles removed from A2/A5/A7; A1/A6 (Chat root) keep theirs.
- **03 B4/B5 rewritten**: the stop sheet keeps two judgment shortcuts (11:00 still quiet; skip — Ben still
  goes) and the field; the three-move menu is gone; B5's alternative is returned in the sheet. Pills on
  B1/B2; ASK door throughout.
- **04/05/06**: composers → pill; the grant and revocation are shown as kept request lines, not bubbles;
  D2's "Maya asks" is annotated as the shared door; pills on E1/E2.
- **07**: decision 3 rewritten; R-9 (one pattern) and R-10 (direct controls are selective) added; removed-
  ceremonies list extended (persistent composer, exhaustive move menu, picker chain, ambiguous CHAT door);
  Q12 (Chat lane: thread/history ownership for in-sheet requests; voice path).
- **00**: board map, recommendation paragraph, review question and status updated.
- **10 Interactive**: composer replaced by the pill-and-field with a private/shared kicker (Maya's kicker
  changes with her grant); "Not now" closes without mutation; "Continue in Chat" is labeled not implemented;
  unsupported input keeps the words in the field; supported input closes the field. Limitation labeled in
  the research chrome: scripted recognizers with selected outcomes, not date/time understanding.

Stress-case coverage (§0.1 F): 1 → 08 P7 · 2 → P3 + P4 · 3 → P6 · 4 → P5 · 5 → P8 · 6 → P9a + P9b. Also
shown: a simple request without a preview (P6, P7), an exploratory alternative (02 A4, 03 B5), a necessary
clarification (P3, P4), dismissal without mutation (P9a, P10), an unsupported request (P10), re-entry after
success (P5, P11). Private assistance vs shared discussion: kicker + doors on every sheet (P2, P9a).

## 3c. §0.2 second export review (22:40) — assistance first, not editing first

Live project, local sources and the 21:18 export were byte-identical before editing. Changes, all in the
existing project (no new project):

1. **One recognizable assistant.** The header ASK/CHAT slot is removed from every arrangement page; the pill
   reads **"Ask Vesper"** (it names the open stop); "Continue in Chat" became **"More room in Chat"**, an
   optional expansion of the same assistant, never a capability escape. Field copy: "Ask about this, or
   change it…".
2. **Inspection is value first (B4, 08 P2).** Opening Tōdai-ji leads with recognition (labeled fixture facts),
   practical context (get in / from / with) and who is coming; no "11:00 instead" / "Skip it" chips.
   Scheduling shortcuts only after expressed intent or a real problem. A3 keeps the two real jazz-set chips
   after a one-line recognition and the derived fit facts.
3. **Read-only question (new P2b).** "Would my mother enjoy this?" answered with substance from authorized
   context only (the person's own note, labeled), no mutation, no receipt; the lunch question named as the same
   shape.
4. **Private entry stable across roles (P9a).** Dana opens the same private sheet; Vesper answers, states in
   one clause that the afternoon isn't hers to change, and offers "Send to Nora and Maya as a suggestion" /
   "Keep it to myself". The expressly shared door remains for speaking to companions from the start. P9b
   annotated accordingly.
5. **Arrival composed into the jazz row (P7, A5).** One 10:30 row carries the venue's set time in bold with its
   source and "you'll aim to arrive about 10" as a phrase; the connector carries "leave dinner by about 9:40".
   No separate "Arrive" object.
6. **Ordinary flexibility (new P6b).** In a separately labeled fixture B′ (ten-day Kyoto, Wednesday 24th free
   mid-trip), "Move Hōnen-in to Wednesday at 10" applies directly with a receipt and true Undo. The Wednesday
   departure collision (P3) and the outing-scope question (P4) remain in the eight-day fixture; the departure
   fact was not deleted.
7. **Supported value in place (P10).** "Book us a hotel in Nara" returns two labeled fixture options with
   external links, the execution boundary in one sentence, and the forward-a-confirmation path; "More room in
   Chat" optional. The annotation separates the product's booking boundary from a prototype recognizer's
   limitation. P11 reframed as chosen expansion after the sheet had already resolved the move, and labeled
   "illustrated, not demonstrated".
8. **07**: decision 3 rewritten again; R-9/R-10 updated, R-11 (private entry stable across roles) added; reuse
   map corrected (`PlanStopInspectSheet → the value-first inspection sheet`, no "hides a picker" claim, no
   "every stop opens an adjustment sheet"); removed-ceremonies list extended; Q13 (entity lane: which facts
   the sheet projects and how authorized personal context is admitted).
9. **00** updated (title line, recommendation paragraph, board map, review question, status). **04/05/06**:
   pill relabeled, ASK slot removed, D2 annotation notes the expressly shared door vs private ask.
10. **10 Interactive**: single "Ask Vesper" entry; private kicker for every role (Maya's shows her scope);
    Maya's edit-like ask without rights → private answer + explicit "Send to Nora as a suggestion" (owner then
    sees it as her words); "More room in Chat" labeled not implemented; research chrome states what is
    illustrated vs demonstrated.

Coverage requested by §0.2: value-first inspection → 03 B4, 08 P2 · read-only question → P2b · simple
successful move → P6b · stable private entry → P9a · optional explicit sharing → P9a→P9b · supported value
without Chat transfer → P10 · dismissal and clean return → P9a/P10 "Not now", P5/P6b · §0.1 stress cases
unchanged (P3, P4, P5, P6, P7, P8, P9).

## 3d. §0.3 journey-friction review (23:09) — the work between the screens

Live project, local sources and the 22:58 export were byte-identical before editing.

- **New board 09** with the three connected journeys (15 frames) and a journey-friction log that separates
  observed board/code inconsistencies from predicted friction and names what changed for each.
- **Concrete inconsistencies fixed:** P9a→P9b now carries Dana's exact words end to end (Maya's editor move
  is 3:30; Dana's suggestion is "Move the bookstore to 4 — it's dead until then", time-stamped, adopted as
  4:00 in J3c). In `kit/proto.js`, Maya's dinner ask (`maya_ask8`) is prepared privately and reaches Nora
  only through an explicit "Send to Nora as a question" tap, the same shape as the bookstore path.
- **Prototype additions:** failure injection in research chrome (slow / failed / interrupted) for the next
  private change — pending state with the plan unchanged and duplicate submit held; failed → nothing changed,
  words kept, honest retry; interrupted → "checking…", retry held, then reconciled once. The exposed `act`
  helper now takes the same commit path as a tap. The research chrome states illustrated vs tested.
- **07:** R-12 (between-the-screens rules) and Q14 (draft custody/retention and the explicit memory-write
  gesture belong to C&C). **00:** board map, status.
- **Design rules recorded on 09:** no leave-by figure without location/route evidence; the field survives
  follow-up; "Remember this about her?" is an explicit offer, never a silent write; latency is a visible state,
  not an optimistic row; unknown outcome reconciles before retry; another person's change is named with its
  consequence and the page does not jump ("See it ↓"); four resume rules (read-only → nothing kept; unsent
  draft → on-device, per plan, discardable, expiring; unadopted alternative → gone; accepted change → stays);
  the sheet expands with the keyboard, has a visible ✕, platform Back closes and never undoes, no nested
  sheets; the exact outgoing message with recipients sits beside Send.

## 3e. §0.4 connected-journey review (2026-09-05 00:04) — preserve the intention, not just the schedule

Live project, local sources and the 23:51 export were byte-identical before editing. All changes in the existing
project; no new screen family.

- **J2f reworked (purpose over chronology).** One coherent branch: the unambiguous, authorized, private addition
  applies and is read back **accurately** ("Added Isuien after Tōdai-ji · about 12:30" — no longer "around noon"
  with a substituted time). Vesper then names the changed tradeoff in the person's own terms — "Ben moved the
  temple to 11 — the busier time we were trying to avoid. Isuien still fits afterward." — without disclosing the
  mother or her preference, and offers help within the person's own scope: "Go early myself" (their participation;
  the 06/08 P8 grammar), "Say something to Ben →" (expressly shared), "Undo mine" (scoped to Isuien; Ben's edit
  stands). No reversal of Ben's edit, no outing move, no approval queue.
- **System mechanics out of customer copy.** J2b: the routine "Remember this about her?" offer removed; the
  correction is used within the exchange and not promoted; explicit "remember that" is a deliberate request via the
  same field. J2e: "Checking whether that saved" with one plain line; duplicate-prevention explained in the
  annotation. J2g: "Draft from 12 minutes ago", the words, Discard; custody/expiry moved to the annotation as a
  proposal to reconcile (not an unlimited-retention promise). J3c: the hypothetical "If Nora had left it…" moved to
  the annotation. J2c copy trimmed.
- **Prototype gaps fixed (`kit/proto.js`).** (1) The pending/unknown guard now holds only the *relevant mutation*;
  navigation, close, viewer switch, Home and reset work while a request is in flight, and returning shows the same
  in-flight request. Cancel is offered only before commit. (2) Authored words are retained: the in-flight/failed
  cards show the person's own words (`req_text`) with the execution identity (`req_id`); a route that is held does
  not clear the field or report success; "Not now" after a failure keeps the words as a draft that reappears in
  the field on reopening (with Discard); retry and unknown-outcome reconciliation refer to the original request.
- **07:** R-13 (preserve the purpose, not just the schedule; no routine memory offer); Q14 reworded. **00** updated.
- **Friction log** on 09 extended (experiential compatibility; mechanics in customer copy; prototype gaps) and the
  illustrated / simulated / mechanically-exercised split restated.

**Verification (live project, after the push).** Board 09 J2/J3 re-rendered and read at full resolution.
Prototype 10 on a fresh load, driven by taps and typed input: slow save → pending card shows "add the bookstore",
plan unchanged; ‹ Home and "Open Saturday" work while pending and return to the same pending card; a second typed
request ("let Maya help…") is held with its words left in the field and applies nothing; the first request then
lands once. Failed save → the words in the card, nothing changed; "Not now" keeps them as a draft that reappears
on reopening; Discard clears it; "Try again" re-runs the same request once. Interrupted → "Checking whether that
saved" with the words; a duplicate tap is held; reconciled once with a single receipt. Cancel before commit →
nothing changed, words kept as a draft. All visible buttons ≥44pt; no horizontal overflow; console clean.

**Illustrated only:** value-first content, read-only answers, retrieval, the drawn keyboard and expanded sheet,
purpose-aware adaptation (J2f), Chat continuation, resume across Maps/provider/background. **Simulated:** slow /
failed / interrupted saves. **Mechanically exercised:** as listed above. The in-flow assistance region in 10 does
not validate the illustrated modal sheet; native keyboard/navigation and participant behavior remain unclaimed.

## 3f. Component restyle after founder review (2026-09-05)

The founder rejected the bordered, tinted, mono-text band used for the receipt and for the “Next” orientation
line (“I don't like this component style”). Both were the E1 receipt-band lineage sitting on the editorial page
as system chrome. Kit-wide change in `kit/plans.css`, so every board updates at once:

- **Receipt** → a serif sentence in the document’s voice (16/22, medium, ink) with a 6pt gold dot as a hanging
  marker and the quiet mono time-stamp to the right; the ink variant uses inkSoft and a muted dot. No border, no
  wash, no mono block. Undo remains a quiet chip beneath.
- **Next line** → a serif sentence (15/20, inkSoft) under a hairline with a small gold “NEXT” kicker; the mono time
  stays bold inside the sentence. No box. The “FIXTURE ROUTE” tag was moved out of the customer frame into the
  annotation, where research labels belong.
- Verified by re-rendering 09 J1a/J2f and 02 A5 from the live project; a wrapped receipt now aligns its second
  line with the text (hanging indent).

## 3g. Documentation-alignment pass (2026-09-05)

After re-reading the product canon, the four-root and contribution contracts, the sixteen decision records since
August 14, and the design-kernel rulings, four concrete deviations were fixed in the project (kit-wide where the
kit owns them):

- **Door law (kernel §11.1).** Attributed source facts in supporting lines were inert gold body text. They are now
  Doors: gold text with the canonical trailing arrow and an invisible 44pt target, opening the evidence (ticket,
  confirmation, venue). "See Isuien" and other in-page jumps use the one arrow idiom.
- **Micro-type floor (kernel §11.2).** Capsule labels, time-stamps, the mic slot, map labels and fixture labels
  were 9–9.5px; all customer-facing roles are now ≥10px.
- **"Do not narrate the product" (Editorial Canon §13.3).** Sentences describing Vesper's own restraint, storage or
  monitoring were removed from customer surfaces on 02, 03, 05, 08 and the prototype ("Nothing is saved — that just
  answers the question", "Vesper isn't watching the reservation", "Vesper doesn't cancel them", "Vesper doesn't book
  stays…"). The boundary is now shown by the object: a door, a receipt, a stub. Audience and consequence statements
  ("Only you see this", "Sam sees your answer") remain, as the canon allows.
- **Physical grammar (kernel §11.7).** The 09:02 train now carries a **ticket stub** plate (03 B2, 09 J1a) instead
  of a gold sentence; the C1 invitation card carries a **facepile with the dashed empty chair** for the invitee who
  has not answered. Both are the kernel's wardrobe, not new components.

07 gained R-14 (this pass) and two mapping rows (Door law; type floor). **Still open for ruling:** kernel §11.8
("Shape default / itinerary demoted", 08-29) versus the 09-04 brief's editorial-itinerary family. This project
follows the brief; the kernel text has not been reconciled. Also noted, not fixed here: the Chat-root frames in
this project are placeholders and do not reflect the ruled Chat entry (§11.9) — the Chat lane should re-clothe them.

## 3h. Ruling — the itinerary is the default (2026-09-05, founder)

Resolves the conflict between kernel §11.8 (08-29, "Shape default / itinerary demoted") and the 09-04 brief.
Written into `docs/working/design-kernel-extraction-2026-08-29.md` §11.8 as a dated amendment; recorded on
boards 07 (R-14 ruled, R-15) and 00; drawn on 02 A9–A10.

- The editorial itinerary grammar is the default projection of any Plan or Occasion. The Shape's four questions
  (settled / open / who's in / unknown) are registers inside it — bold time with a door to its evidence, regular
  time, a gutter word, a "with …" phrase, a supporting line — never sections. Status buckets are prohibited as
  page organization.
- Structure is earned downward as well as upward: no rail below two days, no chapters below two parts, a single
  arrangement is the identity block plus rows, and **below one anchor there is no plan page** (a Move lives on
  its owner with a receipt).
- Two light states of the same grammar were added: **order-less material** drops the time gutter and renders as a
  plain list in the same type (A9); a **conditional pair** is one row with "or" in its title and the condition in
  the supporting line, never two branches (A10).
- Deliberately outside the family: a single Move, a ritual or recurrence (Life/Home), a same-day question
  (answered in the sheet, no plan created).

## 3i. §0.5 revision — better judgment, lighter completion, dependable recovery (2026-09-05)

Applied to boards 09, 10, 07 and `kit/proto.js`; composition family unchanged; no new screens.

- **A. J2f recommendation.** "Go early myself" removed as the primary action: it was permissible (change only
  your own participation) but not shown to be helpful, since the mother's attendance was never established. The
  recommendation is now the continuation the exchange supports: "Ask Ben about 10:15 →" (opens the J3a outgoing
  card; drafted words carry no private reason). Solo option stays reachable through Ask Vesper when it fits. No
  quieter substitute offered (the question was about this temple). No profile question, decision screen or menu.
- **B. Completion hierarchy.** J2f is now brief result → one observation → one optional continuation. "See it →"
  is a door inside the receipt sentence (ordinary navigation). Undo present and subordinate (`.undoq`). Six
  stacked elements became three; the day reads first.
- **C. Unknown wording.** J2e: "Checking whether Isuien was added. Your request is still here." Board 10 cards:
  "Checking whether that went through — your request is still here." "Nothing changed" reserved for confirmed
  non-application. Retry held while unresolved. Recorded as R-16 on board 07.
- **D. Prototype defects fixed in `kit/proto.js`** (backup `kit/proto.pre05.js.bak` local only):
  1. Discard clears the field only when it still holds the matching draft; edited/different input left alone;
     reopening does not resurrect the text.
  2. Undo entries are scoped (action id + prior values of exactly the keys it changed). Nora's Undo no longer
     reverts Sam's independent answer. Undo receipt names what came back.
  3. Private record per viewpoint (`state.priv[you|maya|sam]`: screen, preview, ask, offer, receipt, note, save,
     save_label, req_text, req_id, draft). Shared plan is one object. Deferred outcomes land on the owner's record
     via `asOwner()`. Viewer switch touches nobody's private record. Per-viewer undo stacks and timers.
  Test helper: `PIRL.say(text)`, `PIRL.field()`, `PIRL.priv`, `PIRL.undo`.
- **Friction log (09)** now distinguishes fixed / outstanding / illustrated / exercised; board 10 lists regression
  checks R1–R5. Outstanding: retry idempotency beyond one reconciliation asserted not modelled; the J3a card that
  "Ask Ben about 10:15" opens is drawn, not wired (Kyoto is not the interactive fixture); modal sheet vs in-flow region.
- Native and participant validation remain unclaimed.

## 3j. §0.6 — journey-to-system coverage specification (2026-09-05)

Deliverables: new board **11 Continuations** (K1–K2, G1–G3, I1–I2, W1–W2, F1–F2 + coverage table + Q15–Q19); 02 A4
aligned to the J2 follow-up pattern (field stays; no "Something else…"); 02 A9 "say a day" instruction removed;
07 R-12 wording aligned to the later rulings (no routine memory offer; draft custody is a proposal, Q14); 07 R-17,
Q15–Q19; 00 index. All new frames are **illustrated only**; nothing on 11 is wired into the board-10 prototype.
Engineering reuse below is from §0.6's inspected code (app `c03f909f8` / backend `424e2d23a`) and the
lightweight-arrangements handoff (A0–A4) — referenced, not approved or superseded; reinspect before implementation.

Status vocabulary: **illustrated** (drawn), **wired** (board 10 markup), **simulated/tested** (board 10 runtime,
in-app browser), **existing runtime** (code exists today), **proposed** (named gap).

### J-A — A thought becomes something useful later
1. **Start / value:** Chat, "maybe jazz Saturday"; a fixed dinner exists. Value = the option that fits, why, and the one exclusion (02 A1).
2. **Delivered before any ask:** the fit in the itinerary's own rows; no name, no container, no Trip.
3. **Entry / target / result / return:** "Keep it as an option" → the sparse page (A2). Return via Chat card (A6), Home card + "Places you've kept" row (11 K1), Life (Q2). Same identity block everywhere; no memory of the conversation needed.
4. **Owner / private / untouched:** the arrangement = lightweight Plan (handoff D1, proposed); the place = Places relationship; Theo's note stays Theo's. Dinner untouched.
5. **Interruption / disagreement / non-application / later:** release Saturday → place stays kept, no ghost row (A7, 11 K2); nothing about the place is deleted.
6. **Reuse / gap:** reuse `homecard` shape, word gutter, Places object page. **Gap:** Trip-independent retained intention with optional timing, owner references, scoped release — `LocalPlanScreen` and `planShape` are Trip-scoped; experience-graph Plan has owner/horizon/lifecycle but `update_plan` is metadata mutation.
7. **Evidence:** A1–A2, A6–A7, K1–K2 illustrated; board 10 starts kept (not wired); storage proposed (A0).

### J-B — Understand, follow up, adapt in context
1. **Start / value:** a stop on a shared Kyoto day; "would my mother enjoy this?" Value = a grounded answer with the one remembered fact labeled (08 P2, 09 J2a).
2. **Delivered first:** answer, then the field stays (J2b); no "Something else…" anywhere now (02 A4 corrected).
3. **Entry / target / result / return:** one pill → sheet with the row as target → correction within the exchange → "add Isuien" → accurate readback + observation + one continuation (J2f) → "Ask Ben about 10:15 →" opens the J3a outgoing card. Return: sheet closes, plan resting; Chat handoff carries target + unresolved intent (Q12/Q15).
4. **Owner / private / untouched:** the change is the requester's (their participation/additions); the mother's preference stays private; Ben's edit untouched.
5. **Interruption etc.:** pending (J2c), failed (J2d), unknown ≠ unchanged (J2e), draft recovered/discardable (J2g); all simulated on 10 with regression checks R1–R5.
6. **Reuse / gap:** reuse `PlanStopInspectSheet` target semantics but resolve ONE integration with the entity lane (the plan route also enters entity inspection today — two competing surfaces). **Gap:** contextual assistance with Chat continuity (streaming, expansion, interruption, return); `rootConsequences` adapters extended, not duplicated.
7. **Evidence:** illustrated (08/09); simulated + tested (10: pending navigation, failed input, discard, scoped undo, private records); Chat continuity proposed.

### J-C — Invite, contribute, participate without a committee
1. **Start / value:** host describes dinner (04 C1); guest opens a link (C2). Value for the guest = when/where/who/how/cost before any ask.
2. **Delivered first:** the guest page in the same type; two answers (in / can't).
3. **Entry / target / result / return:** guest: "Reply to Nora · she'll see this" vs the private Ask Vesper pill (11 G1); reply via the exact outgoing card; host sees reply/question/photo/contribution under the row, answers with one message (G2); guest's private question answered in the same sheet, nothing sent (G3). Editor within grant: same words simply apply (09 J3d).
4. **Owner / private / untouched:** plan = host's; messages = multiplayer lane; photo custody = Life; "Sam from 7:30" is participation, not an edit; viewing a link grants no edit rights.
5. **Interruption etc.:** decline is first-class (C2/C7); unanswered stays unanswered (05 D3); contributions never become edits.
6. **Reuse / gap:** reuse guest page (C2), outgoing card (J3a), attach/photo (C4); experience-graph invitation/decision facilities exist. **Gap:** guest delivery, bounded identity, reply channel and media custody without an account (Q9/Q16) — an RSVP endpoint is not this.
7. **Evidence:** illustrated (04/09/11); exercised on 10 for Maya's suggestion vs authorized edit and Sam in/out; guest channels proposed.

### J-D — A change cannot work for everyone
1. **Start / value:** Maya asks for eight (05 D2); owner previews who is affected (D3); sends. Value = consequences legible before sending.
2. **Delivered first:** the preview with responses and the reservation fact; silence ≠ acceptance.
3. **Entry / target / result / return:** Sam "can't do 8" → ink readback, one observation from expressed reasons (Maya's reading, Sam's 9:30), one continuation "Keep 7 — tell Maya and Sam →" (11 I1). Restaurant can't move → mismatch with source, one feasible alternative prepared not booked, "Ask … about Ostro at 8:15 →" (11 I2). After send: "sent · no answer yet".
4. **Owner / private / untouched:** plan = owner's; each person's answer = theirs; reservation fact = Commitment evidence (PCA-2); nobody's agreement restored from organizer intent.
5. **Interruption etc.:** provider evidence supplied, never inferred (D5/D6); a stale alternative explained (D7); send ≠ delivery ≠ acceptance.
6. **Reuse / gap:** reuse mismatch block, evidence pattern, J2f hierarchy; `plan_shape` viewer-relative participation logic (its guarantees, not its buckets). **Gap:** consequence-aware coordination and provider infeasibility as a state (Q17, handoff A3); grounded alternative search with real availability.
7. **Evidence:** illustrated (05/11); exercised on 10 (send 8, Sam can't, forward); resolution intelligence proposed.

### J-E — A conditional plan meets an ambiguous day
1. **Start / value:** "beach, or the Whitney if it rains" as one row (02 A10). Value = one compact expression, no branches.
2. **Delivered first:** on the day, the forecast in the row's supporting line and a recommendation in the row's preview card (11 W1) — both choices explicit, Maya's visibility stated.
3. **Entry / target / result / return:** a held backup is never auto-selected. With an explicit prior instruction and a clear condition, the row resolves with an attributed receipt + Undo (W2); an ambiguous condition still yields W1 even with an instruction.
4. **Owner / private / untouched:** owner's arrangement; forecast = evidence with freshness; dinner dependency untouched.
5. **Interruption etc.:** uncertainty preserved ("showers on and off"), not "the weather settled".
6. **Reuse / gap:** reuse D1 scoped alternative card, J2f receipt. **Gap:** condition meaning, evidence freshness, dependencies, action scope; a scoped revocable instruction as stored semantics (Q18, A0/D4).
7. **Evidence:** illustrated only.

### J-F — The day ends and something carries forward
1. **Start / value:** the morning after (11 F1). Value = the same page, past-tense kicker, nothing marked done by time passing, Sam's voluntary photo where Dana's was.
2. **Delivered first:** planned rows as planned; no questionnaire.
3. **Entry / target / result / return:** one correction through the pill ("the river, not the café") read back as a Saturday fact; three weeks later Chat reactivates by reference — last time's place/people/photo, a new "Keep the 17th" (F2); Sep 19 stays as it was.
4. **Owner / private / untouched:** correction = Plan fact; photo = Life/Place custody (pointer here); new arrangement = new lightweight Plan with owner references, never a copy.
5. **Interruption etc.:** an unfulfilled possibility simply stays a possibility (no inference); personal outcomes need not converge into one story.
6. **Reuse / gap:** reuse A1 chat-with-rows, A2 keep, C4 attach. **Gap:** passed-occasion lifecycle state; planned vs contributed record; owner references from a new arrangement to a passed one (Q19, D5); Life refinding is Life's.
7. **Evidence:** illustrated only.

### Engineering summary (from §0.6 C, restated for the receiving lanes)
Moderate presentation (all primitives reused), substantial integration: contextual assistance + Chat continuity;
lightweight intent without a Trip; contributions and scoped collaboration; participation vs shared consequential
fact; grounded adaptation/conditional plans; recovery across roots; non-app guest delivery. The Trip bridge's
legacy execution ownership is not to be competed with before cutover. AI interprets and explains; it does not replace
authoritative state, deterministic constraints, permission enforcement or arithmetic.

## 3k. Holistic-critique pass — board 12 (2026-09-05)

Founder asked for a holistic critique against the vision, journey traces, engineering complexity and coverage, then
"let's do it." Critique verdict: faithful on the page, weakest between pages. Four gaps closed or proposed on the new
board **12 Arrival, Stacking, Peers, Outcome**; everything illustrated only.

- **Arrival (N1–N3, R-18).** Lock-screen cues carry the receipt sentence and its one observation, titled by the
  arrangement; one per relied-upon change or ask; resolved facts never cue; grouped within the hour. Home shows the
  arrangement's state plus one sentence about what changed (two events that resolve together = one sentence).
  Opening from the cue lands on the plan at the recent region; no interstitial. Q20: notification decisioning + per-
  person "last seen" (a private record, as board 10 already models).
- **Stacking rule (S1–S2, R-19).** Recent region ordered by consequence (needs you / changed and matters / resolved),
  newest first within class; only the top item carries observation + one continuation; three lines then "and N
  more →"; lines leave on the person's action, never a timer. §0.5's hierarchy is the one-event case. S2 shows
  contraction after acting, with "sent · no answer yet" in the row.
- **Authority proposals (P1–P2, PR-1/PR-2, Q21) — NOT adopted until ruled.** PR-1: two participants, no named
  decider → either resolves loose material with attribution and mutual Undo; commitments keep their maker (Multiplayer
  §5.2 applied to authority). PR-2 (stress case): peer occasion, everyone shapes it → loose material changes freely
  attributed; an explicitly agreed time changes as a proposal to those affected, adopted by their answers, never by
  silence; no vote/deadline/approval surface (D3 register). Ceremony risk stated; scoped to explicitly agreed times.
- **Outcome (O1, R-20, Q22).** A materially better second occasion: Oct 17 booked at eight because the table could
  not move last time; Dana's dish note and Sam's 7:30 arrival as attributed facts with doors to Sep 19; Alex's guest
  line pre-carried. Outcome surfaces as a supporting register (like a ticket stub), scoped and removable in a sentence,
  never a statement about the person. Record is Person/Relationship-scoped; scope/provenance/audience and retraction
  at source are Q22.

Critique items recorded but not drawn (still open): groups larger than four; disputing a wrong recommendation beyond
typing; large text and voice as primary input; offline; guest identity when a link is forwarded (named on 11 G1).
Journey-trace frictions from the critique are listed in the conversation record and summarized on 12's lede.

## 3l. Subtraction pass — the Plan in seven sentences (2026-09-05)

Founder verdict after the holistic critique and board 12: "too complex … we tried to avoid too much operational
rules around changing, modifications." Ruled: the design is seven sentences; everything else is a consequence or
engineering. Written to `design-kernel-extraction-2026-08-29.md` §11.15 and
`docs/decisions/2026-09-05-adopt-the-plan-in-seven-sentences.md`.

**The seven sentences** (verbatim in §11.15): a page you read, always current · one way to change anything: say it
(direct controls only for finite real choices) · yours changes with one receipt and Undo; someone else's receives
your exact words, previewed · every event is a sentence on its row, nothing else added · at most one sentence at the
top says what needs you; cues only for that, bundled per arrangement per day; people tell people · Vesper states
facts, recommends once without a button only after a problem, can be turned off · failure says so once, keeps words.

**Cut applied to the live project.**

| Board | Before | After | Moved to |
|---|---|---|---|
| 04 C | 8 frames | 7 (C6 granted edit removed) | 90 |
| 05 D | 8 | 4 (D1, D3, D4, D8) | 90: D2, D5, D6, D7 |
| 09 Journeys | 15 + friction log | 6 (J1a, J2a, J2b, J2f, J3a, J3b); J2f chip removed | 90: J1b–d, J2c–e, J2g, J3c–d, log |
| 11 Continuations | 11 + 3 panels | 4 (K2, G1, I1, F1); I1 chip removed | 91: K1, G2, G3, I2, W1, W2, F2, panels |
| 12 | 8 + panel | deleted | 91 (all; PR-2 marked withdrawn) |
| 10 Interactive | — | renamed 92 Appendix · Prototype | — |
| 07 | R-1–R-20, PR-1/2 | the seven sentences + retirement map; B-1–B-7, mapping, reuse, questions kept | — |

Appendix boards carry an ENGINEERING APPENDIX banner and an APPENDIX tag on every frame; their copy predates the
subtraction and is kept as evidence. Pre-subtraction copies of every board are in the session scratchpad
`pirl/pre-subtraction/` (not in the live project).

**Retired:** R-1–R-20 as rules (mapped to sentences in §11.15); PR-2 withdrawn; PR-1 held as a proposal in sentence 3.
**Kept:** B-1–B-7 (upstream behaviour), the §11.8 amendment, type/material mapping, reuse map, Q1–Q22 as
engineering questions.

## 3m. Proxy validation — research-grounded walkthroughs in place of participants (2026-09-05)

No participant has been observed in this project. The founder asked for the next best thing: use the research and
judgment. Two paper walkthroughs, two questions each ("did they understand what the page was?", "did they know what
to say to change it?"). Predictions, not observations.

**Walkthrough A — the sparse Saturday (02 A1 → A2 → A4 → A5 → A7).**
- *What is this page?* Predicted pass. The identity block is a sentence in the person's own terms and the rows are
  the itinerary grammar people already read. Risk: the gutter word "Option" and "kept" — uncertainty-in-scheduling
  research (Haze, CHI 2022) finds people want to express tentativeness and that calendars force certainty; our
  registers allow it, but "Option ·" is product vocabulary. Test "maybe" and the person's own phrase first.
- *What would you say to change it?* Predicted partial fail. This is the gulf of execution/envisioning documented for
  natural-language interfaces (Subramonyam et al. 2023: capability, language and intentionality gaps; voice-assistant
  discoverability studies: people do not know what they can ask). Mitigations with evidence: (a) a contextual example
  phrase in the field derived from the selected row ("the later set instead"); (b) one suggested next phrase at the
  end of an answer (the LLM cooking-assistant study); (c) keep direct controls for finite choices — A3's set picker
  is validated by the bandwidth argument (tapping a known choice is ~10× faster than describing it). All three fit
  sentence 2 and none adds a screen.

**Walkthrough B — the shared dinner (04 C1 → C2 → C3 → 05 D3 → 11 G1).**
- *What is this page?* Predicted pass for both roles. The guest page matches the conventions Partiful and Apple
  Invites have taught (a link; when/where/who; two answers; no account). Risk: guests may look for the guest list
  (Apple Invites added guest-list visibility later on demand); ours shows names in the people phrase, which is enough.
- *What would you say?* For the guest: the two doors (reply to Nora vs ask Vesper) are labeled by audience, which the
  privacy-first reading requires, but it is the one novel affordance and should be the first thing tested. For the
  owner: moving dinner by saying it maps to the "propose new time" mental model; the novel part is D3's preview of who
  is affected and who has answered. RSVP benchmarks (Greenvelope, 70,624 events, 2025–26: median 85% response;
  personal events ~86%) mean 1 in 7 people will simply not answer — silence-as-state (D3) is the right default, and a
  gentle reminder should come earlier than hosts assume (trade guidance: 48 hours). Partiful's own advice after a time
  change is to text guests and ask them to re-RSVP — exactly sentence 5's "people tell people."

**Verdict.** Comprehension (question 1) is expected to pass in both walkthroughs. Knowing what to say (question 2) is
the main UX risk of the seven-sentence design and should be the first thing tested with people. Three
recommended changes, none applied yet, all within sentence 2: contextual example phrase in the field; one suggested
next phrase after each answer; direct controls retained for finite choices. What the research cannot answer: whether
the accurate-readback + one-sentence-observation form (J2f) reads as helpful or as a scold; no shipped product does it.

Sources: Partiful help (date/time change), Apple newsroom (Invites, Feb 2025) and AppleInsider (co-hosting, Jun 2026),
Google Workspace blog (propose new time), MobiLoud/ContextSDK push statistics, CHI 2024/2025 proactive-assistant
papers, Calm Technology principles, NN/g progressive disclosure, Subramonyam et al. "Bridging the Gulf of Envisioning"
(arXiv 2309.14459), Haze (CHI 2022, 10.1145/3491102.3502107), Greenvelope RSVP benchmarks 2026, julian.digital "The
case against conversational interfaces" (2025).

## 3n. PR-1 ruling (2026-09-05)

Founder ruled **defer** on PR-1 (two participants, no named decider, either resolves loose material). Until
participant walkthroughs show the asymmetry matters, the owner decides for two people and the other person says
it in words, as everywhere else. Recorded in kernel §11.15, the decision record, and board 07 sentence 3.

## 3o. Sentence-2 discoverability fixes applied (2026-09-05)

The three fixes recommended in §3m, applied to the boards that stay:

1. **Contextual example in the field before any answer.** 08 P2 ("move it to 10"); prototype 92 placeholders
   ("add the bookstore" / "add the bookstore at 4"). Rendered as `Ask, or say a change — “…”` with the example in
   ink-2 (kit `.field .txt q`).
2. **One suggested next phrase after an answer** (`.say`: "Or say “…”"): 08 P2b ("then add Isuien after"), P3
   ("Tuesday, but later"), P4 ("Tuesday afternoon instead"), P9a ("ask them about 4:30 instead"); 09 J2a ("then add
   Isuien after"); 02 A4 ("or skip the jazz"). The field returns to the generic "Follow up, or change something…"
   after an answer so the example is not shown twice.
3. **Direct controls for finite choices** — audited, all already present; inventory written into 07 sentence 2 and
   kernel §11.15. Nothing drawn.

Also removed the four remaining "Something else…" branches on 08 (P2b chip, P3/P4/P9a doors) that the §0.6 J-B
correction had missed; the field stays in every case.

## 3p. §0.7 post-subtraction refinement (2026-09-05)

**Changed existing frames** (same reduced family; appendices 90–92 untouched; nothing regenerated):
02 A4 (Or-say removed) · 05 D3 (prepared message with recipients and words beside Send; "Edit the wording"; annotation)
· 08 P3, P4 (Or-say removed; P2b and P9a keep theirs) · 09 J2a (Or-say removed), J2f (one sentence relating the move
to the crowd concern, with the 10:15 possibility, no button) · 11 I1 (thesis corrected; implication on top; one
possibility; one quiet door — PROPOSED), F1 (account, not rewrite; planned row stands) · 07 (§0.7 amendment list)
· 00 (status). Kit: `.page .outgoing` / `.qp .outgoing` rules.

**Before/after effort log.**

| Journey | Step | Before | After | Effort removed |
|---|---|---|---|---|
| Loose Saturday | Read the kept page and leave (02 A2 → close) | No prompt, no ask | Unchanged | — (successful read-and-exit, nothing further required) |
| Loose Saturday | "Make it less rushed" (A4) | Answer + Use/Not now + field + "Or say 'or skip the jazz'" | Answer + Use/Not now + field | One prompt the person did not need; the field still allows any continuation |
| Loose Saturday | Choose the set (A3) | Direct picker | Unchanged | — (finite choice stays direct) |
| Shared dinner | Inspect Tōdai-ji (08 P2) | Field "Ask, or 'move it to 10'" | Unchanged | — (one contextual example before any answer, kept) |
| Shared dinner | Move to Wednesday → Tuesday? (P3, P4) | Chips + "Or say …" on both | Chips + field | Two prompts; the scope question (temple vs morning) is kept because it is consequential |
| Shared dinner | Dana suggests 4 (P9a) | Send-as-suggestion + "Or say 'ask them about 4:30 instead'" | Unchanged | — (kept: reveals a non-obvious capability) |
| Changing day | Move dinner to 8 (05 D3) | Preview of affected people, then Send; the words to Maya and Sam implicit | Preview + prepared message with recipients and words + Edit + Send | The host no longer composes or retypes the change to tell people; prepared vs authored is explicit |
| Changing day | Sam can't do 8 (11 I1) | Objection stated in thesis (wrongly), receipt, people phrase, Sam's words; a recital of facts; mismatch block | Thesis true; implication once; one possibility; row carries participation + reservation door; Sam's words once | Three duplicated facts and one false summary removed; one possibility added (PROPOSED); a door instead of retyping "keep 7, tell both" (PROPOSED) |
| Changing day | Ben moved the temple (09 J2f) | Readback + observation | Readback + one sentence tying the move to the crowd concern with the 10:15 possibility | The person is not left to reconcile the schedule against what they said they wanted |
| After the day | "We went to the river" (11 F1) | Plan row rewritten + receipt "now says the river" | Planned row stands; account under it in her words; "noted" | No accidental rewrite of intention; no outcome editor |

**Amendment list.** *Compatible with the accepted seven sentences (applied):* selective guidance (sentence 2
addendum clarified: not compulsory); prepared message beside Send with prepared ≠ authored (sentence 3); say each
thing once from the same state (sentence 4); an account of what occurred is not a change (sentences 1/4). *PROPOSED
exceptions — need a new decision before adoption; labeled PROPOSED on the boards:* (a) sentence 6: one possibility may
follow the implication, and where adopting it means telling people, one quiet text door prepares the message (11 I1);
(b) sentence 7 clarification: "pending is silent" governs the resting page; the active interaction acknowledges a
submission (form on appendix 90 J2c); (c) sentence 5 clarification: per-day bundling is a non-urgent default; a distinct
urgent change is not suppressed. PR-1 remains deferred; PR-2 remains withdrawn; no authority expanded.

**Research corrections (§0.7 C), applied to §3m's claims without rewriting them:** "help welcome only after a
problem" is one UX-evaluator study (Kuang et al. 2024; timing did not affect performance) and one programming study
(Chen et al. 2025), not a rule for everyday assistance; the "five notifications a week" figure is vendor survey data,
not a threshold; "10× faster" is an essayist's estimate, not a benchmark; Partiful's non-notification is a familiar
convention, not an optimality result. Kernel §11.15 carries a dated correction note.

**Verification.** *Illustrated (rendered from the live project, headless Chrome, and inspected):* 05 D3, 08 P2–P4,
09 J2a/J2f, 11 I1/F1, 02 A4. *Scripted / mechanically checked:* none changed — the prototype (92) was not touched in
this pass; its R1–R5 checks from §0.5 stand. *Native-unverified:* everything. *Participant-unverified:* everything.
Live sync: pushed via DesignSync and re-rendered from the served project, not asserted from local edits.

## 3q. §0.8 content-and-continuation cleanup (2026-09-06)

Four existing treatments refined; two frames added to trace one continuation; nothing else grew.

- **D3 (05).** The draft message and recipients lead ("To Maya and Sam · Draft"); one consequence sending does not
  settle ("Your table is still reserved for seven"); action named for its effect: **Update & send** (owner
  instruction: the arrangement moves and the announcement goes out), Edit, Not now. Removed from customer copy: the
  per-person Maya/Sam/table lines, the prepared-vs-authored note, the correction-vs-unsend footer (now annotation).
- **J2f (09).** "Ben moved the visit to eleven, after the quieter window you asked about. Going together at 10:15
  would need his agreement." Replaces "10:15 is still yours to take", which implicitly encouraged a split. Annotation
  aligned: agreement to attend together, not owner approval of an authorized edit; nothing invented about Ben's
  availability; the pill remains for raising it.
- **F1 (11).** The reported afternoon takes the title ("An afternoon by the river"), attributed ("You said you went
  here instead of the café"), original intention beneath in muted type; gutter word "after" (no invented time);
  people phrase omitted (no attendance asserted). "What was planned stays as it was" removed from copy; the
  invariant lives in the annotation.
- **I1 → I1b → I1c (11).** The door now reads "Prepare a proposal for Maya and Sam". I1b: the prepared proposal in the
  J3a outgoing-card family — recipients, editable question-shaped wording, **Send proposal** (a message; dinner stays
  at eight until they answer), Edit, Not now (contacts no one). I1c: readback — what was sent (her words under the
  row), what did not change (thesis and row still eight; ink receipt states it once), what is unanswered (both).
  Contrast with D3 stated on the frame: expressed intent + outgoing effect, not a new screen. Both PROPOSED under the
  sentence-6 exception. Board 11 is now six frames.
- **Record-keeping.** Selective prompting is recorded on 07 and in kernel §11.15's correction note as a relaxation
  of the accepted sentence-2 addendum wording, alongside the proposed amendments, not as unchanged canon.

**Verification.** *Illustrated (pushed via DesignSync, rendered from the served project, inspected):* 05 D3, 09 J2f,
11 I1/I1b/I1c/F1, 07, 00. *Wired:* none — the prototype (92) was not extended; its §0.5 regression results are not
evidence for the message or proposal paths. *Native-unverified, participant-unverified:* everything.

## 4. Verification (live project, 2026-09-04)

- Every board rendered from the **live project** via `render_preview` serve URLs in headless Chrome
  (viewports 2100–3700 px wide) and read at full resolution; console clean on 02 and 10 in the in-app browser.
- Frames: 393px; one 320px · 135% text frame (03 B7). Google Fonts EB Garamond + JetBrains Mono load;
  fallbacks Georgia/Menlo recorded on 01 and 07.
- **Defects found and fixed during verification:** (a) frame labels overran neighbouring frames and the
  fold label bled into the next frame — board chrome, fixed; (b) at 135% a fixed 44pt gutter let "09:02"
  collide with the title — the gutter now scales with text (44→59pt), noted on B7; (c) long day titles
  ("Saturday, September 6") orphaned a digit beside "Details →" — title row now wraps the door below;
  (d) the DC runtime rewrites camelCase words followed by "=" in text (`numberOfLines=2` →
  `sc-camel-…`) — copy rephrased; (e) elements with an author `display` class ignored the `hidden`
  attribute in the prototype — `[hidden]{display:none!important}` added to the kit; (f) prototype
  runtime guarded against double evaluation and stale array references after reset.
- **Prototype mechanical checks (10):** the seven-step walkthrough (inspect · contribute without editing ·
  authorized edit · participation · scoped alternative → adoption → Undo · consequential change with
  preview, send, no Undo, mismatch, Sam's answer, forwarded confirmation · return via Home) passed against
  `window.PIRL.state`; a real DOM click on "Add to the afternoon" changed state; all visible buttons ≥44pt;
  no horizontal overflow at 393px. After the runtime fixes, a fresh load applies the initial state (three preview cards hidden, one page visible, thesis rendered); real DOM clicks on “Rain at 4 — see an alternative” → “Use this” → ‹ Home → “Open Saturday” changed state and visibility as designed with Undo surviving re-entry; the composer routes by Enter and by Send (“let Maya help with the afternoon”, “the café if it rains”, “move dinner to 8”, “forward the confirmation”, “undo”), and an unsupported phrase (“book me a hotel”) leaves state unchanged with an honest note. Recognizers are regexes with state guards, not parsing.
- **§0.1 revision verification:** boards 08, 02 and 03 re-rendered from the live project in headless Chrome
  after the push and read at full resolution (sheets, kickers, chips, pills, transient receipts all legible;
  no overrun). Prototype 10 on a fresh load: pill visible, field hidden, ASK slot; pill opens the field with
  the private kicker; "book me a hotel" keeps the words and changes nothing; "let Maya help with the
  afternoon" applies, clears the field and closes it; "Not now" closes with no mutation; "Continue in Chat"
  states it is not built; Maya's kicker reads private-with-grant vs suggestion-to-Nora by grant state; all
  visible buttons ≥44pt; no horizontal overflow; console clean.
- **§0.2 verification:** boards 08, 02, 03 re-rendered from the live project after the push and read at full
  resolution (value-first sheets, read-only answer, fixture labels, composed jazz row, P6b, P9a, P10 options).
  One layout defect found and fixed: the longer 08 header ran into the first frame labels (frames moved
  down). Prototype 10 on a fresh load: pill reads "Ask Vesper", capsule has no ASK slot, no composer at rest;
  Maya's private kicker; "add Willow & Page" without rights → private answer + visible "Send to Nora as a
  suggestion", which sets the shared suggestion the owner then sees; with the grant the same phrase applies
  with attribution; "More room in Chat" states it is not built; all visible buttons ≥44pt; no horizontal
  overflow; console clean.
- **§0.3 verification:** board 09 and the corrected P9b rendered from the live project and read at full
  resolution; one defect (sheet ✕ overlapping the kicker) fixed and re-rendered. Prototype 10 on a fresh load,
  driven by real button taps and Enter: Maya's "could we do 8?" prepares privately (owner sees nothing) and
  reaches the owner only after "Send to Nora as a question"; with "Failed save" armed, a tap on "Add to the afternoon" shows the pending state with the plan unchanged, a second tap is refused ("Still saving the last change…"), the failure shows with the words kept and "Try again" then lands the change once; with "Interrupted" armed, adopting the café shows "checking…", a repeat is held, and the change reconciles once with "it had gone through" appended; with "Slow save" armed, "let Maya help with the afternoon" typed in the field shows pending, then the grant applies; with simulation off, taps apply immediately as before; all visible buttons ≥44pt; no horizontal overflow; console clean. Illustrated only (not mechanically tested): value-first content, read-only answers, retrieval, keyboard-open/expanded sheet, resume across Maps/provider/background, Chat continuation.
- **Not verified:** native Dynamic Type / VoiceOver; any participant; motion (the kit animates nothing and
  states swap instantly, which is the reduced-motion treatment by default); contrast beyond token-pair
  inspection (mute #6E6862 on paper #EFEAE0 ≈ 4.6:1; gold-deep #8A6628 on paper ≈ 4.0:1 — used for
  stamps/labels, not body); the 320px frame at 100% text; keyboard focus order in the prototype.

## 5. Decisions returned (see board 07)

- **Answered:** the eight §7 composition decisions (primary organization, current vs possible, read vs
  act — revised per §0.1 to the contextual-request pattern — precision, people, change, continuity, density).
- **Preserved, not re-decided:** owner-edits-by-default and scoped grants; possibilities create no approval
  debt; preview ≠ adoption; agreement ≠ reservation ≠ personal fixed point; Undo scoped, correction not
  unsend, silence ≠ acceptance; link ≠ booking; typed operations resolved server-side.
- **Open, with owners:** Q1 retained intention model (Components & Plan); Q2 Life anatomy; Q3 Chat pointer
  (PCA-3); Q4 Home admission; Q5 entity readback; Q6 "ignored" as no state; Q9 guest delivery; **Q10 (new)**
  compact header — selection follows scroll vs show both; **Q11 (new)** the four proposed type roles against
  the serif-floor / fontSize ratchets and the fate of `itineraryChapterThesis` 13 italic.
- **Contract amendments proposed by this project: none new.** It relies on the lab's PCA-2/3/4 as labeled and
  disagrees with nothing in Multiplayer §5.1–5.2, the lifecycle contract, or C&C. Where the lab treats all
  shared time updates as quiet feedthrough, this project draws the heavier path only for a relied-upon agreed
  time (05 D2–D3) and the lighter path for uncommitted material (05 D1).

## 6. Compliance

New project created rather than overwriting the lab; lab preserved; no repo source, flag, contract, or token
changed; all people/venues/times/reservations/forecasts synthetic and labeled; research chrome (viewer
switch, state readout, supported phrases) outside the phone; no serve URLs in user-facing text or this
report; no booking execution, permissions center, Arrangements tab, or status-grouped composition drawn.
