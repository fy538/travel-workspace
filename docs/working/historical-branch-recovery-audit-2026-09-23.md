---
doc_type: working
status: active
owner: product-engineering
created: 2026-09-23
expires: 2026-10-23
why_new: An exhaustive, dated disposition of three repositories' retained branch tips and detached worktree commits is needed before selective recovery or branch pruning; the program roadmap cannot serve as a historical Git inventory.
supersedes: []
---

# Historical branch recovery audit — September 23, 2026

This began as a read-only audit and is now a **proposed recovery queue plus
dated preservation and selective-lane receipts**, not product canon or a
whole-branch merge authorization. The [program
roadmap](vesper-program-roadmap.md), current owner contracts, and live code
continue to decide what to build. “Retire” below means *no whole-branch merge
or current feature port*; it does **not** mean a Git ref or worktree was deleted.

## Scope and evidence boundary

| Repository | Main HEAD | Historical local Codex tips | Remote-only dependency tips | Worktrees |
|---|---|---:|---:|---:|
| Workspace | `992e22a` | 28 | 0 | 57 |
| Backend | `fdf789d06` | 31 | 5 | 58 |
| App | `23cff76f4` | 24 | 6 | 58 |

All three main checkouts matched `origin/main` and were clean at inspection.
All inspected worktrees were clean in tracked and ordinary untracked files;
ignored runtime artifacts were not inventoried. The audit compared branch
history, patch equivalence, tip files and current owners. Patch inequality
alone was **not** treated as proof that a behavior is missing, and a clean
simulated merge was **not** treated as a reason to merge. No tests, native
captures, migrations, merges or deletions were performed in the audit. The
preservation action below subsequently created exact local refs. A
recommendation must be rechecked against fresh Git state before execution.

The 83 tips span 48 named families. Many carry a cumulative September branch
lineage, so their whole-tree diffs exaggerate what remains useful. Recover
specific behavior and tests under current contracts, never a historical
branch wholesale.

## Recovery lane progress (not landed on main)

The isolated `codex/home-human-opening-recovery-2026-09-23` lane now contains
backend tip `a277ba617` and app tip `9372e154c`. It selectively adapts the
human-note/current-Place join and gives the attributed note a human-first
native hierarchy. The join is limited to pending notes so Keep cannot make
an already-handled contribution look newly received. Three existing native
rehearsals now resolve the presented unit by its exact handoff and venue owner
refs rather than assuming the standalone unit ID; absent or ambiguous matches
fail.

At the earlier code tuple, the backend root-projection suite passed (`494` tests) and the
full offline backend selection passed (`21,758` passed, `14` skipped, `1,458`
deselected, `53` xpassed). App TypeScript, its Home screen suite (`20` tests),
offline suite (`126` tests), and the changed QA-runner tests (`12` tests)
passed. The Home design-reference check is doctrine-only, so native rendering
does not establish design-intent parity.

On September 23 this recovery lane reserved a separate iPhone 16 Pro Max
simulator (`074FD906-F69B-447E-93AD-83DA52D30E2A`) and ran Home Root's
polish-QA doctor successfully with its own Metro port `53936`, Maestro
`2.6.1`, and OpenJDK 17. The initially installed July Vesper binary and Expo
Go both had Worklets native `0.11.3` versus JS `0.12.1`. A cached September
22 custom development bundle with native Worklets `0.12.1` was installed on
the reserved device without changing source or building against the absent
Mapbox download token. All seven registered mock Home postures captured on
that matching native binary. They establish native rendering across the
postures, not true-world supply, visual parity to a verified Claude reference,
or social owner behavior. The other lane's booted simulator was not used.

