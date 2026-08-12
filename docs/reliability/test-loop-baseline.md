---
doc_type: runbook
status: active
owner: workspace test-infrastructure owner (unassigned)
created: 2026-08-12
last_verified: 2026-08-12
why_new: First machine-recorded verification-loop baseline for this workspace, built by scripts/measure_verification.py; no prior doc measured make verify/make -C travel-agent ci/npm run verify:full timing or trustworthiness.
---

# Verification-loop baseline — A2

> Status: partial — 1 of the required 3 repetitions per command; see gaps below.
> Machine: Darwin 25.5.0, arm64, 14 CPUs, Python 3.14.6 (see individual records for exact commit IDs)

Machine-readable evidence: [`test-loop-baseline.json`](test-loop-baseline.json). Full logs for
every run: [`runs/`](runs/). Produced by [`scripts/measure_verification.py`](../../scripts/measure_verification.py).

## Headline finding

**The verification loop is currently red on `main`, in both repos, for two unrelated,
pre-existing reasons that predate this measurement:**

1. `make -C travel-agent ci` fails in 0.12s at `ruff format --check` —
   `backend/concierge/agent.py` is out of formatting sync with the pinned ruff version.
   Flagged separately (spawned task, not fixed here — not this note's file to touch blind).
2. `npm run verify:full` (travel-app) fails in 15.6s at the `home-surface-budgets` check —
   `utils/tripsHomeSectionPlan.ts` is 285 lines against a 267-line budget. Matches the
   existing memory note that both design ratchets fail on main; not fixed here.

Because both gates fail in the first few seconds, **neither command's later, slower steps have
ever produced a passing baseline this session** — the pipeline's own gates prevented reaching
mypy, the full pytest suite, or the full Jest suite through the normal command path. A red
baseline is not a measurement problem to work around; it's the top-line result of this note.

A third pre-existing defect was found while getting supplementary timing (below), unrelated to
either of the above: `mypy` reports 5 real type errors in
`backend/api/routes/occurrence_reconciliation.py:208` (a `**dict[str, object]` unpacked into a
`to_thread` call whose target has more specific parameter types). Also flagged separately, not
fixed here.

`make contract-check` and `make doctor`, run against `main`, both pass cleanly — the OpenAPI
snapshot, app projection, generated-schema diff, and place-identity seams are all current.
`contract-check` additionally fails at its very last step here, but only because that step
(`npm run schema-bridge`, added by A1) doesn't exist on `main` yet — expected until the A1
branch lands; see the commit that added it.

## What was actually measured (1 repetition each, not 3)

| Label | Command | Exit | Wall time | Notes |
|---|---|---:|---:|---|
| `doctor` | `make doctor` | 0 | 0.61s | clean |
| `backend-ci` | `make -C travel-agent ci` | 2 | 0.12s | fails at `ruff format --check` (pre-existing, flagged) |
| `contract-check` | `make contract-check` | 2 | 9.75s | passes through snapshot/projection/schema-diff/place-identity (~9.3s of the 9.75s); fails only at the new A1 schema-bridge step, which doesn't exist on `main` yet |
| `frontend-verify-full` | `npm run verify:full` (travel-app) | 1 | 15.56s | fails at `home-surface-budgets` inside `verify:fast`, before `verify:pr`'s Jest run or `npm test -- --ci` ever starts (pre-existing, flagged) |
| `backend-mypy-supplementary` | `mypy --config-file mypy.ini backend/` | 1 | 8.28s | supplementary — bypasses the ruff-format gate to get real mypy timing; found 5 real errors (pre-existing, flagged), not a timing artifact |
| `backend-offline-pytest-supplementary` | `pytest tests/ -q -k "not requires_postgres and not requires_api_keys"` | — | — | still running at the time this note was written; append the completed record before promoting this note out of `working/` |

"Supplementary" labels bypass one already-flagged, out-of-scope pre-existing gate failure purely
to get real timing signal for the rest of that pipeline — they do not represent what `make ci`
or `verify:full` currently do end to end, which is: fail in well under a second and 16 seconds,
respectively.

## Gaps against the A2 acceptance bar

Recorded plainly rather than silently narrowed:

- **Three repetitions on a clean commit, no source edits between runs** — not done. Only one
  repetition of each command was captured this session. The reference numbers above should be
  treated as a single data point, not a median. A second and third repetition, run back-to-back
  with no edits, are needed before any of these numbers are cited as "the" baseline.
- **`make test-backend-postgres` measured separately against a disposable database** — not
  attempted; no local Postgres instance was verified available this session.
- **API-key, dogfood, device, and live-service lanes listed as separate coverage** — not
  inventoried here. Do not describe the measured set above as "the full suite."
- **Flaky-test detection (10 reruns on any command with cross-run variance)** — not applicable
  yet with only 1 repetition; blocked on the 3-repetition requirement above.
- **`backend-offline-pytest-supplementary`'s full record** — pending completion; see the JSON
  file for the authoritative up-to-date result once it lands.

## Fast-path router (`make verify-changed`)

`scripts/verify_changed.py` (wrapped by `scripts/verify-changed.sh`) classifies files changed
since `BASE_REF` and selects the smallest command set that covers the change, falling back to
the full `make verify` for anything unrecognized or historically risky. `make verify` remains
the required pre-push/merge gate — this is a local speed-up in front of it, not a replacement.

```bash
make verify-changed BASE_REF=origin/main            # run it
make verify-changed BASE_REF=origin/main DRY_RUN=1   # show the selection without running it
```

### Decision table

| Path class | Matches | Selected command(s) |
|---|---|---|
| `high_risk` | shared test config, `conftest.py`, migrations, dependency manifests, workspace/child `scripts/*.{py,sh,mjs}`, API routes/models, `docs/openapi*.json`, `schema.gen.ts`, root/child `Makefile`, `.pre-commit-config.yaml` | `make verify` (short-circuits — any one high-risk or unrecognized file forces this for the whole change set) |
| `unknown` | anything not matched by another class | `make verify` (same short-circuit) |
| `frontend` | `travel-app/**/*.{ts,tsx}` | `npm run verify:fast` + `npx jest --findRelatedTests <changed files>` |
| `backend` | `travel-agent/**/*.py` | `make -C travel-agent ci` — **no dependency-to-test mapper exists yet** (see below), so this is the full backend CI, not a narrowed subset |
| `docs` | `docs/**/*.md` | `make docs-links-check docs-spine-check docs-canon-check`, plus any checker's own test file the doc text references by name (e.g. mentioning `check_import_scc.py` also runs its test) |

A change set spanning multiple classes gets the union of their commands, unless any file is
`high_risk`/`unknown`, in which case the whole set falls back to `make verify` alone.

**Why backend changes aren't narrowed further:** the doc's acceptance bar calls this out
explicitly — "until a tested dependency-to-test mapper exists, uncertain backend changes select
`make -C travel-agent ci`." No such mapper was built here; inventing one to make the numbers
look better would be exactly the kind of fabrication this whole investigation exists to avoid.
Building one for real (likely from the AST import graph `check_import_scc.py` already
constructs) is follow-on work, not part of this pass.

### Gaps against the A2 acceptance bar

- **20 reviewed historical diffs, zero misses** — not done at the required scale. Four real,
  non-merge commits were spot-checked by hand (not a curated example — the next four non-merge
  commits found in each repo's recent history):

  | Commit | Changed files | Classification | Selected |
  |---|---|---|---|
  | `ee2cf5598` (travel-agent) | `tests/scenarios/test_lisbon_group_disruption_replay.py` | backend | `make -C travel-agent ci` |
  | `82f263e1b` (travel-agent) | `backend/concierge/entry_context.py`, `tests/concierge/test_conversation_seed.py` | backend | `make -C travel-agent ci` |
  | `58e34e9ea` (travel-agent) | `backend/core/scenario_entity_check.py`, `scripts/provision_lisbon_group_disruption.py`, `tests/core/test_scenario_entity_check.py` | `scripts/*.py` is high_risk | `make verify` (forced) |
  | `76d7edca` (travel-app) | two `.tsx` files, `utils/api/schema.gen.ts` | `schema.gen.ts` is high_risk | `make verify` (forced) |

  The last two are the interesting cases, not the easy ones: `58e34e9ea` touches a
  `scripts/*.py` file alongside ordinary backend changes, and `76d7edca`'s own commit message —
  "align proposal UI with generated schema" — is precisely the class of change the
  `schema.gen.ts` high-risk rule exists to always fully verify. Both correctly fell back to
  `make verify` rather than the narrower per-class commands. No misses in this sample, but 4
  diffs is not 20, and this does not meet the doc's acceptance bar. Building the full reviewed
  set — ideally including at least one historical defect the fast path would have *missed*, to
  prove the review is adversarial and not just confirmatory — is real, separate work.
- **Median low-risk fast-path run ≤ 5 minutes and ≤ 50% of median `make verify` duration** —
  not measurable yet: `make verify` itself has never completed a clean run this session (see
  Headline finding), so there is no median `make verify` duration to compare against. This
  target can't be honestly evaluated until the two pre-existing blockers are fixed and a real
  `make verify` baseline exists.

## What's real here, unconditionally

Independent of every gap above: `scripts/measure_verification.py` and `scripts/verify_changed.py`
are both fully unit-tested (22 and 31 tests respectively), both pass, and both were exercised
against this actual repository's real state — not fixtures standing in for it. The routing logic
is deterministic and covers every path class named in the spec plus the unknown-path fallback.
What's missing is repetition count and historical-diff validation depth, not working code.
