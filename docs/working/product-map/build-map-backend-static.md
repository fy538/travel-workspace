---
doc_type: working
status: active
owner: Claude orchestrator (product map)
created: 2026-09-26
expires: 2026-10-26
why_new: No single evidence-based inventory existed of what the backend has built (live, dark, backend-only, legacy) and what should be deprecated; this static map feeds the founder's product map.
promotes_to: null
supersedes: []
---

# Backend build map — static inventory (travel-agent @ `c8c9f5785`)

**Evidence boundary.** Static reading only, 2026-09-26. Code: merged baseline
`/Users/feihuyan/travel-workspace--product-map-inventory/travel-agent` at `origin/main` = `c8c9f578594a` (clean), and
workspace `6ef3dca` (`docs/openapi.json`, `docs/openapi.app.json`, `docs/governance/api-operation-policy.json`,
`docs/flags/registry.yaml`). Read-only scripts run: Python parsing of the OpenAPI/policy/registry files, AST parsing of
`feature_flags.py`, `_tables`, Alembic revisions, and the repository's own `scripts/api_contract_audit.py --json`
(passes). **Not done:** no server, database, test run, device, Fly secret or EAS dashboard inspection — every
"production" statement means "as committed in `fly.toml` / code defaults", and Fly secrets can override it.
Several sections were fanned out to read-only helper agents; their key claims that carry a verdict were re-read by
the orchestrating agent and are marked "verified"; the rest is reported as helper evidence with file:line so it can be
re-checked. Mobile "caller" data comes from the audit's method-level discovery and has false negatives.

**Active Codex lane (not merged, not modified):** `/Users/feihuyan/travel-workspace--home-value-delivery/travel-agent`
on `codex/home-value-delivery`, 3 commits over `origin/main`: `6c792ed8b` (offline/replay `AI_MODE` no longer requires
`ANTHROPIC_API_KEY` at startup, `api/lifecycle.py`), `8fbad4db7` and `bf1e5dadf` (Home v2 cold-start sample card
wrapped in a value contract via `with_value_contract`, and allowed to coexist with the automatic Places-context door;
`root_projection/v2/home_portfolio.py`, +116 test lines). Uncommitted edits there touch
`scripts/provision_places_source_field_rehearsal.py` and its test. None of it changes the classifications below.

## 0. Executive summary

1. **Two products share one backend, and production users see the old one.** 574k LOC in `backend/` (37 packages).
   Roughly 86k LOC is purpose-built for the four-root system (Home / Places / Life / Chat + People), ~75k LOC serves
   the legacy trip product directly, and the ~410k LOC shared layer (`core/` alone is 237k) is heavily trip-shaped.
   No `eas.json` profile sets `EXPO_PUBLIC_FOUR_ROOT_SHELL`, so shipped builds render `LegacyTripsHome` and
   `PlacesWorkspace` backed by `backend/home/` and `/api/places/feed`; `root_projection/` is exercised only by
   dev/internal rehearsal builds.
2. **The four-root read endpoints are not server-gated.** Every `/api/root-projections/*` read is served to any
   authenticated user; "dark" is an app-side decision. Only consequence resolve/repair are flag-gated.
3. **API surface: 655 operations (592 paths); 503 in the mobile projection; 475 with a detected mobile caller.**
   By class: NEW-PRODUCT 106, SHARED 151, LEGACY-KEEP 203, LEGACY-RETIRE 139, INTERNAL 56. 62 are `retiring`
   (61 of them have no product caller), 15 `dark`, **17 are past their policy `review_by`**, and 55 more come due
   2026-10-07. Atlas is "retired" in flags but 45 of its 49 ops still have callers (its screens now live under `/you` "Memories").
4. **Flags: 77 env names in `feature_flags.py`, ~45 behavior-changing toggles are unregistered** (incl. default-on
   intake v2 switches, `BOOKING_EXECUTION_RETIRED`, `AI_MODE`, 9 producer families); 30 registry rows expire
   2026-10-04; a deleted flag is still `active` in the registry and cited by the API policy; `fly.toml` still sets
   `ATLAS_LLM_ENABLED=true` for a hard-disabled function.
5. **Background work:** 27 arq crons (23 on), ~13 per-minute ticks, ~30 lifespan loops, 34 subscriber modules, ~20 scheduled-task kinds.
   Legacy-trip LLM work (proactive, digest, pre-trip, story, narration, Takes, trip reading, transport nudges) runs by
   default; the LLM kill switch misses the worker and most subscribers; `seed_city_full` has a ≈$800/day ceiling
   triggered from empty chat searches; **booking execution is still admitted** (`BOOKING_EXECUTION_RETIRED`
   defaults false and is not set in `fly.toml`).
6. **Data: 317 tables** (283 core + 27 graph + 7 relationships; the 34 domain tables are outside Alembic drift
   checks), 477 migrations, one head. **Identity is fragmented:** Trip vs graph Plan vs graph Occasion have no
   row-level bridge (graph `plans` has no `trip_id`; block adoption drops venue and plan); ~12 place id schemes; two
   provider ledgers; two handoff generations; two intake pipelines; Life reads Atlas timeline rows as its only trip
   bridge.
7. **Capability vs design:** Home v2 defines 36 unit kinds (canon 35), produces 22 (4 dark), 14 unimplemented;
   Places v2 emits 14 of 34 kinds and never leaves `WORLD_FIELD`; Life's Featured Return and returns arbitration are
   unimplemented; relationships/originals/pulls are built but dark; the source-contribution worker (~8k LOC) is dark;
   T0/T1/T2 contribution policy is **designed but computed only in shadow** — ~19–20 chat paths write durable state
   without a confirmation.
8. **Risks (§8):** source-contribution pipeline ignores the sender's inference permission (R1) and admits pair notes
   for GROUP audience, locked in by a test (R2); relationship kill switch misses Home, Places friends, source
   synthesis and the consequence gateway (R3); "nearby only" precision bypass (R4); model-settable location sharing
   (R7); private member material into trip-shared briefs (R8); accommodation → shared expense (R9); booking execution
   admitted (R13); incomplete LLM kill switch (R14).
9. **Deprecation (§7):** Tier 0 zero-risk deletes now; Tier 1 booking execution (set the retirement flag first),
   Discover, `lookup_agent`, legacy place handoffs, guest links, Takes surfaces, legacy trip messages, location
   sharing; Tier 2 legacy Home (after the four-root shell ships), the Atlas product surface (keep timeline for Life),
   narration/voice guide, follows, legacy research writeback, intake v1.

## 1. Domain map — every backend package

LOC = non-test Python lines under `backend/<pkg>` at `c8c9f5785` (`find -name '*.py' | xargs cat | wc -l`).
"Tests" = test files / test functions in the matching `tests/<dir>` plus the number of test files anywhere that
import the package. Whole backend: **574,342 LOC** in `backend/`, **2,008 test files / 20,369 test functions**
under `tests/`, **478 Alembic migrations**.

Status legend: **CORE-NEW** = built for the four-root system (Home / Places / Life / Chat + People);
**CORE-SHARED** = infrastructure both products depend on; **LEGACY-ACTIVE** = serves the shipped trip product and
is still reached by the app; **LEGACY-DORMANT** = present, wired, but no production traffic by default;
**RETIRE-CANDIDATE** = no remaining product need, or already on a retirement path.

| Package | LOC | Tests (dir files/fns · importers) | Purpose (verified) | Surface / root served | Status | Key gates |
|---|---:|---|---|---|---|---|
| `api` | 59,139 | 161/2,511 · 256 | FastAPI app, 118 route modules, lifespan loops (`api/lifecycle.py`), auth, rate limits | all | CORE-SHARED | `DISABLE_API_BACKGROUND_TASKS`, `DISABLE_LLM_BACKGROUND_LOOPS` |
| `application` | 4,608 | 1/3 · 20 | Cross-domain use cases: `root_composition.py` (1,001), `portfolio_reads.py`, `canonical_owner_reads.py` (1,838), relationship openings, semantic catalog | Home / Places root composition | CORE-NEW | `ROOT_DELIVERY_PROJECTION/SUPPRESSION`, `ROOT_SOURCE_CONTRIBUTION_PRODUCTION`, `LIVED_EXPERIENCE_CONSEQUENCE_RESOLUTION` |
| `atlas` | 6,653 | 45/429 · 46 | Past-trip photo backfill, timeline, taste boards, "Unpacked" recap, postcards | Atlas tab now redirects to Life (`app/(tabs)/atlas/index.tsx:668`), but `app/atlas/*` screens are re-exported under `/you` ("Memories": scan, candidates, artifacts, unpacked, boards) + **Life reads Atlas timeline rows** (`api/routes/root_projections.py:254`) | LEGACY-ACTIVE (composer/boards RETIRE-CANDIDATE; timeline must stay until Life has its own corpus) | `atlas_llm_enabled()` hard-`False`; `ATLAS_SIGNALS_TO_MEMORY` (**on** in fly.toml); `ATLAS_SEMANTIC_READ/WRITE`; unregistered `ATLAS_BOARD_COPY_LLM_ENABLED` |
| `booking_agent` | 15,467 | 53/456 (`tests/booking`) · 66 | Provider sessions, offers, Duffel holds, checkout, restaurant dispatch (Bland/Twilio), affiliate links, readiness | Legacy trip product booking; `/api/trips/{id}/booking/*` | LEGACY-ACTIVE → RETIRE-CANDIDATE (execution) | `BOOKING_EXECUTION_RETIRED` (default **false**, unregistered, not in fly.toml), `BOOKING_DUFFEL_LIVE_BOOKING_ENABLED`, `BOOKING_OPENTABLE_ENABLED` |
| `composition` | 1,761 | 3/56 · 4 | "Corpus-agnostic" board assembly; only importer is `atlas/taste_board.py` (Discover consumer retired 2026-07-03) | Atlas taste boards | RETIRE-CANDIDATE (with Atlas boards) | `ATLAS_BOARD_COPY_LLM_ENABLED`, `DISABLED_SURFACES` |
| `concierge` | 78,570 | 199/3,132 · 256 | Conversational agent: prompts, `tool_handlers/` (18,247), `agentic_facade/` (1,713), proactive loop, entry context | Chat root + legacy trip chat, voice | CORE-SHARED (large legacy trip-planning share) | `CONCIERGE_*` modes, `FACTS_WRAPPER_ENFORCE`, context-compiler flags |
| `core` | 237,434 | 596/5,247 · 1,323 | Everything shared: `db/` (100,874 incl. `_tables` 17,664), `models/` (24,416), `vector/` (15,357), ~60 `itinerary_*`/`trip_*`/`booking_*` gateways, flags, LLM client | all | CORE-SHARED (≈40% trip-product specific) | `feature_flags.py` (897 lines) |
| `digest` | 2,906 | 4/80 · 4 | Daily/planning digests via LLM, markdown/HTML render | legacy trip digests: 6-hourly Haiku loop feeds legacy Home/reflection; `GET /digests` reaches only unused hooks; `/digest/email` retiring | LEGACY-ACTIVE (loop) / API RETIRE-CANDIDATE | `DISABLE_LLM_BACKGROUND_LOOPS` |
| `discover` | 2,063 | 8/62 · 9 | Discover feed composition | Discover tab is `href: null` (`app/(tabs)/_layout.tsx:90-95`); `/api/discover/feed` and `/trending` have data-layer hooks but no screen consumer (`useDiscoverSectionedFeed` is only re-exported); package survives as personalization cache/metrics helpers | RETIRE-CANDIDATE | — |
| `domains/experience_graph` | 8,215 | 12 dir files (shared) · 39 | Clean-break Plan / Occasion / Commitment / Outcome / Anchor / Opening graph; 28 tables in `schema.py` | Home v1/v2, Life, Occasion flows | CORE-NEW | — (API mostly `server` audience) |
| `domains/relationships` | 4,282 | (shared) · 18 | UUID handoffs, original deliveries, pull grants, pair conversations; 7 tables | People / Home people rows | CORE-NEW (dark) | `RELATIONSHIP_UUID_HANDOFFS_ENABLED`, `PLACE_HANDOFF_PULL_ENABLED` |
| `expenses` | 1,214 | 11/127 · 13 | Settlement, FX, receipt OCR (LLM), accommodation cost | trip expenses | LEGACY-ACTIVE (retained per capability-retirement plan) | — |
| `guide` | 1,118 | 6/76 · 8 | Narration content infra (standalone Guide agent deleted) | legacy narration / voice bridge | LEGACY-DORMANT | — |
| `home` | 17,904 | 50/638 · 66 | Legacy Trips-Home: `concierge_feed/` (5,763), `vesper_workbench/` (2,882), `trip_reading/`, `farout_read/`, per-trip `feed.py` | **Default Home in every build** (`LegacyTripsHome` when `EXPO_PUBLIC_FOUR_ROOT_SHELL` unset; no EAS profile sets it) | LEGACY-ACTIVE | `HOME_TASTE_SEARCH_ENABLED` (false in fly), `HOME_AGENT_LOOP_ENABLED`, `TRIPS_SAVED_UNPLACED_ENABLED`, `CONCIERGE_EXPOSURE_FATIGUE_ENABLED` |
| `inbound` | 5,786 | 37/214 · 41 | Share/screenshot/email/audio intake; custody-first Intake v2 envelope, anchors, semantic interpretation | Capture across roots | CORE-NEW (v2) + LEGACY-ACTIVE (v1 inbound items) | `INTAKE_V2_EMAIL_ENABLED`, `INTAKE_V2_CHAT_IMAGE_ENABLED` (default **on**, unregistered) |
| `ingestion` | 1,689 | 5/64 · 5 | Ticketmaster / Bandsintown / Viator / Amadeus event ingestion | only `api/routes/admin.py` | LEGACY-DORMANT (operator-only) | — |
| `invites` | 409 | —/— · 1 | Signed-out invite projection | trip invites landing | LEGACY-ACTIVE | — |
| `life` | 992 | 3/28 · 3 | `refind_sources()` over legacy itinerary + booking rows | Life refind (`POST /api/life/refind`) | CORE-NEW surface on LEGACY data | app `EXPO_PUBLIC_LIFE_REFIND_LANE` |
| `life_projection` | 10,906 | 54/318 · 52 | Viewer-relative Life corpus/index/organization projectors | Life root (`/api/root-projections/v1/life*`) | CORE-NEW | — (app `EXPO_PUBLIC_LIFE_ROOT_V1`) |
| `lived_experience` | 17,473 | 6/31 · 85 | Engine seam: admission → treatment → consequence grant → readback; producers, exposure, presentation signing | Home/Places/Chat consequences | CORE-NEW (almost entirely dark) | 9 `LIVED_EXPERIENCE_PRODUCER_*`, `LIVED_EXPERIENCE_SURFACE_*`, `..._CONSEQUENCE_RESOLUTION`, `..._DARK/SHADOW_WORKER` |
| `lookup_agent` | 1,689 | 5/61 · 6 | Real-time entity lookup + Qdrant cache + synthesis | only `api/routes/lookup.py` (`POST /api/lookup/` retiring, no app caller) | RETIRE-CANDIDATE | `LOOKUP_SYNTHESIS_ENABLED` |
| `media` | 2,029 | 11/78 · 19 | Photo rehost, variants, hashing, storage | all imagery | CORE-SHARED | — |
| `notifications` | 11,756 | 40/651 · 53 | Arbiter, delivery spine, push/email dispatch, leave-by, receipts reaper | all roots + legacy trips | CORE-SHARED | `EXPO_PUSH_ENABLED`, `NOTIFICATION_*` |
| `places` | 14,820 | 70/611 · 88 | Places feed/sections, discovery, taste, registers, comparison, provider status | Places root and legacy `PlacesWorkspace` | CORE-SHARED | `PLACES_*`, `SPATIAL_REACHABILITY_NEARBY_ENABLED`, `NEARBY_TRAVEL_TIME_RANKING_ENABLED`, `PLACE_CONTENT_PRIMITIVE_READS_ENABLED` |
| `planning_agent` | 10,361 | 29/432 (`tests/planning`) · 55 | Itinerary generation with tool calling, restaurant sub-agent | legacy trip planning via Concierge | LEGACY-ACTIVE | `PLANNING_*`, `PLANNER_SEMANTIC_RANKING` |
| `postcard` | 294 | 3/21 · 3 | img2img riso postcard | Atlas only | LEGACY-DORMANT (ships dark) | `POSTCARD_RENDER_ENABLED` |
| `preference_engine` | 1,855 | 7/99 (`tests/preferences`) · 9 | Observations → Personal Memory synthesis, group profiles | Chat/planning context | CORE-SHARED | — |
| `research_agent` | 17,906 | 55/651 · 61 | LangGraph deep research → dossiers/briefs | content pipeline behind Place pages, Discover, Takes | LEGACY-ACTIVE (internal content supply) | `AUTO_PUBLISH_GREEN_DOSSIERS`, `LEGACY_RESEARCH_WRITEBACK_ENABLED` (default **on**, unregistered) |
| `root_projection` | 18,010 | 35/419 · 49 | v1 compiler + v2 pipeline (17,434): Home portfolio, adapters, **source contribution (~8,000 LOC, 16 files)**, delivery exposure | Home/Places roots | CORE-NEW | `ROOT_*`, `WORLDFOUNDRY_DOGFOOD_SERVING_ENABLED`, relationship flags |
| `scripts` | 722 | 67/513 (`tests/scripts`) | Backfills / parity checks | ops | INTERNAL | — |
| `search` | 1,383 | 6/91 · 8 | Hybrid keyword+semantic search, RRF, LLM interpretation | universal search | CORE-SHARED | — |
| `situation` | 1,981 | —/— · 2 | During-trip situation read model | `GET /trips/{id}/situation`, narration | LEGACY-ACTIVE | — |
| `social_state` | 1,026 | 3/36 · 6 | Group dynamics for tone | group trip chat | LEGACY-ACTIVE | — |
| `tasks` | 1,956 | 9/114 · 12 | Trip completion, Trip Story, The Letter, occasion reconcile | legacy trips / story | LEGACY-ACTIVE | `DISABLE_LLM_BACKGROUND_LOOPS` |
| `voice` | 2,187 | 9/174 · 11 | LiveKit STT→LLM→TTS worker | voice companion | LEGACY-DORMANT (fly `voice` group count 0, needs 6 `VOICE_*` secrets; app `EXPO_PUBLIC_VOICE_ENABLED` true only on the `dogfood` EAS channel) | `VOICE_*` secrets, app `EXPO_PUBLIC_VOICE_ENABLED` |
| `workers` | 6,526 | 20/107 · 33 | arq worker (`audio_jobs.WorkerSettings`) + job modules | all | CORE-SHARED | see §4 |
| `world_foundry` | 1,248 | 6/21 · 10 | Promotion of reviewed World Foundry artifacts; dogfood release | Places/Home content | CORE-NEW (dark) | `WORLDFOUNDRY_DOGFOOD_SERVING_ENABLED` |
| `folio` | 0 | — | Deleted in `5901be82f` ("Retire legacy Folio and Change Studio routes") | — | RETIRED | — |

