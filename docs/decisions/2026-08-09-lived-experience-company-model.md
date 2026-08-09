---
doc_type: decision
status: accepted
owner: founder / product
created: 2026-08-09
decided: 2026-08-09
why_new: Records the company-level identity change from a travel-concierge category to a proactive multiplayer AI for place-grounded lived experiences while preserving group travel as the launch wedge.
supersedes:
  - travel-agent/docs/archive/thesis-evolution/2026-04-18-place-aware-travel-concierge.md
  - travel-agent/docs/archive/thesis-evolution/2026-07-29-travel-world-model.md
source_of_truth_for: [company-product-model-adoption, travel-wedge-boundary]
---

# Adopt the lived-experience company model

## Context

Vesper began as an AI-assisted travel planner and became a place-aware travel
concierge spanning planning, group coordination, on-trip adaptation, place
interpretation, booking, and memory. Founder dogfood showed that even a
competent itinerary was insufficient: it did not provide the situated judgment
of something that knows the people, place, current conditions, and consequences
and remains responsible as reality changes.

Subsequent product and engineering work exposed a more general system already
forming underneath the Trip: person-scoped context, relationship and group
state, place identity and provenance, spatial and temporal grounding, weather
and availability, shared Plans, bounded agency, proactive attention, and
outcome-backed memory. Familiar local occasions exercise the same system at a
smaller scale and provide a more frequent, auditable test of judgment.

## Decision

Vesper's company identity is no longer AI travel planning or a travel
concierge. Vesper is a proactive, multiplayer, place-aware AI for real-world
experiences. In human terms, it notices what becomes possible around people and
helps them make it happen.

The canonical product model is:

```text
Experience = what someone or a group wants to live
Plan       = the temporary structure that helps it happen
Trip       = a sophisticated Plan type for multi-day travel and logistics
Move       = one low-commitment action that may begin or continue an experience
Vesper     = the intelligence that understands, shapes, acts, adapts, and learns
```

Multiplayer means governed shared agency: each person may retain private
context, the people involved share one coherent Plan, authority is explicit,
and Vesper keeps the shared object true as circumstances change.

Proactivity means earned noticing. Vesper may push only when it can explain why
this person, why this place, why now, and what can happen next. Silence is the
correct output when that bar is not met.

Group travel remains the launch wedge, initial proving ground, distribution
event, and monetization concentration. The current repositories and first
release may remain substantially trip-centered while the underlying contracts
generalize. Category adoption does not authorize an unbounded local feed or a
roadmap expansion without dogfood and external evidence.

## Consequences

- Company-level documents lead with people, relationships, places, lived
  experiences, multiplayer, and grounded action—not itinerary generation.
- Trip-specific contracts continue to use Trip and itinerary language where it
  is operationally correct.
- Architecture documents distinguish the generalized company model from the
  current travel-wedge implementation instead of claiming unshipped parity.
- Place intelligence preserves facts, perspectives, conditional judgment,
  provenance, freshness, and disagreement as different kinds of evidence.
- The moat is not architecture alone. Defensibility must be demonstrated by a
  closed outcome loop that makes a later experience materially better.
- Superseded theses remain immutable historical evidence with explicit links to
  current canon.

## Revisit trigger

Revisit the breadth or wording of this model if repeated external use fails to
show that outcome memory improves a second occasion, governed multi-person
context improves a shared experience, or local trust transfers into travel.
Revise through a new decision; do not rewrite this record to imply the newer
position was always held.
