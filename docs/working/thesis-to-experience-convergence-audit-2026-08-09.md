---
doc_type: working
status: active
owner: founder / engineering
created: 2026-08-09
expires: 2026-09-08
why_new: Pressure-tests the accepted product direction against current backend, mobile, release, journey, and seven-day Git evidence, then records the cross-system seams that prevent the substrate from reading as one experienced product.
---

# Thesis-to-experience convergence audit

## Executive verdict

The direction is optimal **under the current architecture, product wedge, and
proof constraints**, with one important correction:

> Vesper should converge around one bounded serving and decision lifecycle, not
> one universal data model, Plan table, memory store, event log, or agent.

The last seven days did not produce a random collection of features. They built
real parts of the same system:

- place identity, provenance, freshness, geometry, route facts, and World
  Foundry capability gates;
- saves as weak, provenance-bearing attention rather than declared intent;
- local Plans, occurrence, private outcomes, companion fit, and prior-occasion
  reuse;
- social circles, confirmation, revocation, explicit sharing, relationship
  claims, and trip links;
- weather rescue, nearby saved-place opportunities, attention arbitration, and
  shadow ambient cycles;
- a canonical trip clock, typed stop identity, route freshness, map projections,
  and Mapbox-backed enrichment;
- `ExperienceScope`, `RelationshipScope`, AI-run identity, Context Compiler,
  Situation, action receipts, and domain outcome ledgers.

That is unusually strong substrate convergence. The product can represent much
more of the thesis than a user can currently experience.

The experienced product is weaker because those parts do not yet meet at one
reliable decision boundary. Context is assembled several ways; relationship
scope is defined but is not populated at the live AI entry point; Situation and
TripWorldModel remain separate; proactive producers stop before delivery;
several substantial mobile surfaces are internal and default-dark; and outcome
evidence reaches future planning through multiple parallel, only partially
applicable paths. The release proof reinforces this conclusion: 27 of 28 seeded
journeys pass, but J08—the live Plan/map/Now coherence journey—fails, while
ambient, voice, live booking, and agent-initiated disruption remain deliberately
out of v1.

The highest-leverage move is therefore not another feature family. It is to
make two bounded loops feel whole:

1. **Group Trip judgment loop:** current Plan + people + place truth + route /
   time / weather → one explainable proposal → group decision → coherent
   Plan/map/Now update → outcome.
2. **Local second-occasion loop:** save or place interest + relationship and
   moment context → one local Plan → lived occurrence → lightweight outcome →
   visibly better next occasion.

Everything else should either help those proofs, stay in shadow, or wait.

## What this document is—and is not

This is a dated working audit. It does not replace:

- the product canon in `travel-agent/docs/product/`;
- the accepted
  [experience, context, and relationship kernel](../decisions/2026-08-09-experience-context-and-relationship-kernel.md);
- the [v1 release contract](../release/v1-scope.md);
- [Current State](../status/current-state.md) or
  [Journey Status](../journeys/STATUS.md);
- backend system or architecture contracts.

It answers four narrower questions:

1. Does current code support the recent thesis direction?
2. Where do independently useful systems fail to become one product judgment?
3. Which parallel systems are intentional domain boundaries, and which are
   unfinished migrations or duplicate policy?
4. What should be implemented next—and what should explicitly not be built?

## Audit method and evidence boundary

The audit read both child repositories at their consolidated `main` heads on
2026-08-09:

| Repository | Audited head | Worktree state at start |
| --- | --- | --- |
| `travel-agent` | `db9e02149` | clean; synchronized with `origin/main` |
| `travel-app` | `f7549bd7` | clean; synchronized with `origin/main` |

It traced production call sites and release evidence across:

- the product Thesis, Product Model, Strategic Implications, and accepted kernel;
- AI run creation, turn loading, Context Compiler, TripWorldModel, Situation,
  group synthesis, and planning context assembly;
- saves, place opportunities, ambient dispatch, weather rescue, notification
  arbitration, and outcome models;
- local Plans, occurrence artifacts, prior occasions, relationship outcomes,
  social circles, and relationship memory;
- map state, route facts, canonical clocks, location consent, spatial situation,
  and mobile Plan/map surfaces;
- World Foundry validation, capability audit, promotion planning, and persistence;
- feature registry, v1 scope, current state, canonical journeys, and seven-day
  authored Git history.

“Implemented” below means a real code path or contract exists. It does **not**
mean production-enabled or device-certified. Commit volume is treated as
supporting evidence, not progress by itself; merge commits, duplicate patch
lineage, generated contracts, formatting, staging data, and consolidation work
inflate raw commit counts.

## 1. Optimality pressure test

### 1.1 The accepted direction is the right one

The accepted kernel has the correct architectural center:

```text
domain evidence and durable truth
        ↓
ExperienceScope + RelationshipScope + audience + task
        ↓
Context Compiler (what may matter) + Situation (what matters now)
        ↓
bounded judgment / proposal / action
        ↓
domain command and durable outbox
        ↓
surface projections + action receipt
        ↓
domain outcome and later applicability evaluation
```

This matches the product thesis better than a chatbot-centric architecture. It
allows the same durable understanding to shape chat, Home, Places, Plan, map,
and proactive surfaces without pretending those surfaces or their authorities
are interchangeable.

It is also the smallest architecture that can reconcile the two central product
stories:

- **Yungang / many lenses:** place truth and interpretation are selected for a
  person, relationship, purpose, and moment.
- **Local best friend:** practical judgment combines place truth with timing,
  route, weather, group fit, and lived local calibration.

Neither story is satisfied by a larger corpus alone. Both require contextually
applicable judgment, explainable evidence, and a loop that learns from what
happened.

### 1.2 The tempting alternatives are worse

| Alternative | Why it is tempting | Why it is wrong now |
| --- | --- | --- |
| Universal `Plan` table replacing Trips | Local nights, travel, and ambient opportunities all look plan-like. | The existing Trip aggregate already provides committed planning, itinerary operations, attendance, roles, proposals, and sync. Replacing it would duplicate mature authority before product proof. `ExperienceScope` supplies polymorphism without another aggregate. |
| One universal context / world-model object | Consumers currently assemble overlapping context. | A giant object would mix privacy, audience, freshness, and task authority. The correct unification is a compiler contract with purpose-bound projections, not one eagerly materialized mega-read-model. |
| One universal memory or outcome table | Saves, notifications, occurrence, place verdicts, itinerary edits, and card actions all generate learning. | They have different truth conditions and correction semantics. A notification dismissal is not a place dislike; attendance is not delight; circle membership is not shared taste. Keep domain evidence separate and standardize causal joins and evaluator vocabulary. |
| Make circles the multiplayer truth | Circles look like the durable social object. | Membership proves consented relationship topology, not attendance, availability, preference, or authority over a Plan. Those remain separate. |
| Require richer save forms | Explicit notes and intentions look easy to reason over. | The user’s desired low-friction behavior is already reflected in `SaveOriginContext`: save is weak attention with provenance. Intent should be a revisable hypothesis assembled from surrounding evidence, not required schema homework. |
| Enable ambient to demonstrate integration | The shadow producers already exist. | Delivery before precision, receipt, outcome, and device proof would create interruption risk and obscure whether the underlying judgment is useful. Earn proactivity after a passive/in-product proof. |
| Build a new “Vesper graph” database now | The thesis names Person, Relationship, Place, Plan, Moment, and Outcome. | These are product concepts, not a mandate for one physical graph. Existing relational authorities plus typed scopes, revisions, and projections already provide safer composability. |

