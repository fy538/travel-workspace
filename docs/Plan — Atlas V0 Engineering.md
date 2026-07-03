# Plan — Atlas V0 Engineering

> **Outcome (as of 2026-07-03):** ✅ Shipped — V0 photo backfill, manual picker, LLM composer, and DNA provenance columns are all live.

Engineering plan for V0 of the Atlas Photo Backfill feature. Companion to `Travel App/docs/Brief - Atlas Photo Backfill.md`, which carries the product decisions this plan implements. Read the brief first; this document does not re-derive its decisions.

## Scope

V0 ships the **manual import path** from the brief's Permission Strategy. The user picks photos themselves, Vesper clusters and renders one or more artifacts, and the artifact loop completes end-to-end into Travel DNA and the audit surface.

**In scope:**

- The "Choose photos myself" path from the brief's Permission Strategy
- Post-onboarding hero moment on the Atlas tab
- Local clustering within the user's selected photos
- Confidence-graded candidate surfacing (three tiers, 3–5 cap)
- One artifact per approved candidate, drawn from Trip Story / Weekend Card / Day Postcard / Place Memory
- Provenance ribbon ("Built from your photos") on imported trips
- Three artifact states (private + signals on default, private + signals off, shareable scaffolding)
- Travel DNA signal extraction with per-artifact provenance and cascade-revoke
- The audit-bridge entry point per artifact
- Memory Inbox surface (V0: empty pass-through; V1 populates it from auto-scan)

**Out of scope — deferred to V1+:**

- Full-library auto-scan
- JournalingSuggestions integration
- Apple Foundation Models hybrid
- Background catch-up (`BGAppRefreshTask`)
- Incremental rescan (`PHPersistentChangeToken`)
- Burst grouping (`burstIdentifier` — needs custom native module)
- Vision feature-print dedup (needs custom native module)
- Custom Expo Module / dev-client move — V0 stays in managed Expo SDK 55
- Shareable artifact projection (the state exists; server-side projection lands V2)

## User flow — V0 happy path

1. User completes onboarding (Clerk auth, intake).
2. Lands on the Atlas tab. Empty state shows the hero card: *"Let Vesper build your first Atlas."*
3. Tap → Screens 1–3 from the brief (Promise / Trust / Scan).
4. iOS limited-access picker opens. User selects ~20–80 photos.
5. App reads metadata, clusters locally, displays 1–5 candidate cards.
6. User taps a candidate, sees the preview (map, dates, sample photos, why-Vesper-grouped-it).
7. User taps "Render story." App posts the approved candidate to the backend.
8. Backend kicks off async artifact generation; LLM composes title + one-line read + sections.
9. App subscribes to the SSE stream and renders the artifact shell immediately (title placeholder + map + hero candidate), story sections stream in.
10. Artifact lands in Atlas. Travel DNA updated. "What Vesper knows" surfaces the new signals with provenance.

## Acceptance criteria

A new user with the app and ≥50 photos in their library can complete the following inside one session:

- [ ] Land on the Atlas tab after onboarding without navigating manually
- [ ] Pick photos via the limited-access picker
- [ ] See ≥1 candidate card within 10 seconds of picker dismissal
- [ ] Preview a candidate showing map, dates, sample photos, and a why-grouped reason
- [ ] Approve a candidate and see the artifact shell within 5 seconds
- [ ] Read a complete artifact with a specific, evidence-grounded one-line read within 30 seconds of approval
- [ ] See Travel DNA update reflected in "What Vesper knows"
- [ ] Tap the audit-bridge row on the artifact and cross to "What Vesper knows" filtered to this artifact's signals
- [ ] Toggle the artifact between signals-on and signals-off; verify signals propagate or revoke
- [ ] Delete the artifact; verify derived signals revoke from the audit surface immediately, and from Travel DNA after the next synthesis cycle (eventual consistency — see Signal extraction below)

Brief-mandated invariants enforced:

- [ ] No candidate surfaces without a specific one-line read passing the hard gate
- [ ] No full-library upload; only selected photos go to the backend, and only for approved candidates
- [ ] Provenance ribbon visible on the imported trip artifact
- [ ] Private by default; share flow is not exposed in V0

## Backend — data model and endpoints

