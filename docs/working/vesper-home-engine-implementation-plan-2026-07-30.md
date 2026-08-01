---
doc_type: working
status: active
owner: founder / product / backend / frontend
created: 2026-07-30
expires: 2026-08-29
why_new: The Vesper Home workbench and its four list kinds are designed, and the sessions-only React Native surface exists, but there is no end-to-end implementation plan for the server-owned envelope, two-wave voice, producer rollout, frontend cutover, privacy boundary, observability, dogfood data, or device evidence. This document owns that implementation sequence.
promotes_to:
  - travel-agent/backend/home/vesper_workbench/FEATURE.md
  - travel-app/docs/surfaces/vesper-home/contract.md
supersedes: []
depends_on:
  - docs/working/vesper-home-workbench-2026-07-28.md
  - docs/working/vesper-home-list-kinds-scope-2026-07-29.md
  - docs/working/home-surfaces-program-2026-07-28.md
source_of_truth_for:
  - vesper-home-engine-implementation-order
  - vesper-home-envelope-contract
  - vesper-home-producer-rollout
  - vesper-home-two-wave-delivery
---

# Vesper Home — engine implementation plan

> **The design is already a system. This plan makes the code one.**
>
> Vesper Home has four slots: `voice · facts[2] · seam · list`.
> The server owns the truth and the selection. The app owns the composition,
> interaction feel, and deliberately unwritten potential around it.

## Outcome

Vesper Home becomes one coherent personal read model rather than a client-side
join over trips, weather, conversation history, and a legacy card queue.

At the end of this program:

- one cheap backend response describes the exact facts, seam, and one selected
  list kind the page may show;
- the page renders immediately from a deterministic read line;
- generated Vesper voice arrives independently and can never hold the page
  hostage;
- sessions, season, route, and here all implement the same eligibility and
  edge contract without becoming a mixed feed;
- the app no longer re-ranks or reinterprets backend truth;
- private and group-scoped session material remains permission-scoped and
  cannot leak into a group write;
- every meaningful state is proved through static tests, a real-backend
  canary, and reviewed device captures.

## Product laws

These are implementation constraints, not art-direction suggestions.

1. **Trips owns objects; Vesper owns sessions.** An urgent item on Vesper is
   a door into Trips, never a place to vote, approve, settle, or book.
2. **One list band, one kind.** `sessions | season | route | here`; never a
   mixed list and never a second band.
3. **Grounded or absent.** No placeholder weather, inferred airport, invented
   event, synthetic deadline, or stale fare presented as current.
4. **Never backfill across kinds.** One eligible row is a valid one-row list.
5. **The well has a reason.** It renders exactly when `seam != null` or the
   selected list has at least one item. Facts alone never create it.
6. **Say it once.** A fact cannot be repeated in the context eyebrow, fact
   strip, seam, and read line as four separate claims.
7. **One envelope, two waves.** Facts, seam, list, and deterministic read are
   Wave 1. Generated voice is Wave 2.
8. **Voice reads the envelope.** It does not perform a parallel trip,
   conversation, weather, or memory query.
9. **The app does not decide truth.** It may derive layout from slot presence,
   but it does not choose a list kind, infer urgency, or decide a session is
   open.
10. **No backend “screen state” enum.** `live/home/quiet/cold` remain useful
    fixture and presentation names, not a second source of product truth.

## Ratified planning decisions

These decisions unblock implementation and should be changed only by editing
this plan explicitly.

| Decision | Ruling |
|---|---|
| Endpoint ownership | Add a dedicated Vesper Workbench route under `/api/concierge/home/workbench`; do not overload the Trips-owned card queue DTO. |
| Migration shape | Additive. Keep `/api/concierge/home` and `/trips-stack` intact while Vesper moves off the legacy feed. |
| List precedence V1 | Eligible sessions win the band. Revisit only after a trustworthy session edge exists. |
| World build order | `season → route → here`. Sessions ship before all three. |
| First world source | A reviewed, versioned seasonal-window catalog; no new vendor and no runtime generation. |
| Route origin | No inference from a display string. Route stays dark until a canonical origin-airport contract exists. |
| Here launch | Editorial-first, one-city pilot; expand only after end-date coverage is measured. |
| World-row interaction | Informational in the first producer release. Do not invent a tap destination or silently seed a chat. |
| Native voice | Tap/hold microphone behavior is a separate device/native-audio program and does not block the Home engine. |
| Generated read | Existing LLM infrastructure may decorate the deterministic floor, but prompt changes require their normal explicit review. |

