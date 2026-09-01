---
doc_type: working
status: active
owner: engineering (Claude Code) / founder review
created: 2026-08-31
last_verified: 2026-08-31
expires: 2026-09-30
why_new: Workstream D ("One contribution through its complete lifecycle")
  requires a complete inventory of every durable writer reachable from the
  eight contribution entry classes, judged writer-by-writer against the
  contribution-and-consequence contract, before the design prototype commits
  to a lifecycle the substrate cannot honor. Audit only — no implementation,
  no migration, no noun changes.
promotes_to: null
supersedes: []
source_of_truth_for: []
depends_on:
  - docs/systems/contribution-and-consequence.md
  - docs/working/life-next-behavior-prototype-handoff-2026-08-31.md
  - docs/working/life-together-consumer-arc-code-audit-2026-09-01.md
  - docs/working/life-human-refinding-code-audit-2026-09-01.md
---

# Life Contribution Lifecycle — Durable Writer Code Audit

Repositories audited (absolute paths):

- Backend: `/Users/feihuyan/travel-workspace/travel-agent/backend`
- Mobile: `/Users/feihuyan/travel-workspace/travel-app`

Evidence labels: **CODE-EVIDENCED** (file:line), **DOCUMENTED TARGET**
(contract/spec language, no code), **ABSENT** (searched, not found; searches
named). Zero callers ≠ dead. Status vocabulary follows the handoff §3 ladder
(Architecture resolved / Projection modules composed / Consumer flow proven at
fixture scale / Canonically integrated / Implemented / Shipped); nothing here
is "done."

## 0. Executive summary

**80 durable writers inventoried** across the eight entry classes (W1-W74
plus plumbing sub-rows; one out-of-scope content-seeding lane). Verdicts
against the contract: **38 conforming · 28 partially conforming · 14
non-conforming.** The conforming mass sits in canonical-owner mutations
(itinerary/booking/expenses with dispatcher-enforced authority evidence),
intake v2, the notification spine, and the correction lattice. The
non-conforming mass is almost entirely **ambient exhaust writers** — code
that converts ordinary conversation, silence, mood, and location into durable
person-adjacent state with no gesture, no authority, no receipt, and no
expiry.

### Headline answers

1. **Ask is not no-write on any lane a user can reach.** Every ordinary chat
   turn durably persists the transcript; an Ask-with-image also persists the
   raw bytes forever (`chat_images`, no TTL — W1b) and a model interpretation
   of the source baked permanently into history (W2); trip-scoped turns
   additionally fire four ambient writers (journal, member brief, social
   signals, GPS observation — W8/W9/W10/W12). The one enforced
   `answer_only` lane (share→pending-chat-turn, W31) is **built, conforming,
   and unreachable** — its `from_chat` entry has zero callers
   (`travel-app/utils/routes.ts:641`). §8.6's "Ask remains no-write" gate
   fails today; migration step 3 must cover the plumbing, not just memory
   tools.
2. **Worst non-conforming writers, ranked by blast radius:**
   - **W40 trip summary/digest** — synthesizes ALL members' observations
     *including private ones* (no `shared` filter, `digest/engine/summary.py:56-70`)
     into a group-visible retrospective whose privacy scrub **fails open**
     ("proceeding unscrubbed", `:110-115`); indefinite retention; also the
     inlet into Personal Memory. The single highest-leverage fix found.
   - **W10 ambient social-signal capture** — an LLM extractor runs on every
     group-room message (default-on) writing durable person-attributed
     `energy_state` / `individual_state` / `engagement_pattern` rows; no
     receipt, no expiry, survives the occasion (§11, §3.3, §3.4).
   - **W39 proposal-silence recorder** — named-person "X did not vote" rows
     via `silence_observed`, which the un-narrowed reflection prompt then
     instructs reading (§11's most explicit prohibition, implemented as a
     deterministic writer — the 08-31 prompt fixes did not touch it).
   - **W7/R-04 trip-brief dynamics/spending skills** — SKILL_GROUP_DYNAMICS
     and SKILL_SPENDING_CONTEXT still instruct durable psych/silence writes
     ("a pointed silence", "who checks out when energy is low", "Alex went
     quiet when €80 restaurants were suggested") into an ungated
     agent-maintained table with no member-facing read route.
   - **W2/W1b Ask-source retention** and **W12 GPS→person-store observations**
     (synthesis input with no exclusion) complete the top tier.
3. **Design-invalidating finding for Workstream D:** the §8.2 loop's middle
   is missing, not merely misbehaving. Chat contributions produce durable
   *exhaust*, not addressable objects — "quiet placement in Life" has nothing
   to place (only intake v2 yields an addressable private anchor); "later
   admitted value" runs backwards (the one explicit learning consent,
   `group_and_learn`, has **no consumer**, while unconsented ambient lanes
   feed real consumers); and "causal receipt only if something changed" is
   unfalsifiable because synthesis regenerates the narrative with **zero
   user-facing receipt** (the event exists; its only listeners are cache
   invalidation). The friend's-addressed-note fixture (F6.4) is
   unimplementable until the Checkpoint-1 grant record exists.
4. **What is genuinely strong:** intake v2 (custody receipts, an interpreter
   that cannot self-grant retention, custody re-verified inside the
   projection transaction, propagating retraction); the action-authority
   dispatcher (structured/conversational evidence, fail-closed, single-use);
   the correction lattice (outbox + event + policy-invalidation, Atlas
   cascade, account deletion); and the notification spine's handling of
   silence as aggregate product state (W45) — the conforming counterpart to
   W39 already running in the same codebase.

### Six-fixture snapshot (full traces §3)

| Fixture | Today's verdict |
| --- | --- |
| Restaurant photo Point | P — value yes; bytes+interpretation retained forever; no Life placement |
| Movie ticket Bring | C via intake v2 (`ticketed`, never occurred); N via legacy chat-paste lane |
| Voice observation | P — preservable; personality protection is prompt-level only |
| Friend's addressed note | ABSENT — no durable audience/grant substrate |
| Forwarded booking email | C — custody/occurrence separation implemented; alias + stall-gap caveats |
| Ask with Source | N on the reachable lane; C on the unreachable `answer_only` lane |

## 0.1 Relationship to the prior audits (do-not-redo boundary)

The Together audit (`life-together-consumer-arc-code-audit-2026-09-01.md`)
§7 established the memory-synthesis laundering findings and its appendix
records four safety fixes applied 2026-08-31. This audit **re-verified all
four fixes are present in the working tree** (uncommitted; confirmed in
`git status` of `travel-agent`):

1. **Cross-user `observe()` write hole — fix present.** `observe` is now
   deliberately included in the actor-binding guard; any resolved `user_id`
   differing from the authenticated speaker is refused with
   `cross_user_memory_access_forbidden`
   (`backend/concierge/memory_tools.py:652-668`; refusal code at `:665`).
2. **Personality/mood/silence observation prompts — narrowed as described.**
   "Do NOT record inferred personality traits, mood/emotional-state
   readings…" (`backend/concierge/_prompts_skills.py:1537`); "Silence is not
   signal you may keep: ignored options, unanswered proposals…" (`:1589`).
   Residue at other skill sites is a finding of this audit (§5, R-04).
3. **Settlement masking bypass — fix present.**
   `_search_trip_settlement_shares` applies
   `or_(expenses.masked.is_(False), expenses.paid_by == actor_id)`
   (`backend/core/db/search.py:1707`).
4. **Durable query-hash retention — fix present server-side.**
   `_scrub_durable_query_state` defined at `backend/api/routes/events.py:71`
   and applied on both the single (`:400`) and batch (`:511`) event writes.
   The client emitter still sends the hash in transit (§5, R-01).

Findings from those audits are cited, not re-derived. This audit's new ground
is the complete eight-entry-class writer inventory (§2-3), the six-fixture
path mapping (§4), and the remaining laundering paths (§5).

---

## 1. Entry-class inventory

The eight entry classes of handoff §8.5, with their concrete entry points and
the durable writers reachable from each. "Durable writer" = any code path that
INSERTs/UPDATEs rows, vector points, or files that outlive the turn, including
background jobs the entry schedules.

| # | Entry class | Concrete entry points |
| --- | --- | --- |
| E1 | Ordinary Chat | `concierge/agent.py::handle_turn` via `api/routes/chat.py` / `conversations.py`; voice is the same turn with `modality="voice"` (`api/routes/_message_flow.py:626`; `voice/FEATURE.md` — LiveKit lane built, gated off in prod by absent credentials, not a flag) |
| E2 | Inbound share / share-sheet / intake v2 | `POST /api/intake/submissions` (`api/routes/intake.py:170`); mobile `travel-app/app/share-capture/index.tsx` via `components/sharing/ShareIntentHandler.tsx`; legacy `POST /api/inbound-items` (`api/routes/inbound_items.py:122`) |
| E3 | Occasion (group) chat | Same `handle_turn` in a group conversation; group-only tools (`concierge/_tools_select.py` `_GROUP_ONLY_TOOLS`); `api/routes/trip_group_memory.py`; proposal automation (`concierge/proposal_automation.py`) |
| E4 | Import / Bring | SendGrid inbound-email webhook (`api/routes/inbound_email.py:89`); trip photo upload (`api/routes/trip_photos.py:136`); Atlas photo upload (`api/routes/atlas.py:1883`); chat-screenshot tool `inbound_screenshot_submit` |
| E5 | Proactive turns | `concierge/triggers.py`; `notifications/` gates→triage; `proactive_events`; scheduled tasks (`backend/tasks/*`, `workers/*`) |
| E6 | Reflection | `concierge/reflection.py` — triggers: post-session (`concierge/session.py:2515-2517`), daily batch (`api/lifecycle.py:1519-1525`), post-trip (`core/db/trips/crud.py:965-970`, `api/services/trip_reflections.py:114-117`), manual admin (`api/routes/admin.py:347-349`) |
| E7 | Memory synthesis | `concierge/refresh_memory.py:361` — triggers: every-5-observations auto-synthesis (`concierge/memory_tools.py:111-146,699-702`), post-trip T+3h (`concierge/post_trip_memory_refresh.py:43,146-204`), invite onboarding (`notifications/invite_delivery_tasks.py:123-125`), DNA-dispute repair (`workers/dna_dispute_refresh_jobs.py:45+`), durable workflow lane (`concierge/memory_workflow.py:11`) |
| E8 | Correction / release | Dispute endpoints (`api/routes/users/me.py:667,731`); `fact_forget` / `memory_constraint_remove` tools; observation prune; Atlas artifact delete (`core/db/atlas.py:1104-1149`); intake submission delete (`core/db/intake_v2.py:628-769`); account deletion (`core/db/account_deletion.py:783+`); retention purges (`core/db/retention.py:65-174`) |

