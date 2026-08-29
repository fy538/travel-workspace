---
doc_type: working
status: active
owner: founder / product / design / architecture / engineering
created: 2026-08-23
last_verified: 2026-08-28
expires: 2026-09-22
why_new: Turns the approved canonical-artifact direction into one cross-repository execution plan covering identity, viewer-safe projection, visual families, bounded relationships, portfolio fixtures, Life exploration, validation, rollout, and cancellation without creating a new artifact authority.
supersedes: []
promotes_to: null
source_of_truth_for: []
---

# Canonical Artifact Projection and Visual System Execution Plan

> Status: active working implementation plan
>
> This document coordinates a bounded cross-repository program. It is not a
> new product canon, durable authority, release approval, schema authorization,
> or approval of the Life root. Product authority remains in Product Thesis,
> Product Model, the Experience Constitution, and the Artifact and Experience
> Anchor Grammar. Stable contracts discovered here should be promoted to their
> canonical backend, frontend, or cross-repository owners before this document
> expires.

Governing inputs and implementation anchors:

- [Systematic Product-Engine Roadmap](systematic-product-engine-roadmap-2026-08-23.md)
- [Vesper Experience Constitution and Interaction Grammar](vesper-experience-constitution-and-interaction-grammar-2026-08-22.md)
- [Consequence Arbitration and Cross-Surface Experience Blueprints](consequence-arbitration-and-cross-surface-blueprints-2026-08-26.md)
- [Product Model](../../travel-agent/docs/product/Product%20Model.md)
- [Vesper Expression, Medium, and Projection Canon](../../travel-agent/docs/product/Vesper%20Expression%2C%20Medium%2C%20and%20Projection%20Canon.md)
- [Artifact and Experience Anchor Grammar v1](../../travel-agent/docs/working/artifact-and-experience-anchor-grammar-v1-2026-08-21.md)
- [Experience Anchors, Occasions, and Visual Memory](../../travel-agent/docs/working/experience-anchors-occasions-and-visual-memory-2026-08-19.md)
- [Clean-Break Experience Graph](../../travel-agent/docs/architecture/clean-break-experience-graph-2026-08-21.md)
- [Intake anchor read model](../../travel-agent/backend/core/models/intake_anchor.py)
- [Intake-to-graph bridge](../../travel-agent/backend/inbound/experience_graph_bridge.py)
- [Viewer-relative graph compiler](../../travel-agent/backend/core/experience_graph_projection.py)
- [Mobile graph data seam](../../travel-app/data/experienceGraph.ts)
- [Chat card blueprint contract](../../travel-app/utils/chat/cardBlueprint.ts)

## 1. Executive decision

Build a **viewer-safe canonical artifact projection and rendering system over
existing authorities**.

Do not build:

- a universal artifact table;
- a universal relationship table;
- a graph database;
- a server-driven layout schema;
- a source-specific component or ingestion pipeline per artifact type;
- a new memory authority;
- a Life archive backed by another accumulation store; or
- an architecture whose ontology is selected by the first mounted loop.

The implementation must be systematic across a deliberately varied artifact
portfolio before production mounting. Work may land incrementally, but the
first implementation case is only an integration packet. It does not define
the system's permanent nouns, visual language, or storage design.

The target runtime is:

```text
existing canonical authorities
  SourceRef / Intake candidate / Experience Anchor / Occasion / Outcome / Receipt
        ↓
viewer-safe adapter for the current ResourceRef and scope
        ↓
CanonicalArtifactProjectionV1
        ├── deterministic render-profile resolver
        │       ↓
        │   Movement / Dwelling / Gathering / Encounter
        │       ↓
        │   one lead medium + optional modifiers
        │       ↓
        │   compact / standard / immersive density
        │       ↓
        │   Home / Chat / Places / Life / Plan / Occasion context
        │
        └── bounded relationship compiler
                ↓
            Occasion / Place / time / Mine / Together neighborhoods
```

“Artifact” is a projection of durable truth, not another truth owner.

The implementation currently retains the legacy `compact | standard |
timeline | occasion | constellation` mode union. Those keys are compatibility
renderers, not one canonical dimension: compact and standard describe density;
timeline is sequence; Occasion is a surface/composition context; and
constellation is a relational composition. This plan records that distinction
without claiming the landed contract has migrated.

This projection system is a carrier layer, not the product center. The human
unit remains Experience; Occasion owns bounded shared consequences; Status is
one featured share projection; and human contribution extends beyond media to
presence, judgment, labor, care, boundaries, Commitments, and meaning.

## 2. Why this is non-regrettable now

The required substrate already exists in several intentionally separate
authorities:

1. Intake owns source custody, semantic candidates, evidence-bound claims,
   correction posture, retention status, and the owner-private
   `ExperienceAnchorProjection`.
2. The Intake anchor compiler already maps confirmed semantic candidates into
   a bounded graph-anchor proposal without writing a Plan, Occasion, memory,
   audience, or notification.
3. The one-way Intake-to-graph bridge already creates deterministic graph
   anchor identity, copies no source bytes, and retains Intake lineage.
4. The graph owns operational anchors, accepted Occasion links, occurrence
   evidence, personal Outcomes, and viewer-relative Mine/Together reads.
5. `ResourceRef`, `SourceRef`, `CommandEnvelope`, and `ActionReceipt` already
   establish the execution identity and readback seam.
6. Mobile already has a shared graph data facade and a mature bounded Chat
   artifact presentation grammar.
7. The product documents already define five semantic anchor families, four
   visual families, seven phases, and the rule that categories are projections
   rather than folders.

The missing layer is therefore mostly a governed **read adapter plus visual and
organizational grammar**. It should not begin with a new database.

## 3. Goals, non-goals, and success condition

### 3.1 Goals

1. Give every retained source-derived Experience Anchor an attractive,
   inspectable, viewer-safe canonical projection.
2. Let a composed Occasion render several anchors as one coherent episode
   without merging their source, truth, audience, or lifecycle.
3. Let the same `ResourceRef` appear coherently in Chat, a focused sheet,
   timeline, Occasion, Place context, and a Life exploration surface.
4. Make Movement, Dwelling, Gathering, and Encounter artifacts feel related by
   brand and interaction grammar while remaining visually and semantically
   distinct.
5. Make phase maturation visible: prospective, upcoming, live, resolving,
   lived, remembered, and expired.
6. Compile useful organization from explicit canonical links before
   introducing model-inferred themes.
7. Preserve Mine/Together plurality and source/correction/deletion behavior
   throughout every projection.
8. Create an executable fixture and visual-QA portfolio that makes later
   renderer and architecture changes cheap to evaluate.

### 3.2 Non-goals for this program

- automatic camera-roll, email, wallet, or background-location ingestion;
- production semantic classification quality;
- a universal Life root or navigation cutover;
- public artifact publishing;
- model-authored biography or emotional narrative;
- inferred relationship health or group meaning;
- first-party booking, payment, expense, or marketplace execution;
- push or proactive resurfacing;
- persistent inferred themes;
- an infinite global constellation; or
- replacing the existing Chat `CardBlueprintV1` contract.

### 3.3 Completion condition

The program is complete when the portfolio can demonstrate that one canonical
resource:

- retains stable identity and revision across all mounted projections;
- changes emphasis honestly across phases;
- appears differently but coherently across visual modes;
- respects Mine/Together privacy;
- degrades safely when source custody changes;
- updates everywhere after correction;
- composes into an Occasion without becoming duplicate truth;
- participates in bounded timeline, Place, and relationship neighborhoods;
- invokes only owner-authorized actions; and
- remains useful and attractive without a perfect hero image.

## 4. Foundational decisions to freeze before runtime work

### D1 — Canonical artifact identity

**Recommendation:** there is no universal artifact identity. The projection's
identity is the canonical resource it makes legible.

Initial allowlisted resource kinds:

```text
experience_anchor
occasion
outcome
receipt
```

Later kinds may be admitted only when a real retained product journey cannot
use these owners or an existing typed Chat artifact.

For source-derived durable artifacts:

```text
SourceRef
  → confirmed Intake candidate
  → deterministic graph Experience Anchor
  → ResourceRef(kind=experience_anchor, id=graph_anchor_id)
```

An answer-only, dismissed, rejected, or expired candidate need not become a
durable canonical artifact. Intake identity remains provenance and custody
identity, not the public artifact identity.

For an episode composition:

```text
ResourceRef(kind=occasion, id=occasion_id)
```

The Occasion projection refers to its accepted anchors. It does not duplicate
their facts, sources, or personal Outcomes into a second owner.

### D2 — Projection ownership

The projection compiler belongs in the application/read layer. It coordinates
owner-scoped reads but writes no canonical domain state.

Adapter boundaries:

