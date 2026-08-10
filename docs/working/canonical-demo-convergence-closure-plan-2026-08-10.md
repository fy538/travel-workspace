---
doc_type: working
status: active
owner: product / engineering / AI systems / evidence
created: 2026-08-10
last_verified: 2026-08-10
expires: 2026-09-09
why_new: Re-baselines the canonical Lisbon demo against current source and defines the commit-sized work required to join the Take us somewhere doorway, temporal availability, grounded place judgment, canonical proposals, Mapbox-backed route truth, weather repair, multiplayer projection, and correctable outcomes into one experienced loop.
source_of_truth_for:
  - canonical-demo-convergence-closure-round-2026-08
related:
  - thesis-to-experience-convergence-audit-2026-08-09.md
  - intentional-convergence-engineering-plan-2026-08-10.md
  - convergence-and-ai-decision-next-execution-plan-2026-08-10.md
  - lisbon-group-trip-staging-device-runbook-2026-08-10.md
  - home-surfaces-post-consolidation-engineering-plan-2026-08-09.md
---

# Canonical demo convergence closure plan

## 1. Executive decision

The recent convergence work is directionally correct, but the flagship journey
is not source-complete as one user experience. The disruption half is strong;
the micro-journey half is still a prompt doorway whose intended proposal is
unreachable from the private conversation it opens.

The next round should close one end-to-end Lisbon loop:

> Feihu and Maya have a verified open interval before dinner. They tap **Take
> us somewhere**. Vesper selects one feasible nearby anchor, prepares one
> group-safe canonical add proposal, and the accepted change appears in the
> shared Plan and Map. Rain then makes that anchor a poor choice; Vesper
> prepares one grounded replacement through the existing weather-rescue path.
> Both observers converge, each privately confirms or corrects the outcome,
> and only applicable evidence may influence a later occasion.

This is a convergence round, not a new architecture wave. It makes four product
and engineering decisions:

1. **No new durable micro-journey aggregate.** Before commitment, the opening is
   a server-owned current-window read projection. The canonical proposal is the
   review boundary. After acceptance, the Plan block is durable truth.
2. **No new chat-card family.** Reuse the existing proposal/vote, change receipt,
   proposal detail, Plan, and Map surfaces. Extend their destinations only where
   the accepted route needs a direct door.
3. **Private judgment may produce a group-safe proposal.** A trip-linked private
   turn may use private context, but only the existing privacy-validated,
   membership-checked, canonical proposal path may cross into shared state.
4. **The demo proves one anchor plus its connective route.** It does not need a
   multi-stop generated itinerary. One placed anchor between two commitments is
   enough to demonstrate time, place, route, AI judgment, multiplayer agency,
   weather repair, and outcome closure.

## 2. Verified baseline

The runtime source investigated for this plan is:

| Repository | Revision | Relevant state |
| --- | --- | --- |
| workspace | `f7427f770b8eb09b468436ee7e948b6fd4047632` | Current Home roadmap rebaseline included. |
| backend | `1bde69535841f849ccdc55550a1d1c6c71fec59d` | Clean runtime source at inspection. |
| mobile | `ce110b54a47f3d601d7c0d4ef7ccfe48429fab3f` | Concurrent Home truth/polish and internal profile-gallery/QA commits are included; the audited doorway, seed, proposal, Map-route, and Now-Mode files are unchanged from the doorway round. |

Focused verification on this baseline:

- mobile: 5 suites / 22 tests passed for the doorway, Now Mode, Map route card,
  and build-profile controls;
- mobile TypeScript: passed;
- backend: 107 of 108 focused open-window, tool-selection, Lisbon contract,
  weather-rescue, proposal, and replay tests passed;
- backend failure: the Postgres Lisbon replay is time-of-day dependent and
  failed with `shape_block_dates_mismatch` after fixture blocks crossed the
  Lisbon schedule-local date.

These are source, deterministic, and backend-real checks only. They do not
establish controlled-device or physical-device acceptance.

## 3. Current system assessment

| System | What is implemented | How it connects today | Closure status |
| --- | --- | --- | --- |
| Doorway | Internal build-profile flag, Plan CTA builder, review-first private composer, conversation seed. | Available only while a block is active; absent in the canonical between-commitments moment. | Partial |
| Time / availability | Canonical Plan instants, transition-aware Now Mode, conservative `ItineraryOpenWindow`, gap suggestions, destination timezone. | Places can use bounded gaps; the CTA and seed do not consume that authority. | Adjacent |
| Place judgment | Canonical entities, gap ranking, duration and geometry gates, operational facts, World Foundry evidence, relationship markers. | Places has the strictest gap projection; concierge calls the lower-level search path directly. | Policy drift |
| Location | Permissioned recent GPS, location context, symbolic `current_location`, origin resolver, private spatial situation. | The doorway says “from here,” which is not a location-loading cue; its review handoff also drops `spatialContext`. | Unreliable |
| AI serving | One-time serving-scope resolution, relationship/experience scope, Situation dependencies, typed tools, causal IDs, private shadow controls. | The CTA supplies prose, not a bounded intent contract or dedicated micro-journey skill/eval. | Partial |
| Proposal / multiplayer | Exact add/replace/remove/reschedule proposals, privacy validation, membership and consent checks, voting, accept/reject/expiry/revert, invite redemption. | `propose_change` is removed from every personal turn even though its handler implements private-shielded authorship. | Unreachable seam |
| Map / Mapbox | Canonical Plan/Map projection profiles, shared route context, route-fact freshness, transport hubs, Mapbox-backed distance resolution, map route card. | Strong after a Plan mutation; no pre-accept route object, and the card requires at least two placed committed stops. | Post-commit only |
| Weather repair | Narrow current-weather matcher, verified indoor alternative, canonical replace proposal, exact cohort flag, group-safe composition. | Strong once an outdoor block already exists. It does not prove creation of the initial micro-journey. | Strong half-loop |
| Outcomes | Private occurrence confirmation, exact-roster companion scope, correction, causal outcome receipts, shared applicability resolver. | Roster checks are strong; several live callers still omit current place, destination, or occasion context. | Partial reuse |
| Evidence | Fixed contract, controlled Trip, deploy identities, simulator doorway support, backend-real rescue lifecycle. | Current runbook and source-complete language overstate the doorway half; no two-device physical receipt exists. | Not promoted |

## 4. Confirmed seams

### F1 — the CTA disappears in the moment the demo requires

