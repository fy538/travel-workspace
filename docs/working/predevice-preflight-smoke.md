# Pre-Device Pre-Flight Smoke Checklist

**Goal:** catch a broken walk environment in **5 minutes, not mid-walk.** Run this
_before anyone picks up a phone_. It verifies four things: (A) the backend is
reachable, (B) the owner preconditions / secrets are actually set, (C) the seeded
dogfood personas + their per-journey fixtures are present, and (D) the MVP
endpoints return 200 for the walked personas.

- **Date authored:** 2026-07-19
- **Backend repo:** `/Users/feihuyan/travel-workspace/travel-agent`
- **Frontend repo:** `/Users/feihuyan/travel-workspace/travel-app`
- **Workspace root (Make orchestration):** `/Users/feihuyan/travel-workspace`
- **Live target (device walk):** `https://vesper-backend.fly.dev` (Fly app `vesper-backend`)
- **Cohort:** `@dogfood.local` personas; MVP journey set `J01–J12`.

> Two things this document assumes are already true (they were set up in the
> pre-device readiness pass): the seeded device-walk states listed in
> §C/§D exist in the target DB, and the Clerk device accounts in
> `tools/dogfood/link_clerk_accounts.py` were created. This checklist **verifies**
> that, it does not create it.

---

## 0. Set the target once (copy-paste)

```bash
# From the workspace root. The device walk hits Fly, so PRELAUNCH_HOST=Fly.
export WS=/Users/feihuyan/travel-workspace
export AGENT=$WS/travel-agent
export FLY_HOST=https://vesper-backend.fly.dev
export PRELAUNCH_HOST=$FLY_HOST
export FLY_APP=vesper-backend
cd $WS
```

You also need, for the deeper checks:
- `fly` CLI authenticated (`fly auth whoami`) — for the secrets checks in §B.
- `$AGENT/.env.prod` present with `PROD_DATABASE_URL` — for the Fly-DB substrate
  audits in §C/§D (this is what `PROFILE=fly` reads; see `scripts/dogfood-env.sh`).
- `$AGENT/.venv` activated (`source $AGENT/.venv/bin/activate`) before running the
  `python -m ...` / `scripts/*.py` probes.

**Fastest single command (30s, no phone):** if you only have one minute, run
`make certify-live` from `$WS` — it chains Fly `/ready`, the Fly substrate smoke
(`dogfood-fly-smoke`), the two-persona journey API cert, and the J04 chat eval,
then prints the human live-walk runbook. The sections below are the itemized
breakdown of what it covers plus the secret/precondition checks it does **not**.

---

## A. Backend reachable (~30s)

Prove the deployed API is up, serving, and DB-connected before anything else.

| Check | Command | PASS when |
|---|---|---|
| A1. Health/ready/openapi + `/api/me` + trip CRUD | `PRELAUNCH_HOST=$FLY_HOST make smoke` | every step prints green `✓`; exits 0 |
| A2. (manual equivalent) | `curl -sf $FLY_HOST/ready && curl -sf $FLY_HOST/health && curl -sf -o /dev/null -w '%{http_code}\n' $FLY_HOST/openapi.json` | `/ready` and `/health` succeed; openapi `200` |

`make smoke` runs `scripts/smoke-happy-path.sh` — it drives `/health`, `/ready`,
`/openapi.json`, the AASA file, `GET /api/me`, and `POST /api/trips → GET
/api/trips/{id}`. It exits non-zero on the first failure.

- **Cold-start note:** Fly `auto_stop_machines=false` / `min_machines_running=1`
  is set (`fly.toml`), so the box should be warm. If `/ready` times out, the
  machine may be booting — retry once; if it still fails, `fly status -a $FLY_APP`
  and `fly logs -a $FLY_APP`.

---

## B. Owner preconditions / secrets (~90s) — the walk-killers

These are the five preconditions called out for the walk. Each row is the exact
check and **what breaks in the walk if it's missing**. All secret checks use
`fly secrets list` (names only — Fly never prints values).

```bash
fly secrets list -a $FLY_APP
```

