# Dogfood & World System — Target State + Decommission Plan

> Status: north-star / canonical index
> Owner: founder / engineering
> Created: 2026-06-28
> Last updated: 2026-06-28 (dual-environment model added)
> Scope: the **one system** dogfood, world content, QA, and environments converge to
> Role: front door + decommission tracker for the four investigation/plan docs below

**Question this doc answers:** If we execute the current plans, do we end up with *one* clean system — smooth dogfood, a rich connected world, no confusion about where content lives, no parallel systems, all wired to holistic AI QA? This doc defines that end-state, tracks what's already built, and lists exactly what to kill.

---

## Companion docs (this is the index)

| # | Doc | Owns |
|---|-----|------|
| 1 | `dogfood-qa-substrate-system-investigation-2026-06-28.md` | QA streamlining, certify ladder, broken gates, duplication |
| 2 | `dogfood-substrate-richness-and-generation-backlog-2026-06-28.md` | Substrate richness, proposals, home cards, liveliness |
| 3 | `dogfood-place-illustration-coverage-gap-2026-06-28.md` | Place-illustration (image) coverage — Stream E |
| 4 | `dogfood-corpus-connection-plan-2026-06-28.md` | Connect world corpus (A+B) to manifests; catalog-vs-fixture governance |
| 5 | `dogfood-world-go-forward-execution-plan-2026-06-28.md` | Sequenced run (Phases 0–4); enrichment-is-the-gap reframing; go/no-go + governance gates; **cartographer gap registry** (import vs authoring per city) |
| — | **this doc** | The unified target state these five converge to |

---

## TL;DR

Executing the four plans gets the **content/world layer genuinely clean**. This doc closes the remaining **integration layer** so all three of your hardest goals are met:

- **No confusion where content goes** → one content-governance model (catalog → prod; fixtures → cohort-isolated).
- **No parallel systems** → an explicit decommission tracker (8 systems to kill).
- **Holistic AI QA** → the certify ladder runs against the *connected* world, not mock/thin backend.

**Pleasant surprise (verified 2026-06-28):** the 4-tier **certify ladder already exists** in the workspace `Makefile` (`certify-fast/logic/visual/live`), along with `dogfood-status`, `seed-s4-local`, `seed-s4-fly`. Much of the "system cleanup" is already built (some uncommitted). The remaining work is **wiring corpus in, killing parallels, and one orchestrator** — not building the ladder from scratch.

**Sharpened by the substrate investigation (verified 2026-06-28):** the corpus is already **structurally connected** — all 59 manifest slugs resolve in Postgres (0 missing) and itinerary blocks resolve via `venue_id`/`experience_id` FK (verified on elif Rome). The real remaining gap is **enrichment, not connection**: Rome has 0 briefs / 0 dossiers, Lisbon has 110 briefs / 0 dossiers, and 600+ editorial MD files sit unimported on disk (`ENRICH=1` never run). So "Doc 4 corpus connection" is re-scoped: the job is editorial import + embeddings so Discover/Vesper are *rich*, not making slugs *resolve*. The sequenced run for this lives in Doc 5.

---

## The one system (north-star)

```text
                         ┌──────────────────────────────────────┐
   AUTHORING (Cursor)    │  ONE WORLD GRAPH (slugs)             │
   ─────────────────     │                                      │
   A: tools/seed JSON ──►│  Postgres entities + briefs          │
   B: content/staging MD►│  Qdrant briefs/dossiers/angles       │
                         └──────────────────┬───────────────────┘
                                            │ referenced by (never duplicated)
                                            ▼
   CATALOG (→ prod, quality-gated)   ┌──────────────────────────┐
   FIXTURES (→ cohort-isolated) ────►│  Dogfood manifests       │
                                     │  trips, blocks, saves,   │
                                     │  discover queries, atlas │
                                     └──────────────┬───────────┘
                                                    │ seed.py
                                                    ▼
                            ┌───────────────────────────────────┐
                            │  Product surfaces (rich)          │
                            │  Plan · Discover · Atlas · Vesper │
                            └──────────────┬────────────────────┘
                                           │ exercised by
                                           ▼
                            ┌───────────────────────────────────┐
                            │  ONE CERTIFY LADDER (holistic QA) │
                            │  fast → logic → visual → live     │
                            └───────────────────────────────────┘
```

**Invariant:** one slug graph, referenced (not copied) by manifests, consumed by surfaces, exercised by one QA ladder. Mock fixtures mirror the same slugs — no third namespace.

