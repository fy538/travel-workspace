# Persona Cast Consolidation Plan

> Status: accepted 2026-07-08 — Cut 1 done; Cut 2 partial (resolver + ledger built;
> derive-from-seed + test repointing deferred, need live seeded stack)
> Owner: founder / engineering
> Created: 2026-07-08
> Source of truth: `travel-agent/tools/dogfood/content/scenarios.yaml`
> (extended per this doc) + `docs/product/Dogfood Scenario Matrix.md` (human narrative)

## Decisions (resolved 2026-07-08)

1. **`default`/Alex** → **delete** (Cut 3; still referenced by FE tests, so deferred not
   immediate). Smoke coverage comes from real seeded identities once mocks are derived.
2. **Live/returned/between substrate** → **do not seed**; `force_state` fixtures on the six
   are enough for cohort 1 (those phases are outside the create→invite→plan→propose walk).
3. **Derive-from-seed script** → **Cut 2**; Cut 1 hand-waves FE mocks and just wires the
   wedge cast into the registry so the device walk seeds from one known cast.
4. **Second group organizer** → **accept mara-as-SPOF** for cohort 1; mitigate by hardening
   her Lisbon seed, not by duplicating. Second organizer is post-cohort-1 (for a *different*
   group dynamic, not redundancy).
5. **Port carmen's budget/fatigue constraint onto a Mara group member** → **DONE
   2026-07-08.** Carrier changed from Dao to **Reza** on evidence: Dao already owns the
   canonical J04 private-DM vector (`dao-quiet-mornings`, `shared: false`), so putting budget
   on Reza spreads the private-leak test across two members and gives Reza a public/private
   split (shares his shellfish allergy openly, hides budget stress). Seeded as observation
   `reza-budget-private` in `manifests/lisbon-phase1.yaml` (`shared: false`,
   `product_moment: J04-private-dm`); validates against `ObservationSeed`. Dossier updated
   (`sources/lisbon-phase1/persona-dossiers.md` Reza privacy posture + must-not-leak).
6. **Taste-diversity expansion (two distant identities)** → **hold** until dogfood shows
   connoisseur over-fit; add demand-driven, not speculatively.

> Schema note: `persona:` on each scenario is the **foreign key** into the new `identities:`
> block (no separate `identity:` field — avoids duplication). `default` is intentionally
> absent from the registry pending its Cut-3 delete.

## Decision

Collapse the persona cast onto the **six identities that already have real backend
seeds** — `elif`, `mara`, `dao`, `reza`, `mike`, `sarah` — make the **backend seed the
single source of truth**, and let the FE mock become a **derived snapshot of the seed**
rather than a hand-authored parallel. Lifecycle "personas" (cold / live / returned /
between / urgent) become **phases or scenarios of the six**, not separate people.
UI-contract fixtures (`torture`, empty states) move to a lane that is explicitly **not**
a persona. Logic QA's anonymous invariant fixtures are left untouched.

Net: **~14 half-overlapping personas → 6 real people + a phase dimension + a UI-vector
lane.**

## Why (the problem in one paragraph)

There are three casts that barely overlap: **13 FE mock bundles** + `default`
(`travel-app/constants/personas/`), **6 backend `@dogfood.local` seeds**, and Logic QA's
**anonymous `scenario_user`** fixtures. Only `elif` and `mara` exist on both the mock and
seed sides — and `M11-elif`'s own note admits the mock is "the ideal-state … **before**
backend-real Elif data is applied," i.e. a hand-drawn stand-in guaranteed to drift. Every
lifecycle-phase persona (`carmen` live, `dev` returned, `Morgan` between, `Riley` urgent)
is mock-only with no real substrate behind it. `theo` is a true orphan (in the FE cast,
absent from `scenarios.yaml` and the backend). The confusion isn't the *count* — it's that
**four different kinds of thing wear the same "persona" costume.**

## Target model — sort by KIND first

| Kind | What it is | Source of truth | Examples |
|---|---|---|---|
| **1. Real person** | A human a dogfooder could be | **Backend seed**; FE mock derived from it | elif, mara, dao, reza, mike, sarah |
| **2. Lifecycle phase** | A *state* of a real person, not a new person | A `phase` / force-state on kind 1 | live, returned, between, pre, urgent-decision |
| **3. UI-contract vector** | Not a person — a rendering assertion | Pure FE fixture, no backend | torture (overflow/unicode/media-fail), empty states |
| **4. Invariant fixture** | Not a person — a throwaway to prove a mechanism | Anonymous `@journey.test` uuid | Logic QA `scenario_user` |

