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

### Phase 0 · Build against the offline harness *(no provider spend)*

**Constraint, 2026-07-28: there is no budget for voice-provider testing
yet.** That does not block the engineering — it blocks *verification*.
The plan is therefore split by cost, not by phase order alone.

`tests/voice/` already exists with eight files (`test_agent`,
`test_deferred_tool`, `test_quota`, `test_resume_directive`,
`test_voice_metrics`, `test_voice_persona_fillers`, `test_worker`,
`test_voice_memory`). Providers are mocked. **This is the harness — build
everything below against it and leave it green.**

Two rules while unfunded:

1. **Everything ships behind the existing gate.** `VOICE_ENABLED` stays
   false; nothing here changes what users experience.
2. **Do the cost-*reducing* work first** — see 1c. Fixing speculative
   spend before the first paid session makes that session cheaper.

**Add the first-audio-out checkpoint now** (`metrics.py`), even though it
cannot be read yet. Everything today measures to text hand-off, not to
sound in the ear. Landing it unfunded means the first funded session
produces a real baseline instead of a second setup task.

**Deferred to the funded session (see the end of this doc):** the actual
p50/p95 baseline, turn-taking feel, persona voice listening checks, and
end-to-end interruption QA. None of it is knowable from code.

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

## The podcast question — format, artifact, interruption, adaptation

Researched 2026-07-28 alongside the above. Short version: **we should
borrow podcast *structure*, not podcast *format*, and the artifact we
need is mostly already specified.**

### Where the format is

**NotebookLM Audio Overviews** is the reference. Its **Interactive Mode**
is the relevant part: you listen, tap *Join*, the hosts call on you, you
ask, they answer from your sources, **then resume the original overview**.
Constraints worth noting even Google has: interactive mode works only on
newly-made Deep Dive overviews, and it is English-only.

Its most useful published lesson is a *design* one: **interrupt at thought
boundaries, not mid-sentence.** The natural intervention point is when one
speaker finishes a thought — cutting in mid-utterance produces awkward
transitions. That argues for segment-granular bookmarks, not
timestamp-granular ones.

**Multi-speaker synthesis** is solved: ElevenLabs v3 (GA early 2026) leads
expressive multi-speaker narration, with the standard workflow being a
`Host A:` / `Host B:` script and two voices contrasting on at least two
axes. **Cartesia** remains the low-latency specialist (sub-100 ms TTFA
over WebSocket) and exposes **`context_id`**, which maintains voice
context across sends so turn-by-turn dialogue sounds like one continuous
speaker.

The commonly-recommended split — **ElevenLabs for long-form narration,
Cartesia for the realtime agent** — is the split we already run.

### Recommendation: one voice, podcast structure

**Do not build two-host banter.** Three reasons, in order:

1. **It contradicts Voice Canon.** Our whole position is *one* voice with
   taste. Two synthetic hosts chatting is a different product wearing a
   very recognisable borrowed aesthetic.
2. **Persona honesty (trait 6).** Vesper doesn't pretend to be human. Two
   hosts performing rapport is precisely that pretence.
3. **The format is already a cliché.** "AI podcast with two hosts" is
   instantly identifiable, and being identifiable as generic AI output is
   the thing we differentiate against.

What we should borrow: **sectioning, pacing, and the join-then-resume
interaction.** The differentiator is that it is *your trip*, not that
there are two voices discussing it.

> Possible later variant, not v1: the Reading's final section is spec'd to
> *argue the trip's open decision*. A two-voice treatment of a genuine
> for/against is a real use of dialogue rather than cargo-culting one.

### The artifact already exists — in two halves that have never met

**Half one — the script.** The companion Reading in
`trips-home-promotion-model-2026-07-27.md` is already podcast-shaped:
sectioned, `Listen N min / read N min`, section titles that carry the
personalisation, a thread line, a refresh clock (recompose on itinerary
commit and at T-7), and a pre-registered quality gate (the swap test).
**Sections are the natural interrupt boundaries** the NotebookLM lesson
asks for.

**Half two — the delivery layer.** `narration.py` is more built than
expected: per-stop audio (`/audio/{entity_type}/{entity_id}`), a
**pre-render manifest** for downloading every cached narration over WiFi
pre-departure and playing it **offline**, geofenced `NarrationStop`s, and
a **depth ladder** (`narration_count` → intro / detail / obscure).

But these are *per-place fragments*, not a long-form piece with a
through-line. The gap between them is the podcast artifact: **the Reading
rendered as a sectioned audio spine.**

### We already designed past NotebookLM

`interruptionController.ts` implements:

```
narrating → pausing (fade + capture bookmark) → in_voice
          → bridging (bridge sentence) → resume
```

with `BookmarkDecision.mode: 'bridge' | 'renarrate' | 'skip'`.

That third field is the **adapt-on-demand** primitive. NotebookLM, per its
own docs, resumes the original overview. Ours can decide to *re-narrate*
the segment because the answer changed its context, or *skip* it because
the question revealed the listener doesn't need it. **That is a better
design than the reference implementation, and it is not wired to
anything.**

### The architecture to build toward

**Pre-rendered spine + live interruption + adaptive resume.**

- **The spine is pre-rendered per section** (ElevenLabs, long-form,
  expressive). Cheap, cacheable, offline-capable — reuses the manifest and
  lease machinery already built.
- **Interruptions are answered live** by the conversational agent
  (Cartesia, low-latency) — the phase-1 streaming work applies directly.
- **Resume is a decision, not a rewind** — `bridge` / `renarrate` / `skip`
  per the controller.

Fully-live generation is the wrong shape: it forfeits pre-render, offline,
and cost control on the modality we already quota.

### ⚠️ The seam this creates

**The voice changes at the moment of interruption.** If the spine is
ElevenLabs and the answer is Cartesia, the listener hears a different
speaker the instant they engage — at the single moment they are paying
most attention. This is the same class of failure as the unwired
`voice_id`, and it undermines the entire "one voice with taste" position.

Three options, decide deliberately:

1. **One provider for both** — simplest, costs long-form expressiveness or
   realtime latency depending which you pick.
2. **Matched voice across providers** — a designed/cloned voice registered
   with both, verified by listening, not by config.
3. **Mask it with the bridge** — the `bridgeText` sentence already exists
   between voice-answer and resume; if the bridge is rendered in the
   *spine's* voice, the handoff back is seamless even if the answer wasn't.
   Cheapest, and the machinery is already there.

Option 3 is likely the v1 answer, but **the switch into voice is still
audible** — only the return is covered.

### Sequencing for the podcast path

It sits **after** phase 1 (the answer path must be fast before it is worth
interrupting into) and **depends on the Reading composer**, which is Trips
phase 4 and gated on the swap test. Order:

1. Reading composer exists and passes the swap test *(Trips plan, phase 4)*
2. Render the Reading as a sectioned audio spine — reuse the manifest,
   lease, and offline machinery
3. Wire the interruption chain end-to-end *(phase 3 above)* — including
   the resume-directive call site
4. Then, and only then, `renarrate` / `skip` — the adaptive modes are
   worthless until the basic loop is trustworthy

**Do not build the podcast before the Reading passes the swap test.**
Audio multiplies whatever the writing is; narrating a generic city guide
in a beautiful voice produces a generic audio guide, which is worse than
shipping nothing.

## Sequencing under the no-budget constraint

**Almost all of this is buildable now.** What is blocked is verification,
not construction.

### Free — build now, against `tests/voice/`

| Item | Why it is free |
|---|---|
| **1c** preemptive-generation audit | pure code reading; **do this first — it may be burning tokens** |
| **1a** stream concierge → TTS | `send_message_streaming` is already exercised by the text path; the clause-buffer is a pure function with unit tests |
| **1d** filler branch | pure refactor |
| **2a** wire `voice_id` | one-line wiring + a test asserting the kwarg reaches the TTS constructor |
| **2b** greeting through the concierge | pure |
| **2c** heuristics | pure |
| **3a/3b** `deferred_tool` + resume call site | both already have test files and no live dependency |
| **3c** FE interruption chain → a screen | RN + jest; no provider |
| **3e** `storage.py` wire-or-delete | pure |

**1b** (Silero VAD + `inference.TurnDetector`) is a middle case: both are
**local models**, not paid APIs, and `livekit-local-inference` is already
pinned — so adding and configuring them costs nothing. Only judging
whether the turn-taking *feels* right needs a live session.

### Blocked on the first funded session

Latency baseline (p50/p95 per stage), turn-taking feel, persona voice
listening checks, end-to-end interruption QA, and the podcast
voice-continuity seam. **Script that session in advance** — a fixed
20–30-turn run across ack / simple / tool-calling, executed once, rather
than exploratory poking. Everything above should be landed and green
before it starts, so one paid hour answers every open question at once.

**Order:** 1c → 1a → 1b → 2a–2c → (Batch 3 as a product decision) →
funded session → re-tune from real numbers.

The one rule that survives the budget constraint: **nothing here gets
called "faster" until the funded session says so.** Build it, test it
offline, keep it gated, and let the measurement be the thing that closes
each item.
