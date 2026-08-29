---
doc_type: working
status: active
owner: product / cross-repo architecture / backend / frontend
created: 2026-08-29
expires: 2026-09-28
why_new: Extracts the minimum semantic projections, field owners, and bounded read capabilities required by the selected integrated four-root experience portfolio.
source_of_truth_for: []
---

# Minimum Four-Root Projection and Owner-Read Contracts

## Scope ruling

This contract is derived only from the selected [Integrated Four-Root
Experience Portfolio](integrated-four-root-experience-portfolio-2026-08-29.md).
It does not authorize a universal read service, root-specific truth, a new
database owner, or a server-authored UI tree.

The client receives semantic results and owner-backed read models. It chooses
native geometry, typography, interaction, density, and accessible ordering.
The agent may select meaning, claims, result family, represented resources, and
an authorized continuation. It may not select components or infer owner truth
from conversation history.

## Shared identity and return

The backend `ResourceRef` is the only production identity vocabulary:

```text
ResourceRef = kind + id + revision
```

Fixture-local TypeScript references may mirror these fields only while marked
non-production. A public contract must be generated from the backend model.

Every cross-root continuation carries:

```text
origin_root
origin_projection_id
selected_resource_refs[]
viewer_ref
audience_context
moment_ref or represented_at
immediate_job
active_result_family
active_instrument_ref?
continuation_capability_ref?
return_root
return_projection_id
```

No route string, component name, geometry, permission expansion, or mutation
payload belongs in this envelope.

## Semantic result envelope

Exactly one primary result family is selected:

| Family | Required semantic payload |
| --- | --- |
| `direct_state` | owner ref, revision, state label/value, freshness, correction path |
| `composition` | `CompositionBrief`, represented refs, claim-local Source bindings, lifecycle |
| `instrument` | instrument ref, owner refs, current state, freshness, available authorized operations, fallback |
| `receipt` | command ref, affected owner refs, per-owner verified result, partial/failure/recovery state |
| `owner_link` | owner ref, reason, selected substate |
| `prose` | complete text, evidence/citation refs where factual, no hidden continuation |
| `silence` | reason code and optional next eligible evaluation time; no visible authored unit |

Supporting material cannot smuggle in a second primary result. A Composition may
contain one supporting medium; an Instrument may expose a receipt after an
attempt; Direct State may link to its owner.

## Root projections

### HomeTemporalProjectionV0

Required fields:

- projection ID, generated time, represented Moment, viewer;
- posture: `ordinary | emerging | urgent | return`;
- foreground semantic result or null;
- zero to two supporting results under the state budget;
- stable root doors;
- why-now basis for every authored result;
- suppression receipts for fixture/debug use only; and
- accessible summary.

Home never requires a response to reveal the initial value. In urgent posture,
one Instrument preempts ordinary editorial units.

### PlacesProjectionV0

One mode per projection:

| Mode | Minimum fields |
| --- | --- |
| `world_field` | viewport/region identity, represented Moment, bounded place candidates, spatial reason, current-world freshness |
| `place_focus` | Place ref, durable identity, current conditions, relationship summary, supported distinctions, owner links |
| `place_path` | ordered Place/route refs, reachability, thresholds, gaps, alternatives, why the sequence matters |
| `live_reduction` | protected intention/commitment, current location, viable alternatives, timing margin, stale/unavailable exclusions, active Instrument |

Places ranking explains why here/there. It does not duplicate Home's why-now
priority or an Occasion's decision state.

### LifeProjectionV0

One mode per projection:

| Mode | Minimum fields |
| --- | --- |
| `index` | eligible Journey/Occasion/owner doors, time range, Place/people/Artifact facets, return cues |
| `episode` | container or projection identity, represented interval, Sources, Claims, Occurrences, plural Outcomes, gaps, saved Compositions |
| `timeline` | ordered owner refs and interval certainty |
| `map` | spatial refs bound to the same episode identity |
| `returns` | reason for return, changed relevance, last-used and current Moment |

Life stores no copy merely because Home or Places rendered something. A generated
Composition appears durably only after an accepted retention trigger.

### ChatProjectionV0

Required fields:

- conversation/turn ref and entry origin;
- selected resource refs and current job;
- contribution classification and five-axis authority references;
- primary semantic result;
- proposed versus authorized operation state;
- canonical readback and receipt refs;
- correction/undo/recovery capabilities where supported; and
- exact return envelope.