```text
Intake adapter     source status, claims, family, subtype, phase, correction
Graph adapter      canonical anchor, Place binding, Occasion links, occurrence
Occasion adapter   shared episode core and accepted members/anchors
Outcome adapter    viewer-owned occurrence/meaning and correction revision
Receipt adapter    command result, readback, reversal, degraded evidence
```

The compiler may join these read models only through explicit stable
identifiers. It may not infer a missing domain link or treat similarity as
authority.

### D3 — Semantic versus visual contract

The backend sends meaning and authority. The app owns visual composition.

The backend contract must not contain:

- colors;
- fonts;
- padding;
- component names;
- card geometry;
- layout coordinates;
- route implementation details beyond canonical owner destinations;
- animation names; or
- a generic block tree intended to render every product surface.

The mobile render-profile resolver must be pure and deterministic. It cannot
write state, call a model, or silently reinterpret truth.

### D4 — Portfolio-first architecture

Contract and renderer decisions must be evaluated against a fixed portfolio
spanning all four visual families, several phases, Mine/Together, correction,
source degradation, sparse media, and ambiguity.

A first mounted artifact may prove integration but cannot promote:

- a schema field;
- a renderer family;
- a generic relation;
- a persistence table;
- a route; or
- a product-wide default

unless the portfolio demonstrates that the decision composes beyond the first
case.

### D5 — Explicit relationships first

V1 relationships are compiled from canonical links, source lineage,
viewer-authored meaning, and observed evidence. Model-inferred semantic themes
are deferred.

### D6 — Life remains a hypothesis

The first Life expression is a read-only lab or dev fixture. It does not become
a root, replace You/Atlas, or introduce a new navigation destination until its
contract, owner state, and correction behavior are accepted independently.

### D7 — One composer, distinct circulation commands

Private artifact, named-person handoff, featured Status, Occasion contribution,
and public Place contribution should reuse source custody, viewer-safe
projection, and presentation primitives. They must not reuse one ambiguous
visibility mutation.

The UI may provide one common composer. It reveals destination choice only
after expressed sharing intent or an invoked share affordance; it is not a
generic follow-up to every input. The application layer still needs typed
command boundaries for Send, Address, Share, Contribute-to-Occasion, and
Publish/Contribute-to-Place, each with audience, purpose, attribution, expiry,
receipt, correction, and revocation behavior.

Do not add a `status` table now. A future featured-share read model should
project the current active share/publication authority. If publish, replace,
expire, and revoke cannot be expressed honestly with existing grants and
receipts, that gap—not the word Status—may justify a small durable authority.

## 5. CanonicalArtifactProjectionV1

### 5.1 Contract shape

The backend should define a strict generated API model conceptually equivalent
to:

```yaml
canonical_artifact_projection:
  schema_version: canonical-artifact-projection.v1

  resource:
    kind: experience_anchor
    id: ...
    revision: ...
    canonical_path: ...

  scope:
    mode: mine                 # mine | together
    audience: private         # private | bounded_shared
    viewer_role: owner        # owner | participant

  source:
    refs: []
    status: available         # available | degraded | deleted | unavailable
    content_available: true
    original_inspectable: true

  anchor:
    family: movement          # movement | base | attendance | dining | attention
    subtype: flight
    phase: upcoming
    occurrence: scheduled
    operational_state: ticketed

  context:
    place_refs: []
    time_window: null
    occasion_refs: []
    plan_refs: []
    participant_summary: null

  facts: []
  media: []
  unknowns: []
  provenance: []
  allowed_actions: []
  correction: null
  owner_destinations: []
  updated_at: ...
```

### 5.2 `resource`

Use the existing `ResourceRef` vocabulary. The response revision must change
whenever a viewer-visible fact, allowed action, source status, audience,
correction, or owner destination changes.

The canonical path points to a stable owner destination, not necessarily a
standalone page. It may focus a conversation artifact, focused sheet, root
projection, or existing owner workspace.

### 5.3 `scope`

Required fields:

| Field | Meaning |
|---|---|
| `mode` | `mine` or `together`; no public `whole` mode |
| `audience` | Private or explicitly bounded shared projection |
| `viewer_role` | Owner or currently authorized participant |

The contract should not return raw viewer IDs, hidden member IDs, or omitted
private values. If the UI must explain that private context was withheld, use
a bounded boolean or count that cannot reveal another person's record shape.

### 5.4 `source`

The source summary exposes custody posture, not raw source payloads:

- safe `SourceRef` identities;
- available/degraded/deleted/unavailable state;
- whether original inspection is currently possible;
- whether some displayed facts have lost their original evidence; and
- optional safe source label.

Raw bytes, signed media URLs, booking codes, addresses, and protected fields do
not live in the projection. An authenticated media/source resolver supplies
ephemeral access when separately authorized.

### 5.5 `anchor`

The anchor block keeps independent axes independent:

- semantic family;
- subtype;
- phase;
- occurrence state; and
- operational state.

Do not collapse these into a single artifact type such as `completed_flight`
or `memory_dinner`.

### 5.6 `context`

Context contains stable references and bounded summaries:

- canonical Place `EntityRef`s;
- time window;
- accepted Occasion references;
- declared Plan references when authorized;
- participant count or safe authored group label; and
- no inferred attendance or relationship meaning.

Participant identities appear only when the relevant Occasion/relationship
projection authorizes them. An artifact source containing names is not enough.

### 5.7 `facts`

Facts use a bounded discriminated contract rather than arbitrary display JSON:

```yaml
fact:
  key: scheduled_departure
  kind: instant              # text | instant | time_window | place_ref |
                             # status | number | money | duration | route
  value: ...
  truth_mode: source_extracted
  confidence: 0.98
  observed_at: ...
  valid_until: ...
  source_refs: []
  audience: private
```

The app owns localized labels and formatting for registered keys. Unknown keys
fail closed into provenance inspection rather than entering the visual hero.

Initial cross-family fact-key registry:

```text
identity
title
provider
place
starts_at
ends_at
duration
status
occurrence_state
source_label
outcome_meaning
open_question
```

Initial Movement keys:

```text
origin_place
destination_place
scheduled_departure
scheduled_arrival
service_identifier
terminal
gate_or_platform
provider_status
```

Initial Dwelling keys:

```text
base_place
check_in
check_out
neighborhood
access_status
```

Initial Gathering keys:

```text
occasion_place
occasion_start
participation_state
participant_count
invitation_author
shared_outcome_state
```

Initial Encounter keys:

```text
focal_subject
observed_place
observed_at
question
grounded_interpretation
authored_meaning
continuation
```

Provider-live fields must carry `valid_until`. Expired gate, platform, access,
availability, or queue facts are excluded from the active facts list and may
leave only a bounded historical provenance cue.

### 5.8 `media`

Media entries contain opaque authenticated references and semantic roles:

```text
evidence
hero_candidate
supporting
source_preview
```

They also name audience and availability. The renderer chooses whether media
is visually appropriate. `hero_candidate` is not a command to display it as a
hero.

Generated decorative images are excluded from V1 canonical artifacts.

### 5.9 `unknowns`

Unknowns are bounded, safe, and actionable where possible:

- unresolved Place;
- uncertain time;
- unconfirmed occurrence;
- source removed;
- participation unknown; or
- interpretation corrected/withdrawn.

The UI should show unknown only when it changes comprehension, trust, or a
possible action. Unknowns are not a confidence dashboard.

### 5.10 `allowed_actions`

Actions contain resolver references, never write payloads:

```yaml
action:
  action_ref: ...
  kind: correct              # inspect_source | correct | link_occasion |
                             # open_owner | share_selected | forget | undo
  label_key: artifact.correct
  role: secondary
  capability: correct_anchor_claim
  availability: available   # available | disabled | expired
  requires_confirmation: false
  disabled_reason: null
```

The action resolver rechecks viewer, membership, revision, capability, source
availability, and current owner state before returning a command destination.

### 5.11 `correction`

The correction summary names which claims can be corrected and the current
correction revision. It does not expose ontology terms to the user. User-facing
choices remain concrete:

- wrong place;
- wrong time;
- not mine;
- did not happen;
- separate from this occasion;
- keep occurrence but remove interpretation;
- make private/remove sharing; or
- forget/delete.

### 5.12 Contract bounds

V1 responses should be deliberately bounded:

- at most 12 visible facts;
- at most 8 unknowns;
- at most 4 visible actions;
- at most 8 source/provenance references in the compact response;
- no raw media bytes;
- no arbitrary nested blocks; and
- deterministic ordering for every repeated field.

These are contract-complexity bounds, not visual requirements. Expanded
provenance may use a separately authorized endpoint.

## 6. Backend architecture

### 6.1 Proposed modules

