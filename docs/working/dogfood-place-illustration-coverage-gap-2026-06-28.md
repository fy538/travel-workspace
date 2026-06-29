# Dogfood Place-Illustration Coverage Gap — Image Generation Spec

> Status: **closed** (Stream E merged — PR #29, `bc24595` on travel-app `main`, 2026-06-29)
> Owner: founder / engineering
> Created: 2026-06-28
> Scope: `travel-app` bundled place art (`assets/ai/places/`), `constants/placeIllustrations.ts`, backend `photo_resolve.py` parity
> Audience: an agent/operator with an image-generation tool, executing the media lane ("Stream E")
> Companion to: `dogfood-substrate-richness-and-generation-backlog-2026-06-28.md`, `dogfood-qa-substrate-system-investigation-2026-06-28.md`

**Question this doc answers:** Several mock personas have trips in cities that have **no city-specific illustration**, so those trips render generic stand-in art instead of on-brand place art. Which cities are missing, why it matters, and exactly what to generate + wire to close it.

---

## TL;DR

- Images **never 404** — there is a graceful 3-tier resolver. This is a **city-authenticity** gap, not a broken-image bug.
- **38 cities** had bundled per-city "place riso" art. **6 referenced cities were missing it** — **closed 2026-06-29** (istanbul, brooklyn, vienna, bangkok, oaxaca + humlebaek→copenhagen alias).
- It disproportionately hits the **flagship persona `elif`** (4 of her 5 cities) and creates a **mock-vs-backend asymmetry** for **Istanbul** and **Brooklyn** (both are backend dogfood packs with real photos, but go generic in mock/Maestro/screenshot mode).
- Fix = generate **6 variants per city** (`day/night/site/fun/nature/hero`), drop into `assets/ai/places/<slug>/`, add one entry to `constants/placeIllustrations.ts`. ~36 images.
- This is **not wedge-blocking** (Lisbon is fully covered). It is an optional richness lane, gated by the dogfood authoring discipline.

---

## How images resolve today (the 3-tier waterfall)

Source: `travel-app/utils/entityImage.ts` → `resolveEntityImage()`.

| Tier | Source | Wins when | Used by |
|------|--------|-----------|---------|
| 1 | **Real backend photo URL** (`resolveDogfoodMediaUrl`) | Backend has a seeded/CDN photo | Live backend / EAS dogfood |
| 2 | **Bundled place riso** (`resolvePlaceIllustration`, `constants/placeIllustrations.ts`) | Entity carries a `citySlug` that is in `BUNDLED_PLACE_SLUGS` | Mock mode, Maestro, screenshots |
| 3 | **Generic category pool** (`AI_IMAGE_POOLS[imageClass]`, `constants/aiImagePools.ts`) | City not bundled, but entity type classifies (restaurant, cafe, culture_art, …) | Fallback |
| 4 | **Nothing** → call site renders branded illustration / color box | Type unclassifiable or fallback flag off | Last resort |

Key consequences:

- In **mock / Maestro / screenshot** mode (`EXPO_PUBLIC_USE_MOCK_API=true`), Tier 1 is unavailable, so **Tier 2 (place riso) is the only path to city-authentic art.** A city missing from Tier 2 drops to **generic** Tier 3 art.
- The tier is toggled by `EXPO_PUBLIC_AI_IMAGE_FALLBACK` (on unless explicitly `'false'`).
- **Style rule (from `placeIllustrations.ts` header):** place riso *may* approximate landmarks (Tagus + dome for Lisbon, Alhambra for Granada) **because the style is clearly stylized print art, not a photo.** Category pools (Tier 3) stay **landmark-free** on purpose. Do not blur these two styles.

---

## Current coverage — 38 bundled cities (Tier 2)

From `BUNDLED_PLACE_SLUGS` (`constants/placeIllustrations.ts`):

```
amalfi-coast, athens, barcelona, bilbao, bologna, bordeaux, cagliari, catania,
copenhagen, dubrovnik, florence, genoa, granada, ibiza, kyoto, lecce, lisbon,
lyon, madrid, malaga, mallorca, marseille, mexico-city, milan, naples, nice,
palermo, paris, porto, rome, san-sebastian, seville, split, thessaloniki,
tokyo, valencia, valletta, venice
```

Backend real-photo packs (Tier 1, `tools/dogfood/content/media/`): **lisbon, rome, tokyo, istanbul, brooklyn**.

---

## The gap — persona cities with NO place riso

Persona → city coverage (city-authentic Tier 2 art):

| Persona | Cities in trips | Tier-2 covered? |
|---------|-----------------|-----------------|
| `ana` | Madrid, Lisbon, San Sebastián, Rome, Paris, Seville | ✅ all |
| `carmen` | Mexico City | ✅ |
| `dev` | Athens | ✅ |
| `urgent` | Porto | ✅ |
| `ben` | Kyoto ✅, Copenhagen ✅, **Humlebæk** ❌ | partial |
| `between` | **Brooklyn** ❌ | none |
| `elif` (flagship) | Rome ✅, **Istanbul** ❌, **Vienna** ❌, **Bangkok** ❌, **Oaxaca** ❌ | 1 of 5 |
| `torture` | Kyoto (adversarial unicode string) | by design — leave as-is |
| `nadia`, `omar`, `ready` | no city trips (Atlas/hero specialists) | n/a |

### Missing cities (the work)

| Slug | Referenced by | Backend pack? | Why it matters | Priority |
|------|---------------|---------------|----------------|----------|
| `istanbul` | `elif` | **Yes** (30 real photos) | Mock/Maestro goes generic while backend is authentic — **asymmetry in the exact mode visual QA runs**; flagship persona | **P0** |
| `brooklyn` | `between`, elif baseline | **Yes** (20 real photos) | Same backend-vs-mock asymmetry; home-city control sample | **P0** |
| `vienna` | `elif` | No | Flagship breadth | P1 |
| `bangkok` | `elif` | No | Flagship breadth (non-Europe) | P1 |
| `oaxaca` | `elif` | No | Flagship breadth (non-Europe) | P1 |
| `humlebaek` | `ben` | No | Minor daytrip (Louisiana museum); **may reuse `copenhagen`** instead of new art | P3 |

**Net new art:** 5 cities × 6 variants = **30 images** (P0+P1), +6 optional for Humlebæk (or skip and alias to Copenhagen).

---

## Asset spec (match existing exactly)

Verified against existing `assets/ai/places/lisbon/*` and the resolver.

| Property | Value |
|----------|-------|
| Format | `.jpg` |
| Variants (filenames) | `day.jpg`, `night.jpg`, `site.jpg`, `fun.jpg`, `nature.jpg`, `hero.jpg` |
| Dimensions — `day/night/site/fun/nature` | **1200 × 900** (4:3) |
| Dimensions — `hero` | **1200 × 675** (16:9) |
| Style | Riso / gouache stylized print art (NOT photographic). Landmark approximation allowed because the style reads as illustration. Match the existing palette/grain of the bundled set. |
| Path | `travel-app/assets/ai/places/<slug>/<variant>.jpg` |
| Slugs to create | `istanbul`, `brooklyn`, `vienna`, `bangkok`, `oaxaca` (+ optional `humlebaek`) |

### Variant intent (so the 6 images differ meaningfully)

| Variant | Used for | Scene intent |
|---------|----------|--------------|
| `day` | default daytime card | iconic daytime cityscape / street feel |
| `night` | evening/nightlife context | same city after dark, warm light |
| `site` | landmark / cultural site | the city's signature site, stylized |
| `fun` | playful / social context | market, café terrace, lively street |
| `nature` | outdoor / viewpoint | water, hills, park, coastline as relevant |
| `hero` | wide hero banner (16:9) | cinematic wide establishing shot |

The resolver picks a variant from `travelLens` + `entityType` (or a forced/seeded variant), so all six should be visually distinct and individually usable.

---

## Code wiring (after images are dropped in)

1. Add **one block per new city** to `PLACE_ILLUSTRATIONS` in `travel-app/constants/placeIllustrations.ts` (mirror the existing shape). `BUNDLED_PLACE_SLUGS` derives automatically from the keys — no second edit needed.

```ts
'istanbul': {
  day: require('../assets/ai/places/istanbul/day.jpg'),
  night: require('../assets/ai/places/istanbul/night.jpg'),
  site: require('../assets/ai/places/istanbul/site.jpg'),
  fun: require('../assets/ai/places/istanbul/fun.jpg'),
  nature: require('../assets/ai/places/istanbul/nature.jpg'),
  hero: require('../assets/ai/places/istanbul/hero.jpg'),
},
```

2. **Slug must match `places.slug`** the entity carries (the comment in `placeIllustrations.ts` notes slugs mirror the backend). Confirm the slug a trip/venue actually emits (e.g. `istanbul`, `brooklyn`, `mexico-city` style — hyphenated, lowercase) before naming the folder, or the riso won't resolve.

3. `EXPO_PUBLIC_AI_IMAGE_FALLBACK` must not be `'false'` for Tier 2 to engage.

---

## Backend parity (separate, optional follow-up)

The bundled app art is described as the **interim transport** while the CDN pipeline is unprovisioned:

- Resolver waterfall: `travel-agent/backend/core/photo_resolve.py` (riso variant beats Pexels stock per place row).
- Seeder: `travel-agent/.../seed_place_illustrations.py` — **unprovisioned** (S3/CDN not wired).

For full Tier-1 parity (so live backend serves the same place riso), the generated variants would also need uploading via that pipeline once provisioned. **Out of scope for the mock-coverage fix**; note it so the two don't drift.

---

## Acceptance criteria

- [ ] `assets/ai/places/{istanbul,brooklyn,vienna,bangkok,oaxaca}/` each contain 6 variants at the correct dimensions.
- [ ] `PLACE_ILLUSTRATIONS` has a key for each new slug; `npx tsc --noEmit` passes (all `require()` paths resolve).
- [ ] In mock mode, `elif`'s Istanbul trip + the Brooklyn baseline show city art (not a generic restaurant/cafe pool image).
- [ ] Style matches the existing bundled set (stylized print art, not photographic); category pools left untouched.
- [ ] (Optional) Humlebæk decision recorded: new `humlebaek` art OR alias to `copenhagen`.

---

## What NOT to do

| Don't | Why |
|-------|-----|
| Generate photographic stock for place riso | Tier 2 is intentionally stylized illustration; photos belong to Tier 1 (real backend) |
| Add landmarks to the category pools (Tier 3) | Those stay landmark-free by design |
| Generate substrate (trips/observations) here | This lane is **art only**; substrate is Stream B's job |
| Generate at seed time via runtime provider API | Violates the dogfood authoring rule (`cursor_subscription_assisted`, no runtime provider calls) |
| Expand to future cities (Seoul, Marrakech, Barcelona already bundled) | Only close the 6 referenced gaps; don't grow the matrix |

---

## Key file index

| Topic | Path |
|-------|------|
| Image resolver (waterfall) | `travel-app/utils/entityImage.ts` |
| Place riso registry | `travel-app/constants/placeIllustrations.ts` |
| Place riso assets | `travel-app/assets/ai/places/<slug>/<variant>.jpg` |
| Category pools (Tier 3) | `travel-app/constants/aiImagePools.ts` |
| Place illustration resolver | `travel-app/utils/placeIllustration.ts` |
| Dogfood media resolver (Tier 1) | `travel-app/utils/dogfoodMedia.ts` |
| Backend resolver waterfall | `travel-agent/backend/core/photo_resolve.py` |
| Backend place-illustration seeder (unprovisioned) | `travel-agent/.../seed_place_illustrations.py` |
| Personas (city references) | `travel-app/constants/personas/*.ts` |