| # | Precondition | Exact check | PASS criteria | If MISSING → walk symptom |
|---|---|---|---|---|
| B1 | **POSTHOG_API_KEY** | `fly secrets list -a $FLY_APP \| grep -i POSTHOG_API_KEY` | name present | Activation funnel goes dark — telemetry is **log-only** (`backend/core/telemetry.py:282` logs "POSTHOG_API_KEY unset — events log-only"). Walk still works; **funnel metrics won't**. |
| B2 | **EXPO_PUSH_ENABLED + Expo token** | `fly secrets list -a $FLY_APP \| grep -iE 'EXPO_PUSH_ENABLED\|EXPO_ACCESS_TOKEN'` | **both** present, and `EXPO_PUSH_ENABLED` truthy | **No push reaches the phones** → J09 push demo fails. Dispatcher runs log-only when unset (`backend/notifications/channel_dispatch.py:471`, `receipt_reaper.py:39`). |
| B3 | **AI_MODE live (or replay cassette)** | live end-to-end: `SMOKE_VERIFY_CONCIERGE=1 PRELAUNCH_HOST=$FLY_HOST PRELAUNCH_JWT=<mara-jwt> make smoke` — **and** confirm the key: `fly secrets list -a $FLY_APP \| grep -i ANTHROPIC_API_KEY` | a real SSE reply streams from `/api/trips/{id}/messages/stream`; Anthropic key present | J01 "Vesper shapes the idea" stalls — the concierge can't produce a turn. `SMOKE_VERIFY_CONCIERGE=1` runs a real LLM turn, which is the honest proof AI is live. |
| B4 | **Clerk device accounts linked** | `cd $AGENT && PYTHONPATH=. python -m tools.dogfood.link_clerk_accounts --dry-run` (against the walk DB) | mara@ and elif@ (and dao/reza for group) rows show a non-empty `external_auth_id` matching the `LINKS` map; script does **not** report "would link" for them | mara can't sign in on her device → the whole organizer-side walk is blocked. The linked IDs are pinned in `tools/dogfood/link_clerk_accounts.py`. |
| B5 | **Fly dogfood-media mount** | `curl -s -o /dev/null -w '%{http_code}\n' $FLY_HOST/dogfood-media/lisbon-phase1/trips/mara-arrival-table.jpg` | `200` (an image body) | J11/J12 hero imagery blank. **Caveat:** on a prod-like Fly host the mount is **off by default** (`should_mount_dogfood_media` returns False when `FLY_APP_NAME` is set) unless `DOGFOOD_MEDIA_STATIC_ALLOW_PROD_LIKE=true` is set. If B5 returns 404, check `fly secrets list \| grep DOGFOOD_MEDIA_STATIC_ALLOW_PROD_LIKE`. |

Extra hero paths to spot-check for B5 (J11 Tokyo / J12 Brooklyn):
```bash
for p in \
  elif-canonical/tokyo/elif-tokyo-tachinomi-standing-sake-bar.jpg \
  elif-canonical/brooklyn/elif-brooklyn-heights-promenade-edge.jpg \
  elif-canonical/rome/elif-rome-friends-walking-dusk.jpg ; do
  printf '%s -> ' "$p"; curl -s -o /dev/null -w '%{http_code}\n' "$FLY_HOST/dogfood-media/$p"
done
```

> **JWTs for B3/§D:** the two-persona live checks want `PRELAUNCH_JWT_MARA` /
> `PRELAUNCH_JWT_DAO` (or `CLERK_SECRET_KEY` to auto-mint). Mint from the Clerk
> instance the `dogfood` EAS profile points at. Without them, run the same checks
> on `TRANSPORT=testclient` (in-process) to still validate logic against the
> seeded rows — you just won't be exercising the real HTTP edge.

---

## C. Seeded personas present (~60s)

Confirms the six `@dogfood.local` travelers exist in the walk DB with non-empty
substrate. Uses the read-only cohort audit (`scripts/dogfood_audit.py`, backed by
`backend/core/db/dogfood_audit.py::score_dogfood_readiness`).

```bash
cd $AGENT
source .venv/bin/activate
# Point at the walk DB the same way the smokes do:
AGENT_DIR=$AGENT PROFILE=fly source $WS/scripts/dogfood-env.sh && dogfood_apply_profile

for p in mara elif reza dao sarah mike; do
  PYTHONPATH=. python scripts/dogfood_audit.py --summary \
    --persona "$p@dogfood.local" --no-target-banner | grep -E "$p@dogfood.local:"
done
```

| Persona | Role in walk | PASS when readiness is |
|---|---|---|
| mara | organizer, mara-lisbon (J01–J06, J10) | `ready` (not `empty`) |
| elif | elif-rome-return-2026 / elif-tokyo-2025 / elif-brooklyn-local-week (J07, J09, J11, J12) | `ready` |
| reza | reza-rome-live-2026 (J08) + companion on mara-lisbon | `ready`/`partial` |
| dao | companion / private-constraint member (J04) | `partial`+ (has membership + vote) |
| sarah, mike | companion accounts | present (row exists) |

