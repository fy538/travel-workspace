---
doc_type: working
status: active
owner: founder / backend / frontend / product operations
created: 2026-07-14
last_verified: 2026-07-16
expires: 2026-08-13
why_new: Record the pre-launch founder ruling to adopt the canonical itinerary operation gateway as the only mutation path, and plan the legacy deletion + dogfood-data rewrite in executable detail.
supersedes: []
source_of_truth_for: [itinerary-legacy-retirement-cutover-plan-2026-07]
---

# Itinerary Legacy Retirement — Pre-Launch Cutover Plan

## Founder ruling (2026-07-14)

The product is pre-launch with zero external users. Therefore:

1. The canonical itinerary operation gateway
   (`POST /api/trips/{trip_id}/itinerary/operations/preview` + `/commit`)
   becomes the **only** itinerary mutation path.
2. Legacy mutation code is **deleted**, not kept as adapters. No old-client
   compatibility, no gradual per-trip enrollment, no governed observation
   window on live traffic.
3. Dogfood data is **wiped and reseeded** through the canonical path so seeded
   trips carry a real operation ledger, history, and recovery capability.

This ruling supersedes the rollout/retirement **posture** of
[`itinerary-redesign-implementation-plan-2026-07-13.md`](itinerary-redesign-implementation-plan-2026-07-13.md)
and the "intentionally blocked on representative live evidence, an approved
policy threshold, and the governed observation window" language in
[`itinerary-redesign-final-local-closure-evidence-2026-07-14.md`](itinerary-redesign-final-local-closure-evidence-2026-07-14.md).
It does **not** change the target architecture, contracts, invariants, or the
IR-00 mutation inventory — those remain governing. The migration rules in
IR-00 §Migration rules still apply, except rule 5 (old-client compatibility)
which is now moot.

Deletion still requires proof gates (below). "Pre-launch" removes the *live
user* constraint; it does not remove the requirement that the canonical path
demonstrably works before the only working code is deleted.

### Required end state

The cutover is complete only when all of the following are simultaneously true:

1. One normalized operation contract represents every product itinerary
   mutation, including planner birth/replan, human and Vesper edits, proposals,
   branch topology, history, and recovery. Provider-domain events link to that
   operation evidence without being mislabeled as itinerary plan mutations.
2. One server-authored preview/policy/commit authority decides and lands those
   mutations. No route, agent tool, planner, proposal workflow, seeder, or client
   can independently alter itinerary truth.
3. The reworked Itinerary frontend is the only mutation experience. Trip Home,
   Map, Trip Details, Changes, and Folio consume canonical itinerary projections;
   they are not competing itinerary authorities.
4. Every retained compatibility table, column, module, or projection is
   read-only with respect to itinerary truth, has a named consumer and owner,
   and has an explicit retain/rename/retire disposition. Retention is not an
   implied second mutation system.
5. CI and runtime evidence make legacy-writer regrowth detectable and
   fail-closed. A retained operational kill switch may make itinerary writes
   unavailable; it must never fall back to legacy mutation code.

This plan is the functional consolidation and deletion cutover. Full visual
polish of the reworked Itinerary × Trip Home/Folio product surface may continue
afterward, but it must build on this single canonical authority rather than
preserving the old itinerary underneath the new design.

## Current state (verified against code, 2026-07-16)

### 2026-07-16 closeout reality check

- C1/C2/C3 implementation has landed: dogfood itineraries now enter through
  deterministic canonical replay, itinerary birth has authored chronology,
  resets respect append-only ledger boundaries, and authored proposals are
  created through the canonical proposal gateway. The old raw itinerary and
  proposal insert sites were removed from `tools/dogfood/content/seed.py`.
- B1 remains green. The backend full-on cert passed 458 + 409 tests under the
  asserted `full` / all-trips / 20-capability posture. Frontend typecheck and
  lint pass (warnings only), and its blocking deletion-reference scan reports
  zero production legacy callers.
- A frontend cutover leak found during this review was fixed: Plan's day rail
  now derives its changed-day markers from canonical operation-history receipts
  and targets, not `recent_change_ids` / legacy day changes.
- The retired Folio and Change Studio transport surfaces are now physically
  removed in both repositories. This includes the backend Folio/read-model
  package, old edit preview/commit routes, frontend Folio components, mock
  clients, generated schemas, query persistence, cache invalidations, and the
  obsolete plan-edit idempotency table (with a drop migration).
- `plan_events` is now a frozen, read-only compatibility ledger: canonical
  commits no longer mirror manual edits, proposal lifecycle writes are gone,
  and the module exposes no product write API. Historical rows remain for
  retention, privacy erasure, and archive sign-off. Proposal resolve/revert
  now use only the canonical proposal gateway; the
  unreachable duplicate route body and the independent
  `core/db/proposal_apply.py` mutation/revert engine are deleted. Proactive
  supersession also resolves through canonical authority.
- The planner execution boundary no longer imports or exposes its dormant
  `persist_planning_output` fallback. Materialization and replanning continue
  through their typed canonical operations.
- Provider booking/restaurant/handoff projection writes now pass through a
  source-validated, revisioned gateway. Deferred planning enrichment is also a
  named active-head-guarded annotation gateway rather than a structural writer.
  The raw `update_block`, `reorder_blocks`, and bulk sort-order helpers are
  deleted; canonical operations and provider projection now own those changes.
  `create_itinerary_version`, `create_itinerary_day`, and `create_block` are
  also deleted. Scenario, certification, and test setup now materialize and
  replay canonical operations; structural legacy itinerary-birth writers are
  zero.
  The obsolete itinerary edit-log producer is gone; historical preference rows
  remain readable/drainable while canonical committed human catalog Replace
  operations produce idempotent preference-observation receipts. The one
  remaining legacy-product writer only acknowledges that finite deployed
  edit-log backlog and is removed after its drain is proved.
- Static boundaries are green after exact-scope classification and ratcheting:
  141 backend writer sites remain classified (including **1
  `legacy_product` site**), 19 legacy imports remain classified (**8
  `replace`, 7 `delete`, 4 `rename`**), and backend compatibility readers are
  **0**. Product readers now use the explicitly named itinerary decision,
  planner-context, and feasibility-projection owners. Green means “no unreviewed
  growth”; it does not mean those legacy rows are retired.
- No B2 lane is formally licensed. A deterministic local refresh records the
  focused canonical exercises across all five lanes, but these are local test
  exercises—not deployed producer traffic. Every lane still lacks an
  identifiable Fly revision, an observation window, per-surface traffic,
  canonical commit/proposal counts where required, deployed artifact/caller
  absence scans, rollback evidence, evidence references, and signatures.
  Compatibility branches deleted before an emitter existed use deployed
  unreachability proof; their compatibility count remains null rather than a
  fabricated zero. Pre-launch physical
  deletion nevertheless started where static reachability and canonical
  journey coverage proved the old authority dead. The evidence bundle therefore
  documents the sequencing exception rather than retroactively licensing it,
  and B2/B3 cannot be claimed complete.
