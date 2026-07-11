---
doc_type: working
status: active
owner: founder / engineering
created: 2026-07-11
last_verified: 2026-07-11
expires: 2026-08-10
why_new: No existing document owns a cross-repo architectural-simplification ranking; working/ is the governed home for expiring investigations; archive to audits/ on close.
supersedes: []
source_of_truth_for: [architecture-simplification-backlog-2026-07]
---

# Architecture Simplification Audit — 2026-07-11

**Scope:** `travel-agent` (backend, 263k LOC + 237k test LOC), `travel-app` (frontend, ~317k TS/TSX incl. 34.7k generated), and the workspace coordination layer (Makefile, scripts/, docs governance, design/, CI hooks).
**Question:** which designs can be simplified for practicality, lower maintenance, and lower logic tax — and which complexity is load-bearing and must not be touched.
**Method:** three parallel code-grounded investigations (backend / frontend / cross-repo), followed by direct verification of every claim that would change a recommendation. Verified 2026-07-11: `LLM_FAILOVER_PROVIDER` absent from `fly.toml` and all `.env*`; `_resolve_legacy_family` live at `concierge_feed.py:629,661,693` with the legacy-seven CHECK at `core/db/_tables/home.py:221`; 229 manual `conn.commit()` sites; persona `.generated.json` files referenced only in "kept in sync by hand" comments; `DeckCompareFace` imported nowhere; 462 design-bundle files git-tracked (`design/` = 219MB on disk).

---

## Executive summary

The complexity in this codebase is **not** diffuse. It concentrates in four repeating patterns, which orders the whole cleanup:

1. **Dormant capability that hasn't been made real** — the multi-vendor LLM layer (~5.5k LOC, never exercised against a real network). **Founder decision 2026-07-11: the layer stays** — vendor portability is strategic. The recommendation therefore flips from *delete* to *verify and light up*: the tax was never its existence, it's the unverified-shelf status (the 07-09 debt-audit fixes closed the catalogued bugs; the one open item, P2-1, is a founder-gated live-spend verification).
2. **Migrations finished 44–90% and then abandoned** — leaving *two idioms* for one concept, which is worse than either idiom alone: `get_tx` vs manual commits (229 sites), card-family wire-vs-DB taxonomies (bridge still live), TTLCache vs ≥10 hand-rolled caches, FE persona bundles hand-mirroring seed JSONs.
3. **Completed-campaign residue** — the dogfood/corpus import machinery (finished 06-29) still occupies ~30% of the Makefile and ~45% of workspace scripts; 66 dated design briefs; ~135MB of superseded design bundles tracked in git; three journey-certification oracles frozen since 06-28 contradicting the one canonical generated matrix.
4. **Parallel read/render models for the same surface** — 3 trip-home read models + 3 card types + 2 translators on the backend; 3 screenshot-QA systems with 3 vocabularies on the frontend.

Meanwhile the things that *look* most excessive — the OpenAPI snapshot churn, the eval-regression gate, the ratchet scripts, the journeys.yaml SSOT, the flag registry, the 3-repo structure — are precisely the load-bearing discipline that kept 3,600 commits coherent. They are catalogued in the **Do-NOT-touch** section and should survive any cleanup.

