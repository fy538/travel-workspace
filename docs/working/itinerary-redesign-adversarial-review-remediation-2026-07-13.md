---
title: Itinerary redesign adversarial review remediation
doc_type: working
status: active
owner: backend / mobile / product
created: 2026-07-13
last_verified: 2026-07-13
expires: 2026-08-12
why_new: Record closure evidence for the independent IR-00–17 implementation review without confusing implementation completion with rollout eligibility.
source_of_truth_for: [itinerary-redesign-adversarial-review-remediation]
---

# Itinerary redesign adversarial review remediation

## Outcome

The actionable implementation findings from the independent IR-00–17 review
are closed in code. Compatibility paths remain measured and the IR-17 exposure
and retirement gates remain in force; this review did not advance a rollout
stage or remove a legacy schema, route, or record.

## Closure by authority boundary

### Canonical mutation and Vesper parity

- Selected occurrence writes, concierge Add/Move/Replace/Remove/Undo, and
  concierge pinning now enter the typed canonical preview/commit/history path.
- Durable tool-call identity supplies idempotency. Vesper/chat attribution and
  confirmed human evidence are preserved instead of being rewritten as a
  direct human itinerary action.
- Unsupported mixed legacy payloads fail closed with a typed-preview-required
  result. Unselected trips continue through measured compatibility paths.

### Proposal governance and database integrity

- Accept, reject, supersede, and apply re-resolve the current policy-selected
  decision owner. Trip-owner and first-organizer heuristics are no longer an
  authority source.
- Affected-member decisions require a strict majority of currently planned,
  affected trip members; personal and subgroup ownership remains distinct from
  whole-trip organization.
- Database constraints reject cross-trip proposal, operation, rebase, and
  provider-evidence links. Operation and transition evidence is append-only,
  with only set-once inverse linkage, declared cascades, and account-erasure
  handling allowed.

### History, privacy, deletion, and recovery

- Group history exposes safe structural deltas rather than raw before/after
  snapshots containing notes, participants, booking references, rationale, or
  decision-owner identifiers.
- Deleted human and Vesper authors resolve to one stable anonymous principal;
  account deletion preserves group-safe structural history without retaining
  the deleted account UUID.
- History cursors use `(created_at, operation_id)`, tombstone successor lookup
  is trip-scoped, and Undo degradation checks day revisions as well as block
  revisions. Vesper Undo retains confirmation and attribution evidence.

### Provider, expense, attention, and read-model coherence

- Booking and expense commits invalidate canonical Plan, Details, attention,
  Bookings, provider, history, and Map observers, including bulk hold expiry.
- Provider state remains distinct from plan and expense truth; settled provider
  evidence clears attention without a separate client-authored synchronization
  write.
- Map stop identity and order are now bound to the canonical Plan projection
  version. Legacy-only blocks are excluded when canonical authority is present,
  and the response reports whether every canonical event identity rendered.
- Completed and cancelled entry recommendations never select an unavailable
  completed record; post-trip routing remains controlled by the existing IR-16
  server-authored readiness gate.

### Frontend convergence

- Changes consumes canonical history/unseen/attention data with explicit
  compatibility degradation; typed object detail preserves partial facts and
  linked-object handoffs.
- Details, object, chat, and operation surfaces honor rollout capabilities;
  provider polling and invalidation converge Bookings and Needs Attention.
- The IR-12 client adapter now uses generated history and Plan-authority types.
  Optional response fields are handled defensively instead of being made
  artificially required by a second handwritten contract.

## Landed commits

- Backend provider/history boundary hardening: `a216d5158`
- Backend adversarial review closure: `15da92baa`
- Frontend exact-return groundwork: `bc58c7c0`
- Frontend history/attention/consensus remediation: `bc77e8ab`
- Frontend generated-contract convergence: `c54c6380`

`bc77e8ab` was created during a concurrent frontend lane and includes unrelated
Atlas/persona work in addition to the listed itinerary files. The later
contract commit is itinerary-only; unrelated uncommitted Atlas work was left
unstaged.

## Verification

- Backend focused remediation suite: 110 passed.
- Backend broader itinerary review suite: 352 passed, with one reproducible
  pre-existing expectation mismatch in
  `TestSettleHold.test_expired_deadline_is_not_settled`: production correctly
  returns before claiming an already expired hold, while the old unit test
  expects the claim mock to run. This is not caused by the itinerary changes.
- Ruff check, Ruff format check, diff check, route authorization, import
  boundaries, secret scanning, event parity, and single-Alembic-head checks
  passed. The repository's three documented stale baseline ratchets remained
  skipped during commit.
- Migration `ir18a001 -> ir17r001 -> ir18a001` passed against the IR-17
  PostgreSQL fixture database, leaving one head at `ir18a001`.
- Frontend itinerary verification: 9 suites and 56 tests passed; ESLint and full
  TypeScript passed.
- Combined current-main plus itinerary OpenAPI: 360 paths, 400 operations, 780
  schemas. Generated TypeScript matches the snapshot exactly.

## Remaining gates

No known actionable code-review item remains in this review set. The remaining
work is operational evidence already owned by IR-17: current-schema CI, measured
IR-00 thresholds, selected-cohort shadow/dual-read evidence, on-device visual
and exact-return evidence, provider fault drills, and a rollback drill before
stage advance or compatibility retirement.
