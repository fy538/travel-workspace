# Frontend Polish — Master Punch List

> Status: synthesis of the 10 area reports under `docs/audits/frontend-polish-2026-05/areas/`
> Created: 2026-05-24
> Scope: dogfood polish for `Travel App`. What would make the app feel less trustworthy, less premium, less native, or harder to use in the first week of internal use.
> Goal: not a redesign — a prioritized, buildable list that gets the app polished enough to dogfood.

## How to read this

- **Severity.** `P0` = a concrete dogfood-blocking *or* core-identity-blocking issue. `P1` = degrades trust/premium feel on a core surface in week one. `P2` = real polish/regression-prevention, not blocking.
- **Fix type.** `design-system` (fix once in a primitive/token, propagates), `screen-specific` (fix at the call site), `QA-process` (tooling/gates). Most P1s are design-system fixes precisely because the same defect repeats across screens.
- **Calibration note.** Each area report independently capped its findings at P1, scoped to its own lane. Synthesis elevates exactly one item to P0 — the private Vesper chat substrate — because three reports (`04`, `02`, `06`) converge on it, it contradicts a *locked* design decision, it is the product's signature surface, and the correct component already exists in group chat (so the fix is bounded, not speculative). Nothing else is inflated.

## Severity summary

| ID | Severity | Surface | One-line | Fix type |
|----|----------|---------|----------|----------|
| P0-1 | P0 | Private concierge chat | 1:1 Vesper renders as a generic purple bubble, not the locked envelope/prose substrate | design-system + screen-specific |
| P1-1 | P1 | Recommendation rendering | `why_for_person` has no UI-side guard against rendering in group context (trust-boundary footgun) | screen-specific |
| P1-2 | P1 | App-wide controls | No mechanical 44pt touch-target enforcement; many icon controls below the app's own floor | design-system |
| P1-3 | P1 | Cards everywhere | Generic white `Card` wins over editorial/letterpress; Vesper memory cards use sacred color but not sacred surface | design-system |
| P1-4 | P1 | Trip workspace | Over-chromed first viewport + two competing "Plan" surfaces (`index` vs `/plan`) | screen-specific |
| P1-5 | P1 | Discover + Me | Both read as accumulation dashboards; Me foregrounds gamified "profile % complete" | screen-specific |
| P1-6 | P1 | Color system | Purple no longer exclusive to Vesper (selection, live/today, categories, dots, profile, empties) | design-system + screen-specific |
| P1-7 | P1 | Editorial content | Reading content (curator takes, `why_for_you`, prose) rendered in caption/UI scale | design-system + screen-specific |
| P1-8 | P1 | Imagery | Trip cards reuse `lisbon-dusk` for every destination; Discover uses color blocks, not place imagery | design-system + screen-specific |
| P1-9 | P1 | QA process | No visual QA gate; Expo web boot is broken (missing `react-native-web`) | QA-process |
| P2-1 | P2 | Tokens | Raw `fontSize`/`borderRadius`/hex and local `StyleSheet` drift; duplicated `#F1EFFB` | design-system + QA-process |
| P2-2 | P2 | Contrast | `text.tertiary` (~2.5–2.8:1) carries real content (timestamps, badges, privacy copy) | design-system |
| P2-3 | P2 | Accessibility state | Missing/inconsistent `disabled`/`checked`/`selected`; raw `Pressable` bypasses `Tap` | design-system + screen-specific |
| P2-4 | P2 | Dynamic Type | Fixed dims + `numberOfLines` caps truncate long names under large text | screen-specific + QA-process |
| P2-5 | P2 | Empty/loading | Empty states generic + purple-by-default; skeletons read as generic gray blocks | design-system + screen-specific |
| P2-6 | P2 | Card hierarchy | Cards nested / over-framed (day wrapper + inner card, Tap-wrapped event cards) | screen-specific |
| P2-7 | P2 | Maintainability | 800–1800-line screen files concentrate local style decisions | screen-specific |
| P2-8 | P2 | Trip Story | Photo duplication via modulo indexing; no branded hero fallback when no photos | screen-specific |

---

## Resolution status (updated 2026-05-24)

All P0/P1/P2/P3 items were implemented on branch `frontend-polish-dogfood` across three commits, verified `tsc` 0 · jest 945 passed · `expo lint` 0 errors.

