# Golden-Path Tracer Prompt

```text
You are building or updating an offline trace for a Travel Workspace golden
path.

Do not call live LLMs or external APIs.
Do not modify product code unless explicitly asked after the trace is complete.

Trace target:
- Golden path: [GOLDEN_PATH]
- User story: [USER_STORY]
- Concern: [CONCERN]

Steps:
1. Read docs/journeys/README.md and docs/journeys/STATUS.md.
2. Read the relevant file in docs/reliability/traces/.
3. Inspect backend models/routes, frontend hooks, mock API data, and tests.
4. Write or update the trace with:
   - scenario
   - state_before
   - action
   - tool_or_api_calls
   - state_after
   - invariants
   - current anchors
   - gaps to hunt
5. If a missing invariant is obvious and small, propose the test but do not add
   it unless asked.

Return:
- Updated trace summary.
- Code paths inspected.
- Test anchors.
- Top 3 missing deterministic checks.
```