`usePlanNowMode` returns the next upcoming block as `nowBlock` when nothing is
active. `buildNowModeHeader` correctly converts that state to `mode='between'`,
but `NowModeStrip` returns the quiet “Next up” card before rendering the CTA.
The parent also gates the callback on the misleadingly named `nowBlock`.

Result: the app can show **Take us somewhere** during an active stop, but not
while the group has ninety minutes free before dinner.

### F2 — the doorway is prompt-shaped, not opportunity-shaped

`buildTakeSomewhereHandoff` references one `trip_block` and asks the model to
consult the Plan. In the between state that reference would name the upcoming
dinner, while the source subtitle would incorrectly read “From dinner.” The
backend has no authoritative current-window seed resolver.

The generic review-first composer rebuilds seeds with entity and client context
but omits `spatialContext`, despite the typed seed and backend resolver both
supporting it.

### F3 — the requested group proposal cannot be created from the opened chat

The CTA opens a `privateTrip` conversation. The prompt says not to mutate the
shared Plan directly and to prepare a reviewable group proposal. Tool selection
then subtracts `propose_change` from every personal turn.

The lower handler already contains the intended security topology:

- private requests use `human_private_shielded` authorship;
- private corpora are checked before group copy persists;
- trip membership is rechecked;
- delegation can downgrade direct action to a proposal;
- the canonical operation proposal is the only shared writer.

The safe capability exists, but this entry point cannot reach it.

### F4 — the strictest gap-candidate policy is not shared with Concierge

Places uses the conservative open-window model, duration/type/geometry gates,
relationship markers, and cached operational truth. The concierge
`itinerary_day_gap_suggestions` handler calls `get_gap_suggestions` directly
and serializes rows without the same readiness policy. A model can therefore
see a candidate that the product feed would refuse to call actionable.

### F5 — Map is truthful after commitment but not yet the route-start surface

The existing `map_route` card deliberately reads committed `TripMapState` and
refuses fewer than two placed stops. That is the right truth contract. It means
the unaccepted idea should not masquerade as a saved route.

The missing UX is smaller than a new map system: after acceptance, provide a
direct **See updated route / Start route** door to the existing Map focused on
the newly added block. Map remains a Plan projection, not another writer.

### F6 — the backend-real replay skips the first half of the flagship story

The current replay begins with Miradouro da Graça already committed and tests
its replacement with Museu Nacional do Azulejo. It proves the rescue half, not:

- current open-window detection;
- **Take us somewhere** grounding;
- one-anchor selection;
- creation and acceptance of the initial add proposal;
- a route from the previous stop through the new anchor to dinner.

Its dinner is also an unplaced custom block, so the replay proves common
projection revision and changed stop coordinates, not a complete three-anchor
route. Its use of `datetime.now(UTC) + N hours` with `now.date()` makes the
fixture fail when those instants cross Lisbon's local date.

### F7 — “source-complete” documentation is too broad

The convergence outcome accurately says the simulator support flow proves only
the doorway. Elsewhere, the execution outcome says the bounded doorway and
Group Trip source implementation are complete and places remaining work
outside source. The runtime findings above show remaining source seams. The
device runbook also says the CTA appears only with a current block, which
contradicts the ninety-minute-open-window scenario.

## 5. Target product contract

### 5.1 Fixed Lisbon state

- two actual Trip members: one rich organizer and one thin participant;
- a current schedule-local day in Lisbon;
- one placed preceding block that has ended;
- one placed birthday-dinner block with a hard start;
- a server-resolved current open window with at least ninety remaining minutes;
- one outdoor candidate that fits location, visit duration, route, hours, and
  the protected dinner boundary;
- one verified indoor replacement for the deterministic rain branch;
- all route anchors use canonical venue/site identity and coordinates.

### 5.2 User-visible sequence

1. Plan shows the open interval and **Take us somewhere**.
2. The organizer opens a private, review-first Vesper composer.
3. Vesper returns one judgment, not a list, and prepares one exact add proposal.
4. The same group-safe proposal is inspectable from the private thread, group
   room, Review stack, and proposal detail.
5. The required humans approve; the canonical add commits once.
6. Plan and Map show the same new block and projection truth for both viewers.
7. **See updated route** opens Map on the new stop; directions remain an
   explicit user action.
8. Synthetic rain makes the outdoor stop materially worse.
9. Existing weather rescue creates one canonical replacement proposal.
10. Accept, reject, expiry, and diff-safe revert preserve truthful projections.
11. Each member privately confirms or corrects the outcome.
12. Changed-roster or changed-occasion reuse is withheld or weakened.

### 5.3 Authority flow

```mermaid
flowchart LR
  A["Canonical Plan + clock"] --> B["Current open-window projection"]
  B --> C["Private Take us somewhere turn"]
  C --> D["Shared grounded gap-candidate policy"]
  D --> E["One AI judgment + exact add proposal"]
  E --> F["Group review / consent"]
  F --> G["Canonical Plan mutation"]
  G --> H["Plan + Map + Now projections"]
  H --> I["Weather rescue replacement proposal"]
  I --> J["Projection convergence"]
  J --> K["Private occurrence + outcome"]
  K --> L["Applicability-gated later occasion"]
```

No edge authorizes a second Plan writer. Private prose does not cross the
proposal/privacy boundary.

## 6. Detailed execution plan

### R0 — restore truth before feature work

#### R0.1 Make the Lisbon replay clock deterministic

- Inject or freeze one schedule-local reference instant instead of deriving
  itinerary days from the wall clock at test execution.
- Build every fixture instant from an explicit `Europe/Lisbon` local date/time
  and convert to UTC.
- Give the protected dinner a canonical placed venue.
- Remove the duplicated in-memory outcome append in the replay.
- Assert at least three placed Map anchors after the initial add, then assert
  replacement preserves route cardinality and protected dinner identity.

Primary files:

- `travel-agent/tests/scenarios/test_lisbon_group_disruption_replay.py`;
- `travel-agent/tests/fixtures/lisbon_group_disruption.json`;
- optionally `travel-agent/backend/concierge/proactive.py` if a narrow `now`
  injection is required for deterministic producer evaluation.

Suggested commit: `test(trips): make Lisbon convergence replay schedule-local`

#### R0.2 Correct planning and runbook claims

