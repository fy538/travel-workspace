---
doc_type: working
status: active
owner: engineering / design
created: 2026-07-18
last_verified: 2026-07-18
expires: 2026-08-17
why_new: Cross-repository execution record for the Vesper 255 parity waves; existing design-validation ledger does not own implementation sequencing or code evidence.
design_target: Vesper 255, Round 1 M01-M12 and S01-S02
code_target:
  travel_app: d10db32c
  travel_agent: 9cd4b143
  workspace: ccae8e2 plus the uncommitted Vesper 255 ledger update
source_of_truth_for: vesper-255-round-1-code-parity-execution
---

# Vesper 255 Round 1 code-parity audit and execution plan

## Executive verdict

Round 1 design is complete, but Round 1 production parity is not. The codebase already contains substantial durable implementation for booking authority, booking consent, expense disputes, recorded payments, currency handling, masking, archive/recovery, receipt upload, and public share projections. This is not a greenfield program.

The remaining work falls into three different classes:

1. **A current privacy contradiction:** the unauthenticated proposal landing and generated card expose vote tallies or vote-derived status, while the validated canon prohibits both.
2. **Narrower production contracts:** booking cancellation, booking viewer projection, archive preflight, expense review capabilities, split-type immutability, and receipt scanning do not expose all states or guarantees represented in the canon.
3. **Implemented but not parity-certified behavior:** recorded payments, currency truth, and masked expenses have strong source and test evidence, but still lack the complete real-backend/device/accessibility evidence required for `PARITY VALIDATED`.

No Round 1 row should be promoted to `PARITY VALIDATED` yet. The correct next move is a bounded full-stack implementation program, beginning with public-proposal containment and then following dependency-shaped vertical slices.

## Audit scope and evidence

The audit read production source rather than comparing screenshots. It covered:

- app routes, screen components, data hooks, mock adapters, generated types, and tests in `travel-app`;
- backend API routes, Pydantic models, database transitions, workers, receipts, and tests in `travel-agent`;
- the Vesper 255 source boards for booking cancellation, booking consent/control, Costs, Receipt/OCR, Trip Workflow, and Public Projection Contract;
- the active Booking, Trip Costs, Trip Settings/Admin, and External Sharing surface contracts.

Repository state during the audit:

- `travel-app` was clean on `main` at `d10db32c`.
- `travel-agent` was on `codex/openai-canonical-cutover` at `9cd4b143` with unrelated vector/embedding changes in progress. This audit did not modify or rely on those files.
- the workspace had the intentional uncommitted Vesper 255 parity-ledger update.

Validation run:

- Frontend: 12 targeted suites, **97 tests passed**.
- Backend: six selected offline modules, **310 tests passed, three PostgreSQL tests deselected**.

Passing current tests proves that current code is internally consistent. It does not prove design parity when the current test expectation itself encodes an older product decision.

## Canon and QA prerequisite

At audit time, the app's design-alignment fingerprint still identified **Vesper 220**. The repository's established alignment architecture intentionally commits normalized page hashes rather than the multi-megabyte Claude Design HTML export; `design/vesper-canon-anchor` is a git-ignored local mirror, not a tracked artifact. Reproducibility therefore means a committed export label, normalized fingerprints, page ownership, and generated status—not checking the design bundle into git.

Before claiming visual parity:

1. fingerprint the chosen Vesper 255 export with the repository's established normalization rules;
2. commit `travel-app/docs/design-alignment/canon.fingerprint.json` and its append-only diff log;
3. register the new Booking Cancellation, Booking Consent/Control, Receipt/OCR, Public Projection, and archived-booking specimens against the owning surfaces;
4. regenerate design status and require current fingerprint references in accepted verdicts.

This prerequisite should be done as a small app evidence commit. It should not be mixed into a behavior-changing backend commit.

## Row-by-row parity assessment

