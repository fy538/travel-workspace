---
doc_type: working
status: active
owner: Claude orchestrator (product map)
created: 2026-09-26
expires: 2026-10-26
why_new: No existing document inventories, in one place and with evidence, what real-world content and user data actually exists to fill Home, Places and Life for a real NYC user, and what a bounded launch-neighborhood supply plan would require.
promotes_to: null
supersedes: []
---

# Supply and data: what actually exists to fill Vesper (NYC focus)

This page is part of the product map. It asks one question: **when a real New York user opens Home, Places and Life, what content and data actually exist to fill those surfaces?**

It covers:

- content corpora;
- supply pipelines;
- user and friend data;
- QA personas;
- a concrete plan for supplying one NYC launch neighborhood.

This is a read-only inventory, not a design proposal.

## 0. Evidence boundary

**Baseline inspected.** Merged baseline `/Users/feihuyan/travel-workspace--product-map-inventory`:

- workspace `6ef3dca`, travel-agent `c8c9f5785`, travel-app `43225df35`, all dated 2026-09-25;
- archived travel-agent refs under `refs/archive/*`.

**Additional local files.** Some content is gitignored and exists only on the founder's machine, in the canonical checkout `/Users/feihuyan/travel-workspace/travel-agent` (`fdf789d06`). These were read as local files:

- `content/staging/{brooklyn,tokyo,copenhagen,kyoto,istanbul}`;
- `.cursor/tasks`;
- `content/place_illustrations`.

**Commands I actually ran** (all read-only; no DB or Qdrant connection, no external API call):

- `python -m tools.dogfood.content.content_inventory_v2 --repo-only`, which exited 0.
- `python scripts/check_vesper_world_catalogs.py`:
  - exited 0 with no flags;
  - **exited 1** with `--runway-days 14`, the flag CI uses; see §2.6.
- The archived NYC corpus adapter from commit `4254554cf`, run with `--validate` against the current backend models from a scratch copy. It printed `4 sources, 3 accepted readings, 0 writes`.
- `git apply --check` of commit `4254554cf` against main.
- Python and YAML parsing of repository and local staging files, to produce the counts below.

**What I did not verify:**

- production or dev Postgres and Qdrant contents;
- deployed secrets and provider keys;
- GitHub Actions run history;
- device rendering.

Row counts from docs are dated observations and are labeled as such. **Anything described as "in production" comes from a receipt or doc, not from a live query.**

**Subagent reports.** Three read-only helper audits were merged in:

- supply pipelines and intake;
- providers and media;
- new-user day-1 content and personas.

Their claims were spot-checked where it mattered. One correction: the pipeline audit said no NYC staging content or Cursor task exists. Both do exist, but only as gitignored local files. See §2.1.

---

## 1. Bottom line

1. **Vesper has no reviewed, runtime-eligible NYC supply on main.** It has four things:
   - A **Brooklyn-only legacy corpus** from May 2026: about 325 venues with AI-authored briefs. Hours cover about 12% of venues, verified photos 0%. It is traveler-framed and has no review state. It is in the DB export and Qdrant.
   - An ignored local Cursor staging dump of **425 Brooklyn briefs**, 109 of which are not in the DB.
   - **Three NYC "Here" exhibition rows** in the Home catalog. They expire **2026-10-09**.
   - **Three reviewed Red Hook readings** stranded on an archived ref.

   There is nothing for Manhattan, Queens or the Bronx beyond place-tree stubs and a loader script.
2. **The governed content system is real, but has hardly been fed.** It comprises World Foundry, `place_content_primitives`, source observations, and the Home public-content adapter. Its total accepted output anywhere is **13 primitives**, all Amalfi/Sorrento and on localhost. The offline acceptance evaluator currently accepts **0 canonical lanes** because a review hash has drifted.
3. **Operational freshness is the weakest layer.**
   - Hours come lazily from Google or Foursquare. The Foursquare adapter still targets the `/v3` API that Foursquare deprecated on 2026-05-15.
   - Venue `photo_urls` were 100% NULL in dev.
   - The event producers exist (Ticketmaster and Bandsintown ingesters) but are not scheduled. In the 2026-07-31 count, only **2 dated events anywhere had a future start**.
   - Every seeded Brooklyn event is now in the past.
4. **The Home "world" band will go dark on its own.** Season and Here rows are hand-maintained YAML with a hard review expiry of 2026-10-09. CI's 14-day runway check already fails as of 2026-09-26.
5. **User-generated supply is the most plausible day-1-to-week-1 source**, but its pipes are partly dark:
   - Share sheet → catalog resolution is built.
   - Email forwarding is code-complete but blocked on DNS MX and SendGrid setup.
   - Source contribution is dark: explicit-warm only, behind two flags and a named cohort.
   - Friend material reaches another user today only as co-member saves inside a shared trip. Addressed handoffs and original deliveries are dark (§4.2).
6. **A default-build NYC newcomer today sees very little of NYC.** The default tabs are Plans, Vesper, Places and Life.
   - **Plans:** generic starter cards; near-you is stripped in public builds.
   - **Vesper:** 3 NYC exhibitions plus national-park seasons.
   - **Places:** "Anywhere" starter cities, or Brooklyn-only nearby rows with location.
   - **Life:** empty.

   After a week, the app mostly reflects back the user's own saves and shares (§5).
7. **Every persona and fixture world is synthetic.** Some are anchored on real places: Elif's Brooklyn uses real venues such as Paulie Gee's and Bakeri. The histories, events, photos and friends are all authored or AI-generated.
8. **The cheapest credible NYC launch is North Brooklyn (Williamsburg and Greenpoint)**, or a founder-lived neighborhood if dogfood realism matters more. It reuses the most existing assets. It needs roughly 4–6 focused weeks of solo-founder supply work plus recurring weekly curation. §9 has the plan.

---

## 2. Content corpora, in detail

### 2.1 Legacy editorial staging (`travel-agent/content/staging`)

**Registry.** `content/staging/README.md` (2026-07-05) lists **39 cities**: 9 active, referenced by a dogfood pack, and 30 frozen.

**What is tracked in git.** 37 directories:

- 34 tracked Mediterranean/European cities, from Amalfi to Venice;
- Budapest;
- a small tracked Istanbul subset of 18 files;
- `README.md`.

**What is local only.** `.gitignore` lines 88–93 ignore **Brooklyn, Tokyo, Copenhagen, Kyoto and Istanbul** as "Large city batches not yet reviewed/promoted". Scout, angle and cartographer intermediates are also ignored. These exist only on the founder's disk:

| Ignored city (local) | Files | Venue/other briefs | `_place_` dossiers | Scout / angle intermediates |
|---|---|---|---|---|
| brooklyn | 519 | 426 (incl. `collections.json`) | 7 | 42 / 42 |
| tokyo | 667 | 438 | 10 | 96 / 96 |
| copenhagen | 818 | 591 | 6 | 92 / 92 |
| kyoto | 584 | 415 | 9 | 79 / 79 |
| istanbul | 570 | 382 | 6 | 87 / 87 |

**Repository-wide inventory.** `content_inventory_v2 --repo-only`, run 2026-09-26:

| Measure | Count |
|---|---|
| Staging files | 5,914 |
| Tracked | 5,794 |
| Brief files | 5,913 |
| Dossier files | 353 |
| Files with a Sources section | 5,700 |
| Content-hash, validity or review-state files | **0** |

That last row means the legacy corpus has no machine-readable review state, validity window or content hash. The runbook says so directly: "A legacy brief with a Sources heading is not automatically a claim-ready primitive" (`travel-agent/docs/operations/content-inventory.md`).

#### The local Brooklyn staging dump

Location: `content/staging/brooklyn/`. File dates are 2026-07-11; content was researched around May 2026.

**Briefs: 425** — 398 venues, 14 sites, 13 accommodations. By venue type: restaurant 308, bar 43, café 33, hotel 12, then a long tail.

**Neighborhoods.** Frontmatter names a neighborhood on only 42 files. By first neighborhood mentioned in the body: Williamsburg 86, Park Slope 78, Bushwick 61, Carroll Gardens 20, Cobble Hill 19, DUMBO 19, Bed-Stuy 17, Greenpoint 16, Fort Greene 14, Brooklyn Heights 12, Red Hook 10, Prospect Heights 9, everything else under 9 each. Manhattan is mentioned first in only 7 briefs.

**Depth.**

- Every brief has a `## Brief` section; the median brief is about 800 characters.
- The median brief cites 3 source URLs, and none has zero.
- Only **44** have dossier sections: `why_here` 39, `tension` 16, `ritual` 10, `affinity` 2.
- There are 7 place dossiers: Brooklyn, Bushwick, Crown Heights, DUMBO, Park Slope, Red Hook and Williamsburg. Each has `why_here`, `day_in` and `tension` lenses.
- `collections.json` holds 7 guides, for example "Williamsburg on a Weeknight" and "Queer Brooklyn After Dark", with 7 members each.

