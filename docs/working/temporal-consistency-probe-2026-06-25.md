# Temporal & Consistency Probe — Bug Report

**Date:** 2026-06-25
**Repos:** `travel-agent` (backend), `travel-app` (frontend)
**Scope:** Timezone/date arithmetic, cache-key correctness, settle-time races.
**Tally:** 4 candidates examined → **2 confirmed**, **1 uncertain (latent)**, 1 refuted.

> All findings survived adversarial refutation. Each was traced end-to-end against the real code at `~/travel-workspace` (the launch cwd is the empty placeholder dir). Verdicts below are post-refutation.

---

## 1. Dedupe

No two findings share a root cause. They are independent:

- **tz-1** — client-side local-midnight date subtraction across DST (presentation-layer off-by-one).
- **anchor-voice-cache-key-omits-user** — server-side cache key missing the `user_id` dimension (cross-user personalization/privacy leak).
- **tz-3** — settle-time race between app-clock pre-check and DB-clock expiry sweep (money-moved-but-not-confirmed).

They land in three different categories (date math / cache keying / distributed-transaction race) and three different files. Nothing to merge. Worth noting all three are *temporal* in flavor but the mechanisms do not overlap.

---

## 2. Confirmed bugs (ranked by severity)

### HIGH — Anchor voice-line cache leaks one traveler's personalized line to co-travelers

- **id:** `anchor-voice-cache-key-omits-user`
- **repo:** `travel-agent`
- **file:** `backend/home/compose.py:266` (key build); value generated at `compose.py:112-121`, fed from `feed.py:757-788`
- **severity:** high (confirmed, high confidence) — a genuine **cross-user privacy/personalization leak**, bounded to a short status line rather than full-profile exfiltration.
- **one-line repro:** Ana and Ben share a Lisbon trip on "Day 3 of 5"; Ana opens trip-home first, her Haiku-generated anchor line (shaped by her private taste / DNA phrase / dietary-medical hard constraints / affect) is cached under `anchor_voice:{trip_id}|during|Day 3 of 5`; within the 6h TTL Ben opens the same trip-home, hits the same user-blind key, and is served **Ana's** personalized line — across both uvicorn workers via shared Redis.
- **why it's real:** The L1 + L2 (Redis `anchor_voice`) key is `f"{trip_id}|{phase}|{temporal_anchor}"` — no user dimension. But the cached value is built from `traveler_context = state_ctx.to_prompt_block()` for the **requesting** user (`user_state.py:93-129`: taste axes, interests, `In their words: "{dna_phrase}"`, `Hard constraints: ...`, `Right now: {affect_summary}`, personal-memory summary). `temporal_anchor` and `phase` are trip-level → byte-identical keys for co-travelers on the same day. The user-keyed *outer* feed cache (`feed.py:668`) means Ben misses there and proceeds straight into the user-blind inner cache. TTL = 6h (`compose.py:228`), outlasting a day boundary, no invalidation on user switch.
- **asymmetry (rules out "deliberate user-agnostic cache"):** The hero-voice cache directly below (`compose.py:348`) **correctly** keys on `{user_id}|{state}|{destination}|{temporal}`, and `UserStateContext.cache_fingerprint()` (`user_state.py:131-149`) is a purpose-built SHA-1 of cache-safe Tier-1 state designed exactly for folding into such keys — this path never uses it. Distinct from the 4 previously-fixed TTL-drift bugs; this is a missing key *dimension*, not TTL drift.
- **fix sketch:**
  - *Minimal (mirror hero path):* `cache_key = f"{user_id}|{trip_id}|{phase}|{temporal_anchor}"`.
  - *Better (busts on taste/constraint change; lets identical cold-start users still share):* thread `state_ctx.cache_fingerprint()` from `feed.py:779` into `get_or_compose_anchor_voice_line` and key on `f"{trip_id}|{phase}|{temporal_anchor}|{state_fingerprint}"` (sentinel `"cold"` when `traveler_context` is empty). Avoids per-user bloat for empty/identical Tier-1 state while closing the leak. Audit any other caller passing non-empty `traveler_context` with a user-blind expectation.
