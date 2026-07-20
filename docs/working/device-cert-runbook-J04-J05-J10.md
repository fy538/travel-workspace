# Device-Cert Runbook — J04, J05, J10 (two-physical-device walk)

> Status: executable runbook
> Owner: founder / engineering
> Last updated: 2026-07-19
> Scope: the three journeys that require a live, two-account, on-device pass —
> J04 (private → group-safe), J05 (proposal → plan mutation), J10 (booking /
> stay / expense trust loop).
> Companion (higher-level ladder + Maestro automation): `journey-live-full-cert-04-05-10.md`.

This document is written to be run **top-to-bottom by a human with no prior
context**. Two real devices (or two device-tier simulators — see the profile
note in Preflight), one signed in as the **organizer**, one as a **member**.
Every step names the seeded state it lands on, the exact taps, the expected
on-screen result, and a PASS/FAIL assertion. Steps that depend on an owner-set
secret or flag are marked **[OWNER-GATED]** — if that precondition is not met,
that step (and only that step) will fail; the assertion tells you how to tell a
real failure from a missing precondition.

---

## 0. Preflight — accounts, secrets, personas

### 0.1 Device / persona assignment

You need **two accounts on two devices**. J04/J05/J10 all run on the
**`mara-lisbon`** group trip (Mara is the organizer; Dao and Reza are members).

| Device | Role | Persona | Email | Notes |
|--------|------|---------|-------|-------|
| **Device A** | Organizer | **Mara** | `mara@dogfood.local` | Owns `mara-lisbon`. Mints invites, drives group-chat plan changes, transacts booking, opts costs in. |
| **Device B** | Member | **Dao** | `dao@dogfood.local` | Member of `mara-lisbon`. Sends the private constraint (J04), casts the deciding vote (J05), verifies member-safe booking/cost visibility (J10). |

> The seeded proposal already has **Dao + Reza approving** (see J05 seed). Dao on
> Device B is the deciding third voter. If you prefer Reza as the second device,
> the private-phrase and vote steps still work; the tally screenshots below name
> Dao.

### 0.2 Build

- EAS profile: **`dogfood`** or **`preview`** (`simulator: false`, real Clerk key,
  `EXPO_PUBLIC_SKIP_AUTH=false`, `USE_MOCK=false`). The `development` profile
  **cannot** reach this tier even with `guide://dev/screenshot-mode?realApi=1` —
  `SKIP_AUTH` is baked in at build time and never presents real Clerk sign-in
  (`app/_layout.tsx`: `if (USE_MOCK || SKIP_AUTH) { /* skip Clerk */ }`).
- API base: `https://vesper-backend.fly.dev` (Fly dogfood).

### 0.3 Owner preconditions — SET THESE BEFORE THE WALK

Confirm each with the owner. A missing one silently breaks a specific step, not
the whole walk; the affected steps are cross-referenced.

| Precondition | What it gates | Symptom if missing |
|---|---|---|
| **`mara@dogfood.local` Clerk device account linked** | All of Device A sign-in | Device A cannot sign in as organizer → whole walk blocked. **Hard blocker.** |
| **`AI_MODE` live OR a replay cassette loaded** | Vesper streaming turns (J05 step A3 plan-change turn; J04 optional Vesper reply) | Vesper turn stalls / never streams a proposal. J05 Track-A creation step hangs. |
| **`EXPO_PUSH_ENABLED` + Expo push secret set** | Push *delivery* to the devices (used by J09; here only the optional J05/J10 push-preview spot-check) | No push banner arrives. In-app notification feed still updates — do not fail the core walk on this; see §J05 step 9 and the note in §4. **[OWNER-GATED]** |
| **`POSTHOG_API_KEY` set** | Activation-funnel instrumentation | Funnel events go dark. Does not change on-screen behavior — do **not** fail any UI step on this; it only affects backstage analytics. |
| **Fly `dogfood-media` mount** | Hero imagery for elif Tokyo/Brooklyn (J11/J12) | Not on the J04/J05/J10 path — hero images here are stay/venue thumbnails, not the returned-hero. Note only. |

> `expo` MCP requires OAuth and is **not** authorizable from an automated
> session. If you are using the Expo MCP for push, authorize it in an
> interactive session first; otherwise verify push delivery from the Expo
> dashboard / device directly.

### 0.4 Seeded states this walk depends on (must be present on the target build)

