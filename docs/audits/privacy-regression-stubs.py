"""Privacy-leak regression stubs — GENERATED from privacy-trace-run-latest.md.

One pytest function per CONFIRMED leak (40). Each asserts that a concrete
private datum (constraint value, Personal Memory phrase, who-said-what
attribution, or a hidden destination) does NOT reach the named egress for the
named surface. These are STUBS: the docstring captures the leak path + the
missing guard, and the body is a TODO that a human fills in against the real
fixtures.

Convention mirrors travel-agent/tests/concierge/test_privacy_redactor.py and
test_group_compose.py: offline where possible (mock LLM + DB), assert the
private datum is absent from / redacted at the egress surface, and DO NOT
loosen the fixture to make the test pass — fix the guard.

Each test is expected to FAIL until the corresponding guard is wired. Mark
`@pytest.mark.xfail(reason="leak not yet fixed", strict=True)` only after a
human has reviewed and accepted the finding, so a future fix flips it to pass.

Severity is in each docstring (critical first in the source report).
"""

from __future__ import annotations

import pytest


# ── CRITICAL ────────────────────────────────────────────────────────────────


def test_no_leak_venue_card_why_for_person():
    """[critical] venue-card: post_venue_card ships the requester's Personal
    Memory to the whole group via recommendation.why_for_person.

    Path: agent prompt injects requester observations + hard_constraints
    (agent.py:839/841) -> _prompts_skills.py:1063 tells the LLM to fill
    why_for_person from Personal Memory -> post_venue_card (tools.py:356) ->
    RecommendationPayload clamp-only (content.py:272) -> create_venue_card
    (structured_messages.py:614) -> create_message(venue_card) into the group
    conversation read by all members.
    Missing guard: NONE. Compose guards scan only the agent REPLY, not the
    tool-emitted card.
    """
    # TODO: GROUP conv WITH trip (Maya requester, Tom member). Maya PM has
    # "you prefer slow evenings, not scenes" + a hard constraint. Agent calls
    # post_venue_card with why_for_person echoing that. Assert the persisted
    # venue_card metadata read by Tom contains no Maya Personal-Memory phrase
    # / why_for_person is redacted before egress.
    pytest.fail("stub: assert why_for_person Personal Memory is not group-visible")


def test_no_leak_daily_digest_content_observations():
    """[critical] daily-digest-content: per-user observations (dietary/budget/
    accessibility/medical, incl. shared=False and named attribution) reach the
    shared morning_brief card with no constraint/identity guard.

    Path: _gather_day_inputs selects observations across ALL members with NO
    shared/user filter (_shared.py:269-284) -> _format_observations raw
    (formatters.py:117-125) -> daily-digest Haiku -> day_arc/forward_signals
    -> _digest_subtitle -> morning_brief card to every member.
    Missing guard: NONE. Sanctioned reader get_shared_observations_for_trip
    gates on shared.is_(True); the digest query ignores `shared` entirely.
    """
    # TODO: trip Priya/Tom/viewer; agent_observe(target_user_id=Priya,
    # category="dietary", content="Priya can only eat vegetarian...") and a
    # shared=False "general" observation. Run generate_daily_digest. Assert the
    # observation is excluded (shared filter) and the morning_brief subtitle
    # contains no per-user constraint value / named attribution.
    pytest.fail("stub: assert private/non-shared observations excluded from digest card")


# ── HIGH ────────────────────────────────────────────────────────────────────


def test_no_leak_proactive_group_turn_router():
    """[high] proactive-group-turn-router: the injected proactive system prompt
    is persisted verbatim into the shared group conversation and served to all
    members, bypassing all compose guards.

    Path: social_state genesis -> group_interjection intent ->
    ProactiveCandidate.prompt (audience=group) -> run_proactive_turn ->
    session.send_message(system) -> persist_user_message(sender_type='system',
    session.py:908-915) -> get_messages (no sender_type filter) -> GET
    /api/conversations/{id}/messages returns it verbatim.
    Missing guard: NONE. Compose guards run only on the agent REPLY; the
    inbound system prompt is persisted before any composer runs; proactive
    turns also skip the input safe-scan.
    """
    # TODO: group trip >=2 members with named constraints in social_state.
    # Drive run_proactive_turn for a group_interjection candidate. Assert the
    # persisted sender_type='system' row content (and the GET /messages
    # response) contains no member name + private constraint, OR that system
    # rows are filtered/redacted on the member-facing read path.
    pytest.fail("stub: assert proactive system prompt is not group-readable")


def test_no_leak_present_options_reaction_card():
    """[high] present-options-reaction-card: present_options content/context/
    labels reach the group thread with no privacy guard.

    Path: present_options (tools.py:336) -> _execute_present_options (only
    non-empty content + option-count checks) -> create_reaction_card (589) ->
    create_message(reaction_card) into the group conversation.
    Missing guard: NONE. Sibling _execute_propose_change calls
    check_proposal_privacy (line 353); _execute_present_options calls nothing.
    """
    # TODO: group trip, Maya has wheelchair/no-stairs + gluten constraint.
    # _execute_present_options(content="...no stairs for the knee issue...",
    # context="gluten-free, step-free", options=[...]). Assert it errors / the
    # card is scrubbed, mirroring the propose_change path.
    pytest.fail("stub: assert present_options card content runs check_proposal_privacy")


