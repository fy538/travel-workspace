# Dead-Code & Code-Health Inventory — Automated Pass

> Status: phase 1 (automated tooling) complete — needs triage
> Owner: founder / engineering
> Created: 2026-07-02
> **Correction (2026-07-02, later same day):** the "Unused files" list below flagged the
> `components/ui/state/*` cluster (12 files) as dead legacy code superseded by something newer.
> That was backwards — those files were the *new*, in-progress state-system migration, sitting
> uncommitted at scan time (knip saw them on disk but their consumer wiring wasn't committed
> yet, so nothing resolved as "used"). They've since been reviewed and committed
> (`feat(design): app-wide state-system migration`, travel-app). Treat every "unused" finding
> below with the same caution — this repo has multiple concurrent agent sessions landing large
> uncommitted diffs; a knip/vulture snapshot is a point-in-time read, not a verdict.
> Tools: knip 5.x (travel-app), vulture 2.16 (travel-agent), custom import-graph + reverse API-coverage scripts, `gh run list`/`gh run view`
> Raw outputs: session scratchpad (`vulture-60.txt`, `knip.txt`)

## ⚠️ HEADLINE FINDING: CI on travel-app has had zero effective signal since 2026-05-13

The 6-broken-test finding below was the tip of the iceberg. **Every CI run on `main` — both
`push` and `pull_request` triggers, 294 of the last 300 runs — has failed since 2026-05-13.**
That's ~50 days and roughly 900 commits' worth of merges that landed with red checks. This
isn't caught by branch protection because branch protection requires GitHub Pro on a private
repo, which this isn't — so CI has been purely advisory (and silently ignored) this whole time.

**Five independent root causes, currently all failing simultaneously on `main` HEAD:**

| Job | Root cause | Fix effort | Owner |
|---|---|---|---|
| `logic-qa` | "Check out travel-agent" step gets `Not Found` — `secrets.TRAVEL_AGENT_CI_TOKEN` is unset/invalid and the default `GITHUB_TOKEN` can't check out a second private repo | 5 min (mint a PAT, add repo secret) | **owner-only** |
| `qa-tooling` | Workflow bug: this job runs `npm run qa:logic:check-drift`, which needs a sibling `travel-agent` checkout, but the job **never checks it out** — missing step, unlike the `logic-qa` job which has it. Copy-paste omission. | 5 min (add the same checkout step) | engineering |
| `contract-types` | Real drift: `utils/api/schema.gen.ts` is stale vs `docs/openapi.json` — the exact contract `CLAUDE.md` says "there is no second snapshot to drift against" | 2 min (`./scripts/sync-types.sh` + commit) | engineering |
| `lint` | Real bugs: `useGatedMutation` and `useEffect`/`useState` called **conditionally** in `BlockProposedBanner.tsx` and `DeckCallFace.tsx` (Rules-of-Hooks violations — can cause real runtime state bugs), plus a banned raw `Image` import in `RisoSlotImage.tsx` bypassing the `AppImage` cache wrapper | ~30–60 min | engineering |
| `test` | **37 of 313 suites failing, 103 of 2,246 tests failing.** Mixed causes: (a) hard import failures from components deleted in the June 19/21/28 refactors (the 6 tests found in phase 1), (b) real regressions — `useTripsList is not a function`, `useFocusEffect is not a function` (context/mock drift), (c) UI-copy assertion drift (expected strings no longer match current copy), (d) behavioral/logic drift in utils tests | hours, needs triage per failure class | engineering |

**Why this matters more than the dead-code cleanup below:** for the last ~50 days, the
project's only backstop against regressions has been Claude Code sessions running tests
locally/ad hoc — not the CI gate the docs describe. Any regression introduced in a session
that didn't happen to run the full suite could be sitting on `main` right now, undetected.
This is worth fixing **before** or **alongside** the dead-code purge, not after — a green CI
is also the safety net that makes the dead-code deletions below low-risk to execute.

**Recommended sequencing:** owner mints `TRAVEL_AGENT_CI_TOKEN` PAT (unblocks 2 of 5 jobs) →
engineering fixes `contract-types` (2 min) → fixes the 2 hook violations + banned import (real
bugs, not busywork) → triages the 37 failing suites by root-cause bucket, starting with the
6 known dead-import failures → re-baseline. Only then start deleting the 71 unused files, so
each deletion is verified against a CI that's actually running.

