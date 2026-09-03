---
doc_type: working
status: active
owner: product / backend / frontend
created: 2026-09-03
expires: 2026-10-03
why_new: Converts the current entity-system assessment into an executable cross-repository program without authorizing broad catalog backfill.
supersedes: []
---

# Entity System Next Program

> Proposed implementation program. This document does not authorize broad
> entity backfill, public rollout, or replacement of existing canonical owner
> systems. Founder review is required at the contract gates named below.

## 1. Outcome

Make one real-world object retain one canonical identity while its world facts,
viewer relationship, current situation, actions, outcomes, and corrections are
projected consistently into Chat, Home, Places, Plans, Life, Search, Map, and
the Experience Graph.

The program should prove this concrete arc:

```text
discover or receive a place
  -> resolve one canonical EntityRef
  -> save or add it to an explicit Plan
  -> confirm what happened for one participant
  -> record that participant's private Outcome
  -> show a materially different later object read
  -> safely apply or withhold that evidence on a later Occasion
  -> survive correction, merge, expiry, and deletion
```

The system is successful when a cold catalog product cannot produce the same
later read, while every displayed claim remains source-bound and correctable.

## 2. Architectural law

An entity is a stable reference and composition subject, not a universal row
that owns every kind of truth.

```text
ExternalRef / catalog row / canonical redirect
                    |
                    v
                EntityRef
                    |
       +------------+-------------+
       |            |             |
       v            v             v
   world owner  relationship   situation/Plan
   facts/status     owner          owners
       |            |             |
       +------------+-------------+
                    |
                    v
       viewer-relative Entity Presentation
                    |
       +------------+-------------+-------------+
       |            |             |             |
      Chat         Places        Plan          Life
```

Rules:

1. `EntityRef` is the only cross-surface place-like identity.
2. `ExternalRef` remains provider identity, never app identity.
3. Historical records retain their original subject and resolve through the
   redirect ledger at read time unless a separately reviewed mutation policy
   says otherwise.
4. Saves, Plans, Occurrences, Outcomes, and public facts remain different
   authorities. No projection may infer one from another.
5. The base entity read remains deterministic and performs no provider I/O or
   prose generation.
6. Live situation is a separate, expiring projection over explicit context.
7. Actions are capabilities delegated to their canonical owners; the entity
   system does not become a generic mutation gateway.
8. Missing evidence renders as absence or a typed unknown, never as generated
   filler.

## 3. Scope and non-goals

### In scope

- Canonical viewer relationship projection for catalog objects.
- Additive entity-presentation contract with relationship revision, evidence,
  and structured action capabilities, plus a separately expiring situation
  read.
- One complete planned/happened/outcome/later-read proof.
- Route-, Plan-, status-, and freshness-aware situation composition.
- Consistent entity action dispatch to Save, Plan, Chat, Map, and booking owners.
- Redirect, merge, correction, retraction, and deletion propagation tests.
- Resolution-review and entity-health operator tooling.
- Mobile migration for object pages and their exact return behavior.
- Mock/real parity, generated API types, accessibility, and device evidence.

### Explicitly out of scope

- Broad entity, hours, photo, dossier, or narrative backfill.
- A new universal entity table or entity event store.
- Replacing Search, Map, Places, Life, Plan, or Experience Graph ownership.
- Rebuilding the Home/Places v2 unit unions or semantic contribution producer.
- Automatic GPS-derived `visited` state.
- Generating a Take, brief, or interpretation when an object page opens.
- Treating an itinerary mention as attendance, or attendance as affection.
- Expanding accommodation and experience provider materialization before their
  lifecycle and source policies are explicitly approved.
- Making embeddings or generated prose canonical truth.

## 4. Concurrent-work boundary

The active Strategy task owns Source attachment and generated Source
contribution into Home and Places. This program must not modify:

- `backend/root_projection/v2/source_contribution_*`
- the semantic Home/Places contribution producer or its evaluation corpus
- the Home/Places v2 unit unions and native state renderers
- `docs/working/vesper-product-system-build-program-2026-09-01.md`

This program may expose canonical entity, relationship, and situation adapters
that those roots consume later. Integration happens only through their public
owner-read or adapter contracts.

## 5. Current implementation baseline

### Strong substrate to preserve

