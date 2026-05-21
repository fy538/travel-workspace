# Pre-Dogfood Area Audit 01 — Privacy & Group-Safe Synthesis

Date: 2026-05-21
Scope: end-to-end private→public boundary for group trips, including the
social sharing paths added 2026-05-20 (public profiles, follow graph,
trip-story shares, plan-similar derivation, conversation-scoped invites).
Mode: read-only; no product code, test, or config was modified.

## Summary

| Severity | Count |
|---|---:|
| P0 | 2 |
| P1 | 3 |
| P2 | 3 |
| TECH-DEBT | 2 |

**Biggest concern:** the invite landing-page snapshot (`invite_snapshot.py`)
feeds the **first 400 chars of the organizer's verbatim Personal Memory
markdown** into a Haiku prompt that produces text rendered on a public
landing page and an OpenGraph link preview. The PM excerpt routinely
contains constraint-shaped sentences (allergies, mobility notes, budget
state, mental-health context); the prompt's only "hard rules" cover
inventing venues, marketing voice, and naming the invitee — it has no
constraint-omission rule, and the privacy gate that other call sites use
(`should_omit_personal_memory_narrative_for_group_synthesis`) is not
wired in. A single tester whose PM begins with "Has a peanut allergy and
avoids stairs after a knee surgery" can land an invite link in any group
chat whose preview text inherits those facts. This is a P0 because the
artifact is reachable by anyone with the URL, not just invitees, and the
link preview hits non-invitees through native iMessage / Slack scraping.

The second P0 is structural: `strict_group_compose` (the privacy-stripped
composer that is the whole point of the boundary) is gated on
`is_group AND has_trip`. Conversation-scoped invites — the entire new
2026-05-20 pre-trip social path — create `conversation_type='group'`
rows with `trip_id=None`. In those rooms the concierge is free to ship
raw, identity-bearing text to multiple humans with no compose stripping
and no constraint-topic check.

---

## Findings

### [P0] — Invite landing snapshot leaks the organizer's private Personal Memory to invitees and link previews

