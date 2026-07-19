---
doc_type: canon
status: active
owner: founder / engineering
created: 2026-07-18
last_verified: 2026-07-19
why_new: Shared and personal lodging now have distinct ownership, visibility, and itinerary contracts that exceed J10's booking loop.
source_of_truth_for: [journey-J21]
---

# 21 — Collaborative Stay and Traveler Ownership

## Product Promise

The group can establish where the trip is based while every traveler retains
control over personal lodging details.

## Canonical User Story

As a traveler, I want shared and personal stays to have clear owners and scope,
so that the group can coordinate without exposing private lodging details.

## Starting State and Surfaces

- Planning group trip with no stay or mixed shared/personal stays.
- Routes: `/trip-accommodations/*`, `/accommodation/[id]`, Trip Details Stay.
- J22 owns provider booking state; J06 owns projection reconciliation.

## Canonical Steps

1. Open Stay from Trip Details.
2. Add or choose a shared base or personal stay.
3. Assign the correct traveler/scope and review dates/location.
4. Edit, replace, or remove the stay under the correct authority.
5. Return to Stay and Itinerary; group-safe truth agrees everywhere.

## Required Branches

| Branch | Path | Required evidence |
|---|---|---|
| `J21.B01` | Organizer creates/edits shared trip base | `FE`, `BE`, `VIS`, `LIVE` |
| `J21.B02` | Traveler creates/edits own personal stay | `FE`, `BE`, `VIS`, `LIVE` |
| `J21.B03` | Organizer assists another traveler | `FE`, `BE`, `VIS` |
| `J21.B04` | Unrelated member cannot view/mutate private slot | `FE`, `BE`, `VIS`, `LIVE` |
| `J21.B05` | Candidate versus manual stay stays honestly sourced | `FE`, `BE`, `VIS` |
| `J21.B06` | Date mismatch, replace, and remove reconcile via J06 | `FE`, `BE`, `VIS` |

## Must Never Happen

- A group stay silently becomes a private stay or vice versa.
- A member sees another traveler's private payment or lodging detail.
- Editing a stay creates a duplicate itinerary object.
- Removing lodging implies a provider reservation was cancelled.

## First Automation Target

Three-person fixture: organizer adds a group base, member adds a private stay,
and a second member can see the base but neither read nor mutate the private row.

## Certification Notes

- The traveler's personal slot overrides the shared base only for that
  traveler. Parallel member slots are not rendered as sequential stay legs.
- Personal slots default private; the traveler can explicitly share one with
  the group. A shared base cannot be made ownerless-private.
- Organizers can create or assist a current member's slot, but cannot attach a
  personal stay to an account outside the trip roster.
- Removing a recorded stay retires the in-app lodging row and its derived
  projections. It does not claim that a provider reservation was cancelled.
- `48b-journey-21-stay-reconcile.yaml` certifies the destructive boundary and
  proves the removed stay disappears after the canonical read model refreshes.
- Mock and real-mode deletion now remove the row from the shared accommodation
  cache before invalidation, preventing a successful removal from visibly
  resurrecting while projections refresh.