The first real-API Home addressed-note rehearsal reached the exact note and
performed Keep but failed its final return assertion. A fresh Home API read
proved the cause: the relationship owner correctly changed the note to
`kept` at revision 1, while Home still emitted the handled note as a `current`
receiving unit. Backend `4327c09fa` now admits an addressed note to Home only
while `available`; it leaves the kept note in its Place owner and eligible for
authorized later Source use. The corrected root-projection suite passed
(`495` tests). The same iPhone 16 Pro Max, real local PostgreSQL/API, selected
fixture account, and live Home/Place owner routes then passed the full native
Home → exact Place note → Keep → exact revision read → Home return flow; the
disposable sender/venue fixture was cleaned. This proves the standalone
receiving path and its handled-state transition. A second disposable fixture
temporarily gave the eval-only recipient a SoHo Home and two verified nearby
venues. Paired with the existing SEND_NOW note at the same café, it forced the
server's exact-entity `home.human-opening.*` composition. The app's
`run-home-real-joined-opening.sh` passed the full real-API native Home → joined
note → exact Place owner read → Keep → advanced-revision owner read → Home
withdrawal/return flow on the reserved device. The script cleaned both
fixtures; a fresh API read showed no pending note unit and direct DB checks
found no temporary Home or companion venues. The root-projection suite passed
`499` tests and six focused app runner checks passed at backend `e2838dbea`
and app `29cc92a97`. A further September 23 quality pass removed the mechanical
“In Places” prefix from the joined unit, kept normal empty optional owner
scopes out of the user-facing retry notice, and moved genuine partial-state
notice below admitted Home value without suppressing it. Focused tests and
the full root-projection suite passed (`503` tests); the app Home screen suite
passed (`21` tests), TypeScript and targeted ESLint passed, and the real-API native
joined flow passed again and exact fixture cleanup was verified. The Home-root
scenario registry and doctor passed on the lane's Metro/device, while the
design check reports a doctrine-only surface with no design-ref manifest.
This is still structural and limited presentation evidence, not strict visual
parity or proof that the opening is worth receiving. The fixture's generic
nearby venues make the surrounding feed thin; contextual value needs a
separate design/content review against a verified reference. A fresh iOS build
would still need the missing Mapbox download token.

The required full gates are **not green**. `make verify` stopped at eight
expired world-catalog rows; current backend main fails the same check. Separate
contract and API coverage checks found `55` expired operation-review policies
on current workspace main too. App `verify:pr` stopped at `59` expired
schema-bridge exceptions in an unchanged manifest. The Maestro governance
check reports the same `12` findings on main and this lane. Backend mypy
reports the same `329` errors in `69` files on main and this lane (the only
Home portfolio error shifts one line after the new import; no error points to
the new join). These are current baseline/owner-review work, not permission to
bump dates or bypass gates in this recovery lane. The lane remains clean,
unmerged and unpushed; it is not product acceptance. The Places mixed-order
and Source activation decisions below remain gated.

The updated audit document passed governance, inventory, spine, canon,
release, status, links and Home-surface documentation checks. `make docs-check`
still exits nonzero at the unchanged compatibility ledger: the
`discover-url-bridge`, `atlas-tab-url-bridge` and `discover-map-api-bridge`
rows expired September 15. No expiry was silently renewed for this recovery.

## Cross-repository decision

| Priority | Candidate | Disposition and acceptance boundary |
|---|---|---|
| 1 — built and native path rehearsed in isolated lane; quality and landing pending | One attributed human Place note joined to one current-world Place opening | Backend `engine-er123-integration` / `native-receiving-next` supplied a selective reference; current main supplies `people_note_door` and `horizon_aperture_row` separately. The lane above adapts the exact-entity, single-author join and native treatment while preserving both owner reads and fallbacks. Standalone and joined addressed-note exact destination/Keep/return now pass on a real local backend and reserved device with disposable fixtures. Value/copy review, design-reference comparison and landing remain. This is a current-Home value slice, not a branch merge. |
| 2 — contract decision | One server-authored mixed Places page order | Backend `engine-er123-integration` and app `quality-comparison` / `native-receiving-next` / `timing-proactive-delivery` contain a `page_sequence` approach. Current Places contract says the section list is the sole client-visible order, while current app still locally promotes the dominant browse section. Decide one canonical order for both semantic units and mature sections; do **not** add a competing order array. Then adapt producer, OpenAPI/types, app renderer and order/exposure tests together. |
| 3 — policy decision | Automatic returned-Source activation | `strategy-useful-supply` and `native-receiving-next` contain trigger/work-item code, but the current roadmap explicitly holds `trip.completed` activation pending source, purpose, audience, lineage, correction/withdrawal, expiry, duplicate and sparse behavior. Do not port this under a generic “resume old work” instruction. It does not block ordinary Home composition. |
| 4 — separate receiving option | Timed delivery of an *already explicitly requested* Source result | `timing-proactive-delivery` adds durable reconsideration, exact workflow reread and in-app Activity destination. This is separable from automatic activation, but still needs an explicit background/notification treatment decision, current delivery-contract adaptation, migration/restart evidence and app destination authority checks. |
| Later, if a measured gap | Per-run engine trace / scarce owner-read ordering | ER1/ER2/ER3 contain content-free trace and read-order ideas. Main has newer shared composition, bounded owner reads and aggregate telemetry. Recover only against a demonstrated missed-candidate or diagnostic problem, with privacy and latency checks. |

