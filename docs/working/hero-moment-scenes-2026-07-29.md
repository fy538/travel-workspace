---
doc_type: working
status: active
owner: founder
created: 2026-07-29
expires: 2026-08-28
why_new: The home-surfaces program's Terminus defines WHEN polish stops (the wedge bar); nothing defined WHAT polish serves. These three scenes are that instrument — every design/polish decision until the MVP test is judged by whether it makes one of them land harder. Written per the idea→job→hero-moments pipeline adopted 07-29.
promotes_to: docs/product/ (fold into Product Thesis or Venture Path if they survive the MVP test unchanged)
supersedes: []
depends_on:
  - docs/working/home-surfaces-program-2026-07-28.md
source_of_truth_for:
  - mvp-hero-moments
  - polish-decision-rule
---

# The Three Hero-Moment Scenes

> The wedge bar made concrete. Each scene is ~30 seconds of product use
> where the value is undeniable *without explanation*. Each has a named
> beat (the second where the feeling lands) and a pass test. The voice,
> lens/taste, and memory moments are **vision-bar scenes — deliberately
> excluded**; grading the MVP against them is the retired mistake
> (see Product Thesis, The Proof [07-29]).
>
> **The standing rule:** every polish decision until the MVP test gets
> one question — *does it make one of these three scenes land harder?*
> If yes, do it. If no — however beautiful — it waits.

## Scene 1 — The thread becomes a trip
*(organizer · inception · "I'm not the admin anymore")*

A group chat, 47 messages deep about Lisbon. Two date ranges, three
hotel links, one "wait are we doing this?" Maya has been herding it for
a week. She opens Vesper, starts a trip, and pastes the chaos in. It
comes back *shaped*: June 12–16 vs 19–23 as an actual question, the two
hotels the chat mentioned standing as candidates, a first sketch of the
days. She drops the trip sheet back into the chat — one beautiful card:
destination, dates-in-question, five faces, "3 things to decide."

**Beat:** the argument becomes votes. The chat doesn't die — it stops
being the *record*. Maya's feeling is relief with a flicker of status:
she did less work and it looks like she did more.

**Test:** an organizer who sees this says "I need this for December" —
before anyone says the word AI.

## Scene 2 — Nine seconds to included
*(joiner · the invite · "I'm part of this before I've committed to anything")*

Tom taps Maya's link on the subway. No app store. No sign-up wall. The
actual trip: where, when, who's in, what's still open — and one question
waiting for him: *"Thursday dinner: two camps."* He votes, taps "I'm
good for the 12th–16th," and his name settles onto the trip. Back in the
group chat, the card quietly updates: *4 of 5 in.* That night he
installs the app — and it already knows him, his vote, his dates.

**Beat:** acting before installing. The product asked for nothing before
giving him standing in the trip. Inclusion first, commitment later.

**Test:** a first-time joiner completes one real action on the first
tap, and can say afterward what the app is.

## Scene 3 — The boomerang
*(the group · booking + money · "it caught it")*

The trip's board reads: *Flights ✓ Sarah · Stay — open · Thursday
dinner ✓ Tom.* Sarah taps the stay and says "I've got it" — everyone
sees it's hers now. She books on Booking.com with her own points, the
way she was always going to. When she comes back, Vesper is waiting:
*"Did you get Casa São Bento?"* She pastes the confirmation screenshot.
The board flips to ✓, the dates land on the plan, and the split appears
— the real €612, €153 each — without anyone typing a number.

**Beat:** two seconds, back to back — the board flipping, then the
amount appearing. The two most awkward sentences in group travel
("did anyone book the hotel?" / "what do I owe you?") never got said.

**Test:** by trip's end, the logistics questions have left the group
chat. Chat displacement, felt rather than measured.

## Substrate map (for the sessions doing the polish)

| Scene | Rides on | Status 07-29 |
|---|---|---|
| 1 | trip creation + inbound ingestion (inception-pointed) + shareable trip sheet/card renderer | ingestion built; trip sheet + card = to build (M1 Rung 1 + card family) |
| 2 | zero-install live trip view + invite-row guest actions (`pending_intake` pattern) | invite token/snapshot/OG substrate built; live view + Rung-2 action = to build |
| 3 | claim-on-handoff + return-catch + coverage board + real-amount expense prefill | claim/return-catch BUILT (uncommitted FE mount gap); prefill substrate committed; coverage board = to build (S1) |
