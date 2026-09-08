---
doc_type: working
status: active
decision_status: implemented
owner: Integration
created: 2026-09-07
last_verified: 2026-09-08
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

## Integration receiving close-out — September 8

The receiving candidate was rebuilt from backend `52e2fe31d` and applied only
the reviewed Life supplier commit `6d2b84d72`. It ran against a newly created,
explicitly disposable Compose project `vesper-engineering-reliability-2026-09-07`
(`54572` Postgres; `54573/54574` Qdrant), with `TEST_DATABASE_URL` and
`TEST_DATABASE_DISPOSABLE=1` set only for the connected lane. The candidate was
not pointed at the canonical/default stack and no shared daemon was restarted.

The receiving branch is local-only at `codex/integration-execution-2026-09-08`:

| Package | Revision | Evidence / state |
| --- | --- | --- |
| Offline lifecycle repair | `7ad926648` | Committed separately; memory recall explicitly exercises lexical fallback offline, and dead-handler audit counts all helpers in one source scan. |
| Context-memory authority docs | `7c2319879` | Four exact Strategy files received and committed separately; child product-doc governance **5 passed**. |
| Life receiving candidate | `d029ead4f` | Life commit applied on top of `52e2fe31d`; candidate branch tip is `7c2319879`. |

### Receiving evidence

* Life Postgres suite: **40 passed / 249 deselected** after `alembic upgrade
  head` reached `lifeorgpipelinemerge01`.
* Life offline suite: **249 passed / 40 deselected**; projector-focused
  selection: **23 passed**.
* Normal pre-commit hooks and backend size budget: **passed** on the combined
  candidate. The connected Life run is now verified by Integration; the prior
  supplier-only 40-pass report is no longer the sole evidence.
