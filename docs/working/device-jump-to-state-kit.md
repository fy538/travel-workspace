# Device Jump-to-State Deep-Link Kit

Teleport a tester straight to each key device-walk state instead of hand-reconstructing it on the phone.

**Scope:** the pre-device walk (J04–J12) against the seeded dogfood substrate.
**Source of truth read for this kit:** `travel-app` linking config (`app.json` `scheme: "guide"`, default Expo Router — no custom `Linking` prefix), the three dev deep-link routes (`app/dev/screenshot-mode.tsx`, `app/dev/force-state.tsx`, `app/dev/persona-switcher.tsx`), `utils/routes.ts` (the typed route map), the mock persona bundles (`constants/personas/*`), and the backend seed id formula (`travel-agent/tools/dogfood/content/schemas.py` + `seed.py`).

---

## 0. TL;DR — the one primitive you need

There is exactly **one** dev deep link that both **switches the mock persona** and **lands on a target route in one shot**, with no JS reload:

```
guide://dev/screenshot-mode?persona=<id>&on=0&to=<route>
```

- `persona=<id>` — sets the active mock persona in-memory (mock builds only).
- `on=0` — leaves screenshot-mode OFF so the floating **MOCK/DEV** button (DevFab) and normal chrome stay visible for an interactive walk. (Drop `on=0`, or use `hideNav=1`, only when you want clean screenshots.)
- `to=<route>` — the Expo Router path to land on. **Nested query params inside `to` must be percent-encoded** (`?` → `%3F`, `=` → `%3D`, `&` → `%26`).

This route is registered only behind `__DEV__ || IS_INTERNAL_BUILD`, so it never exists in external builds.

> **Critical mode caveat.** Everything that reads `persona=` / mock ids / the mock clock inside `screenshot-mode.tsx` is wrapped in `if (USE_MOCK)`. So:
> - **Mock / development build** → `persona=` works, and the mock ids in §2 land exactly.
> - **Live dogfood build** (real Clerk, real backend — the build the owner-precondition walk targets) → `persona=` is **ignored** (you are whoever you Clerk-signed-in as); only `to=<route>` routing happens, and the ids must be **real backend UUIDs** (§3).

**How to fire a deep link on device:**
- iOS Simulator: `xcrun simctl openurl booted "guide://…"`
- Android emulator: `adb shell am start -a android.intent.action.VIEW -d "guide://…"`
- Physical device: paste the `guide://…` link into Notes/Messages and tap it, or use a QR code. Maestro flows use `- openLink: guide://…` (see `.maestro/25-journey-05-*`, `.maestro/28-journey-10-*` for live examples).

---

## 1. The two ways to run the walk

| | **Mock build** (dev/simulator, `USE_MOCK=true`) | **Live dogfood build** (Clerk + real backend) |
|---|---|---|
| Identity | `persona=` param, no login | Clerk sign-in as `<persona>@dogfood.local` |
| Persona switch mid-session | `guide://dev/screenshot-mode?persona=…` (instant) or `guide://dev/persona-switcher` (tap a row, reloads) | **Not possible** — one identity per session; sign out to change |
| IDs | mock fixture ids (§2, known + verified) | deterministic backend UUIDs (§3, computed + validated) |
| Reproduces | the *shape* of each state (may differ in city/details) | the actual seeded rows described in the walk brief |

The mock personas are **independently authored** and do **not** perfectly mirror the live seed (e.g. the mock `elif` has no Brooklyn trip; the mock pending Atlas candidate is Istanbul, not Tokyo). Use §2 to rehearse the interaction on a simulator; use §3 for the real device walk.

---

## 2. MOCK-BUILD teleport table (self-contained, verified ids)

Every link below was verified against the current fixtures. Prefix each with `guide://dev/screenshot-mode?` and fire it as in §0. All are ready to copy-paste; the `to=` values are shown **decoded** for readability with the **encoded** form beneath where nesting matters.

