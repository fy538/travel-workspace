# Postcard / Story — System Charter

> Surface: Atlas
> Maturity (for MVP): Built-dark
> Status: dark
> Last updated: 2026-06-27

## Purpose
The post-trip memory artifact — img2img a real source photo (the user's own pixels)
into the riso brand and return a rendered postcard; the homecoming Trip Story reads
it aloud (narration) over riso renders. Serves belief #27 (the trip's album belongs
in the product) and journey 12. Emotional weight comes from **constraints, not
abundance** — a 3–6/trip cap, not an auto-beautified feed.

## Spans (cross-repo)
- Backend: [`travel-agent/backend/postcard/`](../../travel-agent/backend/postcard/FEATURE.md) — `render.py` (orchestrator: flag → cost guard → provider → quality floor; `store_postcard_render` persistence), `provider.py` (`NullPostcardProvider` default, `ReplicatePostcardProvider`). [`travel-agent/backend/media/`](../../travel-agent/backend/media/FEATURE.md) — `rehost.py` (CDN-rehost of the source + Replicate output). [`travel-agent/backend/digest/`](../../travel-agent/backend/digest/FEATURE.md) — `generate_trip_summary()` (the Sonnet end-of-trip retrospective the Story narrates).
- Frontend: Atlas artifact surfaces; the homecoming Trip Story screen (scaffolded dark).
- Tables of record: atlas artifact `rendered_image_url` / `render_status` (via `core/db/postcard_render.set_artifact_render`); S3/CDN photo variants; `TripSummary`.

## Public interface (what other systems may call / read)
- **Entry points (internal):** `render.render_postcard(*, source_image_url, style_prompt, rendered_today, ...)` (pure, no DB) → `render.store_postcard_render(artifact_id, result)` (the separate persistence wrapper) · `provider.get_postcard_provider(settings)` · `media.rehost.rehost(...)` · `digest.generate_trip_summary()` (on `trip.completed`).
- **Consumes:** `CoreSettings.postcard_render_*` flags/caps/quality-floor; the media rehost CDN boundary; the digest trip summary; narration (read-aloud) for the Story.
- **Never:** hand the render a device-local `ph://` PHAsset — img2img needs real pixels, so the caller must supply a CDN-resolvable URL. Never serve a Replicate output URL raw (it expires) — rehost first.

## Owns (source of truth)
The render pipeline and its result tokens; the rendered-postcard URL / status stamped
onto an atlas artifact. Media owns the photo bytes/variants (`rehost`); Digest owns
the `TripSummary` the Story narrates.

## Invariants (must always be true)
- **SHIPS DARK by two independent gates** — `postcard_render_enabled` defaults False **and** the default provider is `NullPostcardProvider`. `get_postcard_provider` returns null unless the flag is on AND key + model are both set; flipping the flag alone cannot incur cost.
- **Errors are values, not exceptions** — every rejection returns a `RenderResult` with a stable `error` token (`feature_disabled`, `daily_cap_reached`, `no_source_image`, `below_quality_floor`, …); even a scaffold `NotImplementedError` becomes a fail-closed result. Callers branch on `result.ok`, never try/except.
- **Cost guards before any provider touch** — flag check → per-user/day cap → empty-source check short-circuit *before* the provider is called.
- **Quality floor before ship** — a result below `postcard_render_quality_floor` is rejected, not shipped.
- **Render is pure on purpose** — `rendered_today` is an input, not a DB read; persistence is the deliberately separate `store_postcard_render`. Don't fold a DB read into the orchestrator.
- **EXIF stripped + scarcity cap** — media strips GPS/device info on all variants; the artifact lives at 3–6/trip so abundance never dilutes the memory.

## Failure modes
- Flag off / no provider configured → `feature_disabled` / `no_provider_configured` `RenderResult` (the prod posture — `NullPostcardProvider`, no network call).
- Daily cap hit → `daily_cap_reached`, before any provider touch.
- Replicate output expires / rehost fails → caught precisely as `rehost_failed`; only an `ok` result writes a URL onto the artifact.

## Maturity & validation
- Serves journey: 12 (returned trip → story / memory / settle-up).
- **Dark posture:** full pipeline present but gated off — `NullPostcardProvider` in prod (Replicate only when the flag is on AND key + model are set). No real model call is wired into prod; provider selection + quality tuning deliberately deferred. The homecoming Trip Story (narration read-aloud + riso) is **scaffolded dark**.
- DoD state: pure render policy (flag → cost guard → provider → quality floor) + error-as-value + rehost-boundary tests ✅ · **no provider key / no real img2img output validated ❌ · Story screen end-to-end ❌**.

## Canonical docs
- why → `product/Post-Trip Lifecycle.md` (belief #27) · `product/Content as Infrastructure.md` · journey → [`journeys/12-returned-trip-to-story-memory-settle-up.md`](../journeys/12-returned-trip-to-story-memory-settle-up.md) · what(be) → `backend/postcard/FEATURE.md` · `backend/media/FEATURE.md` · `backend/digest/FEATURE.md`.
- Tests: `tests/postcard/*` (render policy + error tokens), media rehost tests.

## Open risks / known gaps
- No real provider has ever rendered in prod — riso quality, the img2img prompt, and the quality floor's real behavior (the Null/Replicate providers report `quality_score=1.0`) are all unproven until a key is added.
- The source-URL contract (CDN-resolvable, never `ph://`) is the most likely integration break — the FE must hand over a fetchable photo URL, not a PHAsset reference.
- The Trip Story (narration + riso composition) depends on **two** dark subsystems (this + Voice/Narration) plus the Sonnet trip summary — the homecoming moment is the furthest from validated.
