# Pre-Dogfood Area Audit 02 — Social Loop: Sharing, Plan-Similar & Follow Graph

Date: 2026-05-21  
Scope: trip → artifact → share → viewer → plan-similar loop; follow graph;
public projection; unauthenticated landing/card; migrations
`f1a2b3c4d5e6` → `a7b8c9d0e1f2` → `b2c3d4e5f6a7` → `c3d4e5f6a7b8` → `d4e5f6a7b8c9`  
Mode: read-only; no product code, test, or config was modified.

## Summary

| Severity | Count |
|---|---:|
| P0 | 0 |
| P1 | 6 |
| P2 | 5 |
| TECH-DEBT | 3 |

**Verdict:** The backend public projection is thoughtfully default-deny and is
backed by strong offline + Postgres integration tests for the share lifecycle
(revoke, rotate, pause/resume, private-photo allowlist, idempotent plan-similar).
The visibility state machine does **not** resurrect content on revoked or
rotated slugs. The highest-risk gaps for dogfood are **consent boundaries**
(cross-member photos and unredacted narrative in section bodies reaching
unauthenticated surfaces), **mock-vs-real preview drift** on photos, and
**operational abuse** (unrate-limited public card rendering + per-pod card cache).

**Positive signals**

- Single projection seam: `build_public_story_payload` + frozen
  `PublicTripStory` allowlist (`tests/test_story_projection.py`,
  `test_public_model_allowlist_is_frozen`).
- Production callers always pass `allowed_photo_urls` from
  `_public_photo_urls`; integration test
  `test_private_photo_in_slot_excluded_from_public` locks the trust boundary.
- Share lifecycle covered at DB layer (`tests/core/test_trip_story_shares_db.py`)
  and route layer (`tests/api/test_story_shares_api.py`,
  `test_story_landing_api.py`, `test_plan_similar_api.py`).
- Migrations form a clean linear chain with documented FK/CHECK behavior;
  merged to single head via `e2f3a4b5c6d7_merge_all_heads.py`.
- Frontend `ShareStorySheet` uses server preview (preview == live) and honest
  copy for link vs group/private pause.

**Dogfood gate:** Safe to **test the share loop on a real backend** for owners
who only use their own group photos and read the privacy preview — but **not**
safe to assume mock mode or co-traveler photo slots match production privacy,
and not safe to run multi-pod production without addressing card-cache +
rate-limit gaps.

---

## Findings

### [P1] — Another trip member can put a co-traveler’s group photo on an unauthenticated public share

**References:**
- `Travel Agent/backend/api/routes/memory.py:415-444` (`_validate_story_photo_url` — CDN host only, no `uploaded_by` / ownership check)
- `Travel Agent/backend/core/db/trip_story_shares.py:494-529` (`_public_photo_urls` — all `group` / `group_and_learn` URLs **on the trip**, not scoped to share owner)
- `Travel Agent/backend/core/story_projection.py:98-108` (slot URL kept if in allowlist)
- `Travel Agent/backend/core/story_card.py:298` (card hero from `public.cover_image_url`)
- `Travel Agent/backend/api/routes/story_landing.py:137-140, 126` (HTML cover + OG `card.png`)
- Cross-audit: `docs/audits/pre-dogfood-2026-05/areas/07-memory-trip-story-photos.md` (same path, composer/photo cluster)

**Why it matters to a real tester:**  
Group visibility means “trip members in the app,” not “anyone with a public link.”
Member A can PATCH member B’s group CDN URL into a story slot, publish link-only,
and B’s image appears on `/stories/{slug}`, `/stories/{slug}/card.png`, and
iMessage/Slack previews — without B choosing to publish that photo externally.

**Repro / deterministic test idea:**
1. Two members on one trip; B uploads a photo with `visibility=group`.
2. A patches `PATCH .../story/sections/{id}/photo` with B’s `cdn_url`.
3. A creates share `visibility=link`; `GET /api/public/stories/{slug}` and
   `GET /stories/{slug}/card.png` as anonymous.
