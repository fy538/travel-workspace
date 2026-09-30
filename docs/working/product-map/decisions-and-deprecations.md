---
doc_type: working
status: active
owner: Claude orchestrator (product map)
created: 2026-09-26
expires: 2026-10-26
why_new: No single place lists every open product, policy and architecture decision blocking execution together with the canon, documents and live product concepts that now contradict the experience-centered, everyday-first, sharing-founded direction.
promotes_to: null
supersedes: []
---

# Vesper product map: decision register and deprecation list

This is a read-only inventory. It changes nothing. Every recommendation below
is the orchestrator's view and needs a founder or lane-owner decision before
anyone acts on it. Where a recommendation would amend canon, it must be recorded
as a dated file in `docs/decisions/` first, following `docs/governance/README.md`.

## 0. Basis and evidence limits

**Revisions read.**
- Workspace main checkout: `878581b` (Sep 25).
- Merged workspace main: `6ef3dca` (Sep 26, PR #36).
- Backend main checkout: `fdf789d06`. Merged backend main: `c8c9f5785` (PR #233).
- App main checkout: `23cff76f4`. Merged app main: `43225df35` (PR #201).
- Codex lane `/Users/feihuyan/travel-workspace--home-value-delivery` at `dafe508`.
  It carries the newest `docs/working/vesper-program-roadmap.md` and
  `docs/working/home-value-composition-execution-plan-2026-09-25.md`.

**Sources.** Workspace decisions, proposals, systems, release, status,
journeys, contracts and Owner Action Items; backend canon
(`travel-agent/docs/product/`); `travel-app/docs/`; the uncommitted
multiplayer design generators (`docs/working/design-gen/multiplayer/`); and the
earlier product-map catalog (`…/7e6d4384…/scratchpad/catalog/*.md`), whose code
findings I spot-checked but did not re-run.

**Boundaries.**
- Nothing was run: no code, tests, builds, databases, or Fly/EAS consoles.
- "Live in code" means reachable in a checked-in build profile, not that real
  users have it. There is no public release.
- Design "RULED" captions are not recorded decisions. The multiplayer index
  (`gen_idx.py`) itself says "Founder direction — said in review, Sept 20–25,
  not yet a recorded decision."
- The orchestrator's vision statement is partly design direction, not canon.
  D01 and D02 address that gap.

## 1. What matters this week

The decisions cluster around three hard dates.

- **Mon Sep 28:** the M1 internal target date. M1 cannot be met, and nothing
  currently says so. Decide D27.
- **Tue Oct 6 and Wed Oct 7:** eight decision proposals expire, along with the
  program roadmap (`expires: 2026-10-07`) and the v1 offer candidate. Letting
  them lapse would silently leave social, continuity and pre-Plan intention
  without any authority. Decide D04–D11 and D29.
- **H1 exit (date not set):** the active build needs three decisions to finish
  honestly: an accepted Home reference (D26), the Home social-placement rule
  (D20), and a recurring-supply trigger (D32).

**The five decisions with the most leverage:**
1. **D02:** record the Sept 13–25 founder design direction as decisions. It
   unblocks most of the deprecations in Parts B and C.
2. **D04:** adopt the retained intention and Life AHEAD. This gives the arc's
   "wanted" stage an owner.
3. **D15:** settle the friend's original. It should be one identity, a pointer
   rather than a copy, with a take-back rule.
4. **D08, D09 and D17 together:** Friends is the relationship and the audience.
   Retire Follow.
5. **D27:** retire M1 as the governing milestone and rebase Owner Action Items.

---

# Part A — Decision register

## A.1 Register

Class key:
- **P** = pending proposal.
- **U** = unowned object.
- **I** = identity rule.
- **S** = social structure or placement.
- **H** = Home, Chat or Live surface policy.
- **C** = company.
- **R** = ratification of founder direction or delegated work.

Deciders: **F** = founder; **F+L** = founder with the named lane owner;
**L** = lane or engineering owner, no founder policy needed.

| ID | Decision | Class | Deadline | Blocks | Recommendation (short) | Decider |
|---|---|---|---|---|---|---|
| D01 | Make the Experience and its arc canonical | R | This week, before any canon amendments | Every amendment in Part B | Record the arc as the lifecycle lens under the four moves. No stage is mandatory. | F |
| D02 | Record the Sept 13–25 design direction | R | Before Oct 7 | Retiring group-social voting, Follow and facilitator canon | Record one dated decision covering social, Chat and Live Home | F |
| D03 | Ratify or reject delegated selections | R | Before any of them become build requirements | Plans and You build | Ratify the You rules that set policy (11, 13, 14) and the Sep 9 sentence-6 door. List the rest as design-only. | F |
| D04 | Retained intention before a Plan, plus Life AHEAD (R1–R6) | P/U | Oct 6 (proposal); Oct 4 (Life docket) | Life AHEAD, Home cues, Plans loose Saturday, "wanted" stage | Adopt both as written. The owner is the experience-graph domain. | F+L (Components & Plan, Life) |
| D05 | Conversation history, source expiry and continuity | P | Oct 6 | Chat search, side-chat lifetime, the "returns" stage, moat proof 4 | Adopt §2 (Sept 7) as policy: prospective opt-in, no backfill, sensitive exclusion. Build after the CC-2 copy inventory. | F |
| D06 | Scope of assistance instructions | P | Oct 6 | Home "shorten"/"fewer decisions today"; Chat redirects | Adopt cases 1–3 now. Defer case 4 (standing default) until D05. | F |
| D07 | Life Outcome audience compare-and-swap | P | Oct 6 | Serving shared Outcomes in Life | Promote the writer contract to a decision record. Serving cutover stays an engineering gate. | L (Life) |
| D08 | Friends audience | P | Oct 7 | Composer audience, Places `From friends`, You page | Adopt. Friends = the author's chosen connections, frozen at Send. No second roster. | F |
| D09 | Ongoing connection default | P | Oct 7 | Friends pill, block/mute, invites | Adopt mutual connection as "Friends". Block immediate. No contacts import. | F |
| D10 | Guest identity and delivery | P | Oct 7 | Guest link pages, gathering invites, the growth loop | Adopt safe preview without an account plus a recipient-bound one-time code at the first sensitive boundary. No bearer rebinding. | F+L (Invites/Trust) |
| D11 | Scoped source-use grant (AI use of a friend's material) | P | Oct 7 | Collection later-use, Asking about a friend's note, a two-person chat's Vesper door | Adopt the immediate-private-question grant via an author-level setting, default off. No per-post checkbox. | F |
| D12 | Collections ("Kept") owner and Life placement | U | Before any collection build; target Oct 7 | Social boards 08–10, Life, Places lists | One user-owned list owner, extending saves. Lives in Life as "Kept". Shared whole only. | F+L |
| D13 | Owner of a thread or curiosity pursuit | U | With D12 | Life Threads lens, "Getting pasta right" | **Revised Sep 26 evening, see D13 detail.** AI-proposed threads (2-context gate, one-tap accept); intersections computed from shared members; actions only from intersections. Supersedes the earlier "retire the word" recommendation. | F+L |
| D33 | One artifact type contract for everything sent to Vesper | U | Before any send/organize build (F0) | F0, threads, Life, Home units, the agent's "hands" | One canonical typed shape for every send (place, screenshot, ticket, menu, photo, a friend's text), with an optional one-tap judgment and an instant counted payoff. Today there are 8+ vocabularies; the typed grammar (15 source kinds × 5 families) expired 09-20 unpromoted. | F+L |
| D34 | A send with a question keeps the send | I | Before F0 | Share + question = Ask (T0, nothing kept) conflicts with "send + optional question" | Amend Contribution & Consequence: a deliberate send is Bring (T1, private by default) even when it carries a question. The question itself stays answer-only. | F |
| D14 | Home for the "ahead" stage | U | With D04 | Life Time, Home, Plans | Life Time AHEAD with two degrees (arranged / kept softly). No fifth lens or tab. | F (via D04) |
| D15 | Friend's original: where it lives, keep = copy or pointer, take-back reach, one id | I | Before Social or Life serving; target Oct 7 | Life `social_contribution` owner, Keep, withdrawal, OriginalReader | Source owner keeps custody. One id (the source). Keep is a pointer bound to the grant. Take-back removes it from others' keeps; recipients' own words stay. | F+L (Relationships, Life) |
| D16 | Trip ↔ Plan/Occasion link; gathering ↔ Occasion | I | Before Package 2 or any Plans rebuild | Life ingestion of Trips, gatherings, M1 remnants | Trip becomes a Plan specialization by an explicit link. A gathering attachment creates or links one Occasion. | L (Components & Plan) with F sign-off |
| D17 | Follow vs mutual friends | S | Oct 7 (with D09) | You page, profiles, `v1-scope` social-profiles | Retire the user-facing Follow. Friends only. Keep the `follows` table read-only until migration. | F |
| D18 | What a group is; group chat vs rooms; group history | S | Oct 7 | Chat rooms design, Trip room, collections | A group is a named audience. No new group room. The legacy Trip room is frozen and answers only when addressed. History: audiences forward-only, collections whole. | F |
| D19 | Voting default | S | With D02 | Trip room, proposals, stay votes | Polls only when a host asks. Remove Vesper-emitted votes. No public holdouts. | F |
| D20 | Placement conflict: Sep 5 social split vs Home "From friends" rows | S | Before H1 exit | H1 active build, MS 03, Home 03 | Keep the Sep 5 split. Home holds addressed material and human-opening joins only. No generic friends section. | F |
| D21 | Does a contributor learn their share helped? | S | Before any receiving build | Social receiving, Home receipts | No automatic viewed/used/helped signal. Only human acts (like, reply, a sent "it helped"). | F |
| D22 | Social notification defaults | S | Before push is enabled | Push, invitations | Invitations, replies to your share and answers to your ask notify. Statuses, places and links never do. | F+L (Notifications) |
| D23 | Vesper naming: Chat ruling 19 vs "Ask Vesper" doors | H | Before Chat or root-door builds | Chat chrome, root doors, `GroupMemberAskingBanner` | The name labels the door, never the answer. Unsigned answers, no avatar. | F |
| D24 | Live Home adoption (lane D + coupon T2, Sep 23) and live posture | H | Before H1's live situation is accepted | H1 case 3, VDL dark Ticket | Record lane D + T2. Live still requires a held commitment. "New city, no plan" = Available with a place card (board 24). | F |
| D25 | Live service promises ("ends at boarding"), Monitor owner, push | H | Before any "we'll tell you" copy ships | Live Home, "Follow this for me" | Don't ship notification promises until a Monitor owner, provider feed, verified push and failure copy exist. | F+L (Live engine) |
| D26 | Accepted design reference for Home (`designRefs: []` on main) | H | Before H1 exit | H1 acceptance ("accepted design reference") | Accept a named, scoped set: 02/03, 18 K, lane D/T2 exemplars. Home 03 note-first is not adopted. | F |
| D27 | M1 fate (Sep 28 target, PearX Oct 4) | C | **Sep 28** | Owner Action Items, journeys, proofs, `v1-scope` | Retire M1 as the governing milestone. Archive with disposition. Decide PearX separately using H1 evidence. | F |
| D28 | Brand: Vesper vs Hermene/Oivaro | C | Before any external surface | Copy, domains, Chat naming | Supersede the Hermene working-brand decision. Vesper stays until a cleared naming review. | F |
| D29 | Membership/pricing and the v1 offer candidate | C | Oct 7 (offer expiry) | Paywall, `COMMERCIAL_*`, offer copy | No price now. Adopt the §7.4 free/paid boundary as principle. Commercial checkpoint after Package 2. | F |
| D30 | Launch geography (NYC) | C | At H1 exit (Package 2 selection) | Recurring supply, Places depth | NYC founder cohort, Brooklyn-first supply, as an internal cohort, not a public launch | F |
| D31 | Four-root shell cutover; retire the trip-first Plans tab | H/C | Define criteria now; cut over after H1 | Deprecation of trip-first Home | Set cutover criteria: H1 exit, Life v1 acceptance, governed Places, push verified | F+L |
| D32 | Recurring Home supply trigger (Source worker cohort, ambient production) | H | Before H1 exit claims production value | Home in production | Allow a bounded, person-independent scheduled preparation for the cohort area under a cost cap. No person-derived ambient generation. | F |

## A.2 Deadline calendar

| Date | What lapses or is due | Decisions |
|---|---|---|
| Sep 28 (Mon) | M1 internal target, "Demo recorded and certified" (`docs/release/m1-plan-repair.md`) | D27 |
| Oct 4 (Sun) | PearX W27 deadline; the Life unfolding docket expires (`life-unfolding-decision-docket-2026-09-04.md`) | D27, D04/D14 |
| Oct 5 | Assisted-expense brief, booking-retirement receipt and integration roadmap expire | Part C |
| Oct 6 (Tue) | Proposals expire: assistance scope, history/source, retained intention, Life Outcome CAS | D04–D07 |
| Oct 7 (Wed) | Proposals expire: Friends audience, ongoing connection, guest, source-use grant. Also the program roadmap and the v1 offer. | D08–D11, D17, D29 |
| Oct 8 (Thu) | Home design review (Live Home studies) expires | D24–D26 |
| Oct 9 (Fri) | Prepared-continuation packet expires (already resolved) | B-list cleanup |

## A.3 Decision details

### Framing and records

#### D01 — Make the Experience and its arc canonical

- **Question.** Should the orchestrator's framing become the canonical lens?
  The framing: the Experience is the center; attention is how it enters; the
  relationship compounds; the arc runs noticed → understood → shared → wanted →
  arranged → live → kept → returns.
- **Current state.**
  - Canon has the four moves (`docs/decisions/2026-08-28-adopt-four-product-moves.md`).
  - Product Model says "Experience is the human product unit", but Experience,
    Move and Moment have no tables (object-model catalog).
  - The nearest written lifecycle is research, not canon: "Noticed →
    Understood → Relevant → Feasible → Socially viable → Experienced →
    Remembered" (`docs/working/multiplayer-corpus-digest-2026-09-20/02-…md:381`).
  - The philosophy source expired Sep 17:
    `travel-agent/docs/working/the-world-is-lived-not-searched-philosophical-foundations-2026-08-18.md`.
- **Options.**
  - (a) Replace the four moves with the arc.
  - (b) Record the arc as a lifecycle lens beneath the four moves.
  - (c) Leave the arc informal.
- **Blocks.** Every amendment in Part B needs a stable reference. Otherwise
  each amendment reinvents the framing.
- **Recommendation: (b).** Add one dated decision and a short Product Model
  section with this mapping:
  - Make sense = noticed and understood.
  - Open possibility = wanted, and shared as a possibility.
  - Help it work = arranged and live.
  - Carry forward = kept and returns.

  Add the law "no stage is mandatory; most experiences stop early." Refresh or
  re-verify the philosophy document, or promote its adopted parts, and let the
  rest expire.
- **Rationale.** The four moves already carry roots, contracts and code
  vocabulary. Replacing them would force a rename across both repositories for
  no behavioral gain. The arc adds what the moves lack: an object-centered
  timeline that Life AHEAD, Live Home and returns can hang on.

#### D02 — Record the Sept 13–25 founder design direction as decisions

- **Question.** Should the founder's spoken design rulings become recorded
  decisions so canon can be amended?
- **Current state.** Three bodies of direction exist only in design projects
  and working docs:
  - **Social** (`gen_idx.py` RULED list):
    - "Sharing is the foundation. Four kinds, one set of verbs."
    - "The chat is a private chat between people. Vesper is in it only when
      someone asks."
    - "Getting together is led by conversation, not a vote."
    - "A collection is shared whole or not at all."
    - "No group chat, for now."
  - **Chat** (Sep 13–14 rulings in the chat-you catalog):
    - Vesper is unnamed in answers.
    - Six writing rules.
    - Rooms: "answers when addressed" (ruling 15 = A).
    - "Side chat".
    - The card gate.
  - **Live Home** (Sep 23): lane D and tray T2 (`home.md` H-15B, H-15C).
- The footers state that nothing is adopted. Canon still contradicts all
  three:
  - `docs/systems/group-social.md` has voting-first rulings dated Jul 13.
  - `Group Chat Facilitator.md` makes Vesper a room facilitator.
  - `Multiplayer Product Strategy.md` §6 says "Vesper's native room owns …
    proposals, votes".
- **Options.** Record all three in one decision; record them per domain; or
  keep them as design direction.
- **Blocks.** Every social, Chat and voting deprecation in Parts B and C. With
  no record, amending canon would violate the governance rule that working
  docs cannot adopt.
- **Recommendation.** One decision record,
  `2026-09-2x-record-social-chat-and-live-design-direction.md`. List exactly
  the RULED lines, the Chat rulings that set policy (19, 15, the card gate, the
  six writing rules) and lane D/T2. Mark the rest (serif, composer, "which view
  opens first") as open.
- **Rationale.** The fastest way to make canon honest. It is also low-risk:
  it records what the founder already said and changes no runtime behavior.

#### D03 — Ratify delegated selections (You page rules; Sep 9 selection)

- **Question.** Which delegated or agent-ruled selections carry product policy
  and need the founder's own ruling?
- **Current state.**
  - `docs/decisions/2026-09-09-select-design-convergence-and-prepared-continuations.md`
    is a "founder-delegated selection … not a claim that the founder separately
    inspected each resulting frame".
  - The You project's "fourteen rules" (0-5) are design rules. The founder
    answered only some questions directly: "Both places, one original";
    "Relationship first"; "Omit it; default is Nobody"; the Friends pill, r3.
- **Policy-bearing items:**
  - Rule 11, "Friends is the relationship and the audience; showing is per entry".
  - Rule 13, "A shared projection is symmetric, bounded and traced".
  - Rule 14, "One original".
  - The shape grant, default Nobody.
- **Blocks.** Plans (Sep 9) and You builds. The acceptance criteria for D08,
  D09, D15 and D17.
- **Recommendation.**
  - Ratify You rules 11, 13 and 14 and the default-Nobody shape grant.
  - Ratify the Sep 9 sentence-6 prepared-message door. It is already amended
    canon, so this confirms rather than reopens it.
  - Label every other You and Plans frame "selected design, not policy".
- **Rationale.** These rules collide with code (Follow) and with the
  proposals. Ratification removes ambiguity without reopening the designs.

### Pending proposals

#### D04 — Retained intention before a Plan, plus Life AHEAD (R1–R6)

- **Question.** Who owns "keep the bookstore in mind for Saturday"? Does Life
  show the future?
- **Evidence.**
  - `docs/working/retained-intention-before-plan-decision-proposal-2026-09-06.md`
    recommends "a narrowly typed, person-owned retained intention in the
    existing experience-graph domain, with no required Plan".
  - The Life docket (`life-unfolding-decision-docket-2026-09-04.md`, R1–R6) asks
    for AHEAD with "exactly two degrees — ARRANGED … and KEPT SOFTLY". It has
    been pending since Sep 4.
  - One architecture conflict exists. Round-3 invariant 1 says "Keeping an
    Opening creates or links a PlanItem". The docket's recommended resolution:
    the intention stays Plan-independent, and a PlanItem is created only on
    arrangement.
  - The runtime still needs a Trip (`LocalPlanScreen`) (life-plans catalog §8.1).
  - The Sep 6 decision §3 calls the proposal "directionally compatible".
- **Options.**
  - (a) Adopt the proposal and R1–R6.
  - (b) Stretch Plan: an ambient default Plan per person. The docket rejects
    this as "the funnel by the back door".
  - (c) Defer.
- **Blocks.**
  - The whole "wanted" stage.
  - Life AHEAD, Home cues ("the jazz you asked to keep in mind").
  - Plans' loose Saturday, Chat Keep readbacks.
  - The You "Looking for" section ("A want has no owner").
- **Recommendation: (a),** with the docket's resolution of the invariant-1
  conflict. Record one decision that adopts both documents, then run the
  schema review the proposal prescribes.
- **Rationale.** The life-plans catalog calls this "the keystone object".
  Without it, Chat, Life, Home and Plans each invent substitutes, which is
  exactly what the proposal warns against.

#### D05 — Conversation history, source expiry and optional continuity

- **Evidence.**
  - `docs/working/conversation-history-source-expiry-decision-proposal-2026-09-06.md`
    (14,440 words). Its §2 (Sept 7) recommends a prospective opt-in with these
    terms:
    - eligible non-sensitive text "until conversation/account deletion";
    - no age cutoff on automatic use;
    - no backfill;
    - sensitive and third-party material excluded;
    - off-with-clearing.
  - The Sep 6 decision §2 accepts the direction but explicitly not the policy.
  - `chat_images` has no custody-purpose or expiry field.
- **Options.**
  - (a) Adopt §2 as the policy.
  - (b) Adopt the older 90-day comparison (§9).
  - (c) Keep Ask/T0 only.
- **Blocks.**
  - Chat search, which is "bounded by the retention agreement" (Chat ruling 06).
  - Side-chat lifetime (Chat 16).
  - The "returns" stage and Thesis proof 4 (consequential continuity).
  - The You/Trust "decision 08" copy.
- **Recommendation: (a) as policy direction, with implementation gated.**
  First, the Contribution & Capture lane completes the copy inventory and the
  request-time denial called for in "Delivery ownership after adoption".
  Record the decision now so design and Chat can draw honest controls.
- **Rationale.** The moat and proof 4 depend on continuity, yet the offer
  makes continuity conditional (vision catalog, contradiction 1). Leaving it
  unadopted keeps the moat outside the product.

#### D06 — Scope of assistance instructions

- **Evidence.** `assistance-instruction-scope-decision-proposal-2026-09-06.md`
  defines four scopes: this response; a named surface and period; a named
  episode; an ongoing default. The 09-09 selection includes a local Home
  "shorten" control.
- **Blocks.** Home "fewer decisions today"; Chat redirect acknowledgments.
- **Recommendation.** Adopt cases 1–3 now. They are ephemeral or bound to an
  owner, and add no durable personal state beyond a scoped instruction. Adopt
  case 4 (a standing default) only together with D05, because it is a durable
  preference.
- **Decider.** Founder.

#### D07 — Life Outcome audience compare-and-swap

- **Evidence.** `life-outcome-audience-cas-decision-proposal-2026-09-06.md`
  reports:
  - "Contract accepted for the Life writer, but not a serving cutover."
  - Commits `66f378fc1`, `ba9463c2a`, `fd66f9f1f`, `329060a88`, `afb13c6fa` landed.
  - PostgreSQL race proofs remain.
- **Recommendation.** No founder policy is needed. Promote the writer contract
  into a decision record or Life contract before Oct 6 so it does not expire as
  a "proposal". Keep serving behind the race-proof package, and keep
  `supports_delta_delivery` false.
- **Decider.** Life lane.

#### D08 — Friends audience

- **Evidence.**
  - `friends-audience-decision-proposal-2026-09-07.md`: "Friends is a sharing
    choice, not a second invitation workflow"; audience "frozen" at Send; later
    connections do not gain old shares.
  - The founder's You r3 ruling (09-14) matches: "message, and friend / not
    friend. similar to instagram".
- **Blocks.** Composer audience pill (MS 01), Places `From friends` scope,
  You thread entries, Home "Addressed to you".
- **Recommendation.**
  - Adopt as written.
  - Choose the proposal's "clear reusable audience choice" as the default UI.
    Per-send selection stays available.
  - Keep the six acceptance cases as the definition of done.

#### D09 — Ongoing connection default

- **Evidence.**
  - `ongoing-connection-default-decision-proposal-2026-09-07.md`: mutual,
    explicit contact; "Receiving an invitation, joining dinner, enjoying a
    photo and creating an account never establish the connection by
    themselves." Block is immediate, with no ladder.
  - Conflict: MS 04 says "Joining from someone's link connects you" and asks to
    match contacts once. SE 09.1 says "No contacts import".
- **Recommendation.**
  - Adopt as written.
  - Name it **Friends**. This is D17.
  - Reject MS 04's auto-connect and contact matching.
  - Block must ship with the first social exposure.

#### D10 — Guest identity and delivery

- **Evidence.**
  - `guest-identity-and-delivery-decision-proposal-2026-09-07.md` withdrew the
    earlier "exact address after answering" rule. It compares a recipient-bound
    verification step against bearer links.
  - Code: `/guest/{token}` backend-only and dark; no `app/guest` route.
  - Design conflict: MS link pages have no verification; SE uses branch V (a
    one-time code); AP uses bearer rebinding (social catalog, conflict 10).
- **Blocks.** Sam's guest view (Live Home 20.5), MS 04 link pages, gathering
  invites, the growth loop that Growth Strategy relies on.
- **Recommendation.**
  - Safe preview without an account.
  - An attributed answer is allowed as bearer, but labelled unverified.
  - The first sensitive disclosure (address, door code, photos later) requires
    a recipient-bound one-time code.
  - Never auto-rebind a link to an account.
- **Rationale.** Forwarded links are the normal case for dinners. Treating
  possession as identity leaks addresses.

#### D11 — Scoped source-use grant (AI use of a friend's material)

- **Evidence.**
  - `scoped-source-use-grant-decision-proposal-2026-09-07.md` separates three
    capabilities: original display, independent world context, and
    recipient-specific composition. It proposes an immediate private-question
    grant and leaves acquisition open (a reusable agreement vs per-share).
  - The Sep 9 decision adopted display only.
  - MS open: "Whether Vesper may use a friend's material to answer a question
    (10)".
  - Social catalog open 8: "Whose context Vesper may use in a two-person chat".
- **Blocks.**
  - Collection later-use ("Which of these would suit?" answered in friends'
    words, MS 10).
  - Side chat about a friend's note ("Ask about the sauce… Maya sees nothing").
- **Recommendation.**
  - Adopt the immediate-only grant.
  - Acquire it through one author-level setting, "Friends can ask Vesper about
    what I share", **default off**, changeable per share.
  - Quoting a friend's words verbatim with attribution in the answer is allowed.
    Paraphrase and retention are not.
  - Composition on Home or Places stays out of scope.
- **Rationale.** This honors "friends' exact words stay theirs". It also
  enables the one later-use experience the social design depends on, without
  per-post homework.

### Unowned objects

#### D12 — Collections ("Kept") owner and Life placement

- **Evidence.**
  - No backend owner. `collections` is editorial only, and `entity_saves` is
    flat (object-model catalog §1.7).
  - Product Model has no Collection noun and warns against "a universal table".
  - Design: MS boards 08–10, "A kept collection opens like everything else in
    Life". Proposed: "Keep is private and immediate… adding to a collection is
    a second, optional step". Founder direction: "A collection is shared whole
    or not at all."
  - Open: "WHERE COLLECTIONS LIVE — Beside Time, Places and People in Life, or
    inside them" (`gen_idx.py`).
- **Options.**
  - (a) Extend the Save owner with user-owned named lists.
  - (b) A new Life-owned collection owner.
  - (c) Reuse editorial `collections`.
- **Recommendation: (a).** One user-owned list owner that extends saves.
  - A shared collection is an audience grant over the whole list.
  - Participation is additive: "nobody edits or removes another person's".
  - Life presents it under a "Kept" entrance, not a fifth lens.
  - Reject (c): it would mix editorial authority with personal custody.
- **Deadline.** Before any collection code, and preferably with D08 and D09.

#### D13 — Owner of a thread or curiosity pursuit; retire "thread"

- **Evidence.**
  - "Thread" has five meanings in code: `atlas_threads`,
    `collections.kind='thread'`, `LifeLens.THREADS`, `trip_cross_trip_threads`,
    `next_thread`.
  - There is no "curiosity thread" object (current-state notes, life-you-social:60).
  - The design bans the word in the UI.
  - "Getting pasta right" is drawn as a private collection.
- **Original recommendation (superseded).** Fold pursuits into D12. A private
  collection with mixed material is a pursuit. Rename the Life Threads lens to
  the D12 entrance. Record "thread" as a retired product noun.
- **Revised recommendation (Sep 26 evening).** This follows the founder's
  direction in a parallel session that day:
  - The pipeline is send, then a standard artifact, then organization into
    threads of your life, then agentic actions.
  - Threads are central, not retired.
  - Life should lead with AHEAD plus threads.

  Recommend:
  - Build **AI-proposed threads**. A thread needs evidence from at least two
    contexts. You accept one with a single tap.
  - A thread is a line. **Intersections** are computed from shared members.
    **Actions come only from intersections**: an offer that expires.
  - Keep: no identity inference, no emotional naming, friends' audience rules.
  - Voice: opinionated about connections and usefulness, silent about meaning.
    Limit frequency, not confidence.

  This needs a four-root §6.4 amendment and D33. The "thread" word collision in
  code (five meanings) becomes a naming task, not a reason to drop the concept.

#### D14 — Home for the "ahead" stage

- **Recommendation.** Decide through D04: Life Time's conditional AHEAD, with
  two degrees and no overdue state.
  - Home carries only a timely cue.
  - Plans carries arranged items.
  - There is no "Upcoming" tab and no intention dashboard (docket R1).

### Identity rules

#### D15 — The friend's original: one identity, pointer not copy, take-back reach

- **Evidence.**
  - Contract and the Sep 9 decision: "Recipient display is not a copy: no
    retained recipient copy, no AI use, no onward distribution."
  - The designs conflict:
    - Life 07.7 "Keep a copy" and SE 08.3: "KEPT FROM NORA · YOUR COPY" as two rows.
    - MS 02: take-back removes it from others' kept things.
    - SE 09.4: a keep "stays with her until it expires".
    - Life 07.8: a copy survives expiry but not revocation.
  - You rule 14: "exists once … a pointer, and goes when the original goes".
    The founder: "Both places, one original".
  - Code has two Life ids for one original: `source.{submission_id}` and
    `original.{source_object_id}`. The delivery route keys on `delivery id`.
    The `social_contribution` Life owner is UNAVAILABLE (object-model and
    life-plans catalogs).
- **Options.**
  - (a) Pointer only.
  - (b) Pointer by default, plus an author-granted "permitted copy".
  - (c) Recipient copy on Keep.
- **Blocks.** Life serving of friends' material. Social Keep. Withdrawal
  semantics on Home, Life and Places. The OriginalReader "withdrawn" state.
- **Recommendation: (a) now, and leave (b) as a later explicit author grant.**
  - Canonical id is the source object. Deliveries and shares reference it;
    Life projects by source id only.
  - Keep = a pointer bound to the delivery grant.
  - Take-back removes the item from every recipient's Home, Life, collections
    and Places. The recipient's own replies and notes stay theirs.
  - Expiry and take-back behave the same for pointers.
- **Rationale.** This is the literal meaning of "friends' exact words stay
  theirs". It also removes the "most likely real identity fork" the object-model
  catalog identifies.

#### D16 — Trip ↔ Plan/Occasion; gathering ↔ Occasion

- **Evidence.**
  - Product Model: "Trip = specialized Plan", but code has "Trip is unlinked to
    any graph Plan" (object-model catalog).
  - Legacy Trips reach Life only as Atlas timeline rows.
  - MS open: "How a gathering links to an occasion in Plans".
  - M1 Act 4's open ruling on "exact-roster equality".
- **Recommendation.**
  - Record that a Trip is a Plan specialization linked by an explicit
    `plan_id` relation. Migration is an engineering plan.
  - A gathering attachment on a share is the front door of exactly one
    canonical Occasion. It creates or links that Occasion.
  - Companion scope stays exact-roster until outcome evidence justifies
    widening.
- **Decider.** Components & Plan lane, with founder sign-off on the gathering
  rule.

### Social structure and placement

#### D17 — Follow vs mutual friends

- **Evidence.**
  - Code ships Follow: `follows.py`, `FollowPill`, follow suggestions,
    `follow_affinity` ranking. `v1-scope.yaml` includes the capability
    "Profiles, people search, follow, and following" as `in`.
  - The Relationship Edge Decision Note (Aug 7) keeps `follows` as the
    interest edge.
  - Multiplayer Strategy §5 lists Follow as a signal.
  - The founder's You r3 ruling, the ongoing-connection proposal and the MS
    kill list ("Upvotes, counts, follower graphs… KILLED Sep 2") all reject
    public following.
- **Recommendation.**
  - Retire user-facing Follow.
  - Friends (pair circle owner) is the only relationship.
  - Keep the `follows` table read-only for ranking until a migration decides
    whether any taste signal survives. Do not convert follows into friendships.
    The Relationship Edge note itself forbids that.

#### D18 — What a group is; group chat vs rooms; group history

- **Evidence.**
  - "No group chat, for now" (Sep 21).
  - The founder's Sep 22 third form: "Chats between people / in a group"
    (threads handoff §3.1).
  - Chat design draws rooms with "Vesper answers when addressed" (ruling 15)
    and side chats.
  - The shipped Trip group room is 1,908 lines, with votes and
    `compose_group_message`.
  - Group history: board 12 says "forward-only"; collections show "everything,
    including what came before them".
- **Recommendation.**
  - A **group** is a named audience (a list with a name) or the participants
    of one Occasion.
  - No new persistent group room.
  - Two-person private chat is allowed (the pair conversation exists).
  - Replies attach to a share or an item.
  - The legacy Trip room is frozen: no new features, Vesper answers only when
    addressed, and it is retired with the four-root cutover (D31).
  - History: joining an audience is forward-only; joining a collection shows
    the whole collection, because it is shared whole.
  - Revisit group chat only through an explicit decision.

#### D19 — Voting default

- **Evidence.**
  - The founder: "Voting feels awkward and should not become the default
    grammar for gathering" (threads handoff §2).
  - `group-social.md` Jul 13 rulings:
    - "names on choices, holdouts visible";
    - "visible voting defaults ON for trips with ≥2";
    - Vesper-created `vote_widget` (current-state notes, chat:188–197);
    - stay-candidate votes.
- **Recommendation.**
  - A poll is an instrument a host asks for. It is off by default and never
    inserted because a conversation contains alternatives.
  - Remove Vesper-emitted vote widgets.
  - Stop public holdout displays ("only people who are in are shown").
  - Accept/decline on an exact change proposal is a decision, not a poll, and
    stays.

#### D20 — Social placement conflict: the Sep 5 split vs Home "From friends" rows

- **Evidence.**
  - The Sep 5 split (`docs/decisions/2026-09-05-amend-home-composition-canon.md`)
    sends casual sharing to Places `From friends`. Home holds only "directed
    and shared-consequential" material.
  - The Sep 6 decision §5: "this refinement does not move casual spatial
    sharing from Places into Home."
  - Friends proposal case 6: "ordinary place sharing does not duplicate the
    Places field on Home."
  - The designs pull the other way:
    - MS 03 draws Home "From friends" compact rows, and MS 03 notes the cap is
      "a guess".
    - Home 03 has a note-first opening.
    - Board 26: "A friend does not get a section. She gets a line inside the
      world."
  - H1 records that "The Home 03 note-first opening is not an adopted
    placement decision."
- **Blocks.** The H1 social situation. Implementation is live now.
- **Recommendation.** Keep the Sep 5 split. Home carries:
  1. material addressed to you (the `Addressed to you` region);
  2. the recovered **human-opening join**: a friend's note fused with a world
     opening Home already admitted (`home_human_openings.py`), ranked by
     situation, not by person;
  3. the featured non-spatial Status exception already in canon.

  There is no generic "From friends" section on Home, only the pull door to
  Places.
- **Rationale.** Board 26's line is the best expression of the vision, and it
  is exactly the human-opening join. A per-person row list is a feed by
  another name.

#### D21 — Does a contributor learn their share helped?

- **Evidence.**
  - The prominence brief allowed it. The social brief bans viewed/used reports
    (social catalog open 17).
  - Friends proposal case 4: "Maya receives no viewing/Keep report."
  - Home board 26 asks: "Does Dara know her note is on your Home with her name
    on it?"
- **Recommendation.**
  - No system-generated viewed, kept, used or helped signals, and no reports
    of private Asks.
  - The contributor learns only through human acts: the ruled "like", a reply,
    or a one-tap "Tell Maya it helped". That tap prepares an editable message
    the recipient sends.
  - The author's own page may say where a share is *eligible* to appear
    ("friends may see this on Home or Places"). It never says where it
    *appeared*.

#### D22 — Social notification defaults

- **Evidence.** Undrawn. The MS proposal: statuses, whereabouts, places and
  links never ping; invitations, comments on your own share and answers to
  your ask do. Push delivery is unverified (`EXPO_PUSH_ENABLED` is not in
  `fly.toml`).
- **Recommendation.** Adopt the MS default under existing caps (4 interruptive
  per day). Decide it before enabling push for any social kind.

### Chat, Home and Live policy

#### D23 — Vesper naming (Chat ruling 19 vs "Ask Vesper")

- **Evidence.**
  - Chat ruling 19 (09-13): "Vesper is not named and has no container…
    drop it everywhere." Writing rule 1: "Never say its own name."
  - Other projects label doors "Ask Vesper":
    - Plans 08 pill;
    - Places "Ask Vesper to read up";
    - Life 05;
    - MS 13's gold spark "ASK VESPER".
  - Code: `VesperSignature`, `GroupMemberAskingBanner` ("{name} is asking
    Vesper…"), and a history kicker of "Vesper".
  - Open 23: attribution once an answer leaves Chat.
- **Recommendation.**
  - **The name labels the door, never the speaker.** "Ask Vesper" stays on
    entry points; answers are unsigned, with no avatar, signature or
    self-reference.
  - An answer that leaves Chat is attributed as "asked by Nora" (MS
    convention), not "Vesper said".
  - Re-evaluate the door label under D28.

#### D24 — Live Home adoption (lane D + coupon T2, Sep 23) and live posture

- **Evidence.**
  - Founder-chosen "lane D 09-23": the object itself goes live, drawn dark
    with a torn stub and pulse.
  - Founder-chosen "T2 coupon and ink/cream". "The coupon holds one to four
    fitting items; it appears only when something fits and is absent in a rush."
  - Board 24 quadrants were explored but not selected. For "Unfamiliar, no
    plan" they propose a place card instead of a map: "Maps stay in Places."
  - The Home contract's Live posture requires a healthy canonical commitment.
    The vision catalog notes "Presence or 'no plan' has no posture".
  - The dark live Ticket stock is "a requested shared variant, not built".
- **Blocks.** H1 case 3 (the healthy live/travel day) and the VDL Ticket variant.
- **Recommendation.**
  - Record lane D + T2 as Home's live visual grammar (via D02).
  - Keep the posture law: Live requires a held commitment (ticket,
    reservation, Occasion).
  - Adopt board 24's quadrant rule. "New city, no plan" is Available with a
    place card, never a live map or a presence inference.
  - Adopt per-item offline degradation as a principle only.

#### D25 — Live service promises ("ends at boarding"), Monitor owner, push

- **Evidence.**
  - Board 21.1 draws "Gate and delay changes · Told to you here and by
    notification, until you board · YOU ASKED · ENDS AT BOARDING". That is a
    "Follow this for me" responsibility.
  - The Sep 6 decision §3 requires a "supported subject/condition, sources,
    checking window, permitted treatment, stop and failure behavior".
  - Wave 0 §2.10 defers the Monitor owner.
  - Push is unverified.
  - The H1 plan forbids a "durable watch" being added to fill Home.
  - The Sep 23 review: "'Available on Home' is not 'I will notify you'."
- **Recommendation.** Designs may keep the frame. No product copy that
  promises notification ships until all four hold:
  1. an adopted Monitor owner;
  2. a supported provider feed for the subject (flight status is not
     integrated);
  3. verified push delivery with a device receipt;
  4. failure copy.

  Until then, Live Home shows "last checked" facts only.
- **Decider.** Founder (service policy) with the live-engine owner.

#### D26 — Accepted design reference for Home

- **Evidence.**
  - Main has `designRefs: []` for `home-root` (`travel-app/scripts/polish-qa/surfaces.mjs`).
  - The Codex lane registers two first-viewport L0 references (Home 02/03)
    with `judgeAgainst: 'doctrine'`.
  - H1 requires "native comparison to the accepted design reference".
  - Board 18 K/L is selected for photos.
  - Home 02's "Today, in order" has no producer contract
    (`RootCompositionSequenceStep` has no time field).
  - Home 03's note-first opening is not adopted.
- **Recommendation.** Accept a named reference set in the home-root contract,
  scoped to hierarchy and treatment, not content or placement:
  - Home 02 (ordinary) and Home 03 (post-return), from the 09-09 selection;
  - Home 18 K for the photo-integrated full scroll;
  - Live 19.1, 20.3/20.7 and 21.1–21.3 under D24.

  State that note-first placement is not adopted (D20). Record "Today, in
  order" as a capability dependency, not a visual requirement.

#### D32 — Recurring Home supply trigger

- **Evidence.**
  - H1: "Ordinary Home reads consume prepared Source results without
    generating/enqueueing work… Recurring useful supply must therefore be
    traced, not assumed."
  - The roadmap's pending gate: "worker registration with a controlled cohort".
  - The Sep 6 decision §4: "Rich Home value must not require bespoke
    generation on every visit."
- **Recommendation.**
  - Authorize a bounded, person-independent scheduled preparation for the
    cohort's supported area (D30), for example public-world readings for
    Brooklyn places, with a daily cost cap.
  - Person-derived ambient generation stays off until D05.
- **Rationale.** Without this, H1 can prove presentation but never production
  value.

#### D31 — Four-root shell cutover (retire the trip-first Plans tab)

- **Evidence.**
  - `utils/productSystemRollout.ts` needs four EXPO_PUBLIC flags that no EAS
    profile sets. The posture is therefore "legacy" in every profile, and the
    default first tab is Plans (`TripsHomeBody`) (current-state catalog §1).
- **Recommendation.** Record cutover criteria now:
  - H1 package exit, with the accepted reference (D26);
  - Life v1 native acceptance;
  - governed Places parity for the default Places reads;
  - verified push, or explicitly no push promises.

  After that, retire the Plans tab as root (see C5).

### Company

#### D27 — M1 fate (Sep 28 internal target, PearX Oct 4)

- **Evidence.**
  - `docs/release/m1-plan-repair.md` was last verified Aug 13. Act 1 (P07) and
    Act 3 (P05) are "dark", and no device receipts exist.
  - It contradicts:
    - the seven sentences: Act 1 has Vesper proactively propose a repair,
      while sentence 6 says it "recommends when asked, or once" and allows no
      button beyond the prepared-message door;
    - voting demotion: Act 3 needs "two-observer vote recovery";
    - everyday-first: Act 4 "Ends on a mutually accepted local Plan", while
      canon now lets a share end at enjoyment.
  - The Sep 25/26 roadmap does not mention M1.
  - `Owner Action Items.md` (including the Sep 24 CI refresh on merged main)
    still says "M1 — Plan Repair owns current engineering priorities".
  - The founder archived the August fundraising packet, including the PearX
    W27 drafts and demo plan, as "historical references" on Sep 23
    (travel-agent `0aaa2ccc4`).
- **Options.**
  - (a) Run M1 to the date.
  - (b) Retire M1 and archive it with a disposition.
  - (c) Re-scope M1 to an H1 demo.
- **Recommendation: (b)** on or before Sep 28:
  - Archive `m1-plan-repair.md` and Demo Journey Canon §13 with a disposition
    line.
  - Repoint Owner Action Items to the program roadmap.
  - Retire M1-specific proofs (P05, P07) from the attestation targets.

  If the founder still wants to apply to PearX, that is a separate decision.
  Show honestly labelled H1 evidence (received original → Home → exact return;
  Quiet Home's sourced reading; the Source workflow), not Plan Repair.
- **Rationale.** The milestone cannot be met, contradicts three later rulings,
  and its application packet is already archived. Leaving it active
  misdirects every agent that reads Owner Action Items.

#### D28 — Brand: Vesper vs Hermene/Oivaro

- **Evidence.**
  - `docs/decisions/2026-08-17-hermene-working-brand-decision.md` is accepted:
    Hermene is the working name.
  - `docs/working/brand-candidate-comparison-hermene-oivaro-2026-08-22.md`
    expired Sep 21.
  - All canon, code, bundle ids, design projects and Chat rulings use Vesper.
- **Recommendation.**
  - Record a short decision superseding the Hermene working-brand decision:
    "Vesper remains the working and product name until a naming review with
    trademark, linguistic and domain clearance precedes any external launch."
  - Archive the comparison.
- **Rationale.** An accepted decision that nobody follows is worse than no
  decision.

#### D29 — Membership, pricing and the v1 offer candidate

- **Evidence.**
  - Monetization Strategy (Sep 7) and the Sep 6 decision §4: membership is the
    leading hypothesis, with a pass as the comparator. "Complete is not
    unlimited."
  - `vesper-v1-supported-offer-2026-09-07.md` is `decision_status: proposed`
    and expires Oct 7. Its §7.9 sets price only after a cost worksheet.
  - Code: `COMMERCIAL_PAYWALL_MODE=off` and `REVENUECAT_ENABLED=false` in
    production and preview.
- **Recommendation.**
  - No price or billing work now.
  - Adopt §7.4's free/paid boundary as a principle in Monetization Strategy.
    The rule: "additional accepted work, not a category of value". Social and
    correction are never paywalled.
  - Extend the offer to a commercial checkpoint after Package 2, or archive it
    and fold its three entrances into the roadmap.
  - Amend What We Believe #0.25, #15, #24 and #33 (Part B).

#### D30 — Launch geography (NYC)

- **Evidence.**
  - Sep 6 decision: "A founder-accessible NYC cohort is a hypothesis, not a
    selected launch geography."
  - The corpus is Brooklyn only: 8 places, 396 venues, 14 sites. There is no
    Manhattan, Queens or Bronx content (cross-cutting catalog §7).
  - The Ticketmaster tool defaults to Lisbon.
  - A possible Google key-name mismatch was reported.
- **Recommendation.**
  - Select NYC as the internal dogfood cohort geography, with Brooklyn-first
    supply.
  - Make "which neighborhoods the cohort actually lives in" the first
    Package 2 supply question.
  - Not a public launch.
  - Fix the provider defaults (Ticketmaster location, Foursquare `/v3`
    deprecation, the key name) as part of D32.

---

# Part B — Deprecation list (canon, docs, release artifacts)

Priority key:
- **P0** misleads agents or builds today.
- **P1** contradicts current direction in canon.
- **P2** is hygiene.

Action key:
- **Amend** means edit in place, preserving numbered anchors and marking the
  correction.
- **Archive** means move under `archive/` with a disposition line.
- **Retire** means archive and remove from indexes and links.

## B.1 Table

| # | Artifact | What's wrong | Action | Priority | Depends on |
|---|---|---|---|---|---|
| B1 | `docs/release/m1-plan-repair.md` | Governs "current engineering priorities". Target Sep 28. Contradicts seven sentences, voting demotion and everyday-first. Last verified Aug 13. | Archive | P0 | D27 |
| B2 | `docs/Owner Action Items.md` | Says M1 owns priorities. Last verified Aug 9 (CI-only refresh Sep 24 on merged main). TestFlight path unrefreshed. | Amend header; re-verify console rows | P0 | D27 |
| B3 | `docs/release/v1-scope.yaml` + generated `v1-scope.md` | "Planning and group participation are the wedge". Promise points to M1. `social-profiles` includes follow; `expenses`, `group-trip`, `plan-repair` (M1 Act 1) are `in`. | Amend principles; mark M1 rows; later replace with offer-based scope | P0 | D27, D17, D29 |
| B4 | `docs/status/current-state.md` | `last_verified: 2026-09-04`. Shell described as "Trips, Vesper, Places, and You". Predates Life tab (Sep 5) and the Sep 26 recovered baseline. | Regenerate (`make docs-status-sync`) and refresh prose | P0 | — |
| B5 | `docs/contracts/chat-card-types.json` | `booking_proposal` and `booking_confirmation` still `active` despite booking retirement. `vote_widget` active as default. Last touched Aug 13. | Amend lifecycle: booking cards → deprecated then retired; vote_widget → deprecated as Vesper-emitted | P0 | D19, C1 |
| B6 | What We Believe #0.1, #0.25, #6, #7, #14, #15, #20, #23, #24, #27, #32, #33 | Travel-led and planning-free beliefs predate Sep 6. Last verified Aug 29. | Amend each in place | P1 | D01, D02, D29 |
| B7 | `Investor Narrative and FAQ.md` (active, Sep 5) | "Why group travel first"; wedge = group trips. The Sep 6 decision didn't list it for update. The fundraising packet is archived. | Mark historical, or amend to everyday-first | P1 | D27 |
| B8 | `Strategic Implications.md` (Aug 28) | Owns `wedge-and-expansion-sequence`. "The launch product is deliberately concentrated in group travel." | Amend | P1 | D01 |
| B9 | `Demo Journey Canon.md` (Aug 24) | Flagship = the M1 four acts. Owns `alpha-experience-scope`. | Amend §13 or archive with M1 | P1 | D27 |
| B10 | `docs/systems/group-social.md` | Jul 13 voting-first rulings (names on votes, holdouts visible, voting on by default). "We do not compete on messaging" and the Trip room as the social object. Marked MVP-required. | Amend to sharing-foundation. Mark the Trip room as compatibility. | P1 | D02, D18, D19 |
| B11 | `docs/systems/README.md` master index | IA "Trips / Vesper / Places / You". "Wedge journeys = group-trip path (02 → 05)". Maturity tied to the wedge. | Amend to four roots and five benefits | P1 | D31 |
| B12 | `Group Chat Facilitator.md` (canonical, Aug 16) | Vesper as facilitator inside trip group chats; proactive interjection; four agency modes. Contradicts "no group chat", "answers when addressed", "Vesper is a door, not a presence". | Amend to "Vesper in a shared conversation answers when addressed", or archive as Trip-room legacy | P1 | D02, D18 |
| B13 | `Multiplayer Product Strategy.md` §5, §6 | Follow is a relationship signal. "Vesper is a quiet facilitator inside a shared room… native room owns … proposals, votes". Last verified Sep 6. | Amend: Friends only; sharing foundation; poll on request | P1 | D02, D17, D19 |
| B14 | `Relationship Edge Decision Note.md` (accepted Aug 7) | Keeps `follows` as a live interest edge feeding Discover ranking, invites and feed. | Amend with a superseding note: follow retired from product | P1 | D17 |
| B15 | `MVP Social Loop.md` | Expired Sep 15 but still `source_of_truth_for: social-distribution-hypothesis`. Predates the sharing-foundation direction. | Re-verify into Multiplayer Strategy §1, then archive | P1 | D02 |
| B16 | `MVP Public Share Canon Lock.md` (Jul 6) | "Canon-locked for engineering". Public story → plan-similar. Story sharing is off everywhere. | Archive | P1 | C10 |
| B17 | `Trips Vision.md` (canonical, Aug 16) | "Trips is the home for time, commitments…" (a Trips surface). Canon has no Trips root, and Plans rules "No Arrangements tab". | Amend into the Plan/Trip specialization owner, or archive | P1 | D16, D31 |
| B18 | Product `README.md` (Aug 28) | Monetization list "premium experience, group transactions, attributed demand". Thesis described as "launch wedge". Chat owners list Group Chat Facilitator. Booking strategy under "Strategy". | Amend | P1 | D29 |
| B19 | `docs/journeys/` J01–J28, `journeys.yaml`, `PRODUCT_PROOF_SPINE.md`, `product-proofs.yaml` | Trip-era certification anchors: J10/J22 booking, J07 Discover, J11/J25–J28 Atlas, J12 story, J19 social loop. Proofs P01–P07 are M1-shaped. | Freeze. Mark retired journeys. Author everyday journeys for the five benefits and H1's three situations. | P1 | D27, D31 |
| B20 | `four-root-loop-object-surface.md` §6.4, Places action | Fixed returns, OPEN/RESTING/CLOSED threads, "All sources". Places "add to a Plan or Occasion" vs the 09-04 ban on generic Add to trip. | Amend | P1 | D04, D13 |
| B21 | `docs/decisions/2026-08-17-hermene-working-brand-decision.md` + `brand-candidate-comparison-…-2026-08-22.md` (expired Sep 21) | Accepted brand that nothing uses | Supersede; archive comparison | P1 | D28 |
| B22 | `Planning Philosophy.md` | Scope note: "Travel is the launch wedge" | Amend scope note | P2 | D01 |
| B23 | `social-loop.md` ("archived in place") | Implementation log in the canon folder | Move to archive | P2 | — |
| B24 | `postcard-primitive.md` | Historical working reference in the canon folder; image generation is out | Move to archive | P2 | C9 |
| B25 | `Booking Product Strategy.md` | Superseded, but still listed under Strategy | Move to archive | P2 | C1 |
| B26 | `Atlas Vision.md`, `Discover Vision.md`, Atlas/Elif dogfood docs in the product folder | Superseded design history and QA matrices in canon | Move to archive (the README already calls them "historical debt") | P2 | C6 |
| B27 | App surface contracts `atlas-*`, `discover-home`, `booking`, `trips-home`, `vesper-home` | Compatibility captures for retired or legacy surfaces | Mark compatibility; archive at code removal | P2 | C1, C5, C6 |
| B28 | `global-navigation-ia-proposal-2026-07-25.md` (expired Aug 24), `customer-journey-expansion-proposal-2026-07-18.md` (expired Aug 17) | Proposes a Trips/Vesper/Places + You hub; journey expansion | Archive | P2 | — |
| B29 | `prepared-continuation-decision-proposal-2026-09-09.md` | Resolved Sep 9 but still `active`. I1/J2f frames still labelled PROPOSED. | Archive; remove PROPOSED labels in designs | P2 | — |
| B30 | Philosophy source `the-world-is-lived-not-searched…-2026-08-18.md` | The orchestrator's vision source expired Sep 17 | Refresh or promote the adopted parts | P1 | D01 |
| B31 | `pin-as-ambient-unit-working-decision-2026-09-02.md` | "Killed" comments under pins; later ruled comment as a verb | Amend or archive | P2 | D02 |
| B32 | Expired working-doc backlog | See B.3 | Bulk disposition | P1 | — |

## B.2 Details on the high-priority items

**B1–B3 (M1 chain).** Three documents route every agent to a demo that
contradicts canon: `m1-plan-repair.md`, Owner Action Items and
`v1-scope.yaml` ("the current milestone lives in M1"). The act-by-act
conflicts are listed under D27.

Archive `m1-plan-repair.md` with the disposition "superseded by the program
roadmap (Sep 25/26) and everyday-first strategy (Sep 6); P02/P03/P04/P06 proof
work retained under the roadmap". Amend `v1-scope.yaml`'s principles and
promise now. Rebuild the capability list against the five benefits when D29
lands.

**B4 (status).** `current-state.md` is the generated front door. Stale since:
- the shell change on Sep 5 (Life replaced You as the fourth tab, commit
  `a548d4d9f`);
- the Sep 26 recovered baseline.

It also says nothing about the rollout posture being "legacy" in every
profile. Regenerate it, and add one line on the posture.

**B5 (card contract).** The contract's policy says "retire it in
`attachment_lifecycle` first". The booking cards should move to `deprecated`
now; the app keeps `RetiredCardFallback` for history. The Chat catalog lists
"Booking card retirement in the wire contract" as open for the card-registry
owner. `vote_widget` should be deprecated only as a Vesper-emitted card. Keep
the renderer for host-requested polls under D19.

**B6 (What We Believe).** Amend in place. The file's own rule: "preserve its
number and mark the correction".

| # | Current text (abridged) | Problem | Proposed correction |
|---|---|---|---|
| 0.1 | "Earn trust at home; carry it into travel." | Treats local value as a bridge; Sep 6: "Local value does not need to drive travel" | "Everyday value is intrinsic; travel is a demanding specialization." |
| 0.25 | "Planning should be free and effortless — Settled for the launch wedge." | Sep 6 §4 replaced "planning is free, always" with "complete is not unlimited" | Retire the wedge qualifier. "Useful free participation is complete and credible; paid expansion is additional accepted work." |
| 6 | Itinerary reconciles "chat, map, booking, voice" | Booking execution retired | Drop "booking" or qualify it as "retained reservation evidence" |
| 7 | "The native room carries proposals, votes…" | Voting demoted; no group chat | "Vesper answers when addressed; polls only when a host asks; the group's conversation can remain where people talk." |
| 14 | "'Join our Trip'… can acquire participants" | Sharing is the foundation | "Receiving something worthwhile is distribution; a recipient owes nothing." |
| 15 | "Per-Trip, not per-month" | Membership is the leading hypothesis | Mark superseded by Monetization Strategy (Sep 7) |
| 20 | "Travel is the wedge, not the boundary" | Everyday-first | Drop "wedge" |
| 23 | "Offer a beautiful artifact and warm conversation" | Conflicts with "no mandatory recap", "no reflection homework", and postcards being retired | "Afterwards, what was shared and kept becomes findable; no manufactured artifact, debrief or rating." |
| 24 | "Free group planning can reduce adoption friction" | Group-planning-first | Generalize to free participation |
| 27 | "The Trip's photo album belongs with the Trip" | Experience-centered, and photos can be friends' originals | "Photos belong with the experience and their authors." |
| 32 | "…does not authorize broad local expansion before evidence" | Everyday-first is now strategy | Keep the evidence caution; remove the travel-first framing |
| 33 | "Monitoring, operating, adapting, executing… create the stronger paid value" | Execution retired | Remove "executing" |

**B10–B14 (social canon).** These five documents encode the older social
model (Trip room, votes, facilitator, Follow), which the Sep 20–25 direction
contradicts. Amend them in one pass after D02. Mark `group-social.md` as the
*compatibility charter* for the legacy Trip room. Move the forward model
(sharing foundation, four kinds and one set of verbs, Friends, named
audiences, poll on request, no group chat for now) into Multiplayer Product
Strategy.

**B19 (journeys).** 28 journeys and the proof spine are the certification
system. Most are trip-era or retired-surface journeys. Freeze them rather than
delete them: they still anchor tests. Author 6–8 new journeys that map to:
- the five complete benefits (Sep 7);
- H1's three situations;
- receiving a friend's original with no account.

## B.3 Expired working documents

Measured on the main checkouts on Sep 26 (active documents whose `expires`
has passed):

| Location | Active | Expired | Expiring by Oct 10 |
|---|---:|---:|---:|
| `docs/working/` | 341 | 127 | 188 |
| `travel-agent/docs/working/` | 84 | 80 | 2 |
| `travel-app/docs/` | 72 | 28 | 2 (42 have no expiry) |

More than half of the workspace working corpus will be expired by Oct 10.
That includes:
- all eight proposals;
- the program roadmap;
- the integration roadmap;
- the v1 offer;
- the Home review.

**Recommendation.** One disposition sweep, owned by the coordination task:
- Archive everything superseded by the recovered baseline or by a decision.
- Re-verify only the documents the roadmap or H1 plan cites.
- Extend nothing by default.

Priority order:
1. The documents this register depends on: the proposals (promote them per
   D04–D11), the roadmap and the Home review.
2. Aug 27–Sep 5 execution receipts, which are now in the program archive.
3. July itinerary, Atlas and Discover material.

`python3 scripts/check_docs.py --all` passes, so expiry is not enforced on
working documents. That gap should be closed in `docs/governance/`, not by
adding a new rule for every incident.

---

# Part C — Product-concept deprecations (alive in code or design)

"Alive" means reachable in a checked-in build profile or drawn as current
design. Sources: the current-state catalog and notes, the cross-cutting
catalog, the booking-retirement receipt
(`docs/working/capability-retirement-execution-receipt-2026-09-05.md`), and
the surface-contraction investigation.

## C.1 Table

| # | Concept | Where it lives | What the vision says | Recommended treatment |
|---|---|---|---|---|
| C1 | **Booking execution** | Backend `booking_agent`: CR-2 guards landed, but `BOOKING_EXECUTION_RETIRED=false` by default and absent from `fly.toml`. App `booking/[sessionId]` is reachable from Details › Booking activity, chat booking cards, object pages and notifications. Concierge booking-tool discovery is still present. There are booking notification kinds. | Retired Sep 5/6. Keep evidence and external continuation only. | Finish CR gates: environment audit → set the retirement flag → deprecate cards (B5) → remove app session routes and booking tools → remove notification kinds → delete the execution footprint after obligations |
| C2 | **Voting as the default** | `VoteWidgetCard` in the Trip room and proposal detail; Vesper-emitted `vote_widget` (group-only capability); visible voting ON for trips with ≥2 members; stay-candidate votes; vote nudges; guest vote links (dark). | "Voting feels awkward"; conversation-led gathering; poll only on request | Flip default off; remove Vesper-emitted polls and vote nudges; remove public holdouts; keep exact-proposal accept/decline |
| C3 | **Follow graph** | `follows.py`, `FollowPill`, follow suggestions, follower/following counts on `/profile/[userId]`, `follow_affinity` ranking, `v1-scope` social-profiles | Friends only (You r3; D09/D17) | Replace with Friends pill on pair circles; hide follow UI; freeze table; remove counts |
| C4 | **Vesper as group facilitator** | `group_interjection.py` proactive triage; room agency modes including proactive/autopilot and consensus automation (opt-in); `compose_group_message`; `GroupVesperNote`; the "{name} is asking Vesper…" banner | "Vesper is in it only when someone asks"; a door, not a presence | Keep only "answers when addressed"; remove proactive interjection and consensus automation; remove the naming banner (D23) |
| C5 | **Trip-first Home** | Default first tab is Plans (`TripsHomeBody`) with the cold "where to?" hero. Onboarding has "I have a trip in mind"; the fallback route is Plans; share-capture "Done" returns to Plans. 34 notification kinds are mostly trip-scoped. Home V2 labels everyday Outcomes "From the trip". | Everyday-first; Home = what is worth attention now | Cut over at D31. Meanwhile re-point fallbacks (share-capture Done, onboarding fallback) to the neutral root, and fix the "From the trip" label. |
| C6 | **Atlas/Discover remnants** | Hidden `discover`/`atlas` tabs that redirect; `AtlasIndex` rendered only by a test; `app/atlas/*` (inbox, compose, scan, long-view, memory, removed) reachable only from legacy paths; `routes.discover()` behind "Find people"; copy "stories appear in Discover"; `atlas_auto_candidate` loop (hard off); deprecated `atlas_draft` card; Atlas timeline rows feeding Life | Retired Aug 12; Life and Places own it now | Delete dead components and redirects after one release; move `/you/memory` and `/you/removed` under You/Trust; fix stale copy; migrate Atlas timeline rows to graph Plans (D16) |
| C7 | **Expenses/split** | 5 routes under `trip-expenses`; Details › Costs; "Help me split what we spent"; deterministic settlement; expense chat tools | Contraction to an assisted ledger (Sep 5 brief); "settling up" undrawn; non-Trip debt has no owner | **Keep, don't promote.** Contract to assisted capture plus the deterministic ledger inside Plan/Occasion. Retire the 5-route UI only after assisted paths cover the retained jobs. Decide non-Trip debt later. |
| C8 | **Voice (live)** | LiveKit `VoiceOverlayProvider` dogfood-only; voice machines scale from 0; commercial pilot `voice.session.start`; dictation defined but unset | Input is multimodal (#11); Chat voice states undrawn | Park dark; keep composer dictation as the voice input path; no live-voice product work until a design exists |
| C9 | **Postcards (image generation)** | `postcard-primitive.md`; `v1-scope` "image-generation artifacts are dark" | Human originals first; no manufactured artifacts | Retire concept; remove dark image-gen code after inventory |
| C10 | **Story sharing / Unpacked / plan-similar** | App `STORY_SHARE_ENABLED=false` hard-coded; `/stories/[slug]` serves existing slugs; `unpacked/[token]` stub; `/you/history/recap` (Unpacked); **`story_backfill` background LLM loop running**; plan-similar routes | Sharing = the person's originals to chosen audiences, not public trip stories | Stop `story_backfill` (cost with no reader); retire minting and plan-similar; keep existing slugs readable until a sunset date; fold Trip Story into Life's record |
| C11 | **Onboarding orphans** | Steps `taste-interest`, `taste-pace`, `gift`, `permission` (photo-diary scan), `decline-reframe` rendered but unreachable; `OnboardingDiaryScanCoordinator` mounted | First question is the onboarding (Chat O2) | Remove steps and coordinator |
| C12 | **Proactive weather-rescue proposals and autopilot kinds** | `WEATHER_RESCUE_PROPOSALS_ENABLED` (M1 Act 1), autopilot and proposal-deadline notification kinds | Sentence 6: recommend once, prepared-message door only | Keep dark; retire with M1 (D27) or rebuild as a one-sentence implication plus prepared message |
| C13 | **`CurrentShapeSurface` status buckets** | SETTLED/FLEXIBLE/OPEN/CHANGED/UNKNOWN sections behind `PLAN_SHAPE` | Sep 5: "Status buckets are prohibited as page organization" | Remove the bucket composition when Plans is rebuilt |
| C14 | **Guest proposal capability (vote links)** | Backend `/guest/{token}` dark; no app route | Guest identity policy pending (D10) | Retire; rebuild guest access under D10 |
| C15 | **Unflagged "Leave this place for someone"** | Legacy venue page, guarded only by a confirmed pair circle; 404s unless the backend secret is set | "No doorway that cannot complete" (`featureFlags.ts:186-188`) | Hygiene bug: gate it on the relationship flag now |
| C16 | **Design-level remnants** | MS 04 auto-connect and contact matching; MS 03 Home "From friends" rows; Home 03 note-first; SE "Keep a copy"; the board 21.1 "ENDS AT BOARDING" promise | D09, D20, D15, D25 | Re-label as rejected or not-adopted in the design indexes once decided |

## C.2 Recommended removal order

The order follows two rules: least product risk first, and nothing removed
before its replacement or disposition exists.

**Wave 0 — now. No product decision needed; dead or dark code only.**
1. C15: gate the unflagged relationship doorway. This is a bug.
2. C10 (part): stop the `story_backfill` loop, which costs money with no
   reader. Leave existing story slugs readable.
3. C11: remove orphaned onboarding steps and the diary-scan coordinator.
4. C6 (part): delete dead `AtlasIndex`/`LegacyAtlas` code and stale "Discover"
   copy. Leave the redirects for one release.
5. C9 and C14: remove dark postcard image generation and the guest vote
   capability, after the inventory confirms no consumer.

**Wave 1 — booking (already authorized, Sep 5).**

6. C1: run the per-environment obligation audit, then:
   - set `BOOKING_EXECUTION_RETIRED` in production;
   - deprecate the booking cards (B5);
   - remove app entry points to `booking/[sessionId]` and the concierge
     booking tools (this needs the Chat lane);
   - remove the booking notification kinds;
   - delete the execution footprint after the closure receipt.

**Wave 2 — after D02/D09/D17/D18/D19 (target Oct 7).**

7. C2: flip the voting default; remove Vesper-emitted polls and vote nudges.
8. C4: remove proactive interjection and consensus automation; keep
   when-addressed answers.
9. C3: Friends replaces Follow in the UI; freeze `follows`.
10. C12: retire weather-rescue proposals with M1, or redesign them to the
    one-sentence form.

**Wave 3 — at the four-root cutover (D31, after H1 exit).**

11. C5: the Plans tab stops being the root. Trip-scoped notification kinds are
    reviewed against the everyday Home. The legacy Trip room is frozen (D18).
12. C6 (rest): remove the Atlas/Discover redirects and migrate Atlas timeline
    rows (D16).
13. C13: remove the status-bucket Plan surface when the seven-sentence Plan
    ships.

**Wave 4 — later, each needing its own design.**

14. C7: contract expenses to an assisted ledger once the assisted paths cover
    capture, correction and close-out.
15. C8: decide live voice once Chat voice states are drawn.
16. C10 (rest): set a sunset date for public story slugs; fold Trip Story into
    Life.

---

# Part D — A suggested founder session

This takes about 90 minutes and is meant to happen before Sep 28. Take the
decisions as packages, in this order:

1. D27 (M1) and D28 (brand).
2. D01 + D02 (the arc and the design direction). This unlocks Parts B and C.
3. D04 (retained intention and AHEAD).
4. The social package: D08, D09, D17, D18, D19.
5. The friends'-material package: D15, D11, D21.
6. D05 + D06 (continuity and scoped instructions).
7. D10 (guests).
8. The Home package H1 needs: D20, D24, D26, D32.
9. Delegate D07, the D12/D13 schema, D16, D22, D25 and the D29–D31 criteria
   to lane owners, with the recommendations above as starting positions.

Everything else in Part B can then be executed by the coordination task as
documentation amendments, each citing the new decision records.