def test_no_leak_trip_shapes_card():
    """[high] trip-shapes-card: generate_trip_shapes posts an LLM-authored card
    (best_for/pitch) to the group bypassing the compose guard.

    Path: known_preferences (tools_schema.py:1091) -> _execute_generate_trip_
    shapes folds it into a temp-0.9 privacy-blind sub-LLM (~97/127) -> shapes
    -> create_trip_shapes_card (structured_messages.py:77) ->
    create_message(reaction_card) into group conv.
    Missing guard: NONE (only a soft prompt instruction; sibling
    check_proposal_privacy not wired here).
    """
    # TODO: group trip; Maya has €50 budget + vegetarian + knee injury. Agent
    # calls generate_trip_shapes(known_preferences=<those>). Assert the posted
    # card's best_for/pitch contain no per-member constraint value / attribution.
    pytest.fail("stub: assert trip_shapes card text is privacy-gated before group egress")


def test_no_leak_venue_card_personal_take():
    """[high] venue-card: a cached personal-tier Take headline/verdict is posted
    to the group unguarded via take_headline/take_verdict.

    Path: get_most_recent_personal_take(user_id=requester) (content.py:246) ->
    take.payload.headline / verdict.opinion (257-260) -> create_venue_card ->
    metadata_ + content_fallback -> all group members.
    Missing guard: NONE. Take selected by requester user_id with no group-safe
    projection; bypasses execute_compose_group_message.
    """
    # TODO: A + B in group; A has "avoids loud rooms"/vegetarian and a personal
    # Take for venue_42. A asks "what do you think of venue_42?" in the group.
    # Assert the venue_card verdict prose surfaced to B encodes no private
    # constraint of A.
    pytest.fail("stub: assert personal-tier take prose is not group-visible")


def test_no_leak_plan_ready_card():
    """[high] plan-ready-card: plan_ready first_day_teaser leaks a planner
    day_theme (constraint by implication) to the group.

    Path: _build_planner_personas adds personal_memory + private_constraints
    (_plan.py:84-111) -> planner LLM -> day_themes[1] -> _teaser (991) ->
    create_plan_ready_card(first_day_teaser=_teaser) -> create_message into
    group conv.
    Missing guard: NONE. _scan_planner_output scans only raw_plan/
    group_facing_message and runs AFTER the card is posted.
    """
    # TODO: group trip pre_trip; member A has accessibility/energy constraint.
    # generate_plan -> day_themes[1]="Gentle step-free wanderings". Assert the
    # plan_ready card teaser discloses no member accessibility constraint.
    pytest.fail("stub: assert plan_ready first_day_teaser is privacy-scanned")


def test_no_leak_taste_dna_reflection_card():
    """[high] taste-dna-reflection-card: a user's private budget/energy/social
    taste phrases are written into the SHARED group conversation, self-attributed.

    Path: chat.py:403 _turn_then_dna_followup ->
    post_dna_reflection_card_if_eligible(actor.id, session.conversation_id,
    trip_id) -> get_latest_personal_memory.taste_dimensions ->
    _build_reflection_phrases -> create_taste_dna_reflection_card ->
    create_message. conversation_id resolves to conversation_type='group'.
    Missing guard: NONE. Fire-and-forget structured write; strict_group_compose
    only intercepts in-turn free text.
    """
    # TODO: group trip (Maya + Sam); Sam has budget {label:"Thrifty"} +
    # energy + social >=3 evidence each, no prior taste_dna observation. Sam
    # sends a message via stream. Assert the eligibility check gates on
    # group/member-count (no card into a group conv) OR no card is inserted.
    pytest.fail("stub: assert taste-DNA reflection card never lands in a group conversation")


def test_no_leak_group_interjection_triage_reason():
    """[high] group-interjection-triage-reason: the Haiku-derived intent/reason
    is persisted as a group-visible system message, bypassing all compose guards.

    Path: triage_group_interjection builds prompt from raw transcript + RAW
    social_state_markdown (NO strip_private_group_sections) -> decision.intent/
    reason -> ProactiveCandidate -> run_proactive_turn -> session.send_message
    (system) -> persisted (session.py:908-912) -> GET /messages unfiltered.
    Missing guard: NONE. get_social_state does not strip; read endpoint has no
    system-row filter.
    """
    # TODO: trip >=2 members; social_state has Optimization Targets / Tensions
    # naming Maya's mobility + Sam's preference. Idle group thread; triage
    # interjects. Assert the persisted system row + GET /messages contain no
    # named private constraint lifted from the agent-only social-state sections.
    pytest.fail("stub: assert interjection intent/reason is stripped before group persist")


