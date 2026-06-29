# Dogfood & World System — Go-Forward Execution Plan

> Status: **in progress** (Phases 0–2 partially executed; environment consolidation added 2026-06-28)
> Owner: founder / engineering
> Created: 2026-06-28
> Last updated: 2026-06-29
> Companion to: `dogfood-world-system-target-state-2026-06-28.md` (north-star)
> Scope: the ordered run that takes us from "structurally connected" to **two deliberate dogfood worlds** (local workbench + Fly/EAS) with one promotion path, rich corpus, and holistic QA

**Question this doc answers:** Given everything verified in the 2026-06-28 substrate investigation — including the cloud/local split-brain — what is the *optimal order of operations* to reach one clean system you can dogfood on **both** local and Fly/EAS?

---

## The reframing that drives this plan

The substrate investigation (2026-06-28) verified a result that **changes the priority order** vs the original corpus-connection plan:

**Structural connection is already done. Enrichment + environment pairing are the real remaining gaps.**

Evidence (local Postgres, after `APPLY=1 make dogfood-city` for all 5 packs):

| Check | Result (2026-06-28) |
|-------|---------------------|
| Manifest slugs resolve in DB (`corpus_refs`) | ✅ 59/59, 0 missing |
| Itinerary block → `venue_id` / `experience_id` FK | ✅ verified on elif Rome (8 blocks, all entity blocks resolve) |
| Canonical entity metadata (name, type, coords, tags) | ✅ present |
| **Lisbon editorial import + briefs** | ✅ Phase 1 run: 312 files, ~249 briefs in DB |
| **Rome editorial import + briefs** | 🟡 Phase 2 run: ~207 briefs in DB — **but manifest canonical slugs still have 0 briefs** (slug namespace split) |
| **Qdrant embeddings** | ⚠️ ran to **cloud Qdrant** from **local Postgres** — split-brain; local Docker Qdrant empty |
| **Fly Postgres corpus + fixtures** | ❌ not promoted; `seed-s4-fly` is Lisbon S4 cohort only |

**Implication:** "Stream F / corpus connection" is **re-scoped**. The gap is not "make slugs resolve" (solved by `import_staged_refs`). The gaps are:

1. **Enrichment** — editorial import + embeddings so Discover/Vesper are rich (partially done for Lisbon/Rome editorial namespace).
2. **Environment pairing** — each dogfood world is an atomic **Postgres + Qdrant** pair; never mix local PG with cloud vectors (or vice versa).
3. **Promotion** — explicit one-way path from local workbench → Fly certified world for EAS + AI QA.
4. **Rome slug bridge** — manifest canonical slugs vs editorial slugs are two namespaces in the same DB.

---

## Dual environment model (new spine — Phase 0.5)

We dogfood in **two deliberate worlds**, not one accidentally split stack.

| | **Local (workbench)** | **Fly + EAS (certified)** |
|---|----------------------|---------------------------|
| **Primary use** | Fast iteration — corpus, manifests, slug fixes, desk dev | Phone dogfood (EAS builds) + AI-enabled QA (`certify-live`, eval agents) |
| **Postgres** | Docker `postgresql://vesper:localdev@localhost:5432/vesper` | Fly/Neon via `PROD_DATABASE_URL` in `.env.prod` |
| **Qdrant** | Docker `http://localhost:6333` | Qdrant Cloud (`QDRANT_URL` in Fly secrets / `.env`) |
| **Personas** | `@dogfood.local` seeded by `dogfood-city` (default) | Same emails; seeded only via **explicit Fly promotion** |
| **Can be ahead of Fly?** | ✅ yes — that's the point | ❌ should never be ahead without knowing |

### The invariant (non-negotiable)

```text
One environment = one Postgres + one Qdrant, embedded FROM that same Postgres.

Local:  local PG  → import + embed → local Qdrant
Fly:    Fly PG    → import + embed → cloud Qdrant

NEVER: local PG → embed → cloud Qdrant   ← current split-brain (venue_id mismatch on Fly)
NEVER: Fly PG  → embed → local Qdrant
```

