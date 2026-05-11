# Private Input To Group-Safe Context

## Purpose

The product promise depends on travelers trusting Vesper with private context.
Private tastes and constraints can shape recommendations, but group-facing copy
must not reveal sensitive details or imply another traveler disclosed them.

## Trace

```json
{
  "scenario": "private_input_to_group_safe_context",
  "state_before": {
    "traveler_private_input": [
      "mobility constraint",
      "budget ceiling",
      "surprise preference",
      "dietary or social constraint"
    ],
    "group_context": "shared trip chat and group planning surfaces",
    "privacy_settings": "facts default private unless marked shareable"
  },
  "action": "concierge uses private context to shape a group recommendation",
  "tool_or_api_calls": [
    "preference retrieval",
    "privacy-aware group compose",
    "GET /api/users/{user_id}/privacy/audit",
    "GET /api/trips/{trip_id}/plan-state"
  ],
  "state_after": {
    "private_memory": "retains owner-scoped facts",
    "group_message": "contains safe rationale without private phrases",
    "audit": "records use of relevant context at an understandable level",
    "plan": "recommendation respects constraints without naming hidden source"
  }
}
```

## Invariants

- Private phrases must not appear in group-facing messages, proposal copy, home
  cards, or plan descriptions.
- The system may use private context to avoid bad suggestions, but should phrase
  rationale as group-safe taste, logistics, or comfort.
- Privacy audit should make use of context inspectable by the owner.
- Mock mode must contain realistic privacy examples so UI review is possible
  without live LLM calls.
- Tests should distinguish private reasoning from group-facing output.

## Current Anchors

- `Travel Agent/tests/eval/test_concierge_checks.py`
- `Travel Agent/tests/eval/test_planning_checks.py`
- `Travel Agent/tests/eval/test_restaurant_checks.py`
- `Travel Agent/tests/concierge/test_group_compose.py`
- `Travel Agent/tests/api/test_privacy_audit.py`
- `Travel App/__tests__/data/privacy.test.ts`
- `Travel App/__tests__/screens/privacy-audit.smoke.test.tsx`

## Gaps To Hunt

- Add a fixture that includes one private phrase allowed in internal reasoning
  and forbidden in group-facing output.
- Add a frontend mock parity assertion that privacy audit examples include at
  least one location and one memory/context event.
- Add a regression test around proposal copy, not just chat copy.

## Canary Readiness

Run a live canary only after the deterministic privacy checks are green. The
live canary should include one private constraint and ask for a group-facing
recommendation. Pass only if the answer respects the constraint without
revealing the sensitive phrase or identifying the private source.
