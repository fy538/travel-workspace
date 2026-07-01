# Vesper v1 — MVP Scope & Flag Manifest

> Status: scope locked (2026-06-30) — ready to execute
> Owner: founder / engineering
> Created: 2026-06-30
> Source of truth for: what ships in the first production release, what is hidden, and how

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
| Auth (Clerk) + onboarding | — | Live-transport JWT gap must close (see DoD) |
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
   - Close the live-transport gap (Clerk JWTs for `dogfood-journey-live-api`).
   - Device full-cert J04/J05/J10(-minus-booking-transaction) — the `0/12 full` gap.
   - Proactive proposal generation (the named launch gap — agent drives the shipped
     Propose UX from trip events).
   - Full-group multi-user QA pass.
8. **Then** release feature-by-feature: each OUT flag flips only after its own certify
   pass (journey + device + eval where relevant).

---

## Definition of done — "v1 in production"

- [ ] FE flag layer live; OUT set unreachable in a release build; zero dead/OUT CTAs
- [ ] Booking record stub works with transaction engine off
- [ ] Expenses `rate=1.0` bug fixed
- [ ] Reachability audit clean (no OUT reachable; no IN broken)
- [ ] Golden path J01–J12 device-walked green on a real build (booking-transaction excepted)
- [ ] Live-transport gap closed (Clerk JWTs) — `make dogfood-journey-live-api` green over HTTP
- [ ] App Store review assets current (privacy, review notes, mic-permission copy)
- [ ] This doc `Status: active` and linked from `docs/systems/README.md`
