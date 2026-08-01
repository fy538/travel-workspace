# Places sectioned feed — implementation handoff

**2026-08-01.** Written to be handed to an agent with no prior context. Read
§0 → §1 → §6 before writing any code; §6 contains one question that changes
the contract and must be answered by the founder first.

**Deliverable:** turn the Places root from a fixed-slot projection into a
posture-driven sectioned feed, per the design board.

---

## 0 · Start here

**You do not need the Claude Design MCP tool.** The design is exported to disk.

| What | Path |
|---|---|
| The board (open in a browser) | `/Users/feihuyan/Downloads/vesper 405/project/PLACES.html` |
| **The spec, as code comments** | `/Users/feihuyan/Downloads/vesper 405/project/places-system.jsx` |
| Prior canon (superseded, read for contrast) | `.../vesper 405/project/PLACES - CORE.html` |

`places-system.jsx` is the real source of truth. It is one self-contained
file — tokens, every component, and long comment blocks that state each rule
and *why* it was chosen. Read the header comment and the `LayoutRules`
function first; between them they contain the whole design grammar.

> ⚠️ `vesper 405` is a **snapshot taken 2026-08-01 16:39.** Before starting,
> run `ls -dt ~/Downloads/vesper\ * | head -3`. If a higher-numbered folder
> exists, use it — the founder re-exports on every design change.

Rules referenced throughout this doc as "rule NN" are the ten in
`LayoutRules`. The four that constrain the contract:

- **Rule 03** — one conviction (full-bleed card) per screen.
- **Rule 09** — an empty section does not render. No divider, no label, no
  "nothing to fill" message. Ever.
- **Rule 10** — everything in the feed is a card. A section holds ≤ 4. If more
  qualify, it shows 3 and the *count becomes a door* to a list screen. Rows
  live only behind that door and in search.
- **Rule 05** — mono is machine facts only (times, counts, distances); labels
  and names are sans caps.

---

## 1 · The code as it exists today

All paths relative to `~/travel-workspace/`.

### Backend (`travel-agent/`)

| Thing | Where |
|---|---|
| Contract models | `backend/core/models/places_projection.py` |
| Scope/anchor/context models | `backend/core/models/places_context.py` |
| Projection builder | `backend/places/projection.py` (265 lines) |
| Routes | `backend/api/routes/places.py` — `GET /api/places` → `PlacesProjection` |
| Auth | `Depends(get_current_user)` → `actor.id` |
| Tests | `tests/places/test_projection.py` and siblings |
| Module doc (**must update**) | `backend/places/FEATURE.md` |
| Feature flags | `backend/core/feature_flags.py` — `_truthy("NAME")`, default OFF |
| Posture (already shipping) | `backend/home/trips_stack.py:27` — `TripsHomePosture` is a `Literal` |
| Card precedent | `backend/home/concierge_feed/models.py:689` — `ConciergeHomeCard` |
| Cross-card arbitration | `backend/home/concierge_feed/ranking.py` (876 lines) |
| Anniversary query (**already exists**) | `backend/core/db/atlas_anniversary.py:34` — `list_on_this_day(user_id, today, limit=3) -> list[OnThisDayRow]` |

`OnThisDayRow` = `source_type ("artifact"\|"trip") · source_id · title ·
place_label · occurred_on · years_ago`.

### Frontend (`travel-app/`)

| Thing | Where |
|---|---|
| Screen | `components/places/PlacesWorkspace.tsx` |
| **Assembler** | `components/places/core/PlacesCore.tsx:55` — `CoreSurface` |
| Atoms / depth | `components/places/core/PlacesAtoms.tsx`, `PlacesDepth.tsx` |
| Canon↔code map (**will go stale**) | `components/places/core/CORRESPONDENCE.md` |
| Fetch | `utils/api/http.ts:1101` — `/api/places` |
| Generated types | `utils/api/schema.gen.ts` |
| Tests | `__tests__/components/places/PlacesCore.test.tsx` |

### The current payload shape

```python
class PlacesProjection(BaseModel):
    section_order: list[PlacesSectionKind]   # CONTEXT MAP HIGHLIGHT PLACES
                                             # EXPERIENCES READING AREAS
    context:     PlacesContext
    map:         PlacesMapSummary | None
    highlight:   PlacesGuidePreview | None
    places:      PlacesRankedPage
    experiences: list[PlacesExperiencePreview]
    reading:     PlacesReadingDoor | None
    areas:       list[PlacesAreaPreview]
```