### 2026-07-02 update — session progress + the rest of the true scope

**Fixed and committed** (travel-app: `28d4040`, `c239fdf`; workspace: `696bb81`):
- `contract-types` job: `docs/openapi.json` regenerated — was stale against a backend docstring
  change. Zero `schema.gen.ts` diff confirms this was the only drift.
- `lint` job / `expo lint` step: 0 errors (was 3) — the 2 Rules-of-Hooks violations and the
  banned `Image` import, all fixed for real, not suppressed.
- `lint` job / `date-parse-guard` step: 0 violations (was 1) — routed through the existing
  `formatDate()` helper instead of hand-rolling.
- `qa-tooling` job: added the missing `travel-agent` checkout step (copy-paste omission vs.
  `logic-qa`). Verified locally with `TRAVEL_AGENT_DIR` set — script passes 17/17.

**Still blocking `lint` from going green — sized, not yet touched:**

GitHub Actions only shows steps *after* the first failure once you fix the one blocking it,
which is how these stayed invisible. All four are hardcoded `BASELINE` ratchets in their own
script files (`scripts/check-*-budget.mjs`) with an explicit "raise BASELINE with sign-off if
you genuinely need it" comment — i.e. these are meant to be a founder call, not something to
silently bump.

| Check | Current vs. baseline | Scope | Risk to fix blind |
|---|---|---|---|
| `typography-budget` | 16 vs 15 (**1 over**) | 8 files; 5 in one dev-only debug overlay (`components/dev/QueryHealthOverlay.tsx` — zero product risk) | Low — closing just the dev-only ones clears it |
| `color-budget` | 61 vs 49 (**12 over**) | ~26 files across product surfaces (trip map, trips home, Atlas) | Medium — wrong semantic token = visible color drift |
| `shadow-budget` | 27 vs 21 on clean HEAD (**6 over**; 36 in the dirty tree — +9 more uncommitted) | ~22 files | Medium — same risk class |
| `spinner-budget` | 66 vs 43 (**23 over**) | ~35 files, `<ActivityIndicator>` → `<Skeleton*>` swaps | Medium — different loading-state visual, needs a look |
| `api-boundaries` | 5 files not on the allowlist | `MakePostcardButton.tsx`, `StoryListenButton.tsx`, `BlockProposedBanner.tsx`, `ConflictResolutionSheet.tsx`, `TripDebriefSheet.tsx` import `api` directly instead of going through `data/`/`hooks/` | **High** — the allowlist comment says the intended fix is a real refactor onto the data/hooks layer, not a bigger allowlist |
| `size-budgets` | `components/trip/TripFolioHome.tsx` at 4,874 lines vs. 3,200 budget | 1 file | **High** — a real split, not mechanical |

None of the four numeric ratchets are new debt from this session or from the uncommitted
tree (verified against clean HEAD via `git stash`) — this is pre-existing drift that
accumulated during the 50 days CI provided no signal. Total remaining surface: **~190
individual raw-value instances across ~50 files, plus 2 real refactors** (a 5-file
architecture boundary fix and a 4,874-line file split). This is not "quick fixes" — treat
each of the 6 rows above as its own scoped task with visual verification, not a single pass.

**Still blocking `test` and `logic-qa`/`qa-tooling`'s auth step — unchanged, not attempted
this session:**
- `logic-qa` + `qa-tooling`: both need a valid `TRAVEL_AGENT_CI_TOKEN` repo secret — owner-only,
  ~5 min once a PAT is minted (Settings → Developer settings → Fine-grained tokens → grant read
  access to `travel-agent`).
- `test` job: 37/313 suites, 103/2,246 tests still failing. Root-cause buckets: 6 dead-import
  suites (known, phase-1 finding), several real regressions (`useTripsList is not a function`,
  `useFocusEffect is not a function` — likely context/mock drift), and a larger tail of
  UI-copy assertion drift (expected strings no longer match current copy). Needs its own
  triage pass — not attempted this session.

