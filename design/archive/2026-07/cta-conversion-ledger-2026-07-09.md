# CTA → Button conversion ledger (2026-07-09)

Source: `cta-conversion-scout` workflow vs canon-true Button (a0a7c657). On-wedge surfaces only (Atlas/Discover excluded). MicPrivacyDisclosure already converted (4c09dd45).

**Disposition:** CLEAN = mechanical swap, only canon-convergent pixel change (radius→r22 pill, height→44). JUDGMENT = needs a visual/human call. LEAVE = deliberately not a Button.

~76 CTAs classified across 5 on-wedge surface groups. Note: many "JUDGMENT" rows are judgment ONLY because the CTA has a dynamic label + a richer accessibilityLabel than its visible text — that's not a decision, just "thread accessibilityLabel explicitly." The genuine decisions collapse to D13/D14/D15 below.

## Bucket 1 execution log (2026-07-09, branch `cc1-atom-adoption`, unpushed)

**11 commits, ~25 CTAs converted, 0 tsc errors, ratchets green (radius 379→374), 356 tests pass.** Full commit range: `e5d39291..d4da4157`.

Converted: all 5 Deck faces (DeckStructuredFace/PickFace/BriefFace/CompareFace — one commit each/paired), ReviewStackSheet (5 CTAs), ConflictResolutionSheet (Fix it), PlanEmptyDay (Add/Free time), PlanColdStart (Set dates/Ask Vesper/Refresh), TripFolioHome+TripFolioPostTrip (4 "Open X" CTAs sharing one style), HeroProse+FocusHome (byte-identical hero pill), ExpenseDetail (Mark my share as settled).

**Held back on closer read (ledger was too coarse to catch these):**
- **ConflictResolutionSheet "Keep it"** — flat `#F5F4EF` fill matches neither `tint` nor `secondary`. → D14.
- **ExpenseDetail "Delete expense"** — text color `terracotta[400]` ≠ Button's `danger` (`colors.danger`, a harsher red); Button exposes no per-call text-color override. → D13.
- **PlanBlockRow "Change" + "Done"** — ledger called these CLEAN/JUDGMENT respectively, but reading the surrounding layout shows both are dense inline chips inside an indented (`paddingLeft: 56`) timeline row with `xxs`/`sm` padding — Button's 44px floor would visually dominate a row designed to be dense and glanceable. "Done" even has an in-code comment: *"Light affordance — secondary text, no filled bg."* **New consideration for the design session: dense inline row chips are a distinct species from Button (card/sheet-footer scaled) and may need their own compact chip primitive** — not folded into an existing D-number, flagged separately.
- **CostsEmptyState "Add first expense" / StayHome "+ Add somewhere to stay"** — both wrap `CostsReceiptButton`/`StayButton`, the local primitives already flagged D14, not hand-rolled Taps. Converting means replacing those primitives' whole visual family.

**Process note:** twice a shared style (`secondaryBtn` in PlanColdStart reused by a "Refresh" button; `secondaryPillInline` in tripFolioStyles.ts reused by TripFolioPostTrip) was NOT visible from a single file's grep — caught only via tsc after the fact. Every conversion in this batch was grepped for all call sites of its style keys before/after editing.

## Conversion plan (buckets)

### Bucket 1 — DO NOW (mechanical + a11y-care). One CC1.1c batch.
- **Deck faces (marquee target):** DeckPickFace / DeckCallFace / DeckBriefFace / DeckCompareFace / DeckStructuredFace hand-roll the SAME `btnFill`(ink)→**primary** / `btnQuiet`(#EBE4D6 cream)→**tint** pill. DeckStructuredFace centralizes it in a local `DeckBtn` helper — migrate the helper once, it fixes the vote/settle/flight faces. ~10 buttons, 5 files, one pattern.
- **trip-plan sheets:** ReviewStackSheet (Fix it / Adjust in plan / Keep as is / Review & vote — all one `primaryBtn`/`secondaryBtn` pair), ConflictResolutionSheet (Fix it→primary), PlanEmptyDay (Add→tint, Free time→ghost), PlanColdStart (Set dates→primary), ChangeStudioSheet apply (primary, alignSelf:stretch NOT fullWidth — column).
- **folio/costs/stay clean ones:** TripFolioHome "Open timeline/itinerary"→secondary, TripFolioPostTrip "Open story"→secondary, CostsEmptyState "Add first expense"→primary, StayHome "+ Add somewhere"→primary, HeroProse/FocusHome ink hero pills→primary.
- **semantic quick wins (accept variant semantics):** ExpenseDetail "Delete expense"→danger, "Mark settled"→success, PlanBlockRow "Done"→success.
- **RULE for this batch:** thread each CTA's existing `accessibilityLabel`; use `style={{alignSelf:'stretch'}}` for full-width-in-a-column (never `fullWidth`, which is flex:1); keep paired flex:1 footers as-is (they're rows); drop manual `opacity:0.4` disabled hacks in favor of Button's `disabled`.

### Bucket 2 — DESIGN DECISIONS
**Superseded by the fully-worked-out version in `adjudication-brief-2026-07-09-component-consistency.md` § BUTTON VARIANT TAXONOMY** (added 2026-07-09 after Bucket 1 execution — real call-site counts, exact hex values, and a 5th item D16 found during conversion). Summary: D12 Button-canon-true (RESOLVED, shipped `a0a7c657`) · D13 solid-emphasis destructive/urgency fill + no-text-color-override gap (4+ sites) · D14 per-surface primitives, now with real counts (CostsReceiptButton 3 sites, StayButton 10 sites — favors folding StayButton in, blessing CostsReceiptButton as-is) · D15 on-dark treatment (3 sites, 1 file) · D16 (new) dense inline row-chip species, a recurring pattern not a one-off (PlanBlockRow + 2 more files share the DNA). Priority order for the design session: D14 → D13 → D16 → D15.

### Bucket 3 — DEFER / LEAVE
- **Booking (~10 CTAs):** flag-dark for v1 per MVP scope — do not convert until un-gated.
- **LEAVE (not Buttons):** vesper-cards `faces/*` (all via ActionRow → CC2 card batch), NowModeStrip / BlockProposedBanner (segmented/toggle over dark cards), Deck.tsx triage bar, People `RolePill` (ruled a deliberate species), dismiss/close icon chrome.

## trip-plan

