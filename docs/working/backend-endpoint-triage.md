# Backend Endpoint Triage

> **UPDATE 2026-06-27: headline count PARTIALLY STALE — ~62 → ~54.**
> Cross-referencing the [cross-repo seam audit (2026-06-25)](../audits/cross-repo-seam-audit-2026-06-25.md)
> and the 2026-06-24..26 fix sprint, **8 endpoints this doc lists as
> uncalled now have a confirmed FE client** in `travel-app/utils/api/http.ts`:
>
> | Path | Method | Old verdict | FE client |
> |---|---|---|---|
> | `/api/me` | GET | unknown | `http.ts:546` |
> | `/api/users/{*}/intake` | POST | planned | `http.ts:553` |
> | `/api/users/{*}/devices` | GET | planned | `http.ts:918` |
> | `/api/trips/{*}/booking/sessions` | POST | unknown | `http.ts:1007` |
> | `/api/trips/{*}/geofence-events` | POST | planned | `http.ts:1847` (GET still uncalled) |
> | `/api/trips/{*}/voice-guide/session` | GET | unknown | `http.ts:1861` |
> | `/api/trips/{*}/voice-guide/session/close` | POST | unknown | `http.ts:1865` |
> | `/api/trips/{*}/debrief` | POST | unknown | `http.ts:2080` |
>
> Most of the **action-items** table below is now answered: `/api/me`,
> booking sessions, both voice-guide endpoints, and debrief are wired.
> Still genuinely uncalled (per seam-audit §4 "missing clients"):
> `/api/trips/{*}/expenses/{*}/comments` GET (#23), `/api/takes/{*}` GET,
> `/api/trips/{*}/geofence-events` GET (#20), `/api/research/*`,
> `/api/lookup/`, `/api/curator/photos`, plus `plan-similar`/`plan-seed`/
> `action-receipts/recent` (not in the count below). **Re-run
> `python3 scripts/api-coverage-check.py --list-unused` to regenerate
> the authoritative list before acting on the count.**

Audit of the 62 endpoints exposed by the Travel Agent backend (per
`docs/openapi.json`) that the Travel App frontend does **not** call.

Generated against the snapshot shipped with the
`docs(openapi): refresh snapshot for event_state + (in-flight) story photo slot`
commit. Re-run `python3 scripts/api-coverage-check.py --list-unused`
to regenerate the source list.

## Verdict legend

- **planned** — UI surface is intentional and coming. Keep the route.
  Frontend will wire it up later.
- **deprecated** — never wired, no near-term plan to surface. Candidate
  for backend removal in a follow-up sweep. Safe to skip in the coverage
  gate (see `--ignore` flag).
- **infrastructure** — health, debug, metrics, webhooks, admin tooling.
  Not meant to be called from the app; will stay backend-only forever.
  Treated as deprecated by the gate (skip), but kept on the backend.
- **unknown** — needs owner review. **Action items at the top of this
  doc.**

---

## Action items — unknown verdicts

Owner input needed on these endpoints:

| Path | Method | Question |
|---|---|---|
| `/api/me` | GET | Why does the frontend not call this? `useUser`/`UserContext` likely should — verify it isn't using a different shape. |
| `/api/conversations/{*}` | GET | Single-conversation read. Likely planned for a conversation deep-link route — confirm or deprecate. |
| `/api/conversations/{*}/messages/{*}/reactions` | GET | Reaction list per message. Confirm whether reaction display reads this or pulls reactions inline with the message. |
| `/api/trips/{*}/voice-guide/session` | GET | Voice-guide session reads. There's a corresponding `/close` POST — confirm if the voice-guide MVP needs the GET. |
| `/api/trips/{*}/voice-guide/session/close` | POST | Same as above. |
| `/api/curator/photos` | POST | Curator-side photo ingest — confirm whether this is operator-only (move to admin) or planned for an in-app curation flow. |
| `/api/trips/{*}/messages/close` | POST | Closing a thread message stream. Probably needed by the chat lifecycle — confirm. |
| `/api/research/deep`, `/api/research/quick` | POST | "Research" endpoints. Confirm whether these are user-facing (planned) or internal-tool-only (deprecate/infra). |
| `/api/lookup/` | POST | Lookup endpoint. Confirm purpose — possibly internal agent tool. |
| `/api/trips/{*}/debrief` | POST | Trip debrief. Confirm planned vs. deprecated. |
| `/api/trips/{*}/booking/sessions` | POST | Creates a booking session. App reads sessions but does it create them or are they backend-spawned only? |

---

## Dossiers

| Path | Method | Verdict | Note |
|---|---|---|---|
| `/api/dossiers/{*}` | GET | planned | Generic dossier detail — Dossier UI is on the roadmap. |
| `/api/dossiers/accommodation/{*}` | GET | planned | Same. |
| `/api/dossiers/site/{*}` | GET | planned | Same. |

> Three GETs. Hold all three for the dossier UI work.

## Booking sessions

| Path | Method | Verdict | Note |
|---|---|---|---|
| `/api/trips/{*}/booking/sessions` | POST | unknown | See action items. |
| (Booking session reads — already covered by app via different routes.) | | | |

> Note: the coverage check shows POST `/api/trips/{*}/booking/sessions`
> as backend-only; the listed "6 booking session reads" the task brief
> mentioned are all covered by the frontend today.

## Narration

| Path | Method | Verdict | Note |
|---|---|---|---|
| `/api/trips/{*}/narration/audio/{*}/{*}` | GET | planned | Audio chunk fetch — the geofence narration path uses this server-side; the app streams via SSE today. Keep. |

## Experiences & Collections

Currently no `/experiences/*` or `/collections/*` paths appear in the
backend-only list — the app surfaces them. Task brief's "8 experiences
/ collections" figure is stale.

## Conversations & messages

| Path | Method | Verdict | Note |
|---|---|---|---|
| `/api/conversations/{*}` | GET | unknown | See action items. |
| `/api/conversations/{*}/messages/{*}/reactions` | GET | unknown | See action items. |
| `/api/conversations/{*}/invites/{*}` | DELETE | planned | Revoke-invite from conversation. Belongs to the invite-management surface. |
| `/api/conversations/{*}/location` | POST | planned | Set conversation location context. Likely wired by upcoming location-handoff feature. |
| `/api/conversations/{*}/messages` | POST | planned | Direct conversation send. App uses the streaming variant today; non-streaming may be wired for offline/retry. |
| `/api/conversations/{*}/messages/stream` | POST | planned | Same as above. |
| `/api/trips/{*}/messages/info` | GET | planned | Thread metadata read. |
| `/api/trips/{*}/messages/stream` | POST | planned | Streaming send to trip thread (parallel to concierge stream). |
| `/api/trips/{*}/messages/close` | POST | unknown | See action items. |

## Memory, observations, events

| Path | Method | Verdict | Note |
|---|---|---|---|
| `/api/me` | GET | unknown | See action items. |
| `/api/users/{*}/intake` | POST | planned | Onboarding intake — app probably uses a different path or this is the new one. Confirm with onboarding owner. |
| `/api/users/{*}/devices` | GET | planned | Device registration introspection — admin-ish. May move to admin namespace. |
| `/api/events/users/{*}` | GET | planned | User event timeline read — feeds digest UI when wired. |
| `/api/trips/{*}/geofence-events` | GET | planned | Read-side geofence events for trip — wired by upcoming map state debug overlay. |
| `/api/trips/{*}/geofence-events` | POST | planned | Write-side geofence events (client emits). Wired by app currently? Verify — should probably already be covered. |

## Trip-scoped reads & writes (misc)

| Path | Method | Verdict | Note |
|---|---|---|---|
| `/api/takes/{*}` | GET | planned | Single-take detail. Take detail route exists in app — confirm wiring. |
| `/api/trips/{*}/expenses/{*}/comments` | GET | planned | Expense-thread comments. Wired by expense detail view when comments ship. |
| `/api/trips/{*}/receipts/{*}/image` | GET | planned | Receipt image fetch. Wired by receipt-thumb in expense detail. |
| `/api/trips/{*}/photos` | POST | planned | Photo upload. App uses a different (presigned) upload flow today; this is the legacy path or a parallel one. Owner check. |
| `/api/trips/{*}/digest/email` | POST | planned | Trigger digest email send for trip. |
| `/api/trips/{*}/debrief` | POST | unknown | See action items. |
| `/api/trips/{*}/voice-guide/session` | GET | unknown | See action items. |
| `/api/trips/{*}/voice-guide/session/close` | POST | unknown | See action items. |
| `/api/curator/photos` | POST | unknown | See action items. |
| `/api/research/deep` | POST | unknown | See action items. |
| `/api/research/quick` | POST | unknown | See action items. |
| `/api/lookup/` | POST | unknown | See action items. |

## Admin tooling (will never be in-app)

| Path | Method | Verdict | Note |
|---|---|---|---|
| `/admin/digests/{*}` | GET | infrastructure | Operator dashboard. |
| `/admin/digests/retry` | POST | infrastructure | Operator dashboard. |
| `/admin/ingestion-status` | GET | infrastructure | Operator dashboard. |
| `/admin/trips/{*}/digest/daily/{*}` | GET | infrastructure | Operator dashboard. |
| `/admin/trips/{*}/digest/daily/{*}` | POST | infrastructure | Operator dashboard. |
| `/admin/trips/{*}/digest/planning-context` | GET | infrastructure | Operator dashboard. |
| `/admin/trips/{*}/digest/planning-context` | POST | infrastructure | Operator dashboard. |
| `/admin/trips/{*}/digest/summary` | GET | infrastructure | Operator dashboard. |
| `/admin/trips/{*}/digest/summary` | POST | infrastructure | Operator dashboard. |
| `/admin/trips/{*}/digests` | GET | infrastructure | Operator dashboard. |
| `/admin/trips/{*}/notification-stats` | GET | infrastructure | Operator dashboard. |
| `/admin/users/{*}/constraints` | GET | infrastructure | Operator dashboard. |
| `/admin/users/{*}/constraints` | POST | infrastructure | Operator dashboard. |
| `/admin/users/{*}/constraints` | DELETE | infrastructure | Operator dashboard. |
| `/admin/users/{*}/events` | GET | infrastructure | Operator dashboard. |
| `/admin/users/{*}/observations` | GET | infrastructure | Operator dashboard. |
| `/admin/users/{*}/personal-memory` | GET | infrastructure | Operator dashboard. |
| `/admin/users/{*}/reflections` | GET | infrastructure | Operator dashboard. |
| `/admin/users/{*}/reflect` | POST | infrastructure | Operator dashboard. |
| `/admin/users/{*}/refresh-memory` | POST | infrastructure | Operator dashboard. |
| `/api/admin/voice-metrics` | GET | infrastructure | Operator dashboard. |
| `/api/admin/discover/trending` | POST | infrastructure | Operator/curator tool. |

## Infra: health, debug, metrics, webhooks

| Path | Method | Verdict | Note |
|---|---|---|---|
| `/health` | GET | infrastructure | Load balancer / uptime check. |
| `/health/background-tasks` | GET | infrastructure | Internal worker health. |
| `/ready` | GET | infrastructure | K8s readiness probe. |
| `/debug/cost` | GET | infrastructure | Dev/debug. |
| `/debug/tokens` | GET | infrastructure | Dev/debug. |
| `/metrics/tokens` | GET | infrastructure | Prometheus / metrics scrape. |
| `/webhooks/bland-ai/call-complete` | POST | infrastructure | Inbound webhook. |
| `/webhooks/twilio/message-reply` | POST | infrastructure | Inbound webhook. |

---

## Coverage gate integration

Lines marked `deprecated` or `infrastructure` are eligible to be skipped
by the coverage check via the opt-in `--ignore` flag:

```bash
python3 scripts/api-coverage-check.py --ignore docs/working/backend-endpoint-triage.md
```

Without the flag the gate reports them as "Backend-only (informational)"
— the default behavior is unchanged. Use the flag in operator dashboards
or follow-up audits where the focus is finding actually-orphaned planned
routes.
