# Golden Paths

> **Redirect:** This doc is retained for link stability. The canonical index is
> [Journey Status Matrix](../journeys/STATUS.md) — twelve user journeys with
> mock-walk, logic QA, Maestro, and live gates tracked in one place.

## Quick commands

| Intent | Command |
|--------|---------|
| Daily / PR gate | `make certify-fast` |
| Backend journey logic (Postgres) | `make certify-logic` |
| Wedge visual (simulator) | `make certify-visual` |
| Wedge golden path subset | `make golden-path-qa` |
| Full offline ladder | `make offline-qa` |
| Dogfood substrate check | `make dogfood-status` |

## Wedge journeys (02 → 05 → 06)

The original six "golden paths" map to journeys as follows:

| Legacy golden path | Journey | Mock-walk owner |
|--------------------|---------|-----------------|
| Create trip + invite | [J02](../journeys/02-concrete-trip-creation-and-invite.md) | `journey-02-mock-walk.smoke.test.tsx` |
| Private → group-safe | [J04](../journeys/04-private-constraint-to-group-safe-plan.md) | `journey-04-mock-walk.smoke.test.tsx` |
| Proposal + plan mutation | [J05](../journeys/05-group-planning-to-proposal-to-plan-mutation.md) | `05-group-planning-proposal-mutation.test.ts` + `journey-05-mock-walk.smoke.test.tsx` |
| Home / plan / map coherence | [J06](../journeys/06-home-plan-map-changes-coherence.md) | `06-cross-surface-coherence.test.ts` |
| Notifications routing | [J09](../journeys/09-notifications-and-proactive-routing.md) | `journey-09-mock-walk.smoke.test.tsx` |
| Atlas memory control | [J11](../journeys/11-atlas-candidate-to-memory-control.md) | `journey-11-mock-walk.smoke.test.tsx` |

Legacy anchors like `__tests__/offline/goldenPath.test.ts` remain useful smoke tests
but are no longer the primary journey index.

See [Agent Reliability Playbook](./Agent%20Reliability%20Playbook.md) for the full
testing model and live canary guidance.
