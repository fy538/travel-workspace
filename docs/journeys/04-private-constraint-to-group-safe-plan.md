# 04 - Private Constraint To Group-Safe Plan

> Status: draft  
> Owner: founder / engineering  
> Last updated: 2026-06-06  
> Primary phase: trust / planning

## Product Promise

Travelers can tell Vesper private truths, and Vesper can help the group without revealing who said what.

## Canonical User Story

As a traveler, I want to privately tell Vesper about my budget, dietary needs, accessibility needs, or energy level, so that the group plan improves without exposing me.

## Why This Journey Matters

- "Privacy enables honesty" is a core product pillar.
- Private signal can affect group chat, proposals, notifications, booking, memory, and Atlas.
- Mock mode can prove redaction rules exist, but real model output and streaming composition can still drift.

## Starting State

- Persona: trip member, not necessarily organizer.
- Trip state: active planning trip with group chat and private concierge available.
- Fixture: `trip-lisbon-26` plus private chat messages about ankle/food/energy constraints.
- Permissions: no special device permission.

## Primary Surfaces

- Routes: `/(tabs)/concierge/chat`, `/(tabs)/trips/[tripId]/chat`, `/(tabs)/trips/[tripId]/plan`, `/notifications`, `/atlas/privacy`.
- App docs: [Agent Chat](../../travel-app/docs/page-specs/agent-chat.md), [Change Proposals](../../travel-app/docs/page-specs/change-proposals.md), [Booking Group Semantics](../../travel-app/docs/page-specs/booking-group-semantics.md).
- Reliability trace: [Private Input To Group-Safe Context](../reliability/traces/private-input-to-group-safe-context.md).
- Existing anchors: `__tests__/data/privacy.test.ts`, `__tests__/utils/chatDestination.test.ts`, `__tests__/components/chat/MessageBubbleCompositionSkipped.test.tsx`, backend eval tests listed in [Golden Paths](../reliability/Golden%20Paths.md).

## Canonical Steps

1. Traveler opens private Vesper chat for a trip.
2. Traveler shares a private constraint.
3. Vesper acknowledges candidly in private.
4. Vesper later recommends or proposes a group-visible adjustment.
5. Group chat receives public-safe explanation.
6. Plan or proposal reflects the accommodation without naming the private source.
7. Privacy/receipt surface can explain what was used in an inspectable way.

## Expected Outcome

- User-visible state: private chat feels candid; group chat feels public and composed.
- Data state: private fact remains scoped to owner; group-facing object stores redacted summary.
- Cross-surface coherence: proposal, plan, notification, and booking copy use public-safe language.
- Trust state: user can inspect or retire remembered private signal.

## Must Never Happen

- Group copy names the member or private constraint.
- Push notification preview leaks private signal.
- Booking justification exposes financial, accessibility, relationship, or dietary details.
- Composition-skipped state renders like a raw bug.
- Privacy audit is missing the relevant use of private signal.

## AI Trace Prompt

```text
Trace a private constraint from private concierge intake through group-safe use in chat, proposal, notification, and booking copy. Identify redactor boundaries, channel-routing logic, frontend rendering, backend eval coverage, and any path that bypasses compose_group_message or the privacy redactor.
```

## First Automation Target

Create a deterministic privacy fixture trace that checks leak phrases across:

- group chat generated/public notes
- proposal summary and rationale
- notification title/body
- booking proposal summary
- memory/Atlas receipt wording

