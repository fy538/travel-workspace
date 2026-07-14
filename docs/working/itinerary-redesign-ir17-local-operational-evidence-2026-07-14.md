---
doc_type: working
status: active
owner: backend / operations
created: 2026-07-14
last_verified: 2026-07-14
expires: 2026-08-13
why_new: Revalidate IR-17 current-schema CI, selected-trip shadow/dual-read, threshold blockers, and rollback after the adversarial remediation.
source_of_truth_for: [itinerary-redesign-ir17-local-operational-evidence-2026-07-14]
---

# Itinerary redesign IR-17 — local operational evidence

**Date:** 2026-07-14  
**Lane:** itinerary-foundation  
**Outcome:** local schema, selected-trip, and rollback mechanics pass; shadow
stage advance and compatibility retirement remain blocked on external cohort
evidence and approved thresholds

## Current-schema CI

A new disposable PostgreSQL database named `vesper_ir17_gate_20260714` was
created on the local PostgreSQL service and upgraded from an empty database
through the feature branch's single head, `ir18a001`. This is feature-branch
evidence only. The separate current-main integration branch owns its required
Alembic merge revision; this lane did not add a competing merge migration.

Commands:

```bash
PGPASSWORD=localdev createdb -h localhost -p 5433 -U vesper \
  vesper_ir17_gate_20260714

DATABASE_URL=postgresql://vesper:localdev@localhost:5433/vesper_ir17_gate_20260714 \
  /Users/feihuyan/travel-workspace/travel-agent/.venv/bin/alembic upgrade head

PYTHONPATH=. \
DATABASE_URL=postgresql://vesper:localdev@localhost:5433/vesper_ir17_gate_20260714 \
  /Users/feihuyan/travel-workspace/travel-agent/.venv/bin/pytest -q \
  tests/core/test_itinerary*.py \
  tests/core/test_trip_lifecycle.py \
  tests/api/test_itinerary*.py \
  tests/scripts/test_audit_itinerary*.py

PYTHONPATH=. \
DATABASE_URL=postgresql://vesper:localdev@localhost:5433/vesper_ir17_gate_20260714 \
  /Users/feihuyan/travel-workspace/travel-agent/.venv/bin/pytest -q \
  tests/api/test_plan_edit_commit.py \
  tests/api/test_plan_edit_preview.py \
  tests/api/test_plan_state.py \
  tests/api/test_proposals_api.py \
  tests/api/test_trip_folio.py \
  tests/api/test_trips_api.py \
  tests/core/test_map_state_builder.py \
  tests/core/test_map_state_builder_modes.py \
  tests/core/test_plan_edit_intent.py \
  tests/core/test_trip_phase_timezone.py \
  tests/core/test_account_deletion.py \
  tests/core/test_accommodation_writeback.py \
  tests/booking/test_restaurant_writeback.py \
  tests/booking/test_smaudit_restaurant_writeback.py \
  tests/scenarios/test_j05_plan_edit_commit.py
```

Results:

- schema: `ir18a001 (head)`, one feature-branch head;
- itinerary/API/audit command: **388 passed**, one non-failing Pydantic enum
  serialization warning in a dark-route fixture;
- compatibility/Plan/Map/Folio/account command: **384 passed**;
- total distinct tests across the two commands: **772 passed**.

The first run found one real current-schema defect: after a failed provider
callback recovered into pending replacement work, operation detail remained on
the earlier `provider_failed` state. The history projector was treating a
hard-coded subset as permanently terminal even though provider failure is
recoverable. It now projects the latest append-only operation transition. The
provider retry proof and complete current-schema commands passed after that fix.

## Selected-trip shadow and dual-read proof

`test_selected_trip_shadow_dual_read_and_read_rollback_are_coherent` is a
PostgreSQL-backed local operational fixture. It selects one explicit trip at
`read_only`, independently enables lifecycle shadow, policy shadow, and
canonical reads, and then exercises both Plan and Map.

Measured local fixture result:

| Measure | Result |
|---|---:|
| Selected trips | 1 |
| Plan lifecycle shadow events | 1 match |
| Map lifecycle shadow events | 1 match |
| Move-policy shadow events | 1 match |
| Unknown/adapter-error policy events | 0 |
| Plan canonical authorities | 1 / 1 |
| Map canonical authorities | 1 / 1 |
| Plan/Map projection-version mismatches | 0 |
| Legacy/Plan/Map event-identity mismatches | 0 |
| Canonical Map identity-complete failures | 0 |

This proves the selected-cohort instrumentation and dual-read mechanics on an
empty current schema. It is deliberately not relabeled as production launch
evidence: one synthetic trip is not a representative operating cohort and has
no product/operations-approved policy threshold.

## Current cohort and threshold result

The read-only lifecycle audit was rerun at `2026-07-14T12:00:00Z` against the
existing local dogfood corpus:

```bash
PYTHONPATH=. /Users/feihuyan/travel-workspace/travel-agent/.venv/bin/python \
  scripts/audit_itinerary_lifecycle.py \
  --as-of 2026-07-14T12:00:00Z
```

The result remains 13/13 evaluated, zero projection errors, zero unexplained
disagreements, zero canonical Plan/Map disagreements, and 13/13 legacy Plan and
Map agreement. It still fails the recorded IR-01 threshold because it has six
destinations without timezone evidence, lacks Ideation, Final prep, and Live,
and lacks Cancelled terminal coverage.

The local selected-trip fixture supplies a non-empty policy instrumentation
proof, but it does not supply a representative selected-cohort baseline or an
approved policy threshold. No numerical threshold was invented. The governed
shadow evidence JSON therefore remains false, and the executable gate correctly
returns exit code `2` with these blockers:

- `lifecycle_disagreement:gate_failed`;
- `policy_disagreement:baseline_not_measured`;
- `policy_disagreement:threshold_not_recorded`;
- `policy_disagreement:empty_sample`;
- `policy_disagreement:gate_failed`.

## Rollback and retirement drills

Commands:

```bash
PYTHONPATH=. \
DATABASE_URL=postgresql://vesper:localdev@localhost:5433/vesper_ir17_gate_20260714 \
  /Users/feihuyan/travel-workspace/travel-agent/.venv/bin/pytest -q \
  tests/core/test_itinerary_rollout.py::test_flag_only_rollback_preserves_canonical_ledger_and_restores_compatibility_read \
  tests/core/test_itinerary_rollout_operational_evidence.py::test_selected_trip_shadow_dual_read_and_read_rollback_are_coherent
```

Result: **2 passed**. The drills prove that lowering the stage immediately
restores the compatibility Plan read while preserving canonical operation,
transition, projection, and structural state.

The retirement evaluator also correctly returned exit code `2`. Remaining
blockers are the open compatibility window, unproven old-client parity,
unproven shadow/dual-read cleanliness, unproven legacy-bypass cleanliness, and
incomplete selected-cohort canonical-history evidence. Local tests cannot close
those production observation gates.

## Decision

- Keep production rollout stage and behavior flags dark.
- Do not start or close the compatibility window from local evidence.
- Do not retire Folio, legacy reads/writes, schema, enums, adapters, or records.
- Next external action remains selection/remediation of a representative cohort,
  collection of policy telemetry, and product/operations approval of the
  measured threshold.
