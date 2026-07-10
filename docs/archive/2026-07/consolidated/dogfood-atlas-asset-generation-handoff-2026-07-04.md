---
doc_type: archive
status: archived
archived: 2026-07-09
owner: founder / engineering
created: 2026-07-09
why_new: Preserve the complete source after its durable content was consolidated into an authoritative owner.
---

# Dogfood Atlas — asset generation + substrate fill-in (handoff)

> Archived 2026-07-09 after the repeatable seed/media workflow was consolidated into the Dogfood Runbook.

**Date:** 2026-07-04
**Purpose:** self-contained brief for a *separate* agent (e.g. GPT image generation in Codex) to make the **new Atlas** demo richly across several dogfood personas — not just `elif`. Assumes no prior context.

---

## Objective

Make the new Atlas surfaces (**taste boards, timeline, Unpacked year-recap, map, artifact reader, scan→candidate→approve flow**) demo richly for **several dogfood personas**. Today only `elif` is rich.

This is **two paired halves**:
1. **Generated image assets** — illustrations (riso/gouache) + photorealistic "fake photos".
2. **DB substrate** — affinity, artifacts, trip photos, and almanac summaries via the dogfood seed manifests; facets via the existing `entity_facets` projection or a new explicit facet-seed/projection step if the chosen places do not already project enough diversity.

An artifact is only "real" when its **DB row AND its image files (with matching ids)** both exist. Do them together.

Recommended scope: do this in phases, not as one giant asset dump.
1. **Phase 0 — unblock wiring:** add the missing DB seed support and photo/riso resolver support described below. **Implemented 2026-07-04.**
2. **Phase 1 — prove the pattern:** enrich `mike` + `sarah` end-to-end and verify all Atlas surfaces. **Implemented locally in `travel-agent/tools/dogfood/content/manifests/atlas-phase1.yaml`.**
3. **Phase 2 — broaden coverage:** add `mara`, `dao`, and `reza` if the first two personas validate cleanly.
4. **Lane 1 riso pool can be partial at first:** cover the facets actually emitted by Phase 1 before producing the full ~113-image pool.

### Implementation status

- Phase 0 wiring is in place:
  - `AlmanacSummarySeed` validates and seeds/resets `atlas_almanac_summaries` through `--kind almanac`.
  - `EntityFacetSeed` validates and seeds/resets `entity_facets` through `--kind facets`.
  - Lane-aware `dogfood-<manifest>-atlas-<slug>` and `dogfood-<manifest>-trips-<slug>` ids resolve to `/dogfood-media/<manifest>/<lane>/<slug>.jpg`.
  - The riso resolver now prefers bundled raster entries and falls back to generated SVG swatches when no PNG is registered.
- Phase 1 is applied locally:
  - Manifest: `travel-agent/tools/dogfood/content/manifests/atlas-phase1.yaml`.
  - Media inventory: `travel-agent/tools/dogfood/content/media/atlas-phase1/inventory.yaml`.
  - Current substrate: 5 kept Atlas artifacts, 6 trip photos, 19 media-inventory assets, 16 explicit facets, 9 affinity rows, 4 almanac summaries.
  - Primary hero images, supporting section photos, and artifact rendered-image illustrations now have generated/polished replacements at the stable inventory paths.
  - Lane 1 has bundled abstract riso PNGs registered for the Phase 1 category/cuisine/occasion facet pool, including `category/_default`.
- Phase 2 is applied locally:
  - Manifest: `travel-agent/tools/dogfood/content/manifests/atlas-phase2.yaml`.
  - Media inventory: `travel-agent/tools/dogfood/content/media/atlas-phase2/inventory.yaml`.
  - Current substrate: 9 kept Atlas artifacts, 18 media-inventory assets, 9 explicit facets, 9 affinity rows, 3 almanac summaries.
  - Lane 1 has bundled abstract riso PNGs for the Phase 2 emitted categories and facets: `hosted_table`, `flat_reset`, `built_route`, `courtyard`, `garden`, `museum`, `station`, `transit`, and `architecture`.
  - Lane 1 was broadened again on 2026-07-05 to the full first-pass target of 113 bundled rasters, adding common category/cuisine/occasion/experience-type keys such as `cafe`, `viewpoint`, `ramen`, `seafood`, `reunion`, `walkable_neighborhood`, `tile_route`, and `arrival_dinner`.
