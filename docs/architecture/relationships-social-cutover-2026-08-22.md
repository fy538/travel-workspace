---
title: Relationships and place-social cutover
status: active
owner: product-and-platform
created: 2026-08-22
date: 2026-08-22
last_verified: 2026-08-22
doc_type: contract
why_new: Define the clean-break domain and rollout contract for place-aware multiplayer.
expires: 2026-09-22
scope: relationships, addressed handoffs, occasions, outcomes, and quiet delivery
---

# Relationships and place-social cutover

> Status: execution contract
> Updated: 2026-08-22
> Scope: clean-break alpha social loop

## Outcome

Vesper's social product is a quiet, place-aware relationship loop. A person
can leave a grounded observation for one explicitly named person, that person
can encounter it in Chat or at the exact place, and the pair can turn it into
an optional Occasion. What happened and what it meant remain separate for each
person.

This is not a feed, follower graph, public review system, or social inbox.

```text
chat / photo / place observation
          -> addressed place handoff
          -> keep, dismiss, or open together
          -> occasion opening + optional commitment
          -> occurrence
          -> private outcomes and explicit relational continuity
          -> a later opening or deliberate silence
```

## Architectural decisions

1. `relationships` is a first-class clean-break domain. It owns explicit
   people/circle scope, addressed handoffs, permissions, and relationship-place
   continuity. It does not own world identity, plans, occasions, or memory.
2. New relationship records reference the UUID world entity from the clean-break
   graph. Legacy integer `places.id` is a read-only adapter during the local
   transition and is not a new runtime authority.
3. A handoff is an addressed relationship-place event, not a post, message
   attachment, generic memory, or engagement object.
4. `open_together` creates an Occasion opening through the application
   transaction boundary. It never creates a Trip, itinerary, booking,
   attendance claim, or completed event.
5. Viewing, opening, or keeping a handoff never creates memory. A shared
   occurrence or an explicit carry-forward is required.
6. Shared occurrence facts and private outcomes are separate records and
   projections. Neither person's private interpretation is copied to the other.
7. A sender may propose a delivery mode, but place-timed delivery requires the
   recipient's permission. No background location push is part of the first
   release.
8. Every mutation is capability checked, revision checked, idempotent, and
   receipt backed. Revoked or expired material is content-redacted.
9. Product surfaces remain Chat, Places, Plans/Occasions, Home, and You/My
   World. There is no social tab or general feed.
10. Public contributions, stranger matching, likes, follower counts,
    relationship scores, and ranked social notifications are out of scope.

## Domain ownership

```text
backend/domains/world/          UUID identity and provenance
backend/domains/intake/         artifacts and anchors
backend/domains/relationships/  people/circles, handoffs, permissions
backend/domains/plans/          personal horizons
backend/domains/occasions/      bounded shared contexts
backend/domains/commitments/    shared consequences and authority
backend/domains/lived/          occurrence, outcomes, continuity
backend/domains/attention/      openings, decisions, delivery, silence
backend/application/             cross-domain commands and ports
backend/platform/                persistence, auth, providers, telemetry
```

Domain packages do not import API routes or another domain's implementation.
Cross-domain transitions use application services, typed ports, or outbox
events. The existing `backend/core/db/place_handoffs.py` implementation is a
transitional adapter until the UUID relationship writer is active. The dark
UUID namespace lives at `backend/api/routes/relationship_handoffs.py`; its
`open_together` command uses `backend/application/relationship_openings.py` to
create one linked `occasions` row and two participant rows atomically. The
`relationship_handoff_occasion_openings` table makes the bridge replayable.

## Core records

### PlaceHandoff

- sender and recipient user IDs;
- UUID `world_entity_id`;
- exact pair conversation;
- source anchor/artifact reference;
- bounded message or interpretation;
- explicit permission envelope;
- `send_now` or recipient-authorized `place_pull` mode;
- lifecycle: available, kept, dismissed, revoked, expired;
- idempotency key and revision;
- event receipt chain.

### OccasionOpening

- source handoff;
- exact pair or explicit circle;
- optional world entity and optional time window;
- opening/proposed lifecycle;
- no implied booking, attendance, or completion.

### Occurrence and outcomes

- one shared occurrence only when evidence or explicit confirmation supports it;
- one private outcome per participant;
- an optional explicit relationship-place carry-forward;
- correction/retraction cascades to derived projections without deleting the
  source receipt.

## Product sequence

This is a staged exposure sequence for one social expression. The relationship,
Occasion, authority, and plurality architecture is derived from the full
personal-and-multiplayer portfolio; later exposure stages may be researched and
designed before send-now ships.

### Send-now alpha

The first release begins in Chat after a useful action such as translation,
photo interpretation, or place explanation. Vesper may offer “Leave this for…”
when the contextual engine has a grounded place and the user has an existing
relationship. The user chooses the exact recipient and confirms the place.

The recipient sees a native Chat card with at most two actions:

- primary: `Open together`;
- secondary: `Keep`;
- quiet overflow: `Not for me` / dismiss.

Non-response is valid and does not create a notification debt.

### Place pull

After send-now is stable, recipients may opt into place pull. A bounded
“From your people” module appears only for the exact world entity and only for
the current viewer. It never exposes the recipient's location to the sender.

### Occasion bridge

`Open together` creates a lightweight Occasion opening and optionally a shared
Commitment when time/place are explicit. Plans and Home may project that
opening, but Trip/itinerary tables do not become authoritative again.

### Continuity

After an occurrence, each person can retain a different meaning. Home may later
surface one relational opening, one second-occasion continuation, or silence.

## API and app boundary

The mobile contract now has a typed data seam for UUID create/read/list/action
operations at `/api/relationships/place-handoffs`, behind
`RELATIONSHIP_UUID_HANDOFFS_ENABLED`. The app seam lives in
`travel-app/data/relationshipPlaceHandoffs.ts`, but no visual surface invokes
it yet;
the existing recipient card still uses its legacy adapter until the sender
card and recipient pull surface switch authorities together. Place pull
remains separately permissioned by the handoff envelope and is not a push.

Chat cards continue to use opaque server-resolved action references. A resolver
returns a typed `place_handoff_action` intention after rechecking membership,
actor, handoff state, and allowed action. The mobile client never constructs a
mutation URL from card metadata.

There is no handoff detail screen in alpha. The card, Place module, and
Occasion projection are the product surfaces.

## Acceptance portfolio

The cutover is not complete until all of these execute with storage, API,
mobile, privacy-negative, receipt, and replay assertions:

1. translated menu -> addressed handoff;
2. exact-place pull for a recipient;
3. pair opens a dinner Occasion;
4. group decision keeps a private constraint private;
5. invitation cold-starts an Occasion;
6. one occurrence yields two private outcomes;
7. sender revokes before encounter;
8. source correction/retraction;
9. second occasion uses explicit continuity;
10. the engine chooses silence when no grounded opening exists.

## Rollout

1. All flags off; local fixtures only.
2. Internal dogfood, UUID send-now API and Occasion bridge in acceptance only.
3. Internal dogfood, recipient-controlled place pull.
4. Occasion bridge.
5. Outcome and second-occasion continuity.
6. Home relational projection in shadow mode.
7. Separate evaluation for any place-timed push.

Postgres remains canonical truth. Qdrant is a disposable projection rebuilt
from the new durable graph. No cloud promotion or public activation is implied
by this contract.