**Roll-up by status (LOC, approximate):** CORE-NEW ≈ 86k (application, experience_graph, relationships,
life, life_projection, lived_experience, root_projection, world_foundry, inbound-v2 share);
CORE-SHARED ≈ 410k (core, api, concierge, places, notifications, media, search, preference_engine, workers);
LEGACY-ACTIVE ≈ 75k (home, booking_agent, planning_agent, research_agent, atlas, expenses, tasks, situation,
social_state, invites); LEGACY-DORMANT / RETIRE-CANDIDATE ≈ 13k (digest, discover, composition, guide, ingestion,
lookup_agent, postcard, voice). The shared layers hide most legacy mass: `core/` alone carries ~60 top-level
`itinerary_*`, `trip_*` and `booking_*` modules and `core/db/trips/` (5,683 LOC).

## 2. API map

**Method.** `docs/openapi.json` parsed per operation (GET/POST/PUT/PATCH/DELETE); `docs/openapi.app.json` = the
generated mobile projection; lifecycle/audience/flag/review from `docs/governance/api-operation-policy.json`
(`defaults` = app/active + 283 explicit entries + 2 `retired_operations`); "mobile caller" = a data-layer or
component caller discovered by the repository's own `scripts/api_contract_audit.py::discover_mobile_consumers`
(run read-only; the audit itself **passes**: 579 active, 15 dark, 62 retiring). Caller detection is method-level and
has false negatives (e.g. the Places root runtime read is consumed via `travel-app/data/rootProjections.ts` but
shows as transport-only) and false positives (a data-layer hook with no screen consumer counts as a caller — e.g.
`/api/discover/feed`, `GET /api/concierge/home`, `GET /digests`, `DELETE /stay-vote`). A helper's screen-level
import graph found 508 ops with an app client method, 482 with at least one first-level caller, and 96 `/api` ops
with no client method at all.

**Totals.** Full snapshot: **592 paths / 655 operations**; app projection: **457 paths / 503 operations**; mobile
caller detected for **475** operations. By policy: app 547 (active 492, retiring 55, dark 13) · server 45 (active 36,
retiring 7, dark 2) · operator 32 · infrastructure 13 · webhook 4 · public_web 1. **17 operations have an expired
`review_by`** (12 dated 2026-09-03: the 6 `OUTCOME_ARTIFACT_ENABLED` trip occurrence/second-occasion ops and 6
`SOCIAL_CIRCLES_ENABLED` circle ops; 5 dated 2026-09-12: 4 conversation participant/owner-handoff/event ops and
`GET /api/trips/{id}/messages/events`, all under `GROUP_TRIP_MICRO_JOURNEY_ENABLED`). **55 more come due
2026-10-07** (almost all the retiring set). The audit script does not fail on expired review dates.

**Roll-up by class (my classification, per family below):**

| Class | Ops | In app proj. | Mobile caller | Retiring | Dark |
|---|---:|---:|---:|---:|---:|
| NEW-PRODUCT (four-root, People, intake v2, Chat transport, events) | 106 | 79 | 66 | 2 | 3 |
| SHARED (users/me, conversations, places, search, notifications, circles, catalog reads) | 151 | 138 | 132 | 9 | 4 |
| LEGACY-KEEP (shipped trip product still in use; incl. legacy Home, invites, inbound v1) | 203 | 185 | 181 | 13 | 4 |
| LEGACY-RETIRE (Atlas, Discover, dossiers/takes/angles/sites, lookup, booking, legacy trip messages, narration, voice guide, location sharing, geofence, legacy handoffs, follows, guest links) | 139 | 98 | 94 | 38 | 3 |
| INTERNAL (admin, metrics, health, debug, webhooks, curator) | 56 | 3 | 2 | 0 | 1 |

**Governance anomalies.**
* 11 operations are in the app projection although their policy audience is not `app`: 8 experience-graph occasion
  invitation/decision/vote ops and `POST /api/relationships/pair-conversations` are `server` but the app calls them;
  `GET /admin/ops/ai-status` and `/admin/dogfood/preflight` are `operator` with an internal-app consumer.
* 27 experience-graph operations are labelled `server`; 8 are actually called by the app (above) and the other 19
  (create/update plan, plan relations, openings, create/leave/transfer occasion, commitments, execution tasks,
  provider/occurrence evidence, outcomes) list the route function itself as their "consumer" (`create_plan_route`,
  `create_occasion_route`, …) — write APIs with **no real caller**. Graph Plans/Occasions are therefore populated
  almost only through adapters (trip-block adoption, intake anchors, handoff openings).
* Stale/mislabelled flags cited by policy — see §3c.

### 2a. Per-family table (families with ≥3 operations; smaller ones summarized)

| Family | Ops | In app proj. | Mobile caller | Audience | Lifecycle | Review expired | Class | Policy flags |
|---|---:|---:|---:|---|---|---:|---|---|
| `users` | 50 | 44 | 44 | app 50 | active 44, retiring 5, dark 1 |  | SHARED | `SOCIAL_CIRCLE_AGENT_CONTEXT_ENABLED` |
| `atlas` | 49 | 45 | 45 | app 49 | active 45, retiring 4 |  | LEGACY-RETIRE (keep timeline reads for Life) |  |
| `experience-graph` | 37 | 18 | 15 | server 27, app 10 | active 37 |  | NEW-PRODUCT |  |
| `/admin` | 34 | 2 | 1 | operator 30, server 4 | active 34 |  | INTERNAL |  |
| `trips/{id}/booking` | 34 | 31 | 29 | app 34 | active 31, retiring 3 |  | LEGACY-RETIRE execution / KEEP evidence reads | `BOOKING_DUFFEL_LIVE_BOOKING_ENABLED` |
| `trips/{id}/itinerary` | 31 | 26 | 26 | app 31 | active 26, retiring 5 |  | LEGACY-KEEP |  |
| `me` | 29 | 29 | 29 | app 29 | active 29 |  | SHARED | `ENTITY_PROVIDER_RESOLUTION_ENABLED` |
| `conversations` | 27 | 24 | 21 | app 27 | active 24, retiring 3 | 4 | SHARED | `GROUP_TRIP_MICRO_JOURNEY_ENABLED` |
| `relationships` | 16 | 13 | 12 | app 12, server 4 | active 13, dark 2, retiring 1 |  | NEW-PRODUCT | `PLACE_HANDOFF_PULL_ENABLED`, `RELATIONSHIP_UUID_HANDOFFS_ENABLED` |
| `trips/{id}/story` | 16 | 16 | 15 | app 16 | active 16 |  | LEGACY-KEEP |  |
| `social-circles` | 15 | 13 | 12 | app 15 | active 13, dark 2 | 6 | SHARED (People) | `PROFILE_TOGETHER_PROJECTION_ENABLED`, `SOCIAL_CIRCLES_ENABLED`, `SOCIAL_CIRCLE_AGENT_CONTEXT_ENABLED` |
| `trips/{id}/expenses` | 15 | 11 | 11 | app 15 | active 11, retiring 4 |  | LEGACY-KEEP |  |
| `intake` | 14 | 11 | 8 | app 11, server 3 | active 13, retiring 1 |  | NEW-PRODUCT |  |
| `places` | 12 | 10 | 9 | app 12 | active 10, retiring 1, dark 1 |  | SHARED | `NEARBY_TRAVEL_TIME_RANKING_ENABLED`, `PLACES_SECTIONS_ENABLED` |
| `root-projections` | 10 | 10 | 7 | app 10 | active 10 |  | NEW-PRODUCT | `EXPO_PUBLIC_FOUR_ROOT_SHELL`, `EXPO_PUBLIC_ROOT_PROJECTION_V2`, `LIVED_EXPERIENCE_CONSEQUENCE_RESOLUTION_ENABLED` |
| `trips/{id}/narration` | 9 | 7 | 6 | app 9 | active 7, retiring 2 |  | LEGACY-RETIRE |  |
| `dossiers` | 8 | 5 | 5 | app 8 | active 5, retiring 3 |  | LEGACY-RETIRE |  |
| `trips/{id}/proposals` | 8 | 6 | 6 | app 8 | active 6, dark 2 |  | LEGACY-KEEP | `GUEST_PROPOSAL_CAPABILITIES_ENABLED` |
| `pending-chat-turns` | 7 | 7 | 5 | app 7 | active 7 |  | NEW-PRODUCT | `PENDING_CHAT_TURNS_ENABLED` |
| `trips/{id}/members` | 7 | 6 | 6 | app 7 | active 6, retiring 1 |  | LEGACY-KEEP |  |
| `trips/{id}/photos` | 7 | 6 | 6 | app 7 | active 6, retiring 1 |  | LEGACY-KEEP |  |
| `/metrics` | 6 | 0 | 0 | infrastructure 6 | active 6 |  | INTERNAL |  |
| `place-handoffs` | 6 | 1 | 1 | server 5, app 1 | retiring 5, active 1 |  | LEGACY-RETIRE (superseded by relationships) | `ADDRESSED_PLACE_HANDOFFS_ENABLED` |
| `trips/{id}/messages` | 6 | 1 | 0 | app 6 | retiring 5, active 1 | 1 | LEGACY-RETIRE | `GROUP_TRIP_MICRO_JOURNEY_ENABLED` |
| `trips/{id}/stay-candidates` | 6 | 6 | 6 | app 6 | active 6 |  | LEGACY-KEEP |  |
| `concierge` | 5 | 5 | 5 | app 5 | active 5 |  | LEGACY-KEEP (legacy Home) |  |
| `events` | 5 | 4 | 4 | app 4, server 1 | active 5 |  | NEW-PRODUCT | `LIVED_EXPERIENCE_SURFACE_EXPOSURE_ENABLED`, `ROOT_DELIVERY_EXPOSURE_ENABLED` |
| `public` | 5 | 4 | 4 | app 4, public_web 1 | active 5 |  | LEGACY-KEEP |  |
| `trips (root)` | 5 | 4 | 4 | app 5 | active 4, retiring 1 |  | LEGACY-KEEP |  |
| `trips/{id}/invites` | 5 | 4 | 4 | app 5 | active 4, retiring 1 |  | LEGACY-KEEP |  |
| `/webhooks` | 4 | 0 | 0 | webhook 3, app 1 | active 3, dark 1 |  | INTERNAL | `BOOKING_DUFFEL_LIVE_BOOKING_ENABLED` |
| `agent-workflows` | 4 | 3 | 3 | app 4 | active 3, dark 1 |  | NEW-PRODUCT | `ROOT_SOURCE_CONTRIBUTION_PRODUCTION_ENABLED`, `SHARED_WORKFLOW_CONTROL_ENABLED` |
| `inbound-items` | 4 | 4 | 4 | app 4 | active 4 |  | LEGACY-KEEP |  |
| `trips/{id}/accommodations` | 4 | 4 | 4 | app 4 | active 4 |  | LEGACY-KEEP |  |
| `trips/{id}/receipts` | 4 | 4 | 3 | app 4 | active 4 |  | LEGACY-KEEP |  |
| `users/{id}/follow*` | 4 | 3 | 3 | app 4 | active 3, retiring 1 |  | LEGACY-RETIRE |  |
| `/debug` | 3 | 0 | 0 | infrastructure 3 | active 3 |  | INTERNAL |  |
| `/health` | 3 | 0 | 0 | infrastructure 3 | active 3 |  | INTERNAL |  |
| `discover` | 3 | 1 | 2 | app 3 | retiring 2, active 1 |  | LEGACY-RETIRE |  |
| `invites` | 3 | 3 | 3 | app 3 | active 3 |  | LEGACY-KEEP |  |
| `notification-deliveries` | 3 | 3 | 3 | app 3 | active 3 |  | SHARED |  |
| `search` | 3 | 3 | 3 | app 3 | active 3 |  | SHARED |  |
| `takes` | 3 | 2 | 1 | app 3 | active 2, retiring 1 |  | LEGACY-RETIRE |  |
| `trips/{id}/group-memory` | 3 | 3 | 3 | app 3 | active 3 |  | LEGACY-KEEP |  |
| `trips/{id}/home_cards` | 3 | 3 | 3 | app 3 | active 3 |  | LEGACY-KEEP |  |
| `trips/{id}/notifications` | 3 | 3 | 1 | app 3 | active 3 |  | LEGACY-KEEP |  |
| `trips/{id}/occurrence-artifact` | 3 | 3 | 3 | app 3 | active 3 | 2 | LEGACY-KEEP | `OUTCOME_ARTIFACT_ENABLED` |
| `trips/{id}/settlements` | 3 | 3 | 3 | app 3 | active 3 |  | LEGACY-KEEP |  |
| `trips/{id}/stops` | 3 | 3 | 3 | app 3 | active 3 |  | LEGACY-KEEP |  |
| `trips/{id}/voice` | 3 | 3 | 3 | app 3 | active 3 |  | LEGACY-KEEP |  |
| `venues` | 3 | 3 | 2 | app 3 | active 3 |  | SHARED |  |
| ≤2-op families — INTERNAL | 4 | | | | | | INTERNAL | `admin` (2), `/ready` (1), `curator` (1) |
| ≤2-op families — NEW-PRODUCT | 13 | | | | | | NEW-PRODUCT | `artifact-projections` (2), `entities` (2), `life` (2), `action-receipts` (1), `inbound-audio` (1), `memory` (1), `spatial` (1), `temporal-coordination` (1), `universal-search` (1), `world-foundry` (1) |
| ≤2-op families — SHARED | 9 | | | | | | SHARED | `collections` (2), `experiences` (2), `notifications` (2), `accommodations` (1), `feedback` (1), `messages` (1) |
| ≤2-op families — INTERNAL + app alias | 2 | | | | | | INTERNAL + app alias | `inbound-email` (2) |
| ≤2-op families — LEGACY-RETIRE (never adopted) | 2 | | | | | | LEGACY-RETIRE (never adopted) | `proposal-guest-capabilities` (2) |
| ≤2-op families — LEGACY-RETIRE | 7 | | | | | | LEGACY-RETIRE | `trips/{id}/location-sharing` (2), `trips/{id}/voice-guide` (2), `angles` (1), `lookup` (1), `sites` (1) |
| ≤2-op families — LEGACY-KEEP | 1 | | | | | | LEGACY-KEEP | `plan-similar` (1) |
| 53 small `trips` families (<3 ops) | 64 | 55 | 55 | — | active 55, retiring 6, dark 3 | 4 | mostly LEGACY-KEEP | `BOOKING_DUFFEL_LIVE_BOOKING_ENABLED`, `OUTCOME_ARTIFACT_ENABLED`, `PLACES_SECTIONS_FEED_ENABLED`, `PLAN_SHAPE_ENABLED`, `STORY_SHARE_ENABLED` |

The 53 small `trips/{id}/*` families (<3 ops each) are live trip-product reads/writes with callers (access state,
archive/cancel/deletion preflights, budget, debrief, destinations, details state, digests, group profile, map,
map-state, movement session, nudge, observations, occasion capsule, organizer handoff, plan-state, planning windows,
post-join payoff, presence, prior-occasion context, reading, recover, relations, reuse template, settlement(s),
shape, shared-plan owner, side chat, situation, stay vote, summary, venue commitments, voice, …). The non-active
ones: retiring `geofence-events` (1 of 2), `action-receipts/recent`, `cross-trip-threads`, `decommit`,
`digest/email`, `memory-evidence`; dark `share` DELETE, `editorial-map`, `planning/suggested-saves`. Four expired
reviews sit in `occurrence-proposals` and `second-occasion-outcomes` (`OUTCOME_ARTIFACT_ENABLED`).

### 2b. Highlighted families

* **`/api/trips/*` — the legacy trip product is still the backend's centre of gravity.** 221 of 592 paths carry
  `{trip_id}`; 187 are in the app projection. Itinerary (31 ops, 26 called; 5 retiring incl. writebacks, history,
  saga advance, cross-day suggestions), story (16, all active), expenses (15; 4 retiring), stay candidates (7),
  proposals/voting (8: vote/resolve/withdraw/revert live; 2 guest-link ops dark), members (7), photos (7),
  invites (5), plan-state/planning-windows/shape/relations/occasion-capsule (live, unflagged). Classification:
  LEGACY-KEEP until the four-root product owns plans; the Plan/Occasion identity question (§5b) decides whether these
  are migrated or become the Plan owner.
