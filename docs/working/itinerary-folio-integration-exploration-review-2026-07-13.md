---
doc_type: working
status: active
owner: founder / product / design
created: 2026-07-13
last_verified: 2026-07-13
expires: 2026-08-12
why_new: Record the design review and boundaries for integrating Folio responsibilities into the canonical itinerary.
supersedes: []
source_of_truth_for: [itinerary-folio-integration-exploration]
---

# Itinerary × Folio integration exploration review

Date: 2026-07-13
Status: Working note; not canon
Scope: Review of the interactive Itinerary × Folio integration exploration

## Overall conclusion

The integration direction is materially closer to the intended single-trip architecture. It feels like one itinerary that acquires and sheds layers rather than an itinerary embedded inside a Folio.

The core architecture should continue, but the prototype needs several honesty, continuity, and interaction corrections before it is treated as canonical.

## What works

### The default state is a strong control

The default itinerary demonstrates that destination, dates, travelers, phase, chronology, and some emotional tone are already present without a Folio contribution. Every additional element can now be evaluated against a calm operational baseline.

### Contextual intelligence is the strongest integration pattern

The `Vesper noticed` treatment is:

- inside the affected day;
- immediately above the affected event;
- flat rather than dashboard-like;
- subordinate to the itinerary;
- capable of collapsing and decaying after resolution.

This is a credible replacement for Folio's persistent “what matters now” responsibility.

### The Memory threshold is correctly placed

Placing the closing observation and Memory doorway after the final itinerary event makes completion feel like an ending rather than a new homepage interrupting the record.

### The transition study is the correct evaluation tool

A single evolving phone exposes continuity problems and lifecycle boundaries better than a set of unrelated screens. It should remain part of the exploration.

## Corrections needed

### 1. Identity treatments do displace itinerary content

The exploration currently says the Tile and Strip displace nothing. That is not accurate:

- the 56px Tile increases the identity row's height;
- the Strip adds approximately 14px above the header;
- both move some itinerary content downward.

This cost may be acceptable, but it must be represented honestly. A more accurate evaluation is:

> Adds warmth at the cost of approximately one partial itinerary row.

The Tile communicates more value than the Strip. Continue testing:

- Identity Off;
- Identity Tile;
- Scrolled compact state.

The Strip probably does not provide enough recognizable place identity to justify another visual mode.

### 2. `Vesper noticed` exposes two actions

The intended rule is one sentence and one action, but the active intervention currently exposes both `Review` and `Nudge Theo`.

`Review` should be the single itinerary-level action. A subsequent decision surface can expose `Nudge Theo` if it remains relevant.

The expiry is also repeated in both the intervention and event row. Separate their roles:

- Intervention: `Ramiro's hold expires tonight. Theo is the last response.`
- Event state: `HELD · 23:00`

The intervention then explains why action is needed while the event row records booking truth.

### 3. Full Memory repeats destination identity

Once full Memory opens, the screen presents both the completed itinerary header and a second large destination hero. This creates two competing mastheads.

Full Memory should use dedicated subordinate chrome, such as:

`‹ Trip record` · `Trip memory` · `•••`

The illustrated Memory hero can then own the destination title. The completed date rail should remain with the itinerary record.

The full Memory state also contains an `Open trip memory` action after Memory is already open. Rename it to a real next action such as `Read the trip story` or `Share this memory`, or remove it.

### 4. The transition does not preserve one continuous trip

Several mock-data inconsistencies break the lifecycle illusion:

- the completed header says the Lisbon trip lasted five days;
- the completed date rail contains four days;
- the active date is Sunday the 15th while the body is Monday the 16th;
- the completion copy reuses a Kyoto-specific four-day observation about temples;
- `Dinner at Ramiro's` appears at noon on the final day.

The transition's argument depends on every date, event, phase, and generated sentence remaining continuous. Use one coherent fixture across every step.

### 5. The scroll-collapse transition is simulated rather than demonstrated

The `Scroll · identity withdraws` step turns identity off without visibly scrolling the itinerary. A scroll reference exists but is not connected to the phone's scrolling region.

The prototype should demonstrate the actual sequence:

`Tile header → body scrolls → tile contracts → ordinary compact header`

This is one of the primary behavioral questions the exploration is meant to answer.

### 6. Add an explicit Live beat

The sequence currently moves from planning and quiet history directly to completion. Add a Live state that proves the Folio contributions withdraw during the most operational phase.

Recommended sequence:

1. Identity greeting
2. Scroll collapse
3. Contextual attention
4. Resolution
5. Quiet history
6. Live operational purity
7. Completed record
8. Memory threshold

The Live beat should use the itinerary's Now/Next posture without an identity tile, persistent Folio summary, or Memory language.

### 7. Namespace the design-canvas identifiers

The transition section uses the generic section identifier `flow`. Persisted design-canvas state has already overwritten its title, leaving the transition section blank in canvas navigation.

Namespace the new section and artboard identifiers, for example:

- `folio-integration-intro`
- `folio-integration-default`
- `folio-integration-identity`
- `folio-integration-intelligence`
- `folio-integration-memory`
- `folio-integration-flow`

## Recommended disposition

- Canonical foundation: Default itinerary
- Canonical integration pattern: In-timeline contextual intelligence
- Canonical lifecycle boundary: Completed itinerary record → Memory threshold
- Continue exploring: Small identity Tile
- Probably remove: Identity Strip
- Keep outside itinerary canon: Full Memory composition

## Strategic implication

The Folio should no longer be a competing pre-trip or live homepage. Its valuable responsibilities can survive as trip identity, contextual intelligence, and post-trip Memory while the itinerary remains the single-trip home throughout the lifecycle.
