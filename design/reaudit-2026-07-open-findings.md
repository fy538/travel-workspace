# Open findings — zero-trust re-audit campaign (2026-07-11)

Every unresolved finding from Waves 0–3 + the handoff-135 re-check, pulled out of `design/surface-manifest.yaml`'s per-row `notes:` fields into one prioritized list. Source of truth is still the manifest — this doc is a synthesis for planning, not a replacement. File:line citations are preserved where the original audit gave one; re-verify before acting, since code keeps moving.

**Already fixed and independently re-verified** (do not re-open — checked against actual current code, not just claim text, on 2026-07-11): Row System's failed-booking halo bug; Buttons' `ghost` variant border; Cards kit's Trust spine color; Trip Settings' ungated Vesper-autonomy permissions; Places' `PlaceHome` naming collision (D23); Voice registers' D8 mechanical follow-ups (6 sites); Voice's purple→amber/gold + `MicPrivacyDisclosure` copy narrowing (D24); People & Collaboration's pending-invite `MemberActionSheet`; Universal Search's saved-venue provenance, 4-chip scope rail, and empty-state sections; and **Trip Story in full** — all 8 P1 items (place chips, landing/card brand pass, Trip-group visibility, owner attribution, ShareLink lifecycle, analytics funnel, Plan Similar resume, `MemoryStoryHeader` fork) — now `status: aligned`. See git log in `travel-app`/`travel-agent` for commits; `design/surface-manifest.yaml` has full per-claim verification notes.

**One claim in circulation was checked and found FALSE**: Universal Search's "Actions group re-enabled" (see P1 below) — the frontend routing was updated but the backend never wires a route, so action rows are still fully non-tappable in the shipped app.

---

## P0 — Security

- **Trip Settings & Admin — RESOLVED same session.** ~~permissions.tsx's Vesper agency-mode/threshold controls had zero `isOrganizer` check~~ — fixed, `travel-app` commit `b55f42e3`. Listed here only so it isn't re-discovered as new.

No other P0s found.

---

## P1 — Structural (breaks a real user-facing promise)

Trip Story's 8 items are fully resolved (see the summary above) — the surface is dropped from this list entirely, `status: aligned`.

### Voice — live mic / voice chat (`status: partial`, handoff 137 D24)
- D24 carve-out: bottom-sheet `VoiceOverlay` blessed as v1; full-screen Calm Listening + hold-to-talk **deferred, not cancelled** — this is the correct, intended state, not a gap.
- `useVoiceSession`'s `_connectToRoom` is a documented no-op stub — intentionally not enabling real audio yet (`VOICE_ENABLED` stays off).
- `useNarrationWithInterruption` still has zero production callers.
- (Color + disclosure-copy fixes verified done — see summary above.)

### Universal Search
- **The "Actions group" is still NOT navigable, despite a claim to the contrary in circulation.** `routeForUniversalItem`'s frontend logic was updated to interpret a route hint (`routeFromHint`), but `backend/search/dispatch.py`'s `_action_items()` (line ~655) still hardcodes `route=None` unconditionally — every other result-group builder in the same file (trips/places/atlas/conversations/receipts/costs/people, 7 of 8) populates a real route string; only Actions doesn't. The FE gates `disabled={!href}` purely on that field, so action rows are still fully non-tappable in the shipped app. This is a one-function backend fix (thread `action_type`/`target_id` into a `route=` string, matching the pattern the other 7 builders already use) — mechanical, not a design question; D25 already ruled what the UX should be.
- (Saved-venue provenance, the 4-chip scope rail, and the empty-state sections verified done — see summary above.)

### Saved & Collections System
- Trip-relevance state grammar (In plan / Stale / Unavailable) is fully built in the row component, but the screen's data-mapping function never sets the `state` field at all — structurally unreachable, not just unstyled.
- Save-date/recency is dead on both ends (type has the field, mapper hardcodes `null`).
- `provenance` — meant to hold "Saved from Guide: X" attribution — is populated with generic venue marketing copy (`curator_hook`) instead. Live content-integrity risk: the field's name promises something it doesn't contain.