**Voice.** The briefs are written for visitors. They say things like "your trip" and "the DUMBO stay when the product is the view". That is the wrong register for an everyday-first product unless it is rewritten.

**Overlap with the DB.** Compared with the DB export (§2.2), **316 slugs overlap, 109 are staging-only, and 9 are DB-only.** The staging-only rows include hotels, the Brooklyn Bridge walkway, the Heights Promenade, Coney Island and about 90 restaurants and bars.

**Cursor tasks.** Four local Brooklyn task files exist in `.cursor/tasks`: `tier1-brooklyn.md`, `tier2-brooklyn.md`, `tier3-brooklyn.md` and `write-dossier-brooklyn.md`. Rule: `.claude/rules/cursor-tasks.md` says never execute them via the Claude API. `_PROGRESS.md` records that 23 place-research tasks were once accidentally run via the API.

### 2.2 Promoted seed batches and the Brooklyn DB snapshot

**The pipeline.** `tools/seed` is an AI-authored JSON pipeline: validate, spot-check 1 in 5, promote to Postgres idempotently, embed, then export to eval YAML. Its README status line (2026-05-13) reads: "Phase 2 bootstrap for Brooklyn + Lisbon is complete. Brooklyn brief coverage went from 3% → 99%".

**Promoted batch totals** (`tools/seed/staging/_promoted/`, 118 files):

| City | Main contents |
|---|---|
| **Brooklyn** | 313 venue briefs, 26 venues, 13 accommodations, 12 sites, 40 experiences, 30 place angles, 40 hours/price drafts, 32 brief drafts, 4 traveler-depth rows |
| Lisbon | 104 venues, 104 briefs, 30 experiences, 84 angles, 15 traveler-depth rows |
| Rome | 2 places, 1 site, 4 venues, 15 experiences |
| Istanbul | 6 places, 3 sites, 3 venues, 17 experiences |
| Tokyo | 5 places, 6 venues, 16 experiences |
| Copenhagen | 1 place, 16 experiences |
| Nadia / Budapest | 1 place, 6 venues, 6 briefs |

**Brooklyn Postgres snapshot.** The best repository evidence of what the DB holds for Brooklyn is `tools/eval/data/brooklyn/*.yaml`, exported from Postgres (last change `b4718037e`, 2026-05-14). This file is fixture evidence, not a live query.

| Entity | Count | Field coverage and notes |
|---|---|---|
| Venues | **325** | Brief summary on 324; coordinates on 325. **Hours on 38 (11.7%)**. Price on 34, reservation info on 32, accessibility on 3. **No photo field.** |
| Venue categories | — | Restaurant 212, café 51, bar 48, cultural 5, music venue 3, market 3, bakery 2, food hall 1. Grocery, pharmacy, gym, library, park and service rows: **0**. |
| Venue neighborhoods | — | Park Slope 78, Bushwick 55, Williamsburg 49, Cobble Hill 38, DUMBO 25, Bed-Stuy 19, Fort Greene 15, Brooklyn Heights 14, Greenpoint 9, Boerum Hill 6, Downtown 4, Red Hook 4, Prospect Heights 3, Carroll Gardens 3, Gowanus 2, Ridgewood (Queens) 1 |
| Hours by neighborhood | 38 total | Williamsburg 16, DUMBO 5, Park Slope 4, Bushwick 4, Greenpoint 4, others ≤ 2 |
| Sites | 28 | Prospect Park, Brooklyn Museum, Green-Wood Cemetery, Domino Park, McCarren Park, Greenpoint Waterfront, Smorgasburg, and others |
| Accommodations | 13 | Hotels |
| Experiences | **27** | All dated April, June or September 2026, and **all now in the past**. Some are generic AI placeholders, such as "Headliner Concert at Brooklyn Steel". A 29-row ticket-URL backfill (`brooklyn-experience-metadata-001.json`) was never promoted. |
| Travelers | 10 | Synthetic eval travelers, e.g. maya-brooklyn and dev-brooklyn |

**Hours backfill.** Two batches exist: `brooklyn-hours-001` (7 chain templates) and `brooklyn-hours-002` (22 per-venue web captures, dated 2026-05-13). Their skip logs record closures found during research, for example Sauvage in Greenpoint and Jack the Horse Tavern. **Staleness is already demonstrated in this corpus.**

**Place angles.** There are 30, six each for DUMBO, Brooklyn Heights, Bushwick, Williamsburg and Greenpoint. They are written for visitors, for example "Sunday-morning coffee loop". They have **no Postgres table**; they live in `_promoted/place_angles/*.json` and in Qdrant.

**Historic fragility.** `docs/operations/Content Pipeline Audit.md` (May 2026) found that a places-tree migration had cascade-deleted Brooklyn venues from Postgres while Qdrant kept 301. The Phase 2 bootstrap later backfilled them. Production parity with this snapshot is unverified.

**Production-wide brief coverage.** `fly.toml` comments that "only ~24% of venues have an authored brief today (sites ~79%)". So Brooklyn's roughly 99% is an exception.

### 2.3 World Foundry (governed research to promotion)

**What it is.** `travel-agent/docs/operations/World Foundry.md` (canon, 2026-08-09) defines a Codex-subscription workflow:

- controller `gpt-5.6-sol` and workers `gpt-5.6-terra`, both with high reasoning;
- repository processes are forbidden to call `call_llm()`;
- field-level source observations, cross-review by a different agent, explicit transactional promotion, and a derived Qdrant.

The evidence order runs: official operator or government source first, then first-party ticketing, open data, reputable editorial, and finally community material as a weak signal.

**What it has produced.** `tools/seed/staging/runs/` holds 34 entries (runs plus a few top-level notes).

City packs total **117 rows and 200 source observations**:

| City pack | Rows | Source observations |
|---|---|---|
| Nice | 28 | 51 |
| Amalfi Coast | 26 | 52 |
| Sorrento | 23 | 46 |
| Istanbul catalog-core | 20 | 1 |
| Lisbon (4 packs) | 14 | 36 |
| Rome (2 packs) | 6 | 14 |

Promotion targets:

- **Production-dogfood (Neon) receipts: 2.**
  - `lisbon.2026-08.demo-anchors-01`, 2026-08-12, 2 rows;
  - `rome.2026-08.demo-beats-production-01`, 2026-08-13, 3 rows.
- **Everything else is localhost.** That includes the Riviera throughput (26 venues, 12 accommodations, 27 sites, 8 hubs, 17 experiences), Istanbul and the Lisbon canary.
- Serving a release requires `WORLDFOUNDRY_DOGFOOD_SERVING_ENABLED`, which defaults to off.

**NYC.** The only NYC run is `brooklyn.2026-08.demo-moments-01`, an offline **controlled-demo** "right now" contract:

- it selects Paulie Gee's in Greenpoint for Elif;
- the opening observation, route minutes and location are all `source_mode: controlled_demo`;
- "database_writes: 0, provider_calls: 0".

It proves a UI moment, not supply.

**No NYC CityPack exists.** The queue tool supports one: `scripts/world_foundry_queue.py --city <slug> --target local`.

### 2.4 Place content primitives ("readings")

**Schema.** `backend/core/models/place_content.py` defines six primitive types:

- interpretive lens
- perceptual cue
- approach cue
- conditional judgment
- question to carry
- relationship rule

Rows move through review states (proposed → accepted, rejected or quarantined) and lifecycle states (active, superseded, retracted), with validity windows. Only accepted, active, grounded, public rows are served.

**What is accepted.** 13 primitives exist, for Amalfi (the Duomo complex) and Sorrento (Marina Piccola), with 25 ordered evidence links. They were accepted on **localhost only**, on 2026-08-16 (`runs/place-content.2026-08.acceptance-01/local-apply-01.receipt.yaml`).

**Acceptance evaluator.** `docs/operations/content-runtime-acceptance.md` (dated observation 2026-09-23) says the evaluator "accepts **zero canonical lanes**". The reason: the immutable review binds an exact hash of `backend/core/db/place_content.py`, which has since changed. A fresh independent review is required.

**Flag.** `PLACE_CONTENT_PRIMITIVE_READS_ENABLED` defaults to off. It gates only the legacy semantic-memory compatibility path.