| ID | Current implementation | Verdict | Principal remaining work |
|---|---|---|---|
| M01 | Durable cancellation claim, reconciliation worker, duplicate prevention, pending recovery, cancelled and manual-attention truth exist. | **PARTIAL** | Preserve requested, processing, refreshing/read-failed, pending-verification, verified not-cancelled, cancelled, and manual-action-required as distinct client states. |
| M02 | Backend emits replay-safe cancellation receipts for cancelled, not-cancelled, and escalation outcomes. | **PARTIAL** | Add canonical structured anatomy: controller, last checked, what changed, what did not, exact next action, and viewer-safe destination; render it as a typed receipt. |
| M03 | Cancelled booking-linked expenses receive a review hint and refund evidence without changing money. | **PARTIAL** | A review hint does not pause settlement. Define and implement the typed transition from cancellation receipt to the affected expense's settlement-excluded review state. |
| M04 | Durable participant ledger supports pending/approved/declined/excluded, self-response, reminder cooldown, self-only narrowing, and confirmation blocking. | **PARTIAL / CLOSE** | Render the complete named ledger, including approved and excluded states and reminder evidence; expand frontend fixtures and accessibility coverage. |
| M05 | Mutations enforce requester/controller authority; non-controller UI is view-only. | **PARTIAL** | The backend returns the same sanitized offer projection to every trip member. Add viewer-aware projection so provider references and continuation controls are controller-only, while other travelers receive plan/status truth and attribution. |
| M06 | Durable expense disputes, opener-only withdrawal, payer/organizer resolution, settlement exclusion, and live-payment rejection exist. | **PARTIAL / CLOSE** | Add server-authored review capabilities. The UI currently offers `Flag for review` on a payment-locked expense and learns the void-first prerequisite only from a failed mutation. |
| M07 | Recorded and voided payment history, either-party void authority, idempotent void, debt restoration, and visible voided rows exist. | **IMPLEMENTED; EVIDENCE OPEN** | Run PostgreSQL lifecycle tests, real-backend app integration, accessibility, and accepted visual QA. No broad redesign is required. |
| M08 | One settlement currency, conversion provenance, sentinel warning, and exclusion of unsupported legacy conversions are implemented and unit-tested. | **IMPLEMENTED; EVIDENCE OPEN** | Add a real mixed-currency fixture and certify totals, day subtotals, original values, estimated-rate labeling, and unsupported exclusions end to end. |
| M09 | Payer-only masking, payer-only shares, settlement exclusion, title/detail/receipt redaction, search/concierge leak guards, and booking-mask rejection exist. | **IMPLEMENTED; EVIDENCE OPEN** | Run a payer/non-payer real-backend visibility matrix and device/accessibility pass. Confirm payer attribution remains visible without reconstructing the private object. |
| M10 | Edit UI renders split type as display-only and never sends it. | **PARTIAL** | The backend update contract still permits an in-place split-type change when shares are resent. Reject split-type changes for existing expenses and sync the generated contract/tests. |
| M11 | Durable archive/recovery, preserved records, organizer gates, closed coordination, reuse, and terminal write gates exist. | **PARTIAL** | The canon and Trip Settings contract refuse archive while a booking search or provider hold is active; backend archival currently expires ordinary active searches and proceeds. Add an archive preflight/read model, align refusal semantics, render the blocked state, and certify archived booking action visibility. |
| M12 | Upload, polling, permission rationale, retry, OCR prefill, explicit Add, idempotent creation, and protected receipt reads exist. | **MAJOR PARTIAL** | Implement typed complete/partial/unreadable states, visible long-scan posture, manual supersession, no late auto-apply, OCR suggestion/correction provenance, failed-scan receipt retention, add-failure recovery, and exact ledger return. |
| S01 | An unauthenticated proposal HTML page and 9:16 card exist. | **CONTRADICTS CANON** | Immediately stop exposing vote counts and vote-derived status to unauthenticated viewers. Until actor-controlled neutral sharing exists, use the canon's unsupported/generic-auth-handoff fallback. |
| S02 | Story, Invite, and Unpacked projections have substantial allowlist and generic-unavailable coverage. Proposal exists outside that frozen contract and violates it. | **PARTIAL** | Bring all four projections under one allowlist/revocation/expiry/stale/alt-text contract; complete actor-controlled field selection and add Proposal only after S01 is safely contained. |

## Material source findings

### 1. Cancellation state is compressed at the API boundary

`travel-agent/backend/api/routes/booking.py::_public_offer` maps processing, refreshing, and pending cancellation into a single `pending` value. It exposes only `pending`, `cancelled`, and `manual_action_required`; `not_cancelled` is dropped to `null`. The generated app contract mirrors that three-value union.

