export const meta = {
  name: 'privacy-invariant-tracer',
  description: 'Statically trace every group/public/cross-user egress surface in travel-agent and prove the privacy guard is on the path; adversarially verify each candidate leak; emit confirmed leaks + regression evals.',
  whenToUse: 'Run to hunt privacy-leak bugs in the backend business logic. Finds paths where a private traveler constraint could reach group/public output without passing a canonical privacy guard.',
  phases: [
    { title: 'Map', detail: 'Pin down canonical guards + enumerate every egress surface (multi-modal sweep)' },
    { title: 'Trace', detail: 'Per surface: can private data reach it unguarded? Produce candidate leaks' },
    { title: 'Verify', detail: 'Adversarially refute each candidate; default to NOT-a-leak unless full path proven' },
    { title: 'Report', detail: 'Write confirmed leaks + per-leak regression eval to disk' },
  ],
}

const REPO = '/Users/feihuyan/travel-workspace/travel-agent'
const OUT = '/Users/feihuyan/travel-workspace/docs/audits'
// Machine-written run output — NEVER the hand-curated consolidated audit
// (privacy-invariant-trace.md). The report agent writes here so a rerun can't
// clobber human-tiered findings + FIXED status.
const RUN_REPORT = `${OUT}/privacy-trace-run-latest.md`

// Throttle: process surfaces through trace+verify in sequential waves of this
// size so the in-flight burst stays well under the server rate limit that
// nulled ~100 agents on the unthrottled 114-surface run.
const WAVE = 6

// Retry wrapper. agent() returns null when the call dies on a terminal API
// error after the harness's own retries (e.g. a sustained server rate limit).
// A null silently became an empty surface list / empty candidate list, which
// read downstream as "scanned & clean" — a false negative. Retry once more,
// then surface the failure to the caller (which records it as ERRORED, not
// clean). Returns {ok, value}.
async function tryAgent(prompt, opts, attempts = 2) {
  for (let k = 0; k < attempts; k++) {
    const value = await agent(prompt, opts)
    if (value !== null && value !== undefined) return { ok: true, value }
    log(`⚠ ${opts.label || 'agent'} returned null (attempt ${k + 1}/${attempts})`)
  }
  return { ok: false, value: null }
}

// Coverage ledger — what actually ran vs what errored out. Reported explicitly
// so "N surfaces scanned" can never overstate coverage again.
const coverage = { erroredAngles: [], erroredSurfaces: [], scannedSurfaces: 0 }

// ---- Schemas ----
const GUARD_SPEC = {
  type: 'object',
  required: ['guards', 'private_sources', 'prod_notes'],
  properties: {
    guards: {
      type: 'array',
      description: 'Canonical functions that, if on a path, make egress safe',
      items: {
        type: 'object',
        required: ['symbol', 'file', 'what_it_guards'],
        properties: {
          symbol: { type: 'string' },
          file: { type: 'string' },
          what_it_guards: { type: 'string' },
        },
      },
    },
    private_sources: {
      type: 'array',
      description: 'Functions/tables/fields that load or hold PRIVATE (1:1, confidential) traveler data',
      items: { type: 'string' },
    },
    prod_notes: {
      type: 'array',
      description: 'Prod-verified facts a verifier must cross-check before flagging (e.g. which redactor is actually wired)',
      items: { type: 'string' },
    },
  },
}

const SURFACE_SCHEMA = {
  type: 'object',
  required: ['surfaces'],
  properties: {
    surfaces: {
      type: 'array',
      items: {
        type: 'object',
        required: ['id', 'file', 'symbol', 'audience', 'why', 'entrypoint'],
        properties: {
          id: { type: 'string', description: 'kebab-case unique id' },
          file: { type: 'string', description: 'path relative to repo root' },
          symbol: { type: 'string', description: 'function/method that emits the output' },
          audience: { type: 'string', enum: ['group', 'public', 'cross-user', 'logs-telemetry'] },
          why: { type: 'string', description: 'why this output is visible beyond the private 1:1 author' },
          entrypoint: { type: 'string', description: 'API route / worker / proactive loop that reaches it' },
        },
      },
    },
  },
}