_This is the highest-value group and it is heavily hand-rolled: roughly 30 hand-styled Tap/TouchableOpacity CTAs across ~12 files, none using the shared Button except ChangeTimelineRow.tsx (already migrated to Button secondary/sm — the reference pattern) and RevertConflictSheet.tsx (already routes all CTAs through StickySheetActionBar, so LEAVE). Two files also route confirm CTAs through StickySheetActionBar (AddBlockSheet "Reserve it", RevertConflictSheet) — those are already component-backed, not hand-rolled. Overall adoptability is high: the dominant idioms are (a) solid-espresso "colors.action.text" fill + borderRadius 8/10 → primary, and (b) bordered/text "Keep/Cancel/Discard" → secondary/ghost — both mechanical swaps once radius→r22 pill and height→44 land. The recurring gotcha to preserve everywhere: nearly every CTA carries a DISTINCT accessibilityLabel richer than its visible text (e.g. "Fix it" → "Fix: {conflict.title}", "Apply" → "Apply: {recommendation}", "Revert" → "Undo: {title}") — the converter must thread accessibilityLabel, not let Button derive it from label. Second gotcha: several are sub-44px compact rows (spacing.sm/xs vertical) that will grow to the 44 pill minimum — acceptable but visually noticeable in dense conflict/vote rows. Third: many live in paired flex:1 footers (Discard/Apply, Fix/Keep, Revert/Cancel) where fullWidth is wanted (a row, not a column) so flex:1 is fine — but the asymmetric OptimizeRouteSheet footer (Discard flex:1 vs Apply flex:2) is a JUDGMENT call. NowModeStrip's dark-on-ink translucent action buttons and BlockProposedBanner's stateful toggle-vote buttons are a distinct species (segmented/toggle over a dark card) and should be LEFT. The following table ranks the ~15 most important; trivia (retry text-links, "See tomorrow →", "View all →", GapAffordance, PlanHealthStrip, disclosure toggles, day-header rows, chips) is left out as non-Button ghost/list-row species._

- **[CLEAN · primary/sm]** `components/trip-plan/ConflictResolutionSheet.tsx:287` — "Fix it"
  - now: backgroundColor colors.action.primary, borderRadius 8, paddingH lg / paddingV sm, labelSemiboldSm white text
  - preserve: accessibilityLabel is 'Fix: {conflict.title}' — richer than visible 'Fix it', must be preserved. Paired in a flex-row with Keep it (styles.conflictActions, gap md). Compact sub-44 height grows to pill. Uses action.primary (solid espresso) not action.text — same solid CTA family.
- **[JUDGMENT · secondary/sm]** `components/trip-plan/ConflictResolutionSheet.tsx:304` — "Keep it"
  - now: backgroundColor background.secondary, borderRadius 8, paddingH lg / paddingV sm, bodySmMedium text.secondary
  - preserve: Dismiss/keep action — muted grey fill, not a bordered outline. Maps closest to secondary but it is a soft-grey fill not espresso-outline; confirm variant with design. accessibilityLabel 'Keep it: {title}'. Always-rendered (paired with optional Fix it), so single-child when Fix it is absent — no longer a pair. sub-44 height.
- **[CLEAN · primary/md]** `components/trip-plan/ReviewStackSheet.tsx:251` — "Fix it"
  - now: styles.primaryBtn: flex:1, backgroundColor action.text, borderRadius 10, paddingV md, labelSemiboldMd white
  - preserve: flex:1 in a flex-row (styles.actions) paired with Keep as is — fullWidth/flex:1 is correct here (row not column). accessibilityLabel 'Fix it: {preview.recommendation}'. Shares styles.primaryBtn with the 'Adjust in plan', 'Done', and 'Review & vote' CTAs in the same file — all four collapse to primary/md.
- **[CLEAN · primary/md]** `components/trip-plan/ReviewStackSheet.tsx:259` — "Adjust in plan"
  - now: styles.primaryBtn: flex:1, backgroundColor action.text, borderRadius 10, labelSemiboldMd white
  - preserve: Alternate branch of the same primary slot as Fix it (only one renders). flex:1 paired-row. accessibilityLabel 'Adjust this in the plan'.
- **[CLEAN · secondary/md]** `components/trip-plan/ReviewStackSheet.tsx:275` — "Keep as is"
  - now: styles.secondaryBtn: flex:1, borderRadius 10, paddingV md, hairline border.light, labelSemiboldMd text.secondary
  - preserve: Classic bordered pill → secondary. flex:1 paired row (correct). accessibilityLabel 'Keep as is'. Always renders even when no primary present (single button case).
- **[CLEAN · primary/md]** `components/trip-plan/ReviewStackSheet.tsx:361` — "Review & vote"
  - now: styles.primaryBtn: flex:1, backgroundColor action.text, borderRadius 10, labelSemiboldMd white
  - preserve: Group-decision card primary. Sole action in its row (flex:1 → effectively full width). accessibilityLabel 'Review the proposal: {item.title}'.
- **[JUDGMENT · primary/md]** `components/trip-plan/ChangeStudioSheet.tsx:494` — "Apply change / Suggest to group"
  - now: styles.applyBtn: backgroundColor action.text, borderRadius 10, paddingV md, alignItems center, labelSemiboldMd white
  - preserve: Label is dynamic ('Apply change' vs 'Suggest to group') and accessibilityLabel is even richer ('Apply: {recommendation}' / 'Suggest to group: {recommendation}') — thread accessibilityLabel explicitly. No fullWidth flag but full-width by block layout — use style alignSelf:stretch, NOT fullWidth (column context). Highest-traffic CTA on the golden path.
- **[JUDGMENT · danger/md]** `components/trip-plan/ChangeStudioSheet.tsx:329` — "I understand — see alternatives"
  - now: styles.bookedGateBtn: backgroundColor terracotta[600], borderRadius 10, paddingH xl paddingV md, labelSemiboldMd white
  - preserve: Solid TERRACOTTA fill (destructive-risk acknowledge on a booked block). Button's danger is red TEXT on transparent, not a solid red fill — so a mechanical swap changes the visual weight significantly. Needs a design call: solid-warning fill has no exact variant. Same pattern as MoveBlockSheet moveBtnAcknowledge.
- **[JUDGMENT · primary/md]** `components/trip-plan/MoveBlockSheet.tsx:497` — "Move / Move anyway"
  - now: styles.moveBtn: backgroundColor action.text, borderRadius 10, paddingV md, labelSemibold white; disabled → opacity 0.4
  - preserve: Primary commit; label flips 'Move'/'Move anyway' on booked state and disabled is wired (!canConfirm || wouldCreateHard) — thread disabled to Button (it has its own disabled styling; drop the manual opacity 0.4). Full-width in a footer View → alignSelf:stretch not fullWidth. accessibilityLabel 'Confirm move'.
- **[JUDGMENT · danger/md]** `components/trip-plan/MoveBlockSheet.tsx:488` — "I understand — continue"
  - now: styles.moveBtnAcknowledge: backgroundColor terracotta[600], borderRadius 10, paddingV md, labelSemibold white
  - preserve: Solid terracotta acknowledge-gate (booked-block risk). Same solid-warning-fill-has-no-variant issue as ChangeStudio bookedGateBtn — danger variant is red-text-transparent, so swap changes emphasis. Design call. Mutually exclusive with the Move btn (only one renders).
- **[JUDGMENT · primary/md]** `components/trip-plan/OptimizeRouteSheet.tsx:175` — "Apply"
  - now: styles.applyBtn: flex:2, backgroundColor action.text, borderRadius 10, paddingV md, labelSemiboldMd white
  - preserve: Paired with Discard but ASYMMETRIC weighting (Apply flex:2 vs Discard flex:1) — Button's fullWidth is flex:1, so the 2:1 ratio can't be expressed via props; needs style flex:2 override or a design call to make them equal. accessibilityLabel 'Apply optimized route'.
