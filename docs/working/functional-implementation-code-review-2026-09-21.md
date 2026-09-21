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

### September 21 current tuple correction

The table below is the historical baseline for the 12-hour review. The current
clean candidate after the Home timezone correction, source retry-budget proof,
supplied-experience comparison, sequence scale hardening, practical catalog
coverage, typed notice admission, native sender-withdrawal proof and semantic
state treatment is:

| Repository | Current HEAD |
|---|---|
| Workspace | `3b47cf9` (current documentation receipt) |
| Backend | `67b617d85` |
| App | `9a597abd4` |

This correction updates tuple identity only; it does not imply merge,
publication, shared-runtime activation, or production flag changes. Earlier
runtime-boundary receipts at workspace `0fd06b7` and `f127543` remain
historical; the current workspace receipt is `3b47cf9`, and the current child
heads are the Life People implementation/test commits shown above.

### September 21 latest-candidate regression packet

After the Life People depth receipt, the candidate ran the backend root
projection packet (**442 passed**), focused Life route/projection/index-projector
packet (**47 passed**), focused Home/Places/Life native packet (**54 passed**),
and persisted schedule-zone unit packet (**36 passed**). These are named
focused regressions, not `make verify`, full device acceptance, or release
evidence. They leave R05 process interruption/transient failure and R09
persisted/native cross-device/DST evidence open; they also do not prove
provider-backed supply, recurring generated content, full-scroll quality,
design parity, merge, activation or publication.

### September 21 Life · People outcome review

The Life adapter previously admitted shared Occasions to People but dropped
their shared Outcomes, and it lacked a commitment-scoped grant when a shared
Commitment had no Occasion. Backend `ef4167163`, `e9ad26f7f` and
`014313121` admit those
Outcomes only when the viewer-relative Occasion has another active participant
and admit non-private multi-participant Commitments through the existing
commitment grant, preserving grant/member refs and leaving viewer-only
material out of People.
App `76af974a0` and `9a597abd4` prove that the native row opens the exact
record while the exact Life reader receives `lens=people` (other owners keep
`lifeLens` return context); backend `014313121` also proves the depth route
returns the same shared commitment with its exact commitment grant and
destination. The latest root packet passes **442** tests, the
Life route/projection/index packet passes **47**, and the combined native root
packet passes **54**, with TypeScript and destination tests green. No new
Occasion producer, audience policy, feed, or inference is introduced; broader
attribution, media and social juxtaposition remain open.

### September 21 Life · People follow-through review

The direct Life adapter already admitted explicit `people=resolved` intake
anchors, but the shadow/index projector serialized every anchor as Time-only.
Backend `67b617d85` preserves the owner-declared lens set while keeping the
anchor private and artifact-owned. The focused anchor/projection/route/index
packet passes **59 tests**, and the root-projection packet passes **442 tests**.
No audience, person dossier, social inference or new storage path was added.

### September 21 native semantic-state treatment review

App `9b463726d` adds the shared `RootUnitStatusMeta` component to the Home and
Places semantic renderers. Pending, partial, stale and unconfirmed units retain
their supplied copy and exact navigation doors but expose an honest status;
revoked units render nothing at the native cache boundary. The backend/schema
contract is unchanged. The focused Home/Places packet passes **35 tests** and
TypeScript passes; targeted ESLint reports only the two pre-existing renderer
max-lines warnings. This closes a native sparse/pending/revocation treatment
gap for admitted semantic units, not all transport-level loading/failure,
visual parity, media breadth or release evidence.

### September 21 supplied-experience comparison review

The new Home value-depth slice is bounded to already supplied Places
experience previews. Backend `7d036bb7c` groups two to four experiences from
one section into a comparison composition over timing, length and price,
while preserving exact context/experience refs, the existing read requirement,
expiry and the single-experience aperture fallback. App `b7d025044` and
`4c53af70d` add the native comparison treatment, registry contract and exact
action-door regression. Backend focused
Home/contract/composition tests pass **80**; the combined Home/Places renderer
packet passes **80**; TypeScript, targeted ESLint, Ruff and formatting pass
(the existing Home/Places renderer max-lines warnings remain). Review found no
new service, ranking,
booking, persistence or route family and no design-parity claim is made.

