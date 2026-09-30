---
doc_type: working
status: active
owner: Claude orchestrator (product map)
created: 2026-09-26
expires: 2026-10-26
why_new: Joins the Design Atlas and the Build Map into one measured gap per designed capability, replacing an unmeasured progress estimate with four explicit measures and the blockers behind each gap.
promotes_to: null
supersedes: []
---

# Gap map: what is designed, built, reachable and delivered

This document combines the product-map inventories into one measurement:

- the design atlases:
  - [Home, Places, Entity, Life, Plans](design-atlas-home-places-life-plans.md)
  - [Social, Chat, You, language](design-atlas-social-chat-you-language.md)
  - [legacy projects](design-atlas-legacy-projects.md)
- the build maps: [app](build-map-app-static.md), [backend](build-map-backend-static.md), and the runtime run on the simulator
- [supply and data](supply-and-data.md)
- [infra and process](infra-and-process.md)
- [decisions and deprecations](decisions-and-deprecations.md)

Each gap below names what blocks it: a build, a switch, a decision, supply, or delivery.

## 0. Method and evidence boundary

**Unit of measure.** One designed capability. The rows come from the canonical target sets in the two current design atlases (§3 in each). They were matched against the capability tables in the app build map (§3) and the backend build map (§6). There are **75 rows across nine surfaces**.

Features the vision retires are **not** counted, even though they are still live:
- the trip-first Plans home
- booking
- voting as the default
- Vesper as group facilitator
- Follow
- Atlas/Discover remnants

They are handled in the deprecation waves.

**Four measures.**

| Measure | Definition | Scoring |
|---|---|---|
| **Built** | Code for the capability exists on merged `main`, under any flag | Built and working (live, dogfood or internal) = 1; partial = 0.5; not built = 0 |
| **Reachable** | A build profile you can install today shows it | Live or dogfood = 1; partial and live = 0.5; internal only = 0 |
| **Delivered** | It is on a phone, running against current production | Measured directly (§1), not scored per row |
| **Decided** | It can be built or switched on without a new founder ruling | Recorded per row in the "Blocked by" column |

**Evidence.**
- Code was read at app `43225df35`, backend `c8c9f5785` and workspace `6ef3dca`.
- The production backend was read at `/ready` (it reports `4a7f3e6f0`). The CI history was read with `gh`.
- The simulator run (§6) supplies screenshot evidence and changed three rows.
- Supply facts come from the repository and the local, gitignored staging data. No production database was read.

**Limits.**
- Rows are unweighted. I chose the granularity of each row, so **challenge individual rows, not the totals**. Changing one row moves a total by about 1.3 points.
- "Built" means the behavior exists. It does not mean design fidelity: several built rows differ from the adopted boards in labels, hierarchy or kinds. Fidelity is tracked in the atlases, not here.
- Nothing was measured on a physical device. Fly secrets and the EAS dashboard were not visible.

## 1. The measured answer

| Measure | Result |
|---|---|
| Designed capabilities | **75** |
| **Built on `main`** (any flag) | **61%**. It is 59% if the stages that set Vesper apart count double (shared, wanted, returns, live). |
| **Reachable in a build you can install today** | **33%** (28% weighted). Every EAS profile resolves to the legacy shell. |
| Reachable with the proposed `founder` profile (app flags only) | **45%** |
| Reachable with the `founder` profile **and** the backend flags | **61%**, but 16 rows sit behind backend flags. The relationship and original rows cannot be switched on safely until the privacy fixes in the [backend map §8](build-map-backend-static.md) (R1–R6) land. |
| **Delivered to a phone against current production** | **About 0% of work since mid-August.** The last EAS build is from **Aug 4**. Production runs backend **`4a7f3e6f0` (Aug 14)**, 1,673 commits and 77 migrations behind `main`. No production or TestFlight build has ever been made. |
| Not built | **20 rows**. **15 of them wait on a founder decision.** 5 can be built now. |

**Correcting my earlier estimate.** I earlier said about 20% of the designed product existed in code. That number was not measured, and it was wrong: about 60% is built. The accurate statement is:

> **About 60% of the designed product is built. About a third can be reached in any installable build. Almost none of it has reached a phone.** Most of the remaining gap is decisions, supply, trust enforcement and delivery, not missing code.