- **[JUDGMENT · secondary/md]** `components/trip-plan/OptimizeRouteSheet.tsx:167` — "Discard"
  - now: styles.discardBtn: flex:1, borderRadius 10, paddingV md, hairline border.medium, text uses typography.h3 (unusual)
  - preserve: Bordered pill → secondary, BUT label text is styled with typography.h3 (discardBtnText), an unusually large/serif face for a button label — the shared Button uses labelSemibold, so the swap changes the type. Confirm intended. Asymmetric flex:1 vs Apply flex:2 (see above).
- **[CLEAN · tint/sm]** `components/trip-plan/PlanEmptyDay.tsx:255` — "Add" · icon add
  - now: styles.primaryBtn: flexrow, backgroundColor tint.action, borderRadius radius.full, paddingH md paddingV xs, gap xxs, add icon + labelSemiboldXs action.text
  - preserve: Textbook tint variant (subtle espresso-tint fill + action text + leading add icon). Already radius.full so pill shape converges cleanly. Icon='add' → Button icon prop. Paired with a bare-text 'Free time' in a row. accessibilityLabel 'Add something to day {n}'. Multi-action component — also has propose-mode branch (line 172) and tertiary link (275) that are NOT buttons (list-row + text-link, LEAVE).
- **[CLEAN · ghost/sm]** `components/trip-plan/PlanEmptyDay.tsx:264` — "Free time"
  - now: styles.secondaryBtn: paddingH sm paddingV xs, NO background, NO border — bare text bodySmMedium text.secondary
  - preserve: Bare tappable text label (no fill/border) → ghost. Paired next to the tint 'Add' pill. accessibilityLabel 'Block out day {n} as free time'. Currently mismatched name ('secondaryBtn' but visually tertiary).
- **[CLEAN · primary/md]** `components/trip-plan/PlanColdStart.tsx:86` — "Set dates"
  - now: styles.primaryBtn: flex:1, backgroundColor action.text, borderRadius 10, paddingV md, labelSemiboldMd white
  - preserve: Cold-start DatesPrompt primary. flex:1 inside styles.actions row (alignSelf:stretch on the row) paired with the 'Ask Vesper' secondary — flex:1 correct. accessibilityLabel 'Set trip dates'.
- **[JUDGMENT · secondary/md]** `components/trip-plan/PlanColdStart.tsx:94` — "Ask Vesper" · icon sparkles-outline
  - now: styles.secondaryBtn: flexrow center, borderRadius 10, paddingH lg paddingV md, hairline border.medium, white bg, sparkles icon + h3-styled text
  - preserve: Bordered pill → secondary with leading icon='sparkles-outline'. BUT label uses typography.h3 (secondaryBtnText) — unusually large for a button; same oversized-label concern as OptimizeRouteSheet Discard (shared idiom in this codebase). Paired flex:1 with Set dates. accessibilityLabel 'Ask Vesper for date suggestions'.
- **[CLEAN · secondary/sm]** `components/trip-plan/PlanBlockRow.tsx:880` — "Change" · icon options-outline
  - now: styles.changeButton: flexrow, gap xxs, paddingH sm paddingV xxs, borderRadius 8, hairline border.light, options-outline icon + labelSemiboldXs action.text
  - preserve: The per-block 'Change' entry point — the most-rendered CTA on the whole surface (once per block). Bordered compact pill with leading icon → secondary/sm + icon='options-outline'. Very small (paddingV xxs) so grows meaningfully to 44 pill — check it doesn't bloat dense day lists; may warrant keeping sm and accepting the min height. accessibilityLabel 'Change {block.title}'.
- **[JUDGMENT · success/sm]** `components/trip-plan/PlanBlockRow.tsx:895` — "Done" · icon checkmark
  - now: TouchableOpacity styles.doneChip: flexrow, gap xxs, alignSelf flex-start, paddingLeft 56 paddingV xs, NO bg/border, checkmark icon + labelSemiboldXs sageDeep text
  - preserve: Now-Mode 'Done ✓' — sage/olive text, no fill (deliberately 'ambient, light affordance, no filled bg' per code comment). Semantically success, but converting to a filled success pill fights the intended ambient look; and it carries a paddingLeft:56 alignment offset that a Button won't reproduce via props. Design call — may be better LEFT as ambient text. Has haptic + Undo-toast wiring on press. Only TouchableOpacity (not Tap) in the group.
- **[LEAVE · LEAVE/n/a]** `components/trip-plan/BlockChangedBanner.tsx:91` — "× (dismiss)"
  - now: bare Tap, no style — Text '×' typography.body text.tertiary
  - preserve: Icon/glyph-only dismiss chrome (× and the 'View diff →' / 'Revert' siblings at 70/79 are bare text links, not buttons). Whole banner is a ghost/attribution strip — LEAVE. Listed to record it was reviewed, not converted.
- **[JUDGMENT · primary/sm]** `components/trip-plan/ConcurrentEditBanner.tsx:95` — "Refresh"
  - now: styles.refreshBtn: paddingH md paddingV xs, borderRadius 6, backgroundColor action.text, labelSemiboldXs white
  - preserve: Small solid-espresso action inside an alert banner (borderRadius 6, very compact). Maps to primary/sm but lives in a tight inline alert row next to an icon-only close (X at 103, LEAVE) — growing to a 44 pill may overpower the banner. Design call on whether inline-banner CTAs adopt Button. accessibilityLabel 'Refresh trip plan'.
- **[LEAVE · LEAVE/n/a]** `components/trip-plan/BlockProposedBanner.tsx:137` — "Approve / Keep / Withdraw (vote toggles)"
  - now: styles.voteBtn: paddingH md paddingV xs, borderRadius 8, hairline border, stateful on-fills (planningInk/mute) when selected
  - preserve: Stateful vote toggle group (Approve/Keep with selected on-states + accessibilityState.selected), NOT plain CTAs — same species as chat VoteWidgetCard. The 'View →' sibling (163) is a bare text link. Leave as a toggle/segmented control; converting to Button would lose the selected-fill semantics.
- **[LEAVE · LEAVE/n/a]** `components/trip-plan/NowModeStrip.tsx:194` — "Walk me there / Running late / Mark done" · icon navigate-outline
  - now: styles.actionButton: flex:1 (primary flex:2), flexrow center, borderRadius 8, translucent rgba(251,247,236,0.08/0.14) fill on dark ink card, captionMedium translucent text
  - preserve: Dark-card live-action row: translucent-on-ink fills, custom disabled color, asymmetric flex 2:1, all-custom light-on-dark palette that none of Button's variants (espresso/olive/red on light) match. Deliberate distinct species for the NOW card — LEAVE. Converting would break the dark theme.