- Canonical type vocabulary: `backend/core/entity_types.py`.
- Identity and provider mapping: `backend/core/models/entity_identity.py`,
  `backend/core/db/entity_identity.py`.
- Redirect resolution and reversible merge ledger:
  `backend/core/db/entity_redirects.py`, `backend/core/entity_merge.py`.
- Public envelope and authenticated presentation:
  `backend/core/models/entity_envelope.py`,
  `backend/core/models/entity_presentation.py`,
  `backend/places/entity_presentation_read.py`,
  `backend/api/routes/entities.py`.
- Generic saves: `backend/core/db/saves.py` and `entity_saves`.
- Plan identity for venue, site, and experience through itinerary blocks.
- Private correctable outcome records in
  `backend/core/db/experience_outcomes.py`.
- `PlaceRelationshipProjection` and lived-experience adapters.
- `RouteFact`, bounded `SituationEnvelope`, trip situation composition, and
  movement judgment.
- Mobile `routeForEntity`, entity resolution, save orchestration, shared object
  shell, and generated API contract.

### Gaps the implementation must close

1. The authenticated presentation's relationship reader derives saved,
   affinity, and venue encounters, but not planned state.
2. Confirmed encounter queries are venue-only even though itinerary blocks can
   bind venues, sites, and experiences.
3. `PlaceRelationshipProjection` and `EntityRelationshipPresentation` are two
   partially overlapping projections with different semantics.
4. The canonical lived-experience provider currently maps the `loved` affinity
   marker through a parameter named `saved`; that semantic ambiguity must be
   removed before reuse.
5. The outcome writer is attached to a generic itinerary block but projects
   only `venue_id`; it can gain a canonical `EntityRef` without changing the
   underlying outcome table.
6. The presentation contract contains `planned` and `situation`, but the main
   object-page composer currently populates neither.
7. The presentation action vocabulary is broader than its composer; today the
   composer advertises only save/unsave and map.
8. Site uses the shared `EntityObjectPage`; venue remains bespoke and uses the
   shared presentation mostly for Take and display policy.
9. Redirect reads are forward-only. A canonical target projection needs a
   bounded alias-set read so historical evidence on a merged source is not lost.
10. Merge effects directly cover saves and external identities. Cross-surface
    projection behavior for Plan, outcome, graph, search, and cached reads is
    not certified end to end.

## 6. Target contracts

### 6.1 Canonical relationship projection

Evolve the existing relationship projection additively. Do not create a third
relationship model.

```python
class EntityRelationshipProjection:
    contract_version: Literal[2]
    viewer_id: UUID
    entity_ref: EntityRef
    states: frozenset["saved" | "planned" | "lived" | "skipped"]
    evidence: tuple[RelationshipEvidence, ...]
    encounter_count: int
    last_lived_on: date | None
    active_plan: RelationshipPlanSummary | None
    latest_private_outcome: RelationshipOutcomeSummary | None
    affinity_label: str | None
    projection_revision: str
    generated_at: datetime
    valid_until: datetime | None
```

Required semantics:

- `saved`: exact active `entity_saves` row for the viewer.
- `planned`: an active canonical Plan commitment for this entity and viewer.
- `lived`: confirmed personal participation with `occurrence_state=happened`.
- `skipped`: explicit personal or canonical skipped evidence; never inferred
  from the absence of `happened`.
- `latest_private_outcome`: only the viewer's active outcome, never a group
  aggregate or another participant's prose.
- `affinity_label`: explicit/derived affinity under its own authority; it does
  not add `saved` or `lived`.
- Corrections and retractions remove active evidence while preserving content-
  free audit lineage.

`face` may remain temporarily in the mobile presentation as a compatibility
field, but the new UI must render from the state set. Multiple true states can
coexist: “Visited twice · Saved · On Kyoto plan.”

### 6.2 Entity presentation v2

Add fields without replacing the existing endpoint during migration:

```python
class EntityDetailPresentationV2:
    revision: Literal["entity-detail-v2"]
    entity: EntityEnvelope
    categories: list[EntityPresentationCategory]
    facts: list[EntityPresentationFact]
    relationship: EntityRelationshipProjection
    take: EntityPresentationTake | None
    interpretation: EntityInterpretationProjection | None
    capabilities: list[EntityActionCapability]
    dependency_revisions: tuple[EntityPresentationDependency, ...]
    treatment: SurfaceTreatmentProjection | None
```

