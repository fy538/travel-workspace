---
doc_id: multiplayer-execution-receipt-2026-08-22
title: Multiplayer execution receipt — 2026-08-22
status: active
owner: product-engineering
created: 2026-08-22
last_updated: 2026-08-22
doc_type: working
why_new: Records the bounded Chat-native multiplayer execution slice and its verified limits.
expires: 2026-09-05
---

# Multiplayer execution receipt — 2026-08-22

## Scope completed in this session

The first multiplayer slice is now Chat-native rather than a new destination
screen. A clean-graph Occasion invitation can be represented as a private
`card-blueprint.v1` artifact and can be acted on from the existing composed-card
renderer.

The path is deliberately revision-bound:

1. The server builds a private invitation card with stable `occasion` and
   `occasion_invitation` references.
2. Pending invitations expose opaque `accept` and `defer` action refs; terminal
   invitations are actionless.
3. Tapping an action calls the card resolver. It verifies the persisted
   invitation, invitee identity, current revision, status, and expiry.
4. The resolver returns an intention, not a URL or arbitrary mutation payload.
5. The app sends the typed Occasion response with a fresh idempotency key,
   invalidates graph projections, and shows a consequence in Chat.

The same artifact grammar now admits Occasion decisions, commitments, outcomes,
and place memories as references, and the collaboration intent is understood by
the native Chat renderer and telemetry. Decision voting transport exists and is
covered independently; decision-card mutation controls remain a follow-up until
their resolver and revision contract are landed together.

## Commits landed

Backend (`travel-agent`, `codex/clean-break-occasion-core`):

- `b75565893` — clean-graph collaboration card grammar.
- `6b4044d72` — server-authorized Occasion invitation actions.
- `697efb248` — bounded invitation control validation.
- `cb265c99c` — persistence-boundary test for the two-control invitation card.

Mobile (`travel-app`, `codex/clean-break-product-shell`):

- `96eaa3d9` — clean-graph collaboration transport and mock policy.
- `84fe3f35` — collaboration artifact schema and telemetry classification.
- `d00fb6d2` — composed-card invitation action test.
- `51e45907` — revision-bound invitation mutation in Chat.

Workspace contract:

- `dec7b69` — regenerated OpenAPI snapshots for the new destination kind.

## Verification

- Backend Chat/graph suite: **99 passed**.
- Backend focused Chat card suite: **33 passed**.
- Mobile focused Chat/graph suite: **44 passed**.
- Mobile TypeScript: **passed**.
- API boundary check: **passed**.
- Polish scenario registry: **31 registered**.
- Vesper Chat design references: **passed**.
- Polish QA doctor: **passed in dry-run mode**. Screenshot capture is still
  blocked until Metro is running on port 8081.

## What is intentionally not claimed

- No cloud Postgres or Qdrant promotion was performed.
- No production-dogfood release or serving flag was activated.
- No new multiplayer screen was introduced.
- Decision voting is not yet wired to a card action; its existing typed API
  transport remains the authority.
- The broader intake/content work currently staged in the backend is separate
  work and was not swept into these commits.

## Next bounded slice

Land decision-card voting as the sibling of invitation cards: a two-option
private card, a server resolver that verifies active Occasion membership and
revision, and a typed `cast vote` mutation from the same `ComposedChatCard`
renderer. Keep options beyond two actionless until the card grammar grows a
reviewed multi-option interaction.
