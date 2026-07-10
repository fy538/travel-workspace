---
doc_type: archive
status: archived
owner: founder / engineering
created: 2026-07-09
archived: 2026-07-09
why_new: Move reviewed completed evidence out of the living documentation tree without deleting its historical record.
---

# Dogfood, QA, Substrate & Product System — Comprehensive Investigation

> Archived from the living documentation tree on 2026-07-09 during Phase 5 cleanup.

> Status: investigation note  
> Owner: founder / engineering  
> Created: 2026-06-28  
> Last updated: 2026-06-28  
> Scope: `travel-agent`, `travel-app`, workspace `docs/`  
> Method: git history, system charters, journey matrix, substrate tooling, QA scripts, CI configs, code verification  
> Verified: 2026-06-28 — claims re-checked against code/git; corrections applied (frontend test count ~1,005→~274, routers 54→63, P0-2 logic-qa now committed)

This document consolidates three deep investigations:

1. **Product & codebase progress** — what was built, day-by-day timeline, vision alignment  
2. **Dogfood push vs substrate vs QA flows** — how the lanes interact  
3. **Streamlining opportunities** — friction, duplication, and concrete simplification plan  

---

## Table of contents

1. [Executive summary](#executive-summary)
2. [Product vision & progress](#product-vision--progress)
3. [Architecture overview](#architecture-overview)
4. [The 14 product systems](#the-14-product-systems)
5. [Day-by-day accomplishment timeline](#day-by-day-accomplishment-timeline)
6. [Journey & quality status](#journey--quality-status)
7. [Dogfood push & wedge definition of done](#dogfood-push--wedge-definition-of-done)
8. [Substrate, mock data & dogfood world](#substrate-mock-data--dogfood-world)
9. [QA certification stack](#qa-certification-stack)
10. [How lanes interact](#how-lanes-interact)
11. [Build profiles & environments](#build-profiles--environments)
12. [Streamlining audit — what's broken](#streamlining-audit--whats-broken)
13. [Streamlining audit — duplication to collapse](#streamlining-audit--duplication-to-collapse)
14. [Streamlining audit — substrate friction](#streamlining-audit--substrate-friction)
15. [Proposed single certify ladder](#proposed-single-certify-ladder)
16. [What to stop doing](#what-to-stop-doing)
17. [Prioritized action list](#prioritized-action-list)
18. [Key file index](#key-file-index)
19. [Evidence & verification notes](#evidence--verification-notes)

---

## Executive summary

In **78 calendar days** (2026-04-12 → 2026-06-28, 2026), Vesper went from empty repos to a feature-rich, contract-driven travel concierge approaching dogfood. Both child repos started the same day; the workspace coordination layer began 2026-05-01.

| Metric | Value |
|--------|-------|
| Active coding days | 66 |
| Total commits | ~2,590 (Backend ~1,502 · Frontend ~944 · Workspace ~144) |
| Peak month | May 2026 — 1,364 commits |
| OpenAPI surface | 310 paths · 345 operations · 588 schemas |
| Backend test files | 707 |
| Frontend test files | ~274 |
| Maestro flows | 62 (committed YAML, excluding `config.yaml`) |
| Postgres tables | 142 |
| API routers | 63 |

**Product headline:** The hard part is largely done — thesis, backend spine, typed contracts, 14 system charters, 12 canonical journeys, serious reliability gates.

**Dogfood headline:** Feature completeness ≠ dogfood readiness. All 12 journeys pass static trace, mock walk, and Logic QA MVP — but **0/12 are dogfood-ready**. Current phase is **proof, not construction**.

**QA headline:** The right layers exist (mock → logic → visual → live), but parallel vocabularies, duplicate tests, broken gates, and stale docs create **fiction** — things look green while daily rituals don't match CI or dogfood reality.

**Highest-efficiency move:** One certify ladder, fix broken gates, retire duplicates, seed **S4 (Lisbon group)** to Fly once — so mock-certified and dogfood-certified mean the same world for the wedge.

---

## Product vision & progress

### What Vesper is

From `travel-agent/docs/product/Product Thesis.md`:

> A place-aware travel concierge companion that helps people get more out of trips by understanding the traveler, the place, the trip, and the group — then acting through the right modality at the right moment.

| Element | Value |
|---------|-------|
| Subtitle | "The trip, before the asking" |
| Launch wedge | Group trip planning (belief #14 — *the invite is the distribution*) |
| Target user | The **Organizer** — the friend who plans everything for the group |
| Moat | Compounding **travel world model** — people, places, trips, memories, groups, taste — inspectable and controllable |

### Three vision claims and progress

| Claim | Progress |
|-------|----------|
| **1. Get more out of trips**, not merely plan them | Strong — planning, live companion, post-trip memory/story/settlement exist as surfaces |
| **2. Group trips are the wedge; world model is the moat** | Strong substrate — Personal Memory, Atlas, group profiles, observations |
| **3. AI consequences must be inspectable and controllable** | Strong architecture — proposals, Change Studio, trust receipts, privacy egress guards, revert; still needs live proof |

### Four product surfaces

| Surface | Role |
|---------|------|
| **Vesper** | Continuous concierge — private chat, group chat mediation, proactive help, voice (built-dark) |
| **Trips** | Plan, map, changes, Folio home, group workspace, stays, expenses |
| **Discover** | Editorial place intelligence → Ask Vesper → trip action |
| **Atlas** | Loved places, artifacts, Travel DNA, privacy controls, post-trip story |

### Phase assessment

```
Apr–May 2026: Build substrate + surfaces
Jun 2026:     Consolidate, certify, harden state machines
Next:         Prove wedge (J02→J05) on real phone with real second user
```

The wedge doc is explicit: *"Do not start new substrate until this slice is genuinely dogfood-ready."*

---

## Architecture overview

### Travel Agent (Backend)

| Layer | Technology |
|-------|------------|
| API | FastAPI (`backend.api.main:app`) |
| DB | PostgreSQL 15 via SQLAlchemy Core (142 tables) |
| Vector | Qdrant (venue/experience briefs) |
| LLM | Anthropic via `backend/core/llm.py` |
| Auth | Clerk JWT (`SKIP_AUTH=true` for local dev) |
| Deploy | Docker + Fly.io (`vesper-backend`) |

**Five LLM agents** (cross-import forbidden; communicate via DB/Qdrant):

| Agent | Purpose |
|-------|---------|
| Concierge | Chat, streaming SSE, tools, memory capture, output guards |
| Planning | Itinerary generation, restaurant sub-agent, feasibility repair |
| Research | LangGraph deep research, dossiers, content pipelines |
| Booking | LangGraph multi-provider search, holds, checkout |
| Preference | Observation-based retrieval, group context synthesis |

Plus **lookup_agent** for fast factual queries.

**Key modules:** `composition/`, `atlas/`, `discover/`, `home/`, `situation/`, `notifications/`, `social_state/`, `places/`, `voice/`, `workers/`, `expenses/`, `digest/`, `postcard/`

### Travel App (Frontend)

| Layer | Technology |
|-------|------------|
| Framework | React Native 0.83 · React 19 · Expo SDK 55 |
| Routing | Expo Router (~100 route files) |
| State / data | TanStack React Query v5 |
| Auth | Clerk (`@clerk/clerk-expo`) |
| Maps | Mapbox (`@rnmapbox/maps`) |

**Data layer pattern:**

```
Screens → data/*.ts hooks → hooks/useData.ts → utils/api (mockApi | httpApi) → FastAPI
```

Types from generated `schema.gen.ts` (OpenAPI snapshot: workspace `docs/openapi.json`).

Largest UI file: `components/trip/TripFolioHome.tsx` (~4,880 lines) — backend-driven trip home via `/folio` read model.

### Workspace coordination layer

Started 2026-05-01. Owns:

- Canonical `docs/openapi.json` snapshot
- `scripts/sync-types.sh`, `make contract-check`, reliability CI
- Journey docs, system charters, audit campaigns, deploy runbooks

---

## The 14 product systems

From `docs/systems/README.md`. **MVP-required** systems must reach `wired+validated` before first real users. All are currently `wired` (reachable, not live-validated).

| System | Surface | MVP tier | Status | Key journeys |
|--------|---------|----------|--------|--------------|
| Concierge (Vesper) | Vesper | MVP-required | wired | 01, 04, 05, 07, 08 |
| Memory & Preference | Vesper | MVP-required | wired | 04, 11 |
| Trips / Folio | Trips | MVP-required | wired | 03, 06 |
| Planning / Itinerary | Trips | MVP-required | wired | 05 |
| Proposals / Change Studio | Trips | MVP-required | wired | 05 |
| Group / Social | Trips | MVP-required | wired | 02, 04, 05 |
| Proactive / Notifications | Vesper | Should-have | wired | 09 |
| Expenses / Settlement | Trips | Should-have | wired (least hardened) | 10, 12 |
| Discover | Discover | Should-have | wired | 07 |
| Atlas | Atlas | Should-have | wired | 11, 12 |
| Places (hours/open) | Trips | Should-have | wired | 08 |
| Booking | Trips | Built-dark | partial/dark | 10 |
| Voice / Narration | Vesper | Built-dark | dark | deferred |
| Postcard / Story | Atlas | Built-dark | dark | 12 |

---

## Day-by-day accomplishment timeline

*Dates with no commits omitted. B = Backend, F = Frontend, W = Workspace.*

### April 2026 — Foundation (118 commits)

| Date | Accomplishments |
|------|-----------------|
| **2026-04-12** | **Day zero.** Both repos initialized. Backend: travel-agent scaffold, early memory consolidation, expense foundations. App: Expo navigation, design system, mock screens. |
| **2026-04-13** | Backend: events, preference engine, signal-deprecation thinking. |
| **2026-04-14** | Backend: content knowledge graph, BFS research, agent cleanup. |
| **2026-04-15** | Backend: agent seeding, notebook setup. |
| **2026-04-16** | Backend: notifications, tour/location-adjacent work. |
| **2026-04-17** | Backend platform leap: Discover/editorial collections, eval tooling, API coverage, research tracing, brief regeneration, Alembic repair. |
| **2026-04-18** | **Dogfood pivot:** dev flags, real API mode, Clerk auth, SKIP_AUTH bypass, seeding hardening. App: real-API bug fixes. |
| **2026-04-19** | Backend: seed data, venue quality, booking/push/location, backfill cleanup. |
| **2026-04-20** | Backend: location context agent. |
| **2026-04-24** | Backend: backfill work. |
| **2026-04-25** | **Agent reliability sprint:** Brooklyn concierge evals, privacy checks, group-compose leak fixes, booking urgency, MCP evals. |
| **2026-04-26** | Eval portfolio expansion; retrieval/tool fixes; anti-confabulation tuning. |
| **2026-04-27** | Preference display names, handoff evals, concerts/nightlife skills. App: Discover component extraction, mock bleeding removed. |
| **2026-04-30** | Backend: concierge tool handler refactor. App: plan/journal/proposal/venue actions wired. |

### May 2026 — Explosive Build (1,364 commits)

| Date | Accomplishments |
|------|-----------------|
| **2026-05-01** | Real itinerary coordinates, digest endpoint, OpenAPI MCP tool. App: mock hooks → real backend, Zod/test/CI scaffolding. **Workspace repo born.** |
| **2026-05-02** | Insight/For You/trip-highlight endpoints, SSE tool status, social intent. App: Events tab, hook tests. |
| **2026-05-03** | **Huge full-stack day.** Backend: guide agent, trust-layer recommendations, photos, post-trip subscriber. App: streaming group chat, invite landing, expenses CRUD, Discover angles/search, notifications, guide screens, daily digest, schema sync. |
| **2026-05-04** | Guide streaming/TTS, narration pre-render, outcome tracking. |
| **2026-05-05** | Onboarding intake, skill registry, SendGrid invites, Voice Guide phases, geofence stops. App: immersive guide/audio UI. |
| **2026-05-06** | App: accommodations, follow/booking/member APIs, accommodation CRUD. |
| **2026-05-08** | Taste DNA, Discover loop, post-trip/memory beginnings, invites, proactive notifications, personal memory surfaces. |
| **2026-05-09** | **Hardening day.** Backend: voice-guide foundation, invite push/SMS, TTFT telemetry, red-team evals, mypy zero, prompt/table modularization. App: privacy audit, polymorphic For You cards, generated types. |
| **2026-05-10** | **Trip Home v1–v5:** attention sections, three-zone feed, dismissal/undo, archetypes, group-state cards. |
| **2026-05-11** | **Trust loop + CI:** plan-state API, map read model, proposal invariants, plan_events ledger, diff-safe revert, privacy redactor, VCR/Soul QA, migration squash. App: Plan v2/Map v2, proposal trust surfaces, Expo SDK 55. |
| **2026-05-12** | Memory/trip story APIs, post-trip composition, content-safety scanner, eval replay, Brooklyn/Lisbon seeding, delegation preferences. App: proposal timeline/conflict UX, Memory home/story editing/share. |
| **2026-05-13** | Booking foundation, legal/privacy, photos, expense tools. App: photo album, mark-as-done, live-trip detection, expenses settlement. |
| **2026-05-14** | Eval baselines migrated to Qdrant; venue-naming discipline. |
| **2026-05-15** | **Excellence day:** eval promotion, content graph, grounding guard, dogfood tooling, Fly config, prompt-diff harness. App: Discover content gap, geofence refactor, mobile polish. |
| **2026-05-16** | Cross-trip threading, safety elicitation, tool consolidation. App: onboarding safety chips, Travel DNA cards/disputes, cross-trip threading UI. |
| **2026-05-17** | Memory drift, agent planning consolidation, route guards. App: API error/SSE handling, invite token survival. |
| **2026-05-18** | Frontend audit batches: auth/security, RN hygiene, type consolidation, offline/errors/forms/a11y. |
| **2026-05-19** | **Massive backend day (146 commits):** OpenAPI unification, release runbooks, Qdrant fixes, deploy hardening. |
| **2026-05-20** | Dogfood + social-loop substrate. App: Sentry, privacy/account deletion, destination-led trip creation, push persistence. |
| **2026-05-21** | Dogfood-readiness docs. App: Home/Plan/Map coherence, silent SSE auth redirect, fault injection. |
| **2026-05-22** | App: invite persistence, booking/voice honesty, Discover city bug fixes. |
| **2026-05-23** | **TestFlight boot:** EAS project, Expo audio migration, auth against Fly backend, OTA updates, startup crash fixes. |
| **2026-05-24** | **Largest frontend product day (75 commits):** chat card kit, Discover blended feed, Trips home simplification, immersive trip workspace, Plan redesign, story share landing. |
| **2026-05-25** | Live-trip layer: trip situation, ambient notices, narration interruption, proactive routing. |
| **2026-05-26** | **Atlas becomes a product surface.** Mapbox lazy-load. Backend: Atlas V1, leave-by, proactive support. Workspace: Atlas engineering plans. |
| **2026-05-27** | Chat/composer/streaming, Discover reader, Atlas review/artifact flows, trip overhaul phases. |
| **2026-05-28** | Trip-overhaul completion: standalone-to-trip promotion, Discover chooser, no eager trip creation. |

### June 2026 — Consolidation & Proof (1,108 commits)

| Date | Accomplishments |
|------|-----------------|
| **2026-06-02** | **Frontend revamp:** Claude design system, palette/shadows/typography, Atlas/trips/concierge/discover redesign. |
| **2026-06-03** | Chat/trip/Atlas design alignment, Document Edit spec. |
| **2026-06-04** | Design mockups, typography roles, Trip Home group-consensus/prep feed, API boundary cleanup. |
| **2026-06-05** | Dogfood/dev-persona QA tools. App: ConversationSeed migration, query-key registry, bottom-sheet unification, offline gating. |
| **2026-06-06** | Atlas Almanac/Timeline/removed moments. Backend: Atlas timeline stack. |
| **2026-06-09** | Push deep-link/card focus, Ask Vesper seed gap. |
| **2026-06-10** | **12 canonical journey docs** written. Large Home/Trips/Atlas/card-contract work. |
| **2026-06-11** | Home/trips/Atlas polish, content contract clamping. |
| **2026-06-12** | Dogfood trust journey contracts, Vesper Trust Receipts plan. App: Atlas v3 UI, design token bridge. |
| **2026-06-13** | Trips Home hero phases, Focus Home fixes, hero contract wiring. |
| **2026-06-14** | Focus Home pick deck face, changes attribution/votes, Atlas mocks/contracts. |
| **2026-06-15** | Folio/deck merge, TripFolioHome alignment, AtlasMemoryReel, Vesper pick substrate. |
| **2026-06-16** | Test reconciliation, trip-less chat routes, Concierge feed refresh. |
| **2026-06-17** | Discover Cover home, plan reasoning/feasibility explanations, booking trust receipt, background location push, Trip Story listen. |
| **2026-06-18** | Change Studio/Health Strip, plan-ready/proposal cards, instant card resolution. |
| **2026-06-19** | **Itinerary hardening round:** edit-preview/commit, conflict keep/dismiss, Now Mode, timezone fix, proposal voter counts, ghost/withdraw/supersede, idempotency, mark-happened. |
| **2026-06-20** | Retired legacy itinerary read model, unified conflict resolution, Atlas/Discover bug fixes. |
| **2026-06-21** | **Folio read model shipped.** Trip Home wired to backend `/folio`. Atlas/Discover composition consolidation. Contract check passes. |
| **2026-06-22** | Booking Phase 0–5 review fixes, Viator attribution, travel insurance CTA, visual QA phases 1–5, Trip Document redesign handoff. |
| **2026-06-23** | Onboarding: secure push at first trip-chat send. Live-trip intelligence. Booking agent v2 (Duffel, checkout reconciliation). |
| **2026-06-24** | Dogfood bootstrap tooling, remote user bootstrap, costs/settlement redesign, stay system, trust controls screens. **Scenario matrix + packs.yaml landed.** |
| **2026-06-25** | **State-machine hardening:** 36 lifecycle defects closed. Privacy egress guard. Journey fixes J01–J12. Cross-repo seam audits. |
| **2026-06-26** | Booking holds hardened, invite redemptions wired, drift guards, Discover/Atlas polish, dogfood media readiness. |
| **2026-06-27** | **Wedge certification:** 307 backend tests green, mock-walk tests J01–J12 committed, J05 scenario + plan-edit tests (I5/I6/I7/I8), 14 system charters written, Maestro flows 24/25 authored. |
| **2026-06-28** | **Stream A/B/D:** certify ladder (`certify-fast/logic/visual`), S4 local seed script, wedge E2E retired → `test_j05_plan_edit_commit.py`, J02/J05/J06 Jest dedupe, Mara persona + mock fidelity, `make dogfood-status`. CI: tool contract + journey scenario tests. Journey Certification Suite spec. Release polish. |

### Monthly commit volume

| Month | Backend | Frontend | Workspace | Total |
|-------|---------|----------|-----------|-------|
| 2026-04 | 104 | 14 | 0 | 118 |
| 2026-05 | 895 | 378 | 91 | 1,364 |
| 2026-06 | 503 | 552 | 53 | 1,108 |

---

## Journey & quality status

From `docs/journeys/STATUS.md` (2026-06-28):

| Gate | Status |
|------|--------|
| Static trace ready | **12 / 12** |
| Mock walk ready | **12 / 12** |
| Logic QA MVP green | **12 / 12** |
| Dogfood ready | **0 / 12** |

All P0/P1 static-trace blockers fixed by 2026-06-26. Next gates: Maestro on-device green, live two-account walk, external TestFlight user.

### The 12 canonical journeys

| # | Journey | Main risk protected |
|---|---------|-------------------|
| 01 | Vague Idea → Vesper-Shaped Trip | Cold start, Trips Home phases, onboarding handoff |
| 02 | Concrete Trip Creation + Invite | Shared workspace and invite membership correctness |
| 03 | Cold Trip Setup → Useful Workspace | Trip Folio state machine, empty states, setup slots |
| 04 | Private Constraint → Group-Safe Plan | Privacy contract across surfaces |
| 05 | Group Planning → Proposal → Plan Mutation | Advise → Propose → Act + Change Studio |
| 06 | Home, Plan, Map, Changes Coherence | Read-model consistency after any mutation |
| 07 | Discover → Contextual Vesper → Trip Action | ConversationSeed, place context, add-to-trip |
| 08 | Live Trip What-Now Companion | Active-trip usefulness, map/location context |
| 09 | Notifications + Proactive Routing | Push/feed routing, cadence, privacy-safe copy |
| 10 | Booking, Stay, Expense Trust Loop | Provider drift, hold-settle, opt-in expense |
| 11 | Atlas Candidate → Memory Control | Memory provenance, trust hub |
| 12 | Returned Trip → Story, Memory, Settle-Up | Post-trip loop, settlement |

---

## Dogfood push & wedge definition of done

### Strategic goal

Prove **one wedge journey end-to-end** before expanding TestFlight:

**J02 (create + invite) → J05 (propose + mutate) → see-it-everywhere (J06 coherence)**

Source: `docs/working/wedge-journey-02-05-path-to-dogfood.md`

Together: **create → invite → plan → propose → mutate → see-it-everywhere.** Smallest thing a real group can do and feel value from.

### Wedge Definition of Done (8 gates)

| # | Gate | State |
|---|------|-------|
| 1 | Charters current for every system in the slice | ✅ |
| 2 | Backend deterministic tests (scenario pytest incl. J05 I5–I8) | ✅ |
| 3 | Frontend mock-walk (J02/J05/J06 consolidated; 88 journey tests) | ✅ |
| 4 | Maestro on-device (flows 24 + 25) | 🔶 Authored, run pending |
| 5 | Live two-account walk (real Clerk + Fly) | ❌ |
| 6 | Invariants I1–I10 spot-checked live | ❌ |
| 7 | Dark features invisible (booking/voice/postcard) | ⬜ |
| 8 | One external user completes on TestFlight | ❌ |

### Wedge invariants (I1–I10)

| # | Invariant | System | Priority |
|---|-----------|--------|----------|
| I1 | Invite maps to exactly one trip; accept lands in correct workspace | Group/Social | High |
| I2 | Auth detour preserves invite token | Group/Social | High |
| I3 | Non-member sees no private trip data pre-accept | Group/Social | High |
| I4 | Private constraint never reaches the group | Memory+Concierge | **Critical** (unrecoverable trust event) |
| I5 | Accepted change emits visible receipt; rejected confirms original remains | Proposals | High |
| I6 | Revert truthfulness — Plan and Map reflect it | Proposals+Folio | High |
| I7 | Optimistic concurrency — stale `expected_updated_at` surfaces 409 | Proposals | High |
| I8 | Idempotency — retries never duplicate votes/applied changes | Proposals | High |
| I9 | Cross-surface coherence after mutation (Home/Plan/Changes/Map agree) | Folio | High |
| I10 | One proposal-creation path (`build_and_persist_proposal`) | Proposals | Medium |

**Server-side logic for I5–I8 is certified** by `tests/scenarios/test_j05_proposal_plan_mutation.py` and `tests/scenarios/test_j05_plan_edit_commit.py`. Live walk verifies **frontend wiring/surfacing** — receipt rendering, 409 conflict UI, double-apply prevention, revert display.

### TestFlight success signals (first 10 testers)

From `docs/TestFlight Tester Onboarding.md`:

| Signal | Threshold |
|--------|-----------|
| "Vesper said something my group needed to hear" | ≥3 of 10 |
| Post-trip Memory artifact kept | ≥1 tester |
| P0/P1 bugs | <5 total |
| Invited friend who signed up | ≥1 tester |

Decision rule: <2 of 4 → hold launch; 3 of 4 → cautious wider TestFlight; 4 of 4 → open public TestFlight.

---

## Substrate, mock data & dogfood world

### Core vocabulary

From `travel-agent/docs/operations/Environments Dogfood and Data Substrate.md`:

| Term | Meaning |
|------|---------|
| **Environment** | Where code runs (local, Fly `vesper-backend`) |
| **Frontend channel** | How app build is delivered (EAS development, dogfood, preview, production) |
| **Runtime mode** | Which paid/intelligent providers are allowed (`AI_MODE=off/replay/cheap/live`) |
| **Data cohort** | Which users and rows the product shows (`@dogfood.local`, eval, real users) |
| **Data substrate** | Authored/seeded world (trips, memories, Atlas, venues, photos) — not mocks alone |

**Operating rule:**

```
Environment = where code runs.
Cohort      = which users/data you see.
Mode        = what external providers may do.
```

### Infrastructure reality (critical)

> As of 2026-06-21, Vesper does **not** have a fully isolated dogfood backend.

The EAS `dogfood` profile hits **`https://vesper-backend.fly.dev`** — the same shared Fly backend as preview and production.

Implications:

- Seeding `@dogfood.local` users into Fly is a **deliberate prod-data operation** (needs `--allow-prod` + cohort guards).
- Frontend TS personas **do not appear** in the dogfood build (`USE_MOCK_API=false`).
- Local substrate counts ≠ Fly dogfood readiness.
- Acceptable for founder dogfood if cohort is explicit, namespaced, resettable, auditable.

### Two sources of truth (by design)

| | **Backend substrate** | **Frontend mock** |
|--|----------------------|-------------------|
| **Location** | `travel-agent/tools/dogfood/content/` | `travel-app/constants/personas/*.ts` |
| **Format** | YAML manifests → Postgres rows | `PersonaBundle` TypeScript fixtures |
| **Users** | `elif@dogfood.local`, `mara@dogfood.local`, etc. | `elif`, `ben`, `carmen`, `urgent`, `torture`, … (12 total) |
| **Activation** | Real HTTP + seeded DB | `EXPO_PUBLIC_USE_MOCK_API=true` |
| **Purpose** | API contract truth, backend-real dogfood | Fast UI/QA, Maestro, persona switcher |
| **Registry** | `scenarios.yaml` S1–S6 | `scenarios.yaml` M0–M11 |

The scenario matrix (`travel-agent/tools/dogfood/content/scenarios.yaml`) is the **Rosetta stone** linking both lanes.

### Backend-real scenarios (S1–S6)

| ID | Account | Pack | Maps to journeys |
|----|---------|------|------------------|
| **S4-lisbon-group-planning** | `mara@dogfood.local` + dao/reza/elif | `lisbon-phase1` | **Wedge J02 + J05** |
| S2-elif-rome-return | elif + Sarah/Mike | `elif-rome` | Active return planning |
| S1-elif-mature-archive | elif | All 6 packs | Cross-city Atlas/Discover |
| S3-elif-istanbul-return | elif | `istanbul-phase1` | Pending second-visit loop |
| S5-elif-tokyo-kept-memory | elif | `tokyo-phase1` | Kept past trip memory |
| S6-elif-brooklyn-baseline | elif | `brooklyn-phase1` | Local baseline (W1 only) |

**S4 is the backend-real counterpart to the wedge** — Mara organizing Lisbon with group members and private constraints.

### Backend-real packs (`packs.yaml`)

| Pack ID | City | Personas | Readiness |
|---------|------|----------|-----------|
| `lisbon-phase1` | Lisbon | mara, dao, reza, elif | W2_local |
| `elif-rome` | Rome | elif, sarah, mike | W2_local |
| `tokyo-phase1` | Tokyo | elif, sarah | backend_parity_local |
| `istanbul-phase1` | Istanbul | elif, sarah, mike | W2_local |
| `brooklyn-phase1` | Brooklyn | elif | W1_local |
| `elif-canonical-profile` | cross-city | elif | profile_consolidation |

All packs list `app_qa_status: not_run` as of investigation date.

### Hydration pipeline (backend world)

```text
Authoring (Cursor-assisted YAML/docs)
  → validate manifests (tools/dogfood/content/validate)
  → bootstrap_users.py (@dogfood.local)
  → import_staged_refs (venues from tools/seed/staging/)
  → seed.py (trips, itineraries, memories, atlas, expenses, photos)
  → optional media upload → /dogfood-media static mount
  → app reads via normal APIs
```

**Canonical local sequence:**

```bash
cd travel-agent
PYTHONPATH=. python -m tools.dogfood.content.validate
PYTHONPATH=. python -m tools.dogfood.content.bootstrap_users --apply
PYTHONPATH=. python -m tools.dogfood.content.import_staged_refs manifests/lisbon-phase1.yaml --apply
PYTHONPATH=. python -m tools.dogfood.content.seed manifests/lisbon-phase1.yaml --apply
python scripts/dogfood_audit.py --summary --persona mara@dogfood.local
```

**Fly promotion (prod-data op):**

```bash
# Requires --allow-prod and cohort guards
PYTHONPATH=. python -m tools.dogfood.content.bootstrap_users --apply --allow-prod
PYTHONPATH=. python -m tools.dogfood.content.seed manifests/lisbon-phase1.yaml --apply --allow-prod
```

### Frontend mock personas (12)

From `travel-app/constants/personas/index.ts`:

| ID | Scenario | Backend `@dogfood.local`? |
|----|----------|---------------------------|
| `default` | M0-default-fixture | No |
| `ana` | M1-ana-cold-start | No (P1 promotion target) |
| `ben` | M2-ben-loose-planning | No |
| `carmen` | M3-carmen-live-trip | No (P0 promotion target; skeleton only) |
| `dev` | M4-dev-just-returned | No (P1 promotion target) |
| `ready` | M5-ready-leaving-soon | No |
| `urgent` | M6-urgent-open-decision | No (used in Maestro flow 25) |
| `between` | M7-between-trips | No |
| `nadia` | M8-nadia-archive | No |
| `omar` | M9-omar-fresh-find | No |
| `torture` | M10-torture-edge | No |
| `elif` | M11-elif-frequent-traveler | **Yes** — `elif@dogfood.local` |
| `mara` | M12-mara-lisbon-group (S4 wedge) | **Yes** — `mara@dogfood.local` |

**Backend-only dogfood users (no dedicated frontend persona file):**

- `dao@dogfood.local`, `reza@dogfood.local` — S4 companions (seeded via `lisbon-phase1.yaml`)
- `sarah@dogfood.local`, `mike@dogfood.local` — Elif companions

**S4 alignment (2026-06-28):** `constants/personas/mara.ts` + `make seed-s4-local` seed the same Lisbon group world for mock-walk, logic QA, and Maestro wedge flows.

**Other legacy seed paths:** `scripts/seed_brooklyn_demo.py` (eval demo, separate from manifest); thin `tools/dogfood/seed_*_offline.py` wrappers. **Retired:** `scripts/seed_group_trip.py` — use `make seed-s4-local` instead.

**Canonical seeder:** `tools/dogfood/content/seed.py` — idempotent, cohort-scoped, `_dogfood` metadata on all rows.

### AI spend control for dogfood sessions

```bash
# travel-agent/scripts/dogfood_ai_safe_mode.sh
AI_MODE=replay
WEB_SEARCH_MODE=off
DISABLE_LLM_BACKGROUND_LOOPS=true
ATLAS_LLM_ENABLED=false
# etc.
```

---

## QA certification stack

### Four layers (intentional split)

| Layer | Question | Tooling | Status (2026-06-28) |
|-------|----------|---------|----------------------|
| **Static trace** | Do routes, contracts, docs align? | Journey docs + AI trace prompts | 12/12 ✅ |
| **Logic QA** | Did the backend do the right thing? | `npm run qa:logic` → `tests/scenarios/test_j*.py` | 12/12 ✅ (CI: `travel-app` `logic-qa` job + agent `test-db` scenarios step) |
| **Mock-walk** | Does the frontend contract + render hold? | `__tests__/journeys/*.test.ts(x)` | 12/12 ✅ |
| **Visual QA** | Does it look and navigate right on device? | Maestro + `qa:polish` | Wedge 🔶 pending |

**Certification formula** (from `docs/working/journey-certification-suite.md`):

```
logic: PASS + visual: PASS = journey CERTIFIED
```

None of the 12 are certified yet.

### Layer A: Logic QA

**Runner:** `travel-app/scripts/logic-qa/run-logic-qa.mjs` (spawns backend pytest)

**Mapping:** 1:1 with journeys via `scripts/logic-qa/scenarios.mjs`:

| Journey | Backend test file |
|---------|-------------------|
| J01 | `tests/scenarios/test_j01_vague_idea_to_trip.py` |
| J02 | `tests/scenarios/test_j02_invite_acceptance.py` |
| J03 | `tests/scenarios/test_j03_cold_trip_setup.py` |
| J04 | `tests/scenarios/test_j04_private_constraint.py` |
| J05 | `tests/scenarios/test_j05_proposal_plan_mutation.py`, `test_j05_plan_edit_commit.py` |
| J06 | `tests/scenarios/test_j06_home_plan_map_changes_coherence.py` |
| J07 | `tests/scenarios/test_j07_discover_context_to_trip_action.py` |
| J08 | `tests/scenarios/test_j08_live_trip_what_now.py` |
| J09 | `tests/scenarios/test_j09_notifications_proactive_routing.py` |
| J10 | `tests/scenarios/test_j10_booking_stay_expense_trust_loop.py` |
| J11 | `tests/scenarios/test_j11_atlas_candidate_memory_control.py` |
| J12 | `tests/scenarios/test_j12_returned_trip_closeout.py` |

**Wedge E2E:** **Retired 2026-06-28.** Unique plan-edit cases live in `test_j05_plan_edit_commit.py`; proposal lifecycle in `test_j05_proposal_plan_mutation.py`.

**CI:** Agent `test-db` job runs all `requires_postgres` tests including `tests/scenarios/`. App `logic-qa` job runs `npm run qa:logic -- --no-write` against a sibling checkout of travel-agent.

### Layer B: Mock-walk Jest (consolidated)

**Location:** `travel-app/__tests__/journeys/` (88 tests, `--runInBand` in CI)

**Wedge journeys:**

| File | Journey | Notes |
|------|---------|-------|
| `journey-02-mock-walk.smoke.test.tsx` | J02 | Merged create+invite data walk + smoke |
| `05-group-planning-proposal-mutation.test.ts` | J05 | 11 data-layer cases |
| `journey-05-mock-walk.smoke.test.tsx` | J05 | Render smoke |
| `06-cross-surface-coherence.test.ts` | J06 | 8 data-layer cases |
| `journey-06-mock-walk.smoke.test.tsx` | J06 | Render smoke |

**Removed duplicates (2026-06-28):** `02-create-trip-and-invite.test.ts`, redundant `journey-06-mock-walk.smoke.test.tsx` subset.

### Layer C: Maestro visual (62 flows)

**Wedge flows** (DoD point 4):

| Flow | Journey | Notes |
|------|---------|-------|
| `.maestro/24-journey-02-create-invite.yaml` | J02 | Dev build mock mode; uses seeded `trip-lisbon-26` |
| `.maestro/25-journey-05-proposal-mutation.yaml` | J05 | Switches to `urgent` persona for Porto vote |

**Run recipe:**

```bash
export JAVA_HOME=/opt/homebrew/opt/openjdk
export PATH="$JAVA_HOME/bin:$HOME/.maestro/bin:$PATH"
npx expo start --dev-client   # leave running
maestro test .maestro/24-journey-02-create-invite.yaml
maestro test .maestro/25-journey-05-proposal-mutation.yaml
```

**Maestro inventory:**

| Bucket | Count | Purpose |
|--------|-------|---------|
| Root `01`–`25` | 25 | Smoke / visual-qa lane |
| `polish/` | 28 | Screenshot certification (cropOn, personas) |
| `baselines/` | 3 | Baseline captures |
| `animation/` | 1 | Animation QA |
| `audit-vesper-*` | 5 | One-off design audits |
| `config.yaml` | 1 | Workspace config |

**`npm run visual-qa`** runs entire `.maestro/` tree — pulls polish + audit into smoke (avoid bare usage).

### Layer D: Elif dogfood polish lane

**`npm run qa:dogfood:elif`** → 9 surfaces via `scripts/polish-qa/run-elif-dogfood-qa.mjs`:

trips-home, single-trip-home, single-trip-interactions, trip-stay, trip-costs, vesper-home, discover-home, discover-compose, atlas-home

Visual fidelity for Elif canonical persona — **orthogonal to wedge J02/J05 certification** (different scenario: M11 vs S4).

### Layer E: Legacy golden paths

**`docs/reliability/Golden Paths.md`** — 6 MVP paths mapping to journeys J02, J04, J05, J06, J09, J11+J12.

**`scripts/golden-path-qa.sh`** runs old anchor files — **not** `__tests__/journeys/`:

- Backend: `test_home.py`, `test_proposals_api.py`, eval checks, etc.
- Frontend: `goldenPath.test.ts`, `plan.smoke.test.tsx`, `map.smoke.test.tsx`

**Parallel vocabulary** — should be demoted to pointer at journey docs.

### Reliability ladder (workspace)

Cheapest first:

1. `make doctor` (includes Postgres / DATABASE_URL alignment)
2. `make contract-check`
3. `make mock-real-parity` ← green (itinerary ref removed 2026-06-28)
4. `make golden-path-qa` ← wedge J02/J05/J06 scenario + Jest
5. `make offline-qa` ← green (includes journey Jest + backend pytest)
6. `make certify-fast` / `certify-logic` / `certify-visual` ← certify ladder
7. Manual live canary (5 scenarios per release)

### CI coverage map

| Check | travel-app PR | travel-agent PR | workspace post-merge |
|-------|---------------|-----------------|----------------------|
| Full Jest (incl. journeys) | ✅ | — | — |
| tsc + contract-types | ✅ | — | contract-check |
| Agent offline pytest | — | ✅ | offline-qa (partial) |
| `tests/scenarios/` | — | ✅ test-db | certify-logic |
| Logic QA npm wrapper | ✅ logic-qa job | — | certify-logic |
| Maestro wedge (24/25) | — | — | `make certify-visual` (local) |
| `test:offline` | ✅ subset | — | offline-qa |

---

## How lanes interact

### For the wedge journey specifically

| Step | Lane used | Proves | Doesn't prove |
|------|-----------|--------|---------------|
| Logic QA J02/J05/J06 | Local backend + Postgres | Server invariants, membership, proposal atomicity | FE wiring, Clerk, share sheet |
| Mock-walk 02/05/06 | Frontend mock | API contract, render, block-id parity | Real network, real auth |
| Maestro 24/25 | Frontend mock + dev build | Routes render, selectors work | Clerk detour, OS share, Fly data |
| S4 substrate seed | Backend-real | Mara Lisbon group world on Postgres | That Fly has this data |
| EAS dogfood build | Live Fly + Clerk | Real user experience | Nothing until someone walks it |

### Mock fidelity gaps — current state

Source: wedge doc (2026-06-27) cross-checked against code (2026-06-28).

#### Closed since wedge doc was written

| Gap | Evidence |
|-----|----------|
| `getTripMembers` not reading `addTripMember` / `acceptInvite` | `mock/trips.ts` layers `_addedTripMembers`; `mock/social.ts` writes on accept. Closed in J02 mock-walk. |
| `viewInvite` can't see `createTrip` trips | `mock/social.ts` searches `_createdTrips`. Documented closed in same file. |
| Folio spine diverges from Plan/Map | `getTripFolio → _getMockItinerarySync`. Documented closed in `06-cross-surface-coherence.test.ts` header. |

**Action:** Update `docs/working/wedge-journey-02-05-path-to-dogfood.md` §"Mock-layer fidelity gaps" to remove closed items.

#### Still mock-blind (fixable in mock once)

| Gap | File | Fix effort | Status |
|-----|------|------------|--------|
| ~~`getActionReceipt` always `{ receipt: null }`~~ | ~~`mock/social.ts`~~ | — | **Closed 2026-06-28** — `trips.ts` derives from `recent_changes` |
| ~~`postEditCommit` no `expected_updated_at` 409~~ | ~~`mock/profile.ts`~~ | — | **Closed 2026-06-28** — throws 409 on stale stamp |
| ~~`postEditCommit` no idempotency token cache~~ | ~~`mock/profile.ts`~~ | — | **Closed 2026-06-28** — `_mockEditCommitCache` |
| Plan mutation keyed on global `MOCK_PROPOSAL_A` only | `mock/trips.ts`, `mock/state.ts` | Medium — per-trip ledger | **Closed 2026-06-28** — `_ledgerProposalIdForTrip` |

#### Requires live walk forever

| Invariant | Why |
|-----------|-----|
| Clerk two-account invite (DoD 5) | Auth + real invite tokens across devices |
| FE rendering of receipt / 409 / double-apply | Backend certifies logic; mock doesn't prove UI wiring |
| EAS dogfood vs local mock | Dogfood build has `USE_MOCK=false` — personas invisible |
| Real group-safe synthesis (I4) | Needs live `group_compose.py` path |

### Scenario matrix ↔ journey mapping

| Journey | Mock scenario | Backend scenario | QA coverage |
|---------|---------------|------------------|-------------|
| J02 Create+Invite | M0 default + mock walks | **S4** (mara Lisbon group) | Logic ✅ Mock ✅ Maestro 🔶 |
| J05 Proposal→Plan | `urgent` in Maestro 25 | **S4** | Logic ✅ Mock ✅ Maestro 🔶 |
| J06 Coherence | `06-cross-surface-coherence.test.ts` | S4 itinerary rows | Logic ✅ Mock ✅ |
| J01 Cold start | **M1 ana** (mock only) | No backend-real yet | Logic ✅ Mock ✅ |
| Elif surfaces | `elif.ts` (M11) | **S1–S3, S5–S6** | Polish QA lane only |

---

## Build profiles & environments

From `travel-app/eas.json`:

| Profile | `USE_MOCK` | Auth | API | QA lanes |
|---------|------------|------|-----|----------|
| **development** | true | skipped | mockApi | Maestro, mock-walk, polish-qa, persona switcher |
| **dogfood** | false | Clerk | Fly.dev | Live walk, TestFlight |
| preview | false | Clerk | Fly.dev | Internal preview |
| production | false | Clerk | Fly.dev | External users |

### Environment table (canonical)

From `Environments Dogfood and Data Substrate.md`:

| Name | API target | Auth/mock | Meaning |
|------|------------|-----------|---------|
| Local mock dev | none | mock on, auth skipped | Cheapest UI loop; no backend truth |
| Local real dev | local backend | SKIP_AUTH=true | API wiring, schema drift, local seed |
| Local dogfood | local backend + fixture data | SKIP_AUTH, loops off | Product-feel without prod data |
| EAS development | mock by default | mock on, auth skipped | Simulator dev client; Maestro |
| EAS dogfood | Fly.dev | mock off, auth on | Internal device build at shared backend |
| Fly `vesper-backend` | itself | Clerk/prod | Shared backend for all client lanes |

### Dev tooling surfaces

| Tool | Path | Purpose |
|------|------|---------|
| DevFab | `components/dev/DevFab.tsx` | Floating overlay: mock toggle, force offline, persona nav |
| persona-switcher | `app/dev/persona-switcher.tsx` | Persona pick, time-travel clock, force-state (duplicates DevFab) |
| force-state | `app/dev/force-state.tsx` | `guide://dev/force-state?...` for Maestro |
| screenshot-mode | `app/dev/screenshot-mode.tsx` | `guide://dev/screenshot-mode?persona=X&to=...` — no JS reload |

**Dogfood build DevFab:** reduced — real account shown, force-offline only; persona switching disabled unless runtime mock toggle on.

### OpenAPI sync — single artifact, multiple entrypoints

**Canonical:** `docs/openapi.json` (workspace root)

| Entry point | Mode | Risk |
|-------------|------|------|
| `./scripts/sync-types.sh` | offline (default) | **Canonical** — snapshot + `schema.gen.ts` + tsc |
| `make export-openapi` (travel-agent) | offline | Same exporter, no TS step |
| `npm run generate-api-types` | **live curl only** | Footgun — bypasses committed snapshot |
| `npm run generate-api-types:snapshot` | reads `../docs/openapi.json` | Correct for app-only regen |
| `make contract-check` | diff check | workspace CI |

**Recommendation:** Deprecate live-only `generate-api-types`; document `make sync-types` as sole workflow.

---

## Streamlining audit — what's broken

Verified in code as of 2026-06-28.

### P0-1: `test:offline` references missing file — **RESOLVED 2026-06-28**

Removed stale `__tests__/data/itinerary.test.ts` from `travel-app/package.json` `test:offline` and from `scripts/mock-real-parity.sh`. `npm run test:offline` and `make mock-real-parity` are green again.

### P0-2: Logic QA runner — **RESOLVED 2026-06-28**

Committed runner: `travel-app/scripts/logic-qa/run-logic-qa.mjs` + `scenarios.mjs`; `package.json` ships `qa:logic`, `qa:logic:ci`, `qa:logic:list`. Workspace `make certify-logic` wraps agent scenario pytest.

**CI wired:** `travel-app/.github/workflows/ci.yml` `logic-qa` job (Postgres service + `npm run qa:logic -- --no-write`); `travel-agent/.github/workflows/ci.yml` `test-db` job runs `pytest tests/scenarios/ -m requires_postgres`.

### P0-3: Wedge doc lists closed mock gaps — **RESOLVED 2026-06-28**

`docs/working/wedge-journey-02-05-path-to-dogfood.md` §"Mock-layer fidelity gaps" trimmed; all original wedge mock gaps (receipt, 409/idempotency, per-trip proposal ledger) marked closed in code.

---

## Streamlining audit — duplication to collapse

### J02/J05/J06 tested multiple ways — **partially collapsed 2026-06-28**

| Journey | Data walk | Smoke | Backend scenario | Maestro | Wedge E2E |
|---------|-----------|-------|------------------|---------|-----------|
| J02 | merged into smoke | ✅ | ✅ | Flow 24 | — (retired) |
| J05 | ✅ | ✅ | ✅ (+ plan-edit) | Flow 25 | — (retired → J05 scenarios) |
| J06 | ✅ | ✅ | ✅ | partial in 25 | — |

**Done:** J02 duplicate Jest removed; wedge E2E retired; `test_j05_plan_edit_commit.py` holds I7/I8.

**Remaining:** Maestro consolidation (~15–20 flows); optional further J05/J06 smoke merge.

### Golden Paths vs Journeys — two parallel lists

`golden-path-qa.sh` now runs wedge journey scenario pytest (J02/J05/J06) + matching journey Jest files. Full journey Jest suite runs in workspace `reliability.yml` and `make certify-fast`.

**Recommendation:** `docs/journeys/STATUS.md` as sole index; update `golden-path-qa.sh` to run scenario pytest + journey Jest for same IDs.

### Maestro overlap (~15–20 flows consolidatable)

| Overlap | Recommendation |
|---------|----------------|
| `02-trip-home` vs `polish/single-trip-home` | Keep polish; demote root `02` |
| `12` vs `polish/trips-home-returned` | Keep polish |
| `15`–`21` (7 hero variants) | Collapse to 4-state polish surface |
| `audit-vesper-*` (5) | Archive if polish vesper covers |
| `24`/`25` vs polish interaction flows | One owner, not both |
| `npm run visual-qa` bare | Split: smoke vs polish explicit lists |

### Logic QA runner in wrong repo

`travel-app/scripts/logic-qa/` spawns `pytest` in `travel-agent`.

**Recommendation:** `make journey-logic-qa` in travel-agent; workspace `make certify-logic` wrapper.

### Seven QA commands today (no single entry point)

```
make offline-qa          # green (itinerary ref fixed)
make golden-path-qa      # wedge J02/J05/J06 scenario + Jest
make mock-real-parity    # green (itinerary ref removed)
make certify-fast        # contract + journey Jest + offline backend pytest
make certify-logic       # scenario pytest (needs local vesper Postgres)
npm test                 # full Jest
npm run test:offline     # focused offline subset (58 tests)
npm run qa:logic         # local logic QA (also in CI)
npm run qa:polish        # visual
maestro test .maestro    # runs everything
```

---

## Streamlining audit — substrate friction

### Dual Elif worlds

| | Frontend M11 | Backend S1–S6 |
|--|--------------|-----------------|
| File | `elif.ts` (~1.3k lines) | manifests + `@dogfood.local` |
| Used by | Polish QA, Maestro, switcher | Seed pipeline, backend dogfood |
| scenarios.yaml | `mock_only` | `backend_real_local` |

Polish QA is M11-heavy; backend dogfood is S*. Visual QA never exercises backend-real substrate.

**Recommendation:** Add more S*-aligned personas as needed; stop expanding `elif.ts`; long-term manifest → PersonaBundle codegen.

### ~~No Mara frontend persona for wedge~~ — **RESOLVED 2026-06-28**

`constants/personas/mara.ts` + `M12-mara-lisbon-group` in `scenarios.yaml` / polish-qa surfaces.

### ~~Legacy `seed_group_trip.py` identity drift~~ — **RESOLVED 2026-06-28**

Deleted. Use `make seed-s4-local` (`scripts/seed-s4-local.sh` + `lisbon-phase1.yaml`).

### Triple scenario documentation

1. `scenarios.yaml` (machine)
2. `Dogfood Scenario Matrix.md` (human mirror)
3. `polish-qa/validate-scenario-ids.mjs` (parses YAML)

**Recommendation:** YAML sole source; generate Matrix or stop manual sync.

### `tests/dogfood/` is NOT redundant with journeys

25 files — ops/replay/canary harness. Keep separate; optionally tag canaries with journey IDs in comments.

---

## Proposed single certify ladder

Replace fragmented commands with explicit tiers:

```bash
# Tier 1 — Daily / PR (fast, no Postgres, no device)
make certify-fast
  → make contract-check
  → cd travel-app && npm test -- __tests__/journeys/
  → make test-backend  # agent offline pytest

# Tier 2 — Pre-merge (needs Postgres)
make certify-logic
  → cd travel-agent && pytest tests/scenarios/ -m requires_postgres -q

# Tier 3 — Pre-TestFlight (needs simulator + Metro)
make certify-visual
  → maestro test .maestro/24-journey-02-create-invite.yaml
  → maestro test .maestro/25-journey-05-proposal-mutation.yaml

# Tier 4 — Dogfood session (human)
make certify-live
  → seed S4 (lisbon-phase1) locally OR --allow-prod to Fly
  → scripts/dogfood_ai_safe_mode.sh
  → two-account walk: I1–I10 checklist
  → dark feature sweep
  → one external TestFlight friend
```

### Extended STATUS.md columns

Add to `docs/journeys/STATUS.md`:

| Journey | Static | Mock-walk | Logic | Maestro | Live | Certified |

Replace parallel claims in Golden Paths, wedge DoD, certification suite.

### Wedge operating sequence (unchanged intent, clarified tooling)

1. ✅ Mock-walk J02/J05/J06
2. ✅ Logic QA J02/J05/J06 (+ backend wedge E2E)
3. 🔶 Maestro 24/25 green on dev build
4. Seed S4 to target environment (local then Fly)
5. Live two-account walk on EAS dogfood build
6. Dark sweep + external friend

---

## What to stop doing

| Stop | Why |
|------|-----|
| Treating `offline-qa` green as full certify | Use `certify-logic` / `certify-visual` for Postgres + device gates |
| Maintaining Golden Paths as separate journey set | Duplicates J02/J04/J05/J06/J09/J11–J12 |
| Running `visual-qa` (full tree) as smoke | Mixes polish + audit; slow, redundant |
| Using `npm run generate-api-types` (live curl) | Drifts from committed snapshot |
| Expanding mock personas before backend promotion | 12 mocks; Elif + Mara have backend parity paths |
| Re-fixing wedge mock gaps from stale doc | GAP 1, 2, Folio spine closed in code |
| Building more substrate packs before S4 on Fly | Wedge DoD 5–8 need one backend-real world |
| Starting new product substrate | Wedge doc: wait until slice dogfood-ready |

### When to split dogfood backend (don't yet)

Create `vesper-backend-dogfood` only when:

- Destructive reset/seed flows needed often
- External testers on dogfood data
- Real production users exist and dogfood could pollute analytics

Until then: shared backend + cohort boundaries + `dogfood_audit.py`.

---

## Prioritized action list

| Priority | Action | Impact | Effort |
|----------|--------|--------|--------|
| **P0** | Run Maestro flows 24/25 (`make certify-visual`) | Closes wedge DoD gate 4 | ~1 hr (+ Java/simulator) |
| **P0** | Seed S4 to Fly with documented bootstrap | Closes mock/Fly world gap for live walk | ~2 hr |
| **P1** | Live two-account walk on Fly (DoD 5/6) | First real external-ready proof | ~4 hr |
| **P2** | Maestro flow consolidation (−15–20 flows) | Maintenance reduction | ongoing |
| **P2** | Split Maestro smoke vs polish npm scripts | Faster runs | ~1 hr |
| **P3** | Manifest → PersonaBundle codegen | Long-term mock/backend unity | project |

### Completed 2026-06-28 (Stream A/B/D)

| Action | Status |
|--------|--------|
| Fix `itinerary.test.ts` refs | ✅ |
| Wire logic-qa + certify ladder | ✅ |
| Merge J02/J05/J06 duplicate Jest | ✅ |
| Retire wedge E2E → `test_j05_plan_edit_commit.py` | ✅ |
| Delete `seed_group_trip.py`; add `make seed-s4-local` | ✅ |
| Add `mara.ts` + S4 mock fidelity | ✅ |
| Mock stubs (receipt, 409, idempotency, per-trip ledger) | ✅ |
| `make dogfood-status` | ✅ |
| Align docker-compose + doctor Postgres story | ✅ |

---

## Key file index

### Product & journeys

| Topic | Path |
|-------|------|
| Journey status matrix | `docs/journeys/STATUS.md` |
| Wedge path to dogfood | `docs/working/wedge-journey-02-05-path-to-dogfood.md` |
| Journey certification spec | `docs/working/journey-certification-suite.md` |
| System charters index | `docs/systems/README.md` |
| Product thesis | `travel-agent/docs/product/Product Thesis.md` |
| Feature map | `travel-agent/docs/Feature-Map.md` |
| Prior progress investigation | `docs/working/codebase-progress-investigation-2026-06-21.md` |

### Substrate & dogfood

| Topic | Path |
|-------|------|
| Environments canonical doc | `travel-agent/docs/operations/Environments Dogfood and Data Substrate.md` |
| Scenario registry | `travel-agent/tools/dogfood/content/scenarios.yaml` |
| Pack registry | `travel-agent/tools/dogfood/content/packs.yaml` |
| Manifests | `travel-agent/tools/dogfood/content/manifests/` |
| Canonical seeder | `travel-agent/tools/dogfood/content/seed.py` |
| Bootstrap users | `travel-agent/tools/dogfood/content/bootstrap_users.py` |
| Legacy group seed | **Deleted** — use `tools/dogfood/content/seed.py` + `lisbon-phase1.yaml` |
| Dogfood audit | `travel-agent/scripts/dogfood_audit.py` |
| AI safe mode | `travel-agent/scripts/dogfood_ai_safe_mode.sh` |

### QA tooling

| Topic | Path |
|-------|------|
| Journey mock-walk tests | `travel-app/__tests__/journeys/` |
| Logic QA runner | `travel-app/scripts/logic-qa/run-logic-qa.mjs` |
| Logic QA scenarios map | `travel-app/scripts/logic-qa/scenarios.mjs` |
| Polish QA runner | `travel-app/scripts/polish-qa/run-polish-qa.mjs` |
| Elif dogfood QA lane | `travel-app/scripts/polish-qa/run-elif-dogfood-qa.mjs` |
| Maestro wedge flows | `travel-app/.maestro/24-journey-02-create-invite.yaml`, `25-journey-05-proposal-mutation.yaml` |
| Backend journey scenarios | `travel-agent/tests/scenarios/test_j*.py` |
| Wedge E2E | **Retired 2026-06-28** — I7/I8 plan-edit ported to `tests/scenarios/test_j05_plan_edit_commit.py`; remainder covered by J05 scenarios |
| Golden path script (legacy) | `scripts/golden-path-qa.sh` |
| Offline QA ladder | `scripts/offline-qa.sh` |
| Mock/real parity | `scripts/mock-real-parity.sh` (green) |

### Frontend mock & dev

| Topic | Path |
|-------|------|
| Persona registry | `travel-app/constants/personas/index.ts` |
| Mock API | `travel-app/utils/api/mock/` |
| EAS build profiles | `travel-app/eas.json` |
| DevFab | `travel-app/components/dev/DevFab.tsx` |
| Persona switcher | `travel-app/app/dev/persona-switcher.tsx` |
| Screenshot mode | `travel-app/app/dev/screenshot-mode.tsx` |

### Workspace

| Topic | Path |
|-------|------|
| Makefile | `Makefile` |
| OpenAPI snapshot | `docs/openapi.json` |
| Sync types | `scripts/sync-types.sh` |
| Contract check | `scripts/contract-check.sh` |
| CI reliability | `.github/workflows/reliability.yml` |

---

## Evidence & verification notes

Investigation performed 2026-06-28 with:

- Git log aggregation across `travel-agent`, `travel-app`, workspace (Apr 12 – Jun 28)
- Read of system charters, journey STATUS, wedge doc, certification suite, environments doc
- Code verification of mock fidelity gap claims (`journey-02-mock-walk.smoke.test.tsx`, `06-cross-surface-coherence.test.ts`, `mock/social.ts`, `mock/trips.ts`)
- Glob confirming `itinerary.test.ts` absence
- `git ls-files` confirming logic-qa now committed (was uncommitted at the original investigation snapshot)
- Maestro flow count: 62 YAML files under `.maestro/`
- OpenAPI counts from `docs/openapi.json`: 310 paths, 345 operations, 588 schemas

### Related agent investigations (session reference)

Subagent explorations informed this document:

- Codebase progress & docs inventory (workspace `docs/`)
- Travel Agent backend architecture
- Travel App frontend structure
- Dogfood substrate backend tooling
- Frontend QA and mock flows
- QA redundancy audit
- Substrate/persona duplication audit

---

## Bottom line

**Product:** In 11 weeks, Vesper went from zero to a place-aware travel concierge with sharp thesis, 142 tables, 63 routers, 5 agents, four polished surfaces, 14 system charters, and 12 canonical journeys. Against vision: strong on architecture and breadth; gap is proof, not construction.

**Dogfood:** Wedge (J02→J05) backend + mock layers are certified; S4 seeds locally via `make seed-s4-local`. Remaining gates: Maestro 24/25, Fly seed, live two-account walk, one TestFlight friend.

**QA system:** Certify ladder landed; wedge duplicates retired. Next: device visual gate, then collapse Maestro overlap.

**Next human action:** Install Java if needed → `make certify-visual` → seed S4 to Fly → two-account live walk → one TestFlight friend.
