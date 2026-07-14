---
doc_type: working
status: active
owner: frontend / product
created: 2026-07-13
last_verified: 2026-07-13
expires: 2026-08-12
why_new: Record the IR-13 itinerary read-shell implementation, synchronization gate, flags, and verification evidence.
source_of_truth_for: [itinerary-redesign-ir13-read-shell-evidence]
---

# IR-13 — Itinerary read shell evidence

Date: 2026-07-13
Lane: `itinerary-foundation`
Status: implementation complete behind dogfood flags; device dogfood remains an exposure check

## Outcome

IR-13 makes the itinerary the flag-gated single-trip entry without expanding
`TripFolioHome` or enabling IR-14 mutations / IR-16 post-trip routing. The
resting shell uses the existing productive Vesper header and row primitives,
adds compact-on-scroll chrome, retains one List/Map artifact, and pushes Trip
Details as a full-screen factual index.

The implementation consumes IR-12 Plan/Details authorities directly. Folio is
unchanged and remains a compatibility source on the flag-off path.

## Exposure flags

- Frontend: `EXPO_PUBLIC_ITINERARY_READ_SHELL_V2=true`
- Backend: `ITINERARY_READ_MODELS_V2=true`
- Backend: `TRIP_DETAILS_STATE_V2=true`

The frontend flag defaults off. If canonical Plan authority is absent, the
itinerary remains readable but canonical attention/domain-link enhancements are
omitted; the client does not reconstruct them from Folio. Trip Details reports
unavailable/partial sources honestly.

## Implemented contract

- Trip landing redirects to the itinerary only under the frontend dogfood flag.
- Light Ledger chrome owns Back, trip identity, Chat, one List/Map switch, and
  a comprehensive Details/overflow entrance; identity withdraws after scroll.
- Trip Details is a full-screen push in the fixed order Identity, People, Stay,
  Transport, Costs, Bookings, Changes/History, Settings.
- Plan rows are inspect-first under the new shell. Generic events open typed
  event inspection; a single linked stay/transport identity opens that domain
  object directly.
- Contextual itinerary and comprehensive Trip Details entrances route through
  the same `{kind,id}` identity. Connected booking, expense, place, stay,
  transport, and history destinations remain explicit.
- One IR-12 attention projection supplies the shell's Needs Attention entry.
- Cross-face state now retains face, active day, typed selection, list offset,
  map camera center, and Details path. Return state is trip-scoped and cannot
  leak between trips.
- Details partial-data state is visible and does not invent absent rows or
  values. Completed-record/Memory readiness is carried in the contract but no
  frontend post-trip routing is enabled.
- Existing Plan mutation surfaces remain unchanged and outside this slice.

## Golden-path proof

- Itinerary event → connected expense and Trip Details → Costs resolve the same
  stable expense identity through the typed object route, with different entry
  modes and native return stacks.
- Itinerary stay anchor and Trip Details → Stay resolve the same stable stay
  identity when the event has one unambiguous `uses_stay` link.
- Map selection publishes the same event identity used by List inspection.
- Captured exact-return state includes every IR-12-required field: face, day,
  selection, scroll, camera, and Details path.

## Synchronization gate cleared

The stale medium-sheet Trip Details language was replaced with the full-screen
index rule. Unconditional completed-trip Memory-default language was replaced
with server-authored completed-record/meaningful-Memory readiness; IR-16 still
owns exposure.

## Verification

- `npx tsc --noEmit --pretty false` — pass
- IR-13 context and Details unit tests — 3/3 pass
- Plan and trip-workspace smoke tests — 28/28 pass
- Plan smoke suite with `EXPO_PUBLIC_ITINERARY_READ_SHELL_V2=true` — 13/13 pass
- `npm run api-boundaries` — pass
- `npm run accessibility-governance` — pass
- `npm run qa:flags:test` — pass
- `npm run state-ownership` — pass
- `git diff --check` — pass

Device dogfood should exercise the exit-gate sequence with all three flags on:
enter trip, switch List/Map, inspect an event/stay, open linked expense, open
the same expense through Trip Details, visit Chat, and verify exact Back return
for day, selection, list offset, and map camera. That exposure check should not
expand IR-13 implementation scope.
