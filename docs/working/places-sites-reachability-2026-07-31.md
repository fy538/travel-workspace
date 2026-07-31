# A1 — make `sites` reachable from the Places root

**Status:** plan only, nothing built. Written 2026-07-31.
**Why it exists:** the Places tab cannot display a museum, monument or landmark
in any city. Not "rarely does" — structurally cannot. This traces why and what
it would take to fix.

**Relationship to the §14 ruling:** independent of it. Whether Places stays one
stream (canon §1/§2) or becomes a sectioned browse (proposed §14, not ruled),
the tab needs to be able to return a museum. Until it can, both layouts are
being judged on a list that is restaurants-and-bars by construction — which is
the main reason the §14 adjudication is currently on hold.

---

## The gap, verified

Root path:

| Step | File |
|---|---|
| route | `backend/api/routes/places.py:35` |
| composer | `backend/places/projection.py:30` — `build_places_projection` |
| ranker | `backend/places/taste.py:157` — `discover_nearby_ranked` |
| discovery | `backend/places/discovery.py:52` — `discover_nearby` |
| **the SQL** | **`backend/core/db/entities.py:1017` — `get_nearby_venues_simple`** |

That query reads `venues` only: `ST_DWithin` on geometry, `verification_status
== "verified"`, ordered by distance, limited. `grep -rn "site" backend/places/`
returns **zero matches across all 21 files** — no join, no union, no separate
fetch, no post-merge.

Culture lives in `sites` (`backend/core/db/_tables/venues.py:208-267`). Fixture
distribution makes the split plain: `sites.yaml` holds 33 museums against
`venues.yaml`'s 1, and `venue_type='cultural'` is 9 rows out of ~549.

The gap reads as an omission, not a decision — there is no comment, test or doc
anywhere in `backend/places/` acknowledging that `sites` is excluded.

**Prior art, in the same repo:** `backend/core/db/search.py:702` `search_nearby`
already unions venues + sites + accommodations, and its docstring at `:718-727`
documents the union-limit starvation hazard described below. Also
`backend/planning_agent/db_provider.py:478` searches both tables; its comment at
`:534-541` describes this exact bug class being fixed there. Any new function
must cite `search_nearby` so two nearby-union implementations don't diverge.

---

## The three things that make this bigger than a union

### 1. ID collision — the truth bug

Site ids and venue ids are independent sequences that overlap.
`projection.py:74` gathers `canonical_venue_ids` from **any** int `row["id"]`,
and `:84-87` feeds those ints into `get_cached_venue_statuses`, `in_trip_ids`
and `loved_ids`.

A site with `id=42` inherits venue 42's open-now hours, "in trip" marker and
"loved" marker. Shipped, that means **a museum labeled as loved by a friend who
has never heard of it.**

Second instance of the same bug: `taste.py:217-218` does `venue_int_id in
saved`, where `saved` is venue-only (`_fetch_saved`, `:263`). A colliding site
gets `+12.0` (`_SAVED_BONUS`), `taste_signal="saved"`, and
`relationship.saved = true` in the payload (`projection.py:163`) — a fabricated
personal signal driving a fabricated ranking boost.

This is the failure mode §11 ("what is backed, and what writes back") and the
marker-provenance discipline exist to prevent. Any implementation must gate
every one of these lookups on `entity_type == "venue"`.

### 2. The candidate cap, not the floor, is the bottleneck

`taste.py:165` caps the candidate pool at 8. In a dense restaurant radius the
nearest 8 verified rows are all venues, so no site is ever scored — a union
plus a floor fix surfaces nothing.

Needs a reserved site quota in the merge. **The constant cannot be chosen from
the code** — it depends on the venue:site ratio inside a typical radius, which
requires measuring the real corpus.

The ranking floor itself (`taste.py:231-232`) turns out to be the easy half:
tag site rows `source = "corpus"` (they pass the same `verified` gate — they
*are* corpus) and carry the distinction in a new `entity_type` field. The floor
predicate then needs no change, live-provider rows stay floored, and
`concierge_home.py:89-90`'s corpus telemetry stays meaningful.

### 3. Sites are not tappable, and would render photoless

- No `GET /api/sites/{id}` (only `backend/api/routes/venues.py:62`), no
  `travel-app/app/site/` screen, and `routes.ts:585` types `venueId: number`.
  `PlacesCore.tsx:231` gates on `canonical_venue_id != null`, so sites render
  disabled. `get_site` exists at `entities.py:812`, so the endpoint is cheap —
  but whether it blocks phase 1 is a product call.
