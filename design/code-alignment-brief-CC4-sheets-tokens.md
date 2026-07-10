# Code Alignment — Batch CC4: Sheets & Tokens Mop-Up + Durability (2026-07-09)

Repo: `~/travel-workspace/travel-app`. Canon mirror: `~/travel-workspace/design/vesper-canon-anchor/project/` (handoff 125, read-only). Ledger: `design/component-consistency-audit-2026-07-09.md`, families **sheets** + **tokens-type**. Sheets are ~87% adopted and the token primitives match canon 1:1 — this batch closes the last call sites, fixes the semantic-token tier, and **installs the ratchets that stop this drift from coming back** (the durability work is the point of this batch).

## Blocked-until
- **Task CC4.2 (stay/costs sheet fields) depends on D3** (which field species is canonical). Do the rest first; do CC4.2 after the D3 handoff.

## Standing rules
Same as CC1. If the fontSize/border-radius ratchets weren't already re-greened in CC1's CC0 step, do that FIRST here.

## Task CC4.1 — Sheet primitive stragglers  ·  severity MEDIUM
Canon: `Vesper Interaction Surfaces.html` + `sheet-header.jsx`. ~10 of ~76 sheet/dialog call sites still bypass the shared primitives. Fix:
- **Corner radius:** `trip-accommodations/index.tsx:550,647` use `radius.input` (20) semantics for a sheet — wrong token, right value. Point at the sheet radius token.
- **SheetHeader non-adoption:** Costs and People sheets hand-roll handle+header. Costs uses a hairline-wrong handle token; migrate to `ui/SheetHeader`. (ExpenseDetail's handle token already matches — just de-duplicate it.)
- **SheetHeader kicker register:** the shared header renders the kicker in sans caps; canon says mono. Fix in `ui/SheetHeader` (one place, all adopters benefit).
- **GroupAgencySheet** hand-rolls a discard-confirm dialog — route to `ui/ConfirmDialog`.

## Task CC4.2 — Stay/costs add-edit fields  ·  severity MEDIUM  ·  BLOCKED on D3
Once D3 rules the canonical field species: migrate the `trip-accommodations` add/edit sheet fields onto it (bordered `SheetField` if D3 picks bordered `Field`; leave read-rows as the borderless species). No action until D3.

## Task CC4.3 — Status-hue token values  ·  severity HIGH
Canon: `vesper-tokens.jsx:42-44` — the status hue trio (success/warn/danger). Code has the canon NAMES but the wrong VALUES. Snap the values to canon. This infects every status pill/chip/banner, so it compounds with CC1.2 — do it before or with that.

## Task CC4.4 — Semantic token tier  ·  severity MEDIUM
Canon: product surfaces should read from a semantic tier, not raw primitives. Code:
- `vesperSemanticTokens` is mis-mapped and effectively dead — reconcile it to canon's semantic layer (accent tokens already match by value; fix names/wiring).
- `ink80`/`muteSoft` carry real body text on **~215 sites** (backlog item, drifted from ~200 — getting worse). Migrate text roles onto the proper text token.
- The legacy neutral palette (`#2C2C28` ink, pure-white chrome) is still primary for some type roles — move to paper/ink tokens. (Correct evidence: `NarrationCard` uses `background.primary` at :395,510,563,574 — the `screen.chrome` sites are in trip-story/share, SegmentedIndicator, memory sheets.)

## Task CC4.5 — DURABILITY: manifest family rows + adoption ratchets  ·  severity HIGH (do not skip)
This is why the batch exists — make the next audit start from a ledger, not from zero.
1. ✅ **DONE 2026-07-09** — the 6 family rows (`Row System`, `Cards kit`, `Sheets`, `State System`, `Tokens`, `Voice registers`) are already in `design/surface-manifest.yaml` under the "Shared-element FAMILIES" section, `aligned_at: 125`, YAML validated + drift-check green. When you finish CC1–CC4, bump each family's `aligned_at` to the then-current handoff and clear the resolved open-items from its `notes`.
2. **Add adoption ratchets** (mirror `check-typography-budget.mjs`): "files defining local `btn`/`button` styles may only decrease" (baseline = CC1.1's after-count), "sheet call sites bypassing BottomSheet/SheetHeader may only decrease," "`ink80`-as-text sites may only decrease" (baseline = post-CC4.4 count). Wire into `ci.yml` next to the existing six ratchets.
3. **`ink80` lint:** add the backlog's proposed ratchet so the 215→ count can't climb again.

## Done
Sheet stragglers on shared primitives · status-hue values snapped · semantic tier live, ink80-as-text reduced + capped · (post-handoff) stay/costs fields aligned · **6 new manifest family rows + 3 new adoption ratchets green in CI** · report gives before/after counts for each ratchet baseline.
