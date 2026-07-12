---
doc_type: contract
status: active
owner: frontend / product
created: 2026-07-12
last_verified: 2026-07-12
why_new: Establish a shared contract for truthful asynchronous UI states.
supersedes: []
source_of_truth_for: [client-state-reliability]
---

# Client State Reliability — Cross-cutting Doctrine

> Surface: Cross-cutting  
> Status: active  
> Last updated: 2026-07-12

## Purpose

Every screen must make the truth of its data and actions legible. A blank
surface, a disabled control without a reason, or a success claim after an
unknown write outcome breaks trust more than a visible failure does.

## Required state model

| Concern | Required states | Recovery rule |
|---|---|---|
| Read | initial loading, ready, empty, stale, partial, unavailable | Keep usable cached/partial content; retry the failed source only when possible. |
| Pagination | loading more, more-page failed, exhausted | Never replace loaded rows with an error; show an inline retry at the boundary. |
| Mutation | idle, pending, succeeded, retryable failure, terminal failure, unknown outcome | Disable duplicates while pending. Reconcile timeout/in-flight writes by reading the source of truth before retrying. |
| Context | offline, reconnecting, background/resumed, revoked/read-only | Explain the restriction and restore/re-read state on return; never silently claim completion. |

## Minimum surface contract

Any dogfood-critical surface must name, in its surface contract or tests:

1. the authoritative read model and what counts as usable cached content;
2. its empty state versus an unavailable state;
3. its mutation pending and rollback behavior;
4. its retry/reconciliation behavior for timeout, conflict, and backgrounding;
5. its pagination behavior when a later page fails;
6. at least one executable test or device route for its highest-risk recovery.

## Current reference implementations

| Surface | Covered state | Evidence |
|---|---|---|
| Atlas Postcards | multi-source partial / hard failure | `travel-app/app/atlas/postcards.tsx` and smoke tests |
| Atlas Removed | later-page failure preserves prior rows | `travel-app/app/atlas/removed.tsx` and smoke test |
| Privacy and notification controls | pending, rollback, inline retry | `travel-app/app/atlas/privacy.tsx`, `app/trip-settings/notifications.tsx` |
| Proposal detail | applying, applied, failed, timeout/in-flight reconciliation, resume | `travel-app/components/trip/proposal-detail/ProposalDetailScreen.tsx` |

## Review checklist

- Does an empty message appear only after a successful read proves emptiness?
- If one source fails, does the screen say which information remains usable?
- Can a second tap duplicate an action?
- After a timeout or resume, does the UI re-read before it tells the traveler what happened?
- Can the traveler recover without leaving the surface?