An action capability carries:

- `kind`: save, unsave, add_to_plan, ask_in_chat, open_map, book,
  record_outcome, or correct_outcome;
- `owner`: save, plan, chat, map, booking, or outcome;
- `availability`: available, needs_context, unavailable;
- `required_context`: for example `trip_id`, `day_id`, or fresh location;
- `reason_code`: machine-readable and non-editorial;
- optional destination metadata, never an unvalidated provider URL.

The presentation endpoint remains a private, request-snapshot database read.
It must not fetch Google, routing, weather, or availability live. The mobile
screen composes the separate live-situation response into its reserved
situation region rather than persisting it inside the durable presentation.

### 6.3 Live entity situation

Use a separate authenticated no-store endpoint because location and live facts
have different privacy, latency, and expiry behavior from the object read.

```http
POST /api/me/entities/{entity_type}/{entity_id}/situation
```

Request, all optional except the intended use:

```json
{
  "intended_use": "object_page",
  "trip_id": null,
  "origin": {
    "lat": 0,
    "lng": 0,
    "accuracy_m": 0,
    "observed_at": "..."
  },
  "travel_mode": "walking"
}
```

Response:

- canonical entity ref and redirect receipt identity;
- `evaluated_at` and a `valid_until` bounded by the shortest source TTL;
- zero or more source-bound predicates for status, route, weather,
  availability, and Plan timing;
- one deterministic display summary or typed silence reason;
- material unknowns and unavailable-source codes;
- situation-specific capabilities such as directions or leave-now;
- no retained precise viewer location.

Initial release supports Plan context and a fresh `RouteFact`. Weather and
availability enter only through existing source-specific owners and TTL rules;
they must not delay the first vertical slice.

### 6.4 Redirect-aware evidence reads

Add one bounded helper that returns the visible active source aliases resolving
to a canonical target for a viewer. Relationship and outcome readers use the
canonical ref plus this alias set. Do not rewrite historical Plan blocks or
outcomes merely to make projection queries easier.

The helper must:

- enforce global versus owner-scoped redirect visibility;
- bound traversal and reject cycles;
- return a stable revision/fingerprint;
- exclude reversed redirects;
- support batch lookup;
- never reveal another owner's provisional identity.

## 7. Implementation phases

Each phase should land in small commits and leave both repos green. Backend API
changes are `contract-sensitive`; relationship primitive changes require the
founder contract gate. Mobile adapter changes are `parity-sensitive`; route or
surface-shape changes require founder and surface-contract review.

### Phase 0 — Contract lock and characterization

**Goal:** freeze semantics before changing projection code.

Backend work:

1. Add focused characterization tests for today's entity presentation:
   new, saved, affinity-only, lived venue, site without encounter, redirect,
   owner-provisional visibility, and retracted Take.
2. Add tests proving today's missing behavior: planned is not projected,
   site/experience occurrences are not counted, situation is absent, and
   action capabilities are incomplete.
3. Add a decision amendment defining the canonical relationship projection,
   state precedence, privacy, and alias-read policy.
4. Record the API evolution as additive v2, not an in-place semantic rewrite.

Mobile work:

1. Characterize venue and site object routes, save behavior, exact return,
   loading/error/not-found, and mock/real parity.
2. Snapshot the current `EntityObjectPage` relationship copy and the venue
   page's bespoke relationship omissions.

**Exit gate:** contract reviewed; all characterization tests green; planned
failures are explicit tests or TODO-scoped assertions, not undocumented gaps.

**Suggested commits:**

- Backend: `test(entity): characterize relationship and presentation seams`
- Mobile: `test(entity): pin object-page parity and return behavior`
- Workspace: `docs(entity): lock relationship and presentation v2 semantics`

### Phase 1 — One canonical relationship reader

**Goal:** replace overlapping relationship composition with one viewer-safe
projection assembled from current authorities.

Backend work:

1. Move or re-export the relationship contract from a shared model location;
   preserve imports from `backend.lived_experience.place_relationship` during
   migration.
2. Introduce typed source readers:
   - generic save reader over `entity_saves`;
   - Plan reader over itinerary blocks for venue/site/experience;
   - accommodation Plan reader over `trip_accommodations` only when its chosen
     state is explicit;
   - confirmed occurrence reader over block participation;
   - private outcome reader joined through the block's canonical entity ref;
   - affinity reader that retains its exact label.
