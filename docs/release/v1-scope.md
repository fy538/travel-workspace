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

This contract governs which surfaces may ship lit and which must stay dark for the first store release. It is a shipping boundary, not a roadmap and not a product promise. The company promise lives in Product Thesis; the current milestone lives in M1 — Plan Repair (docs/release/m1-plan-repair.md).

## Governing principles

- Harden the IN set; keep excluded code dark rather than deleting it.
- Planning and group participation are the wedge; live transaction execution is not required for v1.
- A capability is not production-enabled merely because code exists.
- Journey and device evidence, not this manifest, certify release readiness.
- Journey IDs are informational anchors for coverage; they do not drive device certification.
- Physical evidence for this release comes from the J04/J05/J10 two-device lane plus M1 proof receipts, not from per-capability journey walks.

## Capability boundary

Implementation means the named paths are tracked by their owning repository.
Release defaults come from the flag registry; they are not deployed-production
configuration. Readiness exposes known seeded-replay failures but remains
uncertified until a current-revision receipt exists.

| Capability | Intent | Implementation | Release default | Production-enabled | Readiness |
|---|---|---:|---|---|---|
| Auth and onboarding | **IN** | 1/1 tracked paths | No release flag declared | Unverified externally | [UNCERTIFIED — required promoted layers missing J01: physical; J02: physical](../journeys/STATUS.md) (J01, J02) |
| Trip creation, invite, membership, and roles | **IN** | 2/2 tracked paths | No release flag declared | Unverified externally | [UNCERTIFIED — required promoted layers missing J02: physical; J03: physical; J04: physical](../journeys/STATUS.md) (J02, J03, J04) |
| Planning, itinerary, proposals, and revert | **IN** | 2/2 tracked paths | No release flag declared | Unverified externally | [UNCERTIFIED — required promoted layers missing J01: physical; J05: physical; J06: physical](../journeys/STATUS.md) (J01, J05, J06) |
| Concierge, personal memory, and group synthesis | **IN** | 3/3 tracked paths | No release flag declared | Unverified externally | [UNCERTIFIED — required promoted layers missing J04: physical; J07: physical](../journeys/STATUS.md) (J04, J07) |
| Trip Home, living itinerary, map, and Now behavior | **IN** | 2/2 tracked paths | No release flag declared | Unverified externally | [UNCERTIFIED — required promoted layers missing J06: physical; J08: physical; J09: physical](../journeys/STATUS.md) (J06, J08, J09) |
| Post-trip Story and Trip photos | **IN** | 2/2 tracked paths | No release flag declared | Unverified externally | [UNCERTIFIED — required promoted layers missing J11: physical](../journeys/STATUS.md) (J11) |
| Expenses and settlement | **IN** | 2/2 tracked paths | No release flag declared | Unverified externally | [UNCERTIFIED — required promoted layers missing J10: physical; J12: physical](../journeys/STATUS.md) (J10, J12) |
| Places and universal search | **IN** | 5/5 tracked paths | Enabled by default | Unverified externally | [UNCERTIFIED — required promoted layers missing J07: physical](../journeys/STATUS.md) (J07) |
| Profiles, people search, follow, and following | **IN** | 2/2 tracked paths | No release flag declared | Unverified externally | [UNCERTIFIED — required promoted layers missing J13: physical](../journeys/STATUS.md) (J13) |
| Grounded live Plan repair | **IN** | 2/2 tracked paths | Dark by default | Not claimed; in scope but gated | [UNCERTIFIED — required promoted layers missing J05: device_mock,staging; J06: device_mock,staging; J08: device_mock,staging](../journeys/STATUS.md) (J05, J06, J08) |
| Open-interval micro-journey doorway | **IN** | 2/2 tracked paths | Dark by default | Not claimed; in scope but gated | [UNCERTIFIED — required promoted layers missing J08: device_mock](../journeys/STATUS.md) (J08) |
| Local Plans beyond travel | **IN** | 2/2 tracked paths | Dark by default | Not claimed; in scope but gated | [UNCERTIFIED — required promoted layers missing J07: device_mock; J14: device_mock](../journeys/STATUS.md) (J07, J14) |
| One permissioned relationship opening | **IN** | 2/2 tracked paths | Dark by default | Not claimed; in scope but gated | [UNCERTIFIED — required promoted layers missing J09: ai_eval,device_mock](../journeys/STATUS.md) (J09) |
| Booking record, mark-as-booked, and external handoff | **PARTIAL** | 2/2 tracked paths | No release flag declared | Unverified externally | [UNCERTIFIED — required promoted layers missing J10: physical](../journeys/STATUS.md) (J10) |
| Live booking transaction execution | **OUT** | 2/2 tracked paths | Dark by default | Not claimed; release defaults dark | [OUT — not a v1 certification target](../journeys/STATUS.md) (J10) |
| Live voice, narration, and microphone entry points | **OUT** | 2/2 tracked paths | Dark by default | Not claimed; release defaults dark | [OUT — not a v1 certification target](../journeys/STATUS.md) (J18) |
| Rendered postcards and postcard sub-surfaces | **OUT** | 2/2 tracked paths | Dark by default | Not claimed; release defaults dark | [OUT — not a v1 certification target](../journeys/STATUS.md) (J11) |
| Broad ambient dispatch and nearby feeds | **OUT** | 2/2 tracked paths | Dark by default | Not claimed; release defaults dark | [OUT — not a v1 certification target](../journeys/STATUS.md) (J09) |
| Public story links and social distribution | **OUT** | 2/2 tracked paths | Dark by default | Not claimed; release defaults dark | [OUT — not a v1 certification target](../journeys/STATUS.md) (J19) |
| Agent-initiated venue-disruption proposals | **OUT** | 2/2 tracked paths | Dark by default | Not claimed; release defaults dark | [OUT — not a v1 certification target](../journeys/STATUS.md) (J05, J09) |