| ID | Status | Commit | Notes |
|----|--------|--------|-------|
| P0-1 | ✅ Fixed | `3a55dbe` | `PrivateVesperNote` envelope renderer + dispatcher |
| P1-1 | ✅ Fixed | `3a55dbe` | `RecommendationBlock` channel-aware, fail-closed to group |
| P1-2 | ✅ Fixed | `3a55dbe` | `IconButton` + `Tap minTarget` + `Button minHeight` + NavPills 44pt |
| P1-3 | ✅ Fixed | `3a55dbe` | `EditorialCard`/`ListRow`; Vesper cards on sacred surface |
| P1-4 | ◑ Partial | `3a55dbe` | Header→IconButton + Plan routing unified; **pill collapse deferred** → `TODO(polish P1-4)` (needs simulator) |
| P1-5 | ◑ Partial | `3a55dbe` | Me de-gamified + regrouped; **Discover tab reduction deferred** → `TODO(polish P1-5)` |
| P1-6 | ✅ Fixed | `3a55dbe`,`bf19e21` | semantic agent/state/category tokens; EmptyState neutral default; `#F1EFFB` centralized |
| P1-7 | ✅ Fixed | `3a55dbe`,`bf19e21` | editorial Fraunces type roles adopted |
| P1-8 | ✅ Fixed | `3a55dbe` | destination-keyed illustration |
| P1-9 | ◑ Built, unrun | `3a55dbe` | Maestro lane + scripts + runbook; **needs a simulator to run** |
| P2-1 | ✅ Fixed | `bf19e21` | spacing tokens + non-blocking raw-hex lint |
| P2-2 | ✅ Fixed | `bf19e21` | meaningful text → `metadata.default`; Button disabled tokens |
| P2-3 | ✅ Fixed | `bf19e21` | a11y states normalized; raw `Pressable` → `Tap` |
| P2-4 | ✅ Fixed | `bf19e21` | trust-carrying names wrap instead of clipping |
| P2-5 | ✅ Fixed | `bf19e21` | warm parchment skeletons; specific Discover empties |
| P2-6 | ◑ Partial | `bf19e21` | plan/event/sheet de-framed; **day-picker deferred** → `TODO(polish P2-6)` |
| P2-7 | ◑ Norm added | `bf19e21` | non-blocking `max-lines` warning; actual refactor deferred by design (opportunistic) |
| P2-8 | ✅ Fixed | `3a55dbe` | story photo de-dup + branded hero fallback |

**Deferred (all need the app running in a simulator to verify):** the trip-workspace pill collapse (P1-4), Discover tab reduction (P1-5), ExperienceDetailSheet day-picker (P2-6), running the visual-QA lane (P1-9), and the giant-file refactors (P2-7). All are marked `TODO(polish …)` in code.

A follow-up commit `2fd5f60` migrated 7 data-test suites to UUID trip ids (unrelated to this audit — required by the trip-scoped query guard in `0271c4d` — to keep the full suite green).

---

## P0

### P0-1 — Private Vesper chat renders as a generic chat bubble, not the locked envelope substrate
**Surface:** Concierge tab, private 1:1 (`app/(tabs)/concierge/chat.tsx`).
**User impact:** The concierge relationship *is* the product. In week one, the single most important surface reads like a generic chatbot transcript with a "Private" sticker rather than Vesper writing on the page. Long, candid, privacy-sensitive replies get squeezed into a small purple bubble — less calm, less trustworthy, less premium. This contradicts a decision the brand docs mark **locked**: "1:1 with Vesper = envelope" — prose on parchment, article-scale Fraunces, attribution outside any bubble (`Travel App/docs/Design Language.md:230-236`, `Travel App/docs/design-decisions/agent-chat.md:20-29`).
**Why it's P0 (not P1):** It is the core-identity surface, it violates a locked doctrine, and the correct component already exists — group chat ships `VesperNote` (attributed article-scale prose) via a dedicated dispatcher, while private chat still routes through the legacy `MessageBubble`. The architecture is inverted: the *secondary* surface is doctrine-aligned and the *primary* one is not.
**Evidence:**
- Private screen delegates every non-voice item to `MessageBubble` with `isPrivate` — `Travel App/app/(tabs)/concierge/chat.tsx:65-80`.
- AI text always uses the purple bubble + "Private" badge regardless of private/group — `Travel App/components/chat/MessageBubble.tsx:84-91`, `Travel App/components/chat/MessageBubble.tsx:99-127`, `Travel App/components/chat/MessageBubble.tsx:263-266`.
- Substantive prose uses `typography.body` markdown, not article-scale Fraunces — `Travel App/components/chat/MessageBubble.tsx:347-363`.
- The doctrine-aligned pattern already exists for group — `Travel App/components/chat/group/GroupThreadItem.tsx:84-182`, `Travel App/components/chat/group/VesperNote.tsx:110-148`.
**Fix direction:**
1. Add a `PrivateThreadItem` dispatcher; stop routing private Vesper through `MessageBubble`.
2. Add `PrivateVesperNote` modeled on group `VesperNote`: `+ VESPER` fleuron attribution, article-scale Fraunces prose on parchment, no purple bubble, no per-message "Private" badge.
3. Keep `MessageBubble` for the user's outgoing espresso bubble and compact system/send-failure states.
4. Render taxonomy: prose = candid coaching/planning/memory; note = quiet operational status; card = venue/booking/map/plan-change; inline action = call/reserve/accept-tweak-reject/retry.
5. Replace generic composer copy (`"Ask the Concierge..."`) with the locked string `"Tell Vesper anything — just you"` (`Travel App/docs/Brand Identity.md:230-235`) and add the first-contact opener for empty threads where substrate supports it (otherwise quiet presence).
**Verification:** Screenshot private chat at 390pt for first-contact, long candid reply, streaming at 1s/30s/complete, late venue attachment, send failure, offline, image attached. Side-by-side a private vs group thread — a new tester should understand the privacy boundary *without* reading the word "Private."
**Fix type:** design-system (new `PrivateVesperNote`) + screen-specific (chat dispatcher).
**Source reports:** `areas/04`, `areas/02`, `areas/06`.

