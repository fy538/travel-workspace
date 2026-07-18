---
doc_type: canon
status: active
owner: founder / engineering
created: 2026-07-18
last_verified: 2026-07-18
why_new: Membership epochs, organizer handoff, room authority, and history preservation form one unowned group lifecycle.
source_of_truth_for: [journey-J24]
---

# 24 — Group Membership and Agency Governance

## Product Promise

Joining, leaving, rejoining, changing roles, and changing Vesper's room authority
update current access without rewriting shared history.

## Canonical User Story

As a group traveler, I want current roles and Vesper authority to be legible and
auditable, so that history remains trustworthy while the roster changes.

## Starting State and Surfaces

- Solo or group trip with at least one organizer and a shared room when grouped.
- Routes: `/trip-info`, `/trip-settings/permissions`, group Chat, invite flow.
- J02/J18 own initial invite acceptance; J14/J15 remain assurance packs.

## Canonical Steps

1. Move from solo to group and establish the shared room.
2. Change role, shared-plan owner, room mute, or personal mute.
3. Hand organizer authority to a successor where required.
4. Leave/remove and later rejoin using a new membership epoch.
5. Confirm current access changes while immutable message/audit history remains.

## Required Branches

| Branch | Path | Required evidence |
|---|---|---|
| `J24.B01` | Solo→group→solo→group room lifecycle | `FE`, `BE`, `VIS`, `LIVE` |
| `J24.B02` | Leave/rejoin membership epochs preserve attribution | `FE`, `BE`, `VIS`, `LIVE` |
| `J24.B03` | Promote/demote and shared-plan-owner transfer | `FE`, `BE`, `VIS`, `LIVE` |
| `J24.B04` | Atomic organizer handoff and last-organizer guard | `FE`, `BE`, `VIS`, `LIVE` |
| `J24.B05` | Demotion/departure fences uncommitted work | `FE`, `BE`, `VIS` |
| `J24.B06` | Room mute shared/audited; personal mute private | `FE`, `BE`, `VIS`, `LIVE` |
| `J24.B07` | Invite attention/intake follows current authority | `FE`, `BE`, `VIS` |

## Must Never Happen

- Historical creator provenance grants current organizer authority.
- Rejoin reopens an old membership epoch or rewrites message attribution.
- Dormant room contributes unread/proactive work while the trip is solo.
- A personal mute becomes a group audit event or attribution leak.

## First Automation Target

Promote the six existing archive/membership/cardinality/handoff/authority/agency
backend scenarios into this branch map, then add a two-account native roster walk.