- **Pre-existing bug:** `projection.py:200` `_first_photo_url` accepts only a
  `list`, but `photo_urls` is JSONB in two other shapes
  (`backend/core/models/photos.py:153-197`). `tests/places/test_projection.py:103`
  feeds a synthetic list, so the test passes green while real corpus rows yield
  `photo_url=None`. Sites inherit the identical column shape. Route through
  `extract_photo_url` (`photos.py:181`).
- **Save would write garbage:** `PlacesCore.tsx:222` sends
  `entityType: 'venue'` with id `'site:12'`; `backend/api/routes/saves.py:46`
  only parses provider ids for venues, so it falls through and writes a bad
  `entity_saves` row plus bad user events (`saves.py:82-99`).

---

## Shape of the change

Ordered by dependency. Full detail in the plan this doc summarizes.

1. `entities.py` — add `get_nearby_sites_simple` beside `get_nearby_venues_simple`
   (ends `:1152`). Emit **identical key names** so nothing downstream branches:
   `site_type` labelled `venue_type`, `literal("site").label("entity_type")`,
   nulls for `cuisine_type`/`price_range`, plus `wikidata_id` for dedup.
   Filters: `ST_DWithin`, `verification_status == "verified"`, **and
   `site_type != "reference"`** (easy to miss — from `db_provider.py:694`).
2. `discovery.py` — `include_sites: bool = False` (**default False is
   load-bearing**, see cross-surface risk), `asyncio.gather` both arms,
   dedup pass, then a distance merge with the site quota.
3. `taste.py` — thread `include_sites` through, **add it to the cache key at
   `:178-187`** (else Places and Home collide at the same rounded coords), gate
   the saved lookup on entity type.
4. `places_projection.py` — add `entity_type: str = "venue"` to
   `PlacesRankedItem` (`:120`). Additive with a default → backward compatible.
5. `projection.py` — pass `include_sites=True`; gate `:74` and `:84-87` on
   entity type; `_ranked_item` emits `id = f"site:{n}"`,
   `canonical_venue_id = None`.
6. Contract regen — `scripts/export_openapi.py` → `docs/openapi.json` →
   `travel-app/utils/api/schema.gen.ts`. `check_openapi_snapshot.py` fails
   pre-push on a stale snapshot.
7. Frontend — gate save on `entity_type`; decide tap behavior.

### Why `venue_type` carries `site_type`

`affinity_matches` (`taste.py:89-113`) reads only `venue_type`/`cuisine_type`.
Put the category anywhere else and personalization for sights is dead on
arrival — including the onboarding "art & history" chip, whose mapping at
`place_affinity.py:429-436` is already written against site vocabulary
(`museum / gallery / landmark / monument`). This change is what finally lets it
fire. `venue_type` is already a loose category namespace rather than a table
discriminator (`place_affinity.py:769`, `core/taste_voice.py:7,18`).

`entity_type` is what keeps that honest: `venue_type` is the *display
category*, `entity_type` is the *identity*.

Rejected: reusing `canonical_venue_id` for the site id — `PlacesCore.tsx:239`
would route to the wrong venue's detail page.

### Two queries merged in Python, not one SQL union

The SQL limit here is a **candidate cap, not a page** — `rank_by_taste`
re-sorts (`taste.py:153`), offset/limit apply in Python (`:206`), `has_more` is
computed in `projection.py:72`. A single union `LIMIT` actively defeats the
goal: a dense restaurant radius fills all 8 slots before a museum is seen.
Per-arm limits plus a Python quota is the only way to *guarantee* sights reach
the ranker. Keeps `get_nearby_venues_simple` byte-identical, so
`whereabouts.py:251`, `concierge_home.py:245` and `producers.py:2527` are
untouched.

### Cross-table duplicates are real

Same real-world place can exist in both tables; **there is no cross-table dedup
anywhere.** The seeding classifier is single-assignment
(`osm_provider.py:263-280`) but the dedup cascade is per-table
(`seed_venues.py:453` vs `:494`, `_DEDUP_TABLES` at `entities.py:930`).

Concrete instance: `content/staging/budapest/budapest-gellert-hill-citadel.md`
declares `entity_type: venue, venue_type: cultural` for a place OSM tags
`tourism=viewpoint`, which seeds into `sites`. Curated markdown and OSM sweeps
write to different tables with no mutual check.

Read-time suppression: `wikidata_id` match first (on both tables — `:92`,
`:250`), then normalized-name within ~60 m. Prefer keeping the **venue** (it is
the routable entity). Refill the quota rather than shrinking the page.
`place_id` is **not** a dedup key — on both tables it is a FK to the locality.

