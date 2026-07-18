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
| M01 | Cancellation reconciliation | Separate requesting, processing/refreshing, pending verification, cancelled, not cancelled, and manual action required; prevent duplicate submission | State mapping against internal and client projections; transition tests | DESIGN VALIDATED |
| M02 | Cancellation completion receipt | Canonical replay-safe receipt anatomy for success, not-cancelled, and escalation | Notification payload mapping and replay test | DESIGN VALIDATED |
| M03 | Cancelled booking → Costs review | Booking receipt links to a paused-settlement expense review without implying final settlement | Booking/Costs navigation and settlement exclusion test | DESIGN VALIDATED |
| M04 | Participant consent ledger | Pending, approved, declined, excluded, reminder cooldown, narrow-to-self, and confirmation blocking | Per-participant state fixture and permission test | DESIGN VALIDATED |
| M05 | Booking controller/viewer | Controller owns provider mutations; other travelers see attribution and view-only outcomes | Role matrix and action-visibility test | DESIGN VALIDATED |
| M06 | Expense review governance | Eligible opener, opener-only withdrawal, payer/organizer resolution, payment-void prerequisite, paused settlement | Expense-review permission and settlement tests | DESIGN VALIDATED |
| M07 | Recorded payments and void | Visible recorded/voided ledger rows and restricted void action | Ledger fixture and void permission tests | DESIGNING |
| M08 | Currency truth | One settlement currency; unsupported conversions excluded; estimated rates labeled | Mixed-currency fixture | DESIGN VALIDATED |
| M09 | Masked expenses | Hide amount/details from non-payers while preserving payer attribution, payer-only cost, settlement exclusion, and booking constraints | Payer/non-payer visibility matrix | DESIGN VALIDATED |
| M10 | Split-type immutability | Existing split type remains display-only during edit; language derives from actual shares | Expense-edit fixtures | DESIGN VALIDATED |
| M11 | Archived-trip booking closure | Define booking actions and receipts before archive, while archived, and after recovery | Archive/recover navigation and mutation tests | DESIGNING |
| M12 | Receipt/OCR scan states | Complete confirm-before-add loading, unreadable, partial, retry, and correction states | Scan fixtures and accessibility pass | OPEN |
| S01 | Public proposal privacy contradiction | Public proposal output exposes no vote counts or vote-derived decision status; authentication is required for group decision detail | Anonymous route/card inspection and privacy test | DESIGN VALIDATED |
| S02 | Four public card projections | Exact allowed/redacted fields for Story, Invite, Proposal, and Unpacked 9:16 cards | Projection table mapped to renderer payloads | DESIGN VALIDATED |

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
- Fifth design return: cancellation source checks passed; M01, M02, M03, and M06 promoted to `DESIGN VALIDATED`.
- Sixth design return: consent micro-pass fixed actor perspective and audit labels but skipped status/ownership work and introduced a contradictory role row; M04/M05 remain `DESIGNING`.
- Seventh design return: consent ownership notes and overlapping-role logic landed, but visible status-tone propagation, accessibility completion, and the validation board are still absent; M04/M05 remain `DESIGNING`.
- Eighth design return: visible status tones and a validation board landed, but matrix overflow contradicts the new accessibility claim, three accessibility rows are duplicated, and the validation board omits the unchanged-scope check; M04/M05 remain `DESIGNING`.
- Ninth design return: final consent source checks passed; M04 and M05 promoted to `DESIGN VALIDATED`.
- Tenth design return: exported project is byte-for-byte identical to the ninth return; the handoff identifies Booking Consent & Control as the active page, so the requested External Sharing/Public Projection governance pass was not executed. S01/S02 remain `DESIGNING`.
- Eleventh design return: External Sharing gained the proposal split, posture table, ownership pointer, and validation board, but Public Projection Contract did not change and several new claims remain unimplemented or internally stale. S01/S02 remain `DESIGNING`.
- Twelfth design return: Public Projection Contract gained all five accessibility annotations, but External Sharing is unchanged and the projection matrix still clips enlarged content. S01/S02 remain `DESIGNING`.
- Thirteenth design return: matrix overflow, status definitions, count truth, and the last broad proposal-content contradiction were fixed. S01 promoted to `DESIGN VALIDATED`; S02 remains `DESIGNING` because Story/Invite runtime posture and payload ownership are still duplicated in older tables.
- Fourteenth design return: three money/archive sections and most remaining S02 normalization landed. M09 and M10 promoted to `DESIGN VALIDATED`; M07, M08, M11, and S02 remain `DESIGNING` after code-grounded source checks found authority, currency, archive-preflight, primitive, and residual payload-ownership defects.
- Fifteenth design return: the audit regression was removed, the local Costs `Field` fork was replaced, and External Sharing now consistently delegates all four exact public payloads to Public Projection Contract while rendering runtime postures as separate tags. S02 promoted to `DESIGN VALIDATED`. M07, M08, and M11 remain `DESIGNING` because each still contains a literal source contradiction.
- Sixteenth design return: the payment fixture, mixed-currency arithmetic, sentinel warning, and reachable confirmed-booking archive specimen were corrected. M08 promoted to `DESIGN VALIDATED`. M07 remains `DESIGNING` only because Trip Workflow retains a stale resolved void-authority audit question; M11 remains `DESIGNING` because the archived actions are still local styled spans rather than canonical action primitives and the same stale audit row remains.
- Next gate: a source-only Trip Workflow cleanup—use `VBtn` for the three archived `Screen` actions and remove the resolved organizer/cost-manager void audit residue.

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

