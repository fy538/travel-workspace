---
doc_type: working
status: active
owner: backend
created: 2026-07-13
last_verified: 2026-07-13
expires: 2026-08-12
why_new: Preserve the IR-05 shadow-adapter implementation handoff and its supersession status.
supersedes: []
source_of_truth_for: [itinerary-redesign-ir05-shadow-adapter-progress]
---

# Itinerary redesign IR-05 shadow adapter progress

Date: 2026-07-13
Status: superseded by the completed baseline in
`itinerary-redesign-ir05-shadow-baseline-2026-07-13.md`

## Landed

- A DB adapter loads trip governance, current membership/organizer posture,
  normalized block scope and owner, planned participation, protected provider
  dependencies, and revision.
- Missing block, scope, participation, owner, membership, or revision evidence
  raises a typed fail-closed result. There is no fallback to legacy authority.
- The adapter resolves inspect, Add relative, Move, Replace, Remove, own
  attendance, occurrence, and provider-affecting Replace capabilities through
  the IR-04 resolver.
- Plan State invokes the adapter only when `ITINERARY_POLICY_V2` is explicitly
  enabled. The response payload remains unchanged.
- Shadow Move comparison treats target Confirm as matching legacy Direct commit
  authority while preserving the target confirmation requirement.
- Telemetry now has typed low-cardinality governance, participation scope, and
  actor posture dimensions in addition to operation, outcome, comparison, and
  reason.
- Missing normalized facts emit an Unknown/Denied comparison. Unexpected
  adapter failure is isolated and emits `adapter_error`; Plan State still
  returns the legacy payload.

## Evidence

- Unit tests cover Review proposal routing, Open broad-scope confirmation,
  provider-controller failure, legacy Direct/target Confirm comparison, legacy
  organizer-override disagreement, and Unknown emission for absent owner facts.
- A disposable PostgreSQL database was migrated through `ir03a001`, seeded
  with an explicit Review owner and normalized whole-group participation, and
  queried through the real adapter. A member's Move resolved Propose to the
  named owner. The database was removed.
- Consolidated validation: 163 focused tests, Ruff, diff check, and Alembic
  single-head passed.

## Former remaining gates

- The shared database remains pre-IR-02/IR-03 and was not mutated.
- These gates were closed by the explicit V1 shared-owner migration,
  provenance-aware compatibility defaults, day adapter, target fixture suite,
  and migrated 169-trip/432-block corpus baseline. See the completed baseline.