4. Assert B’s image bytes/URL appear — test should **fail** until allowlist is
   scoped to `uploaded_by_user_id == share.owner_user_id` (or explicit
   co-traveler opt-in on the slot).

**Suggested fix direction:**  
Tighten `_public_photo_urls` to owner-uploaded (or owner + explicit
`included_traveler_ids` on redaction policy). On PATCH photo slot, require
`photo_url` belongs to caller’s `trip_photos` row. Add Postgres regression
extending `test_private_photo_in_slot_excluded_from_public`.

**Confidence:** High.

---

### [P1] — Public story sections are not scanned for constraint-shaped vocabulary

**References:**
- `Travel Agent/backend/core/story_projection.py:90-96` (drops hidden/empty sections; **no body redaction**)
- `Travel Agent/backend/core/models/trip_stories.py:134-153` (`PublicTripStory` allowlist is structural only)
- `Travel Agent/backend/tasks/trip_story.py` (composer fed observations / block titles — see area 07)
- `Travel Agent/docs/audits/pre-dogfood-2026-05/areas/01-privacy-group-safe-synthesis.md` (§ reflection on preview as sole net)

**Why it matters to a real tester:**  
The Privacy Preview shows exactly what will leak — including narrative the
composer wrote from private observations (“migraine,” “tight budget,” “knee”).
The product promise is that **constraints never appear** on public surfaces;
today that depends on the owner noticing prose, not on server-side enforcement.

**Repro / deterministic test idea:**
1. Seed a trip story whose section body contains tokens from
   `privacy_redactor._PRIVATE_KEYWORD_PATTERNS` (budget + medical + accessibility).
2. `POST .../story/share/preview` with default policy; assert preview `public.sections`
   either omit flagged bodies or auto-add section ids to `hidden_section_ids`.
3. Repeat for live `GET /api/public/stories/{slug}` after publish.

**Suggested fix direction:**  
Run `check_private_signal` (or equivalent) on each section at projection time;
default-hide flagged sections in `RedactionPolicy`, surface count in preview UI.
Align composer system prompt with banned vocabulary unless owner-edited.

**Confidence:** Medium.

---

### [P1] — Mock Privacy Preview does not apply the production photo allowlist

**References:**
- `Travel App/utils/api/mock.ts:2249-2282` (`previewStoryShare` — all `photo_slots` with `photo_url` → `photos_shown`, no `trip_photos` visibility)
- `Travel Agent/backend/core/db/trip_story_shares.py:494-561` (real preview uses `_public_photo_urls`)
- `Travel App/data/storyShare.ts:10-11` (mock or real via `EXPO_PUBLIC_USE_MOCK_API`)
- `docs/audits/pre-dogfood-2026-05/dogfood-readiness.md` (mock/real parity gate passes globally — may not cover this triad)

**Why it matters to a real tester:**  
With `EXPO_PUBLIC_USE_MOCK_API=true`, “2 of 2 photos” in ShareStorySheet can
show while production would show `0 of 2` when no group photos exist — or the
inverse if private URLs sit in slots. Testers can publish believing the preview.

**Repro / deterministic test idea:**  
Add mock-real parity test: same story + `trip_photos` rows → compare
`previewStoryShare` photo counts to `preview_story_share` DB helper output.

**Suggested fix direction:**  
Mirror `_public_photo_urls` in mock (filter slot URLs against a mock album map),
or delegate preview to a small shared pure function copied from projection tests.

**Confidence:** High.

---

### [P1] — Revoked or rotated links can still serve stale share cards on other pods (1h TTL)

**References:**
- `Travel Agent/backend/core/story_card.py:243-282` (`_card_cache`, `_CARD_CACHE_TTL_S = 3600`, documented not multi-pod safe)
- `Travel Agent/backend/core/db/trip_story_shares.py:173, 222` (`invalidate_card_cache` on revoke/rotate/update)
- `Travel Agent/backend/api/routes/story_landing.py:84-95` (`Cache-Control: public, max-age=3600` on `card.png`)

