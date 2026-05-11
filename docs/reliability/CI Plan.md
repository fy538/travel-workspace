# Reliability CI Plan

The workspace repo is not a superproject, so CI must check out three repos:

- The workspace repo at the job root.
- `travel-agent` into `Travel Agent/`.
- `travel-app` into `Travel App/`.

That shape matches local development and lets the workspace Makefile run the
same commands in CI.

## Current CI Gate

The workspace reliability workflow runs:

```bash
make contract-check
make golden-path-qa
```

This is intentionally smaller than `make offline-qa`. The full offline ladder
is great locally, but the backend suite has thousands of tests and belongs in
the backend repo's own CI. The workspace gate should catch cross-repo contract
drift and MVP journey regressions without duplicating every child-repo check.

The workflow also writes `reliability-report.txt` and uploads it as a GitHub
Actions artifact on every run, including failed runs. That report is a cheap
snapshot of OpenAPI shape, test surface, and the three repo working states.

## Cross-Repo Triggering

The workspace workflow runs on:

- pushes and pull requests in `travel-workspace`
- manual `workflow_dispatch`
- `repository_dispatch` events from child repos

Child repo CI should dispatch the workspace workflow only after its own `main`
CI succeeds. This makes the workspace repo a real coordination gate without
duplicating full child-repo CI inside the parent.

Expected dispatch event types:

- `travel-agent-ci-success`
- `travel-app-ci-success`

Child dispatch jobs intentionally skip with a notice if their dispatch token is
missing. That keeps child CI from breaking before the secret is installed, while
making the missing automation visible in logs.

## Private Child Repo Access

If `travel-agent` and `travel-app` are private, the workspace repo's default
`GITHUB_TOKEN` cannot check them out as sibling repositories. Add a workspace
repo secret named:

```text
TRAVEL_WORKSPACE_CI_TOKEN
```

Use a fine-grained GitHub token with read-only contents access to:

- `fy538/travel-agent`
- `fy538/travel-app`
- `fy538/travel-workspace`

The workflow falls back to `github.token` for public child repos, but the secret
is required for private sibling checkout.

## Child-to-Parent Dispatch Token

Each private child repo needs a separate secret named:

```text
TRAVEL_WORKSPACE_DISPATCH_TOKEN
```

Use a fine-grained GitHub token with `Contents: read and write` access to:

- `fy538/travel-workspace`

This token is used only to call GitHub's `repository_dispatch` endpoint on the
workspace repo. Keep it separate from `TRAVEL_WORKSPACE_CI_TOKEN`, which is a
read-only checkout token owned by the workspace workflow.

## Contract Ownership

The workspace repo is the canonical cross-repo contract gate.

- Backend CI owns backend lint, import boundaries, offline tests, DB tests, and
  manual evals.
- Frontend CI owns app lint, typecheck, and Jest tests.
- Workspace CI owns committed OpenAPI snapshot vs generated frontend type drift
  and deterministic MVP golden-path coherence.

Do not duplicate the full workspace contract check inside `travel-app` CI unless
there is a specific release reason. Duplicating it requires private sibling repo
checkout and tends to become more fragile than the parent coordination gate.

## Promotion Path

Start with:

- `contract-check`
- `golden-path-qa`

Add later if the workflow is stable and runtime is acceptable:

- `mock-real-parity`
- selected trace-specific tests for newly promoted MVP journeys

Do not add live canaries to CI until there is a separate budget, fixture, and
secret-management decision.

## Failure Triage

- Contract failure: run `make sync-types-snapshot`, review
  `docs/openapi.json` and `Travel App/utils/api/schema.gen.ts`.
- Backend golden-path failure: inspect the failing backend test and the trace
  file in `docs/reliability/traces/`.
- Frontend golden-path failure: run the matching Jest command from
  `scripts/golden-path-qa.sh` in `Travel App`.
- Cross-repo checkout failure: verify repo names and permissions in
  `.github/workflows/reliability.yml`.