- **regression test:** `pytest` in `backend/home/tests`. Use `reset_anchor_voice_cache()` and stub `compose_anchor_voice_line` to echo `traveler_context` so a cache hit returning the wrong user's content is observable; disable/monkeypatch the L2 layer to isolate L1:
  ```python
  def test_anchor_voice_cache_does_not_leak_across_co_travelers(monkeypatch):
      compose.reset_anchor_voice_cache()
      async def fake_compose(*, traveler_context, user_id, **kw):
          return f"line-for[{traveler_context}]"
      monkeypatch.setattr(compose, "compose_anchor_voice_line", fake_compose)
      monkeypatch.setattr(compose, "shared_cache_get", lambda ns, k: None)
      monkeypatch.setattr(compose, "shared_cache_setex", lambda ns, k, v, t: None)
      trip_id, ana, ben = uuid4(), uuid4(), uuid4()
      common = dict(trip_id=trip_id, trip_title="Lisbon", destination="Lisbon",
                    phase="during", temporal_anchor="Day 3 of 5", phase_context="...")
      ana_line = asyncio.run(compose.get_or_compose_anchor_voice_line(
          **common, traveler_context='Taste: minimalist; In their words: "slow mornings"', user_id=ana))
      ben_line = asyncio.run(compose.get_or_compose_anchor_voice_line(
          **common, traveler_context="Hard constraints: shellfish allergy", user_id=ben))
      assert "shellfish allergy" in ben_line, "Ben got Ana's cached personalized anchor line"
      assert ana_line != ben_line
  ```
  Complement with a privacy-invariant-tracer eval scenario: render the home feed for two members of one shared trip on the same day and assert member B's `voice_line` is not byte-identical to member A's when their `UserStateContext` differs.

---

### MEDIUM — `computeLiveDay` reports wrong "Day N of M" across spring-forward DST (off-by-one)

- **id:** `tz-1`
- **repo:** `travel-app`
- **file:** `utils/helpers.ts:177-195` (`computeLiveDay`); renders at `components/trips/TripsHomeModel.ts:772-778` (`liveHeroSub`)
- **severity:** medium (confirmed high confidence; severity adjusted down only by the rarity of the trigger window, not by any correctness doubt).
- **one-line repro:** Device TZ `America/New_York`, trip `start_date=2025-03-08` / `end_date=2025-03-12`, today `2025-03-10` (after the Mar 9 02:00 spring-forward) → live hero renders **"day 2 of 4"** for a 5-day trip on its 3rd day (correct: "day 3 of 5").
- **why it's real:** `computeLiveDay` parses date-only `YYYY-MM-DD` via `parseIsoDateLocal` (`helpers.ts:27-32` → `new Date(year, month-1, day)` = **local** midnight) for both `today` and the trip dates, subtracts `getTime()`, divides by a fixed `86_400_000`, then `Math.floor()+1`. Across spring-forward a local calendar day is only 23h, so the elapsed-ms total is short of a full day-multiple and `Math.floor` truncates downward. Reproduced under `TZ=America/New_York` with node: the `2025-03-08` (EST/-0500) → `2025-03-10` (EDT/-0400) local-midnight delta is 47h = 169,200,000 ms; `/86,400,000 = 1.958`; `floor=1`; `+1 = 2`. `totalDays` likewise computes 4 instead of 5. Under `TZ=UTC` the same inputs give the correct `{3,5}`; a non-DST June NY trip gives the correct `{3,7}` — confirming the defect is specifically a spring-forward-straddling span in a DST-observing zone. Fall-back (Nov, 25h day) rounds correctly because the extra hour does not push `Math.floor` below the integer boundary — the asymmetry claim holds.
- **reachability (real prod, not dev-only):** `now()` (`utils/now.ts`) returns plain `new Date()` in real builds; the mock/time-travel override is dev-only and never called in real builds, so `todayIsoLocal()` is real device wall time. `computeLiveDay` feeds the user-facing live-hero standfirst and is also consumed by `app/(tabs)/trips/index.tsx`, `[tripId]/index.tsx`, `plan.tsx` (day selector), `components/atlas/AtlasTripState.tsx`, `utils/tripNotificationSections.ts`, `hooks/useConciergeHomeState.ts`.
- **corroboration:** `utils/dateOnly.ts` header explicitly warns "Local midnight deltas are not always 24h across DST boundaries"; `utils/inviteTimeline.ts` already uses the **safe** UTC pattern (`parseUtcDate` + `setUTCDate` + `getTime()/86400000`). `helpers.ts` diverges from the repo's own correct convention.
- **fix sketch:** Compute the day delta from calendar dates without subtracting local-midnight `Date`s — mirror `utils/inviteTimeline.ts`. Replace `parseIsoDateLocal(...).getTime()` deltas in `computeLiveDay` (and the analogous `daysBetween` / `computeTripPhase` `daysUntil`) with `Date.UTC`-based math:
  ```ts
  function isoToUtcMs(iso: string): number {
    const [y, m, d] = iso.split('T')[0].split('-').map((p) => parseInt(p, 10));
    return Date.UTC(y, m - 1, d);
  }
  const dayOf = Math.floor((isoToUtcMs(today) - isoToUtcMs(trip.start_date)) / 86_400_000) + 1;
  const totalDays = Math.floor((isoToUtcMs(trip.end_date) - isoToUtcMs(trip.start_date)) / 86_400_000) + 1;
  ```
  `Date.UTC` values are always exactly 24h apart, so the DST offset shift disappears. Prefer factoring a shared `isoToUtcMs`/`diffCalendarDays` helper into `utils/dateOnly.ts` and reusing it across `helpers.ts` to kill the divergence at the root.