3. Add a single batch projection function accepting viewer, entity refs,
   optional Trip scope, one database snapshot, and one clock.
4. Add alias expansion before reading historical Plan and outcome evidence.
5. Update the lived-experience canonical provider and Places adapters to call
   the same projector.
6. Remove the `loved -> saved` parameter ambiguity. Loved remains an affinity;
   only an actual save row yields `saved`.
7. Keep accommodation lived state absent until an explicit stay occurrence
   authority is identified; do not infer it from dates passing.

Tests:

- all four catalog kinds for saves;
- planned venue/site/experience and chosen accommodation;
- participant happened versus group happened versus explicit absence;
- outcome owner isolation and retraction;
- saved + planned + lived coexistence;
- affinity without save;
- redirected historical source evidence;
- owner-provisional isolation across two users;
- batch-query characterization to prevent N+1 regressions.

**Exit gate:** object presentation and lived-experience adapters receive the
same state/evidence/revision for the same viewer/entity/snapshot.

**Suggested commits:**

- `feat(entity): add redirect-aware relationship source readers`
- `feat(entity): compose one canonical viewer relationship`
- `refactor(lived-experience): consume canonical relationship projection`

### Phase 2 — Outcome-backed later entity read

**Goal:** make a confirmed encounter and private outcome change a later object
read without leaking group or private details.

Backend work:

1. Add canonical `entity_ref` to outcome models and summaries while retaining
   `venue_id` as a compatibility field.
2. Derive the ref from the itinerary block's one-of venue/site/experience
   columns; reject unlinked/name-only blocks for relationship outcome use.
3. Keep the existing personal-participation guard and idempotent correction
   behavior.
4. Project only bounded outcome values into entity relationship reads:
   verdict, updated time, correction capability, and evidence reference.
   `noticed`, companion roster, and private rationale do not appear on shared
   surfaces.
5. Ensure later-Occasion applicability consumes the same canonical ref and
   withholds companion evidence unless roster applicability passes.
6. Add explicit correction and retraction readback tests.

Mobile work:

1. Add a compact relationship module to the object page:
   encounter count/date, current Plan membership, save state, and private
   verdict when present.
2. Link to the owning Occasion or Plan only when a valid route target and
   audience permit it.
3. Expose “Update your reflection” or “Correct this” only through the existing
   outcome owner; do not implement an entity-local free-text memory writer.
4. Invalidate entity presentation, Places, Life/You, and relevant Plan queries
   after an outcome mutation.

**Vertical-slice fixture:** one user, one canonical venue, one accepted Plan
placement, one confirmed personal occurrence, one `would_repeat` outcome, and
one later trip where the applicability decision changes the private read.

**Exit gate:** the before/after entity response changes deterministically; a
second participant sees the shared occurrence allowed to them but never the
first participant's private outcome.

**Suggested commits:**

- `feat(outcomes): project canonical entity identity from confirmed blocks`
- `feat(entity): include private outcome in relationship read`
- `feat(app): render outcome-backed place relationship`

### Phase 3 — Entity presentation v2 and object-page convergence

**Goal:** give every catalog object one common read grammar while preserving
kind-specific content and actions.

Backend work:

1. Add v2 models and response route or explicit version negotiation.
2. Populate canonical relationship v2 and structured capabilities.
3. Keep v1 available until all mobile consumers migrate.
4. Resolve redirects once at the envelope boundary and pass the effective ref
   to every downstream reader.
5. Add response revision, dependency revisions, and `Cache-Control: private`
   policy appropriate to viewer-specific content.

Mobile work:

1. Regenerate OpenAPI and TypeScript types through the workspace sync flow.
2. Add a v2 data adapter in `data/entities.ts`; screens never import the API
   directly.
3. Evolve `EntityObjectPage` into composable common regions:
   identity/status, relationship, Take/interpretation, durable facts,
   situation slot, owner-dispatched actions, map, and kind-specific tail.
4. Migrate venue in steps rather than replacing its whole mature page at once:
   - relationship and capabilities;
   - shared status/fact formatting;
   - shared situation slot;
   - shared action dispatch;
   - retain venue-only dossier, exact photo, booking, narration, and planning
     modules as typed slots.
