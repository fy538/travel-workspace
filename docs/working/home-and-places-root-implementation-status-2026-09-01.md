---
doc_type: working
status: active
owner: founder / backend / frontend
created: 2026-09-01
last_verified: 2026-09-02
expires: 2026-10-01
why_new: Record the concrete Home/Places implementation outcome without implying that the v2 roots are production-ready. This status sheet is the handoff from architecture freeze through runtime Home portfolio activation, Places convergence, and typed continuation rehearsal.
source_of_truth_for:
  - Home and Places implementation status, promotion boundary, and known deferred work
depends_on:
  - docs/working/home-and-places-root-implementation-program-2026-08-31.md
  - docs/working/home-and-places-root-consumer-graph-2026-09-01.md
---

# Home and Places — implementation status

## Completed

### Package 0 — architecture freeze and characterization

- The build manifest no longer makes the old `concierge_feed` numeric rank
  output the permanent Home/Places hierarchy. Its inputs and characterization
  cases remain reusable migration evidence.
- The Home and Places bounded unit unions are closed in
  `backend/core/models/root_projection_v2.py`.
- `RootCandidate`, typed semantic payloads, owner references, source
  references, grant references, lifecycle/expiry, lead/support medium, and
  owner-capability destinations are strict and immutable.
- The v2 envelope has explicit root identity, projection revision, source
  revisions, and independently reported degradations. It contains no client
  component or route strings.
- The consumer graph and deletion gates are recorded in the companion graph
  document. Chat/Life UI and behavior were not changed.
- The app now has canonical Home/Places root query factories and centralized
  root-prefix invalidation.

### Package 1 — bounded read and candidate substrate

- `ExperienceProjectionReadLimits` is an opt-in database-bound envelope. The
  existing graph reader applies limits to plans, occasions, joins, commitments,
  evidence, outcomes, openings, and participant rows; callers that do not pass
  limits preserve historical behavior.
- `run_bounded_reads` and `BoundedRootReadPortfolio` run independent sources
  concurrently, bound item/source counts, and return stable degradation codes
  (`source_timeout`, `source_unavailable`, `source_item_bound`) instead of
  leaking exceptions into the root.
- Home and Places adapters convert current owner reads into bounded,
  owner/evidence-backed candidates. They preserve source identity but do not
  treat legacy section order as a new hierarchy.
- Separate Home and Places selectors now apply the shared gates while keeping
  each root's candidate boundary explicit; they do not yet replace the v1
  serving compiler.
- Deterministic hard gates reject missing owners/evidence, unauthorized
  audience, stale/revoked/expired/non-feasible candidates, and candidates
  outside the target root. Unknown descriptive content is suppressed, while an
  unresolved current Commitment remains visible only as a typed recovery
  Instrument with fallback and confirmation. Cluster arbitration precedes seat
  arbitration; demand budget is the final boundedness gate. Diagnostics are
  available to tests/internal evaluation only.
- The pure v2 modules are lazily importable without initializing the legacy
  Places/lived-experience dependency graph.

#### Serving-topology update — 2026-09-01

The bounded portfolio is now active on `GET /api/root-projections/v2/home`.
Eight independently degrading reads contribute candidates: Experience Graph,
legacy Plan/Trip state, open Plan proposals, automatic Places context,
explicit saves, action receipts, bounded contextual Places value, and
recipient-authorized addressed Place handoffs. An unavailable source omits
that family and emits a stable degradation instead of failing the whole Home
projection.

This activation remains deliberately bounded. General Artifact/Source
clusters, prior exposure, and broad provider state are not yet direct Home
readers. Addressed Place handoffs are the one direct relationship contribution
and carry their exact relationship grant; they are not a generic activity
feed. Places still adapts one canonical `PlacesFeed`; its v2 endpoint is a
semantic shadow, not a four-state runtime portfolio. Tested substrate, active
serving, and production-shaped evidence therefore remain separate claims.

## Package 2A — typed dark boundary (completed 2026-09-01)

The first compiler slice now crosses the repository boundary without changing
what a user sees:

- pure `compile_home_v2` and `compile_places_v2` functions emit the immutable
  v2 envelope from already-admitted candidates; they do not read databases,
  rank page-shaped sections, or select a client component;
