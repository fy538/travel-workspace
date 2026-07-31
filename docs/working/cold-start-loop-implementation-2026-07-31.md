# Cold-Start Loop: Implementation Record (2026-07-31)

Companion to `cold-start-and-everyday-places-experience-mvp-2026-07-31.md`.
That doc's §23 asked for one end-to-end design-and-contract board before
implementation; §22 item 10 named where the design would happen (Claude
Design, "Vesper Trips Home — Stack Model (Sans)"). This doc records what
was actually designed there and then built against the real codebase the
same day, and what remains open.

## 1. What shipped

### 1.1 The loop, designed

Claude Design project `551f400f-3da1-42ab-be7f-35f2d28e7c75`, file
`Vesper Trips Home - Stack Model (Sans).html`, section `cold-loop`. Four
artboards: the proposal (crown + typed/voice "OR JUST ASK" + CONNECT), the
global-dossier fallback, today's actual floor (reproduced from the real
producer strings, for comparison), and the in-chat invite moment.

The design correction that mattered: an earlier pass (K–N, section
`cold-brainstorm`) built a strong demonstration — Vesper's voice, hero
scale, a real curator take or dossier — but every one of its CTAs opened a
*reader*, not a conversation. Reading the shipped code revealed why that
regresses activation: a cold account has **no create FAB**
(`app/(tabs)/trips/index.tsx` suppresses it for `heroKind === "cold"`), so
a read-only crown would leave the page with zero doors into Vesper. The
loop's fix: the crown still shows judgment, but its CTA is
`open_chat_prefill` — the same mechanism the four shipped starter cards
already use — carrying that judgment into chat instead of a reader.

### 1.2 Slice A — the cold-start producer (`travel-agent`)

**Backend only.** New `_local_take_cards()` producer
(`backend/home/concierge_feed/producers.py`), three branches in priority
order:

1. A real Curator Take on a venue near the user's resolved location.
   `resolve_place_id_for_position` (already shipped 2026-07-31, same
   session) resolves ambient lat/lng; `get_curator_takes_batch` is the
   same call `GET /api/discover/map` already makes for pin previews — pure
   reuse, no new content pipeline. A `skip`-verdict take is excluded,
   mirroring Discover's own "don't plot an anti-recommendation" rule.
2. Failing that, a real dossier from anywhere in the seeded corpus
   (`get_dossiers_global` — already public, noauth). Proves the craft
   without ever claiming to know the user's own block.
3. Failing that, `[]` — the existing `len(candidates) < 3` starter
   fallback fires unchanged, so an unseeded-city account sees exactly
   today's behavior.

New kind `local_take`, priority `_PRIO_LOCAL_TAKE = 63` (just above the
starter floor), tier-3 mapping in `trips_stack.py` (a gift, never an open
decision the header could call NEEDS YOU). Lead-queue eligibility comes
from `family="explain"` → `authorship="vesper"` → `CardClass.ATTENTION` —
the same mechanism `planning_brief`/`trip_retrospective`/
`settlement_closeout` already use; no new eligibility rule.

Frontend needed almost nothing: `TripsStackCrown` already renders any
card's title/body/CTA generically, and `open_chat_prefill` already maps to
`TripsHomeDestination(type="vesper", message=...)`. One label line added
(`utils/tripsHomeStackModel.ts`) plus the `local_take` kind added to two
FE-side literal unions the schema-sync missed.

Tests: `tests/home/test_local_take_cards.py` (6 cases — all three
branches, the skip-verdict exclusion, malformed-row safety, honest
absence) plus a corrected + a new integration test in
`tests/api/test_concierge_home.py` (the old "cold-start fallback" test
didn't mock the new dependency and started legitimately crowning a real
dev-DB dossier — fixed by mocking it explicitly, and a sibling test now
pins the new "real dossier beats the bare starter" behavior).

### 1.3 Slice B — the conversation-invite callsite (`travel-app`)

**The real bug this found:** `createConversationInvite` /
`listConversationInvites` (`utils/api/interface.ts`, `http.ts`) had wrong
types from day one — a fictional `APIConversationInvite` /
`CreateConversationInviteRequest` shape matching neither the backend
request nor response model. Zero product callsites meant nothing had ever
exercised the mismatch. Reading `backend/api/routes/invites.py` directly
confirmed the conversation route shares the exact same `InviteCreateRequest`
/ `InviteCreateResponse` Pydantic models as the trip-scoped route — only
the URL, the ownership check (`_require_conversation_owner` vs
`require_trip_organizer`), and the substance-gate error code
(`conversation_needs_substance` vs `trip_needs_substance`) differ. Fixed
by repointing to the real types.

