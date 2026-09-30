---
doc_type: working
status: active
owner: Claude orchestrator (product map)
created: 2026-09-26
expires: 2026-10-26
why_new: Index and headline findings for the September 26 product map, so the founder and implementation lanes can find the measured state, the gaps and the proposed plan without reading every inventory.
promotes_to: null
supersedes: []
---

# Product map (September 26, 2026)

This is a measured picture of Vesper: what is designed, what is built, what can be reached in a build, what has been delivered, and what is blocking each gap. It was produced by the orchestrator at your request.

- **Baseline:** workspace `6ef3dca`, backend `c8c9f5785`, app `43225df35`, the merged recovery from Sep 26.
- **Lane:** `codex/product-map-inventory`. No product source was changed.
- **Authority:** product, system, design and program owners keep authority. These documents are dated reference, and they expire Oct 26.

## Start here

1. **[Gap map](gap-map.md).** The measured answer and why the product feels unbuilt.
2. **[Execution plan](execution-plan.md).** Packages, founder checklist, decision sessions, operating cadence, and proposed roadmap edits.
3. **[Decisions and deprecations](decisions-and-deprecations.md).** 34 decisions (D01–D34) with deadlines and recommendations, 32 documents to deprecate, and 16 product concepts to retire in waves.

## Inventories

| Document | Covers |
|---|---|
| [Design atlas: Home, Places, Entity, Life, Plans](design-atlas-home-places-life-plans.md) | 110 boards; canonical target set per surface; 24 contradictions; 19 founder questions; design completeness by state |
| [Design atlas: Social, Chat, You, language](design-atlas-social-chat-you-language.md) | Multiplayer Shapes, Social Experience, Chat (Direction B), You, the Stage 1/S2 workbench and the production kernel; about 48 founder rulings needed |
| [Design atlas: legacy projects](design-atlas-legacy-projects.md) | At least 24 Claude Design projects; lineage; 14 orphaned ideas; cleanup; repository documents still pointing at superseded projects |
| [Build map: app](build-map-app-static.md) | Build posture per EAS profile; 48 public flags; 198 routes; capability map; code health; deprecation candidates; the active Codex lane |
| [Build map: backend](build-map-backend-static.md) | 37 packages; 655 API operations classified; flag map; workers, loops and subscribers; data and identity spine; capability status; privacy and correctness risks R1–R16 |
| [Build map: runtime](build-map-runtime.md) | Simulator run of the merged baseline in three passes: internal four-root build, default legacy shell, and against a real local backend. 290 screenshots in [`screens/`](screens/). The key defects are summarized in [gap map §6](gap-map.md). |
| [Supply and data](supply-and-data.md) | Every content corpus; supply pipelines; what a real NYC user sees; a supply plan for one neighborhood |
| [Infra and process](infra-and-process.md) | CI/CD history, gates, environments, secrets, telemetry, agent workflow, cost safety; ranked recommendations; definition of done |

## Headline findings

1. **About 60% of the designed product is built.** About a third can be reached in any installable build, and almost none of it has been delivered.
   - Built: 61% of 75 designed capabilities.
   - Reachable in a build you can install: 33%.
   - Delivered to a phone against current production: about 0% of work since mid-August.

   The earlier "about 20%" estimate was not measured, and it was wrong.
2. **Delivery is the largest gap.**
   - The last app build was Aug 4.
   - Production runs Aug 14 code, 1,673 commits and 77 migrations behind `main`.
   - Every EAS profile shows the legacy shell.
   - CI on the child `main` branches has been red since mid-May, first because of GitHub billing and now because of credentials and date checks.
   - Branch protection cannot be satisfied by a solo founder.
3. **Decisions are the second gap.** 15 of the 20 unbuilt capabilities wait on a founder ruling. M1 (Sep 28) cannot be met. Eight proposals lapse on Oct 6–7. The newest social direction exists only as board captions.
4. **Trust is designed but not enforced.** The contribution policy runs only in shadow. About 19–20 chat-turn paths write lasting state without confirmation. The relationship pipeline has six privacy defects to fix before any shared audience.
5. **Supply is thin.** There are no reviewed NYC readings on `main` (Red Hook has 3). Home's world catalogue expires Oct 9. Brooklyn has hours for 12% of venues and no photos.
6. **Cost safety must land before the next deploy.**
   - The LLM kill switch misses most paid paths.
   - Empty chat searches can trigger up to about $800/day of city seeding.
   - Retired booking execution, including Bland.ai restaurant calls, is still admitted by default.
7. **At runtime the app largely works, with specific breaks.**
   - The Chat root has no composer in any build tried; the cause is not yet diagnosed.
   - Life's lenses don't reorganise anything.
   - Ask Vesper sends a message on your behalf without review.
   - Home → Chat loses context.
   - Retired names (Trips, Atlas, Discover) still show in the four-root build.
8. **The designs are strong but unevenly settled.**
   - Home, Places, the place page and Chat have adopted or selected references.
   - Social is moving, and its high-severity contradictions are unresolved: group chat, Follow versus Friends, person pages, and custody of originals.
   - The shared design language is split three ways.

## Proposed order of work

These are detailed in the [execution plan](execution-plan.md):

1. **P0 ship path**, now, in its own lane: date gates, green CI, the cost and safety pack, a `founder` profile, migration rehearsal, deploy, and the build on your phone.
2. **Decision session 1** this weekend: M1, the experience arc, recording the design direction, Home references, the neighborhood, and the supply trigger. **Session 2** by Oct 5.
3. **H1** continues, and its acceptance moves to your phone.
4. **T1 trust enforcement** before any shared audience.
5. **S1 supply** in parallel, starting with the Oct 9 catalogue renewal.
6. **Slices after H1:**
   - F0 send to Vesper (the primary mode agreed Sep 26)
   - F1 a friend's place
   - F2 an evening together (the seven-sentence Plan page)
   - F3 Vesper prepares from what you sent

## Evidence boundary

- Most findings come from static reads of code and design boards at the revisions above.
- Direct observations were limited to:
  - the production `/ready` endpoint;
  - GitHub CI history;
  - the EAS build list;
  - the local simulator run, which used the 09-22 dev client with no maps and one synthetic user.
- Fly secrets, the EAS dashboard, production data and the physical device were **not** observed.
- Where a finding was spot-checked by the orchestrator, the source document says so.
- Findings marked unverified in the source documents remain unverified here.