### 1.3 The correction to the current direction

The accepted decision says “migrate context consumers,” but the implementation
program needs a sharper product unit of work. A context migration can be
technically successful while users notice nothing. Every migration phase should
be attached to an experienced decision:

- which user-visible judgment changes;
- which prior evidence now affects it;
- what receipt proves the influence without leaking private context;
- what outcome can confirm, contradict, or leave it unknown;
- what exact old path becomes removable after parity.

The convergence program should therefore be managed as **decision-loop
completion**, not shared-infrastructure completion.

## 2. Thesis obligation matrix

| Thesis primitive | Strong substrate already present | Experienced expression today | Principal gap |
| --- | --- | --- | --- |
| **Person** | Personal Memory, observations, save origin, place affinity, occurrence, private outcomes, corrections. | Planning and chat can use portions; Atlas/Places show some residue. | Evidence enters through different loaders and is not consistently tied to a visible decision or current applicability. |
| **Relationship** | Trip roster, attendance, social circles, invitation confirmation, revocation, relationship claims, explicit circle sharing, companion-specific affinity. | Circle creation/detail/invites/memory sharing exist; group Trips are mature. | `RelationshipScope` is not populated on the live AI run; circle context is dark; repeated-group knowledge does not reliably change the experienced plan. |
| **Place** | Canonical identity, external mappings, projections, provenance, freshness, geometry, briefs/dossiers/angles, World Foundry gates. | Places, Atlas, Discover, search, saves, map, and planning consume different parts. | Corpus capability is sparse; editorial Foundry promotion/runtime indexing is incomplete; a place’s many lenses and practical truth do not yet meet in one decision. |
| **Plan** | Trip aggregate, local `trip_kind`, operation ledger, proposal/vote/revert, attendance, map state. | Group travel is the strongest product loop; local Plan UI is substantial in internal builds. | Local activation is one hard-coded Friday-night door; local and ambient openings do not yet graduate naturally from saves, people, and moments. |
| **Moment** | Canonical trip clock, location freshness/precision/consent, route facts, weather observations, Situation, attention arbitration. | Plan/map/Now and leave-by logic expose pieces. | Several clocks/situations remain; J08 fails; proactive moment selection ends in shadow rather than a user-visible opening. |
| **Outcome** | Occurrence, one-tap place and companion verdicts, relationship claims, prior occasion, notification outcomes, action receipts, policy outcomes. | Local outcome artifact and companion fit exist behind internal gates; planner reads some cross-trip evidence. | No single applicability decision says what prior outcome matters to this person/group/place/occasion; outcome vocabularies and causal joins are fragmented. |

The matrix supports the core conclusion: the substrate is not missing a thesis
primitive. The experienced product is missing the connective decisions among
them.

## 3. End-to-end loop traces and stop lines

### 3.1 Group Trip disruption loop

```text
current weather + place geometry + future itinerary block
  → deterministic weather-rescue match
  → nearby verified covered/indoor alternative
  → canonical replace proposal draft
  → attention candidate
  ── STOP: default-dark; no certified mobile weather-rescue composition ──
  → group sees reasons and trade-off
  → vote / organizer resolution
  → Plan + map + Now converge
  → occurrence and group-safe outcome
```

What exists:

- fail-closed current-weather provider and place provenance;
- shared weather matcher;
- bounded group-safe proposal production;
- canonical proposal rather than direct itinerary mutation;
- attention candidate registration.

What does not yet exist as a certified unit:

- a mobile treatment that makes the proposal legible without overclaiming;
- two-observer device evidence;
- explicit proof that accepted/rejected proposal state, Plan, map, Home, and
  current-condition copy converge after the decision;
- downstream outcome attribution showing whether the rescue helped.

This is the best near-term group-Trip proof because it forces weather, place,
spatial proximity, time, Plan authority, multiplayer, and receipts into one
experienced judgment.

### 3.2 Saved place to local opening

```text
save + SaveOriginContext + weak affinity
  → location freshness / precision / consent
  → exact place geometry + fresh open-now evidence
  → saved-place opportunity
  → ambient-cycle candidate and relevance judgment
  ── STOP: no public opportunity API/surface; default judge rejects; no delivery ──
  → passive in-product opening
  → invite one person / shape local Plan
  → occurrence → place + companion outcome
```

What exists:

- canonical save identity and reversible save behavior;
- bounded `SaveOriginContext` that intentionally does not claim explicit intent;
- save as weak affinity (`0.25`), below the liked threshold;
- saved-nearby producer with strict foreground-location, accuracy, geometry,
  open-now, expiry, and dedup gates;
- `PlaceOpportunity` states and aggregate acceptance metrics.

The stop line is severe: `PlaceOpportunity` has no normal app consumer, its
ambient host intentionally sends no push/message, and the cycle rejects every
candidate when no relevance judge is injected. The code currently proves that
the system can identify a cautious opportunity, not that the opportunity helps
a person act.

The first product step should be passive and reversible: render one opportunity
inside an already-open Places or Trips surface, with “why now,” “not now,” and
“shape a plan.” Notification should come later.

### 3.3 Local Plan to second occasion

```text
Trips Home hard-coded “Friday night” door or chat-local ratchet
  → Trip aggregate with trip_kind=local
  → two-moment local itinerary
  → invite / RSVP / chat / optional voice
  → confirmed per-person occurrence
  → optional outcome artifact + place verdict + companion fit
  → relationship-memory claims
  → prior occasion and cross-trip planning enrichment
  ── STOP: internal gates + fragmented applicability on the next occasion ──
  → visibly better second Plan
```

This loop is much more implemented than a surface-level read suggests:

- local Plan creation uses the canonical Trip and planning path;
- local Plan presentation branches away from travel-specific rail, map, and
  booking machinery;
- the screen supports Plan reading, moments, prior-occasion receipt, chat,
  optional voice, and an optional outcome artifact;
