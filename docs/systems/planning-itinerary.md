# Planning / Itinerary — System Charter

> Surface: Trips
> Maturity (for MVP): MVP-required
> Status: current path wired; itinerary-first target behind governed rollout; on-device journey unvalidated
> Last updated: 2026-07-16

## Purpose
Owns the living itinerary: the primary single-trip surface and canonical shared
trip artifact before, during, and after travel. It generates and revises the trip
with grounded place intelligence, personal and group context, feasibility, typed
authority, and durable history. It serves belief #1.5 (*Vesper adapts to the
planner*), #6 (*the itinerary is operational truth*), and #9.5 (*one change must
not create five new planning problems*).

## Spans (cross-repo)
- Backend: [`travel-agent/backend/planning_agent/`](../../travel-agent/backend/planning_agent/FEATURE.md) (21, custom tool_use loop) + the generation wiring in `concierge/tool_handlers/planning/` + itinerary tables in `core/`.
- Frontend: `travel-app/app/(tabs)/trips/[tripId]/plan`, `components/trip-plan/*` (35), itinerary edit hooks (`useAddBlock`/`useMoveBlock`/`useApplyReschedule`).
- Tables of record: `itineraries`, `itinerary_days`, `itinerary_blocks`, `itinerary_edit_log`, `plan_state`.

## Public interface (what other systems may call / read)
- **Entry points:** `agent.py::run_planning_agent()` / `arun_planning_agent()` (generate | replan) → structured `PlanningOutput`. Invoked by Concierge via the `generate_plan` tool (`tool_handlers/planning/_plan.py`).
- **Reads (FE → BE):** canonical Trip Shape / Plan State, lifecycle, details, and
  operation/history projections. `/folio` is a measured compatibility adapter,
  not the target composed read.
- **Consumes:** Memory & Preference (narrative profiles for fan-out search), Places (live hours), venue/experience corpora (Qdrant).
- **Mutations:** every Add, Move, Reorder, Replace, Remove, attendance change,
  Optimize, and replan resolves through one typed itinerary-operation policy and
  commit path. Current direct, proposal, pin, agent, and replan paths are adapters
  until retirement is proven.
- **Never:** another surface may become a second itinerary mutation authority;
  chat, voice, notification, booking, and Discover actions must open or invoke
  the canonical operation.

These are target boundaries under governed rollout, not a claim that every
legacy client path has retired. Compatibility remains until selected-trip,
first-paint, degradation, old-client, and on-device evidence passes.

## Owns (source of truth)
Trip Shape, dated itinerary structure, lifecycle-aware plan state, typed
operations, stable subject lineage, and operation history. Generation produces a
first draft; the itinerary-operation gateway is the controlled mutation path.
Change Studio remains one review surface over that authority, not the authority
itself.

## Invariants (must always be true)
- **Grounded:** never recommends a venue it can't retrieve from the knowledge base (no hallucinated places).
- **Feasibility-checked:** the LIVE feasibility layer runs after YAML emit, before persist (overlap / travel-time / over-packed / meal-gap / closed-venue), fully **fail-open** — repair shifts times deterministically; bounded LLM repair is gated (`FEASIBILITY_LLM_REPAIR_ENABLED`).
- **Spatial + pacing discipline:** spatially coherent days, ~70% capacity (no over-packing).
- **Budget/group binding:** `trip.budget_band` + group context bind into planning context; budget reasoning surfaced in `ReasoningTrace.budget_analysis`.
- **Provider parity:** eval (`EvalToolProvider`, YAML) and prod (`DatabaseToolProvider`) implement the same `ToolProvider` ABC — generation behaves identically offline.
- **One shared truth:** List, Map, Details, Chat attachments, notifications,
  booking continuations, and History project the same lifecycle, operation, and
  itinerary identities.
- **Coherent revision:** every material change preserves unaffected intent,
  revalidates affected timing/logistics/constraints, distinguishes plan truth
  from provider truth, and returns explicit unresolved consequences.
- **Relational fit:** personal, group, and companion context must shape the plan
  without leaking private inputs into shared rationale.
- **Recoverability:** material operations carry before/after, attribution,
  rationale when useful, provider outcome, stable lineage, and the currently
  valid Undo/Withdraw/Revert or continuation.

## Failure modes
- Feasibility failure → fail-open (plan still returned; repair best-effort).
- Search returns nothing → the agent narrows/re-queries via fan-out; never fabricates to fill.

## Maturity & validation
- Serves journeys: 01 (Vesper-shaped first draft), 05 (group proposal/direct
  mutation), 06 (List/Map/History coherence), 08 (live adaptation), and 15
  (destructive/reversible actions).
- DoD state: planning eval scenarios ✅ (~27 configs) · feasibility unit tests ✅ · **on-device "generate a plan" walk ❌ · mock-walk ❌**.
- Concierge planning + the agent both run on **Sonnet**.

## Canonical docs
- why → `product/Planning Philosophy.md` · how → `architecture/Planning Agent Problem Definition.md` · what(be) → `backend/planning_agent/FEATURE.md` · what(fe) → `page-specs/itinerary-editing.md` · `trip-plan.md`.
- Tests: `tests/planning_agent/*`, eval `configs/planning/*`.

## Cross-cutting constraints
- **Graph legibility**: context signals injected into `trip_context` (planning_brief, loved_places, returning_traveler, upcoming_events, weather_forecast) shape the plan silently — they must never be echoed back to the user as labels. See [graph-legibility-doctrine.md](graph-legibility-doctrine.md).

## Open risks / known gaps
- Governed target rollout still needs selected-trip, device, first-paint,
  degradation, and compatibility evidence before legacy paths can retire.
- The dual read-model collapse (06-20) retired legacy `useItinerary` → plan-state adapter; confirm no surface still reads the old model (feeds journey 06 coherence).
- Replan/edit-inference wiring lives in `concierge/tool_handlers/planning/_plan.py`, **not** in this package — the seam between "agent decides to replan" and "planner replans" is the likely break point.
- Product-quality proof remains experiential: a real traveler must be able to say
  Vesper understood us, improved the itinerary, and repaired a live change at the
  right moment without creating new coordination work.