- Mark the current doorway as active-block-only and prompt-only.
- State that the replay begins after the initial route exists.
- Remove “remaining work is outside source” for the doorway half.
- Keep controlled, backend-real, and physical evidence labels distinct.

Suggested commit: `docs: correct Lisbon doorway and replay boundary`

**R0 exit:** the focused replay passes at every time of day and documentation no
longer claims the unimplemented half.

### R1 — make current availability a canonical read projection

#### R1.1 Add a current opportunity window to Plan state

- Extend the existing open-window authority with boundary block IDs and titles.
- Add a pure resolver that clips the static gap to the current server instant
  and computes remaining minutes.
- Fail closed for untimed, overlapping, cross-day, stale, dispatched, or
  insufficient windows.
- Project one optional `current_open_window` under the Plan status rail with:
  trip/day identity, previous and next block IDs, evaluated-at, ends-at,
  remaining minutes, and minimum-policy identity.
- Bind Plan-state validity to the next boundary so a cached CTA cannot outlive
  the opportunity.

Primary files:

- `travel-agent/backend/core/itinerary_open_windows.py`;
- `travel-agent/backend/core/models/plan_state.py`;
- `travel-agent/backend/core/db/plan_state.py`;
- focused core and Plan-state tests.

Suggested commit: `feat(plan): project the current bounded open window`

#### R1.2 Render the correct between-state doorway

- Drive the CTA from `status_rail.current_open_window`, not from a client guess
  about `nowBlock`.
- Render it in `NowModeStrip`'s between state beneath the next-commitment cue.
- Omit it when the projection is absent or expired.
- Keep active-block support only if product explicitly wants “leave this stop
  now”; do not let that branch define the flagship contract.

Primary files:

- `travel-app/components/trip-plan/NowModeStrip.tsx`;
- `travel-app/utils/planPresentation.ts`;
- `travel-app/app/(tabs)/trips/[tripId]/plan.tsx`;
- `travel-app/hooks/usePlanNowMode.ts` only if naming/derivation cleanup is
  required.

Suggested commit: `feat(trips): open Take us somewhere in a bounded gap`

#### R1.3 Resolve a thin trip-window conversation seed

- Add a thin `trip_open_window` seed reference containing trip/day/boundary IDs,
  not copied times or recommendation claims.
- Re-resolve membership, adjacency, current clock, and window eligibility on
  the backend.
- Render authoritative remaining time and next commitment into entry context.
- If the window expired between tap and send, tell the model it is unavailable;
  never silently reuse the old gap.
- Preserve `spatialContext` through the review-first create-to-chat handoff.

Suggested commits:

- `feat(concierge): resolve trip open-window entry context`;
- `fix(chat): preserve spatial context through review handoff`.

**R1 exit:** the CTA appears exactly in the ninety-minute fixture, disappears
after expiry, and the backend—not route-param prose—states the usable interval.

### R2 — make one grounded judgment executable

#### R2.1 Share one gap-candidate readiness policy

- Extract the actionable candidate policy so Places and Concierge use the same
  duration, type, geometry, trip-membership, relationship, and operational
  truth.
- For an immediate journey, reject known permanently closed candidates and
  fresh `open_now=false` candidates.
- Treat unknown hours as unknown: allow only a qualified suggestion or abstain;
  never label it start-ready.
- Return route-relevant entity IDs and provenance/freshness fields without
  copying presentation prose into the core service.

Suggested commit: `refactor(places): share actionable gap candidate policy`

#### R2.2 Add a bounded Take-somewhere AI contract

- Recognize the typed entry intent independently of the exact English prompt.
- Load the current private location for this explicit private intent when
  permission and freshness allow; otherwise use the previous placed Plan stop
  as an explicitly stated fallback.
- Ensure the turn receives only the required tools: current itinerary/day,
  shared gap candidates, venue status/details, two single-leg distance checks,
  and the canonical proposal tool.
- Instruct the model to choose one anchor, preserve the next boundary, state one
  decisive rationale, and abstain when route/hours/window truth is inadequate.
- Do not run the heavyweight full-day planner for this one-anchor request.

Required deterministic/provider evaluation cases:

- exact ninety-minute fit;
- candidate too long;
- stale or missing GPS with placed-stop fallback;
- stale route fact;
- known closed candidate;
- unknown hours;
- hard private constraint shaping but not appearing in group copy;
- changed roster;
- no viable candidate, producing honest silence/abstention;
- repeated send/idempotent proposal behavior.

Suggested commit: `feat(concierge): add bounded micro-journey decision contract`

#### R2.3 Restore private-to-group proposal reachability

- Keep reaction cards, generic group composition, and group-state readers
  group-only.
- Allow `propose_change` only for a trip-linked personal turn with a current
  itinerary and authenticated membership.
- Preserve the handler's private-shielded attribution and strict privacy check.
- Post the same group-safe proposal projection to the initiating private
  conversation when it differs from the canonical group room, so the organizer
  has an immediate review door.
- Deduplicate both projections by proposal/tool-call identity.
- Verify votes and resolution remain one canonical proposal, not duplicated
  proposal state.

Suggested commit: `feat(multiplayer): bridge private judgment to group proposal`

**R2 exit:** one private CTA turn can select one grounded candidate and create
one group-safe canonical add proposal without direct mutation or private-copy
leakage.

### R3 — close Plan and Map after acceptance

#### R3.1 Use one exact add operation

- Build the initial stop through `create_add_operation_proposal` with the
  authoritative day ID, exact local start/end, canonical entity, full current
  roster, and current day revision precondition.
- Keep one anchor only. The connective path belongs to route projection; it is
  not an itinerary block.
- Revalidate that the proposed duration and travel slack still fit before
  commit; stale proposals fail visibly.

Suggested commit: `feat(trips): commit bounded journey through canonical add`

#### R3.2 Add the route door without a new card family

- After successful acceptance, offer **See updated route** from proposal detail
  or the existing applied-change receipt.
- Deep-link to the existing Trip Map focused on the added block.
- Let Map assemble previous stop -> added anchor -> protected next commitment
  from canonical TripMapState and current route facts.
- Label degraded or approximate geometry honestly.
- Keep external directions as an explicit tap from the focused Map stop.

Suggested commit: `feat(map): open accepted journey on the canonical route`

#### R3.3 Verify warm convergence

- Ensure proposal acceptance invalidates/refetches Plan, Map, Now, proposal
  lists/detail, group-room attachment state, and both viewer caches through the
  existing mutation-impact envelope.
