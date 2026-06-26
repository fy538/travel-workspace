export const meta = {
  name: 'privacy-triage',
  description: 'Re-verify the privacy-tracer Run-3 confirmed findings with sharper lenses (group-vs-1:1, existing-guard, user-vs-operator, human-in-loop) to separate real user-facing leaks from over-confirmations, and emit a precise per-finding fix plan.',
  whenToUse: 'Run after the privacy-invariant-tracer full-coverage run to triage its (over-confirmed) findings before fixing.',
  phases: [
    { title: 'Extract', detail: 'Read the run-output findings file into a structured list' },
    { title: 'Triage', detail: 'Per finding: resolve group-vs-1:1, existing guard, reachability; verdict + fix' },
    { title: 'Plan', detail: 'Cluster verified-real leaks, identify shared chokepoints, write fix plan' },
  ],
}

const REPO = '/Users/feihuyan/travel-workspace/travel-agent'
const RUN_FILE = '/Users/feihuyan/travel-workspace/docs/audits/privacy-trace-run-latest.md'
const OUT = '/Users/feihuyan/travel-workspace/docs/audits/privacy-triage-plan.md'
const WAVE = 6

async function tryAgent(prompt, opts, attempts = 2) {
  for (let k = 0; k < attempts; k++) {
    const value = await agent(prompt, opts)
    if (value !== null && value !== undefined) return { ok: true, value }
    log(`⚠ ${opts.label || 'agent'} null (attempt ${k + 1}/${attempts})`)
  }
  return { ok: false, value: null }
}

const FINDINGS_SCHEMA = {
  type: 'object',
  required: ['findings'],
  properties: {
    findings: {
      type: 'array',
      items: {
        type: 'object',
        required: ['id', 'cluster', 'title', 'file', 'severity', 'private_data'],
        properties: {
          id: { type: 'string', description: 'kebab-case stable id' },
          cluster: { type: 'string', description: 'A|B|C|D|E|F|G|H per the run report clustering, best guess' },
          title: { type: 'string' },
          file: { type: 'string' },
          severity: { type: 'string' },
          private_data: { type: 'string' },
        },
      },
    },
  },
}

const VERDICT_SCHEMA = {
  type: 'object',
  required: ['verdict', 'audience', 'existing_mitigation', 'reachable', 'reasoning', 'fix', 'fix_chokepoint', 'confidence'],
  properties: {
    verdict: {
      type: 'string',
      enum: ['real-user-leak', 'real-operator-leak', 'mitigated', 'false-positive', 'needs-human'],
      description: 'real-user-leak = private data reaches another USER; real-operator-leak = only logs/dashboards; mitigated = a guard or human-in-loop preview already covers it; false-positive = not actually reachable',
    },
    audience: { type: 'string', enum: ['group', 'public', 'cross-user', 'operator-logs', 'self-1to1', 'unclear'], description: 'who actually sees this egress' },
    existing_mitigation: { type: 'string', description: 'any guard / human-preview / anonymization already on the path, or NONE' },
    reachable: { type: 'boolean', description: 'can a concrete private datum actually reach the egress (not just theoretically)' },
    reasoning: { type: 'string', description: 'the full-path trace + the group-vs-1to1 determination with evidence (file:line)' },
    fix: { type: 'string', description: 'the precise fix if real (e.g. which guard to add where), else why none needed' },
    fix_chokepoint: { type: 'string', description: 'the single function/line where the fix belongs, or SHARED:<name> if multiple findings share it' },
    confidence: { type: 'string', enum: ['high', 'medium', 'low'] },
  },
}

// ============ PHASE 1 — EXTRACT ============
phase('Extract')

const extracted = await tryAgent(
  `Read ${RUN_FILE} (a privacy-leak run report). Extract EVERY confirmed leak it lists into a structured array.
For each: a stable kebab-case id, the cluster letter (A tool-emitted cards / B proactive system-message persists / C daily digest / D story hero_title / E Atlas Unpacked public cards / F cross-user feeds (discover, invite) / G booking writeback / H telemetry & logs), the title, the primary file, the severity, and the private_data description.
EXCLUDE anything in cluster C (daily digest) — already fixed. Return all the rest.`,
  { label: 'extract', phase: 'Extract', schema: FINDINGS_SCHEMA },
  3
)

if (!extracted.ok) {
  return { aborted: true, reason: 'could not read/extract the run-output findings file' }
}
const findings = extracted.value.findings
log(`Extracted ${findings.length} findings to triage (cluster C excluded)`)

// ============ PHASE 2 — TRIAGE (sharper lenses) ============
phase('Triage')