---

## Open questions, in the order they block work

1. **Corpus density is unmeasured.** Verified sites per seeded city, and the
   venue:site ratio inside ~900 m. Decides whether the quota is needed and what
   the constant is. Cheap to measure, and it gates the design.
2. **Does the site detail route block phase 1**, or do sites ship as inert
   cards? Product call.
3. **Saved-sites sequencing.** `saves.py:26-48` and `count_saved_venues:69-92`
   filter `entity_type == "venue"`, so a SAVED-scope page will never show a
   saved site. Trap: if the client starts sending `entity_type='site'` before
   that reader is fixed, saves succeed and are then invisible. Either fix
   `saves.py` in the same wave or disable save-on-site in phase 1.
4. `site_type` vocabulary is only partly known — the `'reference'` exclusion is
   inherited from `db_provider.py:694` and should be re-derived from real data.

## Cross-surface risk — why the flag defaults off

`discover_nearby_ranked` is shared with `concierge_home.py:237`/`:248` →
`producers.py:2489` → `deck_payloads.py:414`, which builds
`entity_ref=f"venue:{vid}"` for any non-None id and offers a Save CTA at
`:427-434`. A site reaching that path produces a corrupt `"venue:site:12"`
reference. Home must keep `include_sites=False` until that path is audited.

## Tests

Existing guards on this path: `tests/places/test_discovery.py` (its
`_corpus_row` helper at `:14-26` is the `_site_row` template),
`tests/places/test_taste.py` (floor units `:49-160`, offset `:226`, cache slice
`:254` — the last two break if the cache key is missed),
`tests/places/test_projection.py`, `tests/home/test_near_you_taste_boost.py`
(proves `include_sites=False` is safe by default).

The regressions that matter most:

- a provider row with no taste match is **still dropped** when sites are in the
  same batch (the guarantee must not weaken);
- a site whose int id equals a saved venue id gets **no** bonus and **no**
  `saved` flag;
- a site never picks up another entity's cached operational status, `in_trip`
  or `loved`;
- `include_sites=False` returns venue-only.

Plus a postgres-marked file for real `ST_DWithin` + the verified and
`site_type != 'reference'` filters — mirror `tests/places/test_cache_postgres.py:1-17`.

---

## Measured against the dev database (2026-07-31)

Queried `localhost:15432/vesper` directly (dev, not prod) to answer the open
question in §1: is the quota even necessary, and is it satisfiable? Full
verified corpus, not the fixture files used earlier.

**Corpus-wide, sites are far more present than the fixtures suggested:**
4,770 verified venues vs **3,062 verified sites** — 39% of the verified corpus,
not the ~2% implied by `venues.yaml`/`sites.yaml`. `sites.site_type='museum'`
alone is 306 rows, against 20 `venues.venue_type='museum'`.

**But density is uneven, and it splits cities into two groups.**

At each city's busiest point (the venue with the most neighbors within 900m,
used as a proxy for a real browse anchor):

| city | venues/900m | sites/900m | sites in nearest-8-by-distance |
|---|---|---|---|
| Copenhagen | 304 | 202 | 3 |
| Tokyo | 265 | 15 | 0 |
| Brooklyn | 234 | 6 | 0 |
| Kyoto | 201 | 145 | 1 |
| Athens | 173 | 0 | 0 |
| Istanbul | 148 | 107 | 0 |
| Rome | 124 | 52 | 0 |
| Madrid | 107 | 58 | 1 |
| Lyon | 97 | 78 | 3 |

**This settles §7.1 of the plan and adds a finding it couldn't have predicted.**

1. **The quota is confirmed necessary, not hypothetical.** Rome has a healthy
   2.4:1 venue:site ratio at its busiest point — and a pure nearest-8-by-distance
   merge still returns **zero** sites, because restaurants/cafés cluster
   physically tighter than museums. Same in Istanbul (148 venues/107 sites → 0)
   and Tokyo. Union-and-rank alone would ship almost no visible change in most
   cities even after the query is fixed.
2. **Coverage is a second, separate axis — and it's binary in a way the plan
   didn't anticipate.** Athens has zero verified sites anywhere; the query fix
   does *nothing* there — this is a content gap, not a code gap. 80 of 142
   cities with verified venues have zero verified sites at the city level
   (Athens confirmed; most of the other 69 `places` rows with zero sites are
   neighborhood/trip-scoped entries like `Trastevere` or `J07 Lisbon <hash>`,
   not top-level cities — their venues likely resolve to a parent city that
   does have sites, unconfirmed without a place-hierarchy join). Copenhagen,
   Kyoto, Lyon, Madrid, Istanbul and Rome all have real density and would
   visibly change; Athens, and to a lesser extent Tokyo/Brooklyn, would not.