Rule of thumb: assert a **mechanism** → kind 4 (anonymous). Demo an **experience** →
kind 1/2 (bound to a seeded identity). Assert a **rendering edge** → kind 3 (synthetic).

## The six canonical identities

Declared once, in a new top block of `scenarios.yaml`. Each has up to three *projections*
of the same person.

```yaml
identities:
  elif:
    display_name: Elif
    character: Returning traveler; cross-city archive; counter-food DNA. The solo/archive anchor.
    home_city: brooklyn
    projections:
      seed:    { account: elif@dogfood.local, clerk: user_3G621LSmNvoI83lwBU3cOsNeGq4 }
      mock:    { bundle: constants/personas/elif.ts, derived_from: S1-elif-mature-archive }
      fixture: identity
  mara:
    display_name: Mara
    character: Lisbon group organizer. Carries the wedge (create → invite → plan → propose).
    home_city: lisbon
    projections:
      seed:    { account: mara@dogfood.local, clerk: user_3G61xwb0fxRgMjBfRba8Rvgox4F }
      mock:    { bundle: constants/personas/mara.ts, derived_from: S4-lisbon-group-planning }
      fixture: identity
  dao:
    display_name: Dao
    character: Solo flat-city walker. Also a member in Mara's group trip.
    projections:
      seed:    { account: dao@dogfood.local }
      mock:    null            # GAP — no FE bundle today; derive one (see backfill)
      fixture: identity
  reza:
    display_name: Reza
    character: Solo pizza-tradition / facade-and-material detail. Member in Mara's trip.
    projections:
      seed:    { account: reza@dogfood.local }
      mock:    null            # GAP
      fixture: identity
  mike:
    display_name: Mike
    character: Solo natural-wine / shared-table. Elif's companion.
    projections:
      seed:    { account: mike@dogfood.local }
      mock:    null            # GAP
      fixture: identity
  sarah:
    display_name: Sarah
    character: Solo morning-protocol / walk-in-counter. Elif's companion.
    projections:
      seed:    { account: sarah@dogfood.local }
      mock:    null            # GAP
      fixture: identity
```

`mock: null` is an **explicit, reviewable gap** — not a silent absence. See backfill.

## Two new per-scenario fields (the consolidation key)

Add to every scenario. They let ONE file answer "which person+city proves which journey
on which rail" — which is how the rails consolidate **without merging**.

- `journeys: [Jxx, …]` — binds the scenario to the journey doc(s) it exercises.
- `rails: [logic_qa | maestro | mock_walk | five_pack | eval_world]` — which validation
  systems run this scenario. Each rail still resolves its fixtures from this registry.

A CI ledger can then assert: *every MVP-required journey has ≥1 scenario carrying both
`logic_qa` and `maestro`.* You don't have that coverage check today.

## Re-home mapping — every dangling persona → a phase/scenario of the six

Nothing is deleted until its coverage lands somewhere. Delete by **coverage**, not by name.

| Dangling (delete) | Covered | Re-homes to | New form |
|---|---|---|---|
| `M1 ana` cold-start | J01, empty states | **not a person** → fresh empty account + UI-empty fixture | `cold-start` fixture (kind 3) |
| `M2 ben` planning | planning phase | `mara @ Lisbon, phase=planning` (already S4 pre-proposal) | phase of mara |
| `M3 carmen` live-trip | J08 live | `mara @ Lisbon, phase=live` (force-state on the real seed) | phase of mara (carmen already `will-not-build`) |
| `M4 dev` just-returned | J12 post-trip | `elif @ Tokyo/Rome, phase=returned` (S5 kept-memory) | phase of elif |
| `M5 ready` leaving-soon | pre-trip calm | `phase=pre` on any seeded trip | pure phase |
| `M6 urgent` (Riley) | J05/J09 decision | scenario: `mara` trip with an open proposal awaiting votes | scenario of mara |
| `M7 between` (Morgan) | between-trips | `elif, phase=between` (archive, no active trip = S1) | phase of elif |
| `M8 nadia` archive | Atlas life-doc | absorbed into **elif** (she *is* the archive persona, S1) | delete, → elif |
| `M9 omar` fresh-find | discovery-from-memory | absorbed into elif/dao browsing Discover | delete, → elif/dao |
| `theo` Lisbon member | non-organizer vote surface | **dao or reza as a member** in Mara's S4 trip | delete, → dao/reza |
| `M0 default` (Alex) | legacy smoke | retire, or keep exactly ONE as the M0 smoke default | keep ≤1 or delete |
| `M10 torture` | overflow/unicode/media-fail | **UI-vector lane** (`fixtures/ui-vectors/`) | kind 3, not a persona |

