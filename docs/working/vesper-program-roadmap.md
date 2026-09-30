---
doc_type: current_status
status: active
owner: founder / Orchestration lane
created: 2026-09-07
last_verified: 2026-09-30
why_new: Owns the existing program's lane boundaries and the Orchestration execution plan; specialist roadmaps own their own packages and receipts.
supersedes:
  - single-lane dispatch and current assignments in earlier versions of this roadmap
source_of_truth_for:
  - cross-lane implementation ownership and dependency boundaries
  - Orchestration lane execution order and system reassessment
depends_on:
  - ../decisions/2026-09-27-documenting-core-loop-and-one-composer.md
  - ../decisions/2026-09-28-collections-are-the-spine.md
  - ../decisions/2026-09-29-record-as-first-class-value.md
  - ../decisions/2026-09-29-life-model-occasions-collections-and-sharing.md
  - ../systems/contribution-and-consequence.md
---

# Vesper program roadmap

## Direction and current assignment

Build the complete product on the connected system already implemented.
The next execution model is **three autonomous implementation lanes in three
coordinated worktrees**, each containing the workspace and both independent
children. This file owns the boundaries between them and the work of
**Orchestration**, not a queue through which every other lane must ask permission.

The four moves remain **Make sense. Open possibility. Help it work. Carry
forward.** Keeping, enjoying and refinding a recognizable original are complete
value in their own right. Optional intelligence must add substance. Home returns
value for now and the anticipated future; Places opens the situated world;
Chat supports conversation and contribution; Life organizes the record through
Collections, Time, Places and People. Social participation and practical help
run through those experiences.

The accepted September 27–29 decisions amend older contracts where explicit;
they do not declare their runtime migration complete. No new booking execution,
automatic sharing, connected-inbox sharing, background-generation posture,
notification policy or deployment is authorized by this roadmap.

**Planning status:** the three lanes are scoped below, not started by this edit.
First establish the common committed baseline in section 3. Then each lane can
execute its own first assignment without waiting for the other two to finish.
No new coordination service, fourth integration lane or routine inter-chat
messaging is required.

## 1 Inspected baseline and unfinished product work

<a id="inspected-baseline-and-publication-state"></a>

September 30 inspection distinguishes implementation from publication and
acceptance:

| Repository | Observed revision | Meaning |
| --- | --- | --- |
| Canonical workspace | `7a5d434eb6025e792c0e1dd930d7d295a46f5304` | Includes prior consolidated decisions and roadmaps; current roadmap drafts are additional working changes |
| Existing delivery workspace | `73d9679409793f337be120bf9d6e39e27c966677` | Includes the subsequent integrated documentation-link repair |
| Backend main | `3c170d21fc0ca9231b956f2b9de7f9f195231768` | Home/capture follow-up and CI changes merged through PR #237 |
| App main | `87eceee24512d9086962eea5b844cef9d7bffbeb` | Home/capture follow-up and CI changes merged through PR #202 |

