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

This began as a read-only audit. On September 23 the founder explicitly asked
this task to finish useful integration and clean the dangling branches. It is
now the **execution/disposition ledger for that consolidation**, not product
canon or a direction to merge every historical implementation wholesale. The
[program roadmap](vesper-program-roadmap.md), current owner contracts, and live code
continue to decide what to build. “Retire” below means *no whole-branch merge
or current feature port*; it does **not** mean a Git ref or worktree was deleted.

## September 23 actual historical retirement — latest inventory

The historical disposition is now executed, not just proposed. At 22:35 UTC,
**83 local historical branch names and 167 historical worktrees were removed**.
The older inventory and receipts below remain provenance, not current counts.

| Repository | Branches removed | Local branches remaining | Worktrees removed | Worktrees remaining |
|---|---:|---:|---:|---:|
| Workspace | 28 | 2 | 55 | 3 |
| Backend | 31 | 2 | 56 | 3 |
| App | 24 | 2 | 56 | 3 |
| Total | 83 | 6 | 167 | 9 |

Each repository retains only `main` and
`codex/home-human-opening-recovery-2026-09-23` as local branches. Its three
checkouts are canonical main, the active recovery lane, and the detached
`functional-implementation-2026-09-20--native-presentation-wave1-2026-09-21`
lane. Xcode's `DTServiceHub` (PID 25951 at recheck) still holds a screenshot
directory in that lane. All three checkouts in that coordinated lane were
retained; no unrelated Xcode process was killed. Recheck live ownership before
removing them. The seven cached remote dependency branches remain deliberately
outside product-branch retirement; no remote ref was changed in this batch.

Preservation and execution evidence:

- Reverified the three original Git bundle checksums and every inventoried
  ref's exact bundled identity. Standalone restore evidence remains in each
  original inventory. All 77 local-asset archive checksums matched before
  retirement; regular file bytes/hashes and symlink targets were compared with
  the archived inventory again before each checkout's removal.
- Rechecked exact HEAD/branch, clean tracked and untracked status, locks,
  archive pins, current process working directories and retained-checkout
  symlink dependencies. A full open-file snapshot additionally protected live
  use. Removed backend/app checkouts before their containing workspaces.
  No unexpected preservation or identity check failed.
- Used exact `git worktree remove --force` targets only after local evidence
  was preserved. Generated dependencies/caches were excluded from the asset
  archives; they must be recreated if restoring a checkout.
- Created named recovery refs under
  `refs/archive/retired-2026-09-23/codex/<historical-name>`, then deleted only
  the matching branch tip with `git update-ref -d <ref> <expected-sha>`.
  Existing archive refs and bundles remain. These histories were archived,
  **not falsely described as ancestrally merged**. No object pruning ran.
- Exact per-operation paths, SHAs, asset archives, skips and outcomes are in
  `/Users/feihuyan/vesper-repository-archive-2026-09-23.c4wYxq/retirement-zx9gg870/operations.jsonl`.
  The original inventories retain branch-name mappings, and
  `local-assets-dl9syyft/manifest.json` maps ignored files to their archives.
  Recovery is local, not offsite: recreate a branch/worktree from its retained
  SHA/ref or original bundle, restore its specific asset archive if needed,
  and reinstall generated dependencies. Do not extract an archive over a
  current checkout without reviewing the destination.

The one-off retirement guard tests passed eight cases: valid preserved
checkout, changed HEAD, dirty checkout, live owner, new ignored file, locked
checkout, retained dependency, and ownership-tool failure. The independent
post-removal audit passed: all 167 paths are absent, all 83 branch names are
absent, every retired tip still resolves through its recovery ref, all nine
remaining checkouts are clean, canonical main SHAs are unchanged, and all
three Git bundle checksums still match. Exact command:
`python3 /tmp/vesper-verify-retirement-20260923.py`, measured at **3.123 seconds**
with Python 3.14.6 on Darwin arm64. Receipt:
`/tmp/vesper-landing-verification/historical-retirement-audit-20260923T223547Z.log`.
The checked recovery tuple was workspace `75a4398`, backend `0aaa2ccc4`, app
`717355b17`; this documentation receipt follows that check.

**Still incomplete:** land the published recovery candidate through protected-main review, resolve the
remaining acceptance/pin requirements, land useful work, and finally retire
the recovery lane plus the old native-testing lane once no process uses it.
Historical retirement does not prove recovery landing, native visual parity,
or complete-goal acceptance.

### Published candidate and CI repair — September 23 (UTC September 24 logs)

