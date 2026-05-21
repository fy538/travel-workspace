# Pre-Dogfood Area Audit 12 — Frontend Platform, Error/Offline, Permissions, Deploy Config

Date: 2026-05-21
Scope: Travel App API triad (`utils/api/{interface,http,mock}.ts`) vs the
generated OpenAPI schema; error / offline / loading paths (incl. SSE in
`utils/sse.ts`); permission request + recovery flows for camera, photos,
location, notifications, microphone; crash safety (ErrorBoundary +
Sentry-behind-consent + AppState handling); and the cross-repo release
configuration (`Travel App/eas.json`, `Travel App/app.json`,
`Travel Agent/fly.toml`, `scripts/preflight-eas-build.sh`, env wiring).
Mode: read-only; no product code, scripts, or config were modified.

## Summary

| Severity | Count |
|---|---:|
| P0 | 3 |
| P1 | 4 |
| P2 | 3 |
| TECH-DEBT | 3 |

**Biggest concern:** the release-config story documented in
`docs/audits/pre-dogfood-2026-05/dogfood-readiness.md` is still
**unresolved across three independent surfaces** that all have to be
green simultaneously before a TestFlight build can talk to a backend.
`Travel App/eas.json:18-35` aims preview at `https://travel-agent.fly.dev`
and production at `https://travelagent.app` — DNS for both still fails
from this machine. `Travel App/app.json:52-55` still carries the
placeholder EAS `projectId` `00000000-…`, and the same placeholder
flows through `utils/push.ts:161-167` into `Notifications.getExpoPushTokenAsync({projectId})`,
so a release build that somehow shipped with the placeholder cannot
register for push at all (silent push-loss, not a boot crash). `Travel Agent/fly.toml`
is configured for the `app` name `travel-agent` but no Fly app exists
under that name — first deploy is gated on a manual `fly launch --copy-config --no-deploy`
sequence that has not yet run.

The runtime side is in much better shape: `app/_layout.tsx:98-113` hard-fails
boot on a release build that left `USE_MOCK` / `SKIP_AUTH` on, or that
has no Clerk key; `utils/api/http.ts:101-124` throws at module load
when a non-mock production build is missing `EXPO_PUBLIC_API_URL`;
SSE reconnect, single-flight 401 redirect, the global `OfflineBanner`,
the `useOfflineGate` mutation gate, the per-surface permission rationale
+ Settings recovery toasts, and the consent-gated Sentry sink are all
present. The release-config gap is concentrated at the deployment layer,
not the runtime layer.

**Highest mock/real drift risk:** the mock has no representation of
five distinct real-backend error shapes that the UI is explicitly built
to handle, so dogfood is the first time these paths run end-to-end:
the `trip_needs_substance` 409 on `createInvite` (`utils/api/interface.ts:976-979`),
the `in_flight` 409 + idempotency-key dedupe on `sendMessage` / SSE
(`utils/api/interface.ts:284-292`, `utils/sse.ts:200-216`), the
`410 consumed` invite-accept race (open P1 from
`docs/audits/pre-dogfood-2026-05/dogfood-readiness.md:147-173`), the
SSE `stalled` reconnect at 45s (`utils/sse.ts:235-256`), and the
photo-upload `AppState=background` abort path (`utils/api/http.ts:391-469`).
Mock-mode parity tests pass, but the suite is shape-parity, not
behavior-parity — every one of these paths is "mock returns synchronous
success, real backend can return an error that the UI must handle".

---

## Findings

### [P0] — Production EAS build cannot reach a backend: both release hosts unreachable, projectId still placeholder, Fly app not initialised

**References:**
- `Travel App/eas.json:18-27` — preview profile sets `EXPO_PUBLIC_API_URL=https://travel-agent.fly.dev`.
- `Travel App/eas.json:29-35` — production profile sets `EXPO_PUBLIC_API_URL=https://travelagent.app`.
- `Travel App/app.json:52-55` — `expo.extra.eas.projectId` is `00000000-0000-0000-0000-000000000000`.
- `Travel Agent/fly.toml:46-47` — `app = "travel-agent"`, primary region `iad`, but no `fly launch` has run.
- `scripts/preflight-eas-build.sh:71-78,88-95,189-204` — the preflight gates each of these and aborts on the first miss.
- `docs/Owner Action Items.md:30-50` — items #3 (`eas init`), #5 (deploy at `travelagent.app`), #6 (SSL) all 🔴.
- `docs/audits/pre-dogfood-2026-05/dogfood-readiness.md:61-117` — already documented these as P0 OPEN.