**Why it matters to a real tester:**  
Owner taps “Stop sharing” or “New link”; JSON/HTML 404/410 on pods that handled
the write, but another pod (or CDN) may still return yesterday’s PNG with hero
photo and title for up to an hour — exactly when they expect immediate takedown.

**Repro / deterministic test idea:**
1. Publish share; warm `GET /stories/{slug}/card.png` on pod A.
2. Revoke on pod B; request card on pod A again before TTL — assert 404 or
   non-identifying gradient card (integration test with shared Redis or disable cache in test).

**Suggested fix direction:**  
Shared cache (Redis) keyed by slug + share `updated_at`/`revoked_at`, or shorten
TTL + `Cache-Control: no-cache` when `revoked_at` set; purge CDN on revoke webhook.

**Confidence:** High (design comment admits gap); Medium on likelihood in single-pod dogfood.

---

### [P1] — Unauthenticated public routes have no rate limits (card render is expensive)

**References:**
- `Travel Agent/backend/api/routes/story_landing.py:68-78, 85-95` (JSON + HTML + PNG, no `check_rate_limit`)
- `Travel Agent/backend/core/story_card.py:210-317` (httpx hero fetch + Mapbox + Pillow per miss)
- `Travel Agent/backend/api/rate_limits.py:24-34` (`plan_similar` capped; no `public_story` / `story_card` scope)
- `Travel Agent/backend/api/routes/plan_similar.py:32-39` (public plan-seed also unlimited)

**Why it matters to a real tester:**  
Does not change privacy per se, but a leaked slug enables unbounded card
regeneration (Mapbox token, egress, CPU). Dogfood on Fly with 2+ machines amplifies cost.

**Repro / deterministic test idea:**  
Load-test `GET /stories/{slug}/card.png` × 500/min from one IP; expect 429 after
threshold. Today expect 200 throughout.

**Suggested fix direction:**  
Per-IP (and per-slug) token bucket on `/stories/*` and `/api/public/stories/*`;
cap Mapbox/hero fetches inside `build_story_card_png`.

**Confidence:** High.

---

### [P1] — Link rotation drops `followers_visible` override

**References:**
- `Travel Agent/backend/core/db/trip_story_shares.py:177-223` (`rotate_share` copies `visibility` + `redaction_policy` only)
- `Travel Agent/backend/core/db/trip_story_shares.py:114-144` (`create_share` accepts `followers_visible`)
- `Travel Agent/tests/core/test_trip_story_shares_db.py:262-279` (rotate slug tested; not follower flag)

**Why it matters to a real tester:**  
Owner enables “Show to followers,” rotates link after a leak scare; feed stops
getting `story_published` events (override lost → user default, often false) while
they believe settings persisted.

**Repro / deterministic test idea:**
1. Create share with `followers_visible=true`; rotate in place.
2. Assert new row has `followers_visible=true` and second `emit_story_published`
   behavior unchanged.

**Suggested fix direction:**  
Copy `followers_visible` in `rotate_share` `.values(...)`; add regression in
`test_trip_story_shares_db.py`.

**Confidence:** High.

---

### [P2] — Story edits after publish do not invalidate the rendered card cache

**References:**
- `Travel Agent/backend/core/story_card.py:256-258, 284-317` (cache keyed by slug only)
- `Travel Agent/backend/core/db/trip_stories.py` (PATCH section/photo — no share cache hook)
- `Travel Agent/backend/core/db/trip_story_shares.py:267-268` (invalidates on **settings** update, not story content)

**Why it matters to a real tester:**  
Owner fixes a typo or removes a section, re-shares the same link; OG/card still
show old title/hero for up to 1h — confusing and looks like revoke/pause failed.

**Repro / deterministic test idea:**  
Publish → render card → PATCH hero title → card without cache bust should fail
assertion on new title.

**Suggested fix direction:**  
`invalidate_card_cache` from story PATCH handlers when an active share exists;
include `trip_stories.updated_at` in cache key.

**Confidence:** Medium.

---

### [P2] — Raw `Referer` header stored in share analytics

