---
doc_type: working
status: active
owner: founder / eng
created: 2026-07-28
expires: 2026-08-27
why_new: The voice subsystem was audited 2026-07-28 and found architecturally sound but integration-incomplete. No doc owns the gap between what is built and current SOTA voice-agent practice, or the order to close it in.
source_of_truth_for:
  - voice-agent-sota-gap
  - voice-agent-latency-plan
depends_on:
  - travel-agent/backend/voice/FEATURE.md
  - travel-agent/docs/product/Voice Canon.md
---

# Voice agent — closing the SOTA gap

Audit findings and plan, 2026-07-28. **The architecture is right; the
integration is unfinished and the turn-taking config is default.** This
is a finishing job, not a rebuild.

## Where SOTA is (July 2026, light survey)

**Latency targets.** Time-to-first-audio under **500 ms** is the
threshold for conversational feel. Production targets: **p50 < 250 ms**
optimized, **p50 < 400 ms** standard cloud stack, **p95 < 800 ms**
either way.

**The budget that adds up to it:**

| Stage | Budget |
|---|---|
| streaming STT | 60–100 ms |
| LLM **first token** | 100–180 ms |
| TTS **first chunk** | 40–80 ms |
| WebRTC transport | 20–40 ms |

The load-bearing word is *first*. Every stage streams; nothing waits for
a complete result. Cartesia Sonic 3.5 Turbo reports ~40 ms TTFB — **we
already use Cartesia**, so that budget line is free once we stop
blocking on it.

**Turn detection is a two-signal model now.** Acoustic VAD (Silero) for
speech presence and interruption, plus a **semantic end-of-utterance
model** that reads content to decide whether the speaker is actually
done. LiveKit's separate `livekit-plugins-turn-detector` is deprecated in
favour of `livekit.agents.inference.TurnDetector`, a unified audio EOU
detector that ships inside `livekit-agents`. Turn-taking quality — not
raw speed — is the most common complaint about bad voice agents.

**Interruption handling has real knobs:** adaptive interruption mode,
`min_duration` / `min_words` to filter coughs and line noise, and
`false_interruption_timeout` for when VAD fires but no transcript
materialises.

**Preemptive generation** speculatively starts the LLM before end-of-turn
is confirmed, and is **on by default**. Only the LLM runs preemptively;
TTS waits for confirmation. It costs extra tokens, and the trade worsens
for long utterances where the speculation gets discarded.

## Where we are

We are on **`livekit-agents==1.6.6`** — the current line. The framework
is not the problem.

```python
# worker.py — today
session = AgentSession(
    stt=deepgram.STT(api_key=...),
    tts=cartesia.TTS(api_key=...),
)
```

No `vad=`. No `turn_detection=`. Neither `livekit-plugins-silero` nor a
turn detector is in `requirements.txt`. We are running a current
framework on its weakest default turn-taking path.

And the LLM stage does not stream:

```python
result = await self._concierge.send_message(...)   # blocks to completion
...
yield result.reply                                  # entire reply at once
```

`send_message_streaming` exists at `session.py:1290`, already accepts
`modality: Literal["text","voice"]`, and is used by the **text** route
(`_message_flow.py:631`). The path where latency is cosmetic streams; the
path where latency *is* the experience does not.

**This is why the filler machinery exists.** `agent.py`'s speculative
pre-filler is compensating for a blocking call that has a streaming
sibling.

## The plan

### Phase 0 · Make it measurable *(prerequisite — nothing else is honest without it)*

Voice is gated off (`VOICE_ENABLED=false`, LiveKit/Deepgram/Cartesia
secrets unset). **No baseline exists**, so every claim below is currently
theoretical.

- Stand up a dev-only voice environment with the three provider keys.
- Run 20–30 turns across the mix we care about: acknowledgment, simple
  question, tool-calling question.
- `VoiceTurnTimer` already writes four checkpoints (`stt_final` →
  `filler_yield` → `concierge_done` → `reply_yield`) to
  `voice_turn_metrics`. **Pull p50/p95 per checkpoint.** That is the
  baseline.
- **Add one missing checkpoint: first audio out.** Everything today
  measures up to text hand-off, not to sound in the ear — which is the
  number that actually matters.

Exit: a table of p50/p95 per stage. Expect the concierge stage to
dominate; if it doesn't, re-prioritise the phases below.

### Phase 1 · The latency spine *(the big win)*

**1a · Stream the concierge into TTS.** Switch `llm_node` to
`send_message_streaming` and yield as deltas arrive.

- Buffer to **sentence or clause boundaries** before yielding, not raw
  tokens — TTS prosody degrades badly on fragments. Punctuation-based
  flush with a max-chars fallback is the standard shape.
