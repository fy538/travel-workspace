---
doc_type: decision
status: accepted
owner: founder / product / engineering
created: 2026-08-12
decided: 2026-08-12
why_new: Records the retirement of Discover and Atlas as product concepts so implementation, release scope, and documentation converge on the three-root mobile IA.
supersedes: []
source_of_truth_for: [discover-atlas-product-retirement, mobile-root-information-architecture]
---

# Decision: retire Discover and Atlas as product surfaces

## Context

The app already exposes Trips, Vesper, and Places as its three visible mobile
roots. Discover and Atlas remained registered chiefly for legacy routing, but
their old names still appeared in active journeys, release scope, onboarding,
background producers, documentation, and new implementation work. That made
the product appear to have more owners than it does and kept duplicate,
competing loops alive.

The durable product model does not require a root for every concept. Place
exploration belongs to Places; personal controls belong to You; Trip history
and story belong to Trips; Vesper uses personal memory as governed context.

## Decision

Discover and Atlas are retired product concepts.

The active mobile information architecture is:

| Owner | Responsibility |
|---|---|
| Trips | Plans, group coordination, execution, history, and story |
| Vesper | Intent, judgment, proposals, orchestration, and explanation |
| Places | Exploration, search, map, editorial context, and saved places |
| You | Identity, people, preferences, privacy, permissions, and memory controls |

Discover capabilities move to Places or Vesper. Atlas capabilities either move
to You, Trips, or the internal Personal Memory substrate, or are retired. New
user-facing copy, routes, APIs, journeys, release capabilities, notifications,
or background producers may not introduce either product name.

Existing user data and historical telemetry remain protected. A legacy route,
API, persisted payload, or storage namespace may remain only as explicitly
registered compatibility, with a reason, canonical destination, measurement,
and removal trigger. Internal names do not imply an active product surface.

## Consequences

The team must complete the migration rather than merely hide two tabs. The
release contract, journeys, Maestro suite, documentation, endpoints, and
background workers will contract around the remaining product loops. We retain
only neutral personal-memory reads and controls needed by You and Vesper; this
decision does not authorize recreating Atlas under another name.

## Revisit trigger

Supersede this decision only if validated evidence shows that a distinct,
user-chosen memory or editorial destination materially improves a core loop and
cannot be coherently owned by Trips, Vesper, Places, or You.
