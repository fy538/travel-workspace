---
doc_type: working
status: active
owner: founder / product / engineering
created: 2026-08-21
expires: 2026-09-20
why_new: Provides the first revision-anchored cross-repository keep, refactor, build, quarantine, and deletion register for implementing the August lived-world thesis.
promotes_to: null
source_of_truth_for: [cross-repo-thesis-migration-audit]
supersedes: []
---

# Thesis Migration Register

## Decision in one sentence

Implement the lived-world thesis through a systematic target architecture
derived from the complete behavior portfolio, then migrate through bounded,
composable slices while human product proofs run in parallel. No single loop,
noun, or prototype is allowed to define the ontology by itself.

This is a cross-repository working audit. It classifies current capabilities and
recommends sequencing; it does not itself authorize deletion, schema changes,
production exposure, a new root surface, or a change to canonical product docs.

The accepted
[architecture/proof separation decision](../decisions/2026-08-23-separate-architecture-from-product-proof.md)
supersedes this document's former proof-first architecture rule. Product
evidence, architecture coherence, implementation conformance, and release
readiness are separate gates.

### Architecture and proof are parallel workstreams

The architecture must be reasoned across answer-only interactions, artifacts,
Place capability, solo and multiplayer Occasions, personal Plans, shared
Commitments, live adaptation, occurrence, plural Outcomes, later application,
correction, expiry, forgetting, and silence. Sorrento and Rome are useful
behavioral studies and integration fixtures inside that portfolio; neither is
the source of architectural truth or a prerequisite for systematic modeling.

Vertical slices remain the preferred way to land and verify the design. Their
role is to test composition, migration, and rollback—not to make the first slice
the permanent center of the product.

## 1. What changed, in implementation terms

The codebase contains three overlapping product strata:

1. **Travel workspace:** a concierge centered on Trips, itinerary generation,
   booking, expenses, story, and post-trip memory.
2. **Experience/Plan convergence:** Experience as the product unit; Plans and
   Trips as varying amounts of commitment structure; Places, Vesper, and
   multiplayer as one system.
3. **Lived-world thesis:** a relationship among person, people, and world;
   ordinary attention as entry; situated interpretation; authorized
   consequences; withdrawal and silence; and a later occasion improved by prior
   evidence.

The important migration is not primarily from `Trip` to `Plan` or from
`itinerary` to `Occasion`. It is from a product whose main output is a managed
travel artifact to a product whose repeated behavior is:

```text
fragment already connected to life
  -> immediate world-opening utility
  -> optional, authorized consequence
  -> truthful occurrence/outcome
  -> later judgment changed by prior evidence, or deliberate silence
```

Canonical support for this direction is in the Product Thesis and Product
Model. The more recent Occasion, Plan Shape, artifact grammar, and contextual
engine documents are bounded working or additive implementation authorities;
they do not authorize wholesale replacement of the Trip aggregate.

## 2. Audited baseline

Snapshot at the three repositories' `main` revisions on 2026-08-21:

| Signal | Observed state | Implication |
|---|---:|---|
| OpenAPI | 501 paths / 557 operations / 1,164 schemas | The public/server surface is much larger than a pre-launch thesis proof requires. |
| Database metadata | 264 registered tables | Schema breadth makes additive modeling cheap in the short term and expensive in the long term. |
| Alembic | 550 revision files | A clean pre-user baseline should be considered after the retained schema is decided. |
| Feature flags | 84 registered / 83 active | Flags are carrying product indecision as well as safe rollout. Fifty-eight active flags lack a thesis-journey field. |
| Governed API policies | 194 operations: 123 active, 58 retiring, 13 dark | There is already a retirement mechanism, but a large retiring set still carries maintenance cost. |
| Governed operations without consumers | 74 | Transport and substrate have outpaced adopted product behavior. |
| Atlas API | 49 operations | The retired destination remains a substantial compatibility and substrate domain. |
| Trip API | 242 operations under `/api/trips` | The old wedge still dominates the contract topology. |
| Intake v2 | 8 operations | The newest thesis-aligned entry boundary is comparatively small and coherent. |
| Backend lived-experience package | 46 Python files / about 10.7k lines | Strong contracts and tests exist, but the abstraction surface is already large relative to released behavior. |
| Backend Atlas + Discover packages | 41 Python files / about 8.7k lines | These cannot be deleted as route folders; useful memory, composition, and affinity code is imported elsewhere. |
| Frontend Atlas + Discover components/routes | about 90 TS/TSX files / about 19k lines | The destinations are retired, but much of their behavior is still re-exported under You and reused by Places. |
| Documentation governance | The focused spine, canon budget, release, links, compatibility, and surface checks pass. The full workspace check still fails on 107 pre-existing child-doc metadata issues and 6 unrelated unclassified workspace docs. | Canon convergence is complete for this migration; the broader lifecycle backlog remains separate cleanup work. |

