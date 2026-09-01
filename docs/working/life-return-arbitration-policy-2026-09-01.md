---
doc_type: working
status: active
owner: founder / product / architecture / design
created: 2026-08-31
last_verified: 2026-09-01
expires: 2026-09-30
why_new: Workstream C deliverable (behavior handoff §7.5, §12) — a small explicit admission policy for Return arbitration over the controlled fixtures, with deterministic test cases. Not a recommender; not an implementation.
depends_on:
  - docs/working/life-next-behavior-prototype-handoff-2026-08-31.md
  - docs/working/life-anchors-fresh-design-audit-and-correction-brief-2026-08-30.md
  - docs/working/life-social-lifecycle-fixture-matrix-2026-08-29.md
  - docs/working/life-together-consumer-arc-code-audit-2026-09-01.md
  - docs/working/life-human-refinding-code-audit-2026-09-01.md
---

# Return Arbitration Policy — Adopted v1 Fixture Oracle

> Status: accepted for the v1 fixture behavior by
> `docs/decisions/2026-09-01-adopt-life-v1-behavior-sequences.md`. Companion
> to design boards `19`/`19A–19D` and the accepted paired state on board `23`.
> This is the implementation oracle; it does not imply that the policy is built.

## 0. The law (restated from handoff §7.2, adopted verbatim)

Among eligible Returns that substantially share evidence, surface or
compose the **smallest set whose dominant jobs provide nonredundant value**
under current evidence, authority, freshness, and circumstance. Merge
compatible value; suppress weaker duplication; allow a later material
trigger to recompile the dominant job.

Engagement probability is not a material trigger. More available space is
not permission to fill it.

## 1. Vocabulary

- **Cluster** — the maximal set of candidate Returns whose evidence-
  dependency sets substantially overlap (≥ half of either candidate's
  material evidence shared, or a shared foundation object). Arbitration
  operates per cluster, per surface.
- **Candidate** — (foundation, evidence-dependency set, dominant job,
  material trigger, contribution beyond retrieval, authority footprint,
  freshness state). Dominant jobs use the return families: experiential /
  epistemic / possibility-transfer / relational — plus `recap` (always
  novelty-failing unless explicitly requested) and `silence`.
- **Material trigger** — new evidence; a changed world condition (forecast,
  service resumption, reopening); another person's authorized contribution;
  an unfinished inquiry becoming relevant; explicit request; current
  location. NOT: engagement probability, dwell, calendar coincidence,
  available space, elapsed time alone.
- **Seat** — the right to render active present-delivery at one density.
  STRENGTHENED 09-01 (correction handoff P0-5): a cluster holds **at most
  one active present-delivery seat across ALL surfaces at a time**. When
  Home or Places owns the present value, Life's active root projection
  yields; the durable dossier, lineage, and search access are never seats
  and remain available throughout.

## 2. The admission pipeline (deterministic order)

```text
1. GATES (all-or-nothing, per candidate)
   authority   — every evidence item currently authorized for this viewer
   truth       — no claim exceeds occurrence/plan/unresolved state
   novelty     — contribution beyond retrieval/paraphrase of what the
                 person supplied (recap fails here)
   trigger     — at least one material trigger, inspectable, nameable
                 as a fact ("Thursday's forecast reached 34°C")
   freshness   — trigger and world facts current at composition time
2. SUPPRESSION STACK (imported wholesale from social-lifecycle §7)
   person suppression ("don't bring this back")
     > safety boundary / block
     > source or audience revocation
     > shield / exclusion scopes
     > surface-ownership yield (see 3)
     > evidence bar (see 4)
     > editorial rank
   A lower layer never outvotes a higher one.
3. CLUSTERING — group survivors by shared evidence.
4. MERGE — within a cluster, if one composition can carry two dominant
   values without degrading either (compatible jobs, shared evidence),
   compose ONE candidate that absorbs both. Merge is a composition act.
5. SEAT SELECTION — among remaining cluster members, the strongest
   CURRENT job wins the surface's one seat:
   present-tense trigger > addressed human contribution > new-evidence
   understanding > re-entry. Losers are not queued; they demote (see 4)
   or stand down with lineage preserved.
6. RENDER — the seat renders at the surface's density with reason-as-
   material-fact inline; everything else is invisible. Silence wins when
   no candidate survives — the region is absent, not empty.
```

## 3. Surface ownership and yield

- Present-tense possibility belongs to Home (or Places when the subject is
  a place). While a destination surface is delivering a cluster's value,
  **Life's compact seat for that cluster stands down** (no echo); the
  dossier organ retains foundation + lineage throughout (design: 19C).
- The dominant-job flip (relational → possibility-transfer on a world
  trigger) reuses the same identity: **no new durable object is minted**
  by recompilation (handoff §7.6). Lineage names the prior composition.
