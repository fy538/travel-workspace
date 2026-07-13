# Card Catalog — Vesper’s structured surfaces

**Status:** current cross-repo source of truth

**Last verified:** 2026-07-12

**Implementations:** `travel-app` + `travel-agent`

Cards are Vesper’s structured vocabulary. They are not decoration and they are
not Markdown containers: each card must either carry a decision, a durable
receipt, a useful artifact, or a typed destination.

## 1. Two card systems

### Vesper Home and Deck

The Home feed is assembled from real world state by
`backend/home/concierge_feed/`. A warm glance appears as the Home hero or rail;
only cards with `focus` or `structured` substrate may enter the dark Deck.

Pipeline:

```text
Home producers → ConciergeHomeCard → useConciergeHomeState parser
  → Home hero / rail → Deck face → typed action contract
```

Live Deck faces:

| Substrate | Face | Purpose | Primary completion |
|---|---|---|---|
| `focus.layout=pick` | `DeckPickFace` | Choose one grounded venue | confirmed mutation |
| `focus.layout=call` | `DeckCallFace` | Booking, conflict, or reschedule call | confirmed mutation or seeded chat |
| `focus.layout=brief` | `DeckBriefFace` | Review a drafted plan | navigation / seeded chat |
| `focus.layout=near_you` | `DeckNearYouFace` | Nearby shortlist with Vesper’s read | seeded chat |
| `structured.layout=vote` | `DeckStructuredFace` | Approve or decline a proposal | confirmed mutation |
| `structured.layout=settle` | `DeckStructuredFace` | Close owed expense shares | confirmed mutation |
| `structured.layout=readiness` | `DeckStructuredFace` | Pre-departure open-loop check | navigation |

`compare` and `flight` remain deliberately dormant: components may exist, but
no trustworthy producer emits their substrate. They must not be dispatched
until a real data contract exists.

Home data is deterministic. Small schema-enforced LLM calls may add grounded
judgment (`pick_judgment.py`, `deck_take.py`); failure keeps deterministic copy.

### Structured cards in chat

Chat cards are persisted message rows:

```text
tool / system producer
  → message_type + metadata.card_type
  → utils/chat/messageMapping.ts
  → MessageAttachment
  → components/chat/AttachmentRenderer.tsx
```

The database `message_type` CHECK is authoritative. New visual variants should
normally reuse an allowed message type plus `metadata.card_type`; add a database
message type only when storage or aggregation semantics genuinely differ.

## 2. Current chat registry

This table mirrors the `MessageAttachment` union and `AttachmentRenderer`
registry. A row absent here is not a supported chat card.

| Attachment | Component | Persistence discriminator | Primary producer | Interaction |
|---|---|---|---|---|
| `venue_card` | `VenueCard` | `venue_card` | `post_venue_card` | venue detail when ID exists |
| `reaction_card` | `ReactionCard` | `reaction_card/reaction` | `present_options` | optimistic reaction + rollback |
| `trip_shapes` | `TripShapes` | `reaction_card/trip_shapes` | `generate_trip_shapes` | choose shape, continue planning |
| `vote_widget` | `VoteWidgetCard` / `PreviewEditCard` | `vote_widget` | `propose_change` | group vote or solo approval gate |
| `notification_card` | `NotificationCard` | `notification/notification` | proactive and automation systems | typed destination or external URL only |
| `taste_dna_reflection` | `TravelDNACard` | `notification/taste_dna_reflection` | reflection trigger | dispute learned phrases |
| `change_applied` | `ChangeAppliedCard` | `change_applied` | proposal apply paths | receipt, undo, uncertain state |
| `plan_ready` | `PlanReadyCard` | `notification/plan_ready` | plan generation/refinement | exact Plan destination, revision/undo |
| `booking_confirmation` | `BookingConfirmationCard` | `booking_confirmation` | `confirm_booking` | receipt, provider link/call/session |
| `booking_proposal` | `BookingProposalCardFetched` | `booking_proposal` | `propose_booking` | confirm/decline fetched proposal |
| `document_edit` | `DocumentEditCard` | notification metadata | document/planning tools | open exact day when available |
| `narration` | `NarrationCard` | `narration` | narration endpoint | audio and cited narration |
| `trip_creation_proposal` | `TripCreationProposalCard` | notification metadata | `propose_trip_creation` | versioned, idempotent trip creation |
| `lazy_research` | `ResearchCard` | text metadata | research worker | informational status |

There are no supported chat `itinerary` or `map_card` attachments. Map is a
face of Plan, not a standalone chat card.

## 3. Shared action contract

