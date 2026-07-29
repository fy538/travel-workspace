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

## Status (2026-07-28, end of session)

**Everything in the "Free — build now" list shipped except 3c, which
turned out not to belong on that list.** 8 commits, `travel-agent`,
`ae141dc6` → `d2dcead4`. mypy/ruff clean throughout; 197 tests green
(was 143 at session start). Two pre-commit hooks (broad-exception
ratchet, sync-DB-in-async) caught real issues along the way, both fixed
properly rather than bypassed.

| Item | Status | Commit |
|---|---|---|
| 1c preemptive-generation audit | ✅ shipped — disabled | `ae141dc6` |
| 2a wire `voice_id` | ✅ shipped | `ae141dc6` |
| 2b greeting through the concierge | ✅ shipped | `ae141dc6` |
| 1a stream concierge → TTS | ✅ shipped | `9473998c` |
| 1d filler branch | ✅ shipped — speculative case removed | `61155b44` |
| 2c English-only heuristics | ✅ shipped — reactive safety net, not a translated list | `791b01a0` |
| 3e `storage.py` | ✅ investigated — verified deliberate, left as-is | — (no code change) |
| 1b Silero VAD + turn detector | ✅ shipped — **not** `inference.TurnDetector`, see correction below | `5bb535ca` + `c2b5ea2e` |
| 3a wire `deferred_tool.py` | ✅ shipped — **found and fixed a real race**, see below | `95a58476` |
| 3b wire `resume_narration` directive | ✅ shipped | `d2dcead4` |
| 3c FE interruption chain → a screen | 🔶 **partially unblocked** — Feature A (concierge voice chat) wired; Feature B (narration interrupt) still not started, see below | `travel-app@e2818815` |
| 3d adaptive interruption config | ❌ not started | — |
| Funded-session items (baseline, turn-taking feel, listening QA) | ❌ blocked, unchanged | — |

**Later the same day**: investigating 3c found it was two features sharing
one name — Feature A (live concierge voice chat, `VoiceOverlay`/
`useVoiceSession`, already had a real screen and just needed the LiveKit
SDK installed and wired) and Feature B (narration interrupt-and-resume,
the actually-hard one, needs a net-new mic→VAD pipeline). `travel-app`
commit `e2818815` installs `@livekit/react-native` + `livekit-client` and
wires Feature A's connector, gated behind the existing `VOICE_ENABLED`
flag; verified via `tsc`, the full voice test suite, and a clean
`expo prebuild --no-install` on both platforms — not yet on a real
device. Feature B (the actual 3c/3d scope) is unchanged: still needs the
VAD pipeline and a `NarrationCard` decision. Full writeup in Phase 3
below.

Three corrections to this doc's own earlier claims, found by verifying
against installed packages and the actual codebase rather than the
research pass:

1. **1b was wrong about `inference.TurnDetector` being local.** It
   isn't — its constructor takes `api_key`/`api_secret`, a hosted
   LiveKit Cloud endpoint. Shipped with the deprecated standalone
   `livekit-plugins-turn-detector` package's `MultilingualModel`
   instead, which genuinely runs locally by default. See Phase 1 below
   for the full correction.
2. **3a's "5s budget and graceful deferral" undersold a real bug it
   was hiding.** `asyncio.create_task()` schedules but doesn't run the
   streaming call synchronously, so the naive implementation's first
   queue wait would commit to being unbounded before the tool-start
   signal could arrive — silently never deferring for the common case
   of a tool call as the model's first action. Reproduced as an actual
   hang, not a hypothetical; fixed by bounding every wait. Full account
   in the 95a58476 commit message.
3. **`storage.py` is not a "wire or delete" situation.** It's
   deliberately dormant, well-tested scaffolding for a future R2
   migration that hasn't been provisioned — its own module docstring
   already says so, and the live narration path correctly uses a
   different, index-keyed cache today. Wiring it in would have been
   architecturally wrong. See 3e below.

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

✅ **Shipped, `9473998c`.** `_ClauseBuffer` flushes at sentence ends
always, softer clause boundaries once substantial (≥40 chars, avoids a
premature flush on "Mr."), and a 200-char hard cap regardless. The
callback (push) and the generator's yield (pull) bridge through an
`asyncio.Queue`; `send_message_streaming` runs as a background task
while `llm_node` drains the queue. `first_delta_at` added to
`VoiceTurnTimer` as the new `ttft_ms` anchor (in-memory only — no new
DB column; nothing needs the raw timestamp yet, and a migration meant a
real head-collision risk with other sessions landing migrations the
same night). Flagged, not fixed: `send_message_streaming`'s output
guard runs log-only on the streaming path — a violation may already be
**spoken** before the guard catches it, materially worse than the text
path's silent-bubble-swap. Worth an explicit decision before this ships
live (e.g. evidence-required turns falling back to the blocking path).