New subsystem: `backend/atlas/`.

**New Pydantic models:**

```python
class AtlasCandidate(BaseModel):
    id: UUID
    user_id: UUID
    date_range: tuple[date, date]
    place_guess: str | None             # "Tokyo", "Williamsburg", null if unknown
    place_count: int                    # distinct GPS clusters within
    photo_count: int
    sample_photo_ids: list[str]         # PHAsset localIdentifiers (opaque to backend)
    confidence: Literal["high", "medium", "low"]
    candidate_type: Literal["trip", "weekend", "day_out", "place_memory"]
    cluster_reason: str                 # for the preview "why Vesper grouped this"
    created_at: datetime

class AtlasArtifact(BaseModel):
    id: UUID
    user_id: UUID
    source_candidate_id: UUID
    artifact_type: Literal["trip_story", "weekend_card", "day_postcard", "place_memory"]
    title: str
    one_line_read: str
    sections: list[ArtifactSection]
    hero_photo_id: str | None
    photo_ids: list[str]
    map_points: list[GeoPoint]
    date_range: tuple[date, date]
    place_label: str | None
    signal_state: Literal["signals_on", "signals_off", "shareable"]
    derived_signals: list[DerivedSignal]
    imported_trip_id: UUID | None       # if linked to a Trip with source=photos_import
    created_at: datetime

class DerivedSignal(BaseModel):
    id: UUID
    artifact_id: UUID
    signal_type: str                    # "travel_dna_phrase", "preferred_neighborhood", etc.
    value: str
    confidence: Literal["high", "medium", "low"]
    user_state: Literal["active", "disputed", "forgotten"]
```

The existing `Trip` model gets a new field: `source: Literal["vesper_planned", "photos_import", "manual"]`. Existing trips backfill to `vesper_planned` via Alembic migration.

**New endpoints under `/api/atlas/`:**

| Method | Path | Purpose |
|---|---|---|
| POST | `/api/atlas/candidates` | Submit one or more locally-clustered candidates. Body: list of candidate descriptors. Returns: persisted candidates with ids. |
| GET | `/api/atlas/candidates/{id}` | Fetch a candidate for preview. |
| POST | `/api/atlas/candidates/{id}/approve` | Approve a candidate. Triggers async artifact generation. Returns: artifact id + initial shell. |
| GET | `/api/atlas/artifacts/{id}` | Fetch full artifact (for polling). |
| GET | `/api/atlas/artifacts/{id}/stream` | SSE stream for artifact generation progress. Reuse the Concierge SSE pattern. |
| PATCH | `/api/atlas/artifacts/{id}/state` | Toggle `signal_state`. Body: `{ "state": "signals_off" }`. |
| DELETE | `/api/atlas/artifacts/{id}` | Delete artifact; cascade-revoke all derived signals. |
| GET | `/api/atlas/artifacts/{id}/signals` | List derived signals for the audit bridge. |
| GET | `/api/atlas/inbox` | List pending candidates and recent artifact activity. V0: returns empty + recent artifacts. |
| POST | `/api/atlas/photos/upload` | Pre-signed upload URL for approved photos. |

**Artifact generation** reuses the existing Trip Story composer with a new prompt that:

- enforces the one-line-rule gate (returns `null` when no grounded line can be written)
- applies the brief's Non-Controversial Copy doctrine
- emits the artifact AND `DerivedSignal` records in a single pass

**Signal extraction.** The Travel DNA pipeline does not currently support per-source revocation. Investigation confirmed that `personal_memories.markdown_content` and `personal_memories.taste_dimensions` (in `backend/core/db/_tables/memory.py`) are lossy LLM aggregates synthesized by `refresh_personal_memory()` (`backend/concierge/refresh_memory.py:313+`) with no provenance back-references. The existing dispute endpoints (`me/dna-phrases/dispute`, `me/profile-fact/dispute`) are rebuttal, not revocation — they append counter-observations and re-synthesize.

V0 ships the infrastructure to enable revocation:

- **Schema migration on `observations`.** Add `source_artifact_type TEXT` and `source_artifact_id UUID` columns, with a partial index on `(user_id, source_artifact_type, source_artifact_id) WHERE source_artifact_id IS NOT NULL`. Existing rows backfill from the unstructured `provenance` JSONB where derivable; others remain null. The existing ~20 `create_observation(...)` call sites elsewhere in the codebase are not part of V0's audit — they can migrate over time.
- **Write-side discipline in the Atlas flow.** Every observation written by an Atlas artifact populates both new columns: `source_artifact_type="atlas_artifact"`, `source_artifact_id=<artifact_id>`. The `DerivedSignal` records on the artifact mirror these for the audit-bridge UI.
- **Revoke helper.** New `delete_observations_by_artifact(user_id, artifact_type, artifact_id)` in `backend/core/db/observations.py` that soft-deletes (`is_active=False`) matching rows. Triggers `refresh_personal_memory()` afterward so the next synthesis sees the reduced signal set.
- **Cascade on DELETE `/api/atlas/artifacts/{id}`.** The endpoint calls the revoke helper, removes the `DerivedSignal` rows, then deletes the artifact.

**Honest UX about eventual consistency.** After revoking source observations, the next `refresh_personal_memory()` cycle *should* drop orphaned signals — but the synthesis prompt explicitly preserves prior understanding from older `traveler_profile_versions`, so a signal can persist if the LLM justifies it from versioned snapshots. The artifact-delete UI must communicate fade, not instant forgetting: *"Your signals will fade as Vesper updates your profile."* The existing dispute mechanism remains the user-facing fallback for any signal that won't die. This is consistent with the brief's voice and avoids overpromising.

## Frontend — screens, components, hooks

New screens under `app/atlas/`:

| Path | Purpose |
|---|---|
| `app/(tabs)/atlas/index.tsx` | Atlas tab. Empty state + hero card. Existing-artifacts grid (chronological flat default). |
| `app/atlas/scan.tsx` | Onboarding Screens 1–3 (Promise / Trust / Scan). |
| `app/atlas/candidates.tsx` | Screen 4 — candidate results list. |
| `app/atlas/candidate/[id].tsx` | Screen 5 — candidate preview. |
| `app/atlas/artifact/[id].tsx` | Screen 6 — artifact shell + final rendered artifact. |
| `app/atlas/learned/[artifactId].tsx` | The audit-bridge target. Links to Travel DNA / memory receipt surfaces for provenance context. |

**Atlas tab is new.** Add a fourth tab to `app/(tabs)/_layout.tsx`. The brief commits to Atlas as the surface.

New components under `components/atlas/`:

- `CandidateCard.tsx` — one row in Screen 4
- `CandidatePreview.tsx` — Screen 5 body
- `ArtifactStateChip.tsx` — private / signals-off / shareable
- `AuditBridgeRow.tsx` — *"Vesper learned three things from this →"*
- `ProvenanceRibbon.tsx` — *"Built from your photos"*
- `ConfidenceLabel.tsx` — High / Medium / Low affordance

Reuse from existing `components/memory/`:

- `TripStoryHero` for Trip Story artifact rendering
- `PhotoSlotCard` for photo selection within an artifact
- `StoryArchiveCard` for the Atlas grid

New data-layer hooks in `data/atlas.ts`:

```typescript
useAtlasInbox()
useAtlasArtifacts()
useAtlasArtifact(id)
useSubmitCandidates(localCandidates)   // submit local clusters, get persisted candidates back
useApproveCandidate()                  // mutation
useArtifactStream(id)                  // SSE during generation
useToggleSignalState(id)               // mutation
useDeleteArtifact(id)                  // mutation + cascade signal revocation
```

**Photo selection** uses `expo-media-library` (per the V0 substrate decision in the brief):

1. Request limited permission via `MediaLibrary.requestPermissionsAsync({ accessPrivileges: 'limited' })`
2. Present the picker via `MediaLibrary.presentPermissionsPickerAsync()`
3. For each selected asset id, call `MediaLibrary.getAssetInfoAsync(id)` to retrieve `creationTime`, GPS via `getLocation()`, `mediaSubtypes`
4. Filter screenshots and obvious noise per the brief's Noise Filtering rules
5. Pass the metadata array into the clustering function

## Clustering algorithm — V0

Deterministic, on-device, no LLM. Pseudocode:

```typescript
function cluster(photos: PhotoMetadata[]): Candidate[] {
  // 1. Drop noise (screenshots, panoramas without GPS, downloads with no EXIF)
  const cleaned = photos.filter(isCandidateMaterial)

  // 2. Sort by timestamp
  cleaned.sort((a, b) => a.timestamp - b.timestamp)

  // 3. Bucket into time-contiguous groups
  //    ≤24h gap = same bucket; ≤72h = same bucket if same GPS region
  const timeBuckets = bucketByTimeGap(cleaned, {
    hardGapHours: 72,
    sameRegionGapHours: 168,
  })

  // 4. Within each bucket, grid-cluster GPS (0.01° ≈ 1km cells)
  const candidates: Candidate[] = []
  for (const bucket of timeBuckets) {
    const gpsClusters = gridCluster(bucket, { cellDeg: 0.01 })
    const validClusters = gpsClusters.filter(c => c.length >= MIN_CLUSTER_SIZE)

    // 5. Apply home/work suppression — V0 uses profile home only; full inference is V1
    const filtered = applyHomeWorkFilter(validClusters, userHome)

    // 6. Classify candidate type by duration + cluster count
    const candidate = classifyCandidate(bucket, filtered)
    candidate.confidence = scoreConfidence(candidate)
    candidates.push(candidate)
  }

  // 7. Cap at 5 candidates; rank by confidence
  return candidates.sort(byConfidenceDesc).slice(0, 5)
}
```

For V0, `MIN_CLUSTER_SIZE` relaxes to 3 (vs. ≥15 for V1 auto-scan) — the user has already done the noise-filtering by hand by picking the photos.

**Home/work inference is V1.** V0 uses the user's profile home location if set; otherwise skips home suppression. Acceptable because manually-picked photos rarely contain home-spam.

**Test fixtures** live in `Travel App/__tests__/fixtures/photo-libraries/`:

- `tokyo-trip-184.json` — 184 photos, 6 days, 3 GPS clusters
- `whistler-weekend-72.json` — 72 photos, 2 days, 1 cluster
- `williamsburg-afternoon-18.json` — 18 photos, 1 day, 4 stops
- `mixed-two-trips.json` — selection spanning two distinct trips (verify split)
- `noisy-with-screenshots.json` — verify noise filtering
- `stale-gps-after-landing.json` — verify outlier handling (the "first photo off the plane geocodes wrong" case from the brief's Stale Or Wrong GPS edge case)

## Artifact generation — LLM contract

The backend artifact-composer receives:

```json
{
  "candidate_id": "...",
  "date_range": ["2026-03-12", "2026-03-18"],
  "place_label": "Tokyo",
  "place_clusters": [{ "lat": 35.66, "lng": 139.70, "count": 84 }],
  "sample_photos": [
    { "id": "...", "label_hints": ["food", "neon"], "timestamp": "..." }
  ],
  "user_dna": { "..." : "..." },
  "user_history": { "..." : "..." }
}
```

Returns:

```json
{
  "artifact_type": "trip_story",
  "title": "Tokyo, in side streets",
  "one_line_read": "You followed the neighborhood before the landmark.",
  "sections": [],
  "derived_signals": [
    { "type": "travel_dna_phrase", "value": "neighborhood-first traveler", "confidence": "high" },
    { "type": "preferred_pace", "value": "late evening", "confidence": "medium" }
  ]
}
```

**The one-line read gate.** The composer must return either a specific, evidence-grounded line OR an explicit `null` with a reason. If `null`, the candidate is downgraded to a Place Memory or rejected outright; the artifact is NOT rendered. This is the brief's hard gate, enforced server-side.

## Mock strategy

`utils/api/mock.ts` adds Atlas methods returning three seeded candidates with deterministic ids (Tokyo, Whistler, Williamsburg). Approval triggers immediate artifact generation in mock — no LLM call, returns hand-written artifact.

**Real-mode parity caveat:** photo selection cannot be mocked because `expo-media-library` returns real PhotoKit data. Mock mode skips the picker step and presents pre-selected fixture photos. Document this in `Travel App/docs/Mock vs Real Parity.md` as a named drift hotspot.

**Offline tests cover:**

- Clustering algorithm against every fixture file
- API contract conformance (`schema.gen.ts` round-trip)
- State-toggle logic + signal cascade
- One-line read gate (mock composer returns `null` → verify candidate downgrade)

PhotoKit-dependent code is excluded from offline tests; smoke-tested manually against a real device build per release.

## Sequencing — two engineers, two weeks

**Week 1**

- Backend: Atlas data model + Alembic migrations including the `observations` provenance columns (`source_artifact_type`, `source_artifact_id`); endpoint skeletons returning 200 OK with empty/seed data; mock LLM composer for end-to-end wiring; the `delete_observations_by_artifact` helper.
- Frontend: photo-picker integration; clustering algorithm with tests against fixtures; Screens 1–3 hardcoded against mock candidates; add the Atlas tab to `(tabs)/_layout.tsx`.
- **End-of-week sync point: API contract lock.** Regenerate workspace `docs/openapi.json` via `./scripts/sync-types.sh`; `schema.gen.ts` lands in Travel App.

**Week 2**

- Backend: real LLM artifact composer + prompt iteration against fixture candidates; Travel DNA signal extraction writing observations with the new provenance columns; cascade-delete on `DELETE /api/atlas/artifacts/{id}` calls the revoke helper and triggers `refresh_personal_memory()`.
- Frontend: Screens 4–6 wired to the real backend; audit-bridge integration with existing `what-vesper-knows`; provenance ribbon on imported trips; state-toggle UI with the fade-not-forget copy.
- **End-of-week milestone:** dogfood-ready against the Fly backend. Two team members test against real photo libraries — at least one Tokyo-class trip and one local-only library.

**Long pole:** the LLM one-line-read prompt. Budget 3–4 rounds against the three fixture libraries before the gate behaves correctly. If the quality bar is not met by end of week 2, ship V0 with the one-line read as the artifact title only (degraded but honest) rather than weaken the gate.

## Risks and unknowns

- **`expo-media-library` limited-access behavior in SDK 55.** Verify on day 1 that `presentPermissionsPickerAsync` returns selected assets with full metadata via `getAssetInfoAsync`. iOS picker UX has changed across SDK versions; spike before committing to the V0 timeline.
- **Stale GPS within selected photos.** User picks photos from a trip where the first three off the plane geocode to the wrong city. Clustering treats single-asset GPS outliers within a tight time window as noise and uses the cluster centroid. Covered by `stale-gps-after-landing.json` fixture; verify before release.
- **One-line read quality variance.** Claude may produce generic copy on a thin candidate. The gate must reject rather than soften. Test: feed the composer a deliberately weak candidate; verify it returns `null`.
- **DNA synthesis eventual consistency.** Per-source revocation is added in V0 (see Signal extraction above), but the underlying `personal_memories` table aggregates via LLM synthesis with no provenance attribution. After revoking source observations the next refresh *should* drop orphaned signals — but the synthesis prompt preserves prior understanding from older `traveler_profile_versions`, so the LLM can re-emit a signal it can no longer justify from current observations. The dispute mechanism is the user-facing fallback for stuck signals; the UX must communicate fade, not instant forgetting. See **Follow-up: DNA Provenance Hardening** below for the planned remediation.
- **Mock fidelity.** Photo selection is the only V0 step that cannot be mocked. Document clearly in `Mock vs Real Parity.md`; flag the candidate-clustering algorithm as the highest-stakes offline-testable surface.

## Follow-up: DNA Provenance Hardening

V0 lands the minimum infrastructure for Atlas — new columns on `observations`, write-side discipline inside the Atlas flow, the source-keyed revoke helper, cascade-delete on artifact removal. It explicitly does NOT touch the rest of the codebase or the deeper aggregation problem. The following work is named here so it doesn't drift. It should land within ~6 weeks of V0 shipping, before the second source-tagged feature (likely V1's auto-scan, or trip-story-derived signal extraction) hits production.

### Migrate the ~20 existing `create_observation` call sites

The investigation surfaced unstructured `provenance` JSONB across `backend/` — `memory_interaction` (`backend/core/memory_signal.py:62`), `invite_intake` (`backend/api/routes/invites.py:1072`), `intake` (`backend/api/routes/users/constraints.py:199`), `dna_phrase_dispute` / `profile_fact_dispute` (`backend/api/routes/users/me.py:304, 355`), and a dozen others.