At the fourth return, cancellation remained close but not yet validated; the fifth-return closure below supersedes that interim status.

## Round 1 validation — fifth design return (cancellation closure)

### Cancellation result

Booking Cancellation Truth now passes the cancellation-specific design gate:

- exactly two verified provider outcomes: Cancelled and Still booked;
- Verification needed is durable and unresolved everywhere;
- refresh/network failure is rendered and read-only;
- no retry resubmits cancellation;
- completion and escalation receipts are separated truthfully;
- review opener, manager, controller, and viewer capabilities are distinct;
- split type is display-only without an invented change flow;
- State System render helpers are explicitly noncanonical prototype adapters owned by State System;
- no cancellation-specific meaningful-text decorative-token violation remains.

M01, M02, M03, and M06 move to `DESIGN VALIDATED`. They are not `PARITY VALIDATED`: implementation mapping and focused tests remain required before that later gate.

### Scope drift

The design tool also modified Booking Consent & Control despite the cancellation-only instruction. Those changes removed the mixed-ledger controller action and both consent-specific decorative-token violations. They are directionally correct, but M04/M05 remain `DESIGNING` because canonical row/status ownership, status-tone propagation, edge-state audit labels, and role-overlap modeling are still open.

The global consistency audit now reports 36 decorative-token findings, all outside the Round 1 canvases. Its remaining hard-failure categories are the unindexed Itinerary Redesign page and the pre-existing decorative-token backlog; shared-primitive warnings remain a separate project-wide cleanup item.

## Round 1 validation — sixth design return (consent micro-pass)

### Correctly landed

- The design tool respected the consent-only file boundary.
- Mixed-ledger and declined-recovery captions now identify viewer versus controller perspective explicitly.
- Traveler removal, controller unavailable, concurrent consent change, and provider-action-in-progress are visibly labeled `CODE AUDIT REQUIRED`.
- Consent-specific decorative-token violations remain at zero.

### Blocking residue

1. Status tone still does not reach visible chips in `BHead`, edge `Mini` cards, or receipts; `chipTone` remains unused by the actual `Chip` rendering.
2. `ConChip`, `Av`, and `ConRow` have no prototype-adapter/ownership annotations. The prompt did not require their deletion; it required clear Row System/status-anatomy ownership.
3. The role matrix now contains two self-consent rows that contradict one another:
   - the original row grants self-consent only to the affected-participant column;
   - the added row grants it to organizer, controller, affected participant, and ordinary viewer unconditionally.
4. The new all-columns row is itself false: an ordinary viewer who is not an included booking participant cannot answer consent. The correct rule is capability-based—**any included participant, regardless of other roles**.
5. The explicit doctrine **“Capabilities accumulate”** was not added.
6. Accessibility was not extended to cover text-plus-color status, audit-label reading order, or matrix overflow.
7. The requested validation board was not added.

M04 and M05 remain `DESIGNING`. The next consent pass should edit only status-chip propagation, adapter ownership notes, the role matrix, accessibility annotations, and the validation board; the lifecycle specimens no longer need redesign.