- **[JUDGMENT · ghost/sm]** `components/trip-plan/PlanDaySection.tsx:441` — "＋ Add something"
  - now: styles.addToDayBtn: alignSelf flex-start, paddingV xs paddingLeft 16, NO bg/border — bare text labelSemiboldXs text.tertiary (glyph ＋ in the string)
  - preserve: Per-day add affordance, deliberately quiet (tertiary text, no fill, hard-left aligned under the day). Reads as ghost, but the '＋' is a literal glyph in the label rather than an icon prop — convert to icon='add' + label 'Add something'. Its intentional understatement (text.tertiary) may not survive a ghost pill; design call. accessibilityLabel 'Add to this day'.

## trip-proposal-settings

_Across components/trip/ and components/trip-settings/, the proposal/decision surface is already largely migrated: ProposalReceipt.tsx and ProposalDetailScreen.tsx route every primary decision action (Approve/Decline/Withdraw/Retry/Review-in-Plan/organizer Approve-&-apply/vote/revert) through the shared <Button> — including the destructive danger "Decline" and ghost "Withdraw" — so those are NOT counted below. trip-settings/TripSettingsKit.tsx has ZERO hand-rolled CTAs: its destructive leave/delete actions are TripSettingsRow list rows (Tap-wrapped rows with chevrons/toggles), and TripStatusPill is the already-migrated StatusPill — leave all of it alone. That leaves ~9 genuine hand-rolled CTAs, clustering in two shared pill styles. (1) `secondaryPillInline` (tripFolioStyles.ts:1004 — bordered soft pill, bodySmMedium action text, alignSelf:flex-start) appears 4x with identical role ("Open story"/"Open timeline"/"Open itinerary") → all CLEAN secondary/sm swaps. (2) two solid-fill dark `planningInk` pills — `buildButton` (hero "Build the trip" with sparkles + h3 label) and `vesperCta` (folioCta text, role=link) — map to primary but need JUDGMENT (they use planningInk not action.primary espresso, and non-standard/large label typography, so the swap changes fill color + label size). The remaining bare-text actions ("Ask", "Select all", "Manage selection", "Resolve conflicts →") are ghost-variant candidates but sit at sub-13px caption/xs sizes and sub-44 heights that will grow to the 44px pill — flagged JUDGMENT. EXCLUDED as non-CTAs and folded here: TripHeader IconButton chrome + h2 title-tap; all TripFolioHome document-section rows (682/699/762), start-slots (860), facet cards (1183/1261), section-header text-links (2186/2216) and day/feed list rows (2282/2679/2773); ChoosePlaceSheet arrow-icon + saved/suggest list rows; BlockWhyRow "Why this?" disclosure toggle; LeaveByHintStrip close-X; the deep-link/affected-block nav rows and back-chrome in ProposalDetailScreen. FolioReceiptCard.tsx has no Taps at all._

- **[JUDGMENT · primary/md]** `components/trip/TripFolioHome.tsx:830` — "Build the trip" · icon sparkles
  - now: solid planningInk fill, radius.full pill, h3 (14px) white label, sparkles leading icon, paddingVertical lgl, marginTop xl
  - preserve: HERO cold-start CTA. Fill is colors.trips.planningInk (dark planning ink), NOT action.primary espresso — swapping to primary changes the fill hue; confirm design wants espresso here. Label is typography.h3 (14px medium) which is LARGER/different weight than Button md's 15px semibold — a visible label-typography change. Leading sparkles icon maps to icon='sparkles'. No a11yLabel (falls back to visible 'Build the trip'). Keep marginTop:xl via style; sits above a coldNote caption.
- **[JUDGMENT · primary/sm]** `components/trip/TripFolioHome.tsx:621` — "{ctaLabel} (dynamic Vesper CTA)"
  - now: solid planningInk fill, radius.full pill, folioCta (12.5px semibold) paper label, alignSelf:flex-end, paddingH lg / paddingV sm
  - preserve: accessibilityRole is 'link' NOT 'button' — Button hardcodes role=button; confirm the role change is acceptable. Fill = surface.planningInk (dark), not espresso — hue changes on swap. Label uses typography.folioCta (12.5px, letterSpacing 0) vs sm's bodySmMedium 13px — minor size shift. Right-aligned (alignSelf:flex-end) must be preserved via style. Dynamic label from ctaLabel prop.
- **[CLEAN · secondary/sm]** `components/trip/TripFolioHome.tsx:2172` — "Open timeline"
  - now: secondaryPillInline: bordered soft pill (cardSoft bg + hairline border), radius.full, bodySmMedium action.text label, alignSelf:flex-start
  - preserve: Shared secondaryPillInline style (tripFolioStyles.ts:1004). bodySmMedium (13px) == sm label. Border+transparent-ish fill == secondary. Preserve alignSelf:flex-start via style. Radius already full pill so no shape change. Empty-timeline fallback CTA.
- **[CLEAN · secondary/sm]** `components/trip/TripFolioHome.tsx:2652` — "Open itinerary"
  - now: secondaryPillInline: bordered soft pill, radius.full, bodySmMedium action.text label, alignSelf:flex-start
  - preserve: Same shared secondaryPillInline style as line 2172. CLEAN secondary/sm swap; keep alignSelf:flex-start. Live-mode empty fallback.
- **[CLEAN · secondary/sm]** `components/trip/TripFolioPostTrip.tsx:57` — "Open story"
  - now: secondaryPillInline: bordered soft pill, radius.full, secondaryPillText (bodySmMedium action.text), alignSelf:flex-start
  - preserve: Same shared secondaryPillInline/secondaryPillText style. CLEAN secondary/sm. Empty-moments fallback CTA in PostTripKeepsake.
- **[CLEAN · secondary/sm]** `components/trip/TripFolioPostTrip.tsx:128` — "Open story"
  - now: secondaryPillInline: bordered soft pill, radius.full, secondaryPillText label, alignSelf:flex-start
  - preserve: Duplicate of line 57 in the BackendPostTripKeepsake empty branch. onPress is pressFor(keepsake.primary_action) — preserve the dynamic handler. CLEAN secondary/sm.
- **[JUDGMENT · ghost/sm]** `components/trip/BlockedActionRow.tsx:38` — "Ask"
  - now: bare amber text (bodySmMedium, surface.amber), no fill/border, hitSlop 8, minTarget='auto', flexShrink:0 inside a bordered row
  - preserve: accessibilityLabel is distinct from visible text ('Ask {name} to {action}' vs label 'Ask') — MUST pass accessibilityLabel to preserve. Uses minTarget='auto' (compact, sub-44) — Button's sm grows to 44px minTouchTarget, which will enlarge the tap area and may push the row taller; verify row layout. Text color is surface.amber (not action.text) — ghost's action-text color is a hue change, confirm amber is intended vs generic ghost.
- **[JUDGMENT · ghost/sm]** `components/trip/FindPhotosSheet.tsx:308` — "Select all / Deselect all"
  - now: bare text (captionMedium 12px action.text), no fill/border, paddingV sm / paddingH md, in header meta row
  - preserve: Label toggles between 'Select all' and 'Deselect all' by selection state — dynamic. captionMedium is 12px, SMALLER than sm's 13px bodySmMedium — swapping grows the label. No explicit min-height now; Button sm adds 44px min target which may enlarge the header row. Right-aligned in a space-between header meta row.
