# Pre-Dogfood Area Audit 05 — Concierge Agent Loop, Tools & Output Guards

Date: 2026-05-21  
Scope: `handle_turn()` + shared `agent_loop.py`, concierge tool dispatch/handlers
(booking, itinerary, whereabouts), inline output guards, tool-error recovery/telemetry,
session integration, modular skill selection, LLM discipline.  
Mode: read-only; no product code, test, or config was modified.

## Summary

| Severity | Count |
|---|---:|
| P0 | 1 |
| P1 | 4 |
| P2 | 4 |
| TECH-DEBT | 3 |

**Biggest concern:** Week-1 output guards are wired and run on both non-streaming and
streaming paths in default `log` mode, but two integration bugs make the telemetry
misleading and one privacy check a no-op: (1) `result_preview` is stored as a JSON
**string** in production while `_names_from_tool_calls` only walks dicts/lists, so
search-grounded venue names never enter the allowed set — the grounding dashboard will
show mass false positives and `regenerate` mode would strip legit venues; (2)
`session.py` passes `channel=self.conversation.conversation_type` (`"personal"`) while
`_PRIVATE_CHANNELS` only accepts `"private"`, so **`third_party_disclosure` never fires**
in real 1:1 chats; (3) `log` mode ships every violation unchanged, so confabulated
venues and constraint narration can reach testers today — by design, but testers must
know guards are observe-only.

**Agent loop & tools:** No infinite-loop path found. `run_agent_loop` is bounded by
`max_iterations` (default 10), optional `max_wallclock_seconds` / token caps, and
per-tool 55s timeouts with exception isolation in `parallel_tools.py`. Tool failures
classify through `tool_error_feedback` with a per-loop `RetryBudget` (default 3
attempts per tool+args signature) and emit `tool_error` events. Parallel tool execution
does not crash sibling tools on one failure.

**Privacy compose:** `strict_group_compose` (Haiku launder → Sonnet recovery →
placeholder) is solid for **trip-scoped** group chats. Pre-trip / trip-less group
conversations bypass it (`is_group and has_trip`) — already filed as P0 in Area 01;
cross-reference only here.

**Skill selection:** `IDENTITY_CORE` always loads knowledge/tools/memory/user_facts/
experiences (privacy + grounding prose). `SKILL_COORDINATION` loads only when
`conversation_type == "group"`. Conditional skills are inclusive on ambiguity; ambient
turn detection avoids skipping recommendation skills on substantive messages.

---

## Findings

### [P0] — Confabulation and privacy violations ship unchanged in week-1 `log` mode

**References:**
- `Travel Agent/backend/concierge/output_guards.py:19-23` (default `log` — violations
  recorded, reply unchanged)
- `Travel Agent/backend/concierge/output_guards.py:1109-1115` (`guard_reply` never
  blocks or mutates reply in `log` mode)
- `Travel Agent/backend/concierge/session.py:451-456`, `468-510` (guard runs, then
  `complete_agent_message` with original `result.reply`)
- `Travel Agent/backend/concierge/session.py:1149-1219` (streaming path: comment
  explicitly states text already shipped; guard is log-only)
- `Travel Agent/CLAUDE.md:123-140` (activation runbook: do not flip `regenerate`
  without calibration week)

**Why it matters to a real tester:** A tester who sees the agent name "Joe's Pizza" or
narrate "$40–50/pp" in a group thread is seeing a real product failure, not a
dashboard-only warning. Guards may flag it in `concierge_turns.guard_violations`, but
the chat bubble is already delivered (non-streaming: after loop; streaming: before
guard). Dogfood week 1 is intentionally observe-only — operators must not treat green
chat as proof of grounding/privacy safety.

**Repro / deterministic test idea:**
1. Set `CONCIERGE_OUTPUT_GUARD_MODE=log` (default).
2. Force a turn whose reply contains a multi-word Title-Case venue not in tool
   results (eval fixture or mocked search returning empty).
3. Assert `guard_violations` contains `check: "grounding"` on the persisted turn row.
4. Assert the message body delivered to the client is **unchanged** (still contains the
   venue name).

**Suggested fix direction:** Keep `log` for week 1 per runbook. For dogfood ops: add a
dashboard filter on `guard_violations IS NOT NULL` and treat any `constraint_leak_group`
or `grounding` hit as a manual review queue. Do not flip `regenerate` until
`result_preview` parsing and channel naming bugs below are fixed and false-positive
rate is measured.

**Confidence:** High.

### [P1] — Grounding guard ignores production `result_preview` (JSON string); tool-backed venue names never whitelisted

**References:**
- `Travel Agent/backend/concierge/agent.py:925-932` (`result_preview: result_str[:2000]`
  — truncated JSON **string**)
