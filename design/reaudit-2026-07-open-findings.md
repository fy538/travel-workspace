# Open findings — zero-trust re-audit campaign (2026-07-11)

Every unresolved finding from Waves 0–3 + the handoff-135 re-check, pulled out of `design/surface-manifest.yaml`'s per-row `notes:` fields into one prioritized list. Source of truth is still the manifest — this doc is a synthesis for planning, not a replacement. File:line citations are preserved where the original audit gave one; re-verify before acting, since code keeps moving.

**Already fixed this session** (do not re-open): Row System's failed-booking halo bug, Buttons' `ghost` variant border, Cards kit's Trust spine color, Trip Settings' ungated Vesper-autonomy permissions, Voice registers' D8 mechanical follow-ups (6 sites), Trip Story's 2 privacy leaks + 3 of 4 canon-decision violations (07-07 fix pass). See git log in `travel-app`/`travel-agent` for commits.

---

## P0 — Security

- **Trip Settings & Admin — RESOLVED same session.** ~~permissions.tsx's Vesper agency-mode/threshold controls had zero `isOrganizer` check~~ — fixed, `travel-app` commit `b55f42e3`. Listed here only so it isn't re-discovered as new.

No other P0s found.

---

## P1 — Structural (breaks a real user-facing promise)

### Trip Story (`status: gap`, the most severe open finding of the campaign)
- `visible_places` / `generalized_place_chips` / `route_cue` are hardcoded to `[]`/`None` throughout the entire backend projection builder (`story_projection.py`) despite full schema support and heavy canon spec — the "compute chips from story" step was apparently never written, no flag/TODO marks it deferred.
- The 9:16 share-card and public landing page use a completely different visual language than canon (indigo accent, system sans, no EB Garamond) — `story_landing.py`'s CSS and placeholder env vars are **byte-identical** to the unrelated `invite_landing.py`, strong evidence the invite surface's generic template was copied wholesale without a Vesper brand pass.
- Canon's "Trip group" visibility tier (sign-in-gated viewing by named members) doesn't functionally work — falls back to link/public-only server-side.
- Owner attribution line ("Shared by X") missing from the public viewer.
- `ShareLink` lifecycle/analytics fields unimplemented: `expires_at`, `replaced_by_share_id`, `unique_viewers`; all 13 canon-named analytics events still write to nothing (persistence table dropped 2026-06-20).
- #16 (Plan Similar's "conversation") only partially fixed — an honesty fix (no longer poses as a live chat turn), not the real fix; a true conversational entry needs new pre-auth stash-and-resume infra, explicitly deferred as separate scoped work.
- `MemoryStoryHeader` fork (`app/(tabs)/trips/[tripId]/story.tsx`) still unmigrated — tracked jointly with Header system below.

