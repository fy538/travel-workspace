# Plan - Atlas Timeline Backend

> **Outcome (as of 2026-07-03):** ✅ Shipped — persisted timeline/almanac projection with hide/pin/rename + dedup/restore (journey 11 built & canaried).

Status: planning handoff  
Date: 2026-06-06  
Audience: future implementation session working across `travel-agent` and `travel-app`

## Executive Summary

Atlas Timeline should become the canonical backend read surface for a user's travel life. It should contain both:

- trips created, planned, taken, or returned to inside Vesper
- optional diary memories inferred from the user's photo library after explicit permission

The product distinction matters:

- Trips is where travel is planned.
- Atlas is where travel becomes part of the person.
- Timeline is the factual/provenance-heavy chronology.
- Almanac is the authored Atlas layer over that chronology.

The immediate recommendation is to start with a backend live aggregation endpoint over existing Trips and Atlas tables. Do not create a persistent timeline table in the first slice unless we need hide/pin/rename or generated month summaries immediately. Use V0 to prove the contract, then promote to a projected/persisted read model once the shape is stable.

## Context For A New Session

This plan follows two recent design investigations:

1. Atlas Home Claude design alignment
   - External design bundle: `https://api.anthropic.com/v1/design/h/8dmQ45BSi7Js0WJbV1kToQ?open_file=Atlas+Home.html`
   - Intent from the bundle: Atlas Home should report what is true, not just what is new. The year ribbon should become a named year door into an Almanac. The Almanac/named-ribbon idea should be treated as a product slice, not smuggled into a minor polish pass.

2. Onboarding Claude design alignment
   - Local doc: `docs/audits/onboarding-claude-design-alignment-2026-06.md`
   - Core doctrine:
     - value before auth
     - trip or diary is the value
     - Photos permission is asked only as an optional diary gift
     - auth happens after a trip draft exists or a diary is worth keeping
     - invite users see the real trip first, then sign in to join

The onboarding doc is especially relevant because it frames the "diary" as optional. A user who enters through the dreaming branch may grant Photos permission and allow Vesper to construct a private travel diary from local photo metadata. A user who declines should still land warmly in Atlas without punishment. This creates a backend requirement: the timeline must support both app-native trips and photo-derived memories, while preserving provenance and consent boundaries.

## Current Implementation Snapshot

### Existing Frontend Almanac V0

A frontend-derived Almanac V0 was implemented as a separate route:

- `travel-app/app/atlas/almanac.tsx`
- `travel-app/utils/atlasAlmanac.ts`
- `travel-app/utils/routes.ts` has `routes.atlasAlmanac()`
- `travel-app/app/(tabs)/atlas/index.tsx` makes the Atlas Home year ribbon tappable
- `travel-app/components/atlas/AtlasV3Primitives.tsx` supports optional month labels on the ribbon

That V0 derives entries from:

- `useAtlasArtifactsPage`
- `useAtlasInboxPage`
- `useTrips`

This is the prototype contract, not the final architecture. The frontend should eventually consume a backend timeline/almanac response rather than knowing how to combine trips, pending candidates, and artifacts itself.

### Existing Backend Atlas Surface

Important files:

- `travel-agent/backend/api/routes/atlas.py`
- `travel-agent/backend/atlas/models.py`
- `travel-agent/backend/core/db/atlas.py`

Existing backend read models already include:

- `GET /api/atlas/home`
- `GET /api/atlas/map`
- `GET /api/atlas/receipt`
- `GET /api/atlas/artifacts`
- `GET /api/atlas/search`
- Atlas candidate and artifact CRUD/review flows

`GET /api/atlas/home` already combines:

- pending Atlas candidates
- recent Atlas artifacts
- Personal Memory phrases
- trip count
- artifact/place counts

This proves the backend already has the local pattern for Atlas read models that compose multiple underlying sources.

### Existing Atlas Candidate Model

Atlas candidates are produced by local client clustering and submitted to the backend. The current candidate create shape includes:

- date range
- place guess
- place count
- photo count
- sample photo ids
- confidence
- candidate type
- cluster reason

This is a good basis for diary draft timeline entries. The backend should not treat these as final memories. They are possible memories until the user reviews and approves them.

### Existing Photo Scan Flow

Important frontend files:

