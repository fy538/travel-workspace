# Plan — Cross-Trip Threading UI

> **Outcome (as of 2026-07-03):** 🔲 Not started (UI) — agent-side cross-trip recall IS live (SKILL_CROSS_TRIP_THREADING); the trip-home 'from your Lisbon trip' surface remains unbuilt.

**Status:** approved scope, not started
**Goal:** A visible "from your Lisbon trip" surface on the trip-home, mirroring what the agent now does in conversation via SKILL_CROSS_TRIP_THREADING. Closes the moat-legibility loop on both sides.
**Estimate:** ~1 week focused (3 backend days, 3 frontend days, 1-2 iteration).
**Touches:** both repos (Travel Agent + Travel App).

---

## Why now

The agent-side moat narrative just landed via `SKILL_CROSS_TRIP_THREADING` (committed 651f730). The agent can now thread prior-trip patterns into conversation when it has trip-2+ familiarity. But the UI has no surface that says "I noticed this pattern across your trips." The result is asymmetric: in-chat reads of prior trips, no in-trip-home reads.

This plan closes that gap. After it ships, the moat narrative is felt on three surfaces — the Travel DNA card (P2), in-chat threading (P3 prompt-side), and the trip-home thread surface (this plan).

The data path already exists: `_get_prior_trip_summaries` in `backend/concierge/refresh_memory.py:518-569` already folds the last 3 completed trips' digests into Personal Memory at synthesis time. This plan adds a NEW endpoint + UI surface that surfaces those patterns explicitly (rather than relying on the synthesis-narrative integration).

---

## Locked decisions

1. **Mount point: trip-home middle zone.** Below the concierge attention card (which is the highest-priority slot), above `place_context`. Visible without crowding the attention card. If dogfood shows users miss it, promote.

2. **Up to 3 threads per trip.** Each ≤ 1 sentence + 1-2 chip-style references to specific prior trips. No threads → render nothing (no placeholder content).

3. **Backend storage: dedicated table.** `trip_cross_trip_threads` keyed by `trip_id`, with `threads JSONB` + `source_trip_count` + `computed_at`. Rationale: cross-trip threads need to be regenerated when ANY of the source trips' summaries update (e.g., post-trip digest lands), and that cascade is cleaner with a dedicated row.

4. **Compute trigger: on trip metadata change + on prior-trip completion.** When the current trip's destination / dates / occasion / budget changes via `patch_trip`, or when any of the user's other trips transitions to `status='completed'`, schedule a background recompute. Staleness gate: skip if `computed_at < 7 days old` AND `source_trip_count` unchanged.

5. **Per-user scope, not per-group.** When the trip has multiple members with different trip histories, threads are computed against the viewer's own history. The trip-home is per-user anyway (each member sees a personalized version); threading respects that. Group-level cross-trip surfaces (e.g. "the four of you have these patterns together") are out of scope for v1.

6. **Phrase generation: Haiku call at compute time, cached.** Same architectural pattern as P2's `reflection_phrases`. Single Haiku call given the current trip's context + last 3 prior-trip summaries returns a structured list of threads. No on-read LLM.

---

## Open questions

These don't block starting; surface them when they bite during implementation.

1. **Empty-state for new users (no prior trips).** Today the endpoint returns `[]` → UI renders nothing. Acceptable for v1. Consider later: a "Coming soon: I'll thread this trip into your next one" empty hint for trip 1.
2. **Stale-thread visibility.** If a thread references a prior trip the user later deletes, the chip becomes a dead link. v1 just hides chips whose target trip no longer exists. Better: invalidate-on-delete via FK or cron.
3. **Group trips with mixed histories.** Per the decision above, threads are per-user. But the trip-home is currently a shared surface — does each member see their own threads? Yes. Implementation note: scope the API call by `actor.id`, not by trip alone.
4. **Cache invalidation on prior-trip summary update.** When trip A's post-trip digest gets revised (user edits a Trip Story section), threads on trips B/C/D that reference A should regenerate. v1 implementation: trigger on any user-trip `trip_summary` JSONB update; conservative-and-correct.
5. **Performance.** Trip-home is loaded on every tab-into-trip. The endpoint serves cached threads (cheap DB read) — never a Haiku call on read. The Haiku call happens in background tasks on the trigger events.

---

## Architecture overview

