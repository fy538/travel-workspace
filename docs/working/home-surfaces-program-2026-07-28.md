---
doc_type: working
status: active
owner: founder / eng
created: 2026-07-28
expires: 2026-08-27
why_new: Three build plans landed on 2026-07-28 — Trips stack, Places, Vesper History — each self-contained, each written by a different session, collectively touching the same ranker, the same component folder, and the same typography files. The founder ruled they execute as ONE sequential stream in one worktree pair rather than three parallel tracks merged later. No doc owns that interleaved order, the worktree protocol, or the cross-plan seams. This one owns exactly that and nothing else.
promotes_to: nothing — this doc retires when the program completes
supersedes: []
depends_on:
  - docs/working/trips-home-stack-build-plan-2026-07-28.md
  - docs/working/places-build-plan-2026-07-28.md
  - docs/working/vesper-home-history-implementation-2026-07-28.md
  - docs/working/vesper-home-workbench-2026-07-28.md
  - docs/working/chat-typography-plan-2026-07-28.md
source_of_truth_for:
  - home-surfaces-execution-order
  - home-surfaces-worktree-protocol
  - cross-plan-seams-2026-07
---

# Home Surfaces — the program

> **This doc owns ORDER and STATE. The three plans own CONTENT.**
> Never copy a task's spec here — reference it. If a step's details
> conflict with its plan, the plan wins and this doc gets a one-line
> erratum. A step is DONE when its plan's own exit criteria say so.
>
> The story, one line each:
> **Trips becomes the queue** (objects, decisions) · **Vesper becomes
> sessions** (work with the agent) · **Places becomes the world**
> (browse, place identity). One ranker under all of it.

## Execution posture — ruled by founder 2026-07-28

**One sequential stream, one dedicated worktree pair.** Not three
parallel tracks merged later.

- Create `travel-app` and `travel-agent` worktrees dedicated to this
  program. The docs repo stays on the main checkout (concurrent sessions
  write `docs/working/` daily; docs conflicts are cheap, code conflicts
  are not).
- **Merge to main continuously — commit per landing, not one mega-merge.**
  Every step below is shippable alone by its plan's own design. The
  worktree isolates the stream from other *sessions*, not from main.
- Within the stream, a session may still fan subagents across disjoint
  files. What is banned is a second *worktree* advancing this program.
- Escape hatch: if the stream stalls >1 week on a founder decision,
  Places Tracks **A–B** may split into a second worktree — they are the
  most file-disjoint from the other two plans. Record the split here if
  taken. **C is excluded on purpose:** C2 extracts the ranker from
  `concierge_home.py`, the one file all three plans touch, and S3 fixes a
  strict order on it. A second worktree advancing C would race that order.

### Execution errata — verified against code 2026-07-28

- **Worktree base:** create both lanes from the current local `HEAD`, not
  `origin/main`. `travel-app/main` contains the 90-commit stabilization
  stack this program's plans were verified against; `origin/main` does
  not yet contain those prerequisites. Do not run the ordinary
  `land-worktree.sh` rebase-to-`origin/main` path for the app until that
  integration base is reconciled.
- **Places A1+A2 land atomically.** A non-null provider id immediately
  enables the existing Vesper Near You save action, while today's save
  endpoint would persist that provider id without materialising it.
  A1 alone would therefore create the dead-end state Option A was chosen
  to prevent. The first Places landing includes the namespaced id,
  non-numeric consumer hardening, fingerprint dedup, and materialise-on-
  save path together.
- **Typography step 2 is incremental.** Chat's Roman 15px
  `scale='signature'`, transcript leading, and expanded serif-floor
  ratchet already landed in the mobile stabilization stack. Step 2 adds
  only the approved italic face + one ≥17px role + italic ratchet and the
  Trips serif-13 → sans-13 correction; it does not repeat the shipped
  chat landing.

## The founder decision queue

All six **ratified 2026-07-28** after adversarial analysis; each
ruling's conditions are appended to its owning plan (content lives there,
per this doc's rule).

| # | Decision | Status | Blocks step |
|---|---|---|---|
| F1 | Trips D1 — adopt `concierge_feed` | ✅ **RATIFIED**, 2 conditions → Trips plan Rulings | 4 |
| F2 | Trips D3 — extend `ConciergeHomeCard` | ✅ **RATIFIED** (slim-DTO clarification), 3 conditions → Trips plan Rulings | 4 |
| F3 | Trips row-tap destination (Deck vs trip page) | ✅ **RATIFIED: split** — actionable row → Decision Deck; `· N OPEN` → trip page | 5 |
| F4 | History sectioning | ✅ **RATIFIED: A (state-first)**, composite "open" definition mandatory → History plan | 3 |
| F5 | Vesper promotion moment (eager vs lazy draft-trip) | ✅ **RATIFIED: lazy** — a personal session becomes a trip only after explicit transcript-native confirmation | 7 |
| F6 | Places E2 — `AUTO_PUBLISH_GREEN_DOSSIERS` posture | ✅ **RATIFIED: keep off** — Reading exposes approved rows only; publication remains a manual editorial gate | 8 |