5. Keep site on the shared page and add deliberate accommodation/experience
   adapters. Do not force accommodation into itinerary-block mechanics.
6. Preserve hero-first chrome and exact Places/Home return tokens.

Tests and QA:

- schema generation and contract diff;
- v1/v2 parity for existing fields;
- mock/real adapter parity;
- venue/site/accommodation/experience object states;
- redirect route and owner-provisional page;
- surface QA against the Places contract, including Dynamic Type,
  VoiceOver/TalkBack order, loading, retry, and not-found.

**Exit gate:** all four object types can render from v2; venue no longer creates
its own relationship semantics; v1 has zero mobile consumers before removal.

**Suggested commits:**

- Backend: `feat(api): add entity detail presentation v2`
- Workspace/mobile: `chore(api): sync entity presentation v2 types`
- Mobile: `feat(entity): add shared relationship and capability regions`
- Mobile: `refactor(venue): consume canonical entity presentation`
- Mobile: `feat(entity): add accommodation and experience presentation adapters`

### Phase 4 — Bounded live situation

**Goal:** answer “what matters about this object now?” without contaminating
durable identity or making the base page wait on providers.

Backend work, in order:

1. Implement a Plan-only situation composer from a validated Trip scope and
   current Plan revision.
2. Add `RouteFact` using the existing routing gateway, explicit recent origin,
   requested mode, and provider-use policy.
3. Join adjudicated operating status and stored hours with independent source
   clocks. Never infer `open_now` from unstructured hours in this layer.
4. Add weather or availability only after an existing owner can supply a
   source ref, observation time, expiry, and use authorization.
5. Bound the response's validity by its shortest dependency and return typed
   silence when no decision-changing predicate survives.
6. Mark the endpoint no-store and verify that origin coordinates do not enter
   logs, receipts, analytics, or durable tables.

Mobile work:

1. Fetch base presentation immediately.
2. Fetch situation independently only when context and permission exist.
3. Render no more than one leading “Now” judgment and one quiet source/freshness
   disclosure; operational detail stays behind tap where appropriate.
4. Remove the line when expired rather than wearing a stale face.
5. Offer retry only for a requested live read; absence is not an error.

Tests:

- no trip/no origin produces typed silence;
- trip membership and Plan revision validation;
- fresh, expired, degraded, and provider-disallowed RouteFact;
- source clocks bound the response TTL;
- no location persistence or telemetry leakage;
- partial source failure still returns valid surviving predicates;
- process death and refetch never resurrect stale situation copy.

**Exit gate:** one real route situation renders on a physical device and
disappears or degrades at expiry; the base entity page remains usable offline.

**Suggested commits:**

- `feat(entity): add plan-scoped situation projection`
- `feat(entity): add policy-aware route situation endpoint`
- `feat(app): render expiring entity situation independently`

### Phase 5 — Canonical action and consequence wiring

**Goal:** make every displayed entity action truthful about its owner,
requirements, receipt, readback, and undo/correction behavior.

Action map:

| Capability | Canonical owner | Required readback |
|---|---|---|
| save / unsave | Save owner | relationship projection + Places/Atlas |
| add to Plan | Plan/itinerary operation gateway | Plan block + entity planned state |
| ask in Chat | Chat navigation/seed | immutable entity snapshot, no implicit write |
| open map | Map projection/provider policy | no relationship mutation |
| book | Booking/provider handoff | commitment/booking receipt + Plan |
| record/correct outcome | Outcome owner | relationship + Life + later applicability |

Backend work:

1. Capability builder advertises only actions valid for the entity kind and
   current context.
2. Existing domain command endpoints remain the writers.
3. Every consequential mutation returns or exposes an idempotent receipt and a
   canonical target ref.
4. Define dependency tags for cache invalidation and owner readback.
5. Add contract tests ensuring unsupported actions remain absent rather than
   disabled theater.

Mobile work:

1. Centralize entity capability dispatch in one typed utility/hook.
2. Delegate to existing `useSaveEntity`, Plan placement, Chat routing, map,
   booking, and outcome flows.
3. Use one post-action receipt treatment; do not persist success banners on the
   object page.
4. Refetch canonical owners after success or uncertain completion; never rely
   only on optimistic local state.
