---
doc_type: working
status: active
owner: product / design / cross-repo architecture
created: 2026-08-29
last_verified: 2026-08-29
expires: 2026-09-28
why_new: Defines six evidence-complete artifact worlds that test semantic composition, four-root projection, social authority, persistence, correction, and live-state boundaries.
promotes_to: docs/systems/artifact-expression-and-composition.md
source_of_truth_for: []
---

# Cross-Root Artifact Fixture Pack

## Purpose

This portfolio prevents the artifact system from being derived from one card,
one trip recap, or one renderer. Each fixture starts from a real product story
and must prove one complete value-bearing composition across Home, Chat, Places,
and Life.

The fixtures are product and contract evidence, not claims that all required
Sources, friend contributions, research, provider access, or production roots
already exist. Synthetic or missing evidence must be labeled in the executable
fixture.

## Execution status — 2026-08-29

- **A01–A06** now exist as claim- and Source-complete executable drafts across
  the Travel App fixture lab. A01, A05, and A06 remain in
  `travel-app/constants/mocks/compositionBriefFixtures.ts`; A02–A04 are in
  `travel-app/constants/mocks/artifactPortfolioFixtures.ts`; the aggregate
  `ARTIFACT_PORTFOLIO_DRAFTS` contains the full ordered portfolio.
- `travel-app/utils/compositionBrief.ts` compiles them into renderer-neutral
  `CompositionBriefV0` values and enforces novelty, claim-local support,
  audience, authority, one lead plus at most one support, live freshness, and
  lifecycle disposition.
- The pure saved-composition materializer freezes A01 only after an explicit
  command and evaluates claim-local Source invalidation. It performs no durable
  write.
- A06 is explicitly ineligible for saved-composition materialization; its live
  expression expires while Occasion/Commitment truth and confirmed receipts
  remain owner-governed.
- A05 additionally participates in the fixture-only Home portfolio compositor,
  where its forward New York value beats A01–A04 for the controlled current
  situation rather than receiving placement merely because it compiled.

## Shared evaluation contract

Every fixture must record:

- authorized Sources and canonical owners;
- what the person already noticed or knows;
- the genuinely new contribution Vesper adds;
- immediate job and dominant product move;
- semantic role, lead medium, optional support, modifiers, and format;
- compact Home, conversational Chat, spatial Places, and durable Life posture;
- exact audience, authorship, freshness, and action authority;
- ephemeral, saved/shared, corrected, stale, offline, and unsupported-renderer
  behavior; and
- one continuation at most in the compact projection.

A fixture fails if it merely repeats the user's note, asks for reflection before
delivering value, flatters with a personality interpretation, or uses visual
variety without a different cognitive job.

## Portfolio coverage

| ID | World | Primary proof | Lead medium | Format/lifecycle |
| --- | --- | --- | --- | --- |
| **A01** | Rome after *The Odyssey* and the Colosseum | Vesper adds researched substance beyond the user's Aeneas connection | evidence or prose | bounded article; ephemeral then saveable |
| **A02** | Rome and a friend's simultaneous Paris trace | Multiplayer enriches an owned story only when a substantive common axis exists | comparison | attributed social juxtaposition; private or addressed |
| **A03** | Nice → Sorrento → Amalfi → Rome | Fragmented tickets, photographs, Places, and notes become a truthful journey reconstruction | sequence | reconstructed journey; saveable |
| **A04** | “Sorrento has cliffs” | One noticed cue opens a genuinely broader world without becoming generic travel content | comparison | compact opening into an optional guide/article |
| **A05** | Back in New York before the weekend | Prior travel evidence changes a current possibility without turning Home into a recap | spatial or comparison | refreshable guide/opening; normally ephemeral |
| **A06** | A hot live day with a timed entrance or route disruption | Meaning and operational assistance coexist without becoming separate products | instrument | live owner-backed instrument; UI never persisted |

## A01 — Rome: what the user's connection still did not explain

### Evidence world

- User-authored note connecting a recent *Odyssey* viewing, Troy, Aeneas, Rome,
  and the Colosseum.
- Ticket or location evidence for the Colosseum visit.
- Separately sourced claims from ancient texts, archaeology, and Roman political
  history; source traditions must remain distinct.

### Contribution threshold

Vesper must not lead with “Rome adopted the survivor's side of the Trojan War”
or restate that Aeneas fled Troy. It must supply a supported mechanism,
distinction, contradiction, later appropriation, or material consequence the
person did not already state. If research cannot clear that threshold, silence
or a direct source return beats an artifact.

### Expression contract

- Product move: Make sense.
- Semantic role: Vesper editorial contribution.
- Lead medium: evidence or concise prose, chosen by the claim.
- Supporting medium: at most one sequence or comparison when it proves the
  mechanism.
- Format: bounded article, not a recap card.

### Root projections

