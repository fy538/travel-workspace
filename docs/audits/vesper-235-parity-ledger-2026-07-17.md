---
doc_type: working
status: active
owner: founder / design / engineering
created: 2026-07-17
last_verified: 2026-07-17
expires: 2026-08-16
why_new: Converts the verified Vesper 235 investigation into one bounded cross-design and implementation closure ledger.
supersedes: []
source_of_truth_for: [vesper-235-parity-closure-ledger]
---

# Vesper Design ↔ Code Parity Ledger

> Opened: 2026-07-17
> Source audit: `vesper-235-design-gap-investigation-2026-07-17.md`
> Purpose: track every verified gap from evidence through design decision, implementation, validation, and retirement.

## Status model

- `OPEN` — verified gap; work has not started.
- `DESIGNING` — being resolved in the design canon.
- `DESIGN VALIDATED` — the design source covers the required states and has been checked against code.
- `IMPLEMENTING` — code work is active.
- `PARITY VALIDATED` — design, source, routes, permissions, and recovery behavior agree.
- `RETIRED` — superseded design/code has been removed after parity validation.
- `PARKED` — explicitly out of scope or flag-dark, with an owner and re-entry condition.

No row can move directly from `OPEN` to `PARITY VALIDATED`. A visual specimen alone does not close a row.

## Global acceptance gates

Every applicable row must demonstrate:

1. Canonical owner and entrance route.
2. Happy, empty, loading, unavailable, failure, retry, and recovery states.
3. Actor, viewer, organizer, controller, and affected-member permissions where relevant.
4. Durable truth: what was requested, what actually happened, and what remains uncertain.
5. Human-readable notification and receipt language.
6. Exact-return behavior after sheets, detail views, and external/authentication handoffs.
7. Dynamic Type, VoiceOver, contrast, minimum target size, and reduced-motion behavior.
8. Source-level verification and focused regression tests.
9. Explicit keep, redirect, archive, or delete ruling for superseded surfaces.

The current Trip header is frozen. This program must not redesign it. “Folio” is retired vocabulary.

## Round 1 — money and public truth

| ID | Finding | Required outcome | Validation evidence | Status |
|---|---|---|---|---|
| M01 | Cancellation reconciliation | Separate requesting, processing/refreshing, pending verification, cancelled, not cancelled, and manual action required; prevent duplicate submission | State mapping against internal and client projections; transition tests | DESIGNING |
| M02 | Cancellation completion receipt | Canonical replay-safe receipt anatomy for success, not-cancelled, and escalation | Notification payload mapping and replay test | DESIGNING |
| M03 | Cancelled booking → Costs review | Booking receipt links to a paused-settlement expense review without implying final settlement | Booking/Costs navigation and settlement exclusion test | DESIGNING |
| M04 | Participant consent ledger | Pending, approved, declined, excluded, reminder cooldown, narrow-to-self, and confirmation blocking | Per-participant state fixture and permission test | DESIGNING |
| M05 | Booking controller/viewer | Controller owns provider mutations; other travelers see attribution and view-only outcomes | Role matrix and action-visibility test | DESIGNING |
| M06 | Expense review governance | Eligible opener, opener-only withdrawal, payer/organizer resolution, payment-void prerequisite, paused settlement | Expense-review permission and settlement tests | DESIGNING |
| M07 | Recorded payments and void | Visible recorded/voided ledger rows and restricted void action | Ledger fixture and void permission tests | DESIGNING |
| M08 | Currency truth | One settlement currency; unsupported conversions excluded; estimated rates labeled | Mixed-currency fixture | DESIGNING |
| M09 | Masked expenses | Protect payer identity/amounts while preserving valid split and booking constraints | Payer/non-payer visibility matrix | DESIGNING |
| M10 | Split-type immutability | Existing split type remains display-only during edit; language derives from actual shares | Expense-edit fixtures | DESIGNING |
| M11 | Archived-trip booking closure | Define booking actions and receipts before archive, while archived, and after recovery | Archive/recover navigation and mutation tests | DESIGNING |
| M12 | Receipt/OCR scan states | Complete confirm-before-add loading, unreadable, partial, retry, and correction states | Scan fixtures and accessibility pass | OPEN |
| S01 | Public proposal privacy contradiction | Public proposal output exposes no vote counts or vote-derived decision status; authentication is required for group decision detail | Anonymous route/card inspection and privacy test | DESIGNING |
| S02 | Four public card projections | Exact allowed/redacted fields for Story, Invite, Proposal, and Unpacked 9:16 cards | Projection table mapped to renderer payloads | DESIGNING |

