---
doc_type: working
status: active
owner: founder / Orchestration
created: 2026-09-22
last_verified: 2026-09-22
expires: 2026-10-06
why_new: Records actionable defects in a new 24-hour implementation window without rewriting the earlier 12-hour review or mixing new findings into its repair receipts.
supersedes: []
source_of_truth_for:
  - findings from the September 22 functional-implementation code review
---

# Functional implementation — September 22, 24-hour code review

## Conclusion

**Seven actionable findings: one P1, five P2, one P3. All seven now have
repairs and focused regressions in the current working tree.** Six change
product source; the seventh hardens the local rehearsal runner. The repair pass
kept the existing owner and renderer boundaries and introduced no new service
or product primitive. The backend and app repairs are committed locally on the
coordinated branch; native-device and disposable-DB acceptance remain open.

The work extends existing owners rather than introducing another competing
product architecture. The principal regressions are at the joins: the server
selects or supplies something, but the renderer drops, reorders or mislabels
it; or presentation geometry produces an incorrect delivery signal. These
need correction before treating the new full-scroll compositions as accepted.

Existing tests remain green: **469 mobile tests across all 36 changed Jest
suites**, plus **156 focused backend tests**. Those results do not negate the
new failing cases below and do not constitute release or visual acceptance.

## Scope and pinned revisions

Review window: **September 21, 2026, 18:04:38 EDT through September 22,
2026, 18:04:38 EDT** (`2026-09-21T22:04:38Z`–`2026-09-22T22:04:38Z`).
The end is the time captured at the start of this review, not a moving window.

Reviewed coordinated checkout:
`/Users/feihuyan/travel-workspace--functional-implementation-2026-09-20`.
All three repositories were on `codex/functional-implementation-2026-09-20`
and clean before the review. The canonical main checkout's unrelated design
edits were left untouched.

| Repository | Baseline before window | Reviewed HEAD | Diff size |
|---|---|---|---|
| Workspace | `f56975baeee5f77b4fe85d5afb9f7d451a793de1` | `6455342bb9294d71bc57dbbc1a9f7ae2ae128f25` | 8 files; +3,775 / −275 |
| Backend | `ef4167163f50bcfcd681448a8bda15588d6f8127` | `1aadcfb8dbbfe92a319f71c769b2b6f1870f6db2` | 64 files; +6,239 / −183 |
| App | `76af974a058569d594425ea595a86f43015cb611` | `aefcc034356a2d13ce6937f0d75b6d01cd3a6e33` | 124 files; +8,228 / −712 |

Repair commits, created after the reviewed HEADs above:

- Backend: `2e2d92753cb46aba3ca8ef2a08e091cafedd10d1`
- App: `36ad8acd0280bb54047a8be4b3e327880f9a1cc0`

Both are on `codex/functional-implementation-2026-09-20`. Neither was pushed
or merged. Workspace documentation for this repair pass is committed
separately.

The review used baseline-to-HEAD diffs, including changes integrated by merges,
then followed changed runtime paths into their callers, owner contracts and
tests. It is not an audit of every unmerged branch or every pre-existing file.
Generated schemas were treated as contract changes, not independently authored
implementations. Large roadmap/receipt additions were checked for scope and
evidence boundaries rather than treated as proof that features work.

The [September 21 review](functional-implementation-code-review-2026-09-21.md)
remains the historical ledger for its earlier window and repairs. New IDs below
are deliberately distinct from its R01–R11.

## Findings at a glance

| ID | Priority | Defect | Evidence |
|---|---|---|---|
| CR24-01 | P1 | Nested Places layouts report off-screen units as visible | Failing controlled-layout React test; receipt path traced |
| CR24-02 | P2 | Home's authored-note renderer drops the friends continuation | Failing renderer test with the actual action shape |
| CR24-03 | P2 | Places discards its fallback before admitting its replacement | Executed merge/selector reproduction |
| CR24-04 | P2 | Outcome sequence truncation makes the “latest” destination stale | Executed nine-outcome adapter reproduction |
| CR24-05 | P2 | Standalone Places branches can precede a server-elected browse dominant | Static runtime-to-renderer trace |
| CR24-06 | P2 | Ordinary outcomes are misclassified as travel in Home | Failing outcome-only Home renderer test |
| CR24-07 | P3 | Partial Source-field fixture setup bypasses cleanup | Static shell/Python control-flow trace |