const TRACE_SCHEMA = {
  type: 'object',
  required: ['candidates'],
  properties: {
    candidates: {
      type: 'array',
      description: 'Candidate leaks. Empty array if this surface is provably guarded.',
      items: {
        type: 'object',
        required: ['title', 'file', 'line_hint', 'private_data', 'path', 'why_unguarded', 'severity', 'confidence'],
        properties: {
          title: { type: 'string' },
          file: { type: 'string' },
          line_hint: { type: 'string', description: 'line number or symbol where the gap is' },
          private_data: { type: 'string', description: 'what private datum can leak (e.g. dietary constraint, budget, identity-of-who-said-it)' },
          path: { type: 'string', description: 'private source -> ... -> egress, the concrete call chain' },
          why_unguarded: { type: 'string', description: 'which canonical guard is MISSING from this path and why it is reachable without it' },
          severity: { type: 'string', enum: ['critical', 'high', 'medium', 'low'] },
          confidence: { type: 'string', enum: ['high', 'medium', 'low'] },
        },
      },
    },
  },
}

const VERDICT_SCHEMA = {
  type: 'object',
  required: ['verdict', 'reasoning', 'guard_found_on_path', 'reproduction'],
  properties: {
    verdict: { type: 'string', enum: ['confirmed-leak', 'refuted', 'needs-human'] },
    reasoning: { type: 'string', description: 'the full-path trace you did to confirm or refute' },
    guard_found_on_path: { type: 'string', description: 'name the guard you found upstream that refutes it, or NONE' },
    reproduction: { type: 'string', description: 'concrete inputs + call that would trigger the leak, or why it cannot be triggered' },
  },
}

// ====================================================================
// PHASE 1 — MAP
// ====================================================================
phase('Map')

const guardSpecResult = await tryAgent(
  `You are pinning down the CANONICAL PRIVACY GUARDS in the travel-agent backend at ${REPO}.

Read these files fully and report the real, current guard surface:
- backend/concierge/privacy_redactor.py  (check_proposal_privacy, load_private_corpus_for_user/trip)
- backend/concierge/group_compose.py  (find_constraint_leaks, find_identity_leaks, _semantic_privacy_guard, _regenerate_with_extended_avoid, execute_compose_group_message)
- backend/concierge/strict_compose.py
- backend/concierge/telemetry_redactor.py
- backend/core/privacy_catalog.py  (effective_privacy_levels, should_omit_personal_memory_narrative_for_group_synthesis)
- backend/core/db/privacy.py and backend/core/models/privacy.py
- backend/situation/privacy.py
- backend/api/routes/privacy_audit.py

Then grep the test suite (tests/concierge/test_privacy_redactor.py, test_group_compose.py, tests/api/test_privacy_audit.py, tests/core/test_privacy_catalog.py) to understand what behavior is ALREADY covered by tests (so we don't re-report covered ground).

Return: (1) the canonical guards — the functions that, when present on a path, make group/public egress safe; (2) the private data sources — what loads or holds confidential 1:1 traveler data; (3) prod_notes — any facts a downstream verifier must know to avoid false positives (e.g. "the semantic guard runs on EVERY compose call", "telemetry is redacted at X"). Be precise with file paths and symbol names.`,
  { label: 'guard-spec', phase: 'Map', schema: GUARD_SPEC },
  3 // foundational — try harder before giving up
)

if (!guardSpecResult.ok) {
  // Without the guard spec nothing downstream can run correctly. Abort loud
  // rather than scan with an empty guard list (which would confirm every
  // surface as a "leak").
  return {
    aborted: true,
    reason:
      'guard-spec agent failed after retries (likely sustained rate limit). ' +
      'Re-run with Workflow({scriptPath, resumeFromRunId}) when the limit clears — ' +
      'the cached phases return instantly.',
  }
}
const guardSpec = guardSpecResult.value
const guardContext = JSON.stringify(guardSpec, null, 2)