- **[JUDGMENT · ghost/sm]** `components/trip/FindPhotosSheet.tsx:324` — "Manage selection"
  - now: bare text (captionMedium 12px action.text), no fill/border, paddingV xs / paddingH sm, in count row
  - preserve: Distinct accessibilityLabel ('Manage which photos Vesper can see') vs visible 'Manage selection' — MUST preserve. captionMedium 12px < sm 13px (label grows). Very compact padding (xs/sm) → 44px min target will noticeably enlarge; only renders in isLimited photo-permission state.
- **[JUDGMENT · ghost/sm]** `components/trip/proposal-detail/ProposalDetailScreen.tsx:784` — "Resolve conflicts →"
  - now: bare text (labelSemiboldXs 12px action.text) with trailing → glyph, no fill/border, marginTop xs, alignSelf:flex-start, inside reverted-banner
  - preserve: Label embeds a trailing '→' arrow glyph — decide whether to drop it (Button has no trailing-icon slot; icon prop is LEADING only) or keep it in the label string. accessibilityLabel 'Resolve conflicts' differs from visible 'Resolve conflicts →' — preserve. labelSemiboldXs is 12px < sm 13px. Only shown for revertMode==='diff_safe_partial'; onPress=onResolveConflicts (guarded optional). Keep alignSelf:flex-start.

## money