* **`/api/atlas` — 49 ops, 45 with callers, only 4 retiring** (`/places`, `/search`, `/artifacts/{id}/stream`,
  `/scan-history`). Callers live in `travel-app/data/atlas.ts` (40), `data/atlasArtifacts.ts`, onboarding diary scan,
  and `TripsHomeController.ts`. The Atlas tab redirects to Life, but `app/atlas/*` screens are re-exported under
  `/you` ("Memories") and `routes.atlas*` resolve to `/you/...` (`utils/routes.ts:2045-2104`), so candidates,
  artifacts, timeline, unpacked, boards, compose and parse are live; `atlas/home`, `discovery-reflection` and
  `timeline` are used only inside the redirected (dead) tab file. Flags call Atlas "retired" but the API is
  effectively active. LEGACY-RETIRE except timeline reads that Life needs.
* **`/api/discover` — 3 ops (feed + trending retiring).** Discover tab hidden (`href: null`); `feed`/`map`/`trending`
  have data-layer hooks with **no screen consumer** (the audit counts the hook as a caller). `/users/{id}/for-you`
  (legacy Trips Home) is a separate route. Two scripts still call `/discover/feed`.
* **Booking — 34 ops under `/api/trips/{id}/booking` + `/webhooks/booking/{provider}` (dark) + admin booking.** 31
  active / 3 retiring (readiness, travel-insurance affiliate link, sessions list); 29 have callers
  (`data/booking.ts` 13, `data/bookingReads.ts` 10, `hooks/useBookingDecision.ts` 4, `bookingConfirmationShare.ts` 3,
  `conciergeHome.ts`, `chat.ts`). Session/offer/cart/hold/cancel/restaurant-attempt ops are execution; coverage,
  captured-amount, confirmation-share and link-surfaced/attribution are evidence/continuation. Split classification:
  retire execution, keep evidence.
* **Voting / proposals:** `trips/{id}/proposals` (8) + `stay-candidates` (7) + experience-graph occasion decisions
  and votes (5 ops, labelled `server` but called by the app) — **two parallel group-decision systems** (trip
  proposals vs graph occasion decisions).
* **Follows:** `/api/users/{id}/following` (3 active with callers in `data/social.ts`) + `/followers` (retiring,
  transport-only). A third social graph beside circles and relationships.
* **Root projections (10):** all active; Home v1/v2 and Life with callers; Places root reads consumed via
  `data/rootProjections.ts` (audit shows transport-only — false negative); consequence resolve/repair flag-gated.
  **No server-side gating** on the reads (§6).
* **Life (2):** `POST /api/life/refind`, `/api/life/originals/refind` — active, called behind the app flag
  `EXPO_PUBLIC_LIFE_REFIND_LANE`.
* **Relationships (16), intake (14), entities (2 + 7 under `/api/me/entities`), experience graph (37):** NEW-PRODUCT;
  details in the table above, §6.3–6.4 and §5b.

## 3. Flag map

Sources: `backend/core/feature_flags.py` (897 lines, 77 env names), pydantic settings with env prefixes
(`BOOKING_`, `CONCIERGE_`, `PLACES_`, `LOOKUP_`, `NOTIFICATION_`, `VOICE_`, …), and ad-hoc `os.getenv` reads
(257 distinct env names are read via `os.environ`/`_truthy` helpers across `backend/`). Registry =
`docs/flags/registry.yaml` (106 rows: 80 travel-agent, 26 travel-app; **0 active rows are past `expires` today**,
but **30 travel-agent rows expire 2026-10-04** and 8 more on 2026-10-07). "fly" = value committed in
`travel-agent/fly.toml [env]`; Fly secrets can override it and are not visible statically.

### 3a. Runtime flags in `feature_flags.py`

| Flag (env) | Default | fly | Registry | What it gates (call sites) | Product relevance | Recommendation |
|---|---|---|---|---|---|---|
| `ITINERARY_OPERATIONS_ENABLED` | on (kill switch) | true | ops, 10-04 | `api/routes/itinerary_operations.py` canonical itinerary writes | legacy trip product | keep as ops switch; re-date |
| `PENDING_CHAT_TURNS_ENABLED` | on | true | release, 10-30 | `api/routes/pending_chat_turns.py` | Chat transport (client depends on it) | **delete flag** (client cannot function without it) |
| `SOCIAL_CIRCLES_ENABLED` | on | — | ops, 10-30 | router dependency `api/routes/social_circles.py:59-68` (reads+writes) | People (circles) | keep kill switch; **6 policy review dates expired 2026-09-03** |
| `INTAKE_V2_EMAIL_ENABLED` | on | — | **unregistered** | `api/routes/inbound_email.py` | Capture | register now; delete with v1 email path |
| `INTAKE_V2_CHAT_IMAGE_ENABLED` | on | — | **unregistered** | `concierge/tool_handlers/inbound_screenshot.py` | Capture | same |
| `LEGACY_RESEARCH_WRITEBACK_ENABLED` | on | — | **unregistered** | `research_agent/agents/persist.py`, `experience_research.py` | content supply | register; flip false at evidence-first cutover |
| `WORLDFOUNDRY_DOGFOOD_SERVING_ENABLED` | off | — | 10-30 | `home_portfolio.py`, `core/content_release_scope.py`, `world_foundry/dogfood_release.py`, `lived_experience/place_content.py`, `content_compiler.py` | Home/Places content | turn on for dogfood cohort once a release ledger exists |
| `PLACE_CONTENT_PRIMITIVE_READS_ENABLED` | off | — | 10-30 | `places/sections.py`, `collections.py`, `entity_presentation_read.py`, `lived_experience/place_content.py`, `world_foundry/semantic_memory.py` | Places content quality | dogfood candidate (grants no push/action) |
| `ENTITY_PROVIDER_RESOLUTION_ENABLED` | off | — | 10-07 | `api/routes/entities.py`, `places/projection.py` (materialization → 503 when off) | object page (P05) | turn on for named dogfood cohort |
| `ENTITY_RESEARCH_REQUESTS_ENABLED` (+`_USER_IDS`, `_EMAIL_SUFFIX`, unregistered) | off | — | 10-07 | `api/routes/entities.py` paid research | object page spend | keep dark; cohort-only |
| `CONTENT_CONTROL_PLANE_ENABLED` (+ 5 per-surface `CONTENT_CONTROL_PLANE_{PLACE,CHAT,PLAN,HOME,PUSH}_ENABLED`, **unregistered**) | off | — | 10-30 (global only) | `places/sections.py`, `entity_presentation_read.py`, `concierge/entry_context.py`, `core/ambient_judgment.py`, `lived_experience/adapters/runtime.py` | governed content | keep dark; register per-surface names |
| `ROOT_DELIVERY_PROJECTION_ENABLED` | off | — | 12-01 | `home_portfolio.py`, `application/root_composition.py` | Home/Places delivery identity | turn on with four-root dogfood |
| `ROOT_DELIVERY_EXPOSURE_ENABLED` | off | — | 12-01 | `home_portfolio.py`, `api/routes/events.py` (`POST /api/events/root-delivery`) | exposure telemetry | turn on with four-root dogfood |
| `ROOT_DELIVERY_SUPPRESSION_ENABLED` | off | — | 12-01 | `application/root_composition.py` | repeat suppression | after exposure data |
| `ROOT_SOURCE_CONTRIBUTION_PRODUCTION_ENABLED` | off | — | 12-01 | `api/routes/agent_workflows.py:427-505`, `root_composition.py` | Source contribution | **keep dark until §8 R1–R3 fixed** |
| `ROOT_SOURCE_CONTRIBUTION_WORKER_ENABLED` (+`_COHORT`, unregistered) | off | — | 10-07 | `workers/audio_jobs.py:455-459`, `source_contribution_jobs.py` | paid Sonnet worker | keep dark |
| `LIVED_EXPERIENCE_SURFACE_EXPOSURE_ENABLED` | off | — | 10-30 | `api/routes/events.py` (`/events/surface-treatment`) | content-free telemetry | turn on for dogfood |
| `LIVED_EXPERIENCE_SURFACE_PROJECTION_ENABLED` | off | — | 10-30 | routes `places.py`, `entities.py`, `vesper_home.py`, `plan_state.py`, `trips.py` | treatment identity | keep dark |
| `LIVED_EXPERIENCE_CONSEQUENCE_RESOLUTION_ENABLED` | off | — | 12-01 | `api/routes/root_projections.py:731,766` resolve/repair; `root_composition.py` | consequence grants | keep dark (bypasses relationship kill switch, §8) |
| 9× `LIVED_EXPERIENCE_PRODUCER_*_ENABLED` (**unregistered individually**) | off | — | global row "resolved" | `core/ambient_dispatch.py`, `movement/service.py`, `itinerary_proposal_shadow.py`, `occurrence_shadow.py`, `concierge/decision_frames.py`, `lived_experience/activation.py` | per-family producers | register each; keep dark |
| `LIVED_EXPERIENCE_PRODUCER_INGRESS_ENABLED` | off | — | resolved | **no callers** (`lived_experience_producer_ingress_enabled`) | none | **delete function** |
| `RELATIONSHIP_UUID_HANDOFFS_ENABLED` | off | — | 10-30 | `api/routes/relationship_handoffs.py` (all 16 routes), `entities.py:665`, `concierge/handoff_entry.py`, `home_portfolio.py` (original deliveries only) | People handoffs | keep dark until §8 R1–R4 fixed; then dogfood |
| `PLACE_HANDOFF_PULL_ENABLED` | off | — | 10-30 | `relationship_handoffs.py`, `place_handoffs.py`, `places/friends.py`, `home_portfolio.py:687` | pulls | keep dark |
| `ADDRESSED_PLACE_HANDOFFS_ENABLED` | off | — | 10-30 | legacy integer `api/routes/place_handoffs.py` | superseded | **delete with legacy place-handoffs** |
| `PROFILE_TOGETHER_PROJECTION_ENABLED` | off | — | 10-30 | `social_circles.py:85` | pair "Together" | keep dark (needs consent evidence) |
| `SOCIAL_CIRCLE_AGENT_CONTEXT_ENABLED` | off | — | 10-30 | `concierge/turn_context.py` | group prompt context | keep dark |
| `GROUP_ATTENDANCE_CONTEXT_ENABLED` | off | — | 10-30 | `concierge/turn_context.py` | group prompt context | keep dark or delete |
| `SHARED_WORKFLOW_CONTROL_ENABLED` | off | — | 10-30 | `agent_workflows.py` commands (dark op) | none shipped | delete with code unless planned |
| `GUEST_PROPOSAL_CAPABILITIES_ENABLED` | off | — | 10-30 | `proposals.py`, `proposal_guest_capabilities.py` (4 dark ops, 0 app callers) | legacy trip voting | **delete with code** |
| `VENUE_DISRUPTION_PROPOSALS_ENABLED` | off | — | 10-04 | `concierge/proactive.py` | prepared proposals | decide by 10-04: dogfood or delete |
| `WEATHER_RESCUE_PROPOSALS_ENABLED` + `WEATHER_RESCUE_TRIP_IDS` | off | — | 10-30 | `concierge/proactive.py` (exact trip allowlist) | prepared proposals (P07) | dogfood on named trips |
| `TRIPS_SAVED_UNPLACED_ENABLED` | off | — | 10-30 | `api/routes/concierge_home.py` | legacy Home | delete with legacy Home |
| `PLACES_SAVED_UNPLACED_ENABLED` | off | — | 10-30 | `places/sections.py` | Places | decide: dogfood or delete |
| `PLACES_REGISTERS_ENABLED` | off | — | 10-30 | `places/sections.py`, `places/returns.py` | Places | decide |
| `PLACES_TWO_PLACE_COMPARISON_ENABLED` | off | — | 10-30 | `places/comparison.py` (adapter not wired into feed) | Places | delete unless candidate source exists |
| `PLACES_EXPOSURE_ROTATION_ENABLED` | off | — | 10-30 | `places/sections.py` | legacy Places feed | delete with legacy feed |
| `CROSS_SURFACE_ECHO_DEFERRAL_ENABLED` | off | — | 10-30 | `home/vesper_workbench/assemble.py`, `places/sections.py` | legacy Home/Places | delete with legacy Home |
| `CONCIERGE_EXPOSURE_FATIGUE_ENABLED` | off | — | 10-30 | `home/concierge_feed/ranking.py` | legacy Home | delete |
| `HOME_AGENT_LOOP_ENABLED` | off | — | 10-30 | `home/compose.py` | legacy Home | delete |
| `AMBIENT_ATTENTION_DISPATCH_ENABLED` | off | — | 10-30 | `core/ambient_dispatch.py`, `ambient_judgment.py` | interruptive push | keep dark |
| `AMBIENT_COINCIDENCE_CANDIDATES_ENABLED` | off | — | 10-30 | `core/ambient_coincidence.py` | relationship presence | keep dark (privacy review) |
| `SPATIAL_REACHABILITY_NEARBY_ENABLED` | off | — | 10-30 | `places/discovery.py` | Mapbox isochrone spend | resolve experiment or delete |
| `NEARBY_TRAVEL_TIME_RANKING_ENABLED` | off | — | 10-30 | `places/taste.py` | Mapbox Matrix spend | resolve experiment or delete |
| `ATLAS_LLM_ENABLED` | **hard `False`** (`feature_flags.py:336-345`) | **true (dead config)** | 10-04 | `api/routes/atlas.py:1196,1379`, `atlas/timeline_generator.py:48` | retired | **delete function and the fly.toml line** |
| `ATLAS_AUTO_CANDIDATE_ENABLED` | **hard `False`** | — | 10-04 | `api/lifecycle.py:505-524` loop | retired | delete loop + function |
| `ATLAS_SIGNALS_TO_MEMORY` | off | **true** | 10-04 | `atlas/signal_memory.py`, `api/routes/atlas.py`, `users/me.py` | writes kept-artifact signals into Personal Memory | keep only while Atlas artifacts exist; rename or delete with Atlas |
| `ANNIVERSARY_PUSH_ENABLED` | off | — | 10-04 | `api/lifecycle.py:509` loop | Atlas memories push | delete (or re-home in Life); **advisory-lock collision** (§4) |
| `UNPACKED_SEASONAL_PUSH_ENABLED` | off | — | 10-04 | `api/lifecycle.py:516` loop | Atlas Unpacked | delete with Unpacked |
| `STORY_SHARING_ENABLED` | off | — | 10-04 | `atlas_unpacked.py`, `story_shares.py` | public share links | decide by 10-04 |
| `AUTO_PUBLISH_GREEN_DOSSIERS` | off | — | 10-04 | `research_agent/agents/persist.py` | dossier supply | delete with legacy research writeback |
| `PLANNER_SEMANTIC_RANKING` | off | false | 10-25 | `planning_agent/db_provider.py` | legacy planner | resolve or delete |
| `CONTEXT_COMPILER_SHADOW_ENABLED` | off | **true (5% sample)** | 10-11 (registry says default false) | `core/context_compiler/shadow_runner.py`, `shadow.py` | telemetry | fix registry: record prod-on |
| `CONTEXT_COMPILER_PLANNER_PARITY/CUTOVER_ENABLED` (+`_TRIP_IDS` unregistered) | off | false/false | 10-17 | `concierge/tool_handlers/planning/_plan.py` | planner | resolve by 10-17 |
| `PLANNING_CONTEXT_SNAPSHOT_PARITY/CUTOVER_ENABLED` (+`_TRIP_IDS` unregistered) | off | — | 10-30 | `planning/snapshot_parity.py`, `context_selection.py` | planner | resolve |
| `AI_DECISION_SHADOW_*` (5 envs) | off | — | 10-07 | `core/ai_decision_shadow.py`, `concierge/decision_frames.py` | learning shadow | keep dark |

### 3b. Settings / env toggles outside `feature_flags.py`

