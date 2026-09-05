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