---

## P1

### P1-1 — `why_for_person` has no UI-side guard against group rendering (trust-boundary footgun)
**Surface:** `RecommendationBlock` in both private and group threads.
**User impact:** `why_for_person` is private-only by doctrine and "never rendered in group context" (`Travel App/docs/Design Language.md:217-228`). The UI does not enforce this — `RecommendationBlock` renders the field whenever present, and group threads render `RecommendationBlock`. The backend currently omits it in group payloads, but a single mapper regression or bad payload would surface private rationale in the group room. Given the product's entire moat is "privacy is the product," this defense-in-depth gap is the highest-priority P1.
**Evidence:** `Travel App/components/chat/RecommendationBlock.tsx:21-29`, `Travel App/components/chat/RecommendationBlock.tsx:42-47`; group dispatch at `Travel App/components/chat/group/GroupThreadItem.tsx:152-156`, `Travel App/components/chat/group/GroupThreadItem.tsx:174-176`.
**Fix direction:** Make `RecommendationBlock` context-aware (`channel: 'private' | 'group'`). In group, defensively drop `why_for_person` even if the payload includes it. Pairs naturally with the P0-1 private/group split.
**Verification:** Add a fixture where `recommendation.why_for_person` is present in a group message; assert the group UI suppresses it. (Overlaps the separate privacy audit — fix the UI guard regardless of backend behavior.)
**Fix type:** screen-specific (defensive component guard).
**Source report:** `areas/04`.

### P1-2 — No mechanical 44pt touch-target enforcement
**Surface:** App-wide; concentrated in `TripHeader`, `NavPills`/segmented controls, chat composer, trip-home cards, and the Me data-editing screens.
**User impact:** `minTouchTarget 44pt` is documented as "Non-negotiable" (`Travel App/docs/Design Language.md:153-154`), but the primitives don't enforce it, so the floor is left to each call site and frequently missed. These are controls dogfooders hit constantly in week one; small, unevenly padded targets feel non-native and uncertain — and missed taps on *data-editing* controls (removing an allergy, a learned fact, a photo) feel trust-eroding, not just annoying. This is the most-cited issue in the audit (appears in 6 of 10 reports).
**Evidence:**
- `Tap` forwards styles to `Pressable` with no min size/hitSlop — `Travel App/components/ui/Tap.tsx:55-64`. `Button` sets no `minHeight` at any size — `Travel App/components/ui/Button.tsx:113-135`.
- `NavPills` trip cells `minHeight: 36` — `Travel App/components/ui/NavPills.tsx:202-209`.
- `TripHeader` icon controls: margin only, no box/hitSlop — `Travel App/components/trip/TripHeader.tsx:100-132`.
- `CardShell` dismiss 32×32 — `Travel App/components/trip-home/CardShell.tsx:94`, `:126`.
- Composer image remove 24×24 + 6pt slop (~36pt) — `Travel App/components/chat/ComposerBar.tsx:546-558`.
- `what-vesper-knows` dispute/remove 20–22pt — `Travel App/app/(tabs)/me/what-vesper-knows.tsx:394-433`; `constraints` add-chip 32×32 — `Travel App/app/(tabs)/me/constraints.tsx:381-385`; `TravelDNACard` dispute 22×22 — `Travel App/components/me/TravelDNACard.tsx:85`, `:154`.
**Fix direction:**
1. Add a canonical `IconButton`: requires `accessibilityLabel`, defaults to a 44×44 target, supports `selected`/`expanded`/`disabled`/`destructive`, centralizes haptics. Make it the only approved bare-icon control.
2. Add `Tap` `minTarget="auto" | "none"` (apply `hitSlop` to reach 44pt when visual size must stay small).
3. Give `Button` explicit `minHeight: a11y.minTouchTarget` per size.
4. Raise `NavPills`/segmented controls to a 44pt minimum via track padding, not by shrinking the hit area.
**Verification:** Unit tests on `Tap`/`Button`/`IconButton`/`NavPills` asserting min target or computed hitSlop. Dev-only overlay drawing 44pt bounds around every `Tap`/`IconButton`. VoiceOver + small-iPhone pass on the week-one loops (switch trip tabs, send/stop a message, remove a learned preference, add/remove a photo).
**Fix type:** design-system.
**Source reports:** `areas/03` (primary), `01`, `02`, `05`, `06`, `07`, `08`.

