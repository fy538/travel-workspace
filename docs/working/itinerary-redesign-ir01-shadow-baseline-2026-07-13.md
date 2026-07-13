---
doc_type: working
status: active
owner: backend
created: 2026-07-13
last_verified: 2026-07-13
expires: 2026-08-12
why_new: Record the reproducible IR-01 lifecycle shadow baseline and read-flip decision.
supersedes: []
source_of_truth_for: [itinerary-redesign-ir01-shadow-baseline]
---

# Itinerary redesign IR-01 lifecycle shadow baseline

Date: 2026-07-13
Audit instant: `2026-07-13T18:45:00Z`
Decision: canonical lifecycle remains shadow-only; read flip is not eligible.

## Reproduction

From the `travel-agent--itinerary-foundation` worktree:

```bash
PYTHONPATH=. python scripts/audit_itinerary_lifecycle.py \
  --as-of 2026-07-13T18:45:00Z

PYTHONPATH=. python scripts/audit_itinerary_lifecycle.py \
  --all-local \
  --as-of 2026-07-13T18:45:00Z
```

The audit is read-only and aggregate-only. It emits no trip, user, title,
destination, or itinerary identifiers/content.

## Canonical dogfood cohort

The `@dogfood.local` cohort contained 13 distinct trips:

| Evidence | Result |
|---|---:|
| Evaluated | 13 / 13 |
| Canonical phases | planning 8; post-trip 5 |
| Terminal context | completed 5; cancelled 0 |
| Plan legacy agreement | 13 / 13 (100%) |
| Map legacy agreement | 13 / 13 (100%) |
| Projection errors | 0 |
| Unclassified disagreements | 0 |
| Destination with missing timezone | 6 |
| Invalid destination timezone | 0 |

This cohort is clean where it has evidence, but it is not representative. It
does not exercise ideation, final prep, live, cancelled, destination midnight,
or dogfood-date override through real read-model rows. Six trips have a
destination without an IANA timezone, so their explicit UTC fallback is not yet
good enough for a destination-calendar read flip.

## Broader local corpus

The mixed local seeded/test corpus contained 1,847 trips at audit time. It is
diagnostic rather than launch evidence because ordinary test runs can add rows.

| Evidence | Result |
|---|---:|
| Evaluated | 1,847 / 1,847 |
| Canonical phases | ideation 272; planning 802; final prep 18; live 361; post-trip 394 |
| Terminal context | completed 215; cancelled 0 |
| Plan legacy agreement | 1,717 / 1,847 (92.96%) |
| Map legacy agreement | 1,232 / 1,847 (66.70%) |
| Plan known disagreements | 130 legacy status short-circuits |
| Map known disagreements | 615 status/calendar drift cases |
| Projection errors | 0 |
| Unclassified disagreements | 0 |
| No destination | 1,706 |
| Destination with missing timezone | 57 |
| Invalid destination timezone | 0 |

Observed Plan transitions were `ideation -> pre_trip` (83), `ideation ->
during_trip` (17), and `ideation -> post_trip` (30). Observed Map transitions
were those same 130 plus `pre_trip -> during_trip` (336), `pre_trip ->
post_trip` (148), and `during_trip -> post_trip` (1). These are explained by
the existing Plan raw-status short circuit and Map status-only derivation. They
are evidence for consolidation, not canonical defects.

## Launch threshold

Before `ITINERARY_LIFECYCLE_V2` may change a Plan or Map response, the exact
cohort intended for the flip must satisfy all of the following in one audit:

- 100% of rows evaluate without projection failure;
- zero unclassified old/new disagreement;
- zero canonical Plan/Map disagreement for the same trip and audit instant;
- coverage includes ideation, planning, final prep, live, and post-trip;
- terminal coverage includes both completed and cancelled;
- zero destinations with a missing or invalid IANA timezone;
- destination-midnight, DST, UTC fallback, multi-city-primary, dogfood override,
  raw status/date disagreement, completed, and cancelled deterministic tests
  remain green.

Legacy agreement itself is not a launch threshold. Known disagreement is the
reason to replace the legacy derivations; each disagreement must instead be
classified and attributable to an accepted legacy rule.

## Remediation before re-audit

1. Add canonical dogfood trips for ideation, final prep, live, and cancelled.
2. Populate the missing destination timezone on the six current dogfood trips,
   or remove a destination association that is not actually valid.
3. Add at least one dogfood date-pin case and one destination-midnight case.
4. Run Plan State and Map State with the shadow flag enabled for that cohort.
5. Re-run the aggregate audit and inspect emitted mismatch reason counts before
   considering a read flip.

No fixture seeding or database mutation was performed as part of this audit.