**The Home public-content path is live code.** `home_portfolio.py::places_context` calls `list_current_public_place_content_sources_for_places(...)` for the user's automatic Places context, with a limit of 6. It turns rows into `HORIZON_EDITORIAL_PASSAGE` candidates with no model or provider call (`docs/working/content-home-supply-execution-receipt-2026-09-08.md`). **So the receiving pipe exists; what is missing is NYC rows.** The NYC Pier 57 copy in that receipt is labeled "authored review specimens, not populated production rows".

#### The archived NYC corpus

Commit `4254554cf`, "Add reviewed NYC place reading corpus" (2026-09-15). It is reachable only from `refs/archive/consolidation-2026-09-23/worktrees/0db062db…` and `refs/archive/retired-2026-09-23/codex/engine-er123-integration`; it is **not on main**.

- **Contents.** `tools/dogfood/content/nyc-place-readings-v1.yaml` holds corpus `nyc-red-hook-working-waterfront-v1`:
  - **4 sources**: 2 NYC government PDFs, the Pioneer Works about page, and the Waterfront Museum about page;
  - **3 readings**, all `entity_slug: red-hook`:
    - Pioneer Works as industrial reuse (interpretive lens);
    - the lighterage barge as a surviving freight layer (perceptual cue);
    - Red Hook shaped by one freight system and isolated when it changed (interpretive lens; the only row with `opening_eligible: true`).
- **Review.** `review_authority: founder_delegated_canonical_review`, reviewed 2026-09-15. Scope is durable interpretation only, with no hours, access, event or route claims.
- **Loader.** `nyc_place_reading_corpus.py` is an idempotent operator adapter over the existing source-observation and primitive owners. It supports `--validate`, `--apply` and `--retract`, and needs `--allow-prod` for remote writes. A test file is included.
- **What it takes to land:**
  1. **Applying the patch.** `git apply --check` shows the three new files apply cleanly to main. Only the `backend/lived_experience/FEATURE.md` doc hunk conflicts, which is trivial.
  2. **Offline validation passes against current main models** (run 2026-09-26).
  3. **Tests.** Run `tests/tools/test_nyc_place_reading_corpus.py` on main (not run).
  4. **Place row.** The target DB must contain the `red-hook` place; `scripts/seed_nyc_outer_places.py` inserts it under `brooklyn`.
  5. **Acceptance review.** Because the acceptance lane is currently hash-drifted, get a fresh independent acceptance review rather than reusing the 2026-09-15 receipt, if the lane gate is to be honored.
  6. **Serving.** Apply locally, then to production-dogfood only with explicit authorization. Readings then surface on Home only for users whose automatic Places context resolves to Red Hook or its subtree.
- **Value.** It is small: 3 readings for one neighborhood that has 4 DB venues. Its real value is as **the template** for an NYC reading corpus. It shows the source style, the limits vocabulary, and the one opening-eligible row per cluster.

### 2.5 NYC geography

- **City root.** Migration `nycplace01` (2026-08-02) created `new-york-city` with aliases `nyc` and `new-york`, and **reparented `brooklyn` under it** "without relabeling Brooklyn content as city-wide coverage".
- **Outer places.** `scripts/seed_nyc_outer_places.py` adds Queens and Ridgewood, plus these Brooklyn neighborhoods: Boerum Hill, Downtown Brooklyn, Carroll Gardens, Crown Heights, Red Hook and Gowanus.
- **Boundaries.** `scripts/load_nyc_ntas.py` exists on main. It loads NYC OpenData 2020 Neighborhood Tabulation Area polygons (`9nt8-h7nd`) into `places.geometry`. It references legacy hierarchical district slugs such as `new-york-new-york-city-manhattan`, which may not match the current tree. Whether it has been run anywhere is unknown.
- **Manhattan, Queens and the Bronx: no venue, site or brief corpus exists in the repo.** A new user in the West Village has essentially no curated supply.

### 2.6 Vesper world catalogs (the Home "Here" and "Season" bands)

The catalogs live in `backend/home/vesper_workbench/data/`.

**`here_windows.yaml`: 3 rows, all NYC.** The file header calls it a "First-city pilot".

| Row | Venue | Window | Review expires |
|---|---|---|---|
| Flower Power | NYBG, the Bronx | 2026-05-23 → 10-18 | **2026-10-09** |
| Growing America | NYBG | 07-04 → 10-18 | **2026-10-09** |
| Pioneers in handmade paper | Grolier Club, Manhattan | 09-08 → 11-28 | **2026-10-09** |

Each row carries a source URL, `source_as_of`, a note, and an explicit disclaimer that it is not an opening-hours or ticket claim. The `place_labels` cover all five boroughs.

**`season_windows.yaml`: 4 rows.** They are national-parks seasons:

- Acadia fall color, Yellowstone elk rut and Grand Canyon raptors, each expiring 2026-10-09;
- Hawaii humpbacks, 2026-11-01 → 2027-05-31, expiring 2027-06-15.

None of these is an NYC everyday item.

**`route_destinations.yaml`.** A JFK-origin list of Duffel destinations for the Route band. `HOME_ROUTE_DUFFEL_ENABLED=false` in `.env.example`.

**Gate.** `scripts/check_vesper_world_catalogs.py --runway-days 14` runs in CI (`.github/workflows/ci.yml:249`) and as `make vesper-world-catalogs`. It requires at least 3 current rows per band on every day of the runway.

**Executed 2026-09-26:**

```text
Vesper dogfood catalog runway must contain at least three rows per band on 2026-10-09: season=0, here=0
```

It exits 1. **The CI step should fail on any run from about 2026-09-25 onward.** I executed it locally; I did not observe it in CI.

After October 9, Home's Season and Here producers have no eligible rows. The FEATURE doc confirms that "the catalog is not self-refreshing". Refreshing it is a manual editorial job: roughly 6+ source-checked rows every 2–3 weeks.

### 2.7 Dogfood content packs (`tools/dogfood/content/packs.yaml`)

**Every pack has `app_qa_status: not_run`.**

| Pack | City | Personas | State | Notes |
|---|---|---|---|---|
| lisbon-phase1 | Lisbon | mara, dao, reza, elif | W2_local | Richest. 1,874-line manifest; 44 media files; eval world with 138 venues, 56 sites, 22 hotels, 26 experiences |
| elif-rome | Rome | elif, sarah, mike | W2_local | Two Rome World Foundry rows promoted to production-dogfood |
| tokyo-phase1 | Tokyo | elif, sarah | backend_parity_local | Staging is gitignored |
| istanbul-phase1 | Istanbul | elif, sarah, mike | W2_local | World Foundry catalog-core of 20 rows, local only |
| **brooklyn-phase1** | Brooklyn | elif | **W1_local** | "local baseline/control sample" (details below) |
| local-occasions-phase1 | multi-city | elif, mara, dao, reza, nadia | W2_local | Includes "Elif's Brooklyn Friday night" (2026-07-31) |
| solo-trips-phase1 | Athens, Naples, Copenhagen, Kyoto | dao, reza, mike, sarah | W2_local | |
| nadia-budapest-phase1 | Budapest | nadia | W2_local | Corpus was web-researched by hand |
| atlas-phase1 / atlas-phase2 | cross-city | — | W0 | Atlas artifacts |
| cascade-phase-fixtures | cross-city | — | W1 | |
| riviera-place-relationship-phase1 | Nice / Sorrento | elif, giulia | W0_local | Nice 87 venues and 195 hotels in eval; World Foundry citypacks for Nice, Sorrento, Amalfi; the 13 accepted primitives |

More on **brooklyn-phase1**:

- Its surfaces are `discover`, `atlas`, `receipts` and `media`. `places` and `trip_detail` are marked `gap`.
- `trips_home` is `deferred`, with the note "does not seed or infer a Home location".
- Substrate: 1 local-week trip (2025-07-17 → 23), 5 observations, 4 saves, 3 affinities, 1 Atlas artifact and 8 trip photos.

**Summary:** Lisbon and Rome are the only cities with near-complete dogfood substrate. Brooklyn is deliberately a thin baseline.

### 2.8 Photos and media

- **Venue photos.** `docs/working/places-sites-reachability-2026-07-31.md:335` says "`photo_urls` is 100% NULL in the dev DB for both venues and sites". The Location Seeding Playbook §6 says venue galleries come from Google Places lazily and on demand, and "can't bulk-store per ToS". Place hero images come from hotlinked Pexels (`seed_place_photos.py`).
- **Reviewed photo records.** These exist only for a few Rome dogfood cards: `places_exact_photo_pack.py` rehosts 2 official venue images, and `places_media_pack.py` handles covers.
- **Illustrations.** `content/place_illustrations/` has 44 city folders, including 6 Brooklyn images (hero, day, night, fun, nature, site). They are gitignored, about 728 MB, and "deliberately not run" to a CDN (`.gitignore` comment). `places.illustration_urls` stays empty.
- **Dogfood media.** 211 files, all **AI- or subscription-generated** ("internal-dogfood-authored").
  - Elif's canonical inventory has 119 assets: Rome 36, Tokyo 33, Istanbul 30, Brooklyn 20. All are `staged`.
  - The prompts deliberately avoid real signage and faces.
  - R2/S3 is dormant (`upload_media.py`), so media is served from the repo through `/dogfood-media`.
