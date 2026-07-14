---
doc_type: working
status: active
owner: backend / frontend / product / operations
created: 2026-07-13
last_verified: 2026-07-13
expires: 2026-08-12
why_new: Record IR-17 rollout-control implementation, launch blockers, rollback proof, and retirement gate.
source_of_truth_for: [itinerary-redesign-ir17-rollout-retirement-evidence]
---

# Itinerary redesign IR-17 — rollout and retirement evidence

**Date:** 2026-07-13
**Status:** rollout controls implemented; production stage advance and irreversible retirement blocked on measured evidence
**Lane:** itinerary-foundation

## Outcome

IR-17 now has a fail-closed server rollout resolver. An itinerary flag is not
effective merely because its global boolean is on. Runtime behavior additionally
requires:

1. an explicit `ITINERARY_ROLLOUT_STAGE`;
2. selection through `ITINERARY_ROLLOUT_TRIP_IDS` or
   `ITINERARY_ROLLOUT_COHORTS=canonical_dogfood`; and
3. the independent capability/read/operation flag.

Malformed stages, malformed trip IDs, unknown cohorts, unselected trips,
unreached stages, and dark capability flags all fail closed with distinct
privacy-safe reason codes.

The governed stage order is executable:

1. `shadow` — lifecycle and policy comparisons;
2. `read_only` — canonical read models, history, and Details;
3. `solo_low_risk` — preview/commit plus independently gated Add, Move,
   Replace, and Remove;
4. `open_review` — canonical proposals;
5. `collaboration` — attendance, branches, and Optimize Day;
6. `vesper` — Vesper preparation;
7. `protected_provider` — protected/provider saga;
8. `replan_post_trip` — Replan, completed-entry routing, and write-back.

Stage alone never enables a capability. No umbrella flag turns on the stack.

## Read and write routing

- Plan and Map attach IR-12 canonical authority only for a selected trip whose
  read-model flag and stage are active. The legacy response remains alongside it
  during the dual-read window.
- The mobile build flag permits the target shell code to run, but the trip uses
  that shell only when its response contains server-selected canonical
  authority. If the backend read flag/stage is lowered, or the trip is removed
  from the cohort, the existing trip home remains the compatibility read.
- Canonical preview, commit, proposals, history, provider saga, Vesper, Details,
  completed entry, and write-back routes now resolve per trip.
- Add, Move, Replace, Remove, attendance, branches, Optimize Day, and Replan are
  independently server-gated. Vesper preparation also requires both preview and
  the requested operation family; it cannot prepare a dark operation.
- Legacy Add/Move/Replace/Remove adapters route through the gateway only when
  that exact operation family is active. A failed target preview/commit never
  falls through to a legacy write.

## Compatibility and no-bypass evidence

The new `itinerary.compatibility_path_used` event measures selected-trip legacy
use without recording titles, places, provider references, or other raw trip
content. It currently covers:

- direct Add, Move, Replace/Remove PATCH;
- Mark booked;
- block and planning-revision Undo;
- experience pinning from app and concierge;
- concierge direct update, Move, Add, and Undo.

This makes the remaining compatibility window observable instead of assuming a
new UI means an old producer is unused.

## Launch and retirement gates

`backend/core/itinerary_rollout_gates.py` and
`scripts/audit_itinerary_rollout.py` evaluate the complete governed signal set.
The evaluator contains no invented numerical thresholds. Every required signal
must provide an externally recorded baseline, threshold, non-empty sample,
pass/fail result, and evidence reference.

Irreversible retirement is separately blocked until all of the following are
proved:

- a compatibility window was declared and has closed;
- old-client projection parity is clean;
- shadow and dual-read evidence is clean;
- selected-trip legacy-bypass observation is clean;
- canonical history is complete; and
- a flag-only rollback drill passed.

Therefore IR-17 does **not** yet delete `locked`, Folio compatibility reads,
legacy recent changes, raw-status compatibility, additive schema, canonical
records, or old-client adapters. That is the correct current result: the plan
forbids retirement before evidence, and the required production baselines and
compatibility-window closure have not been supplied.

Rollback lowers a stage, disables one capability flag, or removes a trip/cohort.
It restores compatibility reads without deleting canonical operations, history,
provider partials, proposal state, write-backs, or additive schema.

## Verification

Backend:

- 197 focused rollout/flag/telemetry, canonical route, and concierge mutation
  tests passed.
- Ruff passed on every changed backend, script, and test file.
- Python byte compilation and `git diff --check` passed.
- Alembic remains one head: `ir16a001`.
- A broader read-model/lifecycle run produced 17 passing lifecycle tests; 11
  PostgreSQL read-model tests could not start because the shared local database
  is stale before IR-05 (`trips.itinerary_decision_owner_id` is missing). This
  is an environment migration blocker, not a rollout assertion failure; CI or a
  current disposable database must run those tests before cohort exposure.

Frontend:

- TypeScript passed.
- The rollout fallback test passed (2 tests), proving build permission alone
  does not select a trip and removal of canonical authority restores the
  compatibility shell.
- Targeted ESLint had zero errors; only pre-existing warnings in the two large
  trip route files remained.

## Operational gate

Keep `ITINERARY_ROLLOUT_STAGE=off` and all behavior flags dark until:

1. CI executes the current backend suite against `ir16a001`;
2. IR-00 receives measured baselines and approved numerical thresholds;
3. a selected-trip evidence JSON passes `scripts/audit_itinerary_rollout.py`
   for the requested next stage; and
4. rollback is drilled by removing the selected trip or lowering the stage and
   verifying the legacy read returns while canonical records remain.