Qdrant payloads carry **`venue_id` integers from the Postgres used at embed time**. Fly API + Fly Postgres + cloud Qdrant that was embedded from local Postgres = broken retrieval.

### Environment profiles

| Profile | `DATABASE_URL` | `QDRANT_URL` | When to use |
|---------|----------------|--------------|-------------|
| **`local`** (default) | local Docker Postgres | local Docker Qdrant | Desk dev, `make dev-backend`, fast corpus iteration |
| **`fly`** | `PROD_DATABASE_URL` | cloud Qdrant | EAS dogfood, AI QA, `certify-live` against real stack |

**Engineering (Phase 0.5):**

- Extend `dogfood-city.sh` with `PROFILE=local|fly` (default `local`).
- `PROFILE=local` → set both URLs to Docker defaults; fail if `.env` overrides Qdrant to cloud without `ALLOW_MIXED=1`.
- `PROFILE=fly` → load `.env.prod`, require `--allow-prod` on seed/bootstrap, print target DSNs before writes.
- Add `make dogfood-promote CITY=<city>` → `PROFILE=fly APPLY=1 ENRICH=1 make dogfood-city CITY=...` (wrapper).
- Document profiles in `travel-agent/.env.example` and README.

### Content flow (promotion, not continuous sync)

```text
content/staging/*.md
        │
        ▼
  ┌─────────────────┐
  │ PROFILE=local   │  workbench: iterate, spot-check, go/no-go
  │ import + enrich │
  └────────┬────────┘
           │ validate locally (corpus-check, Vesper/Discover spot-check)
           ▼
  ┌─────────────────┐
  │ PROFILE=fly     │  promote: same city pack to Fly PG + cloud Qdrant
  │ dogfood-promote │
  └────────┬────────┘
           │ certify on Fly (AI QA + EAS)
           ▼
     phone + eval agents hit certified world
```

Local can be ahead of Fly. Fly is **what we trust** for phone + QA. Promotion is intentional, not accidental via `.env` defaults.

### Remediation (do before Phase 2c bulk import)

**Split-brain fix (executed once after Phase 0.5 lands):**

1. Re-run Lisbon + Rome embed with `PROFILE=local` so local Docker Qdrant is populated from local Postgres.
2. Do **not** treat existing cloud Qdrant vectors (embedded from local PG) as Fly-safe until `dogfood-promote` re-embeds from Fly Postgres.
3. Optional: add `scripts/dogfood-env-check.sh` — prints PG host + Qdrant host + warns on mismatch.

---

## Identity of the seeded entities (so "legit restaurant" is unambiguous)

A clarifying note that governs how we talk about dogfood content:

| Slug | DB name | What it actually is |
|------|---------|---------------------|
| `rome-market-testaccio` | Testaccio Market | Real place archetype (Mercato Testaccio) |
| `rome-venue-roscioli-style-reservation` | Roscioli-Style Deliberate Reservation | **Composite, inspired-by** Roscioli — deliberately not a booking-claim entity |
| `rome-venue-suppli-counter` | Suppli Standing Counter | Generic Roman street-food archetype |
| `rome-venue-da-enzo-warm-room` | Da Enzo-Style Warm Trattoria | Composite, inspired-by Da Enzo |

These are **dogfood-safe stand-ins**: real enough for planning UX, deliberately *not* claims of a specific bookable business. The `-style` suffix is the governance signal. Preserve, not "fix."

**Separate from cloud/local:** Rome also has an **editorial slug namespace** (`toastaccio`, `trippa`, `piazza-testaccio`, …) that does not match manifest canonical slugs. Itinerary FKs resolve to canonical stubs; Vesper retrieves editorial venues by editorial slug — not via manifest IDs. See Phase 2a below.

---

## Execution status snapshot

