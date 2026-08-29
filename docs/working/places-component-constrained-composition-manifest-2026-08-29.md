---
doc_type: working
status: active
owner: founder / product / design / engineering
created: 2026-08-29
last_verified: 2026-08-29
expires: 2026-09-28
why_new: Digests the complete vesper-home-surfaces 2 export as a versioned component system, reconciles it with current source, and composes the four proposed Places states from existing vocabulary before naming genuine gaps.
promotes_to: null
supersedes: []
source_of_truth_for: []
depends_on:
  - docs/working/places-consumer-experience-anatomy-2026-08-29.md
  - docs/working/places-four-state-design-fixture-brief-2026-08-29.md
  - docs/systems/four-root-loop-object-surface.md
  - travel-agent/backend/core/models/places_sections.py
  - travel-app/components/places/PlacesSectionFeed.tsx
  - travel-app/components/places/PlacesFeedCardView.tsx
---

# Places Component-Constrained Composition Manifest

## Decision

Do not begin the next Places pass by inventing a new visual language or asking
a visual-design tool to discover the product structure.

The `vesper-home-surfaces 2` export already contains enough component
vocabulary to compose credible versions of:

1. **World Field**;
2. **Place Focus**;
3. **Place Path**; and
4. **Live Reduction**.

The missing work is mostly not “design another card.” It is:

- selecting and composing the existing parts around a persistent semantic
  state;
- producing the right evidence and relationships;
- preserving context as the person moves among map, Place, path, and live
  consequence; and
- adapting a small number of already-shipping Trips receipts for Places.

Only one genuinely new visible semantic family is clearly required: an
**attributed human observation** that can say what an authorized person
noticed about one Place without pretending that a save strip, a co-sign, or a
social feed means the same thing.

Everything else should first be attempted as a composition, data, state, or
interaction change using the existing system.

## 1. What was actually reviewed

The export is a project, not one flat mockup. Its files play different roles
and disagree in useful ways.

| File | What it is good for | Authority limit |
| --- | --- | --- |
| `README.md` | Identifies `Places - Whole Pages.dc.html` as the open/primary handoff canvas and says to follow imports | Handoff guidance, not product doctrine |
| `Places - Whole Pages.dc.html` | The most complete Places page-composition study: eight postures, mixed sections, density taper, and whole-page rhythm | A composition proposal; not a source ledger |
| `Places - The Page.dc.html` | The broadest Places component register: one-Place registers, sets, plans, reading, memory, people, and record | Mixes shipping components, proposals, superseded drawings, and impossible states |
| `Places - As Built.dc.html` | Source-read anatomy of the five shipping card families, four treatments, accessibility branches, and root states | Verified around August 11; not automatically current on August 29 |
| `Places - Proposed.dc.html` | Provenance for 33 earlier proposals and the reasons some moved or were cut | Explicitly superseded as a page proposal |
| `Whole Pages - Both Surfaces.dc.html` | D2/G2 containment conclusion and cold/home-city/away stress states | Older two-surface product model; useful for material logic, not current four-root ownership |
| `Build Manifest - Both Surfaces.dc.html` | Best bundle-level source ledger for reasons, producers, treatments, gates, containment, and drawn/build gaps | Reverified August 11; current source may have moved since |
| `Receipt Gaps - Cross-Surface.dc.html` | Cross-surface evidence and receipt analysis | Diagnoses proof grammar; does not define every destination |
| `Trips - The Page.dc.html` | Complete Plans/Trips component vocabulary, including 12 crown bodies, time, people, evidence, plans, maps, and trip feel | Adjacent-surface vocabulary; reuse must preserve role ownership |
| `Trips - Prototypes.dc.html` | Tests one stable crown anatomy and the receipt swaps needed across trip shapes | Prototype argument, not a Places page |
| `Trips - As Built.dc.html` | Shipping Trips anatomy and containment recipes | Adjacent implementation evidence |
| `Trips - Whole Pages.dc.html` | Trips whole-page compositions and real state mixes | Adjacent composition evidence |
| `Trips - Proposed.dc.html` | Superseded proposals and their categorization | Provenance only |
| `Canon - Home Surfaces.dc.html` | Vocabulary, containment, evidence, traffic between surfaces, and horizontal capability-building | Its three-surface state model predates Home / Chat / Places / Life |
| `support.js` | Generic Claude Design canvas runtime | No Vesper semantic components |

