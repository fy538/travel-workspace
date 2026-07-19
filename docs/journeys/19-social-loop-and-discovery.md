# 19 - Social Loop And Cross-Entity Discovery

> Status: certified
> Owner: founder / engineering
> Last updated: 2026-07-19
> Primary phase: breadth surfaces (social + search)

## Product Promise

A user can find people through their taste, follow them, and discover places across the whole catalog via search — and every result and profile routes to a real, live destination.

## Canonical User Story

As a user, I want to discover people (by taste/public profile) and entities (by search) and act on them, so that the app is a place to find and follow taste, not just plan a single trip.

## Why This Journey Matters

- The social surface (companions, following, public taste profiles, follow-from-taste) and universal cross-entity search now share one executable journey.
- These are the "next initiative" growth loops (social/photo-journal) and the discovery breadth; the journey is now certified with disposable live identities as well as mock/device proof.
- Each is a launch point: a search result or profile that no-ops is a dead growth loop.

## Starting State

- Persona: a user with a public taste profile + a few companions, and a seeded multi-entity catalog (venues, places, guides, dossiers).

## Primary Surfaces

- Routes: `/search` (universal overlay), `/atlas/companions`, `/profile/[userId]`, `/place/[slug]`, `/venue/[id]`, `/guide/[slug]`.
- App docs: [Discover Spec](../../travel-app/docs/page-specs/discover.md), social/people surfaces.

## Canonical Steps

1. Open universal search → query returns correct cross-entity results (person / venue / place / guide / trip / saved).
2. Tap a result → routes to a live entity reader (not a 404 / dead route).
3. Open a companion / public taste profile (`/profile/[userId]`) → renders their shareable taste, follow CTA works.
4. Follow from taste → the follow persists and the companions list updates.
5. Confirm privacy: a public profile exposes only shareable taste, never private constraints or trip membership.

## Expected Outcome

- Search returns correct cross-entity results, each routing to a live destination.
- Public profiles render shareable taste and a working follow loop.
- No private data (constraints, trip membership, private memory) leaks onto a public profile.

## Must Never Happen

- A search result routes to a dead/404 entity.
- A public taste profile leaks private constraints, memory, or trip membership.
- Follow / unfollow no-ops or fails to persist.
- Search returns stale/duplicate entities or misses seeded ones.

## AI Trace Prompt

```text
Trace universal search (query → cross-entity results → entity reader) and the social loop (public profile → follow → companions). Verify every result/profile routes live, follow persists, and no private data (constraints, memory, trip membership) leaks onto a public profile.
```

## Current Automation Evidence

- FE contract/mock walk: `travel-app/__tests__/journeys/journey-19-mock-walk.smoke.test.tsx` proves person-search routing, the default-deny public projection, follow/unfollow persistence, and personal-save boundaries.
- Routed iOS proof: `travel-app/.maestro/48-journey-19-search-social-loop.yaml` walks search → public profile → Follow → Your people and asserts the relationship survives navigation.
- Search-result navigation replaces the modal route in place, so both normal in-app entry and a root deep link reach the destination without a back-then-push race.

- Lived proof: `persona-cert:J19` creates disposable companion, outsider, and public-profile fixtures; it proves mutual-trip people search, outsider non-enumeration, default-deny profile projection, idempotent follow conflict, and persisted following state without mutating seeded social graphs.