| Toggle | Default | fly | Registry | Gates | Recommendation |
|---|---|---|---|---|---|
| `BOOKING_EXECUTION_RETIRED` (`BookingSettings.execution_retired`, `core/booking_retirement.py:36-61`) | **false** | **not set** | **unregistered** | dispatch boundary for provider-changing booking work; `workers/booking_jobs.py:43-45` | **Fix default / set true in prod** after the obligation audit in `capability-retirement-static-inventory-2026-09-05.md`; register it |
| `BOOKING_DUFFEL_LIVE_BOOKING_ENABLED` | false | — | 10-04 | `booking_agent/holds.py`, `providers/duffel.py`, `api/lifecycle.py` | delete with booking execution |
| `BOOKING_OPENTABLE_ENABLED` | false | — | **unregistered** | OpenTable availability/affiliate | register or delete |
| `BOOKING_MONETIZATION_MODE` | `free_affiliate` | — | 10-04 (registry points at a non-`os.getenv` symbol) | affiliate links | delete with booking readiness |
| `AI_MODE` / `WEB_SEARCH_MODE` (`core/ai_mode.py`) | unset → **live** | — | **unregistered** | every paid LLM / web search call | register as ops switches |
| `DISABLE_LLM_BACKGROUND_LOOPS` | false | false | ops 10-04 | only 6 lifespan loops + 8 subscriber sites; **not the arq worker** (§4) | extend to worker jobs |
| `DISABLE_API_BACKGROUND_TASKS` | false | — | ops 10-04 | all lifespan loops | keep |
| `EXPO_PUSH_ENABLED` | false | not in `[env]` (may be a secret) | 10-04 | `notifications/channel_dispatch.py`, `receipt_reaper.py` | verify prod value (unverifiable statically) |
| `HOME_TASTE_SEARCH_ENABLED` | false | false | **unregistered** | `api/routes/concierge_home.py:1176` | delete with legacy Home |
| `TRIP_SIMILARITY_INDEX_ENABLED` / `_READS_ENABLED` | ? | true/true | **unregistered** | similarity subscribers, nightly rebuild, reads | register as ops |
| `REQUIRE_DISTRIBUTED_TURN_LEASE` | ? | true | **unregistered** | Redis turn lease | register as ops |
| `CONCIERGE_OUTPUT_GUARD_MODE` | ? | `log` | **unregistered** | `concierge/output_guards.py` | register; decide `regenerate` |
| `CONCIERGE_CONTEXTUAL_TOOL_RETRIEVAL_MODE` | ? | `shadow` | **unregistered** | contextual capability selection | register |
| `CONCIERGE_SEARCH_TRANSPORT_ENABLED`, `CONTENT_GRAPH_GEOFENCE_ENABLED`, `FACTS_WRAPPER_ENFORCE` | false | — | 10-04 | concierge | resolve by 10-04 |
| `PLANNING_ITINERARY_FIRST/PREFETCH/REPLAN_DIFF/STRUCTURED_OUTPUT` (on), `PLANNING_TERSE_REASONING` (off) | — | — | 10-04 | `planning_agent/schemas.py` | fold the four on-flags into code |
| `ATLAS_SEMANTIC_READ/WRITE` | false | — | 10-04 | `core/db/atlas.py`, `search/dispatch.py`, `derived_artifacts.py` | delete with Atlas search |
| `ATLAS_BOARD_COPY_LLM_ENABLED` + `DISABLED_SURFACES` | **effectively on when `ANTHROPIC_API_KEY` exists** (`composition/core.py:304-316`) | — | **unregistered** | Atlas taste-board copy LLM | Atlas LLM is *not* fully off despite `atlas_llm_enabled()`; delete with boards |
| `POSTCARD_RENDER_ENABLED` | false | — | 10-04 | `postcard/` | delete with Atlas postcards |
| `LOOKUP_SYNTHESIS_ENABLED` | true | — | 10-04 | `lookup_agent` | delete with `/api/lookup` |
| `LIVED_EXPERIENCE_DARK_WORKER_ENABLED` / `_SHADOW_WORKER_ENABLED` | false | — | **unregistered** | arq crons #9–10 | register |
| `EMBEDDING_CANDIDATE_FRESHNESS_MONITOR_ENABLED` | false | — | **unregistered** | nightly cron | register |
| `REVENUECAT_{WEBHOOK,SUBSCRIBER_SYNC,RECONCILIATION_SWEEP}_ENABLED`, `COMMERCIAL_ACCESS_MODE` (`off`/`shadow`/`enforce`), `COMMERCIAL_GRANT_RESOLUTION_ENABLED` | off | — | **unregistered** | commercial access | register |
| `CONTEXT_COMPILER_EPHEMERAL_AUTH_ENABLED`, `DELIVERY_SPINE_SHADOW_LOG`, `R2_ENABLED` | — | — | **unregistered** | misc | register or delete |
| `NOTIFICATION_*` calibration (holdout 0.05, learned value on, need floor 0.25, daily interruptive cap 4, accept-gate shadow on) | — | set | not flags | `notifications/arbiter.py` | keep as config |

### 3c. Registry / governance drift found

* **Stale registry rows (flag deleted in code, row still `active`):** `PLACES_SECTIONS_ENABLED` (registry points at
  `feature_flags.py:131`; removed in `be0804d02`), and app-side `PLACES_SECTIONS_FEED_ENABLED` (not found in
  `travel-app` source). `api-operation-policy.json` still cites both as the gating flag for `GET /api/places/feed`
  and `GET /api/trips/{trip_id}/planning/suggested-saves`.
* **Mislabeled gating flags in the operation policy:** `GET /api/places/comparison` cites
  `NEARBY_TRAVEL_TIME_RANKING_ENABLED` (route is ungated; adapter flag is `PLACES_TWO_PLACE_COMPARISON_ENABLED`);
  `GET /api/trips/{trip_id}/editorial-map` and `POST /webhooks/booking/{provider}` cite
  `BOOKING_DUFFEL_LIVE_BOOKING_ENABLED`; `PATCH /api/users/{user_id}/saves/{entity_type}/{entity_id}` and
  `DELETE /api/social-circles/{id}/members/{user_id}` cite `SOCIAL_CIRCLE_AGENT_CONTEXT_ENABLED`.
* **Registry default ≠ production:** `CONTEXT_COMPILER_SHADOW_ENABLED` (registry false, fly true),
  `ATLAS_SIGNALS_TO_MEMORY` (registry false, fly true), `ATLAS_LLM_ENABLED` (fly true, code hard-false).
* **≈45 backend env toggles that change production behavior are unregistered** — 22 names inside
  `feature_flags.py` itself (5 of them cohort/allowlist lists) plus ~23 settings/ad-hoc toggles, including the two
  default-on intake flags, `BOOKING_EXECUTION_RETIRED`, `AI_MODE`/`WEB_SEARCH_MODE`, `CONCIERGE_AGENTIC_FACADE_MODE`,
  `SEED_CITY_DAILY_CAP`, `auto_capture_signals`, and the 9 producer-family flags.

## 4. Workers, jobs and background loops

Production topology (`fly.toml`): `app` = uvicorn (owns all lifespan loops; deliberately 1 machine), `worker` =
`arq backend.workers.audio_jobs.WorkerSettings` (1 CPU / 2 GB), `voice` = LiveKit worker at **count 0**.
`backend/workers/` = 29 files, 6,526 LOC (largest: `inbound_jobs` 913, `intake_v2_normalization` 845,
`audio_jobs` 744, `research_jobs` 718, `intake_semantic_jobs` 509). Models: Haiku = `claude-haiku-4-5-20251001`,
Sonnet = `claude-sonnet-4-6` (`core/model_registry.py:140-212`).

### 4a. arq worker (`workers/audio_jobs.py`)

47 fixed functions (`:407-460`) + 2 added only when `root_source_contribution_worker_enabled()` (`:455-459`);
`max_jobs` 8, `poll_delay` 2 s, global `job_timeout` 3,600 s, `max_tries` 1. The worker calls
`register_all_subscribers()` (`:122`), so all 34 event-bus subscriber modules also run inside it.
**No arq job consults `DISABLE_LLM_BACKGROUND_LOOPS`.**

**27 cron jobs, 23 active in production by default:**

| Cron (line) | Schedule | Gate / default | Prod | LLM / paid | Surface |
|---|---|---|---|---|---|
| prune_agent_workflows_nightly (:542) | 03:29 | — | RUNS | DB | ops |
| purge_ai_decision_shadow_receipts_nightly (:548) | 03:35 | — | RUNS | DB | ops |
| project_atlas_entity_facets_nightly (:554) | 03:41 | — | RUNS | DB | **Atlas-only consumers** |
| worker_heartbeat_tick (:565) | 2 min | — | RUNS | Redis | ops |
| audit_llm_anomalies (:570) | 5 min | — | RUNS | DB | ops |
| run_live_provider_canaries (:578) | 4×/day | per-probe config | RUNS | **paid**: Anthropic count_tokens, Tavily, Google Places, **Amadeus/Duffel flight search** (`provider_canaries.py:129-139`), OpenTable | ops (booking probe serves a retiring product) |
| resume_due_planning_workflows (:591) | 1 min | — | RUNS | Sonnet when due | Chat/plan |
| resume_due_memory_workflows (:596) | 1 min | — | RUNS | Haiku (Sonnet post-trip) | memory |
| resume_due_lived_experience_workflows (:601) | 1 min | `LIVED_EXPERIENCE_DARK_WORKER_ENABLED` off | DARK | — | Home (future) |
| resume_due_lived_experience_shadow_workflows (:613) | 1 min | `..._SHADOW_WORKER_ENABLED` off | DARK | — | Home (future) |
| resume_due_source_contribution_workflows (:625) | 1 min | production + worker flags + cohort | DARK | Sonnet | Home/Places |
| resume_pending_booking_sessions (:636) | 1 min | `BOOKING_EXECUTION_RETIRED` default **false** | **RUNS** | Haiku ranking + provider APIs when sessions pending | **booking (retiring)** |
| repair_group_message_propagation (:641) | 1 min | — | RUNS | Redis | Chat |
| repair_intake_v2_outbox (:649) | 1 min | — | RUNS | **paid despite "deterministic" docstring**: web fetch, Deepgram transcription, S3 (`intake_v2_normalization.py:235,598-611`) | Capture |
| process_intake_v2_semantics (:658) | 1 min, 50 events | — | RUNS | Haiku `INBOUND_PLACE_EXTRACTION`, 2,500 max tokens, images | Capture |
| project_intake_confirmed_anchors (:663) | 1 min | — | RUNS | DB | Life |
| repair_intake_consequence_handoffs (:668) | 1 min | — | RUNS | DB | Capture |
| expire_intake_sources (:673) | :00/:30 | — | RUNS | DB | Capture |
| purge_deleted_intake_sources (:678) | 1 min | — | RUNS | S3 deletes | privacy |
| repair_itinerary_projection_propagation (:683) | 1 min | — | RUNS | Redis | trips |
| repair_memory_projection_propagation (:688) | 1 min | — | RUNS | Redis | memory |
| repair_life_projection_propagation (:693) | 1 min | — | RUNS | Redis | Life |
| repair_route_enrichments (:698) | 1 min | — | RUNS | **Mapbox** | map |
| schedule_pre_trip_preparations (:703) | hourly | **none (ignores LLM kill switch)** | RUNS | per member memory refresh, group profile, ≤20 research briefs, narration LLM + Cartesia TTS | legacy trips |
| reconcile_known_revenuecat_customers_job (:708) | daily | `REVENUECAT_RECONCILIATION_SWEEP_ENABLED` off | NO-OP | — | commerce |
| certify_embedding_candidate_freshness_daily (:714) | daily | `EMBEDDING_CANDIDATE_FRESHNESS_MONITOR_ENABLED` off | DARK | — | ops |
| reconcile_trip_similarity_index_job (:729) | 05:23 | `TRIP_SIMILARITY_INDEX_ENABLED` true | RUNS | **OpenAI embeddings** | similarity |

About 13 jobs tick every minute with `run_at_startup=True`.

**On-demand jobs** with LLM/paid work: narration pre-render (Haiku + Cartesia), `warm_experience_brief`,
**`seed_city_full`** (≈$80/city, 10 cities/day → **≈$800/day ceiling**, triggered by empty chat searches; R14),
receipt OCR, inbound item processing (Haiku + Deepgram), Trip Story, planning enrichment/durable planning (Sonnet),
DNA dispute refresh, post-turn social-signal capture (`concierge/agent.py:1567`), booking session job, memory
refresh, pre-trip preparation, similarity refresh, and the dark source-contribution/lived-experience jobs.
**`answer_one_question` is registered but never enqueued (dead).**

### 4b. FastAPI lifespan loops (`api/lifecycle.py`)

`DISABLE_API_BACKGROUND_TASKS` (`:404-418`) stops all of them; `DISABLE_LLM_BACKGROUND_LOOPS` (`:420-425`) stops
only the six LLM loops at `:546-556`.

| Loop | Interval | Gate | Prod | LLM / paid | Surface |
|---|---|---|---|---|---|
| booking `expiration`, `session_dispatcher`, `checkout_reconciliation` (:442-446) | — | none | RUNS | provider polling | **booking (retiring)** |
| `booking_session_reaper` (:461) | 300 s | none | RUNS | DB | booking |
| `experience_embed` (:449/:1448) | 600 s | none | RUNS | **OpenAI embeddings** + Qdrant | Places/experiences |
| reapers: stuck messages, OCR, idempotency, isochrone/distance cache, outcome, dedup, stale claims, push receipts (:450-537) | 60 s–6 h | none | RUNS | DB / Expo receipts | ops |
| `edit_inference` (:482) | 1,800 s | none | RUNS | none | memory |
| `cache_invalidation`, `incrementality_stamp` (:487-494) | — | none | RUNS | Redis/DB | ops |
| `leave_by` (:499) | 5 min | mute/dedup | RUNS | push | legacy trips |
| `reengagement` (:500/:671) | daily | none | RUNS | nudges | legacy trip chat |
| `anniversary` (:509) | daily | `ANNIVERSARY_PUSH_ENABLED` off | DARK | push | Atlas memories |
| `unpacked_seasonal` (:516) | — | `UNPACKED_SEASONAL_PUSH_ENABLED` off | DARK | push | Atlas Unpacked |
| `atlas_candidate_backfill` (:524) | daily | hard-false | DARK forever | — | retired |
| `trip_completion` (:529) | daily | none | RUNS | emits `trip.completed` → post-trip subscribers | legacy trips |
| `scheduled_tasks` (:533) | 60 s | kill switch skips only `farout_read_pool` | RUNS | per handler | mixed |
| **`pre_trip`** (:547) | 1 h | LLM kill switch | RUNS | enqueues worker job | legacy trips |
| **`brief_regen`** (:548) | 1 h, batch 20 | LLM kill switch | RUNS | research LLM | Places content |
| **`daily_reflection`** (:549) | 4 h, 50 users | LLM kill switch | RUNS | Haiku | memory |
| **`proactive`** (:550/:1587) | adaptive 30–300 s | LLM kill switch | RUNS | Haiku triage → Sonnet proactive message; producers legacy/autopilot/interjection; venue-disruption & weather-rescue producers dark | Chat/notifications (legacy trips) |
| **`digest`** (:555) | 6 h, batch 20 | LLM kill switch | RUNS | Haiku `DIGEST_DAILY` | **legacy trip digest** (`LIMIT 20` without `ORDER BY`, `digest/engine/daily.py:268-277`) |
| **`story_backfill`** (:556) | daily | LLM kill switch | RUNS | Sonnet + push | Trip Story |

Embedding prewarm is off (`EMBEDDING_PREWARM_ENABLED=false`).

### 4c. Event-bus subscribers and `scheduled_tasks` handlers

`register_all_subscribers()` walks 34 hooks (`core/event_subscribers.py:48-83`) in **both** the API process
(`api/lifecycle.py:325-327`, registered *before* the `DISABLE_API_BACKGROUND_TASKS` early return at `:404`) and the
arq worker (`workers/audio_jobs.py:122`). `background_llm_enabled()` is consulted by only four subscriber modules
(post-trip debrief, post-trip memory refresh, trip story, cross-trip threads). No Atlas, Discover, notifications or
digest module subscribes to events, so `ATLAS_*` flags affect request paths only.

| Event → handler | Work | LLM / paid | Gate | Prod |
|---|---|---|---|---|
| `itinerary.committed` → `booking_agent/subscribers.py:39` | debug log | — | — | no-op (delete) |
| booking.* (6 events) → `concierge/booking_subscribers.py:305-310` | template chat posts; `restaurant_call_initiated` dispatches a **Bland.ai call** (`booking_agent/tasks/restaurant_dispatch.py:293,357`) | Bland | `BOOKING_EXECUTION_RETIRED` (off) + key | RUNS (retiring product) |
| `trip.completed` → post-trip debrief (T+2 h), memory refresh (T+3 h), story prewarm (T+24 h) | schedule tasks | Sonnet per member in handlers | BG | RUNS |
| `trip.completed` → `preference_engine/edit_inference.py:343` | ≤20 swap observations (durable memory write) | — | none | RUNS |
| `itinerary.committed` → `concierge/transport_subscribers.py:364` | 3 transport nudges at +1 h; two post a **Sonnet proactive group turn** (`:182,:323`), `group_split` always returns False (`:217`) | Sonnet | **none** | RUNS |
| `trip.completed` → `cross_trip_thread_subscriber.py:131` | one `create_task` per member × upcoming trip, no semaphore | Haiku | BG | RUNS |
| Takes: `trip.completed` → regenerate post-trip Curator Take for **every venue** (`core/takes/subscribers.py:236-248`, verified); `brief.finalized`/`dossier.persisted` (semaphore 8); `itinerary.committed` prewarm ≤10 | Haiku `TAKE_CURATOR` | **none** | RUNS (Takes surface is retiring) |
| memory/privacy changes → `core/memory_subscribers.py:90-94` | revoke group profiles, evict Discover cache | — | — | RUNS |
| `life_projection.changed` → 6 Life projectors | write the **shadow** Life index | — | — | RUNS (shadow only) |
| `itinerary.committed`, `trip.phase_changed` → `guide/subscribers.py:197-198` | narration prerender for all members × stops | Haiku + Cartesia | **none** | RUNS (TTS no-op without key; LLM spent first) |
| `experience.surfaced` → `research_agent/subscribers.py:320` | ≤5 `warm_experience_brief` | Haiku + Tavily | none | RUNS |
| `place.coverage_missing` → `:321` (emitted on empty chat search, `concierge/tool_handlers/search.py:1510-1550`) | `seed_city_full` | ≤1,500 calls/city, 10 cities/day | **no BG** | RUNS |
| trip lifecycle → `trip_similarity_subscribers.py:54` | re-index | OpenAI embeddings | `TRIP_SIMILARITY_INDEX_ENABLED` (fly true) | RUNS |
| `trip.created/dated`, `save.created` → `home/farout_read/subscriber.py:138-140`; `itinerary.committed` → `home/trip_reading/subscriber.py:116` | schedule legacy-Home generation | Haiku `HOME_HERO`; Sonnet `PLANNING_ENRICHMENT` ×≤3 per commit | **none** (only `farout_read_pool` is excluded by the kill switch, `lifecycle.py:1073`) | RUNS |
| invite / membership / attendance / occasion reconcile / places refresh / saved-place watch | DB, Twilio/SendGrid, Expo, Google/Foursquare | varies | — | RUNS |

