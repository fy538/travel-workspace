---
doc_type: canon
status: active
owner: founder / engineering
created: 2026-07-18
last_verified: 2026-07-18
why_new: A place save can establish useful, honest personal context before a trip or strong learned claim exists.
source_of_truth_for: [journey-J25]
---

# 25 — Places First Save to Useful Personal Context

> Status: historical compatibility evidence; the active product loop is
> Places → Vesper → Places, not a separate Atlas destination.

## Product Promise

Places becomes useful from one grounded action without inventing a strong taste
claim or requiring a completed trip. Vesper may use the resulting explicit
save as governed context; You owns later inspection and correction.

## Canonical User Story

As a traveler with no saved Places, I want one low-pressure way to establish
real context, so the product becomes useful and honest immediately.

## Starting State and Surfaces

- No saved places or accepted memory required.
- Routes: Places, saved places, search, and optional, consented intake.
- J20 owns first-session consent; You owns later memory controls.

## Canonical Steps

1. Open Places without assumed location, taste, or memory.
2. Save a place, establish home/current-location context, approve recovery, or answer one concrete question.
3. See source attribution and no inflated “loved” claim.
4. Return to Places with the new save and, only where permitted, a weak prior
   available to Vesper.

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

- The product invents home context or strong preference.
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