Two structural facts frame every table below:

1. **The contribution-policy gate is still shadow-only.** `resolve_contribution`
   (`backend/core/contribution_policy.py:134`) remains reachable only through
   the agentic-facade compiler in `shadow` mode, default `off`
   (`backend/concierge/config.py:172-175`; prior audit §0.1, re-checked). No
   writer below consults `ContributionAxes` before writing. Proposed authority
   therefore lives in the tool-contract layer and effective authority is
   whatever that layer actually enforces.
2. **The tool-contract layer is real but partial.** Contracts with
   `confirmation != NONE` default to DISPATCHER enforcement
   (`concierge/tool_contracts.py:82-89` — the `_contract` helper), and the
   dispatcher demands `AuthorityEvidence` — a structured client action id, or a
   narrow conversational-evidence match against the current persisted user
   message (`concierge/action_authority.py:1-50`; ambiguous/negated prose fails
   closed; evidence is single-use within a turn) — enforced at
   `concierge/agent.py:1860,1898` (`enforce_confirmation=True`) via
   `validate_contract_context` (`tool_contracts.py:426-457`). This is a genuine
   explicit-instruction check for the tools that declare it. Tools declaring
   `ConfirmationPolicy.NONE` (notably `observe`, `update_intent`,
   `trip_brief_update` — `concierge/tool_registry.py:451-479`) get **no**
   admission check: `validate_contract_context` returns `None` for a tool with
   no contract entry (`tool_contracts.py:396-398`).

---

## 2. Writer tables

Column key — **Gesture/job**: contract §2 vocabulary. **Authority**: proposed
→ effective (who actually decides the write). **Custody**: §3.1 Source-layer
state actually implemented. **Retention S/C/P**: source / claims / projections
per §3.1. **Learn**: §3.4 learning target @ level actually achieved. **Aud**:
audience/social principals. **Tier**: closest T0/T1/T2 as behaved, not as
intended. **Receipt/Undo**: does the person see the write; can they reverse
it. **Verdict**: conforming (C) / partially conforming (P) / non-conforming
(N) vs `contribution-and-consequence.md`, with the violated clause.

### 2.1 E1 — Ordinary Chat (every writer a private 1:1 turn can reach)

Voice is this same table: a voice session is `handle_turn` with
`modality="voice"`; observations land with `source_mode='voice'`
(`concierge/memory_tools.py:579`; `core/db/_tables/memory.py:393-397`).

| W | Writer (entry) | Gesture/job | Authority proposed → effective | Custody | Truth/evidence | Target owner | Retention S/C/P | Learn | Aud | Tier | Receipt/Undo | Causal consumers | Verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| W1 | Chat transcript persistence (`concierge/persistence.py:19,81,118`) | every gesture / continuity | none proposed → automatic on every turn | retained_private (message text) | captured (verbatim) | `messages`/`conversations` | retained indefinitely / n/a / n/a | situation@L1 as context replay | conversation channel (group room = group) | T0-with-residue | transcript IS the record; **no delete/redact/supersede primitive exists** (function inventory `persistence.py` — persist/complete/retry/fail/load only; prior audit A6) | history loader, `conversation_search`, compaction, reflection | **P** — §12.3: no enforceable continuity-read/no-write posture; §8: withdrawn content replays to the model |
| W2 | Vision-summary bake (`concierge/vision_summary.py:1-20` → `messages.metadata_['vision_summary']`; prepended on later loads `persistence.py:343`) | side effect of Ask/Point with image | none → automatic Haiku call per image turn | claim derived from a Source that itself may be transient | generated summary of image content | `messages.metadata_` | n/a / **durable claim, no expiry** / n/a | situation@L1 intended | conversation | T1 silent | none / none | every later turn's prompt | **N** — §3.2 Ask default is "transient Source processing, no new durable claim"; the summary is a durable content-derived claim with no custody, expiry, or correction path |
| W3 | `observe` (`concierge/memory_tools.py:795-908` → `create_observation`, `core/db/observations.py:143`; in `_ALWAYS_TOOLS`, `_tools_select.py:56-77`) | Point (claimed) / model-initiated | ConfirmationPolicy **NONE**, class AGENT_MAINTAINED_STATE (`tool_registry.py:475-479,520`); no contract entry → no admission (`tool_contracts.py:396-398`) → effective authority = the LLM per turn | n/a | interpretation stored as governed claim; provenance JSONB, **no author column** (`_tables/memory.py:359-447`) | `observations` + Qdrant vector (`memory_tools.py:858-860`) | n/a / scoped_governed (optional expiry) / n/a | **person@L3-equivalent without admission** | private by default (`shared` bool; group-visible only from group trip rooms `memory_tools.py:625-636`) | T1 silent | no turn receipt; later visible/retirable in memory screen (`travel-app/app/atlas/memory.tsx:339-385`); prune tool exists | synthesis (E7), recall, reflection | **N** — §11/§12.1-12.3; mitigations since 08-31: cross-user guard (`memory_tools.py:652-668`), narrowed SKILL_MEMORY (§0.1). The writer itself remains ungated |
| W4 | `fact_remember` / `fact_forget` (`tool_handlers/memory.py`; `core/db/user_facts.py:31-171,174-205`) | Keep / Correct | EXPLICIT_USER + dispatcher AuthorityEvidence (conversational or structured; `tool_contracts.py:330-345`, `action_authority.py`) | n/a | authored fact, namespaced key, typed supersede chain | `user_facts` (`core/db/_tables/users.py:509-547`) | n/a / scoped_governed, default `visibility='private'` / n/a | person@L3 admitted by explicit language | private; `group` visibility only if set | T1 | fact visible + retirable in memory screen; full history kept (`get_fact_history`) | synthesis (group-visible subset only, `refresh_memory.py:409-415`) | **C** — cleanest lifecycle in the system; residual §8: no same-turn scope receipt guaranteed |
| W5 | `memory_constraint_set` / `remove` (`tool_contracts.py:319-352`) | Keep (safety constraint) | EXPLICIT_USER + dispatcher evidence; self-bound (`memory_tools.py:670-677`) | n/a | authored constraint | hard-constraints store | n/a / scoped_governed / n/a | person@L3 admitted | private | T1 | listed in memory surfaces; remove tool | prompt assembly, planning | **C** |
| W6 | `update_intent` (`tool_registry.py:456-460`; also deterministic `concierge/ambient_intent.py`) | ambient / working state | NONE → LLM (or regex for bare place/date) | n/a | provisional intent scratchpad | conversation intent state | n/a / session_working (durable row; 24h-inactivity expiry per contract §3.3 NOT verified — no expiry job found for intent rows; grep `intent` in `core/db/retention.py`: no hits) | situation@L1-L2 | conversation | T1 silent | none / superseded by next update | search scoping, planning | **P** — shape matches §3.1 `session_working`, but expiry unenforced (§3.3) |
| W7 | `trip_brief_update` (`tool_handlers/memory.py:3,33`; table `trip_briefs`, `core/db/_tables/trips.py:485-507`, concerns `spending,dynamics,vision,stakes,logistics`) | ambient / trip operating notes | NONE, AGENT_MAINTAINED_STATE → LLM, instructed by skill prose | n/a | model interpretation, no evidence refs | `trip_briefs` | n/a / durable, **no expiry at trip end** / n/a | person+relationship@L2 that persists cross-context | trip-internal (agent-only surface) | T1 silent | none / none (no user surface lists brief content; ABSENT — grep `trip_briefs` in `api/routes/`: no read route for members) | prompt assembly | **N** — SKILL_GROUP_DYNAMICS (`_prompts_skills.py:2145-2170`) still instructs recording "who defers, who's quiet…, who checks out when energy is low", "a pointed silence", "private tensions (marked PRIVATE)", "Sarah stopped engaging" → §11 (model-inferred personality/emotional state/social role; silence as signal), §3.3 (occasion inference never expires), §3.8 (inspect evidence, not personality) |
| W8 | Post-turn trip-journal update (`concierge/doc_updates.py:75-97` → `notes.py:374`, table `trip_journals` `_tables/trips.py:440`) | ambient / trip log | none → automatic Haiku after every clean trip-scoped turn | n/a | generated recap of the interaction | `trip_journals` | n/a / durable / n/a | situation@L2 | trip | T1 silent | none / none | digest, trip summary | **N** — the journal prompt writes hidden `[agent: ...]`-register annotations the user never sees (`notes.py:334-336`) and frames the journal as a future "post-trip artifact for the group" (`notes.py:329-332`) — ambient durable narrative with audience-widening intent, no receipt (§8, §3.6) |
| W9 | Post-turn member-brief update (`doc_updates.py:99-123` → `notes.py:431-465`; prompt `notes.py:345-363`; table `trip_member_briefs` `_tables/trips.py:418-433`) | ambient / per-person trip notes | none → automatic Haiku after every clean trip-scoped turn | n/a | model inference incl. behavioral reads (prompt exemplar: "Mike hasn't said what he wants but reacted positively to food options") | `trip_member_briefs` | n/a / durable, no trip-end expiry / n/a | person@L2 drifting toward L3 (no scope enforcement on content) | trip-internal, per-person | T1 silent | none / none | prompt assembly | **N** — §11 (behavior→durable person note without admission), §3.3 (no expiry), §8 (no receipt) |
| W10 | Ambient social-signal capture (enqueued per **group-room** user message, `concierge/agent.py:1582-1598`, gated `auto_capture_signals=True` default `concierge/config.py:26` → `workers/social_signal_jobs.py:16` → `signal_capture.py:17` → `social_state/retriever.py:106` → LLM extraction pipeline) | ambient / group intelligence | none → config default; LLM extractor decides content | n/a | signal_type incl. `behavioral`, `engagement_pattern`; dimensions incl. **`energy_state`, `individual_state`, `group_dynamics`** (`core/db/_tables/trips.py:340-380`) | `social_signals` (person-attributed via `user_id`) | n/a / durable, is_active/supersede lifecycle, **no trip-end expiry** (only member-departure deactivation `core/db/trips/members.py:863-875` and account deletion) / n/a | person+relationship@L2-durable from L1 exhaust | trip | T1 silent | none / none | `trip_social_state` synthesis, context compiler, world model, reflection prompt | **N** — §11 (mood/energy/engagement inference from ordinary conversation), §3.3 (Occasion inference not discarded after reconciliation), §3.4 (L1→durable promotion without admission) |
| W11 | `trip_social_state` synthesis (`social_state/pipeline.py:160-210`; genesis `social_state/genesis.py:78`) | system synthesis | none → pipeline | n/a | versioned generated markdown; genesis doc marked provisional | `trip_social_state` | n/a / n/a / published_snapshot versions | relationship@L2 | trip (read into group prompts) | — | none / none | concierge prompts, SKILL_GROUP_DYNAMICS reads | **P** — write-time bake; input filter excludes departed members' typed signals at synthesis (`pipeline.py:186-202`) but rendered snapshots persist |
| W12 | Conversation location persistence (`concierge/location_persistence.py:22-123`; 5-min/100m dedup; fed by every located chat request, `api/routes/_helpers.py:52`, and the client attaches lat/lng to every send when available, `travel-app/hooks/useConciergeChatTransport.ts:563-584`) | ambient / situation | none → automatic | n/a | captured position | conversation last-location **plus** `create_observation(category="location_sample", importance=1, no expires_at)` into the personal `observations` store | n/a / **durable person-store rows, no expiry** / n/a | situation@L2 stored at person@L3 custody | private | T1 silent | data-use receipt lists location signals (`travel-app/app/you/data/receipt.tsx:30-33`) / no per-sample undo | whereabouts, spatial context — **and Personal Memory synthesis**, which groups ALL active observations by category with no `location_sample` exclusion (`refresh_memory.py:711-757`; grep `location_sample` in `refresh_memory.py`/`observations.py` category filters: zero exclusions) | **N** — §3.3 ("Location: current Moment or active Occasion only"); §3.4/§11 situation→person laundering via the synthesis inlet |
| W13 | Itinerary mutations: `itinerary_block_add/update/move/undo`, `itinerary_attendance_set`, `itinerary_parallel_plan_set`, `generate_plan`, `pin_experience`, `trip_patch`, `trip_accommodation_set` (`tool_contracts.py:123-283`) | Decide/Act | TRIP_EDIT_POLICY / EXPLICIT_USER, **dispatcher-enforced** with provenance freshness; group-review trips route to proposals (`tool_contracts.py:131`) | n/a | plan truth (not occurrence) | itinerary/trips domain owners | n/a / scoped_governed / cached projections | situation@L2; itinerary edits feed actor-scoped preference inference (`preference_engine/edit_inference.py:149-238` — conforming, prior audit §7.5) | trip | T1/T2 | action receipts + postconditions (`concierge/postconditions.py`); `itinerary_block_undo` is a real undo | itinerary readers, home feed, notifications | **C** |
| W14 | Booking lane: `propose_booking` (PROPOSE) / `confirm_booking` (STRUCTURED_ACTION; `tool_contracts.py:210-239`) | Decide/Act | proposal row → structured client action id required to commit | n/a | commitment truth | booking domain | prepared consequence expires per §3.3 analog | situation@L2 | trip | T2 | structured confirmation card; receipts | booking agent, notifications | **C** — the contract's M3 one-tap boundary implemented |
| W15 | `inbound_screenshot_submit` (`tool_contracts.py:270-283`) | Bring from chat | LLM invokes; idempotent on (owner, content_hash); USER_AUTHORED_INGESTION | private envelope | provisional extraction downstream | `inbound_items` | v1-lane retention (see W26) | none until review | owner | T1 | envelope receipt; review lane | v1 processor | **C** at this seam (v1 downstream caveats in §2.2) |
| W16 | Proposal writers: `propose_change`, `present_options`, `stay_candidate_add`, `propose_trip_creation` | Decide (prepare) / coordinate | PROPOSE effect; approval lives on the proposal | n/a | proposal state | proposals/reaction cards | prepared; deadline-bound | product@L2 | group | T2-prepare | proposal cards are the receipt; votes resolve | proposal automation (→ W34 silence writer caveat) | **C** |
| W17 | `stay_candidate_vote` / `promote_to_trip` (STRUCTURED_ACTION, `action_authority.py:33-39`) | Decide | structured action id only | n/a | vote/commit | stay/trip domain | scoped | product@L2 (votes not generalized to taste — no vote→affinity path found; `save`-effects affinity is save-scoped, `core/save_application.py`) | group | T2 | card + state readback | stay comparison, trip creation | **C** |
| W18 | `expense_log` / `expense_settle` (`tool_contracts.py:284-308`) | Keep/Act (money record) | EXPLICIT_USER; conversational evidence must contain action cue + amount (`action_authority.py:55-60`); actor-bound settle | n/a | financial record | expenses domain | scoped | product@L2 | group (masked-expense guard in search fixed 08-31, `core/db/search.py:1707`) | T1 | expense receipts (`concierge/settlement_receipts.py`) | settlement, COSTS surfaces | **C** |
| W19 | `set_location_sharing` (`tool_contracts.py:111-125`) | consent write | self-only by construction; idempotent | n/a | grant state | trip location sharing grants | until revoked | none | self→trip | T1 | mode readback; revocable | whereabouts disclosure | **C** — model §3 grant behavior |
| W20 | `compose_group_message` (group-compose privacy guard verifier, `tool_registry.py:65,691`) | Address (Vesper→group) | LLM under privacy guard | n/a | generated message | group `messages` | retained | none | group | T1 | visible message | transcript | **C** with W1 caveats |
| W21 | Composed-card snapshots (`concierge/composed_cards.py:236,297,346` → `messages.metadata_`) | display | none → automatic | n/a | derived projection | message metadata | n/a / n/a / published_snapshot | product@L1 | conversation | — | action revalidation at tap rejects revoked sources (`composed_cards.py:891,1049-1050`) | card taps | **C/P** — snapshots acknowledge §3.1 `published_snapshot` semantics; stale render until tap |
| W22 | Action receipts + postconditions (`core/db/_tables/action_receipts.py:18-90`; `concierge/postconditions.py`) | receipt infrastructure | system | n/a | readback of owner state; `SourceRef.degraded` supported | `vesper_action_receipts` | retained | product@L0-L1 | private/group/system | — | this IS the receipt lane | chat receipt UI | **C** |

