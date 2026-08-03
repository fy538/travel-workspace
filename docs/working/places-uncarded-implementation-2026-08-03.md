---
doc_type: working
status: active
owner: founder / frontend
created: 2026-08-03
expires: 2026-09-02
why_new: The Places feed's uncarded direction was designed across four canvases in one session and the implementation path was never written down; this grounds it in the actual code and corrects the gating assumption every board repeated.
promotes_to:
  - travel-app/docs/surfaces/places-workspace/contract.md
supersedes: []
depends_on:
  - docs/working/places-section-contract-2026-08-01.md
source_of_truth_for:
  - places-uncarded-implementation-plan
---

# Places — uncarding the feed · implementation plan

**2026-08-03.** The design is settled across four canvases in Claude Design
project `551f400f`:

| Canvas | What it settles |
|---|---|
| `PLACES - THE UNCARDED CANDIDATE` | the direction, and what the surface was doing |
| `PLACES - UNCARDED, EVERY KIND` | all nine kinds + the two exceptions |
| `PLACES - THE VERB AS A CONTROL` | the verb becomes an outlined gold pill |
| `PLACES.html` §12 | the flush plate this replaces |

This doc is the code path. **Nothing here is built.**

---

## 0 · The headline: the gate is much smaller than the boards say

Every canvas says the illustration resolver blocks this, and describes it as
"a gelateria and a museum get the same picture." I traced it. The claim is
**directionally right and materially overstated**, and the fix is far smaller
than a photo pipeline.

`utils/entityImage.ts:59` `resolveEntityImage` resolves in three tiers:

```
tier 1   realUrl                       — a real photo, wins over everything
tier 2   bundled place riso by citySlug — WINS OVER TIER 3
tier 3   category art by imageClass
```

`imageClassForVenueType` (`utils/entityImage.ts:85`) **does** distinguish
gelateria → `cafe` from museum → `cultural`. Category art exists and is
correct. It simply never renders for a place in a bundled city, because
`placeCardIllustration` (`components/places/PlacesSectionFeed.tsx:178`) passes
`citySlug={placeSlugFromDestination(place.locality ?? scopeLabel)}` and tier 2
short-circuits tier 3.

**Corrections to the boards:**

- Not "the same picture." `placeVariantSeeded` (`utils/placeIllustration.ts:83`)
  hashes the id into one of **four** mood variants (`day`/`fun`/`nature`/`night`).
  So a gelateria and a museum in Rome get one of four generic *Rome* images —
  unrelated to what the venue is, but not identical. The real defect is
  **irrelevance, not repetition**.
- ~44 cities are bundled (`constants/placeIllustrations.ts`, 264 requires ÷ 6
  variants). Inside them tier 2 always wins; outside them tier 3 already works.
- **This is a precedence decision, not missing infrastructure.** It is roughly
  a one-line change plus a product call.

**The product call is genuinely open** and should be made explicitly rather
than by editing the line: is a generic Rome riso better or worse than a generic
cafe illustration, for a card whose job is "this specific place"? My read is
that category art is better *for the uncarded design specifically*, because
once the surface is gone the image is the only thing distinguishing one row
from another — four Rome images across a six-row feed will read as noise. But
that is a call, and swapping precedence globally also changes Trips and Atlas.

**Recommended scope:** do not flip the global tier order. Add an opt-out so the
Places *feed* prefers category art, and leave hero/editorial surfaces on the
city riso where a mood image is the right thing.

---

## 1 · The architectural lever already exists

`constants/cardSurface.ts` is a semantic recipe registry:

```ts
cardSurfaceRecipe: Record<CardSurfaceRecipe, { material, density, radius }>
```

Eight feed components each wrap in `<CardSurface recipe="…">`. `FeedCardView`
(`PlacesSectionFeed.tsx:392`) dispatches to them by payload:

```
card.place      → PlaceFeedCard
card.city       → CityFeedCard
card.angle      → AngleFeedCard
card.experience → ExperienceFeedCard
card.area       → AreaFeedCard
card.memory     → MemoryFeedCard
card.friend     → FriendFeedCard
else            → NoticeOrPromptCard
```

**So uncarding is a material + recipe addition, not eight component rewrites.**
Every material in the registry currently sets `backgroundColor` + `borderWidth`;
there is no "no surface" material. That is the gap to fill.

---

## 2 · Phases

### Phase 0 — merge what is already done  *(blocking, mechanical)*

`places/card-plate-and-rail` (`d6969790`) is **unmerged and behind main**. It
moved the candidate foot inside the copy column so the plate reaches the card's
bottom edge, and freed the experience rail from the page gutter. The uncarded
work builds directly on that geometry. Rebase onto main and land it first, or
every phase below conflicts with it.

⚠️ Another session was last seen on `codex/places-state-consolidation`. Check
`git worktree list` before starting.

### Phase 1 — the surface primitive  *(S · one file + one enum)*

`constants/cardSurface.ts`:

- add `'none'` to `CardSurfaceMaterial`; style is `{}` — no background, no
  border, no shadow.
- add `'uncarded'` to `CardSurfaceRecipe`:
  `{ material: 'none', density: 'none', radius: 'card' }`.
  Radius is retained deliberately: the plate inside still rounds, and a future
  reversal should not have to reintroduce the axis.