```text
travel-agent/backend/core/models/canonical_artifact.py
  strict generated API and application contract models

travel-agent/backend/application/canonical_artifact_projection.py
  resolver, adapter registry, shared redaction, revision calculation

travel-agent/backend/application/artifact_adapters/
  intake_anchor.py
  experience_anchor.py
  occasion.py
  outcome.py
  receipt.py

travel-agent/backend/api/routes/artifact_projections.py
  authenticated allowlisted single-resource read

travel-agent/tests/application/test_canonical_artifact_projection.py
travel-agent/tests/api/test_artifact_projections.py
```

The exact folder split may be reduced if existing application conventions
favor fewer files. The architectural boundary is more important than the
directory count.

### 6.2 Adapter interface

Conceptual interface:

```python
class ArtifactProjectionAdapter(Protocol):
    resource_kind: str

    def compile(
        self,
        *,
        viewer_id: UUID,
        resource: ResourceRef,
        mode: Literal["mine", "together"],
        now: datetime,
    ) -> CanonicalArtifactProjectionV1 | None: ...
```

Rules:

1. Unsupported resource kinds fail closed.
2. Cross-owner private resources return not found, not a distinguishing privacy
   error.
3. Every adapter starts from its canonical owner read.
4. An adapter may call another owner reader only through a stable reference.
5. An adapter may omit a field but may not invent it.
6. All time-sensitive filtering receives an injected `now` for deterministic
   tests.
7. Revision calculation uses normalized viewer-visible output, not source-row
   timestamps alone.

### 6.3 Intake/graph anchor adapter

This is the core source-derived path:

```text
graph anchor ResourceRef
  → verify viewer ownership or authorized projection
  → recover Intake lineage through the existing bridge metadata
  → read owner-private Intake ExperienceAnchorProjection
  → read graph anchor, accepted Occasion links, Place binding, occurrence
  → redact/compile CanonicalArtifactProjectionV1
```

The adapter must not:

- treat an Intake candidate UUID as a graph anchor UUID;
- expose graph-local Place UUIDs as public identity;
- restore a revoked Intake source;
- copy raw source payloads;
- convert allowed read capabilities into write authority; or
- infer occurrence from anchor state alone.

If the current bridge metadata cannot reliably map a graph anchor back to its
Intake candidate, first expose a deterministic content-free mapping helper or
read projection. Do not add a new mapping table unless existing lineage cannot
survive correction, deletion, replay, or account lifecycle tests.

### 6.4 Occasion adapter

An Occasion projection composes:

- shared title/purpose and lifecycle;
- authorized Place and time;
- active membership summary;
- accepted anchor `ResourceRef`s;
- shared commitments when relevant;
- shared occurrence state;
- viewer's separately authorized personal Outcome references; and
- bounded unknown/correction posture.

It must not merge personal meanings into one shared narrative. Personal and
relationship layers remain separately fetchable projections.

### 6.5 Outcome adapter

The Outcome adapter is viewer-owned by default. It may show:

- what occurrence state the viewer recorded;
- explicitly authored meaning;
- linked anchor/Occasion/Place refs;
- correction revision;
- source degradation; and
- current visibility.

It must not promote private meaning into Together because the linked Occasion
is shared.

### 6.6 Receipt adapter

The receipt adapter reuses the canonical execution/receipt seam and exposes:

- what was attempted;
- current state;
- whether anything changed;
- owner readback status;
- reversibility/undo where available;
- degraded evidence; and
- canonical owner destination.

It must not display internal traces, hidden private influences, arbitrary
provider payloads, or a local-only success banner as durable truth.

### 6.7 API shape

Initial single-resource read:

```http
GET /api/artifact-projections/{resource_kind}/{resource_id}?mode=mine
```

Response:

```text
CanonicalArtifactProjectionV1
```

Do not build a generic artifact-search query language in V1.

Root-specific collections should eventually own their own selection policy:

```text
GET /api/life/projection?mode=mine
GET /api/life/projection?mode=together
```

Those root projections may contain bounded compact artifact projections or
stable refs. A batch resolver should be added only after a mounted root exposes
a measured N+1 or latency problem.

### 6.8 API governance

Any new endpoint is contract-sensitive and must include:

- backend model and route tests;
- OpenAPI regeneration;
- app-operation policy classification;
- generated mobile types;
- mock/real parity;
- account export/deletion analysis;
- correction behavior;
- cross-viewer privacy tests; and
- a declared production consumer or dark/retiring posture.

No endpoint may remain unflagged and unconsumed merely because it is useful to
a fixture gallery.

## 7. Mobile architecture

### 7.1 Proposed modules

```text
travel-app/data/canonicalArtifacts.ts
  generated-contract facade and query keys

travel-app/utils/artifacts/renderProfile.ts
  pure semantic projection → visual profile resolver

travel-app/utils/artifacts/contextProjection.ts
  pure explicit relationship and organization compiler

travel-app/utils/artifacts/factFormatting.ts
  registered fact labels, safe formatting, TTL-aware display

travel-app/components/artifacts/CanonicalArtifactFrame.tsx
travel-app/components/artifacts/ArtifactProvenanceSheet.tsx
travel-app/components/artifacts/ArtifactActionRow.tsx

travel-app/components/artifacts/families/MovementArtifact.tsx
travel-app/components/artifacts/families/DwellingArtifact.tsx
travel-app/components/artifacts/families/GatheringArtifact.tsx
travel-app/components/artifacts/families/EncounterArtifact.tsx

travel-app/constants/mocks/canonicalArtifacts.ts
travel-app/app/dev/canonical-artifact-gallery.tsx
travel-app/docs/surfaces/canonical-artifact-system/contract.md
```

Generated backend types must come from `schema.gen.ts`. Client-only render,
layout, and fixture-control types may live under `utils/` or component props.

Screens and components consume the `data/` facade; they do not import the API
transport directly.

### 7.2 Render profile

The landed V1 client contract still exposes the legacy `mode` union. The target
conceptual decomposition is:

```ts
type ArtifactMedium =
  | "evidence"
  | "sequence"
  | "comparison"
  | "spatial"
  | "prose"
  | "instrument";

type ArtifactRenderProfile = {
  family: "movement" | "dwelling" | "gathering" | "encounter";
  leadMedium: ArtifactMedium;
  supportingMedium: ArtifactMedium | null;
  modifiers: Array<"social" | "relational" | "quantitative">;
  semanticRole:
    | "canonical_state"
    | "operational_instrument"
    | "human_contribution"
    | "editorial_contribution"
    | "receipt";
  density: "compact" | "standard" | "immersive";
  surfaceContext:
    | "home"
    | "chat"
    | "places"
    | "life"
    | "plan"
    | "occasion";
  emphasis:
    | "identification"
    | "preparation"
    | "live_support"
    | "reconciliation"
    | "lived_outcome"
    | "continuity"
    | "minimal_receipt";
  morphology: string;
  factPriority: string[];
  mediaSlots: string[];
  materialRole: string;
  motionRole: string;
};
```

Selection inputs:

```text
canonical resource kind
+ semantic anchor family
+ phase
+ Occasion composition role
+ available non-expired facts
+ authorized media
+ Mine/Together scope
+ requested surface context and density
+ admitted job, semantic role, and necessary modifiers
= render profile
```

The resolver is exhaustive and fail-closed. Unsupported combinations fall back
to a compact truthful expression or direct owner link, not to a guessed family,
raw JSON card, or generic prose wrapper. A separate implementation decision
must define migration from the V1 `mode` field; this working plan does not
authorize an incompatible API or TypeScript change.

### 7.3 Family selection rules

| Input | Default visual family | Important exception |
|---|---|---|
| Movement anchor | Movement | An after-arrival focal observation may separately render as Encounter |
| Base anchor | Dwelling | A composed social stay Occasion may lead with Gathering |
| Attendance anchor | Gathering | A lived focal work/object may lead an Encounter projection |
| Dining anchor | Gathering | A standalone live menu question remains Encounter |
| Attention anchor | Encounter | It may support another Occasion without changing its own family |
| Multi-person Occasion | Gathering | Movement-led Occasion may retain a Movement composition |
| Outcome | Parent resource family | Sparse personal note may use Encounter treatment |
| Receipt | Parent resource family or neutral receipt | Never invent a new “receipt family” merely for chrome |

Family selection is a presentation decision. It never changes canonical
anchor family or owner state.

### 7.4 Phase emphasis

| Phase | Dominant visual job | Material that recedes |
|---|---|---|
| Prospective | Identify the object and ambiguity | Decorative media and secondary context |
| Upcoming | Prepare, coordinate, and orient | Source clutter |
| Live | One current fact/action and uncertainty | Historical and interpretive depth |
| Resolving | Compare intention with evidence | Promotional/source styling |
| Lived | Occurrence, selected media, Place, people, personal/shared Outcomes | Expired operational identifiers |
| Remembered | Relationship, question, capability, return cue | Routine logistics |
| Expired | Minimal receipt or nothing | Nearly everything |

### 7.5 Shared frame

