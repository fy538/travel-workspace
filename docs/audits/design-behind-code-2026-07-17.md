---
doc_type: working
status: active
owner: founder / design
created: 2026-07-17
last_verified: 2026-07-17
expires: 2026-08-16
why_new: Independent fresh-eyes audit of where the Vesper design canon (Claude Design bundle "vesper 220") is BEHIND the shipped code. Input for the next design-iteration sessions in Claude Design.
supersedes: []
incorporates: "~/Documents/Claude/Travel Workspace/docs/vesper-220-design-behind-audit.md (the Trip/Itinerary object-inspection deep audit, folded into §1 and §6 on 2026-07-17; overlapping scopes adjudicated here — see §1 note)"
source_of_truth_for: [design-canon-vs-code-gap-inventory-2026-07-17]
---

# Where the Design Is Behind the Code — vesper 220 vs repos @ 2026-07-17

## Post-remediation delta

The companion engineering waves through `travel-app@95b1c2fa` and
`travel-agent@8526bc37` change several reverse-audit assumptions. Claude Design
should now treat these as shipped code truth:

- Vesper 220 is the active fingerprint and all canonical Trip routes have live
  surface owners; broken owner references are gate failures.
- Object Detail and Changes no longer expose raw IDs, numeric confidence, raw
  reason codes, or canonical/ledger implementation language. The design's
  human-readable provenance doctrine remains binding, but this is no longer a
  code defect to reproduce.
- ChangeStudio now includes explicit itinerary-only versus booking-updating
  replacement consent, Was/Now/protection/recovery/revalidation, and a
  three-truth stale-draft recovery state.
- Discover Map now has scope/layer controls, exact-trip context, preserved
  venue/Vesper handoffs, location-denied recovery, and an offline mode limited
  to saved/in-plan pins. Venue, experience, place and friend pins are now typed
  runtime objects with distinct accessible forms and canonical handoffs.
  Friend-location specimens must preserve the shipped privacy boundary:
  authenticated trip context, exact trip-scoped provenance, under-15-minute
  freshness, viewer exclusion, rounded coordinates and no legacy fallback.
- Atlas seed entrances are state-driven, Chat depth is live for booking, vote
  and research, Universal Search action receipts have stable destinations, and
  completed Trip owns the unresolved-settlement pointer.
- Stay's previous provider-hold implication has been removed; an internal
  decision marker must not be drawn as protected inventory.
- The current durable-agency implementation now enforces three plan-editing
  modes (`open`, `review`, `organizers`), persists Vesper consent separately
  for suggestions/minor fixes/major changes, and persists viewer-owned
  quiet-trip plus proactive notification-family choices. Claude Design should
  treat these controls as functional, not speculative. Costs/Booking entry
  authority now persists who may add expenses and start booking work;
  session participant consent and self-only fallback are now enforceable.
  Controller-only reminders to named pending travelers now use the shared
  notification pipeline, persist delivery evidence, honor its cooldown and
  deep-link back to the booking session. Provider-confirmed checkout,
  reconciliation, restaurant, and paid-hold paths now emit replay-safe shared
  trip-room receipts even without a concierge proposal. Expense disputes are
  now durable: affected travelers open, openers withdraw, payers/organizers
  resolve, settlement pauses, and each transition leaves a shared receipt.
- Archived-trip recovery is now a shipped lifecycle contract. Organizers can
  restore the preserved shell to its exact pre-archive phase; only rooms
  archived by that transition reopen, while proposals, searches, workflows,
  notification outcomes, and invites closed by archive remain closed. Canon
  should draw this bounded recovery and must not imply that all earlier work
  resumes or that every recovered trip returns to Planning.
- Trip-level cancellation and reuse-as-template are now shipped contracts.
  Cancellation is organizer-only, begins with a booking/provider-truth
  preflight, never claims to cancel a reservation, preserves confirmed booking
  and unsettled Costs records, and retains a readable cancelled trip. Reuse
  creates a clean undated solo draft from itinerary shape only; it strips
  travelers, bookings, Costs, votes, conversations, workflows, dates, times,
  commitments, prices, and provider state. Canon should draw the blocked and
  ready cancellation postures, retained record, and explicit reuse
  consequences without treating reuse as recovery.
- Terminal lifecycle is now enforced at execution boundaries, not merely in
  route visibility. Late booking/proposal/workflow/planning/message writes,
  notification and invite delivery, scheduled coordination work, recurring
  pre-trip work, and calendar auto-completion all stop after cancellation.
  Money/reconciliation notices and completed-trip story/memory work remain by
  explicit policy. Designs must not imply that cancelled trips silently resume
  queued coordination or that retirement erases financial/provider truth.
- Optimize Route now carries and renders a typed consequence for every stop:
  current/proposed position and time plus kept, moved, retimed, or both. Claude
  Design should treat compact WAS/NOW consequence evidence as shipped Optimize
  behavior. The remaining code-side delta is Replan-wide
  added/moved/removed/kept projection and richer initial parallel-plan
  construction.

Accordingly, remove the resolved items from §7's code-behind appendix. The
highest-value remaining design/code convergence seams are now the deeper trip
and booking lifecycle states plus typed object producers—not a new shell.

**Scope + method.** Independent investigation, deliberately run without reading any prior design-alignment/audit prose in the repos. Sources: the Claude Design handoff bundle at `~/Downloads/vesper 220/project` (canon self-labels **Canon 130**; its governance changelog runs through **2026-07-12**, cleanup verification through 07-13) diffed against `travel-app` + `travel-agent` at HEAD (**commits through 2026-07-17 ~10:30**). Five parallel domain audits (Trip/Itinerary, Money, Chat/Home/Voice/Search, Atlas/Discover/Post-trip, Group/Invite/Sharing) each read the canon JSX sources and verified claims against actual code, not commit messages, plus a cross-cutting route + July-15→17 sweep. Direction judgment applied throughout: **only design-behind-code is reported in detail**; code-behind-design is noted in one-liners at the end.

**Severity key.** **P0** = canon actively wrong/misleading about an enabled surface in a way that would produce false, unsafe, privacy-breaking, or materially unusable behavior. **P1** = enabled user-facing feature/flow with missing target coverage, or implemented flag-dark infrastructure that needs design before activation. **P2** = state/edge coverage gap, taxonomy/ledger reconciliation, or canon self-inconsistency.

