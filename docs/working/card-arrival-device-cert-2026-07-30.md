---
doc_type: working
status: active
owner: frontend / backend
created: 2026-07-30
expires: 2026-08-29
why_new: Device-cert runbook for card-arrival SSE placeholder→materialization (P2/G12).
supersedes: []
---

# Card arrival device cert — SSE → placeholder → materialization

**Status:** lane ready · live device pass **pending**  
**Date:** 2026-07-30  
**Owns:** P2 / G12 of the Vesper cards gap roadmap  
**Related:** `docs/systems/concierge-vesper.md`, `.maestro/36-chat-card-arrival.yaml`,  
`hooks/useCardArrivalReconciliation.ts`

## Goal

Prove on a **release-profile** (or production) iOS/Android build — not Expo Go alone —
that a streamed concierge turn which posts a card tool:

1. Shows `CardArrivalPlaceholder` after `tool_started` / reserved `card_envelope`
2. Replaces it with the durable attachment after `tool_complete` + early history
   handoff (or turn-end history), without a stuck shell
3. Survives backgrounding mid-stream (8s timeout path + foreground reconcile)
4. Handles a multi-card turn (e.g. venue then map_route) with independent shells

Mock Maestro `36-chat-card-arrival.yaml` remains the PR visual smoke for the
handoff morph. It does **not** satisfy this cert (fixture guide link, no live SSE).

## Preconditions

- Backend reachable with `SKIP_AUTH` or real Clerk session as used in dogfood
- App built with release/`preview` profile so `expo/fetch` SSE path matches prod
- A trip + personal conversation that can invoke a card tool (`post_venue_card`
  or `propose_trip_creation` are good)

## Human / Maestro live script

### A. Happy path (single card)

1. Open private Vesper chat for the trip
2. Prompt that forces a card tool (e.g. ask for a specific place recommendation
   that should `post_venue_card`)
3. Observe:
   - Streaming prose
   - Arrival placeholder with typed label (“Preparing the place card…”)
   - Placeholder clears; venue (or other) card soft-enters
4. Pass if placeholder → card completes without manual refresh and without the
   shell lingering after the card is visible

### B. Multi-card turn

1. Prompt that yields venue + route (or two arrival tools in one turn)
2. Pass if each placeholder reconciles independently (first card can appear
   while the second shell remains)

### C. Background mid-stream

1. Start a card-producing turn
2. Background the app during streaming / after `tool_started`
3. Foreground after ~5–10s
4. Pass if: no permanent placeholder; either the card is present or the shell
   cleared via timeout/reconcile and history shows the durable row

## Recording

- Screenshot or screen recording of A + C
- Note build profile, OS, backend env, date
- When green: update `docs/systems/concierge-vesper.md` Open risks — flip
  “on-device streaming path is unvalidated” to validated with this doc link + date

## Explicit non-claim

Green Jest / mock Maestro / this runbook existing ≠ device-validated.
MVP invariant #1: device proof required to close G12.
