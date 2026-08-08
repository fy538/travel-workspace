---
doc_type: working
status: active
owner: founder / engineering
created: 2026-08-08
expires: 2026-09-07
why_new: Records the bounded cross-repo execution, verification evidence, and production rollout gates for the accepted place-identity decision without rewriting that immutable decision or presenting branch work as deployed state.
promotes_to: null
supersedes: []
---

# Place identity rollout execution and evidence

## Question or outcome

Execute the [accepted place identity and provenance decision](../decisions/2026-08-08-place-identity-and-provenance.md) across backend, mobile, and the generated API contract. Preserve one canonical subject as it moves through Saves, Atlas, Plan, Map, AI, weather, location, multiplayer, booking, search/vector projections, and Trips-home decision cards.

This is a branch evidence ledger, not a production-release claim. It answers:

1. Which seams now carry canonical typed identity?
2. Which evidence proves those changes locally?
3. Which production and device gates still prevent removal of compatibility paths?

## Outcome snapshot

The implementation is materially more coherent than the audited starting point:

- `EntityRef {type,id}` is the shared public identity boundary.
- Provider identifiers remain external evidence and cannot silently become durable application identity.
- Saves return durable resolution receipts; redirects and merges have canonical, reversible records.
- Place facts retain source, freshness, confidence, and geometry precision independently of identity.
- Atlas retains raw evidence while joining timelines and drill-ins through canonical geography.
- Plan, Map, location, multiplayer, booking, search, and Trips-home cards now dual-write or consume typed canonical references.
- AI planning rejects ambiguous identity instead of guessing.
- Weather and proximity claims expose their spatial/provenance qualifications.
- Redirected vector projections fail closed, and an idempotent dry-run-first vector backfill exists.
- An executable OpenAPI gate protects ten cross-surface identity seams in both the complete and active-mobile snapshots.

The system is not ready to remove compatibility inputs. Production vector data has not been scanned or rewritten, compatibility counts are process-local until connected to an exporter, and the current simulator did not have a Mapbox public token.

## Implementation ledger

These are direct branch commits, excluding merge commits.

### Route, travel evidence, and mutation foundation

Backend:

- `35deac81` preserves discontinuities around unplaced adjacent stops.
- `4d5ecea5`, `9f03afad`, and `7476474d` establish shared route facts with source, freshness, and expiry.
- `51b08fdc`, `de8029ef`, `ab787fc4`, `fe103180`, and `acab71ba` make feasibility, optimization, and conflict analysis consume authoritative directional route evidence.
- `1bcd7a58` carries route provenance into concierge spatial ETA reasoning.
- `3e0921a8`, `cc83ad5d`, and `e3a54199` define the itinerary mutation envelope, atomic proposal application, and durable projection outbox.
- `506821f6` registers the mutation-envelope contract under workspace documentation governance and records the implemented outbox boundary.
- `140788e9` ranks availability disruption swaps by proximity.

Mobile:

- `86ad5a6f` preserves gaps in mock route projection.
- `20af4217` renders route-fact freshness states.

### Identity core, receipts, redirects, and provenance

Backend:

- `d7abdf2a` persists canonical resolution receipts for Saves.
- `c5948a85` defines the typed entity-reference contract.
- `a96e0987` registers external provider mappings separately from application identity.
- `09b8ef7b` adds the scoped redirect ledger.
- `251056a7` centralizes reversible merge effects.
- `f5d9f01c` governs entity facts and geometry precision.

Mobile:

- `6eed83aa` retains canonical provider-resolution identity on Save responses.

### Atlas and itinerary continuity

Backend:

- `9fb3f387` retains Atlas source evidence and resolves canonical geography.
- `831d89a9` joins Atlas timeline events through canonical place identity.

Mobile:

- `40feedfb` corrects canonical Atlas matches.
- `a2938aeb` drills from Atlas evidence into canonical places.

Workspace API snapshots:

- `abbbe50`, `1158d82`, and `6754d3f` synchronize the identity, Atlas geography, and canonical timeline contracts.