// Multi-modal egress-surface sweep — each angle is blind to the others
const SWEEP_ANGLES = [
  {
    key: 'group-compose',
    prompt: `Find every code path that emits GROUP-VISIBLE chat / message text (text >1 traveler will read). Start from backend/concierge/group_compose.py and trace OUTWARD: who calls execute_compose_group_message, and are there OTHER paths that produce group chat text WITHOUT going through it? Look for direct call_llm() group replies, group event lines, vote widgets, member-facing summaries.`,
  },
  {
    key: 'proposals-plan',
    prompt: `Find every code path that emits PROPOSAL / PLAN-CHANGE text visible to the group. Start from propose_change and backend/concierge/privacy_redactor.py:check_proposal_privacy. Trace which plan-mutation / proposal-rationale / diff-summary paths produce group-facing text, and whether each passes check_proposal_privacy. grep for "propose", "rationale", "diff", "plan_event".`,
  },
  {
    key: 'proactive-notifications',
    prompt: `Find every code path in the PROACTIVE ENGINE and NOTIFICATION system that emits text to a user that could embed another user's private constraint (push copy, digest, nudge, "what now" tiles, channel fan-out). grep backend for proactive, notification, push, digest, nudge, supervised loops. These run server-side without a human in the loop — high leak risk.`,
  },
  {
    key: 'discover-public',
    prompt: `Find every code path that emits PUBLIC / cross-user DISCOVER content (feed, dossiers, boards, editorial, search results, recall band). Could any of it be composed from a specific user's private signals and shown to others? grep backend/discover and backend/home/compose.py. Focus on personalization that crosses the public boundary.`,
  },
  {
    key: 'atlas-shares-receipts',
    prompt: `Find every code path that emits SHARED / EXPORTED artifacts: Atlas shared artifacts, trust receipts, story shares, html shares, year-recap decks, share links. grep for share, receipt, story, html_share, atlas composer/map_compose. A share link is public — does any private datum or who-said-what attribution ride along?`,
  },
  {
    key: 'logs-telemetry',
    prompt: `Find every code path that writes private traveler data into LOGS, TELEMETRY, traces, reasoning_spans, concierge_turns, or error payloads WITHOUT the telemetry_redactor. grep for logger, log., span, trace, capture, Sentry, telemetry. Leaks into observability are real leaks.`,
  },
]

const sweeps = await parallel(
  SWEEP_ANGLES.map((a) => () =>
    tryAgent(
      `You are mapping privacy EGRESS SURFACES in the travel-agent backend at ${REPO} from ONE angle: ${a.key}.

Canonical guards + private sources already identified:
${guardContext}

YOUR ANGLE:
${a.prompt}

Use grep/read freely. Return a structured list of egress surfaces — each a concrete place where text/data leaves the private 1:1 boundary and reaches a wider audience. For each, give the file, the emitting symbol, the audience, why it's visible beyond the author, and the entrypoint (route/worker/loop) that reaches it. Do NOT judge yet whether it's guarded — just inventory the surfaces. Be exhaustive within your angle.`,
      { label: `sweep:${a.key}`, phase: 'Map', schema: SURFACE_SCHEMA }
    ).then((r) => ({ key: a.key, ...r }))
  )
)

// Record which angles ERRORED out (vs genuinely found nothing) so coverage is honest.
for (const s of sweeps) {
  if (!s || !s.ok) coverage.erroredAngles.push(s ? s.key : 'unknown')
}
if (coverage.erroredAngles.length) {
  log(`⚠ ${coverage.erroredAngles.length} sweep angle(s) ERRORED — NOT cleared: ${coverage.erroredAngles.join(', ')}`)
}

// Dedupe surfaces by file+symbol (plain code — needs all sweeps first, hence the barrier above)
const seen = new Set()
const surfaces = []
for (const s of sweeps) {
  if (!s || !s.ok || !s.value) continue
  for (const surf of s.value.surfaces || []) {
    const k = `${surf.file}::${surf.symbol}`
    if (seen.has(k)) continue
    seen.add(k)
    surfaces.push(surf)
  }
}
log(`Mapped ${surfaces.length} unique egress surfaces across ${SWEEP_ANGLES.length} angles`)

