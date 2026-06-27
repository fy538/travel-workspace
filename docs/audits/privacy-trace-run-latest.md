# Privacy-Leak Trace — Run Output (latest)

**40 confirmed / 3 needs-human / 105 scanned / 0 errored**

> **PARTIALLY STALE — SUPERSEDED 2026-06-27 (HEAD `f698d228`).** The "40 confirmed" raw count
> below has since been triaged in `privacy-triage-plan.md`, which is the live status-of-record.
> Of the 40: the 40 collapse to ~34 unique findings → **18 real-user-leaks, ALL FIXED** in main
> (commit `5c46a47b`), plus 5 operator-only (open by design), 8 dismissed (mitigated /
> false-positive), and 3 needs-human (open). Notably, findings #12 (`vote-comment`), #13
> (`feasibility-catch` proposal), #20 (`invitee_note` SMS), and #24 (public-story
> dietary-outside-regex) were re-adjudicated in the triage plan as false-positive / mitigated /
> needs-human — NOT all 40 are real leaks. Do not treat the raw findings below as the current
> open list. **Status of record:** `privacy-triage-plan.md` (real-user) + `privacy-invariant-trace.md`
> (consolidated). This raw machine output is kept verbatim and is safe to overwrite on the next run.

> This is the **machine run-output** file. It is safe to overwrite on every run.
> A human merges confirmed findings into the curated `privacy-invariant-trace.md` (do not edit that here).

---

## COVERAGE

```
surfaces inventoried:                105
surfaces actually traced (scanned):  105
surfaces ERRORED (rate-limited, NOT cleared):        0
sweep angles ERRORED (whole angle missing, NOT cleared): 0
```

> **⚠️ WARNING — ERRORED ≠ CLEARED.** Any surface or sweep angle counted as errored above was
> **NOT examined and is NOT cleared of leaks** — it is merely unexamined. A zero in the
> errored rows means full examination on this run; a non-zero value would mean that many
> surfaces/angles remain unaudited and must not be treated as safe. This run errored on **0**
> surfaces and **0** angles, so all 105 inventoried surfaces were traced.

---

## Confirmed leaks (severity order — critical first)

### CRITICAL

#### 1. post_venue_card ships requester's Personal Memory to the whole group via recommendation.why_for_person
- **Severity:** critical
- **Surface / file:line:** `venue-card` — `backend/concierge/tool_handlers/content.py` `_execute_post_venue_card` ~159-309; `create_venue_card` ~281; recommendation coerced ~272
- **Private datum:** Requester's confidential 1:1 Personal Memory / prior preferences ("you mentioned loving natural wine", "you prefer slow evenings, not scenes") and individual hard constraints (diet/energy/budget), written by the LLM into `recommendation.why_for_person` / `why_for_group` with "chosen for YOU" attribution.
- **Leak path:** agent system prompt injects requester observations + hard_constraints (agent.py:839/841, not stripped when has_trip) → `_prompts_skills.py:1063` instructs LLM to populate `why_for_person` from Personal Memory → `post_venue_card` dispatched (tools.py:356) → `RecommendationPayload` clamp-only (content.py:272) → `create_venue_card` (structured_messages.py:614) → `create_message(message_type="venue_card", sender_type="agent")` into the group conversation read by all members.
- **Missing guard:** NONE on path. All canonical group-egress guards (`find_identity_leaks`, `find_constraint_leaks`, `_semantic_privacy_guard`, corpus `check_private_signal`) live inside `execute_compose_group_message` and only scan the agent's free-text REPLY. The venue card is a separate tool-emitted message; `strict_group_compose` only intercepts free text.
- **Reproduction:** GROUP conversation WITH a trip, members Maya (requester) + Tom. Maya's Personal Memory has "you prefer slow evenings, not scenes" + a hard constraint. Maya asks "where for dinner tonight?". Agent calls `post_venue_card(recommendation={"why_for_person": "you prefer slow evenings, not scenes — quiet neighbourhood spot, natural wine you mentioned loving"})`. Card writes `why_for_person` verbatim to the group conv; Tom reads Maya's confidential 1:1 memory. Only test is `test_recommendation_clamp.py` (length only).

---

### HIGH

#### 2. Proactive system prompt persisted verbatim to shared group conversation and served to all members
- **Severity:** high
- **Surface / file:line:** `proactive-group-turn-router` — `backend/concierge/session.py` `persist_user_message` 908-915 (`sender_type="system"`); entry `backend/concierge/triggers.py` `run_proactive_turn`
- **Private datum:** Member-attributed private constraints + identity of who-said-what (diet/budget/access), carried in `group_interjection` intent synthesized from `social_state_markdown`.
- **Leak path:** social_state genesis (per-member constraints + names) → `get_social_state.social_state_markdown` → `triage_group_interjection` → `InterjectionDecision.intent` → `ProactiveCandidate.prompt` (audience='group') → arbiter.dispatch_candidate → `run_proactive_turn` builds message → `session.send_message` → `_resolve_turn` → `persist_user_message(content=message, sender_type='system')` into SHARED group conv → `get_messages` (no sender_type filter) → GET /api/conversations/{id}/messages returns verbatim to every member.
- **Missing guard:** NONE. Compose guards run only on agent REPLY inside `handle_turn`; the inbound system prompt is persisted before any composer runs. Read-side `get_messages` does not filter `sender_type='system'`. Proactive turns also skip the input safe-scan (`is_proactive` bypass).
- **Reproduction:** Group trip ≥2 members; Maya stores dietary=vegetarian + budget-anxiety; Alex has mobility constraint. Genesis names them in social_state. Chat stalls 30+ min → arbiter ticks → Haiku triage → intent="Nudge toward a vegetarian-friendly spot that fits Maya's budget and keeps pace gentle for Alex". Persisted as system row; any member's GET /messages returns it verbatim.

#### 3. present_options reaction-card content/context bypasses all group-egress privacy guards
- **Severity:** high
- **Surface / file:line:** `present-options-reaction-card` — `backend/concierge/tool_handlers/planning/_propose_present.py` `_execute_present_options` ~519; `create_reaction_card` ~589
- **Private datum:** Any confidential 1:1 datum the model writes into free-text `content`/`context`: a hard constraint (no-stairs/wheelchair, $50/person ceiling, vegetarian/medical), a Personal Memory phrase, or who-said-what attribution.
- **Leak path:** agent loop dispatches `present_options` (tools.py:336) → `_execute_present_options` (only `_check_non_empty_str` + option-count validation) → `create_reaction_card(content, context, ...)` (line 589) → `create_message` raw insert into group conversation.
- **Missing guard:** NONE. Sibling `_execute_propose_change` calls `check_proposal_privacy` (line 353); `_execute_present_options` calls nothing. `compose_group_message`'s gate is off-path; `output_guards` only inspect the reply text, never card content.
- **Reproduction:** Group trip, Maya has wheelchair/no-stairs constraint. Agent calls `present_options(content="I picked the rooftop terrace so Maya doesn't have to deal with the stairs — wheelchair-friendly", context="Thursday dinner — for whoever wanted the step-free option", options=[...])`. All validations pass; card ships to every member.