## Round 1 validation — seventh design return (consent cleanup)

### Correctly landed

- The design tool again respected the consent-only file boundary; no other project source changed.
- `ConChip` is now identified as a local prototype adapter whose consent vocabulary is local while geometry belongs to the canonical chip/status anatomy.
- `ConRow` and `Av` are now identified as local prototype adapters owned by the Row System and traveler/member identity anatomy, not as new shared components.
- The contradictory duplicate self-consent rows were replaced by one capability row.
- The role matrix now states that capabilities accumulate and uses a conditional `◐` marker for organizers or booking controllers who are also included participants.
- The four uncertain lifecycle states retain visible `CODE AUDIT REQUIRED` labels.
- The project consistency audit remains unchanged at the global level: one unrelated unindexed itinerary page, 36 unrelated meaningful-text token findings, and the pre-existing shared-primitive warning. The consent source adds no new consistency-audit finding.

### Blocking residue

1. `chipTone` still does not reach the visible status labels. `BHead`, result receipts, and lifecycle `Mini` cards tint their outer container through `Receipt tone={chipTone}`, but each visible label still renders as the neutral booking-kit `<Chip>`. This does not satisfy text-plus-color status semantics and makes the API misleading.
2. No labeled-status adapter was added. The remaining fix should reuse canonical Chip/StatusPill geometry while accepting a label and semantic tone, then use it consistently in all three call sites above.
3. The accessibility board still lacks explicit guidance for status text plus color, reading `CODE AUDIT REQUIRED` before the speculative state content, the meaning/announcement of `◐`, and horizontal matrix overflow at larger text sizes. Existing Dynamic Type and VoiceOver notes do not cover these requirements.
4. The requested source-visible validation board is absent. There is no final checklist proving status propagation, component ownership, exactly one conditional self-consent rule, audit-label preservation, accessibility coverage, and unchanged scope.

M04 and M05 remain `DESIGNING`. The next pass should touch only `booking-consent-control.jsx` and should not revise lifecycle copy, role permissions, frozen Trip header geometry, or unrelated canvases.

## Round 1 validation — eighth design return (consent finalization)

### Correctly landed

- The only substantive source change remains inside Booking Consent & Control; the thumbnail refresh is expected output.
- A documented local `StatusChip` adapter now gives the visible label itself a semantic foreground, background, and border tone while retaining complete text.
- `BHead`, resulting receipts, and lifecycle `Mini` cards all render their `chipTone` through `StatusChip`; no affected status call site falls back to the neutral booking-kit `Chip`.
- The existing role and consent rules remain unchanged and internally consistent.
- The four required accessibility topics were added in prose.
- A `VALIDATION · CONSENT CLEANUP` board was added and covers consent states, overlapping self-consent, authority, narrowing, viewer behavior, status treatment, prototype ownership, and the four audit-required transitions.
- The project consistency audit remains at the same unrelated global baseline: one unindexed itinerary page, 36 meaningful-text token findings, and the existing shared-primitive warning.

### Final blocking residue

1. The accessibility board claims the role and state matrices scroll horizontally, but both matrix wrappers still use `overflow: hidden`. This would clip enlarged content and makes the annotation false. Each matrix needs an actual horizontal overflow wrapper, with a stable inner minimum width.
2. Three accessibility requirements are duplicated: audit-label ordering, conditional `◐` announcement, and matrix overflow. Consolidate each into one row; retain the distinct text-plus-color status row.
3. The validation board does not visibly verify that no unrelated canvas or frozen Trip header element changed, despite this being an explicit final checklist item.
4. The source is missing its final newline. This is non-product residue, but should be corrected in the same surgical edit.

M04 and M05 remain `DESIGNING` until the annotation matches rendered overflow behavior and the validation checklist is complete. No other consent behavior or visual composition needs another pass.

## Round 1 validation — ninth design return (consent closed)

### Source checks passed

- The design tool changed only Booking Consent & Control plus the generated project thumbnail.
- Both matrices now have real `overflowX: auto` wrappers and stable inner minimum widths while retaining the existing clipped border-radius treatment inside the scroll region.
- The four new accessibility requirements each appear exactly once; the three duplicate rows are gone.
- The validation board now includes the explicit unchanged-scope assertion for unrelated canvases and the frozen Trip header.
- All existing `StatusChip` call sites and semantic tones remain unchanged.
- Exactly one self-consent capability row remains, with organizer/controller access conditional on also being an included participant.
- All four uncertain lifecycle states retain visible `CODE AUDIT REQUIRED` labels.
- The source again ends with a newline.