| Finding | Repair now present | Regression evidence |
|---|---|---|
| CR24-01 | Places field/group/heading offsets are summed before shared registry update | Joined feed, multi-group, reflow, scroll-return and receipt-dwell tests |
| CR24-02 | Unmatched region-level actions render once after per-person cards | Authored Home renderer taps exact person doors and friends continuation |
| CR24-03 | Merge retains fallbacks until Places selector admission | Eligible lead wins; repeated, expired and unknown-status leads leave fallback |
| CR24-04 | Adapter selects newest eight outcomes, then presents chronologically | Ten shuffled outcomes with tied timestamps; sequence and latest destination asserted |
| CR24-05 | A browse-backed dominant section leads before standalone branches | Final feed tree order asserted for dominant browse plus social branch |
| CR24-06 | Travel wording/order needs Trip or Journey ref; vague time copy is neutral | Outcome-only continuity stays ordinary; explicit trip binding retains label/order |
| CR24-07 | Run-scoped EXIT cleanup is armed before fixture apply and preserves status | Runner contract tests and shell syntax check |

P1 here means incorrect delivery/treatment facts can affect later product
behavior, not merely analytics. P2 findings break concrete user-facing
contracts. P3 is a local rehearsal reliability defect. None is a claim of a
confirmed production incident.

## CR24-01 — [P1] Normalize nested Places coordinates before recording exposure

**Location:** [PlacesSemanticField.tsx](../../travel-app/components/places/PlacesSemanticField.tsx),
lines 142–146 and 167–186. Introduced by the new semantic-field composition
(`5e3da033b`). Related paths:
[PlacesSectionFeed.tsx](../../travel-app/components/places/PlacesSectionFeed.tsx),
[useSectionViewportRegistry.ts](../../travel-app/hooks/useSectionViewportRegistry.ts),
[RootUnitExposureBoundary.tsx](../../travel-app/components/root-projection/RootUnitExposureBoundary.tsx).

The registry expects each unit's `y` to be relative to the feed origin. The new
field wraps units in a field View and then an additional View or PlacesSection.
The boundary now forwards `onLayout` unchanged, so its `y` is relative to its
immediate group, not to the feed. Neither the field offset nor group/header
offsets are added. Mature browse cards already perform this coordinate sum;
standalone units do not.

**Reproduction:** give the viewport height 600 and feed origin 0; place a
trailing field after 2,000 points of browse; give its first unit local `y=0`,
height 200. The real registry reports `isVisible(...) === true`. A temporary
React test asserting false failed. No native layout engine was run: the test
supplied parent-relative layout events explicitly.

**Consequence:** when delivery/treatment proofs are present and normal exposure
conditions are satisfied, dwell can record `rendered` for material the person
has never reached. On scrolling to the actual unit, the inverse error is also
possible. These receipts feed delivery suppression and treatment observation;
this is more than an impression-counter error. A live backend receipt write
was not exercised in this review.

**Fix direction:** register absolute feed-relative unit bounds, accounting for
both field segments, nested groups, headings and later reflow. Reuse the shared
registry rather than adding a second visibility system.

**Required regression:** render the joined browse + semantic feed; prove zero
receipts for below-fold units, then exactly one qualified receipt after actual
intersection. Include multiple groups, titled groups, dynamic text height and
return scrolling. Follow with one native scroll check.

**Repair:** the semantic field now adds feed, group, PlacesSection-header and
unit offsets before updating the shared registry. The regression renders the
joined feed, keeps the nested unit below fold, advances dwell without a receipt,
then scrolls it into view and verifies one receipt. Focused layout coverage also
includes multiple groups, a titled group, reflow and scrolling away/back.
Native-device scroll geometry remains unverified.

## CR24-02 — [P2] Preserve region-level actions beside per-person Home cards

**Location:** [HomeRootV2UnitRenderer.tsx](../../travel-app/components/home-root/HomeRootV2UnitRenderer.tsx),
lines 708–745 (`AuthoredRegionBody`; introduced by `8e27ee69a`). Producer:
[home_portfolio.py](../../travel-agent/backend/root_projection/v2/home_portfolio.py),
lines 218–250 (`_attach_places_friends_door`, added in `60da1dcb9`).

The backend appends **From friends in Places** when there are at least two
eligible friend-save contributions. That action targets a `places_context`.
The renderer only emits one action matching each person's case `source_ids`
(handoff/venue). The context-level action matches no case and there is no
remaining region-actions render pass.