**Total opportunity:** roughly **−20–25k LOC of hand-maintained code** (the multi-vendor layer's ~5.5k stays by decision), −135MB of git payload, 70→~40 Make targets, ~10 fewer hook entries (~2–4s per commit), and three dual-idiom states collapsed to one — with only two items carrying medium risk (both sequenced behind a dogfood soak).

---

## Top findings, ranked by tax-reduction ÷ risk

| # | Finding | Repo | Size | Risk | Category |
|---|---------|------|------|------|----------|
| 1 | Make the multi-vendor LLM layer real: P2-1 live verification (Bedrock/Vertex/OpenAI creds + one real call each), then wire `LLM_FAILOVER_PROVIDER` in prod — **KEEP decision 2026-07-11** | agent | ~hours + small spend | Low | D strategic |
| 2 | Finish persona Cut 3 on the FE + stop committing `.generated.json`; generate fixtures from seed JSONs | app | −12–15k LOC | Med | B/C |
| 3 | Card-family DB migration; delete `_resolve_legacy_family` bridge | agent | ~1 day | Low | B dual-idiom |
| 4 | Finish `get_tx` sweep (229 sites); delete `check_db_commit.py` linter | agent | 1–2 days | Low | B dual-idiom |
| 5 | Workspace residue sweep: `dogfood.mk` split, scripts attic, `git rm --cached` 135MB design bundles, retire 3 stale journey oracles | ws | −30 targets, −135MB | ~Zero | A residue |
| 6 | Fold journey-cert scripts under `persona_cert` | agent | −1,200 LOC | Low | B |
| 7 | Fold 3 screenshot-QA systems → 1 (+ cut ~40 npm script aliases) | app | −2–3k LOC | Low | B |
| 8 | Split god modules: `core/db/trips.py` (4,499), `concierge_feed.py` (3,217) | agent | refactor | Low | C |
| 9 | Trip-home read-model convergence; retire standalone `home_cards` after folio soak | agent+app | −400 + future cost | **Med** | B |
| 10 | Typed `request<Path,Method>()` wrapper; retire `interface.ts`+`http.ts` ceremony opportunistically | app | −3–4k over time | **Med** | C |
| 11 | Hook-family folds + re-arm or delete `check_size_budgets.py` | agent | ~10 hooks, 2–4s/commit | Low | C |
| 12 | Docs-governance ceremony fold (6 scripts → 1; drop never-fired L4 + nudge) | ws | −1.5k LOC | Low | C |
| 13 | Atlas freeze made mechanical (delete tombstones + dead route helpers; exclude from polish campaigns) | app | −100 now; stops O(surface) bleed | Zero–low | D + A |
| 14 | Delete confirmed orphans (components, shims, dead scenarios, never-ran tooling) | all | −1.5k LOC | ~Zero | A |

Categories: **A** dead/residue · **B** duplicated/parallel · **C** over-abstracted/premature · **D** deliberately dark (product bet — posture decision, not deletion).

---

## Backend (travel-agent)

### 1. Multi-vendor LLM portability layer — KEEP (founder decision 2026-07-11); close the verification gap (D strategic)

- **What:** `backend/core/providers/` (1,571 LOC: `openai_adapter.py` 1,139, `anthropic_adapter.py` 249, `base.py` 180) + failover plumbing in `llm_client.py`/`llm_retry.py` + the provider dimension in `model_registry.py` + ~9 `provider=="openai"` branches through `llm.py`/`llm_sync.py`/`agent_loop.py`. Tests: ~3,230 LOC across 4 files.
- **Decision:** the original audit finding recommended deletion as dormant abstraction. **Overruled 2026-07-11 — vendor portability is a strategic capability** (provider resilience, pricing leverage, model-mix optionality). The finding is re-scoped to the real residual tax: the layer has **never made a real network call** — `LLM_FAILOVER_PROVIDER` is unset in `fly.toml` and every `.env*` (verified), so `_call_with_failover` (llm.py:161) short-circuits on every call. Unverified insurance is the worst posture: full carrying cost, zero proven payout.
- **State check (verified against 07-09 closure commits):** the debt-audit's catalogued bugs are **fixed** — failover mis-billing (`03351876` P2-6), refusal-signal erasure (`3f988e8d` P2-4), VCR coverage of OpenAI-routed calls (`54abffe7` P2-2), type-system integrity (`a3c8acfe` P2-7), plus two review-gap closes. The **only open item is P2-1** (zero real network calls) — explicitly blocked on live-spend authorization per the debt audit ("P1-4 and P2-1 need a live-spend authorization from a human").
- **Do instead of delete:**
  1. **P2-1 live verification** (founder-gated, ~an hour + trivial spend): provision Bedrock/Vertex creds + an OpenAI key, run one real completion + one streaming + one tool call through each adapter, record the VCR cassettes.
  2. **Wire the failover on:** set `LLM_FAILOVER_PROVIDER` in Fly secrets so the layer earns its keep — failover that isn't enabled protects nothing.
  3. **Anti-rot gate:** ensure the eval-replay/VCR lane exercises the adapter path on every CI run (P2-2's fix makes this possible) so the dormant-decay class can't recur silently.
- **Residual carrying cost (accepted):** ~5.5k LOC rides along in every future `llm.py` refactor. Acceptable for a strategic capability once it's verified; unacceptable only in the unverified state this finding closes.

### 2. Trip-home stack: 3 read models, 3 card types, 2 translators (B)

- **What:** (i) `home/feed.py` (1,224) per-trip `HomeFeed`, still served standalone at `GET /api/trips/{id}/home_cards`; (ii) `folio/read_model.py` (1,626, up from 1,383 — the growth watch stands) whose route *also* calls `assemble_home_feed` and embeds it; (iii) `home/concierge_feed.py` (3,217, 89 top-level defs) re-wrapping both via `_home_card_to_concierge_card` / `_durable_card_to_concierge_card`. Three wire models: `HomeCard`, `VesperCard`, `ConciergeHomeCard`.
- **FE reality:** trip-home uses `/folio` and falls back to `home_cards` **only on folio error** (`app/(tabs)/trips/[tripId]/index.tsx:82`).
- **Simpler:** (a) split `concierge_feed.py` into models/producers/ranking (mechanical, low risk); (b) converge on one wire card model so translators become constructors; (c) retire the standalone `home_cards` endpoint **after a dogfood soak** shows folio's internal degradation (`FOLIO_SOURCE_ERRORS`) makes the FE fallback redundant. The fallback is legitimately load-bearing *today* — this is a sequenced retirement, not a delete.

### 3. Card-family dual taxonomy — the flagged migration never happened (B)

`_resolve_legacy_family` + `_LEGACY_FAMILY_MAP` live at `concierge_feed.py:629–703`; the durable `vesper_cards` CHECK still enforces the legacy seven (`core/db/_tables/home.py:221-222`). Well-contained (~50 LOC) but every durable-card writer must speak the *old* vocabulary and every reader the new one. **Fix:** one Alembic migration rewriting stored families + CHECK to `{family, variant}`, then delete the map. ~1 day, low risk (pre-launch data, one table).

### 4. `get_tx` stalled at ~44% — a linter doing a type system's job (B)

229 manual `conn.commit()` sites remain (169 in `core/`; hottest: `core/db/content/_angles.py`, `trip_invites.py`, `entities.py`, `takes.py`). Whole subsystems (`research_agent`, `notifications`, `places`, `concierge`, `home`) have zero `get_tx`. The forgotten-commit → silent-rollback bug class is currently held off by `scripts/check_db_commit.py`. Error translation does **not** diverge (both paths use `core/db/errors.py` — good). **Fix:** finish the mechanical sweep (clustered in ~a dozen `core/db` files), then **delete the linter**. 1–2 days. Pure-read `get_connection` sites correctly stay.

### 5. Journey-certification triplication in scripts/ (B)

`dogfood_journey_live_api.py` (652) is a strict coverage subset of `dogfood_journey_persona_cert.py` (1,677) which already imports its client helper; `dogfood_journey_j04_chat_eval.py` (365) is a single-journey special case; the five-pack pair overlaps the persona-gate flow. CI is already keyed to persona_cert (`ci.yml:485`). **Fold under persona_cert: ~−1,200 LOC, low risk.** Note: the harness family's real historical problem was *divergence not duplication* (eval-replay validated a planning config prod didn't run — debt-audit P1-1, partially fixed `690ebdf3`); keep converging fixtures, don't merge eval-replay with persona-cert.

### 6. Notification scoring: ~6 independent scorers + a hand-wired producer ladder (B/C — partial)

Arbiter `ProactiveCandidate.score()`, learned Beta-Bernoulli `value_model.py`, channel `_PRIORITY_BY_URGENCY`, home tier/zone ranking (shared with home — good), digest distinctiveness, and deterministic bypass senders (`push.py:718`, `leave_by.py` 1,096 LOC) that skip the arbiter entirely. Producers are a manual try/except ladder (`concierge/proactive.py:1730–1760`); `ProactiveCandidate` constructed in 4 files. **Do now:** producer registry (~½ day). **Do NOT unify the scorers pre-launch** — the tuned tables encode product judgment and per-channel reasoning is actively used; document the bypass channels as deliberate (leave-by determinism is a product property).

### 7. Hand-rolled TTL caches beside the shared primitive (B) — narrower than estimated

`core/cache/ttl_cache.py` exists to kill this pattern (17 adopters); the audit flagged ≥10 hand-rolled stores as migration candidates. **Executed 2026-07-11 — only 2 of the ~8 non-pre-exempt candidates were actually safe drop-in migrations; the other 6 have real architectural reasons to diverge**, discovered by reading each site rather than pattern-matching on shape:

- **Migrated:** `user_signals.py` (clean TTL+LRU dict, `_UserSignals.received_at` field removed — TTLCache handles freshness internally; 2 tests reached into the old `_lock`/`_store`/`.received_at` internals and needed updating to the new `_cache`, both now green). `map_state/enrichment.py`'s `_NO_ROUTE_CACHE` (was a genuinely **unbounded** plain `dict` — the migration is a real bug fix, not just dedup; verified bounded at 4,096 via direct exercise since the file has zero existing test coverage).
- **NOT migrated — `user_modality_state.py`:** despite an identical LRU+lock+OrderedDict *shape* to `user_signals.py`, this store deliberately has **no TTL-based expiry at the storage layer at all** — it returns the raw last-modality timestamp unconditionally, and the caller (`modality_routing.py`) applies its own **modality-specific** decay (2 min voice / 5 min text stickiness) against that raw value. `TTLCache` enforces one uniform `ttl_s` and returns `None` past it — wrapping this store would silently start dropping entries the caller still needs to read. A pattern-matched migration here would have shipped a real bug.
- **NOT migrated — the remaining 6:** `location_context.py`'s reverse-geocode cache has the *same* dual-TTL shape as the already-exempted `idempotency.py` (24h positive / 5min negative — one `ttl_s` can't express two policies). `exchange_rates.py` has an explicit in-code note that it is deliberately "NOT a TTLCache" (stale entries are kept past TTL for a fallback path; TTLCache evicts on expiry). `tool_cache.py`'s `ToolResultCache` is instantiated fresh **per session**, not as a module-level singleton — architecturally a different pattern than TTLCache's shared-process-cache design. `pick_judgment.py` and `compose.py` share a documented two-tier L1(process)+L2(Redis) pattern with lazy-sweep-on-full eviction (not LRU) — migrating one without the other breaks the pair, and neither maps cleanly onto TTLCache's single-tier model. `db/trips.py`'s `_conflict_scan_cache` already uses the same underlying `register_cache`/cross-worker invalidation bus TTLCache wraps internally, via a hand-rolled `OrderedDict`, explicitly mirroring `home/feed.py`'s cache — migrating it means coordinating both files, which is Tier-2/Tier-3 work (also the subject of the `db/trips.py` god-module-split finding, finding 8), not a Tier-1 mechanical swap.