### September 21 plural social perspective review

The relationship owner already supplies privacy-eligible friend activity with
bounded place names and optional exact venue IDs. Backend `c3f64589e` groups two
eligible cards into `social_plural_comparison`, preserves attribution and
combined relationship reads, and falls back to the existing single-person row
when a second perspective is absent. App `62c5982a8` renders the comparison
through the existing composition renderer and preserves exact Place doors.
The focused backend packet passes **81 tests**; the combined Home/Places app
packet passes **80 tests**; TypeScript, targeted ESLint, Ruff and formatting
pass (the existing Places renderer max-lines warning remains). No activity
feed, notification, location inference or response debt was introduced.

### September 21 canonical Places workspace follow-up

The internal `PlacesRootV2Screen` packet did not by itself prove that semantic
units reached the production `PlacesWorkspace`. App `ecdecaffe` adds that
boundary regression: a standalone `social_plural_comparison` unit from the
runtime envelope is forwarded into the canonical `PlacesSectionFeed`. The
focused workspace suite passes **16 tests**, targeted ESLint is clean, and the
app typecheck remains green. This closes an evidence gap in the receiving path;
it does not add a producer, route, rollout, storage family or design-parity
claim.

### September 21 backend runtime follow-up

The first canonical-workspace test supplied `field_units` directly and did not
prove the backend join. Backend commits `90fe88f88` (implementation) and
`5cfcae1c4` (real plural-adapter regression) broaden the runtime adapter's
standalone rail to the kinds the native Places semantic renderer actually
supports, excludes card-bound units, and rejects unsupported kinds. The focused
Places-runtime suite passes **9 tests**; the combined backend packet passes
**96 tests**, with Ruff, formatting and compilation clean. No producer, route,
store, rollout or policy surface changed.

### September 21 next-slice decision

The review does not recommend another receiving-boundary or injected-unit
proof. Backend runtime forwarding, the canonical `PlacesWorkspace` rail,
Home multi-source full-scroll/destination continuity, native sender withdrawal
and shared semantic-state treatment are now covered at their named candidate
boundaries. The next implementation should select either one consequential
sparse/pending/failure state in an already supplied root or one permissioned
Life/social downstream value whose structured inputs and authority already
exist. It must preserve substantive content, exact depth/action destination,
expiry and return; if the selected owner payload is not sufficient, leave the
gap explicit. Do not introduce a new generator, feed, store or route family
just to fill visual space.

### September 21 standalone-only feed-state repair

The prior workspace regression proved semantic-unit forwarding only when the
mature feed also rendered cards. App `66079f456` closes the remaining state
seam: a runtime envelope with an admitted renderable standalone unit and zero
mature sections now remains a feed composition, so `PlacesSectionFeed` mounts
the unit instead of showing an empty/unavailable hero. The app checks the same
native semantic renderer registry before treating the rail as content. The
focused presentation/workspace packet passes **40 tests**, TypeScript and
targeted ESLint pass. No producer, route, store, rollout or policy surface
changed.

### September 21 addressed Place-contribution region

The relationship owner already delivered recipient-authorized Place notes to
Home one at a time. Backend `953e2bc69` adds the admitted
`people_authored_region` candidate when at least two eligible notes are present;
the comparison keeps each sender's exact words and grant/handoff revision and
emits one exact `places.open_entity` action per note. A single note retains the
existing `people_note_door` path, and eligibility is checked before grouping.
App `4c507e1c4` adds the native **Addressed to you** renderer and registry
promotion. Backend root-projection tests pass **438 tests**; focused Home
renderer/smoke tests pass **32 tests**, TypeScript passes, and targeted ESLint
has no errors (the existing max-lines warning remains). No new social store,
audience policy, notification, generator or route was added. Real relationship
backing and native/device evidence are still required for a broader receipt.

### September 21 Life source/original row distinction

