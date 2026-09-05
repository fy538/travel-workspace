---
doc_type: working
status: active
owner: founder / product / design / frontend
created: 2026-09-02
last_verified: 2026-09-02
expires: 2026-10-02
why_new: Gives Claude Code and Claude Design one bounded execution brief for designing the provider-candidate-to-entity-page transition, including the owner-private sparse shell, without reopening Places-root composition or authorizing a catalog backfill.
promotes_to: null
supersedes: []
source_of_truth_for: []
depends_on:
  - docs/decisions/2026-08-08-place-identity-and-provenance.md
  - docs/decisions/2026-08-11-entity-envelope.md
  - docs/decisions/2026-08-11-entity-status-block.md
  - docs/working/places-consumer-experience-anatomy-2026-08-29.md
  - docs/working/places-four-state-design-fixture-brief-2026-08-29.md
  - docs/systems/four-root-loop-object-surface.md
  - docs/systems/contribution-and-consequence.md
  - travel-app/docs/design-decisions/places-object-page-shell.md
  - travel-app/docs/design-decisions/entity-title-register.md
---

# Claude Code + Claude Design Handoff — Candidate Resolution and Entity Object Page

## What this handoff is

This document is a complete execution brief for a Claude Code session using
Claude Design to design and exercise one frontend seam:

```text
person taps a place-like result
  -> Vesper establishes canonical identity when necessary
  -> one real entity object page opens
  -> sparse, live, personal, and verified facts remain visibly distinct
```

The work should produce an interactive design prototype and an implementation
handoff. It should not implement production React Native during the design
session unless the founder separately requests that follow-on.

The design question is deliberately narrower than “redesign Places”:

> How should a place-like candidate become a useful, trustworthy Vesper object
> when Vesper may initially know only its provider identity, name, category,
> and location?

The answer must work for restaurants, museums/sites, accommodations, and
experiences while respecting the current implementation limit: only venue
provider misses may create an owner-scoped shell today. Other kinds require an
existing canonical mapping or must fail honestly.

---

# Part I — Product and interaction contract

## 1. Outcome to design

Design one continuous interaction with three successful paths and two failure
paths:

1. **Canonical open** — the candidate already carries a canonical
   `EntityRef`; the object page opens immediately.
2. **Resolved open** — the candidate carries only an `ExternalRef`; Vesper
   resolves it to an existing canonical entity, then opens that entity.
3. **Owner-shell open** — an explicitly tapped venue is not in the catalog;
   Vesper creates the minimum owner-private shell, then opens a sparse but real
   object page.
4. **Temporary failure** — the provider or network is unavailable; the person
   remains at the origin with retry and provider-continuation options.
5. **Unsupported or ambiguous resolution** — Vesper cannot safely create or
   choose a canonical entity; it does not invent one and does not navigate to
   a broken page.

The prototype must answer:

- Does a tap still feel like opening a place, rather than starting a database
  operation?
- Can resolution latency be legible without introducing a technical loading
  screen?
- Can an owner-private sparse object feel intentional rather than broken?
- Can the page distinguish stable identity, current provider truth, Vesper
  interpretation, and personal relationship without becoming a provenance
  dashboard?
- Can a person return to exactly where they came from?
- Can failure preserve the candidate and the person's intent?

## 2. Product boundary: what Vesper owns

Vesper is not trying to become a universal places directory.

Vesper owns:

- application identity and correction across Places, Chat, Plan, Map, Atlas,
  Saves, and later encounters;
- the person's relationship to an entity: new, saved, planned, or lived;
- Vesper's source-grounded judgment and persisted Take when one already
  exists;
- why the entity matters in the person's current context;
- consequences such as saving, adding to a plan, asking, correcting, or
  returning; and
- continuity back to the exact originating surface and state.

Vesper should leverage providers such as Google or Foursquare for:

