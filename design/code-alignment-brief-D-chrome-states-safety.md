# Code Alignment — Batch D: Chrome, States & Safety Net (2026-07-05)

Repo: `~/travel-workspace/travel-app` (+ one backend test in `~/travel-workspace/travel-agent`). Canon: `~/travel-workspace/design/vesper-canon-anchor/project/` (read-only). Same standing rules. This is the final alignment batch.

## Task D1 — Narration band stack discipline
Canon: `chat-narration-band.jsx` — max 2 banners visible; priority order **live-companion > lease-conflict > geofence > location-permission**; excess defers or collapses into the top banner's subtitle. Code: `app/(tabs)/concierge/chat.tsx` (~1110-1170) stacks all four unconditionally. Build the priority/cap logic per canon; verify each banner's visual form against the canon component rows (snap rule).

## Task D2 — SessionRecovery interstitial
Canon: `session-recovery.jsx` in State System — the hard-lapse moment (silent token refresh failed → user bounced). Code: `utils/api/http.ts` + `tokenStore.ts` already do single-flight refresh + retry-once; the failure path today redirects with no designed moment. Build: the calm SessionRecovery interstitial (no error-red; "sign back in and you'll be right where you were") + post-recovery return to the interrupted screen (not home), with StaleNotice if content refreshed. The soft path stays invisible — do not add UI to successful refreshes.

## Task D3 — ConsequenceBanner two-tier conformance
Canon: `consequence-banner.jsx` — persistent banner = happened-while-away; fading receipt toast = watched-it-happen; banner clears on dismiss OR on visiting the acted-on surface; only recorded kinds carry Undo. Code: `components/ui/ConsequenceBanner.tsx` + `context/ConsequenceContext.tsx`. Audit code behavior against the rules (especially clear-on-visit and which kinds expose Undo); align divergences; verify visual anatomy (sparkles + title + dismiss) against canon.

## Task D4 — Universal Search entry points: Atlas + Vesper tabs
Canon prescribes five scoped entries (Discover · Trips Home · Single Trip Home · Atlas · Vesper — same overlay, different scoped hints). Code has three; **no `universalSearch()` call exists in the Atlas or Vesper/concierge tabs**. Add both entries with their scoped hints per the Universal Search canon page. (Atlas is design-out-of-scope but the entry affordance is Universal Search's canon, not Atlas's.)

## Task D5 — Public-projection shape test (backend, travel-agent repo)
The safety pin from the edge-journey audit. Public surfaces: `invite_landing.py` (`InviteViewResponse` — destination names only, human date_window), `story_landing.py` (title, meta, cover, "Planned with {planned_with}", OG/Twitter meta), FE `app/public/place|venue`. Do a field-by-field audit of every serialized field against Trip Story's redaction rules + External Sharing's recipient-entry rules (canon: `trip-story-app-b.jsx` redaction boards; `vesper-external-sharing-app.jsx` privacy doctrine). Special attention: `planned_with` naming (real names leaking to signed-out viewers?) and OG meta on story pages (cached by scrapers — revocation can't recall it). Then PIN the projections with a shape test: a test that fails if any new field is added to a public response model without an explicit allowlist entry. Flag any field the audit finds questionable — do not silently widen or narrow projections without reporting.

## Done
Five commits (D5 in travel-agent) · banner cap+priority live · SessionRecovery ships · consequence rules conform · five search entries exist · projection shape test green and pinning an explicit allowlist · final report: token mismatches, flagged fields, anything stopped-on.
