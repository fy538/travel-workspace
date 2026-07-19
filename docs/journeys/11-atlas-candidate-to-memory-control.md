# 11 - Atlas Candidate To Memory Control

> Status: draft  
> Owner: founder / engineering  
> Last updated: 2026-07-19
> Primary phase: memory / identity control / trust hub

> **Current Atlas IA:** This cross-repo journey certifies the candidate and
> memory-control trust loop. Its older route inventory below is not the current
> Atlas-internal journey map. Use
> [`../../travel-app/docs/user-flows/atlas-journeys.md`](../../travel-app/docs/user-flows/atlas-journeys.md)
> for the six current journeys that begin and end inside Atlas.

## Product Promise

Atlas should make Vesper's memory inspectable and controllable: users can see what was learned, keep or reject candidates, inspect provenance, and change their mind.

## Canonical User Story

As a traveler, I want to review a memory candidate, turn it into an artifact if I want, and control the signals Vesper learns from it.

## Why This Journey Matters

- Atlas is now a primary tab, not a settings page.
- Memory without provenance or control will feel creepy.
- Timeline, Almanac, and entry controls are now backed by persisted projection rows — mock-derived local logic should not drift from `GET /api/atlas/timeline` and `GET /api/atlas/almanac`.

## Starting State

- Persona: returned traveler or user with pending Atlas candidate.
- Trip state: recently returned trip or saved/memory-rich history.
- Fixture: Dev "Just back" persona with Athens candidate; Atlas inbox/candidate/artifact data.
- Permissions: photo scan variants need photo permission; base candidate flow does not.

## Primary Surfaces

- Routes: `/(tabs)/atlas`, `/atlas/inbox`, `/atlas/candidate/[id]`, `/atlas/artifact/[id]`, `/atlas/learned/[id]`, `/atlas/receipt`, `/atlas/dna`, `/atlas/privacy`, `/atlas/long-view`, `/atlas/postcards`, **`/atlas/profile`**, **`/atlas/account`**, **`/atlas/constraints`**, **`/atlas/data-receipt`**, **`/atlas/delegation`**, `/atlas/companions`, `/atlas/removed`.
- App docs: [Atlas Home](../../travel-app/docs/page-specs/atlas-home.md), [Atlas Backend Contracts](../../travel-app/docs/page-specs/atlas-backend-contracts.md), [Atlas Signal Controls](../../travel-app/docs/page-specs/atlas-signal-controls.md), [archived Me/Account → Atlas trust investigation](../archive/2026-07/retired-live/me-account-atlas-trust-investigation-2026-06-25.md).
- Existing anchors: `__tests__/utils/atlasCluster.test.ts`, `__tests__/data/memory.test.ts`, `__tests__/components/memory/DNAStrip.test.tsx`, `__tests__/screens/personal-memory.smoke.test.tsx`, **`__tests__/screens/atlas-long-view.smoke.test.tsx`**, **`__tests__/components/atlas/AtlasYearStepper.test.tsx`**.

## Canonical Steps

1. Open Atlas Home — year ribbon uses newest travel year from timeline summary, then loads Almanac for that year.
2. Open Inbox or desk candidate.
3. Open candidate detail.
4. Choose Keep and select style, or choose Not this time.
5. If kept, land on artifact detail.
6. Open learned signals.
7. Keep, dispute, or forget a signal.
8. Open full receipt and privacy controls.
9. Open **Almanac** or **Timeline** and confirm entries, year stepper, hide/pin/rename controls.
10. Return to Atlas Home/Postcards/Map and confirm state updates.
11. **Trust hub:** from Atlas monogram → `/atlas/profile` → exercise constraints, data-receipt (privacy audit), delegation, account/export, and following/people — Me tab is removed; these routes are canonical.

### Journey 12 boundary

Post-trip **completed-record entry, story compose, Memory, and settlement
closeout** live in Journey 12. This journey owns memory **control and
provenance**, not the narrative arc.

## Required Branches

The six established Atlas-internal journeys are registered here as branch
trials so their existing evidence no longer collapses into one binary J11 cell.
The coverage refresh will decide which durable outcomes should receive their own
global journey IDs.

