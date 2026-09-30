---
doc_type: runbook
status: active
owner: engineering
created: 2026-09-07
last_verified: 2026-09-29
why_new: Describes the actual three-repository CI contract, immutable candidate identity, private checkout credentials, and enforcement checks.
---

# Reliability CI

Use one coordinated checkout: workspace at the job root, backend in
`travel-agent/`, frontend in `travel-app/`. Both children remain independent
repositories. Local worktrees use the same layout.

## Required checks and evidence

### September 30 merge-latency cleanup — staged rollout

**Target:** ordinary final-push-to-merge-readiness under five minutes. This is a
latency objective, not a five-minute timeout that hides failures. Shared
infrastructure, schema/authority changes and unmapped inputs may require broader
checks. Measure queue/setup/execution separately; do not claim the target from
test-count reduction or a mocked runner test.

The new `Merge readiness` workflows emit `Merge ready` in each repository.
They are initially additive: the existing required checks below remain in force
until a real candidate verifies the replacement. Do not waive the known expired
backend compatibility bridges, private-checkout credential failure, or a real
product regression by changing required check names.

Local commands now match the bounded selection policy:

- Workspace: `make verify-changed WORKSPACE_BASE_REF=<ref> AGENT_BASE_REF=<ref>
  APP_BASE_REF=<ref>`; all three bases are independent, explicit Git revisions.
  `--workspace-only` is for the workspace's hosted job, not cross-repo delivery.
- Backend: `make ci-static` plus `make merge-check BASE_REF=<ref>`.
  `scripts/merge_scope.py --base <ref> --database` is the separate selected DB
  run and requires an explicitly disposable database. Shared/unknown changes
  expand to the full suite. Domain routing is a risk-based boundary, not proof
  of a complete transitive dependency graph.
- App: `npm run verify:fast` plus `npm run verify:merge -- --base <ref>`.
  Related tests are combined with a critical smoke floor and source-reading
  convention tests in one invocation. Unknown/deleted/shared configuration
  expands to the full suite, without coverage instrumentation during merge.
- `make verify`, backend `make ci`, and app `verify:full` remain available for
  comprehensive regression, release checks and deliberate diagnosis. Do not
  automatically repeat them after a bounded local preflight and again at every
  intermediate push. Task-specific real-backend and visual acceptance remains.

Offline and DB full-suite marker expressions form a disjoint, exhaustive
partition of non-live tests: offline excludes both `requires_postgres` and
`requires_dogfood_wedge`; DB includes either. Live-key tests remain separate.
Tool contracts, privacy validators, concurrency proofs, storage faults, journey
scenarios, invariants and Atlas tests remain covered by their owning partition;
extra invocations solely for named logging are removed. Report groups from the
same run rather than executing them again.

Test retirement must name a current replacement guarantee or confirm that the
behavior itself was retired. The removed photo-viewer source-location assertion
is covered by `PhotoViewerSurface.test.tsx`, which exercises both reduced-motion
states and dismissal. The private-original test still verifies exact URL,
authorization header and disabled caching; its mock now follows the actual
image-view import. No failing behavior is excused as test cleanup.

**Cutover order (not yet a completed hosted rollout):**

Local implementation evidence on September 29 (dirty candidate based on workspace
`9c22f773`, backend `d01aa120`, app `c9fea932`): backend `ci-static` and app
`verify:fast` passed (app lint retained 169 warnings, zero errors). Workspace
selector/aggregate/measurement regression checks passed 51 tests; backend selector
checks passed 13; app selector checks passed four. Three focused app suites passed
18 tests. These are tooling and targeted-regression evidence, not full-suite or
hosted merge certification. The measured workspace tooling command took 3.094s
on local Darwin/arm64/Python 3.14.6; this does not establish hosted merge latency.
The workspace aggregate tests require both new child workflows, so update its
exact child pins after the child changes land before certifying the root candidate.

1. Publish the new workflows; verify valid selection, intentional violations,
   missing tooling/base, cancellation/failure handling, and actual candidate
   job runs. Preserve exact child pins in the workspace checks.
2. Fix private checkout credentials and existing regressions. Do not promote
   failed or unrun gates. Keep fast security/API/governance checks required
   until their coverage is explicitly incorporated into the new aggregate.
