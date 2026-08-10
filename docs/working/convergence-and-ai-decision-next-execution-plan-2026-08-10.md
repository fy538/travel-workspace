---
doc_type: working
status: active
owner: engineering / AI systems / product / evidence
created: 2026-08-10
last_verified: 2026-08-10
expires: 2026-09-09
why_new: Defines the executable post-merge round that joins intentional convergence, AI decision-learning shadow readiness, and the Lisbon Group Trip proof without overstating device or causal evidence.
source_of_truth_for:
  - convergence-ai-decision-next-execution-round-2026-08
related:
  - intentional-convergence-engineering-plan-2026-08-10.md
  - ai-decision-and-learning-engineering-plan-2026-08-10.md
  - ai-decision-and-learning-research-agenda-2026-08-10.md
  - ai-decision-and-learning-r1-execution-status-2026-08-10.md
  - journey-live-full-cert-04-05-10.md
  - lisbon-group-trip-staging-device-runbook-2026-08-10.md
---

# Convergence and AI decision-learning: next execution round

## 1. Executive decision

The next round will close the largest remaining engineering gap—causal lineage—
while advancing two proof tracks in parallel:

1. **Product proof:** one fixed Lisbon Group Trip disruption moves through a
   governed proposal, coherent shared projections, private per-person outcomes,
   and revision-bound evidence.
2. **Learning proof:** one narrow private decision family runs offline and then
   in shadow, producing no user-visible copy, mutation, notification, or durable
   inferred memory.

This is a proof-and-observation round, not another broad architecture wave. It
will reuse the merged scope, map, proposal, group-composition, outcome, and
evidence authorities. It will not create a second writer, a general group
agent, a universal context object, or a new profile/memory truth store.

Four isolated lanes may work concurrently after their bases and hot-file
ownership are recorded. A single integration owner controls shared contracts,
generated files, merge order, deployment identity, and evidence promotion.

## 2. Recorded starting point

All three canonical checkouts were clean and aligned with `origin/main` when
this plan was written:

| Repository | Starting revision |
| --- | --- |
| workspace | `47d51880f0fd6dfccf63b989242f8b9c2459b9e5` |
| backend | `e42fc3a3d2a1fccc12ae932c9964f0ef69b35599` |
| mobile | `aba00ae32946d279411836a0337f2df0d41c2cde` |

These revisions contain the four merged convergence lanes, post-lane outcome
and receipt hardening, and the merged AI-DL R1 offline/dark substrate. They are
the creation bases for all four lanes unless the integration owner explicitly
records newer reviewed `origin/main` heads before lane creation.

No device-mock, physical-device, live AI evaluation, human-adjudication, or
causal receipt is implied by these source revisions.

## 3. Scope and completion boundary

### 3.1 Work this round should complete in source

- K2 root decision identity and causal propagation through existing receipts;
- scoped Situation dependency identity without a universal mega-object;
- a disabled, allowlisted, fail-open private shadow adapter;
- one materialized private Decision Set family and frozen human-review packet;
- deterministic, unconstrained, and structured-policy comparison tooling;
- a bounded Lisbon micro-journey doorway and fixed disruption scenario;
- canonical proposal, accept/reject/expiry/revert, and projection convergence;
- exact-roster, private per-person outcome closure;
- a pinned integration/deployment manifest and fail-closed device evidence plan;
- truth refreshes for the now-stale post-A–D planning documents.

### 3.2 Claims this round must not make from source or tests alone

- that the Lisbon journey is device-validated or certified;
- that AI-DL shadow quality is backend-real before real observations exist;
- that a model policy outperforms a deterministic policy before adjudicated
  comparison;
- that inferred claims may be written durably;
- that private proactivity has earned delivery;
- that group-visible AI-DL behavior is authorized;
- that deployment, push, Clerk, or physical-device behavior works because an
  offline or simulator test passed.

### 3.3 Default product decisions

Work may proceed using these conservative defaults unless product overrides
them in writing:

| Decision | Default |
| --- | --- |
| First AI decision family | Private trip-concierge response to one grounded disruption alternative |
| Allowed shadow actions | `ask_attribute`, `show_options`, `recommend`, `abstain` |
| Forbidden shadow actions | proposal, execution, group output, notification, memory write |
| User-visible effect | none |
| Mutation authority | existing canonical proposal/operation gateways only |
| Durable inferred learning | off |
| Group-visible AI-DL | off |
| Proactive delivery | off |
| Product milestone order | Group Trip proof before local second occasion |

