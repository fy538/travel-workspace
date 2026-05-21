# Area Audit: Release, TestFlight, Deploy, And Mobile Platform

Date: 2026-05-21  
Agent: Codex audit session  
Scope: workspace release docs, `Makefile`, release/preflight/smoke scripts, Travel App EAS/app config/runtime guards/permissions/Sentry consent, Travel Agent Fly/Docker/health/AASA/privacy surfaces.  
Mode: Audit only. No product-code changes.

## Executive Summary

- Dogfood risk: Blocked
- Highest-risk finding: The committed production app profile points at `https://travelagent.app`, but the documented production and preview backends are not healthy, and `make preflight-eas` cannot reach green.
- Checks run: `make doctor` -> pass with `uvicorn not found` warning; `make contract-check` -> pass; `make api-coverage-check` -> pass; `make preflight-eas` -> fail; `curl https://travel-agent.fly.dev/health` -> fail DNS; `curl https://travelagent.app/health` -> fail empty reply.
- Residual uncertainty: I did not run EAS build/submit, Apple CDN AASA validation, authenticated smoke, worker smoke, or concierge smoke because the preflight/backend host gates are red and live provider calls are out of scope.

## Owner / Action Checklist

### Account, DNS, Provider Tasks

| Owner action | Exact command / action | Pass criteria |
| --- | --- | --- |
| Install EAS CLI on release machine | `npm i -g eas-cli && eas --version` | `eas --version` prints `>= 12.0.0`; `make preflight-eas` proceeds past step 1. |
| Bind Expo project | `cd "Travel App" && eas init` | `jq -r '.expo.extra.eas.projectId' "Travel App/app.json"` is not `00000000-0000-0000-0000-000000000000`. |
| Set production Clerk publishable key | `cd "Travel App" && eas env:create --environment production --name EXPO_PUBLIC_CLERK_PUBLISHABLE_KEY --value pk_live_... --visibility sensitive` | Re-run `EXPO_PUBLIC_CLERK_PUBLISHABLE_KEY=pk_live_... make preflight-eas`; step `3b. Clerk key` passes. |
| Bring up Fly preview host or update docs/profile | `curl -fsS https://travel-agent.fly.dev/health` | Returns HTTP 200 with `{"status":"ok"}`; otherwise update `Travel App/eas.json` preview URL and docs to the actual Fly hostname. |
| Bring up production custom domain | `curl -fsS https://travelagent.app/health` | Returns HTTP 200 with `{"status":"ok"}`; this must pass before any production-profile TestFlight build. |
| Configure Apple Team/App Store IDs | Add real `INVITE_APPLE_TEAM_ID`, `INVITE_IOS_APP_STORE_ID`, `INVITE_APP_STORE_URL` in backend deploy secrets. | `curl -fsS https://travelagent.app/.well-known/apple-app-site-association` contains the real Team ID and `com.travelagent.app`; invite links open the TestFlight app on a physical iOS device. |
| Configure Clerk review account | Clerk dashboard test phone `+15555555555` / OTP `424242`. | Apple reviewer can sign in without receiving a real OTP. |

### Code / Repo Tasks

| Code task | Exact command / action | Pass criteria |
| --- | --- | --- |
| Fix AASA smoke validator shape | Update `scripts/smoke-happy-path.sh` to accept the route's `appIDs` array, or change the route/smoke to one agreed AASA schema. | `PRELAUNCH_HOST=https://travelagent.app SKIP_TRIP_CRUD=1 make smoke` reaches AASA pass once host is live. |
| Align microphone/audio privacy docs and native permission text | Either remove the mic request from the TestFlight build, or declare/configure it consistently in App Privacy, Apple Review Notes, `app.json`/Expo AV plugin, and public privacy policy. | `npx expo config --type introspect --json` shows a Vesper-specific `NSMicrophoneUsageDescription`, and docs no longer say the mic is not requested if the build can request it. |
| Make public privacy policy launch-ready | Replace draft/legal placeholders, remove stale providers, and remove or implement "Download My Data." | `curl -fsS https://travelagent.app/privacy` serves final contact/provider/deletion language with no placeholders. |
| Re-run full release gate | `EXPO_PUBLIC_CLERK_PUBLISHABLE_KEY=pk_live_... make preflight-eas` | All preflight steps pass: toolchain, project ID, production env, Clerk, live health, contract, API coverage, frontend tests, backend tests. |

## Findings

### P0 - EAS Production Preflight Is Red

Status: Confirmed  
User impact: The team cannot safely produce the promised production TestFlight build from this workspace. The first observed blocker is missing EAS CLI; the next committed blocker is the all-zero EAS project ID, which the runtime guard is designed to crash on in real release builds.  
Product promise affected: deployment / TestFlight readiness / push notifications

References:

- `scripts/preflight-eas-build.sh:71` - checks for `eas` on PATH.
- `scripts/preflight-eas-build.sh:74` - fails with the install instruction; this is the observed first failure.
- `scripts/preflight-eas-build.sh:88` - reads `expo.extra.eas.projectId` from `Travel App/app.json`.
- `scripts/preflight-eas-build.sh:91` - fails when the project ID is the placeholder UUID.
- `Travel App/app.json:52` - `extra.eas` config block.
- `Travel App/app.json:54` - project ID is still `00000000-0000-0000-0000-000000000000`.
- `Travel App/app/_layout.tsx:121` - release runtime guard validates the EAS project ID.
- `Travel App/app/_layout.tsx:124` - throws when the project ID is missing or placeholder.

Why it matters:

`make preflight-eas` is the documented gate before `eas build --platform ios --profile production`. It currently aborts before validating project identity, Clerk, backend health, typecheck, tests, or backend tests. Even after installing the CLI, the committed placeholder project ID would keep the gate red and would also disable push registration in release builds.

Repro or deterministic test idea:

1. Run `make preflight-eas`.
2. Current observed: aborts at step 1 with `eas CLI not on PATH`.
3. After installing EAS, run `jq -r '.expo.extra.eas.projectId' "Travel App/app.json"`.
4. Expected: real Expo UUID.
5. Current: `00000000-0000-0000-0000-000000000000`.

Suggested fix direction:

Install the EAS CLI on the release machine, run `cd "Travel App" && eas init`, commit the real project ID, set the production/preview Clerk `pk_live_` key as EAS env, and rerun `make preflight-eas` until it reaches the later gates.

Related bug class:

Release gate / account bootstrap gap

Confidence: High

### P0 - Documented Preview And Production Backend Hosts Are Not Healthy

Status: Confirmed  
User impact: A production TestFlight build would point at a backend that does not return `/health`; real-auth users would be unable to use the app against the documented production API. Preview builds are also not usable against the committed preview URL.  
Product promise affected: deployment / healthy backend / smoke readiness

References:

- `Travel App/eas.json:24` - preview builds use real backend mode.
- `Travel App/eas.json:26` - preview API URL is `https://travel-agent.fly.dev`.
- `Travel App/eas.json:32` - production builds use real backend mode.
- `Travel App/eas.json:34` - production API URL is `https://travelagent.app`.
- `scripts/preflight-eas-build.sh:198` - probes `${EXPO_PUBLIC_API_URL}/health`.
- `scripts/preflight-eas-build.sh:203` - fails the preflight when that health probe is not HTTP 200.
- `docs/Owner Action Items.md:35` - production domain verification is `curl -fsS https://travelagent.app/health`.
- `Travel Agent/backend/api/main.py:104` - backend defines `GET /health`.

Why it matters:

The release profile is already configured for `https://travelagent.app`, so backend reachability is not an optional post-build check. The requested health curls failed during this audit: `https://travel-agent.fly.dev/health` could not resolve DNS, and `https://travelagent.app/health` returned an empty reply from server.

Repro or deterministic test idea:

1. Run `curl -fsS -i --max-time 12 https://travel-agent.fly.dev/health`.
2. Current observed: `curl: (6) Could not resolve host: travel-agent.fly.dev`.
3. Run `curl -fsS -i --max-time 12 https://travelagent.app/health`.
4. Current observed: `curl: (52) Empty reply from server`.
5. Expected for both documented hosts: HTTP 200 from `/health`.

Suggested fix direction:

Deploy/repair the Fly app and custom domain, or update `eas.json` and docs to the actual deployed host. Do not ship a production-profile TestFlight build until `curl -fsS https://travelagent.app/health` and `make preflight-eas` both pass.

Related bug class:

DNS/deploy configuration gap

Confidence: High

### P1 - Microphone And Audio Privacy Claims Do Not Match The Generated Native Permission Surface

Status: Confirmed  
User impact: TestFlight reviewers or dogfood users can encounter a microphone permission surface while the review/privacy docs say this build does not request microphone access or collect audio data. That is a review-risk and trust-risk mismatch.  
Product promise affected: app store/privacy docs / mobile platform permissions

References:

- `docs/App Privacy Disclosures.md:118` - declares `Audio Data` is not collected and voice features play outbound narration only.
- `docs/App Privacy Disclosures.md:262` - says microphone permission would require revisiting the audio data answer.
- `docs/Apple Review Notes.md:68` - says microphone permission is not requested in this build.
- `Travel App/components/voice/MicPrivacyDisclosure.tsx:107` - requests OS-level microphone permission after disclosure acceptance.
- `Travel App/components/voice/MicPrivacyDisclosure.tsx:111` - calls `Audio.getPermissionsAsync()`.
- `Travel App/components/voice/MicPrivacyDisclosure.tsx:113` - calls `Audio.requestPermissionsAsync()`.
- `Travel App/package.json:37` - includes `expo-av`, whose config plugin generated microphone permission entries during `npx expo config --type introspect --json`.

