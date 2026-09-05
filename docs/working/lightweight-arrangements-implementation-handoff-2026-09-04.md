---
doc_type: working
status: active
owner: founder / product / architecture / engineering
created: 2026-09-04
last_verified: 2026-09-04
expires: 2026-10-04
why_new: Connects accepted lightweight arrangement behavior to four complete situations, inspected runtime owners, legacy contraction, and an implementation decision docket.
supersedes: []
source_of_truth_for: []
---

# Lightweight arrangements — experience and implementation handoff

## 0. Status, scope, and reading order

**Product direction accepted in the September 4 Dynamic Artifacts conversation;
architecture below is recommended, not implemented or schema-approved.** This
handoff records the founder's approval to consolidate, pressure-test, and audit.
It does not authorize runtime changes, retirement, migration, or release exposure.

Promise: **Bring an idea, let someone help, try another version, join the part
you want, and keep the important parts clear.** An arrangement helps people
shape something together without requiring everyone to work on planning it.

Canonical authority stays in:

- [Product Model](../../travel-agent/docs/product/Product%20Model.md): product objects.
- [Multiplayer strategy §5.1–5.2](../../travel-agent/docs/product/Multiplayer%20Product%20Strategy.md#51-owner-controlled-collaboration--decision-of-september-4): collaboration behavior.
- [Plan/Occasion lifecycle contract](../../travel-agent/docs/architecture/plan-occasion-lifecycle-contract-2026-08-22.md): ownership and lifecycles.
- [Contribution and consequence](../systems/contribution-and-consequence.md): ingress, authority, retention, readback, repair.

This is the implementation handoff, not another canon. Read §1–3 for experience,
§4–6 for architecture and code, and §7–8 for execution and acceptance. The broader
[surface contraction investigation](product-surface-contraction-investigation-2026-09-04.md)
owns the booking/expense responsibility audit. Do not expand this lane into an
expense or booking redesign. Coordinate with the entity and Home/Places/Life
lanes; do not redesign Chat or Life roots as part of this work.

## 1. Accepted behavior and its limits

1. **Arrangement is a composition, not a new top-level authority.** It presents
   personal intent, bounded shared material, participation, consequences, and
   assistance from their owners. It is not a renamed Trip or universal document.
2. **Current shape is not collective agreement.** Intended stops can be flexible;
   appearing in a view does not enroll its readers or certify attendance.
3. **Possibilities do not create approval debt.** A recommendation may remain
   optional without a pending badge, deadline, or accept/reject demand. A proposed
   replacement of an agreed detail is a different consequence.
4. **Owner edits by default; invited people contribute.** Explicit named grants
   can permit scoped editing. Helping does not imply attending. Editing rights
   do not grant membership, disclosure, spending, or others' commitments.
5. **Personal participation stays personal.** Dinner-only, skipping a stop, and
   rejoining later are ordinary outcomes, not failed consensus.
6. **Explore without mutation.** A less-walking alternative is a preview until
   deliberately adopted; no automatic whole-arrangement rewrite or announcement.
7. **Materiality exceeds technical reversibility.** A database-reversible time
   change can strand someone already traveling. Apply consequence-aware rules.
8. **Human edit grants and AI autonomy are separate.** Vesper may execute the
   owner's explicit permitted instruction in owner-only mode. It may not infer
   autonomous authority from human collaboration or previous helpfulness.
9. **Keep people oriented, not occupied.** Quiet attribution, relevant catch-up,
   and justified interruption serve different jobs. No activity-feed obligation.
10. **Undo repairs a scoped action.** Do not erase later authored comments,
    independently accepted consequences, or unrelated concurrent work.

Loose intention must be retainable without making the user create/name a Plan.
That product requirement does not settle its storage model. Ask may still end
without retention. No mandatory ticket, timestamp, place, or complete sentence.

### Anatomy: distinctions underneath, not five visible sections

| Material | Example | What changing it means |
| --- | --- | --- |
| Current prospective shape | Bookstore before dinner | Changes permitted intended arrangement, not everyone's participation |
| Available possibility | Maya's jazz suggestion | Adds optional material; does not replace current intent |
| Authored contribution and participation | Maya's note; Sam joins dinner only | Preserves author and individual standing; separate owners/commands |
| Protected dependency | Keep dinner fixed; accepted seven o'clock; reservation | Personal constraint, interpersonal agreement, and provider fact remain distinct |
| Generated assistance | Walking comparison or weather fallback | Recomputable projection, not an independent decision or evidence source |

Do not compress these into one status enum. An agreed dinner can have a proposed
new time while its provider reservation remains confirmed at the old time.

## 2. Four complete situations

All names and example venues/times below are fixtures, not live recommendations.
These are specification walkthroughs, not user-tested or executable test results.

### S1 — Solo Saturday, before any named container

Initial state: no Trip, Plan, Occasion, or invitation. The user asks about an
afternoon in the Village. An answer returns useful possibilities without writing
durable intent. They then say, “Keep the bookstore in mind for Saturday; leave
the rest open.”

| Action | Visible result | Canonical consequence | Must remain untouched |
| --- | --- | --- | --- |
| Ask what is possible | A grounded afternoon possibility | Answer/working context only | Personal intent and durable memory |
| Keep bookstore for Saturday | Sparse retained intention; quiet correction | Owner-scoped intent under the chosen future persistence contract | No synthetic Trip, default Life Plan, or Occasion |
| “What if it rains?” | Useful indoor alternative, practical differences | Private preview | Current intention and audience |
| “Use that instead” with clear referent | Selected alternative becomes current | Narrow owner update, source lineage retained | No automatic reservation, invitation, or schedule completion |
| “Forget Saturday, keep the place” | Saturday cue disappears; place remains kept | Release the temporal-intent relation only | Independently retained Source/Place relationship |

Home can show the useful upcoming possibility; Places explains the bookstore;
Life can refind the retained material without requiring a named container. Chat
and direct actions invoke the same owner behavior. A past chat card re-reads the
current owner before action. No command should restore released intent from it.

### S2 — Dinner with friends, contributors rather than a planning committee

Initial state: the owner has personal afternoon intent. A dinner Occasion exists
with explicit invitation/participation records. Seven o'clock is an agreement
only if separately established, not merely because the owner mentioned friends.

| Action | Visible result | Canonical consequence | Must remain untouched |
| --- | --- | --- | --- |
| Maya suggests a bookstore | Attributed optional idea beside the afternoon | Bounded contribution, if shared to that audience | Current shape, RSVP, private sources |
| Nobody chooses it | No pending task or nag | No required mutation | No inferred disinterest or social rejection |
| Owner grants Maya afternoon editing, keeping dinner fixed | Clear scoped capability for Maya | Explicit revisioned grant | Attendance, ownership, money, dinner agreement |
| Maya adds bookstore to afternoon | Current shape updates, quiet attribution | Permitted material edit | Other people's intent; original authored recommendation |
| Sam says “dinner only” | His view centers arrival at dinner | His bounded participation update | Everyone else's afternoon and dinner |
| Owner ends Maya's editing | Future writes stop | Revoke grant; revalidate prepared work | Maya's attendance, accepted edits, contribution history |

The afternoon can be a shared view for collaborators without creating another
Occasion. Shared dinner consequence references the existing dinner owner.
An editor's accepted change to common planning material is not acceptance by
each attendee. A nonattending local friend can contribute under a bounded grant.

Contribution is useful before decision: Vesper may check opening hours or
geographic fit, but should not echo every comment. “Suggest this” and “Add to
afternoon” make their different consequences clear without asking users to
classify every message. Ambiguity defaults to no arrangement mutation.

### S3 — Overlapping travel, split and rejoin

Initial state: one person's Portugal stay is September 2–10, another's is 5–15;
a local friend joins selected activities. These are separate personal horizons.
Shared dinners/visits have their own bounded participation and consequences.

| Action | Visible result | Canonical consequence | Must remain untouched |
| --- | --- | --- | --- |
| Link the overlap for coordination | Relevant common window, private context omitted | Authorized relationship/projection over existing owners | Neither personal Plan merges |
| Local friend suggests one stop | Useful attributed place context | Contribution without attendance | No implicit invitation or location sharing |
| One traveler skips the museum | Their route can lead directly to reunion | Personal participation, not global cancellation | Museum for others; shared dinner |
| Reunion time changes | Affected people see relevant difference | Consequence evaluated for the shared meeting | Private reasons and unrelated dates |
| A traveler leaves the shared episode | Current participation changes; history remains honest | Scoped departure under member/Commitment rules | Other travelers' Plans and authored material |

Do not create a subgroup Occasion for every divergence. Create one only when a
distinct bounded shared undertaking needs independent participation, lifecycle,
or consequences. Personal routing can differ while agreed meeting facts remain
identical at the same revision. Whole-Occasion departure and skipping one stop
must not use the same command. Organizer succession is a separate responsibility
issue; it should not be necessary merely to skip an activity.

### S4 — A consequential change while people are already moving

Initial state: dinner at seven has accepted participants; imported reservation
evidence also says seven; Sam is already traveling based on authorized current
context. Maya's grant permits afternoon edits, not dinner changes.

| Action | Visible result | Canonical consequence | Must remain untouched |
| --- | --- | --- | --- |
| Maya asks to move dinner to eight | Targeted proposal and relevant impact | Prepare outside her editing scope | Accepted seven o'clock and reservation |
| Owner reviews | Show who/what needs recoordination, not a full-plan diff | Evaluate actual Commitment authority | Owner role does not confer others' consent |
| Authorized people settle new meeting time | Current agreement updates with receipt | Commitment command and required participation semantics | Provider reservation still at seven |
| User follows external reservation link | Handoff, not “reservation changed” | External navigation; later evidence reconciliation | Provider status until supported update |
| Sam receives change | Actionable arrival guidance and uncertain response state | Justified notification; personal response if needed | Delivered/read/silent is not consent |
| Old preview is later adopted | Local conflict/readback if state changed | Revalidate target/dependency and grant revisions | No overwrite of the newer agreement |

If agreement and reservation cannot be made consistent, show the practical
mismatch rather than a confident “done.” Do not resurrect booking execution to
close this gap. If the time was only a draft and nobody relied on it, use the
lighter permitted edit path instead of the same ceremony for every dinner.

## 3. Cross-situation interaction requirements

- **Return:** show current useful shape first; catch-up names relevant differences
  and meaningful unchanged anchors. Full history remains inspectable on demand.
- **Conflict:** independent changes can compose after semantic revalidation;
  competing changes to the same target stay localized. CAS failure must not
  trigger blind client retry with the whole old document.
- **Repair:** removing a stop from current shape does not delete a friend's note
  attached to its retained identity. Removing their note does not cancel a
  separately accepted dinner. Expired/deleted/revoked sources cannot be revived
  by cached compositions.
- **Offline:** cached reading and private draft exploration may work. Shared
  changes never display as accepted before server authorization/readback.
  Reconnection revalidates permission, scope, target and dependency revisions.
- **Visibility:** a private preview stays private; intentional sharing exposes
  only its authorized material. A collaborator cannot obtain the owner's private
  source corpus by requesting an explanation or a different view.
- **Ending:** ignored ideas may lose current prominence without destructive
  deletion. Retention follows source/claim/projection policy. Closed episode
  information is not automatically a lived memory or universal preference.
- **Directness:** visible objects offer meaningful direct actions; Chat is an
  equivalent path, not compulsory editing infrastructure. No settings-first flow.

## 4. Recommended architecture decisions before implementation

### D1 — Retained intention before a Plan

**Recommend:** person-owned prospective material with optional Plan association,
kept in the existing graph domain rather than a new microservice. Retaining one
intent does not require a named container. Investigate reuse of governed claims
and anchor references before introducing a narrowly typed intent record.

The August 31 [PlanItem proposal](plan-occasion-projection-and-consumer-architecture-research-round-3-2026-08-31.md#42-recommended-boundary)
required exactly one personal Plan. Do not implement that requirement unchanged:
it would push S1 toward hidden pseudo-Plans or creation homework. Source/Anchor
records still cannot silently become intent. A Commitment is too consequential
to be the default storage for “maybe bookstore.”

Before schema approval, specify stable identity, person owner, optional Plan
association, source lineage, revision, release behavior, and authored temporal
hint. Preserve “Saturday afternoon” or unknown timing without inventing exact
instants; resolve timezone and concrete bounds only when needed for consequence.
Table/name selection remains open. This is not permission for a universal item
table holding comments, reservations, people, and generated cards.

### D2 — Shared material has a shared owner; personal intent does not transfer

**Recommend:** existing Occasion ownership for common planning material and
contributions; explicitly scoped collaboration on personal Plan material is also
possible. These are separate contexts, not two writers for one fact.

A shared suggestion references its author/source and target. Adoption records
which arrangement relation changed without rewriting the source. Creating a
shared consequence establishes a canonical Commitment reference, not copied
dates in each personal item. A composition can reference both personal and
shared owners without becoming a new aggregate.

Unresolved schema task: choose persistence for authored comments/suggestions
and their target edges after auditing custody reuse. Root Source contribution
storage is generated output, not a suitable substitute (see §5).

### D3 — Minimal command semantics, no generic document PATCH

Implementation must distinguish retain/release intent, contribute/correct own
material, suggest/adopt a scoped alternative, edit permitted material, update
own participation, enable/revoke editing, and change a Commitment. These are
semantic responsibilities, not mandated endpoint names or one endpoint per verb.

Every consequential request binds actor, target owner and identity, current
grant, expected target/dependency revisions, exact effect and idempotency key.
Readback returns actual effect, unchanged protected dependencies and repair
eligibility. Grant evaluation belongs server-side; model interpretation cannot
grant authority. Existing root action grants transport a resolved action; they
are not themselves durable human collaboration policy.

### D4 — Alternatives are bounded working material

**Recommend:** preview result plus a dependency manifest and scoped proposed
delta. Keep it transient unless the user retains/shares it. Adoption revalidates
current targets; unrelated updates need not invalidate everything, but a changed
dependency must not silently inherit the old preview. No branch-management UI,
whole-Plan snapshots as new truth, or regenerated tree PATCH.

### D5 — Participation and material changes need explicit domain semantics

**Recommend:** individual participation at the smallest relevant undertaking or
consequence, plus Occasion-wide windows where appropriate. Existing member-window
and Trip attendance facilities are precedents, not evidence of complete clean-
graph support. Define skip/rejoin and response-after-material-change commands.

Editing tentative common material is not collective acceptance. A changed
agreement must preserve who accepted which version or explicitly mark renewed
participation as unresolved. Do not require a group vote for every reversible
change, and do not use an organizer edit as proof of everyone's agreement.

### D6 — Integrate presentation, do not centralize every surface

Use a bounded native arrangement composition, stable owner targets, reusable
actions and receipts. Home selects current value; Places grounds material in
the world; Life refinds owners/evidence; Chat creates and explores. Do not create
four copies or a single giant all-purpose card. Coordinate the object target
and return behavior with the active entity lane without changing its files.

These decisions are architecture-bearing: schema/auth work is founder-only and
contract-sensitive under [Task Intake](../../travel-agent/docs/operations/Task%20Intake.md).
Approve the exact schema/auth ADR before coding those changes. Product acceptance
here is not that implementation approval.

## 5. Inspected code: what exists and what it proves

Snapshot: September 4, backend `fb38e24f1`, app `a3636e13c`; both main. Concurrent
entity work is active. Reinspect HEAD/status before implementation. Searches
covered graph models, schema, commands/routes, relevant mobile readers/actions,
Trip surfaces, contribution transport and named tests; not every repository file.

| Evidence | Finding | Implication |
| --- | --- | --- |
| [Graph Plan/Occasion models](../../travel-agent/backend/core/models/experience_graph.py), [schema](../../travel-agent/backend/domains/experience_graph/schema.py) | Plan has owner, kind, lifecycle, title, optional horizon, home entity, Commitment refs. Members have window/status/role/revision. No PlanItem or scoped human editing-grant model found in these inspected graph paths | Add narrowly justified material/policy seams; do not claim absent across every unrelated subsystem |
| [update_plan](../../travel-agent/backend/domains/experience_graph/commands.py) | Owner-filtered metadata replacement, CAS and idempotent receipt; rejects lifecycle changes through shape update | Keep guarantees; not an item editor or delegated personal-Plan write |
| [Graph API](../../travel-agent/backend/api/routes/experience_graph.py) and same commands | Invites, decision votes, organizer resolution, membership departure and transfer exist. Invite response accepts member_window | Not a complete comment/suggestion, post-join partial participation, or arbitrary item editing API |
| [update_commitment](../../travel-agent/backend/domains/experience_graph/commands.py) | Shared update requires organizer; server-owned states guarded; revision checked | Does not by itself establish affected-party reacceptance of a changed agreement |
| [Trip bridge](../../travel-agent/backend/domains/experience_graph/trip_adapter.py) | Explicit legacy block link; legacy block remains execution truth, no provider/occurrence copying | Keep until writer/reader cutover; no graph/block dual-write ownership |
| [Plan Shape compiler](../../travel-agent/backend/core/plan_shape.py) | Uses canonical itinerary read blocks, attendance capabilities and my/together/whole filtering | Useful privacy/participation precedent, still Trip-derived |
| [Mobile shape reader](../../travel-app/data/planShape.ts), [CurrentShapeSurface](../../travel-app/components/trip-itinerary/CurrentShapeSurface.tsx) | Requires trip ID; renders block IDs into settled/flexible/open/changed/unknown sections | Presentation exists, not the new material model; five status buckets are not required new UX |
| [Plan route](../../travel-app/app/%28tabs%29/trips/[tripId]/plan.tsx), [LocalPlanScreen](../../travel-app/components/trip-plan/LocalPlanScreen.tsx) | Local route also receives Trip state; travel route coordinates substantial block/day/review machinery | Compact local appearance does not remove Trip dependency |
| [Collaboration actions](../../travel-app/data/experienceGraphCollaborationActions.ts), [topology](../../travel-app/data/planTopology.ts) | Clean graph invite/decision transports exist; planning windows/topology reader is Trip-scoped | Reuse transport conventions, not claim the new collaboration experience is shipped |
| [Root consequences](../../travel-app/data/rootConsequences.ts) | Opaque server-resolved actions, account-bound handling, root/Places/Trip/graph invalidation and repair transport | Reuse orchestration seam; add owner adapter and verify cache coverage for new material |
| [Contribution models](../../travel-agent/backend/core/models/contribution.py), [root Source contribution store](../../travel-agent/backend/core/db/source_contributions.py) | Storage-neutral authority contract versus short-lived generated root contributions | Neither alone supplies durable authored multiplayer comments |
| [Proposal consequence gateway](../../travel-agent/backend/core/itinerary_proposal_consequence_gateway.py) | Existing read/execute/repair gateway around itinerary proposals | Preserve causal repair pattern; add clean material adapter rather than route everything through legacy proposals |
| [Permissions screen](../../travel-app/app/trip-settings/permissions.tsx), [Changes screen](../../travel-app/app/%28tabs%29/trips/[tripId]/changes.tsx) | Combines plan editing, personal AI delegation, costs/bookings, automation; changes exposes canonical history/error states | Consolidate surfaces, preserve distinct authorities and inspectable history |

Existing test entry points include backend `tests/core/test_experience_graph_commands.py`,
`test_experience_graph_lifecycle.py`, `test_experience_graph_projection.py`,
`test_plan_shape.py`, `test_itinerary_proposal_consequence_gateway.py`, and app
`__tests__/data/experienceGraphCollaborationActions.test.ts`, `rootConsequences.test.tsx`,
`__tests__/components/trip-itinerary/CurrentShapeSurface.test.tsx`. Their existence
is not evidence the new requirements pass. This documentation pass did not run
runtime suites or inspect production data.

## 6. Keep / adapt / replace / retire register

| Classification | Target | Work and removal condition |
| --- | --- | --- |
| Keep | Graph ownership, lifecycle, receipts, provider/occurrence separation | Extend with tests; never discard guarantees because screens shrink |
| Keep | Authored Sources, Place identity, independent participation, deterministic timing and expense arithmetic | Remain capabilities beneath lighter experiences |
| Adapt | Current Shape compiler, topology, contribution gate and root consequences | Preserve lawful projection/actions; support new owner material without requiring Trip IDs |
| Adapt | Change history and repair | Quiet in-context catch-up and scoped correction, full history still reachable; do not hide failure as empty history |
| Replace | Block/day-centric composition as the universal planning surface | Native sparse composition; keep high-resolution travel detail only where useful |
| Replace | Monolithic planning permission experience | Small owner editing control plus consequence-specific behavior; personal AI autonomy remains separate |
| Retire after cutover | Redundant day/block creation/review/move navigation for lightweight local arrangements | New path must support retained jobs, old links must resolve honestly, writer/reader dependencies audited |
| Retire candidate, separate scope decision | Booking execution screens/policies | Resolve actual obligations and release manifest first; external handoff and imported reservation truth survive |
| Do not retire merely for fewer screens | Legacy Trip writers, canonical history, membership enforcement, provider evidence and financial ledger | Delete only after exact retained responsibility migrates or is explicitly ended |

Deletion requires method-aware API caller inventory, deep-link coverage, job and
worker dependency review, retained data/obligation handling, and rollback plan.
No source-file removal is approved by this table. Frozen/dark is not unused;
generic availability/routing resilience may serve Places even when booking ends.
The existing Claude kernel export is interaction inspiration, not schema or
authority truth and not permission to retain its full booking rescue workflow.

## 7. Coordinated implementation packages

Architecture covers S1–S4 together; delivery order follows dependencies rather
than narrowing the product to the first demonstration. No arbitrary week-one
proof environment or deadline to freeze all product thinking.

| Package | Deliverable | Depends on | Acceptance before advancing |
| --- | --- | --- | --- |
| A0 — semantic and storage ADR | Resolve D1–D5: exact records, owners, target references, grants, partial attendance, proposal/adoption effects | This handoff plus current code reinspection | Founder approval; all four scenario transitions map to one authoritative writer; no pseudo-Plan or universal blob |
| A1 — owner commands and read model | Migrations, typed commands, scoped permissions, current-state projection, receipts and recovery | A0 | Unit/route/real-DB transaction tests for authority, concurrency, idempotency, revoke-in-flight, lineage; optional timing survives |
| A2 — shared arrangement interaction | Bounded native composition, contextual contribution/direct edits and same commands from existing Chat integration | A1; entity target/return contract | No mandatory configuration or review queue; contributor/editor distinction legible; no Chat/Life root redesign |
| A3 — alternatives and meaningful changes | Scoped preview/adoption, partial participation, changed-agreement handling, catch-up, repair | A1–A2 | S2–S4 conflicts, dependencies, provider mismatch and notification/response separation work end to end |
| A4 — root integration and contraction | Home/Places current value, Life refinding, old-route redirects, staged legacy removals | A1–A3; HPL coordination | All four surfaces read same owners; source revocation/repair propagates; retained jobs covered before removal |

Schema/route changes require workspace `scripts/sync-types.sh`, review of full
and app OpenAPI snapshots plus generated types, and mobile typecheck. Register
new/retired operations in the API governance policy and run coverage checks.
Run existing regressions plus new portfolio tests; pure mocked unit success is
not evidence of concurrent DB correctness. Mobile UI changes use the registered
surface QA process with real native capture; no visual claims from Jest alone.

Uncertain/failed writes must not claim success. Stop old writers before promoting
the new owner for a migrated record. Prefer explicit per-record compatibility
bindings and migration receipts; a feature flag must not enable competing owners.
Rollback may restore a compatible reader, but must not replay an obsolete writer
against material already migrated. Define this before deleting routes.

## 8. Acceptance portfolio and remaining decisions

| Required fixture | Required negative behavior |
| --- | --- |
| Ask then explicit Keep without Plan | Ask does not write intent; Keep does not create dummy Trip |
| Comment, suggestion, and direct edit | No comment/like/view silently becomes edit, RSVP, vote or preference |
| Scoped nonattending collaborator | No implied membership, private-source access, dinner authority or future-Plan grant |
| Independent concurrent edits and same-target conflict | No whole-arrangement overwrite; permission rechecked after rebase |
| Grant revoked while action prepared/offline | No future mutation under stale grant; accepted history remains |
| Preview on old revision, adopt after dinner changes | No stale protected dependency overwrite or duplicate result on retry |
| Dinner-only, skip and rejoin | No cancellation for others or forced new subgroup container |
| Agreed time changes while someone travels | Notification is not acceptance; materiality not reduced to DB undoability |
| Reservation conflicts with intended time | No false provider confirmation or fabricated external execution |
| Remove adopted idea with later comment | No erasure of independent authored material or Commitment |
| Correction across Home/Places/Life/Chat | No stale action resurrection or hidden false claim on another surface |
| Closed episode and expired possibility | No inferred attendance, shared meaning, or permanent disinterest |

Still to decide in A0: exact lightweight storage; stable targets for optional
material before a Plan; Occasion contribution persistence; per-consequence
participation/reacceptance; scope-grant representation and policy revision locks;
shared-delta transaction boundaries; lifecycle and retention of kept alternatives.
Recommended answers are in §4; do not mistake working names for generated API
contracts. Detailed card layout belongs in the dedicated design tool after these
behaviors are expressed, not before or as a substitute for them.

## 9. Research and conversation provenance

This handoff derives from the September 4 Dynamic Artifacts discussion: owner-
controlled editing approval; five remaining collaboration questions plus AI
authority; online research; accepted arrangement walkthrough; approval of the
three-step consolidation/audit. It does not claim a fresh reread of every fork.
The August 31 [effortless editing research](ai-native-effortless-editing-and-composition-research-2026-08-31.md)
and [Round 3](plan-occasion-projection-and-consumer-architecture-research-round-3-2026-08-31.md)
provide the earlier chronology, including the now-reopened mandatory Plan parent.

External sources researched in the preceding turn:

- [Twine, CSCW 2021](https://coseq.kixlab.org/): 45 people in 15 friend groups;
  useful preference awareness, but its individual-itinerary preparation is not a
  workflow recommendation for Vesper.
- [Parallel Paths, CHI 2004](https://ecl.cc.gatech.edu/sites/default/files/publications/C.47-Terry-CHI-2004.pdf):
  alternatives versus revisions; image-editing research used as an analogy, not
  evidence that our travel interaction is validated.
- [Workspace awareness](https://www.cs.usask.ca/faculty/gutwin/1999/WA-theory/Theory-submitted-TR.html):
  contextual knowledge of others' actions, not a requirement to expose all activity.
- [Group POI sequences, RecSys 2019](https://portal.fis.tum.de/en/publications/user-centered-evaluation-of-strategies-for-recommending-sequences/):
  study of 40 groups supports considering temporary splits; not autonomous split authority.
- [AI participation, 2025](https://arxiv.org/html/2501.17258v1): small employee
  brainstorming study warns about intrusive AI contribution; not a universal ban
  on proactivity.
- [Multi-user AI editing, 2025 preprint](https://arxiv.org/html/2509.11826v1):
  30 people/14 teams, largely academic, no comparative baseline; contextual help
  and control findings inform hypotheses rather than consumer outcome claims.
- [Partiful cohost rights](https://help.partiful.com/en-us/articles/15525428-can-my-cohosts-cancel-or-delete-the-event)
  and [changed-event guidance](https://help.partiful.com/en-us/articles/15525362-i-changed-the-time-date-of-my-event-how-do-i-figure-out-if-my-guests-can-make-the-new-time-date):
  product precedents for the scope and response problems, not templates to copy.

## 10. Validation receipt

Documentation-only pass. Runtime, migrations, prompts, design exports, generated
API contracts, release flags, and concurrent entity work were not changed.

- Workspace and backend `git diff --check`: passed.
- Workspace governance metadata for the new handoff, revised Round 3 report,
  and contribution contract: passed.
- Workspace living-document links: passed, 416 files at the check snapshot.
- Backend documentation links: passed, 10,213 Markdown files.
- Backend canonical headers: passed, 56 files.
- Canon word budget: touched Product Model and company orientation are within
  budget. The broader gate still fails on the unrelated app Design Language
  document at 3,506 words against 3,500; it was not edited here.
- No runtime tests, production checks, migration rehearsal, native visual QA,
  user study, or deletion validation were performed. S1–S4 remain specifications.

Files remain uncommitted. Unrelated root inventory, object-page handoff, design
integration, and Life-lane work remain outside this pass.
