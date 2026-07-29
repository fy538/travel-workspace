---
doc_type: working
status: active
owner: founder / eng
created: 2026-07-28
expires: 2026-08-27
why_new: A 2026-07-28 strategy session (booking → venture path → M4 exit
  artifact) converged on a product area nobody owns in writing — the
  personal trip artifact. Code inventory found ~9 overlapping generator
  mechanisms from 3 product eras with no shared substrate. This doc owns
  the vision (what we render, why it's valuable, why users return), the
  generation architecture rules, and the consolidation frame. It does NOT
  own execution order — sequencing defers to the home-surfaces program
  and the dogfood phase.
promotes_to: docs/product/ if the dogfood validates the artifact loop
supersedes: []
depends_on:
  - docs/working/home-surfaces-program-2026-07-28.md   # seam rules; ranker ownership
  - docs/product/Booking Product Strategy.md            # ingestion/coverage context
source_of_truth_for:
  - trip-artifact-vision
  - trip-record-contract-direction
  - artifact-generation-architecture-rules
  - post-trip-generator-consolidation-frame
---

# Trip Artifacts — vision

> ⚠️ **AMENDED 2026-07-28 by
> [`trip-record-adjudication-2026-07-28.md`](trip-record-adjudication-2026-07-28.md).**
> That doc is the verified ruling layer; where the two disagree, **it
> wins.** Three corrections in particular: (C1) **AD2 is reversed** —
> Trip Story is live in prod, per-member, and becomes THE trip artifact;
> Unpacked is a different scope (the Year), not a competitor. (C2) the
> Postcard img2img render is **real, tested code two config values from
> live**, not a design. (C3) the public share-to-a-non-user path
> **already exists twice** and is dark by one flag. The artifact family
> below is superseded by the adjudication's "one artifact per scope;
> everything else is a section" ruling.

> **Thesis: record over renderings.** The durable asset is a canonical
> per-member record of what actually happened on a trip — who was there,
> what the group chose (and almost chose), who did what, what it cost,
> where. Every visible artifact is a disposable *view* of that record.
> Views get regenerated as models improve; the record compounds forever.
>
> Corollary: we do not compete on generation quality. Google Photos /
> Gemini will auto-build trip recaps from photos+email for free. What
> they structurally cannot have: the **cross-person record** (attendance,
> decisions, credits, money), the **counterfactuals** (what the group
> rejected), and **our taste** (riso + type canon + Vesper's voice).
> Interestingness comes from the data; beauty comes from the design
> system; the model only selects, sequences, and writes captions.

## Why this exists (strategy context, one paragraph)

The venture gate is joiner→organizer conversion. A joiner converts when
they leave a trip *owning something* — today they own nothing (M4 gap:
Atlas is demoted off the tab bar into You, `atlas_learning_enabled`
defaults false, and personal memory only accrues from a member's own
actions, so a low-signal joiner ends a trip with an empty Atlas). The
artifact family is the conversion mechanism, the social-distribution
loop (share → web view → claim), and — because artifacts feed context
forward into the next trip — the retention mechanism. It is explicitly
NOT the MVP wedge; it sequences behind the home-surfaces program and
lands with/after the dogfood.

## The fragmentation this consolidates (verified in code 2026-07-28)

~9 mechanisms, 3 product eras, no shared substrate. Each re-derives
"what happened for this person" its own way:

| # | Mechanism | Where | Disposition (proposed, needs founder ruling) |
|---|---|---|---|
| 1 | Trip story | `tasks/trip_story.py` (697 LOC) + narration + backfill loop + subscriber | MERGE-OR-KILL vs Unpacked — two recap objects is one too many |
| 2 | Character read | `tasks/post_trip_character_read.py` + subscriber + loop | MERGE into The Letter (voice POV survives, standalone object dies) |
| 3 | Unpacked | `core/atlas_unpacked_share.py` + seasonal loop + FE `unpacked*.tsx` + public egress | KEEP — graduates to primary recap view |
| 4 | On This Day / anniversary | `core/db/atlas_anniversary.py`, FE strip live, push dark | KEEP — becomes a *re-surfacer of records*, not a generator |
| 5 | Postcard | photos model + content contract + experiments (designed: 10 rules) | KEEP — the atomic unit; build first |
| 6 | Daily reflection | lifespan loop | FOLD into record assembly (its signals feed the record; no separate artifact) |
| 7 | Atlas letter-hero / readings / artifact / whole / compose | `you/atlas/*` (built 06-03) | FREEZE surface; letter-hero substrate is reused by The Letter |
| 8 | Place affinity | `traveler_place_affinity` | KEEP — feeds Companion Ledger + next-trip context |
| 9 | Digest | its own loop | OUT OF SCOPE here (not a trip artifact) |

The adjudication pass (one session) turns this table's "proposed" column
into rulings and writes the Trip Record field contract. That is the
first executable step of this whole area, and it touches no ranker, no
design surface, no new feature.

## The substrate: the Trip Record

One canonical, per-member, per-trip object assembled at
`trip_completion` from truth that already exists:

- **Attendance** — the blocks this member was present for (NEW primitive:
  attendance-based seeding; a member "was there" for confirmed blocks
  regardless of whether they personally acted. Privacy rule: shared facts
  only — *we ate at X Thursday* — never other members' attributed
  signals).
- **Companions** — who, and the cumulative cross-trip tally with each.
- **Decisions** — proposals considered, votes, rejections, the flips
  (the counterfactual record: uniquely ours).
- **Credits** — who organized, who found what, who claimed/booked what
  (booking claim mechanic feeds this), who settled.
- **Money** — settled totals, split shape (tasteful aggregates only).
- **Places** — visited venues/sites, feeding place affinity + Atlas.
- **Media** — the member's photos attached to trip moments.
- **Signals** — the member's own reactions/saves (their private layer).

Renderers may only read the record. If a renderer wants a fact the
record lacks, the record grows a field; the renderer never goes back to
raw tables. (Same consolidation playbook as `call_llm` and the surface
registry.)

## The artifact family — views of the record

Four emotional jobs; each artifact aims at exactly one:

| Artifact | Job | What it is | Why it wins |
|---|---|---|---|
| **The Postcard** | Social currency | One photo → riso → one grounded caption in Vesper's voice. Issued **during** the trip, end of day. | Sharing motivation peaks mid-trip, not after. Daily in-trip return loop + the distribution loop in one object. Design already done (10 rules). |
| **The Credits** | Relationship | Trip ends like a film: *Organized by Sarah · Found the best table: Tom · Settled the ledger: you.* Typography only. | Zero-fabrication-risk (pure record data, no LLM surface). Everyone is named → every member sends it to every member. Data no competitor holds. |
| **The Letter** | Identity | Short post-trip letter *from Vesper* with a POV: what you gravitated to, what changed since last trip. EB Garamond italic (voice canon). | Cheap (text), intimate, reuses letter-hero substrate. Natural carrier of "your Atlas just started" for joiners. |
| **The Almost** | Closure | Decision archaeology: the rejected hotel, the vote that flipped. "You almost stayed in Alfama." | Story structure for free from the counterfactual record. Structurally impossible for photo-roll competitors. |
| **The Map** | Identity | Trip as riso map artifact (route, tables, the long walk). `Mapbox-Riso-Style-Spec.md` exists. | Poster-shaped; accrues to year-map / lifetime-map. |
| **The Companion Ledger** | Relationship | "Your 4th trip with Sarah. 23 shared meals, 3 countries." | The compounding lock-in: the record of *us* exists only here. |
| **The Year, Unpacked** | Identity + social | Annual Wrapped-mechanics compilation. | Nearly free once the record exists (aggregation view); December distribution spike. |
| **The Return** | (comeback) | On This Day / anniversaries as re-renderings of records. | Engine already live; its push path is the first push worth lighting. |

**Build order within the family: Postcard → Credits → Letter.** Everything
else is a later view. Rationale: Postcard = maximum loop per unit effort;
Credits = exercises the full record contract end-to-end with zero
generation risk; Letter = identity + joiner hook on existing substrate.

## Generation architecture — the anti-slop rules

1. **LLM as editor, not artist.** The model selects (which 3 moments of
   40), sequences (the arc), and writes (one caption, not an essay) —
   always grounded in record facts via the facts-only wrapper + content
   contracts. It never invents events and never draws pixels.
2. **Beauty from constraint.** Fixed art-directed templates (riso
   palette, EB Garamond/DM Sans, postcard rules); generated content
   flows *into* them. Taste lives in templates, not prompts — that is
   why quality holds at automation scale.
3. **The voice is the author.** Captions/letters in Vesper's voice via
   the consolidated `call_llm` surface registry. "From your concierge
   who was there," never "generated by AI."
4. **Ride the cost curve; don't race it.** Text + templates now;
   photo-stylization upgrades as image models improve; video ONLY when
   it is a commodity API call — and then it's just a new renderer over
   the same records, not new plumbing.
5. **Provenance is a feature.** As generated slop floods feeds,
   verified real experience (real people, real places, together) is the
   scarce good. The deliberately non-photorealistic riso aesthetic is
   the honest signature of that position.

## The comeback system

| Moment | Artifact | Note |
|---|---|---|
| Each trip evening | Postcard | in-trip daily loop; share/acquisition spike |
| Trip end | Credits + Letter | closure + the group re-share |
| Anniversaries | The Return | push currently dark — first push producer worth lighting (quiet-hours-tz + `EXPO_PUSH_ENABLED` verification are prerequisites; see notification-decisioning notes) |
| Companion milestones | Ledger | unpredictable = delightful |
| December | The Year | annual spike |
| Next trip starts | Ledger + Letter feed forward | "last time you three…" — the record becomes *useful* context for the concierge, not just sentiment. This row is the venture-story row: the record is the context asset agents will need. |

## Delivery (IA reality, post-reorg)

- Artifacts are **delivered, not discovered**: stack card in Trips home
  via `concierge_feed` producer (same adjudication as the booking
  coverage board — content in the stack, not a bolt-on surface).
  You→Atlas is the archive you land in *from* an artifact; never the
  front door. No new tab. No Atlas-surface polish.
- Zero-install joiners receive artifacts via share link (web render) —
  the artifact is the account-claim moment ("claim your Atlas").
  `you/atlas/shared-links.tsx` + unpacked public egress are the
  substrate candidates.
- **Seam discipline:** the `concierge_feed` producer touches the file
  the home-surfaces program owns (seam S1/S3). Artifact producers land
  through that stream's rules (golden-fixture test), after its step 5–7
  pivot — never via a second worktree.

## What we are explicitly NOT building

- AI video montages, diffusion "AI art," long-form generated essays.
- Atlas as a polished browse surface (deferred; cold-start/state design
  cost is not wedge work — and artifacts-as-objects have no empty
  states).
- A group mega-recap as the primary artifact (converts nobody; the
  per-member projection is the point; a shared view can come later).
- Any new generator mechanism outside the record→view architecture.

## Open founder decisions

| # | Decision | Default lean |
|---|---|---|
| AD1 | Adjudication table dispositions (the 9 mechanisms above) | as proposed in table |
| AD2 | Trip-story vs Unpacked: which recap object survives | Unpacked survives; story's narration/backfill machinery is salvage |
| AD3 | Postcard cadence: daily-evening push vs on-demand only | in-app evening card for dogfood; push later |
| AD4 | Attendance-seeding privacy line (shared facts only — ratify) | ratify as stated |
| AD5 | The Return's push: light anniversary push before or after dogfood | after dogfood starts, before it ends |
| AD6 | Web artifact render for zero-install joiners: in dogfood scope? | out of dogfood v1; in before any external cohort |

## Sequencing (defers to home-surfaces program)

1. **Now (no conflicts):** adjudication pass → rulings on AD1/AD2 +
   Trip Record field contract written against real tables. One session.
2. **Backend, stream-safe:** attendance-based seeding + record assembly
   at `trip_completion` (no ranker contact).
3. **First renderers:** Postcard (in-trip), Credits (trip end) — FE
   objects + web render, design-system only.
4. **Stack delivery:** artifact producer into `concierge_feed` — through
   the home-surfaces stream after its pivot clears.
5. **The Letter + Return re-pointing + Ledger** — post-dogfood, informed
   by which artifacts dogfooders actually share.

The dogfood is the validation: a real trip should end with every member
— including the quietest joiner — receiving something they keep.
