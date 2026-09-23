---
doc_type: working
status: active
owner: engineering / social experience
created: 2026-09-07
last_verified: 2026-09-07
expires: 2026-10-07
why_new: Maps the social experience to existing domain owners, distinguishing code existence from reachable behavior and correcting the initial legacy-path audit before implementation planning.
supersedes: []
depends_on:
  - claude-design-social-experience-project-handoff-2026-09-07.md
  - fixtures/shared-fixture-world-2026-09-07.md
  - live-engine-owner-path-matrix-2026-09-05.md
---

# Social experience — capability map to existing owners

## 0. Audit correction and evidence limits

**Revised September 7 after a cross-lane strategy/code investigation.** This
replaces the first audit's capability conclusions and package recommendations;
it does not claim new production implementation. The earlier design response
records what the designers drew, not what engineering supports.

The initial audit missed canonical graph and engine paths while inspecting
legacy Trip implementations. Its universal absence claims are withdrawn:

| Earlier conclusion | Direct counter-evidence | Correct implication |
| --- | --- | --- |
| No Occasion table or durable roster | `travel-agent/backend/domains/experience_graph/schema.py`: `occasions`, `occasion_members`, `occasion_invitations`; `backend/api/routes/experience_graph.py`: creation, invitation, response and invitee-specific reads | Git blame dates core tables to August 21–22. Account-based membership exists. A bounded non-account guest remains a narrower capability question, not grounds for another Occasion owner. |
| T0 is only a metric / prompt instruction | `backend/core/contribution_admission.py::effective_retention_for_decision`, used by `backend/core/db/pending_chat_turns.py`; `permits_private_source_retention`, used by intake v2 | Real admission/retention enforcement exists. End-to-end no-write coverage and an authorized cross-user source path must still be verified separately. |
| Live engine is only a situation GET; no non-applying preparation | `backend/lived_experience/engine.py::LivedExperienceEngine`; `adapters/shared_plan_repair.py::SharedPlanRepairAdapter` evaluates group-safe options without committing them | Trace existing preparation and owner execution before adding a method to situation. This does not prove fresh option production or the complete guest adaptation flow. |
| No source-contribution worker | `backend/root_projection/v2/source_contribution_worker.py::run_source_contribution_workflow` and the source execution/result work in Integration | Private generated-source production is not completed human sharing. Reuse relevant delivery/repair infrastructure without treating the two as identical. |
| Legacy Refind limitations describe all Life capability | `backend/life/refind_sources.py` is a legacy booking/block reader; Life also has owner projections, source-change delivery and active shadow organization work | Inspect the intended Life owner/index path and worktree before proposing a second shared-media archive. |

The fresh pass inspected code, git history, relevant contracts and recent lane
conversations. No application test suite or device journey was run in this
documentation pass. Tests mentioned below are candidates, not passing receipts.
Keyword absence, a missing component name, or the absence of an enum spelling
such as `adopted` is not proof of a missing product behavior.

## 1. Checkout, lane and activation snapshot

This is a September 7 snapshot; active lanes continued changing during review.
Recheck exact HEAD, branch, worktree and flags before implementation.

- Workspace: `main`, with concurrent modified/untracked working documents.
- Backend: `main` plus isolated Home receiving, Life shadow/continuity and
  integration/read-admission worktrees. Content and Integration landed code on
  main during the review; not all related paths are enabled.
- Mobile: `codex/entity-object-design-completion`, not main; separate Home
  receiving worktree. Do not describe every mobile change as released.
- Home: actual receiving/action/return improvements in
  `codex/home-receiving-2026-09-07`; inspect before building parallel cards.
- Life: `codex/life-shadow-rehearsal-2026-09-07` contains projection and repair
  work; shadow/rehearsal does not establish serving cutover.
- Integration: exact source-result identity/read work includes
  `1961eebff`, `35c1b203f`; canonical worker exists but execution remains
  bounded/gated. It is not a generalized task inbox.
- Content: `516c89596` write-free bounded research,
  `5a6bc740a` explicit local event windows, `b0d5a80ca` exact source
  handoff, `0cd27bdee` retained knowledge across anchors, `dd1890eb6`
  answer-only experience mode. These are code receipts, not guest-flow tests.

Read effective flags and their callers for the exact intended route. The first
audit reported several handoff/production flags default-off and social circles
default-on; that is not certification of a deployment's current settings.

## 2. Seven seams — reusable foundation versus unverified completion

Paths below are backend-relative unless prefixed otherwise.

