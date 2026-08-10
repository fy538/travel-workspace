---
doc_type: working
status: active
owner: engineering / product / evidence
created: 2026-08-10
last_verified: 2026-08-10
expires: 2026-09-09
why_new: Defines the fail-closed deployed and two-device proof boundary for the fixed Lisbon Group Trip disruption without promoting source or Postgres evidence to device evidence.
source_of_truth_for:
  - lisbon-group-trip-staging-device-proof-2026-08
related:
  - convergence-and-ai-decision-next-execution-plan-2026-08-10.md
  - journey-live-full-cert-04-05-10.md
  - ../journeys/EVIDENCE_MODEL.md
  - ../journeys/product-proofs.yaml
---

# Lisbon Group Trip staging and device proof

## Claim boundary

The source candidate defines and replays the Lisbon rain-rescue scenario. It is
not controlled-device, staging, or physical evidence. P05 and P07 remain dark
until revision-bound receipts exist for the layers they require.

The fixed scenario is owned by:

- `travel-agent/tests/fixtures/lisbon_group_disruption.json`;
- `travel-agent/tests/scenarios/test_lisbon_group_disruption_contract.py`;
- `travel-agent/tests/scenarios/test_lisbon_group_disruption_replay.py`;
- `travel-app/__tests__/utils/takeSomewhere.test.ts`;
- `travel-app/__tests__/components/trip-plan/NowModeStrip.test.tsx`;
- `travel-app/.maestro/72-group-trip-doorway-device-mock.yaml` (supporting
  live-group doorway proof only; it does not exercise the Lisbon mutation
  lifecycle and cannot pass P05 or P07 by itself).

## Exact staging identity

Before any staging walk, fill every non-source identity in
`convergence-ai-next-round-candidate-2026-08-10.json`:

| Identity | Required value |
| --- | --- |
| Workspace/backend/app | exact clean candidate SHAs |
| Backend | immutable image or deploy digest |
| Mobile | exact EAS/internal build ID |
| Database | applied Alembic revision |
| World | fixed fixture/corpus SHA-256 |
| Flags | backend weather rescue on with the exact Trip in `WEATHER_RESCUE_TRIP_IDS`; internal app and Group Trip doorway on |

The rollback is all-off: `WEATHER_RESCUE_PROPOSALS_ENABLED=false`,
`EXPO_PUBLIC_GROUP_TRIP_MICRO_JOURNEY_ENABLED=false`, or a non-internal build.
AI decision shadow flags remain false throughout this product proof.

## Controlled-device walk

Use an internal build against a controlled backend seeded from the fixed
fixture. Record `device_mock`, never `physical`.

The local simulator support flow has separately confirmed the production Plan
doorway and private review-first handoff on a clean revision. Its receipt is
owned under `P05-doorway-support`, not `P05`; steps 3–7 below remain required
before the product proof can pass.

The 2026-08-10 deployed checkpoint uses backend
`7b7f673610416447aca363fc592d74475fa20f1f`, Fly digest
`sha256:da11da3529dea8161345a48e7ef9a765f5527a3eef1aa6c98cc790eaf02e6113`,
migration `receiptidem01`, existing internal iOS build
`aa524cdb-7b34-4f27-9864-425df19a2e47`, and exact-SHA OTA group
`a8ae572d-f59c-481c-b768-3359ecbc35b6`. Treat the binary and OTA as one mobile
identity. Controlled Trip `f47e582d-85a6-454e-8a2d-be3a199f0b09` is seeded,
verified, and is the only weather-rescue allowlist entry. The global producer
remains off until the staging operator begins the governed walk.

The original four-member canonical-world Trip was not modified. The separate
controlled Trip has exactly the fixture actors and roles, one canonical
itinerary, source block `660002d9-3f0d-5aab-947b-93344bef6adf`, and protected
block `a0cad209-addd-5378-9f74-ad27db8619bf`. Re-run
`python scripts/provision_lisbon_group_disruption.py` as a read-only preflight
immediately before enabling the producer; any roster or plan drift blocks the
walk.

1. Organizer opens the live Lisbon Plan and sees `Take us somewhere` only when
   there is a server-resolved current block.
2. The doorway opens a private review-first chat containing the grounded-route
   request. No plan mutation or group post occurs from the tap.
3. A thin participant joins through the real invite redemption path and can
   read the same open rescue proposal.
4. The participant approves; the organizer accepts. Both observers' Plan, Map,
   and Now show the same replacement block and projection revision.
5. Reject and expiry forks preserve the original block. The revert fork restores
   it on every shared projection and leaves a visible receipt.
6. Each identity privately confirms the occurrence and records an outcome. One
   participant's verdict or rationale is absent from every group surface.
7. Correct one private outcome and verify only that person's private artifact
   changes. A changed roster withholds companion-fit reuse.

Any skipped assertion makes the affected proof blocked, not pass.

## Physical two-device walk

Reuse the hardware, identity, artifact, and receipt discipline in
`journey-live-full-cert-04-05-10.md`, but execute the fixed P05/P07 assertions
above. The operator must supply two unique hardware UDIDs, two unique real
identities, build/deploy/migration/seed identity, oracle and flow hashes,
reviewer, and fresh content-addressed screenshots or video. Simulator labels,
unresolved device names, pre-existing artifacts, and manually authored receipt
JSON are rejected by the evidence tooling.

## Receipt commands

The staging and physical commands are operator-owned because they deploy and
touch real accounts. Use `make dogfood-staging` with
`DOGFOOD_STAGING_PROOFS=P07`; use `scripts/journey_evidence.py record` for the
controlled P05/P07 device-mock command. Extend the physical runner's governed
proof list before running it; do not relabel the existing J04/J05/J10 receipt.

Promotion order is strict: source/database → staging → controlled device →
physical. P05 needs contract, database, and device-mock. P07 needs those plus
staging. Physical evidence is a separate stronger claim and never inferred.
