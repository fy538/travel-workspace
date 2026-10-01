---
doc_type: working
status: active
owner: Claude orchestrator (product map)
created: 2026-09-26
expires: 2026-10-26
why_new: The product map needs one dated, evidence-based atlas of every Social, Chat, You and shared-design-language board, with its disposition, canonical targets, contradictions and debt, so that build progress can be measured against a known design target.
promotes_to: null
supersedes: []
---

# Design Atlas: Social, Chat, You, and the shared design language

This inventory was taken from Claude Design on 2026-09-26. It covers six projects:

- Multiplayer Shapes (MS) `caf916f9`
- Social Experience (SE) `3ef10868`
- Chat, September exploration (CH) `096be8ed`
- You, Identity & Trust (YOU) `b66c82a5`
- Design Language Workbench, Stage 1 plus S2 (WB) `c13ae951`
- Production Kernel (K) `fc85e38a`

The pass was read-only. No design file, repository source or decision record was changed.

## 0. How to read this

### Evidence

- **Complete file lists.** I ran `list_files` (depth −1) on all six projects. I converted each file's etag, a Unix timestamp in microseconds, to UTC.
- **Multiplayer Shapes was re-read today, twice.** It was edited today, 2026-09-26, in two waves:
  - 18:17–21:41 UTC: the "§12 tightening pass".
  - 22:00–22:01 UTC: every board 00–11 again. This wave rewrote the placement on 03 and 00 and trimmed captions.

  I extracted the text of boards 00–11 after each wave. §2.1 reflects the 22:01 state. The Sep 25 catalogs' extraction (22:23 UTC Sep 25) is stale for every MS board.
- **The other five projects are unchanged since their last extraction:**
  - SE was last edited on Sep 22.
  - CH, YOU and the S2 work in WB were last edited on Sep 15.
  - The kernel was last edited on Sep 10.

  For those five I reused the Sep 25 extracted text and catalogs (`catalog/social.md`, `chat-you.md`, `object-model.md`, `life-you-social.md`), and checked each against the etags.
- **Documents read:**
  - `claude-design-multiplayer-threads-life-continuity-handoff-2026-09-22.md`, including its §12 (uncommitted, dated Sep 26)
  - `multiplayer-threads-life-continuity-response-2026-09-22.md`, §8 (the Sep 26 handback, uncommitted)
  - `design-gen/multiplayer/README.md` and `gen_idx.py`
  - `claude-design-chat-rulings-and-handoffs-2026-09-14.md`
  - `claude-design-instrument-language-stage-2-handoff-2026-09-13.md`, §11
  - `vesper-shared-design-language-consolidation-2026-09-10.md`, §§16–25
  - the decisions of 2026-09-05 (Home composition and social split), 2026-09-09 (exact original) and 2026-09-09 (select design convergence)
  - the kernel's `guide.md`
  - the workbench's `vdl-package.json`
  - Social's `vdl-consumed.json`
  - `travel-app/scripts/polish-qa/surfaces.mjs`
  - `travel-app/constants/fonts.ts` and `textVariants.ts`
- **Code revisions checked:**
  - workspace `878581b`
  - travel-app `23cff76f4` (2026-09-22)
  - travel-agent `fdf789d06`

  I spot-checked code only. I did not run it.
- Downloaded HTML was deleted after text extraction. No serve URL is recorded here.

### Who decided what

Each status is tagged with its provenance:

| Tag | Meaning |
|---|---|
| **[Doc]** | An accepted decision record in `docs/decisions/`. |
| **[F]** | A founder ruling or selection in the founder's own words, dated (from a chat message, a question-tool answer, or a board's ruling line). |
| **[F-del]** | A founder-delegated selection, recorded as accepted in a decision (2026-09-09). |
| **[F-dir]** | Founder direction "said in review, Sept 20–26, not yet a recorded decision". MS 00 was relabelled this way on Sep 26. The Sep 25 catalogs called these items "RULED", which overstates them. |
| **[D]** | The design assistant's recommendation or verdict. Where a project's own records say the founder accepted a set of recommendations as a group, it is marked "settled". |

### Dispositions

| Disposition | Meaning |
|---|---|
| **ADOPTED TARGET** | The current authority board for a surface, backed by [Doc], [F] or [F-del]. |
| **SELECTED** | A chosen composition whose supporting states are still proposals, or whose selection is partly contested by later work. |
| **EXPLORATORY-KEEP** | A current proposal or [F-dir] drawing worth building toward, but not decided. |
| **REFERENCE** | An index, ledger, copied donor or historical reasoning board. |
| **SUPERSEDED/REJECTED** | Replaced or ruled out. |

## 1. Headline findings

1. **The newest social direction has no decision record.**
   - On Sep 26, MS 00 relabelled its twelve "ruled" lines as founder direction "said in review, Sept 20–26, not yet a recorded decision".
   - These lines include: the four share kinds with one set of verbs; no Vesper line under shares; the ticket at full size; a private chat between people; conversation-led gathering; Shared with Maya; collections in Life grammar; whole-collection sharing; the place/link line; no group chat; and (added at 22:01 UTC) placement, which "Follows the Sept 5 decision (agreed Sept 26)".
   - Only three social items are backed by an accepted record:
     - the Sep 5 social split;
     - the Sep 9 exact-original display rule;
     - the Sep 9 delegated selection of SE's receiving exemplar and its guest/photo exemplar.
2. **Two contradictions still block a coherent build.**
   - **Group conversation.** MS says "no group chat, for now". Chat B has rooms and side chats, ruled by the founder on Sep 13–14. The shipped Trip group room uses public voting.
   - **The person's identity, split over three or more pages.** You's person page (0-0), Life's "Shared with Maya" (MS 07) and MS 03's "People · Maya" all compete. Code adds the Follow-based `/profile/[userId]` on top.
3. **Three older conflicts were resolved on Sep 26.**
   - **Placement.** Until 21:41 UTC, MS 03 drew a capped "From friends" band on Home, against the Sep 5 [Doc] split. At 22:00, MS 03 was redrawn:
     - place shares live in Places · From friends;
     - Home carries what was sent to you, what has a time, a small strip of the day's posts that have no place, and one line pointing to Places.

     The founder "agreed Sept 26". A residual difference is small: see C1.
   - **Joining and connecting.** MS 04 now keeps joining separate from becoming friends ("Ask to be friends"), and it removed the contacts request. This matches SE's rule that a connection is sought and mutual, and You's mutual Friends.
   - **Keep.** MS 02 and MS 10 now agree on one Keep flow: a private keep at once with Undo, then optionally "Add to a collection".
4. **Chat is the most fully designed of these surfaces.**
   - Direction B was selected [F 09-13], and 17 decisions were ruled [F 09-14].
   - Two proposals still await the founder: B2 and O1.
   - Two contract deltas await the workbench: 07 and 20.
   - Chat conflicts with the social work on four points:
     - rooms;
     - naming Vesper (MS draws "VESPER · ASKED BY NORA" labels);
     - bubbles versus the chip grammar;
     - a decision gate that shows "You: Haven't said", which MS §12.2 removed.
5. **You has the most-ruled person page, but it is anchored to a relationship model that code does not ship.**
   - The design assumes mutual Friends; code ships Follow plus pair circles.
   - The trust half, "yours underneath", is absent from the current canon.
6. **The shared language is split three ways.**
   - VDL 0.4.1: ten components and `vdl.css`, accepted as the design-reference baseline, never published to the kernel. None of its 13 proposed type roles exists in `constants/textVariants.ts`.
   - Life 07's stylesheet, which MS uses for everything.
   - Chat's own `chatkit` CSS.

   S2 has nine library constructions and fifteen bench forms. None is selected. Nothing on the board is adopted, published or migrated.
7. **The kernel's token sources are unchanged since its sync.**
   - Every token source file is identical between `travel-app@e2e792913` and `23cff76f4` (`git diff` is empty).
   - The formal `--check` could not run: `tsc` is missing, so it exited 2 (tool failure). Its drift status is therefore **unverified by the tool** but supported by the source diff.
8. **The QA gate points at older designs.** `polish-qa/surfaces.mjs` anchors `vesper-chat` to August references ("Vesper Chat.html", artifact-language v2.1.1). It anchors `you-portrait` to `profile-self-mature.png`. No QA surface exists for social, original delivery or people.

---

## 2. Board tables per project

Dates are UTC and come from the Claude Design etags. Target build surfaces use the app's actual route or component names where they exist.

### 2.1 Vesper — Multiplayer Shapes `caf916f9`

State:
- Twelve boards, 00–11, plus the `Ticket` component.
- Numbered this way since the Sep 23 renumbering. Board 12, the place-card comparison, was deleted on Sep 25 after the founder chose the line.
- The Sep 26 §12 pass rebuilt 00–06 and 08–10. Its handback is §8 of the response doc.
- A second wave at 22:00–22:01 UTC touched all of 00–11:
  - placement moved on 03 and 00;
  - captions were trimmed on every board;
  - the stale "the place before the show as its card" on 09 was removed.

  This second wave is not yet described in the README or the response doc.
- Every board except 07 now carries the footer: "nothing on these boards is adopted canon, a recorded decision or a promise".