3. Change GitHub protection only after the replacement check has reported:
   replace broad `test`/`test-db`/`Test`/`Logic QA journeys` requirements with
   the validated merge policy. Keep schema/authority and relevant integration
   checks blocking for affected changes; do not confuse skipped with verified.
4. Exclude the old broad test jobs from `pull_request` events only after
   protection is updated. These workflows also contain required fast checks:
   keep their PR triggers and fast jobs, rather than disabling the entire CI
   workflow. Retain main-push, nightly and manual full-regression execution;
   keep deployment separately gated by appropriate exact-revision evidence.
   A broken main regression is repaired promptly or reverted, not ignored.
5. Measure representative docs-only, app, backend and contract changes with
   `scripts/measure_verification.py` and hosted timing data. Review misses as
   well as latency. Five-minute readiness is unproven until measured.

For this solo-owner setup, retain PRs and status checks but remove mandatory
second-person approval. Preserve no-force-push/no-deletion protections. The
founder's consequential design/authority review and actual code review remain;
an author cannot supply their own required GitHub approval.

Cleanup scope stays bounded: retire duplicate execution first, then review
high-maintenance source-string tests and obsolete behaviors. Do not introduce
a new test platform or blanket-delete test directories to meet a count target.

### September 30 integration update

- GitHub approval count is confirmed zero in all three repositories. The
  workspace checkout secret was updated; successful hosted checkout, not the
  secret's existence, is still the access proof.
- Removed all four September 30 AI compatibility registrations together with
  their backend fallback/dispatch/emission paths. Existing mobile angle route
  arguments now serialize as a ConversationSeed entity. Historical promotion
  records and the separately governed promotion API remain readable/supported;
  this retirement removes the agent tool, not that API or proposal confirmation.
- Backend focused tests passed 256 cases; the additional stale-tool dispatch
  rejection passed. App entry-sender tests passed 16. Static checks and the
  regenerated cross-repository contract checks passed; no OpenAPI/type diff
  resulted. Workspace tooling checks passed 110 cases.
- The measured broad backend candidate took 81.668s locally: 21,955 passed,
  four failed, 14 skipped, and 53 xpassed. The failures were three reviewed
  prompt goldens plus the obsolete duplicate Atlas-step assertion; their
  focused follow-up passed 60 tests. This is **not** a clean full-suite rerun.
- The app run passed all 9,035 product tests but failed discovery of two
  third-party tests under local `.tmp` native-build checkouts. Jest now excludes
  that scratch tree from test/module/watch discovery while retaining product
  tests. Hosted validation remains required for the final candidate.
- Hosted app candidate `677dc3781` passed both `Merge ready` (run 36658191461)
  and all existing required checks. Its broad merge test job took 10m15s,
  including setup: the under-five-minute target is **not demonstrated**.
- Backend candidate `1c0b5da7e` passed static and offline checks, but the new
  database job (run 36658333445) failed organizer membership and retained-source
  restoration. The old database gate also failed retained-source tests.
  A fresh explicitly disposable local database reproduced a worker-test race:
  1 failed, 1,458 passed, 38 skipped, 22,042 deselected in 164.71s. A previously
  registered background listener could claim an event before the awaited repair
  sweep. Worker-path tests now isolate prompt delivery while retaining the real
  journal, worker, consumers and owner fences. With the competing listener
  deliberately registered before pytest, the full retained-source test file
  plus charter invariants passed 26 tests in 2.20s. The organizer failure did
  not reproduce; its cause remains unresolved, not certified fixed.
- Default-stage hooks now run at commit only; explicitly declared pre-push
  checks remain. App workspace checkout is narrowed to its single consumed
  Card Catalog file. Latest local hook/checkout and worker-test changes still
  require their own hosted candidate evidence.
- Required-check replacement and disabling broad PR jobs were blocked by the
  execution safety review. Neither was applied. Obtain explicit founder
  approval for that policy cutover; promote only passing replacement gates,
  preserve fast security/contracts/governance checks, and retain main/nightly
  full regression. This is separate from removing mandatory second-person
  approval, which is complete.
- No live-model or native visual claim follows from these results. Workspace
  private-child checkout and coordinated updated child pins remain unverified.

GitHub Actions was disabled in workspace and backend at the September 7 audit.
It has been re-enabled. Their main-branch protection had unrelated frontend
check names; those names have been replaced while preserving strict updates,
review approval, administrator enforcement, and no force pushes/deletions.

