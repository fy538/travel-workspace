# Vesper — Content Contracts: Open-Questions Investigation

**Date:** 2026-07-08 · **Repos:** `travel-agent` (generation) + `travel-app` (render) · **Mode:** investigation only, no code changed.

Follow-up to [content-contracts-audit.md](content-contracts-audit.md). Nine open questions, each answered CONFIRMED / REFUTED / UNCERTAIN with `file:line` evidence and the risk/roadmap item it gates. Two answers change the roadmap materially: **O1 refutes R4**, and **O8 corrects the main audit's Atlas premise** (the LLM path is live in prod, not dark).

Paths are relative to `/Users/feihuyan/travel-workspace/{travel-agent,travel-app}`. `fly.toml` is the checked-in config; where a `fly secrets` override could differ, the exact prod readback command is named.

---

## O1 — Invite itinerary auth (gates R4)

**Verdict:** REFUTED (no leak). **R4 falls, from code alone.**

**Evidence**
- FE call — `travel-app/utils/inviteTimeline.ts:118-126` swallows failure and falls back:
  ```
  if (trip?.trip_id) {
    const days = await api.getItinerary(trip.trip_id);
  } catch { // Fall back to date-derived rows.
  ```
- API client — `travel-app/utils/api/http.ts:750-751` resolves to `GET /api/trips/{tripId}/itinerary`; `_request` attaches a Bearer header only when a token exists (`http.ts:411`), so an anonymous visitor sends none.
- Backend route — `travel-agent/backend/api/routes/trips.py:1230-1241`:
  ```
  async def get_trip_itinerary(
      actor: User = Depends(get_current_user),
      await require_trip_member_async(trip_id, actor)
  ```
- Auth deps — `travel-agent/backend/api/auth.py:156-157` 401s a token-less caller ("Missing or invalid Authorization header"); `auth.py:251-253` 403s an authenticated non-member.
- The only FE path that surfaces `day_theme`/venue titles is `rowsFromItinerary` (`inviteTimeline.ts:88-110`, `:100` `day.day_theme`, `:99` `firstBlock?.title`) — it runs **only when `getItinerary` succeeds** (i.e. a logged-in member). Anonymous visitors get the fallback `buildInviteTimelineDays` (generic "Arrival"/"Yours to shape" + trip dates/title only, `:47-85`).

**Consequence.** The invite page does not leak model-authored venue names or `day_theme` to unauthenticated visitors — the double gate (401 token-less, 403 non-member) holds and the FE degrades gracefully, consistent with the page's own privacy promise (`invite/[slug].tsx:620-621`). R4 is refuted. **One config invariant to preserve (not a code leak):** if `SKIP_AUTH=true` were ever set in prod, `get_current_user` returns the dev user (`auth.py:153-154`) and the itinerary endpoint would return full blocks. That is an environment invariant to verify, not a defect in this code path. (The invite *preview* — real title/destination/dates + Haiku snapshot from the intentionally-public `view_invite`, `invites.py:617-618` — is exposed to any slug-holder by design and is outside R4's scope.)

---

## O2 — Receipt→expense caller set (gates R1 severity)

**Verdict:** REFUTED as active → **R1 is latent, not active.** The FE always confirms; the OCR number wins only for test callers.

**Evidence**
- Handler fallback — `travel-agent/backend/api/routes/expenses.py:925`:
  ```
  amount = body.amount if body.amount is not None else ocr.get("total_amount")
  ```
  then `_compute_shares(amount, …)` (`:941`) and `async_create_expense(…, amount=amount, …)` (`:952-957`) create real split shares.
