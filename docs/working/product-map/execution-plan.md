---
doc_type: working
status: active
owner: Claude orchestrator (product map)
created: 2026-09-26
expires: 2026-10-26
why_new: Turns the measured gap map into an ordered set of packages, founder actions, decision sessions and an operating cadence, proposed as amendments to the program roadmap rather than a second queue.
promotes_to: null
supersedes: []
---

# Execution plan: getting Vesper across the line

This is a **proposal**. [`vesper-program-roadmap.md`](../vesper-program-roadmap.md) stays the only dispatch queue; §7 lists the edits this plan asks for there. The plan rests on the measured [gap map](gap-map.md): about 60% of the designed product is built, a third can be reached in an installable build, and almost none of it has been delivered.

## 0. The strategy in five lines

1. **Delivery first.** Get the current product onto your phone, running against a current production backend, and keep it there daily. Nothing else is judged honestly until then.
2. **Decisions before builds.** 15 of the 20 unbuilt capabilities, and every "shared" capability that is built but switched off, wait on your rulings. Eight proposals lapse on Oct 6–7.
3. **Trust before audiences.** Enforce the contribution contract, and fix the relationship privacy defects, before any friend's material or shared audience is switched on.
4. **Supply in parallel.** One real neighborhood, starting now. It is editorial work, and it gates whether Home and Places feel alive.
5. **Then whole-but-thin slices**, each accepted on your device:
   - **send to Vesper** (just you): the primary mode you agreed on Sep 26;
   - a friend's place, end to end;
   - an evening together;
   - Vesper prepares something from what you sent.

"Done" means something new in this plan: merged, deployed, **on your phone**, tried against production, with one screenshot or log line. See §5.

## 1. Calendar for the next two weeks

| When | What | Who |
|---|---|---|
| **Sat Sep 26 – Sun Sep 27** | Founder checklist part A (§3): CI token, branch protection, billing limit, spend cap. Decision session 1 (§4). | You |
| **Sun Sep 27 – Mon Sep 28** | P0 lane opens. Its first commit neutralizes the date gates **before the Sep 29 flag failure**, which also blocks every workspace push, including Codex's. | Agent |
| **Mon Sep 28** | M1 retired on record (D27). | You |
| **Tue Sep 29 – Thu Oct 1** | P0 safety pack merged. Migration rehearsal on a copy of production. Backend deploy. `founder` build installed on your phone. | Agent prepares, you execute the privileged steps |
| **Oct 1 onward** | H1 acceptance moves to your phone against production. Daily OTA to the `founder` channel. | Codex (H1), you (walks) |
| **By Oct 5** | Decision session 2 (§4): the social, Life, Chat and Live packs, before the Oct 6–7 lapses. | You, with my prepared recommendations |
| **By Oct 8** | Here/Season catalogue renewed for the first neighborhood (it expires Oct 9). Red Hook readings landed. | You (curation) + agent |
| **After H1 exit** | Pick the next package from the evidence. Default: F0 "Send to Vesper", with supply continuing. | Me (recommendation), you (approval) |

## 2. Packages

Each package has one owner, a file-ownership boundary, acceptance on a device, and a rule to land daily.

### P0: Ship path (new; starts now; second lane, files separate from H1)

**Outcome.** Everything already built reaches your phone against a current backend, and `main` stays green without anyone tending the calendar.

**Owner.** One implementation lane, `codex/ship-path`. It touches only:
- CI and workflow configuration;
- governance scripts and registries;
- `eas.json`, `app.json` versioning and `fly.toml`;
- the backend safety files listed below;
- one app file for the doorway gate.

It does **not** touch Home, Places or Life renderers or projections. Those belong to H1.

**Scope, in landing order:**

1. **Date gates become reports** (infra R4). Must land before Sep 29.
   - Flag registry, API-policy expiry, compatibility ledger, bridge expiry, world-catalogue runway and design-gate calibration each warn and exit 0.
   - Remove the flag check from the workspace pre-push hook.
   - Add one weekly `governance-debt.yml` that updates a pinned issue.
   - Renew the 55 API operations and 36 flags **once, in bulk**.
2. **CI to green** (infra R2).
   - Move the catalogue check out of the backend `test` job.
   - Make `design:status` a generated artifact.
   - Remove the dead `schedule:` triggers: `cron.yml`, the AI canaries and `visual-qa`.
   - Add a docs-only path filter with no-op jobs that keep the required check names.