## The target data flow

```text
authorized user
      │
      ▼
Vesper Workbench assembler
  ├─ situation/context
  ├─ eligible sessions
  ├─ grounded facts
  ├─ urgent seam projection
  └─ eligible world windows
      │
      ▼
selector + consistency pass
  ├─ at most 2 facts
  ├─ at most 1 seam
  ├─ exactly 0 or 1 list kind
  └─ deterministic read line
      │
      ├──────── Wave 1 ────────► React Native composition
      │
      └─ normalized grounding
             │
             └──── Wave 2 ─────► optional generated read line
```

The assembler is a read model. It introduces no proposal, booking, itinerary,
expense, or conversation writer.

## Wire contract

### Wave 1

`GET /api/concierge/home/workbench`

Ambient readings may be supplied as today, but every accepted reading carries
its source and freshness. The route authenticates the current user; it does not
accept an arbitrary user id.

```text
VesperWorkbenchEnvelope
  schema_version: 1
  envelope_id: opaque, user-bound snapshot id
  generated_at: datetime
  context:
    label: display-ready situated eyebrow
    situation: live_trip | upcoming_trip | home | away | unknown
    local_date: date
    place_id?: canonical id
    trip_id?: authorized trip id
  read:
    floor: deterministic, display-ready line
    max_chars: 96
    voice_token?: opaque, short-lived Wave-2 token
  facts: WorkbenchFact[0..2]
  seam?: WorkbenchSeam
  list?: WorkbenchList
  coverage:
    producer_statuses
    omitted_reason?: no_eligible_material | source_unavailable | stale_only
```

`coverage` is diagnostic truth for the client and telemetry. It must not become
visible debug copy in production.

### Facts

Facts are display-ready but retain typed provenance:

```text
WorkbenchFact
  id
  kind: weather | live_trip | next_trip | edge | season
  label
  value
  detail?
  source_as_of?
```

Rules:

- maximum two;
- unknown is omitted;
- the second fact follows the selected list, not a separate client rule;
- a seam-changing event is applied before facts are finalized, so a cancelled
  booking cannot still appear as an affirmative fact above its breakage seam;
- the app never fabricates a substitute fact.

### Seam

The seam uses a deliberately slim DTO rather than `ConciergeHomeCard`:

```text
WorkbenchSeam
  id
  kind: deadline | breakage
  trip_id
  kicker
  title
  detail?
  edge_at?
  proof?: depletion | struck_fact
```

The only client action is the fixed behavior `Open in Trips`. No arbitrary
action payload, decision mutation, or card CTA crosses this boundary.

### List

```text
WorkbenchList
  kind: sessions | season | route | here
  cap
  count
  edge_at?: nearest set edge
  items: discriminated item union [1..3]
```

Shared item fields are `id`, `kind`, `title`, and source/freshness metadata.
Kind-specific payloads remain typed:

- **session:** conversation id, authorized scope, trip id, state line, stamp,
  unread, activity, participant summaries;
- **season:** place scope, window label, start/end, edge label;
- **route:** canonical origin/destination, travel window, observed fare,
  currency, observed-at, search-window edge;
- **here:** canonical place scope, dated window, source, start/end, edge label.

Avoid one giant optional-field object. Use a discriminated Pydantic union so
generated TypeScript preserves the actual row contract.

### Wave 2

`POST /api/concierge/home/workbench/voice`

Body: `{ voice_token }`

The opaque token refers to normalized, server-stored grounding for the exact
Wave-1 envelope. It is user-bound, short-lived, and unusable by another user.
The endpoint never trusts client-supplied titles, facts, or prompt text.

```text
VesperWorkbenchVoice
  envelope_id
  status: composed | deterministic | unavailable
  text
  generated_at
```

The app has already rendered `read.floor` before this request begins. On
timeout, cache miss, disabled surface, invalid token, or generation failure,
the floor remains on screen. A late result replaces only the read line and
must not reorganize the page.

## Backend architecture

Create a new bounded package:

```text
backend/home/vesper_workbench/
  FEATURE.md
  models.py
  assemble.py
  context.py
  facts.py
  seam.py
  selector.py
  voice.py
  producers/
    sessions.py
    season.py
    route.py
    here.py
  data/
    season_windows.yaml
```

