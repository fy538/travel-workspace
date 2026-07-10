---
doc_type: archive
status: archived
owner: founder / engineering
created: 2026-07-09
archived: 2026-07-09
why_new: Move reviewed completed evidence out of the living documentation tree without deleting its historical record.
---

# Dogfood Corpus Connection Plan — One World Graph for Lived Substrate

> Archived from the living documentation tree on 2026-07-09 during Phase 5 cleanup.

> Status: execution plan
> Owner: founder / engineering
> Created: 2026-06-28
> Last updated: 2026-06-28
> Scope: `travel-agent` world corpus (A + B) ↔ dogfood manifests ↔ product surfaces
> Companion to:
> - `dogfood-substrate-richness-and-generation-backlog-2026-06-28.md`
> - `dogfood-qa-substrate-system-investigation-2026-06-28.md`
> - `dogfood-place-illustration-coverage-gap-2026-06-28.md`

**Question this doc answers:** How do we connect the deep world we already seeded (venues, experiences, editorial dossiers) to dogfood itineraries and discover fixtures so dogfood feels *real* — not a parallel YAML fiction?

---

## TL;DR

**Yes — connecting pipelines A and B to dogfood manifests is the highest-leverage move for experiential richness.**

Today you have three layers built independently:

| Layer | What exists | Dogfood uses |
|-------|-------------|--------------|
| **A — JSON seed** (`tools/seed/`) | Lisbon ~104 venues, Brooklyn ~26, promoted batches + briefs | **8 Lisbon slugs** via thin `import_staged_refs` |
| **B — Editorial** (`content/staging/` + `import_cursor_dossiers.py`) | Lisbon 304, Rome 314 editorial dossiers | **Not imported for dogfood** |
| **Dogfood manifests** | Trips, blocks, discover query contracts, atlas | Slugs often stub-only; queries **log-only** (no DB rows) |

**Target:** Manifest becomes a **projection** over one slug graph. Every itinerary block, entity save, and discover fixture points at entities that exist in Postgres **with briefs/dossiers in Qdrant**.

**Scope discipline:** Lisbon (S4 wedge) + Rome (S2 elif flagship) first. Istanbul connect A only; editorial B later. Do not wire all 34 editorial cities.

---

## Table of contents