3. **Safety pack for the deploy.** Every item in this list must be merged before `main` is deployed.
   - `BOOKING_EXECUTION_RETIRED="true"` in `fly.toml`. This closes Bland.ai restaurant calls and provider checkout.
   - Put `seed_city_full` and `warm_experience_brief` behind the kill switch, and turn them off by default. They are the ~$800/day ceiling fed by empty chat searches.
   - Make `background_llm_enabled()` a check inside `call_llm` for every background surface, so the kill switch is real.
   - Cap fan-out for Takes on `trip.completed`, cross-trip threads and guide prerender. Stop re-claiming guide rows while the TTS key is absent.
   - Put `saved_place_reopen_scan` behind a flag, off.
   - Stop `story_backfill` (Wave 0; it costs money and nothing reads it).
   - Set `DISABLED_SURFACES` for guide narration and transport nudges until H1 needs them.
   - Require admin auth on `/health/background-tasks`.
   - Fix the two advisory-lock key collisions.
   - In the app, gate "Leave this place for someone" on `RELATIONSHIP_UUID_HANDOFFS_ENABLED` (C15).
   - Remove `EXPO_PUBLIC_ADMIN_API_TOKEN` from the EAS preview environment. You rotate the backend token.
4. **A `founder` EAS profile** (infra R1 §4). It turns on:
   - the four-root shell, v2 projections, the Places v2 renderer and Life;
   - Life refind and the object-page rebuild;
   - crash reporting, with the Sentry DSN in the EAS environment.

   Also: bump the app to `1.1.0`, or set `runtimeVersion: {policy: "fingerprint"}`, so no older binary can receive an incompatible OTA.
5. **Migration rehearsal and deploy.**
   - The agent writes the script: `fly postgres fork` or a `pg_dump` copy, then `alembic upgrade head` and the `test-db-migrate` checks, then `/ready`.
   - You run it with Fly access, authorize the deploy and run `make deploy`.
   - Then set on Fly only the backend flags H1 needs. Relationship and handoff flags stay **off** until T1 lands.
6. **Build once.** Run `eas build -p ios --profile founder` and install it. After that, JavaScript ships daily with `eas update --channel founder`.

**Acceptance, all on evidence:**
- Production `/ready` reports the merged SHA.
- You open the `founder` build on your phone and see Home, Places and Life running against production.
- **The Chat root shows its composer.** The simulator run found it blank in every build tried ([runtime](build-map-runtime.md)). If it is still blank on the new binary, diagnosing it becomes P0's first fix: the main way into Chat is unusable without it.
- One screenshot per root, attached to the PR.
- A Sentry test event arrives.
- The next scheduled date passes without red CI.
- The workspace pre-push works on Sep 29.

**Size.** About 3–5 working days of agent time, plus about 1–2 hours of yours across the privileged steps.

### H1: Complete Home value delivery (existing; Codex; continue)

H1 is on a sound path. Four adjustments:

1. **Accepted references (D26).** When you rule, register the recommended set in the Home contract and QA surface:
   - 02 top scrolls (ordinary and quiet)
   - 03 (post-return, return after absence, trip day as composition reference)
   - 18 K, and 18 L for large text
   - 08 row three
   - 09b
   - 17

   Live lane D waits on D24. H1 "healthy live" is judged against 03 TRIP DAY plus the contract's "Live is not attention protection".
2. **Acceptance moves to your phone once P0 lands.** Walk the three H1 situations on the `founder` build against production with your own account:
   - ordinary day;
   - an evening with other people;
   - a healthy live situation.

   Fixture and simulator captures remain the pre-walk (`device_mock`), not acceptance. The "other people" situation needs a second real account and the relationship flags, so it waits on T1. Until then it is accepted on the local-owner rehearsal and marked as such.
3. **Native dependency gate.** Commit `aa3e235d6` moves `react-native-reanimated` to 4.2.1 and `react-native-worklets` to 0.7.4, the pair Expo SDK 55 bundles. It needs a clean native build and a device run recorded in its PR before merge. After that, P0's `founder` build is the one binary. Coordinate so the `founder` build happens *after* this lands, and only one rebuild is needed.
4. **Cadence.**
   - Land H1 to `main` daily behind its existing flags.
   - At most one doc commit per landed slice. Evidence goes in the PR.
   - H1's exit record replaces the running receipt in the execution plan.

