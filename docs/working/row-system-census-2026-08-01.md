# Row System Census — 2026-08-01

Step 1 of row consolidation. Inventory only: what rows exist, what they're built
on, how many call sites. Taxonomy and board come after this is agreed.

Scope: `travel-app` (`app/` + `components/`), excluding tests and `node_modules`.
Method: static grep over `*Row*` component definitions plus a per-file feature
matrix. Counts are mechanical and reproducible.

> **Read `travel-app/docs/design-system/Row System.md` first.** It is marked
> canonical (updated 2026-07-31) and already defines the architecture, a closed
> register set, and a geometry lock. This census measures the gap between that
> doc and the codebase — it does not propose a new system.

---

## 1. Scope

Excluded per owner decision (2026-08-01): **chat-embedded, card-embedded, and
deck-embedded rows are not part of the row system.**

| Excluded | Files |
| --- | --- |
| Chat | `components/chat/*` — `CardChipRow`, `ComposerContextReceiptRow`, `ConversationCitationRow`, `DocumentEditCard`, `RecommendationBlock`, `ResearchCard`, `VesperChatCardKit` |
| Deck | `components/decision-deck/*` — `DeckBriefFace`, `DeckNearYouFace`, `DeckPickFace`, `DeckStructuredFace` |
| Card-embedded | `BookingProposalCard`, `TripHeroCard` |
| False positives | `ui/Skeleton.tsx` `RowSkeleton`, `ui/Stack.tsx` `Row` (layout helper) |

⚠️ **Two exclusions need an owner call — flagged, not decided:**

- `components/chat/GroupAgencySheet.tsx` `SwitchRow` — lives under `chat/` but is
  a **sheet**, not a bubble. Reads as the Settings register. Probably in scope.
- `components/trips/TripsHomeCards.tsx` `DraftRow` / `ListRow` — caught by the
  `*Cards.tsx` filename rule, but these are trips-home **list** rows and the file
  is already on canon (consumes `DateRailRow`). Probably in scope.

## 2. Headline (in scope)

| Metric | Count |
| --- | --- |
| Row-defining files, all | 82 |
| Row-defining files, in scope | 66 |
| …of which are the bones themselves (`ui/rows/*`) | 7 |
| **In-scope consumer files** | **59** |
| On canon (reach `ui/rows` directly or via a `ui/` register) | **23** |
| Off canon | **36** |

**Adoption: 39%.** The scope cut removed 16 files but barely moved the ratio —
the off-canon population is spread across product surfaces, not concentrated in
the excluded families.

Note the qualifier on "on canon": `app/(tabs)/concierge/history.tsx` and
`app/(tabs)/trips/[tripId]/changes.tsx` reach the bones only *through*
`ui/LedgerRow`, which sits outside `ui/rows/`. A naive `ui/rows` import check
misclassifies them as off-canon — a direct consequence of §5.2(a).

## 3. What already exists

### 3.1 Written canon

`travel-app/docs/design-system/Row System.md` (status: canonical, 2026-07-31)
defines a three-layer architecture — **Page → Registers → Bones** — and a
**closed set of 8 registers**:

> Ledger · Editorial · Utility · Settings · Spine · DateRail · Command · Choice

It also fixes a geometry lock (vertical pad from `rowTokens` only; chevron via
`RowAccessory` @14; divider aligns to leading column; no per-row `paddingTop`
nudges) and a ledger line budget.

Its own framing is the right one: *"Consolidation that stops at `RowCore` is not
done — registers must obey tokens and line budgets."*

### 3.2 Code bones

`components/ui/rows/` — `RowCore.tsx` (277), `rowTokens.ts` (214),
`RowAccessory.tsx` (70), plus register shells `SettingsRow` (173),
`EditorialListRow` (195), `SpineRow` (151), `UtilityRow` (158), `DateRailRow`
(299), and `ledgerLineBudget.ts`.

`rowTokens` enumerates 8 leading kinds (`none`, `bare`, `settings`, `avatar`,
`thumbnail`, `dateRail`, `time`, `sequence`) and 3 densities.