| Phase | Status | Notes |
|-------|--------|-------|
| **0** | ✅ Done | `corpus-check`, `dogfood-city`, Makefile wired; governance in travel-agent |
| **0.5** | ✅ Done | Profiles, promote, fly-smoke, local Qdrant remediation |
| **1** | ✅ Done | Lisbon ENRICH on local PG; go/no-go **GO** |
| **2** | ✅ Done | Rome editorial enriched |
| **2a** | ✅ Done | Rome slug bridge — 9/9 canonical briefs (local + Fly) |
| **2b** | ✅ Done | Five packs promoted Fly; agent certification complete |
| **2c** | ✅ Done | Tier A + B latent corpus local + Fly spot-check |
| **3** | ✅ Done | Decommission tracker (seed paths, discover regression, mock parity) |
| **4** | 🟡 Partial | Certify ladder wired; five-pack agent gates green; per-journey live pending |

---

## The phased run (0 → 4, plus 0.5, 2a, 2b, 2c)

Ordered by dependency. Discipline rule: **Lisbon wedge to W3 before broadening** — now extended with **local profile before Fly promote**.

### Phase 0 — Lock in what's built ✅

1. Commit workspace tooling:
   - `scripts/corpus-check.sh`
   - `scripts/dogfood-city.sh`
   - `Makefile` (`make corpus-check`, `make dogfood-city`, `certify-fast` → runs `corpus-check` first)
2. **Governance enforcement:** `corpus-check` fails on manifest-embedded entities and missing `corpus_tier` tags.

*Status: committed on workspace branch; travel-agent governance committed.*

### Phase 0.5 — Environment profiles (before bulk enrich or Fly dogfood)

3. **`PROFILE=local|fly` in `dogfood-city.sh`** — atomic PG+Qdrant binding; mismatch warning/error.
4. **`make dogfood-promote CITY=`** — Fly promotion wrapper (`PROFILE=fly APPLY=1 ENRICH=1`).
5. **`scripts/dogfood-env-check.sh`** — print active stack; wired into `certify-live` preflight.
6. **Split-brain remediation:**
   - Re-embed Lisbon + Rome with `PROFILE=local` → local Docker Qdrant.
   - Document that cloud Qdrant state from pre-0.5 local embeds is **not Fly-authoritative**.
7. **`.env.example` update** — document `local` vs `fly` profile env vars side by side.

*Gate: Phase 2c and any Fly EAS dogfood depend on this.*

### Phase 1 — Prove enrichment end-to-end on **Lisbon only** ✅

8. Run `APPLY=1 ENRICH=1 make dogfood-city CITY=lisbon` locally.
9. Resolve prerequisites (sentence-transformers, einops, network for embed).
10. **GO/NO-GO GATE — passed:** Vesper/Discover cite real Lisbon dossiers on **local stack**.

*Follow-up under 0.5: re-embed to local Qdrant (was cloud during first run).*

### Phase 2 — Rome enrichment + canonical bridge

11. Run `APPLY=1 ENRICH=1 make dogfood-city CITY=rome` — ✅ editorial import done (~322 files, ~207 briefs).
12. Add **enrichment-depth check** (briefs/dossiers per city; assert rich, not just resolves).

#### Phase 2a — Rome manifest ↔ editorial slug bridge (blocker before calling elif Rome "rich")

**Problem:** Manifest canonical slugs (`rome-market-testaccio`, `rome-venue-roscioli-style-reservation`, …) exist as stub rows from `import_staged_refs` with **0 briefs**. Editorial MD uses different slugs (`toastaccio`, `trippa`, …) with full briefs. Itinerary FKs resolve to canonical stubs; Vesper cannot retrieve manifest-slug venues via editorial corpus.

**Pick one fix (founder decision — default recommendation: alias map):**

| Option | Approach | Pros | Cons |
|--------|----------|------|------|
| **A (recommended)** | Slug alias map: canonical → editorial; copy or join briefs at read time | Preserves `-style` governance on manifests | Requires alias table or seed-time mapping |
| **B** | Copy briefs onto canonical slug rows at import | Simple retrieval by manifest ID | Duplicates editorial content |
| **C** | Re-align manifest slugs to editorial slugs | One namespace | Breaks `-style` fixture semantics; manifest churn |

