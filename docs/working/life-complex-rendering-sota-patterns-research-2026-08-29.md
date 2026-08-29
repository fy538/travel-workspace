---
doc_type: working
status: active
owner: founder / product / design / frontend / architecture
created: 2026-08-29
last_verified: 2026-08-29
expires: 2026-09-28
why_new: Researches complex consumer surfaces and dynamic frontend systems to derive a state-of-the-art rendering, transition, performance, compatibility, and fixture strategy for Life without authorizing a server-driven component tree or a universal card renderer.
promotes_to: null
supersedes: []
source_of_truth_for: []
depends_on:
  - docs/decisions/2026-08-29-adopt-life-continuity-and-return-contract.md
  - docs/working/life-index-and-episode-anatomy-contract-2026-08-29.md
  - docs/working/life-six-world-fixture-execution-report-2026-08-29.md
  - travel-app/docs/working/adaptive-experience-composition-contract-and-lab-2026-08-27.md
---

# Life Complex-Rendering SOTA Pattern Research

## Question or outcome

What can Vesper learn from applications and engineering systems that render
heterogeneous, longitudinal, viewer-relative, highly dynamic interfaces—and
which patterns should Life adopt or explicitly reject?

## Executive finding

No one reference app solves Life. The strongest contemporary systems converge
on a layered architecture:

```text
canonical domain truth
  -> viewer-relative semantic projection
  -> stable section hierarchy
  -> bounded native treatment registry
  -> granular diffing and virtualization
  -> identity-preserving motion
```

The winning pattern is **not** a universal card and **not** a server-authored
component tree. It is a hybrid:

- the backend/read layer decides **what exists, what is true, who may see it,
  what job it serves, and which semantic regions are present**;
- the mobile client decides **how those regions render, reflow, move, respond,
  degrade, and remain accessible**.

The deeper pass adds a second conclusion: Life needs **two cooperating native
renderers**, not one increasingly general surface. A light virtualized index
owns retrieval and orientation; a finite episode composition owns expressive
media and detail. Both resolve the same semantic identity, ResourceRefs,
viewer scope, and revision.

This directly supports the current adaptive-composition contract, which
already rejects server-supplied coordinates, typography, gestures, navigation,
and arbitrary component trees.

### What the deeper pass changed

The first pass selected the hybrid semantic-projection architecture. The
second pass makes five sharper commitments:

1. **Split collection rendering from expressive rendering.** Life index and
   episode composition are cooperating renderers over one identity system.
2. **Restore targets, not pixels.** Lenses, deep links, and process restoration
   resolve a semantic anchor under current authority before applying local
   reading position.
3. **Treat cache scope as authority.** Together content is viewer- and audience-
   epoch-bound and must be synchronously purgeable; refetch is not revocation.
4. **Require a linear semantic equivalent.** Map, graph, collage, audio, and
   spatial comparison cannot ship without an ordered accessible reading.
5. **Extend existing native labs.** Travel App already has the appropriate dev,
   Maestro, screenshot, and performance infrastructure; adding a second UI
   workbench is not justified yet.

## 1. Product precedents

### 1.1 Apple Photos — one corpus, several curated entrances