## 4. Target causal graph

The implementation should make this graph inspectable without copying domain
receipts into a new event system:

```text
serving/root run
  -> admitted scope and dependency revisions
  -> bounded decision or existing serving decision
  -> canonical proposal/command
  -> ledgered mutation and action receipt
  -> Plan/Map/Now/group projection revisions
  -> per-person occurrence/outcome
  -> applicability result and later decision reference
```

The join uses content-free IDs and revisions. Private prose, private preference
values, and private reasoning must not enter shared trace metadata.

## 5. Lane topology

### Lane A — causal spine and private shadow attachment

**Mission:** finish K2 and create one safe, disabled attachment point for
backend-real shadow observation.

**Primary ownership:**

- `travel-agent/backend/core/ai_runs.py`;
- `travel-agent/backend/core/ai_decision_shadow.py`;
- `travel-agent/backend/core/db/action_receipts.py` and its model;
- scoped Situation/entry-context identity;
- one selected private serving adapter;
- focused causal-lineage and non-interference tests.

**Work packages:**

#### A1 — causal contract

- Define the minimum `DecisionCausalRef` or equivalent content-free join:
  root run, optional parent run, workflow/correlation, trip/experience scope
  revisions, policy revision, and dependency revision references.
- Reuse existing `ai_run_id`, `workflow_id`, and `correlation_id` columns where
  sufficient; prefer no migration over redundant storage.
- Specify which identifier is stable across retries and which identifies one
  execution attempt.
- Specify fail-open telemetry behavior separately from required mutation
  receipts.

**Commit boundary:** one additive contract and pure adapters; no production
caller and no behavior change.

#### A2 — root boundaries and receipt propagation

- Establish or verify root runs at the private concierge decision boundary and
  the fixed disruption/proposal boundary.
- Thread the current root run into canonical action receipts and proposal or
  operation receipts without bypassing existing writers.
- Preserve the join through accept, reject, expiry, revert, and outcome capture.
- Add a query/read helper that reconstructs the causal graph for one decision.
- Do not copy private copy or reasoning into receipt metadata.

**Commit boundary:** one end-to-end causal join in backend/static or
backend-real layers; no new product surface.

#### A3 — scoped Situation

- Wrap current Trip/Spatial Situation output in serving identity and dependency
  revisions.
- Keep Context Compiler evidence admission distinct from Situation relevance.
- Record source authority, freshness class, and revision identity, not content.
- Fail honestly when a required dependency is stale or unavailable.

#### A4 — shadow-only consumer

- Register a global and per-policy shadow flag in the canonical flag registry.
- Allow only the declared private surface and action set.
- Invoke structured policy after authorized `DecisionState` construction.
- Record only content-free decisions; never replace visible output or execute a
  tool/mutation.
- Make provider failure, ledger failure, timeout, or validation failure
  non-blocking to the existing serving path and observable by reason code.
- Enforce independent kill switch, latency/cost ceiling, and allowlist.

**Lane exit:** one real private boundary can run shadow when explicitly enabled;
it is disabled by default and cannot affect visible or durable product state.

### Lane B — AI evidence completion and shadow-readiness decision

**Mission:** turn the AI-R1 schemas and seed manifests into an adjudicable
candidate for one narrow family.

**Primary ownership:**

- `travel-agent/eval/ai_decision_learning/`;
- `travel-agent/tests/eval/test_ai_decision_learning_*`;
- new versioned, non-sensitive corpus artifacts;
- annotation guide, anchor packet, reports, and promotion decision record;
- no production backend imports or mobile files.

**Work packages:**

#### B1 — materialize the first Decision Set slice

- Build a balanced first slice for private grounded disruption decisions.
- Cover fresh, stale, missing, conflicting, wrong-trip, wrong-roster,
  unauthorized, high-reversibility, and material-unknown cases.
- Include `ask`, `show`, `recommend`, and `abstain` positives plus forbidden
  proposal, execution, notification, memory, and group-output negatives.
- Bind every case to stable IDs, exact allowed action sets, forbidden evidence,
  expected state, and evidence layer.
