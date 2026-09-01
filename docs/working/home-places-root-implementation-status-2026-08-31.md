---
doc_type: working
status: active
owner: product / cross-repo architecture / backend / frontend
created: 2026-08-31
last_verified: 2026-08-31
expires: 2026-09-30
why_new: Records the first contract-bounded Home and Places implementation after semantic acceptance, separating executable evidence from the larger unimplemented canon.
source_of_truth_for: []
---

# Home and Places Root Implementation Status

## Current executable seam

The first production-shaped read path now exists behind the default-off
internal four-root shell:

```text
canonical owner reads
  -> GET /api/root-projections/home | places
  -> generated OpenAPI mobile types
  -> root-specific data hooks
  -> native Home or the canonical Places workspace
```

The backend remains read-only at this seam. It does not create a new owner,
write ranking, infer durable preference, invoke an agent, or replace existing
Plan, Occasion, Commitment, Outcome, Opening, or Places-feed authorities.

## What is implemented

### Home

- A typed `RootProjectionEnvelopeV1` is compiled from the viewer-safe
  `ExperienceProjection` and served with viewer-relative timezone handling.
- The stable four-region anatomy is enforced: Now, In motion, Horizons,
  Continuity.
- Direct state, Composition, Instrument, owner link, and silence can be
  selected from current owners without requiring input.
- Healthy current Commitment state is ordinary current life, not cold start.
- Urgent provider failure reduces Home to one recovery Instrument; unrelated
  registers are suppressed in the projection but their source revisions remain
  represented for later canonical recomposition.
- Native Returned and Urgent captures are registered. The Urgent capture proves
  that an actionable dominant remains visible below the orientation instead of
  being removed as duplicate prose.

### Places

- The root endpoint lifts the existing canonical `PlacesFeed` unchanged into a
  typed root envelope. Context identity remains exactly shared between the root
  and feed.
- The app consumes that envelope through the existing Places workspace rather
  than creating a second feed or a parallel ranking owner.
- Native saved-scope evidence is registered, and the existing Places QA
  portfolio still covers live, group-decision, booking, gap, and consented
  friend-activity states.

### Transport and compatibility

- The full backend OpenAPI snapshot, active-mobile projection, and generated
  TypeScript types contain the Home and Places root contracts.
- The compatibility shell remains internal and default-off. Existing route
  owners are retained while the target surfaces are evaluated.
- No Chat or Life surface implementation is claimed by this package.

## What this does not prove

The accepted C1/C2/C3/F5 design bundle is broader than this implementation.
The current seam does **not** yet prove:

- the complete 31-kind Home or 34-kind Places unions;
- C2's private contribution grant, minimum-safe group compilation, host
  decision, delivery, withdrawal, and viewer-relative recompilation;
- C3's single contribution identity from Source/Claim through resurfacing,
  command attempt, provider readback, receipt, correction, unwind, and earned
  silence;
- `ReceiptResult` production selection from canonical command/delivery reads;
- an exact `FourRootReturnEnvelopeV1` carried through native pushes and restored
  after origin revision changes;
- Places Focus, Path, and Live Reduction as production root states; the current
  root payload deliberately carries the mature sectioned feed intact;
- provider recovery execution, partial success, monetary rights, or fallback
  branches in F5; the native proof stops before invoking the recovery action;
- real-data ranking quality, accessibility certification, performance, or a
  production shell migration.

## Next contract-bounded package

Keep the next package on Home and Places until explicitly expanded:

1. add canonical receipt/readback adapters only where an existing command or
   provider owner can supply per-owner verified state;
2. carry the exact return envelope for Home-owned Places depth and
   Places-to-Home return without encoding routes or component names;
3. add native Available and Full Quiet evidence, followed by error/degraded
   state evidence;
4. prove one C2 social consequence and one C3 contribution lineage using real
   owner identities, marking every unavailable link rather than filling it with
   fixture prose; and
5. defer shell promotion until those reads survive native and real-data review.

This is substantial implementation progress, but it is a projection spine—not
yet the whole accepted Home/Places product.
