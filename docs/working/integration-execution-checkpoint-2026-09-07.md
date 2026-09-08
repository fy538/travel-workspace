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

## Bounded baseline-repair round — September 7, 23:00 EDT

The first repair round is now partially landed. Integration received the
Social policy correction, regenerated the mobile projection and generated app
types once, and landed the bounded Home/Places repairs. These changes remain
local; no remote publication, deployment, provider activation, flag activation,
or native acceptance occurred.

| Package | Revision | State |
| --- | --- | --- |
| Workspace Social policy/docs | `e80ff66` | landed; sender-history endpoint is active with its reviewed app consumer, while the feature flag, sender-only authority, redaction, and rollout posture remain unchanged |
| Workspace mobile projection | `60ef47b` | landed; `docs/openapi.app.json` now contains the policy-admitted sender-history operation |
| Mobile generated contract | `a60a04230` | landed on `travel-app` `main`; generated schema matches the active projection |
| Mobile Home/Places repair | `6b44041ea` | landed on `travel-app` `main`; budget and bounded surface contracts repaired |
| Backend Engineering Meta repair | blocked at commit gate | supplier's isolated package reaches the declared reliability gates, but repository-wide size/status guard checks fail on pre-existing unrelated paths; no backend changes have been merged in this round |

### Current receipts

* `make contract-check` passes after the Social policy decision and final
  projection/type generation: **581** complete-snapshot paths, **446** mobile
  paths, **491** mobile operations, **1,325** mobile schemas; schema bridge and
  place-identity checks pass.
* `make api-coverage-check` passes: **566 active**, **15 dark** (all flagged),
  and **62 retiring** operations. The sender-history route remains behind
  `RELATIONSHIP_UUID_HANDOFFS_ENABLED`.
* Workspace documentation inventory, links, governance, and the API contract
  audit pass. Workspace `scripts/tests` remains **64 passed** and `make doctor`
  passes with service probes intentionally unrun.
* Mobile Home/Places checks pass: the PlacesFeedCardView budget is **25/125**,
  typecheck passes, lint exits 0 with **169 pre-existing warnings**, and the
  focused production/surface suites pass (**5 suites / 132 tests**).
* The exact six-suite receiving rerun is **62 passed / 1 failed**. The sole
  remaining failure is the previously identified Social-owned
  `components/places/renderers/socialCard.tsx` hit-target offender; Home did
  not modify that file and the Social lane has not yet supplied its transfer.
* The canonical runtime remains unrun. The workspace has no isolated lane
  manifest and the default Compose stack is stopped, so Integration did not
  start a shared database or run migrations against it.
* Engineering Meta's final handoff is **blocked, not bypassed**: the staged
  128-path package reaches the exact broad-exception ceiling (**1,190/1,190**),
  itinerary writer boundary (**151 sites**), and focused reliability receipt
  (**241 passed / 9 skipped**). Its bounded offline run still exposes **10
  undeclared-Postgres** concierge DB-leak failures. Repository-wide
  pre-commit then fails existing size-budget offenders
  (`intake_v2_jobs.py`, `account_deletion.py`, `concierge/agent.py`, and four
  oversized files) plus existing status-guard offenders in
  `backend/ingestion/base.py`, `life_projection/organization_projector.py`,
  and `core/db/life_organization_resolution.py`. No hook was bypassed and no
  baseline was raised.
* The canonical backend focused tuple still reports **7 failures** on
  `afe177b33`: the Experience source-field fixture, HPL social-authority
  revision fixture, four OwnerReadPortfolio identity fixtures, and the
  Occasion-membership producer (`change_kind` is currently undefined). These
  are the exact behaviors covered by the supplier's declared repair paths; the
  uncommitted supplier package was not copied into `travel-agent/main`.

### Receiving order from this round

1. Keep Engineering Meta's dirty worktree isolated. Resolve or explicitly
   accept the pre-existing repository-wide size/status guard blockers before
   requesting a backend commit; do not merge a staged-but-uncommitted package.