### Voice — live mic / voice chat (`status: gap`)
- Structural mismatch: canon specs a full-screen dark "Calm Listening" takeover with a tap/hold gesture split (`vesper-home-voice.jsx`); code ships a bottom-sheet LiveKit modal with no hold-to-talk gesture anywhere, and a purple accent color where canon is consistently amber/gold (and the app's own color doctrine says purple is legacy/agent-presence-only).
- `useVoiceSession`'s `_connectToRoom` is a documented no-op stub — no real audio connects even with the feature flag on.
- `MicStatusIndicator` is fully built and tested but never mounted anywhere (dead code).
- `useNarrationWithInterruption` is a fully-built, ~1000-line-tested hook with zero production callers.
- `MicPrivacyDisclosure`'s shown copy describes the never-wired interruption flow and the never-mounted status indicator — users see a privacy disclosure for a feature that can't currently happen.
- Open product/design question underneath all of this: is the full-screen "Calm Listening" model still the target before investing further in the bottom-sheet shell?

### People & Collaboration
- Canon's pending-invite `MemberActionSheet` variant (Resend / Copy link / Revoke) was never wired — pending invites get only an inline revoke icon.
- Group-chat vote widget is missing canon's per-voter-avatar/tally grammar **both in UI and in the underlying data model** (`VoteWidgetData` has no voter/count fields at all, unlike the itinerary-side `PlanDecision` which does).
- Self-profile has no "Edit profile" affordance canon specifies.
- Unfollow has no long-press friction guard canon's caption calls for.
- Co-organizer role is half-built — present in component props/visual markers, absent from the live `TripContext` role type (unreachable in practice); even the scaffolding is internally inconsistent (`RolePill` and `PeopleAvatar` disagree on its color).

### Universal Search
- The "Actions" result group ships as a read-only, non-tappable audit log where canon specifies executable command rows ("must be executable... never decorative") — a deliberate, self-documented architectural pivot that was never reconciled with canon. Needs a product call.
- Places results never distinguish the user's own saved places from public Discover venues — provenance is hardcoded to "DISCOVER"/public always; the personal-saves table is never consulted, contradicting canon's explicit `saved_by` contract.
- On-trip scope-chip rail grew to 7 chips against canon's explicit "max 4–5" rule — a direct side effect of shipping Receipts/Costs/Actions without folding them back under "This trip."

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
- `ErrorState.tsx` and `StateScreen.tsx(tone='failure')` are two visually different implementations of the same canon-blessed full-page hard-failure tier, live simultaneously (34 vs 13+ call sites) — exactly the "local state treatment" drift canon's own doc warns against.
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
- Several components running legacy-Animated-API loops/timings have **no reduce-motion check at all** (`VoiceOrb`, `CardStates`, `CardLive`, `CardLift`, `Deck.tsx`, `OrganizerInviteNudge`, `ErrorBanner`, `AtlasMemoryReel`, `NavChromeContext`) — contradicts canon's explicit "disables all nonessential animation, app-wide" rule.
- Press-scale drifted 0.98 → 0.97; press feedback uses a spring where canon specifies a fixed-duration timing collapse.
- The row's own canon-file mapping was wrong (assigned file has zero motion content; real content lives in `vesper-canon-consolidation-app.jsx` §06c, uncited by any manifest row).

**Header system**
- `story.tsx`'s `MemoryStoryHeader` is a real, still-unmigrated fork — parked pending the Trip Story rework per the J1 brief's own recommendation (do not migrate standalone). Same item as Trip Story above.

**Notifications**
- TODAY/YESTERDAY/EARLIER sectioning is fully implemented but never wired into 3 of 4 canon screen modes (only Trip-Updates mode sections its rows).
- The priority/time-sensitive strip has reverted to a bordered, tinted card — exactly the pattern canon's own doctrine explicitly killed.
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
- `muteSoft`/`ink80` still used as real text color at ~292 sites despite canon's explicit "never text" rule.
- `blue60`/`planningInk` never reconciled to canon's hex value the way its sibling status hues were.
- `colors.surface.sage` is overloaded (status-affirmative in some places, pure decoration in others) — needs file-by-file judgment before its value can move.
- `fsStamp` equivalent for the sanctioned sub-9pt exception (D7) not yet added to code.

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

## Notes on scope

- Rows not listed above (`Interaction Surfaces` sub-items already folded into P2, family rows, etc.) either had zero open findings after this session's fixes, or are `deferred`/`pending-canon` and intentionally untouched (Discover, Atlas, Planning-Progress Cards).
- Several items above are explicitly **substrate-gated** (real backend data/flags don't exist yet) rather than code bugs — noted inline where the original audit called that out. Don't "fix" those without the backing data model.
- A few items name a real product/design decision needed before code can move (Onboarding's taste-collection lane, Universal Search's Actions inversion, Voice's full-screen-vs-bottom-sheet question, Guide Reader's Ask-bar redesign) — these may want their own D-numbered adjudication brief, same pattern as D23.
