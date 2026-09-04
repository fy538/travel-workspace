---
doc_type: current_status
status: active
owner: engineering
created: 2026-07-09
last_verified: 2026-09-04
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
| API contract | 574 paths / 636 operations / 1447 schemas | [`docs/openapi.json`](../openapi.json) |
| Canonical journeys | 28 total / 12 golden path / 7 holistic extension | [`journeys.yaml`](../journeys/journeys.yaml) |
| Feature flags | 102 registered / 100 active / 2 resolved | [`registry.yaml`](../flags/registry.yaml) |
| System charters | 23 Markdown documents | [`systems/`](../systems/) |
| Documentation inventory | 507 files classified | [`inventory.yaml`](../governance/inventory.yaml) |

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
its shell, Home v2, governed Places, and Life v1 gates to drift independently.
An internal governed rehearsal activates Home, the mature Places workspace, and
the Life root over their server-governed reads together; a missing root gate
leaves the roots on the compatibility posture. Public build flags still cannot
activate this shell or declare release eligibility. This is rollout integrity,
not release evidence: the signed cross-family rehearsal, physical-device
observations, and reviewed family promotion remain pending.

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

### Home · Places · Life acceptance world — 2026-09-04

The integrated productization lane now has an additive HPL-01–HPL-06 scenario
manifest (`travel-agent` commit `abf7d6bc1`). Each world carries one represented
clock, two viewer identities, explicit owner revisions, Source and grant refs,
and expected Home, Places, and Life seats. A compact machine-readable snapshot
is available from the same manifest (`travel-agent` commit `b32f35eae`) for
operator and native review. The manifest compiles the existing Home/Places
rehearsal graph through the Life v1 adapter; it does not seed a second store or
claim real-account evidence.

The Life adapter preserves viewer-safe multiplayer authority for shared
occasion-linked plans, occasions, outcomes, and commitments (`travel-agent`
commit `d33a4f42f`), including group audience, an explicit occasion grant, and
attributed member owners across supported lenses. A follow-up privacy boundary
(`travel-agent` commit `8426531f3`) keeps private outcomes and commitments
private even when they are linked to a shared occasion. Causal withdrawal,
complete correction repair, and a production shared corpus remain open.

The internal native preflight and product-system resolver now require Life v1
alongside Home v2 and governed Places before reporting a governed three-root
rehearsal (`travel-app` commits `09931b20e` and `1daafb8fc`). The Life root and
four-root shell remain default-off; compatibility and public posture are
unchanged. This is rollout integrity and deterministic fixture evidence, not
device, real-data, visual, or release evidence. Active-seat arbitration,
real-owner Home value, Places scoped result-set closure, Life production
corpus/dossiers, native matrix, and cohort gates remain pending per the [Home, Places, and Life
Productization Program](../working/home-places-life-productization-program-2026-09-04.md).

The next bounded seams are now executable. Backend commit `1b449b38e` adds a
finite Life corpus inventory over the same viewer-relative graph used by the
four lens reads; repeated entries retain one owner/source/audience/grant
identity, and sparse lenses remain empty without setup work. Backend commit
`436eb3f90`, workspace contract `57224b7`, and app contract commit
`5817c0a38` make Places map responses echo their opaque context handle,
preserving server-owned scope through map/list transformations. These are
read-only identity boundaries, not production dossier, active-seat, real-data,
or full result-set composition evidence. Chat, entity implementation, and Life
surface UI remain unchanged.

Backend commit `3e287a33e` closes the corresponding Life serving seam. The
additive `/api/root-projections/v1/life` route now builds the finite corpus
inventory before compiling the requested lens and rejects an untracked record
or any lens-local change to canonical identity, owner/source lineage, audience,
or grants. The wire contract is unchanged and the guard is read-only; real
corpus breadth, dossier destinations, Returns, withdrawal repair, and native
evidence remain open.

The broad post-package canaries are not promotion evidence: backend recorded
20,554 passed with two failures and one teardown error (the existing
parallel-load bounded-read timeout expectation and unrelated dead Atlas
handler audit), while frontend recorded 1,177 passing suites and 20 failures
across legacy/entity/Chat/profile/navigation contracts. The HPL-focused
backend/app suites, TypeScript, OpenAPI parity, and docs-link checks passed;
all three repositories are clean.

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
live content claim. A structured prompt/producer adapter, registered model role,
and optional route seam now exist. The independent serving flag remains
default-off, so no generated contribution is live by default.

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

The structured producer path now has a content-free four-situation acceptance
gate. Ordinary/current-world, open-interval, recent-return, and live/shared
baselines must each traverse selection, exact owner reads, governed material,
production, compilation, and distinct Home/Places expression. Separate probes
cover earned silence, exact repetition, authority withdrawal, expiry, provider
and parse failure, compiler rejection, and latency. The artifact records opaque
selection identity, Source kinds/count, audience/grant shape, root identities,
payload hashes, timing, and outcome only; it contains no Source prose,
generated copy, claim text, named person, Place, or raw Source ID.

