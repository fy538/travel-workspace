# Dogfood Atlas — asset generation + substrate fill-in (handoff)

**Date:** 2026-07-04
**Purpose:** self-contained brief for a *separate* agent (e.g. GPT image generation in Codex) to make the **new Atlas** demo richly across most/all dogfood personas — not just `elif`. Assumes no prior context.

---

## Objective

Make the new Atlas surfaces (**taste boards, timeline, Unpacked year-recap, map, artifact reader, scan→candidate→approve flow**) demo richly for **several dogfood personas**. Today only `elif` is rich.

This is **two paired halves**:
1. **Generated image assets** — illustrations (riso/gouache) + photorealistic "fake photos".
2. **DB substrate** — affinity, artifacts, facets, almanac summaries via the dogfood seed manifests.

An artifact is only "real" when its **DB row AND its image files (with matching ids)** both exist. Do them together.

---

## Current per-persona state (verified in the live local DB, 2026-07-04)

| persona | board register | real Atlas artifacts | trip_photos | timeline | verdict |
|---|---|---|---|---|---|
| **elif** | `board` / `lineage` — "market lineage", 4 cities | 5 (2024 Lisbon; 2025 Rome/Tokyo/Istanbul/Brooklyn) | 32 | 16 | **DONE — reference example, do not touch** |
| mike | `board` but **monotone** (32× `cuisine=portuguese`, all weight 5.0) | 0 | 0 | 0 | needs everything |
| sarah | `board` thin (3 portuguese) | 0 | 0 | 0 | needs everything |
| mara | `empty` (2 saves; has 8 trips) | 0 | 3 | 3 | needs everything |
| dao | `empty` (4 saves) | 0 | 1 | 0 | needs everything |
| reza | `list` (2 — below board threshold) | 0 | 2 | 0 | needs everything |

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
Board visual slots today render as **deterministic riso-style SVG swatches synthesized in code** (`travel-app/components/atlas/risoManifest.ts` → `RisoSlotImage.tsx`). These are **temporary placeholders**, on-palette (Atlas gold + rust/olive/blue-green, never Discover violet), so a board reads as *imagery not a text list* without faking a photo. The real riso pool is deferred to *this* asset task.