- C4 local five-pack reset/reseed is complete and reproducible: canonical
  substrate checks and TestClient API exercises cover deterministic identities,
  authored chronology, committed operation history, occurrences, proposals,
  recovery, cross-domain references, Discover, briefs, and Atlas. Authored
  labels without a promoted corpus identity remain honest labels rather than
  fabricated venue/site references. Fly backup/reset/reseed and deployed
  certification remain unperformed.
- Stored `plan_editing='locked'` compatibility is retired end to end. The new
  migration normalizes it to Review and narrows the physical database, backend,
  OpenAPI, generated TypeScript, mocks, scanners, and product documentation to
  `open | review`. Two unreachable writer APIs and the duplicated plan-state
  `raw_status` field are also physically deleted.
- The dead legacy block move/remove/undo editor, itinerary-version pruning
  worker/CLI, and proposal `in_revert` claim/reaper are retired. Canonical
  operation recovery remains authoritative; a migration normalizes any stranded
  transient proposal row to Accepted with explicit recovery evidence before
  narrowing the database constraint.
- Proposal voting now row-locks and writes only through the canonical
  operation-proposal gateway; the old independent vote writer is deleted. The
  unused planner `persist_planning_output` / `fork_itinerary_version` facade is
  also deleted while live planning reads, feasibility warnings, and deferred
  enrichment remain intact.
- The generic itinerary-version hard-delete helper is gone; journey teardown
  now owns a trip- and marker-scoped fixture cleanup boundary. Map route-point
  persistence is isolated as a validated derived-cache gateway reachable only
  from map-state enrichment, rather than masquerading as a product edit writer.
- The legacy proposal write engine is now physically retired. Canonical
  proposal creation owns privacy-safe lifecycle transitions, same-stop
  supersession, trust receipts, automatic-resolution attribution, and atomic
  replan withdrawal of both operation-backed truth and its temporary
  group-facing projection. The old create/build/supersede/resolve/expiry
  helpers and their writer-only tests are deleted; `change_proposals.py` is a
  read/deadline projection module only. Journey certs, scenario fixtures,
  replay/eval spies, and concierge tests now enter through canonical producers.

The sections below retain the 2026-07-14 wiring trace as the audit baseline;
use this closeout block and the executable guards for current status.

### Current gating posture (2026-07-16)

The per-trip stage/cohort/capability rollout selectors and their modules are
deleted. The only retained boundary is the global fail-closed
`ITINERARY_OPERATIONS_ENABLED` switch. Disabling it rejects canonical writes;
it cannot select or resurrect a legacy writer.

The wiring table below records the historical 2026-07-14 starting point, not
the current product graph.

### Legacy mutation-path wiring (historical trace of 2026-07-14)

| # | Path | State | Capability / flag | Writes DB today |
|---|---|---|---|---|
| 1 | `plan_edit_preview.py:114` | pure-legacy (read-only) | none | no |
| 2a | `plan_edit_commit.py:438` `_apply_direct` | pure-legacy | none | yes |
| 2b | `plan_edit_commit.py:504` `_stage_proposal` (gate :552) | dual-path | `proposals` | yes (legacy) |
| 3a | `trips.py:1809` `update_itinerary_block` (gate :1872) | dual-path | `commit`+`remove`/`replace` | yes (legacy) |
| 3b | `trips.py:1979` `mark_itinerary_block_booked` | pure-legacy (telemetry only) | `provider_saga` tracked, not gated | yes |
| 3c | `trips.py:2058` `undo_itinerary_block_edit` | pure-legacy | none | yes |
| 3d | `trips.py:2107` `undo_planning_revision` | pure-legacy | none | yes |
| 3e | `trips.py:2906` `move_itinerary_block` (gate :2929) | dual-path (canonical branch partly hollow, :2955) | `commit`+`move` | yes (legacy) |
| 3f | `trips.py:3133` `add_itinerary_block` (gate :3154) | dual-path | `commit`+`add` | yes (legacy) |
| 3g | `trips.py:2232` `pin_experience_to_itinerary` (gate :2314) | dual-path | `commit`+`add` | yes (legacy) |
| 3h | `trips.py:3384` `optimize_day_route` | pure-legacy (preview → N client moves) | none | preview only |
| 3i | `trips.py:514` `patch_trip` | pure-legacy — **out of scope** (trip settings, per IR-00) | none | yes (trips table) |
| 4 | `concierge/tool_handlers/planning/_plan.py` (~:1808, :1843) | **pure-legacy — the birth path** | none | yes |
| 5 | `planning_agent/replan_merge.py:96` | pure-legacy (in-memory; persistence downstream) | none | no |
| 6 | `concierge/tool_handlers/itinerary_edit.py` update/move/add/undo (gate `_canonical_write_enabled:54`) | dual-path (all 4) | `commit`+dynamic; undo→`history` | yes (legacy) |
| 7 | `concierge/tool_handlers/itinerary.py::_execute_pin_experience` (gate :353) | dual-path | `commit`+`add` | yes (legacy) |
| 8 | `core/db/change_proposals.py:49,:261` (creation) | **pure-legacy** | none | yes |
| 9a | `proposals.py:471` `resolve_proposal` (gate :502) | dual-path (canonical-created proposals only) | `proposals` | yes (legacy) |
| 9b | `proposals.py:805` `withdraw_proposal` | pure-legacy | none | yes |
| 9c | `proposals.py:861` `revert_proposal` | pure-legacy | none | yes |
| 9d | `core/db/proposal_apply.py:238` `apply_accepted_proposal` | pure-legacy | none | yes |
| 10a | `proposal_automation.py` resolution (gate :437) | dual-path | `proposals` | yes (legacy) |
| 10b | `proposal_automation.py` creation (:1067, :1427) | pure-legacy | none | yes |
| 10c | `concierge/proactive.py` creation | pure-legacy | none | yes |
| 10d | `planning/_propose_present.py:469` creation | pure-legacy | none | yes |

Capabilities `optimize_day`, `replan`, `branches`, and `writeback` are wired
through the rollout capability map and have backend and/or frontend flag
readers. What remains unproved is complete producer adoption and exercised
canonical-only behavior for each capability.

In that 2026-07-14 snapshot, no legacy path was retired. The current closeout
block above and executable ratchets supersede that state.

### Historical dogfood seeding mechanics (2026-07-14)