- `Travel Agent/backend/concierge/output_guards.py:560-576` (`_walk_names` only recurses
  dict/list; strings are skipped)
- `Travel Agent/backend/concierge/output_guards.py:598-600` (feeds `result_preview` into
  `_walk_names` without `json.loads`)
- `Travel Agent/backend/concierge/replay_context.py:242-245` (documents production shape
  as string; replay path parses correctly — output guard does not)
- `Travel Agent/tests/concierge/test_output_guards.py:112-130` (test passes
  `result_preview` as a **list**, not a string — diverges from production)

**Why it matters to a real tester:** After `search_restaurants` returns real venues, the
agent can legally say "Cervejaria Ramiro" and still get a `grounding` violation in
telemetry. Operators cannot calibrate false-positive rate; flipping `regenerate` would
instruct the model to remove correctly grounded names. The guard is not a no-op (it
still flags phrases), but its **allowed set is wrong** for the dominant tool path.

**Repro / deterministic test idea:**
```python
tool_calls = [{
    "tool": "search_restaurants",
    "result_preview": json.dumps({"results": [{"name": "Belcanto"}]}),
}]
assert "belcanto" in _names_from_tool_calls(tool_calls)  # fails today
```
Add regression mirroring `replay_context._coerce_output` (parse string, then walk).

**Suggested fix direction:** In `_names_from_tool_calls`, if `result_preview` (or
`output`/`result`) is a `str`, `json.loads` (with regex UUID/name fallback on
truncated JSON per provenance module). Align `test_names_from_tool_calls_result_preview_key`
with production string shape.

**Confidence:** High.

### [P1] — `third_party_disclosure` guard is a no-op: production channel is `"personal"`, guard expects `"private"`

**References:**
- `Travel Agent/backend/core/models/conversations.py:31` (`conversation_type`: `"group"`
  or `"personal"`)
- `Travel Agent/backend/concierge/session.py:472`, `1166` (`channel=self.conversation.conversation_type`)
- `Travel Agent/backend/concierge/output_guards.py:461` (`_PRIVATE_CHANNELS =
  frozenset({"private"})`)
- `Travel Agent/backend/concierge/output_guards.py:687-688` (early return when channel
  not in `_PRIVATE_CHANNELS`)
- `Travel Agent/tests/concierge/test_output_guards.py:772-831` (tests use `channel="private"` only)

**Why it matters to a real tester:** IDENTITY_CORE rule (c) forbids framing another
member's hesitation as about money/budget in private check-ins ("his hesitation was
about the budget"). That shape can reach the user with **zero** runtime flag because
every private concierge thread uses `conversation_type="personal"`. This is the
secondary catastrophic mode (private constraint echo) with no automated backstop in
week 1.

**Repro / deterministic test idea:**
```python
reply = "His hesitation was about the budget when price came up."
assert _check_third_party_disclosure(reply=reply, channel="personal")  # expect violation
# today returns []
```

**Suggested fix direction:** Normalize channel at the `guard_reply` boundary:
`channel in ("personal", "private")` → private checks; `"group"` → group checks. Add
integration test calling `guard_reply(..., channel="personal")`.

**Confidence:** High.

### [P1] — `guard_reply` omits itinerary and traveler allow-lists; itinerary mentions false-flagged

**References:**
- `Travel Agent/backend/concierge/output_guards.py:1055-1103` (`itinerary_venue_names`,
  `traveler_names`, `extra_allowed` documented)
- `Travel Agent/backend/concierge/session.py:468-474`, `1162-1168` (calls omit all three)
- `Travel Agent/backend/concierge/output_guards.py:1096-1100` (itinerary names only help
  when caller supplies them)

**Why it matters to a real tester:** "Let's keep dinner at Taberna da Rua Bica" when
Taberna is already on the itinerary but the agent didn't call `itinerary_read` this turn
can surface a spurious `grounding` hit — noise during calibration. Worse: combined with
the `result_preview` bug, the allowed set is user message + false-positive lexicon only,
so legitimate tool+itinerary grounding is systematically under-represented.

**Repro / deterministic test idea:** Seed itinerary with venue V; turn with no tools;
reply mentions V; call `guard_reply` as session does today → grounding violation. Repeat
with `itinerary_venue_names={v.lower()}` → clean.

**Suggested fix direction:** Thread names from `load_turn_state` / trip context into
`guard_reply` on both session paths (mirror eval harness if one exists).

**Confidence:** High.

### [P1] — Hit-max-iterations can commit tool side effects without a coherent user reply

**References:**
- `Travel Agent/backend/concierge/agent.py:501-524` (`CONCIERGE_HIT_MAX_ITERATIONS`
  telemetry; documents side effects 1..N already committed)
- `Travel Agent/backend/core/agent_loop.py:724-730` (`hit_max_iterations=True`, partial
  text may remain)
