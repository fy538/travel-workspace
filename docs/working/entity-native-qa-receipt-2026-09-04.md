---
title: Entity native QA receipt
date: 2026-09-04
owner: mobile-product
status: active
expires: 2026-10-04
scope: entity-object-page-and-plan-handoff
backfill: false
created: 2026-09-04
why_new: "Records current-build native smoke evidence for the rebuilt venue object page, private handoff doorway, and explicit placement boundary."
doc_type: working
---

# Entity native QA receipt

This receipt records current-build native smoke passes for the default venue
object route, the registered Places route, the explicit plan-placement
boundary, and the guarded shared renderer across venue, site, and experience.
It is evidence for those slices, not a production rollout receipt or proof of
the complete state matrix.

## Run

- Core context run: `travel-app` at `47735f406` (includes the continuity fix
  from `4579a1fc7`)
- Device: iPhone 16 Pro simulator, iOS 18.2
- UDID: `AF31B886-E837-4962-834A-5CBAD5C306DB`
- App id: `com.fyan.vesper`
- Data lane: mock, runner-seeded (`dev.mockModeOverride=true`)
- Object-page rebuild flag: off (the runs exercise the default venue route;
  `ObjectPageRebuild` flag-on acceptance is a separate gate)
- Research: disabled; no queue request or provider call
- Flow: `travel-app/.maestro/54b-journey-07-venue-context.yaml`
- Metro: LAN development bundle with internal-build routes enabled
- Frozen clock: `1780502400000`
- Command:

  ```bash
  maestro test --udid AF31B886-E837-4962-834A-5CBAD5C306DB \
    .maestro/54b-journey-07-venue-context.yaml
  ```

- Result: pass. Every flow step completed, including both screenshots.
- Captured screenshots:
  - `/Users/feihuyan/travel-workspace/travel-app/54-02-venue-identity-and-save-action.png`
  - `/Users/feihuyan/travel-workspace/travel-app/54-03-contextual-private-vesper.png`
- Raw pass log: `/tmp/entity-native-maestro-pass.log`

The explicit plan-placement flow also passed on the follow-up mobile commit:

- Mobile repository: `travel-app` at `35c110f47`
- Flow: `travel-app/.maestro/54c-journey-07-venue-plan-outcome.yaml`
- Fixture: currently unplanned `Pastéis de Belém` in the `Porto` trip
- Result: pass through Add to trip → choose trip → choose day → review →
  Add to itinerary → affected plan projection
- Captured screenshots:
  - `/Users/feihuyan/travel-workspace/travel-app/54-04-explicit-plan-review.png`
  - `/Users/feihuyan/travel-workspace/travel-app/54-05-affected-plan-projection.png`
- Raw pass log: `/tmp/entity-native-plan-maestro-pass7.log`

A second registered Places capture also passed after updating its stale shell
assertion from `Home` to the current `Plans` label:

- Flow: `travel-app/.maestro/polish/places.yaml`
- Run folder: `travel-app/.maestro/runs/20260904T232355Z-places`
- Result: one full screenshot captured (`places-default.png`)
- Raw runner log: `/tmp/entity-places-runner.log`

The guarded shared-renderer slice also passed on the same simulator:

- Mobile source: `travel-app` at `7b4d0601b` (the journey definition was
  committed immediately afterward as `6e3fe8545`)
- Flow: `travel-app/.maestro/54d-journey-07-venue-rebuild.yaml`
- Object-page rebuild flag: on
- Research requests: disabled; no queue request or provider call
- Result: pass through rebuild route → canonical `Cervejaria Ramiro` identity
  → `Keep place` → absence of the legacy `Add to trip` ladder → visible
  `object-rebuild-ask` handoff
- Captured screenshot:
  `/Users/feihuyan/travel-workspace/travel-app/54-06-venue-rebuild-intended-verbs.png`
- Raw pass log: `/tmp/entity-native-rebuild-maestro.log`

The equivalent guarded site slice also passed:

- Mobile source: `travel-app` at `464e7da98`
- Flow: `travel-app/.maestro/54e-journey-07-site-rebuild.yaml`
- Object-page rebuild flag: on
- Research requests: disabled; no queue request or provider call
- Result: pass through rebuild route → canonical `Museu Nacional do Azulejo`
  identity → `Keep place` → absence of the legacy `Add to trip` ladder →
  visible `object-rebuild-ask` handoff
- Captured screenshot:
  `/Users/feihuyan/travel-workspace/travel-app/54-07-site-rebuild-intended-verbs.png`
- Raw pass log: `/tmp/entity-native-site-rebuild-maestro.log`

The guarded experience slice also passed after aligning the mock envelope with
the existing event detail fixture:

- Mobile source: `travel-app` at `377c8a4b5`
- Flow: `travel-app/.maestro/54f-journey-07-experience-rebuild.yaml`
- Object-page rebuild flag: on
- Research requests: disabled; no queue request, booking, or provider call
- Result: pass through rebuild route → canonical `LUX Fragil Closing Night`
  identity → `Keep place` → absence of the legacy `Add to trip` ladder →
  visible `object-rebuild-ask` handoff
- Captured screenshot:
  `/Users/feihuyan/travel-workspace/travel-app/54-08-experience-rebuild-intended-verbs.png`
- Raw pass log: `/tmp/entity-native-experience-rebuild-maestro.log`

The guarded renderer was then exercised against the local real HTTP backend
and native PostgreSQL (not the mock adapter). The temporary backend ran at
`http://127.0.0.1:8001` with `SKIP_AUTH=true`, the existing local dev user,
`DISABLE_API_BACKGROUND_TASKS=true`, and
`ENTITY_RESEARCH_REQUESTS_ENABLED=false`; the app bundle used real API mode
with the object-page rebuild flag enabled. The clean rerun used the same
simulator and route assertions with all API background workers disabled. These
flows only read existing local rows—no save, research request, provider call,
or catalog write was performed:

- App checkout: `travel-app:89367c36e` (the entity renderer change remains
  `d3b22275b`; later commits in this checkout are unrelated Life work).
- Backend checkout: `travel-agent:e33dd4764` (entity health baseline remains
  `9f3d80959`; later commits in this checkout are unrelated resilience work).
- Venue `1` (`J06 Museum 5bc85584`): `/tmp/entity-real-object-page.yaml`,
  log `/tmp/entity-native-real-venue-no-bg.log`, screenshot
  `/Users/feihuyan/travel-workspace/travel-app/entity-real-object-page-local.png`.
- Site `1794` (`Castelo de São Jorge`): `/tmp/entity-real-site-page.yaml`,
  log `/tmp/entity-native-real-site-no-bg.log`, screenshot
  `/Users/feihuyan/travel-workspace/travel-app/entity-real-site-page-local.png`.
- Experience `fb4d6efd-588f-4647-9ca7-3819f90935e8` (`Flavours of Sorrento -
  Food and Walking Tour`): `/tmp/entity-real-experience-page.yaml`, log
  `/tmp/entity-native-real-experience-no-bg.log`, screenshot
  `/Users/feihuyan/travel-workspace/travel-app/entity-real-experience-page-local.png`.

Each real-backend flow passed route identity, `Keep place`, absence of the
legacy `Add to trip` ladder, and the visible `Ask Vesper` doorway. This closes
the live-read portion of the guarded identity/verb gate for the three current
kinds; it does not close auth diversity, research, write/readback, repair,
offline, VoiceOver, Android, or the remaining state matrix.

A follow-up real-backend process-restart flow also passed for venue `1`: it
stopped and relaunched the app, reopened the same deep link, and reasserted
the canonical identity, `Keep place`, and absence of `Add to trip`. Flow
`/tmp/entity-real-process-restart.yaml`, log
`/tmp/entity-native-real-process-restart.log`, and screenshot
`/Users/feihuyan/travel-workspace/travel-app/entity-real-process-restart-local.png`
record this bounded restart check. A cleared-state cold start remains a
development-client harness gate, not a product pass.

The backend companion checks used the same native PostgreSQL instance at
`localhost:5432` (Alembic head `sourcecache01`): the entity/research/
relationship suites passed 48 tests, and the real second-occasion loop-closure
scenario passed 5 tests. These checks exercised existing local rows and
transactional read/write fixtures in their test harness; they did not seed a
catalog or invoke paid research.

The same no-background local API returned an honest `404` for an unknown site
on the public envelope and both authenticated presentation variants
(`/api/entities/site/999999`, `/api/me/entities/site/999999/presentation`, and
`/api/me/entities/site/999999/presentation-v2`). The native UI unavailable
flow could not be completed because clearing the development client state
left Maestro at the Expo development-server picker; that harness limitation is
why unavailable/process-restart remain open native gates rather than being
counted as passes.

The follow-up privacy/repair coverage on that same database passed 66 tests
across entity presentation reads, private-entity contracts, entity routes,
people-lines gating, relationship handoffs, and outcome feedback. On the
current app checkout, the seven entity screen/renderer/projection suites also
passed 78 tests. These are deterministic regression checks; the native state
matrix and two-account device journey remain separate gates.