**Why it matters to a real tester:** a TestFlight build with
`EXPO_PUBLIC_USE_MOCK_API=false` boots, the runtime leak guard at
`Travel App/app/_layout.tsx:98-106` passes (mock/skip-auth are off),
then the very first authed query (`getMe`, `getTripsForUser`,
`getNotificationFeed`, or the chat SSE) targets a host that doesn't
resolve. The user sees a generic "Network error" / `OfflineBanner`
even though their device IS online — the `useNetworkState` belief is
"connected", but `_request`'s `fetch` throws and surfaces as
`APIError { kind: 'network' }`. No part of the UI distinguishes
"backend hostname does not exist" from "your wifi is flaky", so support
churn is guaranteed and there is no in-app recovery — the user has to
delete the app.

**Repro / deterministic test idea:**

```bash
# Reproduces the failure from this machine right now:
curl -sS --max-time 10 -o /dev/null -w '%{http_code}\n' https://travel-agent.fly.dev/health   # → 000 (DNS failure)
curl -sS --max-time 10 -o /dev/null -w '%{http_code}\n' https://travelagent.app/health        # → 000 (no service)

# Static config side:
jq -r '.expo.extra.eas.projectId' "Travel App/app.json"   # → 00000000-0000-0000-0000-000000000000

# What `make preflight-eas` would do once `eas-cli` is on PATH:
#   step 2 → fails on placeholder projectId
#   step 3 → reads eas.json production env, passes (it's set)
#   step 3b → fails unless EXPO_PUBLIC_CLERK_PUBLISHABLE_KEY is exported as pk_live_…
#   step 4 → fails on the same curl above (GET .../health ≠ 200)
```

**Suggested fix direction:** the exact diff required, in the order
`scripts/preflight-eas-build.sh` validates it:

1. **Backend up.** Run the `Travel Agent/fly.toml:1-44` first-deploy sequence
   (`fly launch --copy-config --no-deploy`, `fly secrets set …`, `fly deploy`).
   Confirm `curl https://<fly-app>.fly.dev/health` → 200 and
   `curl https://<fly-app>.fly.dev/openapi.json | jq .info.title` → `"Travel Agent API"`.
   The release_command already runs `alembic upgrade head` so the first deploy
   gets a populated schema.
2. **Fix the preview URL.** If the Fly app name is anything other than
   exactly `travel-agent`, update `Travel App/eas.json:26` so the
   preview profile points at the real `https://<fly-app>.fly.dev`.
   `travel-agent.fly.dev` is unowned today.
3. **Wire the custom domain.** `fly certs add travelagent.app`, point
   the DNS A record at the Fly IPv4, wait for cert, confirm
   `curl https://travelagent.app/health` → 200. Only then is
   `Travel App/eas.json:34` truthful.
4. **EAS project identity.** `cd Travel\ App && eas init` (NOT
   `eas build:configure` — `docs/Owner Action Items.md:30-44`
   warns it would clobber the committed profiles). Verify
   `jq -r '.expo.extra.eas.projectId' Travel\ App/app.json` is a real UUID.
   Note: `utils/push.ts:161-167` passes this same `projectId` into
   `Notifications.getExpoPushTokenAsync` — leaving it as the placeholder
   silently breaks push even if the app otherwise reaches the backend.
5. **Clerk EAS env var.** `eas env:create --environment production
   --name EXPO_PUBLIC_CLERK_PUBLISHABLE_KEY --value pk_live_…
   --visibility sensitive`; repeat for `--environment preview`. The
   runtime guard at `Travel App/app/_layout.tsx:108-113` boot-crashes
   a release build without this.
6. **Green preflight.** `make preflight-eas` must end with
   `passed: N · failed: 0` before invoking `eas build`. Do NOT set
   `SKIP_LIVE_API_PROBE=1` for the canary build — that's the only check
   that catches "preview build pointed at a stale URL".

**Confidence:** High. Every step has a deterministic verify command;
nothing here is judgement-based.

---

### [P0] — Release-build leak guard validates `USE_MOCK` / `SKIP_AUTH` / Clerk-key but not the EAS `projectId` placeholder