### Map and Plan

Backend:

- `467c2d76` carries typed identity on Map stops and actions.
- `84a29b70` exposes canonical entity references from Plan.
- `7e8426e7` keeps the migration additive for older consumers.

Mobile:

- `9ed09734` consumes typed Map-stop identity.
- `59cc17bc` consumes canonical Plan identity.

Workspace API snapshots:

- `dccb6dc` and `85d9fbf` synchronize Map and Plan.

### AI, weather, and location

Backend:

- `5680e0f2` rejects ambiguous planning identities at the AI boundary.
- `5586c0cc` grounds forecasts in place provenance.
- `cd3a9278` qualifies canonical proximity claims.

Mobile:

- `5aff4c5a` consumes typed nearby identity.

Workspace API snapshot:

- `d8114bb` synchronizes nearby provenance.

### Multiplayer and booking

Backend:

- `03c0bb9e` preserves canonical proposal identity through multiplayer reads.
- `50152a2c` preserves canonical proposal identity in booking.
- `3fe718c7` stamps typed identity on group-visible booking cards.

Mobile:

- `1e82528b` and `47dcb201` consume canonical proposal identity in multiplayer and booking.

Workspace API snapshots:

- `b319094` and `e1fa802` synchronize the multiplayer and booking contracts.

### Search, vectors, Trips home, and compatibility control

Backend:

- `acc506d6` suppresses stale redirected search projections.
- `79155ace` counts low-cardinality compatibility input forms without retaining identifiers.
- `bf1d2b7d` adds an idempotent, fail-closed vector identity backfill.
- `9b6d35d1` dual-writes canonical typed identity for Near You and pick cards while retaining additive legacy fields.

Mobile:

- `526209c7` routes search results using canonical typed references.
- `3779658d` consumes typed deck identities and fails closed on malformed or conflicting references.
- `2ee772e8` synchronizes generated mobile types for the deck contract.

Workspace:

- `4a5db8b` synchronizes search identity.
- `058e137` adds the cross-surface OpenAPI identity gate.

### Current-build journey maintenance

Fresh-simulator verification exposed stale automation labels, not identity implementation defects:

- `ffc81ff4` follows the renamed Places tab.
- `e8982735`, `3427c275`, and `aeddde47` follow Atlas's current add-place and saved-place accessibility labels.
- `8dfe9d56` asserts the stable Trips return surface after a proposal revert.
- `134bac29` verifies the two visible fields of the reverted receipt.
- `542d1396` was explicitly neutralized by `9dcbd27c`; the legacy Near You capture remains unchanged because its current product posture needs a separate rewrite, not a gesture-only adjustment.

## Privacy and provenance boundary

The accepted boundary remains:

- Private imported or provisional candidates are owner-scoped by default.
- Provider references, matching evidence, raw resolution receipts, and geometry/source evidence do not enter group-visible messages or booking cards.
- Group surfaces may carry canonical catalog identity plus group-safe presentation fields.
- A merge deduplicates identity without escalating sharing consent.
- Historical receipts retain the originally requested reference and resolve through the redirect ledger.
- Proximity and weather claims disclose their location, precision, source, and freshness qualifications; absence or uncertainty must remain visible rather than being converted into false precision.

## Evidence

### Static and contract evidence

- Mobile changed-surface suite: 25 suites, 317 tests passed.
- Backend changed-surface suite excluding the known corpus mismatch: 968 tests passed.
- Real Postgres identity core: 16 tests passed across external mapping, facts, redirects, merge, Save idempotency, redirected search, multiplayer proposal identity, and booking proposal identity.
- Vector backfill: 6 in-memory Qdrant tests passed for preview, apply, idempotence, and fail-closed blocking.
- Compatibility parsing/counting: 14 focused tests passed.
- OpenAPI identity gate: 10 seams checked in both snapshots, plus 3 checker unit tests.
- Workspace contract check passed after regenerating the complete snapshot, active-mobile projection, and TypeScript schema.
- Documentation governance, inventory, spine, generated status, links, and compatibility-ledger checks passed.
- Maestro structural validation passed for 316 flows, 8 configs, 316 unique names, and 10 package references. The aggregate metadata gate remains red on 26 pre-existing flows; none of the place-identity journey files changed in this tranche appears in that drift list.

