---
doc_type: working
status: active
owner: founder / Chat design
created: 2026-09-14
last_verified: 2026-09-14
expires: 2026-10-14
why_new: The Chat design exploration selected a composition (2026-09-13) and the founder ruled on the seventeen remaining open decisions (2026-09-14); this records the rulings, the design project's current shape, and four bounded handoffs to other owners. The 2026-09-12 exploration brief is superseded as the current description of the project.
supersedes:
  - claude-design-chat-new-project-exploration-handoff-2026-09-12.md
source_of_truth_for: []
---

# Vesper Chat — rulings and handoffs, 2026-09-14

## 1. State

- **Claude Design project:** "Vesper — Chat (September 2026 Exploration)",
  project `096be8ed-c448-4f69-a3ba-af254b75b0a5`. Read-only reference for
  engineering; nothing in it is an implementation contract.
- **Composition selected 2026-09-13:** Direction B, *The Working Surface*.
  A transcript; your turn a solid `ink40` chip; Vesper's answer prose at full
  measure with no container and no name; one text role (`chatTranscript`
  16/26) for every speaker; an in-chat card only when earned (owned elsewhere,
  awaiting a decision, or a comparison on a common axis), one per turn.
- **Seventeen decisions ruled by the founder 2026-09-14** (§2). Eight went
  against the design recommendation; page 6 of the project records both.
- **Project layout now:** page 1 *Decision* (rules 1–14, rulings, what is
  open); 2 *Screens* (start page, rows, search, single chat, group chat);
  3 *Turn* (every turn treatment, large text, six writing rules); 4 *Controls*
  (header, composer); 5 *Cards* (gate, six roles, superseded state, negatives,
  registry mapping); 6 *Ruled* (the seventeen decisions drawn side by side);
  7 *Entered* (arriving from Plans, Places, Social/Life, Entity; cross-root
  agency table); 8 *Returning*; 9 *The first time* (proposed); *Q1 Board*
  (first human question, ready to run). `record/` holds the exploration.
- **Kit:** `chatkit.css` and `chatkit-turns.css` in the project carry every
  rule as a class (`ck-mast`, `ck-row`, `ck-search`, `ck-h .scope`, `ck-next`,
  `ck-retry`, `ck-obj.stale`, `ck-asof`), so a page cannot drift from a ruling.

Standing brief constraints remain: all people, messages, times and places in
the project are fixture material; bookings, payments, rebooking and autonomous
provider contact are not the product's execution promise; Human Reply and
private Ask are different destinations; the AI sends no words and implies no
person's agreement; Chat is not a feed, a second Home or a mandatory gateway.

## 2. The rulings

| # | Decision | Ruling | Against rec? |
| --- | --- | --- | --- |
| 25 | Mast at large text / 320pt | Steps down: base 22/26 past 1.35× scale, 26/30 below 360pt; never more than three lines | |
| 03 | Empty row fill | The nearest things **that are somehow relevant to you** (a place a friend sent, one you asked about, an arrangement you are in), reason in the meta line; never mere proximity | yes |
| 28 | Which photo an answer means | Named in prose, **descriptively** — what is in the picture; never position, number or a re-shown thumbnail | yes |
| 27 | Send while streaming | Queued: lands at once marked NEXT, answered when the current one finishes | |
| 29 | Several cards in a turn | One card per turn; the rest are doors | |
| 30 | Stale card | Fades, keeps its words, loses its actions, dated with what happened and who did it | |
| 21 | Retry placement | Under the whole turn as a plain secondary button; **the amber notice is withdrawn from Chat** (founder rejected its look and colour) | yes |
| 26 | Long header | Scope line truncates from the right, most-important-first, never wraps | |
| 24 | Side chat title | *Side chat* | yes |
| 02 | Uncertainty | In the voice, one step quieter; never a stamp | |
| 22 | What is material | By length (~160 characters); origin is not tracked | yes |
| 15 | Vesper in a room | Answers when addressed | |
| 04 | Carried-in context | Goes with one question only; the held strip is a pre-send state | yes |
| 10 | Microphone | In the send slot while the line is empty | |
| 06 | Search | Real, from the capsule; bounded by the retention agreement | yes |
| 14 | Answer states its fate | Says nothing | |
| 16 | Side chat afterwards | Folded under its room; the room's row says it is there | |