**Classification key** (adopted from the companion object-inspection audit — it encodes *why* a gap exists and therefore what the fix is): **design-behind** = draw something new; **consolidation gap** = the concept exists in folded/transitional/companion material but the active owner never absorbed it — migrate, don't reinvent; **application gap** = shared doctrine exists (e.g. State System) but the surface has no applied specimen — apply, don't redesign.

---

## Executive summary

The canon did a genuinely good job tracking the product through ~07-12 — several July code commits literally cite canon files by name, and whole systems (post-trip spine, stay votes, working states, Your Memory) shipped nearly verbatim from the boards. The debt is concentrated in **what shipped after the canon's last governance pass**: the **Jul 13–16 itinerary cutover** (14 normalized engine operations, canonical shell default, legacy Folio deleted), the **Jul 13–14 correctness campaigns** (settlement payments ledger, group-coordination hardening, invite loop Slice H, chat reliability), and the **Jul 15–16 wave the canon has never seen at all** (flag-dark monetization/paywall infrastructure, booking-cancellation lifecycle, group-chat read sync, shared group memory). The strongest P0s are direct truth/privacy/authority contradictions; the larger tail is active-owner omissions, consolidation gaps, and stale governance. One entire launch-readiness area (**monetization**) has no design owner. The canon's own §06 claim — "No open visual-pass items as of 2026-07-11" — is no longer true and should itself be revised. (Provenance note from the companion audit: vesper 220 differs from 219 only by the Post-Trip Continuity page — the Trip/Itinerary material did not change between packages, so these gaps are not a packaging artifact.)

The single highest-leverage session order for Claude Design: **(1) Canonical Object Inspection v2 + the Workflow vocabulary mapping (§6a), (2) Discover cover redraw to the gen-6 feed + wedge CTA, (3) a new Monetization page, (4) Costs recorded-payments + masked-expense correction, (5) a Chat "reliability & multiplayer states" pass, (6) ledger corrections (External Sharing privacy doctrine, Atlas alignment ledger, Architecture §18).**

---

## 0 · Cross-cutting (found in the Jul 15–17 sweep; no domain agent covers these)