- per-person outcomes require confirmed occurrence and atomically produce
  relationship-memory claims;
- the planner reads loved places, companion-specific place affinity, explicit
  recent outcomes, and a structural prior-occasion packet.

The experienced loop is still not complete:

- `LOCAL_PLAN_DOGFOOD_ENABLED` is internal and false by default;
- `OUTCOME_ARTIFACT_ENABLED` is doubly gated and false by default;
- the only explicit doorway is a fixed “Friday night” seed rather than an
  opportunity derived from a saved place, conversation, person, or moment;
- voice is separately dark;
- the next-occasion path combines three related but distinct inputs without one
  applicability resolver:
  - structural prior occasion: roster overlap and happened/planned counts;
  - recent explicit outcomes: loaded by person, not filtered to the current
    companion roster;
  - companion-specific place affinity and relationship-memory claims.

The data model correctly preserves the exact companion roster with a
`companion_fit` outcome. But `get_recent_experience_outcomes()` omits that scope
from its private summary, and the formatter can say “worked with those
companions” without establishing that “those companions” match the present
Plan. The next implementation should be an applicability resolver, not another
outcome store.

### 3.4 Circle to better decision

```text
explicit circle creation + invited member
  → confirmation / decline / leave / archive
  → optional trip link
  → explicit shared relationship claim
  → Context Compiler projection
  ── STOP: circle agent context dark; RelationshipScope absent at AI entry ──
  → planner / proactive judgment changes for this relationship
  → safe action receipt
  → per-person and shared outcomes update future applicability
```

The topology and consent substrate are real. The app supports Your People,
circle detail, invitations, event replay, revocation, trip linking, and explicit
memory sharing. The backend correctly prevents membership from silently
becoming attendance or relationship memory.

But the relationship does not yet exert commensurate product force:

- `SOCIAL_CIRCLE_AGENT_CONTEXT_ENABLED` is false by default;
- `AIRunContext.relationship_scope` exists, but the live chat entry creates the
  run without it;
- the only production `create_ai_run_context()` call is the message-flow entry;
- there are no production child AI-run callers;
- Context Compiler reads relationship claims, while other group and situation
  paths continue to assemble context separately.

The circle is therefore more visible as a settings/social object than as a
reason Vesper makes a distinct judgment.

### 3.5 World Foundry to experienced place intelligence

```text
live sources
  → immutable observations and candidate claims
  → independent review
  → accepted facts / judgments / evidence-linked editorial
  → deterministic promotion plan
  → transactional accepted-evidence persistence + projection rebuild
  → indexing and runtime retrieval
  → capability-specific product certification
  ── STOP: sparse capability coverage; editorial/runtime/certification seams ──
  → person/relationship/moment-specific place judgment
```

The control-plane direction is excellent. It treats identity, geometry,
availability, narration, proactivity, and multiplayer as separate capabilities
rather than giving an entity a misleading global “verified” badge. It also
keeps Postgres canonical and vector indexes derived.

The current Lisbon report is appropriately honest:

- pilot gate: **NOT READY**;
- identity: 17/30;
- spatial: 6/30;
- catalog: 12/30;
- planning: 3/30;
- narration: 13/30;
- proactive: 0/30;
- multiplayer: 2/30;
- geometry missing for 24/30; price and accessibility missing for all 30.

The report explicitly says runtime retrieval, routing, notification, and
multiplayer require separate certification. That is the right invariant.

There is also a current documentation/code seam: the canonical operations doc
still says promotion is dry-run-only and that no transactional writer exists,
while `backend/world_foundry/persist.py` now implements accepted observation,
identity, claim, judgment, and projection persistence. There is still no exposed
operator apply command, and editorial drafts remain intentionally excluded from
that persistence package. The contract should be updated to distinguish
“transactional persistence library exists” from “operator apply, editorial
promotion, indexing, and product certification are available.”

## 4. Parallel-system inventory

Not all parallelism is waste. The table classifies each overlap before proposing
consolidation.

| Concern | Current paths | Classification | Required convergence |
| --- | --- | --- | --- |
| Context selection | Context Compiler; TripWorldModel; `turn_loader`; planning `_assemble_planning_context`; preference retriever/group synthesizer | **Migration seam** | Context Compiler owns evidence admission, privacy, provenance, and revision. Legacy paths become adapters until parity and cutover. |
| Current relevance | `TripSituation`; prompt-specific `SpatialSituation`; TripWorldModel moment fields; Home/proactive posture | **Migration seam** | One typed Situation envelope with Experience/Relationship scopes and specialized payloads; surface projection remains separate. |
| Group truth | Trip roster, attendance, circle membership, shared group memory, relationship claims | **Intentional separation** | Join through explicit `RelationshipScope` and purpose; never merge the stores or infer one concept from another. |
| Place truth/content | Place projection, briefs, dossiers, angles, Foundry proposals/reviews, vector index | **Intentional layers with incomplete promotion** | One identity/provenance spine and capability certification; complete editorial promotion/index parity rather than flattening content. |
| Route/time | Route-fact cache, distance resolver, map enrichment, itinerary feasibility, leave-by, canonical trip clock, remaining Home/proactive clocks | **Partly converged, residual policy drift** | Route facts and destination-local time must be the shared evidence; each consumer can render differently. Finish multi-trip destination-time handling. |
| Attention | Ambient cycle, proactive arbiter, Home cards, notification state/outcomes, place opportunities | **Migration seam** | One candidate/attention admission contract and causal receipt; Home, in-app, and push remain separate channels. |
| Outcomes | Occurrence, experience outcomes, relationship claims, policy outcomes, notification outcomes, opportunity status, card lifecycle | **Intentional evidence domains; missing evaluator vocabulary** | Preserve domain ledgers; standardize exposure, decision, action depth, achieved/unknown, correction, and correlation semantics. |
| Receipts | Vesper action receipts, memory applications, notification decisions/outcomes, proactive events, work receipts | **Useful specialized receipts; weak cross-loop join** | Reuse AI run/workflow/correlation identities and a small common decision envelope. Do not replace specialized payloads. |
| Product gates | Workspace registry, backend feature helpers, app compile-time flags | **Governance defect** | Canonical registry and guard must cover both repos and all supported flag conventions. |

### 4.1 The highest-cost context duplication

Today, a planning or chat judgment may draw from:

- `turn_loader`, which manually loads social state, preferences, group context,
  location, spatial situation, outcomes, and `ExperienceScope`;
- `SituationBuilder`, which composes plan state, voice, group profile, signals,
  modality, delivery, and nearby state into `TripSituation`;