- Use anonymized/synthetic bounded fixtures; do not place private production
  content in the corpus.

#### B2 — human anchor packet

- Freeze annotation instructions before comparing policies.
- Record acceptable action sets rather than one preferred sentence.
- Separate correctness, privacy, usefulness, friction, and trust labels.
- Require adjudication for disagreements and preserve reviewer/protocol version.
- Do not serialize a schema instance as human evidence until a human actually
  reviewed it.

#### B3 — baseline and structured comparisons

- Run deterministic baseline first.
- Add unconstrained-model output only as a negative/comparison baseline.
- Run the typed structured policy against the same frozen cases.
- Apply deterministic authorization, privacy, freshness, mutation, and receipt
  gates before graded judges.
- Report category errors, abstention behavior, latency, cost, and disagreements;
  do not collapse them into one score.

#### B4 — shadow promotion decision

- Produce a `promote | iterate | stop` recommendation for shadow only.
- Require human-anchor calibration and explicit limitations.
- Pin corpus, policy, prompt, model, evaluator, backend, and workspace revisions.
- A promotion result authorizes only content-free shadow observation, never a
  canary or user-visible change.

**Lane exit:** reproducible M/A/H evidence for the declared slice, or an honest
stop/iterate record explaining why shadow should remain disabled.

### Lane C — Lisbon Group Trip proof implementation

**Mission:** make the fixed Group Trip scenario coherent in product code without
depending on AI-DL promotion.

**Primary ownership:**

- bounded mobile doorway and fixed scenario UX;
- thin participant/invitation/response presentation;
- disruption-to-proposal adapters;
- Plan/Map/Now/group projection convergence;
- private outcome confirmation/correction;
- existing group composer and canonical proposal gateway only through reviewed
  adapters;
- no changes to Lane A hot files until A hands off its contract.

**Work packages:**

#### C1 — executable scenario contract

- Freeze trip, actors, roster, place, route, time, weather/venue disruption,
  initial plan revision, expected proposal, and negative privacy oracles.
- Reuse the canonical Lisbon dogfood world where it matches; add only the
  minimum missing fixture.
- Define both observers' expected Plan, Map, Now, proposal, and group-room
  revisions before implementation.

#### C2 — bounded doorway

- Add one internal, kill-switchable **Take me/us somewhere** entry.
- Produce a short route/plan rather than a recommendation list.
- Preserve time budget, next commitment, route facts, weather, evidence,
  roster, audience, and causal identity.
- Show unavailable/degraded truth honestly; do not fabricate a local plan.

#### C3 — second participant and group safety

- Use existing invitation, consent, membership, visibility, and response paths.
- Preserve rich-owner/thin-participant topology.
- Require no public profile and infer no circle from Trip membership.
- Route every group-bound string through `group_compose.py` or its sanctioned
  equivalent.
- Add direct and counterfactual private-string negative oracles.

#### C4 — governed disruption and repair

- Trigger one deterministic weather or venue-state disruption.
- Ground one alternative with provenance, freshness, and limitations.
- Build the change through the canonical proposal builder.
- Demonstrate accept, reject, expiry, and diff-safe revert.
- Ensure Plan and Map share the accepted revision and all warm projections
  converge without waiting for incidental refetch.

#### C5 — per-person outcome closure

- Let each participant privately confirm or correct occurrence/outcome.
- Preserve exact roster, subject, experience scope, time, and evidence refs.
- Use the shared applicability resolver for any later read.
- Join decision, proposal, mutation, projection, occurrence, and outcome through
  Lane A's content-free causal identity.

**Lane exit:** the fixed journey has source/static, deterministic, and relevant
backend-real support on a pinned candidate. It is not called device-complete.

### Lane D — integration, staging, and evidence integrity

**Mission:** produce a clean candidate and make every higher evidence layer
fail closed.

**Primary ownership:**

- workspace evidence scripts and registries;
- planning/status truth refreshes;
- OpenAPI/type generation after backend merge;
- staging/deployment manifest;
- Maestro/device runbooks and receipt integrity;
- no backend/mobile product behavior.

**Work packages:**

#### D1 — documentation truth reset

