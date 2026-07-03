# Apple Review Notes

Paste-ready content for the **"Notes for Apple"** field in App Store
Connect (App → App Information → App Review Information).

The reviewer has ~10 minutes per app. The goal of this doc is to make
those 10 minutes lead to an approval, not a rejection email three days
later asking for clarification.

---

## Demo account

Apple requires a working demo account for any app behind auth. The app
uses Clerk for sign-in (phone number + OTP). For review, provide a
test account that doesn't require a real phone:

| Field | Value |
|---|---|
| Sign-in method | Phone number (Clerk) |
| Demo phone number | `+1 555 555 5555` |
| OTP code | `424242` |
| Notes | The phone+OTP path on this number is wired to Clerk's review-only test mode. Real phone numbers continue to use real OTP delivery. |

> **Action required before submitting**: configure Clerk dashboard →
> Authentication → Test phone numbers → add `+15555555555` with OTP
> `424242`. Without this, the reviewer hits a real OTP send and the
> review stalls.

---

## What to test (suggested 5-minute reviewer path)

1. **Sign in** with the demo phone + OTP above. Land on the trips tab.
2. **Open the existing demo trip** ("Lisbon · May 2026" — seeded on the
   review account at signup). Verify the trip card renders with the
   place, dates, and members.
3. **Tap "Talk to Vesper"** (1:1 thread). Type *"What should we do
   Thursday night?"* and confirm a streamed reply arrives within ~10
   seconds. The reply will reference Lisbon places.
4. **Open the group chat** for the same trip. Confirm at least one
   prior message from Vesper exists, and that typing a message and
   sending it appears in the thread.
5. **Open the Me tab → "What Vesper knows about you"** — confirm a
   Personal Memory artifact is rendered.
6. **Optional voice test**: trip detail → "Hear about this place"
   triggers an audio narration. iPad reviewers without speakers can
   skip; the visual chrome confirms the surface renders.

> Total reviewer time: ~4 minutes if everything works.

---

## Why each permission prompt appears

Apple flags apps that ask for permissions without obvious justification.
Each prompt in `Travel App/app.json` is wired to a real feature; the
matching usage descriptions are below verbatim. If the reviewer asks,
this is the answer.

| Permission | When the user sees it | Why we need it |
|---|---|---|
| **Photo Library (read + add)** | First time the user adds a photo to a Trip Story slot, expense receipt, chat message, or trip album | The Memory Surface (Trip Story) lets the user select photos from their library to fill in story slots. Expenses needs receipt capture. Group chat supports image attachments. |
| **Camera** | When the user taps "Capture receipt" or "Take photo" inside the app | Receipt capture for expenses; on-the-fly trip photos. Not used for biometrics, identity, or AR. |
| **Location (When In Use)** | First time the user opens the Discover tab on the trip, or when the trip starts | The agent surfaces nearby places relevant to the user's taste, narrates arrivals, and attaches location context to messages the user explicitly sends. Background location is NOT used — the manifest sets `isIosBackgroundLocationEnabled: false`. |
| **Notifications (push)** | After first sign-in, on prompt | Coordination notifications for the group (proposals, mentions, day-of nudges) and post-trip story-ready alerts. The user can disable any category from the Me tab. |

The microphone permission is NOT requested in this build — the voice
companion plays pre-rendered narration. If a future build adds real-
time voice input, the prompt will explain "Vesper listens during voice
mode so you can speak directly to the agent."

---

## Universal Links / deep linking

The app claims `applinks:travelagent.app` (app.json `associatedDomains`).
A reviewer who taps an `https://travelagent.app/invite/<token>` link
on a device with the app installed will be deep-linked into the app's
invite-acceptance flow.

This is **opt-in**: a user must explicitly tap an invite link to
trigger the deep link. There is no background URL-handling, no
auto-launching from clipboard, no clipboard polling.

For Universal Links to work, the AASA manifest must be served at
`https://travelagent.app/.well-known/apple-app-site-association` with
the correct Team ID + bundle ID. Our backend boot validator refuses to
start with a `REPLACE_ME` Team ID in production (see
`Travel Agent/backend/api/lifecycle.py`), so a deploy can't ship a
broken AASA silently.

---

## Subscriptions / IAP

This build has **no in-app purchases and no subscription tier**. The
app is free-to-use throughout TestFlight. If subscriptions are added in
a future build, the App Privacy disclosures will be revised
accordingly.

---

## User-generated content moderation

Group chat allows users to send free-text messages and image
attachments. The product is invite-only at the group level (a user
can only see content from groups they've been added to via invite),
which substantially limits the exposure surface compared to an open
social network.

Image uploads are checked for prohibited content via:
- Client-side: standard Expo image picker; user explicitly selects
- Server-side: stored under per-user paths; no public listing

Reports of abusive content from within a group can be sent via the Me
tab → Send Feedback (text-form report, includes the trip + user
context automatically).

We follow Apple's UGC guidelines: a user can block another user in
their group, leave a group at any time, and delete the entire account
+ all content from Me tab → Account → Delete Account.

---

## Account deletion

Per App Store Review Guideline 5.1.1(v), the app provides in-app
account deletion: **Me tab → Account → Delete Account**.

The deletion is end-to-end: the backend purges the user's profile,
personal memory, conversations, trip memberships (the user is removed
from groups they joined; groups they organized are not deleted, but
the user's identity is anonymized), and all photo/audio uploads. No
re-activation period. No data retention beyond what's legally required
for financial records (none for free tier).

---

## Beta-only features that look unfinished

A few surfaces are deliberately bare for TestFlight 1:

- **Discover tab.** Will eventually surface place-aware suggestions
  between trips. For the demo trip, shows the trip's own city. Empty
  outside trip context is intentional.
- **Booking flow.** The "Book this" CTAs route to provider deep links
  (Viator, Booking.com) rather than completing in-app — affiliate-tier
  integration, not a partial flow.
- **Notifications.** A handful of notification categories are wired
  but most will only fire in real trip windows. The reviewer won't
  see them during a 4-minute session.

If the reviewer flags any of these as "not functional," the answer is
"intentionally scoped for TestFlight 1; full surface in v1.1."

---

## What this build does NOT do

Apple reviewers sometimes assume travel apps do things they don't.
Stating it explicitly avoids confusion:

- Vesper does **not** read or interpret SMS, email, or other apps'
  content.
- Vesper does **not** track location in the background.
- Vesper does **not** access the user's contacts list (group members
  are added via invite link only).
- Vesper does **not** record audio without an explicit user action.
- Vesper does **not** auto-charge or auto-renew anything — no payment
  surfaces in this build.

---

## Contact for review questions

Email the support address from the App Store listing
(`support@travelagent.app`) or message via the App Store Connect
review reply form. Response within 24 hours during the review window.

---

## Build-version history pointer

Each TestFlight build's reviewer notes can reference this doc as the
authoritative source. If a specific build adds a feature that needs
additional review context, add a `## Build X.Y.Z` section to this file
*before* uploading the build, then quote that section in the
build-specific notes field.