| Seam | Existing foundation / owner | Remaining behavior to establish | Smallest next investigation |
| --- | --- | --- | --- |
| **1. Selected sharing and receiving** | Contribution policy; relationships/place handoffs; root source discovery and delivery; Home receiving worktree | Selected human material reaches the intended people with its original author and usable object destination; withdrawal repairs source-dependent views across roots. No complete path certified here. | Trace one authorized human share from its owner through projection, actual mobile renderer and exact-object read. Distinguish human material from generated source contributions. Determine whether existing named-recipient authority can carry a user-facing Friends selection before adding enum/table kinds. |
| **2. Human Reply / private Ask / acknowledgment** | `domains/relationships/repository.py::open_pair_conversation`; conversations routes; `concierge/entry_context.py`; pending-turn admission and source retention gates | A received-object context resolves correctly, stays private for Ask, and returns to its originating surface. Cross-user source admission needs an effective scoped grant, not an owner-predicate bypass. | Trace the received object resolver and every reached writer. Preserve existing T0 safeguards. Test Reply and Ask separately; acknowledgment remains a product proposal, not a required new reaction service. |
| **3. Guest invitation, answer, arrival, later material** | Canonical Occasion membership/invitation schema and `api/routes/experience_graph.py`; legacy `api/routes/invites.py`, landing and public projection provide reusable token/delivery behaviors | No-account access for each specific capability, intended-recipient verification, sensitive-address disclosure, scoped answers and later media delivery are not established by account-based Occasion APIs or a public landing page. | Trace canonical invitations first, then assess reuse of token/landing delivery. Decide guest identity and access boundaries before schema. Do not extend Trip membership merely to unlock dinner or promise secure identity from an unverified RSVP. |
| **4. Remote / non-attending contribution** | Occasion graph and contribution authority; owner-controlled collaboration in Multiplayer Product Strategy §§5.1–5.2; recent Outcome/Commitment-to-Life owner events | Contributor can reach a narrow view, send permitted material, correct it and receive readback without attendance or unrelated address/roster access. End-to-end coverage remains unverified. | Identify the current contributor grant/owner-command path and minimum extension. Existing Occasion membership is not a complete remote-contributor permission, but its existence must not be ignored. |
| **5. Practical adaptation** | `lived_experience` engine, shared Plan repair adapter, prepared consequence and canonical gateways; graph Plan/Commitment owners; legacy proposal paths | A real change produces useful feasible alternatives, preserves accepted dependencies, and carries the authorized result to each affected person's actual reader. Broad signal-to-adaptation completion is not certified. | Follow the [owner-path matrix](live-engine-owner-path-matrix-2026-09-05.md). Inspect options supply, participant availability/constraints and exact readback; a legacy typed constraint list or generic push sentence cannot characterize the whole system. Do not create a second engine or equate preparation with adoption. |
| **6. Connection and attention controls** | Pair `social_circles`, member request/accept/decline states, pair conversation; separate relationship visibility/place-pull grants | One understandable connection and per-share audience selection; consistent mute, disconnect, block and report across entry points. Existing controls do not establish this complete experience. | Map pair semantics and grants before adding friendship structures. Audit messages, invitations, handoffs and bounded links together. Mute/block completion remains unverified; absence must be established by following all relevant owners, not only keyword search. |
| **7. Retrieval, continuity and repair** | Intake deletion/source invalidation and handoff revocation; Life owner events/projections; independent/dependent source handling; ongoing Life shadow work | Refind a specifically authored shared object through Time/People/place context; validate guest/recipient access; preserve independent material while invalidating restricted derivatives and in-flight results. | Reconcile with Life's target read/index path before extending legacy Refind. Verify source identity, author, custody, grant, revision and dependency lineage across consumers. Do not promise universal paraphrase removal from one passing source-lane test. |

## 3. Revised packages and decision gates

These are proposed integration packages, not authorization to code or a new
parallel-lane plan. The complete-system roadmap owns ordering.

0. **Owner/reachability reconciliation.** Record exact commit, flag, producer,
   command, reader and mobile destination for each seam. Classify each as
   existing but isolated, gated, partially connected, missing or verified.
   Resolve conflicts with Home, Content, Life and Integration owners.
1. **Original human receiving and contextual response.** Connect the existing
   sharing/relationship/source owners to root receiving and object readers;
   preserve private Ask, explicit Reply, useful original-only receiving and
   exact return. Add no automatic publication or usage receipt to the author.
2. **Bounded participation and practical help.** Extend canonical Occasion and
   live-engine paths only where the guest/contributor/affected-person experience
   needs it. Separate sensitive access from an unverified invitation response.
3. **Continuity and usable controls.** Reuse Life and relationships for later
   retrieval and optional contact. Build/review mute, disconnect and block as
   distinct controls; reporting is separate. No block prerequisite.
4. **Permissioned enrichment.** Keep original display, independent world help
   and source-based recipient composition distinct. Implement only adopted
   scopes; the immediate-question proposal is neither blanket AI permission
   nor a ban on other separately authorized Home/Places value.

No new memory, invitation, notification, Occasion or live-engine service follows
from this map. A new column or type requires a demonstrated owner-level gap,
not merely a different design-board label.

## 4. Required verification receipts before claiming completion

For each package, record commands actually run, outcomes and environment; do
not add reported test counts across overlapping lane runs.

- Share → recipient original → actual destination → private Ask versus Reply →
  return; no passive-view/Keep reporting.
- Ask-only source admission, no unauthorized retained derivative, correction
  and withdrawal during production and before result publication/read.
- Current versus widened audience; later additions do not silently expose old
  material; exact source/grant expiry and block behavior.
- Guest safe preview, intended-recipient access, answer/constraint, remote
  contribution, later material and account linking as separate capabilities.
- Unadopted alternative versus owner-applied arrangement; affected participation
  and independent commitments remain truthful.
- Same shared object refound through Life; source withdrawal removes only
  disallowed dependents, preserving independent records.
- Rich, sparse and empty social supply; original-only and independently sourced
  value remain worthwhile without participation or generation on each impression.

Existing suites to inspect include contribution policy/pending Chat, relationship
handoffs/social circles, graph invitations, lived-experience repair, source
contributions/root projections, and Life projection/refind tests. Their existence
does not certify the complete route. Native sender/recipient walkthroughs remain
necessary after implementation; none was performed for this map.
