# Atlas — Photo Backfill

Onboarding and activation feature that turns a user's existing photo
library into a private, reviewable set of travel artifacts (Trip Stories,
Weekend Cards, Day Postcards, Place Memories, Pattern Cards). Accepted
artifacts feed derived signals into Travel DNA with per-source provenance
so deleting an artifact revokes its contributions cleanly.

Quick orienting doc — for the decisions, read the brief and the plan.

## Where the work lives

| Concern | Location |
|---------|----------|
| Product brief | `Travel App/docs/Brief - Atlas Photo Backfill.md` |
| V0 engineering plan | `docs/Plan — Atlas V0 Engineering.md` (workspace) |
| Backend subsystem | `Travel Agent/backend/atlas/` (+ `FEATURE.md`) |
| Backend routes | `Travel Agent/backend/api/routes/atlas.py` (10 endpoints) |
| Backend tables | `Travel Agent/backend/core/db/_tables/atlas.py` |
| Backend storage | `Travel Agent/backend/core/db/atlas.py` |
| Frontend tab | `Travel App/app/(tabs)/atlas/` |
| Frontend scan flow | `Travel App/app/atlas/scan.tsx` |
| Frontend components | `Travel App/components/atlas/` |
| Frontend data hooks | `Travel App/data/atlas.ts` |
| Frontend types | `Travel App/types/atlas.ts` (re-exports from `schema.gen.ts`) |
| API contract | `docs/openapi.json` (workspace) |

## Run locally — mock mode

Fastest way to see Atlas working end-to-end without any backend running.

```bash
cd "Travel App"
EXPO_PUBLIC_USE_MOCK_API=true npx expo start --ios
```

Then:

- Tap the **Atlas** tab — empty state shows the hero "Let Vesper build your first Atlas."
- Memory Inbox renders two seeded candidates (Tokyo 6-day trip + Williamsburg afternoon).
- Tap the hero → scan onboarding wizard (Promise → Trust → Scan).
- Mock data + mutations live in `Travel App/utils/api/mock.ts` (`_atlasSeedCandidates`, `_atlasCandidates`, `_atlasArtifacts`).

## Run locally — real backend

```bash
# Backend (mock composer — no API key needed)
cd "Travel Agent"
docker compose up -d
PYTHONPATH=. alembic upgrade head
PYTHONPATH=. uvicorn backend.api.main:app --reload

# Backend (REAL LLM composer — requires ANTHROPIC_API_KEY)
ATLAS_LLM_ENABLED=true PYTHONPATH=. uvicorn backend.api.main:app --reload

# Frontend (separate terminal)
cd "Travel App"
EXPO_PUBLIC_USE_MOCK_API=false \
  EXPO_PUBLIC_API_URL=http://localhost:8000 \
  npx expo start --ios
```

The LLM composer enforces the brief's one-line-read gate server-side: if
Claude returns `one_line_read: null` (or anything < 10 chars), the
composer falls back to the deterministic mock copy. Transport failures
also fall back. The route handler always returns a usable artifact.

The 10 Atlas endpoints live under `/api/atlas/*`. Smoke test with curl:

```bash
curl http://localhost:8000/api/atlas/inbox

curl -X POST http://localhost:8000/api/atlas/candidates \
  -H 'Content-Type: application/json' \
  -d '{
    "candidates": [{
      "date_range_start": "2026-03-12",
      "date_range_end": "2026-03-18",
      "place_guess": "Tokyo",
      "place_count": 3,
      "photo_count": 60,
      "sample_photo_ids": ["t1","t2","t3"],
      "confidence": "high",
      "candidate_type": "trip",
      "cluster_reason": "test"
    }]
  }'

# Capture the returned candidate id, then approve it:
curl -X POST http://localhost:8000/api/atlas/candidates/<id>/approve
```

Approve currently runs the deterministic mock composer (`compose_artifact_mock`); the real LLM composer lands separately.

## Tests

```bash
# Backend — offline, no DB or API keys needed
cd "Travel Agent"
PYTHONPATH=. pytest tests/atlas/ -v
# 18 tests covering candidate validation + composer shape

# Backend — full (needs Postgres + Qdrant via docker compose)
PYTHONPATH=. pytest tests/atlas/ -m "" -v

# Frontend — type-check
cd "Travel App"
npx tsc --noEmit
```

## Schema sync workflow

Every time backend Pydantic models change:

```bash
cd "Travel Workspace"      # workspace root
./scripts/sync-types.sh    # regenerates docs/openapi.json + schema.gen.ts
```

`types/atlas.ts` re-exports from `schema.gen.ts` — no hand-written duplicates.

## Status

| Layer | State |
|-------|-------|
| Backend subsystem | ✓ Shipped |
| Backend tables + migration | ✓ Shipped |
| API contract + OpenAPI snapshot | ✓ Shipped |
| Frontend tab + components + hooks | ✓ Shipped |
| Mock API end-to-end | ✓ Shipped |
| Trip `source` column | ✓ Shipped |
| Real LLM composer (with one-line gate + mock fallback) | ✓ Shipped |
| SSE streaming (shell + ready phases) | ✓ Shipped |
| `expo-media-library` photo picker (manual-pick path) | ✓ Shipped |
| True incremental section-by-section SSE | Deferred (V1) |
| Multi-head Alembic merge | ⚠ Blocked on external bug — see note below |
| Full-library auto-scan (V1) | Deferred |
| `JournalingSuggestions` integration (V1) | Deferred |
| Custom Expo Module for burst grouping + `PHPersistentChangeToken` (V1) | Deferred |
| Broader DNA-provenance hardening | Follow-up (see V0 plan §Follow-up) |

## Note: multi-head Alembic warning

`alembic heads` currently shows two heads:

```
a1b2c3d4e5f6           ← uncommitted budget-columns WIP (broken)
a7b4c1d8e5f2 (head)    ← atlas chain + source column
```

The merge cannot be written cleanly because the budget WIP picked a
revision ID (`a1b2c3d4e5f6`) that collides with the already-committed
`a1b2c3d4e5f6_add_delegation_preferences.py`. Alembic emits
`UserWarning: Revision a1b2c3d4e5f6 is present more than once` and any
merge migration referencing that ID resolves to the wrong ancestor.

Fix sequence (whoever owns the budget WIP):

1. Pick a new unique revision ID for `add_budget_columns_to_trips.py`
   (e.g. `d4e1c8b2a9f6`) and update `revision = ...` in that file.
2. Rename the file to match: `<new_id>_add_budget_columns_to_trips.py`.
3. Verify `alembic heads` shows two heads (atlas, budget) with distinct
   IDs.
4. Generate the merge: `PYTHONPATH=. alembic merge -m
   "merge atlas + budget heads" <atlas_head> <budget_head>`.
5. Commit. `alembic heads` should now show a single head.

The Atlas chain works correctly in isolation — `alembic upgrade
a7b4c1d8e5f2` applies cleanly today.