```
                ┌────────────────────────────────────────┐
                │       trip-home page load              │
                │   (GET /api/trips/{id}/cross-...)       │
                └─────────────┬──────────────────────────┘
                              │ cached threads
                              ▼
                ┌────────────────────────────────────────┐
                │   trip_cross_trip_threads (per trip)   │
                │   threads JSONB, source_trip_count,    │
                │   computed_at                          │
                └─────────────┬──────────────────────────┘
                              │ regenerated on
                              ▼
   ┌──────────────────────────┴──────────────────────────┐
   │                                                     │
   │       Trigger 1: patch_trip changes meta             │
   │       Trigger 2: prior trip → status=completed       │
   │       Trigger 3: prior trip's trip_summary updated   │
   │                                                     │
   └──────────────────────────┬──────────────────────────┘
                              │ background task
                              ▼
                ┌────────────────────────────────────────┐
                │   compute_threads(trip_id, user_id):    │
                │   1. Load current trip context           │
                │   2. Load last 3 prior completed trips   │
                │   3. Haiku call → 0-3 structured threads │
                │   4. Persist to trip_cross_trip_threads  │
                └────────────────────────────────────────┘
```

---

## Phase 1 — Backend (3 days)

### Day 1 — Table + helpers

**Deliverable:** New table + CRUD helpers, no logic yet.

Files:
- `Travel Agent/alembic/versions/<new>_add_trip_cross_trip_threads.py` — single new table.
- `Travel Agent/backend/core/db/_tables/memory.py` — add `trip_cross_trip_threads` Table definition.
- `Travel Agent/backend/core/db/cross_trip_threads.py` — new module with `get_threads(trip_id)`, `set_threads(trip_id, threads, source_trip_count)`, `delete_threads(trip_id)` helpers.
- `Travel Agent/backend/core/models/trips.py` — add `CrossTripThread` Pydantic model: `{thread: str, prior_trip_ids: list[UUID]}`.

Schema:

```python
Table(
    "trip_cross_trip_threads",
    metadata,
    Column("trip_id", PG_UUID, ForeignKey("trips.id", ondelete="CASCADE"), primary_key=True),
    Column("threads", JSONB, nullable=False, server_default="[]"),
    Column("source_trip_count", Integer, nullable=False, server_default="0"),
    Column("computed_at", TZDateTime, nullable=False, server_default=func.now()),
)
```

Acceptance criteria:
- `alembic upgrade head` succeeds locally.
- Round-trip test: write a 2-thread blob, read it back, get the same shape.
- `cross_trip_threads.py` has 100% offline unit coverage (mock the connection).

### Day 2 — Compute pipeline

**Deliverable:** A function that, given a trip + user, returns 0-3 threads.

