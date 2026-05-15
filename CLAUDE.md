# CLAUDE.md — Travel Workspace

This directory is the coordination layer for two related repositories:

| Repo | Path | Stack | Purpose |
|------|------|-------|---------|
| **Travel Agent** | `./Travel Agent/` | Python 3.13 + FastAPI + PostgreSQL + Qdrant | Backend API, all agents, database |
| **Travel App** | `./Travel App/` | React Native + Expo + TypeScript | iOS/Android mobile client |

Read each repo's own `CLAUDE.md` for full context. This file covers the **cross-repo contract** only.

---

## API Contract

The backend exposes a full OpenAPI 3.1 schema at **`GET /openapi.json`** (when running).
The frontend consumes it via generated TypeScript types.

```bash
# Backend base URL (dev)
http://localhost:8000

# OpenAPI schema (live, requires backend running)
http://localhost:8000/openapi.json

# OpenAPI schema (committed snapshot — always available)
./docs/openapi.json
```

The committed snapshot at `docs/openapi.json` is updated by `scripts/sync-types.sh` and
should be committed whenever backend models change.

---

## Sync Types Workflow

**When you change a Pydantic model or add an API endpoint in Travel Agent:**

```bash
# From this workspace directory:
./scripts/sync-types.sh

# What it does:
# 1. Pulls fresh openapi.json from the running backend
# 2. Saves it to docs/openapi.json (commit this)
# 3. Generates TypeScript types in Travel App/utils/api/schema.gen.ts
# 4. Runs tsc --noEmit in Travel App to surface any breakage
```

If the backend isn't running, use the committed snapshot:
```bash
./scripts/sync-types.sh --from-snapshot
```

**When you add a new API endpoint**, the workflow is:
1. Add the FastAPI route + Pydantic models in Travel Agent
2. Run `./scripts/sync-types.sh`
3. Use the generated types in Travel App — import from `utils/api/schema.gen.ts`
4. Commit both `docs/openapi.json` and the updated app code together

**Drift detection** — `make api-coverage-check` (or `python3
scripts/api-coverage-check.py`) verifies every URL fetched by
`Travel App/utils/api/http.ts` exists in `docs/openapi.json` at the
declared method. Fails with exit code 1 on drift, which means either
(a) the frontend will 404 at runtime, or (b) the openapi snapshot is
stale. Run after adding a new endpoint or before opening a PR that
touches the API surface.

---

## MCP Tools Available (when Travel Agent backend is running)

The `travel-agent` MCP server exposes development tools for querying live data.
It's configured in `Travel Agent/.mcp.json` and registered for Claude Code sessions
opened in the Travel Agent directory.

Key tools: `search_venues`, `get_trip`, `get_traveler`, `get_booking_offers`,
`list_trips`, `run_read_query`, `get_openapi_schema` (returns live API shape).

---

## Cross-Repo Patterns

### Adding a new feature end-to-end

1. **Start in Travel Agent**: define the Pydantic model + route + tests
2. **Run sync-types**: `./scripts/sync-types.sh`
3. **Switch to Travel App**: generated types are ready, implement the UI
4. **Never** hand-write TypeScript types that duplicate Pydantic models — generate them

### Type naming conventions

| Backend (Python) | Frontend (TypeScript) |
|------------------|-----------------------|
| `Trip` (Pydantic) | `components['schemas']['Trip']` (from schema.gen.ts) |
| `BookingSession` | `components['schemas']['BookingSession']` |
| `PersonalMemory` | `components['schemas']['PersonalMemory']` |

The `types/` directory in Travel App contains hand-written types for UI concepts
(display formatting, component props) that have no direct backend equivalent.
Backend-mirroring types should be generated, not hand-written.

---

## Quick Reference

```bash
# Start backend
cd "Travel Agent" && docker compose up -d && PYTHONPATH=. uvicorn backend.api.main:app --reload

# Start frontend
cd "Travel App" && npx expo start --ios

# Sync API types (requires backend running)
./scripts/sync-types.sh

# Sync from committed snapshot (no backend needed)
./scripts/sync-types.sh --from-snapshot

# Run backend tests
cd "Travel Agent" && PYTHONPATH=. pytest tests/ -q -m "not requires_postgres and not requires_api_keys"

# Run frontend type check
cd "Travel App" && npx tsc --noEmit
```