### Audit context

The global consistency audit remains unchanged: one unrelated unindexed itinerary page, 36 unrelated meaningful-text token findings, and the pre-existing shared-primitive warning. No consent source appears in those findings.

M04 and M05 move to `DESIGN VALIDATED`. They are not yet `PARITY VALIDATED`; the per-participant fixtures, role/action visibility checks, and implementation mapping remain later code-parity gates.

## Round 1 validation — eleventh design return (public governance integration)

### Correctly landed

- Scope was limited to External Sharing plus the generated thumbnail; no completed cancellation, consent, header, or card-grammar source changed.
- External Sharing now separates neutral proposal context from group decisions/votes.
- Neutral proposal context is labeled `DESIGN-APPROVED · BLOCKED BY CODE`; votes and standing are labeled `AUTHENTICATED-ONLY`.
- The five posture rows align textually with the existing Public Projection Contract decision block.
- External Sharing now states the intended ownership split and points field-level Story/Invite/Proposal/Unpacked payload governance to Public Projection Contract.
- The generic-public versus exact-trusted unavailable-state doctrine remains intact.
- A public-projection governance validation board was added.
- The global consistency audit remains at its unrelated baseline: one unindexed itinerary page, 36 meaningful-text token findings, and the existing shared-primitive warning.

### Blocking residue

1. Public Projection Contract is byte-for-byte unchanged. Its privacy annotations still lack Dynamic Type, VoiceOver/alt-text reading order, post-auth/recovery/retry focus, ≥44px targets, and reduced-motion guidance.
2. The new validation board says accessibility is documented even though the detailed accessibility contract was not added. This is a false completion claim.
3. External Sharing says it no longer maintains a second field matrix, but its Share Object Matrix still lists exact Story and Invite projection fields. Replace those duplicated payload cells with a pointer to Public Projection Contract while retaining shell/route governance.
4. The Share Object Matrix subtitle still says `16 objects`; the proposal split increased it to 17 rows.
5. The status legend renders the four newly added posture labels but provides no explanation for any of them because the legend description switch was not extended.
6. Story and Invite still appear as `CANON READY` in the ownership, object, and implementation-route tables without an adjacent runtime posture. `CANON READY` may remain a design-readiness axis, but those rows must explicitly pair it with `RUNTIME GATED` or `TOKEN-GATED` so readers do not mistake design readiness for availability.
7. The new validation board claims both canvases are aligned, but only one canvas was edited. It should be retained only after the two-source checks above are visibly true.

S01 and S02 remain `DESIGNING`. The next pass should modify only External Sharing and Public Projection Contract; it should correct these governance statements without redesigning any card or landing specimen.

## Round 1 validation — twelfth design return (public accessibility only)

### Correctly landed

- Public Projection Contract now contains distinct Dynamic Type, VoiceOver/generated-image alt-text order, focus, ≥44×44pt target, and reduced-motion requirements.
- The annotations artboard was enlarged to contain the additional rows without changing public-card or landing-state specimens.
- No unrelated source changed; the generated thumbnail is the only other changed artifact.
- The global consistency-audit result remains unchanged from the prior baseline.

### Blocking residue

1. External Sharing is byte-for-byte unchanged, so its duplicated Story/Invite field projections, stale `16 objects` label, blank definitions for four posture labels, and unpaired Story/Invite runtime postures remain.
2. Public Projection Contract now claims its projection matrix scrolls when needed, but the matrix wrapper still uses `overflow: hidden` and has no horizontal-scroll wrapper or stable inner minimum width.
3. External Sharing still lists `Group decisions, vote counts, or proposal content` under content that is never externally shared. This broad phrase contradicts the approved neutral proposal-context projection; it must distinguish vote/decision material from the narrowly allowed context-only projection.
4. The External Sharing validation board continues to claim accessibility and cross-canvas alignment even though the matrix behavior and the stale governance rows above remain unresolved.

