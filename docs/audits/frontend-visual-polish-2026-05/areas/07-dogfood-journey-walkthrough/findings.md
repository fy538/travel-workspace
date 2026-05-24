# 07 - Dogfood Journey Walkthrough Findings

## Summary

Runtime walkthrough/screenshots were unavailable in this pass. I checked runtime feasibility with `npm ls react-native-web --depth=0`; `react-native-web` is not installed, so I did not attempt an Expo web screenshot run or edit app dependencies. This is a static journey-risk audit from code and docs.

The biggest dogfood issue is not isolated visual polish: the journey can stop at the moment a user creates a fresh planning trip and tries to talk to Vesper. The app also loses coherence when moving between Plan home, private Vesper, group chat, proposal review, and map; each surface has improved locally, but the journey still reads as several adjacent products.

Weakest visual-polish step: proposal/recommendation review. It is high-stakes product content, but parts still render like operational review UI rather than Vesper making an opinionated, trustworthy move.

## Journey Reviewed

Static path traced:

1. Open app in mock/default mode and land in Trips.
2. Review live/planning/completed trip list.
3. Create a new trip from Trips, and alternately open the seeded Tokyo planning trip.
4. Inspect invite/member/group state via Trip Info and trip-home group cards.
5. Ask Vesper privately from the Concierge/private chat route.
6. Review recommendation/proposal surfaces from chat and Plan.
7. Inspect Plan landing, deep timeline, and Map.
8. Use group chat.
9. Inspect loading/error/empty states in Trips, chat, invite, proposal, Plan, and Map.
10. Check Me/profile context after the trip flow.

## Findings

### P0 - Fresh trip creation can land in a private chat where sending is a silent no-op

Creating a new trip from the Trips screen sets an optimistic current trip, then routes to generic Concierge chat without passing the new trip id. For an ideation trip with no destination, Concierge chat passes `undefined` as the `tripId` into `useConciergeChat`. The hook's send path immediately returns when `tripId` is missing, before mock or real streaming can add the user's message.

This blocks the dogfood journey if the user chooses "create a planning trip" rather than opening a seeded trip. The user sees a private Vesper surface, but the first prefilled message and later composer sends do not actually send.

Evidence:

- `Travel App/app/(tabs)/trips/index.tsx:81` creates the trip, but `Travel App/app/(tabs)/trips/index.tsx:86` ignores the returned id and `Travel App/app/(tabs)/trips/index.tsx:87` routes to `routes.conciergeChat(...)`.
- `Travel App/app/(tabs)/trips/index.tsx:184` to `Travel App/app/(tabs)/trips/index.tsx:187` uses that path for the zero-trip welcome CTA.
- `Travel App/app/(tabs)/concierge/chat.tsx:142` to `Travel App/app/(tabs)/concierge/chat.tsx:145` passes `undefined` when the current trip is ideation and has no destination.
- `Travel App/hooks/useConciergeChat.ts:343` returns immediately when `tripId` is missing.

### P1 - Default mock group copy undermines the privacy contract

The docs' core doctrine is "invisible privacy, visible care," but the default mock journey includes group-visible copy that names constraint categories and group preference counts. Because mock mode is the default dogfood mode, this is not just fixture debt; it is the version internal users are most likely to experience first.

This is where a user loses confidence fastest: the app claims private signals stay private, then the group-visible plan says why the plan changed in constraint language.

Evidence:

- `Travel App/constants/mocks/chat.ts:30` says breakfast "fits all dietary needs" in a group itinerary attachment.
- `Travel App/constants/mocks/chat.ts:32` says "3 people wanted downtime."
- `Travel App/hooks/useConciergeChat.ts:140` to `Travel App/hooks/useConciergeChat.ts:147` includes mock private recommendation text that says "dietary restrictions are handled well" and `why_for_group: "Fits all dietary needs, mid-range price..."`.
- `Travel App/constants/mocks/itinerary.ts:171` to `Travel App/constants/mocks/itinerary.ts:173` and `Travel App/constants/mocks/itinerary.ts:234` to `Travel App/constants/mocks/itinerary.ts:235` expose aggregate downtime rationale in plan copy.