The package may consume shared repositories and the existing
`concierge_feed` result. It must not import from agent subsystems or create a
second writer for any canonical entity.

`backend/api/routes/vesper_home.py` owns transport only: request validation,
auth, time budgets, failure isolation, and response serialization.

### Reuse boundary

- Reuse the existing concierge ranking output to project one eligible urgent
  seam; do not independently re-rank the same cards.
- Do not expose the full legacy card DTO to Vesper.
- Reuse canonical trip and conversation repositories rather than issuing HTTP
  calls from one backend route to another.
- Keep the old concierge feed alive for Trips. Vesper ceases to be its visual
  consumer after the cutover.

## Producer contracts

Every producer returns candidates plus status. It does not choose the winning
kind and it does not write display fallback data.

```text
ProducerResult[T]
  items: T[]
  status: ready | unavailable | stale | disabled
  as_of?
  reason_code?
```

A producer failure is isolated. One failed source cannot 500 the workbench.

### Sessions

Eligibility V1 is a named predicate, not `status != closed`:

- actor is currently authorized to read the conversation;
- conversation and linked trip are not archived/closed in a way that makes the
  session historical;
- at least one honest open signal exists: unread work, current goal, open
  question, active drafting state, or a fresh active workflow;
- dormant history with no open signal is not eligible.

The producer returns at most the ranker's top three eligible sessions.
Sorting is deterministic and clock-injected for tests.

Session richness lands in two cuts:

1. **V1, no migration:** existing title, scope, trip, unread, intent phase,
   current goal, session status, activity time.
2. **Truthful edge:** participant display summaries; a partial workflow index;
   and a canonical session-edge field (`user | vesper | none`, reason, since)
   updated at the existing turn/workflow lifecycle boundaries.

Until cut 2 exists, the UI may say `open`, `waiting`, or a relative timestamp
only where the existing fields prove it. It must not claim “Vesper is working”
from a stale drafting phase.

Group rows may expose only membership-authorized room metadata. Generated Home
voice must not quote raw group messages, raw private messages, private
constraints, or participant-specific memories. Opening a group row must route
to that exact group conversation, never a personal side chat.

### Season

Start with a reviewed repository-owned catalog, not generated prose:

```text
id
title
place_scope / hemisphere scope
start_date
end_date
edge_label
source_note
reviewed_at
expires_at
```

Catalog validation rejects:

- missing or elapsed edges;
- ambiguous geography;
- impossible date ranges;
- duplicate ids;
- rows past editorial expiry;
- claims whose source note is empty.

The runtime loader is bounded and cached. A later editorial database is a
separate decision; it is not required to prove the producer.

### Route

Route is dark until two gates pass:

1. a canonical origin-airport source exists; `users.home_city` display text is
   not sufficient and read-time geocoding is forbidden;
2. explicit approval is given for the new Amadeus Flight Inspiration Search
   integration.

The producer then:

- queries once per canonical origin and search day;
- caches across users;
- stores observed-at and the searched travel window;
- omits stale results;
- never describes a search-window end as a fare expiry;
- returns no row when origin confidence is insufficient.

### Here

Begin with one city and editorial windows carrying real end dates. New York is
the recommended dogfood pilot because it exercises the Home case directly.

The first producer is not a generic events search. It admits only:

- canonical city identity;
- approved source;
- start and reliable end;
- current, non-expired review;
- a destination-neutral title that does not imply ticket availability.

Vendor evaluation comes after measuring how many candidate rows have usable end
dates. A ticketing API should not be integrated merely to increase raw event
count.

## Selection and consistency

The selector is pure and clock-injected.

1. If eligible sessions exist, select `sessions`, preserving their deterministic
   rank order, maximum three.
2. Otherwise remove elapsed, stale, unavailable, and disabled world candidates.
3. Sort world candidates by edge ascending.
4. The nearest candidate's kind wins.
5. Return up to three candidates of that kind only.
6. Never fill remaining slots from another kind.
7. Resolve the second fact from the selected list.
8. Project at most one seam.
9. Run the “say it once” and seam/fact consistency pass.
10. Derive the floor read and context label from the resulting envelope.

