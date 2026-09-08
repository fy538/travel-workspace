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

## Targeted backend prerequisite round — September 8, completed

Strategy authorized a narrow follow-through without reopening product or
mobile work. Engineering Meta owns the existing 128-path staged reliability
package plus three prerequisite repairs in its isolated worktree
`/Users/feihuyan/travel-workspace-engineering-reliability-2026-09-07/travel-agent`
at base `afe177b33`: preserve genuine Life status detection while correcting
the five false-positive dead gates, guard the `experience_briefs` writer race
under its existing lifecycle, and extract only the measured size-budget
offenders without changing behavior. Integration has not copied or staged any
of that dirty worktree.

Fresh canonical gate measurements before the repair are:

* size: `repair_intake_v2_outbox` **855**, `delete_user_data` **835**, and
  `handle_turn` **801** lines; files `concierge/session.py` **2565**,
  `experience_graph/commands.py` **2492**, `api/routes/conversations.py`
  **2452**, and `concierge/_prompts_skills.py` **2451**;
* status write guard: one unguarded `experience_briefs` status update;
* status parity: green;
* status dead gates: five Life comparisons against values absent from the DB
  CHECK constraints.

The receiving order is Meta package → seven canonical backend failures → the
known `change_kind` database cluster → separately owned residual fixture and
contract repairs. No baseline increase, exemption, broad cleanup, or Wave 2
work is authorized by this section.

### Package A receipt

Meta's first prerequisite package is complete in the isolated staged tree:
four additional owned paths, **131 staged paths total**, no unstaged changes,
and manifest SHA256
`50b3b159530b23ee779d35b45a2266ec8ebb689b40a0d4f683e8cd14a9d4cacc`.
The status checker now ignores only the explicit in-memory Life repair
receivers in the two named modules; the `experience_briefs` writer demotes
only rows currently `complete` inside the existing transaction. Thirty-two
targeted tests pass, both status guards are green, and no DB constraint,
product state, baseline, or broad exemption changed.

The size package is not yet complete. A first mechanical extraction of
`repair_intake_v2_outbox` was fully reverted because it duplicated structure
and left both sides over budget. The remaining three functions/four files
therefore remain unchanged pending deliberate phase-level extraction and
equivalence tests. No backend commit is eligible yet because the full-tree
size gate still fails; the staged package remains isolated and unlanded.

### Integration residual fixture/contract package — September 8

Integration kept the backend residual work in the isolated worktree
`/Users/feihuyan/travel-workspace--mobile-baseline-repair-2026-09-07/travel-agent`
and did not touch Meta-owned source or the canonical runtime. The package is
test-only and is committed there as `a1c841181`
(`test: make backend residual fixtures self-contained`). It repairs only
fixtures whose assumptions drifted from the current contracts:

* proposal/confirmation dates no longer depend on past August 2026 dates;
* trip-save suggestions, provisional places, and inbound text/audio/image
  cases create their own catalog rows and clean them up;
* context-loader profiles carry explicit privacy-source identity and revision;
* save-root assertions compare the serialized UTC representation at the API
  boundary;
* local-occasion closure resolves the venue timezone instead of treating
  Lisbon as UTC;
* group booking receipts assert the current audience contract (provider-proof
  availability without controller-only confirmation details);
* leave-by stubbing patches the route-fact seam actually used by the
  dispatcher;
* relationship persistence supplies a valid custody receipt for a verified
  intake source, preserving the database check constraint; and
* the Brooklyn Home certifier was exercised against a disposable, canonical
  dogfood seed (no certifier write path was changed).

Evidence from the isolated migrated database (Postgres `63610`, Qdrant
`63611`): **79 passed, 1 warning** across the exact residual suite. Ruff,
format, and `git diff --check` pass; the normal backend commit hooks also pass.
The one warning is the existing optional Nomic acceleration warning from an
image-pipeline test. The disposable seed and catalog were not committed.

