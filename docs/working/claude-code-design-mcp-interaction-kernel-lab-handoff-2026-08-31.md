---
doc_type: working
status: active
owner: founder / product / design / research
created: 2026-08-31
last_verified: 2026-08-31
expires: 2026-09-30
why_new: Gives Claude Code one complete, executable handoff for creating a separate Claude Design MCP interaction lab that compares form-first, chat-only, and hybrid shared-object experiences without reopening the semantically closed Home and Places project or prematurely editing production code.
promotes_to: null
supersedes: []
source_of_truth_for:
  - claude-code-claude-design-interaction-kernel-lab-handoff
depends_on:
  - docs/working/form-chat-hybrid-comparative-interaction-research-2026-08-31.md
  - docs/working/ai-native-effortless-editing-and-composition-research-2026-08-31.md
  - docs/working/critique-response-and-composition-phase-2026-08-30.md
  - docs/working/design-kernel-extraction-2026-08-29.md
  - docs/working/whole-product-v1-conformance-workbook-2026-08-29.md
  - docs/systems/contribution-and-consequence.md
  - docs/systems/artifact-expression-and-composition.md
  - docs/systems/four-root-loop-object-surface.md
---

# Claude Code + Claude Design MCP Handoff — Vesper Interaction Kernel Lab

## What this handoff is

This document is a complete execution brief for a Claude Code session with the
Claude Design MCP available.

The session must create a **new, separate Claude Design project** named:

> **Vesper — Interaction Kernel Lab**

The project will compare three interaction paradigms—form-first, chat-only, and
hybrid shared-object—against three fixed Vesper situations:

1. a solo New York weekend;
2. a Brooklyn dinner with friends; and
3. a disrupted return flight.

The lab is intended to answer interaction questions that static semantic boards
cannot answer:

- How little must the person express?
- Where does current state remain legible?
- When does touch beat language?
- When does conversation beat direct control?
- Where must a structured confirmation appear?
- Can a local error be corrected without regenerating everything?
- Can the person leave without finishing setup or cleaning residue?
- Does social participation feel ordinary rather than administrative?
- Can a person supervise, intervene, or take over without operating an agent
  dashboard?

This project is an **interactive research instrument**, not a production
implementation, new product canon, component gallery, visual-language
exploration, or extension of the Home and Places semantic project.

---

# Claude Code execution prompt

Everything below this heading is addressed directly to the Claude Code session
that will execute the handoff.

## 0. Role and outcome

You are operating as the interaction-design engineer and research-instrument
builder for Vesper. You have access to the workspace repository and the Claude
Design MCP.

Your job is to:

1. read the current Vesper product, interaction, authority, and design
   contracts;
2. inspect—but not modify—the semantically closed `Vesper - Home & Places`
   Claude Design project;
3. create a new Claude Design project named exactly
   `Vesper — Interaction Kernel Lab`;
4. reuse the settled Vesper design kernel rather than inventing a new visual
   system;
5. build three genuinely interactive, comparable treatment flows for each of
   three fixed situations;
6. make the flows deterministic and capture-addressable;
7. include lightweight local research tracing and reset behavior;
8. render, exercise, and inspect every required path;
9. record findings without declaring a winner in advance; and
10. return one workspace execution report with the durable Claude Design link,
    project ID, file inventory, checks performed, findings, limitations, and
    decisions still requiring founder review.

Do not implement production React Native, backend, schema, or API changes in
this task.

## 1. Workspace and concurrency preflight

Begin in:

```text
/Users/feihuyan/travel-workspace
```

Before substantive work:

1. Read `AGENTS.md` and `CLAUDE.md` completely.
2. Run `git branch -a` and `git status --short` in the workspace root.
3. Do not stage or commit pre-existing untracked or modified files.
4. Do not use `git add .`, `git add -A`, or `git commit -a`.
5. This task should not require a git branch or commit unless the founder
   separately requests one. The Claude Design project is the primary artifact;
   the only planned repository write is the execution report named in §20.
6. Other sessions may be working in both child repositories. Do not edit either
   child repository.

Treat all existing worktree changes as belonging to the founder or another
session.

## 2. Claude Design MCP preflight

Before invoking project-write tools:

1. Load the Claude Design MCP tools if they are deferred.
2. Call `mcp__claude-design__read_design_skill` and read the complete current
   skill.
3. Call `mcp__claude-design__get_claude_design_prompt` and follow any current
   project-authoring requirements.
4. If current MCP instructions conflict with mechanical advice in this
   handoff, current MCP instructions win. Product and interaction contracts in
   this handoff still govern the result.
5. Use `mcp__claude-design__list_projects` to resolve project identities. Do
   not guess or hardcode a project ID from an old document.
6. Resolve the current project whose title is `Vesper - Home & Places` and use
   `get_project` / `list_files` / `read_file` to inspect the exact live project.
7. Read its current Overview, Handoff Contract, C1, C2, C3, Urgent/F5,
   Findings, Build Manifest, Tokens, and shared kit files that are relevant to
   this lab.
8. Do not modify, delete, rename, or add files to that source project.

Known MCP methods that may be relevant include:

- `list_projects`, `get_project`, `create_project`;
- `list_files`, `read_file`, `copy_files`, `write_files`, `delete_files`;
- `create_support_js`;
- `finalize_plan`;
- `render_preview`;
- `list_comments`, `ack_comments`;
- `get_conversation`, `put_conversation`; and
- the `DesignSync` workflow for local-path uploads.

Discover their current schemas before calling them.

### MCP write discipline

- `mcp__claude-design__write_files` has historically been whole-file and
  inline-only. For large shared files, prefer `DesignSync.write_files` with a
  local path when the current tool supports it.
- `DesignSync.finalize_plan` historically requires a `deletes` field; use an
  empty list when no deletion is planned.
- Read the latest etag immediately before overwriting any existing design-lab
  file. Do not assume cross-session locking.
- After each write, re-read the changed region and render it. A successful
  upload is not visual or runtime proof.
- Never include a temporary `serve_url` or `claudeusercontent.com` URL in a
  user-facing response or workspace document. Return only the durable
  `claude.ai/design/...` project link.

## 3. Precedence and authority

Use this precedence when sources disagree:

1. Canonical product docs and system contracts in the repository.
2. This handoff for the bounded interaction-lab scope and treatment protocol.
3. The current `Vesper - Home & Places` Claude Design project for settled
   visual grammar, fixture material, and semantic compositions.
4. Exported Claude Design bundles in `~/Downloads` as historical mirrors only.
5. Older itinerary, Trips, Chat artifact, or pre-pivot projects as design
   history—not current product authority.

The source Home/Places project is explicitly **semantic phase closed**. Its
current ruling is: canvas work stops there; native interaction and real-data
validation come next. This lab addresses a new interaction question in a new
project. It must not reopen, extend, or silently supersede that source project.

## 4. Required reading order

Read every file in Tier A completely before creating the project. Read the
specified sections in Tier B before authoring the corresponding fixture. Tier C
is visual and implementation grounding.

### Tier A — product and interaction authority

1. `travel-agent/docs/product/Product Thesis.md`
2. `travel-agent/docs/product/Product Model.md`
3. `travel-agent/docs/product/Product Vision and Scope.md`
4. `docs/working/vesper-experience-constitution-and-interaction-grammar-2026-08-22.md`
5. `docs/systems/four-root-loop-object-surface.md`
6. `docs/systems/contribution-and-consequence.md`
7. `docs/systems/artifact-expression-and-composition.md`
8. `docs/working/ai-native-effortless-editing-and-composition-research-2026-08-31.md`
9. `docs/working/form-chat-hybrid-comparative-interaction-research-2026-08-31.md`

### Tier B — fixed fixtures and whole-product checks

1. `docs/working/whole-product-v1-conformance-workbook-2026-08-29.md`
   - whole-product evaluation grammar;
   - A01–A10;
   - A12–A18;
   - especially A01, A03–A10, A12, A13, A16.
2. `docs/working/hci-rebased-home-four-situation-fixtures-2026-08-28.md`
   - S1 ordinary New York;
   - S2 returned to New York;
   - S4 Brooklyn dinner.
3. `docs/working/consequence-arbitration-and-cross-surface-blueprints-2026-08-26.md`
   - treatment ladder;
   - Brooklyn dinner composite;
   - surface consequence responsibilities.
4. `docs/working/plan-occasion-projection-and-consumer-architecture-research-round-3-2026-08-31.md`
   - lightweight Plan / Occasion / expression distinctions;
   - one command layer for language and direct manipulation.
5. `docs/working/critique-response-and-composition-phase-2026-08-30.md`
   - current C1–C3 disposition;
   - §19 semantic-phase closure;
   - the instruction to move to native interaction and real-data validation.

### Tier C — design language and current design evidence

1. `docs/working/design-kernel-extraction-2026-08-29.md`
2. `docs/working/home-and-places-build-manifest-2026-08-30.md`
3. Current `Vesper - Home & Places` design project:
   - Overview;
   - Handoff — Contract;
   - Canon — Tokens;
   - Specimens — Home;
   - Specimens — Places;
   - Specimens — Promoted + Instruments;
   - C1 Ordinary Available / Quiet / Thin First Week / Findings;
   - C2 Occasion / Grant Moment / Evening and After / Findings;
   - C3 Thread / Map, Re-finding, Unwind / Findings;
   - Fixture F5 Disrupted Return;
   - Home Urgent;
   - Phase 2 19-Gate Matrix;
   - the shared board kit and support files.
4. `~/Downloads/vesper-home-places/` may be used only if the MCP project cannot
   be read. If used, state that it is an export and verify that it matches the
   live project before relying on it.

Do not import the old `Vesper · Conversational Artifact Language` project as
the interaction authority. Its declared scope is transcript artifacts only;
it does not own the current shell, four-root movement, Plans, Occasions,
provider consequences, or this lab.

## 5. Product premise the lab must preserve

Vesper is personal and multiplayer intelligence for the lived world. It helps
a person—and the people around them—make sense, open possibility, help it work,
and carry forward only what can improve a later experience.

For this lab, the interaction hypothesis is:

> Keep the thing being shaped visible. Let touch and language address the same
> semantic state. Ask the person to supply only the judgment or meaning the
> system cannot infer. Apply reversible private changes locally. Pause once at
> the actual human or world boundary. Show the result on the owner and make
> repair cheap.

