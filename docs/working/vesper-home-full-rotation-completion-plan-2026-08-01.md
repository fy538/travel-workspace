---
doc_type: working
status: active
owner: founder / product / backend / frontend
created: 2026-08-01
expires: 2026-08-31
why_new: The engine and world-row plans describe the architecture and presentation, but their execution status predates the server-owned rotation, Season/Here catalogs, Duffel Route producer, and Home Airport editor now in the worktree. This plan records the remaining work from today's code to a four-kind, three-row, live-provider dogfood rotation without reopening settled decisions.
promotes_to:
  - travel-agent/backend/home/vesper_workbench/FEATURE.md
  - travel-app/docs/surfaces/vesper-home/contract.md
depends_on:
  - docs/working/vesper-home-engine-implementation-plan-2026-07-30.md
  - docs/working/vesper-home-world-row-presentation-2026-08-01.md
source_of_truth_for:
  - vesper-home-four-kind-rotation-completion
  - vesper-route-live-dogfood-rollout
---

# Vesper Home — four-kind rotation completion plan

## Outcome

Vesper Home presents one homogeneous band at a time and advances through:

```text
sessions → route → season → here → sessions
```

Route, Season, and Here each enter the ring only with three truthful current
rows. Sessions remain honest at one to three rows because an open session is
useful by itself. The server owns eligibility, order, timing, provider spend,
and failover. The app owns only refresh scheduling and the settled transition.

The completion claim requires four layers: static trace, deterministic mock
walk, real-Postgres/provider canary, and reviewed device evidence. Backend and
TypeScript green alone are not a completion claim.

## Current baseline — 2026-08-01

Already implemented in the current worktree:

- Wave-1 envelope, Wave-2 voice, session truth, seam, and generated types;
- durable per-user cursor and opaque-id rotate endpoint;
- ring order `sessions → route → season → here`, six-hour production dwell,
  replay protection, ineligible failover, and app transition;
- two-line world-row presentation, route grid, Dynamic Type-aware density,
  reduced-motion replacement, and one-kind rendering;
- one reviewed Season row and one reviewed New York Here row;
- automatic Duffel Route candidate universe for JFK, exact offer-expiry cache,
  monthly request cap, outbound-only duration/stops projection, and fail-dark
  behavior;
- user-owned canonical `home_airport_iata` backend field and Account editor;
- local migration `vesp_route01` applied; Route locally enabled for JFK with a
  24-request monthly ceiling.

Known gaps:

- Season and Here each have one eligible catalog row, so neither can enter the
  three-row ring;
- no local dogfood user currently has JFK persisted, so no end-to-end Route
  Home response has been produced;
- the current Route producer may spend on an ordinary Home GET, lacks a shared
  refresh lease/negative cache, and can exhaust its cap through repeated empty
  refreshes;
- Route's six-hour cursor dwell can outlive Duffel's offer expiry;
- a screen left open does not schedule a refresh at `rotate_after`; it advances
  only on a later focus/refetch;
- provider/rotation observability from the engine plan is not implemented;
- world-row mock captures exist, but no complete four-kind rotating device run
  or live Route device receipt exists;
- workspace contract-check is presently blocked by unrelated concurrent Places
  schema changes and must be rerun after that lane is synchronized.

## Decisions frozen for this execution

1. **Production ownership:** server-owned, refresh-based rotation. The client
   never names a desired kind or stores a ring index.
2. **Dwell:** Sessions, Season, and Here use six hours. A Route turn ends at
   `min(six hours, earliest displayed supplier-offer expiry)`.
3. **Live search trigger:** ordinary Workbench GETs are cache-only. The server
   may refresh Duffel only when an authenticated due rotation is preparing a
   Route turn, or through an explicit operator canary.
4. **Route discovery V1:** repository-owned, origin-keyed candidate universe;
   no traveler-entered destination and no private-history personalization.
5. **Route spend:** hydrate five automatically selected destinations per Route
   attempt, retain a hard monthly request ceiling, and count/reserve attempts
   durably before network work. No order, hold, payment, or booking calls.
6. **Route freshness:** fare, carrier, stops, duration, observation time, and
   expiry come from the same offer. Expired cache rows never render.
7. **Season semantics:** a global editorial discovery band. Three simultaneous
   reviewed windows may name different destinations; each row retains its place
   label and primary-source provenance.