The backend worker is richer than the projection: `tests/booking/test_cancellation_reconciliation.py` proves `not_cancelled`, terminal receipt delivery, delivery retry, and replay recovery. The missing work is principally contract projection and client composition, not provider reconciliation.

The app screen in `travel-app/app/booking/[sessionId].tsx` renders pending and manual-attention recovery but has no verified still-booked composition, no separate request-submitted phase, and no last-checked/read-failure semantics.

### 2. Cancellation receipts are durable but not yet the canonical object

`travel-agent/backend/core/receipts.py::create_booking_cancellation_receipt` writes a replay-safe trip-room message and a booking destination. Its payload does not carry the canonical controller, checked-at time, changed/unchanged facts, exact cost-review destination, or typed next action.

The receipt worker is a good foundation. Extend this contract rather than introducing a second notification system.

### 3. Booking cancellation and Costs review are connected visually, not transactionally

`travel-agent/backend/api/routes/expenses.py::_with_booking_reconciliation` correctly leaves expense money unchanged and projects refund/cancellation evidence. `ExpenseDetail` correctly says that the existing balance is unchanged. However, settlement exclusion is driven by an open expense dispute, not by `booking_reconciliation.review_required`.

Before implementing M03, make one explicit product/contract decision:

- either cancellation opens a typed system booking-cost review automatically, with payer/organizer resolution and no fictional human opener;
- or an eligible payer/share participant must explicitly open the review, in which case the receipt must not claim settlement is already paused before that action.

The validated design currently depicts the paused state, so the first option is the closer implementation target. Do not silently overload a human-authored dispute row with a fabricated opener.

### 4. Consent persistence is stronger than consent presentation

`backend/core/booking_consent.py` and its PostgreSQL tests cover the full state machine. The booking screen shows waiting/declined summaries and the current traveler's actions, but it does not render a complete status row for every included and excluded participant. After narrowing to self, the consent card disappears because only one active participant remains, hiding the excluded ledger from the surface.

Use the existing consent response. This is primarily a presentation, fixture, and accessibility task.

### 5. Controller authority is enforced for writes but not fully for reads

Booking write routes correctly require the session controller, and the app removes mutation actions for viewers. But `_public_offer` is actor-agnostic. Every trip member receives the same provider-response projection, including provider-side identifiers retained by the sanitizer.

M05 requires a viewer-shaped read model. UI-only hiding is insufficient because the network payload itself must obey the controller-only evidence rule.

### 6. Expense governance needs action capabilities, not error-driven discovery

`ExpenseMutationCapability` covers edit/delete and the live-payment recovery route. There is no equivalent capability object for opening, withdrawing, or resolving a review. `ExpenseDetail` renders `Flag for review` based on share/payer membership even when a live payment makes the action invalid.

Add a server-authored `review_capability` projection and repeat every check transactionally on mutation. It should state:

- `can_open`, `can_withdraw`, `can_resolve`;
- denial reason such as `not_affected`, `review_already_open`, or `live_settlement_payment`;
- recovery such as `void_settlement_payments`;
- the exact open review id and actor relationship needed by the UI.

### 7. Split immutability is only a frontend convention

`EditExpenseSheet` is aligned and its tests prove no `split_type` is sent. The backend API tests also prove that a caller may change `split_type` if it resends shares. That is incompatible with the validated rule that an existing expense is not re-sliced in place.

Make this a contract-sensitive backend change: reject a changed split type, retain share updates within the existing type only where supported, refresh OpenAPI, regenerate TypeScript, and update mock parity.

### 8. Archive behavior disagrees on active searches

`backend/core/db/trip_archival.py` blocks active provider holds but expires ordinary pending/offers-ready/review booking work during archive. The current Trip Settings contract and Vesper 255 archived-booking canon both say archive is refused while a booking search or provider hold is active.

Add a read-only archive preflight and reuse its classifier transactionally inside archive. The UI needs a specific `Finish booking work first` state and route to the exact booking work. A generic archive failure toast is not sufficient.

### 9. Receipt/OCR is a working upload path, not yet the designed review workflow

`useUploadReceipt` exposes `isStillScanning`, but `AddExpenseSheet` does not destructure or render it. The hook sets `done` for every completed OCR result without distinguishing complete, partial, or empty/unreadable extraction. Manual typing does not supersede the active scan; the poll may still finish and apply suggestions to fields that remain empty. Failed or manually superseded scans then use the generic create path without attaching the retained receipt.

