---
doc_type: archive
status: archived
owner: founder / engineering
created: 2026-07-10
archived: 2026-07-10
why_new: Preserve the complete adjudicated investigation after durable decisions and contracts moved to canonical owners.
---

# Plan — Atlas V1 Engineering

> Adjudicated and archived 2026-07-10. Current truth lives in system charters, decisions, generated checks, and code.

> **Outcome (as of 2026-07-03):** 🔶 Partial — V1 core shipped; V1.1 (custom Expo module, burst grouping, Vision dedup, JournalingSuggestions) deferred pending a dev-client cutover decision.

Engineering plan for V1 of Atlas Photo Backfill. Companion to
`Travel App/docs/Brief - Atlas Photo Backfill.md` (product decisions) and
`docs/archive/2026-07/retired-live/Plan — Atlas V0 Engineering.md` (what V0 shipped). Read both first;
this document does not re-derive their decisions.

## Strategy — two stages, not one

The brief's V1 ("Local Candidate Detection") names several capabilities
that are not all accessible from managed Expo:

| Capability | Available in managed Expo? |
|---|---|
| Full-library scan (metadata only) | ✓ via `expo-media-library` |
| GPS + mediaSubtypes (`screenshot`, `panorama`, etc.) | ✓ |
| Limited-access permission + "Manage selection" sheet | ✓ |
| Burst grouping (`burstIdentifier`) | ✗ Swift-only |
| `PHPersistentChangeToken` (incremental rescan) | ✗ Swift-only |
| `VNGenerateImageFeaturePrintRequest` (dedup) | ✗ Swift-only |
| `VNDetectFaceRectanglesRequest` (quality proxy) | ✗ Swift-only |
| `JournalingSuggestionsPicker` (iOS 17.2+) | ✗ Swift-only |
| `BGAppRefreshTask` (background catch-up) | △ via `expo-background-fetch`, limited |
| Apple Foundation Models (iOS 18+, A17+) | ✗ Swift-only |

A monolithic V1 stalls on the custom Expo Module ("Swift-only" rows
above). Two-stage avoids that:

- **V1.0 — managed Expo expansion.** Full-library scan, real home/work
  inference, candidate dismissal, paginated Memory Inbox, scan history.
  Ships against the same Expo SDK 55 dev-client V0 uses. No native code.
- **V1.1 — custom Expo Module.** A new Swift module wrapping the
  capabilities above. Migrates V1.0's AsyncStorage scan-state to
  `PHPersistentChangeToken`, adds burst + Vision dedup, integrates
  `JournalingSuggestions` as the third Permission Strategy path.
- **V1.2 — polish.** Apple Foundation Models hybrid for image labeling
  on capable devices; eval-driven tuning of the home/work radius
  thresholds; sensitive-location blocklist hardening.

V1.0 and V1.1 can be built in parallel by two engineers. V1.2 is a
sequential follow-up.

## Scope

**In scope (V1.0 + V1.1 together):**

- Full-library auto-scan (no manual pick required to trigger)
- Candidates surfaced in the Memory Inbox over time, not only in-session
- Two-stage home/work suppression with real inference (replaces V0's
  profile-home stub)
- Incremental rescan — re-scanning doesn't re-process unchanged assets
- Burst grouping (one representative per burst before scoring)
- Visual dedup using Vision feature prints
- `JournalingSuggestions` integration as the third Permission Strategy
  path on iOS 17.2+
- Candidate dismiss / snooze affordances
- Background catch-up (best-effort)
- Paginated inbox endpoint

**Out of scope — deferred to V2+:**

- Cross-trip threading from imported trips (Concierge surface, not Atlas)
- Public sharing / `shareable` artifact state implementation
- Discover ranking influence from artifact-derived signals (V2)
- Apple Foundation Models hybrid (V1.2 polish; deferred)
- True incremental section-by-section LLM streaming (V0 plan defers this)

## V1.0 — managed Expo expansion

### User flow changes from V0

1. Onboarding wizard's "Find memories from photos" path now requests
   broad library access (V0 used limited). User can decline and fall
   back to V0's manual-pick path.
