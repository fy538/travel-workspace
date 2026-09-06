# Memory & Preference — System Charter

> Surface: Vesper (the world-model substrate)
> Maturity (for MVP): MVP-required
> Status: wired
> Last updated: 2026-09-06 (useful-continuity doctrine; implementation status not re-certified)

## Purpose
Preserve admitted, source-bound evidence about how people and explicit
relationship scopes choose, experience, revisit, correct, and respond to the
world; derive a revisable **Personal Memory** projection; and compile
purpose-bound context for understanding, retrieval, and local or travel help.
It serves the moat thesis only when authorized continuity improves a later
experience or capability. Memory volume,
behavioral exhaust, and personality synthesis are not product value.

## Spans (cross-repo)
- Backend: [`travel-agent/backend/preference_engine/`](../../travel-agent/backend/preference_engine/FEATURE.md) (17) + observation/memory CRUD in `core/db/observations.py`, `core/db/traveler.py`; reflection/synthesis live in `concierge/reflection.py` + `refresh_memory.py`.
- Frontend: controlled through Atlas/You and applied through Vesper, Places,
  local plans, and trips; memory is not a standalone destination.
- Tables of record: `observations`, `personal_memories` (versioned markdown), `hard_constraints`, `trip_group_profiles` (internal synthesis), `trip_shared_memories` (authoritative group-safe document), `relationship_memory_claims`, `traveler_place_affinity`, `user_facts`, and source outcomes.

## Public interface (what other systems may call / read)
- **Entry points:** `retrieval/preference_retriever.py::get_traveler_context()` (Personal Memory + hard constraints; generates if missing) · `get_group_context()` (all members — used by Concierge prompt assembly) · `synthesis/group_synthesizer.py` (merge → `trip_group_profiles`).
- **Inbound writes, as built:** Concierge emits `add_observation`
  (fire-and-forget) and `add_hard_constraint`. Under the target
  [Contribution and Consequence Contract](contribution-and-consequence.md),
  these writes require an admitted Source/claim and policy-owned authority;
  model prompt judgment alone is non-conforming.
- **Shared-memory reads/writes:** the trip group-memory API reads and append-versions the group-safe document under membership, organizer, roster, and revision checks. Internal group synthesis remains separate.
- **Relationship memory:** private personal claims and explicitly governed circle/source-roster claims retain source, scope, state, and visibility rather than being folded into Personal Memory prose.
- **Consumes:** admitted observations, explicit constraints, owned Outcomes,
  governed relationship/place evidence, and narrowly scoped behavioral evidence.
  Raw interaction exhaust may support analytics or current-Occasion delivery
  policy but is not automatically person memory.
- **Never:** other systems must not write `personal_memories` directly — synthesis is the only writer; observations are the only inbound signal.

## Owns (source of truth)
Admitted observations, hard constraints, internal group projections,
trip-shared memory content, relationship-memory claims, and place affinity.
Group/Social owns who belongs to a Trip or explicit circle and therefore who may
receive each projection. Place and outcome history owned elsewhere may be
consumed as evidence; this charter does not duplicate their source-of-truth
records.
**Personal Memory is a derived context projection, not the authority that makes
its prose true.** Sources, explicit claims, constraints, Occurrences, Outcomes,
and correction lineage remain authoritative. Other systems must not treat the
summary as permission to widen scope or audience.

## Invariants (must always be true)
- **Versioned, never destructive:** Personal Memory is append-version markdown (`version_number`); regeneration creates a new version.
- **Narrative, not vectors:** there are **no pre-computed preference embeddings** — the LLM reasons over the markdown at runtime. (Don't "add a vector index" — it's a deliberate non-choice.)
- **Hard constraints are separate** from taste (dietary/accessibility/language live in `hard_constraints`, treated as binding, not preference).
- **Privacy tiering:** individual constraints are sacred; only allow-listed shared interests / binding constraints enter group context (the egress boundary Concierge enforces downstream).
- **Current explicit intent outranks historical inference.** Behavior may
  contradict or qualify a claim only as scoped evidence. Dwell, read timing,
  response latency, silence, ignored suggestions, queries, and individual votes
  do not become durable preference or identity evidence by default.
- **Contribution authority precedes write-back:** every retained observation
  identifies Source, truth type, scope, authority basis, expiry where relevant,
  and correction path. Synthesis cannot upgrade an ungated signal.
- **Use, retention, inference, audience, and action are separate:** Use names
  purpose and eligible consumers; Retention separates Source, claim, and
  projection lifecycle; Inference names world/product/situation/person/
  relationship target and L0–L4 scope; Audience preserves contributor,
  affected principal, custodian, and recipients. Permission on one axis does
  not widen another.
- **Outcome causality is non-transitive:** exposure, save, Commitment, provider
  confirmation, Occurrence, and authored Outcome are separate stages. Product
  and situation learning may proceed without a person claim; person and
  relationship learning require governed evidence.
- **Application proves value:** judge memory by improved understanding,
  retrieval relief, enjoyment, capability, prospective help, coordination, or
  judgment—not volume or callbacks. Evaluate the benefit appropriate to the
  job; a useful return need not produce a decision or transaction.
- **Context transfers carefully:** local evidence may inform travel and travel
  evidence may inform local decisions, but scope, companions, occasion, and
  confidence must remain explicit.
- **Multiplayer memory is plural:** personal evidence, internal group model,
  editable shared episode/agreement, live group state, and recurring-group
  hypothesis are separate records. A shared episode never overwrites different
  private outcomes.
- **Inspectability is contextual:** consequential projections explain concrete
  evidence through “Why this?”; Life supports relation-level correction,
  resurfacing exclusion, release, audience change, and Source deletion. Memory
  must not expose a universal inferred biography or personality dashboard.
