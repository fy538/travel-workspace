# Vesper Design Canon — Session 2 Brief: Close to 95% (2026-07-04)

Context: Session 1 (handoff 89→90) fixed both broken pages, applied 3 of 8 ownership adjudications, and recorded everything else in governance sections 02d (Ownership Adjudications) and 06b (Wedge-Critical Missing Artboards). This session executes the rest. Current coverage ≈81% of v1 routes; this session's contents ≈+14 points.

Standing rules (same as last session):
- **Governance first.** For every item, update `Vesper Canon Consolidation & Ownership.html` (flip 02d/06b statuses to APPLIED/DECIDED as you go) before touching artboards. Keep honest OPEN status on anything skipped.
- **Snap to `design-system.jsx` tokens.** Do not fork another local palette.
- **Frame width:** pick ONE phone-frame width for all new artboards this session (390 or 393 — the project currently uses both), record it as a hygiene rule in governance, and use it consistently from now on.
- Atlas remains out of scope, with one explicit exception in item 12.

---

## PHASE 1 — Execute the trip-creation decision (DECIDED: conversation-first)

**1. Trip Creation is canonically conversation-first.** The product owner has decided: do NOT draw place/date pickers. Instead:
- Rewrite the Trip Creation page banner: remove the claims "blank / place-only / dates-only / place+dates states" and "light pickers." New claim set: entry affordance · conversational capture (NewTrip with open chips) · ShapePicker · SavedBridge · draft chat · promotion ("Make it a trip") · error states · handoff to folio.
- Update the route mapping in governance: `/trip-place` and `/trip-dates` are NOT standalone picker screens in the creation flow. `/trip-dates` (editing context) is already owned by Trip Settings & Admin's DatesEdit ×5. Mark `/trip-place` as **KILL-or-fold candidate for code alignment** (the live route should become a thin conversational capture moment or be removed).
- Draw ONE small missing artboard: the **creation → folio handoff beat**. Today the handoff exists only as a voice line ("I'll open a trip home"). Draw the transition moment: the conversational thread resolving into the Trip Document cover (even as a two-frame before/after board). This closes the last gap in the creation flow.
- Flip the 02d/06b "Trip-creation model decision" row to DECIDED · conversation-first.

## PHASE 2 — Wedge-critical artboards (the drawing session core)

**2. Group agency controls (codebase: GroupAgencySheet).** Zero design exists; this is on the v1 group wedge. Owner: **Chat** (consume People & Collaboration for roster/avatar tokens, Interaction Surfaces for sheet chrome). PRODUCTIVE register — DM Sans-led, at most one italic voice line. Draw:
- The sheet itself: Vesper's posture in this group room — three levels: **Propose freely / Summarize only / Stay quiet** — with a one-line consequence description under each (what the group will and won't see Vesper do).
- **Organizer view** (can change posture) vs **member view** (sees current posture, read-only, with "ask the organizer" affordance).
- **Entry point**: where it lives in the group chat header (draw the header with the affordance visible).
- Default/first-open state (what posture a new group starts in — recommend Propose freely, since the wedge is Vesper demonstrating value in the group room).

**3. Full-screen `/profile/[userId]`.** Only a compact PublicProfileCard exists in a People & Collaboration reference board. Owner: **People & Collaboration** (in-app screen; External Sharing keeps the signed-out public shell and should reference this screen, not redraw it). Draw four states:
- **Viewing another user, not following** (follow affordance prominent)
- **Viewing another user, following** (following state + unfollow path)
- **Viewing self** (edit affordance, what-others-see framing)
- **Empty/new profile** (sparse taste, no shared trips — use State System InlineAbsence, not a custom empty)
Content model: avatar token · name · public taste phrases · shared-trips-with-you section (only mutual trips — never their full trip history; privacy seam doctrine applies) · companions/following counts. No private data of any kind.

**4. `/trips/all` list screen.** Confirmed missing everywhere. Owner: **Trips Home**, PRODUCTIVE register. Reached from the "See all N trips →" footer door. Draw:
- Default state: **Planning (dated)** section + **Dreaming (drafts)** section, rows from Row System shapes (do not invent a new row).
- A returned/past-trips section treatment (or an explicit note that past trips live in Atlas and this list is forward-looking only — decide and record which).
- Loading via State System LoadingSkeleton; empty state should be near-unreachable (a user with zero trips lands on the cold Trips Home instead) — record that suppression rule rather than drawing a dead artboard.

## PHASE 3 — State tail (one board flips four PARTIAL routes)