- `GET /api/root-projections/v2/home` and
  `GET /api/root-projections/v2/places` expose those compilers behind the
  existing authenticated router, with Home's bounded Experience Graph limits
  and Places' independent-source degradation preserved;
- the complete OpenAPI snapshot and generated mobile projection now include
  the v2 paths and response schemas (typed payload families, regions, Places
  states, destinations, degradations, and the optional admitted composition
  brief). `RootCandidate` remains an internal producer type and is no longer a
  mobile alias;
- `EXPO_PUBLIC_ROOT_PROJECTION_V2` is registered as a default-off,
  development/internal-only migration gate with an explicit review date;
- Home mounts its opt-in v2 read behind that gate; Places keeps its v1 renderer
  by default while a separate internal-only World Field renderer is now dark
  and independently gated. Mock mode makes no v2 request and the flag cannot
  activate in a public release build. Native v2 kind registries and Home
  renderer parity were completed in Package 2B.

## Package 2B — Home native v2 renderer (completed 2026-09-01)

The internal Home path can now consume the typed envelope without translating
it back into the v1 semantic-result contract:

- `HomeRootV2UnitRenderer` is a client-owned registry for every kind currently
  emitted by the active Home portfolio: `now_commitment_instrument`,
  `now_recovery_instrument`, `now_prepared_possibility`,
  `motion_occasion_row`, `motion_loose_end_row`, `motion_all_plans_door`,
  `horizon_editorial_passage`, `horizon_aperture_row`, `people_note_door`,
  `continuity_capability_field`,
  `continuity_since_you_looked`, and `continuity_life_door`. Future kinds remain
  dark until their native renderer and tests are registered; there is no
  generic-card promotion bypass;
- `HomeRootV2Screen` renders the envelope's orientation, canonical region
  order, degradation notice, owner/source doors, capability actions, and Rest
  Close from semantic payloads only; no server component, route, or geometry
  appears in the wire contract;
- the Home root selects v2 only when `EXPO_PUBLIC_ROOT_PROJECTION_V2` is
  explicitly enabled in a development/internal build. With the flag off, the
  existing v1 root remains the serving path; a v2 read error stays an explicit
  guarded internal recovery state rather than silently mixing v1 and v2
  snapshots;
- a typed v2 mock fixture makes the initial composition testable without a
  backend, while real builds use the authenticated v2 endpoint; and
- Chat, Life, Places serving, and the existing v1 Home contract remain
  unchanged.

This is a renderer and serving-cutover scaffold, not promotion evidence. The
first-class orientation/week-shape producer now exists, but the v2 envelope
still needs the complete Home posture matrix, real-data captures, generated
Composition/live-Instrument compatibility evidence, and action/readback
evidence before the flag can be broadened.

## Latest implementation slice — 2026-09-01

The next convergence pass moved the contract from typed transport toward an
honest producer boundary:

- `RootHomePosture` is now the canonical v2 posture vocabulary, resolved by a
  pure policy over the bounded Experience Projection. The v2 route no longer
  infers `ordinary` or `quiet` from candidate count.
- Home `world_read` and `week_shape` are first-class chrome candidates. The
  producer owns their evidence, source refs, seven-day local date range, and
  `RootReadScale`; the native renderer consumes `projection.chrome` and no
  longer derives orientation from the dominant card.
- The mobile schema projection is synchronized with the implementation
  contract for `RootHomePosture`, `RootReadScale`, `RootWeekShape`, Home chrome,
  and `CompositionBriefV1`. The complete and mobile OpenAPI snapshots were
  regenerated in an isolated workspace lane rather than overwriting concurrent
  changes in the primary checkout.
- Places v2 adapters leave Home/Life/Path-owned reasons (`gap`, `expiry`,
  `group_waiting`, `anniversary`, `harvest`, `register`) out of World Field
  rather than presenting them under the wrong spatial grammar.
- The compatibility Places workspace accepts the v1 root envelope as its feed
  authority and disables its second `usePlacesFeed` network read when seeded.
  A separately gated v2 request may run in semantic shadow, but cannot replace
  the mature workspace.
- A dark `PlacesRootV2Screen` can inspect World Field units directly, including
  server-authored scope/search-map chrome and typed source/action doors. It is
  rehearsal/debug infrastructure only. The existing
  `EXPO_PUBLIC_PLACES_ROOT_V2_RENDERER` environment name is retained for
  internal-build compatibility, but now enables only the semantic shadow read;
  Home can be dogfooded without replacing the mature Places workspace.