**Two facts that decide the whole approach:**

**(a) It is fixed-slot.** Each slot is a *named field with its own type*.
Adding a section means adding a field. The shape cannot express "three of
these, then two of those, then one of something else."

**(b) The taxonomies are orthogonal.** `PlacesSectionKind` answers *what type
of content is this* (places, reading, areas). The board's section answers *why
is this on my screen right now* (`AFTERNOON · 4 HRS FREE`, `WITHIN TEN
MINUTES · THREE`, `A YEAR AGO TODAY`). `WITHIN TEN MINUTES` is not a new
`PlacesSectionKind`; it is a **reason** that happens to contain items of kind
`places`. So this is a new model, not two more enum members.

### 🔴 The live bug you are inheriting

**`PlacesProjection.section_order` is dead code.** It is in the contract, the
generated schema, the mocks and the tests — and **no client reads it.**
`CoreSurface` hardcodes the slot sequence in JSX. The contract says the server
owns the order; the code says the client does; nothing detects the
disagreement.

Verify yourself:
```bash
cd ~/travel-workspace/travel-app
grep -rn "section_order" --include="*.ts" --include="*.tsx" . | grep -v node_modules
# → only schema.gen.ts, a mock, and a test fixture. No component.
```

This is the exact failure Decision 2 (§5) exists to prevent recurring.

---

## 2 · Corrections to the design board

The board was drawn before anyone read the current contract. Five claims in it
are wrong or stale. **Do not plan against them.** Correcting the board itself
is a separate task — do not do it as part of this work.

| Board claims | Reality |
|---|---|
| `returned` posture blocked on **been / loved ✗** | **`loved` ships.** `PlacesRelationshipTruth.loved`, produced at `backend/places/projection.py:100`. |
| The `Prompt` block is "the only producer `been` and `loved` could ever get" | Wrong for `loved`. |
| `been` is a missing field to build | **`been` was deliberately CUT.** `PlacesRelationshipTruth` docstring: *"Grounded five-marker contract after the unowned Been marker was cut."* Re-adding it is a product reversal — escalate, do not just build it. |
| Search grouping needs `entity_type` + dossiers in the index | Also needs a new response type. `PlacesSearchResponse.items` is `list[PlacesRankedItem]` — homogeneous, and structurally cannot carry a dossier or an area. Not a group-by over the current payload. **Out of scope for this handoff.** |
| Sites work sits on two unmerged branches | **Both halves are merged to `main`.** Backend: `ebe8b753 merge: land Places site collision guards`. Frontend: `615f7cdd` is an ancestor of `main`, and `entity_type` is on `PlacesRankedItem` in `utils/api/schema.gen.ts`. Nothing to merge. |

---

## 3 · Decision 1 — the section contract

New module: `travel-agent/backend/core/models/places_sections.py`. **Purely
additive.** Nothing here changes any existing field on `PlacesProjection`.