`ready` = no `missing` areas; `empty` = ≥5 missing (unseeded — **stop and reseed**).
Areas scored: identity, taste_affinity, personal_memory, trip_context, itinerary,
conversations, atlas, expenses, photos, home_feed, stays, proactive_notifications.

**Manifest/scenario sanity (no DB needed):**
```bash
cd $WS && make dogfood-status   # validates manifests + prints scenario/pack readiness
```

---

## D. Seeded per-journey fixtures present (~90s)

Section C proves the personas exist; this proves each journey's **specific seeded
state** is in place so the interactive step actually has something to act on. The
one umbrella command is the persona journey cert — it runs each journey's core
invariant against the real seeded persona + trip and FAILs (not skips) if the
fixture is missing.

```bash
cd $AGENT
AI_MODE=replay PYTHONPATH=. python scripts/dogfood_journey_persona_cert.py --persona mara
AI_MODE=replay PYTHONPATH=. python scripts/dogfood_journey_persona_cert.py --persona elif
AI_MODE=replay PYTHONPATH=. python scripts/dogfood_journey_persona_cert.py --persona reza --journey J08
# or the workspace front door for personas mara+elif:
cd $WS && cd travel-agent && make dogfood-verify   # substrate + content + journey, one exit code
```

Journey → persona → seeded fixture map (from `scripts/journey_cert/persona.py`
`JOURNEY_PERSONA_MAP`) and what each device step needs:

| J | Persona / trip_key | Seeded fixture that must be present | Interactive payoff it unlocks |
|---|---|---|---|
| J04 | mara / `mara-lisbon` | `privacy_events` row (Dao `private_constraint_used`) | Atlas **Data Receipt** renders the trust payoff |
| J05 | mara / `mara-lisbon` | OPEN proposal `first-dinner-venue-swap` + `vote_widget` in "First dinner decision" chat; dao+reza already approve | vote chips + tally render; a member casts the **deciding** vote |
| J06 | mara / `mara-lisbon` | same open proposal, attached to plan+map | plan + map expose the same block ids |
| J06/J10 | mara / `mara-lisbon` | `booking_session` `mara-first-dinner-booking` (casa-do-alentejo ~114 EUR + cart) | `/booking/[sessionId]` reachable |
| J10 | mara / `mara-lisbon` | `booking_hold` `mara-casa-alentejo-hold` (6h window) | `DeckCall(held)` fires + hold-settle reachable |
| J08 | **reza** / `reza-rome-live-2026` | today-pinned in-progress + upcoming itinerary blocks (J08 was re-pointed mara→reza) | **Now Mode** shows "in progress" + "next stop" |
| J09 | elif / `elif-rome-return-2026` | time-sensitive proactive notification + pending invite | inbox / personal tab / badge-decrement walkable |
| J11 | elif / `elif-tokyo-2025` | pending Atlas candidate `elif-tokyo-transit-candidate` | Atlas Inbox has something to **Keep/approve** |
| J12 | elif / `elif-brooklyn-local-week` | expenses split (2 members) + returned-hero pin | **settle-up** + `StoryReadyEntry` walkable |

> **Note on cert behavior:** the persona cert deliberately creates + tears down
> throwaway rows for the cold-start journeys (J01/J03) and Atlas (J11) so it does
> not pollute the seeded travelers. A `FAIL` here means the seeded fixture is
> absent or malformed; a `SKIP` means the runner couldn't execute (e.g. voice-gated)
> — a skip is not a green.

**Targeted fixture spot-checks (optional, when a specific journey FAILs).** These
confirm the exact seeded rows exist without running the whole cert. Run inside
`$AGENT` with the walk DB profile applied (as in §C):

```bash
PYTHONPATH=. python - <<'PY'
from sqlalchemy import text
from backend.core.db.engine import get_connection
probes = {
  "J05 open proposal (first-dinner-venue-swap)":
    "SELECT count(*) FROM proposals WHERE slug='first-dinner-venue-swap' AND status='open'",
  "J06/J10 booking_session (mara-first-dinner-booking)":
    "SELECT count(*) FROM booking_sessions bs JOIN trips t ON t.id=bs.trip_id WHERE t.slug='mara-lisbon'",
  "J10 booking_hold (mara-casa-alentejo-hold)":
    "SELECT count(*) FROM booking_holds WHERE slug='mara-casa-alentejo-hold'",
  "J11 atlas candidate (elif-tokyo-transit-candidate)":
    "SELECT count(*) FROM atlas_candidates WHERE slug='elif-tokyo-transit-candidate'",
}
with get_connection() as conn:
    for label, sql in probes.items():
        try:
            n = conn.execute(text(sql)).scalar()
            print(f"{'OK ' if (n or 0) > 0 else 'MISS'} {label}: {n}")
        except Exception as e:  # column/table name drift is itself a signal
            print(f"ERR  {label}: {e}")
PY
```

