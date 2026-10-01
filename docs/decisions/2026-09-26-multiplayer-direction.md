---
doc_type: decision
status: accepted
owner: founder / product / social design
created: 2026-09-26
decided: 2026-09-26
last_verified: 2026-09-26
why_new: The founder's direction for the multiplayer layer, given in design review of the Multiplayer Shapes project between September 20 and 26, lived only on design boards and working documents; later sessions reopened it and older documents still contradict it.
supersedes: []
source_of_truth_for:
  - multiplayer-sharing-foundation
  - multiplayer-audience-and-passing-on
  - occasion-group-conversation
  - shared-collections
---

# Decision: Multiplayer direction from the Multiplayer Shapes review

## Context

The Claude Design project "Vesper — Multiplayer Shapes" (`caf916f9`, boards
00–11) was reviewed by the founder between September 20 and 26, 2026. The
September 23 direction audit found that the rulings made there existed only on
board 00 and in working documents, while the group/social charter and the
September 22 handoff still said otherwise. On September 26 the founder answered
the remaining open questions: two in their own words (group conversation, the
serif) and the rest by accepting the recommendations put to them.

This record is consistent with, and does not replace, the
[September 5 Home composition amendment](2026-09-05-amend-home-composition-canon.md)
(the social split, reaffirmed here), the
[September 6 consumer strategy](2026-09-06-reconcile-consumer-strategy.md)
(everyday use first), the
[September 9 exact-original display](2026-09-09-exact-original-recipient-display.md),
and the [August 29 contribution contract](2026-08-29-adopt-contribution-and-consequence-contract.md)
and [use grants](2026-08-29-adopt-contribution-use-grants.md).

## Decision

### Sharing

1. **Sharing is the social foundation.** Four kinds from one composer (the one on
   board 01), chosen by what is attached, never by a type picker: words and
   photos; a gathering invitation; "where I'll be", a time-bound status that may
   carry a ticket; a place with what the sender thinks it is good for.
2. **One set of verbs:** one like, comment, quote into a chat, keep. A like is
   seen only by the author; no counts are shown to anyone else.
3. **People's words lead.** No Vesper line under a share. No quotation marks
   around people's own words; a friend's note appears as a post, on Home and in
   Life alike.
4. **Where it was sent from** is off by default. The sender chooses its
   precision; neighbourhood at most unless they name the place.
5. **A shared place or link is a line:** the name, where, and the sender's
   reason in words. Not a card, and no stand-in picture.
6. **Place shares live in Places**, beside the place, in a From friends view.
   Home carries what is sent to you, what has a time, the day's posts that have
   no place (a small strip), and one line pointing to Places. This reaffirms the
   September 5 social split.

### Audience

7. **"Friends" is one audience** in the share sheet, beside a named person or a
   named group. It applies forward only: people who become friends later do not
   gain earlier shares.
8. **Passing on:** the place or link itself travels freely. A friend's own words
   and photographs stay within the audience they were sent to. There is no
   permission step; that boundary is the rule.
9. **Taking a share back** removes the author's words and photographs
   everywhere, including from other people's kept things. A place someone kept
   stays theirs, without the author's words.
10. **Stop sharing** ends what passes between two people from then on; each
    keeps what they already have. **Block** also hides your past shares from
    them and removes you from their suggestions. Neither is announced. **See
    less** stays private and temporary; **Report** is available on any share.
11. **Opening a link, joining what it holds, and becoming friends are three
    separate acts.** Joining one thing never subscribes someone to another
    person's friends posts. No contacts import. Someone without an account may
    add one thing through a link, credited to the person it was sent to; anything
    more asks for an account, honestly.

### Conversation

12. **The chat between two people is private.** Vesper speaks only when asked;
    what was asked and answered is marked and seen by both.
13. **Group conversation is always allowed. Every occasion, a gathering or a
    trip, has a group chat on by default:** the occasion's room. Vesper speaks
    there only when asked.
14. **Getting together is led by conversation.** A poll is an optional
    instrument a host asks for. Availability is not attendance; only an explicit
    yes counts, including a conditional yes while the details fit. Only people
    who are in are shown. Once sent as the plan, a gathering is a Plans occasion,
    and Plans owns its time, place and changes.
15. **"With":** naming someone asks them once. Their yes puts their name on the
    post; keeping the night in a shared record is their separate choice. Someone
    without an account is a plain name. A group cannot be tagged; people are
    named.

### Keeping

16. **Keep is private and immediate, with Undo.** Adding to a collection is a
    second, optional step; adding to a shared collection says who will see it.
17. **Collections** use Life's editorial grammar. By kind and Over time are two
    views of the same collection; which opens first follows its contents, and
    each person's last choice is remembered. Collections live in Life's Threads
    view (no fifth lens) and also appear under the people they are shared with
    and the places they hold.
18. **A collection is shared whole or not at all.** To share part of it, make a
    new collection with just those things. Someone added later sees all of it.
    Contributors add and reply and remove only their own entries; the owner may
    take any entry out of the collection; leaving takes your own entries with
    you. Counts show only what happened; nothing decays; no streaks.
19. **Vesper may use a friend's shared words to answer the recipient's own
    question**, credited, within the audience the friend shared with, and never
    passes them on. The contribution use-grant contract must be amended to allow
    this before anything is built.

### Visual

20. **EB Garamond remains the serif.** The typeface canon is unchanged.
21. **Photographs:** the founder will supply about twenty ordinary photographs to
    become the shared fixture set. Licensed venue photographs may later appear in
    the product only as the small identity tile of a place.

## Consequences and boundaries

- **Group/social charter.** Group-decision ruling 4 in
  [`docs/systems/group-social.md`](../systems/group-social.md) (visible voting on
  by default for trips) is amended by item 14: a poll is something a host asks
  for. The 2026-07-13 "trip's room" ruling extends to every occasion (item 13).
  The charter keeps its position of not competing with messaging apps as a
  general messenger.
- **September 22 handoff.** Its "share selected material" composition is
  replaced by item 18.
- **Life project.** Items 3, 17 and board 07's shared-list rules (each entry
  belongs to its adder and leaves with them) change Life boards 07 and the
  Threads lens; the Life project applies them.
- **Engineering.** The built sharing primitive (one recipient, a place-required
  note) cannot express items 1, 7 or 8; a new share and audience model is
  needed and is not designed here. Existing trip and group rooms continue. No
  runtime behaviour, flag or schema is changed by this record.
- **Not decided here:** notification policy, guest identity and verification,
  retention periods, and export.

## Revisit trigger

- Place shares in Places go unseen in real use, and senders hear nothing back
  (reopens item 6).
- Occasion group chats are unused or become noise in dogfood (reopens item 13).
- Real friend pairs find whole-collection sharing too coarse (reopens item 18).

Do not rewrite this record if that happens; add a new decision and mark this one
`superseded`.