## Round 2 — itinerary grammar

| ID | Finding | Required outcome | Validation evidence | Status |
|---|---|---|---|---|
| I01 | Fourteen-operation coverage | Matrix for all 14 types covering entrance, preview, authority, execution, receipt, provider effect, failure, and recovery | Exhaustive enum-to-canon assertion | OPEN |
| I02 | Move contradiction | Anchor-relative Before/After is canonical; reorder is separate; time selection appears only for a real time conflict | Move/reorder fixtures and source mapping | OPEN |
| I03 | Parallel-plan lifecycle | Create, update, dissolve, branch-stop cancellation, absorption/restoration, split origin, topology owner, and decision owner | Parallel lifecycle fixtures | OPEN |
| I04 | Reversal modes | Exact/non-exact reversal, lineage, stale review, compound inverse, tombstone/successor, and three recovery modes | Recovery capability fixtures | OPEN |
| I05 | Observed reality | Attendance, occurrence, plan correction, and provider correction with provenance, confidence, visibility, supersession, and receipt | Writeback and visibility fixtures | OPEN |
| I06 | Provider saga continuation | Pending, retry, partial success, held-price approval/decline, expiry, continuation verb, and manual action required | Provider continuation fixtures | OPEN |
| I07 | Authority taxonomy | Meaningful/broad/protected/provider reasons and organizer/affected-member/voluntary proposal rules | Confirmation-reason and proposal-policy table | OPEN |
| I08 | Now Mode | Active, between, and day-complete modes with Walk me there, Running late, and Mark done | Now-mode intent fixtures | OPEN |
| I09 | Shape/replan entrances | Accepted shape → itinerary and Trip Details → destination/date replan have owned landing and return contracts | Deep-link and exact-return tests | OPEN |
| I10 | Decision grammar | One approval vocabulary across Chat, Changes, Proposal Detail, and Stay | Cross-surface copy/state matrix | OPEN |
| I11 | Receipt editorial dictionary | Replace mechanical underscore conversion with approved operation, authority, recovery, and provider copy | Code-to-copy snapshot table | OPEN |
| I12 | Hybrid/legacy plan ownership | Decide keep/fold/remove for DomainIndex handoffs, hybrid plan bands, and incomplete landing edge rules | Route/surface ownership audit | OPEN |

## Round 3 — reliability and authority