**The decision queue is closed.** F6 preserves the current content-governance
boundary instead of turning corpus size into permission to publish. Reading is
now unblocked, but it may expose only rows already carrying manual approval.

## The sequence

### 0 · Setup + hygiene *(≈1 day)*

- Create the worktree pair.
- **Vesper L0** — collapse the duplicate map bodies in
  `data/conversations.ts`. Prerequisite for every later Vesper step.
- **The four stale-doc corrections** (workbench spec §Corrections):
  concierge charter's voice-gate claim, `worker.py:212`, `types.ts:1580`,
  `ComposerBar.tsx:107`. Cheap, and they misled an agent once already.
- **Places A1** — kill `id: None` + the dedup fingerprint. The Places
  plan's own instruction: *"Start at A1… the only irreversible decision
  in the plan."*
- **Places A4** — cut Been: delete `app/(tabs)/places/been.tsx`, drop the
  marker, drop the destination. A deletion, not a deferral, and it is a
  prerequisite for step 6: D1's "572 lines move" is only true because A4
  takes `AtlasLongViewScreen` (720) out of scope first.

### 1 · Decisions + backend slices *(days 1–3)*

- **Trips Phase 1** — write the `_PRIO_*` → tier mapping + test, build
  the no-UI projection slice, honouring F1's 2 and F2's 3 ratified
  conditions. (Trips plan, Phase 1 exit criteria.)
- **Vesper L2** — the serializer cut (`intent_state.phase`,
  `current_goal`, `session_status`). ~3 hours; verified free at the DB
  layer. Unlocks step 3's sectioning.
- **Places A2** — materialise-on-save.

### 2 · Typography, once *(day 3–4)*

**One commit** touching `constants/fonts.ts`, `textVariants.ts`,
`useAppFonts.ts`, `serifFloorContract.test.ts`:

- Trips **D4 as ruled**: register the EB Garamond italic face + **one**
  named role, italic ≥17px, ratchet extended. (Founder approved
  2026-07-28.)
- The chat plan's `scale='signature'` role (serif Roman 15) — same files,
  same commit, so the two new roles land coherently.
- Serif-13 → sans-13 across the Trips scale.

This is the D4 work Trips phases 2–3 block on, done exactly once for all
three surfaces plus chat.

### 3 · The row, on a device *(days 4–6)*

- **Vesper L1** — `HRow` on History, free fields. Retires the "V" avatar.
- **Vesper L3** — sectioning per **F4 as ratified: state-first**, with
  the composite "open" definition from the History plan's ruling (never
  bare `session_status`). The old B-as-interim hedge is void — F4 is
  answered and L2 precedes L3 in this sequence anyway.
- **Vesper L4** — empty / loading / no-results states.
- **First device capture.** The program's first contact with hardware.
  History's row and Trips' docked row are the same *genre* — hairline-
  separated, mono kicker, facepile, chevron, 2-line clamp — so the
  **device lessons transfer**: how hairlines hold at 0.5px, how the
  facepile ring renders, how a clamped row grows under Dynamic Type.
  That is why this is the cheapest place to break them.

  > **They are not the same component, and must not be merged into one.**
  > `HRow` is three lines (kicker+stamp / title sans 15 / state sentence +
  > company) at `padding: 14px 0`, facepile 19, chevron 11. The Trips
  > docked row is two lines (kicker / fact sans 13) at `padding: 9px 16px`,
  > facepile 18, arrow 13, `minHeight 60`. Different information
  > architecture — `HRow` carries a title *and* a state line; the Trips
  > row's fact line *is* the content. Unifying them would either bloat
  > `HRow` with variants or silently drift the Trips geometry contract the
  > mock was measured against. Share the lessons, not the component.
- **Composer corrections** land here too (`+` slot, 17px field, `mute`
  placeholder, the dissolve) — *after* writing the small plan the
  workbench spec calls for, because `ComposerBar` is shared by four
  surfaces.

### 4 · The extraction — the item neither plan owned *(days 6–8)*

Move the Deck type block out of `useConciergeHomeState.ts`; rename
`components/focus-home/` to a neutral owner; keep the dev routes alive as
the keep-alive. Pure mechanics, no behaviour change. **This unblocks
Trips Phase 2 ("start from `Rail.tsx`") and honors Vesper's
retire-don't-delete conditions in one move.**

