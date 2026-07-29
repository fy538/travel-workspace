---
doc_type: working
status: active
owner: founder / eng
created: 2026-07-29
expires: 2026-08-28
why_new: Durable backend-real and local-simulator evidence for the Trips Phase 4 Reading.
promotes_to: nothing
supersedes: []
source_of_truth_for:
  - trips-phase-4-reading-backend-canary
---

# Trip Reading backend-real canary — Elif / Rome

**Date:** 2026-07-29  
**Verdict:** PASS — validation layer 3 plus a local iOS simulator HTTP walk  
**Not claimed:** live-provider generation, Clerk auth, EAS build, or layer-4 live dogfood

## Scope

This receipt proves the persisted companion Reading path against an isolated
clone of the local dogfood Postgres database. The shared `vesper` database was
not migrated or written.

- Trip: `7220dcad-7ee1-57bb-bd24-47883a09aa3d`
- Member persona: Elif
- Destination: Rome
- Database clone: `vesper_trip_reading_clone_20260729`
- Schema: `tripreading01` (Alembic head at execution time)
- Source preflight: 24 active group-safe facts, 20 itinerary facts, one open
  decision, three trip members

## Result

1. A deterministic canary Reading was persisted through the real
   `upsert_trip_reading` path using only active, group-safe cited facts from the
   cloned trip.
2. The membership-gated HTTP route returned `200` to Elif. Its public
   projection contained only `destination`, `listen_minutes`, `read_minutes`,
   `sections`, `thread`, `title`, and `trip_id`; internal citations were absent.
3. The iOS 18.2 simulator forced real API mode and fetched
   `GET /api/trips/7220dcad-7ee1-57bb-bd24-47883a09aa3d/reading` from the local
   backend with `200`. It rendered the collapsed card, expanded exact-section
   index, section-targeted reader, and return to Trips.
4. The same HTTP route returned `403 {"detail":"Forbidden"}` when the backend
   actor was changed to a real database user who is not a member of the trip.

The passing Maestro flow is
`Travel App/.maestro/polish/trips-home-reading-backend-real.yaml`.

## Visual evidence

- [Collapsed companion card](trips-home-reading-backend-real-collapsed.png)
- [Expanded section index](trips-home-reading-backend-real-expanded.png)
- [Focused reader](trips-home-reading-backend-real-reader.png)

## Provider boundary

No Anthropic credential was available. A real regeneration attempt failed
closed and persisted no row. The content used for this canary was therefore
explicitly canary-authored, citation-grounded seed content—not represented as a
live-provider output. Live provider generation on an authenticated build remains
a separate layer-4 dogfood receipt.

## Layer-4 release preflight — 2026-07-29

Read-only checks establish the exact next boundary:

- `https://vesper-backend.fly.dev/health` returns `200` and Fly reports both
  application checks passing.
- Fly reports `ANTHROPIC_API_KEY`, `DATABASE_URL`, `CLERK_ISSUER`, and
  `CLERK_JWKS_URL` as deployed secret names; values were not read.
- The deployed OpenAPI returns `200` with 429 operations, but
  `/api/trips/{trip_id}/reading` is absent. A live authenticated Reading walk is
  therefore impossible until the cutover backend lands and deploys.
- The newest finished iOS dogfood build is dated 2026-07-21 and predates the
  companion Reading and Phase 5 commits.
- EAS CLI authentication and the static release-configuration check pass.
- Both registered physical iPhones were offline during preflight. Simulator
  evidence cannot substitute for this layer.
- Backend and app cutover branches are clean and remain strict fast-forwards
  from their local and tracked `main` refs. Their canonical worktrees contain
  unrelated concurrent edits, so the direct-push landing helper was not run.

Layer 4 requires, in order:

1. obtain a clean landing window and land both cutover branches;
2. deploy the backend and verify the Reading operation in live OpenAPI;
3. regenerate the canonical member trip through the real provider and preserve
   the grounding result without exposing citations or private member input;
4. build the current app with the dogfood profile;
5. sign in through Clerk on a physical device as a real trip member;
6. capture collapsed, expanded, section-targeted, and return behavior, plus a
   non-member denial;
7. write a new receipt that names layer 4 explicitly.

No production row, remote branch, Fly deployment, EAS build, or physical device
state was changed by this preflight.
