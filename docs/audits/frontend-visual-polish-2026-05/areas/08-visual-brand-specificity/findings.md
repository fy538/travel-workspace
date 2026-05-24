# Visual Brand Specificity Findings

## Summary

No rendered screenshots were available in the audit folders, and I did not find pre-captured simulator/device output for this area. This is therefore a static brand-risk audit from code and doctrine.

The app is no longer merely a competent warm travel UI: the strongest surfaces do feel specifically like Vesper. Trip cards, private concierge chat, group Vesper prose, and the trip-home attention stack now carry the leather-journal/editorial/agent-presence doctrine. The main risk is uneven propagation. Several high-traffic secondary surfaces still rely on plain white utility cards, generic gradient placeholders, Ionicons, and older chat attachment cards, so the product can drift back toward "nice React Native travel app" when Vesper is not directly speaking.

## Brand Surfaces Reviewed

- Brand doctrine and tokens: `Travel App/docs/Design Language.md`, `Travel App/docs/Brand Identity.md`, `Travel App/constants/colors.ts`, `Travel App/constants/typography.ts`
- Brand primitives: `Travel App/components/brand/*`
- Strong brand carriers: `Travel App/components/trip/TripCard.tsx`, `Travel App/components/chat/PrivateVesperNote.tsx`, `Travel App/components/chat/group/VesperNote.tsx`, `Travel App/components/plan/*`, `Travel App/components/trip-home/*`
- Dilution-risk surfaces: `Travel App/components/chat/*Card.tsx`, `Travel App/app/(tabs)/discover/index.tsx`, `Travel App/app/(tabs)/me/index.tsx`, `Travel App/app/(tabs)/trips/[tripId]/plan.tsx`

## Findings

### P1 - Discover is the least Vesper-specific high-traffic tab

Discover carries place content, but its first-order visual system is search + six peer pills + masonry cards. That reads like a generic browse marketplace before it reads like a knowledgeable local friend with taste. The code even names the problem in a TODO: six peer pills make Discover "read as a browse console before Vesper expresses an opinion" at `Travel App/app/(tabs)/discover/index.tsx:722`.

Concrete dilution points:
- The fixed header uses generic search copy, "Search places, restaurants, cities..." at `Travel App/app/(tabs)/discover/index.tsx:705`.
- The tab rail remains six peer modes via `NavPills` at `Travel App/app/(tabs)/discover/index.tsx:733`.
- Trending and Guides use gradient color blocks instead of photography or the brand's honest illustration system at `Travel App/app/(tabs)/discover/index.tsx:1443` and `Travel App/app/(tabs)/discover/index.tsx:1527`.
- Their shared masonry card styling is a plain white hairline card at `Travel App/app/(tabs)/discover/index.tsx:1851`.

Against doctrine: Vesper should be specific, editorial, and place-aware (`Travel App/docs/Brand Identity.md:31`, `Travel App/docs/Brand Identity.md:214`), not a neutral browse console.

### P1 - Rich chat attachment cards lag behind the new Vesper chat substrate

Private and group prose are now strong: private AI turns route to `PrivateVesperNote` at `Travel App/app/(tabs)/concierge/chat.tsx:77`, and group AI turns route through `GroupThreadItem`/`VesperNote` at `Travel App/components/chat/group/GroupThreadItem.tsx:167`. But many rich objects underneath still render as old utility cards, so Vesper's best recommendations can visually collapse into generic chat attachments.

Examples:
- `VenueCard` is a plain white bordered card with no photo, letterpress treatment, fleuron, or editorial place framing at `Travel App/components/chat/VenueCard.tsx:46` and `Travel App/components/chat/VenueCard.tsx:87`.
- `RecommendationBlock` renders structured reasoning as an icon-led fact box with a left border at `Travel App/components/chat/RecommendationBlock.tsx:43` and `Travel App/components/chat/RecommendationBlock.tsx:99`.
- `MapCard` uses a plain white card and purple route line/fallback map icon at `Travel App/components/chat/MapCard.tsx:93`, `Travel App/components/chat/MapCard.tsx:122`, and `Travel App/components/chat/MapCard.tsx:146`.

Against doctrine: recommendation reasoning should read as Vesper's structured thought directly on the page, not as a separate rigid card (`Travel App/docs/Design Language.md:217`, `Travel App/docs/Design Language.md:228`).

### P2 - The locked fleuron is implemented inconsistently in group chat