For each: classify whether the observation has a meaningful source artifact (trip, conversation, dispute, invite). Populate the typed `source_artifact_type` and `source_artifact_id` columns. Backfill existing rows from the JSONB where the mapping is unambiguous; leave others null.

Add a lint rule or test that fails new `create_observation` calls missing the typed columns when a source artifact is identifiable.

### Extend `traveler_intakes` to typed provenance

`traveler_intakes` already has `source_type TEXT` and an opaque `source_ref JSONB`. Migrate to the same typed-column pattern: `source_artifact_type` + `source_artifact_id`, with backfill from `source_ref` where derivable. The existing `source_type` column stays for backward compatibility but is deprecated in favor of the new columns.

### Address the aggregation lossiness

The hardest piece. `personal_memories.markdown_content` and `personal_memories.taste_dimensions` are LLM-synthesized aggregates with no per-source attribution. The synthesis prompt at `backend/concierge/refresh_memory.py:91` says *"Preserve existing understanding unless NEW observations contradict it"* — the LLM can re-emit signals it can no longer justify from current observations.

Three approaches, in increasing order of correctness:

1. **Synthesis prompt change.** Strengthen the prompt to require evidence from current observations for every emitted phrase or dimension reading. Soft fix, no data-model change. Probably 60–70% effective; ship with this hardening pass to narrow the eventual-consistency window.
2. **Per-dimension source attribution.** Extend `taste_dimensions` from flat values to `{ value, confidence, sources: [observation_ids] }`. Synthesis writes the source list; revoke recomputes by filtering deleted observation ids. Aggregation stays LLM-driven but provenance survives.
3. **Dimension recomputation pipeline.** Move taste-dimension extraction out of LLM synthesis entirely — deterministic pipeline over typed observations, followed by an LLM narrative pass that reads the dimensions. Per-source revoke becomes trivial. Cleanest long-term, largest scope.

Recommendation: ship #1 with this follow-up pass. Plan #2 if user testing reveals revocation still feels broken. Defer #3 unless DNA quality becomes a P0 concern.

### Unify the dispute mechanism

Today's dispute endpoints write counter-observations and re-synthesize. With per-source revocation in place, "dispute a phrase that originated from artifact X" can become a real revoke of that artifact's contributing observations. The endpoints preserve their current API (the frontend doesn't break) but route through the revoke helper when source attribution exists. Unified semantics; dispute stops being a separate code path.

### Scope estimate

| Work item | Days |
|---|---|
| Migrate ~20 existing `create_observation` call sites | 2–3 |
| `traveler_intakes` provenance migration | 1 |
| Synthesis prompt change (approach #1) | 0.5 |
| Per-dimension source attribution (approach #2, optional) | 4–5 |
| Dispute unification | 1–2 |
| **Total minimum (without #2)** | **~5–7 days** |
| **Total with approach #2** | **~10 days** |

Add an eval scenario: *"delete artifact, verify signal removed within N synthesis cycles."* This locks down the regression and gives the team a measurable bar for "revocation works."

## Locked Decisions

The three pre-V0 decisions are resolved:

1. **Backend subsystem:** new `backend/atlas/`. Clean separation from `concierge/`, `memory/`, and `home/`.
2. **Atlas tab:** new fourth tab in `app/(tabs)/_layout.tsx`. Honors the brief's commitment to Atlas as a first-class surface.
3. **Travel DNA per-source revocation:** does not exist today; V0 builds it.
   - Investigation: the existing Travel DNA pipeline tracks unstructured provenance in `observations.provenance` (JSONB) and `traveler_intakes.source_type`, but `personal_memories` (the synthesized aggregate) carries no provenance back-reference. The only delete-style operations today are `prune_observations` (soft-delete by id) and `reset_personal_data` (nuclear). The dispute endpoints (`me/dna-phrases/dispute`, `me/profile-fact/dispute`) are rebuttal, not revocation.
   - V0 ships: indexed provenance columns on `observations`, write-side discipline in the Atlas flow, a source-keyed soft-delete helper, and cascade-revoke on artifact DELETE. See Signal extraction above for the contract.
   - Known limitation: eventual consistency through LLM re-synthesis. Documented in Risks; surfaced in UX copy.

These decisions are locked. Engineering can start week 1.
