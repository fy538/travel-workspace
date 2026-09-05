---
title: Entity object-page pilot runbook
date: 2026-09-04
created: 2026-09-04
doc_type: runbook
owner: Feihuyan
why_new: "Operational enablement and rollback steps for the entity object-page canary."
status: active
last_verified: 2026-09-05
scope: internal-only, no backfill
---

# Entity object-page pilot runbook

This runbook is the operational companion to
[`entity-roadmap-2026-09-04.md`](./entity-roadmap-2026-09-04.md). It describes
how to exercise the existing entity page, relationship projection, and
explicit research request canary. It does not authorize catalog enrichment,
identity backfill, scheduled research, or production rollout.

## 1. Default posture

The safe default is all capability flags off:

- `ENTITY_RESEARCH_REQUESTS_ENABLED=false` (or unset)
- `ENTITY_RESEARCH_REQUESTS_EMAIL_SUFFIX` and `ENTITY_RESEARCH_REQUESTS_USER_IDS` unset
- `RELATIONSHIP_UUID_HANDOFFS_ENABLED=false` unless the handoff lane has its own receipt
- no research queue scheduler or backfill command enabled

With research disabled, object reads remain sparse and read-only. A `GET`
must never enqueue work. Owner-provisional shells and experiences remain
ineligible for the research canary.

## 2. Preflight checklist

Run from the workspace root and record the exact child-repository SHAs:

```bash
make doctor
make contract-check
make test-backend
make typecheck
make test-frontend
```

For a focused entity receipt, also run:

```bash
cd travel-agent
PYTHONPATH=. pytest \
  tests/api/test_entity_research_requests.py \
  tests/research_agent/test_research_queue.py \
  tests/places/test_relationships.py \
  tests/places/test_entity_relationship_reads.py -q
cd ../travel-app
npm test -- --runInBand \
  __tests__/components/places/objectPageProjection.test.ts \
  __tests__/components/places/ObjectPageRebuild.test.tsx \
  __tests__/data/entityResearchRequest.test.tsx \
  __tests__/hooks/useSaveEntity.test.ts \
  __tests__/screens/venue-detail.smoke.test.tsx \
  __tests__/screens/experience-detail.smoke.test.tsx
```

For a content-free operational snapshot (read-only; no repair or refresh),
run:

```bash
cd travel-agent
PYTHONPATH=. .venv/bin/python scripts/entity_health_report.py
cd ..
```

The PostgreSQL continuity test is required evidence for relationship changes.
Mocks or SQLite-only tests do not substitute for it. Native simulator/device
evidence is a separate gate and must be attached before calling a surface
accepted.

The venue object-page, explicit placement smoke, and guarded venue/site/
experience renderer slices have a scoped current-build receipt at
[`entity-native-qa-receipt-2026-09-04.md`](./entity-native-qa-receipt-2026-09-04.md).
It proves mock-lane identity/save/private-handoff and one canonical placement
path, plus the guarded shared-renderer Keep/Ask contract for all three current
object kinds; it does not replace real-backend, accessibility, platform, or
full state-matrix evidence.

For the existing mock Maestro lane, the installed development client must be
connected to the current Metro bundle and its persisted runtime mode must be
compatible with the journey metadata. Start Expo on a LAN host when the client
cannot reach loopback, and clear/reset any stale `dev.mockModeOverride=false`
before a mock journey. A sign-in screen or the guarded “Couldn’t open your
account” state is a QA-lane configuration failure; it is not native entity
acceptance and must be recorded as such.

## 3. Canary enablement

Enable only for an explicitly opted-in internal account. The backend feature
flag and cohort gate must both be true. Keep the global daily research cap and
global processing lease at their defaults unless an owner records a different
budget before the run:

- six deep requests per user per hour
- fifty deep requests per day across the canary
- four concurrently processing queue items across workers
- thirty-day brief freshness TTL unless an experiment records another value

Use one known venue, one known site, and one known accommodation. Do not use
experience or owner-provisional entities in this canary. Do not create seed
rows merely to make the page look populated.

## 4. Required journeys

For each entity kind, capture the request id and outcome of these journeys:

1. Open the object page. Confirm no research request is sent.
2. Tap `Read up` once. Confirm a `queued` receipt and one queue row.
3. Leave and remount the page. Confirm status polling resumes without a new request.
4. Complete the worker with a page-readable brief. Confirm the status becomes `ready` and the queued copy disappears.
5. Force a stale brief in a disposable environment. Confirm old text remains visible, is dated, and the page offers an explicit refresh.
6. Simulate a missing artifact or quality hold. Confirm the queue is not marked complete and the page reports an honest failure/unavailable state.
7. Retry a terminal failure. Confirm a new idempotency key/attempt and no duplicate active job.
8. Exercise two accounts on the same canonical entity. Confirm relationship facts and private outcomes differ by viewer while shared identity/occurrence remains equal.

## 5. Monitoring and stop conditions

Inspect queue and application telemetry for:

- active jobs per canonical entity and globally
- request-to-readable-brief latency
- completed rows without a matching fresh brief (must be zero)
- duplicate active jobs (must be zero)
- failed/quality-held jobs and retry rate
- rate-limit or budget-store failures
- source URL validation failures and uncited briefs
- cross-account relationship/privacy failures (any one is a stop-ship issue)

The `research_health` object in the entity health report is the bounded
baseline for pending age, retries, expired leases, duplicate active jobs, and
completed rows without a current page-readable brief. Thresholds still need
to be set by the pilot owner before enablement; the report itself does not
declare a healthy rollout.

Stop the canary immediately on a private outcome or requester identity leak,
a `GET` that mutates the queue, duplicate provider work, a completed queue row
without a readable artifact, or an unbounded/fail-open paid request path.

## 6. Rollback

Rollback is configuration-first and reversible:

1. Set `ENTITY_RESEARCH_REQUESTS_ENABLED=false` and remove the cohort values.
2. Stop the research queue scheduler/worker invocation; do not delete queue or brief rows.
3. Keep existing readable briefs available as dated content; do not backfill or rewrite them during rollback.
4. Export the queue/status/error receipt and the affected entity refs for review.
5. If a source or privacy defect is found, retire only the affected artifact through its canonical repair path; preserve the audit row.
6. Re-run `make contract-check`, focused backend tests, and the app state tests before any re-enable decision.

Rollback is not a substitute for correcting canonical identity, ownership, or
source provenance. Those fixes require a reviewed code change and a new
two-account proof.

## 7. Release receipt

The owner records:

- backend and mobile commit SHAs
- exact flags, cohort and budget values
- entity refs and account classes used (never private prose)
- commands and test results
- queue/request/status receipts and inspected source mappings
- native QA captures and accessibility verdict, if the surface was enabled
- unresolved gaps and the precise rollback trigger

Until this receipt exists and all enabled capability gates pass, the entity
system remains an internal canary and no backfill is scheduled.