`scheduled_tasks` registry (`core/scheduled_tasks.py:103`) adds: `itinerary_provider_dispatch` **registered twice**
(`core/itinerary_provider_dispatch.py:177` then `booking_agent/itinerary_provider_executor.py:354`; last hook wins by
order at `event_subscribers.py:56-57` — order-dependent override; Duffel payment path dark via
`BOOKING_DUFFEL_LIVE_BOOKING_ENABLED`), `booking_provider_checkout` (gated only by `BOOKING_EXECUTION_RETIRED`),
`ambient_cycle` (no non-test scheduler → DARK), and `saved_place_reopen_scan` (`places/saved_place_watch.py:149`:
unflagged, self-rescheduling daily chain of ≤20 **paid** place refreshes per user, seeded only by
`scripts/schedule_saved_place_reopen_scans.py`). A dormant duplicate registrar for `occasion_reconcile` exists at
`core/db/occurrence_reconciliation.py:784`.

### 4d. Default production posture — summary

* **Runs by default and serves the new four-root product:** intake v2 normalization/semantics/anchors/purges,
  life-projection propagation, memory workflows, planning workflows (shared), experience embedding.
* **Runs by default for the legacy trip product:** proactive loop, digest, pre-trip (worker cron + loop), trip
  completion, story backfill, reengagement, leave-by, narration pre-render, booking sweeps/loops/reaper, flight
  canaries, Atlas facet projection, `ATLAS_SIGNALS_TO_MEMORY`.
* **Dark:** source-contribution worker, lived-experience dark/shadow workers, anniversary and seasonal push,
  Atlas candidate backfill, embedding freshness, RevenueCat sweep, voice.
* **Cost/LLM hot spots:** `seed_city_full` (≈$800/day ceiling, no switch), per-minute intake semantics (Haiku with
  images), pre-trip fan-out (memory × members + 20 briefs + TTS), proactive Sonnet messages, digest Haiku every 6 h,
  4×/day paid provider canaries, OpenAI embedding loops.

### 4e. Worker/loop risks

Kill-switch gaps, booking admission and the `seed_city_full` ceiling are §8 R13–R14; advisory-lock collisions and the
double-registered dispatch handler are §8 R16. Additionally:

1. Uncapped fan-out on `trip.completed`/`itinerary.committed`: Takes for every venue, cross-trip threads per member ×
   trip without a semaphore, narration members × stops, per-member Sonnet debrief/memory/story/Letter, one Sonnet
   trip reading per itinerary commit.
2. Narration pays for the Haiku call before TTS (`guide/prerender.py:258-266`); with the Cartesia key absent, failed
   rows are re-claimable (`:206-214`), so waste repeats on each commit/phase change (conditional on secrets).
3. Global 3,600 s job timeout; only some jobs have inner timeouts. Five per-minute repair jobs emit a PostHog event
   every tick even when idle (~7,200 events/day).

## 5. Data model and identity spine

### 5a. Tables and migrations

**317 physical tables in three separate SQLAlchemy `MetaData` objects:** 283 in core (`backend/core/db/_tables/*`,
72 files), 27 real experience-graph tables (`domains/experience_graph/schema.py`, own `MetaData` at `:30`; a 28th
entry is a `users` stub at `:48` that declares an `auth_subject NOT NULL` column the real `users` table does not
have), and 7 relationship tables (`domains/relationships/schema.py:22`). **Alembic autogenerate only sees core
metadata** (`alembic/env.py:20,34,55-64` skips reflected tables not in `target_metadata`), so the **34 graph +
relationship tables are outside drift detection** and exist only in hand-written migrations.

**Migrations:** 477 revisions in `alembic/versions/` (+135 archived in `_archive/`), one root
(`73a1ca90a2ef_initial_schema`, 2026-05-11), **one head** (`irdelegationtypes01`), **45 merge migrations**.

| Domain | Tables | Notes |
|---|---:|---|
| Trip / itinerary / core "plan" | 61 | `trips`(17), `itinerary`(8), `itinerary_v2`(11), `itinerary_history_v2`(5), `trip_stories`(5), `plan_topology`(2), `outcomes`(4), leave_by, farout_read, map shares, photos, temporal coordination |
| Users / memory / preferences | 26 | `users`(11 incl. `trip_stay_candidates`, `user_facts`), `memory`(14 incl. `personal_memories`, `observations`, `hard_constraints`, policy tables), `delegation_preferences` |
| Experience graph (Plan/Occasion/Commitment/Outcome/Anchor) | 27 | `plans`, `occasions`, `commitments`, `personal_outcomes`, `experience_anchors`, `world_entities`, `graph_identity_bindings`, … |
| Places / venues catalog and truth | 23 | `venues`, `sites`, `accommodations`, place content (6), place truth (3), affinity (3), distance, status cache |
| Editorial / discover / research + geography (`content.py`) | 21 | `places` geography, angles, dossiers, briefs, review/research queues |
| Conversations / chat | 16 | `conversations`, `messages`, `pending_chat_turns`, `trip_digests`, pipeline cursors |
| Entity identity / semantics | 14 | `entity_external_identities`, redirects, resolution reviews/requests, fact claims, facets, semantics (5) |
| Notifications | 14 | envelopes, deliveries, push receipts, attention cases, decisions, dedup |
| Root projection / Home / delivery | 12 | `root_source_contribution_attempts`, `root_source_contributions`, 9 legacy-Home tables (`vesper_*`, `trip_readings`, `home_card_dismissals`), `cycle_runs` |
| Booking / provider execution | 11 | `booking_sessions`, `booking_offers`, `restaurant_booking_attempts`, sagas (2), provider operations/webhooks |
| Relationships | 11 | clean-break 7 + legacy `relationship_place_handoffs` trio + `relationship_memory_claims` |
| Intake / inbound / receipts | 11 | `inbound_items` (v1), `intake_submissions` … (v2), `vesper_action_receipts` |
| Ops / telemetry | 11 | LLM call records, concierge turns, rate limits, `scheduled_tasks`, `agent_workflows` |
| Atlas | 10 | all `atlas_*` + `atlas_artifact_photos`, `atlas_threads` |
| Life projection / organization | 9 | `life_corpus_entries` (index — **no route reads it**), organization (6) |
| Social / Social circles | 8 / 4 | `follows`, `entity_saves`, `entity_takes`, `collections`, `discover_trending` / circles |
| Voice / narration | 8 | `voice_guide_sessions`, `geofence_events`, narration cache/leases |
| Expenses | 7 | `expenses`, `expense_shares`, `settlement_payments`, `receipts` (OCR) |
| Experiences catalog | 5 | `experiences`, briefs, dossiers |
| Commercial access | 5 | usage buckets/ledger, benefit grants |
| World Foundry / Lived experience | 2 / 1 | releases / `lived_experience_decision_arcs` |

Unreferenced tables: `source_weights` (`content.py:355`), `source_city_scores` (`:726`),
`itinerary_operation_awareness` (`itinerary_history_v2.py:97`, tests/scripts only).

### 5b. Identity spine — where one real-world thing has several ids

**Trip vs Plan vs Occasion (three live namespaces, no row-level bridge).**

| Concept | Storage / id | Reality |
|---|---|---|
| Trip | `trips.id` UUID (`_tables/trips.py:42`), `trip_members` (`:214`) | The operational spine: **221 of 592 OpenAPI paths** take `{trip_id}` (187 in the app projection); ~84 modules touch `trip_members` |
| Core "plan" | **is a trip id**: `plan_participation_windows.plan_id` FK → `trips.id` (`plan_topology.py:27`); `plan_relations.*_plan_id` → trips (`:69-81`) | naming only |
| Graph Plan | own table `plans.id` UUID (`experience_graph/schema.py:280`), **no `trip_id` column** (verified); relations in a separate `experience_plan_relations` (`:304`) | Created only by `POST /api/experience-graph/plans` (server audience, no app caller); the app only calls `plans/{id}/lifecycle` |
| Graph Occasion | `occasions.id` UUID (`:329`), `occasion_members` (`:353`), `occasion_plan_links` (`:451`) | Created by route or by `application/relationship_openings.py:112` (handoff → occasion) |
| Trip-derived "occasion" read models | `core/db/occasion_context.py`, `second_occasion.py`, `decision_occasion.py`; capsule id = `uuid5(trip_id:viewer_id:projection)` (`core/occasion_capsule.py:83`); `settled_commitment_ids` are itinerary **block** ids | `/api/trips/{id}/occasion-capsule`, `/prior-occasion-context`, `/second-occasion-outcomes` |

Only bridges: `commitment_external_links(trip_id, itinerary_block_id)` → graph `commitments`
(`schema.py:544-583`, UUIDs with **no FK**, vocabulary `legacy_trip_block` only), written by
`adopt_trip_block_as_commitment` (`domains/experience_graph/trip_adapter.py:167`), which sets
`world_entity_id=None` and `plan_id=None` (`:254,258`, verified) — the block's venue and its trip are dropped. There is
**no Trip↔Plan or Trip↔Occasion link** and nothing syncs `trip_members` into `occasion_members`. Consequence: Home v1
and Life read the graph, while users' real plans live in `trips`; Home v2 papers over this with a separate
`legacy_plans` reader (`home_portfolio.py:489`).

**Place (~12 id schemes).** `places.id` integer geography + slug (`content.py:47`; and "place_id" is overloaded —
`place_status_cache.place_id` is a Text provider id, `_tables/places.py:30`); `venues.id`, `sites.id`,
`accommodations.id`, `transport_hubs.id` integers + slugs; `experiences.id` UUID + slug; inline provider columns
(`venues.fsq_id`, `google_place_id`, `external_source/external_id`, `wikidata_id`); canonical `EntityRef{type,id}`
(`core/models/entity_identity.py:25-51`, 7 types; `parse_requested_ref` at `:336` accepts `venue_42`, `venue:42`,
bare numerics, `provider:<p>:<id>`; its legacy regex at `:304` omits `transport_hub`); a second agent-facing grammar
(`core/entity_ref.py:40-97`, venue/site only, also parses fixture forms like `lisbon_042`); provider ledger
`entity_external_identities` (`_tables/entity_identity.py:13`) + redirects; graph `world_entities.id` UUID with a
**second provider ledger** `world_entity_identities` (`schema.py:124`); and `graph_identity_bindings` (`:146`), the
only bridge between graph and catalog (`identity_bindings.py:1-6,49,217`). ~25 tables use the Text
`(entity_type, entity_id)` pair; `itinerary_blocks`, dossiers/briefs/queues and `collection_members` still use typed
integer FKs; `trip_venue_commitments.venue_id` has no FK (`social.py:308`).

**Person relationships.** `trip_members` ↔ `conversation_participants` (synced in `core/db/trips/members.py`);
`occasion_members` (unlinked); `social_circles` (kind pair/group/household/other, `pair_key`) with
`social_circle_trip_links` and `relationship_pair_conversations(circle_id → conversation_id)`; a parallel `follows`
+ `relationship_visibility_grants` graph; **two generations of place handoffs** — legacy
`relationship_place_handoffs` keyed on integer `places.id` (`_tables/place_handoffs.py:22,38`) vs clean-break
`relationship_handoffs` keyed on UUID `world_entity_id` (`relationships/schema.py:26`) — with no shared id and both
routers mounted; `relationship_memory_claims` keyed on `relationship_scope_id` + free-text `subject_key`.

**Intake / sources.** Two pipelines with no bridge: `inbound_items` (v1; fed by inbound items/email/audio routes) vs
`intake_submissions → intake_source_objects → observations/candidates → consequence proposals/handoffs` (v2).
Duplicated concepts: `intake_source_objects` vs graph `source_objects`; three observation tables
(`source_observations`, `graph_source_observations`, `intake_observations`); two action-receipt tables
(`vesper_action_receipts` vs `experience_action_receipts`); two occurrence-evidence tables. Name collisions:
`sources` (editorial publishers), `trip_sources` (story remix), `traveler_intakes` (onboarding), `receipts` (expense OCR).

**Life projection owners.** `life_corpus_entries` keys on `viewer_id` + Text `record_id` + `owner_kind/owner_id`
(`_tables/life.py:42-71`). Declared owners (`life_projection/owner_contracts.py:61-140`) are graph plans, occasions,
outcomes, intake retained sources, experience anchors and Atlas timeline — **every one `SHADOW_ONLY` or
`UNAVAILABLE`**. **Trips are not a Life owner**; trips appear in Life only through Atlas timeline rows that deep-link
`/(tabs)/trips/{source_id}` (`life_projection/record.py:26-29`). The served `/v1/life` composes on read; no route
reads the index.

### 5c. Recommendations

1. **Decide the Plan identity now.** Either make `trip_id` canonical and add `plans.trip_id UNIQUE FK` (or an
   `occasion_trip_links` table) with a backfill so Home/Life graph owners cover real trips, or declare graph `plans`
   experimental and stop Life/Home v1 from treating them as the Plan owner. Rename core `plan_*.plan_id` columns to
   `trip_id`, merge `experience_plan_relations` into `plan_relations`, and rename the OccasionCapsule id.
2. **Place:** make `EntityRef` + `entity_external_identities` canonical; fold or quarantine `world_entity_identities`;
   treat `venues.fsq_id/google_place_id` as ledger-backed cache; retire the `core/entity_ref.py` grammar; add
   `transport_hub` to the legacy regex; require a `graph_identity_binding` when a commitment adopts a block with a
   `venue_id`; rename `place_status_cache.place_id` → `provider_place_id`; add the missing FK.
3. **Handoffs:** migrate `relationship_place_handoffs` into `relationship_handoffs` via bindings, then drop the core
   trio and `/api/place-handoffs`.
4. **Intake:** make `intake_submissions` the single envelope (route `inbound_*` through it); merge graph
   `source_objects` into `intake_source_objects`; merge the action-receipt tables.
5. **Membership:** project `trip_members` → `occasion_members` or document that trip occasions are not graph occasions.
6. **Hygiene:** drop the three unreferenced tables; put graph + relationship metadata under Alembic drift checks; fix
   the `users.auth_subject` stub; rename graph Python symbols that collide with core table names.

## 6. Capability status vs the designed product (backend side)

**The single most important fact for this section:** every four-root read endpoint
(`/api/root-projections/{home,places,v2/home,v2/places,v2/places/runtime,v1/life,v1/life/record,v1/life/organization/groups}`)
is served to any authenticated user with **no server-side flag**; only consequence resolve/repair are gated
(`api/routes/root_projections.py:731,766`). "Dark" is enforced by the app: the four-root shell requires
`EXPO_PUBLIC_FOUR_ROOT_SHELL=true` (+ dev/internal build) and v2 requires the governed-rehearsal flags
(`travel-app/utils/productSystemRollout.ts`). **No `eas.json` profile sets `EXPO_PUBLIC_FOUR_ROOT_SHELL`**, so
production/preview builds render `LegacyTripsHome` and `PlacesWorkspace` (`app/(tabs)/trips/index.tsx:7`,
`app/(tabs)/places/index.tsx:7`) — i.e. users are served `backend/home/` and `/api/places/feed`, not
`root_projection/`. (EAS dashboard env was not visible.)

### 6.1 Home composition

| Capability | Status | Evidence |
|---|---|---|
| v1 Home (`GET /api/root-projections/home`) | Live server-side; experience-graph only; 8-value `HomePosture` | `root_projections.py:505` → `root_projection/compiler.py:340`; `core/models/root_projection.py:222` |
| v2 Home (`GET /api/root-projections/v2/home`) | Live server-side ("Dark v2 Home path" docstring); app calls only in governed rehearsal | `root_projections.py:560-582` → `application/root_composition.py:745` |
| Portfolio | 10 concurrent owner readers (experience_graph, legacy_plans, plan_proposals, places_context, explicit_saves, action_receipts, addressed_place_notes, original_deliveries, sample-demo history, contextual_places) with a 900 ms / 24 items / 10 sources budget; each failure becomes a `RootDegradation` | `root_projection/v2/home_portfolio.py:471-808` |
| Postures | 7 (`URGENT, LIVE, PLANNING, AVAILABLE, RETURNED, QUIET, COLD`) = canon's seven; canon's "Thin" has no enum (COLD/QUIET used) | `core/models/root_projection_v2.py:37`; `home_composition.py:135`; `home_portfolio.py:163,442` |
| Admission | Shared gates → one dominant (recovery instrument in URGENT, else highest benefit) → ≤1 unresolved demand (0 in QUIET) → URGENT suppresses non-critical horizons → per-posture attention budget URGENT 3 / LIVE 5 / PLANNING 6 / AVAILABLE 7 / RETURNED 7 / QUIET 6 / COLD 4 → region-coverage ordering | `root_projection/v2/selectors.py:59,197,228,289-352` |
| Cold start | One Places editorial passage re-labelled `now_invitation` when the account is provably empty; fixed fictional "sample ticket" card only with delivery flags + secret. Codex lane `codex/home-value-delivery` (`bf1e5dadf`) wraps the sample in a value contract and lets it coexist with the Places door | `home_portfolio.py:304-395,743-749,844` |
| Optional stages | treatments (`LIVED_EXPERIENCE_SURFACE_PROJECTION_ENABLED`), consequence grants (withheld unless resolution flag), delivery suppression, delivery proofs (`ROOT_DELIVERY_PROJECTION_ENABLED` + `ROOT_DELIVERY_PRESENTATION_SECRET`), prepared source contribution read (0.35 s cap, flag-independent) | `root_composition.py:348-412,879-909`; `delivery.py:37-40` |
| **Home unit kinds** | **36 defined** (canon 35 + non-canon `people_original_delivery`); **22 produced** (18 default path + 4 dark: `now_sample_demonstration`, `people_original_delivery`, `people_note_door`, `people_authored_region`); **14 with no producer**: `root_shell` (client chrome), `now_decision`, `people_waiting_row` (demand-set only), `now_temporal_posture`, `now_annotated_evidence`, `now_attributed_comparison`, `now_merged_into_read` (fold by design), `horizon_hidden_system`, `horizon_world_fact_row`, `people_authorized_door`, `people_gathering`, `people_status_aperture`, `continuity_settling`, `continuity_voice_horizon` | enum `core/models/root_projection_v2.py:64-102`; producers in `adapters.py`, `home_source_adapters.py`, `home_composition.py`, `home_portfolio.py`; app renderer registry `travel-app/utils/homeRootV2RendererRegistry.ts` lists the 20 produced non-chrome kinds |
| Public content on Home | Home reads `list_current_public_place_content_sources*` directly with no flag, while Places gates the same primitives behind `PLACE_CONTENT_PRIMITIVE_READS_ENABLED` — inconsistent gate | `home_portfolio.py:543-565,604-619`; `core/place_content_sources.py:133,197`; `places/collections.py:187,247` |
| Legacy Home (served in production builds) | `GET /api/concierge/home`, `/trips-stack` (`concierge_home.py:370,583`), `/api/concierge/home/workbench` (+rotate, voice; `vesper_home.py:76,115,183` → `home/vesper_workbench/*`), `GET /api/trips/{id}/home_cards` (`api/routes/home.py:63` → `home/feed.py`) | LEGACY-ACTIVE |