The brand brief locks the 8-point Venus star as a custom SVG, "never Unicode emoji" (`Travel App/docs/Brand Identity.md:134`). The shared `Fleuron` component implements that SVG at `Travel App/components/brand/Fleuron.tsx:26`. Private chat uses it correctly at `Travel App/components/chat/PrivateVesperNote.tsx:68`.

Group chat, however, renders a Unicode fleuron-like character in `AttributionLine` at `Travel App/components/chat/group/VesperNote.tsx:66` and `Travel App/components/chat/group/VesperNote.tsx:71`. This is small, but it weakens one of the few truly proprietary visual marks in the product.

### P2 - Purple is mostly meaningful, but it leaks into non-agent or ambiguous decoration

The color doctrine is clear: seeing purple should mean the AI/concierge is doing or saying something (`Travel App/docs/Design Language.md:84`; `Travel App/constants/colors.ts:85`). The strongest uses obey this: `PrivateVesperNote` attribution uses `colors.agent.attribution` at `Travel App/components/chat/PrivateVesperNote.tsx:69`, and `PendingPromptCard` uses sacred agent wash at `Travel App/components/plan/PendingPromptCard.tsx:65`.

Leakage / ambiguity:
- `ContentGraphBanner` falls back to `colors.purple[600]` when a place lens is missing, even though the banner is an editorial/place offer, not necessarily Vesper speaking (`Travel App/components/chat/ContentGraphBanner.tsx:36`).
- Me profile avatar uses `colors.purple[200]` for the user's identity surface at `Travel App/app/(tabs)/me/index.tsx:138`.
- Trip highlight placeholders include `colors.purple[200]` in a generic color rotation at `Travel App/app/(tabs)/me/index.tsx:35`.

These are not catastrophic, but they make purple feel like brand decoration rather than agent presence.

### P2 - Place-aware visual fallback exists, but the vocabulary is too small

`TripCard` is the most unmistakably Vesper surface. It combines `LetterpressCard`, `HonestIllustration`, typographic status, Fraunces display type, and Vesper attribution at `Travel App/components/trip/TripCard.tsx:50`, `Travel App/components/trip/TripCard.tsx:103`, `Travel App/components/trip/TripCard.tsx:132`, and `Travel App/components/trip/TripCard.tsx:163`.

The place-aware illustration mapper, though, only knows Lisbon and Brooklyn/New York before falling back to `generic-warm` (`Travel App/utils/illustrationVariant.ts:15`). `HonestIllustration` itself ships only `lisbon-dusk`, `brooklyn-brick`, and `generic-warm` (`Travel App/components/brand/HonestIllustration.tsx:27`). Unknown destinations therefore lose the "specific over generic" visual promise.

### P2 - Me tab has identity copy, but its visual language is still profile-dashboard-adjacent

The Me tab wisely removes gamified completion language in comments at `Travel App/app/(tabs)/me/index.tsx:128`, and the Travel DNA card likely carries real Vesper identity. But surrounding modules still use profile-avatar, library rows, pastel placeholders, and plain cards.

Examples:
- The identity header is centered avatar/name/interests, a common profile pattern, at `Travel App/app/(tabs)/me/index.tsx:137`.
- Trip highlights use generic color rectangles with an image icon instead of a memory/journal/illustration primitive at `Travel App/app/(tabs)/me/index.tsx:238`.
- Saved venue chips and bottom links use plain white hairline cards at `Travel App/app/(tabs)/me/index.tsx:579` and `Travel App/app/(tabs)/me/index.tsx:590`.

This screen could belong to many travel/planning apps unless the Travel DNA card is in view.

### P3 - The generic `Card` utility is correctly documented, but still appears in brand-bearing contexts

The `Card` primitive explicitly says it is for utility chrome and not for editorial/Vesper/memory/identity content at `Travel App/components/ui/Card.tsx:1`. Yet it still appears in contexts that can carry brand perception:
- Legacy plan timeline wraps each day in `Card` at `Travel App/app/(tabs)/trips/[tripId]/plan.tsx:294`.
- Trip list still imports `Card` at `Travel App/app/(tabs)/trips/index.tsx:18` for invite/utility surfaces.
- Me imports and uses `Card` in the main identity tab at `Travel App/app/(tabs)/me/index.tsx:27`, `Travel App/app/(tabs)/me/index.tsx:301`, and `Travel App/app/(tabs)/me/index.tsx:410`.

