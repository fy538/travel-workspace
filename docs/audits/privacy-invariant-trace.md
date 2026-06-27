# Privacy-Invariant Trace — Consolidated Audit

> **RESOLVED 2026-06-27 (verified against HEAD `f698d228`).** All TIER 1/2/3 fixes
> and clusters A–F/H below landed in main via commit `5c46a47b`
> (*feat(privacy+group+core): egress guard, group profile, compose privacy fixes*).
> Spot-verified in code: `check_proposal_privacy(alternative_options=...)`
> (`backend/concierge/privacy_redactor.py:86,118`); `resolution_note` redacted at the
> resolve choke point (`backend/core/db/change_proposals.py:658-665`); `new_time` now in
> `_IMPACT_TEXT_FIELDS` (`privacy_redactor.py:77`); `strip_private_group_sections`
> exists and is wired (`backend/core/group_profile.py:33`); digest path strips group
> profile + corpus-scrubs (`backend/digest/engine/daily.py:81-83,159-164`); `_shapes.py`
> group-card guard (`_shapes.py:188-200`); Atlas Unpacked DNA filter
> (`backend/atlas/unpacked.py:128`); Discover hook scan (`backend/discover/compose.py:508-509`);
> planning telemetry uses `safe_event_context` (`planning_agent/agent.py:262`).
> Cluster G (booking writeback) remains product-gated/operator-only by design. The
> "Coverage gaps still open" footer (notifications/SMS/email, Discover personalization,
> Atlas share artifacts, logs/telemetry) is still unverified — not cleared. Findings below
> are kept as the historical record.

**Runs:** 2026-06-24 (proposal subsystem, 21 surfaces) + 2026-06-25 (full sweep, 114 surfaces)
**Method:** static egress tracing → adversarial verify → human spot-check (this doc)
**Caveat:** both runs hit heavy *server-side* rate limiting (not usage limit). Many trace/verify
agents returned null, so coverage is **partial** and several skeptic passes never ran. Findings below
are tiered by how much verification actually survived. Re-run after hardening (see footer) for full coverage.

---

## TIER 1 — ✅ FIXED 2026-06-25 (structural, verified against live code by hand)

> **Status:** all three fixed. `check_proposal_privacy` now takes an
> `alternative_options` param and scans every string field of each option (wired at
> both create entry points: `change_proposals.py` build spine + `_propose_present.py`
> agent path). `resolution_note` is now redacted at the `resolve_proposal` choke point
> (covers route resolve, revert, and auto-resolve). Regression tests:
> `tests/concierge/test_privacy_redactor.py::TestProposalLevelCheck` (4 new) +
> `tests/core/test_change_proposals_ledger.py::test_resolution_note_private_signal_redacted`.
> All 10 green; 105 existing privacy tests still pass. (Run `make typecheck` to confirm mypy.)


All three share one root cause: the canonical gate `check_proposal_privacy`
(`backend/concierge/privacy_redactor.py:76`) scans only `title`, `description`, and the seven
`_IMPACT_TEXT_FIELDS` of `impact_analysis`. Group-readable free-text fields outside that set reach
the group with **no** privacy guard on the path. Because proposals are structured persisted records
(not chat replies), they never flow through `execute_compose_group_message`, so the
`strict_group_compose` semantic backstop does not cover them.

### 1. [HIGH] `alternative_options[].reasoning/label` bypass `check_proposal_privacy`
- **Gap:** `create_change_proposal` runs the gate at `change_proposals.py:275` but passes
  `alternative_options=` straight through to verbatim JSONB persist (`:320`, stored `:74`). The field
  is not a parameter of `check_proposal_privacy`.
- **Egress (verified):** `home/deck_payloads.py:352` → `sub=alt.reasoning` on the group **Vote deck**;
  `api/routes/proposals.py:889` → `GET /proposals` to any trip member.
- **Repro:** agent sets clean title/description but `reasoning="Skipping since Sarah can't do stairs — flat route works for her knee."` → renders verbatim to all members.
- **Fix:** add `alternative_options` param to `check_proposal_privacy`; iterate `label`+`reasoning`
  through `check_private_signal` (mirror the `_IMPACT_TEXT_FIELDS` loop). Wire at both create entry
  points: `change_proposals.py:275` and `_propose_present.py:353`.

### 2. [HIGH] `alternative_options` prose — read-side egress (`GET /api/proposals/{id}`)
- Same root gap as #1, read path: `_to_detail` (`proposals.py:889`) returns `alternative_options`
  verbatim to every `require_trip_member`. Fixed by the same create-time gate extension as #1.

### 3. [HIGH] Organizer `resolution_note` ungated by ANY privacy guard
- **Gap (verified):** grep of entire backend for `resolution_note` against
  `redact|check_private|check_proposal_privacy|find_constraint|find_identity` → **zero hits.**
  Authored at resolve/revert (after the create gate), never scanned.