```python
"""Contract for the posture-driven sectioned Places feed.

Design source: `PLACES.html` / `places-system.jsx`, Claude Design project
551f400f (exported to ~/Downloads/vesper 405/project/). Rule numbers in this
module refer to that board's `LayoutRules`.
"""

from __future__ import annotations

from datetime import date
from enum import StrEnum
from typing import Literal
from uuid import UUID

from pydantic import BaseModel, Field, model_validator

from backend.core.models.places_context import PlacesContext
from backend.core.models.places_projection import (
    PlacesRankedItem,
    PlacesReadingItem,
    PlacesStarterCity,
)
from backend.home.trips_stack import TripsHomePosture


class PlacesSectionReason(StrEnum):
    """WHY this section is on the page.

    Orthogonal to PlacesSectionKind, which says what TYPE of content a
    fixed slot holds. Both may coexist during the migration.
    """

    # The spine — a hole in the plan. Gated by rule 08 (claim a gap only
    # when the plan is legible AND complete).
    GAP              = "gap"               # AFTERNOON · 4 HRS FREE
    EXPIRY           = "expiry"            # BOOK NOW OR LOSE IT
    GROUP_WAITING    = "group_waiting"     # four people, nobody has picked

    # The floor — true regardless of the plan. Board §8.
    NEARBY_SET       = "nearby_set"        # WITHIN TEN MINUTES · THREE
    NEIGHBOURHOOD    = "neighbourhood"     # CARROLL GARDENS · TWO WAYS
    ANNIVERSARY      = "anniversary"       # A YEAR AGO TODAY
    UNFINISHED_GUIDE = "unfinished_guide"  # 4 LEFT
    FRIEND_ACTIVITY  = "friend_activity"   # MAYA HAS BEEN SAVING
    SAVED_UNVISITED  = "saved_unvisited"   # YOUR SATURDAY
    CHANGED          = "changed"           # CLOSED PERMANENTLY
    HARVEST          = "harvest"           # HOW WAS IT
    STARTER          = "starter"           # THREE TO START WITH


class PlacesSectionTreatment(StrEnum):
    """How the section renders. SERVER-OWNED — see Decision 2."""

    CONVICTION = "conviction"   # exactly 1 place, full-bleed image
    FORK       = "fork"         # exactly 2 angles, side by side
    CHOICE     = "choice"       # 2-4 cards
    ROWS       = "rows"         # behind a door, or search. NEVER in the feed.


class PlacesCardKind(StrEnum):
    PLACE  = "place"    # -> ConvictionCard | Candidate | PlaceRow
    ANGLE  = "angle"    # -> AngleCard (a dossier)
    FRIEND = "friend"   # -> FriendStrip
    MEMORY = "memory"   # -> MemoryCard (a past trip)
    NOTICE = "notice"   # -> NoticeRow
    PROMPT = "prompt"   # -> Prompt
    CITY   = "city"     # -> DestCard


class PlacesCardVerb(StrEnum):
    """The foot-bar verb. This is the reason a card is not a row (rule 10)."""

    ADD_TO_DAY = "add_to_day"   # the spine — an hour you have
    SAVE       = "save"         # the floor — an hour you do not have yet
    BOOK       = "book"
    OPEN       = "open"
    ANSWER     = "answer"       # harvest
    CLEAR      = "clear"        # notice


class PlacesFriendActivity(BaseModel):
    """NEW. Who, and what they saved."""

    user_id: UUID
    display_name: str = Field(min_length=1)
    initial: str = Field(min_length=1, max_length=2)
    sentence: str                       # "saved five places in Tokyo this month"
    place_names: list[str] = Field(max_length=6)


class PlacesMemoryRef(BaseModel):
    """NEW. A past trip, one line. Maps 1:1 from OnThisDayRow."""

    source_type: Literal["artifact", "trip"]
    source_id: str
    occurred_on: date
    years_ago: int = Field(ge=1)
    place_label: str | None = None


class PlacesSectionDoor(BaseModel):
    """More than four qualified. Rule 10: the count is the way in.

    Prior art: PlacesReadingDoor (places_projection.py:192) already does
    exactly this for reading — same idea, narrower type.
    """

    total: int = Field(ge=5)
    target: Literal["saved", "reading", "nearby", "guide"]
    scope_label: str


class PlacesCard(BaseModel):
    """One wide model with optional fields, discriminated by `kind`.

    DELIBERATELY not a tagged union. ConciergeHomeCard
    (backend/home/concierge_feed/models.py:689) is the shipping precedent and
    uses exactly this shape; matching it keeps ONE card mental model across
    Vesper Home and Places. Type purity loses to that.
    """

    id: str = Field(min_length=1)
    kind: PlacesCardKind

    # Content slots. Which are populated depends on `kind`.
    title: str = Field(min_length=1)
    meta: str | None = None      # sans caption under the title
    kicker: str | None = None    # mono stamp — MACHINE FACTS ONLY (rule 05)
    reason: str | None = None    # serif. Vesper's judgment. CONVICTION only.
    fact: str | None = None      # mono, right-aligned. ROWS only.

    verb: PlacesCardVerb | None = None

    # Payload by kind — exactly one is set. The first three already exist in
    # places_projection.py and are reused as-is; the last two are new above.
    place:  PlacesRankedItem   | None = None
    angle:  PlacesReadingItem  | None = None
    city:   PlacesStarterCity  | None = None
    friend: PlacesFriendActivity | None = None
    memory: PlacesMemoryRef      | None = None

    priority: int


class PlacesSection(BaseModel):
    reason: PlacesSectionReason
    label: str                        # marker label — SANS CAPS (rule 05)
    count: str | None = None          # marker count — MONO. "THREE", "4 LEFT"
    note: str | None = None           # serif italic thesis
    treatment: PlacesSectionTreatment
    door: PlacesSectionDoor | None = None
    cards: list[PlacesCard]
    priority: int                     # board §5 ladder

    @model_validator(mode="after")
    def _cardinality_matches_treatment(self) -> PlacesSection:
        n = len(self.cards)
        if n == 0:
            raise ValueError("rule 09: an empty section does not render")
        if self.treatment is PlacesSectionTreatment.CONVICTION and n != 1:
            raise ValueError("rule 10: a conviction is exactly one card")
        if self.treatment is PlacesSectionTreatment.FORK and n != 2:
            raise ValueError("rule 10: a fork is exactly two")
        if self.treatment is PlacesSectionTreatment.CHOICE and not 2 <= n <= 4:
            raise ValueError("rule 10: a choice set is 2-4 cards")
        if self.treatment is PlacesSectionTreatment.ROWS:
            raise ValueError("rule 10: rows never appear in the feed")
        if self.door is not None and n > 3:
            raise ValueError("rule 10: >4 qualified means 3 cards and a door")
        return self


class PlacesFeed(BaseModel):
    """The sectioned Places page. THE LIST IS THE ORDER."""

    posture: TripsHomePosture
    context: PlacesContext
    sections: list[PlacesSection] = Field(max_length=4)   # board §5 ceiling

    @model_validator(mode="after")
    def _one_conviction_per_page(self) -> PlacesFeed:
        # Rule 03. Enforceable ONLY here — no single section can see the page.
        n = sum(s.treatment is PlacesSectionTreatment.CONVICTION
                for s in self.sections)
        if n > 1:
            raise ValueError("rule 03: one conviction per screen")
        return self
```

