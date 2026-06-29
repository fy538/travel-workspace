# Journey Status Matrix

> Status: draft
> Owner: founder / engineering
> Last updated: 2026-06-29 (five-pack automated certification; live API + simulator gates)

Evidence: [STATIC_TRACE_PUNCH_LIST.md](STATIC_TRACE_PUNCH_LIST.md) — 2026-06-26 four-agent re-trace of all 12 journeys.
Visual gate: [visual-certification-matrix.md](../../travel-app/docs/logic-qa/visual-certification-matrix.md) pairs screenshots/device checks with the Logic QA journeys.

## Dogfood five-pack certification

**Primary gate (agent-owned):** substrate + live API on Fly Postgres.

| Gate | Command | Status |
|------|---------|--------|
| Substrate (DB + offline compose) | `make dogfood-five-pack-verify PROFILE=fly` | **PASSED** 2026-06-29 |
| Fly smoke (API + personas + Rome bridge) | `make dogfood-fly-smoke` | **PASSED** 2026-06-29 |
| Five-pack certification (agent-owned) | `make dogfood-five-pack-verify PROFILE=fly` + `make dogfood-five-pack-simulator` | **COMPLETE** 2026-06-29 |
| Live HTTP (Fly + Clerk) | `TRANSPORT=http PRELAUNCH_JWT=<jwt> make dogfood-five-pack-live-api` | optional — redundant with Fly DB + TestClient gates |

| Pack | Fly promote | Substrate ✅ | Live API (local) | Optional UI spot-check |
|------|-------------|--------------|------------------|-------------------------|
| Lisbon | ✅ | ✅ | ✅ TestClient + Maestro wedge | EAS pixels / place art |
| Rome | ✅ | ✅ | ✅ TestClient | EAS Clerk channel |
| Istanbul | ✅ | ✅ | ✅ TestClient | optional |
| Tokyo | ✅ | ✅ | ✅ TestClient | optional |
| Brooklyn | ✅ | ✅ | ✅ TestClient | optional |

**Optional human spot-check** (EAS build — Clerk + pixels only): [eas-five-pack-phone-walk-2026-06-29.md](../working/eas-five-pack-phone-walk-2026-06-29.md). Not required when automated gates above are green.

**Tier A Fly promote + spot-check (2026-06-29):** `APPLY=1 PROFILE=fly make import-latent-corpus` complete; `make tier-a-spot-check PROFILE=fly` — **PASSED** all 5 cities (Paris, Barcelona, Venice, Amalfi Coast, Nice).

**Mara atlas (2026-06-29):** `mara-lisbon-group-arrival` artifact seeded local + Fly — `mara@dogfood.local` audit **ready** (was `partial; missing=atlas`).

**Lisbon Fly atlas (2026-06-29):** reset + reseed `mara-lisbon-group-arrival` on Fly — map_points now use `confeitaria-nacional-baixa` (not experience-only slug).

**Known catalog gap:** `confeitaria-nacional-baixa` has a venue row but no editorial brief yet (atlas map point only); does not block certification.

**Lisbon Fly promote fix:** Mara atlas `map_points` no longer references `lisbon-exp-walking-baixa-story` as a venue slug (experience-only ref); full `dogfood-promote CITY=lisbon` unblocked.

## Tier A latent corpus (`proof_only`)

Automated spot-check: `make tier-a-spot-check` — **PASSED** 2026-06-29 (local PG + local Qdrant).  
Fly spot-check: `make tier-a-spot-check PROFILE=fly` — **PASSED** 2026-06-29 (cloud Qdrant + Fly catalog).

| City | Local import | Spot-check | Fly catalog | MOCK_DESTINATIONS |
|------|--------------|------------|-------------|-------------------|
| Paris | ✅ 254 MD | ✅ | ✅ | ✅ |
| Barcelona | ✅ 271 MD | ✅ | ✅ | ✅ |
| Venice | ✅ 310 MD | ✅ | ✅ | ✅ |
| Amalfi Coast | ✅ 214 MD | ✅ | ✅ | ✅ |
| Nice | ✅ 119 MD | ✅ | ✅ | ✅ |

