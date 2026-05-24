# State Polish Audit: Empty, Loading, Error, Offline

## Summary

Runtime screenshots were unavailable for this pass. `Travel App` still has a `web` script, but `react-native-web` is not installed in `package.json` or `node_modules`, matching the earlier audit note that Expo web cannot boot cheaply. I performed a static state-coverage audit from code.

The app has better state primitives than the earlier polish memo suggested: `EmptyState`, `ErrorState`, `Skeleton`, `OfflineBanner`, permission rationales, and several screen-level retry branches are already in place. The remaining dogfood risk is uneven adoption. Notifications, Discover, Plan, Photos, Invite, and chat have thoughtful branches; Changes, parts of Trip Home, Trip Settings, Concierge Home, and some stale/partial-data paths can still collapse real backend trouble into a calm but misleading "nothing here" or "tap did nothing" feeling.

No P0s found. The strongest P1s are about dogfood trust: users need to know when Vesper's action log, trip creation, or mutations failed, especially on flaky internal builds.

## States Reviewed

- Empty: Trips, Concierge history, Discover feeds, Near Me, Notifications, Photos, Map, Memory, Expenses, Saved Venues, Changes.
- Loading: shared skeleton primitives, chat history, list screens, invite landing, trip plan, memory, photos, notification settings.
- Error and retry: query failures, streaming/send failures, invite token failures, notification refresh failures.
- Offline: root offline banner, chat composer gate, mutation gating helper.
- Permission denied: notifications, location/Near Me, geofence prompts, photos, mic disclosure.
- Partial and stale data: notifications, Discover, Expenses, Home feed, trip photos, saved venues.
- Disabled and in-flight: create trip, send, upload, invite, revoke, settings, leave trip, radio options.

## Findings

### P1 - Changes timeline can misreport load failure as "No changes yet"

`app/(tabs)/trips/[tripId]/changes.tsx` calls `useTripPlanState(tripId)` and derives `changes` from `planStateQuery.data?.recent_changes ?? []`, but it never renders `planStateQuery.isLoading`, `planStateQuery.error`, or retry UI. The empty branch says "No changes yet" whenever `grouped.length === 0`.

Evidence: `Travel App/app/(tabs)/trips/[tripId]/changes.tsx:62`, `Travel App/app/(tabs)/trips/[tripId]/changes.tsx:63`, `Travel App/app/(tabs)/trips/[tripId]/changes.tsx:85`, `Travel App/app/(tabs)/trips/[tripId]/changes.tsx:86`, `Travel App/app/(tabs)/trips/[tripId]/changes.tsx:89`. The hook can return real error state through `useData`: `Travel App/data/planState.ts:84`.

Dogfood impact: after Vesper edits a plan, the audit trail is a trust surface. A network failure reading as "Vesper has made no changes" is worse than a normal empty state.

### P1 - Concierge Home trip creation lacks disabled/error/retry affordances

Trips list has an in-flight guard, toast on failure, and disabled/busy CTA while `createTrip` runs. Concierge Home's `handleNewChat` awaits `createTrip()` and routes, but has no local `creating` state, no disabled state for suggestions/search submit, and no error surface if `createTrip` rejects.

Evidence for guarded version: `Travel App/app/(tabs)/trips/index.tsx:78`, `Travel App/app/(tabs)/trips/index.tsx:81`, `Travel App/app/(tabs)/trips/index.tsx:88`, `Travel App/app/(tabs)/trips/index.tsx:90`, `Travel App/app/(tabs)/trips/index.tsx:175`, `Travel App/app/(tabs)/trips/index.tsx:189`, `Travel App/app/(tabs)/trips/index.tsx:192`. Evidence for unguarded Concierge Home: `Travel App/app/(tabs)/concierge/index.tsx:43`, `Travel App/app/(tabs)/concierge/index.tsx:44`, `Travel App/app/(tabs)/concierge/index.tsx:45`, `Travel App/app/(tabs)/concierge/index.tsx:48`, `Travel App/app/(tabs)/concierge/index.tsx:52`, `Travel App/app/(tabs)/concierge/index.tsx:177`, `Travel App/app/(tabs)/concierge/index.tsx:180`.

Dogfood impact: the first-week "ask Vesper anything" path is core identity. On backend 500/offline, it can feel like the product ignored the tap.