| Journey | Seeded object | Where it surfaces |
|---|---|---|
| J04 | `mara-lisbon` `privacy_events` incl. **Dao `private_constraint_used`** | Atlas → **Data receipt** renders "Private constraint used" row (the trust payoff). |
| J05 | `mara-lisbon` **"First dinner decision"** group thread with a `vote_widget` resolved to the **OPEN** proposal `first-dinner-venue-swap`; **Dao + Reza already approve** | Group chat shows a `VoteWidgetCard` with tally chips; Device B casts the deciding vote. |
| J10 | `mara-lisbon` `booking_session` **`mara-first-dinner-booking`** (Casa do Alentejo offer ~**114 EUR** + cart) | `/booking/[sessionId]` reachable; offer + cart render. |
| J10 | `mara-lisbon` `booking_hold` **`mara-casa-alentejo-hold`** (6h window) | Home **DeckCall(held)** fires + hold-settle reachable via `/booking/[sessionId]`. |

If any seeded object is absent, the tester lands on an empty screen — re-seed
before continuing rather than improvising. The seeds are the whole point: they
put the tester on a **populated** screen.

### 0.5 Pre-walk sanity (once, from a laptop)

```bash
make dogfood-fly-smoke                 # Fly substrate + personas reachable
make dogfood-journey-live-api          # local TestClient — expect 16/16 green
```

If either fails, stop — the device walk cannot pass what the API tier already fails.

---

## 1. J04 — Private constraint → group-safe plan (I4 is the trust event)

**Promise under test:** a member can tell Vesper a private truth; the group plan
can benefit **without** the group thread ever naming the member or the raw
phrase. (Journey doc: `docs/journeys/04-private-constraint-to-group-safe-plan.md`.)

**Primary routes:** `/(tabs)/concierge/chat` (private), `/(tabs)/trips/[tripId]/chat`
(group), `/(tabs)/trips/[tripId]/plan`, `/atlas/data-receipt`.

**The specific private phrase to grep for on screen:**
> **"I need quiet mornings before long days"**

### Script

| # | Device | Tap / action | Seeded state relied on | Expected on-screen result | PASS / FAIL assertion |
|---|--------|--------------|------------------------|---------------------------|------------------------|
| 1 | **B (Dao)** | Bottom tab **Concierge** → open the **private** Vesper chat (the 1:1 concierge thread, **not** the `mara-lisbon` group thread). | Private concierge chat exists for Dao. | Private chat composer, no other members present. | PASS: this is a 1:1 thread (no roster chips). FAIL: you're in the group thread. |
| 2 | **B (Dao)** | Type exactly **"I need quiet mornings before long days"** and send. **[OWNER-GATED: AI_MODE/cassette]** for Vesper's reply. | — | Message posts; Vesper acknowledges candidly in private. | PASS: message sends; if AI is live/cassette, Vesper replies candidly. FAIL: send errors. If Vesper never replies, check `AI_MODE`/cassette before failing. |
| 3 | **A (Mara)** | Open `mara-lisbon` → **Chat** (group thread). Ask Vesper (in group): **"can you adjust our plan so mornings are a bit gentler?"** **[OWNER-GATED: AI_MODE/cassette]** | Group chat writable for organizer. | Vesper composes a **public-safe** group message / plan nudge. | PASS: reply is public-safe. FAIL if AI stalls → check cassette, don't fail redaction. |
| 4 | **A (Mara)** | Read the full group thread top-to-bottom. | — | No occurrence of the raw phrase; Dao is **not** named as the source. | **PASS: the string "quiet mornings before long days" does NOT appear, and Dao is not named as the reason.** FAIL: raw phrase or "Dao said…" appears → **trust regression, hard fail.** |
| 5 | **B (Dao)** | Open the same group thread on Device B and re-read. | — | Same public-safe copy; Dao does not see themselves named. | PASS: identical public-safe copy on both devices. FAIL: member device leaks the phrase. |
| 6 | **A (Mara)** | Open **Plan** (`/(tabs)/trips/[tripId]/plan`). If a proposal/adjustment landed, read its row + rationale. | — | Any accommodation copy uses public-safe language (e.g. "gentler mornings"), never a named constraint. | PASS: plan/proposal copy is public-safe. FAIL: financial/accessibility/dietary detail or member name in plan copy. |
| 7 | **B (Dao)** | Go to **Atlas** tab → **Data receipt** (`/atlas/data-receipt`, `testID="atlas-data-receipt-screen"`). | **Seeded `privacy_events`: Dao `private_constraint_used`.** | Receipt lists a **"Private constraint used"** row (mapped from `private_constraint_used`) under TODAY/YESTERDAY. | **PASS: a "Private constraint used" row renders** — this is the trust payoff (audited use, no leaked phrase). FAIL: no receipt row → re-check the seed before failing. |
| 8 | **B (Dao)** | Tap the receipt row; read the detail. | — | Detail explains *that* a private constraint was used, **without** reprinting the phrase verbatim. | PASS: audited-but-not-leaked. FAIL: detail reprints "quiet mornings before long days". |