- candidate discovery and provider identity;
- current operational facts such as opening status and hours;
- provider-permitted media;
- provider map or directions continuation when required; and
- source evidence and freshness, not product identity.

Vesper should not compete with Google on:

- exhaustive global listing coverage;
- the broadest review corpus;
- continuously maintained business profiles;
- mass photo inventory;
- commodity map search;
- turn-by-turn navigation; or
- pretending to know volatile logistics it has not checked.

The interface must make that division feel like focus, not deficiency.

## 3. Locked data and authority rules

These are design constraints, not suggestions.

### 3.1 Identity

- `EntityRef { type, id }` is Vesper-owned, canonical identity.
- `ExternalRef { provider, external_id }` is provider-owned identity.
- Provider IDs never become navigation IDs, Save IDs, itinerary IDs, or
  public Vesper URLs.
- Search and discovery remain read-only. Materialization occurs only after an
  explicit person gesture that requires a real object.
- Redirect and merge behavior is resolved before the destination page opens.

### 3.2 Privacy

- A newly materialized shell is `owner_provisional` and readable only by its
  owner.
- It must not appear globally verified merely because it has a numeric ID.
- It must not become public or group-visible through page opening.
- Share should be absent or clearly constrained until a safe share contract
  exists. A public-looking share affordance must not leak a private shell.

### 3.3 Source use

- Store the durable provider identity and only policy-approved normalized
  shell fields.
- Do not persist raw provider payloads, reviews, unrestricted provider photos,
  or copied rich profiles as Vesper catalog truth.
- Provider attribution and freshness must remain recoverable where current
  facts are displayed.
- Missing provider data remains missing. The page may offer an explicit check;
  it may not fill the gap with plausible copy.

### 3.4 Interpretation

- Opening an entity never generates a new Take.
- Render a Take only when an authorized, persisted Take already exists.
- If no Take exists, use a source-grounded stable brief if one exists.
- If neither exists, let the page be short. Do not generate a generic summary
  merely to fill the page.

### 3.5 Backfill

- This project authorizes no bulk import, data sweep, geocoding sweep, or
  catalog backfill.
- The design should assume an incremental world: many candidates remain
  provider-only until someone acts.
- An explicit tap may trigger the existing on-demand venue-resolution path.
  That is not authorization for background materialization.

## 4. Scope and non-scope

### In scope

- Candidate tap feedback and resolution continuity.
- The transition into an existing entity route.
- The owner-private sparse entity page.
- Verified, live-current, unknown, and personal layers on that page.
- Error, retry, and provider-continuation behavior.
- Back-navigation continuity.
- A neutral candidate-origin harness sufficient to test the transition.
- Design annotations precise enough for a later React Native implementation.

### Out of scope

- Redesigning Home.
- Redesigning the Places root, its section arbitration, its root feed, or its
  map/composition transformation.
- Changing root-projection semantics or contribution policy.
- Redesigning search ranking or recommendation ranking.
- Designing a generic place database administration tool.
- Backfilling any entity type.
- Inventing provider licensing or retention rights.
- Replacing the established object-page shell, title register, design tokens,
  or navigation model without evidence.
- Implementing automatic site, accommodation, or experience shell creation.
- Adding a public “unverified” catalog.

## 5. Concurrency boundary

Another task owns integrated Home/Places rehearsal and governed root
composition on branch `codex/integrated-home-places-rehearsal`.

Do not edit or redesign:

- `travel-agent/backend/root_projection/v2/**`;
- `travel-agent/backend/api/services/root_composition.py`;
- source-contribution or known-to-person producers;
- owner reads;
- Home root UI;
- `travel-app/components/places/PlacesWorkspace.tsx`;
- Places root feed rendering, arbitration, or navigation; or
- shared root-system documents being changed by that task.

Use a neutral candidate card and origin frame in the design lab. The eventual
root integration should consume this handoff after the active task lands.

---

# Part II — Current implementation substrate

## 6. Code that already exists

