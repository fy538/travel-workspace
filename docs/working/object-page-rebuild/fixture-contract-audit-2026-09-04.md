---
doc_type: working
status: active
owner: product / design / backend / frontend
created: 2026-09-04
last_verified: 2026-09-04
expires: 2026-10-04
why_new: Records the boundary between the design-lab fixture vocabulary and the generated entity API so implementation does not promote synthetic fields or backfill data by accident.
source_of_truth_for: []
supersedes: []
---

# Object-page fixture contract audit

## Finding

`docs/working/object-page-rebuild/fixtures.json` is a design and acceptance
fixture pack, not a serialized `EntityDetailPresentation` payload. Its states
are useful for composition tests, but several fields intentionally describe
future contracts that are not in the current generated API.

The fixture pack therefore remains unchanged. The guarded mobile renderer is
built from the current v1/v2 presentation plus the separately read-only
`EntityResearchBrief`; it must not coerce fixture-only values into runtime
truth.

## Shape differences found during the 2026-09-04 audit

| Fixture vocabulary | Current wire shape | Decision |
| --- | --- | --- |
| `lineage.place_slug`, `lineage.also_listed_as` | `EntityLineageResponse` has city, neighbourhood, and neighbourhood place id only | Keep fixture-only until a provenance/alias contract is approved; do not render these by guessing from names. |
| `tail.address` on venues/sites | Current `VenueTail`/`SiteTail` do not carry an address | The object page shows the available locality/map handoff; add an address only with an owned catalog field and generated contract change. |
| `research.paragraph_sources` | Newly supported as an optional generated field, but existing stored briefs normally have no mapping | Empty means “no inline markers”; the client never assigns source numbers by paragraph position. |
| `people`, `people_override`, grants, withdrawal, blocked lines | No people-lines read model or server-side audience resolution yet | Keep these acceptance states as future contract fixtures; no client-side filtering or synthetic faces. |
| `viewer.location`, `accuracy_m`, `observed_at` | Live situation request owns these fields and is no-store | Pass only through an explicit situation request; never persist or echo precise origin data. |
| `Tonight?`, `Leave for someone`, face sheet actions | Occasion-live and addressed-handoff owners are not wired to the rebuild | Do not show unavailable verbs; keep existing owner routes as the source of truth. |
| `fixture://` media/source URLs | Production media/source models require permitted HTTP(S) URLs and attribution | Fixture URLs are not production links and must not be sent to `PlacesMedia` or opened externally. |

## Implementation consequence

The acceptance pack can be used in a future fixture adapter that maps its
synthetic values into typed test doubles. Until that adapter exists, tests
should assert the current API contract and explicit absence rules. A fixture
shape mismatch is a contract-review item, not a reason to add catalog columns,
seed rows, provider calls, or broad backfill.

## Current evidence

- `EntityResearchBrief.paragraph_sources` is optional and validated against
  the explicit source list; the object body renders no guessed markers.
- `ObjectPageRebuild` accepts an explicit, request-scoped situation read and
  displays only an unexpired server summary.
- No catalog backfill, research refresh, provider lookup, or fixture migration
  was run as part of this audit.