def test_no_leak_triage_prompt_for_agent():
    """[high] triage-prompt-for-agent: private Personal-Memory taste prose in
    prompt_for_agent is persisted as a group system message and served to all
    members when Haiku mislabels a taste nudge as target='group'.

    Path: taste_summaries ("{name}: {Who They Are prose}") -> run_triage ->
    TriageNotification(target='group', prompt_for_agent=<taste prose>) ->
    candidates_from_triage (arbiter.py:875) -> run_proactive_turn (group
    session) -> persist_user_message(system) -> GET /messages verbatim.
    Missing guard: NONE. Private-routing mitigation fires only for
    target_audience=='private'.
    """
    # TODO: trip Maya + Sam; Maya PM "Drawn to underground techno and
    # natural-wine bars...". Force a triage notification with target="group"
    # and prompt_for_agent naming Maya's taste. Assert the persisted system row
    # is scrubbed of the named taste prose (or target=group taste nudges are
    # blocked / re-routed).
    pytest.fail("stub: assert group-labeled taste nudge does not persist named taste prose")


def test_no_leak_interjection_group_candidate():
    """[high] interjection-group-candidate: the group-interjection intent is
    persisted as a raw system message and served verbatim to all members.

    Path: triage_group_interjection -> Haiku reads social_state (per-member
    dietary/accessibility/budget/fatigue with attribution, genesis.py:266-278)
    + roster -> InterjectionDecision.intent -> ProactiveCandidate(audience=
    'group') -> run_proactive_turn -> session.send_message(system) -> persisted
    -> GET endpoints (no sender_type filter).
    Missing guard: NONE. Inbound proactive system message persisted directly.
    """
    # TODO: trip Maya (vegetarian hard constraint from 1:1) + Sam. Idle
    # restaurant thread; triage returns target="group" intent naming Maya's
    # dietary constraint + resistance. Assert the persisted/served row carries
    # no member name + private constraint.
    pytest.fail("stub: assert group interjection intent is not member-readable with attribution")


def test_no_leak_proposal_detail_readout():
    """[high] proposal-detail-readout: a vote comment leaks a private constraint
    + who-said-it to the whole group via proposal detail.

    Path: POST /vote (VoteRequest.comment) -> vote_on_proposal stores comment
    verbatim into votes JSONB (change_proposals.py:543-545) -> GET
    /proposals/{id} -> _to_detail (proposals.py:891 votes=proposal.votes) ->
    ProposalDetail.votes to every require_trip_member.
    Missing guard: NONE. check_proposal_privacy scans only title/description/
    impact/alternatives; resolution_note is scrubbed but the vote comment is not.
    """
    # TODO: trip Alice/Bob/Carol; Carol votes with comment "...not wheelchair
    # accessible and Sarah needs step-free access". Assert the vote comment is
    # run through redact_private_signal before it ships in _to_detail.votes.
    pytest.fail("stub: assert vote-comment private signal is redacted at proposal detail egress")


def test_no_leak_home_concierge_feed_proposal_card():
    """[high] home-concierge-feed-proposal-card: feasibility-catch reschedule
    proposals reach the group home feed without check_proposal_privacy.

    Path: itinerary block title (user-editable) -> _produce_feasibility_catch
    (proactive.py:908-926) builds title/description/impact -> RAW
    create_change_proposal (proactive.py:904, NO gate) ->
    get_proposals_for_trips -> _catch_reschedule_card -> every member's home
    feed.
    Missing guard: NONE. check_proposal_privacy runs only inside
    build_and_persist_proposal and the tool path.
    """
    # TODO: multi-member trip; member A renames a block "Wheelchair PT"; two
    # same-day blocks geo-close -> feasibility catch. Assert the produced
    # proposal passes through check_proposal_privacy (title/impact scrubbed)
    # before reaching the home feed.
    pytest.fail("stub: assert feasibility-catch proposals run check_proposal_privacy")


def test_no_leak_daily_digest_content_group_profile():
    """[high] daily-digest-content: group-profile private reasoning sections
    (Tensions & Trade-offs / Optimization Targets) feed the daily-digest LLM
    unstripped and surface on the shared morning_brief card.

    Path: get_latest_group_profile.markdown_content[:600] (daily.py:74-76) ->
    inputs.group_context -> _call_daily_digest "### Group Profile"
    (llm_calls.py:42-44) -> Haiku -> day_arc/forward_signals -> _digest_subtitle
    -> morning_brief card to every member.
    Missing guard: NONE. strip_private_group_sections never called; digest
    engine has zero privacy imports.
    """
    # TODO: multi-member in-progress trip; group profile with "## Tensions &
    # Trade-offs" content in first 600 chars. Run generate_daily_digest. Assert
    # the group_context is passed through strip_private_group_sections (no
    # PRIVATE_GROUP_PROFILE_HEADINGS reach the LLM / the card subtitle).
    pytest.fail("stub: assert digest strips private group-profile sections")


