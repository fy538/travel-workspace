# Master Alignment Backlog — accumulator (canon 108 vs main)

## Trips Home — ~1.5 days
- STRUCTURE/STATES/COPY: ALIGNED. BEHAVIOR: MAJOR(1).
- [M] "Not now" session-suppression absent + mis-wired (secondary dismisses table, not urgent lead; needs session hook + material-change re-elevation) — assemblers.ts:118, TripsHomeViews.tsx:380
- [S] Immersion register full-bleed only fires for live; ready/returned/planning never escalate (TripHeroCard vs immersion-register canon fire rule)
- [S] "OR START FROM" carousel = hardcoded STARTER_IDEAS; canon cites real saves (TripsHomeViews.tsx:175-211)

## Vesper Home (FocusHome) — verdict 79%
- Registers 5/5 ✓ (whisper gone), composer two-anchor ✓, universal bar ✓, single-item collapse ✓, status strip weather-backed ✓, deck faces: 6 shipped + Flight/Compare dormant-by-design ✓ ("structure earns deck" logic correct)
- [M/High] NO deck entry card on home surface — canon's 4 entry treatments (incl. session-C2-mounted rail-line) unbuilt; deck only opens via rail/hero tap; missing "N things need you" pre-tap summary
- [S/Low] DeckCompareFace dead code (component exists, no routing/backend signal — documented)
- [S/Low] FocusState→canon-board mapping correct but implicit/undocumented in code

## Trip Document (TripFolioHome) — FULLY ALIGNED, zero gaps
- All 5 lifecycle modes, 8 hero faces, receipt quintet, 8 reaction evidence types (ReactionReceipt exists as placeholder rendering — softer than expected, acceptable), margin AlsoMoving + ChangeLedgerStream (72h dated), edge states incl. solo, memory ×3, ◷ chip routes to changes, substrate-honest copy. "Design execution quality: EXCELLENT."

## Places — ALIGNED (9/10 across axes)
- City rich/cold + neighborhood modes ✓, Take 4 states ✓, experience FULL-SCREEN ✓ (presentation="screen" unwraps sheet chrome), bookmark glyphs ✓
- [S] ExperienceDetailSheet unused BottomSheet imports cleanup
- [S/ruling⚠] Code uses "Add to plan" — canon L-ruling says "Add to trip"; a consolidation doc claims exemption. NEEDS ADJUDICATION (flag in synthesis)
- [M] Verify polish-qa surfaces.mjs + route-owners.yaml register the 6 consolidated routes (in-flight parallel work)

## Trip Creation — behaviorally ALIGNED, visual-moment gaps
- Conversation-first ✓, ChoosePlaceSheet ✓, 6 starter shapes ✓, blank shell ✓, voice ✓
- [S] Draft/Promotion render as chat cards, not screen takeovers (deliberate simplification — ADJUDICATE: accept or build)
- [M] OnboardingResume screen missing
- [S] NotReady state inline-only; [S] error states = banners not screens; [S] CreationFolioHandoff visual beat absent (behavior correct)

## Itinerary/Plan — ALIGNED, 3 gaps
- 5 screens, block grammar, ChangeStudio routing incl. booked-warning, live strip, map-face toggle, composer-resolution per C2, register ✓
- [M] Date-rail CONFLICT DOT missing (rail builds planned/changed only; canon oxblood conflict dot; conflictsByDayId exists server-side)
- [M] ChangeStudio booked-warning strip visual verify vs canon
- [S] ReviewStack group-decision card styling spot-check

## Discover Map — aligned for shipped scope
- 2-snap sheet, 4/5 states, 7/12 pins, cluster zoom, list fallback, AX labels ✓
- [S] reduced-motion guard missing on cluster zoom (300ms hardcoded — stance violation)
- [S] location-denied copy mismatch; [M] offline-cached state (beacon bar + saved-pin filter) not implemented
- [M] trip-aware mode skeleton unwired; [L×2 Phase4+] social pin taxonomy (friend/experience/place/unavail/approx/suggest) + scope/layer sheet