No `.dc.html` file imports another semantic component file. They all depend on
the generic canvas runtime and duplicate or lift drawings into each board.
Therefore “follow the imports” does not reveal a hidden component library. The
component system has to be reconstructed from repeated anatomy, source names,
status stamps, and the build manifest.

## 2. Currency rules

When two parts of the export disagree, use this order:

1. current backend and client source for what exists and renders now;
2. `Build Manifest - Both Surfaces` for the bundle's last source-verified
   state;
3. `Places - As Built` for anatomy and responsive behavior;
4. `Places - Whole Pages` for whole-page composition;
5. `Places - The Page` for proposed component vocabulary;
6. `Places - Proposed` for historical rationale, relocation, and rejection.

This resolves three concrete traps in the bundle:

- `saved_unvisited` is described as the sole orphan on August 11, but current
  source records that it was removed on August 14. It is neither a current
  reason nor a component requirement.
- `conviction` is fully drawn client-side but deliberately has no producer.
  It is not an unfinished wiring task.
- several frames in `Places - The Page` are legally renderable proposals but
  have no producer. Their absence from the app is a production/composition
  gap, not proof that the visual anatomy is missing.

## 3. Status vocabulary

This manifest uses five statuses:

| Status | Meaning |
| --- | --- |
| **Shipping** | Exists on a current render path, even if a gate limits reach |
| **Built-dark** | Client or server path exists but an explicit flag or honesty ruling keeps it unavailable |
| **Designed-legal** | The export contains a coherent component or arrangement that can use existing visual grammar, but it is not a normal current render path |
| **Relocated / superseded** | The idea belongs elsewhere or has been replaced by a stronger composition |
| **Cut** | The design investigation rejected the concept; do not revive it without new evidence |

“Shipping” does not mean verified on a physical device in every state. The
bundle explicitly found that many integrated families lacked fixture,
backend-real, denied-permission, offline, failed-image, and large Dynamic Type
evidence.

## 4. The normalized Places component system

### 4.1 Shell, scope, and state

| Component / role | Bundle state | Current code | Use in the new composition |
| --- | --- | --- | --- |
| Root shell and safe-area chrome | Shipping | `PlacesWorkspace`, `PlacesShell`, shared root header | Keep; it is the continuous surface envelope |
| Scope handle | Shipping/adapted | `PlacesScopeControl` exists; the root mostly presents scope through mast/header | Promote as the stable world handle; do not turn states into tabs |
| Search | Shipping | Scope-aware search in `PlacesWorkspace` | Keep as a temporary narrowing mode, not the Places identity |
| Map door | Shipping | `PlacesMapCanvas`, fallback list, pin peek, `/places/map` | Turn into an alternate medium over the same semantic selection |
| Root mast / standfirst | Shipping | `placesHomeMast`, `RootStandfirstVoice` | Use only when scope needs orientation; not on every ordinary open |
| Loading, error, cold offline, cached/partial notices, empty search | Shipping | `PlacesWorkspaceStateScreen`, `PlacesFeedNotice`, presentation model | Preserve exactly; new compositions must degrade through these states |
| Consequence banner | Shipping, cross-surface | shared `ConsequenceBanner` | Reserve for a real causal update, never ordinary editorial copy |
| Compact shell on scroll | Built but historically unwired | `PlacesShell` supports compact form; root now has morphing header behavior | Use if it preserves the scope/focal Place through depth |

### 4.2 The seven current renderer families

The current client registry is the cleanest code-level statement of the
shipping visual families:

| Renderer family | Wire kinds | Existing expression | Constraint |
| --- | --- | --- | --- |
| Candidate | `place` | 92-point plate row, one fact, one action label, optional save state | Common expression is uncarded; whole row owns the tap |
| Place register | `place` plus structured register | One Place with `verdict`, `change`, or `log` lower block | Evidence-first, non-recommendation; currently feature-gated at producer |
| Editorial | `city`, `area`, `angle` | Cover, area card, reading, fork, optional mirrored spine | Perspective is content, not permanent navigation |
| Experience | `experience` | 212-point rail or complete stacked rows at large type | Time/availability payload, not a generic image carousel |
| Memory | `memory` | Typographic memory object | A source-linked return, not an engagement prompt |
| Social | `friend` | One person leading to a set of saved Places | Currently too narrow for human observation or juxtaposition |
| Notice / prompt | `notice`, `prompt` | Urgent tonal notice or plain prompt | Notice can return value; prompt should not occupy output-led Home/Places by default |

The server still owns the section order, treatment, and action destination.
The client renderer registry selects visual grammar by kind and valid payload;
it does not infer a second ranking.

### 4.3 Treatments and arrangement

| Primitive | Status | What it means |
| --- | --- | --- |
| `single` | Shipping | Default section treatment |
| `choice` | Shipping | A bounded decision set; every `gap` card may be equally lead-worthy |
| `fork` | Shipping | Exactly two honest readings; no claim that one wins |
| `conviction` | Built-dark | One raised Place asserted as the fit for this viewer; blocked by lack of non-proximity confidence |
| Uncarded stack | Shipping | Default Places rhythm; illustrated or structurally strong rows need no box |
| Experience rail | Shipping | Horizontal availability/content rail; becomes full rows for large type |
| Responsive fork stack | Shipping | Width at or below 360 or font scale at or above 1.35 |
| Mirrored reading spine | Built-dark / internal | Alternate rendering of the existing two-angle fork; not new server vocabulary |
| Lead and siblings | Designed-legal | Hierarchy by scale, not by giving the lead a false conviction edge |
| Two side by side | Designed-legal | Comparison held by a hairline; suitable only for genuinely paired options |
| Set behind a door | Designed-legal with shipping contract support | A collection earns containment because the whole set is the object |
| Depth stack | Designed-legal | Uses overlap/depth instead of a mere numeric count |

### 4.4 One Place, six possible registers

`Places - The Page` contains one of the strongest abstractions in the bundle:
one shared Place anatomy whose lower block can answer six different questions.

| Register | Design status | Current contract | Proper use |
| --- | --- | --- | --- |
| Recommendation | Designed, blocked | Absent from register enum; conviction also dark | Only when Vesper has honest viewer-fit confidence |
| Verdict | Shipping-capable, gated producer | `PlacesRegisterRole.VERDICT` | What to actually do, order, or notice there, backed by a source-owned dossier fact |
| Apparatus | Designed, deferred | Absent from enum | Why a claim is believed, with source-per-claim attribution |
| Change | Shipping-capable, gated producer | `PlacesRegisterRole.CHANGE`; closures can attach it | A material then/now update |
| Caveat | Designed, deferred | Absent from enum | Typed dissent or a bounded reason against; silence is better without a dissent relation |
| Log | Shipping-capable, gated producer | `PlacesRegisterRole.LOG` | The person's dated relationship evidence, not a personality interpretation |

These are not six cards to stack or six tabs to expose. The current question,
freshest evidence, and consequence should select one or at most a tightly
paired combination.

### 4.5 Sets and collections

The bundle explores multiple arrangements without requiring new payload kinds:

- candidate rows — shipping workhorse;
- prominent lead plus compact siblings — designed-legal;
- two options in direct comparison — designed-legal;
- a collection behind one door — designed-legal and supported by current
  section `door` contracts;
- a visual depth stack — designed-legal;
- experience rail — shipping;
- dated event stub — designed-legal;
- section editor's note — the `note` field and typography already ship, but
  the producer pipe is usually dry.

The key rule is not “pick a card layout.” It is:

> Use scale for hierarchy, an edge for a real set-level object, and a door
> when the count has a meaningful destination.

### 4.6 Spatial and sequential compositions