## Boundary notes

- **Auth and onboarding:** Real Clerk accounts are the device path; the persona-JWT HTTP harness is non-blocking automation.
- **Trip creation, invite, membership, and roles:** Full-group behavior is in scope and requires multi-device evidence.
- **Planning, itinerary, proposals, and revert:** Explicit propose, approve, apply, and revert are in; autonomous disruption production remains dark.
- **Concierge, personal memory, and group synthesis:** Privacy-mediated synthesis is part of the launch proof.
- **Trip Home, living itinerary, map, and Now behavior:** Cross-surface coherence and current-condition honesty are release-critical.
- **Post-trip Story and Trip photos:** The private/shared-with-members story is in; public distribution and postcard rendering are separate dark capabilities.
- **Expenses and settlement:** Settlement completes the shared Trip loop.
- **Places and universal search:** Places owns exploration, search, maps, editorial context, and saved places. Discover and Atlas are retired product surfaces.
- **Profiles, people search, follow, and following:** Public story distribution is not implied by profiles or relationship edges.
- **Grounded live Plan repair:** M1 Act 1. A disruption becomes one grounded, group-safe replace proposal through the canonical proposal path; it never mutates the Plan directly. _Gate: Allowlisted by WEATHER_RESCUE_TRIP_IDS; lights per-Trip only, never globally._
- **Open-interval micro-journey doorway:** The sixty-second cold demo. One anchor plus its connective route between two commitments; not a generated multi-stop itinerary. _Gate: Internal builds only; requires a bounded open window, not an active block._
- **Local Plans beyond travel:** M1 Act 4. Proof that Experience/Plan/Move persists beyond tourism into bounded everyday occasions. _Gate: Dogfood cohort only; no external cohort until M1 Act 4 outcome capture is certified._
- **One permissioned relationship opening:** M1 Act 4 closing beat. A permitted opening between two people crosses the tentative-to-shared Plan boundary honestly. This is ambient-as-person-trigger, not a feed; a scrollable list is the tell that it became the thing Surfacing Strategy killed. _Gate: Dark until P06 (consent and silence) has anchors and its negative oracles pass. Double-opt-in only; one decline produces silence._
- **Booking record, mark-as-booked, and external handoff:** Honest non-transacting handoff is in; provider transaction execution is out.
- **Live booking transaction execution:** Duffel cart, hold, and execution remain dark for v1.
- **Live voice, narration, and microphone entry points:** Code exists but the live experience remains outside v1 until end-to-end certification.
- **Rendered postcards and postcard sub-surfaces:** Post-trip Story is in; image-generation artifacts are dark.
- **Broad ambient dispatch and nearby feeds:** Split from the former `ambient` capability on 2026-08-10. Broad dispatch and any generic nearby feed remain out; the single permissioned relationship opening is governed separately as `relationship-opening`.
- **Public story links and social distribution:** Requires public-taste and privacy certification before exposure.
- **Agent-initiated venue-disruption proposals:** Explicit proposals are in; this producer remains dark until precision and cohort evidence justify it.

## Readiness

This contract owns release intent only. Use
[Current State](../status/current-state.md) for the generated intent/evidence view,
[Journey Status](../journeys/STATUS.md) for certification, and
[Owner Actions](../Owner%20Action%20Items.md) for external blockers.