13. Implement chosen bridge; verify elif Rome blocks cite dossiers **by manifest slug path**.
14. Re-run enrichment-depth check for Rome canonical slugs specifically.

*Gate: Phase 2b and Fly promote for Rome blocked until 2a passes on local profile.*

#### Phase 2 — engineering debt surfaced by enrichment

15. **Dossier parser:** venue importer expects `## Dossier`; MD uses `## Dossier: {lens}` → most place dossiers skipped (~24 imported). Fix parser to accept lens suffix.
16. **Place angles embed:** filter by city or fix Brooklyn slug refs in global staging JSON (non-fatal skip today).

### Phase 2b — Remaining dogfood cities (after go/no-go + Rome 2a)

**Gate:** Phase 1 GO ✅, Phase 2a complete, Phase 0.5 complete.

| City | Manifest | Path | Step |
|------|----------|------|------|
| **Istanbul** | `istanbul-phase1` | New cartographer pass | 17 |
| **Tokyo** | `tokyo-phase1` | JSON-only or thin editorial | 18 |
| **Brooklyn** | `brooklyn-phase1` | JSON promote + embed | 19 |

17. **Istanbul cartographer (P1):** targeted manifest pass (19 entities) → `import_cursor_dossiers.py --city istanbul` + `import_experience_briefs --city istanbul`. Task files: `cartographer-istanbul-dogfood.md`, `batch-research-istanbul-dogfood.md`.
18. **Tokyo thin editorial (P2):** JSON promote minimum for manifest slugs; full cartographer optional.
19. **Brooklyn promote + embed (P2):** promote from `tools/seed/staging/brooklyn-briefs-*.json`.

Each city: **`PROFILE=local` first** → spot-check → **`make dogfood-promote CITY=`** when ready for EAS/QA.

### Phase 2c — Latent corpus rollout (persona-accessible cities beyond manifests)

**Gate:** Phase 0.5 ✅, Phase 2a ✅, Phase 1 go/no-go ✅. Same retrieval stack proven on local profile before importing ~5,200 additional MD files.

**Do not bulk-import until environment profiles are wired** — importing 34 cities into local Postgres while embeddings accidentally target shared cloud Qdrant deepens split-brain.

**Goal:** Dogfood personas can create ad-hoc trips to European cities beyond the five manifest packs — trip destination resolves, search/Discover/Vesper return real corpus — without expanding certify ladder to 39 cities.

| Concept | Meaning |
|---------|---------|
| **Catalog availability** | City in Postgres + Qdrant (matched profile); trip-create, search, Vesper work |
| **Dogfood-ready** | Manifest, fixtures, certify ladder — still only the 5 packs |

Latent cities get **`corpus_tier: proof_only`**. Tier A + B import runs on **`PROFILE=local`**; Fly promote is a **separate batch** after Tier A spot-check.

#### Tier A — Persona-adjacent (~5 cities)

`paris`, `barcelona`, `venice`, `amalfi-coast`, `nice`

20. Tier A import + embed (`PROFILE=local`).
21. Tier A frontend parity: `MOCK_DESTINATIONS` in travel-app.
22. Tier A spot-check: one ad-hoc trip per city on **local profile**; then optional Fly promote batch.

#### Tier B — Full latent European corpus (~27 cities)

23. Batch import script (`scripts/import_latent_corpus.sh` or extend `dogfood-city`) — `PROFILE=local`, all `proof_only`.
24. Single idempotent embed pass per profile (not per-city).
25. **Fly promotion:** catalog-only batch promote after local spot-check; fixtures remain scoped to five packs.

#### Tier C — Defer

`genoa`, `catania`, `malaga`, `cagliari`, `granada` — import only when scenario references them.

### Phase 3 — Kill parallel systems (coordination-gated)