**5. Shared ReaderStates board.** One companion board consumed by dossier + angle + guide readers (and referenced from Discover Detail & Reader System and Guide & Collection Reader). Compose from State System components — do not invent local treatments: loading (LoadingSkeleton in reader chrome), sparse/partial dossier (InlineAbsence for missing sections), error (ErrorRecovery), offline (OfflineNotice with cached-read affordance), not-found (StateScreen). Draw them inside ReaderChrome so the reader pages can point at one canonical source.

**6. Discover feed states.** Nothing exists today. Draw: cold-start/first-run feed (what a user with no taste signal sees — this is also the post-onboarding landing), empty-city (thin content region), loading, error/offline. Use State System components inside the Discover cover layout.

**7. Changes screen states + banner re-spec.** Draw empty (no changes yet — first-visit), loading, and solo-trip variants of the Changes screen. Then **re-spec the page banner to match what is drawn**: the timeline is sectioned TODAY/EARLIER (time-based) — remove the claimed "source/phase sectioning" language rather than drawing it. Source attribution stays at row level via the existing source chips (Vesper/member/group/Atlas). Flip the governance row accordingly.

## PHASE 4 — Execute the four open adjudications from 02d

**8. Story share merge.** Trip Story owns the owner-facing share screen. Merge the two competing designs into ONE canonical screen with the union control set: **pause · revoke · new-link/rotate · preview-as-recipient · stats**. Update External Sharing's two story artboards to reference the merged screen (keep External Sharing's ownership of recipient entry + link-state taxonomy). Flip 02d to APPLIED.

**9. Photo finder dedup.** Photo & Media Intake is canonical. Reduce Trip Story artboards J–M to thumbnails + an ownership pointer, and align any remaining copy to Photo Intake's. Flip 02d to APPLIED.

**10. Discover search: ARCHIVE (decision upgraded).** New evidence from the codebase: the Discover search overlay was orphaned in production during the Universal Search migration (2026-07-01) — the app already removed this surface. Therefore: **archive all four SearchX artboards** (do not rescope), note in the Discover page that in-discover search is served by Universal Search with discover scope, and update the sx-notes Logic board or archive it with them. Flip 02d to APPLIED · ARCHIVED.

**11. Voice pointer fix (prose only).** Apply the recorded split: **Chat owns voice-in-thread; Home owns the voice button + registers.** Correct the prose pointers on BOTH pages so neither defers to the other for content it actually holds. No new artboards. Flip 02d to APPLIED.

## PHASE 5 — Kill-or-draw records + two small draws

Record every decision below in governance (06b / route mapping) so code alignment can act on it:

**12. Record KILL / FOLD decisions (no drawing):**
- **ExplanationSheet + FeedbackSheet → KILL.** The design deliberately removed "why this ▾" from the home hero; record that the code sheets should be removed at alignment time.
- **SwapBlockSheet → FOLD into Change Studio.** Already spec'd there as an action row; record fold, no standalone sheet.
- **TripDebriefSheet → FOLD into Trip Document memory settle module.** The memory-mode settle prompt already carries this job; record that the standalone code sheet folds into it.
- **`/your-map` + `/dna-card` → ASSIGN to the Atlas design file.** Both are memory artifacts (cross-trip map, Travel DNA share card) and belong to Atlas's canon, which is a separate design project. Record the assignment in the route mapping (owner: Atlas canon, external) and remove them from this file's gap list. Do not draw them here.

**13. DRAW: SectionEditSheet (story section editing).** Real v1 surface; only the post-edit state exists (Reader state H "Restore Vesper's version"). Owner: **Trip Story**. Consume Interaction Surfaces full-screen edit sheet chrome. States: editing (text region + Vesper's-version reference), dirty-dismiss warning (IS pattern), saving, save-failed (ActionFailureInline). Keep it small — one board, four states.

**14. DRAW: RevertConflictSheet.** Owner: **Proposal & Decision Detail** (it already draws the "reverted — later edits kept" receipt; this sheet is the decision moment before it). Consume the ReskinnedSheet chrome from Changes (grab handle, gold kicker, WAS/NOW strikethrough diff). States: clean revert confirm · conflict (list of later edits that depend on the reverted change, with keep/discard choice) · partial-keep result summary. One board, three states.

## Definition of done

Every 02d row APPLIED (or honestly OPEN with a reason) · 06b rows flipped to DRAWN/DECIDED · Trip Creation banner matches its artboards · new artboards exist for items 1(handoff beat), 2, 3, 4, 5, 6, 7, 13, 14 · frame-width hygiene rule recorded · export a fresh handoff bundle for coverage re-verification.