The broad backend changed-test run also reported 978 passes and 3 failures. All three are in `tests/workers/test_inbound_jobs.py`: the isolated database resolves the exact Lisbon coordinates to venue `36`, while the historical corpus assertion hard-codes venue `1104`. Downstream attribution assertions then fail. Re-running every other changed backend test plus the new inbound provisional-geometry case produced the 968-pass result above. This is recorded as a fixture/environment mismatch, not hidden as a green full run.

### Current-build simulator evidence

Build:

- Exact mobile branch compiled as the native iOS app `com.fyan.vesper`.
- Dedicated simulator: iPhone 16 Pro, iOS 18.2, UDID `74F47108-7847-4524-AE53-EC31654E538D`.
- Mock mode was explicit and visibly labeled; these runs do not prove staging or production data behavior.

Passed:

- Atlas search → canonical place detail → Save → return to Atlas: the saved count advanced and “Open saved place Cervejaria Ramiro” was visible.
- J06 proposal apply → clean reversible receipt → Changes history → direct itinerary mutation receipt → Plan truth → Map stop truth: the full flow passed.
- The Map flow preserved an unplaced named stop and disclosed “Some stops are not placed yet — open Plan to add venues.”

Bounded limitations:

- No Mapbox public token was available. The native Map surface and stop sheet rendered, but the screenshot correctly showed “Map preview is unavailable here”; tiles, route geometry, and camera behavior are not device-verified by this run.
- J08 reached the current Carmen Vesper surface, but the old flow expects a retired home-card composition and stops before its Plan/Map handoff. Do not count J08 as current-build passed.
- The legacy Near You capture reached the correct Kyoto planning persona, but its expected Trips posture is no longer present in that composition. Typed Near You/deck identity is covered by focused model/component tests, not a passing current-device journey.
- This is simulator evidence, not physical-device evidence and not a live two-account multiplayer proof.

## Product-vision assessment

The architecture now supports the vision that Vesper understands a trip as one evolving world instead of a set of disconnected screens. A venue discovered from a provider can materialize once, retain its provenance, survive correction or merge, and remain addressable as the same subject in a Save, Atlas history, itinerary block, Map stop, proposal, booking card, nearby recommendation, and AI instruction.

The strongest progress is at the seams:

- time and availability use authoritative route facts rather than ad hoc distance guesses;
- AI is constrained by canonical identity and rejects ambiguity;
- weather and location claims are qualified instead of presented as universal truth;
- multiplayer and booking share canonical subjects without exposing private evidence;
- search/vector projections respect redirects;
- mobile navigation prefers canonical identity but remains additive during rollout.

The remaining gap is operational, not conceptual. Until production data is scanned, compatibility telemetry is exported and observed, Mapbox-backed rendering is exercised, and live multi-account journeys pass, Vesper has a coherent identity spine in code but not yet complete rollout evidence.

## Production rollout plan

Execute in order. Stop at any failed gate; do not remove or rewrite legacy fields to force progress.

### 1. Land additive contracts

1. Review and land backend migrations and writers.
2. Land the tolerant mobile readers and generated API projection.
3. Land the workspace OpenAPI gate.
4. Re-run migrations against a production-shaped staging snapshot.
5. Confirm legacy clients still receive their existing fields and canonical clients receive typed references.

Gate: contract check, changed suites, real-Postgres identity tests, and the cross-surface checker are green on the landed commit set.

### 2. Export compatibility telemetry

1. Connect `snapshot_entity_ref_compatibility_counts(reset=True)` to the production metrics/logging path.
2. Export only aggregate counters for legacy underscore, legacy colon, bare numeric, and provider-wire forms.
3. Never attach raw entity or provider identifiers.
4. Observe at least one full supported-client upgrade window.
5. Attribute remaining compatibility reads to a known client/version or internal caller.

