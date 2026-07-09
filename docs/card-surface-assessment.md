# Vesper — Card Surface Assessment

**Investigation only — no code changed.** This document inventories every real card surface in
`travel-app` (render) and `travel-agent` (the text fields inside cards), and maps them against the
design canon's six card *mechanics* families (Surface · Decide · Transact · Explain · Keep · Trust).
It feeds a design-side polish of `Vesper Cards.html`.

Every claim carries a `file:line`. Paths are relative to `travel-workspace/` unless noted.

**Scope note.** A *card* = a bordered/elevated object with its own container. Plain list rows (the Row
System) are excluded. Shell/anatomy primitives (`CardShell`, `CardHead`, `ActionRow`, `KindTag`,
`CardArt`, `CardStates`, `CardSurface`, `ui/Card`, `EditorialCard`, `LetterpressCard`,
`VesperChatCardKit`) are inventoried once as the shell layer (§3), not as content cards.

---

## TL;DR — the three things `Vesper Cards.html` most needs to resolve

1. **The code's card-family enum is the *deprecated* taxonomy, not the six mechanics.**
   `utils/vesperCardFamilies.ts:6` defines the live family type as `call · prepared · live · signal ·
   capture · resume · starter` — the exact legacy content-intent names the canon says to retire. Every
   glyph, `KindTag`, tint, and Deck-face route keys off these seven, not off Surface/Decide/Transact/
   Explain/Keep/Trust. The canon must decide whether these stay as a *glance-presentation* layer that
   sits under the six mechanics, or get renamed. Today there is no representation of the six mechanics
   anywhere in code.

2. **Three parallel card ecosystems, not one.** (a) The canon `CardShell` — radius **14**, `paper`,
   letterpress shadow (`components/vesper-cards/CardShell.tsx:41`, `constants/cardSurface.ts:24,58`) —
   used by home + concierge. (b) **Chat** artifacts use `ChatCardFrame` instead — radius **16**, a
   separate "glass" shadow (`components/chat/VesperChatCardKit.tsx:213,217`). (c) **Trust** receipts
   (Atlas memory/data) build on their own `TrustControlsKit`, and the Atlas share card is full-bleed
   9:16 outside the paper system. Plus `ui/Card` (r12) backs booking panels. The canon should name
   **one** paper-object radius + shadow and decide whether Trust receipts are a sanctioned variant.

3. **The six families have no home for "process/progress" or "forecast," and two receipt cards each
   span 3–4 families.** `ScanProgressCard`, `ResearchCard` (running), and the capture-nudge submitting
   state are long-running-operation feedback that fits none of the six. `CostsEstimateCard` is an
   explicit *non-truth* forecast ("not ledger truth"). And `FolioReceiptCard` / `VesperReceipt` each mix
   Surface+Transact+Trust+Explain. The canon should either add a mechanic (Process) or rule these into
   Surface/Explain explicitly, and define a shared **receipt anatomy** that Transact and Trust both draw.

---

## 1 + 2. Card inventory mapped to the six families

Grouped by surface. **Family** column: primary family, `+` for a genuine secondary. 🚩 flags a card
that spans 3+ families, doesn't fit, or carries a legacy name. State column: L=loading, E=empty,
Er=error, ⊘=renders raw (no non-happy states).

### Vesper home deck (the "focus" cards)
Family enum lives in `utils/vesperCardFamilies.ts`; faces in `components/vesper-cards/faces/`.

