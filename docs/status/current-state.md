---
doc_type: current_status
status: active
owner: engineering
created: 2026-07-09
last_verified: 2026-09-02
why_new: Replace duplicated prose scorecards with one generated view of executable registries.
supersedes: []
source_of_truth_for: [cross-repo-current-state-summary]
---

# Current State

This is an orientation snapshot, not a release claim. Its numbers are generated
from committed registries; follow the linked authority for evidence and detail.

<!-- BEGIN auto:current-state -->
<!-- Run `make docs-status-sync` to update this block. -->
| Signal | Current value | Authority |
|---|---:|---|
| API contract | 570 paths / 632 operations / 1426 schemas | [`docs/openapi.json`](../openapi.json) |
| Canonical journeys | 28 total / 12 golden path / 7 holistic extension | [`journeys.yaml`](../journeys/journeys.yaml) |
| Feature flags | 97 registered / 95 active / 2 resolved | [`registry.yaml`](../flags/registry.yaml) |
| System charters | 23 Markdown documents | [`systems/`](../systems/) |
| Documentation inventory | 492 files classified | [`inventory.yaml`](../governance/inventory.yaml) |

### V1 intent versus executable evidence

Implementation means the manifest's named paths are tracked by their owning
repository. Release defaults come from the flag registry, not the deployed
environment. Readiness exposes known seeded-replay failures but remains
uncertified until a current-revision receipt exists.

| Capability | V1 intent | Implementation | Release default | Production-enabled | Readiness |
|---|---|---:|---|---|---|
| Auth and onboarding | **IN** | 1/1 tracked paths | No release flag declared | Unverified externally | [UNCERTIFIED — required promoted layers missing J01: physical; J02: physical](../journeys/STATUS.md) (J01, J02) |
| Trip creation, invite, membership, and roles | **IN** | 2/2 tracked paths | No release flag declared | Unverified externally | [UNCERTIFIED — required promoted layers missing J02: physical; J03: physical; J04: physical](../journeys/STATUS.md) (J02, J03, J04) |
| Planning, itinerary, proposals, and revert | **IN** | 2/2 tracked paths | No release flag declared | Unverified externally | [UNCERTIFIED — required promoted layers missing J01: physical; J05: physical; J06: physical](../journeys/STATUS.md) (J01, J05, J06) |
| Concierge, personal memory, and group synthesis | **IN** | 3/3 tracked paths | No release flag declared | Unverified externally | [UNCERTIFIED — required promoted layers missing J04: physical; J07: physical](../journeys/STATUS.md) (J04, J07) |
| Trip Home, living itinerary, map, and Now behavior | **IN** | 2/2 tracked paths | No release flag declared | Unverified externally | [UNCERTIFIED — required promoted layers missing J06: physical; J08: physical; J09: physical](../journeys/STATUS.md) (J06, J08, J09) |
| Post-trip Story and Trip photos | **IN** | 2/2 tracked paths | No release flag declared | Unverified externally | [UNCERTIFIED — required promoted layers missing J11: physical](../journeys/STATUS.md) (J11) |
| Expenses and settlement | **IN** | 2/2 tracked paths | No release flag declared | Unverified externally | [UNCERTIFIED — required promoted layers missing J10: physical; J12: physical](../journeys/STATUS.md) (J10, J12) |
| Places and universal search | **IN** | 5/5 tracked paths | Enabled by default | Unverified externally | [UNCERTIFIED — required promoted layers missing J07: physical](../journeys/STATUS.md) (J07) |
| Profiles, people search, follow, and following | **IN** | 2/2 tracked paths | No release flag declared | Unverified externally | [UNCERTIFIED — required promoted layers missing J13: physical](../journeys/STATUS.md) (J13) |
| Grounded live Plan repair | **IN** | 2/2 tracked paths | Dark by default | Not claimed; in scope but gated | [UNCERTIFIED — required promoted layers missing J05: device_mock,staging; J06: device_mock,staging; J08: device_mock,staging](../journeys/STATUS.md) (J05, J06, J08) |
| Open-interval micro-journey doorway | **IN** | 2/2 tracked paths | Dark by default | Not claimed; in scope but gated | [UNCERTIFIED — required promoted layers missing J08: device_mock](../journeys/STATUS.md) (J08) |
| Local Plans beyond travel | **IN** | 2/2 tracked paths | Dark by default | Not claimed; in scope but gated | [UNCERTIFIED — required promoted layers missing J07: device_mock; J14: device_mock](../journeys/STATUS.md) (J07, J14) |
| One permissioned relationship opening | **IN** | 2/2 tracked paths | Dark by default | Not claimed; in scope but gated | [UNCERTIFIED — required promoted layers missing J09: ai_eval,device_mock](../journeys/STATUS.md) (J09) |
| Booking record, mark-as-booked, and external handoff | **PARTIAL** | 2/2 tracked paths | No release flag declared | Unverified externally | [UNCERTIFIED — required promoted layers missing J10: physical](../journeys/STATUS.md) (J10) |
| Live booking transaction execution | **OUT** | 2/2 tracked paths | Dark by default | Not claimed; release defaults dark | [OUT — not a v1 certification target](../journeys/STATUS.md) (J10) |
| Live voice, narration, and microphone entry points | **OUT** | 2/2 tracked paths | Dark by default | Not claimed; release defaults dark | [OUT — not a v1 certification target](../journeys/STATUS.md) (J18) |
| Rendered postcards and postcard sub-surfaces | **OUT** | 2/2 tracked paths | Dark by default | Not claimed; release defaults dark | [OUT — not a v1 certification target](../journeys/STATUS.md) (J11) |
| Broad ambient dispatch and nearby feeds | **OUT** | 2/2 tracked paths | Dark by default | Not claimed; release defaults dark | [OUT — not a v1 certification target](../journeys/STATUS.md) (J09) |
| Public story links and social distribution | **OUT** | 2/2 tracked paths | Dark by default | Not claimed; release defaults dark | [OUT — not a v1 certification target](../journeys/STATUS.md) (J19) |
| Agent-initiated venue-disruption proposals | **OUT** | 2/2 tracked paths | Dark by default | Not claimed; release defaults dark | [OUT — not a v1 certification target](../journeys/STATUS.md) (J05, J09) |
<!-- END auto:current-state -->