| Composition | Status | Semantic job |
| --- | --- | --- |
| Map fragment | Designed in Places; map primitives ship elsewhere/current app | Explain a small spatial relation, not provide generic map coverage |
| Numbered walk | Designed-legal | Express a sequence whose order matters |
| Stretch map | Designed-legal | Same route/path object in spatial form |
| Day/trip sequence | Relocated to Plans/Trips | Bounded itinerary ownership |
| Full trip map | Trips/map screen | Trip-wide spatial structure |

The map and numbered walk are not competing features. They are two media for
the same composed path. A medium switch must preserve the path, selection,
and source context.

### 4.7 Reading and interpretation

| Component | Status | Keep / change |
| --- | --- | --- |
| Editorial cover | Shipping | Keep for a substantial interpretation with a clear destination |
| Two-reading fork | Shipping | Keep when two perspectives are both honest and neither wins |
| Responsive stacked fork | Shipping but superseded visually by spine exploration | Keep as accessibility fallback |
| Mirrored spine | Internal/designed | Useful for paired reading; do not make it a permanent root grammar |
| Lens switcher | Designed | Treat as an authoring/debug vocabulary, not six consumer tabs |
| Preview registers | Designed | Useful to choose the correct semantic form before rendering |
| Overlay lens geometry | Designed using shipping geometry | A presentation option, not a distinct content type |

### 4.8 Memory and continuity

| Component | Status | Job |
| --- | --- | --- |
| Memory card | Shipping | One sourced memory returned at a meaningful time |
| Postcard memory | Designed | Richer single memory with artifact presence |
| Shelf | Designed | Compact archive/continuity door across trips or occasions |
| Postcard row | Designed | Several memories where image and date do real work |
| Go Back | Designed | A current return possibility grounded in prior relationship and new world truth |

G2's material decision remains useful: illustrated discovery can stay flat;
typographic record sometimes needs a contained surface so it does not vanish.
That is a material rule, not a license to make the record dominate every page.

### 4.9 People and relationship

| Component | Status | What it can honestly say |
| --- | --- | --- |
| Friend strip | Shipping | One authorized person's saved Places in a trip-scoped context |
| Co-sign | Designed; contract gap | Several people support one Place |
| Again? | Designed | A shared prior outcome creates a bounded return possibility |
| Trip marker | Designed from existing relationship marker data | This Place belongs to or affected a trip |
| Belonging scale | Designed; data-limited | Accumulated relationship strength without pretending precision |
| Tally | Designed | Counted record where the count itself has meaning |
| Your rhythm | Designed | Temporal recurrence shown factually |
| The rest | Designed but not a normal section | Feed-level remainder / stopping logic |

The shipping friend strip is not enough for the emerging product. It encodes
“person → saved set.” It cannot honestly express:

- “Maya noticed that this return becomes unreliable after 6 PM”;
- “three friends reached the same conclusion for different reasons”;
- “a friend in Paris experienced a useful contrast at the same time”; or
- “this prior group outcome changes what works now.”

Trying to squeeze those meanings into the existing friend strip would be a
semantic error even if the pixels fit.

### 4.10 Current Places reasons

The August 11 bundle manifest listed 17 reasons. Current source contains 16:

```text
gap · expiry · group_waiting · nearby_set · neighbourhood · anniversary
unfinished_guide · friend_activity · saved_unplaced · changed · harvest
starter · guide · experiences · saved · register
```

Current distinctions:

- `saved_unvisited` was removed on August 14 and should not drive new design;
- `saved_unplaced` and `register` have producers but are default-off;
- `conviction` remains deliberately producer-less;
- `register` supports only verdict, change, and log;
- apparatus, caveat, and recommendation remain absent for explicit evidence
  reasons.

### 4.11 What each primary whole-page composition contributes

`Places - Whole Pages` should not be read as eight products or eight fixed
templates. It is a stress test showing which components become available and
how the page length changes as evidence changes.