**Reproduction:** extend the existing two-person authored-region fixture with
the backend's `places.open_friends` action and context ref. The people cards
render, but `getByText("From friends in Places")` fails. The route resolver
already supports this action; its control is simply unreachable here.

**Consequence:** the social continuation added in the same implementation
window is silently lost. This does not make the entire Places tab inaccessible.

**Fix direction:** bind per-person actions by exact identity as now, then render
the remaining server-provided region actions once. Do not revert to matching
actions by array position.

**Required regression:** compile an authored region containing two exact notes
and the friends continuation; render it and tap all three doors. Verify exact
note identity/revision and the context + `friend_activity` route parameters.

**Repair:** exact source matching remains per-person; the renderer tracks those
matched action objects and renders the remaining server-authored region actions
once after the cards. The focused renderer test taps both exact note doors and
the Friends-in-Places continuation and asserts the exact action object reaches
the owner callback.

## CR24-03 — [P2] Keep the fallback until the replacement passes admission

**Location:** [source_contribution_runtime.py](../../travel-agent/backend/root_projection/v2/source_contribution_runtime.py),
lines 676–690; introduced by `796aa0223`. Consumers:
[root_composition.py](../../travel-agent/backend/api/services/root_composition.py),
[selectors.py](../../travel-agent/backend/root_projection/v2/selectors.py).

`merge_source_contribution_candidates` removes `FIELD_BALANCED_FALLBACK` as
soon as a Source production contains a `FIELD_LEAD_COMPOSITION`. This is before
current owner/value checks and delivery suppression. A retained production is
not a guarantee that its candidate will be admitted on this request.

**Reproduction:** produce the existing deterministic Home/Places Source fixture,
add an independently eligible fallback, and mark the Source lead's fact key as
already delivered. Running selection with both candidates retains the fallback.
Running the new merge first, then the same selector, admits nothing; the Source
lead is rejected with `repeated_exposure`.

```text
without destructive pre-merge removal: ['review.fallback']
after pre-merge removal: []
lead rejection: repeated_exposure
```

**Consequence:** a sparse Places field can lose its honest fallback on a normal
subsequent visit. Other independently admitted content, if any, remains; this
does not imply every Places response becomes blank. Expiry or failed later
owner admission creates the same structural risk.

**Fix direction:** retain fallback candidates through hard/value/exposure gates.
The Places selector already knows how to suppress fallback when substantive
eligible material wins. Make replacement an admission decision, not an
unconditional merge-time deletion.

**Required regression:** valid lead replaces fallback; already-delivered,
expired, and owner-unavailable leads do not erase an otherwise eligible
fallback. Exercise the actual composition pipeline as well as the selector.

**Repair:** merge no longer deletes fallbacks. The selector suppresses one only
when a substantive candidate passes admission. Tests cover the retained merge,
an eligible lead winning, and fallback survival when the lead is already
projected, expired or has unknown owner status.

## CR24-04 — [P2] Cap reconstructed outcomes from the recent end

**Location:** [adapters.py](../../travel-agent/backend/root_projection/v2/adapters.py),
lines 572–576, 606 and 645–652; introduced by `cc357a7c7`.

Occasion outcomes are sorted oldest-first and truncated with `[:8]`. The last
retained item becomes `latest_ref`, and the unit promises to open the latest
record. With nine or more outcomes, that is not the latest outcome.

**Reproduction:** supply nine chronological outcomes to
`home_candidates_from_experience`. The sequence contains Outcome 0 through
Outcome 7; its destination is index 7 although the newest is index 8. The newest
ref is absent from the sequence dependencies and revision digest.

**Consequence:** an accumulating occasion's reconstruction can stop advancing
and its “latest” door opens an older record. Extra outcomes remain eligible for
separate candidate treatment; this is not loss of their underlying records.

**Fix direction:** select the newest bounded set, then display that set in
chronological order. Ensure the destination and digest include the actual
newest retained outcome. If the desired product is an earliest-history excerpt,
name it honestly and still separate its exact latest-record destination.

**Required regression:** 2, 8, 9 and more outcomes; equal timestamps; shuffled
input; adding a newer record changes the sequence identity and latest door.

**Repair:** the adapter takes the newest eight by `(created_at, id)` and sorts
that bounded set back into chronological display order. A ten-outcome shuffled
fixture with timestamp ties verifies the represented sequence, source refs and
latest destination.

