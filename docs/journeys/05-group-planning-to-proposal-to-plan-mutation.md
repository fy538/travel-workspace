# 05 - Group Planning To Proposal To Plan Mutation

> Status: draft  
> Owner: founder / engineering  
> Last updated: 2026-07-16
> Primary phase: collaborative planning + direct itinerary edit

## Product Promise

Vesper can help a group make a decision, turn it into an exact itinerary
operation, preserve the coherence of the surrounding trip, and make the outcome
understandable and recoverable.

## Canonical User Story

As a group planning a trip, we want to ask for a change, review Vesper's proposal, vote or resolve it, and see the itinerary update clearly.

## Why This Journey Matters

- This is the central Advise -> Propose -> Act loop.
- It crosses private/group intent, proposal detail, itinerary policy, operation
  commit, provider consequences, history, notifications, and List/Map coherence.
- Mock mode covers the happy path, but real acceptance/apply behavior is a known drift hotspot.

## Starting State

- Persona: organizer plus at least one member.
- Trip state: pre-trip with itinerary blocks and at least one proposed change.
- Fixture: `trip-lisbon-26` or Porto planning trip with open proposals.
- Permissions: organizer/member role matters.

## Primary Surfaces

- Routes: trip room/private Vesper entry, the canonical Itinerary List/Map faces,
  stop inspection/change flow, Review Stack, Trip Details → Changes, and
  notification deep links.
- App docs: [Change Proposals](../../travel-app/docs/page-specs/change-proposals.md), [Trip Group Chat](../../travel-app/docs/page-specs/trip-group-chat.md), [Trip Plan](../../travel-app/docs/page-specs/trip-plan.md).
- Reliability trace: [Proposal Review And Plan Mutation](../reliability/traces/proposal-review-and-plan-mutation.md).
- Existing anchors: `__tests__/data/proposals.test.ts`, `__tests__/components/plan/ProposalReviewSheet.test.tsx`, `__tests__/components/chat/VoteWidgetCardEmpty.test.tsx`, backend proposal API/apply tests.

## Canonical Steps

### Track A — Vesper proposal (group Advise → Propose → Act)

1. Open group chat for a planning trip.
2. Ask Vesper to change a dinner, time, activity, or route.
3. Vesper creates a proposal with affected ids and public-safe reason.
4. Member votes or organizer resolves.
5. Proposal detail shows accepted/rejected state.
6. Itinerary reflects the accepted operation or reassures that a rejected
   proposal left plan truth unchanged; affected timing/logistics are repaired.
7. The landed row/day summarizes what changed, provider truth, and unresolved
   work; Changes preserves durable history and valid recovery.
8. Notification/activity receipt routes back to the right object.

### Track B — Direct edit (Change Studio, no proposal)

9. Open Plan; tap a block row (edit-first).
10. Use Change Studio: move, swap, edit time, or edit-preview/commit flow.
11. Resolve a conflict via keep/dismiss or unified conflict sheet.
12. Use Now Mode: skip/reorder current block; confirm reversible state.
13. Changes screen and proposal receipts distinguish human edit vs Vesper proposal where applicable.
14. Run Journey 06 coherence pass after the edit.

Both tracks must send idempotency keys on mutating calls where the API requires them.

## Expected Outcome

- User-visible state: proposal is understandable in under 10 seconds and inspectable in detail.
- Data state: proposal status, votes, affected ids, resolution, and applied/reverted state are stable.
- Cross-surface coherence: Chat, Plan, Home, Changes, Map, and Notifications agree.
- Trust state: users can distinguish proposed, accepted, rejected, and reverted changes.
- Product proof: members can say **Vesper understood us** and the organizer can
  see that the revision improved the itinerary rather than creating follow-up
  planning work.

## Must Never Happen

- Accepted proposal silently mutates the plan without a visible receipt.
- Rejected proposal disappears without confirming the original remains.
- Proposal detail leaks private source context.
- Retry creates duplicate votes or duplicate applied changes.
- Revert says success but Plan/Map still show the changed state.
- Direct edit-preview succeeds in UI but commit fails without surfacing conflict or stale `expected_updated_at`.
- Chat-created proposals bypass shared `build_and_persist_proposal` (drift risk).
- A selected block changes while the surrounding day, participants, or provider
  commitments silently become invalid.

## AI Trace Prompt

```text
Trace BOTH tracks: (A) proposal lifecycle from group chat through vote, resolve, apply, revert, notifications; (B) direct Plan edit-preview/commit, conflict dismiss/keep, Now Mode skip, withdraw/supersede. Report API methods, mock behavior, backend endpoints, idempotency, and read-model invalidation. After each mutation, note whether Journey 06 surfaces would agree.
```

## First Automation Target

Add or extend deterministic tests for:

- vote idempotency
- resolve accepted/rejected
- plan state after accept
- recent changes after accept/revert
- notification routing into proposal/chat/plan
