# Discover cruft cleanup — 2026-07-08

> Status: done
> Owner: founder / engineering
> Context: prompted by a design-alignment review of Discover against the
> `vesper 122` handoff bundle. Discover has churned through ~6 design eras in
> ~10 weeks (feed → blended feed → Reading Room → place-first/Compose board →
> spatial map → Universal Search); this pass removes the tailings, it does not
> redesign anything. The map's scope/layer sheet gap and the dormant
> `place_angles` generation backlog were both explicitly deferred, not touched
> — see conversation notes.

## What shipped

**Frontend (`travel-app`):**
- Deleted `components/discover/TodaysRead.tsx` + its smoke test — superseded by
  the hero rendered inline in `DiscoverCoverHome.tsx`; zero live importers.
- Removed the `quickPicks` field end-to-end (`data/discover.ts`,
  `utils/queryKeys.ts`, both call sites in `discover/index.tsx` and
  `trips/index.tsx`, and the two test files that referenced it). It was a full
  query (`api.search`-backed) that every real caller permanently disabled —
  self-documented in code as belonging to the retired in-Discover search
  overlay, superseded by Universal Search on 2026-07-01.
- Confirmed `DiscoverSearchOverlay` no longer exists in the tree (already
  removed before this pass — no action needed).

**Backend (`travel-agent`):**
- Fixed a stale docstring in `backend/composition/core.py::_copy_deadline_s`
  that still named `GET /discover/compose` as a live caller; that route was
  retired 2026-07-03. Only `GET /api/atlas/board` calls this path now.
- Left `backend/atlas/discovery_reflection.py`'s historical note about the
  retired `compose_board.py` as-is — it already correctly describes it in the
  past tense; it was not actually stale.

**Docs (`docs/systems/discover.md`):**
- Removed the charter's references to `POST /api/discover/compose` and
  `compose_board.py` as live Discover interfaces (retired 2026-07-03); pointed
  to Universal Search as the current owner of in-Discover search.
- Fixed a dead component reference (`ReadingRoomLayout.tsx` → the real
  component is `DiscoverCoverHome.tsx`).
- Rewrote the "No false peak" invariant, which described the retired board's
  md5-ordering/synthetic-band score lifecycle (no longer present anywhere in
  the codebase) — replaced with the feed's actual mechanism, `_select_lead_read`
  picking the highest real `quality_score` dossier.

## Explicitly NOT touched (flagged, not cleaned)

- **`GET /api/discover/trending` + `POST /api/admin/discover/trending`** — has
  zero live FE consumers, but is backed by a real seed script
  (`scripts/seed_trending.py`) and is commented as a deliberate "public
  marketing surface" build-ahead. This is a product decision (wire it up or
  formally kill it), not code cruft — left alone.
- **`DOSSIER_VOICE_STUB`** ("Hear this read" button, `onPress={() => {}}`) —
  already correctly gated off (`DOSSIER_VOICE_STUB = false`), consistent with
  the MVP manifest's "flag off the OUT set, delete nothing" posture for voice.
  No action needed.
- **The `place_angles` generation backlog** (~2,132 rows with
  `dossier_id IS NULL`) — this is the research pipeline's job queue, not
  Discover UI cruft. The Era-1 angles-*browse* UI is correctly gone; the
  angles *substrate* is live infrastructure feeding dossier generation, For
  You, Takes, and geofence search. Left untouched; running the backlog is a
  ~$300 corpus-expansion spend decision, deferred until cohort-1 usage shows
  which cities need it.
- **Discover map's Scope + Layer sheet** (`app/(tabs)/discover/map.tsx:170`) —
  canon-122 specs a layer taxonomy; the code deliberately left the control
  empty because there's no honest server-side category filter to put behind
  it yet. Recommendation stands: don't build up to the canon here, or simplify
  the canon down to city/near-me — founder call, not made in this pass.

## Verification

- `npx tsc --noEmit` — clean, zero errors.
- `npx jest __tests__/data/discover.test.ts __tests__/screens/discover.smoke.test.tsx`
  — 32/32 passing.
- `python3 -c "import ast; ast.parse(...)"` on the edited backend file — syntax OK.