- **Egress (verified):** `receipt_composer.py:179` (receipt payload) + `plan_state.py:595-610`
  (trip-wide Plan Change Strip summary) + `proposal_automation.py` group notification.
- **Repro:** organizer resolves with `"Rejecting — blows past Sarah's $50 budget ceiling."` → reaches
  every member via receipt, plan strip, and notification.
- **Fix:** run `resolution_note` through `check_private_signal`/`redact_private_signal` with the trip
  corpus at resolve/revert write time (`resolve_proposal`, before persist).

---

## TIER 2 — ✅ FIXED 2026-06-25 (gate scan + render-side hardening)

> **Status:** fixed both layers. `new_time` added to `_IMPACT_TEXT_FIELDS` so the
> gate scans it (catches keyword/corpus-detectable signal); `_fmt_time` now returns
> `None` on any non-`HH:MM` input instead of echoing it, so arbitrary prose smuggled
> into `new_time` can never render into the group receipt — callers fall back to a
> time-free phrasing. Tests: `test_receipt_composer.py` (prose-no-echo + `_fmt_time`
> contract) + `test_privacy_redactor.py::test_leak_in_new_time_caught`.

### 4. [MEDIUM] `impact_analysis.new_time` not in `_IMPACT_TEXT_FIELDS`
- **Gap (verified):** `new_time` is absent from `_IMPACT_TEXT_FIELDS` (`privacy_redactor.py:65-73`), so
  `check_proposal_privacy` never scans it. `receipt_composer.py:33` reads `ia.get("new_time")` into the
  change-applied receipt.
- **Caveat:** the receipt renders it via `_fmt_time(new_time)`; whether free-text smuggling survives
  depends on `_fmt_time`'s parse-failure fallback (TODO: confirm). If it passes raw text through, an
  attribution like `new_time="early slot since Sarah needs step-free access"` leaks.
- **Fix:** either add `new_time` to the scanned set, or have `_fmt_time` reject non-time input.

---

## TIER 3 — ✅ FIXED 2026-06-25 (investigated, then fixed conservatively)

> **Status:** both investigated against live code (the rate-limited verifiers never
> ran) and fixed without breaking the compose path's asymmetric design.
>
> **F6 (group_legibility):** confirmed neither compose path stripped the private
> sections. Added `backend/core/group_profile.py::strip_private_group_sections`
> (canonical taxonomy, single source of truth — `situation/privacy.py` now imports
> the same set, no drift) and wired it into `build_composition_context`, so the
> "Tensions & Trade-offs" / "Optimization Targets" reasoning never enters the
> composer prompt. Defense-in-depth on top of the output guards. Tests:
> `tests/core/test_group_profile.py`.
>
> **F5 (budget):** confirmed budget is NOT a `hard_constraints` type, so adding budget
> vocab to the asymmetric `_CONSTRAINT_LEAK_TYPES` would be dead code, and a symmetric
> budget guard would false-positive on legitimate group budgeting. Instead added a
> **corpus-only output guard** to `execute_compose_group_message`: it flags a span
> only when it appears verbatim in a member's private corpus (incl. budget figures in
> personal memory) — zero false positives on generic budget talk. Required a
> `keyword_layer=False` opt-out on `check_private_signal`. Tests:
> `test_group_compose.py::test_private_corpus_in_output_rejected` +
> `test_privacy_redactor.py::TestCorpusOnlyMode`.
> _Known limitation:_ corpus-only catches verbatim copies, not paraphrases — a deliberate
> trade to preserve the compose path's asymmetric, false-positive-free design.

### 5. [was contested → fixed] group_legibility "Tensions/Optimization" sections rendered into composer prompt
- **Confirmed:** `group_legibility` (which can contain agent-only "Tensions & Trade-offs" /
  "Optimization Targets" reasoning) is rendered verbatim into the composer **prompt**
  (`group_compose.py:705-708`), apparently without `extract_public_group_sections` filtering.
- **Why contested:** prompt exposure ≠ output leak. The composer **output** is guarded by
  `find_constraint_leaks` + `_semantic_privacy_guard`. End-to-end leak depends on whether those output
  guards catch reasoning that originated in the prompt. Needs a real skeptic pass + a compose eval.

### 6. [contested] No budget/money vocabulary in `_CONSTRAINT_LEAK_TYPES`
- **Confirmed:** the keyword layer has rich `accessibility` vocab but **zero** money/budget/`$` terms
  (`group_compose.py:228+`).
- **Why contested:** two downstream layers remain — the per-trip private-corpus substring match
  (`load_private_corpus_for_trip`) and the `_semantic_privacy_guard` (Haiku) — either may still catch a
  budget figure. This is a defense-in-depth gap in the keyword layer, not a proven end-to-end leak.