### P1 - The trip workspace still depends on competing navigation models

The journey asks the user to understand TripHeader pills, the Plan landing, the deep `/plan` timeline, private Vesper, group chat, map, Trip Info, and proposal sheets. Code comments acknowledge the current dependency: Chat/Map/Photos/Memory are reachable only through TripHeader pills, while the "Across the trip" grid was reduced to Stay and Costs.

This is the main place the experience stops feeling like one coherent product. The user is not always sure whether "Plan" means the landing page, timeline, map-backed plan state, or proposal review.

Evidence:

- `Travel App/app/(tabs)/trips/[tripId]/index.tsx:14` to `Travel App/app/(tabs)/trips/[tripId]/index.tsx:26` documents that removing header pills would orphan Chat, Map, Photos, and Memory.
- `Travel App/app/(tabs)/trips/[tripId]/index.tsx:315` to `Travel App/app/(tabs)/trips/[tripId]/index.tsx:319` keeps only Stay and Costs in "Across the trip" because other destinations rely on the header rail.
- `Travel App/components/trip/TripHeader.tsx:47` to `Travel App/components/trip/TripHeader.tsx:50` changes available pills by trip phase.
- `Travel App/app/(tabs)/trips/[tripId]/_layout.tsx:77` to `Travel App/app/(tabs)/trips/[tripId]/_layout.tsx:81` disables stack animation for pill switches, making surface changes feel abrupt.

### P2 - Proposal/recommendation review feels more like audit UI than concierge judgment

Proposal and recommendation surfaces carry the product's most important promise: Vesper makes an opinionated move and shows enough context to trust it. The current implementation includes useful detail, but visually it leans on badges, rows, labels, icons, a spinner, and an unbounded "alternatives considered" list. That weakens the "recommendation, not options" doctrine at the exact moment users decide whether to trust Vesper.

Evidence:

- `Travel App/components/trip/ProposalReviewSheet.tsx:302` to `Travel App/components/trip/ProposalReviewSheet.tsx:305` uses an `ActivityIndicator` for proposal loading, despite brand guidance preferring anticipation states over spinners.
- `Travel App/components/trip/ProposalReviewSheet.tsx:323` to `Travel App/components/trip/ProposalReviewSheet.tsx:327` uses badge-heavy metadata at the top of the sheet.
- `Travel App/components/trip/ProposalReviewSheet.tsx:367` to `Travel App/components/trip/ProposalReviewSheet.tsx:389` renders every alternative option without a visible cap.
- `Travel App/components/chat/RecommendationBlock.tsx:44` to `Travel App/components/chat/RecommendationBlock.tsx:65` renders recommendation reasoning as labeled icon rows.
- `Travel App/components/chat/RecommendationBlock.tsx:100` to `Travel App/components/chat/RecommendationBlock.tsx:107` frames the recommendation block as a small boxed fact sheet.

### P2 - Plan/map inspection drops context and weakens the sacred-purple signal

The map is functional, but the transition from Plan to Map feels utilitarian compared with the rest of the trip workspace. Day chips only say "Day N," and the strongest route color is purple even though purple is reserved for Vesper/AI presence. In a full journey, this makes the map feel like a separate native utility rather than the spatial expression of Vesper's plan.

Evidence:

- `Travel App/components/trip-map/TripMapScreen.tsx:249` to `Travel App/components/trip-map/TripMapScreen.tsx:309` splits the map and bottom sheet, but the day selector remains generic.
- `Travel App/components/trip-map/TripMapScreen.tsx:267` to `Travel App/components/trip-map/TripMapScreen.tsx:294` renders day chips as only `Day {d.day_number}`.
- `Travel App/components/trip-map/TripMapCanvas.tsx:148` uses `colors.purple[400]` for non-soft route polylines, outside a clear agent-presence context.

### P2 - Me/profile is improved, but still feels like a library/settings destination after a trip journey

