---
doc_type: working
status: active
owner: founder / product
created: 2026-07-27
expires: 2026-08-26
why_new: No existing document owns the Trips-home promotion model — the redesign of the hero/shelf relationship decided 2026-07-27. The trips-home surface contract describes the shipped 8-state hero; this records its successor and the migration reasoning.
promotes_to: Travel App/docs/surfaces/trips-home/contract.md (supersession) plus page-spec updates
supersedes: []
source_of_truth_for:
  - trips-home-promotion-model
  - trips-home-stack-model
  - trips-home-six-section-grammar
  - trip-companion-section
  - trips-home-table-launchpad
  - trips-home-connect-section
  - trips-home-stack-type-geometry-contract
---

# Trips Home — The Stack Model

> **Working spec, not shipped canon.** Records the design decided in the
> 2026-07-27 brainstorm and its same-day revisions, plus the 2026-07-28
> consolidation and canon registration. The spec went through three
> structural collapses; this document describes only the final state,
> with the lineage in one paragraph below.
>
> **This document is self-contained.** Everything needed to build from it
> — the section grammar, the tier ladder, the item contract, the type and
> geometry contract, the verified page states — is here. The Claude Design
> page is the *visual* reference, not a dependency: if it is unreachable,
> this doc is still buildable.

## Status (2026-07-28)

| | |
|---|---|
| Design | COMPLETE — seven page states drawn and measured |
| Canon | **CANDIDATE, not CANON** — registered in the Canon Index 2026-07-28 |
| Code | **Not started.** Zero lines. |
| Canonical page | Claude Design → Vesper → `Vesper Trips Home - Stack Model (Sans).html` |

The shipped `Vesper Trips Home.html` remains canon and its row in the
Canon Index carries a "Succession in progress 2026-07-28" clause pointing
here. It is tagged CANDIDATE rather than CANON deliberately: the README
promises a top-level page is trustworthy for its declared role, and the
chrome states, the 320 px @120 % case, four item kinds, and the "All
trips" destination are not yet covered. Promotion is a tag swap once
those close — see **Before promotion** at the end.

Support modules (Claude Design, Vesper project), registered in
`vesper-canon-consolidation-app.jsx`:

| file | role |
|---|---|
| `trips-home-stack-sans.jsx` | primitives — type scale, geometry, row anatomy, blooms |
| `trips-home-stack-sans-states.jsx` | live · urgent · cold ×2 · loading · absence · Dynamic Type boards |
| `trips-home-stack-sans-connect.jsx` | CONNECT card + the A/B decision record |
| `trips-home-stack-sans-screens.jsx` | composition — **must load last** |

`-screens.jsx` deliberately overrides `SansHomeBusy` / `SansHomeQuiet`
from the primitives module, so adding a section never means editing the
file that owns the type scale. **If the import order changes so it no
longer loads last, the CONNECT section silently disappears.**

## One sentence

**The page is one ranked queue of everything that wants the traveler,
across all their trips — the top item blooms into the voiced hero card,
the rest dock beneath it as rows — followed by their next trip's
reading, a grid of grounded seeds for trips that don't exist yet, and
the trail into memory.**

Compressed: *the item is the fact; the crown is the voice; the queue is
the page.*

## Lineage (how we got here, one paragraph)

v3 had seven sections: per-trip hero + per-trip shelf + companion +
other-trips rows + a seed grid + trail + bridge, with two stacked
judgment systems (8-state cascade picks the trip, tier ladder picks the
item). Three founder corrections collapsed it: (1) *"cards for
seduction, rows for administration"* — evocative treatment belongs to
possibilities, not commitments; (2) other trips' needs must not hide at
the bottom of the page → the queue went cross-trip; (3) hero + shelf
were never two sections — *"the hero is just a promotion of the shelf
items"* taken literally means one list where the first item blooms.
Seven sections became four, and two judgment layers became one ranker.
The count later went back up to six — but by promotion, not by
accretion: YOUR PEOPLE and CONNECT were each earned by an argument
recorded in their own sections below.

## The six-section grammar (fixed, every state — 2026-07-28)

```
THE STACK   — one ranked queue across all in-play trips;
              item #1 at card fidelity (voiced), the rest as
              docked rows in the same container
COMPANION   — the nearest upcoming trip's reading (editorial
              register, compact, sections behind a toggle)
THE TABLE   — the future: the top seed BLOOMS into a SKETCHED
              TRIP (day-spine, named anchors), smaller seeds
              beneath (evocative register + signal instrument)
YOUR PEOPLE — the social pulse: friend activity, the group
              echo, travel-twin reads (ambient, another-person-
              initiated — the strongest trigger class)
CONNECT     — the standing invite door: one card, always the
              same, never counts and never pressures
TRAIL/BRIDGE — on-this-day · Atlas · All trips door
```

