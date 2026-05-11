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

## Promotion Path

Start with:

- `contract-check`
- `golden-path-qa`

Add later if the workflow is stable and runtime is acceptable:

- `mock-real-parity`
- `reliability-report` as an uploaded artifact
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
