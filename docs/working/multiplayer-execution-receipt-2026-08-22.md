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
the native Chat renderer and telemetry. Decision voting is Chat-native for two
to four options: each option is a server-issued opaque action, and the resolver
checks active Occasion membership, current decision revision, and that the
option still exists before the app sends the typed vote mutation. Larger
decisions remain actionless until a separately reviewed presentation exists.

## Commits landed

Backend (`travel-agent`, `codex/clean-break-occasion-core`):

- `b75565893` — clean-graph collaboration card grammar.
- `6b4044d72` — server-authorized Occasion invitation actions.
- `697efb248` — bounded invitation control validation.
- `cb265c99c` — persistence-boundary test for the two-control invitation card.
- `9a545dbf6` — server-authorized two-option Occasion decision votes.
- `40d0c56f3` — bounded four-option vote grammar, contiguous-index validation,
  and card persistence tests.
- `3bbeae064` — explicit four-option persistence-boundary coverage.
- `5b1fb0874` — sparse decision action-index rejection coverage.

Mobile (`travel-app`, `codex/clean-break-product-shell`):

- `96eaa3d9` — clean-graph collaboration transport and mock policy.
- `84fe3f35` — collaboration artifact schema and telemetry classification.
- `d00fb6d2` — composed-card invitation action test.
- `51e45907` — revision-bound invitation mutation in Chat.
- `fdb51f72` — revision-bound decision vote mutation in Chat.
- `1515a9b8` — mobile schema and renderer contract for four bounded vote
  controls.

Workspace contract:

- `dec7b69` — regenerated OpenAPI snapshots for invitation actions.
- `2bbfc6a` — regenerated OpenAPI snapshots for decision vote actions.

## Verification

- Backend Chat/graph suite: **104 passed** on the current branch.
- Backend card/action follow-up: **35 passed** for the card grammar file.
- Mobile focused Chat/graph suite: **44 passed** before the vote slice, plus
  **27 passed** for the invitation/vote/card-grammar follow-up.
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
- Decision voting is intentionally limited to four visible options; larger
  decisions remain actionless and can still use the existing typed API
  transport directly.
- The broader intake/content work currently staged in the backend is separate
  work and was not swept into these commits.

## Next bounded slice

The four-option interaction is now the bounded grammar. The next slice is a
product decision on whether larger decisions should stay Chat-question driven,
followed by cloud/demo promotion and device receipts. Keep the current
default-deny posture until production target evidence is complete.