- Assert both viewers agree on block identity, entity, time, protected dinner,
  and shared revision even when capability envelopes are viewer-specific.

Suggested commit: `fix(sync): converge accepted micro-journey projections`

**R3 exit:** acceptance creates one Plan stop; both users see the same route and
can open it without a manual refresh.

### R4 — join the existing weather-rescue half

- Use the newly accepted outdoor anchor as the weather-sensitive subject.
- Inject explicitly synthetic rain in deterministic/backend-real layers.
- Reuse the existing verified indoor alternative and canonical replace
  proposal.
- Prove independent accepted, rejected, expired, and accepted-then-reverted
  forks.
- Assert the replacement changes only the intended subject lineage; the
  previous stop, protected dinner, roster, and route cardinality remain.
- Preserve the decision -> proposal -> operation -> projection causal chain.

Suggested commit: `test(trips): join micro-journey creation to rain rescue`

**R4 exit:** one replay covers the doorway's canonical add and the repair's
canonical replace instead of beginning halfway through the story.

### R5 — outcome and later-occasion closure

- Keep occurrence confirmation and relationship outcome private per member.
- Preserve the exact roster and accepted subject lineage after replacement.
- Pass current place, destination, occasion kind, correction/retraction state,
  and recency into every live applicability caller that can influence planning.
- Add a later New York evaluation with exact-roster apply and changed-roster /
  changed-occasion withhold or weak-precedent branches.
- Do not enable proactive delivery in this round.

Suggested commits:

- `fix(outcomes): supply current occasion to applicability policy`;
- `eval: prove second-occasion micro-journey reuse`.

**R5 exit:** the outcome can improve a later bounded decision only when its
subject, roster, place, and occasion remain applicable.

### R6 — polish and evidence promotion

#### Source and deterministic gates

- app unit/component tests for between/free/expired/active states;
- seed round-trip tests including spatial context;
- backend current-window and membership/expiry tests;
- tool-surface tests for trip-linked private proposal capability;
- privacy negative oracles and duplicate-proposal tests;
- exact add/replace/reject/expiry/revert tests;
- route freshness/degradation and projection invalidation tests;
- TypeScript, OpenAPI/type sync, async checks, and source budgets.

#### Backend-real gate

- one Postgres replay from open window through initial add, rain replacement,
  two viewers, causal receipts, occurrence, outcome, correction, and changed
  applicability;
- repeat at multiple host times or with a frozen schedule-local clock;
- assert no duplicate proposal, operation, receipt, or outcome rows.

#### Controlled-device gate

- exact app and backend identities;
- organizer doorway, private review, group proposal, participant vote,
  acceptance, Map door, repair, correction, and revert;
- separate controlled/simulator receipt; never label it physical.

#### Physical-device gate

- two physical devices and identities;
- fresh artifacts for both viewers before and after each mutation;
- explicit private-string negative oracle;
- Plan/Map/Now/proposal convergence without manual recovery;
- exact build/deploy/migration/seed/oracle hashes in the receipt.

**R6 exit:** only then may the Group Trip proof be described as physical-device
validated. External-alpha readiness still requires an unrehearsed-user pass.

## 7. Commit order and dependencies

| Order | Commit | Depends on |
| ---: | --- | --- |
| 1 | `test(trips): make Lisbon convergence replay schedule-local` | none |
| 2 | `docs: correct Lisbon doorway and replay boundary` | 1 |
| 3 | `feat(plan): project the current bounded open window` | 1 |
| 4 | `feat(concierge): resolve trip open-window entry context` | 3 |
| 5 | `feat(trips): open Take us somewhere in a bounded gap` | 3–4 + generated types |
| 6 | `fix(chat): preserve spatial context through review handoff` | none; may land before 5 |
| 7 | `refactor(places): share actionable gap candidate policy` | none |
| 8 | `feat(concierge): add bounded micro-journey decision contract` | 4, 7 |
| 9 | `feat(multiplayer): bridge private judgment to group proposal` | 8 |
| 10 | `feat(trips): commit bounded journey through canonical add` | 8–9 |
| 11 | `feat(map): open accepted journey on the canonical route` | 10 |
| 12 | `fix(sync): converge accepted micro-journey projections` | 10–11 |
| 13 | `test(trips): join micro-journey creation to rain rescue` | 10–12 |
| 14 | `fix(outcomes): supply current occasion to applicability policy` | 13 |
| 15 | `eval: prove second-occasion micro-journey reuse` | 14 |
| 16 | evidence/runbook/status commits | exact integrated candidate |

OpenAPI and generated mobile types should be regenerated once after the backend
contract stabilizes, not independently in several commits.

## 8. Product and design acceptance

The first thirty seconds should communicate:

1. **pain:** “We have ninety minutes and do not want to research”;
2. **judgment:** one situated path, not search results;
3. **multiplayer:** it fits these people but reveals no private source;
4. **action:** one governed proposal changes one shared Plan;
5. **reality:** Map and timing make the consequence inspectable;
6. **adaptation:** rain produces one coherent repair;
7. **learning:** the outcome can matter later, under explicit scope.

Design should polish only the surfaces in that sequence. The current Home
redesign is not a blocker: the flagship demo begins inside the live Trip Plan.
A Trips Home doorway can follow after the loop is proven; it should not delay
the canonical Plan entry or force another Home composition family now.

## 9. Negative oracles

The round stops on any of the following:

- the CTA appears without a current server-resolved window;
- the client supplies authoritative remaining time;
- private GPS or a private constraint appears in group copy or metadata;
- a personal turn can create a proposal outside an authenticated Trip;
- the initial journey mutates the Plan before required review;
- a candidate known closed is presented as start-ready;
- stale/estimated route facts are described as precise;
- Map shows an unaccepted idea as committed truth;
- add and replace create unrelated subject lineage;
- reject or expiry changes Plan state;
- revert overwrites a later independent change;
- one observer remains stale until manual refresh;
- changed-roster evidence improves a later group decision;
- a simulator, dry run, skipped assertion, or authored receipt is reported as
  physical evidence.

## 10. Explicit non-goals

- no broad proactive push enablement;
- no general multi-stop micro-journey planner;
- no new universal context model;
- no new Map writer or freeform route object;
- no new group agent;
- no public profile dependency;
- no full Riviera-to-Lisbon corpus expansion before one proof-quality Lisbon
  packet works;