### Photo & Media Intake
- The destructive "Remove from trip" deletion canon specs is UI-present but never wired — the component's own `onRemove` prop is silently only ever used for "make private," and **no delete API exists anywhere in the codebase**. Real removal is currently impossible, not just unwired.
- "Ask Vesper about this photo" and "Hide from my view" actions are specced but dead/absent.
- Signature day/time/place candidate clustering doesn't exist in the main find-photos flow (flat 3-col grid instead).
- Retag is owner-gated where canon grants it to any member on read-only photos.
- AI-suggested story-slot state (`suggested`) is unreachable end-to-end — the data type doesn't carry it.

### Trip Settings & Admin (remainder, beyond the fixed security item)
- "Cancel trip" doesn't exist anywhere in the codebase (only Delete/Archive) — the sole-organizer leave guard is even missing its canon-specified "Cancel trip instead" escape hatch as a direct consequence.
- Delete's typed-confirmation phrase diverges from spec on two axes: canon wants the literal word "delete" typed, code requires the exact trip name; canon marks the draft-delete path as untyped, code requires typing "delete" there too.
- The same "change Vesper autonomy" canon rule is now wrong in **two more places** beyond the fixed permissions.tsx bug: `GroupAgencySheet.tsx` uses Ask where canon specifies no-Ask (opposite direction of the fixed bug) — needs a shared gating primitive, not three hand-rolled checks.

### State System (family)
- ~~`ErrorState` vs `StateScreen(tone='failure')` dual kits~~ — **RESOLVED 2026-07-12 (PR-S1 #78):** `ErrorState` is a thin wrapper around `StateScreen tone="failure"`; `hard-failure-kit` ratchet in CI. Discover cold-start + InlineAbsence still open.
- Discover's cold-start chip-picker ("Tell Vesper what you're drawn to" + interest chips) has zero code counterpart — collapses into a generic empty state.
- The reader's sparse-section `InlineAbsence` panel has zero code counterpart.

---

## P2 — Real, scoped (a missing feature/value/border, contained blast radius)

**Auth and Invite**
- OTP wrong-code/expired inline visual states are fully built (`OtpCodeInput.tsx`) but never triggered — neither `SignInImpl` nor `SignUpImpl` ever passes the error prop; errors surface via toast only, canon's exact copy is lost.
- Safety-chip vocabulary has drifted from canon's specific 6+5 list (code ships a different 8+3 set).
- Canon's dedicated "Picking up where you left off" pending-handoff restoration screen was never built.
- Pre-auth signal chips shifted from canon's multi-select taste-tag model to single-choice (plausibly a deliberate backend redesign canon was never updated to reflect).

**Onboarding**
- The trip-in-mind lane now routes through two taste-collection screens before sign-up, directly contradicting canon's stated principle that a trip-in-mind user "goes straight to the trip" — needs adjudication (a coherent product decision, not dead scaffolding, since the captured signals feed real downstream consumers).
- The D22 Fleuron→VesperMark bug class recurs in 5 more onboarding spots the original fix didn't reach: Cover's brand mark, Gift/Permission button icons, `TripCaptureFrame`'s talk-through line, `ContextualAuthShell`'s sign-in kicker.
- Taste-collection UI ships as a conventional row-list where canon specifies full-bleed gouache tiles.
- `app/onboarding-safety.tsx` (dietary/allergy capture) has no canon counterpart at all.

**Costs**
- No trip-day field on Add/Edit expense — hardcoded to `new Date()`, so users can never log a past-day expense even though the ledger is day-grouped.
- `ExpenseDetail.tsx` has structurally diverged from canon's dashed-card/color-coded-split receipt grammar, growing real undocumented features instead (comments thread, "mark my share as settled," source-proof badge, itinerary link).
- Masked rows show the lock icon but not canon's "PRIVATE" split-label swap.

**Proposal & Decision Detail**
- `RevertConflictSheet`'s "summary" state is dead code (defined, tested, never invoked from any production call site).
- Its live "conflict" state has diverged from canon's per-item Keep/Discard interaction into a backend-resolved binary Force/Keep choice — a real, reasoned redesign canon was never updated to reflect.
- Rejected and plain-withdrawn (non-revert) proposals render **no closed-state banner at all**.
- All 3 `RevertConflictSheet` title calls still default to `size='large'` instead of the newer `dense` size.
- `ProposalDetailScreen` hand-rolls its own header chrome instead of reusing the shared `ProductiveHeader` canon's Chrome wrapper specifies.

**Trips Home**
- `TripsHomeTrail` collapses canon's 8 independently-labeled sections into one list under a single rotating shared label.
- Cold-state shows two sections both labeled "OR START FROM" with Dreams sandwiched between them, breaking canon's specified order.
- `TripsFooter` renders unconditionally where canon shows it only on some hero states.
- Top-bar shows Search+Bell where the canon file on hand shows Plus+Bell (plausibly canon-stale, not code-wrong — Universal Search shipped after this canon page).

**Trip Creation**
- The closing VesperLine uses the wrong register — canon's actual pattern for this specific line is muted-italic-no-kicker; the shared `VesperLine`/`VLine` primitive never renders the "VESPER" kicker canon specifies, in **any** of its usages app-wide.
- The joiner-variant screen never swaps to canon's distinct "Your turn to start one." headline; adds an extra `StateNotice` canon's joiner screen doesn't show.
- `ShapeCard`'s selected-check badge is styled inverted from canon (filled-gold vs. canon's outline-on-cream) plus a small size delta.

