---
doc_type: archive
status: archived
owner: founder / engineering
created: 2026-07-09
archived: 2026-07-09
why_new: Move reviewed completed evidence out of the living documentation tree without deleting its historical record.
---

# Onboarding Deep Dive — Current Stack vs Claude Design

> Archived from the living documentation tree on 2026-07-09 during Phase 5 cleanup.

Status: investigation / alignment plan + frontend polish pass  
Date: 2026-06-06  
Primary external artifact: Claude Design bundle `Vesper Onboarding.html`

Second pass implementation note:

- Updated current auth surfaces to use the Claude-derived Vesper voice grammar: mark + mono kicker, warm paper, serif hero, italic support copy, and softer translucent provider buttons.
- Reworked returning-user sign-in specifically against the HTML `SeamReturn` screen: centered welcome-back moment, soft travel wash behind the auth area, provider stack first, and email as the six-digit-code sub-branch.
- Built the signed-out `/onboarding` front door: Claude-style cover, "I already have an account" returning route, fork, lightweight trip-in-mind capture, dreaming taste beats, diary gift, and pre-auth intent storage.
- Wired auth completion to consume saved onboarding intent: trip drafts create a backend trip after Clerk and land in trip chat; dreaming users land in Atlas or Atlas scan depending on the diary choice.
- Updated invite landing to remove the purple hero, lead with an image-backed place invitation, add a read-only "shape so far" timeline, and move the visual tone toward gold/paper/place-first.
- Remaining structural work is deeper fidelity: real place search, real date windows, real invite seeding, richer diary scan progress during auth, and a backend endpoint for non-constraint taste signals.

## Executive Summary

The current product has strong pieces, but they are arranged in the wrong order for the Claude onboarding direction.

Current app behavior is auth-first:

- real mode boots to Clerk sign-in/sign-up unless already authenticated
- email sign-up collects name and email before product value
- OAuth sign-in routes through a safety-chip modal when constraints are not on file
- trip creation, invite joining, and Atlas photo scan are separate authenticated entry points

Claude's design is value-first:

- open with Vesper's voice, not a form
- branch immediately on intent: "a trip in mind" vs "still dreaming"
- ask for auth only after a trip draft exists or a diary is worth keeping
- ask for Photos only as a contextual gift, not as a toll to enter
- invite users see the real trip first, then sign in to join

The strongest implementation path is not a visual skin of the current auth screens. It is a new pre-auth onboarding controller that captures a local draft, then replays it after Clerk auth into the existing backend APIs.

## Claude Design Intent

The bundle README instructs coding agents to read the chat transcript and `Vesper Onboarding.html`, then follow imports. The relevant design files are:

- `/tmp/vesper-onboarding-bundle/x/project/Vesper Onboarding.html`
- `/tmp/vesper-onboarding-bundle/x/project/onboarding-v2-core.jsx`
- `/tmp/vesper-onboarding-bundle/x/project/onboarding-v2-flow.jsx`
- `/tmp/vesper-onboarding-bundle/x/project/onboarding-v2-invite.jsx`
- `/tmp/vesper-onboarding-bundle/x/project/onboarding-v2-seams.jsx`

Core doctrine:

- "Lead with voice. The trip or the diary is the value. Ask last."
- Cover -> Fork -> Branch.
- Trip branch: where, when, who -> sign in to open the trip -> land in trip Vesper chat.
- Dreaming branch: interest, pace -> diary gift -> Photos permission -> sign in while diary constructs -> land in Atlas.
- Decline branch: graceful no-diary sign-in, then Atlas with the door open.
- Invite branch: real trip peek -> auth framed as joining -> shared trip home/chat; diary gift later.
- Returning branch: "I already have an account" bypasses onboarding entirely.

Visual language:

- warm paper, ink, gold/ochre as Vesper-authored signal
- EB Garamond-style serif voice, DM Sans utility text
- no feature tour, no progress gamification, no signup homework
- illustrations/gouache for emotional altitude; not generic cards

## Concrete Frontend Design Translation

This pass is the design-to-app mapping. The important point: we do not need a new brand system. The app already has most of the correct tokens. We need to make onboarding/auth/invite use them with the same grammar as the Claude file.

### Token Mapping

Claude token -> app token:

- `T.bg #EFEAE0` -> `colors.surface.paper` / `colors.atlas.paper`
- `T.bgDeep #E8E2D4` -> `colors.surface.paperDeep`
- `T.cardWarm #FBF7EC` -> `colors.surface.cardWarm`
- `T.cardSoft #F3EEE3` -> `colors.surface.cardSoft`
- `T.ink #1B1714` -> `colors.surface.ink`
- `T.inkSoft #2C2622` -> `colors.surface.inkSoft`
- `T.mute #86807A` -> `colors.surface.mute`
- `T.muteSoft #B5AFA5` -> `colors.surface.muteSoft`
- `T.gold #B0853A` -> `colors.surface.gold`
- `T.goldDeep #8A6628` -> `colors.surface.goldDeep`
- `T.goldSoft #D9BD86` -> `colors.surface.goldSoft`
- `T.hairline rgba(27,23,20,0.10)` -> `colors.surface.hairline`
- `T.hairThin rgba(27,23,20,0.06)` -> `colors.surface.hairThin`
- `OB.blue #3D5066` -> `colors.surface.planningInk`
- `OB.blueDeep #2A384B` -> `colors.surface.planningInkDeep`

Type mapping:

- Claude `EB Garamond` -> app `Newsreader`. The app intentionally uses Newsreader instead of EB Garamond, so we should preserve this rather than import another serif.
- Claude `DM Sans` -> app `DMSans_*`.
- Claude `JetBrains Mono` -> app `JetBrainsMono_500Medium`.

Existing app files already encode this direction:

- `travel-app/constants/colors.ts`
- `travel-app/constants/fonts.ts`
- `travel-app/constants/typography.ts`
- `travel-app/hooks/useAppFonts.ts`

So the frontend work should mostly use existing `colors.surface`, `colors.atlas`, `fontFamily.serif_*`, `fontFamily.sans_*`, `fontFamily.mono`, and `typography.caps*`/`typography.reading*`/`typography.display*` styles.

### Visual Grammar To Carry Over

Use these as acceptance criteria for every onboarding screen:

- Vesper speaks as page prose, not chat bubbles and not marketing copy.
- Every Vesper-authored section starts with a small mark plus a tiny mono caps kicker.
- Hero titles are serif, warm, slightly literary, and often include one italic phrase.
- Options are usually rows, sentence tokens, timelines, or image tiles, not generic rounded cards.
- Gold/ochre means Vesper-authored intelligence or diary value.
- Ink-blue means trip-planning action.
- Purple should not appear in this onboarding flow unless it is the live AI agent surface; the Claude file uses gold/blue, not purple.
- Hairlines should be warm ink hairlines, usually `StyleSheet.hairlineWidth` with `colors.surface.hairline`.
- CTAs are either gold, ink-blue, or translucent/glass. Avoid espresso primary buttons on these screens unless the surface is a generic app setting.
- On image-backed surfaces, use a real/gouache/place image with a dark gradient overlay and light serif type.
- On paper-backed surfaces, use cardless composition first. Cards are allowed for real artifacts: diary preview, itinerary timeline, auth panel, or modal sheet.
- Progress is understated: two taste dots, a developing strip, or a timeline. No wizard bars, feature tours, confetti, or gamified progress.

### Reusable Frontend Atoms To Add

These should live under something like `travel-app/components/onboarding/` so auth, invite, trip, and Atlas do not each invent the look.

- `OnboardingFrame`: full-screen warm paper layout with safe-area padding, optional image/gouache background, and fixed bottom action area.
- `VesperKicker`: Vesper mark + mono caps label. Default color `colors.surface.goldDeep`.
- `VoiceHero`: kicker + serif headline + optional serif body, matching `V2Prompt`.
- `BranchRow`: number, serif title, italic subtitle, gold arrow, hairline separator. This is the fork grammar.
- `SentenceToken`: inline serif token states: `empty`, `active`, `done`; used by the trip-in-mind capture.
- `GlassAction`: translucent action button. Current app has `expo-linear-gradient` but not `expo-blur`; either approximate glass with translucent backgrounds/hairlines/shadows or add `expo-blur` intentionally.
- `AuthProviderStack`: Apple/Google/email provider buttons with contextual copy. It should be embeddable inside "open the trip", "keep the diary", "join Lisbon", and "welcome back" screens.
- `DiaryTimelinePreview`: vertical year/place rows with gold nodes, ghost rows, and developing rows.
- `InviteItineraryTimeline`: day/date rail with an open-day gold node.
- `TasteTile`: image/gouache tile with dark gradient overlay and serif label.
- `PrivacyLine`: lock icon + short italic serif privacy line. This should centralize wording so we do not overpromise photo handling.