### 6.2 Places

| Capability | Status | Evidence |
|---|---|---|
| Mature feed `GET /api/places/feed` (the Places tab in production builds) | Live; producers anniversary, starter, scoped content (guide, reading door, areas), experiences, saved, gap, friend activity, urgency, returns (harvest/changed), nearby (quiet/starter) | `places/sections.py:145-380` |
| v1/v2 root + runtime join | Live server-side; runtime filters mature cards by v2 admission (10-kind allow-list) | `root_projections.py:533,583,649`; `places_root_runtime.py:22-35` |
| v2 field | **14 of 34** `PlacesUnitKind` emitted; always compiled as `WORLD_FIELD` (no `state` passed) — Focus (7), Path (5 of 6), Live Reduction (5 of 6), provenance label, branch lead and social relevance kinds are never served | `adapters.py:768-784`; `root_composition.py:975-990` (verified) |
| Readings | Dossier readings live; primitive readings dark (`PLACE_CONTENT_PRIMITIVE_READS_ENABLED` + `CONTENT_CONTROL_PLANE_PLACE_ENABLED`) | `sections.py:298-302`; `collections.py:187,247` |
| Visit-fit / practical route check | Live on `/v2/places` when `visit_*` params are sent (`route.evaluate` owner read) | `root_projections.py:614-632`; `canonical_owner_reads.py:1057,1795` |
| Entity situation check | Live, no-store | `api/routes/entities.py:611`; `places/entity_situation.py` |
| Saved-unplaced, registers, exposure rotation, echo deferral | Dark | `sections.py:253,345,383,461`; `returns.py:236` |
| Two-place comparison | Effectively unimplemented (returns unavailable even when flagged; no candidate set) | `places/comparison.py:187-190` |
| Isochrone / Matrix ranking | Dark | `discovery.py:118`; `taste.py:239` |
| Friend place-pulls | Dark (`PLACE_HANDOFF_PULL_ENABLED`) | `places/friends.py:39` |
| World Foundry release scoping | Dark | `collections.py:263,316` |

**Entities / object page** (`api/routes/entities.py`): `GET /api/entities/{type}/{id}` (`:719`), `/presentation`
(`:247`), `/presentation-v2` (`:547`), `/research` (`:291`), `/research-status` (`:461`) live;
`POST /api/me/entity-resolutions` 503 unless `ENTITY_PROVIDER_RESOLUTION_ENABLED` (`:130`, also drives
`resolution_available` at `places/projection.py:269`); research requests need flag + allowlist (`:355`);
`/people-lines` needs `RELATIONSHIP_UUID_HANDOFFS_ENABLED` (`:665`). App renderer cutover is behind
`OBJECT_PAGE_REBUILD_ENABLED` (app flag, default false).

### 6.3 Life projection

| Capability | Status | Evidence |
|---|---|---|
| Endpoints | `GET /api/root-projections/v1/life` (`:1142`), `/record` (`:796`), `/organization/groups` (`:995`), `POST /api/life/refind`, `/api/life/originals/refind` (`life_refind.py:45,64`; zero writes) — no server flags | app shows Life only with `EXPO_PUBLIC_LIFE_ROOT_V1` in rehearsal |
| Composition | Computed per request from experience graph + intake anchors + retained sources + **Atlas timeline entries** (`root_projections.py:254-307`); index/organization tables are written by projectors/workers but no indexed reader is wired | `workers/life_projection_jobs.py` |
| TIME lens | Implemented | `life_projection/adapters.py:225`; `anchor_projector.py:107`; `retained_source_projector.py:112` |
| PLACES lens | Implemented | `adapters.py:265`; `intake_page.py:162` |
| PEOPLE lens | Implemented, thin | `adapters.py:272,315` |
| THREADS lens | Stub-thin (only Plans linked to an occasion/commitment) | `adapters.py:226`; `intake_page.py:119` |
| Featured Return | **Unimplemented** — no producer sets `return_candidate` (grep verified) | `core/models/life_projection_v1.py:161`; `compiler.py:88` |
| Returns arbitration | `arbitrate_returns` exported, **no production caller** (verified) | `root_projection/v2/returns.py:158` |
| Refind | Live over legacy itinerary + booking rows | `backend/life/refind_sources.py` |

### 6.4 Relationships (originals, place notes, pulls, pair circles, guests)

| Capability | Status | Evidence |
|---|---|---|
| UUID handoffs (send-now place notes) | Built; 16 routes gated by `RELATIONSHIP_UUID_HANDOFFS_ENABLED` (off) | `api/routes/relationship_handoffs.py:74-76`; 7 tables in `domains/relationships/schema.py` |
| Original deliveries | Built; gated; strongest re-check (status, expiry, recipient eligibility against an active 2-person room, source custody) | `original_delivery_repository.py:275-466` |
| Place pulls / pull grants | Built; `PLACE_HANDOFF_PULL_ENABLED` off; `PUT /place-pull-grants/{sender}` is `server`/retiring in policy | `repository.py:1829-1923` |
| Pair conversations | `POST /api/relationships/pair-conversations` (policy audience `server`, but the app calls it) | policy anomaly (§2) |
| Legacy integer handoffs | Separate store `core/db/place_handoffs.py` (802 LOC, table `relationship_place_handoffs`); 5 of 6 routes retiring | `api/routes/place_handoffs.py` |
| Social circles | Live (default-on kill switch); Together projection dark | `social_circles.py:59-68,85` |
| Guests (proposal guest links) | Dark, never adopted by the app (0 callers) | `proposal_guest_capabilities.py:31,82` |
| People on Home | `people_participants_row` live; note door / authored region / original delivery dark | §6.1 |

### 6.5 Contribution / consent policy

* Tier model in `core/contribution_policy.py` (`resolve_contribution`): **T0** (current job only, private, no
  durable authority) for every Ask and every model-suggested gesture (`MODEL_CANNOT_GRANT_AUTHORITY`,
  `ANSWER_ONLY`); **T1** (bounded private continuity: deliberate Point/Bring/Keep with verified custody, cheap
  reversal, or explicit Correct — forces PRIVATE and downgrades person-level learning to situation-level L2);
  **T2** (preview first: any non-private audience, Share/Decide/Act, material boundary; Commit → Propose without
  exact/mandate authority).
* Audience enums are not unified: contribution audience PRIVATE/NAMED_PEOPLE/OCCASION/PUBLIC
  (`core/models/contribution.py:97`) vs composition/interaction audience PRIVATE/GROUP/PUBLIC
  (`composition_v1.py:25`, `agentic_turn.py:45`). The GROUP value is where R2 lives.
* Admission: `core/contribution_admission.py` maps Intake/Chat admissions onto the policy; retention without T1 falls
  back to answer-only. `relationship_scope.py`, `companion_scope.py` are content-free contracts; `privacy_catalog.py`
  holds group-synthesis defaults; `public_egress.py` registers public surfaces for a coverage test.
* Withdrawal: handoff revoke/dismiss hides current serving everywhere status is filtered; original deliveries and
  intake withdrawal are end-to-end (intake revokes dependent handoffs, `core/db/intake_v2.py:1035-1043`, and emits
  source-owner retraction events). **Not end-to-end:** derived source contributions (R6), pull-grant revoke and
  pair-room loss on loose readers (R5).

### 6.6 Memory writes — paths that still write durable state from an Ask

**Contract designed, computed in shadow only, not enforced.** The T0/T1/T2 policy is computed only by the agentic
facade, whose mode is `Literal["off","shadow"]`, default `off` (`concierge/config.py:171-176`, verified; shadow
"cannot alter prompts, provider tools, or execution"). A plain Ask compiles to `ASK` → **T0 ANSWER_ONLY**
(`agentic_facade/shadow.py:159`, `core/contribution_policy.py:152-160`), and the shadow comparator already counts
`DURABLE_WRITE_WITHOUT_CONTRIBUTION_GRANT` / `MODEL_MEMORY_WRITE_OBSERVED` (`agentic_facade/comparison.py:258-282`).
The live gate is `ActionAuthorityResolver` + `validate_contract_context(enforce_confirmation=True)`
(`agent.py:1775,1839,1877`; `tool_contracts.py:438-468`), which checks only tools whose contract has
`confirmation != NONE` with dispatcher enforcement; its "conversational" evidence is a regex over the current user
message (`action_authority.py:53-90,340-374`). `TurnPlan.agency_level` is computed but only used to buffer
streaming (`control_plane_adapter.py:106-129`, `core/agent_loop.py:1333-1353`). The one chat-turn write the policy
does constrain is original-image retention for `inbound_screenshot_submit` on intake v2
(`core/contribution_admission.py:106-137`, `core/db/intake_v2.py:700-716`).

| Path (trigger) | Writes | Gate | Confirmation | Evidence |
|---|---|---|---|---|
| **Structured-only** `confirm_booking`, `promote_to_trip`, `stay_candidate_vote`; direct itinerary tools (`itinerary_block_add/update/move/undo`, attendance, parallel plan, `pin_experience`) | bookings, trips, itinerary | dispatcher enforcement, no conversational cue | **yes (client action)** | `action_authority.py:33-39`; `tool_contracts.py:123-193` |
| `observe` | `observations` (+ every 5th triggers `refresh_personal_memory`) | cue word + word overlap, no member names | implicit (words) | `memory_tools.py:124-145,688-700,837`; `action_authority.py:182-229`; `trip_id` comes from the model (`memory_tools.py:828`) |
| `fact_remember` (+ `home:primary` → `set_home_location`) | `user_facts` | only `value` must appear in the message | implicit | `tool_handlers/memory.py:123-195`; **model-chosen `visibility='group'` is unchecked** (`postconditions.py:590`) |
| `fact_forget`, `memory_constraint_set/remove` | facts, `hard_constraints` | cue list incl. "need", "can't", "allergic" | implicit | `memory_tools.py:1066-1116` |
| `trip_patch`, `expense_log`, `expense_settle` | trip row, expenses | cue words ("cost/paid/spent" authorizes a ledger write) | implicit | `action_authority.py` cue table |
| `generate_plan` (first plan) | itinerary | **no contract** (not in `TOOL_CONTRACTS`); edit mode only | none | `_plan.py:1489-1500`; blocked when an itinerary exists (`itinerary_write_policy.py:61-75`) |
| `propose_change` (group chat) | `change_proposals`; DIRECT-mode low-risk change is applied immediately (intended, `itinerary-editing.md` §4) | trip edit policy | intended auto-apply; **defect: when edit-policy grading throws, falls back to the model's own `approval_mode`** (`_propose_present.py:754-758`, verified) | `_propose_present.py:721-757,830-852,1124-1135` |
| `trip_accommodation_set` (`scope=shared` + cost + paid-by-me) | `trip_accommodations` **and a settleable expense split across all members** | edit policy only | none | `accommodations.py:178-289`; `expenses/accommodation_cost.py:183-190` |
| **`set_location_sharing`** | trip location grant, including `precise` | contract has no `confirmation` kwarg → `NONE` (`tool_contracts.py:71,111-119`, verified) | **none** | `location_sharing.py:63-116`; loaded on location keywords (`_tools_select.py:92-104`) |
| `trip_brief_update` | shared trip concern briefs | none; loaded every trip turn | none | `tool_handlers/memory.py:25-62`; `_tools_select.py:218-230` |
| `memory_observations_prune`, `memory_refresh` | archive observations / regenerate Personal Memory | none (memory-admin keywords) | none | `tool_contracts.py:362-384`; `memory_tools.py:712-746` |
| `search_angles` | inserts an unmatched user query into global `place_angles` | none | none | `tool_handlers/search.py:1151-1165` |
| **`<notes>` → `trips.planning_brief`** | shared trip brief on **every trip-linked turn** that produced notes, regardless of channel | none | none | `agent.py:2182-2188` (verified); the notes prompt asks for members' "Private constraints … marked PRIVATE" (`_prompts_skills.py:2032-2050`) |
| Member brief + trip journal (LLM) | per-member brief docs, journal — including from 1:1 turns; all members' briefs are loaded into trip prompts | none | none | `doc_updates.py:50,75-123`; `turn_loader.py:628`; whether private content reaches group output is **UNVERIFIED** |
| Social-signal extraction | `social_signals` from every group-chat user message | `auto_capture_signals=True` | none | `config.py:26`; `agent.py:1558-1575`; `workers/social_signal_jobs.py:15-58` |
| Piggybacked GPS | `conversations.metadata_.last_location`, `users.last_location`, 24 h `location_sample` observation | **no server-side sharing-mode check** (client gating unverified) | none | `api/routes/_helpers.py:33-80`; `concierge/location_persistence.py:81-141` |
| Post-session reflection | prune/refresh for each participant (observe blocked) | none | none | `session.py:2433-2520`; `reflection.py:733` |
| Other | ambient intent patch (`agent.py:1586-1609`), group-profile regeneration on read (`preference_retriever.py:249,420-435`), vision summaries in message metadata, `update_intent`/`stay_candidate_add`/`propose_booking`/`propose_trip_creation` (proposal rows needing later confirmation), card/message tools | — | — | — |

The regex lane blocks hedges ("should I", "maybe") but **not questions**: "Lunch cost 34 euros, is that normal?"
satisfies `expense_log`, "Our budget is 2000, which hotels fit?" satisfies `trip_patch`, "I'm allergic to peanuts,
which dishes are safe?" satisfies `memory_constraint_set` (`action_authority.py:54-67`; static reading, not run).
`stay_candidate_add` also writes a group-visible row with no confirmation (`tool_contracts.py:277`,
`stay_candidates.py:125-185`). Outside `pending_chat_turns.py:205` (source-byte retention, recorded in turn metadata
that nothing in `concierge/` reads back) and intake v2, **no live chat code path calls `resolve_contribution`**.

**Verdict:** roughly **19–20 durable-write paths** can fire from a chat turn without a tap-to-confirm; only the
structured-only tools require an explicit client action. All of them happen on turns the (unenforced) contribution
policy classifies as T0. Highest risk: `set_location_sharing` (privacy control with no server check),
`trip_accommodation_set` → shared expense, planning brief / member briefs / `trip_brief_update` (LLM-inferred member
facts from 1:1 turns into trip-shared documents), `propose_change` grading fallback, GPS persistence, and
`fact_remember` model-chosen visibility.

### 6.7 Source contribution worker

~8,000 LOC across 17 `root_projection/v2/source_contribution_*.py` files (discovery 851, core 851, opportunities 803,
worker 722, runtime 699, continuity 561, materials 541, telemetry 424, serving 359, pipeline 358, producer 324,
rehearsal 291, canonical executor 285, orchestration 282, trip evidence 270, …) plus 2 tables. Flow: `POST
/api/agent-workflows/source-contribution` (production flag; audience hard-coded PRIVATE at
`agent_workflows.py:460`) → arq worker (worker flag + named cohort) → discovery → selection/pipeline → material
loader → Sonnet producer (`source_contribution_producer.py`) → stored → served read-only on every Home/Places GET with
a 0.35 s cap, **independent of flags** (`application/root_composition.py:879-909`). Status: **fully dark for
production; serving path live but empty**. Must not be enabled before R1–R6 (§8) are fixed.

### 6.8 Notifications caps

Code defaults (`notifications/config.py`, prefix `NOTIFICATION_`) vs committed production (`fly.toml`):

| Knob | Code default | fly.toml | Enforced at |
|---|---|---|---|
| Per-(user, trip) Tier-1 daily cap | 4, scaled by cadence (eager ×1.5, minimal ×0.25) | — | `notifications/gates.py:56-75` |
| Cross-trip interruptive cap | 4 / rolling 24 h (push/SMS) | 4 | `config.py:142`; atomic reserve `channel_dispatch.py:673-676` |
| Quiet hours | per-user, trip-timezone fallback; no deferred wake-up queue (suppressed or downgraded) | — | `gates.py:119-184`; `delivery_spine.py:342-355` |
| Holdout | 0.0 | 0.05 | `arbiter.py:656-663` (also needs enforce mode) |
| Need floor | 0.0 | 0.25 | `config.py:76`; arbitration defaults to `shadow` mode (`config.py:28-36`) |
| Learned value model | false | true | `config.py:98`; `arbiter.py:908` |
| Accept-gate floors | off | shadow on | `arbiter.py:1150-1170` |
| **`EXPO_PUSH_ENABLED`** | **false → log-only, deliveries recorded `skipped`** | not in `[env]` (may be a secret) | `channel_dispatch.py:816,998-1030` |