## CR24-05 — [P2] Preserve the dominant across both Places renderer families

**Location:** [PlacesSectionFeed.tsx](../../travel-app/components/places/PlacesSectionFeed.tsx),
lines 248–256; [PlacesSemanticField.tsx](../../travel-app/components/places/PlacesSemanticField.tsx),
lines 64–95. Relevant change: `5e3da033b` / `bdef50f72`.

The backend can elect a mature browse card as dominant while also admitting a
standalone branch, such as a social comparison. The runtime removes card-backed
units from `field_units` because they will render in `workspace_feed`.
`partitionPlacesSemanticField` only searches that standalone array for the
dominant. When the dominant lives in browse it is not found, and the component
unconditionally renders every “leading” standalone unit before every browse
section.

**Consequence:** a lower-priority social/other branch can precede the exact
practical answer or changed-place card the server elected to lead. Preserving
order inside each separate array does not preserve the joined field order.
This is a static cross-layer finding; no native ordering receipt was captured.

**Fix direction:** compose a single ordered render plan from the semantic unit
order and its mature-card bindings, or minimally reserve the first slot for a
browse-backed dominant before placing standalone branches. Keep selection on
the server; do not add independent mobile ranking.

**Required regression:** both directions of the join—standalone dominant with
browse branches, and browse dominant with standalone social/reading branches.
Assert final rendered order, not only the partition helper's output.

**Repair:** when the server-elected dominant has an exact mature-card binding,
its browse section is rendered first and leading standalone units follow it.
Server selection still owns the choice. A final-tree test covers a browse
dominant and standalone social branch; standalone-dominant ordering remains
covered by `partitionPlacesSemanticField`.

## CR24-06 — [P2] Do not infer a trip from an Outcome resource kind

**Location:** [HomeRootV2Screen.tsx](../../travel-app/components/home-root/HomeRootV2Screen.tsx),
lines 90–109; introduced by `a5d0e54d8` and `a8cb8fc94`.

Both `regionLabel` and `displayRegions` count any `outcome` ref as travel
evidence. Outcomes also represent dinners, local encounters and other ordinary
life. An outcome with no Trip/Journey binding therefore receives **From the
trip**; under returned posture it also qualifies for travel-specific continuity
promotion.

**Reproduction:** render a Home envelope whose continuity represented refs
contain only `outcome:local-dinner`, with no Trip/Journey ref. The assertion that
`FROM THE TRIP` is absent fails.

**Consequence:** the everyday-life model is mislabeled as the legacy travel
product. This is a semantic classification error, not a preference about
typography. Nearby label logic also calls any prepared possibility/invitation
“This afternoon” without a time check; cover that in the same contextual-copy
repair rather than treating display kind as time evidence.

**Fix direction:** require an explicit travel association for travel-specific
copy/order; otherwise use neutral continuity language. Time-specific copy must
come from the relevant schedule and timezone, or remain neutral.

**Required regression:** local dinner, unbound observation, explicitly
trip-bound outcome, multi-occasion content, and an evening/future invitation.

**Repair:** only explicit Trip/Journey refs now trigger trip-specific continuity
copy or return ordering. Prepared possibilities and invitations use “Coming
up” instead of an unsupported afternoon claim. Home renderer tests verify
ordinary outcome continuity remains “Carried forward” and explicit trip
binding retains “From the trip” and the corresponding return ordering.

## CR24-07 — [P3] Install Source-field cleanup before the first write

**Location:** [run-places-source-field-real.sh](../../travel-app/scripts/maestro/run-places-source-field-real.sh),
lines 44–56. Related setup:
[provision_places_source_field_rehearsal.py](../../travel-agent/scripts/provision_places_source_field_rehearsal.py),
lines 260–291.

The wrapper runs `fixture --apply` before installing its EXIT trap. Provisioning
is multi-step: it writes public readings, resolves their refs, then writes and
finalizes an Intake attachment. These are not one outer transaction. If a later
step fails after earlier commits, `set -e` exits before any cleanup is registered.

**Consequence:** a failed local rehearsal can leave synthetic owner material
or profile changes behind and contaminate subsequent Home/Places evidence.
The newer Home Outcome wrapper already arms cleanup before provisioning.
No destructive/database reproduction was performed for this finding.

**Fix direction:** arm run-scoped cleanup before apply, make it safe after
partial initialization, and preserve the original failure while reporting any
cleanup failure. Never broaden cleanup to unrelated account/run data.