- **Real NYC venue photo coverage today is effectively 0%.** Only lazy provider photos exist, and only where a key is configured.

### 2.9 Events and "what's on"

- **Ingesters in code** (`backend/ingestion/`): Ticketmaster, Bandsintown (needs an explicit artist list), Viator and Amadeus Tours. The schema also permits `edmtrain`, `getyourguide`, `local` and `curator` sources, but nothing ingests edmtrain or getyourguide.
- **How ingestion runs.** It is CLI-only (`scripts/ingest_events.py`), or inside `seed_place.py`/`seed_city_full` with a 90-day window. There is no cron.
- **Live inventory.** `docs/working/cold-start-and-everyday-places-experience-mvp-2026-07-31.md` (§ open question 7, 2026-07-31) counted the `experiences` table directly. Which environment is unclear.
  - "1 Ticketmaster row, 1 Bandsintown row, 0 Viator/Amadeus Tours rows … ~38 `curator` rows";
  - "only **2 have a future `starts_at`**";
  - "The product cannot honestly promise 'a rave near you this weekend' on this inventory in any city, NYC included."
- **Known Ticketmaster defects** (`docs/working/recommendation-world-supply-architecture-and-roadmap-2026-09-07.md` §3D). These were observed at audit time; some repairs are recorded later in that doc's §10–§13.
  - UTC is applied to local times.
  - Missing dates fall back to 2099.
  - Page bounds are wrong.
  - Currency defaults to EUR.
  - The event query tool defaults to Lisbon/PT.
- **Trip scoping.** The Places experience-preview producer requires a dated Trip and "returns nothing for an ordinary city scope".
- **Legal.** Ticketmaster terms restrict revenue-derived use and caching. Eventbrite's public search API has been shut down since 2019. RA, PredictHQ and EDMTrain are partnership or procurement questions.
- **Result: no producer supplies an ordinary NYC week.** The only live "what's on" material for NYC is the 3 manual Here rows.

### 2.10 External providers and their configuration

I made no live calls. "Doc-prod" means a dated doc claims the key is set in Fly. "Local" means the key name appears in the founder's gitignored `.env`; I read names only, never values.

The authoritative runtime evidence would be the worker's provider-canary snapshot in Redis (`backend/workers/provider_canaries.py`, which runs four times a day). I did not read it. The canary does **not** probe Foursquare, Mapbox, Open-Meteo or Ticketmaster.

| Provider | Job for NYC | Code / env | Status evidence | Concern |
|---|---|---|---|---|
| **Google Places (New)** | Hours, open-now, business status, exact-place photo, linking | `backend/places/google_places.py`, `factory.py`. The live service reads **`PLACES_GOOGLE_API_KEY`**. Everything else, including photo, distance and research, reads `GOOGLE_PLACES_API_KEY`. | Doc-prod: "Google Places + Foursquare keys — set in Fly" (`docs/Owner Action Items.md`, line dated 2026-07-09). `fly.toml` lists only `GOOGLE_PLACES_API_KEY` as a minimum secret. Local: both names set. | **Naming mismatch (verified in code).** With only the unprefixed key in Fly, the live hours/open-now service has **no Google provider**. The cost comments ("$17/1k", daily limit 100) are stale: the hours field is Enterprise Details, about $20/1k. Photos are `no_store` and fetched live per view. |
| **Foursquare** | POI search and status; primary whenever a key exists | `backend/places/foursquare.py` and the research tool both target `https://api.foursquare.com/v3` | Doc-prod as above; local key present | **The `/v3` family was deprecated 2026-05-15.** If the key is still set, Foursquare is primary on the deprecated endpoints, errors fall through, and the fallback exists only if `PLACES_GOOGLE_API_KEY` is set. The free tier is now 500 calls per month, not per day. "Migration vs replacement" is an open decision. |
| **Mapbox** | App map tiles; backend directions, isochrone, matrix, static maps | App: `@rnmapbox/maps`; production builds require `EXPO_PUBLIC_MAPBOX_TOKEN` (`app.config.js`). Backend: `MAPBOX_TOKEN`. | App token set in local `.env.local` (2026-09-04); EAS production env unknown. Backend token absent from every env file (2026-08-06 doc); production unknown. | Isochrone and matrix sit behind default-off flags. Mapbox has no transit profile. Google content may not render on Mapbox. |
| **Open-Meteo** | Home weather, Places weather windows, digest, rescue | `backend/core/weather_provider.py`; no key needed | Works whenever the network works | No cache for current conditions; Home fails closed after 0.8 s. Weather-rescue proposals sit behind an allowlist that defaults closed. |
| **Transit** | Subway and ferry times | No MTA, GTFS or Citymapper integration. Transit times go through Google Distance Matrix, cached 30 min. | Transit "bake-off blocked on credentials" (2026-08-06) | No NYC transit supply beyond request-time Google estimates |
| **Events** | "What's on" | Ticketmaster (`RESEARCH_TICKETMASTER_API_KEY`), Bandsintown (needs an artist list), Viator/Amadeus (query-only by default). Chat live-event discovery goes through Tavily, then approved domains (RA, DICE, TM, Eventbrite, AXS, Songkick, Bandsintown), then JSON-LD validation. | Ticketmaster key status unknown; not in the local `.env` | No ingestion cron. Home `happening_nearby` requires a trip plus `HOME_TASTE_SEARCH_ENABLED`, which is `"false"` in `fly.toml`. |
| **Tavily** | Web research, live-event evidence | Minimum Fly secret; `WEB_SEARCH_MODE` defaults to live | Probed by the canary | $0.008–0.016 per search |
| **Pexels / Wikimedia / Europeana** | Place hero and atmosphere images | `seed_place_photos.py` hotlinks; atmosphere manifests exist for Istanbul, Lisbon, Rome and Tokyo | Local key present | **No NYC atmosphere manifest.** Pexels is "area atmosphere" only, never evidence of a venue. |
| **Media storage (R2/S3)** | Rehosting reviewed images | `MEDIA_S3_*` | Only `MEDIA_CDN_BASE_URL` is set locally; `fly.toml` says R2 is deferred | Blocks any real rehosted photo pipeline |
| **LLMs** | Briefs, extraction, contributions, chat | Anthropic Haiku 4.5 and Sonnet 4.6 by role; OpenAI embeddings (`text-embedding-3-small`, 768) in production | The Anthropic account showed "no credit" on 2026-09-01 and 2026-09-07 (program docs); the spend cap is "FOUNDER-MUST-CONFIRM" | Content generation in World Foundry and Cursor uses subscriptions, not the API |
| **SendGrid inbound** | Email forwarding intake | `/api/inbound-email/sendgrid/{secret}`; `INBOUND_EMAIL_DOMAIN` defaults to `import.vesper.trip` | **Blocked**: DNS MX record plus SendGrid Parse dashboard setup; listed as deferred in Owner Action Items | See §3.3 |

**Canonical venue seeding is not Google.** It comes from OSM Overpass (`research_agent/tasks/seed_venues.py`). So `google_place_id` coverage, which the exact photo and live hours both need, depends on the linker and backfill scripts.

The only measured linkage figure found is local dev only: "21/24 dogfood stub venues resolved a `google_place_id`, 18/24 also got `hours`" (`travel-agent/docs/working/places-object-page-data-gap-2026-08-03.md`).

**Owner checks to run before any NYC supply work:**

1. Confirm which Google key name is in Fly.
2. Confirm whether the deprecated Foursquare key is primary.
3. Read the latest provider-canary snapshot.
4. Confirm the Mapbox and Ticketmaster keys, and the EAS production Mapbox tokens.

---

## 3. Supply pipelines: what is automated and what is manual

### 3.1 Summary table

