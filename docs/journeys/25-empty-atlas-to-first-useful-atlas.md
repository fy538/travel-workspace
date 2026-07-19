---
doc_type: canon
status: active
owner: founder / engineering
created: 2026-07-18
last_verified: 2026-07-18
why_new: Atlas has a distinct activation journey before trips or strong learned claims exist.
source_of_truth_for: [journey-J25]
---

# 25 — Empty Atlas to First Useful Atlas

## Product Promise

Atlas becomes useful from one grounded action without inventing a strong taste
claim or requiring a completed trip.

## Canonical User Story

As a traveler with an empty Atlas, I want one low-pressure way to establish real
context, so that Atlas starts useful and honest.

## Starting State and Surfaces

- Stage 0/provisional Atlas; no accepted memory required.
- Routes: Atlas Home, saved places, search, optional scan/intake.
- Source contract: Atlas `J-A1`; J20 owns first-session consent.

## Canonical Steps

1. Open an honest empty/provisional Atlas.
2. Save a place, establish home/current-location context, approve recovery, or answer one concrete question.
3. See source attribution and no inflated “loved” claim.
4. Return to Home with the new place/weak prior in the correct layer.

## Required Branches

| Branch | Path | Required evidence |
|---|---|---|
| `J25.B01` | Search and save one place | `FE`, `BE`, `VIS`, `LIVE` |
| `J25.B02` | Optional concrete answer creates weak prior | `FE`, `BE`, `VIS` |
| `J25.B03` | Permission denial leaves another value path | `FE`, `VIS` |
| `J25.B04` | No result/save failure recovers honestly | `FE`, `VIS` |
| `J25.B05` | Prompt dismissal retires exactly once | `FE`, `BE`, `VIS` |
| `J25.B06` | Offline cached Home preserves grounded state | `FE`, `VIS` |

## Must Never Happen

- Atlas invents home context or strong preference.
- Photo recovery uploads before approval.
- Multiple activation prompts compete simultaneously.
- Empty Compose/Long View is offered as if meaningful.

## Certification Evidence

- The canonical `journey-25-mock-walk.smoke.test.tsx` proves save rollback, the grounded first save,
  weak optional answers, and exactly-once prompt retirement.
- The J25 Maestro flow covers permission denial, no-result recovery, save
  failure, a provisional venue read, successful activation, dismissal, and an
  offline return to the grounded Home state.
- Postgres scenarios and the lived disposable-persona cert prove that one real
  venue save projects into Atlas without fabricating a DNA claim.
- Device certification also caught and fixed a sparse-profile leak where a new
  traveler inherited strong-fit copy and named-persona evidence.