**J04 verdict:** PASS only if steps 4, 5, 6 show **zero** leak of the phrase or
the member's name across group chat + plan, AND step 7 shows the audited
"Private constraint used" receipt. Record J04 **Live → ready** in
`docs/journeys/STATUS.md` when this passes.

---

## 2. J05 — Proposal → plan mutation (two-account vote loop)

**Promise under test:** the group can decide, the decision becomes an exact
itinerary operation, and the outcome is visible + recoverable, with Chat / Plan /
Changes / Map all agreeing. (Journey doc:
`docs/journeys/05-group-planning-to-proposal-to-plan-mutation.md`.)

**Primary routes:** `/(tabs)/trips/[tripId]/chat`, `/(tabs)/trips/[tripId]/plan`,
`/(tabs)/trips/[tripId]/changes`, `/(tabs)/trips/[tripId]/map`.
**Key component:** `components/chat/VoteWidgetCard.tsx` (tally line `"N for · M against"`,
`CardChipRow` option chips, `resolutionRuleLabel`). Vote hook: `data/proposals.ts`
→ `useVoteOnProposal`.

### Script

| # | Device | Tap / action | Seeded state relied on | Expected on-screen result | PASS / FAIL assertion |
|---|--------|--------------|------------------------|---------------------------|------------------------|
| 1 | **A (Mara)** | Open `mara-lisbon` → **Chat** → open the **"First dinner decision"** thread. | **Seeded "First dinner decision" thread + `vote_widget` → OPEN proposal `first-dinner-venue-swap`.** | A `VoteWidgetCard` renders inline with option chips and a tally line. | PASS: vote card visible with chips. FAIL: no vote card → re-check seed. |
| 2 | **A (Mara)** | Read the tally + resolution rule on the card. | **Seeded: Dao + Reza already approve.** | Tally shows the existing approvals (e.g. `"2 for · 0 against"`); rule line reads e.g. "Needs a majority vote — the organizer may resolve it sooner". | PASS: tally reflects 2 seeded approvals. FAIL: tally shows 0/0 → seed's votes didn't attach. |
| 3 | **B (Dao)** | Open the **same** "First dinner decision" thread on Device B. Confirm the vote card shows and you have not yet cast **on this device session** (seed pre-approves Dao server-side; if the chip already reads as your recorded vote, use **Reza** on Device B for a clean deciding tap, or change/confirm the vote). | Same seeded proposal, cross-device. | Same vote card, same tally, live. | PASS: card + tally identical across devices. FAIL: devices disagree on tally (read-model drift). |
| 4 | **B (Device B voter)** | Tap the **approve** option chip to cast the **deciding** vote. | Open proposal `first-dinner-venue-swap`. | Optimistic chip selects; tally increments; on server-confirm the proposal moves toward resolved. `useVoteOnProposal` rolls the chip back on a server reject. | PASS: tally increments and sticks after refetch; no duplicate on double-tap (idempotent). FAIL: chip reverts silently, or double-tap creates two votes. |
| 5 | **A (Mara)** | Watch the same card on Device A (or pull to refresh). | — | Tally updates to include Device B's vote; when threshold met, card flips to a **read-only resolved/outcome** state (no more phantom vote chips). | PASS: Device A sees the new tally, then resolved state. FAIL: Device A stuck on stale tally. |
| 6 | **A (Mara)** | If the proposal reached consensus, open **Plan**. | — | Itinerary reflects the accepted first-dinner venue swap (the operation applied). | PASS: plan row shows the swapped venue. FAIL: proposal resolved but plan unchanged (silent-no-op / apply drift). |
| 7 | **A (Mara)** | Open **Changes** (`/(tabs)/trips/[tripId]/changes`). | — | A durable **receipt** for the applied proposal (I5): what changed, when, by the group. | PASS: receipt present and legible. FAIL: accepted proposal mutated plan with **no** visible receipt. |
| 8 | **B (Dao)** | Open **Changes** on Device B. | — | Same receipt visible to the member. | PASS: member sees identical receipt. FAIL: member device missing the receipt. |
| 9 | **A (Mara)** | Coherence sweep (I9): compare titles/state across **Home → Plan → Changes → Map** for this trip. **[OWNER-GATED: EXPO_PUSH_ENABLED]** optional: check for a push/notification preview routing back to the proposal. | — | All four surfaces name the same current first-dinner truth; notification (if delivered) deep-links to the proposal/chat. | PASS: Plan/Home/Changes/Map agree. FAIL: any surface shows the pre-swap venue. Missing push ≠ fail — verify the **in-app** notification feed instead. |
| 10 | **A (Mara)** | **Revert (I6):** if the Changes/proposal UI offers a revert control, revert the change. *(Note: the companion doc records no stable revert-control testID — this is a manual visual step; if no revert affordance is present, mark I6 "not-exercised", do not fabricate.)* | — | Plan + Home return to the pre-swap venue; Changes logs the revert. | PASS: revert reflected everywhere (no "success but Map still changed"). FAIL: revert claims success but Plan/Map still show swapped state. |