- `travel-app/app/atlas/scan.tsx`
- `travel-app/hooks/useAtlasPhotoPicker.ts`
- `travel-app/hooks/useAtlasFullScan.ts`
- `travel-app/utils/atlasCluster.ts`
- `travel-app/utils/atlasHomeWorkInference.ts`
- `travel-app/utils/photoPermission.ts`

Current properties:

- manual picker path exists and is more V0-safe
- full-library scan path exists in frontend code, but should be treated carefully
- local clustering reads photo metadata on device
- backend receives candidate descriptors, not raw library-wide photo uploads
- copy must be precise: raw photos can stay local, but submitted candidate descriptors do reach the backend

### Existing Trip Surface

Important files:

- `travel-app/app/trip-begin.tsx`
- `travel-app/context/TripContext.tsx`
- `travel-agent/backend/api/routes/trips.py`
- `travel-agent/backend/core/db/trips.py`

The trip branch from onboarding can replay into existing authenticated trip creation. The timeline should treat trips as one source family.

## Product Model

Atlas Timeline should contain four primary families:

1. Planned trips
   - Source: Trips table/API
   - Meaning: user intends to go somewhere
   - Timeline date: trip start/end when known, created date when date is unknown
   - Example: "Tokyo, Oct 2-9"

2. Taken trips
   - Source: Trips table/API
   - Meaning: a Vesper-planned trip has happened or is in the past
   - Timeline date: trip start/end
   - Example: "Lisbon, returned"

3. Diary drafts
   - Source: Atlas candidates created from photo scan
   - Meaning: Vesper found a possible memory
   - Timeline date: candidate date range
   - Example: "Alfama, 22 photos"
   - Must remain reviewable/dismissible

4. Kept memories
   - Source: Atlas artifacts approved from candidates
   - Meaning: user chose to keep this memory
   - Timeline date: artifact date range
   - Example: "Amalfi Coast, two weeks in"

Future source families could include:

- imported trips
- Apple Journaling Suggestions
- saved places that became meaningful
- postcards/shared memories
- manually authored diary entries

## Key Conceptual Distinctions

### Occurred Time vs Surfaced Time

Do not collapse these.

- `occurred_start` / `occurred_end`: when the travel or memory happened in the user's life
- `surfaced_at`: when Vesper noticed, generated, imported, or showed it
- `created_at`: when the backend row/projection was created
- `updated_at`: when backend projection changed

Example:

- a 2023 photo cluster may be surfaced during onboarding in 2026
- a 2026 trip may be created in May, occur in October, and become a memory afterward

The Timeline mostly sorts by occurred time. Operational feeds sort by surfaced time.

### Timeline vs Almanac vs Activity

Keep these separate:

- Timeline: factual, chronological, queryable, provenance-heavy
- Almanac: authored, grouped, named, more emotional/product-facing
- Activity/Inbox: what needs attention now

Atlas Home should report "what is true." Inbox/desk should report "what needs action." Almanac should report "what the year feels like."

### Canonical Sources vs Projection

Trips, Atlas candidates, and Atlas artifacts remain canonical. Timeline entries should be either:

- live aggregation objects in V0, or
- projected rows in a later `atlas_timeline_entries` table

Do not make timeline entries the canonical source of truth for trips or memories.

## Consent And Privacy Model

Timeline entries need explicit provenance and consent metadata because sources have different privacy expectations.

Recommended consent fields:

```ts
consent_scope:
  | "app_trip"              // user created/planned this in Vesper
  | "photo_metadata_local"  // inferred locally before backend submission
  | "photo_candidate"       // descriptor submitted to backend from scan
  | "user_kept"             // approved/kept by user
  | "imported"              // future import source

raw_photo_policy:
  | "none"
  | "local_only"
  | "selected_upload"
```

For V0 backend responses, `photo_metadata_local` may not appear because local-only preview entries exist before auth/backend submission. Once submitted to backend, use `photo_candidate`.

Important copy implication:

- Safe: "Photos stay on this iPhone unless you choose to add them."
- Safe: "Vesper sends only draft descriptors when you ask it to keep working."
- Unsafe unless guaranteed end to end: "Nothing leaves your phone."

## Backend V0: Live Aggregation

### Goal

Add backend read models that return a unified Atlas timeline and an Almanac grouping using existing tables only.

No new table in V0.

### New API Endpoints

Recommended first endpoint:

```http
GET /api/atlas/timeline?year=2026&limit=100&cursor=...
```

Optional second endpoint, if the frontend wants grouped/authored data immediately:

```http
GET /api/atlas/almanac?year=2026
```

Alternative: implement only `/api/atlas/timeline` and let the frontend group. But because Almanac is a product surface and will eventually have generated month labels/summaries, it is reasonable to add `/api/atlas/almanac` early.

### Response Model Sketch

Add to `travel-agent/backend/atlas/models.py`:

```py
AtlasTimelineSourceType = Literal[
    "trip",
    "atlas_candidate",
    "atlas_artifact",
]

AtlasTimelineKind = Literal[
    "planned_trip",
    "taken_trip",
    "diary_draft",
    "kept_memory",
]

AtlasTimelineConsentScope = Literal[
    "app_trip",
    "photo_candidate",
    "user_kept",
]

AtlasTimelineVisibility = Literal[
    "draft",
    "visible",
    "hidden",
    "archived",
]

class AtlasTimelineEntry(BaseModel):
    id: str
    source_type: AtlasTimelineSourceType
    source_id: str
    timeline_kind: AtlasTimelineKind
    occurred_start: date | None = None
    occurred_end: date | None = None
    surfaced_at: datetime
    title: str
    body: str | None = None
    place_label: str | None = None
    media_count: int = 0
    confidence: Confidence | None = None
    consent_scope: AtlasTimelineConsentScope
    visibility: AtlasTimelineVisibility = "visible"
    provenance: list[AtlasProvenanceRef] = Field(default_factory=list)
    action: AtlasAction | None = None

class AtlasTimelineGroup(BaseModel):
    key: str
    year: int
    month: int
    label: str
    entries: list[AtlasTimelineEntry] = Field(default_factory=list)

class AtlasTimelineSummary(BaseModel):
    year: int | None = None
    entry_count: int = 0
    planned_trip_count: int = 0
    taken_trip_count: int = 0
    diary_draft_count: int = 0
    kept_memory_count: int = 0
    place_count: int = 0

class AtlasTimelineReadModel(BaseModel):
    generated_at: datetime
    summary: AtlasTimelineSummary
    entries: list[AtlasTimelineEntry] = Field(default_factory=list)
    next_cursor: str | None = None

class AtlasAlmanacReadModel(BaseModel):
    generated_at: datetime
    summary: AtlasTimelineSummary
    groups: list[AtlasTimelineGroup] = Field(default_factory=list)
    empty_state: AtlasMapEmptyState | None = None
```

Use existing `AtlasAction`:

- artifact: `{ type: "open_artifact", id: artifact_id }`
- candidate: `{ type: "open_candidate", id: candidate_id }`
- trip: `{ type: "open_trip", id: trip_id }`

### V0 Source Mapping

#### Atlas Artifact -> Kept Memory

Source table/model:

- `atlas_artifacts`
- `AtlasArtifactShell`

Mapping:

```ts
id: "artifact:{artifact.id}"
source_type: "atlas_artifact"
source_id: artifact.id
timeline_kind: "kept_memory"
occurred_start: artifact.date_range_start
occurred_end: artifact.date_range_end
surfaced_at: artifact.created_at or updated_at
title: artifact.title
body: artifact.one_line_read
place_label: artifact.place_label
media_count: artifact.photo_ids.length
confidence: "high"
consent_scope: "user_kept"
visibility: "visible"
action: open_artifact
```

#### Pending Atlas Candidate -> Diary Draft

Source table/model:

- `atlas_candidates`
- `AtlasCandidate`

Mapping:

```ts
id: "candidate:{candidate.id}"
source_type: "atlas_candidate"
source_id: candidate.id
timeline_kind: "diary_draft"
occurred_start: candidate.date_range_start
occurred_end: candidate.date_range_end
surfaced_at: candidate.created_at
title: candidate.place_guess || "A possible memory"
body: candidate.cluster_reason
place_label: candidate.place_guess
media_count: candidate.photo_count
confidence: candidate.confidence
consent_scope: "photo_candidate"
visibility: "draft"
action: open_candidate
```

Only include candidates where `status = "pending"` for diary drafts. Approved candidates should usually be represented by their artifacts to avoid duplicate timeline entries. Dismissed candidates should not appear in the default timeline.

#### Trip -> Planned/Taken Trip

Source table/model:

- Trips backend models/routes

Mapping:

```ts
id: "trip:{trip.id}"
source_type: "trip"
source_id: trip.id
timeline_kind: trip ended before now ? "taken_trip" : "planned_trip"
occurred_start: trip.start_date
occurred_end: trip.end_date
surfaced_at: trip.created_at
title: destination or trip.title
body: trip.planning_brief or phase-aware fallback
place_label: destination
media_count: 0
confidence: null
consent_scope: "app_trip"
visibility: "visible"
action: open_trip
```

If the trip has no dates, use `created_at` for sorting in a separate "undated" group or include only when no `year` filter is supplied. Avoid forcing undated planned trips into an arbitrary month.

### Sorting And Grouping

Default sort:

1. entries with `occurred_start`, descending
2. fallback to `surfaced_at`, descending
3. stable tie-breaker priority:
   - diary draft
   - kept memory
   - trip

Almanac grouping:

- group by `occurred_start` month/year
- label format: `OCT 26`
- omit undated entries from `/api/atlas/almanac?year=...` unless a product decision adds an "On the table" group

### Year Filtering

`year=2026` should include entries where:

- `occurred_start.year == 2026`, or
- date ranges overlap the year

Use overlap logic:

```sql
occurred_start <= year_end AND occurred_end >= year_start
```

If `occurred_end` is null, treat it as `occurred_start`.

### Pagination

V0 can support `limit` and `cursor` later. If implementation is small and the expected result set is low, return up to 100 entries for a year and set `next_cursor = null`.

When adding cursor pagination, use a cursor over:

- primary sort date
- source type
- source id

## Backend V1: Persisted Projection

### When To Add Persistence

Add a table once we need any of:

- hide/pin/rename
- stable cross-device ordering after user edits
- generated titles/summaries
- cached month/year summaries
- expensive provenance joins
- background generation
- audit history of timeline changes

### Suggested Table

```sql
CREATE TABLE atlas_timeline_entries (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,

  source_type TEXT NOT NULL,
  source_id TEXT NOT NULL,
  timeline_kind TEXT NOT NULL,

  occurred_start DATE,
  occurred_end DATE,
  surfaced_at TIMESTAMPTZ NOT NULL DEFAULT now(),

  source_title TEXT,
  generated_title TEXT,
  user_title TEXT,
  source_body TEXT,
  generated_body TEXT,
  user_body TEXT,
  place_label TEXT,
  media_count INTEGER NOT NULL DEFAULT 0,

  confidence TEXT,
  consent_scope TEXT NOT NULL,
  raw_photo_policy TEXT NOT NULL DEFAULT 'none',
  visibility TEXT NOT NULL DEFAULT 'visible',

  pinned_at TIMESTAMPTZ,
  provenance JSONB NOT NULL DEFAULT '[]'::jsonb,
  source_hash TEXT,
  generation_status TEXT NOT NULL DEFAULT 'ready',
  generation_prompt_version TEXT,
  generated_at TIMESTAMPTZ,

  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),

  UNIQUE (user_id, source_type, source_id)
);

CREATE INDEX atlas_timeline_user_occurred_idx
  ON atlas_timeline_entries (user_id, occurred_start DESC, occurred_end DESC);

CREATE INDEX atlas_timeline_user_visibility_idx
  ON atlas_timeline_entries (user_id, visibility);
```

Display rule:

```ts
display_title = user_title ?? generated_title ?? source_title
display_body = user_body ?? generated_body ?? source_body
```

### Projector Responsibilities

The projector should update timeline entries when canonical sources change:

- trip created/updated -> upsert planned/taken trip entry
- trip enters past/completed state -> update `timeline_kind`
- Atlas candidate submitted -> upsert diary draft entry
- Atlas candidate dismissed -> hide/archive draft entry
- Atlas candidate approved -> either hide draft and create artifact entry, or update relation
- Atlas artifact inserted/updated -> upsert kept memory entry
- Atlas artifact deleted/forgotten -> hide/archive entry

Keep projector idempotent. It should be safe to run a full rebuild for one user.

Potential function names:

- `project_trip_to_timeline(user_id, trip_id)`
- `project_candidate_to_timeline(user_id, candidate_id)`
- `project_artifact_to_timeline(user_id, artifact_id)`
- `rebuild_timeline_for_user(user_id)`

## User Control Endpoints

Add after persistence:

```http
PATCH /api/atlas/timeline/{entry_id}
POST /api/atlas/timeline/{entry_id}/hide
POST /api/atlas/timeline/{entry_id}/pin
POST /api/atlas/timeline/{entry_id}/unpin
```

Patch body:

```py
class AtlasTimelineEntryUpdate(BaseModel):
    user_title: str | None = Field(default=None, max_length=120)
    user_body: str | None = Field(default=None, max_length=500)
    visibility: Literal["visible", "hidden", "archived"] | None = None
```

Do not allow the user update to mutate canonical trip/candidate/artifact rows unless explicitly designed. Timeline edits are display overrides.

## Generated Almanac Layer

The Almanac should eventually be more than a chronological list. Add generation only after factual timeline is in place.

Generated fields:

- year title/summary
- month names
- month summaries
- highlight ordering
- "what this year felt like"

Store generation metadata:

```ts
generation_status
generation_prompt_version
source_hash
generated_at
```

Do not block timeline reads on generation. Serve factual entries immediately and enrich asynchronously.

Possible future table:

```sql
CREATE TABLE atlas_almanac_summaries (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  year INTEGER NOT NULL,
  month INTEGER,
  title TEXT,
  body TEXT,
  source_hash TEXT NOT NULL,
  generation_status TEXT NOT NULL,
  generation_prompt_version TEXT,
  generated_at TIMESTAMPTZ,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE (user_id, year, month)
);
```

## Onboarding Integration

The onboarding design wants:

```txt
Cover -> Fork -> Dreaming branch -> Diary gift -> Photos permission -> auth while diary constructs -> Atlas
```

Backend implication:

- Do not require pre-auth backend writes for V0.
- Let the client scan locally and create a local preview.
- After auth, replay selected/submittable candidates into existing Atlas candidate creation.
- Timeline then shows those as `diary_draft` entries.

Potential candidate-create additions:

```py
source: Literal["atlas_scan", "onboarding_diary"] = "atlas_scan"
onboarding_session_id: str | None = None
consent_scope: Literal["photo_candidate"] = "photo_candidate"
```

This can be added later; V0 can infer `photo_candidate` for all Atlas candidates.

Also add a non-constraint onboarding signal endpoint separately from timeline:

```http
POST /api/users/{id}/onboarding-signals
```

This is for dreaming branch taste/pace, not hard safety constraints.

Example body:

```json
{
  "branch": "dreaming",
  "interest_axis": "food_and_neighborhoods",
  "pace_axis": "slow",
  "source": "onboarding_v2"
}
```

This should create observations and optionally refresh Personal Memory. Do not store taste/pace as hard constraints.

## Frontend Migration Plan

### Step 1: Add API Types And Hook

Files:

- `travel-app/types/atlas.ts`
- `travel-app/data/atlas.ts`
- `travel-app/utils/api/mock/atlas.ts`

Add:

- `AtlasTimelineEntry`
- `AtlasTimelineGroup`
- `AtlasTimelineSummary`
- `AtlasTimelineReadModel`
- `AtlasAlmanacReadModel`
- `useAtlasTimeline({ year })`
- `useAtlasAlmanac({ year })`

Mock should include:

- one planned trip
- one diary draft
- one kept memory
- empty state

### Step 2: Update Almanac Screen

File:

- `travel-app/app/atlas/almanac.tsx`

Replace local composition from:

- `useAtlasArtifactsPage`
- `useAtlasInboxPage`
- `useTrips`
- `buildAtlasAlmanacEntries`

with:

- `useAtlasAlmanac({ year })`

Map backend `AtlasAction` to routes:

- `open_artifact` -> `routes.atlasArtifact(id)`
- `open_candidate` -> `routes.atlasCandidate(id)`
- `open_trip` -> `routes.tripDetail(id)` or trip chat depending product decision

Keep `utils/atlasAlmanac.ts` only as a test helper or remove it after backend migration.

### Step 3: Update Atlas Home Ribbon

Once backend returns month marks/groups, Atlas Home should stop deriving the year ribbon only from artifacts/trips/candidates. Use timeline/almanac summary for:

- current year label
- named month dots
- `OPEN ALMANAC` behavior
- empty/no-diary state

### Step 4: Onboarding Diary Source

When onboarding flow exists:

- local preview uses scan result before auth
- post-auth replay submits candidates
- Almanac immediately gets diary drafts from backend

## Backend Implementation Order

Recommended order for a new coding session:

1. Read existing Atlas models/routes/db helpers.
2. Add timeline/almanac Pydantic models.
3. Add DB helper functions if existing list functions are insufficient:
   - list recent/all artifact shells for year
   - list pending candidates for year
   - list trips for user/year
