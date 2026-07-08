# Surface Inventory Diff — Trip Story Public Sharing (2026-07-07)

Canon concept → real code, for the "Implement MVP public story sharing" feature (handoff 118/119, `Vesper Trip Story and Memory Handoff.html`). Companion doc: `product-contract-audit-trip-story-sharing-2026-07-07.md` (the "does it obey the rules" audit — this doc is "what exists and where").

Legend: ✅ built & wired · 🟡 built but partial/misnamed/misfiring · ⚫ built but orphaned (exists, zero consumers) · ❌ not built.

## Owner-side: share creation, redaction, link lifecycle

| Canon concept | Real name | Location | Status |
|---|---|---|---|
| OwnerShareControls | `ShareStorySheet` (default export, 1108 lines) | `travel-app/components/memory/ShareStorySheet.tsx` | ✅ |
| Create-link action | `handleCreate` → `useCreateStoryShare` | `ShareStorySheet.tsx:260` → `data/storyShare.ts:100` → `POST /api/trips/{trip_id}/story/share` (`story_shares.py:105`) | ✅ |
| Redaction toggles | `SettingToggle` rows (dates/destination/followers) | `ShareStorySheet.tsx:472-494` | 🟡 — only 3 of canon's 8 `RedactionPolicy` dimensions have owner controls |
| Compact inline preview (pre-publish) | `PreviewCard` ← `useStorySharePreview` | `ShareStorySheet.tsx:666-722` → `POST .../share/preview` (`story_shares.py:147`) | ✅ |
| Full recipient preview (distinct, pre-publish) | — | — | ❌ — `handlePreview` (`ShareStorySheet.tsx:324-333`) only exists post-publish, opens the live URL; no separate pre-publish full-preview surface |
| Update-in-place | `handleUpdate` → `useUpdateStoryShare` | `ShareStorySheet.tsx:278` → `PATCH .../share` (`story_shares.py:170`) | ✅ |
| Owner exact-status notice | `ShareLinkStateNotice` | `travel-app/components/external-share/ShareLinkStateNotice.tsx` | ✅ |
| Pause | `handlePause` (sets `visibility:'private'`) | `ShareStorySheet.tsx:384` | 🟡 — functionally works, but no `paused_at` timestamp modeled |
| Revoke | `handleRevoke`/`confirmRevoke` → `useRevokeStoryShare` | `ShareStorySheet.tsx:421` → `POST .../share/revoke` (`story_shares.py:251`) | ✅ |
| Rotate | `handleRotate`/`confirmRotate` → `useRotateStoryShare` | `ShareStorySheet.tsx:404` → `POST .../share/rotate` (`story_shares.py:274`) | 🟡 — works, but creates a disconnected new row, no `replaced_by_share_id` lineage |
| Copy link | `handleCopyLink` | `ShareStorySheet.tsx:309-322` (`Clipboard.setStringAsync`) | ✅ |
| Native share link | `handleShareLink` | `ShareStorySheet.tsx:296-307` (RN `Share.share`) | ✅ |
| 9:16 card save | `handleSaveStoryCard` | `ShareStorySheet.tsx:343-362` (`MediaLibrary.saveToLibraryAsync`) | ✅ |
| 9:16 card native share | `handleShareStoryCard` | `ShareStorySheet.tsx:364-382` | ✅ |
| Preflight confidence surface | `OwnerPreflight` | `ShareStorySheet.tsx:597-620` | ✅ — confirmed advisory-only, never blocks |
| Owner-facing share metrics | `ShareStats{opens,conversions}` ← `get_share_stats` | `backend/core/models/trip_stories.py:382`, `trip_story_shares.py:481-503` | 🟡 — covers the concept, different field names/semantics than canon's `views`/`unique_viewers`/`plan_similar_starts` |
| Confirm dialogs (rotate/revoke) | `StoryShareConfirmDialogs` | `ShareStorySheet.tsx:622-661` | ✅ |

## Public/recipient side: the redacted viewer, cards, deep links