This is not automatically wrong for utility panels, but it needs active policing because the brand's stronger card primitive exists at `Travel App/components/brand/LetterpressCard.tsx:1`.

## Evidence

- Vesper doctrine: leather travel journal, parchment, semantic earth tones, sacred purple, and article-scale typography are defined at `Travel App/docs/Design Language.md:55`.
- Purple doctrine: "Seeing purple = the AI is doing something" is stated at `Travel App/docs/Design Language.md:84` and encoded at `Travel App/constants/colors.ts:85`.
- Brand signature: custom 8-point fleuron and letterpress treatment are locked at `Travel App/docs/Brand Identity.md:130`.
- Typography signature: Fraunces article scale is explicitly unusual and should be protected at `Travel App/docs/Brand Identity.md:122`.
- Strongest Vesper screens:
  - Trips list / trip cards: `Travel App/components/trip/TripCard.tsx:1`, `Travel App/components/trip/TripCard.tsx:103`, `Travel App/components/trip/TripCard.tsx:132`.
  - Private chat: `Travel App/components/chat/PrivateVesperNote.tsx:1`, `Travel App/app/(tabs)/concierge/chat.tsx:74`.
  - Trip home: `Travel App/components/trip-home/AnchorCard.tsx:10`, `Travel App/components/trip-home/CardShell.tsx:49`, `Travel App/components/plan/PendingPromptCard.tsx:65`.
  - Plan landing rows: `Travel App/components/plan/DayRow.tsx:11`, `Travel App/components/plan/SurfaceCard.tsx:41`.
- Weakest / most generic screens:
  - Discover: `Travel App/app/(tabs)/discover/index.tsx:700`, `Travel App/app/(tabs)/discover/index.tsx:1440`, `Travel App/app/(tabs)/discover/index.tsx:1517`.
  - Me: `Travel App/app/(tabs)/me/index.tsx:137`, `Travel App/app/(tabs)/me/index.tsx:238`, `Travel App/app/(tabs)/me/index.tsx:579`.
  - Chat attachments: `Travel App/components/chat/VenueCard.tsx:87`, `Travel App/components/chat/RecommendationBlock.tsx:99`, `Travel App/components/chat/MapCard.tsx:171`.

## Suggested Fix Direction

1. Treat Discover as the next brand-anchor surface. Reduce the peer-tab browse-console feel and make the opening surface an opinionated, place-aware editorial index. Use real photography where available, and `HonestIllustration` variants where not.
2. Create reusable brand primitives that are currently missing:
   - `EditorialPlaceCard`: photo/illustration + Fraunces place title + curator hook + optional angle lens.
   - `AgentObjectCard`: letterpress/sacred variants for venue, booking, map, and vote objects emitted by Vesper.
   - `VesperAttributionLine`: one shared implementation using the SVG `Fleuron`, replacing the Unicode group-chat mark.
   - `PlaceVisual`: single API for real photo, destination-aware honest illustration, and warm fallback.
   - `ProfileMemoryCard`: for Me/Memory identity surfaces so they do not regress into generic profile modules.
3. Keep purple sacred by moving non-agent fallbacks to lens colors, earth tones, or espresso. Use `colors.agent.*` only when Vesper is actively speaking, asking, narrating, or composing.
4. Expand the honest illustration vocabulary beyond Lisbon/Brooklyn before broad dogfooding. The current mapper proves the pattern, but not enough destinations can feel place-aware yet.
5. Migrate older rich chat cards toward letterpress/editorial treatments so Vesper recommendations do not become ordinary chat attachments after the prose lands.

## Verification Ideas

- Capture first-viewport screenshots for Trips, private chat, group chat, trip home, deep plan, Discover, and Me on a small iPhone and one large iPhone.
- Run a "logo-off" test: hide tab labels/headers and ask whether each screenshot still reads as Vesper. Expected pass: TripCard, private chat, trip home. Expected fail/risk: Discover, Me, older chat cards.
- Run a purple audit screenshot pass: every purple pixel should answer "what is Vesper doing here?"
- Build a destination-matrix test for `TripCard`: Lisbon, Brooklyn/New York, Tokyo, Paris, Mexico City, unknown destination. Verify unknowns do not all collapse into the same generic warm postcard.
- Add a static check or review checklist for Unicode fleuron use and `colors.purple` outside `colors.agent`/known AI surfaces.
