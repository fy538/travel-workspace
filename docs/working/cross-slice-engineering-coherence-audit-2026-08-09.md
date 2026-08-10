---
doc_type: working
status: active
owner: engineering / product
created: 2026-08-09
expires: 2026-09-08
why_new: Records the post-consolidation, revision-anchored audit of engineering coherence and polish across Map, Places, Trips Home, AI, time, location, multiplayer, booking, expenses, and release evidence.
source_of_truth_for:
  - cross-slice-engineering-coherence-audit-2026-08-09
---

# Cross-slice engineering coherence audit

## Executive verdict

The repositories have made substantial architectural progress. The canonical
itinerary, API contracts, entity identity, multiplayer authorization, and
authenticated interactive map now form a credible shared foundation. Recent
Trips Home and Places consolidation also moved significant behavior out of
screen-local rendering into typed server projections, pure presentation models,
render plans, and explicit integrity guards.

The system is not yet fully coherent as one product. The most consequential
remaining seams are no longer missing foundations; they are alternate consumers
that reconstruct, cache, or hand off the same truth differently:

1. the authenticated map, AI spatial context, AI route cards, editorial map,
   and public map share do not use one authoritative map assembly boundary;
2. a map viewport can visually trigger an area-specific Vesper handoff without
   sending the selected area;
3. save and itinerary mutations do not invalidate every active Places feed that
   derives from the changed truth;
4. current executable journey evidence has advanced beyond the committed
   release-status projection;
5. receipt-upload idempotency is weaker than the real-money trust-loop promise;
6. broad mobile architecture, type, dependency, and visual-governance gates
   remain red even while focused seam suites are green.

This is a dated working audit, not a release claim and not a replacement for:

- `travel-agent/docs/product/Product Thesis.md`;
- `travel-agent/docs/product/Product Model.md`;
- `docs/release/v1-scope.md`;
- `docs/status/current-state.md`;
- `docs/journeys/STATUS.md`;
- the system charters under `docs/systems/`.

## 1. Audit scope and evidence boundary

The review was read-only until this document was written. It inspected the
workspace and both child repositories at clean `main` revisions:

| Repository | Audited revision | Initial state |
|---|---|---|
| Workspace | `6fb04af3848641b3be0a057d131bcf4cf7396870` | clean, synchronized with `origin/main` |
| Backend (`travel-agent`) | `95074b3eea7e1c5905d912822bbb3a6eaf5d9fb3` | clean, synchronized with `origin/main` |
| Mobile (`travel-app`) | `f7549bd757f82bf4688bd599cfc78a96923ef25d` | clean, synchronized with `origin/main` |

The investigation traced production code and tests across:

- product thesis, product model, current state, release scope, and journeys;
- canonical itinerary read authority and mutation impact envelopes;
- Mapbox routing, route-fact freshness, map projections, map sharing, and map
  conversation handoffs;
- Situation, canonical clocks, location capture, spatial proximity, weather,
  availability, and live-trip behavior;
- Places feed composition, context handles, saves, exposure, and search;
- Trips Home stack projection, modules, receipts, composition, and page state;
- AI turn loading, spatial context, route cards, and typed conversation seeds;
- group presence, social circles, relationship memory, invitations, privacy,
  and authority;
- booking, cancellation, provider boundaries, expenses, receipt OCR, and
  idempotency;
- OpenAPI, generated mobile types, operation policy, static budgets, TypeScript,
  dependency security, polish QA, and seeded journey execution.

“Implemented” below means a real production code path or executable contract
exists. It does not mean production-enabled, externally verified, or certified
on physical devices.

## 2. Progress against the product vision

The accepted product direction requires chat, map, itinerary, notification,
booking, Discover/Places, and memory to behave as interfaces into the same
intelligence. Within a Trip, the living itinerary is the canonical shared
operational truth. Spatial judgment must combine deterministic physical,
temporal, social, operational, and personal evidence rather than replace
missing truth with fluent prose.

### 2.1 Where implementation now matches the vision

#### One shared Plan

- The Plan and Map projections carry canonical itinerary authority and
  projection identity.