### P1 - Offline banner overpromises; mutation gates are not broadly applied

The root offline banner says "changes will retry when you reconnect," but the reusable `useOfflineGate` helper is only defined, not broadly adopted. ComposerBar separately blocks sends when offline, but many other mutation surfaces still fire and then rely on a toast/rollback after failure.

Evidence: `OfflineBanner` copy at `Travel App/components/ui/OfflineBanner.tsx:20`, `Travel App/components/ui/OfflineBanner.tsx:21`, `Travel App/components/ui/OfflineBanner.tsx:30`; mounted at `Travel App/app/_layout.tsx:187`, `Travel App/app/_layout.tsx:188`. `useOfflineGate` is defined at `Travel App/hooks/useNetworkState.ts:75`, `Travel App/hooks/useNetworkState.ts:83`, `Travel App/hooks/useNetworkState.ts:85`, but ComposerBar uses direct `useNetworkState` gating at `Travel App/components/chat/ComposerBar.tsx:211`, `Travel App/components/chat/ComposerBar.tsx:222`, `Travel App/components/chat/ComposerBar.tsx:223`. Ungated examples include trip cadence update `Travel App/app/trip-settings/index.tsx:106`, `Travel App/app/trip-settings/index.tsx:109`, invite/revoke surfaces `Travel App/app/trip-info/index.tsx:330`, `Travel App/app/trip-info/index.tsx:354`, and photo uploads `Travel App/app/(tabs)/trips/[tripId]/photos.tsx:112`, `Travel App/app/(tabs)/trips/[tripId]/photos.tsx:139`.

Dogfood impact: flaky office/subway testing will expose inconsistent behavior: chat calmly refuses to send, while settings/photos/invites may spin, rollback, or toast later.

### P2 - Stale-data signaling is inconsistent outside Notifications

Notifications has the right stale-data pattern: keep cached rows visible and show an inline "Couldn't refresh. Tap to retry" banner. Discover and Expenses intentionally hide errors when cached data exists, but do not show an equivalent stale-data banner, so users cannot tell whether they are seeing fresh recommendations/settlements.

Evidence for good pattern: `Travel App/app/notifications/index.tsx:298`, `Travel App/app/notifications/index.tsx:302`, `Travel App/app/notifications/index.tsx:305`, `Travel App/app/notifications/index.tsx:310`. Evidence for masked stale errors: `Travel App/data/discover.ts:575`, `Travel App/data/discover.ts:578`, `Travel App/data/discover.ts:579`, `Travel App/data/discover.ts:580`, `Travel App/data/discover.ts:581`; `Travel App/app/trip-expenses/index.tsx:158`, `Travel App/app/trip-expenses/index.tsx:164`.

Dogfood impact: Discover, Expenses, and trip surfaces are exactly where early backend changes will be uneven. Calm stale banners preserve trust without blocking use.

### P2 - Trip Home can silently drop Days when itinerary fails

Trip Home uses the legacy `useItinerary(tripId)` overload, which returns `data ?? []` and does not expose `isError` or retry. The Days section renders skeletons only while `homeReady` is false; once home feed has loaded or errored, an empty `days` array simply removes the Days section.

Evidence: legacy overload at `Travel App/data/itinerary.ts:29`, return shape at `Travel App/data/itinerary.ts:44`, `Travel App/data/itinerary.ts:48`; Trip Home consumption at `Travel App/app/(tabs)/trips/[tripId]/index.tsx:76`; Days rendering at `Travel App/app/(tabs)/trips/[tripId]/index.tsx:270`, skeleton gate at `Travel App/app/(tabs)/trips/[tripId]/index.tsx:286`, `Travel App/app/(tabs)/trips/[tripId]/index.tsx:293`.

Dogfood impact: the trip workspace can look thin or unfinished when only itinerary fetch fails. This is likely in real-mode dogfood because Plan v2, Home cards, and itinerary are separate read models.

### P2 - Trip Settings ignores notification preference load errors

`useNotificationPreferences` returns `error`, but Trip Settings destructures only `prefs`, `tripOverride`, `loading`, and `setCadenceOverride`. Once loading ends with an error, the UI falls into the normal controls branch with `prefs` null and enabled cadence options.

