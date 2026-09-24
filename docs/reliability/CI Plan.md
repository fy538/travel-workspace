---
doc_type: runbook
status: active
owner: engineering
created: 2026-09-07
last_verified: 2026-09-07
why_new: Describes the actual three-repository CI contract, immutable candidate identity, private checkout credentials, and enforcement checks.
---

# Reliability CI

Use one coordinated checkout: workspace at the job root, backend in
`travel-agent/`, frontend in `travel-app/`. Both children remain independent
repositories. Local worktrees use the same layout.

## Required checks and evidence

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
`scripts/check_check_constraints.py` before and after its full migration
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

- Run `make verify` for the coordinated gate; `make -C travel-agent ci` and
  `npm --prefix travel-app run verify:pr` identify child failures.
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
