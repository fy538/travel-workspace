# Concierge (Vesper) — System Charter

> Surface: Vesper
> Maturity (for MVP): MVP-required
> Status: wired (not yet validated end-to-end on-device against live backend)
> Last updated: 2026-08-29

## Purpose
Vesper's primary conversational operating surface and the lowest-friction
interface into its lived-world intelligence. It accepts Ask, Point, Bring,
coordination, correction, and action; inspects and composes across canonical
objects; calls tools; streams; prepares or executes authorized consequences;
monitors and reconciles work; and hands durable effects to their owners. The
input loop is one loop through Chat, not Chat's sole role. Chat owns
conversation, not memory, Plan, Place, Occasion, Commitment, Source, provider,
or artifact truth.

## Spans (cross-repo)
- Backend: [`travel-agent/backend/concierge/`](../../travel-agent/backend/concierge/FEATURE.md) (96 files) — runs on the shared `core/agent_loop.py` (custom Anthropic tool_use loop, **not** LangGraph).
- Frontend: `travel-app/app/(tabs)/concierge/*`, `trips/[tripId]/chat`, `components/chat/*` (44), `hooks/useConciergeChat`, `useGroupChat`, `utils/sse.ts`.
- Tables of record: `conversations`, `conversation_participants`, `messages`, `concierge_turns` + reasoning/quality telemetry.

## Public interface (what other systems may call / read)
- **Inbound (FE → BE):** `POST /api/trips/{id}/messages` (blocking) · `/messages/stream` (SSE) · `POST /api/trips/{id}/concierge/narrate`.
- **Entry points (internal):** `session.py::ConciergeSession.send_message[_streaming]()`, `agent.py::handle_turn()`, `triggers.py::run_proactive_turn()` (the common path for all system-initiated messages).
- **Consumes:** Memory & Preference (`get_group_context`), Planning, Booking, Research, Places, Situation — **all via tool calls, never direct imports** (lazy cross-agent imports are the only exemption; see `CLAUDE.md`).
- **Never:** other systems must not compose group-bound text directly — `group_compose.py` is the only sanctioned path (it strips attribution).

## Owns (source of truth)
The conversation thread and turn telemetry. Personal/group memory is **owned by
Memory & Preference**—but Concierge may emit only contribution-authorized
observations, not whatever the model considers worth remembering.

## Invariants (must always be true)
- **Privacy egress:** never reveal an individual's private constraint to the group (belief #3/#8). All group-bound text flows through `group_compose.py`; free-text replies into a group conversation are **not delivered** under strict mode.
- **Grounding:** every recommendation is grounded in the knowledge base; output grounding guard runs on every reply (`output_guards.py`).
- **Fail-open context:** a single failed per-turn context loader returns empty, never aborts the turn (`turn_context.py`).
- **`<notes>` are stripped** from the user-visible reply before return.
- **Guardrail** runs on every user turn (prompt-injection→block, self-harm→988, abusive→block); skipped only for proactive turns.
- **Telemetry origin** is tagged on every `concierge_turns` row; eval/test/synthetic never pollute production dashboards or traces.
- **Contribution boundary:** every durable observation, fact, note, reflection,
  Occasion contribution, Plan mutation, audience effect, or external action
  follows [Contribution and Consequence](contribution-and-consequence.md). Ask
  defaults to no new durable personal state.
- **Value before workflow:** a complete answer may end. Point/Bring may apply
  only private source-bound reversible state before a compact receipt; material
  audience or real-world effects stop at their authorization boundary.
- **Gesture follows language and affordance:** an attachment supporting a
  question is transient Ask; a Source sent alone or through share/forward/Add
  is Point/Bring; explicit Keep admits only the named layer. No classification
  prompt precedes value.
- **Connected context is narrow:** a connector read grants only the current
  named purpose and fields. It does not authorize retention, inference,
  audience expansion, provider action, or write-back.
- **Agentic owner handoff:** a surface-originated turn retains its selected
  `ResourceRef`s and return target. Chat may inspect, compose, propose, act,
  monitor, reconcile, or repair across owners, but canonical readback and the
  owner projection—not assistant prose or a rendered artifact—decide what
  happened.
- **Contribution and action remain independent:** information supplied for a
  job does not grant a durable write, and a successful authorized action does
  not grant broader retention, inference, or audience authority.