### 3.3 Enforcement

`__tests__/conventions/` — `rowSurfaceContract`, `rowAccessoryContract`,
`rowOpticalContract`, `ledgerRowContract`, `rowTokens`.

⚠️ **These are allowlists, not ratchets.** They name specific files and assert
*those* stay on canon. Nothing stops a new off-canon row from landing. The doc's
"Convergence status (Done — P4)" is accurate **for the named register owners it
lists** — and that list is ~12 files against a 58-file in-scope population.

This is the central structural finding: canon is defended file-by-file, so the
off-canon population can grow faster than it is converted.

## 4. Register coverage: 8 declared, 6 have shells

| Register | Shell | Location | Call sites | State |
| --- | --- | --- | --- | --- |
| Ledger | `LedgerRow` | `ui/` — **outside the barrel** | 3 | On RowCore; see §5.2 |
| Editorial | `EditorialListRow` | `ui/rows/` | 8 | Atlas-dominated (5 of 8) |
| Utility | `UtilityRow` | `ui/rows/` | 3 (1 = dev gallery) | **2 real consumers** |
| Settings | `SettingsRow` | `ui/rows/` | 5 (1 = dev gallery) | Healthiest register |
| Spine | `SpineRow` | `ui/rows/` | 5 (1 = dev gallery) | — |
| DateRail | `DateRailRow` | `ui/rows/` | 2 | Trips-home only |
| **Command** | — | `ui/ActionRow.tsx` (7), `ui/ActionListSheet.tsx` | 7 | **No shell on bones** |
| **Choice** | — | `ui/SelectionRow.tsx` | 8 | **No shell on bones**; see §5.1 |

`RowAccessory` has 14 call sites — the most-converged single piece.

**Two of eight registers have no implementation on the bones**, and they are the
two with the highest off-canon call-site counts (7 and 8). That is where the
taxonomy is thinnest, not where it's most contested.

## 5. The two open questions — answered

### 5.1 `ui/SelectionRow` — intended register, parallel implementation

**Verdict: deliberate, and already in the taxonomy.** It is the **Choice**
register named in `Row System.md`. Its own docstring claims the role: *"Canonical
text-row selector."* 8 call sites across sheets, onboarding, expense, stay, and
the parallel plan editor.

But it is a **parallel implementation, not a shell**:

- Does not use `RowCore`. Builds its own `Tap` + `flexDirection: 'row'`.
- Its `variant` axis (`compact` / `sheet` / `card`) duplicates `RowCore`'s
  `density` — with independent numbers: `minHeight` 44/56/56 and
  `paddingVertical: spacing.lg` literals. This directly violates the geometry
  lock in `Row System.md` ("must not override `paddingVertical` with literals…
  use `density`").
- Delegates its indicator to a separate primitive, `ui/ChoiceIndicator` — that
  part is clean and should survive re-basing.

**One real blocker for re-basing.** The `card` variant carries a *selected tile*
treatment: `borderRadius: radius.lg`, `backgroundColor: colors.action.tint`,
hairline border. `RowCore`'s `carded` prop only adds horizontal padding — there is
no selected-background or tile-radius state. So re-basing Choice onto RowCore
requires **adding a selected/tile surface state to the bones**, not just moving
the file.

→ **The taxonomy gains a shell.** `ui/rows/ChoiceRow.tsx` on RowCore + retained
`ChoiceIndicator`, with a bones-level selected-surface state.

### 5.2 `ui/LedgerRow` — deliberate register, real geometry drift

**Verdict: not drift in intent; drift in geometry.** It is the Ledger register
owner named in the doc, it is guarded by `ledgerRowContract`, it is listed in
`rowAccessoryContract`'s shared families, and it correctly consumes `RowCore`,
`RowAccessory`, `rowTokens`, and `ledgerLineBudget`.

Two genuine problems:

**(a) Split location.** `ledgerLineBudget.ts` lives inside `ui/rows/` and is
exported from the barrel; `LedgerRow.tsx` sits one level up in `ui/` and is not.
Half the register is inside the canonical folder. Cheap fix: move the file, add
the barrel export.

**(b) It bypasses the leading-kind enum with magic numbers.** `LedgerRow.tsx:159`
declares `leadingKind="bare"`, then overrides all three values that
`leadingKind` exists to derive:

```
leadingWidth={hasAvatar ? 24 : 18}
leadingGap={hasAvatar ? spacing.md : 7}
dividerInset={hasAvatar ? 32 : 25}
```

`rowTokens.leading.avatar` is **34** — sized for the member/roster avatar.
LedgerRow needs a 24px avatar. Rather than adding a token, it hardcoded three
derived numbers at the call site. Same for the severity dot (18/7/25), which is a
leading kind the enum simply doesn't have.

→ **This is a taxonomy gap the census found, not a coding sin.** `rowTokens`
needs at least two more leading kinds — `avatarSm` (24) and `mark`/`dot` (18) —
after which the overrides delete themselves and the geometry lock actually holds
for this register.

## 6. Off-canon inventory, grouped by mechanic

38 in-scope consumer files. Grouping is a first-pass hypothesis from names + the
feature matrix; §7 lists what still needs reading.

**A. Tappable-navigates (leading + copy + chevron)** — largest group; `RowCore` +
`RowAccessory` already covers it exactly.
`places/core/PlacesCore.tsx:195,379` `PlaceRow`/`QueryRow` ·
`places/core/PlacesDepth.tsx:175` `ExperienceRow` ·
`places/PlaceHome.tsx:276` `HoodRow` ·
`places/SpotFacts.tsx:107,245` `FactRow`/`WorldLinkRow` ·
`app/place/[placeSlug].tsx:654` `EventRow` ·
`app/atlas/saved-places.tsx:136` `ManagedSavedRow` ·
`app/guide/[slug].tsx:357,362` ·
`trips/TripsStackRows.tsx` · `trips/TripsHomeViews.tsx` ·
`vesper-workbench/VesperWorkbench.tsx` · `stay/StayRow.tsx`

> **Places is the single largest off-canon cluster: 4 files, 7 row definitions,
> zero canon adoption.**

**B. Choice register, off-shell** — `ui/SelectionRow.tsx` (§5.1) ·
`atlas/StylePickerSheet.tsx:167` `StyleOptionRow` ·
`inbound/InboundCandidatePicker.tsx:37` `CandidateRow` ·
`trip-creation/TripCreationPrimitives.tsx:216` `StartRow`

**C. Command register, off-shell** — `ui/ActionRow.tsx` (7 call sites) ·
`ui/SheetDisplayRow.tsx`

**D. Label→value read-only (receipt / ledger / diff)** — should mostly land on
Ledger or a read-only variant.
`booking/BookingReceiptPrimitives.tsx:87` · `booking/BookingCoverageBoard.tsx:54` ·
`trip/proposal-detail/ProposalDetailScreen.tsx:946` `DiffRow` ·
`trip/proposal-detail/ProposalReceipt.tsx:359` ·
`expense/CostsBalanceSheet.tsx:169,224` ·
`atlas/AtlasMemoryReceipt.tsx:361` `ClaimRow` ·
`app/you/data-receipt.tsx:124` · `app/dev/billing-sandbox.tsx:159` ·
`app/(tabs)/trips/[tripId]/changes.tsx:71` `CanonicalHistoryRow` ·
`app/(tabs)/concierge/history.tsx:415` `HRow`

> The last two are **not** off canon — verified: both import `ui/LedgerRow` and
> render it directly, exactly as the doc's "Done — P2" claims. They only *look*
> off-canon to an import check because LedgerRow lives outside `ui/rows/`.

**E. Spine register, off-shell**
`atlas/AtlasReadingCanvas.tsx:799` `TimelineMomentRow` ·
`onboarding/DiaryTimelinePreview.tsx:40` · `app/atlas/scan.tsx:304,531`

**F. Person / avatar** — `app/you/people.tsx:209` `SocialFollowRow` ·
`app/trip-info/index.tsx:1472` `InviteRow`
(vs. on-canon `MemberRows` `MemberRosterRow`, `ReaderMemberRow`.)

**G. Genuinely special-cased** — `trip-plan/PlanBlockRow.tsx` (668 LOC, drag +
reorder + parallel plan editing), `booking/BookingOfferRow.tsx` (581 LOC, offer
state machine). Candidates for *adopting RowCore as substrate* while keeping
their own logic — not for collapsing.

## 7. Single-call-site rows (absorption / deletion candidates)

`BookingOfferRow` 0 (exports `OfferRow`, verify) · `BlockWhyRow` 0 ·
`StayRow` 1 (dev screen only) · `FoundRow` 1 · `CostsLedgerRow` 1 ·
`SheetDisplayRow` 1 · `PlanExplanationRow` 1 · `AtlasTimelineEntryRow` 1 ·
`TripsStackRows` 1 · `TravelSegmentRow` 1 · `PlanBlockRow` 1

## 8. Design-canon side

`~/travel-workspace/design/` has **no row board**. Rows are drawn inside
per-screen canvases (`Vesper Itinerary.html`, `vesper-trip-settings-app.jsx`,
`trips-home-canon.jsx`, `trust-kit.jsx`, `booking-canon-receipt.jsx`).
No artifact places two rows from different domains side by side.

Code has both a written canon and a token substrate. Design has neither. That
asymmetry explains why code converged first — and it is exactly what a single row
board would fix.

## 9. What the census implies

1. **Don't design a new system.** `Row System.md` already declares the taxonomy.
   The board's job is to *draw* the 8 declared registers side by side.
2. **Two of eight registers have no shell** (Command, Choice) and they carry 15
   off-canon call sites between them. Build those two shells before drawing
   anything.
3. **The bones are missing states the registers demonstrably need** — a selected
   tile surface (§5.1) and two leading kinds, `avatarSm` 24 and `mark` 18 (§5.2).
   Both were discovered from real overrides, not speculation.
4. **Allowlist → ratchet is the highest-leverage change and is independent of any
   design work.** A general rule (any `*Row*` in `app/`/`components/` imports from
   `ui/rows`, with a shrink-only exception list) stops the population growing
   while conversion proceeds.
5. ~~Places is the best first conversion target.~~ **Withdrawn 2026-08-01** — see
   §11.

## 11. The Places board overrides the Places recommendation

`PLACES.html` / `places-system.jsx` in the Claude Design *Vesper* project
(updated 2026-08-01, being executed by a parallel agent) rules:

> Everything in the feed is a card. More than four does not become a longer
> section and never becomes a list — the count becomes a door. **Rule 10 removes
> the row from the feed altogether.** Rows survive only on the far side of that
> door, and in search.

So the 7 off-canon Places row definitions in group A are **being deleted, not
converted**. Do not spend conversion effort there. Three consequences:

1. **Pick a different first conversion target.** The next-largest single-domain
   group-A cluster, not Places.
2. **Places' surviving rows are Utility-register rows** (search results, behind
   the door). Utility currently has *2 real consumers* — it is about to acquire
   its most important one. Build the Utility register out with search in mind.
3. **The board supplies a semantic card/row boundary the row system lacked:**
   *"a row has no foot bar, so it cannot be added to a day."* Generalised: a row
   cannot carry the primary commit action; a card can. That is a sharper test
   than any geometry rule for deciding whether something belongs to the row
   system at all — and it independently supports the owner's 2026-08-01 call to
   exclude chat/card/deck-embedded rows.

⚠️ **Also from that board — a conflict with `rowTokens` to resolve later.** The
two-caps-voices ruling (2026-07-29) states mono is **machine facts only** (times,
counts, distances) and sans caps carries **labels and names**. `LedgerRow`'s
kicker is a label set in `monoStamp`, and `rowType.eyebrow` / `rowType.meta` both
uppercase without distinguishing the two voices. Not addressed in step 1 — it is
a type ruling, not a geometry one, and it needs its own pass.

## 10. Still needs reading (not answerable by counting)

- Are the group-D receipt rows one register or two (read-only ledger vs.
  label→value pairs)?
- The two flagged scope edge cases in §1.
