---
doc_type: working
status: active
decision_status: implemented
owner: Integration
created: 2026-09-07
last_verified: 2026-09-07
expires: 2026-10-07
why_new: Records the bounded Opening-read and optional Places executor fixes landed after the request-to-root checkpoint without absorbing concurrent lane receipts.
supersedes: []
depends_on:
  - complete-system-integration-roadmap-2026-09-05.md
  - source-connected-value-execution-receipt-2026-09-07.md
---

# Integration execution checkpoint — 2026-09-07

This note records the next controlled integration tranche after the
request-to-root fixture. It is an execution receipt, not a new product
architecture or a production-activation decision.

## Wave 1 baseline handoff — September 7, 22:25 EDT

This is the receiving checkpoint for **“establish the shared engineering
baseline.”** It pauses the next practical-owner package until the combined
candidate is repaired and rechecked. The revisions below are local only; no
remote publication, deployment, provider activation, or destructive cleanup
occurred.

| Repository / candidate | Revision | State |
| --- | --- | --- |
| Workspace `main` | `021b4e9` | clean; Strategy program map plus Engineering Meta workspace reliability cuts received, with this checkpoint's policy-mismatch receipt |
| Backend `main` | `afe177b33d25dc3563c362de4ff6e3a47b1a8354` | clean; forward-only `lifeorgpipelinemerge01` reconciles the prior `lifeorg07` and `pipeline_scope_key01` heads |
| Mobile receiving candidate (`travel-app` `main`) | `8dfa19119` | clean; Meta app cut `95b6d39aa`; generated-sync attempt was reverted to preserve type safety while the dark-operation policy is resolved |

### Evidence

* `make doctor` passes; service probes are unrun because the local Postgres
  container is not running. `python3 -m pytest scripts/tests -q` passes **64**.
* The backend migration graph is one head (`lifeorgpipelinemerge01`). The merge
  migration is graph/import/pre-commit verified; a disposable database upgrade
  has **not** run because the local database service is unavailable.
* `make contract-check` is **blocked** at projection: the Social receiving cut
  calls `GET /api/relationships/place-handoffs/sent` from
  `travel-app/data/relationshipPlaceHandoffs.ts`, while the operation policy
  still declares that endpoint dark with no consumers. Removing the generated
  type breaks app typecheck; promoting the dark endpoint changes governance.
  The receiving checkout therefore retains the type-safe pre-sync schema and
  records this as an owner decision, not an automatic contract change.
  Schema bridge, API-boundary, native-compatibility and app typecheck pass on
  this retained candidate.
* The backend canary reports **21,282 passed, 7 failed, 20 skipped, 56
  xpassed**. Failures are existing entity-field coverage, HPL social-authority,
  root-attention fixture identity, and outcome-life producer contracts; this is
  not a green baseline.
* Before the dark-operation mismatch was isolated, the receiving app's
  `verify:fast` reached typecheck, API-boundary and schema bridge successfully,
  then failed the existing Home-surface budget:
  `components/places/PlacesFeedCardView.tsx` is **133/125** lines. A full app
  Jest run was not a complete receipt (it exited 139 after broad execution);
  a bounded six-suite rerun recorded **55 passed / 8 failed**, covering existing
  conversation/history, control-alignment, card-policy, contrast, and
  navigation-contract failures.
* Engineering Meta's backend package remains **unlanded**: its staged 122-path
  cut is blocked by the existing broad-exception ratchet (**1,198** handlers vs
  frozen **1,190** ceiling), with separate writer-boundary, fixture and mypy
  failures. The zero-new-handler claim does not waive that gate. Its committed
  workspace and app cuts are received above; its dirty backend worktree remains
  owned by Meta and was not merged.

### Receiving order after this checkpoint

1. Meta repairs the backend gate/writer/type/fixture blockers and supplies one
   hook-passing backend commit; Integration then reviews it against
   `afe177b33` and the migration merge.
2. Re-run the exact tuple's contract, focused backend and receiving-app gates;
   repair the Home budget and the bounded app contract failures in their owned
   lane, without touching the primary dirty checkout.
3. Start a disposable Postgres/Qdrant runtime and execute the migration upgrade
   plus the relevant database suites. Record runtime evidence separately from
   graph-only validation.
4. Only after those gates are green, reassess the combined candidate and decide
   whether to resume the practical-owner Home/Places package. No wave 2 work is
   authorized by this receipt.

## Landed

### Retained Opening context is an exact Moment dependency

The source-opening lane was converged in backend merge commit `7d9f85488`
(`fix: admit retained opening context through moment reads`). Its tree is
identical to the equivalent `b25702bb1` fix already present on `main`, so the
merge introduces no duplicate behavior. The resulting code keeps the
Source-contribution contract explicit: an Opening resource is read by
`moment.read`, while retained Source resources continue to be read by
`source.inspect`; the compiler admits the exact `opening` resource kind for
Moment reads. The owner-admission tests exercise Home and Places for an active
Opening and suppress the contribution when that Opening changes, is dismissed,
or expires.

This keeps the dependency graph honest: a retained Source does not borrow
current Opening state, and a failed optional Moment read cannot silently turn
an old context into a current claim.

### Optional Places reads have physical admission bounds

The optional-read lane was converged in backend merge commit `5a1b8e493`
(`bound optional blocking read admission`). The same implementation was
already present on `main` as `7a8a6f58c`, so this merge also introduces no
duplicate behavior. The existing code adds a semaphore around the optional
Places blocking executor. A queued timeout or cancellation marks its work
item as cancelled but holds the permit until that physical item drains.
Repeated root deadlines therefore fail closed instead of accumulating
unbounded executor work. Submission failure releases the permit, and running
work still has its existing late-outcome handling.

This is an operational safety correction to the existing owner-read boundary;
it adds no provider, scheduler, durable watch, or new root workload.

## Verification

From `travel-agent`, the combined owner-read, Source, root, practical, exact
request, and optional Places suite passed:

```text
259 passed in 7.77s
```

The suite includes the HTTP/storage request→worker→readback fixture, exact
Home/Places receiving, public/retained Source admission, practical opening
assessment, canonical owner reads, root composition, JSONB digest identity,
and executor saturation/cancellation. It uses local authored fixtures and
does not claim provider or paid-model coverage.

## Deliberate non-goals

* `route.evaluate` remains unavailable to the canonical owner-read mesh. The
  existing `RouteFact`, movement, and leave-by specialists remain scoped
  foreground capabilities; no generic route owner or background location
  permission was invented.
* Source worker/provider activation remains dark. A successful fixture proves
  lifecycle and receiving contracts, not production supply, cost, or user
  usefulness.
* No Chat redesign, Life migration, native screen, or generated API contract
  was changed in this tranche.
* The current workspace still contains concurrent uncommitted strategy,
  design, OpenAPI, and concierge changes. They were intentionally not staged
  or folded into this receipt.

## Next checkpoint

Reassess CV-2 checkpoint 2 against actual owner-to-consumer cases: a practical
fact should change the dependent Home/Places claim while the independent saved,
editorial, social, or historical material survives. Only if a concrete timing
question appears in that portfolio should we design the next explicit
RouteFact/movement adapter. Keep provider activation and native acceptance as
separate gates.