2. Scan runs in foreground with a real progress UI ("Scanning 1,243 of
   8,500 photos…"). Cancelable.
3. Result is N candidates surfaced as a list, not a hard cap at 5.
4. After scan, user lands on the Atlas tab with the Memory Inbox
   populated.
5. Subsequent app opens trigger an incremental rescan (timestamps
   newer than last scan) — typically <2 seconds, no progress UI shown.
6. Users can dismiss candidates they don't want. Dismissed candidates
   stay out of the inbox.

### Acceptance criteria

- [ ] User with 5,000+ photos can complete a first scan in ≤2 minutes
      foreground wall time on an iPhone 13 or newer
- [ ] Scan respects the brief's noise filters (screenshots, panoramas
      without GPS, etc. — V0 had this for selected photos; V1.0 enforces
      across the whole library)
- [ ] Home/work suppression infers location from the user's photo GPS
      clusters; works without any profile data
- [ ] Re-scan on next launch processes only new assets (timestamp >
      stored last_scanned_at), completes in <3 seconds for a 100-asset delta
- [ ] Candidate dismiss surface — `DELETE /api/atlas/candidates/{id}`
      removes from inbox, doesn't re-surface in subsequent scans
- [ ] Memory Inbox paginates with `limit + offset` (or `after_id` cursor)
- [ ] Scan can be canceled mid-progress (`AbortController` on the
      hydration loop)
- [ ] Low Power Mode skips the scan and surfaces a "Resume when charging"
      affordance

### Backend changes (light)

| Endpoint | Purpose |
|---|---|
| `DELETE /api/atlas/candidates/{id}` | Mark dismissed; idempotent |
| `GET /api/atlas/inbox?limit=N&after_id=X` | Pagination on the existing endpoint |
| `GET /api/atlas/scan-history` | Last-scanned timestamp per user; helps the client decide whether to rescan |

New Pydantic models:

```python
class CandidateDismiss(BaseModel):
    # Empty body — DELETE semantics. Defined for OpenAPI clarity.
    pass

class AtlasScanHistory(BaseModel):
    last_scanned_at: datetime | None  # ISO; null = never scanned
    asset_count_at_last_scan: int     # for change detection
    candidates_surfaced_total: int
    candidates_approved_total: int
    candidates_dismissed_total: int
```

Schema migration adds a new `atlas_scan_history` table — `(user_id PK,
last_scanned_at, asset_count_at_last_scan, …counters, updated_at)`.
Existing `atlas_candidates` table gets a new `dismissed` status value
(the existing CHECK constraint allows it via migration).

Estimated backend effort: 2 days.

### Frontend changes (most of the work)

New files:

- `hooks/useAtlasFullScan.ts` — full-library scan with progress
  callbacks, pagination through `getAssetsAsync`, cancellation
- `utils/atlasHomeWorkInference.ts` — pure function: takes the user's
  full asset GPS history, returns inferred home + work cluster centroids
  using DBSCAN + temporal weighting (overnight density = home,
  weekday 9-5 density = work)
- `utils/atlasIncrementalScan.ts` — read `last_scanned_at` from
  AsyncStorage, query assets newer than that, run the same clustering
  pipeline
- `app/atlas/inbox.tsx` — dedicated Memory Inbox screen (V0 just
  shows a section on the Atlas tab; V1.0 promotes it)
- `components/atlas/ScanProgressCard.tsx` — the foreground scan UI
- `components/atlas/InboxItem.tsx` — render one inbox row (pending
  candidate OR recent artifact), with dismiss affordance

Modified files:

- `hooks/useAtlasPhotoPicker.ts` — add a `loadAllPhotos()` method
  alongside `loadSelectedPhotos()` for the broad-access path