All four families share:

- canonical identity and phase cue;
- one dominant statement;
- registered fact formatting;
- truthful uncertainty treatment;
- bounded provenance disclosure;
- owner/action grammar;
- correction affordance;
- accessibility ordering;
- Vesper typography and material kernel; and
- origin-preserving navigation.

The frame does not force every family into an identical rounded rectangle. It
owns semantic rhythm and controls, not a universal silhouette.

## 8. Four visual families

### 8.1 Movement

**Semantic character:** transition, direction, time, threshold, arrival.

**Primary structure:** origin → path → destination.

Potential composition elements:

- directional spine or route trace;
- distinct origin and destination anchors;
- departure/arrival rhythm;
- current threshold marker;
- provider/status as subordinate operational truth;
- connection or onward-base cue; and
- arrival Outcome after the movement resolves.

Phase behavior:

- upcoming emphasizes departure, readiness, and destination;
- live emphasizes current threshold and one current action;
- resolving compares scheduled with observed state;
- lived lets arrival, selected media, and Place relationship lead;
- remembered reduces the ticket into a transition within a larger history.

Avoid resembling a Wallet pass collection. Barcode, seat, terminal, gate, and
provider styling are transient evidence, not permanent identity.

### 8.2 Dwelling

**Semantic character:** center, radius, return, duration, inhabiting.

**Primary structure:** a centered base with the surrounding Place organized
relative to it.

Potential composition elements:

- base node or centered place label;
- stay/dwelling duration;
- neighborhood or nearby practical horizon;
- routes radiating outward and returning;
- companion presence when authorized;
- arrival and departure thresholds; and
- how the base shaped the Occasion after it is lived.

Avoid resembling a hotel-booking confirmation. Price, room type, access code,
and check-in instructions are phase-bound facts.

### 8.3 Gathering

**Semantic character:** people converging, shared core, plural layers,
authorship and audience.

**Primary structure:** shared Occasion core surrounded by separately governed
personal or relational layers.

Potential composition elements:

- Place/time/purpose shared core;
- inviter or organizer authorship;
- bounded participant treatment;
- arrival paths or preceding/following anchors;
- shared evidence;
- separate viewer-authored Outcome; and
- plural Outcome indicators without synthesized group sentiment.

Avoid a social feed or attendance trophy. A shared Occasion does not authorize
all media, meanings, constraints, or memories to become shared.

### 8.4 Encounter

**Semantic character:** something became perceptible, understandable, useful,
or open-ended.

**Primary structure:** focal subject + situated question/interpretation + open
edge back into the world.

Potential composition elements:

- real source or user media when useful;
- Place/material detail;
- question and grounded answer;
- practical distinction;
- authored meaning kept visibly separate from sourced interpretation;
- unresolved continuation; and
- optional relation to a later Occasion or thread.

Encounter should tolerate incompleteness. A translated menu, identified
building detail, or practical answer may expire without being forced into a
memory artifact.

## 9. Legacy projection-mode compatibility and target decomposition

The five landed mode names remain useful fixture and renderer identifiers, but
they must be interpreted through the Expression, Medium, and Projection Canon:

| Legacy mode | Target dimension |
| --- | --- |
| `compact` | density = `compact` |
| `standard` | density = `standard` |
| `timeline` | lead medium = `sequence`, normally standard or immersive density |
| `occasion` | surface context = `occasion`, commonly with the social modifier |
| `constellation` | relational modifier over an appropriate lead medium, with a complete list or sequence alternative |

The rules below remain compatibility requirements for the existing renderer.
They do not authorize the legacy union as the production medium ontology.

### 9.1 Compact density compatibility

Used in Chat, Home, Places context, and cross-surface previews.

Rules:

- one dominant statement;
- at most three facts;
- one primary and one ordinary secondary action unless a bounded decision
  contract explicitly requires otherwise;
- provenance summarized, not hidden;
- opens canonical owner/focused projection; and
- never becomes a miniature management workspace.

### 9.2 Standard density compatibility

Used in a focused sheet or owner projection.

Rules:

- full truthful fact hierarchy;
- source/provenance inspection;
- correction/forgetting controls;
- related Occasion/Place/Outcome context;
- origin-preserving Back; and
- no requirement for a standalone route.

### 9.3 Timeline / sequence compatibility

Used to show maturation and episodes across time.

Rules:

- time is the organizing axis, not card height;
- phase and transitions are legible;
- supporting artifacts may collapse under an Occasion;
- source duplicates do not appear as separate episodes; and
- undated/uncertain items live in an explicit unresolved region.

### 9.4 Occasion-context compatibility

Used to compose several accepted anchors around one bounded episode.

Rules:

- one shared core;
- operational, evidence, and Outcome roles remain distinct;
- Mine/Together layers are explicit;
- personal meaning never becomes group summary by aggregation; and
- the Occasion renderer references anchor resources rather than copying them.

### 9.5 Constellation / relational compatibility

Used for bounded exploration of an artifact neighborhood.

Rules:

- begin from one selected resource;
- show a small, explainable neighborhood;
- typed edges must be inspectable;
- do not render a global hairball;
- cap visible nodes and collapse supporting evidence;
- preserve a non-graph list/timeline alternative; and
- never imply causality or meaning from proximity alone.

## 10. Bounded relationship and organization system

### 10.1 V1 node kinds

```text
experience_anchor
occasion
place
outcome
receipt
source_ref (inspectable evidence, normally not a hero node)
plan (reference only when explicitly linked)
person_or_circle (authorized bounded summary only)
```

### 10.2 V1 predicates

```text
derived_from       SourceRef → Experience Anchor
anchored_to        Experience Anchor → Occasion
located_at         Anchor / Occasion / Outcome → Place
outcome_of         Outcome → Anchor / Occasion
receipt_for        Receipt → ResourceRef
part_of_plan       Anchor / Occasion → Plan
corrects           Correction/Outcome → prior claim/resource revision
supersedes         Resource revision → prior revision
shared_in_scope    Resource → bounded relationship/Circle scope
precedes           Resource → Resource, derived from explicit time
follows            Resource → Resource, derived from explicit time
```

Every edge carries:

```text
from ResourceRef
predicate
to ResourceRef
basis: explicit | observed | authored
viewer scope
source/provenance refs
valid_from / valid_until when applicable
confidence only for observed, non-authority edges
```

`inferred` is intentionally absent from V1.

### 10.3 Initial organizations

| Organization | Authority | Product use |
|---|---|---|
| Occasion | Accepted anchor links | Compose an episode instead of a card pile |
| Timeline | Explicit time windows and occurrence times | Show before/during/after and returns |
| Place | Canonical `EntityRef` | Reveal a person's relationship with a Place |
| Mine | Viewer ownership and private Outcomes | Personal artifacts and meanings |
| Together | Active membership and bounded sharing | Shared Occasion core and plural Outcomes |
| Lifecycle | Phase and unresolved state | Upcoming, live, resolving, remembered, needs correction |
| Source bundle | Intake lineage | One source producing several anchors without duplication |

### 10.4 Deferred organizations

Defer until explicit-link behavior is trusted:

- inferred themes;
- cross-Occasion narrative threads;
- cultural or practical concept clusters;
- similarity neighborhoods;
- automatically inferred recurring rituals;
- relationship trajectories; and
- global personal knowledge graphs.

An authored thread may be introduced earlier because it is an explicit human
claim. It still needs correction, privacy, and withdrawal.

## 11. Portfolio fixture program

### 11.1 Required canonical fixtures

| ID | Fixture | Semantic family | Default visual family | Required phases | Critical trust boundary |
|---|---|---|---|---|---|
| A01 | Plane boarding pass | Movement | Movement | upcoming/live/resolving/lived/expired | Ticket does not prove travel occurred |
| A02 | Train or ferry ticket | Movement | Movement | upcoming/live/lived | Provider status and occurrence remain distinct |
| A03 | Hotel confirmation | Base | Dwelling | upcoming/live/lived/remembered | Confirmation does not prove stay; access facts expire |
| A04 | Dinner reservation | Dining | Gathering | upcoming/live/resolving/lived | Reservation does not prove attendance or enjoyment |
| A05 | Live menu photograph | Attention or Dining | Encounter | live/expired/lived | Practical answer may expire without memory |
| A06 | Food photograph | Attention | Encounter or Gathering support | resolving/lived/remembered | Capture does not prove eating or liking |
| A07 | Museum/heritage ticket | Attendance | Gathering → Encounter | upcoming/live/lived | Ticket and encountered object remain distinct |
| A08 | Concert/rave ticket | Attendance | Gathering | upcoming/live/lived | Shared event does not imply shared meaning |
| A09 | Movie ticket | Attendance | Gathering → Encounter | lived/remembered | Prior media may be a bridge, not a fixed interest label |
| A10 | Book passage or reading note | Attention | Encounter | lived/remembered | Source, reading, and authored interpretation remain distinct |
| A11 | Building detail/sign/inscription | Attention | Encounter | live/lived/remembered | Identification and interpretation retain provenance |
| A12 | Companion photograph | Attention evidence | Gathering support | resolving/lived | No automatic identity, audience, or group meaning |
| A13 | Invitation/place perspective | Attention + Occasion role | Gathering | prospective/upcoming/lived | Human voice and recipient scope remain bounded |
| A14 | Receipt | Supporting evidence | Parent family/neutral | resolving/lived/expired | Purchase does not prove use or satisfaction |
| A15 | Changed gate/closure/entrance | Attention/operational evidence | Parent family | live/expired | Current observed fact must expire and reconcile |