_Two directories, two hand-rolled button PRIMITIVES that dominate the surface. In components/expense/, CostsPrimitives.tsx exports `CostsReceiptButton` (a View pill: borderRadius:999, tone fill or ghost-border, 12px semibold text) wrapped in a `Tap` at 3 call sites (CostsEmptyState:65 add-first-expense, CostsBalanceSheet:58 settle-footer, CostsHeader:61 attention-action). Migrating the primitive once carries all three; each maps to primary (fill) or secondary (ghost). In components/stay/, StayCard.tsx exports `StayButton` (the design's SBtn: Tap pill, radius:999, 13px semibold, fill or ghost border at `${tone}55`) used at ~10 call sites across StayCard, StayHome, StayCompare. These two primitives are the real work — ~13 CTAs collapse to two component swaps. ALREADY MIGRATED (exclude): AddExpenseSheet:674 and EditExpenseSheet:113 primaries both route through StickySheetActionBar, which already wraps canonical Button (verified). Secondary long-tail: many inline `<Text onPress>` tertiary actions (StayCompare Vote/Hold/Book-this/nudge/add-option lines, StayHome, StayRow action labels, StayCompare:256 View-stay) — bare text actions that map to ghost but several are inline-in-row text (not pill buttons) and warrant JUDGMENT/LEAVE. Destructive/settle actions in ExpenseDetail (settleBtn:293, deleteBtn:376) are bespoke bordered/text buttons needing JUDGMENT (olive success + terracotta danger, loading/disabled wiring). CC2 overlap: StayCard is on the card-chrome list — its embedded StayButton CTAs (StayCard:186/292/296) should be coordinated with the CC2 card pass, not converted in isolation. Excluded as non-buttons: all icon-only chrome (ExpenseDetail editBtn:208, close/remove X, sendBtn:358), status pills/kickers (StayMono, CostsKicker, TAG badges), CostsLedgerRow (list row), StayRow's outer row (tappable list row). Caps applied; trivia folded here._

- **[JUDGMENT · primary/sm]** `components/expense/CostsPrimitives.tsx:44` — "CostsReceiptButton (shared primitive)"
  - now: View pill radius:999, paddingH lg/paddingV sm, fill=tone OR ghost=transparent+hairline border tint(tone,0.34); text 12px sans_semibold, cardWarm on fill / tone on ghost
  - preserve: Keystone: one primitive, 3 call sites (CostsEmptyState:65 fill/ink, CostsBalanceSheet:58 fill-or-ghost by variant, CostsHeader:61 fill/tone). Parameterized by tone (goldDeep/amber/planningInk/ink) + ghost bool — Button is fixed-palette espresso, so per-tone coloring is the human call. 12px/paddingV-sm = sub-44 height, grows to 44. ghost=true->secondary, ghost=false->primary. `full` prop -> alignSelf:stretch NOT fullWidth. Wrapped in Tap for onPress+haptic.
- **[CLEAN · primary/md]** `components/expense/CostsEmptyState.tsx:57` — "Add first expense"
  - now: Tap(primaryTap: alignSelf:stretch) wrapping CostsReceiptButton tone=ink full
  - preserve: Full-width in a column (primaryTap alignSelf:stretch) — use style={{alignSelf:'stretch'}}, NOT fullWidth. accessibilityLabel 'Add first expense' == visible. haptic='medium'. Solid ink fill -> primary. Depends on CostsReceiptButton primitive migration.
- **[JUDGMENT · primary/md]** `components/expense/CostsBalanceSheet.tsx:57` — "model.footerLabel (settle/close footer)"
  - now: Tap(footerTap) wrapping CostsReceiptButton tone=FOOTER_TONE ghost={variant==='owed'} full
  - preserve: Variant flips ghost<->fill by model.variant: 'owed'->ghost(secondary), 'owe'/'mixed'->fill(primary). disabled={!onFooterPress} must be preserved. full -> alignSelf:stretch. tone goldDeep/amber/planningInk off-canon — needs tone decision. haptic='medium'.
- **[JUDGMENT · tint/sm]** `components/expense/CostsBalanceSheet.tsx:129` — "row.actionLabel (per-row settle chip)"
  - now: inline View rowAction minHeight:30 radius:15, fill=tone(settle) OR ghost border; 11.5px sans_semibold; wrapped in Tap only when actionable
  - preserve: Compact in-row action inside 76px balance row; 30px+11.5px grows to 44px sm pill, may blow row layout. Only wrapped in Tap when isActionable (onPress && requiresCurrentUserPayment); non-actionable branch renders a bare status chip View — do NOT convert that branch. accessibilityLabel composed `${actionLabel} ${amountLabel}` differs from visible. Could be LEAVE if judged a chip.
- **[CLEAN · primary/sm]** `components/expense/CostsHeader.tsx:53` — "attention.actionLabel"
  - now: Tap(actionTap) wrapping CostsReceiptButton tone=ATTENTION_TONE (non-full pill)
  - preserve: Compact non-full pill beside attention copy (flexShrink:0). tone by state (goldDeep/amber/planningInk) — inherits CostsReceiptButton tone question. accessibilityLabel == actionLabel. haptic='light'. Only renders when onAttentionPress present.
- **[JUDGMENT · success/md]** `components/expense/ExpenseDetail.tsx:293` — "Mark my share as settled" · icon checkmark-circle-outline
  - now: Tap(settleBtn) bordered pill borderWidth:1 olive[400] radius.input paddingV lg; icon checkmark-circle-outline + olive[600] text; ActivityIndicator when settling
  - preserve: Olive outlined confirm -> success intent, but current is outlined not tinted-fill; visual call whether success fill reads right. loading: renders ActivityIndicator + opacity:0.6 while settling, disabled={settling} -> Button loading/disabled. accessibilityLabel == visible. Leading Ionicon via icon prop.
- **[JUDGMENT · danger/md]** `components/expense/ExpenseDetail.tsx:376` — "Delete expense" · icon trash-outline
  - now: Tap(deleteBtn) transparent no border paddingV lg; trash-outline icon + terracotta[400] 13px text; opacity:0.5 when deleting
  - preserve: Destructive -> danger (red text transparent) matches current terracotta-on-transparent. disabled={deleting}+opacity:0.5 -> Button disabled/loading. Destructive semantics = mandatory human review. accessibilityLabel == visible. haptic='medium'. Leading trash icon via icon prop.
- **[JUDGMENT · secondary/md]** `components/expense/AddExpenseSheet.tsx:417` — "Scan receipt" · icon camera-outline
  - now: Tap(scanBtn) dashed border (borderStyle:dashed border.medium) radius.card centered row; camera-outline icon + secondary body text
  - preserve: Deliberate DASHED-border scan/dropzone affordance — canon Button is solid pill, converting loses the dashed cue; visual call, possibly LEAVE. accessibilityLabel 'Scan receipt' == visible. Leading camera icon. Only shown when !pickedImageUri.
- **[JUDGMENT · ghost/sm]** `components/expense/AddExpenseSheet.tsx:452` — "Try again"
  - now: Tap wrapping bare Text (receiptRetryText action.text labelSemiboldXs) — no fill/border
  - preserve: Bare inline text action inside receipt-failed status block; not pill-shaped. Maps ghost but tiny inline text — a 44px sm pill disrupts inline status layout. accessibilityLabel 'Try scanning receipt again' DIFFERS from visible 'Try again' — must preserve. Could be LEAVE.
- **[JUDGMENT · primary/sm]** `components/stay/StayCard.tsx:31` — "StayButton / SBtn (shared primitive)"
  - now: Tap pill radius:999, fill=tone OR ghost=transparent+1px border `${tone}55`; text 13px sansSemibold, cardRaise on fill / tone on ghost; full -> alignSelf:stretch+paddingV12/H0 else paddingV9/H16
  - preserve: Stay keystone: one primitive, ~10 call sites. Parameterized tone (ink/gold/amber) + ghost — same fixed-palette tension as CostsReceiptButton (ink~=primary; amber/gold off-canon). ghost=true->secondary, ghost=false->primary. 13px+paddingV9 sub-44, grows to 44. `full`=alignSelf:stretch NOT fullWidth. CC2 overlap: StayCard on card-chrome list. children is ReactNode — Button label is string-only, verify callers pass plain text.
- **[JUDGMENT · primary/sm]** `components/stay/StayCard.tsx:186` — "primary || 'Add somewhere to stay →'"
  - now: StayButton tone=gold (missing-variant dashed card CTA)
  - preserve: Inside 'missing' dashed-card variant of StayCard (CC2 card-chrome overlap — classify but defer to CC2). tone=gold off-canon. Label carries trailing '→' glyph in text — decide keep-in-label vs icon prop. onPress=onPrimary.
- **[JUDGMENT · primary/sm]** `components/stay/StayCard.tsx:291` — "primary + optional secondary (card action row)"
  - now: row gap:14: StayButton tone=pTone (primary) + optional Tap>Text (secondary 12.5px mute)
  - preserve: PAIRED: StayButton primary (pTone default ink) next to bare-Text secondary (StayCard:296, mute text no fill). Asymmetric pairing = human call on alignment/sizing. Secondary is inline text (ghost) not a pill. Inside StayCard body -> CC2 overlap. onPrimary/onSecondary wiring.
- **[CLEAN · primary/md]** `components/stay/StayHome.tsx:144` — "+ Add somewhere to stay / + Add the booking (+ ghost Save-option)"
  - now: StayButton tone=ink fill then optional StayButton ghost tone=ink stacked with Gap(10)
  - preserve: Repeated across missing(144/150) and target(179/185): ink fill primary + stacked ghost 'Save an option to compare' (secondary). Stacked in a column — if full width needed use alignSelf:stretch not fullWidth. Leading '+' in label text. Clean once StayButton primitive lands; ink == espresso primary/secondary.
- **[JUDGMENT · primary/md]** `components/stay/StayHome.tsx:241` — "Open booking details + Message {booker}"
  - now: row gap:10: StayButton full tone=ink wrapped in flex:1 View (primary) + optional StayButton ghost tone=ink (secondary)
  - preserve: PAIRED flex row: primary is `full` but nested in <View style={{flex:1}}> (flex lives on wrapper) — keep flex on wrapper and drop full/use alignSelf:stretch; do NOT set Button fullWidth (fights sibling). Secondary ghost only when booker!=='You'. Asymmetric optional second button = judgment.
- **[JUDGMENT · primary/sm]** `components/stay/StayCompare.tsx:178` — "Book this / Vote (candidate card actions)"
  - now: StayButton tone=ink 'Book this' (decided leader) OR StayButton tone=amber 'Vote'; plus inline Text 'Hold' (:171) and '✓ YOUR PICK' StayMono status
  - preserve: Mutually-exclusive states in one slot: 'Book this' (ink->primary), 'Vote' (amber->tint/success, amber off-canon), 'Hold' (bare Text onPress :171 -> ghost, inline not pill), 'YOUR PICK' (StayMono status pill = LEAVE). Compact cards (cardWidth 168 in 3+ scroll) — 44px sm pills may crowd. tone=amber decision. StayButton children are plain strings here.
- **[LEAVE · ghost/sm]** `components/stay/StayCompare.tsx:256` — "View stay → / Nudge → / + Add another option"
  - now: bare <Text onPress> lines 12.5px sansSemibold color gold/amber/mute; NOT pill-shaped, no fill/border
  - preserve: Three inline text-link actions (StayCompare:256 View-stay gold, :376 Nudge amber, :389 Add-option mute) as raw Text with onPress — deliberately NOT buttons (no fill/border/pill). Converting to sm pills breaks the quiet-link grammar. Recommend LEAVE (ghost only if design wants buttonized). Trailing '→'/'+' glyphs in label. StayRow:177 action label is the same species (also LEAVE).

## group-booking

_Across the three groups I found ~18 hand-rolled tappables that render a text label and read as buttons; I'm reporting the 15 most load-bearing and folding the rest here. NONE currently use the shared <Button> — every CTA is a bare `Tap` (components/ui/Tap) with an inline StyleSheet pill. Two full "button kit" style blocks (inlinePrimaryBtn / receiptActionBtn / inlineSecondaryBtn / inlineDisabledBtn) are duplicated verbatim across BookingSessionSurfaces.tsx and BookingCheckoutPanels.tsx (and partly BookingOfferRow.tsx), so a Button migration collapses a lot of dead style. Booking is built-dark for v1 (flag off) — all booking CTAs are marked lower priority in risk_notes even where disposition is CLEAN. EXCLUSIONS I made deliberately: the People RolePill (PeoplePills.tsx:10, bordered mono caps — the audit's ruled non-Button species, LEAVE, not listed below); MemberRosterRow (MemberRows.tsx:71, whole-row Tap → list row, not a CTA); DecisionInlineRow (DecisionPrimitives.tsx:56, whole-row navigation Tap → list row); OfferRow itself (BookingOfferRow.tsx:72, the whole offer card is a selectable Tap → list row / selection surface, not a button); the per-offer refresh Tap (BookingOfferRow.tsx:122, icon-only chrome); BookingStatusChip / tradeOff pills / trust chips (status pills, not buttons); the CheckoutConsentPanel terms-accept row (BookingCheckoutPanels.tsx:139, accessibilityRole=checkbox — a checkbox, LEAVE). The single most important non-mechanical call is the paired Accept/Decline footer in BookingProposalCard (flex:1 tinted-outline buttons using olive/terracotta) — those want success + danger variants but the current 50/50 paired layout and tinted-fill aesthetic needs a human sign-off before swapping. Booking's confirm/hold and provider-handoff triad also carry disabled/loading text-swap wiring ("Confirming…"/"Saving…") that must map onto Button's `loading` prop, and most booking primaries embed a trailing arrow-forward Ionicon that Button has no trailing-icon slot for (Button icon is leading-only) — that's a real JUDGMENT snag for the whole booking set._

