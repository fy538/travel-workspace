---
doc_type: working
status: active
owner: backend
created: 2026-07-13
last_verified: 2026-07-13
expires: 2026-08-12
why_new: Record deterministic IR-03 backfill rules and evidence from the mixed legacy corpus.
supersedes: []
source_of_truth_for: [itinerary-redesign-ir03-backfill-baseline]
---

# Itinerary redesign IR-03 backfill baseline

Recorded at `2026-07-13T19:24:49Z` against the local mixed corpus. The audit
was read-only and emitted aggregate counts only.

## Deterministic rules

- Every legacy block self-roots lineage at its own block ID and records
  `legacy_self_root` provenance.
- `participants = NULL` and an empty participant array mean whole group.
  Planned rows come from the current membership snapshot and are labeled
  `legacy_current_membership_snapshot`.
- One explicit participant means personal scope; two or more mean subgroup.
  Explicit participants establish planned inclusion only. They never establish
  decision ownership.
- All backfilled attendance intention is undecided. Legacy `planned`,
  `happened`, and `skipped` occurrence maps to `planned`, `happened`, and
  `did_not_happen`, labeled `legacy_block_event`.
- Decision owner remains null unless durable canonical evidence exists. The
  present corpus has no such evidence at block granularity.
- Legacy `locked` is projected as Review behavior, while the stored legacy
  value remains unchanged.
- A protected dependency is created only for the explicit provider states
  held, held-for-payment, confirmed/booked, paid, or cancelled. Changeability
  remains unknown unless separate provider terms prove otherwise.
- Overlapping timestamps never create branches.
- Legacy history is normalized only when source identity, subject identity,
  canonical operation semantics, and complete before/after identity are all
  provable. Existing plan events do not meet that bar and remain readable as
  legacy evidence.

## Aggregate dry-run

| Measure | Count |
|---|---:|
| Legacy blocks | 416 |
| Whole-group blocks | 386 |
| Personal blocks | 1 |
| Subgroup blocks | 29 |
| Projected participation rows | 758 |
| Missing explicit participant references | 0 |
| Ambiguous decision owners | 416 |
| Ambiguous booking-evidence objects | 52 |
| Booking objects safely normalized | 0 |
| Timestamp overlap pairs observed, not branched | 3 |
| Legacy history events retained | 661 |
| Legacy history events safely normalizable | 0 |

The shared database was not mutated.

## Disposable-database proof

A new local PostgreSQL database was upgraded from base through `ir03a001` and
seeded with null/one/many participants, planned/happened/skipped occurrence,
one confirmed booking, one ambiguous booking object, locked governance, and an
ambiguous legacy history event.

- First apply wrote 3 lineage rows, 3 scope rows, 5 participation rows, and 1
  protected dependency.
- The protected dependency retained `changeability = unknown`.
- A second apply wrote zero rows in every category.
- No branch or canonical operation was invented.
- Selected legacy block bytes were identical before and after both applies.
- Downgrade `ir03a001 -> ir02f001` preserved those legacy bytes.
- The disposable database was removed.

## Activation posture

The backfill command defaults to dry-run. Apply mode requires an exact database
name and refuses non-local hosts. No runtime reader or shared database has been
flipped; IR-03 remains a shadow/dual-read foundation until the policy adapter
and capability work can consume it safely.
