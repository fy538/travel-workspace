# Prompt 99 — Final Synthesis And Master Punch List

```text
You are a Cursor Cloud agent synthesizing the dogfood readiness audit.

Workspace root:
/Users/feihuyan/Documents/Claude/Travel Workspace

Input folder:
docs/audits/dogfood-readiness-2026-05/areas/

Output:
docs/audits/dogfood-readiness-2026-05/MASTER-PUNCH-LIST.md

Rules:
- Audit synthesis only. Do not change product code.
- Read every area report.
- Deduplicate findings across areas.
- Preserve source report links and file/line references.
- Do not inflate severity. P0 requires a concrete dogfood-blocking path.
- If a finding is suspected and not confirmed, keep it separate from confirmed blockers.
- Identify recurring bug classes that should become lints, tests, or CI gates.

Create a master report with:

1. Executive verdict:
   - Ready for local dogfood?
   - Ready for TestFlight/internal real-backend dogfood?
   - Ready for external/semi-external testers?

2. P0 dogfood blockers:
   - one row per deduped finding
   - owner surface: backend/frontend/workspace/account
   - source area report
   - exact repro/check
   - recommended fix direction

3. P1 must-fix before broader dogfood:
   - grouped by golden path

4. P2/P3 backlog:
   - grouped by area

5. Structural gates to add:
   - auth/rate limit checks
   - mock-real parity checks
   - privacy phrase leak tests
   - async DB/event-loop lint
   - Postgres/Qdrant drift checks
   - release/preflight checks

6. Suggested fix order:
   - shortest path to first safe internal dogfood
   - then path to TestFlight
   - then path to external beta

7. Tests/commands summary:
   - which commands passed/failed/not run across reports

Finish with a concise recommendation: fix-now list, gate-now list, and defer list.
```

