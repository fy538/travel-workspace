---
doc_type: contract
status: active
owner: founder / engineering
created: 2026-06-30
last_verified: 2026-08-09
why_new: Renders the machine-readable V1 release intent as the authoritative human scope contract.
supersedes: [docs/working/mvp-scope-and-flag-manifest-2026-06-30.md]
source_of_truth_for: [v1-release-scope]
---

# Vesper v1 release contract

> Generated from [`v1-scope.yaml`](v1-scope.yaml). Do not hand-edit this file;
> run `make docs-release-sync` after changing the manifest or flag registry.

**Status:** scope-locked · **Decided:** 2026-06-30 · **Last verified:** 2026-08-09

## Promise

A vague idea becomes one useful group Trip; members can refine it through governed proposals; it remains useful while traveling; it comes home as a story; and the group can settle up.

## Governing principles

- Harden the IN set; keep excluded code dark rather than deleting it.
- Planning and group participation are the wedge; live transaction execution is not required for v1.
- A capability is not production-enabled merely because code exists.
- Journey and device evidence, not this manifest, certify release readiness.

## Capability boundary

Code evidence means the named implementation paths exist. It does not mean the
capability is enabled, production-configured, or certified. Journey Status and
device receipts own those claims.

| Capability | Intent | Code evidence | Default posture | Certification |
|---|---|---:|---|---|
| Auth and onboarding | **IN** | 1/1 paths present | No release flag declared | [J01, J02](../journeys/STATUS.md) |
| Trip creation, invite, membership, and roles | **IN** | 2/2 paths present | No release flag declared | [J02, J03, J04](../journeys/STATUS.md) |
| Planning, itinerary, proposals, and revert | **IN** | 2/2 paths present | No release flag declared | [J01, J05, J06](../journeys/STATUS.md) |
| Concierge, personal memory, and group synthesis | **IN** | 3/3 paths present | No release flag declared | [J04, J07](../journeys/STATUS.md) |
| Trip Home, living itinerary, map, and Now behavior | **IN** | 2/2 paths present | No release flag declared | [J06, J08, J09](../journeys/STATUS.md) |
| Post-trip Story and Trip photos | **IN** | 2/2 paths present | No release flag declared | [J11](../journeys/STATUS.md) |
| Expenses and settlement | **IN** | 2/2 paths present | No release flag declared | [J10, J12](../journeys/STATUS.md) |
| Places, Atlas, Discover, and universal search | **IN** | 4/4 paths present | Enabled by default | [J07](../journeys/STATUS.md) |
| Profiles, people search, follow, and following | **IN** | 2/2 paths present | No release flag declared | [J13](../journeys/STATUS.md) |
| Booking record, mark-as-booked, and external handoff | **PARTIAL** | 2/2 paths present | No release flag declared | [J10](../journeys/STATUS.md) |
| Live booking transaction execution | **OUT** | 2/2 paths present | Dark by default | [J10](../journeys/STATUS.md) |
| Live voice, narration, and microphone entry points | **OUT** | 2/2 paths present | Dark by default | [J18](../journeys/STATUS.md) |
| Rendered postcards and postcard sub-surfaces | **OUT** | 2/2 paths present | Dark by default | [J11](../journeys/STATUS.md) |
| Ambient and nearby proactive experiences | **OUT** | 2/2 paths present | Dark by default | [J09](../journeys/STATUS.md) |
| Public story links and social distribution | **OUT** | 2/2 paths present | Dark by default | [J19](../journeys/STATUS.md) |
| Agent-initiated venue-disruption proposals | **OUT** | 2/2 paths present | Dark by default | [J05, J09](../journeys/STATUS.md) |

## Boundary notes

- **Auth and onboarding:** Real Clerk accounts are the device path; the persona-JWT HTTP harness is non-blocking automation.
- **Trip creation, invite, membership, and roles:** Full-group behavior is in scope and requires multi-device evidence.
- **Planning, itinerary, proposals, and revert:** Explicit propose, approve, apply, and revert are in; autonomous disruption production remains dark.
- **Concierge, personal memory, and group synthesis:** Privacy-mediated synthesis is part of the launch proof.
- **Trip Home, living itinerary, map, and Now behavior:** Cross-surface coherence and current-condition honesty are release-critical.
- **Post-trip Story and Trip photos:** The private/shared-with-members story is in; public distribution and postcard rendering are separate dark capabilities.
- **Expenses and settlement:** Settlement completes the shared Trip loop.
- **Places, Atlas, Discover, and universal search:** Core place and memory surfaces are in; dark sub-surfaces remain governed below.
- **Profiles, people search, follow, and following:** Public story distribution is not implied by profiles or relationship edges.
- **Booking record, mark-as-booked, and external handoff:** Honest non-transacting handoff is in; provider transaction execution is out.
- **Live booking transaction execution:** Duffel cart, hold, and execution remain dark for v1.
- **Live voice, narration, and microphone entry points:** Code exists but the live experience remains outside v1 until end-to-end certification.
- **Rendered postcards and postcard sub-surfaces:** Post-trip Story is in; image-generation artifacts are dark.
- **Ambient and nearby proactive experiences:** The company vision includes earned proactivity; broad ambient dispatch is not a v1 claim.
- **Public story links and social distribution:** Requires public-taste and privacy certification before exposure.
- **Agent-initiated venue-disruption proposals:** Explicit proposals are in; this producer remains dark until precision and cohort evidence justify it.

## Readiness

This contract owns release intent only. Use
[Current State](../status/current-state.md) for the generated intent/evidence view,
[Journey Status](../journeys/STATUS.md) for certification, and
[Owner Actions](../Owner%20Action%20Items.md) for external blockers.