Result: almost everything re-homes onto **elif** (solo / archive / returned / between /
discovery) and **mara** (planning / live / group-decision, as phases of her real trip).
The solo trio `dao/reza/mike/sarah` cover solo-taste variety + Mara's group members.

## Journey coverage after consolidation (proof nothing is lost)

| Journey | Owning scenario(s) | Identity |
|---|---|---|
| J01 vague idea | `cold-start` fixture + S1 promotion | fresh / elif |
| J02 create + invite | S4 | mara (+ dao/reza members) |
| J03 cold trip setup | S4 early phase | mara |
| J04 private → group-safe | S4 (private constraints per member) | mara + companions |
| J05 proposal → mutation | S4 + urgent-decision scenario | mara |
| J06 coherence | S2 | elif Rome |
| J07 discover → action | S1 / discovery scenario | elif / dao |
| J08 live what-now | `mara phase=live` | mara |
| J09 notifications | urgent-decision scenario | mara |
| J10 booking/stay/expense | S2 stays + S4 costs | elif / mara |
| J11 atlas memory control | S1 | elif |
| J12 returned / settle | `elif phase=returned` (S5) + S4 settle | elif / mara |

Six identities, all twelve journeys.

## Concrete `scenarios.yaml` deltas

**Keep + annotate** (add `identity`, `journeys`, `rails`) — the ten `S*` backend scenarios.
Example:

```yaml
  S4-lisbon-group-planning:
    lane: backend_real
    identity: mara                # NEW (replaces free-floating `persona:`)
    account: mara@dogfood.local
    companions: [dao, reza, elif]
    packs: [lisbon-phase1, atlas-phase2]
    phase: planning               # NEW — lifecycle is a field, not a persona
    journeys: [J02, J03, J04, J05, J09]   # NEW
    rails: [logic_qa, maestro, mock_walk, five_pack]  # NEW — wedge runs every rail
    proves: Organizer relief, group synthesis, private constraints, and shared plan.
    forbidden_fallbacks:
      - Treating all members as identical.
      - Exposing private preference as public fact.
```

