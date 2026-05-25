# Card Catalog — Vesper's structured-message vocabulary

**Status:** living source of truth. Last full audit: 2026-05-24.
**Scope:** cross-repo. Cards are the agent's primary *non-text* way of talking to
the user — the thing that makes the concierge feel alive instead of a chatbot.
This file is the single place that ties together, for every card:
purpose · the three-layer contract · data shape · who emits it · design status ·
prompt status · known risks.

> Why this exists: cards grew organically across ~13 types, ~10 backend creators,
> and 11 frontend components with no shared registry. Adding one means touching
> ~5 spots in two repos. This catalog is the checklist + the contract so new
> cards land consistently and the existing ones can be brought up to one bar.

---

## 1. The card contract (three layers)

Every card threads the same pipeline. A card is **not** a first-class entity —
it's a `messages` row whose `message_type` (+ optional `metadata.card_type`
discriminator) the frontend recognizes and renders as rich UI.

```
backend creator  (Travel Agent/backend/concierge/structured_messages.py)
  └─ writes a messages row: message_type + metadata{ card_type, …fields }
       │
       ▼
messageMapping.ts  (Travel App/utils/chat/messageMapping.ts)
  └─ message_type (+ metadata.card_type gate) → MessageAttachment.type
       │
       ▼
AttachmentRenderer.tsx  (Travel App/components/chat/AttachmentRenderer.tsx)
  └─ attachment.type → component
```

A card is *agent-driven* when a concierge **tool** the model can call results in
the row being written; *system* when a cron / trigger / route writes it.

### message_type CHECK constraint (authoritative)

`Travel Agent/backend/core/db/_tables/conversations.py:221` (squashed into
`alembic/versions/73a1ca90a2ef_initial_schema.py`). The **only** allowed values:

```
text · tool_result · reaction_card · vote_widget · notification ·
system · venue_card · change_applied · narration
```

**The discriminator pattern is the escape hatch.** To add a new card *without a
migration*, reuse an allowed `message_type` and discriminate with
`metadata.card_type`:
- `trip_shapes` rides on `message_type='reaction_card'` (`card_type='trip_shapes'`).
- `taste_dna_reflection` rides on `message_type='notification'`.

**Rule for new cards:** prefer a `card_type` discriminator under an existing
`message_type`. Only add a brand-new `message_type` (and the Alembic migration to
expand this CHECK) when the card needs its own reaction/aggregation semantics.

### Adding a new card — checklist

1. **Backend creator** in `structured_messages.py` — write a `create_<x>_card()`
   helper. Set `message_type` (allowed value) + `metadata.card_type` + a
   plain-text `content` fallback for clients that can't render it.
2. **Emit it** — from a tool handler (agent-driven) or a trigger (system).
3. **Frontend type** — add `<X>Data` + a `{ type: '<x>'; data }` member to the
   `MessageAttachment` union in `Travel App/types/chat.ts`.
4. **Mapper** — add a `case`/branch in `messageMapping.ts` (`_<x>Attachment`).
5. **Component** — build `components/chat/<X>.tsx` (use the design kit; see §4).
6. **Renderer** — register in `AttachmentRenderer.tsx` (+ a direct branch if it
   needs stable callbacks like reactions).
7. **Body-owning** — if the card renders the message body itself, add its type to
   `BODY_OWNING_TYPES` in `VesperNote.tsx`, `PrivateVesperNote.tsx`,
   `MessageBubble.tsx` so the text doesn't double-render.
8. **Prompt** — if agent-driven, add it to the expressive-surfaces guidance
   (see §5) with a quality bar.
9. **This doc** — add the row + entry.

---

## 2. The catalog

Design score is 1–5 vs. the TripShapes "gold standard" (§4). Family: **A** =
agent-driven (a tool emits it), **S** = system/automatic, **F** = frontend-only
(no backend creator found — mock/legacy).

Design scores updated 2026-05-24 after the design-kit migration (see §4).