---

## Four layers, one source of truth each

The cleanup goal in one table — every layer has exactly **one** canonical source:

| Layer | Single source of truth | Parallel systems to kill |
|-------|------------------------|--------------------------|
| **World content** | `tools/seed` (A) + `content/staging` (B) → Postgres/Qdrant | thin-only `import_staged_refs`; manifest-duplicated venue copy |
| **Lived fixtures** | dogfood manifests (`tools/dogfood/content/manifests`) | `seed_group_trip.py` (fixed-UUID drift) |
| **Scenarios** | `scenarios.yaml` | `Dogfood Scenario Matrix.md` (manual mirror) |
| **QA** | `docs/journeys/STATUS.md` + certify ladder | Golden Paths; 7 fragmented QA commands; `discover_queries` log-only fiction |
| **Images** | backend `photo_resolve` + place-riso bundle | unprovisioned CDN vs bundle drift |
| **Environments** | **two deliberate profiles:** local workbench (Docker PG + Docker Qdrant) + Fly certified (Fly PG + cloud Qdrant); promote explicitly | split-brain (local PG → cloud Qdrant); `seed-s4-fly` as only Fly path |

---

## Current state vs target (honest scorecard)

| Capability | Target | Today | Gap |
|------------|--------|-------|-----|
| Certify ladder | 4 tiers, one ritual | ✅ **Exists** (`certify-fast/logic/visual/live`) | Some uncommitted; not corpus-aware |
| Dogfood status CLI | one command | ✅ **Exists** (`make dogfood-status`) | — |
| S4 seed | one command local + Fly | ✅ **Exists** (`seed-s4-local`, `seed-s4-fly`) | Per-city generalization missing |
| Itinerary → real places (FK) | all blocks resolve | ✅ **verified** (59/59 slugs, elif Rome FKs) | — |
| Itinerary blocks have briefs/dossiers | rich, not stub | ✅ Phase 2a done — slug bridge 9/9 canonical → editorial (verified `slug_bridge.py --verify`) | — |
| World corpus connected | full A+B import | ✅ Phases 0–2c complete (Lisbon/Rome/Istanbul/Tokyo/Brooklyn; Tier A+B latent local) | — |
| Environment pairing | atomic PG + Qdrant per profile | ✅ Phase 0.5 done — `PROFILE=local\|fly`, split-brain guard enforced in `dogfood-env.sh:96-117` | — |
| Fly dogfood world | promoted corpus + fixtures on Fly | ✅ Phase 2b done — 5 cities promoted to Fly (Lisbon/Rome/Istanbul/Tokyo/Brooklyn) | — |
| Discover queries | seeded or regression-tested | ✅ compose regression (`certify-logic`, `AI_MODE=replay`) | Doc 4 §discover fix |
| Mock = backend slugs | one namespace | ✅ Phase 3 done — `resolveMockAnchorSlug` + corpus angle fixtures (decommission item 5) | — |
| Content governance | catalog/fixture explicit | 🟡 documented (Doc 4) | Adopt tier field |
| Broken gates | none | ✅ **fixed** — `itinerary.test.ts` refs removed from `test:offline` + `mock-real-parity.sh` | Doc 1 P0-1 (Stream A) ✅ |
| `mara.ts` + mock fidelity | exists | ✅ **done** (Stream D) | — |
| Wedge E2E retired → `test_j05` | one path | ✅ **done** (Stream B) | — |
| Image coverage | referenced cities bundled | 🟡 6 cities missing | Stream E (handed off) |

**Net:** the *machine* (ladder, seed, status) is largely built **and the world is structurally connected** (slugs resolve, FKs wired); the remaining run is **enrichment** (editorial import + embeddings so the connected world is *rich*), *decommissions*, and *governance adoption* — now enforced by a gate, not just documented (Doc 5).

---

## Decommission tracker (kill parallel systems)

The single checklist that makes "no parallel systems" real. Each item = one parallel system retired.