**The swap seam is already wired:** `RisoSlotImage` calls `resolveSlotSvg`; if a real raster exists it returns null and falls through to `<AppImage>`. To swap in real assets (per `risoManifest.ts` header):
1. Drop assets into `travel-app/assets/atlas/riso/<dimension>/<value>.png` (+ one `<dimension>/_default.png` per dimension).
2. Build a static `require()` registry mapping keys → module ids (RN can't `require()` a dynamic path — must be an explicit object map).
3. In `resolveRisoAsset`, look up the registry FIRST; fall back to the generated swatch only when a key is missing. **Nothing in `AtlasTasteBoard` changes** — it already consumes `{ uri }`.

**Brand boundary:** Lane 1 must stay *abstract riso*, never photorealistic (`risoManifest.ts`: *"NOT photographs and must never be mistaken for one"*). Prompt GPT for **flat 2-color riso illustration** for Lane 1. Photorealistic GPT output goes in Lanes 2/3 only.

---

## Media pipeline rules (Lanes 2 & 3 — the `/dogfood-media/` path)

- **Files live at** `travel-agent/tools/dogfood/content/media/<manifest>/` with `atlas/` and `trips/` subfolders. Each is registered in that folder's `inventory.yaml` (`asset_id`, `status: staged`, `priority`, dimensions ~**1448×1086**, `dominant_color`, `surfaces`). Use the existing `lisbon-phase1/` and `elif-canonical/<city>/` folders as templates.
- **URL scheme:** DB stores `local://dogfood/<path>`; the app resolves it to `{API_URL}/dogfood-media/<path>` (`travel-app/utils/dogfoodMedia.ts`; served by `travel-agent/backend/api/dogfood_media.py`, ON locally, OFF on prod-like unless `DOGFOOD_MEDIA_STATIC_ALLOW_PROD_LIKE=true`).
- **HARD CONSTRAINT on photo ids:** must match the resolvable patterns `dogfood-<manifest>-<slug>` or `dogfood-<persona>-<city>-<slug>`. **Any other id renders blank on every phone except the one that scanned it** (`ph://`). Candidate `sample_photo_ids` have no fallback at all.
- **Do NOT:** put anything in `_review_archive/` (guard-rejected discard pile), use fake CDN URLs (`example.com`, `cdn.example`, …), or non-`local://dogfood/` local URLs. `travel-agent/tools/dogfood/content/schemas.py` validators reject all of these.

---

## Seed substrate — how DB rows get in

`travel-agent/tools/dogfood/content/` — manifests (`manifests/*.yaml`) + `seed.py`.

**Existing seed types to reuse:**
- `AtlasArtifactSeed` — `artifact_type`, `style`, `artifact_state: kept`, `generation_status: ready`, `title`, `one_line_read`, `sections`, `date_range_start/end`, `place_label`, `hero_photo_url`, `photo_ids`, `map_points` (**lat/lng required**), `signals`.
- `AffinitySeed` — `weight` (≥3.0 = "loved"), `entity`, `evidence`.
- `EntitySaveSeed`, `TripPhotoSeed` (`photo_id`, `cdn_url: local://dogfood/...`, gps, `dominant_color`).

**Likely need to create** (same pattern as recent seed types): an `AlmanacSummarySeed` → `atlas_almanac_summaries` (for Unpacked year-names, currently 0 rows for dogfood personas), and possibly a saved-board seed.

Validate: `PYTHONPATH=. python -m tools.dogfood.content.validate`. Apply: `PYTHONPATH=. python -m tools.dogfood.content.seed <manifest> --kind <k> --apply` (dry-run by default).

### The board-diversity lever (why mike is monotone)
The board composer (`travel-agent/backend/atlas/taste_board.py` + `story_shape.py`) joins `traveler_place_affinity` (weight≥3.0) to `entity_facets` on `(entity_type, entity_id)`. mike's board is flat because all 32 loved entities carry the **same** facet (`cuisine=portuguese`). A rich board needs the loved places to span **multiple facet dimensions** (occasion, experience_type, cuisine, neighborhood) across **≥2 cities**. Give each persona a distinct *taste identity* and pick loved entities whose `entity_facets` are varied (or seed the facets).

---

## What "rich" requires (thresholds — from `story_shape.py`)

- **Board register:** `_BOARD_MIN=3` loved places. `lineage` = ≥2 cities; `year` = ≥3 dated clustered; `mosaic` = ≥6 diverse; `hero` = a significance peak. Below 3 → honest `list`/`empty`.
- **Unpacked (year recap):** `available` if ≥1 `kept`+`ready` artifact dated in that year; **rich = 3-4 kept artifacts across ≥2 cities in one demo year**. Pick ONE demo year per persona (elif's is 2025).
- **Timeline / Map:** ~6-10 entries across ≥2 years; artifacts need `map_points` to appear on the map.
- **Almanac year-name:** one `atlas_almanac_summaries` row per (user, year).

---

## Per-persona deliverable (repeat for mike, sarah, + optionally mara/dao/reza)

1. A **coherent taste identity/theme** distinct from elif's "counters & markets across cities."
2. **~6-10 loved places** (`AffinitySeed` weight≥3.0) across ≥2 cities with **diverse facets** → non-monotone board.
3. **3-5 kept/ready Atlas artifacts** in one demo year across ≥2 cities → Unpacked + timeline + map.
4. **Assets per artifact:** 1 hero illustration (Lane 2) + 2-3 fake photos (Lane 3), named with the resolvable `dogfood-*` pattern, ~1448×1086, registered in `inventory.yaml`.
5. One **almanac summary** for the demo year (Lane: DB only).
6. **Shared, once:** the Lane-1 board riso pool (~113 facet-keyed abstract-riso images, app-bundled).

---

## Definition of done (per persona, verified against the live DB / composer)

- `compose_taste_board(uid)` → `register='board'`, `template ∈ {lineage, mosaic, year}`, a non-monotone title.
- `build_unpacked(uid, <year>)` → `available: True`, ≥3 artifacts across ≥2 cities.
- Every artifact `hero_photo_url` + section `photo_ids` resolve via `/dogfood-media/` (matching-pattern ids, files present in `inventory.yaml`).
- No `j11c` / eval-residue rows reintroduced.

## Scale estimate

Lane 1 ≈ **113** abstract-riso images (shared, one-time). Lanes 2/3 ≈ 5 artifacts × (1 hero + ~2 photos) × ~4 personas ≈ **50-60** images + inventory entries + the paired seed manifests.
