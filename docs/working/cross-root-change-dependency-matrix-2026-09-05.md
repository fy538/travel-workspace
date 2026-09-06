---
doc_type: working
status: active
owner: strategy integration
created: 2026-09-05
last_verified: 2026-09-06
expires: 2026-10-05
why_new: Records the executable cross-root dependency boundary for owner changes without creating a second authority or a universal invalidation service.
source_of_truth_for:
  - I1 change-propagation coverage
depends_on:
  - complete-system-integration-roadmap-2026-09-05.md
  - ../systems/contribution-and-consequence.md
---

# Cross-root change-dependency matrix

## September 6 delivery ownership

Follow the [coordination register](complete-system-integration-roadmap-2026-09-05.md#2-current-coordination-register--september-6).
These are five different responsibilities, not five names for cache refresh:

| Mechanism | Producing/consuming owner | Current boundary and next evidence |
| --- | --- | --- |
| Foreground read invalidation | Verified owner result → mobile consumers | Life depth and mature Places correction fan-out have landed; verify affected query families, not assumed domain mutation |
| Durable downstream delivery | Source/graph owner transaction → Life projection worker/index | Retained-source verification/attachment/deletion now emits through the Life outbox into a current-authority shadow projector; broader owner producers, indexed serving, and semantic-representation repair remain incomplete |
| Generated-result invalidation | Canonical source/revision/use changes → production/reuse owner | Dark Source worker/readback exists; clearing Home does not invalidate retained generation by itself |
| Pending work cancellation/revalidation | Grant/target/expiry owner → queued action or production executor | Recheck authority and dependencies before effect/publication; a late success cannot restore released material |
| Read-time authorization | Each canonical owner → exact viewer reader | Entity people custody/expiry guards landed; Life/index and other readers need their own current permission evidence |

Each new cross-lane handoff records event identity, owner revision, subject,
scope, causal dependencies, affected consumers, retry/order policy and negative
cases. Use current authoritative reads when an event is a hint rather than a
complete snapshot. The producer owns durable delivery; the consumer owns its
derived state. Do not have Capture write Life rows or have Home mutate sources.
Map source-only expiry, audience withdrawal and explicit correction separately;
independent accepted commitments and authored material must survive repair.

The [history/source-expiry proposal](conversation-history-source-expiry-decision-proposal-2026-09-06.md)
is unadopted. Do not implement its history-specific migration through this
matrix. Settled lifecycle/repair rules and unrelated consumers may proceed.

The first Life delivery seam is now executable: a canonical owner writer can
enqueue a revisioned event through the existing Life outbox, publish an
identifier-only `life_projection.changed` envelope after commit, and rely on a
minute repair sweep when the process-local handoff is missed or a consumer
fails. Retained-source verification, attachment, and deletion now use that
seam and re-read current Intake authority before writing shadow rows. The same
path now also records retained-source semantic representation and withdrawal
when Experience Graph anchors are confirmed or retracted. This is still
delivery/shadow infrastructure only: it does not switch any Life/Home/Places
reader or claim that broader owner families are covered.

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

## Contribution/Capture source-owner envelope — 2026-09-06

The source side now emits a content-free `source-owner-change.v1` envelope in
the existing Intake and Life outboxes (`travel-agent` commit `a669541b2`). A
follow-up (`fce385207`) applies the same transient-expiry guard to canonical
pending-Chat source readers. The
representation follow-up (`780677110`) carries the candidate dependency into
semantic representation handoffs. The
envelope is the receiving contract for retained-source lifecycle and repair;
it does not turn Life into a source writer or copy private material across the
event bus.

| Field | Source-side authority | Receiving obligation |
| --- | --- | --- |
| `event_id`, `event_key`, `ordering.retry_identity` | Intake outbox event key; deterministic event identity | Replays acknowledge the same event; a later gesture/lifecycle transition uses a new key. |
| `owner_id`, `owner_revision`, `ordering.partition/sequence` | Retained-source submission and owner revision | Life compares current owner revision before writing or withdrawing its index; stale hints are not success. |
| `scope` | Authenticated viewer, private audience, purpose (`source_refind` or `projection_repair`) | Re-check viewer/purpose at read and repair; no event metadata grants authority. |
| `source_refs`, `causal_dependencies` | Opaque submission/source/candidate references | Preserve lineage and distinguish source identity from derivative representation; never infer a visit, preference, or shared audience. |
| `lifecycle`, `affected_consumers`, `occurred_at` | Verified/normalized/represented/unrepresented, candidate confirmation/retraction, deleted, or expired transition | Apply the supported owner transition and reject unsupported/stale effects; do not deduplicate by source ID alone. |

The bridge validates and forwards this metadata only. Source bytes, extracted
claims, notes, and generated prose remain outside the cross-root payload. Life
owns its projector/index rows and canonical readback; Home/Places consume
eligible owner revisions after Life or the relevant owner has repaired them.

The source-read side is equally strict: pending-Chat source/image/text reads,
retained-source reads, and anchor source status re-check the owner-bound
custody receipt at read time, not only the mutable storage status/deadline.
Normalization and semantic workers apply the same receipt gate before
prompting, and parent receipt is rechecked before URL/transcript derivatives
are bound. The Life delivery bridge rejects a nested source envelope whose
event key, owner, revision, lifecycle, or viewer scope disagrees with the
legacy outbox fields. These are source-side and delivery checks; they do not
write Life rows or adopt a history/continuity policy.
