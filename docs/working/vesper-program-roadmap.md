---
doc_type: current_status
status: active
owner: founder / coordination task
created: 2026-09-07
last_verified: 2026-09-28
why_new: Owns the single live cross-lane execution queue, accountable package assignments, and system reassessment without duplicating product or implementation contracts.
supersedes:
  - current assignments and sequencing in the historical program and Integration roadmaps
source_of_truth_for:
  - cross-lane program priorities and accountable assignments
  - cross-lane dependency routing and system reassessment
depends_on:
  - ../decisions/2026-09-06-reconcile-consumer-strategy.md
  - ../decisions/2026-09-26-multiplayer-direction.md
  - ../decisions/2026-09-27-documenting-core-loop-and-one-composer.md
  - ../systems/four-root-loop-object-surface.md
  - ../systems/contribution-and-consequence.md
---

# Vesper program roadmap

## Direction and immediate priority — September 28

Build the complete product on the connected system already implemented.
**Finish the remaining Home value and usability work, then implement the accepted
horizontal capture/share experience.** Landing the published Home package is a
separate delivery task, not a reason to redispatch its completed connections or
wait on every unfinished design.

The four moves remain **Make sense. Open possibility. Help it work. Carry
forward.** Home returns value for now and the anticipated future; Places opens
the situated world; Chat supports conversation; Life organizes what can be
revisited. Multiplayer and practical adaptation run through these experiences.

The [September 26 multiplayer direction](../decisions/2026-09-26-multiplayer-direction.md)
and [September 27 core-loop/composer decision](../decisions/2026-09-27-documenting-core-loop-and-one-composer.md)
now sharpen the entrance: documenting for oneself or others, through one
composer with many doors. Chat is a door, not a compulsory gateway. Immediate
benefit, private Keep with Undo, explicit audience and provisional interpretation
must coexist. This is not diary homework or a return to booking execution.

Those two decision files are unchanged snapshots brought from the concurrent
design checkout into this execution lane on September 27. Their accepted
rulings constrain the next implementation; their presence does **not** mean the
owner contracts, schema, runtime or all design boards have been updated.
Their pending recommendations remain pending.

This file owns the only current dispatch queue. The
[H1 package](home-value-composition-execution-plan-2026-09-25.md) owns implementation
detail and current evidence; the
[integration reference](complete-system-integration-roadmap-2026-09-05.md)
owns supporting technical guidance, not another schedule.

## Inspected baseline and publication state

The recovery work is merged on remote main; the subsequent Home package is
published but **not merged**. Remote branch heads and all three PR states were
rechecked on September 28; the table below is the published baseline, not a
claim that the local follow-up has shipped.