- Request model leaves `amount` optional — `expenses.py:85-92`: `amount: float | None = None` (guarded only against *both* being None at `:928-929`).
- FE always sends a validated amount — `travel-app/components/expense/AddExpenseSheet.tsx:292-296` rejects `isNaN || <= 0`, and `:340` always sends `amount: parsedAmount`. FE can never submit null.
- Only prod caller is the route itself (`expenses.py:897`); grep for `create_expense_from_receipt` / `receipt_scan` finds no agent tool, celery task, or retry constructing the request. `source="receipt_scan"` appears only at `:965`.
- Only non-FE callers are tests — `travel-agent/tests/api/test_expenses_api.py:1033-1039` `_create_from_receipt_body()` omits `amount`, so those tests let the OCR total (85.0) win. Test-only.

**Consequence.** In production the money path is safe: the sole prod caller (FE `AddExpenseSheet`) always sends a user-confirmed positive amount, so an OCR number can never silently become a real expense. R1 de-escalates to latent. The residual is structural: the request model leaves `amount` optional (`expenses.py:91`), so a *future* server-side caller (agent import / background job) that omits it would make R1 active. External fact that would flip it: the existence of any such caller — none today.

---

## O3 — Output-guard mode intent (gates Tier-0 item 1)

**Verdict:** REFUTED that `log` is permanent → `log` is an explicitly **temporary, pre-launch measurement phase**; flipping it is an **unresolved risk decision, not a pure config change**.

**Evidence**
- `travel-agent/fly.toml:191-195`: `# log mode = record violations to concierge_turns.guard_violations but ship the reply unchanged. See … output_guards.py for activation runbook before` → `CONCIERGE_OUTPUT_GUARD_MODE = "log"`.
- `travel-agent/backend/concierge/output_guards.py:19-23` (docstring): `"regenerate" and "block" are reserved for Phase 5 (post-launch escalation once we've calibrated false-positive rate).`
- `output_guards.py:1097-1099`: `# LOG-ONLY: the goal for now is to MEASURE how often operational facts reach the user unbacked, before deciding whether to escalate.`
- `output_guards.py:1291-1297`: the posture has **partially advanced** — `session.py` now honours `regenerate` for *grounding* violations, while reply-length stays log-only "pending corrective-prompt design."
- Committed plan — `docs/working/Agent Architecture Review 2026-05.md:33`: "Output guard runs in `log` mode by default; rollout to `regenerate` requires calibration data."

**Consequence.** Tier-0 item 1 is not a one-line flip: escalating to `regenerate`/`block` requires the false-positive-rate calibration data that `log` mode exists to collect. That data lives in prod `concierge_turns.guard_violations` and is not determinable from code. Note the escalation is already mid-transition (grounding→regenerate may be live via `session.py`) — so verify the *current* effective mode per guard type in prod before treating R5 as fully unmitigated.

---

## O4 — Narration length contract (gates §5 scope)

**Verdict:** UNCERTAIN on stated intent — the soft-only word target is **plausibly deliberate for TTS pacing**, but the omission of a hard clamp is **undocumented** (no comment, test, or design note).

**Evidence**
- Narration uses a soft, prompt-embedded target with no output clamp — `travel-agent/backend/concierge/narrator.py:281-283`: `Keep it to {target_words} words — this will be spoken aloud.` Post-generation is strip-only (`:316`); `:345` merely logs `len(reply.split())`.
- Prerender is identical — `guide/prerender.py:253-260` (soft target) → `:270` strip → `:272` straight to TTS `synthesize()`.
- Target source is a plain dict with no ceiling — `core/narration.py:40-44` `DEPTH_WORD_TARGETS = {"intro":200,"detail":150,"obscure":120}`, `style_word_target()` just multiplies (`:155-164`).
- Contrast — surfaces that DO hard-clamp: `concierge/group_compose.py:210-215` `_clamp_group_copy` ("always <= the budget"); `bridge_generator.py:171-176` (`# Hard length cap — 25 words … trim`).
- The only `truncat`/clamp hits in the narration pipeline are prompt-*input* trimming (`guide/prompts.py:91,107`), never output.