Property tests should prove one-kind output, maximum sizes, no elapsed rows,
stable ordering, no backfill, and identical results for identical inputs and
clock.

## Frontend architecture

Add:

```text
data/vesperHome.ts
components/vesper-workbench/
  VesperWorkbench.tsx
  WorkbenchWell.tsx
  WorkbenchList.tsx
  SessionRow.tsx
  WorldWindowRow.tsx
utils/vesperWorkbenchPresentation.ts
```

Use semantic extraction, not component confetti. Facts and seam may remain
inside `WorkbenchWell` if splitting them adds no independent behavior.

The screen consumes one generated API type. It does not call
`useConversationHistory`, `useTripsList`, ambient weather, and
`useConciergeHomeFeed` to reconstruct the same surface independently.
Conversation history remains available to the History screen.

### Component ownership

| Component | Owns |
|---|---|
| Root header | situated label plus Search / History / You capsule |
| Read block | floor-to-generated text transition; typography only |
| Well | exact `seam || list.items` visibility rule and sunken material |
| Fact strip | zero to two server-authored facts |
| Seam | deadline/breakage proof and fixed Trips door |
| List | cap/count and one discriminated row family |
| Session row | scope, title, state, participant mark, correct conversation route |
| World row | dated information only in V1; no invented action |
| Ghost | client-owned potential copy selected from situation + well presence |
| Composer | shared entry control, attachment, text, dictation/voice affordances |
| Floating navigation | overlay geometry and material relationship with composer |

The current `live/home/quiet/cold` names remain fixture helpers. Runtime layout
is derived:

```text
hasWell = seam != null || list?.items.length > 0
ghostFamily = situation + hasWell
```

No `state` field from the server gates content.

### Loading, refresh, and failure

- Header, ghost, and composer remain usable during every read state.
- A cached envelope may remain visible during refresh if its freshness limits
  have not elapsed.
- With no cache and a Wave-1 failure, render the honest no-well fallback and a
  retry affordance that does not resemble content.
- Wave-2 loading never gets a spinner and never hides the floor.
- Pull-to-refresh refreshes Wave 1 and invalidates the associated voice token.
- Conversation completion, unread change, and relevant trip/feed changes
  invalidate the envelope. Polling or app-focus refresh is acceptable first;
  stale “working” claims are not.
- Unsupported producer coverage never shows a plausible mock row.

### Composer and navigation

The visual polish already established around the shared material, aligned
widths, root-header context, and floating inset is the baseline. The engine
cutover must not rewrite it.

The Home composer continues to create or enter a personal session. Lazy trip
promotion remains explicit. Group selection is never inferred from whatever
group row happens to be visible.

Tap dictation and hold-to-converse remain separately gated:

- no microphone call before the iOS permission posture and native dependency
  are proven;
- hold conversation V1 excludes group threads;
- accessible alternate actions are mandatory;
- spoken-memory writes require their own visible/reversible contract.

## Caching and freshness

| Material | Initial policy |
|---|---|
| Workbench envelope | user-scoped, short client cache; refresh on focus/pull and domain invalidation |
| Voice grounding/token | user-bound, approximately 10 minutes; single envelope only |
| Generated voice | fingerprinted by normalized envelope; reuse while envelope fingerprint matches |
| Session rows | no shared cache across users |
| Season catalog | process cache, invalidated by deploy/catalog version |
| Route | shared by canonical origin + search day; short enough to suppress stale observed fares |
| Here | cache by city/catalog version; never beyond editorial expiry |

Do not cache failures as successful empty coverage. Failure and honest empty are
distinct statuses.

## Privacy and authorization

This is a personal root surface even when it contains a group-session row.

- Every session, trip, and seam is membership-checked for the actor.
- Participant summaries are batched and limited to authorized room members.
- Raw transcript text and private constraints are excluded from voice
  grounding.
- Home voice is never written into a group room.
- Opening a session preserves its canonical conversation id and scope.
- Telemetry records ids, kinds, counts, latencies, and reason codes—not titles,
  message previews, constraints, or generated prose.
- An authorization change invalidates the envelope; cached material may not
  outlive access.

The privacy test matrix includes a user who belongs to the trip but not the
conversation, a removed trip member, a personal side chat, and a group room
whose trip contains another member's private constraint.

## Observability

Emit structured, content-free events:

- total Wave-1 latency;
- per-producer latency, status, candidate count, and omission reason;
- selected kind and selected count;
- well/no-well rate;
- no-coverage reason;
- envelope cache/freshness outcome;
- Wave-2 requested/composed/deterministic/unavailable;
- voice cache hit and latency;
- seam impression and Trips-door open;
- session-row open and world-row impression;
- envelope-to-render schema/version mismatch.

Dashboards should answer:

1. How often is each list kind eligible and selected?
2. How often do sessions suppress the nearest world edge?
3. What fraction of launches have no well?
4. Which producer fails or goes stale?
5. Does generated voice arrive soon enough to be worth the transition?
6. How often does the user open the selected work?

## Dogfood and fixture strategy

Mocks prove composition; dogfood proves truth. Never confuse them.

Maintain deterministic mock fixtures for:

- live + session + deadline seam;
- home + three sessions;
- quiet + one session;
- quiet with no well;
- cold with no well;
- cold/home + one season row;
- route three-row and stale-route omission;
- here one-row quiet week;
- breakage seam with corrected fact strip;
- Wave-1 failure with composer available;
- Wave-2 timeout retaining the floor;
- group row routing and privacy.

Real dogfood uses real conversations, trips, holds, weather, and approved
catalog rows. It does not insert fabricated production-looking route fares or
events. Add a diagnostics view or test-only forced state only where it is
clearly dev-scoped and cannot ship as live truth.

## Implementation phases

### Execution status

**Started 2026-07-30 — Phases 0–5 implemented and device-proven at the local
implementation layer.**

- Added the additive Wave-1 models and authenticated
  `/api/concierge/home/workbench` route.
- Added the bounded `backend/home/vesper_workbench/` package with session
  eligibility, one-kind selection, grounded context/facts, slim urgent seam,
  deterministic read, producer status, and failure isolation.
- Season, route, and here remain explicitly disabled.
- Focused compatibility evidence: 56 passed, 9 intentionally skipped across
  the new engine, existing Concierge Home route, and Trips projection suites.
- Read-only local Postgres canaries proved both honest no-material output and a
  permission-scoped one-row group-session envelope without printing personal
  content.
- Runtime OpenAPI registration is proved. The complete workspace snapshot,
  active-mobile projection, and generated TypeScript contract are synchronized
  and reproduce exactly through `generate-api-types:check`.
- Vesper Home now consumes the workbench envelope through `data/vesperHome.ts`;
  the screen no longer joins trips, conversation history, ambient facts, and
  the legacy Concierge Home feed to choose its own truth.
- Mock mode projects the same sessions-first envelope, while exact scenario
  envelopes remain available for future world-kind fixtures.
- The workbench renders the discriminated list union, keeps world rows
  informational, preserves canonical personal/group routing, and treats the
  slim seam as a fixed door into Trips.
- Focused frontend evidence: TypeScript clean; 23 Vesper model, component, and
  screen tests pass; scenario/design-reference registries pass.
- The registered iPhone 16 Pro / iOS 18.2 matrix now passes 6/6 for live, home,
  quiet, cold, seam-only, and keyboard-open states. The default flow carries an
  explicit frozen clock and the workbench resets to the top when its situated
  context changes, so captures cannot inherit a stale scroll offset.
- The device routing flow proves personal rows open private Vesper chat and
  group rows open the trip group chat. The seam-only fixture exposes no Vote or
  Approve control and hands off to the Trips-owned stack.
- Keyboard evidence found and closed a real defect: the absolute composer was
  hidden by the software keyboard. Vesper Home now participates in keyboard
  avoidance, and the composer drops the covered floating-nav inset while the
  keyboard is visible. The final capture retains the typed two-line draft,
  caret, attachment affordance, and send control immediately above the
  keyboard.
- A local real-backend canary passes against canonical dogfood Postgres after
  migrating the database to the repository's single Alembic head. The iOS
  simulator fetched `/api/concierge/home/workbench`, rendered the grounded
  workbench, and kept the composer available.
- The structured six-state visual verdict validates as `pass` with no dimension
  or gate regressions and is committed at
  `travel-app/docs/surfaces/vesper-home/verdicts/vesper-home-after.json`.
  The local-backend receipt and captures live under
  `travel-app/docs/audits/vesper-home-engine-canary/2026-07-30/`.
