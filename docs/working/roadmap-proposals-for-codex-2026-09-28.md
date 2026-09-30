---
doc_type: working
status: active
owner: Claude orchestrator, for the program roadmap owner (Codex lane)
created: 2026-09-28
last_verified: 2026-09-29
expires: 2026-10-12
why_new: The program roadmap belongs to the codex/home-value-delivery lane, and other sessions do not edit it directly. These are proposed changes from the September 24–28 strategy thread, for the lane owner to accept, adapt or decline.
promotes_to: docs/working/vesper-program-roadmap.md (by the lane owner)
supersedes: []
source_of_truth_for: []
---

# Roadmap proposals for the Codex lane (September 28)

**Scope.** These proposals were checked against the roadmap as it stood in
`travel-workspace--home-value-delivery` at workspace `47c91b3` on September 28:
queue items 0–3, with the capture/share package active. They are proposals. The
lane owner decides, and the founder rules where a proposal needs a ruling.

**September 29 documentation recheck:** the execution roadmap at workspace
`af8f4912` still names the September 26–27 decisions as its imported baseline.
This confirms a handoff gap, not that the implementing code was re-reviewed or
that the work should restart. The research-to-execution refinements are in §8.
Earlier deployment, signing, provider and latency observations below retain
their original dates and need current verification before action.

The September 29 evening artifact investigation is in §9. It supplies proposed
package boundaries and acceptance cases, not a new current-state review of the
execution lane or an instruction to interrupt its active work.

The [detailed artifact engineering roadmap](artifact-experience-engineering-roadmap-2026-09-29.md)
now expands §9 into shared contracts, eight dependent packages, migration,
quality and lifecycle replay, decision boundaries and complete assignments.
Its September 29 delivery-lane baseline is explicit. It is a supporting plan
for the program owner to admit, not another dispatch queue; the earlier
uncompleted proposals below remain intact.

**Background.** The reasoning is in
[product direction, September 24–28](product-direction-2026-09-28.md). Two
decisions are new since the roadmap was rebaselined:
- [Collections are the spine](../decisions/2026-09-28-collections-are-the-spine.md)
- [One way in: doors, things and a connected inbox](../decisions/2026-09-28-ingestion-and-connected-inbox.md)

## 1. Bring the two September 28 decisions into the capture/share boundaries

The roadmap's "Capture/share package boundaries" already follow the September
26 and 27 records. The two new records change these parts:

- **The email door is a connected inbox.**
  - Forwarding stays as the fallback where no API exists (iCloud Mail) and for
    people who prefer it. The current forwarded-email Keep work is therefore
    still useful. Finish it as the fallback, and do not grow forwarding UI
    beyond that.
  - The connected-inbox adapter is new work:
    - OAuth;
    - filter before reading;
    - keep only matches;
    - a record of which emails were read and kept, in the inbox's settings;
    - disconnect deletes what was read but not kept.
  - A booking is filed as the person's only when it names them. Use
    schema.org reservation markup (`underName`) where the email carries it.
  - Partial scope grants from Google's granular consent must work.
  - Until Google's policy on showing Gmail-derived items to others is
    confirmed, inbox-found things stay private, even in shared collections.
  - The adapter depends on Google verification (§5).
- **Doors and things are separate.** Replace the six-door map with this door
  list: the OS share sheet, inside Vesper (camera, photos, add, Keep/Send on an
  object), Chat, the connected inbox, and a friend. A Wallet pass arrives
  through the share sheet.
- **Merge only repeated captures of the same material.** One ticket through
  email and a screenshot becomes one artifact that lists both sources.
  - Two visits to one restaurant, or a friend's recommendation and the
    person's photograph of the same place, are related but never merged.
  - The existing retry identity (`owner_id`, `idempotency_key`) deliberately
    refuses content hashes as identity, and that should hold.
  - Cross-door merging belongs in the shared intake contract, not in each
    door.
- **Where things land.**
  - A kept thing joins its kind collection silently, with Undo.
  - It enters a shared collection only when its author adds it.
  - Membership is many-to-many between Capture's typed artifacts and a
    collection owner. No owner exists yet: the backend `collections` table
    serves the editorial Discover guides. Identify the owner in the
    implementation map rather than renaming that table or improvising in
    a root.
- **Where people hear.**
  - Friends' actions arrive as notifications.
  - Vesper's own filing is never narrated: no notification, no "filed" list
    and no status bar on a collection (ingestion decision, item 7). Where a
    thing is, and changing it, belong to the thing's own page.
  - Whether found items send any notification is pending. The current boards
    send none.
  - There is no Updates feed.

  A notifications surface is therefore a dependency of the package's "refound
  and later value" conditions. Its policy (batching, quiet hours, push versus
  in-app) is still pending a founder ruling, so build the owner and hold the
  policy.