**Consequence.** The clamped surfaces render in fixed UI chrome (budget is layout-driven); narration streams to TTS, where over-length costs pacing/latency, not layout breakage — a coherent reason to rely on a soft target plus a generous `max_tokens=600` (`narrator.py:312`) rather than a word slice (which would cut audio mid-sentence). But that reasoning is inferred, not documented. This is the lowest-priority §5 item: either add a one-line rationale comment, or, if a ceiling is wanted, prefer a token-cap / sentence-boundary trim over a hard word slice.

---

## O5 — Curator take grounding (gates R8-adjacent)

**Verdict:** CONFIRMED — the curator take prompt has **no grounding / no-invent / "use only the brief" block**; it can assert place-facts the brief didn't provide.

**Evidence**
- The personal prompt imports `GROUNDING_RULES` (`core/prompts/takes/personal_prompt.py:16-25`, interpolated `:55`); the curator import list omits it — `curator_prompt.py:15-22` pulls `ANTI_PATTERNS, CAVEAT_RULES, OUTPUT_FORMAT, STANCE_GUIDANCE, VERDICT_RULES, VOICE` only.
- `CURATOR_SYSTEM` (`curator_prompt.py:24-53`) has no grounding language; its only source phrase is descriptive: `:32-33` "…based on the structured brief and dossier provided" (names the inputs, doesn't forbid going beyond them). Closing instruction `:95` is formatting-only.
- `GROUNDING_RULES` itself (`shared.py:170-188`) is written **entirely about user claims** ("Do not invent past trips, saved venues, preferences…") — so **no place/venue-fact no-invent rule exists anywhere in `shared.py`**, meaning even the personal take isn't guarded against inventing place-facts.
- `VOICE` (`shared.py:11-29`) actively pushes confident specifics ("Order the bacalhau," "Name things the way locals do"), inviting unbacked operational facts (hours, dishes, "closed Mondays").

**Consequence.** Confirms R8-adjacent: the curator take (generated at research time, off the concierge output-guard path, so uncaught by O3's guard) can state facts its brief didn't provide. Two fixes fall out, not one: (a) add a brief-bounded block to the curator prompt; (b) add a **place-fact** no-invent rule to `shared.py` — the existing `GROUNDING_RULES` covers only *user* claims, so this gap affects the personal take too.

---

## O6 — Dossier auto-publish state (gates R8 priority)

**Verdict:** REFUTED (auto-publish is OFF) — code default false, no repo prod override → green dossiers strand at `draft`.

**Evidence**
- Default false — `core/feature_flags.py:93` `return _truthy("AUTO_PUBLISH_GREEN_DOSSIERS")`; `_truthy` defaults absent env vars to false (`:17`).
- Intended posture — `feature_flags.py:89-91`: "Default off per convention. Set `AUTO_PUBLISH_GREEN_DOSSIERS=true` in prod to close the publication gap. Leave off to keep an editorial human-in-the-loop posture, promoting via the publish script instead."
- Not set in prod config — no match in `fly.toml`/`.env*`/`docs/` (contrast `ATLAS_LLM_ENABLED`, which *is* in `fly.toml`).
- Behavior — `research_agent/agents/persist.py:280` (promote only when on) + `tests/research_agent/test_persist_results.py:304` ("Default (off): land at 'draft'").
- Nuance — `feature_flags.py:86-87`: green content is **not** enqueued for review; it just strands at `draft` until a manual `scripts/publish_approved_dossiers.py --apply` run.

**Consequence.** R8's "confidence discarded at render on a shareable asset" is gated by a manual publish step, not an active review queue — so nothing auto-publishes today, but there's also no human *review* of quality/confidence, just a promotion gate. R8 stays de-prioritized while off. **Settle prod definitively:** `fly ssh console -a <app> -C 'printenv AUTO_PUBLISH_GREEN_DOSSIERS'` (a `fly secrets` override can't be read from the repo; repo evidence strongly indicates OFF).

---

## O7 — Weather source (gates the weather never-generated row)

**Verdict:** CONFIRMED — for the daily-digest `context_notes` path, weather is **minted-always**; it never joins a weather data source before render.

**Evidence**
- `digest/prompts.py:35`: `"context_notes": "weather, energy, occasion, group mood — anything relevant"` — the model authors it, with no weather input.
- Digest input assembly injects no weather — `digest/engine/llm_calls.py:46-56` renders only blocks/messages/agent_events/user_events/observations/edits.
- The block formatter carries none — `digest/engine/formatters.py:36-62` emits time/title/duration/venue_ref/status/notes only.
- A real weather API exists on a **different path** — `concierge/tool_handlers/planning/_plan.py:236` calls open-meteo and writes `trip_context["weather_forecast"]` (`:262`) for the concierge/planner, not the digest. Home concierge weather cards read client-supplied `ambient` query params (`api/routes/concierge_home.py:233-246`), not a server join.

**Consequence.** Any weather claim rendered from daily-digest `context_notes` (e.g. `day_arc`/recap surfaces) is a hallucination anchored to nothing — real weather data (open-meteo) exists in the codebase but is never joined into this prompt. The "weather = model-minted" row stands for the digest path; the fix is to either join open-meteo into the digest input or drop weather from the `context_notes` instruction.

---

## O8 — Atlas honesty gate + LLM path state (gates Atlas risk) ⚠️ corrects the main audit

**Verdict (a):** CONFIRMED — the badge gates strictly on `composed_by === 'llm'`, with a fail-safe fallback.
**Verdict (b):** REFUTED — the Atlas LLM path is **live in prod**, not dark. `ATLAS_LLM_ENABLED = "true"` is set in `fly.toml`.

**Evidence (a)**
- `travel-app/app/atlas/artifact/[id].tsx:164`: `const isAuthored = artifact.composed_by === 'llm';`
- Fail-safe — `:159-160` (comment): "null/undefined (pre-field legacy rows) is treated the SAME as mock, never as authored, so this can never overclaim." Strict equality means `'mock'`, null, or any typo falls to the non-authored branch.
- Render honors it — `:224-233` shows "VESPER WROTE" only when authored, else "DRAFT · NOT YET COMPOSED" + "Vesper hasn't written this up yet — this is a plain summary from what's known."

**Evidence (b)**
- Code default off — `core/feature_flags.py:27` `return _truthy("ATLAS_LLM_ENABLED")`, docstring `:23-25` "Default off — V0 ships with the deterministic mock…".
- **Prod overrides it on** — `travel-agent/fly.toml:198`: `ATLAS_LLM_ENABLED = "true"` (comment `:196-197` "enable the real LLM composer for postcard prose + almanac summaries").
- Docs are stale — `docs/operations/AI Ops Safety Plan.md:80` and `Environments Dogfood and Data Substrate.md:262` still say `false`; the deployed `fly.toml` is authoritative.

**Consequence.** The honesty gate is shipped and fail-safe (it cannot overclaim on a missing/wrong field — good). But the main audit's premise that Atlas fabrication is "latent because the flag is dark" is **wrong**: the LLM path is enabled in prod, so real-LLM artifacts get `composed_by='llm'`, legitimately render "VESPER WROTE," and the Atlas §1/§4/§5 findings (counts restated as prose in almanac/letter prompts, `one_line_read` delete-only on a shareable postcard, prompt-vs-clamp budget mismatches) are **live, not latent**. Confirm the deployed value with `fly ssh console -C 'printenv ATLAS_LLM_ENABLED'` (secrets can override; the checked-in config is explicit `"true"`).

---

## O9 — Planner price field (gates the planner price row)

**Verdict:** CONFIRMED — `price_per_person_cents` is a silent model estimate: absent from the planner prompt, persisted to `price_cents`, consumed downstream as "actual quoted pricing," with no "estimated" render marker.

**Evidence (a) — not in the prompt**
- The planner output schema lists no price field — `planning_agent/prompts.py:196-227` emits `venue_id, venue_name, type, experience_id, duration_minutes, reasoning, energy_rationale, travel_to_next{…}`. "price" appears once, in prose (`:170` "target price point"), never as an emitted field.
- The parser reads it back anyway — `planning_agent/output_parser.py:131` `price_per_person_cents=slot.get("price_per_person_cents")`; the field is populated only if the model volunteers an undocumented key. Schema documents it as "Planner-estimated cost per person… Null means unknown" (`schemas.py:99-102`).
- Persisted to `price_cents` — `core/db/itinerary_persistence.py:202` `price_cents=getattr(slot, "price_per_person_cents", None)`.

**Evidence (b) — rendered as real**
- `core/db/trips.py:3094-3095` (comment): "Prefer `itinerary_blocks.price_cents` when set — the LLM emits this in EUR cents and **it reflects actual quoted slot pricing.**" — false per the schema's own "planner-estimated" definition; the value is rolled into cost/budget totals.
- FE — `price_cents` exposed in `travel-app/utils/api/schema.gen.ts:14777,16671`; a grep for an "estimated"/"per person" qualifier on block price display found none.

**Consequence.** A price the model invents (unprompted, undocumented output key) is silently written to `price_cents`, consumed downstream as a real quoted price (`trips.py:3094`), and folded into budget totals with no "estimated" disclosure to the user — a genuine substrate-honesty defect. This **escalates** beyond the main audit's "latent fabrication vector" framing: the number is not merely persisted, it is actively labeled and used as fact.

---

## What this changes

**Falls / de-escalates.** **R4** (invite itinerary leak) is refuted from code — remove it from the active risk list (keep only the `SKIP_AUTH` prod invariant as a deploy check). **R1** (receipt-OCR → money) de-escalates from "worst path" to **latent**: prod is safe because the FE always confirms the amount; the only residual is the optional `amount` field on the request model, so the fix shrinks from "add a confirmation flow" to "make `amount` required (or reject null) at the API contract" to fence out future callers. **R8** (dossier confidence) stays de-prioritized: auto-publish is off, green dossiers strand at draft behind a manual publish step.

**Escalates.** **Atlas (O8) is the headline change** — the LLM path is live in prod (`fly.toml:198`), not dark, so the Atlas fabrication/reversibility/restraint findings are active today, not latent; the honesty *badge* is shipped and fail-safe, but the underlying prose findings need real attention. **O9 (planner price)** escalates from a latent vector to a confirmed defect — a fabricated number is stored and consumed as an actual quoted price and rolled into budgets, with a downstream comment that explicitly (and wrongly) asserts it's real. **O5 (curator grounding)** confirms a real gap and widens it: there is no place-fact no-invent rule anywhere in `shared.py`, so both curator and personal takes lack it.

**Stays, but re-characterized.** **R5 / Tier-0 item 1 (guard mode)** is not a free config flip — escalating off `log` requires prod calibration data (`concierge_turns.guard_violations`), and grounding-mode may already be partially escalated via `session.py`; verify effective per-guard mode in prod before sequencing. **O7 (weather)** confirmed minted-always for the digest path. **O4 (narration clamp)** is defensible-for-TTS but undocumented — lowest-priority §5 item.

**Needs a prod readback (not code) to fully close:** O6 (`AUTO_PUBLISH_GREEN_DOSSIERS`) and O8 (`ATLAS_LLM_ENABLED`) — both read from `fly.toml` here but could be overridden by `fly secrets`; commands given inline. O3's effective guard mode per type is also worth a prod check.

**Re-sequenced roadmap (evidence-based):** (1) O9 planner price — stop labeling a model estimate as quoted price; (2) Atlas prose findings — now live, not latent; (3) O5 place-fact no-invent rule in `shared.py` (fixes curator + personal); (4) R1 make receipt `amount` required at the contract (cheap fence); (5) O7 join or drop digest weather; (6) R5 guard-mode escalation — gated on calibration data, decision not code; (7) O4 narration clamp rationale — lowest priority.