**Convert** the phase-danglers from standalone personas into phase/derived scenarios of the
six (lane stays `frontend_mock` where we're not seeding new substrate):

```yaml
  P-mara-live:                    # was M3-carmen-live-trip
    lane: frontend_mock
    identity: mara
    derived_from: S4-lisbon-group-planning
    force_state: { phase: live }
    journeys: [J08]
    rails: [maestro, mock_walk]
    proves: Product usefulness during the trip (Now Mode, live itinerary).

  P-elif-returned:                # was M4-dev-just-returned
    lane: frontend_mock
    identity: elif
    derived_from: S5-elif-tokyo-kept-memory
    force_state: { phase: returned }
    journeys: [J12]
    rails: [maestro, mock_walk]
    proves: The after-trip loop — receipt, reflection, candidate review.

  P-mara-urgent-decision:         # was M6-urgent (Riley)
    lane: frontend_mock
    identity: mara
    derived_from: S4-lisbon-group-planning
    force_state: { open_proposal: awaiting_votes }
    journeys: [J05, J09]
    rails: [maestro, mock_walk]
    proves: Needs-you state and decision hierarchy.
```

(Same shape for `ready`→`P-*-pre`, `between`→`P-elif-between`.)

**Delete** (coverage re-homed above): `M2-ben`, `M8-nadia`, `M9-omar`, `theo`,
and `M0-default` (or keep one smoke fixture). Reclassify `M10-torture` out of scenarios
into the UI-vector lane.

## FE cleanup (`travel-app/constants/personas/`)

| Bundle | Action |
|---|---|
| `elif.ts`, `mara.ts` | **Keep, regenerate as derived** from S1 / S4 seed responses (record → freeze). Stop hand-editing. |
| `dao.ts`, `reza.ts`, `mike.ts`, `sarah.ts` | **Create as derived** (currently missing — closes the "can't embody them on device" gap). |
| `carmen.ts`, `dev.ts`, `between.ts`, `ready.ts`, `urgent.ts` | **Delete**; replaced by `force_state` fixtures derived from a seeded identity. |
| `ben.ts` | **Delete**; planning phase of mara. |
| `nadia.ts`, `omar.ts`, `theo.ts` | **Delete**; absorbed into elif / dao-reza. |
| `ana.ts` | **Reduce** to a `cold-start` empty fixture (kind 3), not a person. |
| `torture.ts` | **Move** to `fixtures/ui-vectors/` (kind 3). |
| `index.ts` `default` (Alex) | Retire, or keep as the single M0 smoke fixture. |

**Derivation mechanism** (reuses machinery you already have — dogfood seed pipeline + LLM
VCR record/replay + replay engine): a script walks each real identity's key endpoints
against the seeded backend once and freezes the JSON into the FE bundle. Mock becomes a
*build artifact of the seed* — regenerate on demand, cannot drift, still offline +
deterministic for Maestro.

## Watch-outs (concentration risk we are accepting)

1. **elif is overloaded** — after absorbing nadia/omar/dev/between she carries archive +
   returned + between + discovery + five cities (S1/2/3/5/6). One bad seed breaks half the
   solo-side coverage at once. Keep her seed clean and deliberately treat her as the
   "do-everything solo" fixture.
2. **mara is the single point of failure for the wedge** — she is the *only* group
   organizer among the six, so the entire multiplayer demo rests on one seeded trip being
   coherent. Acceptable for cohort 1 (matches "narrow the wedge"), but her Lisbon seed must
   be the most-hardened substrate we have. A second organizer is a post-cohort-1 item.

## Cast sufficiency — is six enough?

Answer: **enough identities for the cohort-1 wedge; not enough taste-diversity to prove
the personalization moat.** The fix is *not* more people — see below.

**What's genuinely covered (verified in the seeds):** Mara's Lisbon group carries real
private constraints, not a hollow demo — Reza's `reza-shellfish` "absolute" (no
shellfish-forward menus), a mid budget band, accessibility/slope facets, vegetarian-path
caveats (`sources/lisbon-phase1/lisbon-anchors.md`). That is exactly the J04/J05 test
material: dietary + accessibility + budget constraints that must shape the plan without
leaking. For the wedge, six is sufficient.

**The real gap — the six are taste-monochrome.** Every identity is a refined,
food-and-design-forward, aesthetically-literate traveler (from their `proves` lines):
elif "counter-food DNA," mara "food history / architecture," reza "pizza tradition +
facade/material detail," mike "natural-wine / shared-table," sarah "morning-protocol /
walk-in-counter," dao "flat-city-walker." They differ in *flavor*, not in *register*. If
Vesper delights all six, that proves it has **one excellent mode** — not that it
*discriminates*. Personalization ("felt as fit") is only actually tested when identities
are far apart in taste-space **and** include the un-refined. The cast has zero of:

- a **budget-anxious / constraint-first** traveler (ironically the cut `carmen` had exactly
  this — "private fatigue, budget anxiety" — now `will-not-build`);
- a **low-signal / ordinary** user with sparse taste (can't be force-stated from a rich
  archive);
- a **non-food motivation** — nature/outdoors, nightlife, work trip, family-with-kids.
  Everything here is food + architecture.

**The distinction that resolves it:**

- **Structural variety** (2-person group vs mara's 3–4, a 6-person group, different group
  dynamics) → **scenarios/configs of the six**, never new identities. Note the *actual*
  first dogfood invite is 2-person while mara's group is 3–4, so a 2-person config
  (`mara + one member`) is genuinely needed — as a config, not a person.
