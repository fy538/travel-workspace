# Content Contracts — Fix-Now Implementation (applied)

**Date:** 2026-07-08 · **Repo touched:** `travel-agent` only (all six items landed backend-side; the one FE piece is flagged below). **Grounded in:** [content-contracts-audit.md](content-contracts-audit.md) + [content-contracts-open-questions.md](content-contracts-open-questions.md).

**Version control:** working-tree only, per the session decision — no commits/branches (travel-agent `main` carried a concurrent session's uncommitted WIP in `planning_agent/schemas.py`, `agent.py`, `agent_loop.py`; committing per-item would have swept that foreign WIP in). All changes are staged in the working tree for review.

**Test status:** all new tests pass — 32 backend + 11 frontend. The item-1 migration has been applied to the local DB, so item 1 is green. `ruff check` clean on every touched backend file; `tsc --noEmit` clean (0 errors) on the frontend. No shared held-back primitive was improvised — see the note at the end.

Quick map of new tests:

| Item | Test file | Result |
|---|---|---|
| 1 | `tests/core/test_itinerary_persistence.py::...test_planner_price_persists_as_estimate` | ✅ (migration applied) |
| 2 | `tests/atlas/test_atlas_budgets_and_counts.py` (6) · `tests/api/test_atlas_one_line_read.py` (3) · FE `__tests__/screens/atlas-artifact.smoke.test.tsx` (9, incl. "EDITED BY YOU" + edit flow) | ✅ |
| 3 | `tests/takes/test_place_fact_rules.py` (3) | ✅ |
| 4 | `tests/api/test_expenses_api.py::TestCreateExpenseFromReceipt` (8) | ✅ |
| 5 | `tests/digest/test_weather_join.py` (6) | ✅ |
| 6 | `tests/test_prompt_hardening.py` (5) | ✅ |

**Update (this session):** the two previously-outstanding actions are now done — the item-1 migration was applied to the local DB (`localhost/vesper`, user-authorized), and the item-2b **frontend** edit affordance was built (see item 2b). The `travel-app` changes were made on its current `design-align/costs` branch (working tree only, no commit), per the same working-tree-only decision.

---

## 1 — Planner price: stop labeling a model estimate as a quoted price (R12 / O9) · **option A**

**Option chosen: A** (mark as estimate) — confirmed by user.

The block price column is overloaded: the planner writes a *model estimate*, a settled hold writes a *real provider price* (`booking_agent/holds.py:212`). Added a discriminator so they can never be conflated, and corrected the false "actual quoted pricing" comment.

Files touched:
- `backend/core/db/_tables/itinerary.py:188` — new `Column("price_is_estimated", Boolean)` (nullable) beside `price_cents`, with a comment documenting the overload.
- `alembic/versions/pxprice_est01_itinerary_blocks_price_is_estimated.py` — **new migration** adding the column (nullable, no backfill, reversible).
- `backend/core/models/planning.py:120` — `price_is_estimated: bool | None` on `ItineraryBlock`.
- `backend/core/db/trips.py:1594` (`create_block` param) · `:1643` (INSERT value) · `:1849` (`update_block` allowed set).
- `backend/core/db/itinerary_persistence.py:203` — planner persist sets `price_is_estimated=True` when a price is present (else `None`).
- `backend/booking_agent/holds.py:213` — settled hold sets `price_is_estimated=False` (real quote).
- `backend/core/db/trips.py:3094` — corrected `_block_cost_cents` comment: the value is usually a planner estimate, the budget total is a *projected* spend, and any UI must label it as an estimate (not a confirmed cost).

Test: `test_planner_price_persists_as_estimate` — persists a slot with a price → asserts `price_cents=4500, price_is_estimated=True`; a no-price slot → both `None`.

> ✅ **Migration applied.** `alembic upgrade head` was run against the confirmed-local DB (`localhost/vesper`) after user authorization — revision `pxprice_est01` is now head, the column exists, and both the new test and the previously-breaking block-insert tests pass. **Prod still needs the deploy migration to run** (standard release step). Note: one unrelated pre-existing test, `tests/core/test_trips.py::test_full_lifecycle`, fails on itinerary *version* numbering — confirmed **not mine** (reproduces identically with my `trips.py` change stashed; it's a concurrent-WIP / DB-state issue in a code path I never touched).
>
> **Product decision:** the FE does not currently render block `price_cents` anywhere (confirmed by grep), so no "est." label was added to the app. When a block price *is* surfaced in future, it must read `price_is_estimated` and show an "est." qualifier. The Duffel/provider price path was left untouched, as instructed.

---

## 2 — Atlas prose: live-in-prod defects (R11 / O8)

The honesty badge (`artifact/[id].tsx:164`, gates on `composed_by === 'llm'`) was left alone, as instructed. Three sub-fixes:

**2a — budget mismatches → single number per field + word-boundary trim.**
- `backend/atlas/timeline_generator.py` — added `_TITLE_MAX=80 / _BODY_MAX=160` (matching the prompt's stated "Title max 80 / Body max 160"), replaced every `[:120]`/`[:240]` raw slice (mock + LLM paths) with `clamp_text` (word-boundary).
- `backend/atlas/almanac_generator.py` — added `_TITLE_MAX=40 / _MONTH_BODY_MAX=120 / _YEAR_BODY_MAX=160`, replaced `[:120]`/`[:500]` slices with `clamp_text`. These now match the prompt **and** the canonical validator (`atlas/almanac_checks.py` `_*_BODY_MAX`) exactly — previously the code sliced year bodies to 500 while the validator max is 160, so this also removes a real generator-vs-validator mismatch.

**2c — no count-minting in prose.**
- `backend/atlas/prompts.py` — `ALMANAC_MONTH_SUMMARY_SYSTEM` / `ALMANAC_YEAR_SUMMARY_SYSTEM`: added "Do NOT state counts or numbers … write the feeling, not a tally." `HOME_LETTER_SYSTEM`: added a hard rule "Do NOT tally …", and softened the anniversary line from "(place + how long ago)" to "name the place and the occasion (do not compute … years)". (The mock `_mock_year_summary` still renders `len(entries)` — that's a count *from data*, which the contract permits; left as-is.)

**2b — `one_line_read` owner-editable (backend + frontend both delivered).**

Backend:
- `backend/core/db/atlas.py:410` — new `update_artifact_one_line_read(...)` + `async_update_artifact_one_line_read(...)`: ownership-scoped UPDATE, word-boundary clamp (`_ONE_LINE_READ_MAX=120`), flips `composed_by` to `"user"`, re-syncs the Atlas search vector.
- `backend/api/routes/atlas.py:513` — new `PATCH /api/atlas/artifacts/{artifact_id}/one-line-read` (`UpdateOneLineReadRequest` requires non-empty; 404 for non-owner).

Frontend (`travel-app`, on its `design-align/costs` branch, working tree only):
- `utils/api/interface.ts` · `utils/api/http.ts` · `utils/api/mock/atlas.ts` — new `editAtlasArtifactOneLineRead(id, oneLineRead)` API method (real PATCH + mock that updates the mock store and returns `composed_by:'user'`).
- `data/atlas.ts` — new `useEditArtifactOneLineRead()` hook (mirrors `useDeleteArtifact`; invalidates the specific artifact query + the Atlas read models so the shelf/home refresh).
- `app/atlas/artifact/[id].tsx` — an **"Edit"** affordance on the one-line-read row opens a modal (`TextInput`, 120-char cap, Save/Cancel); saving calls the hook and refetches. Added the **"EDITED BY YOU"** badge state so a user-edited read (`composed_by === 'user'`) is framed honestly — not "VESPER WROTE", not "DRAFT" — consistent with trip-story sections.

Tests: `test_atlas_budgets_and_counts.py` (budgets/clamp/no-tally); `test_atlas_one_line_read.py` (BE route: `composed_by='user'`; 404 non-owner; 422 empty); FE `atlas-artifact.smoke.test.tsx` (renders "EDITED BY YOU" for `composed_by:'user'`; the Edit affordance calls `save(id, text)`). Also closed a **pre-existing** incomplete mock in `journey-11-mock-walk.smoke.test.tsx` (it was already failing on `useArtifactPhotoPermanence`; added that + the new hook so it's green).

---

## 3 — Place-fact no-invent rule in `shared.py` (O5, dents R8/R10)

- `backend/core/prompts/takes/shared.py:191` — new `PLACE_FACT_RULES` block: operational facts (hours, prices, availability, "open now"/"closed Mondays", booking status, dish/menu names) must come only from provided structured data; when unsure, generalize ("a long-running local spot", not "open till 2am"); never invent a business/dish/neighborhood name.
- Interpolated into **both** `curator_prompt.py:24` (`CURATOR_SYSTEM`, which previously imported no grounding block at all) and `personal_prompt.py:27` (`PERSONAL_SYSTEM`).

Test: `test_place_fact_rules.py` — the rule is defined and specific, and present in both composed prompts.

> Note (from O5): `GROUNDING_RULES` covers only *user* claims, so this fills the missing *place-fact* rule for the curator **and** personal takes.

---

## 4 — Receipt `amount` required at the API contract (R1 residual)

- `backend/api/routes/expenses.py:91` — `amount: float = Field(..., gt=0)` on `CreateExpenseFromReceiptRequest` (was `float | None = None`). Rejects null/absent/≤0 with 422 before the handler runs.
- `backend/api/routes/expenses.py:938` — removed the `… else ocr.get("total_amount")` fallback; `amount = body.amount`. OCR output stays a client-side pre-fill suggestion and can never be the persisted value. Removed the now-dead `if amount is None` guard.
- `tests/api/test_expenses_api.py:1109` — `_create_from_receipt_body()` now sends an explicit amount; repurposed the old "no amount → 400" test into `test_missing_amount_is_rejected_and_ocr_total_never_persisted` (422 + `async_create_expense` never called) and added `test_nonpositive_amount_is_rejected` (null/0/−5 → 422).

---

## 5 — Digest weather: join a real source (O7) · **option A**

**Option chosen: A** (join open-meteo) — confirmed by user.

- `backend/digest/engine/weather.py` — **new**: `fetch_day_weather(lat, lon, date)` (open-meteo forecast, 4 s timeout, best-effort → `None` on any failure, mirroring the planner's provider posture) + `first_block_coords(blocks)` to anchor the lookup to where the day happened.
- `backend/digest/engine/llm_calls.py:39` — `_call_daily_digest` derives coords from the day's blocks, fetches weather for `inputs.date`, and injects a `### Weather (observed)` section (empty when no coords / provider miss). Fetched at call time, so it doesn't perturb the digest input-hash / cache key.
- `backend/digest/prompts.py` — `context_notes` now says "Include weather ONLY if a Weather section is present … never infer or invent it"; added a `{weather_section}` slot to the user template and a hard rule to the system prompt ("state weather ONLY when a 'Weather (observed)' section is present … never infer it from the season, location, or mood").

Test: `test_weather_join.py` — prompt solicits weather only from provided data; coord extraction; best-effort `None` on provider error; weather injected into the rendered prompt when coords exist; omitted (and not fetched) when they don't.

> **Note / possible follow-up:** open-meteo's forecast endpoint covers recent dates well; a long-past trip day may fall outside its window and simply yield no weather section (honest degradation). If data-backed weather for older trips matters, switch `fetch_day_weather` to the open-meteo **archive** API for past dates. Coordinates come from the day's block `lat/lng`; days whose blocks lack coords get no weather (also honest). The OCR `expense_date` (a separate O-list residual) was left as-is — out of scope for item 5.

---

## 6 — Prompt hardening: kill fact-shaped exemplars (R2 / R3)

- `backend/tasks/trip_story.py` — replaced the `hero_subtitle` exemplar "Three days, four restaurants, one regret" with "Long lunches, and the city in between", and added a rule: the subtitle is not a tally; no counts/dates/prices/place-names unless they appear in the arc/observations.
- `backend/home/prompts.py` — softened the anchor few-shots ("Two dinners"→"A few dinners", "Three travelers"→"A few travelers", "14 photos"→"Your photos"), and changed the rule from "Cite … counts. Do not generalize" to "Cite specifics ONLY when present in the data … otherwise generalize."
- `backend/concierge/refresh_memory.py` — DNA prompt: reversed "No hedging words" into "Hedge when the signal is thin", softened the "always finds …" exemplar, added "Never invent a detail the narrative doesn't contain."
- `backend/booking_agent/agents/prompts.py` — `PARSE_TRANSCRIPT_SYSTEM`: added "if not explicitly stated, return null — do not estimate/infer/guess; never invent a confirmation number or confirmed time", and "`was_successful` true only on explicit confirmation".
- `backend/expenses/receipt_ocr.py` — added "if a value is not explicitly legible, omit it — do NOT estimate/round/guess … a guessed number is worse than a missing one."

Test: `test_prompt_hardening.py` — the count-minting exemplars are gone, the anti-hedging rule is gone, and the null-if-unstated rules are present in the transcript + OCR prompts.

---

## Held-back-primitive check

No item required improvising one of the deferred shared primitives (facts-only `call_llm` wrapper, confidence component, fallback resolver, public-projection verifier). Item 2a/2b reused the **existing** `content_contract.clamp_text` helper (a length primitive that already ships), which is not one of the held-back items. Everything else is a local prompt/model/route change.

## Outstanding actions for the reviewer

1. **Run the migration in prod** at deploy — `pxprice_est01` (add `itinerary_blocks.price_is_estimated`). Applied locally; standard release step for prod.
2. **Review the two branches / working trees before committing** — `travel-agent` changes sit alongside a concurrent session's WIP on `main`; `travel-app` changes sit on `design-align/costs`. Decide how to split into commits/PRs (I left everything uncommitted per the working-tree-only decision). The item-2b FE landed on `design-align/costs` for convenience — you may want to move it to its own branch.
3. Optional / noted: point any future block-price UI at `price_is_estimated`; consider open-meteo's **archive** API for weather on long-past digest days; revisit the OCR `expense_date` residual (item 4 covered `amount` only); the pre-existing `test_full_lifecycle` failure (itinerary versioning) is unrelated to this work but worth a look.
