---
doc_type: working
status: active
owner: founder / product / design / research
created: 2026-09-01
last_verified: 2026-09-01
expires: 2026-10-01
why_new: Execution report for the Interaction Kernel Lab V2.1 integrity fix — how the failed V2.0 step graph was converted to a fixture-local state machine, exactly which integrity paths were verified with state assertions, what was suspended, and what remains blocked.
promotes_to: null
supersedes: []
source_of_truth_for:
  - interaction-kernel-lab-v2-1-execution-record
depends_on:
  - docs/working/claude-design-code-interaction-kernel-lab-v2-1-integrity-fix-handoff-2026-09-01.md
  - docs/working/claude-design-interaction-kernel-lab-v2-execution-report-2026-08-31.md
---

# Interaction Kernel Lab V2.1 — Execution Report

## 1. Project identity and scope

- **Project:** Vesper — Interaction Kernel Lab (continued in place; no new
  project). Project ID `6dd8b450-9686-4814-8db9-667f0e99db2c`.
- **Durable link:** <https://claude.ai/design/p/6dd8b450-9686-4814-8db9-667f0e99db2c>
- V1 pages (`A`, `B`, `D`, `90`, `92`) untouched. V2.0's record preserved:
  93's ledgers retained verbatim under a suspension banner; the V2.0
  execution report carries a §13 correction notice. The source
  "Vesper - Home & Places" project remains unmodified. No production Travel
  App / Travel Agent code was touched; no analytics, network logging, or
  real personal data exist anywhere in the lab.

## 2. What V2.1 changed (the shape of the fix)

V2.0 was a deterministic **step graph**: pre-rendered screens joined by
reachable routes. The audit showed that this architecture *cannot* be
semantically faithful — screens rendered fixture prose regardless of what
the person actually chose or typed. V2.1 replaces it with a **fixture-local
state machine**:

- `fixtures.js` — per-fixture `initialState` (A2: pace/venue/promotion/jazz;
  B2: occasion/place/invitation/attendance×3/constraint/contribution/decision;
  D2: flight/hotel/interview/transfer/lifecycle) plus fixture prices
  (Georgian ≈$38, noodle ≈$24) and diegetic participant titles.
