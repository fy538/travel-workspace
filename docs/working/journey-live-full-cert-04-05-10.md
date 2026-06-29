# Journey live full certification — J04, J05, J10

> Status: active runbook  
> Owner: founder / engineering  
> Last updated: 2026-06-29  
> Goal: close **full-certified** for journeys that require live gates (J04, J05, J10)

## Certification ladder (these journeys)

| Tier | What it proves | Command / action |
|------|----------------|------------------|
| **Agent** | Mock-walk + logic + Maestro (where required) | `make certify-logic` + `make certify-visual` |
| **Live API** | Two-persona real routes (organizer + member) | `make dogfood-journey-live-api` |
| **Device** | Clerk, LLM copy, booking UI, share sheet | This doc — two phones / simulators |

**Full certified** for J04/J05/J10 = all three tiers green.

Automated live API covers backend trust invariants (I1–I3 invite, I5/I7/I8 proposal apply, J04 redaction read path, J10 stay/expense boundaries). Device walks cover what HTTP cannot: streaming concierge copy, notification previews, checkout deeplinks.

---

## Preflight (every run)

```bash
make dogfood-fly-smoke                    # Fly substrate + personas
make dogfood-journey-live-api             # local TestClient — must be 15/15
make certify-visual                       # Maestro 24 + 25 (J02/J05 wedge UI)
```

Fly HTTP (optional, needs two Clerk JWTs):

```bash
TRANSPORT=http \
  PRELAUNCH_JWT_MARA=<organizer-jwt> \
  PRELAUNCH_JWT_DAO=<member-jwt> \
  make dogfood-journey-live-api PROFILE=fly
```

EAS dogfood build: `USE_MOCK=false`, API `https://vesper-backend.fly.dev`, Clerk dogfood channel.

**Accounts (S4 wedge):**

| Role | Email | Password (dogfood seed) |
|------|-------|-------------------------|
| Organizer | `mara@dogfood.local` | (seed) |
| Member | `dao@dogfood.local` | (seed) |

Trip: Mara **Group taste demo** (`mara-lisbon` on Fly).

---

## J05 — Proposal → Plan (required live)

**Automated:** `dogfood-journey-live-api` — create trip, proposal accept/apply, plan-state (TestClient).  
**Maestro:** flows 24 + 25 on simulator (already green in certify-visual).  
**Device (two-account):**

1. **Device A (Mara)** — open S4 Lisbon trip → Trip info → mint invite (or use existing Dao member).
2. **Device B (Dao)** — open invite link → sign in if needed → accept → land on same `tripId`.
3. **Device A** — group chat: ask Vesper for a plan change (e.g. “move Friday dinner later”).
4. **Both** — open Changes / proposal sheet → vote or organizer resolve → accept.
5. **Both** — verify Plan shows mutation; Changes shows receipt (I5).
6. **Device A** — revert if UI offers it → Plan + Home match (I6).
7. **Both** — Home / Plan / Changes / Map titles agree (I9).

Record: `docs/journeys/STATUS.md` — set J05 **Live** → `ready` when device walk passes.

---

## J04 — Private → Group-Safe (required live)

**Automated:** proposal GET redaction + privacy audit event (`J04` checks in `dogfood-journey-live-api`).  
**Device (two-account) — I4 is the trust event:**

1. **Device B (member)** — private Vesper chat for the trip (not group thread).
2. Send a **specific private phrase** you can grep for (e.g. “I need quiet mornings before long days”).
3. **Device A (organizer)** — group chat: ask Vesper to adjust plan using group context.
4. **Device A + B** — group thread must **never** show the raw private phrase or name the member.
5. Proposal / plan copy uses public-safe language only.
6. Optional: Atlas privacy / data receipt shows audited use without leaking phrase.

Record: J04 **Live** → `ready` when I4 spot-check passes on device.

---

## J10 — Booking / Stay / Expense (required live)

**Automated:** organizer vs member stay ACL, expense opt-in (`J10` in `dogfood-journey-live-api`).  
**Device (two-account):**

1. **Device A** — Trip Folio → Stay → add group base (or open seeded Alfama stay).
2. **Device B** — same trip → Stay: sees group label, **not** organizer private payment fields.
3. **Device A** — opt in cost to shared expenses (if not auto).
4. **Both** — Costs: member sees split, not card numbers or provider confirmation secrets.
5. **Device A** — open booking session from chat (if available) → confirm hold path shows terms + human approval; **never** shows “booked” before provider state.
6. **Device B** — booking surfaces show public-safe state only.

Record: J10 **Live** → `ready` when organizer/member visibility matches above.

---

## After all three pass

Update `docs/journeys/STATUS.md`:

- J04, J05, J10 **Live** column → `ready`
- **Certified** column → `full` (for those rows)
- Summary **Journey full-certified** count → `3 / 12` (or more if others completed)

```bash
make certify-live   # preflight + prints this checklist
```

---

## What we are not blocking on

- Duffel live checkout (money-moving) — verify hold/confirm **UI** only; provider stays dark unless explicitly enabled.
- Push notification delivery — in-app notification feed is enough for first cert.
- Third external TestFlight user (wedge doc DoD 8) — optional after founder two-device pass.