Files:
- `Travel Agent/backend/core/personalization/cross_trip_threading.py` — new module:
  - `compute_threads_for_trip(trip_id: UUID, user_id: UUID) -> list[CrossTripThread]`
  - Pulls current trip context (destination, occasion, dates).
  - Pulls last 3 completed trips for the user with their `trip_summary` digests (reuse the helper at `refresh_memory.py:518` — extract it if it's still private).
  - Builds a Haiku prompt: "Given the upcoming trip and these prior trips, extract 0-3 SHORT pattern-callbacks the concierge could naturally surface in conversation. Each callback references a specific prior trip. Patterns must span 2+ trips OR be a strong single-trip parallel. Return JSON: `[{thread, prior_trip_ids}]`. Empty list when no genuine pattern exists." (Final prompt text needs the SKILL_CROSS_TRIP_THREADING voice rules baked in — see references below.)
  - Calls `call_llm_json` with the `MEMORY_REFRESH` ModelRole or a new `THREAD_EXTRACTION` role (decide during implementation).
  - Validates response shape; drops malformed threads.
  - Returns the validated list.
- Inline tests in `tests/core/personalization/test_cross_trip_threading.py` — mock the LLM call, assert shape + filtering.

Prompt anchor: pull voice rules from `backend/concierge/_prompts_skills.py:SKILL_CROSS_TRIP_THREADING`. Same anti-performative + same "patterns must be real" framing. Reusing the existing skill text in the prompt header keeps the agent + this extractor speaking the same language.

Acceptance criteria:
- Mocked Haiku returns canned response → function returns parsed threads.
- Mocked Haiku returns malformed JSON → function returns `[]`, logs warning.
- Single completed-trip user → returns `[]` (need at least 2 prior trips for cross-trip patterns).
- Zero prior trips → returns `[]` (no Haiku call made — short-circuit).

### Day 3 — Endpoint + trigger wiring

**Deliverable:** A live endpoint + compute triggered from the right places.

Files:
- `Travel Agent/backend/api/routes/trips.py` (or wherever trip-scoped routes live — check `backend/api/routes/`) — add `GET /api/trips/{trip_id}/cross-trip-threads` returning `{threads: list[CrossTripThreadView]}` where `CrossTripThreadView = {thread, prior_trips: [{id, title}]}`. Hydrate trip titles from `trips` table at read time.
- `Travel Agent/backend/core/db/trips.py` — in `update_trip()` (already exists), after a successful update on relevant fields, schedule a background task: `asyncio.create_task(compute_and_persist_cross_trip_threads(trip_id, user_id))`.
- Same hook for trip status transitions to `completed` — find where that fires (likely `backend/core/db/trips.py:update_trip` already; the status-CHECK CHECK enforces values).
- Same hook for `trip_summary` updates (likely `backend/core/db/digests.py` or `backend/core/db/post_trip.py`).
- Migrations + table already done in Day 1.

Acceptance criteria:
- Endpoint returns `[]` for new users with no prior trips.
- Endpoint returns hydrated thread+title objects when threads exist.
- Background task runs on `patch_trip` change; verified by integration test (mock the Haiku call, check the table row gets written).
- Auth: gated on trip membership (same pattern as other trip-scoped endpoints).

---

## Phase 2 — Frontend (3 days)

### Day 4 — API client + data hook

**Deliverable:** Frontend types + a hook the component can consume.

Files:
- `Travel App/utils/api/types.ts` — add hand-written `CrossTripThread` interface mirroring backend `CrossTripThreadView`. (Or wait for the sync-types pass after restart and use generated.)
- `Travel App/utils/api/interface.ts` — add `getCrossTripThreads(tripId: string): Promise<CrossTripThread[]>`.
- `Travel App/utils/api/http.ts` — impl hitting the new endpoint.
- `Travel App/utils/api/mock.ts` — return a canned 2-thread mock.
- `Travel App/hooks/useCrossTripThreads.ts` — `useQuery` wrapper, `staleTime: 30s`, key `['cross-trip-threads', tripId]`.
- `Travel App/data/cross-trip-threads.ts` — wrapper that handles the mock/real toggle if needed (follow existing pattern in `data/`).

Acceptance criteria:
- Mock-mode users see threads in the hook return.
- Real-mode hits the endpoint, returns parsed data.
- `tsc --noEmit` clean.

### Day 5 — Component

**Deliverable:** `CrossTripThreadCard.tsx` — bulletted prose + chip references.

Files:
- `Travel App/components/trip-home/CrossTripThreadCard.tsx` — new file.
- Visual treatment: purple-accent card matching `TravelDNACard`'s palette so the moat-narrative surfaces visually rhyme.
- Renders nothing on empty array.
- Each thread: bullet + sentence + 1-2 tappable chips for prior-trip references.
- Chip tap → `router.push(routes.tripChat(prior_trip_id))` (or `routes.tripDetail` — decide based on what feels right).

Reference patterns:
- `Travel App/components/me/TravelDNACard.tsx` — bullet-list layout + purple accent + section label conventions.
- `Travel App/components/memory/DNAStrip.tsx` — chip styling for inline references.

Acceptance criteria:
- Story-style render with 0/1/2/3 threads.
- Per-row chip taps route correctly.
- Accessibility: each chip + each thread row has an `accessibilityLabel`.
- Visual review against TravelDNACard for consistency.

### Day 6 — Mount on trip-home

**Deliverable:** The card lives on the trip-home for real users.

Files:
- `Travel App/app/(tabs)/trips/[tripId]/index.tsx` (or whichever file is the trip-home — confirm with code grep) — mount the new card.
- Place after the concierge attention card, before `place_context` per locked decision (#1).

Acceptance criteria:
- Card appears in mock-mode trip-home with 2+ threads.
- Card hidden when threads is empty.
- No layout regression on the rest of the trip-home (scroll, spacing).

---

## Phase 3 — Iteration (1-2 days)

### Day 7 — Prompt tuning

The Haiku extractor's prompt is the most likely thing to need iteration. Plan for:

- Initial dogfood against 3-5 real users with trip-2+ histories.
- Catalog which threads feel good vs. performative.
- Tighten the prompt's "don't force connections" clause if dogfood shows reach.
- Consider adding example pairs (good thread vs. bad thread) to the prompt — only if the failure rate is high enough to justify the prompt growth.

### Day 8 (optional) — Edge cases

- Stale-chip behavior (prior trip deleted between compute + read).
- Internationalization of trip titles in chips.
- Cache-bust UX (a manual "refresh threads" affordance from the dispute card?).

---

## Out of scope

These are deliberately not in this plan; they'd inflate scope without proving the foundation:

- **Group-level "your group has these patterns" surface.** Per-user only for v1.
- **Cross-trip threading in the FOR-THIS-TRIP angle surface.** The Plan card is enough to validate the pattern; FTT integration is Phase 2.
- **In-chat reinforcement loop.** The agent's `SKILL_CROSS_TRIP_THREADING` already runs in conversation; this card is the visual mirror. Don't try to coordinate them automatically — let dogfood show whether they need it.
- **Auto-revoke threads on dispute.** If we add per-thread dispute (a la the Travel DNA card's `✕`), defer that to a separate plan. v1 is read-only.
- **Multi-language threading.** All threads in user's primary language; deferred to the broader i18n track.

---

## Success metrics

How do we know it landed:

1. **Coverage:** ≥ 70% of users with trip_count ≥ 2 see ≥ 1 thread on their trip-home within 24h of trip creation.
2. **Engagement:** Chip-tap-through rate ≥ 5% of card impressions (lower bar than typical recommendation cards — threading is more contemplative than action-oriented).
3. **Dogfood signal:** In a 5-user qualitative pass, ≥ 3 users describe the surface as "showing what Vesper knows about my patterns" vs. "guessing at random."
4. **Negative signal threshold:** ≤ 10% of threads disputed via per-thread X (if dispute UI lands later). Higher than that means the Haiku extractor is reaching too far.

---

## Files this plan touches (full list)

**Travel Agent:**
- `alembic/versions/<new>_add_trip_cross_trip_threads.py` (new)
- `backend/core/db/_tables/memory.py` (extend with new table)
- `backend/core/db/cross_trip_threads.py` (new)
- `backend/core/db/trips.py` (hook into update_trip)
- `backend/core/db/digests.py` or `post_trip.py` (hook into trip_summary update)
- `backend/core/models/trips.py` (new Pydantic models)
- `backend/core/personalization/cross_trip_threading.py` (new module — compute pipeline)
- `backend/api/routes/trips.py` (new endpoint)
- `tests/core/personalization/test_cross_trip_threading.py` (new)

**Travel App:**
- `utils/api/types.ts` (new type — or wait for sync-types)
- `utils/api/interface.ts` (new method)
- `utils/api/http.ts` (new impl)
- `utils/api/mock.ts` (new mock)
- `data/cross-trip-threads.ts` (new wrapper, optional)
- `hooks/useCrossTripThreads.ts` (new)
- `components/trip-home/CrossTripThreadCard.tsx` (new)
- `app/(tabs)/trips/[tripId]/index.tsx` (mount the card)

**Workspace:**
- `docs/openapi.json` (updated via sync-types after backend lands)

---

## Pre-flight check (run before Phase 2 Day 4)

Plan A's frontend phase regenerates `schema.gen.ts` from the live backend's OpenAPI. If the running backend was started before the recent P2/P3 commits, the regen pulls a stale schema and the frontend loses its typed view of `reflection_phrases`, the dispute endpoints, etc.

Verified on 2026-05-16 that the local backend was indeed stale — `/api/me/dna-phrases/dispute` + `/api/me/profile-fact/dispute` were missing from the live schema, `reflection_phrases` was absent from `UserMeResponse`. So you'll almost certainly need to restart before Day 4.

Run these four checks before starting Day 4:

```bash
# 1. Stop the current backend process (Ctrl-C in its terminal,
#    or kill the uvicorn PID).
#    Then restart on the latest commit:
cd "Travel Agent" && docker compose up -d
PYTHONPATH=. uvicorn backend.api.main:app --reload

# 2. Verify the P2/P3 endpoints are live:
curl -s http://localhost:8000/openapi.json \
  | grep -oE '/api/me/(dna-phrases|profile-fact)/dispute' | sort -u
#    Expected output: both paths printed.

# 3. Verify reflection_phrases is on UserMeResponse:
curl -s http://localhost:8000/openapi.json \
  | grep -c '"reflection_phrases"'
#    Expected output: ≥ 2 (one in the type def, one in the response example).

# 4. Run sync-types and confirm the generated file picks up the new fields:
cd "/Users/feihuyan/Documents/Claude/Travel Workspace" && ./scripts/sync-types.sh
grep -c 'reflection_phrases' "Travel App/utils/api/schema.gen.ts"
#    Expected output: ≥ 2.
```

If any check returns the wrong count, **do not start Day 4** — the regenerated `schema.gen.ts` will be missing fields and you'll spend longer debugging type errors than you save by pressing on. Diagnose first.

### Common diagnosis

| Failed check | What it means | Fix |
|---|---|---|
| 1 — uvicorn fails to start | Import error from recent backend commits | Check `pytest tests/concierge/ tests/core/ -q -m "not requires_postgres"` first; fix the import |
| 2 — both paths missing | Backend is on an old commit | `git log -1 --oneline` in `Travel Agent/` to confirm; rebase or pull |
| 2 — only one path missing | Partial commit landed | Check `git log --oneline` for the missing endpoint's commit |
| 3 — count is 0 or 1 | UserMeResponse Pydantic model is missing the field | Confirm `backend/core/models/users.py` has `reflection_phrases: list[str]` and the backend has been restarted since |
| 4 — count is 0 | sync-types ran against stale snapshot, OR ran but couldn't reach localhost:8000 | Re-run `./scripts/sync-types.sh` with `set -x` to see the curl call |

Pass all four checks → proceed to Day 4 with confidence.