### Four-root target conformance

The [Four-Root Loop, Object, and Surface
Contract](../systems/four-root-loop-object-surface.md) is target product and
architecture doctrine, not a shipped-shell claim. It establishes Home as the
selective temporal return, Chat as the clean contribution and agency layer,
Places as substantial spatial return, and Life as governed continuity over one
shared object model. It also fixes the compounding context loop, cross-root
handoff envelope, Life's container-and-lens organization, multiplayer
placement, and the real-world engine as a cross-cutting capability rather than
a fifth surface.

The default production mobile shell remains materially legacy-aligned around
Trips, Vesper, Places, and You, and the mature Concierge runtime still executes
through its Trip-centered tools. The integrated candidate now has typed,
default-off native Home, Places, and Life paths plus a default-off semantic
Concierge shadow; none changes public navigation or authorizes a release claim.
Production conformance still requires explicit shell promotion, broader typed
owner adapters, authority enforcement, complete cross-root behavior, real-data
validation, accessibility and performance evidence, and device proof without
duplicating owner truth.

As of 2026-08-29, the convergence line introduced a default-off internal
compatibility shell that labels the existing Trips, Concierge, Places, and
Atlas routes Home, Chat, Places, and Life only in development or explicit
internal builds. A native semantic portfolio lab covers five selected
situations across all four roots, and a fixture-only tagged semantic result
envelope preserves exact return context. The backend shadow branch has a
bounded portfolio read plan over the reviewed semantic operation catalog. None
of these changes serves new runtime data, replaces existing owner writers,
constitutes visual selection, or certifies the production shell.

