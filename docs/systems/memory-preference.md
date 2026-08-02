# Memory & Preference — System Charter

> Surface: Vesper (the world-model substrate)
> Maturity (for MVP): MVP-required
> Status: wired
> Last updated: 2026-08-02

## Purpose
The place-relationship world model: capture evidence about how people and
recurring groups choose, experience, revisit, and respond to places; synthesize
a per-user **Personal Memory** projection; and compile purpose-bound context for
local and travel decisions. It serves belief #4 (*behavior over stated
preference*) and the moat thesis — outcome-backed relationships among people,
groups, plans, and places are the durable asset.

## Spans (cross-repo)
- Backend: [`travel-agent/backend/preference_engine/`](../../travel-agent/backend/preference_engine/FEATURE.md) (17) + observation/memory CRUD in `core/db/observations.py`, `core/db/traveler.py`; reflection/synthesis live in `concierge/reflection.py` + `refresh_memory.py`.
- Frontend: controlled through Atlas/You and applied through Vesper, Places,
  local plans, and trips; memory is not a standalone destination.
- Tables of record: `observations`, `personal_memories` (versioned markdown), `hard_constraints`, `trip_group_profiles`, `traveler_place_affinity`, `user_facts`.

## Public interface (what other systems may call / read)
- **Entry points:** `retrieval/preference_retriever.py::get_traveler_context()` (Personal Memory + hard constraints; generates if missing) · `get_group_context()` (all members — used by Concierge prompt assembly) · `synthesis/group_synthesizer.py` (merge → `trip_group_profiles`).
- **Inbound writes:** Concierge emits `add_observation` (fire-and-forget) and `add_hard_constraint`.
- **Consumes:** raw interaction signals only.
- **Never:** other systems must not write `personal_memories` directly — synthesis is the only writer; observations are the only inbound signal.

## Owns (source of truth)
Personal Memory, observations, hard constraints, group profiles, and place
affinity. Place and outcome history owned elsewhere may be consumed as evidence;
this charter does not duplicate their source-of-truth records.
**Personal Memory is the canonical preference document** — not observations, not
vectors.

## Invariants (must always be true)
- **Versioned, never destructive:** Personal Memory is append-version markdown (`version_number`); regeneration creates a new version.
- **Narrative, not vectors:** there are **no pre-computed preference embeddings** — the LLM reasons over the markdown at runtime. (Don't "add a vector index" — it's a deliberate non-choice.)
- **Hard constraints are separate** from taste (dietary/accessibility/language live in `hard_constraints`, treated as binding, not preference).
- **Privacy tiering:** individual constraints are sacred; only allow-listed shared interests / binding constraints enter group context (the egress boundary Concierge enforces downstream).
- **Behavior outranks claims:** a dwell/visit signal outweighs a stated interest.
- **Application proves value:** stored evidence is useful only when it changes a
  later local or travel decision and the outcome can be measured.
- **Context transfers carefully:** local evidence may inform travel and travel
  evidence may inform local decisions, but scope, companions, occasion, and
  confidence must remain explicit.

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
- **Graph legibility**: every new signal this system surfaces back to the user (or injects into other surfaces) must be evaluated against [graph-legibility-doctrine.md](graph-legibility-doctrine.md). Memory is the primary source of graph signals — it is also the highest-risk system for violating show-don't-tell.

## Open risks / known gaps
- **Artifact quality is unvalidated** — the memory surface "is it worth keeping?" claim has no eval gate yet (flagged 🔶 in the vision ledger).
- The group-profile merge is the upstream half of the privacy-egress invariant; a leak here propagates everywhere. Verify alongside Concierge journey 04.
- Place affinity recency-decay (added 06-18) affects cross-trip recall ("Vesper knew") — confirm it doesn't surface stale affinities.
- The no-trip/local path does not consistently receive the same memory contract
  as trip planning. This blocks the hometown-trust loop and local→travel proof.
- Current validation is trip-heavy. Add evaluation for a local choice improving
  a later travel decision and for the same evidence behaving differently with
  different companions or occasions.