The entity-resolution implementation is committed on child-repository branch
`codex/entity-shell-resolution` in isolated worktrees:

```text
/Users/feihuyan/travel-workspace/travel-agent-entity
/Users/feihuyan/travel-workspace/travel-app-entity
```

Treat those worktrees as the current implementation reference. Do not assume
the dirty workspace checkouts contain the same code.

### 6.1 Backend

Relevant implementation:

- `backend/api/routes/entities.py`
  - `POST /api/me/entity-resolutions`
  - `GET /api/me/entities/{entity_type}/{entity_id}/presentation`
  - `GET /api/entities/{entity_type}/{entity_id}`
- `backend/core/entity_resolution.py`
- `backend/core/db/entity_resolution_requests.py`
- `backend/core/db/entity_envelope.py`
- `backend/core/models/entity_resolution_api.py`
- `backend/core/models/entity_envelope.py`
- `backend/core/models/places_projection.py`
- `backend/places/source_policy.py`
- `backend/places/materialization.py`
- `backend/places/status_evidence.py`
- `backend/places/refresh_queue.py`

Committed backend slices:

```text
ef484d504 feat(entities): add safe provider resolution boundary
94079c115 test(entities): cover provider resolution replay
5464d45de refactor(places): centralize status evidence claims
```

### 6.2 Mobile

Relevant implementation:

- `data/entityResolution.ts`
- `data/entities.ts`
- `utils/entityRoute.ts`
- `utils/api/interface.ts`
- `utils/api/http.ts`
- `utils/api/types.ts`
- `components/places/EntityObjectPage.tsx`
- `components/places/ObjectPageShell.tsx`
- `components/places/ObjectPageStateShell.tsx`
- `components/places/EntityStatusNotice.tsx`
- `app/site/[siteId].tsx`
- `app/venue/[venueId]/index.tsx`
- `app/accommodation/[accommodationId].tsx`
- `app/experience/[experienceId].tsx`

Committed app slices:

```text
cb3978847 feat(entities): add mobile candidate resolution bridge
e3c7a01c7 chore(api): classify entity resolution aliases
dc6ae346b test(entities): include catalog state in envelope fixtures
```

### 6.3 Wire contract

Provider-only candidate:

```json
{
  "id": "provider-scoped-display-id",
  "canonical_ref": null,
  "external_ref": {
    "provider": "google_places",
    "external_id": "provider-owned-id"
  },
  "entity_type": "venue",
  "name": "Café Aurora"
}
```

Resolution mutation:

```http
POST /api/me/entity-resolutions
X-Idempotency-Key: <stable key for one logical tap/retry>
Content-Type: application/json
```

```json
{
  "external_ref": {
    "provider": "google_places",
    "external_id": "provider-owned-id"
  },
  "entity_type_hint": "venue",
  "source_surface": "places"
}
```

Successful response:

```json
{
  "receipt": {
    "requested_ref": {
      "provider": "google_places",
      "external_id": "provider-owned-id"
    },
    "canonical_ref": { "type": "venue", "id": "4217" },
    "method": "materialized",
    "evidence": {},
    "resolved_at": "2026-09-02T18:00:00Z"
  },
  "canonical_ref": { "type": "venue", "id": "4217" }
}
```

Authenticated object-page response includes:

```text
entity.ref
entity.name
entity.catalog_state: verified | owner_provisional
entity.lineage
entity.lat / entity.lng
entity.photo_urls
entity.brief / dossier_snippet
entity.status { operating, open_now, hours, as_of, sources }
entity.tail
relationship { face, saved, affinity, encounters, active trip }
persisted take, if any
situation, if separately observed
allowed actions
```

### 6.4 Current implementation limits the design must expose

- Existing provider mappings for all supported catalog kinds may resolve.
- A provider miss may materialize only a **venue** shell today.
- A site, accommodation, or experience miss returns a conflict rather than
  guessing or creating the wrong kind.