> *Why these six and not four: the founder promoted two of the review's
> item clusters to structure. The sketch is the stack's promotion grammar applied to
> the future (seed #1 blooms, like item #1 blooms); YOUR PEOPLE gives
> the strongest trigger class standing real estate instead of one
> buried trail row. Calibration was explicitly ruled NOT a section —
> see "Calibration is items" below.*

Plus a quiet `All trips →` door at the bottom — the roster/archive
lives there and on the trip pages, not on home.

The page reads as a temporal arc: **present** (stack) → **future**
(table) → **past** (trail/bridge). Three registers, distributed: the
voice owns the bloom, the facts own the rows, the long-form voice owns
the companion, the evocative register owns the table.

Sections are existence-gated (an empty section does not render — and
**emptiness has no chrome**: no headers over nothing, no placeholder
cells) but never reordered.

## The stack

One container. The first item renders at **card fidelity** — identity
block, VESPER eyebrow, prose read with italic emphasis, receipt, one
step. The remaining items render as **docked rows directly beneath,
inside the same container** — no section break, no "shelf" label. Each
row: trip kicker (`LISBON · SEP 2–7`) + one fact line + door.

**Queue rules:**

- Rank every action item across every in-play trip on the tier ladder.
  #1 blooms. The bloomed item does not also appear as a row.
- **One row per trip** when multiple trips compete; the crowned trip
  may take a row only for a second *genuine action item*. Cap ~3 rows;
  overflow is caught by `All trips →`.
- **A trip with several open items shows its top item, not a digest**
  (decided 2026-07-27). The row is a *cursor* into that trip's own
  ranked sub-queue: the fact line carries the one next item; depth
  moves into the kicker (`LISBON · SEP 2–7 · 3 OPEN`). Resolving the
  top item surfaces the next — sequential revelation, nothing lost.
  Item counts may be numeric (names-not-fractions is about people,
  not things); the full spread lives on the trip page. Same judgment
  at every zoom: the crown is the #1 item globally, each row the #1
  item of its trip.
- **Same tier → nearer trip wins.** Imminence is the tiebreak: a live
  trip's orient beats a far-out trip's vote; the day before departure
  beats three weeks out.
- **Zero remaining items → zero rows.** The stack is just the card.
  This is why the single-quiet-trip page is complete, not sparse —
  there is no lonely one-row section because there is no section.
- Tapping a row opens that trip (its page owns the full ledger: Plan,
  Costs, Photos, People — those doors no longer live on home).

**Register rule for row facts — names, not fractions.** "Waiting on
Dana and Sam," never "2 of 5 answered." Machines count; hosts name.
This is a composer/contract rule on the fact line, not a UI feature.

## The tier ladder

First non-empty tier wins; ties break by imminence. The floor tier
means the crown is **never empty and never nagging**.

| Tier | Name | Contents | Rule |
|---|---|---|---|
| 0 | Time-critical | Catch fired; vote deadline inside window; departure-day logistics | Always wins; only tier that can usurp intraday |
| 1 | Orient | Live trip's "where you need to go next" | Default crown during `live` |
| 2 | Open decisions | Votes, stay race, **invite**, **overlap match**, **autonomy offer**, low-confidence **questions** — needs the human, no hard deadline | Beats gifts only past an age threshold |
| 3 | Gifts | Story ready; agent work; **group echo**; memory candidates fresh | The good days |
| 4 | Companionship (floor) | No decision required — Vesper says something true: anticipation, recall, pattern | Always available |

Notes:

- **Deadline-gated urgency:** a chore outranks a gift only if it has an
  actual clock. This keeps the page a companion, not an inbox.
- **Tier 4 is the existing farout_read archetype system**
  (Recall/Pattern/Match/Thread/Standing). The shipped planning-state
  hero becomes the floor tier — nothing is deleted, it gets a precise
  job. Floor-tier voice belongs to the nearest trip.
- **Crown hysteresis:** a promotion holds for the day. Only tier 0
  usurps intraday. The difference between a page with a point of view
  and a page that fidgets. Hysteresis relaxes only during `live`,
  where the orient crown refreshes per segment.
- **Push policy (decided 2026-07-27): tier 0 pushes; nothing else,
  ever.** Everything tier 1+ rides home_card/in_app. This is the
  decision rule the proactive engine has been missing (no producer
  ever requests push today), and scarcity is what keeps the push
  channel credible.
- On floor-tier days the crowned voice may *gesture at* the companion
  ("your reading's below") — mention, never promotion.

## The group flows through the stack (no new chrome)

Decided 2026-07-27 (v8). Group presence — the product's wedge — uses
three existing channels rather than any dedicated module:

1. **The empty chair.** The bloomed card's identity block carries a
   facepile: solid avatars = members, dashed hollow = invited-not-
   joined, and always one dashed gold **`+` seat** — the standing
   invite door. Tap → group sheet (members, pending, invite link).
   On a solo trip the facepile is just the chair: a door, not a
   suggestion; it never escalates on its own.
2. **Names in the facts** (rule above).
3. **Invite as a ladder item.** When the group state is the bottleneck
   — a real plan with empty seats, an open vote with half the group
   never joined — "your people aren't here yet" enters the queue as an
   ordinary tier-2 item, scored by the gap between *group described*
   and *group present*. It can win the crown on merit and get voiced
   ("The plan's ready — but Lisbon alone is a different trip"), and it
   demotes like any item the moment something more urgent exists. The
   CTA carries the zero-install promise ("Share a link — no app
   needed"). No banner, no nag module; invite prominence is a judgment
   the page makes, self-tuning per trip. A deliberately solo trip has
   no gap, so the item never ranks. **"Group described" comes from
   hard facts only** (decided 2026-07-27): vote roster size and an
   optional party-size question at trip intake — never chat inference
   in v1. Guess-scoring a growth surface is how the invite crown
   becomes the nag we pre-registered as a falsifier.

## Crown eligibility

| Crown-eligible (queue items) | Never on home (trip-page ledger) |
|---|---|
| orient · Catch · open decisions · settle-up · invite · **overlap match** · **autonomy offer** · **question** · story-ready · agent-work receipt · **group echo** · memory candidates · countdown · floor read | Photos · People/roster-as-list · Plan-as-door · Costs-as-door · anything stale |

The right column is *possessions*; the queue holds only items that want
something or give something. Eligibility is a static flag on the item
type; per-state priors live in the ranker (e.g. `returned` biases story
over settle-up unless settle-up gains a deadline).

**Content is never crowned** (decided 2026-07-27, reversing an earlier
draft): the crown is a judgment about trip *state*, and content is not
state. Content lives in the companion.

## Items: the defined contract

Same payload/rendering split as the work receipt
(`docs/working/work-receipt-2026-07-26.md`):

```
Item {
  kind          — plan_decisions | invite | costs | story | orient |
                  catch | agent_work | overlap_match | autonomy_offer |
                  question | group_echo | …
  trip_id
  facts         — derived counts/values only; never estimated; people
                  referenced by name where true (grounding rules
                  inherited wholesale from the work receipt)
  receipt       — which typed receipt variant renders when crowned
  step          — the one action when crowned
  row_line      — the one-line fact when docked (hard char budget)
  hero_eligible — static boolean
  tier          — static tier assignment
  freshness     — drives NEW stamps and gift ranking
}
```

## Composition lifecycle (voice on promotion)

Receipts and facts are **defined** (deterministic); the Vesper voice is
**generated at promotion time**.

- **Promotion is a server-side event, not a page render.** The ranker
  runs when facts change or a tier fires. Composition happens once at
  the promotion event; the read is stored on the item; page loads read
  the stored voice. Never compose in the request path.
- Cost: one Haiku-tier call per promotion event (~$0.001); with crown
  hysteresis, ~one composition per day.
- **Grounding contract (inherited from the work receipt):** the voice
  narrates the item's facts and may not add to them. Emphasis phrase
  backend-verified (`_cited_verbatim` pattern already used by
  farout_read serve). Group-visible voice routes through the existing
  compose privacy gate.
- **Fallback — suppressed, not softened:** if composition fails or
  trips a guard, the crowned item renders with its defined receipt and
  no prose. The page must work with the crown wearing no voice.

## The companion (compact contract)

The **nearest upcoming trip's** editorial section (decided 2026-07-27:
the reading anchors to anticipation, which is stable — not to the
crown, which moves overnight; exception — during `live`, the live
trip's reading takes the slot). Register: lean-back. **Collapsed by
default, three rows tall:**

```
header   — kicker ("WRITTEN FOR THE FIVE OF YOU") · title ·
           Listen N min / read N min   (art slot BLANK — see below)
toggle   — "N SECTIONS ▾" dropdown, collapsed by default
[secs]   — when open: one line per section, numeral + title + minutes,
           nothing else; tap a row → reader opens at that section
thread   — one seeded conversation line, ALWAYS visible (outside the
           toggle — it is the doorway into chat and the smallest row)
```

**Line-limit contract (rigorous, both layers):** title ≤ 1 line,
section titles ≤ 1 line, thread ≤ 1 line — ellipsized in CSS *and*
budgeted in the composer prompt, so the ellipsis is a guardrail, not
the norm. No subtitles, no teasers, no pull-quote: **the
personalization lives in the section titles themselves** ("Eating the
way you five eat", "What the five of you haven't decided").

Guardrails (definitional): trip-scoped and existence-gated; fixed
capacity (one Reading, audio as a mode toggle on the same card — the
one-shot TTS pipeline from 2026-05 — plus ≤2 threads); no engagement
mechanics. Threads are a property of content, not a content type
(belief #19); each is a tap that seeds a Vesper conversation via
ConversationSeed. The final section should argue the trip's open
decision where one exists — the article argues, the stack executes.

**Refresh clock (ratified 2026-07-27):** recompose on itinerary commit
and once at T-7 days; never on page load. A section whose facts went
stale between recomposes (it argues a vote that has since closed) is
**suppressed, not softened** — dropped from the spine, not rewritten
mid-cycle. Audio follows the article by a release: the swap test gates
the writing first, and the TTS pipeline inherits whatever the writing
proves.

The intent-article variant ("The case for Lisbon in June") is the
cold-adjacent version and the first-session payoff; it renders in the
same card once a draft trip exists.

Quality gate, pre-registered: **the swap test** — show the traveler
their Reading and a generic city guide for the same city. If they
cannot tell which is theirs, the feature fails.

## The table (sketch + seeds)

The section for **trips that don't exist yet**, and — deliberately —
**a preference instrument that happens to look like a travel poster.**

**The sketch — the table's bloom (decided 2026-07-27).** The
top-ranked seed does not render as a card; it renders as a whole trip
already **drawn**: ground kicker ("BECAUSE YOU KEEP SAVING OAXACA" —
why this, why you) · named direction ("Five days in Oaxaca") · the
**day-spine** (anchored days as solid gold nodes with named anchors
beneath; open days dashed — "2 days open, on purpose" is a *feature*,
not an absence) · one quiet door ("Step inside →"). "Not this one ↻"
redraws — and is itself signal. Composed via `generate_trip_shapes`
(exists, previously homeless) once per slow-clock rotation. This is
the stack's promotion grammar applied to the future: seed #1 blooms
the way item #1 blooms.

**Become-organizer renders AS a sketch.** An invitee just back from a
group trip gets "Your Lisbon — from the trip you just took": their
version, anchored in what they saved on that trip, none of the
compromises. The funnel's most valuable conversion event (Growth
Strategy) delivered as a gift, never a prompt.

Layout beneath the sketch: smaller seeds — a row of 2, or a 2×2 when
no sketch is available; *shrinks rather than pads*; 0 grounded seeds
→ the section does not render.

**The interaction (signal collection, not commitment):**

- Tap a seed → it lifts (gold edge), the other cells dim/desaturate;
  tap again to deselect.
- An action bar slides in with one primary button: **"Chat about
  {place}"** — deliberately *chat*, not "start planning." It opens a
  conversation pre-seeded with the ground; planning is something the
  chat can escalate into, never the entry price.
- A small **"not for me"** dismisses the seed (it rotates out and a
  fresh one rotates in). Dismissal is the cheapest, highest-value
  negative preference signal.
- **Every gesture is signal:** the tap (lean-in), the chat (strong
  interest), the dismissal (negative), tap-and-walk-away (curiosity
  without appetite), the redraw (↻ on the sketch). This is the
  cold-start preference interface — the questionnaire users enjoy
  answering.
- **The question-seed (v9):** a low-confidence question renders
  seed-shaped anywhere in the grid, not just at cold start — kicker
  names what answering changes ("A QUESTION · TUNES YOUR EVENING
  PICKS"), answer chips inline ("Quieter / Livelier"), one-tap,
  reversible ("noted — change it anytime").

**The four seed grounds** (every cell grounded in the user's own data;
the kicker names the ground — the line between a seed and an ad):

| Ground | Kicker | Source machinery |
|---|---|---|
| Your saves | `FROM YOUR SAVES` | taste-backs (exists) |
| Your people | `PRIYA'S TRIP` | Plan Similar (social-loop P0); overlap/intent (later) |
| Your patterns | `A YEAR SINCE ISTANBUL` | cross-trip affinity / farout_read recall |
| Your calendar | `OCTOBER'S OPEN` | open windows → date-poll seed |

The deeper flow stays available behind the chat: seed →
`generate_trip_shapes` (exists; currently homeless) → 2–4 named
directions → a draft trip lands with `DATES OPEN`, intent article as
the payoff once the Reading composer exists.

Rules: **grounded or absent** (never generic editorial); **slow
clock** (rotate weekly or on real events — never per page load; a
dismissal rotates immediately); **hidden during `live` days** (no
next-trip seduction mid-trip — trail/bridge absorb the space).

**Signal destination (decided 2026-07-27):** every gesture writes to
concierge Personal Memory via `signal_memory.py` — event kinds
`seed_tap` / `seed_chat` / `seed_dismiss` — the same store Atlas DNA
projects from. No new table. This closes the strategic loop from the
roadmap validation: affinity-as-ranker was refuted for lack of
cold-start signal; the table is the machine that generates that
signal.

**Cold start — CORRECTED 2026-07-28 against shipped code.**

> An earlier revision of this spec specified a "cold-start ground tier"
> of exactly three seeds for zero-trip users — `NEAR YOU` (a home-city
> weekend), `THE SEASON` (what the coming month is good for), and one
> asked question. **That was wrong, and it was ratified before anyone
> read the shipped implementation.** It invents two grounds that are not
> grounded in the user's own data, which is precisely what the
> grounded-or-absent rule forbids — and what the shipped code already
> deliberately refuses.

The shipped `ColdHome` (`components/trips/TripsHomeViews.tsx`) is an
**invitation, not a fabricated grid**. The assembler says so in a comment
that should be treated as doctrine:

> *"Cold — an invitation, not a bet. No receipt (nothing to cite), one
> door. Deliberately breaks the receipt grammar."*
> — `components/trips/hero/assemblers.ts`, `coldHero()`

Its actual structure: `ColdInvitation` → optional `DraftDoor` →
`DreamsInTasteSection` (**returns null when the user has no saves** — it
does not fall back to invented content) → `StartFromSection`. The
standfirst is `A year, still / blank. / nothing booked yet — here's where
to begin.` and `shouldShowTripsFooter` is false for cold.

**The rule this establishes, which the stack model inherits:** when there
is nothing true to say, the cold page says one true thing and opens one
door. It does not manufacture a grid to fill space. The seed grid is for
travellers who have generated grounds; a person with zero saves and zero
trips has none, and the honest response is an invitation.

Two states are therefore mocked, not one: **cold** (no saves — invitation
only) and **cold + saves** (the `FROM YOUR SAVES` ground exists, so real
seeds render). The mock rebuilds the shipped visual values rather than
redesigning them: `planningInk #3D5066` (= `blue60`), `onDarkGold
#E5C16F`, `onDarkCream #F4EEE2`, aspect ratio 1.42, art occupying 39 %.

What survives from the original decision, unchanged: **no separate
onboarding questionnaire — ever.** Taste is taught through the same
instrument the mature page uses, once there is ground to teach from.

**Art direction: TABLED (2026-07-27).** Cells ship blank/typographic
until decided. Options explored and recorded (`table-art-direction.html`
mock): (A) pure typographic; (B) parametric atmosphere —
`wash = f(place, ground)`, deterministic gradient layers over palette
tokens, zero assets; (C) B plus **real pixels when the ground owns
them** (a friend's shared photo with attribution chip, a saved venue's
photo — never stock, never generated). Diffusion-generated imagery was
rejected for chrome surfaces (style drift, stock feel, cost/latency).
No riso/drawn illustration on this surface regardless of choice.

Strategic note: the table is the **origination engine** (Surfacing
Strategy §2.5; Fundraising Playbook §8 metric 2 — "trips surfaced by
Vesper vs. initiated by users") occupying the page's most seductive
real estate.

## Your people (the social pulse as a standing section)

The strongest trigger class in the strategy (another-person-initiated;
Surfacing Strategy §2.5) gets standing real estate instead of one
buried trail row. Register: ambient warmth, ledger-quiet. Three row
kinds:

1. **Friend activity** — "Priya came back from Oaxaca — her week is
   shareable." Door into her shared story / Plan Similar.
2. **The group echo** — "Fei shared the Lisbon story — add your
   favorite photo." Another member's action inviting yours.
3. **The travel-twin read** — paired avatars + a grounded kicker
   (`FROM TRIPS YOU'VE BOTH SHARED`) + one serif line ("You and Priya
   both end up at counter seats — her Oaxaca did it that way").

Rules:

- **The actionable overlap match does NOT live here.** "You and Maya
  overlap in Lisbon for two days — want me to find something?" is a
  tier-2 stack item with a clock; the question form is the product.
  This section carries the ambient forms; anything actionable
  promotes into the queue.
- **Twin reads ground ONLY in shared artifacts** — mutual trips,
  shared stories, public saves. Never inferred private preference
  data (§4.4.1 one step removed). Shared pixels and shared trips, or
  absent.
- **Existence-gated:** no friends → a single quiet invite door, or
  absent. The empty state IS the wedge, stated honestly.

## CONNECT — the standing invite door (decided 2026-07-28)

A dedicated section for bringing people in. Chosen over the alternative
(option B: an invite *row* folded into YOUR PEOPLE) because the wedge
deserves a fixed address the traveler can learn, not a row that appears
and vanishes with social state.

**One card. Always the same. It never counts and never pressures.** No
"3 friends pending", no "invite 2 more to unlock", no streak, no badge,
no progress toward anything. It states the door and opens it. This is
the guardrail, and it is the whole design: the moment this card starts
measuring the traveler's social life, it has become the growth-hack the
model pre-registered as a falsifier.

**Division of labour with the invite item — this is the part to get
right.** Invite exists in two places and they do different jobs:

| | CONNECT section | invite as tier-2 stack item |
|---|---|---|
| Nature | a **door** | a **judgment** |
| When it shows | always | only when the group gap is the actual bottleneck |
| Can it take the crown | never | yes, on merit |
| Voice | none — it is chrome | composed at promotion |
| Escalates | never | demotes the moment something more urgent exists |

The section is the permanent, unpressured way in. The stack item is the
page *noticing* that a real plan has empty seats and saying so once, with
a voice. Neither replaces the other; a page that had only the section
would never speak up when it mattered, and a page that had only the item
would leave the traveler with no way to invite on a quiet day.

Carries the zero-install promise ("Share a link — no app needed"), the
same phrasing as the stack item's CTA. Existence-gated like every other
section, with the honest empty state: no people yet is not a failure to
paper over, it is the wedge stated plainly.

## Calibration is items, not a section (ruled 2026-07-27)

Considered and rejected: a standing preference-calibration section.
It would be the killed living-profile/questionnaire wearing a hat — a
place users feel obligated to tend. Instead, calibration is three
shapes of the same signal, each already housed:

1. **Decision-shaped → the stack.** The `autonomy_offer` ("you've
   kept my last 8 dinner picks untouched — want me to book them from
   now on?"; the streak is the receipt; consent per task class,
   revocable) and the consequential `question` item. **Scarcity is
   what makes them feel earned** — a rare crowned offer reads as the
   relationship advancing; a permanent module reads as settings.
2. **Play-shaped → the table.** Seed taps, chats, dismissals,
   redraws, question-seeds.
3. **Ambient → everything else.** Votes, edits, row dismissals,
   companion section-taps — silent byproduct into Personal Memory.

Composer rule: a question item always states what answering changes.

## Type and geometry contract (2026-07-28, measured not guessed)

This section exists because the first consolidation pass violated the
typography contract badly enough that the founder caught it twice. It is
recorded here so a builder never has to re-derive it from the mock.

### The register rule

**Serif is a voice, not a decoration.** EB Garamond (Roman only — the
family header in `vesper-typography-contract.jsx` declares Roman) is
spoken by exactly three things, and italic by two:

| Register | Family | Owns |
|---|---|---|
| Vesper speaking | **serif** | the H1, the crowned read, the thread quote |
| Editorial objects | **serif titles over sans sublines** | table cards, companion card |
| Productive rows | **sans** | the stack, every row, all metadata and controls |
| Italic | serif italic | the read's emphasis phrase and the thread quote — nowhere else |

The governing contract is explicit that `readingBody` is never for
"dense productive rows; UI controls; metadata", that `readingBodySmall`
is never for "repeating through dense productive rows", and that
`uiTitle` owns "card titles on productive surfaces" while
`editorialTitleSmall` owns "card titles, small editorial headings".

The correction path is worth recording because both directions were
wrong: the page began at **79 serif runs**, was cut to 25, then to 14 —
at which point the founder pushed back the other way, because card
titles like *"Five days in Oaxaca"* and *"A week in Sicily"* are
editorial objects and had lost their voice. The settled state is
**~19 runs**, allocated by register rather than by count. *The number was
never the target; the rule is.*

### Geometry

```
GUT     = 22    page gutter — H1, eyebrows, every card share it
CARD_W  = 349   every card, no exceptions
PAD     = 16    card inner padding → all card text sits at x = 38
ROW_H   = 60    row height, as minHeight (NOT a fixed height)
```

One shared constant per value. This was the fix for a page-wide 8 px
misalignment: the stack card sat at left 14 / width 366 while the H1,
the eyebrows and every other card sat at 22 / 349, putting inner text at
x = 30 against everyone else's x = 38.

### Scale

Three mono (10 / 9 / 8) · six sans (16.5 / 15 / 13 / 13 / 12.5 / 11) ·
**four** serif (32 / 22 / 18.5 / 17). Avatar initials use an **integer
lookup (`AV_FS`)**, never `size * 0.4` — the computed form produced
fractional 9.6 px text. Before the scale was declared the page carried
**31 distinct size/weight pairs**.

> **Corrected 2026-07-28.** The scale originally listed a fifth serif at
> **13 px**. That cannot ship: `__tests__/conventions/serifFloorContract.test.ts`
> enforces `SERIF_FLOOR = 15` as a ratchet, and any *new* sub-floor serif
> fails the suite. Per the contract's own triage rule — *"the correct fix
> is usually System Sans, which at the SAME px is larger in apparent
> size, so it does not reflow the box"* — **serif-13 becomes sans-13.**
> No visual loss, and it is what the register rule wanted anyway: 13 is
> row and metadata territory, which this contract already assigns to
> sans. The mock was inconsistent with its own rule.

### Italic — approved as a limited register (2026-07-28)

Italic marks the Vesper voice: the crowned read's emphasis phrase and the
quoted thread line. **Nothing else** — not editorial titles, not
metadata, not decoration.

Production does not have it yet (EB Garamond is registered Roman-only),
so this is a real build step with conditions set by
`constants/fonts.ts`, and they are not optional:

- **Register the face and one named semantic role together.** The
  contract: *"add the face and named semantic role together; never
  synthesize or register slant at an individual call site."* No
  `fontStyle:'italic'` at a call site, ever — synthesized oblique on a
  Roman family is inconsistent across platforms.
- **Italic never renders below 17 px.** Check both sites against this.
  The crowned read's emphasis should clear it; **the companion's thread
  quote is a small row and may not** — if it sits below 17 it moves up or
  gives up italic. It does not get an exception.
- **Extend the floor ratchet** to guard italic ≥ 17 in the same change,
  or the new register drifts exactly the way the serif floor did.

**Hierarchy rule, learned the hard way:** the row fact line is 13, not
14. At 14 it was the second-largest sans on the card — larger than the
CTA at 13 — which inverted the hierarchy and made administration look
more important than the action. The facepile came down 20 → 18 with it.

### Dynamic Type

**Rows must use `minHeight` plus a 2-line clamp, never a fixed height.**
A hard 60 px row with a one-line clamp clipped at 120 % text: content
needed 289 px in a 253 px box. Verified after the fix — row heights
**60 / 83 / 88 px at 100 / 120 / 135 %**.

Untested and therefore listed as a promotion blocker: **320 px width at
120 % text**. The seed grid's two `1fr` columns are the known risk.

> Verification note: measure the DOM, do not eyeball the mock. A
> truncation probe that filters to `!e.children.length` will skip every
> fact line containing a `<span>` — which is all of them — and report a
> clean page while the screenshot shows clipping. Check every ellipsized
> element.

## What carries over unchanged

- The hero card's **visual design** — untouched, per the founder's
  register decision ("the voice stays the center"). Serif, eyebrow,
  prose spine, italic emphasis, receipt, one step.
- The 8-state cascade — demoted to ranker priors + the identity pill
  (`PLANNING`, `JUST BACK`, `LIVE`) on the bloomed card. No longer a
  page-selection mechanism.
- farout_read — the floor tier's composition engine.
- The trail and Atlas bridge.
- `cold` keeps its bespoke invitation hero (no items exist to rank);
  `between` dissolves into the standing grammar (the table *is* the
  between-state, always present).

## Page states (seven, all drawn as of 2026-07-28)

**The governing principle: a page state is a *parameter change*, never a
new layout.** The six sections never reorder; states differ only in which
sections exist and what the ranker put in them. Any state that needs a
new section is a design failure, not a new state.

| State | What changes |
|---|---|
| **Quiet** (one trip) | bloomed card carries the floor voice; **zero rows** — the stack is just the card. Complete, not sparse: there is no lonely one-row section because there is no section. |
| **Busy** (several trips) | bloomed crown + 2–3 docked rows, one per trip, each showing that trip's top item with depth in the kicker (`· 3 OPEN`). |
| **Live** (mid-trip) | bloom pins to tier-1 orient and refreshes per segment — the one place crown hysteresis relaxes. Rows show same-day items only. Companion re-anchors to today. **The table hides** — no next-trip seduction mid-trip; trail/bridge absorb the space. |
| **Urgent** (tier 0 fired) | the only state that can usurp intraday, and the only one that pushes. Everything else is unchanged — urgency is a promotion, not a redesign. |
| **Cold** (no trips, no saves) | invitation only — see the corrected cold-start section. Stack and companion absent. |
| **Cold + saves** | the `FROM YOUR SAVES` ground exists, so real seeds render. The distinction from plain cold is the whole point: seeds appear when there is ground, never to fill space. |
| **Loading** | must not reflow into the loaded state. |

Live was drawn on 2026-07-28; the "one mock still owed" noted in the
2026-07-27 revision of this doc is closed.

## Migration sketch

1. **Item registry + ranker** (backend): item contract, derive items
   from existing sources (plan-state, membership/invite gap, expenses,
   story, situation), cross-trip ladder + imminence tiebreak +
   hysteresis. No UI change.
2. **Stack FE**: render docked rows under the existing hero (hero still
   composed the old way) — visually the v5 page with old crown logic.
3. **Crown cutover**: bloom driven by the crowned item (receipt + step
   from the item; voice composed on promotion). Facepile + empty chair
   in the identity block. The `agent_work` item kind lands here —
   reuses `WorkReceiptPayload` from the shipped work-receipt build;
   needs the cutover to render.
4. **Companion**: compact card + toggle + thread (requires the
   trip-reading composer — a separate build on the Atlas compose
   engine).
5. **Table**: seed derivation (taste-backs first) + select/dim/chat
   interaction + dismissal signal write. Blank art.

Phases 1–3 are re-plumbing of existing data and can precede the
Reading entirely. Phase 4 is the only net-new content system.

## Metrics

- **Glance test** (cohort 1): 3 seconds → when is the trip, what needs
  you, what would you tap?
- **Crown routing**: taps through the crowned step vs. around it.
- **Origination**: share of trips started from table seeds vs.
  user-initiated.
- **Signal yield**: table gestures (taps, chats, dismissals) per user
  per week — the table earns its keep even when no trip is born.
- **Invite conversion**: invite-crowned impressions → links shared →
  seats filled (the wedge metric, now measurable because invite is an
  item).
- **Swap test** for the Reading.
- **Thread pull-through**: thread taps → seeded conversations that
  continue past one exchange.

## Falsifiers

Reconsider this model if:

- Users can't tell why an item is crowned (judgment reads arbitrary).
- The crown thrashes or is gamed by tier inflation.
- Floor-tier days read as filler — the companionship voice must feel
  like presence, not padding.
- Docked rows go untapped AND their facts go unmissed (then the queue
  belongs inside trip pages, not on home).
- The companion's swap test fails.
- Seed cards read as ads for the product inside the product.
- Table taps don't convert to chats or drafts (the launchpad is
  admired but not launched from).
- The invite item reads as growth-hacking when crowned — if travelers
  screenshot it as a nag, the gap-scoring is miscalibrated.

## Unresolved

Thirteen open items from the 2026-07-27 review were decided the same
day; their resolutions are folded into the sections above (companion
anchor → nearest upcoming trip; refresh clock ratified; audio follows;
live-day = collapse with table hidden; zero-trip = invitation, NOT a seed grid
(corrected 2026-07-28 against shipped code — see The table); story item from phase 1; signals → Personal Memory; push = tier
0 only; `agent_work` item kind in phase 3; group-described = hard
facts only). Remaining:

1. **Table art direction** — deliberately tabled; the three explored
   options are recorded in The table.
2. **Ranker weights** — per-state priors, the tier-2-age vs tier-3
   threshold, the invite gap threshold. Build-time tunables: start
   from the decisions recorded here, tune with cohort data.

*(The third item, "one mock owed — the live-day collapse", is closed:
drawn 2026-07-28.)*

## Before promotion to canon

The page is CANDIDATE until all of these close. None of them block
migration phases 1–3, which are pure re-plumbing.

1. **Chrome states re-verified** against `TripsRootChrome` — scrolled,
   reduced transparency, reduced motion.
2. **320 px at 120 % text** — the seed grid's two `1fr` columns are the
   known risk.
3. **Four item kinds still unmocked:** `overlap_match`, `group_echo`,
   `agent_work` receipt, `story` ready.
4. **"All trips" destination** — three artboards already exist on the
   shipped canon page and are unaffected by the stack model. Carry them
   over; do not redraw.
5. **Post-trip story arc** — `returned` currently surfaces only money.
6. **Interchange manifest** — re-run `audit-interchange.js
   --write-manifest` (it lives design-side and must run in the browser,
   not as a CLI step). Deliberately not run for the CANDIDATE state:
   `authorityStatus` has no CANDIDATE value, and every value in that
   vocabulary asserts authority. Add one at promotion.

**Known dead code:** `trips-home-stack-sans.jsx` still contains the
superseded `SansHomeBusy` / `SansHomeQuiet` definitions, now unreachable
because `-screens.jsx` overrides them. Harmless; delete when convenient.

## References

- `Travel App/docs/surfaces/trips-home/contract.md` — the shipped
  contract this supersedes on promotion
- `Travel App/components/trips/TripsHomeModel.ts` — the 8-state cascade
- `Travel App/components/trips/hero/TripHeroCard.tsx` — the unchanged
  hero template; `promoteHeroIfNeedsYourVote` as the promotion
  precedent
- `backend/home/farout_read/` — the floor tier's composer
- `docs/working/work-receipt-2026-07-26.md` — the payload/rendering
  split and grounding rules this inherits
- `travel-agent/docs/product/Surfacing Strategy.md` §2.5 — origination
- `travel-agent/docs/product/What We Believe.md` — #13, #19, #22
- `components/trips/TripsHomeViews.tsx` — `ColdHome`, the shipped cold
  start this spec was corrected against
- `components/trips/hero/assemblers.ts` — `coldHero()` and its
  invitation-not-a-bet comment
- `components/trips/TripsHomeStyles.ts` · `constants/colors.ts` ·
  `constants/tripsHome.ts` — the cold visual values the mock rebuilds
- `vesper-typography-contract.jsx` (Claude Design) — the governing
  register rules quoted in the type contract above
- `docs/working/canon-index-registration-2026-07-28.md` — the canon
  registration record, and the working method for editing large Claude
  Design files without round-tripping them through model context

### The canonical page

**Claude Design → Vesper project → `Vesper Trips Home - Stack Model
(Sans).html`**, with the four support modules listed under **Status**
above. Seven page states, existence gating, Dynamic Type boards, the
CONNECT A/B decision record, and the type/geometry contract as boards.

Superseded, still deployed, **do not build from**: `Vesper Trips Home -
Stack Model.html` (+ `trips-home-stack.jsx`) — the first consolidation.
It is the serif-forward version that triggered the typography correction
and encodes the superseded *five*-section grammar. Kept for lineage only.

### Mocks — gone, by design

The v3 → v8 iteration mocks (`trips-home-promotion-v3/v4/v5/v6.html`,
`companion-compact-v7.html`, `group-presence-v8.html`,
`table-art-direction.html`, `hero-card-comparison.html`) lived in an
ephemeral session scratchpad and **no longer exist**. They are named here
only so that a reader who meets the names elsewhere knows what they were.

Everything they decided is folded into the sections above — which is what
makes this document self-contained. The three table art directions
(A typographic · B parametric wash · C B-plus-real-pixels) are recorded
in **The table**; the rejected hero-register exploration needs no
artifact beyond the decision that the hero's visual design carries over
unchanged.