- **Suggested hardening:** add a `budget` category to `_CONSTRAINT_LEAK_TYPES` regardless (cheap,
  belt-and-suspenders), then confirm whether corpus+semantic already cover it.

---

## Run 3 — full-coverage pass (2026-06-25, hardened tracer)

**Coverage: 105/105 surfaces scanned, 0 errored, 0 angles errored** (fail-loud hardening
worked — no silent gaps). Raw machine output: `privacy-trace-run-latest.md` +
`privacy-regression-stubs.py` (40 stubs). This curated doc was deliberately not
overwritten.

The tracer auto-**confirmed 40 + 3 needs-human**, but that count is INFLATED — spot-checking
against live code shows a mix of real structural gaps and over-confident/incorrect claims.
The 40 collapse into ~8 root clusters. **None of cluster A–H below is fixed yet — they need a
triage pass before any fix.**

| Cluster | Root cause | Calibration (hand-checked) |
|---|---|---|
| A. Tool-emitted cards (`create_*_card`) | post LLM content to group, bypass compose guard | ✅ **FIXED 2026-06-25** — P2b `why_for_person` dropped in group context (`content.py`); P2c shapes `pitch`/`best_for` scrubbed before card post (`_shapes.py`); P3 personal take falls back to curator when headline/verdict carries private signal (`content.py`). Tests: `TestPostVenueCardGroupPrivacy`. |
| B. Proactive persists (triggers/session) | Haiku intent → group system-message, no guard | ✅ **FIXED 2026-06-25** — P1-A: `message` scrubbed via `redact_private_signal` + trip corpus before `session.send_message()` in group branch (`triggers.py`). P1-B: `social_state_markdown` stripped of private headings before Haiku triage (`group_interjection.py`). P1-C: `sender_type="system"` rows excluded from member-facing chat history response (`chat.py`). |
| **C. Daily digest** (digest/engine) | raw observations + UNSTRIPPED group profile → shared card | ✅ **FIXED 2026-06-25** — confirmed user-facing (home/cards.py, home/feed.py, concierge_feed, trips route). Strip group profile on input (`strip_private_group_sections`) + corpus-only output scrub (`redact_corpus_phrases` w/ trip corpus) before persist. Tests: `test_digest_engine.py::TestDailyDigestPrivacy`. Name-only attribution left intact per the project model ("names aren't a leak, private constraint values are"). |
| D. Story `hero_title` | field skips guard its siblings use | ✅ **FIXED 2026-06-25** (P0) — `safe_hero_title()` guard in `story_projection.py` + bypass-path fix in `trip_story_shares.py`. Tests: `test_story_projection.py`. Originally over-confirmed by tracer (documented owner-preview mitigation existed; "vegetarian not in regex" was false). |
| E. Atlas Unpacked DNA | Personal-Memory phrase → public PNG/og-image | ✅ **FIXED 2026-06-25** (P5) — `check_private_signal` filter on DNA phrases before surfacing in `atlas/unpacked.py:128`. |
| F. Cross-user feeds (discover/invite) | free-text notes → followers/SMS unscanned | ✅ **FIXED 2026-06-25** (P6) — curator hook checked via `check_private_signal` before `DiscoverFeedItem` construction (`discover/compose.py`). |
| G. Booking writeback | constraint values → group thread | Not confirmed as real user leak — booking state is user-initiated and gated dark (G2-G4 product-gated). Operator-only. |
| H. Telemetry/logs | raw private values, no redactor | ✅ **FIXED 2026-06-25** (P8) — planning telemetry replaces raw `tool_input` dict with aggregate-safe fields only (`planning_agent/agent.py`). Operator-facing langfuse spans out of scope for now. |

**Lesson for the harness:** the verifier over-confirms "an LLM *could* write something private"
(true of any LLM field) and misses human-in-the-loop / preview mitigations and group-vs-1:1
context. Next iteration should add those lenses to the verify prompt before trusting volume.

**Recommended order if fixing:** C (verified, fix ready) → A/B (user-facing group leaks, after
group-context triage) → F/G → E → D (product-judgment) → H (operator hygiene).

## Harden the tracer before the next full run
- **Per-agent retry/backoff:** a rate-limited sweep/trace currently drops to null silently → false
  "guarded". Add retry, and fail-loud if an angle returns empty.
- **Don't overwrite the report:** the run-2 findings were clobbered by run-3. Merge/append by surface id.
- **Throttle fan-out:** 114 surfaces × (trace+verify) overran the server limit. Cap concurrency lower
  or batch angles across separate runs.

## Coverage gaps still open (angles that mostly rate-limited out)
Notifications/push/SMS/email bodies, Discover personalization ("why" / "because you" frames), Atlas
share artifacts (story/map/unpacked public pages), and logs/telemetry (langfuse spans, info logs) were
inventoried but their traces largely failed. **These are unverified — not cleared.**