| Card | file:line | Shows | Family | State |
|---|---|---|---|---|
| CardCall | `components/vesper-cards/faces/CardCall.tsx:29` | Urgent trip action / constraint alert; reason bullets + CTA | **Decide** | ⊘ (data) |
| CardPrepared | `faces/CardPrepared.tsx` | Agent-prepared brief / retrospective / closeout | **Explain** | ⊘ |
| CardLive | `faces/CardLive.tsx` | Live/imminent trip, daily brief, weather, near-you | **Surface** | ⊘ |
| CardSignal | `faces/CardSignal.tsx` | Saved-cluster / memory-echo pattern | **Surface** | ⊘ |
| CardCapture | `faces/CardCapture.tsx` | Capture-a-moment prompt | **Keep** | ⊘ |
| CardResume | `faces/CardResume.tsx` | Resume an in-progress thread | **Surface** | ⊘ |
| CardStarter | `faces/CardStarter.tsx` | Begin-a-trip invitation (dashed shell) | **Surface** +Explain | ⊘ |
| RailCard | `components/vesper-cards/RailCard.tsx` | Compact 154×116 in-motion rail card; tap → Deck (governed by `home_card_rail`) | **Surface** | ⊘ |
| CardStates | `components/vesper-cards/CardStates.tsx:17` | Shared loading / preparing / inactive renderers | *(shell state kit)* | **L** + preparing |
| Deck | `components/focus-home/Deck.tsx:70` | Full-screen triage overlay; universal action bar | *(container)* | via faces |
| DeckPickFace | `components/focus-home/DeckPickFace.tsx` | Pick with judgment (reasoning/tradeoff/why-not) | **Decide +Explain** 🚩 | ⊘ |
| DeckCallFace / DeckCompareFace / DeckStructuredFace / DeckBriefFace | `components/focus-home/Deck*Face.tsx` | Deck renderings of call / compare / structured / brief | Decide (brief=Explain) | ⊘ |

> 🚩 **Legacy naming, whole system.** `call/prepared/live/signal/capture/resume/starter`
> (`vesperCardFamilies.ts:13–44`, mirrored in `components/concierge/VesperCardKit.tsx`) are the
> deprecated content-intent names. Mapping to canon: call→Decide, prepared→Explain, live/signal/
> resume/starter→Surface, capture→Keep. This is the single biggest rename surface in the app.

### Chat in-thread artifact cards
All wrap `ChatCardFrame` (`components/chat/VesperChatCardKit.tsx:55`).

| Card | file:line | Shows | Family | State |
|---|---|---|---|---|
| VenueCard | `components/chat/VenueCard.tsx:29` | Place object: art, name, detail, match score, View | **Surface** +Explain | ⊘ |
| ResearchCard | `components/chat/ResearchCard.tsx:30` | Live research step list w/ per-step status | **Explain** (+Process 🚩) | **L / running / Er** |
| VoteWidgetCard | `components/chat/VoteWidgetCard.tsx:47` | Formal vote: options, deadline, outcome banner | **Decide** | outcome + empty-options |
| NotificationCard | `components/chat/NotificationCard.tsx:31` | Side-quest / deadline / weather / update notice | **Surface** | ⊘ |
| BookingConfirmationCard | `components/chat/BookingConfirmationCard.tsx:50` | Booking receipt: venue, method, open/in-progress | **Transact** | provider states |
| ChangeAppliedCard | `components/chat/ChangeAppliedCard.tsx:43` | Plan-diff receipt: before/after, Undo | **Trust** | undo idle/reverted/failed |
| PlanReadyCard | `components/chat/PlanReadyCard.tsx:23` | "Your plan is ready" receipt + deep link | **Surface** | ⊘ |
| PreviewEditCard | `components/chat/PreviewEditCard.tsx:49` | "Preview before it lands" gate: keep/dismiss | **Decide +Trust** 🚩 | pending/kept/dismissed/failed |
| DocumentEditCard | `components/chat/DocumentEditCard.tsx:28` | Draft-edit diff receipt + open draft | **Trust** +Explain | ⊘ |
| NarrationCard | `components/chat/NarrationCard.tsx:53` | Place narration: persona line, body, audio, lenses | **Explain** | audio L/play; cache-miss disable |
| PrivacyHandoffCard | `components/chat/PrivacyHandoffCard.tsx:30` | Privacy-boundary notice; I understand / Not now | **Trust** | ⊘ |
| ReactionCard | `components/chat/ReactionCard.tsx:34` | Lightweight reaction chips (optimistic) | **Decide** (light) | optimistic rollback |
| VoiceSegmentCard | `components/chat/VoiceSegmentCard.tsx:24` | Completed voice call: duration, transcript | **Keep** | expand/collapse |
| DignifiedExceptionCard | `components/chat/group/DignifiedExceptionCard.tsx:35` | Group privacy seam → take private | **Trust** | handoff state |

