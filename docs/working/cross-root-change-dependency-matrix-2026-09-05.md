---
doc_type: working
status: active
owner: strategy integration
created: 2026-09-05
last_verified: 2026-09-05
expires: 2026-10-05
why_new: Records the executable cross-root dependency boundary for owner changes without creating a second authority or a universal invalidation service.
source_of_truth_for:
  - I1 change-propagation coverage
depends_on:
  - complete-system-integration-roadmap-2026-09-05.md
  - ../systems/contribution-and-consequence.md
---

# Cross-root change-dependency matrix

This is a consumer matrix, not a new owner. A canonical owner command or
verified consequence remains authoritative; clients invalidate the read models
that may contain dependent material and then re-read through their existing
owner routes. Invalidation is a freshness signal, not proof that a change was
accepted.

## Current executable fan-out

| Authoritative event | Home | Places | Life | Other dependent readers | Current implementation |
| --- | --- | --- | --- | --- | --- |
| Root consequence resolves or repairs | v2 Home envelope | v2 Places envelope | v1 Life root and direct record pages | Places feed/projection, trip plan/proposals, occurrence artifacts/proposals, experience graph, profile portrait, conversations | `travel-app/data/rootConsequences.ts::invalidateConsequenceReadModels` |
| Home/Places root is stale or a foreground scope changes | matching root envelope | matching root envelope plus scoped feed/projection/search/saves/reading | Life root when the returned continuity target is Life | Existing root-specific query families | `travel-app/utils/invalidateRootProjections.ts`, `travel-app/data/placesProjection.ts` |
| Account session changes | no prior-account read may be reused | no prior-account read may be reused | no prior-account read may be reused | Query clients and opaque grants are session-bound | `rootConsequences.ts` account-session guard; query-key ownership |
| Canonical Life record correction or source revision | dependent Home continuity candidates must refetch when surfaced | dependent Places returns must refetch when surfaced | corpus/root/depth/refind readers | Retained composition and source-dependent readers remain Life-owned | Life query-key contract; exact consumer coverage still being extended |

The first row is deliberately broad because a verified consequence can affect
multiple owner projections. It does not claim every read model changed; query
invalidation is cheap and the subsequent owner reads decide what is current.

## Explicit non-claims

- Invalidating a query does not authorize a new location read, provider poll,
  notification, monitor, or external action.
- A stale root does not imply that the underlying command failed. Readback from
  the canonical owner decides whether the result was applied, rejected,
  partial, unknown, or already current.
- Home and Places do not own Life records, social membership, source custody,
  or consequence receipts. They only invalidate and render their projections.
- A generated Source contribution is not repaired by clearing a root query
  alone. Its durable production/reuse record must be rejected or revalidated
  against source revisions, purpose, audience, grants, and expiry.

## Gaps to close in I1/I2/I5

1. **Background dependency fan-out:** map source-revision, relationship/grant,
   pending-turn, and retained-composition consumers that are not reachable from
   the foreground consequence hook. Each must name its owner event or bounded
   refresh path; do not add an all-account event bus by default.
2. **Cross-root depth evidence:** when Home or Places surfaces a Life-backed
   candidate, its return/depth query must carry the same source/revision and
   audience checks as the root envelope. Life owns the cursor and corpus
   implementation; Strategy verifies the consumer contract.
3. **Late completion protection:** background production and pending actions
   must revalidate the owner revision and account session before publishing a
   result. A successful invalidation cannot make stale late work current.
4. **Signal-to-judgment routing:** a material current-world change must reach a
   bounded evaluator, not only invalidate React Query. No-change, unknown, and
   out-of-scope signals should create no new user demand.

## Acceptance cases

- A verified consequence refreshes affected Home, Places, Life and depth
  readers; a rejected or unknown result does not fabricate a success state.
- A correction or audience/grant revocation removes dependent presentation but
  preserves independent source evidence and other people's authored outcomes.
- A duplicate or out-of-order signal does not create duplicate generation,
  notifications, or prompts.
- An account switch prevents a late receipt, undo, or invalidation from touching
  the next account.

The matrix should be updated when a new owner, query family, or asynchronous
producer is introduced. If a new row cannot name its authoritative event and
readback, the feature is not ready for integration.