The five rows that can be built now, with no decision:
- the Home why-this sheet
- the seven-sentence Plan page
- Chat drafts you send
- contribution-policy enforcement
- two-place comparison

## 2. Why the product feels unbuilt: five gaps, in order of size

### 2.1 The delivery gap (largest)

None of the work since mid-August has reached a phone.

- The app has had 1,890 commits since the last build.
- The backend has had 1,673 commits since the production deploy.
- Every installable profile shows Plans / Vesper / Places / Life on the legacy shell. Life is the only new root that ships unflagged.
- CI on the child repositories' `main` branches has not passed since mid-May. From June to early September that was a GitHub billing problem, not the code.
- Merges came in two big batches (375 and 220 commits) after five weeks with no merge.
- Branch protection requires a reviewer a solo founder does not have, so every merge is a bypass.

Details and fixes: [infra §0 and §6](infra-and-process.md).

**Consequence.** No one, including you, has used the product as it exists. Every judgment about it rests on documents, design boards and fixture screenshots. That is why it feels unbuilt, and why describing it is hard: the product in the pitch is not on anyone's phone.

### 2.2 The decision gap

**15 of the 20 unbuilt rows wait on a founder ruling:**
- D04: retained intention and Life AHEAD
- D05: history and continuity
- D06: assistance scope
- D08, D09 and D17: Friends, connection and Follow
- D12: collections
- D13: threads
- D15: the friend's original
- D21: contributor feedback
- D23: Vesper naming
- D24: Live Home
- D33: the artifact type contract for sends
- Q-P1 and Q-P2: Places order and scope

Several **built** rows also cannot be switched on without a ruling. Received originals, place notes and "Leave for someone" all depend on D15 (where the original lives, and whether Keep is a pointer or a copy). Home placement depends on D20.

Eight decision proposals lapse on **Oct 6–7**. The M1 target date (**Sep 28**) cannot be met, and nothing on record says so yet. The newest social direction exists only as board captions ("said in review, Sept 20–26, not yet a recorded decision").

Register, deadlines and recommendations: [decisions §1 and A.1](decisions-and-deprecations.md).

### 2.3 The supply gap

Home and Places are compositions. Without material to compose, they render Quiet or Cold even when the code is correct.

| What exists | Detail |
|---|---|
| Reviewed NYC readings on `main` | **None**. The archived Red Hook set is 3 rows. |
| Legacy Brooklyn corpus | 325 venues. Hours for 12%, photos for 0%, traveler tone, no review state. |
| Home "Here"/"Season" catalogue | **Expires Oct 9**. The CI runway check already fails locally. |
| Events | No producer for an ordinary week |
| Google hours in production | May be off because of a key-name mismatch (`PLACES_GOOGLE_API_KEY` in code, `GOOGLE_PLACES_API_KEY` documented) |

A first supported neighborhood is about 4–6 weeks of mostly editorial work. [Supply §7–9](supply-and-data.md) recommends Williamsburg + Greenpoint, or the neighborhood you actually live in.

### 2.4 The trust gap

The trust promise is the part that sets Vesper apart from Muse: evidence rather than a profile, you send, friends' words stay theirs. It is designed, but not enforced.

- **The T0/T1/T2 contribution policy runs only in shadow.** The facade is `off`/`shadow`, default `off`.
- **About 19–20 chat-turn paths write durable state without a tap to confirm.** The model can set location sharing to "precise". An accommodation tool creates a shared, settleable expense. Private constraints land in the shared planning brief.
- **The relationship pipeline has privacy defects (R1–R6).** Pair notes are admitted for a GROUP audience, "nearby only" leaks the exact place on Home, and revocation has gaps.

These have to be fixed before any shared audience is switched on, which means before the "shared" stage can go live. Details: [backend §6.5–6.6, §8](build-map-backend-static.md).

### 2.5 The build gap (smallest)

- **5 buildable rows** (listed in §1).
- **Kinds without producers:**
  - Home: 14 of 36 designed unit kinds have no producer.
  - Places: 20 of 34 kinds are never emitted, and the field never leaves its default view.
- **Life's payoff layer is missing:** there is no producer for Returns, Threads is a stub, and there is no Keep→Life path.

This is real work. It is also the work the team is best at and has been doing. It is not what is holding the product back.