### 11.2 Variant matrix for every relevant fixture

Each fixture must include the applicable variants:

```text
mine / together
source available / degraded / deleted
place resolved / candidate / unresolved
time resolved / wrong / stale
occurrence scheduled / likely / confirmed / contradicted / unknown
occasion unlinked / proposed / accepted / separated by correction
media strong / weak / absent
short copy / long copy
actions available / disabled / expired
standard width / 320 pt
normal type / xxxLarge Dynamic Type
light appearance / dark appearance if the production system supports both
offline cached / refreshed / stale
```

### 11.3 Cross-artifact compositions

The fixture portfolio must also prove:

1. flight + hotel + arrival observation;
2. dinner reservation + menu question + food photo + receipt + personal
   Outcome;
3. museum ticket + encountered object + prior movie/book connection;
4. invitation + two participants + private notes + one shared Occasion;
5. changed gate/closure superseding a prior operational fact;
6. one source containing several anchors without duplicating source custody;
7. source deletion after a lived Outcome; and
8. one correction propagating to timeline, Occasion, Place, and Life lab.

### 11.4 Fixture oracles

**Semantic oracles**

- unsupported fields remain unknown;
- phase does not imply occurrence;
- occurrence does not imply meaning;
- sharing does not broaden source access;
- deletion does not resurrect source content;
- personal Outcome remains viewer-owned; and
- expired operational facts do not remain current.

**Visual oracles**

- four family silhouettes are distinguishable without labels;
- all families still belong to one Vesper system;
- the source screenshot is not the permanent hero;
- sparse media remains attractive;
- provenance is reachable but not dominant;
- unknown and degraded states do not look falsely complete;
- the object visibly matures without becoming a new identity; and
- timeline/Occasion composition does not become a pile of equal cards.

**Interaction oracles**

- every action resolves through current authority;
- correction names a human claim, not internal ontology;
- Back preserves origin;
- deep links reopen the same resource/revision;
- Together does not expose private facts during action resolution; and
- offline/stale state cannot masquerade as a fresh operational fact.

### 11.5 Systematic circulation and Occasion-composition portfolio

The A01–A15 artifact fixtures test semantic and visual breadth. The following
experience portfolio tests the product grammar across audience, contribution,
phase, and authority boundaries. No row is the privileged loop from which the
architecture may be generalized.

| ID | Experience pressure | Required system behavior | Must not happen |
|---|---|---|---|
| E01 | Sorrento answer-only help | Decode or orient now; expire cleanly | Retention or sharing becomes the price of utility |
| E02 | Private menu, ticket, or photograph | Produce a sparse private artifact with source/correction controls | Capture implies occurrence, preference, or public meaning |
| E03 | Rome “back from Nice and Sorrento” Status | Human authors one featured share for friends or public audience; replace/expire/revoke | Vesper writes a biography, broadcasts live location, or creates a feed |
| E04 | “This made me think of you” handoff | Address a named person with provenance and human voice; recipient can ignore or respond | Share scope or relevance becomes intimacy or response debt |
| E05 | Brooklyn dinner contribution | Chat creates the Occasion and accepts a dish, late arrival, boundary, perspective, or task through typed contributions | Occasion profile homework or artifact-production requirement |
| E06 | Rome heat / live disruption | Reconcile current truth, authority, affected people, and one repair—or stay silent | Private reasons leak or one stale projection survives |
| E07 | Afterglow | Occasion-phase read composes Occurrence, selected traces, contributions, plural Outcomes, controls, and an optional continuation | New scrapbook owner or synthetic group meaning |
| E08 | Public Place perspective | Publish a bounded, attributable, correctable Place contribution | Universal rank, creator pressure, or private-source leakage |

Each row needs answer/decline/expiry, sparse evidence, correction, deletion,
wrong-audience, offline/stale, and second-occasion-or-silence variants where
applicable. Cross-cutting abstractions may be promoted only when this portfolio
shows that they preserve meaning across several rows.

The companion consequence blueprint owns the detailed choice allocation for
each row, M0-M6 authorization modes, no-homework rules, and the Rome, Brooklyn
dinner, and practical Place cross-surface storyboards.

### 11.6 Architecture and code delta from the portfolio

The current code proves a private Mine/Together artifact read path and a
separate, exploratory hosted-Occasion policy prototype. It does not yet provide
the circulation system described above.

**Backend/application delta**

1. Preserve `CanonicalArtifactProjectionV1` as a read projection over existing
   owners. Do not overload its `scope` field into a universal social command.
2. Define a storage-neutral, normally ephemeral prepared-consequence envelope
   that records the selected intent, proposed owner command, actor, affected
   principals, audience, M0-M6 authorization mode, authority basis,
   materiality, reversibility, preview, and expiry. It is not a new owner.
3. Define typed destination intents and preview/receipt envelopes for
   `address_person`, `share_with_audience`, `feature_share`,
   `contribute_to_occasion`, and `contribute_to_place`.
4. Resolve each intent through owner authority. A featured share needs an active
   audience grant/publication receipt; an Occasion contribution needs Occasion
   membership and typed contribution semantics; a Place contribution needs
   public-Place custody and moderation policy.
5. Model Occasion contribution as a union of ResourceRefs and typed state—not
   only artifacts: participation window, responsibility/Commitment, boundary,
   situated fact, perspective, evidence, and authored meaning.
6. Compile `OccasionPreview` and the afterglow as viewer-relative reads. The
   former must not reuse product Opening identity; the latter must not own
   sources, Occurrence, or Outcomes.
7. Keep `backend/core/hosted_occasion_projections.py` and its policy matrix
   experimental. Remove `EligiblePortraitFacet` from any ordinary product path;
   rename compatibility types only after callers and fixtures are mapped.
8. Add persistence only after command lifecycle analysis shows which existing
   grant, receipt, Occasion, Outcome, or contribution owner cannot express
   publish/replace/expire/revoke honestly. Do not start with a Status table.

**Mobile delta**

1. Reuse the universal input/capture affordance. Reveal destination choice only
   after expressed sharing intent or an invoked share affordance, then show the
   exact audience/consequence preview at the material boundary.
2. Render one featured-share/Status treatment on the person's chosen social
   face; mount it elsewhere only through viewer permission and relevance.
3. Add named-person Address/Respond treatment that preserves source and human
   authorship without manufacturing a message.
4. Add low-friction Occasion contribution actions in Chat and the Occasion
   object for artifact and non-artifact contribution types.
5. Render before/live/after from one Occasion lifecycle, including afterglow,
   instead of creating a standalone recap collection.
6. Keep public Place contribution separate from feeds, profiles, and creator
   ranking.

**Assurance delta**

- map E01-E08 to CJ and J branches before claiming implementation coverage;
- exercise M0-M6 authorization, explicit-language command admission, and
  prepare-versus-apply boundaries across the portfolio;
- add deterministic custody/authority matrices for every destination;
- prove create/replace/expire/revoke and stale-read behavior;
- prove other people's names, media, private constraints, and Outcomes never
  widen with the carrier; and
- run portfolio, API-contract, component, and native visual evidence as each
  layer becomes executable.

## Execution status — 2026-08-26

The first implementation pass has landed in the two child repositories. The
status below is intentionally evidence-bounded; a fixture gallery or pure
compiler test does not count as production mounting or native visual proof.

