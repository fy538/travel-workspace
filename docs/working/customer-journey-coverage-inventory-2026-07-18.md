---
doc_type: working
status: active
owner: founder / engineering
created: 2026-07-18
last_verified: 2026-07-18
expires: 2026-08-17
why_new: Inventory the expanded app against J01-J19 before changing the canonical customer journey registry.
supersedes: []
source_of_truth_for: [customer-journey-coverage-inventory-2026-07]
---

# Customer Journey Coverage Refresh — Initial Inventory

## Executive finding

The current 19-entry registry is a useful lifecycle spine, not a complete model
of the product. The app contains 89 non-dev screens plus 8 navigation layouts.
Several entries certify broad families with one parent-level signal, while
several mature product loops exist only in subsystem docs.

The immediate problem is therefore both **missing journeys** and **incorrect
certification granularity**.

## Evidence snapshot

| Evidence source | Observed state | Implication |
|---|---:|---|
| Canonical registry | 19 entries | Stable historical spine |
| Non-dev app screens | 89 | Route count is not journey count, but breadth exceeds registry ownership |
| Navigation layouts | 8 | Shell infrastructure, not customer journeys |
| Frontend journey test files | 22 | One file per parent cannot describe branch depth |
| Canonical backend scenario files | 19 | File presence currently marks the whole logic column green |
| Numbered/native journey flows | 47 | Multiple branch flows already exist but collapse to one binary visual cell |
| Atlas internal journey flows | 6 | All six sit outside the global registry despite durable contracts |
| Lived certification | 15 pass, 4 skip | J16–J19 still lack complete lived proof |

The generated matrix presently answers “does any matching file exist?” It does
not answer “did every required customer branch pass?”

## Screen-domain ownership

Every current non-dev screen is accounted for in one domain below. Counts total
89; the eight `_layout.tsx` files are excluded.

| Domain | Screens | Representative routes | Current ownership | Initial verdict |
|---|---:|---|---|---|
| Auth and onboarding | 7 | `/(auth)/*`, `/onboarding`, `/onboarding-safety`, `/` | J01, J16, README Phase 0 | Real outcome is under-owned; promote first-run trust/value |
| Invite distribution | 2 | `/invite/[slug]`, `/invite-code` | J02, J18 | Focused, but signed-out device branch is incomplete |
| Private concierge lifecycle | 4 | `/(tabs)/concierge/*`, `/conversations/create` | J01, J04, J07, J08, J13, J14, J17 | Shared dependency with no resume/scope/stop/retry owner |
| Trips portfolio and creation | 3 | `/(tabs)/trips`, `/all`, `/trip-begin` | J01, J03, J08, J12, J17 | Adequate macro ownership; needs state branches |
| Itinerary and collaboration | 9 | plan, map, details, object, changes, chat, proposal | J03, J05, J06, J08, J14, J15 | J06 is an assurance umbrella, not sufficient mutation ownership |
| Post-trip record and sharing | 4 | trip Memory, Story, photo find, story share | J11, J12 | Coherent closeout exists; media intake/share recipient are thin |
| Trip governance and settings | 7 | `/trip-info`, `/trip-settings/*`, dates, place | J02, J04, J09, J14, J15 | Organizer handoff, role epochs, mutes, and lifecycle need one owner |
| Stay and booking | 5 | accommodation, trip accommodations, booking session | J10 | Overloaded; stay ownership and provider exceptions should split |
| Costs and settlement | 5 | `/trip-expenses/*` | J10, J12, J15 | Expense creation, correction/dispute, and payment are under-modeled |
| Discover, search, and catalog | 10 | Discover, search, angle, dossier, place, venue, guide, map | J07, J17, J19 | Search-to-evaluation-to-action lacks one end-to-end owner |
| Atlas | 28 | Atlas Home plus 27 `/atlas/*` routes | J11, J12, J16, J17 | Six durable Atlas journeys are compressed into one global entry |
| Notifications | 1 | `/notifications` | J09 | Focused; branch depth should cover privacy and destination classes |
| Public and social surfaces | 4 | public place/venue, profile, story | J18, J19 | Public recipient-to-action loop remains under-owned |

## Current registry classification

