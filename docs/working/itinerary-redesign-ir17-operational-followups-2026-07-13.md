---
doc_type: working
status: active
owner: backend / frontend / product / operations
created: 2026-07-13
last_verified: 2026-07-13
expires: 2026-08-12
why_new: Close executable IR-17 verification and rollback follow-ups while recording the real rollout and retirement blockers.
source_of_truth_for: [itinerary-redesign-ir17-operational-followups]
---

# Itinerary redesign IR-17 — operational follow-ups

**Date:** 2026-07-13  
**Lane:** itinerary-foundation  
**Outcome:** implementation and local rollback proof complete; cohort exposure and retirement remain correctly blocked

## Current-schema verification

A new isolated PostgreSQL database, `vesper_ir17_20260713`, was created on the
disposable local PostgreSQL service. It upgraded from base through the current
single Alembic head, `ir16a001`. The pre-existing disposable database was not
changed because its revision belonged to a different branch.

The current schema passed:

- 519 backend itinerary, lifecycle, policy, persistence, read-model, API,
  provider, Folio-compatibility, and task tests;
- 210 frontend itinerary, trip-shell, Details, object, operation, Folio, and
  rollout tests across 35 suites; and
- TypeScript with `tsc --noEmit`.

One backend test assumed an unrelated venue row already existed. Its fixture now
creates and removes its own venue, so the itinerary suite is hermetic on an
empty current schema.

## Measured shadow baseline

The lifecycle audit was rerun at `2026-07-13T23:30:00Z` against the current
local corpus without mutating it.

Canonical dogfood cohort:

| Measure | Result |
|---|---:|
| Sample / evaluated | 13 / 13 |
| Projection errors | 0 |
| Unexplained disagreements | 0 |
| Canonical Plan/Map disagreements | 0 |
| Legacy Plan agreement | 13 / 13 |
| Legacy Map agreement | 13 / 13 |
| Missing destination timezone | 6 |
| Present canonical phases | Planning 8; Post-trip 5 |
| Missing required phases | Ideation; Final prep; Live |
| Missing terminal coverage | Cancelled |
| Read-flip eligible | **No** |

All-local diagnostic corpus:

| Measure | Result |
|---|---:|
| Sample / evaluated | 2,448 / 2,448 |
| Projection errors | 0 |
| Unexplained disagreements | 0 |
| Legacy Plan agreement | 2,197 / 2,448 (89.75%) |
| Legacy Map agreement | 1,655 / 2,448 (67.61%) |
| Missing destination timezone | 101 |
| Missing terminal coverage | Cancelled |

The broader corpus initially exposed 31 `planning` trips with no complete date
window as unclassified. Canonical lifecycle intentionally keeps that posture in
Planning while legacy Plan falls back to Ideation. The audit now reports those
rows as `legacy_plan_undated_status_drift`; it does not weaken the canonical
contract or count an unexplained disagreement as passing.

The lifecycle threshold is the already-recorded IR-01 threshold. The measured
dogfood cohort fails it because coverage and destination timezone requirements
are incomplete. A current selected-cohort policy baseline and approved policy
threshold do not exist. The executable shadow evidence therefore records a
zero-sample policy blocker rather than reusing the older migrated-corpus result
as if it were live cohort evidence.

Run the gate with:

```bash
PYTHONPATH=. python scripts/audit_itinerary_rollout.py \
  --target-stage shadow \
  --evidence ../docs/working/itinerary-redesign-ir17-shadow-gate-evidence-2026-07-13.json
```

Expected result: ineligible because lifecycle currently fails and policy lacks
a measured baseline, approved threshold, and non-empty sample.

## Rollback drill

`test_flag_only_rollback_preserves_canonical_ledger_and_restores_compatibility_read`
is a PostgreSQL-backed operational drill. It:

1. selects one synthetic trip at `solo_low_risk` with read, commit, and Move
   flags independently enabled;
2. verifies canonical read authority;
3. previews and commits a cross-day Move through the canonical gateway;
4. lowers only `ITINERARY_ROLLOUT_STAGE` to `off`; and
5. verifies that the compatibility Plan response returns while the moved block,
   exactly one canonical operation, and its two history transitions remain.

The first drill found that the 30-second Plan State cache key did not include
rollout authority, so a cached canonical response could survive a stage
rollback. Canonical and compatibility authority are now separate cache entries;
viewer and trip invalidation evict both. The repeated drill passed against
`ir16a001`.

## Compatibility window and retirement

The compatibility window is declared as follows:

- it starts only when the first selected trip receives the `read_only` shell;
- it remains open for at least 14 consecutive days and through one supported
  mobile-client release cycle;
- any old-client projection mismatch, unexplained dual-read disagreement,
  selected-trip legacy bypass, missing canonical history, or rollback failure
  resets the clean observation interval; and
- closure requires dated production telemetry and an operations sign-off, not
  local tests alone.

The window has not started because the shadow gate is ineligible. No legacy
path, adapter, enum, schema, or record is eligible for retirement. The
retirement evidence intentionally remains false for window closure, old-client
parity, shadow/dual-read cleanliness, bypass cleanliness, and selected-cohort
history completeness. Only the local flag-only rollback drill is currently
true.

Run the retirement gate with:

```bash
PYTHONPATH=. python scripts/audit_itinerary_rollout.py \
  --retirement \
  --evidence ../docs/working/itinerary-redesign-ir17-retirement-gate-evidence-2026-07-13.json
```

Expected result: ineligible with explicit blockers. This is the safe terminal
state until dogfood data, policy telemetry, stage-specific baselines, and the
observation window exist.

## Remaining external actions

These are operational/data dependencies, not unfinished itinerary code:

1. add or select dogfood trips covering Ideation, Final prep, Live, and
   Cancelled, and repair the six missing destination timezones;
2. enable lifecycle and policy shadow only for that selected cohort and collect
   a non-empty policy sample;
3. approve the policy threshold from the measured distribution, then pass the
   executable `shadow` gate;
4. collect and approve each later stage's required signals before advancing it;
5. begin and complete the declared compatibility window; and
6. retire only the paths whose dated production evidence passes the retirement
   evaluator.

Production configuration remains dark. Local evidence does not authorize an
environment flag change or destructive retirement.
