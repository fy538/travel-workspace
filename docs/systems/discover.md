# Discover — System Charter

> Surface: Discover
> Maturity (for MVP): Should-have
> Status: wired
> Last updated: 2026-06-27

## Purpose
The server-side feed composer for the single blended Discover surface — it
gathers for-you / editorial / friends streams, interleaves and sections them
into a paced magazine column, and carries entity context into Vesper via
ConversationSeed. Serves belief #20 (Discover Vision): Discover is the **mouth
of the funnel** — find a place → ask Vesper with context → turn discovery into a
trip action, and trust comes from **a face, not anonymous editorial**.

## Spans (cross-repo)
- Backend: [`travel-agent/backend/discover/`](../../travel-agent/backend/discover/FEATURE.md) (`compose.py::compose_discover_feed` — the feed layout brain; `compose_board.py` — the WORLD-corpus board engine over [`backend/composition/`](../../travel-agent/backend/composition/FEATURE.md)) + [`backend/research_agent/`](../../travel-agent/backend/research_agent/FEATURE.md) (dossier generation). Routes: `api/routes/discover.py`.
- Frontend: `app/(tabs)/discover/index.tsx`, `utils/discoverFeedApi.ts`, `utils/discoverSections.ts`, `utils/discoverContext.ts`, `components/discover/ReadingRoomLayout.tsx`, detail routes (`venue/`, `place/`, `dossier/`, `guide/`, `angle/`).
- Tables read: dossiers, collections (guides), follows, trips, catalog venues/sites. **Discover owns no content tables** (layout/board brain only).

## Public interface (what other systems may call / read)
- **Inbound (FE → BE):** `GET /api/discover/feed` → `DiscoverFeedResponse` (`read` masthead + 4 `sections` + `rhythm` + top-level `lead`) · `POST /api/discover/compose` → WORLD-corpus board (`CompositionResult`, Discover variant).
- **Entry points:** `compose_discover_feed` (the only public feed entry, async, keyword-only) · `resolve_feed_shape(...)` → `dream`/`briefing`/`proximity`/`retrospective`/`dual`.
- **Consumes:** `get_for_you` (insights), `list_collections`, `get_social_feed`, dossiers — read-only; ConversationSeed handoff into Concierge.
- **Never:** treat a bare catalog venue (md5-ordered) as a vetted editorial pick; desync the server composer from its client mock mirror without changing both.

## Owns (source of truth)
**Nothing.** Discover is a composition layer — a deterministic arrangement over
other systems' content. Dossiers belong to `research_agent`; the board assembly
belongs to `composition/`. Discover owns only sectioning, rhythm, and shape
resolution.

## Invariants (must always be true)
- **Honest provenance over decoration** — only dossiers carry a real byline (`source='dossier'`); a bare catalog venue carries `provenance=None` and is surfaced honestly unattributed (a listing, not a vouch). `because` is set ONLY when a real loved facet actually matched.
- **Parse honesty** — a freeform query maps to KNOWN-dimension facets only; unrecognized terms are dropped, never forced into a fabricated dimension.
- **No false peak** — the board score lifecycle puts flat catalog scores in a tight synthetic band so md5-ordering never fakes a `single` hero; re-normalization only fires on genuine spread.
- **ConversationSeed always carries context** (journey 07) — Ask Vesper from a detail page never opens an empty/generic chat; trip context routes group-only for social actions, no-trip context routes private.
- **Real empty state never reads as broken plumbing** — honest absence, not a fabricated feed.
- **Dual-implementation parity** — server composer and client mock mirror (`discoverSections.ts` / `discoverContext.ts` / the rhythm planner) must change together.

## Failure modes
- A content stream fails → that source contributes nothing; the feed composes from the survivors (best-effort `asyncio.gather` over `run_in_executor`).
- Proximity enrichment is a **no-op** outside `during_trip` + GPS (early-returns; no fabricated walk-times).

## Maturity & validation
- Serves journey: 07 (Discover → contextual Vesper → trip action).
- DoD state: feed/section/seed unit tests ✅ (`discoverFeed.test.ts`, `discover.smoke.test.tsx`, `venue-detail.smoke.test.tsx`) · **live feed walk ❌ · dual-parity FE re-verification pending** (post-composition refactor).
- FEATURE.md maturity is **"beta"**; research pipeline auto-publish posture is unsettled (see research-pipeline notes).

## Canonical docs
- why → `product/Discover Vision.md` · `product/One Engine, Two Corpora.md` · what(be) → `backend/discover/FEATURE.md` · `backend/composition/FEATURE.md` · `backend/research_agent/FEATURE.md` · what(fe) → `page-specs/discover.md` · `conversation-seed/Standard.md`.
- Tests: `__tests__/utils/discoverFeed.test.ts`, `__tests__/screens/discover.smoke.test.tsx`.

## Open risks / known gaps
- **Dual-implementation desync is the headline risk** — a cadence/section change on one side (server `rhythm.py` vs client mirror) makes the same feed look different in dev (mock) vs prod (server). The FEATURE.md flags an FE re-verification pass outstanding after the composition refactor.
- **Content sparsity / missing ids** can hide behind polished mocks (journey 07) — real Discover empty states and unwired-looking guide/angle cards are the on-device failure surface.
- Generation gap, not publish gap: angles without dossiers leave thin sections; the funnel's mouth is only as wide as the corpus behind it.