### Three deliberate choices

**The list is the order.** No parallel `section_order` array. The existing one
is dead (§1) and a second ordering that can disagree with the payload is a bug
generator.

**One wide card, not a tagged union.** Matches `ConciergeHomeCard`.

**Every checkable rule is a validator.** Rules 03, 09, 10 fail at the model
boundary, so a producer that breaks the design grammar cannot render wrong.

---

## 4 · Decision 2 — the server owns `treatment`

**The server sends `treatment`. The client renders what it is told. It may
DEGRADE (conviction → choice) for viewport or a failed image. It may never
PROMOTE.**

Three reasons, heaviest first:

1. **Rule 03 is a cross-section constraint.** "One conviction per screen"
   cannot be evaluated by any single section. Only the assembler that sees the
   whole page can enforce it — and that assembler already exists server-side
   (`concierge_feed/ranking.py`, arbitrating against a 31-value priority
   ladder).
2. **`len(cards)` cannot distinguish conviction from attrition.** One card
   because Vesper is sure, and one card because two got filtered out, are the
   same length and opposite claims. Deriving treatment from cardinality
   silently turns every thin section into the loudest thing the page can say.
   That is the exact failure the ladder exists to prevent.
3. **Precedent.** `ConciergeHomeCard.family`/`.variant` are already
   server-sent for this reason, and the six-family taxonomy is canon
   (`Vesper Cards.html`, 2026-07-09). A client-derived treatment system would
   be the third card taxonomy in the codebase.

**Accepted cost:** a treatment change needs a backend deploy.

**Required regression test (Step 3):** the `section_order` failure is
invisible only because nothing asserts on it. Add a test that renders each
posture's payload through the real client assembler and asserts the rendered
treatment matches the server's, so the same drift cannot recur silently.

---

## 5 · Process hazards — read before touching a repo

**⚠️ Concurrent sessions are active in both repos.** As of writing:

```
travel-agent   main                              (dirty working tree)
travel-app     codex/map-platform-consolidation  (dirty working tree)
               + 2 other worktrees
```

- **Never `git checkout`, `git stash`, or `git checkout -- <file>`** in these
  trees. Another agent's uncommitted work is there.
- **Work in a git worktree:**
  ```bash
  cd ~/travel-workspace/travel-agent
  git worktree add ../agent-places-feed -b places/sections-feed main
  cd ../agent-places-feed && ln -s ../travel-agent/.venv .venv
  ```
  (Frontend: symlink `node_modules` the same way.)