**References:**
- `Travel Agent/backend/api/routes/story_landing.py:77, 117` (`referrer=request.headers.get("referer")`)
- `Travel Agent/backend/core/db/trip_story_shares.py:334-357, 361-397` (`log_share_event` / `record_share_open` persist `referrer` text)
- `Travel Agent/alembic/versions/b2c3d4e5f6a7_trip_story_share_events.py:59-60` (`referrer` column unbounded text)

**Why it matters to a real tester:**  
Referrers often carry query tokens (`?utm_`, session ids, email click trackers).
Owner-facing stats are aggregate-only today, but DB copies can end up in backups
or support exports — contrary to “no PII in viewer fields” intent in the spec.

**Repro / deterministic test idea:**  
Open story with `Referer: https://evil.test/path?email=test@example.com`; assert DB row
stores hostname only or hashed bucket, not full query string.

**Suggested fix direction:**  
Store `urlparse(referrer).netloc` only, or truncate + strip query; document in schema.

**Confidence:** Medium.

---

### [P2] — `plan_similar` rate limit is in-process only (multi-worker bypass)

**References:**
- `Travel Agent/backend/api/routes/plan_similar.py:48` (`check_rate_limit` only)
- `Travel Agent/backend/api/rate_limits.py:40-64, 73-149` (`check_rate_limit_pg` exists but not called here)
- `Travel Agent/backend/api/rate_limits.py:33` (20/hour per user)

**Why it matters to a real tester:**  
Low risk for dogfood volume; matters if a token leaks and an attacker spams
`POST /api/plan-similar` across workers to mint trips.

**Repro / deterministic test idea:**  
Call `check_rate_limit_pg` in route; 21st request within hour returns 429 regardless of worker.

**Suggested fix direction:**  
Double-gate pattern used elsewhere: `check_rate_limit` + `check_rate_limit_pg`.

**Confidence:** High.

---

### [P2] — Trip story editor may surface private album photos before share (client-only)

**References:**
- `Travel App/app/(tabs)/trips/[tripId]/story.tsx:82-114` (ST4: `pool = visible.length > 0 ? visible : photos` — includes private when no group photos)
- `Travel App/components/memory/ShareStorySheet.tsx:267-269` (reassurance copy; server preview is authoritative)

**Why it matters to a real tester:**  
Solo traveler with only `private` photos sees them in section slots while editing;
server preview correctly drops them from `photos_shown`, but the in-editor UI
can feel like “this will be on the card” until they open the sheet.

**Repro / deterministic test idea:**  
UI test: trip with one private photo → story screen shows photo in slot →
ShareStorySheet preview counts `0 of 1` photos.

**Suggested fix direction:**  
Align editor pool with group-only (match server), or badge “won’t appear on public link.”

**Confidence:** Medium.

---

### [P2] — `group` visibility is a pause label only (no group-authenticated viewer route)

**References:**
- `Travel Agent/backend/core/db/trip_story_shares.py:50-51, 543-544` (`_PUBLICLY_OPENABLE` = link/public only)
- `Travel App/components/memory/ShareStorySheet.tsx:72-73` (honest copy: group “won’t open publicly yet”)
- `Travel Agent/docs/product/MVP Social Loop.md:315-316` (visibility enum includes `group`)

**Why it matters to a real tester:**  
Expectation drift: “Group” sounds like trip members can open the link; they get the same 410 as private unless switched to link/public.

**Suggested fix direction:**  
Product copy only for dogfood, or implement member-authenticated `/api/trips/{id}/story/shared-view` later.

**Confidence:** High (documented limitation).

---

### [TECH-DEBT] — `anonymous_viewer_id` column never populated

**References:**
- `Travel Agent/alembic/versions/b2c3d4e5f6a7_trip_story_share_events.py:59`
- `Travel Agent/backend/core/db/trip_story_shares.py:361-393` (`record_share_open` never sets it)
- `Travel Agent/docs/product/MVP Social Loop.md:500-501` (nullable anonymous id in spec)

**Why it matters to a real tester:**  
Does not affect privacy today; limits funnel analytics for logged-out viewers on public landing.

