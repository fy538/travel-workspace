# Code Alignment — Atlas Phase 2b + 2c: Build Long View, Retire Map Tile (2026-07-05)

You are working in `~/travel-workspace/travel-app` (React Native / Expo, expo-router). Backend `~/travel-workspace/travel-agent` may gain ONE small read endpoint/extension (Task B) — nothing else backend-side.

## Context

The Atlas design canon (bundle: `~/Downloads/atlas-memory-composition-vision 23`, Canonical Experience Board, "Long View — the unfiltered Atlas (Phase 2, 2026-07-05)" section + Phase 2 rulings in §13) established Long View: the whole-corpus browse surface. Doctrine: "the unfiltered Atlas — browse without asking… year chapters, city nodes, memory counts. Not a search. Not the featured reading. An atlas index."

The canon rulings you are implementing (these are settled — do not re-litigate):
1. **One time-browsing surface, not three**: Long View's Time mode absorbs Almanac's year-chapter structure; the flat Timeline list is retired as redundant.
2. **Index register, not Reading register**: title + count + dimension switcher + drill-down rows. No kicker, no Vesper voice line, no "Vesper made this," no thesis sentence.
3. **v1 ships Time + Places only**; the switcher shows all four tabs (Time · Places · People · Theme) with People/Theme visibly inactive.
4. **Naming**: the kept-views fallback label "Kept view · The whole Atlas" renames to "Kept view · No filters" (it collides with this screen's name).
5. **Places mode unblocks Map's retirement** (Phase 2c below, gated on 2b working).

Two decisions the design session did not push into the Implementation Spec — they are decided HERE, cite this brief:
- **Route**: `app/atlas/long-view.tsx` (`/atlas/long-view`), with `?mode=time|places` param support so retired screens can redirect into a specific mode.
- **Mechanical framing, with a substrate correction**: the canon says "Long View IS the composition engine's arrangement machinery with an empty query." Honor that on the FRONTEND (reuse the arrangement components' visual language — the Places node treatment, provenance glyphs, plate primitives). But do NOT wire the backend composition engine to serve this: the engine composes taste atoms (place affinity), while Long View indexes MEMORIES. The correct data source is the existing timeline projection (`atlas_timeline_entries`, already a persisted projection over trips + candidates + artifacts). Long View = that projection, aggregated two ways (by year, by city). Do not build a parallel memory pipeline and do not touch the taste engine — this is an aggregation over an existing table.

## PHASE 2B

### Task A — The Long View screen

`app/atlas/long-view.tsx`:
- **Shell**: index register per ruling 2. Title (per canon: "The whole Atlas" register), overall memory count, dimension switcher with 4 tabs, People/Theme rendered visibly inactive (disabled state, no navigation — the canon deliberately shows the feature's future shape).
- **Time mode** (default): year chapters (year → memory count), drilling into that year's moments. Reuse `AtlasTimelineEntryRow` for the drill-down rows so the existing per-entry management (hide/restore/pin via `AtlasTimelineEntryMenu`) survives the Timeline retirement — that capability must not be lost. `removed.tsx` stays untouched as the hidden-entries surface.
- **Places mode**: city nodes with whole-corpus counts (canon example: "TOKYO · 6", "LISBON · 9"), consistent with the provenance-glyph and node treatment already used by the composed-reading Places arrangement. Tapping a city drills into that city's moments (same row component).
- Loading/empty/error via the app's standard state components. A brand-new user with zero memories should get an honest quiet state, not fake chapters.

### Task B — Data

Serve Time/Places aggregation from the timeline projection. Preferred: extend the existing timeline read path (e.g. `GET /api/atlas/timeline` gains a `group_by=year|city` + counts summary, or one new small read endpoint beside it in `atlas.py`) — whichever is least invasive given the existing pagination code. No schema changes, no new tables, no engine changes. If the existing endpoints already return enough to aggregate client-side at realistic corpus sizes, client-side aggregation is acceptable — note the choice and why in your report.

### Task C — Retire `timeline.tsx` and `almanac.tsx` into redirects

- `app/atlas/timeline.tsx` → redirect to `/atlas/long-view?mode=time` (preserve any incoming params sensibly). Same for `app/atlas/almanac.tsx`.
- Update `AtlasTimeNavFooter` (cross-links Almanac ↔ Timeline ↔ Removed): it now links Long View ↔ Removed only (or retire the footer if it no longer earns its place — your call, note it).
- Reroute all `routes.atlasTimeline()` / `routes.atlasAlmanac()` call sites to the Long View route with the right mode; update `utils/routes.ts` accordingly (keep or alias the old route helpers as deprecated wrappers if churn is large — but no NEW usages).
- Backend: `almanac_generator.py` + `atlas_almanac_summaries` and the almanac endpoint lose their FE consumer. FLAG as orphaned in your report — do not delete backend code in this batch.

### Task D — Home entry strip

The code home (`app/(tabs)/atlas/index.tsx`) has NO Long View entry today (the canon's "Since 2023 · The whole Atlas →" quiet strip exists only in design). Add it per canon placement: a quiet strip below the composition object area (near where the inbox nudge sits), mono eyebrow ("SINCE {first-memory-year}") + serif line ("The whole Atlas →"), routing to `/atlas/long-view`. Quiet — this is a doorway, never a hero.

### Task E — The naming rename

`app/atlas/boards.tsx` `savedAskLine()` fallback: `'Kept view · The whole Atlas'` → `'Kept view · No filters'` (canon ruling 4). Check for the same string in mocks/tests.

## PHASE 2C — gated on 2b

**Gate: proceed only if Task A's Places mode renders real whole-corpus data correctly (verify against a populated dev persona, e.g. via the persona switcher). If the gate fails, stop here and report — do not retire Map against a broken replacement.**

### Task F — Retire the Map room

- `app/atlas/map.tsx` → redirect to `/atlas/long-view?mode=places`.
- Reroute all `routes.atlasMap()` call sites — there are ~10: `app/(tabs)/atlas/index.tsx` (the shelf tile, see Task G), `app/atlas/search.tsx` (×3, including the `open_map` review action), `app/atlas/inbox.tsx`, `components/atlas/AtlasTripState.tsx` (ThinRoom "Map"), `components/atlas/AtlasTasteBoard.tsx`, `components/atlas/AtlasStartingPoints.tsx` (×2). Point them at Long View places mode; relabel where the label says "Map" and an index framing fits better ("Your places" / keep "Map" where it reads naturally — judgment, note choices).
- Backend: `GET /api/atlas/map` + `map_compose.py` lose their FE consumer — FLAG as orphaned, do not delete.
- `/your-map` (the cross-trip map at `app/your-map.tsx`) is a DIFFERENT surface and is OUT OF SCOPE — do not touch it.

### Task G — Remove the shelf container

With Map's tile gone the shelf has zero always-on tiles (Postcards is flag-dark). Remove the shelf section from `app/(tabs)/atlas/index.tsx` (both render sites — "THE SHELF" / "PRIVATE ARCHIVE" headers, the `AtlasShelfRoomCard` usages, and the postcards skeleton block). Leave `app/atlas/postcards.tsx` and its route registration intact (dark); leave a short code comment noting that when `POSTCARDS_ENABLED` lights up, postcards re-enters via a Moment Action / artifact affordance, not a shelf tile (per the shelf-retirement decision trail). If `AtlasShelfRoomCard` has no remaining consumers, delete it from `AtlasV3Primitives.tsx`.

## Process

- `git status` first (concurrent-session WIP hazard); work on a branch from main; one commit per task; do NOT push without user approval.
- After each task: `tsc`, run the test suite, update tests that referenced retired routes/tiles (convert to redirect assertions or Long View assertions — strengthen, don't delete); grep for dangling references (`atlasTimeline`, `atlasAlmanac`, `atlasMap`, `The whole Atlas` old label, `THE SHELF`) — zero unexplained hits before each commit.
- Update any FEATURE.md/docs touched by route retirement in the same commits (pre-push doc-sync guards).
- OUT of scope: the taste/composition engine, `signal_memory`, the true moment-store migration, `your-map`, `removed.tsx`, backend deletions (flag only), People/Theme modes (inactive tabs only).

## Definition of done

Long View live at `/atlas/long-view` with Time (default) + Places modes over the timeline projection, 4-tab switcher with 2 inactive, index register (no Vesper voice) · timeline/almanac/map are redirects with zero dangling nav references · entry management survives via reused row components · home has the quiet entry strip · boards fallback renamed · shelf container removed, postcards route preserved dark · green tsc + tests · report: data-path choice (B), footer decision (C), relabel choices (F), orphaned-backend flag list, and the 2c gate evidence (populated-persona Places screenshot or equivalent).
