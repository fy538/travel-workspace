---
doc_type: current_status
status: active
owner: product-engineering
created: 2026-08-16
last_verified: 2026-09-23
why_new: Records the specific evidence used to resolve the expired API operation policy window; the policy JSON cannot carry that review narrative.
source_of_truth_for:
  - api-operation-policy-review-2026-08-16
---

# API operation policy review — 2026-08-16

The mobile OpenAPI projector correctly stopped on 2026-08-16 because 53
`retiring` entries had reached their 2026-08-15 review date. This was a policy
deadline, not evidence that any of those routes should be silently exposed.

## Review method

We compared every expired route against the current mobile transport and
product-call discovery using `scripts/api_contract_audit.py`'s
`discover_mobile_consumers` implementation. The review found:

- 3 routes have real product callers and are restored to `active` with their
  exact hook as the declared consumer: conversation invite list, create, and
  revoke.
- 50 routes have no discovered product caller. They remain `retiring`; their
  existing removal triggers remain unchanged and their next review is
  2026-09-15.

This is a control-plane correction only. It neither adds an API surface nor
changes deployment behavior. Each remaining retiring route still needs a
separate, evidence-backed remove-or-adopt decision at its next review.

## September 23 re-review — current integration candidate

This supersedes the August review counts, not its historical rationale. The
current full offline OpenAPI export has no diff. Method-specific discovery was
rerun against app `7e94c42a8` and backend `078d915cb`; all 55 expired retiring
operations still exist in that export. Of these, 34 have no discovered mobile
consumer, 20 have transport declarations only, and one (Discover feed) has an
exported hook without a screen caller. The latter was checked separately:
`useDiscoverSectionedFeed` occurs only at its definition, barrel export and tests.
It must not be promoted to active merely because the scanner sees the facade.

All 55 retain their audience, lifecycle, flags, consumer declarations and exact
removal triggers. They are explicitly retained through **October 7, 2026**,
not certified unused in deployment. Each policy reason now names the observed
source evidence. Removing backend endpoints without deployed-traffic evidence
would change compatibility on an unsupported assumption; no endpoint was
removed, activated or newly included in the app contract by this review.

The three expired compatibility entries were also inspected individually:
Discover's context-preserving Redirect, Atlas's default Life Redirect, and the
legacy map API wrapper. Current route helpers target Places/Life, but the
`useDiscoverMapPins → getDiscoverMap → /api/discover/map` facade remains in source.
All three keep their original retirement condition, with explicit evidence and
the same bounded October 7 review. No released-client or deep-link telemetry
was available in this checkout. This is a retention decision, not proof of
completed retirement or permission to activate legacy surfaces.

Command: `PYTHONPATH=scripts python3` importing
`api_contract_audit.load_policy` and `discover_mobile_consumers`, normalized by
HTTP method and path; source follow-up used `rg` for the hook, transport and
route-helper references. The inventory below records the actual result rather
than inferring adoption from generated types or an HTTP wrapper.

