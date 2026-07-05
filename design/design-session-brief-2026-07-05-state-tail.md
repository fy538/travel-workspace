# Vesper Design Canon — Session 4 Brief: State Tail + Merges (2026-07-05)

Scope: the final items between the canon and ~95% coverage. Eight items: one handoff beat, three state boards, two dedup/merges, two small sheets. All decisions are already recorded in governance — this session is pure execution; nothing here needs adjudication.

Standing rules:
- Frame width **393×852** for phone artboards (recorded hygiene rule).
- Snap to `design-system.jsx` tokens — no local palette forks.
- Compose ALL state treatments from **Vesper State System.html** components (StateScreen, EmptyHero, InlineAbsence, StaleNotice, OfflineNotice, LoadingSkeleton, ErrorRecovery, ActionFailureInline) — do not invent local state treatments.
- Flip the matching 02d/06b governance rows in `Vesper Canon Consolidation & Ownership.html` as each item lands; keep honest OPEN on anything skipped.

---

## 1. Creation → folio handoff beat (Trip Creation page)

The one remaining gap in the conversation-first creation flow: the transition from draft conversation to the opened Trip Document. Today it exists only as a voice line ("I'll open a trip home"). Draw a two-frame before/after board: the conversational thread at the promotion moment ("Make it a trip") → the Trip Document cover it resolves into. Flip the remaining OPEN note on the trip-creation governance row.

## 2. Shared ReaderStates board (companion to Discover Detail & Reader + Guide Reader)

One board, drawn inside ReaderChrome, consumed by dossier + angle + guide readers. States: loading (LoadingSkeleton in reader chrome) · sparse/partial content (InlineAbsence for missing sections) · error (ErrorRecovery) · offline (OfflineNotice with cached-read affordance) · not-found (StateScreen). Add a reference pointer from both reader pages to this board so neither invents its own.

## 3. Discover feed states (Discover page)

Nothing exists today. Draw inside the Discover cover layout: cold-start/first-run feed (no taste signal yet — this is also the post-onboarding landing, so it should feel like an invitation, not an apology) · empty-city (thin content region) · loading · error/offline. State System components throughout.

## 4. Changes screen states + banner re-spec (Changes System page)

Draw: empty (no changes yet — first visit) · loading · solo-trip variant (no group, no votes — what the timeline reads like alone). Then re-spec the page banner to match what is drawn: the timeline is sectioned TODAY/EARLIER (time-based); remove the claimed "source/phase sectioning" language. Source attribution stays at row level via the existing source chips (Vesper / member / group / Atlas). Flip the governance row.

## 5. Story share merge (Trip Story + External Sharing pages)

Execute the recorded adjudication: Trip Story owns the owner-facing share screen. Merge the two competing designs into ONE canonical screen with the union control set: **pause · revoke · new-link/rotate · preview-as-recipient · stats**. Update External Sharing's two story artboards to reference the merged screen (External Sharing keeps recipient entry + link-state taxonomy). Flip 02d to APPLIED.

## 6. Photo finder dedup (Trip Story + Photo & Media Intake pages)

Execute the recorded adjudication: Photo & Media Intake is canonical. Reduce Trip Story artboards J–M to thumbnails + an ownership pointer; align remaining copy to Photo Intake's. Flip 02d to APPLIED.

## 7. SectionEditSheet (Trip Story page)

Story section editing — real v1 surface; only the post-edit state exists today (Reader state H "Restore Vesper's version"). Consume Interaction Surfaces full-screen edit sheet chrome. One board, four states: editing (text region + Vesper's-version reference) · dirty-dismiss warning (IS pattern) · saving · save-failed (ActionFailureInline). Flip the 06b kill-or-draw row to DRAWN.

## 8. RevertConflictSheet (Proposal & Decision Detail page)

The decision moment before the existing "reverted — later edits kept" receipt. Consume the ReskinnedSheet chrome from Changes (grab handle, gold kicker, WAS/NOW strikethrough diff). One board, three states: clean revert confirm · conflict (list of later edits depending on the reverted change, keep/discard per item) · partial-keep result summary. Flip the 06b row to DRAWN.

## Definition of done

All eight items landed (or honestly OPEN with a reason) · banner language matches drawn reality on Changes · both merges leave exactly one canonical owner each · export a fresh handoff for final coverage verification (target ≥95%).
