---
doc_type: working
status: active
owner: founder / product / architecture / engineering
created: 2026-09-05
last_verified: 2026-09-05
expires: 2026-10-05
why_new: Records the repository execution of the bounded capability-retirement packages and keeps local implementation evidence separate from production shutdown or native QA evidence.
supersedes: []
source_of_truth_for: []
---

# Capability retirement — execution receipt

This receipt records what was implemented in the workspace after the
[capability-retirement plan](product-surface-contraction-investigation-2026-09-04.md).
It is intentionally precise about the boundary: repository code and contract
checks are not production decommissioning, an environment obligation audit,
native mobile acceptance, or proof that an external provider secret has been
removed.

## Landed packages

### CR-0 — scope adoption

- Workspace plan and owner/interface contract: `eb032ca`.
- Booking system and v1 scope amendments: `7b06de4`.
- The adopted responsibility boundary is provider-execution retirement with
  retained evidence, external continuation, practical reads, and ordinary
  Plan/Occasion semantics.
- No universal reservation DTO, broad Life migration, Chat rewrite, or
  production shutdown was authorized by this package.

### CR-1 — static inventory

- Static entry-point/consumer inventory: `0f534c6`,
  `docs/working/capability-retirement-static-inventory-2026-09-05.md`.
- The report covers backend routes, concierge discovery, workers and queues,
  provider execution, mobile routes and controls, retained readers, and
  operational requirements.
- No database, queue, provider account, or production environment was queried.
  The per-environment read-only obligation audit is still required.

### CR-2 — close new execution

- Backend admission and dispatch guards: `travel-agent:7fb582700`.
- New session creation, checkout/hold/payment, restaurant contact/retry, and
  provider-changing itinerary dispatch fail at server/domain boundaries; stale
  and replayed worker paths are guarded as well.
- Concierge booking-tool discovery and its promise language remain present for
  the deferred Chat lane. They were not removed here because the explicit
  instruction for this pass was not to change Chat.
- Focused retirement tests passed before later concurrent work was added. The
  setting remains `BOOKING_EXECUTION_RETIRED=false` by default, so repository
  landing does not silently change production behavior.

### CR-3 — retained external continuation

- Venue envelope continuation facts (URL, phone, website):
  `travel-agent:5e40410f3`.
- Places venue/experience provider handoff: `travel-app:78a396b73`.
- The supported Places path opens a provider URL or phone contact directly;
  it does not create a booking session, Trip, Plan day, reservation debt, or
  global return-catch claim. The generated workspace contract was refreshed in
  `925cecc` and `make contract-check` passed.
- Generalized confirmation intake for an independently purchased, non-Trip
  reservation is deliberately not claimed; it remains a Life/Source owner
  seam for the appropriate lane.

### CR-4 — retained-reader preparation

- Shared Places resilience no longer depends on the booking provider module:
  `travel-agent:e33dd4764`.
- Life, stay, cost, history, privacy, export/deletion, and Chat return-catch
  readers were not migrated or deleted in this pass. This is intentional and
  respects the explicit instruction not to change Chat or Life.

## Verification performed

| Check | Result | Boundary |
| --- | --- | --- |
| Backend admission/retirement focused tests | Passed in the landed slice | Does not certify production queues, callbacks, or external obligations |
| Backend venue/entity/projection focused tests | 57 passed for the continuation contract | Does not certify retained Life readers or native UI |
| Backend touched-file Ruff checks | Passed for the landed slices | Broad repository ratchet has pre-existing failures |
| `make contract-check` | Passed; snapshot, mobile projection, generated types, and bridge coherent | Local contract parity only |
| Mobile typecheck | Passed | Not native device evidence |
| Mobile focused Jest | Passed for venue/contract tests and the existing handoff suites | Not native visual QA; Chat behavior unchanged |
| Mobile changed-file ESLint | 0 errors; baseline warnings remain | Not a release acceptance result |
| App generated route inventory | Refreshed in `travel-app:2e73889fe` | Three already-committed routes were absent from the registry; generated output now matches `app/` |
| App surface-contraction guard | Two failures remain: `/you/intake-submissions/[submissionId]` and `/you/life-record` have no M-1 owner/exemption | Both are Life routes from the concurrent Life lane; resolving them would violate this pass's explicit no-Life boundary |

The backend pre-commit baseline still reports the repository's existing broad
exception-count and size-budget failures. Those were not folded into this
lane's commits or reclassified as caused by the retirement work.

## Explicitly not complete

- No per-environment read-only obligation audit has been run.
- The executable audit and operator procedure are documented in the
  [Booking Capability Retirement Audit runbook](../../travel-agent/docs/operations/Booking%20Capability%20Retirement%20Audit.md).
- The retirement setting has not been enabled in a deployed environment.
- No provider secret, job registration, route, table, or execution UI was
  deleted.
- Life retained readers, independent confirmation association, expense/stay
  readers, historical deep links, and Chat return-catch migration remain open.
- No native screenshot/interaction verdict or production deployment receipt is
  implied by local tests.

## Next gates

1. Run the redacted read-only obligation audit in every deployed environment
   using the [audit runbook](../../travel-agent/docs/operations/Booking%20Capability%20Retirement%20Audit.md).
2. Re-run it after CR-2 deployment to account for in-flight work.
3. Have Life/Chat owners approve the retained evidence and return-context seams.
4. Migrate retained readers, then remove only the execution footprint proven to
   have no remaining consumer or obligation.
5. Record native QA, deployment revisions, provider shutdown, and any recovery
   tail in a new closure receipt; do not mark CR-6 complete from this document.