Every actionable card resolves through `utils/cardActionContract.ts`:

| Behavior | Meaning | Completion |
|---|---|---|
| `navigate` | Open a typed in-app destination | immediate |
| `mutate` | Change durable domain state | confirmed |
| `seeded_chat` | Open Vesper with structured card context | immediate |
| `external` | Open a validated external URL or phone handoff | immediate |
| `dismiss` | Remove or decline without another destination | immediate or confirmed when persisted |

Labels must describe the actual behavior. A chat-mediated action cannot say
“Take me there” or “Save”; it says “Ask for directions” or “Ask Vesper to save.”

Route payload rules:

- IDs used for deduplication or provenance are never destinations.
- Notifications navigate only with a typed `destination` object.
- Home Plan actions preserve the backend itinerary `day_id` UUID.
- Missing destinations remove the CTA; they do not fall back to a no-op tap.
- Unknown backend Home actions may fall back to seeded chat, never an invented
  route.

## 4. Shared interaction state machine

Consequential cards use `utils/cardInteractionState.ts`:

```text
ready → acting → committed
             ↘ failed_retryable → acting
             ↘ uncertain → reconciling → committed / uncertain

terminal: committed · superseded · dismissed
```

Vocabulary:

- `ready`: safe to act
- `acting`: a confirmed-completion write is in flight
- `committed`: server-confirmed consequence
- `failed_retryable`: request is known not to have landed; retry is safe
- `uncertain`: write may have landed; do not offer blind retry
- `reconciling`: re-reading durable state
- `superseded`: a newer version or expired moment replaced the card
- `dismissed`: explicitly removed, declined, or undone

The shared vocabulary currently projects persisted Home lifecycle, drives Deck
transactions, solo proposal previews, and consequential receipt status. New
interactive cards must use it rather than inventing local `idle/submitting/done`
unions.

## 5. Arrival and motion contract

Card-producing tool events reserve a structured-card footprint with
`CardArrivalPlaceholder` before the persisted attachment is refetched. The
reservation remains through prose streaming and briefly across the history
handoff. The actual attachment then enters with the shared soft-card animation.

Only known card-producing tools reserve space. Ordinary prose answers do not.

Deck behavior:

- opening: scrim fade + card lift
- confirmed resolution: current card exits left, next enters right
- failed mutation: current card remains in place
- width: capped by the canon 341pt face and available window width
- height: capped by safe-area space and adjusted for font scale
- overflow: vertical scrolling, with a visible indicator for enlarged text
- Reduced Motion: all transitions collapse without changing state semantics

## 6. Design construction

Chat cards compose `VesperChatCardKit` (`ChatCardFrame`, `ChatCardHeader`,
`ChatActionRow`, diff/meta primitives). Home cards compose the Vesper card faces
and shared button/card primitives. Do not recreate shadows, radii, action pills,
or receipt rows inline.

Rules:

- structured fields are plain text, never Markdown
- one card per conversational moment
- prose introduces the human beat; it does not repeat the card
- body-owning attachments must be registered in `components/chat/bodyOwning.ts`
- interactive controls expose busy, disabled, error, and accessibility states
- cards without enough substrate stay warm on Home or do not render

## 7. Agent guidance

`backend/concierge/_prompts_skill_cards.py` owns the expressive-surface quality
bar. `_tools_select.py` owns availability. Group reaction/vote tools are hard
gated out of private turns; trip shapes, venue, booking, planning, and trip
creation surfaces are loaded only when their turn context warrants them.

The model chooses a sanctioned tool. It does not choose a React component,
route string, lifecycle state, or arbitrary metadata shape.

## 8. Adding or changing a card

1. Define the backend creator and plain-text fallback.
2. Emit from a sanctioned tool or system producer.
3. Add or update the `MessageAttachment` data type.
4. Parse and validate in `messageMapping.ts`.
5. Register the component in `AttachmentRenderer.tsx`.
6. Declare its action behavior and typed destination.
7. Use the shared interaction state machine for any consequential action.
8. Add body ownership when the attachment renders the message prose.
9. Add arrival-tool mapping if it is produced during a streamed turn.
10. Test mapping, failure/retry semantics, navigation, reduced motion, Dynamic
    Type, and narrow-screen overflow.
11. Update this catalog in the same change.

## 9. Deliberate open work

- Replace chat-mediated Near You “save” and “directions” with direct typed
  mutations/navigation when those product capabilities exist.
- Add a reconciliation read for every `uncertain` write, rather than requiring
  manual verification for the remaining cases.
- Activate Compare or Flight only after their backend substrate and routing are
  real; do not revive their dormant components from presentation alone.