**Required regression:** stub provisioning to commit its first stage and fail
its second; verify cleanup is invoked for that run. Separately verify partial
cleanup against a disposable database, including absent-run no-op behavior.

**Repair:** the runner arms an idempotent, run-scoped EXIT cleanup before
`--apply`. The EXIT handler preserves the original rehearsal exit status and
reports cleanup failure; a cleanup failure after a successful run still makes
the run fail. Structural Node tests and `bash -n` pass. Partial fixture
provisioning against a disposable database remains unverified.

## Coverage and remaining uncertainty

| Area | Review performed | Boundary |
|---|---|---|
| Home | Portfolio/adapters, attention breadth, sample lifecycle, receipts, outcome/participant producers, renderer, actions and return routes | CR24-02/04/06; no native full-scroll recapture |
| Places/content | Public/saved-place supply, release filtering, finite selection, Source merge, runtime joins, semantic/mature renderers and exposure | CR24-01/03/05; no live provider production |
| Social/entity | Exact selected-handoff ID/revision through backend filtering, route params, owner reread and reply/keep/pass updates | No additional confirmed defect in this pass; no renewed two-account device exercise |
| Life | Keyset original refind, pagination, authority-lens index changes, anchor lens membership, answer presentation, exact depth/return | Focused tests green; DB and cross-device behavior not rerun |
| Media/Chat | Original-media state, authenticated audio readiness, gallery teardown, pending route seed consumption and foreground invalidation | Changed suites green; native codec/playback/focus transitions remain unverified |
| Worker | Lease heartbeat, fenced renewal/completion, exception handling and focused worker tests | No additional confirmed defect; process interruption/provider retry evidence remains separate |
| Tooling/contracts | Changed rehearsal setup/cleanup and runners, API policy/schema deltas, historical review and roadmap claims | CR24-07; no fixture mutations or broad pre-push gate run |

Two focused follow-ups are **not** promoted to confirmed findings here:

- Private audio tears down on unmount/custody change, but the new preview has no
  route-focus cleanup. Check a stack push that keeps the reader mounted, and a
  background transition while native readiness is pending. Whether audible
  playback continues depends partly on native audio-session behavior; mocked
  readiness tests do not settle it.
- Existing September 21 evidence gaps—particularly interrupted-worker recovery,
  persisted release/cohort acceptance and native timezone cases—were not closed
  merely by running today's offline tests. Consult that ledger for exact scope.

## Verification record

Environment: Darwin arm64; Node `v24.13.0`; backend virtualenv Python `3.13.0`.
The workspace measurement wrapper runs under Python `3.14.6`; that is not the
interpreter used by backend pytest.

### Repair verification

From `travel-agent/`:

```sh
.venv/bin/python -m pytest tests/root_projection/test_source_contribution_runtime.py tests/root_projection/test_home_portfolio.py -q
.venv/bin/ruff check backend/root_projection/v2/source_contribution_runtime.py backend/root_projection/v2/adapters.py tests/root_projection/test_source_contribution_runtime.py tests/root_projection/test_home_portfolio.py
.venv/bin/ruff format --check backend/root_projection/v2/source_contribution_runtime.py backend/root_projection/v2/adapters.py tests/root_projection/test_source_contribution_runtime.py tests/root_projection/test_home_portfolio.py
```

**Passed:** 106 backend tests; Ruff lint and format checks passed.

From `travel-app/`:

```sh
npm test -- --runInBand __tests__/utils/homeRootV2Renderer.test.ts __tests__/components/HomeRootV2Screen.smoke.test.tsx __tests__/components/places/PlacesSemanticField.test.tsx __tests__/components/places/PlacesSectionExposure.test.tsx __tests__/components/places/PlacesSectionFeed.test.tsx __tests__/components/places/PlacesRootV2Screen.test.tsx __tests__/utils/rootProjectionNavigation.test.ts
npm run test:typecheck:contracts
node --test scripts/maestro/places-source-field-real.test.mjs
bash -n scripts/maestro/run-places-source-field-real.sh
```

**Passed:** 7 Jest suites / 168 tests; contract TypeScript check; 2 runner
tests; shell syntax. ESLint on changed TS/TSX files reported **0 errors** and
one `max-lines` warning for `HomeRootV2UnitRenderer.tsx` (above the configured
800-line limit).

### Existing regression packets

From `travel-app/`:

```sh
git diff --name-only 76af974 HEAD -- __tests__ | xargs npm test -- --runInBand
```

**Passed:** 36 suites, 469 tests, no skipped tests reported. The run emitted
existing asynchronous React `act(...)` warnings in the original reader and an
expected push-failure warning; they were not reclassified as passing native
behavior.

The same packet was rerun after all temporary probes were removed, through
`scripts/measure_verification.py --label review-24h-mobile`, wrapping the
command above with `bash -c 'cd travel-app && ...'`. It again passed all 469
tests. Log: `docs/reliability/runs/review-24h-mobile-20260922T221746Z.log`.

From the coordinated workspace:

```sh
python3 scripts/measure_verification.py --label review-24h-backend-corrected -- bash -c 'cd travel-agent && exec env -u TEST_DATABASE_URL -u TEST_DATABASE_DISPOSABLE .venv/bin/python -m pytest -q --no-cov tests/root_projection/test_home_portfolio.py tests/root_projection/test_places_runtime.py tests/root_projection/test_source_contribution_runtime.py tests/root_projection/test_source_contribution_worker.py tests/life_projection/test_life_index_projector.py tests/life_projection/test_anchor_projector.py tests/life/test_original_refind.py'
```

**Passed:** 156 tests, no skips. Measurement log:
`docs/reliability/runs/review-24h-backend-corrected-20260922T221333Z.log`.
Two earlier invocation errors ran no tests: a nonexistent `test_index_projector.py`
path, and a relative `.venv` path passed to the workspace-root measurement
wrapper. The corrected invocation above supersedes neither error silently.

### Review-only negative probes

Temporary assertions were applied to the existing tests, run, then removed
exactly. Product files and committed test contents were restored unchanged.

```sh
npm test -- --runInBand __tests__/utils/homeRootV2Renderer.test.ts __tests__/components/places/PlacesSemanticField.test.tsx --testNamePattern='addressed human|review24h'
npm test -- --runInBand __tests__/components/HomeRootV2Screen.smoke.test.tsx --testNamePattern=review24h
```

**Expected failures observed:** missing friends action; off-screen unit reported
visible; outcome-only continuity labeled as a trip. The first filtered run
skipped 16 nonselected tests and the second skipped 19; these were selection
exclusions, not quarantines. The separately run unmodified packet passed all
36 changed suites.

For CR24-03, an inline Python probe reused `_portfolio`, `_assembly_request`
and `_draft` from `test_source_contribution_runtime.py`, called
`produce_source_contribution`, then compared `select_places_candidates` before
and after `merge_source_contribution_candidates` with the lead fact in
`projected_fact_keys`. For CR24-04, an inline Python probe constructed nine
`ProjectedOutcome` records sharing an Occasion and called
`home_candidates_from_experience`. Both executed offline with the actual
production functions; neither called a provider or database.

**Not run:** `make verify`, complete backend suite, disposable-Postgres/HTTP
acceptance, Maestro, native audio/gallery exercises, device visual comparison,
production services or deployments. No skipped check is implied green.

`make docs-check` **failed** (exit 2). Governance, child governance, spine,
canon, release, Home-surface governance and living-link checks passed (500
Markdown files checked). The inventory check and generated status check failed
because the already tracked
`docs/working/practical-judgment-producer-acceptance-brief-2026-09-09.md` is
unclassified. The compatibility check also reports three bridge entries
expired September 15: `discover-url-bridge`, `atlas-tab-url-bridge` and
`discover-map-api-bridge`. These pre-existing governance items were not changed
as part of the seven code repairs. The review-only negative probes were removed
before repair work. The working tree now intentionally contains the backend/app
repairs and regressions; `git diff --check` is recorded after this repair pass.

## Repair disposition and next acceptance step

1. **Places composition integrity:** CR24-01, CR24-03 and CR24-05 now have
   focused geometry, admission and final-order regressions.
2. **Home continuity/social completeness:** CR24-02, CR24-04 and CR24-06 now
   have adapter/renderer regressions at their server-to-surface joins.
3. **Rehearsal cleanup:** CR24-07 now arms cleanup before writes and checks
   runner exit-status behavior structurally.
4. **Remaining acceptance:** run a joined Home/Places native pass for scroll,
   action, exact destination and return; run the Source-field fixture against a
   disposable database and prove partial-apply cleanup plus absent-run no-op.
   Those checks remain open and are not implied by the local tests.