| Pipeline | Produces | Trigger | Automated? | Evidence it ran | NYC relevance |
|---|---|---|---|---|---|
| Legacy `seed_place.py` (Method A) | Places, OSM venues, Google photos, OSM hours, Haiku briefs, TM/BIT events, angles, dossiers | Operator CLI; also the lazy `seed_city_full` Arq job on `place.coverage_missing` (monthly dedup key) | Semi. The lazy seed fires on a search miss with a user plus a trip destination or resolved place. | Brooklyn and Lisbon 2026-04/05. Cost $3–8 per city (runbook, 2026-05-10); lazy seed capped at about $80 per city worst case (`research_jobs.py`). | Could seed Manhattan neighborhoods unreviewed: travel-toned, draft dossiers, OSM hours only |
| Cursor-cheap (Method B) | `content/staging/<city>` briefs, dossiers, collections, then import scripts | Human pastes a `.cursor/tasks` prompt in the Cursor IDE; `import_cursor_dossiers.py` | Manual. Human review gates, **never via the API**. | 39 cities staged. Brooklyn tier 1–3 and dossier tasks exist locally. | Brooklyn is staged but ignored and not imported (§2.1) |
| Seed JSON pipeline (`tools/seed`) | Venues, briefs, hours, price, experiences, angles | Operator: validate, spot-check, promote, embed | Manual | Brooklyn Phase 2, 2026-05-12/13 | The source of today's Brooklyn DB content |
| World Foundry | Governed CityPacks, source observations, identities | Codex-subscription controller and workers; manual CLI (`world_foundry_queue.py`, `promote_world_foundry_city_pack.py`) | Manual, with strong gates | Riviera, Lisbon, Istanbul, Rome (§2.3) | No NYC CityPack |
| Place-content primitive lane | Accepted readings | Operator batches (`place_content_*_batch.py`) or the corpus adapter; independent reviewer required | Manual | 13 primitives, local only | Archived Red Hook corpus (§2.4) |
| Here/Season catalogs | Home world band rows | Hand-edited YAML plus the CI runway gate | Manual | September 23 edition | 3 NYC rows, expiring 10-09 |
| Event ingestion | `experiences` rows | `scripts/ingest_events.py` CLI or `seed_city_full` | No cron | 2 future events in total (2026-07-31) | None |
| Brief regeneration loop | Re-embedded dirty briefs | API lifespan loop, hourly, 20 per run | Automated | `DISABLE_LLM_BACKGROUND_LOOPS="false"` in `fly.toml` | Maintenance only; no new supply |
| GitHub cron | Promotes pending angles; publishes approved dossiers (daily) | `.github/workflows/cron.yml` | Automated, but only drains queues filled manually. Venue refresh, proactive refresh and cache purge are **dormant**. | Not verified (no run-history access) | None directly |
| Saved-place watch | Hours and operating-status refresh | Daily self-rescheduling task per user, 20 venues, forced paid fetch | Automated once seeded (`scripts/schedule_saved_place_reopen_scans.py`) | Unknown | Keeps a user's own saves fresh, **if** a provider key works |
| Places cache | open_now 10 min, hours 24 h, identity 7 d | Request-time or batch | Automated | — | Root Home/Places reads use `allow_provider=False`; they do not fetch live |
| Source contribution worker | One Sonnet-composed private "contribution" for Home or Places | **Explicit warm only** (`POST /api/agent-workflows/source-contribution`, from a "source.inspect" tap) | Dark: needs `ROOT_SOURCE_CONTRIBUTION_PRODUCTION_ENABLED`, `…_WORKER_ENABLED` and a named cohort; none is set in `fly.toml` | Disposable Postgres with a fixture producer only (2026-09-21) | Not public city supply by design (decision `docs/decisions/2026-09-06-bound-source-production-worker.md`) |
| Trip-scoped readings | Trip reading, "far-out read" | Itinerary commit, T-7, trip created or dated | Automated LLM, through `scheduled_tasks` | Unknown in production | Trip-only; nothing for ordinary days |
| Intake v2 | Source custody, extraction, place resolution, Life anchors | Share sheet, chat image, email webhook; six per-minute Arq crons | Automated once submitted | Legacy share path device-verified 2026-07-27; no v2 device receipt; email blocked | The main route by which user-owned NYC data enters |

### 3.2 How content moves from research to Home

A place reading reaches a Home screen only through this path:

```text
research (Cursor / Codex subscription / human)
  → staged artifact with sources (YAML or JSON)
  → validation (deterministic) → independent review receipt
  → explicit promotion (local; production-dogfood only with --allow-prod and authorization)
  → accepted, active, grounded, public PlaceContentPrimitive with valid_until
  → Home places_context reader: user's automatic Places context → place subtree → ≤ 6 records
  → HORIZON_EDITORIAL_PASSAGE candidate → app renderer
```

**Every arrow before "Home places_context reader" is manual today.** Nothing refreshes or expires-and-replaces readings on a schedule. The `valid_until` field simply causes expiry.

### 3.3 Intake v2 and place resolution (user-originated supply)

**Share sheet.** Built with `expo-share-intent` (text, one URL, up to 16 images or files), feeding `POST /api/intake/submissions` with object upload and interpretation resolve. The legacy `/api/inbound-items` route is kept for rollback.

- The legacy Phase 1 path was "shipped and device-verified (real Safari → share sheet → travel-app → Places … real Haiku extraction)" (`docs/working/unified-ingestion-research-2026-07-27.md`).
- **There is no v2 device receipt.** `intake_cutover_audit.py` hard-codes four production blockers:
  - custody receipt on the deployed migration and worker;
  - object-store permissions;
  - URL and audio provider delivery;
  - owner correction and deletion.
- `intake_production_canary.py` is plan-only by default, and no executed receipt was found.

**Email forwarding.** Each user gets a per-user alias, `{token}@import.vesper.trip`. The code is complete.

- It is blocked on a DNS MX record and SendGrid Inbound Parse setup (`backend/inbound/FEATURE.md`, 2026-08-22).
- Owner Action Items marks it "deferred … not blocking".
- **So receipt, ticket and booking emails cannot enter today.**

**Place resolution.** Implemented in `backend/inbound/place_resolution.py`:

1. Haiku extracts a place guess. Coordinates come only from JSON-LD, never from the LLM.
2. The resolver looks up external identity, then matches against the internal catalog within 100 m with fuzzy scoring.
3. If nothing matches, it creates a **provisional** venue or site, plus a review row when the match is ambiguous.
4. Without coordinates, it falls back to the city centroid.

There is **no Google or Foursquare call** in this path. In NYC outside Brooklyn, every shared place becomes a provisional row.

The supply implication cuts both ways:

- **Opportunity.** User shares grow the NYC catalog organically.
- **Risk.** Provisional rows carry no hours, photo or reading until something enriches them. The explicit object-page research path sits behind `ENTITY_RESEARCH_REQUESTS_ENABLED`, a spend canary that defaults off.

### 3.4 Refresh and expiry cadence

| Material | Validity mechanism | Refresh owner |
|---|---|---|
| Here/Season rows | `expires_at` per row (10-09); CI 14-day runway | Manual editorial, every 2–3 weeks |
| Place primitives | `valid_from`/`valid_until`; volatile evidence expires mechanically | Manual re-review; no scheduler |
| Venue hours and status | Cache TTLs (open_now 10 min, hours 24 h). Saved-venue daily scan. Upcoming-venue refresh cron is dormant. | Automated only for saved venues on trips, and only when keys work |
| Legacy briefs and angles | None. The May 2026 Brooklyn corpus has no expiry. | None. Closures were already observed in the hours skip logs. |
| Events | Ingest window of 90 days; no cron | Manual CLI |
| Source contributions | Short `expires_at`; request TTL 60–3600 s | Dark worker |

### 3.5 Costs (documented, not measured for NYC)

| Item | Figure |
|---|---|
| Legacy city seed | $3–8 per city, 3–8 hours (Data Pipeline Runbook, 2026-05-10); lazy seed worst case about $80 per city (cap of 1,500 LLM calls) |
| Brief warming | About $0.10 per brief |
| Background loops | About $1.75/day for one healthy user (`Background LLM Loops.md`, 2026-08-16) |
| Provider reference prices (2026-09-07 roadmap §7) | Google Details Enterprise $20/1k (1,000 free per month); Text/Nearby Pro $32/1k; Foursquare $15/1k after 500 per month; Tavily $0.008–0.016 per search; an illustrative bounded investigation about $0.14 |
| World Foundry and Cursor | Subscription-paid; no per-place dollar figure recorded |
| Receiving-path receipt | "No service price or production cost was measured" (`content-home-supply-execution-receipt-2026-09-08.md`) |

At these prices, raw provider cost is **not** the constraint for a single neighborhood. For example, 400 venues × 4 hours refreshes per month is about 1,600 Details calls, or roughly $12/month after the free tier. The constraints are:

- editorial review time;
- licensing and retention (Google `no_store`, Ticketmaster terms);
- broken or ambiguous provider configuration.

---

## 4. User and friend data as supply

### 4.1 What a user's own week produces