Import: `make import-latent-corpus TIER=a APPLY=1 PROFILE=local` (complete).  
Fly promote: `make import-latent-corpus TIER=a APPLY=1 PROFILE=fly` (complete — catalog + global `place_angles` embed).

## Tier B latent corpus (`proof_only`, 27 cities)

Automated spot-check: `make tier-b-spot-check` — **PASSED** 2026-06-29 (local PG + local Qdrant, all 27 cities).  
Fly spot-check: `make tier-b-spot-check PROFILE=fly` — **PASSED** 2026-06-29 (cloud Qdrant + Fly catalog).

| Stage | Status |
|-------|--------|
| Local import | ✅ ~4k MD dossiers across 27 cities (~2.3h) |
| Local spot-check | ✅ all 27 |
| Fly promote | ✅ (~55m) |
| Fly spot-check | ✅ all 27 |

Import: `make import-latent-corpus TIER=b APPLY=1 PROFILE=local` (complete).  
Fly promote: `make import-latent-corpus TIER=b APPLY=1 PROFILE=fly` (complete).

Cities: athens, bilbao, bologna, bordeaux, cagliari, catania, dubrovnik, florence, genoa, granada, ibiza, lecce, lyon, madrid, malaga, mallorca, marseille, milan, naples, palermo, porto, san-sebastian, seville, split, thessaloniki, valencia, valletta.

## Phase 3 decommission (2026-06-29)

| Item | Status |
|------|--------|
| Golden paths → `journey-wedge-qa` (`golden-path-qa` deprecated alias) | ✅ |
| `seed_group_trip.py` removed; canonical `tools/dogfood/content/seed.py` only | ✅ |
| `seed-s4-fly.sh` deprecated → `dogfood-promote CITY=…` | ✅ |
| Mock slug parity (`make mock-slug-parity`; centralized `destinations.ts` + angles) | ✅ |
| `discover_queries` compose regression (`test_discover_manifest_queries_compose.py`, `AI_MODE=replay`) | ✅ |

## Optional EAS UI spot-check (human)

Operator script: [eas-five-pack-phone-walk-2026-06-29.md](../working/eas-five-pack-phone-walk-2026-06-29.md)  
**Supplement only** — use when validating EAS channel packaging, Clerk login, or Stream E place art. Automated gates above cover data/API.

Preflight: `make dogfood-fly-smoke` — **PASSED** 2026-06-29.

Login (if running): `elif@dogfood.local` / `mara@dogfood.local` · API: `https://vesper-backend.fly.dev`

### Five-pack (optional)

- [ ] **mara Lisbon** — Group taste demo; Discover; Atlas hosted-arrival story
- [ ] **elif Rome** — Rome return planning; Testaccio block
- [ ] **elif Istanbul** — Istanbul second-visit planning
- [ ] **elif Tokyo** — Tokyo counter DNA
- [ ] **elif Brooklyn** — Elif local baseline

### Tier A ad-hoc (optional spot-check on EAS after Fly promote)

- [ ] **Paris** — create ad-hoc trip; search "natural wine bistro"
- [ ] **Barcelona** — ad-hoc trip; search "vermouth bar tapas"
- [ ] **Venice** — ad-hoc trip; search "cicchetti bacaro"
- [ ] **Amalfi Coast** — ad-hoc trip; search "limoncello terrace"
- [ ] **Nice** — ad-hoc trip; search "socca old town"

## Status Legend

| Mark | Meaning |
|---|---|
| `not started` | No journey-specific validation has been run yet. |
| `partial` | Some existing tests/docs cover the journey, but not the full user flow. |
| `blocked` | A known issue prevents credible dogfood validation. |
| `ready` | Good enough for the next promotion step. |
| `required` | Real-backend or live canary needed before dogfood confidence. |
| `optional` | Real-backend pass useful; mock/static can cover most risk. |
| `pending` | Gate exists but not yet run green on device / live. |

## Matrix