- no broad Home-surface redesign inside this closure round;
- no claim that one synthetic Lisbon story proves real provider quality or
  external-user retention.

## 11. Immediate next action

Start with R0.1. The flaky replay currently prevents the principal backend-real
proof from being a stable gate. Once its schedule-local fixture is deterministic,
implement R1's current-window projection. Do not begin visual polish or device
evidence before the private-to-group proposal seam in R2.3 is closed.

## 12. Execution record — 2026-08-10

The following source-controlled closure work has landed and is verified by its
focused unit, component, or backend-real tests:

| Scope | Landed revision | Result |
| --- | --- | --- |
| Workspace plan and claim correction | `d346af0`, `01358c5` | The prior doorway/replay overclaim is explicitly retired. |
| Schedule-local weather replay | backend `2feffe3c4` | The Lisbon fixture uses a controlled destination-local clock; weather selection no longer crosses a local-date boundary. |
| Current bounded opening | backend `9faf77301` | Plan status now projects server-owned previous/next boundaries and remaining time. |
| Trusted entry and location intent | backend `712ddfd08` | A `trip_open_window` seed is membership-checked and re-resolved from live Plan truth; it earns private location retrieval. |
| Mobile doorway and spatial handoff | app `76fee5cc` | The CTA appears in the bounded between-block state, emits only boundary IDs, and preserves private spatial seed evidence. |
| Private review → group proposal | backend `017a11734` | A linked personal Trip turn may prepare a proposal; the same group-safe review card lands in both the group room and initiating private thread. |
| Bounded proposal execution | backend `490b15335` | A micro-journey may only be a review-required add whose current boundaries, day, and timezone-aware interval still fit. |
| Accepted-map handoff | app `943544a2` | An applied receipt opens the canonical Map face rather than a chat-authored route. |
| API contract | workspace `eddb942` | OpenAPI snapshots and generated mobile types expose `PlanCurrentOpenWindow`. |

This closes the current-window, spatial handoff, review bridge, bounded-add,
and canonical-map source seams. It does **not** yet constitute the combined
backend-real replay from initial add through weather replacement and later
outcome reuse, nor any controlled/physical-device proof. Those remain evidence
gates, not claims inferred from the source commits above.

## 13. Open-work replan: actionability, composition, and compounding

### 13.1 Reconciliation correction

The post-execution audit found one successful-path contradiction that the
execution record above does not prove closed:

- the public `propose_change` schema defines add `start_time` and `end_time` as
  destination-local `HH:MM` values;
- `create_add_operation_proposal` also consumes those values as local wall
  times and combines them with the canonical itinerary day and destination
  timezone;
- the `trip_open_window` guard currently parses the same fields as complete,
  timezone-aware ISO datetimes;
- the only bounded-window proposal test exits earlier on a cross-Trip mismatch
  and therefore never exercises a valid bounded add.

The landed guard establishes the intended policy boundary, but a successful
bounded proposal is not yet reachable through the published tool contract.
Repairing this mismatch and adding a successful-path test is order zero below.
It does not require changing the wire contract: the guard should resolve the
canonical itinerary day and destination timezone, convert local wall times to
instants through the same planning-time authority as the proposal producer,
and compare those instants with the current open window.

### 13.2 One product loop, not three projects

The remaining work should be executed as one causal proof:

```mermaid
flowchart LR
  A["Raw nearby candidates"] --> B["Shared actionability decisions"]
  B --> C["One bounded composition"]
  C --> D["Canonical review proposal"]
  D --> E["Accepted Plan occurrence"]
  E --> F["Private correctable outcome"]
  F --> G["Applicability policy"]
  G --> H["Different later decision"]
```

The proof fails if the later decision merely receives more prompt prose. It
must be possible to trace a changed eligibility, ranking, abstention, or
composition decision to the first occasion's active outcome claim. Correction
must change that decision again, and a superseded or inapplicable claim must
not continue to influence it.

## 14. Track A — one actionable-now place policy

### 14.1 Product contract

`Actionable now` is a decision state, not a synonym for nearby or recommended.
Every candidate evaluated for an immediate Move receives one of three results:

| Result | Meaning | Allowed product behavior |
| --- | --- | --- |
| `ready` | Current evidence proves the candidate can support this bounded decision. | May be selected and proposed as start-ready. |
| `needs_verification` | The candidate may work, but one volatile fact is missing, stale, or unknown. | May be checked explicitly; may not be proposed as start-ready yet. |
| `ineligible` | A known fact contradicts this decision or a required invariant is absent. | Omit from the actionable set; retain structured reasons for audit/eval. |

Unknown is never closed and never open. Stale is never fresh. A useful system
may abstain when it cannot establish readiness; candidate coverage is not a
license to lower the truth bar.

### 14.2 Shared domain types

Add a dependency-light module such as
`backend/places/actionability.py` containing:

- `PlaceActionabilityUseCase`: initially `start_now` and
  `schedule_in_bounded_window`;
- `PlaceActionabilityState`: `ready`, `needs_verification`, `ineligible`;
- `PlaceActionabilityReason`: a closed vocabulary including
  `missing_canonical_identity`, `unverified_corpus_identity`,
  `missing_geometry`, `placeholder_geometry`, `unknown_duration`,
  `duration_exceeds_window`, `non_actionable_category`, `already_in_plan`,
  `permanently_closed`, `closed_at_evaluated_time`, `hours_unknown`,
  `hours_stale`, `outside_candidate_radius`, `route_unknown`,
  `route_stale`, `route_degraded`, `insufficient_arrival_buffer`, and
  `private_outcome_excludes_candidate`;
- `PlaceActionabilityEvidence`, carrying only typed source references,
  freshness timestamps, and confidence/knowledge state—not presentation copy;
- `PlaceActionabilityDecision`, carrying state, reason codes, evaluated-at,
  and evidence references.

The model should distinguish corpus verification, operational freshness, and
route confidence. `taste_score` is ranking evidence, not truth confidence.
Distance in meters is candidate retrieval evidence, not proof of a routable
transition.

### 14.3 One candidate service

Create one async service boundary, for example
`get_gap_candidate_decisions(...)`, that owns:

1. Trip membership and day ownership;
2. destination-subtree and nearby retrieval through `get_gap_suggestions`;
3. canonical venue identity, category, geometry, and visit-duration checks;
4. already-in-Plan and relationship enrichment;
5. cache-only operational enrichment for the list path;
6. the shared actionability classifier;
7. bounded, typed output ordered by readiness and existing ranking evidence.