Built: `hooks/useCreateConversationInvite.ts` (mirrors
`useCreateInvite`/`useShareTripInvite` test-for-test), and
`components/chat/ConversationInviteNudge.tsx` — a direct sibling of the
shipped `OrganizerInviteNudge` for the pre-trip case. Wired into
`app/(tabs)/concierge/chat.tsx`, gated on `isStandalone` (no trip yet) and
at least one real assistant reply having landed. No conversation-scoped
eligibility endpoint exists (unlike trips' `GET
/api/trips/{tripId}/invites/eligibility`), so this is the honest
client-side proxy for "a real exchange has happened" — the backend's own
`conversation_has_substance` check at mint time remains the actual
authority; a 409 there degrades to a toast rather than navigating away,
since the caller is already inside the one conversation the nudge is
about.

Tests: 4 hook tests mirroring `useCreateInvite.test.ts` line-for-line, plus
a `conversation_invite_substance` mock-mode fault so the substance-gate UI
path is exercised in dev, matching the trip-scoped convention.

### 1.4 Slice C — the gated voice card (`travel-app`)

`components/voice/VoiceAskCard.tsx` — existence-gated internally on
`VOICE_ENABLED` (renders `null` when off, so no call site can forget the
check). Reuses the app's real, already-shipped tap/hold convention exactly
— the same `Tap` with `onPress` / `onLongPress={openVoice}` and `"Tap to
chat. Hold to talk."` hint the create FAB already uses — rather than
inventing a new gesture. No fabricated "still waveform" bars (the design
mockup's own invention, dropped here for lack of any real precedent); uses
the real `VesperVoiceMark` brand glyph instead.

Wired into `app/(tabs)/trips/index.tsx`: the create FAB (this page's only
voice door) is suppressed for `heroKind === "cold"`, so a cold account has
zero voice entry points today. The card fills exactly that gap, right
after "ALSO IN PLAY." Its tap handler reuses `runStackCrownAction`, the
same destination the crown's own CTA already opens.

Tests: `__tests__/components/voice/VoiceAskCard.test.tsx` (5 cases,
mirroring `NarrationListenButton.test.tsx`'s established `VOICE_ENABLED`
mock pattern).

### 1.5 Phase 0 — corpus measurement (no code)

Ran the existing `tools/dogfood/seeded_city_readiness.py` against the
**local dev DB** (not staging/production — caveat below) for the 9 cities
it has editorial content for:

| City | Score | Verdict | Dossiers |
|---|---|---|---|
| lisbon | 87% | external_dogfood_ready | 3 |
| rome | 60% | internal_dogfood_ready | 2 |
| tokyo | 57% | seeded_but_thin | 2 |
| naples | 45% | seeded_but_thin | 7 |
| istanbul | 43% | seeded_but_thin | 2 |
| kyoto | 38% | not_ready | 2 |
| brooklyn | 32% | not_ready | 3 |
| copenhagen | 32% | not_ready | 2 |
| athens | 25% | not_ready | 2 |

Raw counts: 334 places, 25 dossiers (all `approved`, 0 `draft`), 105
`entity_takes` (all `tier='curator'`). Only Lisbon clears the readiness
tool's own `external_dogfood_ready` bar; most cities are well under the
"≥12 dossiers" target the tool checks for.

**Caveat:** this is a snapshot of the local dev database, not the
staging/production corpus the MVP doc's earlier evidence (34 seeded
cities, ~38 curator-tier rows total) describes — the two clearly diverged
since that note was written, in the dev DB's favor. Re-run the same
command (`PYTHONPATH=. python tools/dogfood/seeded_city_readiness.py
--place <slug> --json`) against staging/prod before treating either number
set as the real answer to "how often does branch 1 (local take) vs branch
3 (starter floor) fire for a real user."

**`AUTO_PUBLISH_GREEN_DOSSIERS`** remains a founder decision, not resolved
here — default is OFF (human-in-the-loop promotion via
`scripts/publish_approved_dossiers.py`), per `backend/core/feature_flags.py`'s
own documented rationale. Flagging it as still open, not deciding it.

### 1.6 Track 2 — `trip_kind` schema layer (`travel-agent`)

**Re-scoped after reading the actual planner code.** The MVP doc framed
`trip_kind` as unlocking planning for local plans via three blockers in
sequence (planner gate → materialization invariants → schema). Reading
`planning_materialization.py` directly showed this overstated the block:

- `_destination_ref` accepts `trip.place_id` **before** it ever falls back
  to a `destination_label` — a local trip with a resolved `place_id` (the
  same one `resolve_place_id_for_position` already gives Slice A's curator
  take) satisfies this with zero code change.
- `dated_trip_required` only checks that real `start_date`/`end_date`
  exist — a local plan for "this Saturday" has real dates by construction;
  nothing about "local" implies dateless.
- `itineraries.trip_id NOT NULL` was never actually a blocker for a
  *local* trip specifically — it blocks planning with **no trip row at
  all**, which was never the actual ask (the ask was "reuse the trip
  aggregate," not "plan without one").

So the planner and materialization gates require **no changes** — proven,
not assumed, by
`tests/core/test_local_trip_creation.py::test_local_trip_with_resolved_place_and_dates_materializes_a_plan`,
which creates a `trip_kind="local"` trip with a real (dynamically-fetched)
`place_id` and real dates, then calls the unmodified
`materialize_planning_output` and asserts it succeeds.

What Track 2 actually needed, and what shipped:

- **Migration** `e8f1c3a6b9d2_add_trip_kind_to_trips.py`: `trips.trip_kind
  TEXT NOT NULL DEFAULT 'travel'`, `CHECK (trip_kind IN ('travel',
  'local'))`, an index. Applied to the dev DB; all 7,678 existing rows
  backfilled to `'travel'` cleanly.
- `TripKind = Literal["travel", "local"]` in `backend/core/models/trips.py`,
  `Trip.trip_kind: TripKind = "travel"`.
- `CreateTripRequest.trip_kind: TripKind = "travel"`
  (`backend/api/routes/_trip_requests.py`), threaded through
  `create_trip_with_organizer` (`backend/core/db/trips/crud.py`) and the
  `POST /api/trips` route.
- Declarative table (`backend/core/db/_tables/trips.py`) updated to match,
  following the codebase's existing (slightly quirky, already-precedented
  for `itinerary_decision_owner_source`) pattern where the declared
  constraint name and the live migrated constraint name differ by a
  doubled `ck_trips_` prefix — not a new inconsistency, matching what
  already exists for that column.
- Fixed two now-stale mock-assertion tests in `tests/api/test_trips_api.py`
  that asserted an exact `create_trip_with_organizer(...)` call signature
  without the new `trip_kind` kwarg.

**What Track 2 does NOT include — deliberately out of scope this pass:**

1. **Agent-behavior wiring.** Nothing yet calls `create_trip_with_organizer(...,
   trip_kind="local")` from the concierge's tool-handler path. The
   producer, the schema, and the materialization proof all exist; the
   piece that turns "what should we do around Fort Greene this Saturday"
   into an actual minted local trip is unwritten. This is real
   LLM-tool-calling and prompt work, not schema plumbing — sized as its
   own follow-up.
2. **Presentation suppression.** `trip_kind` doesn't yet suppress any
   travel-only UI (accommodation readiness, etc.) on either side. The
   field exists to drive that; nothing reads it for that purpose yet.
3. **`PatchTripRequest`** deliberately does not expose `trip_kind` —
   changing a trip's kind after members/bookings/itinerary exist is a
   different, harder question than this pass answered, so it stays
   immutable post-creation for now.

## 2. Doc corrections carried from the design pass

Three stale citations, all now fixed at their source rather than just
noted here:

- The Claude Design board's "shipped, for comparison" artboards modeled
  `ColdHome`, deleted 2026-07-31 — relabelled `⚠ HISTORICAL` in both
  places on the board itself.
- Evidence row citing `_PRIO_NEAR_YOU_NO_TRIP` (deleted the same day as
  dead code) as proof near-you works trip-free — the claim is still true,
  the live citation is `_PRIO_NEAR_YOU_IDLE` + `_near_you_cards`.
- `docs/user-flows/canonical-flow-map.md` still documents the deleted
  `ColdHome` branch — flagged, not yet edited; low-risk doc drift, worth a
  follow-up pass.

## 3. Verification summary

| Area | Result |
|---|---|
| Backend unit/integration (`tests/home/`, `tests/api/test_concierge_home.py`, `tests/core/test_local_trip_creation.py`, `tests/core/test_planning_materialization.py`, `tests/api/test_trips_api.py`) | 612 passed |
| Backend broad sweep (`tests/core/`, `tests/api/`, `tests/concierge/`) | 9,669 passed, 12 failed — all 12 confirmed pre-existing on the clean tree via `git stash` (shared-dev-DB contention noise: narration cache timing, search-index staleness, saga-gateway rollback races — none touch trips/trip_kind/concierge_feed) |
| `ruff` / `mypy` (all touched backend files) | clean (one pre-existing, unrelated mypy error in a generated file, untouched by this work) |
| Frontend `tsc --noEmit` | clean (one pre-existing, unrelated error in `tripsHomeStackFixtures.ts`, untouched) |
| Frontend `eslint` (all new/touched files) | clean |
| Frontend jest (`VoiceAskCard`, `useCreateConversationInvite`, `useCreateInvite`, `tripsHomeStackModel`, `conciergeHomeInteraction`, `concierge-chat.smoke`) | 51 passed |
| J20 certified scenario (`tests/scenarios/test_j20_first_use_trust_value.py`) | passed, both before and after Slice A |

## 4. Suggested next slice

In rough priority order:

1. **Agent-behavior wiring for local plans** — the one piece that turns
   the schema into an actual product capability. Sized as its own pass;
   touches the concierge tool-handler layer and prompt/tool-calling
   behavior, not just plumbing.
2. **Re-run Phase 0 against staging/production**, not just the local dev
   DB, before treating any corpus number as the real answer to how often
   branch 1 vs branch 3 fires.
3. **`AUTO_PUBLISH_GREEN_DOSSIERS` posture** — founder decision, still
   open.
4. **Voice lighting** — its own ops track (flag, LiveKit secrets, Fly
   machine count, Cartesia key); `VoiceAskCard` is ready and waiting,
   existence-gated, the moment any of that lands.