App `b1f37eac4` adds a bounded native comprehension treatment to the existing
Life root and complete-record readers: `source_submission` rows carry a
**SOURCE** stamp and `source_original` rows carry an **ORIGINAL** stamp. Exact
owner destinations, custody checks and lens-aware return parameters are
unchanged. The focused Life root/record/groups/primitives packet passes **34
tests**, TypeScript and targeted ESLint pass. No API, backend, schema, storage,
organization or media-reader behavior changed; this is not indexed-serving or
visual-parity evidence.

### September 21 Home surface follow-up

Home now renders the existing editorial-passage and aperture-row kinds with
distinct native anatomy while retaining the shared source, destination,
action, practical-expiry and composition contracts. App `fda51a42c` adds the
two treatments and regressions; the focused Home renderer/smoke packet passes
22 tests, TypeScript passes, and targeted ESLint has no errors. The existing
max-lines warning remains a maintainability note, not a functional failure.

### September 21 Places surface follow-up

Places now renders the existing `field_editorial_cover` read/composition kind
with a native field-reading rail, authored substance and the same source,
destination, capability and expiry behavior. App `659f572ae` adds the
treatment and regression; the focused Places root/expiry packet passes **28
tests**, TypeScript passes, and targeted ESLint has no errors. This improves
native expression of supplied Places value; it does not claim new content supply
or full Claude-design parity.

### September 21 Places starter follow-up

The admitted `field_browse_shelf` starter kind now has a native way-in tile
instead of falling through to the generic field card. The treatment preserves
the existing source, exact destination, capability and practical-expiry seams;
it does not fabricate the riso/photo media that the design manifest still
requires from a future media-bearing payload. App `17c2c4472` adds the native
treatment and root regression. The focused Places root/expiry packet passes
**29 tests**, TypeScript passes, and targeted ESLint has no errors.

### September 21 Places field-family follow-up

The admitted `field_branch`, `field_returned_understanding`, and
`field_continuity_doors` kinds now have native row, gold-rule reading, and
carry-forward door treatments. Source inspection, exact destinations,
capability actions and practical expiry remain shared through the existing
follow-up seam. App `f4a190b56` adds these treatments, a small styles module to
keep the renderer under its size budget, and root regressions. The focused
Places root/expiry packet passes **30 tests**, TypeScript passes, and targeted
ESLint has no errors. This is native coverage of admitted payloads; it does
not claim returned-understanding supply or full Places design parity.

### September 21 Places balanced-field follow-up

When the current scope has no eligible World Field lead (including a feed made
entirely of deferred encounter-state sections), the backend now emits the
admitted `field_balanced_fallback` kind with an explicit absence explanation
and the existing search/map actions. The native client renders that state as an
open-field orientation treatment and preserves exact expiry/source/action
behavior. Backend `a516ce26d` adds the producer contract and regression;
focused backend Places packets pass **39 tests**. App `34c3651c1` adds the
native treatment and regression; the focused Places root/expiry packet passes
**31 tests**, TypeScript passes, and targeted ESLint has no errors. This closes
an honest sparse-state seam; it does not add provider acquisition, media supply
or a recommendation.

### September 21 Places evidence-register follow-up

The existing feature-flagged Places register producer now has a v2 receiving
path when it supplies an approved verdict, viewer-owned history log, or fresh
change register. The backend preserves the register lines and evidence
revision as a presentation-neutral `path_evidence_apparatus` composition; the
native client renders an evidence list with the existing exact Place source
door and expiry behavior. Backend `aa96caff7` adds the adapter regression;
focused backend Places packets pass **40 tests**. App `e601a9dfd` adds the
native evidence treatment and regression; the focused Places root/expiry packet
passes **32 tests**, TypeScript passes, and targeted ESLint has no errors. This
does not enable `PLACES_REGISTERS_ENABLED`, add a new producer/store, or turn an
unqualified register into a recommendation.

### September 21 post-receiving-surface recheck

The Places receiving surface then gained a native treatment for the already
admitted `social_attributed_evidence` unit. The renderer keeps the relationship
owner's bounded place-name relation visible, preserves source inspection and
exact destination doors, and runs the existing practical-expiry fence before
rendering. App commit `6aedd2c00` adds the renderer and root-screen regression;
27 focused Places root/expiry tests, TypeScript and targeted ESLint pass. This
closes a presentation gap in the supported social payload only. It does not
certify multiplayer supply, general social policy, or full visual parity.