- Mark A–D and AI-R1 branches as merged and record current heads.
- Retire obsolete “dispatch the original four lanes” instructions.
- Update the AI-DL README from its pre-integration R0 boundary.
- Keep implementation, shadow, device, human, and causal evidence distinct.
- Link this plan from the three parent plans and their status records.

#### D2 — clean integration candidate

- Record base/final SHAs and exact commits for all lanes.
- Confirm dirty worktrees and unrelated branches are excluded.
- Regenerate OpenAPI and mobile types once, after backend behavior is fixed.
- Record schema/migration head, flag defaults, rollback controls, and seed hash.
- Produce a machine-readable triple-SHA candidate manifest.
- Treat the workspace SHA as the integration subject revision; one subsequent
  single-parent, manifest-only projection commit may record that SHA without
  changing the candidate's product/tooling identity.

#### D3 — staging package

- Bind backend image/deploy digest, app build ID, migration revision, policy and
  fixture versions, environment, and seed corpus hash.
- Prepare the Lisbon scenario without promoting or mutating production data
  unless an authorized operator explicitly applies it.
- Keep staging and local receipts separate.

#### D4 — controlled and physical evidence

- Extend/reuse the existing J04/J05/J10 runbook for the fixed Group Trip proof.
- Keep controlled device-mock evidence separate from physical evidence.
- Require two resolved physical UDIDs, two identities, fresh artifacts, build
  and deploy IDs, oracle and flow hashes, reviewer, and all required assertions.
- A skipped assertion blocks only the affected branch; it never becomes pass.
- Generate status from receipts; never hand-edit readiness to green.

**Lane exit:** a clean candidate can be deployed and walked, with no mechanism
for a dry run, simulator, skipped assertion, or manually authored receipt to be
mistaken for physical proof.

## 6. Hot-file and ownership rules

| File family | Exclusive owner until handoff |
| --- | --- |
| `_message_flow.py`, AI run identity, shadow runtime adapter | Lane A |
| `ai_decision_learning` schemas, corpora, evaluators | Lane B |
| Group Trip UI, scenario presentation, participant journey | Lane C |
| Workspace evidence scripts, generated status, OpenAPI/type sync | Lane D |
| Group composer and canonical proposal builder | Read-only by default; changes require integration-owner review |
| Database migrations | Lane A if required; one migration owner only |

Lane C rebases onto A's landed causal contract before adding the final join. Lane
D regenerates contracts only after A and C backend changes are stable. No lane
stages generated or unrelated files owned by another lane.

## 7. Commit plan

Prefer small commits with one contract or behavior boundary:

| Order | Suggested commit |
| ---: | --- |
| A1 | `refactor(ai): define content-free decision causal reference` |
| A2 | `feat(ai): propagate root decision identity into canonical receipts` |
| A3 | `refactor(concierge): bind Situation to scoped dependency revisions` |
| A4 | `feat(ai): add disabled private shadow decision adapter` |
| B1 | `eval: materialize private disruption decision set` |
| B2 | `eval: freeze disruption human-anchor protocol` |
| B3 | `eval: compare bounded decision policies by category` |
| B4 | `docs: record AI shadow promote iterate or stop decision` |
| C1 | `test(dogfood): freeze Lisbon group disruption contract` |
| C2 | `feat(trips): add bounded local micro-journey doorway` |
| C3 | `feat(trips): close thin participant disruption loop` |
| C4 | `fix(trips): converge proposal repair and private outcomes` |
| D1 | `docs: rebaseline post-merge convergence program` |
| D2 | `chore(contract): pin next-round integration candidate` |
| D3 | `chore(evidence): bind Lisbon staging and device proof inputs` |

Every commit stages explicit filenames. A worker must check its branch before
committing and report if the intended commit is not landing on its lane branch.

## 8. Merge train

1. Create all lanes from the recorded triple heads.
2. Lane B may work independently throughout.
3. Merge Lane A contract and root propagation first.
4. Rebase Lane C on A and complete causal closure.
5. Merge Lane B only if it remains isolated from production behavior; shadow
   enablement still requires the B4 decision.
6. Lane D rebases after A–C, regenerates contracts once, and records the clean
   triple-SHA candidate.
