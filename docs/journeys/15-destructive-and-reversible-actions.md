# 15 - Destructive And Reversible Actions

> Status: draft
> Owner: founder / engineering
> Last updated: 2026-06-29
> Primary phase: cross-cutting (trust-critical mutations)

## Product Promise

Leaving a trip, removing a member, deleting a trip, or cancelling a booking does exactly what it says — confirms first, cascades correctly, and leaves no orphaned money or ghost members. Reversible actions (undo a proposal, revert a change) restore cleanly.

## Canonical User Story

As a traveler managing a trip, I want destructive actions to be safe and predictable, so that I can leave, remove, delete, or cancel without corrupting expenses, settlement, membership, or read models.

## Why This Journey Matters

- Leave-trip, remove-member, delete-trip, and cancel-booking have no owned journey today; J11 covers only *memory* delete-restore.
- These are the highest-trust mutations: a botched cascade orphans expenses, leaves ghost members, or settles a deleted trip.
- Undo/revert (`changes` timeline) is a core product promise that must actually restore state.

## Starting State

- Persona: organizer + at least one member on a trip with expenses, a settlement balance, and an applied proposal.

## Primary Surfaces

- Routes: `/trip-settings`, `/trip-info`, `/booking/[sessionId]`, `/(tabs)/trips/[tripId]/changes`, `/trip-expenses`.
- App docs: [Booking Group Semantics](../../travel-app/docs/page-specs/booking-group-semantics.md), [Change Proposals](../../travel-app/docs/page-specs/change-proposals.md).

## Canonical Steps

1. Member leaves a trip → membership removed, the member's expense shares handled per policy, no ghost membership.
2. Organizer removes a member → cascades cleanly; settlement re-derives; removed member loses access.
3. Delete a trip → trip + members + itinerary + blocks + expenses cascade; nothing dangles (no settlement on a deleted trip).
4. Cancel a booking / hold → the hold releases, no orphaned expense, status reflects cancellation honestly.
5. Undo / revert an applied proposal in the changes timeline → read models (plan/map/home) restore to the prior coherent state.
6. Every destructive action confirms before committing; irreversibility is stated where it applies.

## Expected Outcome

- Each destructive action cascades to membership, expenses, settlement, and read models with no orphans.
- Reversible actions restore the prior state coherently across surfaces.
- Confirmation precedes irreversible commits.

## Must Never Happen

- A deleted trip leaves orphaned expenses, a dangling settlement, or ghost members.
- Removing/leaving a member corrupts the settlement balance for the rest.
- A cancelled booking leaves a phantom hold or expense.
- Undo/revert renders "reverted" but leaves a stale read model.
- A destructive action commits without confirmation.

## AI Trace Prompt

```text
Trace leave-trip, remove-member, delete-trip, cancel-booking, and undo/revert from the API mutation through every dependent table (members, expenses, settlement, itinerary, read models). Identify any orphaned row, ghost membership, settlement-on-deleted-trip, or undo that leaves stale state.
```

## First Automation Target

Persona-cert (lived): create a throwaway trip with a member + expense as the seeded persona; delete it; assert the trip and all dependent rows (members, itinerary, blocks, expenses) are gone (no orphans). Separately: a member leaves; assert membership removed and settlement re-derives.
