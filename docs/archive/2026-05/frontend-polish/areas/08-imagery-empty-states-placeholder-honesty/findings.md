# Imagery, Empty States, Skeletons, Placeholder Honesty

## Summary

Vesper's doctrine is clear: place should feel concrete, empty states should teach or delight, and gray/generic placeholders should not leak into product surfaces. The implementation has the right seed in `HonestIllustration`, `AppImage`, photo upload, and story/photo flows, but the dogfood app still depends heavily on repeated fallback art, colored gradient cards, icon-only empties, and generic skeleton blocks.

Severity calibration: no P0s. The issues below will not block dogfood, but they will make the first week feel less trustworthy and less premium, especially when testers create trips outside Lisbon or browse Discover expecting editorial travel specificity.

External baseline used: Apple's HIG emphasizes accessible, understandable visual content and 44x44 pt interactive targets; Material accessibility guidance uses 48dp touch targets; WCAG 2.2 defines a 24x24 CSS px minimum web target floor. Premium travel/editorial products such as Airbnb's listing photo tour and Conde Nast Traveler destination guides use real, specific imagery as core trust substrate, not decoration.

## Findings

### P1 - Trip cards reuse Lisbon fallback art for every non-memory trip

`TripCard` says honest illustration fallback is part of the locked visual direction, but both compact and postcard variants hard-code `variant="lisbon-dusk"` regardless of destination. A Tokyo, Oaxaca, or "Somewhere new" dogfood trip can render with Lisbon rooftops, which reads as fake rather than honest.

Evidence:
- Doctrine: real destination specificity is required by "Show, don't ask" and "Interestingness" in `Travel App/docs/Design Language.md:27` and `Travel App/docs/Design Language.md:35`.
- Brand photography requires "Real places, real light" and avoids generic stock in `Travel App/docs/Brand Identity.md:193` through `Travel App/docs/Brand Identity.md:203`.
- `HonestIllustration` currently documents only Lisbon as shipped substrate in `Travel App/components/brand/HonestIllustration.tsx:10` through `Travel App/components/brand/HonestIllustration.tsx:14`.
- It exposes only `lisbon-dusk`, `brooklyn-brick`, and `generic-warm` variants in `Travel App/components/brand/HonestIllustration.tsx:22` through `Travel App/components/brand/HonestIllustration.tsx:25`.
- Compact trip cards force Lisbon art in `Travel App/components/trip/TripCard.tsx:95` through `Travel App/components/trip/TripCard.tsx:102`.
- Postcard trip cards force Lisbon art in `Travel App/components/trip/TripCard.tsx:123` through `Travel App/components/trip/TripCard.tsx:132`.
- The only committed raster assets are app chrome, not seeded destination imagery: `Travel App/assets/adaptive-icon.png`, `Travel App/assets/favicon.png`, `Travel App/assets/icon.png`, `Travel App/assets/splash-icon.png`.

### P1 - Discover's most editorial surfaces use algorithmic color blocks instead of place imagery

Discover is the place-aware browse surface, but Trending, Guides, friends posts, For You teasers, and recommendation heroes mostly render gradients, dots, or generic image icons. The result is an editorial travel surface that has names of places but very little visual proof of place.

Evidence:
- Discover defaults to Lisbon when no active trip destination exists in `Travel App/app/(tabs)/discover/index.tsx:58` through `Travel App/app/(tabs)/discover/index.tsx:60`.
- Trending destination cards render only `backgroundColor: dest.gradient[0]` plus text in `Travel App/app/(tabs)/discover/index.tsx:1407` through `Travel App/app/(tabs)/discover/index.tsx:1422` and again in `Travel App/app/(tabs)/discover/index.tsx:1425` through `Travel App/app/(tabs)/discover/index.tsx:1440`.
- Guide cards do the same, with a book icon over a color block, in `Travel App/app/(tabs)/discover/index.tsx:1494` through `Travel App/app/(tabs)/discover/index.tsx:1497` and `Travel App/app/(tabs)/discover/index.tsx:1514` through `Travel App/app/(tabs)/discover/index.tsx:1517`.
- Trending and guide data models carry only gradient/card height, not `image_url`, in `Travel App/types/discover.ts:27` through `Travel App/types/discover.ts:49`.
- Data adapters assign deterministic gradients from a shared palette in `Travel App/data/discover.ts:73` through `Travel App/data/discover.ts:97`.
- For You venue/accommodation/site cards use a small colored dot, not an image or destination-specific illustration, in `Travel App/components/discover/FeedItemRenderer.tsx:101` through `Travel App/components/discover/FeedItemRenderer.tsx:123` and `Travel App/components/discover/FeedItemRenderer.tsx:203` through `Travel App/components/discover/FeedItemRenderer.tsx:248`.
- Friend venue and moment cards show generic image icons over placeholder colors in `Travel App/components/discover/FeedItemRenderer.tsx:304` through `Travel App/components/discover/FeedItemRenderer.tsx:319` and `Travel App/components/discover/FeedItemRenderer.tsx:341` through `Travel App/components/discover/FeedItemRenderer.tsx:355`.