- **Commit with explicit pathspecs**, never `git commit -a`.

**Hooks that will block you** (`travel-agent/.pre-commit-config.yaml`):

| Stage | Hook | What to do |
|---|---|---|
| commit | ruff, size budgets, broad-exception ratchet, import boundaries | Keep new files small; add zero bare `except` |
| **pre-push** | `check-openapi-snapshot` | Any model change requires regenerating `docs/openapi.json`. Run `make sync-types` (needs backend running) or `make sync-types-snapshot` |
| pre-push | docs headers + freshness | **Update `backend/places/FEATURE.md`** — it has a required header block with `Last updated:` |

Two ratchets (broad-exceptions count, `producers.py` size budget) were
**already failing on main** as of 2026-07-31 for reasons unrelated to this
work. If one fires and you can prove your diff does not touch it, commit with
`--no-verify` **and say so in the commit message.**

**Commands:**
```bash
# backend tests
cd <worktree> && .venv/bin/python -m pytest tests/places -q
# frontend
cd ~/travel-workspace/travel-app && npm test
cd ~/travel-workspace && make typecheck
```

---

## 6 · 🔴 BLOCKING: answer this before Step 3

**Board §9 question 07 — does a section's door open a list of rows, or a
scrolled feed of cards?**

The contract above assumes **rows**: `PlacesSectionTreatment.ROWS` and
`PlacesCard.fact` exist only to serve that answer.

If the answer is **cards**, both are deleted, and `PlaceRow` leaves the
component system entirely — `components/places/core/PlacesCore.tsx` loses a
component and `CORRESPONDENCE.md` loses a row.

**This is the only open question that changes the contract.** Ask the founder.
The other six open questions in board §9 do not touch this work.

---

## 7 · Implementation sequence

Each step is one commit unless noted. Do not batch.

### Step 0 — confirm your starting point  *(5 minutes, do not skip)*

The sites work (venues + museums/monuments in one projection) is **already
merged on both sides**. Confirm before you branch:

```bash
cd ~/travel-workspace/travel-agent && git log --oneline -1 --grep="site collision"
cd ~/travel-workspace/travel-app  && git merge-base --is-ancestor 615f7cdd main && echo "FE sites merged"
```

Both should succeed. If either does not, stop and ask — the tree has moved
since this doc was written.

Then cut your worktrees per §5. Do not work in the shared trees.

### Step 1 — the contract module  *(no producers, no client)*

**Write:** `backend/core/models/places_sections.py` exactly as §3.

**Test:** `tests/places/test_sections_contract.py`. One test per validator,
each asserting the *failure*:

- `CONVICTION` with 2 cards raises
- `FORK` with 1 or 3 raises
- `CHOICE` with 1 or 5 raises
- `ROWS` anywhere in a feed raises
- 0 cards raises (rule 09)
- `door` set with 4 cards raises
- `PlacesFeed` with 2 conviction sections raises (rule 03)
- `PlacesFeed` with 5 sections raises (§5 ceiling)

**Done when:** `pytest tests/places/test_sections_contract.py` is green and
every validator has a test that fails without it. Ablate each validator and
confirm its test goes red — do not skip this.

**Not yet wired to any route.** Nothing imports this module yet.

### Step 2 — the route, dark

**Write:**
- `backend/core/feature_flags.py` → `places_sections_enabled()` reading
  `PLACES_SECTIONS_ENABLED`, default OFF.
- `backend/api/routes/places.py` → `GET /api/places/feed` returning
  `PlacesFeed`, `Depends(get_current_user)`, 404 when the flag is off.
- `backend/places/sections.py` → `build_places_feed(user_id) -> PlacesFeed`
  returning `sections=[]` for now.

**Careful:** `PlacesFeed(sections=[])` is legal (the ceiling is a max, not a
min) but renders nothing. That is correct per rule 09.

**Then:** regenerate the OpenAPI snapshot or pre-push will block you.

**Done when:** route returns 404 with the flag unset, and an empty feed with
`PLACES_SECTIONS_ENABLED=1`.

### Step 3 — one producer: `ANNIVERSARY`

The cheapest possible end-to-end exercise: one section, one card, one query
that **already exists**.

**Write:** `backend/places/producers/anniversary.py`