| Branch | Atlas outcome | Required evidence | Current assessment |
|---|---|---|---|
| `J11.B01` | Empty/provisional Atlas → first grounded saved place or weak prior → useful Home | `FE`, `BE`, `VIS`, `LIVE` | Certified through J25 first-value save, Home projection, and native return |
| `J11.B02` | Review candidate → keep/refine/dismiss → updated queue/artifact | `FE`, `BE`, `VIS`, `LIVE` | Certified through native keep/dismiss and lived candidate-to-artifact grounding |
| `J11.B03` | Open/compose Reading → steer → keep → shelf/Home return | `FE`, `BE`, `VIS`, `LIVE` | Certified through J26 compose, provenance, keep, shelf, and return evidence |
| `J11.B04` | Inspect provenance → correct/soften/forget → originating surfaces reconcile | `FE`, `BE`, `VIS`, `LIVE` | Certified through J27 source-preserving correction/forget reconciliation |
| `J11.B05` | Browse time/place history → hide → Removed → restore to original chapter | `FE`, `BE`, `VIS`, `LIVE` | Certified through J28 native and lived hide/restore/archive-reason evidence |
| `J11.B06` | Grounded timely return → open source → dismiss/expire → slot retires | `FE`, `BE`, `VIS`, `LIVE` | Certified: native open/dismiss plus lived Unpacked postcard grounded by approved artifact |

Existing native anchors:

- `atlas-journey-place-save-return.yaml` → `J11.B01`
- `atlas-journey-review-dismiss-return.yaml` → `J11.B02`
- `atlas-journey-reading-keep-return.yaml` → `J11.B03`
- `atlas-journey-memory-forget-return.yaml` → `J11.B04`
- `atlas-journey-archive-hide-restore.yaml` → `J11.B05`
- `atlas-journey-timely-return-open-dismiss.yaml` → `J11.B06`

See [Atlas canonical internal journeys](../../travel-app/docs/user-flows/atlas-journeys.md)
and [Branch-Level Journey Certification Model](BRANCH_CERTIFICATION_MODEL.md).

## Certification Record

- 2026-07-19: all seven registered Atlas native flows passed on iPhone 16 Pro (iOS 18.2), covering first value, review/dismiss, Reading keep/return, forget, hide/restore, and timely-return retirement.
- 2026-07-19: `persona-cert:J11` and `persona-cert:J25`–`J28` passed against disposable real-backend fixtures. J11 now proves the approved candidate is exposed by `/api/atlas/unpacked` as a postcard grounded in the created artifact.
- Branch fidelity after this pass: `FE 6/6`, `BE 6/6`, `VIS 6/6`, `LIVE 6/6`.

## Expected Outcome

- User-visible state: candidate/artifact/signal status is clear and reversible where appropriate.
- Data state: candidate approval creates or links artifact; signal decisions persist; overlapping trip rows dedupe to artifact in timeline/almanac read models.
- Cross-surface coherence: Inbox, Home, Almanac, Timeline, Map, Postcards, DNA, and Receipt agree.
- Trust state: user can see why Vesper learned something and can dispute/forget it.

## Timeline / Almanac / Controls — Unblocked (2026-06)

| Surface | Backend | App | Tests |
|---|---|---|---|
| Timeline / Almanac (`GET /api/atlas/timeline`, `GET /api/atlas/almanac`) | Persisted projection + grouped horizon data | `/atlas/long-view?mode=time` | `tests/atlas/test_timeline_pagination_integration.py`, `tests/atlas/test_atlas_timeline.py`, `__tests__/screens/atlas-long-view.smoke.test.tsx` |
| Entry controls (hide/pin/rename/restore) | `PATCH` + `POST …/hide` + `POST …/restore` + `archive_reason` | Bottom sheet on Almanac/Timeline; removed-moments screen | `tests/atlas/test_timeline_archive_reason.py`, `tests/atlas/test_timeline_removed.py`, `__tests__/screens/atlas-removed.smoke.test.tsx` |
| Removed moments audit | `GET /api/atlas/timeline/removed` | `/atlas/removed` (linked from Privacy) | `tests/atlas/test_timeline_removed.py`, `__tests__/screens/atlas-removed.smoke.test.tsx` |
| Trip ↔ memory dedup | Projector + reconcile on artifact delete | Read path shows one visible entry; removed screen for folded trips | Postgres canary below |

