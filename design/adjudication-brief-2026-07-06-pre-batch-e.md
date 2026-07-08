# Pre-Batch Adjudications (2026-07-06)

Seven open calls surfaced by the full alignment audit. Each has a recommendation — override any of them, but every one needs a recorded answer before Batch E/F execute, so implementers aren't guessing.

---

## 1. Motion token values — canon vs. code module disagree on 3 numbers

Canon (Session W Motion Stance): fast/press ≈150ms family, sheets 320ms (peek 260), toast 200/150, skeleton pulse ~1.1s.
Code (`constants/motion.ts`, written before the canon Motion Stance existed): fast=160, slow=240, shimmer=1200.

**Recommendation: canon wins.** The module predates the stance; retune the three values to match (160→150, drop/redefine `slow` to align with the 260/320 sheet pair, shimmer irrelevant once #2 below is decided). This is a values-only edit to one file.

## 2. Skeleton shimmer sweep — keep or kill

Canon Motion Stance explicitly bans shimmer: "reads glossy, not paper" — prescribes an opacity pulse (~1.1s cycle) instead. Code's `components/ui/Skeleton.tsx` implements a deliberate `LinearGradient` shimmer sweep at 1200ms.

**Recommendation: kill the shimmer, ship the opacity pulse.** This is exactly the kind of thing the "calm paper" rule zero exists to prevent — shimmer is a decorative flourish that off-brand's every loading moment in the app. Low effort (delete the gradient, animate opacity), touches every skeleton consumer visually but not structurally.

## 3. Fixture-world strategy — how far to chase canon/demo parity

No FE mock trip matches the canon world (Lisbon Oct 12–17, You=Maya R. Lin+Ana+Theo, Casa do Mar). Full parity is L-sized (~10 fixture files, prose coupling, ~30 tests, 71 Maestro YAMLs, ~150 screenshot goldens).

**Recommendation: demo-slice, not full migration.** Fix the "Casa da Mar" typo (S, it's frozen into a test and is just wrong regardless of world-alignment). Add `theo` and `mara` as real dev personas alongside existing ones (M) so canon-shaped demo screens are *reproducible*, without renaming the entire default mock world or touching the 71 Maestro/150 golden files. Full alignment is not worth the churn — the canon world is illustrative, the fixtures are functional; they don't need to be the same story, just compatible enough to demo from.

## 4. "Add to plan" vs. "Add to trip" — is Places exempt from the verb ruling?

The canon Language Session ruled "Add to trip" as the single add-verb everywhere. Places' consolidation doc claims an exemption ("pre-existing handoff, not a Places concern"). Four call sites still say "Add to plan"; one says "Save to the plan."

**Recommendation: no exemption — fix all five to "Add to trip."** A ruling with silent per-surface exceptions isn't a ruling. If Places has a genuine reason "plan" is more correct there, that argument belongs in front of the canon (a new adjudication), not baked into a consolidation doc that contradicts a recorded decision. Cheap fix regardless (string swaps), so there's no cost to just complying.

## 5. Trip Creation: chat-card states vs. dedicated screens

Canon draws Draft/Promotion/NotReady/Error as full-screen takeovers. Code renders them as inline chat attachments (`PlanReadyCard`, prose + banners) — behaviorally correct, visually simplified.

**Recommendation: accept the simplification as the code's actual design, don't build the screens.** The conversation-first ruling already established that chat-native moments beat screen takeovers for this flow; cards-in-thread are consistent with that spirit even though the canon artboards predate the full embrace of "conversational, not modal." Record this as a canon amendment (demote those 4 canon screens to reference/historical) rather than a code gap — building modal takeovers here would fight the flow the product already committed to.

## 6. Third-person "Vesper" meta-copy — status chrome vs. voice lines

The first-person voice rule ("I'll…, never Vesper will…") was written for *voice lines* (Vesper speaking as itself). ~24 hits are status/meta chrome ("Vesper is thinking…", "what Vesper can see") rather than Vesper's authored voice — arguably narrator register, not violations. 4 hits are clear voice-line violations (promissory copy: "Vesper will compose…", "Vesper will record edits here.").

**Recommendation: the rule applies only to attributed voice lines; status/meta chrome may stay third-person** (a progress indicator saying "Vesper is thinking" is system narration, not Vesper talking). Fix only the 4 clear violations in Batch E. Record this distinction in the Ops page's Verb Canon board so it stops being re-litigated.

## 7. Offline floor — build before dogfood or defer

Canon stance: trip map pack + cached reads must WORK offline. Code has zero Mapbox offline pack integration anywhere — this is an unbuilt subsystem (L), not a migration.

**Recommendation: defer past device-cert/dogfood.** Dogfood trips are short, deliberate, and near-guaranteed to have connectivity for the pilot cohort; building offline map tile caching is multi-day infrastructure work disproportionate to that risk. Ship with `OfflineNotice` as the honest fallback everywhere (already the pattern), revisit if dogfood surfaces real connectivity pain.

---

## Recording

Once you've confirmed or overridden these seven, I'll fold the rulings into Batch E/F briefs and, where relevant, into the canon governance page (items 2, 5, 6 change what the canon itself says — worth a two-line note in Claude Design so future sessions don't re-derive them).

---

## DECIDED (2026-07-06) — all seven confirmed as recommended, no overrides

1. **Motion values: canon wins.** Confirmed.
2. **Kill shimmer, ship opacity pulse.** Confirmed. Canon amendment — see governance note below.
3. **Fixture demo-slice, not full migration.** Confirmed.
4. **No Places exemption — all five sites to "Add to trip."** Confirmed.
5. **Accept chat-cards as the real design; demote the 4 takeover screens to reference/historical.** Confirmed. Canon amendment — see governance note below.
6. **Third-person OK for status/meta chrome; rule binds attributed voice lines only.** Confirmed. Canon amendment — see governance note below.
7. **Defer the offline floor past device-cert/dogfood.** Confirmed.

Batch E (`code-alignment-brief-E-rulings-strings.md`) already assumed these outcomes when written — no changes needed there. Batch F is unaffected by any of the seven (none of F1/F2/F3's scope touches Trip Creation, motion, fixtures, or the voice rule). Both batches are unblocked.

### Canon governance page note (paste into Claude Design, Ops page / Verb Canon board or equivalent)

> **Motion Stance:** shimmer sweep is not canon — skeletons use an opacity pulse (~1.1s), never a gradient sweep ("reads glossy, not paper"). `constants/motion.ts` values retuned to match (2026-07-06).
> **Trip Creation:** Draft/Promotion/NotReady/Error render as inline chat-card attachments, not full-screen takeovers. The four takeover artboards are reference/historical — conversation-first superseded them (2026-07-06 amendment).
> **Voice rule scope:** the first-person rule ("I'll…") binds attributed Vesper voice lines only. Status/meta chrome ("Vesper is thinking…") is narrator register and may stay third-person (2026-07-06 amendment).