## 3. The arc view

The product's center is the experience across its arc:
noticed → understood → shared → wanted → arranged → live → kept → returns.

| Arc stage | Rows | Built | Reachable today |
|---|---|---|---|
| noticed | 12 | 75% | 42% |
| understood | 19 | 61% | 26% |
| **shared** | 16 | 62% | **12%** |
| **wanted** | 2 | **0%** | **0%** |
| arranged | 9 | 67% | 56% |
| **live** | 2 | 25% | 25% |
| kept | 12 | 67% | 58% |
| **returns** | 3 | 33% | **0%** |

The stages a default build shows (noticed, arranged, kept) are the ones every travel or places app has. The stages that make Vesper what it is (shared, wanted, returns, and live beyond an itinerary) are either unreachable or not built. So anyone who tries today's build sees a trip planner with a chat.

This is also the order for switching things on:
1. Make "shared" reachable: D15, the privacy fixes, then the `founder` profile.
2. Give "wanted" an owner: D04.
3. Give "returns" a producer: D05, then the Life Returns producer.

## 4. Per surface

Each block states where the design, the build, reachability and supply stand, then the decisions and the next move. "Next move" feeds the [execution plan](execution-plan.md).

### Home: 14 rows. Built 71%, reachable 7%.

- **Design.** The richest of any surface. The adopted core is 02/03 and the 08 pass grammar; 18 K was selected on 09-21. Live lane D was selected on 09-23 but is not adopted. Three kinds are unadmitted (temporal strip, work receipt, money row). The crown order is provisional.
- **Build.**
  - The governed Home is complete as an internal build: crown, seven postures, regions, and 20 renderable kinds, including human place notes, received originals and joined openings.
  - Not built: the why-this sheet, steering, and the Live object and coupon.
  - Region labels differ from Home 11 (C-12).
  - The active H1 lane is polishing hierarchy, received-original fidelity and the Source round trip.
- **Reachable.** Only in an internal binary started with manual flag overrides. `designRefs: []`, so H1 has no accepted reference to be judged against.
- **Supply.** The world band expires Oct 9. There are no NYC readings. The cold-start sample is dark on the backend. Ordinary reads cannot generate supply; recurring supply needs D32.
- **Decisions.**
  - D26: which accepted references (recommended set: 02 top scrolls, 03, 18 K/L, 08 row three, 09b, 17)
  - D20: social placement
  - D24: Live
  - C-05: the three kinds
  - Q-H1: crown order
  - D32: the recurring supply trigger
- **Next move.**
  - Put the governed Home on your phone through the `founder` profile.
  - Register the references.
  - Finish H1 against them.
  - Make the Oct 9 catalogue renewal the first supply task.

### Places: 12 rows. Built 67%, reachable 42%.

- **Design.** The static experience is complete and its absences are unusually well drawn (P03.1–03.4). The interaction work (P10) and the ordering (P05) are proposed, not accepted.
- **Build.**
  - Live by default: the legacy section feed, map, private saved lists and search.
  - Internal only: the World Field and mixed order.
  - The backend emits 14 of 34 kinds and never serves Focus, Path or Live reduction.
  - The scope chooser exists as dead code, and the root ignores a chosen city.
  - "Check a visit now" is a dead end in default builds.
- **Supply.** Brooklyn-only legacy rows. Photos 0%. Governed readings sit behind a flag, with 0 NYC rows.
- **Decisions.** Q-P1 (field order), Q-P2 (scope and map), D30 (launch geography).
- **Next move.**
  - Turn on the governed field in the `founder` profile.
  - Fix the city-ignoring and dead-end paths; both are small.
  - Supply one neighborhood.

### Place page: 8 rows. Built 88%, reachable 19%.

- **Design.** The most ready to build. Use E06 chrome and E14 R1–R5; reconcile the P08 register with E06 (C-10). E09 still contradicts the 09-09 decision (C-01).
- **Build.**
  - The rebuild (Keep, Ask Vesper, Tonight?, Read up, Leave for someone) exists behind `OBJECT_PAGE_REBUILD_ENABLED`, which no profile sets. At runtime it lacked the E06 plate, byline and closing row, and showed internal labels (§6).
  - The default is the 2,018-line legacy venue page. There are six or more coexisting place renderers.
  - **A live bug:** "Leave this place for someone" renders without its flag on three legacy surfaces and 404s.
