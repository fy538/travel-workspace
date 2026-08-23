---
doc_type: working
status: active
owner: founder / product / architecture / engineering
created: 2026-08-23
last_verified: 2026-08-23
expires: 2026-09-22
why_new: Records the first M2 admission-to-immediate-utility vertical slice over the existing Intake v2 custody and pending Vesper conversation authorities.
supersedes: []
promotes_to: null
source_of_truth_for: [m2-admission-situated-context]
---

# M2 admission and situated-context execution receipt

> Status: M2 has started. The admitted-source conversation seam is implemented
> locally; the ContextManifest provider set and richer result treatment remain
> the next M2 packets.

## 1. Selected vertical slice

The first slice is intentionally narrow and uses the authorities already in
production code:

```text
text / image / audio share (from_chat opt-in)
  -> Intake v2 custody + idempotency
  -> content-free SourceRef list
  -> durable pending Vesper turn
  -> personal conversation handoff
  -> canonical conversation send
  -> optional source-bound answer, with answer-only retention by default
```

This is not a new admission table, a second conversation writer, or a second
semantic interpreter. Intake still owns custody and deletion; the pending-turn
service still owns process-death recovery and conversation admission.

## 2. Contracts landed

`travel-agent/backend/core/models/admission.py` defines:

- `SourceRef` (the existing content-safe receipt identity, reused rather than
  duplicated);
- `AdmissionEnvelope` — actor, origin, audience, source kind, idempotency key,
  source refs, immediate job, and requested retention; and
- `AdmissionResult` — custody state, treatment, optional consequence state,
  correction destination, and expiry.

`PendingChatTurnCreate` now accepts identifier-only source refs plus
`source_kind`, `immediate_job`, and `requested_retention`. The existing JSONB
pending-turn payload stores the envelope/result so no migration or parallel
durable noun is introduced. The response exposes only source identities and
receipt state; it never exposes admitted bytes.

## 3. Authority and privacy behavior

- The pending-turn route verifies every Intake submission/source-object ref is
  owned by the actor and is not deleted, failed, or quarantined.
- A source-bound turn cannot fall back to the legacy process-local handoff when
  the durable pending-turn endpoint is unavailable.
- At canonical send, verified Intake image objects are loaded from private
  custody, bounded to four vision images, and passed to the existing
  conversation writer. The source is not uploaded or interpreted again through
  Intake.
- Source refs are stamped into server-built turn metadata so the conversation
  message and any later source correction share one lineage. Inline text is
  read from the verified Intake source object at canonical send; it is not
  copied into the pending-turn outbox.
- Pending turns retain `answer_only` by default and expire after the existing
  24-hour pending-turn TTL. Intake deletion/correction remains the owner
  release path; no Plan, Place, Occasion, attendance, or memory is inferred by
  this seam.

## 4. Mobile continuation

`travel-app/app/share-capture/index.tsx` now supports the existing
`from_chat=1` opt-in. After Intake v2 returns a verified submission, it stages
the source refs through `admitPendingChatTurn` and replaces into the normal
Vesper pending-conversation route. Ordinary OS share behavior is unchanged and
still returns to the share-capture owner surface.

The mobile generated contract and mock client are synchronized. The mock keeps
the same source-ref fields and does not invent a separate source store.

## 5. Evidence

Backend:

- `tests/core/test_admission_contract.py` — content-free envelope/result and
  rejection of raw content fields;
- `tests/core/test_pending_chat_turns.py` — identifier-only admission and
  legacy behavior; and
- 14 focused tests passing across both suites.

Mobile:

- `__tests__/utils/pendingChatTurnOutbox.test.ts` — source-ref transport and
  no-downgrade behavior (4 tests passing);
- share-capture Intake v2 and audio screen suites (11 tests passing); and
- `npx tsc --noEmit` passing.

Contract:

- `./scripts/sync-types.sh` regenerated `docs/openapi.json`,
  `docs/openapi.app.json`, and `travel-app/utils/api/schema.gen.ts`.

Commits:

- backend `7f973e7d` — `feat(m2): bind admitted sources to pending turns`;
- backend `271bb2bd6` — `fix(m2): preserve pending-turn replay fingerprints`;
- backend `0a76d5bcb` — `feat(m2): read admitted text at canonical send`;
- backend `9dd934997` — `fix(m2): ignore inline text in image materialization`;
- mobile `d1049509` — `feat(m2): continue admitted shares into chat`;
- mobile `3558edb5` — `fix(m2): keep shared text source-bound`; and
- workspace `518e516` — `chore(m2): sync admitted-source contract`.

## 6. Remaining M2 boundary

This receipt does not close M2. The next packets must:

1. bind first-turn multimodal selection to custody without relying on a
   process-local image payload;
2. materialize admitted audio through the same source lineage, including
   resumable transcription/interpretation;
3. compile the first bounded `ContextManifest` from existing Place/time,
   movement, weather, people, Commitment, and provider ports;
4. emit a real `AdmissionResult`/answer receipt from the conversation turn,
   rather than only the pending-turn admission receipt; and
5. mount correction/release controls at the conversation/source destination
   with explicit answer-only expiry readback.

The current implementation is therefore a safe M2 foundation and one exercised
vertical seam, not evidence that every S1/S2 journey already has situated
context or cultural interpretation.