- Itinerary operations declare typed downstream impacts covering Plan, Map,
  details, Home, conflicts, proposals, bookings, expenses, live-trip state,
  retrieval, and history.
- The mobile realtime observer consumes identifier-only events and invalidates
  the declared read models, falling back to broad refresh for unknown impacts.
- Proposal, booking, expense, and itinerary mutation paths converge through
  shared invalidation helpers rather than each screen remembering unrelated
  cache keys.

#### Deterministic spatial truth

- Route segments carry requested and resolved mode, provider, observed and
  expiry times, degradation reason, geometry provenance, distance, and duration.
- Unsupported transport modes do not render a false provider route.
- Expired route facts are labelled stale; degraded fallbacks remain distinguishable
  from current provider truth.
- The map refuses to display a duration badge as current operational guidance
  unless its fact is fresh.
- Multi-city crossings, destination-local time, privacy-filtered member stays,
  saved-nearby places, neighborhoods, photos, and offline map state are modeled
  explicitly.

#### Governed multiplayer

- Trip membership remains the authority for shared Trip state.
- Social circles require explicit invitation and confirmation rather than being
  inferred from trip overlap.
- Circle trip links verify roster compatibility.
- Relationship-memory sharing is explicit and circle-scoped.
- Leaving or archiving a circle immediately removes cached shared-memory
  projections rather than waiting for an unauthorized refetch to fail.
- Circle events use a monotonic sequence and the mobile client detects gaps.

#### Honest partial availability

- Places producers execute behind bounded outcomes and expose unavailable
  sources without failing the entire feed.
- Situation composes independent plan, voice, group, signal, and modality reads
  concurrently and exposes partial-source failures.
- Trips and Places presentation layers distinguish loading, cached, offline,
  partial, empty, and failure states more explicitly than before consolidation.

### 2.2 Where implementation still falls short

The product thesis says that surfaces should reconcile with one intelligence.
The code now has many shared models, but several surfaces do not share the same
authoritative assembly or convergence graph. The result is a system that is
locally well designed yet can disagree at cross-surface handoffs.

## 3. Recent engineering progress by slice

### 3.1 Trips Home

Recent backend work extracted typed stack models, destination contracts,
receipt builders, projection identity, dedicated modules, bounded legacy rows,
and producer families. Recent mobile work extracted the route boundary,
controller, section plan, section render model, page-section view model,
physical page plan, state matrix, and body render phases.

The direction is strong: server rank order is preserved, destinations are typed,
renderability is validated, receipts are explicit, and physical rendering is
driven by a plan rather than scattered conditionals.

The remaining concern is ownership density. `TripsHomeController.ts` still
coordinates trips, unresolved decisions, notifications, saves, personal
insight, ambient weather, the server stack, Situation, Discover, editorial map,
Atlas, navigation, telemetry, refresh, and proposal resolution. The extraction
improved legibility but has not yet produced much capacity for another feature
wave.

### 3.2 Places

The canonical Places surface now consumes a server-ordered section feed with a
stable context handle. Backend producers cover saved places, scoped content,
experiences, social context, urgency, gaps, returns, nearby content, and partial
availability. Mobile presentation and render plans reject malformed mixed-card
payloads and route each card family through an explicit renderer.

This is meaningful convergence: context, ordering, relationship facts, producer
availability, and freshness are server-authored; the client primarily renders
and navigates.

The main gap is mutation convergence. The new feed is canonical, but shared
save invalidation still targets older Places projections and collections.

### 3.3 Map and spatial systems

The authenticated map is now the strongest cross-domain read model in the
product. It brings together itinerary authority, route facts, multi-destination
structure, timezones, member stays, saves, neighborhoods, photos, crossings,
offline support, live-day selection, accessibility, and typed navigation.

The weakness is assembly duplication. Other consumers use the same builder but
do not supply the same authoritative inputs, producing different spatial truth
under the same conceptual Map interface.

### 3.4 Time, location, weather, and Situation

- Plan and Situation share a snapshot instant so a block boundary cannot create
  internally impossible current/next states.
- Destination-local time is modeled rather than relying on device time or
  longitude approximations.
