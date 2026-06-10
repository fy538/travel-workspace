# 05 - Group Planning To Proposal To Plan Mutation

> Status: draft  
> Owner: founder / engineering  
> Last updated: 2026-06-06  
> Primary phase: collaborative planning

## Product Promise

Vesper can help a group make a decision, turn it into a clear proposal, apply it to the plan, and explain or undo what changed.

## Canonical User Story

As a group planning a trip, we want to ask for a change, review Vesper's proposal, vote or resolve it, and see the itinerary update clearly.

## Why This Journey Matters

- This is the central Advise -> Propose -> Act loop.
- It crosses chat, proposal detail, plan state, change history, notifications, and map invalidation.
- Mock mode covers the happy path, but real acceptance/apply behavior is a known drift hotspot.

## Starting State

- Persona: organizer plus at least one member.
- Trip state: pre-trip with itinerary blocks and at least one proposed change.
- Fixture: `trip-lisbon-26` or Porto planning trip with open proposals.
- Permissions: organizer/member role matters.

## Primary Surfaces

- Routes: `/(tabs)/trips/[tripId]/chat`, `/(tabs)/trips/[tripId]/plan`, `/(tabs)/trips/[tripId]/changes`, `/notifications`.
- App docs: [Change Proposals](../../travel-app/docs/page-specs/change-proposals.md), [Trip Group Chat](../../travel-app/docs/page-specs/trip-group-chat.md), [Trip Plan](../../travel-app/docs/page-specs/trip-plan.md).
- Reliability trace: [Proposal Review And Plan Mutation](../reliability/traces/proposal-review-and-plan-mutation.md).
- Existing anchors: `__tests__/data/proposals.test.ts`, `__tests__/components/plan/ProposalReviewSheet.test.tsx`, `__tests__/components/chat/VoteWidgetCardEmpty.test.tsx`, backend proposal API/apply tests.

## Canonical Steps

1. Open group chat for a planning trip.
2. Ask Vesper to change a dinner, time, activity, or route.
3. Vesper creates a proposal with affected ids and public-safe reason.
4. Member votes or organizer resolves.
5. Proposal detail shows accepted/rejected state.
6. Plan reflects the accepted mutation or reassures that rejected plan stayed.
7. Changes screen shows recent change with undo/revert when safe.
8. Notification/activity receipt routes back to the right object.

## Expected Outcome

- User-visible state: proposal is understandable in under 10 seconds and inspectable in detail.
- Data state: proposal status, votes, affected ids, resolution, and applied/reverted state are stable.
- Cross-surface coherence: Chat, Plan, Home, Changes, Map, and Notifications agree.
- Trust state: users can distinguish proposed, accepted, rejected, and reverted changes.

## Must Never Happen

- Accepted proposal silently mutates the plan without a visible receipt.
- Rejected proposal disappears without confirming the original remains.
- Proposal detail leaks private source context.
- Retry creates duplicate votes or duplicate applied changes.
- Revert says success but Plan/Map still show the changed state.

## AI Trace Prompt

```text
Trace the proposal lifecycle from group chat intent through proposal creation, vote, resolve, plan mutation, change history, notification routing, and revert. Report API methods, mock behavior, backend endpoints, idempotency protections, and read-model invalidation.
```

## First Automation Target

Add or extend deterministic tests for:

- vote idempotency
- resolve accepted/rejected
- plan state after accept
- recent changes after accept/revert
- notification routing into proposal/chat/plan