### P2 - Empty states are mostly generic icon/text surfaces, not contextual teaching moments

The shared `EmptyState` component standardizes an icon, title, subtitle, and CTA, but it also makes empties feel interchangeable. It defaults to sacred purple for all empty-state icons, which conflicts with the doctrine that purple signals Vesper/AI presence. Discover then implements several local empties with "No..." or "Nothing..." copy and no visual specificity.

Evidence:
- Design doctrine says empty states must teach or delight in `Travel App/docs/Design Language.md:32` through `Travel App/docs/Design Language.md:35`.
- It explicitly bans empty states without specific contextual content in `Travel App/docs/Design Language.md:315` through `Travel App/docs/Design Language.md:327`.
- Shared `EmptyState` documents a generic icon/heading/subtext pattern in `Travel App/components/ui/EmptyState.tsx:1` through `Travel App/components/ui/EmptyState.tsx:5`.
- Shared `EmptyState` always renders purple icon treatment in `Travel App/components/ui/EmptyState.tsx:25` through `Travel App/components/ui/EmptyState.tsx:30` and `Travel App/components/ui/EmptyState.tsx:51` through `Travel App/components/ui/EmptyState.tsx:58`.
- Discover's local empties include generic copy such as "Nothing within range", "No events found", "Nothing trending yet", and "No guides yet" in `Travel App/app/(tabs)/discover/index.tsx:859` through `Travel App/app/(tabs)/discover/index.tsx:863`, `Travel App/app/(tabs)/discover/index.tsx:1349` through `Travel App/app/(tabs)/discover/index.tsx:1355`, `Travel App/app/(tabs)/discover/index.tsx:1391` through `Travel App/app/(tabs)/discover/index.tsx:1405`, and `Travel App/app/(tabs)/discover/index.tsx:1468` through `Travel App/app/(tabs)/discover/index.tsx:1481`.
- Trip story's not-ready state uses the generic shared pattern and "No story yet" copy in `Travel App/app/(tabs)/trips/[tripId]/story.tsx:289` through `Travel App/app/(tabs)/trips/[tripId]/story.tsx:296`.

### P2 - Skeletons are shaped well but still read as generic gray-block loading

The skeleton primitive is better than spinners, but Vesper's doctrine goes further: loading should evoke anticipation and streaming placeholders should be brand-voiced, not generic blocks. Several high-salience surfaces still rely on anonymous `SkeletonBlock` stacks with no destination or task copy.

Evidence:
- Brand motion says loading states should avoid spinners and use anticipation copy plus warm skeletons in `Travel App/docs/Brand Identity.md:172` through `Travel App/docs/Brand Identity.md:179`.
- Design doctrine says the dashed reserved slot is the solution for late attachments and never to use generic skeleton blocks in `Travel App/docs/Design Language.md:253` through `Travel App/docs/Design Language.md:261`.
- It also bans gray skeleton blocks as "no content yet" treatment in `Travel App/docs/Design Language.md:315` through `Travel App/docs/Design Language.md:329`.
- `Skeleton.tsx` describes itself as a generic rectangle/line/circle skeleton system in `Travel App/components/ui/Skeleton.tsx:1` through `Travel App/components/ui/Skeleton.tsx:21`.
- Discover uses repeated skeleton cards and blocks for angle, lens, and guide loading in `Travel App/app/(tabs)/discover/index.tsx:921` through `Travel App/app/(tabs)/discover/index.tsx:928`, `Travel App/app/(tabs)/discover/index.tsx:948` through `Travel App/app/(tabs)/discover/index.tsx:962`, and `Travel App/app/(tabs)/discover/index.tsx:1449` through `Travel App/app/(tabs)/discover/index.tsx:1454`.
- Trip home cold-open uses an anchor-card placeholder plus two anonymous attention-card blocks in `Travel App/components/trip-home/ConciergeAttentionSection.tsx:460` through `Travel App/components/trip-home/ConciergeAttentionSection.tsx:493`.
- Memory loading uses three plain blocks in `Travel App/app/(tabs)/trips/[tripId]/memory.tsx:74` through `Travel App/app/(tabs)/trips/[tripId]/memory.tsx:85`.

### P2 - Trip Story can duplicate one photo across many slots and has no branded visual fallback when there are no photos

The story flow is one of the strongest place-memory surfaces, but the auto-fill logic cycles through the same photo pool with modulo indexing. If a user has one or two photos and several story slots, Vesper may repeat the same image across unrelated narrative sections. If there are no photos, the hero simply omits imagery instead of showing a branded, destination-aware fallback.