**1b · Add the two-signal turn detector.**

✅ **Shipped, `5bb535ca` (deps) + `c2b5ea2e` (wiring).** ⚠️ **This
section's original claim was wrong — corrected during implementation,
not just noted.** `livekit.agents.inference.TurnDetector`'s constructor
takes `api_key`/`api_secret`/`base_url`: it's a hosted **LiveKit Cloud**
endpoint, not a local model, despite being described that way above and
in the sequencing table below. Verified against the installed package
before writing any code. Using it would have meant trading one paid
dependency for another, exactly what this whole unfunded phase exists
to avoid.

Shipped instead: `livekit-plugins-silero` (`VAD.load()` takes only
local tuning params, confirmed no credentials) plus the **deprecated**
standalone `livekit-plugins-turn-detector` package's `MultilingualModel`
— confirmed its constructor sets `load_languages=True` whenever no
remote inference URL is configured, so it runs locally by default.
Multilingual over English because Mateus and Keiko are
Portuguese/Japanese-flavoured. The deprecation is real (LiveKit wants
everyone on the paid path); tracked in `requirements.in` as a follow-up
once there's budget, or if the package is pulled from PyPI first.

**1c · Audit preemptive generation against our side-effecting
`llm_node`.**

✅ **Shipped, `ae141dc6` — disabled.** Confirmed via the installed
`livekit-agents==1.6.6` source, not assumed: preemptive generation
re-invokes `Agent.llm_node` — our override, not a separate LLM-only
path (`on_preemptive_generation` → `_generate_reply` →
`perform_llm_inference(node=self._agent.llm_node)`) — on unconfirmed
transcripts, up to `max_retries=3` per turn. Since `llm_node` persists a
message, records modality, and writes metrics/telemetry, a discarded
speculative attempt was paying for all of it on every voice turn, not
just occasionally. Disabled via
`turn_handling={"preemptive_generation": {"enabled": False}}` until
`llm_node`'s side effects can be deferred until the turn is confirmed.
This was landed **first**, before any other item, on the reasoning that
it might be actively costing money.

**1d · Re-evaluate the fillers.**

✅ **Shipped, `61155b44`.** Once 1a streams, the speculative case is a
net loss, not just unnecessary — the real reply's first clause arrives
about as fast as a filler's own TTS would, so firing one and cutting it
short reads as *more* jerky than starting the stream directly. Removed
the branch entirely; `_filler_reason` now returns `"tool_call"` or
`None`. This also deleted `_ACK_ONLY_PHRASES`/`_ACK_MAX_CHARS` as dead
code — their only job was choosing between "speculative" and `None`, a
distinction that no longer exists.

### Phase 2 · The persona seam *(small, visible)*

**2a · Wire `voice_id` into TTS.** `worker.py:146` computes
`tts_voice_id`, logs that an operator must wire it, and constructs
`cartesia.TTS()` without it. Today every persona speaks in the plugin
default voice while saying persona-flavoured filler text — the exact seam
`_persona_fillers`'s own comment says it exists to prevent. Verify the
kwarg name against the installed `livekit-plugins-cartesia==1.6.6`.

✅ **Shipped, `ae141dc6`.** Kwarg confirmed to be `voice` (not
`voice_id`/`voice_name`) — its default is itself a fixed voice-ID
string, not `None`, confirming the bug: every persona really was
speaking in that one plugin default. Wired conditionally, omitting the
kwarg entirely (not passing `None`) when a persona has no `voice_id`
yet, to preserve the plugin's own default for un-designed personas.

**2b · Route the greeting through the concierge.**
`session.say("Hey! How can I help with your trip?")` is hardcoded,
English, persona-less, and **ungoverned by Voice Canon** — the first
sentence a user ever hears is the one that bypasses the voice.

✅ **Shipped, `ae141dc6`.** Not routed through a live LLM call —
deliberately static, matching `verbal_preamble_phrases`/
`voice_deferral_phrase`'s existing pattern. A session opener has no
user utterance to ground a live composition on, and firing an LLM call
on every connect would add real cost to a modality already under
budget pressure. New `GuidePersona.voice_greeting` field, populated for
Mateus and Keiko; `persona_greeting()` resolves it with a neutral
fallback for un-enriched personas.