| # | Journey | Static | Mock-walk | Logic | Maestro | Live | Certified |
|---|---|---|---|---|---|---|---|
| 01 | [Vague Idea](01-vague-idea-to-vesper-shaped-trip.md) | ready | ready | ready | optional | optional | agent |
| 02 | [Create + Invite](02-concrete-trip-creation-and-invite.md) | ready | ready | ready | ready | optional | agent |
| 03 | [Cold Setup](03-cold-trip-setup-to-useful-workspace.md) | ready | ready | ready | optional | optional | agent |
| 04 | [Private → Group-Safe](04-private-constraint-to-group-safe-plan.md) | ready | ready | ready | optional | required | agent · live pending |
| 05 | [Proposal → Plan](05-group-planning-to-proposal-to-plan-mutation.md) | ready | ready | ready | ready | required | agent · live pending |
| 06 | [Coherence](06-home-plan-map-changes-coherence.md) | ready | ready | ready | ready | optional | agent |
| 07 | [Discover → Vesper](07-discover-to-contextual-vesper-to-trip-action.md) | ready | ready | ready | optional | optional | agent |
| 08 | [Live Companion](08-live-trip-what-now-companion.md) | ready | ready | ready | optional | optional | agent |
| 09 | [Notifications](09-notifications-and-proactive-routing.md) | ready | ready | ready | optional | optional | agent |
| 10 | [Booking / Stay / Expense](10-booking-stay-expense-trust-loop.md) | ready | ready | ready | optional | required | agent · live pending |
| 11 | [Atlas Memory](11-atlas-candidate-to-memory-control.md) | ready | ready | ready | optional | optional | agent |
| 12 | [Post-Trip](12-returned-trip-to-story-memory-settle-up.md) | ready | ready | ready | optional | optional | agent |

**Certified** ladder:

- **`agent`** — static + mock-walk + logic + Maestro (when not `optional`) all green on automated gates.
- **`full`** — `agent` plus live green where the Live column is `required` (none yet; J04/J05/J10 still need two-device live walks).

## Summary

| Metric | Count |
|---|---|
| Static trace ready | 12 / 12 |
| Mock-walk ready | 12 / 12 |
| Logic QA MVP green | 12 / 12 (`J01`–`J12`) |
| Maestro wedge flows (24/25) | **green** 2026-06-29 (`make certify-visual`) |
| Five-pack dogfood (agent gates) | **certified** 2026-06-29 (`dogfood-five-pack-verify` + `dogfood-five-pack-simulator`) |
| Journey agent-certified (12) | **12 / 12** — automated ladder green (mock-walk + logic + Maestro where required) |
| Journey full-certified (12) | **0 / 12** — live two-device gates still open for J04/J05/J10 |

## Certify ladder (workspace)

| Tier | Command | What it runs |
|---|---|---|
| Fast (daily / PR) | `make certify-fast` | `contract-check` → journey Jest → offline backend pytest |
| Logic (pre-merge) | `make certify-logic` | `pytest tests/scenarios/ -m requires_postgres` (J01–J12 + discover manifest compose regression) |
| Visual (wedge) | `make certify-visual` | Maestro 24 + 25 |
| Substrate | `make dogfood-status` | Manifest validate + scenario/pack summary |
| Five-pack DB | `make dogfood-five-pack-verify PROFILE=fly` | Trips, itinerary venues, discover compose (DB) |
| Five-pack live API | `make dogfood-five-pack-live-api` | HTTP routes via TestClient (local) or Fly + JWT |
| Simulator | `make dogfood-five-pack-simulator` | TestClient + optional Maestro 24/25 on real API |
| Tier A catalog | `make tier-a-spot-check` | Local PG + Qdrant search per Tier A city |
| Tier B catalog | `make tier-b-spot-check` | Local/Fly PG + Qdrant search per Tier B city (27) |
| Full offline | `make offline-qa` | doctor, contract, api-coverage, boundaries, backend, journeys, typecheck, test:offline |

Live dogfood (S4 seed + two-account walk) is human/ops — see `docs/working/wedge-journey-02-05-path-to-dogfood.md`.

## Promotion Rules

Unchanged — see [README.md](README.md). **12 / 12** meet agent-certified; **0 / 12** meet full-certified (live pending on J04/J05/J10).
