# 16 - Account And Data Lifecycle

> Status: draft
> Owner: founder / engineering
> Last updated: 2026-07-19
> Primary phase: cross-cutting (account + data rights)

## Product Promise

A user can sign up, control what the app knows and shares, export their data, and delete their account — and deletion actually purges or anonymizes their personal memory and private signals.

## Canonical User Story

As a user, I want real control over my account and data, so that I can trust the app with private constraints, taste signals, and memory — and walk away cleanly if I choose.

## Why This Journey Matters

- Signup is "Phase 0, embedded"; sign-out, account deletion, and data export/receipt have no owned journey.
- The privacy surface is large (~12 settings routes: privacy dims, delegation, constraints/memory-reset, data-receipt, shared-links revoke) and only slivers are covered by J04/J11.
- Data-rights (export, deletion-purges-private-data) is trust-critical and increasingly compliance-relevant.

## Starting State

- Persona: a user with seeded personal memory, hard constraints, private signals, taste/DNA, and at least one shared recap link.

## Primary Surfaces

- Routes: `/(auth)/sign-up`, `/atlas/account`, `/atlas/privacy`, `/atlas/constraints`, `/atlas/delegation`, `/atlas/data-receipt`, `/atlas/shared-links`, `/atlas/receipt`.
- App docs: [archived Me/Account → Atlas trust investigation](../archive/2026-07/retired-live/me-account-atlas-trust-investigation-2026-06-25.md).

## Canonical Steps

1. Sign up → account provisions, seed-by-email backfill links the Clerk identity to any seeded data.
2. Open privacy → the 5 sharing dimensions + profile toggles reflect and persist real state.
3. Memory reset / retire a learned fact (`/atlas/constraints`) → the signal is actually forgotten downstream.
4. Revoke a shared recap link → the public link 404s afterward.
5. Data receipt / "what Vesper knows" → reflects actual stored data, not a static template.
6. Delete account → personal memory, private signals, and PII are purged or anonymized; shared provider-backed obligations remain only as minimized, anonymized operational truth under a remaining member's control; the user is signed out.

## Expected Outcome

- Privacy toggles, delegation, and constraints persist and take effect downstream.
- Export/receipt reflect real stored data.
- Account deletion purges/anonymizes personal memory + private signals; revoked links die.
- Shared bookings with real external obligations remain actionable for the group without retaining the deleted traveler's identity or private booking context. Drafts, unused offers, and solo-trip booking state are deleted.

## Must Never Happen

- Account deletion leaves personal memory, private signals, or PII queryable.
- Account deletion either destroys a shared external obligation/audit trail or leaves it controlled by, or identifiable to, the deleted account.
- A privacy toggle renders changed but doesn't take effect downstream.
- A revoked shared link still resolves.
- The data receipt shows a template instead of the user's actual data.

## AI Trace Prompt

```text
Trace signup → privacy/constraints/delegation edits → data-receipt → shared-link revoke → account deletion. Verify each privacy control takes effect downstream, the receipt reflects real data, revoked links 404, and deletion purges/anonymizes personal_memories + private signals + PII.
```

## Certification Record

- 2026-07-19: `persona-cert:J16` creates a disposable account, persists an explicit private preference, verifies it in the data export, deletes the account through the real API, and proves the user no longer resolves. Shared Mara/Elif data is never targeted.
- The destructive Postgres scenario covers solo-trip deletion, shared-trip preservation, idempotent missing-user deletion, and commercial-history export/erasure.
- The live pass exposed and fixed the account-deletion response model so structured booking reassignment truth serializes instead of failing after the database deletion succeeds.