- **regression test:** Add to `__tests__/utils/tripsHomeHero.test.ts` a spring-forward case pinned to `TZ=America/New_York` (set in jest config env / `process.env.TZ` before module load):
  ```ts
  it('computeLiveDay is correct across spring-forward DST', () => {
    jest.useFakeTimers();
    jest.setSystemTime(new Date('2025-03-10T12:00:00-04:00'));
    try {
      const live = computeLiveDay({ start_date: '2025-03-08', end_date: '2025-03-12' });
      expect(live).toEqual({ dayOf: 3, totalDays: 5 }); // currently returns { dayOf: 2, totalDays: 4 }
    } finally {
      jest.useRealTimers();
    }
  });
  ```
  Pair with a control assertion that a non-DST June trip still yields day 3 of 7, to guard against over-correction.

---

## 3. Uncertain — worth a human look

### `tz-3` — `settle_hold` can charge the provider then lose the confirmation if the hold expires mid-settle

- **repo:** `travel-agent` · **file:** `backend/booking_agent/holds.py:99-129` (settle path); `db/booking_crud.py:748-841` (expire sweep + persist).
- **verdict:** **uncertain** — the race logic is **real and correctly diagnosed** (high confidence), but the entire hold/settle engine is **gated dark in prod** (`duffel_live_booking_enabled` defaults `False`; `pay_for_order` raises `RuntimeError` before the HTTP POST when off). So **no money moves today** and no real user can lose a charge right now. It becomes a severe silent charge-stranding bug the instant `BOOKING_DUFFEL_LIVE_BOOKING_ENABLED=true` — which memory frames as imminent.
- **mechanism:** `settle_hold` pre-checks the deadline against the **app** clock (`datetime.now(UTC)`, line 99), then calls `provider.pay_for_order()` (live Duffel POST, 3–5s, moves money), then persists via `settle_offer_hold_result` which UPDATEs `WHERE status == 'held_for_payment'`. The concurrent `_expire_stale_holds_sync` sweep (every ~60s) flips holds to `'expired'` using the **DB** clock (`func.now()`). `get_tx` is plain `engine.begin()` (READ COMMITTED, no `SELECT ... FOR UPDATE`), so the two paths share no row lock. If the deadline elapses (or DB clock leads app clock) during the provider round-trip, the sweep sets `'expired'`, the settle UPDATE matches **0 rows** and returns `None`; the block is never stamped `confirmed`/`booking_ref` and `price_cents` is never written **even though the charge succeeded**. The route then returns HTTP 410 `hold_expired`. No reconciliation net: the checkout reconciliation worker does not scope `held_for_payment`, so the stranded charge is never reconciled or refunded.
- **why human eyes:** the fix touches live-money transition logic and should land *before* the dark gate flips. Recommended fix: atomically CLAIM the hold via a DB-clock CAS to an intermediate `'settling'` state **before** `pay_for_order` (`UPDATE ... SET status='settling' WHERE id=:id AND status='held_for_payment' AND payment_required_by > func.now() RETURNING ...`); the expire sweep's existing `status=='held_for_payment'` filter then leaves in-flight settles alone; `settle_offer_hold_result` matches `status=='settling'`; and if the charge succeeds but the row isn't in the claimed state, log+alert and persist the charge result anyway rather than dropping money on the floor. A forced-interleave async pytest (gate ON in-test, `pay_for_order` blocks while the expire sweep fires) should assert the charge is never silently dropped.

