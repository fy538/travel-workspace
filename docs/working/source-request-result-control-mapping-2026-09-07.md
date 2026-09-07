---
doc_type: working
status: active
decision_status: proposed
owner: Integration / Contribution and Capture
created: 2026-09-07
last_verified: 2026-09-07
expires: 2026-10-07
why_new: Makes the SP-0a request, result, and control boundaries executable without inventing a second store or claiming exact result support that does not yet exist.
supersedes: []
---

# Source request, result, and control mapping — 2026-09-07

Status: **implemented mapping / contract-sensitive gaps isolated**

This is the SP-0a companion to the complete-system integration roadmap. It
maps the existing private Source preparation path without introducing a second
request store, inbox, or generated-content owner. It is deliberately precise
about what exists today and what is only a proposed interface.

## 1. The three identities stay distinct

| Identity | Current owner | Meaning | Can it be used as the other two? |
| --- | --- | --- | --- |
| Request identity | The authenticated request owner, currently carried as a `ResourceRef(kind="source_preparation_request")` in workflow metadata | Who asked for which bounded job and which accepted purpose/scope it refers to | No. A conversation or message ref alone is not a readable purpose contract. |
| Semantic reuse identity | `SourceContributionWorkItemV1`'s deterministic `work_id` / Source group key | Which governed viewer, evidence/context, roots, audience and policy/compiler versions may reuse one production | No. Reuse identity does not prove who requested it or authorize exact retrieval. |
| Result identity | **Not yet complete.** Today the receipt points to `source_contribution_workflow_status:{workflow_id}` and the current Source group row is the only durable production locator | The exact published production/version that a requester may reopen | No. A group key can be overwritten and therefore cannot promise an immutable historical result. |

The existing `agent_workflows` row remains the lifecycle/control owner. Generated
prose and candidates remain under Source production storage. `result_json` and
the receipt must remain content-free.

## 2. Existing field map

| Requested meaning | Existing representation | Durable location | Revalidated by |
| --- | --- | --- | --- |
| Actor / viewer | `SourceContributionWorkItemV1.viewer_id`; `AgentWorkflow.actor_id` | Work item + workflow row | Canonical executor actor fence |
| Accepted purpose | `trigger=explicit_warm` plus `request_ref` kind | Work item + `agent_workflows.request_json.request_ref` | Explicit submission adapter; no semantic request owner exists yet |
| Exact subjects | **Missing from the current Source work item** | — | — |
| Optional source refs | Only `trigger_ref` / `context_ref` opaque refs | Work item | Trigger/context kind and owner resolver where supported |
| Requested time/context clock | `represented_at`, `timezone_name`, optional Places `context_ref` | Work item | Worker expiry gate and canonical context resolver |
| Permitted roots | `allowed_roots` | Work item + deployment envelope | Worker deployment and Source continuity |
| Audience / use | `audience` | Work item | Source admission and root serving |
| Replay key | `idempotency_key`, derived from the bounded work identity | Workflow row | `create_or_get_workflow` |
| Accepted deadline | `expires_at`; worker lease is separate | Work item + workflow lease | Worker clock, completion fence and Source persistence |
| Output validity | Source candidate expiry plus current source/context custody | Source production row | Shared Source serving/admission |
| Result ref | Status-shaped workflow ref only | Completion receipt | Workflow read route |
| Effective stop | Generic `agent_workflow_commands` intent; `cancel_workflow` exists but is not connected to Source route | Command row / workflow row | **SP-2b** |

## 3. What the current path actually supports

The canonical Source executor is an **explicit contextual warm** path. It can
re-read the viewer's eligible private material, compile a bounded production,
write it through the existing Source attempt/output transaction, verify a
canonical readback, and publish a content-free workflow receipt. It does not
yet implement a commissioned comparison with an exact subject set.

That distinction is important:

* “Prepare something worthwhile from my current private context for Home and
  Places” is representable by the current work item.
* “Compare the Colosseum and the Acropolis for my Saturday afternoon” needs
  exact subject refs, purpose, and a request owner that can be re-read on
  retry and exact-result retrieval. It must not be silently treated as a
  contextual warm job.
* Contextual discovery (“find something nearby that fits”) is also a different
  ingress from an exact commissioned comparison. It may use the same receiving
  boundary later, but it does not inherit exact subjects by implication.

## 4. Proposed narrow extension (not adopted yet)

If an existing Chat/action owner cannot supply the missing semantics, the
minimum additive contract should be a versioned, content-free request record
owned by the existing authenticated ingress—not a new global store:

```text
source_preparation_request.v1
  request_ref
  actor_id
  purpose: contextual_warm | exact_comparison | public_discovery
  subject_refs[]
  source_refs[]
  represented_at + timezone
  context_ref + context_revision (optional)
  allowed_roots
  audience/use
  accepted_deadline
  output_valid_until
  replay_key
```

The Source work item may carry an opaque `request_ref` and the immutable
execution fields derived from this record. It should not duplicate private
conversation text or generated prose. The request owner must be able to answer
“what was asked, by whom, with which exact subjects and scope?” after a retry.

This extension is **decision/contract-sensitive** and is intentionally not
implemented by this mapping commit. The current explicit submission adapter
continues to reject non-`explicit_warm` triggers and does not claim support for
an exact comparison.

## 5. Examples and truthful lifecycle

### Accepted by the current path

```text
request_ref = source_preparation_request:abc
trigger = explicit_warm
roots = {home, places}
context_ref = places_context:rome-now
```

Result: a workflow status receipt. Once SP-1b exists, the requester will also
receive an exact versioned result locator if a useful production was actually
published.

### Rejected as under-specified

```text
request_ref = conversation:123
user_text = "compare these two places Saturday"
```

Result: reject unless the authenticated action/request owner has persisted the
purpose, exact subjects, time window and replay identity. Conversation
membership is not a substitute for request custody.

### Replayed

The same request ref, semantic work identity, and accepted deadline replay the
same workflow/result. A changed exact subject, context revision, purpose,
audience, policy/compiler version or replay key creates a new semantic identity;
an expiry refresh does not silently extend a running job.

### Result states (target shape)

| State | Meaning | Current support |
| --- | --- | --- |
| `pending` / `running` | Accepted handoff has not produced a terminal receipt | Existing workflow projection |
| `ready` | Useful produced/reused output is durably linked to an exact result identity | Worker verifies production, but exact result binding is SP-1b |
| `no_useful_result` | Canonical owner path completed without admitted production | Worker has `producer_silence`; route projection needs mapping |
| `failed` | Technical or contract failure with truthful retryability | Existing workflow failure states |
| `cancelled` | Effective workflow cancellation won the race | `cancel_workflow` exists; Source control wiring is SP-2b |
| `replaced` / `expired` / `unavailable` | Exact result is no longer eligible or was superseded | Exact reader and version/digest binding are SP-1b |

## 6. Dependent implementation gates

1. **SP-1b:** return and durably bind a versioned result identity/digest at the
   Source publication boundary; provide actor-authorized exact retrieval that
   shares ordinary serving validation and never acquires on GET.
2. **SP-2b:** connect an authenticated Source owner stop to `cancel_workflow`
   with a transaction-time ownership/revision check; keep generic command intent
   semantics unchanged for other workflow types.
3. **SP-3a:** deliver the same admitted result through Home and Places while
   preserving exact requester access independent of ranking.

Until those gates land, the status-shaped receipt is honest and the Source
worker remains dark. No client or roadmap should call the current status ref an
exact content result.