### September 21 social destination follow-up

The same recipient-consented friend activity path now carries up to three
owner-provided venue refs into the Places unit and exposes named exact-place
actions. Name-only rows remain fail-closed. Backend `f9fa3d82b` (with the
preceding venue-action commit `cee8a4474`) and app
`6c8b0cd14` add the contract and native action regressions; the backend Places
contract/runtime packet passes 39 tests and the app Places root/expiry packet
passes 27 tests, with TypeScript and targeted ESLint clean. This closes an
exact-destination gap in the existing social receiving path only.

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
changed all 11 areas; the later R04/R09 correction closes their code-level gaps.
The evidence closeout below now covers disposable-Postgres authority/readback,
three named native receiving paths and one real Arq/Redis wrapper execution;
recovery/failure behavior and the remaining edge-case matrices remain open.**
The other nine retain their recorded implementation status and stated
verification limits; this recheck did not recertify them. The implementation has useful
end-to-end paths, but happy-path evidence misses
authorization changes, realistic place hierarchy sizes, non-venue practical
checks, entry-point differences, timezone handling, and the actual queue wrapper.
This ledger records all confirmed findings from this review, not a guarantee that
every defect in the change set has been discovered.

## September 21 recovery follow-up

The functional lane then closed the remaining code-level hole in the Source
recovery fence at backend commit `79175eaed` (`fix: close exhausted source
worker leases`). The existing minute recovery sweep now terminalizes only
`running` Source workflows whose lease has expired **and** whose attempt count
has reached the durable maximum; pending, retryable, or below-budget work still
flows through the ordinary deterministic re-enqueue path. The terminalization
uses the existing workflow event/lease fence and records
`source_worker_lease_exhausted` without creating new work or broadening worker
admission.

Focused worker/workflow tests pass **29 tests** with Ruff, format and compile
checks. The new SQL reaper proof and the existing workflow/source-attempt
packet pass **17 disposable-Postgres tests**; the retry-budget proof adds an
additional **8 disposable-Postgres tests**. This proves branch selection,
durable terminalization, retry scheduling and sweep wiring. A real
process-kill/restart queue run remains the final R05 evidence case.

The app then corrected a separate Home v2 presentation seam at commit
`4d51c1db0` (`fix: honor Home timezone in world read`). The orientation anchor
now formats in the canonical timezone carried by the server-authored week
shape, with an explicit UTC fallback for an unsupported zone. The Home v2
screen suite passes **14 tests**, plus TypeScript and ESLint; this is a focused
presentation correction, not native visual certification.

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

- Backend `ea403ec0a`, `2935757fe`, `79c4b1d8a`, `70b607e34`, `7f993a3cb`,
  `c84d0ea31` and `fcec68bfe` — authority gates,
  release-scoped reading, bounded geography batching, practical entity coverage,
  worker serialization, async DB boundaries, run-isolated rehearsal fixtures
  and schedule-timezone propagation.
- App `44872d0c2` — sender withdrawal history, arrangement-purpose navigation,
  and schedule-zone-aware arrangement time presentation.
- Workspace contract refresh — `docs/openapi.json` and
  `docs/openapi.app.json` now include the relationship `schedule_timezone`
  field and agree with the route's 768-character cursor maximum.

The fixes preserve the original findings and their evidence boundaries. Queue
recovery/failure and the remaining edge-case regressions remain required
acceptance checks. The prior attempt reported a missing `openai` dependency and no configured
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

Before the evidence closeout below, no disposable-Postgres, queue-environment or
native-device acceptance had been established by this correction pass. The
ledger should treat R04 and R09 as code-fixed with their stated persisted/native
matrices still open.

### September 21 evidence closeout

The isolated lane subsequently ran the supported local runtime with disposable
Postgres on `localhost:61460`, API `http://127.0.0.1:61463`, and simulator
`D7C8FEF4-237B-4347-841C-6FE920BFABFA` (iOS 18.2). The following receipts are
now executed evidence, not plans:

- Disposable-Postgres persistence/readback packet: **8 passed, 22 deselected**
  for original-delivery, persistence, Life exact-refind and Place presentation;
  **2 passed, 47 deselected** for relationship handoffs, source-request
  delivery, entity relationship reads, social sections and original-delivery
  content. The commands used `TEST_DATABASE_DISPOSABLE=1` and the exact lane
  `DATABASE_URL`; no ambient or production database was used.
- `run-life-real-source-return.sh`: passed. A real retained text source was
  created, rendered in Life, opened through the exact original-material reader,
  returned to Life, withdrawn, and absent after owner cleanup.
- `run-home-places-real-save-readback.sh`: passed. A real Save was removed via
  the native Place owner, absent from canonical Saves and Home, restored, and
  read back through Home → Places with a non-empty brief.
- `run-places-real-social-pull.sh`: passed after restarting only the lane API
  with `PLACE_HANDOFF_PULL_ENABLED=true`. The recipient-consented note appeared
  in the scoped `From your people` section, opened the canonical venue, returned
  to Places, and disappeared after fixture cleanup. The flag was not enabled in
  the app bundle, production, or any shared runtime.
- `run-cross-root-home-places-life.sh`: passed. Home's addressed social note
  opened the exact Place and returned; Places remained reachable; Life's Places
  lens opened the exact retained original and returned to the same entry. The
  runner verified both temporary fixtures were absent after cleanup.

These receipts close the earlier persisted/native boundary for the named happy
paths. A real Arq/Redis `run_root_source_contribution` job also completed the
`not_claimed` result path. They do **not** close R09's persisted/native timezone
matrix or R05's transient failure/restart recovery behavior, or the full
cohort/release and design-parity gates. R04's native sender-withdrawal matrix
is now closed at its exact one-recipient text-original scope; the review ledger
therefore remains open and should not be marked release-ready.

### September 21 R05 runtime closeout attempt

Docker Desktop and the lane's disposable Postgres/Redis runtime were available
for a bounded process-restart rehearsal. A real Source workflow was inserted,
enqueued with the registered `run_root_source_contribution` job, and executed by
the actual `audio_jobs.WorkerSettings` process. Postgres readback reached
`status=completed`, `outcome=producer_silence`, `attempt_count=1`, with no
result readback; the worker then shut down cleanly with **33 jobs complete, 0
failed, 0 retries**. This is useful confirmation that the current workflow can
complete on the live local rail, but it is **not** process-interruption evidence:
the Source job finished before the worker could be terminated. The worker also
reported unrelated pre-existing fixture-cron errors; those are outside this
workflow and do not change its result.

R05 therefore remains open. The remaining evidence is specifically a
still-current workflow interrupted while executing and recovered after worker
restart, plus a transient provider failure/retry case. Do not relabel the
successful completion as restart safety, and do not broaden this edge rehearsal
into production generation activation.

Focused correction receipts on the candidate tuple:

- Backend relationship/presentation packet: **35 passed** with Ruff check and
  format verification.
- Source worker/registration/recovery packet: **27 passed** with Ruff check and
  format verification; the separate local Arq/Redis receipt below covers one
  wrapper result, while recovery/failure behavior remains unverified.
- Broader Home/Places/root backend packet: **1,142 passed**, with 42 explicitly
  deselected environment/provider cases. This is the current offline owner,
  selection and route packet; it is not populated-database or native acceptance.
- App sender/object-projection packet: **40 passed**; `npx tsc --noEmit`
  passed. ESLint reported no errors and one existing-style max-lines warning
  on the sender screen (803 lines versus the 800-line budget).
- Broader Home/Places/Life mobile packet: **422 passed** across 47 suites,
  including the real Home v2 renderer, Places object/workspace surfaces, Life
  original/refinding paths and return-state tests.
- The canonical OpenAPI projector regenerated `docs/openapi.app.json` and
  `travel-app/utils/api/schema.gen.ts` with `schedule_timezone`. The normal
  `sync-types` audit remains blocked by the pre-existing expired API-operation
  policy findings and missing consumer; this is not claimed as a full gate pass.

## Defect index

