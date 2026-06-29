# EAS Five-Pack Phone Walk — Operator Script

> Status: ready to run  
> Created: 2026-06-29  
> Preflight: `make dogfood-fly-smoke` **PASSED** (mara + elif audit, Rome slug bridge 9/9)

**Build:** EAS dogfood profile — `EXPO_PUBLIC_USE_MOCK_API=false`, API `https://vesper-backend.fly.dev`  
**Accounts:** `mara@dogfood.local` (Lisbon) · `elif@dogfood.local` (Rome, Istanbul, Tokyo, Brooklyn)  
**Record:** Check boxes in [docs/journeys/STATUS.md](../journeys/STATUS.md) Manual phone walk section.

---

## Preflight (5 min)

```bash
make dogfood-fly-smoke          # Fly API + persona audit + Rome bridge
curl -sf https://vesper-backend.fly.dev/ready
```

Confirm EAS build is the **dogfood** channel (not mock). Sign in with Clerk dogfood cohort.

---

## 1. Mara — Lisbon (S4 flagship) · ~15 min

**Trip:** `mara-lisbon` manifest — title **"Lisbon"**, Oct 3–6 2026, members Mara / Dao / Reza.

| Step | Action | Pass if |
|------|--------|---------|
| L1 | Trips → open **Lisbon** group trip | Hero, dates, 3 members visible |
| L2 | **Plan** → Day 1 | "Casa do Alentejo — first dinner" block with real venue name (not stub) |
| L3 | **Discover** → search *"first night Lisbon dinner close by, not touristy"* | Board returns ≥3 venue cards (Casa do Alentejo, Mouraria, etc.) |
| L4 | Open a venue card → **Ask Vesper** | Seed cites venue + Lisbon context |
| L5 | **Atlas** → open **mara-lisbon-group-arrival** artifact | Ready story; map point at Confeitaria Nacional (not experience-only slug) |
| L6 | Group chat | Mara / Dao / Reza thread visible; first-dinner vote topic |

**Fail signals:** empty Discover board, generic venue titles, atlas `partial`, Vesper ignores trip context.

---

## 2. Elif — Rome · ~10 min

**Trip:** `elif-rome-return-2026` — **"Rome return planning"** (or Trips home equivalent).

| Step | Action | Pass if |
|------|--------|---------|
| R1 | Open Rome return trip | Testaccio / Trastevere planning visible |
| R2 | Plan Day 2 | **Testaccio Market** block references real corpus venue |
| R3 | Vesper (group): *"Testaccio and Trastevere food walks"* | Reply cites seeded venues / neighborhoods |
| R4 | Discover: *"Rome like last time"* or *"one reservation loose"* | Non-empty board |

---

## 3. Elif — Istanbul · ~8 min

**Trip:** `elif-istanbul-return-2026` — pending Atlas candidate / ferry beats.

| Step | Action | Pass if |
|------|--------|---------|
| I1 | Open Istanbul trip | Kadıköy / ferry context in plan or Vesper read |
| I2 | Discover: *"ferry food classic"* or *"skip the obvious"* | Board with Istanbul venues (not generic pool) |
| I3 | Atlas candidate (if surfaced) | Ferry / water-base beats feel authored |

---

## 4. Elif — Tokyo · ~8 min

**Trip:** `elif-tokyo-2025` — counter / market slice.

| Step | Action | Pass if |
|------|--------|---------|
| T1 | Open Tokyo trip | Counter / market framing in plan or home |
| T2 | Discover: *"Tokyo counters"* or *"early morning market"* | Venue cards from promoted JSON corpus |
| T3 | Venue detail | Brief text present (not empty shell) |

---

## 5. Elif — Brooklyn · ~8 min

**Trip:** `elif-brooklyn-local-week`.

| Step | Action | Pass if |
|------|--------|---------|
| B1 | Open Brooklyn trip | Counter / neighborhood week visible |
| B2 | Discover: *"Brooklyn mornings"* or *"lived-in neighborhoods"* | Board with Brooklyn venue cards |
| B3 | Visual | Place art or backend photo (not generic category pool only) |

---

## Optional — Tier A spot-check on EAS (~2 min each)

After latent promote, ad-hoc trips: Paris *"natural wine bistro"*, Barcelona *"vermouth bar tapas"*, Venice *"cicchetti bacaro"*, Amalfi *"limoncello terrace"*, Nice *"socca old town"*.

---

## J02 / J05 live extensions (second device)

If validating certify-live human gates, see [wedge-journey-02-05-path-to-dogfood.md](wedge-journey-02-05-path-to-dogfood.md): invite accept on Device B, proposal accept/reject, privacy DM (I4).

---

## When done

Update [STATUS.md](../journeys/STATUS.md) five-pack checkboxes and Maestro row (J02/J05) if `make certify-visual` green.