7. Run deterministic and backend-real gates on that exact candidate.
8. Deploy/build the same candidate; do not certify a rebuilt or drifting head.
9. Gather controlled-device evidence separately.
10. Gather physical two-device evidence with an operator.
11. Run private shadow observation only after its five runtime gates are met.
12. Generate status and make explicit promote/iterate/stop decisions.

## 9. Validation and evidence ladder

### G1 — source and deterministic

- types, schemas, flags, imports, and generated contracts agree;
- wrong audience, roster, trip, freshness, and authority fail closed;
- shadow execution cannot alter visible copy, tools, state, or delivery;
- proposal paths use the canonical writer and produce receipts;
- accept/reject/expiry/revert and projection invalidation are deterministic;
- deliberate false-green evidence fixtures fail.

### G2 — backend-real

- causal IDs survive persisted proposal, mutation, receipt, and outcome rows;
- replay and concurrency do not duplicate mutations or receipts;
- both viewers receive authorized projections of the same accepted revision;
- wrong-roster/private evidence remains excluded from later decisions;
- shadow records are content-free and cannot block the serving path.

### G3 — deployed staging

- exact backend deploy/image, migrations, seed, flags, policy, and app build are
  recorded;
- the deployed environment is the one the device build actually targets;
- degraded providers remain visibly degraded rather than silently empty/current.

### G4 — controlled device

- exact doorway, proposal, response, projection, correction, and revert affordance
  renders are observed;
- evidence is labeled device-mock/controlled, never physical.

### G5 — physical multi-device

- two real devices and identities execute the fixed scenario;
- private phrase and rationale never reach group-visible surfaces;
- both observers converge on Plan/Map/Now/proposal state;
- reject and revert visibly preserve/restore truthful state;
- each participant privately confirms or corrects outcome;
- artifacts and receipts bind the exact build and deployment.

### G6 — AI/human and shadow

- human anchors are genuinely adjudicated;
- policy comparisons publish category errors and hard-gate failures;
- backend-real shadow reports coverage, latency, cost, disagreement, missing
  context, abstention, and failure reasons;
- zero user-visible behavior or mutation is attributed to shadow.

### G7 — decision

Product and engineering record separate decisions for:

- Group Trip proof promotion;
- continued/expanded private shadow observation;
- proceeding to the passive local second-occasion loop;
- whether any future private proactive canary is justified.

No single aggregate score promotes all four.

## 10. What can proceed without the owner

Engineering can complete, without external credentials or physical access:

- all four lane branches/worktrees;
- K2 causal contract and propagation;
- disabled private shadow integration;
- corpus materialization and annotation tooling;
- bounded doorway and Group Trip source implementation;
- fixture, privacy, mutation, projection, and evidence checks;
- contract/type regeneration;
- staging/device manifests and fail-closed runbook improvements;
- documentation truth refresh and integration candidate creation.

Engineering must stop at the relevant boundary if the following are absent:

| Need | Blocks |
| --- | --- |
| Human anchor reviewers/adjudicator | M/A/H shadow promotion decision |
| Approved telemetry retention/review scope | runtime shadow logging |
| Model/provider credential and spend policy | real model comparison or shadow provider call |
| Backend deployment authority | G3 |
| EAS/Apple/Clerk operator access | exact device build and real sign-in |
| Two physical devices and two real identities | G5 |
| Human OTP/device interactions | physical two-account walk |
| Product/privacy approval and consent protocol | any private canary |

Missing external inputs do not block source implementation. They remain
`not_run` or `blocked`; they are never approximated by fabricated receipts.

## 11. Stop conditions

Stop and split or redesign if:

- causal metadata begins carrying private prose or preference values;
- shadow logic affects response copy, tool selection, latency SLOs, or mutation;
- a new proposal/itinerary/outcome writer appears;
- group text can bypass `group_compose.py`;
- Situation and Context Compiler collapse into one unowned policy object;
- one lane edits another lane's hot file without handoff;
- a model judge can override privacy, authorization, state, or receipt failure;
- corpus cases are optimized after seeing candidate outputs without a new
  version;
- a device command can exit successfully after skipping its oracle;
- branch drift means the deployed build no longer matches the candidate manifest.

## 12. Definition of round outcomes

