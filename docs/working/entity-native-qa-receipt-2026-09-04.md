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

These are scoped mock-lane passes. They do not certify real-backend auth,
research lifecycle states, live situation freshness, source attribution,
relationship differences across two accounts, accessibility at large text or
screen-reader navigation, Android, or the full loading/error/empty matrix.
They also do not certify the full shared-renderer state matrix, live
availability/booking, real-backend auth, research lifecycle states, VoiceOver,
Android, or other platform/accessibility coverage. The flag-on venue, site,
and experience routes are now evidenced as three bounded identity/verb slices
plus an enlarged-text iOS pass; broader state convergence and rollout remain
gates in the entity roadmap and must be attached to a reviewed pilot receipt
before any capability is enabled. No production rows, research jobs, provider
calls, booking, or backfill were created by this run.
