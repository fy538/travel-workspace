# Owner Action Items

Account / credential / certificate work that gates first-real-user launch. None of these are code tasks; they're calendar tasks with code-side verification.

**Status legend:** 🔴 do now · 🟠 before TestFlight · 🟡 before public launch · ✅ done

Each item below has the same shape:

- **Status / Time est / Depends on:** at-a-glance
- **What:** the concrete action
- **Verify:** an exact command that returns success when the item is done
- **Notes:** gotchas, links, provider specifics

---

## Critical path (chain — must be done in order)

These five items are interdependent and block every other launch task. Do them in sequence.

### #1 — Apple Team ID into `.env`
**Status:** 🔴 · **Time est:** 5 min · **Depends on:** Apple Developer account
**What:** copy your 10-character Team ID from developer.apple.com → Account → Membership and paste into `Travel Agent/.env`:
```
INVITE_APPLE_TEAM_ID=ABCD1234EF
```
Restart the backend after editing.
**Verify:** `curl -s http://localhost:8000/.well-known/apple-app-site-association | grep -q ABCD1234EF`
**Notes:** Apple's CDN re-fetches AASA within ~24h. Force a refresh via `https://app-site-association.cdn-apple.com/a/v1/travelagent.app` once the domain is live.

### #3 — `eas init` for production builds
**Status:** 🔴 · **Time est:** 10 min · **Depends on:** Apple Developer account, npm/Expo CLI installed
**What:**
```bash
cd "Travel App"
eas init             # writes real projectId to app.json
eas build:configure  # writes eas.json profiles
```
**Verify:** `jq -r '.expo.extra.eas.projectId' Travel\ App/app.json` is NOT `00000000-0000-0000-0000-000000000000`.
**Notes:** Universal Links only work in real EAS builds, not Expo Go.

### #5 — Own and deploy at `travelagent.app`
**Status:** 🔴 · **Time est:** 2-4 hours (varies by host) · **Depends on:** purchased domain
**What:** deploy the FastAPI backend to a host (Railway / Render / Fly.io / your VPS) and point the domain DNS at it.
**Verify:** `curl -fsS https://travelagent.app/health` returns 200.
**Notes:** Railway and Fly.io are fastest for a Python+Postgres+Qdrant stack. Render's free tier sleeps after 15 min idle — avoid for production. Self-hosted on a VPS needs nginx/Caddy as reverse proxy.

### #6 — SSL certificate for `travelagent.app`
**Status:** 🔴 · **Time est:** auto if using Railway/Render/Fly; ~15 min for certbot · **Depends on:** #5
**What:** managed hosts auto-provision Let's Encrypt. If self-managed: `certbot --nginx` or use Caddy (which does this automatically).
**Verify:**
```bash
echo | openssl s_client -servername travelagent.app -connect travelagent.app:443 2>/dev/null | openssl x509 -noout -dates
```
returns valid `notBefore` and `notAfter` dates more than 30 days out.
**Notes:** Apple rejects non-HTTPS AASA, so this is hard-required for Universal Links. Most managed hosts handle renewal automatically.

