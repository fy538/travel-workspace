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

Three of six **ratified 2026-07-28** after adversarial analysis; each
ruling's conditions are appended to its owning plan (content lives there,
per this doc's rule).

| # | Decision | Status | Blocks step |
|---|---|---|---|
| F1 | Trips D1 — adopt `concierge_feed` | ✅ **RATIFIED**, 2 conditions → Trips plan Rulings | 4 |
| F2 | Trips D3 — extend `ConciergeHomeCard` | ✅ **RATIFIED** (slim-DTO clarification), 3 conditions → Trips plan Rulings | 4 |
| F3 | Trips row-tap destination (Deck vs trip page) | ✅ **RATIFIED: split** — actionable row → Decision Deck; `· N OPEN` → trip page | 5 |
| F4 | History sectioning | ✅ **RATIFIED: A (state-first)**, composite "open" definition mandatory → History plan | 3 |
| F5 | Vesper promotion moment (eager vs lazy draft-trip) | open — leaning lazy | 7 |
| F6 | Places E2 — `AUTO_PUBLISH_GREEN_DOSSIERS` posture | open | 8 |

**The stream is unblocked through step 6.** F5 is the next remaining
gate (step 7); F6 has runway through step 7.

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
- F6 has lead time from here: it must be answered before **step 8's**
  Reading destination makes corpus size visible to users.

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

### 8 · Content + tails

- **Trips Phase 4** (companion — gate on the swap test *before* building
  the card) and **Phase 5** (table, when art direction unblocks).
- **Places D2–D5, E2** — the component layers and destinations. (E1 is
  already ruled: the corpus is an attribute of places, no browse-the-world
  surface, B4 closes reachability. No E1 work remains.)
- Deferred throughout, deliberately: voice (both paths), the
  `agent_workflows` busy flag, the named facepile. (Been is **cut** in
  step 0, not deferred — see A4.)

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
| 7 · The Vesper cutover | not started | |
| 8 · Content + tails | not started | |

Update this table as steps land. One line per completion, with the
commit hash.