| Repository | Required GitHub Actions checks |
| --- | --- |
| workspace | `Contract and golden paths` |
| backend | `lint`, `import-boundaries`, `typecheck`, `test`, `test-db-migrate`, `test-db`, `dogfood-persona-gate`, `eval-replay` |
| frontend | `Lint`, `Frontend governance`, `Security audit`, `Visual evidence contracts`, `Type check`, `Test`, `API types freshness`, `Logic QA journeys`, `QA tooling contracts`, `Design alignment gate` (also emitted for documentation-only PRs) |

The new `package-smoke` job is implemented in this lane. Add it to required
checks after publishing the workflow and verifying its emitted check name;
requiring it before a remote workflow can emit it would block unrelated PRs.

A workflow definition, a completed passing run, and a required branch-protection
check are three different facts. Verify all three on the candidate revision.
A passing local subset cannot certify failed, skipped, or unrun required lanes.
Inspect Actions enablement, branch protection, and run/check conclusions through
the GitHub UI or API when troubleshooting enforcement. Keep screenshots and
native judgments separate from build/typecheck evidence.

## Exact candidate identity

`docs/child-repos.ci-lock.json` pins immutable child commits. On a child-success
repository dispatch, `scripts/resolve_ci_tuple.py` substitutes only the triggering
child SHA after validating repository, event type, and full commit format. The
other child remains pinned. It records the workspace and both child SHAs in
`candidate-tuple.json`, checks actual checked-out HEADs against that tuple, and
uploads the tuple even on failure. The dispatch payload is data, never shell code.

App CI separately pins its workspace/backend dependencies in
`.github/ci-lock.json`. Publish child commits before pinning them in a dependent
repository. A newer untested child commit does not inherit an older tuple's pass.

Backend dispatch waits for every backend prerequisite, including the deployed
artifact import smoke. App dispatch follows its own required lanes. Workspace
CI owns cross-repository OpenAPI freshness, generated contracts, journeys,
registry/governance, and reliability checks. Child CI owns its language and
runtime suites. Explicit failing prerequisites must not become successful skips.

`make contract-check` includes `make cross-repo-fixture-check`: registered mobile
enum unions must match backend CHECK vocabularies, and both canonical persona
and angle snapshots must match the backend exporters. Missing child inputs,
stale mobile snapshots, drift and failed tooling fail this gate. The workspace
checks actual pinned children; backend standalone tests own parser fixtures and
backend snapshots, so they do not require an undeclared mobile checkout.

### Backend schema drift boundary

`test-db-migrate` pairs Alembic autogenerate drift with
`scripts/check_check_constraints.py` before and after its supported migration
round-trip. Both must pass. Alembic 1.19.2 disables its name-only CHECK detector
by default because historical naming conventions cause false positives; that
detector also did not compare expressions under unchanged names. The dedicated
gate compares CHECK-expression multisets after PostgreSQL parses metadata on
empty temporary tables, including column-level constraints. It never alters
persistent tables and requires an explicit disposable test database.

Only bounded equivalences are normalized: enum membership order, unbounded
varchar-to-text casts on enum literals, and sign-versus-zero casts on reflected
bounded numeric columns whose finite range cannot overflow/underflow float8.
Unknown expressions remain differences, duplicate/missing checks remain visible,
and query/DDL errors fail. This is not a general SQL equivalence prover or a
replacement for Alembic's column, index, key and type checks. Renaming alone is
not an enforcement change; migrations still own the physical constraint names.
The regression suite exercises valid, violating and tool-failure cases against
PostgreSQL. Workflow wiring is not evidence of a passing published candidate.

These comparisons cover the registered core metadata, not every physical
table. Experience-graph metadata remains domain-owned and separate. Existing
Trip-evidence compatibility columns refer to Occasion's external key through
an isolated key reference, not an incomplete core-owned Occasion table. The
reference must stay outside core autogenerate metadata; declaring an external
key is not permission to migrate or drop the domain owner's other columns.

**Migration lifecycle (September 23 recovery correction):** an unconditional
`head → base` round-trip conflicts with the existing notification-history
safeguards. CI now requires all of the following, without removing those guards:

1. `scripts/check_migration_lifecycle.py` runs only with
   `TEST_DATABASE_DISPOSABLE=1` and an explicit local PostgreSQL
   `TEST_DATABASE_URL`, refusing nonempty targets before any migration. It
   rejects URL/libpq redirection options and overrides both application DSN
   aliases for migration subprocesses. Its target must be a newly provisioned
   disposable database, not a development database being repurposed.
