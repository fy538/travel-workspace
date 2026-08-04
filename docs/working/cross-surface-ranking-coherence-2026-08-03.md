---
doc_type: working
status: active
owner: founder / product / backend
created: 2026-08-03
last_verified: 2026-08-03
expires: 2026-09-02
why_new: No existing document owns the question of whether Trips, Vesper, and Places should share a holistic ranking layer, or inventories the surface-ranking mechanisms and their cross-surface coupling points. The navigation IA proposal owns container ownership; this doc owns what fills the containers.
promotes_to: docs/architecture decision record on cross-surface content arbitration, plus affected surface FEATURE.md files
supersedes: []
source_of_truth_for:
  - cross-surface-ranking-inventory-2026-08
  - cross-surface-coherence-recommendation
---

# Cross-Surface Ranking Coherence — Trips, Vesper, Places

> **Working analysis, not product canon.** Question asked: the three root
> surfaces each control what's shown to the user — should ranking be
> holistic, or is per-surface ranking correct? What does not unifying cost
> in coherence, and what does unifying cost in complexity?
>
> All code claims below were audited twice (initial pass + adversarial
> re-verification on 2026-08-03). Corrections from the second pass are
> folded in, not appended.

## Verdict up front

**Do not unify the ranking functions. Unify the two layers under them:
exposure and fact identity.** The surfaces order content by genuinely
different objectives (urgency / browse stability / novelty rotation), and
collapsing those into one score serves none of them. The incoherence users
would actually feel comes from the layers below ranking — the same fact
appearing on two surfaces independently, and engagement on one surface not
informing another at the level of the specific fact.

A sharper finding from the audit: **personalization investment is
inverted.** The deepest ranker in the codebase serves a place-scoped angle
feed, while the three flagship root surfaces run a static table, a clock,
and a priority queue. A user whose taste visibly shapes one feed and
visibly doesn't shape the adjacent ones is the most likely source of
"this app feels incoherent."

## Inventory: four rankers, not three

| Surface / feed | Code | Mechanism | Personalized? | Learns from behavior? |
|---|---|---|---|---|
| Trips home cards | `backend/home/concierge_feed/ranking.py` | Integer priorities + per-user learned kind boosts/penalties from `concierge_card_feedback`; dedupe by `attention_case_id` with `home.primary` projection preference | Yes (tuning) | Yes (dismiss/useful feedback) |
| Places sections | `backend/places/ranking.py` | Two hardcoded priority tables — spine of 3 (expiry, group-waiting, gap) always precedes a floor of 13; cap 4 | No | No |
| Vesper root band | `backend/home/vesper_workbench/rotation.py` + `selector.py` | Round-robin cursor over 4 list kinds (`sessions → route → season → here`), 6h dwell, server-owned; within a list, deterministic edge-time sort | No | No |
| For You angles (place-scoped) | `backend/api/routes/users/insights.py` (~line 340) | 7-step pipeline: distinctiveness sort → LLM rerank vs Personal Memory → warm engagement stats → LLM cold prior (<5 impressions) → follow-graph affinity → lens-diversity injection → top 8 | Yes (deeply) | Yes (impression write-back loop) |

Plus one non-surface layer that is already holistic:

- **Push arbiter** (`backend/notifications/arbiter.py`): one
  gate → rank → pick → dispatch chokepoint for all proactive drivers, with
  learned value multipliers, tone learning, holdout experiment, 8/24h
  interruptive caps, quiet hours, suppression. This is the "holistic
  layer" — built for the push channel only. Nothing equivalent governs the
  three read surfaces.

So the honest answer to "does each page have its own ranking algorithm" is:
it's more divergent than that. One page learns, one reads a static table,
one reads a clock, and the most advanced learner is attached to an
endpoint rather than a root surface.

## Cross-surface coupling that already exists (audit corrections)

The first-pass claim "surfaces share nothing" was wrong in two places:

1. **`concierge_card_feedback` has two consumers, not one.**
   `backend/notifications/accept.py` reads `count_recent_dismissals` and
   feeds a ratchet that both decays p(accept) and raises the channel accept
   threshold. In-app dismissals therefore DO cross into push today — but as
   a **volume** signal ("user is dismissing a lot → back off globally"),
   not a **per-fact** signal ("user dismissed the anniversary card → don't
   push the anniversary").

2. **An impression write-back loop exists and is live.**
   `user_events` → `angle_user_engagement` materialized view
   (`backend/core/db/engagement.py`) → reward-weighted behavioral score
   (saves=3, upvotes=2, dismissals=−0.5, downvotes=−3, normalized), with
   `MIN_IMPRESSIONS_FOR_WARM = 5` gating fallback to an LLM cold prior.
   Consumed by the For You pipeline. The pattern is proven in-house — it
   just serves only angles.

What genuinely does not exist:

- **No exposure recording for Trips cards or Places sections.**
  `concierge_home_card_impression` events are emitted but never read back
  by any ranker. `places/` neither writes nor reads exposure — and
  `places/ranking.py`'s own docstring records the consequence: rotation was
  tried, looked arbitrary without recorded exposure, and was retreated to
  static ordering.
- **No per-fact identity across surfaces.** `attention_case_id` collapse
  stops at the Trips/notifications boundary. Places sections and Vesper
  lists carry no attention identity.

## Content-family overlap (the coherence exposure)

Families with 2+ independent surface owners today:

| Family | Owners | Current severity |
|---|---|---|
| Anniversary / On This Day | Places section (`places/anniversary.py`) + daily push (`notifications/push.py`) | **Latent** — ANNIVERSARY_PUSH is flag-dark in prod; collision is theoretical until the flag flips |
| Itinerary gap | Places spine + Trips deck payloads + arbiter/notification gates | Live |
| Nearby | Trips stack + Places + Discover models | Live |
| Weather | Trips cards + Vesper workbench context + push prompts | Live (different presentations, same underlying fact) |

At today's family count (~16) this is annoying but survivable. It degrades
non-linearly: each new producer adds N potential collisions, and with no
shared identity, correctness depends on each author remembering the other
three surfaces.

## What the outside literature says

Mostly about unifying **models**, not **policy** — and the applicable
lesson cuts against naive unification:

- Netflix's [UniCoRn](https://arxiv.org/abs/2408.10394) (RecSys '24)
  merged search + recs into one deep model to kill maintenance debt —
  a catalog-scale play (millions of items, shared representations).
  Does not transfer to ~16 content families and a 4-slot feed.
