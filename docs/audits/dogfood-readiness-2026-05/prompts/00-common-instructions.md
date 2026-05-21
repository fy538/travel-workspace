# Common Cursor Audit Instructions

Paste this section at the top of any custom audit prompt, or use the area-specific prompts in this folder directly.

```text
You are a Cursor Cloud agent auditing Travel Workspace for dogfood readiness.

Workspace root:
/Users/feihuyan/Documents/Claude/Travel Workspace

Repos:
- Travel Agent: backend FastAPI/Postgres/Qdrant/agents
- Travel App: Expo React Native/TypeScript frontend
- Workspace repo: shared docs, OpenAPI snapshot, scripts, reliability tooling

Read first:
- AGENTS.md
- CLAUDE.md
- Travel Agent/AGENTS.md
- Travel App/CLAUDE.md
- docs/reliability/Golden Paths.md
- docs/reliability/Agent Reliability Playbook.md
- Travel Agent/docs/product/Product Thesis.md
- Travel Agent/docs/operations/Repo Status.md
- Travel App/docs/Domain Status.md
- Travel App/docs/Mock vs Real Parity.md

Rules:
- Audit only. Do not make product-code changes.
- You may create or update only your assigned audit report under docs/audits/dogfood-readiness-2026-05/areas/.
- Do not call live LLMs, production services, paid APIs, or external provider APIs.
- Do not read .env files or secrets.
- Prefer rg over grep.
- Run cheap deterministic checks only when relevant:
  - make doctor
  - make contract-check
  - make api-coverage-check
  - make mock-real-parity
  - make golden-path-qa
  - targeted pytest or jest tests
- If tests are too broad or dependencies are missing, say so and continue with static analysis.
- Do not inflate severity. P0 requires a concrete dogfood-blocking path.

Finding format:
- Severity: P0, P1, P2, P3
- Status: Confirmed / Suspected / Needs repro
- User impact
- File and line references
- Repro or deterministic test idea
- Suggested fix direction
- Related bug class
- Confidence

Write your final report using:
docs/audits/dogfood-readiness-2026-05/FINDINGS-TEMPLATE.md
```

