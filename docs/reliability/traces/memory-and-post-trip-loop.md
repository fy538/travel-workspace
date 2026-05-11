# Memory And Post-Trip Loop

## Purpose

The product should compound across trips without making memory feel invisible
or irreversible. Captured moments, observations, personal memory, and post-trip
readouts need clear ownership and inspectability.

## Trace

```json
{
  "scenario": "memory_and_post_trip_loop",
  "state_before": {
    "trip": "during-trip or recently completed trip",
    "observations": "moments, choices, or conversation-derived facts",
    "memory": "existing personal memory and user facts"
  },
  "action": "user captures a moment or finishes a trip",
  "tool_or_api_calls": [
    "POST /api/trips/{trip_id}/home_cards/capture_moment",
    "GET /api/users/{user_id}/memory",
    "GET /api/trips/{trip_id}/debrief",
    "post_trip_character_read task"
  ],
  "state_after": {
    "observations": "new moment has source metadata",
    "memory": "personal memory is inspectable",
    "debrief": "post-trip summary is generated from allowed context",
    "control": "user can understand or retire remembered facts"
  }
}
```

## Invariants

- Captured moments must include source metadata and trip association.
- Personal memory screens must render offline with realistic mock data.
- Post-trip outputs should avoid presenting speculation as fact.
- Retired facts should not reappear as active memory.
- Memory updates should preserve privacy levels and owner scope.

## Current Anchors

- `Travel Agent/tests/tasks/test_post_trip_character_read.py`
- `Travel Agent/tests/api/test_trips_debrief.py`
- `Travel Agent/tests/api/test_home.py`
- `Travel App/__tests__/data/memory.test.ts`
- `Travel App/__tests__/screens/personal-memory.smoke.test.tsx`
- `Travel App/__tests__/offline/goldenPath.test.ts`

## Gaps To Hunt

- Add a deterministic test that captured Home moments become observations with
  expected source fields.
- Add a regression test for retiring a fact before a post-trip readout.
- Add mock-real parity around memory markdown sections and fact metadata.

## Canary Readiness

Use a tiny live canary only for post-trip readout tone and usefulness. Keep the
input fixture short, deterministic, and free of real user secrets.