### Current App Alignment

Already aligned:

- The app token system already mirrors the Claude palette closely.
- The app font stack already maps well: Newsreader + DM Sans + JetBrains Mono.
- `/trip-begin` already feels closer than the auth screens: warm paper, serif hero, ochre/planning-blue accents, saved-place bridge.
- `/atlas/scan` already has a gift/trust framing, paper-object motif, metadata-first privacy copy, and gold Atlas styling.
- Invite backend/frontend architecture already supports public pre-auth value, pending invite replay, and post-auth trip-chat landing.
- Current auth screens now have a warmer Claude-aligned visual layer, but still need structural contextual-auth modes.
- Current invite landing now leads with an image-backed place hero and a lightweight itinerary/timeline artifact instead of the old purple block.
- Signed-out cold start now routes through `/onboarding` instead of straight to sign-in.
- `/onboarding` now implements the cover/fork/branch shell and stores pre-auth trip or dreaming intent.
- Auth completion now replays trip intent into `POST /api/trips` and routes to trip chat.

Not yet aligned:

- `SignInImpl` and `SignUpImpl` still contain form-first auth mechanics. Returning sign-in is now a real door, but trip/diary/invite contextual auth variants still need their own titles/artifacts.
- `SignInImpl` still cannot render all contextual auth states: "Sign in to open Lisbon", "Sign in while I finish", or "Join Lisbon."
- `SignUpImpl` still asks for name/email before product value and then routes to safety chips. Claude's design removes standalone sign-up as the cold-start front door.
- `/onboarding` trip capture uses fixed sample destinations/durations rather than real place search and date windows.
- Dreaming taste signals are stored only as local auth intent today; they are not yet persisted to a non-constraint backend signal endpoint.
- `app/invite/[slug].tsx` now has the right first-viewport direction, but the timeline is a frontend artifact from invite snapshot data rather than a real itinerary-backed read-only peek.
- `app/invite/[slug].tsx` still asks for private preference signals before auth. Claude defers the diary/private-taste ask until after the trip join.
- `/trip-begin` uses post-auth door cards and starter tiles. Claude's cold-start trip branch uses a single sentence completed across where/when/who.
- `/atlas/scan` is an authenticated utility flow. Claude's dreaming branch presents a locked diary preview, then permission, then auth while diary construction is visible.

## Screen-By-Screen Frontend Polish Spec

### Cold-Start Cover

Target from Claude:

- Full-bleed dark scenic/gouache image.
- Centered Vesper mark.
- Serif italic hero: "Every place you've loved."
- Mono caps descriptor: "A travel concierge with taste."
- Gold `Begin` CTA.
- Serif italic returning-user text link.

App implementation:

- Add `app/onboarding/index.tsx` or equivalent signed-out route.
- Use `colors.surface.ink` as the dark base and a place image/gouache layer.
- Use `LinearGradient` for dark overlay; use `expo-image` for bitmap assets.
- Route `Begin` to the fork.
- Route "I already have an account" to returning sign-in mode, not the whole onboarding spine.

Do not:

- Use "Welcome to Vesper."
- Put hero text in a card.
- Ask for email, Photos, or safety constraints here.

### Fork

Target from Claude:

- Paper screen, vertically centered.
- Vesper kicker.
- Big serif question: "So - where are we going?"
- Two numbered rows, not cards:
  - `01 A trip in mind`
  - `02 Still dreaming`

App implementation:

- Use `BranchRow` instead of `Card`.
- Use hairline top/bottom separators.
- Keep the whole screen tap-light, no text fields yet.
- Route to local draft branches:
  - `trip`: where/when/who state
  - `dreaming`: interest/pace state

Do not:

- Explain features.
- Show a progress bar.
- Mention scan/photos.

### Trip-In-Mind Branch

Target from Claude:

- A sentence completed across three states: "A trip to where, for how long, with whom."
- The active token is gold and lightly highlighted.
- Where step: search pill plus borderless result rows.
- When step: serif inline options, not boxed chips.
- Who step: serif inline options plus an invite affordance only if a group is chosen.
- Bottom CTA is a glass/planning-blue action. Before selection it says "Skip for now"; after selection it becomes "Next"; final says "Start the trip."
- Secondary line: "Rather just tell me? Talk it through ->"

App implementation:

- Reuse backend trip creation after auth. Before auth, store a local `OnboardingTripDraft`.
- Use `colors.surface.planningInk` / `planningInkDeep` for the trip CTA.
- Use `fontFamily.serif_medium_italic` for active tokens and `colors.surface.goldDeep`.
- On `Start the trip`, route to contextual auth mode.
- After auth, replay into `createTrip({ destination, dates/window, companions metadata })` and route to `routes.tripChat(tripId)`.

Do not:

- Send trip-in-mind users through the diary gift full screen.
- Make the capture feel like a form with labels and rectangular inputs.
- Land them in generic Trips after auth.

### Dreaming Branch

Target from Claude:

- Two quick visual taste beats:
  - "What makes a trip worth it?"
  - "And your pace?"
- Image/gouache tiles with serif overlay labels.
- Tiny taste dots only, no wizard progress.
- The selected signals seed Travel DNA; they are not safety constraints.

App implementation:

- Add a local `OnboardingTasteDraft`.
- Use four visual tiles for interest and three visual tiles for pace.
- Persist after auth through a new non-constraint onboarding-signal endpoint, or hold as local context for Atlas until that endpoint exists.
- Use existing Atlas color/typography patterns, not purple agent chips.

Do not:

- Store "Food & drink" or "Slow & deep" as hard constraints.
- Present this as a quiz.
- Ask for allergies/accessibility in this branch.

### Diary Gift

Target from Claude:

- Offered only after dreaming branch engagement.
- Vesper kicker: "VESPER · ONE MORE THING."
- Serif headline: "Want a diary of your own?"
- Locked preview of a diary timeline, not an empty card.
- Privacy line with lock icon.
- Gold primary: "Build my diary."
- Serif italic secondary: "Maybe later - take me in."

App implementation:

- Build `DiaryTimelinePreview` with `full`, `developing`, and `empty` modes.
- Put the preview in an artifact card; this is a valid card because it represents the product value.
- Use careful privacy copy: "Photos stay on this iPhone unless you choose to add them." Do not say "nothing leaves your phone" unless the implementation fully guarantees that for every descriptor/artifact path.
- If user accepts, request Photos and route to contextual auth while scan/construction is visible.
- If user declines or denies permission, route to no-diary auth and then Atlas.

Do not:

- Ask Photos before the gift.
- Use generic permission rationale copy like "Vesper needs access."
- Guilt the user for declining.

### Contextual Auth

Target from Claude:

- Auth is embedded inside value:
  - Trip: "Sign in to open your trip."
  - Diary: "Sign in while I finish."
  - Invite: "Join Lisbon."
  - Returning: "Everywhere you've been is still here."
- Provider buttons are glass/translucent with icon + label.
- Email path expands inline and converges back to the same post-auth replay.

App implementation:

- Keep Clerk code from `SignInImpl`/`SignUpImpl`, but split presentation from auth mechanics.
- Introduce `AuthProviderStack` and a contextual auth screen that accepts:
  - `mode: 'trip' | 'diary' | 'invite' | 'returning' | 'generic'`
  - `title`, `body`, `draftId`/`inviteToken`, `postAuthIntent`
- Use `resolvePostAuthRoute` as the base but extend it to resolve onboarding trip/diary drafts.
- Email auth should not have a separate "create account" looking screen in cold start; new users and returning users can both enter through Clerk flows while the product value remains visible.

Do not:

- Keep `Create your account` as the main cold-start path.
- Route OAuth universally to `onboarding-safety`.
- Put auth in a blank form-only screen after a beautiful branch.

### Invite Landing

Target from Claude:

- Place-first hero, e.g. "Lisbon" over image/gouache.
- Mono caps date line.
- Organizer avatar/note: "Ana invited you along."
- Read-only itinerary timeline with one open day highlighted in gold.
- Primary: "Join the trip."
- Secondary escape: "Not now - just set up Vesper for me."
- Auth screen framed as "Join Lisbon."
- Diary gift deferred until after join.

App implementation:

- Replace the purple hero in `app/invite/[slug].tsx` with image/gouache + `LinearGradient`.
- Render trip title/destination as the hero object, not sentence copy inside a purple block.
- Replace current private-signal `conciergeCard` with `InviteItineraryTimeline` when itinerary/day data is available; use snapshot text as a fallback invite note.
- Move private preference capture to post-join Vesper/chat or a later private diary nudge.
- Keep existing accept/replay backend path.