2. Exercise `base → onboardevt01 → base`, then upgrade through the four
   forward-only revisions: `notifcorr01`, `notifrecord01`, `notifenv02`, and
   `notifenv04`. Attempt each immediate-parent rollback and require its exact
   existing refusal, an unchanged Alembic revision, and unchanged application
   relations, column/constraint/index definitions, views and fixture rows.
   This is not a general audit of privileges, functions or sequence counters.
   Unexpected failures, successful forbidden rollback, changed state, missing
   tooling and timeouts all fail; no arbitrary error is treated as an exemption.
3. Retain a no-chat-message outcome and an envelope-owned deterministic
   delivery through the compatibility rename. Separately exercise the reversible
   `notifenv02 → notifenv03 → notifenv02 → notifenv03` segment. At `notifenv04`,
   include a permitted optional-correlation row that the old CHECK cannot accept.
4. Upgrade to head; run both drift checks and live event/entity parity. Then
   exercise `head → notifenv04 → head` and rerun both drift checks. A new
   unsupported rollback boundary fails this step and requires explicit review,
   not addition to a generic failure allowlist.

Failed full-chain tests can leave a partial revision because older
concurrent-index migrations use autocommit; inspect `alembic_version` and start
subsequent full-chain attempts from a new disposable database, not an assumed
transaction rollback. Local execution verifies the check's stated boundary;
it does not certify an unpublished candidate's GitHub job.

Historical inverses must restore their immediate parent's
schema, not merely change the Alembic revision. In particular, retiring tables
requires frozen parent definitions on downgrade; restoring empty tables does
**not** recover rows previously deleted by the forward migration. CHECK drops
must mark already-conventioned physical names with `op.f`, and dashboard
rollback must release removed-column dependencies before dropping columns.
Restoring schema is not permission to roll production notification history
back through a forward-only boundary.

## Private checkout and dispatch credentials

| Secret location | Secret | Minimum purpose |
| --- | --- | --- |
| workspace | `TRAVEL_WORKSPACE_CI_TOKEN` | Read contents of both private child repos |
| frontend | `TRAVEL_AGENT_CI_TOKEN` | Read backend contents for contract and logic jobs |
| frontend (when workspace is private) | `TRAVEL_WORKSPACE_CI_TOKEN` | Read workspace contents |
| both children | `TRAVEL_WORKSPACE_DISPATCH_TOKEN` | Send repository dispatch to workspace (workspace contents write permission) |

Prefer a narrowly scoped GitHub App token or fine-grained token for these exact
repositories. Secret presence is insufficient: confirm actual checkout access.
Never replace a missing/invalid private token with the caller repository's
`GITHUB_TOKEN` or copy a broad personal credential into CI as a workaround.

The audit observed frontend run `34120618861` fail private backend checkout with
“Repository not found” despite a present secret. Credential renewal/access must
be verified by a subsequent candidate run; this document does not certify it.

## Reproduce a failure

- Use the bounded commands above during iteration. Run `make verify`,
  `make -C travel-agent ci`, or app `verify:full` deliberately when full
  regression is needed, not as an automatic repeat after each small repair.
- Cross-repository release/evidence Git reads clear hook-local repository
  selectors before reading a child's index or HEAD. A passing shell invocation
  alone does not prove the pre-push environment: exercise the hook as well.
  Parent-only tracked paths cannot certify child implementation, and Git failure
  must remain an error/unknown rather than passing evidence.
- Regenerate changed backend contracts with `make sync-types`, then inspect
  both workspace OpenAPI snapshots and `travel-app/utils/api/schema.gen.ts`.
- Use an explicit disposable `TEST_DATABASE_URL` plus
  `TEST_DATABASE_DISPOSABLE=1` for DB lanes. Offline checks must not probe or
  clean a development database.
- Use `make doctor` for source/tool setup, and `./scripts/doctor.sh --services`
  for service diagnosis.
- Use `scripts/new-worktree.sh` for a separate lane. Landing runs the coordinated
  gate before publication and preserves the protected-main review path.

Live providers, corpus mutation, production migrations, and physical-device
judgments have separate evidence and authorization boundaries. Container package
smoke runs the supported operator's `--help` without network or DB access.