4. Implement pure mappers:
   - `_timeline_entry_from_artifact`
   - `_timeline_entry_from_candidate`
   - `_timeline_entry_from_trip`
5. Implement sorting/grouping helpers with unit tests.
6. Add `GET /api/atlas/timeline`.
7. Add `GET /api/atlas/almanac`.
8. Export OpenAPI/types if that is the repo convention for this workflow.
9. Migrate frontend Almanac hook/screen.
10. Keep persisted table as follow-up unless hide/pin/rename is in scope.

## Backend Test Plan

Add focused tests around pure mapping and endpoint behavior.

Suggested cases:

- artifact becomes `kept_memory` with `consent_scope=user_kept`
- pending candidate becomes `diary_draft` with `visibility=draft`
- approved/dismissed candidate does not duplicate default timeline
- future trip becomes `planned_trip`
- past trip becomes `taken_trip`
- entries sort by occurred date descending
- entries with same date use stable tie priority
- year filter includes overlapping date ranges
- Almanac groups by month label
- empty timeline returns usable empty state

If endpoint tests are expensive, start with mapper/grouping unit tests and one route smoke test.

## Acceptance Criteria

Backend V0 is done when:

- `GET /api/atlas/timeline?year=YYYY` returns trips, pending candidates, and artifacts in one normalized contract
- `GET /api/atlas/almanac?year=YYYY` returns grouped entries suitable for the existing Almanac screen
- each entry includes source type/id, timeline kind, consent scope, visibility, occurred dates, surfaced time, title/body, and action
- approved artifacts and pending candidates do not show as confusing duplicates
- no raw photo upload behavior changes
- no pre-auth backend write is required

Frontend migration is done when:

- Almanac screen consumes backend almanac data instead of local composition
- mock API covers all timeline entry families
- Atlas Home ribbon can still open Almanac
- focused screen/data tests pass
- `npm run typecheck` passes

Persistence V1 is done when:

- `atlas_timeline_entries` exists
- projectors are idempotent
- hide/pin/rename work without mutating canonical source rows
- generated fields have source hashes and prompt versions

## Open Product Questions

1. Should planned future trips appear in Atlas Almanac, or only in Timeline?
   - Recommendation: show them in Timeline; Almanac can include a subtle "on the horizon" group if product wants.

2. Should the same trip appear twice: once as planned and once as returned?
   - Recommendation: one entry whose kind changes from `planned_trip` to `taken_trip`, unless a separate generated memory artifact exists.

3. Should approved candidate drafts remain visible after artifact creation?
   - Recommendation: no in default surfaces. Keep provenance linking artifact back to candidate.

4. Should onboarding diary candidates submit automatically after auth?
   - Recommendation: submit descriptors only after explicit "Build my diary" consent and auth. Keep each resulting memory as a draft until user keeps/dismisses.

5. Should limited Photos permission count as diary consent?
   - Recommendation: yes, but represent scope precisely. The user chose the subset.

6. Should generated Almanac summaries be per year or per month first?
   - Recommendation: per month first, because it supports the named-ribbon/month-door concept and is easier to regenerate incrementally.

## Risks

- Privacy copy drifting ahead of architecture.
  - Mitigation: encode consent scope in the API and keep raw-photo policy explicit.

- Timeline becoming a second source of truth.
  - Mitigation: V0 is live aggregation; V1 table is projection with unique source refs.

- Almanac mixing operational drafts with cherished memories too aggressively.
  - Mitigation: distinguish `visibility=draft` and `timeline_kind=diary_draft` in UI.

- Future planned trips making Atlas feel less like memory.
  - Mitigation: product can filter Almanac to past/current year memories while Timeline still knows future trips.

- Duplicate entries when candidate becomes artifact.
  - Mitigation: default timeline excludes approved candidates and shows artifact.

## Suggested First PR Scope

Keep the first PR small:

- add timeline/almanac backend models
- implement live aggregation helpers
- expose `GET /api/atlas/timeline`
- expose `GET /api/atlas/almanac`
- add backend tests for mapping/grouping

Do not include:

- persisted timeline table
- generated summaries
- hide/pin/rename
- onboarding controller
- photo scan behavior changes

Then second PR:

- migrate frontend Almanac to backend
- update mock API/types
- keep current screen design

Third PR:

- add onboarding diary source metadata and post-auth replay support

This sequence keeps the contract clear and the blast radius low.