Backend commit `e54631927` adds the missing production-attempt continuity
boundary. Before exact owner reads or model work, each viewer must atomically
claim the exact revision-bound Source group. Active leases and typed terminal
cooldowns exclude repeat attempts; concurrent losers try the next bounded
group or return explicit silence. Produced, producer-silence, producer-failure,
compiler-rejected, and pipeline-rejected outcomes remain distinct. The attempt
row stays content-free; an admitted production is retained separately for at
most six hours under the exact viewer, Source-group revision, situation, and
audience boundary. Lease completion and production retention now commit in one
transaction, so a cooldown cannot be burned while its useful output is lost. A
stale worker cannot complete or surface work after another request reclaims its
lease, and an attempt-store outage keeps the optional producer cold rather than
generating without ownership.

This attempt ledger is not the delivery ledger and not the live-engine
treatment ledger. It says that Vesper already spent judgment/generation work
on one exact Source group; qualified delivery separately says a semantic fact
reached the viewport; treatment/consequence separately says a real-world move
was offered or executed. The additive migration has one Alembic head.
PostgreSQL tests cover exclusive claim, expiry repair, stale-worker rejection,
cooldown exclusion, and atomic output retention. Home and Places now reuse that
same admitted production when their exact governed group matches, while their
compilers still produce different temporal and spatial expressions. Real-model
editorial adjudication, cohort rollout, and device evidence remain open.

App commit `31a54cbbb` supplies the missing native Home→Places depth. A
Home-origin Places door stays inside the Home navigator while rendering the
same mature Places owner used by the canonical Places tab. Its ephemeral exact
return identity survives map, Search, Saved, Reading, feed-card, and supported
detail movement. Backend commit `708b1b86c` keeps semantic projection revisions
stable across opaque grant/proof rotation; app commit `6a32beebf` now performs
a canonical fresh read before any final Home scroll. Exact viewer, revision,
unit, family, audience, and selected-resource identity restores once; any
supersession, unavailable read, or missing/consumed token keeps the recomposed
Home and cannot arm a later stale jump. Evidence passes 48 backend tests and 54
app suites / 363 tests plus both TypeScript gates, lint, API boundaries, and
route/surface checks. This closes the code-level route and degradation gaps,
not the physical-device or rollout gate.

App commit `1c134d964` adds the native iOS simulator proof: the Home tab remains
selected while its Places depth opens, an explicit `Back to Home` control
unwinds the route (or safely replaces to canonical Home without history), and
the fresh-read resolver restores the same typed Home unit at its semantic
offset. The PR-smoke Maestro flow passes 1/1 on iPhone 16 Pro / iOS 18.2; the
adjacent selection passes 33 suites / 251 tests plus TypeScript, contract,
boundary, registry, and surface checks. This narrows the remaining gate to
physical-device and Android return, nested map/Reading/detail/action movement,
process death and concurrent real-owner supersession, real-backend readback,
visual continuity, an explicit iOS edge-gesture decision, and shell promotion.
The edge-swipe attempt did not unwind this nested headerless stack; the visible
back control is the proven path. Chat and Life were unchanged.

App commit `a92401579` proves the first nested continuation through Search and
Saved. The rehearsal exposed and fixed an unconditional collection `replace`
that cloned the Places root and broke final Home return. Saved now dismisses to
the existing serialized Places owner, with cold-entry convergence as fallback.
Home → Places → Search → Saved → Places → exact Home passes 1/1 in 23 seconds
on the pinned iOS simulator; five focused suites / 37 tests and adjacent gates
pass. Remaining nested evidence is map, Reading, entity detail, and a verified
owner action; the physical/device, process-death, concurrency, and rollout
limits above remain unchanged. Chat and Life were not modified.

App commit `e3a2cf293` extends native simulator coverage through the product's
other representative Places media and a consequence-bearing action. Direct
guide → Dossier → Reading and Reading → Dossier → existing Reading owner both
preserve context and the root token; Map returns to the same Home-owned Places
workspace; and an Experience save emits its canonical success consequence,
survives detail movement, reads back as saved from the shared Saves owner, and
then returns to the exact Home unit. The three PR-smoke flows pass in 30s, 25s,
and 42s on iPhone 16 Pro / iOS 18.2. The adjacent selection passes 31 suites /
256 tests plus both TypeScript gates, boundaries, surface/core-tab checks,
metadata, and all 349 Maestro syntax validations. This closes representative
mock nested-media and read-after-write evidence—not real-backend, physical
device, process-death, concurrent supersession, Android, edge-gesture, or
public-shell promotion. Chat and Life were unchanged.

Backend commit `be675841c` proves the complementary real-owner half for Saves.
An authenticated, idempotent venue save is durably read through the Saves API,
Places' saved-venue model, and the final Home v2 continuity region with the
same private save and canonical venue references. API unsave removes it from
all three on fresh reads, with no duplicate Home state. The real-PostgreSQL
test and **44** adjacent owner/projection tests pass. The full offline backend
canary reaches **20,071 passed / 25 unrelated failures**. This is real backend
evidence, but it remains separate from the simulator's mock-owner evidence:
native-to-server wiring on pinned revisions, restart, real supersession,
physical iOS, Android, edge gesture, and shell promotion are still open. Chat
and Life were unchanged.