### #7 — Clerk application
**Status:** 🔴 · **Time est:** 30 min (incl. testing with phone OTP) · **Depends on:** none (can start in parallel with #5/#6)
**What:** dashboard.clerk.com → Create application → enable Phone Number sign-in.
Then in `Travel App/.env`:
```
EXPO_PUBLIC_CLERK_PUBLISHABLE_KEY=pk_live_...
EXPO_PUBLIC_SKIP_AUTH=false
EXPO_PUBLIC_USE_MOCK_API=false
```
And in `Travel Agent/.env`:
```
CLERK_JWKS_URL=https://<your-instance>.clerk.accounts.dev/.well-known/jwks.json
CLERK_ISSUER=https://<your-instance>.clerk.accounts.dev
SKIP_AUTH=false
```
**Verify:** `curl -fsS -H "Authorization: Bearer $TEST_JWT" https://travelagent.app/api/me` returns 200; same call without the header returns 401.
**Notes:** test with both phone+OTP flow (production) and the Clerk dashboard's "Impersonate user" feature (dev). See [Pre-Launch Deploy Surface.md](Pre-Launch Deploy Surface.md) item #5 for the recommended startup-time validation.

---

## TestFlight blockers (need #1, #3, #5, #6, #7)

### #2 — App Store Connect listing
**Status:** 🟠 · **Time est:** 30 min · **Depends on:** Apple Developer
**What:** appstoreconnect.apple.com → Apps → New App.
- Bundle ID: `com.travelagent.app`
- Minimum iOS: 17.0
After: copy the numeric App Store ID into `Travel Agent/.env`:
```
INVITE_IOS_APP_STORE_ID=1234567890
INVITE_APP_STORE_URL=https://apps.apple.com/app/id1234567890
```
**Verify:** open `https://apps.apple.com/app/id<your-id>` in a browser — the listing loads (will say "not yet available" until publication).

### #4 — Production iOS build via EAS
**Status:** 🟠 · **Time est:** 30 min build + queue · **Depends on:** #1, #2, #3, #7
**What:**
```bash
cd "Travel App"
eas build --platform ios --profile production
```
Submit to TestFlight from App Store Connect when the build finishes.
**Verify:** TestFlight shows the build in "Internal Testing"; install on a real iOS device; tap an invite link from outside the app and the deep-link resolves into the app.

---

## Push notifications

### #8 — Expo Push access token
**Status:** 🟠 · **Time est:** 5 min · **Depends on:** none
**What:** expo.dev → Account → Access Tokens → Create. Then:
```
# Travel Agent/.env
EXPO_ACCESS_TOKEN=...
EXPO_PUSH_ENABLED=true
```
**Verify:** restart backend, then trigger a test push: `POST /api/users/{me}/test-push` (add the route if missing) → device receives notification.

### #9 — APNs key for production iOS push
**Status:** 🟠 · **Time est:** 15 min · **Depends on:** Apple Developer, #2
**What:** developer.apple.com → Certificates, Identifiers & Profiles → Keys → Create new key (APNs). Download the `.p8` and upload via Expo dashboard.
**Verify:** trigger a push notification from the backend to a TestFlight build on a real device → notification arrives within 10s. Push to simulator does NOT prove this — only a physical device.

---

## Invite delivery (defer until invite flow is exercised)

### #10 — SendGrid (transactional email)
**Status:** 🟡 · **Time est:** 30 min (incl. DNS TXT verification) · **Depends on:** #5 (need a domain)
**What:** sendgrid.com → API Keys → Create (Mail Send permission). Verify `invites@travelagent.app` as sender via DNS TXT record.
```
SENDGRID_API_KEY=SG....
SENDGRID_FROM_EMAIL=invites@travelagent.app
SENDGRID_FROM_NAME=Vesper
```
**Verify:** `curl -X POST -d '{"to":"<your-email>","subject":"test","body":"test"}' http://localhost:8000/admin/send-test-email` (add route if missing) → email arrives.

### #11 — Twilio (transactional SMS)
**Status:** 🟡 · **Time est:** 20 min · **Depends on:** none
**What:** twilio.com → Console → Phone Numbers → Buy a number.
```
TWILIO_ACCOUNT_SID=AC...
TWILIO_AUTH_TOKEN=...
TWILIO_FROM_NUMBER=+15555550123
```
**Verify:** trigger an SMS invite to your own phone number → message arrives.

---

## Third-party content APIs

### #12 — Google Places API key
**Status:** 🟠 · **Time est:** 15 min · **Depends on:** none
**What:** console.cloud.google.com → APIs & Services → Credentials → Create key. Enable Places API (New) + Maps JavaScript API. **Restrict to backend IP + set a daily quota cap** to avoid surprise bills.
```
GOOGLE_PLACES_API_KEY=AIza...
```
**Verify:** `curl -fsS "https://maps.googleapis.com/maps/api/place/textsearch/json?query=coffee+brooklyn&key=$GOOGLE_PLACES_API_KEY" | jq '.status'` returns `"OK"`.
**Notes:** the current `.env` has a placeholder. Without a real key, venue search falls back to whatever's seeded in Qdrant.

---

## Android (post-iOS launch)

### #13 — Google Play Console listing
**Status:** 🟡 · **Time est:** 1-2 hours · **Depends on:** none
**What:** play.google.com/console → Create app. Package: `com.travelagent.app`. Grab the SHA-256 cert fingerprint for Digital Asset Links.
```
INVITE_PLAY_STORE_URL=https://play.google.com/store/apps/details?id=com.travelagent.app
```
**Verify:** Play Console shows the app in draft state; `assetlinks.json` at `https://travelagent.app/.well-known/assetlinks.json` includes the SHA-256.

---

## Dependency graph

```
Critical chain:                                 ┌─→ #2 listing
  Apple Dev → #1 Team ID                        │
            → #3 eas init ────────────────────→ #4 prod build ──→ TestFlight
            → #7 Clerk ───────────────────────→ #4              ┘
  Domain    → #5 deploy → #6 SSL ─────────────→ AASA works
                       └───────────────────────→ #10 SendGrid

Push:        #2 (App Store Connect) + Apple Dev → #9 APNs
                                  + Expo signup → #8 Expo token

Independent: #11 Twilio, #12 Google Places, #13 Play Console
```

The fastest path to "real user on TestFlight" runs #1 → #3 → #7 → #5 → #6 → #2 → #4. Everything else is post-launch polish.

---

## Status board (one-glance)

| # | Item | Status | Time |
|---|------|--------|------|
| 1 | Apple Team ID → `.env` | 🔴 | 5 min |
| 3 | `eas init` | 🔴 | 10 min |
| 5 | Deploy at `travelagent.app` | 🔴 | 2-4 h |
| 6 | SSL cert | 🔴 | auto / 15 min |
| 7 | Clerk application | 🔴 | 30 min |
| 2 | App Store Connect listing | 🟠 | 30 min |
| 4 | iOS production EAS build | 🟠 | 30 min + queue |
| 8 | Expo push access token | 🟠 | 5 min |
| 9 | APNs key | 🟠 | 15 min |
| 12 | Google Places key | 🟠 | 15 min |
| 10 | SendGrid | 🟡 | 30 min |
| 11 | Twilio | 🟡 | 20 min |
| 13 | Play Console listing | 🟡 | 1-2 h |

**Estimated calendar time to "first user on TestFlight":** 1-2 focused days, mostly serial waits (Apple review, DNS propagation, Clerk testing). Most individual items are < 30 min of actual work.
