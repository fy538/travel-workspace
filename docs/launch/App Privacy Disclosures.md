# App Privacy Disclosures

Pre-fill for **App Store Connect → App Privacy** (the per-app data
collection questionnaire). Answers are derived from a real audit of
[`travel-agent/backend/core/db/_tables/`](../../travel-agent/backend/core/db/_tables/) — what tables exist, what
fields they hold, and how the backend uses them.

Apple's questionnaire is structured as: for each data category that
applies, declare *what* is collected, whether it's *linked to identity*,
whether it's *used for tracking*, and for *which purposes*. Walk down
this doc and answer the matching screen in App Store Connect.

---

## Global answers (apply to every category)

| Question | Answer |
|---|---|
| Do you or your third-party partners use this data to track users across apps/sites owned by other companies? | **No** — for every category. Vesper does not track users across apps or websites owned by other companies, does not run third-party advertising SDKs, and does not share data with data brokers. |
| Do you collect any of the data types listed? | **Yes** — see categories below. |

---

## Categories Vesper collects

### 1. Contact Info

| Subtype | Collected? | Linked to identity? | Used for tracking? | Purposes |
|---|---|---|---|---|
| Name | ✅ Yes | ✅ Yes | ❌ No | App Functionality, Product Personalization |
| Email Address | ✅ Yes | ✅ Yes | ❌ No | App Functionality |
| Phone Number | ✅ Yes | ✅ Yes | ❌ No | App Functionality (Clerk sign-in via phone OTP) |
| Physical Address | ❌ No | — | — | — |
| Other User Contact Info | ❌ No | — | — | — |

**Backend source**: `users` table. Name and phone are required for
account creation; email is optional.

---

### 2. Health & Fitness

| Subtype | Collected? |
|---|---|
| Health | ❌ No |
| Fitness | ❌ No |

---

### 3. Financial Info

| Subtype | Collected? | Linked to identity? | Used for tracking? | Purposes |
|---|---|---|---|---|
| Payment Info | ❌ No — Vesper does not process payments | — | — | — |
| Credit Info | ❌ No | — | — | — |
| Other Financial Info | ✅ Yes — *expense amounts* the user voluntarily logs | ✅ Yes | ❌ No | App Functionality |

**Backend source**: `expenses` table. Stores amounts in user-chosen
currency, optional receipt image, and a description. **Does not store
payment credentials, card numbers, or banking info.** External booking
provider payments happen on the provider's site, not in-app.

---

### 4. Location

| Subtype | Collected? | Linked to identity? | Used for tracking? | Purposes |
|---|---|---|---|---|
| Precise Location | ✅ Yes | ✅ Yes | ❌ No | App Functionality, Product Personalization |
| Coarse Location | ✅ Yes | ✅ Yes | ❌ No | App Functionality |

**When**: only while the user is actively using the app (When In Use).
Background location is explicitly disabled in `app.json` — see the
`isIosBackgroundLocationEnabled: false` flag.

**Why**: Discover surfaces nearby places, voice narration knows when
the user has arrived at a venue, and chat messages can optionally
include the user's current location as context.

**Backend source**: `home` table (current location snapshot for feed
ranking), `conversations.messages.location_snapshot` (when user
explicitly attaches location to a message).

---

### 5. Sensitive Info

| Subtype | Collected? |
|---|---|
| Sensitive Info (race, sexual orientation, religion, etc.) | ❌ No |

**Note**: Vesper does **not** ask for or store sensitive demographic
data. Dietary restrictions (vegetarian, kosher, halal, allergies) are
stored as hard constraints, but Apple's "Sensitive Info" category
specifically excludes dietary preferences — those are App Functionality
under "Other User Content."

---

### 6. Contacts

| Subtype | Collected? |
|---|---|
| Contacts | ❌ No |

**Note**: Vesper does **not** read the user's iOS contacts list.
Group members are added by sending an invite link the user explicitly
shares (via iMessage, email, etc.) — not by uploading a contacts list.

---

### 7. User Content

| Subtype | Collected? | Linked to identity? | Used for tracking? | Purposes |
|---|---|---|---|---|
| Emails or Text Messages | ❌ No | — | — | — |
| Photos or Videos | ✅ Yes — when the user selects them for trip albums, story slots, expense receipts, or chat attachments | ✅ Yes | ❌ No | App Functionality, Product Personalization |
| Audio Data | ❌ No — voice features play OUTBOUND narration only; no user audio is recorded in this build | — | — | — |
| Customer Support | ✅ Yes — when the user submits the in-app Send Feedback form | ✅ Yes | ❌ No | App Functionality |
| Other User Content | ✅ Yes — chat messages, trip story edits, dietary/accessibility constraints, group/trip names | ✅ Yes | ❌ No | App Functionality, Product Personalization |

**Backend source**: `conversations` (messages), `trip_photos`,
`trip_stories` (sections + edits), `memory` (personal memory + hard
constraints).

---

### 8. Browsing History

| Subtype | Collected? |
|---|---|
| Browsing History | ❌ No |

**Note**: Vesper does **not** access Safari history, the iOS clipboard,
or any other app's content.

---

### 9. Search History

| Subtype | Collected? |
|---|---|
| Search History | ❌ No |

**Note**: In-app discover queries and chat messages are stored as
conversation content (covered under §7 User Content), not as a
separate "search history" pattern. Vesper does not record what the
user types into the iOS Spotlight, web browsers, or other apps.

