---
doc_type: working
status: active
owner: founder / eng
created: 2026-07-28
expires: 2026-08-27
why_new: The stack-model spec is a design spec — it says what to build and why, but not which modules, in what order, or how you know a phase is done. This is the executable counterpart, written after tracing the shipped home-feed code.
source_of_truth_for:
  - trips-home-stack-build-plan
depends_on:
  - docs/working/trips-home-promotion-model-2026-07-27.md
---

# Trips Home — Stack Model build plan

Companion to `trips-home-promotion-model-2026-07-27.md` (the design spec,
which is self-contained and does not repeat here). **This doc answers
"how", the spec answers "what and why".** Read the spec first.

Design reference: Claude Design → Vesper → `Vesper Trips Home - Stack
Model (Sans).html`, also exported to the handoff bundle at
`~/Downloads/vesper 400/project/`.

---

## What investigation changed (read this before planning anything)

Three findings from tracing the code. Two of them invalidate assumptions
the spec was written on. **None were knowable from the mock.**

### 1 · The ranker already exists. Phase 1 is adoption, not construction.

The spec's phase 1 — "item registry + ranker (backend): item contract,
derive items from existing sources, cross-trip ladder + imminence
tiebreak" — describes something that is **already built, deployed, and
serving a live surface**:

`travel-agent/backend/home/concierge_feed/` — 3,835 lines across
`producers.py` (2,279), `ranking.py` (815), `models.py` (723).

| Spec says the stack needs | `concierge_feed` already has |
|---|---|
| one ranked queue **across all trips** | scoped to one `user_id`, all trips |
| **deterministic** ranking | no LLM in the assembler |
| item #1 blooms, rest dock as rows | one `now_card` hero + a `next_moves` rail |
| voice **composed on promotion**, not on render | hero voice fired by the route *after* assembly |
| a tier ladder | a 26-value numeric priority ladder (`_PRIO_*`, 96 → 20) |
| ranker weights as tunables | `_load_feedback_tuning()` — learned, per-user |
| — | twin suppression, phase awareness, best-effort error isolation |

It serves the **Concierge tab** (`FocusHome`), not Trips home. And
`app/(tabs)/trips/index.tsx:632` **already prefetches it** — purely to
warm the cache for a tab switch, but the query handle is there.

The spec's 5-tier ladder is not a competing design; it is a *coarser
vocabulary* over the same idea. The existing `_PRIO_*` values map onto it
cleanly — `_PRIO_BOOKING_HOLD_OFFER 96` / `_PRIO_CATCH_RESCHEDULE 93` are
tier 0, `_PRIO_LIVE_TRIP 92` is tier 1, `_PRIO_PROPOSAL_DECISION 94` and
`_PRIO_GROUP_COMMITMENT 65` are tier 2, `_PRIO_STORY_READY 84` and
`_PRIO_MEMORY_ECHO 46` are tier 3, and the starters (22/21/20) are the
floor.

**Building a second ranker beside this one would be the most expensive
mistake available.** Phase 1 is therefore a decision phase, not a
construction phase.

### 2 · Two spec requirements cannot ship as written

Both verified directly, not taken on report.

**a. Serif italic is unimplementable.** The spec requires italic in the
crowned read's emphasis phrase and the companion's thread quote.

- `constants/fonts.ts` registers EB Garamond 400/500/600/700 — **Roman
  only**. `hooks/useAppFonts.ts` loads exactly those four.
- The contract is explicit: *"Production is Roman-first: italic faces are
  intentionally not registered yet… never synthesize or register slant at
  an individual call site."*
- `grep "fontStyle: 'italic'"` over `components/ constants/ app/ hooks/`
  → **one hit, and it is a comment** in `app/you/feedback.tsx:160`
  recording that a synthetic slant was *removed*.

Setting `fontStyle:'italic'` on a Roman-only family yields synthesized
oblique on Android and inconsistent results on iOS. Registering the face
is a real decision with a real cost (bundle size, a new semantic role),
and the contract says the face and the named role must be added together.

**b. The serif type scale violates a CI-enforced floor.** The spec's
scale lists five serif sizes: 32 / 22 / 18.5 / 17 / **13**.

`__tests__/conventions/serifFloorContract.test.ts` enforces
`SERIF_FLOOR = 15` as a **ratchet**: existing sub-floor sites are
baselined (`serifBodySm@13`, `serifBodyStrong@14`), counts may only go
down, and **any new sub-floor serif fails the suite immediately.**

The prescribed remedy is in the contract and should be followed rather
than re-litigated: *"FIXING A VIOLATION IS A TRIAGE, NOT A BUMP… the
correct fix is usually System Sans — which at the SAME px is larger in
apparent size, so it does not reflow the box."*

