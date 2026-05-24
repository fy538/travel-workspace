# Summary

Runtime profiling was unavailable in this session. `npm ls react-native-web --depth=0` reported no web target dependency, and `xcrun simctl list devices booted` showed no booted simulator, so this is a static perceived-performance audit from code.

The chat surfaces have already absorbed several good jank fixes: SSE deltas are batched, row renderers are memoized, and chat `FlatList` windows are bounded. The higher dogfood risk is now content-heavy non-chat surfaces that still mount full render trees in `ScrollView`, plus image/attachment paths that can block perceived send/open feedback.

# Performance Surfaces Reviewed

- Discover: `Travel App/app/(tabs)/discover/index.tsx`
- Private concierge chat: `Travel App/app/(tabs)/concierge/chat.tsx`
- Group trip chat and chat hooks: `Travel App/app/(tabs)/trips/[tripId]/chat.tsx`, `Travel App/hooks/useConciergeChat.ts`, `Travel App/hooks/useGroupChat.ts`
- Trip home: `Travel App/app/(tabs)/trips/[tripId]/index.tsx`
- Trip photos: `Travel App/app/(tabs)/trips/[tripId]/photos.tsx`, `Travel App/data/photos.ts`
- Me: `Travel App/app/(tabs)/me/index.tsx`
- Sheets/lists: `Travel App/components/discover/ExperienceDetailSheet.tsx`, `Travel App/components/trip/ProposalReviewSheet.tsx`, `Travel App/components/trip/FindPhotosSheet.tsx`, `Travel App/components/expense/AddExpenseSheet.tsx`, `Travel App/components/trip-map/TripMapStopList.tsx`, `Travel App/components/ui/ListRow.tsx`

# Findings

## P1 - Trip Photos Can Jank On Real Albums

The trip photo screen renders every group and every tile inside one vertical `ScrollView`, then uses a manual flex grid for each group. That avoids the nested-`FlatList` warning, but it also means a dogfood trip with hundreds of photos mounts hundreds of `Animated.View` wrappers and `AppImage` tiles at once.

Evidence: `Travel App/app/(tabs)/trips/[tripId]/photos.tsx:257`, `Travel App/app/(tabs)/trips/[tripId]/photos.tsx:281`, `Travel App/app/(tabs)/trips/[tripId]/photos.tsx:438`, `Travel App/app/(tabs)/trips/[tripId]/photos.tsx:439`, `Travel App/app/(tabs)/trips/[tripId]/photos.tsx:464`, `Travel App/app/(tabs)/trips/[tripId]/photos.tsx:488`. The grouping work also recomputes on each render rather than memoizing by query result: `Travel App/data/photos.ts:25`, `Travel App/data/photos.ts:26`, `Travel App/data/photos.ts:162`.

## P1 - Discover Still Has Several Unvirtualized Growth Paths

Discover only virtualizes Friends/For You. Angles, Events, Trending, Guides, quick picks, and search results render through `ScrollView` plus `.map()`. That is probably fine with seed data, but it is exactly the sort of surface that will feel fine until the backend returns a richer city index, more events, or more editorial modules.

Evidence: Angles use `ScrollView` and map all angle cards at `Travel App/app/(tabs)/discover/index.tsx:774`, `Travel App/app/(tabs)/discover/index.tsx:977`, `Travel App/app/(tabs)/discover/index.tsx:1001`; search/quick picks map inside `ScrollView` at `Travel App/app/(tabs)/discover/index.tsx:1151`, `Travel App/app/(tabs)/discover/index.tsx:1164`, `Travel App/app/(tabs)/discover/index.tsx:1203`; Events map `filteredExperiences` at `Travel App/app/(tabs)/discover/index.tsx:1394`; Trending/Guides build two full masonry columns with `.filter(...).map(...)` at `Travel App/app/(tabs)/discover/index.tsx:1440`, `Travel App/app/(tabs)/discover/index.tsx:1442`, `Travel App/app/(tabs)/discover/index.tsx:1517`, `Travel App/app/(tabs)/discover/index.tsx:1519`.

