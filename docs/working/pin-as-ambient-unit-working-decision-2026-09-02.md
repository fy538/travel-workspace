---
doc_type: working
status: active
owner: founder / product / design
created: 2026-09-02
last_verified: 2026-09-02
expires: 2026-10-02
why_new: Preserves the founder-accepted design exploration of pins and ambient multiplayer without promoting it over canonical product or authority contracts.
source_of_truth_for: []
supersedes: []
---

# Pin as the ambient unit — working decision (2026-09-02)

**Status:** founder-accepted working decision (chat, 2026-09-02, "let's do it"). **Non-canonical** until diffed into *Multiplayer Product Strategy*, the four-root contract, and the contribution-and-consequence contract. Owner of the exploration: Claude Design project *Vesper – Social Aperture* (`fac2051b`). Boards: Ambient 2 (Sorrento, from people), 3 (pin languages), 4 (the pin itself), 5 (by-product production), 6 (the three-tier layer).

## 1. The decision

1. **The pin is the ambient multiplayer unit.** A pin is a claim by one person, at one Place, at one moment: one line in their words, zero or one photo, an audience, revocable. It is the standing-grant form of the addressed act, not a post.
2. **Self-first.** A pin exists with zero audience as private place memory. Sharing is a grant on an object the person would have made anyway. Default audience: *just me*, then the last choice made.
3. **By-product, not behavior.** Pins are produced from moments that already happen — keeping a place, taking a photo at a kept place, an occasion ending — with one optional line. Vesper never asks anyone to "go pin something."
4. **Pull, never push.** A friend's pins are visible when I look at a city (planning) and foregrounded when I am there. No arrival push, no "new pins from friends," no "friends near you." Arrival-timed delivery remains a separately consented later experiment (08-21 §7.1).
5. **The take, not the review.** No ratings, titles, or tags. Reviews stay input, not output.
6. **No counts.** No upvotes, no "12 people kept this." *This was useful* reaches the author only and is the receipt that answers asymmetric decay.
7. **Reply opens a Chat, not a comment.** A reply on a pin starts or continues a one-to-one Chat with the author, anchored to the Place, pin quoted at the top. The pin stays clean; the answers become the replier's private Place memory. Round-3 law 6 holds: social material lands in the object it changes.
8. **Leave-for-you is absorbed** as the directed case of the same object (audience = one person). The dark addressed-Place-handoff record (one sender, one recipient, one canonical Place, `send_now` / `place_pull`) is the candidate carrier for both.

## 2. Kills (no longer explored)

- The standalone "where I have been" journey map (Ambient 1) — value is at city zoom and through people, not at journey scale.
- The social aperture as a *room* (door / tab / circle page). The orientation job is served by the *from people* scope in Places plus the pin.
- Upvotes, comments under pins, counts, follower graphs, public pins.
- Arrival push; passive or inferred presence of any kind.

## 3. The three-tier interaction layer

| Tier | Unit | Verbs | Audience | Lands in | Must never become |
|---|---|---|---|---|---|
| Standing | Pin | Pin it · Take back · This was useful | just me → one person → a circle | Places (from-people scope), Life (private place memory) | a feed, a leaderboard, a check-in |
| Directed | Addressed act | Hand · Ask · Answer · Resolve · Take back | one person | the object it changes (Plan, Place, Occasion) + Chat | an inbox |
| Together | Occasion | Open together · Decide | the people in it | Home (present), Life (after) | a group chat |

Only an Occasion decides; a pin and a handed thing inform (kernel §10.5 / MP rulings).

## 4. Conditions and the value test

- **Density is the design test.** Every pin language is judged at Sorrento-sparse (3 pins) and home-dense (28). Working hypothesis from Ambient 3: sparse and dense are one object in two postures — words on the map when few, rows with a map index when many, the photo only on open.
- **The value test:** a pin works when it changes a decision (which marina, which table, what time). Dogfood metrics: *This was useful* taps; pins opened while planning (before arrival); replies that open Chats. **Not** pins created.
- **Supply bet:** 1–3 pins/week in the home city, a handful per trip, produced as by-products. This is the one bet Foursquare/Swarm lost; by-product production is the mitigation.