**E1 net finding — Ask is not structurally no-write.** A pure conversational
Ask on a trip-scoped turn durably writes, at minimum: the transcript (W1), and
— fire-and-forget, regardless of gesture — social signals (W10), a journal
entry (W8), and a member-brief update (W9); with an image it also bakes a
durable vision summary (W2); and `observe` (W3) is loaded every turn with no
admission gate, at the model's discretion. A personal no-trip Ask still writes
W1/W2/W3/W6. The only Ask lane with an enforced `answer_only` posture is the
share→pending-chat-turn lane (W31): `requested_retention="answer_only"` exists
**only** in the pending-turn/admission models (`core/models/admission.py:52`,
`core/db/pending_chat_turns.py:38,103`; grep `answer_only` across
`concierge/`: zero hits in the ordinary turn path).

#### 2.1b Additional E1 writers (plumbing deep sweep)

| W | Writer (entry) | What persists | Verdict |
| --- | --- | --- | --- |
| W1b | **Chat-attachment bytes** — `concierge/session.py:1235-1256` → `core/db/chat_images.py:62-118` (disk write + `chat_images` row, table `core/db/_tables/conversations.py:43`) | Raw image bytes + row, **indefinitely, for every gesture including Ask-with-image**; no TTL/purge job (ABSENT — greps `chat_images` × `delete/purge/ttl/expire` over `workers/`, `core/db/`: zero; `workers/maintenance_jobs.py` purges only agent_workflows + shadow receipts) | **N** — §3.2 (Ask default: transient Source processing) and §3.3 ("Raw Source used only for Ask: delete after processing; ≤24h") |
| W1c | **Tool-call bake into message metadata** — `concierge/session.py:1986-2011` stores `tool_calls_made_list` (full tool inputs + 2,000-char result previews, `concierge/tool_result_recording.py:108-117`) in `messages.metadata_` | Model-authored tool arguments (which can embed personal content the model wrote into `observe`/`fact` args) persist forever inside message metadata; telemetry redaction (`concierge/telemetry.py:200-232`) covers only `concierge_turns`, not this copy | **P** — §3.1 (no expiry, no redaction path) |
| W1d | **`concierge_turns` telemetry row** — `concierge/telemetry.py:235-324`, shielded write at `session.py:2049-2092` | Redacted-but-content-bearing full user message + reply (up to 32k chars) + tool I/O (8k) with `user_id`, indefinitely; no purge job (ABSENT, same greps) | **P** — claims L0 but §3.4 L0 is "aggregate service telemetry"; per-user conversation text forever is L1-as-stored |
| W1e | **Planning brief from `<notes>`** — `concierge/agent.py:2203-2209` → `trips.planning_brief` (`core/db/_tables/trips.py:85`) + `planning_brief_log` (`:460`) | Durable model reasoning scratchpad; stream filter guarantees the user never sees it (`concierge/notes.py:94-235`) | **P** — legitimate L2 agent-maintained state but no expiry, no inspection path |
| W1f | **Taste-DNA reflection shown-marker** — `concierge/first_contact.py:333-418`: records the card-shown flag as `create_observation(category="taste_dna_reflection_shown", importance=4)` (`:400-413`) | Product bookkeeping stored in the **person** observation store; feeds synthesis input | **P** — product@L0 fact stored at person custody; small product→person channel |
| W1g | **Angle query seeder** — unmatched `search_angles` (`concierge/tool_handlers/search.py:1154`) → `concierge/angle_query_seeder.py:72-218` → `place_angles` rows, `source_type="user_query"`, **verbatim `source_query`** (`:205-218`), status pending_review | A private question's raw text becomes indefinitely durable editorial/world state. No `user_id` stored (de-identified) — so world/product target, permitted for Ask under §3.4 | **P** — conformance is de-identification-dependent; no envelope, no expiry |
| W1h | **`memory_refresh` / `memory_observations_prune` / `memory_events_mark_processed`** — model-invokable maintenance (`concierge/memory_tools.py:737-750,1122-1156,1228-1238`; durable workflow `concierge/memory_workflow.py:11-24`, 30-day GC `workers/maintenance_jobs.py:37-59`) | Regenerates the L4 narrative / archives observations on model judgment | **P** — maintenance framing right; `memory_refresh` re-runs the ungated synthesis at model discretion |

### 2.2 E2 + E4 — Inbound share / intake v2 / import / Bring