> **Action:** track `tz-3` as a release-blocker checklist item gated to the Duffel-live flip, not a today-fix.

---

## 4. Patterns — classes of mistake worth a lint rule or shared helper

Two recurring classes, each addressable structurally rather than one-off:

1. **Two clocks compared without a shared source of truth.**
   - *tz-1:* local-midnight `Date` subtraction assumes every calendar day is 86,400,000 ms — false across DST.
   - *tz-3:* an **app-clock** pre-check guards a state transition that a concurrent **DB-clock** sweep can invalidate, with no shared lock.
   - **Rule of thumb:** never derive calendar-day counts by subtracting local-midnight `Date`s — use `Date.UTC`-based diffs (frontend) and never let one decision read the app clock while another reads the DB clock for the *same* invariant — arbitrate both on `func.now()` through one atomic CAS (backend).
   - **Lint/helper:** (a) a shared `utils/dateOnly.ts#diffCalendarDays(isoA, isoB)` that the lint forbids bypassing — flag any `parseIsoDateLocal(...).getTime()` subtraction or hard-coded `86_400_000` divisor outside it; the repo already has the correct pattern in `utils/inviteTimeline.ts`, so this is consolidation, not invention. (b) Backend: an ESLint-equivalent / code-review check that any `status`-transition UPDATE preceded by a `datetime.now(UTC)` deadline check must run inside a single `get_tx` CAS using `func.now()`.

2. **Personalized value cached under a key that omits the user dimension.**
   - *anchor-voice-cache-key-omits-user:* per-user content keyed only by trip/phase/day → cross-user leak. The codebase already has the right primitive (`UserStateContext.cache_fingerprint()`) and a correct sibling (`compose.py:348` hero cache) — the defect is divergence, not absence.
   - **Rule of thumb:** if a cached value is derived from `traveler_context` / `user_id` / any Tier-1/Tier-2 state, the cache key MUST include `user_id` or a `cache_fingerprint()`.
   - **Lint/helper:** a small static check (or review checklist) over `backend/home/compose.py` and any `shared_cache_setex` caller: if the value-producing function takes `user_id` or `traveler_context`, the key string must reference `user_id` or `cache_fingerprint`. Fits naturally into the existing privacy-invariant tracer workflow as a structural complement to the runtime two-member-shared-trip eval.

---

## 5. Recommended fix order

1. **`anchor-voice-cache-key-omits-user` (HIGH, ship first).** Live cross-user privacy leak on a shared, in-prod surface. Cheap, self-contained fix (fold `cache_fingerprint()`/`user_id` into the key) with a clear regression test. Highest harm-per-effort.
2. **`tz-3` (UNCERTAIN → release-blocker for Duffel-live).** Fix the atomic `'settling'` CAS **before** flipping `BOOKING_DUFFEL_LIVE_BOOKING_ENABLED=true`. Not a today-emergency (dark gate), but must not ship live booking without it. Needs human review of the money-transition logic.
3. **`tz-1` (MEDIUM).** Real user-visible wrong "day N of M", but only for spring-forward-straddling trips in DST zones (narrow window, ~twice a year per affected trip). Fix via the shared UTC helper, which also retires the date-math divergence class. Lowest urgency of the three.

Alongside (3): land the two structural guards from §4 (shared `diffCalendarDays` helper + cache-key-includes-user check) so the next instance of either class is caught at review/CI time rather than in prod.

---

## 6. Second pass — Idempotency / Concurrency / Ordering (added 2026-06-25)

