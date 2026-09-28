---
doc_type: decision
status: accepted
owner: founder / product / contribution / capture
created: 2026-09-28
decided: 2026-09-28
last_verified: 2026-09-28
why_new: On September 28, 2026 the founder moved design work upstream to ingestion, ruled that email arrives through a connected inbox rather than forwarding, and asked for less friction at the point of entry. The rulings amend the September 27 composer's list of doors and the contribution contract's email starting point, and existed only in conversation and on Life board I0.
supersedes: []
source_of_truth_for:
  - ingestion-doors-and-things
  - connected-inbox-email
---

# Decision: One way in: doors, things and a connected inbox

## Context

The [September 27 decision](2026-09-27-documenting-core-loop-and-one-composer.md)
made one composer with many doors the only way to capture and share. The
[September 28 collections decision](2026-09-28-collections-are-the-spine.md)
then set where Vesper's work and other people's actions surface. When the Life
board C7 ("One week with Vesper") drew those surfaces, the founder said the
upstream question had not been settled: how things arrive, "either from chat,
sending a photo, or detecting from email," as one coherent experience.

The code already has one intake envelope across nine channels:

| Channel | Where it is defined |
|---|---|
| `chat`, `ios_share_extension`, `android_share`, `camera`, `photo_library`, `email_forward`, `file_picker`, `paste`, `audio` | `SourceChannel` in `travel-agent/backend/core/models/intake.py` |

The Home lane was at travel-agent `5c54a2d5e` on September 28. The experience
around that envelope is not unified:

- The OS share sheet redirects into the app. An in-place extension exists only
  behind a development opt-in in the capture/share package.
- Chat attachments answer without keeping.
- Email arrives only by forwarding to a per-person import address
  (`backend/inbound/email_forward.py`).
- Nothing detects mail on its own.

