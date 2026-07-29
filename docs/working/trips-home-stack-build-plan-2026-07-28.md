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

Design reference: Claude Design → Vesper project →
**`Vesper Trips Home - Stack Model (Sans).html`** plus its four
`trips-home-stack-sans*.jsx` support modules. That page is the durable
reference.

A snapshot was also exported to
`/Users/feihuyan/Downloads/vesper 400/project/`. **Treat that path as
transient** — these are numbered handoff exports and new ones keep
arriving (394…400 as of 2026-07-28), so a later bundle likely exists by
the time you read this. Prefer the design project; use a bundle only for
offline reading, and check you are in the newest one. Its README names
whatever file was open at export time as "the primary design" — in 400
that is `Vesper Home - Workbench.html`, which is **a different surface
from a different plan.** Ignore that line.

> **Scope: Trips home only.** Vesper/Concierge home is a separate plan
> and a separate session. Where the two touch — both consume the
> `concierge_feed` ranker — this doc records the coordination rule (D2)
> and nothing more. It does not decide anything about that surface.

## Handover state (2026-07-28)

**Decided — do not relitigate:**

- **D1 — RATIFIED 2026-07-28 (founder): adopt `concierge_feed`.** Two
  binding conditions — see **Rulings** at the end of this doc.
- **D3 — RATIFIED 2026-07-28 (founder): extend, with the slim-DTO
  clarification.** Three binding conditions — see **Rulings**.
- **D2** — coordination rule only; Vesper/Concierge home is a separate
  plan. Not blocking.
- **D4 typography** — italic **approved** as a limited register (Vesper
  voice only), subject to the face/role, 17 px floor and ratchet
  conditions in D4. Serif-13 **removed** from the scale → sans-13.
- **Row-tap destination — RATIFIED 2026-07-28 (founder): split by
  intent.** An actionable row opens that item's Decision Deck. The
  `· N OPEN` depth affordance opens the trip page. See **F3** under
  Rulings.

**Landed so far:** Phase 1 backend `3a99ed5a`, mobile consumer
`63dca2b6`; shared typography step `aee56838`.

> Agents: the repos are `/Users/feihuyan/travel-workspace/travel-app`
> (FE) and `/Users/feihuyan/travel-workspace/travel-agent` (BE). Use
> literal absolute paths — the launched cwd may be elsewhere.

---

## What investigation changed (read this before planning anything)

Four findings from tracing the code. Two invalidate assumptions the spec
was written on; one materially shrinks the build. **None were knowable
from the mock.**

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

### 3 · The FE components exist too — phases 2–3 are a redraw, not a build

`components/decision-deck/` already contains the stack's anatomy, built and
tested: **`HeroVoice`** (the bloom), **`Rail`** (docked rows, tapping
through via `onOpenDeck`), and **`Deck`** with `DeckPickFace`,
`DeckBriefFace`, `DeckCallFace`, `DeckStructuredFace`,
`DeckNearYouFace`.

This is the shipped **Card↔Deck two-level system**
(`travel-agent/docs/specs/card-deck-two-level.md`): a card and its
full-screen Deck are two fidelities of one object — level 1 *presents*
the decision, level 2 *helps make* it. Its governing rule is already the
one the stack model needs:

> the glance is a **projection** of the focus, never a separate
> generation

That is precisely the relationship between an item's `row_line`, its
crowned read, and its Deck. **The stack model should be read as the
cross-trip glance layer of this existing system, not as a new one.**

Consequence for scope: **phases 2–3 are substantially a redraw and a
relocation, not new construction.** The row component needs the stack's
geometry contract and the six-section grammar is genuinely new, but the
hero/rail/deck spine and the four Deck faces are reused as-is. Budget
accordingly — the plan's original phase 2–3 estimate assumed building
what already exists.

**Open sub-question, decide deliberately rather than inherit:** the spec
says tapping a docked row opens *that trip*; `Rail.tsx` today opens *that
item's Deck*. Both defensible — the trip page is the full ledger, the
Deck is the decision. Suggested resolution: Deck for actionable items,
trip page for the `· 3 OPEN` depth affordance.

### 4 · `Vesper Home - Workbench` is a different surface

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

### D2 · Consume the shared ranker without forking it

**Scope note: Vesper/Concierge home is a separate plan and a separate
session. This plan does not decide that surface's fate.** What Trips home
owns is narrower, and it is not a product decision:

**Trips home consumes `concierge_feed` as a new projection and changes
nothing about how any other surface consumes it.** The projection is
additive — a second response shape over the same ranked candidates.

The only thing to hold is a **coordination seam**: `concierge_feed` is
now a shared dependency of two independently-planned surfaces. Two rules
follow, and they are cheap:

- **Neither surface forks the ranker.** Divergent judgment about the same
  trip state is the failure this whole model exists to prevent.
- **Producer changes are shared changes.** Adding a producer or moving a
  `_PRIO_*` value moves both surfaces. Say so in the commit.

If the Vesper-home plan retires, narrows, or redraws its use of the feed,
that is their call and it does not block anything here — the projection
Trips home consumes is independent of whether another surface renders its
own.

**Not blocking.** Phase 2 can start once D1, D3 and D4 are answered.

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

- **Italic: APPROVED 2026-07-28 (founder) — limited register.** This
  takes the contract's own sanctioned path, which has conditions
  attached; they are not optional:
  - **Register the face and a named semantic role together.** The
    contract is explicit — *"add the face and named semantic role
    together; never synthesize or register slant at an individual call
    site."* So: add the EB Garamond italic face to `hooks/useAppFonts.ts`
    and `constants/fonts.ts`, and add **one** named role in
    `constants/textVariants.ts` that owns it. No `fontStyle:'italic'`
    at any call site, ever.
  - **Italic never renders below 17px** (`constants/fonts.ts`, decided
    2026-07-27). **Check both italic sites against this before building**
    — the crowned read's emphasis phrase should clear it comfortably, but
    the companion's thread quote is a small row and may not. If the quote
    sits below 17, it moves up to 17 or gives up italic; it does not get
    a synthesized exception.
  - **Extend the floor ratchet.** `serifFloorContract.test.ts` currently
    enforces serif ≥15. Add the italic ≥17 rule to it in the same change,
    or the new register has no guard and will drift exactly the way the
    serif floor did.
  - Scope stays *limited*: italic marks the Vesper voice — the read's
    emphasis phrase and the quoted thread line. It is not available for
    editorial titles, metadata, or decoration.
- **Serif 13 → sans 13** everywhere in the scale, per the ratchet's own
  triage guidance. No visual loss.
- **Confirm the remaining serif sizes** (32 / 22 / 18.5 / 17) against
  `constants/textVariants.ts` roles rather than inventing new ones.

### Phase 1 exit criteria

- [x] D1–D4 answered in writing, appended to this doc
- [x] `_PRIO_*` → tier 0–4 mapping written, with a test asserting every
      existing `_PRIO_*` constant maps to exactly one tier
- [x] One vertical slice proving the projection: `GET` the existing feed,
      project the top candidate + 2 next_moves into the stack shape,
      assert against a fixture. **No UI.**
- [x] The spec doc updated with the D4 outcome — serif-13 → sans-13, and
      the italic register's conditions (face + named role together,
      17px floor, ratchet extended)

**Landed 2026-07-28.** Backend `3a99ed5a` adds the projection, exhaustive
tier guard, S1 golden fixture, slim-wire guard and endpoint. App
`63dca2b6` moves the existing Trips prefetch onto that endpoint without
changing rendered hierarchy. Typography implementation remains program
step 2; this phase answered and recorded D4, as its exit criterion
requires.

---

## Phases 2–5, branched on phase 1

Each phase states what it becomes under each D1/D2 outcome, so the plan
survives either answer.

### Phase 2 — Stack rows on the existing page

**Landed 2026-07-28:** the adopted projection now renders docked rows
under the existing hero and routes row bodies to their Decision Deck while
the separately labelled `· N OPEN` depth control opens the trip. App
`eaeb3627`, lifecycle-action correction `08dc9d19`; device checks passed at
100%, 120%, and 135% Dynamic Type.

Render docked rows beneath the *current* hero, which stays composed the
old way. Visually the stack model's skeleton with old crown logic — the
lowest-risk way to learn whether rows get tapped.

- **If D1 = adopt:** consume the projection from phase 1. FE work is
  `TripsHomeViews.tsx` plus a row component matching the geometry
  contract (`ROW_H 60` as `minHeight`, 2-line clamp — *not* a fixed
  height; the mock proved fixed height clips at 120% text). **Start from
  `components/decision-deck/Rail.tsx`**, which is the same anatomy already
  built and tested — re-dress it to the stack's contract rather than
  writing a new row from scratch.