| Operation | Owner | Discovered mobile reference |
|---|---|---|
| `GET /api/trips/{trip_id}/location-sharing` | location-consent | None |
| `PUT /api/trips/{trip_id}/location-sharing` | location-consent | None |
| `GET /api/trips/{trip_id}/itinerary/cross-day-suggestions` | itinerary | None |
| `GET /api/angles/{angle_id}` | editorial | None |
| `DELETE /api/trips/{trip_id}/expenses/{expense_id}/comments/{comment_id}` | expenses | `app_transport: travel-app/utils/api/http.ts::deleteExpenseComment` |
| `GET /api/atlas/artifacts/{artifact_id}/stream` | atlas | None |
| `GET /api/atlas/places` | atlas | None |
| `GET /api/atlas/scan-history` | atlas | None |
| `GET /api/atlas/search` | atlas | None |
| `GET /api/conversations/{conversation_id}/messages/{message_id}/reactions` | conversations | None |
| `GET /api/discover/feed` | places | `app_source: travel-app/data/discover.ts::getDiscoverFeed`; `app_transport: travel-app/utils/api/http.ts::getDiscoverFeed` |
| `GET /api/discover/trending` | product-engineering | `app_transport: travel-app/utils/api/http.ts::getTrending` |
| `GET /api/dossiers/accommodation/{accommodation_id}` | product-engineering | None |
| `GET /api/dossiers/site/{site_id}` | product-engineering | None |
| `GET /api/dossiers/venue/{venue_id}` | product-engineering | None |
| `GET /api/takes/{take_id}` | product-engineering | None |
| `GET /api/trips/blank` | product-engineering | `app_transport: travel-app/utils/api/http.ts::getBlankTrip` |
| `GET /api/trips/{trip_id}/action-receipts/recent` | expenses | None |
| `GET /api/trips/{trip_id}/booking/affiliate-links/travel-insurance` | booking | None |
| `GET /api/trips/{trip_id}/booking/readiness` | booking | None |
| `GET /api/trips/{trip_id}/booking/sessions` | booking | `app_transport: travel-app/utils/api/http.ts::listBookingSessions` |
| `GET /api/trips/{trip_id}/cross-trip-threads` | product-engineering | `app_transport: travel-app/utils/api/http.ts::getCrossTripThreads` |
| `GET /api/trips/{trip_id}/invites/eligibility` | invites | `app_transport: travel-app/utils/api/http.ts::getInviteEligibility` |
| `GET /api/trips/{trip_id}/expenses/suggest-category` | expenses | None |
| `GET /api/trips/{trip_id}/expenses/{expense_id}` | expenses | `app_transport: travel-app/utils/api/http.ts::getExpense` |
| `GET /api/trips/{trip_id}/expenses/{expense_id}/comments` | expenses | None |
| `GET /api/trips/{trip_id}/geofence-events` | live-companion | None |
| `GET /api/trips/{trip_id}/itinerary/operations/history` | itinerary | None |
| `GET /api/trips/{trip_id}/itinerary/operations/writebacks` | itinerary | `app_transport: travel-app/utils/api/http.ts::listItineraryWritebacks` |
| `GET /api/trips/{trip_id}/memory-evidence` | memory | None |
| `GET /api/trips/{trip_id}/messages/history` | conversations | None |
| `GET /api/trips/{trip_id}/messages/info` | conversations | None |
| `GET /api/trips/{trip_id}/narration/manifest` | live-companion | `app_transport: travel-app/utils/api/http.ts::getNarrationManifest` |
| `GET /api/trips/{trip_id}/voice-guide/session` | live-companion | `app_transport: travel-app/utils/api/http.ts::getActiveVoiceGuideSession` |
| `GET /api/users/me/memory-evidence` | memory | None |
| `GET /api/users/{user_id}/devices` | product-engineering | None |
| `GET /api/users/{user_id}/facts/{fact_id}/history` | product-engineering | `app_transport: travel-app/utils/api/http.ts::getUserFactHistory` |
| `GET /api/users/{user_id}/followers` | product-engineering | `app_transport: travel-app/utils/api/http.ts::getFollowers` |
| `POST /api/conversations/{conversation_id}/location` | conversations | `app_transport: travel-app/utils/api/http.ts::pushLocation` |
| `POST /api/conversations/{conversation_id}/promote_to_trip` | conversations | None |
| `POST /api/lookup/` | product-engineering | None |
| `POST /api/places/{slug}/angles/request` | product-engineering | `app_transport: travel-app/utils/api/httpMemoryEndpoints.ts::requestAngle` |
| `POST /api/trips/{trip_id}/decommit` | product-engineering | `app_transport: travel-app/utils/api/httpExtendedEndpoints.ts::decommitTrip` |
| `POST /api/trips/{trip_id}/digest/email` | product-engineering | None |
| `POST /api/trips/{trip_id}/itinerary/operations/provider-sagas/{saga_id}/advance` | itinerary | None |
| `POST /api/trips/{trip_id}/itinerary/operations/writebacks` | itinerary | `app_transport: travel-app/utils/api/http.ts::createItineraryWriteback` |
| `POST /api/trips/{trip_id}/members` | product-engineering | `app_transport: travel-app/utils/api/http.ts::addTripMember` |
| `POST /api/trips/{trip_id}/messages` | conversations | None |
| `POST /api/trips/{trip_id}/messages/close` | conversations | None |
| `POST /api/trips/{trip_id}/messages/stream` | conversations | None |
| `POST /api/trips/{trip_id}/narration/prerender-hint/{entity_type}/{entity_id}` | live-companion | `app_transport: travel-app/utils/api/http.ts::prerenderHint` |
| `POST /api/trips/{trip_id}/photos` | product-engineering | None |
| `POST /api/users/{user_id}/heartbeat` | product-engineering | `app_transport: travel-app/utils/api/http.ts::postUserHeartbeat` |
| `POST /api/users/{user_id}/modality/route` | product-engineering | `app_transport: travel-app/utils/api/http.ts::routeModality` |
| `GET /api/sites/{site_id}` | places | None |