- Object-page reads perform no provider call and generate no Take.
- Status may be `unknown`; refresh plumbing exists, but coverage is not a
  reason to imply the data has been checked.
- Provider-specific map-surface policy exists in the backend, but the current
  entity envelope does not yet expose a `map_surface` instruction. Record this
  as an implementation gap; do not silently design around it.
- A safe public-share contract for owner-provisional shells is not established.

---

# Part III — Interaction specification

## 7. Transition model

The interaction has one semantic transition and several visual states:

```text
candidate at origin
  ├─ canonical_ref present ───────────────> object page
  └─ external_ref only
       └─ resolve in origin context
            ├─ existing canonical match ─> object page
            ├─ new owner venue shell ────> sparse object page
            ├─ temporary failure ────────> retained candidate + retry
            └─ unsafe/unsupported ───────> retained candidate + honest stop
```

Resolution is not Save, Add to Plan, Follow, Like, or commitment. The tap
creates only the identity necessary to address the object.

## 8. Required interaction states

### 8.1 Canonical candidate

- Tap feedback begins immediately.
- Navigate through `routeForEntity` without a resolution interstitial.
- Preserve origin, selected scope, scroll position, and return destination.
- Do not show “added,” “imported,” or “saved.” Nothing was mutated.

### 8.2 Provider candidate resolving

- Preserve the candidate's visual identity in place.
- Use a quiet progress treatment attached to the tapped candidate or a shared
  element transition; do not replace the whole root with a spinner.
- Prevent accidental duplicate navigation while allowing the same logical
  request to retry with its idempotency key.
- Avoid technical copy such as `Resolving provider entity`.
- Candidate copy may say `Opening…` or remain unchanged with a progress cue.
- If resolution completes very quickly, the intermediate state may be
  visually elided, but the prototype must still include and exercise it.

### 8.3 Existing canonical match

- Navigate to the canonical entity returned by the receipt, not the provider
  identity originally tapped.
- The destination page should not announce that a matching operation occurred
  unless a correction or redirect materially changes what the person selected.
- Back returns to the exact candidate origin.

### 8.4 New owner-private shell

- Open the same entity route and object-page family used by catalog entities.
- Do not open a temporary provider-detail screen that becomes a second object
  model.
- Render only fields actually present.
- Treat shortness as correct. Suppress empty sections rather than filling them.
- Use a calm source/freshness line such as:

  ```text
  Basic place details · source available
  ```

  The final wording must be chosen only after confirming the provider's
  attribution requirements. Do not use this fixture wording as legal copy.
- Do not expose internal labels such as `owner_provisional`, `candidate row`,
  `verification_status`, or `materialized`.
- Do not visually award a “verified” badge to ordinary catalog entities; the
  contrast should come from available evidence, not status theater.

### 8.5 Temporary failure

- Keep the origin candidate visible and selected.
- Explain the failed consequence, not the infrastructure:

  ```text
  Couldn't open this place yet.
  ```

- Offer `Try again`.
- Offer `Open in provider` only when a policy-approved provider URL or deep
  link exists.
- Do not route to a blank or 404 page.
- Do not remove the candidate from the result set.

### 8.6 Unsafe, ambiguous, or unsupported resolution

- Do not make the person choose between opaque duplicate database rows.
- Do not pretend a site is a venue merely because venue materialization exists.
- Retain the candidate and provide a bounded explanation:

  ```text
  Vesper can't safely add this place yet.
  ```

- The design may test a quiet `Open in provider` continuation.
- An engineering handback must distinguish temporary failure from this
  non-retryable state even if production error taxonomy is not yet sufficient.

## 9. Sparse object-page anatomy

The sparse page is still a real object page. It should use the established
shell and taper from identity to useful facts to available actions.

### 9.1 Top chrome

- Back to exact origin.
- Save when the entity is saveable.
- Share hidden or disabled for an owner-private shell until the share contract
  is safe.
