---
doc_type: working
status: active
owner: founder / Orchestration
created: 2026-09-21
last_verified: 2026-09-21
expires: 2026-10-05
why_new: Provides a bounded cross-repository defect ledger for the September 20–21 implementation window without mixing open bugs into chronological roadmap receipts.
supersedes: []
source_of_truth_for:
  - findings from the September 21 functional-implementation code review
---

# Functional implementation — 12-hour code review

## Review boundary and conclusion

Review requested September 21, 2026, after the preceding progress summary.
Scope is work integrated or implemented approximately September 20, 21:55
through September 21, 10:02 EDT. Earlier-authored commits merged or cherry-picked
in this window are included; author dates alone do not define the change set.

Reviewed checkout: `/Users/feihuyan/travel-workspace--functional-implementation-2026-09-20`.
All three repositories use `codex/functional-implementation-2026-09-20`.

| Repository | Baseline | Reviewed HEAD | Changed files |
|---|---|---|---:|
| Workspace | `b6e7014b2f0f03a18dafc0f87f1f256a58fb1d8a` | `13573d5d4983ee227ba3536f31d037a3657e34da` | 7 |
| Backend | `a7c02cbe15940d13303ae98ada8d6e8192fc85a4` | `913f5a7ae52a287a21c1b0e815f93bdcf918d5b1` | 133 |
| App | `e2e792913b1902007ad237b05a3a58784a80332c` | `1142de74fc32c91a3e181389418041d7acae6828` | 187 |

The lane was clean before review. Canonical-main documentation edits belong to
other work and were not changed. The initial review did not fix, merge, publish,
deploy, enable features, or mutate a running database or simulator; the later
fix pass is recorded below.

**Result: 11 actionable findings — one P1, nine P2, one P3. The repair pass
changed all 11 areas; the later R04/R09 correction closes their code-level gaps,
while persisted-database, queue-environment and native-device evidence remains
open.**
The other nine retain their recorded implementation status and stated
verification limits; this recheck did not recertify them. The implementation has useful
end-to-end paths, but happy-path evidence misses
authorization changes, realistic place hierarchy sizes, non-venue practical
checks, entry-point differences, timezone handling, and the actual queue wrapper.
This ledger records all confirmed findings from this review, not a guarantee that
every defect in the change set has been discovered.

Three parallel reviewers were explicitly dispatched as **`gpt-6-astra`, high**:

- Home/Places backend: supply, selection, public/exact reading lifecycle,
  context, root composition, practical evidence and canonical owner reads.
- Life/social: original custody/refinding, sender and recipient flows, linked
  handoffs, migrations, organized readers/pagination and mobile consumers.
- Mobile/practical: Home/Places/entity navigation, purpose, return, expiry,
  practical origin, Plan assistance and current arrangement presentation.

The orchestrator reviewed worker dispatch, contracts and test evidence, checked
the reported code paths, deduplicated findings, and requested an adversarial
cross-review of generation recovery and fixture cleanup. Product source stayed
unchanged throughout.

## Fix pass

The requested correction pass landed in the independent child repositories:

- Backend `ea403ec0a`, `2935757fe`, `79c4b1d8a` plus `70b607e34` — authority gates,
  release-scoped reading, bounded geography batching, practical entity coverage,
  worker serialization, async DB boundaries, run-isolated rehearsal fixtures
  and schedule-timezone propagation.
- App `44872d0c2` — sender withdrawal history, arrangement-purpose navigation,
  and schedule-zone-aware arrangement time presentation.
- Workspace contract refresh — `docs/openapi.json` and
  `docs/openapi.app.json` now include the relationship `schedule_timezone`
  field and agree with the route's 768-character cursor maximum.

The fixes preserve the original findings and their evidence boundaries. The
disposable-Postgres and native-device regressions remain required acceptance
checks. The prior attempt reported a missing `openai` dependency and no configured
test database; this was not proof that the supported backend environment was
unavailable. The September 21 rebaseline successfully ran
`.venv/bin/python -c "import sys,openai; print(sys.executable); print(openai.__version__)"`
from this lane's backend, reporting the shared backend virtual environment and
`openai` **2.32.0**. That import check does not execute a regression or authorize
an ambient database. Retry the affected commands with the repository virtual
environment and an explicitly disposable test DB when needed.

### September 21 post-fix recheck

At backend `79c4b1d8a` and app `44872d0c2`, the two reopened code gaps were
implemented and focused regressions passed:

- **R04 code correction:** sender-owned history and Withdraw remain rendered
  through recipient loading, error and empty states; new-send selection remains
  gated by current eligibility. The focused sender suite includes the final
  eligible-recipient disconnect case.
- **R09 code correction:** the existing Trip/primary-destination schedule zone
  now flows through the relationship read contract and generated app schema;
  object presentation formats UTC instants in that zone and labels an honest
  fallback when zone evidence is unavailable. Focused backend and projection
  suites cover the propagation and Lisbon conversion.

No disposable-Postgres, queue-environment or native-device acceptance was
established by this correction pass. The ledger should treat R04 and R09 as
code-fixed with those evidence boundaries still open.

Focused correction receipts on the candidate tuple:

- Backend relationship/presentation packet: **35 passed** with Ruff check and
  format verification.
- Source worker/registration/recovery packet: **27 passed** with Ruff check and
  format verification; this is offline wiring/contract evidence, not Arq/Redis
  execution.
- App sender/object-projection packet: **40 passed**; `npx tsc --noEmit`
  passed. ESLint reported no errors and one existing-style max-lines warning
  on the sender screen (803 lines versus the 800-line budget).
- The canonical OpenAPI projector regenerated `docs/openapi.app.json` and
  `travel-app/utils/api/schema.gen.ts` with `schedule_timezone`. The normal
  `sync-types` audit remains blocked by the pre-existing expired API-operation
  policy findings and missing consumer; this is not claimed as a full gate pass.

## Defect index

| ID | Priority | Defect | Owning area | Status |
|---|---|---|---|---|
| R01 | P1 | Rejected original can still commit a recipient handoff/message | Relationships transaction | Fixed; DB regression still required |
| R02 | P2 | Places reading bypasses active release/cohort eligibility | Content / Places | Fixed; governed outsider/cohort matrix still required |
| R03 | P2 | Pull-consent revocation leaves attached original readable | Relationships read policy | Fixed; persisted readback matrix still required |
| R04 | P2 | Sender loses withdrawal controls after relationship disconnect | Mobile original sharing | Code-fixed; focused empty-recipient regression passes; persisted/native evidence still required |
| R05 | P2 | Source worker throws while serializing its actual result type | Worker adapter | Serializer fix applied; actual queue-environment acceptance unrun |
| R06 | P2 | Nine expanded place IDs silently remove Home public supply | Home / Places scope | Fixed with 8-ID batching; scale regression still required |
| R07 | P2 | Site, accommodation and experience fit checks cannot succeed | Practical assessment | Fixed; focused backend tests pass |
| R08 | P2 | Primary Plan details entrance hides arrangement information | Plan / object navigation | Fixed; typecheck passes |
| R09 | P2 | Reservation time is shown in device timezone without a label | Object presentation | Code-fixed; focused schedule-zone/UTC conversion passes; persisted/native matrix still required |
| R10 | P2 | Cleanup for one rehearsal can delete another run's venue | Local fixture tooling | Fixed with run-scoped fixture identity |
| R11 | P3 | Life organization cursor contract snapshot is stale | Cross-repo API contract | Fixed; generated snapshots agree |

P1 requires urgent correction because an externally visible effect can commit
despite a rejected command. P2 items are substantive functional, authority or
tooling defects. P3 is lower-risk contract drift; no current mobile runtime
failure from that particular drift was established.

## R01 — Reject the entire handoff when its selected original is no longer authorized

**Location:** [relationship repository](../../travel-agent/backend/domains/relationships/repository.py),
lines 875–884; transaction catch at 1196–1241.

Prepare a place handoff with an independently selected original. Revoke or
expire that original before execution while the spatial handoff's own authority
remains valid. `_create_place_handoff_tx` inserts the recipient chat message
for `send_now`, handoff row and creation event **before** checking original
custody. The resulting `PermissionError` or `LookupError` is caught inside
`get_tx`; the command is marked revoked and the function returns normally.
The previously inserted recipient effects therefore commit.

The reproduction invoked the actual execution and creation functions, patching
only SQL/transport collaborators and the rejected source read. Its trace was:

```text
result: revoked
INSERT recipient chat message
Insert relationship_handoffs
Insert relationship_handoff_events
Update relationship_handoff_commands
Update relationship_original_deliveries
COMMIT
```