- **Decisions.**
  - Q-E1: chrome.
  - D15: the people lines and handoffs.
  - Making the rebuild the default (app build map §5.3, high risk).
- **Next move.**
  - Gate the doorway now.
  - Make the rebuild the default in the `founder` profile.
  - Converge the renderers after cutover.

### Life: 9 rows. Built 44%, reachable 22%.

- **Design.** Complete for ordinary, thin and zero states. There are no large-text boards. The future half (P1 AHEAD, the kept intention) waits on one owner decision.
- **Build.**
  - **The only new root live by default.** Four lenses and "Everything kept". At runtime the lenses showed the same single entry, and the record link was broken (§6).
  - Refind and shared originals are internal only.
  - Missing: a producer for **Returns**, Threads (only a stub), and **Keep→Life**; saves do not reach Life.
  - Life reads the Atlas timeline, so Atlas cannot be deleted outright.
- **Decisions.**
  - D04/D14: AHEAD
  - D05: the returns and continuity policy
  - D12/D13: collections and threads
  - D15: custody of originals
- **Next move.**
  - Hold these decisions in one session.
  - After that, the first Life build is a **Returns producer**. It closes the loop the pitch depends on: what you kept comes back.

### Plans: 8 rows. Built 69%, reachable 69%.

- **Design.** The rules are adopted (07, the seven sentences). The references are 03 B, 08 P, 11 I1 and 05 D3. There is no cold Plans page, by design. Multiplayer (04) and following (12 W) are proposed.
- **Build.**
  - Live: the legacy itinerary rail, change sheets and Send proposal (a message you send).
  - Dogfood: LocalPlan and the outcome artifact.
  - Not built: the seven-sentence page. The flagged `CurrentShapeSurface` violates the no-status-buckets rule (C-21).
- **Decisions.** D16 (the Trip ↔ Plan/Occasion link) and D04 (loose plans).
- **Next move.** The seven-sentence page is **buildable now**. It is a good candidate for a second, independent lane, because it does not touch Home's files.

### Chat: 9 rows. Built 44%, reachable 44%.

- **Design.** The most finished design: Direction B was selected on 09-13, with 17 rulings on 09-14. B2 and O1 await your ruling; decisions 08 and 23 are open.
- **Build.**
  - Answering, attachments and queued turns are live. At runtime the **Chat root composer was blank** in every build tried; threads work (§6).
  - The header still says "Vesper" (D23).
  - Twenty card types are active, including booking.
  - Drafts you send are not built.
  - **The contribution policy is not enforced.**
- **Decisions.** D23 (naming), D05 (history), D18 (group rooms).
- **Next move.** Treat trust enforcement as a named package: move the policy from shadow to enforced on Ask, and add confirmations to the three high-risk tools. It must land before Chat is on by default for anyone but you.

### Social: 7 rows. Built 43%, reachable 14%.

- **Design.** Moving. Multiplayer Shapes was edited today, and the newest direction has no decision record. High-severity contradictions remain:
  - group chat versus rooms versus the voting Trip room;
  - Follow versus Friends;
  - three or four person pages;
  - where the original lives.
- **Build.**
  - Sending and receiving originals and place notes is built and dark (16 routes behind `RELATIONSHIP_UUID_HANDOFFS_ENABLED`).
  - The roughly 8,000-line source-contribution worker is built and dark.
  - Not built: collections, human acts on shares, and Friends.
  - Follow and voting are live, and both are legacy.
- **Decisions.** D02, D08, D09, D10, D15, D17, D18, D19, D21. Most of them lapse on Oct 7.
- **Next move.** A decision session first. Then privacy fixes R1–R6. Then the first slice, **a friend's place, end to end**: send → receive on Home → keep → it returns.

### You: 4 rows. Built 75%, reachable 75%.

- **Design.** Rules 0-0 to 0-4 are well ruled. The design assumes mutual Friends, which the code does not ship. Block and the recipient's side of a request are not drawn. The "what Vesper used" ledger was an orphaned idea.
- **Build.** Portrait, trust controls and memory are live. The person page (friend state, shared axis) is not built.
- **Decisions.** D17.
- **Next move.** Follows the Social decisions.