#### 4. generate_trip_shapes posts LLM-authored card to group bypassing the compose guard
- **Severity:** high
- **Surface / file:line:** `trip-shapes-card` — `backend/concierge/tool_handlers/planning/_shapes.py` `create_trip_shapes_card` ~187 (known_preferences ingest ~38/96-97)
- **Private datum:** A member's confidential constraint (diet/budget/accessibility/energy/medical) or Personal-Memory narrative + who-said-what, surfaced in the LLM `best_for`/`pitch` fields.
- **Leak path:** agent holds member Personal Memory + hard constraints → fills free-text `known_preferences` (tools_schema.py:1091) → `_execute_generate_trip_shapes` folds it into temp-0.9 sub-LLM user_msg (~97/127), prompt demands `best_for`/`pitch` with no privacy instruction → normalized shapes → `create_trip_shapes_card` (structured_messages.py:77) → `create_message(message_type='reaction_card')` into group conv.
- **Missing guard:** NONE (only a soft prompt instruction in `_prompts_skills.py:75-107/408-410` for silent constraint handling — not deterministic, and absent from the second privacy-blind LLM). Sibling `check_proposal_privacy` not wired here.
- **Reproduction:** Group trip; Maya has budget €50 + vegetarian + knee injury. User: "4 days in Lisbon, 4 of us, surprise us." Agent calls `generate_trip_shapes(known_preferences="budget-friendly anchors (capped ~€50pp), vegetarian-forward food, relaxed pace for someone managing a knee injury")`. Sub-LLM emits best_for "keeping things gentle on the legs and easy on the wallet"; card ships to group.

#### 5. Cached Take headline/verdict (personal-tier) posted to group unguarded
- **Severity:** high
- **Surface / file:line:** `venue-card` — `backend/concierge/tool_handlers/content.py` personal take lookup ~246; take_headline/take_verdict ~257-260; create_venue_card ~286-287
- **Private datum:** Personal-tier Take prose (headline + verdict.opinion) generated under the requester's Personal Memory — can encode private constraints ("avoids loud rooms", dietary restriction).
- **Leak path:** `get_most_recent_personal_take(user_id=requester)` (content.py:246) → `take.payload.headline` / `verdict.opinion` (257-260) → `create_venue_card` → metadata_ + content_fallback (structured_messages.py:647-653) → all group members.
- **Missing guard:** NONE. Take selected by requester's user_id with no group-safe projection; bypasses `execute_compose_group_message`.
- **Reproduction:** A and B in group; A has "avoids loud rooms"/vegetarian; A has a personal Take for venue_42 ("Skip — the back room gets loud, and you've said that ruins a night"). A asks "what do you think of venue_42?" in group; agent calls `post_venue_card`; `get_most_recent_personal_take(A)` returns A's Take; verdict prose ships to B. Existing `test_post_venue_card.py:116` asserts the personal take wins (validates the leaking behavior).

#### 6. plan_ready card first_day_teaser leaks planner day_theme to group
- **Severity:** high
- **Surface / file:line:** `plan-ready-card` — `backend/concierge/tool_handlers/planning/_plan.py` create_plan_ready_card ~1002; `_teaser` 991-994; structured_messages.py first_day_teaser 484-485
- **Private datum:** A member's constraint or personal-memory narrative (diet/accessibility/energy/mood) or who-said-what, by implication inside the day-1 theme.
- **Leak path:** `_build_planner_personas` adds personal_memory + private_constraints (_plan.py:84-111) → planner LLM → `day_themes[1]` → `_teaser` (_plan.py:991) → `create_plan_ready_card(first_day_teaser=_teaser)` → metadata + content → `create_message` into group conv.
- **Missing guard:** NONE. `_scan_planner_output` is a prompt-injection redactor that scans only raw_plan/group_facing_message and runs AFTER the card is posted.
- **Reproduction:** Group trip, pre_trip/active_planning; member A has accessibility/energy in Personal Memory. User: "plan our first few days." Planner emits `day_themes[1]`="Gentle step-free wanderings"; teaser shipped to group card, disclosing A's accessibility by implication.

#### 7. Taste-DNA reflection card writes a user's private budget/energy/social phrases into the shared GROUP conversation
- **Severity:** high
- **Surface / file:line:** `taste-dna-reflection-card` — `backend/concierge/first_contact.py` `post_dna_reflection_card_if_eligible` ~350-353
- **Private datum:** One user's private taste_dimensions phrases from their 1:1 Personal Memory — budget rendered as "stretches every dollar"/"pays for the unforgettable", energy/social phrases, self-attributed.
- **Leak path:** chat.py:403 `_turn_then_dna_followup` → `post_dna_reflection_card_if_eligible(actor.id, session.conversation_id, trip_id)` → `get_latest_personal_memory.taste_dimensions` → `_build_reflection_phrases` → `create_taste_dna_reflection_card(conversation_id, phrases)` → `create_message`. `conversation_id` resolves to `conversation_type='group'` (shared trip thread).
- **Missing guard:** NONE. `execute_compose_group_message` never invoked; `create_message` is a raw insert. `strict_group_compose` only intercepts in-turn free text; this is a fire-and-forget structured write.
- **Reproduction:** Group trip (Maya + Sam); Sam has budget {label:"Thrifty"} + energy + social each ≥3 evidence; no prior taste_dna_reflection observation. Sam sends any message via POST messages/stream; post-turn hook fires; card inserted into the GROUP conv with content "Here's what I've picked up about how you travel so far: ...; stretches every dollar." Maya sees Sam's Thrifty posture.

#### 8. Haiku-derived interjection intent/reason persisted as group-visible system message
- **Severity:** high
- **Surface / file:line:** `group-interjection-triage-reason` — `backend/concierge/triggers.py` 150-175; persisted `session.py:908-912`; read `_messages.py:321-357` + `conversations.py:480-527`
- **Private datum:** Per-member constraints, engagement patterns, who-said/prefers attribution lifted by Haiku from raw transcript + member names + raw `social_state_markdown` (incl. Tensions/Optimization Targets).
- **Leak path:** `triage_group_interjection` builds prompt from raw transcript + RAW social_state (NO `strip_private_group_sections`) → Haiku → `decision.intent/reason` → `ProactiveCandidate(prompt, reason)` → arbiter → `run_proactive_turn` → `session.send_message(system)` → persisted verbatim → `get_messages` (unfiltered) → GET endpoints return to every member.
- **Missing guard:** NONE. `get_social_state` does not strip; `_load_context` does not call `strip_private_group_sections`; arbiter does not redact; read endpoint has no system-row filter.
- **Reproduction:** Trip ≥2 members; social state has "## Optimization Targets: Keep the pace gentle for Maya (mobility)" + "## Tensions: Sam pushing rooftop bars, Maya disengaging on cost". Idle group thread >10 min → triage interjects → intent names Sam's preference + Maya's mobility/cost. Persisted as system row; any member GET /messages reads it.

#### 9. present_options reaction-card content/context/labels reach group thread with no privacy guard (dup-id second trace)
- **Severity:** high
- **Surface / file:line:** `present-options-reaction-card` — `_propose_present.py` `_execute_present_options` 519-609 (egress at `create_reaction_card` 589)
- **Private datum:** Confidential 1:1 datum the concierge writes into content/options[].label/context: dietary/accessibility/budget/energy constraint, personal-memory phrase, or who-said-what.
- **Leak path:** agent emits `present_options` → tools.py:336-337 → `_execute_present_options` (non-empty content + 2-5 options only) → `create_reaction_card` (589) → `create_message(message_type='reaction_card')` into group conv.
- **Missing guard:** NONE. `check_proposal_privacy` (wired into sibling at line 353) absent; `strict_group_compose` only intercepts free text; `output_guards` scan reply only.
- **Reproduction:** Group trip, Maya has knee/gluten constraint. Agent calls `present_options(content="Found a step-free spot with no stairs for the knee issue", context="Thursday dinner (gluten-free, step-free)", options=[...])`. All validations pass; card ships.