### P1-3 — Generic white `Card` wins over editorial/letterpress; Vesper memory cards use sacred color but not sacred surface
**Surface:** Discover, Concierge list, Me, chat attachment cards; `TravelDNACard`, `CrossTripThreadCard`.
**User impact:** ~14 distinct card families exist; only a few are product-defining. First-week users see the signature `TripCard`, then many adjacent modules look like ordinary mobile dashboard rows — weakening the "leather travel journal, not a SaaS dashboard" identity (`Travel App/docs/Design Language.md:55-64`). Worse, Vesper/AI memory cards apply purple *accents* to plain white cards instead of using the sacred surface, so purple reads as a tag on generic chrome rather than the agent's own material.
**Evidence:** generic primitive `components/ui/Card.tsx:15`; local white cards at `components/angles/AngleCard.tsx:100`, `components/chat/VenueCard.tsx:87`, `app/(tabs)/concierge/index.tsx:225`, `app/(tabs)/me/index.tsx:627`, `app/(tabs)/discover/index.tsx:1580`; purple-on-white memory cards at `components/me/TravelDNACard.tsx:74`, `:113` and `components/trip-home/CrossTripThreadCard.tsx:49`, `:96`. The better pattern already exists: `components/trip-home/CardShell.tsx:17` (sacred-tint) and `LetterpressCard`.
**Fix direction:** Establish and enforce a card taxonomy before dogfood: `EditorialCard`/`LetterpressCard` (Vesper-authored, trip identity/memory, place theses, Travel DNA, cross-trip threads), `ActionModule` (decisions/votes/prompts/nudges — `CardShell`), `UtilityPanel` (settings/forms — plain `Card` allowed here only), `ListRow` (conversation/search/saved-venue rows, 44pt min height), `MediaCard` (postcards/destinations — must have real or honest-illustration imagery). Migrate `TravelDNACard` + `CrossTripThreadCard` to `LetterpressCard`/an editorial-memory card. Re-document `Card` as utility-only.
**Verification:** A "surface zoo" screen rendering every taxonomy primitive in default/pressed/disabled/loading/error. Lint/review rule: fail new `colors.white + cardRadius + hairline border` outside `Card`/approved row primitives. Review checklist: every new card declares one taxonomy role + one primary action.
**Fix type:** design-system.
**Source report:** `areas/06` (+ README finding 1).

### P1-4 — Trip workspace is over-chromed, and "Plan" is split across two surfaces
**Surface:** `app/(tabs)/trips/[tripId]/` (layout, index, plan), `TripHeader`.
**User impact:** Entering a trip stacks global bottom tabs + sticky `TripHeader` (back, trip switcher, avatar stack, settings) + a second row of nav pills before any trip content. The first viewport reads as a project-management tool, not "entering a trip" — against the "Silence is a design decision"/minimal-chrome doctrine (`Travel App/docs/Design Language.md:37`, `:57`). Separately, both `index.tsx` and a distinct `/plan` route behave plan-like, and different controls route to different destinations, so users land in different "Plan" mental models depending on which control they tapped.
**Evidence:** global tabs `app/(tabs)/_layout.tsx:52`; header before stack `app/(tabs)/trips/[tripId]/_layout.tsx:72`; header rows `components/trip/TripHeader.tsx:97-147`; dual routes `utils/routes.ts:13-15` vs `:23-28`; header Plan pill → index while anchor/empty-state → `/plan` (`components/trip-home/ConciergeAttentionSection.tsx:525-528`, `app/(tabs)/trips/[tripId]/index.tsx:400-407`). The Plan landing file itself notes the header pills are redundant (`app/(tabs)/trips/[tripId]/index.tsx:4-20`).
**Fix direction:** Make the trip index the canonical "Trip home / Plan workspace"; reserve `/plan` for a clearly-named timeline view or fold it in. Collapse the header after first scroll; keep trip title as context, move settings/activity/members into one trip-info sheet, let native back carry return navigation. Demote Chat/Map/Photos/Memory from equal persistent pills to contextual actions. Convert repeated low-frequency controls (per-block "Suggest a change", per-card dismiss) to revealed/row/overflow actions.
**Verification:** Screenshot trip-home first viewport on iPhone SE / 15 / large Dynamic Type; count controls before the first trip-specific content line. Dogfood script: "open a live trip, find tonight's plan, inspect the route, add a photo, return to the plan" — count taps and note where two nav systems offer the same destination.
**Fix type:** screen-specific.
**Source reports:** `areas/05` (primary), `01`.

### P1-5 — Discover and Me read as accumulation dashboards; Me foregrounds gamified profile completion
**Surface:** `app/(tabs)/discover/index.tsx`, `app/(tabs)/me/index.tsx`.
**User impact:** Discover exposes six peer modes (Angles/Friends/For you/Events/Trending/Guides) under a sticky search bar *before* Vesper expresses an opinion — a browse console, not an opinionated index. Me stacks profile, Travel DNA, an insight CTA, **pending votes (active trip work)**, memory, highlights, people, social activity, saved venues, voice logs, and settings in one scroll. Most damaging: Me shows `Profile {x}% complete` — the exact gamification the brand brief bans (`Travel App/docs/Brand Identity.md:48-55`). Both tabs feel accumulated rather than authored.
**Evidence:** six pills + comment that only Angles is graph-backed `app/(tabs)/discover/index.tsx:53-56`; control-led first viewport `:675-699`, `:754-805`, `:897-943`; Events filter stack `:1227-1347`. Me completion copy `app/(tabs)/me/index.tsx:151-163`, `:194-205`; one-wall layout `:145-237`, `:239-523`; pending votes in Me `:232-237`.
**Fix direction:** Discover — lead with the place and one opinionated module (the thing worth noticing now / one featured angle + 1–2 exemplar venues); demote search to a compact affordance; reduce first-order nav to primary + one contextual mode; push Friends/Trending/Guides below the fold; move Events behind a "Tonight/dates" module. Me — lead with the user + one Travel DNA reflection + one "What Vesper knows" action; **remove the completion percentage**; move pending votes to Trips/Concierge; group Library (highlights/memory/saved/voice/people) and Settings & trust (privacy/account/delegation/feedback) into lower sections or routes.
**Verification:** First-viewport screenshot review (SE / 15 / large text). Pass condition: a reviewer states each tab's primary job in five seconds. Manually dogfood first-week taps — if Discover opens mostly into search/events/filters, the editorial job isn't landing.
**Fix type:** screen-specific.
**Source report:** `areas/07` (+ README finding 8).