This proves inconsistent transaction control, not delivery of the rejected
original bytes. The recipient can receive a place message/handoff even though
the sender is told the command was revoked.

**Applied:** validate and lock all required original authority before any
recipient effects. **Regression still required:** disposable-Postgres prepare → source
expiry/revocation → execute; assert revoked command and zero new recipient
messages, handoffs and creation events. The review reproduction was offline,
not a real-Postgres execution.

## R02 — Apply release eligibility to both Places reading discovery and exact reads

**Location:** [Places collections](../../travel-agent/backend/places/collections.py),
lines 187–191 and 252–260.

The new collection lists public Source records directly, exposing their claim
and interpretation preview. The exact reader calls `select_place_content`
without authenticated viewer or active-release scope. Both bypass the checks
used by `compile_eligible_content` in the existing entity reader.

With `WORLDFOUNDRY_DOGFOOD_SERVING_ENABLED=true`, accepted/public content still
requires a current per-entity internal release and eligible viewer. Public
classification alone is insufficient. The same fixture produced:

```text
governed compiler, no release scope: 0 selected
new reading collection, no release scope: 1 public reading
new exact reader, no release scope: full headline/body returned
```

An authenticated account outside the permitted release can consequently
discover and read material withheld by the governed reader. This concerns
release eligibility for public-classified content; the probe did not establish
private-memory disclosure.

**Applied:** carry the actor through both paths and reuse the canonical release,
cohort and current-source eligibility checks. **Regression:** outsider,
unreleased entity, revoked release and eligible-cohort cases for both discovery
and exact content. Treat these two paths as one defect, not duplicate findings.

## R03 — Attached originals must respect withdrawal of place-pull consent

**Location:** [original delivery policy](../../travel-agent/backend/domains/relationships/original_delivery_policy.py),
lines 100–108 and 142–149.

Create/prepare accepts `selected_original` together with `place_pull`. When the
recipient disables the sender's pull grant, the parent place reader correctly
withholds the handoff. `attached_handoff_is_current`, however, checks only pair
membership, handoff status and expiry. It never reads delivery mode or the
current pull grant. Original list, metadata and byte/text readers rely on this
weaker gate, leaving the companion readable and eligible for receiving surfaces.

Executing the actual policy functions against identical synthetic rows with
pull consent disabled returned `False` for the parent and `True` for the
companion. The consent writer only changes the grant row; it does not revoke
the original delivery automatically.

**Applied:** share the applicable current parent-authority checks, including
pull consent, while preserving the intentional rule that dismissal alone is
not withdrawal. **Regression:** revoke consent after delivery and check list,
metadata, content and Home projection; separately retain dismissal behavior.

## R04 — Preserve withdrawal controls independently of new-send eligibility

**Location:** [Intake Source screen](../../travel-app/app/you/intake-submissions/[submissionId].tsx),
lines 129–135 and 197.

After an original is sent, disconnect the eligible relationship and reopen the
Source. `activeSentDeliveries` filters sender-owned grants against the current
eligible-recipient list. If no recipients remain, the entire control returns
`null`. The sender cannot withdraw the still-active grant through this UI.

Backend sender history and withdrawal intentionally remain available after
disconnection. Re-establishing an eligible relationship can make the old grant
readable again, so hiding its controls is consequential.

**Applied:** sender-owned grants are no longer filtered by current recipient
eligibility, and existing-delivery/withdrawal rendering is independent of the
recipient picker loading/error/empty branches. **Focused regression:** remove
the final eligible recipient after Send and verify the persisted grant and
Withdraw remain usable; unavailable/loading recipient selection remains covered
by the rendering branches. New-send eligibility remains restricted. Persisted
native-device reproduction is still required before calling the finding fully
verified.

## R05 — The Source worker calls an unsupported result serializer signature

**Location:** [Source queue job](../../travel-agent/backend/workers/source_contribution_jobs.py),
line 60; result definition in
[canonical worker](../../travel-agent/backend/root_projection/v2/source_contribution_worker.py),
lines 115–143.

`run_source_contribution_workflow` returns a plain
`SourceContributionWorkerResultV1`, not a Pydantic model. Its `model_dump(self)`
already returns JSON-compatible values and accepts no keyword arguments.
The new adapter always calls `result.model_dump(mode="json")`.

Executing the actual decorated job with the canonical call patched to return
its real result type produced:

```text
worker job terminal failure: run_root_source_contribution (... exc=TypeError)
TypeError: SourceContributionWorkerResultV1.model_dump() got an unexpected keyword argument 'mode'
```

Every normal enabled-worker return hits this error. Successful canonical
generation may already have committed, so this does not prove that generated
content is lost; it does make queue completion and terminal-failure telemetry
incorrect. The disabled-worker early return is unaffected.

**Applied:** use the actual serializer contract or deliberately convert the
result to a validated model. The controlled worker now also has a gated,
deterministic due-work sweep that re-enqueues durable workflow rows after a
restart without creating new work. **Focused regression:** the queue-entry
serializer contract and recovery registration/enqueue behavior pass. Actual
Arq/Redis execution with completed, not-claimed and expired result objects
remains unrun.

## R06 — Expanded geography is incompatible with Home's eight-anchor limit

**Location:** [Home portfolio](../../travel-agent/backend/root_projection/v2/home_portfolio.py),
lines 322–326; [Source listing](../../travel-agent/backend/core/place_content_sources.py),
lines 185–186.

`resolve_context_place_ids` returns roots plus all descendant Places. The new
child-Source listing rejects more than eight IDs as though they were eight
top-level anchors. A city with eight descendants or a multi-destination Trip
can exceed this bound. Home catches the `ValueError` and drops all public
content from that reader.

An offline probe invoking the actual Home `places_context` reader gave:

```text
8 expanded IDs -> 1 public candidate; 8 content-owner calls
9 expanded IDs -> 0 public candidates; 0 content-owner calls
```

**Applied:** batch expanded scopes at the existing per-read bound and preserve
useful results for large scopes; do not silently empty the whole reader.
**Regression:** one city with more than eight descendants and a multi-city
Trip. Actual deployed subtree sizes and runtime query cost were not measured.

## R07 — Practical fit rejects entity kinds the app explicitly offers

**Location:** [value composition](../../travel-agent/backend/lived_experience/value_composition.py),
lines 520–526; mobile exposure in
[ObjectPageRebuild](../../travel-app/components/places/ObjectPageRebuild.tsx),
lines 945–959.

The request parser, candidate adapter and canonical readers support `site`,
`accommodation` and `experience`. `_assessment_place_read` recognizes only
`place`, `venue`, `area` and `city`. The other kinds always become unknown
because their exact target is discarded before matching owner evidence.

Using identical valid place/route evidence and changing only the resource kind:

```text
venue -> supported; fits the window
site / accommodation / experience -> unknown; exact place owner read unavailable
```

Mobile reachability was traced through site/experience pages and selected-reading
accommodation pages, which pass `entity.ref.type` into `PracticalVisitCheck`.

**Applied:** share the actual supported canonical-kind set. **Regression:**
positive and negative fit results for every type exposed by the app, preserving
exact identity and current-evidence checks.

## R08 — Primary Plan inspection drops the arrangement purpose

**Location:** [Plan interactions](../../travel-app/hooks/usePlanBlockInteractions.tsx),
lines 175–178 and 188–191; receiving gates in
[object projection](../../travel-app/components/places/objectPageProjection.ts),
lines 432 and 593.

The primary “Open details” action sends `tripId`, `blockId` and the return token,
but omits `openingPurpose: "arrangement"`. Receiving screens obtain purpose
from that explicit parameter. The newly purpose-aware object projection then
suppresses confirmed arrangement facts, timing and confirmation reference,
even when the backend returns them.

The separate itinerary-object Place button sets the correct purpose. A probe
of the actual projection with the same confirmed stop produced no arrangement
fact/body under `{}`, and exposed them under `{purpose: "arrangement"}`.

**Applied:** set arrangement purpose in both primary route branches.
**Regression:** primary Plan inspection → venue/experience details should show
the exact stop's current arrangement and preserve return state.

## R09 — Arrangement timestamps silently use the device's timezone

**Location:** [object projection](../../travel-app/components/places/objectPageProjection.ts),
lines 596–602 and 436–443.

Both arrangement formatters call `toLocaleString` without `timeZone`. For a
New York user inspecting a Lisbon reservation represented as
`2026-09-21T19:00:00+01:00`, the actual projection says:

```text
Confirmed for Lisbon · Sep 21, 2:00 PM. Confirmation ABC.
```

The reservation is at 7 PM Lisbon time. The text provides no device-time
qualifier, so it misrepresents a concrete arrangement while the person plans
from another timezone. Date-boundary cases can show the wrong day too.

