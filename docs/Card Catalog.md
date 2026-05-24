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
| Booking Confirmation | A | `booking_confirmation` ⚠️ | `booking_confirmation` | `booking_confirmation` | `BookingConfirmationCard.tsx` | `confirm_booking` | 2 |
| Booking Proposal | A | `booking_proposal` ⚠️ | — | `booking_proposal` | `BookingProposalCard.tsx` | `propose_booking` (DB row; card path unverified) | 2 |
| Change Applied | A+S | `change_applied` | `change_applied` | `change_applied` | `ChangeAppliedCard.tsx` | `propose_change` auto_approve · cron resolve · `PATCH /proposals` | 2 |
| Notification | S | `notification` | `notification` | `notification_card` | `NotificationCard.tsx` | `proactive.py`, `proposal_automation.py` | 2 |
| Lazy-Research badge | S | `text` | (metadata.kind=`lazy_research_answer`) | `lazy_research` | `LazyResearchBadge.tsx` | B-fast research worker | 1 (badge) |
| Itinerary | F | — | — | `itinerary` | `ItineraryCard.tsx` | none found (mock/legacy) | 2 |
| Voting | F | — | — | `voting` | `VotingCard.tsx` | none found (mock/legacy; superseded by Vote Widget) | 1 |
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
  autonomy level. **⚠️ message_type not in CHECK constraint — see §6.**

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

**Migration status:** the chip family + recommendation/narration cards are on the
kit — TripShapes, ReactionCard, VoteWidgetCard (5), VenueCard (4.5), NarrationCard
(4), plus TravelDNACard (4, via EditorialCard already). Still utilitarian (no kit):
the receipt-style cards (Booking Confirmation, Booking Proposal, Change Applied),
Notification, and the orphan mock cards (Itinerary, Voting, Map).

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

**Gaps:**
- No single "expressive surfaces" framing — nowhere does the agent see its card
  vocabulary as a *set* ("here are your rich surfaces, here's when each shines").
- No per-card **quality bar** — guidance says *when* to emit, rarely *how to fill
  the fields well* (e.g. trip-shapes: vivid distinct names, 3-4 concrete anchors,
  no overlap). This is the gap between "emits a card" and "emits a great card."

---

## 6. Known contract risks

1. **Booking Confirmation message_type not in CHECK constraint** —
   `create_booking_confirmation_card` writes `message_type="booking_confirmation"`
   (`structured_messages.py:450`) but the constraint allows only the 9 values in
   §1. Insert raises IntegrityError against Postgres. **Fix:** either a migration
   expanding the CHECK, or reuse an allowed `message_type` + `card_type`
   discriminator. Verify whether the `confirm_booking` path has run against a real
   DB. Same applies to **Booking Proposal** (`booking_proposal` also absent).
2. **Booking Proposal has no message creator** — frontend renders it; no backend
   path writes `message_type='booking_proposal'`. Frontend-ready, backend-pending.
3. **Markdown-leak fields** — these render prose in plain `<Text>` and will show
   raw `**` if the backend ever puts markdown there: NarrationCard body
   (highest), VoteWidgetCard `description`, BookingProposalCard `notes`,
   ReactionCard/NotificationCard `content`. **Policy needed:** structured data
   only, or one sanctioned rich-text field type.
4. **Orphan attachment types** — `itinerary`, `voting`, `map_card` have frontend
   components but no backend creator (mock/legacy). `voting` is superseded by the
   Vote Widget. Decide: wire, or delete.

---

## 7. Roadmap (proposed)

1. ✅ This catalog (source of truth).
2. ✅ **Design kit** — `EditorialCard tone="agent"` (reused) + new `CardEyebrow` /
   `CardChipRow`; migrated TripShapes, Reaction, Vote, Venue, Narration to the
   bar. *Remaining:* receipt cards (Booking Confirmation/Proposal, Change
   Applied), Notification.
3. **Prompt module** — a unified "expressive surfaces" skill + per-card quality
   bars, kept in sync with §2.
4. **Resolve §6 risks** — booking message_type migration/discriminator; markdown
   policy (sanctioned rich-text field for NarrationCard body etc.); orphan cleanup.