### P1-6 — Purple is no longer exclusive to Vesper presence
**Surface:** `EmptyState`, Me profile, expense sheets/rows, plan/map dots, trip-log/plan-day status.
**User impact:** Purple is the product's single most important signal — "Seeing purple = the AI is doing something." It's currently also used for empty-state icons, profile decoration, selected form chips, the expense "activity" category, plan/map activity dots, and live/today state. In week one users learn purple means five different things, so the concierge presence stops feeling sacred and the app feels less premium.
**Evidence:** purple-by-default empties `components/ui/EmptyState.tsx:23`, `:27`, `:51`; profile purple `app/(tabs)/me/index.tsx:148`, `:549`; expense selection/category `components/expense/AddExpenseSheet.tsx:542`, `:555`, `components/expense/ExpenseRow.tsx:28`, `:31`; plan/map dots `components/trip-plan/PlanBlockRow.tsx:158`, `components/trip-map/mapStopDisplay.ts:27`; live/today → purple `components/memory/TripLogCard.tsx:45-47`, `components/trip-plan/PlanDaySection.tsx:27`, `:38`, `:115` (canonical mapping says `live` → olive: `Travel App/docs/Design Language.md:110`).
**Fix direction:** Introduce source-aware semantic roles rather than new palette colors: `agent.surface/accent/action/attribution`, `state.live/planning/booked/focus/selected`, `category.*` (earth tones only), `metadata.*`. Keep purple for Vesper attribution/asks/private substrate/voice/agent-generated pending work; replace selection purple with espresso/action, live/today with olive/ink-focus, categories with earth tones; make `EmptyState` neutral by default with opt-in `tone="agent"`.
**Verification:** Purple-audit script listing every `colors.purple`/`tone="purple"`/raw-purple site, each classified `agent-presence | agent-memory | selection | category | temporal | profile | unknown`. Visual review of Me/expense/plan-day/trip-log/empties: "Does purple only mean Vesper is present?"
**Fix type:** design-system (tokens) + screen-specific (call-site swaps).
**Source report:** `areas/09`.

### P1-7 — Reading content is rendered in caption/UI scale instead of article scale
**Surface:** trip-home cards, Discover search/Near-Me/masonry, private chat prose (overlaps P0-1).
**User impact:** Curator takes, `why_for_you`, brief signals, and search snippets — content meant to feel specific, trusted, and worth reading — are styled as 12–13pt dense UI labels, so they read like metadata. This weakens the editorial travel-journal identity even where the underlying content is good. The two-scale system exists in tokens (`Travel App/constants/typography.ts:112-145`) and doctrine ("if the surface is a place to read, use article scale" — `Travel App/docs/Design Language.md:120-131`); local usage just doesn't reach for it.
**Evidence:** `components/trip-home/HomeCardBody.tsx:148`, `:155` (12–13pt editorial); `components/trip-home/HappeningCard.tsx:29`, `ConstraintMealCard.tsx:31` (care copy through compact subtitle); Discover curator headlines as caption `app/(tabs)/discover/index.tsx:1195`, `:1689`, `:1816`.
**Fix direction:** Add named editorial tokens (`editorialSnippet`, `homeCardSubtitle`, `homeCardTitle`) and promote reading content out of caption scale; use article scale for longer prose. Bundle with P0-1's `PrivateVesperNote`.
**Verification:** Static check for raw `fontSize`/`fontFamily`/`numberOfLines` in trip-home, Discover, chat. Screenshot trip-home attention cards, Discover search/Near-Me, and private chat at default/Large/Accessibility-Large text on a narrow viewport.
**Fix type:** design-system (tokens) + screen-specific.
**Source report:** `areas/02`.

### P1-8 — Trip cards reuse Lisbon fallback art for every destination; Discover uses color blocks, not place imagery
**Surface:** `TripCard` (all non-memory trips), Discover Trending/Guides/For-You/friend cards.
**User impact:** A Tokyo or Oaxaca dogfood trip renders with Lisbon rooftops — "honest illustration" becomes dishonest, which reads as fake. Discover, the place-aware browse surface, mostly renders gradients/dots/generic icons, so it has place *names* but little visual proof of place. This is exactly where week-one testers expect Vesper to know the place (`Travel App/docs/Brand Identity.md:193-203`).
**Evidence:** hard-coded `variant="lisbon-dusk"` in compact + postcard cards `components/trip/TripCard.tsx:95-102`, `:123-132`; only three illustration variants exist `components/brand/HonestIllustration.tsx:22-25`; Trending/Guides render `backgroundColor: dest.gradient[0]` `app/(tabs)/discover/index.tsx:1407-1422`, `:1494-1517`; data models carry only gradient, not `image_url` `types/discover.ts:27-49`.
**Fix direction:** Destination-keyed fallback selection (Lisbon→Lisbon, Brooklyn→Brooklyn, unknown→generic labeled illustration, never Lisbon). Three-tier ladder: real/curated photo → curated/generated destination art keyed by slug (labeled as illustration) → algorithmic color only for low-salience utility rows. Add a `visual_status` field; require destination cards to carry `image_url` or `fallback_art_key`. Seed real imagery for the dogfood cities first.
**Verification:** Unit tests for fallback selection by destination. Visual audit flagging repeated identical fallback art in one viewport. Static check for `variant="lisbon-dusk"` outside Lisbon mocks/tests. Screenshot Trips/Discover/Story across Lisbon/Tokyo/Oaxaca/"no destination."
**Fix type:** design-system (selection logic) + screen-specific + content seeding.
**Source report:** `areas/08`.