**Landed 2026-07-28:** `components/decision-deck/` and its neutral
`model.ts`, app `8947b1c7`. The gallery and QA routes remain alive.

### 5 · Trips 2–3 — the queue becomes real *(the long middle)*

- **Trips Phase 2** — docked rows under the existing hero (re-dress
  `Rail.tsx` per the extraction). Needs F3.
- **Trips Phase 3** — crown cutover; hysteresis with an injected clock.
- Pull-forwards the Trips plan itself suggests: **CONNECT card** and the
  **table's signal writes** (`seed_tap`/`seed_chat`/`seed_dismiss` →
  `signal_memory.py`) — both cheap, both strategically loaded.
- **Places B1–B4 interleave here** as backend work during any FE
  wait — B4 especially, since it gates dossier reachability (C6).

**Landed 2026-07-28:** Places B1–B4 are in backend `db2fd449`.
The pull-forward is also complete: backend `8120da31` records grounded
tap/chat/dismiss observations as private Personal Memory
(`shared=False`), backend `a2ad99a1` registers the cold+saves device
fixture, app `ea893043` ships the permanent zero-install CONNECT door and
select/dim/chat/dismiss behavior, and app `3bfe8fd3` + `32e35526` land
the fixture and device-found navigation-clearance corrections. Root
contract `a9c8e45` and app worktree contract `8b24a9ff` regenerate the
OpenAPI projection and consumer types.

Focused iPhone 16 Pro evidence passed on iOS 18.2:
`polish-trips-home-cold-saves-connect` selects Kyoto, exposes the
grounded chat action, dismisses it, renders the full CONNECT promise
above floating navigation, and confirms the door exits Trips. The
screen test independently proves the no-trip destination is
`/trip-begin`. Focused Jest: 20/20; TypeScript: clean; scenario registry:
28 registered; ESLint: zero errors (existing warnings only).

### 6 · Places projection + un-borrow

- **Places C1–C6** per the Places critical path. **C2 lands before any
  Vesper-side deletion of `concierge_home.py`'s near-you plumbing** — the
  ranker relay (seam S3 below).
- **Places D1** — the map un-borrow (572 lines move).
- F6 was answered before **step 8's** Reading destination made corpus size
  visible: automatic publication stays off and the destination reads approved
  rows only.

**Landed 2026-07-28:** C1–C6 and D1 are on the canonical branches. Backend
`d15cb49e` closes C3 with honest marker knowledge; app `de15ec8f` lands the
server-owned root, persisted scope rail, five-marker priority, and device
evidence; app `6181ceff` and root `c7df72b` synchronize the generated mobile
contract. The focused Places backend suite passed 180/180. The app passes
TypeScript, focused Jest, scenario-registry, and surface-index gates. The
`polish-places-projection-root` flow passed on iPhone 16 Pro / iOS 18.2 and
records the saved projection plus scope rail. This completes program step 6;
Places D2–D6 remain step 8 work.

### 7 · The Vesper cutover *(gated on step 5 complete)*

Only when Trips' crown demonstrably renders the queue:

- Retire the Vesper rail rendering + `/cards/*` routes per the workbench
  ledger's **conditional** column — the producers/ranking/models survive
  under Trips ownership (D1 = adopt).
- Re-point `notificationDestination.ts` card routes.
- Build the workbench page (read line · well · seam · ghost · composer)
  per the workbench spec's four states. Needs F5.
- **Deck expiry check** (workbench spec): if Trips shipped its queue
  *without* adopting the faces, delete them now.

Implemented and device-proven 2026-07-28 on the isolated Step 7 lanes.
Backend `65d96662` retires the four Vesper-only card feedback/lifecycle
operations while preserving the shared feed and Trips projection. App
`3f2013b7` replaces the Vesper decision rail with the three-row session
workbench, routes notification cards and the urgent seam into the Trips-owned
Deck, preserves lazy trip promotion, refreshes the Vesper 400 design canon, and
records a structured `pass` verdict. Focused evidence: backend 36 passed
(9 retired-route tests skipped), app 55 passed, TypeScript/API boundaries/design
registry passed, and both Elif/default captures passed on iPhone 16 Pro / iOS
18.2. Root contract `5bd01ee` removes the retired operations from both
snapshots. The two product commits are rebased and land-ready but are not yet
on child-repo `main`: concurrent sessions currently hold unrelated dirty
booking/invite edits in both canonical worktrees, so the final fast-forward is
intentionally deferred rather than sweeping their work into this step.

### 8 · Content + tails