**Revised size/risk:** 2 files changed (not ~8), near-zero risk, one real bug fixed (unbounded cache → bounded). The other 6 are correctly load-bearing divergences, not remaining tech debt — do not revisit them without a reason beyond "shape looks similar."

### 8. God modules (mechanical splits)

- `core/db/trips.py` — **4,499 LOC, 94 functions, ~6 concerns** (trip CRUD, members, timezone+zoneinfo cache, group-profile versions, itinerary versions/days/blocks, move/conflict + haversine, event emission). Highest-churn god file (13 commits in 2 weeks). Split into `trips/{crud,members,itinerary,blocks,conflicts}.py` behind the existing import surface.
- `home/concierge_feed.py` 3,217 (finding 2) · `api/routes/atlas.py` 3,042 · `concierge/tools_schema.py` 2,602 · `folio/read_model.py` 1,626 and growing.

### 9. Seed-pipeline triplication + scripts sprawl (B/A)

Three pipelines: `tools/dogfood/content/seed.py` (2,612, canonical), `tools/seed/` (3,074, with a duplicate `schemas.py` role), ~10 `scripts/seed_*.py` one-offs, plus `tools/seed/_archive/` (2,753 LOC already-dead batch scripts). 154 scripts / 40k LOC total. Declare the dogfood pipeline canonical; verify `tools/seed`'s staging→promote isn't still used for content ops (git-log pass), then fold or archive.