- Phase 3 is closed at the stated implementation layer. This is
  `SKIP_AUTH=true` simulator evidence, not Clerk-authenticated, EAS,
  physical-device, or provider-production certification.
- Wave 1 now stores a normalized, display-authorized grounding snapshot and
  returns only a short-lived, actor-bound token. Wave 2 is the authenticated
  `/api/concierge/home/workbench/voice` endpoint and accepts no client-authored
  facts, titles, or prompt text.
- The grounding projection excludes canonical ids, participant records,
  diagnostics, transcripts, and personal constraints. Its full material
  content fingerprints generated reads; a hard facts scan rejects unsourced
  dates, numbers, and prices even if the provider ignores its prompt.
- Redis is authoritative whenever configured. Worker-local entries cannot
  revive an evicted token or an envelope superseded on another worker; the
  bounded local cache remains a development fallback when Redis is absent.
- The app renders `read.floor` first and requests voice independently. It
  accepts only a matching `composed` result and swaps text inside a bounded
  three-line region, so deterministic, stale, failed, or late results cannot
  reorganize the page.
- A direct paid-provider canary and a real local Wave-1-to-Wave-2 HTTP canary
  both produced grounded reads. The HTTP canary returned Wave 1 HTTP 200,
  Wave 2 `composed`, and the same envelope id.
- The registered iPhone 16 Pro / iOS 18.2 success and failure flows pass. The
  success capture preserves geometry from floor to composed voice; the failure
  fixture retains the honest floor, composer, and no-well state.
- Phase 4 focused evidence: 55 backend tests and 36 frontend tests pass;
  TypeScript, OpenAPI synchronization, contract check, and API contract audit
  pass. Device evidence is recorded under
  `travel-app/docs/audits/vesper-home-engine-canary/2026-07-30/phase4/`.
- Phase 4 is closed at the local implementation/device layer. Provider
  generation was exercised directly and through the local backend, while the
  repeatable device captures use explicit mocks. Clerk-authenticated,
  deployed multi-worker Redis, EAS, physical-device, and provider-production
  reliability remain outside this receipt.
- Conversations now persist a canonical `user | vesper | none` session edge,
  reason, and since timestamp. Message and durable-workflow lifecycle
  boundaries update that edge transactionally; same-owner refreshes preserve
  `since`, active workflows keep ownership with Vesper, terminal results hand
  ownership to the user, and archive/close clears it.
- A partial active-workflow index supports conversation-scoped edge refresh
  before Home queries active work. The frontend no longer derives
  `vesper_working` or `your_turn` from idle/goals/timestamps, and invalidates
  the Workbench at relevant message/workflow boundaries plus on focus.
- Group rows receive one batched, permission-scoped participant display
  projection. Trip-linked groups require current trip membership for viewer
  and displayed participant; personal rows render no facepile. Participant
  records remain excluded from voice grounding.
- Phase 5 focused evidence: 72 backend tests and 41 frontend tests pass;
  TypeScript, targeted ESLint, OpenAPI synchronization, contract check, and
  API contract audit pass. Real-Postgres tests prove participant authorization
  and workflow edge transitions, and the migrated database reports exactly one
  Alembic head.
- Registered iPhone 16 Pro / iOS 18.2 canaries pass for the canonical Vesper
  working marker plus authorized group facepile, and for a personal session
  with neither marker nor facepile. Captures and the detailed boundary are
  recorded under
  `travel-app/docs/audits/vesper-home-engine-canary/2026-07-30/phase5/`.
- Sessions continue to win the list band. Phase 5 deliberately did not change
  precedence without measured suppression telemetry.
- Phase 5 is closed at the local implementation/device layer. The repeatable
  device captures use explicit mock personas; backend lifecycle and privacy
  behavior are proved separately against local Postgres. This is not
  Clerk-authenticated, EAS, physical-device, or deployed multi-worker
  certification.

### Program sizing

These are sequencing ranges, not commitments; provider approval and editorial
authoring dominate the uncertainty.

| Scope | Rough size |
|---|---|
| Phases 0–3: real sessions engine on device | 1–2 engineering weeks |
| Phases 4–5: generated voice plus truthful session edge/facepile | 1–2 engineering weeks |
| Phase 6: season producer plus initial reviewed catalog | 3–6 engineering days plus authoring |
| Phase 7: route producer after origin/provider gates | 1–2 engineering weeks |
| Phase 8: one-city here pilot | 1–2 engineering weeks plus editorial sourcing |
| Phase 9: consolidation | 2–4 engineering days |

