# Vesper v1 — MVP Scope & Flag Manifest

> Status: scope locked — flag gating LIVE as of 2026-07-01
> Owner: founder / engineering
> Created: 2026-06-30 · Last updated: 2026-07-06 (Clerk/live-transport rows corrected;
> booking + venue-disruption gates explicitly reaffirmed — see notes below)
> Source of truth for: what ships in the first production release, what is hidden, and how

> **2026-07-06 correction:** every "Clerk JWTs" / "live-transport gap" row below previously
> read as an external Clerk blocker. It isn't. Per [STATUS.md](../journeys/STATUS.md)'s
> 2026-07-05 correction: it's ~3-5h of unbuilt *internal* glue (test Clerk accounts + SQL
> backfill of `external_auth_id` + a JWT-mint script) for one automated CI harness
> (`dogfood-journey-live-api` over HTTP), and it's a CI-automation nice-to-have, **not a
> shipping blocker** — the actual device-certification gate for J04/J05/J10 runs on real
> Clerk accounts on two physical devices and never touches this harness at all. Rows below
> are annotated inline; treat "🔲" on these specific rows as "not built, not urgent," not
> "blocked."

> **2026-07-06 decision — the two remaining MVP gates:** reviewed whether the booking
> transaction engine or proactive proposal generation need to flip before the dogfood
> cohort launches. Neither does:
> - **Booking (`BOOKING_DUFFEL_LIVE_BOOKING_ENABLED` + `EXPO_PUBLIC_LIVE_BOOKING_ENABLED`):**
>   this was already decided 2026-06-30 (see decision record below) — transaction engine
>   OUT/flagged, non-transacting stub IN. Reaffirmed, not reopened.
> - **Proactive proposal generation (`VENUE_DISRUPTION_PROPOSALS_ENABLED`):** genuinely open
>   until now. Decision: stays dark for dogfood cohort 1. The cohort's job is to validate the
>   invite/group-planning loop (belief #14) via explicit propose/vote/revert, which is already
>   agent-certified — it doesn't need the agent proactively drafting proposals from trip
>   events. Flipping an unevaluated proactive surface on for a real friend group's first
>   impression carries the same fake-personalization risk the design-canon audits keep
>   flagging elsewhere. **Next explicit decision, not an open gap:** evaluate this producer
>   against real cohort-1 usage data, then decide whether to flip it for cohort 2.
> See `docs/flags/registry.yaml` for the flag-level record of both.

## Implementation status (2026-07-01)

### Phase A — FE flag layer ✅ COMPLETE

`travel-app/constants/featureFlags.ts` rebuilt as the single import point:
- `VOICE_ENABLED` re-exported from `utils/voiceEnabled.ts` (env-driven `EXPO_PUBLIC_VOICE_ENABLED`)
- `POSTCARDS_ENABLED = false`
- `AMBIENT_ENABLED = false`
- `STORY_SHARE_ENABLED = false`
- `DOSSIER_VOICE_STUB = false`

**Route redirect guards** (`<Redirect href="/atlas" />` wrapper pattern): `atlas/voice-logs`,
`atlas/narration-history`, `atlas/postcards`, `atlas/shared-links`, `atlas/unpacked-card`.

**CTAs hidden** (10 touch points): account voice trust-rows; Atlas-home postcards shelf cards
(warm + cold grid); `AtlasTripState` postcards ThinRoom; `MakePostcardButton` (artifact
screen); atlas/unpacked "SHARE YOUR YEAR"; trip-story "Share story" header action; live-trip
`liveAmbientCards`; mic `onVoice` at both concierge call sites.

**Voice gated at source**: `NarrationListenButton` + `StoryListenButton` return null when
`!VOICE_ENABLED` — covers venue detail, NowModeStrip, PlanBlockRow, story.

**Verification:** `tsc --noEmit` exit 0. Zero TS errors.

### Phase B — BE story-share guard ✅ COMPLETE

`story_sharing_enabled()` + `venue_disruption_proposals_enabled()` added to
`backend/core/feature_flags.py`. Guards on `create_story_share` (`story_shares.py`) and
`create_atlas_unpacked_share` (`atlas_unpacked.py`) → 403 when off. No new unauthenticated
public share links can be minted. Tests: 19 passed incl. `test_create_403_when_sharing_disabled`.

### Phase 7 — Proactive proposals: venue-disruption producer ✅ SHIPPED DARK

New producer: closed venue → swap proposal → existing Propose UX. Ships dark
(`VENUE_DISRUPTION_PROPOSALS_ENABLED=false`).

- `backend/core/venue_disruption.py` — pure precision-first detector (8/8 unit tests)
- `backend/concierge/proactive.py` — `_produce_venue_disruption` producer + registration in
  `collect_legacy_candidates`
- `backend/notifications/arbiter.py` — `CandidateType.VENUE_DISRUPTION`
- `tests/core/test_venue_disruption.py` (8 tests) + `tests/concierge/test_venue_disruption_producer.py` (5 Postgres-gated tests)
- Flag: flip `VENUE_DISRUPTION_PROPOSALS_ENABLED=true` in a seeded env to activate; requires
  eval pass before prod.

**Audit corrections vs original manifest** (grounded in code):
- `atlas/scan` (Add entry) and `atlas/reel` (board player) are **IN** — not postcards.
- The concierge "notices strip" is error/lifecycle recovery UI, not ambient — untouched.
- **Booking**: transaction engine already gated by `EXPO_PUBLIC_LIVE_BOOKING_ENABLED` (FE)
  + `live_booking_enabled` (BE); the "mark as booked" record path remains IN. No new code
  needed.
- **Expenses `rate=1.0`** already fixed in `auto_log.py:124`.

**Uncommitted in working tree** (~12 BE files, ~23 FE files). Branch/commit before next build.

### Remaining to close v1 DoD

| Item | Status |
|---|---|
| Flag layer live + typecheck green | ✅ done 2026-07-01 |
| BE story-share guard | ✅ done 2026-07-01 |
| Expenses `rate=1.0` fixed | ✅ already fixed |
| Booking record stub works with engine off | ✅ no code needed (pre-existing gate) |
| Commit Phase A/B/7 work to branch | ✅ merged to origin/main (Phase A: `6a5177d4`, Phase B: `a2489737`, Phase 7: `1251fc0d`) |
| Reachability audit (device walk, release flags) | 🔲 needs EAS build |
| J01–J12 device-walked on a real build | 🔲 0/12 full-cert (logic 12/12) |
| Live-transport gap: Clerk JWTs for dogfood HTTP | 🔲 not blocked, not built — internal glue only (~3-5h); does not gate device-cert (see 07-06 note above) |
| App Store review assets current | 🔲 |
| Proactive proposals flag-on eval (seeded env) | 🔲 *(deliberately deferred to post-cohort-1 — see 07-06 decision note above, not an open gap for v1 launch)* |

---

## Purpose

Draw one hard line: what is **in** the first production release ("v1"), what is
**hidden behind a flag** (kept in code, unreachable in the UI), and the mechanism
that enforces the line. Everything downstream — hardening, QA, the certify ladder,
the release checklist — targets the **IN** set only.

This doc is the front door for the "ship v1, then release feature-by-feature" plan.
It replaces ad-hoc flag decisions with one manifest.

---

## Decision record (2026-06-30)

Founder decisions that scoped this doc:

1. **Wedge shape:** **Full group** — create + invite + membership/roles + group-chat
   facilitator all ship.
2. **Contested surfaces IN:** Post-trip Story · Atlas memory hub · Discover feed ·
   Universal Search.
3. **Expenses / settlement:** **IN** (completes J12) — requires fixing the
   cross-currency `rate=1.0` bug first.
4. **Booking:** transaction engine (Duffel / cart / hold) **OUT/flagged**; keep a
   non-transacting **"mark as booked" + external deep-link** stub IN.
5. **Social:** profiles + people-search + **follow/unfollow + following list** IN;
   **story-sharing / social distribution OUT/flagged**.
6. **Cut posture:** flag-off the OUT set; **delete nothing**.

> Honest scope note: after these calls, the only things hidden in v1 are **live voice,
> the booking transaction engine, postcards, ambient/nearby, and story-sharing**.
> Everything else ships. v1 is "the full concierge product minus the genuinely
> experimental pieces," not a minimal wedge. The work ahead is **hardening a large
> surface** (including full-group multi-user QA), not shipping a narrow one. This is a
> deliberate, thesis-true choice.

---

## The v1 golden path

**vague idea → Vesper plans it → the group refines it by proposing edits → it's useful
on the trip → it comes home as a story, and the group settles up.**

Covers canonical journeys **J01–J12** (all lived-certified 12/12 as of 2026-06-29),
with J10 partially deferred (booking transaction hidden; expense + "mark as booked"
paths remain).

---

## IN — v1 surfaces (harden to production)

| Surface | Systems | Notes |
|---|---|---|
| Auth (Clerk) + onboarding | — | Real Clerk auth already live; the automated persona-JWT harness gap (see DoD) is a CI nice-to-have and does not block this surface |
| Trips: create, **full group invite + membership + roles** | Trips/Folio, Group/Social | Heaviest QA surface |
| Group chat + facilitator | Group/Social | Merged to main 2026-06-30 |
| Planning / itinerary generation | Planning/Itinerary | Grounded in world model (the moat) |
| Proposals / Change Studio (edit · accept · revert) | Proposals/Change Studio | Propose stage shipped; proactive generation still a gap |
| Concierge (Vesper) chat | Concierge | Core spine |
| Memory & Preference (Personal Memory, group profile, Travel DNA) | Memory & Preference | Core spine |
| Trip Home / Folio + Now Mode (live trip) | Trips/Folio | Server-authored read model |
| Post-trip Story | Postcard/Story (story only) | Narrative artifact IN; postcard *render* OUT |
| **Expenses / settlement** | Expenses/Settlement | **Fix `rate=1.0` cross-currency bug before launch** |
| Atlas memory hub | Atlas | Full hub minus OUT sub-screens (voice-logs, narration-history, postcards, scan, reel) |
| Discover feed (Reading Room) | Discover | Load-bearing: feeds trip creation via ConversationSeed |
| Universal Search (**incl. People**) | Cross-cutting | People results route to profiles (IN) |
| **Social: profiles + follow/unfollow + following** | Group/Social | Story-sharing/distribution excluded (flagged) |
| Booking record stub ("mark as booked" + deep-link) | Booking (thin) | Transaction engine flagged off |

## OUT — flagged off in v1 (code kept, UI unreachable)

| Surface | Flag | Why deferred |
|---|---|---|
| Live voice / narration / mic / "hear the read" | `FLAG_VOICE` | Never run E2E; BE `VOICE_ENABLED` already off |
| Booking transaction engine (Duffel, cart, hold, sessions) | `FLAG_BOOKING` | Over-built, dark, risky; keep record stub only |
| Postcards (img2img riso, scan, reel) | `FLAG_POSTCARDS` | On-device paint unvalidated |
| Ambient / nearby | `FLAG_AMBIENT` | Phase 5+ layer; no v1 job |
| Story-sharing / social distribution | `FLAG_STORY_SHARE` | Profiles + follow IN; public distribution deferred (J19 privacy) |
| Anniversary + seasonal pushes | `ANNIVERSARY_PUSH_ENABLED`, `UNPACKED_SEASONAL_PUSH_ENABLED` | Already BE-flagged off |
| Surprise trip, creator layer | (not built) | Future |

---

## Flag manifest (coarse, surface-boundary)

**Principle:** gate at the **navigation / route boundary**, never sprinkle
`if (flag)` through business logic. One flag per hidden *surface*, default-off. Few
coarse flags — not many fine ones. Build on the existing SSOTs; do not fork a parallel
mechanism.

**Existing SSOTs to extend:**
- Frontend: `travel-app/constants/featureFlags.ts` (currently ~empty — build this out to
  support **surface + sub-surface** gating; single import point)
- Backend: `travel-agent/backend/core/feature_flags.py` (`_truthy(ENV)`; keep for
  background loops / server features)

### Frontend surface flags (v1 values)

| Flag | v1 | Gates these routes/components |
|---|---|---|
| `FLAG_VOICE` | `false` | live-trip narration strip · guide voice · `atlas/voice-logs` · `atlas/narration-history` · mic |
| `FLAG_BOOKING` | `false` | `booking/[sessionId]` · Duffel/cart/checkout/hold CTAs (keep "mark as booked" + deep-link) |
| `FLAG_POSTCARDS` | `false` | `atlas/postcards` · `atlas/scan` · `atlas/reel` · "make a postcard" |
| `FLAG_AMBIENT` | `false` | ambient/nearby notices |
| `FLAG_STORY_SHARE` | `false` | public share link · og:image landing · `atlas/shared-links` · story social distribution |

> **IN, not flagged:** expenses/settlement, social profiles + follow/unfollow +
> `atlas/following`, `profile/[userId]`, Universal Search incl. People.
> Atlas hub is IN; only the OUT sub-screens above are gated inside it.

### Backend — minimal new gating for v1

Endpoints for OUT surfaces may stay reachable at the API layer (simply uncalled by UI).
Heavy background loops are already env-gated. Add a `403`/`404` guard on booking-
transaction + voice routes as defense-in-depth (low priority).

---

## Execution plan

1. **Build the FE surface-flag layer** in `featureFlags.ts` (surface + sub-surface
   booleans, single import point). *(travel-app)*
2. **Wire flags at nav/route boundaries** — tab layouts, route guards, CTA render
   guards for the OUT set. Hidden = unreachable, no dead CTAs. *(travel-app)*
3. **Booking record stub** — ensure "mark as booked" + external deep-link path works
   with the transaction engine flagged off. *(travel-app + travel-agent thin)*
4. **Fix expenses `rate=1.0` cross-currency bug** (blocks Expenses being IN). *(travel-agent)*
5. **Reachability audit** — walk every entry point; confirm no OUT surface is reachable
   and no IN surface lost a load-bearing dependency (Discover→trip-create, Atlas→Story,
   Search→profiles). *(travel-app)*
6. **Optional BE route guards** on booking-transaction/voice. *(travel-agent)*
7. **Harden the IN path to production** — the real work:
   - *(non-blocking, CI nice-to-have — not required for the items below)* Build the
     live-transport JWT harness (`dogfood-journey-live-api` over HTTP): test Clerk
     accounts + JWT-mint script, ~3-5h.
   - Device full-cert J04/J05/J10(-minus-booking-transaction) — the `0/12 full` gap.
     Runs on real Clerk accounts on two physical devices; does not depend on the item above.
   - Proactive proposal generation (the named launch gap — agent drives the shipped
     Propose UX from trip events).
   - Full-group multi-user QA pass.
8. **Then** release feature-by-feature: each OUT flag flips only after its own certify
   pass (journey + device + eval where relevant).

---

## Definition of done — "v1 in production"

- [x] FE flag layer live; OUT set unreachable in a release build; zero dead/OUT CTAs — ✅ 2026-07-01
- [x] Booking record stub works with transaction engine off — ✅ pre-existing gate confirmed
- [x] Expenses `rate=1.0` bug fixed — ✅ already fixed in `auto_log.py:124`
- [ ] **Commit Phase A/B/7 work to a branch** (working tree currently dirty ~35 files)
- [ ] Reachability audit clean (no OUT reachable; no IN broken) — needs EAS build + device
- [ ] Golden path J01–J12 device-walked green on a real build (booking-transaction excepted)
- [ ] *(non-blocking — not required for v1)* Live-transport JWT harness built —
      `make dogfood-journey-live-api` green over HTTP. TestClient path is already
      15/15 green; this only automates the persona-JWT CI path and does not gate
      device-cert above.
- [ ] App Store review assets current (privacy, review notes, mic-permission copy)
- [ ] This doc `Status: active` and linked from `docs/systems/README.md`