| Canon concept | Real name | Location | Status |
|---|---|---|---|
| Public Story viewer | `PublicStoryScreen` (default export) | `travel-app/app/stories/[slug].tsx` | 🟡 — renders correctly for anonymous visitors, but never differentiates owner/logged-in-vs-out (see Decision #19 in the contract audit) |
| Public JSON projection fetch | `getPublicStory` → `GET /api/public/stories/{slug}` | `data/storyShare.ts` → `story_landing.py:71` | ✅ |
| Projection builder (the "one place" canon wants) | `build_public_story_payload()` | `backend/core/story_projection.py:102-218` | ✅ — real single-source builder |
| `RedactionPolicy` model | same name | `backend/core/models/trip_stories.py:220-232` | 🟡 — 3 of 8 canon fields shipped |
| `PublicStoryProjection` model | `PublicTripStory` | `backend/core/models/trip_stories.py:282-313` | 🟡 — all canon field names present, several (`generalized_place_chips`, `route_cue`) permanently unpopulated |
| Title-safety filter | `safe_hero_title()` | `story_projection.py:70-82` | 🟡 — catches private-signal/names, **not** destination-in-title (LEAK 1) |
| Slug → policy → projection resolver | `get_public_story_by_slug()` | `backend/core/db/trip_story_shares.py:607-637` | ✅ |
| Auto people-name redaction | `_non_owner_member_names()` | `trip_story_shares.py:530-563` | 🟡 — real, but blunt (drops whole section/title rather than natural-prose rewrite); not owner-toggleable |
| Photo allowlist (trust boundary) | `_public_photo_urls()` | `trip_story_shares.py:566-604` | ✅ — real hardening against co-traveler private photos |
| Owner-vs-anonymous routing hint | `PublicStoryViewerContext` + `GET .../viewer-context` | `trip_stories.py:315-326`, `story_landing.py:84-113` | ⚫ — built correctly server-side, **zero FE consumers** (Decision #19 violation) |
| "Public unavailable" state (FE) | `PublicUnavailableState` | `travel-app/components/external-share/PublicUnavailableState.tsx` | ✅ (in practice) — supports a `reason` prop that could leak specificity, but every real call site here passes the generic reason |
| "Public unavailable" state (BE) | `_error_html()` + uniform `None`/404/410 | `story_landing.py:246`, `trip_story_shares.py:607-619` | ✅ — revoked/paused/wrong-visibility all collapse identically |
| OG/rich-preview metadata | `_og_description()` + HTML `<meta>` block | `story_landing.py:56-64, 182-243` | 🟡 — respects redaction for everything except the title (LEAK 1) |
| Not-installed web fallback | `story_landing` HTML route | `story_landing.py:137-243` | ✅ |
| 9:16 share card renderer | `render_story_card()` / `build_story_card_png()` | `backend/core/story_card.py:149-207, 280-324` | 🟡 — respects most redaction, **not** the map thumbnail (LEAK 2) |
| Card's map-thumbnail fetch | `_place_lonlat_for_trip()` | `story_card.py:227-316` | ❌ (as a redaction-aware component) — independently queries raw `places`/`trips`, never consults `RedactionPolicy` |
| iOS deep-link claim | `apple-app-site-association` (`/stories/*`) | `backend/api/routes/invite_landing.py:287-314` | ✅ |
| Android deep-link claim | `intentFilters` (`pathPrefix: "/stories"`) | `travel-app/app.json:53-64` | ✅ |
| Logged-in vs logged-out differentiation on open | — | — | ❌ — not built; viewer always renders the same anonymous state |

## Plan Similar / Inspired Trip

| Canon concept | Real name | Location | Status |
|---|---|---|---|
| Pre-auth seed preview | `PlanSeedPreview` | `app/stories/[slug].tsx:209` | ✅ |
| "Start" trigger | `handlePlanSimilar` | `app/stories/[slug].tsx:324-327` | 🟡 — only flips local state, doesn't navigate anywhere real (Decision #16 violation) |
| Fake in-place "conversation" | `PlanCTA` + `planSimilarOpeningLine`/`planSimilarPrompt` | `app/stories/[slug].tsx:235-307` | ❌ (as a real conversation) — static hardcoded strings styled to look like a chat turn |
| Real conversational entry (unused by this feature) | `ConversationSeed` / `parseSeed` | `travel-app/utils/conversationSeed.ts:71,99` | N/A — exists, correctly built for Trip Creation, **never imported by Plan Similar** |
| Real concierge chat screen (unreached) | `app/(tabs)/concierge/chat.tsx` | lines 29, 181 | N/A — real and working for its actual callers, **never reached from Plan Similar** |
| "Save" trigger (auth-gated) | `handleSavePlanSimilar` → `createTripFromPublicStoryShare` | `app/stories/[slug].tsx:329-345` → `POST /api/plan-similar` (`plan_similar.py:42`) | ✅ — correct 401→sign-in redirect |
| Pre-auth seed fetch | `GET /api/public/stories/{slug}/plan-seed` | `backend/api/routes/plan_similar.py:32-39` | ✅ — correctly unauthenticated |
| Seed generator (projection-only input) | `build_plan_seed()` | `backend/core/story_projection.py:270-344` | ✅ — Decision #11 clean |
| `PlanSimilarSeed` model | same name | `backend/core/models/trip_stories.py:366` | ✅ — all canon fields present, correct exactness-gating on `carried_places`/`destination_seed` |
| Derived-trip creation + attribution write | `create_trip_from_share()` | `backend/core/db/plan_similar.py:183-213` | 🟡 — attribution write is correct and correctly place_id-gated; but see below, nothing reads it back |
| Attribution persistence | `trip_sources` table / `_create_trip_with_source` | `plan_similar.py:98-143` | 🟡 — write-only, no FE read path (Decision #17 gap) |
| Inspired Trip post-save UI | — | — | ❌ — grep across `components/trip/`, `app/(tabs)/trips/` for `TripSource`/`source_share_id`/"Inspired Trip" returns zero matches |
| Attribution copy | `"Inspired by a public Vesper story"` | `plan_similar.py` / `story_projection.py:336` | 🟡 — consistent throughout code, but diverges from canon's mandated `"Based on a shared Vesper story."` |

## Analytics / event tracking

| Canon event | Real equivalent | Status |
|---|---|---|
| `story_share_preview_opened` | `logShareEvent('view','preview_recipient')` | 🟡 — different taxonomy, folds into generic `MemoryInteractionCreate` |
| `story_share_created` | `logShareEvent('share','create_share')` | 🟡 (same) |
| `story_share_copied` | `logShareEvent('share','copy_link')` | 🟡 (same) |
| `story_share_native_shared` | `logShareEvent('share','share_link')` | 🟡 (same) |
| `story_card_saved` | `logShareEvent('save','save_story_card')` | 🟡 (same) |
| `story_card_shared` | `logShareEvent('share','share_story_card')` | 🟡 (same) |
| `story_share_paused` | `logShareEvent('share','pause_share')` | 🟡 (same) |
| `story_share_revoked` | `logShareEvent('share','revoke_link')` | 🟡 (same) |
| `story_share_rotated` | `logShareEvent('share','rotate_link')` | 🟡 (same) |
| `public_story_open_in_app_tapped` | — | ❌ — no FE tracking call exists at all |
| `public_story_plan_similar_tapped` | — | ❌ — `handlePlanSimilar` fires no event, client or server |
| `plan_similar_seed_started` | `plan_similar_started` (server, but fires at **save**, not seed-screen-reached) | 🟡 — name survived, lifecycle meaning didn't |
| `plan_similar_seed_saved` | (folded into `plan_similar_started` above) | ❌ — no distinct save-completion event |
| Underlying persistence pipe | `POST /api/memory/interactions` → `log_interaction` | ❌ — table dropped 2026-06-20 per its own docstring; only `save`/`share` interaction-types survive as a folded engagement observation, everything else is silently discarded |
| Server-side page-view event (no canon equivalent) | `event_type="opened"` in `trip_story_share_events` | ✅ exists, but fires on every page load, not a discrete CTA-tap moment |

## Summary counts

- **Fully built & correct**: ~19 of the ~50 rows above.
- **Built but partial/misnamed/misfiring**: ~22 rows — the largest bucket. Mostly: narrower data contracts than canon, analytics under the wrong taxonomy, and two components (title-safety filter, card renderer) that handle *most* but not all redaction cases.
- **Built server-side but completely unconsumed (orphaned)**: 1 — the owner-routing `viewer-context` endpoint. Cheapest real fix in this whole audit (BE done, FE wiring only).
- **Not built at all**: ~8 rows — real conversational Plan Similar continuation, Inspired Trip post-save UI, logged-in/out differentiation, full pre-publish preview, most Plan-Similar-side analytics.

This inventory, read against the product-contract audit's fix-order, gives a natural triage: fix the 2 leaks (both are in the "partial" bucket, narrow surgical fixes) → wire the 1 orphaned endpoint (near-free) → decide what to do about analytics (policy call, not a code gap) → scope the "not built" bucket as deliberate follow-up work, not urgent bugs.