### 10. Small confirmed dead weight (A)

- `core/personas.py` — 16-line re-export shim for `guide_voices.py`. **Executed 2026-07-11:** deleted; 13 consumers (not 8 — included production `backend/guide/prompts.py` and several `mock.patch()` string targets that were silently patching a stale binding the actual routes no longer read, since routes already import `get_persona_for_trip` from `guide_voices` directly) repointed to `guide_voices`; 166 affected tests green.
- ~~The `default` persona: … Repoint at `elif`/`nadia`, delete.~~ **Reversed on execution (2026-07-11):** the "no mock bundle on disk" premise was wrong. `default` is `DEFAULT_PERSONA` in `travel-app/constants/personas/index.ts` — the FE's deliberate no-op baseline, documented in-code as "the app renders exactly as it did before the persona system existed." M0/M13/M14 specifically test that baseline; repointing them to a named persona would misrepresent what they validate. Cut 3 correctly left it alone. Only the stale scenarios.yaml comment (which claimed it was "pending delete") was fixed.
- `api/routes/chat.py` (627) — self-described legacy (`api/FEATURE.md:128`); FE calls only `/messages/history` + `/side-chat` (`travel-app/utils/api/http.ts:956,1882`). ~4 of 6 endpoints look FE-orphaned — verify, then prune.
- Composition `variant=="discover"` branches — 6 sites in `composition/{core,quality_gate}.py` unreachable since Discover Compose deletion 07-03 (`5784ff9f`).

### Dark-subsystem posture (D — freeze-cost ranking, not deletions)

Cheapest→hardest to freeze: **postcards** (294 LOC, one lazy import, already effectively frozen) → **voice** (1,719 + 3,521 test, credential-gated, isolated — clean freeze) → **venue-disruption** (~210 core, flag-gated) → **booking live leaf** (flag gates only Duffel create/confirm/cancel; the other ~7.5k booking LOC is live and co-evolving — do not extract) → **story-share** (~1,100; DB layer shared with live story compose). **Outlier: ambient near-you (`situation/nearby.py`, 630) has no flag at all** — dark only because the GPS push never fires, yet it imports and executes on every home-feed/situation render before early-returning. If any dark subsystem deserves an explicit flag or hot-path extraction, it's this one.

---

## Frontend (travel-app)

### 1. The mock/persona world: ~34k hand-maintained lines mirroring a 7-identity backend (B/C, some A)

