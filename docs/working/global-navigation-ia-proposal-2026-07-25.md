---
doc_type: working
status: active
owner: founder / product / frontend
created: 2026-07-25
last_verified: 2026-07-27
expires: 2026-08-24
why_new: No existing document owns the cross-surface migration from four peer tabs to Trips, Vesper, and Places plus an avatar-opened You hub, including compatibility and retirement plans for Discover and Atlas.
promotes_to: Travel App/docs/Navigation Contract.md plus affected surface contracts and a navigation decision record
supersedes: []
source_of_truth_for:
  - proposed-global-navigation-ia-migration
  - proposed-discover-retirement
  - proposed-atlas-tab-retirement
---

# Global Navigation IA Migration Plan — Trips, Vesper, Places, and You

> **Working migration plan, not product canon.** This plan records the current
> proposed direction, implementation blast radius, compatibility obligations,
> staged retirement criteria, and evidence required before changing the
> canonical navigation contracts.

## Decision summary

The proposed global information architecture is:

- Three bottom destinations: **Trips**, **Vesper**, and **Places**
- A persistent avatar on root surfaces that opens a full-screen **You** hub
- **Discover** retired as a product destination; its useful capabilities are
  recomposed inside Places
- **Atlas** retired as a bottom tab; Atlas survives as the private memory,
  interpretation, and authored-record area inside You

The ownership rule is:

> **Trips owns travel over time. Vesper owns assistance and action. Places owns
> practical place activity. You owns the person. Atlas owns the person's
> private travel memory.**

This is not a plan to delete Discover and Atlas capabilities. It is a plan to
retire two ambiguous top-level containers, assign each surviving capability one
canonical owner, and preserve old links while clients and documentation migrate.

## Why the current model needs to change

The current bottom navigation presents four peer concepts that are not actually
peers:

| Current destination | Actual kind of concept | Current ambiguity |
|---|---|---|
| Trips | Durable object portfolio and time-based workspace | Strong, legible owner |
| Vesper | Relationship, agent, and action surface | Strong, legible owner |
| Discover | A browsing mode created partly to give search a useful default | Risks becoming an undifferentiated feed |
| Atlas | A metaphor spanning archives, place utilities, identity, trust, and settings | No single dominant intent |

The implementation reflects this ambiguity. The Atlas route family currently
contains account identity, privacy, notifications, companions, Vesper
preferences, personal memory, saved places, visited places, readings, artifacts,
recaps, data receipts, and feedback. `/atlas/profile` is titled `Settings` and is
the private trust-and-controls hub, while `/profile/[userId]` is the actual
public/social profile.

The goal is therefore not a label swap. It is an ownership migration.

## Scope

This plan covers:

- Global navigation shell and root headers
- The new You hub and its child routes
- Discover-to-Places capability migration
- Atlas-tab-to-You/Atlas capability migration
- Saved and visited-place ownership
- Public versus private profile boundaries
- Route aliases, notification destinations, cold links, and back behavior
- Tests, visual QA, analytics, documentation, and staged retirement
- Rollback boundaries and retirement gates

## Non-goals

This plan does not:

- Redesign the detailed composition of the Places zero-query page
- Redesign every Atlas memory, reading, or artifact screen
- Move trip-specific settings out of Trips
- Rename backend `/api/me/*` or `/api/atlas/*` endpoints
- Change privacy, booking, proposal, itinerary, expense, or group-message rules
- Treat a successful route refactor as journey or device certification
- Require deletion of inexpensive legacy redirects

## Current implementation baseline

### Global shell

The implemented tab order is:

```text
Trips · Vesper · Discover · Atlas
```

The tab shell lives in:

- `Travel App/app/(tabs)/_layout.tsx`
- `Travel App/components/navigation/FloatingTabBar.tsx`
- `Travel App/app/_layout.tsx`

Discover currently has:

```text
app/(tabs)/discover/_layout.tsx
app/(tabs)/discover/index.tsx
app/(tabs)/discover/map.tsx
```

Atlas currently has a tab root:

```text
app/(tabs)/atlas/_layout.tsx
app/(tabs)/atlas/index.tsx
```

and a large root-stack route family:

```text
app/atlas/account.tsx
app/atlas/artifact/[id].tsx
app/atlas/candidate/[id].tsx
app/atlas/companions.tsx
app/atlas/compose.tsx
app/atlas/constraints.tsx
app/atlas/data-receipt.tsx
app/atlas/delegation.tsx
app/atlas/feedback.tsx
app/atlas/inbox.tsx
app/atlas/long-view.tsx
app/atlas/memory.tsx
app/atlas/narration-history.tsx
app/atlas/notifications.tsx
app/atlas/phone.tsx
app/atlas/privacy.tsx
app/atlas/profile.tsx
app/atlas/readings/[id].tsx
app/atlas/readings/index.tsx
app/atlas/removed.tsx
app/atlas/saved-places.tsx
app/atlas/scan.tsx
app/atlas/shared-links.tsx
app/atlas/unpacked-card.tsx
app/atlas/unpacked.tsx
app/atlas/voice-logs.tsx
app/atlas/whole.tsx
```

### Existing ownership boundaries worth preserving

- `/profile/[userId]` is the public/social projection and is used from social,
  search, map, and companion surfaces.