The mechanical kernel under test is:

```text
FOCUS
  current root + visible owner/projection + selection + moment + authority

EXPRESS
  direct action, brief language, voice, or ordinary contribution

RESOLVE
  referent + semantic intent + smallest affected owner command

ACT
  private reversible -> apply
  material boundary -> preview once -> commit

REFLECT
  changed state on owner + compact receipt + return context

REPAIR OR LEAVE
  Undo, Correct, Stop, take over, or leave without setup debt
```

The consumer expression is:

> **Point at the thing. Say only what is missing. See what changed. Confirm
> only when another person or the world will be affected. Undo or leave.**

This is a hypothesis to test, not a result the boards are allowed to assume.

## 6. Project boundary

### In scope

- Three complete fixture flows.
- Three honest interaction treatments per fixture.
- Same evidence and desired outcome across treatments.
- Clickable state transitions, selection, confirmation, correction, Undo,
  stopping, and refinding where relevant.
- Cross-root origin and return when required by the job.
- Compact annotations and research tracing.
- Comparative findings and explicit failure or falsification records.
- Accessibility and small-screen behavior sufficient for a research prototype.

### Out of scope

- Production React Native implementation.
- Backend, schema, service, or OpenAPI changes.
- New durable product nouns or owners.
- A generalized Plan, Occasion, permission, draft, or agent framework.
- A universal AI edit mode.
- Arbitrary generated UI.
- A new visual theme or visual-language exploration.
- Redesigning Home, Chat, Places, Life, or global navigation.
- Reopening the semantic composition decisions in Home/Places.
- Completing the entire Chat or Life root.
- Provider integration or claims of live provider execution.
- User analytics, network tracking, or collection of real personal data.
- Declaring the lab empirical user research before people actually use it.

## 7. Create a new project, never fork the source authority

Use `mcp__claude-design__create_project` to create:

```text
Vesper — Interaction Kernel Lab
```

Project status must be visible in the Overview and every findings page:

```text
EXPLORATION · INTERACTION RESEARCH · NOT CANON · NOT PRODUCTION
```

Do not fork the whole Home/Places project. Copy only the minimum shared design
substrate needed for visual continuity:

- the current board kit;
- the current token/type/geometry roles;
- current native component expressions required by the fixtures;
- small fixture assets actually used; and
- the current support/runtime helper if required.

Avoid copying semantic boards into the new project. Link or cite their source
identity from the Overview instead. Duplication creates a stale shadow canon.

When a copied shared file is adapted, rename it for the lab and place a header
comment naming its source project, source filename, date copied, and that the
lab copy is non-authoritative.

## 8. Required project file structure

Create this project structure unless the current Claude Design skill requires a
different extension or support layout:

```text
README.md
00 Overview.dc.html
01 Protocol and Scorecard.dc.html
02 Interaction Kernel.dc.html
A — Solo NYC Weekend.dc.html
B — Brooklyn Dinner.dc.html
D — Flight Disruption.dc.html
90 Cross-Fixture Findings.dc.html
91 Decision Log.dc.html
_kit/board-kit.css
lab.css
fixtures.js
lab-state.js
support.js
```

Roles:

| File | Responsibility |
| --- | --- |
| `README.md` | Coding-agent and reviewer handoff, read order, scope, evidence status, durable source links |
| `00 Overview` | Why the lab exists, project boundary, fixed fixtures, links to every treatment and capture state |
| `01 Protocol and Scorecard` | Treatment fairness, task scripts, metrics, moderator protocol, reset instructions, score sheets |
| `02 Interaction Kernel` | Focus/Express/Resolve/Act/Reflect/Repair model, truth planes, authority boundaries, modality division |
| `A` | Three complete solo-weekend treatments over one fixed evidence graph |
| `B` | Three complete Brooklyn-dinner treatments over one fixed evidence graph |
| `D` | Three complete disruption treatments over one fixed evidence graph |
| `90 Findings` | Side-by-side results, failure oracles, observed trace values, unresolved questions, provisional recommendations |
| `91 Decision Log` | Every design judgment with status: hypothesis, adopted-for-lab, founder-ruled, rejected, or unresolved |
| `fixtures.js` | Fixed evidence, actors, authority, starting state, and expected outcome; no UI logic |
| `lab-state.js` | Deterministic flow state, query routing, event trace, reset/export behavior; no product-policy invention |
| `lab.css` | Lab-only layout and instrumentation styles; imports the settled kernel |
| `support.js` | Claude Design runtime support only |

Do not create a separate page for every screen state. Each fixture page owns
its three treatments and can render one treatment/state deterministically from
query parameters.

## 9. Deterministic interaction and capture contract

Each fixture page must support:

```text
?treatment=form|chat|hybrid
&step=<stable-step-id>
&mode=research|capture
&capture=1
&reset=1
```

Requirements:

1. Unknown treatment or step values fail visibly with an error specimen. They
   must not silently fall back to the first screen.
2. `capture=1` removes research chrome, freezes motion, and renders exactly one
   393-point mobile specimen.
3. `mode=research` exposes step navigation, trace summary, reset, and treatment
   status outside the mobile specimen.