`tools/dogfood/content/seed.py` (2,870 lines) writes itineraries as raw SQL
(`pg_insert` into `itinerary_days`/`itinerary_blocks`,
`_seed_itinerary:673`), bypassing all business logic. All IDs are
deterministic via `stable_uuid(dogfood_key, ...)`; cross-domain seeders
(`seed_expenses.py`, `seed_atlas_artifacts.py`, booking proposals via
`create_booking_proposal`) depend on those IDs. Seeded trips have **no**
operation ledger, history, receipts, or recovery capability.

Current dogfood birth and proposal setup uses canonical materialization and
replay with deterministic cross-domain identities. Scenario tools fail closed
when asked to layer partial setup onto incompatible canonical history.

---

## Workstream 0 — Establish the retirement boundary before migration

This lands first. It prevents new legacy writers from appearing while the
cutover is underway and turns the current trace into a complete, ratchetable
inventory rather than a point-in-time route list.

### 0.1. Classify every itinerary writer and proposal consumer

Run a repository-wide static scan for all writes to `itineraries`,
`itinerary_days`, `itinerary_blocks`, branch/participation tables, proposal
apply state, and operation/history tables. Classify every result as:

- **product mutation — migrate/delete**: routes, planners, agents, proposal
  automation, and app-facing service functions that can change plan truth;
- **canonical writer/recovery — retain**: the one gateway and its proven
  recovery implementation;
- **integrity/administrative maintenance — explicit exception**: membership
  departure, account deletion, archival, derived feasibility warnings, and
  similar behavior that does not represent an itinerary-edit intention;
- **seed/test/scenario setup — migrate or isolate**: production-like dogfood
  must use canonical replay; disposable test fixture setup may use a narrowly
  documented direct-write boundary.

Separately inventory every reader of `change_proposals`, `plan_events`, legacy
recent changes, and compatibility columns. Each receives a retain, replace,
rename, or delete disposition before its module is import-banned.

### 0.2. Land ratcheting guards

- Add a CI static import/write-boundary checker before producer migration.
  Initially allowlist every classified legacy writer; remove entries one lane
  at a time until no product mutation exception remains.
- Add a transactional invariant test for canonical commits: mutation evidence,
  operation record, transitions, history/recovery facts, and materialized plan
  state commit or roll back together.
- Do not pretend a source-level SQL checker can infer that an arbitrary block
  update has a corresponding operation. Enforce module/service boundaries in CI
  and prove transactionality in database tests. If a hard database-level writer
  provenance mechanism is later adopted, specify it separately.
- Every integrity/administrative exception must be named, tested, and incapable
  of being called as a normal product edit path.

Acceptance: the inventory accounts for every direct writer and legacy read-model
consumer; the guard is green with an explicit nonzero migration allowlist; each
subsequent deletion lane ratchets that allowlist downward.

Historical execution status (2026-07-14): the two static boundaries are landed locally and
green. After the A1-A3 producer additions and ratchet reductions, the writer
manifest classifies 130 stable sites / 150 occurrences (89 canonical, 28 legacy
product, 7 integrity, 21 seed/scenario, 5 migration). The consumer manifest
classifies 105 legacy imports (63 replace, 21 delete, 21 rename). Both are wired
into the local `gates` target and backend CI. The
canonical fault-injection test now proves plan revisions, operation/transition
evidence, the temporary legacy event mirror, and projected history roll back
together. The six integrity keys are a closed code-level allowlist rather than
free-form manifest labels. A semantic compatibility ratchet now covers 14
backend file/resource pairs / 63 uses and 20 frontend pairs / 83 uses across
legacy recent changes, raw status, planner `persisted_version`, `locked`
governance, and Folio compatibility inputs. The integrity exceptions' five
callable entry points are restricted to named lifecycle importers in CI, and the
focused reachability/authorization/lifecycle suite is green (**54 passed**).
Workstream 0 is complete.

Current status (2026-07-16): inventory and CI ratchets are complete and green at
141 writer sites, 19 retained compatibility imports, and 0 compatibility
readers. Zero legacy-product writers is not yet complete: the sole remaining
site is the finite `itinerary_edit_log` drain acknowledgement described above.

## Workstream A — Build the missing canonical producers

These block everything else. No flag flip makes the gateway the sole writer
while the birth path is legacy.

### A0. Make `materialize_shape` a real commit operation (critical blocker)

- Today: `materialize_shape` exists in the operation model, preview/policy, and
  rollout mapping, but the commit gateway does not support it. Its payload only
  carries destination and dates; it does not define deterministic itinerary/day
  identities or the complete first-draft transaction.
- Contract: one normalized `materialize_shape` operation turns one immutable,
  accepted shape revision into the complete first tentative dated draft. Extend
  the payload or server-authored normalization result to carry/reference the
  exact accepted shape snapshot, dated day identities, initial block/anchor
  placement, stable lineage, participation/ownership, and provenance.
- Atomic boundary: itinerary identity, ordered days, initial blocks/anchors,
  revisions, attribution, ledger evidence, history, and recovery posture commit
  in one transaction under one operation ID and produce one visible history
  item. No empty dated itinerary or partially added first draft may become
  visible. Later user-authored additions remain ordinary `add` operations.
- Identity semantics are canonical, not seed-only: derive itinerary/day/block
  identities deterministically from canonical operation/shape inputs, or make
  caller-supplied identities ordinary validated fields of this operation. The
  route and replay orchestrator must execute the same normalized contract.
- Prove idempotent retry, duplicate birth, stale shape/date input, partial-fault
  rollback, undated→dated transition, and operation/history projection.
- Acceptance: one committed `materialize_shape` creates the complete,
  deterministic first dated itinerary through the canonical gateway, preserving
  accepted anchors/provenance; no separate initial Adds or direct day/version
  writes are needed; all fault points roll back both plan truth and evidence.

Execution status (2026-07-14): **A0 complete** in Travel Agent commit
`5fca67070`. The normalized payload now carries validated caller-supplied
itinerary/day/block identities, exact contiguous dated-day coverage, initial
blocks, stable lineage, participation/ownership, structural roles, scheduled
times, and accepted-shape provenance. Preview rejects missing/already-used
shapes, destination/date drift, non-member participants, invalid catalog
entities, and any trip that already has an itinerary. Commit locks the trip and
shape, then creates the itinerary, days, blocks, canonical participation,
undated→dated trip transition, shape materialization state, immutable operation
evidence, and one history projection in a single transaction. PostgreSQL proof
`test_itinerary_materialize_shape_gateway.py` covers complete birth,
caller-supplied identity preservation, fault rollback before terminal evidence,
same-key idempotent replay, duplicate-birth rejection, stale-date rejection,
and one visible history item. Focused A0 + gateway/policy/preview verification:
**62 passed**. A1 remains responsible for making the planner emit this contract;
A0 does not yet retire the planner's direct persistence path.

### A1. Plan generation → typed operations (critical path)