| ID | Finding | Required outcome | Validation evidence | Status |
|---|---|---|---|---|
| R01 | Deck transaction lifecycle | Acting, reconciling, exiting, error, uncertain, committed, and superseded with input shielding | Transaction reducer fixtures | OPEN |
| R02 | Chat delivery lifecycle | All 11 phases and six failure classes, with turn-versus-screen ownership | Phase/failure mapping assertion | OPEN |
| R03 | Fail-closed roster authority | Loading, unavailable, solo, and group; unverifiable shared room never mounts | Roster-state tests | OPEN |
| R04 | Observer privacy | Room-level presence may expose activity but never another traveler’s reply prose | Observer SSE payload/UI test | OPEN |
| R05 | Split and repaired arrival | Human-message success versus AI-turn failure, late repair seam, and explicit retry ownership | Transcript reconciliation tests | OPEN |
| R06 | Attachment mapping | Map all 15 runtime attachment types to canonical card families and lifecycle behavior | Registry-to-canon assertion | OPEN |
| R07 | Markdown/streaming typography | Canonical partial-syntax repair and readable native markdown treatment | Streaming fixtures and Dynamic Type pass | OPEN |
| R08 | Narration extension | Preserve existing NarrationCard; add depth, feedback, lazy audio, and style/depth rules | Narration fixture matrix | OPEN |
| R09 | Home cold/stale truth | Hero skeleton and visible stale-verdict behavior for restored data up to 12 hours old | Cache-age fixtures | OPEN |
| R10 | Restored queued turn | Explicit Send now action without violating concurrent-send rules | Restoration/concurrency test | OPEN |
| R11 | Voice exploration hygiene | Quiet/Whisper and deleted Deck faces are clearly archived or superseded | Design-source search | OPEN |
| A01 | Succession consequences | Organizer, shared-plan owner, booking controller, proposals, balances, preflight blockers, and atomic handoff-and-leave | Role/departure transaction tests | OPEN |

## Round 4 — governance and secondary surfaces

| ID | Finding | Required outcome | Validation evidence | Status |
|---|---|---|---|---|
| G01 | Route governance | Correct 62-row claim, add 15 absent route files, remove phantom `/atlas/receipt`, rule on two history/log routes | Automated route-table diff | OPEN |
| G02 | Component ownership | Assign or retire StateTransition, ProgressGate, Tap, VesperDiagnosis, NavPills, DismissButton, ScreenScaffold, CardActionPill, CardStatusLabel, QueuedTurnTray, and CardLift | Component registry/design-source diff | OPEN |
| G03 | Canon Index freshness | Close already-resolved items and reissue itinerary parity after the July 16 cutover | Index-to-ledger review | OPEN |
| G04 | Facts-Only governance | Distinguish implemented wrapper substrate from flag-controlled enforcement | Flag/config/source audit | OPEN |
| G05 | Content-contract truth | Separate implemented fixes from log-only and dark-mode enforcement | Rule-by-rule enforcement audit | OPEN |
| G06 | Notification routing | Enumerate every intent, destination, fallback, and inbox section | Intent-to-route assertion | OPEN |
| G07 | Search destinations | Give `site` and `accommodation` valid frontend destinations or stop indexing them | Search-result routing tests | OPEN |
| T01 | Atlas home map | Remove the deleted-endpoint implication or define an explicitly local/decorative projection | Design doctrine and API search | OPEN |
| T02 | Reading archive semantics | Remove archived/re-addable if not being built, or implement a real Reading archive state | Kept-board behavior test | OPEN |
| T03 | Memory rendering contradiction | Reconcile live render toggle, “coming later,” and gated runtime capability | Design-source and flag review | OPEN |
| T04 | Invitee Post-Join | Graduate exploration status and point it at the current Trip plan surface | Route/content review | OPEN |
| T05 | Discover cover | Own Plan a trip, five read shapes, IssueFloor, and updating state | Runtime shape fixtures | OPEN |
| T06 | Invite substance gate | Organizer-facing trip-needs-substance, quota failure, and concierge recovery | Invite failure fixtures | OPEN |

## Code queue

These rows do not need new visual invention before implementation unless the named ruling is reopened.