| Canvas page | Component mix it demonstrates | Durable lesson |
| --- | --- | --- |
| Starter | experiences, nearby candidates, area, editorial reading, shallow saved continuity | A cold surface can be all illustrated/flat and still carry presence; no memory substrate should be invented |
| Between | saved set, anniversary memory, editorial cover/lens, nearby candidates, change notice | Ambient browse may mix discovery, return, and current change; posture should not force one content type |
| Planning | numbered path, paired reading, area, experience, saved candidates | A bounded plan can lift composed and trip-relevant material without making all of Places a planner |
| Ready | composed path, dated experiences, editorial cover, direct comparison, collection stack | Fewer items can become more concrete as an Occasion approaches |
| Live | map rendering of the composed path, editor's note, experience, area, reading, nearby alternatives | The same path can switch from sequence to space; the note says why the unit exists |
| Returned | Go Back, memory/record, reading, nearby, friend material, changed Place | Return value should mix present openings with record; it should not become a retrospective report |
| Trip scope | composed path, reading, nearby, experiences, friend activity | This is the only canvas state matching the current trip-only multiplayer gate; that gate is implementation history, not the long-term social philosophy |
| Quiet | experiences, map fragment, area, shelf, reading, record, change, saved collections | Quiet means user-chosen browsing and no invented urgency; it does not mean empty or unengageable |

The board's strongest page-level finding is the **density taper**, not one of
the named postures. It is the only rhythm study that changes both height and
emphasis: express the strongest composition fully, compress the middle, turn
the tail into doors, then stop.

## 5. The reusable Trips/Plans vocabulary

The four-state Places proposal should reuse adjacent product grammar where the
semantic job is already solved. Reuse does not mean Places takes over Plans.

### 5.1 Crown receipt bodies

The Trips canvas and code contain these proof forms:

| Receipt | What it proves | Places use |
| --- | --- | --- |
| Call | Named trouble, stake, or deadline | A live access failure or expiring opportunity |
| Diff | Before / after and optional impact | A changed Place fact or fallback substitution |
| Candidates | Several options and optional leader | A live reduced set; leader only with honest evidence |
| Checklist | Closed / total and unresolved work | Remaining live burden, not a homework list for the user |
| Ledger | Direction and counterparties | Who owes or supplied what in a shared Occasion |
| Spine | Days, ranges, or ordered segments | Temporal structure of a path or open interval |
| People | Seats, invitees, empty capacity | Occasion participation, not ambient friend presence |
| Shape | Moments/days/themes | Aggregate occasion/trip form, not a Places default |
| Conditions | Current condition and temperature | Live feasibility when materially relevant |
| Waveform | Duration | Audio/podcast or time-bounded content artifact |
| Stamp | Grounded fallback when no richer proof exists | Honest floor; preferable to a fabricated insight |
| Near you | Fresh location-gated possibilities | World Field or Live Reduction when location is authorized and current |

The receipt prototypes contribute three rules that Places should inherit:

1. show the most specific true identity in the lead slot;
2. omit a receipt when there is no grounded proof rather than dressing up a
   reason as evidence; and
3. distinguish exact from estimated route or timing claims.

### 5.2 Other reusable components

- `TripsNowBand` — a compact temporal seam when “now” genuinely changes the
  reading;
- `TripsConditionsBand` — passive condition evidence;
- `TripsCountdownCard` — only when a real deadline governs the state;
- `TripsOpenLoopsCard` — resolvable work receipt, but dangerous on Places if
  it reads as homework;
- `TripDayMapCard` — map-as-editorial-evidence precedent;
- `TripsGroupSection` / facepile / seat — group state when the group is an
  actual Occasion owner;
- `ListRow` and `TableCard` — compact doors and evidence rows;
- `ConsequenceBanner` — causal repair or confirmed downstream result;
- containment recipes from step 0 through step 5 — reuse the material scale,
  not local hand-rolled cards.

For Places, the checklist must describe **what Vesper has resolved and what
still affects feasibility**, not tasks assigned to the person. Example:

```text
3 of 4 constraints resolved
ferry current · weather current · return route current
restaurant walk-in status unknown
```

That is a receipt of Vesper's work. “Confirm weather / choose a route / add a
restaurant” is homework and violates the output-led role of Places.

### 5.3 Complete Trips component register and its relevance

The rest of `Trips - The Page` matters because it prevents Places from
inventing variants of already-solved product jobs.

