# 13 - Failure And Recovery

> Status: draft
> Owner: founder / engineering
> Last updated: 2026-07-16
> Primary phase: cross-cutting (every phase's unhappy path)

## Product Promise

When something goes wrong — a hold expires, the network drops, two people edit at once, an invite is stale, a session is unauthorized — the app says so honestly and offers the next move. It never renders fake success.

## Canonical User Story

As a traveler hitting a real-world failure (expired booking hold, offline edit, stale client, declined invite, auth lapse), I want a clear, actionable recovery path, so that I trust the app with money, plans, and group coordination.

## Why This Journey Matters

- The other 12 journeys are happy-path; failure handling exists only as scattered "must never happen" bullets, never as an owned end-to-end flow.
- This is the dogfood/TestFlight blast radius: real providers, flaky networks, and stale clients are live.
- Fake-success on money or a booking is the single most trust-destroying failure mode.

## Starting State

- Persona: any (mara group / solo).
- Trip state: a planning or live trip with a pending hold, an open proposal, and a pending invite.
- Failure triggers: expired hold (Duffel 410), stale `expected_updated_at` (409), declined/expired/consumed invite, an edit attempted while offline, 401/403 on a member-restricted write.

## Primary Surfaces

- Routes: `/booking/[sessionId]`, `/(tabs)/trips/[tripId]/plan`, `/(tabs)/trips/[tripId]/changes`, `/invite/[slug]`, `/trip-accommodations`.
- App docs: [Booking Group Semantics](../../travel-app/docs/page-specs/booking-group-semantics.md), [Change Proposals](../../travel-app/docs/page-specs/change-proposals.md), [Offline First QA](../../travel-agent/docs/operations/Offline%20First%20QA.md).

## Canonical Steps

1. Open a booking session whose hold has expired → 410 surfaces as "this hold expired, re-search," not a confirmed booking.
2. Resolve a proposal with a stale `expected_updated_at` → 409 surfaces a refresh/conflict path, no silent overwrite.
3. Edit a block offline → the app says the change was not sent and requires an explicit retry after reconnect; it never claims that an outbox exists or renders the edit as saved.
4. Open a declined / expired / already-consumed invite → a clear terminal state, not a join that half-succeeds.
5. Hit a member-restricted write as a non-organizer → 403 surfaces a "ask the organizer" path, not a dead button.
6. Lose auth mid-session (401) → re-auth prompt, no blank screen or partial-state corruption.

## Expected Outcome

- Every failure renders honest, actionable copy and a recovery affordance.
- No fake-success: money, bookings, and plan mutations never show "done" when they failed.
- Read models stay consistent after a rejected write (no orphaned/ghost state).

## Must Never Happen

- A failed booking/payment renders as confirmed.
- A stale or offline write silently overwrites a newer change.
- A failed action leaves a half-applied state (orphaned expense, ghost member, dangling hold).
- An error renders as a blank screen or an infinite spinner with no recovery.

## AI Trace Prompt

```text
Trace each failure path (Duffel 410 hold-expiry, 409 stale-write, offline edit conflict, declined/expired/consumed invite, 401/403) from the API status into the FE. Identify any path that renders fake success, swallows the error, leaves half-applied state, or offers no recovery affordance.
```

## First Automation Target

Backend invariant cert (persona-cert / pytest): drive each failure status against real routes and assert the response is the documented terminal/conflict state — never a success shape. FE mock-mode: force `EXPO_PUBLIC_MOCK_FAULTS` and confirm each surface shows recovery copy, not fake success.