**2c · Fix or drop the English-only heuristics.** `_ACK_ONLY_PHRASES` and
`_TOOL_TRIGGER_WORDS` are English while personas are Portuguese- and
Japanese-flavoured. A user answering Mateus with "sim" fails the ack
check and gets a filler stacked on a 300 ms reply — the precise jerkiness
the list was written to prevent. If 1d deletes the speculative branch,
much of this dissolves.

✅ **Shipped, `791b01a0` — reactive safety net, not a translated
list.** `_ACK_ONLY_PHRASES` dissolved entirely per the 1d prediction
above. `_TOOL_TRIGGER_WORDS`/`_PHRASES` survive (they still gate the
pre-emptive, instant filler) but a translated word list would have
been perpetually incomplete — new languages, code-switching, informal
phrasing. Instead wired `on_tool_complete`'s sibling, `on_tool_start`,
as a reactive fallback: it fires off the model's actual `tool_use`
content block, not a transcript guess, so it's language-agnostic by
construction. If the pre-emptive guess missed, a filler still fires the
moment a real tool call starts — late beats silent for the rest of a
2–5 s execution. Guarded against double-firing across multiple tool
calls in one turn; `voice_turn_metrics.filler_reason` gains a new
`"tool_start_reactive"` value so dashboards can see how often the
prediction actually misses.

### Phase 3 · Interruption — the differentiated part *(the real bet)*

~1,400 lines are built, tested, and **unreachable**:
`deferred_tool.py` (303), `resume_directive.py` (67), and the FE chain
`interruptionController.ts` (471) + `narrationPlayback` (204) +
`liveNarrationPlaybackAdapter` (243) + `liveKitConnection` (148) +
`useNarrationWithInterruption`. `storage.py` (258, `derive_cache_key`)
has zero importers.

- **3a · Wire `deferred_tool`** into the agent's tool path — the 5 s
  budget and graceful deferral. Independent of everything else.

  ✅ **Shipped, `95a58476`.** Found and fixed a real bug on the way in:
  the original consumer loop's first `await chunk_queue.get()` was
  unbounded, issued while `tool_started_at` was still `None` — because
  `asyncio.create_task()` schedules the producer but doesn't run it
  synchronously, the consumer could commit to waiting forever before the
  producer had a chance to set the deadline flag. Reproduced as an
  actual hung `pytest` process (killed via `ps aux | grep pytest` +
  `kill -9`), not a mock artifact. Fixed with a bounded 0.5 s poll
  (`_POLL_INTERVAL_S`) before the deadline is known, then a real budget
  countdown once `tool_started_at` is set. On timeout, the deferred path
  calls `post_deferred_result` / `deferral_phrase_for_persona` and, when
  the background task later completes, posts the result back into chat
  via `asyncio.to_thread(create_message, ...)` (sync DB call kept off
  the event loop, per the repo's async-sync-db hook).

- **3b · Wire the `resume_narration` call site** in `worker.py` (the
  integration note is already written there, as a comment).

  ✅ **Shipped, `d2dcead4`.** `llm_node`'s new `_on_tool_complete`
  callback parses the tool result's envelope (`ToolResultEnvelope` /
  `wrap_envelope()`), and when the structured payload carries a
  `resume_narration` directive, calls `publish_resume_directive(room,
  directive)`. `TravelVoiceAgent.__init__` gained a `room:
  _Room | None = None` param (TYPE_CHECKING-guarded import of the
  `_Room` protocol from `resume_directive.py`, so no runtime import is
  needed) and `worker.py` now passes `room=ctx.room` at construction.
  The stale "Phase 6b.10" comment block in `worker.py` that used to
  describe this as a remaining integration step has been deleted.