### P1-9 — No visual QA gate exists; Expo web boot is broken
**Surface:** Engineering process (`package.json`, CI, `eas.json`).
**User impact:** Type/test posture is strong but cannot catch typography regressions, cramped small-device layouts, private/group substrate drift, or touch-target misses — all of which can merge green. This is the regression risk that lets every other item in this list quietly come back. It also contradicts the project's own "the screen is the eval" doctrine (`Travel App/docs/Design Workflow.md:7-18`).
**Evidence:** no screenshot/visual command in app or workspace gates `Travel App/package.json:5-24`, `Makefile:37-76`, `Travel App/.github/workflows/ci.yml:17-105`; Expo web missing `react-native-web`/`@expo/metro-runtime` `Travel App/package.json:58-82` (README records the failed boot at `docs/audits/frontend-polish-2026-05/README.md:50`). A working opening exists: dev EAS simulator profile with mock+skip-auth `Travel App/eas.json:7-19`, deterministic boot to Trips `Travel App/app/index.tsx:18-24`.
**Fix direction:** Add a native mock-mode screenshot lane first (iOS simulator dev build + Maestro `takeScreenshot`), driven by stable selectors. Seed a `visual-qa` scenario pack with fixed clock + fixed IDs (live/planning/completed/no-trip, private first-contact/long-reply/streaming, group vote pending, plan day with conflict, map fallback, memory story w/ missing photos, permissions, offline/error). Add Expo web second as a review accelerator (after native-only fallbacks are explicit), not the canonical gate. `make visual-qa` local first, then a one-size `visual-qa-smoke` CI artifact upload.
**Verification:** Capture the dogfood-critical screens (Trips, trip workspace, Concierge private states, Discover, Me, system/permission states) at SE-class + 390pt widths and large accessibility text. Manual a11y pass (Accessibility Inspector) before any internal release build.
**Fix type:** QA-process.
**Source report:** `areas/10`.

---

## P2

### P2-1 — Raw values bypass tokens; duplicated sacred-purple literal
**Surface:** App-wide (heaviest in Discover, chat, Me, `TripCard`).
**User impact:** The app looks assembled from adjacent-but-not-identical surfaces. Static scans found 439 raw `fontSize`, 96 raw `borderRadius`, 48 raw hex (README finding 4), plus `headerHeight + 8` offsets and a duplicated `#F1EFFB` sacred background in two files.
**Evidence:** `app/(tabs)/discover/index.tsx:750`, `:1058`, `:1117` (`headerHeight + 8`); `app/(tabs)/concierge/chat.tsx:970`, `:1019` (raw gap/radius); `TripCard.tsx:261` (raw display style); duplicated `#F1EFFB` at `components/plan/PendingPromptCard.tsx:64` and `components/trip-home/CardShell.tsx:49`.
**Fix direction:** Add the missing semantic tokens (`metadata`, `timestamp`, `actionLabel`, `sectionLabel`, `agent.surface`, `chromeGap`, `sectionStackGap`, `timelineKeyline`) so call sites have a named role to reach for; then add a static check failing raw `fontSize`/`borderRadius`/hex in `app/**` and `components/**` with comment-based exceptions for illustrations/photos.
**Verification:** Lint rule + allowlist for SVG/photo files. Re-run the raw-value scan to confirm it trends down.
**Fix type:** design-system + QA-process.
**Source reports:** `areas/01`, `02`, `09`.

### P2-2 — Low-contrast tertiary text carries real content
**Surface:** timestamps, badges, research badges, privacy/consent copy, Discover snippets.
**User impact:** `text.tertiary` `#9C9A90` is ~2.82:1 on white and ~2.39:1 on canvas — below the 4.5:1 small-text guidance — yet it carries meaningful content, including a lazy-research ok/failed verification cue and contract-level privacy copy. Reads as the app hiding useful specifics.
**Evidence:** token `constants/colors.ts:49`, `:52`; timestamps `components/chat/MessageBubble.tsx:336-338`; research badge on tertiary bg `components/chat/LazyResearchBadge.tsx:52-63`; consent copy `components/trip/GroupAndLearnConsentSheet.tsx:263-272`.
**Fix direction:** Treat `text.tertiary` as decorative-only; add a stronger `metadata.default` passing 4.5:1 on parchment/white for timestamps/badges that carry meaning. Avoid global 0.5 opacity for disabled buttons — use explicit disabled foreground/background tokens.
**Verification:** Contrast tests for every text token on `background.primary`/`secondary`/`canvas`, with a decorative allowlist. Snapshot disabled buttons/timestamps/badges in Increased Contrast mode.
**Fix type:** design-system.
**Source report:** `areas/09`.