- No database-state badge in the top bar.

### 9.2 Identity region

- Entity name in System Sans, following the entity-title register.
- One grounded category line.
- Neighborhood or city when known.
- Honest illustration, licensed provider image, or deliberately media-light
  composition. Never substitute unrelated stock photography.
- If imagery is absent, the empty space should look authored rather than like
  a failed network request.

### 9.3 Current truth

If current status is present:

- show the operational claim;
- show or expose `as_of` and source;
- distinguish permanent closure from `not open now`; and
- do not imply future hours from a point-in-time check.

If current status is absent:

- omit “Open now” and hour claims;
- optionally show `Hours not checked` only if paired with a real explicit
  check action; and
- do not turn `unknown` into `closed`, `probably open`, or an empty hours grid.

The prototype should explore an explicit `Check live details` action as a
future-facing state. The execution report must identify that production wiring
as a separate implementation slice, not pretend the current object-page GET
performs it.

### 9.4 Vesper interpretation

- Persisted Take present: render it with its evidence and caveats.
- Stable dossier snippet present but no Take: render the snippet.
- Neither present: render neither.
- Never generate a Take merely because the page opened.

### 9.5 Personal relationship

- `Saved to your places`, `In your plan`, or a past-trip trace may render only
  from the authenticated relationship projection.
- A newly materialized shell is not automatically saved.
- No inferred affinity such as `You love places like this`.

### 9.6 Facts and actions

- Render a small number of supported facts; suppress nulls.
- Save may be available.
- Add to Plan may appear only through the existing governed preview/commit
  path.
- Ask may carry the canonical entity context into Chat.
- Map/directions must honor provider map-surface policy. Until `map_surface`
  reaches the wire, the design should annotate the decision rather than assume
  Mapbox is always correct.

## 10. Density and hierarchy

The sparse page should not become a set of equally weighted cards.

Use:

```text
identity
  -> current truth, if known
  -> one meaningful interpretation, if authorized
  -> a few grounded facts
  -> available actions
  -> stop
```

Avoid:

- a “Profile completeness” meter;
- a provider-data dashboard;
- a stack of empty `About`, `Hours`, `Reviews`, `Photos`, and `Details`
  sections;
- a bright warning banner simply because the shell is owner-private;
- multiple verification badges;
- a skeleton that resolves into a much shorter page without a calm layout
  transition;
- generating editorial filler; or
- a second provider-shaped detail page beside the canonical Vesper page.

---

# Part IV — Deterministic design fixtures

## 11. Fixture rules

- All names and provider content in this section are synthetic design data.
- Do not import live Google reviews, photos, or business profiles into the
  design project.
- Clearly label the fixtures as synthetic in the design project's Overview.
- Use the same candidate and object identity across every frame of one path.
- Every frame must be resettable and directly addressable for review.

## 12. Fixture A — already canonical museum

```text
Origin: neutral Places/search result harness
Name: Museu do Azulejo
Kind: site · museum
Identity: canonical_ref = site:7
Relationship: not saved · no confirmed visit
Status: open · closes 18:00 · checked 24 minutes ago · provider source
Stable brief: present
Take: absent
Expected path: immediate canonical open
```

Purpose: prove that the ordinary path remains fast and that a museum uses the
same object grammar without venue coercion.

## 13. Fixture B — provider-only venue, successful owner shell

```text
Origin: neutral candidate card
Name: Café Aurora
Kind hint: venue
Provider identity: present
Canonical identity: absent before tap
Provider response latency: 1.2 seconds
Resolution result: materialized owner-private venue shell
Known stable fields: name · café · Williamsburg · approximate coordinates
Status: unknown
Media: unavailable
Brief: absent
Take: absent
Relationship: new · not saved
Expected path: resolving cue -> sparse object page
```

Purpose: test whether a deliberately short page still feels like a useful,
addressable Vesper object.

## 14. Fixture C — provider candidate resolves to existing venue

