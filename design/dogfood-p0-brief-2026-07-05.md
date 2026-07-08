# Dogfood World P0 — Open the Device Gate, Fix Time, Disarm the Landmine (2026-07-05)

Context: a 3-agent audit found the dogfood world is structurally sound on the backend but has three P0 issues blocking real on-device dogfooding. Full audit in project memory `project_dogfood_world_audit.md`. This brief has TWO parts: manual ops steps only you can do (Clerk console), and code/content changes an agent can execute.

---

## PART A — Manual ops (you, ~15 minutes, do this first)

1. **Create two Clerk test-instance accounts** using the exact emails the seeded personas already carry:
   - `mara@dogfood.local`
   - `elif@dogfood.local`
   Use the Clerk dashboard for whichever test/dev instance the `dogfood` EAS profile points at (check `eas.json` → `dogfood` profile's Clerk publishable key to confirm which instance). Set any password/OTP method Clerk allows for test accounts.

2. **Verify the adoption bridge fires.** Sign in on a dogfood-profile build (simulator is fine for this check) as `elif@dogfood.local`. Confirm you land in elif's seeded world (her trips, memories, group) rather than a fresh empty account. The bridge is `backend/core/db/traveler.py:137-148` (`get_or_create_user_from_auth`) — it backfills `external_auth_id` on email match. If it does NOT fire, stop and report back with what you saw (don't debug further — this is exactly the kind of surprise worth a second look before proceeding).

3. Once confirmed, this becomes the new documented dogfood device entry path (Part B, item 5 writes it down).

---

## PART B — Code & content (agent-executable)

### 1. Disarm the affinity-seeder landmine

`scripts/seed_persona_affinity.py` is a superseded seeder that creates 4 orphan `@dogfood.local` users (noor/theo/wren/soren) and — critically — would **overwrite canonical elif's affinity data with a stale, different shape** if ever run against the real dogfood cast. It shares the email domain with the real manifests, so it's easy to run by mistake.

- Move it to `scripts/_archive/seed_persona_affinity.py` (or delete if `git log` shows nothing else references it — check first with `grep -rn "seed_persona_affinity" --include="*.py" --include="*.md" --include="*.yaml"`).
- If any doc references it as a live tool, update the doc to point at `tools/dogfood/content/seed.py` instead.
- Do NOT run it before archiving — just move/delete.

### 2. One world day — validator + re-anchor

**Problem:** `dogfood_today` is a per-trip override in `trip_summary` (see `backend/core/dogfood_dates.py`), consumed by only 3 read paths (`trip_note.py`, `concierge_feed.py`, `plan_state.py`). Different manifests pin different, disagreeing dates — elif's world says `2026-06-03`, mara's says `2026-10-04` (which is *day 2 of a trip whose status is "planning"* — a lifecycle contradiction). Meanwhile real-world dates have drifted: elif's Rome-return trip (Jun 20–25) is now in the past while `status: planning`; her Istanbul-return trip (Jul 8–14) goes live in real time in 3 days.

Do:
- **Add a validation check** to `tools/dogfood/content/validate.py` (or `validate_scenarios.py` — check which one actually runs in CI first) that fails when, for any manifest: (a) a trip's `status` field contradicts what its dates + the effective `dogfood_today` (or real today if unset) imply — e.g. `status: planning` but `dogfood_today` falls inside `[start_date, end_date]`; (b) `dogfood_today` falls after `end_date` for a trip not marked completed/kept-memory.
- **Re-anchor elif's manifests** (`elif-rome.yaml`, `istanbul-phase1.yaml`, and any other elif manifest carrying `dogfood_today`): pick ONE of two fixes per trip and apply consistently —
  - Roll the trip dates forward relative to today (2026-07-05) so `dogfood_today` sits inside a still-future or still-current window, OR
  - Flip the Rome-return trip's `status` to `completed`/kept-memory framing (it's already past) and drop its `dogfood_today` override entirely (let it read as a real memory, not a pinned "planning" trip).
  Use your judgment on which reads more naturally per trip; the constraint is that after this change, running the new validator (previous step) against all manifests must pass with zero contradictions.
- Check `lisbon-phase1.yaml` (mara) too — the audit flagged its `dogfood_today: 2026-10-04` as *mid-trip* while `status: planning`. Resolve the same way.
- Do NOT touch `packs.yaml`/`scenarios.yaml` registry structure in this step — that's a separate P1 item.

### 3. Update the stale mental model in docs (small)

`docs/dev-personas.md` or wherever "5 dev personas (ana/ben/carmen/dev/elif)" is documented (grep for it) — update to reflect: 13 FE mock personas (list them) + 6 backend-real personas (mara/elif/dao/reza/sarah/mike), with a one-line pointer to `tools/dogfood/content/scenarios.yaml` as the mock↔backend mapping. Keep it short — this is a correction, not a new document.

### 4. Document the new device entry path

Add a short section (5–10 lines) to whichever doc is the closest thing to a canonical dogfood runbook today (`travel-agent/docs/operations/Dev Modes.md` looked most current in the audit — verify) titled something like "Real-device entry via Clerk email adoption": the two test accounts created in Part A, the mechanism (email-match backfill in `traveler.py`), and a one-line warning that creating a Clerk account with an email that does NOT match a seeded persona creates a fresh empty user (expected, not a bug).

## Explicitly OUT of scope for this pass (P1/P2, do not touch)

- Registering `solo-trips-phase1`/`atlas-phase1`/`atlas-phase2` into `packs.yaml`/`scenarios.yaml`
- The carmen decision (build CDMX pack vs demote) and `personas.py` → `guide_voices.py` rename
- Regenerating stale QA reports, promoting elif's cert into main CI
- Any dev-tooling consolidation (DevFab/persona-switcher merge), riso illustration backfill, media delivery path

## Definition of done

Two Clerk accounts exist and adoption is confirmed (Part A) · `seed_persona_affinity.py` archived, zero live references remain · new validator check exists and passes against all current manifests with zero date/status contradictions · elif + mara manifests re-anchored so the validator passes · dev-personas doc corrected · runbook gains the device-entry section · `make test` / existing dogfood test suite still green.