- [x] **`seed_group_trip.py`** → deleted 2026-06-28; canonical `tools/dogfood/content/seed.py` only
- [x] **`discover_queries` log-only fiction** → compose regression for wedge queries in `test_discover_manifest_queries_compose.py` (`AI_MODE=replay`, `make certify-logic`) *(2026-06-29)*
- [x] **Golden Paths as separate QA set** → collapsed into journeys; `journey-wedge-qa` + `golden-path-qa` alias *(2026-06-29)*
- [x] **Triple scenario docs** → `validate_scenarios` in `dogfood-status`; `scenarios.yaml` sole machine source *(2026-06-29)*
- [x] **Mock compose Lisbon-only** → `resolveMockAnchorSlug` + dogfood corpus angle fixtures *(2026-06-29)*
- [ ] **`import_staged_refs` (thin) as the de-facto importer** → structural import works (slugs resolve); make full enrichment (promote + dossiers + embed, `ENRICH=1`) the default for launch-candidate cities *(Doc 4, Doc 5 Phase 1–2)*
- [x] **Broken `offline-qa` / `mock-real-parity`** (missing `itinerary.test.ts`) → ✅ refs removed (Stream A, committed 2026-06-28) *(Doc 1 P0-1)*
- [ ] **Image tier drift** → provision `seed_place_illustrations` for backend/CDN parity OR accept bundle-only + document *(Doc 3)*

> Track completion here so the kill-list dies in one place instead of being re-discovered per session.

---

## Smooth dogfood — the single workflow

### Exists today

```bash
make dogfood-status              # validate manifests + scenario/pack readiness
make corpus-check                # gate: slugs resolve + governance
make dogfood-city CITY=lisbon    # connect + seed (APPLY=1 ENRICH=1 for full enrich)
make dogfood-promote CITY=lisbon # Fly promote (Phase 0.5 — PROFILE=fly)
make seed-s4-local               # legacy narrow S4 local seed
- [ ] **`seed-s4-fly`** → deprecated; use `dogfood-promote CITY=lisbon` for full promote *(2026-06-29: wrapper retained with deprecation banner)*
make certify-fast                # Tier 1: local profile
make certify-logic               # Tier 2: journey scenario pytest (Postgres)
make certify-visual              # Tier 3: wedge Maestro flows
make certify-live                # Tier 4: Fly profile — EAS + AI QA
```

### Dual environment workflow

**Local (workbench):** iterate corpus, run go/no-go, desk dogfood with `make dev-backend`.

**Fly (certified):** EAS phone builds + AI-enabled QA hit Fly API + Fly Postgres + cloud Qdrant.

Promotion is one-way: local validate → `make dogfood-promote CITY=` → `certify-live` green.

`make corpus-check` joins the certify ladder so manifests never reference unstaged slugs. **Governance enforcement** (Doc 5 Phase 0): fails on manifest-embedded entities or missing corpus tier tags.

---

## QA loop closure (rich world × holistic AI QA)

The payoff: once the world is connected, the certify ladder must **exercise it**, not a parallel mock.

| Tier | Today | Connected-world target |
|------|-------|------------------------|
| **fast** | contract + journey Jest + offline pytest | + `corpus-check` (slugs resolve) |
| **logic** | journey scenario pytest | + discover compose regression on manifest queries (`AI_MODE=replay`) |
| **visual** | wedge Maestro | run against seeded corpus (real venue cards, not stubs) |
| **live** | two-account walk checklist | **Fly profile** + Vesper retrieval spot-check (cites real dossiers on promoted corpus) |

This is what ties "rich world" to "how we QA holistically with AI": the same slug graph that makes dogfood feel real is the graph QA asserts against.

---

## Sequenced execution (what order, what's done)

| Step | Work | Status | Source |
|------|------|--------|--------|
| 0 | Certify ladder + dogfood-status + seed-s4 | ✅ built + committed (`eddd26a`) | Makefile |
| 1 | Fix broken gates (`itinerary.test.ts`) | ✅ done (Stream A) | Doc 1 P0-1 |
| 2 | `mara.ts` + mock fidelity (Jest dedupe) | ✅ done (Stream D) | Doc 4 / Doc 2 |
| 3 | Wedge E2E retired → `test_j05_plan_edit_commit` | ✅ done (Stream B) | Doc 1 |
| 4 | Lisbon **enrichment** + go/no-go | ✅ Doc 5 Phase 1 GO | Doc 5 |
| 4b | **Environment profiles** (`PROFILE=local|fly`, `dogfood-promote`, split-brain fix) | ✅ Done (Phase 0.5 — dogfood-env.sh:96-117 enforced) | Doc 5 |
| 5 | Wedge substrate richness (proposals/home cards in manifest) | ⬜ verify vs Stream B | Doc 2 |
| 6 | Mock slug parity (compose city-scope, place angles) | ✅ Done (decommission item 5 — `resolveMockAnchorSlug` + angle fixtures) | Doc 4 Phase 4 |
| 7 | Rome **enrichment** | ✅ Done (Phase 2 — 322 editorial files, ~207 briefs) | Doc 5 |
| 7a | Rome **slug bridge** (canonical ↔ editorial) | ✅ Done (Phase 2a — 9/9 canonical briefs, `slug_bridge.py --verify`) | Doc 5 |
| 7b | Istanbul/Tokyo/Brooklyn (Phase 2b) | ✅ Done (Phase 2b — all 3 promoted to Fly) | Doc 5 |
| 7c | Latent corpus Tier A + B (Phase 2c) | ✅ Done (Phase 2c — Tier A+B local + Fly spot-check) | Doc 5 |
| 8 | Decommission tracker (8 items) | 🟡 6/8 done; 2 open (import_staged_refs + image tier drift) | this doc |
| 9 | `make dogfood-city` + `make corpus-check` | ✅ Doc 5 Phase 0 | this doc |
| 10 | Place illustrations (6 cities) | ⏳ handed off | Doc 3 / Stream E |