The backend also exposes `ocr_result` as an untyped dictionary and `ocr_status` as a plain string. Implement M12 as a contract-backed vertical slice:

- define a typed OCR result and bounded status/quality vocabulary;
- derive or persist `complete`, `partial`, and `unreadable` without invented confidence;
- keep upload progress indeterminate;
- surface the 30-second still-scanning state already computed by the hook;
- when the user chooses manual continuation, invalidate the client generation and ignore late results;
- retain and attach the receipt even when OCR fails or is superseded;
- preserve OCR suggestions separately from user-confirmed values;
- retry expense creation without rescanning or duplicating the expense;
- return to Costs and select/announce the canonical newly added ledger row.

### 10. Public proposal sharing is the first implementation priority

`backend/api/routes/proposal_landing.py` explicitly treats the trip/proposal id pair as a bearer credential and renders proposal title, description, vote tally, and resolved status without authentication. Its tests intentionally assert `1 for · 1 against`, `Waiting on the group`, and `Accepted`.

This is incompatible with S01 and with the active External Sharing contract, which says group decisions and votes never render on a public route.

The safe immediate posture is:

- preserve the universal/deep-link handoff to the authenticated proposal route;
- make the unauthenticated HTML and generated image generic and non-object-revealing;
- do not read or render proposal votes, status, description, trip identity, or title in the signed-out response;
- add actor-controlled neutral proposal sharing later as an explicit share object with revocation, rather than treating raw ids as a public credential.

## Recommended implementation waves

### Wave 0 — reproducible baseline and privacy containment

**Scope:** canon anchoring plus S01 containment.

1. Promote Vesper 255 through the tracked fingerprint, page-ownership, and generated-status artifacts.
2. Replace signed-out proposal content/card output with a generic authenticated handoff that reads no proposal decision data.
3. Update proposal landing tests so any title, description, vote count, status, ids, or reason leakage fails.
4. Add proposal routes to `test_public_projection_shapes.py` and the external-sharing surface contract.

**Exit:** no unauthenticated proposal request can disclose group-decision content, and Vesper 255 is the reproducible design target.

**Execution checkpoint — 2026-07-18:** functional scope complete, calibration still open.

- Vesper 255 is fingerprinted as 66 pages; its three newly introduced pages—Booking Cancellation Truth, Booking Consent & Control, and Public Projection Contract—now have explicit owning surfaces.
- Generated status and stale-surface evidence were refreshed. Surface mapping and companion-system validation pass.
- Signed-out proposal HTML and card rendering no longer query the private proposal model. Both return frozen generic authentication-handoff content while retaining the app destination.
- Proposal privacy assertions now live both in the focused route tests and the project-wide public-projection shape suite. The broader public projection regression selection passes.
- The design gate's mapping/fingerprint checks are clear. Its remaining failure is the judge calibration age (15 days against a 14-day window); a new blind golden judgment is required before any L5 claim. Rescoring the old judgment would not be valid evidence.

### Wave 1 — cancellation truth vertical slice

**Scope:** M01, M02, M03.

1. Introduce an exact cancellation read model with state, controller attribution, timestamps, safe provider posture, and next-action capability.
2. Preserve `not_cancelled` and read-failure/refresh semantics across OpenAPI and generated app types.
3. Extend the durable receipt metadata and typed client renderer rather than adding a parallel receipt family.
4. Implement the adjudicated booking-cost review transition and exact expense destination.
5. Add replay, restart, controller/viewer, receipt-return, and settlement-exclusion tests.

**Exit:** request, waiting, read failure, cancelled, still booked, and manual action remain distinguishable after restart; no action can resubmit an in-flight cancellation; the Costs consequence is truthful and durable.

### Wave 2 — booking roles and consent projection

**Scope:** M04, M05.

1. Make booking offer/read projection viewer-aware at the backend.
2. Expose controller attribution to everyone while restricting provider references and continuation evidence to the controller.
3. Render a complete named consent ledger, including approved, pending, declined, and excluded rows plus reminder evidence.
4. Certify action visibility for controller, organizer-non-controller, included traveler, excluded traveler, and ordinary viewer.

**Exit:** network payload and UI both obey the role matrix; every included traveler's consent state remains legible; confirmation remains blocked until the active scope approves.

