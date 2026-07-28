---
doc_type: working
status: active
owner: founder / design
created: 2026-07-28
expires: 2026-08-27
why_new: Records the Canon Index / Ownership edits that registered the Trips-home stack model as a CANDIDATE, why the interchange manifest was deliberately left alone, and the working method for editing large Claude Design files.
source_of_truth_for:
  - trips-home-stack-model-canon-registration
---

# Registering the stack model in canon

The design is done and verified in **Claude Design → Vesper →
`Vesper Trips Home - Stack Model (Sans).html`** (seven page states,
existence gating, Dynamic Type, CONNECT section, cold rebuilt against the
shipped `ColdHome`). This records its *registration* — making it findable
by anyone following the project README — which was applied 2026-07-28.

The design itself is specified in
`docs/working/trips-home-promotion-model-2026-07-27.md`, which is
self-contained; this doc covers only governance and method.

## Status — §1 and §2 APPLIED 2026-07-28, §3 deferred by decision

| | file | result |
|---|---|---|
| §1 | `Vesper Design Canon Index.html` | **APPLIED** · 80,282 bytes · etag `1785215395726969` |
| §2 | `vesper-canon-consolidation-app.jsx` | **APPLIED** · 267,221 bytes · etag `1785215850493826` |
| §3 | `vesper-design-manifest.json` | **deferred until promotion** — see below |

### Correction: the "728 unaccounted bytes" was my arithmetic, not drift

An earlier revision of this doc claimed the HTTP-served copy was not
byte-identical to the stored file, with 728 bytes unexplained. **That was
wrong** — I compared Python *character* counts against *byte* counts on a
UTF-8 file dense with `·`, `—` and `'`. Each multi-byte character
accounted for the gap.

Proof: reverting my edit out of the reconstruction reproduced the stored
file at **exactly 78,902 bytes, delta zero**. The only real defect was a
two-space indent on `<meta charset>` that the serve layer's injected
`<style>` had absorbed. The mirror-then-edit workflow is sound; the
alarm was not.

### The mechanism that made this cheap — `DesignSync`

`mcp__claude-design__write_files` is whole-file **and inline-only**
(`local_path` returns *"not yet implemented for server-side callers"*),
so editing a 265 KB module through it means re-emitting the whole thing
through the model context — slow, and the single most likely way a
byte-exact requirement gets silently violated.

**`DesignSync.write_files` takes a `localPath`** and uploads straight
from disk. Contents never enter context. The working loop is:

1. `render_preview` → take the `serve_url` token (never put it in
   user-facing text — it is a `claudeusercontent.com` URL).
2. `curl` the file to scratchpad. `.jsx` serves raw and is byte-faithful;
   `.html` gets an injected `<script>`/`<style>` and a reflowed `<head>`,
   so an HTML mirror must be stripped and re-verified against the stored
   byte count before it is trusted.
3. Edit locally, validate (quote balance, bracket balance).
4. `DesignSync.finalize_plan` (**requires `deletes`**, pass `[]`) →
   `write_files` with `localPath`.
5. Verify with `read_file` at the changed line range, then render the
   page and check the console — for a `.jsx` module, a syntax error is
   silent until Babel fails at runtime.

**Caveat:** `DesignSync` has no `if_match`. Concurrency has to be guarded
by reading the etag immediately before writing, which leaves a sub-second
race window. Acceptable single-user; not acceptable if a second session
is editing the same file.

---

## 1 · Canon Index — `Vesper Design Canon Index.html` — ✅ APPLIED

Live at lines 158–169; verified by `read_file` after the write. Below is
what was applied, kept for the record.

**a. Add one CSS rule**, beside the two existing tag styles:

```css
    .t-c { background: #E9F0E6; color: #4D5E45; }
    .t-p { background: #E3EBF6; color: #2A4878; }
    .t-n { background: #F5EDDD; color: #8A6628; }   /* ← add: CANDIDATE */
```

**b. Replace the existing Trips Home row** (in the surfaces table) with
these two rows:

```html
<tr>
  <td class="nm">Trips Home</td>
  <td class="fi"><a href="Vesper Trips Home.html">Vesper Trips Home.html</a></td>
  <td class="ow">Attention router · hero cascade · eight postures · group variant · trail sections. <strong>Succession in progress 2026-07-28:</strong> the stack model (next row) is the proposed successor and is where new Trips-home work is happening — build the eight-posture cascade from here only until that page closes its remaining items.</td>
  <td class="tg"><span class="tag t-c">CANON</span></td>
</tr>
<tr>
  <td class="nm">Trips Home · Stack Model</td>
  <td class="fi"><a href="Vesper Trips Home - Stack Model (Sans).html">Vesper Trips Home - Stack Model (Sans).html</a></td>
  <td class="ow">Proposed successor to Trips Home. One cross-trip ranked queue (item #1 blooms into the voiced card, the rest dock as rows) · six fixed sections: stack · companion · table (sketch + seeds) · your people · connect · trail · seven page states (busy · quiet · live · urgent · cold ×2 · loading) · existence gating · Dynamic Type 100/120/135% · type + geometry contract (gutter 22 / cards 349 / rows minHeight 60 / 3 mono · 6 sans · 5 serif). Support: trips-home-stack-sans.jsx (primitives) · -states.jsx · -connect.jsx · -screens.jsx (composition, must load last). <strong>NOT yet canon</strong> — open: chrome states not re-verified, 320px @120% untested, some item kinds unmocked, “All trips” destination still owned by the current canon page.</td>
  <td class="tg"><span class="tag t-n">CANDIDATE</span></td>
</tr>
```