### Chat banners (card-adjacent; own container, no list-row)
| Banner | file:line | Shows | Family | State |
|---|---|---|---|---|
| ErrorBanner | `components/chat/ErrorBanner.tsx:29` | Slim error + inline retry | *(system chrome)* 🚩 | Er only |
| LiveCompanionBanner | `components/chat/LiveCompanionBanner.tsx:28` | Active voice-guide arc: entity, stops, End | **Surface** | isClosing |
| GeofenceBanner | `components/chat/GeofenceBanner.tsx:29` | "You're near X" — Narrate / dismiss | **Surface** | isNarrating |

### Concierge home
| Card | file:line | Shows | Family | State |
|---|---|---|---|---|
| ConciergeCaptureNudgeCard | `components/concierge/ConciergeCaptureNudgeCard.tsx:19` | Capture nudge; expands to input | **Keep** | idle/composing/submitting/captured + Er |
| ConciergeCardDecisionSheet | `components/concierge/ConciergeCardDecisionSheet.tsx` | Resolve a call/prepared card action | **Decide** | ⊘ |

### Booking flow
| Card | file:line | Shows | Family | State |
|---|---|---|---|---|
| BookingProposalCard | `components/booking/BookingProposalCard.tsx:50` | Full API proposal: venue, price, policy, provider | **Transact** | proposal + provider states |
| BookingReceiptPrimitives | `components/booking/BookingReceiptPrimitives.tsx` | Shared header/vesper-line/status for receipts | *(Transact kit)* | — |

### Trip-plan inline banners
| Card | file:line | Shows | Family | State |
|---|---|---|---|---|
| BlockChangedBanner | `components/trip-plan/BlockChangedBanner.tsx:36` | "Vesper changed this" + View diff / Undo | **Trust** | dismissed (persisted) / undoPending |
| BlockProposedBanner | `components/trip-plan/BlockProposedBanner.tsx` | Proposed (not-yet-applied) change | **Decide** +Trust | ⊘ |
| ConcurrentEditBanner | `components/trip-plan/ConcurrentEditBanner.tsx` | Concurrent-edit conflict | **Trust** | ⊘ |

### Trip map peeks
| Card | file:line | Shows | Family | State |
|---|---|---|---|---|
| TripMapStopPeekCard | `components/trip-map/TripMapStopPeekCard.tsx:62` | Stop: time, sequence, distance, Open/Ask/Mute | **Surface** | ⊘ |
| TripMapNeighborhoodCard | `components/trip-map/TripMapNeighborhoodCard.tsx:31` | District name + character line | **Surface** +Explain | ⊘ |
| TripMapPhotoCard | `components/trip-map/TripMapPhotoCard.tsx:43` | Full-bleed photo + captured-at | **Keep** | ⊘ |

### Memory / stories
| Card | file:line | Shows | Family | State |
|---|---|---|---|---|
| TripLogCard | `components/memory/TripLogCard.tsx:52` | Trip title, dates, story badge | **Keep** | ⊘ |
| StoryArchiveCard | `components/memory/StoryArchiveCard.tsx:19` | Saved story: kicker, hero, section count, save | **Keep** | isSaved |
| TripStorySectionCard | `components/memory/TripStorySectionCard.tsx:49` | Story section: kicker, heading, body, photo | **Keep** | edited stamp |
| PhotoSlotCard | `components/memory/PhotoSlotCard.tsx:23` | Photo-picker slot for a section | **Keep** | **L / permission / Er** |

### Trip receipts / status  🚩 the over-loaded cards
| Card | file:line | Shows | Family | State |
|---|---|---|---|---|
| FolioReceiptCard | `components/trip/FolioReceiptCard.tsx:50` | Day-at-a-glance facet (stay/decisions/plan/route) × state × evidence | **Surface + Transact + Trust + Explain** 🚩🚩 | state-variant tone |
| VesperReceipt | `components/receipts/VesperReceipt.tsx:61` | Trust receipt: compact / detail / source / status modes | **Trust + Transact + Explain** 🚩 | mode-driven; degraded sources |
| ConsequenceBanner | `components/ui/ConsequenceBanner.tsx:23` | Consequence update: Undo or See-why, dismiss | **Trust** | showWhy disclosure |