Evidence: hook exposes error at `Travel App/hooks/useNotificationPreferences.ts:31`, `Travel App/hooks/useNotificationPreferences.ts:35`, `Travel App/hooks/useNotificationPreferences.ts:146`, `Travel App/hooks/useNotificationPreferences.ts:150`; screen ignores it at `Travel App/app/trip-settings/index.tsx:58`; render branch at `Travel App/app/trip-settings/index.tsx:121`, `Travel App/app/trip-settings/index.tsx:125`, `Travel App/app/trip-settings/index.tsx:131`, fallback copy at `Travel App/app/trip-settings/index.tsx:143`, `Travel App/app/trip-settings/index.tsx:146`, enabled controls at `Travel App/app/trip-settings/index.tsx:149`, `Travel App/app/trip-settings/index.tsx:156`.

Dogfood impact: users may change per-trip notification settings while the app has not actually loaded the global/trip baseline.

### P2 - Permission recovery is strong for location/notifications, weaker for photo/mic surfaces

Near Me and Notifications keep denied states visible with Settings recovery. Photo add flows often rely on a transient toast with a Settings action, and the Trip Album empty state does not persistently reflect "photo access is off." Mic disclosure uses an Alert for denied settings recovery, which is recoverable but visually outside Vesper's calm state language.

Evidence for stronger patterns: Near Me denied panel `Travel App/app/(tabs)/discover/index.tsx:874`, `Travel App/app/(tabs)/discover/index.tsx:876`, `Travel App/app/(tabs)/discover/index.tsx:886`, `Travel App/app/(tabs)/discover/index.tsx:892`; notifications denied banner `Travel App/app/notifications/index.tsx:277`, `Travel App/app/notifications/index.tsx:280`, `Travel App/app/notifications/index.tsx:288`, `Travel App/app/notifications/index.tsx:293`. Weaker photo/mic recovery: photos toast `Travel App/app/(tabs)/trips/[tripId]/photos.tsx:92`, `Travel App/app/(tabs)/trips/[tripId]/photos.tsx:97`, `Travel App/app/(tabs)/trips/[tripId]/photos.tsx:98`; album empty state has only normal add/find CTAs at `Travel App/app/(tabs)/trips/[tripId]/photos.tsx:346`, `Travel App/app/(tabs)/trips/[tripId]/photos.tsx:356`, `Travel App/app/(tabs)/trips/[tripId]/photos.tsx:362`, `Travel App/app/(tabs)/trips/[tripId]/photos.tsx:371`; mic Alert at `Travel App/components/voice/MicPrivacyDisclosure.tsx:119`, `Travel App/components/voice/MicPrivacyDisclosure.tsx:122`, `Travel App/components/voice/MicPrivacyDisclosure.tsx:127`.

Dogfood impact: photo upload and voice are high-emotion moments. Recovery should remain visible after the toast disappears.

### P2 - Brand-critical chat loading still uses generic bubble skeletons

Private Vesper chat correctly routes AI messages to `PrivateVesperNote`, but initial history loading still renders `SkeletonMessage` bubble rows. The skeleton primitive itself is warm, but the shape contradicts the private "envelope" substrate and makes first-load private chat feel like ordinary messaging.

Evidence: private note routing at `Travel App/app/(tabs)/concierge/chat.tsx:74`, `Travel App/app/(tabs)/concierge/chat.tsx:77`, `Travel App/app/(tabs)/concierge/chat.tsx:78`; private chat loading branch at `Travel App/app/(tabs)/concierge/chat.tsx:886`, `Travel App/app/(tabs)/concierge/chat.tsx:888`, `Travel App/app/(tabs)/concierge/chat.tsx:890`; generic skeleton bubble implementation at `Travel App/components/ui/Skeleton.tsx:174`, `Travel App/components/ui/Skeleton.tsx:177`, `Travel App/components/ui/Skeleton.tsx:178`, `Travel App/components/ui/Skeleton.tsx:261`, `Travel App/components/ui/Skeleton.tsx:266`.

Dogfood impact: not broken, but it undercuts the core product relationship during the exact moment the user is waiting for Vesper.

## Evidence

