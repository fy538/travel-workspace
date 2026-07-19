# 15 - Destructive And Reversible Actions

> Status: draft
> Owner: founder / engineering
> Last updated: 2026-07-19
> Primary phase: cross-cutting (trust-critical mutations)

## Product Promise

Leaving a trip, removing a member, archiving or cancelling a trip, and releasing a hold or cancelling a booking do exactly what they say: confirm first, name the consequence, preserve what they promise to preserve, and leave no orphaned money or ghost members. Reversible actions (recover an archive, undo a proposal, revert a change) restore cleanly.

Permanent trip deletion is deliberately narrow: only an unnamed, undated,
unshared solo ideation draft with no itinerary, invite, booking work, costs, or
conversation can pass the server preflight and atomic delete. Any meaningful
trip must use archive/recover or trip cancellation so durable history remains.
Account and personal-data deletion belongs to J16.

## Canonical User Story

As a traveler managing a trip, I want destructive and reversible actions to be safe and predictable, so that I can leave, remove, archive, recover, cancel, release, or revert without corrupting expenses, settlement, membership, or read models.

## Why This Journey Matters

- Leave-trip, remove-member, trip lifecycle, and booking/hold cancellation need one owned trust journey; J11 covers only *memory* delete-restore.
- These are the highest-trust mutations: a botched cascade can orphan expenses, leave ghost members, or misstate what remains available.
- Undo/revert (`changes` timeline) is a core product promise that must actually restore state.

## Starting State

- Persona: organizer + at least one member on a trip with expenses, a settlement balance, and an applied proposal.

## Primary Surfaces

- Routes: `/trip-settings`, `/trip-info`, `/booking/[sessionId]`, `/(tabs)/trips/[tripId]/changes`, `/trip-expenses`.
- App docs: [Booking Group Semantics](../../travel-app/docs/page-specs/booking-group-semantics.md), [Change Proposals](../../travel-app/docs/page-specs/change-proposals.md).

## Canonical Steps

1. Member leaves a trip → membership removed, the member's expense shares handled per policy, no ghost membership.
2. Organizer removes a member → cascades cleanly; settlement re-derives; removed member loses access.
3. Archive/recover or cancel a trip → the app names what closes and what remains; trip cancellation never claims to cancel a provider reservation.
4. Cancel a booking / hold → the hold releases, no orphaned expense, status reflects cancellation honestly.
5. Undo / revert an applied proposal in the changes timeline → read models (plan/map/home) restore to the prior coherent state.
6. Every destructive action confirms before committing; irreversibility is stated where it applies.
7. Delete a truly empty solo draft → server preflight confirms the absence of
   durable activity, then the atomic endpoint permanently removes it.

## Expected Outcome

- Each supported destructive action updates membership, expenses, settlement, and read models with no orphans.
- Reversible actions restore the prior state coherently across surfaces.
- Confirmation precedes irreversible commits.

## Must Never Happen

- The app permanently deletes a named, dated, shared, planned, booked,
  cost-bearing, or conversation-linked trip.
- Removing/leaving a member corrupts the settlement balance for the rest.
- A cancelled booking leaves a phantom hold or expense.
- Undo/revert renders "reverted" but leaves a stale read model.
- A destructive action commits without confirmation.

## AI Trace Prompt

```text
Trace leave-trip, remove-member, archive/recover, trip cancellation, booking/hold cancellation, and undo/revert from the API mutation through every dependent table and read model. Identify any orphaned row, ghost membership, provider-cancellation overclaim, or undo that leaves stale state. Treat hard trip deletion as a gap unless an atomic API contract is added first.
```

## Certification Boundary

- Contract and lived backend coverage certify self-removal, organizer removal, access revocation, group-profile invalidation, notification cleanup, idempotent not-found behavior, and the last-organizer guard.
- Dedicated native visual flows certify member-removal confirmation, the trip-cancellation preservation/provider boundary, and the distinction between releasing an unpaid hold and cancelling a booked reservation.
- Proposal revert remains covered by its shared J05 logic/lived lifecycle. A stable native revert-control selector is still an explicit follow-up; J15 does not claim a dedicated revert screenshot yet.
- Empty-draft deletion is certified through the server preflight, exact
  confirmation literal, row lock + same-transaction recheck, post-delete read,
  and the app's race-to-archive recovery state. Meaningful-trip rejection is a
  separate required assertion.

## Automation Target

Keep the backend removal cascade, empty-draft deletion contract, and native
confirmation flows as the regression gate. Never broaden permanent deletion
to meaningful trips without a separately designed cascade, retention policy,
and orphan-proof certification pack.