- **What:** `constants/personas/` — 16 registered bundles (10,753 LOC) + 5 `.generated.json` seed snapshots (9,572 lines, **zero code consumers** — referenced only in "kept in sync by hand" comments, verified); `constants/mocks/` (2,680); `utils/api/mock/` (10,728; `mock/atlas.ts` 2,910, `mock/trips.ts` 2,503). ≈ 34k lines, ~12% of non-generated app code.
- **Why it's a tax:** seed → JSON → hand-mirrored TS is double bookkeeping; 16 FE personas vs the 7 canonical backend identities (see reconciliation below); `ana` (stale since 06-17) and `ready` (06-29) are dead; `torture/between/urgent/ready` only force cascade states that `app/dev/force-state.tsx` already forces; every backend schema change fans out through mock API + up to 16 bundles; `EXPO_PUBLIC_USE_MOCK_API` now defaults **false**, so the mock world's justification shrinks as dogfood starts.
- **Simpler:** keep the 7 canonical seed-backed personas; replace state-matrix personas with `dev/force-state`; delete `ana`/`ready`/dead bundles; stop committing the generated JSONs (regen on demand); **generate persona fixtures from the seed JSONs at build time** instead of hand-mirroring.
- **Size/risk:** −12–15k lines now; **medium** — Maestro persona walkthroughs (40/44/45/46) and 42 persona-referencing Jest files pin mara/dao/reza/elif only. **Lost:** offline demo variety; the hand-tuned narrative polish in e.g. `elif.ts` (1,401 lines).

### 2. Atlas: ~38k lines / 36 routes still absorbing every consistency campaign while the freeze decision stays open (D + A)

- **Measure:** `app/atlas` + `(tabs)/atlas` 36 files / 14,307 LOC; `components/atlas` 30 / 9,714; utils 1,495; `data/atlas.ts` 1,654; mock 2,910; tests 7,166. 9 screens flag/redirect-gated; `almanac`/`following`/`map`/`timeline` are already 8–26-line tombstone redirects.
- **Why it's a tax:** Atlas is not frozen *in practice* — `voice-logs.tsx` touched 07-10, `AtlasTasteBoard.tsx` (2,854, #2 largest component) merged batches 07-06, and the CC/spinner campaigns swept Atlas files this week. Ratchets and design campaigns pay O(surface), and Atlas is ~30% of the surface while ~35–45% off the group-trip wedge.
- **Simpler (makes the freeze mechanical, independent of the product decision):** (a) delete the 4 tombstone routes + the 0-usage `routes.ts` helpers (`atlasMap`, `atlasAlmanac`, `atlasTimeline`, `atlasFollowing`, `constraints`, `storyArchive`, `tripLog`, `privacyAudit`, `personalUpdates`); (b) add an exclusion list so budget ratchets / CC campaigns skip `app/atlas` + `components/atlas`. Freeze must mean "stop spending polish cycles here," not just "no new features." Actual Atlas deletion remains the open product decision — out of scope here.

### 3. QA-lane proliferation: ~10 harnesses, ~15k tooling LOC, ~54 npm scripts, CI tests the test tools (B/C)

Jest (372 files / 60.6k) · Maestro (115 YAMLs + 480MB untracked runs) · `scripts/polish-qa` (41 files / 6,728) · `scripts/design-alignment` (23 / 4,749) · `scripts/design-qa` (1,002 — overlaps both) · `scripts/logic-qa` (boots the Python backend in CI; run-mode frozen since 06-28) · `mobile-stability` (972, dormant) · `parity-contracts` (dormant since 07-01) · 12 budget ratchets · doc checks. Three separate screenshot-vs-reference systems with three vocabularies. `qa:polish:test` runs a **13-part meta-test suite of the QA tooling itself**. **Fold:** `design-qa` → `polish-qa`; `design-alignment` stays the single canon lane; retire logic-qa run mode + its 16 committed run dirs (**keep `qa:logic:check-drift`** — live in `certify-fast` and workspace CI); parameterize the per-surface npm aliases (~54 → ~15). −2–3k LOC of tooling, dev-only risk.

### 4. API layer quadruple bookkeeping per endpoint (C)

One endpoint touches: `schema.gen.ts` (auto — fine, CI-verified fresh; the hand-bridge era is confirmed over) → `types.ts` (1,971 hand aliases) → `interface.ts` (2,027, every method declared) → `http.ts` (2,901, hand fetch impls) → `mock/*` (10,728) → possibly persona fixtures. ~17.6k hand lines shadowing types the generated schema already encodes. **Simpler:** a typed `request<Path, Method>()` wrapper over `paths`; keep named methods only where FE-side massaging exists; mock intercepts at the wrapper. **Migrate opportunistically, not big-bang.** Medium risk: the `useData` bridge and `setRuntimeMockMode` live-binding (documented in `utils/api/index.ts`) must keep working. Lost: one grep-able named method per endpoint; some per-endpoint fallback docs are genuinely load-bearing (e.g. `_EMPTY_EXPENSES` rationale).

