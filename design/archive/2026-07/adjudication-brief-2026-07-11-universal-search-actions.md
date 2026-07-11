# Claude Design Adjudication Brief — Universal Search Actions (2026-07-11)

**For:** the human, working in Claude Design (claude.ai/design), canon project `Vesper` @ handoff 134.
**Source:** zero-trust re-audit Wave 2 (`design/reaudit-2026-07-open-findings.md`, Universal Search row) — spot-verified against `universal-search-app.jsx`, `travel-agent/backend/core/db/search.py`, `travel-agent/backend/search/dispatch.py`, `travel-app/components/search/UniversalSearchOverlay.tsx`.
**How to use this:** one decision, not a task list. Pick one direction; don't split the difference. If canon changes, regenerate the specimen in the same session.

---

## D25 — "Actions" as executable commands vs searchable audit log

**Conflict:** canon specifies the Actions result group as **executable command rows** ("must be executable… never decorative"). Code ships a deliberate architectural pivot: backend `search_trip_actions()` is explicitly an audit-log search ("without executing commands"); frontend `routeForUniversalItem` returns `null` for `is_action` rows; `UniversalSearchOverlay` renders them **disabled** with amber/gold command styling — looks executable, behaves as read-only history.

**This isn't drift from neglect.** The backend docstring and frontend routing null are self-documenting. The inversion was a safety choice (no re-execute from search) that was never reconciled with canon or renamed in the UI.

**Evidence (code, 2026-07-11):**
- `travel-agent/backend/core/db/search.py` — `search_trip_actions` docstring: audit rows, not commands
- `travel-agent/backend/search/dispatch.py` — `is_action=True`, `route=None`
- `travel-app/utils/universalSearchRouting.ts` — `if (item.is_action) return null`
- `travel-app/components/search/UniversalSearchOverlay.tsx` — `disabled={!href}` on action rows; amber tint styling

**Related (same surface, separate briefs optional):**
- Places provenance hardcoded `DISCOVER` — `saved_by` never consulted (substrate / data wiring)
- On-trip scope rail = **7 chips** vs canon max 4–5 (Receipts/Costs/Actions split out)

**Decide:** one of three directions —

1. **Canon owes code (audit log wins).** Rename the group to **History** or **Changes** (not "Actions"). Remove command-shaped styling (gold glyph, amber row tint). Update canon: search may surface past trip mutations as **navigable receipts**, never as re-executable commands. Taps route to Changes / proposal detail / receipt context — not re-run.
2. **Code owes canon (executable wins).** Define what "execute" means on tap: open concierge with prefilled intent, deep-link to undo surface, or invoke a gated backend action API. Specify safety model for group vs private actions. Wire `route` on dispatch + enable `Tap` in overlay.
3. **Hybrid (navigable receipts).** Rows are tappable but only **navigate to context** (proposal detail, expense, change row) — not re-execute. Canon updates to "executable" = "actionable navigation," not "repeat the mutation." Middle ground; still needs canon language change.

**Regenerate:** if (1), rename panels in `universal-search-app.jsx` and add **ACTIONS → HISTORY (D25)** comment. If (2), keep "Actions" label but add executable row anatomy + safety callouts. If (3), add "navigable receipt" row state distinct from command rows.

---

## Scope rail (optional same session)

If folding Receipts/Costs/Actions under **This trip** restores ≤5 chips, say so in canon. If the 7-chip rail is intentional, bless it explicitly — don't leave max-4-5 rule contradicting the specimen.

---

## After you re-export

Run `python3 scripts/canon-drift-check.py`; update `design/surface-manifest.yaml` Universal Search row with the ruling.