- `/trip-settings/*` owns trip-specific identity, people, privacy,
  notifications, and permissions.
- Conversation history belongs to Vesper even though a legacy
  `/atlas/voice-logs` redirect exists.
- The Saved & Collections contract already states that Atlas does not own
  practical saved-place management.
- Existing `/api/me/*`, social-profile, delegation, notification, memory, and
  Atlas APIs can support the route migration without a backend endpoint rename.

## Target ownership model

### Trips

Trips owns:

- Current, upcoming, draft, past, and archived trips
- Living itineraries and trip-level decisions
- Trip-specific collaboration and membership
- Trip-specific privacy, notifications, and permissions
- Trip stories and memories whose primary meaning is the trip

Completed trips stay recognizable as trips. Place-level and personal-memory
views may cross-link into Places or Atlas without moving the trip itself.

### Vesper

Vesper owns:

- Conversation with the agent
- Advice, synthesis, proposals, and next actions
- Cross-domain assistance before an intent has a durable owner
- Conversation history
- Contextual explanations that may deep-link to You, Trips, or Places

### Places

Places owns:

- Place search
- A useful zero-query starting state
- Nearby and context-aware recommendations
- Recent searches and recently viewed places
- Place, venue, experience, stay, guide, and dossier entrances
- Practical saved-place management
- Visited/Been place history
- Place-centered collections and maps

Discover is dissolved into Places rather than simply renamed. Strong search,
context, map, editorial, social, and recommendation components may survive.
Weak feed mechanics do not inherit permanent ownership merely because they
exist today.

#### Places composition contract — proposed for the first real implementation

Places should be a **contextual place workspace**, not a renamed editorial
feed. The persistent shell has four quiet elements: identity/avatar, one
explicit place-or-trip scope, search, and a contextual utility row (Map, Saved,
Been only when they have useful content). Geography is declared once in the
scope; search should not repeat it.

The zero-query body changes by the strongest honest context, rather than by a
fixed set of feed sections:

| Context | First viewport | Subsequent useful modules | Must not imply |
|---|---|---|---|
| No selected place or trip | Dominant search; Choose a city / Near me entrances | One optional editorial read; recently viewed when real | A generic personalized feed or fabricated nearby data |
| Home / global personal context | Personal city return or practical nearby cue when evidence exists | Your Places summary; saved/been entries; recent cities | That home is an active trip |
| Future trip | Trip scope and saved-but-not-planned decision | One trip-relevant recommendation; places that could be used in the trip | That saving a place added it to a dated plan |
| Live trip | Trip scope, map/proximity, and one time-sensitive recommendation | Alternatives and saved nearby | Live hours, waits, or location precision without evidence |
| Returned trip | Place scope plus a quiet retrospective cue | Been/history and durable saves | That the trip is still active |
| Explicit search | Search results with location declared once; List / Map switch | Honest no-result recovery and a Vesper handoff | The old editorial zero-query composition |
| Chosen place unrelated to active trip | Chosen place as primary scope, with a clear "not your active trip" relationship | Search, saved/been facts, editorial/place detail entrances | Silent rebinding of actions to the active trip |

There can be several selectable scopes (current trip, an upcoming trip, home,
or a globally chosen city), but only one primary scope at a time. A global
search always remains available. Selecting a different city must not mutate the
active trip. The chosen scope and every Vesper/trip handoff carry their context
explicitly.

Places may propose a trip action, but Trips remains the sole owner of a dated
itinerary write. "Use in trip" therefore opens a confirmation naming the trip
and deliberately asks for a day or next Trips step; it must never infer a day
or create a parallel Places itinerary writer.

### You

You owns the private relationship between a person, their account, and Vesper:

- Identity and account access
- Public-profile preview and editing entrance
- Companions
- Global privacy and sharing
- Global notification preferences
- Durable preferences and constraints
- Vesper autonomy
- Data records and receipts
- Feedback and support
- Entry to the private Atlas

You is a concise hub, not a monolithic settings form and not a second feature
catalogue.

### Atlas inside You

Atlas survives with a narrower promise:

> **Atlas is the private memory, interpretation, and authored record of a
> person's travel life.**

Atlas owns:

- What Vesper knows and why
- Memory evidence, correction, and removal
- Personal time-based travel history
- Memory inbox and candidate review
- Personal Readings and artifacts
- Retrospective recaps and durable share records

Atlas does not own:

- Practical saved-place management
- The primary visited-place browser
- Account identity
- Global privacy or notifications
- Companions
- Generic feedback
- Conversation history

## Proposed You composition

Opening the avatar presents:

```text
You

[Identity header]
Name
View public profile →

YOUR ATLAS
  Your Atlas
  What Vesper knows

PERSONALIZATION
  Preferences & constraints
  Vesper autonomy

PEOPLE
  Companions

SETTINGS
  Privacy & sharing
  Notifications
  Account

SUPPORT
  Send feedback
```

Composition rules:

- `View public profile` is an identity-header action, not another settings row.
- Atlas sub-objects such as Readings, Inbox, Timeline, and Recaps stay one level
  deeper inside Your Atlas.
- Saved and Been do not appear as You-owned settings. Contextual links may
  still open their Places destinations.
- Conversations remain reachable through Vesper.
- Account contains credentials, phone, sign-in providers, data download,
  sign-out, and deletion.