- `spatial_situation`, which builds another prompt-oriented view;
- planning `_plan.py`, which constructs personas, trip metadata, itinerary,
  observations, location, weather, cross-trip data, explicit outcomes, loved
  places, companion affinity, prior occasion, and optionally Context Compiler;
- Context Compiler, which loads an authorized repeatable-read snapshot and
  produces purpose/audience-bound bundles;
- TripWorldModel, read by Home, user map, trip reading, turn context, and
  proactive producers.

Only planner code currently selects Context Compiler output, and even there it
does so only behind parity/cutover flags and a trip allowlist. Missing internal
credentials fail back to the legacy overlay. This is the right rollout posture
but an incomplete migration.

The inefficiency is not just duplicate queries. It is duplicated policy:

- different source sets;
- different freshness and fallback behavior;
- different privacy projections;
- different clocks and notions of “current”;
- different evidence wording;
- different instrumentation and invalidation.

The fix is not to make one synchronous loader fetch everything. Keep source
adapters parallel and bounded; make the **admission, purpose, audience,
dependency fingerprint, and selected projection** canonical.

### 4.2 The shared kernel is present but not live

The accepted contracts exist, but their call graph shows they are still
scaffolding:

- `ExperienceScope` is resolved in the turn loader.
- `RelationshipScope` exists and can emit content-free trace metadata.
- `AIRunContext` can carry relationship, occasion, workflow, parent, entry
  handoff, and surface identities.
- the live message flow creates an AI run but does not pass
  `relationship_scope`;
- no production caller creates a child AI run;
- `TripSituation` does not contain `ExperienceScope` or `RelationshipScope`;
- action receipts can carry `ai_run_id` and `correlation_id`, but this does not
  yet form a universal causal chain across all loops.

The next slice should populate and propagate the contracts without changing
behavior, then compare receipts and projections before using them for product
decisions.

## 5. Engineering inefficiencies and seams

### P0 — Release truth contradicts the central experienced loop

J08 fails because the live plan and map cannot identify an in-progress block at
the pinned current time. The v1 contract calls Trip Home, living itinerary,
map, and Now release-critical. This is not a peripheral test failure: it is the
product thesis’s claim that Vesper understands what is happening now.

**Action:** fix or correct the J08 fixture/clock truth, then run the current
revision replay and device lane before claiming map/time convergence.

### P0 — New mobile gates are absent from the canonical flag registry

The app defines:

- `LOCAL_PLAN_DOGFOOD_ENABLED`;
- `TRIP_EDITORIAL_MAP_ENABLED`;
- `OUTCOME_ARTIFACT_ENABLED`.

All are false by default and correctly scoped to internal evidence. None has a
row in `docs/flags/registry.yaml`. `scripts/check_flag_registry.py` still passes
because its unregistered-flag scanner only reads `travel-agent/backend` calls to
`truthy_env`, `falsy_env`, or `_truthy`; it does not inspect mobile exported
booleans or `EXPO_PUBLIC_*` reads. Current State therefore reports 59 registered
flags while omitting these release-relevant gates.

**Action:** register the three flags and extend the guard with an explicit
mobile convention. Avoid a naive every-environment-variable scan; define a
supported helper or exported-constant pattern for app flags.

### P1 — Scope and execution identity stop at the entry seam

AI-run identity is only created for the chat message flow. Relationship scope
is not attached. Home composition, place grounding, ambient judgment, planning
generation, voice, and outcome reconciliation are enumerated operations but do
not consistently create or inherit runs.

**Cost:** cross-surface attribution is weaker than the architecture implies;
one cannot reliably ask which relationship- and place-aware evidence changed
which decision across entry surfaces.

**Action:** create a no-behavior-change execution envelope at each AI boundary,
inherit bounded child runs where appropriate, and thread the same correlation
into action receipts and outcome evaluators.

### P1 — Outcome applicability is weaker than outcome capture

Capture is careful: outcomes are per person, require confirmed occurrence, are
correctable, preserve place and companion verdict separately, and record the
exact confirmed roster. Reuse is less precise:

- recent explicit outcome summaries drop companion scope;
- prior occasion carries only structural overlap and counts;
- companion place affinity performs its own roster-aware selection;
- Context Compiler reads relationship claims through another projection.

**Cost:** the system may possess the right evidence while expressing it too
generically or applying it through several unrelated prompt sections.

**Action:** add a pure, inspectable applicability resolver:

```text
candidate prior evidence
  × current ExperienceScope
  × current RelationshipScope / actual roster
  × place / destination / occasion relevance
  × recency and correction state
  → apply | withhold | apply-as-weak-precedent + reason codes
```

It should produce evidence references for Context Compiler, not another stored
profile.

### P1 — Proactive candidate production stops before product value

`run_ambient_cycle()` intentionally sends no notification. Without an injected
judge it rejects all candidates. Place opportunities are internal; weather
rescue is dark; broad ambient is out of v1.

That conservative posture is correct. The inefficiency is maintaining several
producers without one passive surface and outcome ladder that can prove their
judgments before push.

**Action:** add one in-app opportunity projection with a shared candidate
receipt and explicit lifecycle. Compare it against “no intervention” before
building delivery.

### P1 — World Foundry’s control plane and runtime are only partially joined

The reviewed evidence system is stronger than its runtime product proof:

- capability data is sparse;
- editorial drafts are not persisted by the Foundry package;
- vector sync and parity remain separate;
- operator docs lag the newly landed persistence library;
- runtime retrieval/routing/notification/multiplayer certifications remain
  separate by design but have not been completed.

**Action:** choose a small thesis-anchor set, finish capability predicates and
editorial promotion, synchronize the derived index, then certify retrieval in
the two target decision loops. Do not optimize for total entity count.

### P1 — Substantial hidden surfaces create maintenance without learning

The mobile client contains meaningful local Plan, outcome artifact, editorial
map, voice, circle, and ambient treatments, but several are internal or dark.
Dark code is sometimes the correct rollout state; the problem is an indefinite
state where it continues to evolve without producing device evidence or a
retirement decision.

**Action:** every active dark flag needs a dated promotion or removal question,
an owner, a target journey, and evidence gathered. The new local/map/outcome
flags currently lack even registry lifecycle metadata.

### P2 — Multi-trip clocks still have a destination-time seam

The prior parallel-implementations audit closed most trip-phase contradictions
and correctly rejected several false positives. It still defers user-scoped
Home/proactive readers that rank trips in potentially different destination
timezones using one host-local `today`.

**Cost:** an everyday/home decision can be off by a day at exactly the boundary
where moment relevance matters.

**Action:** pass a per-trip canonical clock into ranking, producer, and posture
evaluation rather than replacing one global date default with another.

### P2 — Commit topology obscures effective progress