S01 and S02 remain `DESIGNING`. The next pass needs no new specimens or doctrine: it is a literal/source-consistency correction across the two existing files.

## Round 1 validation — thirteenth design return (public governance narrowed)

### Source checks passed

- Both authorized sources changed; no unrelated design source changed.
- Public Projection Contract now uses a real horizontal-overflow wrapper with a stable inner minimum width.
- All five accessibility annotations remain present and now agree with rendered matrix behavior.
- The Share Object Matrix count is corrected to 17.
- All four new runtime-posture legend entries have non-empty definitions.
- The broad `proposal content` prohibition was replaced with a precise ban on votes, voter identity, counts, quorum, progress, and standing while preserving the separately governed neutral proposal-context projection.
- Neutral proposal context remains `DESIGN-APPROVED · BLOCKED BY CODE`; votes and standing remain `AUTHENTICATED-ONLY`.
- Generic public unavailable-state doctrine and trusted/owner-only exact reasons remain unchanged.
- The consistency audit remains at the unrelated project baseline.

These checks close the design contradiction tracked by S01. S01 moves to `DESIGN VALIDATED`; anonymous route/card inspection and privacy tests are still required before later `PARITY VALIDATED` status.

### Remaining S02 residue

1. Story public view and Invite peek still show only `ROUTE EXISTS · CANON READY` in the Ownership Map and Route Checklist, and only `CANON READY` in the Share Object Matrix. The separate posture board is correct, but the older tables still omit `DESIGN-APPROVED · RUNTIME GATED` and `TOKEN-GATED` respectively.
2. External Sharing still duplicates exact Story and Invite payload fields in the Share Object Matrix and Route Checklist (`Title, dates, sections...`, `Trip title, dates, organizer...`, and their data-field lists). Those governance cells must point to Public Projection Contract instead. Representative Story/Invite screen specimens may retain illustrative content.

S02 remains `DESIGNING`. Its final pass should change only External Sharing and should not touch Public Projection Contract, public cards, landing states, or accessibility.

## Round 1 validation — fourteenth design return (money/archive round)

### Scope and structure

- The existing Costs canon was extended in place through two new supporting source modules; no second Costs page was created.
- Trip Workflow gained one archived-booking-closure section rather than a new top-level lifecycle canvas.
- External Sharing also received the outstanding S02 table edits from the prior pass.
- The consistency audit baseline regressed from 36 to 39 meaningful-text token findings and added `costs-payments.jsx` to the independent `Field` reimplementation warning. Those three new token findings and the local field primitive must be cleaned before the round can close.

### M09 — DESIGN VALIDATED

- Payer view retains full masked-expense truth.
- Non-payer view hides amount, merchant/detail, category, and share amounts while retaining the payer attribution that current implementation also exposes.
- Masked expenses are payer-only and cannot allocate shares to other travelers.
- Booking-derived expenses cannot be masked.
- The visibility matrix, accessibility notes, and validation block are present.

The M09 ledger wording is corrected accordingly: current code hides non-payer amounts/details but does not hide payer identity.

### M10 — DESIGN VALIDATED

- Split type is rendered display-only during edit.
- No split-type conversion flow was introduced.
- Equal wording is shown only for stored equal shares.
- Matching exact amounts remain described as exact rather than equal.
- Accessibility and validation coverage are present.

### M07 — still DESIGNING

1. Runtime void authority is exact: **either the payment sender or payment recipient may void**. The new viewer copy says the recorder or a trip cost manager may void, while the matrix calls manager authority audit-required. Both are wrong or contradictory.
2. Replace role labels based on `payer (recorded it)` with sender/recipient semantics. `recorded_by` is audit metadata, not the authorization rule.
3. Remove the cost-manager/organizer void claim and its `CODE AUDIT REQUIRED` residue; the backend rule is already verified.
4. The new local nested `Field` implementation triggered the shared-primitive audit. Reuse the existing sheet/field or Costs row anatomy instead of independently defining `Field`.
5. Two disabled-looking meaningful actions (`Void payment` during processing and `Open review` while locked) use decorative muted text and are new consistency-audit failures. Use canonical disabled/action state treatment that remains readable.

### M08 — still DESIGNING