| User action | Status | Where it appears |
|---|---|---|
| Chat about places or taste; say your home city | Built. Observations are written in the same turn, which `docs/systems/contribution-and-consequence.md` §12 calls non-conforming. Home city is stored by the memory tool (`home:primary`, Nominatim) or `/api/me`. **Onboarding does not ask for it.** | Legacy Plans insight. Setting the home city moves Places context to "Home". Home v2 deliberately excludes memories. Life v1 has no memory input. |
| Save a place | Built, on by default | Plans card "Saved places / N saved in {city}"; Places saved section and page; Home v2 generic "Saved {type} / Ready to reopen…" row. **Not in Life** (gap confirmed by the NYC specimen §7). The daily saved-place watch refreshes status for up to 20 saves. |
| Share a link or screenshot from another app | Built (Intake v2 is the default for share-capture and chat images). **No v2 device receipt.** | Life (`intake_submission`, `source_submission` and anchor entries) and Places (a provisional venue or site when no catalog match exists) |
| Forward a booking or ticket email | Code-complete; **blocked on MX/SendGrid** | Would reach Life and Home action receipts |
| Create a trip or local plan | Trips built. Local Plans are internal-only (`LOCAL_PLAN_DOGFOOD_ENABLED`). | A trip takes over the Plans crown and Places context and unlocks trip-only producers: gap, friends, urgency, events preview. |
| Photos | Trip photos stay with trips. There is no photo search or retrieval path (`docs/working/life-human-refinding-code-audit-2026-09-01.md`). | Trip surfaces |

### 4.2 How a friend's material becomes supply for someone else

**Built and on:**

- **"From your people" in Places.** Shows a co-member's saves, but **only when the Places scope is a shared trip** (`backend/places/friends.py`).
- **Follow-graph feed.** Only in You → People.
- **Social circles.** Built.
- **Group trip proposals, votes and expenses.**

**Built but internal-only:**

- **The Home v2 "friends door".** Needs at least 2 unspent friend saves. Home v2 itself is internal.

**Built but dark (server flags default false):**

- Addressed place handoffs (`ADDRESSED_PLACE_HANDOFFS_ENABLED`).
- Recipient pulls (`PLACE_HANDOFF_PULL_ENABLED`).
- Exact-original deliveries to one person (`RELATIONSHIP_UUID_HANDOFFS_ENABLED`). The registry cohort says: "canonical_dogfood only after sender and recipient consent are device-verified".
- Story sharing.
- Profile-together projection.

**Design-only:**

- The friends audience: "Proposed, not adopted or implemented" (`docs/working/friends-audience-decision-proposal-2026-09-07.md`).
- Guest links for people without an account.
- Contributor invitations.
- Ongoing connection.
- Non-spatial shares on Home.

The shared fixture world shows all of these, as invented fixtures.

**Conclusion.** Friend-originated supply is **zero on day 1 by construction.** It stays near zero for a solo NYC user who has no shared trip, even after a week. It becomes meaningful only once dark handoff flags are lit **and** the user's friends are on the app. A launch-neighborhood plan should not count on it.

---

## 5. What a real NYC user sees

### 5.1 Build posture

**Default build tabs.** The default build (preview and production, `EXPO_PUBLIC_IS_INTERNAL_BUILD=false`) shows **Plans, Vesper, Places, Life**. It does not show "Home / Chat / Places / Life" (`travel-app/utils/fourRootShell.ts`).

**Four-root shell.** It appears only when all of these hold (`utils/productSystemRollout.ts`):

- `EXPO_PUBLIC_FOUR_ROOT_SHELL` is set;
- the build is development or internal;
- for the governed Home v2 and Places runtime, also `ROOT_PROJECTION_V2`, the Places renderer and `LIFE_ROOT_V1`.

**No EAS profile sets these**, not even `dogfood`. `eas.json` sets `EXPO_PUBLIC_IS_INTERNAL_BUILD=true` for four profiles and `false` for preview and production.

**Life is a permanent tab** (commit `a548d4d9f`, 2026-09-05). `docs/status/current-state.md` and `docs/flags/registry.yaml` still describe older shells and are stale on this point.

### 5.2 Day 1 in NYC, default build

| Tab | What fills it | NYC-specific? |
|---|---|---|
| **Plans** (Home slot) | `GET /api/concierge/home/trips-stack`. With fewer than 3 candidates, starter cards appear: "The year's still unwritten. Where are we going?", "Find something good close by", "Teach Vesper your taste", "Sketch a weekend away". All four just open Chat. **`near_you` cards are stripped in public builds.** | No |
| **Vesper** | Vesper Workbench: **Here** (3 real NYC exhibitions: 2 at NYBG in the Bronx, 1 at the Grolier Club in Manhattan), **Season** (US national parks), Route (dogfood-only, Duffel dark) | **Yes, but only the 3 Here rows, and they expire 2026-10-09** |
| **Places** | `build_places_feed` walks a context order: live or imminent trip → location reported in the last 15 min → recent return → `home_location` → future trip → "Anywhere". With no trip the posture is "starter": "NO TRIP YET / Start with what pulls you." Without location, the "Anywhere" starter shows the top 4 cities by dossier count, and **NYC is not guaranteed**. With location in Brooklyn, the nearby section reads the Brooklyn corpus (`allow_provider=False`; needs 2–4 hits). With location in Manhattan, Queens or the Bronx, **nearby is effectively empty**. | Brooklyn only, and only with location |
| **Life** | `GET /api/root-projections/v1/life`, reading the Experience Graph, intake anchors, retained sources and legacy Atlas. Empty state: "The record is still taking shape." | No |

### 5.3 Day 1 in NYC, internal and governed-rehearsal builds

**The `dogfood` EAS profile** adds near-you on Plans. For a Brooklyn location this surfaces Brooklyn corpus venues through a taste-ranked producer. Non-corpus candidates without a taste match are dropped, so a user with no history sees few or none. It also adds the Places reading spine, saved-unplaced views and local Plans.

**The governed rehearsal** (all four env vars on) adds Home v2 (`/api/root-projections/v2/home`) with ten readers:

- experience_graph
- legacy_plans
- plan_proposals
- **places_context (public place content)**
- explicit_saves
- action_receipts
- addressed_place_notes
- original_deliveries
- home_sample_demo_history
- contextual_places

For a cold NYC account:

- The world read is "Start anywhere".
- A cold-start invitation is promoted only when every non-world reader succeeds.
- **The public place-content reader returns nothing**, because there are no NYC primitives, and with `WORLDFOUNDRY_DOGFOOD_SERVING_ENABLED` on, release scope is required.
- The fictional "sample ticket" card needs `ROOT_DELIVERY_*` flags, which default off.

The program roadmap says so directly: the "populated New York field remains an explicit frontend rehearsal fixture; it is not production supply".

### 5.4 After a week of normal use (solo, no trip)

| Surface | What has accumulated |
|---|---|
| Plans | "Saved places / N saved in New York" cards. Starter cards drop away once there are at least 3 candidates. |
| Vesper | Unchanged: Here and Season. After 10-09, these bands are empty unless the catalog is renewed. |
| Places | Saved section. Brooklyn nearby rows if location is on. Provisional rows from shares. No readings. No events (the event preview is trip-only). |
| Life | Share and screenshot sources and anchors. Any Plans or Occasions if created. No saves, memories or email receipts. |
| Home v2 (internal only) | Generic saved-place continuity rows and own action receipts. No world readings. |

**Net.** After a week, the product is mostly a **well-organized mirror of what the user put in.** Vesper adds only 3 exhibitions and national-park seasons. Every "Vesper knows the city" promise in the design canon depends on supply that does not exist yet outside Brooklyn's legacy corpus.

---

## 6. Personas, fixtures and seeds: real vs synthetic