- Today: `_plan.py` persists complete itinerary versions directly;
  `replan_merge.py` produces merge output outside the canonical resolver;
  `ITINERARY_OP_REPLAN_V2` is unread.
- Build: after A0, first planner draft emits one complete
  **`materialize_shape`** operation; subsequent planner output emits atomic
  **`replan`** with ordered child operations (IR-11 contract). Carry over the
  preservation-first expected-head compare-and-swap from
  `planning_agent/FEATURE.md` as the replan guard — a late-finishing planner
  must not overwrite newer user edits.
- Specify the deterministic planner-output diff: Add/Move/Reorder/Replace/Remove,
  manual/protected-anchor preservation, stable lineage, maximum child count, and
  large-itinerary behavior. Branch-topology changes are not currently valid
  atomic children; either extend the compound contract with explicit topology
  semantics or emit linked topology operations outside the replan transaction.
- Migrate the legacy persistence result contract, not only its write call.
  `_plan.py` currently uses the returned itinerary version/id/block mapping for
  plan events, proposal cleanup, feasibility warnings, planning progress,
  conversation receipts, and asynchronous enrichment. Define one canonical
  planner-commit result carrying the surviving itinerary/head/block identities;
  rebind each downstream consumer to operation/history/projection truth, retire
  obsolete version-number and `plan_events` assumptions per D1, and preserve the
  intended transactional versus best-effort side-effect boundaries.
- Acceptance: a trip created via chat → planner → itinerary has an
  `itinerary_operations` ledger from birth; `_plan.py` contains zero direct
  block/version writes and no downstream consumer depends on a legacy
  `persisted_version`; replan produces deterministic diff operations, never a
  full-version replacement; a stale planner result fails without overwriting a
  newer human or Vesper edit; receipts/progress/enrichment still close correctly.

Execution status (2026-07-14): **A1 complete.** Travel Agent commits
`0d0ffa1b8`, `c529b8d5f`, and `bc394b268` land canonical first birth; commits
`618ec93e4`, `ed6d49a0b`, `110c730ec`, `5c854b2c7`, and `8188c7d93` land and
adopt canonical replan. A first planner result creates or reuses one accepted
shape and emits one complete `materialize_shape` operation, including
contiguous dated days, stable deterministic itinerary/day/block identities,
group participation/ownership, anchors, reasoning, narratives, transitions,
price-estimate provenance, fidelity, and workflow provenance. Subsequent
planner output compiles deterministically to one atomic `replan` containing
ordered Add/Move/Reorder/Replace/Remove children; unchanged output is a no-op,
the child limit is bounded, and omission of a manual, anchored, confirmed,
booked, or branch-bound block fails closed. Add/Replace carry the full
planner-visible block content, and Replace can atomically reposition a block so
one compound never targets the same block twice.

The planner captures a revision fingerprint over the current day/block
projection before synthesis and requires that exact head inside the durable
workflow transaction. A human or Vesper edit that lands while planning is in
flight therefore rejects the late output without overwriting the newer edit.
The workflow checkpoint and canonical commit share one transaction. Existing
itineraries are mutated in place through operation evidence; replans no longer
call `persist_planning_output` or create replacement versions. The post-write
confirmed-booking copier and its `plan_events` mirror were deleted; protected
blocks are preserved by the atomic diff itself. Legacy version-pair Undo is no
longer emitted for replans—history/recovery belongs to the operation ledger.
The planner result contract now exposes operation ID, mutation kind,
changed/no-op state, itinerary ID, and compatibility projection version; no
planner/response consumer retains the `persisted_version` semantic. Focused
compiler/gateway proof is green (**23 passed**); the final planner,
persistence, durable-workflow, authority, response, and replan regression suite
is green (**91 passed**).

### A2. Proposal creation goes canonical

- Before A2: creation was legacy across four producers (`change_proposals.py`,
  `proactive.py`, `_propose_present.py`, `proposal_automation.py` creation
  half). Resolution adapters (`proposals.py:502`,
  `proposal_automation.py:437`) only fire for proposals that are already
  canonical — so the gateway never owns a proposal end-to-end.
- Build: all four producers persist the exact normalized operation plus an
  immutable creation-policy snapshot (IR-08). Pre-launch: **no** in-flight
  legacy-proposal backfill — reseed handles existing data.
- Acceptance: every proposal row created in dev satisfies
  `get_itinerary_operation_proposal(...) is not None`; resolve/withdraw/revert
  flow through canonical transitions.

`change_proposals` is currently also the group-facing proposal read projection.
A2 retires its independent construction/apply authority; it does **not** delete
the projection or its reader API by implication. The 0.1 consumer inventory must
decide whether to retain and rename that projection or replace its consumers
before B3 can delete/import-ban the module.

**Executed 2026-07-14.** All product proposal producers now construct an exact
normalized operation and call the canonical proposal gateway. This includes
feasibility catches, venue-disruption swaps, exact chat add/swap/reschedule/
remove requests, and Change Studio plan edits. Generic or incomplete chat
“modify” intent fails closed instead of minting an ambiguous proposal. Manual
organizer resolution, vote/deadline automation, author withdrawal, acceptance
and application now use canonical proposal transitions; organizer revert
commits one typed inverse of the applied operation with a stable idempotency key
instead of restoring a whole itinerary version.

The compatibility boundary is deliberate: `change_proposals` remains the
group-facing read projection owned by the itinerary proposal gateway and read
by proposal API, Home/Plan, concierge receipt/notification, and frontend
proposal consumers. It has no product construction or itinerary-apply
authority: the legacy create/build/supersede/resolve/expiry helpers and the
legacy apply module are physically deleted. Canonical replan withdrawal closes
operation truth and the projection atomically, and canonical creation preserves
the product invariant that a newer suggestion supersedes an older open
suggestion on the same stop. The closeout regression suite is green (**134
passed**), while the deletion-license proposal lane records **24 passed** local
canonical exercises. Remaining lane-3 work is the deliberate rename or
replacement of projection readers—not removal of a hidden mutation fallback.

### A3. Remaining producers (parallelizable after their contracts are explicit)

| Item | Replaces | Notes |
|---|---|---|
| Atomic `optimize_day` | `trips.py:3384` preview + N client moves | server-side child moves, one recovery |
| Manual `mark_booked` attestation | `trips.py:1979` | A human report that an external handoff was completed is not provider proof and is not a structural itinerary edit. Define the D5 authority/evidence contract, persist a canonical linked booking-domain event with `user_reported` truth, and prove idempotency/privacy. Never label it provider-confirmed. |
| Held-provider confirmation adoption | existing canonical `/provider-sagas/held-confirmation` | Keep the existing controller-authorized protected-dependency saga and external result path distinct from manual attestation. Migrate frontend/agent callers and prove pending/success/failure/manual-action recovery; do not invent a second held-confirmation contract. |
| REST undo → `OperationRecoveryCapability` | `trips.py:2058`, `:2107` | concierge undo adapter (`itinerary_edit.py:971`) is the template |
| Verify `branches` producers | — | gateway types and flag readers exist; prove every create/update/dissolve producer and recovery path, including frontend construction and replan interaction |