| Packet | Status | Evidence |
|---|---|---|
| Product grammar correction | documented, not implemented | E01-E08 now distinguish private artifacts, Status, Address, Occasion contribution, repair, afterglow, and public Place contribution; the consequence blueprint allocates M0-M6 choice and composes three cross-surface stories. No prepared-consequence runtime, circulation command, Status read model, generalized Occasion contribution, or public Place publication path has landed. |
| P0–P1 | partial | The strict projection contract, identity/resource rules, and A01–A15 fixture portfolio are drafted, but full seven-phase coverage and fixture-oracle validation remain open. |
| P2 | partial | The Intake-anchor compiler now has viewer-safe Mine/Together redaction, expiry filtering, stable revisions, and focused tests; Occasion, Outcome, and receipt adapters remain pending. |
| P3 | complete | Authenticated owner read route, operation-policy entry, OpenAPI snapshots, generated mobile schema, matching mock/real projection transport, and a read-only owner reader route are present; broader product mounting remains pending. |
| P4–P5 | partial | Shared mobile frame, family-specific structural cues, five legacy mode renderings, fixture gallery, component tests, and a registered dev-fixture QA contract are present; the canonical medium/density/context decomposition and native visual evidence remain pending. |
| P6 | partial | Phase-aware render profiles, source deletion/degradation, unknown-state parity, and Intake expiry are covered; full cross-surface correction and cached-view invalidation remain open. |
| P7 | partial | Client-only typed relation compilation, allowlisted predicates, scope filtering, provenance/basis, node cap, and list fallback are present; Outcome, receipt, Plan, and time-edge adapters remain open. |
| P8 | exploratory | The Life lab includes an episode-composition hypothesis, but accepted Occasion composition and role projections remain unimplemented. |
| P9 | partial | The read-only Life lab has Mine/Together, Timeline, Places, and bounded Constellation shells; accepted Occasion composition and shared episode semantics remain exploratory. |
| P10–P11 | pending by design | No production root, Chat mount, persisted theme edge, or semantic-thread promotion has been authorized. |

Native device capture remains pending because the local Maestro doctor could
not reach Metro on port 8081; the committed dry-run proves harness wiring only.

## 12. Execution dependency graph

```text
P0 Branch and doctrine reconciliation
  |
  v
P1 Contract + identity + portfolio freeze
  |-----------------------------|
  v                             v
P2 Backend pure adapters        P4 Mobile render kernel + static fixtures
  |                             |
  v                             v
P3 API + generated types        P5 Four family compositions + gallery
  |-----------------------------|
                |
                v
P6 Phase maturation + correction/degradation parity
                |
        |-------|--------|
        v                v
P7 Relationship compiler P8 Occasion composition
        |                |
        |-------|--------|
                v
P9 Read-only Life lab
                |
                v
P10 Cross-surface mounting and coherence proof
                |
                v
P11 Optional semantic-thread exploration and production decision
```

P2 and P4 may proceed in parallel only after P1 freezes the contract and
fixture semantics. P7 and P8 may proceed in parallel after P6. Production
mounting waits for the portfolio, not for one renderer screenshot.

## 13. Detailed execution packets

### P0 — Branch and doctrine reconciliation

**Purpose:** prevent artifact work from colliding with the current M0/M3
identity, multiplayer, OpenAPI, and mobile summary-card work.

**Tasks**

1. Inspect and assign every current uncommitted file across workspace,
   backend, and app.
2. Finish, commit, move, or deliberately preserve the current M0/M3 packet.
3. Confirm one Alembic head and clean OpenAPI/type sync.
4. Re-run M0 reachability and focused M3 tests.
5. Correct the systematic roadmap's remaining “one loop defines the seam”
   language.
6. Record this program as portfolio-first and projection-only.

**Do not** begin artifact contract code on top of ambiguous graph-schema or
generated-type drift.

**Exit gate**

- each repository has a known clean base or an isolated non-overlapping
  worktree;
- identity bindings and public `EntityRef` behavior are stable;
- current generated types match the committed OpenAPI projection; and
- the roadmap no longer frames one convenient first case as the architecture.

### P1 — Contract, identity, and portfolio freeze

**Purpose:** make the full-system assumptions executable before choosing UI
components or persistence.

**Tasks**

1. Write the canonical artifact identity ADR.
2. Define strict backend models for the projection, facts, media, actions,
   correction, scope, and destinations.
3. Define the fact-key registry and expiry rules.
4. Encode A01–A15 as static backend-neutral JSON/YAML fixtures.
5. Encode Mine/Together, deletion, correction, and forbidden-inference
   variants.
6. Define render-profile and relation-projection client contracts.
7. Add schema validation and fixture-oracle tests.
8. Map every projection field to an existing authority or mark it unavailable.

**Cancellation rule:** if a required field has no canonical owner, remove it
from V1 or write a separate authority decision. Do not add a convenience table.

**Exit gate**

- every field has an owner and privacy rule;
- all four visual families and all seven phases are represented;
- Mine/Together and source-deletion variants validate;
- fixtures require no production database; and
- no schema migration is proposed.

### P2 — Backend pure projection adapters

**Purpose:** prove canonical viewer-safe compilation without API or UI
coupling.

**Tasks**

1. Implement the adapter protocol and allowlisted resolver.
2. Implement Intake/graph Experience Anchor adapter.
3. Implement Occasion adapter.
4. Implement Outcome adapter.
5. Implement receipt adapter.
6. Implement revision hashing over normalized viewer-visible output.
7. Implement TTL filtering, source degradation, and unknown projection.
8. Implement Mine/Together redaction at compilation time.
9. Implement explicit owner destinations and action references.

**Focused tests**

- same input/time produces byte-stable normalized output;
- expired facts disappear;
- wrong viewer receives not found;
- Together never contains private claims or media;
- graph UUID is never exposed as Place identity;
- revoked Intake lineage degrades or removes projection correctly;
- correction changes revision and visible claims;
- no adapter writes a table or enqueues work; and
- malformed/legacy rows fail closed without breaking an entire collection.

**Exit gate:** A01–A15 compile from fixture owner reads through one strict
contract with no database migration and no raw source payload.

### P3 — Authenticated API and generated mobile contract

**Purpose:** expose one governed read seam.

**Tasks**

1. Add the authenticated allowlisted single-resource route.
2. Add route tests for resource kind, ID, scope, auth, not-found privacy, and
   validation.
3. Register API operation lifecycle and consumer posture.
4. Run workspace type sync.
5. Review full and app OpenAPI projections.
6. Add app transport and `data/` facade using generated types.
7. Add mock/real parity fixtures.

**Exit gate**

- contract sync passes;
- API operation audit passes;
- app never hand-copies the backend projection type;
- mock and real facade return the same contract; and
- only the bounded owner reader route consumes the endpoint; no broader product
  surface mounts it yet.

### P4 — Mobile render kernel and fixture lab scaffold

**Purpose:** establish shared semantics and primitives before family art
direction.

**Tasks**

1. Implement exhaustive render-profile resolver.
2. Implement fact-key formatting and TTL-safe display.
3. Implement shared artifact frame, status, provenance, action, unknown, and
   source-degraded primitives.
4. Implement legacy compact/standard/timeline/occasion/constellation
   compatibility containers with placeholder family bodies; do not promote
   those five keys into the canonical medium ontology.
5. Create a dev-only gallery consuming canonical static fixtures.
6. Register a `dev-fixture` surface contract and scenario manifest.
7. Add accessibility order and Dynamic Type scaffolding.

**Exit gate:** every fixture renders truthfully through the shared frame even
before bespoke family compositions exist.

### P5 — Four family compositions and visual portfolio

**Purpose:** create brand-coherent but semantically differentiated canonical
objects.

**Tasks**

1. Design and implement Movement composition.
2. Design and implement Dwelling composition.
3. Design and implement Gathering composition.
4. Design and implement Encounter composition.
5. Implement no-media, weak-media, long-copy, unknown, degraded, and expired
   states for each family.
6. Capture the full portfolio at standard width, 320 pt, and xxxLarge type.
7. Review complete shells, not isolated cards only.
8. Iterate against hierarchy, truth, family distinction, brand coherence,
   material health, and world-facing quality.

**Cancellation rule:** do not add a fifth family because one fixture is
awkward. First attempt a different phase emphasis, Occasion composition role,
or family morphology. A new family requires at least two materially different
retained artifacts that cannot compose honestly.

**Exit gate**

- all four families are visually distinguishable and recognizably Vesper;
- no source-specific renderer is required;
- sparse/no-media variants remain credible;
- accessibility and narrow-width captures have no clipping or action loss;
- visual verdict records concrete evidence limits; and
- no claim of runtime/persistence proof is made from the gallery.

### P6 — Phase maturation, correction, and degradation parity

**Purpose:** prove one object changes honestly over time and across trust
events.

**Tasks**

1. Render each relevant fixture through its phase sequence.
2. Add deterministic phase transition fixture controls.
3. Prove operational fact expiry.
4. Prove source deletion/degradation.
5. Prove Place/time/Occasion/occurrence/meaning/audience correction.
6. Prove revision and cached-view invalidation.
7. Prove the original source can recede while provenance remains inspectable.

**Exit gate:** the same resource identity visibly matures; correction and
deletion converge in every implemented mode; no stale operational fact remains
current.

### P7 — Explicit relationship compiler

**Purpose:** organize artifacts without a universal relation store.

**Tasks**

1. Implement typed relation models in client-only pure code or a bounded
   application read model.
2. Compile source, Occasion, Place, Outcome, receipt, Plan, and explicit time
   edges.
