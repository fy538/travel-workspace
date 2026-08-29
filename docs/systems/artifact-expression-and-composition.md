---
doc_type: contract
status: active
owner: product / cross-repo architecture / frontend
created: 2026-08-29
last_verified: 2026-08-29
why_new: Defines how Artifacts and canonical truth become generated compositions, instruments, direct state expressions, or saved compositions without creating a universal generated-output owner or server-authored UI language.
source_of_truth_for: [artifact-composition-boundary, composition-lifecycle, agent-composition-boundary, cross-root-composition-projection]
---

# Artifact, Expression, and Composition

## Purpose

Vesper turns authorized evidence and canonical truth into value a person can
perceive, use, keep, correct, or share. This doctrine governs the boundary
between that truth, generated composition, native presentation, and optional
persistence.

It does **not** authorize a universal artifact table, a generic artifact writer,
a server-driven component tree, or a new root. Canonical domain owners retain
truth, action, audience, correction, and lifecycle authority.

This doctrine applies the product
[Expression, Medium, and Projection Canon](../../travel-agent/docs/product/Vesper%20Expression%2C%20Medium%2C%20and%20Projection%20Canon.md),
[Four-Root Loop, Object, and Surface](four-root-loop-object-surface.md), and
[Contribution and Consequence](contribution-and-consequence.md) to cross-repo
Artifact intake and composition implementation.

## One architecture

```text
authorized evidence and canonical truth
  -> one immediate job and dominant product move
  -> agent-authored claims and semantic composition brief
  -> evidence, authority, audience, and lifecycle admission
  -> one lead medium plus at most one supporting medium
  -> bounded semantic anatomy
  -> root-native renderer and accessible fallback
  -> ephemeral projection, direct state, instrument, or saved composition
  -> one durable owner and at most one authorized continuation
```

The governing rule is:

> **The agent composes meaning, not application components. The app renders a
> bounded semantic composition, not model-authored UI.**

## Distinct units

| Unit | Meaning | Durable? |
| --- | --- | --- |
| **Source** | Identified evidence with provenance, custody, audience, and reuse rights | Yes, under Source custody |
| **Canonical object** | The owner of world, personal, social, plan, commitment, occasion, or outcome truth | Yes, under its domain |
| **Artifact** | A human-facing thing brought, captured, received, or made: photograph, ticket, receipt, note, message, film, book, link, recording, or document | Under Source custody when admitted |
| **Composition** | A viewer-safe return Vesper generates or assembles from Sources, Claims, and canonical objects | Ephemeral by default |
| **Composition brief** | Validated semantic intent: job, claims, represented resources, media constraints, modifiers, audience, freshness, lifecycle, and consequences | Ephemeral by default |
| **Projection** | A viewer-, root-, density-, and moment-relative expression of the same identity | Normally read-time |
| **Instrument** | Stateful expression tied to current truth, manipulation, or consequence | Its owner/state persists; its UI does not |
| **Direct state expression** | A row, marker, label, or transition that makes canonical state useful without composition ceremony | No separate composition |
| **Saved composition** | A deliberately retained, versioned composition with an exact content snapshot and dependency manifest | Yes, only after a retention trigger |

An article, guide, reconstructed journey, audio brief, podcast, comparison, or
social mosaic is a composition **format**. A card, row, sheet, page, band, or modal
is a container or delivery channel. Neither is a canonical truth owner.

## Responsibility boundary

| Layer | Owns | Must not own |
| --- | --- | --- |
| **Canonical domains** | Resource identity, truth, revision, occurrence, audience, custody, action authority, correction, deletion | Presentation geometry or generated narrative hierarchy |
| **Agent** | Candidate claims, distinctions, explanations, evidence roles, immediate job, preferred and allowed media, optional continuation | Component names, styles, coordinates, route strings, mutation payloads, permission expansion |
| **Admission and composition compiler** | Evidence threshold, known-to-person novelty, authority, audience, freshness, lead/support medium coherence, semantic anatomy, safe action references | Unvalidated factual invention or client geometry |
| **Native client** | Renderer registry, density, geometry, typography, imagery, interaction, accessibility, environment degradation, root-native composition | Inferring occurrence, widening audience, inventing owner actions |
| **Saved-composition owner** | Version, exact saved expression, dependency manifest, audience/use grant, correction and invalidation lineage | Copies of canonical truth or live provider state presented as frozen fact |