```python
def build_anniversary_section(user_id: UUID, today: date) -> PlacesSection | None:
    rows = list_on_this_day(user_id, today, limit=3)   # already exists
    if not rows:
        return None            # rule 09 — no section, not an empty one
    ...
```

Mapping `OnThisDayRow` → `PlacesCard`:

| Row field | Card field |
|---|---|
| `title` | `title` |
| `place_label` | `meta` |
| `years_ago` | `kicker` — e.g. `"THIS WEEK LAST YEAR · 6 DAYS"` (mono, rule 05) |
| `source_type`, `source_id`, `occurred_on`, `years_ago`, `place_label` | `memory` (`PlacesMemoryRef`) |
| — | `kind=MEMORY`, `verb=OPEN` |

Section: `reason=ANNIVERSARY`, `label="A YEAR AGO TODAY"`,
`count=<place label or city>`, `treatment=CHOICE` if 2–3 rows.

**One row is the interesting case.** A single memory card is *not* a
`CONVICTION` — conviction is reserved for a place you can act on, and rule 03
budgets one per page. Use `CHOICE` with one card, or extend the validator to
allow it. **Decide explicitly and write the reason in a comment** — this is
the first real test of Decision 2's logic.

**Test:** `tests/places/test_sections_anniversary.py` — zero rows → `None`
(not an empty section); one row → valid section; three rows → three cards.

**Done when:** `GET /api/places/feed` with the flag on returns a real
anniversary section for a seeded user.

### Step 4 — the client render path

**Write:**
- `make sync-types` (or `--from-snapshot`) → `PlacesFeed` lands in
  `utils/api/schema.gen.ts`.
- `utils/api/http.ts` → `getPlacesFeed()` alongside the existing `/api/places`.
- `components/places/core/PlacesFeed.tsx` — a **new** assembler that maps
  `treatment` → component:

  | treatment | component |
  |---|---|
  | `conviction` | new `ConvictionCard` |
  | `fork` | new `Fork` / `AngleCard` |
  | `choice` | new `Candidate` |
  | `rows` | existing `PlaceRow` — **must never appear in the feed** |

  Port these from `places-system.jsx`. The JSX there is web React with inline
  styles; translate to React Native + `constants/textVariants.ts`. **Do not
  re-derive the type scale** — the board transcribed it from
  `textVariants.ts`, so map back to the same variants.

- `PlacesWorkspace.tsx` — render `PlacesFeed` when the flag is on and the
  payload is non-empty; otherwise fall back to `CoreSurface` unchanged.

**Test:** `__tests__/components/places/PlacesFeed.test.tsx` — **the Decision 2
regression test.** For each treatment, assert the rendered component matches
the server's `treatment` field. Assert the client never promotes.

**Done when:** both paths render, the flag switches between them, and
`npm test` + `make typecheck` are green.

### Step 5 — the rest of the floor

In order: `NEARBY_SET` → `NEIGHBOURHOOD` → `UNFINISHED_GUIDE` →
`FRIEND_ACTIVITY`.

**🔴 `NEARBY_SET` is blocked on a data bug.** ~52% of verified venues and sites
sit exactly on their city centroid, which is why rows read "0 m away".
`NEARBY_SET` is *entirely* distance claims — shipping it now means shipping
"4 MIN ON FOOT" as a lie.

Reproduce before building it (dev Postgres, `localhost:15432`, throwaway
`localdev` credentials — **never prod**): compare `venues.location` against
the centroid of its `places` row and count exact matches. Fix or exclude
centroid-coincident rows before this section renders a distance.

The other three floor sections do not depend on distance and are not blocked.

### Step 6 — deletion trigger  *(stated now so it is not forgotten)*

When `PlacesFeed` covers `starter`, `quiet` and the floor: delete the fixed
slots and `section_order` from `PlacesProjection`, delete `CoreSurface`, and
update `CORRESPONDENCE.md`. **Two parallel section systems is worse than
either one.** Do not let this linger behind a flag indefinitely.

---

## 8 · Out of scope

- **Search grouping by entity kind.** Needs a heterogeneous response type;
  `PlacesSearchResponse` is a separate contract. Board §7 has the design.
- **Correcting the design board** for the five errors in §2.
- **Reinstating `been`.** It was cut deliberately. Escalate if a section needs
  it — `HARVEST` can only produce `loved` until that is reversed.
- Board §9 questions 01–06.