Workspace `a0fab00`, backend `1eb22daf7`, app `7c034796c` passed the clean
coordinated gate in **936.409 seconds** and were published with hooks enabled.
The three open PRs are [workspace #36](https://github.com/fy538/travel-workspace/pull/36),
[backend #233](https://github.com/fy538/travel-agent/pull/233), and
[app #201](https://github.com/fy538/travel-app/pull/201). The app remains draft;
no main has merged. The earlier publication-preparation section below is history.

Remote checks exposed boundaries not certified by that local pass:

- Backend run `35938177449`: standalone offline tests assumed an undeclared
  sibling mobile checkout (six failures); migration drift check reports CHECK
  constraint name differences; the authored Dao returned-trip clock contradicts
  its completed status. DB tests were skipped after migration-check failure.
- Workspace run `35939522206`: private backend checkout fails authentication
  although the secret is present. Credential access/configuration is unresolved;
  no credential has been replaced and no access expansion is authorized.
- App run `35939465963`: frontend size budgets fail; dependency audit reports
  unapproved xmldom/js-yaml advisories; two Life routes lack design ownership;
  calibration is stale, and header inventory/conformance tests fail. These are
  unresolved findings, not permission to refresh baselines or fabricate reviews.
  The Logic QA job also reports two J08 fixture materializations denied as
  `lifecycle_ineligible`: its fixed September 8 scenario does not pass that
  scenario clock to the canonical fixture helper. This is a repair lead, not
  verified resolution; DB reproduction is still required.

The first repair separates standalone backend parser/snapshot tests from actual
cross-repository assertions. `make contract-check` now includes the fail-closed
`cross-repo-fixture-check`, comparing four registered real mobile enum vocabularies
and both generated snapshots against backend owners. Missing children/files,
stale snapshots, enum drift, and failed tooling cannot count as passing. Backend
unit tests use owned parser inputs; no test is quarantined or silently skipped.
Focused standalone tests passed **18/18** with `TRAVEL_APP_ROOT` deliberately
absent. Workspace tooling passed **91/91**, including **11** new positive,
violation, missing-input, and tool-failure checks. Measured log:
`/tmp/vesper-landing-verification/cross-repo-ownership-workspace-suite-20260924T005010Z.log`.
Backend repair commit `1391b1f4d` also passed the complete local `make ci`
with the mobile path absent (**226.691s**): **21,812 passed, 14 skipped,
1,458 deselected, 53 xpassed**, mypy 1,888 files, a further 1,004 checker tests,
and 422 deterministic replay checks (14 LLM-backed checks remain skipped).
Log: `/tmp/vesper-landing-verification/backend-standalone-ownership-ci-20260924T005011Z.log`.
The initial commit hook selected a Python without SQLAlchemy; rerunning with
the lane's existing virtualenv on PATH passed the hook without disabling it.
These repairs require a new pinned candidate and full gate before publication;
they do not inherit the previous tuple's complete verification.

### Fixture-clock repair and CHECK-constraint diagnosis — September 23

The subsequent fixture-clock repair reproduced both J08 failures on a fresh
disposable PostGIS 15/3.3 database at lane port 53932. Fixture birth now passes
its represented `occurred_at`; the scenario injects the same instant into Map's
real canonical time evaluator. Display pins do not grant operational authority,
and no production lifecycle policy changed. Both historical midnight-boundary
cases pass with `--run-quarantined` (**2 passed**, 9.118s), after first reproducing
`lifecycle_ineligible` and then the previously masked completed-Map mismatch.
Log: `/tmp/vesper-landing-verification/recovery-j08-authority-clock-fixed-20260924T010032Z.log`.

Dao's authored completed-trip pin now represents August 10, two days after the
inclusive August 8 end date. All manifests validate; the separate live-calendar
freshness command still correctly fails both stale August windows. Backend/mobile
persona snapshots were regenerated, changing their source hash only. Clock and
cross-repo tests passed **23/23**, mobile persona tests **33/33**. Logs use labels
`recovery-fixture-clock-contracts` and `recovery-persona-mobile-projection` in the
same directory. These are fixture repairs, not refreshed native or live-dogfood
certificates.

Migration diagnosis remains **unresolved, not a blanket false positive**.
Alembic 1.19.1's check reproduces the remote failure on a fresh migration.
A disposable-only probe compares `pg_get_constraintdef` against each metadata
CHECK parsed by PostgreSQL on temporary LIKE tables, rolling back all probe DDL.
The original probe reported 174 tables with identical definition multisets
(84 with differing name sets) and 27 tables needing reconciliation. **That
probe omitted column-level CHECKs.** A corrected rerun includes both table and
column constraints and reports 175 matching tables and 26 mismatches before
repair, with no probe errors. The far-out generation-status CHECK already
exists as a column constraint; its discrepancy is naming, not missing metadata.
Many differences are enum ordering, truncation, duplicate naming prefixes or
cast representation, but the evidence also identifies:

- Four migrated `trips` checks absent from metadata (source, plan editing,
  booking initiation and expense entry policies).
- The migrated notification action-depth check absent from metadata.
- `entity_takes` metadata allowing `trip_story` while the migrated constraint
  excludes it; trace the baseline/migration history and Take owner before
  choosing which side to repair. A completed narrowing migration has not been
  established; the earlier wording overstated that evidence.
- Delegation metadata allowing `restore` and `dissolve_parallel_plan` while its
  migrated operation vocabulary excludes them; inspect the delegation contract
  before expanding accepted authority.

Evidence: `/tmp/vesper-landing-verification/recovery-check-constraint-semantics-20260924T010202Z.log`;
reproduction: `/tmp/vesper-audit-check-constraints-20260923.py` (hard-guarded to the
disposable local database). First reconcile semantic discrepancies with owners,
then solve CHECK naming/truncation without suppressing real drift. No dependency
upgrade, constraint exclusion, migration change or production DB write is claimed.

### Migrated CHECK metadata repair — September 23 (UTC September 24)

Backend commit `8e5187e51` restored the four Trip checks and notification action-depth check in SQLAlchemy
metadata, with the names and expressions already enforced by migrations
`a7b4c1d8e5f2`, `tripagency01`, `costbookauth01`, and `a9f3e2b8c7d1`.
This repairs declarations; it does not change the migrated schema, public API,
accepted permissions, or historical migration files. No new migration is needed
to install checks that are already present. Also corrected the Trip source
comment's migration ID.

Five offline regressions first failed on the missing checks. After repair,
**71 tests passed, zero skips**, including five PostgreSQL cases comparing the
live migrated catalog against metadata parsed by PostgreSQL. Accepted values,
invalid values, and nullable/non-nullable boundaries were exercised on isolated
probe tables. All probe DDL/rows were rolled back. The fresh disposable PostGIS
15/3.3 migration passed in **4.908s**; the final schema suite took **2.318s**.
Ruff, formatting, and diff checks passed. Commands and measured revision tuples:

- `/tmp/vesper-landing-verification/recovery-metadata-fresh-migration-20260924T011131Z.log`
- `/tmp/vesper-landing-verification/recovery-metadata-regression-before-20260924T011235Z.log`
- `/tmp/vesper-landing-verification/recovery-metadata-schema-suite-20260924T011357Z.log`

The corrected column-aware diagnostic before/after logs are
`recovery-check-column-aware-before-20260924T011245Z.log` and
`recovery-check-column-aware-after-20260924T011359Z.log` in that directory.
After repair: **177 matching definition multisets, 24 tables with differences,
86 matching-definition tables with name differences, no probe errors**.
Definition-string differences are not all behavioral differences; enum order,
casts, naming and the Take/delegation vocabulary discrepancies still require
resolution. This remains a diagnostic, not a passing migration gate or evidence
that all schema drift is fixed. Full coordinated verification and publication
remain outstanding for these local repairs.

The post-repair Alembic run emitted remaining differences to
`recovery-metadata-alembic-check-20260924T011500Z.log`. Its command had exited
and no DB connections remained, but the measurement process consumed a full
CPU in `parse_test_counts`; interrupting that owned wrapper confirmed its
unanchored regex in the traceback. This run has no completed measurement
record and must not be cited as a timed pass/fail certificate. The parser now
matches summary lines from their start, preserving pytest banners while
avoiding repeated scans over long non-test diagnostics. A bounded subprocess
regression exercises a 380 KB diagnostic, prior valid summary, and preserved
nonzero exit status; the parser suite passed **27 tests**, and the complete
workspace script suite passed **93 tests** in **11.322s**
(`recovery-workspace-parser-suite-20260924T011730Z.log`). The first saved-log
replay used a nonexistent filename and proves nothing about Alembic output;
the corrected replay uses the exact saved log and is tooling evidence only,
not another database run. No check result was suppressed or converted to pass.

The disposable database was stopped and removed after verifying ownership
and zero client connections. Only generated test data was discarded.

### Take/delegation vocabulary reconciliation — September 23 (UTC September 24)

Two real discrepancies now have different, owner-grounded repairs:

- **Take metadata:** `c58cab3db` makes `TAKE_CACHE_ENTITY_TYPES` equal the
  public Take subject vocabulary. The original `ta7b8c9d0e1f` creation migration
  and `73a1ca90a2ef` baseline both exclude `trip_story`; no narrowing migration,
  production-row deletion, or production-data assertion is needed for this
  declaration repair. Two regressions first failed; **27 Take/schema tests
  passed** after repair, including the migrated PostgreSQL catalog.
- **Delegation migration:** `9b2c8fec7` adds `irdelegationtypes01` after
  `pmevidence02`. The API, metadata, access-state enumeration, and Vesper-attributed
  recovery builders already support `restore` and `dissolve_parallel_plan`;
  their original migrations expanded only `itinerary_operations`, omitting
  delegation storage. Both explicit settings reproduced DB constraint failures.
  The new migration permits persistence of the existing contract, not new
  grants: levels remain none/suggest/prepare-preview/request-confirmation,
  default off, private, explicit and revocable. Execution policy is unchanged.
  The broader schema/access suite passed **87 tests**; the subsequent recovery,
  branch, compound-operation and migration suite passed **35 tests**, including
  transactional downgrade refusal when a recovery setting exists. No setting
  is silently deleted or converted during rollback. Upgrade and single-head
  checks passed on the disposable database.

The entity parity checker also had two hidden defects: `:t::regclass` was not
bound by SQLAlchemy, and a column-substring query assumed only one constraint
could mention that column. A syntax error had been mislabeled as database
unavailability; the first query repair exposed a separate paired-column CHECK.
The corrected query binds `CAST(:t AS regclass)`, selects the actual enum
expression, and propagates programming/ambiguous-result failures rather than
skipping them. Connection unavailability remains the existing explicit skip.
**Seven checker tests passed** (valid input, drift, absent/ambiguous checks,
unavailable connection, SQL failure). The final real-database run checked
**11 Literal mirrors, 14 metadata checks and all 14 live constraints**, passing
with no live-DB skip. Earlier checker runs that printed “Leg C skipped” are
not live-schema evidence.

Measured logs, all under `/tmp/vesper-landing-verification/`:

- `recovery-take-schema-before-20260924T012109Z.log` and
  `recovery-take-schema-after-20260924T012304Z.log`
- `recovery-delegation-before-20260924T012303Z.log` and
  `recovery-delegation-upgrade-20260924T012400Z.log`
- `recovery-domain-schema-suite-20260924T012430Z.log` and
  `recovery-delegation-rollback-20260924T012524Z.log`
- `recovery-live-checker-complete-20260924T013018Z.log` and
  `recovery-live-entity-parity-complete-20260924T013017Z.log`

**Still not ready to land:** the full Alembic drift check exits 255 in **1.679s**
(`recovery-domain-alembic-check-20260924T012559Z.log`). The column-aware
diagnostic reports 177 matching definition multisets and 24 differing tables;
the repaired vocabularies still differ in harmless list order, alongside
remaining naming/truncation and historical cast expressions. Do not use this
bounded repair to waive the whole drift gate. No remote publication, main merge,
new full coordinated gate, native acceptance, or production migration occurred.

### CHECK enforcement gate replaces name noise — September 23 (UTC September 24)

The upstream [Alembic 1.19.2 release notes](https://alembic.sqlalchemy.org/en/latest/changelog.html#change-1.19.2)
confirm that name-only CHECK detection is disabled by default because naming
conventions can produce persistent false positives. That detector also never
compared expressions when names matched. Runtime and development locks were
regenerated with Python 3.13/pip-tools; their only package change is Alembic
1.19.1 → **1.19.2**. The recovery virtualenv uses that exact patch release.

This is paired with a replacement enforcement check, not a blanket exemption.
`scripts/check_check_constraints.py` is wired into backend `test-db-migrate`
before and after the round-trip. It compares table/column CHECK-expression
multisets by parsing metadata on empty PostgreSQL temporary tables and reading
`pg_get_constraintdef`. The existing migration-managed-index filter was not
expanded. Only closed-form enum-order, literal-cast and range-proven numeric
sign equivalences are normalized; other differences and errors fail.
See the [CI owner boundary](../reliability/CI%20Plan.md#backend-schema-drift-boundary).

Local disposable PostGIS evidence:

- Fresh `upgrade head` passed on 1.19.2 in **3.382s**:
  `recovery-alembic192-upgrade-20260924T013712Z.log`.
- New checker regressions: **14 offline cases**, then **23 total cases with
  PostgreSQL**, zero skips. Cases include changed expressions under the same
  logical subject, different names with identical behavior, column-level checks,
  missing/extra/duplicate constraints, malformed SQL, refused non-PostgreSQL
  targets, and bounded numeric zero/NULL/NaN/sign boundaries. Logs:
  `recovery-check-parity-offline-20260924T013713Z.log` and
  `recovery-check-parity-postgres-20260924T013736Z.log`.
- Standalone CHECK gate passed **201 tables, zero differences, zero errors** in
  **1.559s**: `recovery-check-expression-gate-20260924T013806Z.log`.
- `alembic check` remains **failed**, now with a bounded non-CHECK diff:
  `recovery-alembic192-check-20260924T013737Z.log`. It identifies chat image /
  group outbox message nullability, missing occurrence-evidence metadata
  columns/FKs, missing index declarations, and three index-order discrepancies.
  These need owner-grounded reconciliation; no exemption was added for them.
- The previously masked full downgrade test also **failed**:
  `recovery-alembic192-roundtrip-down-20260924T013831Z.log`.
  Dropping `commitments` is blocked by
  `fk_graph_occurrence_evidence_subject_id_commitments`; no CASCADE workaround
  or destructive change was applied. The transaction rolled back to
  `irdelegationtypes01`, verified in `alembic_version` afterward.

The enforcement-gate repair is committed as backend `f2f1cab2b`, with commit
hooks enabled. Complete standalone backend `make ci` passed in **180.084s**
with `TRAVEL_APP_ROOT=/nonexistent/standalone-mobile`: **21,843 passed,
14 skipped, 1,476 deselected, 53 xpassed**, followed by **1,004 checker tests**
and **422 deterministic replay checks**. The 14 LLM-backed replay checks remain
skipped. Log: `recovery-alembic192-backend-ci-20260924T013934Z.log`.
This is offline evidence; it does not override the two migration failures above.

The rollback failure is now traced to `xgraph16_identity_binding_ledger.py`:
its upgrade either renames graph-shaped `occurrence_evidence` or creates
`graph_occurrence_evidence` beside the existing Trip-owned table. Its downgrade
only reverses the rename when the Trip-owned name is absent; when both tables
exist it leaves the graph table behind. Later `xgraph01` cannot drop its
referenced `commitments` table. The correction must distinguish those two
upgrade paths and preserve the Trip-owned table; no fix or successful complete
round-trip is claimed yet.

### Graph rollback repair — September 23 (UTC September 24)

Backend `0b2b9bad9` handles both `xgraph16` upgrade paths: rename graph-only
evidence back, or remove the newly created graph table when Trip evidence
already exists. `xgraph01` now preserves the Trip-shaped table it skipped during
upgrade. No production upgrade, schema shape, or action authority changed.

Four new PostgreSQL cases exercise both paths with and without the identity
ledger; retained evidence rows and the shared users table survive as intended.
The containing migration regression suite passed **8/8**, zero skips, and the
offline graph/chain suite passed **22/22**, five DB cases deselected. The first
test attempt incorrectly included public tables in the fixture search path;
it failed before migration teardown and rolled back. Removing public from the
transaction-local fixture search path produced the isolated passing run.
Logs: `recovery-graph-rollback-tests-isolated-20260924T014734Z.log` and
`recovery-graph-rollback-offline-20260924T014810Z.log`.

The actual database downgrade now passes the graph boundary. Full `downgrade
base` still fails later at `depthencounter01`: its downgrade targets a CHECK
name absent from the migrated schema (`ck_experience_outcome_next_thread_length`).
Log: `recovery-graph-rollback-full-down-20260924T014748Z.log`.
The explicit downgrade to `intakeretention01` succeeds, but re-upgrade fails at
`rootdelivery01` with an existing doubly-prefixed `user_events` CHECK name.
That upgrade transaction rolled back; `alembic_version` is
`intakeretention01`, not head. Log:
`recovery-graph-boundary-roundtrip-20260924T014828Z.log`.
These are the next concrete migration repairs, not permission to bypass the
round-trip or add CASCADE. The full offline pass recorded above predates this
bounded rollback repair; focused results do not replace the next complete gate.

### Historical naming and reconciliation repairs — September 23 (UTC September 24)

Four migration repairs are now exercised against disposable PostgreSQL:

- `depthencounter01`: CHECK drops use the same naming convention and identifier
  truncation as their creation, rather than an untyped physical-name guess.
- `rootdelivery01`: retires all three historical event-CHECK spellings and uses
  `op.f` for its already-canonical name. Downgrade still retains the broader
  event vocabulary; re-upgrade succeeds without duplicate constraints or
  deleting exposure rows.
- `multiplayer08`: dropping `invited_by` removes its own FK, without guessing
  a PostgreSQL-generated name different from the metadata convention.
- `schemaalign01`: preserves the Trip-reading table and canonical share index
  belonging to earlier migrations. It no longer destroys the table or
  resurrects a drift-only index spelling during rollback. Trip-kind index
  restoration remains owned by its original chain.

Fresh head upgrade passed in **3.669s** on `vesper_cleanup_validation`:
`recovery-naming-validation-upgrade-20260924T015616Z.log`. The combined
migration/CHECK regression suites passed **38/38**, zero skips, including
schema-isolated upgrade/downgrade/re-upgrade cases, retained rows, actual FK
reflection, forbidden event rejection, and both previously present/missing
Trip-reading repair paths:
`recovery-migration-repairs-final-tests-20260924T015652Z.log`.

Full historical rollback remains **failed**, but now reaches an intentional
boundary, not those defects. On a new empty database, upgrade passed and
downgrade stopped at `notifenv04`'s explicit refusal:
`recovery-alignment-v2-fresh-roundtrip-20260924T015551Z.log` (**5.593s**).
`notifenv02`, `notifrecord01`, and `notifcorr01` also deliberately reject
downgrade. No guard or CI requirement was removed. The
[CI owner document](../reliability/CI%20Plan.md#backend-schema-drift-boundary)
records this unresolved policy mismatch.

Earlier attempts in this batch exposed and retained evidence for the circle FK,
Trip-reading removal and share-index rename failures. A failed full downgrade
committed intermediate revisions at concurrent-index/autocommit boundaries;
the first target was verified at `geoggist02`, not head. A subsequent regression
attempt against that target failed its head-only delegation case (14 passed,
one failed); this was invalid environment evidence, not an application
regression or a passing run. Subsequent full-chain attempts used fresh databases
and final regressions used a separately verified fresh-head database. Never
infer all-chain rollback from the transactional behavior of an earlier segment.

A separate bounded real-database round-trip **passed**: head → `notifenv04`
(without invoking its forbidden downgrade) → head, followed by the CHECK gate
over **201 tables**, zero differences/errors, in **5.092s**.
Log: `recovery-supported-boundary-roundtrip-20260924T015817Z.log`.
This certifies the tested reversible segment, not `downgrade base`, production
data preservation across every migration, or a change to required CI policy.

The repair batch is committed as backend `9729e3fcf`, hooks enabled. Full
standalone backend `make ci` passed in **177.224s**, with the mobile sibling
deliberately unavailable, including 1,004 checker tests and 422 deterministic
replay checks; 14 LLM-backed replay checks remain skipped. Log:
`recovery-migration-repairs-backend-ci-20260924T015653Z.log`.
The subsequent `alembic check` still fails with the previously identified
non-CHECK metadata drift:
`recovery-post-roundtrip-schema-drift-20260924T015844Z.log`.

The labelled, tmpfs-backed disposable container `6095c0ab88bf` and its four
synthetic databases were removed after verifying zero other clients. No user
database or unrelated Docker service was modified. The recovery app remains
unchanged; no pin update, remote publication or protected-main merge occurred.

### Core metadata drift reconciled — September 23 (UTC September 24)

The remaining core-metadata differences were traced to their original
migrations and runtime owners, rather than exempted from drift detection:

- Chat images require `message_id`; group outbox authority/lifecycle events
  permit no message. The outbox's comment/nullability had been placed on the
  image table. Metadata now matches `roomrt02`, the baseline image schema,
  and the existing writers; no database nullability or API changed.
- Distance cache pruning, Intake dead-letter, Life resolution supersession,
  and pipeline scoped-checkpoint indexes are represented in metadata.
- The entity-resolution and two place-handoff indexes match their migrated
  ascending key definitions. Runtime `ORDER BY` behavior is unchanged.
- Four nullable Trip-evidence columns already persisted by `xgraph12` are
  represented without conflating Trip evidence with `graph_occurrence_evidence`.
  The Occasion FK uses an isolated external-key reference, not an import or
  partial adoption of the separate domain's metadata. Readers still project
  their explicit existing fields; this enables no new evidence writes.

The initial string FK could not resolve Occasion in core metadata and correctly
failed autogenerate. The isolated key reference fixes that ownership seam;
regressions assert the real domain key's name/type, core schema isolation,
sorting, and on-delete behavior. No autogenerate filter was expanded and no
new migration is needed to reflect schema already installed by existing ones.

Verification under `/tmp/vesper-landing-verification/`:

- `recovery-owner-metadata-drift-fixed-20260924T020456Z.log`: **passed** in
  **2.999s**; Alembic reports no new operations and the CHECK gate reports
  **201 tables, zero differences/errors**.
- `recovery-owner-metadata-db-20260924T020513Z.log`: **41/41 passed**, zero
  skips, including reflected columns/keys/indexes for all nine affected tables.
- `recovery-owner-runtime-postgres-20260924T020539Z.log`: **17/17 passed**,
  zero skips, for occurrence, membership outbox and Life resolution DB paths.
- `recovery-owner-metadata-offline-20260924T020247Z.log`: **41/41 passed**
  in the selected offline image, outbox, handoff and Intake suites.
- `recovery-owner-metadata-roundtrip-20260924T020606Z.log`: **passed** in
  **5.760s**; head → `notifenv04` → head, then both Alembic and CHECK gates.

This resolves the previously reported **core metadata drift**. It does not
certify the separate graph schema or waive the forward-only/full-base CI
mismatch. Fresh GitHub readback still shows all three recovery PRs open,
blocked and requiring review, with the app PR draft.

Backend commit `5b19ba11e` passed hooks and full standalone `make ci` in
**182.315s**: **21,845 passed, 14 skipped, 1,488 deselected, 53 xpassed**,
mypy 1,888 files, 1,004 checker cases, and 422 deterministic replay checks.
The 14 LLM-backed replay checks remain skipped. Log:
`recovery-owner-metadata-backend-ci-20260924T020514Z.log`.
Docs checks passed in **6.430s** (`recovery-owner-metadata-docs-20260924T020737Z.log`).
The labelled disposable container `f69c64f681bb` was removed after confirming
head revision and zero other clients; its synthetic database is discarded.
The old native worktree remains protected: live Xcode `DTServiceHub` PID 25951
still holds its screenshot directory. All three old-native checkouts remain
tracked/untracked clean. No unrelated process was stopped, and no main or
remote branch was changed in this batch.

All logs above are under `/tmp/vesper-landing-verification/`. This is a narrower,
more trustworthy diagnosis, **not a passing migration job**. Full coordinated
verification, publication, required CI, review and native acceptance remain open.

### Clean verification and publication preparation — September 23

The clean coordinated gate passed at workspace `ff08cc1`, backend
`1eb22daf7`, app `f77f4f310` in **938.773 seconds**. It ran through
`land-worktree.sh` (without publishing), which fetched each remote main and
checked clean revisions before and after `make verify`. The log is
`/tmp/vesper-landing-verification/recovery-clean-coordinated-gate-20260923T235946Z.log`.
Backend offline evidence: **21,811 passed, 14 skipped, 1,458 deselected,
53 xpassed**; mypy: zero errors in 1,888 files. Full contract generation, API
coverage, mobile journeys/seams/offline tests, 384 Maestro syntax validations
and workspace governance passed. Syntax validation is not device execution.
The separate mobile `verify:pr`, `make docs-check`, backend documentation
push packet and preservation audit also passed at this clean tuple. Logs use
the labels `recovery-app-final-pr-gate`, `recovery-documentation-final`,
`recovery-backend-documentation-push-packet` and
`recovery-preservation-recheck` in the same directory.

The initial publication pushed backend `1eb22daf7` and app `f77f4f310`
to the recovery branch. Workspace publication failed, not the prior shell
gate: the pre-push environment selected the parent's Git index/HEAD during
child evidence reads. `6cba254` fixes the release/journey-evidence ownership
boundary without bypassing the hook or changing release intent. Regression
tests first reproduced the fault; **113 tests** then passed, including real
temporary repositories, wrong-parent index rejection, dirty/clean identity and
Git tool-failure cases. The current-state checker also passed under explicit
hook-style repository variables. Log:
`/tmp/vesper-landing-verification/recovery-workspace-hook-regressions-20260924T002001Z.log`.

CI pin preparation now selects backend `1eb22daf7`, app `7c034796c`
and workspace tooling bridge `6cba254` (the app's dependency). Publish the
workspace bridge first, then the pinned app, then the final workspace tip;
all remote dependency SHAs must resolve before opening the coordinated PRs.
The bridge and final workspace differ only in dependency pins and this dated
receipt/roadmap, not evidence tooling or product contracts. The updated tuple
requires its own clean gate; use the PR's exact-revision results for subsequent
publication/merge status rather than carrying the earlier tuple's pass.

Places' external canonical bundle was hash-verified from the local Downloads
export (one manifest, six pairs, one verified external authority), but no new
native capture was made. Its reserved simulator was shut down and its Metro
port had no listener. Mixed-Places appearance, Home value/design acceptance,
independent protected-main review, and final lane retirement remain separate.
All three remote mains still require one independent review with administrator
enforcement; the authenticated author cannot supply that approval. The old
native lane still has a live Xcode directory owner. No main merge, review
bypass, process termination or final lane removal is claimed.

### Spatial/demo lifecycle closure — September 23

Backend `1eb22daf7` archives nine dated documents: Place-entity and routing
research, the spatial execution plan, and six demo receipts/plans. Their bodies
are preserved with archive metadata, dated authority notices and repaired links.
The beat contract and program remain live references for executable YAML;
the older integration-engine plan remains a requirement reference for pending
`readiness.py` entries. Maintenance does not release families, certify cloud
state, clear the demo registry's recorded lock or restore an August backlog.
The recorded lock is not evidence of a live process.

App `f77f4f310` repairs two historical source paths. Current indexes and this
program's scheduling boundary distinguish history from active authority.
Place Relationship Surface's maintenance date covers ownership/provenance
review, not implementation or visual certification.

Focused offline validation passed **46 tests**, both demo validators, backend
and app links, backend product governance and workspace child-governance,
links and canon budgets. Log:
`/tmp/vesper-landing-verification/spatial-demo-lifecycle-20260923T235326Z.log`.
After the child commits, the exact command
`travel-agent/.venv/bin/python travel-agent/scripts/check_docs_status.py --ci`
passed in **4.797 seconds**, with zero expired-active or stale-header findings:
`/tmp/vesper-landing-verification/spatial-demo-committed-freshness-20260923T235819Z.log`.
The checker scans bounded headers, not every historical statement; the focused
pass preceded final index-label/provenance edits. A clean coordinated gate
remains the next step. No remote, production or canonical main change occurred.

### Research and prototype portfolio disposition — September 23

Backend `2475e6161` preserves fifteen August documents under the existing pivot
and social research archives. Ten are from the expired queue: philosophical
foundations, the dated product-shape audit, artifact grammar, longitudinal and
situated simulations, differentiated social strategy, gathering synthesis,
prototype matrix, study plan and blank study worksheet. Five adjacent attention,
agency/reciprocity, grammar, anchor and Place-capability derivations also carry
expired working dates, but beyond the freshness checker's scanned header lines;
they are classified by their actual lifecycle rather than left active because
the check misses them. The checker itself is unchanged.

This was an authority/lifecycle review of document purpose, scope, proposed
sequences, gates and open-decision sections against current canon—not a new
cover-to-cover empirical research validation or implementation audit. The full
bodies, founder stories, studies, counterexamples and unresolved questions stay
available. Current Product Model, four-root contract and Multiplayer Product
Strategy supersede old three-root, universal-Opening, one-card, exclusive
travel-launch and identity-facet proposals. The program roadmap carries the
remaining research areas without declaring studies complete or scheduling old
experiments as cleanup work. No runtime code, fixture, consent or release gate
changed; source/test/tool searches found no executable old-path consumer.

Thirty-nine unique relocation/backlink transformations were checked before
manual index/owner notices: 36 matched expected hashes exactly; two digest
files gained a final newline and the blank worksheet lost one redundant final
newline. Reversing only those newline differences reproduced all three expected
hashes. Original source-at-relocation hashes remain in the archive headers.
Live index labels now say historical, and canonical backlinks no longer call
the archived Place-capability proposal a current contract. Mobile is unchanged.

Workspace child governance, living links and canon budgets; backend links and
product governance; and 36 focused artifact/Occasion/Intake fixture tests pass:
`/tmp/vesper-landing-verification/research-portfolio-lifecycle-20260923T234514Z.log`
(7.647s, staged tuple). After the backend commit, freshness reports **11 expired
documents and no stale headers** (exit 1):
`/tmp/vesper-landing-verification/research-portfolio-committed-freshness-20260923T234546Z.log`
(4.808s). Remaining items are eight demo/Riviera documents and three
Place/routing/spatial documents. These need individual ownership review, not a
blanket archive: the demo program still has executable owner-lock consumers.
Final delivery verification, protected-main landing and retained-lane retirement
remain incomplete.

### Dated execution-plan handoff — September 23

Backend `6f0a4c164` archives the August Content activation roadmap, Intake V2
completion roadmap and Occasion grammar execution receipt under
`docs/archive/2026-08/implementation-slices/`. All three were read in full;
their bodies are preserved with only relocation-aware links and archive/owner
notices. All three expected transformation hashes matched. Original hashes
remain in their headers. No source/test/tool consumer of the old paths was
found, and no mobile files changed.

The [program handoff](vesper-program-roadmap.md#august-execution-plan-handoff--september-23)
carries unfinished work to current owners rather than deleting it: exact-input
content review and serving/rollback evidence, deployed Intake custody and
provider/deletion proof before legacy cutover, and current-owner reconciliation
of Occasion authority questions. It explicitly avoids treating August local
test counts or old unknown fields as today's implementation inventory. The
Content roadmap's 13-binding completion wording must not override its two
held stale-evidence rows. The source-reviewed Intake audit reports only static
review readiness and always retains production blockers. No gate, model,
schema, flag, service, source data or immutable review was changed.

Measured checks pass: workspace child governance, living links and canon
budgets; backend links/product governance; and 29 focused offline tests for
Intake cutover reporting, Occasion grammar/projections and runtime acceptance.
Exact command and dirty staged revisions are in
`/tmp/vesper-landing-verification/execution-plan-lifecycle-20260923T233729Z.log`
(6.763s). These are local contract checks, not production or device evidence.
The committed backend freshness check still exits 1 with **21 expired documents
and one stale header**:
`/tmp/vesper-landing-verification/execution-plan-committed-freshness-20260923T233751Z.log`
(4.667s). Full final-tuple verification and protected-main landing remain unrun.
PID 25951 was again confirmed live with its cwd in the retained native lane's
screenshots directory; no native worktree or process was removed.

### Content, memory and profile research disposition — September 23

Backend `21de41d49` preserves three full August investigations under
`docs/archive/2026-08/pivot-research/`: differentiated Place-content strategy,
platform memory versus human remembering, and profile/relationship views.
All three were read in full, including founder stories, proposed schemas and
workflows, implementation observations, studies, falsifiers and open questions.
They remain available as research provenance, not erased or declared resolved.

Current ownership is explicit in each archive and its live backlinks:

| Archived investigation | Current rules retained | Still not proved/adopted by this pass |
|---|---|---|
| Place-content strategy | Accepted content runtime decision, Place Interpretation, World Foundry | New source collection, contribution economics, review automation, public promotion and field outcomes |
| Human remembering | Product Model's five memory services, private-memory behavioral covenant, Contribution and Consequence | Six proposed human studies, memory/retention benefit, additional capture or inference authority |
| Profile/relationship views | Product Model, Multiplayer Product Strategy, narrower Together PF1.0 projection contract | Broad private/public profile compositions, public-lens product, prototype sequence and old root layouts |

The old content architecture now points to the existing accepted runtime owner;
archival does not adopt the research wholesale or revive automatic dossier
promotion. Memory Architecture labels its August 21 implementation inventory
as dated rather than implying the link-maintenance date reverified all stores.
Together PF1.0's reference-maintenance date likewise certifies no dogfood,
implementation or activation. Its Decision/§13 implementation-versus-exposure
wording conflict is explicitly unresolved; owner reconciliation is required
before relying on broader authority. No gate or runtime code was changed.

The initial 20-file relocation/backlink transformation was verified: 19 hashes
matched exactly; one historical digest lacked a trailing newline, which
`apply_patch` added. Removing only that final newline reproduces the expected
hash. Subsequent owner notices were reviewed separately. Original hashes remain
in the three archive headers; the original bodies change only for relocated
links and an explicit archive/owner banner. App `372631d04` repairs two profile
design references; no app implementation changes.

Measured documentation checks pass: workspace child governance, living links,
canon budgets; backend links and product governance; mobile links. Receipt:
`/tmp/vesper-landing-verification/pivot-research-lifecycle-checks-20260923T232843Z.log`
(3.647s). Committed child freshness remains exit 1 with **24 expired working
documents and one stale header** in the August philosophical-foundations note:
`pivot-research-committed-freshness-20260923T232910Z.log` in the same directory
(4.622s). That remaining note's newly committed backlink makes its old review
date observable; the research itself was not silently reverified. Full delivery
verification, protected-main landing and the two retained lane retirements are
still incomplete.

### Social-history follow-up — September 23

Backend `8103a9aa8` archives three further historical documents under
`docs/archive/2026-08/social-research/`: the explicitly superseded August 7
multiplayer strategy and the August 23 adjacent-product and Occasion/identity
psychology research snapshots. These were read in full. Their original market
claims, open questions, studies and falsifiers remain historical research, not
revalidated claims or completed experiments. The older strategy's mandatory
group-travel sequence, ambient-centric position and blanket scroll/feed ban
must not override today's broader social-benefit portfolio. Current Multiplayer
Product Strategy already owns that distinction; no new product ruling was made.

The existing `docs/product/MVP Social Loop.md` is retained in place as a maintained
circulation-boundary contract, rather than archived or given another arbitrary
working expiry. Its portfolio, non-reciprocal effort, source/audience boundaries
and still-gated distribution mechanisms were compared with Product Model,
Multiplayer Product Strategy, Growth Strategy and the contribution contract.
An explicit authority/verification section limits this lifecycle promotion to
those existing rules. It does not claim implemented guest entry, native delivery,
consumer validation or permission to ship a new social mechanism.

Fourteen archival/backlink transformations match their expected SHA-256 values.
Original file hashes remain in archive metadata. Eleven incoming references
(including a YAML supersession entry) are repaired across the three repositories;
app `4d1f9140d` only changes the design brief's historical reference. Source/test
search found no executable consumer of the three moved documents.
The measured documentation packet passes backend links/product governance,
workspace links/child governance, and mobile links:
`/tmp/vesper-landing-verification/social-portfolio-lifecycle-checks-20260923T232244Z.log`
(3.384s). This is documentation evidence, not a new runtime test result.

After both child commits, freshness exits 1 with **27 expired active documents,
all in `docs/working/`, and three stale headers** (Place-content strategy,
human remembering, and profile/relationship views). Receipt:
`/tmp/vesper-landing-verification/social-portfolio-committed-freshness-20260923T232306Z.log`
(4.483s). The prior pass's 30/five count below is historical. The remaining
working proposals and execution programs require individual owner/lifecycle
reconciliation; this pass does not complete them or waive the publication gate.

### Place calibration and social-research lifecycle pass — September 23

Backend `61574d8b3` archives the three August 16 Place interpretation notes under
`docs/archive/2026-08/place-calibration/` and promotes the August 22 runtime
acceptance procedure to `docs/operations/content-runtime-acceptance.md`.
Original archive bodies and the relocated backlink match their expected hashes;
only metadata, historical notices and link relocation change the snapshots.
The maintained procedure now separates artifact shape, independent review,
runtime receipt authority and actual release evidence.

The offline calibration replay at `2ae8682fe` passed 19 focused tests, but this
does **not** establish current runtime acceptance. The expansion report remains
ineligible, and the vertical-slice validator explicitly requires the historical
blocked state. It is not a live implementation-progress check. The separate
runtime-acceptance report exits **1**: zero accepted canonical lanes, zero bound
cases, two candidates and 21 blocked cases (23 unresolved total). The old
independent review's `place_content.py` input hash is stale. Preserve that review;
do not regenerate hashes to manufacture acceptance. Current program ownership
must reconcile this bounded historical campaign before using it for expansion;
it does not become a new prerequisite for all product engineering.

The superseded August 9 multiplayer activation companion and its evidence memo
now live under backend `docs/archive/2026-08/social-research/`. The current
Multiplayer Product Strategy already explicitly superseded the companion.
Sources, transfer limits, proposed studies and falsifiers remain preserved;
no study completion, external-source revalidation or new social policy is
claimed. Eleven backlink edits across the three repos preserve discoverability,
including the canonical strategy's YAML supersession reference. All 13 moved
or backlink-edited files match the generated transformation hashes.

Verification on the staged edits: backend/workspace documentation links,
product governance and child governance pass; mobile `npm run docs:links` passes.
The Place focused packet passes 19 tests. Measured receipts are
`/tmp/vesper-landing-verification/place-calibration-doc-cleanup-recheck-20260923T231527Z.log`
(6.646s), `social-research-archive-checks-20260923T231734Z.log` (3.213s), and
`social-research-app-links-20260923T231748Z.log` (0.429s), all in that directory.
An initial command used a nonexistent workspace link-check filename and exited
2; the corrected run used the documented Make targets and passed.

Freshness remains **failed**, not waived: 30 expired active documents plus two
stale headers, down from 36 expired documents before this pass. The headers are
in the August 21 Place-content strategy and human-remembering research; their
claims still need lifecycle review. Receipt:
`/tmp/vesper-landing-verification/social-research-archive-freshness-20260923T231738Z.log`
(4.416s, exit 1). Full committed-tuple `make verify` and protected-main landing
remain pending. Xcode PID 25951 was rechecked and still holds the old native
worktree's screenshot directory; no worktree or process was removed this pass.

Clean committed-tuple follow-up: workspace `3270330`, backend `0f898fd73`, app
`480df92d4` passes the same 19 tests and all four documentation checks in 5.899s
(`calibration-social-clean-committed-20260923T231905Z.log`). The final freshness
run in 4.415s still finds 30 expired documents but **five** stale headers, not
the staged run's two: committing backlinks makes the old verification dates of
three additional documents observable to its Git-date check. This does not
reverify those research/strategy claims. The final receipt is
`calibration-social-committed-freshness-20260923T231920Z.log` in the same log
directory; its exit is 1. Keep these five in the remaining lifecycle review.

### Runtime-evidence lifecycle pass — September 23

Backend `b3ba0e205` archives eight reviewed point-in-time records under
`docs/archive/2026-08/runtime-evidence/`: the August 12 vector-release and runtime
recheck, August 13 production-readonly recheck, the three August 14 runtime
selections, the August 23 Intake baseline, and the completed August 21 Plan
Shape implementation receipt. Their observations, failures, outstanding gates,
test counts and original dates remain historical evidence—not present-day
production assertions or a declaration that unfinished acceptance is complete.
Archive metadata records each original path and full-file SHA-256. All eight
archive transformations and five backlink edits were checked against their
exact expected bytes; original bodies changed only for link relocation and
an explicit historical notice.

The offline eight-beat report directly reads the v206 document. Its input now
points to the archive and its production-foundation summary explicitly names
the historical observation and absence of current health verification. New
regressions check the archive binding/wording and fail-closed missing input;
existing missing-beat and fabricated-runtime-pass checks remain. The demo
program registry points to the relocated evidence without changing task,
acceptance, or lock statuses. Immutable JSON receipts were not rewritten to
manufacture new input hashes.

Checks: 18 focused report/registry tests pass; Ruff and formatting pass;
backend links (6,722 Markdown files), product governance, workspace links
(531 living documents), and child governance (404 post-baseline documents)
pass. The child governance command initially failed before rename staging
because Git still listed the eight removed source paths; it passed after
explicitly staging both sides of the moves. This was not a checker exemption.
Measured focused test receipt:
`/tmp/vesper-landing-verification/runtime-receipt-archive-20260923T224232Z.log`
(6.320 seconds, 18 passed). The freshness gate still fails with **53 expired
active documents**, down from 61; measured receipt:
`/tmp/vesper-landing-verification/runtime-archive-freshness-20260923T224321Z.log`.

The remaining work is not one blanket archive batch. The live environment
audit, production-dogfood/vector-release lane, content inventory/quality/delta
notes, and Intake production canary still describe operating contracts and
must be compared with current implementation and owner runbooks. Research,
social doctrine, prototype portfolios and unresolved execution plans need
separate provenance/authority disposition. Preserve open constraints in current
owners before retiring their old working notes. No expiry extension, deployment,
flag activation, complete-gate pass, or protected-main landing occurred here.

### Operator-note promotion — September 23

Backend `84b69664b` resolves seven more expired working documents by retaining
their useful procedures as Operations runbooks: live environment audit,
production-dogfood release, vector release, content inventory, legacy structural
quality audit, place-content delta review and Intake production canary. These
are promotions after source/test review, not blanket expiry extensions. They
grant no new production authority and do not replace World Foundry policy.

The live audit's original August 12 deployment observations are preserved in
the runtime-evidence archive with original-path/hash metadata; the current
procedure links to them as history, not current service health. The demo task
registry now names the promoted production-dogfood procedure without changing
its task status, lock or acceptance. No immutable execution JSON was rewritten.

Source review corrected concrete drift: content inventory's default contacts
configured stores (`--repo-only` is the offline mode); store-unavailable status
does not necessarily produce a nonzero exit; the quality audit detects headings
and structural signals, not prose quality or complete Git/readability evidence;
Intake semantic confirmation precedes deletion; and delta preview transaction
guarantees differ for adapter-owned versus caller-supplied connections. Existing
consequence-policy binding limits and live-audit Intake schema checks are now
explicit. No runtime behavior, authority gate or product policy changed.

Evidence on the edited candidate: **105 passed, two deselected**, with backend
links (6,723 files), product governance, child governance (405 post-baseline
documents) and workspace links (531 living documents) passing. The two excluded
tests are `test_postgres_adapter_previews_and_applies_one_accepted_create` and
`test_postgres_adapter_persists_reviewed_proactive_expiry`; real DB behavior and
production health remain unverified. Measured receipts retain exact commands,
base tuple and dirty-state boundary:

- `/tmp/vesper-landing-verification/operator-promotion-backend-20260923T225652Z.log`
  — 8.844 seconds, links/governance plus focused operator and registry tests.
- `/tmp/vesper-landing-verification/operator-promotion-docs-20260923T225636Z.log`
  — 1.047 seconds, workspace links and child metadata.

The documented repository-only inventory and quality-audit commands executed
successfully; Intake plan mode returned `planned` with zero API calls. No live
store or production command was run. Freshness still fails with **46 expired
active documents**, down from 53: one product working document, three research
notes and 42 working documents. Full clean-tuple verification and landing remain
outstanding. At the 22:57 UTC ownership recheck, Xcode `DTServiceHub` PID 25951
still held the native-testing screenshot directory; its three worktrees remain.

### Implementation/proposal lifecycle pass — September 23

Backend `2ae8682fe` moves ten August working notes, with original bodies and hashes preserved,
to backend `docs/archive/2026-08/implementation-slices/`. This retires duplicate
as-built narratives, not their useful code or unresolved release obligations.
Relative links are relocated; notices distinguish old observations and proposals
from current authority. Living references that called the prototype an owner
now point to the accepted runtime decision or lifecycle contract instead.

Disposition and preserved requirements:

| Historical note(s) | Current owner / still-required evidence |
|---|---|
| `attention-intake-v2-implementation`, `custody-first-ingestion-slice`, `intake-v2-architecture-execution` | [Contribution and Consequence](../systems/contribution-and-consequence.md), [CC-4–CC-6 completion plan](contribution-contract-and-legacy-memory-migration-plan-2026-08-29.md#11-completion-plan--september-5), and backend Inbound `FEATURE.md` retain useful-first capture, exact custody, retry, correction, retention, raw/derived separation and canonical handoff requirements. Old local migration heads, 59/346-test totals and unsupported-format descriptions are historical observations, not current device/provider acceptance. Deployed storage/worker/provider parity and clean generated-contract evidence remain separately required where applicable. |
| `experience-anchor-and-consequence-bridge` | Contribution and Consequence plus the Lived Experience gateway/readback owners retain explicit canonical bindings, owner confirmation, private derived anchors, correction/retraction, expiry and no inferred recipient. Current `activation_authority.py` and the prepared-command gateway supersede the note's unregistered-adapter/pending-resolver descriptions for their supported paths; that is not proof that every proposed family is released. |
| `addressed-place-handoff` | [Lived Experience release boundary](../../travel-agent/backend/lived_experience/FEATURE.md#addressed-place-handoff-release-boundary) now retains the connected prepare/deliver/recipient-action/revoke/expiry/older-client obligation. The machine-readable `surface_release` evidence points there and remains **pending** with the same work item; flags, rollout and statuses are unchanged. |
| `contextual-engine-slice` | [Content runtime authority decision](../../travel-agent/docs/architecture/content-convergence-runtime-authority-2026-08-22.md) and Lived Experience `FEATURE.md` own one runtime, scoped context, arbitration, hold/silence and owner consequence. The tools-only contextual engine remains a replay oracle, not another production system. |
| `content-convergence-implementation`, `content-authority-clean-break` | The content runtime decision, [World Foundry](../../travel-agent/docs/operations/World%20Foundry.md) and [delta runbook](../../travel-agent/docs/operations/place-content-delta-review.md) retain independent review, exact source/target hashes, policy binding and Postgres authority. Legacy-versus-canonical comparison, freshness/cost/queue measurements, durable release results and surface-specific Home/Push acceptance remain requirements before their respective cutovers. `LEGACY_RESEARCH_WRITEBACK_ENABLED` is still code-default true; archival does not flip it. Historical corpus counts or local DB state are not current measurements. |
| `plan-shape-and-occasion-slice`, `flexible-plans-occasions-and-personal-projections` | [Product Model](../../travel-agent/docs/product/Product%20Model.md), [Plan/Occasion lifecycle](../../travel-agent/docs/architecture/plan-occasion-lifecycle-contract-2026-08-22.md), and [arrangement handoff](lightweight-arrangements-implementation-handoff-2026-09-04.md) retain sparse viewer-relative projections, partial overlap/split/rejoin, private anchors, plural outcomes and typed revision-bound mutations. The existing Trip writer stays authoritative until explicit cutover. Fixtures do not establish live producer/readback, deployed data, final native parity or a new persistence owner. |

These are existing obligations carried into current navigation, not newly
introduced requirements that every dark feature ship before repository cleanup.
The integration roadmap continues to decide delivery scope; archival cannot be
used to mark any acceptance gate passed. A regression asserts that the addressed
handoff release reference names the living owner section and retains its pending
work item. Original test counts and deployment claims were not re-certified.

Verification: all ten archive outputs matched their expected transformed bytes
(original bodies changed only for historical notices and relative links). The
focused readiness, shadow binding, Intake activation, relationship gateway,
content authority, Plan Shape and Occasion capsule suites pass **37 tests**;
Ruff and formatting pass. Backend links (6,723 files), product governance,
workspace links (531 living documents) and child governance (405 post-baseline
documents) pass. The first link check caught one archived Plan receipt still
pointing to the old working path; its link was repaired and the complete batch
rerun. No gate was weakened. Measured recheck:
`/tmp/vesper-landing-verification/implementation-archive-recheck-20260923T230452Z.log`
— 7.323 seconds on the edited candidate. Freshness still fails with **36**
expired active documents; no full verification, live deployment, native journey,
feature activation or protected-main landing is claimed by this pass.

## September 23 consolidation mandate and current execution order

The existing `codex/home-human-opening-recovery-2026-09-23` coordinated lane
is the integration host for all three repositories. Its old name does not
limit the task to Home. The founder's authorization covers necessary recovery,
ordinary integration repairs and the eventual cleanup; do not repeatedly
stop to request the same scope approval. It does not adopt held product
policies, discard ignored files, bypass verification or override protected-main
review requirements.

1. **Preserve — committed-history recovery now verified.** A fresh inventory
   found 58 workspace, 59 backend and 59 app worktrees, all clean in tracked
   and ordinary untracked files. Exact worktree HEADs are pinned under
   `refs/archive/consolidation-2026-09-23/worktrees/<full-sha>`. Three complete
   Git bundles and inventories are at
   `/Users/feihuyan/vesper-repository-archive-2026-09-23.c4wYxq/`.
   Each bundle passed `git bundle verify`; a fresh bare repository fetched
   it without borrowing objects, and all recorded refs and worktree HEADs
   matched (108 workspace, 108 backend, 105 app checks, including repeated
   worktree HEADs). The temporary bare verification copies were then removed
   to avoid retaining another approximately 1.8 GiB of duplicate objects;
   bundles and manifests remain. This is a local committed-history backup,
   not an offsite backup or a copy of ignored/uncommitted files.
2. **Close selective recovery under current owners.** Finish the existing Home
   join's landing work. Resolve mixed Places ordering against current
   contract/producer/consumer evidence. Review the remaining named candidates
   below for a current gap; either adapt and test them, identify their current
   replacement, or explicitly archive them as deferred/rejected. Automatic
   Source activation, custom visit windows and other unaccepted product
   experiments do not become prerequisites to pruning their preserved Git
   branches. They remain decisions/backlog items, not silently shipped features.
3. **Repair the integration baseline.** Own the world-catalog runway,
   API-operation review, schema-bridge, Maestro metadata, compatibility-ledger
   and typecheck failures as explicit integration work. Review actual current
   consumers/owners before retiring a path or renewing an exception. Do not
   convert old expiry dates or test exemptions into apparent completion.
   The first repair aligns Maestro metadata with existing flow tags, gives
   four reusable gallery subflows unique names, and reconciles the Python
   smoke inventory with the app's already-declared 15-flow selection (including
   Home/Places flows 47–51). It changes no flow commands or suite selection.
4. **Land the coordinated result.** Run focused checks as changes accumulate,
   regenerate contracts when necessary, and run the required complete gates
   for the final revision tuple. Publish/land through the repository's current
   protected-main process. Local candidate commits are not remote-main delivery.
5. **Retire exact historical refs and worktrees independently of publication.**
   The accepted recoveries are preserved in the active integration lane and
   historical Git/local-asset archives are verified. Adjudicated obsolete or
   deferred branches can therefore be retired before step 4 completes; keeping
   every old checkout does not resolve publication gates. Retain canonical and
   recovery checkouts, and skip any live, changed, locked or depended-on lane.
   Only final retirement of the recovery lane depends on its accepted work
   landing on main. Recheck ownership, refs,
   status and ignored material immediately before each retirement. Preserve
   non-regenerable local evidence and settings separately; remove children
   before a containing workspace. Revalidate remaining worktrees, branch and
   remote inventories afterward. Record every removal and recovery location.
   Do not equate archived history with ancestrally merged history.

**Done means:** every historical candidate has a final disposition; accepted
ports are on main with current checks; preserved retired branches/worktrees
are removed; canonical checkouts are clean; remaining branches are explicitly
active or deliberately retained dependency work. No branch/worktree has been
deleted in this mandate's preservation/first-repair step.

The ignored-file inventory is significant: 58 workspace, 48 backend and 30
app checkouts contain ignored entries. Beyond generated caches it includes
native builds, environment files, runtime metadata, captures and local design
assets. The JSON inventories record paths only; bundles do not preserve those
files. A clean `git status` is therefore not sufficient deletion evidence.

Bundle SHA-256 values:

| Repository | Bundle | SHA-256 |
|---|---|---|
| Workspace | `workspace.bundle` | `3de13fc2505f237315b90c532e678bac76c912a51c9510a2af996179d5a1f977` |
| Backend | `backend.bundle` | `0a365c1af46e984d63108a7556347d274a6b9da61197ef2ef77a7226ae5a48ac` |
| App | `app.bundle` | `be101f4bc15fa0a0d0c33ace28f8e7e70f91195e2a6bcda038323c95fc848b8b` |

Restore example (use a new destination):

```sh
git clone --mirror /absolute/path/to/workspace.bundle /new/recovery.git
```

Archived worktree commits can be recovered from the full-SHA refs above;
branch-name mappings
are also in each `*-inventory.json`. These bundles precede the subsequent
metadata repair commits; refresh the preservation receipt before final cleanup.

### September 23 complete baseline repair and local-asset preservation — latest receipt

The remaining backend type boundaries are repaired in `486e8abaf`. Full backend
CI passes: mypy reports **zero errors across 1,888 source files**; offline pytest
reports **21,808 passed, 14 skipped, 1,458 deselected and 53 xpassed**; the additional
checker packet passes 1,004 tests. Eval replay verifies 422 deterministic checks
and skips 14 provider-backed checks. No mypy suppression, feature activation,
schema change or database cleanup was used to obtain this result.

App commits `95df3b3f6`, `4376b2ed9`, `a63d2c590` and `717355b17` close the
remaining baseline defects:

- 38 legacy facades derive from their actual generated owner models, with
  compile-time shape assertions. `EditDayDiff` is classified as UI-only; the
  genuinely extensible workflow receipt retains one bounded exception through
  October 7. Exceptions were not blanket-renewed.
- Places pure routing/scope helpers and unchanged styles move out of oversized
  surfaces. Existing budgets remain unchanged; rendering, ordering and state
  ownership are preserved.
- Test observations and fixtures match current owner contracts. The all-test
  typecheck count falls from 602 to the existing **406** allowance; this is a
  passing unchanged ratchet, **not a fully type-clean test tree**. Journey 19
  asserts authored public profile lines and rejects inferred private interests.
- Twelve literal query/invalidation sites use shared factories. Exact legacy
  tuple shapes, account scopes and graph invalidation prefixes are preserved;
  eight focused suites pass 56 tests. Production TypeScript and both query and
  mutation ownership gates pass.

`npm run verify:pr` passes in 60.618 seconds, including production typechecking,
schema bridges, surface budgets, lint (169 existing warnings), the unchanged
test-type ratchet and 181 mock/HTTP seam tests. Measured log:
`/tmp/vesper-landing-verification/integration-query-owner-mobile-gate-20260923T204102Z.log`.
The final reported app revision is `717355b17398861222bcd9d208a7825d897e08d6`;
the command began before that commit was recorded, so this is verified content,
not an immutable-start landing receipt.

The earlier coordinated `make verify` ran 934.88 seconds: backend CI, contracts,
API coverage, 173 journey tests, 181 seam tests, 126 offline mobile tests and all
384 Maestro flow syntax checks passed. It then **failed** on six overdue flag
reviews and four missing registry entries. Other remaining governance commands
were subsequently run separately and passed. Log:
`/tmp/vesper-landing-verification/integration-complete-repaired-gate-20260923T202434Z.log`.
The app tree changed during that run; it is explicitly not final-tuple evidence.

The registry now records the actual provider-resolution, explicit-research,
object-renderer and Source-worker gates. The six older controls receive a
source-reviewed, bounded October 7 disposition review, preserving their prior
default-off/internal/exact-Trip boundaries and independent latency/cost limits.
No rollout or paid execution is authorized. The flag registry passes all 106
entries. The complete clean-commit gate must still run before publication.

The flag-control regression packet passes 31 backend tests (`test_ai_decision_shadow`,
`test_entity_research_requests`, `test_source_contribution_jobs`) and 30 app
tests (`featureFlags`, `groupTripBuildProfiles`). A clean landing attempt at
workspace `b74abab` was deliberately stopped before publication when an early
governance check identified the generated current-state table's old flag count.
`make docs-status-sync` updates only 102/100 to 106/104 registered/active flags;
all remaining governance commands then pass. The interrupted attempt is **not**
a passing landing receipt; the clean tuple must be rerun after this correction.

**Ignored assets are now preserved separately from Git.** The private manifest
`/Users/feihuyan/vesper-repository-archive-2026-09-23.c4wYxq/local-assets-dl9syyft/manifest.json`
covers 170 historical worktrees (canonical and active recovery checkouts are
excluded), 77 archives, 143,185 verified members and 3,432,638,948 compressed
bytes. Readback verified regular-file SHA-256/length and symlink targets; source
metadata stayed stable during capture. Environment/settings files, local designs,
captures, logs and ignored native builds are included. Regenerable `node_modules`,
`.venv` and named Python/checker caches are excluded. This is local recovery,
not an offsite backup. No historical worktree or branch has been removed.

An Xcode DTServiceHub process (PID 25951 at inspection) still holds a working
directory inside the old native-presentation-wave1 app screenshots. Recheck it
before retirement; a clean Git status alone does not establish runtime ownership.

**Additional publication blocker discovered by the actual backend pre-push
packet:** `pre-commit run --hook-stage pre-push --from-ref origin/main --to-ref HEAD`
fails on **94 expired active documents**: 33 fundraising documents, one product
working document (`MVP Social Loop.md`), three research documents and 57 working
documents. The touched Workbench module's stale `Last updated` header is repaired
to match its September 23 catalog change. Other pre-push checks passed or were
explicitly skipped for unchanged file categories. No hook was disabled.

This is distinct from passing `make -C travel-agent ci`: that command does not
include the full documentation-freshness pre-push check. The clean coordinated
attempt at workspace `f750682`, backend `486e8abaf`, app `717355b17` was deliberately
stopped before any publication once this independent blocker was established.
Its backend, contract and mobile stages passed, but its remaining Maestro/
governance/publication stages are **incomplete**, not a final-tuple pass.

At that checkpoint, do not blanket-renew or blanket-archive those 94 documents. For example, the
fundraising index still calls its fact ledger and application drafts current;
PearX W27's draft records a future October 4 deadline, while founder submission
status cannot be inferred from Git. Some working receipts already name promoted
owners and can become historical; others still claim live social/architecture
authority and need individual reconciliation. The required founder input is
which August fundraising applications remain active. That question is now
resolved by the founder's historical-reference direction below; no external
factual re-verification is claimed in this cleanup.

### September 23 founder-directed fundraising archive

The founder explicitly classified the August accelerator/application work as
historical references. The whole 50-document fundraising packet now lives in
backend `docs/archive/2026-08/fundraising/`, including 33 expired active documents,
13 already-archived research/evidence documents, and four original indexes.
Archival metadata and visible notices distinguish captured August claims from
current instructions. Earlier archive dates are preserved where present, along
with original paths and historical authority declarations. Current
`source_of_truth_for` declarations are empty in archived files.

All 50 original bodies were verified against the archive transformation; the
only body changes are explicit historical notices and relative-link relocation.
Draft/submission fields, founder-supplied facts, old dates, citations and language
are retained, not freshly verified. This does not claim any application was
submitted, withdrawn, accepted or rejected. No content is discarded. The live
`docs/fundraising/README.md` is now navigation to the archive and current product,
investor-narrative and evidence authorities, not an active application queue.
Backend documentation and archive indexes reflect that boundary.

Verification: backend link checking passes across 6,722 Markdown files; product
authority checking passes; workspace child-document governance passes with 404
post-baseline documents; workspace living links pass across 531 files. Checks
were rerun after explicitly staging the moves so the child checker sees the
current index rather than removed old paths. `git diff --cached --check` passes.
The measured documentation-freshness command still **fails with 61 expired
active documents**, none in fundraising; the remaining product/research/working
documents require individual current-owner reconciliation. No gate was changed,
no broad date extension was applied, and no runtime source changed in this step.

Remaining delivery sequence: resolve that lifecycle disposition; clean final-tuple verification; publish for the
protected-main process and align dependency pins in dependency order; resolve
native mixed-Places appearance acceptance; obtain required independent review;
land; refresh preservation and retire exact historical refs/worktrees. Neither
local test success nor archive completeness overrides main protection. The
canonical checkouts and all historical refs are unchanged by this repair batch.

### September 23 typed-owner integration repair — earlier receipt

Backend `c58db9afb` removes **121** of the previously measured 329 type errors;
the complete checker now reports **208 errors in 59 files**. Workspace base was
`79548f2`, backend base `898632684`, app `13f81ba04`. No mypy configuration,
suppression, feature flag, database schema or app source changed.

The batch repairs ten implementation files:

- Life organization/resolution DB helpers declare SQLAlchemy `RowMapping`
  results; decoders also continue accepting fixture mappings. Reconciliation
  receives a concrete sequence matching its existing contract.
- Life keyset queries bind explicitly typed literals. Tests preserve the
  original UUID/time/string values, comparison direction and lookahead limit.
- Both worker and HTTP intake fan-in preserve generic page-item types rather
  than erase anchors and retained sources to `object`. Pagination limits,
  continuation handling and current-authority checks are unchanged.
- Retained-source withdrawal/restoration argument bundles retain typed owner
  fences, exact revision tokens and the optional caller-owned connection.
- Home v1 composition uses the existing semantic-result union across mixed
  owners and empty states; no order, suppression or admission rule changed.
- Source-worker telemetry uses a typed argument bundle. Accounting context
  restoration binds each reset to its correctly typed token and runs in the
  same reverse order. A failure-path regression asserts restoration inside the
  worker's task, where `asyncio.run` isolation cannot mask leaked context.
- Life quality joins validate and normalize the two string endpoints without
  losing their fixed-pair type; measurement semantics remain unchanged.

Verification (same arm64 macOS / Node 24.13.0 / backend Python 3.13.0 environment
as the earlier receipt):

| Command | Result |
|---|---|
| `PYTHONPATH=. .venv/bin/python -m pytest tests/life_projection tests/root_projection tests/api/test_root_projections.py -q --run-quarantined -m 'not requires_postgres and not requires_api_keys and not requires_dogfood_wedge'` | **823 passed, 48 deselected**, zero skips; offline behavior only, not real Postgres execution. |
| Same pytest options on `tests/life_projection/test_life_quality.py tests/life_projection/test_life_organization_reader.py tests/root_projection/test_source_contribution_worker.py` | **34 passed** after the final fixed-pair normalization change. |
| Targeted Ruff, formatting, `git diff --check`, backend commit hooks | **Passed**. No checker exceptions added. |
| `./scripts/sync-types.sh` | **Passed** full offline export, app projection, generation and mobile TypeScript; all three generated files have **no diff**. |
| `make verify` | **Failed** at backend mypy: **208 errors in 59 files**, 1,888 source files checked. Earlier architecture/catalog gates passed; subsequent full-test/frontend/workspace stages of this invocation were **unrun**. |

Measured local logs under `/tmp/vesper-landing-verification/`:
`integration-types-behavior-20260923T193140Z.log` (8.733 s),
`integration-types-wave2-20260923T193141Z.log` (6.645 s; intermediate 209 errors),
and `integration-types-final-gate-20260923T193259Z.log` (59.224 s; final 208).
These record the base heads plus dirty backend changes, not a clean-main or
published receipt. No runtime services were started and no DB cleanup ran.

The 40 mobile facade exceptions and previously recorded presentation/budget
gaps remain open. Next work is the remaining Relationships row/API boundaries,
root v2 adapter unions and Life index/consumer contracts, followed by the
mobile facade repair and a complete-gate rerun. Main and archived historical
refs/worktrees remain untouched. This batch is committed integration progress,
not completion of the consolidation mandate.

### September 23 landing-baseline repair receipt

This is the earlier catalog/schema repair state, superseded by the typed-owner
receipt above where counts differ; failures below are dated observations.
All changes remain on `codex/home-human-opening-recovery-2026-09-23`, not main.

- Backend `898632684`: replaced expired August catalog supply with three
  source-reviewed autumn Season entries and three NYC Here exhibitions.
  Official NPS, NYBG and Grolier sources, dates and limits are recorded in the
  YAML. Typical seasonal timing is not a live forecast; an exhibition window
  is not opening-hours, ticket or current-access evidence. The new entries'
  review expiry is October 9, so another editorial review is required before
  then. Existing Hawaii winter supply remains intact; old entries remain in
  Git history. The runway checker now rejects review expiry inside its claimed
  runway, even when an event itself continues longer. Tests cover valid supply,
  expiry now, expiry during the runway and unreadable catalog inputs.
- API registry: re-reviewed all 55 expired retiring operations against the
  current full export and method-specific mobile source. 34 have no discovered
  caller or transport, 20 have only transport declarations, and one has an
  exported unused hook. Retain them through October 7 with evidence, prior
  rationale and removal triggers preserved. This is an explicit bounded
  compatibility decision, **not deployed zero-traffic evidence**. Three legacy
  route/API bridges received the same source-backed retention decision. No
  route was deleted, activated, or promoted into the app contract.
- App `13f81ba04`: 17 hand-copied enums now project generated model fields;
  two dossier feed envelopes now derive from their actual response models
  instead of being compared to the unrelated `FollowListResponse`. Compile-time
  assertions pin the original 19 facade shapes. The venue-item refinement
  remains independently governed. No SDK, UI, endpoint or runtime behavior was
  changed. This removes 19 exceptions rather than renewing their expiry.

Verification on arm64 macOS, Node `v24.13.0`, backend Python `3.13.0`
(measurement launcher Python `3.14.6`):

| Command | Result and boundary |
|---|---|
| `PYTHONPATH=. .venv/bin/python -m pytest tests/home/test_vesper_workbench.py tests/concierge/test_workbench_entry.py tests/scripts/test_check_vesper_world_catalogs.py -q --run-quarantined -m 'not requires_postgres and not requires_api_keys and not requires_dogfood_wedge'` in backend | **62 passed, 1 deselected**; no database test or service access. An earlier invocation without the offline marker stopped at missing disposable-DB configuration; it did not run tests. |
| `PYTHONPATH=. .venv/bin/python scripts/check_vesper_world_catalogs.py --runway-days 14` | **Passed**, four Season rows and three Here rows; at least three current reviewed rows per band for every checked day. |
| `make api-coverage-check` | **Passed**, 579 active, 15 dark (zero unflagged), 62 retiring. |
| `./scripts/sync-types.sh` | **Passed** offline export, projection, generation and app typecheck; no generated-file diff. |
| `python3 scripts/check_compatibility_ledger.py` | **Passed**, four entries. Retention review is not proof of runtime non-use. |
| `python3 -m unittest scripts/test_api_contract_audit.py scripts/test_project_app_openapi.py -q` | **15 passed**. |
| `npx tsc --noEmit` and `npm run test:typecheck:contracts` in app | **Passed**; compile-time checks include the enum/feed contract assertions. |
| `npx jest --runInBand __tests__/conventions/schemaEnumContract.test.ts` | **2 passed**, no skips. |
| Targeted Ruff and app ESLint; `git diff --check` | **Passed**; ESLint retains one existing array-style warning at `utils/api/types.ts:154`. Commit hooks passed in both children. |
| `npm run schema-bridge` | **Failed**, 40 remaining expired facade exceptions (down from 59). They were not blanket-renewed. |
| `.venv/bin/python -m mypy --config-file mypy.ini backend/` | **Failed**, 329 errors across 69 files, 1,888 checked. No suppressions or ratchet exemptions added. |
| `make verify` | **Failed** at the same backend mypy errors after passing the repaired catalog runway. Later contract/frontend/offline/governance stages in this invocation were **unrun**, regardless of separate focused results. |

Measured logs are local, not portable checked-in evidence:
`/tmp/vesper-landing-verification/landing-catalogs-20260923T191652Z.log`
(7.346 s), `landing-mobile-contracts-20260923T191651Z.log` (17.320 s),
`landing-api-governance-20260923T191852Z.log` (7.863 s),
`landing-schema-bridge-20260923T191706Z.log` (0.496 s),
`landing-backend-types-20260923T190454Z.log` (45.767 s), and
`landing-full-verify-20260923T191854Z.log` (52.679 s), all in that directory.
Measurements recorded base heads workspace `85db3ac`, backend `078d915cb`,
app `7e94c42a8` plus dirty working changes; they are not clean-final-tuple
receipts. Subsequent changes preserved policy rationale, formatted the new
test and replaced the shortened Grolier URL with its verified full URL.
Contract tests and the catalog check were rerun before child commits.

**Remaining execution order:** repair backend DB-row/owner-read/literal typing
without weakening authority or validation; resolve the remaining 40 facade
exceptions against actual endpoint contracts; address existing surface-budget
and Places native/design-evidence gaps; then rerun full gates at the final
tuple and land through protected-main review. Largest current type-error
clusters are `source_contribution_worker.py` (23),
`retained_source_projector.py` (22), root `compiler.py` (21), Life organization
DB code (18) and relationship-handoff routes (18). These are repair targets,
not evidence that every diagnostic is a runtime defect. No historical ref,
worktree or ignored local asset was deleted, and neither local nor remote main
was advanced during this repair.

### First consolidation repair receipt

- Workspace tooling commit `dc5eec7`; app metadata commit `b0115dd05`;
  backend unchanged at `a277ba617`. No product flow body or generated API
  contract changed. `make land-worktree` help now describes its actual
  verify-only behavior rather than promising a main push and teardown.
- `make maestro-flow-check` **passed**: structural validation of 384 flows,
  8 configs and 10 package references; metadata normalization check; and
  Maestro CLI syntax validation for all 384 flows. This is syntax/governance
  evidence, not execution of 384 device journeys.
- `python3 -m pytest scripts/tests/test_maestro_flow_inventory.py -q`:
  **6 passed**, covering the admitted 15-flow inventory, missing selection,
  missing name, wrong lane, malformed YAML and missing app inputs. Measured
  receipt: `docs/reliability/runs/consolidation-maestro-inventory-20260923T172603Z.log`
  (local ignored evidence; Python 3.14.6 on arm64 macOS).
- `node --test scripts/maestro/normalize-metadata.test.mjs` in the app:
  **3 passed**. Ruff checks on the changed Python scripts and format on the
  new test passed; `git diff --check` passed in both affected repositories.
- Documentation governance, inventory, spine, canon, release, status, links
  and Home-surface checks passed. The unrelated compatibility-ledger failure
  has not been repaired by this change. Full `make verify` was not rerun;
  the other recorded baseline failures remain open. No push or main landing
  is claimed by these commits.

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
expired world-catalog rows; current backend main fails the same check. As of
September 23, simply removing those expired rows would leave only two
current Season windows and no current Here window, below the check's
three-per-band, 14-day runway. New source-reviewed editorial supply or an
explicit product decision about that legacy band is required; an expiry bump
is not a cleanup. Separate contract and API coverage checks found `55` expired
operation-review policies
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
| 2 — selectively recovered; native appearance and landing unverified | One server-authored mixed Places page order | Adapted the useful behavior from `engine-er123-integration`, `quality-comparison`, `native-receiving-next` and `timing-proactive-delivery`, not their `page_sequence` wire field. Existing semantic projection order already drives backend section/card sorting. Mobile now interleaves standalone units at that order's whole-section boundaries, preserves relative browse order, and removes local dominant-section promotion. Stable card identities work without optional treatments. Incomplete/contradictory joins preserve existing content and browse order. See the verification receipt below. |
| 3 — policy decision | Automatic returned-Source activation | `strategy-useful-supply` and `native-receiving-next` contain trigger/work-item code, but the current roadmap explicitly holds `trip.completed` activation pending source, purpose, audience, lineage, correction/withdrawal, expiry, duplicate and sparse behavior. Do not port this under a generic “resume old work” instruction. It does not block ordinary Home composition. |
| 4 — separate receiving option | Timed delivery of an *already explicitly requested* Source result | `timing-proactive-delivery` adds durable reconsideration, exact workflow reread and in-app Activity destination. This is separable from automatic activation, but still needs an explicit background/notification treatment decision, current delivery-contract adaptation, migration/restart evidence and app destination authority checks. |
| Later, if a measured gap | Per-run engine trace / scarce owner-read ordering | ER1/ER2/ER3 contain content-free trace and read-order ideas. Main has newer shared composition, bounded owner reads and aggregate telemetry. Recover only against a demonstrated missed-candidate or diagnostic problem, with privacy and latency checks. |

The old `cw2-object-continuity` human-Reply safety gate is recovered into the
current Social implementation roadmap as a specific original/pair acceptance
boundary. Its reverted implementation is not revived. `package-b-answers-help`
and `requested-visit-window` are preserved, deferred product/owner choices,
not requirements to implement before retiring their Git branches.

### September 23 useful-work integration receipt

Committed child revisions: backend `078d915cb`, app `7e94c42a8`, both on
`codex/home-human-opening-recovery-2026-09-23`. These include the preceding
Home recovery and metadata-repair commits; they are not main or remote refs.

The accepted code recoveries are the Home human-note/current-Place join above
and the mixed Places renderer. Neither imports a second content owner or
reinstates the pre-pivot operational product. The Places recovery also closes
two contract/exposure defects: an untreated browse unit cannot be rendered
again as a standalone field, and a withdrawn unit's cached geometry cannot
re-register its delivery exposure when a surviving segment moves. Treatment
bindings must name the exact rendered card's semantic identity.

Remaining named candidate dispositions:

- **Superseded:** `content-quality-correction`'s old `httpx.HTTPError` catch
  (`a49068dad`) targets a removed semantic-reader implementation in
  `backend/places/search.py`. Current retained-reading search uses the bounded
  optional producer path. Do not transplant a dead exception tuple/import.
- **Deferred, preserved, not shipping:** automatic Source activation, timed
  delivery of explicitly requested results, custom visit-window controls and
  dark PrivateGraph/assistance expansion. Their respective policy/control
  decisions remain in the current roadmap; archived code is reference only.
- **Not recovered without a demonstrated current gap:** ER run-trace and
  scarce-owner-read machinery. Current shared composition, bounded owner reads
  and aggregate telemetry supersede whole-branch adoption; no parallel engine
  ledger is introduced merely to retain historical code.
- **Selective documentation recovery only:** the original-Reply gate in
  `cw2-object-continuity`. Current group-room human delivery is not proof of
  durable exact-pair provenance or atomic audience-safe original Reply.
- **Reference evidence, not product ports:** historical source-anatomy,
  cold-city/lens and native-original QA variants. Keep their bundled history;
  current owner tests and current runtime receipts, rather than old fixtures,
  decide present acceptance. Dependency updates stay outside product recovery.

Executed from this coordinated lane with the working-tree changes applied:

- `PYTHONPATH=. .venv/bin/python -m pytest tests/root_projection -q --run-quarantined`
  in `travel-agent`: **505 passed**, no skipped cases. This is the root packet,
  not the entire backend or database/native acceptance.
- App Jest packet: `placesPageRenderItems`, `PlacesSectionExposure`,
  `PlacesSemanticField`, `PlacesSectionFeed`: **76 passed**. App
  `npx tsc --noEmit` and changed-file ESLint passed; backend changed-file Ruff
  passed. Tests cover actual rendered interleaving, stable `.open-now`
  identity without treatment, field withdrawal, no treatment-only action
  authority, complete sections, adjacent fields and malformed/legacy fallback.
- Measurement logs are in `/tmp/vesper-recovery-verification/`; they fingerprint
  the pre-commit HEADs and dirty working trees, not a falsely clean revision.
- `./scripts/sync-types.sh`: full offline OpenAPI export succeeded and produced
  **no snapshot diff**. App projection/type regeneration is **blocked** by the
  existing 55 expired operation-policy reviews. No wire field changed; generated
  files were not edited or bypassed.
- Scenario registry: 31 scenarios passed. Places design manifest check:
  six pairs passed structurally, **zero external canon references verified**.
  No fresh native/visual parity is claimed for mixed order.
- Surface budgets still fail at existing `PlacesWorkspace` and
  `editorialFeedCard` limits: baseline 819/112 lines versus 768/87 allowed;
  the changed workspace is 814 lines. The recovered `PlacesSectionFeed`
  shrank from 369 to 323, within its 332-line limit. No limits were raised.
- Fresh measured `make verify` passed workspace doctor, backend Ruff/format,
  import/cycle/route checks and structural gates, then **failed** at the eight
  expired world-catalog rows. Later steps in that invocation, including mypy,
  contract drift, app tests and final documentation gates, were **not reached**.
  The separate checks above do not turn that command into a pass.

Useful historical behavior is now represented in the integration candidate,
with explicit dispositions for the other named candidates. **This is not main
landing or cleanup completion.** The complete-gate failures recorded above,
native appearance boundary, protected-main landing and ignored-file preservation
still apply. Historical branches remain recoverable and have not been deleted.

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

**Fresh fetch after preservation:** four backend remote tracking refs and one
app tracking ref were pruned because their branches were already deleted on
the remote. No remote branch was deleted by this task. Backend now has two
remote dependency tips (`python-minor-patch-6245ec17e7` and
`sentence-transformers-gte-6.0.1`); app has five (the refreshed
`npm-minor-patch-aa826fd39b`, React Native 0.87.1, Purchases and Purchases UI
10.9.0, and Worklets 0.12.1). The old refs and prior npm group tip remain in
the verified bundles. Use this current inventory for maintenance; the initial
audit paragraph below records the earlier state, not a live upgrade queue.

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

## Original selective-recovery plan (superseded in scope by the mandate above)

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
3. **Mixed Places order recovered in the consolidation lane.** Use the
   existing semantic projection to interleave whole browse sections and field
   units while retaining authoritative relative section order. Do not revive
   historical `page_sequence` or start a second recovery lane. Focused behavior
   is verified above; native appearance and final landing remain separate.
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

The original plan favored one owner-backed Home recovery. The later founder
mandate above expands this task to repository consolidation while retaining
its selective-port rule: historical code is evidence, not automatic product
scope.