- **Taste-register variety** → the one place headcount helps, because you cannot fake a
  register you do not have. But the answer is **1–2 deliberately-distant identities**, not
  a dozen. Three identities far apart test personalization better than ten that cluster.

**Recommended moves:**

1. **Cohort 1:** ship the six as-is. Do not expand — demand-driven, and "narrow the wedge"
   argues against breadth here.
2. **Cheap high-value move now:** do *not* resurrect carmen, but **port her constraint
   profile** (budget anxiety / fatigue) onto a *member of Mara's group*. Then J04 tests a
   **budget** leak vector, not just dietary + accessibility — closing the most-dangerous
   journey's most-common real-world constraint for free.
3. **Post-cohort-1 (moat-proving, not wedge-proving):** add exactly **two** identities far
   from the current cluster — one budget/ordinary, one non-food-motivated — *when* real
   dogfood shows Vesper over-fitting the connoisseur register, not speculatively.

**Trap to avoid:** adding more tasteful-food-traveler identities *feels* like coverage while
proving nothing new. Diversity of *register* beats diversity of *count*.

## Sequencing (serve the launch gate, don't delay it)

- **Cut 1 (critical path, ~½ day):** add the `identities:` block + `journeys:`/`rails:`
  fields for the **wedge cast** (mara + dao/reza + elif); wire `resolve_identity()` so the
  two-account on-device walk seeds from one known cast. This is the minimum that makes the
  device cert reproducible.
- **Cut 2 (fast-follow):** — *in progress 2026-07-08*
  - ✅ **`resolve_identity()`** — `tools/dogfood/content/identities.py` (registry resolver +
    FK check); 7 unit tests green (`tests/dogfood/test_identities.py`).
  - ✅ **Coverage ledger** — `tools/dogfood/content/coverage_ledger.py`; `make coverage-ledger`
    (report) / `STRICT=1` (gate). All 10 backend `S*` scenarios now carry `journeys`+`rails`.
  - ✅ **Make targets** — `identities`, `identities-check`, `coverage-ledger`.
  - 🔲 **Point Logic QA narrative-tier + Maestro at `resolve_identity()`** — deferred (touches
    live test infra).
  - 🔲 **Derive-from-seed snapshot script** — deferred (needs a running seeded backend to
    record responses; reuses VCR/replay machinery).
  - 🔲 **Regenerate elif/mara mocks + create dao/reza/mike/sarah mocks** — blocked on the
    script above.

  **Ledger finding (first run):** 7/12 MVP journeys certified (logic_qa + maestro) —
  J02–J06, J09, J10 (the wedge + coherence + booking). Gaps: **J01** (cold-start fixture,
  deferred), **J08/J12** (live/returned — Cut-3 `force_state` fixtures, not yet seeded),
  **J07/J11** (have maestro + eval coverage but their existing `test_j07`/`test_j11` backend
  scenarios aren't yet *linked* to a registry scenario — a pure annotation gap to close).
- **Cut 3 (post-cohort-1):** delete the re-homed FE bundles; convert phase-danglers to
  `force_state` fixtures; move torture to the UI-vector lane; decide a second organizer.

This is refactoring — it does not itself flip the cert gate. Its value is making the cert
**trustworthy** (same cast on every rail) and **reproducible** (one command seeds the walk).
Fix the cast *definition* (Cut 1) before repointing rails, or we cement the current mess.

## Open decisions for the founder

1. **Keep `M0-default` (Alex) as a smoke fixture, or delete entirely?**
2. **Do lifecycle phases (live / returned / between) need real seeded substrate for cohort
   1, or are `force_state` fixtures on the six enough?** (Cohort-1 walk is create→invite→
   plan→propose — live/returned may be out of it, in which case don't seed them.)
3. **Build the derive-from-seed script in Cut 2, or hand-wave FE mocks for the wedge in
   Cut 1 and defer derivation?**
4. **Second group organizer** — accept mara-as-SPOF for cohort 1 (recommended), or seed a
   backup organizer now?
5. **Port carmen's budget/fatigue constraint onto a Mara group member** (recommended — gives
   J04 a budget leak vector for free), or leave J04 to dietary + accessibility only for now?
6. **Taste-diversity expansion** — hold the two distant identities (budget/ordinary,
   non-food) until dogfood shows connoisseur over-fit (recommended), or seed them now?