**J05 verdict:** PASS if the deciding vote (step 4) is idempotent and moves the
proposal to resolved, the plan mutates **with** a receipt (steps 6–8), and all
surfaces agree (step 9). I6 revert is best-effort/manual. Record J05
**Live → ready** when the vote→apply→receipt loop passes on device.

---

## 3. J10 — Booking / stay / expense trust loop (two-account)

**Promise under test:** one person transacts; the group sees the right public
state; private financial detail stays private until opt-in; a hold is settled
only with explicit terms + human approval and never claims "booked" before the
provider confirms. (Journey doc:
`docs/journeys/10-booking-stay-expense-trust-loop.md`.)

**Primary routes:** `/trip-accommodations?tripId=`, `/accommodation/[accommodationId]`,
`/booking/[sessionId]`, `/trip-expenses?tripId=`, `/trip-expenses/balance`,
`/(tabs)/trips/[tripId]/chat`.
**Hold-settle contract:** `hooks/useBookingDecision.ts` → `api.settleBookingHold`
sends `{ terms_accepted: true, final_human_approval: true }` (matches OpenAPI
`SettleHoldRequest`); a 200 with `status` `expired`/`unavailable` must surface
actionable copy, not a "booked" state.

### Script

| # | Device | Tap / action | Seeded state relied on | Expected on-screen result | PASS / FAIL assertion |
|---|--------|--------------|------------------------|---------------------------|------------------------|
| 1 | **A (Mara)** | Open `mara-lisbon` → Trip details → **Stay** (`/trip-accommodations?tripId=…`). | Trip has accommodations list. | Accommodations list renders (group base + any personal slots). | PASS: list renders. FAIL: empty → re-check trip. |
| 2 | **A (Mara)** | Open the seeded stay's detail (`/accommodation/[accommodationId]`). | Casa do Alentejo / group stay seeded. | Stay detail with dates/location; organizer sees full controls. | PASS: detail loads. FAIL: 404 / blank. |
| 3 | **B (Dao)** | On Device B, open the **same** trip → **Stay** → same accommodation. | Shared stay is group-visible; private slots are whole-row excluded. | Dao sees the **group** stay's public projection; sees **no** organizer-only payment fields, and **not** any private per-person slot that isn't Dao's. | **PASS: member sees group label + public status, NOT payment method / confirmation secret.** FAIL: member sees card numbers, provider confirmation, or Mara's private slot. |
| 4 | **A (Mara)** | Open the seeded **booking session** from chat, or navigate to `/booking/[sessionId]` for **`mara-first-dinner-booking`**. | **Seeded `booking_session mara-first-dinner-booking` — Casa do Alentejo offer ~114 EUR + cart.** | Offers grouped by category; the ~**114 EUR** Casa do Alentejo offer + a cart render. | PASS: offer shows **~114 EUR** and cart is present. FAIL: empty session → re-check seed. |
| 5 | **A (Mara)** | Inspect the confirm affordance. Do **not** push a real money-moving checkout. | — | Confirm requires explicit consent (`checkout_consent`); UI shows terms + human-approval before any "confirmed" state. | PASS: no "Booked" appears before provider state; consent gate present. FAIL: UI claims booked pre-provider. |
| 6 | **A (Mara)** | Go **Home**. Look for the **DeckCall (held)** card. | **Seeded `booking_hold mara-casa-alentejo-hold`, 6h window.** | A home Deck card announces a **held** booking with the remaining hold window. | PASS: DeckCall(held) card present with a countdown/window. FAIL: no held card → re-check hold seed / that the 6h window hasn't lapsed. |
| 7 | **A (Mara)** | Tap the held card → it routes to the hold-settle path (`/booking/[sessionId]`, settle affordance). | Same `mara-casa-alentejo-hold`. | Settle screen with explicit **terms + final human approval** before settling. | PASS: settle requires terms + approval (`terms_accepted` + `final_human_approval`). FAIL: settle fires with no consent. |
| 8 | **A (Mara)** | *(UI-only — do not move real money.)* Verify the settle button's request semantics. If settling in a safe/dark provider mode: observe the response. | Hold within 6h. | On confirm → success receipt ("Booking confirmed"); on `expired`/`unavailable` → **actionable** copy ("Hold has expired" / "Booking wasn't available"), not a generic toast, and never "Booked". | PASS: outcome copy matches provider status honestly. FAIL: a non-confirmed status renders as booked, or a 410/expired shows a generic toast. |
| 9 | **A (Mara)** | Close the booking flow. | — | Returns to the **exact** prior Itinerary/booking object context (opaque return token). | PASS: lands back on the originating stop/context. FAIL: stranded on a dead-end / wrong screen. |
| 10 | **A (Mara)** | For a **provider-confirmed** offer only: choose **Share in Costs** → review the provider-price prefill, payer, split → submit. | Confirmed offer + `mara-lisbon` members. | Exactly **one** expense created, stamped `booking_opt_in`, deduped by offer; retry is idempotent. | PASS: one expense, idempotent on retry. FAIL: duplicate expense, or a *selected/session-only* (unconfirmed) offer was allowed into Costs. |
| 11 | **B (Dao)** | Open **Costs** (`/trip-expenses?tripId=…`) → **balance** (`/trip-expenses/balance`, `testID="balance-drillin-screen"`). | Expense from step 10 (or seeded split). | Dao sees the **split** and what they owe; does **not** see card numbers or provider confirmation secret. | **PASS: member sees split amount, not payment method / confirmation number.** FAIL: member sees organizer-only payment detail. |
| 12 | **B (Dao)** | Read the expense's source. | — | Ledger entry shows a **booking source** label (from the opted-in offer). | PASS: expense names its booking source. FAIL: no provenance. |

