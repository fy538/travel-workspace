---
doc_type: archive
status: archived
owner: founder / engineering
created: 2026-07-09
archived: 2026-07-09
why_new: Move reviewed completed evidence out of the living documentation tree without deleting its historical record.
---

# Dogfood Substrate Richness, Frontend Contract Alignment & Generation Backlog

> Archived from the living documentation tree on 2026-07-09 during Phase 5 cleanup.

> Status: investigation note (companion to dogfood-qa-substrate-system-investigation-2026-06-28.md)  
> Owner: founder / engineering  
> Created: 2026-06-28  
> Last updated: 2026-06-28  
> Scope: substrate quality, persona richness, FE contract coverage, what to generate next  
> Verified: 2026-06-28 — counts re-checked against manifests/schema/seed pipeline; corrections applied (8→7 trips, ~141→~146 photo_ids)  

**Question this doc answers:** How rich is our dogfood world today, how well does it match what the frontend actually renders, and what should we generate to make dogfood feel *alive* instead of *structurally correct*?

---

## Table of contents

1. [Executive summary](#executive-summary)
2. [Readiness framework (W0–W3)](#readiness-framework-w0w3)
3. [Quantitative substrate inventory](#quantitative-substrate-inventory)
4. [Per-pack richness scorecard](#per-pack-richness-scorecard)
5. [Frontend contract alignment](#frontend-contract-alignment)
6. [Mock persona richness vs backend](#mock-persona-richness-vs-backend)
7. [What makes dogfood feel alive vs cardboard](#what-makes-dogfood-feel-alive-vs-cardboard)
8. [Systemic gaps blocking liveliness](#systemic-gaps-blocking-liveliness)
9. [Generation backlog — prioritized](#generation-backlog--prioritized)
10. [Per-surface generation guide](#per-surface-generation-guide)
11. [Per-pack next actions](#per-pack-next-actions)
12. [Companion & media generation targets](#companion--media-generation-targets)
13. [What not to generate yet](#what-not-to-generate-yet)
14. [Verification checklist](#verification-checklist)
15. [Key file index](#key-file-index)

---

## Executive summary

### The honest read

Backend dogfood substrate is **authorially rich at W2** for five city slices — not sparse YAML. You have:

- **159 staged media assets** (40 Lisbon + 119 Elif-canonical corpus)
- **~146 Atlas photo_ids** across 5 artifacts
- **35 observations**, **29 discover query fixtures**, **33 itinerary blocks** across 7 trips
- Deep persona dossiers, product-moment maps, and display-copy budgets tied to real renderers

**But it does not yet feel lively on device** because:

1. **No pack has passed app QA (W3)** — everything is `app_qa_status: not_run`
2. **Trips home rich hero is a declared gap** on every trip pack
3. **Wedge-critical proposal/vote rows are missing** — Lisbon voting is chat metadata only, not DB proposals
4. **Home feed / Concierge cards are under-seeded** — manifests don't populate `change_proposals`, digests, proactive events, booking holds
5. **Mock and backend worlds diverge** — 12 frontend personas vs 6 backend scenarios; no `mara.ts`; Elif mock has minimal Concierge feed despite being flagship
6. **Media is local-only** (`local://dogfood/...`) — fine for local QA, invisible on Fly until uploaded
7. **Several product-moment-map items remain GAP** — resolved venue cards for Discover boards, proposal seeds, shellfish-safe lunch observation

**The leverage is not "write more manifest YAML."** It is:

- Seed **proposal + home-card substrate** for the wedge (S4 Lisbon)
- Run **W3 app QA** on Lisbon + Rome with real media mounted
- Generate **~15 high-impact rows** that unlock home feed, group vote, and Trips hero
- Add **`mara.ts`** mock aligned with S4 for fast iteration
- Upload **dogfood media to Fly** for EAS dogfood builds

---

## Readiness framework (W0–W3)

From `trip_realism_audit.py`, `packs.yaml`, and pack status docs.

| Level | Meaning | What it requires |
|-------|---------|------------------|
| **W0** | Profile/synthesis only | Personal memory, no trip ops |
| **W1** | Local baseline | Atlas/Discover/receipts; may lack stay/cost/coverage |
| **W2** | Operational trip slice | `trip_summary` with stay, cost_model, itinerary_coverage; grounded blocks; expenses (demo or authored) |
| **W3** | App-validated | W2 + `app_qa_status: passed` on claimed surfaces via real API on device/simulator |

### Current pack levels

| Pack | Target | Computed | App QA | Blocker to W3 |
|------|--------|----------|--------|---------------|
| `lisbon-phase1` | W2 | W2 | not_run | trips_home gap; no proposal DB rows; Fly media |
| `elif-rome` | W2 | W2 | not_run | trips_home gap; app walk not done |
| `tokyo-phase1` | W2 | W2 | not_run | trips_home gap; memory-only itinerary |
| `istanbul-phase1` | W2 | W2 | not_run | trips_home gap; pending artifact UX |
| `brooklyn-phase1` | W1 | W1 (4 gaps) | not_run | intentional; missing stay/cost/coverage |
| `elif-canonical-profile` | W0 | W0 | not_run | synthesis only; 32 signal_count |

**None are W3.** Richness without device proof is structural, not experiential.

---

## Quantitative substrate inventory

### Totals across all manifests

| Entity type | Count | Notes |
|-------------|------:|-------|
| Unique personas | ~8 | mara, dao, reza, elif, sarah, mike |
| Trips | 7 | 1 Lisbon group + 2 Rome + 2 Istanbul + 1 Tokyo + 1 Brooklyn + 0 profile |
| Itinerary blocks | 33 | Avg ~2–3 blocks/day on seeded days |
| Observations | 35 | Lisbon highest (10) |
| Hard constraints | 4+ | dao hills, reza shellfish, etc. |
| Entity saves | 30+ | Istanbul richest (14) |
| Discover query fixtures | 29 | Lisbon highest (11) |
| Conversations | 10 | |
| Messages | ~32 | Lisbon deepest (10) |
| Atlas artifacts | 5 | 1 per city pack |
| Atlas photo_ids (declared) | ~146 | |
| Expenses (demo rows) | 10 | Brooklyn: 0 |
| Trip photos | 38 | |
| Staged media assets | 159 | All `local://dogfood/...` |

### Media mix by pack

| Pack | Total assets | Trip photos | Atlas photos | Gouache | Riso | Hero |
|------|-------------:|------------:|-------------:|--------:|-----:|------|
| Lisbon | 40 | 6 | 34 | 5 | 2 | photo + gouache |
| Rome | 36 | 4 | 32 | 7 | 3 | photo + gouache |
| Tokyo | 33 | 8 | 25 | 8 | 2 | gouache hero |
| Istanbul | 30 | 12 | 18 | 5 | 2 | gouache pending |
| Brooklyn | 20 | 8 | 9 wired† | 2+ | 2 | pattern board |

† Brooklyn manifest lists 9 `photo_ids`; inventory has 20; some section bodies reference IDs not wired in manifest.

### Conversation depth

| Pack | Conversations | Messages | Special UX |
|------|--------------:|---------:|------------|
| Lisbon | 3 | 10 | `vote_widget`, `change_applied` metadata |
| Rome | 2 | 6 | group + receipt |
| Tokyo | 2 | 6 | counter recall + receipt |
| Istanbul | 2 | 6 | pending candidate receipt |
| Brooklyn | 1 | 4 | baseline receipt |
| Elif profile | 0 | 0 | — |

**Assessment:** Conversation substrate proves *receipt copy* and *group tone*, not a living multi-day chat history. 3–10 messages per pack is enough for demo, not enough for "this group has been planning for two weeks."

---

## Per-pack richness scorecard

### Lisbon (`lisbon-phase1`) — S4 wedge + S1 slice

**Role:** Only full **group-planning ops** slice (Mara organizer, Dao/Reza constraints, voting enabled).

| Dimension | Richness | Detail |
|-----------|----------|--------|
| Group dynamics | ★★★★★ | 4 personas, private constraints, vote chat metadata |
| Itinerary | ★★★☆☆ | 4 blocks / 2 seeded days; open tail days 5–6 |
| Venue grounding | ★★★★☆ | 3/4 blocks grounded (`casa-do-alentejo-baixa`, etc.) |
| Memory/observations | ★★★★★ | 10 observations; Elif Atlas slice |
| Discover fixtures | ★★★★★ | 11 queries (group + Elif atlas_composition) |
| Atlas media | ★★★★★ | 34 photos, gouache hero, map points |
| Expenses | ★★★☆☆ | 4 demo rows (€240); missing transport + lodging rows |
| Proposals/votes | ★☆☆☆☆ | **Chat vote_widget only — no `change_proposals` rows** |
| Home/Concierge feed | ★☆☆☆☆ | **Not seeded** — no open proposals, digests, constraint cards |
| Trips home hero | ★☆☆☆☆ | **Declared `gap`** in manifest |

**Unique product proof:** Organizer relief + private constraint synthesis (Dao hills, Reza shellfish) without group leak.

**Forbidden fallbacks to avoid (S4):** Treating all members identically; exposing private prefs as public facts.

---

### Rome (`elif-rome`) — S2 + S1

**Role:** Strongest **memory → return planning** loop.

| Dimension | Richness | Detail |
|-----------|----------|--------|
| Trips | ★★★★★ | 2 trips (2025 kept + 2026 planning) |
| Itinerary | ★★★★☆ | 8 blocks / 3 seeded days; heat-aware pacing |
| Atlas | ★★★★★ | 36 photos, 8 map points, 5 sections |
| Companions | ★★★★☆ | Sarah + Mike; compromise beat (Mike classic) |
| Expenses | ★★★☆☆ | 2 holds (€250 demo) |
| Home/Concierge | ★★☆☆☆☆ | Under-seeded for departure-readiness, planning brief cards |

**Unique proof:** Past memory shapes active return; cancelled-fancy-dinner as plan_delta signal.

---

### Tokyo (`tokyo-phase1`) — S5 + S1

**Role:** **Counter-food DNA**, non-Europe pattern.

| Dimension | Richness | Detail |
|-----------|----------|--------|
| Itinerary | ★★★☆☆ | Memory beats only (4 days / 7 blocks across 9 calendar days) |
| Atlas | ★★★★☆ | 33 photos, residential-ward signals |
| Discover | ★★★☆☆ | 4 fixtures incl. cross-trip bridge |

**Intentionally not full trip reconstruction** — proves Atlas/discover, not live ops.

---

### Istanbul (`istanbul-phase1`) — S3 + S1

**Role:** **Pending candidate** + second-visit planning.

| Dimension | Richness | Detail |
|-----------|----------|--------|
| Entity saves | ★★★★★ | Richest save set (14) |
| Atlas | ★★★★☆ | Pending artifact: 29 photos, 10 map points |
| Observations | ★★★★☆ | 8; evidence-gap authoring |

**Unique proof:** Uncertain return; base/water tradeoffs; overconfident kept-memory language forbidden.

---

### Brooklyn (`brooklyn-phase1`) — S6 + S1

**Role:** **Home-city control sample** — taste starts local.

| Dimension | Richness | Detail |
|-----------|----------|--------|
| Trip ops | ★★☆☆☆ | W1 by design; 6 blocks / 3 of 7 days |
| Expenses | ☆☆☆☆☆ | None |
| Atlas | ★★☆☆☆ | 9 wired photos; section ID drift |

**Do not expect full trip ops.** Proves Atlas/Discover/receipts at home.

---

### Elif canonical profile (`elif-canonical-profile`)

| Dimension | Richness |
|-----------|----------|
| Cross-city synthesis | ★★★★★ (`signal_count=32`) |
| Trip/artifact/media | ☆ (intentionally zero) |

Consolidates taste across cities; city evidence stays in city packs.

---

## Frontend contract alignment

### What the app actually consumes (read models)

| Surface | Primary hooks / API | Substrate fields that drive liveliness |
|---------|---------------------|----------------------------------------|
| **Trips home hero** | `useTrips`, trip hero cards, `TripHeroCard` | `planning_brief`, phase, destination media, Vesper read (≤100 chars rich / ≤160 plain) |
| **Trip Folio** | `useTripFolio` → `/api/trips/{id}/folio` | Spine block ids, facets (stay, decisions, plan, route), phase, margin note |
| **Plan timeline** | `useTripPlanState`, `useItinerary` | Blocks with `energy_rationale`, open_decisions, `recent_changes`, status_rail |
| **Changes / proposals** | `useOpenTripProposals` | `change_proposals` rows, votes, receipts, revert history |
| **Group chat** | `useGroupChat` | Messages, vote widgets, Vesper interjections |
| **Concierge home** | `useConciergeHome` | `vesper_cards` / home feed: anchor voice, active decisions, ambient cards |
| **Discover For-you** | `useDiscoverForYou` | Entity cards, angles, personal frame |
| **Discover compose** | `useDiscoverBoard` | Query fixtures → composed boards (LLM off = fixture copy) |
| **Atlas home** | `useAtlasArtifacts` | Artifacts, photo strips, sections, signals, pending vs kept |
| **Costs** | `useTripExpenses` | Expense rows, shares, settle balance |
| **Stay** | `useStaySummary` | `trip_accommodations`, stay candidates, planning targets |
| **Notifications** | `useNotifications` | Proactive events, read state, routing targets |

Display budgets enforced in `tools/dogfood/content/display_contract.py` — tied to `TripHeroCard.tsx`, itinerary block renderers, Atlas titles, etc.

### Manifest `surface_targets` vs backend reality

| Surface | Lisbon | Rome | Tokyo | Istanbul | Brooklyn | Seeded in manifest? |
|---------|--------|------|-------|----------|----------|-------------------|
| `trips_home` | **gap** | **gap** | **gap** | **gap** | n/a | Partial (`planning_brief` yes; hero cards no) |
| `trip_detail` | claimed | claimed | claimed | claimed | gap | Yes |
| `itinerary` | claimed | claimed | claimed | claimed | claimed | Yes |
| `stay` | claimed | claimed | claimed | claimed | gap | Authored assumptions, not booked rows |
| `costs` | claimed | claimed | claimed | claimed | gap | Demo expenses only |
| `discover` | claimed | claimed | claimed | claimed | claimed | Query fixtures yes |
| `atlas` | claimed | claimed | claimed | claimed | claimed | Artifacts yes |
| `receipts` | claimed | claimed | claimed | claimed | claimed | Observations + conversations |
| `group_chat` | implied S4 | partial | — | partial | — | Messages yes; thin |
| `proposals` | **missing** | partial | — | open in narrative | — | **Not in manifest schema** |
| `concierge_home` | **missing** | **missing** | **missing** | **missing** | **missing** | **Not seeded** |
| `notifications` | **missing** | **missing** | — | — | — | **Not seeded** |

**Contract gap:** Manifests claim `receipts` via observations/conversations but do not seed the **DB rows** that home feed and Changes screen actually read (`change_proposals`, `plan_events`, `vesper_cards`, `notification_deliveries`).

### Folio facet contract (from `trip-folio-facets.md`)

Folio hero ranker needs real values from:

| Facet | Source | Lisbon S4 today |
|-------|--------|-----------------|
| STAY | `useStaySummary` | Authored assumption only — no accommodation row |
| DECISIONS | `useOpenTripProposals` | **Empty** — no proposal rows |
| PLAN | `useTripPlanState` open_days | ✅ 2 open days |
| ROUTE | `useTransportGaps` / conflicts | Partial — no hard clash seeded |

**Result:** Folio renders but **DECISIONS facet is CTA/empty** — feels inert during wedge demo.

### Home feed card archetypes (from `backend/home/`)

`assemble_home_feed` composes cards from DB substrate. Rich dogfood needs rows that trigger:

| Card archetype | Priority | Seeded today? |
|----------------|----------|---------------|
| `pending_decision` (open proposal) | 94 | ❌ Lisbon |
| `constraint_meal` (dietary conflict) | 89 | ❌ (needs venue dietary fields + block) |
| `morning_brief` / digest | 86 | ❌ |
| `planning_brief` | 73 | Partial (`planning_brief` text on trip) |
| `group_state` (just accepted invite) | varies | ❌ |
| `booking_held` | 95 | ❌ (built-dark) |
| `settlement` | 71 | ❌ post-trip |

**Generating 1–2 open proposals + 1 constraint-meal block** would make Trips home and Concierge tab feel immediately more alive.

---

## Mock persona richness vs backend

### Richness tiers (frontend `PersonaBundle`)

| Tier | Personas | What makes them feel alive |
|------|----------|----------------------------|
| **Alive / demo-grade** | `carmen`, `ben`, `elif`, `dev` | Cross-linked trips, itinerary depth, Atlas, concierge threads, group chat |
| **Atlas-specialist** | `nadia`, `omar`, `between` | Atlas-only richness |
| **Hero-specialist** | `urgent`, `ready` | Narrow state machines (Porto vote, Kyoto imminent) |
| **Intentionally sparse** | `ana` | Cold start |
| **Legacy broad** | `default` | Wide but Lisbon-fallback heavy |
| **Adversarial** | `torture` | Layout stress |

### PersonaBundle fields — populated vs empty

| Field | Rich personas | Often empty |
|-------|---------------|-------------|
| `itineraryByTripId` | ben, carmen, dev, elif, ready | default → global Lisbon fallback |
| `conciergeHomeFeed` | ben, carmen, dev, torture | **elif** (flagship!) — lead-note only |
| `groupChatByTripId` | carmen, elif, dev | wedge personas |
| `planStateByTripId` | **ready only** | elif Rome, urgent |
| `situationByTripId` | **carmen only** | all others |
| `proposalsByTripId` | elif (Istanbul), urgent | blanket demo proposals pollute others |
| `discoverForYouRaw` | ana, ben, carmen, elif | others → Lisbon `mockForYouRaw` |
| `atlasArtifacts` | elif, nadia, omar, carmen | ben/ana forced empty |

### elif.ts vs backend S1–S6

| Scenario | Backend | Mock alignment | Gap |
|----------|---------|----------------|-----|
| S1 mature archive | All 6 packs | Strong Atlas; weak Concierge home | No Brooklyn S6; discover compose Lisbon |
| S2 Rome return | elif-rome | Rome trip + 6-day itin | No `planStateByTripId`; Folio shallow |
| S3 Istanbul | istanbul | Open proposal on Istanbul | Good narrative fit |
| **S4 Lisbon group** | mara pack | **No mara.ts** | **Largest wedge gap** |
| S5 Tokyo | tokyo | Atlas artifact | OK for Atlas-only |
| S6 Brooklyn | brooklyn | **Absent** | No local baseline in mock |

### What mock has that backend lacks (and vice versa)

| Mock richness | Backend richness |
|---------------|------------------|
| `conciergeHomeFeed` with Pick cards, holds (ben) | Composed from DB at request time — needs seed rows |
| `planStateByTripId` imminent hero (ready) | `plan_state` API — not in manifests |
| Live `situationByTripId` (carmen) | `situation` read model — not in manifests |
| Discover compose always Lisbon-anchored | Per-city discover fixtures in manifests |
| Torture/edge hostile states | Not in dogfood cohort |

**Ideal:** Manifest seeds backend; thin `PersonaBundle` projection for mock — not two divergent novels.

---

## What makes dogfood feel alive vs cardboard

### Alive signals (present in rich packs/personas)

1. **Cross-surface story coherence** — same companions, city names, beats across trips, Atlas, saves, notifications, concierge (Rome: Sarah/Mike; Lisbon: Dao shellfish everywhere).
2. **Authored itinerary rationale** — `energy_rationale`, `interlude`, `travel_to_next` on blocks (elif Rome 6-day arc).
3. **Atlas ↔ planning feedback** — signals echo in upcoming plan copy ("one anchor, open edges").
4. **Real media variety** — 30+ photo strip, gouache hero, not text-only Atlas.
5. **Private → group-safe synthesis** — constraints exist in DB without appearing in group chat copy.
6. **Open tail on itinerary** — proves planning-in-progress, not completed checklist.
7. **Pending vs kept Atlas states** — Istanbul proves review UX.
8. **Frozen `now` + phase** — live/returned/imminent heroes resolve correctly.

### Cardboard signals (still common on device)

1. **Empty DECISIONS facet** — no open proposals in DB.
2. **Concierge home with null feed** — elif flagship has lead-note only in mock; backend home feed empty without proposal/digest seeds.
3. **Trips home plain hero** — `trips_home` gap; fallback furniture instead of rich Vesper read.
4. **Demo expenses without receipt texture** — tagged `seeded_expense_demo`; no receipt images.
5. **3-message group chat** — feels like demo, not two weeks of coordination.
6. **Discover compose always Lisbon** — Rome persona browses Lisbon For-you rail.
7. **No notifications** — proactive tab empty.
8. **Local media 404 on Fly** — `local://dogfood/...` not mounted or not uploaded.
9. **Vote widget in chat without Changes screen parity** — metadata only; tapping through shows nothing.

---

## Systemic gaps blocking liveliness

### G1 — No proposal/vote DB rows (wedge-critical)

`product-moment-map.md` MG-S3 explicitly marks proposal seeding as **future**. Lisbon has `voting_enabled: true` and chat `vote_widget` metadata but **no `change_proposals`**.

**Impact:** J05 certified in pytest; **feels dead** on device in group chat → Changes → Folio DECISIONS facet.

**Generate:** 2 proposals on `mara-lisbon`:
- Proposal A: first-dinner venue swap (Casa do Alentejo vs Mouraria alternate) — `pending`, votes from dao/reza
- Proposal B: day-2 route shape — applied or rejected for contrast

### G2 — Trips home rich hero unsubstantiated

All trip packs declare `trips_home: gap`. Need:
- `planning_brief` ✅ already on trips
- **Hero destination media** — trip photo or place hero wired to Trips list
- **Composed Vesper read** — triggers from home feed anchor path; needs substrate for anchor compose or acceptable fallback

**Generate:** 1 hero photo per foreground trip linked in `trip_photos` with `hero: true`; verify `trip_note` / home anchor path with `AI_MODE=replay`.

### G3 — Home / Concierge feed empty

`assemble_home_feed` returns thin zones without proposals, digests, constraint meals, group-state events.

**Generate (Lisbon minimum):**
- 1 open `change_proposal` (see G1)
- 1 `daily_digest` or planning-brief card substrate for trip
- Optional: `constraint_meal` block where venue `dietary_*` conflicts with reza-shellfish

### G4 — Media not on Fly

159 assets staged locally. EAS dogfood build hits Fly — images 404 unless `upload_media.py` + `DOGFOOD_MEDIA_STATIC_ENABLED` on production-like target.

**Generate:** Upload P0 assets per pack (hero + atlas + 3 trip photos); verify `/dogfood-media/` on Fly.

### G5 — Mock/backend persona split

No `mara.ts`; elif mock ≠ S4 world; polish QA uses M11 not S4.

**Generate:** `mara.ts` PersonaBundle from `lisbon-phase1.yaml` projection (or hand-authored S4 slice).

### G6 — Product-moment-map GAPs still open

From `lisbon-phase1/product-moment-map.md`:

| Moment | Gap |
|--------|-----|
| MG-A3 | Discover board venue cards (3+ resolved) — partial; slugs exist |
| MG-A5 | Shellfish-safe lunch observation for day 2 |
| MG-S3 | Proposal rows before vote widget |
| EL-A1 | Atlas section body placeholder prose in places |
| EL-A3 | Full photo strip narrative on Atlas open |

### G7 — Brooklyn W1 + manifest ID drift

9 vs 20 photos; section references unwired IDs; no expenses. Fine for control — fix drift before using as S6 proof.

### G8 — Notifications / proactive layer unseeded

J09 logic QA green; **inbox feels empty**. No `proactive_events`, `notification_deliveries`, or push-worthy copy seeded.

**Generate:** 3–5 notifications per wedge account: proposal ready, invite accepted, planning nudge (group-safe copy).

---

## Generation backlog — prioritized

Impact on **felt liveliness** for wedge + Elif archive. Ordered P0 → P3.

### P0 — Wedge unblockers (do before TestFlight friend)

| # | Generate | Pack | Surfaces unlocked | Effort |
|---|----------|------|-------------------|--------|
| P0-1 | **2 `change_proposals` + votes** on `mara-lisbon` | Lisbon | Changes, Folio DECISIONS, group chat parity, J05 on device | Medium |
| P0-2 | **`mara.ts` mock persona** aligned with S4 | Frontend | Mock wedge without Lisbon fallback | Medium |
| P0-3 | **Upload P0 media to Fly** (6 Lisbon + 4 Rome heroes) | Lisbon, Rome | Atlas, trip journal, hero — no gray boxes | Low ops |
| P0-4 | **1 trip hero photo** flagged for Trips home per foreground trip | All W2 packs | Trips home rich hero | Low |
| P0-5 | **W3 app QA walk** — run lisbon + rome checklists | Lisbon, Rome | Validates everything else | Human |

### P1 — Home feed & concierge aliveness

| # | Generate | Pack | Surfaces unlocked | Effort |
|---|----------|------|-------------------|--------|
| P1-1 | **Daily digest row** or planning-brief home card substrate | Lisbon, Rome | Concierge home active zone | Medium |
| P1-2 | **constraint_meal card** — venue with dietary flags + dinner block | Lisbon | Home feed active; proves Reza constraint | Medium |
| P1-3 | **group_state card** — recent invite accept (sarah on Rome?) | Rome | Home "just joined" beat | Low |
| P1-4 | **`conciergeHomeFeed` for elif** in mock OR seed backend cards for elif@dogfood.local | Elif | Vesper tab feels flagship | Medium |
| P1-5 | **5–8 more group chat messages** — planning thread over 3 days | Lisbon | Group chat feels lived-in | Low authoring |

### P2 — Atlas / Discover depth

| # | Generate | Pack | Surfaces unlocked | Effort |
|---|----------|------|-------------------|--------|
| P2-1 | **Discover board venue cards** — close MG-A3 gaps (3 venues with facets) | Lisbon | Discover composed board | Medium |
| P2-2 | **Atlas section prose** — replace placeholder bodies; tie to signals | All artifacts | Atlas detail feels composed | Low authoring |
| P2-3 | **Shellfish-safe lunch observation** + block note day 2 | Lisbon | MG-A5; Reza arc | Low |
| P2-4 | **Persona-scoped discover compose anchor** — Rome queries return Rome corpus | Rome | Discover feels city-native | Backend |
| P2-5 | **2–4 riso/postcard assets** per kept trip | Rome, Tokyo | Post-trip warmth (built-dark but visible in Atlas) | Media gen |

### P3 — Breadth & future promotion

| # | Generate | Pack | Notes |
|---|----------|------|-------|
| P3-1 | **Carmen CDMX full manifest** from skeleton | carmen-cdmx-live | M3 promotion; P0 in promotion specs |
| P3-2 | **ana@dogfood.local** cold-start backend account | M1 | P1 promotion |
| P3-3 | **Barcelona light chapter** | elif ledger | Breadth; no world yet |
| P3-4 | **Seoul future-saved-idea** rows | elif ledger | Non-Europe breadth |
| P3-5 | **Brooklyn W2 upgrade** — stay, cost, coverage | Brooklyn | Only if S6 needs trip ops |
| P3-6 | **Manifest → PersonaBundle codegen** | All | Long-term mock/backend unity |

---

## Per-surface generation guide

What to author for each surface to cross from "structurally correct" to "lively."

### Trips home

**Needs:**
- Foreground trip with correct phase vs `now`
- `planning_brief` (have)
- Hero image URL resolving on device
- Optional: home feed anchor composed (or strong fallback template)

**Generate:**
- 1 cinematic trip photo per hero trip (inventory already lists P0 targets)
- Seed script hook: mark `trip_photos[].is_hero = true`
- Run Elif/Lisbon checklist §Trips home after seed

**Avoid:** Generic "Your trip to Lisbon" without Vesper read or media.

---

### Trip Folio

**Needs:**
- `/folio` read model: spine block ids matching plan
- Open proposals → DECISIONS facet `needs`
- Stay summary → STAY facet `ok` or `needs`
- Transport gaps or conflicts → ROUTE facet

**Generate:**
- Proposals (P0-1)
- Optional `trip_accommodations` planning row for Baixa apartment (not booked, but STAY label)
- 1 soft transport gap for ROUTE `needs` (optional)

---

### Plan / itinerary

**Needs:**
- 2–4 blocks/day on seeded days with `energy_rationale`
- Open days in `itinerary_coverage`
- Grounded `venue_slug` or `experience_slug` on blocks

**Already strong on Rome/Lisbon.** Generate:
- 1–2 more blocks on Lisbon open days (tentative, not over-planned)
- Shellfish-safe lunch block day 2

---

### Changes / proposals

**Needs:**
- `change_proposals` with `proposal_type`, `status`, `votes`, `rationale_group_safe`
- Applied change → `recent_changes` / plan_events
- Revert candidate for J05 live demo

**Generate:** See P0-1. Mirror structure from `test_j05_proposal_plan_mutation.py` fixtures.

---

### Group chat

**Needs:**
- 8–15 messages across 2–3 threads
- Mix: human, Vesper, vote_widget, change_applied
- Tone: knowledgeable friend, not bot

**Generate:**
- Extend `mara-lisbon-arrival` thread with post-vote acknowledgment
- Add `mara-lisbon-dinner-debate` thread with 4 messages

---

### Concierge home (Vesper tab)

**Needs:**
- `conciergeHomeFeed` cards OR backend-composed `vesper_cards`
- Now/Next deck with real focus layouts

**Generate:**
- Backend: open proposal card + planning brief card for elif/mara accounts
- Mock: expand `elif.conciergeHomeFeed` to match Rome return planning (mirror ben/carmen pattern)

---

### Discover

**Needs:**
- Query fixtures → composed boards with title, sections, entity cards
- Personal frame from Atlas signals (Elif)

**Generate:**
- Resolve remaining entity cards for `mara-arrival-dinner-search`, `elif-food-transit-board`
- 2+ venue cards with slope/group-fit metadata for Lisbon

---

### Atlas

**Needs:**
- Artifact with hero, photo strip (10+), sections, signals, one_line_read
- Pending vs kept status (Istanbul)

**Already strong.** Generate:
- Fix Brooklyn photo_id wiring
- 2–3 more section bodies with evidence-grounded prose (not diagnostic)
- Companion photos per ledger (Sarah hands at table, etc.)

---

### Costs / expenses

**Needs:**
- 3–6 expense rows with realistic splits
- Optional receipt image URLs
- Settle balance ≠ 0 for post-trip demo (J12)

**Generate:**
- Lisbon: local transport row (€45 authored → seeded row)
- Rome: food estimate row beyond holds
- Receipt JPG assets (inventory entries) for 2 expenses

---

### Notifications

**Needs:**
- `proactive_events` with correct `target_audience` (private vs group)
- Read/unread mix

**Generate:**
- 3 notifications for mara@dogfood.local: proposal ready, member joined, planning nudge
- 2 for elif@dogfood.local: Rome return reminder, Atlas artifact ready

---

## Per-pack next actions

### Lisbon — **do first** (S4 wedge)

1. Add `change_proposals` + votes to manifest → seed → verify Changes UI
2. Add `trip_accommodations` planning row (optional STAY facet)
3. Extend group chat to 12+ messages
4. Close MG-A5 shellfish observation
5. Upload 6 P0 trip photos + atlas hero to Fly
6. Run `lisbon-dogfood-push-checklist.md` app QA → set `app_qa_status: passed`
7. Create `mara.ts` mock persona

### Rome — **do second** (S2 proof)

1. Seed departure-readiness / planning-brief home card substrate
2. Verify Atlas → Discover → itinerary loop per `rome-dogfood-push-checklist.md`
3. Trips home hero photo for `elif-rome-return-2026`
4. W3 app QA

### Istanbul — **pending UX proof**

1. Ensure pending artifact renders differently from kept
2. App QA for S3 narrative (uncertain copy, no overconfidence)

### Tokyo — **Atlas/discover only**

1. Do not over-build itinerary; verify counter-DNA boards
2. Cross-trip bridge query in Discover

### Brooklyn — **control sample**

1. Fix manifest ↔ inventory photo_id drift
2. Do not upgrade to W2 unless S6 requires trip ops

### Elif profile — **synthesis**

1. Ensure city packs seed before profile overwrites observations
2. Use for Discover personal frame, not trip ops

---

## Companion & media generation targets

From `elif-canonical/ledger.md` §Asset Targets and §Companion Ledger.

### Companion visual presence (authored media briefs)

| Companion | Show as | Chapters |
|-----------|---------|----------|
| Sarah | Walking ahead, hands at table, transit profile | Rome, Tokyo, Istanbul, Barcelona |
| Mike | Group table energy, tradeoff conversations | Rome return, Istanbul return |
| Solo Elif | Counters, notebooks, corridors, market thresholds | Lisbon, Brooklyn, Tokyo |

**Generate:** 3–5 Sarah partial-presence photos per Rome/Tokyo pack (ledger target); not full companion POV stories.

### Accepted media counts per chapter (ledger)

| Chapter | Target assets |
|---------|--------------:|
| Lisbon | 34 (have) |
| Rome | 36 (have) |
| Tokyo | 33 (have) |
| Istanbul | 30 (have) |
| Brooklyn | 20 (have) |
| Barcelona | 15 (future) |
| Marrakech | 20 (future) |
| Oaxaca | 18 (future) |
| Seoul | 15 (future) |

**Core packs are at target counts.** Quality issue is **wiring + Fly delivery**, not volume.

### Media types that increase perceived life

| Type | Where it shows | Priority |
|------|----------------|----------|
| **Trip journal photos** | Folio, trip memory, hero | P0 |
| **Atlas photo strips** | Atlas detail scroll | Have — verify on device |
| **Gouache/riso renders** | Atlas hero, Discover board | Have — verify paint |
| **Receipt photos** | Expense detail | P2 — missing |
| **Companion partials** | Atlas sections, group chat context | P2 |
| **Destination hero** | Trips home card background | P0 |

---

## What not to generate yet

| Don't | Why |
|-------|-----|
| New city packs before S4 W3 | Wedge doc: no new substrate until dogfood-ready |
| Full Barcelona/Seoul/Bangkok worlds | Ledger: mock-only / later |
| LLM-invented substrate at seed time | Violates dogfood authoring rule; use Cursor-assisted YAML |
| 50 more mock personas | 12 is enough; deepen S4 + elif |
| Fake booking confirmations | Built-dark; forbidden fallbacks in S2 |
| Completed-trip claims on planning trips | Breaks scenario contracts |
| Monument-checklist itineraries | Forbidden in S3, S5, S6 |

---

## Verification checklist

After generation sprint, verify liveliness (not just `validate` + `trip_realism_audit`).

### Backend (per pack)

```bash
cd travel-agent
PYTHONPATH=. python -m tools.dogfood.content.validate manifests/<pack>.yaml
PYTHONPATH=. python -m tools.dogfood.content.dogfood_pack_readiness <pack-id>
python scripts/dogfood_audit.py --summary --persona <email>
```

### App (W3 — human)

Use pack checklists:
- `sources/lisbon-phase1/...` → `lisbon-dogfood-push-checklist.md`
- `sources/elif-canonical/rome-dogfood-push-checklist.md`

**Liveliness spot-checks:**

- [ ] Atlas artifact opens with hero + 10+ photo strip painted
- [ ] Discover query returns composed board with specific title (not "Top 10")
- [ ] Group chat has 8+ messages; vote widget opens real proposal
- [ ] Changes screen shows open proposal with voter names
- [ ] Folio DECISIONS facet shows open vote (not "Add one →")
- [ ] Trips home shows destination media + Vesper read (not plain fallback)
- [ ] Concierge tab has ≥1 active card (not empty deck)
- [ ] Costs show 3+ rows with plausible splits
- [ ] Notifications inbox has 2+ unread items
- [ ] No private constraint visible in group-visible copy (I4)

### Cross-surface (J06)

- [ ] After proposal accept: Plan, Map, Changes, Folio spine share block ids

---

## Key file index

| Topic | Path |
|-------|------|
| Pack registry | `travel-agent/tools/dogfood/content/packs.yaml` |
| Scenario registry | `travel-agent/tools/dogfood/content/scenarios.yaml` |
| Lisbon manifest | `travel-agent/tools/dogfood/content/manifests/lisbon-phase1.yaml` |
| Product moment map (generation spec) | `travel-agent/tools/dogfood/content/sources/lisbon-phase1/product-moment-map.md` |
| Persona dossiers | `travel-agent/tools/dogfood/content/sources/lisbon-phase1/persona-dossiers.md` |
| Elif chapter ledger | `travel-agent/tools/dogfood/content/sources/elif-canonical/ledger.md` |
| Pack readiness snapshot | `travel-agent/tools/dogfood/content/sources/elif-canonical/qa/current-pack-readiness-2026-06-25.md` |
| Lisbon app QA checklist | `travel-agent/tools/dogfood/content/sources/elif-canonical/lisbon-dogfood-push-checklist.md` |
| Rome app QA checklist | `travel-agent/tools/dogfood/content/sources/elif-canonical/rome-dogfood-push-checklist.md` |
| Media inventory (Lisbon) | `travel-agent/tools/dogfood/content/media/lisbon-phase1/inventory.yaml` |
| Display copy budgets | `travel-agent/tools/dogfood/content/display_contract.py` |
| Trip realism audit | `travel-agent/tools/dogfood/content/trip_realism_audit.py` |
| Pack readiness runner | `travel-agent/tools/dogfood/content/dogfood_pack_readiness.py` |
| Home feed assembler | `travel-agent/backend/home/feed.py` |
| Folio facet spec | `travel-app/docs/page-specs/trip-folio-facets.md` |
| Persona registry | `travel-app/constants/personas/index.ts` |
| Companion QA investigation | `docs/working/dogfood-qa-substrate-system-investigation-2026-06-28.md` |

---

## Bottom line

**Substrate richness:** W2 authorial depth is real — 159 media assets, grounded venues, Atlas artifacts with 30+ photos each, persona dossiers with product-moment maps. You are not starting from empty.

**Frontend contract:** Manifests cover itinerary, Atlas, discover fixtures, and demo expenses well. They **do not** seed the DB rows that Trips home, Concierge feed, Changes, and Folio DECISIONS actually read — proposals, home cards, digests, notifications.

**Personas:** Backend S4 (Mara group) has no frontend mirror. Mock elif is rich in Atlas/itinerary but **thin on Concierge home** — the flagship tab feels quiet.

**To make dogfood feel much more lively, generate in this order:**

1. **Proposal + vote rows** on Lisbon (unlocks wedge feel everywhere)
2. **Fly media upload** for heroes (unlocks visual life)
3. **Home feed seeds** (1 digest + 1 constraint card)
4. **`mara.ts` + extended group chat**
5. **W3 app QA** on Lisbon and Rome

That is fewer than 20 targeted authoring tasks — not a new pack empire — and it converts structural W2 richness into something a human would describe as *"this group is actually planning a trip."*