- [RankGraph](https://arxiv.org/html/2509.02942) and
  [Multi-surface Co-training](https://dl.acm.org/doi/10.1145/3705328.3748101)
  (RecSys '25): share **representations/content understanding** across
  surfaces while keeping per-surface serving. This shape does transfer —
  it is roughly what sharing Personal Memory + exposure across surfaces
  achieves without touching ordering.
- [OneRanker](https://arxiv.org/html/2603.02999v2) documents the
  counter-argument: fusing objectives with different geometry (coverage is
  order-invariant and favors breadth; ranking quality is position-sensitive
  and favors concentration) creates gradient/objective conflict. Trips
  (urgency), Places (browse stability), and Vesper (novelty rotation) have
  exactly this kind of objective divergence.

## Recommendation

Keep per-surface ordering. Build three shared substrates, in order:

### 1. Shared exposure ledger — ✅ SHIPPED 2026-08-03 (flag-dark)

Built same day (travel-agent `5dd11f7b`, travel-app `6fc57ee0`):
`backend/core/db/exposure.py` (windowed read model over `user_events`),
new `places_section_impression` / `places_section_opened` events with a
dwell-gated FE emitter mirroring the concierge pattern, and two
default-off consumers — `PLACES_EXPOSURE_ROTATION_ENABLED` (floor
sections seen 3+ times unopened rotate behind fresh material; spine never
rotates) and `CONCIERGE_EXPOSURE_FATIGUE_ENABLED` (bounded decay, max 12,
under the explicit-feedback cap of 36; exposure rides inside
`_FeedbackTuning`). Remaining before flag flip: accumulate real
impressions in dogfood, then device QA the rotation.

### 2. Per-fact attention identity beyond Trips — ✅ PILOT SHIPPED 2026-08-03

On This Day pilot (travel-agent `c502593b`, travel-app `92edab29`):
`PlacesSection.fact_key` (server-owned, additive on the wire) carries a
cross-surface fact identity — `on_this_day:{source_type}:{source_id}`,
mirroring the attention-registry key format and coinciding with
`attention_key` for trip-sourced facts (the registry's ON_THIS_DAY
subject_type is trip-only, which is why the key is composed rather than
taken from `attention_key()` directly). The client echoes it into
exposure-event context; `get_fact_exposure()` reads it back across all
registered surfaces (engagement-only facts count — a touched fact is
known even without a dwell); `send_on_this_day_push` suppresses when the
fact was seen in-app within 7 days, degrading open on ledger failure.
**The ANNIVERSARY_PUSH flip is now collision-safe by construction.**

Remaining to generalize the pattern: set `fact_key` on other fact-shaped
sections (gap, group-waiting) and their push twins; consider the Atlas
On This Day strip emitting the same key; decide whether the arbiter's
candidate gate should consult `get_fact_exposure` generically instead of
per-producer calls.

### 3. Enforce the ownership rule in code — ✅ SHIPPED 2026-08-03

**Correction to this doc's own premise.** It claimed "when a fact
qualifies for two surfaces, nothing arbitrates." That was wrong.
`attention_type_registry` already carries `home_primary_owner`, and
`channel_dispatch.py:1406` already refuses to write a Trips-home card
when a type declares a different owner (`proposal_read_model` vs
`notification_dispatcher`) — live, enforced arbitration for the
notification ↔ Trips-home boundary, plus startup validation that owner
and projection agree.

What that registry genuinely cannot express is the **two root surfaces
that postdate it**: its `Projection` vocabulary is delivery channels plus
`home.primary`/`home.secondary` (Trips). There is no `places` or `vesper`
member, so anything rendered by Places or the Vesper workbench is
invisible to ownership it already enforces.

`backend/core/surface_ownership.py` (`5812499c`) closes that at the level
the collisions actually occur — the **content family**, whose members
live in four native vocabularies (`AttentionType`, `PlacesSectionReason`,
concierge card kinds, workbench list kinds). Four families, each with a
verified multi-surface projection: anniversary → places, itinerary_gap →
trips, nearby → places, weather → trips; each carrying a stated `why`.

The encoded rule is deliberately **not** "only one surface may render a
fact" — an anniversary belongs in both Places and push. It is: one
surface is canonical, others echo, and an echo yields when the owner has
already done the job (`defer_to_owner_surface`, reading the step-2 fact
ledger). Import-time validation — matching `attention_type_registry`'s
precedent, so no bespoke CI hook — rejects nonexistent members,
double-claimed projections, an owner also listed as an echo, an owner
that renders nothing, and unstated reasons. **A renamed section reason
now breaks the build rather than silently orphaning the rule.**

Step 2's hardcoded anniversary suppression was refactored into an
instance of this general rule; its tests passed unchanged, which is the
evidence behavior was preserved.

**Prefixes completed 2026-08-03** (travel-agent `4663c434`, travel-app
`bdafe980`). All four families now mint resolvable keys:
`nearby:place:{id}` (Places, owner), `weather:itinerary_block:{id}`
(concierge card, owner), `itinerary_gap:trip_day:{id}` (Places, echo),
`on_this_day:{type}:{id}` (Places, owner). Subjects are deliberately
stable — the corpus place rather than drifting coordinates, the affected
block rather than the risk word — and a section with no resolved place
claims no identity rather than a fake one. `ConciergeHomeCard.fact_key`
plus its FE echo is the symmetric half of the Places emitter, without
which Trips-owned families would have no readable owner emission.

Two further registry corrections, found by checking rather than trusting
the earlier declarations: `itinerary_gap` had claimed `daily_brief` (that
is the morning brief — the real Trips projection is
`AUTOPILOT_FILL_DAYS`, rendered as the `planning_brief` kind that three
attention types share, so the family now declares the precise type and
not the coarser kind), and `weather` had claimed `VENUE_DISRUPTION`
(which renders as `constraint_alert` and means a venue changed, weather
or not).

Also fixed a latent bug the prefixes would have activated:
`defer_to_owner_surface` read exposure from every surface, so in a
multi-echo family one echo could answer for another and suppress a
legitimate projection. Deferral is now scoped to the owner's own emitter,
and an owner with no emitter can never be deferred to.

**Echo deferral wired flag-dark 2026-08-03** (`d31393de`), behind
`CROSS_SURFACE_ECHO_DEFERRAL_ENABLED`. Two call sites, both written
generically over the registry rather than per family: the Places feed
drops any section whose `fact_key` belongs to a family Places only
echoes (today the itinerary gap), and the Vesper workbench drops
here-items for places already shown as nearby — dropping items rather
than force-excluding the kind, so the existing three-item eligibility
rule still decides whether a rotation turn is deserved. Flag-off is
tested as a true no-op: the ledger is not read at all, not merely
ignored. `deferred_fact_keys()` is the batch form (one ledger read per
owner emitter, not per fact); `defer_to_owner_surface()` is now a thin
wrapper over it so both share one set of rules.

`near_you` — Trips' echo of nearby — is deliberately not wired: the
producer carries a place *label*, not a corpus place id, so it cannot
name the fact without new plumbing through a file already over its size
budget.

Remaining: Vesper still has no exposure *emitter*, so vesper-owned
families could not be deferred to (nothing owns one today, so this is
latent rather than broken); `near_you` needs a place id to participate;
and longer term, consider whether the attention registry's `Projection`
should absorb `places`/`vesper` so the two registries converge into one.

Flip order for all four flags is its own section below.

### Also worth correcting: the inverted-investment gap

Independent of coherence plumbing, the For You pipeline's components
(memory rerank, warm/cold scoring, follow affinity) are modular and
already built. The concierge ranker consuming the engagement pattern
(step 1) and Places sections gaining even coarse affinity ordering within
the floor would close most of the felt gap between "the feed that knows
me" and "the feeds that don't." This is adoption, not construction —
consistent with the standing lesson that rankers here tend to already
exist (`concierge_feed` was adopted, not rebuilt, for trips-home).

## Flag flip order

Everything above ships dark. Four flags gate it, and the order matters
for one structural reason:

> **The emitters are not flagged. The consumers are.**
> `placesSectionTelemetry` and `conciergeHomeTelemetry` write to
> `user_events` whenever auth is live and the user id is a real UUID
> (mock mode is skipped). No backend flag gates them. So the ledger
> starts filling the moment the FE build ships, and every flag below
> only decides whether something *reads* it.

Turning a flag on before its data exists is not dangerous — each
consumer degrades to today's behavior on an empty read — it is simply
inert, which makes it impossible to tell a working feature from a
silent one. Hence: ship the emitters, let data land, then flip in this
order.

| # | Flag (env var) | What changes | Precondition |
|---|---|---|---|
| 0 | *(none — FE build)* | Impressions + `fact_key` start landing in `user_events` | The travel-app build carrying `placesSectionTelemetry` / card `factKey` is live |
| 1 | `ANNIVERSARY_PUSH_ENABLED` | Daily On This Day push starts sending | Step 0 live, so the push's (unflagged) deferral has a ledger to read |
| 2 | `PLACES_EXPOSURE_ROTATION_ENABLED` | Floor sections seen 3× unopened rotate back | Floor sections have ≥ `FLOOR_FATIGUE_IMPRESSIONS` (3) impressions for real users |
| 3 | `CONCIERGE_EXPOSURE_FATIGUE_ENABLED` | Repeatedly-ignored cards decay in priority | Cards have ≥ `FATIGUE_MIN_IMPRESSIONS` (5) impressions |
| 4 | `CROSS_SURFACE_ECHO_DEFERRAL_ENABLED` | Echo surfaces drop facts the owner already showed | Owner-surface impressions landing within the 7-day deferral window |

Notes on specific steps:

- **Step 1 is safe before step 0, just not yet useful.** The anniversary
  push deferral is deliberately unflagged, and degrades *open* — an
  empty ledger means the push sends, which is exactly the pre-existing
  behavior. Flipping it before the FE build simply reproduces the
  collision risk the deferral was built to remove, so there is no reason
  to.
- **Steps 2 and 3 are independent of each other.** Different surfaces,
  different thresholds; either can go first. They are ordered here only
  because Places has the lower threshold (3 vs 5) and will therefore
  have usable data sooner.
- **Step 4 goes last** because it is the only one that *removes*
  something from a screen. Verify on device that a deferred section's
  absence reads as calm rather than broken — that is a judgment call no
  test can make.

Two windows govern how long "let data land" takes: exposure is read over
`DEFAULT_EXPOSURE_WINDOW_DAYS` (14) for rotation and fatigue, and over 7
days for deferral. Impressions are dwell-gated at 800 ms, so a user who
opens a surface and leaves immediately contributes nothing.

**Rollback is symmetric and instant.** All four are pure read-side
overlays — no persisted state, no migration, no backfill. Turning any
flag off restores the previous behavior on the next request. That is
the argument for flipping them one at a time rather than together: if
something reads wrong on device, the flag that caused it is unambiguous.

## What NOT to build

- **A unified cross-surface scoring function.** Objective conflict per
  OneRanker; loses the explainability the static Places tables buy; and
  no user ever sees a ranking function — they see collisions and
  taste-blindness, which are fixed by the substrates above.
- **A single feed service owning all three surfaces.** The push arbiter is
  the cautionary sizing reference: it earns its complexity because push is
  interruptive and channel-scarce. Read surfaces are not.

## Cost/benefit summary

| Option | Cost | Payoff |
|---|---|---|
| Unify rankers | High (objective conflict, explainability loss, migration) | Low (users don't see sort math) |
| Exposure ledger | Low (existing pattern) | Places rotation unblocked; concierge fatigue signal; prerequisite for 2 |
| Per-fact identity | Medium | Cross-surface dismissal; safe ANNIVERSARY_PUSH flip; collision-proof new producers |
| Ownership registry | Low (after 2) | IA rule becomes executable; coherent single-owner presentation |
| Do nothing | Zero now | Coherence debt compounds per new producer; anniversary collision fires when flag flips |

## Open questions

- Should Vesper's rotation consult the exposure ledger (skip a kind the
  user just saw elsewhere), or is its clock-driven independence part of
  its character? Leaning: leave it alone until evidence.
- Does the ownership registry live in `core/surfaces/definitions.py`
  (which already catalogs every surface with target contracts) or a new
  content-family registry? The surface catalogue is adjacent but
  surface-keyed, not fact-keyed.
- For You's LLM rerank cost per request (Haiku ×2 on cold paths) if
  adopted by root surfaces — needs the same effort/cost treatment the
  planning pipeline got.