def test_no_leak_daily_digest_content_messages_identity():
    """[high] daily-digest-content: who-said-what attribution from per-member
    messages surfaces in the shared digest card without find_identity_leaks.

    Path: _gather_day_inputs pulls all trip messages -> _format_messages labels
    each line with metadata_['user_name'] (formatters.py:65-80) -> Haiku ->
    group_cohesion/turning_point -> _digest_subtitle -> shared morning_brief.
    Missing guard: NONE. find_identity_leaks never runs in the digest engine.
    """
    # TODO: trip Maya/Alex; Maya posts a private fatigue/health complaint.
    # Run the digest. Assert the morning_brief subtitle does not name Maya
    # alongside a private sentiment (find_identity_leaks on digest output).
    pytest.fail("stub: assert digest output runs find_identity_leaks over member names")


def test_no_leak_digest_to_home_card_group_profile():
    """[high] digest-to-home-card: group-profile private reasoning sections feed
    the daily-digest LLM and surface on the shared concierge home card.

    Path: get_latest_group_profile.markdown_content -> daily.py:76 group_context
    (NO strip) -> _call_daily_digest group_section (llm_calls.py:43-49) ->
    Haiku -> group_cohesion/turning_point -> _digest_to_card / _digest_subtitle
    (cards.py:233) -> ConciergeHomeCard to every member.
    Missing guard: NONE. strip_private_group_sections not on path.
    """
    # TODO: 3-member active trip; profile Tensions section describing intra-
    # group friction + the budget-constraint holder. Assert the concierge home
    # card subtitle carries no intra-group tension / binding-constraint
    # attribution.
    pytest.fail("stub: assert concierge home card strips private group-profile reasoning")


def test_no_leak_digest_to_home_card_observations():
    """[high] digest-to-home-card: day observations (constraint/preference free
    text, incl. shared=False) flow into the daily-digest LLM and out through
    the shared card subtitle with no constraint guard.

    Path: observations -> _gather_day_inputs (no shared filter) ->
    _format_observations raw (formatters.py:117-125) -> Haiku ->
    forward_signals/day_arc -> _digest_subtitle (cards.py:236-240) -> shared
    card for all members.
    Missing guard: NONE. Sanctioned path uses _aggregate_constraints +
    find_constraint_leaks; the digest applies neither and gathers shared=False
    rows.
    """
    # TODO: trip A/B; A has a private shared=False observation
    # ("A is hiding a $400 hard budget ceiling"). Assert it is excluded from
    # the digest and the card subtitle carries no budget/constraint value.
    pytest.fail("stub: assert digest excludes private observations and scans constraints")


def test_no_leak_digest_to_home_card_messages_identity():
    """[high] digest-to-home-card: per-member message content with attached
    display names feeds the digest LLM, enabling who-said-what attribution in
    the shared subtitle.

    Path: messages_table -> _format_messages stamps user_name -> daily digest
    LLM -> day_arc.group_cohesion/turning_point -> _digest_subtitle -> shared
    ConciergeHomeCard to every member.
    Missing guard: NONE. find_identity_leaks never runs on digest content.
    """
    # TODO: 3-member trip; Maya posts a private withdrawal/fatigue message.
    # Assert the concierge card subtitle does not name Maya with a private
    # sentiment.
    pytest.fail("stub: assert digest card subtitle has no who-said-what attribution")


def test_no_leak_invite_dispatch_sms():
    """[high] invite-dispatch-sms (public): the organizer-authored invitee_note
    ships verbatim to an external non-member over SMS/email with no privacy
    guard.

    Path: POST /invites InviteCreateRequest.invitee_note (no validation) ->
    create_invite (stored verbatim) -> dispatch_invite -> _compose_body
    (invite_dispatch.py:244-245) -> body=f"{who}: {invitee_note}\\n{url}" ->
    Twilio/email to an external prospective invitee.
    Missing guard: NONE. Never routes through compose; redact_private_signal
    never called (only html.escape on email). Sibling state_updater.py:96-98
    DOES call redact_private_signal.
    """
    # TODO: organizer POSTs /invites with invitee_note naming another member's
    # diet/budget/access ("Maya's vegan and her budget is only $50/day...
    # Tom's knee"). Assert the dispatched SMS/email body is run through
    # redact_private_signal (the named constraints are scrubbed).
    pytest.fail("stub: assert invitee_note is redacted before external SMS/email egress")


def test_no_leak_discover_feed_friends_section():
    """[high] discover-feed-friends-section (cross-user): an actor-authored
    free-text note/curator_hook leaks to followers via the Discover friends
    feed with no privacy scan.

    Path: POST /api/events EventCreate.context (actor-controlled) ->
    create_user_event writes context verbatim -> get_social_feed SELECTs
    context across the follow graph -> compose_discover_feed friends loop reads
    ctx.get('note') into hook + display_name into meta_text (compose.py:509,516)
    -> GET /api/discover/feed to follower B.
    Missing guard: NONE on write->read->egress. check_private_signal /
    redact_private_signal never invoked in discover/follows/events.
    """
    # TODO: as A (followed by B) POST /api/events with context.note naming
    # diet/budget/access ("...$50/day ceiling and Maya is vegan + can't do
    # stairs"). B GET /api/discover/feed. Assert the friend-card hook is
    # redacted (no constraint value / attribution).
    pytest.fail("stub: assert friends-feed note/curator_hook is redacted at egress")