| Group | Components in the canvas | Places conclusion |
| --- | --- | --- |
| Time | Now/Tonight band, temporal strip, countdown | Reuse a seam or deadline receipt only when time changes the decision; bounded itinerary time remains Plans-owned |
| People | room, CONNECT trail, seat, Your People | Reuse for actual Occasion membership or invitation state; do not convert into ambient friend tracking |
| Evidence / comparison | conditions, work receipt, compare foot, open loops, price ladder, comparison table | Conditions and proof receipts can cross surfaces; price and booking comparison remain with the bounded decision owner |
| Stack | Also In Play, visual depth, draft shelf | Compactly express other active plans or drafts; do not turn Places into a queue |
| Plan scope | Local Plans, local plan, occasions without plans, occasion register, hosting | These are handoff/destination objects from Places, not sections Places should own |
| Approach | Companion Reading, This Week, This Weekend, Saved Unplaced | Reading and near-term openings can project into Places; the collection owner and temporal owner stay explicit |
| Return | Return / story ready, Since You Last Looked | Reuse only when a readable Artifact or changed state exists; avoid generic “reflect on your trip” prompts |
| Page voice | mast, standing ask, voice ask, offer | Offers can clarify an available capability; asks should stay sparse on an output-led surface |
| Maps | Today Mapped, unroutable/estimated leg, crossing, trip whole, where everyone is, neighbourhood wash, photos on the ground, reachable-now cluster | Reuse exact/estimated route disclosure, crossings, and reachability; person maps require explicit group scope and grants |
| Trip feel | current feel, state switch, what remains, one contrast, asked-not-shown | Useful as an internal state/debug model; do not expose it as a user-facing control panel in Places |

`Trips - As Built` also establishes the shared containment roles:

- crown / finishable object at the strongest step;
- quiet receipt for one resolved proof object;
- outlined group for a navigable set;
- flat object for a reader;
- uncarded section for ordinary page rhythm; and
- banded seams for time or conditions.

Places should reuse those meanings. It should not copy Trips' contained ratio.
G2 reached the opposite material conclusion: on Places, imagery often gives
discovery enough presence, while typographic record may need containment.

## 6. Components that should remain out

The proposal ledger already rejected or relocated several ideas. Do not
rediscover them as “new” components.

| Idea | Status | Reason |
| --- | --- | --- |
| Index | Cut | Density without weight |
| Chip field | Cut | Taxonomy browsing with no meaningful rows |
| Contact sheet | Cut | Image density without semantic hierarchy |
| Permanent status board | Relocated to Home | Time-bound state belongs in the present-facing surface |
| The Move | Relocated to Home | An expiring attention atom, not a Places section |
| Temporal strip as itinerary ownership | Relocated to Plans/Trips | Bounded plan time belongs to the plan owner |
| Price ladder / comparison table as booking work | Relocated to Plans/Trips | Decision logistics, not Places identity |
| Raised Places return crown | Deferred | No accepted return selector or reliably readable artifact destination |
| Conviction | Built-dark | No honest non-proximity fit signal |
| “Rest” as a normal section | Superseded | Stopping is a feed/composer rule, not content to render |

## 7. Four states assembled from the existing vocabulary

The compositions below are deliberately constrained. Each line names an
existing bundle or production component. A new visual component is allowed
only where the existing semantics cannot carry the meaning.

### 7.1 World Field

**Purpose:** orient within one current spatial scope and expose a small number
of materially different openings.

| Order | Existing component | Adaptation |
| --- | --- | --- |
| 1 | Scope handle + root header actions | `NEW YORK`; search and map remain utilities |
| 2 | Editor's note | One sentence stating the current basis, only if it adds a reason such as an explicit open interval |
| 3 | Map fragment / current map canvas | Small spatial field containing the lead set, current anchor, and material route geometry |
| 4 | Lead and siblings | One prominent Place plus two compact alternatives; hierarchy comes from scale, not `conviction` |
| 5 | Candidate rows | Additional branches only when their reason differs materially |
| 6 | Existing one-Place `change` or `verdict` register | One returned understanding when it changes how the field is read |
| 7 | Friend strip only for its current meaning | An authorized person's saved set; do not use it for an observation |
| 8 | Set behind a door / depth stack | Saved, reading, or continuity collection with a real destination |
| 9 | Density taper | Compress lower-value continuity doors and stop |