5. Preserve exact origin and return context across object -> Plan/Chat/Map and
   back.

**Exit gate:** a save and an add-to-Plan action both round-trip through their
owners and visibly update the same entity read. At least one uncertain/retry
case reconciles correctly after app restart.

**Suggested commits:**

- `feat(entity): advertise owner-bound action capabilities`
- `feat(app): dispatch entity actions through canonical owners`
- `test(entity): prove action receipt and owner readback`

### Phase 6 — Correction, merge, deletion, and operations certification

**Goal:** prove one correction reaches every relevant projection without
rewriting unrelated historical meaning or widening audience.

Backend work:

1. Add a projection-impact registry for entity redirect/correction events:
   envelope, relationship, status, Search, Places, Plan reads, Experience
   Graph binding, Life/You, content, and vector payloads.
2. Expand merge tests from direct mutation effects to read-projection effects.
3. Use alias-aware reads for historical Plan/outcome evidence; keep immutable
   artifacts and Chat snapshots historical unless their source is revoked.
4. Add explicit rules for source deletion versus entity deletion versus
   identity merge. These are not interchangeable operations.
5. Verify retraction removes private outcome application and any derived
   relationship affinity that depended solely on it.
6. Add idempotent replay and reversal tests after intervening writes.
7. Provide an operator CLI/read-only report for pending resolution reviews,
   duplicate candidates, unresolved redirects, stale facts, and provisional
   entity health. Do not build a general admin app in this phase.

Cross-surface certification matrix:

| Event | Search | Object | Places | Plan | Chat | Life | Graph |
|---|---|---|---|---|---|---|---|
| owner merge | canonical | canonical + receipt | canonical | resolves history | snapshot remains historical | canonical relation | canonical binding |
| reverse merge | restored | restored | restored | restored resolution | snapshot unchanged | restored relation | restored binding |
| unsave | unchanged identity | saved removed | removed from saved projection | unchanged | unchanged | attention removed | no invented outcome |
| outcome correction | unchanged | verdict updated | relationship updated | occurrence unchanged | unchanged | outcome updated | owner outcome updated |
| outcome retraction | unchanged | verdict absent | derived use absent | occurrence unchanged | unchanged | inactive/audit only | inactive/audit only |
| source deletion | identity may remain | dependent claims degrade | dependent units retract | commitments remain if independently owned | historical artifact marks unavailable | dependent composition retracts | lineage retained, content absent |

Mobile work:

1. Route all returned refs through `routeForEntity` after canonical resolution.
2. Invalidate affected queries from mutation receipts rather than screen names.
3. Render unavailable/deleted source states without deleting independently
   supported entity identity.
4. Verify exact return after a redirect changes while the app is backgrounded.

**Exit gate:** the matrix passes against real PostgreSQL and a real-backend
mobile run; no correction leaves mutually contradictory active projections.

**Suggested commits:**

- `feat(entity): expose redirect alias sets and projection impacts`
- `test(entity): certify cross-surface correction propagation`
- `feat(ops): report entity resolution and projection health`
- `fix(app): reconcile entity mutations by canonical dependency`

## 8. API and migration strategy

1. Prefer additive fields and v2 response models.
2. Keep v1 until generated-type and runtime telemetry prove no remaining
   consumers.
3. Phase 1 relationship generalization and Phase 2 canonical outcome refs can
   be read-model changes without database migration.
4. Add a migration only if tests prove an existing authority cannot be
   projected safely. Do not denormalize `entity_type/entity_id` into outcomes
   merely for query convenience before measuring the block join.
5. If a migration becomes necessary:
   - one Alembic head;
   - nullable/additive first;
   - no data backfill in this program;
   - old rows remain readable through the legacy join;
   - promotion requires an explicit later migration and quality report.
6. Run the workspace OpenAPI sync after every backend response change; never
   hand-edit generated TypeScript.

## 9. Validation program

### Backend minimum per phase

- focused unit tests for changed composers;
- API contract and authorization tests;
- redirect/privacy tests with two users;
- PostgreSQL tests for relationship, outcome, merge, and correction joins;
- `ruff check` and `ruff format --check` on touched files;
- offline suite for every commit group;
- one Alembic head if migrations are touched.

### Mobile minimum per phase

- Jest tests for data adapters, capability dispatch, route/return, and state
  rendering;
