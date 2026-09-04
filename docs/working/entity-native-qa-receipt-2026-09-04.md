---
title: Entity native QA receipt
date: 2026-09-04
owner: mobile-product
status: active
expires: 2026-10-04
scope: entity-object-page-and-private-venue-handoff
backfill: false
created: 2026-09-04
why_new: "Records the current-build native smoke evidence for the rebuilt venue object page and its private handoff doorway."
doc_type: working
---

# Entity native QA receipt

This receipt records current-build native smoke passes for the rebuilt venue
object page and the registered Places route. It is evidence for the core page
and its private handoff doorway, not a production rollout receipt or proof of
the complete state matrix.

## Run

- Mobile repository: `travel-app` at `47735f406` (includes the continuity fix
  from `4579a1fc7`)
- Device: iPhone 16 Pro simulator, iOS 18.2
- UDID: `AF31B886-E837-4962-834A-5CBAD5C306DB`
- App id: `com.fyan.vesper`
- Data lane: mock, runner-seeded (`dev.mockModeOverride=true`)
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

A second registered Places capture also passed after updating its stale shell
assertion from `Home` to the current `Plans` label:

- Flow: `travel-app/.maestro/polish/places.yaml`
- Run folder: `travel-app/.maestro/runs/20260904T232355Z-places`
- Result: one full screenshot captured (`places-default.png`)
- Raw runner log: `/tmp/entity-places-runner.log`

## Assertions covered

1. The rebuilt route opens from the dev handoff and lands on the current Plans
   shell.
2. Venue identity renders as `Cervejaria Ramiro` with the `venue-detail-screen`
   test id.
3. The independent `Save place` action is visible.
4. The private `Ask Vesper` doorway is reachable after scrolling.
5. The private chat composer and completed assistant response render, and the
   response names the focused venue rather than only describing generic venue
   context.

## Limits and next gate

These are scoped mock-lane passes. They do not certify real-backend auth,
research lifecycle states, live situation freshness, source attribution,
relationship differences across two accounts, accessibility at large text or
screen-reader navigation, Android, or the full loading/error/empty matrix.
Those remain separate gates in the entity roadmap and must be attached to a
reviewed pilot receipt before any capability is enabled. No production rows,
research jobs, provider calls, or backfill were created by this run.