The complete entity-focused backend selection (API, Places, core identity,
database identity, research queue, and health-report tests) passes 221 tests
with 10 skips. The skips are the dogfood-wedge-only or explicitly gated cases
that require an enriched corpus or unavailable external capability; they are
not needed for the canonical object-page lane and are recorded rather than
silently counted as passes. The latest selection includes the terminal-Plan
repair coverage for geofence, expense, photo, and compatibility commitment
evidence.

The read-only health report at `2026-09-05T00:41:29Z` reports zero stale
claims, duplicate active jobs, expired processing leases, retried rows, and
completed-without-fresh-brief mismatches. It does report one pending venue
research row with an oldest age of about 25 days and one pending resolution
review; both remain untouched and require named operational disposition before
any research canary.

The three guarded journeys were then repeated at iOS `accessibility-medium`
Dynamic Type on the post-fix source `travel-app:d3b22275b`. All assertions
passed and the simulator content-size setting was restored to `large`
afterward:

- Venue: `/tmp/entity-native-rebuild-a11y-postfix.log`, screenshot
  `/Users/feihuyan/travel-workspace/travel-app/54-12-venue-rebuild-accessibility-medium-postfix.png`
- Site: `/tmp/entity-native-site-rebuild-a11y-postfix.log`, screenshot
  `/Users/feihuyan/travel-workspace/travel-app/54-13-site-rebuild-accessibility-medium-postfix.png`
- Experience: `/tmp/entity-native-experience-rebuild-a11y-postfix.log`,
  screenshot
  `/Users/feihuyan/travel-workspace/travel-app/54-14-experience-rebuild-accessibility-medium-postfix.png`

The static accessibility governance check also passes after removing the
renderer’s Dynamic Type opt-outs (`npm run accessibility-governance`). This is
still a bounded enlarged-text check, not a VoiceOver, Android, or full
accessibility certification.

The supporting mobile contract checks also pass on the current app checkout:
`npm run test:typecheck:contracts`, `npm run api-boundaries`, and
`npm run schema-bridge` (the script runs in CI mode). These are static checks
only; they do not widen the native or backend evidence recorded here.

## Follow-up harness disposition — 2026-09-05

A bounded rerun was attempted after the receipt was written to extend the
mock-lane coverage. The first launch failed inside the iOS simulator's
`dyld_sim` shared-cache preparation with `EXC_BAD_ACCESS`/`SIGBUS`, before app
code executed. After restarting the simulator, the app launched but remained
on the real-auth account-recovery shell rather than entering the intended mock
fixture lane; the `Plans` assertion therefore failed. This is a development
client/environment issue, not a product verdict, and no screenshot from that
attempt is counted as evidence. The temporary local environment override used
for diagnosis was removed and `.env.local` is back to its original Mapbox-only
contents. The unavailable-state, auth-diversity, and cleared-state native gates
remain open until a clean harness run can exercise them.

## Assertions covered

1. The default venue route opens from the dev handoff and lands on the current Plans
   shell.
2. Venue identity renders as `Cervejaria Ramiro` with the `venue-detail-screen`
   test id.
3. The independent `Save place` action is visible.
4. The private `Ask Vesper` doorway is reachable after scrolling.
5. The private chat composer and completed assistant response render, and the
   response names the focused venue rather than only describing generic venue
   context.
6. A currently unplanned venue can be placed through the canonical, explicit
   review boundary and the committed result returns to the affected plan.
7. The guarded shared object renderer uses the same canonical venue identity,
   exposes the intended Keep/Ask contract, and does not regress into the
   compatibility route's generic Add-to-trip ladder.
8. The guarded shared object renderer carries the same identity and verb
   contract for a site (`Museu Nacional do Azulejo`).
9. The guarded shared object renderer carries the same identity and verb
   contract for an experience (`LUX Fragil Closing Night`).
10. Post-fix enlarged-text iOS runs preserve the guarded venue/site/experience
    identity and Keep/Ask assertions without a route or renderer failure.
11. Static accessibility governance passes for the renderer and app.

## Limits and next gate

These are scoped mock-lane and local-real-backend read passes. They do not
certify real-backend auth diversity, research lifecycle states, live situation
freshness, source attribution, relationship differences across two accounts,
accessibility at large text or screen-reader navigation, Android, or the full
loading/error/empty matrix. They also do not certify live availability/booking
or the remaining write/readback and repair paths. The flag-on venue, site, and
experience routes are now evidenced as three bounded identity/verb slices plus
an enlarged-text iOS pass and a local-real-backend read pass; broader state
convergence and rollout remain gates in the entity roadmap and must be attached
to a reviewed pilot receipt before any capability is enabled. No production
rows, research jobs, provider calls, booking, or backfill were created by
these native flows.
