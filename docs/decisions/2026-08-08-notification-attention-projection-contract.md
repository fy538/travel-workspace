---
title: Notification attention and projection contract
status: accepted
owner: product-and-platform
created: 2026-08-08
decided: 2026-08-08
last_reviewed: 2026-08-08
doc_type: decision
why_new: "Second-pass SOTA review aligned Activity, push, lifecycle, privacy, and device validation into one implementation contract."
---

# Notification attention and projection contract

Status: accepted for implementation
Date: 2026-08-08
Scope: proactive signal → Activity → push → current truth

## Decision

The domain object remains the only canonical business truth. An
`AttentionCase` is the canonical recipient-relative work and lifecycle state.
Activity is a durable, privacy-filtered projection of that case. Push, email,
SMS, and OS notification-center entries are interruptive projections only.

Transport payloads carry opaque identifiers and presentation metadata. They do
not carry the state that a destination screen should treat as authoritative.
Every tap or action resolves the case for the authenticated user and then
refreshes the owning domain read model.

## Identity vocabulary

| Identity | Scope | Purpose |
| --- | --- | --- |
| `event_id` | One domain transition | Idempotent source event |
| `attention_case_id` | Subject + recipient lifecycle | Current work/truth state |
| `occurrence_id` | One notification occurrence | Analytics and response window |
| `envelope_id` | One immutable content/policy snapshot | Cross-channel projection source |
| `delivery_id` | One channel/device attempt | Provider and client delivery trace |
| `dedupe_key` | Same occurrence retries | Prevent duplicate work |
| `presentation_key` | Subject lifecycle + recipient | Replace stale OS presentation |
| `thread_key` | Visual grouping scope | Group related OS entries |

`dedupe_key` and `presentation_key` must not be conflated. For example, an
open proposal and its resolved result are different occurrences but share one
presentation key.

## State invariants

1. A private constraint never enters group-visible copy or metadata.
2. A stale payload never substitutes for canonical domain state.
3. Activity persistence is not disabled by push preference or quiet hours.
4. Read, dismissed, snoozed, resolved, expired, superseded, and canceled remain
   distinguishable.
5. A provider receipt means provider acceptance, not device presentation.
6. A user action is accepted only after ownership and current-truth checks.
7. Every domain resolution reconciles all active projections and open outcomes.
8. Account sign-out revokes both server and native device delivery state.
9. A notification journey is not device-certified until real iOS and Android
   presentation tests pass.

## Required flow events

Notification flows use a shared vocabulary:

`candidate_created`, `gate_rejected`, `selected`, `suppressed`,
`activity_persisted`, `channel_attempted`, `provider_accepted`,
`provider_receipt`, `client_received`, `opened`, `destination_resolved`,
`canonical_rendered`, `snoozed`, `dismissed`, `domain_acted`,
`case_resolved`, `case_expired`.

Events are append-only, user-scoped, and contain identifiers rather than
private notification text. Outcome reporting distinguishes response from
achieved domain result.

## Validation boundary

Automated tests prove static and mock behavior. A backend canary proves the
provider-facing path. Only a physical-device canary can prove Focus, Doze,
lock-screen privacy, badge behavior, replacement, deep-link recovery, and
accessibility.
