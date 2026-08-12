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

**Superseded 2026-08-12, same day.** The original headline below described `main` as red in
both repos for two unrelated pre-existing reasons. Both were fixed and committed directly to
`main` shortly after this note was first written (`travel-agent` commits `0400197d6` and
`2aead3ea2` — not on the A1/A2/A3 feature branch, since fixing a shared gate blocks everyone,
not just this work). **`make -C travel-agent ci` now passes end to end**: ruff, import/lazy-
import/SCC boundaries, all structural gates, mypy (0 errors), the offline suite (17,784 passed,
30 skipped, 56 xpassed in 440.85s), the tool-contract suite (1,016 passed in 7.48s), and the
eval baseline replay — `✅ Preflight green. Safe to push.` in 493.3s total (~8.2 min). See the
`backend-ci-recheck` record in the JSON.

This is the number that should be used for the A2 speed target ("fast path ≤ 50% of median
`make verify`") going forward — not the 0.12s fast-failure figure below, which only ever
reflected a broken gate, not real pipeline cost. Still only one measurement, so the
three-repetition gap remains open.

**Original finding (2026-08-12, superseded above):** the verification loop was red on `main`,
in both repos, for two unrelated, pre-existing reasons that predated this measurement:

1. `make -C travel-agent ci` failed in 0.12s at `ruff format --check` —
   `backend/concierge/agent.py` was out of formatting sync with the pinned ruff version. **Fixed**
   (`0400197d6`).
2. `npm run verify:full` (travel-app) fails in 15.6s at the `home-surface-budgets` check —
   `utils/tripsHomeSectionPlan.ts` is 285 lines against a 267-line budget. Matches the
   existing memory note that both design ratchets fail on main. **Still open** — flagged
   separately, not fixed here or since.

A third pre-existing defect was found while getting supplementary timing: `mypy` reported 5 real
type errors in `backend/api/routes/occurrence_reconciliation.py:208` (a `**dict[str, object]`
unpacked into a `to_thread` call whose target has more specific parameter types). **Fixed**
(`2aead3ea2`) — replaced with a `TypedDict(total=False)`, preserving the exact kwarg-presence
behavior two existing tests depend on (an earlier attempt that always passed the fields
explicitly was type-correct but broke those tests; caught before committing).

`make contract-check` and `make doctor`, run against `main`, both pass cleanly — the OpenAPI
snapshot, app projection, generated-schema diff, and place-identity seams are all current.
`contract-check` additionally fails at its very last step here, but only because that step
(`npm run schema-bridge`, added by A1) doesn't exist on `main` yet — expected until the A1
branch lands; see the commit that added it.

**Still open, unrelated to any of the above:** `npm run verify:full` on `main` remains red
today at the `home-surface-budgets` step (item 2). The frontend side of this baseline has not
been re-measured since that fix landed, because it hasn't landed.

## What was actually measured (1 repetition each, not 3)

| Label | Command | Exit | Wall time | Notes |
|---|---|---:|---:|---|
| `doctor` | `make doctor` | 0 | 0.61s | clean |
| `backend-ci` | `make -C travel-agent ci` | 2 | 0.12s | **stale** — fails at `ruff format --check`; both blocking gates fixed same day, see `backend-ci-recheck` below |
| `contract-check` | `make contract-check` | 2 | 9.75s | passes through snapshot/projection/schema-diff/place-identity (~9.3s of the 9.75s); fails only at the new A1 schema-bridge step, which doesn't exist on `main` yet |
| `frontend-verify-full` | `npm run verify:full` (travel-app) | 1 | 15.56s | fails at `home-surface-budgets` inside `verify:fast`, before `verify:pr`'s Jest run or `npm test -- --ci` ever starts (still pre-existing, still open — see Headline finding) |
| `backend-mypy-supplementary` | `mypy --config-file mypy.ini backend/` | 1 | 8.28s | **superseded** — found 5 real errors, fixed same day (`2aead3ea2`); mypy is now clean, see `backend-ci-recheck` |
| `backend-offline-pytest-supplementary` | `pytest tests/ -q -k "not requires_postgres and not requires_api_keys"` | 0 | 445.50s (~7.4 min) | 17,776 passed, 0 failed, 30 skipped — supplementary at the time (bypassed the ruff-format gate), now subsumed by `backend-ci-recheck`'s real end-to-end run |
| `backend-ci-recheck` | `make -C travel-agent ci` | **0** | **493.34s (~8.2 min)** | **the current, real, end-to-end number.** Both blockers fixed and committed to `main`. Offline suite: 17,784 passed, 30 skipped, 56 xpassed in 440.85s. Tool-contract suite: 1,016 passed in 7.48s. Plus gates, mypy, eval-ci replay. `✅ Preflight green. Safe to push.` |

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

The one piece of unambiguously good news in this baseline: 17,776 offline backend tests pass
cleanly in 7.4 minutes. The two things actually blocking a green `make verify` are narrow and
already named (agent.py formatting, tripsHomeSectionPlan.ts budget) — not a systemically broken
test suite underneath them.

## Fast-path router (`make verify-changed`)

`scripts/verify_changed.py` (wrapped by `scripts/verify-changed.sh`) independently diffs the
workspace, backend, and frontend Git repositories, then classifies their prefixed paths and
selects the smallest command set that covers the change. Every repository requires its own
explicit base ref; the router never applies a commit ID from one repository to another or
guesses `main`. It falls back to the full `make verify` for anything unrecognized or
historically risky. `make verify` remains the required pre-push/merge gate — this is a local
speed-up in front of it, not a replacement.

```bash
make verify-changed \
  WORKSPACE_BASE_REF=origin/main \
  AGENT_BASE_REF=origin/main \
  APP_BASE_REF=origin/main                            # run it
make verify-changed \
  WORKSPACE_BASE_REF=origin/main \
  AGENT_BASE_REF=origin/main \
  APP_BASE_REF=origin/main DRY_RUN=1                 # show the selection without running it
```

### Decision table

| Path class | Matches | Selected command(s) |
|---|---|---|
| `high_risk` | shared test config, `conftest.py`, migrations, dependency manifests, workspace/child `scripts/*.{py,sh,mjs}`, API routes/models, `docs/openapi*.json`, `schema.gen.ts`, root/child `Makefile`, `.pre-commit-config.yaml` | `make verify` (short-circuits — any one high-risk or unrecognized file forces this for the whole change set) |
| `unknown` | anything not matched by another class | `make verify` (same short-circuit) |
| `frontend` | `travel-app/**/*.{ts,tsx}` | `npm run verify:fast` + `npx jest --findRelatedTests <changed files>` |
| `backend` | `travel-agent/**/*.py` | `make -C travel-agent ci` — **no dependency-to-test mapper exists yet** (see below), so this is the full backend CI, not a narrowed subset |
| `docs` | `docs/**/*.md` | `make docs-links-check docs-spine-check docs-canon-check`, plus each referenced checker's real executable test command (e.g. `python3 -m pytest tests/scripts/test_check_import_scc.py`) |

A change set spanning multiple classes gets the union of their commands, unless any file is
`high_risk`/`unknown`, in which case the whole set falls back to `make verify` alone. The router
also reads committed, staged, unstaged, and untracked changes from every repository. If a
coordinated workspace checkout does not contain both child repositories, it refuses to launch a
full gate against unrelated canonical checkouts and exits nonzero instead.

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
are both unit-tested and exercised against this workspace's real three-repository state. The
router covers committed, staged, unstaged, and untracked child-repository changes; the recorder
now records all three commit states and propagates a completed command's nonzero exit code.
What's missing is repetition count and historical-diff validation depth, not working code.