### Expenses / costs
| Card | file:line | Shows | Family | State |
|---|---|---|---|---|
| CostsEstimateCard | `components/expense/CostsEstimateCard.tsx:18` | Planning estimate ("not ledger truth"): total, per-person | **Transact?** 🚩 (Forecast — no money moves) | ⊘ |

### Trips home / discover / identity
| Card | file:line | Shows | Family | State |
|---|---|---|---|---|
| TripsHomeCards (TableCard) | `components/trips/TripsHomeCards.tsx:50` | Trip/draft/dream/saved table card | **Surface** | tone variants |
| TripHeroCard | `components/trips/hero/TripHeroCard.tsx` | Featured trip hero | **Surface** | (per hero spec) |
| DiscoverPinPeekCard | `components/discover/DiscoverPinPeekCard.tsx:48` | Pin peek: verdict, state chips, affinity, Open/Ask | **Surface + Explain + Keep** 🚩 | chips/affinity |
| ExemplarInlineCard | `components/discover/reader/ExemplarInlineCard.tsx:37` | Dossier/angle venue callout + Save | **Explain** +Keep | saved/savePending |
| TravelDNACard | `components/me/TravelDNACard.tsx:44` | Reflection phrases + "how Vesper picked this up" | **Explain** +Keep | dismiss + rollback |
| ScanProgressCard | `components/atlas/ScanProgressCard.tsx:28` | Photo-scan progress bar, count, cancel | *(Process)* 🚩 no fit | isLowPowerMode / % |

### Stay / proposals (added in coverage recheck)
| Card | file:line | Shows | Family | State |
|---|---|---|---|---|
| StayCard | `components/stay/StayCard.tsx:22` | One accommodation object, **8 variants** (suggested/confirmed/held/vote/split/missing/private/past) | **Surface + Decide + Transact** 🚩 | 8 variants + missing-degrades-to-dashed-row |
| ProposalReceipt | `components/trip/proposal-detail/ProposalReceipt.tsx` | Proposal-detail receipt, **10 kinds** (applied/reverted/lazy_consensus/booking_hold/conflict/swap/vote…); owns the `proposalReceipt` content contract | **Decide + Trust** 🚩 | kind-variant + vote actions |
| DecisionPrimitives | `components/collaboration/DecisionPrimitives.tsx` | Decide-family primitive kit (neutral/vesper/urgent/success tones) on `CardSurface` | *(Decide kit)* | tone variants |
| StoryReadyEntry | `components/trips/StoryReadyEntry.tsx` | "Your story is ready" entry card | **Surface** +Keep | ⊘ |

### Atlas — memory share & trust receipts (added in coverage recheck)
These sit **outside** the `CardShell` paper-object system — the trust receipts use `TrustControlsKit`,
the share card is a full-bleed 9:16 screenshot format.

| Card | file:line | Shows | Family | State |
|---|---|---|---|---|
| Atlas unpacked-card | `app/atlas/unpacked-card.tsx` | Full-bleed 9:16 "Wrapped" share card (year recap, portrait, gold palette) | **Keep** (+share) | native-capture fallback |
| Atlas postcards (shelf) | `app/atlas/postcards.tsx` | Postcard shelf: draft-hero (Keep it/Refine) + 2-up kept postcards | **Keep** | draft/kept/empty |
| Atlas memory receipt | `app/atlas/receipt.tsx` | "What Vesper knows" — memory receipt via `TrustControlsKit` | **Trust** +Explain | trust-state pills |
| Atlas data receipt | `app/atlas/data-receipt.tsx` | Personal-data audit log (location/voice/redactions) via `TrustReceiptRow` | **Trust** 🚩 (row-based) | audit-event kinds |

### Onboarding / system banners (added in coverage recheck)
| Banner | file:line | Shows | Family | State |
|---|---|---|---|---|
| DevelopingDiaryBanner | `components/onboarding/DevelopingDiaryBanner.tsx:2` | "Still developing your diary — N trips so far…" pulse | *(Surface / Process)* 🚩 | cycling / progressLabel |
| OfflineBanner | `components/ui/OfflineBanner.tsx` | Global offline notice (renders nothing when connected) | *(system chrome)* 🚩 | offline only |