Shared mock ids used below:
- mara Lisbon trip = `trip-lisbon-26`
- open first-dinner proposal = `aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa` (`MOCK_PROPOSAL_A`, status `open`, missing voter = Mara)
- reza in-progress Rome trip = `02fb9de5-36ec-5582-885e-bf9f7c59dcd8`
- elif Istanbul pending Atlas candidate = `cand-elif-istanbul`
- sarah Rome-return trip (has expense splits) = `7220dcad-7ee1-57bb-bd24-47883a09aa3d`

| # | Walk state | Persona | Copy-paste link | Lands on |
|---|---|---|---|---|
| J05 | **Proposal open for vote** (cast deciding vote) | `mara` | `guide://dev/screenshot-mode?persona=mara&on=0&to=/trip-proposal/aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa%3FtripId%3Dtrip-lisbon-26` | ProposalDetailScreen — vote chips + tally, Approve/Decline live |
| J05 | **Group chat with vote widget** | `mara` | `guide://dev/screenshot-mode?persona=mara&on=0&to=/(tabs)/trips/trip-lisbon-26/chat` | First-dinner group thread; inline vote widget resolves to the open proposal |
| J06/J10 | **Booking session** (offer + cart) | `mara` | `guide://dev/screenshot-mode?persona=mara&on=0&to=/booking/qa-offer-compare%3FtripId%3Dtrip-lisbon-26` | `/booking/[sessionId]` with compare offers + cart (also try `qa-provider-table`) |
| J06/J10 | **Held booking** (hold window, needs payment) | `mara` | `guide://dev/screenshot-mode?persona=mara&on=0&to=/booking/qa-held-stay%3FtripId%3Dtrip-lisbon-26` | Booking session in `held_for_payment` — the DeckCall(held) payoff surface |
| J08 | **Now Mode — live trip** (in-progress + next stop) | `reza` | `guide://dev/screenshot-mode?persona=reza&on=0&to=/(tabs)/trips/02fb9de5-36ec-5582-885e-bf9f7c59dcd8/plan` | Rome plan; `NowModeStrip` shows the in-progress block + next stop (persona clock is pinned to `2026-07-09`, trip runs `07-06`→`07-11`) |
| J11 | **Atlas inbox candidate** (Keep/approve) | `elif` | `guide://dev/screenshot-mode?persona=elif&on=0&to=/atlas/inbox` | Atlas Inbox; the pending Istanbul candidate awaits Keep |
| J11 | **Atlas candidate detail** | `elif` | `guide://dev/screenshot-mode?persona=elif&on=0&to=/atlas/candidate/cand-elif-istanbul` | Candidate review screen (approve → artifact) |
| J12 | **Settle-up / balance** | `sarah` | `guide://dev/screenshot-mode?persona=sarah&on=0&to=/trip-expenses/balance%3FtripId%3D7220dcad-7ee1-57bb-bd24-47883a09aa3d` | Balance drill-in with unsettled splits + settle affordance |
| J04 | **Atlas Data Receipt** (privacy trust payoff) | `mara` | `guide://dev/screenshot-mode?persona=mara&on=0&to=/atlas/data-receipt` | Audit log of personal-data uses (location/voice/redactions) |
| J09 | **Personal inbox / pending invite + badge** | `elif` | `guide://dev/screenshot-mode?persona=elif&on=0&to=/notifications%3Fmode%3Dpersonal` | Personal notifications tab (social + invites); walk badge-decrement here |

> **Why `mara` for J12 in mock:** the mock `mara` bundle ships `expenses: []`, so its balance sheet is empty. `sarah` (and `mike`) carry real mock splits, so they demonstrate settle-up. On the **live** build, J12 is elif's Brooklyn trip (§3) as the brief specifies.

**Alternate persona-switch shortcut (screen, not param):** `guide://dev/persona-switcher` opens the switcher list — tap a row to switch (this **reloads** the JS bundle and re-seeds, then you deep-link to the target). Slower than the `persona=` param; use it only if you also want the time-travel controls on that screen.

---

## 3. LIVE dogfood-build teleport (real backend UUIDs)

On the live build you **sign in through Clerk** as the persona that owns the state, then fire `guide://<route>` deep links. `persona=` is inert here, so you can use either the bare scheme form (`guide://trips/<uuid>/plan`) or the `screenshot-mode` wrapper purely for its `to=` routing.

### 3a. Which account owns each state

