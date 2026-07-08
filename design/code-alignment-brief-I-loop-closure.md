# Code Alignment — Batch I: Loop-Closure Entry + Destination (2026-07-06)

Repo: `~/travel-workspace/travel-app`. Canon: `Vesper Trip Creation.html` §01b "The outbound loop — a joiner's turn" (handoff 110, verified — `CreateEntry({ joiner })`, `NewTripJoiner` in `create-screens.jsx`). Replaces the FE stopgap shipped same-day as a functional-but-undesigned placeholder for the multiplayer invite loop's outbound half (a joiner going on to organize their own trip).

Standing rules: git status first (branch from main) · snap rule (app tokens are value truth) · one commit per task · typecheck+tests green · no push without approval.

## Important — a real gap this dig surfaced (read before scoping Task I-2)
Canon's `CreateEntry` (Trips Home's "single, primary creation affordance") is a card: title "Begin a trip" + italic subtitle "Talk it through, or start from a shape." + gold spark icon + arrow. **The current code has no equivalent of this card at all.** The actual entry point (`app/(tabs)/trips/index.tsx:842-851`, `createFab`) is a bare icon-only floating "+" button with no visible text — only an `accessibilityLabel="Begin a trip"`. This predates this session; it isn't something the FE stopgap introduced. It matters here because canon's whole Option A resolution ("only the subtitle copy changes, same position/weight/icon") assumes the subtitle-bearing card already exists — it structurally doesn't. Task I-2 below has to build it, not just retint it.

## Task I-1 — Retire the FE stopgap trail row
Remove the "Plan one of your own" row and its plumbing, now superseded by I-2/I-3:
- `components/trips/TripsHomeTrail.tsx` — remove the `hasOnlyJoinedTrips`/`onStartOwnTrip` props, the `showStartOwnTrip` computed flag, and the `start-own-trip` row push (~lines 137, 165, 169, 230-237). Also drop the `'start'` `RowIcon` variant + glyph added for it in `components/trips/TripsHomeCards.tsx` if nothing else uses it.
- `app/(tabs)/trips/index.tsx:180-186` — the `hasOnlyJoinedTrips` computation stays (it's the substrate signal both I-2 and I-3 need — just stop passing it into `TripsHomeTrail`; wire it into the entry affordance and `trip-begin` instead, per I-2/I-3).

## Task I-2 — Build the missing "Begin a trip" card, with the joiner variant
Replace the bare `createFab` (or add the card alongside it, if a persistent floating "+" is still wanted for one-tap access from anywhere in the scroll — designer's call, canon only depicts the card) with the canon `CreateEntry` card:
- Default: title "Begin a trip", subtitle "Talk it through, or start from a shape.", gold spark icon, arrow — reuse the app's existing card-row primitives (this looks like the same shape as `TripsHomeTrail`'s `ListRow`/`TableCard` family — check `components/trips/TripsHomeCards.tsx` for the closest existing match before building new).
- Joiner variant: subtitle becomes "Your turn — talk it through, or start from a shape." when `hasOnlyJoinedTrips` is true (computed in `index.tsx`, already available). Same position, same weight, same icon — copy is the only thing that changes, per canon.
- Both variants route to `routes.tripBegin()` (unchanged).

## Task I-3 — Personalize the `trip-begin` destination for joiners
`app/trip-begin.tsx` (`BeginTripScreen`) already faithfully implements canon's default `NewTrip` hierarchy (`"How should we start it?"` → "Talk it through with Vesper" recommended path → "OR START FROM": What you've saved / Pick a shape / A blank trip — verified at lines 320-377). Add the `NewTripJoiner`-equivalent variant:
- When the navigating user has `hasOnlyJoinedTrips` true (thread the signal through — either as a route param from the Trips Home entry, or recompute locally via `useTripsList()`, matching the pattern already used in `index.tsx:181-186`), render a "TRIPS YOU'VE BEEN PART OF" receipt above the existing content: each past trip's destination + an `AvatarStack` of co-travelers (`TripWithMembers.travelers`), labeled "JOINED". Reuse `components/ui/AvatarStack.tsx` — don't build a new avatar-stack component.
- Add the honest prose line: "You've always joined someone else's — where's your head going for one of your own?" (or equivalent — match canon's voice, don't invent a different line).
- The recommended "Talk it through with Vesper" path and the "OR START FROM" list (all three rows — What you've saved / Pick a shape / A blank trip) are otherwise **unchanged** — same copy, same order, same destination routing. Do not drop or reorder any of the three rows (this was the exact mistake caught and fixed between handoffs 109 and 110 — don't reintroduce it).
- Substrate honesty: only show real past trips + real co-travelers. If `hasOnlyJoinedTrips` is true but the trip history is otherwise thin (e.g., only one past trip, or travelers didn't resolve), degrade gracefully — omit the receipt row rather than showing an empty or fabricated one. Never invent a "you'd probably want X" destination suggestion — canon is explicit this must not happen.

## Done
FE stopgap trail row fully removed · canon's `CreateEntry` card built (default + joiner subtitle variants) and wired into Trips Home in place of (or alongside) the bare FAB · `trip-begin.tsx` renders the joiner receipt (real trips + real co-travelers only, calm register, no invented inference) when `hasOnlyJoinedTrips` · the three "OR START FROM" rows remain complete and in canon order in both the default and joiner paths · report which entry-affordance approach you took (replace FAB vs. card-plus-FAB) since canon didn't explicitly rule on keeping a persistent floating "+" alongside the card.