- Privacy owns visibility, sharing, public-profile controls, and data-use
  controls.
- “What Vesper knows” is promoted because personalization must be legible and
  correctable, not because it is a separate domain owner.

## Target route hierarchy

Expo route groups are shown where relevant. Public-facing paths omit route
group names.

```text
app/
  (tabs)/
    trips/
    concierge/
    places/
      _layout.tsx
      index.tsx
      map.tsx
      saved.tsx
      been.tsx

  you/
    index.tsx
    account.tsx
    account/
      phone.tsx
    people.tsx
    privacy.tsx
    notifications.tsx
    preferences/
      constraints.tsx
      autonomy.tsx
    data/
      receipt.tsx
    feedback.tsx
    atlas/
      index.tsx
      memory.tsx
      timeline.tsx
      inbox.tsx
      compose.tsx
      scan.tsx
      removed.tsx
      readings/
        index.tsx
        [id].tsx
      artifact/
        [id].tsx
      candidate/
        [id].tsx
      unpacked.tsx
      unpacked-card.tsx
      shared-links.tsx

  profile/
    [userId].tsx

  place/
    [placeSlug].tsx
  venue/
    [venueId]/
      index.tsx
  experience/
    [experienceId].tsx
```

Not every namespace requires an index screen in the first release.
`preferences/` and `data/` may be organizational namespaces until their content
justifies a landing page.

Existing public object URLs such as `/profile/[userId]`, `/place/[placeSlug]`,
`/venue/[venueId]`, and `/experience/[experienceId]` remain stable. Places
becomes their navigation owner without forcing an external URL migration.

## Canonical route helper proposal

Add canonical helpers before changing callers:

```text
routes.you()
routes.youAccount()
routes.youPhone()
routes.youPeople()
routes.youPrivacy()
routes.youNotifications()
routes.youConstraints()
routes.youAutonomy()
routes.youDataReceipt()
routes.youFeedback()

routes.yourAtlas()
routes.yourAtlasMemory()
routes.yourAtlasReceipt(...)
routes.yourAtlasTimeline(...)
routes.yourAtlasInbox()
routes.yourAtlasReadings()
routes.yourAtlasReading(...)
routes.yourAtlasArtifact(...)
routes.yourAtlasCandidate(...)
routes.yourAtlasCompose()
routes.yourAtlasScan(...)
routes.yourAtlasRemoved()
routes.yourAtlasUnpacked(...)

routes.places()
routes.placesMap(...)
routes.placesSaved(...)
routes.placesBeen(...)
```

During migration, old `atlas*` and `discover*` helpers remain compatibility
helpers or deprecated wrappers. New product code must call the canonical helper
for the new owner.

## Route compatibility and redirect ledger

### Atlas routes

| Existing route | New canonical destination | Parameter obligation | Retirement posture |
|---|---|---|---|
| `/(tabs)/atlas` | `/you/atlas` | Preserve entry attribution | Keep redirect long-term |
| `/atlas/profile` | `/you` | None | Keep redirect long-term |
| `/atlas/account` | `/you/account` | None | Keep redirect |
| `/atlas/phone` | `/you/account/phone` | Preserve return intent if present | Keep redirect |
| `/atlas/privacy` | `/you/privacy` | Preserve contextual source if present | Keep redirect |
| `/atlas/notifications` | `/you/notifications` | None | Keep redirect |
| `/atlas/companions` | `/you/people` | Preserve selected person if added later | Keep redirect |
| `/atlas/constraints` | `/you/preferences/constraints` | None | Keep redirect |
| `/atlas/delegation` | `/you/preferences/autonomy` | None | Keep redirect |
| `/atlas/data-receipt` | `/you/data/receipt` | Preserve selected receipt/filter | Keep redirect |
| `/atlas/feedback` | `/you/feedback` | Preserve origin | Keep redirect |
| `/atlas/memory` | `/you/atlas/memory` | Preserve `view`, `phrase`, and `factId` | Keep redirect long-term |
| `/atlas/inbox` | `/you/atlas/inbox` | Preserve filters if present | Keep redirect |
| `/atlas/readings` | `/you/atlas/readings` | Preserve filters | Keep redirect |
| `/atlas/readings/[id]` | `/you/atlas/readings/[id]` | Preserve reading steer and saved action params | Keep redirect long-term |
| `/atlas/artifact/[id]` | `/you/atlas/artifact/[id]` | Preserve artifact id | Keep redirect long-term |
| `/atlas/candidate/[id]` | `/you/atlas/candidate/[id]` | Preserve candidate id | Keep redirect |
| `/atlas/compose` | `/you/atlas/compose` | Preserve source/steer | Keep redirect |
| `/atlas/scan` | `/you/atlas/scan` | Preserve `from` and `session` | Keep redirect |
| `/atlas/removed` | `/you/atlas/removed` | None | Keep redirect |
| `/atlas/unpacked` | `/you/atlas/unpacked` | Preserve `year` | Keep redirect long-term |
| `/atlas/unpacked-card` | `/you/atlas/unpacked-card` | Preserve `year` | Keep redirect |
| `/atlas/shared-links` | `/you/atlas/shared-links` | None | Keep redirect |
| `/atlas/saved-places` | `/(tabs)/places/saved` | Preserve `city` | Keep redirect long-term |
| `/atlas/long-view?mode=places` | `/(tabs)/places/been` | Preserve `city` and `accepted` | Conditional redirect |
| `/atlas/long-view?mode=time` | `/you/atlas/timeline` | Preserve `year`, `undated`, and `accepted` | Conditional redirect |
| `/atlas/long-view` | `/you/atlas/timeline` | Default to time history | Conditional redirect |
| `/atlas/whole` | `/you/atlas` | None | Keep redirect until callers are gone |
| `/atlas/narration-history` | Vesper-owned narration history | Preserve item/deep-link state | Move owner, keep redirect |
| `/atlas/voice-logs` | Existing Vesper conversation history | Existing redirect behavior | Keep compatibility redirect |
| `/your-map` | `/(tabs)/places/been` map state | Preserve city/filter | Keep redirect long-term |