**Applied:** preserve the wall-clock represented by an explicit ISO offset in
both fact and body, carry the existing Trip/primary-destination schedule
timezone through owner/API projection, and use it to format UTC-stored instants.
Missing zone evidence receives a qualified fallback rather than an unlabeled
device-local value. Focused regressions cover schedule-zone propagation and the
Lisbon conversion; persisted data, cross-device zones, midnight/DST boundaries
and native rendering remain required acceptance evidence.

## R10 — Rehearsal cleanup is not isolated by run

**Location:** [Home child-Source provisioner](../../travel-agent/scripts/provision_home_child_source_rehearsal.py),
lines 321–327; provisioning reuse at 147–168.

Source observations and primitives are keyed by `run_id`, but every run reuses
one global venue `FIXTURE_SLUG`. Cleanup unconditionally deletes that venue,
even when the supplied run has no corresponding fixture rows. Provision run A,
then clean absent run B: cleanup targets A's venue. Overlapping runs also
invalidate each other's exact content destinations.

The local-database and explicit database-name guards reduce scope; they do not
establish run ownership of this row.

**Applied:** give the venue a run-specific identity, and clean only that exact
run-owned venue. **Regression:** A/B coexistence,
cleanup of a missing run and idempotent cleanup. This is a static SQL-selector
finding; no destructive fixture command was executed during review.

## R11 — Regenerate the Life organization cursor contract

**Location:** [full OpenAPI snapshot](../openapi.json) and
[app projection](../openapi.app.json),
`GET /api/root-projections/v1/life/organization/groups`, cursor parameter;
runtime route in [root projections](../../travel-agent/backend/api/routes/root_projections.py),
lines 990–993.

The committed snapshots advertise cursor `maxLength: 512`; runtime exports
`maxLength: 768`. The exact full-snapshot freshness check failed. Structural
comparison found this one schema difference, rather than mere JSON ordering.

**Applied:** refresh the full snapshot and app projection through the contract
generators, review the full
snapshot, app projection, generated types and consumers together. No hand edit
of generated files. **Regression:** freshness and projection/type parity checks.
The initial mismatch blocked snapshot freshness; the refresh corrects that
field. The full contract gate remains separately blocked by its recorded
policy/consumer findings. A mobile runtime failure from the wider accepted
maximum was not established.

## Important limitations and investigated non-findings

- **Generation recovery remains incomplete.** Dispatch occurs on explicit POST;
  enqueue can return `None`, shared Arq defaults to `max_tries=1`, and there is no
  production caller draining `list_due_source_contribution_workflows`. Pending
  or retryable work therefore has no automatic recovery on this rail after an
  enqueue failure, a consumed disabled job or a transient execution failure.
  GET polling cannot re-enqueue it. The existing controlled-worker receipt
  explicitly excludes production scheduling, so this is recorded as an
  implementation/readiness limitation rather than another confirmed regression.
  Resolve it before claiming reliably completed background preparation.
- **Original-delivery fixture failure cleanup needs follow-up.** Sender/source
  rows are committed before delivery creation; later failure may orphan them,
  while cleanup locates them through a completed delivery. The failure path
  was inspected but not executed; do not count it as a reproduced bug here.
- **Shared fixture profile restoration has concurrency risk.** Home fixture
  cleanup restores a supplied home-location snapshot unconditionally. Whether
  this violates the exclusive QA-account operating contract was not settled.
- **Negative-fit outer expiry was examined and excluded.** Mobile separately
  suppresses expired assessment prose, so the outer-expiry difference alone
  did not establish a distinct user-facing defect.
- **Speculative Plan races were excluded.** Send revalidates audience and
  revision. A separate stale-answer/privacy defect was not established by
  the inspected paths.

## Verification evidence and boundaries

Review used Python 3.13.0 in the backend virtual environment and offline
fixtures. The measurement launcher itself reports system Python 3.14.6; those
are different interpreter roles. No live providers, Redis jobs, disposable
Postgres mutation, simulator run, full `make verify`, or visual-parity review
was performed in this review turn.

Measured parent runs, from the lane root:

