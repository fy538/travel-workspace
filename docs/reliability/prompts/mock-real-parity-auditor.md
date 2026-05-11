# Mock-Real Parity Auditor Prompt

```text
You are auditing mock-real parity for Travel Workspace.

Do not call live LLMs or external APIs.
Do not hand-edit generated API types.

Target:
- API/data surface: [SURFACE]
- Backend route/model if known: [ROUTE_OR_MODEL]
- Frontend hook/screen if known: [HOOK_OR_SCREEN]

Checklist:
1. Run make contract-check.
2. Inspect docs/openapi.json and Travel App/utils/api/schema.gen.ts only as
   generated contract artifacts.
3. Verify Travel App/utils/api/interface.ts exposes a single API surface.
4. Compare Travel App/utils/api/http.ts and mock.ts behavior for the target.
5. Verify data hooks use data/ as the screen bridge, not direct screen imports
   from utils/api.
6. Add a mock-real parity test if the mock can drift from real behavior.

Good tests:
- Assert shape and fallback behavior.
- Assert ids/status/enums match generated schema expectations.
- Assert retry/error states do not create impossible mock behavior.

Return:
- Parity status.
- Drift risks.
- Files changed.
- Commands run and results.
```