| ID | Code work | Dependency | Validation evidence | Status |
|---|---|---|---|---|
| C01 | Install native LiveKit connector at app startup | Existing voice canon | Real/mock startup and failure tests | OPEN |
| C02 | Remove ten city personas or approve a narration-only exception | Singular-Vesper ruling | Persona/config search and narration test | OPEN |
| C03 | Reconcile ElevenLabs configuration with Cartesia guide narration | Provider ruling | Environment/config/provider integration test | OPEN |
| C04 | Build the Chat thinking ladder | Existing Working States | Duration/state transition tests | OPEN |
| C05 | Add day identity to Plan Build progress | Existing Plan Build design | Event schema and per-day fill test | OPEN |
| C06 | Complete Document mode and conversation-create doorway | Existing Document design | Creation, naming, takeover, and return tests | OPEN |
| C07 | Remove Trips Home create FAB if the A8 ruling remains canonical | A8 confirmation | Source search and UI test | OPEN |
| C08 | Finish archived-trip recovery UI and decide Reuse as template | M11 and recovery audit | Archive/recover/reuse tests | OPEN |
| C09 | Classify gated Atlas/Discover/Story loops | Product flag decisions | Flag registry with owner and exit condition | OPEN |

## Retirement gate

Retirement happens only after the replacement route and state coverage are verified. The final pass must search for:

- retired Folio vocabulary and routes;
- duplicate itinerary readers or writers;
- obsolete Move time-picker doctrine;
- vote-derived public proposal status;
- stale Atlas map endpoint assumptions;
- orphaned Deck faces and voice personas;
- phantom or undocumented routes;
- local action controls that duplicate canonical primitives;
- flags without an owner, exit condition, or production posture.

## Execution checkpoint

- Current phase: Round 1 design work.
- Current batch: M01–M05 and S01–S02.
- First design return: inspected against all three prompts and current source; **not yet validated**.
- Second design return: several source-truth corrections landed, but integration, component reuse, and internal consistency remain open; **no row promoted**.
- Third design return: ownership and runtime labels improved, but the surgical prompt was only partially executed; **no row promoted**.
- Fourth design return: cancellation micro-pass landed most required behavior; a small literal-consistency cleanup remains before cancellation rows can advance.
- Next gate: close the cancellation residue, then run consent and public/governance micro-passes.

## Round 1 validation — first design return

### Prompt 1: Booking Cancellation Truth — PARTIAL

What landed correctly:

- One cross-surface canvas covers request, pending verification, duplicate prevention, terminal outcomes, receipts, Costs review, role notes, accessibility, and a state matrix.
- Request truth is usually distinct from provider outcome.
- The confirmed-cancellation receipt links to the exact Costs item and preserves last-checked/controller/changed/unchanged anatomy.
- Recorded/voided payment, estimated currency, masking, split, and archive specimens were added without redesigning the entire Costs system.

Required corrections before design validation:

1. Remove **Keep the booking instead** after a cancellation has been submitted. Current source has no cancellation-of-cancellation action.
2. `manual_action_required` is not a provider-terminal cancellation outcome. Replace **I’ve cancelled it** and the automatic retry affordance with the currently supported truth: inspect provider records/contact support while Vesper remains unable to verify the outcome. Only the operator evidence workflow can close the durable claim today.
3. Expense review withdrawal belongs only to the traveler who opened the review. Payer/organizer resolution does not grant withdrawal. Split the buttons and role copy accordingly.
4. Archived trips do not simply close cancellation review. They remain read-only for forward booking work, but liability-reducing or truth-verifying recovery—cancellation, reconciliation, and hold release—remains allowed.
5. Split type is display-only for expense edit generally, not only while cost review is active.
6. Masked-expense copy must state that non-payer amounts/details are hidden and that masked expenses cannot allocate shares to other travelers; “amount owner” is not a canonical concept.
7. Replace local `Working`, `StaleLine`, and `FailInline` mirrors with the actual canonical State System primitives or explicitly register a justified wrapper. The prompt prohibited independent reimplementations.
8. Add a bounded refresh/network-failure specimen distinct from provider `manual_action_required`.
9. Receipt/cost-review actions must state opener, resolver, and controller separately; the current matrix conflates them.

### Prompt 2: Public Projection Contract — PARTIAL

What landed correctly:

- One canvas establishes the no-public-votes ruling and a four-type Story/Invite/Proposal/Unpacked matrix.
- The proposal specimen removes vote counts, voter identity, quorum, standing, and vote-derived status.
- The four cards reuse the existing 9:16 grammar, and metadata/alt-text privacy is explicit.
- Loading, unavailable, expiry-scoped, revoked, removed, authentication, render-failure, and stale specimens exist.