Evidence:
- Story cover chooses a best photo or `null` in `Travel App/app/(tabs)/trips/[tripId]/story.tsx:82` through `Travel App/app/(tabs)/trips/[tripId]/story.tsx:94`.
- Section auto-fill uses `pool[i % pool.length]`, which repeats photos across slots when slots outnumber photos, in `Travel App/app/(tabs)/trips/[tripId]/story.tsx:96` through `Travel App/app/(tabs)/trips/[tripId]/story.tsx:114`.
- The hero only renders an image when `heroImageUrl` exists in `Travel App/components/memory/TripStoryHero.tsx:23` through `Travel App/components/memory/TripStoryHero.tsx:34`.
- Empty photo slots are dashed camera prompts rather than place-aware fallback art in `Travel App/components/memory/PhotoSlotCard.tsx:109` through `Travel App/components/memory/PhotoSlotCard.tsx:121`.

### P3 - Empty-state recovery controls are not mechanically protected to premium mobile target size

Some empty-state recovery controls are styled locally with small vertical padding and no explicit minimum hit area. This is adjacent to polish because empty states are recovery moments; small targets make the app feel less native and less cared for.

Evidence:
- Vesper's own accessibility floor is `minTouchTarget 44pt` in `Travel App/docs/Design Language.md:153` through `Travel App/docs/Design Language.md:154`.
- Shared `EmptyState` action has padding but no explicit `minHeight` in `Travel App/components/ui/EmptyState.tsx:70` through `Travel App/components/ui/EmptyState.tsx:80`.
- Discover's empty/retry controls use local styles without minimum height in `Travel App/app/(tabs)/discover/index.tsx:1696` through `Travel App/app/(tabs)/discover/index.tsx:1708` and `Travel App/app/(tabs)/discover/index.tsx:1771` through `Travel App/app/(tabs)/discover/index.tsx:1775`.

## Evidence

Internal doctrine:
- `Travel App/docs/Design Language.md:27` through `Travel App/docs/Design Language.md:35` anchors concrete options and specific empty/loading content.
- `Travel App/docs/Brand Identity.md:191` through `Travel App/docs/Brand Identity.md:207` defines real-place photography and sparse illustration.
- `Travel App/docs/Design Language.md:315` through `Travel App/docs/Design Language.md:329` bans generic empty states and gray skeleton no-content treatment.

External guidance:
- [Apple HIG - Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility): use accessible controls and sufficient touch targets; Vesper already codifies the 44pt floor.
- [Apple HIG - Images](https://developer.apple.com/design/human-interface-guidelines/images): imagery should communicate clearly and support the experience, not act as arbitrary decoration.
- [Material Design accessibility](https://m2.material.io/design/usability/accessibility.html): touch targets should be at least 48x48 dp.
- [WCAG 2.2 Target Size Minimum](https://www.w3.org/TR/WCAG22/#target-size-minimum): 24x24 CSS px is the web accessibility floor, not the premium native target.
- [Airbnb photo tour help](https://www.airbnb.com/help/article/477): high-quality, organized photos are treated as decision support for choosing a place.
- [Conde Nast Traveler destination guides](https://www.cntraveler.com/destinations): editorial travel browsing leads with destination-specific imagery and expert context.

## Suggested Fix Direction

Seed real imagery first for: trip cards, Discover Trending, Discover Guides, For You venue/event/accommodation/site teasers, trip story hero, and memory/photo empty states. These are the dogfood flows where the user most expects Vesper to know the place.

Use a three-tier fallback ladder:
1. Curated/licensed or user-provided real image when available.
2. Generated or curated destination fallback art keyed by `place_id`/slug, with provenance metadata and a visible editorial label.
3. Algorithmic color/gradient only for low-salience utility rows, never for hero cards, destination cards, story covers, or editorial guide cards.

Generated vs curated vs algorithmic:
- Curated is best for dogfood trust on seeded cities and guides.
- Generated is acceptable for long-tail destination fallback art if it is explicitly style-governed, reviewed, and labeled as illustration rather than photo.
- Algorithmic should only choose palettes for surfaces that are not pretending to represent a place.

Rules to prevent placeholder leakage:
- Add a `visual_status` field or local adapter metadata: `real_photo`, `curated_illustration`, `generated_illustration`, `algorithmic_placeholder`, `none`.
- In dogfood builds, assert/log when high-salience surfaces render `algorithmic_placeholder` or destination-mismatched fallback art.
- Add a static check for `variant="lisbon-dusk"` outside Lisbon-specific mocks/tests.
- Require every destination card type to carry `image_url` or `fallback_art_key`; avoid accepting only `gradient`.
- Make `EmptyState` accept a contextual `visual` slot and a `tone`, with purple opt-in only for Vesper-authored states.
- Give shared empty/retry actions a minimum 44pt height.

## Verification Ideas

- Seed dogfood fixtures for Lisbon, Tokyo, Oaxaca, Barcelona, and "no destination yet"; screenshot Trips, Discover, For You, Story, Photos, and Memory.
- Run a visual audit that flags repeated identical fallback art within the same viewport.
- Add unit tests for fallback selection: Lisbon gets Lisbon art, Brooklyn gets Brooklyn art, unknown destination gets generic labeled illustration, not Lisbon.
- Add screenshot checks for empty states with no data, failed data, no permission, limited photos, and no destination.
- Add an accessibility snapshot or style assertion that empty/retry CTAs meet the 44pt minimum target.