26. Collapse Golden Paths into journeys; `scenarios.yaml` sole source.
27. **travel-agent:** delete `seed_group_trip.py`; fix `discover_queries` log-only fiction.
28. **travel-app:** mock slug parity after Stream E lands.
29. **Deprecate narrow `seed-s4-fly`** in favor of `dogfood-promote CITY=lisbon` (keep as alias during transition).
30. Image tier decision (Stream E).

### Phase 4 — Wire connected world into QA + Fly certification

**Fly is the certification target for EAS + AI QA.** Local is the workbench; certify ladder tiers assert against the **Fly profile** for live/AI tiers.

| Tier | Target stack | Connected-world assertion |
|------|--------------|---------------------------|
| **fast** | local or CI | `corpus-check` + `dogfood-env-check` (local profile) |
| **logic** | local Postgres | discover compose regression on manifest queries (`AI_MODE=replay`) |
| **visual** | local or device + local API | Maestro against seeded corpus (real venue cards) |
| **live** | **Fly API + Fly PG + cloud Qdrant** | Vesper retrieval spot-check; two-account walk on EAS build |

31. Add connected-world assertions to certify ladder (above).
32. **`certify-live` preflight:** verify Fly stack has promoted corpus for wedge cities (not just S4 Lisbon cohort).
33. **AI QA agents:** run against Fly profile by default; local profile for debugging only.
34. Document promotion cadence: local iterate → promote city pack → certify-live green → EAS build.

---

## Cartographer gap registry

Two enrichment gaps — each city falls into exactly one bucket:

| Gap type | Meaning | Fix |
|----------|---------|-----|
| **Import gap** | MD in `content/staging/{city}/` | `ENRICH=1` / `import_cursor_dossiers.py --city {city}` |
| **Authoring gap** | No `content/staging/{city}/` | Cartographer pass, then import |
| **Slug bridge gap** | Editorial slugs ≠ manifest canonical slugs | Phase 2a (Rome only today) |

### Dogfood manifest cities

| City | Manifest | Slugs resolve | MD on disk | Briefs in DB | Gap type | Status |
|------|----------|---------------|------------|--------------|----------|--------|
| **Lisbon** | `lisbon-phase1` | ✅ 10/10 | ✅ 312 | ✅ ~249 | Import | ✅ Phase 1 done; re-embed local Qdrant pending 0.5 |
| **Rome** | `elif-rome` | ✅ 11/11 | ✅ 322 | 🟡 ~207 editorial; **0 on canonical slugs** | Import + **slug bridge** | 🟡 Phase 2 partial |
| **Istanbul** | `istanbul-phase1` | ✅ 19/19 | ✅ 19 MD | ✅ briefs+dossiers | Authoring | ✅ local + Fly promote |
| **Tokyo** | `tokyo-phase1` | ✅ 12/12 | ❌ none | 7 venue + 1 exp briefs (JSON) | JSON promote | ✅ local + Fly promote |
| **Brooklyn** | `brooklyn-phase1` | ✅ 7/7 | ❌ none | 3 venue + 2 exp briefs (JSON) | Promote+embed | ✅ local + Fly promote |

### Latent corpus (Phase 2c)

32 cities, ~5,235 MD files — all **import gap only**. Blocked until Phase 0.5.

---

## Dependency graph (critical path)

```text
Phase 0 (scripts) ✅
        │
        ▼
Phase 0.5 (env profiles + split-brain fix) ──► Fly-safe promotion path
        │
        ├──────────────────────────────────────┐
        ▼                                      ▼
Phase 1 (Lisbon ENRICH) ✅              re-embed local Qdrant
        │
        ▼
Phase 2 (Rome ENRICH) 🟡
        │
        ▼
Phase 2a (Rome slug bridge) ──► elif Rome "rich" on manifest path
        │
        ▼
Phase 2b (Istanbul → Tokyo → Brooklyn)     each: local → promote → certify
        │
        ▼
Phase 2c (Tier A → Tier B latent)            PROFILE=local import; batch Fly promote
        │
        ▼
Phase 4 (QA on Fly profile) ◄── EAS + AI QA

Phase 3 (decommissions) — parallel, gated by child-repo streams
```