**H1 exit, as I recommend it:**
- The three situations have been walked on your phone. For "other people", that is the local-owner rehearsal until T1.
- The accepted references are compared first viewport and full scroll, with the differences listed.
- The Oct 9 catalogue has been renewed, so Home is not Quiet by default.
- Everything is merged.

### R0: Runtime defects (a short task after P0; about 2–3 days)

These come from the simulator run ([runtime](build-map-runtime.md)). Each one breaks a promise the design makes. The item that changes Home files goes to H1; the rest go to one small follow-on task.

- **Ask Vesper sends a message on your behalf without review.** This happens on the place page and on the legacy Plans chat button. Change it to a draft you send.
- **Home → Ask Vesper loses the card's context.** This goes to H1.
- **Life lenses don't reorganise**, and the record entry says "no longer available".
- **Retired names in the four-root build:** "Trips", "Atlas", "Discover", "Ready for Atlas", and the notification filters.
- **The rebuilt place page:** remove internal labels, align the actions, and add the E06 plate, byline and closing row.
- **The QA harness:** registered Maestro flows wait for tab labels that no longer exist.
- **Merge the backend offline-start fix** (`6c792ed8b`, in the H1 lane), so the baseline starts without an API key.

### T1: Trust enforcement (new; backend; after P0 step 3; before any shared audience)

**Outcome.** The trust promise holds in code. A plain Ask cannot quietly change durable or shared state. Friends' material cannot leak beyond its grant.

**Scope.** Citations are in [backend §6.6 and §8](build-map-backend-static.md).
- **Confirmation before these writes:**
  - `set_location_sharing` (structured-only);
  - the `trip_accommodation_set` shared expense projection (structured-only, or `expense_log` evidence);
  - `fact_remember` visibility (default private; `group` only on explicit evidence).
- **Planning brief and member briefs:**
  - channel check: no 1:1 content lands in trip-shared documents;
  - a test that proves whether private member-brief content reaches group output, then a fix.
- **Action-authority regex:** questions stop counting as instructions ("…is that normal?", "…which are safe?").
- **`propose_change`:** when grading throws, fail closed to a proposal instead of using the model's `approval_mode`.
- **Piggybacked GPS:** a server-side check of the sharing mode.
- **Contribution policy:** move the facade from shadow to enforcing **for durable writes only**. T0 turns cannot write without a structured grant.
- **Relationship fixes R1–R6:**
  - the sender's inference permission in source contribution;
  - GROUP-audience admission of pair notes, and its test;
  - the kill switch covering Home, Places friend cards and synthesis;
  - "nearby only" precision;
  - re-checking revoked pulls and closed pair rooms;
  - revocation of derived contributions.

**Acceptance:**
- Focused tests for each path.
- One end-to-end check with two real accounts on production (you and one friend):
  - a pair-scoped note never appears to a third person;
  - taking it back removes it from the recipient's Home and Life;
  - a question in chat does not create a constraint, expense or visibility change without a tap.

**Size.** About 1–1.5 weeks of agent time.

### S1: Supply for one neighborhood (new; runs in parallel; mostly editorial)

**Outcome.** On an ordinary day in your neighborhood, Home and Places show at least three real, current, sourced items without you capturing anything first.

**Scope.** Follows [supply §9](supply-and-data.md).

**Steps:**
0. **Stop the bleeding**, by Oct 8:
   - renew `here_windows.yaml` and `season_windows.yaml` with at least 6 source-checked rows;
   - confirm the Google key name on Fly;
   - disable the Foursquare `/v3` key or plan its migration.
1. **Land the Red Hook readings** from `4254554cf`, with a fresh independent review. They become the corpus template.
2. **Entity disposition and fill.** 250–350 verified entities, including everyday categories.
3. **Readings.** 30–50 accepted, across 12–15 anchors.
4. **Hours and status freshness.** At least 90% of recommendable venues covered, or the product makes no open-now claims.
5. **Events.** Curated recurring area items first. Ticketmaster only after the terms are reviewed.
6. **Photos.** An atmosphere manifest, and a decision on R2.
7. **Email intake.** MX record and SendGrid.