- TypeScript and API boundary checks;
- mock/real parity for every new relationship and situation state;
- Places surface scenario validation;
- native screenshots for venue/site/experience/accommodation state variants;
- Dynamic Type, VoiceOver/TalkBack, Reduce Motion, offline, and process-death
  checks before promotion.

### Required end-to-end scenarios

1. Provider result -> owner-provisional shell -> save -> reopen.
2. Existing entity -> add to Plan -> exact day -> planned relationship.
3. Plan block -> personal happened confirmation -> private outcome -> later
   entity read.
4. Two participants -> one shared occurrence -> two different private outcomes.
5. Source entity merged -> canonical page retains historical Plan/outcome.
6. Outcome corrected/retracted -> all active projections update.
7. Fresh route line -> expiry -> honest degradation.
8. Deleted Source -> dependent content disappears while independently supported
   identity and commitments remain.

## 10. Rollout gates

All new serving remains dark or dogfood-only until the relevant gate passes.

### Gate A — Semantic correctness

- no save/love/visit/meaning conflation;
- one canonical relationship projection;
- owner and audience isolation;
- redirect-aware evidence.

### Gate B — Contract parity

- OpenAPI and generated mobile types match;
- v1/v2 parity for unchanged fields;
- mock and real modes represent the same states.

### Gate C — Consequence closure

- save and Plan actions read back from owners;
- happened and outcome are separate;
- correction and retraction propagate.

### Gate D — Live honesty

- provider use is licensed for the display;
- every live predicate has observation and expiry;
- stale data loses action claims before visibility;
- precise origin is not retained.

### Gate E — Physical proof

- two real signed-in accounts;
- iOS and Android or an explicitly documented platform limitation;
- offline, backgrounding, process death, redirect, and exact return;
- surface verdict and accessibility evidence.

### Gate F — Expansion decision

Only after A-E may product decide whether to seed a small flagship entity pack.
Broad backfill remains a separate founder-approved program with its own cost,
freshness, provider-policy, and quality gates.

## 11. Metrics and operational evidence

Measure correctness and continuity, not catalog size:

- canonical resolution success and conflict rate;
- provisional shell creation and later verified-match rate;
- redirect depth and unresolved alias count;
- relationship projection completeness by entity kind/state;
- action capability shown -> attempted -> owner-confirmed -> reconciled;
- outcome capture/correction/retraction rate;
- later entity reads materially changed by prior authorized outcomes;
- situation availability, source mix, latency, and expiry degradation;
- stale fact suppressed versus incorrectly served;
- cross-surface projection mismatch count;
- operator review age and resolution outcome.

Do not optimize for number of entities, pages opened, saves accumulated, or
engagement with recommendation inventory.

## 12. Recommended execution order

```text
Phase 0 contract lock
    -> Phase 1 canonical relationship
    -> Phase 2 outcome-backed later read
    -> Phase 3 presentation/object convergence
    -> Phase 4 live situation
    -> Phase 5 action/consequence wiring
    -> Phase 6 correction and operations certification
```

Phases 4 and 5 may overlap only after Phase 3's capability contract is stable.
Phase 6 tests should be added incrementally from Phase 1 onward, but final
cross-surface certification comes last.

The first product checkpoint is the end of Phase 2. If a confirmed encounter
and explicit outcome do not make the later entity read meaningfully better,
pause before investing in live situation or broad object-page migration. That
is the earliest honest test of the entity system's differentiated value.

## 13. Definition of done

The program is complete when:

1. One canonical entity reference survives Search, object page, Plan, Places,
   Life, and Experience Graph reads.
2. The relationship projection distinguishes saved, planned, lived, skipped,
   affection, and private outcome without inference leakage.
3. Venue, site, experience, and accommodation render through one presentation
   grammar with explicit kind-specific differences.
4. A fresh situation can improve the entity page without blocking or polluting
   the durable read.
5. Entity actions delegate to canonical owners and reconcile through receipts.
6. Merge, correction, retraction, deletion, expiry, and process death have
   end-to-end evidence.
7. Two users can hold different private outcomes about the same shared
   occurrence without contradiction or exposure.
8. A second Occasion demonstrably benefits from prior authorized evidence or
   correctly withholds it.
9. No broad backfill was required to produce the proof.