#### A3 execution evidence (complete 2026-07-14)

- `optimize_day` now returns a server-authored compound-operation preview and
  the client commits or proposes that exact operation once. The former N-call
  partial-move apply path is gone; one compound operation owns recovery.
- Manual `mark_booked` now goes through `booking_attestation_gateway`. Only the
  protected-dependency controller or the explicitly stamped handoff actor may
  act. The block projection records `state=user_reported_booked` and
  `truth_source=user_reported`, while one immutable
  `booking.user_reported_completed` event stores attribution without deep
  links, phone numbers, provider references, or confirmation secrets. Replays
  are serialized and idempotent. Provider-confirmed truth remains a different
  terminal state and is rendered differently in the app.
- The frontend operation gateway now calls the existing
  `/provider-sagas/held-confirmation` contract directly. The booking-agent
  provider executor remains its only money/provider continuation; pending,
  confirmed, failed, repriced, expired, retry, and manual-action states remain
  visible through the canonical saga/history projections. No second held-
  confirmation contract was added.
- Both REST undo entry points resolve a canonical committed operation and call
  `undo_itinerary_operation`; planning cards carry the exact `operation_id`.
  Whole-version restore is no longer a reachable REST mutation strategy.
- Branch create/update/dissolve construction is present in
  `LowRiskOperationSheet`/`ParallelPlanEditor`; compound gateway coverage proves
  recovery and replan interaction. No additional branch writer was needed.

Evidence commits: backend `9b7116e9f`, `eae54e0ea`, `0c30db23b`,
`64ea203b8`, `e45594b86`; frontend `3498cfc0`, `8ab935ea`, `e52c090f`, `31b2497c`;
workspace contract snapshot `ac6536c`. Focused certification is green: 98
backend tests (including optimize, compound/branches, REST recovery, manual
attestation, held-saga route/gateway/executor) and 56 frontend tests, plus
frontend TypeScript validation. A broader `test_trips_api.py` run also exposed
four pre-existing trip-detail/map test mocks returning 404; they are outside A3
but must be green before B1 can be checked.

## Workstream B — Flip, prove, delete

### B1. Flip everything on (dev/local + CI)

`ITINERARY_ROLLOUT_STAGE=full`, cohort = all trips, and every registered
itinerary capability flag true.
Run the named itinerary suites plus the complete journey/persona certifier set
from the canonical journey registry against this posture. The previous closure
evidence's 790 distinct tests are a non-regression baseline, not a permanent
exact count; this cutover must add tests. Fix breakage before proof begins.

The test command must assert the intended environment at startup so a false/off
default cannot make a nominally green suite exercise only compatibility code.
Each mutation producer in the 0.1 inventory must have at least one canonical
success exercise and its relevant denied/conflict/recovery exercise.

Completion evidence (2026-07-14):

- `travel-agent/scripts/certify_itinerary_full_on.py` installs and asserts
  `stage=full`, cohort `all`, and all 20 registered backend capability flags
  before it launches a child command. `make itinerary-full-on-cert` is the
  repeatable local/CI entry point; CI also wraps both persona gates in the same
  asserted environment.
- The two named backend corpora pass under that posture: 447 tests in the
  itinerary/lifecycle/API/audit corpus and 406 tests in the adjacent
  Plan/proposal/folio/map/trip/writeback corpus (853 total executions). Tests
  that intentionally prove a retained compatibility branch now disable the
  specific capability explicitly instead of inheriting an ambient dark flag.
- `travel-app/scripts/certify-itinerary-full-on.mjs` installs and asserts all
  13 frontend itinerary flags. The named frontend itinerary corpus passes 51
  suites / 376 tests under that posture and is a blocking CI step.
- The complete real-persona registry passes under the asserted backend posture:
  mara 11/11 and elif 4/4, with zero failures and zero skips. The run corrected
  stale J01 private-to-group conversation expectations, made J08 create its
  explicit itinerary scaffold, and moved J05 onto the canonical proposal
  producer/resolver path.
- Breakage found and fixed during proof included destination-wall-clock proposal
  rescheduling incorrectly inheriting the database session timezone, dogfood
  trips missing their canonical itinerary decision owner, four stale trip API
  mock targets, and frontend full-on mocks/fixtures that omitted canonical
  history, operation-gateway, completed-entry, and provider-recovery fields.
- CI now proves the full-on posture independently of ordinary default-off test
  runs in both repositories. This is B1 proof only; B2 still requires measured
  nonzero canonical traffic and zero compatibility events per deletion lane.

### B2. Prove zero legacy traffic (the deletion license)

Run the full journey certifier + Maestro wedge flows (J04/J05/J10 device flows).
Compatibility-event evidence is valid only for a path with complete, named
instrumentation coverage. Branches deleted before an emitter existed instead
require deployed unreachability proof from the same identifiable revision as
the static proof; their event count remains null.

Every deletion lane requires a signed evidence row containing all of:

1. every producer and frontend/agent/planner/seeder entry surface assigned to
   the lane was exercised;
2. the exercise count and canonical commit/proposal count are both nonzero;
3. either completely instrumented named paths report zero compatibility events,
   or lane-specific symbol, deployed-artifact, and caller scans prove the
   deleted paths unreachable on the deployed revision;
4. the static writer/import allowlist was ratcheted and is green;
5. repository route/reference scans show no migrated frontend, agent, planner,
   seeder, job, or script caller;
6. direct, denied, stale/conflict, idempotent retry, and supported recovery
   outcomes passed where applicable.

This evidence—not an unqualified zero—is the deletion license. No lane starts
before its complete row is green.

Execution status (2026-07-16): the source-controlled B2 evaluator and a
schema-valid evidence bundle exist for all five physical deletion lanes. The
first evaluator was accidentally deleted when rollout infrastructure was
retired while its JSON evidence remained; the replacement is standalone and
does not depend on the deleted rollout module. Run:

```bash
PYTHONPATH=. python scripts/certify_itinerary_deletion_lanes.py \
  --refresh-local --allow-blocked
PYTHONPATH=. python scripts/certify_itinerary_deletion_lanes.py \
  --check-local --allow-blocked
```

The refresh executes the focused canonical suites, records their real pass
counts, snapshots all three static ratchets, scans the retired lane artifacts,
and preserves deployed evidence and signatures as separate manual inputs. The
check re-runs the focused canonical suites and fails when their paths, counts,
results, static snapshots, or retired-artifact scans are stale. It does not
compare the embedded revision to `HEAD`, because an evidence file cannot contain
the hash of the commit that contains that same file. Omitting `--allow-blocked`
is the fail-closed deletion-license gate. Missing or duplicate lanes fail
validation.