Two new proposals await a founder ruling: page 8 B2 (a hairline "while you
were away" line where a new answer begins, or nothing) and page 9 O1 (first-
ever open: mast absent, three example questions shown once).

## 3. Handoffs

Each is bounded. None asks the recipient to accept the Chat design; each asks
for one thing the Chat project cannot settle alone.

### 3.1 You, Identity & Trust — decisions 08 and 23

- **08 — what a person is told about retention, and where.** Chat has ruled
  its own part: an answer says nothing about what happens to it (14); search
  exists (06); a side chat lives under its room (16). Each of these is bounded
  by whatever 08 settles: what search may find, how long a side chat lives, and
  whether anything is said at the point of asking. Ask: settle 08 in the
  existing history/source proposal
  (`conversation-history-source-expiry-decision-proposal-2026-09-06.md`) and
  say which of the three Chat surfaces it changes.
- **23 — attribution once an answer leaves Chat** (kept to Life, shared into
  Social, put into a room). Chat hands back a door or a decision gate and
  never writes to the destination (page 7). Ask: the receipt wording and the
  attribution line at the destination.

### 3.2 Shared-language workbench — decisions 07 and 20

Two stated deltas from the Chat contract, fallbacks drawn on `record/23`:

- **07** — composer as a raised surface: `radius.surfaceCard 14`, 52pt
  minimum, inset 16, `shadow.composerShelf`, instead of the contract's r12/20.
- **20** — Stop sits under the arriving text; the composer stays writable
  while an answer streams (and, per 27, a question sent then is queued).

Ask: accept, amend, or reject each; the project renders either way.

### 3.3 Card registry owner — `booking_proposal`, `booking_confirmation`

Both are still `active` in `docs/contracts/chat-card-types.json`, with
producers in `travel-agent/backend/concierge/composed_cards.py` and renderers
in `travel-app/components/chat/AttachmentRenderer.tsx`, a month after
`docs/decisions/2026-09-06-reconcile-consumer-strategy.md` retired booking.
The 2026-08-12 artifact investigation named exactly this pattern as a failure
mode. Ask: move both to `deprecated` or `retired` in the contract, or record
why they remain. Not a design question; flagged, not fixed, from this side.

### 3.4 Editorial voice canon — six writing rules

Six rulings are about words and cannot be held by a stylesheet. Page 3 of the
project states them with examples; in short:

1. Vesper never says its own name and is never named in the chrome.
2. Uncertainty is said, not stamped — what is known, when, and how far to lean.
3. A photo is referred to by what is in it, never by position or number.
4. A failure is one sentence in the limit voice inside the answer, plus the
   surest human way round it; the retry is a button, not a paragraph.
5. An answer says nothing about what happens to it.
6. In a room, speak only when addressed, and never speak for anyone; a proposal
   reports what each person actually said.

Ask: adopt into the voice canon (`travel-app/docs/Design Language.md` or its
Roman authored-voice section, whichever owns reply voice), or say where they
should live.

## 4. What this does and does not authorise

Nothing here changes product code, contracts, generated types or the Chat
surface contract. The two contract deltas (07, 20) are proposals. Booking
retirement, Ask/T0 and the retention boundaries are unchanged. Implementation
of the ruled design needs its own Task Intake against
`travel-app/docs/surfaces/vesper-chat/contract.md` and the QA path in
`travel-app/AGENTS.md`; this note is the design-side input to that intake,
not the intake.

## 5. Superseded

`claude-design-chat-new-project-exploration-handoff-2026-09-12.md` remains the
record of the brief and its constraints, which still bind. As a description of
the project's state it is superseded by this note and by page 1 of the project.
