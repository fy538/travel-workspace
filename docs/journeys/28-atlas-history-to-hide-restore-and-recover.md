---
doc_type: canon
status: active
owner: founder / engineering
created: 2026-07-18
last_verified: 2026-07-18
why_new: Mature Atlas history has a distinct browse, archive-reason, restore, and return lifecycle.
source_of_truth_for: [journey-J28]
---

# 28 — Atlas History to Hide, Restore, and Recover

## Product Promise

A traveler can browse the durable record by time or place, hide an entry,
understand why it is removed, and restore it to the right chapter.

## Canonical User Story

As a returning traveler, I want to manage a long travel record without losing
context or confusing system deduplication with my own decisions.

## Starting State and Surfaces

- Mature Atlas with multiple years/places and at least one restorable item.
- Routes: `/atlas/whole`, `/atlas/long-view`, `/atlas/removed`, artifact/memory detail.
- Source contract: Atlas `J-A5`; J17 owns cross-trip recall/timely return.

## Canonical Steps

1. Browse Long View by Time or Places.
2. Open an entry and rename, pin, or hide it.
3. Open Removed and inspect user/system archive reason.
4. Restore the item.
5. Return to the original year/place chapter with counts and pagination reconciled.

## Required Branches

| Branch | Path | Required evidence |
|---|---|---|
| `J28.B01` | Browse time and place dimensions | `FE`, `BE`, `VIS`, `LIVE` |
| `J28.B02` | Rename and pin persist | `FE`, `BE`, `VIS` |
| `J28.B03` | User hide records reason | `FE`, `BE`, `VIS`, `LIVE` |
| `J28.B04` | System/dedup archive remains distinguishable | `FE`, `BE`, `VIS` |
| `J28.B05` | Restore returns to original chapter | `FE`, `BE`, `VIS`, `LIVE` |
| `J28.B06` | Pagination/cache and failed restore recover | `FE`, `BE`, `VIS` |

## Must Never Happen

- A user-hidden item is auto-restored by dedup reconciliation.
- Restore loses its original time/place chapter.
- People/Theme render as active when deferred.
- Long View becomes a competing authored Home.

## First Automation Target

Promote `atlas-journey-archive-hide-restore.yaml` and pair it with the projection
dedup/restore canary, pagination, and failed-restore branches.