The intake v2 core is **the strongest conformance story in either repo** and
matches contract §12's "reusable substrate" claim. Full pipeline trace and
evidence: this audit's sweep found custody receipts at creation
(`core/db/intake_v2.py:475-486`, receipt writer `:151`), server-only derived
source roles (`core/models/intake.py:36`), an interpreter that **cannot
self-grant retention** (`inbound/semantic_contract.py:236-254` raises on any
candidate proposing retention ≠ none; `core/db/intake_semantics.py:597-602`
stamps now+24h), owner-review correction verbs recorded as `user_confirmed`
observations (`intake_semantics.py:750-987`), custody re-checked inside the
graph-projection transaction even on replay
(`inbound/experience_graph_bridge.py:109-140,327-330`), propagating retraction
(`intake_v2.py:726-742` emits `intake_candidate_retracted` on owner delete),
and real scheduled retention enforcement (`intake_v2.py:772-894` +
`workers/audio_jobs.py:647-652` cron; S3 purge `workers/intake_cleanup_jobs.py:34-87`).

| W | Writer (entry) | Gesture/job | Authority proposed → effective | Custody | Target owner | Retention S/C/P | Learn | Aud | Tier | Receipt/Undo | Verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| W23 | Intake v2 submission (`api/routes/intake.py:170-203` → `core/db/intake_v2.py:344-524`; mobile `travel-app/data/inboundItems.ts:234-319`) | Bring/Point, job deferred | owner submits; server policy owns custody; trip binding member-gated | retained_private pending → forced transient (24h) at admission | `intake_submissions`/`intake_source_objects` (`core/db/_tables/intake_v2.py:40-150`) | ephemeral_processing+24h / none / none | none (L0 lifecycle) | owner-only | T1 | admission receipt (`intake_v2.py:151`); DELETE revokes + purges (`routes/intake.py:246-264`); mobile "Delete private share" throughout (`app/share-capture/index.tsx:453,485,640`) | **C**, except the stall gap: `retention_expires_at` is set **only** at semantic admission (`intake_semantics.py:598`, sole setter); a stalled/failed pipeline leaves it NULL and `expire_intake_sources` filters `IS NOT NULL` (`intake_v2.py:790`) → raw private bytes can persist indefinitely (§3.3 ≤24h) |
| W24 | Email forward v2 (SendGrid webhook `api/routes/inbound_email.py:89` → `inbound/email_forward.py:164`; default-on `core/feature_flags.py:47-55`) | Bring (§3.9 adoption order 1) | alias token is the only authenticator; sender identity unverified (`email_forward.py:75-87`) | body → verified inline source; raw provider fields → `provider_archive` custody-only object (`intake_v2.py:539-625`) | same v2 tables | transient(24h) / candidate / none | none until confirm | owner-only | T1 | v2 receipts; delete purges archive (`intake_v2.py:743-760`) | **P** — retention/truth conforming; Audience axis: anyone knowing the alias can exercise the owner's Bring authority (§3 axis 4) |
| W25 | Email forward v1 legacy (`email_forward.py:268-318`, live only if `INTAKE_V2_EMAIL_ENABLED` falsified) | Bring | alias | raw archive "private, permanent until the 30-day purge" (`email_forward.py:100`) — **the purge does not exist** (ABSENT: `inbound_email` in `core/db/retention.py`/workers: zero) | `inbound_items` | retained_private indefinite / — / — | — | owner | T1 | receipt via `workers/inbound_jobs.py:873` | **N** — §3.3; comment promises a backstop that is ABSENT |
| W26 | Legacy share v1 auto-route (`api/routes/inbound_items.py:122` → `workers/inbound_jobs.py:437-466` high-confidence branch → `create_save_with_effects` `:291-299`, `create_accommodation` `:215-246`) | Bring → **implied Keep** | model confidence == effective authority for a durable canonical write | v1 images rehosted to **public CDN variants** (`inbound/submit_image.py:169-180`) vs v2's private bucket | `user_saves`, `trip_accommodations` | retained / scoped / cached | save-effects place affinity (L3-adjacent) | private | T1 without the §7 test | "Added to Places" receipt but **no Undo affordance** (`share-capture/index.tsx:686-703`); dismissal only for needs_review (`routes/inbound_items.py:203`) | **N** — §3 ("Confidence… never expand[s] authority") + §8 (no undo); mitigated: fresh mobile shares default to v2 (`share-capture/index.tsx:177-178`) |
| W27 | v1 review confirm (`routes/inbound_items.py:167` → `inbound/review.py:16-36`) | Keep (explicit) | owner tap | as W26 | saves + effects | retained / scoped / cached | save-derived affinity | private | T1 | item readback; dismiss route | **C** |
| W28 | Trip photo upload (`api/routes/trip_photos.py:136-210`) | Bring/Contribute to trip album | uploader; member-gated; **default `visibility="group"`** server-side (`:145`) — mobile bulk intake defaults `private` (`travel-app/utils/photoCandidateClusters.ts:4`), but story-slot fill hard-codes `group` (`app/(tabs)/trips/[tripId]/story.tsx:271`) | CDN rehost (album group-visible by design) | `trip_photos` | retained / — / published (album) | see W29/W30 | channel-inherited (§10 rule 1) | T1 | upload response; per-photo visibility PATCH; uploader-only soft delete (`:310-335`) | **C** on audience; any member may retag any visible photo (`:281-304`) — watch item |
| W29 | Photo → occurrence evidence (`routes/trip_photos.py:411-426` → `core/db/occurrence_reconciliation.py:150-171`) | implicit side effect of Bring | none → automatic for every block-tagged photo **including `private`** | append-only evidence row | outcomes evidence table | — / scoped evidence / — | situation@L2 (occurrence support, not preference) | owner-scoped | T1 silent | **no receipt for the evidence row; photo delete does not touch it** (§1.3 verification below) | **P** — §2 Bring ("no Occurrence claim by implication") is technically honored (evidence ≠ claim; proposals are user-resolved, `occurrence_reconciliation.py:571`) but the write is silent and unrepairable (§8) |
| W30 | `group_and_learn` opt-in (`routes/trip_photos.py:341-362`; consent sheets `travel-app/components/photo-intake/PhotoIntakeSheets.tsx:368-420`) | explicit narrow mandate | owner bulk-upgrades own group photos only | n/a | `trip_photos.visibility` flag | — | **DOCUMENTED TARGET — no learning reader exists** (readers: story-share inclusion `core/db/trip_story_shares.py:734`, audience filters, consent readback `api/routes/memory.py:345-371`; zero taste/memory consumers — zero callers ≠ dead: declared consent awaiting its consumer) | uploader-scoped | T1 | per-uploader consent readback (`routes/memory.py:308-343`) | **C** as consent plumbing; §3.4 target+level must be resolved when a reader lands. Mobile soft spot: the escalation sheet pre-selects `group_and_learn` (`components/trip/GroupAndLearnConsentSheet.tsx:26-41`) |
| W31 | Pending chat turns (share→chat handoff; `core/db/pending_chat_turns.py`, `api/routes/pending_chat_turns.py`) | Ask with admitted Source | staged by owner+device; fingerprint-locked idempotency | references admitted custody only; **send re-verifies** `custody_status=="verified"` (`pending_chat_turns.py:276,348`; route `:262-277`) | `pending_chat_turns` | transient / turn_candidate, 24h TTL (`:19,153`) + lazy expiry (`:390`) | L1 | personal | **T0** (`requested_retention="answer_only"`) | cancel route (`:358`); content-free release payload | **C** — the contract's custody-re-verification pattern done right; the ONLY enforced answer_only lane in the product |
| W32 | Atlas photo upload + keep-time permanence (`api/routes/atlas.py:1883-1944,1960-2002`; client rehost-on-keep `travel-app/hooks/useAtlasPhotoRehost.ts:1-24`) | Keep | owner; "the deliberate keep IS the consent moment" (`:1952`) | CDN rehost, artifact-private | `atlas_artifact_photos` | retained / — / published | none automatic | owner | T1 | idempotent; postcard readback; full delete cascade exists (E8) | **C** |
| W33 | `backend/ingestion/*` (Ticketmaster/Viator etc.) | not a contribution path | admin-only (`api/routes/admin.py:1014` sole caller) | — | `experiences`/`places` | — | world | public catalog | — | — | out of scope — content seeding, unreachable from user Bring |

**§12 review-first-vs-value-first verdict (mobile): CONFIRMED — and the
value-first lane is built but unreachable.** The share-capture flow submits on
mount, shows custody receipt, then leads with "Vesper found N things to keep
or correct" / "Keep this interpretation" before any value
(`travel-app/app/share-capture/index.tsx:264-335,447-489,516-644`); value copy
appears only after Keep (`:582`). A `from_chat === "1"` branch skips review
and admits the share straight into a T0 `answer_only` chat turn
(`:278-292,305-318`) — but `routes.importCapture`'s `fromChat` option
(`travel-app/utils/routes.ts:641`) has **zero callers passing it** (repo grep:
only the route builder; `ShareIntentHandler` never sets it). Migration step 9
is therefore one wiring decision away from partially landing.

### 2.3 E3 — Occasion (group) chat

Group turns differ structurally from 1:1: channel-tagged provenance
(`concierge/agent.py:619-621`), a group-without-trip turn gets no private
context (`agent.py:1724-1746`), and under `strict_group_compose` every
group-visible message must come from `compose_group_message` — agent free text
is discarded (`agent.py:2072-2100`); private-corpus egress guards fail closed
(`concierge/tool_handlers/_group_guard.py:60-385`).