The generated current-state document is stale relative to this snapshot: it was
last verified on 2026-08-13 and reports 538 operations and 81 flags. The v1
scope was originally locked on 2026-06-30 and remains centered on the prior
launch shape. The J01-J28 journey registry is valuable regression history, but
it is not an adequate build order for the August 18-21 thesis.

### Verification performed

- 76 focused backend tests covering intake custody/semantics, Plan Shape,
  Occasion capsules, contextual value, occasion projection, local closure, and
  second-occasion behavior passed.
- 14 focused mobile tests covering intake resumability, share capture, Occasion
  projection/gallery, and local-occasion transport/closure passed.
- All three new workspace documents pass new-document governance, and the
  living-doc link checker passes. The focused canonical checks pass. The full
  documentation suite remains red for the pre-existing metadata and inventory
  backlog summarized above.

This proves deterministic contracts. It does not prove user value, model
quality, live provider truth, physical-device behavior, or longitudinal value.

## 3. The most important finding

The new thesis is **better represented in contracts and fixtures than in the
current user-visible product**.

The repositories already contain most of the necessary primitives:

- source custody and provenance;
- Place identity and interpretation;
- privacy and audience scopes;
- canonical commitment and itinerary authority;
- proposals, mutation receipts, undo, and outcome evidence;
- context and situation compilation;
- treatment selection, hold, and silence;
- relationship memory and second-occasion models; and
- generated cross-repo API contracts and extensive regression harnesses.

But the user-visible causal chain is split:

```text
Vesper composer image
  -> immediate model answer
  -> chat image persistence
  -> optional legacy inbound tool path

OS share sheet
  -> intake-v2 custody
  -> semantic artifact candidate
  -> correction/retention receipt
  -> no answer to the person's question
  -> Done returns to Plans/Trips
```

The first path provides immediate utility without the strongest custody and
consequence model. The second provides excellent custody without the primary
product value. Joining them is a meaningful product and integration slice. It
does not determine whether a generalized contract is architecturally justified;
that decision belongs to the full portfolio and its ownership invariants.

There is also a concrete honesty defect in the current intake surface. Confirming
an interpretation changes the intake candidate status and records an owner
correction. It does not create a durable Thread, yet the screen can say the
interpretation is “now part of this private thread.” Until a real owner exists,
the copy should describe exactly what was retained.

## 4. Classification rules

Use these rules for every future audit decision:

| Disposition | Rule |
|---|---|
| **Keep** | Owns correct, durable truth; preserves trust; or satisfies an invariant required across the behavior portfolio. |
| **Refactor on path** | Valuable behavior exists, but one or more portfolio journeys cross a wrong boundary, duplicate path, misleading owner, or surface-specific policy. |
| **Build** | A missing link prevents an observable thesis claim from being tested end to end. |
| **Quarantine** | Potentially useful but not part of the current proof or launch promise; keep dark and stop expanding it. |
| **Retire/delete** | A destination, transport, projection, or abstraction has a named replacement, zero required consumers, and a tested deletion lane. |