Required corrections before design validation:

1. Integrate the new contract into the existing External Sharing canon. It still says all proposal content/group decisions are not public, while the new canvas allows neutral proposal context. One rule must win and the owner page must point to it.
2. Reconcile reason disclosure. Existing External Sharing requires generic unavailable copy for untrusted viewers; the new canvas exposes exact **expired**, **revoked**, and **removed** reasons publicly. Exact reasons should remain owner/trusted-only unless the prior privacy doctrine is deliberately overturned.
3. Do not label Story and Unpacked public output simply **SUPPORTED today** while their mint/share paths remain flag-dark. Distinguish design-approved, runtime-gated, authenticated-only, and blocked-by-code states.
4. Mark actor-set Story expiry, actor-controlled Invite fields/max uses, proposal public enablement, Unpacked field selection, cache behavior, revocation, and destination mapping `CODE AUDIT REQUIRED` where runtime support was not established.
5. The proposal row currently says both gated and unsupported. Use one precise posture: design-approved context-only, but runtime-blocked until server-side redaction/gating is verified.
6. Add Dynamic Type, VoiceOver/alt-text order, focus, target-size, and reduced-motion annotations for public landing states.

### Prompt 3: Booking Consent & Control — PARTIAL

What landed correctly:

- One canvas covers all four durable consent states, controller/viewer variants, receipts, edge states, two matrices, and accessibility.
- The four-hour reminder cooldown is represented as text rather than fake progress.
- Controller actions are removed from viewer specimens rather than rendered as dead controls.
- The self-only recovery specimen exists and preserves other travelers’ declines.

Required corrections before design validation:

1. Current code permits **only the booking controller/requester** to remind a pending participant. Remove organizer reminder authority unless implementation is intentionally changed later.
2. Current code permits only `narrow_booking_to_controller`: the controller can narrow the entire session to themselves. Remove **Narrow to 3**, “narrow to fewer,” and any role-matrix capability implying arbitrary subsets.
3. The mixed example is internally false: two people are approved, one is pending, and one declined, yet the copy calls three travelers “in.” Fix the summary and available recovery.
4. Approved consent cannot currently “withdraw to pending.” A new response writes approved or declined. Use the supported transition or mark a pending-withdrawal feature as code work.
5. Excluded is immutable within the current booking session. Rejoining the trip does not automatically re-include that traveler; a new booking scope/session is required unless code changes.
6. Mark controller-unreachable handoff, traveler-removal projection, stale-consent confirmation holding, and paused consent edits during provider action `CODE AUDIT REQUIRED`. Several are plausible doctrine but were presented as shipped guarantees without source proof.
7. Replace the local `ConChip`, `Av`, and `ConRow` family with canonical TravelerPicker/row/status primitives. The source claims reuse while implementing a new picker-like row and approval chip.
8. Fix the specimen implementation so `chipTone` actually reaches the status component; it is currently accepted by `BHead` but ignored.
9. Role matrices must allow role overlap without implying that organizer/controller roles suppress a traveler’s right to answer for themselves.

### Design-bundle governance

The project consistency audit currently fails:

- Four top-level HTML pages are unindexed, including all three new Round 1 canvases and the pre-existing Itinerary Redesign page.
- Meaningful text uses decorative/muted tokens in three new Round 1 locations and numerous pre-existing locations.
- The three Round 1 canvases are not registered in the Canon Index or the consolidation ownership map.
- The audit reports shared-primitive reimplementation warnings, consistent with the local state and consent helpers identified above.

Round 1 remains `DESIGNING`; no M01–M11 or S01–S02 row is promoted to `DESIGN VALIDATED` yet.

## Round 1 validation — second design return

### Corrections that landed