> The column/slug names above are a starting point — if a probe returns `ERR`,
> the schema differs; fall back to the persona cert (authoritative) and adjust the
> SQL. The cert is the source of truth for "is this fixture walk-ready".

---

## E. MVP endpoints return 200 for the walked personas (~60s)

Two-persona live API cert covers the core mutating journeys the walk leans on
(J02 invite, J04 privacy re-draft, J05 proposal accept, J10 stay→expense). It runs
in-process (`testclient`) by default, or over real HTTP with minted JWTs.

```bash
cd $WS
# In-process (no JWT needed) — validates endpoint logic against seeded rows:
make dogfood-journey-live-api

# Real HTTP against Fly (proves the deployed edge + auth):
CLERK_SECRET_KEY=<dogfood-instance-secret> TRANSPORT=http PROFILE=fly \
  PRELAUNCH_HOST=$FLY_HOST make dogfood-journey-live-api
# ...or bring your own tokens:
TRANSPORT=http PRELAUNCH_HOST=$FLY_HOST \
  PRELAUNCH_JWT_MARA=<jwt> PRELAUNCH_JWT_DAO=<jwt> make dogfood-journey-live-api
```

PASS when it reports all cases green (the script prints per-journey ✓ and exits 0).
For a broader substrate read (trips / itinerary venues / discover compose across the
five-pack cities), `make dogfood-fly-smoke` (Fly) hits the persona substrate + the
Rome canonical brief bridge.

---

## F. Runnable pre-flight script outline (~5 min, one shot)

Drop this in a scratch file and run from the workspace root. It chains the fast,
non-destructive checks and prints a green/red board. It is an **outline** — the
JWT-gated and DB-profile steps degrade to a warning when their inputs aren't
present rather than hard-failing, so you always get to the end of the board.

```bash
#!/usr/bin/env bash
# predevice-preflight.sh — 5-minute go/no-go before the device walk.
set -uo pipefail
WS=/Users/feihuyan/travel-workspace
AGENT=$WS/travel-agent
FLY_HOST=${FLY_HOST:-https://vesper-backend.fly.dev}
FLY_APP=${FLY_APP:-vesper-backend}
PASS=0; FAIL=0; WARN=0
ok(){   printf '  \033[32m✓\033[0m %s\n' "$1"; PASS=$((PASS+1)); }
no(){   printf '  \033[31m✗\033[0m %s\n' "$1"; FAIL=$((FAIL+1)); }
warn(){ printf '  \033[33m⚠\033[0m %s\n' "$1"; WARN=$((WARN+1)); }
sec(){  printf '\n\033[1m== %s ==\033[0m\n' "$1"; }

sec "A. Backend reachable"
curl -sf "$FLY_HOST/ready"  >/dev/null && ok "/ready"  || no "/ready unreachable"
curl -sf "$FLY_HOST/health" >/dev/null && ok "/health" || no "/health failed"

sec "B. Owner secrets (fly secrets list)"
if fly auth whoami >/dev/null 2>&1; then
  SECRETS=$(fly secrets list -a "$FLY_APP" 2>/dev/null)
  grep -qi POSTHOG_API_KEY  <<<"$SECRETS" && ok "POSTHOG_API_KEY set"   || warn "POSTHOG_API_KEY unset (funnel dark)"
  grep -qi EXPO_PUSH_ENABLED<<<"$SECRETS" && ok "EXPO_PUSH_ENABLED set" || no  "EXPO_PUSH_ENABLED unset (J09 push fails)"
  grep -qi EXPO_ACCESS_TOKEN<<<"$SECRETS" && ok "EXPO_ACCESS_TOKEN set" || warn "EXPO_ACCESS_TOKEN unset"
  grep -qi ANTHROPIC_API_KEY<<<"$SECRETS" && ok "ANTHROPIC_API_KEY set" || no  "ANTHROPIC_API_KEY unset (J01 stalls)"
else
  warn "fly CLI not authed — skipping secret checks (run: fly auth login)"
fi

sec "B5. Dogfood media mount"
code=$(curl -s -o /dev/null -w '%{http_code}' \
  "$FLY_HOST/dogfood-media/lisbon-phase1/trips/mara-arrival-table.jpg")
[ "$code" = "200" ] && ok "dogfood-media 200" || no "dogfood-media $code (J11/J12 heroes blank)"

sec "B4. Clerk links + C. Personas + D. Fixtures (needs .venv + .env.prod)"
if [ -f "$AGENT/.env.prod" ] && [ -d "$AGENT/.venv" ]; then
  ( cd "$AGENT" && source .venv/bin/activate
    PYTHONPATH=. python -m tools.dogfood.link_clerk_accounts --dry-run \
      | grep -qiE 'mara@dogfood.local: .*external_auth_id' && echo LINKOK ) \
      | grep -q LINKOK && ok "Clerk mara link present" || warn "verify Clerk links (see §B4)"
  ( cd "$WS" && cd travel-agent && make dogfood-verify ) \
      && ok "dogfood-verify (substrate+content+journey) green" \
      || no "dogfood-verify FAILED — a seeded fixture is missing (see §D)"
else
  warn "no .env.prod/.venv — run §C/§D manually against the walk DB"
fi

sec "RESULT"
printf 'PASS=%d  FAIL=%d  WARN=%d\n' "$PASS" "$FAIL" "$WARN"
[ "$FAIL" -eq 0 ] && echo "GO (review any ⚠)" || { echo "NO-GO — fix ✗ first"; exit 1; }
```