1. The design invents a `LOCKED` conversion rate and says a final rate is confirmed at settlement. Current code stores the conversion at expense creation/update; it has no final-settlement rate-confirmation workflow.
2. Current `ESTIMATED RATE` behavior is specifically the `rate_source === sentinel` failure posture: the stored converted total may be badly wrong and is not corrected automatically. Replace the plausible `≈ €71` estimate/final-confirmation story with the shipped warning truth or explicitly mark a safer future design as blocked by code.
3. Keep unsupported legacy/null conversion exclusion separate from sentinel-rate corruption. Do not present the sentinel as a safe approximate rate.
4. The hidden-amount `••••` uses a decorative text token and is a new audit failure; use a sanctioned meaningful-text color.

### M11 — still DESIGNING

1. Archive is organizer-only and the backend **refuses archive while a booking search or provider hold is active**. The new preflight shows a live hold and offers `Archive anyway`, which contradicts the archive endpoint. Replace it with a blocking preflight and a `Review booking work`/release-first recovery.
2. Archived trips do permit reads, cancellation, checkout reconciliation, and hold release in principle, but an active hold must be resolved before the archive transition. Do not use an impossible live-hold-after-archive specimen as the primary example.
3. Recovery restores the archived shell and selected pre-archive status; it does not resurrect proposals, searches, booking workflows, notification outcomes, or invites closed by archival. Add this explicit “closed coordination stays closed” truth to recovery and receipt specimens.
4. Reuse as new trip is implemented in Trip Settings, not unresolved. Replace the all-phases `CODE AUDIT REQUIRED` row with the verified archived-only private-template action and its exact exclusion contract: no travelers, invitations, conversations, bookings/provider references, costs, votes, proposals, workflow identity, event outcomes, or group ownership.
5. The new archived screens draw local pill actions as styled spans instead of using canonical action primitives. Reuse existing `VBtn`/workflow action components and preserve ≥44pt targets in source, not annotation only.
6. Review-opening/resolution and payment recording/voiding while archived need evidence. Keep them audit-required rather than presenting unsupported blocked/allowed claims.

### S02 — still DESIGNING

- Ownership Map and Share Object Matrix now pair Story/Invite design readiness with runtime posture correctly.
- Share Object Matrix payload fields now point to Public Projection Contract.
- Route Checklist projection cells point correctly, but their `data` cells still list exact Story/Invite payload fields. Replace those remaining lists with the same Public Projection Contract pointer.
- Route Checklist status is stored as combined text rather than separately rendered known tags. If the table renders plain text this is legible, but the validation should explicitly identify route existence, canon readiness, and runtime availability as separate axes.

No new canvases or product doctrines are needed. The next pass should correct these literal conflicts and audit regressions in the existing sources.

## Round 1 validation — fifteenth design return (correction round)

### Audit and component hygiene

- The consistency audit returned from 39 to the established 36 unresolved meaningful-text findings, with the same 8 reviewed-decorative findings.
- `costs-payments.jsx` no longer defines a local `Field`; it consumes `VSheetField`, returning the independent `Field` warning from three implementations to the prior two.
- The remaining audit failures are project-wide baseline items: one unindexed legacy HTML file and the 36 pre-existing meaningful-text findings. This return did not add a new audit finding.

### M07 — still DESIGNING

- The sender-or-recipient void rule is now correctly stated in the payment detail, role matrix, and validation copy, and organizer/cost-manager status no longer grants void authority.
- One viewer specimen is internally inconsistent: its visible record is `Ana paid You`, with Ana and You avatars, but the authority explanation calls Theo the recipient. The recipient named in the explanation must be `You`, or the whole fixture must be changed consistently to Ana → Theo.
- Trip Workflow still lists organizer/cost-manager void authority as `CODE AUDIT REQUIRED`. This is stale: backend authorization is already verified as sender-or-recipient only. Remove that audit question and let the Costs canon remain the owner.

### M08 — still DESIGNING

- The sentinel conversion specimen now accurately exposes the stored 1.0 fallback, marks it `MAY BE WRONG`, and says it is not corrected automatically. Unsupported/null conversion remains separately excluded.
- The mixed-currency summary is arithmetically stale: its included rows are €96 + €96 + €780, but the displayed settlement total is €263.00. If all three stored converted values count, the fixture total must be €972.00.
- The sentence `the total is never faked` contradicts a total containing a known sentinel fallback that may be wrong. It should say the displayed total uses stored converted values, flags the sentinel contribution as potentially wrong, and excludes only the unconverted row.

