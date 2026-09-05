---
doc_type: working
status: active
owner: founder / Strategy integration task
created: 2026-09-05
last_verified: 2026-09-05
expires: 2026-10-05
why_new: Records the current owner boundaries and missing runtime joins for the lived-experience engine before new watches, producers, or shared writers are added.
supersedes: []
source_of_truth_for:
  - I0 live-engine owner inventory and observation-to-consequence path matrix
  - Strategy-side readiness and integration decisions for lived-experience families
depends_on:
  - ../systems/four-root-loop-object-surface.md
  - ../systems/contribution-and-consequence.md
  - ../../travel-agent/docs/working/lived-experience-integration-engine-execution-plan-2026-08-16.md
---

# Live-engine owner and path matrix

This is the I0 execution artifact for the complete-system integration roadmap.
It answers a narrow question before implementation expands: for each registered
lived-experience family, who owns the trigger, what current context is admitted,
where judgment happens, what can be shown, which owner may change state, how
readback is verified, and whether any production or watch is actually enabled.

The matrix is an inventory, not an activation decision. A registered adapter,
shadow evaluation, typed treatment, or mobile contract does not imply visible
behavior. Missing signals remain unknown; they do not authorize a poll, watch,
notification, location read, contact, or external action.

The stable product loop remains:

```text
authorized observation
  -> bounded context
  -> judgment or abstention
  -> treatment / silence
  -> owner consequence (optional)
  -> canonical readback
  -> outcome, correction, expiry, or release
```

## 1. Current family paths

| Family | Trigger / observation owner | Context actually admitted | Judgment and treatment | Consequence / readback owner | Delivery and activation truth | Missing join / next package |
| --- | --- | --- | --- | --- | --- | --- |
| `private_disruption` | Concierge-authorized run, turn, loaded state; a current Plan or commitment change may be an input | `concierge_authorized_run`, `turn`, `loaded`; opening and Plan revision refs; request clock | Provider-free engine admission; candidates may choose Chat, Plan, or Push; shadow policy `private_grounded_disruption_v1` | Plan/commitment domain gateway; canonical readback and causal arc contracts exist, but no general visible worker | Registered as `shadow`; no visible root or push release | Connect an authoritative revision/change event to bounded reevaluation without making every Plan read a live watch (I1/I2/I5) |
| `place_interpretation` | Entity/place-content owner or an explicit viewer read | Entity identity, accepted place-content primitive, optional relationship projection and group receipt | Read-only interpretation; treatment candidates are Places, Chat, or Home; no action is implied by an interpretation | No consequential write; source/content owner remains authoritative | `read_only`; entity presentation has the strongest current consumer, root adoption remains partial | Carry current conditions, limits, privacy, and attribution into a root-ready value candidate without lossy venue-only projection (I2/I4) |
| `foreground_movement` | Movement owner: current `MovementSession`, qualified position, route fact, timing/slack | One-clock `SituationEnvelope`; Occasion scope, Commitment identity, Plan revision, position/route freshness and movement risk | `situated_judgment.py` admits only late/leave-now/unknown operational candidates; treatment is in-context, Plan, or Chat | Existing Plan/commitment owners; no command is performed by movement judgment | `component_only`; no general foreground surface or mobile release | Join movement reevaluation to a concrete foreground consumer and stop/expiry semantics; do not infer background tracking from this adapter (I2/I5) |
| `ambient_home_attention` | Attention registry / ambient dispatch; bounded current-world signals or a retained, authorized attention item | Attention revision; optional place content and relationship projection; recipient and purpose | Home/Chat treatment selection with silence and displacement; no generic production authority | Usually no domain mutation; if a consequence exists it must route through a named owner gateway | `producer_specific`; ambient cycle exists but no general production caller is enabled | Separate useful complete-on-view Home value from any watch; name the producer, budget, and cancellation owner before enabling (I2/I4/I5) |
| `notification_treatment` | Attention owner plus an expiring situation signal | Attention revision and situation envelope; effective audience, quiet/receptivity and delivery policy | Push or Chat treatment arbitration; notification arbiter owns dedupe and delivery outcomes | Domain gateway only when an explicit action is authorized; receipt/readback remains domain-owned | `family_gated`; mature push machinery is not proof this family is enabled | Prove signal-to-judgment freshness, no-change suppression, and stop/expiry behavior; never use push as the live engine itself (I2/I5) |
| `shared_plan_repair` | Canonical Plan revision plus group constitution / safe-option receipt | Itinerary revision, group decision constitution, optional situation, group-safe options and receipt | Proposal-oriented judgment; Home, shared proposal, or Chat treatment; preserves plural participation | Canonical Plan proposal/commit path and verified readback; no surface may write Plan state | `canonical_proposal_path`; proposal contract exists, visible cross-root adoption remains partial | Connect current condition changes to purpose-preserving alternatives and receipts without turning every arrangement into an itinerary editor (I3/I5) |
| `encounter_confirmation` | Explicit viewer confirmation or a relationship/place observation requiring confirmation | Viewer-relative place relationship projection and optional expiring situation | Private confirmation treatment in Places, Chat, or context; abstains when relationship evidence is insufficient | Relationship/occurrence owner; confirmation must be explicit and correction-capable | `explicit_confirmation`; no inferred attendance or meaning | Define the exact confirmation command/readback and how a later correction removes dependent interpretations (I3/I5) |
| `later_occasion_application` | An authored relationship/outcome signal is considered for a later Occasion | Place relationship projection plus an experience outcome, both revision-bound | Narrow in-context, Places, or Chat application; independent participation is preserved | Occasion/relationship owner; later-use receipt must identify source and audience | `narrow_adapter`; not a general recommendation or social feed | Specify adoption/withdrawal semantics and prevent a derived suggestion from becoming a new authored fact (I3/I5) |
| `addressed_place_handoff` | A person deliberately addresses a place note or place-specific contribution to a recipient | Canonical place entity ref, source-bound trace, recipient address authority, delivery permission | Explicit-confirmation Chat/Places/Home treatment; attribution and audience stay visible | Relationship handoff/delivery owner; delivery readback and withdrawal are authoritative | `explicit_confirmation`; strongest current multiplayer seam, still not a general social publisher | Complete the capture-to-addressed-material return path and cross-root invalidation without creating response debt (I1/I3/I5) |