---

### 10. Identifiers

| Subtype | Collected? | Linked to identity? | Used for tracking? | Purposes |
|---|---|---|---|---|
| User ID | ✅ Yes — every user has an internal UUID | ✅ Yes | ❌ No | App Functionality |
| Device ID | ✅ Yes — Expo push token (per-device identifier) | ✅ Yes | ❌ No | App Functionality |

**Backend source**: `users.id` (UUID), `users.expo_push_token`.
The Expo push token is the only device-level identifier the app
collects and is used solely to deliver notifications to that device.

---

### 11. Purchases

| Subtype | Collected? |
|---|---|
| Purchase History | ❌ No |

**Note**: Vesper has no in-app purchases or subscriptions in this
build. External booking purchases happen on the provider's website
(Viator, Booking.com, etc.) — Vesper does not see or store the
purchase details.

---

### 12. Usage Data

| Subtype | Collected? | Linked to identity? | Used for tracking? | Purposes |
|---|---|---|---|---|
| Product Interaction | ✅ Yes — taps, screen visits, agent turn counts | ✅ Yes | ❌ No | Analytics, App Functionality |
| Advertising Data | ❌ No | — | — | — |
| Other Usage Data | ✅ Yes — agent-quality telemetry (turn latency, tool usage, guard violations) | ✅ Yes | ❌ No | Analytics, App Functionality |

**Backend source**: `telemetry`, `concierge_turns`, `reasoning_spans`.
Used to measure agent quality, debug regressions, and rank what to
fix. **Not** shared with third-party analytics SDKs in this build.

---

### 13. Diagnostics

| Subtype | Collected? | Linked to identity? | Used for tracking? | Purposes |
|---|---|---|---|---|
| Crash Data | ✅ Yes — Expo Crashlytics-equivalent (TestFlight built-in) | ❌ No | ❌ No | App Functionality |
| Performance Data | ✅ Yes — latency metrics on the agent path | ✅ Yes | ❌ No | App Functionality, Analytics |
| Other Diagnostic Data | ✅ Yes — backend error logs (excludes user content via the redactor at the propose_change boundary) | ❌ No | ❌ No | App Functionality |

---

### 14. Other Data

| Subtype | Collected? | Linked to identity? | Used for tracking? | Purposes |
|---|---|---|---|---|
| Travel preferences synthesized from user behavior | ✅ Yes | ✅ Yes | ❌ No | Product Personalization, App Functionality |

**Backend source**: `personal_memories`, `hard_constraints`,
`travel_dna`. This is the core of what makes the concierge specific to
the user. Stored as text and structured tags; never sold, never shared
with third parties.

---

## Tracking summary (for the questionnaire's first screen)

**Q: Do you use any of this data to track users?**
**A: No.**

Tracking, per Apple, means linking user/device data to data from other
companies' apps, websites, or offline services for the purpose of
targeted advertising, advertising measurement, or sharing with data
brokers.

Vesper does **none** of the following:
- No third-party advertising SDKs
- No cross-app or cross-site identifier sharing
- No data sold to or shared with data brokers
- No advertising measurement frameworks (no IDFA usage)
- No conversion-tracking SDKs (Meta, TikTok, etc.)

This means the App Tracking Transparency (ATT) prompt is **not
required** for this build. If a future build adds advertising or
attribution measurement, this will need to be revisited.

---

## Data deletion

In-app: **Me → Account → Delete Account** purges the user's profile,
personal memory, conversations, trip memberships, and uploaded
photos/audio. No retention period.

Out-of-band: user can email `privacy@travelagent.app` and we will
manually delete within 14 days (per GDPR Article 17 and CCPA §1798.105
where applicable).

This is mentioned in the App Store description and on the privacy
page served at `https://travelagent.app/privacy`.

---

## Source-of-truth pointer

This doc must be revisited whenever **either** of two things changes:

1. **Backend schema** — new tables may collect new data categories.
   Authoritative inventory:
   [`travel-agent/backend/core/db/_tables/`](../../travel-agent/backend/core/db/_tables/).
2. **iOS permissions in app.json** — adding a permission usually means
   activating a new collection path. Specifically:
   - **NSMicrophoneUsageDescription / microphone permission** would
     mean Vesper now records user audio → §7 "Audio Data" flips to ✅
   - New NSLocationAlwaysUsageDescription → §4 Background location
   - Any NSContactsUsageDescription → §6 Contacts flips to ✅

Drift check before launch:

```bash
# (a) Table count — bump §1-14 if this changes
ls Travel\ Agent/backend/core/db/_tables/*.py | wc -l

# (b) Permission audit — every UsageDescription string maps to one
# category above. If grep surfaces a new one, this doc is stale.
grep -E "Permission|UsageDescription" Travel\ App/app.json
```

If either result drifts from what this doc declares, audit the new
table/permission for data collection that might trigger a new
category before submitting the App Privacy questionnaire.

---

## Submission checklist

Before tapping "Submit for Review" on the App Privacy form:

- [ ] Every category in §1-14 above is filled in on the App Store
  Connect form with the same answer as this doc
- [ ] "No" is selected for the tracking question (the global answer)
- [ ] The privacy policy URL on the listing matches what the backend
  serves at `https://travelagent.app/privacy`
- [ ] The data deletion path (Me → Account → Delete Account) is
  actually wired in the build being submitted (do not declare what
  isn't implemented)
