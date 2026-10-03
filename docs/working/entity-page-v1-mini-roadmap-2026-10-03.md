---
doc_type: working
status: active
owner: Entity lane / 01a1031d-fc9a-7c10-ad71-bac294d72e5c
created: 2026-10-03
last_verified: 2026-10-03
expires: 2026-11-02
why_new: The founder requested an independent Entity Page v1 implementation lane and a mini roadmap first. The September acceptance plan preserves a different receiving-lane assignment and historical C0–C8 receipts; this finite plan owns the new lane, current baselines and completion sequence without rewriting that history.
supersedes:
  - September 6 current assignment in entity-system-acceptance-plan-2026-09-05.md, for this Entity Page v1 lane only
source_of_truth_for:
  - entity-page-v1-implementation-sequence
depends_on:
  - ../../travel-app/docs/surfaces/entity-object/contract.md
  - ../systems/contribution-and-consequence.md
  - entity-system-acceptance-plan-2026-09-05.md
---

# Entity Page v1 implementation roadmap

**Current package — central Goal regroup, October 3:** follow G1 → G2 in the
[central execution plan](vesper-program-roadmap.md#central-execution-goal--october-3).
The prior EP0–EP4 receipts below close their bounded local turn; they do not
establish whole-lab parity or accepted integration. Central owns publication.
First reconcile the current raw-file hashes, board 14 versus board 09, and the
newer one-field decision; deliver an exact reference/authority and gap matrix.
Then repair demonstrated reading gaps using existing owner data, with focused
regressions for purpose selection/omission, sparse/no-photo and originals.
The current body composer appends every research paragraph after purpose blocks;
prove the intended cases before claiming that it matches board 14. An absent
discriminator is a contract dependency, not permission for semantic guessing.
Board 16 is tracked by Adaptive G4 as a contract handoff, not silently included
in core v1 implementation. Native/design parity remains unverified until its
specific evidence exists. Preserve old failing receipts and revalidate the
small accessibility slice against the accepted API policy baseline.

Finish the existing venue, site and experience page as one coherent product
surface: open the correct place, understand its available evidence, inspect the
selected original, Keep or share through existing owners, enter the supported
question flow, and return to the originating surface correctly.

This lane can complete the core implementation independently of the four
infrastructure lanes. It consumes their accepted contracts; it does not take
over Collection composition, context generation, root feeds or verification
infrastructure. The initial turn created the lane and plan. Current work follows the G1/G2
package above; EP0–EP4 below retain that earlier turn's receipts.

**There are two finish lines.** Implementation completion means reviewed code,
reconciled contracts, appropriate local evidence and accepted merges. Product
release additionally needs the current native, authenticated and accessibility
evidence required by the surface contract, followed by an explicit activation
decision. Those device checks remain deferred. Neither a merge nor this plan
claims they passed.

## Scope and authority

Use the [Entity surface contract](../../travel-app/docs/surfaces/entity-object/contract.md)
for the current runtime boundary and the
[contribution contract](../systems/contribution-and-consequence.md) for authority,
retention and effects. Accepted newer product decisions govern target meaning;
EP0 must reconcile a difference with existing runtime contracts explicitly.
The [September acceptance plan](entity-system-acceptance-plan-2026-09-05.md)
retains the independent core, research and people gates. Its completed repairs
are historical evidence, not a backlog to repeat.

The local design input is
`~/Downloads/vesper-entity-object-handoff-lab/project/`. Boards 06 and 06B provide
the page anatomy and size cases. Board 14 supplies the later purpose-sensitive
reading direction: stable identity and shell, with purpose affecting selection,
order and emphasis of existing evidence. Board 09's earlier invariant-body
rule is superseded for that target. Boards 07/08 mirror older engineering
proposals; current API contracts win over their obsolete endpoint suggestions.
Board 16's requested-work return is a future extension, not core v1 scope.
Downloads exports require reviewed promotion into registered references before
they can support a strict visual verdict.

The October 3 accepted design record
`docs/decisions/2026-10-03-one-field-and-one-way-to-send.md` was inspected in
the product-direction lane. It describes a note/question field and Send on
every Thing page; it is absent from this lane's fetched workspace baseline.
EP0 must record its exact revision and applicability to canonical Place detail
versus a kept Thing. Do not finalize a new separate Ask button against a newer
applicable decision, and do not invent a note-writing owner or general answer
service to make the field appear functional. Until that reconciliation,
preserve existing action behavior and continue independent reading work.

Included: existing canonical venue/site/experience routes; rich and sparse
reading; purpose-sensitive facts and body; selected original; existing Keep,
permitted share, question and deliberate source/map handoffs; loading, failure,
stale and unavailable states; exact entry/return and viewer changes.

Excluded: new entity kinds or catalog backfill; new private-note/retention or
sharing policy; Useful/Reply or retained friend copies; loosely dated intentions;
new arrangement commands; per-fact public lookup; background research; provider,
model or paid calls; production deployment or default flag changes. Existing
gated research/people paths receive regression protection, not activation.

## Lane and verified baseline

Created with the coordinated workspace tooling on October 3. All three lane
repositories began clean on `codex/entity-page-v1-20261003`.

| Repository | Fetched main used as the exact base |
| --- | --- |
| Workspace | `98a05b3bcdcc4a53c5bc1e0e3981e6a8a8c7c961` |
| Backend | `815f72e7f5c72c86c792ef68c97d0bc88a3ea593` |
| App | `057f5c95ac7d93d26f134db83f4c77ddd7a32dbf` |

Lane: `/private/tmp/vesper-entity-page-v1-20261003`. Owner: this Entity task.
The local `.workspace-lane.json` records the three bases, Compose project and
ports: Postgres 64032, Qdrant 64033/64034, API 64035 and Expo 64036. No device is
assigned and no runtime was started. Recheck allocation before starting services.
Canonical dirty documentation and every other owner checkout remain untouched.

Remote Git main refs were fetched and verified. GitHub GraphQL was rate-limited
during the fresh PR/check query, so this planning receipt does not assert fresh
hosted-check acceptance. The workspace CI lock still pins app `4bbee04e8`, while
this lane includes the later merged app through #223. Central integration owns
the pending shared pin reconciliation; do not silently call this tuple an
already-pinned release candidate or copy unmerged backend #250 as a dependency.

## What is already present

These are source-inspection findings at the baseline, not new test results.
The earlier 75–85% core estimate is a rough capability judgment, not a measured
completion percentage or remaining-effort estimate. Track the packages below
by evidence and accepted commits instead.

| Capability | Existing implementation | Work remaining in this lane |
| --- | --- | --- |
| Shared page and state shell | `ObjectPageRebuild`, `ObjectPageShell`, `ObjectPageStateShell`; three canonical routes | Compare the actual variants with promoted references; repair only demonstrated gaps |
| Purpose-sensitive reading | `objectPageProjection.ts` ranks facts and composes existing material for discovery, visit and arrangement | Verify useful hierarchy across purposes and sparse data; preserve exact trip/block occurrence and provenance |
| Selected original | Exact selected reading appears first; current place facts remain a separate continuation | Prove revision, unavailable and withdrawal behavior across receiving routes |
| Keep and sharing | Existing relationship mutations/readback and `PlaceShareOwnerSheet` | Check pending/failure/reopen and public/private boundaries without adding new owners |
| Questions | Existing entity Ask handoff; separately merged selected-source Ask | Reconcile the action design, then use only the appropriate supported contract |
| Research and people | Cached briefs, explicit gated request/status and current-owner people actions | Retain existing semantics and regression evidence; richer actions are out of scope |
| Visual and native acceptance | Registered `entity-object` surface, focused tests and dated native receipts | Promote screen references; current-build full native, auth and accessibility evidence remains deferred |

The selected-source Adaptive Context flow currently serves an eligible private
original and optional explicitly selected private Collection. It is not a
general question-answerer or public fact checker. Core Entity v1 does not wait
for a new Adaptive Context milestone and does not route arbitrary place
questions through that API. A future original-to-context adapter needs its own
eligibility, source revision, deletion and result-readback acceptance.

## EP0 receipt: frozen gap list and reference set

The lane inspected the current contract, the three route families, the shared
renderer/projection and their nearest tests. Board 14 is the reading-order
authority: purpose changes emphasis and ordering of existing evidence while the
identity shell remains stable. Board 09's invariant-body rule is not used for
this target. The newer one-field/one-way-to-send decision was absent from the
fetched lane baseline, so the lane preserves the existing Ask handoff and does
not invent a note owner or replacement composer; that action boundary remains a
separate product-direction reconciliation item.

The structural reference set is recorded by source hash because no promoted
phone-screen export was available in this lane:

| Reference | Source hash | Use |
| --- | --- | --- |
| Board 06 — The Page | `9bc587a417e9fc57c35d4b3c2e71f65ce08721adf0b0352149d7b6b998704cd0` | shared anatomy |
| Board 06B — Arrival Large Text | `8b6607af7a6d0aa53b207cd7cd3671a7ec32abd0e56a2ab7a199bf6fb697a05c` | large-text ordering |
| Board 14 — Received from Places | `cff9b12b2bf3b282b8dd21377bb447c63312e7fcb15e15d97f8701555aaec61f` | purpose-sensitive reading |
| Board 09 — One Place Five Doors | `b25f8ad561fa41be70ef81d7fd009d1d0db06d3a44196451a2a1cd77971f344d` | entry/door comparison |

The concrete implementation gap found in EP0/EP1 was that inline page verbs
had a button role but no explicit accessible label. `TextVerb` now forwards its
visible label as `accessibilityLabel`; the focused regression asserts labels for
Ask Vesper, Tonight? and Leave for someone. No new layout system, data cache,
prompt, or owner contract was introduced. Native visual and assistive-technology
acceptance is still a release gate rather than a local claim.

EP2/EP3 evidence then exercised the existing action and receiving boundaries:
the action suite passed 43 tests across Keep/share, public eligibility, gated
research/people and the Entity renderer; the route/return suite passed 95 app
tests covering entity routing, Places map return, root projection navigation
and state shells; and the four focused backend contract files passed 55 tests
with the lane's existing test environment. No new backend or API contract was
needed, and no late response, viewer change or origin token behavior was
altered by this lane.

## Implementation packages

Run EP0 first, then EP1–EP3 as small coherent slices in this lane. EP4 closes
integration. A package with no demonstrated gap closes with its existing-code
evidence; do not manufacture a refactor to fill it. Keep the same lane through
delivery rather than creating a new worktree for every package.

### EP0 Freeze the target and name the actual gaps

- Prepare this lane's dependency environments from its committed locks using
  the existing workspace setup instructions before product tests. A clean
  source checkout is not a runnable test environment; do not mistake missing
  dependencies or sandbox socket restrictions for Entity behavior failures.
- Read the current Entity contract, handoff, three route implementations and
  nearest tests. Resolve board 14 against boards 06/09 and the newer Thing-page
  decision; record the chosen action treatment and owner boundary.
- Select rich venue, sparse/no-photo site, experience, visit, exact arrangement
  and selected-original reference cases, plus large text. Promote only the
  necessary isolated screens into the app surface's `design-refs/`; record
  original file hashes and stable screen IDs. Use the existing design-export
  tooling and register the references, not a full board as a phone screenshot.
- Produce a short gap list in this roadmap with each discrepancy linked to its
  component/route, expected behavior and acceptance case. Update the existing
  surface contract where design authority changes; avoid another competing spec.

**Finish:** reference selection and action ownership are explicit; every
implementation item has a concrete expected result. If the field-versus-Ask
boundary requires a product ruling, isolate that decision to EP2 and continue
the already-supported anatomy, evidence and navigation work. If export tooling
is unavailable, retain source hashes and the structural comparison; pixel
acceptance stays unverified while deterministic behavior work proceeds.

### EP1 Finish the reading surface

- Implement the EP0 gaps in `ObjectPageRebuild.tsx`, `objectPageProjection.ts`,
  the existing shell and necessary route adapters. Keep one renderer for the
  three kinds and existing semantic design tokens.
- Finish photo/no-photo, name/byline, fact pair, authored body, citations, source
  list, closing facts and permitted map/source continuations. Missing content
  collapses honestly; it must not become fabricated filler or fixture truth.
- Preserve selected authored words and their revision. Purpose may arrange
  existing evidence; page reads must not trigger generation or memory writes.
  A reservation requirement or trip membership is never booking confirmation.
- Cover long names, long originals, dynamic type, action labels and hit targets
  without introducing a second data cache or a new layout system.

**Finish:** all selected variants have deterministic component/projection
evidence and a reviewed structural comparison. Native visual verdict remains
separately pending. Backend data gaps become precise owner-contract findings;
render honest absence and continue the other variants while those are resolved.

### EP2 Complete the existing actions

- Carry EP0's resolved action treatment through all three routes. Reuse the
  existing supported question handoff; any approved field treatment must use
  real note/question owners and must not be simulated with an unrelated API.
- Verify canonical Keep pending, duplicate tap, failure, revision conflict and
  authoritative reopen/readback. Distinguish keeping a place from keeping a
  received line while its grant remains active.
- Preserve allowed public sharing and deliberate external source/map actions.
  Private relationship text, provisional shells and original-only material
  must not enter a public payload. Sharing and any memory effect follow the
  existing contribution and owner contracts.
- Protect existing research retry correlation and people lease/revision rules.
  An unknown request status must not silently submit a second paid operation.

**Finish:** action and data-layer tests demonstrate the allowed transitions
and failure behavior; changed owner assumptions have provider-free real-backend
evidence where required. No new prompt, runtime generation, retention or social
scope is required to finish core Keep/share/return. Hold only an unresolved new
composer slice, and report it explicitly if it prevents the intended v1 target.

### EP3 Close receiving and return behavior

- Trace actual Home, Places, Life, Plan and deep-link entry contracts for each
  supported route. Cover actual supported combinations rather than inventing
  every possible door for every entity kind.
- Preserve canonical type/ID, origin, purpose, exact selected source/revision
  and exact trip/block occurrence. Back/close returns to the right owner and
  state; an absent origin uses the existing documented fallback.
- Revalidate on focus, viewer change, entity replacement, source withdrawal,
  expiry and deletion. A late response for an old account or selection cannot
  restore stale private text or actions. Unavailable originals do not silently
  become a different reading.
- Add only the minimal typed handoff fix at an affected caller boundary;
  coordinate shared route registries and caller-owned files with their owner.
  Update existing route/operation ownership inventories if the route changes.

**Finish:** route and lifecycle regressions prove exact entry/return and stale
response suppression. An upstream missing payload is a specific dependency
with the expected fields and test; independent supported doors still finish.

### EP4 Integrate and close the implementation

- Review the combined diff and accepted upstream changes. Reconcile any API
  changes with offline `scripts/sync-types.sh`, both snapshots, generated app
  types and consumers; run `make api-coverage-check` when adoption changes.
  No backend or schema change is planned unless EP0–EP3 demonstrate a need.
- Run one measured `make verify-changed` preflight with explicit bases for all
  three repositories. Preserve focused results and name skipped, quarantined,
  blocked and unrun checks; repeat only after a material change or failure.
- Hand central integration exact commits, dependency order and evidence. Keep
  publication/merge ownership singular; use the actual current merge policy
  and explicitly applicable approvals. Do not infer a standing security or
  hosted-check waiver from earlier conversations or exceptions for other PRs.
- Update this plan and the existing Entity surface contract with accepted
  changes and remaining native evidence. Coordinate shared pins with central.
  Retire only after every lane commit is merged, all repos are clean and the
  workspace safety tool confirms runtime/data preservation.

**Finish:** intended core code is accepted, or a concrete unresolved slice is
reported with its dependency and remaining work. Stop this finite chain here;
do not expand into board 16 or restart the deferred E1 device investigation.

## Acceptance cases

Mock evidence proves composition and state transitions. Real-backend evidence
proves the changed owner/readback contract. Native evidence proves rendered
behavior on the recorded build; none substitutes for the others.

| Case | Required result | Evidence before implementation completion |
| --- | --- | --- |
| Rich venue, sparse site, experience | Same coherent anatomy; no invented photo, address, source or fact | Projection and component cases for all three kinds |
| Discovery versus visit | Existing evidence changes emphasis without generation or hidden writes | Purpose projection and base-read regression |
| Repeated place on a Plan | Exact occurrence and owner confirmation state; correct timezone | Route and owner-read tests |
| Selected original | Exact authored content first, current place continuation separate | Projection plus exact source/revision route case |
| Revoked, expired or deleted original | Unavailable state; no stale source text/action or generic replacement | Owner read plus late-response regression |
| Keep success and failure | One pending action, honest failure, authoritative later state | Data/route tests; real-backend test if owner contract changes |
| Public share and private shell | Only permitted public fields; private state does not escape | Payload and eligibility tests |
| Ask and return | Correct entity/source context under the resolved contract; correct origin restored | Typed handoff and navigation tests |
| Account or entity switch in flight | Old results cannot populate the new viewer/page | Lifecycle regression |
| Loading, offline, retry, stale, not found | Honest state, correct permitted actions and recovery | Existing state-shell tests plus changed-route cases |
| Existing gated research/people | Flag boundaries, request identity, lease and revision preserved | Relevant focused regressions; no live dispatch |
| Long content and large text | Reading and controls remain usable and correctly ordered | Component coverage now; registered device capture and assistive-tech checks before release |

Start with existing suites: app `ObjectPageRebuild.test.tsx`,
`objectPageProjection.test.ts`, `ObjectPageShell.test.tsx`,
`ObjectPageStateShell.test.tsx`, `entityRoute.test.ts`,
`entityResearchRequest.test.tsx` and `entityPeopleLines.test.tsx`.
Select only those affected by a slice. Backend seams include
`tests/places/test_entity_presentation_read.py`,
`tests/places/test_private_entity_contracts.py`,
`tests/api/test_entity_people_lines.py` and
`tests/api/test_entity_research_requests.py`; inspect their prerequisites first.
Any database test uses a lane-isolated disposable database with explicit
`TEST_DATABASE_URL` and `TEST_DATABASE_DISPOSABLE=1`.

The task is **parity-sensitive** overall. Local layout-only changes can use the
app's safe-frontend evidence scope; backend wire changes are contract-sensitive.
No new prompt-sensitive work is admitted. Use the current Task Intake and
surface capture workflow; native and signed-in validation stay deferred until
explicitly reopened, with fresh build, serial device and runtime ownership.

## Coordination and efficient execution

| Owner | Boundary with Entity |
| --- | --- |
| Entity | Shared entity renderer, projection, three routes, receiving regressions, registered Entity references and this roadmap |
| Connectivity | Existing root/capture behavior; request only an exact demonstrated handoff correction |
| Artifact | Private Thing and Collection ownership; Entity does not edit Collection member projection or replace the original reader |
| Adaptive Context | Selected-source and Collection context contracts; optional future consumer work is separate from core Entity completion |
| Eng Efficiency | Verification tools and environment evidence; Entity consumes the supported commands |
| Orchestrator | Cross-lane overlap, final integration, shared snapshots/pins and publication coordination |

Keep a short handoff per completed package: exact revisions, changed behavior,
tests/evidence, remaining gap and the next admitted package. Continue through
unblocked packages without a new status-only turn. Check owners when a shared
file or contract is actually needed; do not wake idle lanes for reassurance.
Do not rerun broad suites or poll unchanged external blockers to simulate work.
Publication delays do not block independent local packages; missing native
proof remains a release condition and is not chased during this code round.

If a design or owner-contract choice changes product meaning, prepare the
concrete alternatives and ask once. Complete disjoint work while it is pending.
No successor feature is automatically admitted when EP4 finishes.

## Progress and next action

| Package | Current state | Completion evidence |
| --- | --- | --- |
| Planning | Lane and mini roadmap prepared | Three exact bases and isolated runtime allocation recorded above |
| EP0 | Complete locally | Contract/route/test inspection, Board 14 promotion, source hashes and action boundary recorded above; visual export unavailable |
| EP1 | Complete locally | Accessibility-label gap fixed in `TextVerb`; focused component regression passes; remaining reading variants rely on existing projection/shell evidence |
| EP2 | Complete locally | 6 focused app suites / 43 tests passed; existing Keep/share/Ask and gated research/people contracts remain unchanged |
| EP3 | Complete locally | 4 focused app suites / 95 tests and 4 focused backend files / 55 tests passed; exact route/return and lifecycle boundaries remain intact |
| EP4 | Complete locally; merge-gated | Two measured explicit-base preflights are recorded below; all Entity/product checks pass, while one pre-existing cross-repo contract finding still blocks the wrapper |
| Native acceptance and activation | Deferred | Current-build full evidence and explicit activation remain outstanding |

Planning checks on October 3 passed documentation metadata, inventory, living
links, generated status, canonical spine and canon budgets; `git diff --check`
also passed. The measured explicit-base `make verify-changed` run took 34.011s
with stable inputs and **failed**: 210 workspace tests passed, one cross-repo
fixture test lacked SQLAlchemy in the fresh lane's Python environment, and four
runtime tests could not bind loopback sockets in the sandbox. The contract
group stopped at the same missing backend dependency; its later checks are
unrun. No Entity product or native test was run in this planning turn.

Retained log:
`/private/tmp/vesper-entity-page-v1-planning-evidence/entity-v1-planning-preflight-20261003T193022Z.log`.
The affected tests are `test_real_cross_repo_inputs_agree`,
`test_create_builds_three_independent_worktrees_with_distinct_runtime`,
`test_second_process_failure_stops_already_ready_sibling`,
`test_status_reports_lanes_without_mutation` and
`test_retire_previews_then_removes_only_merged_clean_lane`. Re-run the preflight
after supported dependency setup in an environment permitting its local
socket fixtures; do not weaken the tests. This is a planning handoff, not merge
readiness or product acceptance.

## EP4 implementation receipt

The coordinated lane now contains two local commits after the planning commit:

- App `1e345ab984918257706801bb915314d640f87b7b` — add explicit accessibility
  labels to the three inline Entity page verbs, with a focused regression.
- Workspace roadmap receipt — record EP0–EP3 references, gap, tests and this
  integration evidence in the final lane commit.

The app dependency install used the committed lockfile and applied the existing
Clerk patch from `travel-app/patches/`; no lockfile or dependency source changed.
App typecheck passed. The full changed-app selection then passed 101 suites and
805 tests. The explicit-base command below was measured twice with stable lane
inputs and exact bases from the lane manifest:

```text
make verify-changed \
  WORKSPACE_BASE_REF=98a05b3bcdcc4a53c5bc1e0e3981e6a8a8c7c961 \
  AGENT_BASE_REF=815f72e7f5c72c86c792ef68c97d0bc88a3ea593 \
  APP_BASE_REF=057f5c95ac7d93d26f134db83f4c77ddd7a32dbf
```

The sandbox run took 91.440s and the elevated supported-local run took
72.066s. The elevated run passed the 805 app tests and 215 workspace tests;
its only remaining failure was the existing contract audit finding
`dark-has-caller` for `POST /api/research/selected-source`, which is already
present at the app base and is outside this Entity slice. The same finding is
unchanged by `1e345ab98` (no selected-source registry or policy file is in its
diff). The non-elevated run additionally reported four lane-runtime socket
tests blocked by sandbox binding; those same tests passed in the elevated run.
This is an integration-owner dependency, not a product failure or a reason to
weaken the contract checker. The measured logs are:

- `/private/tmp/vesper-entity-page-v1-planning-evidence/entity-v1-preflight-20261003.log`
- `/private/tmp/vesper-entity-page-v1-planning-evidence/entity-v1-preflight-20261003-elevated.log`

Docs governance, inventory, links, status, spine, canon budgets and
`git diff --check` passed after the final roadmap edit. No backend/schema or
generated-type change was needed, so `sync-types` and `api-coverage-check` were
not rerun as changed-surface checks. Native, signed-in, accessibility-device,
production and hosted merge evidence remain separate gates.

**Next:** commit this roadmap receipt, then run one measured explicit-base
preflight after the implementation commits. Re-run only the supported checks
affected by material changes. Before November 2, close or archive this plan
and preserve durable rules in the existing Entity contract rather than keeping
two living specifications.