def test_no_leak_story_landing_html():
    """[high] story-landing-html (public): hero_title bypasses check_private_
    signal + name redaction and ships verbatim to the public story page and
    link-preview crawlers.

    Path: composer (observations + co-traveler context) -> hero_title
    (trip_story.py:478) -> trip_stories.hero_title -> get_public_story_by_slug
    -> build_public_story_payload copies hero_title verbatim (story_projection
    .py:167, NO check_private_signal/_names_present) -> story_landing
    (story_landing.py:119) -> <title>/og:title/<h1> on noauth /stories/{slug}.
    Missing guard: NONE. Sections + hero_subtitle are scanned; hero_title is
    deliberately exempt.
    """
    # TODO: owner observation "Kept every meal strictly gluten-free";
    # composer hero_title="The Gluten-Free Lisbon Week". Render /stories/{slug}.
    # Assert hero_title is run through check_private_signal/_names_present
    # (constraint/name dropped or blanked) before the public HTML.
    pytest.fail("stub: assert public story hero_title is privacy-scanned")


def test_no_leak_story_public_json():
    """[high] story-public-json (public): hero_title bypasses check_private_
    signal and _names_present; a constraint or co-traveler name reaches public
    JSON unredacted.

    Path: compose_trip_story composes hero_title from overall_arc +
    get_active_observations -> trip_stories.hero_title ->
    get_public_story_by_slug -> build_public_story_payload(hero_title=
    story.hero_title) (no scan) -> public_story_json GET
    /api/public/stories/{slug}.
    Missing guard: NONE. hero_title exemption; owner preview has no hero_title
    flag.
    """
    # TODO: owner Ana + co-traveler Maya (redact_names={"Maya"}), accessibility
    # constraint. Composer hero_title="Maya's Step-Free Birthday in Lisbon".
    # GET /api/public/stories/{slug}. Assert hero_title is redacted (Maya
    # stripped, step-free dropped).
    pytest.fail("stub: assert public story JSON hero_title is redacted")


def test_no_leak_build_public_story_payload():
    """[medium] build-public-story-payload (public): public story section/hero
    leaks dietary & medical constraints outside the finite keyword regex
    because the corpus layer is never run.

    Path: compose_trip_story (observations + overall_arc) -> sections[].body /
    hero_subtitle -> build_public_story_payload -> check_private_signal(body)
    with keyword_layer=True but NO private_corpus -> public landing/json/card/
    plan-seed.
    Missing guard: corpus layer of check_private_signal (verbatim match vs
    load_private_corpus_for_trip) never invoked; finite keyword regex omits
    vegetarian/celiac/diabetic/low-sodium/pescatarian.
    """
    # TODO: owner observation "Kept it vegetarian... celiac-safe bakeries".
    # Composer body echoes it. Assert build_public_story_payload runs
    # check_private_signal WITH the trip private_corpus, so the section is
    # dropped.
    pytest.fail("stub: assert public story projection runs the corpus layer of check_private_signal")


def test_no_leak_plan_seed_public():
    """[high] plan-seed-public (public): the unredacted story hero_title leaks
    constraint / personal-memory / co-traveler signal to the public login-free
    plan-seed.

    Path: compose_trip_story (raw observations + overall_arc -> hero_title,
    stored verbatim) -> get_public_story_by_slug -> build_public_story_payload
    (hero_title unscrubbed, 167) -> build_plan_seed weaves into planning_brief
    (232) + inspiration_hero_title (249) -> get_plan_seed_by_slug ->
    public_plan_seed GET /api/public/stories/{slug}/plan-seed (noauth).
    Missing guard: NONE. hero_title exemption; redact_names not applied to
    hero_title.
    """
    # TODO: trip owner Sam + member Maya; arc beat "Maya's birthday dinner";
    # composer hero_title="Maya's Birthday in Porto". GET /plan-seed. Assert
    # inspiration_hero_title + planning_brief carry no co-traveler name /
    # constraint.
    pytest.fail("stub: assert plan-seed hero_title is redacted before noauth egress")


def test_no_leak_story_published_feed_event():
    """[high] story-published-feed-event (cross-user): the composer-generated
    hero_title reaches followers' feed without check_private_signal.

    Path: create_trip_story(hero_title=<LLM from observations>) ->
    trip_stories.hero_title -> emit_story_published_if_visible (309 ->
    build_public_story_payload returns hero_title unredacted at 167) ->
    context["hero_title"] (trip_story_shares.py:316) ->
    create_user_event("story_published") -> follows.get_feed reads context for
    every follower.
    Missing guard: NONE. Fires on every share create/PATCH regardless of the
    owner ever opening the Privacy Preview.
    """
    # TODO: owner observation "Navigated Kyoto gently after the knee surgery";
    # hero_title="A Gentler Pace Through Kyoto After My Knee"; share with
    # followers_visible=True. Follower GET /api/users/{own_id}/feed. Assert the
    # story_published event context carries no constraint hero_title.
    pytest.fail("stub: assert story_published feed event hero_title is privacy-scanned")