### Dedup + restore scenarios (Postgres canary)

`tests/dogfood/test_atlas_dedup_canary.py`:

1. **Approve overlapping memory** — trip + candidate overlap → trip projection archived (`archive_reason=dedup`), artifact visible; timeline and almanac each show one `kept_memory` entry.
2. **Delete artifact via HTTP** — archived trip restores to `visible`; timeline shows trip again.
3. **Reconcile after memory removed** — same restore semantics when artifact projection is removed and reconcile runs.

User-initiated hides (`archive_reason=user`) are **not** restored by reconcile — see `test_timeline_archive_reason.py`.

### Staging note: projection version rebuild

`TIMELINE_PROJECTION_VERSION = 4` (`backend/atlas/projection_meta.py`). Existing users rebuild lazily on first timeline/almanac access via `ensure_timeline_projected`. After deploy, spot-check one legacy account: open Almanac, confirm entries appear and year list matches expectations.

**Automated spot-check (Postgres):** `tests/atlas/test_projector_integration.py::test_legacy_projection_v4_first_timeline_almanac_access`.

**Manual spot-check (~15 min, optional):** on a **legacy staging account** that predates projection v4 (pre-deploy rows in `atlas_timeline_projection_meta` with version &lt; 4, or no projection row yet). Use a real device or simulator pointed at staging; do not use mock API.

| # | Surface | Pass criteria |
|---|---|---|
| 1 | **Atlas Home** | Tab loads without error; year ribbon shows a year; desk shows draft **or** kept postcard (not blank when artifacts exist); shelf map count roughly matches **Map** hero. |
| 2 | **Almanac** (first open) | Lazy v4 rebuild completes; year stepper lists expected years; month groups populate (not permanently empty for an active account). |
| 3 | **Timeline** (same year) | Entries match Almanac grouping; no duplicate trip + kept-memory pair for the same trip after dedup. |
| 4 | **Map** (same year) | Vertical spine + header year stepper agree with Almanac year; pins match backend geography (trips/saves/artifacts); **OPEN ALMANAC** / **FULL TIMELINE** deep-link correctly. |
| 5 | **Privacy → Removed moments** | Archived rows show reason; restore one user-hidden entry if present; entry reappears on Timeline/Almanac. |
| 6 | **Candidate loop** (optional) | Approve or dismiss a pending candidate; Home desk + Inbox count update within one focus cycle; artifact/learned routes open. |

Record account id + date in staging notes when complete. If step 2 fails, check API logs for `ensure_timeline_projected` errors before filing a bug.

## Mock walk (2026-06)

With `EXPO_PUBLIC_USE_MOCK_API=true`, Journey 11 screen coverage:

| Step | Screen | Test |
|---|---|---|
| Candidate review | `/atlas/candidate/[id]` | `__tests__/screens/atlas-candidate.smoke.test.tsx` |
| Artifact detail | `/atlas/artifact/[id]` | `__tests__/screens/atlas-artifact.smoke.test.tsx` |
| Learned signals | `/atlas/learned/[id]` | `__tests__/screens/atlas-learned.smoke.test.tsx` |
| Postcards shelf | `/atlas/postcards` | `__tests__/screens/atlas-postcards.smoke.test.tsx` |
| Inbox review queue | `/atlas/inbox` | `__tests__/screens/atlas-inbox.smoke.test.tsx` |
| Atlas Home (desk + ribbon + shelf) | `/(tabs)/atlas` | `__tests__/screens/atlas-home.smoke.test.tsx` |
| Long View (Time + Places) | `/atlas/long-view` | `__tests__/screens/atlas-long-view.smoke.test.tsx` |
| Timeline entry menu | Almanac/Timeline bottom sheet | `__tests__/components/atlas/AtlasTimelineEntryMenu.test.tsx` |
| Receipt + privacy | `/atlas/receipt`, `/atlas/privacy` | `__tests__/screens/atlas-receipt.smoke.test.tsx` |
| Removed moments | `/atlas/removed` (+ links from Privacy, Almanac, Timeline) | `__tests__/screens/atlas-removed.smoke.test.tsx` |
| End-to-end mock walk | inbox → candidate → artifact → learned → privacy → almanac → timeline | `__tests__/journeys/journey-11-mock-walk.smoke.test.tsx` |