What is not needed:

- a new “world card”;
- a universal hero;
- a permanent mast explaining Places;
- a feed of Reading / Events / Friends / Nearby in fixed order; or
- a new map visual language.

The missing implementation is a **World Field composer/producer** that can
choose one bounded set, its reasons, and one shared map extent. The visual
vocabulary is already present.

### 7.2 Place Focus

**Purpose:** make one Place intelligible as stable world truth, current
affordance, personal relationship, and relevant perspective.

| Order | Existing component | Adaptation |
| --- | --- | --- |
| 1 | `ObjectPageShell` / `PlaceHero` / `SpotTopBar` | Stable identity, status, image, and exact back context |
| 2 | `PlaceAreaMap` or `MapSummary` | Show where the Place sits only when geometry explains something |
| 3 | One-Place register anatomy | Select `verdict`, `change`, or `log`; do not show the register taxonomy |
| 4 | Relationship marker + factual log | Saved, chosen, visited, returned, people, and dates only when supported |
| 5 | Editorial cover or two-reading spine | One or two meaningful perspectives, chosen by the current question |
| 6 | Editor's note / apparatus drawing | Source or limit note attached to the claim it qualifies |
| 7 | Existing experience stub or candidate row | Current consequence or nearby continuation |
| 8 | Go Back or set door | Return/continuity only when a current opening exists |

The current `EntityObjectPage` already proves that identity, current
situation, Take, relationship, facts, and Ask can live in one detail
destination. The work is to replace a feature-stack feeling with one selected
reading and a clear path outward.

The missing work is not a new Place-detail card. It is:

- a one-Place composition contract that selects the right register;
- source and relationship projection into that contract; and
- state-preserving entry and return from the World Field.

### 7.3 Place Path

**Purpose:** follow one meaningful edge from the focal Place—a comparison,
route, source, person, prior experience, or hidden system—without losing the
Place.

| Order | Existing component | Adaptation |
| --- | --- | --- |
| 1 | Compact Place identity / scope handle | Keep focal Place and origin visible |
| 2 | Editorial cover or paired spine | State the path proposition and the two connected subjects |
| 3 | Map fragment | Show the spatial relation if geometry carries the claim |
| 4 | Numbered walk | Show ordered movement if sequence carries the claim |
| 5 | Apparatus register drawing | Claims and sources, attached locally rather than as a bibliography dump |
| 6 | Editor's note / caveat drawing | Bound the analogy or name what does not transfer |
| 7 | Candidate row, experience stub, or Go Back | One consequence: follow, use now, save, or return |

For the Red Hook ↔ Sorrento fixture, the comparison can use the existing
paired reading spine, map fragment, numbered walk, apparatus, and editor's
note. No new “connection graph card” is required.

The missing implementation is a **typed path object and navigation envelope**:

```text
origin + focal Place + edge kind + connected subject(s)
+ selected claims/Sources + current interval + return destination
```

That is architecture and interaction state, not visual invention.

### 7.4 Live Reduction

**Purpose:** compress the same Place/path toward what works under current time,
conditions, commitments, and uncertainty.

| Order | Existing component | Adaptation |
| --- | --- | --- |
| 1 | `TripsNowBand` or compact scope seam | Current interval and end constraint; omit if time is not decisive |
| 2 | `TripsConditionsBand` | Weather/access/service conditions only when material |
| 3 | Map fragment + numbered walk | Current route and sequence as two views of one plan candidate |
| 4 | Checklist receipt | What Vesper resolved and what remains unknown; never assign chores |
| 5 | Candidates receipt or candidate rows | Viable alternatives if the preferred path fails |
| 6 | Diff receipt or Places notice | Exact change from the prior state and its consequence |
| 7 | Existing action row / typed handoff | `Use this interval`, `Open in Plans`, `Book`, or `Save`; owner performs the mutation |
| 8 | Consequence banner after action | Confirm the actual downstream effect and provide repair/undo where appropriate |

