# Frontend ↔ Design Canon Alignment Plan (canon = vesper 141)

**Status:** ready to execute · **Created:** 2026-07-11 · **Scope:** `travel-app` frontend only, Atlas excluded
**Source:** a fresh 8-domain design-vs-code audit (2026-07-11) + three design-canon adjudication/generative sessions that followed it (bundles vesper 138→141). This doc is the code-side work that remains after the design side was brought to a clean state.

> **Read this whole "Orientation" section before touching code.** A fresh agent has none of the audit reports or session history that produced this plan; everything you need is here or cited to a file you can open.

---

## 0. Orientation

### 0.1 What this project is
Vesper is a place-aware travel concierge (React Native / Expo app + Python backend). Two independent git repos live under `~/travel-workspace/`:
- `travel-app/` — the Expo client (this plan's target). Currently on branch `main`.
- `travel-agent/` — backend/AI. **Out of scope** except where an item is explicitly tagged `[BACKEND]`.

### 0.2 The design canon
The canon is an exported "handoff bundle" from Claude Design at **`~/Downloads/vesper 141/project/`** (a user-local path — if it's missing, ask the user for the latest `vesper NNN` bundle; always use the highest number).

**How to read it — important, it is not normal HTML:**
- Every top-level `Vesper *.html` file is **canvas-mode**: the visible page is empty; the real content is in the JSX file named in its `<script src="...jsx">` tag. Open the `.jsx`, not the `.html`. Example: `Vesper Costs.html` → `costs-system.jsx` (kit) + `costs-screens.jsx` (screens).
- **`Vesper Design Canon Index.html` → `...jsx`** is the map of which page owns which surface. Read it first.
- **`Vesper Canon Consolidation & Ownership.html` → `vesper-canon-consolidation-app.jsx`** is the governance object: register model, the 53-route→page mapping (§02b), ownership adjudications (§02d), the Kill-or-Draw list (§06b), and a dated changelog (§06d). When two design boards seem to disagree, this file's tables win.
- Do **not** implement from files in `archive/` or any file the consolidation marks ARCHIVE/DELETE. Do not grep raw JSX for "truth" — only boards imported by a top-level CANON/COMPANION page are in scope.
- The bundle is HTML/CSS/JS **prototypes**. Match the visual output; do not copy prototype structure. Recreate in RN idioms that fit the existing codebase.

### 0.3 The register model (governs all typography/material choices)
Two registers only, plus explicit hybrids — never invent a third:
- **EXPRESSIVE** — reading/memory/authored judgment/trip identity. EB Garamond titles + Vesper voice; warm paper/receipt material; short italic voice lines (never stacked, never every line).
- **PRODUCTIVE** — acting/booking/paying/configuring/searching/editing. DM Sans-led; EB Garamond at most **one** intentional voice moment; **italic never touches values, dates, or money**; the voice speaks as "I", never "Vesper will…".
- **HYBRID** — allowed but each region must read as clearly one or the other.
Three type families only: **EB Garamond** (serif), **DM Sans** (UI), **JetBrains Mono** (dates/times/codes/amounts). Inter/Georgia-as-primary = stale residue, replace on sight. Every price/total/rate renders through **mono**.

### 0.4 Token locations in code
- `travel-app/constants/colors.ts` — palettes (canonical ink/paper tokens live at ~lines 13–31; a legacy neutral palette at ~98–109 still powers core chrome — see Phase A).
- `travel-app/constants/typography.ts` — type roles. `travel-app/constants/fonts.ts` — families.
- `travel-app/constants/motion.ts` — durations/curves. `travel-app/constants/layout.ts` — radius/spacing.
- `travel-app/components/ui/*` — shared primitives (Button, BottomSheet, SheetHeader, state kit, rows, etc.).
- Design-side token source: `vesper-tokens.jsx` + `design-system.jsx` in the bundle.

### 0.5 Ground rules for execution
1. **Verify before editing.** Every `file:line` in this doc came from the 2026-07-11 audit, which read a snapshot of `main`. Code may have moved. Open the file, confirm the thing still exists as described, then change it. If reality contradicts this doc, trust the code and note the drift.
2. **Branch per phase.** Don't work on `main`. One branch per phase (e.g. `align/phase-a-tokens`). Keep phases landable independently.
3. **Atlas is out of scope.** `app/atlas/*`, `app/(tabs)/atlas/*`, `components/atlas/*` — do not touch. (Exception: two items explicitly redirect *into* Atlas Long View — that's a redirect, not an Atlas edit.)
4. **Verify each change end-to-end**, not just typecheck. Use the `/verify` skill (drives the affected flow) and `/run` to see it in the app. Run `make typecheck` / `make test-frontend` from `~/travel-workspace` before landing.
5. **Run `/code-review` after each phase lands** — AI-written UI duplicates and drifts; a reviewer pass catches it.
6. **`[BACKEND]`, `[LAUNCH-GATE]`, `[DECISION]` tags** mark items a frontend agent cannot finish alone — surface them, don't fake them.

### 0.6 What the design sessions already resolved (so you don't re-do it)
The audit (run against canon 137) flagged several things as "MISALIGNED" or "needs ruling." Canon 138→141 then ruled on them. Net effect on code:
- **Standalone accommodation chrome** → ruled *context-dependent*; code already does context-based rendering. **Already aligned — verify only.**
- **Discover pill-rail reduction** → the shipped scope-pill reduction was blessed as canonical. **Already aligned — no work.**
- **Conversation history IA** → Chat's Active/Standalone/Earlier grouping won; code already follows Chat. **Already aligned — verify only.**
- **Voice-in-thread** → grouped "Spoken turn" card ruled canonical for multi-turn sessions; code already groups. **Already aligned — verify only.**
- **Costs `DecisionSeal` settle ceremony** → blessed as a sanctioned one-trigger exception. **Already aligned — keep.**
- **`BRIEF_ANCHOR` (0.44) third composer pin** → kept and documented. **Already aligned — keep.**
- **DeckCall `reschedule` variant** ("the Catch") → canon drew it to match code. **Already aligned — verify.**
- **Trust & Controls / Saved living under `/atlas/*`** → claimed as a *named exception*; the URL prefix is an IA choice, not a design-owner signal. **Not a bug — no move needed.**
- **`session-recovery`, `trip-expenses/balance`** → now mapped in canon §02b. **Already aligned.**
- **Kill list** (ExplanationSheet, FeedbackSheet, SwapBlockSheet, TripDebriefSheet) → already removed from code. **Done.**

And these design rulings *created* new code work (folded into the phases below): Stay money→sans, Costs balance-sheet→sans, RevertConflictSheet sequencing→decide-before-revert, `your-map`→kill/redirect, `dna-card`→move out of `components/me/`, plus everything newly *drawn* (Voice & Narration page, Expense Detail, masked toggle, StoryReadyEntry, RecallBand states, mic permission).

---

## Phase A — Token & material foundations
*Systemic; highest polish-per-effort; unblocks visual correctness on every screen. Do this first — later phases build on correct tokens.*

**A1 · [P1] Retire the legacy espresso/white neutral palette.**
The single largest, everywhere-visible drift. `colors.ts` (~98–109, 182–194) carries a second neutral palette that predates the ink/paper token canon and still drives core chrome: `text.primary #2C2C28`, `action.primary #3D3630` (espresso), `background.primary #FFFFFF`, `screen.canvas #EDECE6`. These bake into `Button` primary fill, `FloatingTabBar` active/inactive, `BottomSheet` default background, and most typography roles.
- **How:** migrate these consumers onto the canonical `ink*`/`paper*` tokens (canon values at colors.ts ~13–31; canon token sheet = `vesper-tokens.jsx`). Do it token-by-token with a visual check after each — Button primary → ink; body text roles → ink rungs; sheet/canvas backgrounds → paper rungs.
- **Verify:** `/run` the app; spot-check Button, tab bar, a bottom sheet, and a text-heavy screen against the bundle's warm-paper look. No white sheets, no espresso buttons.

**A2 · [P1] Money renders in mono, not DM Sans.**
`typography.amount` (typography.ts:87) is DM Sans 22 and is used for money on the highest-stakes surfaces: `ExpenseDetail.tsx:502`, `BookingSessionSurfaces.tsx`, `BookingOfferRow.tsx`. Productive Type doctrine: every price/total/rate is JetBrains Mono.
- **How:** repoint `typography.amount` (and any money-specific role) to the mono family; verify booking checkout, offer rows, and expense amounts. (Costs ledger already uses mono — use it as the reference.)
- **Note:** ExpenseDetail is being rebuilt in Phase C; coordinate so you don't fix the amount twice.

**A3 · [P2] BottomSheet snapless default → r20 + paper.**
`BottomSheet.tsx` uses radius 20 + correct scrims *when a snap is passed*, but the snapless default falls back to r16 + `colors.white`. Canon sheet radius is 20 everywhere on paper surfaces. Make the default match the snap path.

**A4 · [P2] Toast: bottom dark pill, not top light banner.**
`context/ToastContext.tsx` renders a top banner on a light surface. Canon (`vesper-interaction-surfaces-app.jsx`) is a bottom floating dark pill, 52–64px, auto ~3.5s, **swipe-to-dismiss**, Undo family, replace-not-stack (replace/Undo already correct). Move it to the bottom, dark material, add swipe-dismiss.

**A5 · [P2] Sub-floor type sizes.** Canon floor is 9pt except mono stamps (8pt allowed). Offenders: `folioDiscoveryPill` mono 7pt, `folioDayMonth`/`folioDayChip` mono 7.5 (typography.ts:710–718), and `inviteDayStampLabel` **DM Sans 7pt** (typography.ts:292–296) — the last is an outright breach (7pt DM Sans). Bump to floor.

**A6 · [P2] Missing button variants + button drift.** `Button.tsx` lacks canon's **amber** and **sage** variants (only an olive-ish `success` approximates sage). Add them. Also: label sizes are +1px vs canon (md 15/sm 13 → 14/12); primary fill fixed by A1.

**A7 · [P2] Token self-consistency + retired-red residue.**
- `stateTokens.oxbloodSurface` (`components/ui/state/stateTokens.ts:20`) is keyed to the retired red `#A04030` (colors.ts:149 documents the snap-away). Repoint to the live oxblood.
- App's `vesperPrimitiveTokens.green60 #4F6F52` sits under a canon name at a non-canon value (canon sage60 `#2E5A3A` lives in `olive[600]`); `vesperSemanticTokens.textMuted`→ink80 is documented "decorative only, never text." Both are dormant (few/no call sites) — fix the declarations so they can't become a re-theme footgun. (Canon already corrected its own `blue60` to `#3D5066` to match code, so app blue is fine.)

**A8 · [P2] FloatingTabBar collapse geometry.** Collapsed circle is 56px anchored bottom-**left**; canon is 52px bottom-**right**. Also translucency is rgba parchment 0.78 without native blur (canon 0.92 + blur 12 — code comments an OTA constraint; leave blur if still constrained, fix size/side/opacity).

**A9 · [P3] Motion + naming cleanup.** Two "house curves" coexist in `motion.ts` (`Easing.out(cubic)` declared "house curve" at :50 vs the real `easing.lift` cubic-bezier(0.2,0.7,0.2,1) at :57 that drives presets) — collapse to the canon curve. Rename `hooks/useShimmer.ts` (it exports `usePulse`). Remove dead `badge`/`badgeText` styles in `FloatingTabBar` (canon: no tab badge).

**Phase A exit:** buttons/sheets/tab bar/text read as warm-paper canon; money is mono; no white sheets or espresso primaries; `make typecheck` clean; `/code-review`.

---

## Phase B — Kills & cheap ruling-follow-ups
*Fast, low-risk deletions and one-line register flips. Mostly executing design-session rulings.*

**B1 · [P2] Flip Stay status money off italic.** `StayCard.tsx:262–271` renders the money status slot in serif italic (it matched the old Stay canvas; canon ruled Productive Type wins). Change the status span to DM Sans. The single italic Vesper-voice line *above* the card stays (that's the sanctioned moment).

**B2 · [P2] Flip Costs balance-sheet money/titles to sans.** `CostsBalanceSheet.tsx:207` still renders transfer titles in serif; canon ruled the ledger total + merchant titles are DM Sans (Costs home already migrated). The colored attention banner keeps its one italic voice line.

**B3 · [P2] RevertConflictSheet → decide-before-revert.** `RevertConflictSheet.tsx:145–177` does a safe partial revert then offers force-full-vs-keep *after*. Canon ruled the decide-before-acting sequencing wins (per-dependent-edit Keep/Discard *before* any revert executes). Rework to present the choice first, then act.

**B4 · Kills on Trips Home** (canon §06b Kill-or-Draw, all ruled KILL):
- **Resume rows** ("pick up where you left off") — remove; latent drafts route through the existing dreaming/seeds trail.
- **"Worth reading" Discover row** — remove (cross-surface bleed; Trips Home is an attention router).
- **Returned notifications-as-desk-rows + "How did it go? →" debrief link** — remove the duplicate debrief entry; the returned-trip entry should route *into* the trip's memory-settle (Trip Document owns `MemorySettlePrompt`). Keep the homecoming beat only as StoryReadyEntry (Phase C).
- (Location: `components/trips/TripsHomeViews.tsx` / `TripsHomeTrail.tsx` — grep the component names.)

**B5 · Kill TripActiveFeedStrip.** Remove the home-feed card strip under the Trip Document cover (`components/trip/*`) — canon ruled it violates Trip Document's strict one-hero, two-tier (DocumentLead + AlsoMovingStream) model. Anything worth surfacing goes into AlsoMovingStream under existing phase rules.

**B6 · Kills on Discover cover** (`components/discover/DiscoverCoverHome.tsx`):
- **AtlasLoopCue** ("ATLAS REMEMBERS" row, ~:421) — remove from Discover (Atlas-owned teaser, out of scope here).
- **serverRead "START HERE" module** (~:1102–1138) — remove (survived on commit-inertia, no decision behind it).
- **InlineTOC after hero** + the legacy **"IN THIS ISSUE" SectionRule** on the fallback path (~:1175) — remove; canon's CoverHome is explicitly "quiet, no TOC" (canon already deleted its own InlineTOC).

**B7 · Remove voice persona names.** `VoiceOverlay.tsx:5–6` labels sessions "Talking with Mateus" / "Listening — Keiko". Canon ruled voice identity is singular — always "Vesper". Strip the persona names (see Phase C for the full chrome rebuild; this is the copy half).

**B8 · `your-map` → redirect, don't render.** Canon ruled `your-map` KILL (Atlas already retired the equivalent into Long View). Make `app/your-map.tsx` redirect to Atlas Long View instead of rendering a standalone map. Update the two entry points (`app/place/[placeSlug].tsx:277`, `utils/nearYouRoutes.ts`).

**B9 · `dna-card` file move.** `components/me/TravelDNACard.tsx` is a chat-attachment card, not a "Me" surface (no Me tab exists). Move it out of `components/me/` (to `components/chat/` or the cards family — its only consumer is `components/chat/AttachmentRenderer.tsx:136`) and delete the empty `components/me/` dir.

**B10 · [P3] Copy leak + dead code.** Fix `TripFolioHome.tsx:2171` "The folio is waiting for its spine." → user-facing word is "trip". Delete unimported `components/trip-plan/PlanHealthStrip.tsx`.

**Phase B exit:** removed surfaces gone with no dangling imports/exports; register flips verified on Stay/Costs; `make typecheck`; `/code-review`.

---

## Phase C — Build the newly-drawn canon
*These surfaces were drawn/finalized in design sessions (vesper 139–141). Canon is ready; build to it.*

**C1 · [P1] VoiceOverlay chrome rebuild.** Canon: `Vesper Voice & Narration.html` → `voice-narration-app.jsx` (`VoiceShellRest`, `VoiceShellListening`). Replace the shipped plain-white sheet + red end-call button with: warm `cardWarm` sheet matching every other sheet, amber/gold accents only, a **non-alarming "End"** (dark ink pill w/ gold dot in rest; amber ghost in listening) — **no red, no purple** (purple is the D24 hard line). `components/voice/VoiceOverlay.tsx` + `VoiceOrb.tsx` (VoiceOrb purple was already fixed; this is the sheet chrome + end button). Feature is behind `VOICE_ENABLED` (dark) — build it correct so it's ready when the flag flips.

**C2 · [P1] Mic permission states.** Canon: `voice-narration-app.jsx` `MicPermission` — request / denied / limited, real in-app pre-permission screens (not the native-sheet mockup). Build/replace the current pre-permission screen and narrow `MicPrivacyDisclosure.tsx` copy to what ships (it currently over-promises an interruption flow + a deleted status indicator).

**C3 · [P1] Expense Detail rebuild.** Canon: `Vesper Costs.html` → `costs-screens.jsx` `ExpenseDetail` (states normal/masked/settled/disputed). Rebuild `components/expense/ExpenseDetail.tsx` (`app/trip-expenses/[expenseId]/index.tsx`): remove the circular tinted icon well (banned on productive surfaces), DM Sans-led merchant/header, **mono amount + date** (coordinate with A2), split table with per-person owed (mono), linked-itinerary + receipt + one comment, exactly one italic voice line, typed-confirm Delete (canon `ExpenseDeleteConfirm`). Keep the full-screen pushed presentation (canon ratified it — don't revert to a sheet).

**C4 · [P2] Masked-expense create toggle.** Canon added a private/masked toggle to the Costs `AddSheet` (`costs-screens.jsx`). Add it to `components/expense/AddExpenseSheet.tsx` so masked expenses can be created, not just displayed (today the flag is server-only). Ledger + detail already render the masked state.

**C5 · [P1] StoryReadyEntry.** Canon: `trips-home-canon-screens.jsx` `StoryReadyEntry` / `StoryReadyBoard` — a Trips Home trail card for a just-returned trip's story readiness, 5 states (composing/ready/delayed/failed/sparse), consuming Trip Story's homecoming vocabulary. Ready gets the one dark primary; others stay quiet. Taps route into Trip Story; the card never composes the story. Build it in `components/trips/*`. (This is the sanctioned homecoming beat that replaces the killed B4 debrief rows.)

**C6 · [P2] RecallBand honest states.** Code has a `RecallBand` on Discover with no state model; canon (`discover-cover.jsx` `RecallBand`) drew three honest states: has-signal (names the real taste pattern), cold-start (invitation, no claim), no-signal-this-week (stays quiet — never fabricates a signal). Add the state handling to the code component.

**Phase C exit:** each drawn surface matches its canon board across all states; voice chrome has zero red/purple; `/verify` the expense-detail and add-expense flows; `/code-review`.

---

## Phase D — P1 designed mechanics (build-to-existing-canon)
*Canon for these predates the recent sessions (it's in the surface pages), but the code never built the mechanic. Larger than Phase C items.*

**D1 · [P1] The Deck run-through.** The Deck faces exist, but it's a one-card modal: Done/Not-now/primary all just close it (`FocusHome.tsx:231–249`); the "N TO CLEAR" counter + pile-peek promise a sequential triage that doesn't happen. Canon = sequential clear-through ("Run through · 3 →"). Build the advance-to-next behavior. Pairs with:
- **D1b · Canonical deck entry (rail line D):** build the aggregated "N in motion · votes, a stay… RUN ›" entry under the rail (canon `vesper-deck-entry.jsx` `DeckEntryRail`); today only per-card rail taps open the deck.
- **D1c · Comparison face:** build the Two-Stays columns deck face (`useConciergeHomeState.ts:51,189` has no `compare` layout; Pick-flex-to-2 is explicitly *not* it).

**D2 · [P1] Trips Home Between/Tempt hero.** `BetweenHome` (`TripsHomeViews.tsx:310–335`) renders no hero — just a carousel + Atlas bridge, while the standfirst promises "a few places keep pulling." Build the canon TemptShell hero (sage "A PLACE YOU KEEP CIRCLING" marker, CiteSaved receipt, "Make it a trip" conversion step) — the between-trips wedge moment.

**D3 · [P1] Trip-creation promotion moment.** Canon (`create-screens.jsx` §06) = an explicit beat: "I think this is a trip now." + captured-evidence card + **Make it a trip / Keep talking** + NotReady variant. Code fires a toast "Saved as a trip" (`chat.tsx:213–250`). Build the real promotion beat + the creation→folio handoff.

**D4 · [P1] Notifications entry points.** The Global ledger (with filter pills) and Personal ledger are *built but unreachable*: `routes.personalUpdates()` (routes.ts:383) has zero callers and its doc references a nonexistent Me-tab bell; the only bell (`trips/index.tsx:720`) routes to Trip Updates. Wire real entry points to Global + Personal. Also clean the dead unread-count computations (`(tabs)/_layout.tsx:39–42`) and repoint push-denied "Preferences" from Atlas prefs to Trust & Controls.

**D5 · [P1] Itinerary honesty details** (`components/trip-plan/*`, `app/(tabs)/trips/[tripId]/plan.tsx`):
- **Date-rail conflict dot** (oxblood) and **backbone dot** (amber ring) — plan.tsx:1409–1422 rail only has planned/empty/changed; a broken or skeleton day is invisible from the rail.
- **Empty-day:** the direct-edit branch leads with a 16:7 illustration plate (`PlanEmptyDay.tsx:232–237`) — canon bans oversized illustration cards on empty days, and this branch also drops the OPEN chip + phase voice line the read-only branch has. Make both branches match Ruling A.
- **BackboneBand theme in italic** (`BackboneBand.tsx:79`) → serif **roman** (italic is voice-only; the theme is content).

**D6 · [P1] Trip Document memory mode** (`components/trip/*`, `app/(tabs)/trips/[tripId]/memory.tsx`):
- **VesperClose** — the calm-gold "VESPER · CLOSING THE LOOP" reflective paragraph from real facts (canon `trip-memory.jsx:25–37`); code leads with a facet hero instead.
- **Shaped week-ribbon** — memory ribbon is a flat count; canon = density bars + kept-moment markers + legend (the Trips-*home* returned hero already renders the shaped ribbon; port it to the document).
- **CarriedForward** — "saved-never-visited → Keep for next time →" section (no code counterpart).
- **All-clear "ALL SET" band** — code suppresses the lead on all-clear (`shouldSuppressClearLead`); canon shows a calm-gold ALL SET band. (And the canonized empty-state wording "Nothing needs you — the trip's just unfolding." is used nowhere — adopt it.)
- **XrefBeat** — PENDING/DECIDING ghost-chips tying spine beats to attention items (`trip-imminent.jsx:39–60`).

**D7 · [P1] Trust & Controls post-deletion goodbye.** `app/atlas/account.tsx:164–199` tears down straight to `/(auth)/sign-in` on delete. Canon `account-lifecycle.jsx` `ScreenAccountGoodbye` = "Your account is gone… It was a pleasure traveling with you. / Start again". Build the dignified-exit screen. *(This route is under `/atlas/` but is a Trust & Controls surface per the named exception — editing it is in scope.)*

**D8 · [P1] Discover feed empties + map pins + saved index:**
- **Feed empties** (`DiscoverCoverHome.tsx:1265`): build the two canon states — cold-start invitation with interest chips, and empty-city ("Vesper doesn't have much of a read on Reykjavík yet." + Ask). Today both collapse to a generic EmptyHero.
- **Map pin taxonomy** (`DiscoverMapCanvas.tsx:59–147`): ~half the 12 canon pin types are unbuilt (friend/experience/place-area/unavailable/approx/suggested) and pins only handoff to `/venue`, never `/place` or `/experience`. Build the missing variants + non-venue handoffs. Swap the heart glyph in the peek card (`DiscoverPinPeekCard.tsx:44–45`) for a non-heart affinity mark (bookmark-only doctrine).
- **Saved index** (`app/atlas/saved-places.tsx`): venues-only today — wire saved experiences + stays; wire **add-to-trip from saved**; populate row states (in-plan/stale/unavailable/needs-decision are never set). *(Under `/atlas/` but a Saved & Collections surface per the named exception — in scope.)*
- **Guide "In plan" state** (`app/guide/[slug].tsx:53–56`): row supports it; the backend membership check is unwired so it never lights up. Wire it.

**D9 · [P1] Onboarding trip lane.** `app/onboarding.tsx:239–296` inserts `trip-interest` → `trip-pace` taste beats between `trip-who` and sign-up. Canon lane A is where→when→who→**sign-in at peak intent** (taste beats belong to the dreaming lane, not the trip lane). Remove the detour from the trip path.

**Phase D exit:** each mechanic works end-to-end (`/verify` the deck run-through, promotion beat, notification entry, memory mode); no regressions to the one-hero rule; `/code-review`.

---

## Phase E — Transport & ticket band (large deferred subsystem)
*The one genuinely big designed-but-unbuilt area. Post-dogfood scale; sequence last.*

**E1 · [P1] Ticket band.** Canon: Vesper Itinerary "OWNS: Ticket band (pre-departure transport)" + Route & Transport §05 — a T−24h pre-departure band on the Plan surface (boarding/gate/platform). No code counterpart (nearest is `LeaveByHintStrip` on trip home). Build it into the plan header region.

**E2 · [P1] Transport status-first system.** Canon Route & Transport §03–§04 — a transport-leg view with the 7 booking states (missing/researching/options-offered/held/confirmed/used/cancelled), by-traveler filtering, and a missing-leg "Find flights" CTA. Today only day-level connectors (`TravelSegmentRow`) + map segments exist; there's no transport-leg system. Build it (`components/trip-map/*` + a transport surface).

**E3 · [P1] Map-face route-gap banner.** Canon Route & Transport artboard 07 — a "Route gap before stop 2 … Add walk or transit" ISSUE banner in the map sheet between summary and stop rows. Not built. Add it (`components/trip-map/*`).

**Phase E exit:** transport legs render all 7 states; ticket band appears T−24h; `/verify` a booked-transport trip; `/code-review`.

---

## Phase F — Copy & polish sweep
*Cheap, do anytime after A; good "cool-down" work between big phases.*

- **F1 · Voice sweep:** ~15 "Vesper will…" hits where the voice should speak as "I" — home state copy (`surfaceStateCopy.ts:61`), `conciergeHomeInteraction.ts:83`, typing ladder (`TypingIndicator.tsx:42`). Convert to first person on speaker surfaces (leave genuine system/UI copy).
- **F2 · PrivacySeamDivider tappable:** canon makes the seam chip tap → a one-line explainer citing Trust & Controls; code has no `onPress`.
- **F3 · Trail section labels (Trips Home):** canon fixes named sections (Friends / Saved-no-trip / While-you're-here / Vesper-noticed); code merges into one "OR START FROM" and adds a "STILL ON THE DESK" label that violates the one-label rule (`TripsHomeTrail.tsx:271–279`).
- **F4 · `/trips/all` register:** title is EB Garamond serif (`typography.ts:565`); canon marks the page PRODUCTIVE / DM Sans-led. Flip the title.
- **F5 · Invite landing polish:** day-strip receipt artifact (canon horizontal "read-only until you join" strip vs code's vertical timeline); multi-select signal chips (code single-select); AvatarCluster hero vs single organizer avatar.
- **F6 · Profile screen:** stop wrapping the in-app `/profile/[userId]` in `ExternalShareShell mode="publicWeb"`; add the self-view "Edit profile"; add the empty-taste absence line; hold-to-unfollow.
- **F7 · Trip Story polish:** homecoming delayed/failed states; the edit sheet's in-sheet "VESPER'S VERSION" reference block; inline save-failed banner (vs toast).
- **F8 · Stale comments:** `Rail.tsx:9` (quiet-lens — quiet mode is dead), `Deck.tsx:4` (long-press — actual trigger is tap), `GroupVesperNote.tsx` (Fraunces mention).
- **F9 · Chat micro-drift:** context label "private - trip-linked" hyphen → canon middot "private · trip-linked" (`chat.tsx:437–446`).

---

## Not-frontend / needs an owner (surface these; a frontend agent can't finish them)

- **`[BACKEND]` Trip delete/cancel end-states.** Canon's Trip Settings end-state matrix (typed 'cancel' + 30-day retention + traveler notification; delete-with-content = all deleted + memory cleared) is unimplementable — no hard-delete/cancel endpoint exists; both paths currently map to archive (`app/trip-settings/index.tsx:50–53`). Needs backend + one canon ruling on the typed phrase (canon 'delete' always vs code's trip-name-for-content-trips).
- **`[BACKEND]` DateChangeImpactSheet impact rows.** `app/trip-dates/index.tsx` is a full-screen picker with a removed-days warning; canon wants a *sheet* child of Trip Settings with per-system ImpactRows (itinerary/stay/booking conflicts), save-blocked-until-resolved, offline queue. The impact-row data (which stays/bookings a date change breaks) needs backend. Build the sheet shell in FE; the per-system conflicts need `[BACKEND]`.
- **`[BACKEND]` Universal Search D25 action routes.** FE routing is done (`utils/universalSearchRouting.ts`), but action rows render disabled unless the backend populates `route` hints on `is_action` results. Backend must emit the hints.
- **`[BACKEND]` Deck Flight face producer.** FE face built (`DeckStructuredFace.tsx:8`); no backend card emits `layout:'flight'`.
- **`[BACKEND]` Costs disputed/reimbursement rows.** UI built; no backend dispute flag or cash-settlement event to trigger them.
- **`[LAUNCH-GATE] STORY_SHARE_ENABLED = false`** (`constants/featureFlags.ts:17`) — the entire (canon-complete) Trip Story sharing surface is dark. Flip is a launch decision, not a code fix.
- **`[LAUNCH-GATE] VOICE_ENABLED`** — live mic dark; build Phase C1/C2 correct behind it, but going live needs the 6 Fly secrets + 3rd Fly process + on-device audio QA (a product/ops decision).
- **`[DECISION] TimelineObjectRow vs PlanBlockRow fork.** Canon's row system says SpineRow is the canonical itinerary row grammar, but the shipped Plan surface renders through a bespoke `PlanBlockRow` while `TimelineObjectRow` (the row-system member) lacks the commitment states and is used only by `TripFolioHome`. Reconciling them is an architecture decision, not a quick edit — decide whether to fold PlanBlockRow onto the row system or bless the fork.
- **Booking per-category vocabulary + group-approval states, Stay compare recommendation feed, per-offer reason lines** — mostly need data the backend doesn't emit yet; build UI where the data exists, tag the rest `[BACKEND]`.

---

## Suggested order & rationale
1. **A** (foundations) — everything downstream inherits correct tokens; highest visible-polish-per-effort.
2. **B** (kills/flips) — fast, shrinks surface area, removes drift before you build on it.
3. **C** (drawn canon) — design is freshest and unambiguous here; satisfying, self-contained builds.
4. **D** (P1 mechanics) — the load-bearing behavior gaps (deck run-through, wedge hero, promotion beat, notifications).
5. **F** (polish) — interleave with D as cool-down.
6. **E** (transport) — largest, most deferrable; do when the wedge surfaces are solid.
Handle the "needs an owner" bucket by surfacing to the user/backend as you hit each — don't block a phase on it.

## Provenance
This plan consolidates a 2026-07-11 fresh 8-domain design-vs-code audit (foundations, trips, planning, home+chat, productive surfaces, discover/places/search, entry/social/memory, route-coverage) reconciled against canon rulings in bundles vesper 138–141. Every `file:line` is from the audit's read of `main` on 2026-07-11 — **verify current before editing** (§0.5). The audit found **zero P0s**; nothing here is user-breaking, it's alignment and completion.
