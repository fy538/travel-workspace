---
doc_type: archive
status: archived
owner: founder / product
created: 2026-08-03
archived: 2026-08-04
why_new: The Trips crown has 23 admissible card kinds and exactly one receipt rendering. No document owns the mapping between the two, and the ratified item contract's `receipt — which typed receipt variant renders when crowned` field was never implemented.
promotes_to: a `TripsHomeReceipt` contract in the Trips stack projection plus a new `invite_seat` card kind
supersedes: []
source_of_truth_for:
  - trips-crown-card-kind-to-receipt-mapping
---

# The Trips Crown: card kinds and their receipts

> Audit, 2026-08-03. Read against HEAD of both repos on the day it was written.
> Every file:line below was verified directly, not taken from prior notes.

> **🏁 SHIPPED 2026-08-04.** All ten shapes below landed in
> `backend/home/trips_stack.py` (`TripsHomeReceipt`, a 10-variant
> discriminated union): `ledger`, `checklist` (people/invite_seat came in
> the same push, not listed in the original 8-shape table above — see
> `project_crown_receipt_union` memory), `shape` (imminent_trip, built by a
> concurrent session), `diff`, `call`, `candidates`, `spine`, `waveform`,
> `conditions`. Commits `603cbd34`/`ea6b4392` (invite_seat + people),
> `a48f5cfc` (diff/call/candidates), `d205859c` (spine), `ce2bd77d`
> (waveform — needed a real producer change, not just a projection: see
> correction below), `44a877e7` (conditions — the one other producer
> change, per Sequence step 5).
>
> Two corrections against this doc's original mapping, found during build:
> - **`candidates`** ships scoped to `focus.pick`/`focus.compare` only.
>   `near_you` was **excluded** — `focus.near_you` is a structurally
>   different payload (`DeckNearYouPlace`: no `leading` flag, a raw
>   `walk_min` int, not `DeckPickCandidate`'s pre-formatted strings).
>   Force-fitting it would mean inventing a leader that doesn't exist.
>   `near_you` still falls to `stamp`.
> - **`spine`** ships scoped to `planning_brief` only, not the four kinds
>   the table below lists. `build_brief_focus`'s one real call site
>   (`producers.py`) sits exclusively inside `planning_brief`'s
>   else-branch, firing only when `_readiness_card` returns `None` — none
>   of `live_trip`/`daily_brief`/`trip_thread` ever construct
>   `focus.brief`. `imminent_trip` already has its own separate mechanism
>   (`TripsHomeReceiptShape`, fetched via a dedicated API-route DB call,
>   built by a concurrent session before this correction was found) — a
>   competing spine there would have been silently starved, since that
>   route only fetches `shape` when `crown.receipt` is already `None`.
>
> `agent_work`'s closed-polarity `checklist` (Sequence step 3) turned out
> to be **blocked, then unblocked same day (`5c5baedd`)** — not "the price
> of a boolean" as originally scoped, but not permanently stuck either. The
> proactive-events payload `agent_work` reads had no human-readable
> subject name, only a categorical `subject_type` and inconsistently-
> formatted free-text `reason`; building a `label` by parsing that text
> would have violated grounded-or-absent. Fixed at the **write side**
> instead: a new optional `ProactiveCandidate.subject_label` field, wired
> through the two producers that actually have one real named subject in
> scope (`_produce_venue_disruption`, `_produce_feasibility_catch` — both
> also weren't setting `reason` before this fix, a second latent gap found
> in passing). The other three registered producers (`events_tonight`,
> `itinerary_health`, `pre_trip_drip`) have no single named subject and
> stay unlabeled by design — found subjects from them still count toward
> the card's totals, they just don't earn a named row. No new receipt kind
> was added — `_agent_work_card` now projects into the EXISTING
> `checklist` shape via a new `ConciergeHomeChecks` excluded field, closed
> polarity, same geometry as the open-polarity branch.

## One paragraph

The crown can be occupied by **23 card kinds**. It renders **one** receipt:
two strings in a gold-tinted box — `item.title` in uppercase mono and
`item.row_line` in caption grey (`TripsStackCrown.tsx:202-219`). Meanwhile
**7 of those 23 kinds compute rich, contract-validated visual substrate**
(settlement transfers, readiness checklists, day spines, candidate sets with
a marked leader, before→after diffs) and **none of it reaches the crown** —
the Trips wire carries no `structured` and no `focus`
(`TripsHomeStackCrown`, `schema.gen.ts:23906-23933`). The ratified item
contract already names the missing field —
`receipt — which typed receipt variant renders when crowned`
(`trips-home-promotion-model-2026-07-27.md:251-259`) — and it was never
built. The consolidation this surface needs is not fewer card kinds; it is
**one typed receipt union, 23 kinds → 8 render shapes + a stamp.**
(Revised same day from six, then from seven — see the corrections after Part 2's table:
`agent_work` and `audio_tour` already have receipts *designed* on the
Focus/Room/Range board, `weather` has substrate the producer discards, and
the genuinely-empty set is **7 kinds, not 10**; and `focus.call` was inventoried as substrate but never given a shape.)

---

## Part 1 — What the crown renders today

The whole receipt, verbatim from `travel-app/components/trips/TripsStackCrown.tsx:202-219`:

```
<View style={styles.receipt}>          // gold hairline, gold 7% wash
  <VText variant="monoStampStrong" numberOfLines={2}>{crown.item.title}</VText>
  <VText variant="caption"         numberOfLines={2}>{crown.item.row_line}</VText>
</View>
```

Three structural facts follow from this:

1. **It is text-only for every kind.** There is no branch on `kind`, on
   `tier`, or on anything else. A settle-up crown, a stay race, a weather
   alert and a memory echo render identical geometry.
2. **It reads the wrong field.** `row_line` is the *docked-row* field —
   its budget is `CONTRACTS["home_card_preview"].max_for("body")`
   (`models.py:768`), authored for a 60pt row, not for the hero. This was
   flagged 2026-07-30 and is still true at HEAD.
3. **Most kinds don't even author it.** `row_line` falls back
   `row_line or body or title` (`models.py:773`). Only 11 of ~30 emission
   sites author a real `row_line`; the rest inherit `body`, which is prose
   written for a full card and frequently templated — the same generic-fallback
   root cause that produced the identical-docked-rows defect.

The crown's other three regions are in good shape and are **not** what this
audit proposes changing: identity block → trip door (chevron, `:130-136`),
facepile + empty chair → people (`:138-157`), foot → CTA or the
Approve/Decline confirm pair (`:222-269`).

---

## Part 2 — The 23 kinds and the receipt each one *could* render

Source: `ConciergeHomeCardKind` (`concierge_feed/models.py:56-80`), the
priority ladder (`models.py:119-203`), `DECK_REQUIRED_KINDS`
(`models.py:454-464`), and every producer emission site in
`concierge_feed/producers.py`.

**Legend for "Substrate":** what the producer already computes and validates.
`structured.<layout>` = `DeckStructured`; `focus.<layout>` = `DeckFocus`;
`—` = nothing but prose.

| # | Kind | Producer | Prio | Tier | Substrate it already computes | `row_line` authored | Receipt today |
|---|---|---|---|---|---|---|---|
| 1 | `urgent_trip_action` | `_needs_you_cards:772` (hold offer) | 96 | 0 | `structured.proposal_approval` | no → `body` | 2 strings |
| 2 | `urgent_trip_action` | `_needs_you_cards:858` (proposal) | 94 | 2 | `structured.proposal_approval` (`build_proposal_approval_structured`) | no → `body` | 2 strings |
| 3 | `urgent_trip_action` | `_needs_you_cards:925` (booking status) | 90 | 1 | `focus.call` (`build_call_booking_status_focus`) | no → `body` | 2 strings |
| 4 | `constraint_alert` | attention `constraint_meal` | 89 | 1 | **deck-required**, from `HomeCard.focus` | `HomeCard.row_line` | 2 strings |
| 5 | `stay_compare` | `stay_compare.py:24` | 88 | 2 | `focus.compare` — exactly 2 candidates, ≤1 leader | no | 2 strings |
| 6 | `daily_brief` | attention `morning_brief` | 86 | 3 | — | `HomeCard.row_line` | 2 strings |
| 7 | `atlas_homecoming` | `producers.py:1245` | 85 | 3 | — | `"{n} days home"` | 2 strings |
| 8 | `trip_retrospective` | attention `trip_retrospective` / `story_ready` | 84 / 70 | 3 | — | only for `story_ready` | 2 strings |
| 9 | `imminent_trip` | `_trip_lifecycle_cards:2167` | 84 | 3 | — | `"Starts {label}"` | 2 strings |
| 10 | `weather` | `_weather_cards:2490` | 91 / 84 | 1 / 3 | — | no | 2 strings |
| 11 | `agent_work` | `_agent_work_card:1369` | 83 | 3 | ledger rows (`proactive_events`); `WorkReceiptPayload` exists in `core/models/work_receipts.py` | yes | 2 strings |
| 12 | `near_you` | `_near_you_cards:2700` | 82/63/52 (+6 taste) | 3 | `focus.near_you` — places w/ `walk_min`, `tag` | no | 2 strings |
| 13 | `live_trip` | `_trip_lifecycle_cards:2140` | 92 | 1 | — | `_live_day_row_line` | 2 strings |
| 14 | `group_room` | `_group_room_card:1299` | 79 / 67 | 2 / 3 | `_GroupRoomSignal` (snippet, sender, unread) | `"{n} new in the room"` | 2 strings |
| 15 | `audio_tour` | `_narration_stop_card:1451` | 77 | 3 | — | `"Tour ready · {stop}"` | 2 strings |
| 16 | `capture_nudge` | attention `capture_nudge` | 76 | 3 | — | `HomeCard.row_line` | 2 strings |
| 17 | `trip_thread` | group-state `just_accepted` | 74 | 1 | invite rows | no → `body` | 2 strings |
| 18 | `planning_brief` | `producers.py:1116` / `_readiness_card:1983` | 73 | 2 | `focus.brief` (day spine) **and** `structured.plan_readiness` (rows) | `"{n} still to close"` | 2 strings |
| 19 | `settlement_closeout` | `_settlement_card:2011` | 71 | 2 | `structured.settle` — `people[]`, `settlement_transfers[]`, direction | no → `body` | 2 strings |
| 20 | `pre_trip_prep` | `producers.py:1152` | 72 | 2 | — | `"{n} days out"` | 2 strings |
| 21 | `trip_thread` | `_trip_lifecycle_cards:2188` (pre) | 68 | 2 | — | `"Starts {label}"` | 2 strings |
| 22 | `intake_offer` | `_intake_offer_card:1499` | 66 | 2 | — | fixed string | 2 strings |
| 23 | `trip_thread` | `_group_commitment_card:2045` | 65 | 2 | member + pending-invite counts | no → `body` | 2 strings |
| 24 | `local_take` | `_local_take_cards:2722` | 63 | 3 | — | no | 2 strings |
| 25 | `starter` | `_starter_cards:2843` | 62/22/21/20 | 4 | — | no | 2 strings |
| 26 | `trip_thread` | group-state `unread_intake` | 60 | 2 | intake answers | no → `body` | 2 strings |
| 27 | `saved_cluster` | `_saved_cluster_cards:2363` | 58−idx | 3 | `focus.pick` — candidates, one leader | no | 2 strings |
| 28 | `trip_thread` | group-state `pending_too_long` | 52 | 3 | invite age | no → `body` | 2 strings |
| 29 | `memory_echo` | `_memory_cards:2395` | 46 / 44−idx | 3 | — | no | 2 strings |

(29 emission sites across 23 declared kinds. `trip_thread` alone carries
five structurally different situations — see Part 4.)

### ⚠️ Correction, same day: 23 kinds is not 23 cards, and three rows above are wrong

The kind enum has 23 entries. The number of **distinct cards a traveller can
actually see is closer to 40**, because nine kinds each hide several
situations that differ structurally, not cosmetically:

| Kind | Situations it carries |
|---|---|
| `trip_thread` | **5** — just-accepted · unread-intake · pending-too-long · group-commitment · pre-trip lifecycle |
| `urgent_trip_action` | **4** — booking-hold offer · proposal · booking status · the default catch-all for any archetype `_attention_kind` doesn't map |
| `starter` | **4** — half-planned · nearby · style · weekend |
| `near_you` | **3** — active-trip · live-location · idle (plus the taste boost) |
| `weather` · `group_room` · `memory_echo` · `local_take` · `trip_retrospective` | **2** each |

This matters for the receipt work in one specific way: **the `stamp` bucket
looks small at kind level and is not**, and `trip_thread` doing five jobs
under one label is the concrete argument for giving the invite its own kind
rather than making it a sixth (Part 4).

**And three rows in the table above under-report their substrate:**

- **`agent_work` and `audio_tour` already have receipts designed** — on the
  Focus/Room/Range board, 2026-07-30. `FRRCiteWork` renders ✓-rows of what
  was checked with a `CHECKED 04:12` stamp; `FRRCiteAudio` renders a
  **waveform** with a play control and the played portion darkened. Filing
  either as `stamp` contradicts a board that already exists.
- **`weather` has real substrate and the table said it had none.** The
  producer receives condition, temperature, precipitation and wind
  (`ConciergeAmbientContext`), interpolates them into a sentence, and drops
  the values. The card's own id is
  `weather:{place}:{condition}:{round(temp)}` — the numbers are one line
  above where they are discarded. Keeping them is a producer change, not a
  new pipeline.

**So the truly empty set is 7, not 10:** `capture_nudge` (fires on the clock,
knows only a day number) · `trip_retrospective` (a door back to a finished
itinerary) · `memory_echo` · `local_take` (the take *is* the prose) ·
`starter` (cold account — nothing exists to cite, by definition) ·
`atlas_homecoming` (knows one integer) · `intake_offer` (an offer, not a
report — nothing has happened yet). Those get `stamp`, and nothing else,
forever.

### The eight visual receipt shapes that already exist and are already validated

Every one of these has a contract checker (`_structured_contract_issues`
`models.py:472-506`, `_focus_contract_issues` `models.py:509-546`) and a
shipped renderer in `travel-app/components/decision-deck/` — which is
**production-dead**, mounted only by `app/dev/*` galleries since `c8fffe2b`.

| Substrate | Fields | Natural visual | Renderer that exists |
|---|---|---|---|
| `structured.proposal_approval` | `current_state`, `proposed_state`, `impact` | before → after diff | `DeckStructuredFace` |
| `structured.choice_vote` / `vote` | `options[]` w/ `leading` | tally bar | `DeckStructuredFace` |
| `structured.settle` | `people[]` (+`amount`), `settlement_transfers[]`, `settlement_direction` | payer chips + direction | `DeckStructuredFace` |
| `structured.plan_readiness` / `traveler_readiness` | `readiness_rows[]` (`label`, `detail`, `resolved`) | N-of-M checklist | `DeckStructuredFace` |
| `focus.pick` | `candidates[]` (`name`, `walk`, `price`, `attribute`, `leading`) | candidate chips, leader marked | `DeckPickFace` |
| `focus.compare` | exactly 2 candidates, ≤1 leader | two-up compare | `DeckCompareFace` |
| `focus.call` | `subject`, `chips[]`, `deadline_at` | flags + countdown | `DeckCallFace` |
| `focus.brief` | `days[]` (`label`, `title`, `is_open`) | day spine w/ open gaps | `DeckBriefFace` |
| `focus.near_you` | `places[]` (`name`, `walk_min`, `tag`) | place list w/ distance | `DeckNearYouFace` |

**All display values are already pre-formatted by the backend** — "€128",
"12 min walk" — precisely so the client never re-derives money or distance
(`vesper_cards.py:75-86`). The hard part of a visual receipt is done.

---

## Part 3 — The consolidation

### What NOT to consolidate

Do not collapse the 23 kinds. `kind` is doing three real jobs that a
smaller vocabulary would break:

- it is the **feedback-tuning key** (`_load_feedback_tuning` →
  `suppressed_kinds`, `kind_penalties`, `useful_kind_boosts`);
- it drives **posture** (`_posture_for_projection`, `trips_stack.py:318-354`);
- it is the **analytics unit** — the spec names invite conversion as the
  wedge metric, which requires the invite to be its own kind.

### What to consolidate

**One new typed field: `receipt`, a discriminated union of eight shapes.**
Symmetric with `destination`, which is already a well-designed 12-type
discriminated union on the same model. The crown goes from *one* render
path with 23 inputs to *eight* render paths with a declared input each.

| Shape | Renders | Fed by |
|---|---|---|
| `diff` | before → after, one impact line | `urgent_trip_action` (proposal) |
| `call` | subject, real flag chips, stakes, deadline | `constraint_alert`, `urgent_trip_action` (hold · catch · booking status) |
| `ledger` | 2–3 payer chips w/ amounts, direction | `settlement_closeout` |
| `checklist` | rows, **open** polarity: dashed, named, unresolved | `planning_brief`, `pre_trip_prep` |
| `checklist` | rows, **closed** polarity: ✓, named, past tense | `agent_work` |
| `candidates` | name over meta, one leader marked | `stay_compare`, `saved_cluster`, `near_you` |
| `spine` | day strip, open days hollow | `live_trip`, `daily_brief`, `trip_thread` (pre), `imminent_trip` |
| `people` | facepile: filled / dashed-invited / empty chair | `group_room`, all `trip_thread` group states, **`invite_seat` (new)** |
| `waveform` | play control, bars, played portion darkened | `audio_tour` |
| `conditions` | condition glyph + temperature | `weather` *(producer must stop discarding the values)* |
| `stamp` *(fallback)* | one grounded fact, no title line | the 7 genuinely empty kinds |

### ⚠️ Second correction: `call` is a shape, and `constraint_alert` was mis-mapped

Part 2's substrate table lists `focus.call` — "flags + countdown",
`DeckCallFace` — and the shape union above originally **gave it no shape**,
folding `urgent_trip_action` into `diff` and putting `constraint_alert`
there too. Both are wrong.

**A diff proposes a change; a call reports a break.** A diff is state A →
state B with an approve/decline foot. A call is a named subject in trouble:
`subject` · `subject_meta` · `chips[]` (real flags — `"ELIF · COELIAC"`,
`"5 SEATED"`) · `stakes` · `deadline_at`, and a foot that is
**work-or-dismiss** — "Find an alternative" / "Keep it anyway" — modelled
already as `primary_kind: find_alt` / `secondary_kind: keep`. Nothing is
being approved, so it is not the confirm pair.

`DeckCallSubstrate.variant` is `held | conflict | reschedule` and **four
builders already ship**: `build_call_conflict_focus`,
`build_call_reschedule_focus`, `build_call_held_focus`,
`build_call_booking_status_focus`. `constraint_alert` is the canonical one —
`feed.py` builds it with `build_call_conflict_focus`.

**The process lesson:** a substrate inventory and a shape union have to be
reconciled *against each other*, not written in sequence. Part 2 knew about
`focus.call`; Part 3 didn't read Part 2.

**`checks` is not a separate shape — it is `checklist` with `resolved`
flipped.** Open loops render dashed and unresolved; completed overnight
checks render ✓ and past-tense. Same geometry, opposite polarity, and
`DeckReadinessRow` **already carries `resolved: bool`**, so the flag exists
and costs nothing. That is the cheapest shape in the set: `agent_work` gets
a real receipt for the price of a boolean.

### The three rules that keep it honest

1. **Project, never copy.** `test_trips_stack_projection.py` pins that Trips
   never copies Deck substrate onto the wire, and the destination refactor's
   own docstring states the intent: *resolve a target "without creating a
   second action UI."* Each receipt shape gets its own minimal model —
   `ReceiptLedger{direction, counterparties[≤3]{initial,label,amount_label}, total_label}`
   — not a `DeckStructured` passthrough. Six small models, no substrate leak.
2. **Grounded or absent.** No substrate → `stamp`. Never a synthesised
   visual. This is not hypothetical: the `standingProgress` diagram deleted
   in phase 1 derived "N OF M DAYS HAVE A SHAPE" from `crown.item.depth`
   (a feed-card count) with a hardcoded 6-day fallback. The union must make
   that unrepresentable, not merely discouraged.
3. **A receipt is evidence, not a door.** The receipt tap was retired
   2026-07-31 for good reasons. A visual receipt must not smuggle it back —
   no tappable chips, no per-row navigation. The foot still owns the action.

### Why this also answers "too much text"

The 07-30 density pass measured ~65 text elements on a busy screen, ~30
carrying zero unique information. A visual receipt is the only move in the
backlog that **removes** text while **adding** information: the settle crown
today says `"3 SHARES OPEN"` / `"You owe Elif and Ben"` (2 elements, no
amounts); the `ledger` shape says the same in two avatar chips carrying the
real numbers. Same slot, fewer strings, more truth.

---

## Part 4 — The invite card

### It is already specified, and it is the one channel never built

The stack model ratified **three group channels**: the facepile with its
dashed empty chair, names-in-facts, and *invite as a tier-2 ladder item
that can win the crown*. The doc is explicit about the division of labour
(`trips-home-promotion-model-2026-07-27.md:517-532`):

| | CONNECT section | invite as tier-2 stack item |
|---|---|---|
| Nature | a **door** | a **judgment** |
| When it shows | always | only when the group gap is the actual bottleneck |
| Can it take the crown | never | **yes, on merit** |
| Voice | none — it is chrome | composed at promotion |
| Escalates | never | demotes the moment something more urgent exists |

**Both doors are built. The judgment is not.** The CONNECT section ships in
`TripsHomeTrail.tsx:132` (`onConnect` → `index.tsx:700`), and the crown
facepile's empty chair ships at `TripsStackCrown.tsx:138-157` →
`openStackCrownPeople` (`index.tsx:809-822`). Nothing on the page ever
*says* the group gap is what's blocking the trip.

### The gap in the current producers is precise

Five invite-adjacent producers exist. **Every one requires invites to
already exist:**

| Producer | Fires when | Kind emitted |
|---|---|---|
| `just_accepted` (74) | an invite was consumed <36h ago | `trip_thread` |
| `unread_intake` (60) | a consumed invite left unread answers | `trip_thread` |
| `pending_too_long` (52) | an invite is >3 days unanswered | `trip_thread` |
| `_group_commitment_card` (65) | **≥3 total group AND >1 pending invite** AND ≥14 days out | `trip_thread` |
| `_group_room_card` (79/67) | unread messages in a ≥2-member room | `group_room` |

A trip with the organizer alone — or one member and zero pending invites —
produces **no invite signal of any kind**. That is exactly the wedge case
the whole positioning rests on.

### Recommendation

**A new kind, `invite_seat`, not a sixth `trip_thread` overload.**
`trip_thread` already carries five structurally different situations and is
consequently un-suppressible (one feedback penalty silences all five) and
un-measurable (invite conversion is the named wedge metric,
`…-2026-07-27.md:734`). It also gets its own `KIND_LABELS` entry — the four
existing invite states all render as "Trip thread" today.

**Fires on the gap, not on the absence.** The honest trigger is a group the
plan *describes* being larger than the group *present* — the spec's own
group-described vs group-present scoring, grounded only in the vote roster
and intake party size, **never chat inference**. A solo trip that was always
solo has no gap; a trip whose intake says "four of us" with one member does.

**Two strengths, following the `group_room` precedent** (79 waiting / 67
alive) rather than one flat number. The spec says tier 2 items "beat gifts
only past an age threshold", and `_is_lead_queue_eligible` gates the crown
at priority ≥74:

- below the floor while the gap is young → ambient, can still reach the
  crown on a quiet day, can never seize it;
- ≥74 once the gap has persisted past a threshold → crown-eligible on merit.

**Destination costs one literal value.** The empty chair already routes to
`routes.tripDetails(tripId, {focus: 'people'})`, but `TripsHomeDestination`
cannot express it: `details_section` is `Literal["bookings"] | None`
(`trips_stack.py:62`). Adding `"people"` reuses the existing `trip_details`
type — no new destination case, no new route.

**Its receipt is the `people` shape, and that is the point.** Filled avatars
for members, dashed for invited-not-yet-joined, one empty chair for the gap.
Zero prose. It is the cleanest possible pilot for Part 3 — the one card
whose receipt is *entirely* visual and where the visual is more honest than
any sentence, because a facepile can't round up.

**The guardrail, restated:** the CONNECT *section* never counts and never
pressures. The stack *item* may state the gap once, with a voice, and must
demote the instant anything more urgent exists. No streaks, no "invite 2
more to unlock", no progress meter. The pre-registered falsifier stands: if
the invite reads as growth-hacking when crowned, it was wrong to crown it.

---

## Sequence

1. `receipt` union on `TripsHomeStackCrown` + the `people` and `ledger`
   shapes. Two shapes prove the contract; `settlement_closeout` and the
   group states already have their substrate.
2. `invite_seat` producer + `details_section: "people"`. Ships on the
   `people` shape from step 1.
3. `checklist` — build it with `resolved` honoured from the start, so
   `agent_work`'s closed-polarity receipt lands in the same step for the
   price of a boolean. Highest value per unit of work in the whole set.
4. `candidates`, `spine`, `diff`, `call`, `waveform` — mechanical once the
   union holds; each is a projection of substrate already computed. `call`
   also needs its work-or-dismiss foot, which is a third foot state beside
   the CTA and the confirm pair.
5. `conditions` — needs the one producer change (`_weather_cards` must keep
   condition/temperature instead of interpolating them into a sentence).
   Sequence it last precisely because it is the only shape that isn't
   already a pure projection.
6. Retire `row_line` from the crown. It is the docked-row field; once every
   crown has a typed receipt it has no job in the hero.

## Not missing receipts — missing cards

Four item kinds the stack-model spec introduced on 2026-07-27 have **no
producer at all**; `overlap_match` returns zero hits across both repos. They
are listed here so a later pass doesn't rediscover them as a hole in the
union:

| Kind | What it would say | Likely receipt |
|---|---|---|
| `overlap_match` | "You and Dana are both free the same week" | `people` with a second axis (dates) |
| `autonomy_offer` | "Want me to book dinners from now on?" | none — it's a question; the confirm pair *is* the card |
| `question` | a low-confidence ask Vesper needs settled | answer chips, closest to `choice_vote` — undecided |
| `group_echo` | what the room did while you were away | `people` or `stamp`, depending on whether names are grounded |

## Open questions for the founder

- **~~Does the receipt ever show on rows?~~ DECIDED 2026-08-03: crown-only.**
  `receipt` lives on `TripsHomeStackCrown`, never on `TripsHomeStackItem`;
  rows keep `row_line`, which is the field it was always budgeted for.
  Reasons, in order of weight: (a) a row is **60pt** (`rowMinHeight`) already
  holding two lines and two tap regions, and the board's shapes run 40–70px
  on their own — a receipt roughly doubles it, and two doubled rows is a
  second crown's worth of page; (b) rows are already under width pressure —
  they lost their date range on 07-31 to a 393pt wrap; (c) it would undo
  phase 2, which pulled rows out of the crown card precisely so they'd read
  as lower fidelity (*cards for seduction, rows for administration*);
  (d) sharpest — **a receipt makes a judgment feel earned, and a row carries
  a pointer, not a judgment.** Evidence for a claim nobody is making is just
  more text. ⚠️ This is not "rows are never visual": the right rail already
  renders an `AvatarStack` facepile. That is a row-native affordance, not the
  receipt union.
- **`stamp` fallback, or no receipt at all?** Seven kinds have no substrate.
  Grounded-or-absent argues for rendering nothing; the 07-30 "hero too empty"
  finding argues the crown needs a foot-band partner. The two well-formed
  foot states already resolve that, so absent may now be safe. Measured on
  the board: dropping the stamp's title line buys **19px**, so decide it on
  information, not on space.
- **Does `agent_work` keep its prose?** It has `WorkReceiptPayload`, a
  seven-move prose anatomy, and the earlier answer here was "prose, so
  `stamp` with a longer budget." That was wrong on the evidence: the
  Focus/Room/Range board already draws it as named ✓-rows, and named
  subjects are exactly what the producer computes (`_AGENT_WORK_MAX_SUBJECTS
  = 3`). The full prose anatomy belongs on the *detail* surface; the crown
  gets the closed-polarity checklist. The open version of this question is
  narrower: **does the crown's receipt cite the work receipt, or replace
  it?**