These are bounded producer/authority corrections. They do not promote Places
v2, change Chat or Life, or claim final Home editorial coverage.

## Post-review corrections — 2026-09-01

The implementation review found several places where the seam was typed but
not yet truthful under bounded reads or real user consequences. Those gaps are
now closed in the backend and the internal Home consumer:

- bounded Experience Graph queries prefer recent rows and filter inactive or
  expired openings before applying limits, so old records cannot starve the
  current Home read;
- Home adapters interleave commitment, opening, occasion, and outcome families
  instead of allowing one family to consume the entire bounded portfolio;
- adapters emit canonical status/freshness, explicit target-root projections,
  and recovery instruments/actions; Places friend cards no longer manufacture a
  contribution grant from the card itself;
- gate diagnostics now contain one final decision per candidate, and compiler
  revisions hash all visible candidate content (including actions, sources, and
  explanation) rather than only lifecycle fields;
- Home projection validation enforces the four unique regions, unique unit IDs,
  and a real dominant unit; source failures degrade independently for the
  bounded portfolio; and
- the mobile v2 cache keys now match root invalidation prefixes, source doors
  are available on instrument units, and typed action/continuation destinations
  route by their declared owner root.
- Home posture, world-read chrome, week-shape chrome, and producer-selected
  read scale now come from the v2 composition policy; the client no longer
  synthesizes opening copy from a regional unit.
- Places' compatibility bridge no longer performs a second feed request when a
  root envelope already supplied the canonical feed, and deferred non-World
  Field reasons are filtered before v2 admission.
- Provider `unknown`, Commitment `changed`, and Commitment `unknown` now resolve
  to the same urgent recovery path as provider failure. The urgent projection
  contract requires a real dominant unit, and repair continuations require
  confirmation.
- Semantic silence and unregistered Home/Places kinds render nothing. Legacy
  Places cards now remain owner links, and canonical Outcomes remain direct
  state; neither is promoted to generated Composition merely because it has
  title/body copy.
- The executable backend `CompositionBriefV1` compiler admits claim-local,
  audience-safe, novelty-bearing generated drafts into a typed
  `RootComposition` while retaining the complete brief. Its bounded canonical
  Opening owner path is now wired, but there is no universal saved-composition
  writer or real model producer yet.
- Typed destination navigation now carries a short-lived exact-return token;
  the associated registry preserves origin projection/revision, active unit,
  selected Resources, viewer, audience, represented time, and continuation.
- The global return tracker now completes destination handoffs, and Home and
  Places restore the exact originating unit after a background refresh and
  native layout rather than merely retaining an unused token.
- A canonical Opening can retain a strict semantic composition draft. Home v2
  revalidates and re-admits that draft on every read, emits its claim-local
  Sources and typed anatomy only when still valid, and degrades to short prose
  without pretending legacy copy is generated synthesis.
- Native composition rendering now covers bounded evidence, sequence,
  comparison, spatial, and prose anatomy for both lead and support media. The
  conformance gate rejects medium/anatomy mismatches; this is semantic renderer
  coverage, not final visual approval.
- Canonical artifact projections now hydrate optional graph owner/time/place
  context, preserve artifact-to-Source derivation semantics, expose executable
  owner doors, and serve confirmed owner image Sources through an authenticated,
  no-store streaming route without exposing private custody keys.

These are seam corrections, not a production promotion. The remaining
promotion gates listed below are unchanged.

## Production-shaped Home value slice — 2026-09-02

The first package after the sequencing correction returns S2/S3 work to
visible product value while preserving the system architecture already built:

- Home may take at most two current-world contributions from the canonical
  Places feed. A source-backed editorial angle must carry real preview
  substance and becomes a complete-on-view read; a grounded place,
  experience, area, or city remains a typed Door into Places. Saves, memories,
  generic friend activity, notices, and prompts are not copied into Home.
- Recipient-authorized `send_now` Place handoffs can become private,
  attributed Home reads only after the Experience Graph entity resolves to a
  canonical Places identity. The sender's message is preserved as human copy;
  Vesper supplies placement and the typed Places Door without paraphrasing or
  inferring relationship meaning.