- Composer verification against the live local DB:
  - `mike`: `board/year`, selected chip `occasion=shared_table`, 3 moments / 3 visual slots, 2026 Unpacked available with year title "One table, then the city". Live DB currently has 3 kept/ready Mike artifacts in 2026: 2 from Phase 1 plus one existing Rome row.
  - `sarah`: `board/year`, selected chip `occasion=standing_counter`, 4 moments / 4 visual slots, 2026 Unpacked available with year title "Mornings as the control surface". Live DB currently has 3 kept/ready Sarah artifacts in 2026 from Phase 1, plus one older 2025 Rome artifact.
  - `mara`: `board/year`, selected chip `occasion=hosted_table`, 3 moments / 3 visual slots, 2026 Unpacked available with year title "The year the table hosted first".
  - `dao`: `board/year`, selected chip `experience_type=flat_reset`, 3 moments / 3 visual slots, 2026 Unpacked available with year title "A year of level first hours".
  - `reza`: `board/year`, selected chip `experience_type=built_route`, 3 moments / 3 visual slots, 2026 Unpacked available with year title "Routes made of tile and transit".
- Visual QA:
  - `atlas-home` captured successfully through the polish QA flow (`20260705T082639Z-atlas-home`); the flow now hides the floating nav for content-polish captures, and riso imagery was visible/nonblank.
  - `atlas-board` captured successfully through the polish QA flow (`20260705T082330Z-atlas-board`) with full screenshot plus read-panel and context-strip crops. The opened reading now uses the full editorial grid instead of the earlier narrow left-column composition.
- Media review:
  - Contact-sheet review on 2026-07-05 found the Phase 1/Phase 2 generated media coherent and nonblank, and the 113 Lane 1 rasters stayed abstract/riso rather than photorealistic.
- Scope note: this proves the manifest/media/resolver pattern for all current dogfood personas. Remaining work is ongoing review/sign-off and future refinements, not missing Mike/Sarah/Mara/Dao/Reza substrate.

### Fresh environment runbook

The assets are committed in `travel-agent` / `travel-app`, but the Atlas persona substrate still has to be seeded into each fresh DB. Run these from `travel-agent` against the target database:

```bash
PYTHONPATH=. python -m tools.dogfood.content.seed tools/dogfood/content/manifests/atlas-phase1.yaml --kind all --apply
PYTHONPATH=. python -m tools.dogfood.content.seed tools/dogfood/content/manifests/atlas-phase2.yaml --kind all --apply
```

For a brand-new local DB, start infra and migrate first:

```bash
docker compose up -d
PYTHONPATH=. alembic upgrade head
```

Verification status on 2026-07-05:
- Phase 1 dry-run plans `facets=16`, `affinity=9`, `atlas=5`, `almanac=4`, `photos=6`.
- Phase 2 dry-run plans `facets=9`, `affinity=9`, `atlas=9`, `almanac=3`, `photos=0`.
- Live `--apply` could not be re-run in this shell because local Postgres was not listening on `localhost:5432` and the Docker daemon was stopped. The commands above are the required fresh-env step once DB infra is up.

### Concrete follow-ups / sign-off

This remains a good idea if it stays disciplined: each future batch must keep DB substrate, manifest ids, inventory rows, and media files landing together. Do not accept a media-only or DB-only batch as "done."

Before sign-off or promotion to another environment:
1. Re-run both Atlas seed dry-runs, then apply both manifests against the target DB.
2. Re-run manifest/media inventory validation for `atlas-phase1` and `atlas-phase2`; accept only zero missing files, zero unreferenced inventory assets, and zero bad `manifest_targets`.
3. Re-run the persona hookup report; accept only zero `missing_inventory`, zero `bad_files`, and zero unused inventory ids for each phase.
4. Review the latest contact sheet and visual QA captures, including `atlas-home` and `atlas-board`; replace any weak asset through the manifest/inventory path, not ad hoc filenames.
5. If adding another persona or asset tranche, keep it small enough to review in one contact sheet and require the same live composer checks (`compose_taste_board` and `build_unpacked`) before merge.

