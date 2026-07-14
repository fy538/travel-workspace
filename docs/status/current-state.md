---
doc_type: current_status
status: active
owner: engineering
created: 2026-07-09
last_verified: 2026-07-09
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
| API contract | 360 paths / 401 operations / 777 schemas | [`docs/openapi.json`](../openapi.json) |
| Canonical journeys | 19 total / 12 golden path / 7 holistic extension | [`journeys.yaml`](../journeys/journeys.yaml) |
| Feature flags | 56 registered / 55 active / 1 resolved | [`registry.yaml`](../flags/registry.yaml) |
| System charters | 20 Markdown documents | [`systems/`](../systems/) |
| Documentation inventory | 226 files classified | [`inventory.yaml`](../governance/inventory.yaml) |
<!-- END auto:current-state -->

For readiness, use [Journey Status](../journeys/STATUS.md). For the bounded first
release, use [V1 Scope](../working/mvp-scope-and-flag-manifest-2026-06-30.md).
For human/external blockers, use [Owner Actions](../Owner%20Action%20Items.md).
Those documents own their claims; this page deliberately does not paraphrase them.
