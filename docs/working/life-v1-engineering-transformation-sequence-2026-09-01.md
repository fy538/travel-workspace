---
doc_type: working
status: active
owner: founder / product / architecture / engineering
created: 2026-09-01
last_verified: 2026-09-04
expires: 2026-10-01
why_new: Converts the accepted Life v1 experience contract into a sequenced cross-repository transformation while preserving separate repositories, generated API contracts, and independently shippable commits.
depends_on:
  - ../contracts/life-v1-experience.md
  - ../decisions/2026-09-01-adopt-life-v1-behavior-sequences.md
  - ../systems/contribution-and-consequence.md
related:
  - life-v1-non-regrettable-engineering-execution-plan-2026-09-01.md
---

# Life v1 engineering transformation sequence

## Current state, 2026-09-04

- The active mobile Life tab can now open the flagged native Life root. The
  legacy Atlas route remains the default compatibility path while the flag is
  off; the native root's complete-record door now opens a dedicated paginated
  reader backed by the existing Atlas timeline.
- Seven provisional Life primitives exist in the mobile tree; they are useful
  raw material, not proof that the root is assembled.
- A deterministic `LifeRefindLane` exists dark on mobile and
  `POST /api/life/refind` exists in the backend.
- The full and active OpenAPI snapshots, operation policy, and generated
  TypeScript now include the additive `LifeRecordPageV1` depth route. The
  mobile reader uses that generated contract; the underlying timeline remains
  Atlas-owned and no second Life archive was introduced.
- Return arbitration, Together propagation, the full contribution lifecycle,
  and causal repair are not implemented as one system.

This means the design is ahead of the product. The next move is not more
independent concept boards and not a legacy-Atlas reskin. It is a controlled
replacement in dependency order.

## Sequence

### 0. Close the contract lane before adding Life payloads

1. Reconcile the Home/Places operation-consumer registry entries blocking
   `make contract-check`.
2. Regenerate `docs/openapi.app.json` and mobile `schema.gen.ts`.
3. Replace the handwritten Life refind response mirror with generated types.
4. Keep `EXPO_PUBLIC_LIFE_REFIND_LANE` off until the native result opens a real
   canonical destination.

Exit: snapshot → app projection → generated mobile types is clean and
repeatable; no Life endpoint has mobile drift.

### 1. Introduce a read-only Life root projection

Add one versioned backend read model for the root rather than asking mobile to
reconstruct Life from many services. It should contain:

- viewer and selected-lens state;
- earned header read or factual fallback;
- deterministic digest entries with canonical object handles;
- the one full-record door and reconciled count/span;
- zero to three already-arbitrated record-native Returns;
- zero to two fixed windows;
- partial-authority and freshness metadata required to render honestly.

The projection reads existing trip, artifact, experience-graph, contribution,
and place owners. It does not create a new universal Life database or migrate
all historical nouns.

Exit: replay fixtures produce stable rich, ordinary, thin, and yielded payloads;
all counts reconcile with the custody query.

### 2. Build and deepen the dedicated native root behind a new flag

1. Create a dedicated Life screen instead of extending Atlas. **Landed:**
   native root, bounded digest, and explicit state handling.
2. Assemble the accepted primitives into the production composition: speaking
   header, labeled lenses, digest, one scroll door, bounded Returns, fixed
   windows, Everything kept.
3. Preserve Atlas as a compatibility route while the flag is off.
4. Implement loading, offline, partial, error, thin, and yielded states at the
   same time as rich—not afterward.
5. Ensure every rendered item carries the canonical object handle.

6. Add a dedicated complete-record reader behind the root door, using a
   cursor-paginated owner projection rather than an unbounded archive. **Landed:**
   Time/Places reader, generated contract, mock parity, and canonical owner
   navigation.

Exit: the Time root works on device from real projection data, without cards,
prompts, filler, or client-side editorial invention.

### 3. Land refinding as navigation, not a side product

1. Attach Search to the Life header and generated contract.
2. Render target-first result, containment chain, match reason, and capability
   limit.