**References:**
- `Travel Agent/backend/concierge/invite_snapshot.py:93-99` (`organizer_taste_summary = memory.markdown_content[:400]`)
- `Travel Agent/backend/concierge/invite_snapshot.py:145` (hash + prompt include `organizer_taste`)
- `Travel Agent/backend/concierge/invite_snapshot.py:156-183` (system prompt's only hard rules: no invented venues, no naming invitee, no marketing voice — no constraint-omission rule)
- `Travel Agent/backend/concierge/invite_snapshot.py:201-203` (prompt JSON sends `organizer.taste_summary` to the model)
- `Travel Agent/backend/concierge/invite_snapshot.py:270-279` (`_clamp` only length-caps output — no leak check)
- `Travel Agent/backend/core/privacy_catalog.py:66` defines `should_omit_personal_memory_narrative_for_group_synthesis` — used in `group_synthesizer.py:179` but **never imported** in `invite_snapshot.py`.
- `Travel Agent/backend/core/models/trip_invites.py:19-27` (snapshot is persisted on the invite row as `snapshot_text` / `question_prompt` / `og_title` / `og_description`).

**Why it matters to a real tester:** the invite landing page is the
first surface a stranger sees. The `og_description` field is what
iMessage, WhatsApp, Slack, and Twitter render as a link preview when
the invite URL is pasted — so the leak surface includes every person
who sees a forwarded link, not just invitees who tap it. A tester whose
seeded PM is `"Maya is recovering from a meniscus tear and avoids
stairs. Tight budget right now — looking for cheaper Lisbon options.
Migraine-prone in loud spaces."` can plausibly receive a snapshot like
`"Maya's leaning into flat, low-key Lisbon — quiet spots over loud
ones, a budget-friendly week. Want to help shape it?"` — every clause
of which is private to Maya, none of which she chose to publish.

**Repro / deterministic test idea:**
1. Seed a user with `personal_memories.markdown_content` whose first
   400 chars contain all four sensitive axes: an allergy
   (`"peanut allergy"`), an accessibility note
   (`"avoids stairs since the knee injury"`), a budget signal
   (`"tight budget — cheap eats only this trip"`), and a health note
   (`"recovering from migraines"`).
2. Call `invite_snapshot.generate_snapshot(collect_inputs(trip_id))`
   for a trip created by that user.
3. Assert that none of `snapshot.snapshot_text`, `snapshot.og_title`,
   or `snapshot.og_description` contains any term from the union of:
   - dietary vocabulary `_PRIVATE_KEYWORD_PATTERNS["dietary"]` in
     `privacy_redactor.py`,
   - accessibility vocabulary `_PRIVATE_KEYWORD_PATTERNS["accessibility"]`,
   - budget vocabulary `_PRIVATE_KEYWORD_PATTERNS["budget"]`,
   - medical vocabulary `_PRIVATE_KEYWORD_PATTERNS["medical"]`.
4. Run a red-team variant: seed the four axes one at a time and assert
   the Haiku output is clean on each — confirms the model isn't simply
   ignoring the more loaded phrases.

**Suggested fix direction:** treat the organizer's PM as private input
by default. Two layers, layered:
- Replace `organizer_taste_summary = memory.markdown_content[:400]` with
  a redacted summary: load the organizer's `taste_dimensions`
  (`reflection_phrases`, `interests_strong`) which are already
  curated-vocabulary safe (`api/routes/users/me.py:90-113`), and pass
  *only* those to the snapshot prompt. The narrative excerpt was a
  convenience, not a requirement.
- Add the `should_omit_personal_memory_narrative_for_group_synthesis`
  gate so that any organizer who has flipped a privacy dimension to
  `private` gets a `mode='fallback'` snapshot keyed on destination /
  saved venues only.
- Run the output through the same keyword sweep
  `privacy_redactor.check_private_signal` already enforces on proposals;
  re-prompt or fall back on a hit. The asymmetry today (proposals get
  scanned, invite snapshots don't) is the root cause.
- Add a regression test that seeds each constraint axis and asserts no
  surface vocabulary appears in any rendered field.

**Confidence:** High.

### [P0] — Pre-trip group conversations bypass `strict_group_compose`; concierge can ship raw identity-bearing text to multiple humans

**References:**
- `Travel Agent/backend/concierge/agent.py:676-677` (`has_trip = turn.trip_id is not None; is_group = conversation.conversation_type == "group"`)
- `Travel Agent/backend/concierge/agent.py:873` (`strict_compose_active = ... and is_group and has_trip` — `and has_trip` is the hole)
- `Travel Agent/backend/concierge/agent.py:1063, 1143` (every gate that flips the recovery ladder, the suppressed text-delta path, and the strict-fallback reply uses the same `is_group and has_trip` test)
- `Travel Agent/backend/concierge/group_compose.py:709-716` (compose itself bails out with `code: "no_trip"` for trip-less conversations — there is no privacy-stripped composer available pre-trip)
- `Travel Agent/backend/api/routes/invites.py:888-890` (`if invite.conversation_id is not None: return await _accept_conversation_invite(...)` — the conversation-scoped accept path adds members to a group with `trip_id=None`)
- `Travel Agent/backend/core/models/trip_invites.py:138-157` (`InviteConversationSummary` — the Phase-4 pre-trip social affordance, the exact path the 2026-05-20 social work depends on)

**Why it matters to a real tester:** the 2026-05-20 social additions
treat conversation-scoped group invites as the on-ramp — three friends
chat for a week, *then* the conversation is promoted to a trip. During
that pre-trip window, conversation members may have already submitted
intake (`/api/invites/{token}/intake`), and the concierge sees their
PM + observations via `load_preference_profiles` even when `trip_id`
is `None`. With strict compose disabled, a free-text reply such as
*"Given Sam needs wheelchair-accessible spots, let's pivot toward the
Baixa flats…"* is delivered to the group verbatim — no Haiku launder,
no Sonnet recovery, no identity check, no constraint-topic check. The
entire structural-privacy guarantee the boundary advertises (`The
architectural goal: even if the model wanted to leak Maya's name, it
has no way to know who Maya is at the composition step.` —
`group_compose.py:24-25`) does not apply in the room where multiple
humans are first interacting.

**Repro / deterministic test idea:**
1. Create a `conversations` row with `conversation_type='group'`,
   `trip_id=NULL`, and 3 `conversation_participants`.
2. Seed user B with a hard constraint: `{constraint_type:
   "accessibility", value: "wheelchair access"}` and a PM line
   `"can't afford expensive dinners this trip"`.
3. Call `handle_turn` with `turn.conversation_id` set, `turn.trip_id =
   None`, `conversation.conversation_type = "group"`, and a user
   message such as *"Where should we eat Friday?"*.
4. Assert that either (a) `result.composition_skipped` is True with the
   placeholder, OR (b) the final `reply_text` contains zero matches
   from `find_identity_leaks(reply_text, member_display_names)` AND
   zero matches from `find_constraint_leaks(reply_text,
   constraint_values, constraint_types)`. Today neither check runs —
   raw `loop_result.text` ships.
5. Stronger version: assert that for every reply produced in a
   `conversation_type='group'` thread the `_resolve_final_reply_text`
   ↔ `compose_group_message` mapping is invoked regardless of
   `has_trip`.

**Suggested fix direction:** drop the `has_trip` half of the gate.
Either (a) extend `compose_group_message` to accept conversation-scoped
contexts — feed `intent_scratchpad` + participant_count where it
currently reads `trip_summary` + `group_legibility`; the constraint
and identity checks work without a trip row — or (b) treat pre-trip
group rooms as a special case where the runtime forces the concierge
into a narrow safe-reply mode (no synthesized preference reasoning,
no PM access until promotion). Option (a) preserves the product
behavior; option (b) is simpler if pre-trip rooms don't need the rich
recommender. Either way, `is_group` alone should arm the privacy
boundary; `has_trip` is a planning-state signal, not a privacy signal.

**Confidence:** High.

### [P1] — Mock client still returns the literal chip text (`"I'm in"`) as the privacy-preserving summary

**References:**
- `Travel App/utils/api/mock.ts:1283` (`answer_summary: "I'm in"` in mock notification feed)
- `Travel App/utils/api/mock.ts:2699, 2711` (`pending_intake_summary: "I'm in"` in mock invite list)
- `Travel Agent/backend/core/models/trip_invites.py:203-222` (real backend now returns `PRIVATE_INTAKE_SUMMARY = "Answered privately"`)
- `Travel App/__tests__/data/notifications.test.ts:201,236,275` (tests now assert `'Answered privately'`)
- `Travel App/data/notifications.ts:90-92` (renderer wraps `answer_summary` in fancy quotes — the bell body for the mock build is *"I'm in" · Maya 30 — Lisbon*, recreating the exact leak the prior P0 closed at the backend)
- `Travel App/app/trip-info/index.tsx:421-423` (renders `pending_intake_summary` in the Pending invites row — mock build will read `"I'm in"`)

**Why it matters to a real tester:** the dogfood-readiness charter
specifically lists *"mock/real drift"* as a launch-blocking risk
class. The backend P0 that landed `summarize_pending_intake →
"Answered privately"` is undone in any code path that runs with
`EXPO_PUBLIC_USE_MOCK_API=true` — preview builds, PR review videos,
designer screens, smoke tests. Worse, the mock is what reviewers
treat as the spec when they ask *"what should this render?"*; a
future engineer reading the mock can plausibly conclude the
backend's neutral string is the regression and revert it.

**Repro / deterministic test idea:** add a workspace mock-parity
check (or extend `make mock-real-parity`) that greps
`Travel App/utils/api/mock.ts` for any `answer_summary` or
`pending_intake_summary` literal that isn't either `null` or
`"Answered privately"` (the backend constant). Fail the suite when a
non-matching literal appears.

**Suggested fix direction:** swap the three mock string literals to
`"Answered privately"`, then add the parity grep above (or a typed
constant imported from a shared module so the strings can't drift
independently). Optional: have `make doctor` warn when a mock string
diverges from a backend `PRIVATE_*` constant by simple-name match.

**Confidence:** High.

### [P1] — `group_compose` constraint-leak detector has no patterns for budget / fatigue / medical, the very vocabulary the proposal redactor catches

**References:**
- `Travel Agent/backend/concierge/group_compose.py:228-344` (`_CONSTRAINT_LEAK_TYPES` covers only `accessibility`, `dietary`, `allergy`)
- `Travel Agent/backend/concierge/group_compose.py:921-955` (output validator only invokes `find_constraint_leaks`, which only fires for `constraint_values` + `constraint_types` extracted from `hard_constraints` rows)
- `Travel Agent/backend/preference_engine/synthesis/group_synthesizer.py:115-122` (the `_CONSTRAINT_TYPE_TO_PRIVACY_DIM` map confirms the live constraint-type enum: `allergy / dietary / medical / accessibility / language / visa` — no `budget`, no `fatigue`; both axes typically live in PM narrative, not in `hard_constraints`)
- `Travel Agent/backend/concierge/privacy_redactor.py:80-104` (the *proposals* redactor explicitly covers `budget`, `fatigue`, and `medical` keyword classes — proving the topic vocabulary exists and is enforceable, just not at the compose seam)

**Why it matters to a real tester:** a member whose private PM says
*"can't afford expensive dinners"* or *"completely drained after the
overnight flight"* sees the concierge compose to the group, *"I went
budget-friendly so we don't blow the trip on one night"* or *"a slower
Saturday — sounds like the group is wiped"*. Today `find_constraint_leaks`
returns `{}` because no row of type `budget` / `fatigue` exists, so the
output ships. The signal is exactly the kind the existing
`privacy_redactor` already understands — the asymmetry between
`propose_change` (catches it) and `compose_group_message` (doesn't) is
both surprising and exploitable.

**Repro / deterministic test idea:**
1. Build a `CompositionContext` with `aggregated_constraints=None` and
   `constraints_by_user={}` (no hard-constraint rows).
2. Call `execute_compose_group_message` with `intent="propose a
   budget-friendly Friday near the hotel because the group is exhausted
   after the overnight flight"`.
3. Assert the returned JSON is an error (`constraint_topic_in_output`
   or new `private_pattern_in_output`), not a `{"message": ...}`.
4. Today the call returns `{"message": "Friday: budget-friendly spot
   near the hotel, easy night to recover."}`.

**Suggested fix direction:** import
`privacy_redactor._PRIVATE_KEYWORD_PATTERNS` (or a shared module) and
run both the intent and the composed output through the *full* pattern
set, not just the value/type-keyed one. The proposals path already
runs both layers — pull the shared bits out so the privacy guarantee
is the same across every group-facing seam.

**Confidence:** High.

### [P1] — Public profile `interests` array is filled by an LLM extractor with no privacy allowlist; constraint phrases can land in the public payload

**References:**
- `Travel Agent/backend/concierge/refresh_memory.py:170-197` (`_TASTE_EXTRACT_SYSTEM`: *"interests_strong: concrete activities/topics they explicitly love"* — no negative examples, no constraint-omission rule)
- `Travel Agent/backend/concierge/refresh_memory.py:200-214` (`_extract_taste_dimensions` writes the result into `taste_dimensions`)
- `Travel Agent/backend/api/routes/profiles.py:31-44` (`PublicProfile.interests` ← `dims.get("interests_strong", [])[:6]`, returned by `GET /api/users/{user_id}/profile`)
- `Travel App/app/profile/[userId].tsx:106-114` (renders each interest as a chip on the public profile screen)
- `Travel Agent/backend/api/routes/users/me.py:116-170` (`reflection_phrases` are mapped through curated dicts and are safe — `interests` are not)

**Why it matters to a real tester:** the prior audit's framing is
*"Backend serves only public-safe content (no constraints / budget /
health)"* — `profiles.py:7-11`. That's true for the curated
`reflection_phrases` path; it is **not** true for `interests`. An LLM
given a PM containing *"kosher only"*, *"needs wheelchair access"*,
*"sober now"*, *"anxious in crowds"*, *"recovering from a meniscus
tear"* will plausibly return `interests_strong: ["kosher dining",
"wheelchair-accessible venues", "sober travel", "low-anxiety spaces",
"low-impact walking"]`. Those chips then appear on the user's public
profile to every viewer (the profile only requires
`public_profile_enabled` and any authenticated viewer).

**Repro / deterministic test idea:**
1. Seed a PM whose narrative mentions five typed constraints (allergy,
   accessibility, dietary, sobriety, mental-health framing).
2. Run `_extract_taste_dimensions` against it.
3. Assert no item in `interests_strong` / `interests_mild` matches a
   dictionary of constraint-topic stems (the union of
   `_CONSTRAINT_LEAK_TERMS` values plus `_PRIVATE_KEYWORD_PATTERNS`
   regexes from the proposals redactor).
4. Convert any hit into a filter applied in `_build_reflection_phrases`
   or in `_build_profile` itself — defense in depth.

**Suggested fix direction:** add a "never include" allowlist to
`_TASTE_EXTRACT_SYSTEM` and a server-side filter on the read side in
`profiles._build_profile` (so an existing cached `taste_dimensions`
blob with bad entries doesn't keep leaking until the next memory
refresh). Same redaction pattern as `find_constraint_leaks`.

**Confidence:** Medium-High (the LLM's behavior depends on prompt
phrasing; the structural risk is real).

### [P2] — Group-profile aggregated constraints become deanonymizing in 2-person trips

**References:**
- `Travel Agent/backend/concierge/group_compose.py:546-573` (`_aggregate_constraints` emits literal `"1 wheelchair access"` lines)
- `Travel Agent/backend/preference_engine/synthesis/group_synthesizer.py:142-158` (renders structured constraint lines per anonymized traveler — even though the labels are `Traveler 1`/`Traveler 2`, the LLM is encouraged in the system prompt to identify *"the strictest dietary need, the lowest budget ceiling, accessibility requirements"*)

**Why it matters to a real tester:** when a couple shares a trip (group
size 2) and one partner has a wheelchair-access constraint, every
group-facing artifact that surfaces *"1 wheelchair access"* or *"the
group includes one wheelchair user"* effectively names the wheelchair
user — the other partner already knows it isn't them. The composer
itself never repeats the topic (output validator catches it), so this
is a P2 not a P0; but the *input* path that the planner consumes (and
that any future operator dashboard reading aggregated_constraints
might also consume) does carry the deanonymizing facts as text.

**Repro / deterministic test idea:** for `member_count <= 2`,
substitute count-based aggregations with a coarser shape (`"this trip
carries 1 accessibility constraint"` rather than the value, OR collapse
to a binary `has_accessibility=True` signal). Add a unit test that
asserts `_aggregate_constraints({uid_a: [Constraint("accessibility",
"wheelchair access")], uid_b: []})` does not include the literal
value `"wheelchair access"` when `member_count == 2`.