No lane is licensed yet. The local refresh proves the focused canonical suites
and the absence of the retired plan-edit, proposal-apply, and rollout modules,
but it deliberately leaves deployed surface counts, canonical commit/proposal
counts, deployed-revision/static-revision identity, lane-specific symbol and
artifact/caller scans, observation windows, reset/reseed evidence, rollback
checkpoint, evidence references, and sign-off unresolved. Lane 5 also lacks the
lanes-1-to-4 license and the recorded global-switch decision. The static
inventories are green ratchets but still contain 1 classified legacy-product
writer site, 19 compatibility imports (8 replace, 7 delete, 4 rename), and 0
compatibility readers.
Those are retirement debt, not deletion proof.

The frontend deletion-reference scanner now reports **0** production callers.
Both the adapter and Change Studio preview lanes are reference-clean. API
implementations, mocks, and tests are excluded from that count. The scanner can
now run as a blocking gate when either frontend-dependent lane requests its
deletion license.

`useEditCommit` has crossed the boundary: concrete Change Studio Move, Remove,
and Replace intents are now constructed from the revisioned canonical plan
projection and sent through canonical preview plus server-resolved
Direct/Confirm/Propose/Denied handling. Replace now carries a stable venue
identity instead of only a display title. The legacy `postEditCommit` caller is
gone; target-less recommendation generation remains the separate lane-4
preview migration.

`useMoveBlock` has also crossed the boundary. Plan-row up/down controls now
compile to canonical Reorder with an explicit before/after anchor; timed and
cross-day moves compile to canonical Move. Both carry current day/block
revision preconditions, revalidate in preview, and follow the server's
Direct/Confirm/Propose/Denied decision. The old `api.moveBlock` product caller
is gone.

`useAddBlock` has crossed the boundary as well. Additions now construct a
revision-bound canonical Add from the current day projection, preserve stable
venue identity and cross-surface attribution, and follow
Direct/Confirm/Propose/Denied policy. Direct callers receive the created block
identity from the canonical commit receipt; proposal outcomes do not fabricate
a navigable block. The Add toast's Undo now targets the operation receipt. Both
the legacy `api.addBlock` and `api.undoBlockEdit` callers in this hook are gone.

`usePinExperience` now delegates to that same canonical Add authority after
resolving the requested day number and stable experience identity. It preserves
the experience's real title, avoids duplicate receipts, and no longer calls the
legacy pin route.

`useUpdateBlock` now maps the only supported production update shape—planned,
happened, or skipped event state—to a revision-bound canonical Mark Occurrence
operation. Unsupported legacy edit shapes fail closed. Undo targets the landed
canonical operation directly, using the immediate commit receipt first and the
live history recovery capability after navigation or reload. The legacy update
and undo route callers are gone, leaving the adapter lane reference-clean.

Change Studio recommendation preview no longer calls the legacy plan-edit
preview route. Candidate discovery remains a read-only better-slot query; the
client compiles the selected candidate into a revision-bound canonical Reorder
or Move preview before displaying it. Direct/Confirm/Propose/Denied therefore
comes from canonical policy, and Apply performs a fresh canonical preview before
commit. Free-form instructions and non-Move legacy preview shapes fail closed
into the existing rephrase/full-conversation path instead of being silently
reinterpreted or reviving the old authority. The frontend deletion-reference
scan is now clean.

### B3. Deletion lanes (strict order; each lane: delete → suites green → next)

1. **Planner/version and raw seed writers** (after A0/A1/C1/C2): remove the
   legacy `persist_planning_output` / durable version-write path from planner
   execution, superseded replan merge/write helpers, raw-SQL itinerary/day/block
   dogfood writes, and obsolete version-shaped downstream adapters. Import-ban
   the deleted product-writer entry points; retain only explicitly classified
   disposable test-fixture setup.
2. **Adapter legacy branches**: `trips.py` update/move/add/pin legacy halves;
   concierge `itinerary_edit.py` / `itinerary.py` legacy writes;
   `plan_edit_commit.py` `_apply_direct` + legacy `_stage_proposal`. **Hard
   prerequisite:** the matching frontend hooks and all agent callers are already
   on canonical preview/commit and the lane's B2 evidence row is green.
3. **Legacy proposal mutation engine** (after A2): remove
   `core/db/proposal_apply.py`, legacy construction/apply functions, and legacy
   branches in `proposals.py` resolve/withdraw/revert. Keep the group-facing
   `change_proposals` projection/read API until the 0.1 reader inventory has an
   implemented replacement. Import-ban deleted mutation APIs, not a still-live
   read projection.
4. **`plan_edit_preview.py`**: fold into `operations/preview`; Change Studio
   calls the canonical endpoint. Delete only after its frontend construction
   paths and request-shape mapping are proven.
5. **Collapse and delete the rollout gate (last)**: first rewire every canonical
   preview/commit/read/history/proposal/provider/Vesper/writeback caller away from
   per-trip stage/cohort/capability selection. Canonical authority becomes the
   unconditional product path. If D2 retains one operational switch, implement
   it as a global fail-closed availability check at the write boundary. Capture
   final compatibility evidence, remove compatibility telemetry, then delete
   `core/itinerary_rollout.py`, stage/trip-ids/cohort env vars, and obsolete `_V2`
   flags/readers from both repos and `docs/flags/registry.yaml`.
6. **Keep** `patch_trip` — trip settings, outside the operation model.

### B4. Close the guards and retained-read-model ledger

- Ratchet the Workstream 0 product-mutation allowlist to zero. Only the named,
  tested integrity/administrative and disposable-test exceptions may remain.
- CI import-ban deleted modules and specific deleted APIs (`proposal_apply`,
  legacy `change_proposals` mutation APIs, `plan_edit_commit`, planner-version
  persistence entry points, superseded replan writers, and raw dogfood itinerary
  writers). Do not ban a retained proposal read projection until its consumers
  have migrated.
- Record every retained compatibility table/column/module in a small disposition
  ledger with purpose, consumers, owner, and delete/rename review date. None may
  expose an independent itinerary mutation path.
- Record removal dates per path in
  [`itinerary-redesign-ir00-mutation-inventory-2026-07-13.md`](itinerary-redesign-ir00-mutation-inventory-2026-07-13.md)
  — closing its one unchecked completion-gate box.

## Workstream C — Dogfood data rewrite

### C1. Seeding mechanism: service-layer, single writer