### P2-3 — Accessibility state missing/inconsistent; raw `Pressable` bypasses `Tap`
**Surface:** composer, constraints/privacy switches, delegation/radio options, Photos/Memory tiles.
**User impact:** VoiceOver users get an unpredictable contract: composer camera/send don't expose `disabled`, privacy switches don't expose `checked`, and radio-like controls use `selected` in one place and `checked` in another. Raw `Pressable` in Photos/Memory gives less press confirmation than nearby `Tap` controls.
**Evidence:** composer disabled state missing `components/chat/ComposerBar.tsx:333-409`; switch checked missing `app/(tabs)/me/constraints.tsx:322-328`; radio convention mismatch `components/ui/RadioOption.tsx:40-52` vs `app/(tabs)/me/delegation.tsx:92-99`; raw `Pressable` `app/(tabs)/trips/[tripId]/memory.tsx:143-154`, `photos.tsx:470-495`.
**Fix direction:** Normalize a11y states (switches expose `checked`, disabled `Tap` exposes disabled, selected filters use tab/radio semantics consistently). Replace raw `Pressable` with `Tap` or an explicit no-haptic `Tap` variant that still gives pressed visuals. Fold the radio convention into the `IconButton`/primitive work from P1-2.
**Verification:** A11y snapshot tests for composer disabled, switch checked, selected segmented controls. VoiceOver pass on trip workspace, composer, Discover filters, "What I know about you."
**Fix type:** design-system + screen-specific.
**Source report:** `areas/03`.

