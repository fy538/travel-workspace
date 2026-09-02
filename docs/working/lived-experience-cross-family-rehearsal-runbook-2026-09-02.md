---
doc_type: working
status: active
owner: founder / engineering
created: 2026-09-02
last_verified: 2026-09-02
expires: 2026-10-02
why_new: Operationalizes the revision-pinned, two-account, three-family Home/Places system rehearsal without converting local fixtures or automated tests into release evidence.
supersedes: []
source_of_truth_for:
  - lived-experience cross-family rehearsal procedure
depends_on:
  - vesper-product-system-build-program-2026-09-01.md
  - ../systems/contribution-and-consequence.md
---

# Lived-Experience Cross-Family Rehearsal Runbook

## Purpose and claim boundary

This run proves that one deployed Vesper candidate can carry a person from
evidence and owner truth through judgment, Home or Places presentation,
server-issued authority, canonical consequence, readback, repair, multiplayer
invalidation, continuity, degraded behavior, and rollback.

It is intentionally broader than a behavior-loop demo. The same two accounts
exercise three different owner shapes:

| Family | Social shape | Root obligation | Canonical owner |
| --- | --- | --- | --- |
| `encounter_confirmation` | private personal occurrence | Places | occurrence reconciliation |
| `shared_plan_repair` | shared Plan with roster epoch | Home | itinerary proposal and Plan |
| `addressed_place_handoff` | sender-to-one-person contribution | Home and Places | relationship handoff with Intake Source custody |

Provisioning is not evidence that any consequence worked. A simulator is not a
physical device. An automated test cannot satisfy a device-required probe. A
local fixture cannot be relabeled dogfood. Passing one family does not release
another. The machine audit owns those rulings.

## Candidate freeze

Select one clean backend revision and one clean app revision. Deploy exactly
those revisions and retain their 7–40 character lowercase Git SHAs. Do not
collect evidence while either repository is dirty or while a deployment is
floating between revisions.

Required runtime controls are narrow and additive:

```text
GIT_SHA=<exact deployed backend SHA>
LIVED_EXPERIENCE_GOVERNED_REHEARSAL_ENABLED=true
LIVED_EXPERIENCE_GOVERNED_REHEARSAL_BACKEND_REVISION=<same backend SHA>
LIVED_EXPERIENCE_GOVERNED_REHEARSAL_USER_IDS=<primary UUID>,<secondary UUID>
LIVED_EXPERIENCE_GOVERNED_REHEARSAL_FAMILIES=encounter_confirmation,shared_plan_repair,addressed_place_handoff
LIVED_EXPERIENCE_CONSEQUENCE_RESOLUTION_ENABLED=true
```

Keep the existing signing, projection, exposure, producer-ingress, and selected
family-producer configuration revision-controlled in the deployment. Do not
paste signing values into an evidence artifact. Rehearsal access does not make
an unregistered or unbound owner executable, and removing any cohort coordinate
must immediately withhold the control and reject dispatch.

## Accounts and devices

Prepare two real signed-in accounts with stable opaque evidence references,
for example `acct:founder-primary` and `acct:friend-secondary`. Record their
actual backend user UUIDs privately for provisioning. Use at least one physical
device; use two when validating recipient projection and simultaneous
multiplayer state. Device references in evidence should be opaque and stable,
not serial numbers or personal device names.

Verify before mutation:

1. both UUIDs exist in the deployed database;
2. both clients report the frozen app revision;
3. the backend reports the frozen `GIT_SHA`;
4. Home and Places resolve the coherent governed-rehearsal shell posture;
5. Chat and Life UI remain on their current product lanes; and
6. logs and screen capture exclude private Source prose and credentials.

## Provision the canonical cohort

From the clean backend repository, preflight first:

```bash
PYTHONPATH=. .venv/bin/python scripts/provision_lived_experience_rehearsal.py \
  --run-id dogfood-YYYY-MM-DD-a \
  --environment dogfood \
  --real-accounts \
  --primary-user-id <primary-user-uuid> \
  --secondary-user-id <secondary-user-uuid> \
  --primary-account-ref acct:<opaque-primary> \
  --secondary-account-ref acct:<opaque-secondary> \
  --output <private-manifest-path>
```

Confirm `actor_cohort_ready: true`, the intended revisions, and no blocker.
Then add `--apply`. The command creates owner truth and pending openings but
does not press a control or create release evidence. Store the manifest outside
the repository. Re-run the exact command once and compare the files; the second
manifest must be byte-identical.

Evaluate the complete authority-to-treatment path before opening a client:

```bash
PYTHONPATH=. .venv/bin/python scripts/run_lived_experience_shadow_rehearsal.py \
  --manifest <private-manifest-path> \
  --output <private-shadow-report-path>
```