- The shared GPS stream prevents duplicate native subscriptions and centralizes
  permission state.
- Active Trip layout pushes significant location changes so Situation, leave-by,
  and concierge spatial context are not dependent on a recent chat message.
- Location-dependent nearby candidates carry freshness and accuracy.
- Weather can shape Trips Home ranking and weather-rescue proposals while
  remaining distinguishable from deterministic itinerary authority.

These systems are individually coherent. Their principal open question is not
data capture but whether every downstream surface consumes the same current,
purpose-bound snapshot.

### 3.5 AI and agent integration

The agent has real spatial Situation, trip context, typed conversation seeds,
canonical itinerary tools, route-card tools, receipts, and privacy-aware group
composition. That is far beyond a generic chat wrapper.

However, the AI spatial path does not assemble the same enriched map truth as
the interactive map, and the viewport handoff cannot express the actual area a
traveler selected. The AI is therefore integrated structurally but not yet
fully grounded at two important map seams.

### 3.6 Booking, expenses, and outcome trust

Booking surfaces now distinguish capability, preview, proposal, provider,
handoff, held-price, cancellation, and reconciliation states. Booking and
expense changes participate in the shared itinerary convergence graph. Receipt
OCR moved to a durable worker with a reaper so API restarts do not strand scans
forever.

The remaining reliability gap is receipt-row idempotency: OCR jobs are deduped
per receipt, but the upload operation itself is only process-locally deduped.

## 4. Confirmed findings

### P1-01 — Map assembly differs across interactive, AI, and public consumers

The interactive endpoint in `travel-agent/backend/api/routes/trips.py` assembles:

- resolved schedule timezone;
- explicit ordered destinations;
- privacy-filtered accommodations and member names;
- neighborhoods, saved-nearby places, and photos;
- current expiring route facts;
- canonical itinerary authority;
- city crossings.

It passes all of those into `build_trip_map_state`.

Three other active paths call the same builder with only `trip`, `full`, and the
legacy primary `place`:

- `travel-agent/backend/concierge/spatial_situation.py`;
- `travel-agent/backend/concierge/tool_handlers/content.py` for `post_map_route`;
- the public map preview in `travel-agent/backend/api/routes/trips.py`.

The editorial Trips Home map is intentionally cache-only, but it still passes
canonical authority and cached route facts. That makes the omission in the AI
and public-share paths more visible rather than less.

#### User-visible risk

- Vesper can reason from legacy transition duration while the interactive map
  shows or withholds a fresher provider fact.
- AI context can omit a multi-city route, crossing, or schedule-timezone fact
  that the traveler can see on Map.
- A shared public map can differ structurally from the authenticated map that
  produced the share action.
- A fix to interactive assembly does not automatically repair AI or share
  behavior.

#### Required correction

Create one map-state assembly service with named projection profiles, for
example:

- `interactive_viewer`;
- `ai_context`;
- `editorial_cache_only`;
- `public_share`.

Every profile must share a mandatory common core: canonical itinerary identity,
resolved schedule timezone, ordered destination route, crossing identity, and
route-fact provenance. Viewer-private layers must be explicit additions, not a
reason to omit canonical public-safe truth.

Add parity tests that assert the same canonical block IDs, day order, timezone,
destinations, crossings, and fact-status semantics across all applicable
profiles.

### P1-02 — Panned-map Vesper handoff omits the selected viewport

`travel-app/components/trip-map/TripMapScreen.tsx` records `viewportCenter` and
uses it to show “Ask Vesper” after a user pan. The action then creates a new
Trip-scoped conversation with a generic “near this part” prompt but sends no
center, bounds, zoom, observed time, or area identity.

`travel-app/utils/conversationSeed.ts` has no typed spatial viewport context,
so the omission cannot be repaired at the call site without extending the
handoff contract.

#### User-visible risk

The interface promises a question about the selected area, but the agent knows
only the overall Trip and destination. The answer can be plausible yet about
the wrong neighborhood—the exact fluent-without-grounding failure the product
model forbids.

#### Required correction

Add a typed, bounded spatial seed containing:

- center and optional visible bounds;
- zoom or derived area scale;
- observed time;
- geometry precision/source;
- permission/disclosure posture.