> **Updated 2026-06-30:** Phases 0–3 + 2a/2b/2c ALL COMPLETE. Five cities promoted
> to Fly (Lisbon/Rome/Istanbul/Tokyo/Brooklyn). Latent corpus Tier A+B local+Fly done.
> Only remaining work: step 5 (wedge substrate richness needs verify vs Stream B),
> step 8 (2 open decommission items: import_staged_refs + image tier drift).

Discipline (unchanged): **Lisbon wedge to W3 before broadening.** Each city: local profile first → promote → certify on Fly.

---

## Definition of done — "everything in place"

This run is complete when:

- [x] `make corpus-check` green for lisbon-phase1 + elif-rome (0 unresolved slugs) **and enforcing governance**
- [x] **Dual env:** `PROFILE=local|fly` + `make dogfood-promote`; no split-brain — Phase 0.5 done ✅
- [x] **Phase 1 go/no-go passed:** enriched Lisbon cites real dossiers on local profile ✅
- [x] **Phase 2a:** Rome canonical manifest slugs have briefs/retrieval (slug bridge 9/9 ✅)
- [x] **Fly promoted:** Lisbon + Rome corpus + fixtures on Fly for EAS + AI QA ✅
- [x] **Phase 2c Tier A:** latent persona-adjacent cities imported as `proof_only` (local then promote) ✅
- [ ] Decommission tracker: 6/8 done; 2 open (import_staged_refs thin importer + image tier drift)
- [x] Certify ladder tiers exercise the connected world (corpus-check + compose regression wired)
- [x] Catalog/fixture governance adopted (corpus tier tagged; `corpus_governance.py` enforces)
- [x] `docs/journeys/STATUS.md` is the sole QA index (Golden Paths demoted)
- [x] One front door: this doc links all four plans; no orphan parallel docs

---

## Environment model (dual profiles — see Doc 5 Phase 0.5)

Two deliberate dogfood worlds, not one split stack:

| Profile | Postgres | Qdrant | Use |
|---------|----------|--------|-----|
| **`local`** | Docker local | Docker local | Workbench: iterate corpus, desk dev, go/no-go |
| **`fly`** | Fly/Neon (`PROD_DATABASE_URL`) | Qdrant Cloud | EAS phone dogfood + AI-enabled QA |

**Invariant:** embed always from the **same** Postgres the API reads. Promotion (`make dogfood-promote CITY=`) is explicit local → Fly.

- **Catalog** (world corpus) → quality-gated; promote to Fly after local spot-check.
- **Fixtures** (lived substrate) → cohort-isolated (`@dogfood.local`), `--allow-prod` gated on Fly promote.
- **Split a dedicated `vesper-backend-dogfood` Fly app** only when: external testers, analytics isolation, or frequent destructive reseed. Until then: shared Fly + cohort guards.

---

## Bottom line

You're closer than the four docs imply: the **certify ladder, dogfood-status, and S4 seed already exist**. What converts "substantially cleaner" into "one clean system" is finishing three things this doc now owns: **connect the world** (Doc 4 execution), **kill the 8 parallel systems** (decommission tracker), and **wire the connected world into the certify ladder** (QA loop closure) — plus a single `make dogfood-city` so the whole thing is one command.

**Status 2026-06-30:** Phases 0–3 + 2a/2b/2c all complete. Remaining open items: (a) step 5 — wedge substrate richness needs verification vs Stream B; (b) 2 decommission items — `import_staged_refs` thin importer default + image tier drift. See decommission tracker above.