4. `reset=1` clears only the current fixture/treatment session.
5. Every transition is reachable by a real target in the mobile specimen.
6. Back restores the prior state and selection accurately.
7. Refresh preserves a research session only when persistence is part of the
   treatment; otherwise it returns to the declared start state.
8. No path depends on a network call or live personal data.
9. No action may present a timeout or fake loading delay merely to make the
   design feel agentic.

Target device:

- primary: 393 points wide;
- minimum validation: 320 points wide;
- standard text and one 135% text-size pass for the most information-dense
  state in each fixture;
- minimum target size: 44×44 points;
- reduced-motion path required;
- keyboard focus and visible focus treatment required in the browser lab.

## 10. Lightweight research trace

The lab must record a local, in-memory trace for research comparison. Do not
send analytics anywhere.

Suggested event shape:

```js
{
  fixture: "A" | "B" | "D",
  treatment: "form" | "chat" | "hybrid",
  sessionId: "fixture-local-random-id",
  atMs: 0,
  stepId: "stable-step-id",
  eventType: "tap" | "type" | "submit" | "back" | "undo" | "confirm" |
             "correct" | "stop" | "takeover" | "inspect",
  targetId: "stable-target-id",
  wordsEntered: 0,
  ownerBefore: null,
  ownerAfter: null,
  consequenceClass: "none" | "private-reversible" | "shared" |
                    "audience" | "provider" | "spend" | "public"
}
```

The research shell should compute without interpretation:

- elapsed time;
- taps/clicks;
- screens or distinct states;
- words entered;
- clarification turns;
- backtracks;
- confirmations;
- local corrections;
- whole-result regenerations;
- owner/surface changes; and
- whether the user ended with residue.

Provide `Reset treatment` and `Copy trace JSON`. If clipboard access is not
reliable inside Claude Design, render a selectable trace block instead. Do not
add an external export service.

Counts are descriptive. The lab must not convert them into an automatic winner
score.

## 11. Treatment fairness contract

Each treatment receives the same:

- authorized fixture evidence;
- current world facts and freshness;
- model intelligence;
- available provider or social capability;
- desired human outcome;
- final truth constraints;
- privacy and authority rules; and
- recovery capability.

Only the interaction paradigm changes.

### Form-first must be honest

Give it:

- good defaults;
- autocomplete;
- progressive disclosure;
- native pickers and direct controls;
- clear labels;
- sensible validation;
- strong overview and structured review; and
- no intentionally absurd number of fields.

Its limitation should emerge from representational and integration burden, not
poor design craft.

### Chat-only must be honest

Give it:

- strong grounding;
- concise answers;
- high-quality transcript cards;
- sensible conversational reference resolution;
- no gratuitous clarification;
- clear assistant readback; and
- the same reasoning capability as hybrid.

But current state still lives primarily in the transcript. Transcript cards
may summarize, but they do not become an independently manipulable owner
surface.

### Hybrid must be honest

Do not give hybrid every control and every conversation at once. The shared
object must be the resting state. Language appears contextually for the part
touch cannot express efficiently.

Hybrid receives no special intelligence or hidden shortcut. It must prove its
advantage through lower total collaboration cost, better state legibility,
local repair, and appropriate boundary handling.

If form-first or chat-only wins a job, record that outcome.

## 12. Shared semantic annotation contract

Every meaningful step needs a compact annotation outside the mobile specimen:

| Field | Required value |
| --- | --- |
| Fixture / treatment / step | Stable IDs |
| Actor and viewer | Named fixture principal |
| Immediate human job | What the person is actually trying to accomplish |
| Root and visible owner | Home, Chat, Places, Life, Plan, Occasion, or operational owner |
| Truth plane | canonical truth, proposal, expression, or execution |
| Agency phase | inspect, compose, propose, commit, monitor, or reconcile |
| Authority | Use, Retention, Inference, Audience, and Action consequence in human terms |
| Persistence | ephemeral, session, private durable, shared durable, provider truth, or none |
| Boundary | none, private reversible, shared, audience, provider, spend, or public |
| Return | exact destination and selection/context that survives |
| Repair | Undo, Correct, Withdraw, Stop, Take over, retry, or no recovery |
| Failure oracle | What would make this step a product failure |

Do not display internal permission-axis jargon inside the consumer UI. The
annotations may name the axes; the interface must describe the concrete human
effect.

## 13. Fixture A — solo New York weekend

### Fixed evidence

- It is an ordinary week in New York.
- Saturday 2–8 PM is open.
- The person has expressed: `Maybe jazz Saturday.`
- Two relevant saved Places exist as venue candidates.
- No exact time has been chosen.
- The initial shape is not yet a durable Plan.
- Current weather changes before the weekend.
- No one else is involved.
- No booking, message, or provider action is authorized.

Use realistic fixture names for the two venues, but mark all hours, set times,
availability, weather, and transit durations as fixture data. Do not present
them as live truth.

### Task script shared by all treatments

1. Add the jazz possibility without choosing an exact time.
2. Make the evening less rushed.
3. Compare the two venues in the context of the whole Saturday shape.
4. Keep one privately.
5. Remove it.
6. Verify that no empty Plan or cleanup task remains.

### A-form required journey

Show the strongest plausible conventional experience:

1. enter a Saturday planning surface;
2. create a loose possibility with optional time;
3. add or compare the two venues;
4. manually resolve pace, ordering, and travel burden through native controls;
5. save or keep the selected shape;
6. remove the jazz entry; and
7. show the resulting container/residue truth honestly.

Do not intentionally force title, category, or exact time if a good conventional
product could make them optional. The comparison is about remaining
representational and integration labor.

### A-chat required journey

1. Start from a clean Chat.
2. Enter `Maybe jazz Saturday.`
3. Return a useful shape without a form.
4. Enter `Less rushed.`
5. Ask to compare the two candidates.
6. Use natural references such as `the other one` or `keep this` and make any
   ambiguity visible but not artificially exaggerated.
7. Keep the selected result.
8. Remove the jazz portion.
9. Show how the person determines current truth after several versions.

The transcript may contain structured cards, but no independent Plan or owner
surface may be directly manipulated.

### A-hybrid required journey

1. Accept `Maybe jazz Saturday` in Chat or from a contextual Home entry.
2. Return an ephemeral visible Saturday shape, not an intake flow.
3. Select the evening span and express only `Less rushed.`
4. Show the smallest localized semantic delta in place.
5. Select the two venue candidates and compare them in context.
6. Use an explicit `Keep Saturday` or equivalent action to promote the accepted
   shape into private Plan truth.
7. Remove the jazz entry directly.
8. Show `Undo` and the no-empty-shell outcome.

Private reversible edits should not require a preview ceremony.

### A required capture states

- start;
- first useful shape;
- less-rushed delta;
- comparison;
- kept state;
- removal receipt;
- no-residue end; and
- one correction or Undo state.

### A failure oracles

- The person must choose Plan before receiving value.
- `Less rushed` causes unbounded whole-result regeneration.
- Current versus proposed state cannot be identified.
- `This` requires the person to restate visible context.
- Keeping occurs without an explicit promotion decision.
- Removal leaves an empty durable container or task.
- Ignoring the result creates preference evidence or follow-up debt.

## 14. Fixture B — Brooklyn dinner with friends

Reuse the current C2 semantic fixture from the Home/Places project rather than
inventing a second social world.

### Fixed evidence and principals

- **Nora** is the host and Vesper user.
- **Dana** is visiting, has no app, and participates through a bounded guest
  link.
- **Sam** is local, uses Vesper, and can contribute a Place and authored rule.
- **Alex** cannot attend.
- Nora begins with: `Dinner while Dana's here—Saturday night?`
- Naming people does not authorize contact.
- Dana privately contributes an approximate `$40` limit.
- Sam has not initially opened the Occasion.
- Sam later contributes the Georgian-room Place and his authored khinkali rule.
- The two current candidates are the Georgian room and the noodle bar.
- Both fit every **known** constraint; Sam's unopened or unanswered state is
  unknown, not compatible.
- Nora owns the bounded final Place decision.
- Contributions, attendance, audience, retention, and later relay are distinct.

Use fixture markers for all provider availability, address, timing, price, and
reservation facts.

### Task script shared by all treatments

1. Prepare the dinner from Nora's ordinary sentence.
2. Resolve materially missing time only if needed.
3. Invite Sam, Alex, and Dana without profiles or a permission dashboard.
4. Give Dana immediate private value before asking for a response.
5. Accept Dana's private limit without exposing it.
6. Let Sam contribute a Place and authored rule through ordinary language.
7. Produce a safe shared comparison that uses private constraints in aggregate.
8. Preserve Sam's unknown participation state.
9. Let Nora make the bounded shared decision.
10. Correct or withdraw one contribution and recompile dependent state.
11. Show the settled consequence without a social feed.

### B-form required journey

Create the strongest conventional event experience:

1. event setup with good defaults and progressive disclosure;
2. participant and guest-link selection;
3. invitation preview and send;
4. participant responses;
5. private constraint entry;
6. contribution or option entry;
7. comparison/poll or host-decision surface;
8. settled result; and
9. correction/withdrawal.

Do not add an intentionally bad permissions matrix. If the form treatment needs
audience or contribution configuration to remain safe, expose only the minimum
credible conventional controls and count that burden honestly.

### B-chat required journey

1. Prepare the Occasion through conversation.
2. Keep preparation distinct from sending.
3. Preview and send the invitations in Chat.
4. Let all contributions and responses arrive in the transcript.
5. Return concise state-summary cards as needed.
6. Resolve the group-safe comparison conversationally.
7. Let Nora choose.
8. Correct or withdraw one contribution.
9. Show how a returning participant finds current truth without a standalone
   Occasion object.

The Chat treatment must not become deliberately incoherent. Give it excellent
summaries and reference resolution; its limitation should be transcript-based
common ground and refinding.

### B-hybrid required journey

1. Nora's ordinary sentence prepares an Occasion but sends nothing.
2. Ask only for a materially missing time.
3. Show one exact invitation/audience preview.
4. Confirmation creates the Occasion and sends the invitations.
5. The Occasion becomes a compact shared object: settled facts, attributed
   participation, one current open question, and ordinary conversation.
6. Dana receives immediate guest-link orientation before any response request.
7. Dana's private limit shapes the shared safe set without becoming attributed
   shared explanation.