| Board | Last modified | Purpose | Disposition | Evidence | Target build surface |
|---|---|---|---|---|---|
| 00 Start here | 09-26 22:01 | Index. Lists the twelve lines of founder direction (Sept 20–26), the four §12 proposals and ten open items. | REFERENCE (the ledger) | Relabelled on Sep 26 from "Ruled" to [F-dir], per §12.9. The placement line was added at 22:01: "agreed Sept 26". | — |
| 01 Sharing | 09-26 22:00 | Four share kinds (A words and pictures, B gathering, C where I'll be with the ticket, D place), each shown written, received and as the sender sees it. D4 shows the place keeping the note. Q quotes a share into a person chat. | SELECTED ([F-dir] Sep 20–25). The composer itself is unruled (07, decision 3). | [F-dir]: "Four kinds, one set of verbs"; no Vesper line (removed Sep 21 as "noise"); the ticket at full size; where-from placement. The ARTIFACTS·PLACE note still says "place card… hours from the world", which is stale. | New share composer. Home receiving units (`HomeRootV2UnitRenderer`). Places From-friends scope. Chat quote. |
| 02 Sharing the edges | 09-26 22:00 | Audience picker; audience legible on receipt; Keep (now immediate and private, with Undo); Kept in Life; an ask; a link; take back; after withdrawal; pass it on; link page with no app. | SELECTED (verbs [F-dir]); rules EXPLORATORY-KEEP | §12.4 Keep, proposed Sep 26. The eight-frame permission flow was cut Sep 21. The LINK note still says "card… thumbnail", which is stale. | Audience picker; Keep → Life; withdraw; guest web page (`app/invite/[slug]`-style public route). |
| 03 Receiving ("Where friends' shares arrive") | 09-26 22:00 | Frames:<br>• Home across a week: "To you" first; then "With a time"; then "From friends, today", a strip of at most three or four no-place posts; then one line, "Priya and Sam added 2 places · In Places →".<br>• A quiet Sunday.<br>• New frame 6, **Places · From friends** (Near you / Saved / From friends; this week; earlier).<br>• The person page ("still reachable"), with "You kept" kept separate.<br>• See less. | EXPLORATORY-KEEP. **Now aligned with the Sep 5 [Doc] split.** | Placement [F-dir] "agreed Sept 26". "WHY THIS SPLIT" cites the Sep 5 decision "which the code already follows". Also names what would change it: place shares going unseen. | Home people units; Places From-friends scope; Life · People. |
| 04 Connecting | 09-26 22:00 | Invite by sending a thing; the no-app link page, with one proposed "Add, as Maya"; joining one thing; "Maya added Hato"; becoming friends separately; connecting from an occasion; the record starting small; stopping sharing. | EXPLORATORY-KEEP | §12.6, Sep 26: three separate acts, and the contacts request removed. Guest scope and phone identity are open. | Guest link page; friend request (`social_circles`); Occasion "who was there". |
| 05 The chat | 09-26 22:00 (footer and captions) | A private two-person chat with bubbles. Vesper is a gold-spark door; its answer is marked "VESPER · ASKED BY NORA · TO BOTH OF YOU". A one-line card appears when something the two of them own changes. | EXPLORATORY-KEEP ("private chat between people" is [F-dir]). The board itself says a person chat "is proposed and does not exist". | The Sep 21 cut removed the plan/list at the top. Open: what Vesper may use; whether groups get the same door. | Chat root person chat (`relationship_pair_conversations`); no designed UI exists. |
| 06 Getting together | 09-26 22:00 | A: "With" split into three. B: opening, then replies, then **"Send as the plan"** in one step; the conditional yes is honoured; the day-of plan. C: the optional poll. D: presence as a bounded sentence. | EXPLORATORY-KEEP (principles [F-dir]: "conversation, not a vote"; "being free ≠ coming") | §12.2, Sep 26: the details screen and the separate ask are gone; "Dana hasn't said anything" is removed. The board records its conflict with the group-social charter. | Plans/Occasion invitations; composer "With"; presence share. |
| 07 Shared with Maya | 09-26 22:00 (captions trimmed only; not in the §12 pass; still no provenance footer) | Life 07 used verbatim, plus an Ours section, her note as a post, a conversations row, Ours as a page, "been" offered, when she stops sharing, and a year on. It poses four decisions. | EXPLORATORY-KEEP. Only the record's name is [F-dir]. | All four are still shown as "RULED — not yet —". Decision 2 is effectively answered by the [F-dir] "no quotation marks" line, but the board was not updated. It still carries copy that §12.7 removed elsewhere. | Life People lens and relationship record (no owner in code). |
| 08 The collection | 09-26 22:00 | Collections in Life grammar: Our New York (now active: + Add, latest first, three sections), Nights out, Getting pasta right, Interesting stuff, One thing, Our places. | SELECTED ([F-dir] Sep 22: "Collections are drawn in Life's editorial grammar, never as cards or colour fields"; the card versions were retired) | §12.3 and §12.7: removed "Nobody counted…". | Life collection (no user-owned collection object in code). |
| 09 The collection over time | 09-26 22:00 | The same collections on a dated spine: "added" is distinguished from "been"; NOW line; STILL OPEN; a gap drawn as a dashed spine; one night kept on its own. | SELECTED (grammar); the switch default is open | §12.3: "added is not been". The stale "as its card" wording was removed at 22:00. | Life collection, Over-time lens. |
| 10 Around a collection | 09-26 22:00 | Keep then maybe add; correct in one line; share whole, or "make a new collection"; use it later ("Jo's here with her parents… which would suit?" returns 3 of 12, with checked facts and unknowns). | EXPLORATORY-KEEP (whole-collection sharing is [F-dir]) | §12.8. History access and contributor rights are proposed, not settled. | Life collection; a share out; a Vesper answer over kept material (the grant question is open). |
| 11 Type | 09-26 22:00 (footer and captions) | The serif four ways: EB Garamond now, Garamond about 15% larger, Source Serif 4, Newsreader. | EXPLORATORY-KEEP (a study) | §12.9: Source Serif 4 is a "provisional preference for dense rows, not a global change". | `constants/fonts.ts` and `textVariants.ts` (a canon decision). |
| Ticket (component) | 09-21 23:15 | The Life ticket, admission mode. | REFERENCE (a copy) | Copied from Life `e72a2fd2`, unmodified. It is the same size (17,327 bytes) as the WB Ticket. | `TicketBand` (one form only in code). |

Shared files:
- `vdl.css`, `vdl-package.json` (claims 0.4.1) and `support.js`, dated 09-20.
- The kernel `_ds/styles.css`, dated 09-20.
- The nine other package components were **deleted on Sep 22**. The manifest still lists them.

### 2.2 Vesper — Social Experience `3ef10868`

State:
- Consumes `vdl-stage1 0.4.1`, recorded 09-11 in `vdl-consumed.json`.
- Last edits were on 09-22: 00, 07, 10 and 10P.
- The frame budget is recorded as an unresolved discrepancy: 41 storyboard slots against a ceiling of 24, and 16 comparison frames against 12.

| Board | Last modified | Purpose | Disposition | Evidence | Target build surface |
|---|---|---|---|---|---|
| 00 Start Here | 09-22 01:53 | Promise; cast (Nora, Maya, Dana, Sam, the boat couple); three experiences; entry points; legend; budget; index; reference shelf R1–R12. | REFERENCE | — | — |
| 01 Checkpoint 1 — Cast, Ledger, Sequence | 09-11 19:38 | Calendar, grants ledger, drift, sequences, the 24-slot allocation, the six decision pairs. | REFERENCE | Reviewed; corrections incorporated. | — |
| 02 A little of your world | 09-11 19:38 | 02.1 private Ask with a photo; 02.2 share from the object ("WHO: Just me · Friends · Nora only"); 02.3 Places From friends; 02.4 the Print Room opened (original, then reply, then gallery notes, then Priya, then private Ask); 02.5 reply in context; 02.6 Ask Vesper (Maya sees nothing); 02.7 the sender's quiet return. | **ADOPTED TARGET** for original-first receiving | [Doc]/[F-del] 2026-09-09: "select original-first receiving… as the core exemplars". Uses OriginalReader 0.4.1 in full density. | Places From friends; `/original-delivery/[id]` reader; Chat private Ask. |
| 03 An easier way to get together | 09-11 19:38 | 03.1 host once from one sentence; 03.2 guest link (InviteCard guest, pill); 03.3 Dana's contribution; 03.4 the dinner as one page; 03.5 proposal with cost; 03.6 the change for Sam; 03.7 arrival; 03.8 phones away. | **SELECTED** (03.5 proposal route and 03.7–03.8 guest hospitality) | [Doc] 09-09: the sentence-6 prepared-message door; the guest-hospitality exemplar [F-del]. 03.1/03.2 InviteCard is contested by MS 01 ("read as a form"). | Occasion invitations (account-only in code); guest link (not built). |
| 04 Something stays with us | 09-10 01:15 | 04.1–04.3 Maya's photo, its arrival, and Sam's later photo; 04.4 the evening record; 04.5 one retrieval; 04.6/04.7 staying in touch (C5); 04.8 another evening; 04.9 withdrawal. | **SELECTED** (04.1–04.3), rest EXPLORATORY-KEEP | [F-del] 09-09 asymmetric-photo sequence. C5 is only a proposal (ongoing-connection proposal). | Home photo arrival; Life evening record; `life-find`. |
| 05 The important alternatives | 09-11 19:38 | D1–D7 matched pairs, each with a recommendation and its cost. | REFERENCE ([D] recommendations proposed) | D2 (acknowledgment) was left unadopted and is now overtaken by MS's one like [F-dir]. D7-A was re-adopted on 0.4.1. | — |
| 06 Connected route | 09-09 05:21 | Linked frames per participant: an action → result → return map. | REFERENCE | — | — |
| 07 Decisions and return to the app | 09-22 01:53 | The recommended composition, six decisions, accepted versus proposed, the cost ledger, dependencies, ten root deltas, and what was consumed at which version. | REFERENCE (a ledger; its deltas are proposals) | States "Nothing here amends canon". | Root owners' delta queues. |
| 08 Continuations | 09-10 01:15 | 08.1–08.3 a friend's original without a place (received, opened, found again); 08.4–08.5 where Sam returns. | EXPLORATORY-KEEP | Its wording was agreed with Life 07.7/07.8. The Keep copy is contested (§4). | Home addressed region; Life People. |
| 09 Sending, access and control | 09-15 23:44 | Recipient resolution (two Noras, a typo); preview; truthful result; the sender's edit and withdrawal and what survives; four controls (fewer, mute, leave, block, plus report); a one-time code at the address boundary. | EXPLORATORY-KEEP (the best existing Send state spec) | Marked "POLICY PROPOSED, NOT ADOPTED". | The built exact-original send; controls (not built). |
| 10 Photos, sent and received | 09-22 01:53 | Selecting a set from Life's evening photos, preview naming what is left out, five outcomes, the pair arriving on Home, a viewer, later titles. | EXPLORATORY-KEEP | "The set is a bounded proposal". 10.5 B (light context) is [D]-recommended. | Life photo selection; Home arrival (a set is not built). |
| 10P Photo exchange, simulated | 09-22 01:53 | A stateful prototype of 10's outcome rule. | EXPLORATORY-KEEP | Offered to Life 04c. | — |
| Before shared package — 02 / 03 / 05 | 09-11 04:45 | Copies of 02, 03 and 05 from before 0.4.1. | SUPERSEDED | Replaced by the 0.4.1 re-adoption. | — |
| R1–R12 reference shelf | 09-07 18:18–18:52 | Copied donors: R1 Places Through My People; R2 Places Taking It Forward; R3 Life People; R4 Life Inside a Record; R5 Entity People Slot; R6 Entity Useful Edges; R7 Plans Shared Afternoon; R8 Plans Continuations; R9 Aperture Map as Invite (non-canonical); R10 Home Return; R11 Home Persona A; R12 Places Ordinary Opening. | REFERENCE (frozen Sep 7 copies) | SE 00 cautions: R5 "used in tonight" is excluded; R9's keep-report and rebinding are excluded. | — |

Components (copies of 0.4.1):
- `OriginalReader` (09-11 19:38)
- `InviteCard`, `Notice` (09-11 04:45)
- `media/print-room-*.svg`
- `_kit/board-kit.css`

### 2.3 Vesper — Chat (September 2026 Exploration) `096be8ed`

State:
- Direction B, *The Working Surface*, was selected [F 09-13]: "we want B but the dynamic artifact is optional".
- Seventeen decisions were ruled [F 09-14]; eight of them went against the recommendation.
- The rest of the recommendations were "go with recommendations" [F 09-14], which I tag as settled.

| Board | Last modified | Purpose | Disposition | Evidence | Target build surface |
|---|---|---|---|---|---|
| 1 Decision | 09-15 03:06 | Chat as decided: 14 rules, the ruling table, what is open. | **ADOPTED TARGET** (authority page) | [F] 09-13 and 09-14; `chat-rulings-and-handoffs-2026-09-14.md`. | `app/(tabs)/concierge`; `docs/surfaces/vesper-chat/contract.md`. |
| 2 Screens | 09-15 02:53 | Start page (mast S1/S2; rows R1–R7, at most two), search F1–F3, single chat C1–C6, group room G1–G5 (room, side-chat door, side chat, proposal awaiting, guest view). | **ADOPTED TARGET** (rooms are contested; see §4) | [F] ruling 03 (relevant fill), 06 (search), 15 (answers when addressed), 16 (folded side chat), 24 ("Side chat"). | Concierge start, `history`; the side-chat backend (`POST /side-chat`, `chat.py:664`). |
| 3 Turn | 09-15 02:53 | Every turn treatment; large text; six writing rules. | **ADOPTED TARGET** | [F] rulings 02, 04, 21, 22, 27, 28. The six writing rules were handed to the voice canon but are **not adopted there**. | Transcript renderer; voice canon. |
| 4 Controls | 09-15 03:08 | Header (world stamp, scope line, room, side chat, offline) and composer (raised, mic in the send slot, held, room, listening). | ADOPTED TARGET, except composer **delta 07** (r14/52/16) and **delta 20** (Stop under the text), which are proposed to the workbench | Contract says 48/r12/20. Code follows the contract. | Composer; header. |
| 5 Cards | 09-15 03:06 | The gate ("only when earned"), six roles, the superseded card, the must-not list, the registry role map. | **ADOPTED TARGET** (gate [F 09-13]; roles settled) | Registry: `booking_proposal` and `booking_confirmation` are still `active` in `attachment_lifecycle` in `docs/contracts/chat-card-types.json` (verified). | Card renderers; card contract. |
| 6 Open (the "Ruled" page) | 09-15 03:02 | The seventeen decisions drawn side by side, each with its ruling. | REFERENCE (the record of the rulings) | The file is named "6 Open"; the index on page 1 calls it "6 Ruled". | — |
| 7 Entered | 09-15 02:57 | Arriving from Plans, Places, a person's note, Life or Entity: the scope line and what Chat may hand back. | SELECTED (settled en bloc 09-14) | "Chat never writes to the source." | `routeForPrivateAsk`, `newConciergeThread(seed)`. |
| 8 Returning | 09-15 02:57 | Mid-draft; an answer that arrived while away; something held. | EXPLORATORY-KEEP (**B2 awaits the founder**) | Rulings doc §2. | Transcript state restore. |
| 9 Onboarding | 09-15 02:57 | First-ever open: no mast, three example questions, once. | EXPLORATORY-KEEP (**O1 awaits the founder**) | Not reconciled with the 09-12 onboarding brief. | Onboarding → Chat. |
| Q1 Board | 09-15 02:57 | The first human test: does the solid chip take the eye from the answer? | EXPLORATORY-KEEP (ready, **not run**) | Q2 (side-chat discoverability) needs a build. | — |
| record/00 Index and Reference Notes | 09-14 14:45 | Round 1 index; reference resolution. | REFERENCE | — | — |
| record/01 A · The Continuous Page | 09-14 14:45 | Direction A. | SUPERSEDED/REJECTED | Serif ranks Vesper above people; one role makes the question look like the answer. | — |
| record/02 B · The Working Surface | 09-14 14:45 | Direction B as first drawn. | SUPERSEDED (by pages 1–5) | Selected [F 09-13]. | — |
| record/03 C · One Thing at a Time | 09-14 14:45 | Direction C. | REJECTED | [D] recommended it; [F] chose B. | — |
| record/04 Comparison, Family Check and Recommendation | 09-14 14:45 | Turn-1 comparison. | REFERENCE | — | — |
| record/05 D · The Lens | 09-14 14:45 | The material fills the screen. | REJECTED | [F] "no D, should never fill the screen like that". | — |
| record/06 E · Aloud | 09-14 14:45 | Voice-first. | REJECTED | Voice is a control, not a composition (decision 13). | — |
| record/07 F · The Slip | 09-14 14:45 | An answer expires unless kept. | REJECTED | Ruling 14: "an answer says nothing about its fate". | — |
| record/08 Turn 2 — Six Directions | 09-14 14:45 | Updated recommendation. | SUPERSEDED | — | — |
| record/08b Comparison — Six Compositions Redrawn | 09-14 14:45 | Side-by-side comparison. | REFERENCE | — | — |
| record/09 Start Here — Page and Component Canvases | 09-14 14:45 | Page-keyed index ([F] restructure request). | SUPERSEDED (by page 1) | — | — |
| record/10 Page — Chat Start | 09-14 14:45 | Start-page variants. | SUPERSEDED (by page 2) | [F] "add a headline bolded just like home or places". | — |
| record/11 Page — Group Chat | 09-14 14:45 | Rooms and private-answer variants. | SUPERSEDED (by page 2 G1–G5) | [F 09-13]: "group chat… no private mechanism, any private chat should be a side chat". | — |
| record/12 Component — Headers | 09-14 14:45 | Header variants. | SUPERSEDED (by page 4) | — | — |
| record/13 Component — Message Anatomy | 09-14 14:45 | Chip fill and outline; V1–V7 treatments of Vesper. | REFERENCE (the solid ink40 chip, W5 [F]) | [F] "i don't like umber"; "go with W5, apply it everywhere". | — |
| record/13b Component — What You Attach | 09-14 14:45 | Attachment sizes. | SUPERSEDED (rule 4) | [F] "why can't the photo be smaller?" | — |
| record/14 Page — Single Chat | 09-14 14:45 | Single-chat page. | SUPERSEDED (page 2 C1–C6) | — | — |
| record/15 Component — Does Vesper Need a Name | 09-14 14:45 | VA1–VA7. | REFERENCE (source of the "no name" ruling) | [F 09-13] "apply the name change too — drop it everywhere". | — |
| record/16 Your Turn at Four Lengths | 09-14 22:47 | Material threshold. | SUPERSEDED (ruling 22: by length) | — | — |
| record/17 Your Turn, Fill Weight | 09-14 14:45 | Chip weight. | SUPERSEDED (W5) | — | — |
| record/18 State of Play | 09-14 14:45 | The Sep 13 state. | SUPERSEDED (page 1) | — | — |
| record/22 Component — Composer | 09-14 14:45 | Composer variants. | REFERENCE (source of delta 07) | — | — |
| record/23 Shared Language — Five Proposals | 09-14 14:45 | Deltas for the workbench. | REFERENCE (handoff 3.2) | — | — |
| record/24 Large Text and Narrow Widths | 09-14 14:45 | AX sizes. | SUPERSEDED (page 3 T11/T12) | — | — |
| record/25 Review Session — Three Questions | 09-14 14:45 | Human questions. | SUPERSEDED (Q1/Q2) | — | — |
| record/26 Component — Result Objects | 09-14 14:45 | Card gate, registry mapping. | SUPERSEDED (page 5) | — | — |
| record/refs/home/02 and record/refs/home-0912/02 (Persona A) | 09-14 14:45 | Two copies of Home 02 (337,652 and 329,529 bytes). | REFERENCE (duplicate, stale) | — | — |
| record/refs/home-0912 `OriginalReader`, `Notice` | 09-14 14:45 | Copied components. | REFERENCE | — | — |

Kit files:
- Top level: `chatkit.css` and `chatkit-turns.css` (09-15), plus `chat.css`.
- `record/` holds **older** copies: `chatkit.css` at 9,319 bytes against 15,633; `chatkit-turns.css` at 11,628 against 14,021.
- There are two kernel copies: `kernel/styles.css` and `_ds/…/styles.css`.

### 2.4 Vesper — You, Identity & Trust `b66c82a5`

State:
- The current state is canvases 0-0 to 0-5 [F 09-14: "Five canvases 0-1–0-5 are the current state"].
- Boards 00–34 are history.
- The ledger on 0-5 records 14 rules, 24 decisions and 13 open questions.
- The package is `vdl-stage1 0.4.1`, copied in and pinned.

| Board | Last modified | Purpose | Disposition | Evidence | Target build surface |
|---|---|---|---|---|---|
| 0-0 Sections | 09-15 02:16 | Authority for the person page. It has nine sections: 01 Head, 02 State row (self), 03 Line, 04 Standing, 05 Message/Friends pills, 06 One live ask, 07 Her time here (two-layer axis), 08 Places, 09 Thread (朋友圈). | **ADOPTED TARGET** | [F] r1–r3, 09-14 ("message, and friend / not friend. similar to instagram"; relationship first; one original; the Message pill is kept). | `/profile/[userId]`, `/you` (the current code is the Aug portrait plus Follow). |
| 0-1 The Page | 09-15 02:13 | The page rendered, with callouts. | **ADOPTED TARGET** | `you-head.css` rhythm (r3). | Same. |
| 0-2 Who Sees What | 09-15 02:18 | Self, friend, anyone; unavailable/partial; withdrawn entry. | **ADOPTED TARGET** | Rule 10: "no such person" must look the same as "not shared with you". Stranger reach is open. | Profile projection per viewer. |
| 0-3 Connecting | 09-15 02:22 | Add friend sheet (with its exclusion list), Requested, Friends sheet (Mute, Remove friend), per-entry audience, remove entry. | **ADOPTED TARGET** (design); the relationship primitive is open at product level | [F r3]. The code ships `FollowPill` and `follows.py`. Block and "her side" are undrawn. | `/you/people`, `social_circles`, `follows`. |
| 0-4 The Axis | 09-15 00:16 | "Her time here": a grey layer for her shape and a gold layer for your exchanges; the shape grant sheet (default Nobody). | **ADOPTED TARGET** | [F 09-14] "Board 34, decision made"; "Omit it; default is Nobody". The S2 check is open. | Together projection (backend-only, dark). |
| 0-5 Rules and Open Decisions | 09-15 02:20 | Ledger: 14 rules, 24 decisions, 13 open questions, archive map, extensions to send back. | REFERENCE (the ledger) | — | — |
| 00 Index and Reference Notes | 09-13 16:02 | Round 1 index. | SUPERSEDED (0-0, 0-5) | — | — |
| 01 A · Who's Looking; 02 B · Working From; 03 C · In Effect | 09-12 23:39 to 09-13 16:04 | Round 1 directions. | SUPERSEDED | C was the [D] recommendation. [F 09-13] "still needs to resemble a rough profile". | — |
| 04 Cross-Root and Spot Checks; 05 Recommendation and Open Decisions | 09-12 23:39; 09-13 16:00 | Round 1 checks and recommendation. | SUPERSEDED | — | — |
| 06 D · The Card; 07 E · One Sentence; 08 F · How Close; 09 The Bolder Set | 09-13 00:12 to 15:58 | The bolder directions. | SUPERSEDED | Superseded by the language rebuild at 21. | — |
| 10 The Entrance; 11 What Others See; 12 The Adjustment; 13 With Almost Nothing (each "Six Ways") | 09-13 15:48–15:51 | The same page across variants. | SUPERSEDED | 12 keeps "it still can't book, pay or message anyone". | — |
| 14 Component Ledger | 09-13 15:56 | Component defects. | REFERENCE (its eight defects "are still real") | — | Package extension queue. |
| 15 Practical Entrances; 16 The Type Fix; 17 The Contract Skeleton | 09-13 16:37–18:08 | Practical entrances, the type fix, the contract skeleton. | SUPERSEDED (by 21 and 0-1) | — | — |
| 18 In Vesper's Own Language | 09-13 19:07 | **The only drawing of the trust half**: Always true / In force now / Kept / A change being proposed / People and account. | REFERENCE (**missing from current canon**) | Decision 09-12 "yours underneath". | `/you/settings`, `constraints`, `memory`, `autonomy`, `privacy`. |
| 19 You For Others | 09-13 19:22 | Outward-only fails for Wes on day nine; so "outward on top, yours underneath". | REFERENCE | Decision 09-12. | — |
| 20 The Thread | 09-13 19:56 | The 朋友圈 thread. | REFERENCE (live as section 09) | [F]: "like a thread of pengyouquan… but more editorial". | — |
| 21 A Page With No Picture | 09-13 20:43 | The language rebuild; the header is typographic. | REFERENCE | [F] "what if there's no profile background pictures". | — |
| 22 Places More Visual | 09-13 20:53 | Places made visual; the map option. | REJECTED (map) / REFERENCE | "Cluster density is disclosure". | — |
| 23 Places As Plates; 24 Places Carousel | 09-13 21:10; 21:21 | Place plates; grid at two or fewer, rail at three or more. | REFERENCE (live in 0-1) | [F] "let's make it a carousel… if there are more than 2". | — |
| 25 An Ordinary Tuesday; 26 The Seam | 09-13 22:40; 23:00 | Home-side context: 6 of 16 rows need a friend; "a friend gets a line inside the world". | REFERENCE | The seam question is open. | Home rows (attribution avatar → profile). |
| 27 Your Own Page | 09-13 23:13 | Your own page = the visitor page + a state row + gold lines; no compose. | REFERENCE (live in 0-2) | Decision 09-13. | — |
| 28 Sections We Do Not Have; 29 More Sections | 09-13 23:17; 23:22 | Sections kept and rejected. | REFERENCE | Decision 09-13: availability, travel list, guestbook and others were rejected. | — |
| 30 How A Connection Forms | 09-13 23:32 | "Follow is a claim; showing is a gift". | SUPERSEDED (by r3 pills) | — | — |
| 31 Where The Actions Go | 09-13 23:39 | Action placement. | REFERENCE (its "both at top" option is now the answer) | [F] "can the option be top of the screen, under the name?" | — |
| 32 The Profile On The Package | 09-14 00:01 | The page ported onto 0.4.1. | SUPERSEDED in part (the OriginalReader thread is retired) | r2. | — |
| 33 The Elastic Axis; 34 The Whole Shape And Your Slice | 09-14 00:09; 01:17 | Axis mechanics. | REFERENCE (live in 0-4) | [F] 09-14. | — |

Components (0.4.1 copies, 09-13 23:57):
- `ActionGroup`, `FactPair`, `InviteCard`, `LocationFooter`, `Notice`, `OriginalReader`, `PlaceHead`, `PlaceIdentity`, `SourceList`.
- `OriginalReader` is retired as the thread unit but still present.

Local CSS:
- `you-head.css` and `you-thread.css` are current.
- `you.css`, `you-bold.css`, `you-compare.css`, `you-practical.css` and `you-refs.js` serve the history boards.

### 2.5 Vesper — Design Language Workbench (Stage 1 + S2) `c13ae951`

| Board | Last modified | Purpose | Disposition | Evidence | Target build surface |
|---|---|---|---|---|---|
| 00 Reuse and Provenance | 09-10 22:35 | The kernel stamp; the propagation test (a bound `_ds` folder is a copy, not a link). | REFERENCE | — | — |
| 01 Selection Manifest | 09-11 01:21 | The selected compositions per root. | REFERENCE | [F-del] 09-09 selections. | — |
| 02A Comparison — Same Human Original | 09-11 16:55 | OriginalReader open/card/full/retrieval against Home, Places, Social and Life. | **ADOPTED TARGET** | §19 [F] accepted the baseline; §22 accepted the 0.4.1 reader patch. | `ReceivedOriginalSurface` and `OriginalMaterialView` (no card, full or retrieval density in code). |
| 02B Comparison — Same Invitation | 09-11 03:45 | InviteCard host/guest/answered, pill and rounded. | **ADOPTED TARGET** (contested by MS 01) | §19, §22. Plans keeps its own layouts. | None in code. |
| 02C Comparison — Same Place | 09-11 02:09 | Entity 14 R2 rebuilt from PlaceHead, FactPair, SourceList, ActionGroup and LocationFooter. | **ADOPTED TARGET** (R2 protected) | §17.2, §19. | `ObjectPageRebuild` (gated). |
| 02D Comparison — Same Ticket | 09-11 03:45 | Ticket in four modes × three densities. | **ADOPTED TARGET** (the visual family, not the fixture data) | §19. | `TicketBand` (one form). |
| 03A Full Scroll — Home; 03B — Places | 09-11 02:04; 02:07 | Fidelity ports. | REFERENCE | "Fidelity references, not part of the package". | — |
| 03C Density Counterchecks — Life and Plans | 09-11 01:21 | Counterchecks. | REFERENCE | — | — |
| 04 Coverage Map | 09-11 01:23 | Coverage dispositions. | REFERENCE | — | — |
| 05 Checkpoint | 09-11 01:26 | Fidelity handback; §17.4 dispositions; named mapping gaps. | REFERENCE | Its header reads "VDL STAGE1 0.2-DRAFT", which is stale. | — |
| 06 Shared Package | 09-11 19:14 | The package manifest board: 10 components, `vdl.css`, proposed roles, the extension queue. | **ADOPTED TARGET** (design-reference level; "not published to the Production Kernel") | §22. | A future shared RN component set; `textVariants.ts`. |
| S2-A Start here and the style | 09-15 03:39 | Direction sentence, the 15-mark alphabet, the five-line ladder, honesty rules, refusals. | EXPLORATORY-KEEP (for founder selection) | Brief §11.12–11.16. | `components/instruments/index.ts` docblock. |
| S2-B The constructions | 09-15 03:21 | The nine library constructions (Part I); bench round 1 (II, §12–19); bench round 2 (III, §20–27). | EXPLORATORY-KEEP | §11.17, §11.20. | `components/instruments/*` (dev gallery only). |
| S2-C The compositions | 09-15 02:21 | Six compositions; 17 ordinary-life compositions (II); register study (III). | EXPLORATORY-KEEP | §11.18, §11.19. | — |
| S2-D Recommendation, native map and checks | 09-15 03:35 | Per-construction recommendations, bench leans, rule amendments, native map, consumers. | EXPLORATORY-KEEP (**the decision sheet; nothing selected**) | "Selection is yours — nothing here is adopted, published or migrated". | `DayBand`, `WeekShape` (a real Home consumer), `TideCurve`. |
| refs/ (home, life, places, plans, social, entity) | 09-10 22:59 | Donor copies from before consolidation. | REFERENCE (frozen) | — | — |

Components are listed separately:

- **Package 0.4.1** (ADOPTED at design-reference level):
  - `OriginalReader` (09-11 19:09; the only component changed in 0.4 and 0.4.1)
  - `InviteCard` (09-11 03:40)
  - `Ticket` (09-11 01:10)
  - `PlaceHead`, `SourceList`, `ActionGroup`, `LocationFooter` (09-11 01:01)
  - `FactPair` (09-11 01:04)
  - `Notice` (09-10 23:08)
  - `PlaceIdentity` (09-10 23:30; its `preview` density only)
- **S2 library, nine constructions** (proposed): `S2Track`, `S2Section`, `S2Sequence`, `S2Pair`, `S2Against`, `S2Correction`, `S2Level`, `S2Count`, `S2Cycle` (dated 09-13 19:34 to 09-15 01:12).
- **Withdrawn:** `S2Change` (09-13 22:57), kept only as the rejected specimen.
- **S2 bench, fifteen forms** (loaded only through `s2-test.css`):
  - round 1: `S2Scales`, `S2Chain`, `S2Profile`, `S2Bearing`, `S2Almanac`, `S2Ledger`, `S2Journey`
  - round 2: `S2Plan`, `S2WeekGrid`, `S2Dots`, `S2Curve`, `S2Ribbon`, `S2Roster`, `S2SunPath`, `S2DayRing`
  - dated 09-15 00:05 to 03:13

### 2.6 Vesper · Production Kernel `fc85e38a`

State:
- A design-system project and the org default. Org-shared, edit link.
- **Guide pages** (09-10 22:23–22:32): `Tokens.html`, `Actions.html`, `Fields.html`, `Headers.html`, `Rows.html`, `Selection.html`, `Sheets.html`, `States.html`, `Surfaces.html`, `index.html`.
- **Files:** `guide.md` (09-10 22:26), `styles.css` (09-10 22:20; sha256 `a843ca5b…`, 29,657 bytes), `tokens.json`.
- `_ds_manifest.json` and `_ds_bundle.js` date from **07-25** and are stale: board 00 notes the manifest "still listed no global CSS".
- Disposition: **ADOPTED TARGET** as a projection of code ("the code wins: regenerate, don't hand-edit").
- It documents 9 of 113 registry components. Newer components such as `Door`, `RootFloatingHeader` and `SectionHeader` are "ungrounded until read from source".

#### Token comparison

**The kernel against the app.**
- The kernel was synced from `travel-app@e2e792913`.
- `git diff e2e792913 23cff76f4` over the eight source files the export reads is empty: `colors`, `textVariants`, `layout`, `cardSurface`, `fonts`, `headerChrome`, `segmentedTokens`, `stateTokens`. The kernel is therefore current by source diff.
- `design_kernel_export.mjs --check` exited **2**: `tsc` is absent from `travel-app/node_modules`. The tool verdict is **unverified**.
- Every consumer copy (MS, SE, CH, YOU, WB) is the same 29,657-byte file. The manifests record the same sha.

**`vdl.css` against the kernel.**
- `vdl.css` is geometry built only on `--vk-*` variables.
- It has four component-local hex tokens: map water, deep water, road, and media hatch.
- It proposes 13 type roles. None exists in `constants/textVariants.ts`:
  - propose permanent: `sectionHeading` 13/600 (ruled Sep 5 but missing from code), `metaLine`, `supportLine`, `unitTitle`, `excerpt`
  - owner call: `placeName`, `placeStamp`, `placeReading`
  - component-local: `readerOriginal`, `factValue`, `routeCode`, `recordTitle`, `stepNumeral`
- Its `--vdl-version` string still reads **0.3** while the manifest says 0.4.1.

**Other consumers.**
- MS styles its boards with Life 07's stylesheet (the "Life skin"), not with VDL roles.
- Chat uses `chatkit` CSS, whose `chatTranscript` 16/26 role does exist in code.
- You's head avatar is 44pt. It is not in the kernel's avatar ladder (22 / 28 / 40 / 58).

**Serif.**
- The kernel lists `serifBodySm` at 13px, below the app's own 15px serif floor. `fonts.ts` enforces that floor with a ratchet test and baselines the existing sites.
- `fonts.ts` records that **Newsreader shipped in 2026-06 and was reversed**. It also carries a ×1.2 serif-to-sans companion rule.
- Both facts bear directly on MS 11's candidates C and D and on option B (Garamond about 15% larger).

---

## 3. Canonical target set per surface

"Canonical" means the board a builder should treat as the target today. Where authority is thin, that is said.

### 3.1 Social

| Surface | Canonical target | Supporting state specs | Authority strength |
|---|---|---|---|
| **Share composer** | MS 01 A1/B1/C1/D1 (one composer; type inferred; `To ▸ audience`; where-from line; glyph toolbar). MS 02.1 audience picker. MS 06 A1 "With" and D0 presence. | SE 02.2 (share from the object, no prelude). SE 09.1–09.3 (recipient resolution, preview is the message, truthful Sent / Didn't send / Not sure). | [F-dir] for the kinds and verbs. **The composer choice is unruled** (MS 07 decision 3: board 01's composer vs Life 04c's). The first built slice, exact original to one recipient, should adopt SE 09's semantics. |
| **Receiving** | MS 01 A2–D2 post anatomy (words, then attachment smaller, then where-from, then the four glyph verbs). MS 02.2 audience legible. MS 03 (22:00): Home = to you / with a time / today's no-place strip / one line to Places; frame 6 is Places · From friends. SE 02.3/02.4 (Places From friends; opened original with its sections in order). SE 04.2/10.3 photo arrival. OriginalReader `full` 0.4.1. | SE 08.1–08.3. | [F-del]/[Doc] for SE 02 and 04.1–04.3. [F-dir] for the verbs. Placement is [Doc] Sep 5, and MS now matches it ([F-dir] "agreed Sept 26"). |
| **Connecting** | MS 04 (Sep 26: invite with a real thing; link page; joining ≠ friends; "Ask to be friends"; from an occasion; stop sharing). You 0-3 (Add friend sheet with its exclusion list; Requested ≡ declined; Friends sheet). | SE 04.6/04.7 (C5, sought not solicited). SE 09.6 controls. | You [F r3]. MS and SE are proposals. **Product-level primitive open** (friends vs follow). |
| **Getting together** | MS 06 B1–B6 ("Send as the plan"; conditional yes; only people who are in shown; day-of plan), C1 (optional poll), A1–A5 (With), D0/D1 (presence). | SE 03.1 host once; 03.2 guest link; 03.4 dinner page; 03.5 proposal route ([Doc] sentence 6); 03.7 arrival; 09.7 guest code (conditional). | [F-dir] principles. SE's exemplars are [F-del]. The **Occasion link is open**. |
| **Collections** | MS 08.1–08.6, 09.1–09.5, 10.1–10.4. | MS 02.3–02.4 Keep. | [F-dir] Life grammar (Sep 22). Whole-collection sharing [F-dir]. Location, default view, history access and contributor rights are open. |
| **Shared with <person>** | MS 07 (Life 07 verbatim plus Ours, her note as a post, conversations row, "been" offered, when she stops sharing). | Life 07.7/07.8 withdrawal wording; SE 08.3 pull route. | Name [F-dir]. **Four decisions unruled.** |
| **Chat between people** | MS 05.1–05.3 (bubbles; Vesper door; one-line card when something shared changes). MS 01 Q. | Chat B rules 1–3 would apply if person chats live in the Chat root. | **Thinnest.** "A chat with a person inside Vesper is proposed and does not exist." |
| **No-app / guest** | MS 02.12 (share by link), MS 04.2 (collection by link). SE 03.2/03.6/03.7/04.3/08.5. | SE 09.7 one-time code. | Proposals. The guest-identity decision proposal is only `proposed`. |
| **Take back / controls** | MS 02.9/02.10, MS 04.8, MS 03.7. SE 09.4/09.5/09.6. You 0-3 frame 4. | SE 04.9 (recipient withdrawn). | The withdrawal contract is canon (the correction contract). The sheets are proposals. Block is undrawn in You. |

### 3.2 Chat (Direction B)

- **Target:** CH pages 1–5 and 7.
  - Rules 1–14.
  - Start page: mast; at most two rows filled with live items, then items relevant to you.
  - Capsule search.
  - Single chat.
  - Rooms, with side chats folded under them.
  - The card gate and six roles.
  - Entered-from-object behaviour.
  - Returning survival.
- **Pending:**
  - B2 (page 8) and O1 (page 9) await the founder.
  - Deltas 07 and 20 await the workbench.
  - Decision 08 (retention wording, search reach, side-chat lifetime) belongs to You/Trust and the history/source-expiry proposal.
  - Decision 23 (attribution once an answer leaves Chat).
  - Six writing rules await adoption into the voice canon.
  - Booking-card retirement awaits the registry owner.
- **Not in the Chat project:** a person-to-person chat. MS 05 and You's "Message" pill both assume one.

### 3.3 You / person page

- **Target:** YOU 0-0 (nine sections, in fixed order, each conditional) plus 0-1 to 0-4, governed by the 14 rules on 0-5.
- **Missing from the target:**
  - the trust half (only on board 18);
  - where your own page is reached from;
  - the place → Places handoff;
  - the flow from Chat contribution to the thread;
  - her side of a friend request;
  - block.

### 3.4 Shared components and instruments

| Component | Canonical | Consumers | Status and gaps |
|---|---|---|---|
| **OriginalReader** 0.4.1 | WB 02A / 06 | Home, Places, Life, Social, Entity (versions vary; see §6) | The most complete. Its queue: direct original, nonspatial receiving, sender-owned states. **You retired it** for the thread entry. MS uses its own post anatomy. |
| **Ticket** | WB 02D | Life, Home, MS (a copy) | Asked for: a live variant, road mode, wristband, a 32pt chip. |
| **InviteCard** | WB 02B | SE 03, You 06 | **MS rejects it as a share** in favour of the gathering attachment. Plans keeps its own. |
| **PlaceIdentity** | WB 02C (`preview` rows only) | Places | Destination and sparse variants are extensions. The **place line** [F-dir Sep 25] is a new, unpackaged form. |
| **Notice** | WB 06 | Plans, Home, SE | Its action buttons are 36px, below the 44pt minimum. Chat withdrew the amber notice [F 09-14 ruling 21]. |
| PlaceHead, FactPair, SourceList, ActionGroup, LocationFooter | WB 02C (R2) | Entity | `ActionGroup` sits on `.vdl-door` and measures **15pt against a 44pt minimum** (You 0-5 correction). |
| **Unpackaged new parts** | MS 01/02/06/08/09 | MS only | Share post, place line, link line, gathering attachment, Keep/"With" receipt, the four-glyph verb row, audience picker, composer, collection masthead and spine (from Life 03/07). None of these is in the package. |
| **You extensions** | YOU 0-5 | YOU | PersonHead (`you-head.css`), thread entry (`you-thread.css`), place plate and rail, audience line as control, the two-layer axis. All are listed "to send back". |

**Instruments (S2), per S2-D.** Nothing is selected. What can be offered for selection now:

- **Select, as the library of nine.**
  - `S2Against` is recommended "select first". It is the smallest and has no native counterpart; build it new.
  - `S2Correction` is recommended "select second". It has no drawing at all.
  - `S2Track` adapts `DayBand`. It needs runtime label re-flow.
  - `S2Section`, `S2Sequence` (Life already renders it), `S2Level`, `S2Count`.
  - `S2Cycle`: adopt the week and year forms and hold the month grid. It adapts `WeekShape`, which Home already uses.
  - `S2Pair` as a composition.
- **Withdrawn:** `S2Change`.
- **Bench leans.**
  - Graduate: `S2Scales`, `S2Chain`, `S2Plan`, `S2WeekGrid`, `S2Dots`, `S2Curve`, `S2Ribbon`.
  - The almanac line becomes a pattern, the ledger a composition, and the table becomes candidate nine.
  - Hold: `S2Profile`, `S2Journey`.
  - Keep small: `S2Roster`.
  - The three contested circles (`S2Bearing`, `S2SunPath`, `S2DayRing`) must be decided together, in situ.
- **The print register** applies to all nine constructions or to none.

The ones relevant here:
- You's axis. You 0-5 lists as open whether `S2Track` or `S2Cycle` already is the axis.
- MS 09's dashed gap is S2's "gap row" form of absence.
- MS 08's "counts, not badges" matches the discipline of `S2Count`.
- `S2Roster` ("four dinners", no totals) could sit inside Shared with Maya.

---

## 4. Contradictions

Severity:
- **H**: blocks a coherent build, or contradicts an accepted record or shipped code.
- **M**: will cause rework.
- **L**: wording or hygiene.

| # | Contradiction | Sides (with dates) | Sev | Recommended resolution |
|---|---|---|---|---|
| C1 | **Where casual friend shares land.** Mostly resolved at 22:00 UTC Sep 26. | [Doc] 2026-09-05:<br>• casual shares go to Places · From friends;<br>• casual shares with no Place keep "a Status doorway on Home while featured, and Life People after".<br><br>MS 03 now puts place shares in Places ("agreed Sept 26"). It keeps a Home strip of "the day's posts with no place", capped at three or four, plus one line to Places.<br><br>MS 01's receiving frames (A2–D2) still show a place share (Priya's Lulu's) in a Home feed. | **L-M** (was H) | Record the Sep 26 agreement. Either treat the no-place strip as the Sep 5 "doorway while featured", or amend Sep 5 to say so explicitly. Redraw MS 01 D2 so the place share appears as the one line to Places. H1 Home builds follow Sep 5. |
| C2 | **Group conversation** | MS: "No group chat, for now" [F-dir Sep 21]; "A group is not a chat" (02). Founder Sep 22 names a third form, "Chats between people / in a group" (handoff §3.1). CH rooms and side chats are [F 09-13/14]. Code: the Trip group room with GroupVesperNote, the member-asking banner, a side-chat endpoint and public voting. | **H** | One scope ruling. Suggested: rooms exist only as an arrangement's room (CH "Saturday dinner"), owned by an Occasion or Plan. Named audience groups never get a room. Supersede the Trip-room voting grammar. Decide whether a small group chat gets the Vesper door (MS 05 open). |
| C3 | **Relationship primitive and naming** | Code: `FollowPill`, `follows.py` (live) and pair `social_circles` (on by default). You: mutual Friends [F r3 09-14, "friend / not friend. similar to instagram"]. MS 04: "Ask to be friends" (Sep 26). SE: "stay in touch" (C5 proposal). Names in use: friend, connection, stay in touch, circle, follow. | **H** | Adopt the friends-audience and ongoing-connection proposals together as one decision, "Friends": mutual, request and accept, silent decline. Decide whether Follow is retired or kept as legacy. Note that the founder's Instagram reference is a follow-with-approval model, so confirm the intent. |
| C4 | **The person has 3+ pages** | You person page (0-0, "a person page rendered for a viewer"). Life "Shared with Maya" (MS 07: "a record, not a profile… no portrait"). MS 03 frame 7 "People · Maya" (shared lately / you kept). Code: `/profile/[userId]` and `/you/circle/[id]`. | **H** | Rule one destination with explicit faces. For example: You page = the outward face; Shared with <person> = the private record, reached through a door from the You page and from Chat. Fold MS 03's People · Maya into one of them. |
| C5 | **Where the original lives / one original** | You rule 14: it "exists once, as a thread entry" [F 09-14, "Both places, one original"]. MS D4: "stays with the thing it was about". [Doc] 09-05: Life · People is the record. [Doc] 09-09: custody stays with the author's Source. Code has three IDs: source, delivery and handoff. | **H** | The original lives in the author's custody. The thread, the place, Home, Life People and the relationship record are all projections or pointers under one ID, carried from sender to recipient to Life. Record this as a decision; it is the highest-leverage identity rule. |
| C6 | **Keep: copy or pointer** | [Doc] 09-09: display grants no "independent retained recipient copy". MS 02: Keep "puts the share into your own Life", and take-back removes it (02.9). SE 08.2 and Life 07.7: "a copy to reread until she takes it back". SE 09.4: kept items stay "until it expires" (the outlier). §12.4: Keep only material "eligible for private retention". | **M-H** | One rule: Keep = your pointer plus your note. It survives expiry, not take-back (Life 07.8 and MS 02.9). Fix SE 09.4. Keep "keep the place" and "keep her words" as separate effects. Needs the scoped retention agreement (proposed). |
| C7 | **Verbs on a person's post** | MS: one like, comment, quote, keep [F-dir]. You thread: "no likes, no counts, no comment rail; a reply goes to her as a note" [F 09-12]. SE D2 acknowledgment unadopted. | **M-H** | The same object should carry the same verbs everywhere. Show likes by name to the author only, which stays within You's "no counts". Decide whether comments appear on the You thread. |
| C8 | **Naming Vesper** | CH rule 3 and ruling 19: never named, no container, faceless gold disc [F 09-13 "drop it everywhere"]. MS 01 Q and 05.2: "NORA ASKED VESPER" and "VESPER · ASKED BY NORA · TO BOTH OF YOU". SE: "Ask Vesper" buttons. Code: tab title "Vesper", `VesperSignature`, `GroupMemberAskingBanner` ("{name} is asking Vesper…"). The kernel's `vesperVoiceItalic` role. | **M** | Extend rule 3 to person and group chats: the attribution line names the asker and audience ("Asked by Nora · to both of you") beside the disc, with no "VESPER" label. Settle it with decision 23. |
| C9 | **Face of a person's words** | MS feed: sans. MS collections: serif ("one type for what is kept"). You: serif (rule 02). Chat: one sans role for everyone. Life 07: serif italic with quotation marks. | **M** | Rule it by context: live exchange in sans, held record in serif. Or unify. Tie this to the MS 11 decision. |
| C10 | **Serif candidates vs code history** | MS 11: Source Serif 4 is a "provisional preference" (§12.9); Newsreader is candidate D. `fonts.ts`: Newsreader shipped 2026-06 and was **reversed**; the mismatch is "size-and-adjacency"; ×1.2 rule; 15px floor. | **M** | Present option B (Garamond about 15% larger), which is the code's ×1.2 rule, as the lowest-risk option. Treat D as already tried. C is a canon change across Life, Places and Home. |
| C11 | **Quotation marks** | [F-dir] no quotation marks. MS 07 decision 2 still "RULED — not yet". Life 07 uses serif italics with quotes. MS 01 B3 host answers use curly quotes. You 26 and CH 7 use quotes. | L | Record the ruling; update MS 07 and send a Life 07 delta. |
| C12 | **Invitation form** | WB InviteCard (host/guest/answered) is used by SE 03 and You 06. MS 01: "not the InviteCard: as a share it read as a form", replaced by a gathering attachment. Plans keeps its own layouts. | **M** | Package the gathering attachment as an InviteCard `attachment` density, with the full invitation page behind it. Re-point SE 03.1/03.2. |
| C13 | **Place attachment** | [F-dir Sep 25]: a line, no card, no picture, no hours. Stale captions remain in MS 01 ("hours from the world"), 02 ("card… thumbnail"), 09 ("its card") and 11 ("A PLACE CARD"). The OriginalReader place line carries hours and a thumbnail; SE 02.4 draws place details inside the reader; You places are photo plates. | **M** | Fix the captions. Decide whether the OriginalReader place line conforms for social shares; place plates stay a You-page form. |
| C14 | **Voting and non-response display** | MS 06 [F-dir, "voting feels awkward"]: only people who are in are shown; "hasn't said" removed (§12.2). CH C-D6 group gate shows "You: Haven't said" and maps to `vote_widget`. The group-social charter (Jul 13, implemented): public votes, holdouts visible, voting on by default. | **H** (charter) / M (CH) | Supersede the charter's voting rulings by decision. Change the CH gate to list only answers given. |
| C15 | **Person-chat grammar** | MS 05: bubbles, "looks like every other chat". CH B: a solid chip for your turn, uncontained prose for Vesper, no bubbles; start-page rows have no person-chat type. You's "Message" opens Chat. | **M** | The Chat project owes a person-chat page. Rule bubbles vs chip for human-to-human talk, and add a person-chat row type. |
| C16 | **Selected SE exemplars vs later MS grammar** | SE 02/04 are [F-del 09-09] in SE's grammar (OriginalReader full, Places scope). MS redraws receiving as a Home post with glyph verbs. | **M** | Treat SE 02.4 and the SE guest/photo sequence as the detailed states beneath MS's share anatomy. Record which supersedes where. |
| C17 | **Homonyms** | "Ask" means a private Vesper question, an MS status, and You's one live ask. "Thread" means a Chat conversation, the Life Threads lens, MS "thread = shared record", and You's 朋友圈 thread. "Invitation" means an occasion invite, an app invite, and a friend request. | L-M | A naming pass in the voice canon. |
| C18 | **Presence vs availability** | MS 06 D "happy for company · until Sunday night". You board 28 rejected an "Open to" availability section. | L | Rule that presence exists only as a share with an end, never as a profile field. |
| C19 | **Guest identity** | MS: link page, with a proposed "Add, as Maya". SE: branch V one-time code. You: "Add friend may not be offerable to someone who arrived by link". AP: bearer rebinding (excluded by SE). | **M** | Decide the guest-identity proposal. |
| C20 | **QA anchors** | `polish-qa` `vesper-chat` points to August references; `you-portrait` to `profile-self-mature.png`. | **M** | Re-point to CH pages 2–5 and YOU 0-1 when implementation starts. Add social surfaces. |
| C21 | **Chat contract vs rulings** | Contract composer 48/r12/20 and Stop in the bar; `VesperSignature` EB Garamond; booking cards `active`. | **M** | Decide deltas 07 and 20; apply the naming ruling; retire the booking cards. |
| C22 | **You ↔ Social division** | The Sep 7 Social handoff gives "deliberate public/friend status" to Social; the You page carries a thread and a live ask. | **M** | Rule the division (You 0-5 open). |
| — | *Resolved Sep 26* | Joining ≠ connection and contacts matching (MS 04 vs SE); Keep flow (MS 02 vs MS 10); the Home state for "With"; place-share placement (C1, apart from its residual). | — | Keep the older catalogs from re-raising these. |

---

## 5. Open questions needing founder rulings

**Multiplayer Shapes**
1. Record the twelve lines of Sep 20–26 direction as a decision, or keep them as direction. MS 00 (09-26) explicitly says "not yet a recorded decision". This includes the placement agreement of Sep 26.
2. Board 07's four decisions, unchanged since Sep 21 and shown as "RULED — not yet":
   - ownership of Ours entries: each entry is its adder's;
   - quote or post (answered in effect by the "no quotation marks" direction);
   - one composer (board 01's);
   - the ledger counts only what happened.
3. Placement residual (C1): is the Home strip of no-place posts the Sep 5 "doorway while featured"? MS 03 names what would reopen placement: place shares going unseen in Places.
4. Where collections live: beside Time/Places/People, or inside them (00, 10).
5. Which view opens first: contents decide, the choice is remembered (08, 09).
6. The serif (11). Source Serif 4 is provisional, B is the code's ×1.2 rule, D was reversed in June (C10).
7. How a gathering links to an Occasion in Plans (00).
8. Group conversation scope (00, deferred; C2).
9. History access and contributor rights for shared collections (10: "proposed, not a settled policy").
10. Whether a guest can add through a link (04).
11. Whether Vesper may use friends' material (10.4, 01 "Whose context", 05).
12. Who sees who's in when the audience is "all friends" (01).
13. The Home cap: "three or four is a guess" (03).
14. Notifications: the proposal on 02/03 is otherwise undrawn.
15. Phone-number identity, link lifetime, several invitees on one link (04).
16. "With": does the third door need both people; naming non-account people or groups (06).
17. A permitted photo source. No approved photographs exist in any project.

**Social Experience**
18. Budget overruns: 41 slots against 24, and 16 comparison frames against 12. Move the ceilings or fold frames.
19. D1–D6 recommendations (SE 05/07).
20. The proposed decisions on friends audience, ongoing connection, scoped source use and guest identity (all `proposed`, 09-07).
21. The ruling on block, mute, disconnect and report.

**Chat**
22. B2: a "while you were away" hairline, or nothing (page 8).
23. O1: first open with no mast and three examples (page 9).
24. Deltas 07 and 20 (workbench).
25. Decision 08 on retention: the history/source-expiry proposal of 09-06, still unadopted.
26. Decision 23 on attribution once an answer leaves Chat.
27. Adopting the six writing rules into the voice canon.
28. Run Q1. Q2 needs a build.
29. Voice states (undrawn).
30. Onboarding reconciliation with B.

**You**
31. The relationship primitive (C3).
32. The You ↔ Social division (C22).
33. Whether a stranger reaches the page at all.
34. Retroactive widening of the visibility window.
35. Decay of lit windows.
36. Who owns "Looking for" (the retained-intention proposal).
37. Aggregate disclosure.
38. Her side of a request, and whether you can ask twice.
39. Block.
40. Guests.
41. World images: licensing.
42. The S2 axis check.
43. Where the trust half ("yours underneath") now lives.

**Shared language**
44. S2 selection: the nine; each bench lean; the print register (all or none); whether S2 becomes package 0.5.
45. The rule amendments on S2-D: two labels per *line*; a correction as the one non-dismissible instrument; a qualitative scale's stops must be observable; a mark has a side.
46. Promote the "propose permanent" roles (`sectionHeading`, `metaLine`, `supportLine`, `unitTitle`, `excerpt`) into `textVariants.ts`.
47. Publish 0.4.1 (or 0.5) to the kernel.
48. Package the MS parts (C12, C13).

---

## 6. Design debt and cleanup

**Stale or "before" copies**
- SE: `Before shared package — 02/03/05` (09-11), superseded.
- CH `record/`:
  - older `chatkit.css` and `chatkit-turns.css`;
  - `kernel/styles.css` duplicated three times across the project;
  - **two** different copies of Home 02 Persona A (`refs/home` and `refs/home-0912`).
- YOU: `kernel/styles.css` duplicates `_ds`; 35 history boards; four history-only CSS files.
- WB: `refs/` donor copies from 09-10 (for example `refs/social/02` is the pre-package Social 02).
- SE: R1–R12, frozen 09-07.

**Stale captions**
- MS 01 ARTIFACTS·PLACE ("place card… hours from the world").
- MS 02 LINK ("card… thumbnail").
- MS 11 ("A PLACE CARD"). These MS 01/02/11 captions all survived the 22:00 caption-trim wave.
- MS 01 D2 still shows a place share in the Home feed, although MS 03 now routes place shares to Places.
- MS 07 decision 2 still reads "RULED — not yet", and 07 keeps copy that §12.7 removed elsewhere ("Your account of the time shared — hers stays hers", "Write back, if you want to").
- MS 07 alone lacks the provenance footer.
- WB 05's header still says "VDL STAGE1 0.2-DRAFT".
- CH page 6's file name "Open" does not match its index title "Ruled".

**Forks of shared components**
- SE kept six presentations local:
  - the nonspatial reader with Keep;
  - the sender-owned share;
  - the photo on Home;
  - the changed arrangement for a guest;
  - arrival and the guest link;
  - attributed contributions.
- You: the thread entry, PersonHead, plates and axis.
- MS: all of its new share and collection parts, on Life 07's stylesheet.
- Chat: its own kit.
- Plans: invitation and arrival layouts.
- OriginalReader has four local reader families (object-model catalog).

**Package and version drift**
- The workbench manifest is 0.4.1, but `vdl.css` still declares `--vdl-version` 0.3.
- Social's two `print-room` SVGs are **70 bytes larger than the manifest's hashes** (consumed as stored).
- MS's `vdl-package.json` claims 0.4.1, but nine of its ten components were deleted on 09-22. Only the Ticket, copied from Life, remains.
- Consumers by version:
  - Social: 0.4.1 (09-11)
  - You: 0.4.1 (09-13)
  - Home: 0.4 reader, with the metadata patch pending per §22
  - Places: 0.3 reader cards
  - Life: 0.3 retrieval reader
  - Entity lab: **0.3** (board 16 stayed on 0.3; memory note)
  - Chat: `vdl.css` only

  As §22.1 notes, a different version is not automatically drift: a retrieval-only reader does not need 0.4.
- The kernel's `_ds_manifest.json` dates from 07-25. The package is "not published to the Production Kernel".

**Measured defects not yet fixed**
- `ActionGroup` is 15pt tall against a 44pt minimum.
- Notice buttons are 36px.
- The You larger-text pass has not been re-run.
- `vdl-port` has not been run on YOU 0-1.

**Placeholder photos**
- Every MS and SE plate is a riso placeholder or labelled stand-in: "No approved photographs exist yet in any project".
- You's world images are fixtures with unresolved licensing.
- The value of friends' originals has never been judged against real pictures.

**Uncommitted design-generator files in the workspace**
- Modified: `design-gen/multiplayer/README.md`, `build_all.py`, `mp_common.py`, and `gen_s1`, `gen_s2`, `gen_s4`, `gen_s6`, `gen_s8`, `gen_s9`, `gen_s12`, `gen_s13`, `gen_s14`, `gen_s15`, plus `heights.json` and `paths.json`.
- **Untracked:** `gen_idx.py` (the generator for board 00), `gen_t1.py` (board 11), `gen_cards.py`.
- Also uncommitted: handoff §12 and response §8.
- The generators depend on a copied `../social/hp/` kit.
- The README warns that the old `gen_00` writes a stale "00".
- Home's `gen_live*.py` files are also untracked, but out of scope here.

**Kernel vs code**
- The export check cannot run (`tsc` missing).
- The kernel documents 9 of 113 components.
- `serifBodySm` (13px) sits below the code's serif floor.

---

## 7. Per-surface design completeness and build distance

"Designed" means drawn with states. "Thin" means drawn once or only as a proposal. Build evidence is spot-checked (catalogs and code at `23cff76f4` / `fdf789d06`).

| Surface | Designed well | Thin or missing | Build today |
|---|---|---|---|
| **Share composer** | Four kinds written (MS 01); audience picker; link; "With"; presence; preview and result (SE 09.2–09.3); share from the object (SE 02.2); photo set (SE 10) | Composer choice unruled; creating a named group; editing a sent share (only "Edit keeps comments"); drafts; errors beyond SE 09; large text; notifications | Only exact original → one account (`RELATIONSHIP_UUID_HANDOFFS_ENABLED`, off by default) and the dark place handoff. No composer. |
| **Receiving** | Post anatomy × 4 (MS 01); week on Home (MS 03); Places scope and opened original (SE 02.3/02.4); photo arrival (SE 04.2, 10.3); withdrawn states; see less; quiet day | The like as the receiver sees it; comment threads beyond one reply; recording the Sep 26 placement agreement; empty and sparse Places scope at real density; report flow | Home v2 `PEOPLE_ORIGINAL_DELIVERY` and `/original-delivery/[id]` (gated); the legacy Places `socialCard`. |
| **Connecting** | MS 04 (8 frames); You 0-3 (4 frames); SE C5 both sides; controls (SE 09.6) | Her side of a request; asking twice; block (You); guest-to-account merge; identity (phone) | Pair circles (on by default); Follow (live); `/you/people`; trip invites. No friends model. |
| **Getting together** | MS 06 (A1–A5, B1–B6, C1, D0/D1); SE 03 (8 slots) with guest code, arrival, change; CH G1–G5 | The Occasion link; changing or cancelling after "Send as the plan"; multiple dates or times; host managing plus-ones (Sam's "could i arrive with someone?" is unanswered) | Trip group room with voting (legacy, live); Occasion invitations for accounts only; guest capabilities dark. |
| **Collections** | Six compositions × two lenses; Keep → add; correction; share whole; later use | Creating, renaming, deleting or leaving; removing a contributor; the map view ("On a map" is only a door); location in Life; history policy; large text | None. No user-owned list (`entity_saves` is flat; `collections` is editorial). |
| **Shared with <person>** | MS 07 (six panels on Life 07) | Maya's side; "Manage what's shared"; the relationship ending (only MS 04.8 "stop sharing"); four decisions | None. The Together projection is backend-only and dark. |
| **Chat between people** | MS 05 (3 frames) | Chat list and entry; unread and notifications; media; group; Vesper permission sheet; person-chat rows on the Chat start page | `relationship_pair_conversations` backend; group chat UI (legacy). |
| **Chat (B)** | Start page, rows, search, single chat, rooms and side chats, header, composer, six card roles, entered-from, returning, first open, large text, offline | Voice states; native accessibility (a "HIGH risk"); retention wording; attribution; deleting chats; person chats | Concierge tab; `chatTranscript` 16/26 implemented; Vesper still named; composer per contract; history search over titles only; side-chat backend; 20 card renderers; booking cards active. |
| **You / person page** | Nine sections × self/friend/anyone/unavailable; Add friend, Requested, Friends sheets; per-entry audience; removal; axis grant; window | The trust half; block; her side of a request; stranger reach; the entry point to your own page; place → Places; Chat → thread; stress cases (a 200-occasion record, a long name) | Aug portrait `/you`; `/profile/[userId]` with Follow, authored lines and featured places; settings hub. None of the new canon is built. |
| **Shared components** | OriginalReader (4 densities + states); Ticket (4 × 3); InviteCard (3 views); R2 set; Notice (6 tones) | Extension queue; MS parts unpackaged; You extensions; accessibility defects | No `vdl` in app code. Nearest: `ReceivedOriginalSurface`, `TicketBand`, `StateNotice`, `ActionGroup`. |
| **Instruments (S2)** | 9 constructions, 15 bench forms, 6 + 17 compositions, register study, native map, linter | Founder selection; native builds; solar model unverified; bench forms at narrow and large widths | `components/instruments` is dev-gallery only; `WeekShape` is live in Home; `DayBand` and `TideCurve` exist. |

---

## 8. Evidence boundaries

- **Board texts.** I read the MS boards as rendered text on 2026-09-26. All other projects were read from text extracted on 2026-09-25, and their etags confirm nothing changed since. I did not do a visual pixel review.
- **MS editing is ongoing.** Two write waves landed today: 18:17–21:41 UTC and 22:00–22:01 UTC. The second changed placement after my first draft of this atlas and was folded in. The second wave has no README or handback entry yet. Re-list MS and compare etags against `1790460021665043` and `1790460073134943` (board 00) before relying on §2.1.
- **Code.** Code checks were targeted greps and git diffs; nothing was run. The kernel drift tool failed with exit 2 because `tsc` is missing, so its verdict is unverified.
- **Founder provenance.** Founder words come from the boards, the dated docs and the founder's messages in Claude Code transcripts (extracted Sep 25). Where a board's caption and a doc disagree about ruled versus proposed, the more conservative label is used (§12.9).
- **What this proves.** Static drawings prove proposed paths only. They do not prove usability, demand, implemented behaviour or release readiness.