## P2 - Discover Lazy Fetch Flags Are Misaligned With Visible Tabs

The pill order is `Events` at index 3 and `Trending` at index 4, but the lazy-fetch flags treat index 3 as `trending` and index 4 as `quickPicks`. In real mode, this can make the visible Events tab wait on the wrong query and make Trending render before its query is enabled. It is a perceived-performance issue because the tab can look blank/empty while a different feed warms.

Evidence: pill order at `Travel App/app/(tabs)/discover/index.tsx:56`; active flag mapping at `Travel App/app/(tabs)/discover/index.tsx:391`, `Travel App/app/(tabs)/discover/index.tsx:395`, `Travel App/app/(tabs)/discover/index.tsx:397`; rendered tab branches at `Travel App/app/(tabs)/discover/index.tsx:1263` and `Travel App/app/(tabs)/discover/index.tsx:1414`; query `enabled` gates at `Travel App/data/discover.ts:458`, `Travel App/data/discover.ts:465`, `Travel App/data/discover.ts:495`, `Travel App/data/discover.ts:513`.

## P2 - Chat Streaming Is Mostly Controlled, But Still Unmeasured

Streaming no longer appears to call `setState` on every raw SSE chunk: both private and group hooks batch deltas in 100 ms windows, cap messages at 150, and the screens bound `FlatList` rendering. Residual risk remains that every flush still maps the message array and reparses markdown for the streaming row; this is acceptable for now but should be measured before dogfooding long agent turns with attachments.

Evidence: private batching at `Travel App/hooks/useConciergeChat.ts:197`, `Travel App/hooks/useConciergeChat.ts:544`, `Travel App/hooks/useConciergeChat.ts:554`; private cap at `Travel App/hooks/useConciergeChat.ts:64`, `Travel App/hooks/useConciergeChat.ts:262`; private list controls at `Travel App/app/(tabs)/concierge/chat.tsx:677`, `Travel App/app/(tabs)/concierge/chat.tsx:850`, `Travel App/app/(tabs)/concierge/chat.tsx:921`, `Travel App/app/(tabs)/concierge/chat.tsx:924`. Group equivalents are at `Travel App/hooks/useGroupChat.ts:101`, `Travel App/hooks/useGroupChat.ts:376`, `Travel App/hooks/useGroupChat.ts:386`, `Travel App/hooks/useGroupChat.ts:145`, `Travel App/app/(tabs)/trips/[tripId]/chat.tsx:236`, `Travel App/app/(tabs)/trips/[tripId]/chat.tsx:296`, `Travel App/app/(tabs)/trips/[tripId]/chat.tsx:387`, `Travel App/app/(tabs)/trips/[tripId]/chat.tsx:391`.

## P2 - Image Send Can Feel Frozen Before The Bubble Appears

The chat composer allows up to four images, keeps only URIs during compose, then base64-encodes every pending image in `onSend` before calling `onSendWithImages`. That saves heap during compose, but the user gets no obvious "preparing image" state while large files are read and encoded, and the optimistic chat bubble is delayed until conversion finishes.

Evidence: max image count at `Travel App/components/chat/ComposerBar.tsx:48`; lazy conversion rationale at `Travel App/components/chat/ComposerBar.tsx:183`; send-time conversion at `Travel App/components/chat/ComposerBar.tsx:211`, `Travel App/components/chat/ComposerBar.tsx:227`, `Travel App/components/chat/ComposerBar.tsx:231`, `Travel App/components/chat/ComposerBar.tsx:233`, `Travel App/components/chat/ComposerBar.tsx:237`.

## P2 - Several Sheets Are Heavy Enough To Feel Sluggish On Large Trips

`ExperienceDetailSheet` opens a full-screen sheet, fetches detail on mount, renders a hero image, and maps every itinerary day into animated day rows. `ProposalReviewSheet` renders a large modal tree with multiple mapped animated sections. `AddExpenseSheet` maps travelers repeatedly for member pickers and share rows. These are not broken, but they are prime candidates for perceived open-lag once trips have many days, proposals, or travelers.