- **If D1 = parallel:** phase 2 cannot start; it waits on producers.

Exit: rows render in busy and quiet states; Dynamic Type verified at
100/120/135% **on device, not in the mock**; row taps instrumented (the
falsifier "docked rows go untapped AND their facts go unmissed" needs
data from here).

### Phase 3 — Crown cutover

**Landed 2026-07-28:** the crown now owns identity, grounded voice,
receipt, step, facepile, empty chair, and docked rows. Durable promotion
hysteresis holds within the UTC day, permits tier-0 intraday usurpation, and
refreshes at the day boundary with an injected clock. Backend `76f534ba`;
app `14280999`, `a68c5755`, `4e375e67`; structured surface verdict
`4cb5e342` is intentionally MIXED and records the remaining returned-state
and fixed-chrome defects rather than treating capture as certification.

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

**Gate implementation landed 2026-07-29; verdict still pending.** Backend
`94f011a1` adds the pre-UI `vesper.trips.reading` composer and blind A/B
runner; `cead0f60` adds its privacy and grounding proof. The composer receives
an explicit allowlist of shared destination/date/party-size, itinerary display,
and open-decision facts. It cannot see member briefs, group-profile prose,
planning rationales/notes, or private user context. Every title, section, and
thread line must cite the allowlisted fact IDs; unknown citations, a weak
substantive spine, misplaced open-decision copy, transport failure, or stale
facts suppress rather than generate a generic fallback. No route, persistence,
card, or audio was added.

The Lisbon source preflight passes with 10 facts (7 substantive, 1 open
decision), and 44 focused tests plus Ruff pass. The repository-wide offline
suite reached 14,873 passed / 29 skipped with 15 failures outside this slice
(venue/site field-consistency drift, dogfood snapshot/identity drift, retired
Concierge lifecycle tests, and a scheduled-workflow assertion).

The canonical backend's local provider credential then generated the matched
blind pair after `5f9469a9` fixed control-only metadata normalization; the
production personalized candidate remained under the strict line and grounding
guards. Evidence is sealed at
`docs/audits/trip-reading-swap/2026-07-29-mara-lisbon/`: the traveller must
judge `blind.md` before anyone opens `answer-key.json`. Generation is live-model
eval evidence, not a passing verdict.

**REFUTED 2026-07-29.** The human selected Candidate A; the sealed key
identified Candidate B as the personalized Reading. No rationale or confidence
was supplied. The mismatch is recorded without reinterpretation in
`docs/audits/trip-reading-swap/2026-07-29-mara-lisbon/verdict.md`. Per the
pre-registered rule, Phase 4 remains gated and the collapsed-card UI must not
start. Diagnose the composer, preserve this failed pair, and run a newly sealed
swap after revision.

**Remediation landed 2026-07-29; revised human verdict pending.** Backend
`07e69de0` adds deterministic quantity/date citation checks, a separate
fail-closed semantic-entailment verifier, exact date/duration facts,
fact-grounded title/heading/decision projections, bounded repair attempts, and
strict transport/completeness recovery. The writer moves to Sonnet after
repeated Haiku grounding failures; the independent verifier remains Haiku.
Backend `d21eaea5` covers the privacy boundary, malformed structured output,
truncation, quantity/date rejection, exact-fact handling, semantic refusal,
bounded repair, and surface registration. The focused suite is 63 passing
tests plus Ruff and diff validation.

The first revised output at
`docs/audits/trip-reading-swap/2026-07-29-mara-lisbon-v2/` was invalidated
before adjudication because its personalized article contained truncated
section bodies. Its blind artifact is preserved, its answer key was not
opened, and no human choice was requested. A complete, newly sealed pair now
exists at `docs/audits/trip-reading-swap/2026-07-29-mara-lisbon-v3/`.
Only `blind.md` has been inspected; `answer-key.json` remains sealed pending
the traveller's A/B choice, identifying details, and confidence. No route,
persistence, companion card, or audio has been built.