const triaged = []
for (let i = 0; i < findings.length; i += WAVE) {
  const chunk = findings.slice(i, i + WAVE)
  const waveResults = await parallel(
    chunk.map((f) => () =>
      tryAgent(
        `You are TRIAGING a claimed privacy leak in travel-agent at ${REPO}. The original verifier OVER-CONFIRMED similar findings by (a) assuming GROUP exposure without checking, (b) ignoring human-in-the-loop preview gates, and (c) flagging operator-only logs as user leaks. Apply these sharper lenses and read the REAL code.

CLAIMED FINDING:
${JSON.stringify(f, null, 2)}

Resolve, with file:line evidence:
1. AUDIENCE — does this egress actually reach another USER (group chat / public page / a different user's feed), or is it the requester's OWN 1:1 thread (self — not a leak), or operator-only (logs/telemetry/admin dashboards)? Trace the conversation_id / route / consumer to prove it. For a card/message tool, determine whether the conversation it posts to is the GROUP trip conversation or a 1:1 user thread.
2. EXISTING MITIGATION — is there already a guard (check_private_signal/find_constraint_leaks/redact/strip_private_group_sections/compose), an anonymization, OR a human-in-the-loop preview (e.g. owner reviews before share) on the path?
3. REACHABILITY — can a CONCRETE private datum actually reach it, or is it only "an LLM could theoretically write something"? Per the project model, naming a trip member is NOT a leak (the group knows who's on the trip) — only a private CONSTRAINT VALUE or who-holds-which-constraint attribution is.

Then give a verdict:
- real-user-leak: concrete private constraint reaches another user, no mitigation.
- real-operator-leak: only reaches logs/dashboards (still worth noting, lower priority).
- mitigated: a guard or human-preview already covers it.
- false-positive: not actually reachable / self-1to1 / names-only.
- needs-human: genuinely hinges on product judgment.

If real, give the PRECISE fix and the single chokepoint where it belongs (use SHARED:<name> when several findings share one chokepoint, e.g. SHARED:create_message). Be specific and grounded.`,
        { label: `triage:${f.id}`, phase: 'Triage', schema: VERDICT_SCHEMA }
      ).then((r) => ({ finding: f, ...r }))
    )
  )
  triaged.push(...waveResults)
  log(`Triaged ${Math.min(i + WAVE, findings.length)}/${findings.length}`)
}

const ok = triaged.filter((t) => t && t.ok).map((t) => ({ finding: t.finding, ...t.value }))
const realUser = ok.filter((t) => t.verdict === 'real-user-leak')
const realOps = ok.filter((t) => t.verdict === 'real-operator-leak')
const mitigated = ok.filter((t) => t.verdict === 'mitigated')
const falsePos = ok.filter((t) => t.verdict === 'false-positive')
const needsHuman = ok.filter((t) => t.verdict === 'needs-human')
log(`Triage: ${realUser.length} real-user, ${realOps.length} real-operator, ${mitigated.length} mitigated, ${falsePos.length} false-positive, ${needsHuman.length} needs-human`)

// ============ PHASE 3 — PLAN ============
phase('Plan')

const planAgent = await agent(
  `Write a privacy-triage fix plan to ${OUT} (Write tool) and confirm the path.

TRIAGE RESULTS (post sharper-lens re-verification of the Run-3 findings; cluster C already fixed):

REAL USER-FACING LEAKS (${realUser.length}):
${JSON.stringify(realUser, null, 2)}

REAL OPERATOR-ONLY LEAKS (${realOps.length}):
${JSON.stringify(realOps, null, 2)}

MITIGATED / FALSE-POSITIVE (${mitigated.length + falsePos.length}):
${JSON.stringify([...mitigated, ...falsePos].map((t) => ({ id: t.finding.id, verdict: t.verdict, why: t.existing_mitigation || t.reasoning })), null, 2)}

NEEDS-HUMAN (${needsHuman.length}):
${JSON.stringify(needsHuman, null, 2)}

The doc must have:
1. A one-line headline: X real user leaks / Y operator-only / Z dismissed (mitigated+false) / W needs-human, out of ${findings.length} triaged.
2. **Shared chokepoints** — group the real-user-leaks by fix_chokepoint (e.g. SHARED:create_message). For each shared chokepoint, note how many findings one fix would close and sketch the fix.
3. **Ordered fix plan** for the real-user-leaks (highest blast-radius shared chokepoint first), each with file:line, the precise fix, and audience evidence.
4. A short **Operator-only** section (lower priority).
5. A **Dismissed** table (id + why) so the over-confirmations are on record.
6. A **Needs-human** section (product-judgment calls).

Return: the path written, and the counts.`,
  { label: 'plan', phase: 'Plan' }
)

return {
  triaged: findings.length,
  real_user_leaks: realUser.length,
  real_operator_leaks: realOps.length,
  mitigated: mitigated.length,
  false_positive: falsePos.length,
  needs_human: needsHuman.length,
  shared_chokepoints: [...new Set(realUser.map((t) => t.fix_chokepoint).filter(Boolean))],
  real_user_findings: realUser.map((t) => ({ id: t.finding.id, cluster: t.finding.cluster, title: t.finding.title, audience: t.audience, chokepoint: t.fix_chokepoint, fix: t.fix })),
  plan: planAgent,
}