Backend commits `b30f8b70c`, `08a14498d`, and `a9b0249a2`, together with app
commits `ea67fed6c` and `d5df71912`, now join that backend owner proof to the
native Home→Places path on the local real API. Home resolves the saved venue's
name through the canonical Place owner read, exposes its destination and
nested controls independently to assistive technology, and keeps structured
backend degradation diagnostics out of product copy. A deterministic operator
fixture and runner prove native unsave, absence from the Saves owner and fresh
Home projection, canonical reprovisioning, named Home readback, Place-owned
detail, and exact semantic return on iPhone 16 Pro / iOS 18.2 simulator.

The rehearsal also exposed and fixed an admission defect: equally ranked Saves
were previously selected by random UUID order when Home reached its bounded
unit budget. Recent explicit Save attention now resolves contention inside the
low-demand continuity lane without outranking current-world or coordination
value. Focused verification passes 15 backend tests and 18 app tests plus Ruff,
backend formatting, TypeScript, Prettier, shell syntax, Home/Places QA
preflight, and the real native rehearsal. This is simulator and local-real-API
evidence—not physical-device, Android, process-death, concurrent supersession,
other owner-family, visual-approval, or public-shell promotion evidence. Chat
and Life were unchanged.

### Home page composition arbitration — 2026-09-02

Backend commit `c2bd2fc01` replaces Home's generic twelve-item selector with a
Home-specific page arbitration pass after candidate-level value judgment. The
shared gate still owns truth, authority, freshness, exposure, evidence-cluster,
and seat admission; the Home pass now owns the page-level relationships that
cannot be decided one card at a time:

- posture selects one explicit crown identity, including a truthful world read
  when Quiet has no unresolved foreground;
- Quiet admits zero unresolved demand, other postures admit at most one, and
  optional doors do not become demands merely because they are actionable;
- one In-motion row survives page composition;
- Urgent preserves the direct read, week shape, recovery crown, and at most one
  non-demanding live row while Horizons and Continuity yield;
- the world read and week shape no longer spend the content allowance; and
- earned low-demand returns are not governed by an arbitrary card-count cap
  after each has beaten silence. They share a posture-specific cumulative
  attention budget, while owner reads and an optional caller safety bound remain
  finite.

The admission report carries the exact dominant candidate and structured
composition suppressions. Non-empty Home projections must name one admitted
dominant across chrome or any owner region; an entirely withheld/degraded
projection may remain empty rather than fabricate a crown.

App commit `89bf47fd7` consumes that contract. Chrome dominance resolves through
the existing world read, while a dominant from Now, In motion, Horizons, or
Continuity is promoted into one page-level crown and removed from its ordinary
row position. Empty regions no longer render headings, and exact semantic
restoration targets the promoted crown rather than its former region slot.

Verification passes **180 backend root-projection tests**, **29 focused app
tests**, Ruff, backend formatting, TypeScript, and Prettier. No OpenAPI shape
changed. This is deterministic composition and native semantic structure, not
visual approval of every posture: the remaining Home package is native
seven-posture rehearsal against production-shaped portfolios plus application
of the outstanding §12.7 instrument/register rules. Chat and Life were
unchanged.

### Home seven-posture native system — 2026-09-02

Backend commit `152776b4e` repairs the dogfood rehearsal boundary: the resolved
Home posture now reaches both selection and compilation. Returned therefore
selects its Continuity crown, while a Planning case without an admitted
In-motion decision honestly falls back to its world read.

App commit `e7a6ae7e7` makes the complete accepted posture set executable in the
actual flagged Home tab rather than a gallery. A typed matrix covers Available,
Planning, Live, Returned, Quiet, Cold, and Urgent, and existing mock personas
select those envelopes at runtime. Every non-chrome fixture unit passes the
explicit native renderer registry; Cold's `now_invitation` is promoted rather
than falling through a generic card.

The same slice applies the low-risk §12.7 structural laws that were still
missing: the week renders as a banded temporal seam; world-read anchors use the
accepted ghost ink; subordinate In-motion material is one 44pt status row
without an icon plate; a dominant In-motion decision expands into the crown;
and a unit with a typed continuation no longer shows a second competing source
door. Seven registered polish flows now correspond to the seven postures.

Verification passes **40 focused app tests**, TypeScript, scenario-ID
validation, the seven-flow dry run, focused lint with no new errors, and the
backend rehearsal/composition set. On the booted iOS simulator, manual launch,
persona deep links, and Maestro hierarchy inspection resolved `home-v2-screen`
plus the expected posture-specific crown for all seven cases. The aggregate
Maestro capture runner remains blocked by a local Simulator launch-service
failure, so this is executable native hierarchy evidence—not accepted visual,
backend-real, physical-device, Android, or public-shell evidence. Chat and Life
were unchanged.

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