3. Attach basis, scope, provenance, and validity.
4. Implement bounded neighborhood selection and node caps.
5. Implement list/timeline alternative for accessibility and comprehension.
6. Add tests forbidding untyped or inferred V1 edges.

**Exit gate:** a selected artifact can explain why each visible neighbor is
present, and removing/correcting the canonical link removes the relation.

### P8 — Occasion composition

**Purpose:** turn several related artifacts into one coherent episode without
merging truth or privacy.

**Tasks**

1. Compose accepted anchor refs beneath an Occasion resource.
2. Assign operational, evidence, supporting-media, and Outcome roles.
3. Render one shared core and separate Mine/Together layers.
4. Collapse source duplicates and supporting evidence.
5. Test late join, leave/rejoin, removed source, private Outcome, and organizer
   correction.
6. Demonstrate the dinner, museum/movie/book, and invitation compositions.

**Exit gate:** one Occasion replaces a card pile while every underlying owner,
revision, audience, and correction path remains inspectable.

### P9 — Read-only Life lab

**Purpose:** explore how artifacts accumulate without prematurely approving
Life navigation or a new archive.

Initial lab views:

1. **Mine / Together** scope switch.
2. **Occasions** as episode compositions.
3. **Timeline** with phase and unresolved regions.
4. **Places** showing the person's relationship with canonical Places.
5. **Constellation** for one bounded selected neighborhood.

Do not initially add:

- algorithmic feed ranking;
- a global graph overview;
- country counts or achievements;
- automatic themes;
- generated biography;
- public profile;
- settings/account control dumping ground; or
- a permanent tab/root.

**Research questions**

- Can a new person explain what accumulated and why?
- Does Occasion composition feel more coherent than a timeline of fragments?
- Does Together preserve plurality rather than becoming a group scrapbook?
- Are practical artifacts as legible and attractive as cultural ones?
- Does a constellation reveal relationships or merely decorate them?
- Can people find and correct the claim they care about?
- Does the lab return attention to the world or invite archival maintenance?

**Exit gate:** founder/product/design review accepts at least one coherent Life
composition and rejects the archive/card-pile failure modes. This is not root
approval.

### P10 — Cross-surface mounting and coherence proof

**Purpose:** prove one canonical resource remains coherent across the whole
product.

Mount in controlled order:

1. compact Chat reference/readback;
2. focused artifact sheet;
3. Place-scoped compact relation;
4. Occasion composition;
5. read-only Life lab;
6. Home only when current relevance and attention authority justify it.

Chat integration should reference and refresh the canonical projection. Do not
turn `CardBlueprintV1` into the full artifact schema or duplicate canonical
facts inside a persisted Chat block when current owner readback is required.

**Cross-surface tests**

- same `ResourceRef` and revision everywhere;
- correction propagates everywhere;
- source deletion propagates everywhere;
- action resolves against the current owner revision;
- origin-preserving Back works from every entry;
- stale/offline views disclose their state;
- Together privacy holds across navigation; and
- no surface creates a shadow owner.

**Exit gate:** a user can encounter, inspect, correct, and revisit one resource
across the mounted product without seeing contradictory truth or duplicate
objects.

### P11 — Optional semantic threads and production decision

Only after P10:

1. Test user-authored threads.
2. Test model-proposed, explicitly labeled theme candidates.
3. Require source-bound reasons and easy correction/withdrawal.
4. Measure whether themes change later perception, action, or Occasion quality.
5. Decide whether any semantic edge merits persistence.
6. Decide whether Life becomes a root, evolves You/Atlas, or remains a
   projection reachable elsewhere.

No inferred theme becomes canonical merely because it makes a beautiful
constellation.

## 14. Validation program

### 14.1 Backend unit tests

- adapter mapping and allowlist;
- strict model validation;
- fact-key registry;
- deterministic ordering and revision;
- TTL filtering;
- source degradation;
- correction handling;
- resource not found/privacy;
- Mine/Together redaction;
- account deletion/export effects;
- malformed lineage fail-closed behavior; and
- no-write/read-only enforcement where practical.

### 14.2 Backend integration tests

- confirmed Intake candidate → graph anchor → canonical projection;
- source revoked after graph admission;
- anchor accepted into Occasion;
- occurrence evidence changing Occasion lifecycle;
- personal Outcome and correction;
- shared Occasion with two accounts and different private Outcomes;
- receipt/readback projection; and
- canonical Place binding/redirect.

### 14.3 Contract tests

- OpenAPI full snapshot;
- active-mobile projection;
- generated TypeScript;
- API operation policy;
- mock/real parity;
- backward-compatible nullability/defaults; and
- cross-repository fixture schema parity.

### 14.4 Frontend semantic tests

- exhaustive family resolver;
- phase emphasis;
- fact formatting;
- expired fact suppression;
- action availability;
- unknown/degraded treatment;
- relation compiler predicates and scope;
- bounded neighborhood caps;
- same-resource mode switching; and
- no transport imports from screen/component code.

### 14.5 Frontend component tests

- shared frame accessibility order;
- each family's primary structure;
- compact action limits;
- provenance and correction access;
- Mine/Together differences;
- no-media/long-copy/narrow-width states;
- offline/stale cue; and
- origin-preserving navigation contract.

### 14.6 Visual QA

Register the canonical artifact system as `dev-fixture` until production
mounting. Capture:

- A01–A15 representative states;
- all four families;
- phase sequences;
- no-media/degraded/unknown/correction states;
- 320 pt width;
- xxxLarge Dynamic Type;
- complete Chat/focused-sheet/Life-lab shells where applicable; and
- any supported appearance modes.

Visual verdicts must evaluate:

- family differentiation;
- one-system brand coherence;
- hierarchy and first viewport;
- truth and uncertainty;
- practical usefulness;
- source/media honesty;
- multiplayer plurality;
- accessibility resilience;
- motion restraint; and
- whether the interface remains world-facing.

### 14.7 Human product research

Use comprehension and consequence tasks rather than preference-only review:

1. What is this object?
2. What is known versus planned or uncertain?
3. What matters now?
4. What can you do?
5. Where did this fact come from?
6. Who can see it?
7. How would you correct it?
8. How is this related to the Occasion, Place, or another artifact?
9. Does the later form feel like the same object?
10. Did the connection make a real Place, practice, or cultural detail more
    legible?

Test both resonant cultural examples and ordinary practical examples. The
system fails if only the Odyssey/Rome or museum/book case feels meaningful
while movement, dwelling, food safety, navigation, repair, and social
coordination feel like generic utility cards.

## 15. Privacy, authority, and deletion matrix

| Event | Required behavior |
|---|---|
| Source retained privately | Mine may inspect; Together sees only separately authorized fields |
| Source shared selectively | Shared projection includes only selected fields/media, not original blanket access |
| Source deleted | Raw inspection disappears; unsupported claims are removed/degraded; allowed derived Outcome follows retention policy |
| Viewer leaves Occasion | Together access follows current membership/epoch policy |
| Personal Outcome corrected | Mine revision changes; shared Occasion truth remains unchanged unless separately corrected |
| Shared Occasion corrected | Every authorized shared projection invalidates; personal meanings are not overwritten |
| Place merged/redirected | Artifact resolves through canonical `EntityRef`; historical source identity remains provenance |
| Receipt reversed | Artifact shows reversal/current owner readback, not prior success as current |
| Account deleted | Owned private resources follow deletion; shared Occasion succession rules apply; no orphaned private media |

## 16. Offline, caching, and performance posture

### Offline

- Canonical projections may be cached as read models.
- Cached projections retain resource revision and fetched/validated time.
- Expiring operational facts are re-evaluated locally and visibly marked stale
  or suppressed.
- Offline actions queue only through existing governed command/outbox paths.
- A stale projection cannot authorize a mutation by itself.

### Performance

- Keep projections bounded and content-light.
- Do not embed raw source/media payloads.
- Memoize deterministic render profiles by resource revision + mode.
- Virtualize timeline and Life collections.
- Constellations render bounded neighborhoods, never the full corpus.
- Measure before adding a batch resolver or denormalized read store.
- Prefer root-specific read projection optimization over a generic graph query
  engine.

## 17. Telemetry and evaluation

Content-safe events may record:

- resource kind;
- projection schema version;
- phase;
- selected visual family/mode;
- Mine/Together scope;
- source degraded boolean;
- action kind and resolver state;
- correction entry/completion;
- owner-open success;
- projection compile/render latency;
- stale/offline state; and
- relation predicate counts.

Do not log:

- source content;
- extracted fact values;
- private authored meaning;
- participant identities;
- protected constraint values;
- media URLs; or
- model-generated narrative text.

Product evaluation should favor:

- comprehension speed;
- false-implication rate;
- correction success;
- cross-view coherence;
- later recognition;
- changed perception/action/capability;
- multiplayer safety; and
- quality of a second Occasion.