**Suggested fix direction:**  
Set signed cookie / header-based anon id on public routes when no auth.

**Confidence:** High.

---

### [TECH-DEBT] — Share card omits “3 place chips” from MVP spec; no in-app PNG export

**References:**
- `Travel Agent/backend/core/story_card.py:311-312` (`StoryCardData` without `chips` from places)
- `Travel Agent/docs/product/MVP Social Loop.md:329-346` (9:16 card + place chips)
- `Travel App/components/memory/ShareStorySheet.tsx:176-187` (native share of URL only, no `expo-sharing` image)

**Why it matters to a real tester:**  
Distribution quality / spec completeness, not a leak.

**Suggested fix direction:**  
Pull top places from public projection when place chips exist; add save-to-camera-roll path.

**Confidence:** High.

---

### [TECH-DEBT] — Postgres integration suite is strong but not in default offline CI

**References:**
- `Travel Agent/tests/core/test_trip_story_shares_db.py:8-9` (`@requires_postgres`)
- `Travel Agent/tests/core/test_plan_similar_db.py:8-9`
- User note: integration tests run once

**Why it matters to a real tester:**  
Regressions on visibility/photo allowlist/idempotency won’t show in `make test-backend`
offline runs; dogfood relies on someone running Docker pytest before release.

**Suggested fix direction:**  
Wire `test_trip_story_shares_db` + `test_plan_similar_db` into CI job with Postgres service (mirror contract-check reliability).

**Confidence:** High.

---

## Known / Accepted

Items verified as **working as designed** or tracked elsewhere — not filed as new defects.

- **Default-deny public projection** — `story_projection.py` + `PublicTripStory`
  frozen allowlist; raw `trip_stories` / observations never serialized on public routes.
- **Revoked / rotated slugs do not resurrect content** — `get_public_story_by_slug`
  checks `revoked_at` and `_PUBLICLY_OPENABLE`; `test_revoke_makes_link_dead`,
  `test_rotate_changes_slug` (`test_trip_story_shares_db.py`).
- **Reversible pause vs revoke** — `update_share_settings` keeps slug;
  `visibility=private|group` gates public route; same slug works when reopened
  (`test_update_settings_in_place_keeps_slug`).
- **Plan-similar idempotency** — `find_existing_derived_trip` per (viewer, share);
  `test_idempotent_for_same_viewer` (`test_plan_similar_db.py`); rate limit 20/hr
  on authenticated create (`rate_limits.py:33`).
- **`trip_sources` provenance** — `UNIQUE(trip_id)`; `source_share_id ON DELETE SET NULL`
  (`a7b8c9d0e1f2_trip_sources.py`); conversions counted from `trip_sources`, not events alone.
- **Migrations** — Linear chain
  `f1a2b3c4d5e6` → `a7b8c9d0e1f2` → `b2c3d4e5f6a7` → `c3d4e5f6a7b8` → `d4e5f6a7b8c9`,
  merged at `e2f3a4b5c6d7`; CHECK on `visibility` and `event_type`; FK CASCADE on share
  delete for events; share slug globally UNIQUE.
- **Mapbox token-gated** — `static_map.py:35-37` returns `None` without `MAPBOX_TOKEN`;
  card renders without map strip.
- **Follow graph read path** — `follow_affinity.py` never writes PM; degrades to `{}`;
  `social_feed` requires `require_self` (`follows.py:135`).
- **Public profile default-deny** — `profiles.py:58-59` 404 unless `public_profile_enabled`;
  only `reflection_phrases` + `interests` + openable story list (no PM markdown).
- **Share analytics** — `ShareStats` is counts only; `viewer_user_id` optional on events,
  not exposed to owner UI.
- **Invite / intake P0s** — documented in `dogfood-readiness.md` and area 01; out of scope
  for this file except mock parity note above.
- **Deploy blockers** — unreachable `travelagent.app` / EAS preflight (dogfood-readiness P0s)
  block end-to-end share tests in TestFlight, not the sharing code path itself.
