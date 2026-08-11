---
doc_type: archive
status: archived
owner: engineering
created: 2026-07-26
last_verified: 2026-07-26
archived: 2026-08-10
why_new: Record the immutable cross-repository candidate selected for the post-2026-07-26 integration stabilization cycle, including its remote safety branch and known gate baseline.
promotes_to: docs/journeys/STATUS.md and release evidence after the candidate passes its required certification layers
supersedes: []
source_of_truth_for:
  - stabilization-candidate-2026-07-26
  - candidate-sha-set-2026-07-26
---

> **Archived 2026-08-10.** Expired 2026-08-09 with no live consumers. The
> stabilization cycle it described is closed; current certification is
> [Journey Status](../../journeys/STATUS.md) and promoted receipts in
> `evidence-attestations.json`.


# Stabilization Candidate — 2026-07-26

> This is a candidate receipt, not a release claim. Its purpose is to keep the
> integrated SHA set stable while deterministic gates, journey flows, and
> device evidence are repaired and re-run.

## Candidate SHAs

| Repository | Branch | SHA | Remote state |
|---|---|---|---|
| Travel Workspace | `main` | `0e2fb5d97432aa417f4ca328d3d72976cbac0c59` | `origin/main` |
| Travel Agent | `main` | `e92942a9c97d49bf2b9a3f6175c3e4fe8ada9b57` | `origin/main` |
| Travel App | `main` | `f18d0917ead640c621271a77fe8b2a4d8908a79d` | safety snapshot: `origin/codex/stabilization-20260726` |

The app snapshot deliberately does not update `origin/main`. It protects the
53 locally accumulated commits while the candidate is stabilized.

## Freeze boundary

Until this candidate has passed the deterministic gates, no feature merge may
expand the notification, itinerary mutation, trip destination, or test-runtime
surface. Repairs that make the named candidate green are in scope.

## Baseline at selection

- OpenAPI contract and generated mobile API types: passing.
- Journey registry and frontend journey mock-walk suite: passing.
- `make certify-fast`: blocked first by corpus governance violations.
- Maestro governance: one lane/tag mismatch.
- Backend offline suite: order-sensitive failures requiring isolation and
  contract reconciliation.
- Frontend lint and test-type ratchets: failing.
- Current-head simulator evidence: mixed; it must be re-run after repair.
- Required physical-device certification for J04, J05, and J10: not yet run
  for this candidate.

## Promotion rule

The candidate may be promoted only after the deterministic gates are green,
the mutation and notification flows have current-head simulator evidence, and
the required physical-device runbook supplies its separate evidence. Green
tests alone do not establish physical-device certification.
