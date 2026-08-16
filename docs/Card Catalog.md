# Card Catalog — Vesper’s structured surfaces

**Status:** current cross-repo source of truth

**Last verified:** 2026-08-15 (founder-approved: Deck is `/dev`, not production Home)

**Implementations:** `travel-app` + `travel-agent`

Cards are Vesper’s structured vocabulary. They are not decoration and they are
not Markdown containers: each card must either carry a decision, a durable
receipt, a useful artifact, or a typed destination.

## 1. Two card systems

### Vesper Home and Deck

Production Vesper Home is the workbench (`VesperWorkbench`). It is not a
decision queue and it does not mount Deck.

Deck faces remain a **deterministic `/dev` fixture** (`/dev/deck-gallery`,
polish lifecycle `dev-fixture`). They are not live product destinations.
Do not describe Home → Deck as the current user journey.

Historical Deck pipeline (lab / compatibility inventory only):

```text
Home producers → ConciergeHomeCard → useConciergeHomeState parser
  → Home hero / rail → Deck face → typed action contract
```

Lab Deck faces (not production Home):

| Substrate | Face | Purpose | Primary completion |
|---|---|---|---|
| `focus.layout=pick` | `DeckPickFace` | Choose one grounded venue | confirmed mutation |
| `focus.layout=compare` | `DeckCompareFace` | Lean between ≥2 active stay candidates | stay vote (`POST …/stay-candidates/{id}/vote`) |
| `focus.layout=call` | `DeckCallFace` | Booking, conflict, or reschedule call | confirmed mutation or seeded chat |
| `focus.layout=brief` | `DeckBriefFace` | Review a drafted plan | navigation / seeded chat |
| `focus.layout=near_you` | `DeckNearYouFace` | Nearby shortlist with Vesper’s read | Maps handoff / confirmed save |
| `structured.layout=vote` | `DeckStructuredFace` | Approve or decline a proposal | confirmed mutation |
| `structured.layout=settle` | `DeckStructuredFace` | Close owed expense shares | confirmed mutation |
| `structured.layout=readiness` | `DeckStructuredFace` | Pre-departure open-loop check | navigation |

`flight` remains parked (no producer; booking schedule-change G2–G4 still dark). Do not revive a Flight face from presentation alone.

Shared decisions in product go to the group-chat `vote_widget`
(`routes.tripChatProposal`), not `DeckStructuredFace`.

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

**Contract ownership (P3):** `docs/contracts/chat-card-types.json` is the
allowlist for `metadata.card_type` values, the FE `MessageAttachment` type list,
and `CHAT_ATTACHMENT_NO_ARRIVAL` reasons. `scripts/sync-chat-card-types-contract.py`
generates FE/BE registries; `make chat-card-types-check` fails on drift. Pilot
payload schemas live under `docs/contracts/chat-attachments/` (currently
`booking_proposal_snapshot` and `map_route`) and generate Zod + Pydantic
validators — expand that set when a card payload needs shared shape proof.
Do not invent new DB `message_type` values for visual variants alone.

### Composed cards (v1 pilot)

`composed_card` is a declarative, native-rendered presentation path for a
server-authored `CardBlueprintV1`. It deliberately separates tool execution,
grounded artifacts, and visual composition: a tool is not a card type, several
artifacts may make one card, and a tool may yield prose only. The blueprint may
select approved semantic blocks, but it cannot contain executable UI, styling
instructions, route strings, or mutation payloads. The app owns dimensions,
accessibility, visual language, and action execution.

The shared schema is `docs/contracts/chat-card-blueprint.v1.schema.json`. v1 is
read-oriented only; booking, proposal, itinerary, and receipt mutations retain
their specialized components and canonical action paths until separately proven.
`body_mode` says whether the card replaces the durable text fallback (`card`) or
accompanies it (`message`), so a compact research/status companion cannot hide a
useful longer answer.

`composed_card.v1` permits at most two visible actions: one primary and one
secondary. The backend validator and mobile parser enforce the same bound.
The renderer never silently drops an accepted action; an invalid or historical
payload falls back to its durable message text instead of partially changing
the card's meaning.

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
| `map_route` | `MapRouteCard` | `notification/map_route` | `post_map_route` | inspect grounded route evidence, open focused Map face |
| `comparison_card` | `ComparisonCard` | `notification/comparison_card` | `post_stay_comparison` | inspect saved stay facts and vote truth, open canonical Stay comparison |
| `composed_card` | `ComposedChatCard` | `notification/composed_card` | composition policy over grounded artifacts | native read-only blueprint with server-resolved safe actions |
| `atlas_draft` | `AtlasDraftCard` | `notification/atlas_draft` | **deprecated; no new production writer** | compatibility render for an owner-scoped historical candidate during the retention window |
| `error_recovery` | `ErrorRecoveryCard` | `notification/error_recovery` | durable planning workflow | background retry status or revised-request handoff |
| `booking_confirmation` | `BookingConfirmationCard` | `booking_confirmation` | `confirm_booking` | receipt, provider link/call/session |
| `booking_proposal` | `BookingProposalCardFetched` | `booking_proposal` | `propose_booking` | confirm/decline after live fetch; display snapshot may paint first |
| `document_edit` | `DocumentEditCard` | notification metadata | document/planning tools | open exact day when available |
| `narration` | `NarrationCard` | `narration` | narration endpoint | audio and cited narration |
| `trip_creation_proposal` | `TripCreationProposalCard` | notification metadata | `propose_trip_creation` | versioned, idempotent trip creation |
| `lazy_research` | `ResearchCard` | text metadata | research worker | informational status; composed companion may offer one server-resolved, read-only Place handoff while its artifact remains current |
| `itinerary_operation` | `ItineraryOperationCard` | notification metadata | itinerary operation preparation | review in canonical itinerary flow |