For the fuller (slower, JWT/Maestro-aware) version, prefer the maintained
`make certify-live` (§0) over hand-rolling — this script is the 5-minute triage,
`certify-live` is the complete Tier-4 gate.

---

## Go / No-Go board

| Section | Green means | If red |
|---|---|---|
| A | Fly API up + DB-connected | `fly status`/`fly logs -a $FLY_APP`; redeploy if down |
| B1 POSTHOG | funnel will record | set `fly secrets set POSTHOG_API_KEY=... -a $FLY_APP` (non-blocking for the walk itself) |
| B2 EXPO push | J09 push lands | set `EXPO_PUSH_ENABLED=true` + `EXPO_ACCESS_TOKEN` secrets, redeploy |
| B3 AI live | J01 Vesper responds | ensure `ANTHROPIC_API_KEY` + `AI_MODE=live` on Fly |
| B4 Clerk | mara/elif can sign in | run `link_clerk_accounts --apply --allow-prod` on the walk DB |
| B5 media | J11/J12 heroes render | check `DOGFOOD_MEDIA_STATIC_ALLOW_PROD_LIKE` + re-promote media |
| C | personas seeded | `APPLY=1 make dogfood-promote CITY=lisbon` (+ rome/tokyo/brooklyn) |
| D | per-journey fixtures present | reseed the specific manifest; re-run `dogfood_journey_persona_cert` |
| E | MVP endpoints 200 | inspect the failing journey's endpoint before the walk |

**Rule of thumb:** any **✗** in A, B2, B3, B4, B5, C, D, or E is a **no-go** — fix
before the phone. A **⚠** on B1 (PostHog) degrades your metrics, not the walk, so
it's a "note and proceed."

---

## Referenced tooling (already exists — do not reinvent)

- `make smoke` / `scripts/smoke-happy-path.sh` — happy-path HTTP (A). `SMOKE_VERIFY_CONCIERGE=1` proves AI live (B3).
- `make certify-live` / `scripts/certify-live.sh` — Tier-4 umbrella: Fly ready + `dogfood-fly-smoke` + `dogfood-journey-live-api` + J04 chat eval + human runbook.
- `make dogfood-fly-smoke` — Fly API + persona substrate + Rome brief bridge.
- `make dogfood-status` / `scripts/dogfood-status.sh` — manifest + scenario/pack readiness (no DB).
- `make dogfood-verify` — substrate + content + journey, one exit code (§D umbrella).
- `make dogfood-journey-live-api` — two-persona J02/J04/J05/J10 endpoint cert (§E).
- `scripts/dogfood_audit.py --summary --persona <email>` — per-persona readiness (§C).
- `scripts/dogfood_journey_persona_cert.py --persona <p>` — per-journey fixture cert (§D); map in `scripts/journey_cert/persona.py`.
- `tools/dogfood/link_clerk_accounts.py --dry-run` — Clerk device-account link audit (B4).
- `scripts/dogfood-env.sh` (`dogfood_apply_profile`) — binds Postgres+Qdrant for `PROFILE=local|fly`.