Unless the Fly secret sets `EXPO_PUSH_ENABLED`, **no push reaches a device** in production; this cannot be verified
statically.

### 6.9 Plan assistance / prepared proposals

| Capability | Status | Evidence |
|---|---|---|
| Proactive loop (6 producers) | Live unless `DISABLE_LLM_BACKGROUND_LOOPS` | `concierge/proactive.py:2184`; `api/lifecycle.py:550,1587` |
| Feasibility catch (timing) | Live, unflagged | `proactive.py:774` |
| Venue-disruption swap proposals | Dark | `proactive.py:1292-1294`; `core/venue_disruption.py` |
| Weather rescue | Dark (flag + exact trip allowlist) | `feature_flags.py:636`; `proactive.py:1707-1709` |
| Proposal gateway / producer / eligibility | Live canonical writers | `core/itinerary_proposal_gateway.py`, `_producer.py`, `proposal_eligibility.py` |
| Proposal vote/resolve/withdraw/revert | Live, 6 ops with app callers (`data/proposals.ts`, `useVoteProposal.ts`, …) | `api/routes/proposals.py` |
| Proposal consequence gateway | Code live; reachable only with consequence resolution on | `core/itinerary_proposal_consequence_gateway.py` |
| Shared-plan lived-experience shadow | Dark | `itinerary_proposal_shadow.py:76` |
| Guest proposal links | Dark, never adopted | `feature_flags.py:654` |
| Open proposals on Home v2 | Live as `motion_loose_end_row` | `home_portfolio.py:500-514`; `home_source_adapters.py:1483` |
| Occasion capsule / planning windows / shape / relations | Live, unflagged endpoints (trip-derived) | `api/routes/plan_state.py:46-162`; `core/occasion_capsule.py` |
| Stay candidates / stay vote | Live (7 ops, all with callers) | `api/routes/stay_candidates.py` |


### 6.10 Concierge agent

* **73 model-visible tools** (`concierge/tool_registry.py`, `capability_catalog.py` 73 declarations,
  `tool_contracts.py`): 24 commit, 4 propose, 45 read/presentation. By group: itinerary 17, memory/preferences 11,
  discovery 8, collaboration 7 (group only), trips 7, planning 4 (`generate_trip_shapes` catalogued
  `planning.shapes.legacy`), expenses 3, stays 3, conversation 3, booking 2 (`propose_booking`, `confirm_booking`),
  Atlas angles 2, location 2, transport/web/inbound/narration 1 each.
* **Live vs shadow in production:** agentic facade (~1.7k LOC) **off** (`config.py:173`, not set in fly);
  contextual tool retrieval computed every turn in `shadow`, the served set is the deterministic legacy eligible set
  (`agent.py:1066-1071`); output guard `log` (hard-blocks unsupported venue names/operational facts on
  venue-retrieval and money turns, `output_guards.py:19-23`; `regenerate` warned against in prod,
  `lifecycle.py:243`); `search_transport` dark (`tool_handlers/transport.py:179`); `FACTS_WRAPPER_ENFORCE` unset
  (scan+log only, `core/llm.py:373-377`); context compiler 5% shadow sample.
* **Turn entry points:** `POST /api/conversations/{id}/messages(/stream)` (live path; `useConciergeChatTransport.ts`,
  `useGroupChatTransport.ts`); `POST /api/pending-chat-turns/{id}/send` → `send_message_stream`
  (`pending_chat_turns.py:232,357`); `POST /api/trips/{id}/concierge/narrate`; **legacy
  `POST /api/trips/{id}/messages*` (5 ops) still run full concierge turns with no app client** — only
  `scripts/smoke-happy-path.sh:331`, `scripts/journey_cert/j04_chat_eval.py`, `tools/dogfood/content/derive_mock_from_seed.py`
  use them; server-initiated turns from the proactive loop, post-trip debrief and transport nudges.
* **Sub-agents:** `planning_agent` via `generate_plan` (sole external caller); `booking_agent` via
  `propose_booking`/`confirm_booking` and dark transport search; `research_agent` only indirectly (geocode helpers +
  search events that enqueue research jobs); `lookup_agent` not called.
* `GET /api/concierge/home` has a hook (`data/conciergeHome.ts:125`) but **no screen**; `trips-stack` is used by
  `TripsHomeController.ts`, workbench rotate/voice by `app/(tabs)/concierge/index.tsx`.

### 6.11 Booking

* **Retired in intent, admitted in code.** `BookingSettings.execution_retired=False`
  (`booking_agent/config/settings.py:15`), `BookingRetirementPolicy` default False (`core/booking_retirement.py:53,60`),
  no `BOOKING_*` in fly; the execution receipt itself says it "remains opt-in (`false`)… until environment obligations
  are audited" (`docs/working/capability-retirement-execution-receipt-2026-09-05.md:68`); `docs/release/v1-scope.yaml`
  lists `live-booking` as `intent: out`.
* **What can change the world:** Duffel is the only `checkout=True` provider and every money-moving call checks
  `_assert_live_booking_allowed` (`providers/duffel.py:49-60`; `BOOKING_DUFFEL_LIVE_BOOKING_ENABLED` false) → dark.
  **Bland.ai restaurant phone calls are the real live-world risk:** phone-only restaurants resolve to `voice`
  (`capability.py:118-137`), `confirm_booking` creates a session and `restaurant_dispatch.py:293-310` places an
  automated call when the Bland key, signing secret and public webhook URL exist; the only kill switch is the
  retirement check (`restaurant_dispatch.py:73`). Twilio SMS is quarantined to deep links (`capability.py:123-127`);
  Amadeus sandbox by default; Viator/OpenTable/Rome2Rio are search + deep link (OpenTable dark).
* **The 34 routes:** 5 can create provider obligations and are guarded by `_require_booking_execution_admitted()`
  (`POST /sessions` 1511, holds settle 1397, offer cancel 2123, cart confirm 2374, restaurant retry 2595); 4 call a
  provider without a retirement guard (offer refresh/reconcile, cancel quote — Duffel POST gated only by the live flag
  — and venue availability); the rest are local state (proposal confirm/reject, hold release, offer select, consent,
  link-surfaced, domain attribution, confirmation share) or read-only/affiliate.
* **App:** `app/booking/[sessionId].tsx` (registered stack screen reached from 9 entry points) drives session,
  consent, offers, cart confirm, holds, cancel and restaurant retry; sessions are created only by the concierge
  `confirm_booking` (the REST `useCreateBookingSession` has no consumer). Proposal confirm/reject via
  `hooks/useBookingDecision.ts` (chat `BookingProposalCard`, decision deck). No app caller: `readiness`,
  `link-domain-attribution/*`, travel-insurance affiliate, `POST`/`GET /sessions`, venue availability.
  `EXPO_PUBLIC_LIVE_BOOKING_ENABLED` only changes labels.

### 6.12 Other product capabilities (one line each)

| Capability | Status | Evidence |
|---|---|---|
| Expenses | LEGACY-ACTIVE: 11/15 expense ops + settlements/settle-batch/receipts called from `app/trip-expenses/*`, `components/expense/*`, share-capture receipt upload; concierge `expense_log`/`expense_settle` also write; receipt OCR is Haiku vision | `expenses/`, `api/routes/expenses.py` |
| Voice | LEGACY-DORMANT: `POST /voice/token` used by `VoiceOrb`/`VoiceOverlay`, gated by `VOICE_ENABLED`; `eas.json` enables it only for the `dogfood` channel; Fly `voice` process count 0 pending `VOICE_*` secrets; v1-scope `voice: out` | `voice/`, `fly.toml` header |
| Narration / voice guide / geofence | Plumbing active (`GeofenceProvider` mounted in the trip layout calls voice-guide session + narration stops + `POST geofence-events`); audio players return null without `VOICE_ENABLED`; `guide/` prerenders TTS on commit | `context/GeofenceContext.tsx:97,123`; `guide/subscribers.py` |
| Digest | Loop active (Haiku every 6 h; output feeds legacy `home/feed.py`, world model, reflection); `GET /digests` reaches only unused hooks; `POST /digest/email` retiring | `lifecycle.py:1560-1584` |
| Story / story sharing | Story active (`app/(tabs)/trips/[tripId]/story.tsx`); 6 share ops reachable but hidden by app `STORY_SHARE_ENABLED=false` and backend `STORY_SHARING_ENABLED` off | `constants/featureFlags.ts:166` |
| Postcard | Dormant (`POSTCARD_RENDER_ENABLED` off; v1-scope out) | `postcard/render.py:41` |
| Search | Active: `POST /universal-search` (12 callers incl. `app/search.tsx`), `POST /search`, `search/suggest`; `search/nearby` dormant | `search/`, `api/routes/universal_search.py` |
| Research agent | Backend-only, active: hourly brief regen, experience-brief embeds, search-triggered `warm_experience_brief`/`seed_city_full`, pre-trip, Takes | `research_agent/`, §4 |
| Intake | v2 active (`app/share-capture/index.tsx` create/upload/finalize, interpretations, `app/you/intake-submissions/*`); v1 `inbound-items` is the fallback branch; `inbound-audio` dormant (no consumer); `inbound-email/alias` active | `inbound/`, `api/routes/intake.py` |
| Situation, social state, preference engine, tasks, media, invites | Active internal or trip-product infrastructure | §1 |

## 7. Deprecation list (backend), ordered by value ÷ risk

Ordering: first the items with the highest cost/risk removed per unit of migration risk. "Blocked by" names the
mobile callers (from `scripts/api_contract_audit.py` discovery) or backend readers that must move first. Existing
plans that already own some of this: `docs/working/capability-retirement-static-inventory-2026-09-05.md` and
`capability-retirement-execution-receipt-2026-09-05.md` (booking), `itinerary-legacy-retirement-cutover-plan-2026-07-14.md`.

### Tier 0 — zero-dependency deletes (do now)

| # | Remove | Evidence it is dead | Dependency notes |
|---|---|---|---|
| 0.1 | `feature_flags.lived_experience_producer_ingress_enabled` | 0 callers | registry row already `resolved` |
| 0.2 | `atlas_llm_enabled()` + `ATLAS_LLM_ENABLED="true"` line in `fly.toml` | hard-returns False; fly value is dead config | callers `api/routes/atlas.py:1196,1379`, `atlas/timeline_generator.py:48` take the False branch — inline it |
| 0.3 | `atlas_auto_candidate_enabled()` + `atlas_candidate_backfill` loop (`api/lifecycle.py:505-524,910`) | hard-False; loop can never start | none |
| 0.4 | `answer_one_question` arq function (`workers/audio_jobs.py:146`) | registered, never enqueued | none |
| 0.5 | `booking_agent/subscribers.py` (`itinerary.committed` debug log) and `transport_nudge_group_split` task kind (`transport_subscribers.py:217`, always False) | no-ops that still write rows / consume events | none |
| 0.6 | Tables `source_weights`, `source_city_scores`, (after checking data) `itinerary_operation_awareness` | unreferenced in `backend/` | migration only |
| 0.7 | The 22 audit `transport_only` operations — `http.ts` methods with no product caller — and, once they are gone, the backend handlers of the **61 retiring ops that have no product caller** (only `GET /api/discover/feed` among the 62 retiring ops still has one). Transport-only set: `/discover/trending`, `/trips/blank`, `/booking/sessions` GET, `/cross-trip-threads`, `/expenses/{id}` GET + comment DELETE, `/itinerary/operations/writebacks` GET/POST, `/planning/suggested-saves` (dark), `/voice-guide/session`, `/users/{id}/facts/{id}/history`, `/users/{id}/followers`, `PATCH /users/{id}/saves/…` (dark), `/conversations/{id}/location`, `/experience-graph/occasions/{id}/anchors/{id}/link`, `/places/{slug}/angles/request`, `/decommit`, `POST /trips/{id}/members`, `/narration/prerender-hint`, `/users/{id}/heartbeat`, `/users/{id}/modality/route`, `DELETE /social-circles/{id}/members/{user}` (dark) | `scripts/api_contract_audit.py --json` → `transport_only` (22) | delete app transport methods in the same change; keep `occasions/.../anchors/link` if the graph anchor flow is still planned |
| 0.8 | Stale registry rows `PLACES_SECTIONS_ENABLED`, `PLACES_SECTIONS_FEED_ENABLED`; fix mislabelled policy flags (§3c) | flag removed in `be0804d02` | docs only |
| 0.9 | Advisory-lock key collisions (`lifecycle.py:711/1168`, `:814/1477`) | fix before either push flag is enabled | none |

### Tier 1 — high value, contained risk

| # | Remove / change | Why | Blocked by / dependency notes |
|---|---|---|---|
| 1.1 | **Set `BOOKING_EXECUTION_RETIRED=true` in production and register it**; then delete provider execution: session dispatcher / checkout reconciliation / expiration loops (`lifecycle.py:442-446`), `resume_pending_booking_sessions` cron, booking session/offer/cart/hold/cancel/restaurant-attempt routes (≈26 ops), Bland/Twilio restaurant dispatch, Duffel holds/saga executor, `booking_provider_checkout` task, flight-search canaries, `/webhooks/booking/{provider}` (dark), concierge booking subscribers | product decision already made ("provider execution retiring", `booking_agent/FEATURE.md`); default still admits execution; 4 always-on loops + per-minute sweep + paid canaries | App callers still exist: `travel-app/data/booking.ts` (13 ops), `data/bookingReads.ts` (10), `hooks/useBookingDecision.ts` (4), `app/booking/[sessionId].tsx`, venue action creating L1 sessions. Retained readers must keep working: `life/refind_sources.py` (joins booking rows), `core/db/plan_state.py` coverage, expense `booking_offer_id` seam, stay attestation in `api/routes/trips.py`, confirmation shares (3 ops), coverage/captured-amount reads. `booking_sessions/offers` are reached by 17 route modules via itinerary gateways — tables stay until the gateways are refactored. Environment obligation audit (not performed) is the gate. Also remove or make handoff-only the concierge `propose_booking`/`confirm_booking` tools — until the flag is set, `confirm_booking` can trigger **Bland.ai restaurant phone calls** when Bland secrets exist (`booking_agent/tasks/restaurant_dispatch.py:73,293-310`). Shrink `app/booking/[sessionId].tsx` to read-only history/evidence/handoff |
| 1.2 | **Discover:** `backend/discover/` (2,063 LOC), `/api/discover/*` (3 ops, 2 retiring), `discover_trending`, Discover cache invalidation in `memory_subscribers.py`, `personalization_cache.py` LLM upgrade, router mount (`router_registry.py:37,137`) | tab is `href: null`; still spends LLM on cache upgrade | no screen consumer (hooks `useDiscoverSectionedFeed`/`useDiscoverMapPins` unused); move `scripts/dogfood_five_pack_live_api.py:305` and `tools/dogfood/content/derive_mock_from_seed.py:203` first; keep `/users/{id}/for-you` (legacy Trips Home) |
| 1.3 | **`lookup_agent`** (1,689 LOC) + `POST /api/lookup/` + `LOOKUP_SYNTHESIS_ENABLED` | only importer is its own route; op retiring with no caller | none |
| 1.4 | **Legacy integer place handoffs:** `api/routes/place_handoffs.py` (6 ops, 5 retiring), `core/db/place_handoffs.py` (802 LOC), `relationship_place_handoffs` trio, `ADDRESSED_PLACE_HANDOFFS_ENABLED` | superseded by `domains/relationships` | `POST /api/place-handoffs/{id}/actions` still has an app caller (`data/placeHandoffs.ts`); `_conversation_handoff_visibility.py`, `composed_card_actions`, experience-graph route read the legacy table; migrate rows via `graph_identity_bindings` first (§5c.3) |
| 1.5 | **Guest proposal capabilities** (4 dark ops, `proposal_guest_capabilities` table, `GUEST_PROPOSAL_CAPABILITIES_ENABLED`) | never adopted (0 callers) | none |
| 1.6 | **Takes / dossier / angles surfaces:** `/api/takes/{id}` (retiring), `/api/angles/{id}`, `/api/dossiers/{venue,site,accommodation}/{id}` (3 retiring), `/api/sites/{id}`; Takes subscribers that regenerate a Curator Take for every venue on `trip.completed` | retiring ops with no callers; uncapped Haiku fan-out | `briefs`/`dossiers` tables still feed active venue/entity pages and Places readings — keep the tables and research supply; delete only the surfaces and the Takes fan-out |
| 1.7 | **Legacy trip messages** `/api/trips/{id}/messages*` (6 ops, 5 retiring, 1 expired review) and `trip_cross_trip_threads` | Chat moved to `/api/conversations` | no app client; still run full concierge turns; used by `scripts/smoke-happy-path.sh:331`, `scripts/journey_cert/j04_chat_eval.py`, `tools/dogfood/content/derive_mock_from_seed.py` — move them to `/api/conversations/*`; keep `side-chat` and `messages/events` (SSE in `utils/tripEventStream.ts`) |
| 1.8 | **Location sharing + geofence events** (4 ops retiring, `trip_member_location_sharing`, `geofence_events`) | retiring, no callers | read by `members.py`, `invite_landing.py`, `booking_confirmation_landing.py` — remove those reads |

### Tier 2 — valuable, needs a replacement first