### 5. Orphans kept alive — and actively polished — by their own tests (A)

**`components/focus-home/DeckCompareFace.tsx` (266L): zero renders anywhere** (`Deck.tsx` has no 'compare' case), yet it received 3 CC-batch commits on 07-09/07-10 — the consistency campaigns are polishing dead code. Confirm it isn't next week's feature, then delete. Also: `AtlasRoomArt.tsx` (27), `AtlasYearStepper.tsx` (86), `memory/DNAStrip.tsx` (103), `StoryArchiveCard.tsx` (130), `TripLogCard.tsx` (146 — matches the dead `routes.tripLog` helper), `discover/…VerdictChip.tsx` (69). (`MicStatusIndicator.tsx` is voice-dark → category D, keep.) ~1,100 LOC + ~8 test files, near-zero risk.

### 6. The folio cluster is one 5.4k-line organism at 91% of its own budget (C)

`TripFolioHome.tsx` 2,905 (budget 3,200) + `tripFolioStyles.ts` 1,325 (split to satisfy the ratchet, not along seams) + `FolioReceiptCard.tsx` 750 + `TripFolioPostTrip.tsx` 443. A folio redesign is queued ("COMPLETE not built") — churn is incoming into the worst file to churn. **Don't split preemptively; split along trip-state seams (pre/live/post — `TripFolioPostTrip` proves the seam) when the redesign lands, with co-located styles.** Peers to watch: `plan.tsx` 1,887, `DiscoverCoverHome.tsx` 1,929, `AtlasTasteBoard.tsx` 2,854, `useConciergeChat.ts` 1,481.

### 7. Repo hygiene (A, trivial)

~150 untracked QA screenshots at repo root; `.maestro/runs` = 480MB local; ~17 orphaned Maestro flows (26–33, 40–46) referenced by no npm script or runner. Point capture output at a gitignored `artifacts/`; `.gitignore` root `*.png` + `.maestro/runs`.

### Verified non-findings (leads that are now healthy — no action)

`schema.gen.ts` regenerates cleanly (CI `generate-api-types:check`); query-key registry has only 3 inline-key bypasses repo-wide; the state-system migration is complete (35 remaining `ActivityIndicator`s enumerated + justified in the ratchet header); the card system has no dual-path rendering (9 faces + 5 Deck faces = the deliberate two-fidelity split; `TimelineObjectRow` is wired at `TripFolioHome.tsx:2737`); `DiscoverSearchOverlay` already deleted; design ratchets are live, not no-ops (spinner 58→42→41 with dated rationale).

---

## Workspace / coordination layer

### 1. Completed-campaign residue: ~30% of the Makefile, ~45% of scripts/ (A)

