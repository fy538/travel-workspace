# Testing & CI Audit — 2026-07-08

> Status: 4/7 findings fixed (needs-chain flatten, pytest-timeout,
> --durations, 21 FE test failures); Finding 6 investigated and
> deliberately NOT changed (empirically confirmed real DB contention risk);
> coverage-floor (7) remains open
> Owner: founder / engineering
> Created: 2026-07-08
> Relates to: [Dogfood clock reconciliation](dogfood-clock-reconciliation-2026-07-08.md)
> (the CI outage that prompted this audit)

## Why this exists

Investigating a repo-wide CI outage (every run failing in 2-3s, root cause:
Actions runner/billing) surfaced something bigger: **the CI test tier has
produced no real signal since at least mid-May**, independent of the outage.
This doc records what was found and what to do about it.

## Finding 1 — the `needs:` chain silently starved the test tier for months

`test`, `test-db`, `eval-replay`, `dogfood-persona-gate` all had
`needs: [lint, import-boundaries]`. Every sampled run back to **2026-05-17**
shows these jobs `skipped`/`cancelled` — because `lint`/`import-boundaries`
were failing, which is an intentional fail-fast optimization for CI minutes,
but has the side effect that a trivial doc-lint nit **completely hides**
whatever the test suite would have said. Two independent signals (does the
code lint clean? does the product work?) had been silently collapsed into one.

**Fixed 2026-07-08**: flattened `.github/workflows/ci.yml` — `test`,
`test-db-migrate`, `dogfood-persona-gate`, `eval-replay` no longer gate on
`lint`/`import-boundaries`; they run independently and in parallel.
`test-db` keeps `needs: [test-db-migrate]` only — that one *is* a genuine
fail-fast (a broken migration fails every DB test anyway, so it isn't hiding
independent information, unlike lint).

## Finding 2 — `pytest-xdist` has been broken since 2026-05-04

`tests/voice/test_agent.py` parametrized a test over
`list(_TOOL_TRIGGER_WORDS)`, a `frozenset` — iteration order is
hash-seed-dependent per process, so xdist workers collected different test
orders and aborted with `Different tests were collected between gw0 and gwN`.
CI's `test` job runs `-n auto`, so **even if the needs-chain above hadn't
starved it, this would have prevented the job from ever completing** since
the line landed.

**Fixed 2026-07-08**: `sorted(_TOOL_TRIGGER_WORDS)` instead of
`list(...)`. Verified: the file collects consistently under `-n 4`; a full
local parallel run now proceeds past collection.

## Finding 3 — no timeout means one hung test hangs everything

No `pytest-timeout` was installed. Concretely reproduced during this audit: a
full local `-n auto` run of the ~10.8k-test suite stalled at 98% complete for
20+ minutes with zero progress — a real hang, not slowness — and had to be
killed. This is the same failure class as the pre-push hook hang fixed
earlier the same day (`check_docs_symbols.py`).

**Fixed 2026-07-08**: `pytest-timeout>=2.3.1` added; `timeout = 120` set as
the suite-wide default in `pyproject.toml`. Verified: an artificial 999s-sleep
test is correctly killed at the configured bound, standalone and under `-n 2`.
Per-test override remains available via `@pytest.mark.timeout(N)` for
legitimately slow tests.

**Immediate value**: rerunning the suite with the timeout live is expected to
name the exact test that was hanging (previously invisible — a silent hang
gives no test name, just no progress). See the follow-up run's `--durations`
output once it completes.

## Finding 4 — no visibility into the slow tail

Added `--durations=25` to both bulk pytest invocations in `ci.yml` (`test`
job's offline+coverage step, `test-db` job's DB-backed step) so the slowest
tests are named on every run instead of inferred from a stopwatch.

## Finding 5 (not yet fixed) — 19 real FE test failures on current `main`

Under `TZ=UTC` (the blessed local invocation), 5 suites fail for real reasons,
not CI/env flakiness:

| Suite | Failures |
|---|---|
| `RevertConflictSheet.test.tsx` | 4 |
| `story.smoke.test.tsx` | 9 |
| `changes.smoke.test.tsx` | 2 |
| `trips-home.screen.test.tsx` | 3 |
| `journey-11-mock-walk.smoke.test.tsx` | 1 |

These map onto the 07-05/06 landing wave (F-series proposals, story-share,
Changes redesign). **J11 (Atlas candidate → memory control) mock-walk
certification is currently red** and nobody has seen it, because CI hasn't
executed since before these changes landed.