Seven-day reachable history is extremely large and contains merge commits,
duplicate patches from parallel branches/consolidation, generated schemas,
formatting, and seed artifacts alongside product work. The consolidation itself
was valuable, but raw commit counts cannot answer how much new user capability
landed.

**Action:** report weekly progress by stable patch identity and experienced
loop, with separate categories for product behavior, substrate, data/corpus,
tests/evidence, generated artifacts, refactor, and docs. Treat merge commits as
integration events, not additional implementation.

### P2 — API breadth increases the cost of partial integration

The current contract contains 467 paths, 520 operations, and 1,039 schemas.
Large surface area is not inherently wrong, but it makes “implemented” a weak
signal and increases projection, mobile-mapper, mock, flag, and journey upkeep.

**Action:** every new endpoint in the convergence program must name its live
consumer, target journey, authority, dark/release posture, receipt, and eventual
retirement of any superseded path. Prefer projections through existing surface
contracts when semantics already fit.

## 6. Obvious missing implementations

These are the smallest missing pieces with disproportionate product leverage.
They are ordered by dependency, not excitement.

| ID | Missing implementation | Why it is obvious now | Completion evidence |
| --- | --- | --- | --- |
| C1 | Resolve and attach `RelationshipScope` at every AI entry | Contract exists; live call omits it. | Private/group/circle/trip-roster trace tests; no raw IDs in unsafe telemetry; relationship-specific eval fixture. |
| C2 | Put Experience/Relationship scopes into typed Situation | Accepted decision requires it; current `TripSituation` lacks both. | Same moment compiles consistently for chat/Home/Plan with audience differences only where intended. |
| C3 | Create one causal decision envelope | AI runs, action receipts, proactive events, memory applications, and outcomes have join fields but no enforced loop. | One trace can follow evidence → judgment → proposal/action → surface → response/outcome without prompt content. |
| C4 | Finish planner Context Compiler parity and bounded cutover | It is the only current consumer and remains dual-path. | Source coverage, privacy, latency, itinerary-quality parity, allowlisted canary, rollback, legacy-read deletion ledger. |
| C5 | Implement current-context outcome applicability | Companion scope is captured but dropped from recent summaries; prior occasion is structural only. | Second-occasion eval demonstrates correct apply/withhold for changed roster, destination, and corrected outcome. |
| C6 | Expose one passive place opportunity | Producer and state model exist; no user value path. | Saved place → in-app opportunity → dismiss/shape Plan → receipt, with no push. |
| C7 | Complete weather-rescue mobile proposal composition | It joins the most thesis systems in one bounded Trip use case. | Two-device proposal/vote/apply/revert; Plan/map/Now agreement; grounded freshness/provenance. |
| C8 | Generalize local Plan activation | Current doorway is a hard-coded Friday-night prompt. | Create local Plan from save, place detail, conversation, or person with the originating evidence preserved. |
| C9 | Finish Foundry editorial promotion and index certification | Accepted editorials are selected but Foundry persistence excludes them; product capabilities remain sparse. | Reviewed editorial reaches canonical store and derived index; retrieval receipt proves identity/hash parity. |
| C10 | Repair J08 and certify map/time truth | Central release journey is blocked. | Current-revision seeded replay plus device proof for live block, next stop, route freshness, and timezone. |
| C11 | Extend flag governance to mobile | Three consequential gates are invisible to registry/current state. | Registry rows, two-repo static guard, generated current state includes them. |
| C12 | Add a second-occasion product evaluator | The thesis claims compounding; current tests largely prove transport/contracts. | Blind comparison shows prior evidence improves specificity/fit without inappropriate repetition or privacy leakage. |

## 7. Recommended target architecture

The target is a small shared kernel around existing authorities:

```text
┌──────────────────────────────── durable domain authorities ────────────────────────────────┐
│ Person evidence │ Relationship topology/claims │ Place truth │ Trip/Plan │ Moment evidence │
└───────────┬──────────────────────┬────────────────┬──────────────┬─────────────────────────┘
            │                      │                │              │
            └──────────── source adapters with revisions, provenance, freshness ────────────┐
                                                                                              │
                     ┌────────────── ServingRequest ──────────────┐                          │
                     │ ExperienceScope                            │                          │
                     │ RelationshipScope                          │                          │
                     │ actor / audience / purpose / surface / task│                          │
                     └───────────────┬────────────────────────────┘                          │
                                     │                                                       │
                   ┌─────────────────┴───────────────────┐                                   │
                   │                                     │                                   │
          Context Compiler                         Situation Compiler                         │
     what is admissible/relevant                what is current/urgent                        │
                   │                                     │                                   │
                   └─────────────────┬───────────────────┘                                   │
                                     ↓                                                       │
                         bounded judgment / proposal                                          │
                  reason codes + evidence refs + uncertainty                                  │
                                     ↓                                                       │
                     canonical domain command / outbox                                        │
                                     ↓                                                       │
              channel projections: chat │ Plan │ map │ Home │ Places │ push                  │
                                     ↓                                                       │
                     domain outcome + causal receipt                                          │
                                     ↓                                                       │
                       applicability evaluator ───────────────────────────────────────────────┘
```

### Ownership rules

1. **Context Compiler owns admission, not all loading.** Adapters may run in
   parallel and cache under explicit revisions.
2. **Situation owns current relevance, not durable truth.** It is rebuildable
   and surface-neutral.
3. **Domain commands own mutation.** AI never writes read models directly.
4. **Receipts explain influence, not private content.** Safe public reasons and
   content-free private influence labels remain the rule.
5. **Outcomes remain domain-specific evidence.** A later evaluator decides
   applicability; it never turns proxy behavior directly into truth.
6. **Channels remain different.** Chat, map, Home, Places, and push may render
   the same decision differently without independently deciding it.
7. **Compatibility is explicit and temporary.** TripWorldModel and prompt-
   specific situation paths remain adapters with named consumers and removal
   gates.

## 8. What not to build

- Do not replace Trips with a universal Plan aggregate.
- Do not persist `TripMemberFacet`; the accepted benchmark decision remains
  sound until measured thresholds are crossed.
- Do not create a universal outcome or event table.
- Do not make circle membership imply attendance, availability, authority, or
  shared preference.
- Do not add required “why I saved this” fields.
- Do not let inferred intent become an uncorrectable user fact.
- Do not expose raw private memory as a receipt explanation.
- Do not add a second notification or realtime channel for this program.
- Do not promote World Foundry row count as product readiness.
- Do not enable broad ambient merely to demonstrate that the code runs.
- Do not start a new card family for every producer; project decisions into
  existing surface roles where possible.

## 9. Ordered convergence program

### Phase 0 — Re-establish truth and governance

**Goal:** ensure the baseline can be trusted before behavioral convergence.