- Both families enter the existing owner-read, value-over-silence, treatment,
  consequence, and continuity spine. Neither creates a new Home feed model or
  a second durable writer.
- The native Home renderer now explicitly admits
  `horizon_editorial_passage` and `people_note_door`, and read payloads preserve
  their typed destination instead of degrading to a generic source door.

Backend commit `ce1cc3e94` and mobile commit `ed28aeb26` carry the slice.
Focused and adjacent verification covers 45 backend root-projection tests,
four native renderer tests, TypeScript typecheck, and Expo lint. Physical
device evidence remains a later promotion gate; this package is not public
promotion evidence.

### Places substance and exact-depth correction — 2026-09-02

The follow-on review closed two product-coherence failures in the first slice:

- an approved editorial angle with bounded preview substance now reaches the
  Places semantic root as a `read` / `make_sense` contribution. Places no
  longer throws away the body and reduces an authored reading to its title and
  an Open link. Angles without usable preview substance remain smaller owner
  links; overlong content is declined rather than silently truncated;
- `places.open_entity` now resolves an exact venue, site, accommodation, or
  experience destination before falling back to the broader Places context.
  The short exact-return token survives that detail handoff. An addressed
  Place note therefore opens the object it names instead of discarding its
  identity at the tab boundary.

Backend commit `5c7ef3fe1` and mobile commit `36b4e9a48` carry the correction.
Verification covers 38 adjacent backend root/runtime tests, 14 native
Places/Home/navigation tests, TypeScript typecheck, and Expo lint.

The Artifact/Source audit also narrows the next package. The repository has a
canonical artifact projection, executable `source.inspect` owner reads,
claim-local composition admission, native evidence/sequence/comparison/spatial
renderers, and an Opening that can retain an admitted private Home draft. It
now has the authority-preserving half of the production contribution boundary;
the production seed assembler and governed producer remain absent. Adding a
recent-artifact count, recap, or generic Source shelf to Home would still be a
flat report and is not an acceptable substitute.

### Governed Source contribution compiler — 2026-09-02

Backend commit `0b3cbfcac` and mobile commit `b875af02f` establish the shared
contract between governed evidence and root-native value:

- `SourceContributionSeedV1` freezes the Sources, represented time, audience,
  permitted roots and moves, subject/owner scope, canonical audience grants,
  and claims already known to the person before a producer drafts anything;
- the compiler rejects invented or mutated Sources, expired evidence, widened
  audience, unauthorized roots/moves/subjects/owners, relabeled known claims,
  unsupported synthesis, unused claims, invalid root jobs, and expressions
  that fail the existing claim-local Composition admission contract;
- a successful compile preserves one contribution and one evidence identity
  while admitting distinct root-native briefs. Home receives a temporal
  `horizon_editorial_passage`; Places receives a spatial
  `field_lead_composition`. This is not one cloned card mounted in two tabs;
- private ordinary/current-world, open-interval, and recent-return cases pass.
  A live/shared case passes only with an existing canonical use, Occasion, or
  relationship grant. Source visibility by itself cannot widen the audience;
- both root candidates are complete on view, retain `source.inspect` evidence
  doors, and preserve Source expiry, lifecycle, subject, owner, and grant
  references. The app now explicitly renders the admitted Places field
  composition; Home already rendered its admitted editorial passage kind.

Focused verification covers **95** backend root-projection and semantic-result
tests and **31** mobile Home/Places renderer tests. TypeScript typecheck, Expo
lint with zero errors, and the 31-scenario polish registry validation pass.
The Places workspace design contract and dry-run QA scaffold pass, but no Metro
session or device capture was available; this is deterministic compiler and
native-renderer evidence, not visual or release certification.

### Canonical owner-read assembly and shared portfolio seam — 2026-09-02

Backend commit `d98cd02e3` implements the next authority layer without turning
generated text into its own evidence:

- producer-readable material is private server input; the compiler receives
  only a seed assembled from exact canonical owner reads;
- every material Source must already appear in an available Source read, and
  every subject must already appear in Source, Place, or Moment authority;
- unrelated reads cannot donate owner scope. Owner overflow rejects the
  assembly instead of being silently truncated;
