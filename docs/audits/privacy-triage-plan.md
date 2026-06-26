# Privacy Triage Fix Plan

**18 real user leaks / 5 operator-only / 8 dismissed (mitigated + false-positive) / 3 needs-human, out of 34 triaged.** (Cluster C already fixed in a prior pass.)

> **Progress (2026-06-25):** ✅ **P0** (hero_title projection guard, 4) · ✅ **P1** (proactive system-message scrub + social_state strip + system-row filter, 3) · ✅ **P2a** (present_options `check_proposal_privacy` guard, 2) · ✅ **P2b** (`why_for_person` dropped in group, 1) · ✅ **P2c** (shapes pitch/best_for scrubbed, 1) · ✅ **P3** (personal take falls back to curator in group, 1) · ✅ **P4** (DNA card skipped in group conversations, 1) · ✅ **P5** (Atlas Unpacked DNA, 2) · ✅ **P6** (Discover friends hook, 1) · ✅ **P7** (destination RedactionPolicy, 1) · ✅ **P8** (planning telemetry private fields stripped, 1) — **ALL 18/18 real-user-leaks FIXED, tested, boundary-clean.** 240 privacy-related tests pass. 0 new failures.

Sharper-lens re-verification of the Run-3 findings. "Real user leak" = a private constraint VALUE or who-holds-which-constraint attribution reaches another USER (group / cross-user / public) — not merely a member name, not an operator-only sink. Verdicts use the project's asymmetric-compose model (the compose path is corpus-guarded; sibling structured-card / proactive / public-projection paths were left unguarded).

---

## 1. Shared chokepoints

Grouping the 18 real-user-leaks by fix chokepoint reveals four clusters where one fix closes multiple findings:

### SHARED-A: `build_public_story_payload` hero_title guard — closes 4 findings
**File:** `backend/core/story_projection.py:167` (the `hero_title=story.hero_title` assignment)
- `hero-title-public-story-landing-html` (public HTML `<title>`/OG tags)
- `hero-title-public-story-json` (public `/api/public/stories/{slug}` JSON + profile list + feed event)
- `hero-title-public-plan-seed` (login-free plan-seed + HTML `<h1>`)
- `hero-title-story-published-feed-event` (followers' feed event context)

All four egress sinks read `PublicTripStory.hero_title` from this single projection. Sections and `hero_subtitle` are already guarded by `check_private_signal` + `_names_present(redact_names)` (lines 131-141); `hero_title` is the deliberate unguarded exception. **One fix:** add a `_safe_hero_title(story.hero_title, redact_names)` helper that, when `not check_private_signal(...).is_safe` OR `_names_present(..., redact_names)`, substitutes a neutral fallback (`f"A {destination} Trip"` / `trip_title`) instead of the raw composed title. Then route the two bypass paths through the projection too: `list_public_stories_for_user` (`trip_story_shares.py:435-439`) and `_emit_published` (`trip_story_shares.py:316`) must consume the sanitized title, not the raw `trip_stories.c.hero_title` column. Do NOT rely on the owner preview — it is not server-enforced (`create_story_share` never calls it) and shows `hero_title` verbatim anyway.

### SHARED-B: proactive group-interjection system row — closes 3 findings
**File:** `backend/concierge/triggers.py:150-175` (build/persist of the enriched proactive system message), with ingest-side scrub at `backend/notifications/group_interjection.py:286`
- `proactive-system-prompt-persisted-group`
- `haiku-interjection-intent-reason-group-system-message`
- `interjection-group-candidate-raw-system-message`

These are three traces of the same defect: a Haiku-derived `decision.intent` (synthesized from raw `social_state_markdown` carrying per-member constraints + who-said-what) is persisted verbatim as a `sender_type="system"` row into the trip's shared GROUP conversation and served to all members via `get_history` (`get_messages` applies no `sender_type` filter). The agent's REPLY is already protected by strict-compose; only this inbound steering row is exposed. **One structural fix:** in `run_proactive_turn`, for the group branch (`private_uid is None`), deliver the proactive framing as ephemeral turn context (feed `message` to the model, persist only the composed reply) rather than writing a served system row — OR run `intent`/`prompt` through `strip_private_group_sections` + `check_private_signal` before persisting. **Plus ingest scrub:** in `group_interjection.py:_load_context:286` wrap `social_state_markdown` in `strip_private_group_sections` before it reaches the triage LLM (matching `group_compose.py:644`). **Belt-and-suspenders:** `get_history`/`get_messages` exclude proactive `sender_type="system"` rows from member-facing payloads.

### SHARED-C: `check_proposal_privacy` / `load_private_corpus_for_trip` on sibling group-card tools — closes 4 findings
**Shared primitive:** `check_proposal_privacy` + `load_private_corpus_for_trip` (`backend/concierge/privacy_redactor.py`), already wired into `_execute_propose_change` only.
- `present-options-reaction-card-bypasses-guards` (`_propose_present.py:_execute_present_options`)
- `present-options-reaction-card-dup-trace` (same handler — duplicate trace, same fix)
- `generate-trip-shapes-card-bypasses-compose-guard` (`_shapes.py:158`)
- `post-venue-card-why-for-person-personal-memory` (`content.py:_execute_post_venue_card`) — uses the re-exported `check_private_signal`

Same defect class on four group-facing structured-card writers that bypass the trust-loop boundary. Each needs: load the trip-wide private corpus, scan the LLM-authored free-text fields, reject/re-draft on violation. `present_options` and `generate_trip_shapes` need `trip_id` threaded through (present_options currently only gets `conversation_id`/`conversation_type`). Two distinct handler edits cover three of these (present_options is one handler, two traces); `_shapes.py` and `content.py` are separate. They share the guard primitive, not the call site.

### SHARED-D: `check_private_signal` on Atlas Unpacked DNA line — closes 2 findings
**File:** `backend/atlas/unpacked.py:121-122` (`build_unpacked`, `dna_line` selection)
- `atlas-unpacked-builder-dna-phrase-no-check`
- `atlas-unpacked-interests-strong-constraint-label`

Both public consumers (HTML landing lede in `atlas_unpacked_landing.py` and the PNG via `render_unpacked_card`) read the same `you_card.title` from this single `build_unpacked` output. **One fix:** `dna_line = next((p for p in dna_phrases if check_private_signal(p).is_safe), None)` instead of `dna_phrases[0]`; drop the "you" card if none pass.

**Standalone real-user-leaks (no shared chokepoint):**
- `cached-personal-take-posted-to-group` — `content.py:_execute_post_venue_card` take selection (lines 245-262); shares the corpus primitive with SHARED-C but a distinct sub-path (personal-tier Take prose).
- `taste-dna-reflection-card-to-group` — `first_contact.py:350-353`; fix = re-target card to user's 1:1 conversation, not the group.
- `discover-feed-friends-note-curator-hook` — `discover/compose.py:509`; `redact_private_signal` at read/compose boundary.
- `destination-ignores-redaction-policy-profile-list` — `trip_story_shares.py:list_public_stories_for_user`; honor `RedactionPolicy.show_destination`.
- `agent-events-planning-search-venues-input-passthrough` — `planning_agent/agent.py:_log_planning_tool_event`; sanitize `tool_input` at source.

---

## 2. Ordered fix plan (real-user-leaks, highest blast-radius first)

### P0 — SHARED-A: hero_title public projection guard (4 findings, public audience)
**File:** `backend/core/story_projection.py:167` (+ `trip_story_shares.py:316,435-439`)
**Audience evidence:** `get_public_story_by_slug` → `story_landing.py` unauthenticated routes render `hero_title` into HTML `<title>`/OG/Twitter tags (crawler-indexable) and `/api/public/stories/{slug}` JSON; `list_public_stories_for_user` selects the raw column for another user's profile view; `_emit_published` copies it into a followers' `story_published` event. All public/cross-user, none 1:1 or operator-only.
**Fix:** Add `_safe_hero_title(raw, redact_names)`: return raw only when `check_private_signal(raw).is_safe and not _names_present(raw, redact_names)`, else a neutral fallback (`f"A {destination} Trip"` / `trip_title` / `"A Trip"`). Use it in `build_public_story_payload` and route the two bypass paths (`list_public_stories_for_user`, `_emit_published`) through the projected value. Optionally surface a `hero_title_redacted` flag in `StorySharePreview`.
**Why first:** single helper closes 4 findings across the widest (public, crawler-reachable) audience.

### P1 — SHARED-B: proactive group-interjection system row (3 findings, group audience)
**File:** `backend/concierge/triggers.py:150-175` + `backend/notifications/group_interjection.py:286`
**Audience evidence:** group branch resolves to the trip's shared group conversation (`get_or_create_session_for_trip`, `conversation_type="group"`, ≥2 human members); `persist_user_message(sender_type="system")` writes verbatim; `get_history` (`require_trip_member_async`) → `get_messages` applies no `sender_type` filter → every member reads the row. FE renders `sender_type="system"` as a visible bubble.
**Fix:** (A) In `run_proactive_turn` group branch, persist the proactive intent/prompt as ephemeral turn context (or a neutral marker), not a served `sender_type="system"` row; if a row must persist for audit, run `intent`/`prompt` through `strip_private_group_sections` + `check_private_signal` first. (B) In `group_interjection.py:_load_context:286`, strip `social_state_markdown` before the triage LLM. (C) Belt-and-suspenders: exclude proactive system rows from `get_messages` member-facing output.

### P2 — SHARED-C: sibling group-card privacy guards (4 findings, group audience)
**Shared primitive:** `check_proposal_privacy` + `load_private_corpus_for_trip` (`privacy_redactor.py`).
**Audience evidence:** all four post via `create_message`/`create_reaction_card`/`create_venue_card`/`create_trip_shapes_card` into the bound GROUP trip conversation, read by every member. `present_options` hard-rejects `conversation_type=="personal"` and is `_GROUP_ONLY`; `post_venue_card` is `_ALWAYS_TOOLS` and reachable on group turns.

- **P2a — `_propose_present.py:_execute_present_options`** (closes `present-options-reaction-card-bypasses-guards` + `present-options-reaction-card-dup-trace`): before `create_reaction_card` (~line 589), thread `trip_id` through `tools.py:337` dispatch, load corpus, run `content`/`context`/`options[].label` through `check_proposal_privacy`; on `not is_safe` return a re-draft error mirroring `_execute_propose_change` lines 360-377. Keyword layer works pre-`trip_id`-wiring.
- **P2b — `content.py:_execute_post_venue_card` `why_for_person`** (closes `post-venue-card-why-for-person-personal-memory`): thread `conversation_type` into the handler (mirror `present_options` at `tools.py:337`); for group conversations, scan `why_for_person`/`why_for_group`/`move`/`what_to_notice[]`/`what_to_skip[]`/`timing_note` via `check_private_signal` + `load_private_corpus_for_trip`; strip/down-convert `why_for_person` (a structurally 1:1 slot) in group context regardless of corpus match.
- **P2c — `_shapes.py:158`** (closes `generate-trip-shapes-card-bypasses-compose-guard`, confidence medium): in the `if conversation_id and shapes:` block before `create_trip_shapes_card`, run each shape's `pitch`/`best_for`/`anchors` through `check_proposal_privacy` using the already-threaded-but-unused `trip_id`; reject/scrub on violation, keyword-layer fallback on corpus-load failure.

### P3 — `cached-personal-take-posted-to-group` (group audience, high)
**File:** `backend/concierge/tool_handlers/content.py:245-262` (take selection), `tools.py:356-362` (thread `conversation_type`)
**Audience evidence:** `post_venue_card` (`_ALWAYS_TOOLS`, not `_GROUP_ONLY`) → `create_venue_card` → `create_message(sender_type="agent")` into the group conversation. `get_most_recent_personal_take(user_id, mode=None)` pulls the requester's PERSONAL-tier Take, generated with their `personal_memory` + `hard_constraints` in context.
**Fix:** When `conversation_type=="group"` (or unknown), run `take_headline`/`take_verdict.opinion` through `check_private_signal` + `load_private_corpus_for_trip`; on violation fall back to `get_curator_take` or name+detail only. Prefer curator-tier outright in group conversations. Fail-safe: corpus-load failure falls back to curator, never posts unscanned personal prose.

### P4 — `taste-dna-reflection-card-to-group` (group audience, high)
**File:** `backend/concierge/first_contact.py:350-353` (`post_dna_reflection_card_if_eligible`), driven from `backend/api/routes/chat.py:403`
**Audience evidence:** card posts to `session.conversation_id` = the trip's PRIMARY GROUP conversation (`get_or_create_trip_conversation`, one shared conversation per trip); `get_messages` filters only by `conversation_id`, so every member sees it. `_build_reflection_phrases` emits deterministic server-side budget-band phrases (`"stretches every dollar"` / `"pays for the unforgettable"`) from the actor's private Personal Memory — a concrete constraint VALUE, not an LLM maybe.
**Fix:** Re-target the card to the actor's OWN 1:1/personal conversation instead of the group `session.conversation_id` (preferred — removes cross-user exposure entirely). In `chat.py:403`, stop passing the group `session.conversation_id`; have `post_dna_reflection_card_if_eligible` resolve/create the actor's personal (non-trip) conversation and post there. Do NOT add redaction inside `create_message` (shared by legitimate 1:1 flows).

### P5 — SHARED-D: Atlas Unpacked DNA line (2 findings, public audience)
**File:** `backend/atlas/unpacked.py:121-122` (`build_unpacked`)
**Audience evidence:** unauthenticated `/unpacked/{token}` HTML lede (`atlas_unpacked_landing.py:143`) and `/unpacked/{token}/card.png` PNG (`render_unpacked_card`), both `noauth`, token = bearer credential. `dna_phrases[0]` is the LLM-generated cached `reflection_phrases[0]` (from `_generate_dna_phrases` fed the raw PM narrative) — can carry sobriety/accessibility/medical/budget constraint values.
**Fix:** `dna_line = next((p for p in dna_phrases if check_private_signal(p).is_safe), None)`; drop the "you" card if none pass. Single site feeds both HTML and PNG. (Note: this is a tighter, deterministic subset of the needs-human Unpacked items — see §6; the in-app self-preview makes the *budget* case product-judgment, but the build-time `check_private_signal` guard is the load-bearing fix and safe to ship now.)

### P6 — `discover-feed-friends-note-curator-hook` (cross-user audience, high)
**File:** `backend/discover/compose.py:509`
**Audience evidence:** `get_social_feed(user.id)` surfaces events authored by accounts the requester FOLLOWS; the actor's free-text `note` (from unconstrained `POST /api/events` `context` dict, no key whitelist) renders as the friend-card `hook` attributed by `display_name`. A follower reads another user's note.
**Fix:** `raw_hook = ctx.get("curator_hook") or ctx.get("note"); hook = redact_private_signal(raw_hook) if raw_hook else None`, dropping on `check_private_signal` flag. Scan belongs at the read/compose boundary (audience-known), since the same note feeds the actor's own surfaces where redaction is unwanted. Also remove the dead `curator_hook` key.

### P7 — `destination-ignores-redaction-policy-profile-list` (cross-user audience, medium)
**File:** `backend/core/db/trip_story_shares.py:list_public_stories_for_user` (select lines 409-414, build 435-441)
**Audience evidence:** feeds `PublicProfile.stories` served by `GET /api/users/{user_id}/profile` to any authenticated viewer of another user's profile. Emits `destination = place_name or trip_title` without selecting/consulting `redaction_policy` — bypassing the `if policy.show_destination` gate the slug path honors (`story_projection.py:158-160`). `show_destination=False` is the owner's explicit act of hiding a sensitive destination (rehab/medical/partner's home city).
**Fix:** Add `trip_story_shares.c.redaction_policy` to the select; set `destination` only when `RedactionPolicy.model_validate(...).show_destination`, else `None`, mirroring the slug path.

### P8 — `agent-events-planning-search-venues-input-passthrough` (group audience, medium/LLM-mediated)
**File:** `backend/planning_agent/agent.py:_log_planning_tool_event` (the `context={"input": tool_input, ...}` construction)
**Audience evidence:** raw `search_venues` args (`dietary_requirements`, `max_price_per_person`, `max_energy`) land in `agent_events.context` → `_format_agent_events` dumps the full context verbatim into the Haiku daily-digest prompt → digest is keyed by `trip_id+day_number` (not per-user) and rendered on the GROUP home/concierge feed for every member. The `redact_corpus_phrases` egress guard cannot catch a numeric EUR ceiling or sub-8-char tokens like `halal`.
**Fix:** Stop storing the full `tool_input` under `context["input"]`. Store only aggregate-safe fields (tool name, iteration, `result_length`, count of dietary tags, has-price-cap bool, energy band bucket) — never the raw constraint values. This removes the values from the digest prompt entirely, making the redactor gap moot. Defense-in-depth: drop a constraint-key denylist in `_format_agent_events`.

---

## 3. Operator-only leaks (lower priority — no cross-user egress)

These reach operator dashboards / telemetry tables / git-ignored trace files / app logs only. Real PII gaps worth closing for operator data-minimization, but NOT user leaks. None is reachable by another user (verified: no API route, feed, conversation, or card reads these sinks back).

| id | file:chokepoint | fix |
|---|---|---|
| `reasoning-spans-plan-personal-memory` | `telemetry.py:_insert_reasoning_spans:315,317` | wrap `plan`/`observation` in `redact()` before `_truncate` (redact-then-truncate ordering) |
| `reasoning-spans-observation-tool-result` | `agent.py:1500` (`_on_tool_result` snippet capture) | optional: coarse-redact whereabouts/location results (strip km/minutes) before `result_str[:2000]` |
| `concierge-turns-tool-calls-input-fact-values` | `telemetry.py:_normalize_tool_call` | redact string input/output; or drop/whitelist `fact_remember` `value` field (store key only) |
| `planning-tracer-metadata-task` | `planning_agent/agent.py:50` (`_build_planning_tracer`) | store structural surrogate (`task_hash`, `task_len`) instead of `task[:200]`; sink is git-ignored + origin-gated |
| `memory-prune-reason-log-info` | `concierge/memory_tools.py:780` | drop free-text `reason` from INFO line (`logger.info("Pruned %d observations", count)`); move to DEBUG |

---

## 4. Dismissed (mitigated + false-positive — on record)

| id | verdict | why |
|---|---|---|
| `triage-prompt-for-agent-taste-prose-system-message` | mitigated | Triage prompt mandates taste nudges be `target="private"`; `triggers.py:76-131` routes private to per-user 1:1 conversation; fails closed (`InvalidPrivateTarget`) if target missing, no group fallback. |
| `feasibility-catch-reschedule-proposal-no-privacy` | mitigated | `check_proposal_privacy` invoked unconditionally inside `create_change_proposal` (`change_proposals.py:275`) against the unioned trip corpus; redacts all `impact_analysis` strings on violation. |
| `hero-title-profile-public-stories-list` | mitigated | Human-in-the-loop owner preview returns byte-for-byte public payload incl. raw `hero_title`; owner authors/reviews before publishing. (Note: SHARED-A still hardens the non-owner-constraint case the preview doesn't flag.) |
| `booking-receipt-venue-brief-constraints-group` | mitigated | `build_venue_brief` runs every dietary/accessibility value through `_strip_named_subject` + `redact_corpus_phrases` against the trip corpus before the receipt; `[private detail omitted]`. |
| `agent-events-concierge-search-input-passthrough` | mitigated | `daily.py:156-171` runs `redact_corpus_phrases` (unioned member corpus, ≥8-char verbatim) on the rendered group digest — canonical egress guard. (Contrast P8: the planning-agent variant leaks numeric/short values the corpus scrub can't catch.) |
| `plan-ready-card-first-day-teaser-day-theme` | false-positive | Only `_scan_planner_output` runs (a prompt-injection redactor, `PEER_AGENT_REPLY`), and it scans `raw_plan`/`group_facing_message`, NOT `day_themes`. No private-constraint guard, but the flagged field is structurally not a constraint carrier. |
| `vote-comment-leaks-constraint-proposal-detail` | false-positive | Vote `comment` is self-authored user free text, not agent-composed from another member's private corpus — the leak class the redactor exists to stop cannot arise. |
| `invitee-note-verbatim-external-sms-email` | false-positive | `invitee_note` is organizer-authored free text addressed to the very recipient it is sent to; human author chooses content and audience. HTML-escaping covers injection, not privacy. |

---

## 5. Needs-human (product-judgment calls)

These egress to a real audience but turn on a product decision — usually "is an owner publishing their OWN previewed self-constraint a leak?" Defer to product; sketched fixes attached if the call is "yes."

- **`public-story-section-hero-constraints-outside-regex`** (`story_projection.py:build_public_story_payload`, public) — section/hero filter runs `check_private_signal` WITHOUT a `private_corpus` arg, so only the keyword layer runs; terms outside the lexical list (`vegetarian`, `celiac-safe`, `diabetic-friendly`, `low-sodium`, `pescatarian`) pass to the public card. The owner previews the literal text byte-for-byte, but the preview does NOT FLAG these as private. **Question:** is owner self-disclosure of their own dietary note under a faithful-but-unflagged preview acceptable? **Fix if yes-it's-a-leak:** thread the owner's `private_corpus` into the section/hero `check_private_signal` calls (corpus layer is the principled fix; the keyword list will always be incomplete).

- **`atlas-unpacked-dna-phrase-constraint-card-png`** (`refresh_memory.py:_generate_dna_phrases`, public) — LLM-generated DNA phrase can echo a confidential constraint (celiac/step-free/allergy) verbatim into the public Unpacked card PNG. There IS a genuine human-in-the-loop gate (user previews the exact DNA line in-app before minting the share link), so it's self-authored public sharing, not silent cross-user exposure. **Question:** is self-initiated, previewed public sharing of one's own recap a "leak" if the user won't recognize the phrase as disclosing a private diagnosis? **Fix if yes:** add a constraint-exclusion clause to `_DNA_PHRASE_SYSTEM` + post-filter phrases against the `hard_constraints` snapshot before caching at `refresh_memory.py:545`. (P5's build-time `check_private_signal` guard is the deterministic floor and ships regardless.)

- **`agent-events-tool-error-context`** (`digest/engine/formatters.py:_format_agent_events`, group) — tool-error headline can carry a reformatted constraint scalar (`price_ceiling=50`, `kosher`) into the group digest prompt; `redact_corpus_phrases` only catches ≥8-char verbatim corpus matches, so a bare reformatted scalar escapes — but WITHOUT attribution (no who-stated-which mapping in the prompt). **Question:** is an un-attributed reformatted scalar a leak (weakest datum class)? **Fix if yes:** drop `original_error`/`args_sig` from the digest-prompt `ctx_items` in `_format_agent_events` (operator telemetry has no business in a user-facing digest); leaves the operator row untouched.