- **3c · Consume the FE interruption chain from a real screen.** Today
  it is wired only to itself.

  ❌ **Investigated, not started — this is not wire-up work.** Two of
  the hook's three injectable dependencies do have real implementations
  now (`LiveNarrationPlaybackAdapter` in
  `utils/voice/liveNarrationPlaybackAdapter.ts`, and
  `liveAudioSessionProvider.ts`) — but two things are still missing, and
  neither is small:

  1. **No live microphone → VAD pipeline.** `feedVadFrame` (the entry
     point `useNarrationWithInterruption` needs to detect a voice
     interruption) has zero real callers anywhere in the app — grepped
     for it across `travel-app`; only the hook and
     `interruptionController.ts` mention it. There is no existing
     capture pipeline to hook up; one would have to be built from
     scratch.
  2. **No real `voiceSessionOpener`.** The third injectable dependency
     (`interruptionController.ts`'s `VoiceSessionOpener` type — distinct
     from, and never wired to, `useVoiceSession`'s `configureVoiceRoomConnector`
     below) has no implementation outside the hook's own no-op default
     stub.

  The realistic integration target is `components/chat/NarrationCard.tsx`
  (550 lines, the actual current narration entry point, built on the
  much simpler `useNarrationAudio` play/pause/progress hook) — but
  swapping it onto `useNarrationWithInterruption` is a full
  interaction-model rewrite of that screen, not a call to an unused
  hook. Left as a scoping decision for the user, not picked up.

  **Follow-up (2026-07-28, later same day): `travel-app@e2818815` makes
  the second gap smaller, but doesn't close it.** Investigating this
  item surfaced that "3c" was actually two separate features wearing one
  name:

  - **Feature A — live concierge voice chat** (`VoiceOverlay` /
    `useVoiceSession`, already mounted in `concierge/chat.tsx`, real
    token endpoint, real state machine). No client-side VAD needed —
    it's an open-mic conversation; turn-taking is server-side (1b's
    `MultilingualModel`). It was stalled at `ready_to_connect` purely
    because no one had ever installed `@livekit/react-native` or called
    `configureVoiceRoomConnector()`.
  - **Feature B — narration interrupt-and-resume** (this item, 3c as
    originally scoped). Needs Feature A's LiveKit transport *plus* the
    client-side VAD pipeline *plus* a `NarrationCard` interaction
    rewrite — genuinely harder, and still fully unstarted.

  `e2818815` installed `@livekit/react-native` + `livekit-client` +
  `@livekit/react-native-expo-plugin` + `@livekit/react-native-webrtc`,
  and wired Feature A's connector
  (`utils/voice/registerVoiceRoomConnector.ts`, called once at app
  startup from `app/_layout.tsx`, gated behind the existing
  `VOICE_ENABLED` flag so the native module and its `registerGlobals()`
  WebRTC globals are never touched when voice is off — consistent with
  `app.config.js`'s existing "voice is off in production" throw). Found
  and fixed a real correctness gap on the way in: `liveKitConnection.ts`
  never called `AudioSession.start/stopAudioSession()`, which configures
  the platform's play+record audio category — without it a connection
  can succeed while the mic silently never captures.

  Deliberately did **not** install `react-native-audio-api` or
  `onnxruntime-react-native` + the Silero ONNX model — both are
  Feature-B-only (`LiveAudioSessionProvider`'s own docstring says so
  explicitly: "for the narration interrupt flow") and have zero
  consumers today. No reason to pull in a model asset for nothing.

  Verified: `tsc --noEmit` clean, all 252 voice tests pass, `expo
  prebuild --no-install` succeeds on both iOS and Android with the
  plugin present. **Not** verified: `pod install` / Gradle sync, an
  actual `expo run:ios`/`expo run:android`, or a real `room.connect()` —
  the last of those starts the metered LiveKit/Deepgram/Anthropic/
  Cartesia spend this whole doc has been avoiding. That's the next step
  whenever there's budget for it, and it's now a much smaller step than
  "get any of this working" was this morning: install deps → wire
  connector → device build → connect.

  `voiceSessionOpener` (Feature B's own connector seam) is still a
  no-op — `e2818815` didn't touch it. But it's now a much shorter piece
  of work than before: it can call the same
  `connectToLiveKitRoom`/`AudioSession` plumbing Feature A now uses,
  just pointed at `interruptionController` instead of `useVoiceSession`.
  The VAD pipeline (point 1 above) is still fully unbuilt and is the
  larger remaining piece of 3c.

- **3d · Configure adaptive interruption** — mode, `min_duration`,
  `min_words`, `false_interruption_timeout`.

  ❌ Not started; not investigated this session.

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

## Sequencing under the no-budget constraint — completion record

**Everything free landed.** Actual order was 1c → 1a → 1d → 2a → 2b →
2c → 3e → 1b → 3a → 3b, each as its own commit in `travel-agent`, then
3c was investigated and correctly stopped short of implementation. See
the [Status](#status-2026-07-28-end-of-session) section at the top for
the commit hashes and the corrections found along the way — in
particular, **1b's original framing below was wrong**: it shipped, but
not as `inference.TurnDetector`.

### Free — build now, against `tests/voice/` *(original framing, kept for record)*

| Item | Why it is free | Outcome |
|---|---|---|
| **1c** preemptive-generation audit | pure code reading; **do this first — it may be burning tokens** | ✅ shipped — disabled |
| **1a** stream concierge → TTS | `send_message_streaming` is already exercised by the text path; the clause-buffer is a pure function with unit tests | ✅ shipped |
| **1d** filler branch | pure refactor | ✅ shipped |
| **2a** wire `voice_id` | one-line wiring + a test asserting the kwarg reaches the TTS constructor | ✅ shipped |
| **2b** greeting through the concierge | pure | ✅ shipped |
| **2c** heuristics | pure | ✅ shipped — became a reactive safety net, not a translated list |
| **3a/3b** `deferred_tool` + resume call site | both already have test files and no live dependency | ✅ shipped (3a found a real race; see Phase 3 above) |
| **3c** FE interruption chain → a screen | RN + jest; no provider | 🔶 **half of it was free after all** — see below |
| **3e** `storage.py` wire-or-delete | pure | ✅ investigated — deliberate, left as-is, no code change |

**1b** (Silero VAD + turn detection) was originally framed as "both are
local models, including `inference.TurnDetector`." That was wrong:
`inference.TurnDetector` requires `api_key`/`api_secret`/`base_url` —
paid LiveKit Cloud inference. Shipped instead with the deprecated
standalone `livekit-plugins-turn-detector` package's `MultilingualModel`,
which is genuinely local by default (loads local language files when no
remote inference URL is configured). Chosen over `EnglishModel` because
the personas are Portuguese/Japanese-flavored. Silero VAD was correct as
originally framed — genuinely local, no credentials.

**3c turned out to be two features, and only one of them was free.**
Investigating it found "the FE interruption chain" actually names two
things: Feature A (live concierge voice chat, already had a real screen
and a working state machine, just needed the LiveKit SDK installed and
its connector wired — genuinely free, RN + jest, no provider) and
Feature B (narration interrupt-and-resume, which needs a net-new
mic→VAD capture pipeline and a real `voiceSessionOpener` — not free,
infrastructure that doesn't exist yet). `travel-app@e2818815` shipped
Feature A: `@livekit/react-native` + `livekit-client` installed,
`configureVoiceRoomConnector` wired behind `VOICE_ENABLED`, and a real
gap fixed along the way (`liveKitConnection.ts` never started/stopped
the platform `AudioSession`, which could have meant a connection
succeeding while the mic silently never captured). Verified via `tsc`,
the full voice test suite, and clean `expo prebuild --no-install` on
both platforms. Feature B is unchanged — still needs the VAD pipeline
and the `NarrationCard` product decision below.

### Free — turned out to be, once split: Feature A

| Item | Why it turned out free | Outcome |
|---|---|---|
| Install `@livekit/react-native` + `livekit-client` | npm installs, `expo prebuild` is local/no-cost | ✅ shipped |
| Wire `configureVoiceRoomConnector` at app startup | the seam already existed in `useVoiceSession.ts`, unconnected | ✅ shipped, gated behind `VOICE_ENABLED` |
| `AudioSession` start/stop in `liveKitConnection.ts` | found missing while wiring the above; a pure correctness fix | ✅ shipped |

Still not free, and not attempted: `pod install`/Gradle sync, an actual
device build, or a real `room.connect()` — that's the first LiveKit
session, and it starts the metered spend (LiveKit + Deepgram + Anthropic
+ Cartesia) this whole doc has been designed around avoiding.

### Blocked on the first funded session

Mostly unchanged from the original plan, but the entry point is
different now — the first funded session should be **"does the
concierge voice chat actually work on a device,"** not an abstract
latency/turn-taking benchmark. It exercises the whole native stack
(mic capture, AEC, LiveKit connect, agent audio playback) with the
smallest possible surface, before anything narration-interrupt-shaped is
built on top of it:

Device build + `pod install`/Gradle sync, real `room.connect()` against
the concierge, latency baseline (p50/p95 per stage), turn-taking feel,
persona voice listening checks, end-to-end interruption QA, and the
podcast voice-continuity seam. **Script that session in advance** — a
fixed 20–30-turn run across ack / simple / tool-calling, executed once,
rather than exploratory poking.

3d (adaptive interruption config) and Feature B of 3c (the narration
interrupt) can both be tackled before or after that session — neither
strictly depends on it, but Feature B in particular is a product
decision (does an interrupt-and-resume narration experience belong on
`NarrationCard`, and is it worth a screen rewrite) rather than an
engineering one, so it's left for the user to scope rather than picked
up here. If Feature A's device validation goes well, Feature B's
`voiceSessionOpener` reuses the same `connectToLiveKitRoom`/
`AudioSession` plumbing — it would no longer be starting from zero.

The one rule that survives the budget constraint: **nothing here gets
called "faster" until the funded session says so.** It's built, tested
offline, and gated — the measurement is still what closes each item.