The friction proposal (save on share, filing when confident instead of asking,
and corrections on the thing's own page) is drawn on I0 and I1 and is not
ruled. It is worth keeping in mind for the share extension's receipt, because it
would remove the in-sheet Keep tap.

Still excluded, as the roadmap already says:
- R1–R5;
- the friction proposal;
- the ingestion defaults drawn on I0;
- whether Vesper may add to shared collections on its own.

## 2. Make the send-time payoff a measured finish condition

The author should receive a recognizable useful thing where they contributed
it. About two seconds is an unmeasured target, not an established service promise.
The September 27 observation placed semantics and anchors on a once-a-minute
pipeline; recheck the current path before treating that as today's bottleneck.

**Proposed:**
- Add p50 and p95 time-to-payoff for five share types to the capture/share
  finish condition: a place link, a screenshot, a photographed menu, a ticket
  and a book.
- Measure on the lane API before choosing between a synchronous recognition
  path and a designed waiting state.
- Record the numbers in the package's receipt.

## 3. Narrow Home's remaining gaps to what the loop needs

The roadmap already keeps Home's residuals (recovery option comparison, social
hierarchy, recurring supply) from blocking capture/share. **Proposed:** state
the Home exit the MVP needs, which is that Home shows what came back, from real
data, on a device. Treat full-scroll design parity and sustained supply as
later gates, not MVP gates.

## 4. Build profile and trust fixes before anyone else uses it

- **A dogfood build profile.**
  - The new shell is on by default and the legacy surfaces are hidden.
  - Trips, booking, Atlas and Discover are hidden, not deleted.
  - Include Sentry and PostHog.
  - On September 26 no EAS profile turned the four-root flags on; re-check.
- **The consent bug.** The newer composition path ignores `inference="none"`.
  Fix it before any friend's material reaches composition. A separate task was
  already suggested for this.
- **The booking default.** Set `BOOKING_EXECUTION_RETIRED=true` in deployed
  configuration. It was unset in `fly.toml` on September 26.
- **Background AI cost caps.** The product map found paid loops that
  `DISABLE_LLM_BACKGROUND_LOOPS` does not stop. Cap them before the next
  production deploy.

## 5. External prerequisites to start now

These need the founder. They are listed here so the queue does not wait on them
silently.

- **iOS signing and provisioning** for the in-place share extension. The Xcode
  team `QNZ5K23A74` differs from the local identity `J6ZKHAT2H7`, and the
  extension needs its App Group and Keychain entitlements.
- **Google OAuth verification for Gmail's restricted read scope,** including the
  annual CASA assessment.
  - The lane can draft the scope justification and the data-handling
    description.
  - Until verification, Google shows an unverified-app warning and caps the
    app at 100 new users (Google Cloud help, accessed September 28). That could
    carry a 20–30 person cohort through the warning screen.
- **The founder setup (about 45 minutes):**
  - the workspace CI token;
  - branch protection for a solo founder;
  - GitHub billing;
  - an Anthropic spend cap.

## 6. Ship path

**Date-based checks.** They begin failing on September 29 and block pushes, then
again on October 5, 6, 8, 9 and 12. Renew or convert to reports whatever has
not already been handled.

**Delivery closeout (queue item 0).** Close the published PRs, then deploy with
a rehearsed migration. Production ran August 14 code on September 26.

**Documentation size.** The roadmap was 217 lines on September 26 and is 399
lines on September 28. The proposal is to keep one evidence summary in H1 and
to stop committing docs after every slice, as the roadmap's own maintenance rule
already asks.

## 7. Landing note

Both this branch (`codex/product-direction-2026-09-28`) and the Home lane add:
- the September 26 and September 27 decision files, which are byte-identical;
- rows for them at the top of `docs/decisions/README.md`.

Identical files merge cleanly. The README table and its `last_verified` line
will conflict for whichever branch lands second. The fix is to keep both sets of
rows, newest first.

The September 29 Thesis/Model reconciliation is in a separate backend worktree
at this strategy lane's `travel-agent/`, branch
`codex/product-direction-2026-09-28`, based on `fdf789d06`. Do not replace
the implementation lane's newer canon wholesale: preserve its September 27
entrance amendments while applying the record-value and collection changes.
Carry the [September 29 record-value amendment](../decisions/2026-09-29-record-as-first-class-value.md)
and its index entry with those changes. Earlier accepted decision files are
unchanged; the new amendment is limited to product value and optional continuation.