Redirect screens should use replacement semantics so obsolete routes do not
remain as phantom screens in the back stack.

### Discover routes

| Existing route or entry | New canonical destination | Obligation | Retirement posture |
|---|---|---|---|
| `/(tabs)/discover` | `/(tabs)/places` | Preserve query, trip context, and entry attribution | Keep redirect for persisted links |
| `/(tabs)/discover/map` | `/(tabs)/places/map` | Preserve camera, filters, search, and selected item | Keep redirect |
| Discover search entry | Places search | Preserve zero-query and typed-query behavior | Migrate callers |
| Discover saved entry | Places Saved | Preserve save state and city | Migrate callers |
| Discover people/profile entry | `/profile/[userId]` or `/you/people` | Preserve public/private distinction | Migrate callers |
| Discover-to-Vesper handoff | Vesper with Places provenance | Preserve prompt, place context, and trip context | Migrate callers |
| Discover-to-trip handoff | Existing trip creation or trip destination | Preserve candidate objects and origin | Migrate callers |

The capability migration must be explicit. A tab rename that leaves component,
analytics, route, and ownership vocabulary as `Discover` is an incomplete
retirement.

## Navigation and back-stack contract

### Avatar and You

- Show the same identity/avatar control on the root of Trips, Vesper, and
  Places.
- The avatar pushes `/you` as a normal full-screen route.
- Back from `/you` returns to the surface that opened it.
- A cold deep link to `/you` falls back to Trips when there is no history.
- A cold deep link to `/you/*` falls back to `/you`.
- A cold deep link to `/you/atlas/*` falls back to `/you/atlas`.
- Contextual entrances may deep-link directly to the relevant child route; they
  do not need to pass through the You index.

### Places

- Places child screens use Places as their semantic owner.
- A cold deep link to Places Saved, Been, or Map falls back to Places.
- Existing object detail screens remain history details: ordinary entry returns
  to the originating surface; cold-link fallbacks use the most truthful stable
  owner.

### Public profile

- `/profile/[userId]` remains a history detail and public projection.
- Viewing oneself shows a private editing/control entrance into You.
- Public-profile visibility never implies access to private You or Atlas data.

### Legacy redirects

- Redirects replace rather than push.
- Redirects preserve all recognized parameters.
- Unknown safe parameters may be forwarded during the compatibility window.
- Redirects record alias usage when analytics support exists.
- A legacy route is not deleted merely because internal callers have reached
  zero; persisted notifications and external links may outlive code callers.

## Blast radius

### 1. Global shell and header chrome

Primary surfaces:

- `Travel App/app/(tabs)/_layout.tsx`
- `Travel App/components/navigation/FloatingTabBar.tsx`
- `Travel App/app/_layout.tsx`
- `Travel App/app/(tabs)/trips/index.tsx`
- `Travel App/app/(tabs)/concierge/*`
- `Travel App/app/(tabs)/discover/*`
- `Travel App/app/(tabs)/atlas/*`
- Root-header and identity-control components, including the Atlas-specific
  identity control

Required work:

- Register Places and You routes
- Introduce a shared root-avatar contract
- Remove Atlas-specific ownership from the identity control
- Preserve center-slot Vesper behavior and floating-tab ergonomics
- Verify three-tab widths, labels, safe areas, collapse behavior, accessibility,
  keyboard behavior, and tablet layouts
- Ensure avatar availability does not collide with back, search, compose, or
  trip controls

### 2. Route helpers and navigation semantics

Primary surfaces:

- `Travel App/utils/routes.ts`
- `Travel App/utils/navigation.ts`
- `Travel App/utils/notificationDestination.ts`
- `Travel App/utils/universalSearchRouting.ts`
- `Travel App/utils/nearYouRoutes.ts`
- Any raw `/atlas`, `/discover`, or `/(tabs)/atlas` strings

Known semantic changes:

- `exitAtlas()` becomes an exit to `/you/atlas`
- `notificationFallback({mode: 'personal'})` moves from `/atlas/profile` to
  `/you`
- Social notifications continue to public profiles or `/you/people`
- Memory/timeline notifications move to `/you/atlas/*`
- Saved/visited notifications move to Places
- Universal Search must distinguish public people, practical places, trips,
  Vesper conversations, and private Atlas objects

### 3. You and trust-control surfaces

Current implementations to rehome:

- `app/atlas/profile.tsx`
- `app/atlas/account.tsx`
- `app/atlas/phone.tsx`
- `app/atlas/privacy.tsx`
- `app/atlas/notifications.tsx`
- `app/atlas/companions.tsx`
- `app/atlas/constraints.tsx`
- `app/atlas/delegation.tsx`
- `app/atlas/data-receipt.tsx`
- `app/atlas/feedback.tsx`

Required work:

- Extract route-independent screen bodies before adding aliases
- Compose the smaller You index rather than copying the existing Settings page
- Remove duplicate privacy and record entrances
- Keep account actions and destructive controls in Account
- Preserve existing UserContext, notification, social, delegation, memory, and
  auth hooks
- Keep trip-specific settings separate

### 4. Atlas memory and archive surfaces

Current implementations to retain and rehome:

- Atlas tab home
- Memory and receipt view
- Inbox and candidate review
- Readings and reading detail
- Artifact detail
- Compose and scan
- Removed-memory review
- Time-oriented Long View
- Unpacked, share card, and shared links

Required work:

- Recompose Atlas Home for its narrower private-memory role
- Remove primary Saved and Been ownership from Atlas Home
- Replace the current four-way Whole Atlas directory with a memory-oriented
  index or retire it
- Split `long-view` by ownership rather than carrying a permanent `mode`
  switch across domains
- Preserve current hooks, caches, API shapes, and receipt correction behavior
- Update all Atlas component call sites that open Saved or place-mode Long View

### 5. Discover and Places surfaces

Primary surfaces:

- `app/(tabs)/discover/index.tsx`
- `app/(tabs)/discover/map.tsx`
- `components/discover/*`
- Discover feed, search, map, social, guide, save, and Vesper-handoff components
- Place, venue, experience, accommodation, dossier, and guide details
- Universal Search and search-routing utilities

Required work:

- Create Places route ownership before renaming internal components
- Classify every Discover module as keep, recompose, move, or delete
- Preserve typed search, zero-query value, map state, saves, detail entry,
  Vesper handoff, and trip handoff
- Move practical saved management and Been into Places
- Prevent Places from becoming an endless generic feed
- Remove Discover-only copy, icons, accessibility labels, test IDs, analytics
  names, and internal type names after cutover

Module-classification questions:

| Capability | Presumptive disposition |
|---|---|
| Search and search suggestions | Keep; make primary in Places |
| Contextual/nearby recommendations | Keep; constrain to useful modules |
| Recent searches and recently viewed | Keep or add |
| Saved-place entrance | Keep; canonical Places child |
| Map/spatial browse | Keep; canonical Places child |
| Place details and readers | Keep; stable external routes |
| Editorial guides/dossiers | Keep selectively as place understanding |
| Social profiles and friend activity | Keep only where it improves place decisions |
| Generic engagement feed mechanics | Re-evaluate; no automatic migration |
| Discover-specific composition vocabulary | Retire after parity |

### 6. Saved, Been, and map ownership

Primary surfaces:

- `app/atlas/saved-places.tsx`
- `app/atlas/long-view.tsx`
- `app/your-map.tsx`
- Saved controls in Discover, Atlas, Trips, details, guides, and trip creation
- Atlas shelves and readings that deep-link into saved or place history

Required work:

- Reuse existing components and data hooks; do not fork saved state
- Preserve city filters and accepted-history semantics
- Keep “save” distinct from like/favorite
- Define whether Places Been defaults to list, map, or remembered last mode
- Define whether time-based history remains a separate Atlas Timeline
- Ensure moving routes does not change cache keys or write semantics

### 7. Public identity, people, and social routing

Primary surfaces:

- `app/profile/[userId].tsx`
- Companion screens
- Discover social modules
- Universal Search people results
- Map pins that link to public profiles

Required work:

- Keep public profile URLs stable
- Change self-edit from `/atlas/profile` to `/you`
- Move private companion management to `/you/people`
- Preserve public-profile privacy projections
- Audit language so `Profile`, `You`, `Account`, and `Companions` have distinct
  meanings

### 8. Notifications, push, and persisted destinations

Primary surfaces:

- Notification destination resolver
- Push deep-link handling
- Notification center rows
- Personal-mode fallback
- Memory, social, saved, place, and trip notification payloads

Required work:

- Build a destination matrix by notification family
- Preserve existing trip destinations
- Move personal trust/settings fallbacks to You
- Move memory objects to You/Atlas
- Move saved/visited place objects to Places
- Keep public-person destinations on public profiles
- Test both warm navigation and cold app launches
- Retain aliases for already-delivered notification payloads

### 9. Analytics and observability

Audit:

- Screen-view names
- Tab-selection events
- Search and zero-query engagement
- Avatar/You entrance
- Atlas entrance and child usage
- Discover alias hits
- Atlas alias hits
- Route-not-found and redirect failures
- Origin attribution across Places → Vesper → Trip

Recommended migration signals:

- `you_opened` with originating surface
- `you_destination_selected`
- `places_opened` with zero-query context
- `legacy_route_redirected` with old path and canonical owner
- Task-level success signals for finding Saved, Been, Privacy, and Memory

Analytics are evidence, not the sole retirement gate. Low use may mean poor
findability rather than low user value.

### 10. Tests and device QA

Affected suites include:

- Route helper unit tests
- Navigation semantic-parent tests
- Notification destination tests
- Universal Search routing tests
- Atlas and Discover screen tests
- Public-profile self-edit tests
- Root Stack registration tests
- Convention tests containing route literals
- Maestro flows and direct deep links
- Polish-QA surface manifests
- Mobile stability budgets
- Screenshot/design-alignment registries

Required evidence:

- New canonical route tests
- Old-route redirect tests with parameter preservation
- Warm and cold back-stack tests
- Notification destination matrix tests
- Public/private identity boundary tests
- Three-tab global-chrome visual QA
- You hub and child-route visual QA
- Places zero-query, search, map, Saved, and Been visual QA
- Atlas memory, timeline, reading, and receipt visual QA
- Accessibility labels and focus order
- Physical-device evidence before claiming the navigation migration shipped

### 11. Documentation and governance

Documents likely to require revision or supersession:

- `Travel App/docs/Navigation Contract.md`
- `Travel App/docs/surfaces/global-chrome/contract.md`
- `Travel App/docs/surfaces/header-system/*`
- `Travel App/docs/page-specs/atlas-home.md`
- `Travel App/docs/surfaces/atlas-home/contract.md`
- `Travel App/docs/surfaces/atlas-memory/contract.md`
- `Travel App/docs/surfaces/trust-controls/contract.md`
- `Travel App/docs/implementation/saved-collections-system-handoff.md`
- `Travel App/docs/user-flows/atlas-journeys.md`
- `Travel App/docs/user-flows/canonical-flow-map.md`
- `docs/systems/atlas.md`
- `docs/systems/discover.md`
- Relevant product vision and journey documents

Promotion should produce:

1. A dated navigation decision record
2. An updated Navigation Contract
3. Updated surface contracts for global chrome, You/trust controls, Places,
   Atlas memory, and Saved/Collections
4. Updated canonical flow maps
5. Archival of this working plan

### 12. Backend and API surface

No backend route rename is required for the first migration:

- `/api/me`
- `/api/me/memory`
- `/api/me/delegation-preferences`
- `/api/me/home-bootstrap`
- `/api/me/map`
- `/api/me/narration-history`
- `/api/users/{user_id}/profile`
- `/api/atlas/*`

Backend work is required only if the new Places composition exposes a data gap,
or if a server-authored destination emits hard-coded mobile paths. Audit
notification payload construction and any persisted/shareable URL generation
before declaring the blast radius frontend-only.

## Phased migration

### Execution status — 2026-07-27

Phases 1–2 have established the additive personal-hub foundation in the mobile
app:

- `/you` is the canonical private-hub route;
- `/atlas/profile` remains available as a compatibility redirect to `/you`;
- the Atlas identity control, self-edit action on public profile, and personal
  notification fallback now enter You;
- the same You entry control is now present on the Trips, Vesper, Discover,
  and Atlas tab roots; Atlas and Discover retain their current tab status;
- person-owned child controls now use canonical `/you/*` routes; the old
  `/atlas/{account,phone,privacy,notifications,companions,constraints,
  delegation,data-receipt,feedback}` paths are compatibility redirects.

Phase 3 has a deliberately narrow routing seam, not a Places product surface:

- `/(tabs)/places` and `/(tabs)/places/map` are available as hidden additive
  routes inside the current tab shell;
- they temporarily reuse the existing Discover feed and map, preserving the
  shared navigation chrome and allowing isolated validation;
- practical Saved and Been now have hidden canonical Places facades at
  `/(tabs)/places/saved` and `/(tabs)/places/been`; their legacy Atlas routes
  and implementations remain intact;
- Discover's Saved action and Atlas's practical Saved/Been doors now enter the
  canonical Places children; old deep links and the visible four-tab shell are
  still unchanged.

The first dedicated Places composition now replaces the temporary Discover
facade at `/(tabs)/places`:

- it provides an explicit local scope selector (selected trip, other trip, or
  all places, or a city from the user's actual saved places), search-first
  entry, and context-sensitive Saved/Been/Map
  utilities;
- it renders only existing trip and saved-place read models, with no invented
  home, recommendation, availability, or map state;
- the sole trip action is an explicit "Choose a day in Trips" handoff. It does
  not mutate an itinerary or create a second plan writer.

The global-chrome cutover is now implemented, subject to founder/device review:

- the visible tab shell is **Trips · Vesper · Places**;
- Discover and Atlas remain registered only as hidden legacy tab-route owners;
  their tab roots replace into Places and Your Atlas respectively, preserving
  city, trip, and map context where it is representable;
- `routes.discover()` and `routes.discoverMap()` now resolve to Places, so
  remaining product callers no longer create new Discover-root entrances;
- `routes.atlas()` and the archive/memory route helpers now resolve to
  `/you/atlas/*`; the legacy `/atlas/*` URLs remain available for existing
  deep links while their canonical destinations are exercised;
- practical saved places resolve to Places. Atlas's durable memory, readings,
  artifact, review, scan, recap, and timeline screens are exposed as You/Atlas
  child routes without rewriting their underlying implementations;
- Places route state is serialised through search, map, and map-opened place,
  venue, and experience detail back paths.

Still required before this migration is formally accepted: fresh device
captures for the visible shell and Places state matrix, review of any external
or persisted legacy URL producer, and founder review of the new visible
navigation.

### Phase 0 — Decision and contract lock

Decide:

- Trips, Vesper, Places as the bottom navigation
- Avatar-opened full-screen You hub
- Atlas inside You
- Saved and Been inside Places
- Public profile remains separate
- Trip settings remain trip-owned

Work:

- Approve the route and compatibility tables
- Choose stable labels and analytics names
- Record baseline navigation and task-finding metrics
- Inventory every live route caller and raw string
- Define the route-alias support policy

Exit criteria:

- No unresolved canonical owner for any current Discover or Atlas capability
- Product, design, and frontend agree on the target
- Existing contracts to supersede are named

Rollback:

- None required; no product behavior changes

### Phase 1 — Additive You foundation

Work:

- Add `/you` and canonical `you*` route helpers
- Extract reusable bodies from current Atlas trust/settings screens
- Build the concise You index
- Add the shared avatar to root tab surfaces
- Register routes in the root Stack
- Keep all four current tabs and old routes

Exit criteria:

- Every current trust/account capability is reachable through You
- Public profile remains distinct
- Warm and cold back behavior passes
- No old route has been removed

Rollback:

- Hide the avatar/You entrance; old Atlas settings entrance remains intact

### Phase 2 — Canonicalize You children

Work:

- Move trust/account implementations to `/you/*`
- Convert old Atlas trust/account routes into thin redirects
- Update internal callers, notification fallbacks, and self-profile editing
- Remove duplicated entrances from the You composition

Exit criteria:

- New product code calls only `you*` helpers for person-owned controls
- Old paths preserve parameters and back behavior
- Internal callers to retired trust-route helpers reach zero except explicit
  compatibility tests

Rollback:

- Repoint helpers to old implementations; additive routes remain harmless

### Phase 3 — Create Places as a facade

Work:

- Add `/(tabs)/places` using the strongest current Discover composition
- Add canonical `places*` helpers
- Preserve search, zero-query, map, detail, Vesper, and trip handoffs
- Keep Discover tab available behind the existing shell during validation
- Begin component classification without performing broad renames

Exit criteria:

- Places satisfies the current core Discover finding tasks
- Places has a legible primary search action
- Zero-query state is useful without requiring a generic feed
- Query and map state survive route changes

Rollback:

- Restore Discover as the visible tab; Places remains an additive route

### Phase 4 — Extract Saved and Been

Work:

- Rehome practical Saved under Places
- Split place-mode Long View into Places Been
- Move `/your-map` to the Places-owned map state
- Keep time-mode Long View as You/Atlas Timeline
- Update Atlas shelves, readings, notifications, and Near You callers
- Add parameter-preserving compatibility redirects

Exit criteria:

- Save state has one data implementation and one canonical management owner
- Saved and Been work from cold links
- Atlas no longer presents itself as the owner of practical saved management
- Time and place history have unambiguous owners

Rollback:

- Canonical helpers may temporarily point back to the old implementations while
  preserving the new public route contract

### Phase 5 — Global chrome cutover

Work:

- Change the visible tabs to Trips, Vesper, Places
- Remove Discover and Atlas from the tab bar
- Make the old tab roots redirects
- Verify the floating bar, Vesper center treatment, root avatar, safe areas,
  accessibility, and performance
- Roll out through a reversible shell configuration or feature flag if the app
  has a suitable navigation flag mechanism

Exit criteria:

- All critical tasks remain reachable without either retired tab
- You and Atlas are findable from each root surface
- Saved and Been are findable in Places
- Three-tab visual and interaction QA passes on supported devices
- No unacceptable regression in search, privacy, memory, or active-trip finding

Rollback:

- Restore the four-tab shell while keeping canonical new routes and redirects

### Phase 6 — Semantic retirement

#### Discover retirement work

- Remove Discover terminology from navigation, copy, accessibility, test IDs,
  analytics, component names, type names, and docs
- Delete feed mechanics explicitly rejected from Places
- Rename retained modules when the new ownership is stable
- Retain route redirects

#### Atlas-tab retirement work

- Remove Atlas-specific tab chrome and root-only identity ownership
- Recompose the surviving Atlas Home inside You
- Remove Saved/Been ownership and the four-way Whole Atlas directory
- Remove old helper use from live code
- Retain route redirects for memory, artifacts, readings, and shared links

Exit criteria:

- A repository scan finds no live product call to retired helpers except the
  compatibility layer and its tests
- QA registries and stability budgets use canonical routes
- Current contracts describe the new model
- Alias telemetry is understood
- Device evidence is recorded

Rollback:

- Semantic retirement is not rolled back by resurrecting duplicate owners.
  Restore an entrance to the canonical capability if findability is weak.

### Phase 7 — Compatibility cleanup

Work:

- Review alias usage after the agreed support window
- Remove only redirects proven to have no persisted or external consumers
- Keep cheap aliases for externally shareable Atlas objects
- Archive this working plan after promotion

Exit criteria:

- Every removed alias has an owner, evidence, date, and rollback answer
- No notification, shared link, or persisted navigation record can emit it

## Discover retirement gates

Discover is retired only when all are true:

- Places is the visible and canonical search/browse owner
- Typed search, zero-query value, map, details, saves, Vesper handoff, and trip
  handoff have parity or an explicitly accepted replacement
- Old Discover routes redirect correctly in warm and cold starts
- Discover-specific notification and search destinations have migrated
- Places does not depend on an unexplained generic feed
- Copy, accessibility, analytics, QA, and docs no longer teach Discover as a
  destination
- Rejected Discover modules are deleted or archived rather than left as hidden
  parallel composition

Retirement means the destination and ownership model are gone. It does not mean
that every component originally written under `components/discover` must be
discarded.

## Atlas-tab retirement gates

Atlas is retired as a tab only when all are true:

- The avatar and You hub are available from Trips, Vesper, and Places
- `/you/atlas` provides a coherent private-memory home
- What Vesper Knows and memory correction remain prominent and functional
- Trust/account controls have canonical You routes
- Practical Saved and Been have canonical Places routes
- Time-based history, readings, artifacts, inbox, candidates, and recaps remain
  reachable
- Notifications and shared links resolve through new or legacy paths
- The old Atlas tab root redirects without a broken back stack
- Canonical docs no longer require Atlas as a top-level tab

Retirement means Atlas no longer competes with Trips, Vesper, and Places in
global navigation. The Atlas concept and durable objects remain.

## Validation task set

At minimum, validate that a person can:

1. Find an active trip
2. Start or continue a Vesper conversation
3. Search for a place from a zero-query state
4. Reopen a saved place
5. Review places they have been
6. Open their private Atlas and a Reading
7. Inspect and correct what Vesper knows
8. Find privacy and notification controls
9. View their public profile without exposing private controls
10. Open old Discover and Atlas deep links
11. Open an already-delivered notification into its intended destination
12. Return predictably using back from every warm and cold entry

Measure task success, time to destination, wrong turns, and the first place
participants look. A lower Atlas-tab click count after hiding the tab is not
proof that the underlying memory need disappeared.

## Risks and mitigations

| Risk | Mitigation |
|---|---|
| You becomes another overloaded Atlas directory | Keep You shallow; group Atlas artifacts one level deeper |
| Public and private profile concepts blur | Preserve `/profile/[userId]`; use “View public profile” as a projection |
| Places becomes a generic engagement feed | Make search primary; constrain zero-query modules to useful context |
| Saved state forks during the route move | Reuse existing hooks/components; change owner and route before redesign |
| Long View spans two owners forever | Split place mode into Places Been and time mode into Atlas Timeline |
| Cold links develop false back behavior | Give every child a semantic fallback and test cold launches |
| Old notifications break | Keep aliases and audit destination construction before cutover |
| Atlas memory becomes hard to find | Persistent avatar, visible Your Atlas row, contextual Vesper links |
| Discover and Atlas retire in one un-debuggable release | Keep You and Places migrations independently reversible |
| Internal names preserve the old mental model | Perform semantic cleanup only after canonical routes stabilize |
| Documentation contradicts the product | Promote into Navigation and surface contracts before final retirement |

## Open decisions

- Final label: `You`, `Your profile`, or another title. Current recommendation:
  **You**.
- Whether the identity avatar appears on every root screen or only canonical
  tab roots. Current recommendation: every canonical tab root.
- Whether Places Been defaults to list, map, or remembered last state.
- Whether Atlas Timeline should retain the `Long View` product label.
- Whether `Preferences & constraints` needs an index or opens the current
  constraints screen directly.
- Whether public-profile editing needs a focused `/you/public-profile` route.
- Which current Discover modules earn the first Places zero-query composition.
- Alias-support duration and which externally shareable Atlas routes remain
  permanent.
- Whether the global-shell cutover uses an existing feature-flag system or a
  short-lived build-time configuration.

## Definition of migration complete

The migration is complete only when:

- Trips, Vesper, and Places are the visible bottom destinations
- The avatar opens You consistently
- Every current capability has one documented canonical owner
- Atlas is coherent and reachable inside You
- Discover no longer exists as a taught product destination
- Saved and Been are canonical Places children
- Public profile and trip settings retain their boundaries
- Old routes resolve through tested compatibility redirects
- Notification, search, and social destinations are migrated
- QA registries, tests, analytics, and docs use the new vocabulary
- Supported-device evidence confirms navigation, layout, accessibility, and
  back behavior
- The accepted model has been promoted into canonical contracts and this
  working plan has been archived

## References

- `docs/product/Product Thesis and Strategy.md`
- `docs/product/Trips Vision.md`
- `docs/product/Discover Vision.md`
- `docs/product/What We Believe.md`
- `docs/product/Surfacing Strategy.md`
- `docs/systems/discover.md`
- `docs/systems/atlas.md`
- `Travel App/docs/Navigation Contract.md`
- `Travel App/docs/page-specs/atlas-home.md`
- `Travel App/docs/surfaces/global-chrome/contract.md`
- `Travel App/docs/surfaces/atlas-home/contract.md`
- `Travel App/docs/surfaces/atlas-memory/contract.md`
- `Travel App/docs/surfaces/trust-controls/contract.md`
- `Travel App/docs/surfaces/trip-settings-admin/contract.md`
- `Travel App/docs/implementation/saved-collections-system-handoff.md`
- `Travel App/docs/user-flows/canonical-flow-map.md`