Chat can end with prose or silence. It does not need to manufacture an Artifact
or durable state for every turn.

## Field-to-owner ledger

| Visible field | Canonical owner | Bounded reader | Freshness | Correction or failure behavior |
| --- | --- | --- | --- | --- |
| person identity and selected relationship | Person / relationship | `relationship.read_context` | revisioned | unavailable or membership/audience epoch mismatch |
| audience and use grant | relationship / Occasion / Source grant | `audience.read_effective_scope` | revision + epoch | revoke and causally invalidate dependent projections |
| Artifact custody and provenance | Source | `source.inspect` | source revision | correct relation, release use, or delete under owner policy |
| bounded Claim and support | Claim/Source authority | `source.read_claims` | claim + source revisions | unsupported, disputed, superseded, or expired |
| Place identity and durable facts | Place | `place.read_focus` | place revision | disputed/unknown retained explicitly |
| current conditions | provider/world state | `place.read_conditions` | observed/verified time + expiry | stale or unavailable; never backfill from prose |
| reachability and route alternatives | routing/provider state | `place.read_path` | request time + provider expiry | partial route or unavailable mode |
| current Moment | Moment compiler over owned inputs | `moment.read_frame` | represented time | list missing inputs; do not persist every frame |
| Occasion purpose, members, constitution | Occasion | `occasion.read_state` | revision + membership epoch | viewer-relative unavailable fields |
| Plan shape | Plan | `plan.read_state` | revision | proposed and accepted versions distinct |
| consequential promise | Commitment | `commitment.read_state` | revision + provider verification | pending, failed, partial, superseded |
| external reservation/action truth | provider/action gateway | `provider.readback` | verified time | never infer success from request or assistant reply |
| action/delivery result | command/delivery receipt | `receipt.read` | immutable event + latest reconciliation | expose per-owner failure and recovery |
| Journey/Life door | Journey/Occasion or eligible episode projection | `life.read_index` | owner revisions | projection falls back without inventing a container |
| episode reconstruction | Journey/Occasion + Source/Occurrence/Outcome | `life.read_episode` | dependency manifest | gaps and plural Outcomes remain explicit |
| Maya social trace | Maya's Source grant + relationship audience | same Source/audience readers | grant expiry + revision | withdrawal invalidates or revises dependent claims |
| Home priority | ephemeral Home composer | no durable owner reader | current evaluation | suppress/recompute; never persist as preference |
| Place Horizon relevance | ephemeral Places composer | no durable owner reader | current evaluation | suppress/recompute |

## Minimum reader package

Implement only these grouped capabilities for the native lab:

1. `source.inspect` including claim bindings and audience/use state;
2. `place.read_focus`, `place.read_conditions`, and `place.read_path`;
3. `occasion.read_state`, `plan.read_state`, and `commitment.read_state`;
4. `provider.readback` and `receipt.read` for verified consequence;
5. `life.read_index` and `life.read_episode` over existing owners;
6. `relationship.read_context` plus `audience.read_effective_scope`; and
7. `moment.read_frame` as an ephemeral compiler result.

Opening, Home priority, Place Horizon, and interval composition remain derived
assessments. Monitor remains specified but unimplemented until read and command
authority is stable.

## Reuse gate

A reader advances beyond fixture or adapter status only if:

- at least three accepted portfolio states use it;
- its owner and revision are explicit;
- privacy, unknown, stale, conflict, and unavailable behavior are typed;
- it replaces transcript excavation or presentation-specific lookup; and
- it does not duplicate an existing authoritative gateway.

## Explicit exclusions

- no universal `get_context` endpoint;
- no arbitrary owner-kind dictionaries in a public payload;
- no React component or route fields;
- no persistence of Home ranking or Place Horizon;
- no inferred person preference from clicks, silence, query topic, or votes;
- no generalized Monitor owner in this package;
- no replacement of proven Trip writers; and
- no production shell migration before the native lab and visual selection.

## Verification fixtures

The contract must pass the five selected situations plus:

- missing Maya grant;
- Source withdrawn after a saved Composition;
- route provider unavailable;
- current conditions stale;
- Occasion membership epoch changed;
- provider action partially succeeded;
- Journey transfer remains unresolved;
- origin projection superseded before return; and
- quiet Home with no admitted authored unit.