The old `cw2-object-continuity` workspace tip also preserves a detailed
human-Reply safety gate. Review it against the current Social/Relationships
owner before exposing Reply; do not revive the reverted old original-reply
implementation. `package-b-answers-help` and `requested-visit-window` are
separate product/owner choices, not cleanup work.

## Complete local-tip disposition

Names in these tables omit the common `codex/` prefix. A branch appearing in
multiple repositories is assessed **per repository**; a stale workspace
checkpoint does not imply its child implementation is discardable.

### Workspace — 28 tips

| Disposition | Branches |
|---|---|
| Patch-equivalent to main | `engineering-reliability-2026-09-07` |
| Stale checkpoint; current owner docs/receipts are newer | `content-quality-corpus-2026-09-08`, `dogfood-experience-docs-2026-09-15`, `engine-er123-integration`, `experience-feedback-roadmap-2026-09-16`, `home-acceptance-2026-09-08`, `home-content-receiving-2026-09-08`, `home-pier57-quality-2026-09-08`, `later-reuse-2026-09-10`, `life-anchor-contract-2026-09-08`, `multiplayer-design-exploration-2026-09-20`, `practical-judgment-2026-09-09`, `purpose-receiving-2026-09-10`, `receiving-completion-2026-09-10`, `strategy-return-loops-2026-09-10` |
| Re-export only if a corresponding child feature is accepted; old generated snapshots/policy are stale | `content-quality-correction-2026-09-08`, `life-human-continuity-2026-09-10`, `life-refinding-2026-09-10`, `situated-value-supply-2026-09-10` |
| Historical evidence only; do not promote an old QA receipt to the current tuple | `acceptance-runtime-2026-09-08`, `life-7b-reader-comparison-2026-09-08` |
| Selective owner review, not branch merge | `cw2-object-continuity-2026-09-11` (Reply gate), `package-b-answers-help-2026-09-11` (dark assistance flag), `package-d-gates-2026-09-11` (entity rollout gates), `native-receiving-next-2026-09-15` (still-open engineering-health findings only), `situated-intelligence-map-2026-09-12` (expiring research), `social-ordinary-sharing-2026-09-08` (unresolved audience/source policy), `timing-proactive-delivery-2026-09-16` (historical timing plan; current trigger policy wins) |

### Backend — 31 tips

| Disposition | Branches |
|---|---|
| Patch-equivalent or substantially absorbed in newer owners; retain tests only where a current gap is found | `acceptance-runtime-2026-09-08`, `content-quality-corpus-2026-09-08`, `home-content-receiving-2026-09-08`, `integration-execution-2026-09-08`, `life-anchor-contract-2026-09-08`, `life-human-continuity-2026-09-10`, `plan-assistance-2026-09-10`, `purpose-receiving-2026-09-10`, `life-real-evidence-2026-09-08`, `requested-visit-window-2026-09-10`, `situated-value-supply-2026-09-10`, `practical-judgment-2026-09-09`, `changed-world-behavior-2026-09-10`, `supply-lifecycle-2026-09-10`, `supply-lifecycle-n2-2026-09-11`, `restart-acceptance-2026-09-11`, `package-b-answers-help-2026-09-11`, `package-b-receiving-return-2026-09-11`, `package-d-gates-2026-09-11`, `cw2-object-continuity-2026-09-11`, `situated-intelligence-map-2026-09-12`, `receiving-completion-2026-09-10`, `experience-feedback-roadmap-2026-09-16`, `engine-er3-read-execution` |
| Selectively recover only after current-owner adaptation | `engine-er1-evidence-continuity` (run trace), `engine-er2-workflow-truth` (run/outcome trace), `engine-er123-integration` (human/Place join), `native-receiving-next-2026-09-15` (join) |
| Product/notification-policy gated | `strategy-useful-supply-2026-09-15` (automatic activation), `timing-proactive-delivery-2026-09-16` (result timing and Activity) |
| Uncertain, low-priority old-tail behavior | `content-quality-correction-2026-09-08` (HTTP fallback specific to old optional semantic reading tail) |