Avoid artifact-count, import-count, time-in-Life, constellation exploration,
and memory-volume goals.

## 18. Rollout posture

### Stage 0 — Static portfolio

The gallery remains fixture-only with no backend, persistence, or product data
read. Contract and visual exploration only.

### Stage 1 — Local authenticated projection

Read-only single-resource API against local data plus the owner reader route.
No broader product surface consumes the projection yet.

### Stage 2 — Private dogfood

Mine projection for explicitly retained source-derived anchors. No push,
sharing, or automatic memory.

### Stage 3 — Two-account Together dogfood

Bounded shared Occasion plus separate personal Outcomes. Signed-in two-device
evidence required.

### Stage 4 — Cross-surface read mounting

Chat/focused sheet/Place/Life lab consume the same canonical projection.
Actions remain existing owner-gateway actions.

### Stage 5 — Correction and deletion certification

Production-like source revocation, Place correction, Outcome correction,
membership change, and account lifecycle evidence.

### Stage 6 — Product-shell decision

Founder decides whether and where Life/artifact organization becomes a
production destination. The decision is independent from approval of the
projection/rendering system.

## 19. Feature flags and release controls

Do not add flags until a runtime consumer exists. When needed, flags must be
registered before merge and scoped separately:

```text
canonical_artifact_projection_read
canonical_artifact_together_read
canonical_artifact_life_lab
canonical_artifact_cross_surface_mount
```

Avoid one broad `ARTIFACTS_ENABLED` flag that mixes private reads, multiplayer,
Life navigation, and actions.

Every flag needs:

- owner;
- default;
- environment posture;
- exposure surface;
- rollback behavior;
- evidence gate; and
- review/retirement date.

## 20. Cancellation and anti-sprawl rules

Stop or redesign a packet if:

1. it requires a new durable owner merely to make rendering convenient;
2. a renderer needs source-specific API or schema fields;
3. a fifth family is justified by only one artifact;
4. the user must understand anchor-family vocabulary;
5. Together is implemented as Mine minus a few fields;
6. source deletion leaves unsupported confident facts;
7. a card blueprint becomes a universal UI DSL;
8. the constellation requires a global graph or inferred edges to feel useful;
9. Life becomes a feed, archive dump, or card wall;
10. a new route has no approved production consumer;
11. correction updates one view but not another;
12. operational facts survive their TTL;
13. beautiful output requires generated fake media or invented narrative;
14. the product rewards accumulation rather than changed experience; or
15. the first mounted case begins dictating the whole ontology.

## 21. Documentation changes required

The 2026-08-25 grammar migration reconciled Product Model, Multiplayer Product
Strategy, Surfacing Strategy, My World, the Experience Constitution, the hosted-
Occasion exploration, and the social-circulation hypothesis around these
decisions: Experience is the product unit; artifact is a carrier; Status is a
featured share; contribution exceeds media; Afterglow belongs to the Occasion
lifecycle; ordinary Occasion creation is chat-first; and generalized hosted
policy is deferred. The items below remain implementation and promotion work,
not an invitation to restore the superseded profile/facet model.

Before P1 implementation, reconcile these documents:

1. **Systematic Product-Engine Roadmap**
   - replace remaining “one artifact loop proves the seam” framing with a
     portfolio-safe seam exercised incrementally;
   - state explicitly that a first integration packet does not define ontology;
   - preserve the already-landed two-authority M1 receipt;
   - place this artifact program within Projection/Artifact/Destination and M6,
     with pieces beginning earlier as read contracts;
   - keep Life root approval separate.
2. **Artifact and Experience Anchor Grammar**
   - retain the four-family and fifteen-fixture decisions;
   - replace any now-completed prototype step with the next read-adapter and
     visual-system boundary;
   - preserve its no-universal-table warning.
3. **Experience Constitution**
   - do not change canon from visual prototyping alone;
   - preserve “screens own durable truth; conversation owns movement” while
     recognizing that an anchored artifact/focused sheet may itself be the
     canonical owner projection.
4. **Frontend surface contracts**
   - add a dev-fixture contract for the canonical artifact portfolio;
   - update Chat only when canonical artifact mounting occurs;
   - add Life only after its product contract is approved.
5. **Backend architecture**
   - document the read adapter boundary and lineage mapping once implemented;
   - do not describe the projection as a new graph authority.

At this working plan's expiry, promote stable pieces into:

- a cross-repository system contract for canonical artifact projection;
- backend model/API architecture;
- frontend artifact-system surface/design contract;
- accepted identity or Life decisions; and
- executable fixture/QA registries.

Archive the remaining execution narrative.

## 22. Decision register

| ID | Decision | Recommended answer | Must be resolved by |
|---|---|---|---|
| A-D01 | What is artifact identity? | The projected canonical `ResourceRef`; source-derived durable artifact uses graph Experience Anchor ID | P1 |
| A-D02 | Is a new artifact table needed? | No for P1–P10; reconsider only with demonstrated unmappable durable truth | Any schema proposal |
| A-D03 | Where does projection compilation live? | Application/read layer with owner adapters | P1 |
| A-D04 | Does backend select layout? | No; it sends strict semantics/authority only | P1 |
| A-D05 | Does CardBlueprint become universal? | No; remain Chat-specific | P1 |
| A-D06 | Which visual families ship? | Movement, Dwelling, Gathering, Encounter | P1/P5 |
| A-D07 | Which relations exist in V1? | Explicit/observed/authored allowlist only | P1/P7 |
| A-D08 | Are themes persisted? | No in V1 | P11 |
| A-D09 | Is Life a root? | Unresolved; read-only lab first | P9/P11 |
| A-D10 | How does graph anchor map to Intake lineage? | Reuse/expose deterministic bridge lineage; no new table unless lifecycle proof fails | P2 |
| A-D11 | What survives source deletion? | Only separately authorized derived truth/Outcome with degraded provenance | P1/P6 |
| A-D12 | What is the first production mount? | Decide after portfolio and Life-lab evidence; do not encode in architecture | P10 |
| A-D13 | What is Status? | One human-authored, audience-scoped featured-share projection; no new owner by default | Circulation contract |
| A-D14 | Does one composer imply one command? | No; Send, Address, Share, Occasion contribution, and Place publication remain typed consequences | Mobile/application design |
| A-D15 | What may be contributed to an Occasion? | ResourceRefs plus participation, responsibility, boundary, situated fact, perspective, evidence, and meaning | Occasion command design |
| A-D16 | Who owns afterglow? | Occasion lifecycle read over independently owned Occurrence, contributions, Outcomes, and permissions | Occasion projection |
| A-D17 | Is the hosted policy matrix P0? | No; named invitations and host membership control are the ordinary default; broad discovery/delegation remains experimental | Hosted Occasion review |
| A-D18 | Who chooses the consequence? | Vesper selects and prepares at most one candidate against silence; humans authorize meaning, audience, shared expectations, and external action through M0-M6 | Consequence fixtures and owner-command design |
| A-D19 | Do the five landed projection modes define one canonical enum? | No; retain them as compatibility renderer keys until a reviewed migration separates lead medium, modifiers, semantic role, density, and surface context | Render-profile migration decision |

## 23. First executable backlog

The next reviewable design packet should contain:

1. E01–E08 storage-neutral journey fixtures with M0-M6 authorization,
   prepare/apply boundaries, and negative branches;
2. destination-intent, audience-preview, and receipt envelopes for the five
   distinct circulation commands;
3. an authority map showing what existing owner would read or write every
   field, including replacement, expiry, revocation, and deletion;
4. a typed Occasion contribution envelope that includes non-artifact
   participation;
5. viewer-safe `OccasionPreview` and before/live/after Occasion projections;
6. mobile wire treatments for the common composer, featured Status, addressed
   handoff, Occasion contribution, and afterglow;
7. explicit treatment of the current hosted-policy prototype as exploratory;
8. CJ-to-J assurance mapping and portfolio oracles; and
9. an explicit compatibility map from each landed projection mode to lead
   medium, modifiers, semantic role, density, and surface context; and
10. a review decision about which seams belong in existing grants, receipts,
    and Occasion contracts before any schema or production surface is
    authorized.

That packet is systematic architecture work. It does not ask the organization
to bet the product on a single behavioral loop, and it does not require a
repository-wide noun migration.

## 24. Final engineering principle

The artifact system succeeds when it makes existing truth feel coherent,
beautiful, revisable, and alive across time and relationships.

It fails if “artifact” becomes another database noun, another collection to
maintain, another card taxonomy, or another excuse to expose internal
machinery.

The durable pattern is:

```text
authorities preserve truth
projections preserve viewer scope
visual families preserve experiential character
Occasions preserve episode coherence
relationships preserve inspectable context
correction preserves freedom
and the product returns attention to the world
```