Gate: canonical reads dominate, every remaining legacy caller has an owner, and the observation window contains no unexplained rebound.

### 3. Preview the vector backfill

From the backend runtime with production Qdrant credentials:

```bash
python -m backend.scripts.backfill_vector_entity_refs
```

The command scans all five collections before any write. Preserve its JSON result as an operational artifact.

Gate: `blocked` is false; there are no missing, malformed, conflicting, or unresolvable identities; point counts reconcile with collection totals.

### 4. Apply the vector backfill

After a Qdrant snapshot/backup and review of the preview artifact:

```bash
python -m backend.scripts.backfill_vector_entity_refs \
  --apply \
  --confirmation backfill-canonical-vector-entity-refs
```

Immediately rerun dry-run preview.

Gate: the second preview proposes zero writes, vector values are unchanged, redirected projections are inactive, and representative searches resolve to the canonical subject.

### 5. Shadow-read and compare

1. Compare typed and compatibility resolution for Map, Plan, Atlas, search, nearby, proposals, booking, and deck cards.
2. Track mismatch counts by low-cardinality surface and form.
3. Verify redirect chains, reversal behavior, and idempotent Save/merge receipts on staging.
4. Measure search projection lookup cost; the current per-result redirect resolution may require batching before production scale.
5. Exercise exact, approximate, missing, stale, and disputed geometry/fact states.

Gate: zero unexplained subject mismatches, no privacy-boundary violations, and acceptable latency/error budgets.

### 6. Run user-facing proof

1. Build with a valid Mapbox public token and verify pins, route geometry, camera focus, stop sheet, and fallback states on iOS and Android.
2. Rewrite J08 and the Near You journey around the current product composition, then run them on the exact release candidate.
3. Run Atlas save/correct/forget and place-merge correction on a physical device.
4. Run two-account proposal and booking-card flows; inspect both viewers for canonical identity and group-safe text only.
5. Run offline/retry/restart cases for receipts and redirects.

Gate: release-candidate device evidence exists for the protected journeys; screenshots alone do not replace interaction and persistence proof.

### 7. Switch and retire compatibility

1. Make canonical typed reads authoritative one surface at a time.
2. Keep rollback switches and aggregate mismatch telemetry during the bake period.
3. Remove legacy writers only after their read counters remain zero for the agreed window.
4. Remove legacy readers in a later release after supported old clients age out.
5. Archive this working note or promote repeatable operations into a runbook.

Gate: no supported client depends on compatibility input, production backfill is idempotently complete, and rollback has been rehearsed.

## Residual risks and owners

| Risk | Consequence | Required owner action |
|---|---|---|
| Compatibility counters are process-local | Restarts and multi-worker aggregation hide true usage | Connect to an aggregate exporter before using counts as a removal gate |
| Search redirect suppression resolves per result | Potential N+1 database cost | Batch or cache canonical resolution and load-test |
| Legacy deck fields remain | Dual truth can drift during a long rollout | Compare canonical and legacy fields, then retire by telemetry |
| Production Qdrant is untouched | Old vectors may lack or conflict on identity | Run preview, repair blockers, snapshot, apply, and rerun |
| Mapbox tiles/routes were not available in simulator | Visual and interaction regressions remain possible | Provide a valid token and run release-candidate iOS/Android proofs |
| J08 and Near You fixtures lag current composition | Protected seams lack current journey evidence | Rewrite without weakening identity or privacy assertions |
| Provider mapping and merge operations need operating UX | Correctness may depend on manual database work | Add reviewed repair/admin workflows around the canonical service |
| No live two-account proof in this pass | Group projection/privacy behavior is not release-proven | Run persisted organizer/member staging evidence |

## Exit

Before 2026-09-07, either:

- archive this as point-in-time branch evidence after the rollout;
- promote the repeatable vector/telemetry procedure into an operations runbook; or
- replace open work with owned tasks and preserve only the final release evidence.
