---
doc_type: archive
status: archived
owner: engineering
created: 2026-06-29
archived: 2026-08-10
why_new: Preserves the June 2026 dogfood and latent-corpus certification narrative removed from Journey Status so that document carries current evidence only.
supersedes: []
---

# Journey Status — June 2026 certification narrative (archived 2026-08-10)

Historical evidence moved out of `docs/journeys/STATUS.md` so that document
carries current certification only. Dogfood five-pack gates, Tier A/B latent
corpus tables, the Phase 3 decommission note, and the optional EAS spot-check
below were all recorded 2026-06-29 and are **not** current evidence. Current
truth: `docs/journeys/STATUS.md` and `docs/journeys/evidence-attestations.json`.

## Dogfood five-pack certification

**Primary gate (agent-owned):** substrate + live API on Fly Postgres.

| Gate | Command | Status |
|------|---------|--------|
| Substrate (DB + offline compose) | `make dogfood-five-pack-verify PROFILE=fly` | **PASSED** 2026-06-29 |
| Fly smoke (API + personas + Rome bridge) | `make dogfood-fly-smoke` | **PASSED** 2026-06-29 |
| Five-pack certification (agent-owned) | `make dogfood-five-pack-verify PROFILE=fly` + `make dogfood-five-pack-simulator` | **COMPLETE** 2026-06-29 |
| Live HTTP (Fly + Clerk) | `CLERK_SECRET_KEY=… TRANSPORT=http make dogfood-journey-live-api PROFILE=fly` | **automation complete** — TestClient 16/16 green; the HTTP runner now creates short-lived sessions for the linked dogfood accounts, passes their JWTs only to the certification child process, and revokes the sessions afterward. A supplied `PRELAUNCH_JWT_MARA` / `PRELAUNCH_JWT_DAO` still takes precedence. Running against Fly remains an operator credential lane. |

**Note (updated 2026-07-19):** automated HTTP certification and physical-device certification are separate lanes. The latter still runs J04/J05/J10 on **real Clerk accounts on two physical devices** (see [journey-live-full-cert-04-05-10.md](../working/journey-live-full-cert-04-05-10.md) and [dogfood-loop-validation-2026-07-04.md](../working/dogfood-loop-validation-2026-07-04.md)); it requires an operator to complete the real sign-in/OTP flow.

| Pack | Fly promote | Substrate ✅ | Live API (local) | Optional UI spot-check |
|------|-------------|--------------|------------------|-------------------------|
| Lisbon | ✅ | ✅ | ✅ TestClient + Maestro wedge | EAS pixels / place art |
| Rome | ✅ | ✅ | ✅ TestClient | EAS Clerk channel |
| Istanbul | ✅ | ✅ | ✅ TestClient | optional |
| Tokyo | ✅ | ✅ | ✅ TestClient | optional |
| Brooklyn | ✅ | ✅ | ✅ TestClient | optional |

**Optional human spot-check** (EAS build — Clerk + pixels only): see the optional five-city section in [journey-live-full-cert-04-05-10.md](../working/journey-live-full-cert-04-05-10.md). Not required when automated gates above are green.

**Tier A Fly promote + spot-check (2026-06-29):** `APPLY=1 PROFILE=fly make import-latent-corpus` complete; `make tier-a-spot-check PROFILE=fly` — **PASSED** all 5 cities (Paris, Barcelona, Venice, Amalfi Coast, Nice).

**Mara atlas (2026-06-29):** `mara-lisbon-group-arrival` artifact seeded local + Fly — `mara@dogfood.local` audit **ready** (was `partial; missing=atlas`).

**S4 companions (2026-06-29):** `dao-lisbon-arrival-reset` + `reza-lisbon-tiles-tram` artifacts, entity saves, affinity — `dao@dogfood.local` and `reza@dogfood.local` audit **ready** (was `partial; missing=taste_affinity, atlas`). J04 device phrase seeded: `dao-quiet-mornings` observation (`shared: false`). Promote: `APPLY=1 PROFILE=fly make dogfood-promote CITY=lisbon`.

**Elif companions (2026-06-29):** `sarah-rome-table-memory` + `mike-rome-classic-beat` in `elif-rome` — personal memories, observations, saves, affinity, atlas. Promote: `APPLY=1 PROFILE=fly make dogfood-promote CITY=rome`.

**Lisbon catalog (2026-06-29):** `confeitaria-nacional-baixa` editorial brief added (`content/staging/lisbon/confeitaria-nacional-baixa.md`); import via `import_cursor_dossiers --file`.

**Lisbon Fly atlas (2026-06-29):** reset + reseed `mara-lisbon-group-arrival` on Fly — map_points now use `confeitaria-nacional-baixa` (not experience-only slug).

**Known catalog gap:** none blocking S4/Lisbon atlas map points (Confeitaria Nacional brief added 2026-06-29).

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

Operator script: [journey-live-full-cert-04-05-10.md](../working/journey-live-full-cert-04-05-10.md)
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