- **Trips Phase 4** (companion — gate on the swap test *before* building
  the card) and **Phase 5** (table, when art direction unblocks).
- **Places D2–D5, E2** — the component layers and destinations. (E1 is
  already ruled: the corpus is an attribute of places, no browse-the-world
  surface, B4 closes reachability. No E1 work remains.)
- Deferred throughout, deliberately: voice (both paths), the
  `agent_workflows` busy flag, the named facepile. (Been is **cut** in
  step 0, not deferred — see A4.)

**In progress 2026-07-28:** app `3f2013b7` begins the Places tail with the
server-ordered `CoreSurface`, the mono `VKicker` section grammar, grounded
map/guide/place/experience/reading/area component family, independent
open/save targets, and honest unknown-hours/time states. It also repairs the
mock parity defect that forced every persona into Saved: cold now resolves to
Anywhere, default/live resolve to their real lead trip, and explicit scope
writes read back. Focused Jest passes 8/8, TypeScript and the surface registries
pass, and all four Places Workspace captures pass on iPhone 16 Pro / iOS 18.2
with a structured `pass` verdict.

Backend `917cb424`, app `6d60823b`, and contract `942befb` then close Places
D4–D5: Saved and Reading share one seven-state destination contract, the
root exposes only grounded entry doors, dossier return navigation preserves
Places ownership, and the offline root is limited to cached scope, geometry,
and personal saves with operational/editorial claims suppressed. Reading
queries approved rows only, preserving the ratified F6/E2 manual publication
gate. Focused evidence is backend 15 passed plus Ruff, app 8 passed plus
TypeScript and 28 registered polish scenarios, a green 394-operation API
reachability audit, and the passing iPhone 16 Pro / iOS 18.2 Maestro run
`direct-maestro-2026-07-29T04-19-37-613Z`. Step 8 remains in progress: this
does not claim D2's full 49-component catalogue or the gated Trips Phase 4–5
tails.

App `f3f54ac2` starts the next D2 pass with the Layer 2 row-family contract:
`PlaceList`, `PlaceRow`, `PhotoThumb`, `RelationshipMarker`, `StatusText`,
`SaveControl`, `MapSummary`, and `AreaCard` now compose through shared truth
resolvers; failed saves stay visible and retryable; and forced-offline rows
do not announce operational claims that the UI has suppressed. The default,
cold, and live registered flows pass on iPhone 16 Pro / iOS 18.2, with clean
default/live row captures and the cold flow confirming the grounded empty
state. Focused Jest passes 11/11, TypeScript and ESLint pass. This is a
device-proven Layer 2 slice, not D2 completion.

Two substrate gates now bound the next catalogue layers. Layer 5 scoped search
needs a canonical machine-readable search scope (for example a city slug or
semantic search key) from the Places projection; deriving it from the displayed
trip/city label would turn presentation copy into backend truth. Layer 6's cold
guide needs a location write seam that is not conversation/trip-bound plus a
real place-id or coordinate resolution path for starter-city selection.
`SearchEscape` is implemented but remains intentionally unwired until the first
contract exists; no location or starter-city fact is fabricated in the
meantime.

App `846083aa` continues D2 through the shippable Layer 3–4 objects.
`GuidePreview` now owns the single optional highlight shape, consumes a real
cover URL when the projection supplies one, and otherwise shows an explicit
image fallback rather than fabricated photography. `ReadingDoor` remains a
non-row—no photograph or excerpt—and exposes only its grounded title and
coverage count. `ExperienceRow` now has independent open/save targets and a
single time resolver that says `Times unconfirmed` when the projection has no
time fact. The default registered flow passes on iPhone 16 Pro / iOS 18.2 with
separate guide and reading-depth captures, opens the dossier, and returns to
Places (`direct-maestro-2026-07-29T05-13-11-817Z`). Focused Jest passes 14/14;
TypeScript, ESLint, and both Places registries pass.

The boundary remains explicit. Layer 3's carousel and shared-place variants are
still deliberately deferred; `GapPreview` still waits for Trips to distinguish
a real itinerary gap from missing knowledge. ReadingDoor is device-proven. D2
as a whole remains open.

Backend `85285a12` and app `1e0a3389` close the Layer 4 Experience projection
and device gate. The server now emits active experiences only for an authorized,
dated trip scope, proves one-off/recurring overlap against that trip window,
preserves the place's IANA timezone, and batches the traveler's personal saved
truth. Arbitrary-city and undated-trip scopes omit the section instead of
inventing temporal relevance. The app formats the machine-readable timing,
uses the server save hint, and the default mock points at an existing routable
experience rather than a display-only fixture.

