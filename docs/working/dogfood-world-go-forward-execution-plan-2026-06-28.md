# Dogfood & World System — Go-Forward Execution Plan

> Status: execution plan (sequenced, not yet run)
> Owner: founder / engineering
> Created: 2026-06-28
> Companion to: `dogfood-world-system-target-state-2026-06-28.md` (north-star)
> Scope: the ordered run that takes us from "structurally connected" to "one rich, clean, QA'd world"

**Question this doc answers:** Given everything verified in the 2026-06-28 substrate investigation, what is the *optimal order of operations* to reach one clean system — and does that order actually solve every stated problem?

---

## The reframing that drives this plan

The substrate investigation (2026-06-28) verified a result that **changes the priority order** vs the original corpus-connection plan:

**Structural connection is already done. Enrichment is the real remaining gap.**

Evidence (local Postgres, after `APPLY=1 make dogfood-city` for all 5 packs):

| Check | Result |
|-------|--------|
| Manifest slugs resolve in DB (`corpus_refs`) | ✅ 59/59, 0 missing |
| Itinerary block → `venue_id` / `experience_id` FK | ✅ verified on elif Rome (8 blocks, all entity blocks resolve) |
| Canonical entity metadata (name, type, coords, tags) | ✅ present |
| **Editorial briefs in DB** | ❌ Rome **0** / Lisbon 110 |
| **Editorial dossiers in DB** | ❌ Rome **0** / Lisbon **0** |
| **Editorial MD on disk, unimported** | ⚠️ Rome 322 / Lisbon 312 |
| **Qdrant embeddings (`ENRICH=1`)** | ❌ never run |

**Implication:** "Stream F / corpus connection" must be **re-scoped**. The gap is *not* "make slugs resolve" (solved by `import_staged_refs`). The gap is "run editorial import + embeddings so Discover/Vesper are actually rich." Elif's restaurants are real seeded canonical entities — but they're structural stubs (no briefs, no dossiers, no vectors) until enrichment runs.

This re-scoping is the spine of the sequence below.

---

## Identity of the seeded entities (so "legit restaurant" is unambiguous)

A clarifying note that governs how we talk about dogfood content, to prevent future confusion:

| Slug | DB name | What it actually is |
|------|---------|---------------------|
| `rome-market-testaccio` | Testaccio Market | Real place archetype (Mercato Testaccio) |
| `rome-venue-roscioli-style-reservation` | Roscioli-Style Deliberate Reservation | **Composite, inspired-by** Roscioli — deliberately not a booking-claim entity |
| `rome-venue-suppli-counter` | Suppli Standing Counter | Generic Roman street-food archetype |
| `rome-venue-da-enzo-warm-room` | Da Enzo-Style Warm Trattoria | Composite, inspired-by Da Enzo |

These are **dogfood-safe stand-ins**: real enough for planning UX, deliberately *not* claims of a specific bookable business. The `-style` suffix is the governance signal. This is correct for fixtures and should be preserved, not "fixed."

---

## The phased run (0 → 4, plus 2b and 2c)

Ordered by dependency and by the discipline rule: **Lisbon wedge to W3 before broadening.**

### Phase 0 — Lock in what's built (workspace-only, zero coordination)

1. Commit uncommitted workspace work:
   - `scripts/corpus-check.sh`
   - `scripts/dogfood-city.sh`
   - `Makefile` (`make corpus-check`, `make dogfood-city`, `certify-fast` → runs `corpus-check` first)