#### 10. Private Personal-Memory taste prose in prompt_for_agent persisted as system message and served to every group member
- **Severity:** high
- **Surface / file:line:** `triage-prompt-for-agent` — `backend/notifications/triage.py` `run_triage`/`TriageNotification.prompt_for_agent`; persisted `session.py:908-915`
- **Private datum:** A member's confidential 1:1 Personal Memory "Who They Are" taste prose, keyed by display name ("Maya: drawn to underground techno and natural-wine bars, avoids touristy spots").
- **Leak path:** lifecycle `get_latest_personal_memories_batch` → `extract_taste_snippet` → `taste_summaries` → `run_triage` → Haiku emits `TriageNotification(target='group', prompt_for_agent=<taste prose>)` → `candidates_from_triage` (arbiter.py:875) → arbitrate → `run_proactive_turn` (group session) → `session.send_message(system)` → `persist_user_message(system)` → GET /messages returns verbatim.
- **Missing guard:** NONE. Compose guards run only on agent reply; the private-routing mitigation (triggers.py:76-84) fires only for `target_audience=='private'`; a Haiku misclassification (target='group') leaks the named taste profile.
- **Reproduction:** Trip Maya + Sam; Maya's PM "Drawn to underground techno and natural-wine bars; avoids touristy spots." Triage runs with upcoming techno event; Haiku mislabels target="group", `prompt_for_agent="...it's exactly Maya's scene: she's drawn to underground techno and natural-wine bars."` Routed to group session, persisted as system row; Sam's GET /messages returns Maya's named taste prose.

#### 11. Group-interjection intent persisted as raw system message, served verbatim to all members (dup-id triage-reason variant)
- **Severity:** high
- **Surface / file:line:** `interjection-group-candidate` — `backend/concierge/triggers.py` 160-163; persisted `session.py:908-915`
- **Private datum:** Inferred member dynamics + an individual's constraint + who-said-it; `decision.intent` from `social_state_markdown` (per-member dietary/accessibility/budget/fatigue with attribution per genesis.py:266-278) + member roster.
- **Leak path:** `triage_group_interjection` → Haiku reads social_state + roster → `InterjectionDecision.intent` → `ProactiveCandidate(prompt, audience='group')` → dispatch → `run_proactive_turn` (group conv, private_uid None) → `session.send_message(system)` → persisted → GET endpoints (no sender_type filter) return to every member.
- **Missing guard:** NONE. Inbound proactive system message persisted directly; compose stack runs on reply only.
- **Reproduction:** Trip Maya (vegetarian, hard constraint from 1:1) + Sam. Group chat idles on restaurants; triage returns target="group", intent="Maya keeps steering away from the steakhouse because the vegetarian options are thin — propose a compromise venue." Persisted as system row; Sam reads Maya's private dietary constraint + resistance inference.

#### 12. Vote comment in votes dict leaks private constraint + who-said-it to whole group via proposal detail
- **Severity:** high
- **Surface / file:line:** `proposal-detail-readout` — `backend/api/routes/proposals.py` `_to_detail` line 891 (`votes=proposal.votes`); source `change_proposals.py:543-545`
- **Private datum:** A constraint (diet/budget/accessibility/fatigue) + identity of who-said-it. Vote comments are free text keyed by voting member's user_id.
- **Leak path:** POST /vote (`VoteRequest.comment`) → `vote_on_proposal` stores comment verbatim into votes JSONB (543-545, no privacy call) → GET /proposals/{id} → `_to_detail` (891) → `ProposalDetail.votes` returned to every `require_trip_member`.
- **Missing guard:** NONE. `check_proposal_privacy` scans only title/description/impact/alternatives; `resolution_note` is scrubbed via `redact_private_signal` at resolve — but the structurally identical vote comment has no equivalent.
- **Reproduction:** Trip Alice/Bob/Carol; Bob creates proposal P. Carol POSTs vote {comment:"we can't, it's not wheelchair accessible and Sarah needs step-free access"}. Stored verbatim; Bob GET /proposals/P reads Carol's accessibility constraint attributed to her user_id.

#### 13. Feasibility-catch reschedule proposals reach the group home feed without check_proposal_privacy
- **Severity:** medium → (high private_data class)
- **Surface / file:line:** `home-concierge-feed-proposal-card` — `backend/concierge/proactive.py` 904 (`create_change_proposal` inside `_produce_feasibility_catch`); feed `concierge_feed.py` ~941/2678
- **Private datum:** Private datum in an itinerary block title (`moved.title`/`other.title`) — e.g. "Wheelchair PT", an accessibility/medical constraint and who-it-belongs-to.
- **Leak path:** block title (user-editable) → `_produce_feasibility_catch` builds title/description/impact → RAW `create_change_proposal` (904, NO gate) → `get_proposals_for_trips` → `_catch_reschedule_card` renders moved_title/other_title into body/title/chips/stakes → every member's home feed.
- **Missing guard:** NONE. `check_proposal_privacy` runs only inside `build_and_persist_proposal` (change_proposals.py:275) and the tool path; this producer calls raw `create_change_proposal`.
- **Reproduction:** Multi-member trip; member A renames block "Wheelchair PT". Two same-day blocks geo-close → feasibility catch → `_produce_feasibility_catch` builds proposal.title="Move Wheelchair PT to 14:30", impact moved_title="Wheelchair PT", raw create. Every member's home Catch card reads it.

#### 14. Group-profile private reasoning sections feed daily-digest LLM unstripped, then surface on shared home card
- **Severity:** high
- **Surface / file:line:** `daily-digest-content` — `backend/digest/engine/daily.py` 75-76 (`gp.markdown_content[:600]`) → 124 → `llm_calls.py:42-44`
- **Private datum:** Agent-only group reasoning (Tensions & Trade-offs / Optimization Targets) — inter-member tensions, trade-offs, optimization targets.
- **Leak path:** `get_latest_group_profile.markdown_content[:600]` (daily.py:74-76) → `inputs.group_context` → `_call_daily_digest` prepends as "### Group Profile" (llm_calls.py:42-44) → Haiku → day_arc/forward_signals → `upsert_digest` → `_digest_to_card`/`_digest_subtitle` (cards.py:216-261) → morning_brief card to every member.
- **Missing guard:** NONE. `strip_private_group_sections` never called on the digest path; digest engine has zero privacy imports.
- **Reproduction:** Multi-member in-progress trip whose latest group profile has "## Tensions & Trade-offs" content within first 600 chars (compact profiles). Nightly digest reflects friction into `day_arc.group_cohesion`; next-day morning_brief card surfaces it to all members.

#### 15. Per-user observations (constraints, named attribution) reach the shared digest card with no guard
- **Severity:** critical
- **Surface / file:line:** `daily-digest-content` — `backend/digest/engine/_shared.py` 269-284 (obs query, no shared/user filter) → `formatters.py:117-125`
- **Private datum:** Confidential per-user observation content with category (dietary/budget/accessibility/fatigue/medical) and free-text naming who has the constraint ("[dietary] Priya can only eat vegetarian").
- **Leak path:** `_gather_day_inputs` selects observations across ALL members (no `shared`/user filter, is_active only) → `_format_observations` raw → P_DAILY_DIGEST_USER → Haiku → day_arc.turning_point/forward_signals → `_digest_subtitle` → morning_brief card to all members.
- **Missing guard:** NONE. Sanctioned reader `get_shared_observations_for_trip` gates on `shared.is_(True)`; the digest query ignores `shared` entirely. No constraint/identity/semantic guard on path.
- **Reproduction:** Trip Priya/Tom/viewer; agent records `agent_observe(target_user_id=Priya, category="dietary", content="Priya can only eat vegetarian and gets anxious at loud places")` or any `shared=False` observation. Nightly digest pulls it (no shared filter); Haiku writes "Finding a vegetarian spot Priya could eat at reset the group's mood" into turning_point; surfaced to all members.

