---
doc_type: current_status
status: active
owner: engineering
created: 2026-07-09
last_verified: 2026-08-23
why_new: Replace duplicated prose scorecards with one generated view of executable registries.
supersedes: []
source_of_truth_for: [cross-repo-current-state-summary]
---

# Current State

This is an orientation snapshot, not a release claim. Its numbers are generated
from committed registries; follow the linked authority for evidence and detail.

<!-- BEGIN auto:current-state -->
<!-- Run `make docs-status-sync` to update this block. -->
| Signal | Current value | Authority |
|---|---:|---|
| API contract | 557 paths / 619 operations / 1292 schemas | [`docs/openapi.json`](../openapi.json) |
| Canonical journeys | 28 total / 12 golden path / 7 holistic extension | [`journeys.yaml`](../journeys/journeys.yaml) |
| Feature flags | 93 registered / 91 active / 2 resolved | [`registry.yaml`](../flags/registry.yaml) |
| System charters | 23 Markdown documents | [`systems/`](../systems/) |
| Documentation inventory | 453 files classified | [`inventory.yaml`](../governance/inventory.yaml) |

### V1 intent versus executable evidence

Implementation means the manifest's named paths are tracked by their owning
repository. Release defaults come from the flag registry, not the deployed
environment. Readiness exposes known seeded-replay failures but remains
uncertified until a current-revision receipt exists.

| Capability | V1 intent | Implementation | Release default | Production-enabled | Readiness |
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
<!-- END auto:current-state -->

### Four-root target conformance

The [Four-Root Loop, Object, and Surface
Contract](../systems/four-root-loop-object-surface.md) is target product and
architecture doctrine, not a shipped-shell claim. It establishes Home as the
selective temporal return, Chat as the clean contribution and agency layer,
Places as substantial spatial return, and Life as governed continuity over one
shared object model. It also fixes the compounding context loop, cross-root
handoff envelope, Life's container-and-lens organization, multiplayer
placement, and the real-world engine as a cross-cutting capability rather than
a fifth surface.

The production mobile shell remains materially legacy-aligned around Trips,
Vesper, Places, and You, and the mature Concierge runtime still operates over a
Trip-centered semantic model. The current Chat, Life, and Home/Places research
and fixture packs are architectural evidence for the target; they are not
implementation or release certification. Production conformance requires an
explicit shell migration, typed adapters into canonical owners, projection and
handoff contracts, authority enforcement, and complete cross-root fixture
verification without duplicating owner truth.

As of 2026-08-29, the convergence branch has a default-off internal
compatibility shell that labels the existing Trips, Concierge, Places, and
Atlas routes Home, Chat, Places, and Life only in development or explicit
internal builds. A native semantic portfolio lab covers five selected
situations across all four roots, and a fixture-only tagged semantic result
envelope preserves exact return context. The backend shadow branch has a
bounded portfolio read plan over the reviewed semantic operation catalog. None
of these changes serves new runtime data, replaces existing owner writers,
constitutes visual selection, or certifies the production shell.

### Contribution-contract conformance

The accepted [Contribution and Consequence
Contract](../systems/contribution-and-consequence.md) is target architecture,
not a shipped-behavior claim. The accepted [Structured Contribution Use Grants
decision](../decisions/2026-08-29-adopt-contribution-use-grants.md) now refines
Source/claim/projection lifecycle, Outcome learning targets, multiplayer
purpose, affected-person roles, contextual inspection, and connected-service
boundaries. Intake v2 already preserves much of its source-bound candidate,
truth, authority, and correction structure. Ordinary Concierge memory remains
non-conforming: current prompt/tool paths can still write inferred preference,
personality, mood, emotional-investment, and silence observations without the
shared policy gate. Home, Places, Life, and new Chat input work must not treat
those legacy writes as canonical product doctrine. Use the expanded F01–F18
fixture portfolio as target requirements, not shipped-behavior evidence.

For readiness, use [Journey Status](../journeys/STATUS.md). For the bounded first
release, use the generated [V1 release contract](../release/v1-scope.md).
For human/external blockers, use [Owner Actions](../Owner%20Action%20Items.md).
Those documents own their claims; this page deliberately does not paraphrase them.