### Wave 3 — Costs governance and contract hardening

**Scope:** M06, M10, then certification of M07-M09.

1. Add review capabilities and void-first recovery to each expense projection.
2. Reject in-place split-type changes in the backend contract and regenerate client types.
3. Run real PostgreSQL fixtures for disputes, payments/void, mixed currency, and masking.
4. Run app mock/real parity, accessibility, and surface QA for payer, non-payer, opener, payer-manager, organizer-manager, transfer party, and unrelated viewer.

**Exit:** M06 and M10 behavior is complete; M07-M09 have code-backed evidence sufficient to consider promotion to `PARITY VALIDATED`.

### Wave 4 — archived booking closure

**Scope:** M11.

1. Add one archive-preflight classifier shared by read route and archive transaction.
2. Refuse active searches and provider holds; return exact blocker objects and destinations.
3. Render ready, blocked, archived/read-only, archived booking detail, and recovered/revalidation states.
4. Verify that archived state removes forward actions while preserving only authority-controlled cancellation, reconciliation, and hold-release truth where still valid.
5. Add two-connection archive-versus-booking tests and route-return tests.

**Exit:** archive behavior matches the active Trip Settings contract and Vesper 255 source, with no silent booking-work expiry that the UI described as a clean archive.

### Wave 5 — Receipt/OCR vertical slice

**Scope:** M12.

1. Add typed OCR status/result/quality contracts and regenerate client types.
2. Refactor `useUploadReceipt` into an explicit state machine with manual supersession and late-result rejection.
3. Recompose Add Expense around shared primitives and the complete/partial/unreadable review states.
4. Preserve the receipt through failure/manual continuation and attach it to the confirmed expense.
5. Add upload, long-scan, empty extraction, partial extraction, correction, add failure/retry, idempotency, privacy, restart, and accessibility tests.
6. Run the Trip Costs surface capture against current Vesper 255 design refs.

**Exit:** scanning never creates an expense before confirmation, never overwrites manual work, never invents extracted values, never loses the retained receipt, and returns through canonical Costs truth.

### Wave 6 — four-projection public contract

**Scope:** S02 after S01 is safely contained.

1. Define one testable projection registry for Story, Invite, Proposal, and Unpacked.
2. Pin allowed/prohibited payload, HTML, generated image, alt text, cache/stale, expiry, revocation, and generic-unavailable behavior for all four.
3. Implement actor-controlled neutral proposal sharing only if the product is ready to persist a share/revocation object; otherwise leave it unsupported.
4. Finish actor-selected Story/Unpacked fields and Invite token controls where current contracts remain narrower.
5. Run public route, generated-card, and external-sharing device QA.

**Exit:** all four projections share one enforceable default-deny contract and no public artifact leaks group decisions, costs, companions, or private state.

## Commit and branch boundaries

Keep the work reviewable and avoid the unrelated backend vector lane:

1. workspace/app canon-anchor commit;
2. backend/app S01 privacy-containment commits;
3. backend contract + OpenAPI snapshot + generated app types for each full-stack wave;
4. app composition/tests in the matching wave branch;
5. workspace ledger/status update only after evidence passes.

Do not combine all Round 1 work into one branch. Every contract-changing backend wave should use the required flow:

1. backend model/route/tests;
2. workspace OpenAPI refresh;
3. generated app types;
4. mock adapter parity;
5. frontend behavior/tests;
6. real-backend cheap mode;
7. registered surface QA where visible behavior changed.

## Promotion gates

A row may move from `DESIGN VALIDATED` to `PARITY VALIDATED` only when all applicable evidence exists:

- exact requirement-to-source mapping;
- backend authorization and transition tests;
- mock and real adapter parity;
- generated contract synchronized;
- route/return and restart/replay behavior tested;
- privacy matrix tested for every actor role;
- accessibility semantics and large-text behavior checked;
- registered surface capture judged against the current Vesper 255 fingerprint;
- no unresolved contradiction is hidden behind a design or implementation note.

## Recommended immediate action

Start Wave 0 now. The proposal landing is the only finding that currently violates the validated privacy direction in enabled code, and the stale Vesper 220 fingerprint prevents honest visual certification of every later wave. After that, execute the cancellation vertical slice before polishing already-strong Costs behavior.