This table classifies the **backend** `package-b-answers-help` implementation
as largely absorbed; the app's absent Graph assistance surface and workspace
flag remain a separate product choice below.

### App — 24 tips

| Disposition | Branches |
|---|---|
| Largely absorbed in newer main behavior | `content-quality-correction-2026-09-08`, `cw4-life-native-2026-09-12`, `engineering-reliability-2026-09-07`, `home-content-receiving-2026-09-08`, `integration-execution-2026-09-07`, `life-7b-reader-comparison-2026-09-08`, `life-human-continuity-2026-09-10`, `native-receiving-2026-09-10`, `package-b-receiving-return-2026-09-11`, `package-c-native-2026-09-11`, `plan-assistance-2026-09-10`, `practical-judgment-2026-09-09`, `purpose-receiving-2026-09-10` |
| Selective recovery or reusable QA only | `acceptance-runtime-2026-09-08` (cold-city/lens fixtures), `cw1-native-receiving-2026-09-11` (source anatomy/QA), `cw4-home-native-2026-09-12` (ordinary-NYC/native-original QA), `engine-er123-integration` (mixed Places order), `native-receiving-next-2026-09-15` (mixed order and human note treatment), `quality-comparison-2026-09-15` (mixed order/quality fixtures), `timing-proactive-delivery-2026-09-16` (Source-result destination and mixed order) |
| Product/owner decision | `package-b-answers-help-2026-09-11` (private Graph assistance), `requested-visit-window-2026-09-10` (custom window versus main's fixed next-two-hours action) |
| Superseded branch shape | `cw2-object-continuity-2026-09-11` (Life absorbed; original-reply experiment reverted), `home-acceptance-2026-09-08` (old header audit) |

### Remote-only dependency branches — separate maintenance queue

Backend has five remote Dependabot tips. `pytest-randomly-gte-5.0.0` is already
covered by main's dev lock; two older Python patch groups are superseded by
`python-minor-patch-1978744215`, which itself needs a fresh dependency/lock
review from current main. `sentence-transformers-gte-6.0.1` concerns an
optional retired legacy embedding input and is low priority. App has six
remote Dependabot tips: two overlapping old npm patch groups should be
replaced by a fresh update, while React Native 0.87.1, Purchases 10.10.0,
Purchases UI 10.10.0 and Worklets 0.13.0 need independent Expo/native
compatibility review. None is a product-branch recovery candidate.

## Detached worktrees: preservation gate before cleanup

Fifteen clean detached worktree HEADs were not reachable from any named local
or remote branch at audit time. Removing their worktrees without first
recording exact commit refs could have made their histories difficult to
recover. On September 23, all 15 were protected by local
`refs/archive/branch-audit-2026-09-23/<short-hash>` refs in their respective
repositories, each created from a verified exact commit with a create-only
compare-and-swap. They have not been pushed; another clone will not have
these recovery refs unless they are explicitly published or bundled.

| Repo | Unreferenced HEADs | Assessment |
|---|---|---|
| Workspace | `40044cd6ab` (content Home receipt), `c11cc8fff6` (Home source checkpoint), `813deb7284` (Home factual context), `b9abf374f8` (Life capture shadow), `128ea16005` (old generated Plan API snapshot) | Each has one tip commit beyond named refs; main has newer corresponding owner material. Low feature-port priority, but protect exact commits before worktree removal. |
| Backend | `3cce198dd9` (Home public content), `57ebb95652` (Home trip context), `5dbf7eb019` (Life capture shadow), `6d2b84d72d` (Life withdrawal) | Each single detached tip is patch-equivalent to main. Preserve exact identity before pruning if historical recovery matters. |
| Backend — high attention | `7b93243be2` (finished-lane docs) | Tip patch is equivalent, but its inherited lineage has 106 patch-distinct commits. Local ref preserves the tip; review any targeted recovery before removing the worktree. |
| App | `5f6a068cdf` (Source results), `70453a0bd9` (Place depth), `019c81b7bb` (baseline repair), `6ab20f227d` (social touch target) | Each single detached tip is patch-equivalent to main. |
| App — high attention | `ae8100363b` (receiving history) | 130 ancestry commits are patch-distinct from main; includes the absent mixed Places ordering and custom visit-window work. Local ref preserves the tip; targeted review still precedes worktree pruning. |

The September 23 read-only lineage check confirmed why tip-only cleanup would
be misleading. Backend `7b93243be2` has `128` commits beyond its merge base:
`106` patch-distinct from main and `22` patch-equivalent. App `ae8100363b`
has `155`: `130` patch-distinct and `25` patch-equivalent. Their tip commits
are finished-lane documentation checkpoints, while their ancestry ranges
across Source preparation/continuity, Home and Places receiving, Life
organization, practical windows, native QA, and the explicit mixed Places
order. Patch-distinct means *not the same patch*, not *missing behavior*;
current main often has newer owners and different implementation. The
identified selective candidates and product gates above remain the recovery
queue. These two refs and worktrees are retained; no ancestry was bulk-merged
or pruned on the strength of a tip comparison.

## Plan of attack

1. **Preserve before pruning — local refs created, lineage audit still open.**
   Recheck all three statuses and worktree inventories before cleanup. The 15
   detached HEADs now have local retention refs, especially backend
   `7b93243be2` and app `ae8100363b`; audit their inherited commits before
   removing worktrees. Publish or bundle the refs if cross-machine recovery
   is required. Do not delete refs/worktrees merely because a tip patch is
   equivalent.
2. **Run one small product recovery lane.** In an isolated coordinated
   workspace lane, adapt the Home human-note/current-Place join to current
   backend and app code. Keep the old branch read-only. Prove exact entity,
   attribution, owner read, audience, withdrawal, no arbitrary author choice,
   practical/open-now distinction, one seat, fallback and useful native
   hierarchy. Compare ordinary and returned Home, and follow the exact
   destination and return. No new social store or generic Home generator.
3. **Resolve the Places ordering decision in parallel.** Establish whether
   the current section list can represent standalone semantic units or needs
   one replacement ordered sequence. The same server-authored order must
   govern backend, OpenAPI, app, delivery exposure and direct-section handoff.
   Then implement/test the chosen contract in a separate lane; do not
   cherry-pick `page_sequence` while the existing sole-order rule stands.
4. **Keep Source activation and delivery separate.** Decide the automatic
   trigger's source/purpose/authority/lifecycle before porting intake jobs.
   Independently decide whether a result explicitly requested by the person
   merits timed in-app Activity; only then adapt temporal delivery and app
   destination, with restart/duplicate/expiry and authority-readback tests.
5. **Recover observability only against a named failure.** Use old ER run
   traces or scarce-read ordering as implementation references if current
   Home/Places acceptance reveals an unexplained omission or contention.
   Do not introduce a parallel engine ledger merely because old code exists.
6. **Retire branches after evidence, not by age.** For each family, record
   current-main equivalent, ported commit/test, explicit rejection or pending
   product decision. Verify branch-associated worktrees are clean, detached
   HEADs protected, and cross-repo generated contracts current. Then retire
   stale local refs/worktrees in a separately authorized cleanup operation.
   Review Dependabot updates through the normal dependency lane, not this
   historical product recovery.

The plan favors the current roadmap's owner-backed Home composition. Branch
recovery should create a better experience for a person, not become a
repository-wide integration project.
