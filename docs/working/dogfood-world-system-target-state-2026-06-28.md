# Dogfood & World System — Target State + Decommission Plan

> Status: north-star / canonical index
> Owner: founder / engineering
> Created: 2026-06-28
> Last updated: 2026-06-28
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
| — | **this doc** | The unified target state these four converge to |

---

## TL;DR

Executing the four plans gets the **content/world layer genuinely clean**. This doc closes the remaining **integration layer** so all three of your hardest goals are met:

- **No confusion where content goes** → one content-governance model (catalog → prod; fixtures → cohort-isolated).
- **No parallel systems** → an explicit decommission tracker (8 systems to kill).
- **Holistic AI QA** → the certify ladder runs against the *connected* world, not mock/thin backend.

**Pleasant surprise (verified 2026-06-28):** the 4-tier **certify ladder already exists** in the workspace `Makefile` (`certify-fast/logic/visual/live`), along with `dogfood-status`, `seed-s4-local`, `seed-s4-fly`. Much of the "system cleanup" is already built (some uncommitted). The remaining work is **wiring corpus in, killing parallels, and one orchestrator** — not building the ladder from scratch.

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
| **Environments** | shared Fly + cohort guards (until split trigger) | (none yet — keep until trigger) |

---

## Current state vs target (honest scorecard)

| Capability | Target | Today | Gap |
|------------|--------|-------|-----|
| Certify ladder | 4 tiers, one ritual | ✅ **Exists** (`certify-fast/logic/visual/live`) | Some uncommitted; not corpus-aware |
| Dogfood status CLI | one command | ✅ **Exists** (`make dogfood-status`) | — |
| S4 seed | one command local + Fly | ✅ **Exists** (`seed-s4-local`, `seed-s4-fly`) | Per-city generalization missing |
| Itinerary → real places | all blocks resolve w/ brief | 🟡 Lisbon/Rome phased (Doc 4) | Execute Phase 1–2 |
| World corpus connected | full A+B import | ❌ thin `import_staged_refs` only | Doc 4 core work |
| Discover queries | seeded or regression-tested | ❌ log-only | Doc 4 §discover fix |
| Mock = backend slugs | one namespace | ❌ mock compose Lisbon-only | Doc 4 Phase 4 |
| Content governance | catalog/fixture explicit | 🟡 documented (Doc 4) | Adopt tier field |
| Broken gates | none | ✅ **fixed** — `itinerary.test.ts` refs removed from `test:offline` + `mock-real-parity.sh` | Doc 1 P0-1 (Stream A) ✅ |
| `mara.ts` + mock fidelity | exists | ✅ **done** (Stream D) | — |
| Wedge E2E retired → `test_j05` | one path | ✅ **done** (Stream B) | — |
| Image coverage | referenced cities bundled | 🟡 6 cities missing | Stream E (handed off) |

**Net:** the *machine* (ladder, seed, status) is largely built; the *world connection*, *decommissions*, and *governance adoption* are the remaining run.

---

## Decommission tracker (kill parallel systems)

The single checklist that makes "no parallel systems" real. Each item = one parallel system retired.

- [ ] **`seed_group_trip.py`** → delete; canonical `tools/dogfood/content/seed.py` only *(Doc 1, Doc 2)*
- [ ] **`discover_queries` log-only fiction** → compose regression for wedge queries OR rename to `discover_query_contracts` *(Doc 4)*
- [ ] **Golden Paths as separate QA set** → collapse into journeys; `golden-path-qa.sh` points at journey tests *(Doc 1)*
- [ ] **Triple scenario docs** → `scenarios.yaml` sole source; generate or drop `Dogfood Scenario Matrix.md` *(Doc 1)*
- [ ] **Mock compose Lisbon-only** → city-scoped to trip; slug parity with manifests *(Doc 4 Phase 4)*
- [ ] **`import_staged_refs` as the only importer** → full import (promote + dossiers + embed) is default for launch-candidate cities *(Doc 4)*
- [x] **Broken `offline-qa` / `mock-real-parity`** (missing `itinerary.test.ts`) → ✅ refs removed (Stream A, committed 2026-06-28) *(Doc 1 P0-1)*
- [ ] **Image tier drift** → provision `seed_place_illustrations` for backend/CDN parity OR accept bundle-only + document *(Doc 3)*

> Track completion here so the kill-list dies in one place instead of being re-discovered per session.

---

## Smooth dogfood — the single workflow

### Exists today

```bash
make dogfood-status              # validate manifests + scenario/pack readiness
make seed-s4-local               # seed S4 lisbon fixtures → local Postgres
make seed-s4-fly                 # seed S4 → Fly (dry-run; SEED_S4_FLY_APPLY=1 to write)
make certify-fast                # Tier 1: contract + journey Jest + offline backend
make certify-logic               # Tier 2: journey scenario pytest (Postgres)
make certify-visual              # Tier 3: wedge Maestro flows
make certify-live                # Tier 4: dogfood preflight + live-walk checklist
```