| Repository | Merged recovery baseline | Published Home candidate | Open PR |
| --- | --- | --- | --- |
| Workspace | `6ef3dca09be2b4ea40c83ae21d8cbf112ee17f24` (#36) | `a73e9d2348c07b398a91a4aee3733cfca4485252` | [#37](https://github.com/fy538/travel-workspace/pull/37) |
| Backend | `c8c9f578594a98beb41300c1a780f86ebb30eca4` (#233) | `c50b2286e9fcb477d015d7df20bcfdcce791f8b6` | [#234](https://github.com/fy538/travel-agent/pull/234) |
| App | `43225df35a01295993def384b5958c53ab8f1c8b` (#201) | `551e2a94b1ef58137a2fa7b3e309b245571e7e17` | [#202](https://github.com/fy538/travel-app/pull/202) |

The coordinated `codex/home-value-delivery` lane owns the Home candidate in all
three independent repositories. Workspace `1f4a9e5` contains the local roadmap
and accepted-decision rebaseline beyond the published tuple. App `332e77523`
adds reading clearance, quieter provenance, readable comparison rows and a
lighter original-reader door. App `64961a9cf` completes the next H1-A patch:
useful editable Home-to-Chat questions, readable/removable source context and
draft preservation without starter prompts reappearing. Its 102 focused tests,
app gate, 48 backend owner-grounding tests and three targeted native reviews
passed. These bounded reviews retain content/hierarchy residuals; the full
matrix remains MIXED. Both patches are local, not published or merged, and need
the coordinated gate before publishing. H1 records exact evidence and remaining
findings. Backend is clean at the published head.

Local canonical `main` checkouts are not identical to remote main: workspace
`8a14d87` also contains separate design commits and dirty design work; backend
`fdf789d06` and app `23cff76f4` predate the merged recovery baseline. Do not derive
completion from the local branch name. Re-inspect heads, dirty changes and PR
state before execution; a dated table is not current Git state.

The separate canonical checkout contains concurrent design work and is not the
execution target. Do not switch it, advance its children, or bring unrelated
uncommitted design changes into this lane.

| Evidence at the published tuple | State and boundary |
| --- | --- |
| Coordinated local verification | `scripts/land-worktree.sh home-value-delivery --publish` completed `make verify` and published the three branches. This evidence predates the docs-only rebaseline; detailed counts and exclusions are in H1. |
| Backend CI | [Passed](https://github.com/fy538/travel-agent/actions/runs/36355954051), including DB and migration checks. |
| App CI | [Passed on the final app head](https://github.com/fy538/travel-app/actions/runs/36358544184), including tests, types, design/governance and contracts. |
| Workspace CI | [Failed before product tests](https://github.com/fy538/travel-workspace/actions/runs/36355993401/job/108723720414): private child checkout could not authenticate. Renew/fix `TRAVEL_WORKSPACE_CI_TOKEN` access, then rerun. A configured secret is not proof of usable access. |
| Merge | All three PRs remain open and review-required; no merge conflict was reported. User authorization to publish/merge is already recorded in the task. Any owner-approved one-off override must be reported with the failed/unrun boundary intact; do not silently change standing protections or label an override a passing check. |
| Native product quality | Full Home matrix remains MIXED. Targeted Planning and Cold follow-ups passed their bounded assertions, not full-scroll design parity. The newer local H1-A patch does not inherit a full PASS from these older captures or from its passing component checks. |

## What is already delivered in the candidate

| Capability | Established progress | Still not established |
| --- | --- | --- |
| Supported Source value | Canonical owner discovery/read, explicit preparation, production boundary, saved result, Home serving and withdrawal connected; rejected outputs preserve their true terminal outcome | Recurring useful supply or real-model editorial quality; the integrated producer caller was deterministic |
| Contextual Home continuation | Exact Plan/opening/recovery context reaches a private editable Chat draft and supported backend prompt assembly | Quality of a real model answer or authority to send automatically |
| Received original | Exact authorized private photo through local DB, object storage, API and native reader/return | Production media service, album/grouped-photo identity, Reply or broader audience model |
| Practical value | Supported open-now possibility reaches the exact venue and returns | Provider-backed freshness or a generalized live service |
| Cold Home | Source-backed current-Places reading before an input request; owner-backed local API to native depth and return | Real recurring editorial supply, full design parity |
| Native composition | Compact planning motion, corrected Home glyph/region treatment, removed gold reading edge, exact return position and selected first-viewport references | All remaining matrix findings resolved or full-scroll reference acceptance |

Do not repeat these connection projects under new names. The
[H1 completion map](home-value-composition-execution-plan-2026-09-25.md#delivered-connections)
records their limits. More tests or fixture screenshots of the same paths alone
are not the next product increment.

## Current dispatch queue

| Order | Outcome / accountable owner | Finish condition and next decision |
| --- | --- | --- |
| 0 — delivery closeout | Current lane owner closes the three published PRs, preserving exact revisions and evidence. Fix the workspace checkout credential through the repository owner; honor already-recorded merge authority without treating blocked checks as green. | Record actual merged heads and branch/worktree disposition. Reuse the lane for follow-on Home work if it remains suitable; do not archive it merely because a PR merged. This administrative gap does not block independent local building. |
| 1 — active H1 remainder | Same owner finishes the remaining bounded usefulness/hierarchy work under the [assignment](home-value-composition-execution-plan-2026-09-25.md#next-complete-assignment); reading/navigation/original-door and exact-context Chat patches are committed. Trace and repair the next actual authorized supply gap using existing owners. | Address remaining producer copy and receiving hierarchy, retaining changed-state evidence and explicit preparation/serving limits. Close the connected package or name the specific remaining gap; do not expand H1 into all future content production. |
| 2 — next capture/share package | One coordinated owner reconciles the accepted decisions with contribution, Chat and social owners, then implements the common private Keep/Send path. Begin with a contract/door map, not a new universal artifact store. | A complete authored item can enter, return immediate value, reach its selected authorized audience, be refound and be corrected/withdrawn. Door coverage and staged implementation order must be explicit; completing one adapter is not completing all six entrances. Pending policies remain excluded. |
| 3 — reassess receiving and later value | At the capture/share checkpoint, choose the next whole-product package against the actual retained/shared material: richer Home/Places receiving, Life continuity, or an accepted preparation gap. | Select from observed code/design gaps and received benefit, not a standing parallel backlog. Do not launch all three automatically. |

**Next execution checkpoint:** reading/navigation and exact-context Chat patches
are complete locally; do not repeat them. Work the remaining producer-copy and
receiving-hierarchy clusters in H1, and classify the supply gap as
implemented-but-unverified, a repair in an existing authorized path, or a
capability requiring a separate decision. Missing
external access does not justify repeated fixture rehearsals or indefinitely
postponing capture/share. Keep a specific residual; do not declare it solved.

### Capture/share package boundaries

The next owner should produce one compact implementation map in the active
package, using existing canonical owners and generated contracts. It must cover:

- **Owner reconciliation before affected runtime changes:** contribution §3.2,
  §9 and §12; Product Thesis/Model entrance wording; Chat ruling 04; group/social
  optional polls and occasion rooms; relationship audience and use-grant rules.
  Amend only accepted rulings, retain rationale, and identify remaining conflicts.
- **Shared path:** just-me default, Keep/Send/Share labels, immediate private
  custody with Undo, provisional recognition and truthful send-time payoff.
  Remove review-first capture without replacing it with invisible personal claims.
- **Doors:** OS share sheet finishing in place; camera/photo picker; global add;
  Chat attachments with visible keep state and Ask only; existing-object Keep/Send;
  email forwarding. Audit existing adapters, share one contract, and identify
  native/server delivery constraints rather than pretending every door is a
  React component.
- **Receiving and repair:** existing selected-original and place/link ownership,
  authorship, permitted audience, forward-only Friends eligibility, withdrawal
  and independent kept place survival. The newer audience model is accepted
  direction but its schema is not designed; do not force it through the old
  place-required one-recipient note or silently widen an existing grant.
- **Separate policy dependencies:** friend's words used for an explicit question
  require the named use-grant amendment. Guest identity, notifications, retention
  periods and export are not settled by the decisions; they need a ruling only
  where the selected implementation depends on them.

The September 27 R1–R5 recommendations are **not adopted by this roadmap**:
thread-intersection mechanics, the new voice register, autonomous artifact-type
evolution, status-triggered offers and the proposed intersection-offer sequence.
The accepted one-composer work can proceed without them. Selecting capture/share
as the next package does not approve an offer that depends on those pending rules.
Casual-question continuity remains unadopted; deliberate share-plus-question is
the separate accepted amendment.

## Execution and reassessment

Use the existing [lane lifecycle](../Workspace%20Repo%20Setup.md) and root AGENTS.
One owner keeps responsibility through landing or an explicitly held disposition;
temporary workers require authorized delegation and disjoint write ownership.
Keep at most one or two active implementation packages, not a new tracking system.

- **One complete assignment per round.** The owner carries diagnosis, implementation,
  focused tests, review corrections and landing. Ordinary debugging needs no
  founder round trip.
- **Parallelize only independent outcomes.** A bounded worker can handle Home
  presentation while another inspects existing preparation/serving, with one
  owner for shared wire contracts and navigation. Contract mapping for the next
  package can run independently; no competing runtime owner or permanent
  integration lane is needed.
- **Check in at the first working result, a consequential decision/blocker, and
  the reviewed finish.** Coordinate shared files, runtime and devices directly;
  escalate changed product/authority/architecture choices.
- **Verify proportionately.** Focused checks during implementation; affected
  contract/behavior/native evidence at package completion; required coordinated
  `make verify` before publication. Do not repeat the full matrix for every copy
  change or replace the required gate with a weaker one.
- **Maintain this roadmap in place.** Replace the baseline and queue; do not
  prepend dated overrides. H1 holds one current evidence summary; large receipts
  remain historical. Retire or replace its active assignment when done, not by
  accumulating another endless log.

At each package checkpoint ask: what is now worth receiving; does context improve
it; how much effort remains with the person; did we reuse the right owners; and
what exact evidence supports the result? Judge progress by finished outcomes,
rework, blocked time and founder intervention—not agents, commits or doc volume.

Documentation validation: the September 27 rebaseline refreshed the generated
inventory with `make docs-status-sync`; this September 28 status update changes
no registry and passed `make docs-check` for the updated documents. No additional
product behavior is changed by this update; the separate locally committed app patch
and its checks remain explicitly bounded in H1. A docs check does not refresh
the full coordinated product gate.

## History, not another queue

The [September 27 program snapshot](../archive/vesper-program-roadmap-history-through-2026-09-27.md)
and [H1 receipts](../archive/home-value-composition-history-through-2026-09-27.md)
preserve the full prior bodies at workspace `a73e9d2`. Older strategy and
integration history remain linked below. No historical “current” statement
overrides the baseline above.

## Historical link compatibility

These anchors preserve older references. They do not reactivate old queues.

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