**Deliberately excluded as sub-primitives, not cards** (own no independent card container): `CardChipRow`,
`CardActionPill`, `CardLift`, `CardStatusLabel`, `DecisionSeal`, `PlanDecisionInline`,
`MakePostcardButton`, and the `TrustControlsKit` / `BookingReceiptPrimitives` member rows.

---

### Family-mapping flags (the actionable exceptions)

**Legacy names in code (rename candidates):** the *entire* Vesper card-family system
(`vesperCardFamilies.ts:6`, `concierge/VesperCardKit.tsx`) — 7 deprecated content-intent names, keying
all glyphs/tints/KindTags/Deck routes.

**Spans 3+ families (mis-scoped / doing too much):**
- `FolioReceiptCard` — 4 families across its facet × state × evidence matrix. The clearest "one card
  became a framework" case.
- `StayCard` — 8 variants spanning Surface (suggested) + Decide (vote) + Transact (confirmed/held/split).
  A second "one card became a framework" case, parallel to FolioReceiptCard.
- `VesperReceipt` — 3 families across 4 modes (compact/detail/source/status).
- `ProposalReceipt` — 10 kinds spanning Decide (vote) + Trust (applied/reverted/booking_hold receipts).
- `DiscoverPinPeekCard` — Surface + Explain + Keep in one peek.
- `DeckPickFace` / `PreviewEditCard` — each legitimately span 2 (Decide+Explain, Decide+Trust); note
  but don't split.

**Fits no family (proposed taxonomy gaps — see §6):**
- **Process/Progress:** `ScanProgressCard`, `ResearchCard` (running), capture-nudge submitting. Long-
  running-operation feedback is a recurring shape with no mechanic.
- **Forecast/Estimate:** `CostsEstimateCard` — explicitly *not* a transaction and *not* ledger truth;
  it is a projection. Neither Transact nor Explain fits cleanly.
- **System chrome:** `ErrorBanner` — genuine error surface; arguably out of the content taxonomy
  entirely (belongs to a State System, not a card mechanic).

---

## 3. Shared shell vs fork — the consolidation answer

**Yes, there is a shared shell — and it is layered, with two competitors beside it.**

**Canonical stack.** `CardShell` → `CardSurface` → tokens in `constants/cardSurface.ts`.
- `CardShell` (`components/vesper-cards/CardShell.tsx:41`): tints warm/soft/urgent/calm, dashed variant,
  `ctx` (solo/group/deck) threading. Anatomy kit around it: `CardHead` (glyph + `KindTag` + mono meta,
  `CardHead.tsx:22`), `CardArt` (swappable illustration/photo slot), `ActionRow` (solo/group/deck-aware
  actions, `ActionRow.tsx:37`), `CardStates` (loading/preparing/inactive, `CardStates.tsx:17`).
- `CardSurface` (`components/ui/CardSurface.tsx:30`) is the real token owner: radius `card`=**14**
  (`cardSurface.ts:24`), 4 density presets, and the material table — `paper` = `cardWarm` bg + hairline
  border + `letterpress.shadow` (`cardSurface.ts:58`).

**Who actually builds on the shell** (import trace):
- **Vesper-cards kit** → all 7 home faces + `FocusHome` + `HeroProse` + `Rail`.
- **Chat cards** (VenueCard, ResearchCard, NotificationCard, BookingConfirmationCard, ChangeAppliedCard,
  PrivacyHandoffCard, PlanReadyCard, PreviewEditCard, DocumentEditCard, ReactionCard, VoiceSegmentCard)
  → wrap `ChatCardFrame`, **not** `CardShell`.
- **`CardSurface` directly** (~24 surfaces): trips index, invite, public place/venue, stories, atlas
  timeline, memory sheets, photo-intake, trip-creation, `TripMapPhotoCard`, `TripsHomeCards`, pretrip
  feed, `LetterpressCard`, discover reader.
