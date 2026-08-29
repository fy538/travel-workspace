---
doc_type: decision
status: accepted
owner: founder / architecture / backend
created: 2026-08-29
decided: 2026-08-29
last_verified: 2026-08-29
decision_class: founder-only architecture
why_new: Records implementation of the shared semantic spine after Wave 0 closed the whole-product contract, while preserving the shadow-only and runtime-off boundary.
related:
  - working/whole-product-v1-conformance-workbook-2026-08-29.md
  - working/agentic-semantic-facade-engineering-package-2026-08-29.md
  - working/agentic-chat-cross-surface-fixture-pack-2026-08-29.md
  - systems/four-root-loop-object-surface.md
---

# Execute Wave 1: shared semantic spine

## Decision

Wave 1 is implemented as an additive, shadow-only contract extension in the
backend. It does not change the Concierge prompt, served tools, owner writers,
mobile surfaces, or the default-off facade flag.

The existing `ResourceRef` remains the one canonical resolved owner identity.
Unresolved client hints remain `ResourceLocator` values and cannot acquire a
revision, canonical path, or authority merely because they were supplied by a
caller.

## Contract seams now present

`AgenticTurnFrame` is versioned as `agentic-turn-shadow-v2` and carries:

- typed `AuthoritySource` provenance, kept separate from contribution policy;
- one `OperationContract` per selected semantic operation, including owner
  kind, effect, authority boundary, phases, postconditions, and return modes;
- `ReadbackContract` for canonical-owner status and receipt references;
- `UncertaintyContract` for unresolved and unavailable conditions;
- `CorrectionLink` for a relation-level target and invalidated projections; and
- `ReceiptLink` for canonical receipt correlation without merging the control
  plane execution receipt with the owner receipt.

The compiler derives authority-source kind from the existing contribution
gesture basis unless a server-issued typed source is supplied. It derives
uncertainty from unresolved entry locators and unavailable catalog operations;
it never fabricates a successful readback. Entry, selection, agency ceiling,
return contract, contribution decision, operation metadata, and receipts remain
distinct objects linked by the frame.

## Fixture coverage

The offline portfolio is now `agentic-turn-portfolio-v2` and compiles A01–A18.
A13–A18 cover quiet Home value, an everyday Bring contribution, asynchronous
social value, post-return re-entry, Life re-finding, and longitudinal
compounding. Selector assertions cover all eighteen cases, and contract tests
assert the typed links and conservative uncertainty behavior.

## Exit evidence

- focused semantic facade, contract, selector, and contribution tests pass;
- all eighteen fixtures compile without new ad hoc enum values;
- contribution treatment, action authority, and owner/execution receipts are
  still separate contracts; and
- runtime behavior remains unchanged while `CONCIERGE_AGENTIC_FACADE_MODE` is
  `off`.

## Explicit non-goals

This decision does not add owner readers, expose contracts through OpenAPI,
replace itinerary writers, implement a generalized Monitor owner, or enable
dogfooding. Those remain later waves gated by surface stability and owner
readback evidence.
