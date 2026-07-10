---
doc_type: archive
status: archived
owner: founder / engineering
created: 2026-07-10
archived: 2026-07-10
why_new: Preserve the complete adjudicated investigation after durable decisions and contracts moved to canonical owners.
---

# Multiplayer Propagation Matrix — Phase 0 (adjudication draft)

> Adjudicated and archived 2026-07-10. Current truth lives in system charters, decisions, generated checks, and code.

**Status:** Phase 2 wedge-trio fixes landed + certified 2026-07-09 (working tree, not committed). D1–D9 accepted; Phase 1 verified (Section 5); Phase 2 shipped (Section 6). Remaining gaps + FE follow-up tracked below.
**Date:** 2026-07-09
**Inputs:** 4 code-trace agents (proposals/itinerary, stays/membership/trip-meta, expenses/bookings, live-trip/photos/chat) + 1 canon/surfaces agent. Traces cite backend file:line; canon cites docs/design paths.

**Purpose.** This document crosses every group-visible mutation (what member A can do) against observer surfaces (what member B should see, where, how fast). Column 2 of each matrix row is what the code does *today* (from traces); columns 3–4 are *proposed* expectations grounded in canon where it speaks and in modest defaults where it is silent. You bless or amend the expectations; Phase 1 agents then verify code against the blessed rows using seeded dogfood personas (A acts via API → assert B's read models).

**How to adjudicate.** Section 1 first — its decisions (D1–D9) parameterize matrix rows below. Then each matrix row: mark the `[ ]` cell **✅** (agree with proposed expectation) or **✏️** (change, with a short note). Unmarked = not yet decided; Phase 1 skips unmarked rows. Budget: Section 1 ≈ 15 min, Section 2 skim ≈ 20 min (rows referencing an undecided D# can be deferred), Section 3–4 ≈ 5 min.

---

## Section 1 — Founder decisions needed first (canon silences & tensions)

Recommended defaults are biased toward: **honest** (no fake liveness, no silent mutation), **quiet** (ledger/refetch over push), **reversible** (settings and soft defaults over schema commitments) — the cheapest trust-preserving posture for a first dogfood cohort.

### D1 — Vote identity visibility
**Question:** Who sees individual votes, and may non-voters be named ("waiting on Ana, you")?
**Sources conflict:** canon JSX renders voter avatar stacks + named decided receipts (`design/vesper-canon-anchor/project/people-collab-app.jsx` ~230–892); FE page-spec says "counts and my vote are enough; avoid naming voters" (`travel-app/docs/page-specs/change-proposals.md` §11.6); chat canon makes it a setting (`vesper-chat-sections.jsx:220`); `Surfacing Strategy.md` §4.4.1 leans anonymous ("Anonymity is the privacy firewall"); graph-legibility doctrine forbids vote *reuse* as taste regardless. Group-social fairness invariant needs non-voter identity at least agent-side.
**Recommended default:** Tallies + own vote only on all group surfaces; voter names never rendered; non-voter naming allowed only in the *organizer's* private view and agent-side nudge targeting (never in group chat copy). Canon JSX voter stacks marked deferred. Cheapest, most privacy-safe, reversible later by adding a per-decision setting.
**Founder ruling:** ✅ Accepted (2026-07-09). Tallies + own vote only; voter names never in group surfaces; non-voter naming organizer/agent-side only.

### D2 — Delivery-mechanism doctrine (which events are live / refetch / push)
**Question:** What is B's channel + latency expectation when A acts? No canon anywhere assigns SSE vs refetch-on-focus vs push per event class (`phase0-surfaces.md` Part 3 #2); J09 route matrix covers destinations only.
**Recommended default:** Three tiers. **T1 push** = existing arbiter-gated events only (proposal created, booking event, invite answered, settlement) — no new push classes for dogfood. **T2 refetch** (≤ pull-to-refresh / next focus) = everything group-visible: votes, tallies, plan edits, expenses, stays, membership. **T3 ledger-only** = audit rows with no active delivery (undo, dismissals). SSE stays scoped to concierge streaming; no new live channels for dogfood. Honest and cheap; declares in-app propagation = invalidation-chain + focus-refetch.
**Founder ruling:** ✅ Accepted (2026-07-09). T1 push = existing arbiter events only; T2 refetch-on-focus for all other group-visible state; no new live channels for dogfood.

### D3 — Plan-sharing spectrum (curator / wiki / selective)
**Question:** `Interaction Design and Social Dynamics.md` §5 defines propagation *gating* ("nothing goes to the group until the admin says so") as first-class; every built surface (Folio, Plan, Changes, Map) assumes wiki-mode — everything visible immediately (`phase0-surfaces.md` §2.7).
**Recommended default:** MVP = wiki-only; mark curator/selective canon **deferred** explicitly so Phase 1 doesn't flag wiki behavior as a gap. A draft/private plan layer is a large schema+surface build with no dogfood evidence of demand.
**Founder ruling:** ✅ Accepted (2026-07-09). MVP = wiki-mode only; curator/selective propagation marked deferred (Phase 1 must not flag wiki behavior as a gap).

### D4 — Direct-edit and live-action fan-out
**Question:** When A direct-edits (Change Studio / concierge itinerary tools) or skips/reorders in Now Mode, does B get anything beyond the Changes ledger + refetched read models? Code today: direct-edit receipt is `visibility="private"` (`plan_edit_commit.py:412`), no chat bridge — while the proposal path posts group receipts + chat widgets + push (`phase0-family-proposals-itinerary.md` #6). Canon only guarantees ledger + J06 parity; J05 step 13 "where applicable" undefined; §12 during-trip speed tiers map to no channel.
**Recommended default:** Direct edits become **group-visible but quiet**: flip receipt to `visibility="group"`, appear in Changes ledger + PlanChangeStrip on refetch (T2); NO chat card, NO push pre-trip. Live-trip (Now Mode) skips: same, plus eligible for the live-mode urgency path later — not for dogfood. Silent-mutation-free without proposal-level noise.
**Founder ruling:** ✅ Accepted (2026-07-09). Direct edits = group-visible but quiet: receipt visibility="group", Changes ledger + PlanChangeStrip on refetch; no chat card, no push for dogfood.

### D5 — Consensus / threshold / resolution mechanics
**Question:** What accepts a proposal? Canon has narrative only: lazy consensus 24h pre-trip, 15-min live window, organizer escalation, a `tied` state with no resolution rule (`Interaction Design…md` §6/§9/§12; `people-collab-app.jsx` ~863–880). Code today: organizer-only resolve endpoint; `maybe_resolve_on_vote()` auto-resolves "on consensus" best-effort (`proposals.py:289` path).
**Recommended default:** MVP rule = **organizer resolves; unanimous-yes among voters ≥2 may auto-accept; no timeout automation** (deadlines are copy, not machinery). GroupEventLine posts on *resolution*, not on each vote. Document the 24h/15-min figures as post-dogfood.
**Founder ruling:** ✅ Accepted (2026-07-09). Organizer resolves; unanimous-yes among ≥2 voters may auto-accept; no timeout automation. GroupEventLine on resolution, not per vote.

### D6 — Organizer role: fixed gate vs earned fluidity
**Question:** Canon vision says organizer must NOT be a fixed privileged role (`Interaction Design…md` §3/§6); every shipped gate hardcodes it (`core/edit_policy.py`, `require_trip_organizer`, stay control, resolve/revert rights; role table `people-collab-app.jsx:298-300`).
**Recommended default:** MVP = fixed organizer role, declared openly (it is what's built and what J05/J10 assume); log the fluid-role vision as post-dogfood. Adjudicating the opposite would invalidate Ask-the-Organizer, resolution receipts, and stay control weeks before dogfood.
**Founder ruling:** ✅ Accepted (2026-07-09). MVP = fixed organizer role, declared openly; earned/fluid role logged as post-dogfood.

### D7 — Expense line-item visibility
**Question:** Contract shows all members see A's logged amounts/categories/receipts pre-settle (`surfaces/trip-costs/contract.md`); expenses canon governs only booking-total privacy + masked payer-covers-fully (`docs/systems/expenses-settlement.md`). Silent: per-line privacy, whether new expenses notify the group, payer control.
**Recommended default:** Ordinary logged expenses are group-visible by default (they exist to be split); masked = payer-covers-fully remains the only privacy mechanic for dogfood; new expense = NO notification, visible on next Costs refetch (T2). Note: FE bug `costsViewModel.ts:375` hardcodes `masked:false` — must fix regardless of ruling.
**Founder ruling:** ✅ Accepted (2026-07-09). Logged expenses group-visible by default; masked=payer-covers-fully is the only privacy mechanic; new expense = no push, T2 refetch. `masked:false` bug queued for immediate fix.

### D8 — Join / leave / removal / role-change fan-out
**Question:** "Theo joined" GroupEventLine + invite-answer notification exist in canon (`people-collab-app.jsx`, J09 route matrix); silent on leave/removal announcement, role changes, invite-*sent* visibility. Code today: membership mutations emit nothing and invalidate nothing (`members.py:53/93/123`).
**Recommended default:** **Join** = GroupEventLine in chat + roster refetch + organizer notification (already canon-adjacent, and J02-critical). **Leave** = quiet GroupEventLine, no push. **Removal** = roster change only, NO group announcement (dignity; organizer knows, others see roster). **Role change** = roster only. **Invite sent** = visible on Trip Info to members, no announcement.
**Founder ruling:** ✅ Accepted (2026-07-09). Join = GroupEventLine + roster refetch + organizer notify; leave = quiet line; removal = roster-only (no announcement); role = roster-only; invite-sent = Trip Info only.

### D9 — room_muted: room-wide agent toggle with no audit
**Question:** Any member can flip `room_muted`, silently changing the whole group's agent behavior; no who-muted history, no event (`conversations.py:577`; trace `phase0-family-livetrip-photos-chat.md` gap #4). Canon silent.
**Recommended default:** Keep member-operable (least-trusting-member doctrine, `Interaction Design…md` §9) but make it honest: GroupEventLine "Vesper muted for this room" (unattributed) + audit field (who/when, organizer-visible). Cheap, preserves trust floor.
**Founder ruling:** ✅ Accepted (2026-07-09). Keep member-operable; add unattributed GroupEventLine ("Vesper muted for this room") + who/when audit field (organizer-visible).

---

## Section 2 — The matrix, by mutation family

Column key — **Gap?**: NONE / GAP (code < expectation) / EXCESS (code noisier than expectation) / ASYMMETRY (paths disagree). Delivery tiers per D2: T1 push, T2 refetch (≤ pull-to-refresh/next focus), T3 ledger-only.

### 2.1 Proposals and votes (wedge: J05)

| Mutation | What code does today | Proposed expectation: other members see... | Delivery + latency | Gap? | Adjudicate |
|---|---|---|---|---|---|
| Create proposal | plan_events `proposal_created`; group receipt; push; vote widget in chat; home+plan cache invalidated (`_propose_present.py:84`, `change_proposals.py`) | Vote widget in group chat; pending-decision Folio card; proposed block state on Plan; Changes row; hero promotion on Trips Home | T1 push (arbiter-gated) + T2 everywhere else | NONE | [ ] |
| Vote on proposal | NO plan_events; chat reaction emoji bridge; proposal/home/plan caches invalidated; auto-resolve check (`proposals.py:289`) | Tally updates on vote widget + Deck face + Folio facet; **no voter names (D1)**; NO push per vote; GroupEventLine only on resolution (D5) | T2; plan_events row required (durable decision history) | GAP — no plan_events; identity per D1 | [ ] |
| Resolve (accept/reject/supersede) | plan_events written; group receipt; change_applied_card or rejection notice in chat; caches invalidated (`proposals.py:409`) | Chat receipt card; Changes row with rationale; block state flips on Plan/Map; rejected = original confirmed intact (charter invariant) | T2; resolution notification via arbiter (T1) | NONE | [ ] |
| Revert accepted | plan_events `proposal_reverted`; group receipt; chat revert notice; caches invalidated (`proposals.py:657`, :802, :837) | Revert receipt in chat + Changes; Plan AND Map reflect it (revert-truthfulness invariant) | T2 | NONE (Phase 1: verify Map parity) | [ ] |
| Withdraw | plan_events via resolve path; chat notification; caches invalidated (`proposals.py:612`) | Widget flips to withdrawn; quiet chat notice; no push | T2 | NONE | [ ] |

### 2.2 Stays: candidates, votes, holds, choose (wedge: J05/J10)

| Mutation | What code does today | Proposed expectation: other members see... | Delivery + latency | Gap? | Adjudicate |
|---|---|---|---|---|---|
| Add stay candidate | Zero events; plan+home caches invalidated (`stay_candidates.py:129`, :49-62) | New candidate on stay compare + Folio stay facet | T2; plan_events row (audit) | GAP — no audit event | [ ] |
| Vote / clear vote | Zero events; **NO cache invalidation** (`stay_candidates.py:180`, :203) | Tally updates on stay compare + Folio facet; identity per D1 | T2 — requires invalidation to be wired | GAP — stale tallies until TTL | [ ] |
| Hold candidate | Zero events, zero fan-out (`stay_candidates.py:214`) | Hold badge on candidate + Folio; organizer-gated group commitment should be visible | T2 + plan_events row | GAP | [ ] |
| Withdraw candidate | Zero events; caches invalidated (:141, :361) | Candidate disappears; tallies recompute | T2 | GAP — no audit event | [ ] |
| Choose (→ accommodation) | Zero events; caches invalidated + expense sync (`:250`, :360, :351) | Group's biggest pre-trip decision: GroupEventLine in chat + Folio `just_accepted` + stay row + Changes entry | T2 + plan_events row; candidate for T1 (arbiter) | GAP — decision invisible outside stay screen | [ ] |
| Accommodation create/update/retire | Zero events; home invalidation + cost sync (`trips.py:1135/1191/1257`) | Shared base: stay row + map pin on refetch. Personal stay: respect per-stay visibility group/private (J10 semantics) | T2 | GAP — no audit; visibility honored (verify) | [ ] |

### 2.3 Expenses and settlement (wedge: J10/J12)

| Mutation | What code does today | Proposed expectation: other members see... | Delivery + latency | Gap? | Adjudicate |
|---|---|---|---|---|---|
| Create expense (incl. from receipt) | ZERO events; no invalidation; no push (`expenses.py:167`, :911) | Ledger row + updated balances on next Costs open; NO notification (D7); masked renders as payer-covers-fully | T2 (needs invalidation wired) | GAP — zero emission, stale settlement card | [ ] |
| Update / delete expense | Zero events, zero fan-out (`expenses.py:351`, :444) | Ledger + balances update on refetch; delete cascades to shares | T2 | GAP | [ ] |
| Settle shares (single/batch) | Zero events; `send_shares_settled_push()` to payer only, 30s coalesce (`expenses.py:473/:526/:552`) | Payer push (exists); balances update for all on refetch; J12 closing loop | T1 payer + T2 others | GAP — no event; push OK | [ ] |
| Comment add/delete | Zero events, zero fan-out (`expenses.py:660/:706`) | Comment visible on expense detail on refetch; no notification | T2 | NONE (accept quiet) | [ ] |
| Receipt upload/OCR | No events; arq OCR job w/ idempotency (`expenses.py:765`, :856) | Receipt thumbnail on expense row on refetch; OCR is actor-facing | T2 | NONE | [ ] |

### 2.4 Bookings and holds (wedge: J10)

| Mutation | What code does today | Proposed expectation: other members see... | Delivery + latency | Gap? | Adjudicate |
|---|---|---|---|---|---|
| Confirm booking proposal (REST) | No events; home feed invalidated; **no push** (`booking.py:468`, :505) | Booking public state (name/address/dates — never payment detail, J10 must-never); Call card clears | T2 + T1 (parity with concierge path) | ASYMMETRY — concierge pushes, REST doesn't | [ ] |
| Reject booking proposal (REST) | No events; invalidation only (`booking.py:520`) | Proposal card flips rejected; original state confirmed | T2 | ASYMMETRY (same) | [ ] |
| Confirm booking (concierge) | agent_event log; handoff card; push on L1 (`booking_flow.py:596`, :794) | booking_event object in group chat; Folio booking card; block → booked on Plan | T1 + T2 | NONE | [ ] |
| Propose booking (concierge) | agent_event; proposal card w/ privacy redaction; group card gated by privacy check (`booking_flow.py:116`, :261-291, :445) | Anonymized justification (no traveler naming — booking charter); vote widget if delegation="ask" | T2 | NONE — privacy gate is canon-correct | [ ] |
| Confirm cart | `booking.cart_confirmed` → trip_events + bus; chat bubble; receipt card; push via reconciliation (`booking.py:1105`, :1132-1141) | Richest path; treat as reference implementation for the family | T1 + T2 | NONE | [ ] |
| Settle/release hold; offers; sessions | Zero events, zero fan-out (`booking.py:590/:649/:822`) | Hold state on stay/booking surfaces on refetch; sessions are actor-scoped until outcome | T2 (holds); T3 (sessions) | GAP — hold state changes invisible | [ ] |
| Mark block booked | Group receipt (Trust Receipt) but NOT posted to chat; no invalidation (`trips.py:1673`, :1728-39) | Block flips tentative→booked on Plan/Folio; quiet chat booking_event line | T2 + chat bridge | GAP — receipt stranded outside chat | [ ] |

### 2.5 Membership and invites (wedge: J02)

| Mutation | What code does today | Proposed expectation: other members see... | Delivery + latency | Gap? | Adjudicate |
|---|---|---|---|---|---|
| Invite mint / revoke | Mint not logged; SMS/email dispatch + snapshot pre-bake (`invites.py:214`, :310, :334); revoke zero fan-out (:436) | Pending-invite row on Trip Info (D8); no group announcement | T2 | GAP — no audit trail | [ ] |
| Invite accept | REST logs `invite.consumed` + home invalidation + genesis synthesis (`invites.py:911`, :1120, :1158); **concierge path logs nothing** | "Theo joined" GroupEventLine; roster updates everywhere (membership-coherence invariant); organizer notification (J09 route: invite answer → trip info) | T1 organizer + T2 group | ASYMMETRY — concierge accept unlogged; GAP — no event line, no roster invalidation | [ ] |
| Intake submit | trip_event logged; organizer push/SMS w/ dedupe (`invites.py:736`, :785, :856) | Organizer-only until accept (no pre-accept leakage — group-social charter) | T1 organizer only | NONE | [ ] |
| Member add / remove / role change | ZERO events, ZERO invalidation, zero notifications (`members.py:53/93/123`) | Per D8: join line; quiet leave line; removal = roster-only; role = roster-only. Roster refetch on all surfaces | T2 (+ join line per D8) | GAP — joiner invisible until manual refetch | [ ] |
| Promote conversation → trip | ZERO emission at REST layer; participants copied to members (`conversations.py:1127`) | Every participant sees the new trip on Trips Home; genesis event in trip record | T2 + audit event | GAP — highest-impact funnel step, zero audit | [ ] |

### 2.6 Itinerary / plan edits (J05/J06)

| Mutation | What code does today | Proposed expectation: other members see... | Delivery + latency | Gap? | Adjudicate |
|---|---|---|---|---|---|
| Direct edit commit (REST + concierge block update/move/add) | plan_events written; receipt **visibility="private"**; no chat bridge; conflict-scan invalidation only (`plan_edit_commit.py:102`, :412) | Per D4: Changes row + PlanChangeStrip w/ attribution ("by whom" — Changes contract); NO chat card, NO push | T2 | ASYMMETRY — private receipt vs proposal path; per D4 | [ ] |
| Edit commit (propose mode) | Group receipt + push + widget; **no cache invalidation found** (`plan_edit_commit.py:223`, :534) | Same as create proposal (2.1) | T1 + T2 | GAP — missing invalidation | [ ] |
| Undo block edit | Reverses ledger entry, writes NO new event; no invalidation (`trips.py:1746`) | Changes ledger shows the undo (append-only doctrine: undo is itself a change); Plan refetch | T2 + ledger row | GAP — undo invisible in history | [ ] |
| Pin experience | plan_events `experience_pinned`; no receipt; NO idempotency (`trips.py:1814`) | New block on Plan on refetch; Changes row | T2 | GAP — no receipt; retry-dup risk (J05 must-never) | [ ] |
| Move/add/update block (REST) | plan_events only; no receipt, no invalidation, no idempotency (`trips.py:2243/:2397/:1604`) | Per D4 (same as direct edit) | T2 | GAP — no invalidation/receipt; ASYMMETRY — REST 403 vs concierge "needs_proposal" on propose-mode trips | [ ] |
| Conflict dismiss/undismiss | No events; per-viewer read-time filter (`conflict_dismissals.py:66`, `trips.py:2522`) | Nothing — personal preference, actor-only | T3 | NONE | [ ] |
| Observation / debrief | user_events written; shareable categories auto-shared (`home.py:212`, `trips.py:2075`) | Shareable observations may surface in group synthesis (anonymized); debrief private | T3 | NONE | [ ] |

### 2.7 Trip metadata

| Mutation | What code does today | Proposed expectation: other members see... | Delivery + latency | Gap? | Adjudicate |
|---|---|---|---|---|---|
| Trip patch (dates/destination/name) | No events; read models invalidated; thread recompute (`trips.py:457`, :478) | Updated header everywhere on refetch; Changes row for date/destination shifts (they invalidate members' plans) | T2 + audit event for material fields | GAP — material changes unaudited | [ ] |
| Budget update | No events, NO invalidation (`trips.py:2538`) | Budget context updates on refetch; budget detail stays privacy-tiered (always-private doctrine) | T2 | GAP — no invalidation | [ ] |
| Decommit | No events; phase reset (`trips.py:742`) | Trip state change visible to all; quiet | T2 | GAP — no audit | [ ] |
| Group memory patch/forget | No events, no invalidation; privacy keyword gates at write (`trips.py:2168/:2205`) | Updated group memory on refetch; consensus-only rendering (never Tensions — Surfacing Strategy §5) | T2 + audit event | GAP — group-visible, zero audit | [ ] |

### 2.8 Live-trip actions (J08)

| Mutation | What code does today | Proposed expectation: other members see... | Delivery + latency | Gap? | Adjudicate |
|---|---|---|---|---|---|
| Mark block happened / skip / event state | No events; conflict-scan invalidation only; any member may mark (`plan_mark_happened.py:33`) | Block state on Plan/Folio live cards on refetch; Changes row for skips (per D4); no push for dogfood (§12 speed tiers deferred) | T2 | GAP — no ledger row; folio/home not invalidated | [ ] |
| Nudge member (stay_vote / settle_up) | Push via triage w/ per-target cooldown; NOT deduped across senders (`trips.py:2741`) | Target gets one push; nudges never visible to the rest of the group | T1 target only | EXCESS risk — cross-sender dup ("nudge earns its interruption") | [ ] |
| Leave-by dismiss/mute | Suppression rows only (`trips.py:2665/:2687`) | Nothing — actor-only | T3 | NONE | [ ] |
| Heartbeat / presence | Writes silently dropped — table removed, ImportError swallowed, `presence_recorded` always False (`heartbeat.py:95`, migration d2e4f6a8b0c1) | Members do NOT see each other's presence (graph-legibility lean, silence #8); but the code must not pretend to record | n/a | GAP — dishonest dead write path | [ ] |

### 2.9 Photos and story (J12)

| Mutation | What code does today | Proposed expectation: other members see... | Delivery + latency | Gap? | Adjudicate |
|---|---|---|---|---|---|
| Upload photo | No events; visibility private/group/group_and_learn; story reads at query time (`trip_photos.py:74/:135`) | Group-visible photos appear in trip story/moments on refetch; private never | T2 | NONE (quiet by design) | [ ] |
| Patch visibility / block retag / learning opt-in | No events; retag open to any member who can see the photo (`trip_photos.py:243/:275/:308`) | Retags visible on refetch (collaborative curation); visibility changes take effect silently | T2 | NONE | [ ] |
| Create/patch/rotate story share | user_event `story_published` when openable+visible, deduped (`trip_story_shares.py:344`); card cache invalidated | Group Echo — "Fei shared the Lisbon story" soft in-app line (MVP Social Loop §7) — NOT BUILT; members' names/photos require explicit inclusion | T2 echo (no push) | GAP — group echo missing (canon-required) | [ ] |
| Revoke story share | Link dies immediately; does NOT retract `story_published` (`story_shares.py:251`) | Revoke fully honest: feed entry retracted, echo (once built) withdrawn | T2 | GAP — orphaned feed entry | [ ] |

### 2.10 Chat / agent (group room)

| Mutation | What code does today | Proposed expectation: other members see... | Delivery + latency | Gap? | Adjudicate |
|---|---|---|---|---|---|
| Send message (user) | No events; home-feed invalidation; NO SSE for plain user messages; no notifications (`conversations.py:685`) | Message in thread on next open/refetch; typing indicator per page-spec. Liveness canon-silent (silence #12) — D2 default: refetch OK for dogfood; declare it | T2 (explicit non-live) | NONE under D2 (verify honesty of typing indicator) | [ ] |
| Agent-triggered message / stream | SSE to streaming subscribers; interjection scan post-turn; agency gates (`conversations.py:828`) | Group-safe replies only (group_compose strict mode — concierge charter); SSE for the requesting client | SSE actor; T2 others | NONE | [ ] |
| React to message | Read-time aggregation, no events (`conversations.py:1248`) | Tally on the card on refetch; vote-widget reactions feed decision tally | T2 | NONE | [ ] |
| Update agency (room_muted etc.) | Room-wide toggle, any member, no audit, no event (`conversations.py:577`) | Per D9: unattributed GroupEventLine + who/when audit | T2 | GAP — silent room-wide behavior change | [ ] |
| Group interjection (agent) | social_signals row; arbiter + Haiku triage; cooldown at dispatch (`group_interjection.py:637`) | Agent message in room only when gates pass; stay-silent default (facilitator canon §2) | T2 | NONE | [ ] |
| Venue card / options post (concierge) | Structured cards appended, no events (`tools_schema.py` ~980/~1320) | Cards in thread on refetch; reaction tallies live in card state | T2 | NONE | [ ] |

**Row totals:** proposals 5 · stays 6 · expenses 5 · bookings 7 · membership 5 · itinerary 7 · trip-meta 4 · live-trip 4 · photos/story 4 · chat 6 = **53 rows**.

---

## Section 3 — Ranked gap register (top 15, wedge-weighted)

Ranked by impact on J05 (proposals/votes/decisions), J10 (booking/expense trust), J02 (invite loop). "Fix shape" is a one-line sizing hint, not a design.

| # | Defect | Evidence | Blast radius | Fix shape |
|---|---|---|---|---|
| 1 | Stay votes have NO cache invalidation → stale tallies on the group's biggest pre-trip decision | `stay_candidates.py:180/:203` — vote/clear emit nothing, invalidate nothing | J05 wedge demo: B votes, A's screen shows the old tally until TTL | Wire `_invalidate_trip_read_models()` into vote/clear (pattern exists at :49-62) |
| 2 | Membership changes emit nothing and invalidate nothing — joiner invisible until manual refetch | `members.py:53/93/123`; invite accept invalidates home only (`invites.py:1138`) | J02: the "aha" moment (friend appears) silently fails; membership-coherence invariant unverifiable | Wire roster invalidation + join GroupEventLine (decide D8 first) |
| 3 | Proposal votes write no plan_events — no durable decision history | trace #2, `proposals.py:289` path: chat emoji bridge only | J05: Changes ledger can't show how a decision was reached; auto-resolve forensics impossible | Add `proposal_vote` plan_events write (identity payload per D1) |
| 4 | Expense mutations emit ZERO events stack-wide; no invalidation | `expenses.py:167/:351/:444/:473` — complete asymmetry vs bookings | J10/J12: settlement card stale; no audit for money-adjacent writes | Wire invalidation now; add event emission behind D7 |
| 5 | Invite-accept REST-vs-concierge asymmetry: concierge path never logs `invite.consumed` | `invites.py:1120` (REST only); `_accept_trip_invite()` skips append_trip_event | J02: invite-funnel metrics (ACTIVATION_LOOP_CLOSED) undercount concierge accepts | Add append_trip_event to concierge accept — small, do now |
| 6 | `costsViewModel.ts:375` hardcodes `masked:false` though backend threads the real field | `phase0-surfaces.md` §1.12; `data/expenses.ts:110` | J10 trust: payer-covers-fully privacy mechanic silently broken on device | One-line FE fix + regression test — do now, no D# needed |
| 7 | Mark-booked group receipt never bridged to chat; no invalidation | `trips.py:1673/:1728-39`; trace-1 finding #6 | J10: "the group sees the right public state" fails at the booked moment | Post booking_event line to group chat + invalidate |
| 8 | promote_to_trip: highest-impact funnel mutation, zero audit | `conversations.py:1127` — no emission at REST layer | J02 genesis moment unmeasurable; no record of who committed the group | Add trip_event emission (genesis event) |
| 9 | user_events vocab has no entries for stays/votes/members; `booking_confirmed`/`booking_cancelled` enums exist but are never written | `_tables/_event_types.py`; trace-2 finding #3, trace-3 obs #7 | All downstream analytics/memory/proactive systems blind to the wedge actions | Extend vocab + write at mutation sites (after D-rulings; use event-type codegen from consolidation) |
| 10 | Direct-edit receipt visibility="private" — silent group mutation vs "every accepted change emits a visible receipt" invariant | `plan_edit_commit.py:412`; charter invariant §2.1 | J05/J06: B's plan changes with no attribution anywhere but the ledger | Decide D4 first; then flip receipt visibility + strip rendering |
| 11 | Stay choose emits nothing — the decision that ends the stay debate is invisible outside the stay screen | `stay_candidates.py:250/:360` | J05: no GroupEventLine, no Folio receipt, no Changes row for the biggest call | Add plan_events + chat line after D5 ruling |
| 12 | room_muted: room-wide agent kill-switch, member-operable, zero audit | `conversations.py:577`; trace-4 gap #4 | Whole-group behavior change attributed to no one; debugging "Vesper went quiet" impossible | Decide D9; add audit fields + event line |
| 13 | Story revoke doesn't retract `story_published` — orphaned feed/Discover entry | `story_shares.py:251` vs `trip_story_shares.py:344` | Post-trip trust: "I revoked it" isn't fully true | Emit retraction / tombstone on revoke |
| 14 | Heartbeat presence writes silently dropped — table removed, broad except swallows ImportError, `presence_recorded` always False | `heartbeat.py:95`; migration d2e4f6a8b0c1 | Dishonest wire contract; masks future regressions in the modality selector | Delete dead write path + return honest False (or narrow the except) |
| 15 | Nudges not deduped across senders; nudge+leave-by bypass the notification journal | `trips.py:2741`; trace-4 gap #6 | 3 members nudge Bob → 3 pushes; violates "a nudge earns its interruption" | Cross-sender cooldown key; route through arbiter journal later |

Systemic note: gaps 1–4, 8, 9, 11 are one underlying defect — **the stay/expense/membership families were built without the emission+invalidation discipline the proposals family has**. Phase 1 should verify per-row, but the fix is a shared checklist (event + receipt + invalidation + chat-bridge decision per mutation), not 15 bespoke patches.

---

## Section 4 — Proposed Phase 1 dispatch plan

Each lane = one verification agent. Method: act as persona A via API (seeded @dogfood.local cast — mara/elif/dao/reza/sarah/mike), then assert persona B's read models (`GET /folio`, `/plan-state`, proposals list, costs view, roster, chat history) — not the DB. Verify only ✅-blessed rows; report NONE/GAP/EXCESS per row against the blessed expectation.

| Lane | Matrix sections | Verifies | Blocked on |
|---|---|---|---|
| L1 Proposals & votes | 2.1 | Create→vote→resolve→revert loop across chat widget, proposal detail, Changes, Plan, Folio, Trips-Home hero; idempotency (replayed preview token); vote-identity rendering | D1, D5 |
| L2 Stays | 2.2 | Candidate→vote→hold→choose; tally freshness after fix #1; accommodation visibility (group vs personal); map pins | D1 (tallies), D5 (choose receipt) |
| L3 Money | 2.3 + 2.4 | Expense create/settle balances as B sees them; masked rendering on device (fix #6); booking public-state (never payment detail); REST-vs-concierge booking parity; mark-booked bridge | D7 |
| L4 Membership & invites | 2.5 | Full J02 loop: mint→intake→accept (BOTH paths)→roster coherence across Trips list/Trip Info/Chat/Notifications; promote_to_trip visibility | D8 |
| L5 Itinerary & live | 2.6 + 2.8 | Direct-edit visibility as B (receipt/strip/ledger); undo history; J06 parity Plan↔Map↔Folio after each mutation; mark-happened propagation | D3, D4 |
| L6 Photos, story, chat | 2.9 + 2.10 | Photo visibility tiers as B; story share/revoke honesty; room_muted audit; message propagation latency honesty (typing indicator vs actual liveness) | D9 (D2 for latency assertions) |

Sequencing: L1+L2 first (pure wedge, unblocked the moment D1/D5 are ruled); L3+L4 next (J10/J02); L5/L6 last. D2 and D3 rulings are cheap to make and unblock latency/scope assertions in every lane — rule them even if defaults are accepted as-is.

---

## Section 5 — Phase 1 verification results (2026-07-09)

All 6 lanes ran as static second-observer traces (no live LLM calls). Verdicts corrected several Phase 0 rows — Phase 0 traces read code as old as pre-2026-07-06. **Verify-before-fix cleared 3 phantom gaps and corrected 4 fix targets.**

### Phantoms — Phase 0 "gaps" that are NOT real (do not fix)
- **Masked-expense privacy break (was gap #6):** already fixed 2026-07-06 — `costsViewModel.ts:393` + `data/expenses.ts:110` thread the real `masked` field; regression test exists (`costsViewModel.test.ts:252`). Backend redaction correct. Residual `masked:false` = test fixtures only.
- **Expense zero-emission staleness (2.3):** NOT a defect — expense list/settlement reads are direct-DB *uncached* (`expenses.py:736/:268`), so B's Costs view is fresh on every refetch. "Zero emission" is the blessed T2 behavior. No fix needed.
- **Invite-accept concierge asymmetry (was gap #5, as cited):** there is no concierge/tool trip-accept path; the trip-scoped REST accept `_accept_trip_invite` DOES log `invite.consumed` (`invites.py:1120`). The real undercount is the *conversation-scoped* accept `_accept_conversation_invite` (`invites.py:1185/:1226`, documented "no conversation_events table yet"). Same net funnel effect, different + narrower location.

### Confirmed real gaps (verdicts + corrected evidence)
| # | Gap | Verdict | Corrected evidence / fix target |
|---|---|---|---|
| 1 | Stay vote/clear stale tally | CONFIRMED — but Phase 0 fix was WRONG | Tally served by an UNCACHED compare endpoint; staleness is FE react-query `DEFAULT_STALE_MS=120s` + `refetchOnWindowFocus:false` (`constants/query.ts:9`). Backend `_invalidate_trip_read_models` would NOT fix it. Fix = FE query config (focus-refetch / invalidate stay-compare query on vote). |
| 2 | Joiner invisible until refetch | CONFIRMED | `members.py:58/97/128` → `core/db/trips.py:812/:993/:1031` emit nothing, invalidate nothing, notify no one. Roster reads uncached but nothing prompts the refetch. No "Theo joined" GroupEventLine primitive exists backend-wide (D8). |
| 3 | Proposal votes no durable history | CONFIRMED | `vote_on_proposal` (`change_proposals.py:529-598`) writes no plan_events; tally is live but ephemeral (mutable votes JSON only). Note: tally DOES refresh for B (unlike stays). |
| 4 | Direct-edit vs D4 (private receipt) | CONFIRMED + worse | `plan_edit_commit.py:412` writes receipt `visibility="private"` (D4 wants `"group"`); the concierge edit path (`itinerary_edit.py`) writes NO receipt at all — flipping :412 alone won't cover it. |
| 5 | Folio never reconciles promptly after ANY itinerary edit | CONFIRMED — NEW (systemic) | Every itinerary mutation invalidates only db-layer plan_state, skips `home_feed`, so Folio attention band + Trips-Home hero lag until TTL. Bigger than any single row. Fix = route mutations through `_invalidate_trip_read_models` incl. home_feed. |
| 6 | Story-revoke orphan, B-observable | CONFIRMED — worse than theoretical | `revoke_share` (`trip_story_shares.py:170`) stamps `revoked_at`, never retracts `story_published` (`:342`); `get_social_feed` (`follows.py:105/:140`) + Discover `compose.py:365` surface it to followers with a share_url on the DEAD slug. |
| 7 | Stay choose emits no decision event | CONFIRMED | No plan_events / GroupEventLine / Folio `just_accepted`; only `:360` invalidate + `:351` expense-sync. B sees the booked stay row, never the decision. |
| 8 | Booking REST-vs-concierge push asymmetry | CONFIRMED | REST confirm/reject (`booking.py:468/:520`) invalidate home only; concierge path pushes + posts group booking_event. B learns of a decision differently by entry point. |
| 9 | Mark-booked receipt stranded | CONFIRMED | `trips.py:1673/:1710` writes group Trust Receipt, never bridges to chat, no invalidation. |
| 10 | promote_to_trip zero audit | CONFIRMED (visibility OK) | Participants DO see the new trip (`promotion.py:394`→`trips.py:757`); but no genesis `append_trip_event` (`conversations.py:1127`, `promotion.py:253`). Audit-invisible, not user-invisible. |
| 11 | room_muted no audit | CONFIRMED | `conversations.py:577/:279-285` — any member flips room-wide, no `muted_by/at`, no event line. Mute IS honored; purely a trust/audit gap. |
| 12 | Pin experience dup risk | CONFIRMED | `block_added` with NULL actor + no idempotency (retry-dup, a J05 must-never). |

### Matrix corrections (Phase 0 trace inaccuracies)
- **Undo** DOES write a `block_updated` plan_event (`trips.py:2199`) — Phase 0 "writes NO new event" is false; real residual = no receipt + route does no cache invalidation (Plan stale until TTL).
- **Move/add/update block** DO invalidate plan_state + emit plan_events at the db layer — Phase 0 "NO invalidation" inaccurate; real residual = no receipt, no idempotency, no home_feed invalidation.
- **Stay withdraw** — Phase 0 "caches invalidated (:141)" inaccurate; REST withdraw has no server invalidation.

### New findings not in Phase 0
- **Privacy:** `plan_state.py:772` bypasses the `viewer_id` filter — narrow private-primary-accommodation leak vector (L2). Needs its own look.
- **D1 code violation:** `missing_voter_ids` names non-voters to all members (L1) — violates the just-accepted D1 (non-voter naming organizer/agent-side only).
- **D5 code divergence:** `maybe_resolve_on_vote` auto-accepts wider than blessed — a lazy_consensus proposal auto-accepts once all voted with no rejections, including neutral votes (L1).
- **Adjacent (flagged, not fixed):** `_recover_consumed_invite` re-adds a member on fresh-device retry without any event (fix agent).
- **Map is always honest:** composes live from DB, so Plan↔Map parity holds after every edit except Undo (L1, L5).

### Not-broken confirmations (bank these — no work needed)
Create/resolve/revert/withdraw proposal (2.1); expense create/settle/comment/receipt (2.3); concierge booking confirm/propose/cart-confirm + J10 no-payment-detail invariant (2.4); intake privacy organizer-only (2.5); photo visibility tiers + collaborative retag (2.9); user-message honesty / no dishonest typing cue / agent group-compose / interjection gating (2.10).

---

## Section 6 — Proposed Phase 2 (fix + prevent)

Two workstreams. The founder decides scope; nothing below is started.

**A. Fix the confirmed gaps as ONE shared discipline, not 12 patches.** Gaps 2, 3, 5, 7, 9, 10 share a root cause: mutations built after the proposals family skip the emit + invalidate (incl. home_feed) + receipt + optional chat-bridge steps the proposals family does. Define a per-mutation checklist and apply it family-by-family (stays, membership, itinerary-Folio invalidation first — they hit the wedge). Gap 1 (FE query config) and gap 6 (revoke retraction) are separate one-file fixes. The D1 (`missing_voter_ids`) and D5 (auto-accept breadth) code divergences are small conformance edits to match rulings already made.

**B. Make it permanent — second-observer certifier.** Extend the existing journey certifier so that after persona A performs each blessed mutation, it asserts persona B's read models (roster, tally, Folio, Changes, feed) at the blessed tier. That converts this whole audit into a CI gate, so the gap class cannot silently regrow as agents keep building — the founder's actual long-term worry. Deterministic, replayable, zero LLM cost per run.

Suggested first slice: fix the wedge-critical trio (stay-tally FE fix, membership join event+invalidation, Folio home_feed invalidation) → add second-observer assertions for exactly those → then work outward. Rank/scope TBD by founder.

### Phase 2 outcome (2026-07-09) — SHIPPED to working tree (not committed)

**Fixes landed, tests green:**
- **FE group-collaborative refetch** (travel-app): per-query `refetchOnWindowFocus:true` + 10s `COLLAB_STALE_MS` on stay-tally (`data/stayCandidates.ts`), roster (`data/trips.ts` all `useTripMembers*`), proposal-tally (`data/proposals.ts`) queries. One lever, closes gap #1 + the FE half of #2 + proposal-tally sibling. 5 new tests + proposals suite 7/7 green. Key insight: fix lives on the *observer's* read query, not the actor's write (invalidation-on-vote can't help B — B never mounts A's mutation).
- **Backend Folio invalidation** (travel-agent, gap #5): db-layer chokepoint `_invalidate_itinerary_read_models(trip_id)` in `core/db/trips.py` adds `home_feed` to create_block/update_block/move_block — covers all itinerary paths (REST + concierge) uniformly. 2 tests.
- **Backend membership join** (travel-agent, gap #2 + D8): `api/routes/_membership_events.py` (`emit_member_joined/left/removed/role_changed`) reuses the conversation-message primitive (`card_type="group_event"`) + `append_trip_event("member.joined")` + home_feed/plan_state invalidation + organizer push; wired into members.py add/delete/role + invites.py `_accept_trip_invite`. Idempotent. D8-compliant (join=line+push; remove/role=silent audit). 8 tests.

**Permanence: second-observer certifier** — `tests/scenarios/_second_observer.py` (reusable harness: `SecondObserver` per-persona clients + substrate readers `group_event_lines`/`trip_ledger_event_types`/`capture_invalidations`) + `tests/scenarios/test_second_observer_wedge_trio.py` (5 tests). Drives real routes as persona A, asserts persona B's real read models (never the DB) at the blessed tier. **13 tests green together** (5 certifier + 6 FIX B + 2 FIX A). This is the CI-gate seed; extension rule documented in the harness docstring.

**FE FOLLOW-UP GAP (not built):** backend now posts the join line as `card_type="group_event"`, but FE doesn't render it — `classifyGroupMessage.ts` has no `group_event` branch (falls through to `vesper_note`), and `messageMapping.ts:142-156` routes it to a generic `NotificationCard`, not `GroupEventLine`. Joiner still appears via roster refetch; the "Theo joined" centered line won't show until a `group_event` case is added to both `classifyGroupMessage` and `messageMapping` → `GroupEventLine kind="system"`.

### Pre-cohort trust/privacy fixes (2026-07-09) — SHIPPED to working tree (not committed)

- **Gap #6 story-revoke orphan — FIXED + CERTIFIED.** `revoke_share` (`core/db/trip_story_shares.py:170`) now deletes the `story_published` user_event (matched on owner + entity_id) in the revoke transaction, so revoked stories disappear from BOTH the follower feed and Discover (both read the same `get_social_feed`). Rotate/re-publish preserved (rotate doesn't call revoke; deleting resets the (owner,trip) dedupe so re-publish re-emits). Certifier `tests/scenarios/test_second_observer_story_revoke.py` (2 tests); 57 green; mutation-checked.
- **New privacy finding `plan_state.py:772` viewer_id bypass — VERIFIED REAL, FIXED + CERTIFIED.** `_cross_trip_section` called `list_for_trip` without `viewer_id`, leaking member A's PRIVATE primary accommodation label to observer B via 3 read paths (plan-state route, folio, situation builder). Fixed by threading the existing `viewer_id` predicate (`plan_state.py:760/:777/:1234`); shared-group stays untouched. Certifier `tests/scenarios/test_second_observer_private_accommodation.py` (2 tests, incl. shared-stay control); 50 green; mutation-checked (revert → leak test fails with the actual private label).

**Remaining confirmed gaps (post-trio backlog, from Section 5):** #3 vote plan_events history, #4 direct-edit D4 receipt (+concierge no-receipt), #7 stay-choose decision event, #8 booking REST/concierge push asymmetry, #9 mark-booked chat bridge, #10 promote_to_trip genesis audit, #11 room_muted audit, #12 pin idempotency+actor. Plus conformance edits: D1 `missing_voter_ids` non-voter naming, D5 auto-accept breadth. Plus FE follow-up: render `card_type="group_event"` join line (task chip filed). Extend the certifier per-row as each is fixed. Recommendation: let cohort-1 behavior prioritize these — all are honest-but-quiet, none are trust/privacy blockers.