2. Decide whether Social should provide the one remaining `socialCard.tsx`
   control-alignment repair. Do not fold that file into Home by inference.
3. Run the backend focused failures and the combined mandatory checks once the
   backend package is landed. Keep the isolated runtime/migration validation a
   separate gate.
4. Reassess the complete candidate. No Wave 2 feature or product-surface work
   begins from this receipt.

## Baseline close-out — September 7, 23:22 EDT

The remaining mobile baseline failure is now received. The backend package is
still not eligible to land, so this checkpoint is **not baseline verified**.

| Package / validation | Revision or result | State |
| --- | --- | --- |
| Social control-alignment repair | `travel-app` `5f41be821` (supplier `6ab20f227`) | landed on canonical mobile `main`; only `components/places/renderers/socialCard.tsx` changed |
| Exact mobile six-suite baseline | **6 suites / 63 tests passed** | green on receiving `main` |
| Mobile gates | typecheck, test typecheck contracts, schema bridge, API boundaries, native compatibility, Home/Places budgets, scoped ESLint, full lint | green; lint reports 169 existing warnings and 0 errors |
| Disposable runtime | `vesper-mobile-baseline-repair-2026-09-07`, ports `63610–63614` | started with explicit Compose override for the repository's fixed container names; Postgres and Qdrant healthy |
| Forward migration | `alembic upgrade head` → `lifeorgpipelinemerge01` | passed; `alembic current` and `alembic heads` agree on the single head |
| Postgres-marked suite | **1,316 passed / 46 failed / 5 skipped**, 21,414 deselected, 2 warnings | executed against the disposable database; not green |
| API service | startup readiness | unrun: isolated API exited because `ANTHROPIC_API_KEY` is absent; no shared service was touched |

### Runtime failure reconciliation

The 46 Postgres failures do not represent one new regression. The dominant
cluster is the known `change_kind` `NameError` in
`outcome_life_propagation.py`, reaching Occasion/life/outcome/account-erasure
tests; this is directly covered by Engineering Meta's staged seven-path repair.
The other failures are separate pre-existing contract or fixture debt exposed
by a fresh database: August 2026 proposal dates are now in the past, several
tests assume hard-coded seeded place rows, the context loader's internal group
profile fixture is incomplete, a relationship fixture violates the current
verified-source receipt constraint, and there are independent receipt
metadata, UTC-offset formatting, local-plan time, notification, provisional
place, and dogfood-catalog mismatches. None was silently reclassified as a
green result or folded into Social/Home.

Engineering Meta's consolidated handoff remains read-only and unlanded: 128
staged paths at base `afe177b33`, manifest SHA256
`ce0bf1606d2b3bb077d2758dab3bea377c6ee2898b7a6b3c8a77199422650ab6`, with
the broad-exception ceiling (**1,190/1,190**), writer boundary (**151**), and
focused receipt (**241 passed / 9 skipped**) green. The normal commit hook is
blocked by unrelated repository-wide size/status guard debt, while the bounded
offline run exposes 10 undeclared-Postgres concierge fixtures and full mypy
still reports 264 errors across 63 files. No hook, baseline, or quarantine was
bypassed.

The disposable containers, volumes, network, temporary Compose override, and
lane venv symlink created for this validation were removed explicitly after
the run. No remote push, deployment, activation, or shared-daemon restart
occurred.

### Current prerequisite sequence

1. Decide whether the repository-wide size/status guard debt may be repaired or
   explicitly accepted so Meta can produce a normal hook-verified backend
   commit; do not copy its staged package into `travel-agent/main`.
2. Separately triage the fresh-database fixture/contract failures above; the
   `change_kind` cluster should be rechecked first once Meta is eligible.
3. Supply `ANTHROPIC_API_KEY` only if API-lifecycle validation is required,
   then repeat the isolated runtime smoke; keep provider/model execution
   separate from migration and Postgres evidence.
4. Re-run the combined mandatory checks and only then mark the baseline
   verified. Wave 2 remains paused.

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