### P2-4 — Dynamic Type fragility
**Surface:** `TripCard`, trip-home cards, Discover masonry, Me saved-venue chips.
**User impact:** Fixed card dimensions + `numberOfLines` caps + non-shrinking CTAs mean long city/venue/trip names clip or crowd under larger accessibility text; even at default size, aggressive truncation hides specifics.
**Evidence:** compact title 1 line beside fixed 92pt photo `TripCard.tsx:105`; absolute hero title at fixed 30/32 `TripCard.tsx:130-145`, `:261`; capped title beside `flexShrink:0` CTA `trip-home/HomeCardBody.tsx:75-82`, `:122`; saved-venue 1-line in 160pt chip `me/index.tsx:409`, `:616`.
**Fix direction:** Let trust-carrying text (destination/venue/trip names, curator hooks) wrap or expose full text on the next tap; avoid fixed heights where content must scale.
**Verification:** Long-name fixtures (city/trip/venue/CTA). Screenshot at default/Large/Accessibility-Large on a narrow viewport. (Capture covered by P1-9's matrix.)
**Fix type:** screen-specific + QA-process.
**Source report:** `areas/02`.

### P2-5 — Empty states and skeletons read as generic, not brand-native
**Surface:** shared `EmptyState`, Discover empties, trip-home/memory loading.
**User impact:** `EmptyState` is a generic icon+title+subtitle that renders purple by default (conflicting with P1-6), and Discover has "No…"/"Nothing…" empties with no specificity — against "empty states must teach or delight" (`Travel App/docs/Design Language.md:32-35`). Skeletons are anonymous gray blocks, which doctrine explicitly bans in favor of anticipation copy / the reserved-slot pattern (`:253-261`, `:315-329`).
**Evidence:** purple-default empties `components/ui/EmptyState.tsx:25-58`; generic Discover copy `app/(tabs)/discover/index.tsx:859-863`, `:1349-1355`, `:1468-1481`; generic skeletons `components/ui/Skeleton.tsx:1-21`, `trip-home/ConciergeAttentionSection.tsx:460-493`, `memory.tsx:74-85`.
**Fix direction:** Give `EmptyState` a contextual `visual` slot + `tone` (purple opt-in only for Vesper-authored states); add minimum 44pt CTA height. Replace high-salience skeletons with warm, surface-tinted anticipation placeholders / reserved-slot.
**Verification:** Screenshot empties for no-data/failed/no-permission/limited-photos/no-destination. Assert empty/retry CTAs meet 44pt.
**Fix type:** design-system + screen-specific.
**Source report:** `areas/08`.

### P2-6 — Cards nested / over-framed
**Surface:** plan day sections, Discover event cards, sheet subpanels.
**User impact:** Card-in-card framing makes hierarchy noisy and admin-like, especially in itinerary/event flows that need calm hierarchy.
**Evidence:** day wrapper + inner `Card` `app/(tabs)/trips/[tripId]/plan.tsx:260`, `:285`, `:447`; event `Tap` wrapping a full `EventCard` `app/(tabs)/discover/index.tsx:1358`, `:1365`; card-in-sheet `components/discover/ExperienceDetailSheet.tsx:357`, `:615`, `:685`.
**Fix direction:** Prefer dividers/full-width sections over card-in-card; merge the touch layer into the visible card. Covered by the P1-3 taxonomy (`SheetSection` role).
**Verification:** Surface-zoo review; design-review rule against >1 level of card framing.
**Fix type:** screen-specific.
**Source report:** `areas/06`.

### P2-7 — Large screen files concentrate local style decisions
**Surface:** `discover/index.tsx` (1824), `concierge/chat.tsx` (1042), `ProposalReviewSheet.tsx` (1049), `AddExpenseSheet.tsx` (885), `me/index.tsx` (632).
**User impact:** Not user-visible directly, but these files are where local spacing/typography/card drift accumulates — they make every other fix here harder to land and keep landed.
**Fix direction:** Refactor into screen shell + named sections + focused hooks as each screen is touched for the items above (don't refactor for its own sake). Adopt a "no new 800+ line screen file without justification" review norm.
**Verification:** File-size trend in review; sections extracted as part of P1-4/P1-5 work.
**Fix type:** screen-specific.
**Source report:** README finding 3.

### P2-8 — Trip Story photo duplication; no branded hero fallback
**Surface:** `app/(tabs)/trips/[tripId]/story.tsx`, `components/memory/`.
**User impact:** One of the strongest memory surfaces can repeat the same photo across unrelated narrative slots (modulo indexing) when slots outnumber photos, and the hero simply omits imagery when there are no photos instead of a branded destination-aware fallback.
**Evidence:** modulo auto-fill `story.tsx:96-114`; hero only renders with `heroImageUrl` `components/memory/TripStoryHero.tsx:23-34`; dashed camera prompt instead of place-aware fallback `components/memory/PhotoSlotCard.tsx:109-121`.
**Fix direction:** De-duplicate slot assignment (no repeats until the pool is exhausted); render an honest destination-keyed illustration in the hero when no photos exist (ties to P1-8).
**Verification:** Story screenshots with 0/1/2/many photos; assert no repeated image within a viewport.
**Fix type:** screen-specific.
**Source report:** `areas/08`.

---

## Cross-cutting design-system investments

Most of the P1s collapse into a small set of primitives. Building these first makes the screen-specific fixes cheap and keeps them from regressing:

1. **`IconButton` + `Tap` `minTarget` + `Button` `minHeight`** → resolves P1-2, most of P2-3, and the touch-target tail of P1-4/P1-5/P2-5.
2. **Card taxonomy** (`EditorialCard`/`ActionModule`/`UtilityPanel`/`ListRow`/`MediaCard`/`SheetSection`) → resolves P1-3, P2-6.
3. **Semantic token additions** (agent/state/category/metadata roles + editorial type roles) → resolves P1-6, P1-7, P2-1, P2-2.
4. **`PrivateVesperNote` + private dispatcher** (mirroring the existing group `VesperNote`) → resolves P0-1 and the private half of P1-1 and P1-7.
5. **Destination-keyed honest-illustration selection** → resolves P1-8 and P2-8.
6. **Native screenshot QA lane + scenario pack** → resolves P1-9 and provides the verification surface for everything else.

## Recommended sequencing for dogfood

- **Before dogfood (identity + trust):** P0-1, P1-1, P1-2, P1-6, P1-8. These are the items a tester *feels* in the first session — the concierge surface, privacy boundary, tappability, the purple signal, and "does it know the place."
- **Early in dogfood (cohesion):** P1-3, P1-4, P1-5, P1-7. Workspace calm, card cohesion, editorial scale, IA — the difference between "works" and "premium."
- **Alongside, as a gate:** P1-9, then the P2 token/contrast/a11y cleanup (P2-1, P2-2, P2-3) ride on the primitives above and get protected by the screenshot lane.
- **Opportunistic:** P2-4, P2-5, P2-6, P2-7, P2-8 — fix as the relevant screens are touched for the items above.

## External guidance referenced (preserved from area reports)

- [Apple HIG — Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility) (44×44 pt default control size)
- [Apple HIG — Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons)
- [Apple HIG — Layout](https://developer.apple.com/design/human-interface-guidelines/layout) · [Typography](https://developer.apple.com/design/human-interface-guidelines/typography) · [Color](https://developer.apple.com/design/human-interface-guidelines/color) · [Designing for iOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-ios) · [Images](https://developer.apple.com/design/human-interface-guidelines/images)
- [Material — Accessibility](https://m2.material.io/design/usability/accessibility.html) (48×48 dp) · [Layout](https://m2.material.io/design/layout/understanding-layout.html) · [Cards](https://m2.material.io/components/cards)
- [WCAG 2.2 — Target Size Minimum](https://www.w3.org/TR/WCAG22/#target-size-minimum) (24×24 CSS px floor) · [Resize Text](https://www.w3.org/TR/WCAG22/#resize-text)
- [React Native — Accessibility](https://reactnative.dev/docs/accessibility)
- [Expo — Web](https://docs.expo.dev/workflow/web/) · [Simulator builds](https://docs.expo.dev/build-reference/simulators) · [Maestro — takeScreenshot](https://docs.maestro.dev/api-reference/commands/takescreenshot)
- [IBM — Progressive disclosure](https://www.ibm.com/docs/en/technical-content?topic=practices-progressive-disclosure) · [Airbnb photo tour](https://www.airbnb.com/help/article/477) · [Condé Nast Traveler destinations](https://www.cntraveler.com/destinations)
