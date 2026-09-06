---
doc_type: working
status: active
owner: Life lane
created: 2026-09-06
last_verified: 2026-09-06
expires: 2026-10-06
source_of_truth_for:
  - Life owner-change delivery consumer contract
  - Capture/graph producer handoff fields
why_new: "Records the first connected consumer package and its cross-lane producer dependency."
---

# Life owner-change delivery handoff — 2026-09-06

## Purpose

This package connects the existing durable Life projection outbox to the
existing shadow index. It does not introduce a second outbox, a new indexing
framework, a Life-owned source writer, a serving cutover, or Atlas deletion.

The path is:

```text
canonical owner transaction
  -> life_projection_outbox (separate downstream journal)
  -> life_projection.ready (after-commit prompt)
  -> life_projection.changed (identifier-only event bus envelope)
  -> current-authority Life fan-in
  -> existing lens/cursor corpus + owner-checked shadow batch
  -> existing revision-CAS index writer
```

The implementation lives across `travel-agent` commits `1bb03e1c7`,
`77d4a8474`, `073d33b9d`, `420176821`, and `a669541b2`. The final two follow-up
packages make semantic representation withdrawal/restore explicit and add the
versioned content-free source-owner lifecycle envelope.
The pure Occasion audience contract is now landed in `travel-agent` commit
`6d4365a83`, and the canonical Occasion producer seam is landed in
`travel-agent` commit `8558d7110`, with direct account-erasure handling in
`a3b0edc84` and `73baf2be2`. The producer still does not authorize an
Occasion serving cutover. The shadow-only Occasion projector and audience
revision adapter are landed in `travel-agent` commit `72950377b`.

## What landed

### 1. Typed consumer envelope

`backend/life_projection/change_events.py` validates the existing
`PendingLifeProjectionEvent` and the identifier-only event-bus payload.

- Viewer scope is mandatory. Producers provide `payload.viewer_ids` as UUID
  strings; a single `payload.viewer_id` and viewer/person `affected_refs` are
  accepted only as replay compatibility.
- `represented_at` is an optional aware ISO timestamp in the payload. If it is
  absent, the durable outbox `created_at` is the read clock.
- Change kinds normalize to upsert, withdrawal, or explicit restoration.
- Owner identity, owner revision, event key, and policy revision are required.
- Raw owner content is never trusted as projection input.

### 2. Current-authority projector

`backend/life_projection/current_authority.py` reads the current graph,
paginated intake anchors/retained sources, and retained timeline rows at one
clock, then builds all four Life lenses through the existing
`build_life_corpus_snapshot` path.

It refuses to materialize a truncated/partial fan-in because missing rows must
not be interpreted as withdrawals. Record-to-owner joins are explicit and
normalize the existing `anchor`/`intake_submission` aliases to the declared
Life owner kinds. Owner families declared unavailable remain excluded rather
than being silently reauthorized by a broad rebuild.

### 3. Shadow delivery behavior

`backend/life_projection/delivery.py` subscribes to
`life_projection.changed` for graph/corpus owners. Retained-source events are
handed to the narrower first adapter in
`backend/life_projection/retained_source_projector.py`, so the generic
consumer and owner-specific adapter do not double-write.

- Active rows use the existing `read_life_index_owner_rows` state and pass the
  exact prior owner revision (or the incoming revision for a first insert) to
  the existing CAS writer.
- A stale/out-of-order upsert projects the current owner read, not the event
  payload, so the newer authority wins.
- A withdrawal waits if the owner is still present at the event revision;
  if the current owner has a different revision, the newer current read wins.
  Removed identities are withdrawn with a keep-set, avoiding a revoke-then-
  reinsert race.
- Ordinary replay never restores a withdrawn row. Restoration requires an
  explicit restore event, a currently authorized owner record, an existing
  withdrawn row, and an exact revision match.
- Unavailable owner families fail closed. Shadow-only families may be rebuilt
  for comparison/materialization, but this does not authorize indexed serving.

The retained-source adapter now has a producer and dedicated current-owner
read: Intake attach/verify/delete paths call the existing
`register_life_projection_propagation` handoff, and the adapter uses the event
clock, previous derived-row revision, withdrawal tombstone, and explicit
restore CAS. Its owner matrix remains `SHADOW_ONLY`; the first adapter is not
completion of Life.

`backend/core/life_projection_broadcast.py` now includes the durable event
clock and optional represented clock in the identifier-only envelope and
returns/defer-fails when the final outbox acknowledgement loses its lease.
The already-landed `backend/workers/life_projection_jobs.py` remains the retry
and prune sweep; no duplicate worker was added.

## Exact producer contract for Capture / graph owners