Me contains good trust primitives, especially Travel DNA, but after completing the dogfood journey it still reads as identity plus library plus settings. The user's likely question is "what did Vesper learn from this trip and how does that affect the next one?" The answer is present but diluted among trips, people, social activity, saved venues, voice logs, and settings links.

Evidence:

- `Travel App/app/(tabs)/me/index.tsx:163` to `Travel App/app/(tabs)/me/index.tsx:183` surfaces Travel DNA and a personal insight.
- `Travel App/app/(tabs)/me/index.tsx:195` to `Travel App/app/(tabs)/me/index.tsx:200` introduces a broad "Library" grouping.
- `Travel App/app/(tabs)/me/index.tsx:202` to `Travel App/app/(tabs)/me/index.tsx:493` stacks memory, trips, people, social activity, saved venues, voice logs, and settings/trust controls.
- `Travel App/components/me/TravelDNACard.tsx:75` to `Travel App/components/me/TravelDNACard.tsx:113` is the most product-specific part of Me, but it is only one module in the larger accumulation surface.

## Evidence

Runtime evidence: no screenshots or simulator captures were produced in this pass. `npm ls react-native-web --depth=0` returned an empty tree, so web rendering was not available without changing dependencies.

Static evidence was gathered from:

- Trips list and new-trip creation: `Travel App/app/(tabs)/trips/index.tsx`
- Trip workspace/Plan landing: `Travel App/app/(tabs)/trips/[tripId]/index.tsx`
- Trip workspace header: `Travel App/components/trip/TripHeader.tsx`
- Private Vesper chat: `Travel App/app/(tabs)/concierge/chat.tsx`, `Travel App/hooks/useConciergeChat.ts`, `Travel App/components/chat/PrivateVesperNote.tsx`
- Group chat: `Travel App/app/(tabs)/trips/[tripId]/chat.tsx`, `Travel App/components/chat/group/*`, `Travel App/constants/mocks/chat.ts`
- Proposal/recommendation review: `Travel App/components/trip/ProposalReviewSheet.tsx`, `Travel App/components/chat/RecommendationBlock.tsx`
- Plan/map: `Travel App/app/(tabs)/trips/[tripId]/plan.tsx`, `Travel App/components/trip-map/*`
- Profile context: `Travel App/app/(tabs)/me/index.tsx`, `Travel App/components/me/TravelDNACard.tsx`

## Suggested Fix Direction

Top 5 fastest changes to make the app feel dogfoodable:

1. Fix the fresh-trip chat handoff: after `createTrip`, route with a real trip id or make ideation/private chat explicitly support no-trip conversations. Add a visible error if send is unavailable.
2. Rewrite default mock group/plan copy to obey privacy doctrine. No "dietary needs," "restrictions," "budget won't be awkward," or private aggregate rationale in group-visible copy.
3. Collapse the trip workspace mental model: make the Plan landing carry obvious entries to Chat, Map, Photos, Memory, Group, and Invite so the header rail is not the only connective tissue.
4. Redesign proposal/recommendation review as a concierge judgment surface: verdict first, one clear proposed move, capped alternatives only when truly useful, no spinner, fewer badges.
5. Make Map feel like Vesper's spatial plan: non-purple route styling, richer day labels, and a stronger link back to the plan/proposal that produced each stop.

## Verification Ideas

- Add an offline smoke test for: Trips `+` → create ideation trip → private chat opens → prefilled message appears as a user bubble → Vesper response streams.
- Add fixture lint or snapshot checks for group-visible mock copy that flags phrases like `dietary`, `budget`, `ankle`, `constraint`, `preferences`, and `people wanted`.
- Run the journey on a device/simulator with mock mode and record screenshots at each step once native visual QA is available.
- Add a Maestro dogfood script covering: Trips list → Tokyo planning trip → Trip Info invite state → private Vesper → proposal sheet → map → group chat → Me.
- For proposal review, capture before/after screenshots with loading, error, open proposal, accepted/applied, and apply-failed states.