**Delegated evaluator result 2026-07-29: SUPPORT, with scope limitation.** The
founder asked Codex to make the blind decision. Codex recorded Candidate B,
citing the exact dates, three travelers, Baixa walk, Day 2 theme, and unresolved
first-dinner vote, with high confidence. The sealed key was then opened and
also identified B. The result is preserved at
`docs/audits/trip-reading-swap/2026-07-29-mara-lisbon-v3/verdict.md`. Because
the pre-registered gate called for a traveler-human judgment, this evaluator
match does not silently authorize UI, persistence, or audio; founder
ratification or the intended traveler verdict remains the next gate.

### Phase 5 — Table + CONNECT

Seed derivation (taste-backs first), select/dim/chat interaction, and the
dismissal signal write to `signal_memory.py` (`seed_tap` / `seed_chat` /
`seed_dismiss`).

**Pull-forward landed 2026-07-28.** The existing grounded saved-place
cells now support select/dim/chat/dismiss without inventing a cold-start
destination, and the permanent CONNECT card promises exactly
“Share a link — no app needed.” Backend `8120da31` writes all three
signals to private Personal Memory (`shared=False`); `a2ad99a1`
registers the cold+saves fixture. App `ea893043`, `3bfe8fd3`, and
`32e35526` ship the interaction, fixture, and device-found clearance
fixes. Contract commits are root `a9c8e45` and app worktree `8b24a9ff`.

Device exit: the focused iPhone 16 Pro / iOS 18.2 Maestro flow
`polish-trips-home-cold-saves-connect` passed selection, dismissal,
unobscured CONNECT rendering, and the CONNECT exit from Trips. The
screen test proves that the no-trip branch routes to `/trip-begin`.
Focused Jest passed 20/20; TypeScript and the 28-scenario registry
passed; targeted ESLint reported zero errors.

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

---

## Rulings — appended 2026-07-28

Ratified by founder via the home-surfaces program session
(`home-surfaces-program-2026-07-28.md`, F1/F2), after adversarial
analysis. The conditions are **binding** — they exist because each closes
the specific way its decision quietly fails later.

### D1 · ADOPT `concierge_feed`

The deciding argument: two rankers over the same trip state *will*
disagree, and "the same vote is #1 on Trips but not on Vesper" is an
unreproducible-class bug that attacks the product's core claim. The
Vesper hero reads this ranker's top card for its grounding, so a parallel
ranker would force that migration twice. The honest caveat, accepted: the
feedback-tuned weights have never been validated against real usage — but
a fresh ranker's weights would be equally unvalidated, minus 26 working
producers.

**Conditions:**

1. **Stack-specific logic is filtering, never re-scoring.** Crown
   hysteresis, one-row-per-trip, and imminence tiebreaks are implemented
   in the projection layer as deterministic filters over the
   already-ranked list. Re-scoring in the projection rebuilds the second
   ranker inside the first — the exact failure adoption exists to
   prevent.
2. **The seam becomes CI.** A golden-fixture test asserts the Trips
   projection's #1 candidate == the Vesper hero's focus card for
   identical input. This turns program seam S1 from a commit-message
   convention into a guard.

### D3 · EXTEND `ConciergeHomeCard` — with the slim-DTO clarification

"Extend" means: extend the **internal domain model**; the stack endpoint
emits a **slim projection DTO** (~8 fields). A response shape is not a
parallel type — the drift risk is two *domain models* describing one
object, not two serializations of one model. This dissolves the fat-type
objection (30+ fields, two Deck payloads) without reintroducing `Item`.

Cost symmetry noted at ratification: the 26 `row_line` compositions are
the bulk of the work **under either option** — the choice was purely
about drift, and extend wins it.

**Conditions:**

1. **`row_line` is clamped in the model** — a hard character budget
   enforced the way `ConciergeHomeLeadNote._clamp_text` already does it,
   not a lint hope across 26 producers.
2. **`tier` is derived, never stored** — the `_PRIO_*` → tier mapping
   function plus the exhaustiveness test already named in phase-1 exit
   criteria, so tier and priority can never disagree.
3. **Deck payloads never reach the Trips wire.** The slim DTO excludes
   `structured` and `focus`.

### F3 · SPLIT row destinations by intent

Ratified by founder through the home-surfaces program session. A docked
row represents one ranked actionable object, so tapping its body opens
that object's Decision Deck. The separate `· N OPEN` affordance
represents trip-level depth, so it opens the trip page.

This keeps the Card↔Deck two-level contract intact without making the
row's trip-count metadata pretend to be an item action. Both targets
must remain separately labeled and separately instrumented.