8. **Here semantics:** exact-place local band. V1 remains New York only and
   needs three overlapping, officially sourced, reliable-end-date windows.
9. **Sessions:** included in the same ring; one to three truthful rows are
   eligible. Dogfood fixtures will supply three to prove equal visual density.
10. **Origin:** explicit `home_airport_iata` only. Never infer it from city,
    coordinates, trip title, or current location.
11. **Interaction:** world rows remain informational in V1. No invented deep
    link, chat seed, or booking action.
12. **QA timing:** an explicitly local/test-only accelerated dwell may exercise
    the full ring. Production defaults and production config cannot use it.

## Execution batches

### Batch 0 — checkpoint and contract isolation

- Preserve the existing unrelated parent Places changes.
- Review and checkpoint only the Vesper files in each child repository.
- Record the current Alembic head and local Route flags without printing the
  Duffel credential.
- Add the Home Airport editor test before relying on it for dogfood.
- Do not regenerate or commit unrelated OpenAPI/Places diffs from this lane.

Exit: Vesper changes are reviewable by explicit filename and neither child
repo contains accidental unrelated staging.

### Batch 1 — harden Route into a safe rotation input

- Split Route into `read_cached` and `refresh_due_turn`; ordinary Home GET is
  cache-only.
- Add a shared Postgres refresh lease keyed by origin + travel window so only
  one worker hydrates a scope.
- Add a short negative-result/error cooldown so insufficient offers or a
  provider failure cannot trigger another search on every paint.
- Reserve and record the exact candidate request count atomically before the
  provider call; keep the monthly ceiling fail-closed.
- Select five candidates deterministically from the origin catalog, rotating
  the subset by search window so the system—not the user—chooses destinations.
- Run provider requests with bounded concurrency and close the HTTP client.
- Preserve each offer's supplier expiry in cache and expose the earliest expiry
  to the rotation decision without adding it to traveler-visible copy.
- Parse day-bearing ISO durations (`P1DT2H`) and retain outbound-only handling
  for round trips.
- Add content-free outcomes: cache hit/miss, lease held, cap reached, request
  count, provider latency/status, valid-offer count, and earliest expiry. Never
  log titles, fares, airport choice tied to user id, or provider payloads.

Exit: repeated GETs spend zero; concurrent due rotations spend once; failed or
thin results cool down; expired offers never render; no booking endpoint is
reachable from this producer.

### Batch 2 — make every world kind truthfully three-wide

- Research primary/official sources for at least three simultaneous global
  Season windows and three overlapping New York Here windows.
- Record source URL, source label, source-as-of, source note, review time, and
  editorial expiry for every row.
- Extend Season catalog semantics to admit reviewed global windows without
  pretending they are local; retain the destination/place label in line two.
- Keep Here exact to canonical New York aliases and verify its place identity.
- Add catalog lint for duplicate ids, missing provenance, impossible ranges,
  expired review, copy budget, and fewer than three rows in the declared
  dogfood window.
- Add fixed-date tests proving exactly three eligible Season rows and exactly
  three eligible Here rows, plus omission before/after each window.

Exit: on the declared dogfood clock, Season and Here each yield three real
rows; outside supported dates/places they fail absent rather than backfill.

### Batch 3 — finish due-time rotation and expiry failover

- Make the rotate endpoint prepare Route only when the due server cursor is
  about to consider Route.
- Pass Route's earliest offer expiry into cursor timing; persist
  `rotate_after` no later than that expiry.
- Keep ordinary GET behavior: hold a valid selected kind, immediately fail over
  an ineligible/expired kind, never advance a still-valid kind.
- In the app, schedule one timer for the server's `rotate_after`; on fire,
  refetch and submit the opaque id only when `may_advance` is true.
- Cancel/rebuild the timer on blur, account change, envelope change, and
  unmount. Keep focus refresh and replay protection.
- Add a local/test-only accelerated dwell to prove the complete ring without
  waiting six hours. Fail startup if an accelerated dwell is configured in a
  production environment.
- Verify the existing transition swaps cap, read, and rows together; reduced
  motion performs an immediate replacement.

Exit: a continuously open local device advances through all eligible kinds;
production timing remains server-authored; stale Route cannot linger.

### Batch 4 — fixtures, tests, and observability

Backend:

- property tests for ring order, skip/failover, replay, early advance, and
  Route-expiry-shortened dwell;
- cache/lease/cooldown/cap tests against Postgres;
- provider projection cases: direct, connecting, round trip, day-bearing
  duration, mismatched/expired/malformed offers, and fewer than three winners;
- API tests proving GET cannot call Duffel and due POST can call it once;
- privacy tests confirming Route remains personal read material and never
  enters voice/group writes as private preference context.

Frontend:

- Account editor add/edit/remove/validation and profile invalidation;
- timer scheduling/cancellation, due POST, replay, focus refresh, and account
  boundary tests;
- three-row fixtures for Sessions, Route, Season, and Here;
- transition and reduced-motion tests across all four kinds;
- default/135% Dynamic Type density and one-edge-label assertions.

Operations:

- a read-only Route diagnostics command showing configured origin cohort,
  monthly attempted searches, fresh cache count, earliest expiry, cooldown,
  and last provider outcome without credentials or user content;
- catalog validation command included in the focused verification target.

Exit: static trace, focused backend/frontend suites, migration, typecheck,
lint, and Vesper-specific contract checks pass.

### Batch 5 — real dogfood and device receipt

1. Use Account → Home Base to set the dogfood account to JFK.
2. Run the operator canary once; record provider request count, valid winners,
   earliest expiry, and confirmation that no order/hold/payment was created.
3. Fetch the real Workbench envelope against migrated Postgres and prove three
   Route rows came from the fresh cache.
4. Run the accelerated local rotation on iPhone and Android:
   Sessions → Route → Season → Here → Sessions.
5. Capture each settled band at default type and world rows at 135% type;
   capture Reduce Motion replacement.
6. Review layout, copy, source/freshness receipt, route expiry failover,
   composer reachability, and absence of debug/provider chrome.
7. Restore production dwell before final config verification.

Exit: live-provider/backend canary and reviewed device evidence both exist.
This is still internal dogfood, not broad production/provider certification.

### Batch 6 — synchronize, document, and roll out

- After the concurrent Places contract lane settles, run the required workspace
  OpenAPI/type synchronization and review only the resulting intended diffs.
- Run backend tests, frontend Vesper tests, typecheck, lint, API boundaries,
  contract check, and single-head migration check.
- Update the engine plan's stale execution status and promote the settled rules
  to backend `FEATURE.md` and the app surface contract.
- Commit backend, frontend, and workspace documentation independently with
  explicit filenames.
- Keep Route on the JFK dogfood allowlist and retain one-switch rollback:
  `HOME_ROUTE_DUFFEL_ENABLED=false`.
- Observe cache-hit rate, provider attempts, cap exhaustion, producer
  eligibility, selected-kind counts, no-well rate, and rotation failures before
  adding another origin.

Exit: the four-kind program is documented at the evidence layer actually
reached, rollback is immediate, and no stale planning claim remains.

## Verification matrix

| Layer | Required receipt |
|---|---|
| Static | schemas, privacy boundary, catalog provenance, GET/POST provider boundary |
| Mock walk | four kinds × three rows, full ring, reduced motion, Dynamic Type |
| Backend canary | migrated Postgres, cap/lease/cache, fresh Duffel winners, no booking calls |
| Device | iPhone + Android settled captures, continuous rotation, expiry failover |
| Rollout | dogfood flag/cohort, diagnostics, rollback, spend ceiling |

## Execution order and stopping policy

Execute Batches 0–4 continuously without asking for product decisions already
frozen above. Pause only for:

- a source that cannot support three honest rows in the declared window;
- a provider response/permission change that invalidates the Duffel contract;
- a conflicting concurrent edit on the same Vesper files;
- the live dogfood call if its configured request ceiling would be exceeded;
- device infrastructure unavailable after mock/backend gates pass.

Batch 5 intentionally performs live provider searches within the configured
ceiling. It remains read-only flight search. Batch 6 may wait for the unrelated
Places OpenAPI lane rather than overwriting its work.

## Explicitly deferred

- destination personalization from private history or constraints;
- global Here coverage or generic ticket/event ingestion;
- world-row tap actions, chat seeding, booking, holds, or payments;
- broad origin expansion beyond the approved dogfood cohort;
- replacing the candidate catalog with a commercial inspiration/discovery API;
- native voice work and any structural reallocation between seam/facts/list.