### Receiving after landing — September 8

The two backend packages are now landed on canonical backend `main` in this
order:

1. Meta structural reliability package: `6da6905ac`
   (`chore: land structural reliability package`, 149 paths; normal commit
   hooks passed).
2. Integration residual fixture/contract package: merge commit `5e9d0a190`,
   bringing `a1c841181` onto backend `main`.

The canonical backend candidate is clean at `5e9d0a190`. Post-landing
verification is green for the bounded package: the engineering-focused tuple
is **243 passed / 9 skipped**, and the exact residual Postgres suite is
**79 passed / 1 warning**. A fresh disposable migration reaches the single
head `lifeorgpipelinemerge01` before those tests run.

The broader `-m requires_postgres` run was intentionally stopped after it
entered the existing Life projection concurrency/deadlock path (the run
reported an async timeout in `life_projection/occasion_projector.py` and
additional failures before termination). It is therefore not represented as a
green full-suite result. No production process was involved; the disposable
Compose project was stopped and removed after the bounded evidence.

This closes the structural prerequisite and the residual fixture package, but
does not certify the entire repository. Remaining work is a separate repair
of the Life projection concurrency failures and the previously recorded
undeclared-Postgres offline fixtures. The post-landing offline run is
**21,086 passed / 240 undeclared-Postgres failures / 14 skipped / 53 xpassed**;
the failures are the expected leak family exposed by the tightened baseline,
not a migration or API-contract failure. No baseline, hook, or test quarantine
was changed.

The preceding staged-tree measurements are retained as historical pre-landing
evidence. They are superseded by the receiving record above; the staged tree
was committed and merged, and the disposable Compose project, volumes,
network, temporary override, and lane venv symlink were removed after
validation. No remote push, deployment, provider activation, generated
contract sync, or shared-daemon restart occurred.

## Offline isolation follow-through — September 8

The bounded offline leak-repair round is complete on canonical backend `main`
at `52e2fe31d` (`test: isolate offline readers across backend suites`). The
package stays inside the test-isolation boundary, with one small production
guard in `backend/concierge/group_compose.py` that returns the existing
`no_members` result before optional trip-context reads when a room has no
members. It does not change the API contract, migration graph, provider
activation, notification policy, or surface behavior.

The package explicitly mocks optional DB-backed readers at the test boundary,
marks true persisted-DB cases `requires_postgres`, aligns the HPL social grant
fixture with the audience-sensitive Occasion revision, and drains dedicated
external-health tasks so teardown warnings cannot contaminate another test.
The canonical backend worktree is clean; no remote push or deployment occurred.

Evidence:

* Ruff, formatting, vulture, and all applicable commit-stage hooks passed.
* The changed-test tuple is **1,168 passed / 43 xpassed** offline, with no
  undeclared-Postgres failures.
* The full offline suite is not claimed green: its prior complete run reached
  **21,290 passed / 26 failed / 14 skipped / 2 xfailed / 51 xpassed** before
  the final residual fixes, and a later 99%-complete run was interrupted by the
  known end-of-suite unawaited-task/content-safety hang. The remaining
  non-isolation repository signal is the docs-governance stale status for the
  canonical Unified Context and Memory Plan (`status: blocked`), which needs a
  Strategy/founder authority decision rather than a test-only change.
* The full mypy gate remains a pre-existing baseline failure at **262 errors
  across 62 files**; no changed-file typing error was introduced by this
  package.

The Life supplier commit `6d2b84d72` was validated separately in an isolated
combined candidate on top of `52e2fe31d`. Normal applicable hooks and the size
gate passed; Life offline tests were **249 passed / 40 deselected**, with the
projector-focused selection **23 passed**. Disposable Postgres was unavailable
in this lane, so the supplier's connected **40 passed / 249 deselected** report
remains unverified here and must be rerun by Integration before landing. The
Life source commit was not merged or pushed from this lane.

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