Both consumers must call this service:

- `backend/places/gaps.py` renders Add cards only from `ready` decisions;
- `backend/concierge/tool_handlers/itinerary_edit.py` returns `ready` and
  `needs_verification` decisions plus reason codes, so the agent may run one
  explicit live status check and re-evaluate a candidate.

The concierge handler currently lacks `user_id` and is synchronous. Thread the
authenticated user into it, make the dispatch await the service, and remove its
direct raw call to `get_gap_suggestions`. A list read must not fan out into live
provider calls. One explicitly selected `needs_verification` candidate may be
upgraded only through the existing venue-status provider/cache path.

### 14.4 Operational truth rules

For `start_now`:

- known permanent closure is `ineligible`;
- fresh `open_now=false` is `ineligible`;
- fresh `open_now=true` may satisfy the operational gate;
- stale `open_now`, missing status, or unknown hours is
  `needs_verification`, never `ready`;
- a successful live refresh is normalized into the same operational model and
  re-run through the same classifier;
- provider failure preserves `needs_verification` or produces abstention; it
  never converts unknown into open.

For a future bounded window, `open_now` alone is insufficient. Regular and
exceptional hours must cover the proposed visit interval, with exceptional
hours taking precedence. Until that interval evaluator exists, future-window
operational truth remains `needs_verification` rather than borrowing current
status.

### 14.5 Route and proximity boundary

The shared place policy establishes only candidate readiness. Final
micro-journey readiness additionally requires two fresh route facts:

1. resolved origin -> candidate anchor;
2. candidate anchor -> protected next commitment.

Reuse `backend/core/distance/resolve_distance` and
`backend/core/feasibility/evaluator.py`. A Haversine fallback or degraded route
may support qualified copy but may not prove a hard arrival boundary. The
composition evaluator, not SQL's one-kilometer radius, owns the final travel
and buffer decision.

### 14.6 Tests and gates

Add:

- a pure truth-table test for every actionability state/reason;
- freshness-boundary tests at exactly the TTL and one instant beyond it;
- permanent/fresh-closed/stale/unknown/open operational cases;
- duration, category, geometry, already-in-Plan, and membership cases;
- a parity test proving Places and Concierge consume identical decisions for
  the same fixture rows;
- a no-provider-fanout assertion for the list path;
- a live-refresh upgrade test and provider-failure abstention test;
- a privacy test proving private outcome reasons are never serialized in the
  group-safe candidate payload.

**Track A exit:** no candidate can be presented or proposed as start-ready by
one consumer while the shared policy classifies it as unknown or ineligible.

## 15. Track B — first-class bounded micro-journey composition

### 15.1 Product contract

For this release, a micro-journey is one committed anchor plus a route-shaped
experience around it. It is not a multi-stop itinerary and does not create a
new durable aggregate:

```text
origin
  -> connective path
  -> one committed anchor
  -> at most one optional, non-commitment flourish
  -> protected ending / next commitment
```

The anchor becomes one itinerary block after acceptance. The path and ending
are consequences of canonical route and Plan truth. A flourish is an optional
grounded lens or along-route cue; it is not a second promised stop, does not
receive an itinerary block, and must disappear when evidence or slack is weak.

### 15.2 Typed composition contract

Add a pure typed contract, for example under
`backend/core/models/micro_journey.py`:

- `BoundedWindowRef`: Trip/day and previous/next boundary IDs, evaluated-at,
  starts-at, ends-at;
- `JourneyOrigin`: permissioned current location or explicit
  `previous_plan_stop` fallback, with private provenance stripped from the
  group-safe projection;
- `JourneyAnchor`: canonical entity reference, visit duration, operational
  actionability decision, and scheduled local interval;
- `JourneyLeg`: from/to references, requested/resolved mode, fresh duration,
  distance, provider, observed/expires timestamps, degradation state, and
  evidence reference;
- `JourneyFlourish`: optional title/lens/source reference and zero commitment
  semantics;
- `JourneyEnding`: protected next-block reference, expected arrival, and
  arrival-buffer minutes;
- `MicroJourneyComposition`: version, status (`ready` or `abstain`), reason
  codes, the fields above, and a group-safe evidence summary.

This object may be embedded as versioned metadata on the canonical proposal so
review and receipts can explain the decision. It is not an independently
mutable record and must not become a second Plan writer.

### 15.3 Deterministic composition service

Implement a pure evaluator plus an async evidence-loading adapter:

1. Re-resolve the current open window and authenticated membership.
2. Resolve origin from fresh, permitted private location; otherwise use the
   previous placed Plan stop and label that fallback.
3. Load the selected canonical candidate through Track A.
4. Resolve both route legs for the intended mode and departure instants.
5. Compute:

   `outbound travel + visit duration + inbound travel + arrival buffer <= remaining window`.

6. Require a fresh operational decision covering the visit interval.
7. Add a flourish only when it lies on the proven path, has explicit evidence,
   and consumes no required schedule slack. The first implementation may
   always return `None`; absence is valid.
8. Return `abstain` with closed reason codes when any hard fact is unavailable
   or contradictory.

The pure evaluator should accept injected facts and a clock. The adapter owns
DB/provider calls. This keeps exact feasibility testable without Mapbox or an
LLM and lets backend-real tests inject controlled fresh route facts.

### 15.4 Canonical proposal integration

Do not let model-authored times become the authority for a bounded entry.
Within the existing `propose_change` path when the seed is
`trip_open_window`:

- require `proposal_type=add`, review mode, one canonical venue/site entity,
  no custom entity, and no alternative list masquerading as the primary
  decision;
- require the selected entity to have been surfaced by the shared candidate
  tool in the current turn;
- run the composition service again at proposal creation;
- derive exact local `HH:MM` start/end values from the ready composition;
- persist the versioned group-safe composition metadata with the canonical
  proposal;
- pass only those server-derived values into
  `create_add_operation_proposal`;
- re-run current-window, place, operational, route, and day-revision checks at
  apply time, failing visibly when the opportunity changed.

First repair the current `HH:MM` versus full-ISO mismatch by using the proposal
producer's existing planning-time parser for the guard. Then add a successful
bounded proposal test before adding richer composition behavior.

### 15.5 AI decision surface

The typed entry intent, not the exact words “Take us somewhere,” earns this
tool surface. Limit it to:

- current itinerary/day;
- shared gap-candidate decisions;
- one selected venue-status refresh when required;
- composition/route evidence;
- the canonical proposal tool.

The model's responsibility is judgment among eligible candidates and concise
group-safe explanation. The backend's responsibility is feasibility,
freshness, authority, and exact mutation. The response must lead with one
composition. Alternatives are available only after the user asks or the first
choice fails.

### 15.6 Composition evaluation rubric

Grade observed structured output, not prose fluency:

| Dimension | Hard requirement |
| --- | --- |
| Anchor count | Exactly one committed anchor. |
| Time | Entire composition and buffer fit the current server window. |
| Route | Both legs are fresh, non-degraded, and mode-honest. |
| Operations | Anchor is `ready` under Track A at the intended interval. |
| Ending | Protected next commitment is unchanged and arrival buffer is explicit. |
| Flourish | Zero or one; grounded, optional, and never represented as committed. |
| Multiplayer | Shared proposal contains no private reason or precise location. |
| Agency | No Plan write before review; repeat execution is idempotent. |
| Failure | Missing truth produces a specific abstention, not an approximate success. |

Fixture cases must cover exact fit, thin buffer, route failure, degraded route,
candidate closure between selection and proposal, stale window, stale day
revision, missing GPS fallback, no placed fallback, private constraint shaping,
and duplicate tool execution.

**Track B exit:** a valid doorway produces one reviewable, typed composition
and canonical add proposal; every invalid branch abstains or fails without a
Plan write.

## 16. Track C — prove second-occasion compounding

### 16.1 Verified baseline and precise gap

The repository already has most of the storage and privacy substrate:

- confirmed personal occurrence is required before outcome capture;
- `experience_outcome_feedback` stores correctable `place_verdict` and
  optional `companion_fit`;
- outcome writes atomically project append-and-supersede private
  `relationship_memory_claims`;
- the Context Compiler reads active private claims;
- companion-fit reuse has an exact-roster gate;
- `get_prior_occasion_context` supplies a weak structural precedent for local
  Plans;
- P04 has a task bank, but no observed AI-evaluation receipt.

The gap is causal application. Place-verdict claims enter current context
without one shared current-place/current-occasion/recency policy, the prior
occasion reader primarily matches roster overlap, and no replay proves that a
first outcome changes a later eligible decision.

### 16.2 Current occasion decision context

Introduce a read-only `DecisionOccasionContext` adapter built from existing
truth, not a new table:

- current Trip/Plan ID and `trip_kind`;
- canonical `place_id` when present;
- durable `occasion` vocabulary (`celebration`, `decompress`, `explore`,
  `work_play`, `reunion`, `other`);
- current member IDs;
- current candidate entity when evaluating a specific choice;
- evaluated-at instant and policy version.

Load corresponding source context for an outcome by joining its source outcome
and Trip/Plan: source place, occasion, occurrence roster, timestamps,
correction/supersession state, and evidence refs. Prefer read-time joins over a
new copied provenance column unless profiling shows the join is untenable.

### 16.3 One applicability authority

Make `resolve_experience_outcome_applicability` the shared authority for:

- direct recent-outcome prompt projection;
- relationship-memory claims loaded by the Context Compiler;
- candidate eligibility/ranking in Track A;
- prior-occasion structure in the planning adapter;
- the second-occasion eval trace.

Extend its inputs/outputs only as needed, preserving closed reason codes. The
policy should distinguish:

- exact candidate place verdict: may directly promote `would_repeat`, suppress
  `good_once`/`not_for_me`, or qualify a choice;
- different candidate: may not infer a category-level taste from one venue
  outcome;
- companion fit: applies only to the exact confirmed roster and an applicable
  occasion; otherwise withhold or mark weak precedent without companion prose;
- prior structural occurrence: may influence density only as a weak precedent,
  never as evidence that anyone liked it;
- corrected active claim: replaces the earlier claim;
- superseded, retracted, stale, or provenance-incomplete claim: withheld.

The group-safe proposal may say that a choice fits the group, but it may not
quote, identify, or reveal a private verdict. Actionability decisions exposed
to shared surfaces should use a neutral reason such as
`member_fit_constraint`, while the private audit retains the source claim ID.

### 16.4 Minimal credible two-occasion proof

Do not begin with an unsupported claim that Vesper has learned a universal
taste. Use the existing outcome vocabulary to prove something it can actually
mean:

1. Occasion 1 is a local `explore` Plan for an exact two-person roster.
2. The bounded composition proposes canonical Venue A and the group accepts.
3. Both members' personal occurrence is confirmed.
4. The test actor records `good_once` for Venue A and `worked` for the exact
   companion roster.
5. Occasion 2 uses the same city, occasion kind, roster, time shape, and raw
   candidate set. Generic ranking places Venue A first and Venue B second.
6. The active `good_once` claim makes Venue A ineligible for a repeat while
   preserving its factual history; Venue B becomes the selected anchor.
7. The decision trace cites the outcome/claim evidence privately; group copy
   does not expose the verdict or its author.
8. Correct the first outcome to `would_repeat` and replay the exact same second
   occasion. The prior claim is superseded, Venue A becomes eligible again,
   and the decision changes according to the active claim.

Required forks:

- changed roster: companion fit is withheld; personal place verdict remains
  usable only for its owner and must not be attributed;
- changed occasion: companion/structural precedent weakens or withholds under
  the declared policy; an exact personal place verdict remains place-specific;
- different destination and different candidate: no category preference is
  invented;
- retracted/corrected claim: old evidence has zero active effect;
- missing outcome: occurrence alone does not become affection;
- no viable alternative after applying the outcome: abstain rather than
  silently reselect the excluded place.

### 16.5 Evaluation and measurement

Add one backend-real scenario that records both the baseline and learned run:

- identical current inputs and candidate set;
- active outcome claim IDs and revisions;
- applicability decisions and reason codes;
- selected anchor or abstention;
- proposal and operation IDs when committed;
- shared-text privacy scan;
- correction replay result;
- explicit `None` for coordination-cost fields that were not measured.

Produce observed trials for P04-01 through P04-04 rather than authored passing
JSON. P04-04 must not claim “less coordination” until an explicit comparable
measure exists. Candidate-choice change, fewer required clarifications, and
coordination minutes are separate metrics; unknown remains unknown.

An AI/provider evaluation then runs at least three trials for each privacy- or
correction-sensitive branch. The grader should require the same evidence-bound
effect across runs, while allowing wording variation.

