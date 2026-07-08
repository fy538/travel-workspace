# Code Alignment — Batch G1: Stay State-Space Completion (2026-07-06)

Repo: `~/travel-workspace/travel-app`. Canon: `~/travel-workspace/design/vesper-canon-anchor/project/stay-screens.jsx` + `stay-system.jsx` (read-only). The kit is faithful (plates, NightRibbon, 8-variant StayCard, StayCompare, copy verbatim) — ~1/3 of the 23-state canon matrix renders. This batch completes the state space, with the accommodation-detail composition as the single biggest gap.

Standing rules: git status first (branch from main) · snap rule (app tokens are value truth) · one commit per task · typecheck+tests green · no push without approval · **flag backend-gated items, do not fake data** (three tasks below are BE-gated — verify + flag, don't stub).

## Task G1-1 — Accommodation detail = ConfirmedDetail composition, not Places Spot face (biggest gap)
`app/accommodation/[accommodationId].tsx:47-51` currently renders the Places "Spot" template (`SpotTopBar`/`SpotTake`/`SpotActions`/`LeadFacts`) — it is the wrong composition for a confirmed stay. Canon's `AccommodationStandalone` (`stay-screens.jsx:220-250`) is the ConfirmedDetail: booking facts (check-in/out, nights, price, party, reference), night coverage, who's on it, and a tap-through opened *from the Trip row*, not a home promotion.
- Build the ConfirmedDetail composition from the Stay kit (reuse `NightRibbon`, StayCard confirmed variant, the plates) instead of the Places face.
- Wire the tap-through: `components/stay/StayHome.tsx:195` (`onOpenStay`) currently routes to `handleStayMenu` — route a confirmed stay to this detail screen instead. Verify the Trip-row entry point exists (the folio StaySection / TripFolioHome stay row) and lands here.

## Task G1-2 — Suppress "No bed yet" on returned trips + add the missing state variant
`components/trip/TripFolioHome.tsx:625-662` (`StayDocumentRow`) always renders "No bed yet · Add" when `!hasStayContext`, even in `post` phase — this violates the canon suppress ruling (`stay-screens.jsx:387-411`, "Returned · has record → Suppress"; "Returned · missing data → Suppress"). Root cause: `utils/stayState.ts:32-48` discriminator has no `returned`/`post` variant — only `none / target / missing / confirmed / split`.
- Add a `returned` (or phase-aware) branch to the `stayState` discriminator.
- Suppress the "No bed yet" prompt entirely for returned trips (match the folio's existing `post`-mode gating used elsewhere on that screen).

## Task G1-3 — Candidate / private-visibility sheets (hook exists, zero UI)
`data/stayCandidates.ts:68-77` (`useAddStayCandidate`) has zero UI callers. Canon `StaySheet` (`stay-screens.jsx:252-304`) defines the `candidate` variant fields (name, neighborhood, check-in/out, price/night, 5-night total, cancellation/hold, saved-by·source, note·why-this-one). Also: `app/trip-accommodations/index.tsx:241` hardcodes `visibility: 'group'` on create — the `private` visibility path is unreachable.
- Build the candidate sheet (reuse the `BottomSheet` family + existing StaySheet edit chrome as the base; add the candidate-specific fields).
- Add a "Save candidate" entry point (from StayCompare / stay home add-affordance) that calls the hook.
- Wire real visibility selection (group vs private) instead of the hardcoded `'group'`.

## Task G1-4 — StayCompare: 3+ candidates + VESPER PICK recommendation
`components/stay/StayCompare.tsx:233` hard-caps at 2 with `active.slice(0, 2)`. Canon shows compare as flexible per phase (`stay-screens.jsx:82-158`) and threads a recommendation. The `recommendation` prop (`StayCompare.tsx:249-255`) is optional and never populated.
- Lift the 2-candidate cap so 3+ candidates render (verify the layout holds — canon shows 2 side-by-side; 3+ may need horizontal scroll or a stacked treatment, follow the kit's compare grammar).
- Wire the "VESPER PICK" recommendation from the decision read model (if the field isn't exposed by the stay decision API, **flag it** — this may be a backend gap like the vote-phase one below).

## Task G1-5 — Vote-arc tail: nudge + one-blocking phase [PARTIALLY BACKEND-GATED — flag]
`components/stay/StayCompare.tsx:21-43` (`headlineFor`) models 4 phases: `not_started / open / tie / decided`. Canon `VoteStates` (`stay-screens.jsx:111-158`) has six, including **ONE BLOCKING** (one holdout, "Nudge Theo →" action) and a resolved→booked post-view.
- **Backend gap:** `utils/api/types.ts:1491` — `StayVotePhase = 'not_started' | 'open' | 'tie' | 'decided'` has no `'blocking'`. The one-blocking state cannot render without this field. **Flag this as backend schema work** (add `'blocking'` phase + the holdout identity to the stay-vote read model). Do NOT synthesize "blocking" from tie on the client.
- **Nudge is also backend-gated:** there is no nudge/remind endpoint anywhere in `data/` or `utils/api/`. The "Nudge {name}" action needs one. **Flag it** (shared with G2-4's nudge — likely one endpoint serves both cost-settle nudges and stay-vote nudges). Build the FE affordance behind the flag; keep it dormant with a comment until the endpoint lands.
- **Buildable now:** the resolved→booked post-view (the `decided` phase currently shows only the organizer "Book this" action — add the post-booking confirmation/resolved read state, which uses data already present).

## Done
ConfirmedDetail composition built + tap-through wired from the Trip row · "No bed yet" suppressed on returned trips (state variant added) · candidate sheet + private-visibility path reachable · StayCompare renders 3+ candidates and threads VESPER PICK (or flags it as BE-gated) · resolved→booked view built · one-blocking + nudge flagged as backend schema/endpoint work (FE prepped + dormant, not faked) · report exactly which fields/endpoints backend must expose.
