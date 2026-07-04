# Dogfood Loop Validation — Pre-flight + Cohort Plan

> Status: active plan
> Created: 2026-07-04
> Owner: founder
> Purpose: validate the ONE load-bearing bet — does the "join our trip" invite loop
> actually produce re-invites? — with the cheapest path to real signal.
> Companion: `scripts/invite_loop_funnel.py` (travel-agent) measures the funnel;
> workspace memory `project_positioning_multiplayer_wedge` + `project_monetization_reality_check`.

## Why this exists

Deep-research (2026-07-03) confirmed the category can't monetize the usual ways and that
trip-planning is the highest-failure travel vertical — the graveyard was almost entirely
**single-player** planners. Vesper's only differentiated bet is that being **multiplayer**
changes the growth math. That bet was uninstrumented; the funnel script now measures it,
but it needs **real** data. This plan gets real groups through the loop while routing
*around* the Clerk-persona certification rabbit hole (that blocker is a cert-harness
artifact; real humans sign up through Clerk normally and never hit it).

---

## Part 1 — Two-device pre-flight walk

Prove the loop's front door works with two **real, distinct** Clerk accounts against the
live backend BEFORE spending real testers. Each step names the event the funnel reads, so
passing this walk also proves the instrument captures real cohort data.

### Step 0 — Clerk / backend config (VERIFIED 2026-07-04, no action needed)
Confirmed live against `vesper-backend.fly.dev`:
- `/health` + `/ready` → 200; backend up.
- `CLERK_ISSUER` + `CLERK_JWKS_URL` present & deployed (`fly secrets list -a vesper-backend`).
- `SKIP_AUTH` = false (digest matches known-false flag; also required to boot on Fly).
- `/api/me` with no token → 401 "Missing or invalid Authorization header"; with a garbage
  bearer → 401 "Invalid token" — so Clerk JWKS verification is active AND the JWKS URL is
  configured/reachable (an empty URL would 500 here, not 401).
- App dogfood EAS profile: `USE_MOCK_API=false`, `SKIP_AUTH=false`, `API_URL=vesper-backend.fly.dev`,
  `pk_test` Clerk key present. Decoded tenant = **`picked-firefly-95.clerk.accounts.dev`** (dev instance).

**The one residual check (settled by the walk itself, not a command):** that the backend's
`CLERK_ISSUER`/`CLERK_JWKS_URL` point at `picked-firefly-95` (not another valid tenant). No
API can prove this — a garbage token fails before tenant-matching. **Step 1 below (A's first
real signup) IS the test.** If that first login 401s, and only then, re-point the secrets:
```
fly secrets set -a vesper-backend \
  CLERK_JWKS_URL=https://picked-firefly-95.clerk.accounts.dev/.well-known/jwks.json \
  CLERK_ISSUER=https://picked-firefly-95.clerk.accounts.dev
```
(That triggers a redeploy — hence it's a fix-if-needed, not a precaution.)

> Note: `picked-firefly-95` is a **development** Clerk tenant (`pk_test`) — fine for dogfood.
> A real public launch needs a **production** tenant (`pk_live`) + the `production` EAS profile
> wired to it (it currently has no Clerk key). Not a dogfood blocker.

### Setup
- Fly backend: `SKIP_AUTH` off, Clerk configured — **all verified in Step 0**.
- Two genuinely different Clerk accounts — **A** (organizer) and **B** (invitee), different emails. Two devices, or device + simulator.
- Dogfood EAS build installed, pointing at that backend.

### The walk (action → expect UI → expect event)
| # | Action | Event the funnel reads |
|---|---|---|
| 1 | A signs up via Clerk | user row, `external_auth_id` set (stage 0) |
| 2 | A creates a trip | `trips.created_by = A` |
| 3 | A invites B (share link / send) | `invite.dispatched`, user_id=A |
| 4 | B signs up as a **different** Clerk account | B user row, own `external_auth_id` |
| 5 | B opens invite link → join screen → accept | **`invite.consumed`, user_id=B, already_member=false → S1 joined** |
| 6 | A proposes, B votes | `proposal_accepted` (J05) |
| 7 | Add an expense, settle | (J12) |
| 8 | **B starts their OWN trip** | **`trips.created_by=B` after join → S2 activated** ← the hop that matters |
| 9 | B invites someone | **`invite.dispatched`, user_id=B → S3 loop closed** |

### Pass criteria
Every event lands; the deeplink resolves; **no 401s between the two distinct users**; and
the privacy invariant holds — B never sees A's private constraints in any group surface.
Then run `invite_loop_funnel.py` and confirm **S1≥1, S2≥1, S3≥1 from your own walk** — that
single check proves the instrument works on real data.

### If it breaks — triage
- Deeplink won't open → AASA / universal-link config.
- 401 between users → Clerk issuer / JWKS mismatch.
- `invite.consumed` missing → event not emitted on that path.
- B blocked from creating a trip → permissions.
- **B sees A's constraints → STOP.** That's the unrecoverable-trust failure mode.

This doubles as the J02 hardening test and the pre-wave smoke test.

---

## Part 2 — Cohort plan

**Recruit:** 5–10 real friend groups, 3–6 people each, with a real or near-term trip (or a
realistic hypothetical). Prioritize groups with one **motivated organizer** — the wedge
persona. Bias toward the young friend-group segment (viral cohort); least monetizable, but
we're testing the loop, not revenue.

**Framing (what you tell them):** NOT "AI travel planner." Say: *"I'm building something that
plans your group trip and handles the annoying coordination — can your group try it for your
[X] trip?"* Give **only the organizer** the app; let **them** invite their own people.

**The one methodological rule:** **do NOT seed the groups yourself.** The whole experiment is
whether invites and re-invites happen *organically*. Hand-adding members or over-coaching
contaminates the exact signal you're paying to observe.

**Measure** (funnel + light qualitative):
- **Primary — re-invite rate (S2/S1):** did any invited member start their OWN trip? The bet.
  1–2 of 10 is real signal; **0 is a loud, informative negative.**
- **Secondary:** invite acceptance (dispatched→consumed); did invitees actually engage
  (vote, add expense); qualitative *"would you use this for your next trip?"*
- **WTP (demoted):** end-of-trip fake-paywall tap or blunt *"would you pay $X/trip?"* — signal only.

**Cadence:** weekly `invite_loop_funnel.py --since <start> --by-month` + a 15-min debrief with
2–3 organizers. Timebox **4–6 weeks.**

**Pre-committed decision gates** (data decides, not hope):
- 🟢 **Green:** invitees re-invite / start own trips at ~≥20% activation AND organizers say
  they'd use it again → the loop has legs; raise on it.
- 🟡 **Yellow:** used for the one trip but no return / no re-invite → a tool, not a loop;
  venture thesis weak — rethink before raising.
- 🔴 **Red:** groups don't finish even one loop / invites not accepted → product or wedge
  broken; fix before scaling.

**Honest caveat:** 5–10 groups is directional and qualitative, not statistically significant.
Goal = a read strong enough to de-risk a raise or force a pivot, plus the qualitative "why."

---

## What this deliberately is NOT
- NOT automated persona-JWT certification. That produces synthetic data that cannot answer a
  behavioural question, and the token-minting work is a side quest. (See the Clerk-blocker
  diagnosis: the "personas have no external_auth_id" issue blocks cert harnesses, not real
  humans.)
- The real gating items for real humans are build/secrets/TestFlight (see
  `project_dogfood_phase`) — Clerk on Fly, dogfood EAS build, APNs — NOT auth code.