def test_no_leak_profile_public_stories_list_hero_title():
    """[high] profile-public-stories-list (cross-user): hero_title bypasses the
    public-story projection (check_private_signal + redact_names) on the profile
    aggregation path.

    Path: trip_stories.hero_title (composer, stored raw) ->
    list_public_stories_for_user SELECTs it directly
    (trip_story_shares.py:412) -> PublicProfileStory(hero_title=row[...]) (437)
    -> profiles.py _build_profile stories (67) -> GET /api/users/{user_id}/
    profile, viewable by ANY user.
    Missing guard: NONE. Raw SQL read, no build_public_story_payload
    projection, no check_private_signal, no redact_names, no preview gate.
    """
    # TODO: owner A + Maya, gluten-free; composer hero_title="Maya's
    # Gluten-Free Grand Tour"; share visibility "link"; A public_profile_enabled.
    # User B GET /api/users/{A}/profile. Assert stories[].hero_title is
    # projected through check_private_signal + redact_names.
    pytest.fail("stub: assert profile-list hero_title runs the public-story projection")


def test_no_leak_profile_public_stories_list_destination():
    """[medium] profile-public-stories-list (cross-user): destination ignores
    RedactionPolicy.show_destination on the profile aggregation path.

    Path: trip_story_shares.redaction_policy (show_destination=False set via
    update_share_settings) NOT read by list_public_stories_for_user -> SELECT
    places.name / trips.title -> destination unconditionally
    (trip_story_shares.py:438) -> PublicProfileStory.destination -> GET
    /api/users/{user_id}/profile.
    Missing guard: NONE. Slug path emits destination only when
    policy.show_destination; the profile-list query never joins redaction_policy.
    """
    # TODO: owner A creates a share with
    # update_share_settings(redaction_policy=RedactionPolicy(show_destination=
    # False)), public_profile_enabled. User B GET /api/users/{A}/profile.
    # Assert destination is omitted (honors show_destination=False).
    pytest.fail("stub: assert profile-list destination honors RedactionPolicy.show_destination")


def test_no_leak_atlas_unpacked_render_card():
    """[high] atlas-unpacked-render-card (public): an LLM-generated DNA phrase
    echoes a confidential constraint verbatim into the public Unpacked card PNG.

    Path: refresh_personal_memory -> _generate_dna_phrases(taste_dims,
    narrative[:1200]) -> cached taste_dims['reflection_phrases']
    (refresh_memory.py:545, no redaction) -> _build_reflection_phrases cached
    branch verbatim (me.py:136-138) -> you_card.title -> render_unpacked_card
    paints into PNG -> noauth GET /unpacked/{token}/card.png + og:image.
    Missing guard: partial only (synthesis [private]-abstraction is LLM-side
    fail-open and exempts allergy/accessibility). No canonical guard on path.
    """
    # TODO: user logs celiac/gluten-free or step-free constraint; cached DNA
    # phrase "always finds the gluten-free table". Build the unpacked card.
    # Assert the rendered you_card.title is run through check_private_signal /
    # _public_safe before the PNG.
    pytest.fail("stub: assert unpacked card DNA phrase is privacy-scanned before render")


def test_no_leak_atlas_unpacked_builder_cached_phrase():
    """[high] atlas-unpacked-builder (public): a cached LLM-generated DNA phrase
    leaks personal-memory constraints onto the public Atlas Unpacked card with
    no check_private_signal.

    Path: refresh_personal_memory -> _generate_dna_phrases -> cached
    reflection_phrases (no scrub) -> build_unpacked: dna_phrases =
    _build_reflection_phrases(dims) cached branch verbatim -> dna_line ->
    AtlasUnpackedCard(kind='you', title=dna_line) -> noauth GET /unpacked/{token}
    (dna_html) AND /card.png.
    Missing guard: NONE. Sibling profiles.py:_public_safe runs check_private_
    signal on these exact cached reflection_phrases; the Atlas path applies none.
    """
    # TODO: PM narrative includes sober/wheelchair note; cached phrase "travels
    # sober, always finds the alcohol-free table". build_unpacked. Assert
    # dna_phrases are filtered via check_private_signal / _public_safe inside
    # build_unpacked.
    pytest.fail("stub: assert build_unpacked filters DNA phrases via _public_safe")