| W | Writer (entry) | Gesture/job | Authority → effective | Target owner | Retention | Learn | Aud | Receipt/Undo | Verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| W34 | Group `observe(visibility="group")` (`concierge/memory_tools.py:617-636,795-907` → `observations.shared=true`) | Point/Keep | group visibility admitted only from a group trip room (`:833-838`); cross-user refused (`:617-624,651-667`); still AGENT_MAINTAINED, no envelope | `observations` | expires_at optional; purge only when set (`core/db/retention.py:65-71`) | person@L3 on model judgment; observe still MANDATORY on booking turns (`_prompts_skills.py:1552-1566`) | other members' turns load it via `load_shared_observations` (`concierge/turn_loader.py:635`; author excluded `core/db/observations.py:301-315`); attribution retained (§10 rule 2) | none in-turn | **P** — §13.3 (agent-discretionary durable write), §6 (no receipt); §11-safe on paper post-narrowing |
| W35 | Trip shared memory member edit/forget (`api/routes/trip_group_memory.py:299-375` → `core/db/trip_shared_memories.py:57-201`) | Contribute / Correct / Release | organizer-only, re-verified in-tx (`:89-100`); optimistic versioning (`:122-126`) | `trip_shared_memories` versions + `trip_events` receipt (`:173-184`) | occasion-scoped, versioned; forget = new version (lineage kept) | relationship@L2 | trip members | trip_events row is a real receipt | **C** for its scope — best-behaved group writer; gaps: item-level attribution absent (Together audit A8); non-organizers cannot Correct their own projected material (§3.8) |
| W36 | Group profile synthesis (`preference_engine/synthesis/group_synthesizer.py:115-345` → `core/db/trips/members.py:1279-1333` → `trip_group_profiles`; lazily regenerated from any chat turn `preference_engine/retrieval/preference_retriever.py:421-436`) | system synthesis | pipeline; per-member privacy prefs gate inclusion (`group_synthesizer.py:151-258`) | `trip_group_profiles` versions | 10-version prune; old versions containing since-revoked material persist (revocation withholds serving, `preference_retriever.py:410-418`, but does not rewrite rows) | person→group L4 bake | whole group | none to the profiled member | **P** — §11 (markdown bake erases per-item source/scope); compensating controls: revision stamps + serve-time withholding |
| W37 | Change proposals (`concierge/tool_handlers/planning/_propose_present.py:514`, persist `:165-236` → `change_proposals`, `core/db/_tables/itinerary.py:393-459`) | Decide (prepare) | `authorship_origin` preserved: `human_group` / `human_private_shielded` / `vesper_autonomous` (`:1043-1044`; `concierge/weather_rescue_proposal.py:81-94`); stale-provenance check (`:545-568`); privacy validator (`:200-212`) | proposals | deadline-bound | product@L2 | group | proposal card = receipt | **C** — textbook T2 |
| W38 | Proposal auto-resolution (`concierge/proposal_automation.py:203-267,458-616`) | Act (apply group decision) | resolver authority re-derived at resolve (`:479-487`); canonical gateway apply (`:488-499`) | itinerary | — | product@L2 | group | receipt card + push (`:510-566`); honest accepted-but-failed semantics | **P** — `lazy_consensus` treats silence as consent (`:365-394`); defensible only if `approval_mode` counts as Occasion constitution (§3 order), and the mode is set by proposer/agent, not group setting |
| W39 | **Proposal-silence recorder** (`proposal_automation.py:675-727` → `record_interaction(source_type="silence_observed")` → per-member `social_signals` rows) | none | none → automatic on resolve | `social_signals` ("X did not vote on 'Y'", named person) | indefinite; no expiry | engagement_pattern → person@durable from silence | trip | none | **N** — §11 bullet 2 (silence as durable person inference), §3.3. The conforming counterpart already exists: aggregate `notification_state.response_pattern` (W46) |
| W40 | Trip digests / end-of-trip summary (`digest/engine/daily.py:111,180`, `digest/engine/summary.py:35-147` → `trip_digests`; nightly loop `api/lifecycle.py:1565-1571`) | system synthesis | pipeline; **no member authored it** | `trip_digests`, served whole to any member (`api/routes/trips.py:2181-2205`) | indefinite upsert; no §3.3 occasion-end discard (ABSENT) | occasion→group L4; also the inlet to Personal Memory (`refresh_memory.py:833-877`, `what_worked`/`what_didnt` retained by design) | **group-visible** | none | **N — worst group writer.** `generate_trip_summary` reads ALL members' trip-scoped observations **including private ones — no `shared` filter** (`summary.py:56-70`); the privacy scrub is verbatim-corpus redaction that **fails open** ("proceeding unscrubbed", `summary.py:110-115`) — the inverse of the fail-closed posture in `_group_guard.py:209-217`. Violates §3.6 (private→group audience without grant), §3.3, §11 (laundering layer), and the contract's Failure posture |
| W41 | Expense log/settle from group chat (`concierge/tool_handlers/expenses.py:43-217,354+`) | Keep/Act | settle refuses tool-supplied `from_user_id` (`:376-387`); log imposes equal shares on every member (`:144-166`) | `expenses` | — | product@L2 | group ledger | settlement cards (`concierge/settlement_receipts.py:247,412`) | settle **C** (exemplary); log **P** — T1-applied group-material consequence, mitigated by ledger visibility + edit-undo |
| W42 | Experience-graph occasion lifecycle (`domains/experience_graph/commands.py`: create_occasion `:915`, invitations `:967,1060`, leave `:1246`, decisions `:1445,1520`, occurrence evidence `:2084`, outcomes `:2154`) | full gesture vocabulary | user-authored authority required (`:95-110`); idempotent action receipts on every mutation (`:224-248`); shared Outcome requires shared Commitment (`:2195-2196`) | graph tables | revisioned | per-mutation | participant-gated | receipts per mutation | **C — the conforming exemplar**; registered API (`api/router_registry.py:42,142`) but ABSENT from any live chat writer path — dormant as the §13.7 canonical-owner target |

### 2.4 E5 — Proactive turns

| W | Writer (entry) | Gesture/job | Authority → effective | Target owner | Retention | Learn | Receipt/Undo | Verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | 
| W43 | `run_proactive_turn` (`concierge/triggers.py:20-324`; arbiter single-exit `notifications/arbiter.py:277-317`) | system-initiated turn | group-branch privacy scrub **fails closed** (`triggers.py:186-210,348-377`); private-target routing refuses group fallback (`:96-124`) — but the turn is a **full agent loop**: `observe` stays armed (`_tools_select.py:52-64`) and proactive turns ADD tools (`:779-780`); acting principal = session owner (organizer for group sessions, `triggers.py:134-147`) | `messages` (system + reply), `proactive_events` (`:150,265,298`) | — | a machine-initiated turn can create person-level observations whose `evidence_origin="user_message"` points at a **system-authored** message (`memory_tools.py:820-828` + `triggers.py:212-214`) — provenance mislabeling | attention/turn rows | **P** — audience/routing conforming; authority axis non-conforming in reach (§3: model judgment never expands authority; §13.3 no proactive no-write posture) |
| W44 | Notification outcomes + state (`notifications/state_updater.py:52-241,573-627,358+,456`) | system | group copy must carry verified `group_composed` provenance or the write raises (`:88-89`); stored-copy redaction leaves a durable privacy-event receipt (`:116-137`) | `notification_outcomes`, `notification_state` | — | product/situation@L0-L2 | trip-level "Learning:" annotations, deliberately not per-member (`:594-601`) | **C** |
| W45 | Response-pattern learning (`state_updater.py:632-663` → `notification_state.response_pattern`/`engagement_velocity`, `core/db/_tables/notifications.py:49-51`; consumed by `notifications/gates.py:220`, `notifications/accept.py:23-24`) | system | aggregate counters | notification state | — | silence/ignore used exactly as §3.4 permits: aggregate, trip-scoped, gates future interruptions, never narrative | n/a | **C — the conforming counterpart to W39** |
| W46 | Decision/holdout ledger (`core/db/notification_decisions.py:29-79,116-163`; `notifications/incrementality.py:108`) | system | propensity-logged, content-free | decisions table | — | product@L0 | n/a | **C** |
| W47 | AttentionReceipt ambient ledger (`core/db/proactive_events.py:30-58`; callers `core/ambient_dispatch.py:140,625`; flag-gated; purge exists `core/db/retention.py:111-128`) | system | content-free by contract ("private prompt/copy/place context must never be smuggled into it") | proactive_events | purged | product@L0 | n/a | **C** |
| W48 | Arbiter suppressions (`notifications/arbiter.py:1590-1630` → `core/db/arbiter_suppressions.py:19-49`) | user "Not now" | time-boxed, type-scoped, duration-expiring | suppressions | expires | product@L2 | dismissal honored | **C — exemplary §3.3/§3.4** |
| W49 | `send_nudge` (`notifications/push.py:567-691`) | Address (actor→target) | user-initiated; spine cooldown/dedup/gates | push + **group-visible card in the shared conversation** (`:652-671`) | — | product@L2 | outcome row | **P** — the room-wide projection widens the *target's* audience without their grant (§3.6); flag for product ruling |
| W50 | Group interjection (`notifications/group_interjection.py:606-664`) | system | cooldown stamp conforming; `_record_interjection_signal` is a structural no-op (submits `source_type="agent_message"`, which intake rejects, `social_state/retriever.py:148-150`) | conversations stamp | — | — | — | **C** (signal writer dead-in-effect; cleanup candidate) |
| W51 | Attendance-derived affinity (`tasks/trip_attendance_affinity.py:169-229`, per `trip.completed` `:242-277` → `traveler_place_affinity`) | system | weight 0.0 (`:71`), `signal_source="trip_attendance"`; per-member participation rows honored with `did_not_happen` suppression (`:77-151`); membership fallback otherwise | affinity rows | — | person@L3-custody at zero weight — convention-held safety (readers gate on weight ≥ 1.0) | none | **P** — §5 fallback infers occurrence from membership; mitigated by zero weight + provenance + participation override |
| W52 | Occasion reconciliation (`tasks/occasion_reconcile.py:19-39` → `core/db/occurrence_reconciliation.py:453-553`) | system → user-resolved proposals | proposal-only staging (`proposal_only: True`), on-conflict-do-nothing; user resolves (`:571`) | occurrence proposals + evidence | evidence append-only, **no retraction API**; §3.3's "occasion end + 72h window / discard after reconciliation" has **zero implementation** (ABSENT in `tasks/`, `retention.py`) | situation@L2 | proposals visible/correctable | **P** — write side conforming; expiry/repair DOCUMENTED TARGET |
| W53 | Surface exposure receipts (`lived_experience/exposure.py:80-150` → `user_events`) | system | content-free ("domain state and private frame values never enter telemetry" `:88-90`); idempotent; presentation-proof verification (`:127-140`) | user_events | — | product@L0-L2, consumed only by ranking rotation (`home/concierge_feed/ranking.py:230`, `places/sections.py:365`, `core/surface_ownership.py:338-342`); no person-claim promotion found (ABSENT) | n/a | **C — reference implementation of §3.4's views/dwell rule** |

### 2.5 E6 — Reflection

Triggers and effective authority: post-session (`concierge/session.py:2515-2517`),
daily batch over every user with events in the last 24h
(`api/lifecycle.py:1519-1525` → `reflection.py:518-571`), post-trip
(`core/db/trips/crud.py:965-970`; debrief `api/services/trip_reflections.py:114-117`),
manual admin (`api/routes/admin.py:347-349`). **Effective authority for the
whole pipeline is the reflection LLM itself** — it chooses what becomes a
durable observation, at what importance, and when the identity narrative
regenerates, with no human admission step and no receipt.