As of 2026-08-31, the Home and Places semantic design phase is closed against
the accepted C1/C2/C3/F5 portfolio. The accepted bundle defines 65 root kinds
(Home 31 and Places 34) plus 13 shared instruments and lifts the blanket hold
on contract-bounded native implementation.

The first production-shaped projection spine now also exists: authenticated
read-only Home and Places endpoints compile canonical owner reads into a
generated mobile contract; gated native Home consumes the Home projection; and
gated Places carries the existing canonical Places feed unchanged inside the
root envelope. Returned Home, Urgent Home, and saved-scope Places have registered
native captures. This is implementation evidence, not production conformance:
the compatibility shell remains internal and default-off; C2 contribution
authority, C3 causal receipt/unwind, provider recovery, complete unit-union
coverage, and real-data validation remain open. Chat is unchanged by this
package. See the
[bounded implementation status](../working/home-places-root-implementation-status-2026-08-31.md)
for the exact proved and unproved boundary.

As of 2026-09-01, the integrated candidate also carries exact root return
context, typed Composition anatomy, authenticated owner-bound Artifact media,
and a default-off Life Time root. Life has a read-only projection over existing
Plans, Occasions, Commitments, and Outcomes; a canonical ResourceRef resolver;
and a separate dark refinding lane backed by truth-aware Source and Occurrence
reads. These are additive projection and retrieval seams, not a generalized
Life owner, complete People/Places/Threads lenses, Together write path, final
visual selection, or production shell. The backend and app preserve the same
generated contract, and legacy Atlas/You machinery remains the compatibility
owner while migration is dark.

The client shell now resolves one explicit system posture rather than allowing
its shell, Home v2, and governed Places gates to drift independently. An
internal governed rehearsal activates Home and the mature Places workspace over
their server-governed reads together; a missing root gate leaves both on the
compatibility posture. Public build flags still cannot activate this shell or
declare release eligibility. This is rollout integrity, not release evidence:
the signed cross-family rehearsal, physical-device observations, and reviewed
family promotion remain pending.

The release-evidence path is now executable without making release depend on
itself. A governed rehearsal posture can expose already-reviewed shadow
consequences only to an explicit user-and-family cohort on one exact deployed
backend revision, and dispatch revalidates that posture before owner mutation.
An idempotent operator tool provisions the same two principals across private
encounter confirmation, multiplayer Plan repair, and addressed Place handoff,
including canonical Plan/occurrence owners, Intake custody, Experience Graph
Source lineage, relationship command authority, workflows, and root openings.
A local three-family run and byte-identical replay pass. This is integration
evidence, not release evidence: clean dogfood revisions, two real signed-in
accounts, physical-device observations, degraded and negative probes, and a
passing machine-audited release artifact remain required. The procedure is in
the [cross-family rehearsal runbook](../working/lived-experience-cross-family-rehearsal-runbook-2026-09-02.md).

The local cross-family path now also executes through canonical judgment and
owned root treatment rather than stopping at fixture creation. Shared Plan
repair reconstructs the current proposal and is Home-owned; encounter
confirmation is Place-owned; and addressed handoff revalidates its exact
relationship command, pair audience, entity binding, custody, permissions,
revision, and expiry before selecting Place. A repeatable shadow-rehearsal
runner verifies pending evaluation, durable arc persistence, and completed
replay across the three families. Home v2 reads canonical open Plan proposals
as exact group coordination candidates, and a fresh local run joined the
persisted shared-Plan arc back onto the matching Home candidate and reviewed
consequence action. The portfolio now fails closed on missing adapter runtime
or canonical provider coverage independently of gateway readiness. These are
local system-integration results, not release or physical-device evidence.