**Decision needed.** D30: which neighborhood. Choose the one you live in and walk daily, or Williamsburg + Greenpoint, which reuses the most existing assets.

**Acceptance:**
- `seeded_city_readiness` passes with the everyday thresholds added.
- `runtime_acceptance` accepts a canonical lane.
- A walk on your phone shows Home and Places populated on a normal weekday and on a weekend.

**Size.** About 4–6 weeks. The editorial time is yours, or a curator's; agents do the research and pipelines.

### Next product slices (after H1 exit and session 2 decisions)

Each slice is whole but thin: across the roots, on real accounts, accepted on the device.

**Order.** F0 comes first. It follows the primary mode you agreed on Sep 26 ("You send Vesper the things life hands you, and they come back when they matter"). It is single-player, with the audience "just me", so it needs neither the privacy fixes nor the social decisions. It also produces the user-originated supply that the [supply inventory](supply-and-data.md) calls the most plausible source from day 1 to week 1.

| Slice | The experience | Needs first | Main build |
|---|---|---|---|
| **F0: Send to Vesper** | You send Vesper something life handed you: a place, a screenshot, a ticket, a menu, a photo, a friend's text. Optionally you add a question. It lands instantly, without a review-first screen and without leaving the app you were in. Vesper turns it into a typed artifact and shows an immediate payoff. It files it by place, person or a proposed thread. It comes back on Home or in Life AHEAD when it matters. | D33 (artifact contract), D34 (a send with a question keeps the send), D13 revised (AI-proposed threads), D04 (AHEAD) | Frictionless share extension: today's capture is review-first and redirects out. One artifact contract. The intake → anchor → Home/Life read path; today little downstream reads anchors, and a share never becomes a save. Proposed threads with one-tap accept. A Returns producer. |
| **F1: A friend's place** | You send a place with your own words to a friend. It arrives on their Home, joined with a current opening. They Keep it (a pointer, not a copy). Later it returns in their Life, and you can take it back. | D15, D08/D09/D17, D20, T1 | Switch on the built send/receive path. Keep → Life. A minimal Friends pill on pair circles. Retire the Follow UI (Wave 2). |
| **F2: An evening together** | A small group settles an evening without voting. One person proposes, others answer, and the Plan reflects it. The evening is kept, and returns. | D18, D19, D16, D02 | The seven-sentence Plan page (buildable now). The proposal flow already exists. Voting stops being the default (Wave 2). |
| **F3: Vesper prepares from what you sent** | Where threads intersect (this Saturday, these people, this trip), Vesper prepares a rough plan, weekend or draft from your owned artifacts, crediting whoever each piece came from. It prepares and never executes: you send or commit. | F0, D11 (use of friends' sends), D05, D32 | Put the legacy planning engine (`arun_planning_agent` local mode) and `AgentCompositionDraftV1` behind prepared possibilities on Home. Actions come only from intersections. |

**Optional second lane** after P0 lands: the **seven-sentence Plan page**. Its rules are adopted and it touches no Home files, so it can run alongside H1 without conflict. It becomes F2's main build.

### Deprecation waves

The detail is in [decisions §C.2](decisions-and-deprecations.md), [app §5](build-map-app-static.md) and [backend §7](build-map-backend-static.md).

| Wave | When | Contents | Package |
|---|---|---|---|
| 0 | Now; no decision needed | Doorway gate (C15), stop `story_backfill`, onboarding orphans, dead Atlas code, dark postcard and guest-vote code, backend Tier 0 (dead flags, loops, jobs, tables, 22 client methods) | P0 for the safety items; one small cleanup task after P0 |
| 1 | After the obligation audit | Booking: flag set in P0, then remove cards, entry points, tools, notification kinds and the execution footprint | Its own short task after P0 |
| 2 | After session 2 | Voting default off, Vesper-emitted polls removed, proactive interjection removed, Friends replaces Follow, weather rescue retired | With F1/F2 |
| 3 | At the four-root cutover (D31) | Plans tab stops being the root, Atlas/Discover redirects and timeline migration, status-bucket Plan surface | After H1 exit and F1 |
| 4 | Each with its own design | Expenses contract to an assisted ledger, live voice, story slug sunset | Later |

## 3. Founder checklist: only you can do these

**Part A: today or tomorrow (about 45 minutes)**
- [ ] Replace `TRAVEL_WORKSPACE_CI_TOKEN`: a fine-grained PAT or GitHub App token, `contents:read` on both children, 1-year expiry. Check `TRAVEL_WORKSPACE_DISPATCH_TOKEN` at the same time.
- [ ] Set branch protection on all three repos:
  - 0 required approvals;
  - drop "approval of the most recent push";
  - `strict: false`;
  - the core required checks only (infra R3);
  - auto-merge and delete-branch-on-merge on.
- [ ] Confirm the GitHub billing spending limit on the account that owns the private repos.
- [ ] Set the Anthropic monthly spend cap.
- [ ] Decide whether `travel-workspace` stays **public**. It contains strategy, the API snapshot and the design archive.

**Part B: this week, during P0**
- [ ] Put the Mapbox download token in `~/.netrc`, so local native builds work.
- [ ] Fly secrets:
  - `SENTRY_DSN`, `POSTHOG_API_KEY`, `EXPO_PUSH_ENABLED=true`;
  - check `PLACES_GOOGLE_API_KEY` against `GOOGLE_PLACES_API_KEY`;
  - rotate `ADMIN_API_TOKEN`.
- [ ] Upload the APNs key to Expo.
- [ ] Run the migration rehearsal script against a copy of production, then authorize and run the deploy.
- [ ] Run `eas build -p ios --profile founder` and install it.
- [ ] From then on, spend **10 minutes a day on your phone** with the `founder` build. Any "this is wrong" goes to me in one line, and I turn it into a task.

**Part C: decisions.** See §4.

## 4. Decision sessions

My recommendations for each decision are in [decisions Part A](decisions-and-deprecations.md). I'll bring each session as a short list with a default you can accept or change.

**Session 1: this weekend, about 45 minutes. It unblocks P0, H1 and S1.**
1. **D27.** Retire M1 as the governing milestone. Decide PearX separately.
2. **D01.** Make the experience and its arc canonical as the lifecycle lens under the four moves. I'll draft the decision record for you to approve. It also resolves the expired philosophy source (B30).
3. **D02.** Record the Sept 13–25 design direction as one dated decision. This covers social, Chat and Live Home: everything currently marked "RULED" only in board captions.
4. **D26.** The accepted Home references (the set in §2 H1).
5. **D30.** The first neighborhood.
6. **D32.** A bounded recurring-supply trigger for the cohort area, under a cost cap.
7. **D34, and the direction for D33.** A send with a question keeps the send. Approve one artifact type contract in principle; I'll draft its shape for session 2. Together they let design and backend work on F0 start while H1 finishes.

**Session 2: by Oct 5, about 90 minutes. It unblocks F1–F3 and stops the Oct 6–7 lapses.**
- **Social pack:**
  - D08 Friends audience, D09 connection default, D17 retire Follow
  - D15 the friend's original: one id, pointer Keep, take-back
  - D18 no new group room
  - D19 polls only on request
  - D20 Home placement
  - D21 no automatic "helped" signals
  - D10 guests
  - D11 source-use grant
  - D22 notification defaults
- **Life and F0 pack:** D33 the artifact contract (draft attached), D13 revised (AI-proposed threads, intersections, actions only from intersections), D04 retained intention and AHEAD, D14, D12 collections, D05 history and continuity, D06 assistance scope. The Life D0 board's seven rulings belong here; row 1, the kept-intention owner, is the keystone.
- **Chat and Live:** D23 naming, D24 Live lane D, D25 no "we'll tell you" copy until a monitor owner exists.
- **Company:** D28 brand, D29 pricing principle, D31 cutover criteria.

**Design housekeeping after session 2.** I'll prepare it and you approve it in one pass:
- Stamp the rulings onto the boards.
- Rename the legacy projects `ARCHIVE ·` or `REFERENCE ·`.
- Take a snapshot before any deletes.
- Unify VDL 0.4.1 across Entity and Life.

## 5. Operating model

**Roles**
- **You** own product rulings, secrets and consoles, the daily 10-minute phone walk, and editorial supply.
- **Claude (orchestrator)** owns:
  - this plan and the gap map, updated weekly, with the Delivered number first;
  - decision preparation with recommendations and deadlines;
  - package handoffs with device acceptance;
  - review of each landed PR against the gap map;
  - watching for drift: long-lived lanes, docs outgrowing code, consumers built before their owner decisions.

  Claude does not edit files in Codex's active lanes.
- **Codex (implementation)** runs one lane per package through landing and retirement. There are at most two active lanes: H1 plus P0 now, then H1 plus Plans or T1.

**Cadence rules.** Proposed for root `AGENTS.md`; infra R5–R6.
- Land to `main` at least once per working day, behind flags. No lane lives longer than 3 days without landing.
- Retire a lane the day it merges.
- Evidence goes in the PR description and CI artifacts. At most **one** doc commit per landed package. Today's lane ratio is 28 doc commits to 19 code commits; the target is ≤1:5.
- Stop adding an `expires` date to every working doc, or archive expired ones automatically.

**Definition of done.** A user-visible change is done only when all of these hold:
1. It is merged to `main` with the core checks green.
2. It is deployed. Production `/ready` reports the merge SHA.
3. It is on your phone, through the `founder` OTA or a build, with the ID recorded.
4. It has been walked on the device against production, with one screenshot, or one line in a `DONE` log.
5. The PostHog event arrives and Sentry shows no new error class within 24 hours.

Anything less is "merged" or "candidate", and the gap map's Delivered column does not move.

**Weekly checkpoint.** About 15 minutes, with me. Four questions:
1. What rose in Delivered?
2. Which decisions are due?
3. What is blocked, and on whom?
4. Is the next package still the right one?

## 6. What I'd measure

| Measure | Now | Target by Oct 10 | Target by Oct 31 |
|---|---|---|---|
| Delivered: post-mid-August capabilities on your phone against production | About 0% | ≥ 45%: the `founder` profile, excluding the backend-dark rows | ≥ 60%: T1 done, F1 live between two real accounts |
| Days since the last production deploy | 43 | ≤ 3 | ≤ 3 |
| `main` CI green, children | Red since mid-May | Green | Green |
| Open lanes older than 3 days | 1+ | 0 | 0 |
| Decisions past their deadline | 1 (M1) | 0 | 0 |
| Doc-to-code commit ratio per lane | 28:19 | ≤ 1:3 | ≤ 1:5 |
| Supplied neighborhood: real items on an ordinary day | 0 | ≥ 3 (catalogue + Red Hook) | ≥ 10 |

## 7. Proposed edits to the program roadmap

I will not edit the H1 lane's copy of `vesper-program-roadmap.md`. I propose that the lane owner, or you, apply these edits at H1's next checkpoint:

1. **Add row "0.5 — active: P0 Ship path".** Give its outcome and acceptance from §2 P0, and mark it as a second lane with separate files.
2. **Add "Cross-cutting before any shared audience: T1 Trust enforcement"** as a named package, not an obligation inside each package.
3. **Change H1 acceptance** to "walked on the `founder` build against production once P0 lands", keeping fixture captures as pre-walks. Add the native-dependency gate for `aa3e235d6`.
4. **Change Package 2 from "select later" to a default:** F0 "Send to Vesper", with S1 supply continuing in parallel. Then T1, then F1 "A friend's place". All subject to the H1 bottleneck evidence.
5. **Add a "Decisions due" block** with the Oct 5 session and the Oct 6–7 lapse dates, linked to [decisions](decisions-and-deprecations.md).
6. **Add the definition of done** from §5, and the doc-commit rule.
7. **Retire the M1 references** in Owner Action Items once D27 is ruled (B1–B3).

## 8. Risks and how this plan handles them

| Risk | Handling |
|---|---|
| The 77 migrations fail on real production rows | Rehearse on a fork first. Production is effectively your dogfood environment, and no external users exist yet. |
| The `founder` build shows rough edges everywhere | That is the point. It turns every document-based judgment into something observed. Rough edges become one-line tasks, ranked weekly. |
| The decisions don't get made, and builds proceed on board captions | Two dated sessions, with defaults prepared. The alternative, as now, is building consumers before owners. |
| Supply stalls because it is editorial | Start with the smallest piece that pays (catalogue renewal by Oct 8). Agents do the research and pipelines; you only review. |
| Cost spikes after the deploy | The safety pack must land before the deploy. The spend cap is set in Part A. The kill switch becomes real. |
| Two lanes collide | P0 owns only infra, config and safety files. Anything touching Home, Places or Life projections goes to H1. |