8. Sam's contribution becomes an attributed Place/rule contribution with
   local `Added · Undo`; ordinary conversation without coordination consequence
   remains unstructured.
9. Nora sees that both candidates fit every **known** constraint and that Sam's
   response state remains unknown.
10. Independent responses remain independent; Nora makes the bounded decision.
11. Withdrawal updates Sam's lane and only the dependent comparison/result.
12. Home later shows only the material settled consequence.

No Occasion profile, group dashboard, activity feed, reaction system, or
permission worksheet is allowed.

### B required capture states

- prepared, not sent;
- exact audience preview;
- invitation sent / Occasion created;
- Dana's guest-link first value;
- Dana's private contribution receipt;
- Sam's attributed contribution;
- group-safe comparison with unknown state;
- Nora's bounded decision;
- settled consequence;
- contribution withdrawal; and
- recomputed result with provenance intact.

### B failure oracles

- Naming people contacts them.
- The first sentence silently sends invitations.
- Dana must install, create a profile, or complete setup before receiving value.
- A private constraint becomes shared rationale or attributed gossip.
- Sam's nonresponse becomes compatibility, consent, or decline.
- A contribution is treated as attendance.
- The shared result becomes a poll feed or synthetic group preference.
- Withdrawal rewrites other people's contributions or occurred history.
- The Occasion becomes a project-management dashboard.
- Returning participants must read the whole transcript to know current truth.

## 15. Fixture D — disrupted return flight

Reuse the current F5 disruption semantics and urgency register. Do not invent
live airline, legal, compensation, inventory, or reservation facts.

### Fixed evidence

- The original return flight is cancelled or materially disrupted.
- Current provider state was recently verified in the fixture.
- A provider reroute exists as an **offer**, not an accepted itinerary.
- Accepting it may affect a refund or alternate-travel path.
- Hotel, dinner/interview, companion/pickup, ground transport, and evidence may
  be affected.
- Vesper has prepared a comparison and one intent-preserving adaptation.
- Nothing has been accepted, submitted, booked, or sent initially.
- The person wants to preserve the important evening or next-morning commitment
  and reduce walking.
- One external sub-action will succeed and another will fail or remain unknown,
  forcing partial recovery.

All times, margins, prices, inventory, routes, and provider states must remain
explicit fixture values such as `[VERIFIED TIME]` where not already grounded.

### Task script shared by all treatments

1. Understand what changed and what is still only prepared.
2. Inspect one coherent adaptation rather than separate service alerts.
3. Change the priority to preserve the important commitment and reduce walking.
4. Distinguish private prospective changes from provider, money, audience, and
   shared consequences.
5. Review the exact external bundle once.
6. Commit the authorized external action.
7. Encounter one partial, failed, or unknown sub-action.
8. Understand current truth per owner.
9. Repair, retry safely, stop, or take over without replaying successful work.

### D-form required journey

Create the strongest conventional disruption center:

1. disrupted flight overview;
2. provider alternatives and exact details;
3. affected reservations/commitments;
4. ground transport and burden comparison;
5. notification selection;
6. structured review;
7. execution progress; and
8. partial-failure recovery.

Use excellent overview and structured controls. The burden should emerge from
the person integrating several service surfaces and expressing an experiential
priority that is not naturally a field.

### D-chat required journey

1. Announce the verified disruption in Chat.
2. Explain what is known, prepared, and unchanged.
3. Let the person say: `Keep the dinner if possible. Less walking.`
4. Return a coherent revised plan.
5. Make the person authorize the exact external consequences; do not accept an
   ambiguous bare `Do it` as sufficient.
6. Narrate or card the execution state.
7. Show the partial failure.
8. Let the person repair or take over.

Give Chat strong structured cards, but keep current operational state in the
conversation rather than a separate persistent instrument.

### D-hybrid required journey

1. Home or the active owner elevates one disruption instrument.
2. It shows current provider truth, affected commitments, prepared adaptation,
   freshness, and explicit non-action.
3. The person selects the walking-heavy leg and says:
   `Protect dinner. Less walking.`
4. Vesper recomputes the smallest coherent alternative and shows the localized
   tradeoff in place.
5. Private prospective state may update reversibly; provider, spend, audience,
   and shared changes remain visibly uncommitted.
6. One structured review names the exact provider choice, cost/refund effect,
   commitment change, affected people, outgoing message, and recovery limits.
7. One confirmation commits the authorized bundle.
8. The instrument shows `verified`, `pending`, `failed`, `unknown`, and
   `not attempted` per owner as applicable.
9. A successful sub-action is never replayed after another fails.
10. The person can retry the safe remainder, stop, inspect, or take over one
    action without taking over the whole adaptation.

### D required capture states

- verified disruption / nothing acted;
- prepared adaptation;
- selected leg with qualitative edit;
- localized revised adaptation;
- exact external review;
- applying;
- partial/unknown result;
- per-owner current truth;
- safe repair;
- stop; and
- one-action takeover.

### D failure oracles

- Prepared appears as accepted or completed.
- A callback appears as provider success.
- A Plan mutation appears as reservation truth.
- `Do it` hides affected people, money, audience, or providers.
- The person confirms twice for one constitutive boundary.
- Partial execution collapses into a generic error.
- Retry replays a successful provider action.
- A failed action has no stable new current state.
- The person cannot stop or take over.
- The interface makes a legal, compensation, eligibility, or inventory claim
  without fixture evidence.