---

## Open decisions (founder forks)

| # | Decision | Recommendation | Status |
|---|----------|----------------|--------|
| 1 | Dual env vs single | **Dual:** local workbench + Fly certified | ✅ decided |
| 2 | Rome slug bridge option | **A:** alias map canonical → editorial | ✅ implemented |
| 3 | Istanbul cartographer scope | Full ~250–300 vs targeted 19-slug pass | ✅ **targeted 19-slug pass** (see `.cursor/tasks/cartographer-istanbul-dogfood.md`) |
| 4 | Tokyo editorial depth | JSON briefs only vs thin cartographer | ✅ **JSON briefs only** (6 venue + experience description in tokyo-dogfood-corpus-001.json) |
| 5 | Tier B timing | After Tier A spot-check + Fly promote | ✅ done 2026-06-29 |
| 6 | Embeddings on Fly promote | Always re-embed from Fly PG (never copy vectors) | ✅ decided |

---

## Corpus tier model (governance)

| Tier | Cities | Import | Certify ladder | Manifest refs |
|------|--------|--------|----------------|---------------|
| `launch_candidate` | Lisbon, Rome (+ Istanbul post-cartographer) | Full ENRICH + W3 spot-check | ✅ exercised | Required for dogfood packs |
| `proof_only` | Tier A + B latent corpus | Import + embed (`PROFILE=local` first) | ❌ sample spot-check only | Allowed if explicitly tagged |
| `fixture_only` | `-style` composite entities in manifests | `import_staged_refs` | Via manifest QA | Dogfood fixtures only |

`corpus-check` enforces: dogfood manifest slugs reference `launch_candidate` or explicitly tagged `proof_only` — never untagged stubs or inline manifest copies.

---

## Commands reference

```bash
# Local workbench (default)
APPLY=1 ENRICH=1 make dogfood-city CITY=lisbon
APPLY=1 ENRICH=1 PROFILE=local make dogfood-city CITY=rome   # after Phase 0.5

# Fly promotion (EAS + AI QA)
make dogfood-promote CITY=lisbon                                # after Phase 0.5
SEED_S4_FLY_APPLY=1 make seed-s4-fly                            # legacy; superseded by promote

# Gates
make corpus-check
make dogfood-env-check                                          # after Phase 0.5
make certify-fast    # local profile
make certify-live    # Fly profile — EAS + AI QA
```

---

## Definition of done (this run)

### Environment
- [ ] `PROFILE=local|fly` in `dogfood-city.sh`; mismatch guard active
- [ ] `make dogfood-promote CITY=` works end-to-end
- [ ] Local Docker Qdrant populated from local Postgres (Lisbon + Rome)
- [ ] Fly Postgres + cloud Qdrant populated via explicit promote (at least Lisbon + Rome)

### Corpus + enrichment
- [ ] Phase 0 committed; `make corpus-check` is a live gate with governance
- [ ] Phase 1 GO/NO-GO passed (Lisbon rich on local profile)
- [ ] Phase 2a Rome slug bridge complete — canonical manifest slugs have briefs/retrieval
- [ ] Enrichment-depth check exists
- [ ] Dossier parser accepts `## Dossier: {lens}`

### Remaining cities
- [ ] Phase 2b: Istanbul cartographer + import; Tokyo + Brooklyn briefs verified
- [ ] Phase 2c Tier A: paris, barcelona, venice, amalfi-coast, nice (`proof_only`, local then promote)
- [x] Phase 2c Tier B: batch import; Fly promote batch *(2026-06-29 — 27 cities, local + Fly spot-check green)*
- [ ] Tier C cities explicitly deferred

### QA + cleanup
- [ ] Decommission tracker: all 8 items closed
- [ ] Certify ladder: fast/logic on local; **live on Fly profile** with corpus assertions
- [ ] AI QA agents documented to target Fly profile
- [ ] Target-state doc scorecard reconciled
