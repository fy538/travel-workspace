---
doc_type: working
status: active
decision_status: proposed
owner: Integration / Contribution and Capture
created: 2026-09-07
last_verified: 2026-09-07
expires: 2026-10-07
why_new: Maps Source request semantics, implemented exact-result retrieval and cancellation, and the remaining authenticated-ingress and consumer boundaries.
supersedes: []
---

# Source request, result, and control mapping — 2026-09-07

Status: **mapping rebaselined after SP-1b/SP-2b / request extension still proposed**

This is the SP-0a companion to the complete-system integration roadmap. It
maps the existing private Source preparation path without introducing a second
request store, inbox, or generated-content owner. It is deliberately precise
about what exists today and what is only a proposed interface.

September 7 rebaseline: exact result binding/retrieval and Source-specific
effective cancellation are implemented in `381bbba29` and `1447eeccd`, with
subsequent hardening through `1961eebff`. The
[execution receipt](source-connected-value-execution-receipt-2026-09-07.md)
owns their verification. The request owner, runnable ingress and mobile result
consumer remain incomplete. This correction adopts no new request schema or
retention policy. The next execution order is
[integration roadmap §9.8](complete-system-integration-roadmap-2026-09-05.md#98-connected-system-next-stage--september-7-holistic-rebaseline).

## 1. The three identities stay distinct

| Identity | Current owner | Meaning | Can it be used as the other two? |
| --- | --- | --- | --- |
| Request identity | The authenticated request owner, currently carried as a `ResourceRef(kind="source_preparation_request")` in workflow metadata | Who asked for which bounded job and which accepted purpose/scope it refers to | No. A conversation or message ref alone is not a readable purpose contract. |
| Semantic reuse identity | `SourceContributionWorkItemV1`'s deterministic `work_id` / Source group key | Which governed viewer, evidence/context, roots, audience and policy/compiler versions may reuse one production | No. Reuse identity does not prove who requested it or authorize exact retrieval. |
| Result identity | Source completion receipt carries `ResourceRef(kind="source_contribution_result", id=workflow_id, revision=production_digest)`; the owner-only `/api/agent-workflows/{workflow_id}/result` reader resolves it | The exact published production/version while its retained row, Sources and context remain eligible | No. Status, request and result refs remain distinct; overwritten or expired output is unavailable, not an immutable archive. |

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
| Result ref | Versioned `source_contribution_result` ref and canonical production digest; status ref remains separate | Completion receipt + existing Source production row | Actor-authorized exact-result route and shared current Source/context validation |
| Effective stop | Source-only cancel command calls `cancel_owned_source_workflow` behind the existing workflow-control flag | Applied command + workflow state in one transaction | Actor/type/control-revision checks at mutation time; other workflow commands retain their existing semantics |

## 3. What the current path actually supports

The canonical Source executor is an **explicit contextual warm** path. It can
re-read the viewer's eligible private material, compile a bounded production,
write it through the existing Source attempt/output transaction, verify a
canonical readback, and publish a content-free workflow receipt. It does not
yet implement a commissioned comparison with an exact subject set. No runtime
caller of `create_explicit_source_contribution_workflow` or worker registration
was found at this rebaseline. The examples below describe the adapter's
representable inputs, not a currently offered end-user service.

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

Result: when an authorized caller explicitly runs the current adapter/executor,
the workflow exposes status and can carry an exact versioned result locator
after useful production/readback. A normal mobile request does not yet invoke
that complete path. The result reader remains declared dark without a mobile
consumer.

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

### Result states (current wire support and remaining semantics)

| State | Meaning | Current support |
| --- | --- | --- |
| `pending` | Work has no terminal receipt | Exact reader returns `pending` with the workflow state in `reason`; running is not a separate result status |
| `ready` | Useful produced/reused output is durably linked and currently eligible | Implemented exact digest/ref validation and Source/context readback |
| `no_useful_result` | Execution ended without admitted production | Implemented for a completed `producer_silence` workflow when its content-free status reference is valid; a malformed or missing reference remains `unavailable` |
| `failed` | Terminal technical or contract failure | Exact reader maps `failed_terminal`; retryable nonterminal work remains pending |
| `cancelled` | Effective workflow cancellation won the race | Implemented Source-specific mutation and exact-reader status; inspect owner state rather than generic command acceptance |
| `unavailable` | Exact result is missing, replaced, expired or no longer authorized for current use | Implemented with reason codes; replacement/expiry are not distinct top-level wire statuses |

## 6. Dependent implementation gates

1. **SP-0a/SP-1 remainder:** select the authenticated request owner and bind
   purpose, exact subjects where requested, time window, authority, deadline and
   replay semantics. Reuse existing workflow/custody infrastructure; review the
   proposed extension before claiming commissioned comparisons.
2. **SP-2/SP-3 remainder:** connect an executable ingress and truthful ending
   states, including no-useful-result, to the existing exact reader and stop
   path. Verify accepted work can actually run before exposing acceptance.
3. **SP-3a:** add the generated mobile consumer and supported result destination;
   preserve requester access independently of Home ranking, plus current
   source/context expiry and account isolation. Ordinary prepared Home/Places
   serving already exists; do not implement it again.
4. **SP-5:** evaluate one connected local request/execution/readback/result/root
   portfolio before any separate worker/provider activation. Current exact
   reads can require the original eligible context; independent partial results
   need explicit dependency support before that restriction can be relaxed.

The Source worker remains dark because ingress, request semantics, consumer
delivery and activation evidence are unfinished. Exact backend result retrieval
and Source cancellation are no longer missing foundations.