**Implication for sequencing:** A1 (query + quota) is worth building — it
transforms Places in a majority of dense cities. But it should ship alongside
an explicit acknowledgment that coverage varies by city, not a claim that it
fixes Places everywhere. The Athens-shaped gap is a content/ingestion backlog
item, separate from this change, and no query fix closes it.

---

## Decision: how sites become tappable (2026-07-31)

**Question asked:** can sites just reuse the existing venue detail page?

**Answer: not as-is — that is the most dangerous option available.**

`GET /api/venues/{venue_id}` (`backend/api/routes/venues.py:62`) takes a plain
`int` and selects from `venues` where `id == venue_id`. Handed a site id it does
**not** 404. It returns a different real place, confidently, with no error.

Measured on the dev DB: **all 3,062 sites collide with a real venue id — 100%,
not an edge case.** Both tables number from 1 (venues max 5459, sites max 3098).

| site id | site name | venue you would actually open |
|---|---|---|
| 1 | A Padaria Portuguesa — Belém | A Baiuca |
| 2 | Café A Brasileira | A Cevicheria |
| 3 | Café Almirante | A Cevicheria |
| 4 | Café de São Bento | Adega Machado |

Right name in the list, wrong page on arrival, silent. This is worse than sites
being untappable.

**Chosen approach: one shared detail screen, endpoint resolves either table.**

The venue detail screen is already mostly generic — name, neighborhood, map
position, curator brief, photos are all fields sites have too. So the screen is
reusable; the *lookup* is what must change.

- id namespaced as `site:42` so the resolver knows which table to open
- `get_site` already exists (`entities.py:812`), so the backend half is cheap
- hide for sites: `cuisine_type`, `price_range`, `price_per_person_estimate`,
  `reservation_required`, `avg_meal_duration_minutes`
- surface for sites: `admission_fee`, `visit_duration_minutes`, `period`,
  `significance_level`, `accessibility`

Meaningfully cheaper than a separate screen, and it avoids the collision
entirely because the namespaced id never enters an int-typed venue lookup.

---

## Illustration wiring fix (2026-07-31, same day)

Asked separately, after phase 6: "is our illustration all wired up?" — checked
rather than assumed, and the answer was no.

**The site-aware fallback already existed in the codebase, unused.**
`imageClassForEntityType('site')` correctly maps to `viewpoint_nature`, and
`EntityImage` already accepts an `entityType` prop to pick the right riso
variant — but `PhotoThumb` (what every Places row renders through) only ever
called `imageClassForVenueType(venueType)` and never passed `entityType`
through. A site row could reach neither.

This mattered immediately, not hypothetically: `photo_urls` is 100% NULL in
the dev DB for both venues and sites (confirmed earlier this session), so this
fallback illustration is what renders for every museum card today.

**Measured impact:** `imageClassForVenueType` silently defaulted **45% of
site rows (1,377 of 3,062)** to the generic `city_neighborhood` bucket via its
catch-all default — mostly `day_trip` (358) and `transit` (272), which have no
venue_type bucket at all.

**Fix**, on `travel-app` branch `places/sites-frontend-2026-07-31` (commit
`615f7cdd`):
- `imageClassForVenueType` now returns `null` when it can't classify, instead
  of silently defaulting. Confirmed type-safe and non-breaking against all 9
  existing call sites via `tsc --noEmit`.
- Added `mosque` to the `culture_art` bucket (temple/cathedral/church were
  already handled — a clean omission, not a judgment call).
- `PhotoThumb`/`PlaceRow`: `imageClassForVenueType(venueType) ??
  imageClassForEntityType(entityType) ?? 'city_neighborhood'` — a confident
  venue_type match (museum → culture_art) is never overridden; the
  entity-type fallback only fires for what venue_type genuinely couldn't
  classify. `entityType` is also now passed to `EntityImage` so sites reach
  the tier-2 bundled-place-riso variant picker the same way venues do.

**Deliberately left open:** `day_trip`/`transit` stay unmapped in
`imageClassForVenueType` — which specific bucket fits them is a design call,
not a bug. They now correctly fall through to the site fallback
(`viewpoint_nature`) instead of the wrong generic default, which is the
actual fix.
