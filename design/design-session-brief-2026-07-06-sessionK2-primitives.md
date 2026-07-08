# Vesper Design Canon — Session K2 (FINAL): Primitive Promotion & Token Forks (2026-07-06)

Scope: the last design session of the campaign — the shared-primitive layer, plus a mechanical punch list left over from K1-R. After this session the canon is DONE: every remaining item is code-side. Honest-tracking rule applies; update the ledger AS each item lands, not at the end (K1-R did the work but never touched its OPEN rows — the ledger currently understates reality; fix that pattern here).

---

## 0. K1-R leftovers punch list (mechanical — do first, ledger rows included)

- **Delete the 30 dead component BODIES** (exports are already purged; the bodies remain as grep-bait). The zero-live-mount verification already covers them: HeroV1–V5, HeroAir, TwoTierDoc, DocAes, DeckClear, DeckDoc (trip-document-canon) · VesperQuote, VES (vesper-shared) · StarterChip, StarterGlyphs (trips-shared) · DossierBar, FieldEyebrow, VesperBy (discover-kit) · DelegationAnnotated (changes-kit) · SeamForming (onboarding-canon-seams) · ChatTop, UserSaid, PLast (onboarding-kit) · HistoryBoard (vesper-home-history) · RailEdge, RailScene, RailBare (vesper-rail-variants) · FoundRow, DevStrip, IllustratedRead, PlacePortrait (wherever defined). KEEP: HomeLoading, HistCombo, HistPhone, RailRow. Console-check touched pages.
- **Rename the card-level trio in people-collab-app**: GroupDecisionCard → GroupDecisionCardRef, GroupEventLine → GroupEventLineRef, MemberBubble → MemberBubbleRef (Chat owns the canonical versions; same Ref caption pattern as the screens).
- **Record the invite-hero decision** that was made but not written: the merged canonical landing KEPT auth's AvatarCluster hero (TripReceiptArtifact not adopted) + adopted the "Not now — set up Vesper" escape. One 02d line.
- **Truth-up the three stale OPEN rows** from K1 (items 2/3/5) to reflect what actually shipped in handoff 104 + this session.

## 1. Promote ONE Phone into design-canvas.jsx

19 Phone implementations exist in 4 families, and the two biggest families disagree on frame width (393 vs 390). The canon frame rule is **393×852**. Build the canonical `Phone` in design-canvas.jsx (bezel + status bar + dynamic island, from design-system's richest version) with `width` and `radius` props, defaulting 393/r44. Then delete the local Phone definitions file-by-file, letting pages consume the canvas one (design-canvas is already loaded by 22 pages — add the script tag to the handful that lack it). Any page whose frames render at 390 after this is CORRECT behavior — 393 is the rule; note the visual delta in the changelog rather than preserving the fork.

## 2. Promote Kicker + the board-section wrapper into shared-visual-primitives.jsx

The 4-file copy-paste Kicker family (auth-invite / people-collab / places-canon / chat-canon) collapses into one shared `Kicker`. Same for the `Sec`/board-section wrapper (14 copies) and the thrice-implemented ImplNotes board chrome — one shared `ImplBoard`. Delete locals as each page is switched. (The two-letter token atoms — M, T, Lbl, Hair — stay page-local by design; do not promote those.)

## 3. Rule the Saved/Guide row dialect vs Row System

SavedRow (saved-collections) and MemberRow (guide-reader) forked a shared new row shape (28px glyph slot, sans 14.5 w500 titles, full-bleed hairline) that contradicts the Row System grammar both pages claim to consume (serif titles, inset-divider math). Decide: (a) bless the dialect — add it to Row System as an official row type ("UtilityRow" — dense, sans-led, for management/reader lists) and have both pages cite it; or (b) restyle both onto existing Row System shapes. Recommend (a): the dialect is arguably the better mobile row for dense lists, and blessing costs one board section. Either way, fix the two pages' "consumes Row System" claims to be true.

## 4. Token-fork consolidation — the ranked list (as far as the session comfortably goes)

16 local palettes fork design-system.jsx tokens. Consolidate in this order, verifying each page renders identically (the forks drifted in places — where a forked value differs from the shared token, the SHARED token wins and the visual change is noted in the changelog): 1 vesper-chat-canon (CH) · 2 universal-search-app (US) · 3 notifications-app (NT) · 4 auth-invite-app (AU) + people-collab-app (PC) · 5 vesper-trip-settings-app (TS) · 6 vesper-proposal-detail-app (PD) · 7 Global Chrome (GC — session 5's own violation) · 8 the reader/sharing tail (GR/ES/PM/SV/DM) · 9 system boards (SS/IS) last. Method per page: add design-system.jsx to the HTML's script list before the app file; replace the local const's values with references to shared tokens (keep the local alias name so in-file references don't churn); delete fully-redundant entries. STOP when quality drops and record exactly which pages were converted — an honest partial beats a sloppy total.

## 5. Record the two bundle-tooling rules (governance, two lines)

- "Script srcs may carry ?v= query strings — any live-file tooling must strip them before existence checks" (two live files were nearly misclassified as orphans).
- "The _archive/ (or archive/) folder is historical only — never import from it; new explorations go to new top-level pages per the freeze rule."

## Definition of done

One Phone, one Kicker, one Sec/ImplBoard · row-dialect ruling recorded and claims corrected · token forks consolidated at least through rank 5 with per-page verification notes · tooling rules recorded · every skip has an OPEN row · export the final handoff. After verification, the design canon is COMPLETE — remaining campaign work is entirely code-side (alignment batches A–D).