Why it matters:

`npx expo config --type introspect --json` shows the generated iOS config includes `NSMicrophoneUsageDescription: "Allow $(PRODUCT_NAME) to access your microphone"` and Android includes `android.permission.RECORD_AUDIO`. That contradicts the Apple Review Notes, and the generated iOS text is generic rather than the Vesper-specific privacy rationale shown in-app.

Repro or deterministic test idea:

1. Run `cd "Travel App" && npx expo config --type introspect --json`.
2. Inspect `.ios.infoPlist.NSMicrophoneUsageDescription` and `.android.permissions`.
3. Open a voice surface that mounts `MicPrivacyDisclosure` and tap the affirmative path.
4. Expected: docs and App Store form disclose the same permission/data behavior as the build.
5. Current observed/static: docs say no mic request; generated native config and component code can request mic access.

Suggested fix direction:

Pick one TestFlight posture. If voice is playback-only, remove/disable the mic permission request and configure `expo-av` with `microphonePermission: false` if possible. If voice interrupt/mic stays in, update App Privacy, Apple Review Notes, public privacy policy, and Expo plugin permission text to describe the actual mic/audio behavior.

Related bug class:

Privacy disclosure drift / platform permission mismatch

Confidence: High

### P1 - Public Privacy Policy Is Still Draft/Placeholder And Diverges From The Launch Disclosures

Status: Confirmed  
User impact: The App Store privacy URL would serve draft language with placeholder contact information and claims that do not match the current TestFlight disclosure set. Users and reviewers get inconsistent answers about providers, audio, analytics, and data export.  
Product promise affected: privacy disclosures / app review readiness

References:

- `Travel Agent/docs/legal/privacy.md:12` - policy last updated date.
- `Travel Agent/docs/legal/privacy.md:13` - explicitly marked draft for MVP and requiring counsel review.
- `Travel Agent/docs/legal/privacy.md:71` - says voice recordings and transcripts are collected when using voice features.
- `Travel Agent/docs/legal/privacy.md:145` - lists APNs / Firebase Cloud Messaging.
- `Travel Agent/docs/legal/privacy.md:146` - lists PostHog as product analytics provider.
- `Travel Agent/docs/legal/privacy.md:165` - says users can export data through `Me -> Account -> Download My Data`.
- `Travel Agent/docs/legal/privacy.md:251` - contact email remains `[privacy@your-domain.com - fill in before launch]`.
- `Travel Agent/backend/api/routes/legal.py:91` - serves this file publicly at `/privacy`.

Why it matters:

`docs/App Privacy Disclosures.md` says no third-party analytics SDKs and no audio data in this build, while the public policy says PostHog may receive analytics data and voice recordings/transcripts are collected. The policy also promises a download-my-data path that I did not find on the account screen; the account screen does expose deletion, but not a matching export action.

Repro or deterministic test idea:

1. Once production is live, run `curl -fsS https://travelagent.app/privacy`.
2. Search the response for `Draft`, `your-domain.com`, `PostHog`, `Voice recordings`, and `Download My Data`.
3. Expected: no placeholders and no promises/providers that are absent or contradicted by the submitted App Privacy questionnaire.
4. Current static: all listed strings exist in the served policy source.

Suggested fix direction:

Before App Store submission, update the served privacy policy to match the actual TestFlight build: final contact details, actual analytics/crash providers, actual voice/audio behavior, implemented deletion/export rights, and retention language that matches backend retention jobs.

Related bug class:

Legal/privacy documentation drift

Confidence: High

### P2 - AASA Smoke Check Disagrees With The AASA Route Shape

Status: Confirmed  
User impact: Once the backend host is live, `make smoke` can report Universal Links as malformed even if the backend serves the route's current JSON successfully. That creates a false deploy blocker and weakens confidence in the deep-link smoke.  
Product promise affected: deep links / smoke and rollback procedures

References:

- `Travel Agent/backend/api/routes/invite_landing.py:301` - builds the AASA payload.
- `Travel Agent/backend/api/routes/invite_landing.py:305` - emits `appIDs: ["TEAM.bundle"]`.
- `scripts/smoke-happy-path.sh:146` - validates `apps[0].get('appID')`, singular.
- `scripts/smoke-happy-path.sh:149` - fails when `appID` is missing or malformed.

Why it matters:

The smoke script and backend route are not testing the same schema key. The route emits `appIDs`, while smoke only accepts `appID`. This means the documented post-deploy smoke can fail on its own validator instead of the actual Universal Links state.