```text
Origin: neutral candidate card
Name shown by provider: Bar Aurora
Provider identity: present
Canonical identity: absent before tap
Resolution result: existing canonical venue:412, current name Aurora Bar
Status: open now · checked 8 minutes ago
Relationship: saved
Persisted Take: present
Expected path: resolving cue -> canonical page for Aurora Bar
```

Purpose: prove that provider wording does not outrank canonical identity and
that the destination does not look like a newly created shell.

## 15. Fixture D — temporary provider failure

```text
Origin: same Café Aurora candidate
Failure: provider timeout
Candidate remains visible
Actions: Try again · Open in provider when available
Expected path: no navigation
```

Purpose: prove that a tap can fail without losing the candidate, scroll
position, or intent.

## 16. Fixture E — unsupported site materialization

```text
Origin: provider-only museum candidate
Name: Harbor Textile Archive
Kind hint: site
Existing mapping: absent
Current backend result: conflict; site shell materialization unsupported
Actions: Open in provider when available
Expected path: no fake venue, no broken object page
```

Purpose: prove honest refusal and give engineering a clear target for a later
site-admission slice.

## 17. Required prototype frames

At minimum, create:

1. candidate-origin harness with canonical and provider-only rows;
2. provider candidate in resolving state;
3. verified canonical museum object page;
4. sparse owner-private venue object page;
5. existing-match venue object page;
6. explicit live-details check in idle, checking, success, and unavailable
   states;
7. temporary resolution failure at origin;
8. unsupported-resolution stop at origin; and
9. return from each destination to the preserved origin.

The frames must be connected into interactive paths. A collection of static
screens is insufficient.

---

# Part V — Claude Design execution requirements

## 18. Design project

Create a new Claude Design project named exactly:

> **Vesper — Entity Object Handoff Lab**

Do not modify the current Home/Places project. Inspect it only for settled
visual grammar and components if access is available.

The new project should contain, at minimum:

```text
Overview
Contract
Candidate Origin
Resolving Transition
Canonical Object
Sparse Owner Object
Live Detail States
Failure States
Flow Matrix
Findings
Implementation Handoff
```

The project may organize those as files, pages, or addressable sections, but
each must be individually reviewable.

## 19. Reuse requirements

Reuse the current Vesper visual kernel:

- surface, ink, muted, and gold token roles;
- established top-bar and object-page geometry;
- System Sans entity titles;
- serif only for authored Vesper sentences;
- existing state-shell posture;
- existing Save/action affordance family;
- calm motion and reduced-motion behavior; and
- current accessibility expectations.

Do not invent a new brand, icon family, card system, navigation shell, or
provider-themed visual mode.

## 20. Exploration freedom

Claude Design should explore:

- in-card progress versus shared-element transition during resolution;
- how an image-light sparse page can feel deliberate;
- the minimum source/freshness treatment that remains trustworthy;
- whether the explicit live check belongs inline, in the status row, or behind
  a compact disclosure;
- how to suppress unsafe Share without making the page feel disabled;
- how temporary failure differs visually from an unsafe/unsupported stop;
- how an existing canonical match absorbs a provider naming difference; and
- how back-navigation visibly restores the candidate's origin context.

The exploration must preserve the locked authority rules in Part I.

## 21. Accessibility and motion

- Resolution state must have an accessible progress announcement.
- Tap targets must meet the current mobile minimum.
- Progress may not be communicated by motion alone.
- Failure actions must have clear labels and focus order.
- Source/freshness copy must pass contrast requirements.
- Reduced motion should replace shared-element or morph behavior with a calm
  state swap.
- Dynamic type must not hide status, source, or retry actions.

## 22. Design acceptance gates

The design is ready for founder review only when:

- all nine required frames exist;
- every required path is interactive and resettable;
- no path uses a provider ID as a route;
- the owner-private page does not look globally verified;
- the owner-private page also does not look like an alarming moderation state;
- no missing content is fabricated;
- canonical, current, personal, and interpreted information are visually
  distinguishable without permanent section-taxonomy chrome;