The backend or application layer may send semantic section identity, ordered
claims, Source and Resource references, allowed actions, freshness, and a bounded
preference or fallback family. It must not send React Native component trees,
arbitrary `custom` blobs, typography, spacing, coordinates, gestures, or client
navigation instructions.

## Composition brief contract

The first fixture-only `CompositionBriefV0` contract is implemented in
`travel-app/utils/compositionBrief.ts`, with A01 editorial and A06 live
instrument fixtures. It is not an API payload or production writer. A present
brief contains:

- schema version and composition identity for the current evaluation;
- immediate job and dominant product move;
- represented Resource references and revisions;
- claim-local evidence, Source references, and source roles;
- semantic role;
- one lead medium and at most one supporting medium;
- social, relational, and quantitative modifiers when applicable;
- bounded composition format or semantic anatomy when one is earned;
- viewer/audience scope, use grant, authority ceiling, freshness, and expiry;
- zero or one authorized continuation with an opaque capability reference;
- lifecycle intent: ephemeral, candidate-to-save, saved, shared, or live;
- correction owner, exclusions, and invalidation requirements; and
- a complete textual/accessibility alternative.

`quiet` is absence of an authored composition, not a seventh medium. Social and
relational are modifiers. Editorial and receipt are semantic roles. Article,
guide, reconstruction, and podcast are formats. Compact, standard, and
immersive are projection densities.

## Structured formats, dynamic composition

Vesper uses bounded anatomy rather than a universal block DSL or one page per
object type.

| Format | Required semantic anatomy | Common lead media |
| --- | --- | --- |
| **Bounded article** | contribution, claim, support, mechanism or distinction, optional continuation | prose, evidence, comparison |
| **Reconstructed journey** | represented interval, ordered events, gaps/unknowns, occurrence states, supported conclusion | sequence, spatial, evidence |
| **Comparison** | common axis, two or three cases, honest differences, decision or implication | comparison, evidence |
| **Guide** | orientation, bounded possibilities, constraints, current truth, handoff | spatial, comparison, prose |
| **Social juxtaposition** | attributed human contributions, substantive common axis, audience boundary, plural meaning | comparison, evidence, sequence, spatial |
| **Operational instrument** | current state, threshold or margin, authorized action, fallback, receipt/recovery | instrument, sequence, spatial |

Within that anatomy, selection, ordering, copy, medium, density, and optional
sections may change with the viewer, root, current Moment, and client
capabilities. The represented meaning, evidence, authority, and identity must
not drift silently.

## Projection across the four roots

One Artifact, canonical object, or Composition keeps one identity and revision
lineage appropriate to what it is:

- **Home** returns complete compact value now and normally offers no more than
  one continuation. Home does not ask for reflection to unlock the value.
- **Chat** lets a person ask, inspect, challenge, reshape, authorize, or repair.
  Chat-specific delivery blueprints may persist with transcript history, but
  they are not the universal artifact schema.
- **Places** situates spatial truth, current conditions, reachability, and the
  Place relationship using native maps and complete ordered alternatives.
- **Life** preserves durable Sources, episodes, saved compositions, audience,
  correction, and continuity. It does not store another copy for every root.

Plan and Occasion continue to own commitments, participation, shared decisions,
and live reconciliation. A root projection never grants action authority.

## Persistence policy

Generated output is ephemeral unless at least one retention trigger is true:

1. the person explicitly saves, names, shares, publishes, or curates it;
2. the person cites it or acts through it and later audit or repair requires a
   stable revision;
3. another governed object refers to the exact expression;
4. correction, revocation, or causal invalidation must address it later; or
5. an authored collaboration requires a stable shared version.

When a composition becomes durable, persist:

- stable ID, version, status, and human/Vesper/combined authorship;
- the exact saved copy and selected media snapshot;
- represented Resources, revisions, Source spans, and claim-local roles;
- represented time, generated time, and last verified time;
- semantic role, product job, format, and semantic anatomy;
- audience, use grant, purpose, membership epoch, and expiry;
- exclusion, correction, supersession, and invalidation lineage;
- lifecycle mode: `frozen`, `refreshable`, or `live`; and
- complete text/accessibility fallback.

Do not persist React trees, component names, geometry, colors, client gestures,
or executable actions. A `refreshable` or `live` section must remain visibly
separate from a frozen authored body. Regeneration creates a new version or an
explicitly live projection; it never rewrites what the person saved silently.