- **[JUDGMENT · primary/sm]** `components/people/PeoplePills.tsx:33` — "Follow / Following"
  - now: radius.full pill, minHeight 30, paddingHorizontal lg; two states: followAction = solid ink bg + cardWarm text (12px sans_semibold), following = cardSoft bg + hairline border + mute text
  - preserve: Toggle button with TWO visual states from one component: unfollowed=solid (primary) vs following=outlined/quiet (secondary or ghost) — a single Button variant can't express both, needs a state-conditional variant. accessibilityLabel diverges from visible text (label is 'Follow'/'Following'/'Unfollow' depending on following+onPress; visible text only 'Follow'/'Following') — MUST preserve. Also carries accessibilityState selected/disabled, hitSlop={8}, disabled+opacity styling, and disabled=(disabled||!onPress). Sub-44 height (30) will grow to Button's 44 — verify it still fits the roster-row/profile-header inline slot. 13px-ish label maps to sm.
- **[JUDGMENT · ghost/md]** `components/people/MemberActionSheet.tsx:68` — "action.label (dynamic; destructive variant)"
  - now: full-width sheet action row: paddingH xxl / paddingV lg, hairline bottom border, no fill/radius; bodySm ink label (h3 fontFamily), destructive→oxbloodDeep; optional description sub-line
  - preserve: Action-sheet rows, not pills — they're full-bleed bordered list rows with an optional secondary description line and a destructive color branch. This is a distinct sheet-row species; converting to Button loses the two-line label+description layout and the row divider. If migrated, destructive rows → danger, others → ghost, but likely better LEFT as a bespoke sheet row. accessibilityLabel = action.label (matches). onPress wraps onClose()+action.onPress() ordering — preserve.
- **[JUDGMENT · ghost/md]** `components/people/MemberActionSheet.tsx:86` — "Cancel"
  - now: bare text row, paddingH xxl paddingTop lg, no fill/border/radius; bodySm mute text
  - preserve: Sheet dismiss affordance — bare muted text, not a pill. Pairs with the action rows above as the same sheet-row species; classify with them. If the sheet stays bespoke, LEAVE; if converted, ghost/md. No accessibilityLabel divergence (label='Cancel').
- **[JUDGMENT · ghost/sm]** `components/collaboration/DecisionPrimitives.tsx:117` — "Details" · icon arrow-forward
  - now: text + trailing arrow-forward(13); minHeight 30, paddingH sm; captionMedium planningInk text, no fill/border
  - preserve: Bare text tertiary action in a receipt-card header. accessibilityLabel='View proposal details' DIVERGES from visible 'Details' — MUST preserve. Trailing arrow-forward icon has no Button slot (leading-only) — dropping/relocating it is a visual call. Sub-44 height (30). Small caption-weight label → sm.
- **[JUDGMENT · ghost/sm]** `components/collaboration/DecisionPrimitives.tsx:149` — "Continue privately (default; action prop overridable)" · icon arrow-forward
  - now: alignSelf flex-start, no fill/border/radius; captionMedium planningInk text + trailing arrow-forward(13); paddingTop xs
  - preserve: Bare tertiary text action inside PrivateSeam card. Label is a prop (default 'Continue privately'), accessibilityLabel={action} tracks it (no divergence). Trailing arrow-forward has no Button leading-icon equivalent. No height set (intrinsic) — will jump to 44 as a Button, changing the seam card's compact rhythm; verify.
- **[JUDGMENT · primary/md]** `components/booking/BookingCheckoutPanels.tsx:155` — "vocabulary.bookLabel / 'Confirming…' when pending" · icon arrow-forward
  - now: receiptActionBtn: alignSelf STRETCH, minHeight 42, radius.pill, solid ink bg, paper text (labelSemiboldMd) + trailing arrow-forward(15); inlineDisabledBtn opacity 0.6 when pending
  - preserve: LOWER PRIORITY (booking built-dark, flag off). Primary checkout CTA. pending drives BOTH a label swap ('Confirming…') AND disabled+opacity — map onto Button loading+disabled (label swap must be preserved or handled via loading). Trailing arrow-forward has no Button slot. Uses alignSelf:stretch in a column (correct pattern; do NOT use fullWidth). accessibilityLabel=vocabulary.bookLabel matches base label. 42→44 height is canon-convergent.
- **[JUDGMENT · secondary/sm]** `components/booking/BookingCheckoutPanels.tsx:165` — "Hold instead" · icon time-outline
  - now: inlineSecondaryBtn: alignSelf flex-start, minHeight 38, radius.pill, cardWarm bg + hairline border, goldDeep text (labelSemiboldSm) + trailing time-outline(14); opacity 0.6 when pending
  - preserve: LOWER PRIORITY (booking dark). Outlined secondary paired under the primary confirm. goldDeep text is a gold-tinted secondary, not the canon action color — variant/color is a visual call. Trailing time-outline icon (no Button trailing slot). disabled=pending + opacity. Sub-44 (38) grows to 44. Label size labelSemiboldSm → sm.
- **[JUDGMENT · primary/md]** `components/booking/BookingCheckoutPanels.tsx:219` — "I booked it" · icon checkmark
  - now: inlinePrimaryBtn: alignSelf flex-start, minHeight 42, radius.pill, solid ink bg, paper text + trailing checkmark(15)
  - preserve: LOWER PRIORITY (booking dark). First of a 3-button provider-return stack (handoffActionGrid, gap sm). Semantically a 'confirmed' action — could be success rather than primary; that's a visual call. Trailing checkmark icon (no Button trailing slot). alignSelf flex-start inside a column stack — for full-width stack use alignSelf:stretch. No accessibilityLabel (falls back to text 'I booked it').