---

## Current per-persona state (latest local verification)

| persona | board register | real Atlas artifacts | trip_photos | timeline | verdict |
|---|---|---|---|---|---|
| **elif** | `board` / `lineage` — "market lineage", 4 cities | 5 (2024 Lisbon; 2025 Rome/Tokyo/Istanbul/Brooklyn) | 32 | 16 | **DONE — reference example, do not touch** |
| mike | `board/year` — `occasion=shared_table` | 3 in 2026 (2 Phase 1 + 1 existing Rome) | 3 Phase 1 | verified through Atlas/Unpacked composer | **Phase 1 DONE** |
| sarah | `board/year` — `occasion=standing_counter` | 3 in 2026 Phase 1 (+1 older 2025 Rome) | 3 Phase 1 | verified through Atlas/Unpacked composer | **Phase 1 DONE** |
| mara | `board/year` — `occasion=hosted_table` | 3 in 2026 Phase 2 (+ existing Lisbon context) | media via atlas-phase2 artifacts | verified through Atlas/Unpacked composer | **Phase 2 DONE** |
| dao | `board/year` — `experience_type=flat_reset` | 3 in 2026 Phase 2 (+ existing Lisbon context) | media via atlas-phase2 artifacts | verified through Atlas/Unpacked composer | **Phase 2 DONE** |
| reza | `board/year` — `experience_type=built_route` | 3 in 2026 Phase 2 (+ existing Lisbon context) | media via atlas-phase2 artifacts | verified through Atlas/Unpacked composer | **Phase 2 DONE** |