def test_no_leak_atlas_unpacked_builder_interests_strong():
    """[medium] atlas-unpacked-builder (public): an interests_strong-derived DNA
    phrase can carry a constraint label to the public Unpacked card unfiltered.

    Path: refresh memory -> taste_dimensions['interests_strong'] (un-curated)
    -> build_unpacked -> _build_reflection_phrases derived branch builds "drawn
    to {interests[0]} and {interests[1]}" (me.py:165-170) -> dna_phrases[0] ->
    AtlasUnpackedCard(kind='you') -> public /unpacked/{token} + /card.png.
    Missing guard: NONE. profiles.py guards interests_strong with
    _public_safe(check_private_signal); the Unpacked builder applies no filter.
    """
    # TODO: PM has "wheelchair-accessible venues" in interests_strong; derived
    # branch -> "drawn to wheelchair-accessible venues and coastal towns".
    # Assert both the derived and cached branches route through
    # check_private_signal before becoming dna_line.
    pytest.fail("stub: assert interests_strong DNA phrase is privacy-filtered before public egress")


def test_no_leak_booking_confirmation_receipt():
    """[high] booking-confirmation-receipt: restaurant venue-brief constraint
    values (incl. severe allergies) are posted into the group trip thread
    without small-group anonymization.

    Path: traveler_profiles.severe_allergies/accessibility_requirements ->
    _load_trip_preferences_sync unions ALL members (booking_crud.py:1170-1215)
    -> build_venue_brief -> venue_brief_provider_text "Dietary needs: ...;
    Accessibility: ..." -> confirmation_details['venue_brief_shared_text'] ->
    _post_receipt -> create_booking_confirmation_receipt(group conv) -> "Shared
    with restaurant" receipt to ALL members.
    Missing guard: the small-group anonymizer _aggregate_constraints
    (member_count<=2 -> value-free counts) is MISSING; redact_corpus_phrases
    skips keyword patterns, so a value not in the personal_memories corpus
    passes.
    """
    # TODO: 2-member trip; A's severe_allergies=['shellfish allergy'] not
    # verbatim in A's personal_memories. A initiates a restaurant booking.
    # Assert the receipt posted to the group conv applies a member-count gate /
    # value-free aggregation (B cannot read A's constraint value).
    pytest.fail("stub: assert venue-brief receipt anonymizes constraints for small groups")


def test_no_leak_concierge_reasoning_spans_plan():
    """[high] concierge-reasoning-spans-plan (logs-telemetry): the reasoning-
    span plan text persists the model scratchpad over Personal Memory +
    hard_constraints with no redaction.

    Path: personal_memories + get_active_constraints_batch ->
    assemble_system_prompt (HARD_CONSTRAINTS_TEMPLATE) -> LLM -> text blocks ->
    _build_iteration_span plan_text (agent.py:766-786) -> persist_reasoning_
    spans -> _insert_reasoning_spans -> concierge_reasoning_spans.plan
    (_truncate only).
    Missing guard: NONE. telemetry_redactor.redact is wired only on the
    concierge_turns path (telemetry.py:239-242).
    """
    # TODO: member has accessibility="wheelchair user, cannot manage stairs".
    # Run a turn that emits a plan text restating it. Assert
    # concierge_reasoning_spans.plan is passed through telemetry_redactor.redact
    # (or a constraint scrub) before insert.
    pytest.fail("stub: assert reasoning-span plan text is redacted before warehouse insert")


def test_no_leak_concierge_reasoning_spans_observation():
    """[high] concierge-reasoning-spans-plan (logs-telemetry): the reasoning-
    span observation field persists raw tool-result snippets with no redaction.

    Path: private tool result (e.g. whereabouts -> per-member display_name +
    distance) -> _on_tool_result result_str (agent.py:1483-1504) ->
    span['observation']='[tool] '+snippet -> persist_reasoning_spans ->
    _insert_reasoning_spans -> concierge_reasoning_spans.observation (_truncate
    only).
    Missing guard: NONE. observation never passed through telemetry_redactor or
    any privacy detector.
    """
    # TODO: trip >=2 members with last_location; user asks "who's nearby?";
    # agent invokes whereabouts(include_group=true). Assert the persisted
    # observation field is redacted of member names + location relationship.
    pytest.fail("stub: assert reasoning-span observation field is redacted before insert")


def test_no_leak_concierge_turns_tool_calls():
    """[high] concierge-turns-tool-calls (logs-telemetry): tool_calls[].input
    persists verbatim private fact values and constraint-derived queries to the
    operator dashboard with no redactor.

    Path: result.tool_calls_made -> telemetry.persist_turn -> _insert_turn ->
    _normalize_tool_call keeps tc['input'] unchanged (telemetry.py:196-197) ->
    tool_calls JSONB insert (259). redact() applied only to user_message/reply
    (241-242).
    Missing guard: NONE. _normalize_tool_call truncates only; telemetry_redactor
    is PII-only and never runs on tool_calls.
    """
    # TODO: 1:1 turn; agent emits fact_remember({key:"trait:nut_allergy",
    # value:"severe nut allergy", visibility:"private"}). Assert the persisted
    # tool_calls.input value is redacted (or private facts are excluded from
    # the warehouse).
    pytest.fail("stub: assert tool_calls.input private fact values are redacted before insert")


