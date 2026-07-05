# Vesper Design Canon — Consolidation Session Brief (2026-07-04)

Context: a full artboard-level audit of this project (handoff 89) against the production codebase measured ~80% coverage of the 55 v1-reachable app routes. This session closes the gap to ~95%. The Canon Index + Canon Consolidation & Ownership governance model was verified accurate — keep it that way: **for every change below, update the governance table / residue inventory in `Vesper Canon Consolidation & Ownership.html` FIRST, then do the artboard work.** Atlas remains out of scope. Snap all new work to `design-system.jsx` tokens — do not fork another local palette.

---

## PHASE 1 — Repairs (both pages currently render broken)

**1. Costs page crashes.** `costs-screens.jsx` defines `CostsHomeDense` but omits it from the `Object.assign(window, …)` export at the end of the file (~line 307). The page's `h-dense` artboard references it → ReferenceError, whole canvas blank. Add it to the export.

**2. Booking & Reservation page renders nothing.** The HTML mounts `<BookingApp/>` but no file in the project defines it — the assembly was lost. Rebuild the assembly from the existing components in `booking-kit.jsx` + `booking-screens-1/2/3.jsx` (ProposalCard ×4, SessionHeader, OfferCard/OfferCompare, TermsPreview, ReservationReceipt, ProviderHandoff, CheckoutConsent, HoldReceipt ×4, ConfirmedReceipt, FailureState ×9, StatusState ×5, StateTable, DataFields). While there: the page has **zero phone-frame screens** — draw at least one assembled `/booking/[sessionId]` session screen (offers → hold → checkout consent → confirmed) plus the v1-live slice ("mark as booked" + provider handoff; the transaction engine is feature-flagged dark and the StateTable already models `live_booking_disabled` — keep that).

## PHASE 2 — Ownership adjudications (record each in the governance table)

**3. Trip settings is designed twice.** Trust & Controls block 05 ("Controls for this trip", serif ledger style) vs Trip Settings & Admin (DM Sans, 3 role variants, complete). Decision: **Trip Settings & Admin wins.** Demote T&C block 05 to an appendix with a pointer.

**4. Productive sheets violate the LOCKED Interaction Surfaces doctrine.** Stay's StaySheet ×7, Costs' AddSheet/ExpenseDetail/BalanceSheet render values in serif+gold; Interaction Surfaces (LOCKED) mandates DM Sans leads all productive overlays — the project currently contains two different canonical Add-expense designs (Costs AddSheet vs IS flow #1). Decision: **IS wins.** Reskin the Stay/Costs sheet values to DM Sans; at most one serif voice moment per sheet.

**5. Save glyph conflict.** Places uses ♡ hearts in circular containers; Saved & Collections mandates "bookmark glyph only, never a heart"; Guide Reader bans circular icon containers. Decision: **bookmark.** Fix the venue/experience heroes in `places-canon-app.jsx`.

**6. Guide chrome drawn in two places.** Places' Guide+Angle reference board draws its own reader chrome; Guide & Collection Reader owns that screen. Reduce the Places board to a pointer.

**7. Story share designed twice with different controls.** External Sharing (copy/rotate/revoke/preview-as-recipient) vs Trip Story (pause/revoke/new-link/stats). Merge into ONE canonical owner-share screen with: pause, revoke, new-link/rotate, preview-as-recipient, stats. Ownership per charter: **Trip Story owns the owner-facing share screen; External Sharing owns recipient entry + link-state taxonomy** and references the merged screen.

**8. Photo finder designed twice with divergent copy.** Trip Story artboards J–M vs Photo & Media Intake (the charter owner). **Photo Intake is canonical**; Trip Story keeps thumbnails + a pointer; align copy to Photo Intake's.

**9. Discover's search artboards are pre-Universal-Search.** The four SearchX artboards' own spec text claims global scope ("reaches everything Vesper knows"), contradicting the retrofitted canon banner. **Rescope them to discover-only reading search** (update the sx-notes Logic board too) — or archive them if discover-scoped search isn't a v1 surface. Universal Search owns global.

**10. Voice ownership pointer loop.** Home's prose defers the voice world to Chat, but the voice screens (Calm Listening, Editorial Transcript, pivot-to-text) live on the Home canvas; Chat has one mixed thread artboard. Voice is dark for v1, so this is a prose fix only: pick the split (suggest: Chat owns voice-in-thread; Home owns the voice button + registers) and correct the pointers on BOTH pages.

## PHASE 3 — Wedge-critical missing artboards (draw these)

**11. Group-chat facilitator / agency controls.** Zero design exists for what the codebase calls GroupAgencySheet — this is on the v1 group wedge. Owner: Chat (People & Collaboration for roster context). Cover: what Vesper may do in the group room (propose / summarize / stay quiet), organizer vs member control, and the entry point in the group chat header.

**12. Full-screen `/profile/[userId]`.** Only a compact PublicProfileCard exists in a People & Collaboration reference board. Profiles + follow are v1-IN. Owner: People & Collaboration. States: viewing self vs other, following vs not, empty profile.

**13. `/trips/all` list screen.** Confirmed missing everywhere — only the "See all N trips →" footer door exists. Owner: Trips Home, PRODUCTIVE register. Content per codebase: Planning (dated) + Dreaming (drafts) sections.

**14. Trip-creation model decision.** The page banner claims "blank / place-only / dates-only / place+dates states + light pickers," but the 14 artboards follow a conversation-first model — no place or date picker is drawn anywhere, and the folio handoff is a voice line. Decide: (a) draw the light pickers, or (b) declare conversation-first canonical and rewrite the banner + route notes. Note: `/trip-place` and `/trip-dates` are live routes in the codebase; Trip Settings & Admin's DatesEdit ×5 already covers dates editing.

## PHASE 4 — If time remains

- Shared **ReaderStates** board (loading/empty/error/sparse for dossier + angle + guide, composed from State System components) — one board covers three PARTIAL routes.
- **Discover feed cold-start/empty/loading** — nothing exists.
- **Changes screen**: empty/loading/solo states; and either draw the claimed source/phase sectioning or re-spec the banner to the TODAY/EARLIER model actually drawn.
- Kill-or-draw list (make the call explicit in governance; don't draw silently): ExplanationSheet + FeedbackSheet (design already removed "why this ▾" from the hero — recommend recording KILL so the code sheets get removed), SectionEditSheet (recommend DRAW — story editing is real), RevertConflictSheet (small, DRAW), SwapBlockSheet (fold into Change Studio, already spec'd there), TripDebriefSheet (recommend KILL or fold into Memory settle module).
- Assign `/your-map` and `/dna-card` an owner (Atlas design file, or two small artboards here) — currently unowned by any page.

## Definition of done

Governance table updated with every decision above · Costs + Booking pages render · each conflict has exactly one owner · Phase 3 artboards exist → export a fresh handoff bundle.
