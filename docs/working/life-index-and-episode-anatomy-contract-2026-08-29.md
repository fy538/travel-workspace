---
doc_type: working
status: active
owner: founder / product / design / architecture / editorial / engineering
created: 2026-08-29
last_verified: 2026-08-29
expires: 2026-09-28
why_new: Defines one canonical semantic composition for the Life root and its episode detail after the six evidence worlds eliminated archive-first, lens-first, source-feed, and composition-feed alternatives.
promotes_to: null
supersedes: []
source_of_truth_for: []
depends_on:
  - docs/decisions/2026-08-29-adopt-life-continuity-and-return-contract.md
  - docs/working/life-six-world-fixture-execution-report-2026-08-29.md
  - docs/working/life-object-and-lens-fixture-pack-2026-08-29.md
  - docs/working/life-refinding-query-benchmark-2026-08-29.md
  - docs/working/life-social-lifecycle-fixture-matrix-2026-08-29.md
---

# Life Index and Episode Anatomy Contract

## Question or outcome

What is the one complete semantic version of Life that organizes Trips,
Journeys, Occasions, Plans, Occurrences, Sources, Outcomes, social
contributions, Place relationships, and generated compositions without feeling
like an archive, database, card feed, or second Home?

## Executive decision

Life uses a **period-and-episode spine with contextual lenses and a bounded
return layer**.

```text
Life
├── Find and scope
├── In motion                 conditional, same governed objects
├── Lived periods             canonical stable spine
│   └── episode doors         Journeys, Occasions, supported bounded episodes
├── Across time               earned longitudinal relationships
├── Returns                   bounded derived value, separate from record
└── Timeline · Map · Sources  contextual lenses and utilities
```

The canonical detail unit is an **episode projection**, not an artifact page or
generated story:

```text
episode identity and truth
  -> occurred story spine
  -> plans, changes, and unresolved state
  -> people and attributed contributions
  -> Sources nested where they matter
  -> optional source-grounded See anew
  -> contextual Continue
  -> inspect and repair
```

This contract defines hierarchy, admission, behavior, and information roles.
It deliberately leaves typography, geometry, card shape, motion, illustration,
and exact component styling to a dedicated visual-design tool.

## 1. Root responsibility

Life owns the standard viewer experience for:

- accumulated continuity;
- known-item and contextual re-finding;
- episode and longitudinal organization;
- viewer-relative Mine/Together projection;
- authorship and source inspection;
- correction, detachment, suppression, release, and deletion;
- returning to something on request; and
- carrying governed context into another root.

Life does not own:

- the attention-ranked present—that is Home;
- the lowest-friction contribution and interrogation path—that is Chat;
- current spatial/world possibility and provider truth—that is Places;
- every durable object's write authority;
- a social activity feed;
- an AI autobiography; or
- a task queue made from the past.

The root relationship is:

| Root | Dominant posture toward the same object |
| --- | --- |
| **Home** | Why this matters now; complete-value possibility or consequence |
| **Chat** | Give, ask, transform, correct, or deliberately change state |
| **Places** | What this Place makes possible now under current world truth |
| **Life** | Where this belongs across time, episodes, relationships, Sources, and governed return |

## 2. Canonical Life index

### 2.1 Find and scope band

The first stable capability is contextual search. It accepts incomplete cues
involving a person, Place, period, episode, medium, Plan state, occurrence
state, author, or adjacent landmark.

Beside search, Life exposes a viewer-scope control with three semantic states:

- **Combined** — the person's private record plus currently authorized,
  addressed shared context;
- **Mine** — private and personally owned state plus governed shared core where
  necessary to keep the person's episode truthful; and
- **Together** — current or frozen historical shared cores and attributed
  contribution lanes visible to this viewer.

The default is **Combined**. This does not merge ownership or Outcomes. It lets
social life appear naturally inside the person's life while retaining an
explicit way to inspect scope. Exact labels may change after comprehension
testing; the authority semantics may not.

Search returns the target first and at most three default landmarks. It does
not route every query through the index or retain raw reformulations as
personal meaning.

### 2.2 In motion

This region exists only when a governed Journey, Occasion, or Plan is currently
active or materially upcoming.

It contains the same object that will later appear in its lived period. It is
not a duplicated planning card and does not become a second Home. Its Life job
is continuity:

- identity and current lifecycle state;
- authoritative time and Place;
- unresolved or changed state that affects the object;
- the viewer's current commitment; and
- entry into the episode's complete record.

Operational urgency, recommendations, and attention arbitration remain Home's
job. When the object happens or closes, the door settles into its represented
period; no scrapbook object is created.

### 2.3 Lived periods: the stable spine

Life's primary index is a hierarchy of landmark-bearing periods and episode
doors:

```text
2026
  Summer
    Nice → Rome · Aug 14–27        Journey
    Dinner in Brooklyn · Aug 29    Occasion
  Spring
    …
2025
  …
```

Periods are retrieval scaffolding, not AI-written life chapters. Acceptable
period names come from calendar structure, explicit titles, canonical Places,
bounded Trips/Journeys, or user-authored labels. Vesper must not silently name
a period `A season of becoming` or another identity/emotional interpretation.

Only stable doors appear at this level. Nested evidence remains available
inside its parent or through search:

- L01 Europe is a stable Journey door.
- L02 Brooklyn dinner is a stable Occasion door.
- L03 unused museum ticket remains under the Europe Plan/history and in search.
- L04 film–Rome relation remains under its Rome Encounter; a saved sourced
  composition may receive its own authored return shortcut.
- L05 Rome–Paris comparison remains an addressed Together return under the
  relevant period/Journey, not a friend-activity door.
- L06 Red Hook becomes a stable longitudinal door only after supported
  recurrence passes every gate.

Ordering inside a period is primarily represented time and user-authored
curation. Dynamic editorial rank may break ties or select a compact preview; it
must not make the period behave like an engagement feed.

### 2.4 Across time

This region contains earned longitudinal relationships that cannot be reduced
to one episode:

- a supported relationship with a Place such as Red Hook;
- a recurring practice with explicit or strongly governed continuity; or
- an authored thread spanning several episodes.

Frequency alone never earns admission. The doorway must pass the same seven
entrance gates, reference its constituent episodes, and remain correctable.
People may later become a longitudinal lens, but relationship trajectories and
inferred identity themes remain deferred.

### 2.5 Returns

Returns is the bounded dynamic layer for:

- saved compositions;
- newly eligible source-grounded reconstructions;
- addressed Together juxtapositions;
- explicit `return later` choices; and
- dormant material made newly useful by a changed world condition.

Returns is visibly derived and subordinate to the stable record. It cannot
reorder or masquerade as the period spine. Every unit must add complete value
before asking anything, expose source role, and have a suppression path.

The region may be empty. Silence is better than a factual trip summary,
reflection prompt, nostalgia filler, or speculative identity reading.

### 2.6 Timeline, Map, and Sources

These are canonical lenses and utilities over the same corpus:

- **Timeline** retrieves by represented time and folds supporting state beneath
  episodes. It keeps planned, occurred, authored, captured, and generated times
  distinct.
- **Map** retrieves autobiographical Place relations with occurred, planned,
  source-only, Mine, and Together states. Current opportunity opens Places.
- **Sources** provides heterogeneous known-item retrieval and custody
  inspection. It is not a primary Library feed or a folder-maintenance system.

The lenses may be opened globally with current filters or contextually from an
episode. They never create copies or compete as separate canonical memories.

## 3. Canonical index composition for the six-world fixture

The complete semantic index produced from L01–L06 is:

```text
Life · Combined

Find anything from your life…

IN MOTION
  [Only a genuinely active/upcoming governed object; absent in post-return
   fixture unless the Brooklyn dinner or NYC weekend is still prospective]

2026
  SUMMER
    Nice → Rome · Aug 14–27
      supported Journey · returned · Mine + authorized Together
      nested: unused museum Plan, Colosseum Encounter, film relation

    Dinner in Brooklyn · Aug 29
      Occasion · upcoming/live/happened according to current truth
      shared core + viewer-private overlay

  SPRING / EARLIER PERIODS
    other stable episode doors when governed

ACROSS TIME
  Red Hook
    supported visits and Occasions · planned/source-only states remain distinct

RETURNS
  Why Rome needed Troy to lose
    sourced composition · human observation and Vesper contribution separate

  Same heat, different escape valves
    addressed Together comparison only while current grants permit

Timeline · Map · All sources
```

Important absences:

- no standalone museum memory;
- no artifact count as value;
- no `Places that changed you` identity bucket;
- no Maya/Paris activity tile;
- no equal card for every ticket, restaurant, and photograph;
- no prompt asking what the person does not want to lose; and
- no completion or reflection chores.

## 4. Canonical episode anatomy

An episode is a viewer-relative read projection over governed owners. It is not
automatically a new durable object. Its anatomy has eight semantic regions,
only the applicable ones render.

### 4.1 Identity and truth header

Always present:

- descriptive or human-authored name;
- semantic type and lifecycle state;
- represented period;
- canonical Place or route scope where applicable;
- viewer scope;
- compact truth/completeness state; and
- direct correction or scope inspection.

The header never leads with Source counts, AI interpretations, engagement, or
capture completeness.

Examples:

- `Nice → Rome · Aug 14–27 · Journey · Returned · Some route gaps`
- `Dinner in Brooklyn · Occasion · Happened · Shared with Maya and Alex`
- `Red Hook · Across 4 supported visits · 2 planned-only relations`

### 4.2 Episode skeleton

The skeleton answers what the episode is before exposing detail:

- bounded purpose or human-facing description;
- main Places and people under current authority;
- supported start/end or lifecycle state;
- major chapter boundaries; and
- material unresolved truth.

For a sparse episode, the skeleton may be the entire useful treatment. Life
does not generate prose simply to occupy space.

### 4.3 Occurred story spine

Supported Occurrences lead. The spine groups evidence into meaningful chapters
using changes in Place, people, activity, goal, and causal structure.

```text
Nice
  supported stay and encounters
Movement south
  occurred rail segment
  ferry remained planned-only
Sorrento / Amalfi
  supported Places, photographs, notes
Rome
  supported Colosseum Encounter
Return to New York
  supported arrival and open continuity
```

Timeline and Map are available within this spine, but neither replaces it.
Unknown gaps remain unknown. A continuous route is never fabricated for visual
smoothness.

### 4.4 Plans, changes, and unresolved state

Prospective and changed state sits beside the chapter it affected:

- original Plan;
- revision and author;
- commitment;
- cancellation, miss, or non-occurrence;
- unresolved evidence; and
- authoritative current/final state.

This region makes L03 useful without turning it into a standalone memory. It
also provides decision archaeology without regret framing.

### 4.5 People and contributions

Social episodes compile:

```text
governed shared core
  + viewer-private overlay
  + attributed contribution lanes
  + plural Outcomes
```

People appear because they changed or contributed to the episode—not as social
engagement inventory. Each contribution retains author, audience, precision,
and membership epoch. Private Outcomes never become group sentiment.

If a boundary removes a person lane, the episode recompiles. Independent
history remains when it can remain truthful without that lane.

### 4.6 Sources in place

Tickets, photographs, notes, receipts, books, films, messages, and generated
outputs appear where they support the episode:

- a train ticket under the movement it planned or evidenced;
- a photograph under the Place/moment it depicts;
- Maya's receipt under her attributed dinner contribution;
- the movie Source beside the Rome Encounter it later informed; and
- external citations beside the composition claim they support.

`All sources` opens the complete episode-scoped retrieval bundle. Sources do
not become an equal card stream or require manual categorization.

### 4.7 See anew

Generated value occupies a clearly derived region and must add one evidenced
operation:

- distinction;
- reconstruction;
- comparison;
- explanation;
- relational mapping;
- sourced current reopening; or
- playable transformation into another medium.

Every material claim carries a compact source role and inspectable lineage.
An eligible composition may be saved, shared as a bounded projection, hidden,
or regenerated. It never rewrites the occurred story spine.

### 4.8 Continue and repair

Valid Continuations appear beside the object that justifies them:

- `Open this Place now`;
- `Follow this sourced thread`;
- `Use this in New York`;
- `Return here`;
- `Ask Maya about the recipe`; or
- `Start a new Occasion with selected context`.

The action preview carries source identity, current authority, represented
time, freshness, destination, and allowed consequence. It creates a receipt
only when state changes.

Repair remains available without dominating reading:

- Correct;
- Detach from episode;
- Exclude from resurfacing;
- Release interpretation/use;
- Change audience or precision;
- Leave;
- Block/unblock;
- Delete/revoke Source; and
- inspect provenance and downstream uses.

## 5. Lifecycle-specific episode emphasis

The same governed object changes emphasis without changing identity:

| Lifecycle | Episode leads with | It does not become |
| --- | --- | --- |
| **Prospective** | Purpose, authoritative time/Place, decisions, current commitment, unresolved coordination | Setup form or archive preview |
| **Live** | Current state, material changes, relevant commitments, bounded participant cues | Location surveillance or noisy live feed |
| **Recently happened** | Supported Occurrences, contributions, immediate receipts, optional complete-value afterglow | Reflection assignment or communal camera roll |
| **Historical** | Find, stable story spine, source inspection, substantive See anew, deliberate Continue | Nostalgia feed or task queue |
| **Dormant/uncertain** | Honest retained state and searchability | Periodic reminder or failed-completion story |

## 6. Object movement through Life

### Contribution enters

```text
Chat / share / import
  -> contribution contract resolves authority
  -> canonical Source / Plan / Occasion / Occurrence / Outcome changes
  -> Life updates the existing episode projection
```

No generic artifact card is created merely because a contribution persisted.

### Plan becomes occurrence

The Plan remains historical. Supported Occurrence is added through its domain
owner. Life changes emphasis and Map/Timeline state; it does not rewrite the
Plan as though it had always happened.

### Occasion closes

The active Occasion door settles into its represented period. Contributions
remain attributed. A generated afterglow appears only if eligible. No second
memory object is created.

### Composition is saved or shared

Saving creates stable access to a versioned composition identity and manifest,
not new occurrence truth. Sharing creates a bounded viewer projection from
currently authorized inputs.

### Continue succeeds

The destination owner returns a receipt/readback reference. Life may display
that consequence in the originating episode lineage. Personal meaning or a new
Outcome requires separate admission.

### Correction or revocation occurs

Every lens and composition recompiles from surviving authority. The index door
may remain, degrade to nested/search-only, or disappear if it no longer passes
the hard gates. Pinning cannot preserve an invalid door, though an authorized
shortcut may continue to a governed search result.

## 7. Sparse, rich, and quiet states

### Sparse Life

Life shows only admitted Sources, Plans, Places, and Occasions that already
have useful identity. Search works immediately. One supported event may sit in
a calendar period without a generated story. The interface never asks the
person to complete days, label people, write reflections, or organize folders
to unlock value.

### Rich Life

More evidence increases:

- search resolution;
- episode and chapter confidence;
- social plurality;
- longitudinal Place eligibility;
- composition substance; and
- relevant Continue possibilities.

It does not increase visible card count proportionally. Richness should produce
better folding, context, and synthesis.

### Quiet Life

Quiet means low pressure, not low value. The stable record remains explorable,
searchable, and connected to Places. Returns may offer complete value when
earned, but no placeholder composition or input prompt appears merely to make
the page feel active.

## 8. Semantic acceptance gate

The anatomy is ready for dedicated visual composition only when a prototype can
show that:

1. L01, L02, and rich L06 are recognizable as different stable units without
   becoming unrelated design systems;
2. L03, L04, and L05 remain useful while subordinate to their correct context;
3. Combined, Mine, and Together change the viewer projection without copying
   objects or leaking private Outcomes;
4. planned, occurred, source-only, unresolved, and generated state remain
   legible in both index and episode;
5. Timeline, Map, and Sources feel like ways into the same life rather than
   competing products;
6. generated compositions are valuable but visibly derived;
7. Continue is available without turning Life into a task list;
8. correction and suppression are predictable without a policy-dashboard
   aesthetic;
9. sparse state supplies value without homework; and
10. rich state becomes more coherent rather than more crowded.

## 9. Engineering consequences after acceptance

The contract implies these read projections, not a new universal Life owner:

- `LifeIndexProjection`;
- `LifeEpisodeProjection`;
- `LifeSearchResultProjection`;
- `LifeTimelineProjection`;
- `LifeMapProjection`;
- `LifeSourceBundleProjection`;
- `LifeTogetherProjection`;
- `CompositionManifestProjection`;
- `ReturnEligibilityProjection`; and
- `ContinueEnvelope` plus destination receipt.

The next engineering planning pass should map every field to current owners,
identify missing adapters, and separate aggregate-read infrastructure from
domain writes before naming tables or services.

## Compact standard

> Life is a stable way back into the person's world, with enough intelligence
> to make it newly useful and enough restraint not to rewrite it.