Resolve the seed server-side into canonical Place/Area context before it enters
the prompt. Treat raw coordinates as untrusted navigational evidence, not as an
instruction or stable place identity.

### P1-03 — Save/unsave does not invalidate the canonical Places feed

`travel-app/utils/invalidatePlaceSaveConsumers.ts` refreshes:

- legacy Places projection keys;
- saved collection keys;
- Home projections;
- Atlas venue-save projections.

It does not invalidate `queryKeys.placesFeedPrefix()`.

The mounted canonical Places workspace reads `usePlacesFeed`, whose response
contains `saved_total` and may include a ranked saved section. The default query
stale window is two minutes, global focus refetch is disabled, and the explicit
Places focus revalidation only refetches queries that are already stale.

#### User-visible risk

A successful save or unsave can leave the currently visible canonical Places
feed showing the old count, old section membership, or old ordering until an
unrelated refresh boundary.

#### Required correction

- Add `placesFeedPrefix()` to the shared save-consumer invalidation.
- Decide whether Trip itinerary `retrieval` impacts also invalidate trip-scoped
  Places feeds, because those feeds are context-handle aware and can derive from
  the current Plan.
- Add direct tests for save, unsave, redirected entity identity, and Trip-scoped
  context handles.

### P1-04 — Executable journey truth has advanced beyond committed status

The committed `docs/journeys/STATUS.md`, generated release scope, and Current
State still report J08 failing and Trip Home/Map/Now blocked.

The current local seeded replay executed during this audit returned:

| Persona | Result |
|---|---:|
| Mara | 23 / 23 pass |
| Elif | 4 / 4 pass |
| Reza | 1 / 1 pass |
| Total | 28 / 28 pass |

J08 passed the live Plan + Map next-stop invariant in the current seeded world.
`make dogfood-status-sync CHECK=1` correctly detects that the committed status
projection is stale.

This is positive progress, not device or release certification. The required
physical-device lane remains 0 / 3 current receipts for J04, J05, and J10.

#### Required correction

Regenerate committed persona and journey status from the current seeded replay,
then run the revision-bound device lane. Do not promote the local 28 / 28 result
into a production claim.

### P1-05 — Receipt-upload idempotency is not durable

The mobile receipt hook preserves one idempotency key for a retry of the same
image. The backend upload route consults `backend/core/idempotency.py`, whose
contract is explicitly process-local, non-durable, and permissive of concurrent
duplicate execution.

#### User-visible risk

Two workers, a deploy boundary, or concurrent retries can mint more than one
receipt row for the same logical upload. The OCR queue dedupes jobs by receipt
ID, but two duplicate rows produce two distinct job IDs.

#### Required correction

Use a durable unique identity such as `(trip_id, actor_id, idempotency_key)` on
a receipt-upload attempt or receipt row. Bind the key to an upload fingerprint
where appropriate and return the original row on replay. Add concurrent
Postgres coverage, not only process-local cache tests.

### P2-01 — Route freshness is enforced by the canvas but not the day summary

The canvas withholds travel-duration badges unless `fact_status == "fresh"`.
`travel-app/components/trip-map/tripMapDayRouteSummary.ts` nevertheless sums
every non-zero segment duration and selects the longest leg without considering
fact status.

In Plan travel mode, the sheet can therefore show an approximate movement total
derived from stale, degraded, or unknown facts while the map line correctly
refuses the same fact as current guidance.

#### Required correction

Define one shared travel-fact presentation policy. At minimum, separate:

- fresh operational totals;
- explicitly estimated planning totals;
- stale or unavailable totals that must be withheld.

Add coverage for fresh, stale, degraded, unknown, legacy-cache, and unsupported
transport-mode segments.

### P2-02 — Trips semantic tier is inferred from numeric producer priority

`travel-agent/backend/home/trips_stack.py` maps numeric priorities and fallback
bands into user-facing Trips tiers. The map contains many named exceptions
because rank priority and presentation meaning are not actually the same
dimension.

#### Risk

A new producer or changed priority can silently enter “urgent,” “orient,”
“needs you,” “gift,” or companionship presentation without explicitly
declaring that semantic intent.