| ID | Priority | Defect | Owning area | Status |
|---|---|---|---|---|
| R01 | P1 | Rejected original can still commit a recipient handoff/message | Relationships transaction | Fixed; disposable-Postgres revocation regression passes |
| R02 | P2 | Places reading bypasses active release/cohort eligibility | Content / Places | Fixed; governed outsider/cohort matrix still required |
| R03 | P2 | Pull-consent revocation leaves attached original readable | Relationships read policy | Fixed; disposable-Postgres attached-read regression passes |
| R04 | P2 | Sender loses withdrawal controls after relationship disconnect | Mobile original sharing | Code-fixed; real API and native sender-control rehearsals pass, including revoked readback; broader audiences/media remain out of scope |
| R05 | P2 | Source worker throws while serializing its actual result type | Worker adapter | Serializer and exhausted-lease recovery code fixed; 29 focused tests, 25 disposable-Postgres tests, and real wrapper/expired recovery pass; only process-restart queue evidence remains open |
| R06 | P2 | Nine expanded place IDs silently remove Home public supply | Home / Places scope | Fixed with 8-ID batching; nine-ID scale regression passes; deployed scale/cost still unmeasured |
| R07 | P2 | Site, accommodation and experience fit checks cannot succeed | Practical assessment | Fixed; positive catalog-kind owner-adapter matrix passes |
| R08 | P2 | Primary Plan details entrance hides arrangement information | Plan / object navigation | Fixed; typecheck passes |
| R09 | P2 | Reservation time is shown in device timezone without a label | Object presentation | Code-fixed; focused schedule-zone/UTC conversion passes; named native packets pass; persisted/native timezone matrix still required |
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
recipient effects. **Verified:** the dedicated disposable-Postgres regression
at backend `c84d0ea31` passed (`1 passed`): prepare → source revocation →
execute returns a revoked command and leaves zero recipient messages, handoffs
or creation events. The test also covers the prepared original's revocation
state. A separate source-retention-expiry variant is not claimed; the existing
prepare contract prevents a delivery from outliving source retention, so that
case remains a distinct boundary if the contract later permits it.

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
not withdrawal. **Verified:** backend `fcec68bfe` adds the attached-original
fixture to the disposable-Postgres relationship packet. With consent enabled,
`get_original_delivery_source_access` returns the exact text; after consent is
disabled it raises `PermissionError` and the readable pull list is empty. The
selected packet passed **7 tests, 1 deselected**. Native capture of this exact
attached-original withdrawal and a Home serialized-content assertion remain
outside this receipt; they are not claimed here.

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
by the rendering branches. New-send eligibility remains restricted.

**September 21 API rehearsal:** the new sender-mode disposable fixture used an
existing sender account, created a temporary recipient and active delivery,
removed that recipient from the conversation after delivery creation, and
verified through the real local API that sender history still contained the
delivery while eligible-new-recipient results did not. Posting Withdraw returned
`revoked`, revision `1`; cleanup removed the delivery and temporary recipient
without deleting the existing sender. The native sender flow then ran on the
iOS 18.2 simulator: it scrolled to the below-fold sender history, showed
Withdraw after recipient disconnection, removed the control after the gesture,
and kept the original material visible. The runner re-read sender history and
confirmed the exact delivery was `revoked` at revision `1` before cleanup.
This closes native presentation at the exact one-recipient text-original
scope; it does not broaden audience or media policy.

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
restart without creating new work. **Verified:** with Redis on the isolated
lane and the real `audio_jobs.WorkerSettings`, an enqueued
`run_root_source_contribution` job for a nonexistent workflow completed with
the serialized result `status=not_claimed` and `workflow_id`; the worker shut
down with **18 jobs complete, 0 failed, 0 retries**. This proves the actual
registered wrapper/result serialization path without provider work.

