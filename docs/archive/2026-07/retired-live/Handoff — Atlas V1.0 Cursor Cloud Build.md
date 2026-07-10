---
doc_type: archive
status: archived
owner: founder / engineering
created: 2026-07-09
archived: 2026-07-09
why_new: Move reviewed completed evidence out of the living documentation tree without deleting its historical record.
---

# Handoff — Atlas V1.0 Cursor Cloud Build

> Archived from the living documentation tree on 2026-07-09 during Phase 5 cleanup.

> **Outcome (as of 2026-07-03):** ✅ Historical — the Atlas V1.0 build described here was completed; retained as a build record, not an active handoff.

**Audience:** Cursor cloud agent. Build target: Atlas V1.0 across the
Travel Agent backend (Python/FastAPI) and Travel App frontend (React
Native/Expo). Estimated 8–12 hours of agent time.

You have no memory of prior conversations. This document plus the repo
itself is everything you need. Read it end-to-end before starting; the
order matters.

---

## 1. Mission brief

Atlas Photo Backfill is a feature that turns the user's existing photo
library into reviewable travel-memory artifacts. V0 has shipped: backend
subsystem with 10 endpoints, frontend tab with onboarding flow, manual
photo picker (the brief's "Choose photos myself" Permission Strategy path).

**Your job is V1.0** — the managed-Expo-only expansion that adds:

1. **Full-library auto-scan** (the brief's "Find memories from photos" path,
   replacing V0's manual-pick-only). Foreground scan with progress UI,
   cancelable, Low Power Mode aware.
2. **Real home/work inference** from photo GPS clusters (replaces V0's
   profile-home stub). DBSCAN + temporal weighting.
3. **Candidate dismissal** — backend endpoint + frontend UI so users can
   reject candidates they don't want.
4. **Paginated Memory Inbox** as a dedicated screen (V0 surfaces it as a
   section on the Atlas tab; V1.0 promotes it).
5. **Incremental rescan** via AsyncStorage timestamp — re-opening the app
   processes only assets newer than `last_scanned_at`. *(V1.1 will
   replace this with `PHPersistentChangeToken` via a custom Expo Module
   — but V1.1 is not your job.)*
6. **Scan history tracking** — backend table + endpoint for "when did
   this user last scan?"

**Done means:** every acceptance criterion in §11 passes, all tests are
green, `npx tsc --noEmit` is 0 errors, `ruff check` is clean, and one
commit per repo lands on the working branch with a clear message.

---

## 2. Required reading (read in this order)

Spend 10–15 minutes on these before writing any code. They have the
decisions you'll need.

1. `Travel App/docs/Brief - Atlas Photo Backfill.md` — the product brief.
   You must honor the brief's voice, copy doctrine, and Permission
   Strategy framing.
2. `docs/Plan — Atlas V0 Engineering.md` — what V0 already shipped.
   Section "Backend: data model and endpoints" and "Frontend: screens,
   components, hooks" tell you what exists and the conventions used.
3. `docs/Plan — Atlas V1 Engineering.md` — your reference plan.
   §V1.0 section is your primary scope; §V1.1 is explicitly out of scope.
4. `docs/Atlas — README.md` — orientation. Has the run-locally recipes.
5. `Travel Agent/CLAUDE.md` — backend conventions. CRITICAL:
   SQLAlchemy Core only (no ORM), `call_llm()` from `core/llm.py` never
   raw SDK, tables in `_tables/`, prompts in `prompts.py` files.
6. `Travel App/CLAUDE.md` — frontend conventions. CRITICAL:
   data hooks are the sole bridge to API, never import `utils/api`
   directly from screens, generated types live in `schema.gen.ts`.
7. `Travel App/.claude/rules/api-types.md` — the two-tier type system.
8. `Travel Agent/.claude/rules/patch-routes.md` — use `model_fields_set`
   for PATCH, never `exclude_none`.

If anything in this document conflicts with the linked sources, **the
linked sources win.** This doc is a handoff, not a re-derivation.

---

## 3. Working environment

### Repo layout

```
/Users/feihuyan/Documents/Claude/Travel Workspace/    ← workspace root
  Travel Agent/                                       ← backend repo
  Travel App/                                         ← frontend repo
  docs/                                               ← cross-repo docs
  scripts/sync-types.sh                               ← OpenAPI sync
```

Each of the three (workspace, Travel Agent, Travel App) is a separate
git repo on its own branch. Check the branch you're on before committing.

### Commands you'll use

```bash
# Backend tests (offline only — no DB needed)
cd "Travel Agent"
PYTHONPATH=. pytest tests/atlas/ -v
PYTHONPATH=. pytest tests/ -q -m "not requires_postgres and not requires_api_keys"

# Backend lint
ruff format --check backend/atlas/ backend/api/routes/atlas.py backend/core/db/_tables/atlas.py backend/core/db/atlas.py tests/atlas/
ruff check backend/atlas/ backend/api/routes/atlas.py backend/core/db/_tables/atlas.py backend/core/db/atlas.py tests/atlas/

# Alembic head check
PYTHONPATH=. alembic heads

# OpenAPI + TypeScript types sync
cd "/Users/feihuyan/Documents/Claude/Travel Workspace"
./scripts/sync-types.sh

# Frontend type-check
cd "Travel App"
npx tsc --noEmit

# Frontend lint (Expo's lint runs ESLint with the project config)
npx expo lint

# Run a single Jest test file
npx jest __tests__/utils/atlasCluster.test.ts
```

### Conventions you MUST follow

- **Python:** snake_case, type hints on every signature, `from __future__ import annotations`, Pydantic BaseModel for contracts, `call_llm()` from `backend/core/llm.py` (never raw Anthropic SDK), `get_connection()` from `backend/core/db/engine.py` for DB.
- **TypeScript:** strict mode, no `any`, relative imports (no path aliases), DM Sans for UI / Newsreader for editorial copy, no purple (purple = AI/Vesper only).
- **Markers on backend tests:** `@pytest.mark.requires_postgres` for DB-touching tests; offline tests need no marker.

---

## 4. What V0 already shipped (don't redo these)

Read carefully. These exist. Don't recreate them.

### Backend
- `backend/atlas/__init__.py`
- `backend/atlas/FEATURE.md` — subsystem README
- `backend/atlas/models.py` — Pydantic contracts (AtlasCandidate, AtlasArtifact, DerivedSignal, etc.)
- `backend/atlas/clustering.py` — server-side candidate validation
- `backend/atlas/composer.py` — `compose_artifact_mock`, `compose_artifact_llm`, `compose_artifact` dispatcher
- `backend/atlas/prompts.py` — LLM system + user prompts
- `backend/api/routes/atlas.py` — 10 endpoints (POST candidates, approve, GET/PATCH/DELETE artifact, SSE stream, signals, inbox, photo upload)
- `backend/core/db/_tables/atlas.py` — three tables: `atlas_candidates`, `atlas_artifacts`, `atlas_derived_signals`
- `backend/core/db/atlas.py` — storage layer (CRUD + revoke helper)
- `alembic/versions/b3d5f7a9c1e2_atlas_v0_foundation.py` — atlas tables migration
- `alembic/versions/a7b4c1d8e5f2_add_source_to_trips.py` — trips.source column
- `tests/atlas/test_atlas_clustering.py`, `test_atlas_composer.py`, `test_atlas_composer_llm.py`

### Frontend
- `app/(tabs)/atlas/_layout.tsx`, `app/(tabs)/atlas/index.tsx` — tab + landing
- `app/atlas/scan.tsx` — 3-screen onboarding wizard (Promise → Trust → Scan)
- `components/atlas/HeroCard.tsx`, `CandidateCard.tsx`, `ConfidenceLabel.tsx`, `ProvenanceRibbon.tsx`, `ArtifactStateChip.tsx`, `AuditBridgeRow.tsx`
- `hooks/useAtlasPhotoPicker.ts` — limited-access picker; `loadSelectedPhotos()` for V0 manual-pick
- `utils/atlasCluster.ts` — client-side clustering (DBSCAN-ish on selected photos)
- `data/atlas.ts` — `useAtlasInbox`, `useAtlasArtifact`, `useAtlasCandidate`, `useArtifactSignals`, `useAtlasArtifacts`, `useToggleSignalState`, `useDeleteArtifact`, `useApproveCandidate`, `useSubmitCandidates`
- `types/atlas.ts` — re-exports from `schema.gen.ts`
- `utils/api/interface.ts`, `http.ts`, `mock.ts` — 9 Atlas methods on each
- `utils/api/schema.gen.ts` — generated Atlas types

### Workspace
- `docs/openapi.json` — committed OpenAPI snapshot with Atlas endpoints
- `docs/Atlas — README.md` — orientation
- `docs/Plan — Atlas V0 Engineering.md`, `docs/Plan — Atlas V1 Engineering.md`

---

## 5. What V1.0 adds (the work)

**Backend (~25% of total effort):**
- New table `atlas_scan_history` (one row per user)
- Extend `atlas_candidates.status` CHECK constraint to include `'dismissed'`
- New endpoints: `DELETE /api/atlas/candidates/{id}` (dismiss), `GET /api/atlas/scan-history`, paginate existing `GET /api/atlas/inbox`
- New Pydantic models: `AtlasScanHistory`, `AtlasInboxResponse` updated with pagination cursor
- New storage helpers
- Backend tests

**Frontend utilities (~25% of effort):**
- New `utils/atlasHomeWorkInference.ts` — pure function, DBSCAN + temporal weighting
- New `utils/atlasIncrementalScan.ts` — AsyncStorage-based last-scanned tracking
- Modified `utils/atlasCluster.ts` — accept `minClusterSize` as parameter
- Tests for each (Jest + fixture libraries — see §10)

**Frontend hooks (~15% of effort):**
- New `hooks/useAtlasFullScan.ts` — paginated `getAssetsAsync` with progress + cancel + Low Power Mode handling
- Modified `hooks/useAtlasPhotoPicker.ts` — add `loadAllPhotos()` alongside `loadSelectedPhotos()`
- Modified `data/atlas.ts` — add `useDismissCandidate`, `useScanHistory`, paginated `useAtlasInbox`

**Frontend screens (~25% of effort):**
- New `app/atlas/inbox.tsx` — dedicated Memory Inbox screen
- New `components/atlas/ScanProgressCard.tsx` — foreground scan UI
- New `components/atlas/InboxItem.tsx` — one inbox row with dismiss
- Modified `app/atlas/scan.tsx` — "Find memories from photos" button triggers full scan
- Modified `app/(tabs)/atlas/index.tsx` — "View all" link when inbox has > 3 pending

**API client glue (~10% of effort):**
- `utils/api/interface.ts` — new method sigs
- `utils/api/http.ts` — real implementations
- `utils/api/mock.ts` — mocks + seed state additions

---

## 6. What V1.0 does NOT include

Touching any of these is scope creep — **stop and do not build**:

- ❌ Custom Expo Module (no Swift, no `modules/` folder, no `ios/` directory work)
- ❌ `PHPersistentChangeToken` (V1.1 only — use AsyncStorage timestamp)
- ❌ Burst grouping via `burstIdentifier` (V1.1)
- ❌ Vision feature-print dedup (V1.1)
- ❌ `JournalingSuggestions` integration (V1.1)
- ❌ `BGAppRefreshTask` / background catch-up (V1.1)
- ❌ Apple Foundation Models (V1.2)
- ❌ True incremental SSE section-by-section streaming (V1.1+)
- ❌ Touching the merge migration for `a1b2c3d4e5f6` (blocked on external bug — documented in README)
- ❌ Cross-trip threading (V2+)
- ❌ Discover ranking influence (V2+)
- ❌ DNA-provenance hardening (separate follow-up sprint)

If you discover any of these as "needed" while implementing, **stop and
leave a `TODO(atlas-v1.1)` comment with a paragraph of context.** Do
not silently build them.

---

## 7. Build order

Do the work in this order. Each phase ends with a verification step. Do
not start a later phase until the verification of the earlier passes.

| Phase | What | Time |
|---|---|---|
| 1 | Backend foundation (migration + models + storage + routes + tests) | 2.5 h |
| 2 | OpenAPI + TypeScript types sync | 0.25 h |
| 3 | Frontend API client glue (interface + http + mock) | 1 h |
| 4 | Frontend utilities (home/work, incremental, cluster modification) + tests | 2 h |
| 5 | Frontend hooks (full scan + photo picker addition + data hooks) | 1.5 h |
| 6 | Frontend screens (inbox + ScanProgressCard + InboxItem + wire-up) | 2 h |
| 7 | Verification sweep + commit | 1 h |

**If you have less than 8 hours of available time:** ship Phase 1–5 and
defer Phase 6 (screens) to a TODO. The screens can be added in a second
session and the backend + utilities + hooks all stand alone.

---

## 8. Phase 1 — Backend foundation

### 8a. Migration

Create `Travel Agent/alembic/versions/c2e9b4a8d1f7_atlas_v1_scan_history.py`:

```python
"""atlas_v1_scan_history: scan history table + dismissed candidate status

Adds per-user scan tracking and extends the candidates status vocabulary
to include 'dismissed' (for the new DELETE endpoint).

Chains off ``a7b4c1d8e5f2`` (V0's add_source_to_trips). The uncommitted
budget-columns branch (``a1b2c3d4e5f6``) has a revision-ID collision
with delegation_preferences — that's blocked on external bug, do not
merge yet.

Revision ID: c2e9b4a8d1f7
Revises: a7b4c1d8e5f2
Create Date: 2026-05-27
"""

from __future__ import annotations

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql as pg

revision: str = "c2e9b4a8d1f7"
down_revision: str | Sequence[str] | None = "a7b4c1d8e5f2"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # 1. New atlas_scan_history table
    op.create_table(
        "atlas_scan_history",
        sa.Column(
            "user_id",
            pg.UUID(as_uuid=True),
            sa.ForeignKey("users.id", ondelete="CASCADE"),
            primary_key=True,
        ),
        sa.Column("last_scanned_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("asset_count_at_last_scan", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("candidates_surfaced_total", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("candidates_approved_total", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("candidates_dismissed_total", sa.Integer(), nullable=False, server_default="0"),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
    )

    # 2. Extend atlas_candidates.status CHECK to include 'dismissed'.
    # Drop + recreate is the safest way with Postgres CHECK constraints.
    op.drop_constraint("ck_atlas_candidates_status_values", "atlas_candidates", type_="check")
    op.create_check_constraint(
        "ck_atlas_candidates_status_values",
        "atlas_candidates",
        "status IN ('pending', 'approved', 'dismissed')",
    )


def downgrade() -> None:
    op.drop_constraint("ck_atlas_candidates_status_values", "atlas_candidates", type_="check")
    op.create_check_constraint(
        "ck_atlas_candidates_status_values",
        "atlas_candidates",
        "status IN ('pending', 'approved')",
    )
    op.drop_table("atlas_scan_history")
```

The V0 migration already allowed `'dismissed'` as a status value (check
`backend/core/db/_tables/atlas.py` — the CHECK constraint already lists
all three). If the constraint already allows `'dismissed'`, drop the
constraint-modification ops from `upgrade()` / `downgrade()` and leave
only the table creation. **Read the existing CHECK constraint first
before writing the migration.**

### 8b. SQLAlchemy table

Add to `Travel Agent/backend/core/db/_tables/atlas.py` — append after
`atlas_derived_signals`:

```python
# ============================================================================
# ATLAS SCAN HISTORY — V1.0 per-user scan tracking
# ============================================================================

atlas_scan_history = Table(
    "atlas_scan_history",
    metadata,
    Column(
        "user_id",
        PG_UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column("last_scanned_at", TZDateTime, nullable=True),
    Column("asset_count_at_last_scan", Integer, nullable=False, server_default="0"),
    Column("candidates_surfaced_total", Integer, nullable=False, server_default="0"),
    Column("candidates_approved_total", Integer, nullable=False, server_default="0"),
    Column("candidates_dismissed_total", Integer, nullable=False, server_default="0"),
    Column("updated_at", TZDateTime, nullable=False, server_default=func.now()),
)
```

Add `"atlas_scan_history"` to the `__all__` list at the top of the file.

### 8c. Pydantic models

Append to `Travel Agent/backend/atlas/models.py`:

```python
# ─── V1.0 — Scan history ────────────────────────────────────────────────────


class AtlasScanHistory(BaseModel):
    """One-row-per-user scan tracking. Updated after every successful scan."""

    user_id: UUID
    last_scanned_at: datetime | None
    asset_count_at_last_scan: int
    candidates_surfaced_total: int
    candidates_approved_total: int
    candidates_dismissed_total: int
    updated_at: datetime


# ─── V1.0 — Paginated inbox ─────────────────────────────────────────────────


class AtlasInboxPage(BaseModel):
    """Paginated inbox response. ``next_cursor`` is null when no more rows."""

    items: list[AtlasInboxItem]
    next_cursor: str | None = None
    total_pending: int  # so the UI can show a "N more to review" tease
```

Keep the existing `AtlasInboxResponse` for backward compatibility — the
old non-paginated endpoint still uses it (don't break V0 mocks).

### 8d. Storage layer

Append to `Travel Agent/backend/core/db/atlas.py`:

```python
from backend.atlas.models import AtlasScanHistory
from backend.core.db.tables import atlas_scan_history

# ─── V1.0 — Scan history CRUD ───────────────────────────────────────────────


def get_scan_history(user_id: UUID) -> AtlasScanHistory:
    """Fetch the scan history row; returns a zero-filled row if none exists."""
    with get_connection() as conn:
        row = (
            conn.execute(
                select(atlas_scan_history).where(atlas_scan_history.c.user_id == user_id)
            )
            .mappings()
            .one_or_none()
        )
        if not row:
            return AtlasScanHistory(
                user_id=user_id,
                last_scanned_at=None,
                asset_count_at_last_scan=0,
                candidates_surfaced_total=0,
                candidates_approved_total=0,
                candidates_dismissed_total=0,
                updated_at=datetime.now().astimezone(),
            )
        return AtlasScanHistory(**dict(row))


def upsert_scan_history(
    user_id: UUID,
    *,
    last_scanned_at: datetime,
    asset_count: int,
    candidates_surfaced: int,
) -> AtlasScanHistory:
    """Upsert + increment counters atomically."""
    from sqlalchemy.dialects.postgresql import insert

    with get_connection() as conn:
        stmt = (
            insert(atlas_scan_history)
            .values(
                user_id=user_id,
                last_scanned_at=last_scanned_at,
                asset_count_at_last_scan=asset_count,
                candidates_surfaced_total=candidates_surfaced,
                updated_at=datetime.now().astimezone(),
            )
            .on_conflict_do_update(
                index_elements=["user_id"],
                set_={
                    "last_scanned_at": last_scanned_at,
                    "asset_count_at_last_scan": asset_count,
                    "candidates_surfaced_total": (
                        atlas_scan_history.c.candidates_surfaced_total + candidates_surfaced
                    ),
                    "updated_at": datetime.now().astimezone(),
                },
            )
            .returning(atlas_scan_history)
        )
        row = conn.execute(stmt).mappings().one()
        conn.commit()
        return AtlasScanHistory(**dict(row))


def dismiss_candidate(candidate_id: UUID, user_id: UUID) -> bool:
    """Soft-dismiss a candidate (status='dismissed'). Returns True if matched.

    Increments ``candidates_dismissed_total`` in scan history.
    """
    from sqlalchemy import update
    with get_connection() as conn:
        result = conn.execute(
            update(atlas_candidates)
            .where(
                atlas_candidates.c.id == candidate_id,
                atlas_candidates.c.user_id == user_id,
                atlas_candidates.c.status == "pending",
            )
            .values(status="dismissed")
        )
        if result.rowcount == 0:
            return False
        # Increment counter (best-effort; only if scan history row exists)
        conn.execute(
            update(atlas_scan_history)
            .where(atlas_scan_history.c.user_id == user_id)
            .values(
                candidates_dismissed_total=atlas_scan_history.c.candidates_dismissed_total + 1,
                updated_at=datetime.now().astimezone(),
            )
        )
        conn.commit()
        return True


def list_pending_candidates_paginated(
    user_id: UUID,
    *,
    limit: int = 20,
    after_id: UUID | None = None,
) -> tuple[list[AtlasCandidate], UUID | None, int]:
    """Returns (items, next_cursor, total_pending_count).

    Cursor pagination by ``created_at DESC, id`` — stable + efficient with
    the existing ``idx_atlas_candidates_user_pending`` index.
    """
    from sqlalchemy import and_, func as sqlfunc
    with get_connection() as conn:
        # First: total pending count for the "N more to review" tease
        total = (
            conn.execute(
                select(sqlfunc.count())
                .select_from(atlas_candidates)
                .where(
                    atlas_candidates.c.user_id == user_id,
                    atlas_candidates.c.status == "pending",
                )
            )
            .scalar_one()
        )

        # Page query
        query = (
            select(atlas_candidates)
            .where(
                atlas_candidates.c.user_id == user_id,
                atlas_candidates.c.status == "pending",
            )
            .order_by(atlas_candidates.c.created_at.desc(), atlas_candidates.c.id)
            .limit(limit + 1)  # +1 to detect if there's a next page
        )
        if after_id is not None:
            cursor_row = (
                conn.execute(
                    select(atlas_candidates.c.created_at).where(
                        atlas_candidates.c.id == after_id
                    )
                )
                .scalar_one_or_none()
            )
            if cursor_row is not None:
                query = query.where(
                    and_(
                        atlas_candidates.c.created_at <= cursor_row,
                        atlas_candidates.c.id != after_id,
                    )
                )

        rows = conn.execute(query).mappings().all()
        candidates = [_candidate_from_row(r) for r in rows[:limit]]
        next_cursor = candidates[-1].id if len(rows) > limit else None
        return candidates, next_cursor, total


# Async wrappers — same pattern as existing helpers
async def async_get_scan_history(user_id: UUID) -> AtlasScanHistory:
    return await asyncio.to_thread(get_scan_history, user_id)


async def async_upsert_scan_history(
    user_id: UUID,
    *,
    last_scanned_at: datetime,
    asset_count: int,
    candidates_surfaced: int,
) -> AtlasScanHistory:
    return await asyncio.to_thread(
        upsert_scan_history,
        user_id,
        last_scanned_at=last_scanned_at,
        asset_count=asset_count,
        candidates_surfaced=candidates_surfaced,
    )


async def async_dismiss_candidate(candidate_id: UUID, user_id: UUID) -> bool:
    return await asyncio.to_thread(dismiss_candidate, candidate_id, user_id)


async def async_list_pending_candidates_paginated(
    user_id: UUID,
    *,
    limit: int = 20,
    after_id: UUID | None = None,
) -> tuple[list[AtlasCandidate], UUID | None, int]:
    return await asyncio.to_thread(
        list_pending_candidates_paginated, user_id, limit=limit, after_id=after_id
    )
```

### 8e. Route additions

In `Travel Agent/backend/api/routes/atlas.py`:

1. **Add `DELETE /api/atlas/candidates/{candidate_id}`** between
   `approve_candidate` and the `# ─── Artifacts ───` separator:

```python
@router.delete(
    "/api/atlas/candidates/{candidate_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def dismiss_candidate_endpoint(
    candidate_id: UUID,
    actor: User = Depends(get_current_user),
) -> None:
    """Mark a candidate as dismissed. Idempotent — repeated calls succeed silently.

    Dismissed candidates do not re-appear in subsequent scans (the client
    is expected to check the dismiss status before re-submitting candidates
    that match a previously-dismissed date+place cluster).
    """
    from backend.core.db.atlas import async_dismiss_candidate
    # Idempotent: return 204 whether or not it was actually pending,
    # but a true 404 if the candidate doesn't exist or belongs to another user.
    from backend.core.db.atlas import async_get_candidate

    existing = await async_get_candidate(candidate_id, actor.id)
    if not existing:
        raise HTTPException(status_code=404, detail="candidate not found")
    await async_dismiss_candidate(candidate_id, actor.id)
```

2. **Modify `get_inbox`** to add pagination. Replace the current body
   with the paginated version that returns `AtlasInboxPage`:

```python
@router.get("/api/atlas/inbox", response_model=AtlasInboxPage)
async def get_inbox(
    limit: int = 20,
    after_id: UUID | None = None,
    actor: User = Depends(get_current_user),
) -> AtlasInboxPage:
    """Paginated Memory Inbox.

    V1.0: pending candidates + recent artifacts, cursor-paginated by
    ``created_at DESC``. Pass ``after_id`` of the last item in the previous
    page to get the next.
    """
    from backend.core.db.atlas import (
        async_list_pending_candidates_paginated,
        async_list_recent_artifacts,
    )

    limit = max(1, min(limit, 100))
    pending, next_cursor, total_pending = await async_list_pending_candidates_paginated(
        actor.id, limit=limit, after_id=after_id
    )
    # V1.0: artifacts only on the first page (no cursor); keeps the contract simple
    recent = await async_list_recent_artifacts(actor.id, limit=10) if after_id is None else []

    items: list[AtlasInboxItem] = []
    for candidate in pending:
        items.append(
            AtlasInboxItem(
                kind="pending_candidate",
                candidate=candidate,
                surfaced_at=candidate.created_at,
            )
        )
    for artifact in recent:
        shell = AtlasArtifactShell(
            id=artifact.id,
            source_candidate_id=artifact.source_candidate_id,
            artifact_type=artifact.artifact_type,
            title=artifact.title,
            hero_photo_id=artifact.hero_photo_id,
            photo_ids=artifact.photo_ids,
            map_points=artifact.map_points,
            date_range_start=artifact.date_range_start,
            date_range_end=artifact.date_range_end,
            place_label=artifact.place_label,
            generation_status=artifact.generation_status,
        )
        items.append(
            AtlasInboxItem(
                kind="recent_artifact",
                artifact=shell,
                surfaced_at=artifact.updated_at,
            )
        )
    items.sort(key=lambda i: i.surfaced_at, reverse=True)

    return AtlasInboxPage(
        items=items,
        next_cursor=str(next_cursor) if next_cursor else None,
        total_pending=total_pending,
    )
```

You'll need to import `AtlasInboxPage` from `backend.atlas.models`.
Don't remove `AtlasInboxResponse` from the imports — mock/test paths
may still use it.

3. **Add `GET /api/atlas/scan-history`** at the end of the file, before
   the closing comment:

```python
@router.get("/api/atlas/scan-history", response_model=AtlasScanHistory)
async def get_scan_history_endpoint(
    actor: User = Depends(get_current_user),
) -> AtlasScanHistory:
    """Last-scanned timestamp + lifetime counters for the user.

    Frontend calls this on app open to decide whether to trigger an
    incremental rescan. ``last_scanned_at`` null = user has never scanned.
    """
    from backend.core.db.atlas import async_get_scan_history
    return await async_get_scan_history(actor.id)
```

Import `AtlasScanHistory` from `backend.atlas.models`.

### 8f. Backend tests

Create `Travel Agent/tests/atlas/test_atlas_v1_scan_history.py`:

```python
"""Offline tests for V1.0 scan history + dismiss endpoints.

These cover Pydantic model contracts and the paginated inbox shape.
DB-backed integration tests live separately and need ``requires_postgres``.
"""

from __future__ import annotations

from datetime import datetime
from uuid import uuid4

import pytest

from backend.atlas.models import AtlasInboxPage, AtlasScanHistory


class TestAtlasScanHistory:
    def test_zero_initialized(self) -> None:
        hist = AtlasScanHistory(
            user_id=uuid4(),
            last_scanned_at=None,
            asset_count_at_last_scan=0,
            candidates_surfaced_total=0,
            candidates_approved_total=0,
            candidates_dismissed_total=0,
            updated_at=datetime.now().astimezone(),
        )
        assert hist.last_scanned_at is None
        assert hist.candidates_surfaced_total == 0

    def test_populated(self) -> None:
        now = datetime.now().astimezone()
        hist = AtlasScanHistory(
            user_id=uuid4(),
            last_scanned_at=now,
            asset_count_at_last_scan=1843,
            candidates_surfaced_total=12,
            candidates_approved_total=3,
            candidates_dismissed_total=4,
            updated_at=now,
        )
        assert hist.last_scanned_at == now
        assert hist.candidates_surfaced_total == 12


class TestAtlasInboxPage:
    def test_empty_page(self) -> None:
        page = AtlasInboxPage(items=[], next_cursor=None, total_pending=0)
        assert page.items == []
        assert page.next_cursor is None
        assert page.total_pending == 0

    def test_next_cursor_when_more(self) -> None:
        page = AtlasInboxPage(items=[], next_cursor="abc-123", total_pending=42)
        assert page.next_cursor == "abc-123"
        assert page.total_pending == 42
```

### Phase 1 verification

```bash
cd "Travel Agent"
ruff format --check backend/atlas/ backend/api/routes/atlas.py backend/core/db/_tables/atlas.py backend/core/db/atlas.py tests/atlas/
ruff check backend/atlas/ backend/api/routes/atlas.py backend/core/db/_tables/atlas.py backend/core/db/atlas.py tests/atlas/
PYTHONPATH=. python -c "
from backend.api.routes.atlas import router
print('routes:', len(router.routes))
assert len(router.routes) == 12, f'expected 12 routes, got {len(router.routes)}'
print('atlas_scan_history table:', __import__('backend.core.db.tables', fromlist=['atlas_scan_history']).atlas_scan_history.name)
"
PYTHONPATH=. pytest tests/atlas/ -q
PYTHONPATH=. alembic heads
```

Expected:
- ruff: 0 errors
- routes: 12 (10 from V0 + DELETE candidates + GET scan-history; the
  paginated inbox replaces the V0 inbox so net +2)
- atlas_scan_history table importable
- All tests pass (the V0 test count + the new tests)
- `alembic heads` shows `c2e9b4a8d1f7 (head)` (warning about
  `a1b2c3d4e5f6` collision will persist — that's OK, see V0 README)

---

## 9. Phase 2 — OpenAPI + TypeScript types sync

```bash
cd "/Users/feihuyan/Documents/Claude/Travel Workspace"
./scripts/sync-types.sh
```

If this fails with a non-Atlas error, the WIP state of other repos is
interfering. **Do not fix unrelated errors.** Document the issue,
roll back the openapi.json change, and proceed without sync — the
frontend can use re-exports already in `schema.gen.ts`. Add a
`TODO(atlas-v1.0-sync)` note in the commit message.

If sync succeeds, verify:

```bash
python3 -c "
import json
spec = json.load(open('docs/openapi.json'))
must_have = ['/api/atlas/scan-history']
for p in must_have:
    assert p in spec['paths'], f'missing path: {p}'
must_have_schemas = ['AtlasScanHistory', 'AtlasInboxPage']
for s in must_have_schemas:
    assert s in spec['components']['schemas'], f'missing schema: {s}'
print('OpenAPI sync OK')
"
```

---

## 10. Phase 3–6 — Frontend

### 10a. Frontend types (Phase 3a)

If sync-types.sh ran successfully in Phase 2, `schema.gen.ts` already
has `AtlasScanHistory` and `AtlasInboxPage`. Add re-exports to
`Travel App/types/atlas.ts`:

```typescript
export type AtlasScanHistory = components['schemas']['AtlasScanHistory'];
export type AtlasInboxPage = components['schemas']['AtlasInboxPage'];
```

If sync didn't run, hand-write these types matching the Pydantic models
in §8c.

### 10b. API client glue (Phase 3b)

In `Travel App/utils/api/interface.ts`, append to the Atlas section:

```typescript
  /** DELETE /api/atlas/candidates/{id} — dismiss a candidate. */
  dismissAtlasCandidate(candidateId: string): Promise<void>;

  /** GET /api/atlas/inbox — paginated; replaces the V0 non-paginated version. */
  getAtlasInboxPage(opts?: {
    limit?: number;
    afterId?: string;
  }): Promise<components['schemas']['AtlasInboxPage']>;

  /** GET /api/atlas/scan-history — when did this user last scan? */
  getAtlasScanHistory(): Promise<components['schemas']['AtlasScanHistory']>;
```

Keep the existing `getAtlasInbox()` method on the interface — some
existing V0 code calls it. Mark it deprecated in a comment.

In `Travel App/utils/api/http.ts`, append implementations:

```typescript
  async dismissAtlasCandidate(candidateId) {
    await _request<unknown>(`/api/atlas/candidates/${candidateId}`, {
      method: 'DELETE',
    });
  },

  async getAtlasInboxPage(opts) {
    const params = new URLSearchParams();
    if (opts?.limit !== undefined) params.set('limit', String(opts.limit));
    if (opts?.afterId !== undefined) params.set('after_id', opts.afterId);
    const qs = params.toString();
    return _request<components['schemas']['AtlasInboxPage']>(
      `/api/atlas/inbox${qs ? `?${qs}` : ''}`,
    );
  },

  async getAtlasScanHistory() {
    return _request<components['schemas']['AtlasScanHistory']>(
      '/api/atlas/scan-history',
    );
  },
```

In `Travel App/utils/api/mock.ts`, append to the `Object.assign(mockApi, ...)`
block (or to the main mockApi object if you choose to merge):

```typescript
  async dismissAtlasCandidate(candidateId: string) {
    const c = _atlasCandidates.get(candidateId);
    if (!c) throw new Error('candidate not found');
    _atlasCandidates.set(candidateId, { ...c, status: 'dismissed' });
  },

  async getAtlasInboxPage(opts?: { limit?: number; afterId?: string }) {
    const limit = opts?.limit ?? 20;
    const allPending = [..._atlasCandidates.values()]
      .filter((c) => c.status === 'pending')
      .sort((a, b) => (a.created_at < b.created_at ? 1 : -1));
    // Cursor: find index of afterId, return slice after
    let startIdx = 0;
    if (opts?.afterId) {
      const idx = allPending.findIndex((c) => c.id === opts.afterId);
      if (idx >= 0) startIdx = idx + 1;
    }
    const pageCandidates = allPending.slice(startIdx, startIdx + limit);
    const nextCursor =
      startIdx + limit < allPending.length ? pageCandidates[pageCandidates.length - 1].id : null;
    const items: components['schemas']['AtlasInboxItem'][] = pageCandidates.map((c) => ({
      kind: 'pending_candidate' as const,
      candidate: c,
      artifact: null,
      surfaced_at: c.created_at,
    }));
    // First page also includes recent artifacts
    if (!opts?.afterId) {
      for (const a of _atlasArtifacts.values()) {
        items.push({
          kind: 'recent_artifact' as const,
          candidate: null,
          artifact: {
            id: a.id,
            source_candidate_id: a.source_candidate_id,
            artifact_type: a.artifact_type,
            title: a.title,
            hero_photo_id: a.hero_photo_id,
            photo_ids: a.photo_ids,
            map_points: a.map_points,
            date_range_start: a.date_range_start,
            date_range_end: a.date_range_end,
            place_label: a.place_label,
            generation_status: a.generation_status,
          },
          surfaced_at: a.updated_at,
        });
      }
    }
    items.sort((x, y) => (x.surfaced_at < y.surfaced_at ? 1 : -1));
    return { items, next_cursor: nextCursor, total_pending: allPending.length };
  },

  async getAtlasScanHistory() {
    return {
      user_id: 'mock-user',
      last_scanned_at: null,
      asset_count_at_last_scan: 0,
      candidates_surfaced_total: 0,
      candidates_approved_total: 0,
      candidates_dismissed_total: 0,
      updated_at: new Date().toISOString(),
    };
  },
```

### 10c. Frontend utilities (Phase 4)

#### `Travel App/utils/atlasHomeWorkInference.ts`

Pure function. No React, no PhotoKit imports — easy to test against
fixture libraries.

```typescript
/**
 * Atlas home/work inference.
 *
 * Pure function — takes the user's photo GPS history, returns inferred
 * home + work centroids using density-based clustering + temporal
 * weighting (evenings/overnight = home; weekday 9–5 = work).
 *
 * No iOS API exists for "home" or "work" — Apple's Significant Locations
 * are E2E encrypted. We have to infer.
 *
 * V1.0 thresholds are anchors, to be calibrated against real libraries
 * in V1.2 polish per the V1 plan.
 */
import type { AtlasPickedPhoto } from '../hooks/useAtlasPhotoPicker';

export interface InferredLocation {
  latitude: number;
  longitude: number;
  /** Number of photos contributing to this cluster's centroid */
  photoCount: number;
}

export interface HomeWorkInference {
  home: InferredLocation | null;
  work: InferredLocation | null;
}

const GRID_CELL_DEG = 0.005;  // ~500m cell — tighter than the cluster grid since this is home, not trip
const MIN_DAYS_FOR_HOME = 5;
const MIN_PHOTOS_FOR_HOME = 10;

export function inferHomeWork(photos: AtlasPickedPhoto[]): HomeWorkInference {
  const withGps = photos.filter(
    (p) => p.latitude != null && p.longitude != null,
  );
  if (withGps.length < MIN_PHOTOS_FOR_HOME) {
    return { home: null, work: null };
  }

  // Group photos into ~500m grid cells
  type Cell = {
    latSum: number;
    lngSum: number;
    count: number;
    eveningOvernight: number;  // 21:00–07:59
    weekday9to5: number;        // Mon–Fri, 09:00–16:59
    distinctDays: Set<string>;
  };
  const cells = new Map<string, Cell>();
  for (const p of withGps) {
    const lat = Math.floor(p.latitude! / GRID_CELL_DEG);
    const lng = Math.floor(p.longitude! / GRID_CELL_DEG);
    const key = `${lat}:${lng}`;
    const d = new Date(p.timestamp);
    const hour = d.getHours();
    const dow = d.getDay();
    const isEveningOvernight = hour >= 21 || hour < 8;
    const isWeekday9to5 = dow >= 1 && dow <= 5 && hour >= 9 && hour < 17;
    const dayKey = `${d.getFullYear()}-${d.getMonth()}-${d.getDate()}`;

    const cell = cells.get(key);
    if (cell) {
      cell.latSum += p.latitude!;
      cell.lngSum += p.longitude!;
      cell.count += 1;
      if (isEveningOvernight) cell.eveningOvernight += 1;
      if (isWeekday9to5) cell.weekday9to5 += 1;
      cell.distinctDays.add(dayKey);
    } else {
      cells.set(key, {
        latSum: p.latitude!,
        lngSum: p.longitude!,
        count: 1,
        eveningOvernight: isEveningOvernight ? 1 : 0,
        weekday9to5: isWeekday9to5 ? 1 : 0,
        distinctDays: new Set([dayKey]),
      });
    }
  }

  // Score each cell. Home = max evening/overnight density across distinct days.
  // Work = max weekday-9-to-5 density across distinct days.
  let bestHome: { cell: Cell; score: number } | null = null;
  let bestWork: { cell: Cell; score: number } | null = null;
  for (const cell of cells.values()) {
    if (cell.distinctDays.size < MIN_DAYS_FOR_HOME) continue;
    if (cell.count < MIN_PHOTOS_FOR_HOME) continue;
    const homeScore = cell.eveningOvernight * cell.distinctDays.size;
    const workScore = cell.weekday9to5 * cell.distinctDays.size;
    if (homeScore > 0 && (!bestHome || homeScore > bestHome.score)) {
      bestHome = { cell, score: homeScore };
    }
    if (workScore > 0 && (!bestWork || workScore > bestWork.score)) {
      bestWork = { cell, score: workScore };
    }
  }

  return {
    home: bestHome
      ? {
          latitude: bestHome.cell.latSum / bestHome.cell.count,
          longitude: bestHome.cell.lngSum / bestHome.cell.count,
          photoCount: bestHome.cell.count,
        }
      : null,
    work: bestWork
      ? {
          latitude: bestWork.cell.latSum / bestWork.cell.count,
          longitude: bestWork.cell.lngSum / bestWork.cell.count,
          photoCount: bestWork.cell.count,
        }
      : null,
  };
}

const HOME_HARD_SUPPRESS_METERS = 100;
const HOME_SOFT_SUPPRESS_METERS = 500;

export function distanceMeters(
  lat1: number,
  lng1: number,
  lat2: number,
  lng2: number,
): number {
  // Equirectangular approximation; fine for <1km distances.
  const R = 6371000;
  const x = ((lng2 - lng1) * Math.PI) / 180 * Math.cos(((lat1 + lat2) / 2 * Math.PI) / 180);
  const y = ((lat2 - lat1) * Math.PI) / 180;
  return Math.sqrt(x * x + y * y) * R;
}

export type SuppressionLevel = 'hard' | 'soft' | 'none';

export function homeSuppressionLevel(
  photoLat: number,
  photoLng: number,
  home: InferredLocation | null,
): SuppressionLevel {
  if (!home) return 'none';
  const d = distanceMeters(photoLat, photoLng, home.latitude, home.longitude);
  if (d < HOME_HARD_SUPPRESS_METERS) return 'hard';
  if (d < HOME_SOFT_SUPPRESS_METERS) return 'soft';
  return 'none';
}
```

#### `Travel App/utils/atlasIncrementalScan.ts`

```typescript
/**
 * Atlas incremental rescan — V1.0 AsyncStorage-based approximation of
 * ``PHPersistentChangeToken`` (which is V1.1 work, behind a custom Expo
 * Module).
 *
 * On each scan, we persist the most-recent asset creationTime we saw.
 * Next scan, we query only assets newer than that. Approximate — misses
 * deletions and edits — but acceptable for V1.0.
 */
import AsyncStorage from '@react-native-async-storage/async-storage';

const LAST_SCANNED_KEY = 'atlas:last_scanned_at';
const LAST_ASSET_COUNT_KEY = 'atlas:last_asset_count';

export async function readLastScannedAt(): Promise<number | null> {
  try {
    const raw = await AsyncStorage.getItem(LAST_SCANNED_KEY);
    return raw ? Number(raw) : null;
  } catch {
    return null;
  }
}

export async function writeLastScannedAt(timestampMs: number): Promise<void> {
  try {
    await AsyncStorage.setItem(LAST_SCANNED_KEY, String(timestampMs));
  } catch {
    // Silently fail — incremental scan optimization, not correctness-critical
  }
}

export async function readLastAssetCount(): Promise<number> {
  try {
    const raw = await AsyncStorage.getItem(LAST_ASSET_COUNT_KEY);
    return raw ? Number(raw) : 0;
  } catch {
    return 0;
  }
}

export async function writeLastAssetCount(count: number): Promise<void> {
  try {
    await AsyncStorage.setItem(LAST_ASSET_COUNT_KEY, String(count));
  } catch {}
}

export async function resetIncrementalState(): Promise<void> {
  try {
    await AsyncStorage.multiRemove([LAST_SCANNED_KEY, LAST_ASSET_COUNT_KEY]);
  } catch {}
}
```

#### `Travel App/utils/atlasCluster.ts` modification

Change the existing `clusterPhotos` signature to accept an options object:

```typescript
export interface ClusterOptions {
  /** Minimum photos in a cluster for it to surface. V0 manual-pick: 3. V1 auto-scan: 15. */
  minClusterSize?: number;
  /** Maximum candidates returned. */
  maxCandidates?: number;
  /** Inferred home for suppression. If provided, candidates inside 500m of home are demoted. */
  home?: { latitude: number; longitude: number } | null;
}

export function clusterPhotos(
  photos: AtlasPickedPhoto[],
  opts: ClusterOptions = {},
): AtlasCandidateCreate[] {
  const minClusterSize = opts.minClusterSize ?? 3;
  const maxCandidates = opts.maxCandidates ?? 5;
  // ... existing logic, replacing MIN_CLUSTER_SIZE references ...
}
```

Existing callers (in `app/atlas/scan.tsx`) still work because the
options are optional.

Then in the candidate-building step, apply home suppression:

```typescript
import { homeSuppressionLevel } from './atlasHomeWorkInference';

// Inside the cluster-building loop, after candidate is built:
if (opts.home) {
  const centroidLat = bucket[0].latitude;  // or compute properly
  const centroidLng = bucket[0].longitude;
  if (centroidLat != null && centroidLng != null) {
    const level = homeSuppressionLevel(centroidLat, centroidLng, opts.home);
    if (level === 'hard') continue;  // skip entirely
    if (level === 'soft') {
      // demote to place_memory only if it has clustered visits
      if (candidate.candidate_type !== 'place_memory') continue;
    }
  }
}
```

#### Fixture tests

Create `Travel App/__tests__/utils/atlasCluster.test.ts`:

```typescript
import { clusterPhotos } from '../../utils/atlasCluster';
import { inferHomeWork } from '../../utils/atlasHomeWorkInference';
import type { AtlasPickedPhoto } from '../../hooks/useAtlasPhotoPicker';

// ─── Fixture helpers ───────────────────────────────────────────────────────

const BROOKLYN_LAT = 40.7128;
const BROOKLYN_LNG = -73.9858;
const TOKYO_LAT = 35.6762;
const TOKYO_LNG = 139.6503;

function syntheticPhoto(
  id: string,
  daysAgo: number,
  hour: number,
  lat: number | null,
  lng: number | null,
): AtlasPickedPhoto {
  const date = new Date();
  date.setDate(date.getDate() - daysAgo);
  date.setHours(hour, 0, 0, 0);
  return {
    id,
    timestamp: date.getTime(),
    latitude: lat,
    longitude: lng,
    mediaType: 'photo',
    mediaSubtypes: [],
    isFavorite: false,
  };
}

// ─── Tests ────────────────────────────────────────────────────────────────

describe('Brooklyn weekly shooter regression', () => {
  // 400 photos near home over 8 months + 200 photos in Tokyo for 6 days
  const photos: AtlasPickedPhoto[] = [];
  // Home photos — evenings, varied days across 8 months
  for (let i = 0; i < 400; i++) {
    const daysAgo = Math.floor(Math.random() * 240);
    photos.push(
      syntheticPhoto(
        `home-${i}`,
        daysAgo,
        22,  // evening
        BROOKLYN_LAT + (Math.random() - 0.5) * 0.001,
        BROOKLYN_LNG + (Math.random() - 0.5) * 0.001,
      ),
    );
  }
  // Tokyo trip — 6 consecutive days, ~33 photos/day
  for (let day = 0; day < 6; day++) {
    for (let p = 0; p < 33; p++) {
      photos.push(
        syntheticPhoto(
          `tokyo-${day}-${p}`,
          90 - day,  // ~3 months ago
          10 + (p % 12),
          TOKYO_LAT + (Math.random() - 0.5) * 0.05,
          TOKYO_LNG + (Math.random() - 0.5) * 0.05,
        ),
      );
    }
  }

  it('infers home at Brooklyn centroid', () => {
    const { home } = inferHomeWork(photos);
    expect(home).not.toBeNull();
    expect(Math.abs(home!.latitude - BROOKLYN_LAT)).toBeLessThan(0.01);
    expect(Math.abs(home!.longitude - BROOKLYN_LNG)).toBeLessThan(0.01);
  });

  it('surfaces Tokyo as a high-confidence trip', () => {
    const { home } = inferHomeWork(photos);
    const candidates = clusterPhotos(photos, { minClusterSize: 15, home });
    const tokyoCandidates = candidates.filter(
      (c) => c.confidence === 'high' && c.candidate_type === 'trip',
    );
    expect(tokyoCandidates.length).toBeGreaterThanOrEqual(1);
  });

  it('does NOT surface home-radius photos as primary candidates', () => {
    const { home } = inferHomeWork(photos);
    const candidates = clusterPhotos(photos, { minClusterSize: 15, home });
    // No primary candidate should be near Brooklyn home
    for (const c of candidates) {
      // Loose check: if there's a candidate with hundreds of photos, it shouldn't
      // be the home cluster — should be Tokyo
      if (c.photo_count > 100) {
        // Heuristic: home cluster would have place_count == 1 because all 400 photos
        // are in the same grid cell; Tokyo will have a higher place_count
        expect(c.place_count).toBeGreaterThan(1);
      }
    }
  });
});

describe('all-home library produces no candidates', () => {
  it('returns empty when entirely within 300m of inferred home', () => {
    const photos: AtlasPickedPhoto[] = [];
    for (let i = 0; i < 200; i++) {
      const daysAgo = Math.floor(Math.random() * 180);
      photos.push(
        syntheticPhoto(
          `home-${i}`,
          daysAgo,
          22,
          BROOKLYN_LAT + (Math.random() - 0.5) * 0.002,  // ~200m spread
          BROOKLYN_LNG + (Math.random() - 0.5) * 0.002,
        ),
      );
    }
    const { home } = inferHomeWork(photos);
    const candidates = clusterPhotos(photos, { minClusterSize: 15, home });
    // All photos are within home radius — should produce zero primary candidates
    const primary = candidates.filter((c) => c.candidate_type !== 'place_memory');
    expect(primary.length).toBe(0);
  });
});
```

### 10d. Frontend hooks (Phase 5)

#### `Travel App/hooks/useAtlasFullScan.ts`

```typescript
/**
 * useAtlasFullScan — paginated full-library scan via expo-media-library.
 *
 * Cancelable. Surfaces progress (assetsLoaded / assetsTotal). Skips
 * scan when device is in Low Power Mode.
 *
 * V1.1 will replace the AsyncStorage timestamp with PHPersistentChangeToken
 * via a custom Expo Module. The hook surface stays stable.
 */
import { useCallback, useRef, useState } from 'react';
import { Platform } from 'react-native';
import * as MediaLibrary from 'expo-media-library';
import { isPhotoAccessGranted } from '../utils/photoPermission';
import { readLastScannedAt, writeLastScannedAt } from '../utils/atlasIncrementalScan';
import type { AtlasPickedPhoto } from './useAtlasPhotoPicker';

const PAGE_SIZE = 500;

export interface UseAtlasFullScanResult {
  isScanning: boolean;
  assetsLoaded: number;
  assetsTotal: number;
  isError: boolean;
  isLowPowerMode: boolean;
  startScan: (opts?: { incremental?: boolean }) => Promise<AtlasPickedPhoto[]>;
  cancelScan: () => void;
}

export function useAtlasFullScan(): UseAtlasFullScanResult {
  const [isScanning, setIsScanning] = useState(false);
  const [assetsLoaded, setAssetsLoaded] = useState(0);
  const [assetsTotal, setAssetsTotal] = useState(0);
  const [isError, setIsError] = useState(false);
  const [isLowPowerMode, setIsLowPowerMode] = useState(false);
  const cancelRef = useRef(false);

  const cancelScan = useCallback(() => {
    cancelRef.current = true;
  }, []);

  const startScan = useCallback(
    async (opts: { incremental?: boolean } = {}): Promise<AtlasPickedPhoto[]> => {
      cancelRef.current = false;
      setIsScanning(true);
      setIsError(false);
      setAssetsLoaded(0);
      setAssetsTotal(0);

      try {
        // Low Power Mode check
        const lowPower = await detectLowPowerMode();
        if (lowPower) {
          setIsLowPowerMode(true);
          setIsScanning(false);
          return [];
        }

        const { status } = await MediaLibrary.getPermissionsAsync();
        if (!isPhotoAccessGranted(status)) {
          setIsScanning(false);
          return [];
        }

        const createdAfter = opts.incremental ? (await readLastScannedAt()) ?? undefined : undefined;
        const collected: AtlasPickedPhoto[] = [];
        let cursor: string | undefined;
        let totalReportedByOs = 0;

        while (true) {
          if (cancelRef.current) break;
          const page: MediaLibrary.PagedInfo<MediaLibrary.Asset> =
            await MediaLibrary.getAssetsAsync({
              mediaType: MediaLibrary.MediaType.photo,
              first: PAGE_SIZE,
              after: cursor,
              ...(createdAfter !== undefined ? { createdAfter } : {}),
              sortBy: [MediaLibrary.SortBy.creationTime],
            });
          totalReportedByOs = page.totalCount;
          if (assetsTotal !== totalReportedByOs) setAssetsTotal(totalReportedByOs);

          for (const asset of page.assets) {
            if (cancelRef.current) break;
            let location: { latitude: number; longitude: number } | null = null;
            try {
              const info = await MediaLibrary.getAssetInfoAsync(asset.id);
              location = info.location ?? null;
            } catch {}
            const subtypes: readonly string[] =
              (asset as unknown as { mediaSubtypes?: readonly string[] }).mediaSubtypes ?? [];
            collected.push({
              id: asset.id,
              timestamp: asset.creationTime,
              latitude: location?.latitude ?? null,
              longitude: location?.longitude ?? null,
              mediaType: asset.mediaType,
              mediaSubtypes: subtypes,
              isFavorite: Boolean(
                (asset as unknown as { isFavorite?: boolean }).isFavorite,
              ),
            });
            setAssetsLoaded(collected.length);
          }

          if (!page.hasNextPage) break;
          cursor = page.endCursor;
        }

        // Record the most-recent timestamp seen for next incremental scan
        if (collected.length > 0) {
          const mostRecent = Math.max(...collected.map((p) => p.timestamp));
          await writeLastScannedAt(mostRecent);
        }

        return collected;
      } catch {
        setIsError(true);
        return [];
      } finally {
        setIsScanning(false);
      }
    },
    [assetsTotal],
  );

  return {
    isScanning,
    assetsLoaded,
    assetsTotal,
    isError,
    isLowPowerMode,
    startScan,
    cancelScan,
  };
}

async function detectLowPowerMode(): Promise<boolean> {
  if (Platform.OS !== 'ios') return false;
  try {
    // React Native exposes this through expo-battery or NativeModules.
    // V1.0 best-effort: check via expo-battery if available; else assume false.
    const battery = await import('expo-battery');
    return await battery.isLowPowerModeEnabledAsync();
  } catch {
    return false;
  }
}
```

(If `expo-battery` is not a dep, just always return `false` — Low Power Mode handling becomes a `TODO(atlas-v1.0-lowpower)`.)

#### Modify `Travel App/hooks/useAtlasPhotoPicker.ts`

Don't remove the `loadSelectedPhotos` method. Add a `loadAllPhotos`
method that fetches everything available under the current permission
(in full mode, the whole library; in limited mode, the user-selected
subset — same shape, different scope):

```typescript
const loadAllPhotos = useCallback(async (): Promise<void> => {
  // Identical to loadSelectedPhotos for now — the difference is that
  // upstream code calls this after requesting BROAD permission, where
  // getAssetsAsync returns the whole library, not the limited subset.
  // The hook doesn't know which mode it's in; it just queries.
  await loadSelectedPhotos();
}, [loadSelectedPhotos]);

return {
  // ... existing returns ...
  loadAllPhotos,
};
```

Update `UseAtlasPhotoPickerResult` accordingly.

#### Data hooks in `Travel App/data/atlas.ts`

Append:

```typescript
import type { AtlasInboxPage, AtlasScanHistory } from '../types/atlas';

const _emptyInboxPage: AtlasInboxPage = {
  items: [],
  next_cursor: null,
  total_pending: 0,
};

const _emptyScanHistory: AtlasScanHistory = {
  user_id: '',
  last_scanned_at: null,
  asset_count_at_last_scan: 0,
  candidates_surfaced_total: 0,
  candidates_approved_total: 0,
  candidates_dismissed_total: 0,
  updated_at: new Date().toISOString(),
};

export function useAtlasInboxPage(afterId?: string): AtlasInboxPage {
  const { data } = useData<AtlasInboxPage>(
    ['atlas', 'inbox-page', afterId ?? null],
    () => api.getAtlasInboxPage({ afterId }),
    _emptyInboxPage,
  );
  return data ?? _emptyInboxPage;
}

export function useAtlasScanHistory(): AtlasScanHistory {
  const { data } = useData<AtlasScanHistory>(
    ['atlas', 'scan-history'],
    () => api.getAtlasScanHistory(),
    _emptyScanHistory,
  );
  return data ?? _emptyScanHistory;
}

export interface UseDismissCandidateResult {
  dismiss: (id: string) => Promise<void>;
  isPending: boolean;
}

export function useDismissCandidate(): UseDismissCandidateResult {
  const qc = useQueryClient();
  const [isPending, setPending] = useState(false);
  const dismiss = useCallback(
    async (id: string) => {
      setPending(true);
      try {
        await api.dismissAtlasCandidate(id);
        await qc.invalidateQueries({ queryKey: ['atlas'] });
      } finally {
        setPending(false);
      }
    },
    [qc],
  );
  return { dismiss, isPending };
}
```

### 10e. Frontend screens (Phase 6)

#### `Travel App/components/atlas/ScanProgressCard.tsx`

```tsx
/**
 * Foreground scan progress UI. Shows photos-loaded/total + cancel button.
 */
import React from 'react';
import { ActivityIndicator, Pressable, StyleSheet, Text, View } from 'react-native';
import { colors } from '../../constants/colors';
import { typography } from '../../constants/typography';
import { radius, spacing } from '../../constants/layout';

interface ScanProgressCardProps {
  loaded: number;
  total: number;
  isLowPowerMode: boolean;
  onCancel: () => void;
}

export function ScanProgressCard({
  loaded,
  total,
  isLowPowerMode,
  onCancel,
}: ScanProgressCardProps) {
  if (isLowPowerMode) {
    return (
      <View style={styles.container}>
        <Text style={styles.title}>Low Power Mode</Text>
        <Text style={styles.body}>
          Vesper will resume scanning when your phone is charging.
        </Text>
      </View>
    );
  }
  const pct = total > 0 ? Math.round((loaded / total) * 100) : 0;
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Looking for travel-shaped memories…</Text>
      <Text style={styles.body}>
        {total > 0 ? `${loaded.toLocaleString()} of ${total.toLocaleString()} photos · ${pct}%` : `${loaded.toLocaleString()} photos`}
      </Text>
      <ActivityIndicator color={colors.action.primary} />
      <Pressable onPress={onCancel}>
        <Text style={styles.cancel}>Cancel</Text>
      </Pressable>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    padding: spacing.lg,
    borderRadius: radius.md,
    backgroundColor: colors.background.secondary,
    gap: spacing.md,
    alignItems: 'center',
  },
  title: { ...typography.h2, color: colors.text.primary },
  body: { ...typography.body, color: colors.text.secondary },
  cancel: { ...typography.bodyMd, color: colors.action.text, marginTop: spacing.sm },
});
```

#### `Travel App/components/atlas/InboxItem.tsx`

```tsx
import React from 'react';
import { Pressable, StyleSheet, Text, View } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { router } from 'expo-router';
import { CandidateCard } from './CandidateCard';
import { useDismissCandidate } from '../../data/atlas';
import type { AtlasInboxItem } from '../../types/atlas';
import { colors } from '../../constants/colors';
import { typography } from '../../constants/typography';
import { radius, spacing } from '../../constants/layout';

interface InboxItemProps {
  item: AtlasInboxItem;
}

export function InboxItem({ item }: InboxItemProps) {
  const { dismiss, isPending } = useDismissCandidate();

  if (item.kind === 'pending_candidate' && item.candidate) {
    return (
      <View>
        <CandidateCard candidate={item.candidate} />
        <Pressable
          style={styles.dismiss}
          onPress={() => dismiss(item.candidate!.id)}
          disabled={isPending}
          accessibilityRole="button"
          accessibilityLabel="Dismiss this candidate"
        >
          <Ionicons name="close" size={14} color={colors.text.secondary} />
          <Text style={styles.dismissText}>Not a memory</Text>
        </Pressable>
      </View>
    );
  }

  if (item.kind === 'recent_artifact' && item.artifact) {
    const a = item.artifact;
    return (
      <Pressable
        style={styles.artifactRow}
        onPress={() => router.push(`/atlas/artifact/${a.id}`)}
      >
        <Text style={styles.artifactTitle}>{a.title}</Text>
        <Text style={styles.artifactMeta}>
          {a.date_range_start} → {a.date_range_end}
        </Text>
      </Pressable>
    );
  }

  return null;
}

const styles = StyleSheet.create({
  dismiss: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: spacing.xs,
    alignSelf: 'flex-end',
    paddingVertical: spacing.sm,
    paddingHorizontal: spacing.md,
  },
  dismissText: { ...typography.caption, color: colors.text.secondary },
  artifactRow: {
    padding: spacing.lg,
    backgroundColor: colors.background.primary,
    borderRadius: radius.md,
    borderWidth: 1,
    borderColor: colors.border.light,
    gap: spacing.xs,
  },
  artifactTitle: { ...typography.h2, color: colors.text.primary },
  artifactMeta: { ...typography.caption, color: colors.text.secondary },
});
```

#### `Travel App/app/atlas/inbox.tsx`

```tsx
/**
 * Memory Inbox — dedicated page for the user's pending candidates + recent
 * artifacts, with cursor pagination.
 */
import React, { useState } from 'react';
import { FlatList, Pressable, StyleSheet, Text, View } from 'react-native';
import { Stack, router } from 'expo-router';
import { Ionicons } from '@expo/vector-icons';
import { useSafeAreaInsets } from 'react-native-safe-area-context';
import { InboxItem } from '../../components/atlas/InboxItem';
import { useAtlasInboxPage } from '../../data/atlas';
import { colors } from '../../constants/colors';
import { typography } from '../../constants/typography';
import { spacing } from '../../constants/layout';

export default function AtlasInboxScreen() {
  const insets = useSafeAreaInsets();
  const [cursor, setCursor] = useState<string | undefined>(undefined);
  const page = useAtlasInboxPage(cursor);

  return (
    <View style={[styles.container, { paddingTop: insets.top + spacing.lg }]}>
      <Stack.Screen options={{ headerShown: false }} />
      <View style={styles.header}>
        <Pressable onPress={() => router.back()}>
          <Ionicons name="chevron-back" size={24} color={colors.text.primary} />
        </Pressable>
        <Text style={styles.title}>Memory Inbox</Text>
      </View>
      {page.total_pending > 0 ? (
        <Text style={styles.tease}>
          {page.total_pending} memor{page.total_pending === 1 ? 'y' : 'ies'} to review
        </Text>
      ) : null}
      <FlatList
        data={page.items}
        keyExtractor={(item, idx) =>
          (item.candidate?.id ?? item.artifact?.id ?? `idx-${idx}`)
        }
        renderItem={({ item }) => <InboxItem item={item} />}
        contentContainerStyle={styles.list}
        ListFooterComponent={
          page.next_cursor ? (
            <Pressable
              style={styles.loadMore}
              onPress={() => setCursor(page.next_cursor ?? undefined)}
            >
              <Text style={styles.loadMoreText}>Load more</Text>
            </Pressable>
          ) : null
        }
        ListEmptyComponent={
          <Text style={styles.empty}>
            Nothing to review right now. Vesper will surface new memories as your photo
            library grows.
          </Text>
        }
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: colors.screen.canvas },
  header: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: spacing.md,
    paddingHorizontal: spacing.lg,
  },
  title: { ...typography.display, color: colors.text.primary },
  tease: {
    ...typography.caption,
    color: colors.text.secondary,
    paddingHorizontal: spacing.lg,
    paddingTop: spacing.sm,
  },
  list: { padding: spacing.lg, gap: spacing.md },
  loadMore: {
    paddingVertical: spacing.md,
    alignItems: 'center',
  },
  loadMoreText: { ...typography.bodyMd, color: colors.action.text },
  empty: {
    ...typography.body,
    color: colors.text.secondary,
    padding: spacing.lg,
    textAlign: 'center',
  },
});
```

#### Modify `Travel App/app/atlas/scan.tsx`

Add a new branch when the user picks "Find memories from photos" — instead of routing through manual-pick, trigger the full scan via `useAtlasFullScan`. Then run `clusterPhotos` with `minClusterSize: 15`, `home: inferHomeWork(allPhotos).home`, submit, navigate to `/atlas/inbox`.

This is the largest edit. Sketch:

```tsx
import { useAtlasFullScan } from '../../hooks/useAtlasFullScan';
import { inferHomeWork } from '../../utils/atlasHomeWorkInference';
// ...

const fullScan = useAtlasFullScan();

const runFullScan = useCallback(async () => {
  setStep('scan');
  // request broad permission first
  const granted = await picker.requestPermission();
  if (!granted) { /* same fallback */ return; }
  const photos = await fullScan.startScan({ incremental: false });
  if (photos.length === 0) {
    setStatus('No photos found.');
    return;
  }
  const { home } = inferHomeWork(photos);
  const clustered = clusterPhotos(photos, { minClusterSize: 15, home });
  if (clustered.length === 0) {
    Alert.alert('No memories found', 'Vesper couldn\'t find a travel-shaped cluster.');
    return;
  }
  await submit({ candidates: clustered });
  router.replace('/atlas/inbox');
}, [picker, fullScan, submit]);

// Wire to the "Find memories from photos" PathButton
<PathButton
  icon="search-outline"
  label="Find memories from photos"
  sublabel="Vesper scans your library for travel-shaped clusters"
  onPress={runFullScan}
/>
```

Keep the existing manual-pick flow on the "Choose photos myself" button.

#### Modify `Travel App/app/(tabs)/atlas/index.tsx`

Add a "View all" link in the Memory Inbox section header when there are more than 3 pending candidates:

```tsx
import { useAtlasInboxPage } from '../../../data/atlas';

// inside AtlasIndex
const inboxPage = useAtlasInboxPage();
const pending = inboxPage.items.filter((i) => i.kind === 'pending_candidate');

{pending.length > 0 ? (
  <View style={styles.section}>
    <View style={styles.sectionHeader}>
      <Text style={styles.sectionLabel}>Memory Inbox</Text>
      {inboxPage.total_pending > 3 ? (
        <Pressable onPress={() => router.push('/atlas/inbox')}>
          <Text style={styles.viewAll}>View all {inboxPage.total_pending}</Text>
        </Pressable>
      ) : null}
    </View>
    {/* ... existing rendering ... */}
  </View>
) : null}
```

Add `sectionHeader` and `viewAll` to the styles object.

---

## 11. Phase 7 — Verification + acceptance

### Verification commands

```bash
# Backend
cd "Travel Agent"
ruff format --check backend/atlas/ backend/api/routes/atlas.py backend/core/db/_tables/atlas.py backend/core/db/atlas.py tests/atlas/
ruff check backend/atlas/ backend/api/routes/atlas.py backend/core/db/_tables/atlas.py backend/core/db/atlas.py tests/atlas/
PYTHONPATH=. pytest tests/atlas/ -q
PYTHONPATH=. alembic heads

# Sync
cd "/Users/feihuyan/Documents/Claude/Travel Workspace"
./scripts/sync-types.sh

# Frontend
cd "Travel App"
npx tsc --noEmit
npx jest __tests__/utils/atlasCluster.test.ts
npx expo lint app/atlas/ app/\(tabs\)/atlas/ hooks/useAtlasFullScan.ts hooks/useAtlasPhotoPicker.ts data/atlas.ts utils/atlasCluster.ts utils/atlasHomeWorkInference.ts utils/atlasIncrementalScan.ts components/atlas/
```

### Acceptance checklist

- [ ] Backend ruff format + check clean on all atlas files
- [ ] `PYTHONPATH=. pytest tests/atlas/ -q` shows all V0 tests + new V1 tests passing
- [ ] `alembic heads` shows `c2e9b4a8d1f7 (head)` (`a1b2c3d4e5f6` collision warning persists — that's OK)
- [ ] `./scripts/sync-types.sh` succeeds OR is documented as skipped due to WIP collision
- [ ] `npx tsc --noEmit` returns 0 errors in Travel App
- [ ] `__tests__/utils/atlasCluster.test.ts` Brooklyn fixture passes
- [ ] `__tests__/utils/atlasCluster.test.ts` all-home fixture passes (zero primary candidates)
- [ ] Atlas tab loads without crash; Memory Inbox section visible
- [ ] `/atlas/inbox` route accessible and renders the page
- [ ] `/atlas/scan` "Find memories from photos" button triggers `useAtlasFullScan` (not the manual-pick path)

### Commit strategy

Three commits, one per repo. Branch names: `atlas-v1.0` in each repo (or
whatever the cloud agent's worktree convention is). Commit messages:

**Travel Agent:**
```
feat(atlas): V1.0 scan history + pagination + candidate dismiss

- Add atlas_scan_history table + Pydantic model + storage helpers
- Add DELETE /api/atlas/candidates/{id} (dismiss; idempotent)
- Add GET /api/atlas/scan-history
- Migrate GET /api/atlas/inbox to cursor-paginated AtlasInboxPage
- Migration c2e9b4a8d1f7 chains off V0 head a7b4c1d8e5f2
- Tests cover scan history + paginated inbox models

See docs/Plan — Atlas V1 Engineering.md §V1.0 for the full scope.
```

**Travel App:**
```
feat(atlas): V1.0 full-library scan + Memory Inbox + dismiss

- New hooks/useAtlasFullScan.ts (paginated getAssetsAsync + progress + cancel)
- New utils/atlasHomeWorkInference.ts (DBSCAN + temporal weighting)
- New utils/atlasIncrementalScan.ts (AsyncStorage timestamp; V1.1 will replace
  with PHPersistentChangeToken)
- clusterPhotos now accepts minClusterSize + home suppression
- New app/atlas/inbox.tsx (dedicated paginated inbox screen)
- New components/atlas/{ScanProgressCard, InboxItem}.tsx
- data/atlas.ts: useAtlasInboxPage, useAtlasScanHistory, useDismissCandidate
- API client: dismissAtlasCandidate, getAtlasInboxPage, getAtlasScanHistory
- scan.tsx wires "Find memories from photos" to the full-scan path
- Atlas tab landing shows "View all" link when >3 pending

Brooklyn weekly-shooter + all-home regression fixtures green.

See docs/Plan — Atlas V1 Engineering.md §V1.0 for the full scope.
```

**Workspace:**
```
chore(atlas): sync OpenAPI snapshot for V1.0 backend additions

Adds AtlasScanHistory, AtlasInboxPage schemas + new endpoints
(/api/atlas/scan-history, paginated /api/atlas/inbox, dismiss DELETE).
```

If the workspace sync didn't run, skip the workspace commit and note it
in the PR description.

### Final PR description (Travel App + Travel Agent)

Once branches are pushed, open PRs against the same target branch the
V0 work was on (likely the `codex/dogfood-readiness-*` branches —
verify from the existing branch state). PR title:

```
Atlas V1.0 — full-library scan, Memory Inbox, candidate dismiss
```

PR body:

```markdown
Builds the V1.0 scope from `docs/Plan — Atlas V1 Engineering.md` §V1.0.

## What ships

- Backend: scan history table + endpoint, dismiss endpoint, paginated inbox
- Frontend: full-library auto-scan, home/work inference, Memory Inbox screen,
  candidate dismiss
- Brooklyn weekly-shooter + all-home regression fixtures pass

## What's deferred to V1.1 (not in this PR)

- Custom Expo Module (Swift) for burst grouping, Vision feature prints,
  PHPersistentChangeToken, JournalingSuggestions
- Background catch-up via BGAppRefreshTask
- The plan §V1.1 covers this

## Verification

- [x] `PYTHONPATH=. pytest tests/atlas/ -q` all green
- [x] `npx tsc --noEmit` 0 errors
- [x] `__tests__/utils/atlasCluster.test.ts` Brooklyn + all-home fixtures pass
- [x] `ruff format --check` + `ruff check` clean on all atlas files
- [x] Manual smoke: Atlas tab loads, scan flow triggers full-library scan,
      candidates appear in Memory Inbox, dismiss works
```

---

## 12. Known gotchas

These are real lessons from V0 that will save you time:

1. **Alembic revision IDs collide easily.** Before writing a new
   migration, `grep -l "revision = '<your_id>'" alembic/versions/*.py`
   to verify uniqueness. The chosen ID `c2e9b4a8d1f7` was verified
   unique at handoff time but re-check before committing.

2. **The `a1b2c3d4e5f6` budget WIP migration has an unresolved
   revision-ID collision with `add_delegation_preferences.py`.** This
   creates a multi-head warning that persists across all atlas work.
   Document it; don't try to fix it.

3. **`Travel App/utils/api/*` files are large (1400–4000 lines).**
   When editing them, you MUST `Read` them through the harness's read
   gate before `Edit`-ing — even if you only need to append. Read with
   `offset` near the file end if the file is large.

4. **Mock/real parity matters.** Every new method added to `interface.ts`
   needs a real impl in `http.ts` AND a mock impl in `mock.ts`. CI
   would fail on missing implementations.

5. **`./scripts/sync-types.sh` regenerates `docs/openapi.json` AND
   `Travel App/utils/api/schema.gen.ts`.** Both files become modified.
   This is expected; commit both with the same change.

6. **`expo-media-library` `getAssetsAsync` returns up to ~1000 assets
   per call regardless of `first`.** Pagination is real — `endCursor`
   + `hasNextPage`. Don't ask for `first: 100000` and assume you get them all.

7. **`getAssetInfoAsync` is slow per call (~50ms each on a real device).**
   The full-scan hook calls it per asset to fetch GPS — for a 10k-photo
   library that's ~8 minutes of compute. **Defensive scope:** for V1.0,
   skip `getAssetInfoAsync` and use only the bare `asset.location` field
   (which Asset technically doesn't type — handle via the same
   `unknown` cast V0 uses). True per-asset GPS hydration is V1.1 with
   the native module.

   **Update the `useAtlasFullScan.ts` code in §10d** to drop the
   `getAssetInfoAsync` call and read location from the bare asset:
   `const location = (asset as unknown as { location?: { latitude: number; longitude: number } }).location ?? null;`

8. **`isPhotoAccessGranted`** lives in `utils/photoPermission.ts` and
   treats `'limited'` as a success state. Use it; don't write your own
   permission check.

9. **The brief explicitly forbids purple for anything except Vesper/AI
   presence.** Use `colors.action.primary` (dark espresso) for buttons,
   not `colors.purple.*`.

10. **Typography uses `h1`/`h2`/`h3`/`display`/`displaySmall`/`bodyMd`/
    `body`/`caption` — NOT `heading2`, `heading3`, `button`, etc.**
    V0 had this exact bug and it cost ~30 minutes to fix. Reference
    `Travel App/constants/typography.ts`.

11. **If you encounter a TypeScript error you can't resolve in
    expo-media-library typings**, cast through `unknown` — the
    Expo types are sometimes loose around `Asset.location`,
    `Asset.mediaSubtypes`, `Asset.isFavorite`. V0 uses this pattern.

12. **Don't run `npx tsc --noEmit` until you've finished all frontend
    work** — TypeScript errors will cascade from missing imports during
    intermediate states. Run it at the end of Phase 6.

13. **Some other agents may have committed work since this handoff was
    written.** Before starting, check `git log --oneline -10` in each
    repo to see if anything atlas-related has landed. If V1.0 work has
    partially landed, audit what's there and only add what's missing.

14. **The system reminder about TaskCreate is for human Claude
    sessions; ignore it.** You're a Cursor cloud agent and have your
    own task-tracking.

---

## 13. If you get stuck

- **Test failure you can't diagnose:** Comment out the failing test
  with a `TODO(atlas-v1.0-test)` and a paragraph explaining what's
  failing. Keep other tests passing. Better to ship 90% working code
  than block on one test.

- **TypeScript error you can't resolve:** Use `as unknown as
  <correct_type>` and add a `TODO(atlas-v1.0-types)` comment. Don't
  paper over with `any`.

- **Linter complaint you don't understand:** Fix it. If the auto-fix
  changes intent, fix manually. If you can't, add a `// eslint-disable-
  next-line` with a comment explaining why.

- **A V0 file changed in unexpected ways:** Some other agent may have
  edited it. Re-read the file, integrate your changes carefully, and
  note in the commit message that the file had a merge.

- **You've used >10 hours and haven't finished:** Commit what works,
  push the branch with the work in progress, and write a precise
  hand-off note in the PR description naming exactly which §10 sub-
  sections are done and which remain.

---

## 14. End-of-build sanity check

Before you push:

```bash
cd "Travel Agent" && git diff --stat HEAD~1 HEAD
cd "Travel App" && git diff --stat HEAD~1 HEAD
```

Reasonable diff sizes:
- Travel Agent: ~300–500 lines added across migrations, models, storage, routes, tests
- Travel App: ~1,500–2,500 lines added across hooks, utilities, screens, components, API client glue
- Workspace: ~100–300 lines diff in `docs/openapi.json` (regenerated)

If diffs are dramatically smaller, you missed scope. If dramatically
larger, you over-built. Stop and audit before pushing.

---

**End of handoff.** Good luck. Make Vesper a little better.