#### 16. Who-said-what attribution from per-member messages surfaces in shared digest card without find_identity_leaks
- **Severity:** high
- **Surface / file:line:** `daily-digest-content` — `backend/digest/engine/formatters.py` 65-80 (`_format_messages`, sender = metadata_['user_name'])
- **Private datum:** Identity of who-said-what; each message line is labeled with the member's display name tied to its content.
- **Leak path:** `_gather_day_inputs` pulls all trip messages → `_format_messages` labels each line with user_name → P_DAILY_DIGEST_USER → Haiku → group_cohesion/turning_point → `_digest_subtitle` → shared morning_brief.
- **Missing guard:** NONE. `find_identity_leaks` never runs in the digest engine or card renderer.
- **Reproduction:** Trip Maya/Alex; Maya posts "I'm completely exhausted, I can't do another museum, my back is killing me." Digest emits day_arc.turning_point "Maya was visibly drained after the museum and asked to slow the pace." morning_brief subtitle surfaces named fatigue/health complaint to all.

#### 17. Group-profile private reasoning sections feed daily-digest LLM, surface on shared home card (concierge_feed variant)
- **Severity:** high
- **Surface / file:line:** `digest-to-home-card` — `backend/digest/engine/daily.py` 75-76 → `llm_calls.py:43-49`
- **Private datum:** Per-member friction/identity attribution in the agent-only group-profile sections — who wants slower pace, whose budget binds, intra-group tension.
- **Leak path:** `get_latest_group_profile.markdown_content` → daily.py:76 group_context (NO strip) → `_call_daily_digest` group_section → Haiku → group_cohesion/turning_point → `_digest_to_card`/`_digest_subtitle` (cards.py:233) → ConciergeHomeCard to every member.
- **Missing guard:** NONE. `strip_private_group_sections` not on path.
- **Reproduction:** 3-member active trip; profile "## Tensions & Trade-offs: One traveler wants museum-dense days while another finds them draining... budget-conscious member will quietly resist premium menus." Haiku → group_cohesion "Pacing tension... budget sensitivity shaping dinner choices." Rendered on shared morning_brief to all.

#### 18. Day observations flow verbatim into daily-digest LLM and out through shared card subtitle with no constraint guard
- **Severity:** high
- **Surface / file:line:** `digest-to-home-card` — `backend/digest/engine/formatters.py` 117-125 (`_format_observations`: raw o.content); consumed `llm_calls.py:54`
- **Private datum:** Confidential 1:1 constraint/preference observations (dietary, budget ceiling, accessibility/fatigue, medical), incl. `shared=False` rows.
- **Leak path:** observations table → `_gather_day_inputs` day_observations (no shared filter) → `_format_observations` raw → P_DAILY_DIGEST_USER → Haiku → forward_signals/day_arc → `_digest_subtitle` (cards.py:236-240) → shared card for all members.
- **Missing guard:** NONE. On the sanctioned path constraints are routed through `_aggregate_constraints` + re-scanned by `find_constraint_leaks`; the digest applies neither; gathers private (shared=False) rows.
- **Reproduction:** Trip A/B; A has private `create_observation(category="general", content="A is hiding a $400 hard budget ceiling", shared=False)`. Digest pulls it (no shared filter); Haiku → forward_signals[0] "watch the budget ceiling around the group dinner"; B's home card surfaces it.

#### 19. Per-member message content with display names feeds digest LLM, enabling who-said-what attribution in shared subtitle
- **Severity:** medium → (identity class)
- **Surface / file:line:** `digest-to-home-card` — `backend/digest/engine/formatters.py` 65-80 (`_format_messages`)
- **Private datum:** Identity-of-who-said-it; each conversation line labeled with member display name.
- **Leak path:** messages_table → `_format_messages` stamps user_name → daily digest LLM → day_arc.group_cohesion/turning_point → `_digest_subtitle` → shared ConciergeHomeCard to every member.
- **Missing guard:** NONE. `find_identity_leaks` never runs on digest content.
- **Reproduction:** 3-member trip; Maya posts "I'm honestly exhausted and don't think I can do the late dinner." Digest → turning_point "The evening fractured when Maya pulled out of the group dinner, drained." morning_brief subtitle to whole group.

#### 20. Organizer-authored invitee_note ships verbatim to external non-member over SMS/email
- **Severity:** high
- **Surface / file:line:** `invite-dispatch-sms` (audience: public) — `backend/notifications/invite_dispatch.py` `_compose_body` 244-245
- **Private datum:** Another member's confidential constraint (diet/budget/access/energy), personal-memory detail, or who-said-what that the organizer types into the free-text `invitee_note`.
- **Leak path:** POST /invites `InviteCreateRequest.invitee_note` (no validation) → `create_invite` (stored verbatim) → `dispatch_invite` (fire-and-forget) → `_compose_body` → `body = f"{who}: {invitee_note}\n{url}"` → Twilio/email → external prospective invitee.
- **Missing guard:** NONE. Never routes through `execute_compose_group_message`; `check_proposal_privacy` not wired; `redact_private_signal` never called. Only `html.escape` on the email path (XSS hygiene). Sibling `state_updater.py:96-98` DOES call `redact_private_signal`.
- **Reproduction:** Organizer POSTs /invites {contact_channel:"sms", contact_value:"+15551234567", invitee_note:"Maya's vegan and her budget is only $50/day... keeping it gentle pace for Tom's knee too"}. Note stored verbatim; Twilio sends the exact body to a non-member's handset.

#### 21. Actor-authored free-text note/curator_hook leaks to followers via Discover friends feed with no privacy scan
- **Severity:** high
- **Surface / file:line:** `discover-feed-friends-section` (cross-user) — `backend/discover/compose.py` 509 (`hook=ctx.get("curator_hook") or ctx.get("note")`); 516 (`meta_text=ev.display_name`)
- **Private datum:** Any confidential datum the actor types into an event context note: dietary/budget/accessibility/energy constraint, personal-memory phrase, or who-said-what, rendered as the friend-card hook attributed by display_name.
- **Leak path:** POST /api/events `EventCreate.context` (actor-controlled) → `create_user_event` writes context verbatim → `get_social_feed` SELECTs context across follow graph → `compose_discover_feed` friends loop reads `ctx.get('note')` into hook + display_name into meta_text → GET /api/discover/feed to follower B.
- **Missing guard:** NONE on write→read→egress. `find_identity_leaks`/`find_constraint_leaks`/`_semantic_privacy_guard` scoped to group-compose; `check_private_signal`/`redact_private_signal` never invoked in discover/follows/events/saves. (Note: the saves.py path stores only `{"source": ...}`; the live trigger is the direct POST /api/events context dict.)
- **Reproduction:** As user A (followed by B), POST /api/events {event_type:"venue_saved", context:{"note":"Booking on my $50/day ceiling and Maya is vegan + can't do stairs"}}. B's GET /discover/feed shows hook=that note, meta_text=A's display_name.

#### 22. hero_title bypasses check_private_signal + name redaction, ships verbatim to public story page + crawlers
- **Severity:** high
- **Surface / file:line:** `story-landing-html` (public) — `backend/core/story_projection.py` 167 (`hero_title=story.hero_title`) vs 125-143
- **Private datum:** A traveler constraint or a non-owner co-traveler identity embedded in the LLM-composed hero_title ("The gluten-free Lisbon week", "Recovering Maya's knee in Kyoto").
- **Leak path:** trip_story composer (observations + co-traveler context) → hero_title (trip_story.py:478) → trip_stories.hero_title → `get_public_story_by_slug` → `build_public_story_payload` copies hero_title verbatim (167, NO check_private_signal/_names_present) → `story_landing` (story_landing.py:119) → <title>/og:title/twitter:title/<h1> on noauth /stories/{slug}.
- **Missing guard:** NONE. Sections (130-133) and hero_subtitle (138-143) run check_private_signal + _names_present; hero_title is deliberately exempt (comment 137-138). Owner preview is advisory only.
- **Reproduction:** Owner has high-importance observation "Kept every meal strictly gluten-free." Composer emits hero_title="The Gluten-Free Lisbon Week"; stored verbatim; link share; crawler fetches /stories/{slug}; title rendered with only html.escape. Test `test_story_projection.py:111` asserts a CLEAN title survives (no constraint test).