Do not:

- Use purple as the invite hero color.
- Ask private taste chips before the user joins.
- Land in a generic concierge chat when a trip ID exists.

### Atlas Landing / Scan

Target from Claude:

- Diary construction happens while auth is happening or quietly in Atlas.
- Atlas chrome remains usable.
- Developing state uses a timeline and soft status, not a blocking spinner screen.
- No-diary landing is warm and non-punitive.

App implementation:

- Reuse the existing `/atlas/scan` scan/progress machinery.
- Add an onboarding source param/state so copy and layout can switch to "diary gift" mode.
- Use `DiaryTimelinePreview` instead of only progress rows for onboarding-origin scans.
- Make status copy Vesper-voiced and precise about metadata/photos.

Do not:

- Block the entire app with scan progress after auth.
- Claim raw-photo privacy beyond the architecture.

## Current Frontend Implementation

### Boot And Auth Gate

Files:

- `travel-app/app/_layout.tsx`
- `travel-app/app/index.tsx`
- `travel-app/components/auth/AuthRedirect.tsx`
- `travel-app/context/UserContext.tsx`
- `travel-app/context/AuthUserProvider.tsx`

Current flow:

- Mock or `SKIP_AUTH`: root redirects directly to `/(tabs)/trips`.
- Real auth: root lazy-loads Clerk, then `AuthRedirect`.
- Signed-out real user goes to `/(auth)/sign-in`.
- Signed-in user goes to pending invite if one is stashed; otherwise `/(tabs)/trips`.

Important implementation detail:

- Internal user creation is lazy. The backend user row is created on the first authenticated backend request via Clerk JWT resolution.
- `/api/me` is the hydration pivot. The frontend gates several downstream queries on `profileLoaded` so mock user IDs do not leak into real requests.

Mismatch with Claude:

- There is no pre-auth value surface.
- There is no generic "Begin" cover/fork.
- The only post-auth routing memory today is pending invite token.

### Sign-In

Files:

- `travel-app/app/(auth)/sign-in.tsx`
- `travel-app/components/auth/SignInImpl.tsx`

Current behavior:

- Email OTP: email -> code -> session -> `resolvePostAuthRoute(routes.trips())`.
- OAuth: Google/Apple -> session -> `routes.onboardingSafety()`.
- OTP has resend, code autofill, haptics, loading copy, and error recovery.

Strength:

- Mechanically solid. It should be reused as the auth substrate.

Mismatch with Claude:

- First screen says "Welcome to Vesper" and asks for email before product value.
- OAuth always routes through safety chip skip-through, not through a pending trip/dreaming draft.
- The sign-in screen is not contextual: it cannot currently say "Sign in to open Lisbon" or "Sign in while I finish your diary."

### Sign-Up

Files:

- `travel-app/app/(auth)/sign-up.tsx`
- `travel-app/components/auth/SignUpImpl.tsx`
- `travel-app/components/auth/SafetyChipsForm.tsx`

Current behavior:

- Name + email -> email OTP -> active Clerk session -> safety chips.
- OAuth sign-up -> active session -> `/onboarding-safety`.
- Safety chips post allergy/accessibility data to `/api/users/{id}/intake`.
- After onboarding, route honors pending invite; otherwise Trips.

Strength:

- The hard-constraint capture is safety-aware and backend-integrated.

Mismatch with Claude:

- Requires name/email before value.
- Safety chip form is positioned as onboarding homework.
- No trip/dreaming branch; all new users get essentially the same account-creation path.

### Safety Chips

Files:

- `travel-app/components/auth/SafetyChipsForm.tsx`
- `travel-app/app/onboarding-safety.tsx`
- `travel-agent/backend/api/routes/users/constraints.py`

Current behavior:

- Captures allergies and accessibility only.
- Dietary preferences are explicitly not captured here; conversation asks later.
- `POST /api/users/{id}/intake` writes hard constraints and creates onboarding observations, then schedules Personal Memory refresh.
- Existing OAuth users with constraints skip the screen.

Product tension:

- Safety constraints are genuinely important, but Claude's design intentionally avoids early "homework."
- We should not delete this capability. We should move it to a better moment or make it contextual.

Recommendation:

- Keep safety capture, but do not make it the first universal onboarding step.
- For the trip branch, ask safety only when planning food/stays or via Vesper chat.
- For the dreaming branch, let taste/pace seed memory first; prompt safety later from Atlas profile or first planning session.

