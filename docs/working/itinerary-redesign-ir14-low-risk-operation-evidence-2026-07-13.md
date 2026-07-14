---
doc_type: working
status: active
owner: frontend / product
created: 2026-07-13
last_verified: 2026-07-13
expires: 2026-08-12
why_new: Record the IR-14 low-risk operation implementation, authority boundaries, flags, and verification evidence.
source_of_truth_for: [itinerary-redesign-ir14-low-risk-operation-evidence]
---

# IR-14 — Low-risk operation UX evidence

Date: 2026-07-13
Lane: `itinerary-foundation`
Status: implementation complete behind dogfood flags; paired device/backend dogfood remains an exposure check

## Outcome

IR-14 adds the inspect → Change → construct → preview → resolver ending →
landed path for low-risk Add, Move/Reorder, Replace, and Remove. It calls the
canonical IR-06 preview, IR-07 commit, and IR-09 recovery endpoints; it does not
reuse the legacy Plan writers or infer authority, recovery, provider truth, or
proposal behavior in the client.

The implementation remains within the amended trip-shell boundary. IR-15 still
owns proposal submission and collaboration. IR-16 still owns Vesper entry UX,
protected provider continuation, Replan, and lifecycle completion.

## Exposure flags

The frontend flags are independent and default off:

- `EXPO_PUBLIC_ITINERARY_ADD_OPERATION_V2`
- `EXPO_PUBLIC_ITINERARY_MOVE_OPERATION_V2`
- `EXPO_PUBLIC_ITINERARY_REPLACE_OPERATION_V2`
- `EXPO_PUBLIC_ITINERARY_REMOVE_OPERATION_V2`

Dogfood also requires the existing backend preview/commit/read-model exposure
and the IR-13 read shell. Disabling an operation flag removes only that
operation family. A server-denied exposed operation remains visible but
disabled with its server reason.

## Implemented contract

- One typed builder constructs Add, Move/Reorder, Replace, and Remove with
  stable trip/day/block/lineage identity and explicit revision preconditions.
- Manual and Vesper attribution produce the same target, payload,
  precondition, and provider intent. Attribution remains evidence and does not
  fork the semantic operation contract.
- Same-day placement becomes `reorder`; cross-day placement becomes `move`.
  Structured Before/After controls and the accessible gesture control invoke
  the same builder and produce the same payload.
- Add and Replace select catalog-backed venue candidates. No title-only swap or
  placeholder event is submitted.
- Preview renders server-authored Direct, Confirm, Propose, or Denied outcomes.
  Direct and Confirm can commit; Propose is intentionally non-submittable until
  IR-15; Denied never mutates.
- Commit sends the exact normalized preview operation, preview identity/hash,
  idempotency key, and hash-bound confirmation evidence when required.
- Landed state renders the returned receipt and recovery. Undo is exposed only
  when the returned recovery is `undo`, and calls the IR-09 undo endpoint;
  there is no invented remove-only fallback.
- Every IR-14 operation uses `provider_intent=plan_only`. Protected provider
  continuation remains IR-16 work and cannot be implied by this UI.
- Successful commit/recovery invalidates Plan State, Details State, Map,
  itinerary, Folio compatibility, Home cards, and conflicts through the shared
  read-model invalidation boundary.
- The IR-13 Plan shell hides legacy gap/Add mutation affordances while the
  inspect-first read shell is active, so dogfood users do not bypass the
  canonical operation gateway.

## Continuity and typed-object boundaries

The trip-scoped continuity owner retains the exact normalized operation,
construction stage, structural event identity, source typed object, and entry
mode. The draft survives sheet dismissal, object detail, Map/Chat navigation,
stale preview/commit refresh, and restoration of an older return token. A Plan
header chip resumes the exact draft.

Contextual and comprehensive entrances preserve their distinct native return
stacks while resolving the same typed object. Event, stay, and transport
inspection may expose structural Change only when a canonical source event is
known. Expense and provider objects never alias their own action to structural
itinerary Change.

## Convergence evidence

Frontend builder fixtures prove manual and Vesper inputs converge on identical
typed payload, target, revision precondition, and `plan_only` provider intent.
The existing IR-06 backend parity fixture proves equivalent Plan, Map,
Discover, Chat, and Vesper operations share semantic preview identity. The
existing IR-07 and IR-09 evidence remains authoritative for idempotent commit,
one immutable history result, stable receipt identity, and server recovery.

The final paired device/backend dogfood check should run one unprotected
manual operation and the equivalent Vesper-prepared operation against the same
backend fixture and compare normalized operation semantics, receipt, history
identity, and recovery. Vesper preparation/opening itself remains an IR-16 UI
surface; IR-14 supplies the canonical destination it must open.

## Verification

- TypeScript (`npm run typecheck`) — pass
- IR-14 builder, exact-return draft, and typed-object boundary tests — 9/9 pass
- Focused IR-12/13/14 and Plan smoke tests — 23/23 pass
- Flagged Plan smoke with the read shell and all four operation flags — 13/13 pass
- Shared read-model invalidation regression test — pass
- `npm run state-ownership` — pass
- `npm run api-boundaries` — pass
- `npm run accessibility-governance` — pass
- `npm run qa:flags:test` — pass
- Focused ESLint — zero errors
- `git diff --check` — pass

The local backend foundation worktree has the prior executable convergence,
commit, and history tests but its Python test dependencies are not installed in
this desktop environment, so those suites were not redundantly rerun for this
frontend slice. Their committed IR-06–IR-09 evidence is the backend handoff;
the device dogfood exposure check above remains the IR-14 rollout gate.