- **`EditorialCard`** (`components/ui/EditorialCard.tsx:41`) → `NarrationCard`, `BookingProposalCard`,
  `TravelDNACard`. A *fourth* shell (agent/receipt tones).
- **`ui/Card`** (`components/ui/Card.tsx:28`, radius 12) → only booking checkout/session panels.
- **`TrustControlsKit`** (`components/trust/TrustControlsKit.tsx`) → a **fifth** shell: the Trust family
  (Atlas memory/data receipts) builds on its own `TrustReceipt`/`TrustRow`/`TrustZone` primitives, not
  `CardShell`. Plus the Atlas **`unpacked-card`** share format is full-bleed 9:16, outside the paper
  system entirely. So the Trust + Atlas-share surfaces are a third parallel card ecosystem.

### Fork / drift catalog

| Container | file:line | Radius | Padding | Shadow | Shell? |
|---|---|---|---|---|---|
| `CardSurface` (canon) | `constants/cardSurface.ts:24,58` | **14** | density preset | letterpress 5-layer | — (base) |
| `ChatCardFrame` | `chat/VesperChatCardKit.tsx:213,217` | **16** 🚩 | child-owned | glass 5-layer 🚩 | own |
| `ui/Card` | `ui/Card.tsx:28` | **12** 🚩 | 12 | (paper) | wraps Surface |
| `EditorialCard` | `ui/EditorialCard.tsx:41` | 14 | 16 | letterpress | wraps Surface |
| `StayCard` | `stay/StayCard.tsx:313,198` | 14 | 15/12–14 asym | **none** 🚩 | hand-rolled ❌ |
| `CostsEstimateCard` | `expense/CostsEstimateCard.tsx:37,36` | **13** 🚩 | 12 | **none** 🚩 | hand-rolled ❌ |
| `TripLogCard` | `memory/TripLogCard.tsx:105,102` | 12 | 12/16 | **none** 🚩 | hand-rolled ❌ |
| `FolioReceiptCard` | `trip/FolioReceiptCard.tsx:479,540,490` | **12 / 9 / 10** 🚩 | 6 / 4 | **none** 🚩 | hand-rolled ❌ |
| `TripMapPhotoCard` | `trip-map/TripMapPhotoCard.tsx:60` | via `paperRaised` | 12/8 | raised (custom) | Surface, off-material |

**Quantify.** ~13 distinct card container patterns. Shell-backed: `CardShell`(+kit), `EditorialCard`,
`ui/Card`, direct `CardSurface`. Forked: 4 hand-rolled (`StayCard`, `CostsEstimateCard`, `TripLogCard`,
`FolioReceiptCard`) + 1 competing shell (`ChatCardFrame`). Diverging dimensions, worst-first:
**radius (9→16, five values)** and **shadow (letterpress / glass / raised / none — four recipes)**;
padding ranges 4→20. There is even a double-definition trap: `layout.cardRadius`=12 vs
`cardSurfaceRadius.card`=14 (`cardSurface.ts:21`).

**Consolidation size: MEDIUM–LARGE.** Not VField-scale (there is a real shared base), but the chat
ecosystem is a full parallel primitive and 4 cards hand-roll shadow/radius/padding. High-confidence
moves: (a) reconcile `ChatCardFrame` 16→14 + one shadow recipe; (b) migrate the 4 hand-rolled cards
onto `CardSurface` with a `stayCompact` density; (c) retire the unused `paperFlat`/`glass`/`paperRaised`
materials or make them canon. Est. ~150 lines of duplicated shadow/radius/padding removed.

---

## 4. Generated-field census — governed vs ungoverned

**Two governance layers exist.** (1) **Length** — `content_contract.py:137` `CONTRACTS` (11 named
contracts) truncate-not-raise, mirrored in `constants/contentContract.ts:72`. (2) **Facts** —
`content_contract.py:357` `PROSE_SURFACES` (~30 surfaces) — but **every one is `facts_policy="log"` in
M1**: it scans + logs, it does not enforce (`content_contract.py:315`). So "facts-governed" today means
*observed*, not *clamped*.

**Length-governed card fields** (registered + clamped at the generator):