## 16. Cross-root and owner-continuity proof

The lab must prove that hybrid does not mean “Chat owns everything.”

For each hybrid fixture, annotate and render one complete continuity chain:

```text
origin root or owner
  -> selection / context envelope
  -> contextual Chat or voice expression when needed
  -> typed semantic command
  -> owner-local result
  -> compact receipt
  -> exact return with selection and scroll restored
```

The context envelope must preserve at least:

- origin root and projection identity;
- visible owner and revision;
- selected resource identities;
- current Moment;
- immediate job;
- active expression/instrument identity;
- audience and authority scope;
- unresolved question;
- return root/projection; and
- expiry/correction lineage.

Do not expose this envelope as a consumer card. Its proof is that the
destination already knows and the return does not lose place.

## 17. Visual and content constraints

### Preserve

- Current Vesper paper, ink, gold, oxblood, planning-ink, type, spacing,
  geometry, material, and containment laws from the design kernel.
- Current 393-point mobile grammar.
- Serif for earned editorial/read moments, system sans for interaction and
  operational work, mono for facts and state.
- One dominant job per surface/state.
- Direct state or an instrument may lead without editorial preamble.
- Real or fixture-grounded imagery only when it is evidence.
- Calm, precise operational language.

### Do not introduce

- a permanent copilot rail;
- a floating AI orb as the primary grammar;
- a large empty Chat box on Home;
- a universal sparkle button;
- gradients, glass, neon, or a new AI visual theme;
- arbitrary generated controls;
- heavy card nesting;
- a reflection question as first value;
- “What do you want to do?” over a state Vesper can already compose;
- user-identity interpretations such as “you experience travel through
  transitions”;
- artifact counts or thread counts as value;
- fake social activity or reactions;
- setup checklists;
- permission matrices in consumer UI;
- success language without owner verification; or
- placeholders that masquerade as real provider facts.

### Content bar

Every Vesper-authored contribution must add a mechanism, comparison,
reconstruction, practical consequence, or genuinely new relation. It may not
merely repeat what the person said or saw. In this lab, however, interaction
clarity outranks demonstrating editorial range; do not overload a flow with
content to make Vesper look intelligent.

## 18. Protocol and scorecard page

`01 Protocol and Scorecard.dc.html` must include:

### Moderator script

1. Reset the treatment.
2. Read the same human goal, not UI instructions.
3. Let the participant discover the path.
4. Do not explain capabilities unless the participant is blocked beyond the
   declared threshold.
5. Record whether the participant chose direct action, language, oversight, or
   takeover when several were available.
6. Ask state-comprehension questions after the task, not during it.
7. Ask the participant to re-find the settled state after five minutes; reserve
   one-day refinding for later live testing.

### Comprehension questions

- What is true now?
- What is only proposed?
- What, if anything, has been shared or sent?
- Who owns the next decision?
- What did Vesper change?
- What can you undo or correct?
- If you leave now, is anything unfinished?
- Where would you return tomorrow to find this?

### Qualitative ratings

Use the eight comparative dimensions from the research:

1. value first;
2. expression burden;
3. state legibility;
4. correction locality;
5. boundary clarity;
6. refinding;
7. social ease; and
8. ownership.

Also capture:

- perceived administrative burden;
- perceived prompting burden;
- perceived control;
- confidence about what happened;
- whether Vesper felt helpful, invasive, passive, or demanding; and
- preferred collaboration posture.

Use coarse qualitative ratings and comments. Do not invent a composite
quantitative score or statistically interpret prototype traces.

## 19. Findings and falsification requirements

`90 Cross-Fixture Findings.dc.html` must begin blank or hypothesis-labeled. Do
not pre-fill it with “hybrid wins.”

For each fixture and treatment, record:

- what the treatment made unusually easy;
- what work moved onto the person;
- where current state became unclear;
- where correction became broad or local;
- where confirmation was unnecessary or missing;
- where a user could or could not leave cleanly;
- whether the result felt authored;
- which modality the user tried to use naturally;
- trace totals; and
- the strongest counterexample to the preferred hypothesis.

The hybrid hypothesis is falsified or materially weakened if any of these hold:

1. users cannot reliably predict the scope of selection carried into language;
2. users spend more effort choosing between modalities than the hybrid saves;
3. state refinding is no better than Chat;
4. local repair still regenerates or invalidates the whole object;
5. the visible object feels like Vesper's work that the person merely approves;
6. the same action has different authority or result through touch and Chat;
7. an always-visible assistant is required for discoverability;
8. conventional direct controls consistently outperform hybrid for the whole
   fixture; or
9. the shared object makes an Occasion feel like project management.

Record those outcomes honestly. A useful lab may reject part of the current
hypothesis.

## 20. Workspace execution report

At the end, create exactly one new workspace document:

```text
docs/working/claude-design-interaction-kernel-lab-execution-report-2026-08-31.md
```

It must contain:

1. project title, project ID, and durable `claude.ai/design` link;
2. creation date and Claude Code session context;
3. exact files created and copied;
4. source project and source files inspected;
5. confirmation that the source Home/Places project was not modified;
6. which required flows are complete;
7. capture-addressable URLs expressed as durable project/file links plus query
   strings—never temporary serve URLs;