| W | Writer (entry) | What persists | Verdict |
| --- | --- | --- | --- |
| W54 | Reflection `observe` (`reflection.py:714-762` → `execute_memory_tool(source_mode="reflection")` `:725-731` → `memory_tools._execute_observe:795-908` → `core/db/observations.py:143`) | Observations with provenance `{"evidence_origin": "agent_interpretation"}` (no source_message_id), Qdrant vector, `agent_events` audit row. Schema is a **stripped variant** (`:157-174`: only user_id/content/category/importance/trip_id — no visibility/context_scope/confidence/expires_at; lands `shared=false` by default) | **N (deliberate seam, verified current)** — §3.4 L1→L3 promotion without admission; three left-as-is items confirmed at current lines: the "Notice absence patterns… silence_observed signals" instruction (`reflection.py:111-116` — the 08-31 narrowing did NOT reach the reflection prompt), group agent-event folding `user_id is None` into one person's input (`:247-249`), and 8,000 chars of the group trip digest injected into the personal reflection prompt (`:598-603`) |
| W55 | Reflection prune (`memory_observations_prune` → `core/db/observations.py:484-514` + vector delete `memory_tools.py:1141-1143`) | is_active=false, actor-scoped, all-or-nothing | **C** mechanically; PM narrative repairs only at next synthesis (staleness guard catches retirement counts, `refresh_memory.py:441-461`) |
| W56 | Reflection-triggered `memory_refresh` (`concierge/memory_workflow.py:11` → arq → W57) + `reflection_log` (`reflection.py:765-783` → `observations.py:993`) + `pipeline_cursors` (`:461-464`) | audit/bookkeeping rows | **C** (audit-only) |

### 2.6 E7 — Memory synthesis

| W | Writer (entry) | What persists | Verdict |
| --- | --- | --- | --- |
| W57 | `refresh_personal_memory` (`concierge/refresh_memory.py:361` → `personal_memories`, `core/db/_tables/memory.py:41-61`) | Versioned identity-narrative markdown + `taste_dimensions`. Inputs: ALL active observations (`:405` — including `location_sample` GPS rows W12 and product markers W1f; no category exclusion), current PM, hard constraints, `get_active_facts(visibility="group")` (`:409-415` — the one real structural audience filter, because PM renders into BOTH 1:1 and group contexts); prior trip summaries still fold `what_worked`/`what_didnt` (`:829-874`) while the `group_dynamics_learned` inlet remains stripped (comment `:875-878` citing contract §11-12 — 08-31 fix holds). Prompt still writes "Who They Are" (`:61`), "Social & Group Dynamics" (`:76`), "Energy & Rhythm" (`:81`); private observations mitigated by paraphrase instruction (`:123-135`) + `[private]`/`[shared]` tags (`:768`) | **P** — custody, group-visibility filter, correction chokepoints (`:606-608` corrections; `:586-591` disputed DNA; `:649-662` reset-race guard; 10-version prune) are real. Open violations: **no receipt of any kind** — `emit("personal_memory.refreshed")` (`:698`) has exactly two listeners, both cache invalidation (`core/memory_subscribers.py:48-51`, `core/takes/subscribers.py:48`); the person is never told their narrative changed (§8). And admission-free L1→L3/L4 promotion (§3.4) persists by design |
| W58 | Group profile synthesis (see W36) | consumes W57's narrative (`group_synthesizer.py:272`, correction-filtered `:268-272`) | **P** (as W36) |
| W59 | Taste-DNA extraction + phrases (`refresh_memory.py:244,279` → `personal_memories.taste_dimensions`) | structured profile card material | **C** — the one lane with gesture + repair: dispute endpoints (`api/routes/users/me.py:667,731`) → `set_memory_correction` + feedback observation + durable re-synthesis (`workers/dna_dispute_refresh_jobs.py`) |
| W60 | `insert_fact` lifecycle (`core/db/user_facts.py:31-171`) | namespaced-key facts, advisory-lock supersede chain (`valid_to` + `superseded_by`, `:139-169`), full history | **C** — cleanest lifecycle in the system (see W4); one caveat: fact **retirements are not detected** by the synthesis staleness guard (`refresh_memory.py:437-440` comment) — a retired fact can survive in the narrative until an unrelated trigger fires |
| W61 | Place affinity accumulation (`core/db/place_affinity.py:147`; callers `core/save_application.py`, `core/itinerary_operation_commands.py`, W51) | weight rows with recency decay (`:56`); `retract_place_affinity` (`:297-340`) on unsave; user-state override (`:1033`) | **C** mechanically; positive-only accumulation without admission, weight-level not narrative |

### 2.7 E8 — Correction / release

| W | Writer (entry) | What it repairs | Verdict |
| --- | --- | --- | --- |
| W62 | Memory corrections (`core/db/memory_corrections.py:22-90` → `memory_correction_exclusions`, `_tables/memory.py:270-296`) | **Three propagation lanes, all real**: durable outbox row in the same tx (`:52-58` → `memory_projection_outbox`, `_tables/memory.py:303-346`, leased worker); after-commit event → group-profile revoke + Discover cache evict (`core/memory_subscribers.py:25-56`); policy-learning invalidation (`:81-90`). Applied at synthesis chokepoint (`refresh_memory.py:606-608`), runtime read (`memory_corrections.py:224-234`; markdown line-drop `:188-221`), group synthesis read, DNA filter | **C** on propagation — the model §8 implementation alongside Atlas; receipt is implicit-by-disappearance (no "here's what changed downstream" scope readback) |
| W63 | Atlas artifact delete cascade (`core/db/atlas.py:1104-1149`) | derived signals FK-cascade; sourced observations soft-deleted (`:1135`); timeline archived (`:1141`); Qdrant vector deleted (`:1143`); **kept-place affinity retracted** (`:1144-1148`) | **C — the reference cascade**; PM refresh delegated to route caller (`:1110-1111`) |
| W64 | Intake submission delete / revocation (`core/db/intake_v2.py:628-769`) | source payload scrub with `revoked_at`/reason (`:237-273,675-680`); dead-letters pending outbox (`:660-673`); **revokes derived interpretations** (`:693-700+`); forget receipt (`:188`); `intake_candidate_retracted` emitted for confirmed candidates (`:726-742`) → graph anchor retraction (`experience_graph_bridge.py:387+`) | **C** — cross-root revocation wired, not just local hiding |
| W65 | Account deletion (`core/db/account_deletion.py:783+`) | observation vectors (`:1031-1038,1448-1450`); S3 keys (`:1000-1026`); force-deletes `trip_group_profiles` for member trips incl. legacy `edited_by` scrub (`:1205-1233`); social_signals incl. JSON-ref legacy rows (`:1233-1242`); trip_social_state (`:1243-1250`); JSONB anonymization (`:476-576`) | **C — most thorough repair path in the codebase** |
| W66 | Retention purges (`core/db/retention.py:65-174`) | expired observations (hard DELETE `:65`), geofence events `:74`, audio `:92`, soft-deleted photos + S3 `:131-174` | **P** — `purge_expired_observations` does **not** delete Qdrant vectors (ABSENT: no vector import in `retention.py`); read-side hydration is the only backstop |
| W67 | Product-source observation retirement (`core/db/observations.py:517-536`; callers `api/routes/users/onboarding.py:185`, `users/privacy_facts.py:179`) | is_active=false by provenance source; **no vector delete on this path** — retired-row embeddings persist in Qdrant (read-side hydration backstop only, `memory_tools.py:990-1010`) | **P** — vector hygiene gap |
| W68 | Relationship-memory claim retraction (`core/db/relationship_memory.py:51-85,166,395`; callers `core/db/social_circles.py:495,779,851,894`) | typed `retracted`/`superseded` states; explicitly-shared descendants retracted (`:179`) | **C** |
| W69 | Trip-photo withdrawal (`api/routes/trip_photos.py:310-335` → `_soft_delete_photo:531-548`) | **a bare `deleted_at` UPDATE** — no event, no evidence retraction (occurrence_reconciliation is append-only: `record_*` only, `:100-334`; ABSENT: `retract_occurrence_evidence`/`retract_photo_evidence`), no reconcile re-run; bytes purged later by retention (`retention.py:131-174`) which also does not touch evidence rows | **N (verified current, deliberately-left item §1.3)** — §3.1 (withdrawn Source, surviving inference), §8 (Release repairs nothing downstream) |

### 2.8 E-client — Mobile-side durable writers

Client emitters land on `POST /api/events` (single/batch) via
`travel-app/utils/api/http.ts:3106-3118`; `data/events.ts:11-14` is the write
boundary. No client PostHog/Amplitude/Segment SDK exists (ABSENT:
`package.json` + greps).

| W | Writer (entry) | What persists | Verdict |
| --- | --- | --- | --- |
| W70 | Universal-search telemetry (`travel-app/utils/universalSearchTelemetry.ts:38-45`) | `query_len` + **`query_hash`** (`:41-42`) still computed and sent; hash is FNV-1a (`utils/stableHash.ts:7-14`) — low-entropy queries dictionary-reversible. Server now scrubs the hash before persistence (`api/routes/events.py:71,400,511` — 08-31 fix verified) | **P** — durable-state failure closed server-side; the client still transmits a re-identifiable fingerprint (deliberately-left item §1.4); Atlas telemetry uses the same hash pattern (`utils/atlasTelemetry.ts:56-73`) |
| W71 | Concierge-home telemetry (`travel-app/utils/conciergeHomeTelemetry.ts:38,43`) | **`card_title` — full rendered card-title text** + `fact_key`; the one emitter shipping rendered content strings (titles reflect personal inferences) | **P** — §3.4: content-bearing exposure telemetry stored as user_events |
| W72 | Ambient location push (`travel-app/hooks/useLocationPush.ts:66-72`; plus lat/lng attached to every chat send, `hooks/useConciergeChatTransport.ts:563-584`) | lat/lng/accuracy → durable server `last_location` ≥1/min while a trip is ACTIVE; chat-side feeds W12's observation rows | **P** — §3.3 window discipline server-side is the gap (see W12 **N**) |
| W73 | On-device residue that outlives sign-out (`travel-app/utils/accountTeardown.ts:46-65` clears an allow-list of six items; everything else persists by default) | expo-image disk cache (photos; zero `clearDiskCache` callers — `components/ui/AppImage.tsx:114`); **raw search query text** in recents (`utils/universalSearchRecents.ts:12,22`, `utils/placesSearchRecents.ts:5-15`); **provider receipt drafts with confirmationNumber/pricePaid** on a device-global key (`utils/providerReceiptDrafts.ts:3-31`); scan cursors, shadow evidence, perf stores | **P** — revocation/undo all operate server-side; nothing ties revocation to on-device residue (Together audit A10 extended) |
| W74 | Client receipt/correction surfaces (read-side inventory) | Memory receipt + "Correct or forget" (`app/atlas/memory.tsx:339-385`), data-use receipt (`app/you/data/receipt.tsx:1-33`), removed-rows recovery (`app/atlas/removed.tsx`), intake lifecycle receipts, in-chat receipt components (`components/chat/ChatReceiptDisclosure.tsx` etc.), occurrence `did_not_happen` correction (`app/(tabs)/trips/[tripId]/object/[kind]/[objectId].tsx:797`) | **C** — the client receipt surface is ahead of the backend's receipt production: the memory screens can render what W3/W57 never announce |

