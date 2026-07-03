# Prompt 02 — Invite, Join, Auth, And Deep Links

```text
You are a Cursor Cloud agent auditing Travel Workspace for dogfood readiness.

Use the common rules in:
docs/audits/dogfood-readiness-2026-05/prompts/00-common-instructions.md

Area:
Invite/join flow, auth detours, token handling, Universal Links/deep links.

Output:
docs/audits/dogfood-readiness-2026-05/areas/02-invite-join-auth-deeplinks.md

Product promise:
A friend can tap an invite, give private signal, sign in if needed, join the right trip, and land in the shared workspace without losing context or exposing bearer tokens.

Inspect:
- Travel Agent invite routes, invite models, token generation/storage, accept/intake semantics.
- AASA/assetlinks routes and deploy env assumptions.
- Auth mode handling: SKIP_AUTH false/true, Clerk JWT, current user identity.
- Travel App invite landing route, auth redirect persistence, deep link routing, onboarding chips.
- Notification or pending invite surfaces.

Start with:
- docs/reliability/traces/create-trip-and-invite-group.md
- docs/Owner Action Items.md
- docs/Deploy & Rollback Runbook.md
- Travel Agent/tests/api/test_invites_api.py
- Travel Agent/tests/api/test_invite_landing.py
- Travel App/app/invite/[slug].tsx
- Travel App/docs/page-specs/trip-group-chat.md

Audit questions:
1. Is invite accept idempotent for mobile retry after a lost success response?
2. Are raw invite tokens absent from logs, events, notifications, analytics, and IDs where not needed?
3. Does pre-auth intake survive sign-in and attach to the same user/trip?
4. Can a consumed/expired invite produce a scary false failure for someone already added?
5. Are Universal Link and fallback paths production-realistic?
6. Are organizer-visible pending invite summaries privacy-safe?
7. Are auth-disabled dev paths prevented from leaking into release builds?

Run if cheap:
- make contract-check
- targeted invite API tests
- targeted invite/auth frontend tests

Deliver:
Focus on first-user dogfood breakage: failed join, wrong trip, lost intake, leaked token, or misleading expired state.
```