## Current implementation lanes

| Lane | Present role | Doctrine |
| --- | --- | --- |
| `CanonicalArtifactProjectionV1` | Legacy-named viewer-safe semantic read model over an Intake anchor | Preserve as a read spine; align its naming and expand owner adapters deliberately, not into a visual DSL |
| `CardBlueprintV1` / `ComposedChatCard` | Constrained Chat delivery grammar | Keep Chat-specific; do not universalize across roots |
| Adaptive composition lab | Native treatment and environment fixture lab | Migrate to orthogonal expression dimensions; retain old treatment keys only as compatibility adapters |
| `CompositionBriefV0` fixture compiler | Claim-local Source admission, novelty, medium coherence, authority, audience, and lifecycle compilation for A01–A06 | Keep fixture-only until shadow evaluation justifies a production boundary |
| `ArtifactCirculationV0` fixture compiler | One stable identity through Home, Chat, Places, and Life with root-native medium, action, persistence, correction, spatial-binding, and return-envelope rules | Use to derive native semantic renderers; never clone one cross-root card |
| `HomePortfolioCompositionV0` fixture composer | Current-consequence precedence, response-free value, bounded page selection, absorption, power diversity, and explicit suppression across one shared evidence world | Keep renderer-neutral; do not turn its scores or reason codes into a production ranking API without longitudinal evaluation |
| Editorial map composition | Specialized renderer-neutral spatial contract | Use as an exemplar for medium-specific semantics and native rendering |
| Lived-experience composition authority | Selection/suppression lineage for treatments | Keep distinct from saved user-facing composition |
| Atlas/Discover `visual_slots` composition | Legacy server-resolved visual assembly | Compatibility only; do not use as the general artifact architecture |
| `CanonicalArtifactCard` | Dev/gallery and limited artifact reading implementation | Decompose toward medium renderers and root-native anatomy; do not grow a universal prop matrix |

## Invariants

1. Initial value is legible before the person answers, classifies, reflects, or
   opens a detail screen.
2. Every present projection has one lead medium and at most one necessary
   supporting medium.
3. Every material generated claim retains inspectable evidence and correction.
4. Social authorship and audience remain visible; layout never implies consent.
5. One identity survives root, density, environment, and renderer changes.
6. Unknown renderers degrade within the same semantic section or omit safely;
   they never render raw JSON or widen authority.
7. Saving freezes the exact expression the person chose while preserving its
   dependency and invalidation manifest.
8. Direct canonical state remains direct when an artifact would add ceremony
   but no value.
9. Instruments work against current owner truth and have honest stale,
   unavailable, and recovery states.
10. Silence is valid when Vesper has not earned a substantive contribution.

## Explicitly rejected

- an LLM-authored React or block-component tree as the canonical artifact;
- one universal `ArtifactCard` or `LifeCard` with domain and lifecycle branches;
- a generic cross-domain `artifact_write` capability;
- persisting every generated response or projection;
- backend-authored coordinates, typography, gestures, or native navigation;
- treating social, editorial, relational, or receipt as peer media;
- hiding all substance behind a tap or a reflective prompt; and
- regenerating a saved expression in place without a visible new revision.

## Promotion sequence

1. Maintain a six-case cross-root fixture portfolio.
2. Run a component and pipeline disposition audit against those fixtures.
3. Land `CompositionBriefV0` and the orthogonal expression dimensions in the
   fixture-only adaptive composition lab.
4. Canonize semantic component contracts and native medium renderers from
   demonstrated fixture needs; keep exact visual composition root-owned.
5. Run agent composition in shadow mode against human and deterministic
   baselines.
6. Pilot one saved editorial composition and one live instrument to prove the
   persistence boundary.
7. Circulate one identity through Home, Chat, Places, and Life.
8. Add persistence only after save/share/correction behavior requires it, then
   retire superseded compatibility taxonomies deliberately.

Execution state on 2026-08-29: steps 1–3 are complete at fixture-contract
altitude. All six now compile and circulate under one identity through the four
roots. A01 and A06 prove opposite saved-versus-live persistence; A02 proves
attributed withdrawal; A03 proves immutable versioned revision; A04 proves
known-versus-new admission; and A05 plus the Home portfolio composer prove
page-level selection across quiet, emerging, and urgent states. Native semantic
renderer evaluation and agent shadow evaluation remain next; no production
persistence, ranking API, or UI has been authorized.