- `utils/atlasCluster.ts` — promote `MIN_CLUSTER_SIZE` to a parameter
  (3 for manual-pick, 15+ for auto-scan per the V0 plan's tiered thresholds)
- `app/atlas/scan.tsx` — wire the "Find memories from photos" button
  to the full scan flow (currently routes through manual-pick fallback)
- `app/(tabs)/atlas/index.tsx` — surface the new inbox screen via a
  "View all" link when there are >3 pending candidates
- `data/atlas.ts` — add `useDismissCandidate`, `useScanHistory`,
  paginated `useAtlasInbox`

AsyncStorage keys:

```
atlas:last_scanned_at      // ISO timestamp, set after every successful scan
atlas:last_asset_count     // helps detect "user deleted assets in Photos"
atlas:dismissed_local      // optimistic dismiss cache (server is source of truth)
```

### V1.0 acceptance for "real home/work inference"

The V0 plan committed to a two-stage filter (0–100m hard, 100–500m
soft, >500m none) with an empirical-calibration follow-up. V1.0 ships
the inference algorithm with the V0 plan's anchors (100m / 500m) and
the Brooklyn-weekly-shooter named regression test:

- [ ] Fixture: a synthetic 600-asset library where 400 photos sit
      within 200m of "home" (Brooklyn) across 8 months and 200 sit in
      Tokyo across 6 days. Expected output: home inferred at Brooklyn
      centroid; Tokyo trip surfaces as a high-confidence candidate;
      Lilia restaurant (clustered visits at 200m from home) surfaces
      as a Place Memory in the inbox, NOT in the primary "I found
      a few memories" view
- [ ] Fixture: a 200-asset library entirely within 300m of home —
      no candidates surface (the user has no travel-shaped memories)
- [ ] Calibration log: every scan records the inferred home/work
      centroids in dev mode so we can review samples and tune the
      thresholds before V1.1

### V1.0 sequencing — one engineer, 1.5 weeks

**Week 1 (5 days):**
- Day 1: backend migration + new endpoints + tests
- Day 2: full-scan hook + clustering threshold tuning
- Day 3: home/work inference utility + fixture tests
- Day 4: incremental scan + AsyncStorage state
- Day 5: dismiss + paginated inbox UI

**Week 2 (3 days):**
- Day 6: real-device testing against multiple library shapes
- Day 7: scan-progress UI polish + Low Power Mode handling
- Day 8: dogfood + adjust thresholds

## V1.1 — custom Expo Module

### Strategic decision: scaffold via `create-expo-module`

`npx create-expo-module@latest atlas-photokit` produces a complete
TypeScript wrapper + iOS Swift skeleton + EAS-friendly config plugin
that wires the `Info.plist` keys (`NSPhotoLibraryUsageDescription`,
`NSUserActivityTypes` for JournalingSuggestions). Lives inside the
Travel App repo at `modules/atlas-photokit/`. No separate package.

This is the moment the managed-Expo escape hatch ends. After V1.1
ships, all future Travel App builds require a dev-client.

### Swift surface (target)

```swift
public class AtlasPhotokitModule: Module {
  public func definition() -> ModuleDefinition {
    Name("AtlasPhotokit")

    // ── Change-token incremental scan ──────────────────────────────────
    AsyncFunction("loadChangeToken") { () -> String? in ... }
    AsyncFunction("saveChangeToken") { (token: String) in ... }
    AsyncFunction("assetsChangedSince") { (token: String?) -> [PhotoMetadata] in ... }

    // ── Burst grouping ──────────────────────────────────────────────────
    AsyncFunction("groupBursts") { (assetIds: [String]) -> [BurstGroup] in ... }

    // ── Vision feature prints (dedup) ──────────────────────────────────
    AsyncFunction("featurePrint") { (assetId: String) -> Data in ... }
    AsyncFunction("featurePrintDistance") { (a: Data, b: Data) -> Double in ... }

    // ── JournalingSuggestions picker (iOS 17.2+) ────────────────────────
    AsyncFunction("presentJournalingPicker") { () async throws -> [JournalingSuggestion] in ... }
    Function("journalingSuggestionsAvailable") { () -> Bool in ... }

    // ── Vision face detection (quality proxy) ──────────────────────────
    AsyncFunction("faceCount") { (assetId: String) -> Int in ... }
  }
}
```

TypeScript binding lives at `modules/atlas-photokit/src/index.ts`:

```typescript
export interface PhotoMetadata {
  id: string;
  timestamp: number;
  latitude: number | null;
  longitude: number | null;
  burstIdentifier: string | null;
  mediaSubtypes: string[];
  isFavorite: boolean;
}

export interface BurstGroup {
  burstIdentifier: string;
  representativeAssetId: string;  // the rep — favorite > center > first
  memberAssetIds: string[];
}

export interface JournalingSuggestion {
  kind: 'trip' | 'place_visited' | 'workout' | 'photo_memory' | 'other';
  title: string;
  startDate: string;
  endDate: string;
  assetIds: string[];           // PHAsset localIdentifiers
}

export function loadChangeToken(): Promise<string | null>;
export function saveChangeToken(token: string): Promise<void>;
export function assetsChangedSince(token: string | null): Promise<PhotoMetadata[]>;
export function groupBursts(assetIds: string[]): Promise<BurstGroup[]>;
export function featurePrint(assetId: string): Promise<Uint8Array>;
export function featurePrintDistance(a: Uint8Array, b: Uint8Array): Promise<number>;
export function presentJournalingPicker(): Promise<JournalingSuggestion[]>;
export function journalingSuggestionsAvailable(): boolean;
export function faceCount(assetId: string): Promise<number>;
```

### Acceptance criteria

- [ ] `npx create-expo-module atlas-photokit` scaffolds successfully
- [ ] Dev-client builds with the new module included
- [ ] `loadChangeToken` / `saveChangeToken` / `assetsChangedSince`
      round-trip correctly — second scan returns only assets added/changed
      since the first
- [ ] `groupBursts` collapses an iOS burst (10 rapid-fire shots) to one
      representative
- [ ] `featurePrint` returns a Data blob; `featurePrintDistance` between
      near-duplicates is <0.3, between dissimilar is >0.6
- [ ] `journalingSuggestionsAvailable()` returns true on iOS 17.2+,
      false otherwise
- [ ] `presentJournalingPicker` opens the system picker and returns
      whatever the user selected
- [ ] `Info.plist` keys land via config plugin (no manual Xcode edits)

### V1.1 integration with V1.0

After the module exists:

1. `utils/atlasIncrementalScan.ts` swaps AsyncStorage timestamp for
   `AtlasPhotokit.loadChangeToken()` / `saveChangeToken()`. The
   `assetsChangedSince` returns native PhotoMetadata which the existing
   clustering utility consumes after a thin adapter.
2. `utils/atlasCluster.ts` gains a "collapse bursts" pre-step using
   `groupBursts` — runs after the noise filter, before time bucketing.
3. New "dedup pass" runs `featurePrint` on representatives of high-density
   GPS clusters; near-duplicates collapse to one entry.
4. `useAtlasPhotoPicker.ts` gains a `pickJournalingSuggestion()` method
   wrapping `presentJournalingPicker()`. The scan wizard's Promise screen
   surfaces "See Apple's suggested trips" as a real, working option on
   iOS 17.2+.
5. Memory Inbox shows "Apple flagged this" badge on candidates merged
   from a JournalingSuggestion.

### V1.1 sequencing — one engineer, 2 weeks

**Week 1 (5 days):**
- Day 1: scaffold module, set up dev-client EAS build profile
- Day 2: implement `loadChangeToken` + `saveChangeToken` + `assetsChangedSince`
- Day 3: implement `groupBursts` + `faceCount`
- Day 4: implement `featurePrint` + `featurePrintDistance`
- Day 5: implement `journalingSuggestionsAvailable` + `presentJournalingPicker`

**Week 2 (5 days):**
- Day 6: TypeScript bindings + unit tests for the adapter layer
- Day 7: integrate change-token incremental scan into V1.0's flow
- Day 8: integrate burst + feature-print dedup
- Day 9: integrate JournalingSuggestions path in scan wizard
- Day 10: real-device end-to-end testing

## V1.2 — polish

Deferred to after V1.0 + V1.1 ship and user testing reveals the rough
edges. Named for completeness:

- **Home/work radius calibration** — replace the V0 plan's 100m / 500m
  anchors with empirically-derived values after ~5 real user libraries
  surface in beta. The V1.0 calibration log feeds this.
- **Apple Foundation Models hybrid** — on iPhone 15 Pro+ / 16+, shift
  photo-grounded labeling (scene captions, OCR) to AFM. Narrative
  synthesis stays on Claude. Hardware-gated; falls back to existing
  composer on older devices.
- **Sensitive-location blocklist hardening** — replace the V0 plan's
  conservative POI category lookup with a real blocklist + a hospital /
  funeral home / school radius filter. Calibrate against false positives.

## Cross-stage shared work

- **Backend `atlas_scan_history` table** lands in V1.0; V1.1 just writes
  to it through the same endpoints.
- **`useDismissCandidate` + paginated inbox** is V1.0 work; V1.1 inherits.
- **Memory Inbox surface (`app/atlas/inbox.tsx`)** lands in V1.0; V1.1
  adds the "Apple flagged this" badge variant.

## Risks and unknowns

- **`expo-media-library` performance at 10k+ assets.** Spike day 1.
  If `getAssetsAsync({ first: 10000 })` blocks the JS thread for too
  long, switch to paginated reads (`first: 500, after: cursor`). Plan
  assumes pagination is acceptable.
- **`PHPersistentChangeToken` serialization.** Apple's docs say it's
  `NSSecureCoding`-compatible but not stable across iOS versions. V1.1
  must persist it as Base64 + handle "token invalidated by OS" by
  falling back to a full rescan.
- **JournalingSuggestions capability provisioning.** Requires a paid
  Apple Developer entitlement (Journaling Suggestions Capability).
  Confirm the team's Apple Developer account has this before V1.1
  starts — otherwise day 5 stalls.
- **Vision feature-print performance.** Apple docs claim
  `VNGenerateImageFeaturePrintRequest` runs at ~10-20 ms per photo on
  modern iPhones. At 10k photos that's 100–200s of compute — too long
  for foreground. Run only on candidate-cluster representatives
  (~50–100 photos), not the full library. Plan reflects this scope.
- **Module + Expo SDK 55 compatibility.** SDK 55 modules use the
  `expo-modules-core` v3.x API. Confirm `create-expo-module@latest`
  generates SDK-55-compatible scaffolding (not the SDK-56 preview).
  Pin the scaffold version explicitly.
- **Low Power Mode + foreground scan UX.** Apple recommends not
  burning the battery in Low Power Mode. V1.0 should detect and
  defer (`isLowPowerModeEnabled` from React Native's `PowerState`).
- **Dismissed candidates re-surfacing.** Naive incremental scan
  would re-discover a candidate the user dismissed. Backend's
  `dismissed` status needs to be checked client-side before submitting
  fresh candidates, OR backend must de-duplicate against dismissed
  candidates from the same date+place cluster.

## Decisions needed before V1.0 starts

1. **Dev-client cutover timing.** V1.1 requires moving the entire app
   from managed Expo to a custom dev-client. Confirm with the release
   team that this is acceptable for the V1.1 timeframe and doesn't
   collide with TestFlight builds.
2. **JournalingSuggestions entitlement.** Confirm the Apple Developer
   team account has been granted the capability, or start the request
   now (Apple's review can take a week).
3. **Memory Inbox primary placement.** V0 surfaces inbox as a section
   on the Atlas tab. V1 promotes it. Should it be:
   - **A**: A "View all" link from the Atlas tab leading to a dedicated
     `app/atlas/inbox.tsx` (recommended; preserves Atlas as the gift surface)
   - **B**: A dedicated tab in `(tabs)/_layout.tsx` (would be 5 tabs total)
   - **C**: A modal triggered by a notification bell on the Atlas tab
4. **Scan trigger UX.** Two options:
   - **A**: Background-only — scan runs silently on app open + every N
     hours; user only sees results in the inbox (recommended)
   - **B**: Foreground-only — scan runs only when user taps "Look for
     new memories"; gives the user full control
   - **C**: Both (auto + manual button)

Recommendations: 3A, 4A.

## Follow-up — DNA Provenance Hardening (still pending)

V0 deferred the broader provenance work documented in
`docs/archive/2026-07/retired-live/Plan — Atlas V0 Engineering.md` §Follow-up. V1.0 does not touch
that scope. V1.1 also does not. Schedule it as a parallel backend
sprint OR fold into V1.2 polish.

## Status when V1 ships

| Capability | V0 | V1.0 | V1.1 |
|---|---|---|---|
| Manual photo pick (the brief's "Choose photos myself") | ✓ | ✓ | ✓ |
| Full-library auto-scan (the brief's "Find memories from photos") | — | ✓ | ✓ |
| Apple-Suggested via JournalingSuggestions (iOS 17.2+) | — | — | ✓ |
| Real home/work inference | — | ✓ | ✓ |
| Burst grouping | — | — | ✓ |
| Vision feature-print dedup | — | — | ✓ |
| Incremental rescan | — | ⚠ AsyncStorage approximation | ✓ Native change token |
| Background catch-up | — | — | ✓ via BGAppRefreshTask |
| Memory Inbox as first-class surface | — | ✓ | ✓ |
| Candidate dismiss | — | ✓ | ✓ |
| Paginated inbox | — | ✓ | ✓ |

After V1 ships, the brief's V0–V3 rollout has covered V0 (manual) + V1
(local detection). V2 (Artifact-To-App Personalization) and V3 (Ongoing
Memory Inbox enrichment loop) follow.