The critical product milestone is Phase 3. It replaces the stitched client
surface with a real engine without waiting for speculative world coverage.
Phases 6–8 expand what the engine can say; they are not prerequisites for the
engine being useful.

### Phase 0 — baseline and contract

- Ratify this plan.
- Record the current sessions-only device screenshots as the visual baseline.
- Measure current Home request count, first useful paint, and no-well rate.
- Add the Wave-1 and Wave-2 schemas plus route skeletons.
- Add `FEATURE.md` before the backend package crosses the repository size gate.

**Exit:** OpenAPI exposes the additive contracts; no app behavior changes.

### Phase 1 — pure engine and sessions envelope

- Implement context, session producer V1, selector, fact resolver, seam
  projection, consistency pass, and deterministic read.
- Reuse existing repositories and ranked feed output.
- Add producer isolation and diagnostics.
- Add authorization, privacy, clock, timezone, stale-data, and property tests.
- Add a real-Postgres assembler canary.

**Exit:** Wave 1 returns a truthful sessions envelope for live, home, quiet,
cold, seam-only, and no-material cases. Backend evidence only; no visual
completion claim.

### Phase 2 — frontend cutover

- Sync OpenAPI through the workspace script.
- Add `data/vesperHome.ts` and mock parity.
- Generalize `VesperWorkbench` from hardcoded threads to one typed list.
- Preserve current header/composer/navigation geometry.
- Remove client-side trip/session/feed selection from the Home screen.
- Keep legacy hooks for their other consumers.
- Add loading, cached refresh, error, and unsupported-version behavior.

**Exit:** focused Jest, TypeScript, API-boundary checks, mock parity, and the
registered Vesper Home surface checks pass.

### Phase 3 — sessions device gate

- Run the registered live/home/quiet/cold matrix.
- Verify group versus personal routing.
- Verify seam-only rendering and Trips handoff.
- Verify composer reachability with keyboard and floating navigation.
- Run a real-backend dogfood capture.
- Commit the structured visual verdict.

**Exit:** sessions engine is device-proven. Only now may the sessions phase be
described as complete.

### Phase 4 — Wave-2 generated voice

- Persist normalized envelope grounding in the shared cache.
- Add user-bound voice tokens and the Wave-2 endpoint.
- Adapt the existing Home voice composer to accept only normalized envelope
  grounding.
- Fingerprint cache entries by the full material envelope.
- Implement floor-to-voice transition without reflow.
- Test timeout, disabled, cache eviction, cross-user token, prompt-injection
  text, and stale-envelope cases.

**Exit:** the page always paints the floor first; a real-provider canary and
device run prove success and failure paths.

### Phase 5 — truthful session edge and facepile

- Batch participant display summaries.
- Define and persist the canonical session edge at existing turn/workflow
  lifecycle boundaries.
- Add the partial workflow index before querying active work by conversation.
- Invalidate Home when the edge changes.
- Replace inference-based `running/waiting` with the canonical activity value.
- Revisit—but do not automatically change—sessions-always-win using measured
  suppression telemetry.

**Exit:** no stale “working” label in the canary matrix; migration tests show a
single Alembic head; participant/privacy device cases pass.

### Phase 6 — season producer

- Author and review the initial seasonal catalog.
- Add schema/catalog validation and expiry tooling.
- Match rows to canonical place/hemisphere context.
- Enable the world selector behind sessions precedence.
- Add one-row, three-row, elapsed, ambiguous-place, and no-coverage tests.
- Re-shoot the realistic cold/home launch against season rather than the
  design's unavailable `here` specimen.

**Exit:** season is real, reviewable, and device-proven; no generated or
hand-waved production rows.

### Phase 7 — route discovery gate and producer

- Decide and implement the canonical origin-airport contract.
- Run a provider spike against Flight Inspiration Search.
- Obtain explicit approval for the external API addition.
- Implement shared origin/day cache, freshness, rate/cost telemetry, and
  fail-absent behavior.
- Add real-provider canaries without asserting fare expiry.

**Exit:** route remains disabled until origin truth, provider behavior, cost,
and stale suppression all pass.

### Phase 8 — here pilot

