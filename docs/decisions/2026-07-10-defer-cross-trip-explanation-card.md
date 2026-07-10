---
doc_type: decision
status: accepted
owner: founder / engineering
created: 2026-07-10
decided: 2026-07-10
why_new: Separate the shipped cross-trip substrate from an unvalidated explanatory UI commitment.
supersedes: []
---

# Decision: Defer the dedicated cross-trip explanation card

## Context

Cross-trip thread storage, computation, endpoint, types, and app client exist, but no
Trip Home component consumes them. Graph Legibility prefers personalization through
better output over labels that narrate what the system knows.

## Decision

Do not make the dedicated “from your Lisbon trip” card part of V1. Certify cross-trip
recall and privacy through J17 and let the concierge demonstrate familiarity quietly.

## Consequences

The existing backend may remain dark/unused without implying the UI is incomplete
for launch. The old build plan is archived rather than treated as current scope.

## Revisit trigger

Cohort users fail to perceive compounding value across trips, or explicitly ask why
a recommendation fits, and Atlas/“Why this?” cannot satisfy that need.