1. [Why this matters](#why-this-matters)
2. [Data classification: catalog vs fixtures (staging vs prod)](#data-classification-catalog-vs-fixtures-staging-vs-prod)
3. [Current architecture (broken connection)](#current-architecture-broken-connection)
4. [Target architecture (one world graph)](#target-architecture-one-world-graph)
5. [Inventory — what we have vs what dogfood uses](#inventory--what-we-have-vs-what-dogfood-uses)
6. [Connection model (A + B + manifest)](#connection-model-a--b--manifest)
7. [Phased execution plan](#phased-execution-plan)
8. [Phase 1 — Lisbon (S4 wedge)](#phase-1--lisbon-s4-wedge)
9. [Phase 2 — Rome (S2 elif flagship)](#phase-2--rome-s2-elif-flagship)
10. [Phase 3 — Istanbul + Tokyo (compact canonical)](#phase-3--istanbul--tokyo-compact-canonical)
11. [Phase 4 — Mock parity (frontend)](#phase-4--mock-parity-frontend)
12. [Tooling & validation gates](#tooling--validation-gates)
13. [Events & Discover specifics](#events--discover-specifics)
14. [Relationship to parallel streams](#relationship-to-parallel-streams)
15. [What not to do](#what-not-to-do)
16. [Acceptance criteria (W3 + liveliness)](#acceptance-criteria-w3--liveliness)
17. [Key file index](#key-file-index)

---

## Why this matters

Dogfood currently passes logic QA (J01–J12) while still feeling **cardboard on device** because:

1. **Itinerary blocks** reference slugs that resolve to thin Postgres rows (no brief, no dossier, no Qdrant).
2. **Discover query fixtures** (29 across packs) are **authoring contracts only** — `seed_discover_queries()` logs them; compose reads live corpus at runtime.
3. **Discover boards** expect entities (lx-factory, crisfama, Testaccio market) that **exist in promoted corpus or search-board-contract** but **not in manifest corpus refs**.
4. **Events** — few dated `experiences` in trip windows; mock detail layer is Lisbon-only with orphan `experience_id`s.
5. **Vesper retrieval** needs Qdrant embeddings; `import_staged_refs` skips embed entirely.

Connecting A+B fixes richness at the **source** — Plan, Discover, Atlas, and Vesper all consume the same slug graph instead of parallel fictions.

---

## Data classification: catalog vs fixtures (staging vs prod)

> Added 2026-06-28 — the foundational decision that governs how this plan touches production.

A natural worry: *"the cities we seeded might not be the final content — should this be kept separate from production, like a staging vs prod thing?"* The answer is **two different answers**, because what we built is **two data classes with opposite lifecycles**. Conflating them is the trap.

| | **Catalog (world corpus — A + B)** | **Fixtures (lived substrate — manifests)** |
|---|---|---|
| Examples | Lisbon's ~104 venues, 304 dossiers, experiences | Mara's group trip, Elif's Rome return, `@dogfood.local` users |
| Who should ever see it | **Real users** — a real Lisbon trip *should* surface these venues | **Nobody real** — pure demo/test scaffolding |
| Lifecycle | Grows, curated, **becomes the product** | Throwaway, resettable, discarded |
| "Final content?" | Always in-progress (catalogs never are "final") | Never meant to be content |
| Right home | **Production**, quality-gated | **Isolated** (cohort now, separate backend later) |
| Separation concern | Quality, not isolation | Isolation (analytics, exposure, privacy) |

**This reframes the worry:** seeding Lisbon/Rome/etc. is *not* throwaway dev work. The **pipeline** (cartographer → promote → embed) is the durable asset, and the corpus is reusable/extendable even if launch cities change. You built the machine and proved it on real cities. Nothing is wasted.

### Catalog → belongs in production (staging is a *gate*, not an *environment*)

Good practice for reference/seed content is **content staging as a promotion gate**, which you already have:

```text
author (Cursor) → tools/seed/staging/ → validate + spot_check → promote → PRODUCTION
```

That `staging/` directory *is* the staging concept. You don't need a staging *environment* for catalog — you need a **quality bar** before promotion. (Same pattern as a product catalog / CMS publish flow.) The only thing to tighten: `spot_check` is currently a soft 1-in-5 sample — fine for proof cities, not for content a paying user will see.

### Fixtures → must never pollute prod (cohort isolation is fine for now)

The real isolation risks live here:

- **Analytics pollution** — fake trips in funnel metrics (this *will* bite at fundraise time when engagement numbers are half Mara).
- **Accidental exposure** — a bug surfaces a `@dogfood.local` user or Mara's trip in a real Discover/social feed.
- **Privacy egress** — dogfood private constraints leaking cross-cohort.

Current guard (`@dogfood.local`, `_dogfood` metadata, `--allow-prod` gate, egress guard) is **defensible and standard for pre-funding MVP**. A second full backend now is premature ops cost for a one-founder loop.

### The good-practice rule

> Treat **world corpus as production content** (keep in prod, gate on quality, grow it) and **lived fixtures as resettable test scaffolding** (cohort-isolate now, separate backend only when a real external user or clean analytics forces it).

### Two new concepts this plan adopts

**1. Corpus quality tier (distinct from W0–W3).** The W0–W3 ladder measures *"is this fixture rich enough to demo."* It does **not** measure *"is this venue content good enough to ship to a paying user."* Different bars. Tag each city's corpus:

| Tier | Meaning | Quality bar |
|------|---------|-------------|
| `proof_only` | Exists to prove the app during dev/MVP | Loose — spot_check sample OK; may be rough |
| `launch_candidate` | Real users may consume it | Full review; brief/dossier quality verified; no placeholder copy |

Lisbon/Rome are the first `launch_candidate` candidates (wedge + flagship); Tokyo/Brooklyn can stay `proof_only`.

**2. Pre-funding guardrails (cheap, do soon — none require a new environment):**

- [ ] **Analytics exclusion** of the `_dogfood` cohort by default (cheapest insurance for fundraise-time metrics)
- [ ] **Egress filter** so dogfood users/trips never appear in a real user's feeds (extends existing privacy egress guard)
- [ ] **One-command fixture reset** so reseeding never feels risky on shared prod

### When to split a dedicated `vesper-backend-dogfood` (trigger checklist)

Split when **any one** is true (mirrors the QA investigation doc):

- [ ] External TestFlight testers create **real** data alongside fixtures
- [ ] Real users exist whose analytics must be clean (e.g. active fundraising)
- [ ] Destructive reset/reseed is frequent enough to be scary on shared prod

Until then: shared backend + cohort boundaries + `dogfood_audit.py`.

---

## Current architecture (broken connection)

```text
┌─────────────────────────────────────────────────────────────────────────┐
│  A — tools/seed/staging → promote → Postgres + Qdrant embed             │
│     (104 Lisbon venues, 20 experiences, briefs, place_angles)         │
└───────────────────────────────┬─────────────────────────────────────────┘
                                │ import_staged_refs (THIN: rows only)
                                ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  B — content/staging/{city}/*.md → import_cursor_dossiers.py            │
│     (304 Lisbon, 314 Rome editorial dossiers)                          │
│     ╳ NOT CALLED for dogfood                                          │
└───────────────────────────────┬─────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  Dogfood manifest → seed.py → trips, blocks, observations, atlas       │
│     discover_queries → LOG ONLY (no DB)                                 │
│     8 venue slugs referenced vs 104 promoted                          │
└───────────────────────────────┬─────────────────────────────────────────┘
                                ▼
                         App surfaces (thin)
```

**Cartographer** = stage 1 of pipeline B (documented in `scripts/import_cursor_dossiers.py` header): cartographer → scout → angles → write → import. Not a separate tool.

---

## Target architecture (one world graph)

```text
Authoring (Cursor-assisted)
  │
  ├─ A: tools/seed/staging/*.json
  │      validate → promote → Postgres entities + briefs
  │      embed → Qdrant (venue_briefs, experience_briefs, place_angles)
  │
  ├─ B: content/staging/{city}/*.md
  │      import_cursor_dossiers.py → dossiers + brief upsert + Qdrant
  │
  └─ Manifest: picks subset + adds LIVED substrate
         trips, members, constraints, observations, atlas, conversations
         itinerary blocks → venue_slug / experience_slug (MUST ∈ corpus)
         discover_queries → entity refs (MUST ∈ corpus)
         entity_saves → same slugs
         proposals, expenses, trip_photos (lived rows — not in A/B)
              │
              ▼
         seed.py → Postgres (lived + refs resolve to world rows)
              │
              ▼
         App: Plan block → real venue → dossier in Discover/Vesper
```

**Principle:** Manifest **references** the world; it does not **duplicate** venue copy or invent parallel entity IDs.

---

## Inventory — what we have vs what dogfood uses

### World corpus depth (A + B)

| City | Promoted venues | Experiences (batches) | Editorial MD (`content/staging/`) | Dogfood manifest refs |
|------|----------------:|----------------------:|----------------------------------:|----------------------:|
| **Lisbon** | ~104 | ~20 | **304** | 8 venues, 1 experience |
| **Brooklyn** | ~26 | ~25 | 0 | 3 venues, 2 experiences |
| **Rome** | 4 (canonical bundle) | 3 | **314** | 4 venues, 3 experiences, 1 site |
| **Istanbul** | 3 (canonical) | **6** | **0** | 19 refs (rich manifest, thin world) |
| **Tokyo** | 6 (canonical) | 1 | **0** | 12 refs |

### Editorial-only cities (no dogfood pack)

**34 cities** in `content/staging/` with 200–300 dossiers each (Venice, Madrid, Florence, Paris, Barcelona, Athens, …). Latent asset — **out of scope** until a scenario needs them.

### Dogfood manifest substrate (lived layer — stays in manifests)

| Entity type | Lisbon | Rome | Istanbul | Tokyo | Brooklyn |
|-------------|-------:|-----:|---------:|------:|---------:|
| Trips | 1 | 2 | 2 | 1 | 1 |
| Itinerary blocks | 4 | 8 | 8 | 7 | 6 |
| Discover queries | 11 | 4 | 6 | 4 | 4 |
| Observations | 11 | 6 | 8 | 6 | 5 |
| Atlas artifacts | 1 | 1 | 1 | 1 | 1 |

### Critical wiring gaps (verified 2026-06-28)

| Gap | Evidence |
|-----|----------|
| `import_staged_refs` skips briefs, dossiers, Qdrant | `import_staged_refs.py` — structured columns only |
| `seed_discover_queries` is log-only | `seed.py` lines 832–839 — prints `"would record"`, no INSERT |
| Lisbon discover queries reference unstaged entities | `search-board-contract.md` — lx-factory, crisfama, azulejo site, time-out-market |
| Mock compose always Lisbon | `discoverCompose.ts` `ANCHOR_SLUG = 'lisbon'` |
| Mock place dossiers: 4 cities only | `mockPlaceAngles`: lisbon, rome, paris, amalfi-coast |

---

## Connection model (A + B + manifest)

For each dogfood city pack, execute **five connection steps**:

| Step | Action | Owner |
|------|--------|-------|
| **1. Audit** | Run `corpus_refs.py` — manifest slugs vs staging vs DB | Engineering |
| **2. Expand refs** | Add manifest `corpus_refs` / block slugs / discover entity targets to match search-board-contract + itinerary needs | Authoring |
| **3. Import A (full)** | `promote` (if batches pending) + embed scripts for briefs/angles | Ops |
| **4. Import B** | `import_cursor_dossiers.py --city {city}` for cities with editorial staging | Ops |
| **5. Seed lived** | `seed.py --apply` for manifest (trips, blocks, saves, atlas — not discover query logs) | Ops |

**Slug rule:** Every `venue_slug`, `experience_slug`, `site_slug` on an itinerary block and every entity named in a discover query **must** resolve in `corpus_refs` audit before W3 sign-off.

**New manifest fields (optional, Phase 2 engineering):**

- `corpus_refs:` explicit list of slugs the pack depends on (machine-checkable)
- Or derive refs automatically from blocks + discover_queries + entity_saves in `validate.py`

---

## Phased execution plan

| Phase | City / scope | A (promote+embed) | B (dossiers) | Manifest expansion | Priority |
|-------|--------------|-------------------|--------------|-------------------|----------|
| **1** | Lisbon S4 wedge | Full stack | `--city lisbon` | search-board-contract closure | **P0** |
| **2** | Rome S2 elif | Canonical + embed | `--city rome` | Return-planning discover + events | **P0** |
| **3** | Istanbul S3 | Canonical + embed | **Author new** (0 MD today) | Venue slugs on blocks | **P1** |
| **3b** | Tokyo S5 | Canonical + embed | Optional thin set | Memory beats only | **P2** |
| **4** | Mock parity | N/A | N/A | Same slugs in `mara.ts`, elif compose | **P1** |
| **5** | Brooklyn S6 | Already promoted | N/A (JSON-only) | Expand refs, fix photo drift | **P2** |
| **—** | 34 editorial cities | — | — | Only when scenario exists | **P3** |

**Do not start Phase 3 Istanbul editorial until Lisbon W3 passes** (wedge doc discipline).

### Target environment (ties to the catalog-vs-fixture decision)

Where you run the import matters, and it follows directly from [Data classification](#data-classification-catalog-vs-fixtures-staging-vs-prod):

| Target | When | How |
|--------|------|-----|
| **Local dogfood DB** | Phase 1–2 authoring/iteration; mock + local-real walks | Default DSN; no `--allow-prod` |
| **Fly (`vesper-backend`)** | To feel the win on an **EAS dogfood build** (it hits Fly, `USE_MOCK=false`) | Point DSN at Fly + `--allow-prod` on `import_staged_refs` |

**Key consequence of the catalog decision:** importing Lisbon/Rome **corpus + dossiers** to Fly is *correct, not a violation* — catalog is production content. Only the **fixture** seed (`seed.py` trips/`@dogfood.local` users) is the cohort-guarded, prod-data-sensitive step. So: promote/embed/dossiers → Fly freely (quality-gated); `seed.py --apply --allow-prod` → deliberate, cohort-scoped, resettable.

> ⚠️ Safety caveat: `import_cursor_dossiers.py` connects via `backend.core.db.engine.get_connection` and has **no `--allow-prod` mutation guard** (unlike `import_staged_refs` and `seed.py`). It writes to **whatever DB the engine DSN resolves to**, and auto-creates missing neighborhood places via Nominatim geocoding (a network call) at import time. Always `--dry-run` first and set the DSN deliberately before any Fly-targeted run. It also reads from `content/staging/<city>/`, so run from the `travel-agent` repo root.

---

## Phase 1 — Lisbon (S4 wedge)

**Goal:** Mara group trip where every block, discover query, and vote references real seeded entities with dossier depth.

### 1A — Corpus import (A + B)

> Note: manifest-path tools (`corpus_refs`, `import_staged_refs`, `validate`, `seed`)
> take the **full repo-root path** `tools/dogfood/content/manifests/<pack>.yaml`
> (per their own `--help`/docstrings). `dogfood_pack_readiness` takes a **pack id**.
> Run all commands from the `travel-agent` repo root with `PYTHONPATH=.`.

```bash
cd travel-agent

# Audit first (read-only; lists manifest slugs vs staging vs DB)
PYTHONPATH=. python -m tools.dogfood.content.corpus_refs \
    tools/dogfood/content/manifests/lisbon-phase1.yaml

# A: ensure promoted + embedded (if not already on target DB).
# Lisbon venues are already promoted (33→136 per tools/seed/README.md); embed is
# idempotent. These embed scripts are GENERAL (Postgres → Qdrant), not city-flagged —
# only Brooklyn has dedicated embed_brooklyn_*.py scripts.
PYTHONPATH=. python -m tools.seed.validate            # validates staging batches
PYTHONPATH=. python scripts/embed_eval_briefs.py       # venue briefs → Qdrant
PYTHONPATH=. python scripts/embed_experience_briefs.py # experience briefs → Qdrant
PYTHONPATH=. python scripts/embed_place_angles_staging.py

# B: full editorial depth (304 Lisbon dossiers in content/staging/lisbon/)
PYTHONPATH=. python scripts/import_cursor_dossiers.py --city lisbon --dry-run  # preview
PYTHONPATH=. python scripts/import_cursor_dossiers.py --city lisbon            # apply

# Thin bridge (only for manifest slugs not covered by promote/dossiers)
PYTHONPATH=. python -m tools.dogfood.content.import_staged_refs \
    tools/dogfood/content/manifests/lisbon-phase1.yaml --apply
```

### 1B — Manifest expansion (authoring)

Cross-reference `sources/lisbon-phase1/search-board-contract.md` and `product-moment-map.md`:

| Moment / query | Action |
|----------------|--------|
| **MG-A3** — Discover board venue cards (3+ resolved) | Wire slugs for mara-arrival-dinner-search board entities |
| **MG-A5** — Shellfish-safe lunch day 2 | Block + observation; venue with dietary facet |
| Unstaged refs in contract | Add to manifest or promote: lx-factory, crisfama, azulejo site, time-out-market (per contract notes) |
| Itinerary blocks (4 → 6+) | Ground all blocks on promoted slugs; add 1–2 tentative open-day blocks |
| **Events** | 2–3 dated `experiences` in Oct 2026 window (fado, market morning) — slugs from promoted batches |

Current block slugs (keep, verify in corpus): `casa-do-alentejo-baixa`, `o-raposo-intendente`.

### 1C — Lived substrate (may overlap Stream B)

- 2 `change_proposals` + votes (if not done by wedge substrate stream)
- Hero photo flag on trip
- Extended group chat

### 1D — Verify

```bash
PYTHONPATH=. python -m tools.dogfood.content.validate \
    tools/dogfood/content/manifests/lisbon-phase1.yaml
PYTHONPATH=. python -m tools.dogfood.content.dogfood_pack_readiness lisbon-phase1   # pack id
PYTHONPATH=. python scripts/dogfood_audit.py --summary --persona mara@dogfood.local
```

**Manual W3 spot-checks:**

- [ ] Tap itinerary dinner block → venue detail with brief/dossier copy (not stub)
- [ ] Run discover query `mara-arrival-dinner-search` → composed board with ≥3 entity cards
- [ ] Vesper ask about first dinner → retrieval cites seeded venue (not confabulation)
- [ ] Event card in trip window resolves on tap-through

---

## Phase 2 — Rome (S2 elif flagship)

**Goal:** Return-planning loop where Atlas memory, discover, and itinerary share Rome corpus slugs.

### 2A — Corpus import

```bash
cd travel-agent

# Canonical bundle already aligned 11/11 with manifest refs
PYTHONPATH=. python -m tools.dogfood.content.import_staged_refs \
    tools/dogfood/content/manifests/elif-rome.yaml --apply

# Full editorial depth (314 Rome dossiers in content/staging/rome/)
PYTHONPATH=. python scripts/import_cursor_dossiers.py --city rome --dry-run  # preview
PYTHONPATH=. python scripts/import_cursor_dossiers.py --city rome            # apply

# Embed briefs + experiences (idempotent)
PYTHONPATH=. python scripts/embed_eval_briefs.py
PYTHONPATH=. python scripts/embed_experience_briefs.py
```

### 2B — Manifest expansion

| Area | Action |
|------|--------|
| Discover queries (4 → 6) | Departure-readiness, Testaccio market, Trastevere evening |
| Events | 1–2 dated experiences on `elif-rome-return-2026` window (opera, evening walk) |
| Itinerary | Verify all 8 blocks grounded; heat-aware blocks keep venue slugs |

Existing slugs: `rome-market-testaccio`, `rome-venue-roscioli-style-reservation`, `rome-experience-tiber-river-dusk-walk`, etc.

### 2C — Verify

- [ ] Discover compose for elif Rome trip city returns Rome corpus (not Lisbon fallback on backend)
- [ ] Atlas artifact sections reference same slugs as itinerary saves

---

## Phase 3 — Istanbul + Tokyo (compact canonical)

**Istanbul:** Richest experience set (6) but **zero editorial dossiers**. Phase 3A = connect A only (canonical JSON + embed + import_staged_refs). Phase 3B = new cartographer editorial pass (separate authoring project).

**Tokyo:** Memory-beat pack by design — generic venue anchors acceptable. Connect A, add 1–2 experiences, do not over-build editorial.

---

## Phase 4 — Mock parity (frontend)

Backend-real connection does not fix mock mode automatically. After Phase 1–2 slug graph is stable:

| Task | File / area |
|------|-------------|
| Add `mockPlaceAngles` for Istanbul, Tokyo (minimum) | `constants/mocks/angles.ts` |
| City-scoped discover compose (elif → Rome when on Rome trip) | `utils/api/mock/discoverCompose.ts` |
| Persona fixtures use same slugs as manifest | `mara.ts`, `elif.ts` |
| Fix orphan for-you `experience_id`s | `constants/mocks/discover.ts` + experience detail mock |
| Experience detail rows for Rome/Istanbul event IDs | `utils/api/mock/` or shared fixture module |

**Rule:** Mock slugs = manifest slugs = promoted slugs. No third namespace.

---

## Tooling & validation gates

### Existing tools to use

| Tool | Path | Role |
|------|------|------|
| Corpus audit | `tools/dogfood/content/corpus_refs.py` | Manifest slugs vs staging vs DB |
| Thin import | `tools/dogfood/content/import_staged_refs.py` | Minimal rows (fallback only) |
| Full editorial | `scripts/import_cursor_dossiers.py` | Dossiers + Qdrant |
| JSON promote | `tools/seed/promote.py` | Postgres entities + briefs |
| Embed | `scripts/embed_eval_briefs.py`, `embed_experience_briefs.py`, … | Qdrant |
| Manifest validate | `tools/dogfood/content/validate.py` | Schema + media |
| Pack readiness | `tools/dogfood/content/dogfood_pack_readiness.py` | W0–W3 |

### Proposed new gates (engineering — P1)

| Gate | Behavior |
|------|----------|
| **`make corpus-check`** (workspace wrapper) | Runs `corpus_refs` for wedge manifests; fails on unresolved slugs |
| **Extend `validate.py`** | Every block slug + discover query entity ref must appear in staging search roots |
| **Discover compose regression** (optional) | For each manifest `discover_queries[].key`, assert compose returns ≥N entity cards when `AI_MODE=replay` |
| **Post-seed audit** | `dogfood_audit.py` reports % blocks with resolvable venue briefs |

### Fix discover_queries fiction (P1 engineering)

Today `seed_discover_queries()` only logs. Options (pick one):

1. **Documentation-only** — rename to `discover_query_contracts` in schema; keep as spec (status quo, honest).
2. **Compose regression fixtures** — store expected board snapshots keyed by query key (offline test).
3. **Seed compose cache rows** (heavier) — only if product needs deterministic offline compose.

**Recommendation:** Option 2 for wedge queries (Lisbon Q1–Q3, Rome Q1–Q2); Option 1 elsewhere until needed.

---

## Events & Discover specifics

### Events

| Need | Source | Action |
|------|--------|--------|
| Dated one-offs in trip window | Promoted `experiences` rows with `starts_at` | Pick 2–3 per pack from batches or canonical JSON |
| Discover for-you event cards | `get_for_you` + experience rows | Ensure IDs in for-you match seeded slugs |
| Folio dated-events rail | `useTripExperiences(availability: one_off)` | Block or save links to same experience slugs |
| Live API events | `ingest_events.py` | **Out of scope** for dogfood v1 — curator tier only |

### Discover

| Need | Connection |
|------|------------|
| Board entity cards (MG-A3) | Manifest refs → promoted venues with briefs |
| Facet contract (search-board-contract.md) | Partial today — vibe/accessibility GAP on entities; enrich promoted JSON tags or accept contract-only filters for v1 |
| Editorial emphasis | Dossiers from pipeline B |
| Compose city scope | Backend uses trip destination; mock needs Phase 4 fix |

---

## Relationship to parallel streams

| Stream | Overlap | Coordination |
|--------|---------|--------------|
| **B — Backend wedge substrate** | Lisbon proposals, home feed, shellfish obs | Same manifest — merge PRs or sequence: corpus refs first, then proposals |
| **D — Frontend mock + mara.ts** | Slug namespace | Mock must use manifest slugs after Phase 1 audit published |
| **E — Place illustrations** | Visual tier only | Orthogonal — same cities, different asset type |
| **A — Workspace certify ladder** | Add `make corpus-check` | This plan proposes it |

**API contract:** Corpus connection should **not** require OpenAPI changes. Seeding rows + importing dossiers only. If a route/model change is needed, run `make sync-types` and coordinate with D.

---

## What not to do

| Don't | Why |
|-------|-----|
| Wire all 34 editorial cities | No scenarios; massive ops cost |
| Replace manifests with DB-only seeding | Lived substrate (constraints, group chat, private obs) belongs in manifests |
| Use `import_staged_refs` as the only import | Leaves Discover/Vesper thin — no dossiers/Qdrant |
| Generate LLM substrate at seed time | Violates dogfood authoring rule |
| Expand mock personas before backend promotion | 12 mocks enough; deepen S4 + elif |
| Live Ticketmaster ingest for dogfood v1 | Curator-tier experiences sufficient for wedge proof |
| Block wedge on Istanbul editorial | Istanbul B is P1; Lisbon W3 is P0 |

---

## Acceptance criteria (W3 + liveliness)

After Phase 1–2 on target environment (local dogfood DB + optional Fly):

### Corpus connection

- [ ] `corpus_refs` reports **0 unresolved slugs** for lisbon-phase1 and elif-rome manifests
- [ ] Every itinerary block with `venue_slug` / `experience_slug` resolves to a row with brief OR dossier
- [ ] Qdrant collections populated for wedge city venue slugs (spot-check retrieval)

### Surface liveliness (extends substrate richness checklist)

- [ ] Itinerary block tap → venue/experience detail with authored copy (not empty stub)
- [ ] Discover query `mara-arrival-dinner-search` → board with ≥3 named entities from corpus
- [ ] Same venue name appears on Plan block, Discover card, and Atlas save (cross-surface coherence)
- [ ] ≥2 dated events visible in trip window (Folio or Discover for-you)
- [ ] Vesper question about seeded place → grounded answer with provenance

### Pack readiness

- [ ] `app_qa_status: passed` for lisbon-phase1 and elif-rome in `packs.yaml`
- [ ] `trips_home` gap closed or explicitly deferred with rich hero wired

---

## Effort estimate

| Phase | Work | Effort |
|-------|------|--------|
| Phase 1 Lisbon corpus + manifest | Import ops + authoring + audit | 1–2 days |
| Phase 2 Rome | Mostly import (314 MD ready) + light manifest | 0.5–1 day |
| Tooling gates (`corpus-check`, validate extend) | Engineering | 2–4 hrs |
| Phase 3 Istanbul editorial (B) | New cartographer pass | 3–5 days (separate project) |
| Phase 4 mock parity | Frontend fixtures | 1 day (overlaps Stream D) |

---

## Key file index

| Topic | Path |
|-------|------|
| This plan | `docs/working/dogfood-corpus-connection-plan-2026-06-28.md` |
| Substrate richness backlog | `docs/working/dogfood-substrate-richness-and-generation-backlog-2026-06-28.md` |
| Lisbon search-board contract | `travel-agent/tools/dogfood/content/sources/lisbon-phase1/search-board-contract.md` |
| Lisbon product-moment-map | `travel-agent/tools/dogfood/content/sources/lisbon-phase1/product-moment-map.md` |
| Lisbon manifest | `travel-agent/tools/dogfood/content/manifests/lisbon-phase1.yaml` |
| Rome manifest | `travel-agent/tools/dogfood/content/manifests/elif-rome.yaml` |
| Corpus audit | `travel-agent/tools/dogfood/content/corpus_refs.py` |
| Thin import | `travel-agent/tools/dogfood/content/import_staged_refs.py` |
| Editorial import | `travel-agent/scripts/import_cursor_dossiers.py` |
| JSON seed pipeline | `travel-agent/tools/seed/README.md` |
| Discover compose (backend) | `travel-agent/backend/discover/compose_board.py` |
| Discover compose (mock) | `travel-app/utils/api/mock/discoverCompose.ts` |
| Place angles (mock) | `travel-app/constants/mocks/angles.ts` |
| Data pipeline runbook | `travel-agent/docs/operations/Data Pipeline Runbook.md` |
| Events architecture | `travel-agent/docs/architecture/Events Strategy and Architecture.md` |

---

## Bottom line

**Dogfood feels real when itinerary → venue → dossier → discover query share one slug graph.**

You already built the graph for Lisbon and Rome. This plan connects it to manifests through full A+B import, manifest ref expansion, dated events, validation gates, and mock slug parity — scoped to the wedge first, without boiling the ocean across 34 editorial cities.

**Next human action:** Run Phase 1A corpus audit on Lisbon, then execute import + manifest expansion against `search-board-contract.md` before the next W3 walk.