The [contribution contract §3.9](../systems/contribution-and-consequence.md#39-connected-services-are-narrow-adapters)
says to "begin with forwarded reservation email rather than a full inbox." It
puts ambient ingestion last in its adoption order.

The founder's direction on September 28, in substance:

- Ingestion from chat, a photo or email has to be one coherent experience.
- Email should not be forwarded email. With the person's permission, Vesper
  looks at the mail that might generate artifacts or be relevant.
- The drawings ask for too many permissions. Ingestion friction should be
  lower still, and permission settings are still needed because every person is
  different.

The founder also asked for board I0, which draws this model, and had its rows
relabeled as doors and things. Later the same day the founder asked for research
on related designs. On its findings, they approved redrawing I0 without
confirmations and drawing a new board, I1 ("Asked once").

## Decision

1. **One pipeline, one result.** Every door opens the one composer and feeds
   one intake contract.
   - A thing becomes the same standard artifact whichever door it came through.
   - The same thing arriving through two doors merges into one artifact that
     lists both sources.
   - Recognition follows the open catalog (September 27, item 7): Vesper
     recognizes what a thing is. It never reads a person into it.
2. **Doors and things are separate.**
   - A door is how something arrives: the OS share sheet; inside Vesper (camera,
     photos, add, Keep or Send on an object); Chat; the connected inbox; a
     friend.
   - A thing is what arrives: a screenshot, photograph, link, pass, email
     message, file, text or voice note.
   - A Wallet pass comes through the share sheet door. No door implies a type.
3. **Three origins, different only at arrival.**
   - **You send it.** The payoff appears where you are, as soon as the thing is
     recognized. The target is about two seconds. It is unmeasured; today's
     intake pipeline takes minutes.
   - **Vesper finds it.** Something found through the connected inbox arrives
     quietly, and the person hears about it once, grouped.
   - **A friend sends it.** It arrives as a notification (September 28
     collections decision, item 13).

   After arrival, all three are the same kept thing, in the same collections,
   with the same Undo, removal and deletion.
4. **Email is a connected inbox, not forwarding.** With the person's explicit
   permission, Vesper looks for mail that can become artifacts, such as
   bookings, tickets and reservations. The connection is a narrow adapter under
   contract §3.9:
   - Vesper filters before it reads, and keeps only what matches, never the
     mailbox.
   - A booking is filed as the person's only when it names them. TripIt's inbox
     scan admits importing other travelers' trips. Many confirmation emails
     carry the traveler as structured data (schema.org `underName`).
   - It works with whatever scopes the person grants, including partial grants
     from Google's granular consent.
   - It keeps a visible log of what it found and where it went.
   - It never sends, deletes or changes mail.
   - Disconnecting stops the search and deletes what was read but not kept.

   Forwarding remains as a fallback where a provider has no suitable API
   (iCloud Mail), and for people who prefer it. This amends the "email
   forwarding" door in September 27 item 5, and contract §3.9's starting point
   of forwarded reservation email, for email only. The rest of §3.9 stands:
   permission to retrieve still does not authorize retention beyond matches,
   inference about the person, sharing or write-back.
5. **Entry asks for as little as possible, and how much Vesper does on its own
   is the person's setting.** Ingestion asks for nothing beyond what the
   operating system requires, unless the person benefits right then. The
   defaults and the controls are pending below.
6. **Where things land and where people hear follow the collections
   decision.**
   - A thing joins its kind collection silently, with Undo (item 11).
   - It enters a shared collection only when the person adds it (item 8, and
     the pending default there).
   - What Vesper found arrives as one grouped notification (item 12).
   - What friends send arrives as notifications (item 13).

## Not decided here — founder ruling pending

- **The friction proposal.** Proposed on September 28 and refined by research
  the same day. The founder approved drawing it on I0 and I1; a ruling on those
  boards is pending.
  - **Save on share.** There is no Keep tap. The receipt closes itself, for
    example "Flight · TAP 210 · Oct 12 · Trips".
    - There are two share targets: *Send to Vesper*, which saves at once, and
      *Send to a collection…*, for choosing.
    - Precedents: mymind and Raindrop.
  - **No yes-or-no questions.**
    - When confident, Vesper files the thing with a short, factual "why ·
      Change" line on the item.
    - When unsure, the thing waits in *Not yet placed*, and nothing asks.
    - A correction made on the item applies to similar things going forward.
  - **Undo replaces confirmation.** Undo lives on the item. A collapsed,
    non-alerting "Filed quietly · N" group in notifications keeps a durable
    record of silent actions.
  - **Ask once, when it pays off.**
    - The inbox is offered after the first booking screenshot.
    - Notifications start as iOS provisional (quiet) notifications, and full
      alerts are asked for when a friend first adds something.
    - A standing rule is offered when a collection is first shared.
    - Nothing is asked up front: the photo picker, share extension and Wallet
      need no permission, and a shared photograph carries its own time and
      place.
  - **Presets** under "How much Vesper does on its own": *Keep and organize*
    (default), *Just keep*, and *Do more for me*. Each has per-source,
    per-collection and per-notification switches.
  - **Shared collections are the exception to act-then-undo,** because
    showing something to others cannot be undone. Things enter only by the
    person's choice or by a standing rule they previewed, with a visible
    marker on each item.

  It is in tension with September 27 item 10, where the send control is
  labelled *Keep* for just me. A ruling should say whether the share sheet shows
  that control or completes on its own.
- **Defaults drawn on I0:**
  - A photograph sent to Chat is kept, with *Ask only* available (September 27,
    item 14).
  - One email holding several things becomes several items, grouped.
  - Vesper offers one guess about where or when, only when the photograph's own
    time and place support it. The friction proposal replaces the question with
    filing plus a "why · Change" line, or with *Not yet placed*.
  - A friend's share of something the person already has links to it rather
    than copying it.
- **Which mail counts.** Travel, reservations and tickets are the starting set.
  Google's user-data policy explicitly permits apps that "automate travel
  itineraries or track flights or package delivery statuses." Receipts, orders
  and subscriptions are not decided.
- **Showing inbox-found things to others.** It is unverified whether Google's
  user-data policy allows Gmail-derived items to be shown to other people.
  - Recommended default: anything found in the inbox stays private, even in a
    shared collection, until that is confirmed.
  - Google Calendar does the same with events it creates from Gmail on shared
    calendars.
- **Providers for v1.** Gmail first:
  - Its read scope is a restricted scope, which needs Google OAuth verification
    and an annual third-party security assessment (CASA) when mail data reaches
    Vesper's servers. That takes weeks, so it is on the critical path.
  - Until verification is complete, the app shows an unverified-app warning and
    is capped at 100 new users.
  - Microsoft and Yahoo requirements have not been checked.
  - Camera-roll scanning (Life board 04) stays out of v1.
- **Grouped-notification cadence** for found items: per arrival, daily, or with
  the notification policy the collections decision leaves open.

## Consequences

- **September 27 record.** Item 5's door list reads as the connected inbox, with
  forwarding as a fallback. That record is not rewritten.
- **Contribution contract.** §3.9 records the email amendment. §9 names the
  composer and one intake contract as the horizontal owner of every door
  (already required by the September 27 record).
- **Engineering.** The existing forwarding path (`email_forward`) remains the
  fallback and is not wasted work. New work:
  - a connected-inbox adapter: OAuth, filter first, keep only matches, a visible
    log, disconnect and delete;
  - merging across sources, so one artifact lists its sources;
  - grouped arrival for found items.

  Google verification starts early if the connected inbox is in the first
  cohort. No runtime behaviour, flag or schema is changed by this record, and
  implementation needs a lane and Task Intake evidence.
- **Trust.** The caution is Meta Muse's message sync, reported to have copied a
  columnist's texts after access was declined. Flighty, meanwhile, positions
  itself as "we do not scrape your inbox" and leads with forwarding. The
  connected inbox is explained, narrow and visible, and people can leave it;
  forwarding stays available as the no-permission option.
- **Design.** Life board I0 ("Five ways in, one thing out") draws this model.
  On September 28 a parallel session was redrawing I0 without its
  confirmations and drawing I1 ("Asked once"). C7 is on hold until it is
  rebuilt on I0.

## Revisit trigger

- **Reopen item 4** if people decline the inbox connection because of what it
  asks for, or if Google verification cannot be completed. Forwarding would then
  be the v1 email door.
- **Reopen item 3** if the two-second payoff cannot be met. Arrival would then
  need a designed waiting state.
- **Reopen item 1** if merged artifacts confuse people about where something
  came from.

Do not rewrite this record if that happens; add a new decision and mark this one
`superseded`.
