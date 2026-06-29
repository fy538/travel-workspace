# Golden Paths

> **Redirect:** Canonical QA index is [Journey Status Matrix](../journeys/STATUS.md).
> Golden paths were the pre-2026-06 MVP name for a **subset of journeys** (J02, J04–J06, J09, J11).

## Commands (use these instead of "golden path")

| Intent | Command |
|--------|---------|
| Daily / PR gate | `make certify-fast` |
| All backend journey scenarios (Postgres) | `make certify-logic` |
| Wedge subset (J02/J05/J06 only) | `make journey-wedge-qa` |
| Mock slug parity (dogfood corpus) | `make mock-slug-parity` |
| Wedge visual (simulator) | `make certify-visual` |
| Full offline ladder | `make offline-qa` |
| Dogfood substrate | `make dogfood-status` |

`make golden-path-qa` remains as a **deprecated alias** for `journey-wedge-qa` (CI link stability).

## Legacy path → journey map

| Legacy golden path | Journey |
|--------------------|---------|
| Create trip + invite | [J02](../journeys/02-concrete-trip-creation-and-invite.md) |
| Private → group-safe | [J04](../journeys/04-private-constraint-to-group-safe-plan.md) |
| Proposal + plan mutation | [J05](../journeys/05-group-planning-to-proposal-to-plan-mutation.md) |
| Home / plan / map coherence | [J06](../journeys/06-home-plan-map-changes-coherence.md) |
| Notifications routing | [J09](../journeys/09-notifications-and-proactive-routing.md) |
| Atlas memory control | [J11](../journeys/11-atlas-candidate-to-memory-control.md) |

Trace write-ups under [traces/](./traces/) are historical context. Scenario registry:
`travel-agent/tools/dogfood/content/scenarios.yaml` (sole machine source).

See [Agent Reliability Playbook](./Agent%20Reliability%20Playbook.md) for the full ladder.
