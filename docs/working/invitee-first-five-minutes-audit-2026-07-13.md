---
doc_type: working
status: active
owner: founder / product / engineering
created: 2026-07-13
last_verified: 2026-07-13
expires: 2026-08-12
why_new: No existing document owns the invitee-side first-touch experience as a full-stack (design + backend + frontend) audit; J02/J18 certify plumbing contracts only. This audit grounds the pre-cohort fix list for the distribution wedge.
supersedes: []
source_of_truth_for: [invitee-first-five-minutes-audit]
---

# The Invitee's First Five Minutes — Full-Stack Audit

## Executive finding

**This surface is not another itinerary.** The itinerary failed because its domain
model was incoherent (five concepts fused into overloaded controls, no single
authority spine) and required a redesign. The invitee path has a **coherent,
well-designed core** — the invite landing is arguably the best-crafted screen in
the app — surrounded by a **ring of last-mile fractures**, plus **one missing
thesis moment that design, backend, and frontend are all missing together**.

It needs a bounded punch list and one designed moment, not a redesign.

The two broken paths are the two *most common* real-world paths:

1. **Link tap with no app installed** (every first-ever user) — the invite token
   dies at the App Store; there is no deferred deep link.
2. **Group-share multi-use link** (the likely-dominant organizer behavior: one
   link dropped into the group chat) — joins work, but the invitee's signal
   contribution silently goes nowhere while the UI claims it was saved.

And the thesis moment — belief #14's *"each invited person gets a personal
reason to be excited and a low-friction way to contribute"* — currently ends at
a toast. The invitee gives signal; nothing they ever see reflects it.

## Why this journey matters

- The multiplayer invite loop is the **one unvalidated load-bearing bet**
  (see `dogfood-loop-validation-2026-07-04.md` and
  `project_monetization_reality_check`). Cohort-1's green threshold is a
  ≥20% re-invite rate; that rate is downstream of these five minutes.
- At the time of this audit, J18 was a **visible skip** in persona-cert because
  the signed-out auth detour was not exercised by the in-process certifier.
  That certification gap closed on 2026-07-19 with a disposable invitee walk;
  this audit remains the felt-experience trace.
- J02/J18 are **plumbing contracts** (token survival, membership correctness,
  no leaks). Neither says a word about warmth, representation, or first value.
  The certified bar for this path is "doesn't break," not "feels like joining
  a trip." That gap is what this audit covers.

## Method

Three parallel code/design-grounded traces on 2026-07-13, synthesized here:

1. **Design canon** — `~/Downloads/vesper 166/project/` handoff bundle:
   `Vesper Auth and Invite.html` (CANON, "implement from here"),
   `Vesper Onboarding.html` (Path 4 · Invite), `Vesper People and
   Collaboration.html` (companion), `Vesper External Sharing & Public Entry
   Points.html` (appendix: shell mode D, link-state taxonomy), plus their
   `.jsx` canon imports (`auth-invite-app.jsx`, `onboarding-canon-invite.jsx`,
   `people-collab-app.jsx`, `vesper-external-sharing-app.jsx`).
2. **Backend** — `travel-agent`: `backend/api/routes/invites.py` (1,306 lines),
   `invite_landing.py`, `core/db/trip_invites.py`,
   `concierge/invite_snapshot.py`, `api/routes/_membership_events.py`,
   `scripts/invite_loop_funnel.py`.
3. **Frontend** — `travel-app`: `app/invite/[slug].tsx`, `app/invite-code.tsx`,
   `utils/invitePending.ts`, auth screens (`SignInImpl.tsx`, `SignUpImpl.tsx`,
   `onboarding-safety.tsx`, `AuthRedirect.tsx`), `utils/api/http.ts`,
   mock layer, Jest + Maestro coverage.

All file:line citations below were verified in code on the audit date.

---

## What is genuinely good (verified; keep all of it)

