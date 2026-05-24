# Frontend Visual Polish — Master Punch List

> Status: synthesis of the 10 area reports under `docs/audits/frontend-visual-polish-2026-05/areas/`
> Created: 2026-05-24
> Scope: **perceived** product quality for `Travel App` — does Vesper *feel* finished, native, calm, premium, and trustworthy in the first week of internal use? This is the companion to the earlier `frontend-polish-2026-05` round (design-system drift). That round's P0/P1 fixes are already merged (`3a55dbe`, `bf19e21`), so the findings here sit on top of a partially-cleaned baseline.
> Goal: a buildable, prioritized list that gets the app polished enough to dogfood — not a redesign.

## How to read this

- **Severity.** `P0` = a concrete dogfood-*blocking* journey issue **or** a core-identity-blocking trust/doctrine violation that ships in the default experience. `P1` = degrades trust/native/premium feel on a core surface in week one. `P2` = real polish or regression-prevention, not blocking.
- **Fix category** (the lens the work lives in): `visual design`, `native behavior`, `copy`, `state coverage`, `performance`, `QA-process`. Most items have a primary category; a few are mixed.
- **Evidence basis.** This matters more than usual: **every one of the 10 area reports is static / code-based.** No researcher could render a screen. `react-native-web` is not installed, no iOS simulator was booted, and Maestro was not on `PATH` in any pass. So this round — whose entire premise is "how does it look on real screens" — was conducted *blind*. That makes the visual-QA item (P1-9) the highest-leverage process fix: it is the only thing that converts the rest of this list from inference to observation. Per-item, "Evidence basis" is `static/code` for all current findings; the column exists so future reruns can mark items `rendered/runtime` once the lane runs.

## Calibration note

Each area report independently capped its own findings at P1, except area `07`, which raised one true P0 (a journey dead-end). Synthesis keeps that P0 and elevates **one** additional item to P0: the default-mock privacy leak. The reasoning mirrors the prior round's discipline — elevate only when an item is *core-identity-blocking*, violates a **locked** doctrine, and ships in the surface a tester actually hits first. Privacy ("invisible privacy, visible care," `Travel App/docs/Design Language.md:22-26`) is the product's stated moat; mock mode is the **default** dogfood mode; the offending copy is the exact constraint-attribution anti-pattern the docs ban (`Travel App/docs/Design Language.md:319`). Two P0s, both bounded fixes. Nothing else is inflated.

## Verification status (2026-05-24)

Every citation in this list was re-checked against the current code after synthesis (the area reports were written blind, so this was the missing step). Result: citations are **overwhelmingly accurate** — no fabricated findings, no missing files. Caveats:

- **Line drift:** ~12 references are off by 1–2 lines (the claim holds; the exact line moved). Examples: expenses route is registered at `_layout.tsx:245` (not `:243`); the Changes empty text is at `changes.tsx:86-91` (not `:85-89`); `trip-info` revoke mutation is at `:242` (not `:354`); `MemoryMomentCard` hero `height: 220` is at `:148` (not `:147`); `illustrationVariant.ts` keyword table is at `:16` (not `:15`). These are not re-listed per-item — treat cited lines as ±2.
- **One substantive correction (P0-1):** the trip-*creation* step is now guarded — `createAndOpen` (`trips/index.tsx:81`) has an in-flight lock and a failure toast (`:83`, `:90`). So the "silent no-op" is specifically the **send** inside the opened ideation chat, not the create call. The defect is still real and still P0 (undefined `tripId` → `useConciergeChat.ts:343` early-returns the send), but the wording below is corrected.
- **One minor nuance (P1-7):** `ContentGraphBanner`'s action pill uses `spacing.xs` (~4pt) vertical padding, while `GeofenceBanner`'s uses `spacing.xxs` (~2pt). Both are still below 44pt with the close control; the "same pattern" framing is structurally true but the exact value differs.
- **Render attempt:** I tried to produce real first-viewport screenshots (the whole point of this round). It is **not possible in this environment** — managed Expo app with no `ios/` project, and `expo run:ios` fails because CocoaPods 1.16.2 crashes on Ruby 4.0.5 (`Encoding::CompatibilityError` in `pod install`) plus no signing cert; `react-native-web` and Maestro are also absent. So P1-9 remains the gating item, and all evidence here stays `static/code`.

The **Rendered Composition / First Viewports** findings (area 01) were verified surface-by-surface against the code and all hold — see each item's Evidence line. Notably the trip-home file's own `:14` comment references `P1-4`, and Discover's `:722` comment literally calls itself a "browse console before Vesper expresses an opinion," corroborating P1-1 and P1-3 from inside the source.

## Resolution status

Implementation is proceeding section by section. Static gates after each section: `tsc --noEmit`, `jest`, `expo lint`.