`elif` is the "rich, done right" template — **mirror her shape.** Do **not** reintroduce `j11c-*` / "Days in Tokyo" artifacts (that was eval residue; purged 2026-07-04, and the J11 cert teardown was fixed so it won't recur).

---

## THE THREE ASSET LANES (read this before generating anything)

These are wired **differently** — do not conflate them.

| Lane | What | Keyed by | Delivery mechanism | Style rule |
|---|---|---|---|---|
| **1. Board riso pool** | the swatch replacements (~65 category + ~48 per-place ≈ **113**) | **facet** (`cuisine/pizza.png`, `category/viewpoint.png`) — **shared across all personas** | **app bundle** `travel-app/assets/atlas/riso/<dimension>/<value>.png` via a static `require()` registry | **flat abstract riso — MUST NOT look like a photograph** |
| **2. Artifact illustrations** | per-artifact `hero_photo_url` / `rendered_image_url` | per artifact | `/dogfood-media/` URL + DB row | riso or gouache painterly |
| **3. Trip / section photos** | the "fake photos" (`trip_photos`, artifact section `photo_ids`) | per persona / trip | `/dogfood-media/` URL + DB row | **photorealistic** (may include people) |

### Why Lane 1 exists (the SVG question)
Board visual slots today render as **deterministic riso-style SVG swatches synthesized in code** (`travel-app/components/atlas/risoManifest.ts` → `RisoSlotImage.tsx`). These are **temporary placeholders**, on-palette (Atlas gold + rust/olive/blue-green, never Discover violet), so a board reads as *imagery not a text list* without faking a photo. The generated placeholders now paint through `react-native-svg`'s `<SvgXml>` path, not through raster `<Image>`.

The real riso pool is now partially wired and expanded through Phase 2 plus a common shared tranche. Current behavior:
- `RisoSlotImage` calls `resolveSlotSvg(slot)` first.
- For `source: "riso"`, `resolveSlotSvg` returns `null` when the static registry has a bundled raster for that key, so the renderer falls through to `<AppImage>`.
- When no bundled raster exists, the resolver returns generated SVG XML and keeps the no-empty-slot guarantee.

To expand real bundled riso assets safely:
1. Drop assets into `travel-app/assets/atlas/riso/<dimension>/<value>.png` (+ one `<dimension>/_default.png` per dimension when the pool is broader).
2. Add each asset to the static `require()` registry in `travel-app/components/atlas/risoManifest.ts` (RN can't `require()` a dynamic path — must be an explicit object map).
3. Keep `AtlasTasteBoard` unchanged. The renderer should still consume `visual_slots`; only the asset resolver/rendering seam changes.

**Brand boundary:** Lane 1 must stay *abstract riso*, never photorealistic (`risoManifest.ts`: *"NOT photographs and must never be mistaken for one"*). Prompt GPT for **flat 2-color riso illustration** for Lane 1. Photorealistic GPT output goes in Lanes 2/3 only.

---

## Media pipeline rules (Lanes 2 & 3 — the `/dogfood-media/` path)

- **Files live at** `travel-agent/tools/dogfood/content/media/<manifest>/` with `atlas/` and `trips/` subfolders. Each is registered in that folder's `inventory.yaml` (`asset_id`, `status: staged`, `priority`, dimensions ~**1448×1086**, `dominant_color`, `surfaces`). Use the existing `lisbon-phase1/` and `elif-canonical/<city>/` folders as templates.
- **URL scheme:** DB stores `local://dogfood/<path>`; the app resolves it to `{API_URL}/dogfood-media/<path>` (`travel-app/utils/dogfoodMedia.ts`; served by `travel-agent/backend/api/dogfood_media.py`, ON locally, OFF on prod-like unless `DOGFOOD_MEDIA_STATIC_ALLOW_PROD_LIKE=true`).
- **HARD CONSTRAINT on photo ids:** artifact section photos currently resolve through `travel-app/utils/dogfoodMedia.ts` and then fall back to `ph://<photo_id>`. Use the explicit lane-aware patterns `dogfood-<manifest>-atlas-<slug>` and `dogfood-<manifest>-trips-<slug>` for new media; these map to `/dogfood-media/<manifest>/atlas/<slug>.jpg` and `/dogfood-media/<manifest>/trips/<slug>.jpg`. Existing special cases still support `dogfood-lisbon-phase1-*` and `dogfood-elif-(rome|tokyo|istanbul|brooklyn)-*`.

  Any id outside the supported patterns may render blank on phones that do not have the corresponding local `ph://` asset. Candidate `sample_photo_ids` have no fallback at all.
- **Do NOT:** put anything in `_review_archive/` (guard-rejected discard pile), use fake CDN URLs (`example.com`, `cdn.example`, …), or non-`local://dogfood/` local URLs. `travel-agent/tools/dogfood/content/schemas.py` validators reject all of these.

---

## Seed substrate — how DB rows get in

`travel-agent/tools/dogfood/content/` — manifests (`manifests/*.yaml`) + `seed.py`.

**Existing seed types to reuse:**
- `AtlasArtifactSeed` — `artifact_type`, `style`, `artifact_state: kept`, `generation_status: ready`, `title`, `one_line_read`, `sections`, `date_range_start/end`, `place_label`, `hero_photo_url`, `photo_ids`, `map_points` (**lat/lng required**), `signals`.
- `AffinitySeed` — `weight` (≥3.0 = "loved"), `entity`, `evidence`.
- `EntitySaveSeed`, `TripPhotoSeed` (`photo_id`, `cdn_url: local://dogfood/...`, gps, `dominant_color`).

**Implemented:** `AlmanacSummarySeed` → `atlas_almanac_summaries` supports Unpacked year/month names, with dry-run/apply/reset in `seed.py` under `--kind almanac`.

**Implemented:** `EntityFacetSeed` → `entity_facets` supports explicit catalog facet enrichment, with dry-run/apply/reset in `seed.py` under `--kind facets`.

**Possible implementation gap:** a saved-board seed may be useful if the demo needs persisted saved boards. Do not add it unless a target surface actually reads persisted saved-board rows; the core taste board can be produced from affinity + facets.

Validate: `PYTHONPATH=. python -m tools.dogfood.content.validate`. Apply: `PYTHONPATH=. python -m tools.dogfood.content.seed <manifest> --kind <k> --apply` (dry-run by default).

### The board-diversity lever
The board composer (`travel-agent/backend/atlas/taste_board.py` + `story_shape.py`) joins `traveler_place_affinity` (weight≥3.0) to `entity_facets` on `(entity_type, entity_id)`. The Phase 1 fix lets the lean-back board selector choose the strongest loved facet across dimensions, not just `cuisine`. A rich board still needs loved places to span **multiple facet dimensions** (occasion, experience_type, cuisine, neighborhood) across **>=2 cities**. Give each persona a distinct *taste identity* and pick loved entities whose `entity_facets` are already varied. If the catalog projection cannot supply that, use `EntityFacetSeed` in the manifest for deliberate facet coverage.

---

## What "rich" requires (thresholds — from `story_shape.py`)

- **Board register:** `_BOARD_MIN=3` loved places. Below 3 → honest `list`/`empty`.
  - `lineage` requires ≥2 cities **and** category coherence (currently `_LINEAGE_MIN_COHERENCE=0.6`), not just city spread.
  - `year` requires ≥3 dated moments with bounded span/clustering (currently `_YEAR_MIN_DATED=3`, `_YEAR_MAX_SPAN_DAYS=550`, `_YEAR_MIN_CLUSTERING=0.55`).
  - `mosaic` requires ≥6 moments and high city diversity (currently at least half the moments in distinct cities).
  - `single`/hero wins when one moment is a real significance peak; avoid accidental outlier weights if the target is lineage/mosaic/year.
- **Unpacked (year recap):** `available` if ≥1 `kept`+`ready` artifact dated in that year; **rich = 3-4 kept artifacts across ≥2 cities in one demo year**. Pick ONE demo year per persona (elif's is 2025).
- **Timeline / Map:** ~6-10 entries across ≥2 years; artifacts need `map_points` to appear on the map.
- **Almanac year-name:** one `atlas_almanac_summaries` row per (user, year).

---

## Per-persona deliverable (Phase 1: mike + sarah; Phase 2: optionally mara/dao/reza)

1. A **coherent taste identity/theme** distinct from elif's "counters & markets across cities."
2. **~6-10 loved places** (`AffinitySeed` weight≥3.0) across ≥2 cities with **diverse facets** → non-monotone board.
3. **3-5 kept/ready Atlas artifacts** in one demo year across ≥2 cities → Unpacked + timeline + map.
4. **Assets per artifact:** 1 hero illustration (Lane 2) + 2-3 fake photos (Lane 3), named with the resolvable `dogfood-*` pattern, ~1448×1086, registered in `inventory.yaml`.
5. One **almanac summary** for the demo year (Lane: DB only).
6. **Shared, once:** the Lane-1 board riso pool. Start with the Phase 1 emitted facets; expand toward the full ~113 facet-keyed abstract-riso images after resolver wiring is proven.

---

## Definition of done (per persona, verified against the live DB / composer)

- Wiring prerequisites are done once:
  - generated riso SVGs still render, but bundled riso PNGs win when present;
  - new lane-aware dogfood `photo_id` patterns resolve to `/dogfood-media/` instead of falling through to `ph://`;
  - `AlmanacSummarySeed` can validate, seed, reset, and dry-run/apply via `tools.dogfood.content.seed`.
- `compose_taste_board(uid)` → `register='board'`, `template ∈ {lineage, mosaic, year}`, a non-monotone title.
- `build_unpacked(uid, <year>)` → `available: True`, ≥3 artifacts across ≥2 cities.
- Every artifact `hero_photo_url` + section `photo_ids` resolve via `/dogfood-media/` (matching-pattern ids, files present in `inventory.yaml`).
- No `j11c` / eval-residue rows reintroduced.

## Scale estimate

Full target: Lane 1 ≈ **113** abstract-riso images (shared, one-time). Lanes 2/3 ≈ 5 artifacts × (1 hero + ~2 photos) × ~4 personas ≈ **50-60** images + inventory entries + the paired seed manifests.

Recommended next slice: merge the current phased substrate/media/app work, then handle any future dogfood refinements as small reviewed batches. This remains a good idea only if it stays phased: DB substrate, media files, inventory rows, and live composer verification should land together each time.