**The invite door itself — design/code parity.**
- Value before auth: the full pre-auth trip peek renders without an account
  (`GET /api/invites/{token}` is public — `invites.py:614`;
  `app/invite/[slug].tsx:593-726`): organizer avatar + honest `+N` count (no
  fabricated member initials, `:606-619`), "{Organizer} invited you", travelers
  + dates, destination title, Haiku-personalized snapshot quote (`:89-114`),
  privacy note ("Private notes, costs, and group details stay closed until you
  accept", `:633-635`).
- **The "2-minute signal" is one screen, zero extra steps, before the auth
  wall** — exactly as designed (`ScreenInviteLanding` signal chips;
  implemented at `[slug].tsx:667-705`, submit with rollback-on-failure so a
  failed POST never shows a false "Noted ·" at `:471-478`). The backend web
  landing renders the same chips for browser visitors
  (`invite_landing.py:140-152, 284-313`).
- Substance gate: minting 409s (`trip_needs_substance`) on blank trips
  (`invites.py:258-271`; `trip_has_substance` at `db/trip_invites.py:606`) —
  no cold generic invites can exist.

**The plumbing J02/J18 worried about is solid.**
- Atomic exactly-once accept: consume + `trip_members` INSERT +
  `trip_invite_redemptions` ledger in one transaction, race-safe WHERE
  re-evaluation, loser → 410 (`db/trip_invites.py:354-454`). Already-member =
  idempotent success without burning a use (`invites.py:1105, 1139`).
  Lost-200 retry recovery incl. exhausted group links
  (`invites.py:959-1028`; `has_redeemed_invite` `db:457-478`).
- Token survives the auth detour on **all four** return sites: sign-in
  `finishAuth` (`SignInImpl.tsx:221-248`), sign-up short-circuit
  (`SignUpImpl.tsx:149-158`), OAuth tail (`onboarding-safety.tsx:51-53,
  74-76`), cold-start `AuthRedirect` (`components/auth/AuthRedirect.tsx:33-70`).
  Storage: SecureStore envelope, issued-at + 30-min TTL
  (`utils/invitePending.ts:28-59`), cleared on sign-out.
- Eight distinguishable failure states with a real disclosure model:
  pre-auth strangers get one generic "not found" for revoked/expired/gone (no
  lifecycle probing), trusted post-auth holders get exact copy
  (`[slug].tsx:116-131, 185-311, 581`). Already-joined offers "Open
  {destination}". Backend reasons machine-readable
  (`invites.py:595-600`; `is_redeemable` `db:181-191`).
- Privacy held consistently: organizer sees only "Answered privately"
  (`summarize_pending_intake`, `models:224-249`) across bell, list, push, and
  journal digest; intake is injection-scanned before reaching the concierge
  prompt (`turn_context.py:1189`); snapshot prompt bans inventing venues and
  naming the invitee; content-contract clamped (`invite_snapshot.py:270`).
- Join fan-out (D8): group-chat "X joined" line, `member.joined` audit, roster
  invalidation, organizer push (`_membership_events.py:139-170`).
- The diary gift (`InvGift` canon) is implemented and correctly deferred
  (`DeferredDiaryGiftSheet`, `chat.tsx:193-201, 774-782`) — never during join.

---

## Implemented paths, graded

| # | Path | Likely share of real cohort invitees | State |
|---|---|---|---|
| P1 | Link tap, app installed, signed in | Small (existing users) | 🟢 works, warm |
| P2 | Link tap, app installed, signed out | Small–medium | 🟡 works; greets them wrong (D3/D4) |
| P3 | **Link tap, NO app installed** | **Majority — every first-ever user** | 🔴 token dies at the App Store (D1/D2) |
| P4 | **Group-share multi-use link** | **Likely dominant organizer behavior** | 🔴 joins work; signal loop silently dead (D9) |
| P5 | Manual code paste (`/invite-code`) | Fallback | 🟢 works (`parseInviteToken` accepts URL/segment/bare token) |
| P6 | Conversation (pre-trip) invite | Unknown | 🟡 works; invisible to funnel, no join announcement (D11) |
| P7 | Re-tap own consumed link (web) | Common accident | 🟡 "already been used — ask for a fresh link" instead of "you're in" (D12) |

---

## Defect register (ranked by first-five-minutes damage)

### Tier 0 — config, not code (hours; blocks everything downstream)

- **D1 — Android invite links never deep-link.** `app.json:36-48` intent filter
  claims host `travelagent.app/invite`; invites mint
  `vesper-backend.fly.dev/invite/...` (`invites.py:93-95`). iOS `applinks:` is
  correct. Every Android invitee gets the web page even with the app
  installed. Mock invite URLs also still say `travelagent.app`
  (`mock/social.ts:887`).
- **D2a — Store buttons are placeholders.** `INVITE_APPLE_TEAM_ID=REPLACE_ME`,
  store URLs `idREPLACE_ME` (`invite_landing.py:41-66`); iOS Smart App Banner
  emitted only when `INVITE_IOS_APP_STORE_ID` is set (`:122-128`). Until the
  `INVITE_*` env set is deployed, the no-app path is web page → dead button.

### Tier 1 — the cold fractures (P0 code, days)

- **D2b — No deferred deep link.** Nothing reads clipboard/install-referrer on
  first launch. After install, the app cold-starts to the onboarding cover;
  recovery only via the small "Have an invite link?" link
  (`app/onboarding.tsx:394-396` → `/invite-code`). The most common first-ever
  experience currently ends in a cul-de-sac. Minimum viable fix without true
  deferred deep-linking: web page instructs "after installing, tap this link
  again"; make cold-start invite recovery prominent; lengthen the pending-token
  TTL for this path (30 min will not survive an App Store detour — D8a).
- **D3 — "You've been signed out" flashes at someone who has never signed
  in.** Every 401 in `_request` unconditionally calls `redirectToSignIn()` →
  `/(auth)/session-recovery` (`utils/api/http.ts:459-464, 226-262`) *before*
  the invite screen's own 401 handler (`[slug].tsx:517-521`) replaces again to
  sign-in. A brand-new invitee tapping Join sees "You've been signed out. Sign
  back in and you'll be right where you were."
  (`app/(auth)/session-recovery.tsx:36-39`) — false copy at the exact
  trust-formation moment, plus two stacked `router.replace`s racing. Fix: the
  invite route needs an opt-out from the global 401 redirect (or `_request`
  needs a public-endpoint allowlist).
- **D4 — The detour lands a likely-new user on sign-IN, not sign-up.**
  `goInviteSignIn` → `routes.signIn({mode:'invite'})` (`[slug].tsx:488-493`).
  Invitees are definitionally usually new; email/phone-OTP users burn a full
  round trip to hit "We don't have an account for that email — sign up?"
  (`SignInImpl.tsx:134-145`). Design canon frames auth as "Join Lisbon" —
  route `mode:'invite'` sign-up-first (OAuth is immune; Clerk merges).
- **D5 — Invited users skip safety intake entirely, permanently by default.**
  Pending invite short-circuits ahead of `SafetyChipsForm` (allergy +
  accessibility **hard constraints**) and clears onboarding intent
  (`SignUpImpl.tsx:152-158`; `onboarding-safety.tsx` bypassed). No deferred
  capture exists (`SafetyChipsForm.tsx:22-23` punts to settings). The member
  most likely to have meals booked by other people's plans is the one whose
  allergies Vesper never asked about. Design canon has the safety tail
  (`ScreenSafetyChips`) *inside* the invite path; implementation dropped it.
  Fix: deferred hook — the diary-gift slot is the natural place.
- **D6 — No trip-lifecycle gate on redeem.** `is_redeemable` reads only
  invite-row fields (`db/trip_invites.py:181-191`); neither
  `consume_and_add_trip_member` nor `add_trip_member`
  (`core/db/trips/members.py:42`) checks `trips.status`. Invites to
  completed/cancelled trips redeem normally until token expiry.
- **D7 — Immortal/unbounded tokens are client-mintable.**
  `expires_in_days <= 0` silently means *no expiry* (`db/trip_invites.py:87-88`);
  neither `expires_in_days` nor `max_uses` has an upper bound
  (`models/trip_invites.py:86-93`). A buggy/malicious client can mint a
  never-expiring, million-use bearer link to the trip.
- **D8 — Pending-token seams.** (a) 30-min TTL (`invitePending.ts:29`) loses
  the resume for store-detour or slow-OTP users; `AuthRedirect` then dumps
  them on Trips with no hint an invite was pending. (b) The sign-in
  interrupted-route path (`SignInImpl.tsx:229-234`) returns to the invite
  without consuming the pending token (benign ghost re-open within 30 min).

### Tier 2 — the missing thesis moment (design work, then build)

- **D9 — "Feeling represented" is unimplemented at all three layers.**
  The chips promise *"used to shape your join experience."* Then:
  - **Design**: its own biggest gap — **no artboard exists** for the trip as
    first seen by a just-joined member. "Land straight in the existing
    shared-trip home … Vesper greets you in-context there" is asserted, never
    drawn; the InvInvite "open day — yours to shape" hook has no designed
    follow-through; the chip promise has no visible payoff screen.
  - **Backend**: the only payoff channel is a concierge turn-1 acknowledgment
    (`PENDING_INTAKE_TEMPLATE`, `_prompts_templates.py:140-155`, injected via
    `load_pending_intake`, `turn_context.py:1246`) — private, single-channel,
    fires **only if the invitee opens chat**, and **only for single-use
    invites** (`invites.py:1148-1167`; `_schedule_intake_persistence`
    `:1031-1093`).
  - **Frontend**: invitee lands on the generic Trip Folio
    (`[slug].tsx:561-563`) with **no invitee-specific state**; "X joined"
    lives in a chat they haven't opened; their answer flows to the organizer
    (`tripChannelRouting.ts:38-76`) but is never mirrored back ("Noted ·"
    dies with the pre-join screen). The one proactive post-join surface is
    the diary *ask*, not an acknowledgment.
  Nothing the invitee ever sees says "the trip now knows what you said."
- **D10 — Group-share intake is quietly dishonest.** Multi-use-link answers
  append anonymously to `submissions` (`record_pending_intake`,
  `db:197-250`), are never attributed, never seeded into memory, never
  acknowledged (`invites.py:1148-1156, 1204-1211`) — but the web page says
  "Thanks — saved for when you join" (`invite_landing.py:152`) and the chips
  invite an answer. On the likely-dominant path the promise is false. Fix:
  attribute at accept time, or move chips post-join for group links.
- **D11 — The invite timeline fabricates an itinerary.**
  `buildInviteTimelineDays` invents "Arrival / Day N / Last morning" cards
  from pure date math (`utils/inviteTimeline.ts:34-60`), suppressed only when
  `snapshot.mode === 'insufficient'` (`[slug].tsx:454, 639`) — a trip with
  dates, zero itinerary, and a passable snapshot still shows an invented
  multi-day plan under "THE TRIP SO FAR" (in-file comment admits it,
  `:442-453`). The canon's E14 fabrication guard ("never invent a timeline
  from date math", `auth-invite-app.jsx:343-350`) is only partially
  implemented. Design-substrate-trap violation on the first screen a new
  user ever sees.

### Tier 3 — measurement + test integrity (you cannot see any of this happening)

- **D12 — Funnel S3 is blind to share-sheet invites.** `invite.dispatched`
  trip_events are journaled only when SMS/email actually dispatches
  (`invite_dispatch.py:244-262, 313`); manual share-sheet mints (the dominant
  mobile flow) write no trip_event, so `invite_loop_funnel.py`'s loop-closure
  stage undercounts — possibly badly. `ACTIVATION_INVITE_MINTED` covers them
  but lives only in PostHog (no key → log lines). The cohort go/no-go metric
  reads systematically low.
- **D13 — Conversation invitees are invisible.** No `invite.consumed` event on
  the conversation accept path (`invites.py:1285` documents the gap) — pre-trip
  joiners never enter S1, and there is no join announcement in the chat they
  joined.
- **D14 — The Maestro invite flow cannot fail.**
  `24-journey-02-create-invite.yaml:138-148` asserts eyebrow copy
  `"AN INVITATION"` — that string no longer exists (the screen renders kicker
  `INVITE`, `[slug].tsx:627`) — and every invite-step assertion is
  `optional: true`. The signed-out detour is untested end-to-end anywhere
  (J18's own header acknowledges this; phone-signup/signin Maestro flows
  exist but are not invite-linked). Mock hides most of the edge states: mock
  `viewInvite` produces only 404 and one 410 fault
  (`mock/social.ts:893-950`) — no expired/revoked/insufficient-snapshot
  variants; mock intake is a no-op.
- **D15 — Public intake endpoint: no rate limit, unbounded growth.**
  `POST /api/invites/{token}/intake` is unauthenticated; group-share appends
  without cap (`db:237-240`); every group-share submission triggers an
  organizer push (G-7 dedupe applies only to `max_uses==1`,
  `invites.py:782-784`). A bot with a leaked group link can buzz the
  organizer's phone indefinitely and bloat the row.
- **D16 — Web landing renders colder than its own data.** Dates, organizer
  name, member count are fetched (via `view_invite`) but never hit the
  template (`invite_landing.py:96-99` vs `:273-276`) — a browser visitor sees
  generated prose + buttons, not "Ana is planning this for 5 of you." The
  coldest render is on the no-app path — the most common first touch.
- **D17 — Organizer Personal Memory excerpt feeds a public page.** 400 raw
  chars of the organizer's memory document are handed to Haiku for the
  unauthenticated landing (`invite_snapshot.py:98-104`). Prompt rules + clamps
  mitigate; nothing structurally prevents a private detail from surfacing in
  `snapshot_text` on a link that lives in SMS threads. Consider a
  facts-only/scrubbed input instead of raw memory text (ties to the
  facts-only primitive, M1).

---

## Design canon cross-reference

What the canon covers well (see `auth-invite-app.jsx` FlowMapBoard, "13 auth
entry doors"): the invite landing + signal chips, auth-framed-as-joining with
context restated ("Your signal choices from the invite preview are saved."),
equal-weight providers, phone OTP (11 artboards), safety-chips tail, pending
handoff, 8 invite error states, signed-in fast path (`ScreenInviteSignedIn`
with taste-profile pre-selected chips), manual code board, web invite peek +
reason-disclosure doctrine, and the deferred diary gift ("Never during the
join").

Design gaps confirmed by the extraction (no artboard exists):

1. **The invitee's actual first minutes inside the trip** — the single biggest
   gap; asserted by reference to "Vesper Trip Home," never drawn (this is D9's
   design leg).
2. Conversation-invite variant (flow-map row only).
3. Trip-already-over / joining mid-trip (live) / post-trip invite states.
4. Offline during accept; offline first-session.
5. The web→store→app deferred chain (no smart-banner/store-redirect design).
6. Where "Not now — set up Vesper without joining" actually lands.
7. The SMS/email/push content the recipient receives *before* tapping.
8. Chip-privacy final semantics (deliberately open: "do not over-promise
   organizer-only access without backend confirmation").

Fixture note: Onboarding invite screens say June 12–17 / Ana, Ben & Mara /
6 days; Auth & Invite canon says Oct 12–17 / Ana, Theo, Maria / 5 days.
Unify when cutting the payoff artboards.

---

## Recommended execution order

1. **Tier 0 (hours):** fix the Android intent-filter host; deploy the
   `INVITE_*` env set (store ID, team ID); re-verify AASA + store buttons on
   a real device.
2. **Tier 1 (days):** D2b store-detour recovery + TTL; D3 401-flash
   suppression on the invite route; D4 sign-up-first routing for
   `mode:'invite'`; D5 deferred safety hook; D6 lifecycle gate on redeem;
   D7 server-side bounds on expiry/max_uses.
3. **Tier 2 (one design day + build):** cut the missing artboard set — "the
   first sixty seconds inside the trip as an invitee": chip acknowledgment
   visible on landing ("Making room for slow mornings and fado"), the open-day
   hook's follow-through, and the group-share variant. Then implement; decide
   D10 (attribute at accept vs post-join chips for group links) as part of it.
4. **Tier 3 (half a day + ongoing):** journal a trip_event for share-sheet
   mints so S3 counts (D12); add the conversation-accept event (D13); fix the
   Maestro flow so it can fail + add one real two-device signed-out E2E per
   the dogfood pre-flight walk (D14); rate-limit the public intake endpoint
   (D15); render the fetched facts on the web landing (D16).

The two-device pre-flight walk in `dogfood-loop-validation-2026-07-04.md`
remains the final gate — it is currently the *only* check that would catch
most of Tier 0–1, which is exactly why automation (Tier 3) must be made
trustworthy before the cohort.

## Open product decisions

- **Chip privacy semantics** (design left it open): today the answer is
  private-to-Vesper, organizer sees only "answered privately." Confirm and
  then let the design copy promise exactly that — no more, no less.
- **Group-share signal policy** (D10): attribute at accept time vs move chips
  post-join. Attribution at accept is warmer (answer travels with them);
  post-join chips are simpler and avoid anonymous-submission plumbing.
- **Joining a live trip**: no designed or gated state exists. Decide whether
  mid-trip joins are welcome (probably yes — "join us, we're here") and what
  they land on (today's plan, not Trip Shape).

## Relationship to other documents

- `docs/journeys/02-concrete-trip-creation-and-invite.md` — organizer-side
  contract; unchanged.
- `docs/journeys/18-signed-out-join-by-invite.md` — plumbing contract; this
  audit is the felt-experience layer above it. The former J18 persona-cert skip
  closed on 2026-07-19; D14 still tracks broader real-auth/device coverage.
- `docs/working/dogfood-loop-validation-2026-07-04.md` — the funnel this
  audit's Tier 3 items make trustworthy; the pre-flight walk is the final
  gate.
- `docs/working/phone-auth-plan-2026-07-11.md` — D4's sign-up-first routing
  should ride the same auth surface.
- Design bundle: `~/Downloads/vesper 166` (vesper 166 handoff; Auth & Invite
  = canon). The Tier 2 artboard set extends this canon; keep new sections
  namespaced per the folio-integration lesson.

## Evidence provenance

Three parallel traces (design bundle extraction; travel-agent backend trace;
travel-app frontend trace), 2026-07-13, synthesized same day. All file:line
references verified at trace time against the working trees on `main`
(travel-agent, travel-app) and the vesper 166 bundle.
