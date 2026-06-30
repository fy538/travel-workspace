# 18 - Signed-Out Join-By-Invite

> Status: draft
> Owner: founder / engineering
> Last updated: 2026-06-29
> Primary phase: distribution (invitee's first touch)

## Product Promise

Someone who receives an invite link with no account can land it, see what they're joining, sign up, and end up a member of the right trip — the token survives the auth detour.

## Canonical User Story

As an invited person who has never used the app, I want to tap a link, understand the trip, create an account, and land inside that trip, so that joining a friend's plan is frictionless — the viral/distribution loop.

## Why This Journey Matters

- J02 covers invite creation from the *organizer* side; the *signed-out invitee's* first-touch (token carried through auth → membership) is uncovered.
- This is the distribution loop — the most-common first-ever experience for a new user, and the riskiest (auth detour can drop the token).
- A dropped token = a confused new user who signed up but isn't in the trip.

## Starting State

- Persona: a brand-new, signed-out recipient.
- A valid (unconsumed, unexpired) invite token for an existing trip.
- Also test: a manual invite-code paste fallback.

## Primary Surfaces

- Routes: `/invite/[slug]`, `/invite-code`, `/(auth)/sign-up`, `/(auth)/sign-in`, then `/(tabs)/trips/[tripId]`.
- App docs: invite landing + token-through-auth handoff.

## Canonical Steps

1. Open `/invite/[slug]` while signed out → the invite landing renders the trip preview (organizer-safe fields only, no private leak).
2. Tap "Join" → routed into the auth flow with the token preserved.
3. Sign up (new account) → on completion, the token is consumed and the user lands inside the trip as a member.
4. Manual fallback: paste an invite code at `/invite-code` signed out → same join outcome.
5. Edge: an expired/consumed token shows a clear terminal state, not a half-join.

## Expected Outcome

- The token survives the signup/sign-in detour and produces membership in the correct trip.
- The signed-out landing shows only organizer-safe public fields (no private group leak — ties to J04).
- Terminal states (expired/consumed) are honest.

## Must Never Happen

- A new user signs up but is NOT added to the trip (dropped token).
- The signed-out invite landing leaks private group fields (members, itinerary, constraints).
- A consumed/expired token half-joins or errors opaquely.

## AI Trace Prompt

```text
Trace a signed-out invite: /invite/[slug] → auth → signup → membership. Verify the token survives the auth detour, the landing exposes only organizer-safe public fields, and consumed/expired tokens reach a clean terminal state. Identify any path where signup succeeds but membership doesn't.
```

## First Automation Target

> NOTE: the signed-out auth detour is a FE/Clerk flow not cleanly exercised in the in-process persona-cert; certify the token→membership contract in BE (invite accept) + the public-field shape in the FE mock-walk. Registers as a visible skip in persona-cert until the auth path is harnessed.