3. Open the canonical dossier for supported targets; unsupported targets open
   a truthful source/object fallback.
4. Keep “Around this” session-local. Do not retain a search or promote a thread
   unless the person separately contributes or authorizes a change.

Exit: all deterministic benchmark queries open the correct object; unsupported
semantic recovery admits its limit; search produces zero writes.

### 4. Build dossiers before adding more root density

Implement the smallest destination set required by what the Time root and
search actually render: journey/episode, place relationship, thread, and
viewer-relative shared record. Each owns:

- canonical identity and containment;
- plan versus occurrence state;
- source/claim lineage and honest counts;
- contribution attribution and current authority;
- contextual map only when spatial structure matters;
- a context-preserving Chat door.

Exit: no root entry or search result terminates in a dead end or a competing
legacy object.

### 5. Add Returns and cross-root arbitration as one read-side policy

1. Represent candidates by foundation object, evidence dependencies, dominant
   job, material trigger, authority footprint, and freshness.
2. Implement the deterministic gates and suppression stack from the arbitration
   policy as a pure replayable function.
3. Persist candidate identity/lineage only where needed; do not mint a new
   durable object when its dominant job flips.
4. Have Home, Places, and Life consume the same seat decision so duplication is
   impossible by construction.
5. Begin with the corrected record-native comparison/explanation family; add
   other families only after their fixtures pass the same bar.

Exit: the ten arbitration fixtures pass, including silence, yield, withdrawal,
and same-identity recompilation.

### 6. Add contribution, Together, and causal repair

1. Resolve Chat gestures through the contribution contract: Ask, Observe,
   Source, Invite, Correct, or authorized Action.
2. Return immediate value first; create a receipt only after a durable mutation.
3. Store addressable claim/relation identity and the five authority axes so
   grants can be narrowed without deleting unrelated truth.
4. Project attributed shared records into existing Life objects—never a social
   inbox.
5. Make correction, undo, withdrawal, and blocking invalidate dependent root,
   dossier, search, and Home/Places projections before the next read.

Exit: the accepted board 21 and 24 sequences run end to end against real state,
including causal repair and viewer-relative blocking.

### 7. Validate and replace, then retire legacy Atlas deliberately

- Add content-free telemetry for projection failures, stale authority, count
  mismatches, duplicate seats, correction propagation, and destination dead
  ends—not engagement ranking.
- Run real-device VoiceOver, Dynamic Type, touch-target, interruption, offline,
  and partial-data checks.
- Dogfood with the Europe-return and ordinary-NYC fixtures, then real records.
- Expand the flag only when the acceptance contract is green.
- Retire Atlas components and handwritten mirrors only after route parity and a
  recoverable migration are verified.

## Recommended solo-founder order

Work one vertical dependency at a time: **contract closure → read projection →
native root → destinations/refinding → arbitration → contribution/Together**.
Keep each child-repository commit independently testable and land API changes
through the workspace sync workflow. Do not parallelize visual density, new
Return families, or generalized object architecture ahead of the destination
and authority seams they depend on.

## Commit-sized checkpoints

1. Workspace: repair operation registry and regenerate contracts.
2. Backend: Life root response models + fixture projection tests.
3. Mobile: dedicated flagged Life route + static states.
4. Mobile: bind real projection + object-handle navigation.
5. Backend/mobile: refind generated types + canonical destinations.
6. Backend: arbitration policy + ten golden fixtures.
7. Backend/mobile: shared seat consumption across roots.
8. Backend: addressable contribution/grant/repair primitives.
9. Mobile: Together and contribution sequences against live state.
10. Workspace: end-to-end certification and flag decision.

## Verification commands

Run from the workspace root as each relevant checkpoint lands:

```bash
make contract-check
make typecheck
make test-backend
make test-frontend
make doctor
```

Also require focused replay fixtures for Life root states, the refinding
benchmark, the ten arbitration scenarios, withdrawal/blocking, and correction
propagation. A green unit suite without a device walk is not release proof.