- a non-private assembly requires one identical canonical grant across every
  selected Source, every selected Place/Moment context read, and the relevant
  relationship or coordination owner. A grant on only one Source cannot
  authorize the others;
- rejected assembly never calls the producer. Producer failure, compiler
  rejection, and admission remain distinct fail-closed states;
- Home and Places now accept the same production object at their shared
  pre-judgment portfolio boundary and select only their native expression.
  Existing treatment, value judgment, root selection, and rendering still run
  after that merge.

Focused and adjacent verification at this checkpoint covered **112**
root-projection, owner-read, and semantic-result tests; all changed backend
hooks passed. It still did **not** generate a live contribution on a default
route. The next package therefore had to add owner-backed material loading and
governed invocation without allowing a model draft to supply its own Sources,
subjects, owners, grants, or novelty baseline.

### Canonical material loading and bounded producer pipeline — 2026-09-02

Backend commit `0f8c32aac` implements the next shadow-runtime layer:

- retained Experience Anchors, approved evidence-bearing dossiers, and
  attributed Place handoffs now have exact canonical material loaders. The
  loaders resolve current revisions, custody, authorship, freshness, audience,
  and expiry from existing owners and fail closed on missing evidence,
  withdrawal, expiry, revision conflict, malformed identity, or unsupported
  Source kind;
- the Source owner-read registry now supports an exact Place handoff without
  exposing its human message in the owner-read payload. It preserves the
  relationship grant and expiry; non-private use requires the same explicit
  grant, and public material remains forbidden;
- Anchor claims and addressed human prose are treated as already known input,
  preventing the producer from relabeling them as Vesper novelty. Approved
  dossier claims remain outside that baseline because availability as public
  research does not prove the person already knew them;
- one typed selection fixes Sources, subjects, situation, audience, roots, and
  moves before loading. The pipeline derives one viewer and represented clock
  from canonical reads, rejects selection substitution or mixed-viewer input,
  and invokes the producer only after every selected material is available;
- the existing owner assembly and compiler still independently verify exact
  Source, subject, owner, context, audience, grant, novelty, and evidence
  authority. Stale Source material now produces stale root candidates rather
  than fresh-looking generated value.

Focused and adjacent verification now covers **148** root-projection,
owner-read, and semantic-result tests, plus every changed backend commit hook.
The runtime remains intentionally cold on default Home and Places routes. It
has no production Source-selection policy or default prompt/model producer.
Those are activation dependencies, not reasons to create a second contribution
or projection architecture.

### Semantic delivery identity and qualified root exposure — 2026-09-02

Backend commits `cbe300c9a` and `9f52a1294`, app commit `d89111d6f`, and the
corresponding generated contract close the exact-repeat seam without confusing
it with live-engine consequence:

- an admitted contribution derives a root-neutral `fact_key` from canonical
  claim text, operation, authorship, novelty, confidence, claim-local Source
  roles, Source identities and revisions, subjects, and audience. Generator
  IDs, titles, media choice, and surface expression copy do not change it;
  correcting a canonical Source revision does;
- `RootUnit` retains the key through compilation. Home and Places selectors can
  reject an exact key already delivered to the viewer with the explicit
  `repeated_exposure` gate rather than relying on page position or card copy;
- the server wraps each deliverable unit in a short-lived HMAC proof binding
  recipient, root, projection identity and revision, unit, fact key, and
  expiry. `POST /api/events/root-delivery` accepts only that proof-bound,
  content-free receipt and remains unavailable through generic event ingress;
- recent-delivery lookup suppresses `rendered`, `opened`, `dismissed`, or
  `acted` facts. An explicit `not_rendered` receipt never claims delivery, and
  a receipt-reader outage fails open rather than blanking a root;
- native Home and the dark Places v2 renderer share measured viewport geometry.
  A unit must remain visible for the qualified dwell before the client reports
  delivery. Fetch, render-tree mount, and below-fold layout do not count; and
- semantic delivery and causal treatment retain independent dwell identities,
  device receipts, server proofs, and dedupe keys. One unit may carry either or
  both without one lifecycle standing in for the other.

The three delivery flags remain default-off. This package proves exact semantic
delivery and repeat suppression only. It does **not** prove comprehension,
agreement, memory, general familiarity, or claim-level knowledge for every
fact in a composition. It also does not add a default model producer, public
route activation, or device/release evidence.

