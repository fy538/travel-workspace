---
doc_type: decision
status: accepted
owner: founder / product / Life / social design
created: 2026-09-29
decided: 2026-09-29
last_verified: 2026-09-29
why_new: On September 29 the founder accepted six recommendations from the Life design investigation. They settle how things and collections relate, how Life opens, and how shared collections behave, before the Life boards are reorganized and redrawn. They existed only in conversation.
supersedes: []
source_of_truth_for:
  - life-occasion-versus-span
  - life-root-readings
  - shared-collection-viewer-and-leaving
---

# Decision: Occasions are things, spans are collections

## Context

The founder made Life, artifacts, collections and their multiplayer use the
first design priority, and asked for an investigation of the Life Claude Design
project (`e72a2fd2`) before polishing it. The investigation found three design
passes stacked without retirement:

- the September 6 package, with its four lenses, nesting (journey, chapter,
  day, evening) and receipts;
- the September 26–27 catalog and first collections view;
- the September 27–28 collections spine and ingestion boards.

The app on the Codex lane (app `87e39c758`) builds the oldest model: four
lenses including Threads, no collection object, hard delete only, and a fixed
"Just me" audience. No rule said how an evening, a trip and a collection
relate. Nor did any rule say what a member of a shared collection sees on
another member's thing, or what leaving does. The founder accepted the
investigation's recommendations on all six points below.

## Decision

1. **Occasions are things; spans are collections.**
   - A single occasion is one thing that holds its photographs and originals.
     Examples: an evening, a round of golf, a flight, a concert.
   - Anything that spans several occasions is a collection: a trip, a theme,
     a kind, a season.
   - Journey, chapter and day are ways of reading a collection over time, not
     containers. This replaces the September 6 boards' nesting and applies the
     [collections decision](2026-09-28-collections-are-the-spine.md), items 1–2.
2. **Life opens as the whole record, read four ways: Collections, Time, Places
   and People.**
   - Places is the map.
   - The first view follows the contents: Time for someone new, Collections
     once there are some. After that, Life opens where the person last left it.
   - This completes the Threads-to-Collections change (D0 row 10).
3. **The back of a thing is always the viewer's own.**
   - In a shared collection, each member sees facts from their own record on a
     thing's back: their visits, and who was with them.
   - Anything written on a thing in a shared collection is shared, whether a
     reply or a note.
   - Private thoughts belong in the person's own collections. There is no
     private layer inside a shared collection. This applies collections
     decision item 8.
4. **Leaving a shared collection takes your things with you.**
   - A sheet names what leaves before the person confirms.
   - Everything else in the collection stays as it was.
   - The owner can remove any thing, and members can remove their own.
5. **Things found in the connected inbox never enter a shared collection
   automatically.**
   - Neither Vesper nor a standing rule adds them.
   - A person may add one by hand only once Google's policy on showing
     Gmail-derived data to others is confirmed. Until then, inbox finds stay
     private, as the [ingestion decision](2026-09-28-ingestion-and-connected-inbox.md)
     recommends.
6. **The Life project is reorganized by object, and retired boards are
   archived.**
   - The new sections are the model, ways in, the thing, the collection,
     together, Life, doing, decisions and reference.
   - Boards the rulings retire move to an `archive-2026-09-29/` folder in the
     project.
   - Board 00 lists every current board with its status.

## Not decided here

- **The friction proposal** (save on share, no Keep button). The boards draw
  both versions until it is ruled.
- **Whether Vesper may add to a shared collection on its own** (recommended
  default: no), and the shared-collection rule drawn on I1.
- **Notification policy:** batching, quiet hours, push versus in-app, and
  where the notifications list lives.
- **The artifact's form over time** (research §15), and the catalog mechanism
  (September 27, R3).

## Consequences

- **Life boards.** Wave 1 redraws the model, the action map, the thing's page,
  the collection page, sharing, and receiving with notifications. Later waves
  cover forming and editing collections, the Life root, editions and the
  remaining boards.
- **Engineering.**
  - Life needs a collection owner with many-to-many membership.
  - Occasions are artifacts that hold originals.
  - Readings replace the Threads lens.
  - Leaving and removal have defined effects.

  No runtime behavior, flag or schema is changed by this record.
- **Older canon.** The Life v1 contract's four lenses and the September 6
  containers read as superseded where they conflict with items 1–2.

## Revisit trigger

- **Reopen item 1** if people expect an evening to behave like a collection
  (adding unrelated things to it), or a trip to behave like one thing.
- **Reopen item 3** if members are surprised that a reply or note on a shared
  thing is visible to the other members.

Do not rewrite this record if that happens; add a new decision and mark this one
`superseded`.