Markup validated: `<tr>` 56/56, `<td>` 208/208, `<span>` 114/114 balanced;
the new row parses as 4 cells with tag `t-n / CANDIDATE`.

**Why CANDIDATE and not CANON.** The README promises that a top-level page
is "governed and trustworthy for its declared role", and that an absent
page is a design gap to escalate. Flipping the tag today would tell agents
the chrome states and the "All trips" destination are covered when they
are not. When the open items close, promotion is a two-word edit: swap the
tags and move the succession note into §03 Folded / Removed, following the
existing `Vesper Trips.html → superseded by Trips Home` precedent.

## 2 · Ownership — `Vesper Canon Consolidation & Ownership.html` — ✅ APPLIED

Content renders from **`vesper-canon-consolidation-app.jsx`**, not from
markup, so this was an edit to that module rather than the page. Applied
2026-07-28 into the **Trips Home cluster** of `SupportCleanup()` at lines
618–621, plus a succession clause on that cluster's `canon:` string.

Verified: page compiles under Babel with **zero console errors**, all four
rows render, and the succession note renders. Status column reads
`ACTIVE — CANDIDATE SUPPORT` ×3 and `ACTIVE — MUST LOAD LAST` ×1.

The four support files as registered:

| file | role |
|---|---|
| `trips-home-stack-sans.jsx` | primitives — type scale, geometry, row anatomy, blooms |
| `trips-home-stack-sans-states.jsx` | live · urgent · cold ×2 · loading · absence · Dynamic Type boards |
| `trips-home-stack-sans-connect.jsx` | CONNECT card + the A/B decision record |
| `trips-home-stack-sans-screens.jsx` | **composition — owns section order; must load last** |

The load-order constraint is load-bearing: `-screens.jsx` intentionally
overrides `SansHomeBusy` / `SansHomeQuiet` from the primitives module so
that adding a section never means editing the file that owns the type
scale. If it is reordered, the CONNECT section silently disappears.

## 3 · Interchange manifest — `vesper-design-manifest.json`

Generated by `audit-interchange.js --write-manifest`; stale at
`canonVersion 2026-07-24`. Do **not** hand-edit — re-run the generator.
The seven screens already carry the attributes it reads:

```
trips-home-stack-busy-sans        trips.home.stack.busy
trips-home-stack-quiet-sans       trips.home.stack.quiet
trips-home-stack-live-sans        trips.home.stack.live
trips-home-stack-urgent-sans      trips.home.stack.urgent
trips-home-stack-cold-sans        trips.home.stack.cold
trips-home-stack-cold-saves-sans  trips.home.stack.cold.saves
trips-home-stack-loading-sans     trips.home.stack.loading
```

All carry `data-page-id="trips-home-stack-sans"`.

**Decision 2026-07-28 — leave unregistered until promotion.** The
manifest's `authorityStatus` vocabulary has no CANDIDATE value. The two
options were to add one, or to hold. Holding, because every value in that
vocabulary asserts *authority*, and the whole point of tagging this page
CANDIDATE in §1 was to avoid telling downstream agents it is settled when
its chrome states and "All trips" destination are not. Inventing a
vocabulary value for a page that may still change would spend a schema
change on a temporary state.

Re-running the generator is therefore part of the **promotion** checklist,
not this pass. Note also that `audit-interchange.js` lives design-side, not
in this repo — it has to be run in the browser against the project, so it
is not a one-line CLI step.

## Remaining before promotion to canon

0. **Re-run `audit-interchange.js --write-manifest`** and add an
   `authorityStatus` value at that point (§3 above) — deferred from this
   pass by decision, not by oversight.

1. Chrome states re-verified against `TripsRootChrome` (scrolled, reduced
   transparency, reduced motion).
2. 320 px at 120 % text — the seed grid's two `1fr` columns are the risk.
3. Item kinds still unmocked: overlap match, group echo, agent-work
   receipt, story-ready.
4. "All trips" destination — three artboards already exist on the shipped
   canon page and are unaffected by the stack model; carry them over
   rather than redrawing.
5. Post-trip story arc — `returned` currently surfaces only money.
