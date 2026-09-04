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
object route, the registered Places route, and the explicit plan-placement
boundary. It is evidence for those slices, not a production rollout receipt
or proof of the complete state matrix.

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

## Limits and next gate

These are scoped mock-lane passes. They do not certify real-backend auth,
research lifecycle states, live situation freshness, source attribution,
relationship differences across two accounts, accessibility at large text or
screen-reader navigation, Android, or the full loading/error/empty matrix.
the guarded `ObjectPageRebuild` flag-on route, or full shared-renderer
convergence. Those remain separate gates in the entity roadmap and must be
attached to a reviewed pilot receipt before any capability is enabled. No production rows,
research jobs, provider calls, or backfill were created by this run.