- Preserve the existing idempotency key and `VoiceTurnTimer` marks; add
  a `first_delta` mark.
- Expected effect: TTFA stops being *(full LLM completion + TTS start)*
  and becomes *(first clause + ~40 ms)*. **This is the single largest
  improvement available.**

**1b · Add the two-signal turn detector.** Add `livekit-plugins-silero`,
configure `AgentSession(vad=silero.VAD.load(), turn_detection=...)` using
`livekit.agents.inference.TurnDetector`. This is the fix for
turn-taking feel, which the survey says users complain about more than
speed.

**1c · Audit preemptive generation against our side-effecting
`llm_node`.** ⚠️ **Verify before assuming either way.** Our `llm_node`
is not a pure LLM call — it persists a message, records modality state,
writes metrics, and emits telemetry. If preemptive generation invokes it
speculatively and the turn is then not confirmed, we may be persisting
messages for utterances the user never finished, and double-counting
telemetry. The idempotency key may absorb the message duplication; it
will not absorb `record_modality` or the metrics row.

Decide explicitly: either make `llm_node` side-effect-free until the turn
is confirmed, or disable preemptive generation. **Also price it** — it
increases token usage on the modality we already quota for cost.

**1d · Re-evaluate the fillers.** Once 1a lands, the speculative filler
is probably unnecessary for normal turns (sub-500 ms needs no
scaffolding) and still valuable for tool calls (2–5 s). This is also the
moment to fix the dead heuristic: `_filler_reason` currently returns
`"tool_call"` vs `"speculative"` but **both paths yield the same filler**,
so ~25 lines of keyword matching change only a telemetry label. Give tool
calls a distinct treatment or delete the branch.

### Phase 2 · The persona seam *(small, visible)*

**2a · Wire `voice_id` into TTS.** `worker.py:146` computes
`tts_voice_id`, logs that an operator must wire it, and constructs
`cartesia.TTS()` without it. Today every persona speaks in the plugin
default voice while saying persona-flavoured filler text — the exact seam
`_persona_fillers`'s own comment says it exists to prevent. Verify the
kwarg name against the installed `livekit-plugins-cartesia==1.6.6`.

**2b · Route the greeting through the concierge.**
`session.say("Hey! How can I help with your trip?")` is hardcoded,
English, persona-less, and **ungoverned by Voice Canon** — the first
sentence a user ever hears is the one that bypasses the voice.

**2c · Fix or drop the English-only heuristics.** `_ACK_ONLY_PHRASES` and
`_TOOL_TRIGGER_WORDS` are English while personas are Portuguese- and
Japanese-flavoured. A user answering Mateus with "sim" fails the ack
check and gets a filler stacked on a 300 ms reply — the precise jerkiness
the list was written to prevent. If 1d deletes the speculative branch,
much of this dissolves.

### Phase 3 · Interruption — the differentiated part *(the real bet)*

~1,400 lines are built, tested, and **unreachable**:
`deferred_tool.py` (303), `resume_directive.py` (67), and the FE chain
`interruptionController.ts` (471) + `narrationPlayback` (204) +
`liveNarrationPlaybackAdapter` (243) + `liveKitConnection` (148) +
`useNarrationWithInterruption`. `storage.py` (258, `derive_cache_key`)
has zero importers.

- **3a · Wire `deferred_tool`** into the agent's tool path — the 5 s
  budget and graceful deferral. Independent of everything else.
- **3b · Wire the `resume_narration` call site** in `worker.py` (the
  integration note is already written there, as a comment).
- **3c · Consume the FE interruption chain from a real screen.** Today
  it is wired only to itself.
- **3d · Configure adaptive interruption** — mode, `min_duration`,
  `min_words`, `false_interruption_timeout`.

**Interrupt a narration by voice, ask something, say "go on," resume at
the bookmark** is the one capability here a general assistant cannot
copy, because it needs both the narration content and the conversational
agent. It is also the one thing on this list that is a *product* bet
rather than a fix — treat 3a–3d as a decision to make, not a queue to
grind.

### Explicitly not doing

**Speech-to-speech (gpt-realtime, Gemini Live).** It emits audio with no
text in the middle, so the word ban, the facts-scan wrapper, the
grounding check and the compose privacy gate cannot be applied. For a
product whose moat is a *governed* prose voice, that trades the
differentiator for latency. It would also replace the concierge — the
actual product — and break vendor portability.

The cascade is the right architecture. It is simply not currently
configured or streamed like one.

## Sequencing

Phase 0 → 1 is the critical path and worth doing as one push; 1a alone
likely moves p50 more than everything else combined. Phase 2 is a
half-day of visible polish that can ride along. Phase 3 is a separate
decision.

**Do not start any of it while voice is gated off and unmeasured** —
Phase 0 exists because "it feels faster" is not a result.