**FIXED 2026-07-08** (travel-app branch `fe-test-fixes`, PR #64) — all 19,
plus 2 more (`ProposalReceipt.test.tsx`) that only surfaced on a full-suite
run, for 21 total. Two root causes, none real regressions, each confirmed
against current component/hook source before any assertion was touched:
stale copy/labels (`'Today'`→`'TODAY'`, `'Keep'`→`'Decline'`, a removed
generic label), and stale prop/mock interfaces (`RevertConflictSheet`
became a 3-state machine with a required `sheetState` prop the tests never
passed; several screens gained new `data` hooks the tests' mocks were never
extended to cover). Verified: `npm test` — 351/351 suites, 2701/2701 tests,
all green.

## Finding 6 — `test-db`'s bulk step runs serially — INVESTIGATED, NOT CHANGED

Initially flagged as a likely quick win (parallelize to match `test`'s `-n
auto`). **Tested empirically before changing anything, and the result
overturned that assumption.**

Comparing `pytest tests/core/ tests/scenarios/` serial vs `-n auto` against
the *same* local DB state:

| Mode | Result |
|---|---|
| Serial | 36 failed, 2097 passed, **0 errors** |
| `-n auto` | 43 failed, 2000 passed, **90 errors** |

The 90 errors are new under parallel — `test_world_model.py` in particular
fails only in combination with the rest of the DB-touching suite (27/27 pass
when run alone under `-n auto`). This points to genuine connection/resource
contention when many xdist workers hit **one shared Postgres instance**
simultaneously — the same class of confound documented in the "Full-suite
failure count" section above, but now shown to be a property of the
parallelism itself, not just a dirty local dev DB.

**Conclusion: do not parallelize `test-db`'s bulk step.** The serial
execution looks like an oversight in isolation but is very plausibly the
correct call once DB contention is accounted for — flip it and CI's `test-db`
job would likely become measurably flakier, the opposite of the intended
speedup. No code change made. If DB parallelism is wanted later, it needs
either connection-pool tuning (e.g. a larger `max_connections` + pool size
on the CI Postgres service) or splitting the DB-touching suite across
multiple isolated database instances, not just adding `-n auto` to the
existing single-instance setup.

## Finding 7 (not yet fixed) — coverage has no threshold

`--cov-report=term-missing` / `--cov-report=xml` run in CI but nothing
enforces a floor (`--cov-fail-under`). Currently decorative. A ratchet
(matching this repo's existing pattern — commit-count-only-decreases,
color-budget, fontSize-budget) would convert it to enforcement.

## Also found, out of scope for this pass

- CI's `lint` job runs several Python scripts via bare `python3` with no
  `requirements-dev.txt` install step — works only because the GitHub-hosted
  runner image happens to preinstall PyYAML. Fragile; one dependency bump on
  the runner image away from breaking silently.
- No CI health canary exists — nothing would have caught either the 4-day
  runner outage or the 2-month test-tier starvation faster than "someone
  happens to look." See the dogfood-clock-reconciliation doc's outage
  writeup for the concrete recommendation (alert on N consecutive
  sub-5-second run conclusions).

## Verification log

- `tests/voice/test_agent.py -n 4`: 50 passed (was: instant collection abort)
- Artificial timeout probe: fires correctly at configured bound, standalone
  and under `-n 2`
- `.github/workflows/ci.yml`: YAML-valid post-edit; job graph manually
  reviewed (no orphaned `needs:` references)
- Full local `-n auto` run with timeout protection live: **completed in
  3:11** (was: hung indefinitely at 98%, killed after 20+ min with zero
  progress). This is the headline proof that Finding 3's fix works —
  independent of the failure count below.

### Full-suite failure count — NOT obtained this session, confound documented

Three attempts to get a trustworthy pass/fail count all hit the same
external confound: **another session's `pytest tests/concierge/` process was
running against the same local Postgres for 40+ minutes** (PID 57668,
started 12:56AM, only 17s of CPU time accumulated in that span — itself
possibly stuck, not just slow; not touched, as it isn't this session's
process to manage).

1. Parallel (`-n auto`) run: 112 failed, 52 errors. Sampled errors were
   `sqlalchemy.exc.OperationalError` at fixture *setup* — a connection-pool
   symptom, not a test regression.
2. Checked `pg_stat_activity`: only 13/100 connections in use at rest — ruled
   out a sustained pool exhaustion, consistent with a *transient* burst
   during `-n auto` worker startup instead.
3. Reran the exact 164 failed/errored IDs serially (no xdist, minimal
   connection use): 93 still failed — but the raw output shows
   `+++ Timeout +++` markers mid-run, meaning `pytest-timeout` (120s) was
   firing on tests slowed past that bound by the *other* session's ongoing
   DB load, not real hangs. Still confounded, just via a different mechanism.

**Conclusion:** no number from this session should be treated as the real
backend failure count. Re-run `pytest tests/ -n auto` (or the CI-equivalent
invocation) when no other process holds the local Postgres, and use that
result — not the numbers above — to decide what's real. The FE finding
(Finding 5, 19 failures under `TZ=UTC`) is unaffected by this — the frontend
suite has no DB dependency and was not run concurrently with anything.