8. runtime and console checks performed;
9. 393/320/text-size/accessibility checks performed;
10. interaction-trace support and known limitations;
11. fixture or copy substitutions, with reasons;
12. provisional findings, clearly separated from observed participant evidence;
13. failed or weakened hypotheses;
14. unresolved founder decisions;
15. whether Italy reconstruction and post-return Home should proceed to a
    second lab phase; and
16. the recommended native-harness scope after founder review.

Do not modify canonical product docs, the design kernel, the Home/Places build
manifest, or the comparative research memo as part of this task.

## 21. Review and verification sequence

Work in bounded passes.

### Pass 0 — grounding and project skeleton

- Complete all required reading.
- Inspect the live source project.
- Create the new project.
- Copy the minimum design substrate.
- Create README, Overview, Protocol, Kernel, Findings, and Decision Log shells.
- Verify all project links and imports.

### Pass 1 — fixture A

- Lock fixed evidence.
- Build form, Chat, and hybrid treatments.
- Exercise every target and back path.
- Verify capture query states.
- Record design findings without choosing a global winner.

### Pass 2 — fixture B

- Reuse the current C2 principals and facts.
- Build all three treatments.
- Test preparation versus sending, private constraint use, unknown/nonresponse,
  host decision, contribution withdrawal, and recomputation.
- Verify each principal's view.

### Pass 3 — fixture D

- Reuse F5 semantics and the urgency register.
- Build all three treatments.
- Test proposed versus applied, exact boundary review, partial/unknown state,
  repair, stop, and takeover.
- Ensure no provider or legal claim outruns fixture evidence.

### Pass 4 — cross-fixture comparison

- Normalize step IDs and metric definitions.
- Complete the scorecard and failure-oracle matrix.
- Validate cross-root and owner continuity.
- Identify which moments are best served by conversation, touch, authored
  output, owner surface, or structured review.

### Pass 5 — visual and runtime QA

- Render every required capture state.
- Run every flow from a clean reset.
- Inspect browser console errors.
- Validate 393 and 320 widths.
- Validate the densest state at 135% text.
- Validate focus order, targets, reduced motion, and unknown query failures.
- Check for stale or contradictory language across pages.

### Pass 6 — return

- Complete Findings and Decision Log.
- Write the workspace execution report.
- Return the durable project link and a concise list of open founder decisions.
- Stop. Do not begin native implementation.

## 22. Definition of done

The handoff is complete only when all of the following are true:

1. A new project exists under the exact required title.
2. The source Home/Places project is unchanged.
3. The project declares itself exploration, not canon or production.
4. The required README, eight design pages, and shared lab runtime/style files
   exist.
5. Fixtures A, B, and D each have three honest, complete treatments.
6. All treatments use the same evidence, capabilities, authority, and desired
   outcome inside their fixture.
7. Every required transition is clickable.
8. Every required capture state is addressable deterministically.
9. Unknown capture parameters fail visibly.
10. Research traces can be reset and copied locally.
11. Current truth, proposal, expression, and execution are distinguishable.
12. Private reversible changes, social boundaries, and provider boundaries use
    different proportional treatments.
13. Correction, Undo, stop, and takeover appear where the fixture requires.
14. No treatment wins through extra intelligence or deliberately worse craft in
    another treatment.
15. No new product object, generalized workflow, or permission dashboard has
    been invented.
16. Visual language remains continuous with the current Vesper kernel.
17. Every flow works at 393 points; required narrow/text-size checks pass or are
    documented as failures.
18. Findings include counterevidence and falsification, not only confirmation.
19. The workspace execution report exists and contains a durable project link.
20. No production code or canonical docs were changed.

## 23. Final return format

Return to the founder with:

```text
Created: Vesper — Interaction Kernel Lab
Project: <durable claude.ai/design link>

Completed:
- Fixture A: form / chat / hybrid
- Fixture B: form / chat / hybrid
- Fixture D: form / chat / hybrid
- Protocol, trace, capture states, findings, and decision log

Strongest current finding:
<one concise evidence-backed sentence>

Most important counterevidence:
<one concise sentence>

Founder decisions needed:
1. ...
2. ...

Workspace report:
docs/working/claude-design-interaction-kernel-lab-execution-report-2026-08-31.md
```

Do not describe the project as validated, canonical, native-evidenced, or ready
for production unless the evidence actually supports those claims.

---

## Founder note on what happens after this handoff

This handoff ends at an interactive Claude Design research lab. The next step
is not automatically implementation.

After reviewing the comparative flows, the founder should decide:

1. which modality owns each interaction moment;
2. whether the Focus → Express → Resolve → Act → Reflect → Repair kernel
   survives;
3. which cross-root context and command contracts are sufficiently stable for
   a native harness;
4. whether the Italy reconstruction and post-return Home fixtures add new
   interaction evidence; and
5. the smallest native React Native research harness that can test touch,
   voice, latency, accessibility, device behavior, and real data without
   turning a research sequence into a narrow product strategy.

The lab should reduce uncertainty about Vesper's interaction grammar. It must
not reduce the ambition or scope of the product thesis to the three fixtures it
tests.