Evidence is the full Places backend suite (188 passed plus Ruff), a read-only
query against the local Postgres experience corpus that returned three
timezone-correct previews, app TypeScript/test-contract/ESLint gates, focused
Jest (13 passed), and the passing iPhone 16 Pro / iOS 18.2 Maestro run
`direct-maestro-2026-07-29T05-31-05-875Z`. That device run rendered the row,
confirmed personal save state, opened the experience detail, returned to
Places, and continued through Reading. This proves the ExperienceRow slice;
it does not close the remaining D2 catalogue, the Layer 5–6 substrate
contracts, or gated Trips Phase 4–5.

Backend `fafbbcf0`, app `c59a747e`, and contract `a244b92` close the Layer 5
search-identity substrate gate. The projection now supplies a canonical trip,
corpus-place, or explicit global identity; the search route membership-checks
trip scope and expands every destination subtree. Coordinate-only city, Home,
Around Me, and Saved scopes expose no search contract yet, so the client shows
that limitation instead of searching globally under a local label.

Static evidence is 232 Places/search backend tests plus Ruff, 56 focused app
tests, both TypeScript checks, ESLint, and a current 347-operation app contract.
The runner-seeded iPhone 16 Pro / iOS 18.2 flow
`direct-maestro-2026-07-29T13-57-57-898Z` proves scoped submit, result render,
return to Places, and the independent `Search everywhere` escape. This is
device proof for the substrate and handoff only: the canon's same-surface
Layer 5 search states remain open.

Backend `c0abd4c9`, app `53cb30d7`, device-flow follow-up `28599876`,
and contract `1877c8d` close the same-surface Layer 5 search slice. Places now
owns `GET /api/places/search`: the server reads the persisted scope, reuses the
canonical BM25/hybrid venue retriever, drops non-routable identities, and
batches personal saved/in-trip/loved plus cache-only operational truth. The
only request-level scope override is the explicit `everywhere=true` escape; it
does not mutate or relabel the persisted Places scope. Retrieval relevance is
reported separately from taste score.

The app no longer leaves Places for Universal Search. Focus, typing/loading,
results, grounded empty, error, and forced-offline states replace the Places
body under the unchanged context header; cancel clears the query and restores
the contextual surface. The global escape keeps the query and can return to the
original scope. Unsupported Home, Around Me, Saved, and coordinate-only scopes
remain honestly unavailable rather than silently widening.

Static evidence is 196 Places/search backend tests plus Ruff; 19 focused app
tests, TypeScript, targeted ESLint, generated-contract validation, and the
current 348-operation app projection. The runner-seeded iPhone 16 Pro /
iOS 18.2 run `direct-maestro-2026-07-29T14-25-26-581Z` proves focused,
scoped-result, global escape/return, scoped/global empty, cancel restoration,
forced-offline, Experience, and Reading continuation in one passing flow.
This is mock-fixture device evidence, not a real-backend canary. Layer 5 is
complete; Step 8 remains open for the remaining D2 catalogue, Layer 6
substrate, and gated Trips Phase 4–5 tails.

Backend `943626b1`, app `054582c1`, device-flow follow-up `87f1b498`, and
contract `43e7311` close the Layer 6 cold-start substrate. Anywhere now returns
up to four canonical city identities ordered by approved dossier coverage plus
one approved, display-ready guide; this is corpus ordering, not
personalization. Machine taxonomy such as `local_favorite` can still contribute
city coverage but cannot leak into the guide title. The explicit
`PUT /api/places/position` action atomically writes the latest foreground fix
and Around Me scope; Places never requests permission on render, and denial or
failure leaves the prior scope unchanged.

The cold app surface exposes that deliberate location action, labelled starter
city rows that select real place ids, and the existing GuidePreview. It shows
no map until an anchor exists. After the explicit action, the runner fixture
proves the truthful state transition to a live Around Me anchor, one map result,
and an unsaved nearby place with no invented taste or relationship marker.

Static evidence is the full 196-test Places backend suite plus Ruff; 14 focused
app tests, TypeScript, targeted ESLint, generated-contract parity, and the
current 349-operation app projection. A read-only local corpus canary returned
Naples, Brooklyn, Lisbon, and Athens as the coverage leaders and the
human-readable Brooklyn guide `Counter before the crowd`. The runner-seeded
iPhone 16 Pro / iOS 18.2 run
`direct-maestro-2026-07-29T14-43-23-937Z` proves cold content, canonical city
selection, return to Anywhere, deliberate location acquisition, and the
located result. This is mock-device evidence; no real user location write was
performed. Layer 6 is complete. Step 8 remains open for the remaining D2
catalogue and gated Trips Phase 4–5 tails.