There are no supported legacy chat `itinerary` or `map_card` attachments.
`map_route` is a persisted evidence object, not an independent map screen: its
primary action opens Map as the second face of Plan.

Strict group-compose privacy handoffs are a typed group-thread state, not a
`MessageAttachment`. The failed agent row persists `message_type=dignified_exception`
inside `error_details`; `messageMapping` projects it to `DignifiedExceptionCard`,
and `PrivateHandoffSeamCard` opens the exact idempotently seeded personal trip
conversation. The group-visible contract contains routing identifiers and seed
status only. The suppressed draft stays in a server-authored system row that
conversation-history endpoints never return.

## 3. Shared action contract

Every actionable card resolves through `utils/cardActionContract.ts`:

| Behavior | Meaning | Completion |
|---|---|---|
| `navigate` | Open a typed in-app destination | immediate |
| `mutate` | Change durable domain state | confirmed |
| `seeded_chat` | Open Vesper with structured card context | immediate |
| `external` | Open a validated external URL or phone handoff | immediate |
| `dismiss` | Remove or decline without another destination | immediate or confirmed when persisted |

Labels must describe the actual behavior. Near You opens native directions and
performs a confirmed save directly; neither action detours through chat.

Route payload rules:

- IDs used for deduplication or provenance are never destinations.
- Notifications navigate only with a typed `destination` object.
- Home Plan actions preserve the backend itinerary `day_id` UUID.
- Missing destinations remove the CTA; they do not fall back to a no-op tap.
- Unknown backend Home actions may fall back to seeded chat, never an invented
  route.

### Deliberate non-attachments

These are real `messages` rows but **not** `MessageAttachment` types. Do not
add them to the chat registry (§2) without a product decision that they need
card chrome, actions, or a typed destination.

| Persistence | Producer | Thread treatment |
|---|---|---|
| `booking_update` message_type | `booking_subscribers.py` on `booking.*` events | Ambient agent prose (`content`); metadata holds `booking_event` + payload for idempotency/debug. Full booking detail lives on trip / booking surfaces. **Not** a card — see §9. |
| `notification` + `card_type=group_event` | group systems | Centered system line, not a card. |

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

The shared vocabulary currently projects persisted Home lifecycle, solo proposal
previews, consequential receipt status, and the Deck lab. New interactive cards
must use it rather than inventing local `idle/submitting/done` unions.

Every uncertain consequential write has an exact durable readback: venue
commitments, proposal votes, settled expense shares, saved entities, applied
reschedules, booking proposals, provider holds, and Home feedback suppression.
A card-feed disappearance is never treated as proof that a consequential write
landed.

## 5. Arrival and motion contract

Card-producing tool events carry a typed `card_envelope`. Start events identify
the attachment type so `CardArrivalPlaceholder` reserves the correct shell;
completion events add the persisted card/message ID when available. The
reservation remains through prose streaming and briefly across the history
handoff, then the exact attachment enters with the shared soft-card animation.

Only known card-producing tools reserve space (`docs/contracts/card-arrival.json`).
Ordinary prose answers do not. Attachment types that are produced outside the
streamed tool loop (async workflows, narrate, proactive notifications, side
effects of another tool) are listed in
`docs/contracts/chat-card-types.json` → `no_arrival` (generated into
`travel-app/utils/chat/cardCatalogContract.ts` as `CHAT_ATTACHMENT_NO_ARRIVAL`)
with an explicit reason — every registry type must be either arrival-reserved
or no-arrival. Do not invent mid-turn shells for no-arrival types.

**Early handoff (P2):** when `tool_complete` supplies a `card_id` that is not yet
in the local thread, the client fetches a recent conversation history slice and
upserts that durable row so the placeholder can morph without waiting solely on
turn-end invalidate. Full history refetch and the 8s materialization timeout
remain authority. Device proof:
`docs/working/card-arrival-device-cert-2026-07-30.md`.

Lab Deck behavior (not production Home):

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
- one assistant turn emits at most one primary structured artifact; alternatives
  belong inside that artifact, not in a stack of competing cards