### 0.1 · Monetization / commercial gating — an entire missing launch-readiness area — **P1 (flag-dark)**
- **Code (Jul 15–16, a 7-phase program):** `travel-app/context/CommercialUpgradeProvider.tsx`, `billing/` (RevenueCat client, `upgradeConfig.ts`, `commercialDenial.ts`, `accessReconciliation.ts`), `docs/monetization-phase-7.md`. Implemented mechanics: capability-gated commercial denials (`candidate_paid` / `limit_reached` are upgrade-eligible; other errors must never be relabeled as upsells), RevenueCat native paywall per placement (`commercial_gate_voice` / `_ai` / `_trip` / `_travel`), paywall only from a user gesture (never background), post-purchase **server-convergence wait** (store result doesn't unlock; app polls `GET /api/me/commercial-access`), Restore/Customer Center entry at **Account → Purchases & subscription** (`app/atlas/account.tsx`), no-offering = respected (no silent fallback), product events for presented/result/not-offered. Presentation is dark by default (`EXPO_PUBLIC_COMMERCIAL_PAYWALL_MODE=off`); voice-token denial is the first wired trigger (`hooks/useVoiceSession.ts`). Treat this as design-before-activation, not proof of a broadly shipped paywall journey.
- **Canon:** nothing. No monetization/paywall/upgrade page exists anywhere in the bundle; Trust & Controls has no Purchases row; no denial-moment, limit-reached, activating/convergence, or restore states.
- **Iterate:** a new **Vesper Monetization & Commercial Gate** page: the denial moment (candidate-paid vs limit-reached copy registers), the pre-paywall beat (what Vesper says before handing to the store sheet), the post-purchase "activating…" convergence state (and its timeout → "retry the action" honesty copy), Purchases & subscription row in Settings, and the *never-upsell* rule list (which error shapes must not present a paywall) as binding doctrine.

### 0.2 · Itinerary code cutover finished Jul 15–16; design-reference retirement still needs parity adjudication — **P2**
- **Code:** canonical itinerary shell made **default** (`088ff79a`), legacy Trip Folio frontend **deleted** (`70261e76`, `c08c9030`, "Purge retired Folio cache state"), trip entry routed itinerary-first with an entry resolver + pre-itinerary trip shape (`4e5a5bed`), rollout flags retired, CI ratchets ban legacy readers.
- **Canon:** the Canon Index still routes implementation through "Trip Document = IMPL REFERENCE / LEGACY MIGRATION SOURCE" and "Itinerary = transitional source"; Architecture & Coverage §18 still marks the route migration REQUIRED (see 1.10). Invitee Post-Join is still drawn on the retired Folio shell (see 5.3).
- **Iterate:** refresh the cutover facts and rerun the responsibility-by-responsibility retirement gates. Reclassify a transitional design source as historical only where visual, behavioral, route, and support parity are verified; legacy-code deletion alone does not prove full parity with Trip Visual Canon. Re-anchor every surviving page that still draws on the retired Folio backdrop to the canonical itinerary shell.

### 0.3 · Group-chat cross-device read sync + re-entry (Jul 16) — **P2**
- **Code:** "Sync group chat reading position across devices", "Reconcile group chat unread counts", "Improve group chat usability and re-entry" — reading-position and unread-count now server-reconciled.
- **Canon:** Chat owns thread grammar, Notifications owns unread awareness — but no rule for cross-device read-position (what "caught up" means when you read on another device) or the re-entry scroll anchor.
- **Iterate:** one rule + one state: re-entry lands at last-read marker, unread counts reconcile silently.

### 0.4 · Shared group memory with conflict edits (Jul 16) — **P2**
- **Code:** group memory moved to a shared store (BE); FE `components/chat/GroupAgencySheet.tsx` gained **optimistic concurrency + conflict-preserving edits** ("Preserve group memory conflict edits") — a member editing group memory can now hit a version conflict and keep their edit.
- **Canon:** `group-agency-board.jsx` has no conflict state on the agency sheet.
- **Iterate:** add the conflict beat (your edit vs newer version, keep/merge) to the group-agency board.

### 0.5 · Route-map coverage — routes shipped but absent from §02b's 62-route map — **P2**
In code, not in the canon route map (after honoring canon's stated exceptions): `/(tabs)/trips/[tripId]/object/[kind]/[objectId]` (the canonical typed-object inspection route, including ordinary objects and history records — see 1.11/1.16), `/(tabs)/trips/[tripId]/details` + `/details/[section]` (the Details entrance the canon itself ruled into Trip Visual Canon but never routed), `/(auth)/goodbye`, `/atlas/whole`, `/atlas/scan`, `/atlas/candidate/[id]`, `/atlas/unpacked-card`, `/atlas/shared-links`, `/atlas/removed`, `/atlas/narration-history`, `/atlas/voice-logs` (Atlas tail partly under the Trust & Controls exception — adjudicate which). Conversely `/your-map` was ruled **KILL → redirect** by canon and still renders — that half is a code cleanup, not design debt.

### 0.6 · Binding doctrine for ALL passes: don't copy engineering artifacts into targets *(from the companion audit — adopted project-wide)*
When drawing a shipped surface, **exclude raw canonical IDs, truncated linked-object IDs, numeric model confidence, raw reason codes, and internal phrases like "canonical sources"** from traveler-facing target UI, even though production renders them today. These are implementation scaffolding — *code-behind-design*, not design-behind-code. Preserve the underlying truth and correction behavior via human-readable labels, relationships, provenance, and recovery language. Without this rule, every catch-up pass in this doc risks faithfully reproducing engineering chrome as canon.

---

## 1 · Trip / Itinerary / Changes (6 P0 · 12 P1 · 1 P2)

The July IR-series + cutover made the backend the operational authority; the Workflow Canon's *doctrine* (inspect≠edit, typed ops, four authority endings, capability-authored Undo, plan-vs-provider truth) is validated by code almost clause-for-clause — but its concrete vocabulary and rendered journeys now trail the product.

> **Incorporation note.** Findings 1.16–1.20 and the merged material in 1.10/1.11/1.14 are folded in from the companion deep audit (`vesper-220-design-behind-audit.md`, adversarially revalidated, 4 suites / 37 tests at `9ec97d63`). Its central synthesis is adopted here: the individual gaps below the itinerary spine are really **one design program — a canonical object-inspection family with typed variation** — and that program, plus an operation-family↔engine-operation mapping, is now design session #1 (§6). Scope boundaries are preserved: Workflow Canon's operation doctrine and production journeys remain valid and should not be reinvented, while its vocabulary mapping and the applied ChangeStudio menu need updating (1.1/1.2). People & Collaboration adequately owns rosters/member actions; the distinct shared-plan succession + atomic-departure slice remains missing in Trip Settings (1.8). Verified exclusions are recorded in §6b.

1. **P1 — Traveler-facing operation families are not mapped to the 14 normalized engine operations.** Code ships **14 normalized types**: `materialize_shape, add, move, reorder, replace, remove, restore, set_attendance, mark_occurrence, create_parallel_plan, update_parallel_plan, dissolve_parallel_plan, optimize_day, replan` (`travel-agent/backend/core/models/itinerary_operations.py:196`; FE mirror `utils/api/itineraryOperations.ts`). Canon presents six traveler-facing families: Move · Replace · Add · Remove · Split/Rejoin · Optimize/Replan. Those abstraction levels can legitimately differ; the gap is the missing binding map and the omission of visible personal-record/recovery capabilities. → Add a family↔normalized-type board: Move/Reorder; Split/Rejoin→create/update/dissolve parallel plan; personal record→attendance/occurrence; recovery→restore; shape materialization; Optimize/Replan. Keep plain-language families where useful; do not expose fourteen backend identifiers as fourteen top-level UI verbs.
2. **P0 — ChangeStudio sheet anatomy.** Shipped `LowRiskOperationSheet.tsx` (770 lines): three sections **STRUCTURE** (Move/Reorder via relative Before/After + drag gesture, Replace, Add near this, Create/Change parallel plan), **YOU & THE RECORD** ("My attendance": attending/not/undecided; "Record what happened": happened / didn't happen / still planned), **REMOVE**; disclosure line "Each choice is one typed operation…"; stages menu→preview(`PREVIEW · DIRECT/CONFIRM/PROPOSE/DENIED`)→landed/proposed/recovery, capability-gated from the server. Canon's ChangeStudio (itinerary-canon.jsx ~935) still draws PLAN/MARK/VIEW/REMOVE with "Mark as skipped" (no such state — occurrence is `happened/did_not_happen/planned`) and pick-a-time-slot move (placement is relative). → Redraw to the shipped sheet.
3. **P1 — Parallel-plans lifecycle beyond Split/Rejoin.** Code: topology owner + per-branch decision owners/travelers, `starts_after`/`rejoins_before` anchors, "no scheduled rejoin", branch editing after landing, branch-stop cancel + restore-absorbed-stops, **dissolve as a server-authored reversal with exact-return validation** (`itinerary_parallel_recovery.py`; FE `ParallelPlanEditor/Summary.tsx`). Canon Workflow §E stops at create→assign→commit→rejoin. → Extend §E with the post-landing branch lifecycle.
4. **P1 — Commitment-state vocabulary.** Code: 10 `commitment_state`s (`open|suggested|proposed|tentative|confirmed|handed_off|booking_in_progress|booked|cancelled|completed`) + `structural_role` (anchor/soft_suggestion) + participation scope picker in Add ("Just me / A subgroup / Everyone"). Canon chips: `planned, booked, held, changed, now, done, skipped, gap`. → Add a commitment↔chip mapping board + the Add ownership step.
5. **P0 — Changes screen model.** Code (`changes.tsx`): Changes = **applied-history record** (TODAY/EARLIER, seen/unseen dots, degraded-envelope states, "What changed since you looked."), open decisions rendered as a compact vote block on top routing to Proposal detail — no in-row Undo, no mixed timeline. Canon draws a merged votes+timeline surface with in-row Undo. → Split the page model to record-vs-decisions; recovery lives on operation detail.
6. **P1 — Provider-saga endings.** Code: saga states incl. `manual_action_required`, **price-changed reapprove/decline** (quote-hash + final human approval), hold-expired, `provider_payment_outcome_unknown` retry-blocking. Canon Workflow §B has pending/refund-failed/retry/partial only. → Add a saga-endings board.
7. **P1 — Traveler-reported (attested) bookings.** Code: `handed_off → user_reported_booked` via attestation gateway; UI "Booked · reported by traveler". No canon concept. → Add the attestation posture to plan-vs-provider truth.
8. **P0 — Organizer departure/succession.** Code: handoff+departure are **one atomic action**; shared-plan ownership is a second transferable role with required successor + departure preflight (balance guard) + membership fencing. Canon's Trip Settings shows separate handoff, warns "Leaving without assigning will freeze the trip" (impossible now), and promises a 30-day retention claim its own doctrine forbids. → Redraw as atomic handoff+departure with successor step; delete freeze/retention copy.
9. **P1 — Trip date shift.** Code: preview → per-item dispositions (`undated / outside_new_range / unchanged / remap`) → atomic contextual `replan` commit, with blocked-shift ending; "flexible" hands off to Vesper. Canon's "Queue date change" state was never built. → Replace queue with preview→atomic-commit + dispositions.
10. **P1 — Architecture §18 handoff matrix + coverage claims stale** *(merged with companion D7, governance gap)*. Every §18 row still "CODE AUDIT REQUIRED / ROUTE MIGRATION REQUIRED" even though the code cutover and legacy-UI deletion shipped (Jul 15–16); full visual parity still requires adjudication rather than assumption. Additionally the coverage matrix marks **Object Detail design "complete"** while the active component API supports only `booking | flight`, and the consolidation page claims "no open visual-pass items." → Refresh §18 with verified code status; keep any still-unverified visual/support parity explicit; flip Object Detail type coverage / object-state coverage / history-record integration / Trip Details difficult states to **partial**; scope or remove the no-open-items claim.
11. **P1 — Operation detail/history/revert boards live only in a "NOT CANON" file** *(merged with companion D4, consolidation gap)*. Code ships `/object/[kind]/[objectId]` + `ItineraryOperationDetail` + revert-preview ("one server-built reversal against current itinerary truth"), predicted-recovery vocab (`undo|withdraw|review_revert|provider_action|new_change|none`), tombstone→successor lineage, stale-reversal review — and exposes **`history_record` through the same canonical object route**, making a live decision among Undo / provider recovery / new Change / no recovery. The only rendered designs sit in `itinerary-redesign-history.jsx` stamped "TARGET / EXPLORATION · NOT CANON". → Add one canonical **History Record specimen** to Trip Visual Canon as a member of the object-detail family (1.16) that *consumes* Workflow Canon rules (operation identity + human summary, initiator, what changed, current/successor object, provider consequence, exactly one live recovery path, no stale Undo, Back to Changes or originating object); promote the folded boards; update the "server-proven" ledger.
12. **P1 — Proposal machinery.** Code: auto-supersede of overlapping open proposals, rebased-proposal minting (`rebased_from/to`), `proposal_policy` (organizer_review / affected_member_vote), aggregate-only tally lines. Canon lacks superseded-by-overlap and rebase lineage, and its per-voter VoteReceipt is unreconciled with the aggregate-only stance. → Add both states; pick one voting-visibility rule.
13. **P2 — Trip-creation card vocab drift.** Code stamps `TRIP CREATED / SHAPING UP / STILL SHAPING` + an ambiguous-outcome "couldn't confirm — safe to retry" state; canon (07-12) stamps `READY TO BECOME A TRIP / CREATING… / …` without the unknown-outcome card. → Align stamps; add unknown-outcome.
14. **P0 — Object-level truth & failure states unapplied** *(upgraded from P2; merged with companion D2, application gap)*. The State System doctrine exists, but canonical object inspection has no applied specimens for what production actually distinguishes: complete · partial/degraded canonical sources (`partial_data` + per-source `degraded/unavailable` reasons — "Canonical history is temporarily limited…") · canonical authority unavailable (fail closed) · true absence · unverifiable facts · cancelled-but-inspectable · structurally locked/authority-denied · attendance-only or occurrence-only correction · provider partially completed · manual provider continuation · controller-only provider detail. **Degraded source data must never render as factual absence.** → Render the five-state strip on the ordinary-event/provider-booking foundation: complete / sources-limited (quiet notice naming the limited source) / facts-unavailable (fail closed + Retry, absence not inferred) / cancelled-or-locked (readable, no structural Change, permitted personal correction stays) / provider-partial (plan, reservation, cost truth kept separate).
15. **Canon self-declared OPEN (schedule):** Trip Document reactions/pace check-ins (no owner); coverage-matrix "lifecycle + edge states" column missing; whole-bundle render audit never run; Changes delegation hand-off dark.
16. **P0 — Canonical object detail supports two fixtures; production inspects seven object families** *(companion D1)*. The active Trip Visual Canon `ObjectDetail` accepts only `booking` and `flight`, both drawn as near-identical hold receipts (held-until, hold note, time band, Plan Truth, Confirm Hold, See in Itinerary). Production's canonical object route serves **event · stay · transport leg · provider booking · expense · place · history record**, with conditional authority, linked facts, participation, provider truth, corrections, history, and recovery. The most common entrance from the spine — an **ordinary event** (walk, meal, museum) — has no definitive full-screen target at all. → Design **one coherent object-detail family with typed variation**, anchored by a definitive ordinary-event screen answering in traveler language: what is this / when & where / what does the plan say / who's participating / anything unresolved / related facts / what can *this viewer* do / where does Back return. Do not carry the engineering "Stable Identity" card into the target (see §0.6).
17. **P0 — Object-detail action hierarchy** *(companion D3)*. The active specimen demonstrates Confirm Hold + See in Itinerary; production conditionally exposes Change · Confirm booking · Release hold · Report as booked · Continue/retry booking session · Place · Map · Ask Vesper · Split the cost · Correct occurrence · Open connected facts · Undo (exact-inverse only) · Start new change (no inverse) · Continue provider recovery (controller only). The design problem is priority + semantic separation, not button count: a linked expense must not inherit structural Change; provider continuation is not Undo; cancelled stays inspectable without Change; attendance/occurrence correction can outlive structural editability. → Define the action grammar: one primary permitted operation, one secondary when necessary, restrained More-Actions disclosure, a distinct recovery treatment, no inert/misleading action on denial, no universal Change/Undo/Dismiss language.
18. **P1 — Trip Details truth states** *(companion D5, consolidation/application gap)*. Production distinguishes populated · truly-empty · degraded-source-where-absence-can't-be-claimed · unattached provider activity (still reachable) · transport with/without an itinerary anchor · Trip Details available while Plan authority is temporarily down · handoff to a domain owner (Stay). Concepts exist scattered across the package; the active target never renders the family. → Use **Bookings as the stress specimen**: populated / truly empty / source-degraded / unattached, plus one anchored-transport row. Don't duplicate Booking/Route domain behavior inside Trip Details.
19. **P1 — Linked-object continuity journey** *(companion D6, consolidation gap)*. Production preserves the originating structural event while the traveler traverses linked expense/stay/booking/history objects — including day, List/Map face, selection, scroll, and contextual return state. The event↔expense round trip exists only in folded/transitional sources; the active canon has abstract Back contracts but no rendered journey. → Migrate one golden path into the active canon: `Friday itinerary → dinner event → linked expense → Back to dinner → Back to Friday` — distinct objects, a quiet "connected to" relationship, same expense identity when entered from Costs, correct Back label at every level. No stacked sheets; full-screen depth with one-level Back.
20. **P1 — Trip Details "Replan destination or dates" entrance undesigned** *(companion D8)*. Shipped since 2026-07-16: a first-class Trip Details row handing the traveler to Vesper with a constrained instruction (smallest coherent change → one typed canonical Replan → returned to Itinerary review; chat never silently mutates the trip). Workflow Canon designs the Replan *operation*; the *entrance* has no specimen or copy contract. → Add the row + one handoff strip (`Trip Details → Vesper prepares typed Replan → Itinerary review`); make clear it's an operation entrance, not a ninth information domain, and Back from an abandoned handoff changes nothing.

---

## 2 · Money: Costs / Booking / Stay (1 P0 · 9 P1 · 4 P2)

1. **P0 — Masked-expense semantics.** Code enforces **masked = payer-covers-fully**: shares to others rejected (`expenses.py:187`), non-payers see a fully redacted "Hidden expense" (title, amount→0, shares emptied, receipt stripped), masked never enters the balance graph, booking-linked can't be masked. Canon's masked ExpenseDetail draws a *hidden group split* (real merchant, 3 participants, `••••` amounts) — a state the backend forbids — and the AddSheet toggle copy implies only the amount hides. → Redraw as payer-view + redacted non-payer view; fix copy.
2. **P1 — Recorded settlement payments + void.** Code: `settlement_payments` is the **sole source of cleared debt** (append-only, void marker as only correction); FE "Recorded payments" section with struck-through `VOIDED` rows + undo, record-payment confirm ("Record that you paid X…?"), trip-wide settle-up recorded as a real payment. Canon's balance sheet has Nudge/Settle/Review only; its `reimbursement` ledger row ("SETTLED IN CASH") is a mechanism the code never emits. → Add the Recorded Payments block + record/void moments; decide the reimbursement row's fate.
3. **P1 — Multi-currency truth.** Code: per-expense currency picker, server-converted `settlement_amount`, original-vs-converted display rule, sentinel-FX-rate warning ("the converted total shown in the trip balance may be off"). Canon is 100% `€` with no currency field. → Add currency select, dual-display rule, degraded-rate notice.
4. **P1 — Split types + validation.** Code: equal/exact/%/items chips with per-member shares; itemized/exact must sum; split-type immutable in Edit (display-only, with rationale). Canon: equal-split only; no Edit sheet at all. → Design split editor + sum-mismatch error + read-only-in-edit rule.
5. **P1 — Booking↔Costs provenance + cancelled-booking review.** Code: `ExpenseSource` enum (manual/booking_auto/booking_opt_in/receipt_scan/…); organizer-only opt-in "Share in Costs" CTA on confirmed bookings; ledger "BOOKING CANCELLED · REVIEW COST" marker + refund-reconciliation panel (Jul 15–16). Canon has no provenance and implies auto-filing. → Add provenance treatment + review states; align to opt-in.
6. **P1 — Receipt scan flow.** Code: photo→OCR→suggested total→**user must confirm** (model-guessed totals never split real money). Canon: passive photo/note field only. → Design the scan sub-flow with the confirm rule visible.
7. **P1 — Booking cancellation is a lifecycle** (Jul 15–17). Code: `cancellation_status` pending ("Do not submit another cancellation…") / `manual_action_required` (unverifiable provider outcome) / completed receipts; survives restart; BE ambiguous-resolution + operator queue + SLA. Canon: one cancel-confirm card + terminal `cancelled` chip. → Extend the state table with cancellation_pending/ambiguous/complete and their exact words.
8. **P1 — Vesper contacts the venue** (voice/message booking). Code: full attempt state machine (pending/dialing/in_progress/no_answer/failed/declined/confirmed + `manual_action_required` + stale-claim recovery "…may have reached the restaurant. Do not contact them again from Vesper", guarded retry-once). Canon's `manual` category = *you* call the venue; Vesper-initiated contact is absent. → New method family with its chips + do-not-double-contact language.
9. **P1 — Expense-dispute doctrine trails the durable lifecycle.** Canon draws disputed ledger/detail states, but production now defines the missing authority and transition truth: payer or assigned-share traveler opens; opener withdraws; payer or organizer resolves; one open dispute suspends the whole expense from settlement and blocks settle/delete; live payments must be voided first; no transition silently changes money; every transition leaves a shared trip-room receipt and exact expense deep link. → Keep the existing visual treatment, add the authority variants, written reason, resolution/withdrawal moments, payment precondition, and receipt-to-detail journey.
10. **P2 — Booking controller authority (viewer ≠ actor).** Non-assigned members see "The assigned traveler is reviewing this…"; session banner names controller authority; control transfers on departure. No canon variants.
11. **P2 — Held-price change:** decline-and-record + "Managed by your itinerary change" saga-owned holds — beyond canon's keep/find-cheaper.
12. **P1 — Stay "recorded, not booked".** Code: reservation-proof boundary (`stayBookingTruth.ts` — proof requires booking_confirmed source or reference; booker chip suppressed without proof; STATUS "Stay recorded · not booked"). Canon's 8-state StayCard jumps held→confirmed. → Add the recorded state + proof rule. (Stay otherwise notably current: vote blocking/holdout matches canon.)
13. **P2 — Non-equal "EACH OWES" suppression + `CONFIRMING SETTLEMENT`/`settling` in-flight states.**
14. **P2 — Canon self-inconsistency:** Costs FlowNotes still says Expense Detail is a sheet; the same file's 07-11 ruling (and code) made it a full-screen route. Also §consolidation claims the Settle face is "currency-aware" — not shown anywhere on the Costs page.

---

## 3 · Chat / Vesper Home / Voice / Search / Notifications (1 P0 · 4 P1 · 2 P2)

1. **P0 — Plan Build card promises a backend signal that doesn't exist.** Canon's flagship day-fill artboards are captioned `completed_day_numbers=[1,2] · next=3` under a board that vows "No artboard promises anything the event stream can't deliver" — but no SSE event carries day identity mid-run (`backend/planning_agent/status_labels.py` is iteration/tool-category only); the shipped card (`PlanBuildCard.tsx`) is a determinate step bar + tool line, no day rows; "Notify me" and "Finish without me" currently resolve identically. → Ratify step-bar v1; move day rows to a named blocked-on-backend follow-up; rule the two leave-postures.
2. **P1 — Group live-presence banner.** Shipped "{name} is asking Vesper…" observer banner (`GroupMemberAskingBanner.tsx`; Tier-0 poll name-only, Tier-1 editorialized tool line + ≤2-line trail; phases active/completed/background/failed/superseded; deliberately not typing-dots). Canon covers only the *landed* observer view. → Add the observer-presence state family to Chat Working States (anatomy, stacking vs GroupEventLine/narration band).
3. **P1 — Roster-uncertainty fail-closed gate.** Shipped full-screen "Couldn't verify trip members / Group chat stays closed until we can confirm who belongs to this trip" + intentionally blank inert frame pre-verification (`GroupChatRosterGate.tsx`, Jul 14). No canon state. → Add to the chat states board (copy register + color ruling + inert-frame spec).
4. **P1 — Markdown grammar in the thread.** Shipped native markdown runtime (`components/markdown/` — headings, links https-only, code, tables, quotes, streaming-safe, "Copy as Markdown") across all Vesper prose. Canon rules "serif prose, never a bubble" but has no per-element mapping, allowed/banned list, or streaming-partial rule. → A "markdown in the thread" board.
5. **P1 — TripShapes picker + planning continuation.** Shipped in-chat mode picker ("Sketch the backbone / Build it day by day / Draft the whole trip"), versioned day receipts ("Day 2 · v3"), "Build Day N" continuation actions, planner-refine Undo. Canon has PlanReadyReceipt modes but no TripShapes card, chip row, or continuation grammar. → Add to the cards canon as receipt-family members.
6. **P2 — Human-vs-AI delivery separation in group rooms** (Jul 14): member messages send without a Vesper placeholder/thinking line unless addressed; optimistic/sending/failed/retry states on member bubbles; "Retry Vesper reply" on failed AI turns. Canon implicitly treats every send as starting an AI turn. → Group-delivery board + the placeholder rule.
7. **P2 — Deck transactional phases** (`acting/reconciling/exiting/error/uncertain`, controls locked, "N TO CLEAR"): undesigned; 'uncertain' (write may have landed) needs honesty copy.
- *Notably current:* voice identity ruling, D25 receipts, near_you + currency-gauge deck faces (code cites canon by name); Universal Search FE routing ready while BE still emits `route=None` (code behind design).

---

## 4 · Atlas / Discover / Places / Post-trip (3 P0 · 7 P1 · 4 P2)

1. **P0 — Atlas alignment ledger inverted.** Canon's 07-12 open-decisions board still records "featured-reading hero killed — code still ships it" and "Reel deferred — code ships it live" as mismatches. Both closed Jul 12–14: place-first home is shipped and composition-authoritative (`atlas-place-first-home-contract`), Reel is disabled ("Reel — coming later"). → Mark both DONE, dated.
2. **P0 — Discover has a shipped trip-commitment path canon doesn't know.** Dream-shape lead carries a third CTA **"Plan a trip"** → plan-similar sheet ("Ask Vesper about X" / "Start a X trip") → `createTrip` instrumented `discover_durable_action: trip_started`. The "start-trip unreachable from Discover" era is over; canon's hero still has only Read on / Ask Vesper. → Draw the dream-shape hero + commitment sheet + suppression rule when a trip is already in context.
3. **P0 — Discover canon predates the gen-6 server-composed feed.** Shipped contract: `read` block + semantic `sections[]` (`debate|reads|places|friends`; layouts `hero|lead|rows|split`; first non-empty promoted; per-layout caps) + `rhythm` (interlude/punctuation) + `lead` + `meta` (`degraded_sources`, `personalization_status`); shapes `dream|dual|proximity|retrospective|briefing`; For you / Vesper / Friends emphasis pills. Canon still draws a hand-composed zone cover (and `CoverHome` still renders the `PillCarousel` its own B8 adjudication superseded). → Redraw the cover as the chapter grammar; swap in ScopeChips.
4. **P1 — Discover learning loop.** Five shipped telemetry events + durable actions (`save|ask|trip_intent|trip_started|map_open|not_interested`) that invalidate personalization cache. Canon has no notion of durable signal or where the not-interested affordance lives. → One "what Discover learns from" board.
5. **P1 — Atlas home composition rules.** Shipped: order hero→**attention**→places, an **editorial budget** (max 2 prominent modules across consequence/readings/timely-return/cold-teaching/whole-atlas/learning), consequence banner slot, mid-stack stale-notice, developing-scan slot, stage gates. Canon's locked order says places before attention (its own accumulating artboard disagrees) and lacks the budget + extra slots. → Fold the shipped eligibility model in; fix the order.
6. **P1 — "The whole Atlas" directory.** `/atlas/whole` is a shipped four-doorway directory (Places/History/Readings/Taste) between home entrance and Long View index; canon draws only the entrance row and the index. → Draw the directory; adjudicate entrance→directory vs entrance→index.
7. **P1 — Unified reading lifecycle vs undrawn fold.** Code shipped compose→board→Keep→`/atlas/readings`, kept-view re-open ("Ways Back In re-opens a kept board live"), latest-reading home row (matches canon's row exactly). Canon declared "Ways Back In folds into Readings" but never drew the merged surface — the superseded `WaysBackIn` component is still the only home of its five states. → Draw the single post-fold Readings surface.
8. **P1 — Memory Inbox narrowed.** Code deliberately ships a candidates-only review contract; canon's five-kind queue (candidate/pattern/cluster/ready/correction) presents the other four as canonical. → Annotate: candidates = shipped; rest = staged/gated.
9. **P1 — Post-trip Memory screen carries ungoverned modules.** The shipped spine matches canon impressively (five homecoming states verbatim), but Memory also embeds a full **debrief submission**, **Group & Learn consent sheet**, **photo-album intake**, and a Vesper-composed closing line — none placed by the canon's Memory threshold spec. → Extend the spec to place (or relocate) debrief/consent/photos; rule the closing line.
10. **P2 — Anniversaries accepted-history rule** (On This Day composes only from accepted memories + completed trips; push shares the same filters) is silent in canon — add the doctrine line.
11. **P1 — Saved system rulings missing from the matrix.** Resolvable-objects constraint (save removed from accommodation/guide/abstract targets), 3-stage Add-to-Trip (trip→**day**→receipt) with provenance, SavedIndex's shift to a neutral non-Atlas voice. Canon's control matrix + add-flow predate all three. → Rev the matrix + redraw add-to-trip.
12. **P2 — Discover Map pin taxonomy self-conflict** (§05 table says saved=sage fill; pin spec + code say saved=ring). Reconcile to ring.
13. **P2 — Atlas route tail** (shared-links index, removed-list, unpacked-card, scan, candidate detail; monogram → `/atlas/profile` vs canon's "Settings behind the monogram") — add a route appendix; adjudicate monogram.
14. **P2 — Your Memory:** shipped default for the learning toggle should close canon's OPEN item; add the capability-unavailable × user-toggled-on state.
- **Canon self-declared OPEN (Atlas):** Reel v1 · People/Theme facets · style-set names · Unpacked celebratory ceiling · render/riso v1 — several now have shipped de-facto answers; close rather than re-litigate.

---

## 5 · Group / People / Invite / Auth / Sharing / Trust (2 P0 · 5 P1 · 4 P2)

1. **P0 — External Sharing privacy doctrine is now factually false.** Canon: "Never externally shared: Group decisions, vote counts, or proposal content"; the 16-object share matrix has no proposal object. Code (Jul 14): unauthenticated **public proposal-share landing** (`proposal_landing.py` — title, description, aggregate tally, status; OG card `card.png`; unguessable id pair as bearer; voter identity never leaks). → Add "Proposal/decision share" as a 17th object with its projection rules; amend the doctrine list.
2. **P0 — Members hold the room-wide mute brake.** Code: non-organizer members can toggle `room_muted` (Jul 13; "members retain both mute brakes"); posture/threshold stays organizer-only. Canon's member sheet shows personal mute only. → Redraw member sheet with both mutes + the authority rule (mute = safety brake anyone can pull).
3. **P1 — Invitee Post-Join shipped from an "ACTIVE EXPLORATION — do not implement" page.** The whole payoff shipped (LLM `welcome_aside` + block asides, once-per-membership, "Take me to the open day →", `OPEN · YOURS TO SHAPE`, group-share attribute-at-accept with silent live-claim vs restore-claim "Still sound like you?"), matching the exploration boards almost line-for-line — but the page is still non-canon **and drawn on the retired Folio shell**. → Promote to CANON under Auth & Invite; redraw backdrop on the canonical itinerary shell; add the two shipped nuances (silent live claim; content-contract limits for the LLM asides).
4. **P1 — OG link-preview cards (invite + proposal).** Shipped 1080×1920 renderer with revocation-safe cache; no canon primitive anywhere. → Add a "Link-preview card" spec to External Sharing (per-object variants; no private data; revocation kills cache).
5. **Resolved 2026-07-20 — Member-initiated decision nudges belong to Review, not Changes.** The mixed-era Changes implementation (open-proposal query, Waiting-on row, vote buttons, deadline banner, and Nudge) was removed. Changes now renders settled operation history/recovery only. Keep proposal/stay-vote nudge states in the decision/Review grammar; settle-up nudges remain a Costs concern. Do not add them to the Changes canon.
6. **P1 — Deferred safety-chips catch.** Invited OTP signups used to skip safety capture forever; code added a durable deferred catch (flag → one-time sheet in trip chat). Canon's safety rules say "new user only — after first sign-up" and its invite path has no deferred beat. → Add the deferred-catch beat to the Auth & Invite flow map.
7. **P1 — Shared-plan owner succession** (see 1.8 — same campaign; Trip Settings canon needs the authority-transfer family).
8. **P2 — Membership rejoin history** (events preserved across leave→rejoin; add rejoin status + "Marco rejoined" event line).
9. **P2 — Membership-change consequence receipts** (proposals expired / booking control transferred because someone left — no reason-carrying states on expired/transferred objects).
10. **P2 — Masked-expense marker in the group seam** (privacy-seam board lacks the payer-covers-fully object state).
11. **P2 — Quiet-hours timezone honesty** — Trust canon renders a set timezone ("Lisbon") but onboarding never captures tz; specify device-tz default seeding + trip-tz override so the screen is honest.
- *Consistent (no action):* External Sharing's deferred objects (route-share, guide share, itinerary export) remain unbuilt as declared; story sharing built but flag-dark (add only a small owner-side "sharing is off" state for the dark period).

---

## 6 · Ranked design-iteration queue for Claude Design

| # | Session | Covers | Why first |
|---|---------|--------|-----------|
| 1 | **Canonical Object Inspection v2 + Workflow vocabulary mapping** (see 6a) | 1.16, 1.17, 1.14, 1.11, 1.18, 1.19, 1.20, 1.1, 1.2, 1.3, 1.4, 1.10 | The layer directly beneath the itinerary spine: one object-detail family with typed variation, plus a binding map from traveler-facing operation families to the normalized engine registry and the current ChangeStudio anatomy |
| 2 | **Discover cover redraw** | 4.2, 4.3, 4.4 | The wedge CTA + feed structure a designer would otherwise design against a dead model |
| 3 | **Monetization page (new)** | 0.1 | Entire commercial layer undesigned; required before broader activation |
| 4 | **Costs truth pass** | 2.1, 2.2, 2.3, 2.4, 2.6 | Money-truth: one active P0 (masked) + the payments/void system |
| 5 | **Booking lifecycle pass** | 2.7, 2.8, 2.9, 2.10, 1.6, 1.7 | Cancellation + Vesper-calls-venue + saga endings, one coherent trust-vocabulary session |
| 6 | **Chat reliability & multiplayer states** | 3.1–3.7, 0.3, 0.4 | The 07-11→07-16 reliability wave; mostly additive state boards |
| 7 | **Group authority & settings truth** | 5.1–5.7, 1.8, 1.5, 1.9, 1.12 | Two doctrine corrections, the succession/atomic-departure family, the Changes-screen model split, the date-shift preview, and promoting Invitee Post-Join to canon |
| 8 | **Atlas ledger & composition sync** | 4.1, 4.5–4.9, 4.11 | Mostly annotation/fold-drawing; doctrine already aligned |
| 9 | **Governance sweep** | 0.2, 0.5, 1.10, §06 self-claim, route appendix | Cheap, prevents the next agent from implementing from stale scaffolding |

### 6a · Session 1 brief — Canonical Object Inspection v2 (adopted from the companion audit, extended)

Stay inside the existing Trip visual language; preserve the frozen header, Details entrance, and List/Map toggle. Canvas = one section, seven related boards — not every condition on one phone:

- **A · Foundation anatomy** — the definitive **ordinary-event** detail screen (reference anatomy for all typed variants): frozen Level Header · status + contextual note · date/time/place · traveler-facing Plan Truth · primary action · restrained More Actions · participation · Needs Attention only when real · Connected Facts · History entrance · human-readable provenance, never a raw-ID footer (§0.6).
- **B · State strip** — four variants of the same foundation: sources limited · facts unavailable · cancelled/locked · occurrence-correction available (1.14).
- **C · Typed divergences** — the three types that genuinely need different anatomy: expense · provider booking with partial outcome · **history record** (1.11). Stay/transport/place ride in the component matrix unless an owner page needs a handoff specimen.
- **D · Context & domain truth** — the event↔expense round-trip journey (1.19) · Bookings domain populated/empty/degraded/unattached (1.18) · the Trip Details Replan entrance + handoff strip (1.20).
- **E · Governance + vocabulary repair** — expand the ObjectDetail component API past `booking | flight`; add a binding map from the traveler-facing operation families to the shipped 14-type normalized registry; add attendance/occurrence/recovery as visible capability families; retain plain-language Split/Rejoin while mapping it to create/update/dissolve-parallel operations; remove the false "skipped" state and align ChangeStudio anatomy (1.1, 1.2, 1.4); extend Workflow §E with the post-landing parallel-branch lifecycle (1.3); refresh the coverage matrix + §18 + "no open visual-pass items" (1.10).

**Acceptance criteria** (condensed from the companion audit; the full list lives there): ordinary event has a definitive target · all seven object kinds acknowledged with shared anatomy + explicit divergence · partial data visually distinct from true absence · authority-unavailable distinct from loading and empty · cancelled/denied objects stay inspectable without misleading Change · personal/factual correction independent of structural editability · plan/provider/cost truth never collapsed into one status · expense can't inherit structural Change · provider continuation can't read as Undo · History Record consumes (not redefines) Workflow recovery doctrine · Back restores the correct level and originating context · no raw IDs/confidence/reason-codes in target UI · header and spine unchanged · coverage boards tell the truth.

### 6b · Settled — do not reopen (verified exclusions carried over from the companion audit)

These held up under verification; don't spend design sessions here: **header & Trip entrance chrome** (frozen; preserve) · **the central itinerary spine** (canon is *ahead* of production here) · **the core typed-operation doctrine and already-rendered Workflow journeys** (consume them; update the family↔engine mapping and current ChangeStudio application rather than inventing a second operation system) · **Story/Memory/sharing composition + share lifecycle** (covered; only the §4.9 module-placement and §5 flag-dark-state additions remain) · **people rosters & member action sheets** (covered — but the distinct *shared-plan succession/atomic-departure* slice is not; it stays in session 7) · **typography/tokens/row/button systems** (apply, don't fork) · **trip-entry waiting screen** (no visible production state to match; future polish, not parity).

## 7 · Code-behind-design (for completeness — NOT design debt)
Home Flight/Comparison faces await grounded producers · voice takeover remains flag-dark (residual `Vesper · {city}` subtitle on reopening) · live in-app checkout is gated dark · richer Replan delta and initial parallel-plan construction remain. Trip-creation row-level correction and heterogeneous Discover pins are now implemented.

---

*Method note: five parallel domain audits, each reading canon JSX sources (the HTML pages are shells) and verifying against actual code + git history through 2026-07-17; cross-cutting route diff (62 canon-mapped routes vs shipped Expo Router tree) and a Jul 15–17 commit sweep done separately. No prior investigation docs were consulted during the original investigation. On 2026-07-17 the independent companion audit `~/Documents/Claude/Travel Workspace/docs/vesper-220-design-behind-audit.md` (Trip/Itinerary object-inspection deep dive; source-level, test-verified — 4 suites / 37 tests at `9ec97d63`; adversarially revalidated) was folded into §0.6, §1 (findings 1.10, 1.11, 1.14, 1.16–1.20), §6a, and §6b. Overlapping scopes were adjudicated: the Workflow operation doctrine remains valid while its family↔engine mapping and ChangeStudio application trail production; People & Collaboration covers rosters/member actions while shared-plan succession belongs to a distinct Trip Settings slice. The companion's D8 (Replan entrance) plus the engineering-artifact doctrine were additions this audit had missed. That standalone doc remains the home of the full acceptance-criteria list and evidence matrix for session 1; this doc is the cross-domain superset and planning authority.*