- `Travel Agent/backend/concierge/agent.py:487-491`, `1114-1128` (fallback: "I got
  tangled up…" / synthetic assistant stub for API alternation)

**Why it matters to a real tester:** Agent runs `pin_experience` + `propose_change` in
iterations 8–10, exhausts budget, user sees a vague apology while the itinerary changed.
Map/Plan may update; chat says "give me one more nudge." Hard to debug without
`concierge_turns` + `reasoning_spans`.

**Repro / deterministic test idea:** Mock loop returning `hit_max_iterations=True`
with `tool_calls_made` containing `pin_experience`; assert turn record shows tools +
`error_state` unset while reply is fallback string.

**Suggested fix direction:** On `hit_max_iterations`, set `error_state="budget_exhausted"`,
include tool summary in telemetry, consider suppressing further mutating tools in the
last iteration via re-anchor prompt (already partially present in loop).

**Confidence:** Medium.

### [P2] — Provenance gate allows first side-effect before any tool surfaces UUIDs

**References:**
- `Travel Agent/backend/concierge/_provenance.py:132-144` (empty scope → `is_surfaced`
  returns `True`)
- `Travel Agent/backend/concierge/tool_handlers/itinerary.py:366-388` (`pin_experience`
  checks `is_surfaced`)
- `Travel Agent/backend/concierge/agent.py:652-663` (`provenance_scope` per turn)

**Why it matters to a real tester:** If the model's first action is `pin_experience` with
a UUID from conversation history (not this turn's search), the stale-UUID guard does not
fire. DB may still accept a real row — user sees pin without a fresh search in-thread.

**Repro / deterministic test idea:** Turn with empty tool history; call `pin_experience`
with UUID from prior turn fixture; expect structured `stale_provenance` — today succeeds
when scope empty.

**Suggested fix direction:** Tighten empty-scope policy for mutating tools (require at
least one search tool in turn, or allowlist admin_directive source_type).

**Confidence:** Medium.

### [P2] — Streaming path evaluates guards after text is delivered (voice/SSE)

**References:**
- `Travel Agent/backend/concierge/session.py:1149-1177` (explicit comment: text already
  shipped)
- `Travel Agent/backend/concierge/session.py:1213-1214` (violations only in message
  metadata)

**Why it matters to a real tester:** Voice and SSE users can hear/read uuid leaks,
markdown bullets, or confabulated names even when `guard_violations` is non-empty.
Week-1 posture is acceptable if documented; `regenerate` cannot fix streaming without
architectural change (guard before final delta or mid-stream compose-only).

**Repro / deterministic test idea:** Stream a reply with embedded UUID; assert client
received full text before `guard_violations` persisted.

**Suggested fix direction:** Defer streaming `regenerate`; for P0 shapes (uuid_leak),
consider cheap inline strip before last delta in voice mode only.

**Confidence:** High.

### [P2] — Grounding guard only catches multi-word Title-Case phrases

**References:**
- `Travel Agent/backend/concierge/output_guards.py:1041-1043` (single-word phrases
  skipped as too noisy)
- `Travel Agent/docs/working/Known Gaps Register.md:564-588` (O-10: training-data names
  like "Output" — closed/low, prompt-tightened)

**Why it matters to a real tester:** Lowercase or single-token venue confabulation
(e.g. "output" nightclub, "joes" without Title Case) ships unflagged. Prompt +
`SKILL_KNOWLEDGE` are the primary defense in week 1.

**Repro / deterministic test idea:** Reply "output is great tonight" after empty search;
assert `guard_reply` returns no `grounding` violation.

**Suggested fix direction:** Post-launch: extend extractor or tie to tool-empty +
venue-like token heuristic; keep week 1 prompt-first per O-10.

**Confidence:** Medium.

### [P2] — Vision/citation helpers bypass `call_llm()` wrapper

**References:**
- `Travel Agent/backend/concierge/vision_summary.py:96-100` (`client.messages.create`
  with `get_model(ModelRole.VISION_HISTORY_SUMMARY)`)
- `Travel Agent/backend/concierge/citation_extraction.py:147` (same pattern)
- `Travel Agent/CLAUDE.md` (discipline: concierge LLM via `backend/core/llm.py`)

**Why it matters to a real tester:** Not on the hot chat path; if image upload or
citation flows run during dogfood, retries/telemetry differ from main concierge loop.
Low user-visible risk.

**Repro / deterministic test idea:** Grep `backend/concierge/` for `messages.create` —
expect only vision/citation modules.

**Suggested fix direction:** Route through `call_llm` when vision message shape is
supported; until then document as accepted exception.

**Confidence:** High.

### [TECH-DEBT] — `result_preview` truncated at 2000 chars may cut mid-JSON

**References:**
- `Travel Agent/backend/concierge/agent.py:931` (`result_str[:2000]`)
- `Travel Agent/backend/concierge/replay_context.py:98`, `228` (`truncated: bool` in
  replay; guard has no equivalent)

**Why it matters to a real tester:** Large search payloads may lose trailing venue names
from the allowed set even after JSON-parse fix — edge case for big result sets.

**Suggested fix direction:** Extract name list in `_on_tool_result` before truncation;
store `surfaced_names: [...]` on tool_calls_made entry.

**Confidence:** Medium.

### [TECH-DEBT] — Conditional tool surface still ships ~31 tools in planning phase

**References:**
- `Travel Agent/backend/concierge/_tools_select.py:8-14`, `216-224` (41 → ~24–31 per
  turn; trip-admin always loaded)
- `Travel Agent/backend/concierge/_tools_select.py:134-147` (`_TRIP_ADMIN_TOOLS`
  always on — MVP conservative)

**Why it matters to a real tester:** Tool-selection errors under load are possible;
not a crash. Inclusive gating reduces miss risk.

**Suggested fix direction:** Tighten trip-admin gating when organizer signal exists;
monitor `tool_calls_made` distribution in dogfood.

**Confidence:** Low.

### [TECH-DEBT] — Output-guard tests diverge from production tool_calls shape

**References:**
- `Travel Agent/tests/concierge/test_output_guards.py:112-130` (list `result_preview`)
- `Travel Agent/backend/concierge/agent.py:925-932` (string `result_preview`)

**Why it matters to a real tester:** CI green does not prove production grounding
whitelist works.

**Suggested fix direction:** Single factory fixture for `tool_calls_made` rows used in
unit + integration tests.

**Confidence:** High.

---

## Positive signals (no finding)

| Area | Assessment |
|---|---|
| **Guard invocation** | `guard_reply` runs on non-streaming and streaming paths when `result.reply` is non-empty and not `composition_skipped`; failures swallowed with `OUTPUT_GUARD_FAILED` event. |
| **Group constraint patterns** | `constraint_leak_group` regex suite fires when `channel=="group"` (matches production). |
| **Tool crash isolation** | `parallel_tools._execute_one` catches exceptions and timeouts; returns JSON error envelope. |
| **Tool error recovery** | `LoopConfig.tool_error_feedback` + `RetryBudget` (3 attempts); classified wrap in `_collect_tool_results`. |
| **Loop bounds** | `max_iterations`, optional wallclock/token caps; no unbounded loop. |
| **Strict compose (trip-scoped)** | Recovery ladder + streaming suppression of pre-compose text; compose result forwarded via `text_delta`. |
| **Core skills** | `IDENTITY_CORE` always includes privacy/confabulation rules; `SKILL_COORDINATION` gated to `conversation_type=="group"`. |
| **Whereabouts validation** | Requires `include_group` or `include_nearby`; radius clamped; raw coords omitted from group payload. |
| **Booking flow** | Structured errors, proposal TTL, block matching window; uses `call_llm` path only indirectly via agent. |
| **Provenance tracking** | `track_uuids_from_json` on every tool return; pin/propose check `is_surfaced` when scope non-empty. |
| **LLM discipline (main path)** | `handle_turn` → `run_agent_loop` → `call_api_with_retry` / `call_llm`; model from registry. |

---

## Known / Accepted

- **Week-1 `log` mode** — Confirmed intentional per `CLAUDE.md` and `output_guards.py`
  module docstring. Violations are for calibration, not user protection, until
  `regenerate` rollout criteria are met.
- **Pre-trip group `strict_group_compose` bypass** — Documented P0 in Area 01
  (`agent.py:873`, `has_trip` gate). Out of scope to re-file; dogfood testers in
  conversation-scoped invite rooms should assume **no** compose stripping.
- **O-10 (training-data venue names)** — Known Gaps Register: prompt-tightened in
  `SKILL_KNOWLEDGE`; grounding guard may still miss single-word/lowercase names.
  Accept for week 1.
- **O-11 (private constraint echo)** — Product ambiguity on whether literal constraint
  phrases are allowed when user asks about self in 1:1; runtime `third_party_disclosure`
  should fire once channel naming is fixed.
- **G-9 (disruption → search vs generate_plan)** — Skill/tool routing gap in Known Gaps;
  not a crash; agent may pick suboptimal tool under replan stress.
- **Privacy guard scope** — Module docstring notes Phase 2c; runtime has
  `constraint_leak_group` + `third_party_disclosure` (latter broken on channel name).
  Full cross-channel privacy needs composer + eval alignment, not guard alone.
- **Vision/citation direct API** — Accepted auxiliary paths; not blocking dogfood chat.