---

## 3. The six §8.3 fixture inputs mapped to current code paths

### F6.1 — Restaurant photograph (Point: "This texture is what I meant")

- **Chat lane (what fires today):** W1 message row; **W1b image bytes into
  `chat_images` + disk, indefinitely**; W2 vision summary baked into message
  metadata forever; W3 `observe` at model discretion (the authored Point CAN
  be preserved as an explicit observation — that part is the intended
  behavior); on a trip turn, W8/W9/W10 ambient writers also fire.
- **Share-sheet lane:** W23 intake v2 — conforming custody, but review-first
  (§2.2 verdict), so the Point's *meaning* arrives only after classification
  work.
- **Does it become a preference?** No automatic photo→preference path exists
  (ABSENT; save-effects affinity requires a save, W61). The pixels do not
  become taste; the risk is discretionary `observe` phrasing, not a wired
  writer. The photo's *meaning coming from the authored Point* has no durable
  representation beyond observation text — there is no Point-object linking
  photo + utterance + the nested pasta question (DOCUMENTED TARGET, handoff
  §8.3.1).
- **Verdict: partially conforming.** Immediate value works; Source custody
  violates §3.2/§3.3 in the chat lane (bytes + interpretation retained
  forever with no receipt); quiet placement in Life is ABSENT (a chat photo
  lands in no Life-addressable object).

### F6.2 — Movie ticket (Bring: proves attendance, not opinion)

- **Share-sheet lane (conforming):** W23 → semantic candidates
  (`truth_mode="source_extracted"`) → owner confirm → private
  `experience_anchors` at most **`AnchorState.ticketed`** — "a confirmed
  source is not enough to make an operational anchor active"
  (`inbound/anchor_compiler.py:214-231`); contradiction → cancelled;
  unresolved place/time → held. **Ticket ≠ attendance ≠ interest is honored
  structurally** (§5 ladder). No ticket→affinity path exists (ABSENT).
- **Chat-paste lane (risk):** W1b bytes retained; `inbound_screenshot_submit`
  (W15) routes into the v1 lane where a high-confidence guess can auto-write
  a save/accommodation without the owner (W26).
- **Later cross-medium connection:** DOCUMENTED TARGET only — no reader
  connects a ticketed anchor to other media today.
- **Verdict: conforming on the v2 lane; the v1 chat-paste lane is the
  non-conforming shadow.**

### F6.3 — Voice observation (Point; must not become personality)

- Live voice turns run the ordinary concierge loop with `modality="voice"`
  (built, gated off in prod by absent LiveKit/Deepgram credentials —
  `voice/FEATURE.md`); observations stamp `source_mode='voice'`. A voice memo
  *file* arrives via share → intake v2 audio; a pending chat turn will not
  send until the derived transcript's custody verifies
  (`core/db/pending_chat_turns.py:279-294`).
- **Personality protection:** SKILL_MEMORY now prohibits inferred
  personality/mood (`_prompts_skills.py:1537-1539`), but the protection is
  prompt-level, not structural: the un-narrowed reflection prompt (W54), the
  ambient social-signal extractor's `individual_state`/`energy_state`
  dimensions (W10), and synthesis's "Who They Are"/"Energy & Rhythm" sections
  (W57) all remain live consumers of conversational exhaust.
- **Verdict: partially conforming** — the authored observation is preservable
  and attributable-by-provenance (though `observations` still has no author
  column, §4 item 2), and nothing structurally prevents its later promotion
  into personality narrative.

### F6.4 — Friend's addressed note (Share/Address with independent axes)

- **Nothing conforming can fire today.** Person-to-person addressed
  contribution has no model: audience recipients exist only on the in-flight
  `ContributionAudience` (`core/models/contribution.py:97-101,174-189`), never
  on a durable row; no durable grant object exists (Together audit §1.11 —
  nine of thirteen grant fields have zero backend occurrences); the together
  projection transport 403s pending "graph-owned sharing authorization"
  (`api/routes/artifact_projections.py:51-55`). The nearest durable precedent
  remains single-purpose place handoffs (`core/db/place_handoffs.py:579-663`).
- If the note physically arrives (pasted text/file), it enters the
  *recipient's* intake custody: authorship collapses to the recipient, and the
  five axes cannot be represented (`Addressed to you` establishes nothing).
- **Verdict: ABSENT** — this fixture is unimplementable until Checkpoint 1's
  13-field grant record (the durable promotion of `ContributionAxes`) exists.

### F6.5 — Forwarded booking email (Source custody vs occurrence truth)

- W24 end-to-end: webhook signature + path-secret verified
  (`api/routes/inbound_email.py:93-111`), unknown alias accept-and-drop
  (`:116-121`) → one verified inline-text source + one `provider_archive`
  custody-only object (`core/db/intake_v2.py:539-625`) → `source_extracted`
  observations → candidate mapping to at most `ticketed` — the parser writes
  **no reservation/itinerary rows and no occurrence claim**; consequence
  proposals stay PROPOSE-mode descriptors (`inbound/consequence_bridge.py:46-55`).
- **Verdict: conforming** — the §5 "tickets prove purchase or schedule, not
  boarding" ladder implemented. Caveats: alias-spoofing (W24), the
  NULL-`retention_expires_at` stall gap (W23), and the legacy v1 fallback's
  phantom 30-day purge (W25) one env-flag away.

### F6.6 — Ask with a Source ("What does this ticket say?")

- **Chat-attachment lane (the lane users actually have): NOT no-write.**
  Before any gesture resolution the turn durably writes the message row (W1),
  the image bytes forever (W1b), a Haiku interpretation of the source baked
  into history forever (W2), and a content-bearing `concierge_turns` row
  (W1d); `observe` remains armed (W3). `answer_only` is not consulted
  anywhere in the ordinary turn path (`concierge/turn_admission.py` handles
  idempotency only; grep `answer_only|requested_retention` in `concierge/`:
  compat re-exports only).
- **Share→chat lane: truly T0** — `requested_retention="answer_only"`,
  custody re-verified at send, 24h TTL (W31). **But it is unreachable**: the
  `from_chat=1` branch that admits a share directly into an answer-only chat
  turn has zero callers (`travel-app/utils/routes.ts:641`; repo grep).
- **Verdict: non-conforming on the reachable lane (§8.6 gate "Ask remains
  no-write" fails); conforming on a built lane no user can reach.**

---

## 4. Remaining laundering paths (conversation / silence / mood / personality / repeated topics → durable memory)

The four deliberately-left items from the 08-31 pass, verified current, plus
what this audit found beyond them. Ordered by blast radius.

| # | Path | Status | Evidence |
| --- | --- | --- | --- |
| R-01 | **Trip summary / digest: every member's observations — private included — synthesized into a group-visible retrospective, with a fail-open scrub** ("proceeding unscrubbed") | NEW, live | `digest/engine/summary.py:56-70,110-115`; served `api/routes/trips.py:2181-2205`; inverse of the fail-closed `_group_guard.py:209-217` posture (W40) |
| R-02 | **Ambient social-signal extraction per group message** → durable person-attributed `energy_state`/`individual_state`/`engagement_pattern` rows, no expiry, no receipt | NEW, live | `concierge/agent.py:1582-1598`; `social_state/retriever.py:106-179`; `core/db/_tables/trips.py:340-388` (W10/A2) |
| R-03 | **Proposal-silence recorder**: named-person "did not vote" rows via `silence_observed` | NEW, live | `concierge/proposal_automation.py:675-727` (W39); reflection prompt then instructs reading these signals (`reflection.py:111-116`) — a chained silence→signal→reflection→PM lane |
| R-04 | **SKILL_GROUP_DYNAMICS + SKILL_SPENDING_CONTEXT**: durable psych/silence writes into `trip_briefs` ("who defers… who checks out when energy is low", "a pointed silence", "Alex went quiet when €80 restaurants were suggested") — the 08-31 narrowing did not reach the trip-brief skills | NEW, live | `_prompts_skills.py:2113-2143,2145-2177`; writer `tool_handlers/memory.py:25-62`; ungated AGENT_MAINTAINED table with no member-facing read route (W7) |
| R-05 | **Reflection**: silence instruction, `user_id is None` group agent-event folding, 8,000-char group digest in the personal prompt, stripped observe schema | DELIBERATELY LEFT — verified current | `reflection.py:111-116,247-249,598-603,157-174` (W54) |
| R-06 | **GPS piggyback**: every located chat turn writes `location_sample` observations into the person store with no expiry; synthesis has no category exclusion | NEW, live | `concierge/location_persistence.py:22-123`; `refresh_memory.py:711-757` (W12) |
| R-07 | **Member brief + trip journal**: per-turn Haiku inference about persons ("reacted positively"), hidden `[agent:]` register, future group-artifact framing | NEW, live | `concierge/notes.py:329-336,345-363`; `doc_updates.py:75-123` (W8/W9) |
| R-08 | **Ask-source retention**: chat image bytes + vision summaries retained forever regardless of gesture | NEW, live | `core/db/chat_images.py:62-118`; `concierge/vision_summary.py`; `persistence.py:343-371` (W1b/W2) |
| R-09 | **Proactive turns** keep the full person-write tool surface with `evidence_origin` mislabeled as user evidence | NEW, live | `concierge/triggers.py:134-147,212-214`; `_tools_select.py:52-64,779-780` (W43) |
| R-10 | **Observations author column** still ABSENT (provenance JSONB only; `source_mode` CHECK is the only typed authorship trace) | DELIBERATELY LEFT — verified current | `core/db/_tables/memory.py:359-447` |
| R-11 | **Photo withdrawal cascade** still a bare tombstone; occurrence evidence append-only, no retraction API | DELIBERATELY LEFT — verified current | `api/routes/trip_photos.py:531-548`; `core/db/occurrence_reconciliation.py:100-334` (W69) |
| R-12 | **Client query-hash emitter** still transmits; server scrubs before persistence (08-31 fix verified) | DELIBERATELY LEFT — verified current | `travel-app/utils/universalSearchTelemetry.ts:41-42`; `api/routes/events.py:71,400,511` (W70) |
| R-13 | `concierge_turns` full-text per-user telemetry, no purge; `card_title` content strings in client exposure telemetry | NEW | `concierge/telemetry.py:235-324`; `travel-app/utils/conciergeHomeTelemetry.ts:38` (W1d/W71) |
| R-14 | Group digest `what_worked`/`what_didnt` → Personal Memory (by-design residual of the 08-31 fix); fact retirements undetected by the synthesis staleness guard | KNOWN residuals | `refresh_memory.py:833-874,437-440` (W57/W60) |
| R-15 | Qdrant orphan vectors on provenance-source retirement and retention purge (read-side hydration is the only backstop) | NEW | `core/db/observations.py:517-536`; `core/db/retention.py:65` (W66/W67) |

---

## 5. Gaps vs the §8.2 loop — where the lifecycle breaks today

```text
Ask / Point / Bring / Keep / Address in Chat
  -> immediate value                       WORKS (chat + intake both deliver)
  -> only authorized durable consequence   BREAKS: 14 non-conforming writers;
                                           ambient exhaust writers fire on
                                           every turn regardless of gesture
  -> quiet placement in Life               BREAKS (structural): a chat
                                           contribution lands in no
                                           Life-addressable object — observations,
                                           briefs, signals have no durable
                                           address, no member-facing surface
                                           (trip_briefs has no read route);
                                           ONLY the intake v2 lane produces an
                                           addressable private anchor
  -> connections to existing objects       intake candidates → anchors exists;
                                           cross-medium / cross-root connection
                                           is DOCUMENTED TARGET (no reader)
  -> later admitted value in Home/Places   PARTIAL: save-effects affinity and
                                           PM-fed ranking exist; the explicit
                                           consent lane (group_and_learn) has
                                           NO consumer; no surface can say
                                           "this contribution changed X"
  -> optional shaping in Chat/Plan/Occasion WORKS (proposals, pending turns)
  -> authoritative readback                SPLIT: real for itinerary/booking/
                                           facts (receipts + postconditions);
                                           ABSENT for observe and synthesis
  -> causal receipt only if changed        BREAKS in the opposite direction:
                                           synthesis changes the narrative
                                           SILENTLY (zero receipt listeners
                                           beyond cache invalidation) — the
                                           "only if" clause is unfalsifiable
                                           to the person
  -> refinding, correction, release,       STRONG for memory-corrections /
     withdrawal                            Atlas / intake / account deletion;
                                           BROKEN for photo withdrawal, chat
                                           transcript (no redaction), vectors
                                           (two orphan paths), on-device residue
```

The loop's three load-bearing breaks, in order:

1. **Quiet placement** — the contract's evidence chain (Source → Observation →
   Claim → owner → projection) is implemented end-to-end only in intake v2.
   Chat, the "lowest-friction entry" (§9), produces durable exhaust rather
   than addressable contributions. Workstream D's design cannot render "where
   it becomes findable in Life" for chat contributions because there is no
   there.