A decision is incomplete without a trigger. “Keep for now” must name the event
that causes adoption, migration, or deletion.

## 5. Capability migration register

### 5.1 Durable foundations

| Capability | Disposition | Why | Next action / decision trigger |
|---|---|---|---|
| Authentication, owner identity, membership epochs | **Keep** | Required for private, shared, and viewer-relative authority. | Preserve; include denial and stale-membership cases in the first shared proof. |
| Place/entity identity, redirects, source observations | **Keep** | The thesis depends on stable world truth and revisable interpretation. | Use existing Place resolution; do not create an Occasion-specific place store. |
| Source custody, scan, idempotency, deletion | **Keep and adopt** | This is the strongest implementation of agency and epistemic separation. | Make intake v2 the source boundary for the first composer-image proof. |
| Itinerary operation gateway, ledger, proposal resolution, undo | **Keep** | Correct authority for consequential commitment changes already exists. | Retain as writer while Plan Shape remains an additive projection. |
| Participation, capability, and viewer-scope projections | **Keep** | Necessary for plural agency and private/shared separation. | Exercise through My/Together fixtures before broadening topology. |
| Action receipts, occurrences, outcomes, causal lineage | **Keep** | Makes consequences inspectable and later learning defensible. | Unify receipt grammar; avoid inventing a parallel “thesis receipt” store. |
| Context/situation providers | **Keep behind contracts** | Situated judgment requires fresh, scoped facts. | Adopt one real provider per proof; keep undeclared fields unavailable. |
| Generated OpenAPI projection and operation policy | **Keep** | Strong cross-repo discipline and retirement evidence. | Add thesis disposition and consumer intent to new operations. |
| Test fixtures, negative oracles, dogfood galleries | **Keep, demote as proof** | Excellent engineering evidence; not user evidence. | Label deterministic, device, model, and human evidence separately. |
| Privacy, correction, retention, public-egress checks | **Keep and strengthen** | Core product differentiation, not compliance garnish. | Add a thesis fitness suite rather than surface-specific copies. |

### 5.2 Refactor only where the proof crosses the boundary

| Capability | Disposition | Current mismatch | Refactoring seam |
|---|---|---|---|
| Composer images and chat-image storage | **Refactor first** | Immediate utility bypasses intake-v2 custody; an optional tool re-ingests through the legacy pipeline and can duplicate vision work. | Bind a pending chat turn to an intake submission/source object, then let the existing conversation consume that admitted source. |
| Share-capture result surface | **Refactor first** | It classifies/retains but does not answer; `Done` returns to Trips; confirmed copy can overstate durable ownership. | Reopen/continue the originating Vesper conversation; show exact custody, answer, retention, and correction state. |
| Intake semantic consequence proposals | **Refactor on adoption** | Generic proposals can be accepted in quarantine but no domain writer applies them; transport is already marked retiring without a consumer. | Choose one domain-specific consequence, route it through its existing writer, or remove the generic resolution endpoint. |
| Atlas memory substrate | **Extract, do not delete wholesale** | Retired Atlas namespaces own useful timeline, correction, affinity, and composition behavior imported by Trips, You, Places, and profile projection. | Rename/extract by owned invariant only when a current caller migrates; keep compatibility adapters thin. |
| Discover substrate | **Extract then retire feed** | Retired feed code still supplies types, telemetry, composition, and cache invalidation to Places/profile code. | Move Place-owned primitives first; delete feed/ranking paths only after caller and contract audits pass. |
| Three “what matters now” systems | **Converge incrementally** | Trips stack, Vesper workbench, and lived-experience composition can independently rank attention. | Introduce one decision/treatment seam; surface adapters retain rendering ownership. Shadow-compare before cutover. |
| Onboarding | **Replace behavior, not refactor** | Still asks for a travel/profile structure before demonstrating the broader relationship. | Test three doors: ask/bring something, operationalize a commitment, join someone. Do not rebuild ten states first. |
| Plan presentation | **Continue additive migration** | Canon says the Trip itinerary is operational truth; the newest working model treats itinerary as viewer-relative projection. | Keep the writer; validate Current Shape against real partial-overlap and local cases before changing canon. |
| Memory language and surfaces | **Refactor** | “Memory” mixes platform retention, source evidence, human remembering, recap, profile inference, and Atlas destination concepts. | Separate platform evidence/control from user-visible Place/Occasion continuity; keep You as whole-record control. |
| Chat artifacts | **Refactor when touched** | Many artifact renderers can become surface-specific mini-products. | Artifacts reference canonical owners and one consequence receipt; chat does not become a second writer. |
| Proactive notifications | **Refactor through arbiter** | Large policy substrate exists while broad delivery is dark. | Bounded evidence programs may generate Hold/Silence receipts; no push until the relevant human-value, interruption-cost, and release gates pass. |