### Proposed addition — one-command city connection

Generalize the S4-specific seed into a per-city orchestrator that runs the full A+B+fixture connection (Doc 4's 5 steps) behind one target:

```bash
make dogfood-city CITY=lisbon    # audit → import A → import B → embed → seed → readiness
make corpus-check                # NEW gate: every manifest slug resolves in corpus
```

`make corpus-check` joins the certify ladder (Tier 1 or a pre-seed gate) so a manifest can never reference an unstaged slug without CI catching it.

---

## QA loop closure (rich world × holistic AI QA)

The payoff: once the world is connected, the certify ladder must **exercise it**, not a parallel mock.

| Tier | Today | Connected-world target |
|------|-------|------------------------|
| **fast** | contract + journey Jest + offline pytest | + `corpus-check` (slugs resolve) |
| **logic** | journey scenario pytest | + discover compose regression on manifest queries (`AI_MODE=replay`) |
| **visual** | wedge Maestro | run against seeded corpus (real venue cards, not stubs) |
| **live** | two-account walk checklist | + Vesper retrieval spot-check (cites real dossiers) |

This is what ties "rich world" to "how we QA holistically with AI": the same slug graph that makes dogfood feel real is the graph QA asserts against.

---

## Sequenced execution (what order, what's done)

| Step | Work | Status | Source |
|------|------|--------|--------|
| 0 | Certify ladder + dogfood-status + seed-s4 | ✅ built + committed (`eddd26a`) | Makefile |
| 1 | Fix broken gates (`itinerary.test.ts`) | ✅ done (Stream A) | Doc 1 P0-1 |
| 2 | `mara.ts` + mock fidelity (Jest dedupe) | ✅ done (Stream D) | Doc 4 / Doc 2 |
| 3 | Wedge E2E retired → `test_j05_plan_edit_commit` | ✅ done (Stream B) | Doc 1 |
| 4 | Lisbon corpus connection (Phase 1) | ⬜ Stream F | Doc 4 |
| 5 | Wedge substrate richness (proposals/home cards in manifest) | ⬜ verify vs Stream B | Doc 2 |
| 6 | Mock slug parity (compose city-scope, place angles) | ⬜ Stream D follow-up | Doc 4 Phase 4 |
| 7 | Rome corpus connection (Phase 2) | ⬜ Stream F | Doc 4 |
| 8 | Decommission tracker (remaining 7 items) | ⬜ ongoing | this doc |
| 9 | `make dogfood-city` + `corpus-check` | ⬜ engineering | this doc |
| 10 | Place illustrations (6 cities) | ⏳ handed off | Doc 3 / Stream E |

Discipline (unchanged): **Lisbon wedge to W3 before broadening.** Don't connect editorial city #7 or split the backend until a trigger fires.

> **Reality check (verified 2026-06-28):** Streams A, B, and D have substantially landed
> (certify ladder, gate fix, wedge-E2E retirement, `mara.ts`, mock fidelity, Jest dedupe).
> The remaining run is **corpus connection (Stream F)**, **mock slug parity**, the
> **decommission tracker**, and the **`dogfood-city`/`corpus-check` engineering** — i.e. the
> integration layer, not the streams.

---

## Definition of done — "everything in place"

This run is complete when:

- [ ] `make corpus-check` green for lisbon-phase1 + elif-rome (0 unresolved slugs)
- [ ] `make dogfood-city CITY=lisbon` runs the full connection end-to-end
- [ ] Decommission tracker: all 8 items closed
- [ ] Certify ladder tiers exercise the connected world (corpus-check + compose regression wired)
- [ ] Catalog/fixture governance adopted (corpus tier tagged; analytics-exclusion + egress + reset guardrails in place)
- [ ] `docs/journeys/STATUS.md` is the sole QA index (Golden Paths demoted)
- [ ] One front door: this doc links all four plans; no orphan parallel docs

---

## Environment model (recap — see Doc 4 for detail)

- **Catalog** (world corpus) → production, quality-gated. Importing to Fly is correct, not a violation.
- **Fixtures** (lived substrate) → cohort-isolated (`@dogfood.local`, `_dogfood`), `--allow-prod` gated, resettable.
- **Split a dedicated `vesper-backend-dogfood`** only when: external testers create real data, OR real users need clean analytics, OR destructive reseed is frequent. Until then: shared Fly + cohort guards.

---

## Bottom line

You're closer than the four docs imply: the **certify ladder, dogfood-status, and S4 seed already exist**. What converts "substantially cleaner" into "one clean system" is finishing three things this doc now owns: **connect the world** (Doc 4 execution), **kill the 8 parallel systems** (decommission tracker), and **wire the connected world into the certify ladder** (QA loop closure) — plus a single `make dogfood-city` so the whole thing is one command.

**Next action:** commit the existing Makefile/script work (step 0), then run Stream A (fix gates) + Stream F (Lisbon corpus) against this target.