Apple Photos organizes one media library into collections such as Memories,
People & Pets, Albums, Recent Days, and pinned collections. It also permits
large, small, mixed, or collapsed collection treatments; user reordering; and
Personal, Shared, or Both library scope. See [Apple Photos
Collections](https://support.apple.com/en-ie/guide/iphone/iph4f36c4148/26/ios/26).

**Pattern to borrow:** one corpus can support several curated entrances and
user-authored shortcuts without creating copies or requiring one fixed density.

**Life translation:** Combined/Mine/Together, period doors, Across time,
Returns, and pinning can coexist over one governed corpus. Pinning changes
access, not semantic type.

**Warning:** Photos can tolerate a media-first default because every canonical
item is media. Life cannot; its primary units include Plans, Occurrences,
Occasions, Outcomes, Sources, and compositions.

### 1.2 Notion — stable objects, multiple views, progressive detail

Notion renders the same database through table, board, list, calendar, gallery,
timeline, chart, and other views. Each view can own layout, property visibility,
filtering, sorting, and grouping, while an item can open in side peek, center
peek, or full page. See [Notion database
views](https://www.notion.com/en-gb/help/views-filters-and-sorts).

**Pattern to borrow:** the object is stable while projection and detail depth
change. Context can remain interactive while detail opens.

**Life translation:** Timeline, Map, Sources, and episode detail should be
viewer projections over the same ResourceRefs. A compact episode doorway may
expand progressively without changing identity.

**Warning:** Notion exposes database configuration to the user. Life must
compile useful views automatically and keep repair lighter than database
administration.

### 1.3 Google Maps Timeline — several spatial-temporal lenses with correction

Google Maps Timeline exposes day/calendar retrieval plus Places, Cities, and
World lenses. It allows a person to edit a Place or visit time, while Place
detail can link back to visit history. Timeline is opt-in and supports deletion.
See [Google Maps Timeline](https://support.google.com/maps/answer/6258979/google-maps-timeline-computer?co=GENIE.Platform%3DAndroid&hl=en-GB).

**Pattern to borrow:** day, Place, city, and world are ways into the same
history; correction belongs beside the projection where an error is visible.

**Life translation:** Timeline and Map should preserve an episode's identity,
truth state, and correction path rather than become separate archival products.

**Warning:** raw location history overproduces apparently precise Occurrences.
Vesper must keep ticketed, planned, source-only, unresolved, and occurred state
separate and avoid surveillance as a product premise.

### 1.4 Apple Health — heterogeneous sources, summary, category, trend, detail

Apple Health combines sensor data, Apple Watch, health providers, third-party
apps, connected devices, and manual entries; it renders summaries, highlights,
trends, categories, and detailed records while keeping source permissions
separate. See [Apple Health data](https://support.apple.com/guide/iphone/intro-to-health-data-iphbb8259c61/26/ios/26).

**Pattern to borrow:** heterogeneous provenance does not require one visual
shape. Summary, trend, category, and raw detail can coexist when sources and
authority remain inspectable.

**Life translation:** episode spine, See anew, longitudinal Place reading, and
Source inspection should be separate levels over the same evidence.

**Warning:** health metrics have relatively regular numeric schemas. Life's
social meaning, narrative evidence, and negative occurrence truth are more
irregular and require stronger abstention.

### 1.5 Strava — a stable activity with specialized analytic lenses

Strava keeps an activity as the stable unit while maps, route, analysis, media,
and privacy remain attached; its Personal Heatmap adds longitudinal filtering
by activity type and date and can include or exclude private activities and
media. See [Strava Personal
Heatmaps](https://support.strava.com/en-us/articles/15402028-personal-heatmaps).

**Pattern to borrow:** specialized treatments can orbit a stable episode and
inherit explicit privacy/filter state.

**Life translation:** a Journey or Occasion may expose Map, Timeline, people,
and Sources without each becoming a separate owner.

**Warning:** intensity, frequency, and achievement are central to fitness but
are dangerous proxies for meaning in Life.

### 1.6 Spotify Wrapped — eligibility-gated, bounded immersive composition

Spotify Wrapped uses participation thresholds, excludes private/profile-
excluded activity, sequences eligible stories, lets people control playback
speed and revisit moments, and exposes bounded share cards. See [Spotify 2025
Wrapped](https://newsroom.spotify.com/2025-12-03/2025-wrapped-user-experience/).

**Pattern to borrow:** generated storytelling should be eligibility-gated,
bounded, replayable, and separately shareable rather than always-on.

**Life translation:** Returns and See anew can use immersive or sequenced media
when substance and authority pass thresholds. They remain derived compositions,
not the Life index itself.

**Warning:** annual spectacle and superlatives would turn Life into performance
and identity scoring. Vesper should borrow eligibility and bounded playback,
not recap theater as the default.

### 1.7 Apple Journal — entries stay stable while retrieval changes

Apple Journal can retrieve the same entries through full-text search, media and
location filters, calendar dates, bookmarks, and a Places map. Entry Date and
Moment Date remain distinct rather than being collapsed into one apparently
precise time. Its suggestion inputs can also be controlled by category and are
processed privately on the device. See [Apple Journal search and
views](https://support.apple.com/en-ie/guide/iphone/iph6257be047/ios) and
[Journal suggestion settings](https://support.apple.com/en-gb/guide/iphone/iphf965002cf/ios).

**Pattern to borrow:** retrieval lenses should not mutate the record, and the
system should preserve the difference between when something happened and when
it was authored or saved.

**Life translation:** Timeline, Map, Sources, search, and bookmarks/pins can all
lead to the same episode or Source without manufacturing copies. Occurred time,
Plan time, Source time, contribution time, and composition time need explicit
roles in the projection contract.

**Warning:** Journal is still entry-centric and writing-centric. Life must not
require a person to produce prose or turn evidence into a journal entry before
it can become useful.

### 1.8 Google Photos — compression without destructive merging

Google Photos can automatically collapse similar media into a stack, select a
top pick, expand the stack into a filmstrip or grid, and let a person decide
whether an action applies to the selected item or the whole stack. Its Places
view coordinates a map, visible-area photo grid, and optional day path. See
[Google Photos stacks](https://support.google.com/photos/answer/14169846?co=GENIE.Platform%3DAndroid&hl=en)
and [Google Photos map and
Timeline](https://support.google.com/photos/answer/6153599?co=GENIE.Platform%3DAndroid&hl=en).

**Pattern to borrow:** visual compression must preserve membership, expansion,
and action scope. A coordinated map and list are two synchronized views, not
two independent copies.

**Life translation:** a burst of meal photos, tickets for one transfer, or
several Sources supporting one occurrence can collapse into an evidence bundle
without becoming one artifact. Bulk actions must say whether they affect the
representative, the bundle, or the episode.

**Warning:** similarity is sufficient for photo cleanup but not for semantic
episode formation. Life's grouping threshold must be evidence- and
relationship-aware, and every inferred group must remain repairable.

### 1.9 Day One — one corpus through time, media, map, and calendar

Day One exposes Timeline, Photos, Map, and Calendar over one journal corpus,
and its calendar can open a day summary with entries, Photos, Places, and
Events. It also supports entry-to-entry links and targeted deep links. See [Day
One journal views](https://dayoneapp.com/guides/tips-and-tutorials/journal-views-in-day-one-for-macos/),
[Calendar view](https://dayoneapp.com/guides/tips-and-tutorials/calendar-view-in-day-one/),
and [entry linking](https://dayoneapp.com/guides/tips-and-tutorials/linking-journal-entries/).

**Pattern to borrow:** the same durable object should be addressable from every
lens, and contextual day/place summaries can surround it without changing its
identity.

**Life translation:** every stable Life door needs a canonical deep link;
Timeline, Map, search, Home returns, notifications, and Together compositions
should converge on that address and viewer scope.

**Warning:** Day One asks the person to maintain the journal. Vesper should
automatically organize supported evidence and make correction cheaper than
authorship.

### 1.10 Personal information management — keeping and re-finding are different

Personal-information-management research distinguishes **keeping**—moving from
encountered information toward an anticipated future need—from **finding and
re-finding**, which move from a present need toward previously encountered
information. It also warns that keeping too much creates competition for
attention and can obscure what is useful now. See [Jones on keeping
decisions](https://firstmonday.org/ojs/index.php/fm/article/view/1123) and the
[PIM research synthesis](https://arxiv.org/abs/2107.03291).

**Pattern to borrow:** capture, organization, re-finding, and use are one
information lifecycle but not one interaction. Life should absorb much of the
organization cost and support both recognition-based browsing and direct
retrieval.

**Life translation:** Sources can enter through Chat with almost no filing;
Life later exposes period, place, people, Source, and search landmarks; an
episode opens into useful context and Continue. The person should not need to
predict the correct folder, tag, or future use at capture time.

Research on heterogeneous personal data has also explored temporal zoom, where
the visible representation changes with time scale rather than merely shrinking
the same object. See [organization and exploration of heterogeneous personal
data](https://link.springer.com/article/10.1186/2192-1962-2-1).

**Life translation:** index-to-episode is a form of semantic zoom. At year or
period scale, show recognition anchors and earned structure; at episode scale,
show the event/evidence anatomy; at Source scale, show claim-local provenance.
Do not render the same card at three physical sizes.

## 2. Engineering precedents

### 2.1 Shopify Shop — server selects sections; client owns renderers

Shopify's Shop app moved store-section presence and layout selection to the
server while keeping a native top-level screen, section container, typed
section renderers, navigation callbacks, and client fallback layouts. Unknown
layout types fall back to a client-defined default for compatibility with older
versions. See [Shopify's server-driven UI
architecture](https://shopify.engineering/server-driven-ui-in-shop-app).

**Pattern to borrow:** server-selected semantic sections plus a bounded client
renderer registry and explicit unknown-version fallback.

**Life translation:** the server may return `period_spine`, `episode_door`,
`across_time`, `return`, or `source_bundle` semantics. It must not return a tree
of arbitrary `View`, font, margin, and gesture instructions.

### 2.2 DoorDash Facets — semantic view models, stable IDs, and the failure of
domain-coupled heterogeneous arrays

DoorDash reports that an earlier heterogeneous component-array response was
prone to deserialization errors and that coupling UI components to backend data
models forced changes across services. Its later Facet system describes view
semantics, events, nesting, layout/style tokens, logging, and unique IDs used
for diffing and caching. See [DoorDash's generic server-driven UI
components](https://careersatdoordash.com/blog/improving-development-velocity-with-generic-server-driven-ui-components/).

**Pattern to borrow:** decouple domain storage models from surface projection;
give every rendered instance stable identity; centralize consequence semantics
outside leaf components.

**Pattern to reject:** an unbounded `custom` payload or backend-defined styling
becomes a second, weakly typed UI framework. Vesper should keep a smaller
semantic schema than DoorDash's general marketplace system.

### 2.3 Airbnb Epoxy and unidirectional data flow — declarative complex screens
with stable identity

Airbnb's Epoxy powers dynamic screens through declarative models, custom native
views, stable IDs, automatic diffing, layout variants, and saved transient view
state. Airbnb's recent SwiftUI work keeps unidirectional data flow and focuses
on preventing unnecessary re-evaluation through diffable, value-semantic
inputs. See [Epoxy for
Android](https://airbnb.tech/opensource/epoxy-for-android/) and [Airbnb's
SwiftUI performance work](https://airbnb.tech/web/understanding-and-improving-swiftui-performance/).

**Pattern to borrow:** immutable, diff-friendly presentation models; stable IDs
separate from revision; local transient state keyed to those IDs; leaf-level
updates rather than whole-screen rerenders.

**Life translation:** when Maya's lane is revoked, only the affected episode
subtree, composition, and related controls should recompile—not every period
and media item in Life.

### 2.4 Meta Litho Sections — a section tree over several data sources

Meta's Sections represents a scrollable surface as a hierarchy whose internal
nodes are sections and leaves are components. The framework calculates minimal
changes and allows different subtrees to be powered by different sources. Meta
reported significant performance improvements on complex scroll surfaces. See
[Litho Sections](https://engineering.fb.com/2017/10/26/android/open-sourcing-sections-declarative-data-handling-for-litho-lists/).

**Pattern to borrow:** Life is naturally a semantic section tree. Each subtree
can update from its relevant owner while preserving a single scroll and stable
index hierarchy.

**Warning:** Vesper does not need to reproduce Litho. It needs the same
declarative boundary in React Native: pure projection-to-section resolution,
stable keys, and granular subscriptions.

### 2.5 Spotify Encore — layered abstraction and slots

Spotify's design-system work argues that fully configured complex components
are useful until their parent APIs accumulate too many props. Slot-level
abstraction lets local products replace or extend subcomponents without losing
shared structure, routing, analytics, and design-system behavior. See [Spotify
Encore's abstraction layers](https://engineering.atspotify.com/2023/5/multiple-layers-of-abstraction-in-design-systems).

**Pattern to borrow:** common Life anatomy should expose bounded semantic slots,
not a mega-component with dozens of booleans and not total local freedom.

**Life translation:** `EpisodeShell` can standardize identity, truth, scope,
accessibility, motion boundary, provenance access, and repair while Journey,
Occasion, and Place-relationship renderers provide their own story-spine,
people, Source, and See-anew slots.

### 2.6 Slack Block Kit — bounded vocabulary plus a fixture builder

Slack Block Kit composes app surfaces from typed blocks, nested elements, and
composition objects and provides a dedicated Builder for previewing payloads.
See [Slack Block Kit](https://docs.slack.dev/reference/block-kit/).

**Pattern to borrow:** a bounded vocabulary becomes trustworthy only when
developers and designers can inspect every valid combination in a dedicated
fixture tool.

**Warning:** Slack's third-party platform optimizes for broadly composable
payloads. Life should have fewer, richer semantic regions and stronger native
editorial behavior.

### 2.7 React Native performance and transition primitives

Shopify's FlashList v2 supports heterogeneous item types, recycling, stable
key extraction, layout-state hooks, and variable-height/masonry layouts on
React Native's New Architecture. See [FlashList v2
usage](https://shopify.github.io/flash-list/docs/usage/).

React Native Reanimated supports list/layout transitions and reduced-motion
integration, but its shared-element transitions remain explicitly experimental
and not recommended for production. See [Reanimated shared-element
transitions](https://docs.swmansion.com/react-native-reanimated/docs/shared-element-transitions/overview/).

**Pattern to borrow:** virtualize the stable section stream, provide explicit
item types, keep keys stable, animate layout changes at section boundaries, and
respect Reduce Motion.

**Pattern to reject for now:** do not make experimental shared-element
transitions a dependency of Life's identity model. Semantic continuity must be
correct even with ordinary native navigation and no motion.

### 2.8 Native collection systems — section composition is the mature primitive

Apple's `UICollectionViewCompositionalLayout` builds a collection from items,
groups, and independently arranged sections, while diffable data sources apply
identifier-based snapshots. Android's Compose lazy layouts likewise preserve
item state with stable keys and improve heterogeneous reuse with explicit
`contentType`. See [Apple compositional
layout](https://developer.apple.com/documentation/uikit/uicollectionviewcompositionallayout?changes=_3_9),
[Apple diffable data
sources](https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa?changes=_1),
and [Compose lazy lists and
grids](https://developer.android.com/develop/ui/compose/lists).

These independent native systems converge on the same lesson:

- identity belongs to content, not position;
- a section is a first-class update and layout boundary;
- heterogeneous types should be declared, not guessed at runtime;
- state should travel with stable identity through reorder and insertion; and
- expensive data should be prefetched before its cell becomes visible.

**Life translation:** `semanticId`, `sectionKind`, and `treatmentFamily` are
architecture-bearing. Array index and `id:revision` are not safe list keys.
Media prefetch should follow likely visibility while policy and text skeletons
remain available immediately.

### 2.9 State production, local reads, and restoration

Android's current architecture guidance treats UI as the output of a state
production pipeline and recommends a local source of truth for offline-first
reads. UIKit state restoration similarly asks apps to restore a person's prior
configuration after process death. See [Android UI state
production](https://developer.android.com/topic/architecture/ui-layer/state-production),
[Android offline-first
architecture](https://developer.android.com/topic/architecture/data-layer/offline-first?hl=en),
and [UIKit state
restoration](https://developer.apple.com/documentation/uikit/preserving-your-app-s-ui-across-launches?changes=_6&language=objc).

**Pattern to borrow:** restore semantic context, not a screenshot of stale UI.
The durable restoration tuple for Life should be approximately:

```ts
interface LifeRestorationAnchor {
  route: "index" | "episode" | "search";
  semanticId?: string;
  lens: "periods" | "timeline" | "map" | "sources";
  scope: "combined" | "mine" | "together";
  relativeOffset?: number;
  viewerEpoch: string;
}
```

On restore, the client resolves the ID under current authority and then applies
the relative offset if the target still exists. Persisting only a raw pixel
offset would reopen the wrong content after insertions, corrections, or
revocation.

**Warning:** offline availability is not permission permanence. A locally
cached Together projection must still be bound to viewer and audience epoch
and must fail closed when current authority cannot be established.

### 2.10 Accessibility — semantic order must survive expressive layout

React Native exposes accessibility roles, state, actions, live regions, focus,
and motion preferences. W3C guidance requires focus order to preserve meaning
and asks dynamic status changes to be announced without unnecessarily taking
focus. See [React Native
accessibility](https://reactnative.dev/docs/accessibility.html), [W3C focus
order](https://www.w3.org/WAI/WCAG21/understanding/focus-order.html), and [W3C
status messages](https://www.w3.org/WAI/WCAG21/Understanding/status-messages).

**Pattern to borrow:** every specialized visual module needs a semantic linear
form. A map needs an ordered place/episode list; a graph needs a concise textual
reading; a comparison needs explicit sides; a timeline needs chronological
grouping that does not depend on x/y position.

Life should not announce background editorial refreshes as if the person
requested them. Announce direct-action results, loading/error status, and
material visible corrections. Preserve focus across ordinary insertion and
move it only when the current target is removed or the person enters a new
context.

### 2.11 Fixture systems and controlled release

React Native Storybook can reuse portable stories in Jest and device testing,
while Expo supports Maestro E2E flows and gradual update rollouts. Expo also
warns that rollback can be unsafe after a release mutates persistent client
state incompatibly. See [React Native Storybook
testing](https://storybookjs.github.io/react-native/docs/intro/testing/),
[Expo Maestro workflows](https://docs.expo.dev/eas/workflows/examples/e2e-tests/),
[Expo rollouts](https://docs.expo.dev/eas-update/rollouts/), and [Expo update
error recovery](https://docs.expo.dev/eas-update/error-recovery/).

**Pattern to borrow:** the semantic fixture matrix must be executable, and new
renderer/schema versions need staged exposure, a safe fallback, and rollback-
compatible persisted state.

**Repository-specific decision:** Travel App already has more than thirty
`app/dev` laboratories, screenshot mode, extensive Maestro flows, performance
measurement scripts, and golden-image infrastructure. Do not introduce
Storybook merely because it is a common pattern. Extend the existing native
lab first; reconsider Storybook only if portable component stories materially
reduce fixture duplication.

## 3. Synthesis: the recommended Vesper architecture

### 3.1 Choose the hybrid, not either extreme

| Architecture | Strength | Failure for Life | Verdict |
| --- | --- | --- | --- |
| **Fully client-driven** | Maximum native control | Duplicates truth, authority, eligibility, and ordering logic; hard to keep clients coherent | Reject |
| **Server-driven component tree** | Fast remote layout experimentation | Creates an untyped remote UI language, weak native behavior, compatibility burden, and policy leakage | Reject |
| **Semantic projection + native renderer registry** | Central truth and viewer compilation with native treatment, motion, fallback, and accessibility | Requires disciplined schemas and fixture coverage | Adopt |

The server/read layer owns:

- canonical ResourceRefs and revisions;
- viewer scope and audience epoch;
- entrance posture and eligibility explanation;
- truth, time roles, authorship, and provenance;
- section presence and semantic order;
- allowed actions and Continue authority;
- freshness, invalidation, and fallback-safe payloads; and
- one density or emphasis hint where meaningfully constrained.

The client owns:

- visual component and medium selection within the allowed treatment family;
- geometry, typography, imagery, spacing, and responsive reflow;
- interaction, gesture, focus, accessibility, and nonvisual alternatives;
- virtualization, memoization, local transient state, and media loading;
- navigation and index/detail continuity;
- layout, presence, and state-change motion;
- Reduce Motion, screenshot, offline, denied-location, and stale-state behavior;
- client-version fallback; and
- final root-native composition.

### 3.2 Use a semantic section document, not a block DSL

An illustrative, non-canonical projection boundary is:

```ts
type LifeSection =
  | PeriodSpineSection
  | InMotionSection
  | AcrossTimeSection
  | ReturnsSection
  | LensEntrySection;

type LifeEntry =
  | EpisodeDoor
  | PlaceRelationshipDoor
  | AddressedTogetherReturn
  | SavedCompositionReturn;

interface ProjectionIdentity {
  semanticId: string;
  revision: string;
  viewerEpoch: string;
  posture: "stable" | "nested" | "contextual" | "search_only" | "pinned";
}
```

The backend does not choose `SerifCard`, `MasonryTile`, `16px padding`, or
`swipeLeft`. The client does not infer that a ticket was used, that an audience
grant is valid, or that a composition may enter Returns.

### 3.3 Build anatomy slots, not object-type pages

Recommended common slots:

1. identity and truth;
2. episode skeleton;
3. occurred story spine;
4. Plans/changes/unresolved;
5. people and contributions;
6. Sources in place;
7. See anew; and
8. Continue and repair.

Each slot has a small set of native treatment families—evidence, sequence,
comparison, spatial, prose, and instrument—already defined by the expression
canon. Journey, Occasion, and Place relationship supply different native slot
implementations without bypassing common authority, accessibility, motion, and
analytics boundaries.

This is Spotify's layered-slot lesson applied to Vesper: shared shell,
configurable defaults, replaceable bounded slots, and composition only when the
default truly cannot express the job.

### 3.4 Name the kinds of complexity instead of calling Life one complex page

Life combines at least seven different complexity classes:

| Complexity | Example | Correct boundary | Wrong response |
| --- | --- | --- | --- |
| **Collection** | Hundreds of episodes and Sources | Virtualized section stream | One unbounded `ScrollView` |
| **Projection** | Periods, Timeline, Map, Sources | Stable ResourceRefs through multiple lenses | Duplicate lens-owned objects |
| **Expression** | Sequence, map, comparison, audio, article | Bounded native treatment module | Generic card for every medium |
| **Lifecycle** | Prospective, live, happened, historical | Same ID with posture/revision changes | New page/object per phase |
| **Authority** | Mine, Together, revocation, block | Viewer- and epoch-bound projection | Client-side hide after render |
| **Environment** | Offline, large text, Reduce Motion, narrow width | Client-native fallback and reflow | Server-authored coordinates |
| **Evolution** | New treatment on an older client | Versioned semantic section with safe fallback | Arbitrary remote UI payload |

This taxonomy matters because each class has a different owner. Virtualization
cannot solve authority. A content DSL cannot solve accessibility. A universal
card cannot express a map, and a custom map cannot own the episode's truth.

### 3.5 Use two cooperating renderers, not one Life renderer

The deeper research sharpens the architecture into two native composition
levels:

```text
Life index renderer
  stable, virtualized, retrieval-oriented
  period spine + earned relationships + bounded Returns + lens entries
                  |
                  | same semanticId / ResourceRefs / viewer epoch
                  v
Episode composition renderer
  finite, expressive, evidence-oriented
  identity + skeleton + story + plans + people + Sources + See anew + Continue
```

The **index renderer** optimizes scanning, orientation, re-finding, scroll
retention, and incremental updates. Its entries should be relatively light and
structurally predictable even when their editorial emphasis varies.

The **episode renderer** can use bounded specialized media because it has a
finite semantic anatomy and a clear subject. It may contain an evidence strip,
route, comparison, annotated image, short generated article, audio return, or
decision instrument without making those media root-level object types.

This is not master/detail in the database sense. Both levels are projections
over canonical domain truth. It is an attention contract: the index answers
"where can I return?"; the episode answers "what is here, and what can it still
open?"

### 3.6 Choose medium by information job

| Information job | Default treatment | Escalate when | Never rely on alone |
| --- | --- | --- | --- |
| Re-find one episode | Compact semantic door | Strong lead evidence improves recognition | AI title without time/place anchors |
| Understand what happened | Ordered event/evidence sequence | Spatial movement materially changes the story | Decorative collage |
| Understand where | Coordinated map + ordered list | Route or geographic comparison is substantive | Pins without textual alternative |
| Compare | Two-sided aligned comparison | More than two dimensions need a small table/plot | Vague prose saying two things are similar |
| See change across time | Trend/recurrence view | Evidence supports a longitudinal claim | Psychological trait inference |
| Inspect support | Source bundle with claim-local provenance | Conflicting evidence needs side-by-side inspection | Opaque confidence score |
| Continue | One bounded action/intent instrument | Real coordination requires a plan or Occasion | Open-ended reflection prompt |
| Receive a generated return | Short native article/audio/sequence | Substance and eligibility justify immersion | A flat summary or recap for its own sake |

The renderer resolves treatment only after the projection has named the job,
evidence, authority, and available alternatives. Medium selection is therefore
an editorial rendering decision, not ontology.

## 4. Transition model

Transitions must communicate semantic continuity, not decorate every update.

| Transition | Identity behavior | Recommended motion behavior |
| --- | --- | --- |
| **Upcoming → live → happened** | Same Occasion ID and episode door | Reflow emphasis within the same boundary; no remove-and-reinsert spectacle |
| **Plan gains Occurrence** | Plan remains; Occurrence is added with its own ID | Insert occurred state and settle Plan treatment; preserve scroll anchor |
| **Search-only → stable door** | Same underlying ResourceRefs; new projection posture | Quiet entrance into period spine with an inspectable reason |
| **Index → episode detail** | Same semantic door ID and viewer epoch | Native navigation; optional continuity treatment, never dependent on experimental shared-element APIs |
| **Combined ↔ Mine ↔ Together** | Same resources, new viewer projection | Granular diff/crossfade; preserve index position when safe |
| **Periods ↔ Timeline ↔ Map ↔ Sources** | Same target IDs through a different lens | Resolve target and surrounding context in the destination lens; do not preserve meaningless raw offset |
| **Correction** | Same object ID, new revision | Update only affected region; briefly reveal changed truth, not celebratory motion |
| **Revocation/block** | Invalid lane disappears under new audience/safety epoch | Immediate safe removal; do not let sensitive content linger in an exit animation |
| **Composition invalidates** | Composition ID may persist with degraded/closed revision | Replace with honest degraded state or remove; stable record does not move |
| **Text skeleton → rich media** | Same section and semantic ID | Preserve geometry/anchor; hydrate media inside its reserved treatment boundary |
| **Process death / relaunch** | Resolve saved semantic anchor under current epoch | Restore route, lens, scope, ID, and relative offset only after authority check |

The stable key should represent semantic identity; revision should decide
content refresh. Using `id:revision` as the list key would cause corrections to
look like object deletion and recreation, lose local state, and produce false
motion.

Cross-lens continuity should be target-based. If a person opens the Rome
episode in Timeline and switches to Map, the map should reveal Rome and its
ordered episode list; it should not try to transpose the Timeline's pixel
offset. If the target is unavailable under the new lens or scope, explain the
scope boundary and preserve a safe route back.

## 5. Rendering and performance posture for the current app

### Repository evidence

The mobile app currently uses:

- Expo `~55.0.30`;
- React Native `0.83.10` with Android New Architecture enabled;
- Reanimated `4.5.3`;
- Expo Router `~55.0.18`;
- Gesture Handler `~2.30.0`;
- `FlatList` and `SectionList` across major surfaces; and
- existing motion boundaries such as `AnimatedSectionBoundary`,
  `ExpandableRegion`, and `SurfaceStateSwap` with reduced-motion/screenshot
  behavior;
- TanStack Query 5 with structural sharing and targeted invalidation;
- a deliberately allow-listed persisted Home cache with a twelve-hour maximum
  age and an authenticated cache buster; and
- an established native dev-lab, screenshot-mode, Maestro, golden-image, and
  release-performance toolchain.

The current `canonical-artifact-life` lab is a `ScrollView` that changes the
density of repeated `CanonicalArtifactCard` instances. It proves projection
plumbing but not the new Life architecture. The adaptive-composition lab
already supplies a more relevant medium/role/density/environment vocabulary.

Three existing product surfaces offer useful internal precedent:

- Atlas Long View already switches one corpus between time and place modes,
  uses virtualized year/city/drill-down lists, paginates detail, and preserves
  already-loaded content when older pages fail;
- Trip Plan already bounds expensive day mounts with small render batches and
  uses viewability plus stable day identity for reading navigation; and
- Universal Search already groups typed results in a `SectionList`, although
  its small non-scrolling list is intentionally nested inside the overlay's
  outer `ScrollView` and should not be copied for an unbounded Life corpus.

These are implementation ingredients, not the Life information architecture.
Atlas is still media/archive-shaped; Plan is one object family; search is a
temporary task surface. Life needs their proven mechanics behind its own
semantic contract.

### Recommended frontend posture

1. Start with one virtualized vertical section stream, not nested vertical
   scroll views.
2. Keep each semantic section independently memoizable and independently
   loadable.
3. Give heterogeneous rows explicit item types and stable semantic keys.
4. Keep transient expansion/playback state in a keyed local state store, not in
   canonical projections.
5. Precompute authority, ordering, and expensive relational composition in the
   read layer; do not recompute the life graph during `renderItem`.
6. Load text/truth skeleton first; progressively hydrate media, Map, and rich
   composition.
7. Preserve scroll position across scope, revision, and incremental hydration.
8. Use current Reanimated section/layout primitives for bounded transitions and
   disable unsafe exit motion on revocation.
9. Evaluate FlashList v2 only after deterministic SectionList fixtures reveal a
   real performance need; New Architecture is compatible, but a new list engine
   should not precede the semantic section contract.
10. Profile release builds with L01 rich evidence and L02/L05 social mutations;
    dev-mode intuition is insufficient.
11. Restore by semantic anchor and relative offset, not pixel offset alone.
12. Give every specialized visual module a compact, ordered, nonvisual reading.
13. Deep-link to canonical episode identity plus requested lens/scope; re-resolve
    authority on entry rather than trusting route parameters.
14. Use TanStack Query selectors or narrowly keyed section queries so an update
    to one lane does not subscribe and rerender the whole Life projection.

### Cache and authority posture

TanStack Query's structural sharing can preserve unchanged subtree references,
and its `select` option can narrow component subscriptions. That is useful for
the section-granular renderer, but it is not normalization and does not enforce
authority. See [TanStack Query render
optimizations](https://tanstack.com/query/latest/docs/framework/react/guides/render-optimizations)
and [query removal](https://tanstack.com/query/latest/docs/reference/QueryClient?from=reactQueryV3).

The current codebase already has the right seed pattern in
`profileProjectionIdentity.ts`: Together cache identity includes viewer,
circle, and circle revision, and authority loss synchronously removes every
matching revision. Life should generalize that policy:

```text
life query identity = viewer + scope + audience epoch + semantic target/lens
```

Recommended persistence policy:

- private stable episode skeletons may be eligible for a bounded encrypted or
  platform-protected local read cache;
- public/source metadata may persist under ordinary freshness rules;
- Together projections and generated social returns should not enter the
  existing broad Home persistence allow-list by default;
- if Together offline reads are later required, persist them in a separately
  erasable, viewer/epoch-bound store with an explicit offline-authority policy;
- revocation, leaving, blocking, depicted-person removal, logout, and account
  switching perform synchronous in-memory removal and persisted-store purge;
  and
- refetch/invalidation is insufficient for authority loss because stale content
  may remain visible while the network is unavailable.

This is stricter than ordinary stale-data handling because a stale restaurant
name is a quality problem; a stale audience grant is a privacy failure.

### Restoration and deep-link posture

Expo Router makes every screen addressable, which is valuable for Home returns,
notifications, social handoffs, and test fixtures. See [Expo Router's
deep-linking model](https://docs.expo.dev/router/introduction/).

Use canonical routes such as an episode ID, not the index position or rendered
section path. A deep link may request a lens and scope, but the client/read layer
must downgrade safely if the requested scope is no longer authorized. The Life
index should retain a per-lens semantic anchor in local UI state so returning
from detail feels continuous without treating old projection content as truth.

### Accessibility posture

The semantic section tree doubles as the default reading tree. Specialized
treatments must declare:

- accessible label and concise summary;
- ordered children or a textual alternative;
- explicit actions and expanded/selected/busy state;
- focus behavior for insert, correction, removal, and scope change;
- whether a direct-action result warrants a polite announcement; and
- motion-free behavior that preserves the same semantic transition.

Do not make every card and all of its descendants independently focusable.
Group static evidence, expose only meaningful actions, and let detail provide
the longer reading. This keeps an expressive episode from becoming screen-
reader homework.

## 6. Compatibility and failure behavior

Every semantic section and treatment family needs:

- schema version and minimum client capability;
- native default renderer;
- safe compact fallback;
- no-op/silence behavior;
- error and stale treatment;
- unsupported-action removal;
- offline and denied-location alternative;
- nonvisual reading order; and
- a kill switch at section/treatment level.

Unknown treatment variants fall back within the same semantic section. Unknown
semantic sections do not render generic JSON or arbitrary cards; they omit
safely and emit diagnostics. A stable Life door must not disappear merely
because one optional See-anew treatment is unsupported.

Compatibility operates on two axes:

1. **Semantic compatibility:** can this client understand the section's job,
   identity, authority, and allowed actions? If not, omit safely.
2. **Treatment compatibility:** can this client render the preferred expression?
   If not, fall back to another treatment for the same semantic section.

A client must never fall back from a viewer-scoped section to a less-scoped
payload. Fallback may reduce richness, never authority.

Persisted projection migrations also require explicit compatibility tests. Expo
notes that over-the-air rollback may be unsafe after incompatible persistent-
state mutation. Therefore every Life schema change must either be backward-
readable, use a new versioned storage key, or delete its old cache before the
new renderer can commit state.

## 7. Fixture and evaluation architecture

Create a dedicated Life composition lab modeled on the discipline of Slack's
Block Kit Builder, but using Vesper's governed fixtures rather than free-form
blocks.

The lab must switch:

- L01–L06 evidence world;
- stable, nested, contextual, search-only, and pinned posture;
- Combined, Mine, and Together;
- prospective, live, happened, historical, and dormant lifecycle;
- sparse and rich evidence;
- correction, revocation, block, and reconciliation transitions;
- 320-point width and 150% text;
- Reduce Motion and screenshot mode;
- screen-reader transcript;
- offline/stale and denied location;
- unknown section/treatment version; and
- loading, partial, degraded, and error states.

It must also let a reviewer change one axis without resetting all others. The
point is not a screenshot gallery; it is controlled comparison. A reviewer
should be able to hold L02 + Together + happened constant, then toggle only
block, leave, reconcile, large text, or offline state and inspect the semantic
diff.

Automated gates should include:

- projection-schema decoding and fallback;
- stable-key uniqueness;
- no duplicate ResourceRef ownership;
- no whole-list remount for a leaf revision;
- scroll-position retention;
- item-render and frame-time instrumentation;
- accessibility order and action labels;
- screenshot snapshots for semantic states, not every data permutation;
- hard privacy assertion before and after animated frames; and
- all fifty re-finding plus fourteen social-lifecycle oracles.

### Evaluation lanes

| Lane | Tooling posture | What it proves |
| --- | --- | --- |
| Projection contract | Pure TypeScript fixtures/tests | Schema decode, authority, ordering, stable identity, fallback |
| Native composition lab | Existing `app/dev` infrastructure | Full valid state space on a real renderer |
| Component behavior | Jest + React Native Testing Library | Actions, focus/state labels, targeted rerender behavior |
| Cross-screen journeys | Existing Maestro infrastructure | Deep links, lens/detail return, relaunch, screenshots |
| Mutation/privacy | Deterministic L02/L05/S01–S14 transitions | No unauthorized frame, cache purge, focus recovery |
| Release performance | Existing release profiling scripts + device traces | Mount, scroll, hydration, media, mutation under realistic load |
| Deployment compatibility | Version/fallback/rollback fixtures | Older client, newer treatment, persisted-state migration, kill switch |

Do not snapshot every data permutation. Snapshot treatment families and
high-risk semantic transitions; assert the larger matrix structurally. Visual
goldens cannot prove an audience epoch or a stable key, while structural tests
cannot prove text clipping, reading order, or jank.

### Performance questions, not premature thresholds

Profile these founder-visible journeys in a release build before choosing a new
list engine or adding renderer abstractions:

1. Cold-open Life with locally available stable skeletons.
2. Scroll L01 through mixed media without blank regions or blocked taps.
3. Open an episode, hydrate its richest eligible medium, and return to the same
   semantic anchor.
4. Switch Periods to Map and back while preserving the target.
5. Apply an L02 contribution/correction without whole-index remount.
6. Revoke or block L05 content with zero unauthorized visible frames.
7. Relaunch offline into an authorized private episode and an unauthorized
   Together target.

Measure time-to-useful-content, dropped frames, JS and UI thread stalls, memory,
network/media overfetch, rerender counts, and scroll-anchor error. React Native
itself recommends release-mode profiling with platform tools; see [React Native
profiling](https://reactnative.dev/docs/profiling).

## 8. Ranked patterns for Life

| Rank | Pattern | Value | Complexity | Adopt when |
| ---: | --- | --- | --- | --- |
| **1** | Semantic projection + native renderer registry | Very high | Medium | Now |
| **2** | Separate index and episode composition renderers | Very high | Medium | Now |
| **3** | Stable IDs separate from revision and viewer epoch | Very high | Low | Now |
| **4** | One section tree over several owners | Very high | Medium | Now |
| **5** | Common anatomy with bounded slots | Very high | Medium | Now |
| **6** | Authority-bound cache identity and synchronous purge | Very high | Medium | Before Together production |
| **7** | Targeted granular diffing and subscriptions | High | Medium | Now |
| **8** | Safe client-version fallback | High | Low | Now |
| **9** | Semantic-anchor restoration and deep links | High | Low–medium | Now |
| **10** | One corpus, multiple contextual lenses | High | Medium | Canon already adopted |
| **11** | Linear accessibility alternative for every rich module | High | Medium | With each treatment |
| **12** | Eligibility-gated immersive Returns | High | Medium–high | After stable index/detail |
| **13** | Virtualized heterogeneous item types | High at rich scale | Medium | During prototype profiling |
| **14** | Identity-preserving layout motion | Medium–high | Medium | After semantic transitions work without motion |
| **15** | Managed slot-level customization | Medium | Medium | When Journey/Occasion/Place diverge legitimately |
| **16** | Shared-element navigation transitions | Cosmetic/continuity value | High/risky | Defer while RN support is experimental |

## 9. Anti-patterns to reject

- one `LifeCard` with a growing matrix of props;
- one page component branching on every object, mode, lifecycle, and audience;
- backend-authored React Native component trees;
- domain-table payloads bound directly to visual components;
- arbitrary untyped `custom` rendering blobs;
- `id:revision` list keys that turn correction into object replacement;
- one mixed feed of stable episodes and volatile generated compositions;
- nested vertical virtualized lists for every section;
- restoring a raw scroll offset after the underlying projection changed;
- using Map, graph, collage, or audio without an ordered accessible alternative;
- persisting Together projections in a broad cache without viewer/epoch identity;
- treating invalidation/refetch as sufficient for revocation;
- animating every server update;
- exit animations that leave revoked content visible;
- using engagement to choose ontology or authority;
- introducing a new renderer/list framework before fixture-based profiling; and
- treating a successful lab screenshot as evidence that correction, scope, and
  long-scroll behavior work.

## 10. Recommendation

Life should adopt a **two-level semantic section architecture** built over the
existing expression dimensions and current React Native stack:

```text
Life projection compiler
  -> index projection: typed lightweight doors with stable identity
  -> virtualized Life index renderer
  -> canonical semantic route
  -> episode projection: common anatomy + bounded expressive slots
  -> native episode composition renderer
  -> section-level motion, accessibility, cache policy, and fallback
```

Do not start by building every episode type. First build the fixture lab and
the projection/renderer boundary across L01–L06. That is not a narrow behavior
proof; it is the systematic environment in which the complete Life grammar can
be rendered, mutated, profiled, and compared without committing production
navigation or visual composition prematurely.

The lab should extend the app's existing dev-route and Maestro system rather
than introduce a parallel component-workbench stack now. Its first architecture
deliverable is not a polished screen. It is a typed projection document, a
stable key/anchor contract, index and episode renderer boundaries, and the six
worlds running through scope, lifecycle, failure, accessibility, and mutation
states.

The strongest new conclusion from the second research pass is:

> Richness belongs inside stable retrieval structure. Life can support many
> media and modes without feeling like many products only if every expression
> returns to the same governed person-place-time-people identity.

The compact standard is:

> The backend should understand the life. The client should understand the
> screen. Stable identity should let both change without making the person's
> world feel replaced.