Verification covers 165 focused backend root-projection, route, receipt,
private/multiplayer, correction, repeated-exposure, and fail-open tests; 22
focused mobile utility, transport, boundary, Home, and Places tests; TypeScript
and generated-contract typechecks; Expo lint with zero errors; API-boundary and
schema-bridge checks; and deterministic schema regeneration. The aggregate
mobile fast gate still stops on pre-existing size-budget overruns in the
unchanged mature `PlacesSectionFeed.tsx` and `PlacesWorkspace.tsx`.

### Governed Source opportunity discovery and selection — 2026-09-02

Backend commit `66d83911f` closes the pre-model Source-selection seam without
turning the model into an index, authority resolver, ranker, and writer:

- discovery is bounded to 32 exact metadata-only coordinates across current
  retained Experience Anchors, approved and evidenced dossiers under the
  already-resolved canonical Places context, and recipient-visible live or
  kept Place handoffs. Producer prose, Anchor claims, dossier bodies, and human
  messages do not enter the inventory;
- ordinary and open-interval Anchors require an exact canonical context link.
  A recent-return bridge is separately bounded to lived evidence updated within
  45 days and the current return context; it is a retrieval fact, not a claim
  that every artifact concerns every Place;
- handoff discovery rechecks recipient, lifecycle, expiry, graph-to-canonical
  Place binding, owner, and exact relationship grant. Dossiers recheck approval,
  contextual Place identity, current revision, and evidence receipts;
- a deterministic situation table forms only complementary pairs and retains
  at most 12 inspectable groups. It prefers lived evidence plus world context
  after a return, and addressed perspective plus world context in ordinary or
  live/shared situations. It never promotes two generic public readings into
  personal value merely because inventory exists;
- low discovery budgets interleave Source families so the bound cannot starve
  the complementary evidence required for synthesis. Stale, future, expired,
  public-only, context-free, split-grant, or exact excluded-repeat groups return
  an explicit silence result;
- the chosen Source, subject, and grant coordinates expand into one exact owner
  read per Source plus the required Place and Relationship reads. The existing
  material loader and compiler still revalidate every ID. Assembly additionally
  rejects a canonical grant that differs from the selected grant before the
  producer can run.

Verification covers **187** root-projection, canonical-owner, Places-content,
and Discover tests, plus every changed backend commit hook. The selector is now
a real shadow-runtime dependency. It is not a live feed or release claim: the
default governed producer, latency/retry/failure budgets, dark route invocation,
and situation-matrix dogfood remain the next package.

### Structured Source producer and double-dark root wiring — 2026-09-02

The next backend package completes the production-shaped seam without claiming
that generated contributions are live:

- a versioned structured prompt and strict decision schema permit either one
  governed draft or explicit earned silence. The producer is instructed to add
  new intellectual work rather than paraphrase known attention, infer a person,
  manufacture intimacy, or ask for more input;
- the adapter has explicit Source, input-character, output-token, timeout, and
  schema-retry ceilings. It requires a named model role as a constructor input;
  no existing role is borrowed and no unapproved registry default is added;
- a single orchestration preserves discovery inventory, exact deterministic
  selection, owner-read portfolio, canonical material load, production, and
  compiler result. A silent selection performs no content read and no model
  call;
- Home and Places now share the same optional pre-judgment production seam.
  Each receives only its native expression, after which all existing judgment,
  consequence, selection, delivery, and renderer contracts remain binding; and
- the serving seam requires both a default-off backend flag and a configured
  producer. The latter is intentionally absent pending model-role approval, so
  current routes preserve established response behavior. Known optional
  failures collapse to absence rather than failing either root.

Focused verification covers producer budgets and retry/silence behavior,
orchestration stop/proceed behavior, feature-gate truth tables, route fail-closed
behavior, and the existing Home/Places API suite. The next step is explicit
model-role assignment followed by the four-situation rehearsal; this checkpoint
is architectural and regression evidence, not content-quality or release proof.

### Content-free situation-matrix acceptance gate — 2026-09-02

Backend commit `de7bb3bb4` turns “test the whole matrix” into an executable
contract rather than a checklist:

- ordinary/current-world, open-interval, recent-return, and live/shared each
  execute as produced baselines through the full governed shadow pipeline;