2. **Governance enforcement (close goal 4's hole):** extend `corpus-check` so governance is *self-enforcing*, not just documented. It should fail when:
   - a manifest embeds venue/place metadata inline instead of referencing a corpus slug (no manifest-duplicated entity copies), and
   - a corpus entity is missing its tier tag (`proof_only` vs `launch_candidate`) or a fixture-only entity lacks its dogfood-safe signal (e.g. the `-style` suffix convention).

   *Rationale:* without a check, the parallel systems killed in Phase 3 grow back. A doc cannot stop the next contributor; a failing gate can.

*Why first:* no dependencies, makes `corpus-check` a live gate immediately, and everything downstream references these scripts.

### Phase 1 — Prove enrichment end-to-end on **Lisbon only**

2. Run `APPLY=1 ENRICH=1 make dogfood-city CITY=lisbon` locally — import 312 Lisbon dossiers + embeddings to Qdrant.
3. Resolve the prerequisites this surfaces (the real unknowns):
   - Nominatim / network access for dossier import
   - API keys for the embed step
4. Patch `dogfood-city.sh` for any `ENRICH=1` friction (this path has never been exercised).
5. **GO/NO-GO GATE — "does it feel real?" (the one unproven goal):**
   Spot-check the payoff and make this an explicit decision, not a checkbox:
   - **GO** if Vesper cites real Lisbon dossiers *and* Discover composes from real venues (not stubs/fallbacks). → proceed to Phase 2.
   - **NO-GO** if enriched Lisbon still feels thin. → **stop broadening.** The problem is not import; it is retrieval/composition quality. Branch to a *new* investigation (embedding quality, retrieval ranking, board composition) before spending enrichment cost on Rome or any other city.

   *Rationale:* "feels real" is the only one of the five goals that is still a hypothesis. Proving or disproving it cheaply on one city — before paying the five-city cost — is the highest-leverage decision in the whole run.

*Why Lisbon-only:* already has 110 briefs → closest to rich → lowest-effort proof the enrichment path works before paying the cost on five cities. Honors the wedge rule.

### Phase 2 — Generalize, then **Rome**

6. Run `APPLY=1 ENRICH=1 make dogfood-city CITY=rome` — fills Rome's 0-brief / 0-dossier gap from the 322 MD files.
7. Add an **enrichment-depth check** (briefs/dossiers per city) so "connected" now asserts *rich*, not just *resolves*.

*Why second:* Rome is the second canonical wedge (elif/Sarah/Mike) and the subject of the substrate question that started this — closing it makes the flagship-persona dogfood story whole.

### Phase 2b — Remaining dogfood cities (after go/no-go + Rome)

**Gate:** Do not start until Phase 1 go/no-go is **GO** and Phase 2 (Rome import) is complete. Doc 4 wedge discipline also applies: **do not start Istanbul cartographer until Lisbon W3 passes.**

The five active dogfood manifests do **not** share the same enrichment path. See [Cartographer gap registry](#cartographer-gap-registry) below.

| City | Manifest | Path | Phase 2b step |
|------|----------|------|---------------|
| **Istanbul** | `istanbul-phase1` | **New cartographer pass** (no MD on disk) | 8 — authoring project |
| **Tokyo** | `tokyo-phase1` | Optional thin editorial OR JSON-only | 9 — light pass |
| **Brooklyn** | `brooklyn-phase1` | JSON promote + embed (not cartographer MD) | 10 — verify promote |

8. **Istanbul cartographer pass (P1):** Run pipeline B from scratch — cartographer → scout → angles → write → `import_cursor_dossiers.py --city istanbul`. Richest elif narrative surface (14 entity saves, 6 experiences, pending Atlas artifact) with **zero editorial depth** today. Expect 3–5 days of authoring work before import is possible. Structural connection (19/19 slugs) is already done via `istanbul-elif-canonical-001.json`.

9. **Tokyo thin editorial (P2):** Memory-beat pack by design — generic venue anchors may be acceptable. Minimum: ensure Pipeline A briefs are promoted + embedded for manifest slugs (12 refs). Full cartographer pass is **optional**, not required for W2.

10. **Brooklyn promote + embed (P2):** Has JSON briefs in `tools/seed/staging/brooklyn-briefs-*.json` (99% brief coverage per seed README) but **no** `content/staging/brooklyn/`. Run promote + embed for manifest venues (`bakeri-williamsburg`, `hotel-delmano`, `paulie-gees-greenpoint`); verify briefs land in DB. Full cartographer dossiers only if home-city Discover/Vesper still feels thin after JSON briefs.

*Why after Rome:* Istanbul/Tokyo/Brooklyn are W2 dogfood packs, not wedge cities. Istanbul is the highest-risk "feels fake" surface after Rome because it has the richest manifest narrative with no editorial layer — but proving the import path on Lisbon/Rome first avoids authoring 300 MD files into a broken retrieval stack.

### Phase 2c — Latent corpus rollout (persona-accessible cities beyond manifests)

**Gate:** Do not start until Phase 1 go/no-go is **GO** and Phase 2 (Rome import) is complete. Same retrieval stack that makes Lisbon feel real must be proven before importing ~5,200 additional MD files.

**Goal:** Dogfood personas can create ad-hoc trips to European cities beyond the five manifest packs — trip destination resolves, search/Discover/Vesper return real corpus — without expanding the certify ladder or dogfood manifest QA surface to 39 cities.

**Key distinction:**

| Concept | Meaning |
|---------|---------|
| **Catalog availability** | City in Postgres + Qdrant; trip-create, search, Vesper work on real backend |
| **Dogfood-ready** | Manifest, fixtures, certify ladder, mock parity — still only the 5 packs |

Latent cities get **`corpus_tier: proof_only`**. Lisbon/Rome (and eventually Istanbul post-cartographer) stay **`launch_candidate`**. Dogfood manifests must only reference `launch_candidate` slugs unless explicitly tagged `proof_only` (enforced by `corpus-check` in Phase 0).

**Scale (verified 2026-06-28):** 34 cities in `content/staging/`, **~5,869 MD files** total. Lisbon + Rome = ~634; remaining **32 cities ≈ 5,235 files**. All are **import gap only** (cartographer already ran) — no new authoring.

#### Tier A — Persona-adjacent (import first, ~5 cities)

Cities personas and mocks already *imply* but that have **zero Postgres presence** today:

| City | MD on disk | Why Tier A |
|------|------------|------------|
| `paris` | 254 | Mock autocomplete + cross-city memory framing |
| `barcelona` | 271 | M0 default fixture memories |
| `venice` | 310 | Common ad-hoc elif exploration city |
| `amalfi-coast` | 217 | M0 default fixture memories |
| `nice` | 119 | Compact Riviera second-visit candidate |

11. **Tier A import + embed:** For each Tier A city:
    ```bash
    cd travel-agent
    PYTHONPATH=. python scripts/import_cursor_dossiers.py --city {city} --dry-run
    PYTHONPATH=. python scripts/import_cursor_dossiers.py --city {city}
    # then shared embed pass (idempotent)
    PYTHONPATH=. python scripts/embed_eval_briefs.py
    PYTHONPATH=. python scripts/embed_experience_briefs.py
    PYTHONPATH=. python scripts/embed_place_angles_staging.py
    ```
    Tag imported entities `corpus_tier: proof_only` (via import metadata or post-import audit).

12. **Tier A frontend parity (travel-app):** Add Tier A slugs to `MOCK_DESTINATIONS` in `data/search.ts` so mock-mode dogfood can pick Paris/Venice/etc. Place illustrations (Stream E) for Tier A cities if visual QA needs them.

13. **Tier A spot-check (sample, not full certify):** One ad-hoc trip per Tier A city on real backend — destination resolves (`place_id` non-null), search returns ≥3 venues, Vesper cites a dossier. Failures block Tier B, not the five-pack ladder.

#### Tier B — Full latent European corpus (batch, proof_only)

Remaining **27 cities** in `content/staging/` excluding Lisbon, Rome, and Tier A:

`athens`, `bilbao`, `bologna`, `bordeaux`, `cagliari`, `catania`, `dubrovnik`, `florence`, `genoa`, `granada`, `ibiza`, `lecce`, `lyon`, `madrid`, `malaga`, `mallorca`, `marseille`, `milan`, `naples`, `palermo`, `porto`, `san-sebastian`, `seville`, `split`, `thessaloniki`, `valencia`, `valletta`

(Tier C cities in this list are skipped by the batch script unless explicitly opted in.)

14. **Batch import script:** Add `scripts/import_latent_corpus.sh` (or extend `dogfood-city.sh`) — iterates Tier B cities, dry-run summary first, `--apply` writes, logs per-city entity counts. All imports tagged `proof_only`.

15. **Batch embed:** Single idempotent embed pass after all imports (not per-city — embed scripts are global).

16. **Fly promotion:** Catalog import to Fly is correct per governance model (quality-gated, not fixture seed). Promote Tier A + B corpus after local spot-check; fixtures (`seed.py --allow-prod`) remain scoped to the five packs.

*Do not add Tier B cities to certify ladder or dogfood manifests until a scenario is authored.*

#### Tier C — Defer (below minimum richness or no persona hook)

| City | MD count | Policy |
|------|----------|--------|
| `genoa` | 9 | Defer until cartographer backfill |
| `catania` | 32 | Defer |
| `malaga` | 35 | Defer |
| `cagliari` | 36 | Defer |
| `granada` | 45 | Defer |

Import only when a scenario manifest references them or cartographer expands the slice.

#### What Phase 2c unlocks for dogfood personas

| Capability | Before 2c | After Tier A | After Tier B |
|------------|-----------|--------------|--------------|
| Create trip to Venice (real backend) | ❌ no `place_id` | ✅ | ✅ |
| Search / Discover in Venice | ❌ | ✅ (if embedded) | ✅ |
| Vesper cites Venice dossiers | ❌ | ✅ (if go/no-go passed) | ✅ |
| Mock mode Venice trip | ❌ not in autocomplete | ✅ after step 12 | ✅ for Tier A only |
| Certify ladder coverage | 5 packs | 5 packs (unchanged) | 5 packs (unchanged) |
| Dogfood manifest QA | 5 packs | 5 packs (unchanged) | 5 packs (unchanged) |

*Why after 2b:* Manifest cities (Istanbul cartographer, Tokyo, Brooklyn) are higher priority for the elif/Mara dogfood story. Tier A closes the gap between "persona remembers Barcelona" and "backend has no Barcelona." Tier B makes the full authored corpus reachable without pretending each city is dogfood-certified.

### Phase 3 — Kill parallel systems (coordination-gated)

Decommission tracker, sequenced by repo owner to avoid colliding with active branches:

17. **Workspace-safe now:** collapse Golden Paths into journeys; make `scenarios.yaml` the sole source (drop/generate `Dogfood Scenario Matrix.md`).
18. **travel-agent — coordinate with `stream-b`:** delete `seed_group_trip.py`; fix `discover_queries` log-only fiction (compose regression or rename to contracts); make full import the default for launch-candidate cities.
19. **travel-app — after Stream E lands:** mock slug parity (city-scope compose, mirror manifest slugs).
20. **Image tier (Stream E / Doc 3):** decide provision-CDN vs bundle-only and document.

*Why later:* cleanup, not capability; also most likely to conflict with `stream-b/lisbon-proposal-substrate` and `stream-e-place-illustration-media`.

### Phase 4 — Wire the connected world into QA (the payoff)

21. Add connected-world assertions to the certify ladder:
    - **fast:** `corpus-check` (slugs resolve)
    - **logic:** discover compose regression on manifest queries (`AI_MODE=replay`)
    - **visual:** Maestro against seeded corpus (real venue cards)
    - **live:** Vesper retrieval spot-check (cites real dossiers)
22. Single Fly promotion path: `dogfood-city ... --allow-prod` for the EAS dogfood build; latent corpus promote separately (catalog-only, no fixture seed).

---

## Cartographer gap registry

Two enrichment gaps that are easy to conflate — each city falls into exactly one bucket:

| Gap type | Meaning | Fix |
|----------|---------|-----|
| **Import gap** | Cartographer already ran; MD files exist in `content/staging/{city}/` | `ENRICH=1` / `import_cursor_dossiers.py --city {city}` |
| **Authoring gap** | Cartographer **never ran**; no `content/staging/{city}/` directory | New cartographer pass (cartographer → scout → angles → write), then import |

**Cartographer** = stage 1 of pipeline B (`scripts/import_cursor_dossiers.py` header): cartographer → scout → angles → write → import. Not a separate tool.

### Dogfood manifest cities (active packs)

Verified 2026-06-28 against `content/staging/`, local Postgres, and `corpus_refs` audits.

| City | Manifest | Slugs resolve | `content/staging/` MD | Pipeline A (JSON) | Briefs in DB | Dossiers in DB | Gap type | Priority |
|------|----------|---------------|----------------------|-------------------|--------------|----------------|----------|----------|
| **Lisbon** | `lisbon-phase1` | ✅ 10/10 | ✅ **312** | ✅ promoted (~104 venues) | 110 | 0 | **Import** | P0 — Phase 1 |
| **Rome** | `elif-rome` | ✅ 11/11 | ✅ **322** | ✅ canonical bundle | 0 | 0 | **Import** | P0 — Phase 2 |
| **Istanbul** | `istanbul-phase1` | ✅ 19/19 | ❌ **none** | ✅ `istanbul-elif-canonical-001.json` | 0 | 0 | **Authoring** | P1 — Phase 2b |
| **Tokyo** | `tokyo-phase1` | ✅ 12/12 | ❌ **none** | ✅ `tokyo-dogfood-corpus-001.json` | 0 | 0 | **Authoring** (optional thin) | P2 — Phase 2b |
| **Brooklyn** | `brooklyn-phase1` | ✅ 7/7 | ❌ **none** | ✅ JSON briefs in `tools/seed/staging/` | 0* | 0 | **Promote+embed** (not cartographer MD) | P2 — Phase 2b |

\* Brooklyn manifest venues show 0 briefs locally; seed README claims 99% brief coverage on promoted Brooklyn corpus — likely promote/embed not run for manifest slice. Verify before assuming authoring gap.

**Istanbul detail (highest authoring risk):** 3 venues, 6 experiences, 3 sites, 5 neighborhoods in DB — all structural stubs from canonical JSON. Richest dogfood narrative surface (14 entity saves, pending Atlas artifact with 29 photos) with nothing for Vesper/Discover to retrieve. `ENRICH=1` cannot help until cartographer writes MD files.

**Tokyo detail:** Memory-beat pack — generic venue anchors acceptable by design. Full 300-dossier cartographer pass is optional.

**Brooklyn detail:** Home-city control sample (W1 by design). Editorial depth comes from JSON promote pipeline (`brooklyn-briefs-williamsburg-mopup-001.json`, etc.), not cartographer MD. Different fix path than Istanbul.

### Latent corpus cities (32 beyond Lisbon/Rome — Phase 2c)

**32 cities** have cartographer output in `content/staging/` but **zero Postgres presence** today (~5,235 MD files). All are **import gap only**.

| Tier | Cities | MD range | Action | QA |
|------|--------|----------|--------|-----|
| **A** | paris, barcelona, venice, amalfi-coast, nice | 119–310 | Import + embed first; mock autocomplete | Sample spot-check (1 trip/city) |
| **B** | athens, bilbao, bologna, bordeaux, dubrovnik, florence, ibiza, lecce, lyon, madrid, mallorca, marseille, milan, naples, palermo, porto, san-sebastian, seville, split, thessaloniki, valencia, valletta, … | 45–305 | Batch import + embed; `proof_only` | None until scenario authored |
| **C** | genoa, catania, malaga, cagliari, granada | 9–45 | Defer | — |

**Ad-hoc trip policy:** Dogfood personas (`@dogfood.local`) are not API-blocked from creating trips to any destination. Before Phase 2c, latent cities fail at `place_id` resolution and return empty search. After Phase 2c Tier A, personas can explore Paris/Venice/etc. on real backend. Catalog availability ≠ dogfood manifest coverage — certify ladder stays on the five packs.

See [Phase 2c](#phase-2c--latent-corpus-rollout-persona-accessible-cities-beyond-manifests) for execution steps.

### How to check a city's gap type

```bash
cd travel-agent

# 1. Does editorial staging exist?
ls content/staging/{city}/ 2>/dev/null | wc -l   # >0 → import gap; 0 → authoring gap

# 2. Do manifest slugs resolve?
PYTHONPATH=. python -m tools.dogfood.content.corpus_refs \
    tools/dogfood/content/manifests/{pack}.yaml

# 3. Enrichment depth (after import)
# briefs + dossiers per city slug prefix in Postgres
```

---

## Dependency graph (critical path)

```text
Phase 0 (commit scripts) ──► everything
        │
        ▼
Phase 1 (Lisbon ENRICH, prove path) ──► Phase 2 (Rome ENRICH)
        │                                      │
        │         GO/NO-GO gate                │
        └──────────────┬───────────────────────┘
                       ▼
            Phase 2b (Istanbul cartographer → Tokyo thin → Brooklyn promote)
                       │
                       ▼
            Phase 2c (Tier A latent → Tier B batch, proof_only)
                       │
                       ▼
            Phase 4 (QA wiring) — five packs only; Tier A sample spot-check

Phase 3 (decommissions) runs in parallel, gated by child-repo streams
```

---

## Open decisions (founder forks — not auto-resolved)

1. **First enrichment scope:** Lisbon-only wedge proof first (recommended, honors discipline) vs Lisbon + Rome together (both flagship personas)?
2. **Embeddings cost/keys:** run embed locally with your keys now, vs briefs/dossiers-only first (offline, free, Discover/Vesper stay semi-thin)?
3. **Istanbul cartographer scope:** full ~250–300 dossier pass (matches Lisbon/Rome depth) vs targeted pass covering only the 19 manifest slugs (faster, may feel thin on open Discover queries)?
4. **Tokyo editorial depth:** JSON briefs only (memory-beat acceptable) vs thin cartographer pass (~30–50 dossiers for key manifest anchors)?
5. **Tier B timing:** Run immediately after Tier A spot-check passes, vs defer until a persona explicitly needs a Tier B city in dogfood?
6. **Tier C threshold:** Import cities with <50 MD files anyway (completeness) vs strict defer (quality signal)?

---

## Corpus tier model (governance)

| Tier | Cities | Import | Certify ladder | Manifest refs |
|------|--------|--------|----------------|---------------|
| `launch_candidate` | Lisbon, Rome (+ Istanbul post-cartographer) | Full ENRICH + W3 spot-check | ✅ exercised | Required for dogfood packs |
| `proof_only` | Tier A + B latent corpus | Import + embed | ❌ sample spot-check only | Allowed if explicitly tagged |
| `fixture_only` | `-style` composite entities in manifests | `import_staged_refs` | Via manifest QA | Dogfood fixtures only |

`corpus-check` (Phase 0) must enforce: dogfood manifest slugs reference `launch_candidate` or explicitly tagged `proof_only` entities — never untagged stubs or inline manifest copies.

---

## Definition of done (this run)

- [ ] Phase 0 committed; `make corpus-check` is a live gate
- [ ] `corpus-check` enforces governance (no manifest-embedded entities; corpus tier tag required)
- [ ] `APPLY=1 ENRICH=1 make dogfood-city CITY=lisbon` produces real dossiers + embeddings
- [ ] **Phase 1 GO/NO-GO passed:** Vesper/Discover spot-check on Lisbon cites real corpus, not stubs
- [ ] Rome enrichment fills 0-brief/0-dossier gap
- [ ] Enrichment-depth check exists (asserts rich, not just resolves)
- [ ] **Phase 2b — Istanbul:** cartographer pass complete; `content/staging/istanbul/` exists; import + embed run
- [ ] **Phase 2b — Tokyo:** manifest slugs have briefs (JSON promote minimum; cartographer optional)
- [ ] **Phase 2b — Brooklyn:** manifest venues have briefs in DB (promote + embed verified)
- [ ] **Phase 2c — Tier A:** paris, barcelona, venice, amalfi-coast, nice imported + embedded; `proof_only` tagged
- [ ] **Phase 2c — Tier A:** mock autocomplete includes Tier A slugs; ad-hoc trip spot-check passes (1/city)
- [ ] **Phase 2c — Tier B:** batch import script run; ~27 cities in Postgres + Qdrant as `proof_only`
- [ ] **Phase 2c — Tier C:** genoa/catania/malaga/cagliari/granada explicitly deferred or backfilled
- [ ] Decommission tracker: all 8 items closed
- [ ] Certify ladder tiers exercise the connected world
- [ ] Catalog/fixture governance adopted (tier tag + guardrails)
- [ ] Target-state doc scorecard reconciled with the enrichment finding