#### 23. hero_title bypasses check_private_signal and _names_present → constraint/co-traveler name reaches public JSON
- **Severity:** high
- **Surface / file:line:** `story-public-json` (public) — `backend/core/story_projection.py` 167 vs 138-143
- **Private datum:** A dietary/accessibility/fatigue constraint or non-owner member identity in the story title.
- **Leak path:** `compose_trip_story` composes hero_title from overall_arc + `get_active_observations` → trip_stories.hero_title → `get_public_story_by_slug` → `build_public_story_payload(hero_title=story.hero_title)` (no scan) → `public_story_json` GET /api/public/stories/{slug}.
- **Missing guard:** NONE. Same hero_title exemption; owner preview has no hero_title flag.
- **Reproduction:** Owner Ana + co-traveler Maya (redact_names={"Maya"}), private accessibility constraint. Composer emits hero_title="Maya's Step-Free Birthday in Lisbon"; GET /api/public/stories/{slug} returns it raw; identical phrase in a section/subtitle would have been dropped. Test `test_hero_subtitle_with_constraint_vocab_is_blanked` enshrines the leak.

#### 24. Public story section/hero leaks dietary & medical constraints outside the keyword regex (corpus layer never run)
- **Severity:** medium
- **Surface / file:line:** `build-public-story-payload` (public) — `backend/core/story_projection.py` 131 (sections) and 139-142 (hero_subtitle): `check_private_signal` called with NO private_corpus
- **Private datum:** A dietary/medical constraint phrased outside the fixed lexical list — "vegetarian", "celiac-safe", "diabetic-friendly", "low-sodium", "pescatarian" (not in `_PRIVATE_KEYWORD_PATTERNS`).
- **Leak path:** `compose_trip_story` (observations + overall_arc) → LLM → `TripStory.sections[].body`/hero_subtitle → `get_public_story_by_slug` → `build_public_story_payload` → `check_private_signal(body)` with keyword_layer=True but NO private_corpus → PublicTripStory → public landing/json/card png/plan-seed.
- **Missing guard:** Corpus layer of `check_private_signal` (verbatim match vs `load_private_corpus_for_trip`) is never invoked here — only the finite keyword regex + name match run. The keyword_layer=False asymmetry note applies to the GROUP composer, not this public path.
- **Reproduction:** Owner observation "Kept it vegetarian the whole trip and hunted for celiac-safe bakeries." Composer body "You kept it vegetarian... celiac-safe bakery." check_private_signal (no corpus) doesn't match "vegetarian"/"celiac"; section survives; GET /api/public/stories/{slug} renders it. Tests only use regex-matching terms ("wheelchair"/"gluten-free").

#### 25. Unredacted story hero_title leaks constraint / personal-memory / co-traveler signal to public login-free plan-seed
- **Severity:** high
- **Surface / file:line:** `plan-seed-public` (public) — `backend/core/story_projection.py` 167 → 232,249 (`build_plan_seed`)
- **Private datum:** A traveler constraint or co-traveler identity in hero_title ("The No-Gluten Lisbon Trip", "Lisbon on $40 a Day", "Maya's Birthday in Porto").
- **Leak path:** `compose_trip_story` (raw observations + overall_arc → hero_title, stored verbatim) → `get_public_story_by_slug` → `build_public_story_payload` (hero_title unscrubbed, 167) → `build_plan_seed` weaves into planning_brief (232) + inspiration_hero_title (249) → `get_plan_seed_by_slug` → `public_plan_seed` GET /api/public/stories/{slug}/plan-seed (noauth).
- **Missing guard:** NONE. hero_title exemption; no compose-time scrub; redact_names populated for sections/subtitle but not hero_title.
- **Reproduction:** Trip owner Sam + member Maya; arc beat "Maya's birthday dinner." Composer hero_title="Maya's Birthday in Porto." Attacker GET /plan-seed: inspiration_hero_title="Maya's Birthday in Porto", planning_brief embeds it. redact_names would have stripped "Maya" on sections.

#### 26. Composer-generated hero_title reaches followers' feed without check_private_signal
- **Severity:** high
- **Surface / file:line:** `story-published-feed-event` (cross-user) — `backend/core/db/trip_story_shares.py` 316 (`context["hero_title"]=public.hero_title`); root `story_projection.py:166-167`
- **Private datum:** A constraint or medical/identity datum in the LLM-composed hero_title ("A gentler pace through Kyoto after my knee", "Lisbon, recovering").
- **Leak path:** `create_trip_story(hero_title=<LLM from observations>)` → trip_stories.hero_title → `emit_story_published_if_visible` (309 → `build_public_story_payload` returns hero_title unredacted at 167) → `context["hero_title"]` (316) → `create_user_event("story_published")` → `follows.get_feed` reads context for every follower → cross-user feed.
- **Missing guard:** NONE. Fires on every share create/PATCH regardless of whether the owner opened the Privacy Preview; pushes hero_title to followers who never consented to a link.
- **Reproduction:** Owner observation "Navigated Kyoto gently after the knee surgery." Composer hero_title="A Gentler Pace Through Kyoto After My Knee." Owner shares (followers_visible=True). Follower GET /api/users/{own_id}/feed returns FeedItem with context.hero_title intact. `test_hero_subtitle_with_constraint_vocab_is_blanked` asserts hero_title passes through.

#### 27. hero_title bypasses public-story projection (check_private_signal + redact_names) on the profile aggregation path
- **Severity:** high
- **Surface / file:line:** `profile-public-stories-list` (cross-user) — `backend/core/db/trip_story_shares.py` `list_public_stories_for_user` 400-442 (raw select hero_title → PublicProfileStory at 437)
- **Private datum:** A constraint phrase or co-traveler identity in the composer-authored hero_title ("The Gluten-Free Grand Tour", "The Sober Lisbon Weekend", "Maya's Birthday Escape").
- **Leak path:** trip_stories.hero_title (composer) → stored raw → `list_public_stories_for_user` SELECTs it directly (412) → `PublicProfileStory(hero_title=row['hero_title'])` (437) → `profiles.py _build_profile` stories (67) → GET /api/users/{user_id}/profile, viewable by ANY user.
- **Missing guard:** NONE. Raw SQL read, no `build_public_story_payload` projection, no check_private_signal, no redact_names, no preview gate. Sibling slug path wires `redact_names=_non_owner_member_names`.
- **Reproduction:** Owner A + Maya, gluten-free constraint; composer hero_title="Maya's Gluten-Free Grand Tour"; share visibility "link"; A public_profile_enabled. Any user B GET /api/users/{A}/profile → stories[0].hero_title leaks Maya identity + dietary constraint. Tests use only a clean title.

