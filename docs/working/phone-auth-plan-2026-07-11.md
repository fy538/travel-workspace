---
doc_type: working
status: active
owner: founder / engineering
created: 2026-07-11
last_verified: 2026-07-11
expires: 2026-08-10
why_new: No existing document owns the phone-auth implementation plan; working/ is the governed home for execution plans. Archive to audits/ on ship or kill.
supersedes: []
source_of_truth_for: [phone-auth-implementation-plan-2026-07]
---

# Phone Auth — Fullstack + Design Plan

**Question:** add phone-number + OTP as a first-class sign-in / sign-up method,
alongside the existing email-code and Google/Apple OAuth.

**Status:** plan only — not a committed decision. Phone auth is **not** in the
locked v1 scope (`mvp-scope-and-flag-manifest-2026-06-30.md`) and is **not**
required for App Review (guideline 4.8 is already satisfied by Apple + Google
Sign-In). Treat this as a post-cohort-1 product decision. This document exists
so that if we say yes, the path is de-risked and the design brief is ready.

---

## TL;DR / Recommendation

- **Do it via Clerk-managed phone OTP**, exactly the way email-code and OAuth
  already work. Clerk issues and verifies the SMS code; our backend keeps
  resolving the user from the JWT `sub` claim and needs **near-zero change**.
- **Do NOT build a self-managed OTP scheme.** The `users` table already carries
  dormant `phone_*` columns from an abandoned "Phase N2" (a self-managed OTP
  design). Building that path means owning Twilio/SMS delivery, rate-limiting,
  hashing, and expiry — infra we deliberately deferred. Leave those columns
  dormant (or drop them in a later cleanup); Clerk owns the phone identity.
- **Frontend is the real work:** a new `phone` stage in the two auth screens
  reusing the existing staged-flow machinery, a country-code + phone input
  component, and reusing `OtpCodeInput` for the verify step. The `code` stage
  is already strategy-agnostic in spirit — it just needs to verify against
  `phone_code` instead of `email_code`.
- **Rough size:** ~1.5–2.5 eng days FE + ~0.5 day BE/Clerk config + design.
  Medium risk concentrated in one place: country-code input correctness and
  the account-linking edge cases (same human, phone vs email vs OAuth).

---

## Verified current state (2026-07-11)

Grounded in code, not memory.

### Frontend (`travel-app`)
- Auth lives in two components with an identical shape:
  - `components/auth/SignInImpl.tsx` — stages: `providers → email → code`
  - `components/auth/SignUpImpl.tsx` — stages: `providers → email → code → onboarding`
- Both use `@clerk/clerk-expo`: `useSignIn` / `useSignUp`, `useOAuth`, `setActive`.
- Email uses Clerk's `email_code` first-factor strategy. OAuth via `startOAuthFlow`.
- **Reusable pieces already built** (this is why FE cost is bounded):
  - `components/onboarding/AuthProviderStack.tsx` — the Apple / Google / email
    button stack. Adding a "Continue with phone" row here is one entry.
  - `components/onboarding/ContextualAuthShell.tsx` — the shared shell (kicker +
    fleuron + title + subtitle + slot). Accepts a `copyOverride` for per-stage
    copy. Phone stages just supply new copy.
  - `components/onboarding/OtpCodeInput.tsx` — the 6-box code field. **Strategy-
    agnostic already** — reuse as-is for the phone verify step.
  - `Button size="auth"`, `Tap`, toast, haptics, resend-cooldown pattern — all
    reusable verbatim.
- Post-auth routing (`finishAuth`) is identity-source agnostic — it keys off
  invite/onboarding intent, not how you signed in. **No routing changes needed.**

### Backend (`travel-agent`)
- `backend/api/auth.py` verifies the Clerk JWT and resolves the internal user
  purely from `claims["sub"]` → `external_auth_id` via
  `get_or_create_user_from_auth`. **It does not care which factor authenticated
  the session.** A phone-authed Clerk user provisions exactly like an email or
  OAuth user.