```sh
python3 scripts/measure_verification.py --label review-source-worker-existing-tests -- zsh -c 'cd travel-agent && PYTHONPATH=. .venv/bin/python -m pytest -q tests/api/test_source_request_http.py tests/core/test_root_source_contribution_feature_flag.py tests/research_agent/test_worker_wiring.py -m "not requires_postgres and not requires_api_keys and not requires_dogfood_wedge"'

python3 scripts/measure_verification.py --label review-home-places-life-focused -- zsh -c 'cd travel-agent && PYTHONPATH=. .venv/bin/python -m pytest -q tests/places/test_collections.py tests/core/test_value_composition.py tests/core/test_place_content_sources.py tests/root_projection/test_home_portfolio.py tests/life/test_original_refind.py tests/life_projection/test_life_organization_reader.py tests/life_projection/test_source_evidence.py -m "not requires_postgres and not requires_api_keys and not requires_dogfood_wedge"'

python3 scripts/measure_verification.py --label review-openapi-freshness -- zsh -c 'cd travel-agent && PYTHONPATH=. .venv/bin/python scripts/check_openapi_snapshot.py --ci'
```

- Worker admission/registration packet: **28 passed**, 3.581 seconds measured.
- Home/Places/Life packet: **117 passed**, 4.075 seconds measured. Together
  these two non-overlapping packets passed **145 tests**, with no skips reported.
- OpenAPI freshness before the fix: **failed**, 7.110 seconds; R11. The
  refreshed snapshots now agree; the full freshness command still encounters
  the pre-existing expired API-operation policies listed in its output.
- Actual worker-wrapper probe: **failed as expected for R05** with the exact
  TypeError above; canonical execution and deployment builders were patched,
  while the decorator, wrapper and result object were real. Its measured
  record includes the complete reproduction command.
- Reviewer probes for R01–R03 and R06–R09 were executed offline without
  persisted measurement receipts; their specific evidence boundaries are
  documented above. They do not constitute PostgreSQL or native acceptance.

Local measured logs/JSON live under `docs/reliability/runs/`, with labels
`review-source-worker-result`, `review-source-worker-existing-tests`,
`review-home-places-life-focused` and `review-openapi-freshness`.
Passing existing tests do not contradict the findings: the reproduced edge
conditions are outside those assertions.

Documentation validation: new-document governance passed, and `git diff --check`
passed. The full inventory check still reports the already-existing unclassified
`practical-judgment-producer-acceptance-brief-2026-09-09.md`; the living-link check
reports five already-existing roadmap links to missing design-review documents.
Their references and the unclassified file predate this review window's root
baseline. No new-document link error was reported. These baseline documentation
issues were left unchanged and are not counted in R01–R11.

September 21 roadmap/ledger rebaseline validation: measured
`python3 scripts/check_docs.py --governance --inventory --spine --links`
passed the spine and new-file governance checks (no new documents); inventory
and links still failed on the same one unclassified document and five missing
design-document links above. Receipt label: `roadmap-rebaseline-docs`, under
`docs/reliability/runs/`. This is a documentation-only update; no product suite,
full `make verify`, device run or publishing was performed.

## Recommended correction order

**Current:** R04 and R09 code-level corrections are complete; close their
outstanding persisted-database and native-device evidence boundaries in the
correct environment. Include Source recovery
in the next reliably supplied-value package; registration/serialization fixes
do not establish recovery. Do not rerun the initial repair list as though the
implemented changes were absent, or call the ledger closed based on happy-path
test totals. Independent feature implementation can proceed outside these
affected ownership/file boundaries.

The following preserves the initial repair ordering and its rationale:

1. **Authority and transaction correctness:** R01, R03 and R04; review R02's
   release-policy reuse in the same correction wave with a separate file owner.
2. **Generation execution:** R05. Decide the bounded retry/recovery posture
   before expanding controlled generation activation.
3. **User-visible completeness:** R06–R09; Home supply, practical kinds and
   arrangement navigation/time are independent enough for parallel owners.
4. **Safe verification and contract synchronization:** R10–R11, then focused
regressions and the coordinated delivery gates before any landing claim.

After the fix pass, the locally runnable packets were rerun: backend focused
content/relationship/Places tests passed **54 tests**, and the mobile projection
and original-sender suites passed **38 tests**; TypeScript compilation and
backend Ruff/compile checks also passed. These are execution evidence for the
changed code, not a substitute for the unavailable disposable-Postgres,
queue-environment and native-device regressions above.

Keep the [program roadmap](vesper-program-roadmap.md) and
[integration roadmap](complete-system-integration-roadmap-2026-09-05.md) as the
execution authorities. This document is a dated bug ledger, not another roadmap.