| Entry class | Journeys | Finding |
|---|---|---|
| Focused customer outcomes | J02, J03, J04, J05, J07, J08, J09, J16, J17, J18 | Retain; add branch manifests |
| Broad but coherent lifecycle | J01, J12 | Retain; make first-run and closeout branches explicit |
| Overloaded product families | J10, J11, J19 | Split ownership while keeping historical IDs stable |
| Cross-cutting assurance packs | J06, J13, J14, J15 | Reference from customer journeys; reconsider global-number status later |

This means the registry currently contains about 15 customer-outcome journeys
and four assurance packs—not 19 equally scoped customer journeys.

## Overloaded journey findings

### J06 — coherence

J06 proves that Plan, Map, Details, Chat, and Changes agree after a mutation.
That is an essential projection invariant, but it cannot own the customer intent
behind every date, stay, attendance, route, proposal, and booking mutation.

**Direction:** keep J06 as an assurance pack. Each mutation journey declares a
J06 reconciliation branch.

### J10 — stay, booking, and expense

J10 currently spans candidate evaluation, per-person visibility, booking
authority, provider state, hold settlement, expense opt-in, and group cost
visibility. These have different actors, irreversible boundaries, and failure
modes.

**Direction:** retain the commercial trust-loop ID, then add focused ownership
for collaborative stay, provider/booking exceptions, and cost settlement.

### J11 — Atlas

The canonical Atlas map already defines six journeys:

1. Build the first useful Atlas.
2. Review what needs a decision.
3. Open, shape, and keep a Reading.
4. Understand and correct what Vesper learned.
5. Browse, manage, and recover Atlas history.
6. Receive one timely return.

J11 directly owns only the second path plus part of memory correction. All six
already have dedicated native flows, but the global matrix collapses them into
one binary J11 visual signal.

**Direction:** keep J11 for review-to-memory; promote the other durable outcomes
or attach them to explicit new customer journeys.

## Resolved backend evidence namespace

An adjacent backend checkout used by the workspace contained scenario files
labeled J22–J27. They were renamed on 2026-07-18 without changing behavior:

| Former label | Descriptive scenario file | Likely owner |
|---|---|---|
| J22 | `test_trip_archive_history.py` | J15 branch or trip lifecycle journey |
| J23 | `test_membership_epochs.py` | Membership/governance journey |
| J24 | `test_trip_cardinality_transitions.py` | J14 assurance + membership journey |
| J25 | `test_organizer_handoff.py` | Membership/governance journey |
| J26 | `test_active_membership_authority.py` | Membership/governance + booking/proposal branches |
| J27 | `test_group_agency_governance.py` | Group agency/governance journey |

All six renamed scenarios pass. They remain evidence, not implicit canonical
journeys, and the global registry again owns the full `JNN` namespace.

## Approved ownership expansion

The audit approved these registry entries on 2026-07-18:

| Journey | Outcome | Why it is distinct |
|---|---|---|
| J20 | First-run trust setup → first personalized value | Phase 0 is now a real multi-screen promise |
| J21 | Collaborative stay and traveler ownership | Different visibility/authority lifecycle from booking |
| J22 | Booking exception and provider handoff | Held, expired, unknown, retry, cancel, and external responsibility |
| J23 | Group costs → correction/dispute → settlement | Money authority and durable payment state deserve direct ownership |
| J24 | Group membership, organizer handoff, and agency | Existing backend depth has no canonical customer owner |
| J25 | Empty Atlas → first useful Atlas | A durable value moment independent of completing a trip |
| J26 | Atlas Reading → steer → keep → return | Authored interpretation has its own persisted lifecycle |
| J27 | Atlas provenance → correct/forget | Core trust promise across memory and originating artifacts |
| J28 | Atlas history → hide/restore/recover | Distinct long-record management and archive-reason lifecycle |

Search/evaluate/action, public recipient conversion, timely returns, and
photo/media closeout remain new branches of J07/J18/J19/J17/J12 rather than new IDs.

## What should remain a branch, not a new journey

- offline, stale, loading, and retry states;
- permission denial and unavailable media;
- organizer/member/solo persona variants;
- empty and dense versions of the same outcome;
- route aliases and legacy redirects;
- visual style variants without a distinct state transition.

## Next audit actions

1. Write branch manifests for J06, J10, and J11 as schema trials.
2. Map all 47 numbered native flows and six Atlas flows to branches.
3. Map the renamed governance evidence files to approved branch IDs.
4. Red-team the provisional candidates for overlap with J01–J19.
5. Approve the expanded registry only after branch coverage exposes the real gaps.