This first command is read-only for pending workflows. Review the three
actions, owned treatments, revisions, and blockers, then add `--apply` to
persist the shadow arcs. Run it once more without `--apply`; completed workflow
and arc readback must still pass. The report is local or environment
integration evidence only. It does not dispatch a consequence, satisfy a
physical-device probe, or promote a family.

The manifest is the coordinate source for later capture. Do not infer workflow,
family, owner, scope, target, revision, or Source identity from a screenshot.

## Global preflight

Run the source-addressability audit against the rehearsal environment:

```bash
PYTHONPATH=. .venv/bin/python scripts/audit_xgraph23_rollout.py
```

The contribution ledger must exist and active anonymous `mark_happened`
affinity rows must be zero. Missing migration or ambiguous active legacy
meaning stops the run; do not probabilistically backfill identity.

Generate a fresh evidence skeleton:

```bash
PYTHONPATH=. .venv/bin/python scripts/audit_lived_experience_release.py \
  --template > <private-evidence-path>
```

Replace placeholders only with observed references. Preserve pending status for
anything not yet exercised.

## Family run order

Run the least socially expansive family first, then the shared Plan, then the
addressed handoff. This does not make them independent slices; it limits damage
while the same system seams are exercised repeatedly.

### 1. Encounter confirmation

1. Open Places as the primary account and capture the exact control presented
   for the manifest opening.
2. Confirm the encounter once.
3. Verify the canonical occurrence readback, dependent Places refresh, causal
   terminal, and treatment `acted` only after verified readback.
4. Retry the same opaque grant and verify no second occurrence write.
5. Relaunch the app and recover the same terminal from owner truth.
6. Use the issued repair grant, verify the canonical personal correction, and
   confirm the original occurrence-derived Place meaning retracts without
   deleting independent evidence.

### 2. Shared Plan repair

1. Open Home as the primary account and capture the exact Plan-repair control.
2. Apply the proposal once and verify the canonical itinerary operation,
   proposal terminal, Plan revision, Home refresh, and multiplayer roster
   scope.
3. Verify the secondary account observes only viewer-correct shared truth.
4. Replay the grant and relaunch both clients; no second Plan operation may
   appear.
5. Exercise Undo, verify the inverse itinerary operation through owner
   readback, and confirm Home/Plan/world projections invalidate together.

### 3. Addressed Place handoff

1. Capture the sender-visible control on its one selected owner surface without
   exposing private message text in telemetry. Record suppressed alternatives;
   do not duplicate the control merely to satisfy both downstream root
   obligations.
2. Send once and verify one canonical relationship handoff and one pair-room
   message owned by the sender-authored prepared command.
3. Verify the recipient projection on the secondary account and the resulting
   viewer-correct Home and Places refreshes; do not infer a group Occasion or
   public distribution.
4. Replay and relaunch; no duplicate message or handoff may appear.
5. In a separately provisioned pending command, revoke or delete the exact
   Intake Source and verify dispatch becomes terminally unavailable and every
   visible Source-bound handoff retracts.
6. Confirm an already executed command remains historical receipt evidence,
   while current visibility follows custody and a separately authorized
   recipient-created Occasion remains independently owned.

## Mandatory negative and degraded probes

Exercise these against the same frozen candidate and record the expected
content-free terminal:

- grant replay after successful resolution;
- stale owner revision;
- membership-epoch change before shared dispatch;
- Source revocation before addressed dispatch;
- removal of the user or family from governed-rehearsal access after a control
  is displayed but before it is pressed;
- owner readback unavailable, rejected, or conflicting after dispatch;
- app process death before response and after verified consequence;
- backend restart between presentation and dispatch, and between dispatch and
  retry;
- coherent shell rollback to compatibility posture; and
- an older client receiving a terminal it cannot render richly.

An error toast alone is insufficient. Verify canonical owner state and the
absence of an unauthorized or duplicate write.

## Evidence and audit

For each required probe, record:

- passed, failed, or pending;
- device or automated evidence kind as required by the schema;
- stable evidence reference;
- observation time;
- participating opaque account references;
- physical device reference when required; and
- the exact backend/app revisions already present in the fixture manifest.

Keep screenshots, logs, and videos in private storage. The JSON artifact holds
references, not private content. Run:

```bash
PYTHONPATH=. .venv/bin/python scripts/audit_lived_experience_release.py \
  --evidence <private-evidence-path>
```

A nonzero exit is a product result: read the global and per-family blockers and
repair the shared system seam that caused them. Do not edit a pending or failed
probe to passed without new observation.

## Promotion and rollback

Only a passing, revision-matched audit permits a reviewed family-policy change.
Promotion remains per family even though the rehearsal is cross-family. Keep
the governed cohort available until the release posture is independently
verified, then remove the rehearsal enable and cohort configuration.

Rollback must be possible by configuration without deleting canonical owner
truth: withhold new controls, retain verified receipts and current readback,
keep repair paths for already completed consequences, and return Home/Places to
the coherent compatibility posture. Chat and Life UI do not move as part of
this runbook.