- `lab-state.js` (V2.1 runtime) — a state snapshot stack parallel to the step
  stack (`__back`/Undo restores the **exact predecessor**); `data-set`
  (with `@key` copy and `++` increment) and `data-set-from` (input value →
  state — typed text becomes owner truth); a fail-closed `data-intents`
  language router (declared regex/`matchState`/`capture`/first-sentence
  `split` entries; **no match ⇒ state unchanged, no navigation,
  `result:unresolved`, diegetic "nothing changed" note**); state-derived
  rendering (`data-bind` + value maps, `data-show-if`/`-not`/`-gte`/`-lt`,
  `data-value-from` prefill); djb2 state digests on every event; `phase`,
  `viewer`, `semantic_intent`, `result`, `state_digest_before/after` in the
  trace; per-phase action counts in the research rail; `&state=` overrides
  for deterministic state-conditional capture (validated keys; refused in
  participant mode); session key bumped `lab2:`→`lab3:` so stale V2.0
  sessions cannot corrupt V2.1 state; two new self-check assertions
  ("unresolved input never changed state", "state matches its stack
  snapshot" — 8 total).
- `A2` / `B2` / `D2` — fully rewritten as state-conditional pages (A2
  collapses to ONE shape step per treatment; B2 becomes four per-actor
  segments over one state; D2 gets a byte-equivalent common prelude with
  divergence only at re-entry, plus restored expiry endings t10/i10).
- Docs re-based: `94` (new — audit ledger + state matrices + suspensions),
  `00`, `01`, `03`, `04`, `91` (D-33–D-42 appended), `93` (suspension
  overlay), `README`.

## 3. P0 dispositions (all verified in-browser with state assertions)

| ID | Fix | Verified by |
|----|-----|-------------|
| P0.1 | One state-derived shape; comparison adds venue facts only | loose→compare→choose→keep leaves `pace:open`, renders no dinner rows; breathing/fit-more persist through compare+keep |
| P0.2 | Durable `venue` state | choose Corner Note → keep → refresh → refind all render Corner Note |
| P0.3 | Real Undo-keep | pre-keep state JSON == post-undo state JSON (exact snapshot) |
| P0.4 | Empty hybrid input blocked | participant click on empty composer: no nav, no event |
| P0.5 | Input-to-state binding | typed "Cafe X"/"Order the soup." renders verbatim through attribution, decision, settled, Dana's view; Edit opens prefilled with current value; revision increments `contribution_rev` |
| P0.6 | Dinner OUT ruling | "at Nora's" absent everywhere; "Place to be decided" in invitation; place open until host decision |
| P0.7 | TO INVITE pre-send | invitation state binds TO INVITE/LINK READY → SENT exactly at the send boundary |
| P0.8 | Actor isolation | segments end in-actor with durable receipts (Dana's bound amount + withdraw/change); switching = research-only chrome, stripped in participant mode |
| P0.9 | Amount is state | $40 chip and typed "Other" (30) both persist, render back, and gate the eligibility copy against fixture prices (≥38 both-fit / <38 noodle-only) |
| P0.10 | Language edit path | c7e composer prefilled with current advice; any ≥2-char text becomes the revision; short input fails closed |
| P0.11 | Equal preludes | normalized markup byte-equal p0–p3; p4 differs only by the t5/i5 divergence pointer; state digests equal at all five prelude steps |
| P0.12 | 04 reclassified | header reads "CONTRACT COMPATIBILITY DOCUMENTED · GENERATED-COMPOSITION INTERACTION NOT EXERCISED HERE"; five evidence classes on every claim |

P1.1–P1.5 all closed: unscored orientation preludes with identical measured
checkpoints; fail-closed recognizers; diegetic titles/announcements (regex
token scans clean on visible text and `aria-live` in participant mode);
multi-field word totals; this report + the V2.0 correction notice.

## 4. Verification detail (what was actually run)

All in the live served pages, research mode unless stated; every assertion
on **state content**, not step reachability.

- **A2 (7 §11 paths):** all three treatments; fail-closed gibberish at the
  shape and comparison composers (state digest unchanged, unresolved traced,
  diegetic note shown); "keep the second one" keeps Corner Note; undo-of-keep
  returns to the exact pre-keep comparison state; removal shows the
  no-residue receipt; hybrid selection carries the referent; participant walk
  clean of research tokens.
- **B2 (10 §11 paths):** direct path with typed "Cafe X"/"Order the soup." →
  edit "Get the noodles" → $40/$30 constraint set/withdraw/change → decision
  by `@contribution_place` deref → settled + Dana's-view bindings → advice-only
  vs full withdrawal with distinct receipts and provenance. Language: split
  parse of a custom sentence, amount capture ($35), `matchState` decision on
  "Cafe X", full withdrawal by words, fail-closed no-number and gibberish.
  Hybrid: same arc with direct Edit/Undo (undo restores empty contribution
  exactly). Participant: Dana segment at 320pt+135% — no research tokens, no
  overflow, all targets ≥44pt, real `--tscale` scaling; seeds cleared.
- **D2 (10 §11 paths):** prelude byte-equivalence + digest equality (above);
  research walk of ask-road and scroll-road refinding (thread overflows
  ~910px, opens at bottom; scroll metric counts once events flush — hidden-tab
  deferral is a test artifact only, documented since V2.0); all three endings
  in both treatments with correct lifecycle state; expiry (t10/i10): controls
  gone, receipts remain, corrected interview bound; participant delay gate:
  locked with countdown, early click blocked, unlocks at the deadline,
  overnight facts applied to state on pickup; participant token scan clean.
- **Cross-cutting:** 8/8 self-check PASS after every scenario; zero console
  errors on every exercised page; refresh restores the exact kept state;
  Enter submits composers; `prefers-reduced-motion` and focus styles present;
  `state=` override refused for unknown keys and unavailable to participants.

## 5. Runtime regressions caught during this pass

Three defects in my own V2.1 work were found by the state-assertion suites
and fixed before completion: (1) the D2 `data-scroll="bottom"` attribute was
on the step node instead of `.ph-scroll`, so the transcript opened at the top
(refinding burden would have been fake again) — caught by the "opens at
bottom" assertion; (2) the delay gate's wrapper attribute placement; (3) the
first D2 rewrite dropped the expiry endings — restored as t10/i10 and
exercised. A malformed (duplicate-key) intent attribute on B2's language
edit composer was also cleaned and re-verified.

## 6. Findings status

- **Suspended (D-42):** V2.0's comparison ledger, the "hybrid narrows to two
  questions" claim, and 04's "holds as drawn" verdict — retained as
  historical record on 93/04, suspended on 94. V2.0 trace totals join V1's
  as retired.
- **Restored/kept:** nothing was "restored" as a finding — V2.1 makes no new
  comparative claims. The falsifiers V2-1…V2-10 remain OPEN; V2-3 and V2-4
  remain live hypotheses (the corrected direct and language treatments are
  stronger contenders than before, which is the point).
- **Participant authorization:** A2/B2 **direct + hybrid** and **D2 both
  treatments** meet the V2.1 acceptance bars for moderated sessions.
  **A2/B2 language are BLOCKED** for open-language participant claims
  (D-41): fail-closed keyword recognizers make the surface honest but cannot
  evidence natural-language quality; they may run only as scripted-phrase
  walkthroughs with unresolved events reported.

## 7. Remaining blocks and not-run items

1. **Founder walkthrough — not run** (it is yours to do, in participant
   mode; per-actor B2 entry points are listed on 01).
2. **Participant sessions — not run.** Nothing is validated.
3. **AT screen-reader pass — not run** (announcement content verified
   programmatically; a real AT session is still owed before any
   accessibility claim beyond the measured mechanics).
4. **Language treatments** — blocked as above; the honest ceiling stands
   (D-31) and remains the main argument for the coded/native harness.
5. Eligibility copy at the B2 decision references only fixture-priced rooms;
   a contributed place with no fixture price is not priced or pretended to
   be (annotated on d9/c8/h8).

## 8. One bounded recommendation

Unchanged in direction, sharpened by the audit: build the native harness
around **D2's two treatments first** — it is the comparison the browser can
least fake and the only one whose decisive variable (where truth rests
across real hours, notifications, and re-entry) survived V2.1 fully
exercised. Adopt the V2.1 state-machine contract (state snapshots + exact
undo + fail-closed language + phase-scoped, digest-carrying traces) as the
native harness's trace/data spec verbatim; it is the transferable artifact
of this correction.

## 9. Compliance

Repair executed in place; V1 + V2.0 record preserved and labeled; no new
project; no production code, schema, or canonical doc changed; no analytics,
network logging, or real personal data; no serve URLs in any user-facing
text or this report; participant surfaces and accessible announcements carry
no research identifiers (regex-scanned); no universal artifact/workflow
schema or component trees; a keyword recognizer is nowhere presented as
evidence about production AI.