Nothing changes visually yet. This phase is separately reviewable.

### Phase 2 — the separator moves from the card to the stack  *(S)*

Today `styles.cards` is `{ gap: placesCandidateGeometry.stackGap }` (10) and
each card's own border ends it. Uncarded, the stack draws a hairline between
children instead.

`PlacesSectionFeed.tsx:1514` and `treatmentStyle` (`:386`). Prefer wrapping
each non-first child in a row view carrying `borderTopWidth` over
`gap` + `:not(:first-child)` tricks — RN has no sibling selectors and the
wrapper is also where the 10-top/15-bottom padding lives.

**Row padding is asymmetric on purpose**: the hairline sits *above* each row,
so the top already has a visual stop and the bottom does not — and a bordered
control needs more clearance from the next rule than a text baseline did.

### Phase 3 — the verb becomes a control  *(S)*

Today `CardAction` renders a bare gold text label. It becomes an outlined pill:
`padding 7×12`, `borderRadius 999`, `0.5px` border **in the action colour**.

The gold border is load-bearing. A neutral-hairline variant was drawn and
rendered as a *tag* — at a glance closer to a disabled state than to the primary
action. Do not "quieten" this; quiet is the one thing it cannot be, since the
whole reason it exists is that the bare label did not look pressable.

⚠️ **The pill measures ~30pt — under the 44pt tap minimum.** It needs
`hitSlop`. Do **not** pad it to 44; that makes it the heaviest object on the row
and reproduces the filled variant the design rejected. `places-blocks.jsx`
already carries the identical debt against Prompt's chips.

### Phase 4 — per-kind geometry  *(M · the bulk of the work)*

`components/places/cardGeometry.ts`:

```
plate            88 → 78     (notice 62, prompt 68)
copy inset       0  → 5 top / 12 bottom
title → foot gap 10 → 6
row pitch        114 → 104   (measured)
```

The inset is the subtle one and it is **one idea, not two**: the text block sits
*optically inside* the plate's height rather than flush to it — title starting
~5pt below the plate top, last line ~5.5pt above its bottom. Flush read as two
rectangles of equal weight. Put it on the copy column so every kind inherits it,
not as per-node nudges.

An earlier value of 8 for the bottom inset measured **1.5pt** of clearance —
arithmetically correct, visually nothing. 12 is the smallest that reads. It
costs no pitch, because the plate governs row height.

### Phase 5 — two layouts, and the two exceptions  *(S)*

**Two layouts, chosen by content height — this is the one that bit:**

- copy **taller** than plate → verb bottom-aligned (`marginTop:auto`). Place,
  Memory, Conviction.
- copy **shorter** than plate → verb **inline and vertically centred**. Notice,
  Friend. Bottom-aligning here strands the pill in dead air; the notice shipped
  on the board that way and looked broken.

**Exception 1 — Notice keeps a tint.** Its job is to *interrupt*, and a hairline
is the same mark that separates two ordinary rows. Uncarding it deletes the only
device it has. Keep the oxblood wash + ox rule; drop the border and radius.

**Exception 2 — the rail keeps spacing.** A rule between items is a
vertical-stack device; the experience rail is horizontal, so hairlines are not
available there. This is geometry, not preference, and it is the one place the
instruction cannot be followed literally.

### Phase 6 — ratchets  *(S, and overdue)*

**No test in `__tests__/components/places/` currently asserts a recipe, a
border, or a background.** The surface change is therefore low-risk to break
and completely unguarded. Add:

- the feed's stacked kinds use `recipe="uncarded"` (catches a silent revert)
- the separator hairline exists between rows and **not** above the first
- the verb has a border in the action colour (catches the neutral-tag drift)
- plate is 78 and the copy inset is 5/12
- Notice still has its tint (catches over-application of the rule)

Ablate each one. Three of the four canvases changed a conclusion after a
measurement contradicted a written claim; assertions that never fail are the
main way that happens.

### Phase 7 — amend rule 10  *(XS, docs only)*

Rule 10 currently reads "everything in the feed is a card; rows live only behind
a door and in search." Uncarded items keep picture, name, reason and verb — they
are not rows in the sense the rule forbids — but the wording no longer matches
the surface. **Amend it deliberately, as a decision, not as a side effect.**

This also touches the founder's own earlier call that lists should be rare and
"even three items can still be a card." Worth explicit re-confirmation rather
than assuming the uncarded object satisfies it.

---

## 3 · What this plan does NOT propose

- **Uncarding only the candidates.** The feed mixes nine kinds; uncarding one
  runs two materials at once with no rule a reader can find. It is all or none.
- **A chevron** to solve pressability. That trades a surface for different
  chrome and wins nothing.
- **Flipping the global illustration tier order.** Places' feed is not the only
  consumer.
- **Touching the object/venue page.** Separate call, separate canvas.

## 4 · Sequencing risk

Phases 1–5 all touch `components/places/PlacesSectionFeed.tsx` (1813 lines and
growing — it is over the 800-line lint budget already and warns on every run).
Two other sessions have edited it today. Land Phase 0 first, then keep phases
small and sequential rather than parallel; this file does not tolerate
concurrent branches well.