- failure preserves the origin candidate;
- back restores exact origin context;
- provider attribution and map-surface gaps are annotated;
- no Home or Places-root redesign appears in the project; and
- the design can be described as one object-page system, not parallel
  provider and Vesper detail products.

---

# Part VI — Claude Code execution prompt

Everything below this heading is addressed directly to the Claude Code session
that executes the handoff.

## 23. Role and deliverable

You are the interaction-design engineer for the bounded entity-opening seam.
Use repository evidence and Claude Design to build the interactive project
specified above.

Return:

1. the durable Claude Design project link and project ID;
2. a file/frame inventory;
3. the interaction paths exercised;
4. screenshots or durable capture references for required states;
5. decisions made and alternatives rejected;
6. unresolved product, provider-policy, and implementation questions;
7. an exact later React Native implementation map; and
8. a workspace execution report.

Do not edit production backend or mobile code during this design task.

## 24. Workspace preflight

Begin in:

```text
/Users/feihuyan/travel-workspace
```

Before design writes:

1. Read root `AGENTS.md` and `CLAUDE.md` completely.
2. Read each child repo's `AGENTS.md` and `CLAUDE.md` before inspecting code.
3. Run `git branch -a` and `git status --short` in the workspace and both
   child repositories.
4. Treat all existing modifications as belonging to another task.
5. Do not stage or commit pre-existing files.
6. Never use `git add .`, `git add -A`, or `git commit -a`.
7. Inspect the implementation worktrees listed in §6 read-only.
8. Do not edit any excluded surface in §5.

If an execution report is written to the repository, use a new isolated
workspace worktree and commit only that report by explicit filename.

## 25. Claude Design preflight

1. Discover the current Claude Design tools and read their complete current
   authoring instructions.
2. Resolve project identities by listing projects; never guess an ID.
3. Inspect the existing Vesper Home/Places design project read-only when
   available.
4. Create the separate project named in §18.
5. Read the latest etag before overwriting any file in the new project.
6. After each meaningful write, re-read the affected file/section and render
   it.
7. Exercise interactions, not just static rendering.
8. Return only durable `claude.ai/design/...` links. Never record temporary
   serving or `claudeusercontent.com` URLs in repository docs.

Current tool instructions win over mechanical MCP advice in this handoff.
The product and authority constraints here continue to govern the output.

## 26. Required reading order

Read completely before authoring:

### Product and authority

1. `docs/decisions/2026-08-08-place-identity-and-provenance.md`
2. `docs/decisions/2026-08-11-entity-envelope.md`
3. `docs/decisions/2026-08-11-entity-status-block.md`
4. `docs/systems/four-root-loop-object-surface.md`
5. `docs/systems/contribution-and-consequence.md`

### Places and object-page design

1. `docs/working/places-consumer-experience-anatomy-2026-08-29.md`
2. `docs/working/places-four-state-design-fixture-brief-2026-08-29.md`
3. `travel-app/docs/design-decisions/places-object-page-shell.md`
4. `travel-app/docs/design-decisions/entity-title-register.md`
5. `travel-app/docs/Design Language.md`

### Current implementation

Read the files in §6 from the isolated entity worktrees. Verify the contract
from code; do not infer it solely from this handoff.

## 27. Prototype evaluation script

Exercise and record each task:

### Task A — immediate canonical open

1. Start at the candidate-origin harness.
2. Tap the canonical museum.
3. Verify no resolution UI appears.
4. Verify the correct site page opens.
5. Return and verify origin continuity.

### Task B — provider venue becomes a sparse object

1. Tap Café Aurora.
2. Hold the resolving state for the deterministic fixture latency.
3. Open the owner-private sparse page.
4. Verify no Save, visit, verification, hours, media, brief, or Take is
   implied beyond fixture evidence.