## 5. Grants

Five-axis contract applies (use / retention / inference / audience / action). Each pin keeps the audience it was made with; widening a circle later re-exposes nothing older. Withdrawal removes the mark and the row and recompiles derivatives. Block is a viewer-relative overlay. A pin from a blocked or narrowed grant is not drawn.

## 6. Open questions (for boards, then dogfood)

1. Circle vs. one person as the *second* default after just-me.
2. The sparse→dense handover and clustering for pin/photo languages.
3. Where the three by-product hooks live in code: the save path, photo upload (real but flag-dark), occasion end (Home evening / Life return).
4. Whether a pin and a "kept" place are one record or two.
5. How your own pins and your people's share one map without regalia (ink = people, umber = you, no colour per person).

## 7. Evidence this rests on

consumer mechanics 08-04 (time capsules, hand-me-downs, dead-drop verdict, N=2, asymmetric decay) · attention traces 08-18 §8.9–8.10 · differentiated social 08-21 §1.3, §4.2, §5.2, §7.1–7.3 · addressed Place handoff 08-21 (code, dark) · My World canon ("an absent friend can leave a perspective for a later arrival") · reviews positioning · contribution-and-consequence contract · Ambient Near-You probe (passive presence banned).

## 8. Addendum (2026-09-02, later) — layers of the map and self-sourced coordinates

Prompted by the entity-resolution handoff (`docs/working/claude-code-design-entity-resolution-object-page-handoff-2026-09-02.md`, §3.3, §6.4, §9.6): provider map-surface policy exists in the backend but is not on the wire, and provider-sourced places may not be drawable on Mapbox.

**Two surfaces that never blend.** *Vesper's map* (Mapbox geography) draws only what Vesper and its people own. The *provider surface* (Google, Foursquare) is a mode Vesper hands off to and returns from; nothing seen there is drawn on Vesper's map unless it becomes a canonical entity and its lineage permits.

| Layer | Who owns the coordinates | Drawn on | Mark |
|---|---|---|---|
| Geography | Mapbox | Vesper's map | streets, water, wash |
| Lived | the person (self-sourced at the moment of the by-product) | Vesper's map | ink heads; your umber |
| Known | Vesper: canonical entities that exist because someone acted, plus World Foundry seeded places; subject to a lineage test | Vesper's map, when lineage permits | quiet outline marks |
| Read | Vesper's editorial pipeline | Vesper's map | the plate, never a pin |
| Provider world | Google / Foursquare | their surface only, or a list under the map | never dots on Mapbox |

**Rules added**

1. **Self-sourced coordinates.** A by-product pin records the coordinates of the moment it was made — the photo's own location or the device's, as an explicit act — never the provider's coordinates for the place. The lived layer is therefore Vesper-owned regardless of the underlying place's provider lineage.
2. **No provider dots.** Provider-only places are never plotted on Vesper's cartography. They reach the map by becoming canonical through someone's tap (the resolution path). Vesper's map fills as people act on it.
3. **The known layer has a lineage test.** Whether a Vesper-owned canonical entity with Google lineage may be drawn on Mapbox must be settled before the known layer is designed further. Until `map_surface` is on the wire, boards annotate the decision rather than assume.
4. **Scope pills are layer toggles.** *From people* = lived (others); *for me* = your keeps + known; *Vesper* = read forward. Density still decides which leads.

**Open, for the resolution handoff:** the second-owner case. A newly materialized shell is owner-private; a friend's pin cannot land on a place that exists only as her shell. The pin model needs a promotion rule (first grant, or second resolver reaching the same external ref, makes the entity shared-canonical).

Ambient 10 rev 2 draws this model.