### 5.3 User-visible evidence and integration links

These are the smallest missing links needed to make the current thesis
observable to people. They are not an exhaustive architecture backlog and do
not prohibit separately authorized work required by the systematic target
model.

| Missing link | Why it is necessary | Smallest acceptable form |
|---|---|---|
| One user-tested immediate world-opening response | Value risk is unproven despite extensive fixtures. | A menu photograph plus question tested with prospective users using the current model path before deeper architecture work. |
| Custody-bound conversation source | Joins the best product-value path to the best trust boundary. | One image, one owner, one personal conversation, one admitted source reference. |
| Exact consequence/expiry receipt | The thesis requires agency and visible non-action. | “Answered; original expires…” or an exact retained owner. No invented Thread or Occasion. |
| One optional durable consequence | Tests “carry it forward” without making retention mandatory. | Owner-confirmed source-bound Encounter/cue, or explicitly no durable consequence. |
| One later-occasion application | Tests whether continuity changes judgment rather than merely accumulating content. | A deterministic or dogfood second menu/cooking occasion with an inspectable prior evidence reference. |
| Human evidence register | Prevents engineering completion from standing in for product proof. | Session, observed behavior, quote/paraphrase, capability delta, confusion, retention choice, and follow-up outcome. |

### 5.4 Keep outside the current product release

These may contain reusable code, but should not compete for product attention or
receive product exposure merely because the architecture can represent them.
Architecture may preserve or design the necessary boundaries when the wider
portfolio requires them; activation and product investment require their own
strategy, human-value, and release decisions:

- live booking execution and broad provider automation;
- expenses and settlement beyond regression preservation;
- public story distribution, postcards, Unpacked, and anniversary engagement;
- generic public social discovery and generalized taste APIs;
- broad ambient/nearby feeds;
- live voice/narration as a separate modality program;
- full camera-roll mining and generalized background location;
- a public My World destination;
- a standalone Occasion persistence aggregate;
- generalized cross-Plan social topology;
- new memory galleries or generated identity narratives; and
- microservice decomposition or a universal relationship graph.

Quarantine means: default dark, no new product caller, security fixes and
regression preservation only, and a dated decision trigger.

### 5.5 Retirement and deletion lanes

| Lane | Delete only after | Likely retained kernel |
|---|---|---|
| Discover root/feed | Hidden routes, direct helpers, API consumers, types, telemetry, mocks, and Places imports have migrated. | Place identity, dossiers, source-aware interpretation, spatial browse. |
| Atlas product destination | You/Places callers no longer import Atlas presentation or domain names; compatibility deep links have metrics or an explicit pre-launch cutoff. | Evidence, correction, timeline/relationship projection, owner controls. |
| Generic intake proposal transport | One named domain writer consumes a typed proposal, or the experiment is rejected. | Intake custody and candidate correction. |
| Duplicate chat image ingestion | Conversation uses admitted intake sources and history rendering can read them. | Conversation attachment reference, not a second raw-source owner. |
| Lived-experience transitional abstractions | One production loop has selected the durable seam and no registered caller needs the migration wrapper. | Opening/treatment decision and receipt contracts that have real consumers. |
| Old v1 release manifest | A new thesis-proof release contract is accepted. | Regression lanes for still-retained Trip behavior. |
| Old migration history | Retained schema and any dogfood data migration are decided; environments can be rebuilt. | A single clean pre-launch baseline plus archived historical revisions. |