1. Resolve J08’s live block / pinned-now mismatch.
2. Re-run the 28 seeded journeys at the current consolidated revisions.
3. Add the three missing app flags to the registry and extend the scanner.
4. Update World Foundry operations to reflect persistence-library reality while
   retaining the no-operator-apply/no-editorial/index-cert caveats.
5. Select the exact group weather-rescue and local saved-place scenarios that
   will own the convergence proof.

**Exit:** 28/28 seeded replay or an accepted correction to an invalid journey;
flag/current-state truth is complete; no doc claims an absent Foundry apply path.

### Phase 1 — Shared scopes and causal identity, no behavior change

**Goal:** make current executions inspectably related before changing decisions.

1. Resolve `ExperienceScope` and `RelationshipScope` at chat, planner, Home,
   Places grounding, ambient judgment, voice, and outcome-reconciliation entry.
2. Add scopes to typed Situation.
3. Create child AI runs for bounded planner/grounding/judgment attempts.
4. Thread AI run, workflow, correlation, source revisions, and target identity
   into existing receipts.
5. Add privacy-safe trace assertions and orphan-join checks.

**Exit:** both target scenarios produce one content-free causal trace even while
legacy behavior remains selected.

### Phase 2 — Context convergence on the group Trip loop

**Goal:** prove the new serving boundary changes one real decision safely.

1. Complete Context Compiler source coverage required by weather rescue and
   current group planning.
2. Dual-render legacy and compiled planner packets.
3. Compare source coverage, constraints, group safety, route/time/weather
   freshness, latency, and itinerary/proposal quality.
4. Canary compiled context for the selected trip only.
5. Render the weather-rescue proposal in the app through canonical proposal,
   vote, apply, revert, and receipt paths.

**Exit:** two-device proof shows one grounded disruption decision and all Plan,
map, Home, and group views converge after resolution.

### Phase 3 — Passive everyday activation and second occasion

**Goal:** prove everyday value before earning push.

1. Expose one saved-place opportunity in an existing in-app surface.
2. Preserve save origin and opportunity receipt through “shape a Plan.”
3. Replace the single hard-coded local doorway with bounded origin-aware entry
   from save/place/conversation/person.
4. Enable local Plan and outcome artifact only for the internal cohort.
5. Implement outcome applicability across current roster, place, occasion,
   recency, and correction state.
6. Run the second-occasion comparison.

**Exit:** a real user completes saved interest → local Plan → occurrence →
outcome → materially better next Plan, with no notification required.

### Phase 4 — Golden-world depth for the two loops

**Goal:** make the place corpus support local-friend judgment and multiple
lenses, not generic recommendation coverage.

1. Select a small Lisbon/Riviera thesis-anchor set used by the target scenarios.
2. Fill exact geometry, hours/availability, operating state, access, price, group
   fit, arrival guidance, and interpretive evidence as each anchor requires.
3. Add evidence-linked editorial promotion.
4. Synchronize the derived index and prove ID/hash/review parity.
5. Certify planning, narration, proactive, and multiplayer capabilities through
   the actual runtime consumers.

**Exit:** every target recommendation can explain practical judgment, one
interpretive lens, applicability to this person/group, and current limitations.

### Phase 5 — Earned proactive delivery

**Goal:** move from passive value to push only after precision is demonstrated.

1. Compare in-app opportunity acceptance, dismissal, expiry, Plan creation, and
   realized outcome against non-intervention.
2. Establish per-user attention budget, cooldown, channel eligibility, and
   quiet-hour behavior through existing arbitration.
3. Canary one candidate type to a tiny internal cohort.
4. Join delivery to downstream action and lived outcome using the causal
   envelope.
5. Keep a kill switch and holdout.

**Exit:** push shows incremental action or value without unacceptable
interruption/dismissal/regret, and every delivery has an explainable source and
reversible user control.

## 10. Product and engineering scorecard

### Product-loop metrics

- time from opportunity or disruption to a committed decision;
- percentage of proposals changed before acceptance;
- group participation and unresolved-decision rate;
- passive opportunity → local Plan conversion;
- Plan → confirmed per-person occurrence;
- outcome capture without explicit form completion burden;
- second-occasion improvement in specificity, fit, and coordination effort;
- inappropriate-repeat and wrong-companion application rate;
- user-rated “felt like local judgment” and “showed me a meaningful lens.”

### Trust and safety metrics

- private-context egress violations: zero;
- stale/wrong-place/wrong-roster decisions: zero in certification corpus;
- route/weather/availability provenance coverage;
- receipt availability and safe explanation coverage;
- correction propagation latency;
- circle revocation and location-consent teardown correctness;
- unsupported certainty and degraded-evidence disclosure rate.

### Engineering convergence metrics

- percentage of AI runs carrying Experience and Relationship scopes;
- percentage of target decisions with complete causal joins;
- Context Compiler parity, cutover, and legacy consumer count;
- count of active competing clock/situation/context policies;
- registered vs discovered feature flags in both repos;
- dark flags with current owner, expiry, journey, and evidence;
- World Foundry accepted anchors with runtime capability certification;
- stable-patch weekly progress by experienced loop rather than raw commits.

## 11. Seven-day convergence readout

The recent commit history supports, rather than contradicts, this diagnosis.
Representative sequences include:

- Aug 6: lived-experience Product Model adoption, spatial truth repair,
  trip-optional spatial situations, local Plan and outcome surfaces;
- Aug 7: ExperienceScope, local occasion compounding, ambient shadow cycles,
  relationship visibility, per-person outcomes, and companion-fit learning;
- Aug 8: route-fact provenance/freshness, canonical trip time, typed map stop
  identity, weather grounding/rescue, place opportunity metrics, social circles,
  and relationship-aware agent gates;
- Aug 9: RelationshipScope in AI contracts, governed relationship claims,
  consented sharing, save-origin context, saved-nearby opportunities, World
  Foundry promotion/persistence/capability gates, editorial maps, and canon
  consolidation.

This is coherent substrate progress. It also explains the product gap: work was
distributed across authorities, migrations, gates, corpus, app surfaces, and
tests faster than the team could close and certify the final user loops.

The weekly narrative should therefore be:

> We assembled the governed ingredients of a place- and relationship-aware
> world model. The next milestone is not more ingredient count; it is proving
> that they make one group decision and one everyday local occasion materially
> better end to end.

### 11.1 Commit volume is integration evidence, not a feature count

At the end of this audit, the reachable seven-day histories contained:

| Repository | All reachable commits | Reachable non-merge commits | Meaning |
| --- | ---: | ---: | --- |
| `travel-agent` | 783 | 733 | Backend, corpus, policy, migration, tests, and consolidation lineage. |
| `travel-app` | 654 | 581 | Mobile behavior, home-surface composition, tests, generated types, and consolidation lineage. |
| workspace | 187 | 171 | Cross-repo contracts, journeys, governance, release evidence, and documentation. |

These numbers are intentionally **not** presented as 1,624 distinct product
features. The histories include formerly parallel branches, repeated logical
remediation, merges, generated contracts, seed/corpus material, formatting,
tests, and consolidation. “Non-merge” means Git commits that have at most one
parent; it removes merge nodes from the count, but it does not deduplicate
equivalent patches or convert commits into user value.

The meaningful seven-day progression is architectural and experiential:

1. the company thesis and Product Model became more explicit about lived
   experience, relationships, places, moments, outcomes, proactivity, and the
   second occasion;
2. the backend gained governed primitives for those claims;
3. the app gained substantial local-Plan, map, outcome, circle, Trips, and
   Places expressions;
4. the design system moved from isolated card studies toward whole-page
   composition and surface responsibility;
5. the proof system became more honest about the difference between code,
   fixtures, backend-real behavior, and device evidence.

The same evidence also shows the central risk: implementation breadth has been
growing faster than end-to-end product closure.

### 11.2 Home-surface design evolution

The Aug 9 `vesper-home-surfaces` bundle is directionally aligned with the
product pivot. It no longer treats Home as a static choice between “travel
mode” and “local mode.” Its strongest rules are:

- state is a **composition mix**, not a global mode;
- local Plans can coexist with travel Trips;
- Trips owns urgency, decisions, active Plans, and operational consequence;
- Places owns place judgment, provenance, interpretation, change, and durable
  place relationship;
- the map explains spatial shape and consequence but does not become a second
  Plan authority;
- source code and real contracts win on implementation truth; the boards govern
  adopted design intent rather than pretending to be executable truth.

This is a real design improvement. The bundle already contains an offer close
to Journey 2: “I can put Thursday together,” grounded by free time and saved
places. It also allows local Plans to appear between Trips, which is much closer
to the thesis than a tourism-only Trips feed.

The implementation inventory is appropriately less optimistic:

| Home composition state | Count |
| --- | ---: |
| Adopted | 13 |
| Unresolved | 19 |
| Relocated | 1 |
| Deterministic fixture-reviewed (`F`) | 0 |
| Backend-real verified (`B`) | 0 |
| Physical-device verified (`V`) | 0 |

This does not mean the surfaces are empty. It means components, producers,
projections, and actions exist at different depths, while none of the 33
tracked composition families has yet crossed the review, backend-real, or
device-certification boundary against this exact design authority.

Two design/governance seams should be repaired during convergence:

1. The authority record pins `Trips - The Page` and `Places - The Page`, but
   excludes `Trips - Whole Pages` and `Places - Whole Pages`, even though the
   whole-page studies contain important cross-state rhythm and placement rules.
   Either pin their current hashes or state explicitly that they are advisory.
2. The design bundle describes local Plan production as missing in one place,
   while the current app and backend have a real, gated local Plan path. The
   design audit should be refreshed so adoption decisions are made from the
   actual implementation baseline.

The app architecture has nevertheless become more coherent. Trips Home now has
one physical page plan, a controller, a render model, and an ordered body rather
than multiple independent features competing to render. Places has a pure
presentation boundary and a renderer-family registry. This is the right base
for convergence, but it should now be used to compose the canonical journeys,
not to add more families.

### 11.3 Demo readiness against the canonical journey order

The canonical journey ranking is correct. The following estimates describe
distance in **vertical product slices**, not engineer-days. One slice includes
the product decision, backend behavior, mobile path, action semantics,
deterministic evidence, and proportionate device proof.

| Rank | Journey | Current substrate | Principal missing seam | Estimated distance |
| ---: | --- | --- | --- | ---: |
| 1 | **Save our Plan when reality changes** | Weather and venue-disruption detection, route/time facts, grounded alternatives, canonical proposal operations, notification/attention substrate, Plan/map projections. | Select one deterministic disruption, make the proposal legible in mobile, drive accept/reject/revert, and prove Plan/map/Now/group convergence. Relevant rescue flags remain dark. | 2–3 slices |
| 2 | **Make something of right now** | Local Plan aggregate and screen, spatial reachability, nearby/open-now place opportunities, saves, map door, chat planning, route facts. | Add the explicit **Take me somewhere** entry, compose one bounded micro-journey rather than a list, preserve the next commitment, start it, and repair it once. | 3–4 slices |
| 3 | **Make tonight easy for the group** | Local Plan path, invite/RSVP foundations, group chat, constraints, companion context, proposals, outcome artifact. | Replace the hard-coded Friday-night doorway, provide one credible second-participant/thin path, and certify private-to-group-safe contribution and commitment. | 1–2 slices for a fixture demo; 2–3 for external alpha |
| 4 | **Notice an opening for us** | Shadow ambient cycle, attention arbitration, coarse consented coincidence, saved-place opportunities, social circles, cadence/silence primitives. | Product-facing candidate projection, explicit relationship permission, invitation agency, tentative-to-shared Plan transition, negative-oracle behavior, and outcome attribution. | 3–4 slices |
| 5 | **Know the place like a trusted local friend** | Place identity/provenance, dossiers and briefs, World Foundry review/capability gates, automatic context, geometry, hours, route and basic grounded reasons. | Complete one small anchor corpus with practical local judgment, confidence/freshness/caveats, group/occasion applicability, and a direct Plan action. | 2–3 slices in one seeded city |
| 6 | **Be better on the next occasion** | Confirmed occurrence, correctable outcomes, place verdict, companion fit, relationship claims, structural prior occasion, planner reuse. | Add one governed applicability projection so the current roster/occasion/place can safely reuse rich prior evidence, then show the new Plan changed because of it. | 2 slices |
| 7 | **Experience a place through a meaningful lens** | Place angles, dossiers, editorial evidence, narration and interpretation substrate, user steering/memory concepts. | Promote and retrieve one evidence-linked lens, reveal it at the useful physical moment, distinguish fact/interpretation/memory, and measure changed attention or action. | 1–2 slices scripted; 2–3 robust |
| 8 | **Plan an entire trip** | Most mature historical planning, itinerary, collaboration, proposal, map, booking handoff, and journey coverage. | Current-revision/device certification and focused polish; it should support the demo rather than lead the category story. | About 1 certification/polish slice |

The estimates should not be summed into one giant sequential roadmap. Several
share the same missing joints: a real second participant, a causal receipt,
one grounded place packet, Plan/map/time convergence, and device evidence.

### 11.4 What is connected today—and what is merely adjacent

The system is already coherent at the level of authorities:

