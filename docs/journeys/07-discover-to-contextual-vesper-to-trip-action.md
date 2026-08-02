# 07 - Places To Contextual Vesper To Trip Action

> Status: implementation evidence in progress; not device-certified
> Owner: founder / engineering  
> Last updated: 2026-08-02
> Primary phase: inspiration / place-aware planning

## Product Promise

Places is not a browse-only endpoint. A traveler can open a concrete place,
review the context Vesper will receive, ask from a private thread, and carry
the resulting decision into the canonical Trips action path.

Vesper is the connective spine, not a second itinerary: it helps form and
explain a decision. Trips remains the owner of shared itinerary mutations and
their durable receipts.

## Canonical User Story

As a traveler browsing a place, I want to open a venue, experience,
accommodation, or dossier, review what Vesper will use, and continue without
re-explaining it. If I make a trip decision, I want the normal Trips flow to
own the write and show its receipt.

## Why This Journey Matters

- Places, Vesper, and Trips are the active product surfaces; legacy
  Discover/Atlas references must not define new behavior.
- A thin `ConversationSeed` helps the chat form a helpful opening turn, while
  typed composer attachments make the concrete object visible, removable, and
  server-resolvable.
- The wrong failure is not merely a generic answer: it is hidden context,
  accidental group visibility, a non-canonical trip write, or a funnel that
  cannot be debugged without logging traveler content.

## Starting State

- Persona: traveler with or without an active trip.
- Trip state: no trip for solo inspiration variant; planning trip for add-to-plan variant.
- Fixture: a Places city/detail/map entry with a concrete place, venue,
  experience, accommodation, or dossier.
- Permissions: no location required, but place search/network state matters.

## Primary Surfaces

- Routes: `/(tabs)/places`, `/(tabs)/places/map`, `/place/[placeSlug]`,
  `/venue/[venueId]`, `/accommodation/[accommodationId]`,
  `/dossier/[dossierId]`, `/conversations/create`, and the private/group
  chat routes reached from it.
- Code anchors: `app/place/[placeSlug].tsx`, `app/(tabs)/places/map.tsx`,
  `app/conversations/create.tsx`, `hooks/useConversationEntrySeed.ts`,
  `backend/api/routes/_composer_attachments.py`, and
  `backend/concierge/entry_context.py`.

## Canonical Steps

1. Open Places, a Place detail, or the Places map.
2. Select a concrete object or an area context.
3. Tap **Ask Vesper**.
4. Confirm a private, review-first composer opens with a removable context
   chip and no auto-send.
5. Send an explicit opening turn. Confirm the server resolves the typed
   attachment and classifies the AI run as `places`.
6. If the discussion leads to a trip mutation, use the established Trips
   proposal/commit route for the trip and audience—not an ad-hoc chat write.
7. Confirm its durable action receipt links to the active AI run when one
   exists, and that the Trips read model reflects the canonical mutation.
8. Return to Places and confirm the user can continue browsing; no hidden
   context or generic thread is left behind.

## Expected Outcome

- User-visible state: the traveler sees, can remove, and explicitly sends the
  object context before Vesper receives it.
- Data state: typed attachment carries a stable reference; the server resolves
  it as best-effort grounding; an opaque `entry_handoff_id` connects opening,
  accepted turn, AI run, and later receipt without copying prompt text.
- Cross-surface coherence: Places creates context, Vesper helps with the
  decision, and Trips owns shared plan mutation and receipts.
- Trust state: the route is private by default. Group-visible work must enter
  through the normal proposal/review boundary.

## Must Never Happen

- A Places entry silently sends a prompt or hides the attached context.
- A malformed/mixed typed attachment is persisted or treated as authoritative
  instead of falling back honestly.
- A private Places question becomes group-visible through route defaults.
- A Places/Vesper flow writes a shared itinerary outside the canonical Trips
  proposal/commit boundary or cannot produce a durable receipt.
- Funnel telemetry includes a prompt, display label, or raw attachment body.

## AI Trace Prompt

```text
Trace a Places detail or map entry into Vesper. Verify review-first routing,
typed composer attachment construction, server grounding, and `places` AI-run
classification. Then follow a real trip action through its existing canonical
Trips path and receipt. Inspect telemetry only for opaque IDs and
classifications—never the prompt or display label.
```

## First Automation Target

Maintain a four-layer proof, with each layer named rather than inferred:

1. **Contract:** typed attachment validators reject mixed/missing references;
   client route parsing preserves the opaque handoff identity.
2. **Logic:** a Places seed produces `AIRunSurface.PLACES`; terminal metadata
   returns both `ai_run_id` and the opaque handoff ID; an action receipt created
   inside the run scope retains the run ID.
3. **Visual/device:** Places detail and map each show a removable context chip;
   removing it changes what is sent; the route remains private until a traveler
   deliberately selects a group-safe Trips action.
4. **Live canary:** one fixture traveler runs the flow below against a
   non-production fixture trip. This remains open until device evidence is
   attached; backend or mock tests alone are not a certification.

## Places → Vesper → Trips Live Canary

**Setup:** fixture traveler, fixture planning trip, one seeded Places object,
and a deterministic/replay-safe response. Do not use a real place label,
prompt, or personal trip in logs or screenshots.

**Pass rubric:**

1. Enter from Place detail and Places map separately; both open the private
   review composer with a context chip.
2. Remove the chip once and send once with it intact. The former has no typed
   attachment; the latter has exactly one well-typed reference.
3. The accepted turn terminal metadata has `ai_surface=places`, `ai_run_id`,
   and the same opaque `entry_handoff_id` recorded at entry. No prompt or label
   appears in telemetry.
4. A shared-plan decision travels through the existing proposal/commit route.
   The canonical action receipt and Trips read model agree; a group member can
   see only group-safe content.
5. Capture device evidence and add a deterministic regression test for any
   failed leg before another live retry.

**Current limitation:** typed attachment resolution is grounding, not a
guarantee that every catalog object remains available at send time. An absent
or stale object must lead Vesper to acknowledge the missing context, rather
than fabricate a specific recommendation.