| Card | Fam | message_type | card_type | Attachment | Component | Emitter | Design |
|---|---|---|---|---|---|---|---|
| **Trip Shapes** | A | `reaction_card` | `trip_shapes` | `trip_shapes` | `TripShapes.tsx` | `generate_trip_shapes` | **5** ✅kit |
| Reaction Card | A | `reaction_card` | `reaction` | `reaction_card` | `ReactionCard.tsx` | `present_options` | 5 ✅kit |
| Vote Widget | A | `vote_widget` | `vote` | `vote_widget` | `VoteWidgetCard.tsx` | `propose_change` (lazy/active) | 5 ✅kit |
| Venue Card | A | `venue_card` | — | `venue_card` | `VenueCard.tsx` | `post_venue_card` | 4.5 ✅kit |
| Narration | S | `narration` | — | `narration` | `NarrationCard.tsx` | narrate endpoint (user-triggered) | 4 ✅kit |
| Travel-DNA Reflection | S | `notification` | `taste_dna_reflection` | `taste_dna_reflection` | `TravelDNACard.tsx` | `first_contact.py` | 4 |
| Booking Confirmation | A | `booking_confirmation` | `booking_confirmation` | `booking_confirmation` | `BookingConfirmationCard.tsx` | `confirm_booking` | 3.5 ✅kit |
| Booking Proposal | A | `booking_proposal` ⚠️ | — | `booking_proposal` | `BookingProposalCard.tsx` | `propose_booking` (DB row; no message creator yet, §6 #2) | 4 ✅kit |
| Change Applied | A+S | `change_applied` | `change_applied` | `change_applied` | `ChangeAppliedCard.tsx` | `propose_change` auto_approve · cron resolve · `PATCH /proposals` | 3.5 ✅kit |
| Notification | S | `notification` | `notification` | `notification_card` | `NotificationCard.tsx` | `proactive.py`, `proposal_automation.py` | 3.5 ✅kit |
| Lazy-Research badge | S | `text` | (metadata.kind=`lazy_research_answer`) | `lazy_research` | `LazyResearchBadge.tsx` | B-fast research worker | 1 (badge) |
| Itinerary | F | — | — | `itinerary` | `ItineraryCard.tsx` | none found (mock/legacy) | 2 |
| Map | F | — | — | `map_card` | `MapCard.tsx` | none found (mock/legacy) | 2 |

`✅kit` = migrated onto the shared card kit (§4).

⚠️ = contract risk, see §6.

---

## 3. Per-card detail

Key fields only; the component/creator are the full source of truth.

### Trip Shapes — `generate_trip_shapes` → `TripShapes.tsx`
- **Purpose:** cold-start exploration — 2-4 opinionated "what could this trip feel
  like" sketches the group taps to choose a direction. The reaction feeds
  `generate_plan`.
- **Data:** `{ context, prompt, shapes: [{ id, emoji, name, pitch, anchors[], best_for }], my_selection[] }`.
- **Interactive:** each shape is the tappable choice; tap → `record_reaction`.
- **Reference implementation.** New cards should look and feel like this one.

### Reaction Card — `present_options` → `ReactionCard.tsx`
- **Purpose:** group weighs in on a genuine tradeoff (2-3 options) via one tap.
- **Data:** `{ content, options:[{id,label,emoji}], context, deadline, allow_multiple, my_selection[] }`.
- **Anti-pattern (prompted):** do NOT use when the user *delegated* the choice —
  commit to a pick + a venue card instead. See `_prompts_skills.py:615`.

### Vote Widget — `propose_change` (lazy/active) → `VoteWidgetCard.tsx`
- **Purpose:** formal vote on a change proposal; cron auto-resolves at deadline.
- **Data:** `{ proposal_id, title, proposal_type, description, impact_summary, deadline, options[], my_selection[] }`.
- **Gate:** only when `Voting` is enabled for the trip; else auto_approve or a
  reaction card. See `_prompts_skills.py:628`.

### Venue Card — `post_venue_card` → `VenueCard.tsx`
- **Purpose:** the structured form of a recommendation — verdict + headline +
  short take, tap → full venue page. Prompted: "always `post_venue_card` after
  your text" (`_prompts_skills.py:766`).
- **Data:** `{ name, type, detail, matchScore, venue_id }` (+ `recommendation`
  payload in metadata).

### Booking Confirmation — `confirm_booking` → `BookingConfirmationCard.tsx`
- **Purpose:** receipt after a booking; deep-link / phone / in-progress by
  autonomy level. **message_type now allowed (fixed §6 #1; deploy the migration).**

### Booking Proposal — `propose_booking` → `BookingProposalCard.tsx`
- **Purpose:** pre-commit booking offer; card fetches the proposal by id.
  `propose_booking` writes a `booking_proposals` row; the *message* that carries
  `message_type='booking_proposal'` has **no creator found** — likely
  frontend-ready, backend-pending. **⚠️ see §6.**

### Change Applied — auto_approve / cron / route → `ChangeAppliedCard.tsx`
- **Purpose:** visual receipt after a proposal is applied. Emitted three ways
  (agent auto_approve, cron `_do_resolve`, manual `PATCH /proposals/{id}`).

### Notification — `proactive.py` / `proposal_automation.py` → `NotificationCard.tsx`
- **Purpose:** system nudges (deadline approaching, offer expiring, escalation,
  rejection). `notification_type`: side_quest / deadline / weather / update.

### Travel-DNA Reflection — `first_contact.py` → `TravelDNACard.tsx`
- **Purpose:** surfaces 3-5 learned-preference phrases mid-conversation; each
  disputable. Wrapped in `EditorialCard tone="agent"` (inherits letterpress).

### Narration — narrate endpoint → `NarrationCard.tsx`
- **Purpose:** on-the-ground place narration (persona, depth, citations, audio).
  Personal conversation only; user/geofence triggered.

### Lazy-Research badge — B-fast worker → `LazyResearchBadge.tsx`
- A badge on a normal `text` message (metadata.kind=`lazy_research_answer`), not
  a container card — signals "researched live, verify before booking."

---

## 4. Design status & the kit

**Doctrine** (Brand Identity §6-7, Design Language §2-4): cards are *Vesper
artifacts*. They should wear the **letterpress** card (`letterpress.cardBg` +
`letterpress.shadow`), the **sacred-purple** `colors.agent.*` palette (reserved
for Vesper alone), the **fleuron** mark, and the two type scales (Fraunces to
read, Inter to act). Content is **structured data rendered in styled `<Text>`**,
*not* markdown — that's why TripShapes reads clean and why stuffing `**bold**`
into a card leaks raw asterisks.

### The card kit (built 2026-05-24)

The shared kit now exists. Crucially, the **container already existed** — reuse it,
don't re-implement:
- **`components/ui/EditorialCard.tsx`** `tone="agent"` — the letterpress +
  sacred-purple-wash + agent-hairline container. Composes
  `components/brand/LetterpressCard.tsx` (the locked shadow stack). This is the
  card container; never re-implement letterpress inline.
- **`components/chat/CardEyebrow.tsx`** — `Fleuron` (agent accent) + uppercase
  caps label. The card-header signature.
- **`components/chat/CardChipRow.tsx`** — presentational selectable chips
  (parent owns state/haptics); `variant: 'wrap'` (reaction) | `'fill'` (vote);
  sacred-purple selected state.

**New cards:** wrap in `EditorialCard tone="agent"`, add a `CardEyebrow`, use
`CardChipRow` for any tappable options. That reproduces the TripShapes bar by
default — no inline letterpress, no generic purple.

**Migration status:** on the kit — TripShapes, ReactionCard, VoteWidgetCard (5),
VenueCard (4.5), NarrationCard (4), TravelDNACard (4, via EditorialCard already),
and the receipt/notification cards ChangeApplied, BookingConfirmation, Notification
(3.5 — `EditorialCard` default-tone letterpress + their *semantic* accents
olive/slate/type; intentionally not agent-purple, which stays reserved for cards
where Vesper is actively conversing). Remaining: BookingProposalCard (deferred —
not backend-emitted, larger fetched accept/reject component) and the orphan mock
cards (Itinerary, Voting, Map).

**Still missing:** a sanctioned rich-text field for prose-bearing fields (see
markdown risk in §6) — NarrationCard's body still renders as plain `<Text>`.

---

## 5. Prompt status

Agent-side guidance is **good but scattered** across the ~2000-line
`Travel Agent/backend/concierge/_prompts_skills.py`, tool-by-tool:
- when to card vs. propose vs. just-do-it — `:651`
- reaction card vs. delegation — `:615`
- vote widget gating on `Voting` — `:628`
- always `post_venue_card` after text — `:766`
- `generate_trip_shapes` as cold-start move — `:463`

**Expressive-surfaces skill** (`backend/concierge/_prompts_skill_cards.py`) —
*shipped.* Closes both prior gaps: it frames the card vocabulary as a *set* and
gives a per-card **quality bar** (how to fill each well — e.g. trip-shapes:
vivid distinct names, 3-4 concrete non-overlapping anchors), explicitly
deferring *when* to emit to the Tools skill so it doesn't duplicate tuned text.
Split by surface, wired in `_prompts_select.py`:
- `SKILL_EXPRESSIVE_SURFACES` — trip shapes / venue / booking bars; loads in
  **any** chat (recommend-likely, not-ambient).
- `SKILL_GROUP_CARD_SURFACES` — reaction + vote bars; **group-only** (those are
  coordination surfaces), so a 1:1 prose chat never carries group-tool guidance.

The scattered when-to-use guidance still lives in `_prompts_skills.py`. Note:
effectiveness is unverified by eval/dogfood — it passes structural checks only.

**Mode gating is now hard, not just prompt-deep.** The group-coordination cards
(reaction via `present_options`, vote via `propose_change`, plus
`compose_group_message`) are dropped from the tool surface on personal turns
(`_GROUP_ONLY_TOOLS` in `_tools_select.py`), and `_execute_present_options`
rejects a personal call as defense in depth. So a 1:1 can't emit a reaction/vote
card even if the prompt slips. Trip-shapes / venue / booking cards remain
available in both modes. The privacy/compose machinery (`is_group`
strict-compose) is the separate, already-correct gate.

---

## 6. Known contract risks

1. **Booking Confirmation message_type not in CHECK constraint** — ✅ *fixed.*
   `create_booking_confirmation_card` writes `message_type="booking_confirmation"`;
   the insert is wrapped in try/except in `confirm_booking`, so it failed
   *silently* (booking succeeds, no receipt card). Migration
   `b1c9a4e7f2d8_add_booking_card_message_types` adds `booking_confirmation` +
   `booking_proposal` to the CHECK (+ tables.py), using `ADD CONSTRAINT … NOT
   VALID` + `VALIDATE CONSTRAINT` to avoid locking `messages`. **Not yet
   deployed** — the migration must run against prod before the receipt path works.
2. **Booking Proposal has no message creator** — frontend renders it; no backend
   path writes `message_type='booking_proposal'`. Frontend-ready, backend-pending.
3. **Markdown-leak fields — ✅ resolved (structured-only + one rich-text field).**
   Cards are *artifact surfaces*, so the rule is "no markdown in card fields"
   except the one genuinely long-form field. Implemented:
   - **`stripMarkdown()`** (`utils/stripMarkdown.ts`, unit-tested) runs at the
     mapper boundary on the plain-`<Text>` prose fields — reaction `content`,
     notification `content`, vote `title`+`description` — and on BookingProposal
     `notes` in its component (API-fetched, not via the mapper). A stray `**`
     degrades to clean text. It deliberately ignores underscores so snake_case
     (`trip_shapes`) isn't mangled.
   - **NarrationCard body** is the one sanctioned rich-text field — it renders
     through the markdown stack (bold/italic/bullets format properly).
   - Trip-shapes fields are left untouched (structured/short, the gold standard).
4. **Orphan attachment types** — `voting` removed (superseded by the Vote
   Widget; component + union member + mock deleted). `itinerary` and `map_card`
   remain: no backend creator yet, but they read as intended-future features
   (`map_card` has a handler + an empty-state test), so kept as mock-only
   placeholders rather than deleted. Decide later: wire or drop.

---

## 7. Roadmap (proposed)

1. ✅ This catalog (source of truth).
2. ✅ **Design kit** — `EditorialCard` (reused) + `CardEyebrow` / `CardChipRow` +
   a `receipt` tone (left-accent). All emitted cards migrated: TripShapes,
   Reaction, Vote, Venue, Narration, ChangeApplied, BookingConfirmation,
   Notification, BookingProposal. Orphan `voting` removed; `itinerary`/`map_card`
   kept as mock placeholders.
3. ✅ **Prompt module** — `SKILL_EXPRESSIVE_SURFACES` + `SKILL_GROUP_CARD_SURFACES`
   (card vocabulary + per-card quality bars), surface-split. Shipped (see §5).
4. **§6 risks** — booking constraint ✅ fixed (still needs the migration deployed
   to prod, §6 #1); `voting` orphan ✅ removed; markdown policy ✅ implemented
   (`stripMarkdown` guard on card fields + rich-text for the NarrationCard body).
   Only carryover left: **deploy the booking migration.**
