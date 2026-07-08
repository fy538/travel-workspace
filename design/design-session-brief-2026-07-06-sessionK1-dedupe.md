# Vesper Design Canon — Session K1: Component Dedupe & Ownership (2026-07-06)

Scope: first half of the final consolidation. A component-layer audit found same-named components with different designs across pages — implementer traps, because a coding agent grepping by name can land on the wrong page's version. Five items, all dedupe/ownership; K2 handles primitive promotion and token forks. Honest-tracking rule applies: anything skipped gets an OPEN row, recorded BEFORE export.

---

## 1. Rename the three Composers (a live load-order bug rides on this)

`Composer` is defined in vesper-shared.jsx (~72), onboarding-kit.jsx (~56), and vesper-chat-canon.jsx (~538) — three different designs, different props. On Vesper Onboarding.html, onboarding-kit loads AFTER the shared file and silently shadows it. Fix: vesper-shared keeps `Composer` (the canonical home composer); rename onboarding's to `OnboardingComposer` and chat's to `ChatComposer` (update their in-file usages + any consumer in the same page family). Verify Onboarding still renders identically after the rename (its flow files must now reference OnboardingComposer explicitly — no more accidental shadow). Same treatment for the smaller `Chip` shadow on the same page and the `Eyebrow` shadow on Row System (rename row-system's to `RowEyebrow`).

## 2. One owner for the group-chat room and the venue/dossier screens

Full renditions exist on TWO pages each: `ScreenGroupRoom`/`ScreenPrivateThread`/`GroupDecisionCard`/`GroupEventLine`/`MemberBubble` in both people-collab-app and vesper-chat-canon; `ScreenDossier`/`ScreenVenueDetail` in both places-canon-app and vesper-discover-detail-app. Ruling per prior ownership: **Chat owns the chat screens; Places owns venue detail; Discover Detail owns the dossier reader.** For each non-owner: rename its copies to `*Ref` with a one-line pointer caption ("reference render — canonical version lives on X"), or replace the artboard with a pointer note. The non-owner pages keep their context (People & Collab needs a group-room frame for the privacy-seam story) — the point is that the DEFINITION site says who owns it.

## 3. Merge the drifted invite landing

`ScreenInviteLanding` exists in auth-invite-app AND people-collab-app at ~50% similarity — a copy that drifted, which reads as intent. **Auth & Invite owns it** (per canon). Update people-collab's to match auth-invite's current design and mark it `Ref` per item 2's pattern.

## 4. Rename the three LedgerRows + rule the diff grammar

- `LedgerRow` means three things: a changes-ledger row (row-system), an expense row (costs-system), and a third in action-grammar-rows. Rename: row-system's → `ChangesLedgerRow`, costs' → `ExpenseRow`; action-grammar-rows' copy gets retired or renamed to match whichever it actually depicts.
- Diff grammar: Changes' ReskinnedSheet strikes WAS in stacked rows; revert-conflict-sheet strikes NOW in side-by-side cards — inverted. RULE IT: either revert-mode is a sanctioned inverted variant (record why: reverting means the CURRENT state is being struck), or redraw revert-conflict onto the Changes grammar. Recommend: sanction the inversion WITH the rationale written down — it's semantically defensible — and extract the shared chrome constants (handle 36×4, gold kicker) so only the diff direction differs.

## 5. Purge the 28 dead exports

Led by trip-document-canon's 10 (HeroV1–V5, HeroAir, TwoTierDoc, DocAes, DeckClear, DeckDoc — superseded explorations still exported from a canon file) and the dead names in multi-page shared files (vesper-shared: VesperQuote, VES; trips-shared: StarterChip, StarterGlyphs; discover-kit: DossierBar, FieldEyebrow, VesperBy). Keep: HomeLoading (deliberate rescue), HistCombo/HistPhone/RailRow (live). Delete the export entries AND the dead component bodies unless a body is referenced by a live component. Also delete the two truly-orphaned files places-kit.jsx and places-composed.jsx.

## Definition of done

Zero same-name-different-design collisions among live files (grep any component name → exactly one definition or clearly-marked Refs) · Onboarding renders with explicit OnboardingComposer · diff-grammar ruling recorded · ≤0 dead exports beyond the sanctioned keeps · export a handoff.