Evidence: `ExperienceDetailSheet` detail fetch and body at `Travel App/components/discover/ExperienceDetailSheet.tsx:162`, `Travel App/components/discover/ExperienceDetailSheet.tsx:217`, `Travel App/components/discover/ExperienceDetailSheet.tsx:262`, day row mapping at `Travel App/components/discover/ExperienceDetailSheet.tsx:432`. `ProposalReviewSheet` modal body and mapped sections at `Travel App/components/trip/ProposalReviewSheet.tsx:286`, `Travel App/components/trip/ProposalReviewSheet.tsx:317`, `Travel App/components/trip/ProposalReviewSheet.tsx:370`, `Travel App/components/trip/ProposalReviewSheet.tsx:396`, `Travel App/components/trip/ProposalReviewSheet.tsx:667`. `AddExpenseSheet` repeated traveler rendering at `Travel App/components/expense/AddExpenseSheet.tsx:460`, `Travel App/components/expense/AddExpenseSheet.tsx:466`, `Travel App/components/expense/AddExpenseSheet.tsx:589`, `Travel App/components/expense/AddExpenseSheet.tsx:622`.

# Evidence

Positive controls already in place:

- `AppImage` gives every image a non-white placeholder and 180 ms fade, reducing blank-pop perception: `Travel App/components/ui/AppImage.tsx:56`, `Travel App/components/ui/AppImage.tsx:72`, `Travel App/components/ui/AppImage.tsx:78`.
- The photo picker sheet uses a virtualized 3-column `FlatList` with bounded windows, which is the right pattern for camera-roll scale: `Travel App/components/trip/FindPhotosSheet.tsx:278`, `Travel App/components/trip/FindPhotosSheet.tsx:292`, `Travel App/components/trip/FindPhotosSheet.tsx:295`.
- The map stop list is virtualized and bounded: `Travel App/components/trip-map/TripMapStopList.tsx:112`, `Travel App/components/trip-map/TripMapStopList.tsx:129`, `Travel App/components/trip-map/TripMapStopList.tsx:132`.
- Private chat now uses `PrivateVesperNote` instead of AI bubbles, and the row renderer routes AI turns directly there: `Travel App/app/(tabs)/concierge/chat.tsx:31`, `Travel App/app/(tabs)/concierge/chat.tsx:77`; the note is memoized at `Travel App/components/chat/PrivateVesperNote.tsx:123`.

# Suggested Fix Direction

- Move trip photos to a virtualized grouped grid (`SectionList`, FlashList, or a flattened `FlatList` with section headers) and memoize `_groupByBlock` from the query result.
- Convert Discover's Events and Angles to virtualized lists before scaling content volume; treat masonry tabs as capped editorial modules or use a virtualized masonry implementation.
- Fix the Discover active-pill mapping so the visible tab warms the correct query.
- Keep chat's 100 ms stream batching, but add measurements before changing it; only optimize further if real traces show markdown/row work crossing frame budget.
- Add an explicit image-send "preparing" state or move image conversion/upload off the visible send path.
- Split heavy sheets into memoized sections, virtualize large day/traveler lists, and prefetch detail data from the card tap where possible.

# Verification Ideas

- Add a dev-only render counter or `React.Profiler` wrapper around `PrivateVesperNote`, `GroupThreadItem`, `FeedItemRenderer`, `PhotoTile`, and major sheet sections.
- Add cheap marks: chat send tap → optimistic bubble visible, first SSE delta → rendered text, sheet open tap → first content paint, photo album mount → first tile visible.
- Seed local mock fixtures with 300 photos, 80 events, 80 angles, 20 itinerary days, and 18 travelers; record FPS/JS frame time while opening each affected screen.
- Add Sentry/native performance spans once production telemetry is enabled: `chat.stream.flush`, `discover.tab.switch`, `photos.grid.mount`, `sheet.open`.
- Dogfood with one long streaming reply containing markdown plus venue/map attachments and verify the user can scroll history without jumps.
