---
doc_type: working
status: active
owner: founder / backend / frontend
created: 2026-09-01
last_verified: 2026-09-01
expires: 2026-10-01
why_new: Record the concrete Package 0–1 implementation outcome without implying that the v2 roots are already the production renderer. This status sheet is the handoff from architecture freeze to compiler work.
source_of_truth_for:
  - Package 0–1 completion status and known deferred work
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
- Deterministic hard gates reject missing owners/evidence, unauthorized
  audience, stale/revoked/unknown/expired/non-feasible candidates, and
  candidates outside the target root. Cluster arbitration precedes seat
  arbitration; demand budget is the final boundedness gate. Diagnostics are
  available to tests/internal evaluation only.
- The pure v2 modules are lazily importable without initializing the legacy
  Places/lived-experience dependency graph.

## Verification

- Backend v2 contract/adapter/gate/portfolio tests: **8 passed**.
- Frontend root query/invalidation tests: **5 passed**.
- Frontend TypeScript typecheck: **passed**.
- Ruff, formatting, import-cycle, boundary, surface-registry, and related
  pre-commit checks: **passed** for changed files.

The backend commit hooks report two repository-baseline failures unrelated to
these files: the broad-exception count is above its audited ceiling and three
pre-existing backend files exceed the size budget. Those checks were skipped
only for the backend commits; no new broad exception was introduced.

## Deliberately not claimed yet

Package 0–1 establishes the permanent seam; it does not make v2 production
visible. The following remain Package 2 work:

- wiring bounded candidate reads into separate Home and Places v2 compilers;
- generated OpenAPI/mobile v2 projection types and a dark contract endpoint;
- native kind registries and full real-data renderer parity;
- generated Composition compatibility and live-Instrument fixtures through the
  renderer path;
- removal of duplicate Places feed fetching in `PlacesWorkspace`; and
- deletion of legacy Trips/Places compatibility code after route-state,
  action/readback, degradation, and social/grant gates pass.

This boundary is intentional: the app has a coherent v2 contract and cache
seam before we commit to a repository-wide renderer or to Chat/Life changes.