### Cross-cutting: 4 rows. Built 38%, reachable 38%.

- **Share sheet:** live, but a near dead end. Capture is review-first and redirects out of the source app. A kept interpretation becomes only a private anchor, and a share never becomes a save. Per the founder's Sep 26 direction this is the primary mode, so it is the first slice after H1 (F0).
- **Artifact contract:** not built. There are 8+ vocabularies and no single typed shape for a send (D33).
- **Push:** registration is built. Delivery depends on the Fly secret `EXPO_PUSH_ENABLED` and APNs, and neither is verified.
- **Onboarding:** there is no home-city step, which Home and Places supply need.
- **Next move:** set up push with the founder checklist, and add a home-city step when supply lands.

## 5. Full capability table

"Blocked by" names the ruling needed to **build** a row. For rows that are built but dark, it names what is needed to **switch it on** ("on:").

**Home**

| Capability | Build state | Backend | Arc stage | Blocked by |
|---|---|---|---|---|
| Crown (dominant unit) | Internal only | — | understood | on: founder profile |
| Seven postures | Internal only | — | understood | on: founder profile |
| Regions and labels (design 11 mapping) | Partial | — | understood | Q-H5 label ruling |
| WorldRead / WeekShape / RestClose | Internal only | — | noticed | on: founder profile |
| Degradation notice after value | Internal only | — | understood | on: founder profile |
| Why-this sheet | Not built | — | understood | — (buildable) |
| Steering (not this / less like this) | Not built | no producer | understood | D06 |
| Live object crown + coupon (lane D) | Not built | no producer | live | D24, C-03 colour |
| Received originals | Internal only | backend flag off | shared | on: D15 + R1–R6 |
| Addressed place notes | Internal only | backend flag off | shared | on: D15, D20 + R2/R4 |
| Joined human openings | Internal only | backend flag off | shared | on: D20 |
| Cold-start sample | Internal only | backend flag off | noticed | on: backend flag + secret (H1 lane) |
| Source inspection request/return | Internal only | backend flag off | understood | on: worker cohort flag, D32 |
| Full unit vocabulary (22 of 36 kinds produced) | Partial | — | understood | C-05 (three kinds) |

**Places**

| Capability | Build state | Backend | Arc stage | Blocked by |
|---|---|---|---|---|
| Section feed by context | Live (default build) | — | noticed | — |
| World Field (semantic units) | Internal only | — | noticed | on: founder profile |
| Mixed order | Internal only | — | noticed | on: founder profile |
| Pocket / map | Live (default build) | — | noticed | — |
| Scope chooser (P10) | Not built | — | noticed | Q-P2 |
| From friends | Partial | backend flag off | shared | on: D08 + R3 |
| Checks / visit fit | Partial | — | arranged | — (dead end in default build) |
| Saved collections (private) | Live (default build) | — | kept | — |
| Inline search | Live (default build) | — | noticed | — |
| Field states beyond default (Focus / Path / Live reduction) | Not built | no producer | arranged | Q-P1/Q-P2 |
| Two-place comparison | Not built | no producer | understood | — (buildable) |
| Governed readings (primitives) | Internal only | backend flag off | understood | on: supply + flag |

**Place page**

| Capability | Build state | Backend | Arc stage | Blocked by |
|---|---|---|---|---|
| Invariant shell (E06 rebuild) | Partial, internal only (runtime: no plate, byline or closing row; internal labels visible) | — | understood | on: founder profile; Q-E1 |
| Keep verb | Internal only | — | kept | on: founder profile |
| Ask Vesper verb | Live (default build) | — | understood | — |
| Leave for someone | Internal only | backend flag off | shared | on: D15 + R1–R6 (legacy doorway bug C15) |
| Tonight? verb | Internal only | — | arranged | on: founder profile |
| Read up | Internal only | backend flag off | understood | on: research canary allowlist |
| Purpose-responsive body (E14) | Partial | — | understood | — |
| People lines / face sheet | Internal only | backend flag off | shared | on: D15 |

**Life**