**References:**
- `Travel App/app/_layout.tsx:98-106` — release-build leak guard for `USE_MOCK` and `SKIP_AUTH`.
- `Travel App/app/_layout.tsx:108-113` — release-build assertion that Clerk key is present.
- `Travel App/app.json:52-55` — `expo.extra.eas.projectId: "00000000-0000-0000-0000-000000000000"`.
- `Travel App/utils/push.ts:161-167` — `Constants.expoConfig?.extra?.eas?.projectId` is read at runtime and passed verbatim into `Notifications.getExpoPushTokenAsync({ projectId })`.
- `Travel App/utils/push.ts:183-205` — successful token fetch then calls `api.registerDevice`, persisting it server-side.

**Why it matters to a real tester:** the runtime leak guard is the
documented backstop ("if the EAS profile is ever wrong, the runtime
catches it" — `scripts/preflight-eas-build.sh:122-124`), but it does
not check the placeholder projectId. A release build can ship with all
three flags correct, boot fine, and then silently break push registration:
Expo's push service rejects the all-zero UUID, `getExpoPushTokenAsync`
throws, `registerForPushNotifications` returns
`{ ok: false, reason: 'error' }`, and the user gets zero notifications
for the entire trip — the single most-trusted communication channel
during dogfood. There is no in-app error surface for this — the catch
at `Travel App/utils/push.ts:206-209` only `console.warn`s.

**Repro / deterministic test idea:**

1. Leave `Travel App/app.json:54` at the placeholder.
2. Build with the release leak-guards satisfied (correct mock/skip/Clerk).
3. Cold-launch on a real device, sign in.
4. Observe `[push] registration failed` in device logs; observe that
   `POST /api/users/{id}/devices` is never hit (no row appears in the
   backend `push_devices` table).
5. Trigger a server-side push (e.g. invite acceptance) — never arrives.

**Suggested fix direction:** add a fourth assertion next to the existing
leak guards. The cheapest is a startup-time check that compares
`Constants.expoConfig?.extra?.eas?.projectId` against the placeholder
and throws in `!__DEV__ && !USE_MOCK && !SKIP_AUTH` mode — same shape
as the Clerk-key assertion already there. Mirror the same check inside
`registerForPushNotifications` so even a TestFlight build that somehow
boots returns a structured `{ ok: false, reason: 'misconfigured_project_id' }`
that the caller can log or toast.

**Confidence:** High. The wiring through `expo-notifications` is
direct; the only uncertainty is whether the placeholder ever ships
(today the preflight catches it — but the preflight requires `eas-cli`
on PATH, which `dogfood-readiness.md:26` reports it isn't).

---

### [P0] — Five real-only error paths the mock never exercises will hit a tester on first dogfood traffic

**References:**
- `Travel App/utils/api/interface.ts:976-979` — `createInvite` "Throws an `APIError` with status 409 and `detail.error === 'trip_needs_substance'`".
- `Travel App/utils/api/mock.ts:2612-2626` — mock `createInvite` always returns success; no substance gate.
- `Travel App/utils/api/interface.ts:283-292` — `sendMessage` "throws `APIError` with `kind='in_flight'` (HTTP 409) if the original is still running".
- `Travel App/utils/api/mock.ts:782-795` — mock `sendMessage` always returns a random canned reply; ignores `options.idempotencyKey`.
- `Travel App/utils/sse.ts:200-216` — real-mode SSE path classifies 409 → `in_flight`, 504 → `timeout`.
- `Travel App/hooks/useConciergeChat.ts:652-705` — UI-side `in_flight` recovery with exponential-backoff history poll (7 attempts over ~44s); never exercised by mock.
- `Travel App/utils/sse.ts:229-256` — 45s inactivity reconnect + silent retry-once with the same idempotency key.
- `Travel App/utils/api/http.ts:391-469` — `_uploadFile` honours an external `AbortSignal` (used by photo + receipt upload on `AppState=background`).
- `docs/audits/pre-dogfood-2026-05/dogfood-readiness.md:147-173` — open P1 about same-user retry returning `410` from `acceptInvite`; mock returns success unconditionally.

**Why it matters to a real tester:** the dogfood readiness doc reports
"`make mock-real-parity` PASS — 7 suites, 93 tests passed", but the
parity suite is **response-shape parity, not behavior parity**. The
mock implementations above all short-circuit to a success literal. The
moment a real tester hits any of the conditions — empty trip on first
invite (substance gate), a flaky cellular send that triggers an
idempotent retry, a successful join whose 200 was dropped on the wire,
a 45-second LLM stall mid-stream, an upload that's still in flight when
the user backgrounds the app — they exercise code paths that the entire
preflight + test suite has never observed. Each of these has explicit,
sophisticated UI handling (e.g. `useConciergeChat.ts:665-704`'s
in-flight backoff poll), and a regression in any of them would surface
only in real mode.

**Repro / deterministic test idea:** add ONE mock-mode integration
test per path that flips on a hidden `EXPO_PUBLIC_MOCK_FAULTS` env to
trigger:

```ts
// Travel App/__tests__/integration/mock-fault-paths.test.ts (proposed)
test('createInvite mock surfaces trip_needs_substance on empty trip', async () => {
  process.env.EXPO_PUBLIC_MOCK_FAULTS = 'invite_substance';
  await expect(mockApi.createInvite('trip-empty')).rejects.toThrow(/trip_needs_substance/);
});
test('sendMessage mock with same idempotencyKey surfaces in_flight', async () => { /* ... */ });
test('acceptInvite mock with prior consume returns membership, not 410', async () => { /* ... */ });
```

The `_MOCK_LATENCY_MS` knob at `Travel App/utils/api/mock.ts:191-198`
is the right precedent for an env-gated fault-injection mode: opt-in,
test-only, and visible in the file you're already reading.

**Suggested fix direction:** add a `MOCK_FAULTS` switchboard to
`utils/api/mock.ts` — a parsed-once env var like
`EXPO_PUBLIC_MOCK_FAULTS=invite_substance,sse_stall,upload_bg_abort,accept_consumed,sendmessage_inflight`
— and have the five mock methods consult it. Then add one regression
test per fault to `__tests__/integration/` and gate the dogfood call
on that suite green. This is the minimum surface that converts the
parity claim from "shapes match" to "the UI's documented error-handling
paths are exercisable from mock".

**Confidence:** High. Each of the five is an explicit contract in
the interface docstring or in an audit ticket; none of them is a
hypothetical.

---

### [P1] — `app.json` carries the `applinks:travelagent.app` Universal Link but no fallback for the preview backend, so preview-build deep links break silently

**References:**
- `Travel App/app.json:19-22` — `ios.associatedDomains = ["applinks:travelagent.app"]`.
- `Travel App/app.json:31-47` — Android intent filter is `host=travelagent.app` only.
- `Travel App/app.json:10` — `scheme: "guide"` (the custom scheme works for in-app shares).
- `Travel App/eas.json:18-27` — preview profile points at `travel-agent.fly.dev` for HTTP, but the AASA is on travelagent.app.
- `Travel App/app/_layout.tsx:164-167` — `invite/[slug]` stack screen exists, but it depends on the deep link resolving in the first place.

**Why it matters to a real tester:** the preview build is the
"test on a device before the custom domain is wired" profile
(`docs/Owner Action Items.md:43-44`). Testers will tap invite URLs from
SMS / iMessage / Slack — but the share URL format minted by
`utils/api/mock.ts:2621` and (presumably) the backend is
`https://travelagent.app/invite/<token>`. On the preview build, the
phone's Universal-Link verifier hits `travelagent.app/.well-known/apple-app-site-association`
which is currently 000 (DNS / no service). Apple silently falls back to
opening Safari, which then 000s as well — the user sees a broken page
and the app never receives the deep link. A custom-scheme link
(`guide://invite/<token>`) would work, but invite URLs aren't minted
that way.

**Repro / deterministic test idea:** on the preview build, send a
copy of the invite URL via iMessage to the test device; tap it; observe
that Safari opens (rather than the app) and the page fails to load.
Then send `guide://invite/<token>` via the same path; observe the app
opens the modal correctly.

**Suggested fix direction:** until the custom domain is live, either
(a) configure a second associatedDomain pointed at the preview backend
(`applinks:travel-agent.fly.dev` or whatever host the preview
actually uses) AND have the backend serve `/.well-known/apple-app-site-association`
under that host, or (b) document that preview builds get their invite
URLs via the custom scheme only (the in-app share sheet can prefer
`guide://invite/<token>` when `BASE_URL` doesn't match `travelagent.app`).
Option (a) is more faithful to the dogfood scenario; option (b) is the
zero-DNS-work mitigation.

**Confidence:** Medium. The exact share-URL format minted by the backend
is one curl away (`POST /api/trips/{tripId}/invites`) but I didn't
exercise it — the mock returns `travelagent.app/...` so the assumption
holds for at least that side.

---

### [P1] — SSE 401 path fires `redirectToSignIn()` AND surfaces an HTTP-401 error to the UI callback simultaneously

**References:**
- `Travel App/utils/sse.ts:194-216` — on non-OK response, calls `redirectToSignIn()` then immediately also `callbacks.onError(`HTTP 401: …`, 'error')` and `callbacks.onDone()`.
- `Travel App/utils/api/http.ts:326-350` — REST-side counterpart does NOT surface a separate 401 toast: it redirects then throws an `APIError` that the React Query layer interprets via `shouldRetryQuery`.
- `Travel App/hooks/useConciergeChat.ts:707-720` — `onError` in real mode sets `streamError` (rendered as an `ErrorBanner`) and fires a `haptic.error()`.

**Why it matters to a real tester:** when a token-expired SSE call
fires (the most common cause of a mid-session 401 in normal use), the
user sees the app navigate to sign-in AND a scary "HTTP 401: …" error
banner flash on the previous screen, plus an error haptic. The redirect
is correct; the banner + haptic on the chat screen they just left is
noise that signals "something broke" right as they're about to be told
to sign in again. In the REST path, the equivalent 401 is silent
because the `APIError` is caught by React Query and the redirect is the
only user-visible effect.

**Repro / deterministic test idea:** in `__tests__/utils/sse.test.ts`,
add a case where the mocked fetch returns `{ status: 401 }`; assert
that `onError` is NOT called (or is called with a distinguishable
`kind: 'unauthorized'` that callers can swallow) and that
`onDone` is called. Mirror the REST-side behavior.

**Suggested fix direction:** in `utils/sse.ts:194-216`, special-case
401 in the same way the http path does — after `await redirectToSignIn()`,
return without firing `onError`/`onDone`, or add an
`kind: 'unauthorized'` to the union and have the chat hook
(`hooks/useConciergeChat.ts:652`) swallow it without setting
`streamError` or firing the error haptic.

**Confidence:** High. The branch is right there; the only judgement is
whether to be silent or to add a new `'unauthorized'` kind.

---

### [P1] — `createTrip` from a destination card still discards the `destination` even though the backend just gained that field

**References:**
- `Travel App/context/TripContext.tsx:302-304` (per `dogfood-readiness.md:178-181`) — sends only `{ created_by, title }`.
- `Travel App/app/(tabs)/discover/index.tsx:457-479` — `handlePlanSimilar` calls `createTrip({ title: destination, destination })` but the second field is dropped on the way to the backend.
- `docs/openapi.json` (uncommitted local diff) — `CreateTripRequest.properties.destination` was just added (a string with maxLength 200) — see `git diff docs/openapi.json` from workspace root.
- `Travel App/utils/api/http.ts:545-554` — `createTrip` ships the body unmodified; the surface is fine, the caller is the gap.
- `Travel App/utils/api/mock.ts:379-405` — mock honours `body.destination` into `trip_summary.destination` already.

**Why it matters to a real tester:** the prior audit's P1 is now half-fixed
— the backend snapshot grew the field, but `TripContext.createTrip`
still flattens it out. So in real mode, "Plan similar to Lisbon" creates
a trip whose `trip_summary.destination` is the optimistic-only value
(`TripContext.tsx:262-279`) and gets dropped on the next trips refetch,
disabling the "For this trip" preview rail
(`components/for-this-trip/ForThisTripPreview.tsx:68-107`). In mock mode
it works fine — so the regression won't surface until real-backend dogfood.
This finding is the "mock hides a real bug" pattern in concentrated form.

**Repro / deterministic test idea:** real-backend integration test that
calls `handlePlanSimilar("Lisbon")`, awaits the trips-list query
invalidation, then asserts the resulting trip row has
`trip_summary.destination === "Lisbon"` (or the slugified equivalent
that powers `ForThisTripPreview`).

**Suggested fix direction:** update `TripContext.tsx:302-304` to thread
the `destination` field through to `api.createTrip` once the backend
schema diff is committed (the snapshot is currently modified but not
staged — see workspace `git status`). Stage that openapi.json change
together with the frontend fix so the contract-check stays green.

**Confidence:** High. Verified by reading both call sites; the open
question is only whether the destination field has been merged to
`main` yet.

---

### [P1] — Hand-written `Itinerary` / `ItineraryDay` / `ItineraryBlock` interfaces in `types/itinerary.ts` duplicate the canonical generated types

**References:**
- `Travel App/types/itinerary.ts:11-50` — three hand-written interfaces (`Itinerary`, `ItineraryDay`, `ItineraryBlock`).
- `Travel App/utils/api/types.ts:182-200` — canonical `APIItineraryDay` and `APIItineraryBlock` derived from `components['schemas']['ItineraryDayOut']` and `ItineraryBlockOut`.
- `Travel App/CLAUDE.md:96-105` — workspace rule "Never hand-write TypeScript types that duplicate Pydantic models — generate them".

**Why it matters to a real tester:** the workspace rule against
hand-written types exists exactly because pre-2026-05-18 the
hand-written `Trip` interface drifted from the backend and the type
checker stayed green while the runtime broke (audit-fe pass 1 P0). The
3 itinerary interfaces in `types/itinerary.ts` are currently dead code
— ripgrep shows zero imports outside the file itself — but the
docstring explicitly markets them as "kept hand-written until the
backend exposes equivalent Pydantic models", which is no longer true:
`ItineraryDayOut` and `ItineraryBlockOut` ARE in the snapshot. The
file is a trap for the next contributor who searches for `ItineraryBlock`
and imports it.

**Repro / deterministic test idea:** none required — verified by
ripgrep: `rg "import.*types/itinerary" Travel\ App` → 0 hits.

**Suggested fix direction:** delete the hand-written interfaces in
`types/itinerary.ts`, leaving only `BlockTransition` (already re-exported
from the schema). Replace the docstring with a pointer to
`APIItineraryDay` / `APIItineraryBlock` in `utils/api/types.ts`. Add
an `eslint-no-restricted-types` rule (or a `scripts/api-coverage-check.py`
sibling) that fails CI if any new hand-written interface duplicates a
backend schema name.

**Confidence:** High. Verified by reading both files + ripgrep.

---

### [P2] — `ImagePicker.MediaTypeOptions.Images` is deprecated in expo-image-picker; the chat composer still uses it while the photos screen has migrated

**References:**
- `Travel App/components/chat/ComposerBar.tsx:181` — `mediaTypes: ImagePicker.MediaTypeOptions.Images`.
- `Travel App/app/(tabs)/trips/[tripId]/photos.tsx:104-109` — already migrated to `mediaTypes: ['images']`.
- `node_modules/expo-image-picker/src/utils.ts:19` — deprecation log: `MediaTypeOptions have been deprecated. Use MediaType or an array of MediaType instead.`

**Why it matters to a real tester:** the deprecated path still works
on Expo SDK 55, but every photo attach in chat will log a yellow-box
deprecation warning that bug reports will surface as a regression. When
SDK 56 lands and the option is removed, the composer's image attach
flow silently fails (the picker returns `result.canceled = true` or
throws) and the user can't attach photos to chat.

**Repro / deterministic test idea:** tap the image attach button in
the composer with photo access granted; observe Metro logs for the
deprecation warning.

**Suggested fix direction:** change `ComposerBar.tsx:181` to
`mediaTypes: ['images']` matching `photos.tsx`. One-line change.

**Confidence:** High.

---

### [P2] — `OfflineBanner` reports network connectivity but cannot detect "backend hostname doesn't resolve"

**References:**
- `Travel App/components/ui/OfflineBanner.tsx:20-33` — renders solely from `useNetworkState().isConnected`.
- `Travel App/hooks/useNetworkState.ts:25-44` — `isConnected` reflects OS-level link state, not backend reachability.
- `Travel App/utils/api/http.ts:360-375` — `APIError` with `kind: 'network'` is the only signal the UI gets when the host is unreachable.

**Why it matters to a real tester:** when `EXPO_PUBLIC_API_URL` points
at a host that doesn't resolve (the current state — see top P0), the
device is online, `OfflineBanner` stays hidden, and every query throws
`APIError { kind: 'network', detail: 'Network error: /api/me (...)' }`.
Toasts fire per surface, but the user has no global "you can't reach
the backend" signal — they see scattered failure messages that look
like individual screen bugs. The runtime backstop is the
`_resolveBaseUrl` boot crash in production builds without a URL set,
but a URL that's set but unreachable is the more likely dogfood failure
mode.

**Repro / deterministic test idea:** set
`EXPO_PUBLIC_API_URL=https://travelagent.app` in Expo Go (where the
runtime guard doesn't fire), boot the app, observe that `OfflineBanner`
never renders despite every API call failing with `kind: 'network'`.

**Suggested fix direction:** wire a periodic /health probe (or
piggyback on the first `getMe` call) and surface a distinct banner
state: "online but can't reach Vesper — we're investigating". Keep
`OfflineBanner` for OS-level offline; add an `BackendUnreachableBanner`
that arms after N consecutive `kind: 'network'` errors and disarms
after one successful authed call. Same pattern as
`http.ts:354`'s `_clearAuthRedirectGuard` after a successful authed
request.

**Confidence:** Medium. Sketched the wiring; the exact UX hierarchy
between the two banners is a product call.

---

### [P2] — `_resolveBaseUrl` allows a mock-mode release build to silently target `http://localhost:8000`

**References:**
- `Travel App/utils/api/http.ts:101-124` — production-build guard is gated on `!useMock`; mock-mode release builds fall through to `http://localhost:8000`.
- `Travel App/app/_layout.tsx:98-106` — separate runtime guard already forbids `USE_MOCK=true` in release builds, but it runs AFTER `_resolveBaseUrl` (which executes at module load — line 126 `export const BASE_URL = _resolveBaseUrl()`).

**Why it matters to a real tester:** the asymmetry note in
`http.ts:111-114` is correct that mock-mode never hits `httpApi`, BUT
the comment also acknowledges the guard is "INCOMPLETE". If anything
in the runtime cascade fires `httpApi` before the leak guard throws
(e.g. an eager import in `data/` evaluated by Metro before `_layout.tsx`
renders, or a future code path that prefetches before render), a
mock-mode release build would briefly target localhost and silently
fail. The defense-in-depth fix is one extra branch.

**Repro / deterministic test idea:** none for current code (the leak
guard catches it first), but: import `BASE_URL` into a module that
side-effects at module-load time, set `EXPO_PUBLIC_USE_MOCK_API=true`
in a release-built bundle, observe `BASE_URL === 'http://localhost:8000'`.

**Suggested fix direction:** make `_resolveBaseUrl`'s prod-path check
mirror the runtime leak guard: in `!__DEV__`, throw unless
`EXPO_PUBLIC_API_URL` is set, period. The mock-mode-release case
already throws elsewhere; this aligns both layers on the same rule.

**Confidence:** Medium. Risk is theoretical today.

---

### [TECH-DEBT] — `mock.getHomeConversation` returns a stable `home-convo-mock` id but never wires the conversation through `_userId`

**References:**
- `Travel App/utils/api/mock.ts:3021-3024` — returns `{ conversation_id: 'home-convo-mock', trip_id: null }` unconditionally.
- `Travel App/utils/api/http.ts:1579-1584` — real impl reshapes the backend's `{id, title, created_at}` and binds it to the user.

**Why it matters to a real tester:** mock mode shows every user the
same Home conversation id, so two mock-mode signed-in identities
(e.g. testing UserContext switch) see colliding conversation state —
not a dogfood-blocker, but exactly the kind of state-coherence drift
the audit flagged as one of the four dogfood risk surfaces.

**Suggested fix direction:** make the mock key the id by `userId`
(`home-convo-${userId}`) so the parity with the real backend's
per-user binding is preserved.

**Confidence:** Low. Worth fixing for parity hygiene but not gating.

---

### [TECH-DEBT] — Mock-mode artificial latency is 120ms uniform; real backend p95 is 600-1500ms with multi-second outliers on cold start

**References:**
- `Travel App/utils/api/mock.ts:191-198` — `_MOCK_LATENCY_MS = 120` (overrideable via env).
- `Travel App/utils/api/http.ts:188` — `DEFAULT_TIMEOUT_MS = 15_000` — real-mode tolerance is 100× the mock latency.
- `Travel App/utils/api/interface.ts:976-979` — `createInvite` comment "Server runs a Haiku snapshot generation as part of this call, so it can take 1-2s — show a spinner".

**Why it matters to a real tester:** every spinner / optimistic-UI
state was tuned against 120ms. Long-running real-backend operations
(`createInvite`, `narrateConcierge`, the SSE turn) feel laggy in a way
the dev never sees. Compounded with the cold-Fly machine on first
request after auto-stop (when that's eventually enabled —
`fly.toml:99` keeps it off for dogfood, which mitigates this), the
disparity is jarring.

**Suggested fix direction:** flip `EXPO_PUBLIC_MOCK_LATENCY_MS=800` in
the development EAS profile (`eas.json:13-16`) so devs feel the real
shape of network latency during routine work; document the override in
the README. Already a one-line env tweak — the plumbing is built.

**Confidence:** Medium.

---

### [TECH-DEBT] — `Sentry` plugin loaded at app.json:90 even when consent is off; lazy-require in `observability.ts` is partial protection

**References:**
- `Travel App/app.json:90` — `"@sentry/react-native"` config plugin.
- `Travel App/utils/observability.ts:72-103` — runtime `initObservability` is consent + DSN gated and lazy-`require()`s the SDK.
- `Travel App/app/_layout.tsx:40-47` — `initObservability` is called at module scope; the gate is `!__DEV__ && !USE_MOCK && (EXPO_PUBLIC_CRASH_REPORTING_CONSENT === 'true')`.

**Why it matters to a real tester:** the consent gate is a build-time
env flag, not a per-user runtime preference (`app/_layout.tsx:38-46`'s
comment explicitly flags this). On a release build with crash reporting
consented at build time, every user has consented — there's no in-app
opt-out and no way to revoke. The privacy promise in the audit-readiness
doc ("Sentry behind consent") is satisfied at the BUILD level only.

**Suggested fix direction:** wire `initObservability` to read a
per-user `APIPrivacyPreference` (the schema already supports custom
dimension keys — `/api/users/{userId}/privacy/{dimensionKey}`) instead
of an env flag. Re-init or `Sentry.close()` on toggle. Document the
lifecycle in `observability.ts` so the next contributor doesn't ship a
build with consent baked in.

**Confidence:** Medium.

---

## Known / Accepted

| Item | Reference | Status |
|---|---|---|
| `dogfood-readiness.md` P0: release backend hosts unreachable | Audit doc:61-93 | **OPEN** — repeated as P0 above with the precise diff. |
| `dogfood-readiness.md` P0: EAS production projectId placeholder + preflight cannot run | Audit doc:95-117 | **OPEN** — repeated above; added the `utils/push.ts` wiring as a second blast radius. |
| `dogfood-readiness.md` P1: same-user invite-accept race returns 410 | Audit doc:147-173 | **OPEN** — backend-side fix tracked there; mock-side parity captured in the P0 "five real-only error paths" finding above. |
| `dogfood-readiness.md` P1: destination-created trips lose destination after refetch | Audit doc:175-199 | **PARTIALLY-FIXED** — backend openapi snapshot grew the `destination` field (uncommitted in `docs/openapi.json`); frontend `TripContext.createTrip` still drops it. Captured as P1 above. |
| `make api-coverage-check` 175/175 unique frontend HTTP call sites covered | Audit doc:23 | **PASS** — confirmed; nothing new in this audit. |
| `make mock-real-parity` 7 suites / 93 tests | Audit doc:24 | **PASS for shapes, INCOMPLETE for behavior** — the P0 above documents the five behavior-parity gaps the suite doesn't catch. |
| Production-build leak guard (USE_MOCK / SKIP_AUTH / Clerk key) | `Travel App/app/_layout.tsx:98-115` | **WORKING** — verified by reading; complemented by a fourth-projectId guard suggestion in the P0 above. |
| `OfflineBanner` + `useOfflineGate` + mutation refetch-on-reconnect | `Travel App/app/_layout.tsx:76-78`, `hooks/useNetworkState.ts:75-93` | **PRESENT** — only gap is "online but backend unreachable", flagged as P2. |
| SSE 45s inactivity reconnect + single-flight 401 redirect | `Travel App/utils/sse.ts:235-256`, `Travel App/utils/api/http.ts:128-185` | **WORKING** — only behavioural nit is double-firing onError on 401 (P1). |
| Per-permission rationale sheet + Settings recovery toast | `Travel App/components/ui/PermissionRationale.tsx`, `Travel App/app/(tabs)/trips/[tripId]/photos.tsx:90-101`, `Travel App/components/chat/ComposerBar.tsx:170-179`, `Travel App/app/(tabs)/concierge/chat.tsx:762-803` | **WORKING** — camera, photos, location, microphone (`MicPrivacyDisclosure.tsx:117-124`), and notifications (`utils/push.ts:138-156`) all have either rationale-first prompts or Settings-recovery affordances. The only deprecated API usage is the P2 above. |
| Mock-mode `Sentry` lazy-require pattern | `Travel App/utils/observability.ts:75-77` | **WORKING** — verified mock-mode doesn't load `@sentry/react-native`'s native graph. |
| `__DEV__`-gated `console.error` in `ErrorBoundary.componentDidCatch` | `Travel App/components/ErrorBoundary.tsx:45-60` | **WORKING** — forwards to `reportError` which is a no-op until consent + DSN. |