- **Direct manipulation remains available:** simple, visible, low-risk owner
  operations should not require Chat. Conversation earns ambiguous,
  compositional, cross-owner, monitoring, and repair work; structured
  projections operate on the same owner state.

## Failure modes
- Tool error → structured feedback to the loop (classifier + retry budget), not a crash.
- Re-anchor at ~iteration 7 if the model loops without converging.
- Model/provider error → surfaced via `core/llm.py` retry/backoff; turn fails loud rather than fabricating.

## Maturity & validation
- Serves journeys: 01 (vague→shaped), 04 (private constraint→group-safe), 05 (propose→mutate), 07 (discover→contextual), 08 (live what-now).
- DoD state: backend replay tests ✅ · grounding/privacy guards ✅ · **mock-walk ❌ · Maestro on-device ❌ · live-walk ❌**.
- Dark/flagged: narration text ships (persists as `message_type='narration'`); the live mic path is dark — the `voice` process is defined in `fly.toml`, but its machines remain at `count=0`, the required `VOICE_*` credentials are unset, and the client gate (`EXPO_PUBLIC_VOICE_ENABLED`) stays false with the SDK uninstalled.

## Canonical docs
- why → `product/Concierge Behavior Spec.md` · how → `architecture/Conversation System Architecture.md` · what(be) → `backend/concierge/FEATURE.md` · what(fe) → `travel-app/docs/page-specs/agent-chat.md` (§2 transport) + `travel-app/docs/design-decisions/agent-chat.md` (locked UX) · **cards / arrival SSOT** → [`Card Catalog.md`](../Card%20Catalog.md) + [`contracts/card-arrival.json`](../contracts/card-arrival.json).
- Tests: `tests/concierge/*`, eval `configs/` (~21 concierge scenarios) + CI replay baselines.

## Cross-cutting constraints
- **Contribution and consequence:** Chat transport is not retention authority.
  Use the shared gesture, structured five-axis authority, scoped learning,
  purpose, treatment, owner-handoff, and repair contract in
  [contribution-and-consequence.md](contribution-and-consequence.md).
- **Graph legibility**: every new "the model knows X → should we show it?" decision must be evaluated against [graph-legibility-doctrine.md](graph-legibility-doctrine.md) before building. The short rule: show as behavior, not as a label; explicit personal-memory controls live in You.

## Open risks / known gaps
- The current first-turn path still classifies a private no-trip conversation
  as `INTAKE`, normally restricts it to an intake scratchpad lane, and suppresses
  first-turn `COMMIT` agency. This is legacy product-model debt: first-turn
  requests may be reads, comparisons, Plan/Occasion shaping, monitoring, or
  authorized action. The target fixture and semantic tool migration are in
  [Agentic Chat cross-surface fixture
  pack](../working/agentic-chat-cross-surface-fixture-pack-2026-08-29.md) and
  [Agentic capability and tool cutover
  plan](../working/agentic-capability-and-tool-cutover-plan-2026-08-29.md).
- The model-visible tool catalog remains Trip/itinerary-heavy and includes
  presentation and maintenance operations. Legacy itinerary writers retain
  authority during migration, but model-facing semantics should move to Plan,
  Occasion, Commitment, Source, Place, Occurrence, Outcome, provider, monitor,
  and receipt operations behind compatibility adapters.
- The current modular memory prompt and `observe()` description still authorize
  same-turn preference, personality, mood, emotional-investment, and silence
  inference without the shared policy gate. This is target-contract debt, not a
  behavior to preserve while adding new surfaces.
- The privacy-egress invariant is the **unrecoverable-trust-event** risk — the highest-value thing to verify with a live group walk (journey 04).
- `conversation_locations` is a **phantom table** (reverted feature) — any query against it fails at runtime.
- Streaming SSE on RN uses a custom fetch parser (`utils/sse.ts`); the on-device streaming path is **still unvalidated on a release-profile device**. Cert lane + runbook: [`docs/working/card-arrival-device-cert-2026-07-30.md`](../working/card-arrival-device-cert-2026-07-30.md). Early card handoff (recent-history upsert on materialized `card_envelope`) is implemented in `useCardArrivalReconciliation` — mock Maestro `36-chat-card-arrival.yaml` covers visual morph only.
- Page-spec Round 1 narrative elsewhere may still describe pre-envelope attachment timing; treat **§2 Backend contract** in `page-specs/agent-chat.md` and the Card Catalog as authoritative for transport and cards.