| Capability | Build state | Backend | Arc stage | Blocked by |
|---|---|---|---|---|
| Root with four lenses | Partial (runtime: lenses do not reorganise; record entry "no longer available") | — | kept | — |
| Dossier per record | Partial | — | kept | — |
| Refind | Internal only | — | returns | on: founder profile |
| Shared-with-you originals | Internal only | backend flag off | shared | on: D15 |
| Everything kept (full record) | Live (default build) | — | kept | — |
| Returns | Not built | no producer | returns | D05 |
| Threads / pursuits | Not built | no producer | returns | D13 |
| Keep → Life gesture | Not built | no producer | kept | D12/D15 |
| AHEAD (retained intention) | Not built | no producer | wanted | D04 |

**Plans**

| Capability | Build state | Backend | Arc stage | Blocked by |
|---|---|---|---|---|
| Itinerary rail + stop sheet | Live (default build) | — | arranged | — |
| Change sheets + undo | Live (default build) | — | arranged | — |
| Seven-sentence Plan page | Not built | — | arranged | — (buildable; rules adopted) |
| Send proposal (you send) | Live (default build) | — | arranged | — |
| Contextual Ask pill / value-first stop sheet | Partial | — | arranged | — |
| Local (non-trip) Plan | Dogfood build | — | arranged | D16 |
| Outcome artifact / micro-journey | Dogfood build | — | kept | — |
| Loose / order-less plan | Not built | no producer | wanted | D04 |

**Chat**

| Capability | Build state | Backend | Arc stage | Blocked by |
|---|---|---|---|---|
| Answering (Ask) | Partial (runtime: Chat root composer blank in every build tried; threads work) | — | understood | — (diagnose first) |
| Unnamed header / unsigned answers | Not built | — | understood | D23 |
| Cards only when earned | Partial | — | understood | booking cards retire (B5) |
| Side chat | Partial | — | shared | D18 |
| Drafts you send | Not built | — | shared | — (buildable) |
| Scope line from objects | Partial | — | understood | — |
| Attachments | Live (default build) | — | noticed | — |
| Queued turn | Live (default build) | — | understood | — |
| Contribution policy enforced (T0/T1/T2) | Not built (shadow only) | — | kept | — (buildable) |

**Social**

| Capability | Build state | Backend | Arc stage | Blocked by |
|---|---|---|---|---|
| Send an original | Internal only | backend flag off | shared | on: D15 + R1 |
| Receive (Home, Life, detail) | Internal only | backend flag off | shared | on: D15 |
| Collections / Shared with X | Not built | no producer | kept | D12 |
| Human acts on shares (like, reply, keep) | Not built | no producer | shared | D21 |
| Audience controls | Partial | — | shared | D08 |
| Guests (link without account) | Partial | backend flag off | shared | D10 |
| Connecting / Friends | Not built | no producer | shared | D08/D09/D17 |

**You**

| Capability | Build state | Backend | Arc stage | Blocked by |
|---|---|---|---|---|
| Portrait | Live (default build) | — | kept | — |
| Person page (friend state, shared axis) | Not built | backend flag off | shared | D17 |
| Trust controls | Live (default build) | — | kept | — |
| What Vesper knows / used | Live (default build) | — | kept | — |

**Cross-cutting**

| Capability | Build state | Backend | Arc stage | Blocked by |
|---|---|---|---|---|
| Share-sheet capture | Partial (review-first; share never becomes a save) | — | noticed | D34 |
| Typed artifact contract for sends | Not built | no producer | noticed | D33 |
| Push delivery | Partial | backend flag off | live | on: `EXPO_PUSH_ENABLED` + APNs (founder) |
| Onboarding (home city) | Partial | — | noticed | — |

## 6. Runtime evidence

The full record is [build-map-runtime.md](build-map-runtime.md), with 290 screenshots in [`screens/`](screens/).

**How it was run.**
- Lane `codex/product-map-inventory`, on an iPhone 16 simulator, in three passes:
  1. the internal four-root build with mocks;
  2. the default legacy shell;
  3. the four-root build against a real local backend with one synthetic, lane-only user.
- **Binary.** It used the **09-22 dev client**, because the 09-26 dev client was built from the H1 lane's uncommitted native pair (worklets 0.7.4), which does not match merged `main` (0.12.1).
- **Offline setup.** The merged backend would not start offline without an `ANTHROPIC_API_KEY` (the fix, `6c792ed8b`, is unmerged), so a non-secret placeholder was used. Nothing reached a provider.
- **Maps.** No Mapbox token was used, so maps are blank.