`commit_itinerary_operation(conn, ...)` already provides the transactional
service-layer writer used beneath the route. Build one internal **replay
orchestrator** around canonical preview + commit; do not extract a second writer.
The route and replay orchestrator must converge on the same preview/policy/commit
semantics. Seeds stay offline-capable (the five-pack gate is "DB + offline
compose"); HTTP seeding is rejected. Replay-only orchestration affordances:

- **Historical replay clock** — historical trips (elif-tokyo-2025, completed
  Lisbon/Rome arcs) need preview, operation, transition, proposal, provider-saga,
  history, and occurrence facts stamped on one declared timeline. Exposed only
  through the internal replay entry point, never on the route.
- **Deterministic IDs without seed mutation semantics** — operation, itinerary,
  day, block, proposal, and scenario-linked identities derive deterministically
  from canonical operation/shape inputs, or are ordinary validated fields of the
  normalized contract. Replay supplies stable canonical inputs; the commit
  gateway contains no `seed_mode` identity branch. Preserve existing
  `dogfood_key` cross-domain references by mapping them to those canonical inputs
  and verify `seed_expenses.py`, `seed_atlas_artifacts.py`, and booking-proposal
  references explicitly.
- **Lifecycle replay** — timestamp override alone is insufficient because policy
  also reads stored trip status and terminal context. Replay creates a trip in
  its historically correct editable state, lands plan/proposal/provider events
  in order, transitions trip status/lifecycle, then lands allowed post-trip
  occurrence or attendance corrections. Replay does not bypass policy.

Acceptance: the same normalized request produces the same identities, policy,
and plan result through route orchestration and internal replay; replay-specific
code controls chronology/input sourcing only; deterministic replay is
idempotent; an already-completed trip cannot receive structural edits merely
because replay supplied an older timestamp.

Execution status (2026-07-16): implemented and covered by the canonical seed
and replay suites. The internal replay orchestrator owns chronology while the
canonical commit gateway remains the writer.

### C2. Rewrite `_seed_itinerary` (seed.py:673)

Replay each manifest itinerary chronologically:

1. create the trip in its historical planning state;
2. one `materialize_shape` operation creates the complete initial dated draft,
   including deterministic itinerary/day/block identities, anchors, provenance,
   participation/ownership, and stable lineage;
3. authored later `add`/`move`/`replace` operations express scenario history;
4. canonical proposal operations and transitions cover group-decision scenarios;
5. manual booking-attestation events and held-provider saga events remain
   distinct, following the contracts decided/proved in A3;
6. transition the trip to live/completed/cancelled as the manifest requires;
7. `mark_occurrence` or allowed factual corrections follow after the trip.

This is an upgrade, not just compliance: seeded trips gain real history,
receipts, undo capability, and Changes-feed content — surfaces that are empty
in dogfood today.

Execution status (2026-07-16): implemented for itinerary birth and authored
proposal replay. Final acceptance remains coupled to C4's all-five-pack reset,
cross-domain verification, and journey run against the newly replayed data.

### C3. Manifest schema pass

Extend `tools/dogfood/content/manifests/*.yaml` so scenarios can express
operation history ("this block was moved once by dao, proposed by mara").
Default remains plain adds; only journey-certification trips (mara-lisbon,
elif-rome, …) need authored operation narratives.

### C4. Wipe & reseed

1. Local: full reset → canonical replay of all five packs + persona bundles →
   `make dogfood-five-pack-verify`.
2. Run B1/B2 and the full journey set against this ledger-from-birth local data;
   do not certify deletion only against old raw-SQL dogfood.
3. Update `packs.yaml` / `scenarios.yaml`; re-run the "one world day"
   validator and verify every cross-domain stable ID reference resolves.
4. Fly: record the exact target environment, take and verify a restorable
   snapshot/export, print the destructive scope, require the existing explicit
   apply acknowledgement, then `APPLY=1 PROFILE=fly make dogfood-promote
   CITY=…` per city → `make dogfood-fly-smoke`.
5. If verification fails, stop promotion and restore/re-run from the recorded
   snapshot procedure; do not repair the canonical ledger with ad hoc SQL.

IR-03 backfill of existing dogfood rows is explicitly **rejected** — the data
is synthetic; reseeding is cheaper and yields richer substrate.

## Workstream D — Frontend adoption + certification

- Point mutation hooks (`useEditCommit`, `useMoveBlock`, `useAddBlock`,
  `useUpdateBlock`, `usePinExperience`, optimize, occurrence, attendance, branch,
  and recovery entry points) at canonical operation/proposal/history/provider
  APIs via the generated client; delete legacy call paths. Change Studio
  decomposes into typed construction per IR-14 — one UI for
  Direct/Confirm/Propose/Denied; the server resolver decides, the client renders.
- Maintain a route/entry-surface matrix mapping Plan rows/day controls, venue
  detail, Discover, Saved Places, Changes, Trip Details, Map, and Vesper handoffs
  to their canonical request and landed result. A B3 lane cannot delete its
  adapter until every corresponding matrix row is green and static route scans
  find no legacy caller.
- Adopt the IR-13 read shell / canonical read authority as the default
  (then delete `ITINERARY_READ_MODELS_V2` with the rest).
- Make the reworked Itinerary the default single-trip planning surface. Inventory
  every older Plan/Itinerary route and component: delete duplicates, redirect
  obsolete routes, or retain only thin presentation wrappers over canonical
  reads/actions. No user-visible second itinerary editor or competing trip-entry
  authority survives the cutover.
- Changes feed + inline undo consume the IR-09 history/recovery endpoints
  (currently built-dark behind `ITINERARY_HISTORY_V2`) instead of
  synthesizing capability from proposal type.
- Regenerate `schema.gen.ts` from the new OpenAPI. Note: this was
  hand-bridged once (Trip Workspace Phase C) due to cross-branch divergence;
  both repos are on main — verify a clean regen and retire the hand-bridge.
- Re-certify every journey currently registered in
  `docs/journeys/journeys.yaml` rather than hardcoding a range; J05
  proposal→plan-mutation remains the primary wedge, while account/data
  lifecycle, membership/invite, and social propagation journeys protect the
  administrative exceptions and retained projections. Re-run the relevant
  Maestro and 2026-07-14 device-QA fixtures against the canonical-only posture.
- Docs closure: mark `travel-app/docs/audits/itinerary-edit.md` (Change
  Studio) superseded; update journeys / page-specs / trip-itinerary surface
  contract; `make docs-status-sync`.

This workstream completes functional adoption of the reworked itinerary. It does
not require the final visual-polish pass of Itinerary × Trip Home/Folio, but no
old Plan/Folio component may retain an independent legacy write path. All
surviving surfaces must read or mutate the same canonical itinerary truth.

### Deployment and rollback posture

- Deploy additive schema and canonical backend support first, then the canonical
  frontend. Do not ship a frontend that requires a route not yet present or
  delete a route still called by the current internal build.
- Before physical deletion, deploy and certify a **canonical-only checkpoint**:
  legacy files may still be present, but every legacy selector/branch is
  unreachable and any canonical outage fails closed. Record this exact backend,
  frontend, schema, and configuration tuple as the rollback target.
- Physical deletion is a later deployment based on that checkpoint. Rolling
  back deletion restores only the certified canonical-only checkpoint; it never
  restores a build/configuration capable of selecting legacy mutation authority.
- Any retained `ITINERARY_OPERATIONS` operational kill switch is fail-closed:
  disabled means read-only/explicit service unavailable, never legacy fallback.
- Rollback must preserve additive schema and all canonical
  operation/history/provider evidence. A rollback that requires discarding that
  evidence or re-enabling a legacy writer is invalid.
- Destructive schema cleanup, if any, occurs only after code deletion and
  canonical reseed/certification are stable. It is not bundled into the adapter
  deletion deployment.

## Sequencing

```text
Week 1: Workstream 0 inventory + ratcheting guards
        → A0 materialize_shape contract/commit  ← first critical path
        parallel after boundaries are known: A2 proposal creation/read-model
        disposition, C1 replay-orchestrator design
Week 2: A1 planner birth/replan producer  ← second critical path
        parallel: A3 contracted producers, D frontend route/entry migration,
                  C2/C3 canonical manifest replay
Week 3: canonical local reset/replay → B1 full-on posture
        → B2 positive per-lane exercise + zero-compatibility evidence
        → deploy/certify canonical-only rollback checkpoint
        → B3 lanes 1→2→3→4, one evidence row and allowlist ratchet at a time
        → D all-registered-journey + device certification
Final:  C4 backed-up Fly wipe/reseed → Fly smoke/certification
        → B3 lane 5 rollout-gate/flag collapse and deletion LAST
        → B4 zero-product-writer guard + retained-read-model ledger + docs closure
```

Sizing (rough): A0 and A1 are both architecture-bearing work. Materialization,
deterministic diff/replan, and planner migration should be estimated separately.
A2's mutation conversion may be one–two days, but proposal-reader replacement
is separate if D4 chooses replacement. Manual booking attestation is contract
work until D5 is ruled; held-provider confirmation is an adoption/proof lane over
the existing saga. C2 begins after the replay orchestrator and canonical
deterministic identities exist. B3 deletion lanes are fast only after frontend,
producer-exercise, canonical-only checkpoint, and static-boundary proof are
complete.

## Decision record

| # | Decision | Affects | Recommendation |
|---|---|---|---|
| D1 — resolved | `plan_events` is a frozen read-only historical ledger. Product writes, readers, and the dead read module are gone; table rows remain only for archive/privacy lifecycle and deployed retirement evidence. | A1, B3 lanes 1/3 | Physically drop the table only after archive/privacy and deployed evidence license it. |
| D2 — resolved | Per-trip rollout selectors are deleted; retain one global fail-closed `ITINERARY_OPERATIONS_ENABLED` switch. | B3 lane 5 | The switch rejects canonical writes when off and can never select a legacy writer. |
| D3 — resolved | Historical replay time belongs to a separate internal replay orchestration path. | C1 | Never expose the replay clock on the public route. |
| D4 — open physical disposition | The group-facing decision projection is retained behind the explicit `itinerary_decision_projection` owner. | A2, B3 lane 3, B4 | Preserve display/vote/deadline/status behavior; rename or replace the physical projection only after its lifecycle and deployed consumers are proved absent. |
| D5 — resolved | Only the booking controller or assigned handoff actor may make manual booking attestation. | A3, C2, B3 lane 2 | Record immutable `user_reported` attribution, distinct from provider-confirmed truth. |

## Acceptance — definition of done

- [x] 0a: every direct writer and legacy proposal/history consumer is
      classified and the CI boundary guards are installed and ratcheted.
- [ ] 0b: the legacy-product writer allowlist is zero. One finite
      `itinerary_edit_log` drain acknowledgement remains until deployed backlog
      evidence licenses its removal.
- [x] A0: one `materialize_shape` operation commits the complete first dated
      draft—days, initial blocks/anchors, ownership, provenance, and canonical
      deterministic identities—with idempotency, one history item, and atomic
      fault rollback; no partial/empty first draft is visible.
- [x] A1: planner births itineraries with that one materialization operation and
      replans as deterministic guarded diffs; `_plan.py` has zero direct writes,
      no downstream consumer depends on legacy `persisted_version`, and stale
      output cannot overwrite newer edits.
- [x] A2: all four proposal producers mint canonical operation proposals.
- [x] A2 projection boundary: legacy proposal construction/apply authority is
      gone; every retained group-facing proposal projection has an explicit
      consumer/owner/disposition and no independent itinerary writer.
- [x] A3: optimize_day, REST recovery, branches, D5-approved manual booking
      attestation, and existing held-provider confirmation adoption are
      implemented and proven as distinct semantics.
- [x] B1: full suites + every journey in the canonical registry are green with
      the intended full-on environment asserted and every producer exercised
      canonically; the prior 790-test corpus has not regressed and new cutover
      tests are included.
- [ ] B2: each deletion lane has deployed nonzero exercise and canonical-write
      counts, green negative/static scans, and direct/denied/conflict/retry/
      recovery evidence as applicable. Zero compatibility events applies only
      where instrumentation existed; already-deleted paths require deployed
      unreachability proof with null—not fabricated zero—event counts.
- [ ] B3: local physical source deletion is substantially complete, but a
      certified deployed canonical-only rollback checkpoint and lane evidence
      are still required; `patch_trip` remains intentionally retained.
- [ ] B4: deleted API/module import bans are green; IR-00 removal dates and the
      retained-read-model disposition ledger are complete.
- [x] C-local: five packs replay chronologically through canonical preview/
      policy/commit and distinct manual/provider booking contracts with stable
      cross-domain IDs and no seed-specific mutation semantics.
- [ ] C-deployed: Fly is backed up, reset/reseeded, and verified without ad hoc
      repair SQL.
- [x] D-functional-local: every itinerary mutation entry surface uses canonical
      APIs; app/backend compatibility readers and app production callers are
      zero.
- [ ] D-deployed-closeout: schema/device journeys, the J05 wedge, default
      reworked-Itinerary presentation, duplicate-editor absence, and docs are
      re-certified against the deployed revision.
- [ ] End-state audit: one normalized operation model and one server mutation
      authority own itinerary truth; every retained compatibility structure is
      read-only with an explicit purpose; the operational kill switch, if kept,
      fails closed and cannot resurrect legacy behavior. Formal closure still
      requires zeroing the one legacy writer, resolving the 19 retained imports,
      and completing deployed B2/C/D evidence and sign-off.