**J10 verdict:** PASS if member visibility (steps 3, 11) is public-safe with zero
payment-detail leakage, the hold settles only with explicit terms + approval and
never overclaims "booked" (steps 5–8), and cost opt-in is organizer-only /
idempotent (step 10). Record J10 **Live → ready** when organizer/member
visibility and hold semantics match. **Do not** block on Duffel live checkout —
verify hold/confirm **UI** only; provider stays dark unless explicitly enabled.

---

## 4. Owner-gated step index (fast reference)

| Step | Gate | If gate is unmet |
|---|---|---|
| J04 §1 step 2, 3 (Vesper turns) | `AI_MODE` live **or** replay cassette | Vesper won't stream a reply/proposal. Confirm the gate before failing the redaction assertions — a stalled turn is a config gap, not a leak. |
| J05 §2 step 9 (push preview) | `EXPO_PUSH_ENABLED` + Expo secret | No push banner. **Do not fail** — verify the in-app notification feed instead. Expo MCP needs interactive OAuth; verify via device/Expo dashboard. |
| All (Device A sign-in) | `mara@dogfood.local` Clerk device account linked | **Hard blocker** — the organizer cannot sign in; the whole walk is blocked. |
| Backstage only | `POSTHOG_API_KEY` | Activation funnel goes dark. **No UI step fails on this.** |
| J11/J12 (not in this walk) | Fly `dogfood-media` mount | Not on the J04/J05/J10 path; noted for completeness. |

There is **no** bypassable Clerk test OTP for `@dogfood.local` accounts — each
real sign-in needs a human to read a real inbox and key the code once (reusable
fragment: `travel-app/.maestro/_signin-dogfood-account.yaml`).

## 5. After all three pass

Update `docs/journeys/STATUS.md`:

- J04, J05, J10 **Live** column → `ready`
- **Certified** column → `full` for those rows
- Bump the **Journey full-certified** count accordingly.

```bash
make certify-live   # preflight + prints this checklist
```

**Not blocking this cert:** Duffel live money-movement (UI-only here), external
push delivery (in-app feed is sufficient), a third external TestFlight user
(optional after the founder two-device pass).