Repro or deterministic test idea:

1. Compare the route output shape to the Python expression in `scripts/smoke-happy-path.sh:146`.
2. Or run smoke against any backend serving this route once `/health` is live.
3. Expected: smoke accepts the app identifier shape the backend serves.
4. Current static: backend emits `appIDs`; smoke checks `appID`.

Suggested fix direction:

Update the smoke validator to accept the route's `appIDs` array and assert that at least one entry matches `<TEAM_ID>.com.travelagent.app`, or change the route and smoke together to a single Apple-supported schema.

Related bug class:

Smoke false negative / sibling inconsistency

Confidence: High

### P3 - Dockerfile Healthcheck Still Probes `/docs`

Status: Confirmed  
User impact: Container-level health does not exercise the same `/health` endpoint used by Fly and smoke. This is unlikely to block the current Fly dogfood path, but it is stale release hygiene and can mislead local/container operators.  
Product promise affected: deployment observability

References:

- `Travel Agent/Dockerfile:60` - comment says to swap to a real endpoint once one exists.
- `Travel Agent/Dockerfile:63` - Docker `HEALTHCHECK` definition.
- `Travel Agent/Dockerfile:64` - probes `http://localhost:8000/docs` instead of `/health`.
- `Travel Agent/backend/api/main.py:104` - real `/health` endpoint exists.

Why it matters:

Fly's `fly.toml` correctly checks `/health` and `/ready`, but the image's own healthcheck is stale. If this image is reused outside Fly, `/docs` availability becomes the container health signal rather than the explicit liveness endpoint.

Repro or deterministic test idea:

1. Build/run the Docker image locally.
2. Inspect `docker inspect --format '{{json .Config.Healthcheck}}' <image>`.
3. Expected: healthcheck probes `/health`.
4. Current static: healthcheck probes `/docs`.

Suggested fix direction:

Point the Dockerfile healthcheck at `/health`; keep deeper dependency checks in `/ready` and smoke.

Related bug class:

Deploy healthcheck drift

Confidence: High

## Non-Findings / Things Ruled Out

- Contract drift is not the release blocker: `make contract-check` passed with 210 paths, 241 operations, 330 schemas, and generated API types matched `docs/openapi.json`.
- API coverage is not the release blocker: `make api-coverage-check` passed with 175/175 frontend HTTP call sites covered by OpenAPI.
- Production mock/auth flags are committed correctly in `Travel App/eas.json`: production has `EXPO_PUBLIC_USE_MOCK_API=false`, `EXPO_PUBLIC_SKIP_AUTH=false`, and an HTTPS API URL.
- The iOS bundle ID and Associated Domains are present in `Travel App/app.json`: `com.travelagent.app` and `applinks:travelagent.app`.
- Runtime release guards exist for mock mode, skip-auth mode, missing Clerk key, and placeholder EAS project ID in `Travel App/app/_layout.tsx`.
- Sentry is gated off unless both a DSN and explicit crash-reporting consent are present, and the remote sink scrubs obvious PII keys.
- Photo permissions have recoverability work: iOS limited-library is treated as success, "Manage selected photos" is surfaced, and Settings fallbacks exist after denial.
- Push registration avoids prompting at launch and has structured errors for physical-device and placeholder-project-ID cases.
- Backend Fly config has realistic release/rollback bones: `release_command = "alembic upgrade head"`, separate `app` and `worker` processes, `/health` and `/ready` Fly checks, Redis surfaced via `/health/external`, and rollback docs cover app rollback vs schema-forward behavior.

## Suggested Follow-Up Checks

- `EXPO_PUBLIC_CLERK_PUBLISHABLE_KEY=pk_live_... make preflight-eas` after EAS CLI, project ID, and backend health are fixed.
- `PRELAUNCH_HOST=https://travelagent.app SMOKE_VERIFY_AUTH=1 PRELAUNCH_JWT=<test JWT> make smoke` to prove Clerk production auth rejects anonymous requests and accepts the demo/test JWT.
- `PRELAUNCH_HOST=https://travelagent.app SMOKE_VERIFY_WORKER=1 make smoke` to prove Redis-backed worker intake is alive without requiring a live LLM turn.
- `PRELAUNCH_HOST=https://travelagent.app SMOKE_VERIFY_APPLE_CDN=1 SKIP_TRIP_CRUD=1 make smoke` after AASA origin is correct and Apple's CDN has had time to refresh.
- `cd "Travel App" && npx expo config --type introspect --json | jq '.ios.infoPlist.NSMicrophoneUsageDescription, .android.permissions'` before App Store submission to confirm native permissions match review/privacy docs.
- `curl -fsS https://travelagent.app/privacy | rg 'Draft|your-domain|Download My Data|PostHog|Voice recordings'` before submitting the App Store privacy URL.
