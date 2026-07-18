---
doc_type: canon
status: active
owner: founder / engineering
created: 2026-07-18
last_verified: 2026-07-18
why_new: A grounded Reading has its own compose, steer, keep, provenance, and return lifecycle.
source_of_truth_for: [journey-J26]
---

# 26 — Atlas Reading to Steer, Keep, and Return

## Product Promise

A traveler can understand the evidence behind an interpretation, steer it, keep
it, and reliably find it again.

## Canonical User Story

As a traveler with enough accepted material, I want to shape a grounded Reading
without losing its sources, so that it becomes worth revisiting.

## Starting State and Surfaces

- Atlas has enough accepted evidence for a grounded Reading.
- Routes: `/atlas/compose`, `/atlas/readings`, `/atlas/readings/[id]`, artifact sources.
- Source contract: Atlas `J-A3`; J11 retains candidate review.

## Canonical Steps

1. Open an existing Reading or compose from eligible source material.
2. Read thesis, evidence, provenance, and thin-result honesty.
3. Steer the Reading while retaining the source contract.
4. Keep exactly once and return through shelf/Home.
5. Reopen the kept Reading with its query/evidence/corrections intact.

## Required Branches

| Branch | Path | Required evidence |
|---|---|---|
| `J26.B01` | Open existing grounded Reading | `FE`, `BE`, `VIS`, `LIVE` |
| `J26.B02` | Compose and progressive result | `FE`, `BE`, `VIS`, `LIVE` |
| `J26.B03` | Thin result remains an honest list | `FE`, `BE`, `VIS` |
| `J26.B04` | Generation failure/retry and offline cache | `FE`, `BE`, `VIS` |
| `J26.B05` | Steer retains provenance | `FE`, `BE`, `VIS`, `LIVE` |
| `J26.B06` | Keep idempotently and return/reopen | `FE`, `BE`, `VIS`, `LIVE` |
| `J26.B07` | Missing/deleted source degrades honestly | `FE`, `BE`, `VIS` |

## Must Never Happen

- Compose is offered to a truly empty traveler.
- A thesis lacks supporting evidence/provenance.
- Steering silently swaps the source contract.
- Keep duplicates or strands the Reading.

## First Automation Target

Promote `atlas-journey-reading-keep-return.yaml`, then add thin, failure/retry,
steer-provenance, and missing-source scenarios.
