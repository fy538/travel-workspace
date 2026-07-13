# Planning / Itinerary — System Charter

> Surface: Trips
> Maturity (for MVP): MVP-required
> Status: wired (backend shipped; on-device generation walk unvalidated)
> Last updated: 2026-06-27

## Purpose
Generates and modifies trip itineraries with Claude tool-calling, grounded in the
knowledge base. Owns the itinerary as data and the generation/replan path. Serves
belief #1.5 (*Vesper adapts to the planner*) and the Planning Philosophy (grounded,
spatially coherent, paced).

## Spans (cross-repo)
- Backend: [`travel-agent/backend/planning_agent/`](../../travel-agent/backend/planning_agent/FEATURE.md) (21, custom tool_use loop) + the generation wiring in `concierge/tool_handlers/planning/` + itinerary tables in `core/`.
- Frontend: `travel-app/app/(tabs)/trips/[tripId]/plan`, `components/trip-plan/*` (35), itinerary edit hooks (`useAddBlock`/`useMoveBlock`/`useApplyReschedule`).
- Tables of record: `itineraries`, `itinerary_days`, `itinerary_blocks`, `itinerary_edit_log`, `plan_state`.

## Public interface (what other systems may call / read)
- **Entry points:** `agent.py::run_planning_agent()` / `arun_planning_agent()` (generate | replan) → structured `PlanningOutput`. Invoked by Concierge via the `generate_plan` tool (`tool_handlers/planning/_plan.py`).
- **Reads (FE → BE):** `GET /api/trips/{id}/...` plan/itinerary reads; the Folio spine is the composed read.
- **Consumes:** Memory & Preference (narrative profiles for fan-out search), Places (live hours), venue/experience corpora (Qdrant).
- **Never:** other systems must not write itinerary blocks directly — mutations go through the Change Studio / edit-commit gateway (see [proposals-change-studio](proposals-change-studio.md)).

The final two statements above are target boundaries, not current proof. The
accepted redesign replaces Folio as the target composed read with Trip Shape /
Plan State + Details/History projections and replaces Change Studio-specific
mutation with one typed itinerary-operation gateway. Existing direct, agent,
pin, proposal, and replan paths remain migration adapters until contract tests
prove convergence.

## Owns (source of truth)
The itinerary structure (days/blocks) and edit log. **Generation** produces it;
**Change Studio** is the controlled mutation path over it.

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
- Serves journey: 05 (the plan that gets proposed against and mutated).
- DoD state: planning eval scenarios ✅ (~27 configs) · feasibility unit tests ✅ · **on-device "generate a plan" walk ❌ · mock-walk ❌**.
- Concierge planning + the agent both run on **Sonnet**.

## Canonical docs
- why → `product/Planning Philosophy.md` · how → `architecture/Planning Agent Problem Definition.md` · what(be) → `backend/planning_agent/FEATURE.md` · what(fe) → `page-specs/itinerary-editing.md` · `trip-plan.md`.
- Tests: `tests/planning_agent/*`, eval `configs/planning/*`.

## Cross-cutting constraints
- **Graph legibility**: context signals injected into `trip_context` (planning_brief, loved_places, returning_traveler, upcoming_events, weather_forecast) shape the plan silently — they must never be echoed back to the user as labels. See [graph-legibility-doctrine.md](graph-legibility-doctrine.md).

## Open risks / known gaps
- Undated Trip Shape, parallel-plan topology, per-traveler delegation, typed
  operations, and operation-linked write-back are accepted target contracts but
  not current tables/read paths.
- The dual read-model collapse (06-20) retired legacy `useItinerary` → plan-state adapter; confirm no surface still reads the old model (feeds journey 06 coherence).
- Replan/edit-inference wiring lives in `concierge/tool_handlers/planning/_plan.py`, **not** in this package — the seam between "agent decides to replan" and "planner replans" is the likely break point.