20 of 70 Make targets + ~22 of 57 scripts belong to the dogfood/corpus campaign that finished 2026-06-29 (STATUS.md marks every lane PASSED/COMPLETE; every script's last git touch is 06-28/29). **Fix:** `include dogfood.mk` + `scripts/attic/`. Keep the reusable city machinery in the main file (`dogfood-city`, `dogfood-promote`, `corpus-check`, `dogfood-env-check`, `dogfood-status`, `dogfood-status-sync`).

### 2. Five overlapping "is journey J green?" oracles → 2 (B)

Canonical: generated `docs/journeys/STATUS.md` (from `journeys.yaml` SSOT + `sync_journey_status.py` + set-drift guard — the *good* pattern, shipped 06-30/07-01). Complementary: FE Jest mock-walks (20 files, active 07-08). Stale: logic-qa run mode (frozen 06-28, 16 committed run dirs), hand-written `visual-certification-matrix.md` (stale 06-28), parity-contracts (dormant 07-01). Retire the stale three; **keep `qa:logic:check-drift`** (live in `certify-fast` Makefile:116 and `reliability.yml:134` — the only thing keeping `scenarios.mjs` honest against backend test files); fold the visual matrix into STATUS.md's generated Visual column.

### 3. QA-ladder aliases: 5 Make ladders → 1 + the certify tier (B)

`offline-qa` / `verify` / `certify-fast` / `mock-real-parity` (strict subset) / `pre-launch` are near-identical compositions that drift independently. **Taxonomy:** `make verify` = the one pre-push cross-repo gate (absorb offline-qa; delete mock-real-parity; pre-launch → verify+smoke) · `make certify-*` = the tiered journey ladder (keep; delete the `golden-path-qa` deprecated alias) · `sync-*`/`docs-*`/dev unchanged. Result: 70 → ~40 targets with finding 1. Half a day; leave one-line `@echo moved` stubs for a month.

### 4. Hook layer: fold 3 families, fix or delete 1 toothless ratchet (C)

40 backend hooks (23 commit / 17 pre-push) vs the config header's own claim of "~17/8" — the tiering note drifted from the tiering it documents. Folds: 3 `status-*` checks (one 06-25 audit split three ways, same parser, 3 AST walks) → 1; 2 timeout checks → 1; 6 doc-guard scripts → 1 (see 5). vulture has no `files:` gate so it runs on every commit. **`check_size_budgets.py` is ceremony:** function ceiling raised to exactly 956 on 07-11 to match its largest offender; all 3 exempted files grew 40–60% past their exemption notes (`trips.py` 4,499 vs noted 2,845); not in CI. Re-arm (freeze exemptions at current size) or delete. **CI-floor gap:** 6 checks exist only as local hooks — one `--no-verify` push escapes them forever; add to CI or accept as advisory.

### 5. Docs governance: keep the spine, fold the ceremony (C, partially D)

8 workspace scripts / 2,404 LOC (incl. 172 LOC of tests *for the doc police*) + 8 hooks + 9 targets, all shipped 07-09/10. **Load-bearing (fired recently):** flag registry (07-11 "register ad-hoc backend flags" commit), `check_docs_symbols` L3 (caught real drift at introduction), inventory admission gate, `render_current_state` (replaced prose scorecards — genuinely good). **Never fired since creation:** L4 `check_feature_coverage`, warn-only `docs-drift-nudge`. Fold the 6 workspace doc scripts into one `check_docs.py --all`; drop L4 + the nudge + `check_child_doc_governance` + the tooling self-tests. *Caveat:* this layer is 2 days old — an equally defensible posture is to wait 30 days and delete whichever sub-checks still have zero catches.

### 6. Design folder: active loop healthy; residue is heavy (A + D)

**Keep:** `surface-manifest.yaml` (38 surfaces, updated 07-11) + `canon-drift-check.py` + the gitignored `vesper-canon-anchor/` mirror + the FE design-alignment loop (STATUS regenerated 07-11 — the one FE QA system that ran this week). **Residue:** 66 dated adjudication/code-alignment briefs (campaigns A→J1/CC1-4 shipped) → `design/archive/2026-07/`; **462 files (~135MB+) of superseded design-direction bundles are git-tracked** (`vesper-home-claude-design` 39M, `vesper-cards` 39M, `vesper-discover-fetched` 30M, `vesper-discover` 14M, `trips-full-anthropic` 13M, `atlas-direction-03` 2.4M) while the actual canon mirror is correctly ignored — this is most of the workspace pack. `git rm --cached` + gitignore (files stay on disk). Also removable: `design/serve.py`, 3 `font-*.html` experiments (typeface decision settled).

### 7. Never-ran machinery (A)

`daily-digest/` + `.routines/daily-digest.md` + `scripts/digest-inputs.sh` — LATEST.md still says "first real entry appears after the routine's first successful run"; untouched since **2026-05-11**. `scripts/ci-review.sh` (same era). `scripts/new-branch.sh` (superseded by the active worktree lane). The stale launch-cwd checkout at `~/Documents/Claude/travel-workspace/` has a dangling symlink + a May-26 orphan `travel-app/` copy — clean to just the two working symlinks.

### Keep as-is (looks expensive, is correct)

- **openapi.json snapshot flow:** 113/249 workspace commits touch it, but diffs are small, cadence is *declining* (50→41→22/month), generation is offline-deterministic, and the layered verification (backend byte-compare → CI freshness regen → contract-check ↔ `schema.gen.ts`) is exactly why the 05-19 drift class never recurred. The churn is the SSOT *working*.
- **Three-repo + workspace structure**, `child-repos.ci-lock.json`, `repository_dispatch`, worktree lanes — clean solution to cross-repo testing without a monorepo.

---

## Reconciliations & reversed leads

Findings where this audit **corrects earlier notes** (including this workspace's own memory):

1. **Angles engine is NOT deletable.** The ~1.2k dead browse stack was already deleted 06-17 (`c06c0b85`, −1,303). The surviving 2,009 LOC is the *input queue* to the dossier pipeline (`research_agent/agents/persist.py:345` links dossier→angle); the 2,132 `dossier_id IS NULL` rows are unwritten backlog, not orphans. Only a product decision to freeze index growth would make the ~845-LOC generation side retirable.
2. **Persona "Cut 3" was cancelled on the backend, not forgotten** — the audit found the pending-delete personas load-bearing and re-homed them (`tools/dogfood/content/identities.py:34–63`); the canonical cast is now **7** (nadia added 07-10). What remains is: (a) the backend `default` remnant (above), and (b) the **FE-side** collapse of 16 bundles → the 7 canonical identities, which is still open and is FE finding #1.
3. **`folio/read_model.py` watch confirmed:** 1,383 → 1,626 and growing.
4. **schema.gen.ts hand-bridge era is over** — regen is clean and CI-verified.
5. **The FE state-system migration is complete, not partial** — remaining spinners are enumerated and justified in the ratchet header.

---

## Consolidated Do-NOT-touch list

| Item | Why it stays |
|---|---|
| OpenAPI snapshot flow + `sync-types` + `contract-check` + `api-coverage` | The contract spine; prevented recurrence of the 05-19 drift class |
| `eval-regression` pre-push (43 baselines) | Primary prompt-safety gate |
| `journeys.yaml` SSOT + registry guard + generated STATUS.md | The already-consolidated pattern everything else should converge on |
| Flag registry + `check_flag_registry.py` | Fired 07-11; keeps 35 flags from rotting |
| Secret guards; IDOR/route-auth/async-db/broad-exception AST ratchets | Security floor (fold the *packaging*, keep the checks) |
| `check_get_tx_ratchet` | Live ratchet — worked 344→224 through 07-09 (delete only when finding B-4 completes) |
| `surface-manifest.yaml` + `canon-drift-check.py` + canon mirror + design-alignment loop | The active canon mechanism; ran 07-11 |
| `utils/routes.ts` typed route registry | It's why orphan detection is even possible |
| `useData` mock bridge + `setRuntimeMockMode` live-binding | Powers the dogfood-build persona toggle |
| Budget-ratchet scripts + prose headers | Institutional memory of a solo+AI repo; all actively lowered |
| `home/feed.py` producers consumed by `concierge_feed` | Reuse, not duplication |
| `discover/compose.py` | Different file from the deleted `compose_board.py`; serves live `/api/discover/feed` |
| `value_model.py` / holdout / incrementality | Built-dark measurement lever (`holdout_fraction=0.0`) — deliberate |
| Booking agent bulk; eval-replay and persona-cert as *separate* harnesses | Complementary by design; converge fixtures, not harnesses |
| `llm_vcr.py` | Shared replay substrate under both harnesses |
| Multi-vendor LLM layer (`core/providers/`, failover, provider registry dimension) | **Founder decision 2026-07-11: strategic keep** — close P2-1 verification instead (backend finding 1) |
| Card/deck two-fidelity split; `data/` vs `hooks/` layering | Documented, conventioned seams that only look like duplication |
| 3-repo + workspace structure; worktree lanes | Correct cross-repo architecture |

---

## Suggested sequencing

**Tier 0 — hours, ~zero risk (do any time):**
`git rm --cached` the design bundles (−135MB) · delete Atlas tombstone routes + 9 dead route helpers · delete the 7 orphaned FE components (+tests) · delete `core/personas.py` shim + repoint the `default` persona scenarios · delete daily-digest / ci-review.sh / new-branch.sh · gitignore QA artifacts + `.maestro/runs` · archive the 66 design briefs · fix the stale launch-cwd checkout.

**Tier 1 — a day each, low risk:**
Card-family DB migration (delete the bridge) · `dogfood.mk` split + scripts attic · retire the 3 stale journey oracles · fold hook families + re-arm-or-delete `check_size_budgets` · TTL-cache adoption sweep (skip the 2 exempt) · notification producer registry.

**Tier 2 — 1–3 days each, low→medium risk:**
Finish `get_tx` + delete `check_db_commit.py` · fold journey-cert scripts under persona_cert · Makefile taxonomy 70→~40 · FE persona Cut-3 (16→7, stop committing JSONs, fixtures generated from seeds) · fold design-qa into polish-qa + npm script diet · split `core/db/trips.py` and `concierge_feed.py` · docs-governance fold (or the 30-day-wait variant).

**Tier 3 — sequenced behind product decisions / dogfood evidence / founder-gated steps:**
Multi-vendor P2-1 live verification + wire `LLM_FAILOVER_PROVIDER` in Fly secrets (needs founder cloud creds + live-spend authorization) ·
Retire standalone `home_cards` endpoint after a folio soak (needs FE change) · converge on one wire card model · typed `request<>` wrapper migration (opportunistic) · **Atlas freeze decision** (until decided: campaign-exclude Atlas so polish cycles stop flowing there) · prune legacy `chat.py` endpoints after FE-call verification · folio split along trip-state seams *when the redesign lands* · ambient near-you: add a flag or extract from the hot path.

**What this buys, roughly:** −20–25k hand-maintained LOC, three dual-idiom states collapsed to one each, ~10 fewer hooks (~2–4s/commit), 70→40 Make targets, −135MB git payload, and — the real prize — every future schema/card/LLM change stops fanning out across parallel implementations that exist only for historical reasons.