Do not delete legacy namespaces merely because their product name is retired.
The import graph shows that Atlas currently feeds composition, profile, Trip
projection, timeline, and Places behavior. Delete destinations first, extract
invariants second, delete substrate last.

## 6. Thesis fitness functions

Add these as executable checks where feasible and as review gates otherwise:

1. Source, observation, interpretation, occurrence, and meaning remain
   distinguishable.
2. A model may propose capability; policy and an existing domain owner grant it.
3. No commitment is created from a photograph, location point, or classifier
   result alone.
4. No shared projection reads owner-private context.
5. Immediate utility does not require Plan creation or retention consent.
6. Every durable consequence names owner, audience, evidence, reversibility,
   correction, and retention.
7. One opening yields at most one foreground treatment; Hold and Silence are
   valid decisions.
8. A surface cannot bypass the treatment arbiter by reading raw source evidence
   for its own proactive ranking.
9. Existing Trip/itinerary mutations continue through the canonical gateway
   until a superseding authority is explicitly accepted.
10. A second-occasion claim must cite the prior evidence and the changed
    judgment; resurfacing alone is not success.
11. Every active flag has an owner, target proof, cohort, safe-off behavior,
    and removal question.
12. Every new operation has a named consumer or a dated removal trigger.
13. Working product language cannot be presented as implemented truth.
14. A deterministic fixture, model evaluation, device run, and human outcome
    are separate evidence layers.

## 7. Coordinated operating program

### Track A — freeze the systematic architecture

1. Accept the complete behavior portfolio and cross-cutting invariants as
   architectural input.
2. Decide canonical ownership and lifecycle for Source Artifact, Experience
   Anchor, Plan, Occasion, Commitment, Occurrence, Outcome, Opening, and their
   viewer-relative projections.
3. Resolve where the current Trip/itinerary authority remains a specialization,
   where it becomes an adapter, and where the clean graph becomes authoritative.
4. Produce a portfolio matrix covering personal, pair, group, local, travel,
   live-change, second-occasion, correction, expiry, and silence cases.
5. Record explicit non-goals and rejected alternative topologies.

Architecture gate: every portfolio family has an owner, truth model, authority,
lifecycle, projection, correction path, and forbidden disclosure. This gate does
not claim user value or release readiness.

### Track B — migrate and integrate through bounded slices

Land independently reviewable slices against the accepted target architecture:

- custody-bound conversational sources and exact receipts;
- Plan/Occasion/Commitment lifecycle and multiplayer authority;
- viewer-relative personal and shared projections;
- Place relationship and capability projections;
- live condition, action, occurrence, and plural Outcome reconciliation;
- later application, correction, forgetting, and silence; and
- cross-surface treatment and canonical readback.

Each slice proves conformance, migration, replay, privacy, and rollback. Slices
may proceed in parallel when their ownership is stable. No slice acquires
architectural authority merely by landing first.

### Track C — run the human evidence portfolio in parallel

- Use the Sorrento menu study to test immediate utility, world-opening value,
  attention cost, uncertainty, and retention choice.
- Use the Rome couple study to test independent participant value, plural
  perception, practical relief, shared action, and withdrawal.
- Test group-travel creation, live repair, and participant-to-organizer
  distribution separately.
- Test later application against a control that lacks prior evidence.
- Test a bounded local expression for frequency and travel transfer.

Human-value gate: repeated observed behavior supports the intended capability
delta. Failure changes product priority, interaction design, or architectural
assumptions explicitly; it does not silently redefine storage or authority.

### Track D — converge surfaces and release claims

