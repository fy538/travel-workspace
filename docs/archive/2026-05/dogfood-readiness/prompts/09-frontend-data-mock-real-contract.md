# Prompt 09 — Frontend Data Layer, Mock/Real Parity, And Contract Drift

```text
You are a Cursor Cloud agent auditing Travel Workspace for dogfood readiness.

Use the common rules in:
docs/audits/dogfood-readiness-2026-05/prompts/00-common-instructions.md

Area:
Frontend data hooks, generated API types, mock/real parity, API boundary rules.

Output:
docs/audits/dogfood-readiness-2026-05/areas/09-frontend-data-mock-real-contract.md

Product promise:
Mock mode accelerates development without lying about real-mode payloads, persistence, error states, or navigation flows.

Inspect:
- Travel App data hooks, utils/api/http.ts, utils/api/mock.ts, interface.ts, schema.gen.ts usage.
- Screens importing API directly instead of `data/`.
- Handwritten backend-mirroring types.
- Mock fixtures for sparse/null/error/latency behavior.
- Workspace OpenAPI snapshot and api coverage tooling.

Start with:
- Travel App/docs/Mock vs Real Parity.md
- Travel App/docs/Domain Status.md
- Travel App/docs/Components.md
- Travel App/CLAUDE.md
- docs/reliability/prompts/mock-real-parity-auditor.md

Audit questions:
1. Do any screens bypass the `data/` bridge and call `utils/api` directly?
2. Are backend-shaped types hand-maintained instead of generated or derived?
3. Do mock responses include fields real backend never sends, or omit required real fields?
4. Do mocks hide real error states, auth redirects, latency, nulls, or empty lists?
5. Are all frontend HTTP call sites represented in OpenAPI?
6. Does schema.gen.ts match workspace `docs/openapi.json`?
7. Are release builds guarded against mock/skip-auth mode?

Run:
- make contract-check
- make api-coverage-check
- make mock-real-parity
- targeted TypeScript/Jest tests if needed

Deliver:
List drift by call site and user impact. For recurring classes, propose one lint/test gate.
```