- Cancellation no longer offers to undo an already-submitted request.
- Manual cancellation now warns against resubmission and offers provider-record/support paths.
- Masked-expense, split-type, and archived-trip copy moved materially closer to source truth.
- Public unavailable states now distinguish generic untrusted copy from exact trusted/owner reasons.
- Consent reminders are controller-only; arbitrary “narrow to 3” became self-only; the mixed ledger count and consent-state transitions were corrected.
- All three new pages were added to the Canon Index, and the Booking/External Sharing index rows point toward them.

### Blocking issues still open

#### Booking Cancellation Truth

1. The canvas still calls **Finish by phone** a third terminal outcome in comments, subtitles, accessibility notes, artboard labels, and the “All terminal receipts” board. Manual verification is durable but unresolved; only Cancelled and Still booked are verified provider outcomes.
2. The locally recreated `Working`, `StaleLine`, and `FailInline` helpers remain. Canonical State System primitives were not consumed.
3. Refresh failure was added only as a matrix row; no rendered specimen exists.
4. The Costs specimen still renders Resolve and Withdraw together, does not identify the opener, and the matrix still grants “resolve · withdraw” to payer/organizer. A note beneath the wrong controls does not correct the interaction.
5. Controller/viewer copy still says the controller may resolve or withdraw if payer/organizer and may “complete” a manual cancellation.
6. Split-type copy now invents a separate change action. Current edit truth is simply display-only; do not imply another action unless it is designed and implemented.
7. A new meaningful note uses the decorative `muteSoft` token, increasing rather than eliminating the Round 1 token violations.

#### Public Projection Contract

1. Only the new projection file and the Index changed. The existing External Sharing source still says proposal content/group decisions are wholly non-public; the neutral-context distinction was not integrated into its object and route matrices.
2. Runtime postures remain stale: Story and Unpacked still say `SUPPORTED`, and the proposal row still says both `GATED · CONTEXT ONLY` and unsupported.
3. Implementation-dependent actor controls, expiry, caching, revocation, and destinations remain presented without the requested `CODE AUDIT REQUIRED` labels.
4. Dynamic Type, VoiceOver/focus, target-size, and reduced-motion annotations were not added.

#### Booking Consent & Control

1. `ConChip`, `Av`, and `ConRow` remain independent local primitives; TravelerPicker/row/status primitives were not adopted.
2. `chipTone` now reaches the receipt container but still does not reach the status chip itself.
3. The mixed ledger exposes **Book for myself** while presenting Theo as controller and “You” as a different participant. The actor perspective is inconsistent; only the controller may invoke that action.
4. Unverified edge states remain asserted as shipped truth. Only controller-unavailable handoff is marked `CODE AUDIT REQUIRED`; traveler removal, concurrent consent revalidation, and paused consent edits remain unqualified.
5. The role matrix still treats roles as mutually exclusive for self-consent instead of representing role overlap.

#### Governance and source integrity

The consistency audit now reports **three hard-failure categories and one warning category**:

- one unindexed page remains: Itinerary Redesign;
- all three new indexed pages are ungoverned because the consolidation ownership map was not updated;
- decorative-token failures increased from 39 to 40, with four Round 1 violations;
- shared-primitive reimplementation warnings remain.

The Canon Index edit is also malformed HTML: it contains an extra closing table row after Booking Consent & Control and drops the opening row/name cell for Photo & Media Intake. This must be repaired before the index is trustworthy.

Round 1 remains `DESIGNING`; the second return improves truthfulness but does not close any ledger row independently.

## Round 1 validation — third design return

### Changes that landed

- Manual escalation receipt now says **Verification needed / Provider outcome unverified**.
- The receipt board is correctly renamed **Outcome & Escalation Receipts**.
- Public runtime labels now distinguish design-approved/runtime-gated, token-gated, blocked-by-code, and authenticated-only.
- The Photo & Media Intake opening row/name cell was restored.
- All three Round 1 canvases were registered in the consolidation ownership map; the ungoverned-page audit is now clear.