So serif-13 in the mock becomes **sans-13**, not serif-15. This costs
nothing visually (sans at 13 reads larger than serif at 13) and it is
what the register rule already wanted — 13 is row/metadata territory,
which the spec assigns to sans anyway. *The mock was inconsistent with
its own rule; the codebase caught it.*

> This is the third time this design has specified something the shipped
> code already refuses — after the cold-start seed grid and the serif
> over-use. The pattern is worth naming: **the mock is not a constraint
> system.** Check `constants/`, the convention tests, and the surface's
> own doctrine comments before ratifying a visual decision.

### 3 · `Vesper Home - Workbench` is a different surface

The handoff bundle's README flags `Vesper Home - Workbench.html` as the
primary design, because it was the open file at export time. It is not
this project — it is **Vesper Home** ("Trips owns objects, Vesper owns
sessions"), a concurrent initiative, matching the untracked
`chat-typography-plan-2026-07-28.md` in this repo. Do not build it from
this plan, and do not let its README line redirect the work.

---

## Phase 1 — Decisions (the phase everything else adapts to)

**Phase 1 produces decisions and one thin vertical slice, not a
subsystem.** Its job is to resolve the four questions below, because
phases 2–5 branch on them. Estimate: 2–4 days, most of it reading and
arguing, not typing.

### D1 · Does the stack adopt `concierge_feed`, or get its own producers?

| | Adopt + extend | Build parallel |
|---|---|---|
| Cost | learn 3,835 lines; risk destabilizing a live surface | ~2 weeks rebuilding producers that exist |
| Gets for free | 26 producers, feedback tuning, twin suppression, phase logic, error isolation | nothing |
| Risk | Concierge tab and Trips home now share a spine — a change to ranking moves both | two rankers drift; the same trip state produces different judgments on two surfaces |

**Recommendation: adopt.** The parallel option's real cost is not the two
weeks — it is that two rankers over the same trip state *will* disagree,
and the product's whole claim is that the page exercises judgment. Two
surfaces making different judgments about the same trip is the most
expensive bug this design can have.

**What adopting actually means:** the stack model is a **new projection**
of `assemble_concierge_home_feed()` — a second response shape over the
same ranked candidates, not a fork of the ranker.

### D2 · If adopted — what happens to the Concierge tab?

This is a **product** decision, not an architecture one, and it is the
one that most needs the founder rather than an agent.

If Trips home renders a cross-trip ranked queue, and the Concierge tab
renders a cross-trip ranked queue, they are the same page in two
fidelities. Three coherent answers:

1. **Trips home becomes the queue; Concierge stays sessions.** Concierge
   keeps the Vesper-presence surface it already migrated to
   (`app/(tabs)/concierge/index.tsx` is already "a state machine, not a
   conversation list"); `FocusHome` retires or narrows to the Deck
   experience. Cleanest story, matches the Workbench session's framing
   ("Trips owns objects, Vesper owns sessions"). **Recommended.**
2. **Both render it, different fidelities** — Trips as the six-section
   page, Concierge as the full-screen Deck. Defensible, but needs an
   explicit rule for why a traveller would visit both.
3. **Concierge keeps the queue; Trips home stays a roster.** Rejects the
   stack model. Listed for completeness.

**Blocking.** Do not start phase 2 without an answer — phase 2 is FE work
whose target surface this determines.

### D3 · The item contract — extend `ConciergeHomeCard` or introduce `Item`?

The spec defines `Item { kind, trip_id, facts, receipt, step, row_line,
hero_eligible, tier, freshness }`. `ConciergeHomeCard` already carries
most of this in different clothes.

**Recommendation: extend, and add only what is genuinely missing** —
which is essentially three fields:

- `row_line` — the one-line docked fact, with a hard character budget.
  **This is the real new work**, and it is a *composition* problem, not a
  schema one: 26 producers each need a row-line voice that obeys
  names-not-fractions.
- `tier` — the coarse 0–4 bucket, derived from the existing `_PRIO_*`
  value, not stored independently. One mapping function, one test.
- `depth` — the count behind the cursor rule (`· 3 OPEN`).

`hero_eligible` already exists in spirit (the now_card/next_moves split).
`freshness` and `receipt` have equivalents. **Do not introduce a parallel
type**; that is D1's mistake wearing a smaller hat.

### D4 · Typography reconciliation — resolve before any FE work

Three sub-decisions, all cheap, all blocking phase 2/3:

- **Italic:** either register an EB Garamond italic face with a named
  semantic role (per the contract's "face and role together" rule), or
  **drop italic from the spec** and mark emphasis another way (weight, or
  the existing `goldDeep` colour shift the mock already uses for
  `strong`). *Recommend dropping* for v1 — the emphasis phrase is
  backend-verified via `_cited_verbatim` and can be marked without slant;
  registering a face to serve one phrase is a poor trade.
- **Serif 13 → sans 13** everywhere in the scale, per the ratchet's own
  triage guidance. No visual loss.
- **Confirm the remaining serif sizes** (32 / 22 / 18.5 / 17) against
  `constants/textVariants.ts` roles rather than inventing new ones.

### Phase 1 exit criteria

- [ ] D1–D4 answered in writing, appended to this doc
- [ ] `_PRIO_*` → tier 0–4 mapping written, with a test asserting every
      existing `_PRIO_*` constant maps to exactly one tier
- [ ] One vertical slice proving the projection: `GET` the existing feed,
      project the top candidate + 2 next_moves into the stack shape,
      assert against a fixture. **No UI.**
- [ ] The spec doc updated with the D4 outcome (it currently specifies
      italic and serif-13, both of which are wrong)

---

## Phases 2–5, branched on phase 1

Each phase states what it becomes under each D1/D2 outcome, so the plan
survives either answer.

### Phase 2 — Stack rows on the existing page

Render docked rows beneath the *current* hero, which stays composed the
old way. Visually the stack model's skeleton with old crown logic — the
lowest-risk way to learn whether rows get tapped.

- **If D1 = adopt:** consume the projection from phase 1. FE work is
  `TripsHomeViews.tsx` + a new row component matching the geometry
  contract (`ROW_H 60` as `minHeight`, 2-line clamp — *not* a fixed
  height; the mock proved fixed height clips at 120% text).
- **If D1 = parallel:** phase 2 cannot start; it waits on producers.
- **If D2 = Concierge keeps the queue:** phase 2 targets `FocusHome`
  instead, and the whole plan becomes a Concierge redesign.

Exit: rows render in busy and quiet states; Dynamic Type verified at
100/120/135% **on device, not in the mock**; row taps instrumented (the
falsifier "docked rows go untapped AND their facts go unmissed" needs
data from here).

### Phase 3 — Crown cutover

The bloom is driven by the crowned item: receipt and step come from the
item, voice composed at promotion. Facepile + empty chair land in the
identity block.

- Depends on **D3** for the item shape and **D4** for how emphasis
  renders without italic.
- The `agent_work` kind reuses the shipped `WorkReceiptPayload` — it
  needs this cutover to render at all, so it is a free win here rather
  than new work.
- **Crown hysteresis** (a promotion holds for the day; only tier 0 usurps
  intraday) is the highest-risk logic in the whole build and the easiest
  to get subtly wrong. Write it with a clock injected, and test the
  intraday-usurp and day-boundary cases explicitly.

Exit: crown matches the ranker's #1 across all seven page states;
suppression path verified — **composition failure renders the defined
receipt with no prose**, never a softened invention.

### Phase 4 — Companion

The only net-new content system, and the only phase that does not depend
on D1. It needs the trip-reading composer built on the Atlas compose
engine.

Gate it on the **swap test** stated in the spec: show a traveller their
Reading and a generic city guide for the same city; if they cannot tell
which is theirs, the feature fails. Run that before building the
collapsed-card UI, not after — the card is cheap, the composer is not.

### Phase 5 — Table + CONNECT

Seed derivation (taste-backs first), select/dim/chat interaction, and the
dismissal signal write to `signal_memory.py` (`seed_tap` / `seed_chat` /
`seed_dismiss`).

- **Blocked on the tabled art direction** — but only for the cells.
  The *signal writes* are not blocked and are independently valuable:
  they are the plumbing answer to the affinity-ranker that the roadmap
  validation refuted for want of cold-start signal. **Consider pulling
  the signal writes forward into phase 2** if the table slips.
- CONNECT ships here or earlier — it is one static card with no ranking
  dependency, and it is the wedge. It could ship in phase 2 as the
  cheapest thing on this list.
- Respect the corrected cold start: **cold renders the invitation, not a
  fabricated seed grid.**

---

## Sequencing note

Phases 2–3 are re-plumbing and can precede the Reading entirely. Phase 4
is the only net-new content system. Phase 5's signal writes should be
pulled forward if the art direction stays tabled — they are the part with
strategic value, and they do not need pixels.

## What this plan does not cover

- Ranker weight tuning (spec calls these build-time tunables; they need
  cohort data, not a plan)
- The four unmocked item kinds (`overlap_match`, `group_echo`,
  `agent_work` receipt, `story` ready) — design gap, tracked in the spec
- "All trips" destination — three artboards exist on the shipped canon
  page; carry them over rather than redrawing
- Promotion of the design page CANDIDATE → CANON, which is governance,
  not build