- every produced case must reach both Home and Places with distinct payload
  hashes, preventing a shared semantic contribution from becoming one cloned
  card mounted twice;
- live/shared must carry group audience plus an exact grant count, while the
  three private baselines must remain grant-free;
- earned silence, excluded exact repeat, withdrawn authority, Source expiry,
  provider outage, parse failure, compiler rejection, and latency overflow are
  independently observable acceptance probes; and
- the resulting artifact contains no Source prose, generated copy, claims,
  named people, Places, or source IDs. It can therefore become the stable
  structural envelope for later model-backed and dogfood evidence without
  turning private content into release telemetry.

The adjacent suite passes **216** tests. The structured adapter also decodes a
complete provider-style nested draft and re-enters the governed compiler, so
the positive JSON path is covered alongside silence, parse failure, character
and Source ceilings, retry, and timeout behavior. This is deterministic structural proof,
not a claim about real-model content quality or device presentation. Model-role
approval, real generated outputs, editorial adjudication, and internal-cohort
evidence remain necessary before enabling the existing double-dark serving gate.

### Content-free production-attempt continuity — 2026-09-02

Backend commit `e54631927` closes a different repeat boundary from semantic
delivery. Before the runtime opens canonical owner reads, loads governed
material, or calls the structured producer, it now acquires an atomic lease for
`viewer × exact Source group`:

- the group key already binds situation, audience, every Source identity and
  revision, subject revision, and grant revision. Corrected or newly revised
  evidence creates a new group rather than inheriting an old suppression;
- one durable row contains only viewer, opaque group key, situation, audience,
  lifecycle state, attempt count, lease token/times, and retry boundary. It
  stores no Source IDs, prose, claims, people, Places, generated draft, or root
  payload;
- active leases and terminal cooldowns become selector exclusions. If another
  Home or Places request wins the same group concurrently, the loser considers
  the next bounded group or returns typed repeat silence without opening owner
  reads or paying for a model call;
- terminal outcomes distinguish produced, earned producer silence, producer
  failure, compiler rejection, and pre-/post-producer pipeline rejection. Their
  retry windows are explicit rather than an undifferentiated permanent cache;
- completion requires the current lease token. Work from an expired worker is
  withheld if another request has reclaimed the group; and
- attempt-store failure fails the optional contribution path closed. The
  established Home or Places root still returns, but generation cannot proceed
  without durable ownership.

The ledger does not claim delivery, comprehension, memory, treatment, or
consequence. Qualified semantic delivery continues to use its proof-bound
viewport receipt and root-neutral `fact_key`; causal treatment continues to use
its own identity and receipt. Attempt continuity prevents duplicated internal
work, delivery continuity prevents repeated surfaced meaning, and the
live-engine lifecycle governs real-world action.

The migration remains the single Alembic head. A real PostgreSQL two-thread
race proves exactly one claimant, expiry repair, stale-token rejection, and
terminal cooldown exclusion. The complete adjacent Home/Places/Source suite
passes **231** tests. The wider offline repository run completed with **20,076
passed** and **25 pre-existing unrelated failures** in itinerary, vector
release, research, privacy-coverage, and fixture-promotion areas. No model role
was assigned and no rollout flag changed, so this is concurrency and continuity
evidence—not content quality, device, cohort, or release evidence.

## Integrated convergence execution — 2026-09-01

The latest package converts the earlier seam into a broader, executable
Home/Places rehearsal while preserving the product boundaries accepted after
the August pivot.

### Home

- The v2 route now composes the active five-source portfolio described above.
  Legacy Plans remain canonical owners during migration; the adapter projects
  their current consequence without importing the Trips Home page hierarchy.
- Automatic Places context contributes one current-world aperture and carries
  the exact opaque context handle into Places. Explicit saves contribute
  refinding doors. Action receipts contribute causal evidence without
  pretending a request was a completed result.
- A deterministic one-person rehearsal covers ordinary New York, an open
  weekend, a shared Saturday Occasion, a live Plan, a recent Europe return,
  and a ferry disruption. Together those cases exercise the four Home
  postures and all four Places encounter-state contracts without creating one
  privileged behavior loop.
- The native Home registry now renders the ten kinds actually emitted by the
  active portfolio. Unsupported members of the larger accepted union still
  render nothing.