**Suggested fix direction:** for small groups, fall back to topic
buckets without the stored value (`accessibility: 1`, not
`accessibility: 1 wheelchair access`). The composer prompt already
knows not to repeat the topic word; remove its ability to *infer* the
specific value when only one member could be the source.

**Confidence:** Medium.

### [P2] — `trip_events.invite.intake_received` payload stores raw chip / free-text intake; no current public surface, but no privacy attestation either

**References:**
- `Travel Agent/backend/api/routes/invites.py:746-771` (`append_trip_event(..., payload={"intake": payload, ...})` — `payload` is `body.model_dump(exclude_none=True)`, i.e. the raw `chip_answer` / `free_text`)
- `Travel Agent/backend/core/db/plan_events.py:83-112` (`get_trip_events` exposes a generic reader keyed by `trip_id` — no current API caller, but the function is general-purpose)
- `Travel Agent/backend/core/models/trip_invites.py:171-176` (invitee can submit `free_text` up to 1000 chars; this is the same input the previous P0 banned from organizer-facing notifications)

**Why it matters to a real tester:** the prior P0 closed the
organizer-facing render path but left the underlying storage
unchanged. `trip_events` is the canonical journal — any future
"organizer audit log", "trip activity feed", or admin debugging
endpoint that reads `get_trip_events` will surface the raw answer
verbatim. The architectural promise to invitees (*"answers go to the
Concierge, not the group"*) extends to internal surfaces too: the
journal is the wrong place to store that text. Defense in depth.

**Repro / deterministic test idea:** add a regression test that
`get_trip_events(trip_id, event_types=["invite.intake_received"])`
returns rows whose `payload` does NOT contain the substrings
`chip_answer` or `free_text` keys with raw values — only a digest /
length / category-shape.

**Suggested fix direction:** in `submit_intake`, replace the
`"intake": payload` storage with a structured digest:
`{"chip_present": bool, "free_text_present": bool, "length":
len(free or "")}`. The Concierge already gets the raw intake via
`invite.pending_intake` JSONB (different table, owner-scoped) when
accepting; the event journal does not need it. If audit is required,
add a separate owner-only `invite_intake_audit` row that the existing
audit endpoint can opt into.

**Confidence:** High (storage shape clear; absence of public surface
today is fortunate, not designed).

### [P2] — `follow_affinity.follower_count` can leak which specific followed user engaged when the count is 1

**References:**
- `Travel Agent/backend/core/personalization/follow_affinity.py:55-62` (`FollowSignal{score, follower_count}`)
- `Travel Agent/backend/core/personalization/follow_affinity.py:190-198` (per-entity result counts distinct engaging followed users)
- Consumers (Discover for-you blend) surface a *"N people you follow saved this"* callout off the score + count.

**Why it matters to a real tester:** if a viewer follows 50 people and
only one of them, Alice, has a strong vegan taste signal, a callout
on a niche vegan venue with `follower_count=1` lets the viewer infer
"that was Alice." With a small follow graph this becomes a structured
attribution channel that the engaging user did not consent to. This
is a side-channel, not a direct leak; rate-limit class P2.

**Repro / deterministic test idea:** in
`compute_follow_affinity`, when `len(users) < K` (K=2 or 3),
either suppress the signal entirely or downscale `follower_count` to
`>= K`. Add a test that for a viewer with `following=50` and a niche
exemplar with only 1 engaging followed user, the returned
`FollowSignal` is either absent or reports a bucketed count.

**Suggested fix direction:** ship `follower_count >= 2` as a hard
minimum for surfaced signals; below that, treat as no signal. Adds
near-zero quality cost (one-follower-saved-a-niche-place is a weak
signal anyway), removes the inference channel.

**Confidence:** Medium.

### [TECH-DEBT] — `list_followers` / `list_following` are not `require_self`-gated; social graph readable regardless of `public_profile_enabled`

**References:**
- `Travel Agent/backend/api/routes/follows.py:88-120` (`list_following` and `list_followers` take any authenticated user via `_actor: User = Depends(get_current_user)`; no `require_self` and no opt-in check)
- `Travel Agent/backend/api/routes/follows.py:127-140` (`social_feed`, by contrast, uses `require_self(user_id, actor)`)
- `Travel Agent/backend/api/routes/profiles.py:55-59` (the public profile itself is gated on `target.public_profile_enabled`)

**Why it matters to a real tester:** a user who has explicitly set
`public_profile_enabled=False` (private profile) still has their
followers/following enumerable by any authenticated user. Not a
private constraint leak per se, but inconsistent with the explicit
opt-in elsewhere — and the social graph is itself sensitive
metadata (who you follow can imply taste / location / orientation).

**Suggested fix direction:** require the target to either be `self`
or `public_profile_enabled=True` before returning followers/following.
Same opt-in test the profile route already uses.

**Confidence:** High.

### [TECH-DEBT] — Trip Story composer has no privacy rules in the system prompt; relies on the owner to preview before sharing

**References:**
- `Travel Agent/backend/tasks/trip_story.py:46-107` (`_COMPOSER_SYSTEM_V1` — voice, structure, anti-marketing rules; nothing about constraint vocabulary)
- `Travel Agent/backend/tasks/trip_story.py:143` (`get_active_observations(user_id, ..., limit=7)` — observations can include any free-text fact, including health/budget/mood)
- `Travel Agent/backend/core/story_projection.py:90-128` (the public projection allowlist is structural — sections / photos — but does not redact *within* a section body)
- `Travel Agent/backend/core/story_projection.py:131-171` (`build_share_preview` is the *only* user-facing line of defense — relies on the owner to read what's exposed and toggle visibility)

**Why it matters to a real tester:** the composer is told to write
"warm, specific travel writing about THIS person's THIS trip", takes
the user's own observations verbatim, and can produce section bodies
like *"You spent most of Saturday at the hotel because the migraine
came back hard."* — true, the owner's own data, but the story is
public when shared. The Privacy Preview is the contractual safety
net; the audit observation is just that it is the ONLY net.

**Suggested fix direction:** add a "Privacy" paragraph to the system
prompt that explicitly bans health/budget/medical/accessibility
vocabulary unless the owner ALREADY referenced it in the trip's
`overall_arc` (which the owner can edit before sharing). Optionally
re-use `privacy_redactor._PRIVATE_KEYWORD_PATTERNS` at section
write-time, marking flagged sections `hidden_by_default=true` in
the redaction policy.

**Confidence:** Medium.

---

## Known / Accepted (not new findings)

These were already documented or fixed prior to this audit; re-stating
to prevent re-discovery as findings.

- **Invite intake organizer-facing summary collapsed to "Answered
  privately"** — `core/models/trip_invites.py:203-222`; closed by the
  2026-05-21 dogfood-readiness P0 fix (`docs/audits/pre-dogfood-2026-05/
  dogfood-readiness.md` §"P0 — Invite intake answers are exposed to the
  organizer..."). The backend path is now neutral; the mock-mode
  duplicate of the leak is filed above as P1.
- **Raw invite tokens routed through `_token_fp` fingerprint in logs
  and event payloads** — `core/api/routes/invites.py:746-771` (line
  757 uses `_token_fp(token)` rather than the raw token); closes the
  same audit's *"Raw invite bearer tokens are logged and persisted..."*
  P0.
- **Personal Memory narrative withheld from group synthesis when a
  member sets any privacy dimension to `private`** — `group_synthesizer.py:179`
  via `should_omit_personal_memory_narrative_for_group_synthesis`;
  also withholds the structured constraints in the privacy-mapped
  dimension. This is the *baseline* privacy gate the audit recommends
  porting to `invite_snapshot` (P0 above).
- **Group-facing message composer strips identity and constraint-topic
  vocabulary on output, with Haiku auto-launder + Sonnet recovery +
  placeholder fallback** — `concierge/group_compose.py` +
  `concierge/strict_compose.py`. Strong default-deny for trip-scoped
  group rooms; the P0 above is specifically about the pre-trip hole.
- **Story-projection default-deny + photo-allowlist** —
  `backend/core/story_projection.py:74-128` and
  `backend/core/db/trip_story_shares.py:494-529`; only owner-marked
  `group` / `group_and_learn` photo URLs survive the public projection.
- **Public profile only surfaces curated `reflection_phrases` and
  `interests`** — opt-in via `public_profile_enabled`; the
  `reflection_phrases` half is curated-vocab safe. The `interests`
  half is filed as P1 above.
- **Notifications-feed `PendingInviteAnswer.invite_token`** is a
  fingerprint, not the raw bearer token — `_notifications_feed.py:22-26`
  and `_invite_token_fp` usage at line 206.
- **`O-11 Private-channel constraint echo`** — `Known Gaps Register.md`
  §O-11; whether the agent can repeat a constraint back to the user
  in a private channel is an open product question, not a defect.
- **`S-5 Venue allergen enforcement — only gluten filterable`** —
  Known Gaps S-5; the data-shape gap is owned by the search/retrieval
  area, not this one.
- **`G-11 Inviter visibility v2`** — push/SMS dispatch on intake
  composes *"Sam answered your invite privately"* (no chip/free text);
  see `invites.py:789-851`. Acceptable.