2. **Later admitted value** — the one explicit learning consent
   (`group_and_learn`) awaits a consumer, while unconsented ambient lanes
   (social signals, briefs, GPS) feed real consumers. The product currently
   delivers later value from the material people did NOT deliberately give,
   and no value yet from what they did.
3. **Causal receipt** — receipts fire for canonical-owner mutations (T2-ish)
   but never for the person-level narrative (the thing §8 most wants
   witnessed). The client receipt surface (W74) is already built to render
   more than the backend announces.

---

## 6. Open questions for the founder

1. **Ordinary-turn admission (migration step 3 scope).** `answer_only`
   admission exists and is enforced in the pending-turn lane only. Should the
   contribution envelope's retention axis be wired into `turn_admission.py`
   (per-turn posture: continuity-read/no-write unless a gesture resolves
   otherwise), covering the plumbing writers (W1b/W2/W1d) — or is chat
   transcript custody declared out of the envelope's scope?
2. **Ambient-writer kill/keep list.** Journal (W8), member brief (W9), social
   signals (W10), silence recorder (W39), trip-brief dynamics/spending
   (W7/R-04): which survive behind an envelope + receipt, which are removed
   outright? The conforming replacements already exist in-house
   (aggregate response_pattern W45; occasion-scoped proposals W52).
3. **Trip-summary failure posture (R-01).** Authorize flipping
   `summary.py:110-115` to fail-closed (and adding a `shared` filter at
   `:56-70`) ahead of the migration order, as was done for the four 08-31
   fixes? This is the widest private→group aggregation in the codebase.
4. **Trip-brief skill narrowing (R-04).** Apply the same narrowing given to
   SKILL_MEMORY on 08-31 to SKILL_GROUP_DYNAMICS and SKILL_SPENDING_CONTEXT
   (silence/psych content out; logistics/stated-preferences stay)?
5. **Ask-source custody (R-08).** Adopt §3.3's ≤24h rule for `chat_images`
   (TTL + purge job) and give vision summaries an expiry or re-derivation
   policy? Both currently retain forever with no user-visible trace.
6. **Location samples (R-06).** Exclude `location_sample` from synthesis
   input and give those observations a Moment-scoped expiry?
7. **Value-first share capture (migration step 9).** The T0 `from_chat` lane
   is built and unreachable. Wire the OS share sheet to it (answer-first,
   review-on-demand), or keep review-first pending the Workstream D design?
8. **`group_and_learn` reader.** Before any consumer lands, which §3.4
   target/level does photo-learning resolve to — and does the consent sheet's
   pre-selected escalation (`GroupAndLearnConsentSheet.tsx:26-41`) need to
   default down?
9. **Synthesis receipt (§8).** When Personal Memory regenerates, where does
   the causal receipt surface — Life (per the §8.2 loop), the memory screen,
   or chat? The event bus hook (`personal_memory.refreshed`) already exists
   with zero user-facing listeners.
10. **Proactive no-write posture (R-09).** Should proactive turns drop
    person-level write tools (or the envelope check `initiator.kind !=
    person` force T0), and should `evidence_origin` distinguish
    system-authored source messages?
11. **Occasion-inference expiry (§3.3).** `social_signals`,
    `trip_social_state`, `trip_digests`, and reconciliation evidence all
    outlive the occasion indefinitely; the 72h reconciliation window has zero
    implementation. Is a trip-end expiry sweep authorized as its own slice,
    or folded into the revocation-bus workstream?

---

## 7. Status

- Writer inventory + conformance table: **complete at audit scale** (this
  document; audit only, no code changed).
- Contribution envelope / policy gate: **Architecture resolved** (shadow-only;
  unchanged).
- Intake v2 lane: **Implemented** and largely conforming (two retention gaps).
- Ordinary-chat no-write posture, quiet placement, causal receipt: **ABSENT /
  DOCUMENTED TARGET** — the Workstream D design should treat these as new
  construction, not wiring.

---

## 8. Applied fixes

### Safety batch 2 — 2026-08-31


Two narrowly-scoped fixes applied in the working tree (uncommitted), answering
founder questions 3 and 4 above. Verified against code before editing; golden
prompt snapshots regenerated via `UPDATE_GOLDEN=1`.

1. **R-01 / W40 — trip summary visibility filter + fail-closed scrub**
   (`backend/digest/engine/summary.py`):
   - Observation query now requires `shared IS TRUE`
     (`summary.py:69`) — only group-visible observations feed the
     group-visible retrospective. Comment records that the scrub is a
     backstop, not a substitute for source filtering.
   - The privacy scrub now fails CLOSED (`summary.py:113-130`): on any scrub
     error the generation logs at ERROR, sets `skipped`, and returns without
     persisting — the input hash is not stored, so the nightly loop retries
     on its next pass. Previously it logged "proceeding unscrubbed" and
     persisted.
2. **R-04 / W7 — trip-brief skill narrowing**
   (`backend/concierge/_prompts_skills.py`):
   - `SKILL_SPENDING_CONTEXT` (`:2113-2145`): removed silent-budget-pressure
     inference ("Alex went quiet when €80 restaurants were suggested", "they
     go quiet… stop engaging"), removed the `## Private pressure` section;
     now instructs recording only stated ceilings/ranges/decisions, with an
     explicit "Do NOT infer budget pressure from silence, mood, or who stops
     engaging… silence is not signal you may keep."
   - `SKILL_GROUP_DYNAMICS` (`:2147-2179`): removed psych/silence tracking
     ("who defers", "quiet voters", "private tensions", "Sarah stopped
     engaging", "a pointed silence", disengagement/role-shift solicitation);
     retained operational content only (stated decision roles, stated
     presentation preferences, explicit commitments, logistics), with the
     same explicit prohibition mirroring the 08-31 SKILL_MEMORY narrowing.
   - Golden snapshots regenerated: `tests/concierge/golden_prompts/12_concern_briefs_active.md`
     (this batch); files 04/05/08-11 in the same directory carry the prior
     08-31 batch's uncommitted regeneration.

Validation: `tests/digest/` + `tests/concierge/test_prompt_golden.py` +
`tests/concierge/test_concierge.py` all pass offline (`-m "not
requires_postgres and not requires_api_keys"`); mypy clean on both touched
modules; ruff check/format clean.

Deliberately deferred (unchanged, per scope):

- **Chat-image TTL (R-08 / W1b/W2)** — retention is gesture-dependent
  architecture; awaiting the envelope design.
- **Silence-row reflection read (R-03 / W39)** — `silence_observed` rows are
  operational vote state; only characterization *instructions* were in scope.
  The reflection prompt's instruction to read these signals remains.
- **Addressable-object gap (§0 headline 3)** — Workstream D new construction.
- **Noted in passing:** `digest/engine/daily.py:158-164` retains the same
  fail-open scrub posture ("proceeding unscrubbed") for the daily digest, and
  the daily gatherer (`digest/engine/_shared.py:298-313`) reads observations
  without a `shared` filter — same class of issue as W40, not covered by the
  batch-2 authorization, left for a founder ruling.

### Safety batch 2 extension — daily digest, same class — 2026-08-31

The batch-2 agent flagged that `digest/engine/daily.py` carried the
identical fail-open scrub and `digest/engine/_shared.py`'s daily gatherer
read all members' observations with no `shared` filter (same class as
W40, outside that batch's authorized scope). Applied under the same
precedent, same pattern as `summary.py`:

- `digest/engine/_shared.py` (~line 300): daily-window observation query
  now requires `obs_table.c.shared.is_(True)` — only group-visible
  observations feed the group-visible daily digest.
- `digest/engine/daily.py` (~line 158): scrub failure now fails CLOSED —
  logs at ERROR, sets `result.skipped`, returns without persisting; the
  input hash is not persisted on that path so the next cycle retries.

Verified: `tests/digest/` 80 passed offline; mypy clean on both touched
files (pre-existing errors in transitive imports only). Uncommitted.
