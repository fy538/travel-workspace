---
doc_type: working
status: active
owner: engineering / product / design
created: 2026-08-10
last_verified: 2026-08-10
expires: 2026-09-09
why_new: Records the exact code, operator, source-truth, and device-evidence steps required to dogfood the August Trips and Places home-surface explorations.
source_of_truth_for:
  - home-surfaces-dogfood-activation-2026-08-10
related:
  - intentional-convergence-engineering-plan-2026-08-10.md
---

# Home Surfaces Dogfood Handoff — 2026-08-10

## Purpose

Prepare the Trips and Places home-surface explorations for an internal device
walk without presenting seeded or unavailable material as live truth.

## Code landed

- The app's `dogfood` EAS profile enables the existing internal gates for
  Trip Feel, Places Reading Spine, and Places Saved Unplaced. Near You and
  Today Mapped were already enabled there.
- `S19-mara-home-surface-state` is a deterministic dogfood scenario. It
  specifies Mara's grounded Open Loops state and private Places Register log.
- `GET /api/places/comparison` returns an authenticated, typed, content-free
  availability result. It remains dark because there is no published editorial
  pair with complete public provenance.

## Operator steps (not performed by source control)

1. Deploy the backend commits and run the normal OpenAPI/type synchronization
   after the workspace API-operation registry baseline is green.
2. On the dogfood backend, set only:

   ```text
   PLACES_REGISTERS_ENABLED=true
   PLACES_SAVED_UNPLACED_ENABLED=true
   ```

   These stay off in preview and production. `PLACES_TWO_PLACE_COMPARISON_ENABLED`
   must remain false; a flag does not create a truthful comparison.
3. Confirm the Clerk-linked Mara mapping against the exact dogfood backend,
   then seed/verify `S19-mara-home-surface-state` using the guarded dogfood
   tooling. Do not write directly to an external database.
4. Produce and install a fresh `dogfood` EAS binary. The feature gates are
   compile-time environment values, so an older installed binary cannot see
   them.
5. Run the physical device matrix: normal and large Dynamic Type, loading,
   offline cache/cold offline, failed image, location granted/denied/stale,
   map action/back navigation, and all configured door destinations.

## Truthful absences

- Near You requires a real foreground location reading and server receipt. It
  is not seeded.
- Saved Unplaced requires an owner save on an actual venue whose `place_id` is
  null. No such row is manufactured by the scenario.
- Reading Spine requires two already-published source-backed angle cards in
  one Places fork. The current dogfood manifest has no dossier/angle authoring
  field, so it correctly remains absent until that source exists.
- Comparison needs a public editorial owner for an ordered venue pair plus
  immutable public fact/provenance snapshots. The canonical design calls for
  two uncarded venue columns and a hairline, not a generic fact table; price
  table comparison belongs in Trips or Plans.

## Evidence boundary

Source tests, contract checks, and a simulator doctor establish readiness to
run the walk. They are not device acceptance. Capture and commit the normal
F/B/V receipts after the authenticated device walk.