| Walk states | Sign in as | Trip |
|---|---|---|
| J04, J05, J06, J10 | `mara@dogfood.local` | mara-lisbon |
| J08 | `reza@dogfood.local` | reza-rome-live-2026 |
| J09, J11, J12 | `elif@dogfood.local` | elif-rome-return-2026 / elif-tokyo-2025 / elif-brooklyn-local-week |

(`mara`'s Clerk device account must be linked to `mara@dogfood.local` — an owner precondition; without it the mara walk can't sign in.)

### 3b. Verified live trip UUIDs

These are **deterministic** (`uuid5(DOGFOOD_NAMESPACE, "{manifest_id}:trip:{trip_key}:trip")`, namespace `85f5317d-6f19-4da2-9f54-5bdfd7ce7f3d`). Computed with the repo's own formula and **cross-validated** against the fixtures that already hardcode them (`personas/sarah.ts`, `personas/mike.ts`, `personas/reza.ts`):

| Trip (manifest) | Live trip UUID |
|---|---|
| mara-lisbon (`lisbon-phase1`) | `be3e2072-ff16-5a46-a529-12ed6d31ed31` |
| reza-rome-live-2026 (`cascade-phase-fixtures`) | `02fb9de5-36ec-5582-885e-bf9f7c59dcd8` |
| elif-rome-return-2026 (`elif-rome`) | `7220dcad-7ee1-57bb-bd24-47883a09aa3d` |
| elif-tokyo-2025 (`tokyo-phase1`) | `16e7cf14-48f3-57ca-b6fc-ef253694d37c` |
| elif-brooklyn-local-week (`brooklyn-phase1`) | `af736e5e-ae23-5d40-8eca-69327b377572` |

### 3c. Live trip-level deep links (fire after Clerk sign-in)

| Walk state | Link |
|---|---|
| J08 Now Mode (reza) | `guide://trips/02fb9de5-36ec-5582-885e-bf9f7c59dcd8/plan` |
| J12 settle-up (elif Brooklyn) | `guide://trip-expenses/balance?tripId=af736e5e-ae23-5d40-8eca-69327b377572` |
| J04 data receipt (mara) | `guide://atlas/data-receipt` |
| J09 personal inbox (elif) | `guide://notifications?mode=personal` |
| J11 Atlas inbox (elif) | `guide://atlas/inbox` |
| J05 group chat (mara) | `guide://trips/be3e2072-ff16-5a46-a529-12ed6d31ed31/chat` |

### 3d. Sub-object ids (proposal / candidate / booking session / hold)

The walk brief names these by shorthand (`first-dinner-venue-swap`, `mara-first-dinner-booking`, `mara-casa-alentejo-hold`, `elif-tokyo-transit-candidate`). Their **exact seed keys were not committed in the manifests I read** (they were created in the pre-device readiness pass), so I will **not** publish guessed UUIDs for them — a wrong id lands on an error screen and wastes the walk.

Two reliable options:

1. **Resolve them from the real seed** — the ids are deterministic. Run this against `travel-agent` with the exact seed key strings the readiness pass used:

   ```python
   # travel-agent $ python3
   import uuid
   NS = uuid.UUID("85f5317d-6f19-4da2-9f54-5bdfd7ce7f3d")
   su = lambda *p: uuid.uuid5(NS, ":".join(p))
   trip      = lambda m,k: su(f"{m}:trip:{k}", "trip")
   proposal  = lambda m,k: su(f"{m}:proposal:{k}", "proposal")     # schemas.proposal_seed_id
   # e.g. proposal("lisbon-phase1", "mara-group-dinner-vote")
   ```
   For booking sessions / holds / atlas candidates, confirm the seed helper and key in `travel-agent/tools/dogfood/content/*_seed.py` before computing — each entity has its own `stable_uuid(...)` suffix. Or just export the live ids directly: `scripts/dogfood_coherence_export.py`.

2. **Reach them by navigation** (id-free, always works on the live build):
   - **Proposal vote (J05):** open the mara-lisbon trip → group chat / Decisions → tap the open first-dinner proposal.
   - **Booking session (J06/J10):** mara-lisbon → Plan → the first-dinner block → the booking session it carries; the **held** booking also surfaces as a **DeckCall(held)** card on the home/focus surface.
   - **Atlas candidate (J11):** elif → `guide://atlas/inbox` → tap the pending Tokyo-transit candidate.

