# Code Alignment — Atlas Batch D: The Bug Batch (2026-07-06)

Repos: `~/travel-workspace/travel-app` (FE) + `~/travel-workspace/travel-agent` (BE), branch main. Follows Batch A+B+C. Theme: fix the real defects the PM journey audit found (docs/atlas/atlas-user-journeys-2026-07-06.md). These are correctness fixes with obvious right answers — no product decisions.

Process: `git status` first. Branch from main. One commit per task. No push without approval. After each: `tsc` + FULL `TZ=UTC npx jest` / BE `pytest` + `mypy`.

---

## D1 — Long View silently under-counts "the whole corpus"

**Bug:** `count_timeline_entries_grouped` (`backend/core/db/atlas_timeline.py:400-411`) fetches with `.limit(2000)` and **no `.order_by()`** → Postgres returns an arbitrary 2000 rows, so year/city counts are nondeterministic across refetches, and a >2000-row corpus is silently under-counted (the §7 "whole corpus" promise broken). The endpoint returns `truncated=True` (`api/routes/atlas.py:2563`) and the FE model carries it (`data/atlas.ts`), but `long-view.tsx` never reads it — no banner, no signal.

**Fix:**
- Add `.order_by(occurred_start.desc())` (or a stable key) so the limited window is deterministic.
- Surface `truncated` in the Long View `IndexShell` header when true — an honest "showing your most recent N" note. Do NOT silently show partial data as complete.
- Consider raising the cap or paginating the aggregation if realistic corpora exceed 2000 (report the call).
- Test: deterministic counts across two calls; truncation note renders when the flag is set.

## D2 — Undated bucket is a dead-end drill

**Bug:** `openYear` routes `Undated` → `atlasLongView({year: 0})` (`app/atlas/long-view.tsx:127`); the drill calls `useAtlasTimelinePaged({year: 0})`; year 0 fails `_validate_timeline_year` (`atlas.py:2433`) → 422 → generic "Couldn't load this chapter." Undated memories are countable but unreachable.

**Fix:** give the paged endpoint an explicit `undated=true` mode (returns entries with null `occurred_start`), and route the Undated chapter to it — OR, if undated entries shouldn't be drillable, drop the chevron/tap affordance on the Undated row. Pick the one truer to the vision (drillable is better — they're still memories). Test the chosen path.

## D3 — On This Day push deep-links to the wrong place

**Bug:** the push names a specific memory ("On this day, 3 years ago — Lisbon.", `backend/api/routes/notifications/push.py:462`) but the destination for `intent==='on_this_day'` routes to the generic `atlasLongView({mode:'time'})` index (`utils/notificationDestination.ts:70-71`). The in-app strip already does it right (`AtlasOnThisDay.tsx:29-34` deep-links per-item to artifact/candidate/trip). When `ANNIVERSARY_PUSH_ENABLED` flips, tap-through lands users on the whole-Atlas index to hunt for the named memory — opposite of "opens with meaning."

**Fix:** thread `source_type`/`source_id` (or the artifact/candidate id) into the push payload and route `on_this_day` to the specific item, mirroring `AtlasOnThisDay.tsx`. Feature stays dark, but the routing is correct for when it lights. Test the destination resolution.

## D4 — Scanned photos die on device change/reinstall (permanence)

**Bug:** scanned photos are opaque PHAsset `localIdentifier`s (`utils/atlasCluster.ts:238`), rendered as `ph://${id}` (`candidate/[id].tsx:313`, `artifact/[id].tsx:355`). On reinstall / new device / restored library, every artifact hero + photo strip breaks to the `image-outline` fallback — the *visual* memory silently evaporates while the prose survives. There's no rehost of scanned photos (only the separate `uploadAtlasPhoto` for postcards). Fatal longevity risk for a "private memory instrument."

**Fix (scope carefully — this is the biggest task in D):**
- The trip-photo path already rehosts device photos to CDN (multipart → `rehost_from_bytes`, per the memory notes on atlas photo upload). Mirror that for the photos a user KEEPS into an artifact: on approve/keep, rehost the artifact's selected photos to stable URLs and store those alongside (not replacing) the PHAsset IDs — PHAsset for fast local render, stable URL as the durable fallback.
- Respect the privacy contract: only rehost photos the user *kept into an artifact* (the deliberate keep IS the consent moment) — never during the scan (metadata-only by promise). Confirm the trust copy still holds.
- Render: artifact/candidate photo components prefer the stable URL when the PHAsset fails to resolve (crossfade, no layout shift).
- If full rehost is too large for this batch, at minimum: (a) detect the broken-PHAsset state and show an honest "this photo isn't available on this device" instead of a generic broken-image icon, and (b) file the rehost as its own follow-up. Report which you did.
- Tests: a kept artifact's photos survive a simulated PHAsset-resolution failure via the stable URL (or the honest unavailable state renders).

---

## Explicitly OUT of Batch D
- The seam / Learning Signal / dispute-scope (Batch C). Provenance glyphs, freshness states, hero/cold polish, virtualization (Batch E). Re-engagement flag flips (dogfood-timing).

## Definition of done
D1: deterministic Long View counts + honest truncation note. D2: Undated drillable (or affordance removed). D3: On This Day push routes to the named memory. D4: kept-artifact photos survive device change (rehost) OR an honest unavailable state + filed follow-up. Green tsc + FE jest (full) + BE pytest + mypy. Report: the D1 cap call, the D2 chosen path, and the D4 scope (full rehost vs honest-state).