- Typed Home doors resolve canonical Trip, Place, venue, site, dossier,
  experience, person, artifact, save, receipt, and Places-context references.
  Commitment repair opens Chat with a viewer-resolved Experience Graph seed;
  unfinished Plan continuation carries Trip scope. The short return token
  still preserves the originating projection and unit.

### Places

- The mature Places workspace is the canonical serving renderer. Search, map,
  saved collections, editorial reading, social rows, offline behavior, and
  exact context propagation are not discarded when the v2 shadow flag is on.
- The v2 adapter now points known cards at their canonical objects instead of
  the UI-level `places_card` placeholder and emits typed open-owner actions.
- Consent-bearing social fixture data is scoped to the exact group Trip in
  mock mode. Passing a Places context handle now reaches the mock projection
  rather than being silently dropped; this prevents a contribution from
  leaking into a different Lisbon occasion.
- The World Field boundary is explicit: gap/expiry/group-waiting belong to
  Home, anniversary/harvest to continuity, and register to Path. The shadow
  compiler omits those reasons rather than recreating the legacy omnibus feed.

### Promotion and deletion verdict

- **Home v2 remains development/internal only.** Its architecture and
  deterministic scenarios are credible enough for dogfood, but not yet for a
  public default.
- **Places v2 remains shadow only.** The internal inspection renderer is not a
  replacement for the mature workspace.
- **No further legacy deletion is safe in this slice.** The removed v2 serving
  branch in `PlacesRootExperience` was dead as a product path; the remaining
  v1 Home/Places compatibility owners still serve released behavior or
  capabilities absent from v2.
- Exact semantic return is implemented, but the stronger Home→Places
  navigation law—depth inside the Home origin stack without selecting the
  Places tab—does not yet have a production route family. Do not call Package
  4 complete until that native navigation behavior and owner readback are
  exercised on device.

## Verification

- Backend Home/Places rehearsal, portfolio, compiler, return, composition, and
  API suites: **69 passed** in the final focused run.
- Frontend root mock, conformance, renderer, navigation, return, invalidation,
  Places-route, and workspace-navigation suites: **38 passed** in the final
  focused run.
- Frontend TypeScript typecheck and generated-contract typecheck: **passed**.
- Complete OpenAPI and active-mobile contract check: **passed** with 564 paths,
  626 operations, and 1,406 schemas in the complete snapshot; the app
  projection remains current at 431 paths, 476 operations, and 1,253 schemas.
- Convergence candidate validation and relevant Ruff, formatting, import-cycle,
  boundary, status-guard, and pre-commit checks: **passed**.

The repository-wide suites are not green and therefore are not promotion
evidence. The complete backend canary reported 24 failures in unrelated vector
release, research fixture, bundle-review, privacy-coverage, itinerary-operation,
and dead-handler tests. The complete frontend run reported 29 failing suites /
33 failing tests across existing trip-hero, controls, fixture, detail-hook,
typography, and interaction-adoption contracts. One adjacent failure—the
scoped Mara/Dao Places social fixture—was corrected here and its focused rerun
passes; the entire suite has not been rerun after that correction.

## Deliberately not claimed yet

The current packages establish the permanent seam, an active internal Home
portfolio, and a Places semantic shadow; they do not make v2 production
visible. The following remain:

- full Home posture/real-data and human visual evaluation, including real
  model-authored Composition and live-Instrument compatibility evidence;
- state-specific Places Focus/Path/Live producers and their native renderers;
- confirmed owner/provider consequence readback through the renderer path;
- Home→Places depth that remains in the Home stack, followed by exact native
  return after map/search/detail/action movement;
- explicit model-role approval, real-model editorial adjudication, and
  smallest-cohort Home/Places activation through the existing double-dark
  serving seam, plus a complete known-to-person resolver beyond exact
  delivered-fact suppression;
- direct artifact/Source and broader relationship-grant readers in Home's
  runtime portfolio;
- promotion of any state-specific Places renderer and removal of the remaining
  v1 root/feed compatibility authority; and
- deletion of legacy Trips/Places compatibility code after route-state,
  action/readback, degradation, and social/grant gates pass.

This boundary is intentional: the app has a coherent v2 contract, native
semantic renderer seam, exact-return behavior, and an independently flagged
Life foundation without turning any of them into a repository-wide renderer or
public rollout.
