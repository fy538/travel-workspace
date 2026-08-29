---
doc_type: working
status: active
owner: frontend / cross-repo architecture
created: 2026-08-29
last_verified: 2026-08-29
expires: 2026-09-28
why_new: Maps current artifact, card, composition, and rendering paths to the canonical semantic spine, native medium registry, owner-specific instrument, compatibility, or retirement roles.
promotes_to: travel-app/docs/Components.md
source_of_truth_for: []
---

# Artifact Component and Pipeline Disposition Audit

## Executive finding

The repository does not lack artifact infrastructure. It has several useful
systems built at different moments with different meanings of “card,”
“artifact,” and “composition.” The next step is convergence, not another
universal renderer.

The target architecture is:

```text
canonical truth
  -> viewer-safe semantic projection
  -> CompositionBrief / semantic anatomy
  -> bounded native medium renderer registry
  -> root-owned composition and environment fallback
```

## Backend and cross-repo pipelines

| Existing lane | Current capability | Disposition | Required action |
| --- | --- | --- | --- |
| `backend/core/models/canonical_artifact.py` and projection compiler | Strict viewer-relative evidence, facts, provenance, actions, correction, owner destinations | **Canonical semantic read spine** | Preserve; add new owner adapters only with authorization and fixture coverage. Do not add layout or component instructions. |
| `/artifact-projections` route | Read-only Intake-anchor projection; Together intentionally rejected without graph authorization | **Bounded production read path** | Keep scope honest. Expand only after owner authorization, not to satisfy renderer needs. |
| `CardBlueprintV1` | Validated Chat-only block grammar with opaque actions and durable text fallback | **Surface-specific delivery contract** | Keep in Chat. Do not make it the Home/Places/Life artifact schema. Reuse its validation discipline. |
| Editorial map composition | Renderer-neutral spatial claims, features, actions, and accessibility summary | **Medium-specific exemplar** | Preserve as spatial specialization; align identity/fallback vocabulary with the shared expression contract. |
| Lived-experience composition authority | Treatment selection, suppression reasons, and fingerprints | **Selection-lineage owner** | Rename in explanatory docs when ambiguity matters; do not treat it as saved content. |
| Atlas/Discover composition with `visual_slots` | Server-resolved template, slot layout, imagery, and copy assembly | **Legacy compatibility** | Stop generalizing. Extract useful deterministic assembly/quality-gate ideas, but keep future UI geometry client-owned. |
| Home and Places feed ranking/composition | Root-specific selection and ordering | **Root composer** | Preserve root ownership; consume semantic projections rather than becoming artifact truth. |
| No saved-composition model | No general persisted generated artifact owner exists | **Intentional open seam** | Pilot exact snapshot plus dependency manifest only after a real save/share/correction case earns it. |

## Frontend rendering lanes

| Existing lane | Current capability | Disposition | Required action |
| --- | --- | --- | --- |
| `CanonicalArtifactCard` | Universal card over `CanonicalArtifactProjectionV1`, with older family and density branches | **Compatibility/dev reader** | Freeze feature growth. Decompose fixture requirements into medium renderers and root-native anatomy. |
| `ArtifactNeighborhood` | Bounded related-resource visualization | **Specialized relational treatment** | Keep only with explicit typed edges and a complete list alternative; relational is a modifier, not its own canonical medium. |
| Adaptive composition lab | Native spatial, sequence, comparison, social, relational, editorial, receipt experiments plus environment stress states | **Primary fixture lab** | Add orthogonal presence/medium/modifier/role/density/context contract and legacy adapter. Do not mount in production. |
| `ComposedChatCard` | Native renderer for Chat `CardBlueprintV1` | **Chat-only renderer** | Keep transcript lifecycle, fallback, and safe action resolution. Do not import it as a root-generic artifact renderer. |
| `VesperChatCardKit` | Chat frame/header/chip/action anatomy | **Surface-owned primitives** | Reuse inside Chat only unless a primitive independently passes cross-root semantics and visual review. |
| Places renderer registry | Candidate, editorial, experience, memory, social, and notice/prompt rendering | **Root-owned renderer registry** | Preserve root specialization. Map eligible cards to shared expression dimensions; do not rename every family into a global medium. |
| Places maps and fallback lists | Native spatial behavior and nonvisual/denied-location alternatives | **Spatial medium capability** | Candidate for the spatial renderer contract; keep live world truth and geometry Places-owned. |
| `SpineRow` and itinerary/decision spines | Stable sequence anatomy | **Sequence capability** | Reuse behavior and reading order; do not force all temporal stories into itinerary styling. |
| `CardSurface`, `EditorialCard`, `HomeCardPrimitives` | Material and container recipes | **Container layer** | Keep separate from medium semantics. A comparison or sequence may use different containers by root. |
| `ProjectionStateNotice`, state primitives | Stale, partial, unavailable, permission, and recovery states | **Cross-root environment kernel** | Align semantic state vocabulary and ensure every medium declares degradation behavior. |
| Receipt components across Chat/collaboration | Consequential state, readback, undo/recovery | **Owner-specific instrument/receipt renderers** | Consolidate shared lifecycle vocabulary, not the underlying mutations or domain components. |

