# 02 - Concrete Trip Creation And Invite

> Status: draft  
> Owner: founder / engineering  
> Last updated: 2026-06-06  
> Primary phase: trip creation / group formation

## Product Promise

An organizer can create a real trip, invite people, and see everyone land in the same shared workspace with the right membership and permissions.

## Canonical User Story

As an organizer, I want to create a trip and invite my friends, so that the group has one shared place to plan.

## Why This Journey Matters

- Shared membership is the foundation for group planning, privacy routing, booking, expenses, and notifications.
- Invite flows are easy to break with auth detours, stale tokens, and current-user assumptions.
- This is already a reliability golden path and should become a full product journey.

## Starting State

- Persona: organizer user with no current active trip selected.
- Trip state: no relevant trip or an existing planning trip for comparison.
- Fixture: `trip-lisbon-26` for existing workspace checks; mock invite APIs for create/view/accept.
- Permissions: auth may be signed in or invitee may need sign-in detour.

## Primary Surfaces

- Routes: `/trip-begin`, `/(tabs)/trips/[tripId]`, `/trip-info?tripId=`, `/invite/[token]`.
- App docs: [Canonical User Flow Map](../../travel-app/docs/user-flows/canonical-flow-map.md), [Trip Page](../../travel-app/docs/page-specs/trip-page.md).
- Reliability trace: [Create Trip And Invite Group](../reliability/traces/create-trip-and-invite-group.md).
- Existing anchors: `__tests__/offline/goldenPath.test.ts`, `__tests__/hooks/useCreateInvite.test.ts`, `__tests__/hooks/useTripInvites.test.ts`, `__tests__/screens/invite-landing.smoke.test.tsx`.

## Canonical Steps

1. Organizer starts a concrete trip from `/trip-begin`.
2. App creates the trip and routes to Trip Folio Home.
3. Organizer opens trip info or invite management.
4. Organizer creates an invite link.
5. Invitee opens `/invite/[token]`.
6. If signed out, invitee signs in and returns to invite landing.
7. Invitee accepts and lands in the correct trip.
8. Organizer and invitee both see membership reflected in the workspace.

## Expected Outcome

- User-visible state: organizer sees invite as active/pending; invitee sees correct trip title and accepts successfully.
- Data state: trip id is stable; organizer membership exists; invite token maps to one trip; accept creates member row.
- Cross-surface coherence: Trips list, Trip Info, Group Chat, and Notifications agree on membership.
- Trust state: invite link does not expose hidden personal data.

## Must Never Happen

- Invite accepts into the wrong trip.
- Auth detour loses the invite token.
- Consumed/expired invite renders as active.
- Non-members can see private trip data before accepting.
- Organizer sees fake success when invite creation failed.

## AI Trace Prompt

```text
Trace trip creation and invite acceptance across app routes, invite hooks, mock API methods, backend invite endpoints, auth detours, and membership reads. Report any stale currentTripId assumptions or route params that could send the user to the wrong workspace.
```

## First Automation Target

Extend the existing offline golden path into a screen-level mock walkthrough:

- create invite
- view invite landing
- accept invite
- verify trip member count changes
- verify route lands on `routes.tripDetail(tripId)`

