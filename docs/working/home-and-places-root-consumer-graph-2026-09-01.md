---
doc_type: working
status: active
owner: founder / backend / frontend
created: 2026-09-01
last_verified: 2026-09-01
expires: 2026-10-01
why_new: Package 0 requires an explicit consumer graph before any root compiler can replace a legacy producer. This is the migration map for Home and Places; it is intentionally narrower than a general service inventory.
source_of_truth_for:
  - Home and Places legacy consumers and deletion gates
depends_on:
  - docs/working/home-and-places-root-implementation-program-2026-08-31.md
  - docs/working/home-and-places-build-manifest-2026-08-30.md
---

# Home and Places — consumer graph

This graph distinguishes the new root contract from the legacy surfaces that
still carry production behavior. A producer is not safe to delete merely
because a new route exists: every consumer below must either move to a typed
root projection or be explicitly retired.

## Home

```text
canonical owners (Experience Graph, commitments, openings, receipts)
        │
        ├── legacy ExperienceProjection read
        │       └── root v1 compiler ──► /api/root-projections/home
        │                                  └── HomeRootExperience (flagged)
        │
        ├── concierge_home / concierge_feed producers
        │       ├── Chat and notification grounding (shared; keep)
        │       └── legacy Trips Home / TripsHomeController (migration target)
        │
        └── trip stack producers/models
                └── Trips stack page (migration target; receipts remain owner data)
```

The current v1 compiler is a characterization bridge, not the v2 ordering
authority. `concierge_feed` may supply proven source signals and golden cases,
but the v2 candidate gates choose the dominant and region seats. Chat and
notification consumers are outside this package and must not be changed by a
Home migration.

## Places

```text
canonical place / relationship / provider owners
        │
        ├── places.sections producers
        │       └── PlacesFeed (legacy section/reason contract)
        │              ├── root v1 compiler ──► /api/root-projections/places
        │              └── legacy usePlacesFeed / PlacesWorkspace (migration target)
        │
        ├── Experience Graph summary read
        │       └── PlacesWorkspace side-card (must become a candidate source)
        │
        └── search + map providers
                └── Places search/map affordances (remain owner capabilities)
```

The v2 Places compiler consumes bounded candidate adapters, not a page-shaped
`PlacesFeed`. Existing section reasons become evidence and source labels;
they do not become the new World Field / Focus / Path / Live hierarchy.

## Shared seams and deletion gates

| Legacy surface | Keep now | Migration gate | Delete only when |
| --- | --- | --- | --- |
| `concierge_feed` | Yes; Chat/notifications still consume it | candidate characterization parity | Home v2 has equivalent owner-backed signals and Chat has its own migration decision |
| `TripsHomeController` / Trips stack | Yes, behind legacy route | Home v2 real-data parity | Home root serves every route state and its action/readback tests pass |
| `PlacesFeed` + `usePlacesFeed` | Yes, as adapter source | Places v2 bounded portfolio + state parity | Places root owns ordering, partial failure, and typed action continuity |
| Experience Graph summary side-card | Yes, read-only | candidate adapter with cluster identity | same evidence is admitted once in the Places projection |
| search/map capabilities | Yes | typed projection envelope and owner handoff | never delete; migrate destination identity, not provider ownership |

No package 0–1 change edits Chat or Life UI/behavior. Life's accepted grant,
return-arbitration, and refinding contracts are referenced as upstream
authority; their production lanes remain independent.

## Package 0 characterization cases

The first fixture set should preserve these proven behaviors while the carrier
changes: urgent provider failure, current commitment, prepared opening, quiet
empty state, one Places conviction/fork, saved-unplaced continuity, partial
Places producer failure, and a typed search/map handoff. These are signals to
retain—not evidence that the old section/rank hierarchy is canonical.
