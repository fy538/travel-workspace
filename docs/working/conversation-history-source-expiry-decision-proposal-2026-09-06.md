---
doc_type: working
status: active
decision_status: proposed
owner: founder / Contribution and Capture / Integration
created: 2026-09-06
last_verified: 2026-09-06
expires: 2026-10-06
why_new: Resolves one review boundary for conversation history, transient source derivatives and optional later reuse without silently expanding the accepted Ask contract.
supersedes: []
---

# Decision proposal: conversation history, source expiry and optional continuity

## Status and recommendation

**Proposed, not adopted or implemented.** Creating this document does not
authorize new retention, retrospective reuse, deletion or a migration. The
[contribution contract](../systems/contribution-and-consequence.md) remains
authoritative: Ask creates no new durable personal state; raw Ask processing
sources expire after processing, with at most 24 hours of technical retry
custody; session working context expires after 24 hours of inactivity.

**Recommend separating three permissions:** conversation-history display,
source/derivative custody, and use in a later context. A record stored for one
does not acquire the other two. Keep optional cross-session conversational
continuity **unadopted** for this implementation batch; it remains a future
opt-in proposal, not something enabled by continued use or inferred interest.

This document supplies the missing CC-2 decision packet and refines Integration
D4's implementation dependency. D4's five-axis policy is settled; the treatment
of history copies and their derivatives still needs this explicit resolution.

## Proposed treatment by material

| Material | Proposed history/custody treatment | Later use and repair |
| --- | --- | --- |
| Person-authored text | Ordinary conversation history only under its existing, explicit account/history policy; no new duration is granted here | History storage is not memory admission. Deletion and context exclusion remain effective |
| Independent assistant explanation | May remain readable under that same history policy if it does not reconstruct expired/released source content | No automatic indexing into Life, preference synthesis or Home production |
| Raw Ask attachment and processing copies | Transient, including copied Chat images, OCR/extracted text and transcripts when source-derived | Enforce processing-end/expiry at read and prompt assembly before eventual cleanup; retries never renew authority |
| Source-dependent generated answer | Dependency-aware treatment; no blanket exemption for prose | Redact/withhold source-dependent portions when eligibility ends; retain only independently supportable explanation and a minimal unavailable-source marker |
| Deliberately retained Bring/Keep original | Its own custody policy; history holds an authorized ref rather than an independent permanent copy | Source controls govern derivatives and eligible reuse; conversation deletion is not automatically deletion of an independently retained original |
| Human-authored claim independently retained under explicit authority | Its named owner and scope, distinct from the original attachment | Repair causal dependencies without deleting independent claims or widening purpose |
| Minimal tombstone/receipt | Content-free identity/status needed to explain unavailability and prevent replay | Cannot preserve enough text, embeddings or media to reconstruct released content |

Do not infer the gesture from MIME type or the presence of `chat_images`.
“What does this ticket say?” and “Keep this ticket” use different authority.
An authored message that deliberately contains quoted material requires its own
custody classification; do not blindly delete all user-authored text or retain
all copied source text under a history label.

An expired attachment should not make unrelated conversation vanish. Conversely,
keeping a generated transcription in history must not defeat source expiry.
Where existing storage cannot distinguish answer spans, withhold the whole
source-dependent answer from future model use and use a minimal display marker
until an approved representation can safely separate it. Do not run a model
over released material to reconstruct a replacement.

## Existing implementation gap

[`chat_images.py`](../../travel-agent/backend/core/db/chat_images.py) stores
images for conversation use and now cleans up files on row-write failure.
Its [model](../../travel-agent/backend/core/models/chat_images.py) has no
explicit custody-purpose or expiry field. Transactional cleanup is therefore
not complete lifecycle enforcement. The [CC execution receipt](contribution-contract-and-legacy-memory-migration-plan-2026-08-29.md#116-execution-receipt--september-5)
also records intake deadline preservation and useful-first facts, not a fully
implemented history/source distinction.

Implementation must inventory every copy and consumer: original, thumbnail,
extracted text, transcript, message metadata, summaries, caches, pending jobs,
generated results and future prompt assembly. Reuse existing source identity and
policy fields where possible; do not introduce a second source-custody owner.

## Optional continuity: policy not adopted

The [September 6 strategy decision](../decisions/2026-09-06-reconcile-consumer-strategy.md)
accepts optional ordinary-conversation continuity as intended product behavior,
not this proposal's material, duration, migration or source-expiry choices.
Manual Keep should not be the only eventual continuity path. Current Ask/T0
rules remain in force until a separate policy amendment is accepted.

Evaluate history readability explicitly: independent explanations should remain
available where permitted; source-dependent answers must not reconstruct
released material; unrelated conversation should not disappear. User testing
must include returning to an answer after attachment expiry, not only whether
a source can enter a future prompt. None of this authorizes new custody or
retroactive reuse.

Ordinary questions must still be useful on their own. Already authorized
context may improve an answer within its scope. Neither requires retaining
every new question or turning a topic into a person claim.

A future opt-in must explicitly settle all of the following before adoption:

- What is retained and for how long; whether selection is prospective only.
- Which later answers, Home/Places contributions or retrieval may use it.
- Sensitive and third-party exclusions, inference limits and subject scope.
- Inspection, correction, exclusion, opt-out and deletion behavior.
- Treatment of previously produced derivatives and running jobs on revocation.
- A comprehensible agreement without per-question memory-management homework.

Do not preselect an opt-in, backfill from historical Chat, equate enabling
history with continuity, or broaden audience/action permissions. This proposal
does not choose a new retention duration or deploy a continuity preference.

## Delivery ownership after adoption

| Lane | Responsibility |
| --- | --- |
| Contribution and Capture | Lifecycle classification, copy inventory, read rejection, prompt-use filtering, cleanup and exact receipts |
| Integration | Shared dependency events, late-production suppression and cross-consumer verification |
| Life | Only eligible retained sources/claims; withdrawal in index and exact readers; no ambient history scan |
| Home / Places / Entities | Revalidate source-dependent results and cached material; preserve independent owner truth |
| Strategy / founder | Approve the policy and any later continuity agreement; do not mark implementation shipped |

Recommended execution: define the minimal lifecycle binding; implement request-
time denial and worker revalidation; then bounded cleanup with audit and retry.
Do not start by deleting historical files. Existing rows with unknown authority
need a non-destructive classification/inventory and a separately reviewed
migration. Unknown reuse eligibility must not silently become a grant.

Verify Ask/Bring differences, processing completion, expiry, retries, revocation
mid-job, no reconstruction from derivatives, exact source deletion versus
conversation deletion, preserved independent history and account isolation.
No UI redesign, native test session or production cleanup is authorized here.

## Approval and tradeoff

Approve or revise the material-by-material policy before implementing CC-2's
history-specific migration. The recommended separation preserves useful history
without turning it into hidden long-term memory; dependency-aware answer repair
is extra implementation work, not a promise the current model already fulfills.
On approval, publish an accepted decision and update the owning contribution
contract. Until then, this remains one bounded proposal, not a new roadmap.