| Contract | Fields | Card(s) it lands in |
|---|---|---|
| `home_card` | eyebrow/title/body/cta_label | Vesper home faces; `NotificationCard` (clamped at dispatch) |
| `home_card_rail` | eyebrow/title/body/cta_label | Rail preview faces |
| `deck_judgment` | reasoning/tradeoff/why_not | `DeckPickFace` |
| `recommendation` | move/why_for_group/why_for_person/timing_note/bullet | chat recommendation block |
| `change_proposal` | title/description | `VoteWidgetCard` / `BlockProposedBanner` proposal text |
| `itinerary_block` | title/notes | plan blocks (title **unreconciled to venue**, notes governed) |
| `invite_snapshot` | snapshot_text/question_prompt/og_* | invite landing (card-adjacent) |
| `proposalReceipt` (FE-only) | waiting_on_label | `ProposalReceipt` "Waiting on {names}" footer |
| `home_anchor_voice`, `concierge_lead_note`, `trip_hero`, `atlas_dna` | — | home/hero prose, DNA essence label |

**Fact-rendered (no generated prose — low content risk despite high consequence):**
`BookingConfirmationCard`, `BookingProposalCard`, `BookingReceiptPrimitives`, `ChangeAppliedCard`
(before/after from data), `FolioReceiptCard` (facets from state), `TripMap*PeekCard`.

**Ungoverned generated text inside cards (highest content-risk):**

| Rank | Card | Ungoverned generated field(s) | Why it's risky |
|---|---|---|---|
| 1 | `StoryArchiveCard` / `TripStorySectionCard` / `TripLogCard` | hero_title, hero_subtitle, section body | Public share (OG meta + HTML); subtitle **mints counts** ("three days, four restaurants"); no length contract |
| 2 | `NarrationCard` | narration body | Spoken aloud (irreversible); entity names interpolated; no clamp, no confidence surface |
| 3 | `DiscoverPinPeekCard` | `venue_verdict` (curator take) | Editorial verdict on a real business; no body budget, no confidence styling |
| 4 | `ExemplarInlineCard` / dossier callout | thesis / detail line | Shareable; `coverage_depth` computed but never surfaced |
| 5 | `TravelDNACard` | reflection phrases | Ungoverned (essence label *is* governed via `atlas_dna`); dispute affordance is the only guard |
| 6 | `CostsEstimateCard` | `note` | Money-adjacent estimate prose, unbudgeted |
| 7 | `VenueCard` | detail / match line | Mixed generated; no clamp (chat scroll grows) |

Prior findings corroborated (verify-before-trust): `docs/content-contracts-audit.md` (R1 receipt-OCR,
R2 story public-share) and `docs/content-contracts-fixes-applied.md` (six prompt-hardening fixes) — but
those cover *all* prose surfaces; the card-scoped concentration above is the story/narration/verdict
cluster, not the booking receipts (which are fact-rendered).

---

## 5. State coverage

The dominant pattern is **⊘ render-raw**: most cards render their data directly with no loading/empty/
error branch, relying on the parent to gate. A shared kit exists but is under-used:

- **Shared `CardStates`** (`CardStates.tsx:17`) provides loading/preparing/inactive — used by the Vesper
  home faces only. No other surface adopts it.
- **Real state coverage** lives in interaction-heavy cards: `ResearchCard` (L/running/error),
  `PhotoSlotCard` (loading/permission/error), `ConciergeCaptureNudgeCard` (4 phases + error),
  `PreviewEditCard`/`ChangeAppliedCard`/`ReactionCard` (optimistic + rollback), `NarrationCard` (audio
  lazy-load / cache-miss), `ScanProgressCard` (progress + low-power).
- **No formal error boundaries** on cards; failures surface as parent state flags. Story, discover,
  trip-map, memory, and receipt cards render raw — an empty/failed generated field shows as blank.

The `stability-*-{loading,error,offline,normal}.png` fixture set at `travel-app/` shows a **screen-level**
State System is exercised, but it does not reach individual card fallbacks.

---

## 6. Summary tables

### Table A — Family coverage