- Runtime inspection: not available in this pass because Expo web dependencies are absent (`react-native-web` missing). No simulator/device output was attached.
- Strong existing state primitives:
  - `EmptyState`: `Travel App/components/ui/EmptyState.tsx:20`, `Travel App/components/ui/EmptyState.tsx:28`, `Travel App/components/ui/EmptyState.tsx:60`.
  - `Skeleton`: `Travel App/components/ui/Skeleton.tsx:32`, `Travel App/components/ui/Skeleton.tsx:43`, `Travel App/components/ui/Skeleton.tsx:85`, `Travel App/components/ui/Skeleton.tsx:146`.
  - `ErrorState`: `Travel App/components/ui/ErrorState.tsx:42`, `Travel App/components/ui/ErrorState.tsx:45`, `Travel App/components/ui/ErrorState.tsx:50`, `Travel App/components/ui/ErrorState.tsx:69`.
  - Root offline awareness: `Travel App/components/ui/OfflineBanner.tsx:20`, `Travel App/app/_layout.tsx:188`.
- Best examples to copy:
  - Notifications first-load, stale refresh, permission denied: `Travel App/app/notifications/index.tsx:277`, `Travel App/app/notifications/index.tsx:298`, `Travel App/app/notifications/index.tsx:361`.
  - Invite loading/network/terminal split: `Travel App/app/invite/[slug].tsx:327`, `Travel App/app/invite/[slug].tsx:369`, `Travel App/app/invite/[slug].tsx:387`, `Travel App/app/invite/[slug].tsx:397`, `Travel App/app/invite/[slug].tsx:408`.
  - Near Me permission/error/empty states: `Travel App/hooks/useNearMe.ts:103`, `Travel App/hooks/useNearMe.ts:111`, `Travel App/hooks/useNearMe.ts:137`, `Travel App/app/(tabs)/discover/index.tsx:847`, `Travel App/app/(tabs)/discover/index.tsx:860`, `Travel App/app/(tabs)/discover/index.tsx:874`, `Travel App/app/(tabs)/discover/index.tsx:895`.

## Suggested Fix Direction

Require this state matrix for dogfood-critical screens:

| Surface | Empty | Loading | Error + retry | Offline/mutation gate | Permission denied | Partial/stale |
|---|---|---|---|---|---|---|
| Trips list | Required | Required | Required | Required for create/invite | N/A | Optional stale banner |
| Concierge home | Required | Required | Required | Required for create/search/suggestion | Voice if used | Conversation list stale banner |
| Private chat | Required for no history | Envelope-shaped skeleton | History + send retry | Required for send/images | Photo/mic/location inline recovery | Streaming partial failure |
| Group chat | Required for new group | Bubble/group skeleton | History + send retry | Required for send/vote/react | Photo if enabled | Streaming partial failure |
| Trip home | Required for no plan/feed | Required | Required per read model | Required for dismiss/capture | N/A | Feed/day stale banners |
| Plan + Changes | Required | Required | Required | Required for undo/revert | N/A | Recent-changes stale banner |
| Discover | Required | Required | Required | Required for plan/invite/save | Location inline recovery | Feed/search stale banners |
| Photos/Memory | Required | Required | Required | Required for upload/learn | Persistent photo access recovery | Partial upload/read warning |
| Expenses | Required | Required | Required | Required for add/settle/delete | Receipt photo recovery | Settlement stale banner |
| Settings | N/A | Required | Required | Required for all saves | Notifications/mic as relevant | Baseline prefs stale warning |

Implementation direction:

- Reuse `ErrorState` and `Skeleton` rather than adding local text-only empties.
- Add a small `StaleBanner`/`RefreshFailedBanner` primitive based on the Notifications pattern.
- Adopt `useOfflineGate` on all user-facing mutations, or change `OfflineBanner` copy so it does not promise retries the surface does not provide.
- Prefer persistent permission-denied panels for core workflows; keep toast actions for secondary affordances.
- Add private-chat-specific skeletons shaped like `PrivateVesperNote`, not bubbles.

## Verification Ideas

- Add mock/real-mode story fixtures or Maestro flows for: first-load skeleton, empty, backend 500, offline send, offline mutation, stale refetch failure, permission denied, retry success.
- Use network toggling on device for the dogfood top five: create trip from Concierge Home, send private chat, open Changes, add photos, settle expense.
- Add static checks for dogfood-critical screens that import a data hook with `error`/`isError` but do not render `ErrorState` or an explicit inline error.
- Add an audit fixture where each major read model succeeds/fails independently: home feed succeeds while itinerary fails, plan succeeds while changes fail, expenses list succeeds while settlement refresh fails.