- time and availability can constrain a Plan;
- location and spatial reachability can qualify nearby candidates;
- Mapbox-backed route facts can shape feasibility and map projections;
- weather and venue state can identify a broken Plan;
- place identity and provenance can ground an alternative;
- proposal operations can govern a multiplayer mutation;
- occurrence and outcome can record what happened;
- relationship evidence can, in bounded paths, affect a later plan.

It is not yet fully coherent as one user experience because the joins stop at
different boundaries:

- ambient produces candidates but does not deliver a user-facing opening;
- rescue produces drafts but is not a certified mobile loop;
- circles represent permissioned relationship topology but do not reliably
  change live AI judgment;
- the map shows useful consequence but is still mostly a door/static projection
  rather than the active micro-journey surface;
- rich outcomes are captured, but the next-occasion packet is still mostly
  structural;
- several surfaces are internal or default-dark;
- `TRIP_EDITORIAL_MAP_ENABLED` is defined and tested, while the observed
  day-map composition is currently controlled through another local-Plan gate,
  indicating flag/call-site drift that should be resolved before promotion.

The honest product description is therefore: **integrated substrate, partially
integrated experience, not yet a coherent external-alpha loop**.

### 11.5 Convergence scenario and operating rule

The next milestone should use one fixed scenario so that product, engineering,
design, and evidence all optimize the same experienced truth:

> Feihu and Maya are in Lisbon with ninety minutes before dinner. They tap
> **Take us somewhere**. Vesper composes a small route that fits their time,
> interests, weather, and next commitment. A material condition changes;
> Vesper proposes one grounded repair. Both people remain synchronized through
> one shared Plan and map. Afterward, each can privately confirm or correct the
> outcome. On a later New York occasion, Vesper uses only permitted evidence to
> notice a relevant opening and make the next plan better.

This scenario exercises the company rather than one feature: place truth,
spatial proximity, route/time, weather, AI judgment, multiplayer agency,
governed action, outcome, proactivity, and the second occasion.

For the next implementation cycle, change the work mix from substrate expansion
to convergence:

| Work type | Recent tendency | Next-cycle target |
| --- | ---: | ---: |
| New substrate / feature families | ~70% | ~15% |
| Cross-system integration and UX closure | ~20% | ~55% |
| Fixtures, backend-real proof, device evidence, and user rehearsal | ~10% | ~30% |

The percentages are directional planning constraints, not time accounting.
Their purpose is to prevent another broad architecture week from delaying the
moment when a user can feel the thesis.

The ordered build sequence is:

1. land and certify a clean consolidated baseline;
2. repair J08 and any map/editorial-map flag drift;
3. add the explicit **Take me/us somewhere** doorway;
4. compose and launch one bounded local micro-journey;
5. connect one real second participant through the thinnest credible path;
6. route one deterministic weather or venue failure through the canonical
   proposal, acceptance, and coherent projection path;
7. capture one correctable outcome;
8. apply it through a governed second-occasion resolver;
9. only then expose one passive ambient opening; push remains earned, not
   assumed.

### 11.6 Are we on the right track?

**Yes strategically; not yet at the proof threshold.**

The recent push is coherent with the product vision. It moves Vesper away from
“AI trip planner” and toward a proactive, multiplayer, place-aware system that
can remain responsible as people turn intent into lived experience. The code
is not missing a wholesale re-pivot. It is missing ruthless completion of the
seams that make the thesis visible.

The next week should therefore be judged by a different question. Not “How many
systems or frames did we add?” but:

> Can one person show another person, on a device, that Vesper understood the
> people, place, time, and changing reality; took one governed action; kept the
> shared world coherent; and became concretely better on the next occasion?

If the answer becomes yes for the fixed scenario, the recent architectural
investment will read as one differentiated product rather than an impressive
collection of adjacent capabilities.

## 12. Final recommendation

Proceed with the accepted direction, but narrow execution to the two proof
loops and the shared serving/receipt kernel they require.

The convergence is genuinely stronger in the substrate than in the experienced
product. That is not because the product thesis is ahead of the architecture;
the architecture already embodies most of it. It is because the final mile is
distributed across several safe but incomplete boundaries:

- context selection versus current situation;
- relationship storage versus relationship effect;
- place truth versus runtime judgment;
- opportunity production versus user opening;
- outcome capture versus future applicability;
- backend implementation versus mobile gate;
- code path versus journey/device evidence.

Close those boundaries in an experienced loop before widening the corpus,
adding more social mechanics, or enabling broad push. If the two loops work,
the thesis will become legible in the product: Vesper will not merely know more
about places and people; it will make better-timed, more grounded, more
relationship-specific decisions—and get better after the experience.

## Evidence index

Primary code and contract anchors consulted:

- `travel-agent/backend/core/experience_scope.py`
- `travel-agent/backend/core/relationship_scope.py`
- `travel-agent/backend/core/ai_runs.py`
- `travel-agent/backend/api/routes/_message_flow.py`
- `travel-agent/backend/concierge/turn_loader.py`
- `travel-agent/backend/concierge/tool_handlers/planning/_plan.py`
- `travel-agent/backend/core/context_compiler/`
- `travel-agent/backend/situation/`
- `travel-agent/backend/concierge/spatial_situation.py`
- `travel-agent/backend/core/ambient_dispatch.py`
- `travel-agent/backend/core/models/place_truth.py`
- `travel-agent/backend/places/opportunity_producers.py`
- `travel-agent/backend/core/db/experience_outcomes.py`
- `travel-agent/backend/core/db/occasion_context.py`
- `travel-agent/backend/core/db/relationship_memory.py`
- `travel-agent/backend/world_foundry/`
- `travel-agent/tools/seed/staging/runs/lisbon.2026-08.pilot-01/capability-report.md`
- `travel-app/constants/featureFlags.ts`
- `travel-app/components/trips/TripsHomeController.ts`
- `travel-app/components/trip-plan/LocalPlanScreen.tsx`
- `travel-app/data/social.ts`
- `docs/decisions/2026-08-09-experience-context-and-relationship-kernel.md`
- `docs/flags/registry.yaml`
- `docs/journeys/STATUS.md`
- `docs/release/v1-scope.md`
- `docs/status/current-state.md`
- `scripts/check_flag_registry.py`

Related prior audits remain useful for their narrower scopes, especially:

- `travel-agent/docs/working/parallel-implementations-audit-2026-08-04.md`;
- `travel-agent/docs/working/Map and Itinerary Integration.md`;
- `docs/working/multiplayer-implementation-sequence.md`;
- `docs/working/shared-plan-handoff-execution-2026-08-07.md`.

Those documents should not be read as fresher evidence than the dated findings
above where their implementation status differs.