// ====================================================================
// PHASE 2+3 — TRACE then VERIFY (pipelined per surface, no barrier)
// ====================================================================
phase('Trace')

const traceStage = (surf) =>
  tryAgent(
    `You are tracing a single privacy EGRESS SURFACE in travel-agent at ${REPO} to find LEAKS.

SURFACE:
${JSON.stringify(surf, null, 2)}

CANONICAL GUARDS + PRIVATE SOURCES + PROD NOTES:
${guardContext}

TASK: Read the actual code for this surface and trace BACKWARD from the emitted output to its data sources. Determine: can any PRIVATE (confidential 1:1) traveler datum — a constraint (diet/budget/access/energy), a personal-memory narrative, OR the identity of who-said-what — reach this output WITHOUT passing one of the canonical guards on the path?

Rules:
- A path is GUARDED if a canonical guard (e.g. find_constraint_leaks, _semantic_privacy_guard, check_proposal_privacy, telemetry_redactor, should_omit_personal_memory_narrative_for_group_synthesis) provably runs between the private source and this egress.
- Only report a candidate if you can name the concrete private datum, the concrete call chain, and the SPECIFIC guard that is missing.
- If the surface is provably guarded, return an empty candidates array. Do not invent leaks.
- Aggregated/anonymized constraints intended for group synthesis are NOT leaks unless they expose who said it or an individual's confidential value verbatim.

Return candidate leaks (possibly empty).`,
    { label: `trace:${surf.id}`, phase: 'Trace', schema: TRACE_SCHEMA }
  ).then((r) => ({ surf, ...r }))

const verifyStage = (traced) => {
  // traced.surf + traced.ok + traced.value. A trace that ERRORED is recorded as
  // a coverage gap (NOT silently treated as "clean").
  const surf = traced.surf
  if (!traced.ok || !traced.value) {
    coverage.erroredSurfaces.push(surf.id)
    return []
  }
  coverage.scannedSurfaces += 1
  const cands = traced.value.candidates || []
  if (!cands.length) return []
  return parallel(
    cands.map((c) => () =>
      tryAgent(
        `You are an ADVERSARIAL VERIFIER. Your job is to REFUTE this claimed privacy leak, not confirm it. Default to "refuted" unless you can prove the full leak path.

CLAIMED LEAK:
${JSON.stringify(c, null, 2)}

CANONICAL GUARDS + PRIVATE SOURCES + PROD NOTES (cross-check these — a finding that contradicts a prod_note is refuted):
${guardContext}

Repo: ${REPO}. Read the real code along the ENTIRE path from private source to egress. Try hard to find a guard UPSTREAM that the trace agent missed (a redactor called by a caller, a gate in the router, an aggregation that strips identity, a privacy-level check). Confirm ONLY if:
  (1) a concrete private datum is provably reachable at the egress,
  (2) NO canonical guard sits on the path,
  (3) you can state concrete inputs that trigger it,
  (4) it is not already covered by an existing test.
Otherwise refute. If you genuinely cannot tell without running it, say needs-human.

Return your verdict with the full-path reasoning, the guard you found (or NONE), and a concrete reproduction.`,
        { label: `verify:${surf.id}`, phase: 'Verify', schema: VERDICT_SCHEMA }
      ).then((v) =>
        // A verify that ERRORED is escalated to needs-human, never dropped.
        v.ok
          ? { surface: surf, candidate: c, verdict: v.value }
          : { surface: surf, candidate: c, verdict: { verdict: 'needs-human', reasoning: 'verifier errored (rate limit) — not adjudicated', guard_found_on_path: 'UNKNOWN', reproduction: c.path } }
      )
    )
  )
}

// Throttle: run trace+verify in sequential waves of WAVE surfaces so the
// in-flight burst stays under the server rate limit. Each wave is a small
// pipeline (trace→verify, no barrier within the wave).
const perSurface = []
for (let i = 0; i < surfaces.length; i += WAVE) {
  const chunk = surfaces.slice(i, i + WAVE)
  const waveResults = await pipeline(chunk, traceStage, verifyStage)
  perSurface.push(...waveResults)
  log(`Traced ${Math.min(i + WAVE, surfaces.length)}/${surfaces.length} surfaces (${coverage.erroredSurfaces.length} errored)`)
}