| Outcome | Required claim |
| --- | --- |
| Source round implemented | A–D merged on named revisions; exact G1 result stated |
| Causal spine backend-real | persisted graph reconstructed on named backend revision; G2 |
| AI shadow-ready | M/A/H gate and approvals recorded; runtime flag remains controlled |
| AI shadow-observed | B evidence on a pinned deployment; zero visible effect |
| Group Trip controlled-device | D receipt for exact build/deploy |
| Group Trip physical proof | V receipt from two real devices/identities |
| Ready for local second occasion | Group Trip proof decision plus scoped kernel stability |
| Ready to consider private canary | passive value, shadow result, physical controls, protocol, and explicit approval |

## 13. Follow-on round after successful proof

Only after the Group Trip decision should the team start the local
second-occasion program:

1. expose one saved-place opportunity passively in an existing private surface;
2. activate one origin-aware local Plan without push;
3. capture a correctable outcome;
4. apply only exact-scope evidence to a later occasion;
5. compare against a non-personalized/prior-policy baseline;
6. measure fit, coordination effort, inappropriate repeat, wrong-companion use,
   and correction burden;
7. consider a tiny private no-send-controlled canary only if passive value and
   shadow evidence justify interruption.

Group-visible AI-DL remains optional and later. It requires its own product,
privacy, consent, inferential-leakage, canonical-proposal, and physical
multi-member gates even if the private shadow and Group Trip product proof both
succeed.

## 14. Initial dispatch briefs

Each lane receives:

1. this document and the three parent plans;
2. its exact workspace/backend/mobile base SHAs;
3. owned and prohibited file families;
4. the default private decision family and forbidden actions;
5. canonical writer, group composition, privacy, and evidence invariants;
6. required commit-sized handoffs;
7. exact checks and achieved evidence layer;
8. known deferred branches and external blockers.

The integration owner maintains the dependency board and does not implement a
second copy of lane work. Its job is to keep contracts singular, revisions
known, evidence honest, and the two proof tracks converging on the same product
event.

## 15. Execution outcome — 2026-08-10

The four lanes have been integrated on the named candidate branches. The
machine-readable candidate manifest owns the final triple-SHA after its final
projection commit; this section records the lane outcomes and evidence boundary.

| Lane | Final source revision | Outcome |
| --- | --- | --- |
| A — causal spine | backend `3cb2c66d440dce0b4e70f9d37fa3d793ae6f1fd3` | Content-free causal reference, receipt reconstruction, scoped Situation dependencies, and a disabled private shadow adapter. |
| B — AI evidence | backend `cf0a5c712416a883ffe9950baeb4658c11f436ae` | Sixteen synthetic disruption cases, frozen annotation protocol, deterministic/structured comparisons, and an immutable `iterate` decision. No A/H evidence. |
| C — Group Trip | backend `827937b82`; app `7e063ecd` | Fixed Lisbon contract/replay, real invite redemption, canonical weather proposal lifecycle, two-observer projection convergence, exact-roster private outcomes, and a dark internal doorway. |
| D — integration | candidate manifest | One regenerated OpenAPI/type contract, registered dark flags/proof anchors, deployment-status guards, and a fail-closed staging/two-device runbook. |

Integration closed the cross-lane seam that the parallel branches could not
own independently: the weather decision root now propagates one stable
correlation through proposal creation, human acceptance, the applied itinerary
operation, and each private outcome receipt. The Postgres Lisbon replay
reconstructs that chain without copying private verdicts or rationale into
group-visible evidence.

The checked-in AI readiness decision remains `iterate`. The structured reference
policy produced M-layer evidence; no unconstrained provider observations or
human anchors exist. Shadow attachment is source-complete and remains disabled
by its global flag, policy flag, empty trip allowlist, timeout, and zero-default
cost ceiling.

The remaining work is deliberately outside source implementation:

- adjudicate human anchors and approve telemetry retention/review scope;
- authorize provider/model spend and collect real A-layer comparisons;
- deploy the exact candidate and record backend/build/migration/seed identity;
- run controlled P05/P07 device evidence;
- run the two-identity physical walk with real hardware and fresh artifacts;
- make separate promotion decisions for Group Trip, shadow observation, the
  local second occasion, and any future private canary.

Until those receipts exist, P05/P07 remain dark, AI shadow remains off, and no
device, staging, human, model-quality, causal-impact, or release certification
is claimed from the source and backend-real results above.