| # | Remove | Why | Blocked by |
|---|---|---|---|
| 2.1 | **Legacy Home** (`backend/home/` 17,904 LOC: `concierge_feed`, `vesper_workbench`, `trip_reading`, `farout_read`, `feed.py`; routes `/api/concierge/home*` 5 ops, `/api/trips/{id}/home_cards` 3 ops; 9 legacy-Home tables; flags `HOME_AGENT_LOOP`, `TRIPS_SAVED_UNPLACED`, `CONCIERGE_EXPOSURE_FATIGUE`, `CROSS_SURFACE_ECHO_DEFERRAL`, `HOME_TASTE_SEARCH`; subscribers `farout_read`, `trip_reading` (Sonnet per commit)) | this is what production users see today; two Home stacks double every Home change | **Four-root shell must ship in an EAS profile** (`EXPO_PUBLIC_FOUR_ROOT_SHELL`) and Home v2 must reach parity (14 unimplemented kinds, §6.1); app consumers `LegacyTripsHome`, `components/trips/TripsHomeController.ts`, `app/(tabs)/concierge/index.tsx` |
| 2.2 | **Atlas product surface** (49 ops; boards/compose/candidates/inbox/scan/unpacked/postcards; `composition/`, `postcard/`, `ATLAS_BOARD_COPY_LLM_ENABLED` path, `ATLAS_SEMANTIC_*`, anniversary + seasonal push loops, `project_atlas_entity_facets_nightly`) | "Atlas is no longer a product surface" (`feature_flags.py:336`) yet 45 ops have callers and the board-copy LLM is still effectively on | `app/atlas/*` screens re-exported under `/you` ("Memories": scan, candidates, artifacts, unpacked, boards, compose; `utils/routes.ts:2045-2104`) plus account/profile/privacy screens in the `app/atlas/` route group, `data/atlas.ts` (40 ops), onboarding diary scan, `TripsHomeController.ts`; `atlas/query_parse.py:148` and `taste_board.py` still call LLMs. **Keep `atlas_timeline_entries` and the timeline reads**: Life's served projection reads them (`api/routes/root_projections.py:254`) and they are Life's only trip bridge (`life_projection/record.py:26-29`). `ATLAS_SIGNALS_TO_MEMORY` writes Personal Memory — decide whether kept artifacts remain a memory source before deleting |
| 2.3 | **Narration / voice guide / digest email / situation-for-voice** (`guide/`, narration prerender subscribers, `/trips/{id}/narration*` 9 ops, `/voice-guide` 2 ops, `POST /digest/email`, `voice/` worker at count 0) | LLM+TTS spend with voice unconfigured; retiring ops | narration audio/lease endpoints still active with callers; Trip Story narration (`tasks/trip_story_narration.py`) and `api/routes/voice_bridge_render.py` import `guide` |
| 2.4 | **Follows** (`/api/users/{id}/following` 3 active + followers retiring; `follows`, `relationship_visibility_grants`) | parallel social graph to circles/relationships | `data/social.ts` used by `components/you/YouHubScreen.tsx`, `ExperienceGraphSummaryCard.tsx` |
| 2.5 | **Legacy research writeback** (`LEGACY_RESEARCH_WRITEBACK_ENABLED` default on, `AUTO_PUBLISH_GREEN_DOSSIERS`) and `seed_city_full` auto-trigger from chat search misses | ≈$800/day ceiling without a kill switch | evidence-first content primitives (`PLACE_CONTENT_PRIMITIVE_READS_ENABLED`) must be on first |
| 2.6 | **Intake v1** (`inbound_items`, `/api/inbound-items` 4 ops, `process_inbound_item`, `INTAKE_V2_*` rollback flags) | two capture pipelines with no bridge | app `data/inboundItems.ts`; route inbound email/audio through intake v2 first |

### Tier 3 — structural convergence (plan, don't rush)

* **Trip ↔ graph Plan/Occasion convergence** (§5c.1). Until decided, keep both; do not build new Home/Life features
  on graph Plans that real users never create.
* **Itinerary v1 vs v2 tables** (`itinerary` 8 + `itinerary_v2` 11 + `itinerary_history_v2` 5): follow
  `itinerary-legacy-retirement-cutover-plan-2026-07-14.md`; `ITINERARY_OPERATIONS_ENABLED` is the only writer.
* **Two provider ledgers, two receipt tables, three observation tables** (§5b).
* **Dark investments to keep but gate harder:** source contribution (~8,000 LOC; fix §8 R1–R6 before any flag),
  lived-experience producers, World Foundry serving.

### Flags to delete with their code (summary)

`ATLAS_LLM_ENABLED`, `ATLAS_AUTO_CANDIDATE_ENABLED`, `LIVED_EXPERIENCE_PRODUCER_INGRESS_ENABLED`,
`ADDRESSED_PLACE_HANDOFFS_ENABLED`, `GUEST_PROPOSAL_CAPABILITIES_ENABLED`, `BOOKING_DUFFEL_LIVE_BOOKING_ENABLED`,
`BOOKING_MONETIZATION_MODE`, `LOOKUP_SYNTHESIS_ENABLED`, `POSTCARD_RENDER_ENABLED`, `ATLAS_SEMANTIC_READ/WRITE`,
`ANNIVERSARY_PUSH_ENABLED`, `UNPACKED_SEASONAL_PUSH_ENABLED`, `HOME_AGENT_LOOP_ENABLED`,
`TRIPS_SAVED_UNPLACED_ENABLED`, `CONCIERGE_EXPOSURE_FATIGUE_ENABLED`, `HOME_TASTE_SEARCH_ENABLED`,
`PLACES_TWO_PLACE_COMPARISON_ENABLED` (unimplemented), `SHARED_WORKFLOW_CONTROL_ENABLED` (if unplanned);
fold into code: `PENDING_CHAT_TURNS_ENABLED`, `PLANNING_ITINERARY_FIRST/PREFETCH/REPLAN_DIFF/STRUCTURED_OUTPUT`.

## 8. Correctness and privacy risks (with file:line)

Verdicts are from static reading at `c8c9f5785`; each "verified" item was re-read by the orchestrating agent,
not only by a helper. None of these was exercised against a running system.

### R1 — Source-contribution pipeline ignores the sender's handoff inference permission — **CONFIRMED** (Medium now, High once shared audiences exist)

* The per-handoff permission envelope carries `inference ∈ {contextual_only, none}`
  (`domains/relationships/models.py:145`, `api.py:37`).
* The **only** reader of `permissions.inference` in the backend is the Ask grounding path
  `concierge/handoff_entry.py:76` (`… or handoff.permissions.inference != "contextual_only"`), verified by grep.
* Discovery turns every live handoff addressed to the viewer into a source opportunity without reading
  permissions (`root_projection/v2/source_contribution_discovery.py:356-420`); the material loader passes the
  sender's message to the producer as `producer_context=handoff.message` and `known_claim_texts=(handoff.message,)`
  (`source_contribution_materials.py:378-379`); the canonical owner read (`application/canonical_owner_reads.py:476-530`)
  never checks it either. No `source_contribution_*.py`, `canonical_owner_reads.py` or
  `domains/relationships/repository.py` imports `feature_flags`.
* Effect: a sender who chose `inference="none"` still has their note fed to Sonnet for recipient-facing synthesis.

### R2 — Pair-scoped notes are admitted for GROUP audience — **CONFIRMED in code and locked in by a test; latent in production**

* Discovery sets `allowed_audiences=(PRIVATE, GROUP)` for every place handoff
  (`source_contribution_discovery.py:398-401`, verified).
* The loader rejects only PUBLIC (`source_contribution_materials.py:360-365`) and returns material whose
  `allowed_audiences=(PRIVATE, GROUP)` (`:374`, verified) without checking `scope.kind == PAIR` or
  `recall_and_reuse == "recipient_only"`.
* The "grant" authorizing the audience is minted from the handoff's own id (`discovery.py:378`;
  `canonical_owner_reads.py:1569-1570`) — circular authority. `read_relationship_owner`
  (`canonical_owner_reads.py:1638-1700`) returns handoff refs with `effective_audience=request.audience` and is
  reachable from agentic turns via `application/portfolio_reads.py:916-943`.
* `tests/root_projection/test_source_contribution_materials.py:303-327`
  (`test_live_handoff_material_is_attributed_but_never_public`) asserts that a PAIR handoff loads successfully under
  `CompositionAudience.GROUP` with the private message as known claim text (verified).
* Latent because every production entry point hard-codes PRIVATE (`api/routes/agent_workflows.py:460`,
  `source_contribution_serving.py:235`), but the rehearsal requires a LIVE_SHARED baseline with GROUP
  (`source_contribution_rehearsal.py:232-240`), LIVE_SHARED ranks PLACE_HANDOFF first (`discovery.py:706-707`), and
  `application/root_composition.py:697` maps LIVE_DISRUPTION → LIVE_SHARED. Conflicts with
  `docs/systems/contribution-and-consequence.md` §3.6 ("An audience grant never implies every purpose").

### R3 — Handoff reads and one write are not behind the relationship kill switch — **PARTIAL (routes gated; side paths not)**

* All 16 routes in `api/routes/relationship_handoffs.py` call `_require_enabled()` (`:74-76`); legacy
  `place_handoffs.py` gates reads too (`:36-40`); `social_circles.py` gates at router level (`:59-68`).
* **Not gated:** Home `addressed_place_notes()` (`root_projection/v2/home_portfolio.py:671-714`, verified) calls
  `list_place_handoffs(... SEND_NOW)` with no `relationship_uuid_handoffs_enabled()` check, while its sibling
  `original_deliveries()` (`:716-720`) is gated; `places/friends.py:39` checks only the pull flag; source discovery,
  material loading and canonical owner reads have no flag checks; stored productions are served on every Home/Places
  GET regardless of flags (`application/root_composition.py:879-895`); conversation-history handoff messages filter
  on status only (`api/routes/_conversation_handoff_visibility.py`).
* **Write bypass:** `POST /api/root-projections/v2/consequences/resolve` (`api/routes/root_projections.py:716-740`,
  gated only by `LIVED_EXPERIENCE_CONSEQUENCE_RESOLUTION_ENABLED`) dispatches the `addressed_place_handoff` gateway
  (`lived_experience/gateways.py:210-212`) → `execute_place_handoff_command`
  (`domains/relationships/consequence_gateway.py:104-141`, `repository.py:1140`) with no UUID-handoff flag check: a
  command prepared while the flag was on can still be delivered after the kill switch is turned off.

### R4 — "Nearby only" precision bypass on Home and Places — **CONFIRMED** (Medium; reachable when the flag is on)

The recipient API masks `world_entity_id` and message for `naming="nearby_only"` (`domains/relationships/api.py:206-226`)
and people-lines skip them (`repository.py:1639`), but Home (`root_projection/v2/home_source_adapters.py:900-1003`)
renders the full message and an exact "Open X's place" link, Places friend cards (`places/friends.py:84-97`) show
message + `place_names=[venue.name]`, and source discovery/materials use the exact place. Nothing at creation prevents
send-now + nearby-only.

### R5 — Revoked pull grants and closed pair rooms not re-checked on loose readers — **CONFIRMED** (Low–Medium)

`list_place_handoffs` (`repository.py:1460-1495`) and `get_place_handoff` (`:1383-1401`) skip the strict eligibility
re-check that `list_readable_place_pull_handoffs` and people-lines use (`:1655-1767`). Consumers: route list/detail
(`relationship_handoffs.py:495-560`, which also skip the pull flag), source discovery (`discovery.py:356`), material
loader (`materials.py:485-491`), canonical owner reads (`:476-530`, `:1656-1660`).

### R6 — Derived source contributions survive revocation — **CONFIRMED** (Low–Medium)

`invalidate_source_contributions_for_source` (`core/db/source_contributions.py:66`) is called only from Intake
(`core/db/intake_v2.py:974`, `intake_semantics.py:1086,1181`), never on handoff revoke/dismiss, pull-grant revoke or
original-delivery withdraw. Serving re-checks status (`source_contribution_serving.py:146-176`), but revoked claims
keep feeding later prompts as `known_claim_texts` for 14 days (`source_contribution_pipeline.py:315-319`,
`source_contribution_runtime.py:553-584`).

### R7–R12 — Chat-turn durable writes without confirmation (details and citations in §6.6)

| # | Risk | Verdict | Severity |
|---|---|---|---|
| R7 | `set_location_sharing` is a COMMIT contract with confirmation `NONE` (`concierge/tool_contracts.py:71,111-119`, verified); the model can set `precise` disclosure from a keyword-loaded tool | CONFIRMED | High (privacy control) |
| R8 | `<notes>` → `trips.planning_brief` on any trip-linked turn regardless of channel (`agent.py:2182-2188`, verified) while the notes prompt asks for members' PRIVATE constraints (`_prompts_skills.py:2032-2050`); member briefs/journal regenerated from 1:1 turns and loaded into every trip prompt (`doc_updates.py:50-123`, `turn_loader.py:628`) | write path CONFIRMED; group egress **UNVERIFIED** — run `privacy-invariant-tracer` | Medium-High |
| R9 | `trip_accommodation_set` (shared scope + cost + paid-by-me) creates a settleable expense split across all members, bypassing `expense_log` evidence (`tool_handlers/accommodations.py:178-289`, `expenses/accommodation_cost.py:183-190`) | CONFIRMED | High (money) |
| R10 | `propose_change`: DIRECT-mode low-risk auto-apply is intended, but when edit-policy grading throws it keeps the model's `approval_mode` (`tool_handlers/planning/_propose_present.py:754-758`, verified) — should fail closed | CONFIRMED | Medium |
| R11 | GPS written to `conversations`/`users.last_location` + 24 h observation on every send with no server-side sharing-mode check (`api/routes/_helpers.py:33-80`, `location_persistence.py:81-141`) | server side CONFIRMED; client gating UNVERIFIED | Medium |
| R12 | `fact_remember` accepts model-chosen `visibility='group'` (checked against itself, `postconditions.py:590`); `observe` takes `trip_id` from the model (`memory_tools.py:828`); regex authority accepts questions ("Lunch cost 34 euros, is that normal?" → `expense_log`) | CONFIRMED (static) | Medium |

### R13 — Retired booking execution is still admitted by default — **CONFIRMED** (High operational/financial)

`BookingSettings.execution_retired = False` (`booking_agent/config/settings.py:15`) and
`BookingRetirementPolicy` defaults to not retired (`core/booking_retirement.py:36-61`); the variable is absent from
`fly.toml` and from the flag registry. With it unset: the per-minute `resume_pending_booking_sessions` cron, three
unconditional lifespan booking loops, the reaper, Bland restaurant-call dispatch from
`concierge/booking_subscribers.py`, `booking_provider_checkout`, and 4×/day paid flight-search canaries all remain
live (§4). Duffel payment stays dark only because `BOOKING_DUFFEL_LIVE_BOOKING_ENABLED` is false.

### R14 — The LLM kill switch is incomplete and one trigger has a ~$800/day ceiling — **CONFIRMED** (High cost)

`DISABLE_LLM_BACKGROUND_LOOPS` stops 6 lifespan loops and 4 subscriber modules only; no arq job checks it; Takes,
guide narration, trip reading, transport nudges (Sonnet group posts), research seeding and invite-intake refresh
ignore it; subscribers are registered before the `DISABLE_API_BACKGROUND_TASKS` early return
(`api/lifecycle.py:325-327` vs `:404`). `seed_city_full` is enqueued from empty chat searches
(`concierge/tool_handlers/search.py:1510-1550` → `research_agent/subscribers.py:130-150`, verified) with up to 1,500
LLM calls ≈ $80/city and `SEED_CITY_DAILY_CAP=10` (`workers/research_jobs.py:355-370`, verified).

### R15 — Four-root reads have no server-side gate, so relationship kill switches do not cover Home — **CONFIRMED** (Medium)

`/api/root-projections/v2/home` (and v1/Places/Life) are served to any authenticated user
(`api/routes/root_projections.py:505-582`); combined with R3 the Home portfolio lists send-now handoffs without the
UUID-handoff flag (`home_portfolio.py:671-714`). Today this is data-dark (handoff rows are written only through
flag-gated routes or the consequence gateway), but flipping the flag off after dogfood would not hide existing
notes on Home. Similarly Home reads public place-content primitives with no flag while Places gates them behind
`PLACE_CONTENT_PRIMITIVE_READS_ENABLED` (`home_portfolio.py:541-613` vs `places/collections.py:187,247`).

### R16 — Other correctness hazards (verified unless noted)

* **Advisory-lock collisions** `7_831_209_453` (anniversary vs stale-claims) and `7_831_209_454` (unpacked seasonal vs
  experience embed) in `api/lifecycle.py:711,814,1168,1477`.
* **Order-dependent handler override:** `itinerary_provider_dispatch` is registered by
  `core/itinerary_provider_dispatch` and then `booking_agent/itinerary_provider_executor` (hook order at
  `core/event_subscribers.py:56-57`); the last one wins.
* **Digest starvation:** `LIMIT 20` without `ORDER BY` (`digest/engine/daily.py:268-277`) — some trips may never get
  a digest (reported by helper; not re-read).
* **Schema drift blind spot:** Alembic autogenerate excludes the 34 experience-graph + relationship tables
  (`alembic/env.py:55-64`, verified); the graph `users` stub declares a non-existent `auth_subject` column.
* **Lossy bridge:** trip-block adoption into graph commitments drops the venue and plan
  (`domains/experience_graph/trip_adapter.py:254,258`, verified), so Life/Home graph readers cannot place adopted
  commitments.
* **Unflagged self-perpetuating paid job:** `saved_place_reopen_scan` reschedules itself daily with ≤20 paid
  Google/Foursquare refreshes per seeded user (`places/saved_place_watch.py:142-149`).
* **Governance drift:** 17 operations past `review_by`; stale registry rows for a deleted flag; ~45 unregistered
  behavior-changing env toggles; registry defaults that contradict `fly.toml` (§3c).

