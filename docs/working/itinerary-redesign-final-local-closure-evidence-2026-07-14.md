---
doc_type: working
status: active
owner: backend / frontend / product operations
created: 2026-07-14
last_verified: 2026-07-14
expires: 2026-08-13
why_new: Consolidate the final locally executable itinerary implementation, integration, contract, and rollout evidence after the adversarial review.
source_of_truth_for: [itinerary-redesign-local-closure-2026-07-14]
---

# Itinerary redesign — final local closure evidence

**Outcome:** All locally executable engineering and proof gates found by the
post-IR-17 adversarial review are closed. Production rollout advancement and
compatibility retirement remain intentionally blocked on representative live
evidence, an approved policy threshold, and the governed observation window.

## Integrated backend

Final integration branch:
`codex/itinerary-integration-20260714` at `0fd8f7a16`.

The branch incorporates the itinerary foundation, current main, provider fault
evidence, IR-17 selected-trip/rollback evidence, the current membership and
archive semantics, and the current settlement correction model.

- Alembic has one head: `spvoid01`.
- An empty PostgreSQL database upgraded through the complete graph to
  `spvoid01`.
- The redundant local merge revision `ir19m001` was removed after current main
  supplied the canonical `177c97f898a1` merge revision.
- Route coverage is complete: **294 client-covered + 79 explicitly dark = 373
  non-admin routes**.
- OpenAPI export is deterministic and byte-identical to the workspace snapshot:
  **361 paths, 402 operations, 782 schemas**, SHA-256
  `febbc7f9406601107012bc4f00aa2403549f29be3648c1c42aaa2e1248c7724e`.
- The generated frontend schema check passes against that snapshot.

Current-schema integration evidence on the fresh database:

- itinerary/API/audit suite: **388 passed**;
- Plan/Map/Folio/account/compatibility suite: **402 passed**;
- adjacent current-main settlement suite: **102 passed**;
- focused provider/history/rollout/hold integration suite: **31 passed**;
- Ruff and formatting checks pass for the integrated itinerary and merge files.

The two large itinerary commands contain **790 distinct tests**. The focused
command overlaps those suites and is recorded as targeted integration evidence,
not added to the distinct total.

## Provider and history proof

Provider fault evidence proves both Replace-and-rebook and held confirmation
from plan commit through saga creation and retry boundaries.

- held to confirmed preserves booking, event, expense, subject, saga, and
  history identities;
- idempotent replay emits exactly one provider transition and one terminal
  history transition;
- cancellation and replacement-booking failures resume without phantom
  dependencies;
- Bookings, itinerary metadata, and Needs-attention projections advance
  coherently;
- provider transitions do not mutate expense truth;
- an expired hold cannot trigger provider payment after the atomic database
  claim rejects it;
- changed-price approval is bound to one quote hash and saga revision, while an
  explicit rejection is terminally recorded as `declined`; and
- natural deadline expiry is terminally recorded as `expired` and atomically
  converges the offer, dependency, block booking reference, saga, provider
  transition, operation history, and read-model invalidation. Fault injection
  proves no partial expiry can land.

The history projector now returns the latest append-only transition. A saga
that recovers from `provider_failed` through pending to success no longer
appears stuck on the earlier recoverable failure.

## IR-17 local operational proof

The selected-trip fixture proves the locally executable shadow, dual-read, and
rollback mechanics:

- Plan lifecycle shadow: 1 match;
- Map lifecycle shadow: 1 match;
- Move-policy shadow: 1 match;
- canonical Plan/Map authorities: 1/1 each;
- projection-version mismatches: 0;
- legacy/Plan/Map event-identity mismatches: 0;
- adapter/unknown policy errors: 0;
- lowering the stage immediately restores compatibility Plan reads while
  retaining canonical state and history.

The existing local dogfood lifecycle audit remains 13/13 evaluated with zero
projection errors, unexplained disagreements, or canonical Plan/Map
disagreements. It is not launch evidence: the corpus still lacks six destination
timezones and coverage for Ideation, Final prep, Live, and Cancelled.

## Frontend and on-device evidence

Final frontend evidence is owned by branch
`codex/itinerary-on-device-evidence` at `088403af`, merged onto the current
frontend main. The final device capture's manifest pins the itinerary code under
test to `d902dffa`; the later branch commits record the structured verdict and
merge two unrelated Atlas-only mainline commits.

Integration audit correction (2026-07-14): the original branch history had
merged frontend `main` into the evidence branch, but the evidence branch itself
had not become reachable from `main` before its worktree/ref was removed. The
complete chain was recovered at `e23b4400` and merged into frontend `main` as
`8c2ae16f`. Commit `e23b4400` is post-capture hardening for typed contextual
return boundaries and one-time scroll restoration; the device manifest remains
correctly pinned to the captured implementation at `d902dffa`.

The Simulator pass found and fixed a real dogfood blocker: mock persona Plan
State omitted canonical authority, so the server-selected read-shell boundary
correctly fell back and the new itinerary shell could not be exercised. Mock
Plan State now passes through one canonical construction path, with structural
capability derived from trip role/edit policy and booking change denied when
provider evidence is unavailable. The ready fixture also no longer duplicates
days 4–6, and its active traveler is present in the member roster.

Static and focused frontend verification:

- TypeScript: pass;
- final post-merge itinerary-adjacent sweep: **622 passed** across 75 suites,
  with one snapshot;
- exact-return/object coverage for event to expense, stay to expense, and
  contextual return state: **12 passed**;
- Plan row/explanation and screen smoke coverage after the final voice clamps:
  **49 passed**;
- accessibility governance: pass;
- registered polish-QA scenario identifiers: pass (**27 registered**);
- itinerary design-reference validation: pass (**1 manifest, 7 pairs**);
- committed structured-verdict validation: pass (**39 verdicts**);
- polish-QA device doctor: pass;
- OpenAPI generated-schema check: pass.

The tracked design references come from the user-approved final Vesper
Itinerary export and live under
`docs/surfaces/trip-itinerary/design-refs/`. Real iPhone 16 Pro capture covers
the resting itinerary, dense scrolled itinerary, proposal path, and typed
Change launcher. Both registered personas completed successfully (**2/2**).
The skeptical structured verdict validates as **pass**, with nine improvements
over the previous mixed verdict, zero regressions, and four retained p2 polish
findings. It records correct destination-local times, compact Vesper voice,
row-inspection before explicit Change, stable selected-object context, typed
action grouping, destructive Remove treatment, and usable 393pt safe-area
behavior. The capture manifest and verdict remain the authority for visual
findings and known mock-data noise.

## Decision and remaining external gates

Keep production rollout flags dark. Do not start or close the compatibility
window, and do not retire Folio, compatibility reads/writes, legacy schema,
enums, adapters, or records from local evidence.

The remaining gates are external operating evidence, not unfinished local
implementation:

1. select and remediate a representative production cohort with the missing
   lifecycle and timezone coverage;
2. measure a non-empty live policy sample and obtain product/operations approval
   for its numerical threshold;
3. advance staged cohorts only after the governed shadow/dual-read gates pass;
4. observe at least 14 days and one app release with old-client parity,
   shadow/dual-read cleanliness, legacy-bypass cleanliness, and canonical
   history completeness;
5. retire compatibility only after that observation window passes.

No local fixture, test result, or design capture is relabeled as production
cohort evidence.
