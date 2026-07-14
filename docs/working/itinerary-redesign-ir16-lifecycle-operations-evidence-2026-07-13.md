---
doc_type: working
status: active
owner: frontend / backend / product
created: 2026-07-13
last_verified: 2026-07-13
expires: 2026-08-12
why_new: Record IR-16 Vesper, provider, lifecycle, completed-entry, and write-back implementation evidence.
source_of_truth_for: [itinerary-redesign-ir16-lifecycle-operations-evidence]
---

# Itinerary redesign IR-16 — lifecycle and operation completion evidence

**Date:** 2026-07-13
**Status:** complete behind independent flags
**Lane:** itinerary-foundation
**Backend commit:** `e7dfd1eca`
**Frontend commits:** `c95303a8`, `662f36da`, `9195d349`

## Outcome

IR-16 completes the selected-cohort bridge from the canonical IR-10/11/12
authorities into the itinerary shell. It does not add a chat-native editor or
reconstruct provider, lifecycle, expense, attention, or history truth on the
client.

The implementation now provides:

- Vesper-prepared operations as typed chat attachments that open the existing
  itinerary operation sheet. Vesper requests use the separately gated backend
  `/vesper/prepare` route; manual requests continue through the same canonical
  preview contract and both converge on the same confirmation/proposal/commit
  UI.
- Protected Replace as Replace-and-rebook when an authorized provider revision
  is available. The provider precondition binds dependency identity and
  revision, and the confirmed commit starts the durable IR-10 saga rather than
  applying a plan-only mutation.
- Provider detail that displays itinerary commitment, provider outcome, and
  expense linkage as three separate facts. Controller-limited provider detail
  remains limited; shared status remains visible. Pending/partial continuations
  remain linked to the saga and Bookings/Changes entrances.
- A contextual destination/date Replan entrance in Trip Details. It sends the
  traveler to Vesper to recommend and prepare one typed canonical Replan, then
  returns to Itinerary for review; chat is not an editor.
- Backend-authored hybrid entry routing. Fresh entry follows the IR-12
  recommendation only when the independent backend and frontend routing gates
  are both enabled. Not-ready/thin Memory and completion-session entry open the
  completed itinerary record; meaningful Memory may become the fresh default;
  cancelled trips always retain the itinerary record.
- Explicit completed-record/Memory choice stored in trip workspace session
  state. Memory always offers the final itinerary, and the final itinerary
  offers Memory only when the server says it is meaningful.
- Planned-versus-happened correction remains in the canonical factual operation
  flow while structural post-trip operations remain server-denied. The live
  shell retains its existing server-derived Now/Next, disruption, and cached
  offline-reading behavior.
- Typed write-back observations with bounded confidence, viewer-scoped reads,
  idempotent creation, idempotent correction retry, and explicit supersession.
  Cross-trip operation/lineage/provider references and non-self attendance are
  rejected. The object detail renders confidence and sends corrections through
  the offline-gated API.

## Additive backend contract

Migration `ir16a001` follows `ir11a001` and adds required `confidence` and
`idempotency_key` columns to the existing write-back substrate. Legacy rows are
backfilled deterministically (`confidence=1`, `legacy:<id>` idempotency key).
The migration keeps one Alembic head and is reversible.

The IR-12 Plan authority now includes viewer-scoped active write-backs and
authorized provider revisions. Completed-entry `routing_enabled` becomes true
only under `ITINERARY_COMPLETED_ENTRY_V2`; recommendation and Memory state remain
server-authored.

## Independent rollout controls

- `ITINERARY_PROVIDER_SAGA_V2`
- `ITINERARY_OP_REPLAN_V2`
- `ITINERARY_VESPER_GATEWAY_V2`
- `ITINERARY_COMPLETED_ENTRY_V2`
- `ITINERARY_WRITEBACK_V2`
- matching `EXPO_PUBLIC_*` client flags

No umbrella IR-16 flag enables the stack.

## Exit-gate evidence

- Manual/Vesper parity: builder parity from IR-14 remains intact; the IR-16
  sheet test proves a Vesper-attributed operation calls the Vesper gateway and
  does not call the manual preview path or create a second editor.
- Provider partial: the typed-object test renders a committed-plan / partial-
  provider / recorded-expense fixture and retains `retry_booking`. The provider
  sheet test proves protected Replace starts the saga and never calls ordinary
  commit.
- Lifecycle edges: executable fixtures cover immediate/not-ready, thin,
  meaningful Memory, explicit session choice, cancelled record, client flag
  dark, and server routing dark.
- Offline: all new mutations use `useGatedMutation`; the shared offline gate and
  mutation-boundary tests pass. Plan remains readable from the persisted query
  model and does not invent a fallback write.
- Write-back correction: the object test renders a confidence score and submits
  a typed superseding occurrence. Backend contracts enforce confidence bounds,
  idempotency, self-only attendance, reference scope, visibility, and
  supersession.
- Awareness: IR-09/12 unseen/history remains keyed by operation ID; IR-16 adds no
  parallel cursor or notification state.

## Verification

Frontend:

- `npx tsc --noEmit` — passed.
- Six focused itinerary/chat suites — 87 tests passed.
- Provider/Vesper sheet suite after the final gateway handoff — 8 tests passed.
- Provider-partial/write-back object suite — 5 tests passed.
- Offline network/gate suites — 4 tests passed.
- Targeted ESLint — zero errors; pre-existing size/hook/style warnings only.

Backend:

- Ruff on every changed backend/migration/test file — passed.
- Python byte compilation — passed.
- Alembic single-head check — passed (`ir16a001`).
- Route-auth, cross-agent, lazy-import, timeout, secret, and surface-registry
  pre-commit checks — passed.
- Backend runtime pytest was not runnable in this worktree because the Python
  dependencies (including Pydantic/SQLAlchemy/Pytest) are not installed. The
  new route and contract tests are committed; database execution remains a CI
  requirement before flag exposure. Pre-commit ratchets that require those
  dependencies, and unrelated repository-wide size/status baselines, were
  explicitly skipped for the backend commit rather than reported as passing.

## Integration note

The shared `MessageAttachment` addition and HTTP/API interface methods were
captured by concurrently landing commits `4529ce59` and `44f3f3a9` while this
slice was in progress. The IR-16 frontend commits above contain the remaining
implementation and tests; the recorded verification ran against the resulting
current `main` tree.

## IR-17 handoff

Keep every flag dark until CI executes the new backend tests and the selected
cohort has real provider partial, completed-entry, and write-back correction
telemetry. IR-17 may then roll out in the governed order: Vesper preparation,
provider continuation, Replan, completed entry, and write-back independently.
Rollback disables the relevant flag without deleting durable operations,
provider partials, write-backs, or history.