#### 28. destination ignores RedactionPolicy.show_destination on the profile aggregation path
- **Severity:** medium
- **Surface / file:line:** `profile-public-stories-list` (cross-user) — `backend/core/db/trip_story_shares.py` `list_public_stories_for_user` 422-438 (WHERE omits redaction_policy; destination=row['place_name'] or row['trip_title'])
- **Private datum:** The trip destination the share owner explicitly chose to HIDE via `RedactionPolicy.show_destination=False` (rehab/medical destination, partner's home city); also user-authored `trips.title` fallback.
- **Leak path:** `trip_story_shares.redaction_policy` (set via `update_share_settings`) NOT read by `list_public_stories_for_user` → SELECT places.name/trips.title → destination unconditionally (438) → PublicProfileStory.destination → GET /api/users/{user_id}/profile.
- **Missing guard:** NONE. Slug path emits destination only when `policy.show_destination`; profile-list query never joins redaction_policy.
- **Reproduction:** Owner A creates share with `update_share_settings(redaction_policy=RedactionPolicy(show_destination=False))`, public_profile_enabled. Slug card hides destination; any user B GET /api/users/{A}/profile returns destination = "Cirque Lodge, Sundance UT" (or trip_title). No test covers `list_public_stories_for_user`.

#### 29. LLM-generated DNA phrase echoes a confidential constraint verbatim into the public Unpacked card PNG
- **Severity:** high
- **Surface / file:line:** `atlas-unpacked-render-card` (public) — `backend/core/story_card.py` `render_unpacked_card` 369 (`dna = you_card.title`) → 414-415
- **Private datum:** A confidential constraint (dietary gluten-free/celiac, accessibility step-free, allergy) from the user's Personal Memory narrative. (Budget figures are abstracted by synthesis; dietary/accessibility/allergy land verbatim.)
- **Leak path:** `refresh_personal_memory` → `_generate_dna_phrases(taste_dims, narrative[:1200])` ("use the actual details from the narrative") → cached `taste_dims['reflection_phrases']` (refresh_memory.py:545, no redaction) → `build_unpacked` → `_build_reflection_phrases` cached branch returns verbatim (me.py:136-138) → you_card.title → `render_unpacked_card` paints into PNG → noauth GET /unpacked/{token}/card.png + og:image.
- **Missing guard:** Partial only — synthesis `[private]`-abstraction (refresh_memory.py:113-126) is LLM-side fail-open and explicitly exempts absolute-severity constraints (allergy/accessibility). No canonical guard on path.
- **Reproduction:** User logs celiac/gluten-free or step-free constraint; synthesis writes it verbatim; `_generate_dna_phrases` emits "always finds the gluten-free table locals trust"; cached; user shares Unpacked; anyone with link (or crawler fetching og:image) hits /unpacked/{token}/card.png and sees the constraint.

#### 30. Cached LLM-generated DNA phrase leaks personal-memory constraints onto public Atlas Unpacked card (no check_private_signal)
- **Severity:** high
- **Surface / file:line:** `atlas-unpacked-builder` (public) — `backend/atlas/unpacked.py` 120-122, 147-148; emitted `atlas_unpacked_landing.py:97-101` + `story_card.py:369,410-416`
- **Private datum:** A confidential constraint (sobriety, accessibility, medical low-anxiety, budget ceiling) the DNA-phrase LLM lifted from the raw Personal Memory narrative.
- **Leak path:** `refresh_personal_memory` → `_generate_dna_phrases` → cached `reflection_phrases` (no scrub) → `build_unpacked`: dna_phrases = `_build_reflection_phrases(dims)` cached branch verbatim → dna_line → `AtlasUnpackedCard(kind='you', title=dna_line)` → noauth GET /unpacked/{token} (dna_html) AND /card.png.
- **Missing guard:** NONE. Sibling public surface `profiles.py:_public_safe` runs `check_private_signal` on these exact cached reflection_phrases; the Atlas Unpacked path applies none.
- **Reproduction:** PM narrative includes sober/wheelchair note; `_generate_dna_phrases` emits "travels sober, always finds the alcohol-free table"; cached; user creates share; unauthenticated GET /unpacked/{token} renders it in the page lede + og:image card.png. Fix: run `check_private_signal`/`_public_safe` on dna_phrases in `build_unpacked`.

#### 31. interests_strong-derived DNA phrase can carry a constraint label to the public Unpacked card unfiltered
- **Severity:** medium
- **Surface / file:line:** `atlas-unpacked-builder` (public) — `backend/api/routes/users/me.py` 165-170 ("drawn to {i0} and {i1}"); consumed `backend/atlas/unpacked.py:121`
- **Private datum:** A constraint-shaped interest token LLM-extracted from raw Personal Memory into `interests_strong` ("sober travel", "wheelchair-accessible venues", "low-anxiety spaces").
- **Leak path:** refresh memory → `taste_dimensions['interests_strong']` (un-curated) → `build_unpacked` → `_build_reflection_phrases` derived branch builds "drawn to {interests[0]} and {interests[1]}" → dna_phrases[0] → `AtlasUnpackedCard(kind='you')` → public /unpacked/{token} + /card.png.
- **Missing guard:** NONE. `profiles.py` guards interests_strong with `_public_safe(check_private_signal)`; the Unpacked builder applies no filter. `check_private_signal` would match "wheelchair"/"anxiety"/"sober".
- **Reproduction:** PM has "wheelchair-accessible venues" in interests_strong; derived branch → dna_phrases[0]="drawn to wheelchair-accessible venues and coastal towns"; public GET /unpacked/{token} renders it in lede + og:image. Tests mock `_build_reflection_phrases` (stub path). Fix: route both branches through check_private_signal.

#### 32. Restaurant venue-brief constraint values (incl. severe allergies) posted into group trip thread without small-group anonymization
- **Severity:** high
- **Surface / file:line:** `booking-confirmation-receipt` — `backend/booking_agent/db/restaurant_writeback.py` `_post_receipt` L124-142; `get_or_create_trip_conversation` L129
- **Private datum:** Per-member severe dietary allergies and accessibility requirements ("shellfish allergy", "limited mobility"). In a 2-person trip the de-attributed value still identifies the holder.
- **Leak path:** `traveler_profiles.severe_allergies`/`accessibility_requirements` → `_load_trip_preferences_sync` unions ALL members (booking_crud.py:1170-1215) → `build_venue_brief` → `venue_brief_provider_text` "Dietary needs: ...; Accessibility: ..." → `_build_special_requests` → `confirmation_details['venue_brief_shared_text']` → `_post_receipt` → `create_booking_confirmation_receipt(group conv, agent)` → metadata → "Shared with restaurant" receipt to ALL members.
- **Missing guard:** Brief runs `redact_private_signal`/`redact_corpus_phrases` + `_strip_named_subject`, but the canonical small-group anonymizer `_aggregate_constraints` (member_count<=2 → value-free counts) is MISSING. No member-count check anywhere in venue_brief.py or the receipt path. `redact_corpus_phrases` deliberately skips keyword patterns and only removes verbatim corpus phrases ≥8 chars, so a value not present verbatim in personal_memories passes.
- **Reproduction:** 2-member trip; A's `severe_allergies=['shellfish allergy']`, not verbatim in A's personal_memories (corpus empty/different phrasing). A initiates a restaurant booking; brief → "Dietary needs: shellfish allergy"; receipt posted to group conv; B (only other member) sees A's medical constraint uniquely identified.

#### 33. Reasoning-span plan text persists model scratchpad over Personal Memory + hard_constraints with no redaction
- **Severity:** high
- **Surface / file:line:** `concierge-reasoning-spans-plan` (logs-telemetry) — `backend/concierge/telemetry.py` `_insert_reasoning_spans` 300-321, plan field 315
- **Private datum:** Confidential 1:1 data: hard_constraint values (diet/accessibility/budget/energy), Personal Memory narrative, who-said-what — restated verbatim in the model's free-text plan.
- **Leak path:** personal_memories + `get_active_constraints_batch` → `assemble_system_prompt` (HARD_CONSTRAINTS_TEMPLATE, prompts.py:330) → LLM → text blocks → `_build_iteration_span` plan_text (agent.py:766-786) → result.reasoning_spans → session.py:696 `persist_reasoning_spans` → `_insert_reasoning_spans` → concierge_reasoning_spans.plan (`_truncate` only).
- **Missing guard:** NONE. `telemetry_redactor.redact` is wired ONLY on the concierge_turns path (telemetry.py:239-242); the reasoning-spans insert applies only `_truncate`.
- **Reproduction:** Member stores accessibility="wheelchair user, cannot manage stairs". User asks "find us a dinner spot." Model emits text "Since one traveler is a wheelchair user who cannot manage stairs, I'll filter for step-free venues..." → plan_text → concierge_reasoning_spans.plan unredacted.

#### 34. Reasoning-span observation field persists raw tool-result snippets with no redaction
- **Severity:** high
- **Surface / file:line:** `concierge-reasoning-spans-plan` (logs-telemetry) — `backend/concierge/agent.py` `_on_tool_result` span patch 1498-1505; insert `telemetry.py:317`
- **Private datum:** Tool observation snippets (result_str[:2000]) — e.g. `whereabouts` returns per-member {user_id, display_name, freshness, minutes_ago, km_from_me} (who-is-where attribution).
- **Leak path:** private tool result → `_on_tool_result` result_str (agent.py:1483-1504) → `span['observation'] = '[tool] ' + snippet` → result.reasoning_spans → `persist_reasoning_spans` → `_insert_reasoning_spans` → concierge_reasoning_spans.observation (`_truncate` only).
- **Missing guard:** NONE. observation field never passed through `telemetry_redactor.redact` or any privacy detector.
- **Reproduction:** Trip ≥2 members with last_location; user asks "who's nearby?"; agent invokes `whereabouts(include_group=true)`; returns Maya's name+user_id+distance+minutes_ago; `_on_tool_result` writes span['observation']; persisted verbatim to the warehouse.

#### 35. tool_calls[].input persists verbatim private fact values and constraint-derived queries to operator dashboard
- **Severity:** high
- **Surface / file:line:** `concierge-turns-tool-calls` (logs-telemetry) — `backend/concierge/telemetry.py` `_normalize_tool_call` 187-203 (input passthrough 196-197; insert 259)
- **Private datum:** (1) `fact_remember` inputs {key, value} where value is the raw private fact ("severe nut allergy", "$50/night ceiling"), incl. visibility='private'; (2) agent-composed search queries derived from a user's private constraints ("wheelchair accessible vegan spot under $30").
- **Leak path:** turn → `ConciergeSession.persist` passes `result.tool_calls_made` → telemetry.persist_turn → `_insert_turn` → `_normalize_tool_call` keeps input unchanged (196-197) → tool_calls JSONB insert (259). `redact()` applied only to user_message/reply (241-242).
- **Missing guard:** NONE. `_normalize_tool_call` truncates only. `telemetry_redactor` is PII-only and never runs on tool_calls.
- **Reproduction:** 1:1 turn; user "I have a severe nut allergy, remember that." Agent emits `fact_remember({key:"trait:nut_allergy", value:"severe nut allergy", visibility:"private"})`. tool_calls.input row contains the raw value; operator dashboard reads it.

#### 36. Concierge-composed planning task string leaks private constraint/rationale into trace metadata unconditionally
- **Severity:** medium
- **Surface / file:line:** `planning-tracer-metadata-task` (logs-telemetry) — `backend/planning_agent/agent.py` `_build_planning_tracer` 50-54 (`metadata={'task': request.task[:200]}`)
- **Private datum:** Private traveler constraints + rationale + who-said-what in the concierge-composed task string ("Rework the afternoon — find a wheelchair-accessible spot, Maya can't manage stairs"). Up to 200 chars verbatim.
- **Leak path:** concierge generate_plan → tool_input['task'] (LLM free text) → `task_with_context` (_plan.py:631) → `PlanningRequest.task` (645) → `arun_planning_agent` → `_build_planning_tracer` → `Trace.metadata['task']` (53) → `persist_trace` writes `model_dump_json` to disk.
- **Missing guard:** NONE. Trace.metadata is serialized unconditionally; the `TRACE_CAPTURE_USER_CONTENT` gate governs only prompt/response span capture, NOT metadata. `redact_private_signal`/`telemetry_redactor` never invoked on task. 200-char truncation is not redaction.
- **Reproduction:** Production-origin process with TRACE_CAPTURE_USER_CONTENT off; user "rework the afternoon — find a wheelchair-accessible spot, Maya can't manage stairs"; generate_plan composes that task; trace file `traces/planning/*.json` contains metadata.task verbatim despite content-capture off. (Severity bounded to local filesystem archive.)

#### 37. Tool error headline written to agent_events.context JSONB with no redactor — can carry user-stated constraint/budget values
- **Severity:** medium
- **Surface / file:line:** `agent-events-tool-error-context` (logs-telemetry) — `backend/core/event_logger.py` `log_tool_error_event` 150-159 (truncated_error → context['original_error'])
- **Private datum:** A confidential constraint value supplied as a tool argument that the tool's error message echoes ("price_ceiling=50 must be > 0", "Invalid value for dietary_restriction: kosher", date/enum echoes).
- **Leak path:** parallel_tools wraps exception as `ToolOutcome.error` (verbatim, may embed user arg) → `_outcome_error_text` → `log_tool_error_event(original_error=err)` → `err.split('\n',1)[0][:200]` (length cap only) → context['original_error'] → `create_agent_event` → agent_events.context JSONB.
- **Missing guard:** NONE. First-line+200-char truncation is not a value scrubber. Parallel sink concierge_turns wires `telemetry_redactor.redact`; this agent_events sink has no equivalent. args_sig is a SHA-256 hash (not a leak); the leak is original_error only.
- **Reproduction:** User states a private budget ceiling; agent calls a tool routing it through `_validators._check_positive_number` with an out-of-range value → error envelope "price_ceiling=50 must be > 0" → agent_events.context['original_error'] verbatim, attributable via contextvars user_id/trip_id. Test `test_tool_error_telemetry.py` pins the unredacted behavior.

#### 38. Concierge tool-call logger dumps full search tool_input (dietary_requirements, budget_ceiling_eur) into agent_events.context
- **Severity:** high
- **Surface / file:line:** `agent-events-context-passthrough` (logs-telemetry) — `backend/concierge/tools.py` `_log_concierge_tool_event` 612-623 (input dict 618-620)
- **Private datum:** Per-trip hard constraints in search args: `dietary_requirements` (hard filter), `budget_ceiling_eur` (per-person budget), free-text query "include constraints" — derived from confidential per-user hard_constraints/Personal Memory.
- **Leak path:** search_restaurants/activities tool call → tool_input → `_log_concierge_tool_event` → context={'input': {k:v for tool_input if k!='search_descriptions'}, ...} → `log_agent_event('search_executed')` → `create_agent_event` → agent_events.context. Downstream: `get_agent_events` feeds the trip-scoped digest; `_format_agent_events` dumps the entire context into the digest LLM prompt → member-facing /api/trips/{trip_id}/summary.
- **Missing guard:** NONE. Dict comprehension excludes only `search_descriptions`; constraint values pass verbatim. No redactor on path. Asymmetric composer guards bound to group_compose only.
- **Reproduction:** Group trip; member A has kosher + €40 budget. User "where should we eat tonight?"; agent calls `search_restaurants(dietary_requirements=['kosher'], budget_ceiling_eur=40, ...)`. agent_events row stores 'kosher'/40 verbatim; nightly digest inlines them; GET /api/trips/{trip_id}/summary retrievable by every member.

#### 39. Planning tool-call logger dumps ENTIRE search_venues tool_input (dietary/budget/energy) into agent_events.context
- **Severity:** high
- **Surface / file:line:** `agent-events-context-passthrough` (logs-telemetry) — `backend/planning_agent/agent.py` `_log_planning_tool_event` 253-265 (input at 261)
- **Private datum:** `search_venues` args `dietary_requirements` (['halal','vegetarian']), `max_price_per_person` (EUR ceiling), `max_energy` (energy/fatigue) — confidential per-traveler hard constraints.
- **Leak path:** search_venues tool call → tool_input → `_log_planning_tool_event` → context={'tool':..., 'input': tool_input (NO field exclusion), ...} → `log_agent_event(agent='planning','search_executed')` → `create_agent_event` → agent_events.context.
- **Missing guard:** NONE. The whole tool_input serialized. No redactor on the planning event path.
- **Reproduction:** Planner run; traveler A has hidden 'halal' + €50 ceiling, B low energy. Model emits `search_venues(dietary_requirements=['halal'], max_price_per_person=50, max_energy='low')`. `_log_planning_tool_event` stores it verbatim; `SELECT context FROM agent_events WHERE agent='planning'` returns the hard-constraint values unredacted.

#### 40. Model-composed prune reason logged at INFO leaks confidential observation content to app logs
- **Severity:** medium
- **Surface / file:line:** `memory-prune-reason-log` (logs-telemetry) — `backend/concierge/memory_tools.py` line 780 (`logger.info` in `_execute_prune`)
- **Private datum:** Confidential observations referenced in the prune reason: dietary/medical/budget/accessibility constraints + who-said-what ("pruning duplicate of Ben's nut-allergy note", "Maya no longer vegetarian per latest 1:1").
- **Leak path:** concierge turn → `memory_observations_prune` (dispatch memory_tools.py:566) → `_execute_prune` → reason = tool_input['reason'] (model free text) → `logger.info('Pruned %d observations: %s', count, reason)` (780) → stdlib logging to stdout/aggregation.
- **Missing guard:** NONE. `telemetry_redactor.redact` is wired only on the concierge_turns columns; no global logging filter performs redaction (only `RequestContextFilter`, which adds context and returns True). `redact_private_signal`/`check_private_signal` never called on the reason.
- **Reproduction:** 1:1 turn; model calls `memory_observations_prune(reason="duplicate of Dev's nut-allergy constraint... Maya no longer vegetarian per latest 1:1")`; line 780 emits the full reason to stdout unredacted, with names + dietary/medical values. (Egress class: application logs / internal sink.)

---

## Needs human judgment (3)

These were traced but NOT auto-confirmed — they hinge on a product/privacy judgment call or non-deterministic LLM behavior that static reading cannot settle. Treat as open until a human owner rules.

### NH-1. Individual budget ceiling leaks to group via paraphrased "Binding Constraints" synthesis section
- **Surface:** `compose-group-message-tool` — `backend/concierge/group_compose.py` `execute_compose_group_message`; root gap `find_constraint_leaks` has no budget coverage + corpus check keyword_layer=False (1042)
- **Why needs-human:** Verifier errored (rate limit) — not adjudicated. The claim: a member's `$50/day` ceiling, paraphrased by group synthesis into "Binding Constraints" (kept by `strip_private_group_sections`), reaches the composer prompt; `find_constraint_leaks` structurally cannot fire on a budget figure, `_semantic_privacy_guard` is fail-open, and the corpus check is verbatim-only so the synthesizer paraphrase won't substring-match the source memory.
- **Decision needed:** Does a group-framed budget target ("aim for ~$50/day", no name) constitute a private leak under the system's model, and should `find_constraint_leaks`/corpus coverage be extended to budget?

### NH-2. Autopilot prompt embeds raw group-profile private reasoning sections without strip_private_group_sections
- **Surface:** `autopilot-group-candidate` — `backend/concierge/planning_autopilot.py` `_build_prompt` 362-366, 398
- **Why needs-human:** Prompt-side gap is REAL and confirmed (`_build_prompt` embeds raw `group_profile.markdown_content[:600]` with NO `strip_private_group_sections`, unlike the sanctioned composer at group_compose.py:644). But (1) the private sections are already de-attributed at synthesis time ("describe the party in aggregate"), so the reachable datum is an unattributable group tension, and (2) egress is mediated by an LLM told to "use group-safe synthesis" plus strict-compose recovery. Whether a paraphrased taste-tension actually carries forward AND the fail-open semantic guard lets it pass is probabilistic LLM behavior, so criterion "provably reachable" is not deterministically met.
- **Decision needed:** Add `strip_private_group_sections` to `_build_prompt` as Tier-3 defense-in-depth regardless (cheap, matches the sanctioned composer), and decide whether de-attributed tension counts as a leak. Tests always pass `group_profile=None`, so the populated path is untested.

### NH-3. Unredacted hero_title leaks constraint/identity into public share PNG + og:image
- **Surface:** `story-card-png` — `backend/core/story_projection.py` 167; rendered `story_card.py:319,178-181`
- **Why needs-human:** Mechanically accurate (hero_title bypasses check_private_signal + _names_present and is painted into the noauth /stories/{slug}/card.png + og:image fetched by crawlers with no human in the loop). NOT auto-confirmed because the pass-through is a documented, test-codified product tradeoff: `tests/test_story_projection.py:113-118` asserts hero_title is intentionally left intact while a leaking hero_subtitle is dropped, and the source comment defers redaction to the owner's pre-share preview. Whether that posture is acceptable for the noauth og:image surface is a product/privacy call, and the trigger depends on the LLM choosing to put a constraint/name in a 4-8 word title.
- **Decision needed:** Either (a) accept the owner-preview-only posture for the card PNG, or (b) extend hero_title redaction/blanking to the public projection (and update the enshrining test).

---

## Appendix — every scanned surface id (105 traced, 0 errored)

> Surface ids inventoried and traced this run. Confirmed/needs-human surfaces are enumerated above; the remainder were traced and not flagged as leaks on this run. (Distinct ids below; several ids appear under multiple independent traces.)

- proactive-group-turn-router
- present-options-reaction-card
- trip-shapes-card
- venue-card
- plan-ready-card
- taste-dna-reflection-card
- group-interjection-triage-reason
- triage-prompt-for-agent
- interjection-group-candidate
- proposal-detail-readout
- home-concierge-feed-proposal-card
- daily-digest-content
- digest-to-home-card
- invite-dispatch-sms
- discover-feed-friends-section
- story-landing-html
- story-public-json
- build-public-story-payload
- plan-seed-public
- story-published-feed-event
- profile-public-stories-list
- atlas-unpacked-render-card
- atlas-unpacked-builder
- booking-confirmation-receipt
- concierge-reasoning-spans-plan
- concierge-turns-tool-calls
- planning-tracer-metadata-task
- agent-events-tool-error-context
- agent-events-context-passthrough
- memory-prune-reason-log
- compose-group-message-tool
- autopilot-group-candidate
- story-card-png

> NOTE: the inventory counted **105 surfaces traced** across all sweep angles (group / cross-user / public / logs-telemetry egress classes); the ids above are the distinct surface ids that produced findings or were explicitly adjudicated. The full 105 includes the multi-trace duplicates (e.g. `venue-card`, `daily-digest-content`, `digest-to-home-card`, `present-options-reaction-card`, `agent-events-context-passthrough` each traced multiple times under different candidates) plus surfaces traced and cleared on this run. **0 surfaces and 0 angles errored**, so the inventory is fully examined for this run.