**Where the run agreed with the static maps:**
- Both shells work as navigable apps.
- Home renders all seven postures, with a crown, a week strip, labelled regions and the rest-keeps close.
- Places is rich across personas.
- Booking, invites, public share pages, notifications, search, trust controls, the legacy itinerary and the dev galleries all render.
- Against the real local API, a fresh user gets 200 responses everywhere, but content is thin:
  - Home says "The week is open".
  - Places says "Nothing leads this field yet".
  - Life is empty.
  - Chat shows US national-park seasonal rows.

  This is the supply gap (§2.3), seen directly.

**Where it changed a row** (already applied in §1 and §5):
1. **Chat root has no composer.** The docked "ask" band is an empty panel in the four-root Chat, the legacy Vesper tab and the real-local build. The accessory from `app/(tabs)/concierge/index.tsx:168–202` never mounts into `FloatingTabBar`. Threads opened elsewhere have a working composer. The cause, JavaScript or the 09-22 binary, is **not yet diagnosed**. It is now the first acceptance check of the `founder` build.
2. **Life lenses do not reorganise.** Time, Places, Threads and People show the same single entry for every persona. Opening it says "That record entry is no longer available".
3. **The rebuilt place page is incomplete.** It lacks the E06 plate, byline and closing row. Its two actions are misaligned. Internal labels ("ADJUDICATED", "CATALOG") are visible.

**Other defects to fix** (listed as tasks, no row change):
- **Chat context and consent.** Home → Ask Vesper opens a blank chat that loses the card's context. The place page → Ask Vesper keeps the context, but its reply mentions "Discover". Both it and the legacy Plans chat button **send a message on the user's behalf without review**, which breaks "you send".
- **Mock-mode crashes.** The original reader crashes in mock mode (`mock://` fetch). No baseline persona receives an original, so received-original Home units were **not observed** at runtime on the baseline. Legacy Plans crashes for the Dev persona (`utils/api/mock/tripsPlan.ts:1768`).
- **Internal Plan Shape.** It counts "deciding" and "nothing booked" as settled, and misplaces days. It also replaces the day-by-day view, so all six itinerary flows fail when it is on.
- **Retired names in the four-root build:**
  - "The itinerary stays in Trips"
  - an "Atlas" search chip
  - "Trips / Vesper" notification filters
  - "Ready for Atlas"
  - "Discover" in chat
- **Fixture problems:**
  - Home is always dated "Tuesday, Sep 1", with the same week strip in every posture.
  - The Live headline says "tonight" while its card says "Saturday".
  - A "Canonical outcome" caption is visible.
  - Chat headers have no background, so text scrolls under them.
- **Many registered Maestro flows fail.** They wait for tab labels that no longer exist ("Discover", "Trips", "Plans", "Vesper"). The QA harness itself needs a pass.

**Cleanup done by the run.**
- Services were stopped, with volumes kept.
- The simulator was shut down.
- The synthetic user was deleted.
- The only lane file changed was `.workspace-lane.json`, to record the device.

## 7. Not counted here

**Legacy product that is still live and slated for retirement:**
- trip-first Plans home
- booking (with Bland.ai restaurant calls still reachable)
- voting default
- facilitator
- Follow
- Atlas/Discover remnants
- expenses UI

See [decisions Part C](decisions-and-deprecations.md) and [app §5](build-map-app-static.md) / [backend §7](build-map-backend-static.md).

**Also outside this map:**
- **Operations and cost safety:** kill switch, fan-out caps, `seed_city_full`, and the booking retirement flag. See [infra §5](infra-and-process.md).
- **Design fidelity and visual polish:** see the atlases §4–6.
- **Design debt:**
  - 52 before-copies
  - package drift (VDL 0.4.1 vs 0.3)
  - three stylesheets
  - legacy projects still acting as authority

## 8. How to keep this current

- When a row's state changes, edit it in the §5 table. The totals are simple sums over that table, using the scoring in §0.
- Update a row only on evidence:
  - a merged commit, for Built;
  - a profile or flag change, for Reachable;
  - the definition of done in the [execution plan](execution-plan.md), for Delivered.
- **Delivered is the number to watch.** It should rise every week from now on.