## 8. Apply September 29 research to the collection experience

The [research synthesis](memory-as-product-direction-research-2026-09-28.md#14-september-29-collection-experience-follow-up)
and [direction refinement](product-direction-2026-09-28.md#13-september-29-collection-experience-refinements)
do not add an implementation queue or adopt pending defaults. The program
owner should map these requirements into existing packages at its next
checkpoint, while finishing useful capture work already underway.

| Concern | Owner boundary to preserve | Proposed acceptance evidence |
| --- | --- | --- |
| Collection formation | Source/capture identity, relationship evidence and collection membership are distinct; collections do not own reservation truth. | A relationship is useful without creating a new container; a noticed collection demonstrates a reason to persist before Keep. |
| Recognition and enrichment | Original, attributed human addition and generated interpretation retain separate provenance. | Compare a capable original-only treatment with a genuine enrichment winner, including attribution on delayed return. |
| Correction | Existing memory/contribution contracts resolve target, scope and authority. | One regrouping stays local; an explicit ongoing instruction affects its named class; neither widens sharing or action authority. |
| Home receiving | Retained value, eligibility, whole-page prominence and interruption remain separate. | A quiet ordinary week after dense travel delivers current value without recap dominance, capture homework or a mandatory task. |
| Life navigation | Stable item/collection identity and membership support views without copied records. | Refinding by partial person/time/place cues, an exact original, and a related-item detour with a clear way back. |
| Multiplayer continuity | Contribution, source-use permission, audience and withdrawal survive every view. | A mostly receiving friend gets value without equal effort; original voices survive later additions and source withdrawal. |

Use day 1 evidence, day 2 explanation and day 5 related material across these
cases. A map/list/time switch preserves scope; following a relation preserves
the return path; moving into asking, sharing or planning checks the new purpose.
Membership removal, deletion and revoked access have different effects.
Correctness and withdrawal outrank visual stability; preserve independent
material rather than treating the entire collection as invalid.

Distinguish the evidence layers: owner tests establish identity and repair;
connected readback establishes current projections; installed surfaces establish
interaction; voluntary behavior establishes preference or return. A fixture
or attractive collection screenshot cannot certify all four. Retain a sparse
everyday example and measure repeated repair/disorientation, not storage growth,
generation volume or raw override count.

No fixed item threshold, content ratio, retention target or push cadence follows.
In particular, the ingestion proposal's “correction applies to similar things”
needs the scoped clarification in the direction note, not automatic global
learning. The collections decision's notifications destination is not permission
to push. Keep friction presets, catalog mechanism and autonomous shared additions
separate from implementation of already accepted private organizing.

At the next package checkpoint, verify three outcomes: contribution is
dependable; the resulting personal/shared collection is worthwhile to have;
and later evidence improves it without avoidable repair. These are complementary
system checks, not a demand to stop engineering until one behavior loop is proved.

## 9. Focused artifact engineering proposals

**Detailed package plan:** use the
[artifact experience engineering roadmap](artifact-experience-engineering-roadmap-2026-09-29.md)
for implementation dependencies, ownership, acceptance and rollout. The A/B/C
map below remains the strategy-level summary; its package detail is expanded
there rather than copied into a second implementation backlog here.

The [focused artifact direction](product-direction-2026-09-28.md#14-september-29-focused-artifact-experience)
and [technical investigation](memory-as-product-direction-research-2026-09-28.md#17-september-29-artifact-engineering-investigation)
clarify the next experience: an appealing kept thing opens immediately, offers
substantive contextual value when available, and stays recognizable as its
relationships grow. The program owner should absorb the following into useful
existing packages at its next checkpoint. These are coordinated workstreams,
not three new services, an additional roadmap or automatic parallel dispatch.

The inspection used backend fdf789d06 and app 23cff76f4 on September 29.
Reconcile against the implementation lane's actual HEAD before scheduling or
repairing anything below. Current and earlier uncompleted handoff items remain
intact; this section does not report implementation, passing tests or launch
readiness. The [accepted Life decision](../decisions/2026-09-29-life-model-occasions-collections-and-sharing.md)
governs its named object/collection and sharing choices where earlier notes
conflict; artifact form, pending grants and defaults remain separately open.

### A Object and change contracts

Map source, artifact, component, subject, occurrence, collection membership and
derived relationship onto their existing owners. Establish consumer collection
ownership without repurposing editorial collections by implication or
duplicating reservation/commitment authority. Add reversible reconciliation
for multiple captures of the same thing while preserving separate occasions
and contributors.

Specify event versus received time, uncertain dates and timezone handling,
typed corrections, retry identity versus a new correction, and dependency
revisions. Recheck the inspected fact writer's freshness/validity coupling and
wrong-time correction behavior before making narrowly scoped repairs. This
is not a prerequisite for a database replacement or universal noun migration.

### B Stable focused artifact reading

Build on the current artifact and exact-result readers. Deliver the
recognizable object without waiting for generation, preserve original access
and return navigation, and distinguish a changing exploration from the exact
result deliberately kept. Use existing frozen/refreshable/live semantics.
Revalidate current authority and expiry even when an expression is frozen.

Recheck the result reader's stale-payload/action behavior, not just its
expired-state heading. Exercise timer passage while open, return from a
related object, permission change and provider failure. Honor whatever offline
policy is adopted; do not promise current remote revocation while disconnected.
Existing source and renderer plumbing can progress before exact visual
composition settles; its absence need not block all engineering.

### C Contextual discovery and delivery

Provide a selected-object context path through the existing engine. Combine
structured relationships, keyword/semantic retrieval and bounded relationship
expansion across authorized collections, people, current circumstances and
public evidence. Separate candidate discovery from judging supported value.
Reuse composition and practical-help owners; no fabricated Trip or required
Chat turn should be needed.

Prepare reusable results and public subject evidence selectively, with bounded
on-demand depth. Invalidate for corrected sources and newly available relevant
material, including previous no-result selections. Track all supplied source
dependencies, recheck before serving and preserve independent contributions
after repair. Shared public evidence does not make private composition a
shared cache. Budget reservations, concurrency deduplication and cancellation
are separate from caching.

The shared identity, context and revision contracts precede incompatible
implementation choices; B and C can then advance independently. Do not hold
unrelated capture, reader or reliability improvements until every research
question is settled. Jev or another fast judge is an optional experiment
within C, not a critical-path dependency. See [research §18](memory-as-product-direction-research-2026-09-28.md#18-september-29-bounded-decision-model-research).

### Shared acceptance portfolio

Use tickets, dish photographs, book passages and scorecards to exercise the
same system with different media and evidence. These are comparison cases,
not a commitment to four bespoke products or a fixed first-release catalog.

| Case | Required comparison or invariant |
| --- | --- |
| First contribution with sparse history | A recognizable, worthwhile object without forced classification, another contribution or generated filler. |
| Original versus enrichment | Include both an original-only winner and a supported addition that clearly improves what the person receives. |
| Day 1 evidence, day 2 explanation, day 5 related material | New value without changing original authorship or confusing event time with upload time. |
| Same ticket, another location or purpose | Relevant selection can change; retained identity, event facts and an actively read result do not silently drift. |
| Related-object detour and exact kept explanation | Return to the originating selection; reopen the kept version without rerunning current ranking. |
| Local correction and another later correction | Distinguish new edits from retries; repair only their dependencies and preserve explicit membership exclusions. |
| Shared contribution withdrawn during generation | Resolve AI-use grants before context assembly, recheck before serving, and invalidate affected derivatives. |
| Cold/warm open, offline or provider failure | Independently eligible retained value remains usable; no stale practical actions or fictitious freshness. |
| Repeated opening without relevant change | No manufactured novelty or compulsory new model work; a complete original remains satisfactory. |

Measure object recognition, added value, attribution, false novelty/suppression,
retrieval recall, interaction/return, repair, p50/p95 and end-to-end cost.
Separate automated correctness, connected readback, installed interaction and
voluntary preference evidence. Reuse existing editorial and lifecycle
evaluations rather than introduce a second evaluation platform.

### Checkpoints and unresolved choices

At contract mapping, resolve any consequential owner or sharing ambiguity
before implementing its effect. At the first connected reader/discovery
result, inspect the whole experience and total latency, not isolated model
quality. At the repeated-use checkpoint, assess new evidence, return,
correction, withdrawal and spend; adapt the package when failures reveal a
wrong abstraction rather than adding receipts for an unchanged gap.

Still open: focused layout and density, initial family coverage, preparation
budgets and refresh cadence, offline retention, and what happens to a kept
explanation or mixed-contributor Occasion after withdrawal. The general rule
that things leave with their contributor does not by itself settle every
composite case. A cheap model's score cannot resolve these product choices.
Do not impose the current Home producer's two-source novelty or cross-root
output requirements on all artifacts. Document adopted refinements in their
existing owner contracts; the active program roadmap retains sequencing.