**New, unrelated finding surfaced while checking a clean baseline:** `git stash` revealed
**55 uncommitted files in `travel-app` and 35 in `travel-agent`** sitting in the working tree
right now — none of it ever exercised by CI. This is the same gap `mvp-scope-and-flag-manifest-2026-06-30.md`
flagged as "~12 BE / ~23 FE uncommitted, branch/commit before next build" two days ago; it has
roughly tripled since. One concrete casualty already found inside it: `app/booking/[sessionId].tsx`
has a real TypeScript error (`Property 'subtitle' does not exist on type '{ title: string }'`)
that doesn't exist on clean HEAD — i.e. there's already an uncommitted, unreviewed type error
sitting in local state. Not fixed here — out of scope of this pass, and not safe to touch
blind inside someone else's in-progress work.

## Headline numbers

| Signal | travel-app | travel-agent |
|---|---|---|
| Unused files | **71 files / 9,436 LOC** (knip) | 4 orphan modules (~515 LOC) |
| Unused exports / symbols | 122 exports + 120 types | 1,336 raw vulture hits (needs triage; FastAPI/Pydantic decorator false positives) |
| Broken test suites | **6 (import deleted modules — hard-fail)** | — |
| Unlisted dependencies | 8 (works via transitive deps) | — |
| TODO/FIXME/HACK | 13 | 11 |
| BE endpoints never called by FE | — | 71 of 353 ops (27 admin, 3 public, **41 product**) |

## RED FLAGS (verified, not just tool output)

### 1. Six test suites hard-fail on import — and jest lists them as runnable
Verified: `npx jest __tests__/components/trip-home/zoneLabels.test.ts` → module-not-found FAIL.
Either FE CI is currently red, or CI doesn't run the full suite. Files:

- `__tests__/components/chat/MapCardEmpty.test.tsx` → `components/chat/MapCard` (gone)
- `__tests__/components/chat/group/VesperNoteAttribution.test.tsx` → `components/chat/group/VesperNote` (gone)
- `__tests__/components/plan/EventRow.test.tsx` → `components/plan/EventRow` (gone)
- `__tests__/components/trip-home/PreTripPrepFeed.test.tsx` → gone
- `__tests__/components/trip-home/channelRouting.test.ts` → gone
- `__tests__/components/trip-home/zoneLabels.test.ts` → gone

**Action:** delete the 6 test files (their subjects were deliberately deleted in the era-1/era-2 cleanups) AND find out why CI didn't catch this.

### 2. Eight unlisted dependencies (imported but not in package.json)
`@jest/globals`, `expo-system-ui`, `@react-navigation/native`, `expo-file-system` (×3 files),
`@react-navigation/bottom-tabs`, `pngjs`. These resolve via transitive deps today and break
silently on any lockfile refresh. 10-minute fix: add to package.json.

## Unused files — travel-app (71 files, 9.4k LOC)

Spot-verified (Chip.tsx, AuthGuard.tsx confirmed zero-references). Clusters map to known
redesign eras — this is the uncollected garbage from the June rebuilds:

| Cluster | Files | Likely era |
|---|---|---|
| `components/discover/*` (FeedCard, Waterfall, ReadingRoomLayout, ShelfSection, immersive-hero set…) | 11 | pre-Reading-Room Discover (June 10 v2 replaced) |
| `components/ui/state/*` (whole state kit incl. index.ts + stateTokens) | 12 | superseded state-screen system |
| `components/atlas/*` (CandidateCard, HeroCard, InboxItem, ProvenanceRibbon…) | 10 | pre-v3 Atlas rebuild |
| `components/trip-plan/*` (BudgetSheet, PlanProposalRow, PlanStatusRail…) | 6 | pre-Change-Studio plan UI |
| `components/ui/*` misc (Chip, ListRow, SwipeableRow, SettingsList, StickyActionBar…) | 8 | orphaned primitives |
| stays/takes/expense/venue/trips/memory/chat singles | ~18 | various |
| `constants/designTokens.ts`, `constants/index.ts`, `constants/phrases.ts` | 3 | pre-token-bridge design system |
| hooks: `useNarrationManifest`, `useStayState`; utils: `angleAdapters`, `experienceDisplay` | 4 | — |

Full list: knip output. **Caveat before deleting:** confirm none are referenced by Maestro
flows/design-QA scripts (knip only follows TS imports).

Also 7 duplicate exports (named + default from same file — StayCard family + BookingProposalCard).

## Orphan modules — travel-agent (verified incl. relative imports)