| Family | Cards implementing it | Verdict |
|---|---|---|
| **Surface** | CardLive, CardSignal, CardResume, CardStarter, RailCard, VenueCard, NotificationCard, PlanReadyCard, LiveCompanionBanner, GeofenceBanner, TripMapStop/Neighborhood, TripsHomeCards, TripHeroCard, DiscoverPinPeek, StoryReadyEntry, StayCard(suggested) | **Crowded** — the default bucket |
| **Decide** | CardCall, DeckPick/Call/Compare/Structured, VoteWidgetCard, PreviewEditCard, ReactionCard, ConciergeCardDecisionSheet, BlockProposedBanner, DecisionPrimitives, ProposalReceipt(vote), StayCard(vote) | Well covered |
| **Transact** | BookingConfirmationCard, BookingProposalCard, BookingReceiptPrimitives, VesperReceipt(status), FolioReceiptCard(booking facet), StayCard(confirmed/held/split), CostsEstimateCard* | Covered (*estimate is a stretch) |
| **Explain** | CardPrepared, DeckBrief, ResearchCard, NarrationCard, ExemplarInlineCard, TravelDNACard, DocumentEditCard, TripMapNeighborhood | Well covered |
| **Keep** | CardCapture, ConciergeCaptureNudgeCard, TripMapPhotoCard, TripLogCard, StoryArchiveCard, TripStorySectionCard, PhotoSlotCard, VoiceSegmentCard, Atlas unpacked-card, Atlas postcards | **Crowded** |
| **Trust** | ChangeAppliedCard, PrivacyHandoffCard, DignifiedExceptionCard, BlockChangedBanner, ConcurrentEditBanner, ConsequenceBanner, VesperReceipt(provenance), ProposalReceipt(receipt), Atlas memory/data receipts | Well covered (**own shell: TrustControlsKit**) |
| *(gap)* **Process** | ScanProgressCard, ResearchCard(running), capture-nudge(submitting) | **Unrepresented** in taxonomy |
| *(gap)* **Forecast** | CostsEstimateCard | **Unrepresented** in taxonomy |

All six are represented; none empty. Surface and Keep are the crowded buckets; the only true holes are
Process and Forecast (both currently shoe-horned).

### Table B — Consolidation

| Question | Answer |
|---|---|
| Shared shell? | **Yes, layered:** `CardShell`→`CardSurface`(+kit: CardHead/CardArt/ActionRow/CardStates) |
| Competing shells | `ChatCardFrame` (r16, glass), `ui/Card` (r12), `EditorialCard` (agent/receipt), **`TrustControlsKit`** (Trust family), Atlas `unpacked-card` (full-bleed 9:16) — **3 parallel ecosystems** |
| Forked containers | `StayCard`, `CostsEstimateCard`, `TripLogCard`, `FolioReceiptCard` (hand-roll shadow/radius/padding) |
| Worst-diverging dims | radius (9→16, 5 values) · shadow (4 recipes) · padding (4→20) |
| Consolidation size | **Medium–Large** — real base exists, but chat is a parallel primitive + 4 hand-rolls |

### Table C — Content-contract binding (highest content-risk first)

| Rank | Card | # ungoverned generated fields | Public/irreversible? |
|---|---|---|---|
| 1 | Story cards (Archive / Section / Log) | 3 (title, subtitle, section body) | **Public share** |
| 2 | NarrationCard | 1 (body) | **Spoken, irreversible** |
| 3 | DiscoverPinPeekCard | 1 (verdict) | Real-business editorial |
| 4 | ExemplarInline / dossier callout | 2 (thesis, detail) | Shareable |
| 5 | TravelDNACard | ~1 (phrases; essence governed) | Profile |
| 6 | CostsEstimateCard | 1 (note) | Money-adjacent |
| 7 | VenueCard | 1–2 (detail/match) | In-chat |
| — | Booking/receipt cards | **0** (fact-rendered) | High consequence, low *content* risk |

---

*Method: three parallel read-only sweeps of `travel-app` + `travel-agent`, cross-checked against
first-hand reads of `CardShell`/`CardSurface`/`cardSurface.ts`/`cardContract.ts`/`content_contract.py`/
`contentContract.ts` and the shell import graph. No code modified.*