* Full offline suite, correctly filtered and run with four workers: **21,308
  passed / 20 skipped / 1 xfailed / 52 xpassed / 7 failures** in **59.14s**.
  The prior 99% stall is repaired: there was no end-of-suite hang, unawaited
  coroutine failure, or content-safety teardown error. The seven remaining
  failures are bounded environment/authority debt: four backend↔frontend enum
  parity tests and two frontend snapshot tests cannot resolve the sibling
  `travel-app` from a standalone backend worktree, plus the former blocked
  product-spine status (resolved by the received Strategy docs, but not part
  of the code candidate's original run).
* A lower-timeout diagnostic identified the former stall's actual causes: the
  query-recall test was loading the local SentenceTransformer instead of
  exercising its lexical fallback, and each dead-handler audit repeated a
  full `git grep` for 155 helpers. Both are now bounded at their ownership
  boundaries with regression coverage; no timeout was raised, test was
  excluded, exception swallowed, or baseline changed.
* Full mypy remains a separate baseline failure: **262 errors across 62 files**.
  No changed-file typing error was identified in this receiving package.

### Memory-authority handoff

Strategy's exact four documentation files were received without modifying
checker code, canonical-spine registration, baselines, or tests:

* `docs/architecture/Vesper Unified Context and Memory Plan.md` is now a
  bounded active integration contract rather than an expired blocked rollout
  plan.
* `docs/architecture/Memory Architecture.md` and its README entry route
  policy/retention/execution authority to the accepted canon and current
  roadmaps.
* `docs/archive/vesper-context-memory-plan-pre-reconciliation-2026-09-08.md`
  preserves the full former plan and original metadata as historical evidence.

No remote push, deployment, provider/flag activation, generated-contract sync,
blanket exemption, baseline raise, or Life-source merge occurred. The isolated
Compose project remains disposable and should be stopped/removed by the
receiving owner after any further database work; its volumes were not used for
dogfood or production data.

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

## Final bounded receiving round — September 8

The candidate was rebuilt with coordinated sibling checkouts so the backend could
exercise the previously environment-bound mobile/workspace parity and snapshot
tests. The candidate branch is local-only at `ab13107b6`
(`chore: reconcile audit and documentation gates`), on top of the received Life
and offline-lifecycle commits. No remote publication, deployment, provider or
flag activation, generated-contract sync, or shared-daemon restart occurred.

### Candidate evidence

* The four enum-parity tests and two frontend snapshot test files pass in the
  coordinated layout: **16 passed / 3 skipped**. The skips are intentional
  snapshot prerequisites, not parity failures.
* The dead-handler audit now scans tracked Python files in a Git checkout,
  falls back recursively only for non-Git fixtures, and counts lexical
  word-boundary references explicitly (including repeated same-line and
  comment/docstring matches). Regression coverage includes ignored and
  untracked files. The full audit is **155 handlers / 155 alive / 0 dead**;
  its focused test file passes **10**.
* The full offline backend suite, with the repository's required exclusions,
  completed without the prior end-of-suite stall: **21,321 passed / 14
  skipped / 1 failed / 1,422 deselected / 53 xpassed**. The single failure is
  the existing background-memory test passing a `MagicMock` into the local
  SentenceTransformer path; it is outside this audit/docs package and no
  baseline or quarantine was changed.
* The connected disposable Postgres run was executed serially after a fresh
  migration to `lifeorgpipelinemerge01`: **1,364 passed / 23 skipped / 4
  failed / 21,420 deselected** in 207.38s. The four failures are bounded
  existing debt: missing canonical Brooklyn dogfood seed, a read-pointer
  concurrency flake (passed on targeted rerun), a retained-projector race
  (passed on targeted rerun), and the J08 date-rollover fixture at the current
  UTC boundary. The targeted rerun was **2 passed / 1 failed** (J08 only).
  The earlier xdist attempt also exposed shared-fixture cleanup deadlocks and
  is not treated as the connected contract.

### Documentation gate reconciliation

The candidate mechanically repaired the stale backend header/symbol and broken
relative links, promoted the current AI Ops Safety Plan to active authority,
and marked five expired August working documents historical/superseded rather
than extending their expiry. The final checks are green:

* headers, status, links, symbols, and feature coverage all pass;
* child product-document governance is **15 passed** (including the prior five
  context-memory governance tests); and
* the root current-state inventory was regenerated with
  `python3 scripts/render_current_state.py --write`.

Strategy's four context-memory files were compared against the canonical dirty
backend checkout byte-for-byte; all four matched exactly. They were then
committed as the reviewed authority handoff (`6ef180ee4`) and the candidate's
Life, audit, and documentation-gate commits were landed locally on backend
`main`, now clean at `0116a12b4`. The candidate branch remains local as an
auditable receipt; no remote publication occurred.

### Boundary and remaining debt

The full mypy baseline remains **262 errors across 62 files**, unchanged. The
connected failures above are not reclassified as green, and the one offline
failure is not silently swallowed. The disposable Compose project was stopped
and removed after evidence collection. The reviewed candidate is landed locally;
no additional feature work is authorized by this receiving round.

## Residual baseline-repair package — September 8

The four residuals from the preceding receiving run were repaired on canonical
backend `main` and landed locally at `78ea8a05f` (`fix: close residual
integration test boundaries`). The package is intentionally narrow: it fixes a
real read-pointer race and repairs three test contracts without changing the
feature surface, baselines, hooks, or coverage policy.

### Repairs

* `mark_as_read` now serializes each `(conversation_id, user_id)` pair with a
  transaction-scoped PostgreSQL advisory lock, reads the marker under
  `FOR UPDATE`, and applies the monotonic message/timestamp comparison before
  updating or inserting. The previous scalar subquery was not safely correlated
  to the conflict target and produced PostgreSQL `CardinalityViolation` under
  concurrent writers (`more than one row returned by a subquery used as an
  expression`).
* The cross-trip subscriber test drains only the subscriber-owned background
  task set; it no longer gathers unrelated event-loop tasks that can feed a
  `MagicMock` into the local embedding model.
* The Brooklyn runtime certifier test creates and removes only its exact
  `elif@dogfood.local` user and `paulie-gees-greenpoint` venue when a disposable
  database does not already contain the canonical seed.
* J08 seeds an explicit Tokyo-local date/instant and is parametrized on both
  sides of the UTC/local-midnight boundary.

### Evidence on the landed tree

* Full offline suite (required exclusions: `not requires_postgres`, `not
  requires_dogfood_wedge`, `not requires_api_keys`): **21,322 passed / 14
  skipped / 1,423 deselected / 53 xpassed / 6 warnings** in 199.07s.
* Full serial connected suite against a fresh disposable Compose project
  (`vesper-residual-20260908`, Postgres `54772`, Qdrant REST `54773`, Qdrant
  gRPC `54774`, migration head `lifeorgpipelinemerge01`): **1,369 passed / 23
  skipped / 21,420 deselected / 1 warning** in 239.29s.
* Focused residual checks: cross-trip subscriber **9 passed**; full read-state
  file **11 passed**; read-pointer concurrency **10/10 repeated passes**;
  retained-source projector **10/10 repeated passes** plus **5/5** sibling-order
  rounds; Brooklyn plus both J08 rollover cases **3 passed**.
* Commit-stage hooks and `git diff --check` passed. The final tested backend
  tree is exactly the landed `main` tree at `78ea8a05f`; its worktree is clean.

This closes the delegated residual package. The repository-wide mypy baseline
remains a separate **262 errors across 62 files** and was not broadened into
this repair. No remote push, deploy, provider activation, feature flag change,
or shared-daemon restart occurred. The disposable Compose project was removed
after the connected run.

## Strategy documentation recheck — September 8

During program-roadmap reconciliation at workspace `b16857d`, backend
`78ea8a05f` and mobile `5f41be821`, `make docs-check` exited 2 because child
document admission rejects five files typed `working` with historical or
superseded status. Its accepted working statuses are `active` and `blocked`.
This does not contradict the recorded passing application suites, but it
corrects any inference that all cross-repository documentation gates passed.

Affected backend paths under `docs/working/`:

- `editorial-map-qa-gates.md`
- `outcome-inference-and-reconciliation-2026-08-06.md`
- `session-log-product-model-and-outcome-inference-2026-08-06.md`
- `session-log-product-model-and-spatial-intelligence-2026-08-06.md`
- `spatial-intelligence-roadmap-2026-08-06.md`

Workspace governance, inventory, spine, canon budgets, release projection,
current-state projection, living links, compatibility and Home-surface governance
all passed in that same invocation. This is a lifecycle classification/archival
repair for Integration before the next combined landing, not a new product
decision or permission to raise a baseline, extend expiry, reactivate old plans,
or bypass admission. No backend file or checker was changed in this review.
Explicit validation of the edited receipt also caught its 31-day review window;
the expiry was shortened from October 8 to October 7 to meet the existing
30-day policy. No review period was extended.

## Child documentation lifecycle repair — September 8

The five affected child documents were repaired on an isolated backend branch
and locally received on backend `main` at `262f0963c` (`docs: archive
superseded spatial plans`). Their historical content and existing provenance
links remain intact; only the lifecycle metadata was normalized from invalid
`working` + historical/superseded combinations to `doc_type: archive`,
`status: archived`, with an explicit `archived: 2026-09-08` and metadata review
date. The spatial tracker now explicitly links the current integration roadmap
and says its status lines are historical evidence, not a live queue.

The actual workspace command was rerun after the landing:

* `make docs-check`: **passed**;
* child document admission: **403 post-baseline documents checked**;
* inventory: **600 Markdown files**, with zero merge/investigate/delete-candidate
  entries;
* spine, canon, release, current-state, living links, compatibility and
  Home-surfaces checks: all passed.

This closes the delegated documentation gate without weakening the validator,
reviving an August plan, or changing product/runtime behavior. Backend and
workspace worktrees remain clean; no remote push, deployment, provider or flag
activation occurred.

## Life retained-source organization package — September 8

Integration reviewed and locally landed the bounded real-owner organization
adapter from the isolated Life lane. Backend commits `0af5aacef`
(`life: maintain retained source organization`) and `3c76118b0`
(`test: cover stale source organization replay`) are now on backend `main`,
based on the closed baseline `78ea8a05f`. The package extends the existing
retained-source projector/maintainer only: an eligible Capture creates a
deterministic UTC capture-month Life group, exact owner-revision
representation/deletion events supersede only that source's active derived
memberships, and explicit unrepresentation restores the existing row and
membership. User exclusions and neighboring independent records remain
untouched. The calendar bucket is an explicit shadow policy, not an occurrence,
place, or people interpretation.

No API/OpenAPI/schema/migration, mobile, Home/Places/Chat, serving cutover,
Atlas deletion, provider call, or production flag changed. The remaining
dependency is Capture's richer typed occurred/negative/place/people/locator
evidence envelope; Life must not infer those relations from capture time or
source custody alone.

Evidence on the canonical backend tree:

* focused retained-source/maintenance/source-evidence tests: **22 passed**;
* complete offline `tests/life_projection`: **253 passed / 41 deselected**;
* fresh disposable Postgres at migration head `lifeorgpipelinemerge01`, complete
  connected `tests/life_projection -m requires_postgres`: **41 passed / 253
  deselected**;
* Ruff check and format check for all six changed files: passed.

An earlier run against a concurrently terminated disposable container produced one
connection failure and 37 setup errors; it is infrastructure-invalid evidence,
not a code verdict, and was superseded by the fresh 41-test run above. No remote
push or deployment occurred. Temporary disposable Postgres instances are
stopped/removed after this receipt; active Home/Life worktrees remain preserved.

## Home / Places Source receiving package — September 8

Integration reviewed and locally landed the mobile receiving package from the
isolated Home lane at Travel App commit `6dfd0d8cf` (`feat(mobile): connect Home
and Places source results`), based on app `5f41be821`. The existing
provenance-first `source.inspect` action remains read-only until the user
explicitly chooses **Ask Vesper**. That action submits the existing
`SourceContributionRequestCreate` with exact subject/source refs, bounded root,
context, represented time/zone and a 15-minute request horizon; accepted
`workflow_id` and the existing root-return token open the exact-result route.

The new result screen consumes the existing exact-result hook and renders
pending, ready, unavailable, no-useful-result, expired, changed and terminal
states, including the existing composition/read/direct-state/instrument/link/
receipt/silence/week-shape payload families. Canonical destination/resource
resolution returns to the originating Home or Places root. Unavailable does not
promise later delivery, expiry/change does not present stale claims as current,
and no second request or result store is created.

Evidence on canonical app `main`:

* focused source/result, inspection and Home-routing suites: **32 passed**;
* `npm run typecheck`: passed;
* `npm run lint`: **0 errors / 169 existing warnings**;
* targeted ESLint and `git diff --check`: passed.

The lane also ran the broader seven-suite/52-test focused set; the canonical
rerun above is the directly inspected subset. Native/visual, populated producer
and production Source evidence remain unrun by design; the worker must still
provide a version-bound result with substantive content. No backend, OpenAPI,
generated type, Social transport, Chat/Life layout, booking flow, provider call
or production flag changed. No remote push or deployment occurred.