#### Required correction

Make presentation tier explicit, typed producer metadata validated alongside
rank priority. Retain priority for ordering; stop using it as an implicit public
meaning contract.

### P2-03 — Consolidated mobile owners are at or over practical capacity

The home-surface ratchets pass, but several are exact or nearly exact:

| Boundary | Current / budget |
|---|---:|
| `TripsHomeModel` | 932 / 932 |
| `TripsHomeStyles` | 1483 / 1483 |
| `tripsHomeSectionPlan` | 267 / 267 |
| `PlacesWorkspace` | 768 / 769 |
| `TripsHomeController` | 809 / 825 |

The broader size gate remains red with 12 functions over 800 lines and two
files over 3,193 lines. The largest product owners include Plan, private chat,
booking, venue detail, group chat, Trip Map, Trip Info, expenses, and the Trip
provider.

The recent decomposition improved responsibility naming and testability. It did
not yet create enough ownership headroom for another cross-slice feature wave.

### P2-04 — Visual and route-chrome governance is incomplete

`npm run qa:polish:test` reaches the header-system audit and then reports:

- `/(tabs)/trips` has no declared header family or reviewed headerless exemption;
- `/angle/[angleId]` points at a missing source file;
- canonical Atlas memory surfaces do not report the expected `tab-root` chrome
  ownership.

The design-alignment calibration is also stale. Static contracts and committed
verdicts are present, but this audit did not capture new simulator or physical
device screenshots. No visual acceptance claim is made here.

### P2-05 — Test TypeScript debt and dependency advisories remain release debt

- Runtime application TypeScript passes.
- Test TypeScript reports 449 errors against a ratchet baseline of 407.
- The production dependency audit reports unapproved advisories in
  `image-size`, `js-yaml`, and `nanoid`.

Focused seam coverage can remain green while fixtures and test-facing contracts
drift. The test ratchet growth is therefore an architectural signal, not merely
test cleanup.

## 5. Validation evidence

### 5.1 Passing checks

| Check | Result |
|---|---|
| `make doctor` | pass; Docker/Postgres, Java, Maestro, and repo layout available |
| `make contract-check` | pass |
| Full OpenAPI snapshot | 467 paths / 520 operations / 1039 schemas |
| Mobile OpenAPI projection | 367 paths / 404 operations / 940 schemas |
| Generated `schema.gen.ts` parity | pass |
| Canonical place identity | pass across 10 seams in both snapshots |
| `make api-coverage-check` | 453 active, 11 dark, 0 unflagged, 56 retiring operations |
| `make docs-check` | pass after concurrent documentation consolidation landed |
| Mobile `npx tsc --noEmit` | pass |
| Focused mobile seam tests | 80 pass |
| Focused backend seam tests | 123 pass |
| Current local seeded personas | 28 / 28 pass |

The focused mobile set covered Trip read-model invalidation, save mutations,
Places feed render planning, Trips Home screen behavior, and Trip authority
observation. The focused backend set covered Trips stack projection and identity,
Places feed orchestration, Situation, group presence, relationship memory,
saves, social circles, and map sharing.

### 5.2 Failing or incomplete checks

| Check | Result |
|---|---|
| `make dogfood-status-sync CHECK=1` | fail; persona and journey status blocks are stale |
| `npm run size-budgets` | fail; 12 oversized functions, 2 oversized files |
| `npm run test:typecheck:ratchet` | fail; 449 errors vs baseline 407 |
| `npm run security-audit` | fail; 5 unapproved production advisories |
| `npm run qa:polish:test` | fail; header/route ownership gaps |
| Design-alignment gate | stale judge calibration |
| Current physical-device journey evidence | 0 / 3 required receipts |

### 5.3 Coverage holes exposed by the audit

No focused test located during the review asserts:

- parity between interactive map, AI spatial context, AI route card, and public
  shared-map canonical truth;
- propagation of a panned viewport through the conversation seed into server
  spatial grounding;
- canonical Places-feed invalidation after save/unsave;
- day-summary treatment of stale/degraded route facts;
- durable concurrent receipt-upload idempotency across workers.