## 2. Shared path stages and current owner

| Stage | Current owner / evidence | What is safe now | What is not yet proven |
| --- | --- | --- | --- |
| Observe / admit | Family registry, context requirements, `judgment_admission`, movement and attention owners | Typed freshness, privacy, attention burden, and abstention can be evaluated in shadow or read-only paths | A registry entry does not establish a real trigger stream or a durable watch |
| Compose context | Situation envelope, Plan/Occasion/Commitment reads, place relationship projection, Concierge authorized state | One request clock and bounded owner reads are now enforced for the Home graph path; owner-specific revisions remain visible | No universal cross-domain snapshot; repeated readers and scenario-derived operation plans still need convergence |
| Judge | Provider-free lived-experience coordinator plus family adapters | Treatment candidates, silence, posture, and causal lineage are typed | Production value and live reevaluation are not the same as shadow judgment; no model call belongs on ordinary root response paths |
| Treat | Surface treatment identity, root composition, notification arbiter, Chat/Places/Home contracts | A treatment can be bounded, attributed, and fail closed | The same treatment identity is not yet rendered/recorded consistently across all roots |
| Consequence | Named domain gateway: Plan, relationship, occurrence, or other canonical owner | Opaque grants, owner routing, readback, repair, and receipts exist for selected paths | There is no universal consequence gateway, and no adapter may invent one to make a family look complete |
| Monitor / reevaluate | Existing specialized workers, ambient checkpoint machinery, movement/session owners | Reuse/lease, expiry, cancellation, and shadow checkpoint primitives exist in parts | No approved general watch owner; no always-on scheduler; signal-to-judgment budgets are not yet measured end to end |
| Reconcile / carry forward | Occurrence/outcome authorities, Life corpus, source custody and correction paths | Life depth revisions and direct-read invalidation are advancing independently; causal repair contracts exist | Cross-root dependent-result repair and later-occasion adoption still need an integrated acceptance portfolio |

## 3. Decisions that gate the next implementation packages

### D1 — No universal manifest or second owner

Keep the pure decision contracts, situation envelope, owner-read portfolio, and
family adapters. Do not add a new universal context/object service. A new
contract is justified only when two existing owners need a stable boundary that
cannot be expressed by their current typed refs, revisions, audience, purpose,
or readback receipt.

### D2 — Readiness must be executable

`route.evaluate` is currently catalogued and bound to an owner-read registry,
but its canonical reader returns `canonical_route_reader_not_available` and
place reads omit current-condition/reachability fields. Until a real owner and
field contract exists, generic root plans must not spend routine budget on the
known-unavailable operation. The next change should be a readiness/field
coverage gate, not a speculative route service.

### D3 — Request clock is necessary but not a snapshot

Every root read and derived candidate must share the represented-at clock and
retain owner revisions. This prevents expiry/posture drift without pretending
that independently read owners form an immutable database snapshot.

### D4 — Watches require an exact owner

Before any `WAIT_FOR_SIGNAL` or `MONITOR` path becomes durable, record subject,
condition, source/refresh policy, purpose, audience, permitted action, expiry,
cancellation, last evaluation, and delivery/readback owner. Normal Keep,
browsing, sharing, and mention remain complete-on-view unless the user or an
authorized owner explicitly establishes that contract.

### D5 — Production is separate from judgment and serving

Optional source contribution production may be reused or produced in a bounded
worker. It must not block an ordinary Home/Places response or create a second
meaning for one semantic candidate. Delivery identity can be root-neutral only
when purpose, audience, source revisions, context, and policy are equivalent.

### D6 — Surface promotion is explicit

Home/Places native renderers, generated API vocabulary, server candidate kinds,
and mobile conformance are three different scopes. Promote a kind only after a
named producer, typed payload/anatomy, renderer, return route, exposure/readback,
and acceptance fixture exist. Do not broaden the renderer registry merely to
silence an unsupported-kind finding.

## 4. Receipts and next package

Already-landed continuity receipts that this matrix consumes:

- `travel-app` `2d30015c5`: root consequence resolution invalidates direct Life
  record-page readers as well as Home/Places/Life roots.
- `travel-agent` `e0d0f52d1`: the bounded Home experience-graph read receives
  the root request clock.
- The concurrent Life lane has since advanced its cursor/revision and direct
  history work; this matrix does not reassign those files.

The next bounded implementation package is **I2 readiness and serving**:

1. add an executable readiness/field-coverage result to owner-read planning;
2. omit routine known-unavailable work such as `route.evaluate` from production
   root budgets while retaining truthful limitation evidence;
3. measure optional source production separately from fast root assembly; and
4. add focused tests for practical value surviving unavailable enrichment.

Do not add watch persistence, a general scheduler, a new route owner, or a
second Home/Life producer in that package. Reassess after the package against
latency, cost, usefulness, and the live-engine invariants before proceeding to
I3 shared material or I4 surface promotion.
