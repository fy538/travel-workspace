# Dogfood Readiness Audit — 2026-05

This folder is the collection point for area-by-area Cursor Cloud audits before dogfooding.

Use the prompts in `prompts/` to launch one agent per surface. Each agent should write exactly one report into `areas/` using `FINDINGS-TEMPLATE.md`.

## How To Run

1. Open a new Cursor Cloud agent from the workspace root:
   `/Users/feihuyan/Documents/Claude/Travel Workspace`
2. Paste one prompt from `prompts/`.
3. Let the agent inspect code and docs, run only cheap deterministic checks, and write its findings file.
4. After all area reports land, run `prompts/99-synthesis.md` in a final agent to dedupe and create the master punch list.

## Rules

- Audit only unless the prompt explicitly asks for tests.
- Do not call live LLMs, paid APIs, production services, or external provider APIs.
- Prefer static tracing, deterministic tests, generated contract checks, and mock mode.
- Findings need file and line references, concrete impact, and a repro or test idea.
- P0 means a concrete dogfood-blocking path, not just a scary smell.

## Output Paths

- Area findings: `docs/audits/dogfood-readiness-2026-05/areas/NN-area-name.md`
- Final synthesis: `docs/audits/dogfood-readiness-2026-05/MASTER-PUNCH-LIST.md`

## Prompt Index

Launch these in parallel where possible:

- `prompts/01-privacy-group-safe-synthesis.md`
- `prompts/02-invite-join-auth-deeplinks.md`
- `prompts/03-trip-creation-destination-identity.md`
- `prompts/04-concierge-chat-sse-agent-loop.md`
- `prompts/05-proposals-plan-state-revert.md`
- `prompts/06-home-plan-map-coherence.md`
- `prompts/07-memory-trip-story-photos.md`
- `prompts/08-notifications-proactive-push-digest.md`
- `prompts/09-frontend-data-mock-real-contract.md`
- `prompts/10-backend-auth-security-ratelimit.md`
- `prompts/11-async-workers-scheduled-tasks.md`
- `prompts/12-content-graph-search-qdrant.md`
- `prompts/13-booking-expenses-transport.md`
- `prompts/14-release-testflight-deploy-mobile.md`
- `prompts/15-performance-observability-cost.md`

Run this after the area reports land:

- `prompts/99-synthesis.md`