- **Relationship scope is exact:** person-place, person-companion, and
  `(person, place, companion)` projections do not grant one another visibility
  or authority automatically. Current intent and membership outrank history.

## Assistance preferences and scoped correction

Topic interest does not establish the benefit a person wants, the depth they
prefer, or the part they want to do themselves. Compile those distinctions
under [Product Model §4.1](../../travel-agent/docs/product/Product%20Model.md#41-adaptive-assistance-within-one-product)
and the existing contribution contract; do not introduce a second personality
profile or silently learn a durable role from usage.

Current instructions govern the immediate response. Session/Occasion treatment
adjustments expire with their scope; ongoing assistance preferences require
admitted evidence and remain correctable. “Not this weekend” changes timing;
“that was for my parents” corrects subject/context; “too long” can change depth
without rejecting the topic. “Keep, but don't recommend from it” separates
custody from future influence and must invalidate dependent recommendation use.
Resolve only consequential ambiguity; do not add a setup or feedback ritual.

Observed behavior is conditioned on what Vesper exposed and which alternatives
were available. Repeated reads or selections do not independently prove the
person prefers that value mix. Non-use and silence establish neither success
nor dislike. Apply the existing L0–L3 boundary rather than automatically
promoting treatment history into person memory. Learned convenience preferences
never widen action, audience, or inference authority.

Evaluate changed purpose, correction scope, subject attribution, and retained
capability access using the [adaptive-experience cases](../working/vesper-consumer-promise-and-adaptive-value-research-2026-09-05.md#7-adaptive-experience-comparison-and-design-handoff).
This section defines target behavior; it does not certify legacy writers or
claim that adaptive defaults are implemented.

## Useful continuity beyond recollection

An ordinary question can be a complete entry and a natural reason to return.
Answer it well now; neither an Occasion nor future memory is required. A
question records a current request, not automatically a durable interest,
intention, preference, or identity. Where prior context is already authorized
for this purpose, use it to improve the contribution rather than merely repeat
what the person said. Current purpose and new interests can outweigh history.

Low-effort acquisition, precise representation, and useful application are
separate design goals. Automatic use within granted authority need not require
manual curation of every memory; effortless input does not authorize hidden
inference. Preserve original authorship, AI additions, and user-endorsed meaning
through reuse. Offer contextual evidence and correction without narrating every
retrieval or requiring a profile-maintenance habit.

**Current Ask authority is unchanged:** no new durable personal state by
default. The [casual-question continuity proposal](contribution-and-consequence.md#310-open-proposal-casual-question-continuity-not-in-force)
is pending, not an enabled agreement or a runtime claim. Its
[research basis](../working/vesper-consumer-promise-and-adaptive-value-research-2026-09-05.md#10-casual-questions-and-useful-continuity)
separates acquisition, representation, application, initiative, visibility,
and control; “implicit versus explicit memory” is not a sufficient contract.

## Failure modes
- Missing Personal Memory → generated on demand in `get_traveler_context()`.
- Synthesis (Haiku) failure → returns last good version; staleness check retries in background.

## Maturity & validation
- Serves journeys: 04 (private constraint → group-safe plan), 11 (Atlas candidate → memory control).
- DoD state: synthesis/retrieval unit tests ✅ · eval fixtures pre-seed memories ✅ · **artifact-quality not yet validated** (memory surface eval pending) · mock-walk ❌.
- All synthesis is **Haiku** (cost-sensitive, high volume); `reflection`/`memory_refresh` auto-upgrade to Sonnet post-trip.

## Canonical docs
- why → `product/Content as Infrastructure.md` · how → `architecture/Memory Architecture.md` · `architecture/Unified Context Graph.md` · what(be) → `backend/preference_engine/FEATURE.md` · `backend/core/FEATURE.md`.
- Tests: `tests/preference_engine/*`, eval fixtures via `scripts/load_eval_fixtures.py`.

## Cross-cutting constraints
- **Contribution authority:** every observation, fact, constraint, note,
  reflection, affinity, and synthesis input follows
  [Contribution and Consequence](contribution-and-consequence.md). Personal
  Memory cannot launder raw chat or telemetry into higher-authority truth.
- **Graph legibility**: every new signal this system surfaces back to the user (or injects into other surfaces) must be evaluated against [graph-legibility-doctrine.md](graph-legibility-doctrine.md). Memory is the primary source of graph signals — it is also the highest-risk system for violating show-don't-tell.

## Open risks / known gaps
- **Legacy observation admission is non-conforming.** Concierge prompts and
  `observe()` tooling still encourage same-turn writes for inferred preference,
  personality, mood, emotional investment, and patterns of silence. Gate these
  writers before expanding Chat, Home, Places, or Life on top of them.
- **Synthesis can erase epistemic type.** Current Personal Memory markdown and
  group-profile generation do not yet prove that Source, truth, scope, expiry,
  disagreement, and correction survive every synthesized sentence.
- **Artifact quality is unvalidated** — the memory surface "is it worth keeping?" claim has no eval gate yet (flagged 🔶 in the vision ledger).
- The internal group-profile merge remains an upstream half of the privacy-egress invariant; the editable shared-memory document is now separate. Verify both audience paths alongside Concierge journey 04.
- Shared-memory UI/storage exists, but second-occasion application and
  relationship-scoped recurrence are not yet validated product behavior.
- Place affinity recency-decay (added 06-18) affects cross-trip recall ("Vesper knew") — confirm it doesn't surface stale affinities.
- The no-trip/local path does not consistently receive the same memory contract
  as trip planning. This blocks the hometown-trust loop and local→travel proof.
- Current validation is trip-heavy. Add evaluation for a local choice improving
  a later travel decision and for the same evidence behaving differently with
  different companions or occasions.