def test_no_leak_planning_tracer_metadata_task():
    """[medium] planning-tracer-metadata-task (logs-telemetry): the concierge-
    composed planning task string leaks a private constraint/rationale into
    trace metadata unconditionally.

    Path: generate_plan tool_input['task'] (LLM free text) -> task_with_context
    (_plan.py:631) -> PlanningRequest.task -> arun_planning_agent ->
    _build_planning_tracer (agent.py:50-54) -> Trace.metadata['task'] ->
    persist_trace model_dump_json to disk.
    Missing guard: NONE. Trace.metadata is serialized unconditionally; the
    TRACE_CAPTURE_USER_CONTENT gate covers only prompt/response span capture,
    not metadata. 200-char truncation is not redaction.
    """
    # TODO: production-origin process, TRACE_CAPTURE_USER_CONTENT off; task=
    # "Rework the afternoon — find a wheelchair-accessible spot, Maya can't
    # manage stairs". Assert the persisted trace metadata.task is redacted (or
    # not captured when content-capture is off).
    pytest.fail("stub: assert planning-tracer metadata.task is redacted/gated")


def test_no_leak_agent_events_tool_error_context():
    """[medium] agent-events-tool-error-context (logs-telemetry): a tool error
    headline is written to agent_events.context JSONB with no redactor — can
    carry user-stated constraint/budget values.

    Path: parallel_tools wraps exception as ToolOutcome.error (verbatim,
    embeds user arg) -> _outcome_error_text -> log_tool_error_event ->
    err.split('\\n',1)[0][:200] (length cap only) -> context['original_error']
    -> create_agent_event -> agent_events.context.
    Missing guard: NONE. Truncation is not a value scrubber; the parallel
    concierge_turns sink wires telemetry_redactor.redact; this sink has none.
    """
    # TODO: user states a private budget ceiling; tool validation rejects it
    # -> error "price_ceiling=50 must be > 0". Assert agent_events.context
    # ['original_error'] is redacted of the user-supplied value.
    pytest.fail("stub: assert tool-error original_error is redacted before agent_events insert")


def test_no_leak_agent_events_context_passthrough_concierge():
    """[high] agent-events-context-passthrough (logs-telemetry): the concierge
    tool-call logger dumps the full search tool_input (dietary_requirements,
    budget_ceiling_eur) into agent_events.context.

    Path: search_restaurants/activities tool_input -> _log_concierge_tool_event
    (tools.py:612-623) -> context={'input': {k:v for tool_input if
    k!='search_descriptions'}, ...} -> log_agent_event('search_executed') ->
    create_agent_event -> agent_events.context. Downstream: get_agent_events ->
    digest LLM -> member-facing /api/trips/{trip_id}/summary.
    Missing guard: NONE. Only search_descriptions excluded; constraint values
    pass verbatim.
    """
    # TODO: group trip; member A has kosher + €40 budget. Agent calls
    # search_restaurants(dietary_requirements=['kosher'], budget_ceiling_eur=40).
    # Assert the persisted agent_events.context.input is redacted of the
    # constraint values (and they do not reach the digest summary).
    pytest.fail("stub: assert concierge search tool_input is redacted before agent_events insert")


def test_no_leak_agent_events_context_passthrough_planning():
    """[high] agent-events-context-passthrough (logs-telemetry): the planning
    tool-call logger dumps the ENTIRE search_venues tool_input (dietary/budget/
    energy) into agent_events.context.

    Path: search_venues tool_input -> _log_planning_tool_event
    (planning_agent/agent.py:253-265, input at 261) -> context={'input':
    tool_input (NO field exclusion), ...} -> log_agent_event(agent='planning',
    'search_executed') -> create_agent_event -> agent_events.context.
    Missing guard: NONE. The whole tool_input is serialized; no redactor on the
    planning event path.
    """
    # TODO: planner run; traveler A has 'halal' + €50 ceiling, B low energy;
    # model emits search_venues(dietary_requirements=['halal'],
    # max_price_per_person=50, max_energy='low'). Assert the persisted
    # agent_events.context.input is redacted of the hard-constraint values.
    pytest.fail("stub: assert planning search_venues tool_input is redacted before agent_events insert")


def test_no_leak_memory_prune_reason_log():
    """[medium] memory-prune-reason-log (logs-telemetry): a model-composed prune
    reason logged at INFO leaks confidential observation content to app logs.

    Path: memory_observations_prune (dispatch memory_tools.py:566) ->
    _execute_prune -> reason = tool_input['reason'] (model free text) ->
    logger.info('Pruned %d observations: %s', count, reason) (memory_tools.py
    :780) -> stdlib logging to stdout/aggregation.
    Missing guard: NONE. telemetry_redactor.redact is wired only on the
    concierge_turns columns; no global logging filter performs redaction (only
    RequestContextFilter, which returns True).
    """
    # TODO: 1:1 turn; model calls memory_observations_prune(reason="duplicate
    # of Dev's nut-allergy constraint... Maya no longer vegetarian per latest
    # 1:1"). Assert the emitted log record is redacted (or the reason is not
    # logged at INFO with names + constraint values).
    pytest.fail("stub: assert prune-reason log line is redacted of private observation content")
