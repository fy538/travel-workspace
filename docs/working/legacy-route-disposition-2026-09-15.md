---
doc_type: working
status: active
owner: product-engineering / API owners
created: 2026-09-15
expires: 2026-10-15
why_new: Records a bounded three-route retirement execution audit, including hidden producer and retained-data obligations not resolved by the existing broad service-consolidation investigation.
supersedes: []
source_of_truth_for: []
---

# Three legacy routes — disposition audit

This is an execution receipt, not retirement authorization or a new API policy.
It separates a directly mounted product consumer, a client transport facade,
backend callers of the same handler, and producers used by other routes. The
current API lifecycle authority remains
[`api-operation-policy.json`](../governance/api-operation-policy.json).

## Checkout and evidence boundary

Isolated lane `codex/legacy-route-disposition-2026-09-15` was created from
workspace `3465b83`, backend `1637b9fd4`, and mobile `fe1de89ac` on
2026-09-15. The concurrent receiving-completion checkout and its uncommitted
service-consolidation investigation were not changed. This audit uses repository
search, route and call-graph inspection, the committed OpenAPI/policy snapshot,
and the local API contract audit. It does **not** establish production traffic,
older supported-client usage, provider obligations, or native behavior.

`python3 scripts/api_contract_audit.py --list-transport-only` passed and
reported 582 active, 15 dark, and 62 retiring operations. The list is a
transport inventory, not a mounted-screen or traffic census. The direct
Discover and Concierge transports are present behind facades, so their absence
from that list is not evidence of use.

Read-only deployment inspection is unavailable in this environment:
`flyctl auth whoami --json` returned `no access token available`. A connector
search did not expose an exact Fly.io connection. No zero-traffic inference is
made from this failure.

## Route-by-route disposition

| Operation | Current repository evidence | Disposition before deletion |
| --- | --- | --- |
| `GET /api/discover/feed` | Policy says `retiring`, with no named current consumer. `useDiscoverSectionedFeed` and `api.getDiscoverFeed` remain exported but repository search found no mounted product caller; the hidden Discover tab redirects to Places. The dev cold-start cover does not call this hook. `useDiscoverFeeds` on legacy Trips Home is a different For You/social/collections path. | Keep route and facade pending supported-client **and** deployed traffic evidence. If both are zero, remove the feed-specific route, facade, mock, and compose implementation as one reviewed cross-repo cutover; do not delete the whole Discover package. |
| `POST /api/lookup/` | Policy says `retiring`, with no consumer or flag. No mobile API facade or mounted caller was found; the backend route is the direct caller of `backend.lookup_agent.agent.lookup`. | Keep pending deployed traffic evidence or a separately approved flag/journey. If traffic is zero, route removal is plausible, but the lookup package/cache and derived-artifact registry need a separate retained-data disposition. |
| `GET /api/concierge/home` | Full/app OpenAPI and `api.getConciergeHomeFeed`/`useConciergeHomeFeed` remain; search found no mounted direct product caller beyond tests. Unlike the first two, there is no explicit policy entry for this exact operation, so it inherits the default active app classification. The backend `GET /api/concierge/home/trips-stack` calls `get_concierge_home_feed()` internally. | Do **not** classify this as already retiring or remove it yet. First resolve owner policy and supported-client/deployed traffic; then factor the Trips-stack internal call away from the route handler while preserving its ambient/weather/location/degraded behavior. Keep the shared Concierge producer. |

## Hidden consumers and data obligations

- `backend.discover.compose` is used by the feed route and the five-pack
  dogfood verifier. `backend.discover.personalization_cache` is invalidated
  from the user-event route and memory subscriber; Discover metrics serve an
  API metrics route. Discover map/trending routes and Places projection tests
  also depend on the package. Feed-route retirement cannot be treated as
  package retirement without migrating or retiring these specific callers.
- The Concierge Home producer `assemble_concierge_home_feed` is the default
  loader for the active Vesper workbench and is called by ambient dispatch.
  Trips-stack calls the direct handler for the richer weather/location feed.
  Models and ranking also have notification, posture, and Trips-stack callers.
  A dead direct mobile screen does not make this producer dead.
- `lookup_cache` is registered as a Qdrant derived artifact with no canonical
  source, cache-only rebuild, and logical read-time TTL. Collection creation,
  version routing, embedding migration, and cache tests refer to it. Before
  deleting the lookup package, decide whether to discard this disposable
  collection, migrate any required readers, and retire its registry/checker
  entry. A TTL at read time does not by itself prove physical deletion.

## Required next evidence and cutover order

1. Obtain a read-only production operation-traffic window for each exact
   method/path, with client/version breakdown and an owner-defined observation
   interval covering supported older clients. Record the source and window;
   static search or a zero in one local fixture is not a substitute.
2. Resolve the active-versus-retiring policy for the direct Concierge Home
   operation with its owner. Confirm replacement parity and older-client/deep
   link obligations for all three routes; preserve current Trips stack and
   Chat workbench independently.
3. If a route meets its policy removal trigger, implement a small route-level
   cutover first, update full and app OpenAPI plus generated mobile types via
   `./scripts/sync-types.sh`, and run `make api-coverage-check`, focused backend
   and mobile tests, and the coordinated verification gate. Delete a producer
   or cache only after its own caller and retained-data review.

No route, producer, cache, feature flag, deployment setting, or product policy
was changed by this audit.

## Local verification

- `make api-coverage-check`: passed (582 active, 15 dark, 62 retiring).
- `make docs-inventory-check`: passed (606 classified workspace Markdown files).
- `make docs-check`: passed after `make docs-status-sync` refreshed the derived
  document count from 605 to 606. The initial run failed only on that derived
  count; it was not treated as a pass.
- `git diff --check`: passed. Backend/mobile tests and `make verify` were not
  run because no product source or wire contract changed; deployed traffic and
  native evidence remain unverified.
