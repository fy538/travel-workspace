---
doc_type: contract
status: active
owner: founder / engineering
created: 2026-07-11
last_verified: 2026-07-15
expires: 2026-08-10
why_new: The simplification backlog identifies compatibility debt but does not own the individual migration contracts, expiry rules, or enforcement policy.
supersedes: []
source_of_truth_for: [cross-repo-compatibility-exceptions]
---

# Compatibility Ledger

This is the control layer for pre-launch standardization. It records every
runtime compatibility exception that is allowed to survive while the product
converges on its canonical architecture and design canon.

The machine-readable registry is
[`compatibility-ledger.json`](../governance/compatibility-ledger.json). This
document owns the policy; the registry owns the individual entries.

## Default posture

**Delete** is the default. Backward compatibility is allowed only for:

1. persisted user data;
2. distributed external links;
3. a coordinated deployed-version boundary; or
4. an intentional dark surface that is explicitly flag-owned.

Historical implementation convenience, old tests, mock fixtures, and an
earlier design direction are not sufficient reasons to retain a compatibility
path.

## Required entry contract

Every exception has:

- a stable `id` used in code comments as `compatibility_id: <id>` when new
  compatibility logic is introduced;
- a status (`active` or `retiring`);
- one allowed reason;
- a named owner;
- its canonical replacement;
- exact code/data paths;
- an observable removal trigger; and
- an expiry date.

`retiring` means the canonical path exists and migration work is expected.
`active` is reserved for real persisted-data or external-link protection.

## Enforcement

`python3 scripts/check_compatibility_ledger.py` validates that every ledger
entry is complete, its tracked paths exist, and each declared marker still
appears in the named path. It runs through `make docs-check`.

The check deliberately does not treat every use of the word "legacy" as a
failure: generated API descriptions, historical comments, and non-runtime
documentation would create noise. Instead, new compatibility behavior must
declare a ledger id in the code review and be added to the registry first.

## Deletion protocol

When an entry's trigger is met:

1. migrate all consumers to the listed canonical replacement;
2. delete the branch, alias, adapter, overload, fixture, and tests that exist
   solely for the old path in the same change;
3. run the entry's relevant contract, logic, and visual evidence;
4. remove the registry entry and archive its decision in the simplification
   audit if the removal changed a cross-repo contract.

Do not leave a dead entry as a historical checklist. Git history is the record
of completed compatibility removals.

## Current queue

There are no active compatibility exceptions. Phase 11 materialized every
persona's authored day seeds into canonical `TripPlanState` at the registry
boundary, removed Mock API reads of persona itinerary rows, and renamed the
plan-to-day presentation selector. Scenario personas now each name their QA
recipe, so they are bounded test substrate rather than alternate product
identities.

The Atlas route-alias exception is now retired. Its redirect-only route files,
marker document, and registry entry were deleted together after the canonical
Atlas routes became the only supported pre-launch surface.

The deprecated place-media helper, unused token-link helper, no-op composer
prop, and duplicate Maestro script aliases were removed in Phase 2; they are
not compatibility exceptions and therefore do not remain in the ledger.

Phase 4 replaced the option-dependent data-hook overloads with explicit list,
value, snapshot, and query hooks. The overload exception was removed with its
call sites and tests.

Phase 7 removed the `group_state` home-card alias from backend tier policy,
cross-trip presentation, the OpenAPI contract, and the app's card union. The
three explicit invite archetypes are now the only supported wire contract.

Phase 8 removed the group chat's trip-scoped non-streaming send. A send now
uses conversation-scoped SSE exclusively; an unresolved conversation is an
explicit, retryable connection failure rather than a silent transport change.

Phase 9 deleted the unused Atlas redirect-only routes for Almanac, Timeline,
Map, and Following. Long View and Companions are the only supported paths.

Phase 10 removed two false migration paths: the unused install-scoped
SecureStore copier and the invite token's bare-string compatibility wording.
Scoped preferences remain isolated, while malformed invite storage is cleared
as invalid data before it can resume an auth flow.
