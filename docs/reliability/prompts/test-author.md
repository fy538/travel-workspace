# Test Author Prompt

```text
You are adding deterministic reliability coverage for Travel Workspace.

Workspace:
- Parent: /Users/feihuyan/Documents/Claude/Travel Workspace
- Backend: Travel Agent
- Frontend: Travel App

Constraints:
- Do not call live LLMs or external APIs.
- Do not require Postgres unless the task explicitly asks for DB-backed tests.
- Prefer backend fakes, frontend mock mode, generated types, and existing test
  helpers.
- Add the smallest useful test for one invariant.
- Do not rewrite product behavior unless the test exposes a real bug.

Target:
- Feature or trace: [FEATURE_OR_TRACE]
- Invariant to protect: [INVARIANT]
- Preferred repo or layer: [BACKEND_FRONTEND_OR_BOTH]

Steps:
1. Read AGENTS.md and the relevant child repo CLAUDE.md.
2. Read docs/journeys/README.md, docs/journeys/STATUS.md, and the matching journey file.
3. Inspect existing tests before adding new ones.
4. Add or update one deterministic test.
5. Run the smallest targeted command first.
6. If green, run one workspace command when appropriate:
   - make contract-check
   - make mock-real-parity
   - make golden-path-qa

Return:
- The invariant covered.
- Files changed.
- Commands run and results.
- Any remaining reliability gap.
```
