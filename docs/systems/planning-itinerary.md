# Planning / Itinerary — System Charter

> Surface: Trips
> Maturity (for MVP): MVP-required
> Status: canonical mutation/read path shipped; deployed/on-device closeout pending
> Last updated: 2026-07-16

## Purpose
Generates and modifies trip itineraries with Claude tool-calling, grounded in the
knowledge base. Owns the itinerary as data and the generation/replan path. Serves
belief #1.5 (*Vesper adapts to the planner*) and the Planning Philosophy (grounded,
spatially coherent, paced).

## Spans (cross-repo)
- Backend: [`travel-agent/backend/planning_agent/`](../../travel-agent/backend/planning_agent/FEATURE.md) (21, custom tool_use loop) + the generation wiring in `concierge/tool_handlers/planning/` + itinerary tables in `core/`.
- Frontend: `travel-app/app/(tabs)/trips/[tripId]/plan`, `components/trip-plan/*` (35), itinerary edit hooks (`useAddBlock`/`useMoveBlock`/`useApplyReschedule`).
- Tables of record: normalized itinerary shape plus the canonical operation,
  transition, proposal, provider-saga, and projection tables. The retained
  `itinerary_edit_log` is a finite historical preference-drain input, not
  itinerary truth.

## Public interface (what other systems may call / read)
- **Entry points:** `agent.py::run_planning_agent()` / `arun_planning_agent()` (generate | replan) → structured `PlanningOutput`. Invoked by Concierge via the `generate_plan` tool (`tool_handlers/planning/_plan.py`).
- **Reads (FE → BE):** canonical plan authority, lifecycle, Map, Trip Details,
  object inspection, proposal, and operation-history endpoints.
- **Consumes:** Memory & Preference (narrative profiles for fan-out search), Places (live hours), venue/experience corpora (Qdrant).
- **Never:** another surface may become a second mutation authority. Manual,
  Vesper, proposal, replan, optimize, recovery, and provider-linked changes
  converge on typed canonical operations or a named narrow projection gateway.

## Owns (source of truth)
The itinerary structure, stable subject lineage, operation/transition ledger,
policy result, exact recovery, and canonical read projections. Generation
births one accepted first draft with `materialize_shape`; subsequent structural
changes use typed operations.

## Invariants (must always be true)
- **Grounded:** never recommends a venue it can't retrieve from the knowledge base (no hallucinated places).
- **Feasibility-checked:** the LIVE feasibility layer runs after YAML emit, before persist (overlap / travel-time / over-packed / meal-gap / closed-venue), fully **fail-open** — repair shifts times deterministically; bounded LLM repair is gated (`FEASIBILITY_LLM_REPAIR_ENABLED`).
- **Spatial + pacing discipline:** spatially coherent days, ~70% capacity (no over-packing).
- **Budget/group binding:** `trip.budget_band` + group context bind into planning context; budget reasoning surfaced in `ReasoningTrace.budget_analysis`.
- **Provider parity:** eval (`EvalToolProvider`, YAML) and prod (`DatabaseToolProvider`) implement the same `ToolProvider` ABC — generation behaves identically offline.

## Failure modes
- Feasibility failure → fail-open (plan still returned; repair best-effort).
- Search returns nothing → the agent narrows/re-queries via fan-out; never fabricates to fill.

## Maturity & validation
- Serves journeys: 03, 05, 06, 08, 10, 12, with privacy/recovery coverage from
  04, 13, 14, and 15.
- DoD state: canonical backend itinerary certification ✅ · app itinerary
  certification ✅ · deterministic J01–J19 logic QA ✅ · static legacy-reader
  and caller scans ✅ · **deployed evidence and on-device walks pending**.
- Concierge planning + the agent both run on **Sonnet**.

## Canonical docs
- why → `product/Planning Philosophy.md` · how → `architecture/Planning Agent Problem Definition.md` · what(be) → `backend/planning_agent/FEATURE.md` · what(fe) → `page-specs/itinerary-editing.md` · `trip-plan.md`.
- Tests: `tests/planning_agent/*`, eval `configs/planning/*`.

## Cross-cutting constraints
- **Graph legibility**: context signals injected into `trip_context` (planning_brief, loved_places, returning_traveler, upcoming_events, weather_forecast) shape the plan silently — they must never be echoed back to the user as labels. See [graph-legibility-doctrine.md](graph-legibility-doctrine.md).

## Open risks / known gaps
- Deployed deletion-lane counts, rollback checkpoint, observation windows,
  reset/reseed proof, and signatures remain operational closeout work.
- One historical edit-log acknowledgement writer remains until its deployed
  backlog is proved drained; it cannot mutate itinerary truth.
- Planner orchestration now separates runtime progress, handoff telemetry,
  plan-ready receipts, and deferred enrichment from policy and canonical
  persistence. `_execute_generate_plan_once` is below the enforced function
  budget; preserve that boundary as planning behavior evolves.