### Trip Creation

Files:

- `travel-app/app/trip-begin.tsx`
- `travel-app/context/TripContext.tsx`
- `travel-agent/backend/api/routes/trips.py`

Current behavior:

- Authenticated Trips "+" opens `/trip-begin`.
- User can talk with Vesper, start blank, pick a shape, or continue from saved places.
- `createTrip()` optimistically creates a local trip, then posts to real backend.
- Backend `POST /api/trips` accepts `destination`, dates, title, etc.
- Blank trip create dedupes to one blank slot per user.
- Destination labels are resolved to place IDs when possible.

Strength:

- This maps well to Claude's "trip in mind" branch.

Mismatch with Claude:

- Only available after auth.
- It is framed as a Trips-tab utility, not first-session onboarding.
- "Talk it through" jumps to generic concierge chat, not a controlled branch with where/when/who capture and post-auth replay.

### Invite Landing

Files:

- `travel-app/app/invite/[slug].tsx`
- `travel-app/data/invites.ts`
- `travel-agent/backend/api/routes/invites.py`

Current behavior:

- Public `GET /api/invites/{token}` renders invite data before auth.
- Invitee can submit private chips/free text before auth via `POST /api/invites/{token}/intake`.
- Accept is authenticated via `POST /api/invites/{token}/accept`.
- If accept returns 401, token is stashed and user is routed to sign-in.
- After auth, `AuthRedirect` routes back to the invite.
- Accept adds membership, logs event, persists pending intake as observations, refreshes memory, and lands the app in trip chat.

Strength:

- This is the closest current flow to Claude's design.
- It already has public pre-auth value and pending-intake replay.

Mismatch with Claude:

- Visual design is old purple/card-heavy.
- The private preference ask appears on the invite screen before auth.
- It does not show a polished read-only itinerary timeline as the main hook.
- Auth is generic sign-in, not framed as "Join Lisbon."

### Atlas Photo Scan

Files:

- `travel-app/app/atlas/scan.tsx`
- `travel-app/hooks/useAtlasPhotoPicker.ts`
- `travel-app/utils/photoPermission.ts`
- `travel-app/data/atlas.ts`
- `travel-agent/backend/api/routes/atlas.py`
- `docs/Atlas — README.md`

Current behavior:

- Authenticated Atlas scan flow: Promise -> Trust -> Scan.
- Manual picker path requests photo permission, loads selected assets, hydrates metadata, clusters locally, submits candidates, routes to Atlas inbox.
- Full-library scan path exists in frontend direction but is still drift-risk and broader than V0 manual-pick.
- iOS limited photo access is treated as granted.
- Backend Atlas routes are authenticated.

Strength:

- Privacy posture and local clustering are real.
- The current flow already treats photo access as a controlled, reviewable gift.

Mismatch with Claude:

- It is post-auth and inside Atlas, not part of cold-start onboarding.
- Design wants "sign in while diary constructs"; current implementation needs auth before candidates can be submitted.
- Copy must be tightened. "Nothing leaves your phone" is only true for raw photos; candidate descriptors and approved artifacts do go to backend.

## Current Backend Implementation

### Auth And User Creation

Files:

- `travel-agent/backend/api/auth.py`
- `travel-agent/backend/core/db/traveler.py`
- `travel-agent/backend/api/routes/users/me.py`

Current behavior:

- Clerk JWT is verified on protected routes.
- `get_or_create_user_from_auth()` creates or backfills internal users.
- Home conversation is bootstrapped on first user creation.
- `/api/me` returns user row plus memory-derived taste DNA, interests, reflection phrases, taste completion, and trip count.

Implication for Claude alignment:

- Pre-auth onboarding cannot write to user-owned resources without a new persistence pattern.
- The simplest approach is local draft storage before auth, then post-auth replay.
- The invite flow already uses a server-side pre-auth token pattern; that pattern can inform a future anonymous onboarding-session API if local-only draft replay proves too brittle.

### Intake And Memory

Files:

- `travel-agent/backend/api/routes/users/constraints.py`
- `travel-agent/backend/core/db/observations.py`
- `travel-agent/backend/concierge/refresh_memory.py`

Current behavior:

- `/api/users/{id}/intake` supports `dietary`, `accessibility`, `languages`, `allergies`.
- It writes hard constraints, creates observations, and refreshes Personal Memory.

Gap:

- Claude's dreaming branch captures interest and pace. These are not hard constraints and should not be shoved into the existing constraint shape.

Needed backend work:

- Add a first-class onboarding preference intake endpoint, or extend intake with non-constraint sections that create observations without hard constraints.
- Candidate shape:
  - `POST /api/users/{id}/onboarding-signals`
  - body: `branch`, `interest_axis`, `pace_axis`, `destination_label`, `duration_bucket`, `party_shape`, `source`
  - effects: create observations with `source_mode="onboarding"` and provenance, optionally refresh memory.

### Trips

Files:

- `travel-agent/backend/api/routes/trips.py`
- `travel-app/context/TripContext.tsx`

Current behavior supports the trip branch well:

- authenticated trip create
- idempotency
- blank-trip dedupe
- destination labels
- organizer membership

Needed work:

- A post-auth replay function that reads a local onboarding trip draft and calls existing `createTrip()`.
- Optional backend enhancement: accept `party_shape` or `onboarding_source` on create, and/or create invite drafts for "a few of us."

### Invites

Files:

- `travel-agent/backend/api/routes/invites.py`
- `travel-agent/backend/core/db/trip_invites.py`

Current behavior supports Claude's invite door well:

- public invite view
- public pre-auth intake
- authenticated accept
- pending token replay
- private intake observations after accept
- organizer notification for private invite answer

Needed work:

- Mostly frontend redesign and route framing.
- Backend may need a richer invite view model if the Claude itinerary peek needs ordered day rows beyond current snapshot summary.

### Atlas

Files:

- `travel-agent/backend/api/routes/atlas.py`
- `travel-agent/backend/atlas/`
- `travel-app/app/atlas/scan.tsx`
- `travel-app/hooks/useAtlasPhotoPicker.ts`

Current behavior is authenticated and candidate-based.

Needed work:

- Decide whether cold-start photo scan can run pre-auth as local-only work.
- If yes: cache local candidate descriptors until auth, then submit.
- If no: reuse Claude styling but route "Build my diary" to sign-in first, then run `/atlas/scan?source=onboarding`.
- Tighten privacy copy so it does not overpromise.

## Gap Matrix

| Claude concept | Current support | Gap | Recommended approach |
|---|---|---|---|
| Cover with Begin / returning door | none | app starts at auth | Add `/onboarding` as signed-out root destination |
| Fork: trip vs dreaming | none | no pre-auth branch state | Local onboarding draft state |
| Trip where/when/who | partial via `/trip-begin` and trip create | only post-auth; no replay | New native onboarding trip capture; replay after auth |
| Sign in to open trip | partial via auth + createTrip | generic auth destination | Add post-auth target/replay for `pendingOnboardingTrip` |
| Land in trip Vesper chat | supported route | not wired from onboarding | After create, `router.replace(routes.tripChat(tripId))` |
| Dreaming interest/pace | not currently captured | no backend non-constraint intake | Add onboarding-signals endpoint or extend intake |
| Diary gift | partial via Atlas scan | inside authenticated Atlas | Re-skin and expose as onboarding branch |
| Photo permission after value | partial | current scan is post-auth | Use existing picker later in flow |
| Sign in while diary constructs | not directly | submit requires auth | Either local pre-scan + replay, or post-auth scan with transitional UI |
| Graceful decline | partial via skip | no no-diary Atlas landing from onboarding | Store decline state; route Atlas with no-diary hero |
| Invite door | strong partial | visual and sequencing mismatch | Redesign invite screen first |
| Returning user | supported | generic sign-in | Redesign sign-in as calm returning door |

## Recommended Implementation Plan

### Phase 1 — Low-Risk Shell Alignment

Goal: align the first impression and invite door without touching backend contracts.

Frontend:

- Add `app/onboarding/index.tsx` or equivalent signed-out onboarding route.
- Change signed-out root redirect from `/(auth)/sign-in` to `/onboarding`.
- Build Claude-style `Cover` and `Fork` native screens.
- "I already have an account" routes to existing sign-in with new returning copy.
- Redesign invite landing using existing `GET /api/invites/{token}` data:
  - illustrated/paper hero
  - organizer/friend proof
  - read-only trip shape / day timeline
  - "Join the trip" -> existing accept flow
  - private diary gift deferred until after join

Backend:

- None required.

Tests:

- signed-out root goes to onboarding
- returning door still reaches sign-in
- pending invite still survives auth
- invite accept still lands in trip chat