**Interaction Surfaces**
- `ConfirmDialog`'s scrim value is 0.45 vs. canon's 0.40, and its justifying code comment is factually backwards (claims Center Dialog is canon's "heaviest" scrim; canon has two heavier).
- Peek/chooser snap-height caps run ~1.3–1.4x past canon's stated envelope (max-height ceilings, so short content is unaffected).
- `ConsequenceBanner` violates canon's explicit "no circular icon containers" rule.
- `Deck.tsx`'s raw `<Modal>` gap (long-tracked) is still open.
- `sheet-atoms.jsx` and `field.jsx` — real canon content — are still unread by any audit; flagged follow-up.

**Sheets (family)**
- Canon's own reference implementation, `SectionEditSheet.tsx`, doesn't use `SheetHeader`'s `edit` mode built specifically for it — stacks a hand-rolled Cancel/Save row instead, and routes dirty-dismiss through the heavier `ConfirmDialog` rather than canon's sheet-anchored discard panel. `edit` mode has zero call sites anywhere in the app.
- `large`/`edit` title sizes render Medium weight against canon's spec'd SemiBold — flagged for adjudication, not auto-fixed.
- `RevertConflictSheet.tsx` is a ready, un-migrated `dense` candidate (same item as under Proposal & Decision Detail above).
- No code equivalent of canon's `VSheetField` (borderless read-only display atom).

**Motion**
- ~~Several components … no reduce-motion~~ — **RESOLVED 2026-07-12 (PR-M1 #79):** audit list already gated; SpotTake caret → `usePulse`; `motion-governance` ratchet in CI.
- ~~Press-scale 0.97 + spring~~ — **RESOLVED 2026-07-12 (PR-M2 #76):** `pressScale` 0.98 + 120ms `withTiming` in `Tap`.
- The row's own canon-file mapping was wrong (assigned file has zero motion content; real content lives in `vesper-canon-consolidation-app.jsx` §06c, uncited by any manifest row).

**Header system**
- ~~`story.tsx`'s `MemoryStoryHeader` fork~~ — **RESOLVED**, now a thin `ProductiveHeader` wrapper (see Trip Story resolution in the summary above). Note predates the fix.

**Notifications**
- ~~TODAY/YESTERDAY/EARLIER only on Trip-Updates~~ — **RESOLVED 2026-07-12 (PR-N1 #77):** Global / Trip-Scoped / Personal now time-sectioned; Trip Updates keeps Live/Planning/Returned.
- ~~NeedsEye bordered priority card~~ — **RESOLVED 2026-07-12 (PR-N1 #77):** full-bleed hairline band, no card chrome.
- Kicker isn't always the spec'd muteSoft; loading skeleton doesn't mirror the row shape; push-denied CTA says "Turn on" instead of canon's "Open Settings"; stale banner drops the last-synced timestamp and list-dimming.

**Places**
- ~~`PlaceHome.tsx`'s naming-collision shadow function~~ — **RESOLVED**, renamed to `PlaceFleuron` per D23 (commit `236f280e`). The Wave 3 note predates this fix.
- `SpotActions.tsx` is dead code with a now-false self-description, and is literally the "forbidden floating action rail" canon explicitly says not to build — should be deleted.

**Itinerary**
- Date-rail conflict-dot gap (long-tracked) still open — `conflictsByDayId` never threaded into the date-rail's own dot computation.
- `ReviewStackSheet.tsx` uses `colors.purple` for its "GROUP DECISION" kicker — violates both the itinerary canon's 4-tone rule and the app-wide color doctrine.
- `ChangeStudioSheet`'s flat action list vs. canon's sectioned PLAN/MARK/VIEW/REMOVE hierarchy (self-documented as deliberate Phase-0 scope).
- No held-booking warning banner.

**Chat**
- `history.tsx`'s `ThreadHistoryRow` shows the thread's own title-initial where canon always shows a fixed serif "V" Vesper monogram.
- `ChatActionRow` secondary-action register, `GroupEventLine` italic misuse on system/join lines, `GroupVesperNote`'s compact-variant register swap, offline cached-thread signal, `PrivacyHandoffCard` still orphaned outside the dev gallery.

**Route & Transport**
- Route-line color/dash is keyed on travel mode in code vs. canon's booking-status taxonomy — a legible promise ("this leg isn't booked") isn't currently visible on the map.
- Neighborhood card missing canon's "n saved here" affordance (no backend field either — substrate-gated).
- Bespoke parchment Mapbox tile style honestly self-documented as not-yet-shipped (substrate-gated on an external asset).
- canon-owes-code: a real, live "Optimize route" TSP-reorder feature has zero canon documentation.

**Booking & Reservation**
- No manual/phone-only handoff branch in the session screen.
- Hold states show a static deadline, not canon's live mm:ss countdown.
- Confirmed-booking receipt drops "View in plan"/"Contact provider" down to Cancel-only.
- Group/shared-booking states (organizer-books-for-group, waiting-on-approval) entirely absent, no flag gating them.

**Trust & Controls**
- Canon's "post-deletion goodbye" terminal screen still missing (canon itself flags this as a remaining gap) — account deletion drops the user cold onto generic sign-in.
- Default toggle-ON fill is a diluted gray, not canon's near-black ink — affects the app's 4 most common toggle rows.
- One state (`PHONE NEEDED`) bypasses the shared `TrustStatePill` component, rendering as a chrome-less raw label.
- `trust-screens.jsx` and `account-lifecycle.jsx` (2 of 4 sibling canon files, define the actual screen bodies) still unverified — real follow-up needed for full screen-composition fidelity.

**External Sharing & Public Entry Points**
- `PrivateSurfaceGate` — canon's dedicated answer to protecting costs/decisions/itinerary from link-walkers — is fully built to spec but wired into **zero** app screens.
- The "Ask Vesper" secondary CTA canon specifies for place entries is absent from both public place/venue routes.
- Only 1 of canon's 3 place-entry recipient modes is implemented (no person-attribution mode, no trip-scoped-hidden mode).

**Guide & Collection Reader**
- Canon's "Ask Vesper bar" (quiet/strong states, contextual copy) was replaced by a materially different pattern (a row of always-strong pill buttons); the "more" 3-dot menu is entirely unported. **Caveat**: the code cites a different, newer canon file as its source of truth — needs a follow-up read of that file before treating this as a regression rather than an intentional supersession.

**Global Chrome**
- Background alpha is 0.78 vs. canon's 0.92 (borrowed the wrong token, authored for a different surface).
- Collapsed-circle size is 56 vs. canon's 52.
- Badge-count computation + styles are dead code contradicting the file's own doc comment.
- App-shell files (`app/_layout.tsx`, `app/index.tsx`, `PushAskHost.tsx`) have no real canon home — the mapping itself is weak.

**Buttons (family)**
- ~~`ghost` variant missing hairline border~~ — **RESOLVED** (commit `5fb353e1`). Note predates the fix.
- Canon's `amber` variant has no `Button.tsx` home (mitigated by `StayButton`'s tone wrapper reaching the same tones).
- Code ships `secondary`/`success`/`tint` variants canon's taxonomy doesn't name.
- `CostsReceiptButton`'s entire stated reason for staying separate — a "ticket silhouette with punched notches" — was never built; renders a plain pill.

**Cards kit (family)**
- ~~Trust's spine color off by one hex digit~~ — **RESOLVED** (commit `5fb353e1`, new `trustInk` token). Note predates the fix.
- `ActionRow` never implements canon's dismiss-vs-navigational secondary-action styling split.
- `ConciergeCaptureNudgeCard` hand-rolls its own card shell instead of using `CardSurface`.
- `Deck.tsx`'s r20 full-screen overlay is a 6th, unaudited shadow recipe outside canon's container table.

**Tokens (family)**
- `muteSoft`/`ink80` text debt largely cleared (2026-07-12 tokens campaign T0–T7): raw budget **286→134**; classifier post-T7 **TEXT 0 / DECORATIVE 101 / UNCLEAR 33**. Decorative muteSoft stays by design; UNCLEAR leftovers need render checks (icons/chrome/aliases).
- `blue60`/`planningInk` **RESOLVED** (T4): snapped to canon `#2A5A8A`.
- `colors.surface.sage` is overloaded (status-affirmative in some places, pure decoration in others) — needs file-by-file judgment before its value can move.
- `fsStamp` equivalent for the sanctioned sub-9pt exception (D7) not yet added to code.
- UNCLEAR muteSoft sites (33): leave until render-checked — list via `travel-app` `node scripts/classify-muteSoft.mjs`.

**Stay**
- `StayRow` (canon's Trip-Home stay module) is fully built and correctly ported but never wired into the live Trip Home — `TripFolioHome.tsx` uses a structurally different row that carries none of canon's vote-pending/hold-expiring attention signal.
- No confirm/release affordance for a held candidate once it's held (backend supports releasing with `null`, never called).

---

## P3 — Minor / cosmetic / hygiene / dead code

- **Changes**: resolved-row "Undo" renders as a full secondary Button labeled "Revert," heavier than canon's subtle inline mono-text toggle.
- **Row System (family)**: `TimelineObjectRow.tsx`'s reduced 4-state grammar vs. the rich 8-state spec — known, deliberately-deferred (1 call site, mock data).
- **Header system**: `ScreenHeader`'s `showBack=false` fallback branch is dead code (zero call sites).
- **Trip Settings & Admin**: destination-row gating inconsistent between trip-settings and trip-info screens for the same action; Archive uses a centered `ConfirmDialog` where canon specs a bottom Sheet with itemized reassurance.
- **Trust & Controls**: 4 dead exported primitives (one, `TrustGroup`, also structurally drifted from canon's Zone-alias behavior).
- **Photo & Media Intake**: default visibility is unconditionally "group" even solo, where canon's stated doctrine says private-by-default (canon itself is internally split on this one).
- **External Sharing**: privacy-note copy runs 2 sentences against canon's explicit one-sentence rule; no dedicated tests for the two public route files despite being unauthenticated and privacy-sensitive.

---

## Polish family gap-close leftovers (2026-07-12)

Campaign brief: `design/code-alignment-brief-2026-07-12-polish-gap-close.md`. G1–G4 implemented on feature branches; do not rediscover the closed items (local-button budget 0, PublicHeader/TripFolio cold chrome, StatusPill rename+ratchet, SheetHandle budget, GroupAgency ConfirmDialog).

Still deferred by design (owners: frontend polish):

- **Buttons — Keep it muted fill** (`ConflictResolutionSheet`): adjudicate new `Button` variant vs permanent local exception.
- **Buttons — `CostsReceiptButton`**: ticket silhouette never built; implement notches or document as plain-pill exception.
- **Buttons — species park:** on-dark Discover cover CTAs, booking tone-pills, People `RolePill`.
- **Sheets — remaining Modal bypasses** (tracked by `check-sheet-bypass-budget.mjs` @ 13): VoiceOverlay, ProposalDetail sheet mode, Deck, FindPhotos native `pageSheet`, etc.
- **Headers — device dogfood** of glass entry + G1/G2 chrome (checklist in gap-close brief G5); not a code bug.

---

## Notes on scope

- Rows not listed above (`Interaction Surfaces` sub-items already folded into P2, family rows, etc.) either had zero open findings after this session's fixes, or are `deferred`/`pending-canon` and intentionally untouched (Discover, Atlas, Planning-Progress Cards).
- Several items above are explicitly **substrate-gated** (real backend data/flags don't exist yet) rather than code bugs — noted inline where the original audit called that out. Don't "fix" those without the backing data model.
- A few items name a real product/design decision needed before code can move (Onboarding's taste-collection lane, Guide Reader's Ask-bar redesign) — these may want their own D-numbered adjudication brief, same pattern as D23. Universal Search's Actions routing and Voice's full-screen-vs-bottom-sheet question are **not** in this bucket anymore — D25 and D24 already ruled on both; what's left in each case is mechanical code follow-up (see P1 above), not an open design question.