| ID | Status | Notes |
|----|--------|-------|
| P0-1 | ✅ Fixed (static-verified) | `useConciergeChat` now takes `seedAsNewThread`; chat passes the real ideation trip id so the composer + prefill auto-send work, opener preserved. tsc 0 · jest 945 pass. **Needs device verification** (no sim/web here). |
| P1-8 | ◑ Largely fixed | **Contrast:** meaningful `text.tertiary` (~2.8:1) → `metadata.default` (~5.7:1) or `metadata.subtle` (~4.6:1, for done/inactive states) across NavPills inactive labels, VenueCard type, TravelSegmentRow mode/note, ProposalReviewSheet (timestamps/conflict/impact label), LiveTodaySection (done times+titles, free-day, view-day, group pulse), Discover (near-me meta, masonry stat). Decorative tertiary (chevrons, dots, separators, section eyebrows) left as-is. **Wrap:** ProposalReviewSheet diff `numberOfLines` 1→2 (was hiding the changed item). **Deferred:** absolute-hero-overlay wrap on TripCard title/date + MemoryMomentCard caption — risky to change without large-text screenshots (could overflow the hero). tsc 0 · jest 945 · lint 0. |
| P1-7 | ✅ Fixed (static-verified) | Shared primitives fixed so the floor propagates: `ScreenHeader` back + icon actions → `IconButton` (44pt), text actions → `Tap minTarget="auto"`, balanced the back placeholder + added action gap; `NotificationBell` → `minTarget="auto"` (badge preserved). One-offs brought to 44pt via `hitSlop` (no layout growth): GeofenceBanner + ContentGraphBanner close/action, Discover search-clear, Discover event filter pills (vertical only — horizontal scroll), `BlockWhyRow` "Why this?" inline disclosure. Chat header back/voice were already ≥44pt via existing `hitSlop={8}` (audit counted only the visual box). tsc 0 · jest 945 · lint 0 errors. ScreenHeader targets are ~6pt larger now — **needs a screenshot check** for header balance. |
| P1-6 | ◑ Largely fixed | **Done:** locked composer strings (group `"Message the group"`; private already locked); user-facing **"Concierge" → "Vesper"** across ~14 files (Me sub-screens, concierge home/history, venue, experience sheet, story, trip memory, guide, discover editorial copy, invite, DNAStrip, VoiceSegmentCard, personal-memory, trips welcome) — visible text **and** paired a11y labels; Concierge-home search placeholder → "Ask Vesper anything". **Intentionally kept "Concierge":** the tab name + notification bucket (IA), and the *settings* screens (trip-settings autonomy, constraints data/reset) per the doctrine's "reserve Concierge for lower-level settings" allowance. **Deliberately deferred (needs founder's voice, not my taste):** permission-prompt concision, error-message brand voice, and the generic entry prompts / `COMPOSER_SUGGESTIONS`. tsc 0 · jest 945 pass. |
| P1-5 | ✅ Fixed (static-verified) | Four sub-fixes: Changes timeline now shows error/retry + loading skeleton instead of "No changes yet" on failure (`changes.tsx`); Concierge Home create is in-flight-guarded with a failure toast (`concierge/index.tsx`); Trip Home Days uses the `withRefetch` overload + an error/retry branch (`trips/[tripId]/index.tsx`); `OfflineBanner` copy no longer over-promises auto-retry, and `useOfflineGate` now gates the three cited mutations (trip-settings cadence, photos upload, trip-info invite/revoke). Updated the trip-workspace smoke test's `useItinerary` mock to the new shape. tsc 0 · jest 945 pass. Error/offline branches only fire in real mode — **needs device verification**. |
| P0-2 | ✅ Fixed | The 5 cited spots rewritten to quality-attributed copy (`mocks/chat.ts:30,32`, `useConciergeChat.ts:140,143`, `mocks/itinerary.ts:172,235`). Extended to `constants/mocks/venues.ts`: all person-named constraint copy in `agent_reasoning`/`group_fit` (venues 1,2,4,5,6,8) rewritten — no "Alex/Sarah/Mike/Diana" + constraint pairings remain. Note: those venue fields are currently **unrendered** (no consumers found), so they were latent, not a live leak; fixed as hygiene per the "treat fixtures as product copy" call. `profile.ts`/`voice.ts` matches left as-is (user's *own* private settings/logs — correct by doctrine). tsc 0 · jest 945 pass. |

## Severity summary

| ID | Sev | Surface | One-line | Fix category | Evidence |
|----|-----|---------|----------|--------------|----------|
| P0-1 | P0 | New trip → private chat | Creating a planning trip lands in a chat where sends are a silent no-op (`tripId` undefined) | native behavior + state coverage | static/code |
| P0-2 | P0 | Group chat / plan (mock default) | Default mock copy names constraint categories in group-visible surfaces — breaks the privacy contract | copy | static/code |
| P1-1 | P1 | Discover | Opens as a six-pill browse console with color-block imagery, not an opinionated place-aware index | visual design + copy | static/code |
| P1-2 | P1 | Add Expense | Custom overlay (not native modal): backdrop-dismiss can drop a long form; disabled-button validation feels stuck | native behavior | static/code |
| P1-3 | P1 | Trip workspace | Pill animates but body teleports; pills look like a segmented control but push routes; over-chromed first viewport | native behavior + visual design | static/code |
| P1-4 | P1 | Proposal / recommendation review | Reads as audit/workflow UI (badges, spinner, uncapped alternatives, quiet vote feedback), not concierge judgment | visual design + copy | static/code |
| P1-5 | P1 | Changes, Concierge home, Trip home, mutations | Load failures misreport as "nothing here" / silent no-op on trust surfaces | state coverage | static/code |
| P1-6 | P1 | App-wide chrome | "Concierge / proposal / vote / backend" mechanics language + overexplained permissions read as software, not a companion | copy | static/code |
| P1-7 | P1 | Header actions, bell, banners, chat mic, filters | Many high-traffic controls still below the 44pt floor despite `IconButton` existing | native behavior | static/code |
| P1-8 | P1 | Metadata text + large-text layouts | Meaningful text in faint `text.tertiary`; one-line caps + fixed heights truncate trust-carrying content | visual design | static/code |
| P1-9 | P1 | Engineering process | The screenshot QA lane was built last round but **never run**; this whole audit is blind | QA-process | static/code |
| P2-1 | P2 | Motion / feedback | Voice spring overshoot, orb doesn't encode states, generic spinners in product moments, partial Reduce-Motion | native behavior + visual design | static/code |
| P2-2 | P2 | Sheets app-wide | Fragmented presentation, nested modals, immediate revert without confirm, a safe-area gap | native behavior | static/code |
| P2-3 | P2 | Photos, Discover, sheets, image send | Unvirtualized growth paths + a lazy-fetch flag misalignment + image-send freeze | performance | static/code |
| P2-4 | P2 | Chat attachment cards, group fleuron, purple | Rich Vesper cards lag the new substrate; Unicode fleuron in group; purple leaks into decoration | visual design | static/code |
| P2-5 | P2 | Private chat loading | First-load private chat shows generic bubble skeletons, contradicting the envelope substrate | visual design + state coverage | static/code |
| P2-6 | P2 | Stale data + photo/mic permission recovery | Stale-data banners and persistent permission recovery exist only on some surfaces | state coverage | static/code |
| P2-7 | P2 | Chips, reaction/vote cards, filters | Selected state is color-only — invisible to VoiceOver and color-blind users | visual design | static/code |
| P2-8 | P2 | Me tab | Still reads as profile + library + settings dashboard once Travel DNA scrolls away | visual design | static/code |
| P2-9 | P2 | Trip cards, Discover, Story | Honest-illustration vocabulary is only Lisbon/Brooklyn/generic — unknown destinations collapse to one look | visual design + content | static/code |

---

## P0

### P0-1 — Creating a planning trip lands in a chat where sending silently does nothing
**Surface:** Trips `+` / zero-trip CTA → Concierge private chat (`app/(tabs)/trips/index.tsx`, `app/(tabs)/concierge/chat.tsx`, `hooks/useConciergeChat.ts`).
**User impact:** This is a hard dogfood dead-end on the most natural first action. Trip *creation* is now guarded (`createAndOpen` has an in-flight lock and a failure toast), but it routes to Concierge chat **without passing the new trip id**, and for an ideation trip with no destination the screen passes `undefined` as `tripId` into `useConciergeChat`, whose send path returns immediately before any message (mock or real) is added. So the user lands on a private Vesper surface, types, and the **send** silently does nothing — no bubble, no error (the failure toast only covers a `createTrip` rejection, not the dead send). A tester who picks "plan a trip" over "open the seeded trip" hits a wall in the first minute.
**Evidence:** guarded create that drops the returned id — `Travel App/app/(tabs)/trips/index.tsx:81`, `:86`, `:87` (in-flight guard `:83`, failure toast `:90`); zero-trip CTA uses the same path — `Travel App/app/(tabs)/trips/index.tsx:184-187`; `undefined` tripId passed — `Travel App/app/(tabs)/concierge/chat.tsx:142-145`; send returns early on missing tripId — `Travel App/hooks/useConciergeChat.ts:343`.
**Evidence basis:** static/code (verified against current source 2026-05-24; not reproduced on device — see Verification status).
**Fix direction:** After `createTrip`, route with the real trip id; *or* make ideation/private chat explicitly support a no-trip conversation. Whichever path, make a blocked send *visible* (disabled composer with reason, or an inline error) so it can never read as "the app ignored me."
**Verification:** Offline smoke test: Trips `+` → create ideation trip → private chat opens → prefilled message appears as a user bubble → Vesper response streams. Add to the Maestro dogfood script once the lane runs (P1-9).
**Fix category:** native behavior + state coverage.
**Source report:** `areas/07`.

### P0-2 — Default mock copy leaks constraint attribution into group-visible surfaces
**Surface:** Group chat itinerary attachments, plan copy, and a mock private recommendation (`constants/mocks/chat.ts`, `constants/mocks/itinerary.ts`, `hooks/useConciergeChat.ts`).
**User impact:** "Invisible privacy, visible care" is locked doctrine and the product's stated moat: surfaces show *what* changed, never *who required what*, and never in constraint language (`Travel App/docs/Design Language.md:22-26`, anti-pattern at `:319`). The default mock journey violates this in the group room — copy says a meal "fits all dietary needs" and "3 people wanted downtime." Because mock mode is the **default** dogfood mode, this is the version internal users see first: the app promises privacy in its chrome, then the group-visible plan explains itself in exactly the vocabulary the doctrine forbids. It is the fastest way to lose a tester's trust.
**Evidence:** "fits all dietary needs" — `Travel App/constants/mocks/chat.ts:30`; "3 people wanted downtime" — `Travel App/constants/mocks/chat.ts:32`; mock private rec with `why_for_group: "Fits all dietary needs, mid-range price…"` — `Travel App/hooks/useConciergeChat.ts:140-147`; aggregate downtime rationale in plan copy — `Travel App/constants/mocks/itinerary.ts:171-173`, `:234-235`.
**Evidence basis:** static/code.
**Fix direction:** Rewrite group-visible mock copy to obey the doctrine — quality-attributed reasons only ("incredible seafood and a quiet courtyard"), never "dietary," "restrictions," "budget," or "N people wanted…". Keep constraint-aware reasoning in `why_for_person` (private channel only). Treat fixtures as product copy, not throwaway data, since they are the default experience.
**Verification:** Fixture lint / snapshot check flagging `dietary`, `budget`, `constraint`, `preferences`, `people wanted`, `restrictions` in any group-visible mock string. Manual: open the seeded trip's group chat and plan in mock mode and read every visible sentence.
**Fix category:** copy.
**Source report:** `areas/07` (raised P1 in-lane; elevated to P0 here per the calibration note — core-identity-blocking, default surface, locked-doctrine violation).

---

## P1

### P1-1 — Discover opens as a browse console, not an opinionated place-aware index
**Surface:** `app/(tabs)/discover/index.tsx`, `components/discover/FeedItemRenderer.tsx`.
**User impact:** Discover leads with a sticky search bar plus six peer pills (Angles / Friends / For you / Events / Trending / Guides) *before* Vesper expresses any opinion, and its cards render flat gradient/color blocks instead of place imagery. The result reads like a generic travel marketplace, not "the knowledgeable local friend with taste." The code itself flags this: a TODO says the six peer pills make Discover "read as a browse console before Vesper expresses an opinion." It is the least Vesper-specific high-traffic tab and the one most likely to feel generic in week one.
**Evidence:** six-pill rail + fixed header — `app/(tabs)/discover/index.tsx:53`, `:700`, `:733-734`; self-flagged TODO — `:722`; generic search copy — `:705`; taxonomy-led first content ("The index for", view toggle) — `:790`, `:801`, `:933-953`; color-block imagery — `:1443`, `:1527`, `:1851`; feed color dots / placeholder image blocks — `components/discover/FeedItemRenderer.tsx:115`, `:259`, `:308`, `:344`. Doctrine: specific, editorial, place-aware — `Travel App/docs/Brand Identity.md:31`, `:214`.
**Evidence basis:** static/code.
**Fix direction:** Collapse the first viewport to one place thesis — destination, Vesper's editorial read, and one primary list (one featured angle + 1–2 exemplar venues). Demote search to a compact affordance; reduce first-order nav to primary + one contextual mode; push Friends/Trending/Guides below the fold; make Events a "tonight/dates" module rather than a top peer. Use real photography where seeded, `HonestIllustration` where not — never bare color blocks on editorial cards.
**Verification:** First-viewport screenshot on SE / 15 / large text (via P1-9). Pass condition: a reviewer states Discover's job in five seconds and the first focal point is place content, not a filter row.
**Fix category:** visual design + copy.
**Source reports:** `areas/01`, `04`, `06`, `08`, `10`.

### P1-2 — Add Expense is a custom overlay with fragile dismissal and stuck-feeling validation
**Surface:** `components/expense/AddExpenseSheet.tsx`, mounted from `app/trip-expenses/index.tsx`.
**User impact:** The single most text-heavy, multi-minute form in the app is an absolutely-positioned `KeyboardAvoidingView` with a backdrop `Pressable` that immediately calls `onClose` — not a native `Modal`. So a tap outside the form (easy on a keyboard-covered screen) can discard a long entry — including after a receipt scan or custom splits — with no dirty-state confirmation, and the overlay must own every safe-area/keyboard edge case itself. Submit is purely disabled-button-driven, so the specific toast validation is unreachable for most invalid states; a disabled button at the bottom of a long, keyboard-covered form reads as "broken" even when the logic is correct, especially for percentage/exact split modes whose per-person inputs sit far below the amount field.
**Evidence:** custom overlay, not Modal — `components/expense/AddExpenseSheet.tsx:355`, `:359-360`, `:692`; conditionally mounted on a non-modal route — `app/trip-expenses/index.tsx:321`, `app/_layout.tsx:243`; disabled-button gating makes toast validation unreachable — `:335`, `:674`, `:238-252`; split inputs far below amount, percentage constraint only as caption — `:617`, `:663`.
**Evidence basis:** static/code.
**Fix direction:** Promote to a real `Modal` page sheet (or a shared sheet primitive — see P2-2), add native accessibility isolation and dirty-state confirmation on backdrop/swipe dismiss, and replace pure disabled-button gating with inline field-level errors that say what needs attention.
**Verification:** On SE + notched iPhone: open, focus every field, switch split modes, scroll to the bottom, then tap the backdrop — confirm data is not silently lost and VoiceOver focus stays inside the sheet.
**Fix category:** native behavior.
**Source reports:** `areas/02`, `03`, `09`.

### P1-3 — Trip workspace: animated pill, teleporting body, and a segmented-control that actually pushes routes
**Surface:** `app/(tabs)/trips/[tripId]/_layout.tsx`, `components/trip/TripHeader.tsx`, `components/ui/NavPills.tsx`, `app/(tabs)/trips/[tripId]/index.tsx`.
**User impact:** Three native-feel problems compound on the most-used in-trip surface. (1) The pill has a 220ms sliding thumb but the nested stack disables screen animation (`animation: 'none'`), so the chrome says "smooth segmented control" while the body teleports — a split signal that reads as unfinished. (2) The pills *look* like an in-place segmented control but each selection pushes a route, so back behavior can traverse internal mode history instead of returning to the trip list — surprising on a control that signals "switch view." (3) The first viewport stacks global tabs + sticky header (back, switcher, avatar stack, settings) + the pill row before any trip content, reading as a project tool rather than "entering a trip."
**Evidence:** pill animates, stack does not — `components/ui/NavPills.tsx:66`, `:68`, `app/(tabs)/trips/[tripId]/_layout.tsx:77`, `:80`; segmented-control look but push semantics — `components/ui/NavPills.tsx:49`, `:76-89`, `components/trip/TripHeader.tsx:81-94`; chrome stack before content — `components/trip/TripHeader.tsx:97-147`, plan landing modules begin at `app/(tabs)/trips/[tripId]/index.tsx:193-244`; file comment acknowledging the nav dependency — `:14-26`.
**Evidence basis:** static/code.
**Fix direction:** Decide the mental model. If pills are *state*: switch in place (replace, not push), add a subtle body cross-fade or native horizontal transition that respects Reduce Motion, and make back leave the workspace. If pills are *navigation*: style them less like a segmented control and restore native push transitions. Either way, add alternate entry points to Chat/Map/Photos/Memory in the landing content *before* trimming header chrome, so nothing is orphaned; collapse the header after first scroll.
**Verification:** On SE / 15 / large text: tap Plan → Map → Photos → Chat, then use the visual back button and the iOS edge-swipe; confirm behavior matches the chosen model. Count controls before the first trip-specific content line.
**Fix category:** native behavior + visual design.
**Source reports:** `areas/01`, `02`, `03`, `07`.

### P1-4 — Proposal / recommendation review reads as audit UI, not concierge judgment
**Surface:** `components/trip/ProposalReviewSheet.tsx`, `components/chat/RecommendationBlock.tsx`, `components/trip-plan/PlanChangeStrip.tsx`.
**User impact:** This surface carries the product's central promise — Vesper makes an opinionated move and shows enough to trust it — but it currently leans on badge-heavy metadata, a generic spinner, an uncapped "alternatives considered" list, icon-led fact-box reasoning, and backend mechanics language ("votes", raw `proposal_type`, "when the backend supports it"). That weakens the "recommendation, not options" doctrine at the exact moment the user decides whether to trust Vesper. Feedback is also too quiet: votes update optimistically but success/failure has no haptic, toast, or inline rollback explanation, and the pending spinner only appears on Approve even if the user tapped Reject — so a core group decision feels ambiguous on a flaky network.
**Evidence:** spinner instead of anticipation — `ProposalReviewSheet.tsx:302-305`; badge-heavy header — `:323-330`; uncapped alternatives — `:367-389`; quiet/uneven vote feedback — `:186`, `:212`, `:218`, `:729-733`; mechanics copy ("Voting is off… when the backend supports it") — `:741-755`; reasoning as icon fact-box — `components/chat/RecommendationBlock.tsx:43-65`, `:99-107`; workflow labels in the change strip — `components/trip-plan/PlanChangeStrip.tsx:138-150`. Doctrine: recommendation as structured prose on the page, not a rigid card — `Travel App/docs/Design Language.md:217`, `:228`.
**Evidence basis:** static/code.
**Fix direction:** Redesign as a concierge judgment surface: verdict first, one clear proposed move, capped alternatives (≤2, only when truly useful), no spinner (anticipation copy / reserved slot), fewer badges. Rewrite mechanics copy around outcomes ("Move dinner to 8:30", "The group is split", "Sarah can make this call"). Add one feedback pattern for optimistic / pending / rollback / confirmed, with success+error haptics and a quiet inline or toast message; show the spinner on the actually-tapped action.
**Verification:** Screenshot loading / open / accepted-applied / apply-failed states; cast each vote and fail one offline. A new tester should be able to act in <5s and know whether their vote landed.
**Fix category:** visual design + copy.
**Source reports:** `areas/02`, `04`, `07`, `08`.

### P1-5 — Load failures misreport as "nothing here" or a silent no-op on trust surfaces
**Surface:** `app/(tabs)/trips/[tripId]/changes.tsx`, `app/(tabs)/concierge/index.tsx`, `app/(tabs)/trips/[tripId]/index.tsx`, plus ungated mutations.
**User impact:** State *primitives* are good now (`EmptyState`, `ErrorState`, `Skeleton`, `OfflineBanner`), but adoption is uneven on exactly the surfaces where early-backend flakiness will bite. The Changes timeline — Vesper's audit trail — renders "No changes yet" on a load *failure*, which reads as "Vesper made no changes." Concierge Home's create-trip path has no disabled/error/retry affordance, so a backend 500 looks like the app ignored the tap. Trip Home drops the Days section entirely when only the itinerary read fails, making the workspace look thin. And the root offline banner promises "changes will retry when you reconnect," but the `useOfflineGate` helper isn't broadly adopted — settings, invites, and photo uploads still fire and rollback later while chat calmly refuses, so behavior is inconsistent on flaky networks.
**Evidence:** Changes shows empty on failure — `app/(tabs)/trips/[tripId]/changes.tsx:62-63`, `:85-89`, hook can error `data/planState.ts:84`; Concierge Home create unguarded — `app/(tabs)/concierge/index.tsx:43-52`, `:177-180` (vs guarded Trips `app/(tabs)/trips/index.tsx:78-90`); Trip Home drops Days on itinerary error — `data/itinerary.ts:29`, `:44-48`, `app/(tabs)/trips/[tripId]/index.tsx:76`, `:270-293`; offline overpromise + ungated mutations — `components/ui/OfflineBanner.tsx:20-30`, `hooks/useNetworkState.ts:75-85`, `app/trip-settings/index.tsx:106-109`, `app/trip-info/index.tsx:330`, `:354`, `app/(tabs)/trips/[tripId]/photos.tsx:112`, `:139`.
**Evidence basis:** static/code.
**Fix direction:** Render the error/retry branch on every dogfood-critical read (start with Changes, Trip Home Days, Concierge Home create). Add a small `StaleBanner`/`RefreshFailedBanner` based on the Notifications pattern. Adopt `useOfflineGate` on user-facing mutations, or soften the offline-banner promise to match what surfaces actually do. The state matrix in `areas/05` lists the required coverage per surface.
**Verification:** Add a static check: a dogfood-critical screen that imports a data hook exposing `error`/`isError` but renders no `ErrorState`/inline error fails. Device network-toggle on the dogfood top five (create from Concierge Home, send private chat, open Changes, add photos, settle expense).
**Fix category:** state coverage.
**Source report:** `areas/05`.

### P1-6 — Chrome copy reads as software managing travel data, not a companion
**Surface:** Concierge/Trips entry prompts, permission prompts, Discover/Me chrome, error/loading defaults.
**User impact:** High-traffic chrome still slips into generic assistant/startup/backend language — "Ask me anything about travel…", "Suggestions", "proposal", "vote", "For You", "research team", "Concierge team", "check your connection", "start from scratch" — and permission prompts overexplain internal mechanics (raw-mic streaming, "Taste DNA dimensions that get richer"). That makes Vesper feel like a SaaS chatbot managing data rather than a quietly opinionated friend. The contrast is sharpest *inside the same codebase*: the mock travel content is specific and alive while the chrome around it is generic.
**Evidence:** generic concierge prompts — `app/(tabs)/concierge/index.tsx:58-60`, `:84-86`, `:170-175`; generic trip prefills — `app/(tabs)/trips/index.tsx:170-195`, `:253-275`, `:299-310`; permission overexplanation — `components/ui/PermissionRationale.tsx:57-84`, `components/voice/MicPrivacyDisclosure.tsx:165-210`, `components/trip/GroupAndLearnConsentSheet.tsx:84-87`, `:111-115`; Discover taxonomy copy — `app/(tabs)/discover/index.tsx:705-718`, `:967-972`, `:1481-1505`; generic error defaults — `components/ui/ErrorState.tsx:42-47`, `components/ErrorBoundary.tsx:107-111`; locked composer string not used in group — `app/(tabs)/trips/[tripId]/chat.tsx:420-423` (doctrine `Travel App/docs/Brand Identity.md:230-235`). Stronger contrast examples — `constants/mocks/profile.ts:49-51`, `constants/mocks/discover.ts:75-89`.
**Evidence basis:** static/code.
**Fix direction:** Use "Vesper" where the relationship matters; reserve "Concierge" for low-level settings. Replace generic entry prompts with one or two concrete, opinionated examples seeded by current trip/location/season. Reduce each permission prompt to one concrete benefit + one quiet privacy promise; move mechanics to a "Learn more"/settings layer. Apply the locked composer strings. Build a shared copy checklist: concrete place/person/trip noun, no backend nouns, no raw mechanics, one clear action verb.
**Verification:** String audit flagging `Concierge`, `proposal`, `backend`, `try again`, `No .* yet`, `Something went wrong`, `For You` across `app/**`, `components/**`, `constants/**`. For each empty state, require an answer to "what does this say about *this* user/trip/place/moment?"
**Fix category:** copy.
**Source report:** `areas/04`.

### P1-7 — Many high-traffic controls are still below the 44pt floor
**Surface:** `ScreenHeader` actions, `NotificationBell`, chat/location banners, private-chat mic, Discover filters, `BlockWhyRow`.
**User impact:** `minTouchTarget 44pt` is documented "Non-negotiable" and the canonical `IconButton` now guarantees it — but `Tap` still defaults to no minimum, and many controls hand-roll compact hit areas (a 22pt icon with 8pt padding is ~38pt; the chat mic is ~36pt). These are controls dogfooders hit constantly, and missed taps feel non-native and uncertain. The gap now is inconsistent *adoption* of a primitive that already exists, not a missing primitive.
**Evidence:** `Tap` defaults to no min target — `components/ui/Tap.tsx:32-39`, `:53`; `IconButton` exists and is correct — `components/ui/IconButton.tsx:1`, `:84`; `ScreenHeader` ~38pt actions — `components/ui/ScreenHeader.tsx:95-103`, `:130`; `NotificationBell` ~38pt — `components/ui/NotificationBell.tsx:31-58`; banner pills/close ~minimal — `components/chat/GeofenceBanner.tsx:54-100`, `components/chat/ContentGraphBanner.tsx:50-106`; private mic ~36pt — `app/(tabs)/concierge/chat.tsx:754-761`, `:995`; Discover filters/clear — `app/(tabs)/discover/index.tsx:263`, `:1282`, `:1290-1315`; `BlockWhyRow` 3pt vertical — `components/trip/BlockWhyRow.tsx:56`, `:97`. Doctrine `Travel App/docs/Design Language.md:153-154`.
**Evidence basis:** static/code.
**Fix direction:** Make `IconButton` the only approved bare-icon path and migrate `ScreenHeader` actions, the bell, banner dismiss/action controls, and the chat mic to it; or make `Tap minTarget="auto"` the default for icon-like controls (apply `hitSlop` to reach 44pt when the visual must stay small). Keep an explicit `InlineTap` exception for genuine inline text links.
**Verification:** Dev-only overlay drawing 44pt bounds around every `Tap`/`IconButton`; unit tests asserting computed min target/hitSlop. VoiceOver + SE pass on week-one loops (switch trip tabs, send/stop, dismiss a banner, filter Discover).
**Fix category:** native behavior.
**Source reports:** `areas/03`, `10`.

### P1-8 — Faint metadata text and large-text truncation hide trust-carrying content
**Surface:** `NavPills` inactive labels, `VenueCard`, `LiveTodaySection`, `TravelSegmentRow`, proposal timestamps/diffs, Discover metadata; plus `TripCard`, `MemoryMomentCard`, banners under Dynamic Type.
**User impact:** Two accessibility-resilience problems that read as "the app is hiding the useful part." (1) `text.tertiary` (`#9C9A90`, ~2.82:1 on white, ~2.39:1 on canvas — below the 4.5:1 floor) carries *meaningful* labels — venue type, done times, travel mode, proposal timestamps/diffs, Near-Me stats — even though the tokens document tertiary as decorative-only. (2) High-value surfaces cap content to one or two lines inside absolute/fixed layouts, so at accessibility text sizes trip names cover the hero, proposal diffs hide the changed item, and live-trip activity truncates.
**Evidence:** tertiary on meaningful text — `components/ui/NavPills.tsx:170`, `components/chat/VenueCard.tsx:67`, `:106`, `components/trip/LiveTodaySection.tsx:349-467`, `components/trip/TravelSegmentRow.tsx:96-100`, `ProposalReviewSheet.tsx:889`, `:1023`, `app/(tabs)/discover/index.tsx:1722`, `:1862`; token intent — `constants/colors.ts:128`, `:135`, `constants/typography.ts:232`. One-line/absolute caps — `components/trip/TripCard.tsx:136-137`, `:261`, `components/trip/MemoryMomentCard.tsx:35`, `:131`, `:147`, `ProposalReviewSheet.tsx:471-477`, `components/trip/LiveTodaySection.tsx:100-107`, `:247-249`, banners `components/chat/GeofenceBanner.tsx:45`, `components/chat/ContentGraphBanner.tsx:43-46`.
**Evidence basis:** static/code (contrast computed from tokens; truncation inferred from styles — both need large-text screenshots to confirm).
**Fix direction:** Promote meaningful supporting text from `text.tertiary` to `metadata.default`/`text.secondary`; keep tertiary for rules, chevrons, and non-semantic dots only. Let trust-carrying text (destination/venue/trip names, curator hooks, proposal diffs) wrap or reveal full text on tap; avoid fixed heights where content must scale; move hero captions below imagery past a text-scale threshold.
**Verification:** Contrast test for every text token on primary/secondary/canvas with a decorative allowlist. Screenshots at default / Large / Accessibility-XXL on SE + Pro for Trips postcards, trip header, Discover, composer, vote/reaction cards, Plan, proposal sheet, Memory cards (via P1-9).
**Fix category:** visual design.
**Source report:** `areas/10`.

### P1-9 — The screenshot QA lane was built last round but never run, so this audit is blind
**Surface:** Engineering process (`package.json`, CI, `eas.json`, `.maestro/*`).
**User impact:** This is the meta-finding that gates the rest. The premise of this round — "how does it look on real screens" — could not be tested by any of the 10 researchers: `react-native-web` is missing, no simulator was booted, Maestro wasn't on `PATH`. The prior round *built* a Maestro lane + scenarios + runbook but left it "built, unrun." So every visual claim here is inference from code, and typography regressions, cramped SE layouts, substrate drift, and touch-target misses can all merge green. Until someone runs the lane, polish regressions stay invisible — which contradicts the project's own "the screen is the eval" doctrine.
**Evidence:** Maestro flows exist for every focus surface — `.maestro/01-trips.yaml` … `.maestro/06-me.yaml`; no researcher could render (recorded in each report's Evidence section, e.g. `areas/01` lines 5, 61, `areas/05:89`); a working opening exists — dev EAS simulator profile with mock + skip-auth `Travel App/eas.json` and deterministic boot to Trips `Travel App/app/index.tsx`.
**Evidence basis:** static/code (by definition — this item *is* the absence of runtime evidence).
**Fix direction:** Stand up and actually run the native mock-mode screenshot lane (iOS simulator dev build + Maestro `takeScreenshot`) against a seeded scenario pack with a fixed clock and fixed IDs (live/planning/completed/no-trip, private first-contact/long-reply/streaming, group vote pending, plan day with conflict, map fallback, memory story with missing photos, permission-denied, offline/error). Capture at SE-class + 390pt widths and large accessibility text. `make visual-qa` locally first, then a one-size smoke artifact in CI. Run it once now to convert this entire list from inferred to observed.
**Verification:** The lane producing the dogfood-critical screenshot set is itself the verification. Add a manual Accessibility Inspector pass before any internal release build.
**Fix category:** QA-process.
**Source reports:** `areas/01`, `05`, `06`, `07`, `09`, `10` (every report names the missing runtime).

---

## P2

### P2-1 — Motion is underspecified against the restrained doctrine
**Surface:** `components/voice/*`, `NavPills`, `TypingIndicator`, `ErrorBanner`, product-loading moments.
**User impact:** The voice sheet uses a spring (doctrine bans spring overshoot) and the orb pulses on a fixed 2.4s loop regardless of state, so presence/connecting/listening/live are visually indistinguishable. Generic `ActivityIndicator` still appears in product-defining moments (proposal detail, receipt OCR, chat "load earlier"), where doctrine wants anticipation. Reduce Motion is honored for Reanimated presets but not for RN `Animated` (NavPills, typing dots, voice orb, error banner), and there's no haptic opt-out despite Apple guidance that haptics be optional.
**Evidence:** spring + fixed pulse — `components/voice/VoiceOverlay.tsx:190-191`, `components/voice/VoiceOrb.tsx:16-31`; spinners in product moments — `components/trip/ProposalReviewSheet.tsx:302`, `components/expense/AddExpenseSheet.tsx:375`, `app/(tabs)/concierge/chat.tsx:873`; Reduce-Motion gaps — `utils/motion.ts:36`, `:76` vs `NavPills.tsx:68`, `TypingIndicator.tsx:41`, `ErrorBanner.tsx:27`. Doctrine — `Travel App/docs/Brand Identity.md:167`, `:173`, `:178`.
**Evidence basis:** static/code.
**Fix direction:** Write a small motion spec: map voice states (idle/connecting/live/closing/error) to orb pulse speed/intensity without spring overshoot; reserve `ActivityIndicator` for tiny inline utility only and use warm skeletons/reserved-slot/anticipation copy for proposal, OCR, and concierge-generated content; extend Reduce-Motion handling to RN `Animated`; add a central haptic flag.
**Verification:** Capture video (SE + large iPhone) of voice start/stop, proposal/OCR loading, tab switches with Reduce Motion on; confirm fade/no-motion fallbacks and visual feedback with haptics off.
**Fix category:** native behavior + visual design.
**Source report:** `areas/02`.

### P2-2 — The sheet system is fragmented
**Surface:** `ProposalReviewSheet`, `AddExpenseSheet`, `ShareStorySheet`, `FindPhotosSheet`, `ExperienceDetailSheet`, `RevertConflictSheet`.
**User impact:** Five+ sheets use different patterns (native `pageSheet`, custom absolute overlay, transparent bottom sheet) with different heights, handles, close affordances, and safe-area handling, so users can't predict whether a surface is swipe-, backdrop-, or button-dismissable. Proposal review can also open a second modal on top (`RevertConflictSheet`), and the organizer "revert change" applies immediately with no confirmation while the nested force-revert path *does* confirm — an inconsistent destructive flow. `ShareStorySheet` lacks `useSafeAreaInsets`, risking home-indicator collisions on its share/revoke actions.
**Evidence:** divergent patterns — `ProposalReviewSheet.tsx:286-292`, `FindPhotosSheet.tsx:306`, `:323`, `ExperienceDetailSheet.tsx:217-249`, `ShareStorySheet.tsx:235-245`, `AddExpenseSheet.tsx:355`, `:701`; immediate revert vs confirmed force-revert — `ProposalReviewSheet.tsx:237`, `:242`, `:777-785` vs `RevertConflictSheet.tsx:83`, `:92`; nested modal — `ProposalReviewSheet.tsx:443`, `RevertConflictSheet.tsx:42`; missing safe-area — `ShareStorySheet.tsx:530`.
**Evidence basis:** static/code.
**Fix direction:** Create a shared `AppSheet` taxonomy (`taskFullScreen`, `bottomForm`, `mediaPicker`, `detailSheet`) with consistent handle/close/height/backdrop/insets/accessibility containment; chat keyboard handling is the reference implementation to match. Add confirmation before immediate plan-changing reverts; avoid modal-on-modal except for native alerts/action sheets.
**Verification:** On iPhone + iPad: open each sheet type and confirm consistent dismissal; trigger the revert-conflict path and verify which layer closes and whether plan state changed; check `ShareStorySheet` clears the home indicator.
**Fix category:** native behavior.
**Source reports:** `areas/03`, `09`.

### P2-3 — Unvirtualized growth paths and a lazy-fetch flag misalignment
**Surface:** `app/(tabs)/trips/[tripId]/photos.tsx`, `app/(tabs)/discover/index.tsx`, `components/chat/ComposerBar.tsx`, heavy sheets.
**User impact:** Trip Photos renders every group and tile inside one `ScrollView`, so a real album mounts hundreds of `Animated.View`/`AppImage` wrappers at once, and grouping recomputes each render. Discover virtualizes only Friends/For-You; Angles, Events, Trending, Guides, and search map through `ScrollView` — fine on seed data, janky once the backend returns a richer index. A pill-index/lazy-fetch mismatch makes the visible Events tab wait on the wrong query while Trending warms early, so a tab can look blank. Image send base64-encodes every pending image before the optimistic bubble appears, so a multi-image send can feel frozen.
**Evidence:** photos ScrollView grid + per-render grouping — `photos.tsx:257`, `:281`, `:438-488`, `data/photos.ts:25-26`, `:162`; Discover unvirtualized maps — `discover/index.tsx:774`, `:977`, `:1394`, `:1440-1519`; flag misalignment — `:56`, `:391-397`, `data/discover.ts:458-513`; image-send conversion before bubble — `ComposerBar.tsx:48`, `:183`, `:211-237`. Existing good patterns to copy — `FindPhotosSheet.tsx:278-295`, `TripMapStopList.tsx:112-132`.
**Evidence basis:** static/code (no profiling captured).
**Fix direction:** Move Photos to a virtualized grouped grid (SectionList/FlashList) and memoize grouping; virtualize Discover Events/Angles before scaling volume; fix the active-pill→query mapping; add an explicit image-send "preparing" state or move conversion off the visible send path; split heavy sheets into memoized sections.
**Verification:** Seed 300 photos / 80 events / 80 angles / 20 days / 18 travelers; record JS frame time opening each screen; add render-count marks around `PhotoTile`, `FeedItemRenderer`, and major sheet sections.
**Fix category:** performance.
**Source report:** `areas/06`.

### P2-4 — Rich chat attachment cards lag the new substrate; group fleuron and purple drift
**Surface:** `components/chat/VenueCard.tsx`, `RecommendationBlock.tsx`, `MapCard.tsx`, `components/chat/group/VesperNote.tsx`, several purple call sites.
**User impact:** Private and group *prose* are now strong (`PrivateVesperNote`, group `VesperNote`), but the rich objects underneath still render as plain white utility cards, so Vesper's best recommendations visually collapse into generic chat attachments right after the prose lands. Two smaller brand erosions ride along: group chat draws a Unicode fleuron-like character instead of the locked custom SVG `Fleuron`, weakening one of the few proprietary marks; and purple — the sacred agent signal — leaks into non-agent decoration (a place-offer banner fallback, the Me profile avatar, trip-highlight placeholders, map route lines).
**Evidence:** plain attachment cards — `components/chat/VenueCard.tsx:46`, `:87`, `RecommendationBlock.tsx:43`, `:99`, `MapCard.tsx:93`, `:122`, `:146`; Unicode fleuron in group — `components/chat/group/VesperNote.tsx:66`, `:71` (correct SVG at `components/brand/Fleuron.tsx:26`, used right at `PrivateVesperNote.tsx:68`); purple leakage — `components/chat/ContentGraphBanner.tsx:36`, `app/(tabs)/me/index.tsx:138`, `:35`, `components/trip-map/TripMapCanvas.tsx:148`. Doctrine — `Travel App/docs/Design Language.md:84`, `:217`, `:228`.
**Evidence basis:** static/code.
**Fix direction:** Migrate attachment cards toward letterpress/editorial treatment (a shared `AgentObjectCard` for venue/booking/map/vote). Replace the group Unicode mark with the SVG `Fleuron` via one shared attribution line. Move non-agent purple fallbacks to lens colors / earth tones / espresso so purple only ever means "Vesper is present."
**Verification:** "Logo-off" test on chat attachments — do they still read as Vesper? Purple-audit pass: every purple pixel should answer "what is Vesper doing here?"
**Fix category:** visual design.
**Source reports:** `areas/08`, `07`.

### P2-5 — Private chat first-load shows generic bubble skeletons
**Surface:** `app/(tabs)/concierge/chat.tsx`, `components/ui/Skeleton.tsx`.
**User impact:** Private chat correctly routes AI turns to `PrivateVesperNote`, but initial history loading still renders `SkeletonMessage` bubble rows. The skeleton primitive is warm, but the bubble *shape* contradicts the envelope substrate and makes first-load private chat feel like ordinary messaging — during the exact moment the user is waiting on the core relationship.
**Evidence:** note routing — `app/(tabs)/concierge/chat.tsx:74-78`; bubble skeleton on load — `:886-890`; generic skeleton shape — `components/ui/Skeleton.tsx:174-178`, `:261-266`.
**Evidence basis:** static/code.
**Fix direction:** Add a private-chat skeleton shaped like `PrivateVesperNote` (hairline `+ VESPER` attribution + parchment prose lines), not bubbles. Bundles naturally with any further private-substrate work.
**Verification:** Screenshot private chat first-load vs a loaded thread; the loading state should read as an envelope, not a transcript.
**Fix category:** visual design + state coverage.
**Source report:** `areas/05`.

### P2-6 — Stale-data and permission recovery exist only on some surfaces
**Surface:** Discover, Expenses (stale data); Photos, mic (permission recovery).
**User impact:** Notifications has the right patterns — keep cached rows + an inline "Couldn't refresh, tap to retry" banner, and a persistent permission-denied panel. Discover and Expenses instead hide errors when cached data exists with no stale indicator, so users can't tell if recommendations/settlements are fresh. Photo and mic flows rely on a transient toast for recovery (mic uses an `Alert`, outside Vesper's calm state language), so after the toast disappears there's no visible path back — on high-emotion photo/voice moments.
**Evidence:** good stale pattern — `app/notifications/index.tsx:298-310`; masked stale errors — `data/discover.ts:575-581`, `app/trip-expenses/index.tsx:158`, `:164`; weak photo/mic recovery — `app/(tabs)/trips/[tripId]/photos.tsx:92-98`, `:346-371`, `components/voice/MicPrivacyDisclosure.tsx:119-127`; strong permission patterns to copy — Near Me `discover/index.tsx:874-892`, notifications `notifications/index.tsx:277-293`.
**Evidence basis:** static/code.
**Fix direction:** Add the shared `StaleBanner` (from P1-5) to Discover/Expenses; prefer persistent permission-denied panels for core photo/voice workflows, keeping toast actions for secondary affordances only.
**Verification:** Stale-refetch and permission-denied screenshots for Discover, Expenses, Photos, voice; confirm recovery remains visible after any toast.
**Fix category:** state coverage.
**Source report:** `areas/05`.

### P2-7 — Selected state is color-only and invisible to VoiceOver / color-blind users
**Surface:** `Chip`, `ReactionCard`, `VoteWidgetCard`, Discover filters.
**User impact:** Some primitives do this right (`NavPills` and `RadioOption` set `accessibilityState`), but `Chip`, reaction/vote cards, and Discover filters communicate selection through tint/border/text color alone — no `accessibilityState.selected` and no non-color mark — so the choice is ambiguous to VoiceOver and color-blind users on exactly the ≤5-second decision controls that are core to the product's interaction model.
**Evidence:** `Chip` selected not exposed — `components/ui/Chip.tsx:14`, `:31`, `:35`; reaction/vote color-only — `components/chat/ReactionCard.tsx:63-65`, `components/chat/VoteWidgetCard.tsx:122-124`; Discover filters — `discover/index.tsx:1297-1359`. Good patterns — `NavPills.tsx:40`, `:95`, `RadioOption.tsx:49-53`.
**Evidence basis:** static/code.
**Fix direction:** Give these controls `accessibilityState.selected` plus a non-color cue (checkmark, leading mark, or "Selected" in the accessible name). Fold into the primitive work.
**Verification:** A11y snapshot tests for selected chips/reactions/filters; VoiceOver pass on reaction and vote cards.
**Fix category:** visual design (a11y semantics).
**Source report:** `areas/10`.

### P2-8 — The Me tab still reads as a profile + library + settings dashboard
**Surface:** `app/(tabs)/me/index.tsx`, `components/me/TravelDNACard.tsx`.
**User impact:** Me has good trust primitives (Travel DNA is the most product-specific module), but after a trip the user's likely question — "what did Vesper learn, and how does it change the next trip?" — is diluted among a centered profile header, library rows, pastel placeholders, and stacked settings links. Once Travel DNA scrolls out of view, the screen could belong to many travel apps. (The prior round de-gamified Me; this is the remaining first-viewport hierarchy gap.)
**Evidence:** centered profile-dashboard header — `app/(tabs)/me/index.tsx:137`; broad "Library" grouping over stacked modules — `:195-200`, `:202-493`; generic highlight placeholders — `:238`; Travel DNA is one module among many — `components/me/TravelDNACard.tsx:75-113`.
**Evidence basis:** static/code.
**Fix direction:** Give Me one hero — lead with the user + one Travel DNA reflection + one "What Vesper knows" action; treat avatar/name as supporting metadata; group Library and Settings & trust into lower sections or routes; use a memory/journal visual for highlights instead of color rectangles.
**Verification:** First-viewport screenshot (SE / 15 / large text); pass if a reviewer names Me's primary job in five seconds and Travel DNA/memory is the focal point.
**Fix category:** visual design.
**Source reports:** `areas/01`, `07`, `08`.

### P2-9 — Honest-illustration vocabulary is too small for dogfood destinations
**Surface:** `utils/illustrationVariant.ts`, `components/brand/HonestIllustration.tsx`, `TripCard`, Discover, Story.
**User impact:** `TripCard` is the most unmistakably-Vesper surface, and the prior round made fallback selection destination-keyed — but the illustration set is still only `lisbon-dusk`, `brooklyn-brick`, and `generic-warm`. Any destination outside Lisbon/Brooklyn collapses to the same generic warm postcard, so a Tokyo or Oaxaca dogfood trip loses the "specific over generic" promise even though the *selection logic* is now correct.
**Evidence:** mapper only knows Lisbon/Brooklyn before `generic-warm` — `utils/illustrationVariant.ts:15`; only three variants ship — `components/brand/HonestIllustration.tsx:27` (`:22-25`); strong usage — `components/trip/TripCard.tsx:50`, `:103`, `:132`, `:163`.
**Evidence basis:** static/code.
**Fix direction:** Expand the curated/generated illustration vocabulary to cover the dogfood cities first (slug-keyed, labeled as illustration); reserve `generic-warm` for genuinely unknown destinations only. Seed real photography where available. Ties to the Trip Story hero fallback.
**Verification:** Destination-matrix render for `TripCard` (Lisbon / Brooklyn / Tokyo / Paris / Mexico City / unknown); confirm adjacent cards don't all collapse to the same art.
**Fix category:** visual design + content.
**Source reports:** `areas/01`, `08`.

---

## Cross-cutting investments

Most of the list collapses into a few moves; building these first makes the screen-specific work cheap and keeps it from regressing:

1. **Run the native screenshot QA lane** (P1-9). It is built; running it once converts every visual P1/P2 here from inferred to observed and is the gate that protects all the others. Do this first.
2. **`IconButton`-everywhere + `Tap minTarget` default** → P1-7, the touch-target tail of P1-2/P1-3, and the a11y-state work in P2-7.
3. **Shared `AppSheet` taxonomy** (`taskFullScreen`/`bottomForm`/`mediaPicker`/`detailSheet`) → P1-2 and P2-2.
4. **`StaleBanner`/`RefreshFailedBanner` + broad `useOfflineGate` adoption + an "imports `error` but renders no `ErrorState`" static check** → P1-5 and P2-6.
5. **Semantic token discipline** (promote meaningful `text.tertiary` → `metadata.default`; keep purple agent-only) → P1-8 and P2-4.
6. **A copy checklist + fixture lint** (no constraint attribution, no backend nouns) → P0-2, P1-6, and guards the privacy moat in mock data.
7. **`AgentObjectCard` + expanded illustration vocabulary** → P2-4, P2-9, and the Story hero fallback.

## Recommended sequencing for dogfood

- **Do first (so we stop flying blind):** P1-9. Run the lane against the seeded scenario pack — then re-grade every visual item against real screenshots.
- **Before dogfood (blockers + identity/trust):** P0-1, P0-2, P1-5, P1-6, P1-7. The two hard blockers, the failure-misreporting trust gaps, the language that says "software," and tappability — the things a tester *feels* in the first session.
- **Early in dogfood (native feel + cohesion):** P1-1, P1-2, P1-3, P1-4, P1-8. Discover's editorial job, native sheet/form behavior, the trip-workspace mental model, the proposal judgment surface, and accessibility-resilient text.
- **Opportunistic (as the relevant screen is touched):** all P2s — motion spec, sheet system, performance growth paths, attachment-card brand, envelope skeleton, stale/permission recovery, selected-state a11y, Me hierarchy, illustration vocabulary.

## External guidance referenced (preserved from area reports)

- [Apple HIG — Layout](https://developer.apple.com/design/human-interface-guidelines/layout) · [Typography](https://developer.apple.com/design/human-interface-guidelines/typography) · [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility) · [Color](https://developer.apple.com/design/human-interface-guidelines/color)
- [Apple HIG — Navigation](https://developer.apple.com/design/human-interface-guidelines/navigation) · [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars) · [Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets) · [Modality](https://developer.apple.com/design/human-interface-guidelines/modality)
- [Apple HIG — Virtual keyboards](https://developer.apple.com/design/human-interface-guidelines/virtual-keyboards) · [Entering data](https://developer.apple.com/design/human-interface-guidelines/entering-data) · [Text fields](https://developer.apple.com/design/human-interface-guidelines/text-fields) · [Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons) · [Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts)
- [Apple HIG — Playing haptics](https://developer.apple.com/design/human-interface-guidelines/playing-haptics) · [Motion](https://developer.apple.com/design/human-interface-guidelines/motion)
- [Material — Understanding motion](https://m2.material.io/design/motion/understanding-motion.html) · [Accessibility](https://m2.material.io/design/usability/accessibility.html)
- [WCAG 2.2 — Target Size Minimum](https://www.w3.org/TR/WCAG22/#target-size-minimum) · [Contrast Minimum](https://www.w3.org/TR/WCAG22/#contrast-minimum) · [Non-text Contrast](https://www.w3.org/TR/WCAG22/#non-text-contrast) · [Resize Text](https://www.w3.org/TR/WCAG22/#resize-text)
- [Maestro — takeScreenshot](https://docs.maestro.dev/api-reference/commands/takescreenshot) · [Expo — Web](https://docs.expo.dev/workflow/web/) · [Expo — Simulator builds](https://docs.expo.dev/build-reference/simulators)