## Chat — ~70%, weakest surface so far
- Structure/copy strong (left-aligned header, group room, card families, agency wiring)
- [S] header still uses title PILL (canon = plain text); [M] in-thread THINKING escalation missing (only typing footer)
- [M] failed-send state (grayed bubble + Retry + Edit) unwired; [M] offline "showing cached thread" in-list signal missing
- [S] Load-earlier affordance missing at top; [M] privacy-seam DIVIDER not rendered in group thread (card exists, seam doesn't)
- [S×4] verify: decision-card open-state layout, header→agency wiring, document-mode draft badge, create-flow 3 scopes

## Changes — 2 MAJOR behavior gaps (weakest behavior score yet)
- Masthead/urgent banner/delegation/undo/error ✓; empty/loading/solo ✓
- [M] SourceChip component missing (Vesper/member/group/Atlas 26px badges — rows show text author only)
- [M] VoteInPlace inline voting buttons missing (only Review→detail chevron)
- [M] read/unread state + 0.55 fade missing entirely
- [M] RevertConflictSheet uses generic list, NOT canonical WAS/NOW tinted diff (canon sanctioned NOW-struck side-by-side — unbuilt)
- [S] bucket casing TODAY/EARLIER (code has Yesterday 3-bucket); [S] empty copy variant

## Saved & Collections — foundations solid, flows unshipped
- Index + manage mode + row grammar + save-state labels ✓
- [L] add-to-trip sheets ×7 missing entirely (onAddToTrip = dead prop)
- [M] city collection detail + multi-city anchor screens missing
- [M] row state hydration never populated (labels exist, no data derivation)
- [S] empty-state copy says "guide" (canon: concrete objects only)

## Readers (dossier/angle/guide) — 7.4/10 CONDITIONAL PASS
- ReaderChrome shared ✓, behavior/copy strong, walk-minutes clean
- [M] ReaderStates board NOT consumed — states ad-hoc per screen (canon: shared components)
- [M] 6 routes unregistered in polish-qa surfaces.mjs + route-owners.yaml
- [S×2] contracts missing/stale — ⚠ ALL COVERED BY IN-FLIGHT parallel consolidation doc; assign there, don't duplicate

## Story/Photo/Sharing — aligned; gaps = verification not build
- SectionEditSheet/ShareStorySheet (pause/revoke/stats) ✓, public DEFAULT-DENY ✓, copy 9/10
- [S×3] state-badge + permission-variant + composing-spinner parity checks
- [M×3] public-landing shape-test fixtures, redaction render parity, photo-artifact 4-state
- [L×4 = QA-lane work, not alignment: visual regression suites + flag-dark renderer validation]

## Discover feed — structure 9, states 6
- Zone grammar + server-sectioned layout + dossier formats ✓
- [S] COLD-START state absent entirely (canon session-4 board never built)
- [S] empty-city copy generic; [S] error copy variant
- [M] in-discover search not scoped to editorial (Universal Search opens unscoped)

## Contrast tokens (cross-cutting) — best-case finding
- SSOT = constants/colors.ts:82-83; atlas/vesper aliases propagate; ZERO hardcoded stragglers; ZERO snapshot fallout
- [S] mute #86807A → #6E6862 = ONE-LINE fix (518 text sites fixed at once)
- [M] muteSoft carries text at ~200 sites (1.8:1!) — per-site retoken to mute; muteSoft stays decorative

## Universal Search — 83%
- All states + 5 scoped entries + Ask handoff + provenance ✓
- [M] action rows NON-FUNCTIONAL (routing returns null for is_action — canon: never show unexecutable action)
- [M] scroll-to-entity rule unimplemented (lands top-of-page)
- [S×3] discover-group untested, nearby permission retry, provenance-tier validation

## Proposal & Decision Detail — WEAKEST WEDGE SURFACE (~13/18 states)
- Skeleton + receipt dispatch + trust plumbing ✓; author/read-only/vote-comment/version-restore ✓
- [M/ruling⚠] VERB VIOLATION: "Reject" + "Accept change" buttons (canon: Decline / Approve & apply to Plan); "Neutral" off-canon
- [L] ProposalVoteRows contract absent (no voter avatars, per-option counts, "Waiting on X")
- [L] RevertConflictSheet = 1 of 3 canon states (no clean-confirm, no per-item Keep/Discard, no partial summary) — CORROBORATED by Changes audit (no WAS/NOW tinted diff)
- [M] conflict state C (hour-track + Fix it) missing; [M] booking-hold receipt bare
- [S×5] lazy countdown+Object, author Withdraw (mutation exists!), expired/superseded ClosedBanner, organizer retry, offline-stale, AffectedPlanRows tags

## Notifications — 88%
- 4 modes + filter wiring + severity + unread + push-denied recovery ✓
- [L] stale-tap rule covered for 1/20 types only (hold_expired); resolved-subject landing unguaranteed elsewhere
- [L→BE] type taxonomy: only 4 notification sources; Booking/Stay/Costs/Route types conflated into proactive (backend schema work)
- [M] ownerSurface = fragile route-path heuristics (canon: explicit field, flagged future)
- [M] push permission state machine split across 2 flows; [S] priority strip noisier than canon flat label+action; [S] severity-field fallback removal; [S/M] actor initials beyond social

## Global Chrome — CRITICAL ruling violation
- Pill states + scroll behavior + tap-expand + collapsed-no-badge ✓; inset hook used in 13 files
- [M/ruling⚠] BADGES ON ALL TABS (canon: NO badge — recorded decision) — _layout.tsx:83/95/106 + FloatingTabBar:144
- [M] hide-matrix incomplete: edit sheets/lightbox/voice overlay/map drawer/permission/checkout unverified
- [M] inset adoption unaudited outside 13 files; [S] 'me' hidden-tab undocumented in canon

## State System conformance — kit built, legacy dominates
- Kit maps 1:1 (StateNotice covers Stale/Offline tones); SessionRecovery VERIFIED incl. route-restore via stash/consume
- [M-wide] migration: ErrorState 37 vs ErrorRecovery 2; EmptyState 13 vs EmptyHero 6; Skeleton legacy 44; OfflineBanner legacy 6; ActionFailureInline used 0×; 2 hand-rolled screens (TripFolioHome local error card, profile toast-only errors)
- [L] OFFLINE FLOOR NOT MET: zero Mapbox offline packs anywhere (canon stance: map pack + cached reads must WORK offline) — unbuilt subsystem
- [S] copy rules not encoded (only oxblood color rule in stateTokens)

## Motion Stance conformance — module EXISTS, predates canon
- constants/motion.ts + utils/motion.ts (reduce-motion aware, "no spring overshoot" documented); house bezier exists but demoted to easing.lift; default = out(cubic)
- [ADJUDICATE] canon vs module disagree on 3 token values (fast 160v150, slow 240, shimmer 1200v1100) — decide authority BEFORE code changes
- [S] retune token values + promote house curve to default (1 file)
- [M] migrate stragglers: ~29 hardcoded durations (9 files), 25 legacy Animated.timing, 5 unclamped springs (Tap.tsx ζ≈0.65 overshoots = "never bounces" violation ×5), toast 220/180 vs 200/150
- [S/ADJUDICATE] Skeleton = deliberate 1.2s SHIMMER SWEEP — canon explicitly bans shimmer ("reads glossy, not paper") → pulse rework or canon amendment

## Onboarding + Auth/Invite — 9/10 ALIGNED, no required fixes
- 12/12 screens, 5 paths, OTP semantics sound (3-stage machine), 8 invite errors (> canon 6), escape hatch, safety/signal chips ✓
- [S optional] invite hero = single organizer avatar vs canon AvatarCluster (conscious variant — record or align)

## Fixture parity — WORST-CASE cost; needs ADJUDICATION
- NO fixture matches canon world: default Lisbon Jun 4–10 w/ Alex Kim/Sarah/Mike; mara-persona Lisbon Oct 3–6; ben Kyoto Jun 17–24 no Mara; "Casa da Mar" TYPO frozen into tests; Maya R. Lin + theo don't exist
- Full alignment = [L]: ~10 fixture files + prose coupling + ~30 test files + 71 Maestro yamls + ~150 screenshot goldens cascade
- OPTIONS: (a) accept disjoint worlds (canon illustrative, fixtures functional) + fix only "Casa da Mar" typo [S]; (b) minimal demo slice: add theo/mara personas + rename default self [M]; (c) full migration [L]

## Costs — ~70%; "last 30% render-only"
- Chassis/states model/settle math genuinely canon-shaped; empty line EXACT canon match
- [L] disputed/masked/reimbursement rows = renderers with NO data path (masked:false hardcoded)
- [M] Balance drill-in missing (dense computed, unconsumed); [M] AddExpenseSheet = pre-canon form (no amount hero/trip-day, old typography); [M] Add/Detail push as SCREENS not sheets-over-ledger; [M] Nudge = stub toast
- [S/substrate⚠] "Estimated trip shape" card VIOLATES no-forecast ruling (in code!); [S] starters fake amounts + not tappable; [S] settled drift + dead "All settled up!" legacy component; [S] hasTripHomeSignal unwired

## Interaction Surfaces conformance — primitives 85%, adoption thin
- ONE BottomSheet family w/ canon props (snap presets, scrimOpacity, onDirtyDismiss) — canon was literally written against this code; Alert.alert = 0 ✓; ~5-6 real raw-Modal offenders
- [M] snap presets used in only 4/24 consumers; NO swipe-to-dismiss anywhere (canon requires on peek/chooser/form)
- [S-M] scrim sprawl: 13 distinct values vs canon 6; default = photoScrim 0.35 token misuse
- [S] toast: no 5s error tier; no swipe-dismiss; [S] dirty-dismiss adopted 1/6 sites; [S] typed-confirm ZERO callers
- [M] ASK-THE-ORGANIZER NOT BUILT: one static no-onPress string; ~8-10 gate sites + BlockedActionRow + chat-send hook needed

## Trip Settings & Admin — STATES D+ (~40% of canon state space)
- Kit mirrors canon component table ✓; leave-guard/handoff-then-leave/remove-days warning/substance-gate real ✓; destructive copy near-verbatim ✓
- [L] delete/cancel trip + typed confirmation ABSENT end-to-end (ConfirmDialog.typedConfirmation = dead code)
- [L] ask-organizer 403 pattern unbuilt (tripChatPrefill infra exists — corroborates IS audit)
- [M] trip NAME uneditable (no TripInfoEdit form + dirty guard); [M] ConnectedSystems statuses static; [M] member role-gating leaks (Trip rows + Archive tappable by members)
- [S×3] remove-member cost-risk banner, dates conflict ignores stay/bookings + no live-caution, no trip-unavailable/failed-save states
- States: dates 1.5/5, connected 0/2, settings ~2/5, admin end-states 2/6

## Route & Transport map face — 95% ALIGNED
- All 9 artboards implemented; lenses/peek/live/sparse/suppress/face-state-sharing ✓
- [M] tentative marker lacks dashed border (RN limitation, needs SVG workaround); [M] no-pin variant missing (renders as tentative, wrong border color)

## Stay — kit faithful, ~1/3 of 23-state canon rendered
- Kit ported (plates, NightRibbon, 8-variant StayCard, StayCompare) ✓; suppress-on-no-dates + quiet-row ✓; vote/hold/choose wired w/ organizer gating ✓; copy verbatim ✓
- [L] /accommodation/[id] = Places Spot face, NOT session-P canon composition; no ConfirmedDetail tap-through anywhere
- [M] trip-home StayRow orphaned; folio StaySection lacks urgency/vote/hold rows + "No bed yet · Add" shows on RETURNED trips (suppress ruling violation)
- [M] candidate/confirm/private sheets missing (useCreateStayCandidate has zero UI; visibility hardcoded 'group')
- [M] StayCompare hard-caps 2 candidates; recommendation/VESPER PICK never passed
- [S×2] vote-arc tail (nudge/majority-hold/resolved-view); split clash FIX + returned record
- Note: utils/staySurfaceState.ts = dead duplicate (WIP deletion in tree is CORRECT)

## Trust & Controls — kit-faithful, A−/B+ structure/states
- All 7 screens on shared kit; receipts/constraints/companions verbatim; push-off banner ✓
- [L] GOODBYE terminal state absent (delete routes straight to sign-in)
- [M] Privacy "WHAT'S VISIBLE" rows = wrong ledger (dietary/budget/energy vs canon saved-places/trips/voice/DNA/stories)
- [M] TrustContract italic-by-default — carries the PRE-repair default the canon compliance pass reverted (+ italic loading lines)
- [M] sign-out = destructive-typed dialog + wrong copy (canon: routine, "nothing is deleted")
- [S×3] export copy variant, memory-receipt "Atlas" vocab drift + missing DNA row, YourPeople row deltas

## Profile — privacy-correct but not promoted to in-app board
- Follow optimistic+haptic ✓, privacy line verbatim ✓, not-following/following ✓
- [M] wrapped in publicWeb ExternalShareShell chrome (canon: in-app board); self state lacks "Edit profile" + "what others see" prefix; sparse hides taste instead of "Nothing shared yet."
- [S] taste phrases italicized (canon: roman non-voice); trips open share_url via Linking (leaves app)

## Copy rulings grep — ~17 visible violations, ALL string swaps [S total]
- Folio leak ×1 (TripFolioHome:2477 "the folio is ready"); Itinerary label ×5 (plan.tsx fallback title/eyebrows, story, settings)
- Add-verb ×4 ("Add to plan" ExperienceDetailSheet:638 + SpotActions + SpotPlanningRail; "Save to the plan" BookingCheckoutPanels:277)
- Voting ×1 visible (ProposalDetailScreen:864 "Reject") + a11y nits
- Undo-vs-Revert ×2 (BlockChangedBanner:87, ChangeTimelineRow:126 — both call revertProposal) + 1 borderline
- Third-person voice ×4 clear (story:658, changes:274, search:541, atlas:726); ~24 meta-copy "Vesper is/can" = ADJUDICATE narrator register
- Dismissal: "Not now" dominant 25; 5 stragglers (Maybe later ×2, Skip for now ×3 — adjudicate onboarding intent)

## Booking — A− structure; "high-fidelity port; debt is behavioral tail, not drift"
- Module decomposition 1:1; 13-state vocab 9 exact/3 partial/1 missing; canon copy verbatim; dark slice fully built behind flag
- [M/LIVE] provider capture saves device-local draft only — "Save to the plan" files NOTHING into plan/costs; confirmed receipt never shows reference
- [S/LIVE×4] plan-level mark-booked skips confirmation-number capture; network-ambiguity copy loses double-booking guard; group states missing; designed empties missing
- [S/DARK×2] hold expires-soon variant + release control; consent panel itemized rows + capture attach field
