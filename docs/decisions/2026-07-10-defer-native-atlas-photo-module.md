---
doc_type: decision
status: accepted
owner: founder / engineering
created: 2026-07-10
decided: 2026-07-10
why_new: Resolve the long-running Atlas V1.1 dev-client cutover ambiguity.
supersedes: []
---

# Decision: Defer the native Atlas photo module

## Context

Managed Expo supports library scanning, permissions, metadata, inbox pagination,
and dismissal. Burst identifiers, persistent change tokens, Vision dedup,
Journaling Suggestions, and full background catch-up require a custom Swift Expo
module and change the release/tooling boundary.

## Decision

Keep managed-Expo scanning as the supported V1 boundary. Do not cut over to a custom
Atlas PhotoKit module until dogfood evidence shows that duplicate quality,
incremental scanning, or background discovery materially harms the memory loop.

## Consequences

Native-quality grouping and background behavior remain deferred. The completed V1.0
work is maintained, while the implementation plan becomes historical.

## Revisit trigger

Repeated cohort failures attributable to managed-Expo limitations, plus an approved
dev-client/TestFlight migration window and required Apple entitlements.