> The first pass was rate-limited and never probed categories A (idempotency), B (concurrency), C (ordering). This pass covered them with a single sequential tracer. Net: the proposal/vote/expense/settle paths are **unusually well-hardened** (conditional `from_status` UPDATEs, `FOR UPDATE` on votes, guarded `is_settled=false` settle, partial-unique idempotency indexes, fingerprint-stable FE keys). Most candidates were refuted. **Two findings survived — both lower-severity than they first look.**

### LOW–MEDIUM — Revert mutates the itinerary *before* taking the status-transition guard (Concurrency)

- **repo:** `travel-agent` · **file:** `backend/api/routes/proposals.py:657-731` → `backend/core/db/proposal_apply.py:1195` (`revert_accepted_proposal_v2`, holds no lock)
- **scenario:** Organizer double-taps "Revert" (or two organizers tap ~simultaneously). The route checks `status == "accepted"` (read, **no lock**), then mutates the itinerary, and only *afterward* runs the conditional `db_resolve(..., from_status=("accepted",))`. Both concurrent requests pass the `accepted` check and both run `revert_accepted_proposal_v2` before either flips status.
- **verdict:** CONFIRMED as unguarded mutation-before-transition; UNCERTAIN it produces user-visible corruption. Ledger/receipt writes *are* gated (only one wins the transition; the loser 409s), and the itinerary mutation is mostly idempotent (compare-and-set reverse-patches skip on second pass; added-block deletes return rowcount 0). Residual risk: the `version_restore` path under contention stacking two redundant restore versions — wasteful/confusing history, not corruption.
- **fix:** Flip the order — take the `accepted → withdrawn` (or a dedicated `reverting`) transition **first** via the conditional UPDATE, run the itinerary mutation only if it fired. Or wrap the route in `pg_try_advisory_lock(hashtext('proposal_revert_' || proposal_id))`. Mirrors the apply path, which already gates side-effects on the transition firing.
- **regression test:** two concurrent reverts on one accepted proposal → assert exactly one 200 + one 409, added block deleted once, history grows by ≤1.

### LOW (latent) — `plan_events` `since`-exclusive cursor can skip same-`created_at` siblings (Ordering)

- **repo:** `travel-agent` · **file:** `backend/core/db/plan_events.py:111-112` (filter `created_at > since`); column default `_tables/itinerary.py:394` (`server_default=func.now()`)
- **mechanism:** `created_at` defaults to `now()` = `transaction_start_time()`, **identical for every row written in the same transaction** (`apply_accepted_proposal` writes several events per txn). Display order is correctly disambiguated by `(created_at DESC, id DESC)`, but the incremental `since` filter uses **only** `created_at` and is strictly `>`. A consumer advancing `since` to the last event's `created_at` would permanently skip any sibling sharing that timestamp that fell past `limit`.
- **verdict:** CONFIRMED latent defect in the function contract; **not currently triggered** — the only `since` caller (`plan_state.py:135`) uses a fixed time-window cutoff, not an advancing cursor, so dropping an event exactly at the cutoff is harmless. Becomes a real bug the moment someone builds an incremental "events since last seen" tail (plausible given the SSE/timeline direction).
- **fix:** Make the cursor `(created_at, id)`-based (`WHERE (created_at, id) > (:ts, :id)` + matching `ORDER BY`), or add a monotonic `bigserial seq` and cursor on that. Document the `now()`-ties-within-a-transaction gotcha.
- **regression test:** write 3 events in one txn (shared `created_at`), page with `limit=2`, then fetch `since=page1[-1].created_at` → assert the 3rd event is still returned (currently skipped).

### Cleared (refuted) — paths confirmed safe

Proposal accept→apply double-write (gated by `from_status` CAS in both manual + auto-resolve) · vote loss under contention (`SELECT … FOR UPDATE` merge) · duplicate expense on retry (partial unique `uq_expenses_idempotency` + 409) · expense settle double-apply/double-push (`WHERE is_settled=false` no-op + rowcount-derived `actually_settled`) · chat turn double-submit (`idempotency_key` unique + `TurnInFlightError`, single SSE stream so deltas can't reorder) · FE double-submit (fingerprint-stable idempotency keys).

**Updated tally across both passes:** 6 candidates confirmed/uncertain examined → **2 high/medium confirmed (anchor-cache, DST day-count)** · **3 low/latent (revert-order, plan_events cursor) + uncertain (settle race)** · large set of candidate races refuted as already-hardened.