### Phase 2 — Trip-In-Mind Branch

Goal: make the first valuable path real.

Frontend:

- Add local draft persistence, e.g. `utils/onboardingDraft.ts`.
- Capture:
  - destination label
  - duration bucket / dates if available
  - party shape
  - optional invite names later
- On "Start the trip":
  - if signed out: persist draft and route to contextual sign-in
  - if signed in: replay immediately
- After auth:
  - read draft
  - call existing `createTrip({ destination, start_date, end_date })`
  - route to `routes.tripChat(tripId)` with onboarding prefill/context
  - clear draft

Backend:

- Optional: extend `CreateTripRequest` with `party_shape`, `source`, or `onboarding_context`.
- Optional: create observations from trip branch choices.

Tests:

- draft survives auth redirect
- createTrip uses hydrated real user id, not mock fallback
- slow/retry path does not duplicate trip
- route lands in trip chat

### Phase 3 — Dreaming Branch / Taste Signals

Goal: capture useful signal without making onboarding a quiz.

Frontend:

- Implement two Claude taste beats:
  - interest: food, art/history, nature/air, sea/sun
  - pace: slow/deep, full/restless, depends
- Persist selections as local draft.
- After auth, submit taste signals.

Backend:

- Add non-constraint onboarding signal endpoint.
- Do not store these as hard constraints.
- Create observations with provenance and schedule memory refresh.

Tests:

- selected taste axes appear in `/api/me` memory/dna after refresh
- no hard constraints are created for taste axes
- skip path still lands

### Phase 4 — Diary Gift / Atlas Integration

Goal: make Claude's diary gift real without breaking privacy.

Safer dogfood path:

- User accepts diary gift.
- Route to contextual auth.
- After auth, route to `/atlas/scan?source=onboarding`.
- Restyle scan screens to match Claude.

More ambitious path:

- Request Photos pre-auth.
- Locally hydrate metadata and cluster.
- Persist candidate descriptors locally.
- After auth, submit candidates to `/api/atlas/candidates`.
- Show "sign in while I finish" while replay runs.

Backend:

- No change for safer path.
- For ambitious path, verify candidate descriptor persistence does not include raw photo content and that expired/local-only PHAsset IDs are handled.

Copy correction:

- Use "Photos stay on this iPhone unless you choose to add them" rather than "Nothing leaves your phone" if candidate descriptors are submitted.

### Phase 5 — Safety And Compliance Repositioning

Goal: preserve safety without ruining activation.

Options:

- Keep safety chips after auth only for users entering planning, but render it as "anything I should always avoid?" not account setup.
- Trigger safety elicitation in the trip chat when food/stay planning starts.
- Keep `/onboarding-safety` as a fallback route for OAuth/new users until the new replay pipeline fully replaces it.

Decision needed:

- Whether allergy/accessibility capture remains mandatory-ish before first trip chat, or becomes contextual.

## Highest-Risk Decisions

1. Pre-auth persistence model:
   - Local-only is fastest and privacy-preserving.
   - Server-side anonymous onboarding sessions are more reliable across devices but require a new bearer-token surface.

2. Photo scan before auth:
   - Better Claude fidelity.
   - Higher risk with permissions, local storage, and privacy copy.
   - Recommend delaying until the trip branch and invite door are live.

3. Safety chip placement:
   - Current product treats allergy/accessibility as a safety floor.
   - Claude design treats early asks as activation killers.
   - Need founder/product call.

4. Auth architecture:
   - Clerk remains the right auth substrate.
   - The product should no longer expose Clerk as the first experience.

## Proposed First PRs

1. Add onboarding draft storage and post-auth route resolver.
2. Build signed-out `Cover` and `Fork` screens.
3. Redesign returning sign-in copy/skin while preserving `SignInImpl` behavior.
4. Redesign invite landing visual layer using existing invite data.
5. Implement trip branch capture and replay to `createTrip()`.
6. Add backend `onboarding-signals` endpoint for taste/pace observations.
7. Restyle Atlas scan as the diary gift and optionally wire onboarding source params.

## What Not To Do

- Do not replace Clerk internals; reuse them.
- Do not store taste axes as hard constraints.
- Do not ask Photos on the cover or fork.
- Do not make the invite flow pass through generic onboarding.
- Do not promise "nothing leaves your phone" unless raw photos, metadata, and candidates all truly remain local.
- Do not remove the existing safety chips until there is a contextual replacement.
