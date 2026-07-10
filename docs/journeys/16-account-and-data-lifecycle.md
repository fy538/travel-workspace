# 16 - Account And Data Lifecycle

> Status: draft
> Owner: founder / engineering
> Last updated: 2026-06-29
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
6. Delete account → personal memory, private signals, and PII are purged or anonymized; the user is signed out.

## Expected Outcome

- Privacy toggles, delegation, and constraints persist and take effect downstream.
- Export/receipt reflect real stored data.
- Account deletion purges/anonymizes personal memory + private signals; revoked links die.

## Must Never Happen

- Account deletion leaves personal memory, private signals, or PII queryable.
- A privacy toggle renders changed but doesn't take effect downstream.
- A revoked shared link still resolves.
- The data receipt shows a template instead of the user's actual data.

## AI Trace Prompt

```text
Trace signup → privacy/constraints/delegation edits → data-receipt → shared-link revoke → account deletion. Verify each privacy control takes effect downstream, the receipt reflects real data, revoked links 404, and deletion purges/anonymizes personal_memories + private signals + PII.
```

## First Automation Target

> NOTE: account-deletion certification must NOT run against a shared seeded persona (it would destroy mara/elif and break other certs). Certify against an ephemeral throwaway user, or a dedicated disposable persona, in BE pytest — not the lived persona-cert.

BE scenario (ephemeral user): create a user with personal memory + private signals + a shared link; delete the account; assert personal_memories/private signals are purged or anonymized and the shared link no longer resolves.
