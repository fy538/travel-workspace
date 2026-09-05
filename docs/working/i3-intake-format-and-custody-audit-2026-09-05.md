---
doc_type: working
status: active
owner: strategy integration / contribution and capture
created: 2026-09-05
last_verified: 2026-09-05
expires: 2026-10-05
why_new: Records the I3 format and custody boundary from the actual mobile and backend paths before any new document-family adapter is approved.
source_of_truth_for:
  - I3 intake format support and truthful fallback boundary
depends_on:
  - complete-system-integration-roadmap-2026-09-05.md
  - ../working/contribution-contract-and-legacy-memory-migration-plan-2026-08-29.md
  - ../systems/contribution-and-consequence.md
---

# I3 intake format and custody audit

This is an implementation audit, not a proposal to widen the intake
portfolio. It answers one bounded question: what can the current product
accept, retain, interpret, and render honestly at each entry path? A format is
not supported merely because a lower-level picker or generic image helper can
read it. The custody boundary and its recoverable user treatment are the
product contract.

## Current result

| Input family | Entry / custody path | Interpretation / rendering path | Current status | Required user treatment |
| --- | --- | --- | --- | --- |
| Plain text / URL | Share-capture text branch → `useSubmitIntakeText` → verified custody → interpretation poll → Chat/subject handoff | Text source and derived candidates use the existing source/candidate contract | Supported for the current intake contract | Admit useful value first; preserve original and exact source lineage |
| JPEG / PNG / supported WebP image | Share-capture v2 → custody-first multipart submission → verified custody → interpretation poll | Source and accepted candidates can be retained and addressed to an explicit subject | Supported, subject to scanner/custody result | Show receipt, partial interpretation, retry, correction, and source return honestly |
| Audio | Share-capture audio branch → custody/worker path | Existing audio intake and pending Chat handoff; no new format claim in this audit | Existing path; not widened here | Preserve pending/failed state and return to the originating conversation when present |
| HEIC / HEIF from share intake | Native share payload can arrive, but intake-v2 admission rejects it before normal custody | No ordinary interpretation claim is made | Intentionally unsupported at the intake boundary | Say HEIC/HEIF intake is not enabled; suggest JPEG/PNG export or original text; permit retry without losing the physical share |
| PDF | Intake-v2 admission rejects it before custody | No document scanner or page-renderer contract exists | Intentionally unsupported | Explain that PDF is not enabled; do not create a false source or generic success receipt |
| Apple Wallet / PKPass | Intake-v2 admission rejects it before custody | No ticket extraction/normalization owner exists | Intentionally unsupported | Explain the missing document path; keep the fallback actionable and non-destructive |

## Evidence in the current checkout

### Mobile admission and recovery

- `travel-app/app/share-capture/index.tsx` uses the custody-first v2 branch for
  files and preserves capability errors containing `HEIC/HEIF intake is not
  enabled`, scanner requirements, and supported-count limits. These are not
  collapsed into a generic network error.
- `travel-app/__tests__/screens/share-capture-intake-v2.test.tsx` covers a
  successful image custody submission, a retry of the same physical share,
  local PDF/Wallet/HEIC rejection, server-side HEIC rejection, quarantined
  custody, relaunch by submission id, and a deliberate Place subject.
- `travel-app/__tests__/data/intakeV2Resumability.test.ts` asserts that PDF,
  Apple Wallet, and HEIC/HEIF do not create a custody record while resumable
  submissions retain their canonical path and custody revision.
- `travel-app/components/chat/ComposerBar.tsx` may decode a device-picked HEIC
  for the ordinary Chat image path. That lower-level picker capability is not
  evidence that share-capture intake supports HEIC; the two paths remain
  deliberately separate until a common scanner/conversion owner exists.
- `travel-app/utils/imageUploadGuard.ts` admits HEIC/HEIF for generic image
  upload. This is a component-level upload guard, not the intake-v2 product
  contract and must not be copied into share-capture admission without a
  custody and server-normalization decision.

### Backend boundary

- The intake security/custody contract rejects PDF, Apple Wallet/PKPass, and
  HEIC/HEIF before normal interpretation. The existing mobile error copy is
  therefore an accurate capability limit, not a temporary UI omission.
- Existing source retention and candidate resolution remain source-bound. A
  rejected file never becomes a fake `SourceRef`, memory claim, intent, or
  social contribution.

## Decisions for this roadmap

1. **Keep the unsupported boundary.** Do not add a PDF parser, Wallet reader,
   or HEIC conversion dependency in I3 without a separately named owner for
   security scanning, normalization, source custody, original retention,
   derived lineage, and native acceptance.
2. **Keep generic Chat image support distinct.** A picker conversion that makes
   a Chat image usable does not silently authorize share-extension intake or
   document interpretation.
3. **Treat partial success as value.** A verified original with interpretation
   pending is a useful result; a failed scanner or unsupported format is a
   recoverable capability state. Neither should be represented as a completed
   semantic artifact.
4. **Require one owner before widening.** A future format adapter must specify
   the accept/normalize/render owner, source and derivative references, expiry
   and deletion behavior, correction/readback, supported native entry paths,
   and a user-visible fallback before code or a generated API type is added.

## Exit evidence and remaining work

The current I3 format boundary is **implemented and locally tested** for the
supported and rejected cases above. It is not native end-to-end evidence and
does not claim a document-family rollout. Remaining I3 work is independent:

- controlled native/share-extension receipts for supported text, image, audio,
  and multi-file payloads;
- interrupted-finalize and relaunch evidence with the same custody identity;
- an owner ADR if PDF, Wallet, or HEIC/HEIF support becomes a product priority;
- the separate audit of reflection/background/synthesis writers; and
- approved personal-intention and attributed-contribution commands.

Until those decisions land, the semantic renderer and source-derived
consequences must continue to distinguish supported intake, verified-but-
pending custody, quarantined failure, and unsupported format.