- prose introduces the human beat, interprets the choice, or records an honest
  limitation; it does not repeat the artifact payload
- body-owning attachments must be registered in `components/chat/bodyOwning.ts`
- interactive controls expose busy, disabled, error, and accessibility states
- cards without enough substrate stay warm on Home or do not render

Chat attachments also share one telemetry boundary. It records an 800 ms
exposure, action tap/start, callback/resolver return, and explicitly reported
known outcomes using the message ID and attachment type. A callback return is
not a durable commit; only an owning-domain readback may report committed,
failed, uncertain, reconciled, or superseded truth. Mutation telemetry is
best-effort and never changes interaction behavior.

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
3. Add the `metadata.card_type` (and FE attachment name) to
   `docs/contracts/chat-card-types.json`; run
   `python3 scripts/sync-chat-card-types-contract.py`.
4. Add or update the `MessageAttachment` data type.
5. Parse and validate in `messageMapping.ts` (use a pilot schema under
   `docs/contracts/chat-attachments/` when the payload should be shared).
6. Register the component in `AttachmentRenderer.tsx`.
7. Declare its action behavior and typed destination.
8. Use the shared interaction state machine for any consequential action.
9. Add body ownership when the attachment renders the message prose.
10. Add arrival-tool mapping in `docs/contracts/card-arrival.json` if it is
    produced during a streamed turn; otherwise add a `no_arrival` reason.
11. Test mapping, failure/retry semantics, navigation, reduced motion, Dynamic
    Type, and narrow-screen overflow.
12. Update this catalog in the same change.

### 8.1 Deprecating or retiring a card

A card type is **never removed outright** from `attachments` or
`metadata_card_types`. Persisted messages are immutable history; dropping a
type from the generated union would either delete a call site's compile-time
knowledge of it or — for a `body_mode: 'card'` composed card, whose durable
text fallback is deliberately suppressed once a client can render the native
body — leave historical messages with nothing to show at all.

Instead, retirement is a status change in
`docs/contracts/chat-card-types.json`'s `attachment_lifecycle` map:

1. **`deprecated`** — no new producer should target this type; it still
   renders its real component normally. Use this while a successor is being
   proven out.
2. **`retired`** — `AttachmentRenderer` renders `RetiredCardFallback`
   (the message's persisted `content` text, as ordinary prose) instead of the
   real component, for every existing and future message of that type. Stop
   producing it first; retiring does not stop production on its own.

To retire a type:

1. Confirm no producer still emits it (`grep` the creator function; check
   `no_arrival` / `card-arrival.json` reservations).
2. Set its `attachment_lifecycle` status to `"retired"` in
   `docs/contracts/chat-card-types.json`. Optionally record `successor` if
   another type replaces it.
3. Run `python3 scripts/sync-chat-card-types-contract.py` — regenerates
   `GENERATED_CHAT_ATTACHMENT_STATUS` and `GENERATED_RETIRED_CHAT_ATTACHMENT_TYPES`
   on both sides. `make chat-card-types-check` fails if `attachments` and
   `attachment_lifecycle` ever disagree on membership (a type without a
   lifecycle entry, or a lifecycle entry naming nothing).
4. The registry entry, `MessageAttachment` union member, and
   `messageMapping.ts` branch all stay — they are what keeps historical
   messages type-safe and mappable. Do not delete them.
5. Update this catalog's §2 registry row to note the retirement and successor.

A retired type's component and any producer-side code become genuinely dead
and may be deleted in application code once no message row references it and
the retirement has been live long enough to be confident of that (query the
`messages` table for the `message_type`/`card_type` pair). The contract entry
itself still never disappears — it is the permanent record that the type
existed.

## 9. Deliberate open work

- **Flight stays parked** until booking schedule-change (G2–G4) is real and a
  `layout='flight'` producer can emit from that substrate. Do not revive a
  Flight face from presentation alone. Compare is live via stay candidates
  (`stay_compare` → `focus.layout='compare'` → stay vote).
- Add new Home mechanics families only with a real producer and complete card
  substrate. Dormant Trust and Transact faces were removed pre-launch.
- **Progressive card-field streaming stays deferred** (design-decisions
  agent-chat C.3). Arrival envelopes remain content-free identity/type hints;
  first-paint latency work uses reserved shells plus history reconciliation
  (and, when prioritized, slim authenticated handoff / targeted message fetch)
  — not partial mutable card bodies on SSE. Reopen only with an explicit new
  design decision and an allowlist (e.g. research/preview), never for
  receipts or consequential mutations.
- **`booking_update` is ambient prose, not a chat card** (decided 2026-07-30).
  Keep the DB `message_type` for storage, idempotency, and subscriber emits;
  keep FE mapping as ordinary agent text (no `MessageAttachment`). Promote to
  a registry card only if product later needs a typed destination or
  structured receipt beyond `booking_confirmation` / `booking_proposal`.
  Cross-link: `travel-agent/docs/working/State of Booking 2026.md` (Concierge
  subscriber).