Capture or an eligible graph owner should call the existing
`register_life_projection_propagation(conn, ...)` while its own transaction is
open, after its own source mutation and authority/revision checks have passed.
The retained-source producer is now landed by the adjacent Capture commit;
Life does not invent additional source transactions in this lane.

Required fields:

| Field | Contract |
|---|---|
| `event_key` | Stable, idempotent owner-event identity; unique in the Life outbox |
| `owner_kind` | A declared Life owner (`retained_source`, `plan`, `occasion`, `outcome`, etc.) |
| `owner_id` | Canonical owner identity, opaque to Life |
| `owner_revision` | Exact owner revision/sequence used by the mutation |
| `change_kind` | Any owner verb; consumer maps withdrawal/restore aliases explicitly |
| `policy_revision` | Audience/authority policy version used by the owner |
| `payload.viewer_ids` | UUID strings for every viewer whose Life projection may change |
| `payload.represented_at` | Optional aware ISO clock for deterministic replay |
| `affected_refs` | Identifier/revision-only refs; never raw source text or secrets |

The producer must enqueue the Life event in the owner transaction, but the
after-commit event-bus prompt is only a latency optimization. A missed prompt
must be repaired by the existing Life outbox worker. The event must not reuse
Intake's single acknowledgement or be inferred from a presentation/card ID.

Current repository evidence: retained-source producer call sites exist in
`backend/core/db/intake_v2.py` for source attach, source verification, and
source deletion. Occasion producer call sites now cover creation, accepted
membership (including the handoff bridge), leave, organizer transfer,
lifecycle transitions, and reconciliation-driven lifecycle changes. They all
compute the composite audience revision and fan out to the before/after viewer
union inside the owner transaction. The direct account-erasure path now
snapshots the pre-erasure audience and journals surviving shared Occasions
after the generic membership sweep in `travel-agent` commits `a3b0edc84` and
`73baf2be2`; solo Occasions are skipped before their owner cascade. Graph Plan
and Outcome producers are still absent. The remaining dependency is to
review/land the graph owner contract, not to invent a second Capture
transaction or a Life-owned source writer.

## Verification

Focused local evidence on the isolated Life lane:

- 103 tests passed across Life projection, retained-source adapter,
  current-authority/shadow delivery, CAS/withdrawal/restore, outbox bridge,
  propagation, and worker suites.
- `ruff check` passed for all touched backend/test files.
- Existing pre-commit checks passed except the repository's time-decayed
  broad-exception and size-budget ratchets; those counts were already over
  their frozen baseline before this package. The package added no broad
  `except Exception` handler and passed the status-write guard after adding an
  explicit source-status predicate.

The local PostgreSQL database is now migrated through `lifeoutbox01`. The
combined focused suite passes 42 tests, including 17 PostgreSQL-backed
bridge/intake tests. These checks prove the local transaction/schema path only;
no production activation, reader cutover, or device test is claimed.

The Occasion contract/producer package adds 48 command and helper tests, and
the combined Life/Occasion focused suite passes 81 tests. Two additional
PostgreSQL tests now cover membership fan-out and account-erasure handoff; the
local producer suite passes 2/2. The producer package was committed as
`8558d7110`, account-erasure handling as `a3b0edc84` and `73baf2be2`, and the
PostgreSQL proof as `cf2988abd`; focused format/lint checks pass. These numbers
prove the transaction wiring and pure contract only; no serving read or
production activation is claimed.

The shadow-only projector and audience-revision adapter are committed as
`72950377b`; three projector tests and the subscriber-wiring suite pass. This
package validates current-authority re-read, exact revision matching, and
departure withdrawal in pure tests; the remaining Postgres projector exercise
is now smoke-verified against a real Occasion and `life_corpus_entries`, but
remains a checkpoint, not a serving-read approval.

## Next checkpoint

1. Run the existing worker against a fixture retained-source event and verify
   the exact shadow row, stale replay, withdrawal, and explicit restore
   transitions end to end.
2. Extend PostgreSQL transaction coverage to lifecycle, organizer transfer,
   reconciliation, and handoff acceptance (membership fan-out and account
   erasure are now covered).
3. Exercise the landed Occasion projector against Postgres current-authority
   reads: member departure, role transfer, stale replay, withdrawal, and
   restoration, without enabling serving cutover. The projector is registered
   in the canonical event-subscriber bundle but remains shadow-only.
4. Expand owner coverage one family at a time by updating the owner matrix and
   adding owner-specific authority/audience tests. Do not mark Life complete or
   cut over readers after the first adapter.

The canonical roadmap and execution status remain the forward register; this
handoff is the package receipt and cross-lane interface, not a competing plan.