| Module | LOC | Note |
|---|---|---|
| `backend/planning_agent/context_loader.py` | 104 | never imported |
| `backend/research_agent/agents/testing.py` | 43 | never imported |
| `backend/scripts/backfill_atlas_qdrant.py` | 197 | not in Makefile; one-shot backfill, likely done |
| `backend/scripts/check_atlas_qdrant_parity.py` | 171 | not in Makefile; may be worth wiring into ops instead of deleting |

(First pass flagged 39; 35 were false positives reached via relative imports — `_tables/*`
via `tables.py` star-reexport, `routes/users/*` via router aggregation.)

## Backend endpoints never called by the app (41 product ops)

Computed: openapi.json (353 ops) minus every `/api/...` literal in app/hooks/utils/components/contexts.
After removing ops/health/webhooks (9) and flag-dark booking (≈6), the interesting residue:

**Parallel-read-path suspects (superseded seams still live):**
- `GET /api/trips/{id}/proposals` — proposals UI reads via plan-state adapter now; raw list endpoint vestigial?
- `GET/POST /api/conversations/{id}/messages` + `/messages/stream` — pre-trip-chat conversation seam; superseded by trip messages?
- `POST /api/trips/{id}/messages/stream` + `/messages/close`, `GET /messages/info` — verify vs sse.ts URL construction before concluding
- `GET /api/users/{id}/privacy/audit` — May-era privacy-audit screen; superseded by trust hub?

**Built-but-never-surfaced intelligence (the "surface what's built" theme, in endpoint form):**
- `GET .../blocks/{id}/better-slots`, `/move-check`, `/days/{id}/gap-suggestions` — planning intelligence with no UI
- `GET /api/users/{id}/for-you`, `/feed`, `/followers` — social/for-you substrate uncalled
- `GET /api/trips/{id}/situation`, `/action-receipts/recent`, `/expenses/suggest-category`, `/itinerary/edit-history`
- `GET /api/dossiers/accommodation/{id}`, `/site/{id}`, `GET /api/takes/{id}`, `GET /api/trips/{id}/experiences`

**Caveat:** FE URL extraction is literal-string based; endpoints called through dynamically
built URLs would be false-positived. Spot-verify each before acting.

## Vulture triage guide (1,336 raw → what's real)

Known false-positive classes to filter first: FastAPI route handlers (decorator-registered),
Pydantic models used only in `response_model=`/serialization, `_reset_for_tests` helpers,
protocol/ABC methods. Genuinely suspicious clusters spotted in the raw output:

- `backend/core/db/expenses.py`: `async_update_expense`, `async_replace_shares`, `async_settle_shares` — if unused, the async expenses write path may be a dead twin of the sync one (get_tx migration leftover?)
- `backend/booking_agent/db/booking_crud.py`: `expire_stale_holds`, `list_held_offers_for_trips` — dark feature, but expire_stale_holds sounds like it SHOULD be scheduled (hold-expiry sweep missing?)
- `backend/core/request_context.py`: `set_trip_id/set_session_id/set_user_id` setters unused — context never populated?
- `backend/core/surfaces/registry.py`: 4 unused query methods on the registry

## Dark-by-design filter (do NOT count as dead)

BE flags: anniversary_push, atlas_auto_candidate, atlas_llm, atlas_signals_to_memory,
story_sharing, unpacked_seasonal_push, venue_disruption_proposals.
FE flags: VOICE, POSTCARDS, AMBIENT, STORY_SHARE (+ booking transaction engine).
Anything reachable only behind these is intentional (v1 scope lock, 2026-06-30).

## Suggested next phases

1. **Quick wins (hours):** delete 6 broken tests + fix CI gap; add 8 unlisted deps; delete the 4 BE orphans (or wire parity-check into ops); dedupe the 7 double exports.
2. **Unused-file purge (needs judgment):** confirm the 71 FE files against Maestro/design-QA references, then delete in era-labeled batches (matches the June 10 simplification-sprint precedent: era-1 deletion was ~4.4k LOC).
3. **Vulture triage (agent pass):** filter the 4 false-positive classes, then verify the ~50 survivors file-by-file — the expenses/booking/request-context clusters first, since those smell like parallel systems, not just dead code.
4. **Endpoint reconciliation:** for each of the 41 uncalled product ops decide: delete, mark dark-by-design, or ticket as "built-but-unsurfaced" product work.