Route templates for when you *do* have the real ids:
- Proposal: `guide://trip-proposal/<proposalId>?tripId=<tripUuid>` (interactive vote surface; `app/trip-proposal/[proposalId].tsx`)
- Booking session: `guide://booking/<sessionId>?tripId=<tripUuid>` (`app/booking/[sessionId].tsx`)
- Atlas candidate: `guide://atlas/candidate/<candidateId>` (`app/atlas/candidate/[id].tsx`)

---

## 4. States with NO stable deep link (reach by navigation)

| State | Why no deep link | How to reach |
|---|---|---|
| **DeckCall(held) card on Home** (J06) | It's a home/focus-feed producer card, not a routable screen — it renders when a held booking exists for the signed-in user. | Land on the home/Trips surface with the held booking present; the Call face appears in the Deck/Rail (`components/focus-home/DeckCallFace.tsx`). Deep-link the booking session (§3d) to inspect the underlying state directly. |
| **In-progress "Now Mode" strip** (J08) | It's a conditional strip on the Plan screen, gated on the live clock intersecting a today-pinned block — not a route. | Deep-link to the reza Rome **plan** (§2/§3c); the strip renders only if a block is in-progress *now*. On mock, the pinned persona clock guarantees it; on live it depends on the real seeded today-pin. |
| **Badge decrement** (J09) | Side effect of viewing/acting on a notification, not a destination. | Deep-link to `notifications?mode=personal`, then act on the item; watch the tab badge decrement. |
| **StoryReadyEntry → story** (J12) | The entry card lives on the returned-trip home; the story itself is routable. | After settle-up, the returned-hero pin shows StoryReadyEntry; tap through, or jump straight to `guide://trips/<elif-brooklyn-uuid>/story`. |

---

## 5. Deep-link mechanics reference

- **Scheme:** `guide://` (`app.json` → `scheme`). No custom `Linking` prefixes; Expo Router maps URL paths to files in `app/`.
- **Route groups collapse:** `app/(tabs)/trips/[tripId]/plan.tsx` is reachable as `guide://trips/<id>/plan` (the `(tabs)` and `[tripId]` group/segment names don't appear in the URL). Both the bare form and the `to=/(tabs)/trips/<id>/plan` form work.
- **Encoding inside `to=`:** the outer link is parsed first, so a nested query string must be encoded — `?`→`%3F`, `=`→`%3D`, `&`→`%26`, `/`→`%2F` (encoding the leading slash is optional but safe). Example: `to=/booking/qa-held-stay%3FtripId%3Dtrip-lisbon-26`.
- **Other dev deep links** (complementary, not persona-aware):
  - `guide://dev/force-state?data=loading|error&offline=0|1&to=<route>` — force loading/error/offline states, then route. No `persona=`.
  - `guide://dev/screenshot-mode?...&hideNav=1&hideMockBanner=1` — clean-chrome capture variants (drop `on=0`).
  - `guide://dev/screenshot-mode?...&mockNowMs=<ms>` — override the mock clock (wins over the persona's pinned `now`).
  - `guide://dev/screenshot-mode?...&resetMock=0` — keep mock mutations you just made instead of re-seeding.
- **Full typed route map:** `travel-app/utils/routes.ts` — the `routes.*` helpers are the canonical list of every screen + its params.

## 6. Owner preconditions that gate these links (recap)

Deep links land, but the *content* still depends on the owner-set preconditions:
- `AI_MODE` live (or a replay cassette) — else J01 "Vesper shapes the idea" stalls even after teleporting into chat.
- `EXPO_PUSH_ENABLED` + Expo secret — else no push reaches the device; J09's push demo fails (the in-app inbox link still works).
- `POSTHOG_API_KEY` — else the activation funnel is dark (states still render).
- mara's Clerk device account linked to `mara@dogfood.local` — else the live mara walk can't sign in (§3a).
- Fly `dogfood-media` mount — else J11/J12 hero imagery is blank.