App `5135382d` and device-flow follow-up `420105a7` close the grounded
`QueryRow` catalogue slice. Empty focused search now shows only deliberately
submitted recents stored under the current user and canonical trip/place/global
scope; partially typed completions are derived only from those same recents,
not from an invented suggestion service. Query rows remain visibly distinct
from place entities and carry no place id, status, save action, or relationship
claim. Cancel now exits the mode completely by dismissing the keyboard.

Static evidence is 28 focused app tests, TypeScript, targeted ESLint, and diff
validation. The runner-seeded iPhone 16 Pro / iOS 18.2 flow
`direct-maestro-2026-07-29T15-10-16-998Z` submits `coffee`, reopens it as a
recent, derives and physically selects it from the `cof` prefix while the
keyboard remains present, and returns to the grounded place result before
continuing the existing offline, Experience, and Reading proof. This is
mock-device evidence backed by device-local recents, not a backend
autocomplete canary. The next non-gated exact-catalogue gap is the
row-geometry loading skeleton; producer-gated and deliberately deferred
variants remain outside this slice.

App `2d59829a` and device-flow follow-up `c6518881` close that exact
`RowSkeleton` gap. Search loading now uses the place row’s 60px thumbnail,
three information bands, and 84px vertical rhythm instead of the generic
notification-row placeholder; skeleton content stays out of the accessibility
tree. Device inspection also caught and fixed a shared row-family defect:
`marginLeft` had shifted every non-final row to indent its divider. Real rows
and skeletons now remain aligned while only the hairline begins after the
thumbnail.

Static evidence is 30 focused app tests, TypeScript, targeted ESLint, and diff
validation. The runner-seeded iPhone 16 Pro / iOS 18.2 flow
`direct-maestro-2026-07-29T16-47-23-280Z` holds the dev-only mock loading state,
captures the corrected geometry, then continues through grounded search,
offline, Experience, and Reading behavior. This is mock-device loading-state
evidence, not a real-network latency canary. All currently non-gated shipping
atoms in the Places D2 catalogue are now device-proven; D2 itself remains open
for `AskReading` and `GapPreview` producer gates plus the two deliberately
deferred highlight variants.

Trips Phase 4 has now entered its pre-UI content gate. Backend `94f011a1`
adds the grounded `vesper.trips.reading` composer and a matched-format blind
Reading-versus-generic-guide runner; `cead0f60` proves the shared-fact privacy
boundary, citation rejection, open-decision placement, silent failure, and
stale-section suppression. The Lisbon input preflight passes (10 facts, 7
substantive, 1 open decision), and 44 focused tests plus Ruff pass. Backend
`5f9469a9` then normalized control-only metadata and a live provider generated
the sealed A/B evidence under
`docs/audits/trip-reading-swap/2026-07-29-mara-lisbon/`. Generation alone is
not a pass. The human then selected Candidate A; the sealed key identified B
as personalized, so the swap test is **REFUTED**. Rationale and confidence
were not supplied. No route, persistence, companion card, or audio was built.
Phase 4 remains gated for composer diagnosis and a newly sealed rerun; the
failed pair and verdict remain immutable evidence.

The grounding remediation is now committed in backend `07e69de0`, with its
expanded proof in `d21eaea5`. It adds deterministic quantity/date checks, an
independent fail-closed entailment verifier, exact trip-date facts, grounded
article grammar, bounded repair, and malformed/truncated transport rejection.
Sonnet now writes the candidate after repeated Haiku grounding failures; Haiku
remains the independent verifier. The focused result is 63 passing tests plus
Ruff and diff validation.

The generated v2 artifact was rejected before human review because its
personalized article had truncated bodies; its key was never opened and the
invalid pair is preserved at
`docs/audits/trip-reading-swap/2026-07-29-mara-lisbon-v2/`. A complete v3 pair
is sealed at
`docs/audits/trip-reading-swap/2026-07-29-mara-lisbon-v3/`. Only the blind
article has been inspected. Phase 4 remains gated pending the human A/B verdict,
and no route, persistence, companion card, or audio has started.

The founder then delegated the blind decision to Codex. Codex selected B with
high confidence from the exact dates, party size, Baixa walk, Day 2 theme, and
first-dinner vote; the opened key also identified B. This is recorded as
**SUPPORT from a blinded evaluator**, not mislabeled as the pre-registered
traveler-human test. The founder then explicitly ratified that delegated
evidence as sufficient and authorized continuation. Phase 4 has therefore
passed its content gate without rewriting the evaluator class.