## 6. Hardening sequence

### Phase 1 — One authoritative map assembly boundary

1. Introduce the profile-driven map assembly service.
2. Route the authenticated map, editorial map, AI Situation, `post_map_route`,
   and public share through it.
3. Define mandatory public-safe canonical fields and profile-specific private
   enrichments.
4. Add cross-profile parity and privacy tests.
5. Preserve cache-only behavior for editorial composition without weakening its
   canonical identity contract.

Exit criteria:

- all profiles agree on canonical block IDs, day order, timezone, destination
  route, crossings, and route-fact status;
- profile differences are declared and tested as privacy/performance policy;
- public share and AI no longer call the low-context builder directly.

### Phase 2 — Spatial handoff grounding

1. Extend `ConversationSeed` with a bounded spatial-context variant.
2. Send the panned viewport or selected neighborhood through that variant.
3. Validate and resolve it server-side to Place/Area identity and current
   spatial context.
4. Add disclosure copy and telemetry that identify whether grounding came from
   a selected entity, panned viewport, or current location.
5. Test trip switching, stale viewport reset, permission changes, and malformed
   coordinates.

Exit criteria:

- “this area” always resolves to inspectable spatial evidence;
- the model never has to infer a selected map area from prose alone.

### Phase 3 — Projection convergence graph

1. Add canonical Places feed invalidation to save/unsave.
2. Inventory every mutation-to-projection dependency for Places, Home, Map,
   Situation, Atlas, booking, and retrieval.
3. Move that inventory into one typed/tested invalidation contract rather than
   distributed comments.
4. Add context-handle-specific tests and a conservative unknown-impact fallback.

Exit criteria:

- every user-visible mutation identifies every derived projection it can change;
- no active canonical feed depends on a two-minute stale window for correctness.

### Phase 4 — Durable trust-loop idempotency

1. Add durable receipt-upload attempt identity.
2. Bind replay to actor, Trip, logical upload, and request fingerprint.
3. Return the original receipt row across workers and deploys.
4. Cover concurrent requests against Postgres.
5. Audit other real-money or external-side-effect endpoints still using the
   process-local idempotency helper.

Exit criteria:

- one logical receipt upload creates one receipt row and one OCR job under
  concurrent, cross-worker, and post-restart retry.

### Phase 5 — Evidence and release truth

1. Regenerate journey status from the current 28 / 28 local replay.
2. Re-run the fast and logic certification lanes on the pinned revisions.
3. Complete revision-bound J04/J05/J10 physical-device certification.
4. Repair header-route ownership and Atlas chrome classification.
5. Refresh design judge calibration and capture current critical surfaces.

Exit criteria:

- generated release/status docs match executable registries;
- device evidence is explicit and revision-bound;
- no seeded result is presented as deployed-provider or device proof.

### Phase 6 — Mobile ownership and global gates

1. Split Map orchestration from route-sheet, layer, share, AI-handoff, and
   optimization concerns.
2. Continue decomposing Plan, booking, chat, Trip Info, expense, and Trip
   provider owners.
3. Reduce test TypeScript errors below the ratchet before accepting new debt.
4. Resolve or explicitly approve production dependency advisories.
5. Move Trips tier semantics into explicit producer contracts.

Exit criteria:

- global size, type-ratchet, dependency, and polish gates pass;
- consolidated home-surface budgets retain meaningful headroom rather than
  sitting at their exact limits.

## 7. Final assessment

The system is progressing strongly against the “one coherent shared Plan” part
of the vision. Itinerary authority, mutation impacts, canonical identity,
multiplayer governance, and route-fact honesty are now genuine foundations.

It is only partially satisfying the stronger promise that Map, AI, Places,
Home, booking, notification, and memory are interfaces into one intelligence.
The authenticated map is currently ahead of the AI, public-share, and cache
convergence paths. Those paths can disagree without violating their local
tests.

The next highest-leverage work is therefore seam hardening, not another feature
family: one map assembly boundary, one spatial handoff contract, one projection
dependency graph, durable idempotency for trust loops, and evidence that the
whole flow converges on device.

