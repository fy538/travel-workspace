---
doc_type: current_status
status: active
owner: engineering
created: 2026-07-09
last_verified: 2026-08-09
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
| API contract | 457 paths / 507 operations / 1028 schemas | [`docs/openapi.json`](../openapi.json) |
| Canonical journeys | 28 total / 12 golden path / 7 holistic extension | [`journeys.yaml`](../journeys/journeys.yaml) |
| Feature flags | 59 registered / 58 active / 1 resolved | [`registry.yaml`](../flags/registry.yaml) |
| System charters | 20 Markdown documents | [`systems/`](../systems/) |
| Documentation inventory | 316 files classified | [`inventory.yaml`](../governance/inventory.yaml) |

### V1 intent versus executable evidence

Code evidence reports only whether the manifest's named implementation paths
exist. Default posture comes from the flag registry. Neither column is a
certification claim; Journey Status and device receipts own readiness.

| Capability | V1 intent | Code evidence | Default posture | Certification |
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
<!-- END auto:current-state -->

For readiness, use [Journey Status](../journeys/STATUS.md). For the bounded first
release, use the generated [V1 release contract](../release/v1-scope.md).
For human/external blockers, use [Owner Actions](../Owner%20Action%20Items.md).
Those documents own their claims; this page deliberately does not paraphrase them.