- Measure end-date coverage for the candidate source set.
- Author the New York editorial pilot with approvals and expiry.
- Add the here producer and canonical city matching.
- Prove one-row quiet weeks and no-coverage behavior.
- Evaluate vendor expansion only after the pilot data identifies the actual
  coverage gap.

**Exit:** one city is honest and device-proven. Do not call the kind global.

### Phase 9 — consolidation and promotion

- Remove Vesper Home's dependency on legacy concierge feed and conversation
  list hooks after rollback confidence.
- Retain the shared feed for Trips and other actual consumers.
- Delete dead client selection helpers and stale mock-only producer code.
- Promote the settled backend architecture to `FEATURE.md`.
- Update the Vesper Home operating contract and design comparisons.
- Record remaining native voice work as its own program.

**Exit:** static trace, mock walk, backend canary, and live device evidence are
all named and current; no “done” claim rests on backend tests alone.

## Test matrix

### Backend

- model validation and copy budgets;
- deterministic selector/property tests;
- session authorization and composite-open predicate;
- group/private privacy fixtures;
- seam slim-projection and fixed destination;
- fact/seam contradiction prevention;
- timezone boundaries and injected clock;
- producer exception isolation;
- stale versus empty distinction;
- voice token ownership, expiry, cache, and fallback;
- season catalog validation;
- route freshness/cost/provider parsing;
- here approval/end-date eligibility;
- OpenAPI snapshot and app projection.

### Frontend

- envelope version decoding;
- exact well visibility rule;
- one list renderer and no mixed kinds;
- session routing by canonical conversation scope;
- world rows non-interactive in V1;
- seam opens Trips only;
- floor survives Wave-2 loading/failure;
- no claim-bearing skeletons;
- cache refresh and Wave-1 failure;
- keyboard/composer/nav clearance;
- Dynamic Type, VoiceOver labels, reduced motion, and contrast;
- mock API parity.

### Device evidence

Each producer needs:

1. static trace;
2. deterministic mock walk;
3. real-backend canary;
4. reviewed iPhone capture;
5. structured Vesper Home verdict.

World kinds also need a source/freshness receipt in the run manifest.

## Rollout and rollback

1. Deploy additive backend routes dark to the app.
2. Run server-side dogfood and contract canaries.
3. Ship an app build capable of the new endpoint with the existing screen as
   rollback.
4. Enable engine rendering for internal dogfood.
5. Compare selected-kind/no-well telemetry with the old client assembly.
6. Expand only after privacy, stale-data, and device gates pass.
7. Roll back by switching the app consumer, not by deleting the new data or
   changing the shared Trips feed.

Do not maintain two active selection algorithms longer than the rollback
window. Once the engine is accepted, the client-side selector is deleted.

## Explicit non-goals

- rebuilding the Trips queue or Deck;
- creating a second cross-trip card ranker;
- resolving decisions inside Vesper;
- a generic news/events feed;
- personalized world ranking beyond the stated edge rule;
- inferring location from IP, locale, saved clusters, or display copy;
- fabricating dogfood route/here rows;
- shipping tap/hold voice before native audio and accessibility proof;
- changing conversation-to-trip promotion from lazy to eager;
- building an editorial admin before the versioned catalog proves the model.

## Risks and falsifiers

Reconsider the model if:

- the composite session-open predicate makes an old session suppress useful
  world material indefinitely;
- the generated line arrives late enough to feel like text changing under the
  traveler;
- the season catalog cannot sustain useful coverage without becoming an
  editorial treadmill;
- route lacks a trustworthy origin often enough to make coverage misleading;
- `here` sources do not carry reliable end dates;
- world rows feel inert and user testing consistently expects a destination;
- a group row's scope is ambiguous or opens the wrong room;
- the backend envelope makes the first useful paint slower than the current
  stitched screen;
- the no-well state reads as unfinished on device.

## First executable slice

The next implementation slice is deliberately narrow:

1. add the Wave-1 Pydantic models;
2. build the pure selector and deterministic floor;
3. implement the sessions V1 producer;
4. project the existing urgent seam into the slim DTO;
5. assemble facts from the same snapshot;
6. expose the authenticated endpoint;
7. prove it with unit, privacy, contract, and real-Postgres tests.

No frontend cutover, generated voice, migration, vendor, or seasonal catalog is
needed in that first slice.