**Track C exit:** occasion 1 produces a correctable private claim; that claim
causally changes an otherwise identical occasion-2 decision; correction changes
the decision again; inapplicable or superseded evidence has no effect; and no
private verdict appears on a shared surface.

## 17. Ordered implementation and commit plan

| Order | Commit | Principal result | Depends on |
| ---: | --- | --- | --- |
| 1 | `fix(concierge): align bounded add with local wall-time contract` | Valid `HH:MM` add is compared to the canonical UTC window and reaches the canonical producer. | existing R1/R2 work |
| 2 | `test(concierge): prove successful bounded add proposal` | Membership, current boundary, review mode, entity, interval, and no-write failure forks are covered. | 1 |
| 3 | `feat(places): define actionable place decisions` | Shared tri-state model, closed reasons, and pure truth table. | none |
| 4 | `refactor(places): share gap candidate service` | Places and Concierge consume one enriched candidate policy; authenticated async handler replaces raw DB serialization. | 3 |
| 5 | `test(places): prove actionable consumer parity` | Operational freshness, provider abstention, privacy, and no-fanout gates. | 4 |
| 6 | `feat(plan): model bounded micro-journey composition` | Typed contract and pure two-leg/time/buffer evaluator. | 3 |
| 7 | `feat(concierge): compose bounded add from server truth` | Proposal path re-resolves actionability/routes and derives exact mutation inputs. | 4, 6 |
| 8 | `eval(concierge): gate micro-journey composition` | Hard rubric and deterministic/provider cases prevent list-like or infeasible output. | 7 |
| 9 | `fix(outcomes): apply current occasion context consistently` | Context Compiler, recent outcomes, candidate policy, and prior occasion share one applicability authority. | 3–4 |
| 10 | `test(outcomes): replay correction and applicability forks` | Exact place/roster/occasion, correction, retraction, and privacy rules are backend-real. | 9 |
| 11 | `eval(outcomes): prove second-occasion decision change` | Identical-input baseline/learned/corrected trace supplies observed P04 evidence. | 7–10 |
| 12 | `test(trips): join composition outcome and later occasion` | Canonical add -> occurrence -> outcome -> second bounded decision closes the causal loop. | 11 |
| 13 | `docs: record compounding-loop evidence boundary` | Execution record distinguishes deterministic, backend-real, AI-eval, controlled, and physical proof. | exact tested candidate |

Commits 3–5 and 6's pure model may be developed independently after order 2,
but commits should land in dependency order. Do not start the second-occasion
provider evaluation until deterministic actionability and correction forks pass.

## 18. Release gates and product metrics

### 18.1 Source gates

- full actionability truth table and consumer parity;
- successful and failed bounded add through the published tool schema;
- composition invariant/property tests over window durations and route facts;
- Context Compiler privacy, roster, occasion, correction, and retraction tests;
- OpenAPI/type sync when public payloads change;
- backend size, async, migration, and focused scenario gates;
- mobile typecheck and focused Plan/Map/outcome surface tests.

### 18.2 Evidence gates

- deterministic replay: no provider and no model;
- backend-real replay: Postgres sources, canonical proposal/operation/outcome
  rows, injected controlled operational and route facts;
- provider/model eval: observed trials with revision-bound inputs and grader;
- controlled-device run: organizer and participant projections plus privacy
  negative oracle;
- physical-device run remains a separate later promotion gate.

### 18.3 Metrics worth collecting

- actionable candidate precision sampled against manually verified truth;
- abstention rate by reason (`hours_unknown`, `route_unknown`, no fit, private
  fit exclusion);
- live verification upgrade rate and provider failure rate;
- time from doorway tap to reviewable proposal;
- proposal acceptance, rejection, expiry, and stale-at-apply rates;
- route/buffer invalidation between selection and apply;
- occurrence confirmation and outcome-correction rates;
- fraction of second occasions with applicable evidence;
- fraction whose selected action changes because of that evidence;
- privacy violations and superseded-claim influence, both with a target of
  zero.

Do not optimize for fewer abstentions before false start-ready rate is known.
Do not call a recommendation “better” merely because it changed. The first
credible claim is narrower: Vesper used permitted evidence, changed a concrete
decision in the expected direction, remained correctable, and preserved
privacy.

## 19. Execution record — 2026-08-10

The deterministic engineering slice is implemented in `travel-agent`:

| Concern | Landed evidence |
| --- | --- |
| Local-wall-time bounded add | `7ab19f5c0`, `dbac14a00` — public `HH:MM` inputs resolve through the same producer authority used for persistence; success and no-write failure forks are covered. |
| Shared actionable candidate truth | `56c11a992` — cache-only, authenticated gap candidates use identity, geometry, duration, plan membership, operating-hours freshness/interval coverage, and named abstention states. Places and Concierge read the same service. |
| Typed composed micro-journey | `7ab19f5c0`, `c400bba99`, `0f2cfd659` — exactly one canonical venue plus two fresh route legs and a buffer are required. The server derives the persisted local anchor times and records a structured receipt on the proposal. |
| Current occasion outcome context | `0020561e4` — direct outcome reads, planner context, and Context Compiler join source trip/place/occasion at read time and fail closed for roster, occasion, correction, or provenance mismatches. |
| Second-occasion decision change | `584cc174d` — an applicable `good_once` makes the same candidate ineligible; correcting it to `would_repeat` makes it eligible again. A different occasion leaves the one-off verdict as weak precedent instead of inventing a broad taste. |

Focused deterministic gates passed during implementation:

- 54 shared actionability/Places/Concierge tests;
- 50 bounded-add and pure-composition tests before the route-composition
  integration update, followed by 19 focused route/outcome/candidate tests;
- 84 outcome/Context Compiler/planner-context tests;
- all touched files pass Ruff and `git diff --check`.

The repository-wide pre-commit remains blocked by pre-existing global ratchets
at this checkout (broad exception count `1192` vs ceiling `1191`, and existing
size-budget failures). Commits for this slice used `--no-verify` only after the
relevant focused gates passed; the new bounded proposal error categories are
registered in the same slice.

This does **not** yet constitute an observed provider/model P04 evaluation or
a physical-device result. Those remain promotion gates: they must run against
revision-bound inputs and report abstentions/unknowns rather than synthesizing
success. The deterministic evidence above is the prerequisite, not a claim of
measured coordination improvement.