| Root | Projection |
| --- | --- |
| **Home** | Complete compact claim plus its strongest support; no question or “reflect on this” CTA |
| **Chat** | Inspect the claim, challenge sources, ask for another interpretation, or remove one input |
| **Places** | Situate only the spatially relevant sites or layers; do not turn the article into map decoration |
| **Life** | If saved, preserve the exact article version, represented Rome encounter, sources, exclusions, and correction lineage |

### Lifecycle tests

- Default: ephemeral, with Sources and the encounter retained under their own
  authority.
- Save: exact body and evidence ordering freeze as version 1.
- Correction: removing an unsupported claim invalidates or versions the article
  without deleting independent Sources.
- Old client: readable text and source list survive without the preferred
  medium renderer.

## A02 — Rome and Paris: a substantive social juxtaposition

### Evidence world

- The user's authorized Rome evidence.
- A friend's explicitly shared Paris contribution, time window, and audience
  grant.
- Public/world evidence only as necessary to establish a real common axis.

### Contribution threshold

Co-presence in Europe is not enough. “You were both traveling” or two photo
tiles fail. The compiler must find and support a substantive shared dimension—
for example, two different civic uses of inherited monumental space, two heat
adaptations, or two transit constraints—or omit the juxtaposition.

Vesper never merges personal meaning, infers friendship quality, or exposes the
friend's private itinerary.

### Expression contract

- Product moves: Make sense and Carry forward.
- Semantic role: attributed human contributions plus Vesper editorial
  contribution.
- Lead medium: comparison.
- Modifier: social authorship; quantitative only if units are genuinely
  comparable.
- Format: attributed social juxtaposition.

### Root projections

| Root | Projection |
| --- | --- |
| **Home** | One complete contrast, both authors visible, and no social-engagement bait |
| **Chat** | Ask why the axis is valid, remove either contribution, or draft an addressed share without sending it |
| **Places** | Show bounded Rome and Paris Place references only when space carries part of the comparison |
| **Life** | Preserve a private saved juxtaposition or an addressed shared version with distinct audience and revision |

### Lifecycle tests

- Grant expiry withdraws the friend's material while preserving the user's
  independent value when possible.
- Blocking, leaving, and contribution withdrawal remain distinct.
- A saved shared version records the exact audience epoch.

## A03 — The southern-Europe journey reconstructed from fragments

### Evidence world

- Plane, train, and ferry tickets.
- Hotel and restaurant records.
- Photographs and capture times.
- User notes, questions, saved Places, and supported location evidence.
- Intent and occurrence remain separate when proof is incomplete.

### Contribution threshold

The result must reveal more than an ordered itinerary or place count. Useful
contributions include a supported divergence between intended and actual
movement, how transportation changed reachability, or a gap the person can now
understand. The system must preserve uncertainty rather than drawing one
continuous fabricated route.

### Expression contract

- Product moves: Make sense and Carry forward.
- Semantic role: Vesper reconstruction over canonical evidence.
- Lead medium: sequence.
- Supporting medium: spatial or evidence.
- Modifier: quantitative only for honest distances, durations, or mode counts.
- Format: reconstructed journey.

### Root projections

| Root | Projection |
| --- | --- |
| **Home** | One newly useful reconstruction or contrast, not a flat “four places, twelve artifacts” report |
| **Chat** | Resolve a gap, correct occurrence, exclude a Source, or ask for a different supported lens |
| **Places** | Route and Place relations with planned, occurred, and unresolved segments visibly distinct |
| **Life** | Durable Journey composition over existing owners, with Timeline, Map, Sources, gaps, and revision lineage |

### Lifecycle tests

- Imported-later tickets attach to represented time, not import time.
- Deleting one ticket invalidates dependent route claims, not photographs or
  unrelated events.
- Save freezes the reconstruction version; a newly discovered Source proposes a
  new revision.

## A04 — From one Sorrento cliff cue into a broader world

### Evidence world

- The user's explicit observation that Sorrento has cliffs.
- Supported Place identity and visit evidence.
- Researched geological, architectural, agricultural, transportation, or
  settlement evidence.

### Contribution threshold

The artifact must connect the cue to something the person did not already say:
a mechanism, a meaningful comparison with another cliff settlement, or a
practical consequence for how people build, move, eat, or see. It must not
diagnose that the user “experiences travel through transitions.”

### Expression contract

- Product moves: Make sense and Open possibility.
- Semantic role: Vesper editorial contribution.
- Lead medium: comparison or evidence.
- Supporting medium: spatial when geography is necessary.
- Format: compact opening with optional deeper guide/article.

### Root projections

| Root | Projection |
| --- | --- |
| **Home** | One surprising, supported distinction fully legible at a glance |
| **Chat** | Follow the mechanism, compare another place, or inspect why this cue was used |
| **Places** | Show the cliff/settlement relationship and one current or future Place horizon, not a generic recommendation carousel |
| **Life** | Keep only if saved or if it becomes part of the Sorrento episode; the original observation remains independently retrievable |

