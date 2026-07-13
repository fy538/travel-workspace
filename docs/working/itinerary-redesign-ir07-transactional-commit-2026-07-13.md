---
doc_type: working
status: active
owner: backend / frontend
created: 2026-07-13
last_verified: 2026-07-13
expires: 2026-08-12
why_new: Document the IR-07 transactional commit gateway, ledger evidence, and rollout posture.
supersedes: []
source_of_truth_for: [itinerary-redesign-ir07-transactional-commit]
---

# Itinerary redesign IR-07 — transactional commit and minimal ledger

Date: 2026-07-13
Branch: `codex/itinerary-foundation`
Backend worktree: `travel-agent--itinerary-foundation`
Frontend worktree: `travel-app--itinerary-foundation`

## Outcome

IR-07 is implemented behind the independent, default-off
`ITINERARY_OPERATIONS_COMMIT_V2` flag.

The canonical write endpoint is now:

```text
POST /api/trips/{trip_id}/itinerary/operations/commit
```

It consumes the exact normalized operation, `preview_id`, and `preview_hash`
from IR-06 plus a trip-scoped idempotency key and optional confirmation
evidence. The endpoint returns a typed `ir07-v1` terminal result in either
`committed` or `rejected` state.

## Transaction and evidence guarantees

- A PostgreSQL advisory transaction lock serializes each
  `(trip_id, idempotency_key)` pair.
- A trip row lock serializes canonical structural commits within one trip.
- Commit locks and re-reads the trip membership, Vesper delegation,
  participation, block, day, branch, and protected-dependency facts used by
  policy resolution.
- Commit recomputes the IR-06 preview from current facts and verifies both the
  submitted preview identity and semantic hash.
- Principal, capability, revisions, protection, provider facts, and any
  confirmation evidence are revalidated inside the write transaction.
- Structural mutation, the immutable operation row, and terminal transition
  evidence commit atomically.
- Unexpected exceptions roll back both mutation and ledger evidence. A fault
  injected after mutation but before terminal evidence proves this boundary.
- Repeating one idempotency key returns the original operation and visible
  result with `idempotent_replay=true`; it does not append another transition
  or mutate the plan again.
- Reusing an idempotency key for a different preview or reusing an operation ID
  is a typed conflict.
- Policy/stale/unsupported outcomes are persisted as immutable `rejected`
  terminal evidence, so retries remain stable and inspectable.

Committed transition evidence includes the target block before/after state,
every affected revision, sibling sort-order before/after values, attendance
before/after values, confirmation evidence, and actor attribution. That is the
minimum recovery substrate IR-09 will need to decide whether Undo is still
truthful.

## Typed handlers

IR-07 implements plan-only handlers for:

- Add
- Move
- Replace
- Remove
- Set attendance

Remove soft-cancels the plan block and never changes attendance. Attendance
updates the per-user participation record and remains a distinct operation.
Replace resolves the chosen typed entity (`venue`, `site`, `experience`, or
`custom`) and clears stale entity links.

Move now has explicit semantics that were ambiguous in IR-06:

- `time_semantics`: `preserve`, `set`, or `unscheduled`
- `branch_semantics`: `preserve`, `set`, or `main`
- destination day and before/after anchors remain explicit
- a cross-day Move must bind both the destination day revision and a separate
  source-day revision; otherwise it terminates as
  `source_day_precondition_required`

Provider-changing commits remain unavailable in IR-07. A
`plan_and_provider` operation terminates as `provider_commit_not_available`.

## Guarded legacy convergence

When `ITINERARY_OPERATIONS_COMMIT_V2` is off, existing block routes retain
their previous behavior.

When it is on, legacy Add, Move, Remove, and Replace routes adapt into the same
preview-and-commit gateway. They require `X-Itinerary-Idempotency-Key`; the
mobile mutation hooks now generate one stable key per logical mutation and
reuse it across React Query retries. Unsupported legacy shapes fail closed
instead of dropping fields. In particular, Add metadata outside the canonical
Add payload and structural PATCH combinations that do not map exactly to
Replace/Remove direct callers to typed preview.

Legacy confirmation is not fabricated. If current policy requires a
consequence-aware confirmation, the adapter returns the canonical rejected
result and the caller must use typed preview/commit.

## Cache and API integration

- Successful non-replay commits invalidate conflict, Plan State, and home-feed
  read models after the database transaction commits.
- OpenAPI was regenerated at `docs/openapi.json`.
- `travel-app/utils/api/schema.gen.ts` was regenerated.
- The legacy app API interface and HTTP client accept and transmit canonical
  idempotency keys for Add, Move, and Update.
- The commit endpoint remains in the dark-endpoint allowlist until a native
  typed-operation app client is introduced.

## Verification

Focused IR-00 through IR-07 verification:

```text
43 passed
```

This includes real PostgreSQL proofs for atomic Add, idempotent replay,
post-mutation fault rollback, cross-day source/destination revision binding,
Move, Replace, Remove, attendance separation, immutable recovery evidence, and
legacy Move adaptation.

Additional checks:

```text
ruff: clean for all IR-07 backend files
mypy --follow-imports=skip: clean for the three new commit modules/routes
OpenAPI snapshot: fresh
frontend tsc --noEmit: clean
frontend focused tests: 54 passed
disposable PostgreSQL migrations: upgraded through head
```

The broader itinerary glob was `224 passed, 1 failed`; the single failure
expects a pre-seeded venue catalog and therefore fails on the intentionally
empty disposable database.

The full offline backend audit completed with:

```text
11,455 passed, 20 failed, 2 skipped, 594 deselected, 1 xpassed
```

The same 20 unrelated baseline failures remain (including the shared local
database missing the already-built IR-05 decision-owner migration, plus
existing search/booking/home/postcard cases). IR-07 added no new full-suite
failure. Existing global Alembic metadata drift and the pre-existing route/
response-model ratchets also remain unchanged; no IR-07 schema migration was
required because IR-02 already supplied `preview_hash`, trip-scoped unique
idempotency, operation rows, and transition evidence.

## Rollout posture and IR-08 handoff

Keep `ITINERARY_OPERATIONS_COMMIT_V2` off until a dogfood caller uses the native
IR-06 preview and IR-07 commit pair. The legacy adapters are a convergence
safety net, not a substitute for presenting confirmation consequences.

IR-08 can now consume rejected `proposal_required` results and persist the
exact normalized operation plus its immutable creation-policy snapshot. It
must preserve the current distinction between `accepted` and `applied`, rerun
the same commit-time locks/revalidation on acceptance, and never rewrite a
stale proposal in place.