- `users` table (`backend/core/db/_tables/users.py`) already has, from the
  initial schema (unwired "Phase N2"):
  `phone_number` (E.164), `phone_verified_at`, `phone_otp_hash`,
  `phone_otp_expires_at`, `phone_otp_attempts`, plus `uq_users_phone_number`.
  **Verified unused:** no backend code, no route, no frontend flow references
  these columns for auth. They are substrate for a self-managed OTP scheme that
  was never built.
- Consequence: **Clerk-managed phone auth needs no new backend route and no
  schema change.** The only *optional* backend touch is persisting the verified
  phone onto our `users.phone_number` (see "Backend" below) if we want it for
  display / SMS invites later.

### Design canon — the phone screens are already designed
- **The phone auth UI is fully designed in canon handoff "vesper 136."** The
  bundle lives at `~/Downloads/vesper 136/` (a Claude Design export). Its
  `project/Vesper Auth and Invite.html` loads a new file, **`auth-phone.jsx`**,
  containing all 8 phone screens/states, plus an updated `auth-invite-app.jsx`
  that adds "Continue with phone" to the provider stack. This supersedes the
  older in-repo `design/vesper-canon-anchor/project/auth-invite-app.jsx` (which
  predates phone auth). **Implement from canon 136** — see "Design — source of
  truth (canon 136)" below for the file map and the self-contained spec.
- Brand voice + tokens are locked (Brand Identity §6 typography, §10 voice).
  The self-contained spec below is extracted verbatim from `auth-phone.jsx`.

---

## The one real decision: Clerk-managed vs self-managed OTP

| | **Clerk-managed (recommended)** | Self-managed (Phase N2 columns) |
|---|---|---|
| Who sends SMS | Clerk | Us (Twilio — deferred) |
| Backend work | ~none (JWT `sub` unchanged) | New routes, hashing, expiry, rate-limit, SMS vendor |
| Consistency | Same as email/OAuth today | A second, bespoke auth path to maintain |
| Cost | Clerk SMS pricing | Twilio + our infra |
| Risk | Low | Medium-high, and off the current architecture |

**Recommendation: Clerk-managed.** The self-managed columns are a trap — they
look like a head start but commit us to owning SMS infra we chose to defer. If
we go Clerk-managed, note the dormant columns in a cleanup ticket; don't wire
them.

---

## Frontend plan (the bulk of the work)

Mirror the email flow exactly. New stage token `phone` in both screens.

### New component: `components/onboarding/PhoneNumberInput.tsx`
> Build to match canon 136 `auth-phone.jsx` → `PhoneField` + `CountryPill` +
> `ScreenCountryPickerSheet`. Those give exact geometry, tokens, and copy; the
> notes below are the RN implementation contract.
- Country-code selector (default from device locale via `expo-localization`;
  fall back to `+1`) + national number field.
- Emits a normalized **E.164** string (`+<cc><number>`). Do the normalization
  here so the screens stay dumb. Use `libphonenumber-js` (small, RN-safe) for
  parse/format/validation rather than hand-rolling — country rules are a swamp.
- Visual parity with the email input row in `SignInImpl` (`cardWarm` bg,
  hairline border, `radius 15`, mail-icon slot → replace with a country-code
  pill on the left).
- `keyboardType="phone-pad"`, `textContentType="telephoneNumber"`,
  `autoComplete="tel"`.