### M11 — still DESIGNING

- The before-archive preflight now correctly blocks archive while searches or holds are active, and the ready state correctly preserves records without implying cancellation, refund, settlement, or deletion.
- The archived booking specimen still shows an active Ramiro’s hold (`Held until 18:00`) and offers `Release hold`. That state cannot be reached through the archive endpoint because active provider holds block archival. Use a confirmed booking/cancellation or reconciliation example for surviving archived recovery, or explicitly model a later-discovered stale provider state rather than an active hold carried through archive.
- The archived journey still renders `Screen` actions as styled `<span>` elements with 9px vertical padding, despite claiming canonical actions and ≥44pt targets. Replace them with the existing workflow/VBtn action primitive.
- The matrix and audit block still ask whether an organizer/cost manager may void a payment. That question is already resolved by Costs/backend truth and must be removed; other genuinely unaudited archived expense/payment permissions may remain marked for code audit.
- Recovery truth, closed-coordination truth, exact return, and archived-only `Reuse as new trip` with its exclusion contract are now correctly represented.

### S02 — DESIGN VALIDATED

- Share Object Matrix and Route Checklist now delegate exact Story and Invite allowed/redacted fields to Public Projection Contract instead of maintaining duplicate payload lists.
- The broader ownership note delegates Story, Invite, Proposal, and Unpacked field-level payloads to the same owner.
- Route existence, canon readiness, and runtime posture are stored and rendered as separate status tags rather than one combined label.
- External Sharing remains responsible only for shell, lifecycle, route, fallback, privacy-doctrine, and governance concerns. No public-card or landing-state redesign was introduced.

No new canvas is needed for the next pass. Correct only the three existing owner sections above and leave the frozen Trip header, validated public-projection work, and all unrelated canvases untouched.

## Round 1 validation — sixteenth design return (three-item correction)

### Source checks passed

- The payment viewer now consistently renders and describes Ana → You. Its authority copy correctly states that only sender Ana or recipient You may void, and organizer/cost-manager status grants nothing.
- The mixed-currency headline is now €972.00, matching the three included stored values (€96 + €96 + €780). The sentinel-derived €780 remains visibly `MAY BE WRONG`; the unsupported row remains excluded.
- Currency copy no longer claims the total is infallible. It explicitly says the total uses stored converted values, identifies the 1.0 fallback contribution as potentially wrong, and separates it from the excluded unconverted expense.
- The archived booking specimen is now a reachable confirmed booking rather than an active hold carried through archive. Forward modification/rebooking is absent, while controller-attributed cancellation/reconciliation is presented as surviving liability-reducing work.
- The consistency audit remains at the established project baseline: one unindexed legacy HTML file, 36 unresolved meaningful-text findings with 8 reviewed-decorative findings, and the pre-existing shared-primitive warning. This return introduced no new audit regression.

### M08 — DESIGN VALIDATED

The currency section now distinguishes normal stored conversions, sentinel-corrupted stored conversions, and unsupported/unconverted exclusions without inventing a settlement-time rate-locking or auto-correction workflow. Its displayed arithmetic and explanatory copy agree.

### M07 — still DESIGNING

The Costs owner section is now internally correct. Trip Workflow nevertheless still contains the audit item `Whether a cost-manager/organizer may void a payment they did not record`. This question is already resolved by backend and Costs truth: only the payment sender or recipient may void. Remove the stale audit item and leave void ownership delegated to Costs before promoting M07.

### M11 — still DESIGNING

1. The impossible archived active-hold specimen is fixed.
2. The `Screen` action renderer still maps actions to locally styled `<span>` elements. Adding `minHeight: 44` improves geometry but does not satisfy the explicit requirement to consume the existing canonical `VBtn`/workflow action primitive. Replace those spans with `VBtn`; do not create another wrapper family unless it is a trivial adapter with no independent geometry.
3. The archived matrix still renders `Void a payment` as audit-required, and the audit block repeats the resolved organizer/cost-manager question. Remove the resolved role question. If archived payment mutation availability itself is not code-verified, label that exact archived-route availability question rather than reopening payment-role authority.

No content redesign or new canvas is required. The remaining work is a small source-only cleanup in the existing Archived Trip Booking Closure section.