Workspace [PR #37](https://github.com/fy538/travel-workspace/pull/37) was still
open at the preceding publication check. The fresh GitHub request during this
rebaseline could not connect; its current status is **unverified**, not assumed
merged. Recheck it before choosing the launch baseline. Do not rerun old
credential repairs or reopen already merged child packages merely because
historical receipts describe those blockers.

The latest completed Strategy roadmap draft was inspected in its existing
product-direction checkout; the latest Technical draft was in the canonical
workspace. This rebaseline consolidates those roadmap contents here without
changing the source Strategy checkout. Reconcile their pending documentation
changes once before branching, rather than launching lanes from different
draft generations. Strategy-child Thesis/Model edits remain separate owned work.

| Area | Implemented foundation | Remaining work and owner |
| --- | --- | --- |
| Capture | Shared private composer, native extension host, retry/session custody, supported email attachment intake, original access | Supported-door delivery, failure/retry clarity and authenticated handoff: Orchestration D1 |
| Home | Source discovery/request/worker/readback connections, contextual continuation, current commitment facts, native hierarchy improvements | Useful recurring supply, complete receiving, full-scroll quality and recovery options: D2/D3 |
| Artifacts and Life | Source custody, original readers, owner references, Life projections and original receiving | Stable thing/component identity, typed family readers, catalog anchors, consumer collections and accepted Life model: Strategy |
| Context and research | Existing retrieval, bounded research pieces, jobs, generation infrastructure and publication fences | General selected-object capability, evidence fidelity, correct reuse and bounded maintenance: Strategy Technical |
| Places and practical help | Situated projections, entity pages, current place facts and owner-backed actions | Consume richer results coherently; useful current options and exact return: D2/D3 |

These are code/evidence boundaries, not design-completion percentages.
[H1](home-value-composition-execution-plan-2026-09-25.md) preserves the detailed
implementation receipts. Its complete native matrix remains MIXED; targeted
passes are not full acceptance. Real recurring supply, all-door authenticated
readback, signed extension behavior and some provider paths remain unverified.
Do not reconstruct completed Source/Home connections or build another generator.

## 2 Three lane ownership

| Lane and its execution roadmap | Owns | Does not own |
| --- | --- | --- |
| **Orchestration — this file** | Entry transport/custody integration; Home/Places composition and native presentation; practical live-engine adapters; caller-side navigation/return | Artifact identity, focused reader internals, Life/collection schema, public research or shared generation engine |
| **Strategy — [Artifact roadmap](artifact-experience-engineering-roadmap-2026-09-29.md)** | P0/P1 identity, components, typed readings, consumer collections; PC subject/catalog anchoring; P2 focused readers; P4 exact kept editions; Life and original-sharing/collection semantics in P6 | A second P3/P5 research/runtime implementation; root-feed composition; native capture transport |
| **Strategy Technical — [Adaptive context roadmap](product-map/adaptive-context-and-research-roadmap-2026-09-29.md)** | R0–R7 context/retrieval, bounded acquisition, evidence fidelity, prepared-result execution/reuse, budget/publication safeguards, relevance maintenance and evaluations | A second artifact store, collection owner, focused reader, Home/Places screen or notification policy |

**One implementation, several experience requirements.** Artifact P3 and the
shared research/runtime portion of P5 are fulfilled by Technical R1–R5; they
remain useful requirements in the Artifact plan, not competing work orders.
Artifact P4 owns durable kept editions; Technical R4 owns changing candidate
selection and prepared-result validity, consuming P4 when retention is required.
P6 is split: Strategy owns collections, original sharing/receiving and Life;
Orchestration owns their Home/Places placements. Technical R6 provides result
readback and consumer-conformance evidence, not its own mobile redesign.

### Code boundaries and shared files

Choose exact files at each lane's intake from these existing owner areas.
A directory is a starting point, not permission to rewrite every file in it.

| Boundary | Initial writer |
| --- | --- |
| App `native-capture/`, capture plugin/session modules, `components/inbound/`; backend inbound transport/security/email handling | Orchestration; artifact reconciliation and durable collection membership stay with Strategy |
| App `components/home-root/`, Places feed/map/root composition, `data/home.ts`, `data/placesProjection.ts`; backend Home/root/Places projections | Orchestration |
| Artifact/source open-target resolution, family renderer/reader, consumer collection and Life organization, subject/catalog identity | Strategy; place pages/facts remain existing domain owners, not automatically cultural-object capabilities |
| Backend `research_agent/`, selected-evidence adapters, shared preparation/job execution and reuse | Strategy Technical; a root composer consumes their output rather than implementing research |
| Lived-experience admission, surface treatment and practical owner adapters | Orchestration; shared research execution, retry/budget and result-publication changes stay Technical |
| App navigation infrastructure, shared design tokens, dependency manifests, global CI/governance tooling | Preserve by default; assign a bounded owner before a change spanning lanes |

Transport idempotency is not thing reconciliation. Catalog lookup is not general
research. Research recommendations are not current operational facts or
authorized commands. A shared UI component is not a new domain owner.

**Shared-file rule:** only the owning lane changes a semantic contract or its
implementation. Other lanes consume the landed version or keep an explicit
unsupported state. Avoid opportunistic moves/renames and cross-cutting cleanup.
If a task reveals a necessary change outside its owner, record the exact missing
interface in that lane's roadmap and continue its independent fallback work;
resolve a consequential boundary change at the next program checkpoint.
Do not edit the other lane's checkout or send it routine instructions.

Generated OpenAPI/type files are an exception to exclusive physical-file
ownership: every lane changing an owned API regenerates and reviews the complete
snapshot/projection/types in its own coordinated checkout. At landing, regenerate
against the combined backend and resolve consumers; never hand-merge generated
models. Separate domain migrations may proceed independently. The later landing
owner reconciles migration heads/order and validates the combined migration;
do not rename or rewrite another lane's already landed migration.

## 3 Prepare the common baseline once

Before implementation starts:

1. Preserve and reconcile the three latest roadmap drafts, accepted decisions
   and relevant pending owner-contract edits. Resolve workspace PR #37's actual
   state and the delivery-only link repair; do not assume local main equals
   remote main. Commit/land the intended shared starting tuple under the current
   publication authority.
2. Inspect `make worktrees`, branches, HEADs and dirty files in all three repos.
   Reuse suitable free coordinated lanes. Do not repurpose a read-only inventory
   checkout or another session's unfinished checkout by assumption.
3. Provision each execution checkout under the existing
   [workspace setup](../Workspace%20Repo%20Setup.md) and root AGENTS. A root-only
   app worktree is not sufficient: verify its own `travel-agent/` and
   `travel-app/` checkouts, matching intended bases, before any cross-repo command.
   Keep three independent Git histories; no submodules or canonical-child fallback.
4. Record the same starting workspace/backend/app SHA tuple in each lane's
   existing assignment. Select a descriptive `codex/` branch per lane. Reuse the
   worktree for follow-on packages rather than retaining a new branch per helper.
5. Check each lane's runtime manifest and `scripts/dev.sh --print-runtime`.
   Use isolated API/Expo ports, Compose projects, disposable test databases and
   caches. Reserve distinct simulator/device instances where capacity permits;
   otherwise only the device-dependent check waits. Do not restart another lane's
   services or repoint its app to a different backend.

After this one-time setup, lanes are autonomous. Each keeps current progress
in its own roadmap, not in all three. This file changes when priority or ownership
changes, not whenever another lane passes a test.

## 4 Interfaces and dependency order

The following are semantic seams to map onto existing contracts, not four new
services or an instruction to invent new wire schemas before inspecting owners.

| Producer | Minimum shared seam | Consumer behavior while unavailable |
| --- | --- | --- |
| Strategy P0/P1 | Stable source/thing/subject reference; selected component plus representation revision; typed reading and correction/withdrawal semantics | D1 uses existing supported custody/source references; Technical uses an existing-original adapter, with new identity modes disabled |
| Technical R1/R2 plus required safeguards | Prepared result and state; selected target; eligible input/dependency revisions; evidence fidelity; error/empty/stale treatment; supported action references | Strategy shows a useful original; D2 uses existing authorized supply. No generated placeholders presented as product value |
| Strategy P4/P6 | Exact retained-edition behavior and collection/audience operations, when adopted and implemented | Keep original-only and existing eligible receiving; disable unsupported retention/shared derivatives |
| Orchestration D2/D3 | Root caller context and return behavior; invocation of existing practical owner commands and current facts | Other lanes preserve existing navigation/actions; do not emulate a provider result or successful mutation |

**First parallel wave:**

- Strategy maps P0 early, then delivers the P1/PC/P2 foundation with original-first
  value and honest catalog fallbacks.
- Technical starts R0/R1 and an existing-original R2 path with first-producer
  safeguards. It can improve evidence fidelity and public-acquisition boundaries
  before new artifact identities land.
- Orchestration starts D1 against existing custody and proceeds with independent
  Home/Places improvements. It does not wait for catalog licensing, a new reader
  or broad research infrastructure.

Land the small additive P0/interface portion once ready; do not hold shared
interfaces until every family renderer is complete. Consumers adopt **landed
revisions**, not copied uncommitted code or a sibling branch that may change
under them. Typed fixtures can unblock presentation and adapter work but do not
prove the producer connection. Recheck owner state at receipt, publication and
readback where the existing contract requires it.

The next connected checkpoint combines a real supported input, Strategy's
reader and Technical's useful addition, with Orchestration's appropriate root
preview and exact return. This is a system connection checkpoint across several
representative families, not a decision to narrow Vesper to one behavior loop.

## 5 Orchestration execution plan

### D0 Rebaseline and prepare execution

**Current task:** reconcile these roadmaps, ownership, evidence and start order.
**Finish:** the three documents agree; each lane has a first assignment,
exclusions, dependency fallback and acceptance boundary. Execution preparation
in section 3 remains a separate step until actually performed.

Do not turn D0 into another architecture inventory or recurring acceptance-only
lane. The existing system and unfinished product work are sufficiently concrete
to begin bounded implementation after baseline preparation.

### D1 Finish supported capture delivery

**Outcome:** a supported contribution reaches durable custody with a clear
receipt and opens the same eligible original. Failure and retry do not require
the person to reconstruct their effort.

Work from H1's remaining capture evidence and current inbound/native code:

- Inventory actual door × file-format support, using existing contracts:
  in-app text/link/photo, external share, forwarded email and already supported
  structured attachments. Do not infer PDF/Wallet/HEIC support from “ticket.”
- Finish transport failure, account/session changes, duplicate attempts,
  cancellation and retry behavior. Preserve input and idempotency through the
  established custody path; do not introduce new cross-door thing identity here.
- Make rejected email bundles and unsupported files explicit. The inspected
  email path rejects the bundle on an unsupported attachment; partial admission
  is a separate reviewed behavior change, not a silent fix. Preserve scanner/
  security requirements and clearly bound any unsupported format.
- Connect receipts and open actions through the current source resolver,
  adopting Strategy's stable target when landed. Ordinary capture must work
  before model recognition or catalog lookup finishes.
- Resolve native extension signing/entitlements when the required access is
  available. The last device blocker was a team/provisioning mismatch; verify
  credentials before another expensive build. Real email-provider configuration
  and authenticated mobile readback need their own evidence.

**Acceptance:** current supported paths survive retry and account changes; a
real authorized backend read returns the retained original; unsupported paths
show honest failure and recovery. Separate in-app, extension, email-provider
and signed-device results. Mock/DB-only checks do not establish all-door delivery.

**Independent work when blocked:** supported in-app delivery, email transport
failure semantics, original-open integration and D2's existing-supply composition.
Do not block the whole lane on signing, an unavailable provider or an unapproved
sharing policy. No Chat redesign or Life implementation belongs to D1.

### D2 Make Home and Places complete receiving surfaces

**Outcome:** both roots deliver substantial, navigable value from current
authorized supply, with the polish of the adopted design references.

- Compare the current registered Home/Places designs and latest adopted handoffs
  with actual section/row coverage. Implement missing supported sections and
  interactions, not just another screenshot or first-viewport crown.
- Home balances what matters now with immediately engageable possibilities,
  useful records and eligible human contributions. A return from a trip does
  not make the feed exclusively retrospective. No generated-card quota, routine
  input prompt or speculative personality interpretation.
- Places prioritizes situated discovery, spatial context and practical relevance.
  Consume the same underlying objects/results through a place-appropriate view;
  do not copy Home or create a second research pipeline.
- Consume Technical's prepared results and Strategy's reader/collection seams as
  they land. Keep originals recognizable; navigate to the exact object/component
  and restore root position on return. Show useful original/current-owner
  fallbacks for no result, failure, staleness or changed access.
- Add social placements from existing permitted originals and later P6 contracts.
  Preserve authorship, intended audience and distinct perspectives. No automatic
  shared filing, equal-effort requirement or unsupported shared synthesis.
- Complete hierarchy, density, image treatment, component spacing, large type,
  touch behavior, loading/empty/error states and full-scroll continuity. Frontend
  polish is part of completion, not a later optional pass.

**Acceptance:** representative sparse, ordinary, social, returned and live states
have useful real-owner content and working actions. Review full-scroll native
output against the correct adopted reference/build/data source. Name unavailable
supply and unsupported components; fixture parity alone does not establish
backend delivery or recurring value.

**Independent work when blocked:** use existing Source/Place/commitment/authorized
social supply; finish root layout, navigation and failure treatment. Do not
rewrite P2's reader or generate pretend enrichment to fill a design.

### D3 Make practical help part of the same system

**Outcome:** what is happening now changes the useful options and actions across
the same Home/Places experience, without reviving the legacy booking product.

- Trace current plans/commitments, place constraints and situational changes
  through existing domain producers, lived-experience admission, projection,
  native action and owner readback.
- Fill missing useful option evidence where a current authorized provider/domain
  path exists. A renamed CTA or an alternative's name does not resolve H1's
  recovery-quality gap. The inspected venue-alternative tool is not a transport
  rerouting capability; scope such gaps honestly.
- Keep public researched possibilities distinct from current availability, cost,
  hours, commitment state and executable changes. Technical supplies bounded
  research; the operational owner remains responsible for practical truth.
- Connect permitted review/confirm/act/return behavior through existing commands.
  An outbound booking link is allowed only as a link, not an executed booking.
  Preserve the person's choice and do not infer obligations or attendance.
- Reassess generation supply and surface behavior together: appropriate later
  evidence may improve an option, but should not rewrite the original or silently
  create monitoring. Existing initiative/notification authority still applies.

**Acceptance:** a useful ordinary near-term situation and a material change
reach current owner-backed options, correct action outcomes and exact return.
Expired/unavailable facts stay distinguishable. Cover the meaningful changed
contract and failure path; do not treat one synthetic ferry story as the product.

**Independent work when blocked:** improve supported current-place/commitment
paths and disclose unsupported provider capabilities. Record the exact external
gap without building a parallel operational subsystem or pretending completion.

## 6 Autonomous execution and landing

Each lane starts by reading its roadmap, the ownership section above, root and
affected child AGENTS, Task Intake and relevant owner contracts. It then owns
diagnosis, implementation, focused verification, review corrections and delivery
of its selected outcome. Ordinary debugging does not need an orchestrator reply.

- Keep **one active coherent assignment per lane**, with bounded internal
  subagents only when delegation is authorized and writes are disjoint. Three
  lanes is a capacity limit, not a reason to invent work or run three native
  builds simultaneously.
- The owner updates only its own roadmap's current assignment: exact base tuple,
  owned files/interfaces, finished behavior, remaining gaps and next action.
  Use existing PRs and receipts; no new daily report files or duplicate trackers.
- At assignment start and a meaningful interface/landing checkpoint, inspect
  landed main and the required dependency. No constant polling or direct chat
  relay. If absent, take the named independent work; escalate only a genuine
  product/authority choice or incompatible boundary.
- Complete long slices without status chatter. Checkpoints are a working result,
  a consequential blocker and a reviewed finish. A helper's completion is not
  automatically a reason to redispatch or stop the owning lane.
- Integrate additive interfaces and complete useful increments while the next
  part proceeds. Do not merge every tiny commit, but do not keep completed work
  for weeks until all three roadmaps finish. If a dependency cannot land, name
  the specific blocker and stop adding dependent branch-only work.
- Each owner lands its own slice; Orchestration is not a required manual relay
  for ordinary merges. Serialize actual landings onto shared main, recheck the
  current base and affected compatibility, and follow the existing lane/CI policy.
  Land required child changes and then the workspace's matching contract/lock
  tuple. Never advance another session's checkout or overwrite its lock blindly.
- Publishing, merging and deployment use their actual authorization. Passing a
  local subset does not waive required hosted checks. A complete worktree can be
  reused after landing; retiring it follows the existing recovery-safe lifecycle.

### Proportionate verification

Use focused checks during iteration. For a landing candidate use
`make verify-changed WORKSPACE_BASE_REF=<base> AGENT_BASE_REF=<base> APP_BASE_REF=<base>`
with explicit bases in that coordinated lane. API changes require
`./scripts/sync-types.sh`, review of snapshots/generated consumers, and
`make api-coverage-check`. Current root/child AGENTS and the
[CI Plan](../reliability/CI%20Plan.md) govern actual required checks.

`make verify` is the full diagnostic/release suite, not a mandatory rerun after
every push. Native acceptance follows visible behavior changes; confirm runtime,
persona, data source and reference before capture. Disposable DB tests require
explicit opt-in. Keep exact commands, revisions and passed/failed/blocked/unrun/
stale boundaries; use existing measurement tooling. Never claim a five-minute
merge guarantee from this workflow or erase tests just to meet a slogan.

## 7 Reassessment and scope control

Reassess after the first shared interfaces, the first connected useful result,
and each complete D/P/R outcome—not every ordinary code change.

Ask: is the received result worth opening; is the original useful without AI;
does context improve it; how much effort remains; does social participation
benefit a thin recipient; are current practical claims dependable; and did we
reuse the correct owners? Review original-only and enriched experiences as
different valid modes. Track finished outcomes, rework, blocked time, generation
cost/latency and founder intervention, not commits or agent utilization.

Catalog rights, unresolved cultural/collection owner choices, shared derivative
retention, connected-inbox policy, automatic preparation and notification cadence
retain their explicit decision boundaries. Record which behavior is blocked and
continue independent supported work. These are not blanket reasons to stop all
three lanes or permission for an agent to decide new product policy.

## 8 Research basis and history

The worktree recommendation follows official [Codex worktree guidance](https://developers.openai.com/codex/app/worktrees/)
and [Git's worktree documentation](https://git-scm.com/docs/git-worktree):
separate checkouts permit parallel branches; they do not settle application
ownership or isolate external runtimes. Our three-repository setup therefore
needs coordinated child checkouts and separate runtime assignments.

[Fowler's integration guidance](https://www.martinfowler.com/articles/continuousIntegration.html)
distinguishes textual from semantic conflicts and warns that pulling main without
landing one's own work does not prevent divergence. Our application is a
bounded-slice landing practice, not a claim of strict continuous integration or
evidence that exactly three agents is optimal. The lane count is the founder's
chosen capacity. Explicit owners, additive interfaces and timely landing should
reduce coordination; measure the result rather than assume a speedup.

H1 remains the detailed implementation/evidence reference, not a fourth active
queue. Earlier program wording is preserved in
[the pre-rebaseline version](https://github.com/fy538/travel-workspace/blob/73d9679409793f337be120bf9d6e39e27c966677/docs/working/vesper-program-roadmap.md)
and the [September 27 archive](../archive/vesper-program-roadmap-history-through-2026-09-27.md).
The [integration roadmap](complete-system-integration-roadmap-2026-09-05.md)
is technical reference, not another schedule. This update changes planning and
ownership only; it is not new runtime, device, provider or consumer evidence.

## Historical link compatibility

These anchors preserve older references, not old queues.

<a id="2-inspected-baseline--september-22"></a>
<a id="2-inspected-baseline--september-8-after-reliability-landing"></a>
Historical baselines: [September 22](../archive/vesper-program-roadmap-history-through-2026-09-25.md#2-inspected-baseline--september-22)
and [September 8](../archive/vesper-program-roadmap-history-through-2026-09-25.md#historical-september-8-reliability-and-acceptance-evidence).

<a id="4-current-package-register"></a>
<a id="6-coordination-completion-and-next-system-review"></a>
<a id="7-current-acceptance-round--dispatched-september-8"></a>
Historical [package register](../archive/vesper-program-roadmap-history-through-2026-09-25.md#4-current-package-register),
[system review](../archive/vesper-program-roadmap-history-through-2026-09-25.md#6-coordination-completion-and-next-system-review)
and [acceptance round](../archive/vesper-program-roadmap-history-through-2026-09-25.md#7-current-acceptance-round--dispatched-september-8).

<a id="connected-dogfood-experience"></a>
<a id="current-round--meaning-based-discovery-and-exact-original-receiving"></a>
<a id="execution-order-and-event-triggered-reviews"></a>
Historical [connected experience record](../archive/vesper-program-roadmap-history-through-2026-09-25.md),
[discovery/receiving round](../archive/vesper-program-roadmap-history-through-2026-09-25.md#current-round--meaning-based-discovery-and-exact-original-receiving)
and [execution order](../archive/vesper-program-roadmap-history-through-2026-09-25.md#execution-order-and-event-triggered-reviews).
