---
doc_type: decision
status: accepted
owner: founder / product / Life / social design
created: 2026-09-28
decided: 2026-09-28
last_verified: 2026-09-28
why_new: The founder made collections the first-class object and ruled how they are shared and how Vesper's work reaches people, in strategy review on September 27–28, 2026. The rulings change the Life lenses, the September 26 collection rules and the September 27 decision's pending R1, and existed only in conversation and on Life boards C0–C6.
supersedes: []
source_of_truth_for:
  - collections-as-spine
  - collection-visibility-and-membership
  - where-vesper-work-surfaces
---

# Decision: Collections are the spine

## Context

The [September 27 decision](2026-09-27-documenting-core-loop-and-one-composer.md)
set the core loop: document, standard artifact, threads, action. Working it
through on Life boards C0–C6 (Claude Design project `e72a2fd2`), the founder
made the container itself the product's center. Collections were already drawn
as a Life object on Multiplayer Shapes boards 08–10 (`caf916f9`) and governed by
the [September 26 multiplayer direction](2026-09-26-multiplayer-direction.md),
items 16–18.

The founder's direction, in substance:

- Artifacts, threads and collections give Vesper its identity without
  restricting what it can hold.
- A kept thing should have the same consequences whether it points back
  ("a place I've been") or forward ("jazz on Saturday, loosely").
- Organizing work should surface as notifications, not as banners inside the
  record.
- A shared collection shows everything to everyone in it; managing privacy
  inside a collection has no point.
- Things that matter, and insights, belong on Home. Other people's actions
  belong in notifications.

## Decision

### The object

1. **Collections are the spine.** Every kept thing is an artifact that lives in
   one or more collections. Home, Places, Chat and Plans read from collections.
   Returns, time and place, and connecting the dots are downstream of this
   layer, and none keeps its own copy of the material.
2. **A thread is a collection read over time.** There is one container, not
   two. People see "collection"; "thread" remains a design word for the
   over-time reading. Collections read by kind, over time, or on a map when
   they hold places. This refines R1 of the September 27 decision.
3. **A collection forms three ways:** a person starts one; Vesper notices one
   and the person keeps it with one tap; or a kind forms from the catalog
   (September 27, R3).
4. **An item can be in many collections.** Membership is many-to-many. A book
   can sit in Books and in "Lisbon, before we go" at once.
5. **A kept thing is time-agnostic.** Been, ahead, loose and open are states of
   one kind of object, with the same consequences: kept, in collections,
   findable, removable, deletable. This retires D0 row 1 (no separate
   intention owner) and row 2 (Ahead is a reading above NOW).
6. **Remove and Delete.** Remove takes a thing out of one collection; delete
   removes it everywhere and stops Vesper using it. Deleting a collection
   never deletes its things. This retires D0 row 3.

### Sharing

7. **Any collection can be shared, including a personal one,** whole, with a
   person, a group or Friends (September 26, items 7 and 18).
8. **A shared collection shows everything to everyone in it.** There is no
   per-item privacy inside a collection. Adding something to a shared
   collection is sharing it.
9. **Only what can travel enters a shared collection.** A friend's own words
   and photographs stay within the audience they were sent to (September 26,
   item 8). When a person adds a friend's recommendation to a shared
   collection, the place or link goes in and the friend's note stays with the
   person. This is a property of the thing, so no privacy controls are needed
   inside the collection.

### Where Vesper's work and other people's actions surface

10. **Your own actions** get their payoff in place: the share-sheet payoff, a
    kept collection, Undo.
11. **Private, low-stakes, reversible organizing is silent.** A photo placed in
    its evening, a round added to Golf rounds, a book joining a second
    collection. Undo lives on the item.
12. **New structure goes to notifications:** a collection Vesper formed or
    noticed, a split, a merge.
13. **Other people's actions go to notifications:** someone added to, replied
    in or joined a collection you are in.
14. **Insights and what matters now go to Home:** connections between
    collections and timely returns, shown with the things themselves.
15. The separate Updates feed drawn on board C1 is folded into notifications.

## Not decided here — founder ruling pending

- **Vesper adding to a shared collection on its own.** Recommended default:
  it does not. Because adding is sharing, a person's things enter a shared
  collection only when that person adds them; the share sheet offers their
  collections, showing who is in each.
- **Notification policy details:** batching, quiet hours, what is pushed
  versus held in the in-app list. The September 26 decision leaves
  notifications open.

## Consequences

- **Life lenses:** Threads becomes Collections (Life board 01b; D0 row 10).
- **Life boards to update:** C0 drops private suggestions from provenance; C1
  becomes Notifications; C3 drops "only you see this" suggestions and shows
  full visibility and many-to-many membership; C6 is superseded by a
  storyboard of one week (C7), which is on hold until it is rebuilt on the
  arrival model in the [ingestion decision](2026-09-28-ingestion-and-connected-inbox.md)
  (board I0).
- **D0:** rows 1–3 are retired by items 5 and 6; row 4's banners are replaced
  by items 11–13.
- **The contribution contract** records item 9 for collections, and the
  September 26 record's items 16–18 are read together with items 7–9 here.
- **Engineering:** membership many-to-many between Capture's typed artifacts
  and a collection owner, a notifications surface, and Home returns reading
  from collections. No runtime behavior, flag or schema is changed by this
  record.

## Revisit trigger

- **Reopen item 8** if people add things to shared collections that they later
  regret sharing.
- **Reopen items 11–13** if silent organizing surprises people, or if
  notifications become noise in dogfood.
- **Reopen item 2** if people need threads and collections to behave
  differently.

Do not rewrite this record if that happens; add a new decision and mark this one
`superseded`.