- The return-derived item competes under the destination's own admission
  bar; arbitration grants no reserved lane anywhere.

## 4. The evidence bar and demotion ladder

A candidate that passes gates but is too weak for a root seat demotes
rather than dies:

```text
root RETURNS row  →  dossier organ (WHAT THIS OPENS)  →  search-only
```

Demotion is a density decision, never a deletion; promotion back requires
new evidence or a new trigger — never accumulated impressions.

## 5. Deterministic test fixtures (the ten §7.3 scenarios, executable)

World: the Rome–Paris–NY cluster (F1+F3), viewer Feihu. Time steps:
T0 = Mon Aug 31 (Maya's note is the only trigger, addressed Sun Aug 30);
T1 = Wed Sep 2 07:00 (34°C Thursday forecast lands); T2 = Thu Sep 3
(Home delivery window); T3 = after Thursday.

| # | Setup (state Δ) | Expected output | Hard-failure oracle |
|---|---|---|---|
| 1 | T0, all grants valid | Exactly one Life seat: relational juxtaposition (merged per #2); reason = "Maya addressed this to you · Sunday" | >1 row from the cluster; recap rendered |
| 2 | T0, epistemic + relational both pass gates | ONE composition carrying mechanism inside juxtaposition | two sibling rows sharing evidence |
| 3 | T0 minus Maya's note | RETURNS region absent (no trigger) | placeholder, apology, or teaser |
| 4 | T1 forecast arrives | Cluster recompiles: dominant job = possibility transfer; seat reason = the forecast fact; same identity, lineage names the T0 composition | new durable object minted; both old and new rows rendered |
| 5 | T1, query old return | Relational juxtaposition absent from root; whole in shared-with-Maya dossier; reachable by search | old row coexisting on the root |
| 6 | T2, Home delivering | Life compact seat stands down; dossier organ intact all day | root echo of Home's card |
| 7 | T1 + Maya withdraws note (S05) | Recompile BEFORE delivery from Feihu-only evidence; no paraphrase of her lane; if remainder passes gates, seat persists with narrowed substance | "a friend once suggested…" residue; stale composed text |
| 8 | Same, but Rome evidence = 1 day not 3 | Remainder fails root bar → demote to dossier organ; no root seat | root row on thin evidence; deletion of the distinction |
| 9 | Feihu: "don't bring the heat thing back" | All cluster surfacing stops (root, Home, push) across surfaces; record, grants, dossier organ, search retrieval intact; reversible | any resurface under rewritten copy; deletion of record |
| 10 | T0 with zero triggers anywhere | Silence; region absent; page complete | filler content; "nothing new" card |

Zero-count invariants (all fixtures): rendered rows citing dwell/views as
reason = 0; active present-delivery projections for one cluster across
Home + Places + Life at one time > 1 = 0; reasons that
are category labels instead of material facts = 0; recompiles triggered
by engagement = 0.

## 6. Code mapping (audit-informed, no implementation authorized)

- **Candidate identity / lineage**: extends the composition-manifest
  requirement (object-and-lens pack §15 P0-7); the refinding audit's
  result envelope carries the same why-matched/freshness fields — reuse
  one envelope shape for both.
- **Evidence-dependency sets**: the Together audit's grant record (ruled
  08-31 as the durable promotion of `ContributionAxes`) supplies the
  authority footprint per evidence item; scenario 7 is exactly an S05
  propagation consumer.
- **Triggers**: world-condition triggers are read-side facts (forecast,
  service state) — no new ingestion; addressed-contribution triggers come
  from the grant record's audience axis.
- **Where it runs**: a pure function over (cluster, viewer, surface,
  time) → seat | silence. Deterministic, replayable under the eval lane
  (`AI_MODE=replay`), testable with the table above as golden cases.
  Explicitly NOT a learned ranker; editorial rank exists only below every
  boundary layer in the suppression stack.

## 7. Implementation tuning questions (not acceptance blockers)

1. Seat arithmetic across *unrelated* clusters: the root region allows
   0–3 rows; this policy fills seats per cluster. Is 3 the global cap
   with first-come-by-trigger-recency, or should cross-cluster selection
   also prefer job diversity (max one possibility-transfer at a time)?
2. Does a person-suppressed cluster (scenario 9) suppress FUTURE
   compositions from *partially* overlapping evidence (e.g., a Rome
   food return sharing the traces), or only this cluster's identity?
   Proposal: cluster identity only; a shared-evidence future candidate
   renders but its lineage discloses the suppressed sibling.
3. May the person inspect the losing candidates ("what else could this
   have been?") — or does exposing the contest undermine 19A's "contest
   the person never sees"? Proposal: no browsing UI; the seat's Why-this
   door names merged/yielded siblings only.
