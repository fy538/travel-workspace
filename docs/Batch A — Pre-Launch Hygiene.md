# Batch A — Pre-Launch Hygiene

**Goal:** close the gap between "substrate is excellent" and "a real user can use this."

**Why this batch is the right one right now:**
- The 13 Owner Action Items have been an untracked file for a while. They're not engineering problems; they're calendar problems pretending to be engineering problems.
- `CONCIERGE_OUTPUT_GUARD_MODE` rollout (per `Travel Agent/CLAUDE.md`) requires "at least one full week of `log` mode against real traffic" before flipping to `regenerate`. That's a hard dependency on having real users. Most of the protective gates we built this session have the same shape: they need traffic to calibrate.
- 5 of 13 Owner Action Items are 🔴 and *interdependent* (Apple Team ID → EAS init → domain → SSL → Clerk → APNs). One day of focused ops work, not three weeks.

**Scope:** one focused session. NOT a sprint. Deliverables are concrete artifacts, not "do everything."

---

## Deliverables

1. **`docs/Pre-Launch Deploy Surface.md`** — security/ops audit memo enumerating every secret, env var, scope, key rotation policy, signed-URL TTL. Status column per item.
2. **`docs/Owner Action Items.md` (rewritten)** — same 13 items but each row gains: prerequisites, verification command, time estimate, owner. Becomes a real punch list.
3. **`scripts/smoke-happy-path.sh`** — drives the canonical user flow (create trip → invite member → concierge turn → memory query) against a configurable host. Exits non-zero on first failure. The cheapest way to find the next 5 bugs.
4. **`make pre-launch`** target that runs `offline-qa` + the smoke test against a target host.

---

## Order of operations

### 1. Inventory pass (delegate to research subagent, ~20 min)

Send an Explore agent with this prompt scope:
- Every `os.getenv(...)` and `os.environ[...]` in `Travel Agent/backend/`
- Every `EXPO_PUBLIC_*` referenced in `Travel App/`
- Cross-reference each against `.env.example` (both repos) — what's documented vs not
- Every place a third-party key is used (Anthropic, Langfuse, Clerk, SendGrid, Twilio, Tavily, Google Places, Cartesia, Deepgram, OpenTable…) with read/write scope detection
- Any signed-URL generation (S3, image uploads) — TTL?
- Clerk session config (lifetime, refresh policy)

Output: a table, one row per secret/var, with columns: `name | repo | usage_sites | in_env_example? | scope_or_ttl | rotation_policy | risk`.

### 2. Draft the deploy-surface memo (~15 min)

Take the table from step 1 and synthesize:
- 🔴 Missing from `.env.example` (anything used in code but not documented)
- 🟠 Scope too broad (any key that's read-write when read-only would suffice)
- 🟡 Rotation policy unclear / never rotated
- 🟢 Good

Write to `docs/Pre-Launch Deploy Surface.md`. Same format as `Owner Action Items.md`.

### 3. Rewrite Owner Action Items as a real punch list (~20 min)

Current file is descriptive. Rewrite each of 13 items as:

```markdown
### #N — <title>
**Status:** 🔴/🟠/🟡 · **Time est:** Xh · **Depends on:** #M
**What:** <one-sentence concrete action>
**Verify:** `<exact command that returns 0 when done>`
**Notes:** <gotchas, links to provider docs>
```

Items #5, #6, #7 (domain/SSL/Clerk) probably need a sub-tree because they chain.

### 4. Smoke-test runner (~30 min)

`scripts/smoke-happy-path.sh` — bash + curl, NOT a TS test. Reasons:
- Type-safety isn't the point; "does the prod surface actually respond" is.
- Easy to run against any host: `./scripts/smoke-happy-path.sh https://travelagent.app`
- Output is human-readable for ops triage

Minimum viable flow:
1. `GET /health` → 200
2. `GET /openapi.json` → 200, valid JSON
3. (auth setup — depends on Clerk being live; phase 2)
4. `POST /api/trips` → 201
5. `GET /api/trips/{id}` → 200 matching
6. `POST /api/conversations/{id}/messages` → SSE stream starts
7. Cleanup: `DELETE` the trip

Each step prints `✓` or `✗ <reason>` and exits non-zero on first failure. Idempotent where possible.

### 5. Wire `make pre-launch` (~5 min)

```makefile
pre-launch: offline-qa  ## Pre-launch gate: offline QA + smoke test against a target host
	@./scripts/smoke-happy-path.sh "$${PRELAUNCH_HOST:?Set PRELAUNCH_HOST=https://...}"
```

---

## Definition of done

- [ ] Deploy-surface memo committed; counts: 🔴 = 0, 🟠 ≤ 3 with documented mitigations
- [ ] Owner Action Items rewritten with verification commands for every item
- [ ] Smoke test runs green against local backend (`PRELAUNCH_HOST=http://localhost:8000 make pre-launch`)
- [ ] At least 2 of OAI 🔴 items have a *committed* PR (not just documented) — the point of this session is movement, not more docs

---

## What's NOT in this batch

- Implementing Clerk integration end-to-end (that's OAI #7 itself; we're documenting it, not doing it)
- Adding new tests (test confidence is Batch B)
- Touching the engine (architecture is Batch C)
- Splitting mock.ts

---

## After this batch

The next session should be either:
- **OAI execution session** — actually do items #1-7 with `pre-launch` running as the gate. This is calendar work + waiting on Apple/Google.
- **First real-user smoke** — invite one trusted tester, give them TestFlight access, sit with them while they use it. Record everything. The first 30 minutes of real-user use will produce more bugs than the next month of refactoring.

---

## Estimated time: 90–120 minutes for the deliverables. The OAI execution itself is separate calendar time.
