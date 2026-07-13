# Itinerary, Map, Details, Chat, And Changes Coherence

## Purpose

The app should feel like one living trip, not disconnected tabs. Itinerary List,
Map, Trip Details, Chat attachments, and Changes can emphasize different views,
but they must reference compatible trip, block, proposal, provider, and place
state. The current Folio/Home read remains a compatibility projection during
migration, not a target trip destination.

## Trace

```json
{
  "scenario": "home_plan_map_coherence",
  "state_before": {
    "trip": "shared trip with itinerary blocks, proposals, and maybe stays",
    "itinerary": "Plan State current truth and one contextual attention item",
    "map": "Trip Map v2 spatial read model"
  },
  "action": "user opens Itinerary, Map, Details, Chat context, and Changes after a plan change or proposal",
  "tool_or_api_calls": [
    "GET /api/trips/{trip_id}/plan-state",
    "GET /api/trips/{trip_id}/map-state",
    "GET /api/trips/{trip_id}/details-state",
    "GET /api/trips/{trip_id}/itinerary/history",
    "GET /api/trips/{trip_id}/folio (compatibility during migration)"
  ],
  "state_after": {
    "itinerary": "days, blocks, open decisions, and recent changes render",
    "map": "placed blocks render as pins/routes; unplaced blocks do not crash",
    "details": "trip-wide summaries deep-link to the same anchors/provider truth",
    "history": "operation status and recovery match the landed itinerary",
    "identity": "shared ids let users connect the same thing across surfaces"
  }
}
```

## Invariants

- List blocks, Map pins, Details summaries, Chat attachments, Changes, and the
  transitional Folio adapter must agree on trip and canonical object ids.
- A block shown as affected by an open proposal in Plan should not disappear
  from Map unless it was actually removed or unplaced.
- Dismissing ambient Home cards must not hide Tier 1 critical state.
- Empty itinerary, unplaced item, and missing accommodation cases must render
  safe fallback states.
- Generated app types must match the backend snapshot before this trace is
  considered valid.

## Current Anchors

- `Travel Agent/tests/api/test_home.py`
- `Travel Agent/tests/api/test_home_group_invites.py`
- `Travel Agent/tests/api/test_plan_state.py`
- `Travel Agent/tests/api/test_trips_api.py`
- `Travel App/__tests__/data/planState.test.ts`
- `Travel App/__tests__/utils/tripMapStateParity.test.ts`
- `Travel App/__tests__/screens/plan.smoke.test.tsx`
- `Travel App/__tests__/screens/map.smoke.test.tsx`

## Gaps To Hunt

- Add one cross-fixture test that compares Plan block ids to Map item ids.
- Add a Home-to-Plan route test for pending-decision cards.
- Add a test for accommodation state appearing in Plan cross-trip shell and Map
  origin context when both are present.

## Canary Readiness

This is mostly deterministic. A live canary is useful only after an LLM-driven
proposal or recommendation changes the trip state and the user opens all three
surfaces.