| Asset | People | Places | Events and facts | Photos | Where it lives |
|---|---|---|---|---|---|
| Canonical dogfood cast: Elif (home: Brooklyn), Mara (Lisbon), Dao, Reza, Mike, Sarah, Nadia (Budapest) | Synthetic (`@dogfood.local`); all Clerk-linked except Nadia | **Real catalog slugs** | Authored histories; trips dated 2025–26 | AI- or subscription-generated | `tools/dogfood/content/manifests/*`, `scenarios.yaml` |
| Elif's Brooklyn (brooklyn-phase1, W1) | Synthetic | Real: Bakeri, Sey Coffee, Paulie Gee's, Hotel Delmano, Greenpoint waterfront, Brooklyn Heights Promenade | 2025 "Brooklyn week"; seed events from 2026 are now past | 20 generated assets | Manifest; `sources/elif-canonical/brooklyn-anchor-map.md` |
| Local-occasions pack | Synthetic | Real (Paulie Gee's → Hotel Delmano) | "Friday, close to home", 2026-07-31, completed | — | `manifests/local-occasions-phase1.yaml` |
| Brooklyn right-now certifier | Elif | Real Paulie Gee's; representative geometry | **Controlled** clock, opening and route | — | `certify_brooklyn_right_now.py`; `runs/brooklyn.2026-08.demo-moments-01`. No recorded receipt found. DEMO-BEAT-02 is `blocked: [brooklyn_cloud_anchor_and_operational_receipts]`. |
| Brooklyn eval world | 10 synthetic travelers | **325 real venues** (README says 5 and is stale) | 27 events, partly AI placeholders, all past | None | `tools/eval/data/brooklyn/` |
| `seed_brooklyn_demo.py` and `scenario_setup_brooklyn.py` | Synthetic users and trips | Real slugs (Roberta's, Four Horsemen, Maison Premiere, Win Son, Brooklyn Museum…) | Authored itineraries | — | `travel-agent/scripts`, `tools` |
| Lena (root rehearsal) | Synthetic, in memory only | "ORDINARY_NYC / Brooklyn Saturday" situation | Authored | — | `tools/dogfood/content/root_rehearsal.py`; nothing written to a DB |
| HPL Home value review | "Two real accounts" (dao, lena) | — | `status: not_started`, `reviews: []` | — | `tools/dogfood/content/hpl-home-value-review.yaml` |
| Shared fixture world 2026-09-07 (Nora, Maya, Dana, Sam, Priya) | Invented | Invented ("The Print Room", Court Street apartment) | Invented week, Sep 17–20 | Stand-ins | `docs/working/fixtures/shared-fixture-world-2026-09-07.md`; **not seeded anywhere** |
| NYC newcomer specimen; NYC recommendation specimens (Governors Island, friend lunch, Saturday electronic, Art Cart) | Synthetic | **Real, sourced NYC venues** (researched 2026-09-07; target date 2026-09-12, now stale) | Real at research time | Referenced only | `docs/working/nyc-*-2026-09-07.md` |
| FE mock world | Synthetic (`home_city: 'Brooklyn'`) | Mock | Mock | Mock | `travel-app/constants/mocks` |

**Name collision.** The design's "Nadia" is Home Persona A, "The New Yorker". The backend's Nadia is a budget traveler in Budapest.

**Persona QA staleness.** `persona-qa/elif.md` (2026-06-29) is marked STALE. `mara.md` (2026-07-05) has a verdict of MIXED.

**No real person's NYC week exists in any seed.** The closest thing to real NYC data is the founder's own production account. It was not inspected, and should not be without explicit consent and scope.

---

## 7. Gaps, ranked by how much they block a real NYC user

1. **No reviewed NYC world readings on main.** The archived Red Hook set is 3 rows. The receiving pipe is ready; the supply is not.
2. **Operational freshness.**
   - Hours cover about 12% of Brooklyn venues and are 4+ months old.
   - The live-provider config is ambiguous: the Google key name and the deprecated Foursquare `/v3`.
   - Root reads are provider-free by design, so freshness must be prepared ahead of the read.
3. **No events producer for an ordinary week.** Ingesters are unscheduled and have known defects; the preview is trip-only; `happening_nearby` is off. Legal terms are unresolved.
4. **Here/Season will expire on 2026-10-09**, and the CI runway gate is already red.
5. **Geography.** No corpus exists outside Brooklyn. A Manhattan or Queens user gets nothing curated.
6. **Photos.**
   - No verified venue photos exist. Exact photos are Google live and `no_store`, and only for linked venues.
   - There is no NYC atmosphere manifest.
   - R2 is dormant.
   - Brooklyn illustrations are local only.
7. **The legacy corpus has the wrong register and no review state.** It is written for visitors ("your trip"), heavily restaurant-weighted, and missing everyday categories: grocery, libraries, parks, errands, gyms.
8. **User-supply pipes are partly dark.**
   - Email intake is blocked on DNS and SendGrid.
   - Share v2 has no device receipt.
   - Saves do not reach Life.
   - Friend handoffs are dark.
9. **The governed acceptance lane is currently hash-drifted**, so zero canonical lanes are accepted. Any new primitive corpus must start with a fresh independent review.
10. **Measured coverage and cost are absent.** No NYC run of `seeded_city_readiness`, `content_inventory_v2` or a DB inventory exists, and no production cost was measured.

---

## 8. Choosing a launch neighborhood

| Candidate | Existing assets | Everyday fit | Gaps |
|---|---|---|---|
| **Williamsburg + Greenpoint (North Brooklyn)** | 58 DB venues (W 49, G 9). About 100 staging briefs. **20 of the 38 hours rows.** 12 Qdrant angles (6 each). About 10 sites (McCarren Park, Domino Park, Greenpoint waterfront, Smorgasburg, Brooklyn Steel, Brooklyn Bowl…). Williamsburg place dossier. **All of Elif's anchors and the right-now demo location.** | Dense food, coffee, culture and waterfront; strong evening and weekend rhythm | Greenpoint is thin (9 venues). Everyday categories are missing. Briefs are nightlife-heavy and traveler-toned. |
| Park Slope (+ Prospect Heights) | 78 DB venues (56 restaurants), Park Slope place dossier with a `day_in` lens, Prospect Park and Grand Army Plaza Greenmarket, Brooklyn Museum | The most "ordinary life" neighborhood: market, park, library, brownstone errands | Only 4 hours rows. No Qdrant angles. No persona anchors. |
| Red Hook | **3 reviewed readings** (archived), place dossier, Pioneer Works, Waterfront Museum | Distinctive but small and isolated | Only 4 venues; a poor daily-use density |
| Founder's own neighborhood (if not one of these) | Unknown | Best dogfood realism, because the founder uses it daily | Everything must be built |

**Recommendation.** Use **Williamsburg + Greenpoint** as the first supported area.

- It has the most reusable facts and the only persona and demo anchors.
- Keep Park Slope as the second area.
- Land Red Hook readings as the corpus template.
- If the founder lives and uses the app elsewhere, pick that neighborhood instead. A supported area nobody on the team walks through daily cannot be dogfooded honestly.

This is a founder product decision. NYC is currently "an evaluation context, not an adopted launch geography" (`docs/working/home-connected-experience-implementation-map-2026-09-04.md`).

---

## 9. Supply plan for one NYC launch neighborhood

The plan below assumes Williamsburg + Greenpoint. It targets "ready value before personal history", the requirement in `recommendation-world-supply-architecture-and-roadmap-2026-09-07.md` §5.

### 9.1 Targets (what "supplied" means)

| Layer | Target for launch | Current (W+G) | Source of truth |
|---|---|---|---|
| **Entities** | 250–350 verified entities with canonical identity (Google Place ID or OSM), coordinates, category and operating status verified in the last 30 days. Mix: about 150 food and drink; 30 coffee and bakery; 15 parks, waterfront and public space; 30 culture (galleries, music rooms, cinema, bookstores, library branches); 30–50 everyday errands (grocery, market, hardware, pharmacy); about 10 transit anchors (G, L, J/M/Z stations, NYC Ferry landings) | 58 venues plus about 10 sites, unverified since May | Postgres venues and sites via World Foundry disposition |
| **Readings** | 30–50 accepted public primitives across 12–15 anchors, with at most one `opening_eligible` per cluster. Candidate anchors: Domino/sugar refinery reuse, Bushwick Inlet Park and the waterfront rezoning, McCarren Pool, Newtown Creek, Greenpoint's Polish-American main street, Kent Ave bike corridor, the Williamsburg Bridge, the Northside/Southside split, the Greenpoint Terminal Market, library branches | 0 (Red Hook: 3) | `place_content_primitives` plus `source_observations` |
| **Hours and status** | At least 90% of recommendable venues either (a) linked to a working provider for live hours with per-field TTL, or (b) official hours with `valid_until` ≤ 30 days. Otherwise the product makes **no** open-now claim. | 20 hours rows, from 2026-05 | Places cache plus refresh jobs |
| **Photos** | At least 30% of surfaced entities have a permitted real image (the readiness bar). An NYC area atmosphere manifest of 6–10 images. An illustration fallback everywhere else. | Effectively 0 | `media/policy.py` lanes |
| **Events and "Here"** | At least 3 current Here rows every day of a 14-day runway, city-wide plus at least 1 in the area. Plus 15–30 dated or recurring items per week in the area: markets, music rooms, cinema, library and gallery programs. | 3 city-wide rows expiring 10-09; 0 area events | `here_windows.yaml`; `experiences` table (curator and Ticketmaster sources) |
| **Season** | At least 3 rows that are actually NYC-relevant (fall foliage in Prospect and Central Parks, migratory birds at Jamaica Bay, the holiday market season) | 4 national-park rows | `season_windows.yaml` |

### 9.2 What to reuse

- **Brooklyn DB venues and local staging briefs.** Reuse facts, source URLs and identity only. Re-verify each row's operating status; closures already appear in the May skip logs. **Do not reuse the prose**: it is traveler-toned and unreviewed. Treat it as research leads for World Foundry.
- **The 12 Williamsburg/Greenpoint place angles and the Williamsburg `_place_` dossier.** Use as anchor and topic leads only.
- **The archived Red Hook corpus (`4254554cf`).** Land it as the NYC template: the source style, limits vocabulary and loader. It is also the first 3 NYC rows.
- **The Pier 57 and NYC newcomer specimens.** Use as known-answer probes and future Manhattan-waterfront candidates.
- **`load_nyc_ntas.py`** for neighborhood polygons, so "in the area" is spatially honest. **`seed_nyc_outer_places.py`** for missing Brooklyn neighborhood rows.
- **Elif's anchors and the right-now contract.** Use for dogfood demos, labeled controlled.

### 9.3 Pipeline to run, in order

Each step: (owner) — effort — what it produces. Effort figures are rough solo-founder estimates using subscription agents.

0. **Stop the bleeding.** Founder — 1–2 days.
   - Renew `here_windows.yaml` and `season_windows.yaml` with at least 6 source-checked NYC rows, and get `make vesper-world-catalogs` green.
   - Confirm the provider configuration:
     - the `PLACES_GOOGLE_API_KEY` name in Fly;
     - disable or migrate the Foursquare `/v3` key;
     - read the provider-canary snapshot;
     - check the Mapbox tokens.
1. **Land the Red Hook corpus.** Engineering — 0.5 day. Cherry-pick the three files, run its test and `--validate`, seed `red-hook` if missing, apply locally, run a fresh independent acceptance review, then production-dogfood with explicit authorization.
2. **Entity disposition and fill.** World Foundry — about 1–1.5 weeks.
   - `world_foundry_queue.py --city brooklyn --target local`, scoped to the Williamsburg and Greenpoint subtree.
   - Disposition every existing row: keep, repair, retype, rebind, merge or exclude. Several "sites" are actually cafés.
   - Add everyday categories from OSM (`seed_venues` for the two neighborhoods) plus official sources.
   - Link Google Place IDs with the backfill scripts.
   - Promote the CityPack locally, then production-dogfood with authorization.
3. **Readings.** World Foundry plus a place-content batch — about 1–2 weeks.
   - Research 12–15 anchors from official, government and institutional sources, following the Red Hook pattern.
   - Compile primitives; get independent review; apply.
   - Verify that Home's `places_context` surfaces them for a Williamsburg `home_location`, then check on a device.
4. **Hours and status freshness.** Engineering — 2–4 days.
   - Scope a neighborhood refresh job. The `refresh upcoming venues` cron is dormant, and saved-place watch covers saves only.
   - Store official hours with `valid_until`.
   - Keep Home and Places reads provider-free.
5. **Events.** Engineering plus curation — about 1 week, then 2–3 hours per week.
   - Repair the Ticketmaster ingester defects (timezone, 2099 dates, paging, currency).
   - Get legal and terms sign-off.
   - Schedule a bounded Brooklyn ingest.
   - Hand-curate recurring area items as `curator` experiences: markets, music rooms, cinema, library programs.
   - Decide whether Places and Home may show dated items outside a Trip. Today the preview producer is trip-only and `happening_nearby` is flagged off.
6. **Photos.** 2–3 days.
   - Create an NYC atmosphere manifest from Wikimedia, Pexels (area-only) or founder-shot images.
   - Decide on R2 for rehosting reviewed images.
   - Use the Google exact photo only as a live `no_store` view.
7. **User-supply pipes.** Owner plus engineering — 1–3 days.
   - Set the MX record and SendGrid Parse so email intake works.
   - Record a v2 share-sheet device receipt.
   - Decide whether saves should reach Life.

**Total.** About 4–6 weeks to a first supported area. Ongoing, about 3–5 hours per week:

- Here and event curation;
- monthly status re-verification;
- re-reviewing expiring primitives.

**Direct provider spend** for one area is small: tens of dollars per month at published prices. **Editorial time is the binding cost.**

### 9.4 Quality gates, all of which already exist

**Area-level readiness:**

- `python -m tools.dogfood.seeded_city_readiness --place williamsburg` (and greenpoint). Critical thresholds: at least 50 venues, 70% briefs, 50 Qdrant briefs, 12 angles. The bar is travel-shaped; add everyday-category and hours thresholds.
- `content_inventory_v2` against the target DB (authorized). The primitive and observation counts by review and lifecycle state must match the plan.

**Content acceptance:**

- `tools.dogfood.content.runtime_acceptance` must accept the new canonical lane, not 0.
- World Foundry lifecycle: independent cross-review, target fingerprint, and a promotion receipt per run. Production writes only with `--allow-prod` and founder authorization.

**Catalog runway:**

- `check_vesper_world_catalogs.py --runway-days 14` stays green in CI.

**Receiving path and consumer value:**

- `certify_brooklyn_home_runtime.py` and `certify_brooklyn_right_now.py` with real, not controlled, opening data where claimed.
- The HPL Home value gate on two real accounts (`hpl_home_value_gate.py`).
- A native device walk of Home → reading → Places → back.

**Honesty checks:**

- No open-now claim without a current observation.
- No event without a local date and timezone.
- Every reading carries a source and `valid_until`.
- Unsupported areas say so rather than showing starter filler.

---

## 10. Decisions this inventory surfaces for the founder

1. **Is NYC the launch city, and which neighborhood?** It is currently "an evaluation context, not an adopted launch geography".
2. **Foursquare: migrate or replace?** And which Google key name is actually deployed?
3. **Events.**
   - Are dated items allowed on Places and Home outside a Trip?
   - Which sources are legally acceptable (Ticketmaster commercial terms; RA and DICE partnerships; curator-only)?
4. **Here/Season ownership.** Who renews the catalog every 2–3 weeks? Should the pilot rows be neighborhood-scoped rather than NYC-wide?
5. **Photos.** Activate R2 for rehosted reviewed images, or stay illustration-first?
6. **Legacy Brooklyn corpus.**
   - Import the 109 staging-only rows through World Foundry disposition, or leave the corpus frozen?
   - Should traveler-toned briefs keep serving in Chat and Places at all?
7. **Default-build posture.** The default build's Home slot is "Plans" with generic starters and no near-you. Should a supported-area newcomer see world supply in the **default** build, or only after the four-root shell ships?

---

## Appendix A. Where to look first

| Topic | Paths |
|---|---|
| Staging and seeds | `travel-agent/content/staging/README.md`; `.gitignore:76-100`; `tools/seed/README.md`; `tools/seed/staging/_promoted/`; `tools/eval/data/brooklyn/` |
| World Foundry and readings | `docs/operations/World Foundry.md`; `tools/seed/staging/runs/`; `backend/core/{models,db}/place_content.py`; `docs/operations/content-runtime-acceptance.md`; archived `4254554cf` |
| Home world and receiving | `backend/home/vesper_workbench/data/`; `scripts/check_vesper_world_catalogs.py`; `backend/root_projection/v2/home_portfolio.py`, `home_source_adapters.py` |
| NYC geography | `alembic/versions/nycplace01_*`; `scripts/seed_nyc_outer_places.py`; `scripts/load_nyc_ntas.py` |
| Events and providers | `backend/ingestion/`; `backend/places/{factory,settings,cache,saved_place_watch}.py`; `backend/core/weather_provider.py`; `backend/media/policy.py` |
| Intake and contribution | `backend/api/routes/{intake,inbound_email}.py`; `backend/inbound/place_resolution.py`; `backend/root_projection/v2/source_contribution_*.py`; `docs/decisions/2026-09-06-bound-source-production-worker.md` |
| Strategy | `docs/working/recommendation-world-supply-architecture-and-roadmap-2026-09-07.md`; `content-home-supply-execution-receipt-2026-09-08.md`; `cold-start-and-everyday-places-experience-mvp-2026-07-31.md` |

## Appendix B. Evidence status legend used above

| Label | Meaning |
|---|---|
| Executed 2026-09-26 | The catalog checker, `content_inventory_v2 --repo-only`, the archived corpus `--validate`, `git apply --check`, and file parsing |
| Dated doc observation | DB row counts (2026-05 and 2026-07-31), provider key presence (2026-07-09), `photo_urls` NULL (2026-07-31) |
| Not verified | Production and dev DB and Qdrant contents, Fly and EAS secrets, GitHub Actions history, device rendering, provider health |
