# Owner Deploy Checklist (Gate B) — the account/infra chain

These are the Gate B steps that **cannot be code-fixed** — they need your Fly,
Expo, Clerk, and Apple accounts. Wave 3A already landed the *code-side*
guardrails (a release build now boot-fails on a placeholder EAS projectId or a
loopback API URL, and `.env.example` defaults `SKIP_AUTH=false`), so a
misconfigured build can't silently reach a tester. What's left is standing up
the real host + identities below.

Do them in this order — `scripts/preflight-eas-build.sh` validates them in the
same sequence and aborts on the first miss. Each step has a verify command;
don't move on until it passes. Substitute the placeholder values in `<…>`.

Cross-references: `docs/Owner Action Items.md` (status board),
`docs/Deploy & Rollback Runbook.md` (full runbook), and the audit
`docs/audits/pre-dogfood-2026-05/dogfood-readiness.md` (P0 detail).

---

## 1. Deploy the backend on Fly  (Owner Action Items #5)

```bash
cd "Travel Agent"
fly launch --copy-config --no-deploy        # uses the committed fly.toml; do NOT let it overwrite
fly secrets set \
  ANTHROPIC_API_KEY=<rotated-live-key> \
  TAVILY_API_KEY=<rotated-live-key> \
  CLERK_JWKS_URL=<https://…clerk.accounts.dev/.well-known/jwks.json> \
  CLERK_ISSUER=<https://…clerk.accounts.dev> \
  SKIP_AUTH=false \
  DATABASE_URL=<managed-postgres-url> \
  QDRANT_URL=<qdrant-url> QDRANT_API_KEY=<…> \
  MAPBOX_TOKEN=<…>            # lights up the story-card static map
fly deploy                                   # release_command runs `alembic upgrade head`
```

Verify:
```bash
curl -fsS https://<fly-app>.fly.dev/health                       # → 200
curl -fsS https://<fly-app>.fly.dev/openapi.json | jq -r .info.title   # → "Travel Agent API"
```

> Rotate `ANTHROPIC_API_KEY` / `TAVILY_API_KEY` to fresh live keys BEFORE sharing
> any build (they may have been used in dev). See `docs/operations/Secret Rotation Runbook.md`.

## 2. Point the preview EAS profile at the real host

If your Fly app name is not exactly `travel-agent`, update the preview URL:

- File: `Travel App/eas.json` (preview profile `EXPO_PUBLIC_API_URL`).
- `travel-agent.fly.dev` is unowned today — leaving it there is the unreachable-host P0.

Verify: `jq -r '.build.preview.env.EXPO_PUBLIC_API_URL' "Travel App/eas.json"` resolves with `curl .../health` → 200.

## 3. Custom domain + SSL for travelagent.app  (Owner Action Items #6)

```bash
fly certs add travelagent.app
# add the DNS A record (and AAAA) Fly prints, at your registrar
fly certs show travelagent.app          # wait for "Certificate Authority: Let's Encrypt … Issued"
```

Verify: `curl -fsS https://travelagent.app/health` → 200. Only then is the
production profile (`Travel App/eas.json` → `https://travelagent.app`) truthful.

## 4. EAS project identity  (Owner Action Items #3)

```bash
cd "Travel App"
eas init                # NOT `eas build:configure` — that clobbers the committed profiles
jq -r '.expo.extra.eas.projectId' app.json   # → a real UUID, not 00000000-…
```

> The Wave 3A boot guard now throws on the placeholder, so a build that skips this
> fails fast instead of silently breaking push — but you still need the real id.
> Commit the updated `app.json`.

## 5. Clerk live app + EAS env vars  (Owner Action Items #7)

```bash
cd "Travel App"
eas env:create --environment production --name EXPO_PUBLIC_CLERK_PUBLISHABLE_KEY --value pk_live_… --visibility sensitive
eas env:create --environment preview    --name EXPO_PUBLIC_CLERK_PUBLISHABLE_KEY --value pk_live_… --visibility sensitive
```

Confirm `EXPO_PUBLIC_USE_MOCK_API=false` and `EXPO_PUBLIC_SKIP_AUTH=false` in both
EAS profiles (the runtime leak guard boot-crashes a release build otherwise).

## 6. Apple Team ID + AASA deep links  (Owner Action Items #1, #6; audit 12-P1)

- Replace `REPLACE_ME` Apple Team ID wherever it appears in the AASA file the
  backend serves at `/.well-known/apple-app-site-association` (and any
  `appID`/`appIDs` entry).
- Confirm `Travel App/app.json` `ios.associatedDomains` host matches the host
  that serves the AASA (`applinks:travelagent.app`).
- Preview-build caveat (audit 12-P1): preview builds point at `<fly-app>.fly.dev`
  but the AASA is on `travelagent.app`. Until the custom domain is live, either
  (a) add `applinks:<fly-app>.fly.dev` as a second associated domain AND serve
  the AASA under that host, or (b) accept that preview invite deep links only
  work via the `guide://invite/<token>` custom scheme.

Verify:
```bash
curl -fsS https://travelagent.app/.well-known/apple-app-site-association | jq .   # valid JSON, real Team ID
```

## 7. Green preflight, then build

```bash
cd "<workspace root>"
make preflight-eas        # must end "failed: 0"; do NOT set SKIP_LIVE_API_PROBE=1 (it's the stale-URL catch)
cd "Travel App"
eas build --platform ios --profile preview      # smoke on a device first
eas build --platform ios --profile production    # then production → TestFlight
```

## 8. App Store Connect + push delivery  (Owner Action Items #2, #8, #9)

- App Store Connect listing (copy in `docs/App Store Connect Copy.md`).
- APNs key / Expo push credentials so the notifications golden path works on device.

---

## 9. Re-enable scheduled workflows (at dogfood start)

The maintenance crons were paused pre-dogfood for cost (commit 0b220c49) —
they had no real work to do without testers and were draining GitHub Actions
minutes (the every-2h cache refresh alone was ~360 runs/month). Once the
backend is deployed and real testers exist, turn them back on:

- In `Travel Agent/.github/workflows/cron.yml`, uncomment the `schedule:` block.
  These jobs need `DATABASE_URL` + `ANTHROPIC_API_KEY` set as repo Actions
  secrets (see the workflow header) — which only exist post-deploy, so this
  step belongs here, not earlier.
- In `Travel Agent/.github/workflows/live-booking-canary.yml`, uncomment the
  weekly `schedule:` if you want the booking-provider canary running again.

Until then, any job can still be triggered on demand from the Actions tab
(`workflow_dispatch`).

---

## Pre-tester verification gate

Run the full reliability ladder against the LIVE host before inviting anyone:

```bash
make contract-check
PRELAUNCH_HOST=https://travelagent.app make smoke
# one paid live-canary pass of LC-1 (private constraint stays group-safe) —
# the Wave 1 privacy fixes are new; prove them under a real LLM turn before a tester does.
```

When `/health` is 200, `make preflight-eas` is green, a preview build runs on a
device, and LC-1 passes against the deployed stack — the deploy gate is cleared.