### `SignInImpl.tsx` changes
- Add `'phone'` to the `Stage` union.
- `AuthProviderStack`: add `onPhone` → `setStage('phone')`. (Add a "Continue
  with phone" row + a `logo` — use an Ionicons `call-outline` / `phone-portrait`.)
- New `phone` stage body: `PhoneNumberInput` + `Button size="auth"` "Send the
  code". On press call:
  ```ts
  await signIn.create({ identifier: e164 });          // phone as identifier
  const f = signIn.supportedFirstFactors?.find(x => x.strategy === 'phone_code');
  if (!f?.phoneNumberId) { /* no-account nudge → Sign up, mirror email O6 path */ }
  await signIn.prepareFirstFactor({ strategy: 'phone_code', phoneNumberId: f.phoneNumberId });
  setStage('code');
  ```
- **`code` stage: make it strategy-aware.** Today `handleVerifyCode` hardcodes
  `strategy: 'email_code'`. Introduce a `codeStrategy: 'email_code' | 'phone_code'`
  state set when entering the `code` stage, and pass it to `attemptFirstFactor`.
  This is the single most important correctness change — the OTP UI is shared,
  only the strategy differs.
- `shellCopyOverride`: add phone-stage copy ("What's your number?" / "We'll text
  a one-time code.") and verify copy ("Check your texts." / "Code sent to
  {formattedPhone}.").
- Resend / "Different number" / auto-submit-on-6-digits: reuse verbatim.

### `SignUpImpl.tsx` changes
- Same `phone` stage. `signUp.create({ phoneNumber: e164, firstName })` then
  `signUp.preparePhoneNumberVerification({ strategy: 'phone_code' })`, and in the
  `code` stage call `signUp.attemptPhoneNumberVerification({ code })` when the
  chosen factor is phone.
- `parseClerkError` already handles Clerk's error shape — reuse. Add the
  `form_identifier_exists` → "that number already has an account, sign in"
  branch, mirroring the email one.
- Onboarding hand-off (`SafetyChipsForm`, intent replay) is unchanged.

### Utilities
- `utils/authContext.ts` — no change (context is source-agnostic).
- Optionally add `formatE164ForDisplay()` helper for the verify-stage subtitle.

### Files touched (frontend)
- NEW `components/onboarding/PhoneNumberInput.tsx`
- EDIT `components/onboarding/AuthProviderStack.tsx` (one new row + prop)
- EDIT `components/auth/SignInImpl.tsx` (phone stage + strategy-aware code)
- EDIT `components/auth/SignUpImpl.tsx` (phone stage + strategy-aware code)
- ADD dep `libphonenumber-js` (+ maybe `expo-localization` if not present)
- Maestro flow + a mock-walk assertion for the phone path

---

## Backend plan (minimal)

**Required: nothing.** Clerk-managed phone auth provisions users through the
existing `sub` → `external_auth_id` path. Ship the FE and it works.

**Optional (nice-to-have, do later, not for first cut):**
- Persist the verified phone to `users.phone_number` so we can (a) show it in
  account settings and (b) power SMS trip-invites later. Read it from the Clerk
  JWT/session claims (add `phone_number` to the Clerk JWT template) or from a
  Clerk webhook (`user.updated`) → upsert `users.phone_number` + stamp
  `phone_verified_at`. This reuses the dormant columns for *storage only*, not
  for OTP issuance.
- If we never do the above, file a cleanup ticket to drop the five `phone_otp_*`
  columns + `uq_users_phone_number`, since they imply a scheme we won't build.

**Explicitly out of scope:** any `/phone`, `/otp`, or SMS-send route on our
backend. That is the self-managed path we are rejecting.

---

## Clerk dashboard config

1. **User & Authentication → Phone** → enable *Sign-up with phone* and *Sign-in
   with phone*. (This is the toggle that makes `phone_code` a supported factor.)
2. Confirm SMS is enabled for the instance and check the SMS budget / pricing on
   the current Clerk plan.
3. Dev instance already has **test mode on by default** — fictional numbers in
   the `+1 (XXX) 555-0100`–`0199` range accept the universal OTP `424242` with no
   real SMS. Use one for the Apple review notes and Maestro. (Corrects the stale
   `Apple Review Notes.md`, which currently describes a phone flow that doesn't
   exist yet and an invalid `+15555555555` number.)
4. For public launch on the `pk_live` prod instance, re-enable phone there too
   (instance settings don't carry over from dev).

---

## Account-linking edge cases (design + logic must both answer these)

These are where phone auth gets subtle. Decide the posture explicitly:

- **Same human, different factors.** Mara signs up with email today, tries phone
  next month. Clerk treats phone and email as separate identifiers on possibly
  separate users unless linked. Decide: do we let Clerk auto-link by verified
  contact, or accept two accounts? Simplest v1 posture: **each identifier is its
  own account; no auto-merge.** Document it; don't silently merge.
- **No-account-on-sign-in.** Mirror the email O6 nudge exactly: "we don't have an
  account for that number — sign up?"
- **Number already registered on sign-up.** Mirror `form_identifier_exists` →
  "that number already has an account — sign in."
- **Number change / re-use.** Out of scope for v1; Clerk owns it.

---

## Testing / QA

- **Maestro:** new `phone-signin.yaml` flow using a `+1XXX5550100` test number +
  `424242`. Add to the auth QA lane.
- **Mock-walk:** assert the `phone` stage renders, the strategy-aware `code`
  stage verifies with `phone_code`, and post-auth lands on Trips.
- **Manual matrix:** sign-up-phone, sign-in-phone, wrong-code, resend, different-
  number, no-account nudge, already-exists nudge, country-code ≠ +1.
- **Regression:** email + OAuth paths unchanged (the strategy-aware `code` stage
  is the risk surface — assert email still verifies with `email_code`).

---

## Rollout

- Gate behind a FE flag `AUTH_PHONE_ENABLED` (mirror `featureFlags.ts` pattern)
  so the "Continue with phone" row can ship dark and flip after the Clerk toggle
  + Maestro pass are both green. This keeps it off the v1 critical path while
  making it a one-line flip when we want it.
- Ship order: Clerk dashboard toggle → FE behind flag → Maestro green → flip flag.

---

## Effort / risk

| Piece | Size | Risk |
|---|---|---|
| `PhoneNumberInput` + libphonenumber | ~0.5–1 day | country-code correctness |
| Strategy-aware `code` stage (both screens) | ~0.5 day | **regression risk on email** — test it |
| Phone stage wiring (both screens) | ~0.5 day | low |
| Clerk config + test numbers | ~0.5 hr | low |
| Optional: persist phone to `users` | ~0.5 day | low, deferrable |
| Design (screens + states) | see brief | low (reuses canon) |
| Maestro + mock-walk | ~0.5 day | low |

**Total ≈ 2–3.5 days.** Bounded because the staged-flow machinery, the OTP
input, the shell, and the backend identity resolution all already exist.

---

## Design — source of truth (canon 136)

**Implement the phone screens from the canon 136 handoff bundle. It is the
pixel-perfect design; do not re-derive it.**

### Where it is
```
design/vesper-canon-anchor/project/
├── AUTH-PHONE.md                          # vendoring note + RN mapping
├── Vesper Auth and Invite.html            # entry; open this first, follow its <script> imports
├── design-canvas.jsx                      # canvas harness (dependency)
├── kicker.jsx                             # VKicker mono eyebrow (dependency)
├── auth-invite-app.jsx                    # AU tokens + shared primitives + provider stack
│                                          #   (now includes ProviderButton provider="phone")
└── auth-phone.jsx                         # ← THE PHONE DESIGN: 8 screens + primitives board
```
Load order (from the HTML): `design-canvas → kicker → phone → auth-invite-app →
auth-phone`. `auth-phone.jsx` depends on primitives defined in `auth-invite-app.jsx`
(`AU`, `Phone`, `BackNav`, `Kicker`, `AuthField`, `OtpInput`, `PrimaryButton`,
`GhostButton`, `InlineError`, `InlineNotice`, `ProviderButton`) — read that file too.

> **Durability note:** Canon 136 is vendored in-repo at
> `design/vesper-canon-anchor/project/` (`auth-phone.jsx`, updated
> `auth-invite-app.jsx`, `Vesper Auth and Invite.html`). See
> `design/vesper-canon-anchor/AUTH-PHONE.md`. The self-contained spec below
> is the fallback if those files are removed.

### Self-contained spec (extracted verbatim from `auth-phone.jsx`)

Everything here is DM Sans unless noted. **Phone entry/verify screens use a PLAIN
DM Sans subtitle, NOT the italic EB Garamond line** — only the provider-stack
shell screens (`ScreenAuthTrip`/`ScreenAuthReturning`) use the italic serif
subtitle. Screen frame: `Phone` 393×852 on `AU.bg`, content padded `22px 22px 28px`,
`BackNav` at top.

**AU palette (hex):** `bg #EDE8DC` · `sheet #F9F5ED` · `card #F4EFE4` ·
`ink #1B1714` · `mute #6E6862` · `muteSoft #B0A9A2` · `hair rgba(27,23,20,0.10)` ·
`hairThin rgba(27,23,20,0.06)` · `amber #B0853A` (accent) · `oxblood #7A2E20`
(error) · `green #3A5C3A` (success). Buttons are DARK (`ink` fill, `#FBF7EC` text).

**Header rhythm (every phone screen):** `Kicker` (mono 9px, letter-spacing 2,
`AU.amber`) → title (DM Sans **22px**, weight 700, letter-spacing −0.5, lineHeight
1.2, `AU.ink`) → subtitle (DM Sans **14px**, `AU.mute`, lineHeight 1.5 — plain, not
italic).

**New primitives in `auth-phone.jsx`:**
- `CountryPill` — flag emoji (16px) + dial code (DM Sans 15, `AU.ink`), a `0.5px
  AU.hair` right-divider; sits inside the field on the left.
- `PhoneField` — `AuthField` geometry (h50, r12, `card`/`sheet`-focused,
  hair/ink/oxblood border, `AU.amber` focus caret) with `CountryPill` embedded
  left. Label `PHONE NUMBER` (mono 9). Placeholder `(415) 555-0134`.
- `PHONE_ICON` — line handset SVG, `#1B1714` stroke 1.3, matching apple/google/email
  icon weight (added to `PROVIDER_ICONS` so `<ProviderButton provider="phone">` works).
- `COUNTRIES` — US, CA, GB, PT, FR, JP, ES, DE, MX, IT (flag + name + dial). This is
  a design sample; production uses `libphonenumber-js`'s full list (see FE plan).

**The 8 screens (component → copy):**
| Component | Kicker | Title | Subtitle / body | Notable |
|---|---|---|---|---|
| `ScreenPhoneEntry` | PHONE | "What's your number?" | "We'll text a one-time code. No password needed." | `PhoneField` + `PrimaryButton` "Send the code" + "Other ways to continue" + footer "We'll only text this number to verify it's you." · link "Sign up instead". Error variant `format`: field shows "That doesn't look like a complete number." |
| `ScreenPhoneVerify` | VERIFY | "Check your texts." | "Code sent to **{+1 (415) 555-0134}**" (destination bold `ink`) | `OtpInput` (reused as-is) + `{n}/6 digits`→"Verifying…" counter (muteSoft, center) + "Resend code" box (cooldown → "Resend in {n}s", muteSoft) + "Different number". `error` → `InlineError` "That code isn't right. Try again or resend." |
| `ScreenPhoneNoAccount` | PHONE | "What's your number?" | same | `InlineError` "We don't have an account for this number." action "New here? Sign up instead." + `PrimaryButton` disabled |
| `ScreenPhoneAlreadyRegistered` | PHONE | "Create your account." | same | `InlineError` "This number already has a Vesper account." action "Sign in instead — it's the same code." + disabled button (this is the **sign-up** variant) |
| `ScreenPhoneVerified` | VERIFY | "Check your texts." | destination line | `InlineNotice` green "Verified. Opening Vesper…" + filled `OtpInput` |
| `ScreenCountryPill` | PHONE | "What's your number?" | same | Closed country pill w/ chevron; hint "Tap the flag to change country." |
| `ScreenCountryPickerSheet` | PHONE | "What's your number?" | — | Bottom sheet: grabber, "Country or region" title, "Search countries" field, country rows (flag + name + dial) |
| `PhoneComponentBoard` | — | "Phone primitives" | — | Reference board: CountryPill, PhoneField idle/focused/error, phone ProviderButton idle/loading |

**Provider-stack placement (from `auth-invite-app.jsx`):** the stack now renders
`Apple · Google · email · phone` (phone LAST, after the `OrDivider` that splits the
OAuth pair from the identifier methods). All four are equal visual weight.

### FE mapping (canon component → RN target)
- `PhoneField` + `CountryPill` → `components/onboarding/PhoneNumberInput.tsx`
- `ScreenCountryPickerSheet` → a country-picker bottom sheet (reuse the app's
  existing sheet primitive; rows = flag + name + dial)
- phone `ProviderButton` row → new entry in `components/onboarding/AuthProviderStack.tsx`
- `ScreenPhoneVerify` → reuse `components/onboarding/OtpCodeInput.tsx` verbatim;
  only the strategy (`phone_code`) and the destination-in-subtitle differ
- `InlineError`/`InlineNotice` copy → the toast/inline messages in the FE plan's
  "account-linking edge cases" section (strings match, so use them verbatim)