The shared Source-to-contribution runtime now also exists in shadow. It can
admit one evidence-bound semantic contribution across private ordinary,
open-interval, recent-return, and explicitly authorized live/shared situations,
then express that contribution through distinct native Home and Places grammar
without changing Source metadata, ownership, audience, expiry, or claim
lineage. Home uses a temporal editorial passage; Places uses a spatial field
composition. Exact owner-backed loaders now resolve retained Experience
Anchors, approved evidence-bearing dossiers, and attributed Place handoffs at
their current revision, audience, expiry, and custody boundary. The handoff's
human prose stays outside owner-read payloads and enters only the bounded
producer material path. A selected Source set, one viewer, and one represented
clock are fixed before loading; omission, withdrawal, expiry, stale evidence,
selection substitution, mixed-viewer authority, split multiplayer grants, or
producer failure yields no root candidate. Root freshness can no longer relabel
stale Source truth as fresh.

A governed preflight now supplies that exact selection instead of asking the
model to discover its own evidence. It inventories at most 32 metadata-only
coordinates across viewer-owned retained Experience Anchors, approved
evidence-bearing dossiers in the current canonical Places context, and live or
kept addressed Place handoffs. Every coordinate carries an exact revision,
clock, freshness/expiry, audience and grant boundary, canonical subjects and
owners, and named retrieval facts—but no Anchor claims, dossier prose, or human
message. A deterministic doctrine table considers at most 12 complementary
Source pairs for ordinary/current-world, open-interval, recent-return, and
live/shared situations. Missing context, public-only pairs, stale or future
evidence, split grants, repeated exact groups, or insufficient complementary
Sources produces explicit silence. The chosen IDs and grant then expand into
independent exact Source, Place, and Relationship owner reads; canonical
assembly rejects any grant substitution before generation.

This is runtime, compiler, renderer, and authenticated-delivery evidence, not a
live content claim. The pipeline still invokes only an injected governed
producer; no default prompt/model producer or route activation exists.

Admitted semantic contributions now derive one root-neutral `fact_key` from
canonical claim meaning and authority rather than producer IDs or presentation
copy. Home and Places bind that key to a short-lived, recipient- and
projection-specific proof. The app records a content-free delivery receipt only
after the native unit remains in the measured viewport; mounting below the fold
does not count. Recent delivered keys can suppress the exact same semantic fact
on a later projection, while `not_rendered` and telemetry outage do not. This is
deliberately separate from live-engine treatment identity: delivery says which
meaning reached the surface, not which real-world intervention was offered or
executed.

This closes exact repeat suppression, not human understanding or a complete
known-to-person model. A delivery receipt does not prove comprehension,
agreement, memory, or that every underlying claim was previously known.
Therefore neither default portfolio receives generated contributions yet.
Backend commits `0f8c32aac`, `cbe300c9a`, `9f52a1294`, and `66d83911f`, plus app
commit `d89111d6f`, carry the owner-backed material, governed selection,
semantic identity, authenticated delivery, and qualified viewport packages.

### Contribution-contract conformance

The accepted [Contribution and Consequence
Contract](../systems/contribution-and-consequence.md) is target architecture,
not a shipped-behavior claim. The accepted [Structured Contribution Use Grants
decision](../decisions/2026-08-29-adopt-contribution-use-grants.md) now refines
Source/claim/projection lifecycle, Outcome learning targets, multiplayer
purpose, affected-person roles, contextual inspection, and connected-service
boundaries. Intake v2 already preserves much of its source-bound candidate,
truth, authority, and correction structure. The integrated Concierge prompt
and `observe` path now actor-bind personal writes and explicitly reject inferred
personality, mood, emotional-investment, and silence as durable memory. Full
conformance remains open because the shared policy is not yet the single gate
for every legacy writer and historical stores may contain older inferences.
Home, Places, Life, and new Chat input work must not treat those legacy writes
as canonical product doctrine. Use the expanded F01–F18 fixture portfolio as
target requirements, not shipped-behavior evidence.

For readiness, use [Journey Status](../journeys/STATUS.md). For the bounded first
release, use the generated [V1 release contract](../release/v1-scope.md).
For human/external blockers, use [Owner Actions](../Owner%20Action%20Items.md).
Those documents own their claims; this page deliberately does not paraphrase them.