## Must Never Happen

- Candidate approval creates duplicate artifacts.
- Forget/dispute says success but signal still appears as active.
- Artifact generation spinner never resolves or strands the user.
- Atlas privacy controls mutate generic account settings without memory-specific clarity.
- Photo scan uploads original/private data before explicit approval.
- Overlapping trip + kept memory both appear as separate visible timeline/almanac entries.
- Deleting a kept memory leaves the linked trip permanently archived.

## Deferred / Later

- **Live almanac LLM smoke** (`tests/atlas/test_almanac_llm_live.py`): excluded from CI via `@requires_api_keys`; offline checks in `test_almanac_llm_checks.py` gate mock output. Manual run: `cd travel-agent && PYTHONPATH=. pytest tests/atlas/test_almanac_llm_live.py -m requires_api_keys`.
- **Map region/country count**: backend reports `region_count=0` until a real country signal exists; frontend omits the clause when zero.

## AI Trace Prompt

```text
Trace Atlas candidate approval and signal control from home/inbox through candidate, artifact, learned signals, receipt, DNA, almanac, timeline, map, privacy, and trust hub routes (profile, account, constraints, data-receipt, delegation, following). Verify GET /api/atlas/facets returns `suggestions` (not `facets`) end-to-end. Identify local derivations versus backend contract endpoints, dedup/restore on overlapping trip+memory, and orphan routes.
```

## First Automation Target

Atlas state regression:

- candidate keep -> artifact route
- candidate dismiss removes from inbox/home desk
- signal keep/dispute/forget persists
- receipt/privacy route reachable
- map/postcards reflect artifact state
- **overlapping trip + approve memory -> one timeline/almanac entry**
- **artifact delete -> trip restored in timeline**
- **almanac horizon section + year stepper + timeline error/empty states**
- **map year spine (Direction 03) + almanac deep link**
- **candidate detail + learned-signal screen tests**
- **privacy → removed moments link + restore flow** (Privacy, Almanac, Timeline)
- **inbox + receipt + artifact + postcards smoke coverage**
- **timeline entry menu hide/pin/rename component tests**

## Real-backend checklist

| Check | Command / test | CI |
|---|---|---|
| Dedup + restore canary | `pytest tests/dogfood/test_atlas_dedup_canary.py -m requires_postgres` | yes (`test-db` job + named Atlas canary step) |
| Projection v4 first-access backfill | `pytest tests/atlas/test_projector_integration.py::test_legacy_projection_v4_first_timeline_almanac_access -m requires_postgres` | yes (`test-db` job + named Atlas canary step) |
| Map year filter + honest summary | `pytest tests/atlas/test_atlas_map.py` | yes (`test-db` job + named Atlas canary step) |
| Home read model (pending previews, unified place count) | `pytest tests/atlas/test_atlas_home.py` | yes (`test-db` job + named Atlas canary step) |
| Almanac LLM output gates (offline) | `pytest tests/atlas/test_almanac_llm_checks.py` | yes |
| Almanac LLM live smoke | `pytest tests/atlas/test_almanac_llm_live.py -m requires_api_keys` | no — run manually when keys available |
### Atlas subjourneys protected by J11

J11 contains two connected spines rather than a second journey registry:

1. **Read spine:** cold/empty Atlas → lean-back board → compose/steer → save and
   return through Ways Back In.
2. **Memory spine:** manual or eligible automatic scan → candidate review → explicit
   keep → provenance/correction/privacy controls.

Long View, recap, re-engagement, and immersive playback are supporting surfaces.
They do not pass J11 if candidate approval, provenance, dispute, forget, or restore
is broken. Auto-candidate creation remains dark until its privacy and exactly-once
contracts are certified.