The post-gate slice is now implemented on the isolated lanes: one group-shared
Reading persists per trip, regenerates from fresh shared truth after itinerary
commit and at T-7, suppresses stale cited sections at read time, and exposes a
membership-gated citation-free API without composing on page load. The app
selects the live trip or otherwise nearest upcoming trip, renders a collapsed
companion card, deep-links exact sections into a focused reader, and sends the
visible closing thread only into a private trip-scoped Vesper conversation.
Mock mode returns `null` for unseeded trips rather than fabricating prose.
Backend targeted evidence includes the earlier 130-test pass and a final
94-test focused rerun, plus Ruff, pre-commit policy guards, and a single Alembic
head. App typecheck, lint, API boundaries, mock/client parity, focused Reading
tests, scenario registry, and design-reference checks pass. The generated full
and mobile OpenAPI snapshots are synchronized.

The Elif mock-device receipt now passes on iPhone 16 Pro / iOS 18.2. It proves
the collapsed default, expanded exact-section index, section-targeted reader,
private thread affordance, and explicit return to Trips. The structured
`trips-home-reading-2026-07-29` verdict is `pass`; it records two non-blocking
P2 overlaps in the long full-screen capture (floating navigation over the
Reading teaser and the create control over a queued-row action). Backend
`7bb5abab` and app `c3976b93` close the implementation plus mock-device UI
gate.

The local backend-real canary now also passes. An isolated clone of the Elif /
Rome dogfood database was migrated to `tripreading01`; a deterministic
citation-grounded Reading was persisted through the real repository; the public
route returned a citation-free `200` to Elif and `403` to a non-member; and the
iOS 18.2 simulator forced real API mode, fetched the canonical trip UUID, and
rendered the collapsed card, expanded index, focused reader, and return path.
App `e70bae97` preserves that forced-real Maestro flow and aligns the Elif mock
copy with the canonical dogfood facts.
The receipt and captures live under
`docs/audits/trip-reading-canary/2026-07-29-elif-rome/`. This closes the
backend-canary implementation gate, not live dogfood: no provider credential,
Clerk auth, EAS build, or physical device was involved, and the seeded prose is
not represented as provider-generated. That layer-4 receipt remains a release
gate. Audio remains deliberately deferred.

## The four seams

The places where two plans touch one artifact. The rule at every seam:
**say so in the commit message.**

| # | Seam | Rule |
|---|---|---|
| S1 | `concierge_feed` | Trips D2's rule, now program-wide: neither surface forks the ranker; a producer or `_PRIO_*` change moves **both** surfaces and Vesper's hero grounding. **Upgraded from convention to guard by F1's condition 2** — a golden-fixture test asserts the Trips projection's #1 candidate == the Vesper hero's focus card for identical input. Lands in step 1; after that this seam fails CI rather than relying on someone remembering the commit message. |
| S2 | `components/focus-home/` → `components/decision-deck/` | Extracted once in step 4 (`8947b1c7`). Trips re-dresses; Vesper retires its route. Nobody edits the retired pre-extraction path. |
| S3 | `concierge_home.py` | Three plans touch it. Order: Trips projection **added** (1) → Places C2 extracts the ranker (6) → Vesper deletes rendering + `/cards/*` (7). Deletions last. |
| S4 | Typography files | Step 2 only. After it lands, new type roles go through the ratchet like everything else. |

## Stop conditions

The escape hatch above covers *scheduling* stalls. This covers **technical
failure**, which it did not.

**Step 5 is the pivot.** Everything from step 6 on assumes the projection
works — step 7 in particular *retires* Vesper's rail and `/cards/*`
routes on that assumption. So:

- **Do not begin step 7 until Trips' crown demonstrably renders the queue
  on a device.** Already stated as step 7's gate; restated here because it
  is the program's one irreversible threshold.
- **If Trips Phase 2–3 cannot render the queue** — the projection loses
  information the rows need, hysteresis proves unworkable against the
  ranker's refresh cadence, or the golden-fixture seam test cannot be made
  to pass — **stop and reassess the program, not just the step.** F1's
  adoption ruling is the load-bearing assumption; if adoption fails in
  practice, step 7's retirement plan and S3's deletion order both need
  rewriting before anything else proceeds.
- **Everything through step 6 is independently valuable** if the program
  halts there: the typography lands once, History ships its row, Places
  gets its projection and un-borrow, and the ranker is untouched. Nothing
  before step 7 is a bet on the stack model succeeding.

Record any halt here with the date and reason, the way completions are
recorded below.

## Terminus — ruled by founder 2026-07-29

**This program is the last private design iteration.** Standing rule from
here: no new redesign cycle begins without new *external* evidence between
cycles.

The program ends at the **wedge bar**, not the vision bar — the test is
"four people coordinate a real trip here instead of their group chat,"
NOT "the founder feels the world model." Real users compare against
WhatsApp; only the founder can see what's missing. Concretely, polish
stops when:

1. The **organizer's first five minutes** and the **joiner's first five
   minutes** each work end-to-end without apology.
2. **One full trip loop** runs with real data — decide → queue → claim →
   capture → settle — even if rough at the edges.

When the bar passes, the next step is external contact, in order:
(a) five strangers, ten minutes each, first-touch ("what is this? what
would you do?") — the only instrument that can answer whether the
aesthetic register fits the social job; (b) one real trip with one real
group, read via `scripts/invite_loop_funnel.py` + the three numbers
(re-invite, money attach, chat displacement).

If step 8 completes and the bar doesn't pass, that is a finding to
record here — not a reason for a step 9.

## Contradictions resolved by this doc

- **Italic.** Trips D4 (founder, 2026-07-28) supersedes the workbench
  spec's blanket "no italic." Correct reading: no italic *until step 2
  lands the face + role*; never below 17px; History rows and the chat
  transcript are sans and unaffected; the 15px chat byline stays Roman
  (below the floor). The workbench read line's gold-weight emphasis may
  adopt italic after step 2 for cross-home rhyme — decide then, not now.
  *(Workbench spec errata applied 2026-07-28.)*
- **The workbench spec's open decisions 1–2** are substantially answered
  by the Trips plan (finding 3 + D1): the Deck is reused, the ranker is
  shared. The page's real gate is **step 5 complete**, not abstract
  decisions. *(Errata applied.)*

## State

| Step | Status | Commit |
|---|---|---|
| 0 · Setup + hygiene | complete 2026-07-28 | agent `c55e7819`, `42efbfe8`, `71681013`; app `4ffe418d`, `32594311`, `cc94b84c`; docs `2354f86` |
| 1 · Decisions + backend slices | complete 2026-07-28 | agent `3a99ed5a`, `0cda2748`; app `63dca2b6`, `25a862bb`; docs `72eba35` |
| 2 · Typography, once | complete 2026-07-28 | app `aee56838` |
| 3 · The row, on a device | complete 2026-07-28 | app `f74dbafb`, `b9138405`, `27a009d8`, `8bde3c98`, `06af07c9`, `7f36afe2`, `b4b4e745`; docs/evidence `8647fce` |
| 4 · The extraction | complete 2026-07-28 | app `8947b1c7` |
| 5 · Trips 2–3 | complete 2026-07-28 — phases 2–3, Places B1–B4, CONNECT, and private grounded signal writes landed with device proof | agent `76f534ba`, `db2fd449`, `8120da31`, `a2ad99a1`; app `eaeb3627`, `08dc9d19`, `14280999`, `a68c5755`, `4e375e67`, `3bfe8fd3`, `32e35526`; contract `a9c8e45`, `8b24a9ff`; verdict `4cb5e342` |
| 6 · Places projection + un-borrow | complete 2026-07-28 — C1–C6 and D1 landed; the server-owned root, persisted scope, and marker priority are device-proven | agent `b05be32d`, `17c0cf5d`, `84ccc496`, `e859f0e5`, `b95f97de`, `d15cb49e`, `bd8a83a4`; app `8d676b4f`, `de15ec8f`, `6181ceff`; contract `6ed14cf`, `63395a2`, `c7df72b` |
| 7 · The Vesper cutover | complete + device-proven 2026-07-28 on isolated lanes; child-main landing deferred behind concurrent dirty worktrees | agent `65d96662`; app `3f2013b7`; contract `5bd01ee` |
| 8 · Content + tails | in progress 2026-07-29 — Places D3–D6, destinations/offline, and every currently non-gated D2 shipping atom are device-proven; founder-ratified v3 evidence opened Trips Phase 4, and the persisted membership-gated Reading plus companion card/reader now pass mock-device and local backend-real simulator gates. Layer-4 provider/Clerk/EAS dogfood remains a release gate; AskReading/GapPreview producer gates, deferred highlight variants, and Trips Phase 5 remain; audio is explicitly deferred | agent `917cb424`, `85285a12`, `fafbbcf0`, `c0abd4c9`, `943626b1`, `94f011a1`, `cead0f60`, `5f9469a9`, `07e69de0`, `d21eaea5`, `7bb5abab`; app `3f2013b7`, `6d60823b`, `f3f54ac2`, `846083aa`, `1e0a3389`, `c59a747e`, `53cb30d7`, `28599876`, `054582c1`, `87f1b498`, `5135382d`, `420105a7`, `2d59829a`, `c6518881`, `c3976b93`, `e70bae97`; contract `942befb`, `a244b92`, `1877c8d`, `43e7311` |

Update this table as steps land. One line per completion, with the
commit hash.