No new “live mode” screen chrome is required. Live Reduction is a posture over
World Field, Place Focus, or Place Path. Plans/Trips still owns the committed
schedule and group plan; Places owns the spatial understanding and hands the
bounded consequence to the proper owner.

## 8. True gaps after the constrained assembly

### 8.1 New visible semantic component: attributed human observation

This is the only clear new visible family.

Required payload:

```text
author identity
audience / may-use / may-name state
Place or path subject
bounded observation
observed_at and freshness
source Artifact or Occasion, when present
relationship/context line, only when authorized
action destination
revocation/correction behavior
```

It may reuse the friend avatar, editor's-note typography, source apparatus,
and candidate-row action anatomy. It still deserves a distinct semantic
renderer because “a person noticed X” is not “a person saved these Places.”

### 8.2 Composition and producer gaps

- World Field composer: selects a finite spatial set and one shared reasoned
  field rather than independently ranked sections.
- Place Focus composer: selects one register and the minimum supporting
  evidence around one Place.
- Place Path object/composer: resolves one meaningful edge and the proper
  media for it.
- Live reducer: derives current feasibility, unknowns, fallbacks, and the
  correct owner handoff.
- one-Place producer beyond the currently gated evidence-first register.

### 8.3 Data and evidence gaps

- visit/return signal for local Places;
- non-proximity viewer-fit confidence if conviction is ever reconsidered;
- source-per-claim attribution for apparatus;
- typed dissent relation for caveat;
- current transit/access/conditions authorities for live reduction;
- governed human observation projection beyond trip-scoped saved-place
  activity;
- exact/estimated status on routes and timings; and
- readable Artifact and Outcome destinations for return expressions.

### 8.4 Interaction gaps

- one state envelope preserved through root, map, Place, path, and live
  reduction;
- synchronized map pin, row, selection, viewport, and back-scroll state;
- exact return from a Home proposition to the originating Home position;
- medium switching without requerying or losing the followed path;
- typed handoff to Plans/Trips, booking, Chat, or Life without duplicate
  ownership; and
- consequence/repair after a delegated action.

### 8.5 Refactoring gaps, not visual gaps

- make Trips receipt bodies reusable outside the crown shell while retaining
  grounded/absent rules;
- adapt condition, candidate, diff, checklist, and spine receipts to Places
  composition contexts;
- keep all containers on the shared containment scale instead of introducing
  local radius/fill/elevation objects;
- make editor's-note and source apparatus production-addressable; and
- expose current Place identity and scope consistently across root and detail
  routes.

## 9. What should be drawn next

The next dedicated design-tool brief should not ask for “a new Places home.”
It should ask for one component-constrained board with:

- the same Red Hook evidence world across all four states;
- every visible unit labeled with its source component family;
- one badge for `shipping`, `built-dark`, `designed-legal`, or `new gap`;
- no new component unless the board records why every existing family fails;
- a second pass at large Dynamic Type and failed/absent imagery;
- a map/composition switch showing preserved selection;
- back transitions showing exact restored origin; and
- one output-led quiet state with no prompt card.

The board should compare only two decisions:

1. **composition:** which existing units earn prominence, compression, or
   omission in each state; and
2. **semantic sufficiency:** where an existing component would misstate the
   evidence even if it looked acceptable.

It should not spend time on colors, illustration style, icon language, or
pixel-perfect card geometry yet.

## 10. Final interpretation

`vesper-home-surfaces 2` is richer and more coherent than its current whole
pages make it appear. It already contains most of the atoms for the emerging
Places product:

- a spatial field;
- one Place in several evidence registers;
- sets and comparisons;
- maps and sequences;
- interpretations and sources;
- memory and return;
- social traces and group evidence;
- temporal/condition receipts; and
- graded containment and density taper.

What it does not yet contain is the **spine that composes those atoms as one
continuous encounter**. That spine is not another component. It is the state
and selection grammar:

```text
scope
  -> focal Place
  -> meaningful path
  -> current consequence
  -> owner handoff
  -> preserved return
```

The right next step is therefore to compose from the existing vocabulary and
prove the state transitions. Visual exploration should refine the result
after the semantic assembly—not substitute for it.