### Surgical prompt items that were skipped or remain contradictory

#### Booking Cancellation Truth

- The file still labels manual action as terminal in its section comment, terminal screen caption, accessibility rule, lifecycle subtitle, and artboard label.
- Local `Working`, `StaleLine`, and `FailInline` mirrors remain unchanged.
- Refresh failure remains matrix-only; no specimen was added.
- Resolve and Withdraw still render together without an opener identity, and both role matrices still grant incorrect withdrawal authority.
- Controller/viewer copy still says a controller may complete a manual cancellation.
- Split-type copy still implies a separate change action.
- Both Round 1 decorative-token violations remain.

#### Public Projection Contract and External Sharing

- The existing External Sharing source was not modified. Its object/route matrices still conflict with the neutral proposal-context ruling.
- The requested accessibility board was not added.
- The decision block improved, but the field-level matrix still presents several implementation-dependent controls without local audit labels.

#### Booking Consent & Control

The consent source did not change at all in this return. Every blocker from the second validation remains:

- custom `ConChip`, `Av`, and `ConRow` primitives;
- tone not applied to the status chip;
- incoherent controller/current-actor perspective in the mixed ledger;
- unqualified traveler-removal, concurrent-consent, and edit-pause guarantees;
- mutually exclusive role matrix;
- two Round 1 decorative-token violations.

#### Governance

- Itinerary Redesign remains the sole unindexed top-level page.
- The Canon Index still contains the extra closing table row after Booking Consent & Control; structural validation reports an unexpected `</tr>`.
- The consistency audit now reports **two hard-failure categories**—unindexed page and decorative meaningful text—plus the shared-primitive warning category.
- All 40 decorative-token findings remain, including four introduced by Round 1.

Round 1 remains `DESIGNING`. The third return closes the ownership-registration subtask but does not independently satisfy any product ledger row’s full validation evidence.

## Round 1 validation — fourth design return (cancellation micro-pass)

### Materially corrected

- Two verified outcomes are rendered separately from the durable unresolved verification-needed state.
- The manual receipt is an escalation receipt, not a false success receipt.
- A full refresh/network-failure specimen now preserves prior truth and makes retry read-only.
- Costs review identifies the opener and renders opener, manager, and viewer capabilities separately.
- Booking control is explicitly separated from Costs withdrawal/resolution authority.
- Split type is presented as display-only without a named alternate flow.
- The new permission note no longer uses a decorative token; total decorative findings fell from 40 to 39.
- A validation board records the intended cancellation truth.

### Small blockers still present

1. The lifecycle section subtitle still says: **“Only three terminal outcomes are truth: cancelled · not cancelled · finish by phone.”** This directly contradicts the corrected boards.
2. The manual artboard label remains **“Manual action required · retry.”** It must say **“Verification needed · unresolved”** or equivalent.
3. The accessibility recovery row still says **“Try again re-requests only when safe.”** In this canvas, retry must mean read provider status only; a new cancellation is a later explicit workflow after verified Still booked truth, not an inline retry.
4. The verified-outcomes section says each state ends with a single valid next action, while the unresolved specimen intentionally exposes several bounded verification/support paths. Adjust the section doctrine rather than deleting valid support paths.
5. One Round 1 decorative-token violation remains in the controller/viewer capability board: meaningful unavailable-capability markers use `muteSoft`.
6. State System inspection shows that WorkerProgress, StaleNotice, and ActionFailureInline are documented prototype patterns, not exported reusable JSX components. Annotated local render adapters are therefore acceptable in this design medium, but all three helper comments should say **noncanonical prototype adapter · owned by State System**, not “mirror,” so they cannot be mistaken for new component ownership.

Cancellation is close, but M01–M03 and M06–M11 remain `DESIGNING` until these internal contradictions are removed and the relevant source mappings are rechecked.