5. Return and verify origin continuity.

### Task C — provider candidate matches an existing object

1. Tap Bar Aurora.
2. Resolve to canonical Aurora Bar.
3. Verify saved relationship, current status, and persisted Take come from the
   destination object rather than the provider candidate.
4. Verify the provider name mismatch does not create a second page identity.

### Task D — explicit live check

1. Start on the sparse page with unknown status.
2. Invoke the proposed live-check action.
3. Exercise checking, success, and unavailable outcomes.
4. Verify source and freshness remain visible on success.
5. Verify unavailable does not become closed.

### Task E — temporary failure

1. Tap the provider candidate.
2. Trigger timeout.
3. Verify the candidate remains visible.
4. Retry successfully using the same logical action.
5. Verify exactly one destination opens.

### Task F — unsupported kind

1. Tap Harbor Textile Archive.
2. Trigger the unsupported-site result.
3. Verify no venue page opens.
4. Verify provider continuation is understandable when available.

### Task G — accessibility and reduced motion

1. Repeat Tasks B and E with reduced motion.
2. Inspect progress and error announcements.
3. Increase text size and verify source, status, retry, and back remain usable.

## 28. Implementation handback requirements

Map the accepted design to existing code without editing it. At minimum,
identify:

- where root/search candidate renderers should call
  `resolveAndRouteEntityCandidate` after the active root task lands;
- how one logical tap retains its idempotency key across retry;
- where resolving and error state should live so it does not become global
  root state;
- how router origin/return context should be preserved;
- whether `EntityObjectPage` needs a deliberate owner-private treatment;
- how unsafe Share is suppressed;
- how explicit live-detail refresh should be represented in API and data
  layers;
- how provider `map_surface` reaches the mobile contract;
- how temporary versus unsupported resolution errors become typed; and
- which Jest, route, API-contract, and on-device tests certify the result.

Do not recommend wiring candidate taps by parsing `id`,
`canonical_venue_id`, or provider prefixes. The typed refs and resolution
bridge already exist.

## 29. Execution report

Write one report named:

```text
docs/working/claude-design-entity-object-handoff-execution-report-2026-09-XX.md
```

It must contain:

- durable project URL and project ID;
- project/file inventory;
- fixtures implemented;
- evaluation results for Tasks A–G;
- screenshots or capture identifiers;
- accepted interaction decisions;
- rejected alternatives and reasons;
- accessibility findings;
- exact production gaps;
- no-backfill confirmation;
- no-overlap confirmation; and
- founder decisions still required.

## 30. Stop conditions

Stop and report rather than guessing if:

- Claude Design access is unavailable;
- the source Home/Places project cannot be identified safely;
- provider attribution or map requirements would be invented;
- the implementation worktree no longer matches the listed contract;
- the active Strategy task has begun editing the same object-page surfaces;
- a production code change appears necessary to complete the design artifact;
  or
- the work would require a backfill.

---

# Part VII — Founder review questions

The design should make these decisions concrete rather than answering them in
prose alone:

1. Should the resolving cue live entirely on the tapped candidate, or begin a
   shared transition into the page shell?
2. What is the least alarming way to communicate that a sparse object has only
   basic, source-backed details?
3. Should unknown current status be silent, or should the page offer an
   explicit `Check live details` action?
4. Should owner-private shells have no Share action, or a separate private
   handoff that never creates a public entity URL?
5. How should a provider naming difference be revealed, if at all, after
   canonical matching?
6. When provider map policy requires a provider surface, should Vesper deep
   link directly or show a compact chooser?
7. Is unsupported site materialization acceptable as a bounded launch
   limitation, or must site shell admission land before root integration?

## Compact standard

The work succeeds when a person can tap something Vesper found, arrive at one
real Vesper object, understand exactly as much as the evidence supports, and
continue without ever needing to know that identity resolution, provider
policy, or provisional catalog state exists underneath.