- **[CLEAN · secondary/sm]** `components/booking/BookingCheckoutPanels.tsx:223` — "Still deciding"
  - now: inlineSecondaryBtn: minHeight 38, radius.pill, cardWarm bg + hairline border, goldDeep text (labelSemiboldSm)
  - preserve: LOWER PRIORITY (booking dark). Second in the return-stack. Plain outlined secondary, no icon, no disabled wiring — mechanical swap; only canon change is 38→44 height and goldDeep→action text color. No accessibilityLabel (uses text).
- **[JUDGMENT · secondary/sm]** `components/booking/BookingCheckoutPanels.tsx:226` — "It failed"
  - now: inlineSecondaryBtn: minHeight 38, radius.pill, cardWarm bg + hairline border, goldDeep text
  - preserve: LOWER PRIORITY (booking dark). Third in the return-stack. Reads semantically negative ('It failed') but is styled identically to 'Still deciding' — could arguably be danger; the current design deliberately keeps it neutral-secondary, so variant is a human call. Paired-stack sibling of the two above.
- **[JUDGMENT · primary/md]** `components/booking/BookingCheckoutPanels.tsx:270` — "Add to trip / 'Saving…' when saving" · icon book-outline
  - now: inlinePrimaryBtn (+inlineDisabledBtn): alignSelf flex-start, minHeight 42, radius.pill, solid ink bg, paper text + trailing book-outline(15)
  - preserve: LOWER PRIORITY (booking dark). Capture-stage save primary. saving drives label swap ('Saving…') + disabled + opacity → Button loading+disabled. accessibilityLabel='Save provider confirmation' DIVERGES from visible 'Add to trip' — MUST preserve. Trailing book-outline icon (no Button trailing slot).
- **[JUDGMENT · primary/md]** `components/booking/BookingCheckoutPanels.tsx:300` — "Open provider" · icon open-outline
  - now: inlinePrimaryBtn: alignSelf flex-start, minHeight 42, radius.pill, solid ink bg, paper text + trailing open-outline(15)
  - preserve: LOWER PRIORITY (booking dark). accessibilityRole='link' (not button) and accessibilityLabel='Open provider' (matches text) — opens an external provider URL, so the link role is intentional; Button defaults to button role, preserve link semantics. Trailing open-outline icon (no Button trailing slot).
- **[CLEAN · primary/md]** `components/booking/BookingSessionSurfaces.tsx:81` — "actionLabel ('Refresh' | 'Try again')" · icon arrow-forward
  - now: inlinePrimaryBtn: alignSelf flex-start, minHeight 42, radius.pill, solid ink bg, paper text + trailing arrow-forward(15)
  - preserve: LOWER PRIORITY (booking dark). Recovery-card primary; onPress branches refresh vs retry on recovery.action. Label is dynamic but accessibilityLabel=actionLabel (matches). Only snag is the trailing arrow-forward icon (no Button trailing slot); otherwise mechanical, 42→44 canon-convergent. No disabled/loading wiring.
- **[JUDGMENT · primary/md]** `components/booking/BookingSessionSurfaces.tsx:248` — "actionLabel (dynamic reservation action)" · icon arrow-forward
  - now: receiptActionBtn: alignSelf flex-start, minHeight 40, radius.pill, solid ink bg, paper text (inlinePrimaryText) + trailing arrow-forward(15); inlineDisabledBtn when actionDisabled
  - preserve: LOWER PRIORITY (booking dark). ReservationReceipt primary; only rendered when not confirmed AND onAction present (else falls back to a plain 'Next:' hint Text — not a button). actionDisabled → disabled+opacity, map to Button disabled. accessibilityLabel=actionLabel matches. Trailing arrow-forward (no Button slot). NOTE this file's receiptActionBtn is minHeight 40 + alignSelf flex-start, unlike the checkout file's stretch/42 — don't assume they're identical.
- **[JUDGMENT · danger/sm]** `components/booking/BookingProposalCard.tsx:295` — "Decline  +  bookLabel (paired footer)"
  - now: actionBtn: flex:1, paddingV sm, radius.lg, alignItems center; rejectBtn=terracotta 18% fill + terracotta border + terracotta600 text; acceptBtn=olive 18% fill + olive border + olive600 text (labelSemiboldSm)
  - preserve: LOWER PRIORITY (booking dark) but the HARDEST call in the set. Two paired 50/50 buttons (flex:1) in a row: Decline→danger, Accept(bookLabel)→success. Current style is tinted-fill+matching-border (olive/terracotta at 18%), NOT canon danger(transparent red text)/success(olive tint) — converting changes the look materially, needs design sign-off. Both carry disabled=mutationPending. accessibilityLabels DIVERGE: 'Reject booking proposal' / 'Accept booking proposal' vs visible 'Decline' / bookLabel — MUST preserve. Accept label is dynamic (vocabulary.bookLabel). radius.lg not pill; flex:1 paired layout must be kept (do NOT use Button fullWidth on both without the row wrapper).

## home-deck

_Three regimes: (1) the 5 FocusHome Deck faces hand-roll an IDENTICAL btn/btnFill(ink→primary)/btnQuiet(#EBE4D6 cream→tint) pill pattern (padY spacing.mdl, radius.full, labelSemiboldSm) — a copy-pasted mini design-system, the highest-value mechanical target; DeckStructuredFace centralizes it in a local `DeckBtn` helper (migrate once, fixes lines 155/156/207/275). (2) Trips-home hero CTAs mostly already route through the shared CardActionPill (out of scope); the hand-rolled ones are cream-on-dark pills that sit on dark scene overlays. (3) Vesper card faces render every CTA through ActionRow.tsx → LEAVE / CC2 card-kit overlap._

- **[CLEAN · primary/sm]** DeckPickFace:148, DeckBriefFace:88, DeckCompareFace:115, HeroProse:104, FocusHome:342 — the ink "Choose {name}"/"Open the plan"/hero pills → primary. btnFlex flex:1 is in a ROW so fullWidth is safe.
- **[CLEAN · tint/sm]** DeckBriefFace:99, DeckPickFace:160(a11y note) — cream #EBE4D6 secondary → tint.
- **[CLEAN · primary/sm]** DeckStructuredFace:53 `DeckBtn` helper (drives vote/settle/flight faces) — migrate the helper once; fill→primary, quiet→tint.
- **[JUDGMENT · primary/sm]** DeckCallFace:159 — dynamic accent bg (oxblood urgency / mute-when-expired), disabled={isExpired||isPending}. Oxblood ≠ espresso primary → D13 (on-emphasis/urgency treatment) + thread disabled.
- **[JUDGMENT · tint/sm]** DeckCallFace:172 — "Let it go" quasi-destructive cream secondary; danger-vs-tint call.
- **[JUDGMENT · tint/sm]** TripsHomeViews:116/581/614 — cream/ink "Tell Vesper a place"/"Walk me there" pills sit on DARK scene overlays; tint/primary tokens assume light surfaces → D15 (on-dark treatment). Trailing icon (Button only does leading).
- **[JUDGMENT · ghost/sm]** TripsHomeViews:769 "How did it go? →" — trailing arrow (Button leading-icon only); low-emphasis text link.
- **[LEAVE]** vesper-cards/faces/* (all via ActionRow, CC2), Deck.tsx triage bar (segmented text links).