1. Bind product surfaces to canonical owners and remove misleading receipt copy.
2. Classify old J journeys as active product assurance, regression,
   compatibility, quarantined, or retired.
3. Give active flags a portfolio journey, cohort, safe-off behavior, and removal
   question.
4. Retire duplicate paths only after replacement, migration, and rollback
   evidence passes.
5. Claim only the evidence layer actually demonstrated: contract, local
   integration, device, provider, human, or production.

## 8. Work packet template

Every migration bet should fit on one page:

```text
Thesis claim:
Person and situation:
Observable capability delta:
Riskiest assumptions:
Existing owners reused:
Smallest end-to-end behavior:
Explicit non-goals:
Privacy and authority boundary:
Expected deletions or displaced paths:
Deterministic evidence:
Model evidence:
Device evidence:
Human evidence:
Failure and kill criteria:
Flag and removal date:
Decision date:
```

## 9. Decision docket

These decisions should be made with evidence; they should not be smuggled into
refactoring work:

1. Confirm the distinct roles of group travel as acquisition/distribution wedge
   and “bring something from life” as a first-use doorway; do not force one to
   replace the other.
2. Is Current Shape merely a better Trip projection, or the resting surface for
   local and partial-overlap Occasions too?
3. What durable owner receives a kept attention trace before an Occasion or
   Plan exists?
4. Which Atlas invariants are enduring platform memory, and which are retired
   product behavior?
5. Does the user ever browse My World directly, or is it an intelligence
   projection inside Places, Vesper, and You?
6. Does the full behavior portfolio require an independent Occasion aggregate,
   and which ownership/lifecycle invariants cannot be represented coherently
   without it?
7. Which old v1 capabilities are launch-critical regression promises versus
   merely completed code?

## 10. Research basis

The execution method follows several established practices:

- test specific product assumptions before complete implementation:
  https://www.producttalk.org/glossary-discovery-assumption-testing/
- tackle value, usability, feasibility, and viability risks early:
  https://www.svpg.com/four-big-risks/
- use fixed appetite and variable scope:
  https://basecamp.com/shapeup/1.2-chapter-03
- work in small, independently testable batches:
  https://dora.dev/capabilities/working-in-small-batches/
- insert seams and replace systems gradually:
  https://martinfowler.com/bliki/StranglerFigApplication.html
- allow old/new implementations to coexist during migration:
  https://martinfowler.com/bliki/BranchByAbstraction.html
- keep early architecture replaceable without sacrificing internal quality:
  https://martinfowler.com/bliki/SacrificialArchitecture.html

## 11. Evidence references

- `travel-agent/docs/product/Product Thesis.md`
- `travel-agent/docs/product/Product Model.md`
- `travel-agent/docs/product/What We Believe.md`
- `travel-agent/docs/working/current-product-and-effortless-shape-audit-2026-08-19.md`
- `travel-agent/docs/working/three-entry-longitudinal-product-simulations-2026-08-20.md`
- `travel-agent/docs/working/flexible-plans-occasions-and-personal-projections-2026-08-21.md`
- `travel-agent/docs/working/custody-first-ingestion-slice-2026-08-21.md`
- `travel-agent/docs/working/contextual-value-engine-v1-2026-08-21.md`
- `travel-agent/backend/api/routes/intake.py`
- `travel-agent/backend/inbound/semantic_interpreter.py`
- `travel-agent/backend/inbound/consequence_recipes.py`
- `travel-agent/backend/core/plan_shape.py`
- `travel-agent/backend/core/occasion_capsule.py`
- `travel-agent/backend/lived_experience/activation.py`
- `travel-app/app/share-capture/index.tsx`
- `travel-app/hooks/useConciergeHomeConversationEntry.ts`
- `travel-app/data/inboundItems.ts`
- `travel-app/docs/surfaces/canonical-entry-points.json`
- `docs/governance/api-operation-policy.json`
- `docs/flags/registry.yaml`
- `docs/release/v1-scope.yaml`
- `docs/journeys/product-proofs.yaml`