**Additional recovery evidence:** in the same isolated Postgres/Redis lane, a
real expired Source work item was inserted for a disposable user. The actual
`resume_due_source_contribution_workflows` sweep returned **1** and enqueued
the deterministic Arq job; `audio_jobs.WorkerSettings` then ran the registered
`run_root_source_contribution` wrapper, which returned `status=expired`.
Postgres readback showed `status=failed_terminal`,
`last_error_code=source_work_item_expired`, `last_error_category=stale_state`
and `attempt_count=1`. A second recovery sweep returned **0**, proving a
terminal expired row is not re-enqueued. This closes the due-work → queue →
terminal stale-state recovery boundary. Restart recovery for a still-current
row, transient provider failure/retry exhaustion, and disabled-worker behavior
with a due row remain unverified. The worker process also ran unrelated
fixture cron jobs that logged pre-existing intake/semantic errors; those were
outside this Source workflow and are not included as R05 success evidence.

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
**Regression:** the focused scale case now passes in backend commit
`7fc1858df`: nine expanded IDs are read as eight-plus-one owner calls and all
nine current records survive the bounded listing. Actual deployed subtree
sizes and runtime query cost were not measured.

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
backend commit `248237edd` now covers positive supported results for `venue`,
`site`, `accommodation`, and `experience` through the real owner adapters,
preserving exact identity and current route evidence. Unsupported and stale
owner-read cases remain covered by the existing matrix; no provider booking
behavior is implied.

### September 21 follow-through packet

The sequence and practical-kind corrections were rerun together with the
content-source and Home portfolio suites. The combined backend packet passes
**94 tests**. The native sequence/renderer and Home smoke packet passes **20
tests**; TypeScript, Ruff, formatting and compilation are green. The stale
Home assertion corrected in backend `17f20921b` preserves the intended public
reading-limit text rather than weakening the contract.

This closes the local regression gap for R06 and R07 at the stated evidence
boundary. It does not measure deployed expanded-place cost, prove a
provider-backed fit run, establish recurring source generation, or close the
remaining R05/R09 environment-dependent evidence. The ledger therefore remains
active.

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

The initial review used Python 3.13.0 in the backend virtual environment and
offline fixtures. The measurement launcher itself reports system Python 3.14.6;
those are different interpreter roles. The later evidence closeout (above) ran
only the explicitly disposable Postgres, local simulator and one isolated
Redis/Arq wrapper packet; no live provider, recovery/failure queue scenario,
full `make verify`, or visual-parity review was performed.

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
- Actual worker-wrapper probe: the original reproduction **failed as expected
  for R05** with the exact TypeError above; canonical execution and deployment
  builders were patched, while the decorator, wrapper and result object were
  real. A later real wrapper run completed the `not_claimed` path, and a real
  expired due-work recovery run reached durable `failed_terminal` readback.
- Reviewer probes for R02–R03 and R06–R09 were executed offline without
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

**Current:** R01 and R03 are now closed for their disposable-Postgres
revocation/readback cases. R04 and R09 code-level corrections are complete, and
the named Life/Home/Places happy paths now have disposable-database and native
receipts. R04's native sender-control matrix is now closed at the stated
one-recipient text-original scope; close the remaining timezone matrices in the
correct environment. Include Source recovery
in the next reliably supplied-value package; registration/serialization fixes
do not establish recovery. Do not rerun the initial repair list as though the
implemented changes were absent, or call the ledger closed based on happy-path
test totals. Independent feature implementation can proceed outside these
affected ownership/file boundaries.

The following preserves the initial repair ordering and its rationale:

1. **Authority and transaction correctness:** R04; review R02's release-policy
   reuse in the same correction wave with a separate file owner.
2. **Generation execution:** R05. Decide the bounded retry/recovery posture
   before expanding controlled generation activation.
3. **User-visible completeness:** R06–R09; Home supply, practical kinds and
   arrangement navigation/time are independent enough for parallel owners.
4. **Safe verification and contract synchronization:** R10–R11, then focused
regressions and the coordinated delivery gates before any landing claim.

After the fix pass, the locally runnable packets were rerun: backend focused
content/relationship/Places tests passed **54 tests**, and the mobile projection
and original-sender suites passed **38 tests**; TypeScript compilation and
backend Ruff/compile checks also passed. The later native sender-control run is
recorded above and in the current candidate tuple. These are execution
evidence for their named scopes, not a substitute for the remaining
disposable-Postgres, queue-environment and persisted/native timezone matrices.

Keep the [program roadmap](vesper-program-roadmap.md) and
[integration roadmap](complete-system-integration-roadmap-2026-09-05.md) as the
execution authorities. This document is a dated bug ledger, not another roadmap.
