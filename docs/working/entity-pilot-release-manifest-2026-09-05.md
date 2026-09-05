---
title: Entity pilot release manifest
date: 2026-09-05
doc_type: working
status: active
owner: product / backend / mobile
scope: internal-only-no-backfill
expires: 2026-10-05
created: 2026-09-05
why_new: "Prepares an owner-reviewable entity pilot manifest without enabling capabilities or writing data."
---

# Entity pilot release manifest

This is the review packet for a possible bounded internal object-page pilot.
It is intentionally not an enablement record: no flag, scheduler, provider
call, research job, catalog write, or backfill is authorized by this document.

## Current source revisions

| Surface | Revision | Evidence |
| --- | --- | --- |
| Backend (`travel-agent`) | `e6bf7a75f` | Entity presentation/research gating, queue safety, terminal-plan repair, read-only health report |
| Mobile (`travel-app`) | `9d2224ec7` | Shared object routes, identity-scoped actions, mock state harness, native matrix slice |
| Workspace docs | `8073187` | Roadmap, runbook, native receipt, execution log and this manifest |

These are local `main` revisions, not deployed build identifiers. A pilot
cannot start until the deployed artifact SHAs/build numbers are recorded and
match the reviewed source.

## Capability posture

| Capability | Current posture | Pilot disposition |
| --- | --- | --- |
| Rebuilt venue/site/experience page | Internal flag off by default | Keep off until full flag-on native matrix and owner review |
| Research request admission | Off; no scheduler | Keep off pending artifact canary, budget owner and health disposition |
| Addressed relationship handoff | Off | Keep off pending two-account privacy/revocation device proof |
| Catalog/entity backfill | Not run | Not part of this pilot |
| Provider refresh/booking | Not run | Not part of this pilot |

## Evidence available now

- Deterministic mobile selection: **102 tests**; TypeScript,
  test-contract TypeScript, API-boundary, schema-bridge and accessibility
  governance checks pass.
- Backend presentation/research/relationship selection: **46 tests** in the
  current runbook receipt; the complete entity-focused backend selection is
  **221 tests with 10 recorded skips**.
- iPhone 16 Pro mock native matrix slice: **12 steps**, covering compatibility
  loading geometry, retryable read error, malformed-link unavailable state and
  offline save gating. Direct site/experience forced-read and named research
  faults are covered by focused hook tests.
- Existing flag-on renderer and local-real-backend read receipts remain
  bounded identity/verb evidence only; they are not full release acceptance.
- Health snapshot (`2026-09-05T02:50:05Z`) is content-free: zero stale claims,
  duplicate-active jobs, expired leases, retried rows or
  completed-without-fresh-brief mismatches; one old pending venue research row
  and one pending resolution review remain untouched.

## Required owner decisions before any enablement

1. Name the operational owner and backup for entity reads, research queue,
   relationship repair and rollback.
2. Resolve the pending venue research row and pending resolution review by
   their existing owner paths; do not delete or silently retry them.
3. Record deployed backend/mobile build identifiers and the explicitly opted-in
   account classes/entity sample. No private prose or identifiers belong in
   this manifest.
4. Set measurable latency, queue-age, retry/error, duplicate-active and cost
   thresholds from a pre-pilot baseline. A missing budget/telemetry decision is
   a blocker, not an implicit zero.
5. Attach the full flag-on venue/site/experience state matrix: real-backend
   auth diversity, write/readback and repair, sparse/unavailable/photo/offline
   and process-restart states, VoiceOver, Android/platform verdict, and the
   research lifecycle if research is enabled.
6. Rehearse configuration-first rollback: disable admission and cohort,
   stop workers without deleting rows, preserve readable dated briefs, export
   receipts, and re-run the focused contract suites.

## Hard stop conditions

Any private-outcome or requester-identity disclosure, wrong-person
relationship state, false current claim, duplicate active paid request,
uncorrectable projection, or completed queue row without a readable artifact
stops the pilot. UI rollback does not repair canonical identity or delete
history; those require the owning repair path and a new review.

## Approval record

- Product owner: **pending**
- Backend/operations owner: **pending**
- Mobile/accessibility owner: **pending**
- Thresholds and cost ceiling: **pending**
- Deployed build identifiers: **pending**
- Pilot decision: **not approved**

Until every approval field is resolved and the remaining native gates are
attached, this manifest remains a preparation artifact. It does not authorize
flags, scheduled work, provider access, research spend, or backfill.