const confirmed = perSurface
  .flat()
  .filter(Boolean)
  .filter((r) => r.verdict && r.verdict.verdict === 'confirmed-leak')
const needsHuman = perSurface
  .flat()
  .filter(Boolean)
  .filter((r) => r.verdict && r.verdict.verdict === 'needs-human')

log(
  `Confirmed ${confirmed.length} leaks, ${needsHuman.length} need human judgment. ` +
    `Coverage: ${coverage.scannedSurfaces}/${surfaces.length} surfaces scanned, ` +
    `${coverage.erroredSurfaces.length} errored, ${coverage.erroredAngles.length} sweep angles errored.`
)

// ====================================================================
// PHASE 4 — REPORT (+ regression eval per confirmed leak)
// ====================================================================
phase('Report')

const coverageBlock = `COVERAGE LEDGER (report this honestly — do NOT overstate):
- surfaces inventoried: ${surfaces.length}
- surfaces actually traced (scanned): ${coverage.scannedSurfaces}
- surfaces ERRORED (rate-limited, NOT cleared): ${coverage.erroredSurfaces.length} ${coverage.erroredSurfaces.length ? '→ ' + coverage.erroredSurfaces.join(', ') : ''}
- sweep angles ERRORED (whole angle missing, NOT cleared): ${coverage.erroredAngles.length} ${coverage.erroredAngles.length ? '→ ' + coverage.erroredAngles.join(', ') : ''}`

const reportAgent = await agent(
  `Write a privacy-leak audit RUN report and the regression artifacts, then SAVE them to disk.

CONFIRMED LEAKS (${confirmed.length}):
${JSON.stringify(confirmed, null, 2)}

NEEDS-HUMAN (${needsHuman.length}):
${JSON.stringify(needsHuman, null, 2)}

${coverageBlock}

CANONICAL GUARD SPEC:
${guardContext}

Do the following:
1. Write a markdown report to ${RUN_REPORT} (this is the MACHINE run-output file — it is safe to overwrite). Start with a summary line: "N confirmed / M needs-human / X scanned / Y errored". Then a **COVERAGE** section reproducing the ledger above verbatim, with a bold warning that errored surfaces/angles are NOT cleared, merely unexamined. Then per confirmed leak: title, severity, file:line, private datum, full leak path, missing guard, concrete reproduction (severity order, critical first). Then a "Needs human judgment" section. Then an appendix listing every scanned surface id.
2. **Do NOT touch ${OUT}/privacy-invariant-trace.md** — that is the human-curated consolidated audit with hand-tiered FIXED status. Your job is only the run-output file above. (A human merges confirmed findings into the curated doc.)
3. For each CONFIRMED leak, append a regression test stub into ${OUT}/privacy-regression-stubs.py — a pytest function named test_no_leak_<surface_id_snake> with a docstring describing the leak and a TODO body. Match conventions in ${REPO}/tests/concierge/test_privacy_redactor.py and test_group_compose.py (read them first). If there are zero confirmed leaks, skip this file.
4. Use the Write tool. Confirm the absolute paths written.

Return: the absolute paths you wrote, the confirmed count by severity, the coverage ledger, and a 3-sentence executive summary for the founder.`,
  { label: 'report', phase: 'Report' }
)

return {
  surfaces_inventoried: surfaces.length,
  surfaces_scanned: coverage.scannedSurfaces,
  surfaces_errored: coverage.erroredSurfaces.length,
  angles_errored: coverage.erroredAngles,
  confirmed_leaks: confirmed.length,
  needs_human: needsHuman.length,
  confirmed: confirmed.map((r) => ({
    title: r.candidate.title,
    severity: r.candidate.severity,
    file: r.candidate.file,
    line: r.candidate.line_hint,
    private_data: r.candidate.private_data,
  })),
  report: reportAgent,
}
