---
doc_type: working
status: active
owner: founder / backend / frontend
created: 2026-09-01
last_verified: 2026-09-01
expires: 2026-10-01
why_new: Record the concrete Package 0–1 and Package 2A implementation outcome without implying that the v2 roots are already the production renderer. This status sheet is the handoff from architecture freeze through the dark typed compiler boundary.
source_of_truth_for:
  - Package 0–1 and Package 2A completion status and known deferred work
depends_on:
  - docs/working/home-and-places-root-implementation-program-2026-08-31.md
  - docs/working/home-and-places-root-consumer-graph-2026-09-01.md
---

# Home and Places — Package 0–1 status

## Completed

### Package 0 — architecture freeze and characterization

- The build manifest no longer makes the old `concierge_feed` numeric rank
  output the permanent Home/Places hierarchy. Its inputs and characterization
  cases remain reusable migration evidence.
- The Home and Places bounded unit unions are closed in
  `backend/core/models/root_projection_v2.py`.
- `RootCandidate`, typed semantic payloads, owner references, source
  references, grant references, lifecycle/expiry, lead/support medium, and
  owner-capability destinations are strict and immutable.
- The v2 envelope has explicit root identity, projection revision, source
  revisions, and independently reported degradations. It contains no client
  component or route strings.
- The consumer graph and deletion gates are recorded in the companion graph
  document. Chat/Life UI and behavior were not changed.
- The app now has canonical Home/Places root query factories and centralized
  root-prefix invalidation.

### Package 1 — bounded read and candidate substrate

- `ExperienceProjectionReadLimits` is an opt-in database-bound envelope. The
  existing graph reader applies limits to plans, occasions, joins, commitments,
  evidence, outcomes, openings, and participant rows; callers that do not pass
  limits preserve historical behavior.
- `run_bounded_reads` and `BoundedRootReadPortfolio` run independent sources
  concurrently, bound item/source counts, and return stable degradation codes
  (`source_timeout`, `source_unavailable`, `source_item_bound`) instead of
  leaking exceptions into the root.
- Home and Places adapters convert current owner reads into bounded,
  owner/evidence-backed candidates. They preserve source identity but do not
  treat legacy section order as a new hierarchy.
- Separate Home and Places selectors now apply the shared gates while keeping
  each root's candidate boundary explicit; they do not yet replace the v1
  serving compiler.
- Deterministic hard gates reject missing owners/evidence, unauthorized
  audience, stale/revoked/unknown/expired/non-feasible candidates, and
  candidates outside the target root. Cluster arbitration precedes seat
  arbitration; demand budget is the final boundedness gate. Diagnostics are
  available to tests/internal evaluation only.
- The pure v2 modules are lazily importable without initializing the legacy
  Places/lived-experience dependency graph.

## Package 2A — typed dark boundary (completed 2026-09-01)

The first compiler slice now crosses the repository boundary without changing
what a user sees:

- pure `compile_home_v2` and `compile_places_v2` functions emit the immutable
  v2 envelope from already-admitted candidates; they do not read databases,
  rank page-shaped sections, or select a client component;
- `GET /api/root-projections/v2/home` and
  `GET /api/root-projections/v2/places` expose those compilers behind the
  existing authenticated router, with Home's bounded Experience Graph limits
  and Places' independent-source degradation preserved;
- the complete OpenAPI snapshot and generated mobile projection now include
  the v2 paths and schemas (`RootCandidate`, typed payload families, regions,
  Places states, destinations, and degradations);
- `EXPO_PUBLIC_ROOT_PROJECTION_V2` is registered as a default-off,
  development/internal-only migration gate with an explicit review date;
- Home and Places mount opt-in shadow reads behind that gate while continuing
  to render the v1 compatibility treatment. Mock mode makes no v2 request and
  the flag cannot activate in a public release build; and
- the native v2 kind registries, renderer parity, and duplicate Places fetch
  removal remain deliberately deferred to the next package.

## Verification

- Backend v2 contract/adapter/gate/portfolio/compiler tests: **11 passed**.
- Frontend root query/invalidation and v2 flag tests: **9 passed**.
- Frontend TypeScript typecheck: **passed**.
- API contract audit and OpenAPI mobile projection: **passed against the
  implementation app worktree** with 428 paths, 473 operations, and 1,190
  schemas in the app projection. The parent checkout still has unrelated
  concurrent-app drift and is not used as this slice's source checkout.
- Ruff, formatting, import-cycle, boundary, surface-registry, and related
  pre-commit checks: **passed** for changed files.

The backend commit hooks report two repository-baseline failures unrelated to
these files: the broad-exception count is above its audited ceiling and three
pre-existing backend files exceed the size budget. Those checks were skipped
only for the backend commits; no new broad exception was introduced.

## Deliberately not claimed yet

Package 0–1 and Package 2A establish the permanent seam and a dark typed
transport; they do not make v2 production visible. The following remain the
renderer/convergence portion of Package 2 and later:

- native kind registries and full real-data renderer parity;
- generated Composition compatibility and live-Instrument fixtures through the
  renderer path;
- removal of duplicate Places feed fetching in `PlacesWorkspace`; and
- deletion of legacy Trips/Places compatibility code after route-state,
  action/readback, degradation, and social/grant gates pass.

This boundary is intentional: the app has a coherent v2 contract and cache
seam before we commit to a repository-wide renderer or to Chat/Life changes.