### Lifecycle tests

- Known-to-person check suppresses a connection already stated in Chat.
- Weak comparison axis falls back to evidence or silence.
- Offline fallback retains the claim and sources without interactive geography.

## A05 — Home after travel: New York opens forward

### Evidence world

- Current location, time, weather, opening hours, and weekend conditions.
- Authorized prior travel evidence and current New York Place relationships.
- Explicit friend contributions or availability only when granted for this
  purpose.

### Contribution threshold

The unit must make the coming weekend more possible now. Prior travel may change
the lens, but the trip cannot dominate Home merely because it is recent. The
result must not ask the person to process returning home or turn a past pattern
into a personality claim.

### Expression contract

- Product moves: Open possibility and Help it work.
- Semantic role: Vesper editorial contribution or operational instrument,
  depending on immediacy.
- Lead medium: spatial, comparison, or instrument.
- Modifiers: relational/social only with explicit current relevance.
- Format: refreshable guide or compact opening.

### Root projections

| Root | Projection |
| --- | --- |
| **Home** | The most valuable current possibility plus immediate conditions; no setup task |
| **Chat** | Adjust radius, companions, effort, or time through ordinary language |
| **Places** | Own current world truth, reachability, alternatives, and native exploration |
| **Life** | Preserve the prior evidence and any explicitly saved guide, but not every regenerated weekend ranking |

### Lifecycle tests

- Current conditions expire independently of the durable Place relationship.
- If nothing beats the ordinary Home context, the artifact is omitted.
- A saved guide marks which sections are frozen and which require refresh.

## A06 — One live operational instrument with optional depth

### Evidence world

- Accepted Plan or Occasion.
- Timed entry, route, weather/heat, current location, provider state, and named
  participants within authority.
- Optional relevant cultural depth supported independently.

### Contribution threshold

The instrument must reduce uncertainty or effort: when to leave, where to meet,
what changed, what fallback remains, or what action is authorized. Editorial
depth may be offered only after the live job is complete; it must not compete
with the operational hierarchy.

### Expression contract

- Product move: Help it work; optional Make sense support.
- Semantic role: operational instrument.
- Lead medium: instrument.
- Supporting medium: sequence, spatial, or concise prose—one only.
- Format: live stateful instrument.

### Root projections

| Root | Projection |
| --- | --- |
| **Home** | Current threshold or change, complete enough to act or dismiss |
| **Chat** | Ask, alter, authorize, or repair while preserving exact Plan/Occasion context |
| **Places** | Route, gate, current conditions, and ordered nonvisual fallback |
| **Life** | Preserve only the resulting occurrence, receipt, and explicitly saved composition—not the live UI tree |

### Lifecycle tests

- Stale state visibly removes action confidence.
- A consequential action returns an owner-backed receipt and readback.
- The instrument expires cleanly; the Plan, Occasion, Source, occurrence, and
  receipt follow their own retention rules.

## Cross-fixture pass matrix

| Requirement | A01 | A02 | A03 | A04 | A05 | A06 |
| --- | :---: | :---: | :---: | :---: | :---: | :---: |
| New value before input | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Editorial substance | ✓ | ✓ | ✓ | ✓ | optional | optional |
| Multiplayer authority | — | ✓ | optional | — | optional | ✓ |
| Sequence | optional | optional | ✓ | — | optional | ✓ |
| Comparison | optional | ✓ | optional | ✓ | optional | — |
| Spatial | optional | optional | support | optional | ✓ | support |
| Live instrument | — | — | — | — | optional | ✓ |
| Saved composition | ✓ | ✓ | ✓ | optional | optional | receipt only |
| Correction/invalidation | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Complete fallback | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

## Promotion gate

Do not promote a general composition API or saved-composition table until:

1. all six fixtures compile into one lead medium and at most one support;
2. the same identity survives all four root projections;
3. a human reviewer can identify the new contribution without opening detail;
4. social withdrawal and Source deletion degrade without leakage;
5. one saved editorial artifact preserves its exact version and lineage;
6. one live instrument proves that useful UI can expire without becoming an
   artifact record; and
7. an unsupported client receives a complete, authority-safe fallback.

Current result: all six satisfy the semantic compiler and circulate under one
identity through Home, Chat, Places, and Life. A01 and A06 satisfy the opposite
persistence boundary; A02 satisfies attributed withdrawal; A03 satisfies
versioned reconstruction revision; A04 satisfies known-versus-new novelty; and
A05 satisfies page competition, absorption, suppression, and no-homework
oracles. These are fixture tests, not production, visual, agent-runtime, or
durable-storage proof. See the [execution
report](six-artifact-cross-root-circulation-execution-report-2026-08-29.md).