## Candidate canonical presentation kernel

Canonize contracts and behavior before exact visual styling. Existing components
should be adapted where possible; these names describe capabilities, not an
approved public API.

| Capability | Required semantics | Existing material to evaluate |
| --- | --- | --- |
| **Expression boundary** | Identity, semantic role, density/context, stable accessibility grouping | `CardSurface`, `EditorialCard`, root section primitives |
| **Identity and truth header** | Resource identity, represented time, freshness, source/owner distinction | canonical artifact view helpers, `StatusMeta`, Places truth lines |
| **Trust footprint** | Authorship, audience, strongest evidence, unknowns, inspect/correct affordance | `CatalogEvidenceDisclosure`, `WhyThisReceipt`, canonical artifact source/unknown rows |
| **Continuation dock** | Zero or one compact continuation; opaque authorized capability; honest disabled state | `ActionGroup`, `TextAction`, Chat safe action resolution |
| **Receipt/state rail** | Owner, consequence, status, readback, undo/recovery | `ActionReceiptStatus`, `ChatReceiptDisclosure`, collaboration decision receipts |
| **Degraded fallback** | Stale/offline/denied/unsupported treatment without authority widening | `ProjectionStateNotice`, Places fallback lists, adaptive environment adapters |
| **Accessible alternative** | Ordered, complete reading independent of geometry, motion, image, or audio | adaptive reading-order oracle, Places map fallback, semantic section tree |

These capabilities are not all cards. Some are inline rows, rails, map-linked
lists, or detail-page regions.

## Candidate native medium registry

| Canonical medium | Existing implementation seeds | Missing before canonization |
| --- | --- | --- |
| **Evidence** | Canonical artifact facts/media/provenance, Places evidence disclosure, editorial evidence rows | Claim-local source roles, compact trust footprint, deletion/invalidation fixtures |
| **Sequence** | Adaptive sequence, `SpineRow`, itinerary and decision lifecycles | General represented-time model, gaps/unknowns, non-itinerary visual posture |
| **Comparison** | Adaptive comparison, Chat comparison, Places candidate fork | Shared axis semantics, evidence comparability checks, compact/standard variants |
| **Spatial** | Places maps, editorial map, adaptive spatial plus ordered fallback | Shared semantic spatial input boundary, denied/offline fallback contract, root projection adapters |
| **Concise prose** | Adaptive editorial passage, Places editorial cards, long-form typography | Known-to-person novelty gate, citations/claims contract, compact complete-on-view variant |
| **Interactive instrument** | Trip/booking/decision components, live map/route, receipts | Common state/action/fallback interface without collapsing domain mutation owners |

Social authorship, relational context, and quantitative encoding remain
modifiers across these media. Editorial contribution, attributed human
contribution, receipt, canonical state, and operational instrument remain
semantic roles.

## Component admission checklist

A component becomes cross-root canonical only when:

1. at least two fixture worlds and two roots need the same semantic behavior;
2. its props describe meaning or state, not one domain's backend table;
3. it has a complete nonvisual reading and Dynamic Type behavior;
4. stale, unavailable, corrected, withdrawn, and unsupported states are defined;
5. it cannot widen audience or invent action authority;
6. it retains stable identity independently of revision and viewer epoch;
7. root-native composition can alter container, density, and geometry; and
8. focused tests prove semantics without pretending to be visual evidence.

Failing this checklist means the component remains root- or feature-owned.

## Files to freeze from architectural expansion

- `components/artifacts/CanonicalArtifactCard.tsx`: maintenance and fallback
  fixes only until medium decomposition is approved.
- `utils/adaptiveCompositionResolver.ts`: legacy shadow-oracle behavior only;
  new production selection should target orthogonal dimensions.
- `backend/core/models/composition.py` and `backend/composition/*`: no new
  cross-product renderer grammar based on `visual_slots`.
- `CardBlueprintV1`: no non-Chat surface expansion without a new decision.

## Ordered action list

### P0 — Converge the contract

1. **Complete:** land the artifact system doctrine and cross-root fixture pack.
2. **Complete:** add fixture-only orthogonal expression types and a legacy treatment adapter.
3. **Complete:** validate one lead medium, at most one support, modifiers, role, density,
   context, stable Resource identity, and text fallback.

### P1 — Prove the kernel and media

4. **Complete at fixture altitude:** implement semantic fixture payloads for
   A01–A06 without production API changes. All six are claim- and
   Source-complete `AgentCompositionDraftV0` values.
5. Map each fixture to existing components before creating new ones.
6. Extract only repeated semantic behavior into provisional kernel contracts.
7. Build or adapt one renderer per canonical medium inside the dev lab.

### P2 — Prove agent composition

8. **Fixture contract complete; runtime pending:** define an agent-facing
   `CompositionBriefV0` schema with Source/claim references and no presentation
   code.
9. **Fixture compiler complete; runtime pending:** compile briefs through
   deterministic authority, evidence, and medium-policy checks.
10. Compare agent, deterministic, human-authored, flat-report, and silence
    treatments in shadow evaluation.

### P3 — Prove lifecycle before generalizing

11. **Pure fixture pilot complete; durable writer pending:** one saved editorial
    artifact has an exact snapshot, dependency manifest, audience, version, and
    claim-local invalidation.
12. **Pure fixture pilot complete; owner integration pending:** one live
    instrument's expression expires while its persistence disposition retains
    owner truth and allows a receipt only after confirmed consequence.
13. **Complete at fixture altitude:** circulate each identity through Home,
    Chat, Places, and Life with stable identity, root-native posture, correction,
    persistence, and return-envelope validation.

### P3.5 — Compose before rendering

The fixture-only `HomePortfolioCompositionV0` now selects one foreground and a
bounded, power-distinct field across current state, instruments, human value,
and Vesper value. It proves three states and rejects four baselines without
choosing components or geometry:

- quiet Friday: one immediately usable opening, not an empty screen or recap;
- emerging Saturday: Red Hook, dinner consequence, and pasta transfer;
- urgent return: one live operational instruction preempts the ordinary field;
- flat feed, chronological recap, everything-visible, and silence all fail the
  controlled evidence-world oracle.

### P4 — Consolidate

14. Replace legacy adaptive treatment decisions with the orthogonal contract or
    a documented compatibility adapter.
15. Decompose the universal canonical artifact card.
16. Retire duplicate Chat attachments only when lifecycle and action semantics
    have a proven replacement.
17. Keep Atlas visual-slot composition in compatibility until its consumers are
    migrated independently.

## Not authorized by this audit

- production Home/Chat/Places/Life navigation changes;
- a new backend table or endpoint;
- a general agent `artifact_write` or `composition_create` tool;
- moving domain action logic into shared artifact components;
- declaring visual canon from Jest, typecheck, or the dev fixture alone; or
- deleting compatibility renderers before production consumers and fallback
  windows are known.
