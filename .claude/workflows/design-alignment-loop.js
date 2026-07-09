export const meta = {
  name: 'design-alignment-loop',
  description: 'Autonomously audit product surfaces against design canon and fix gaps in code, batching many surfaces onto one shared branch and opening a single consolidated PR for human merge',
  phases: [
    { title: 'Preflight', detail: 'Refuse to run against a dirty shared checkout — protects any of your own in-progress work' },
    { title: 'Discover', detail: 'Read surface-manifest.yaml + canon-drift-check to build the work queue, skipping surfaces with an open design-align branch already' },
    { title: 'Audit+Fix', detail: 'Per surface, sequential (shared simulator + shared checkout): screenshot vs canon, write a brief, implement, verify, push, leave the tree clean' },
    { title: 'Review', detail: 'Independent adversarial code review of each pushed branch' },
    { title: 'Consolidate', detail: 'In a real, self-managed git worktree: merge every approved branch onto one integration branch, open ONE PR for human merge' },
  ],
}

// How many surfaces to process in this batch. Default is a moderate first batch —
// raise args.limit once you've seen a batch's PR quality once.
const LIMIT = (args && args.limit) || 5

const REPO = '/Users/feihuyan/travel-workspace'
const APP = `${REPO}/travel-app`

// Shared everywhere a surface name needs to become a branch suffix — used both to
// filter out surfaces with an already-open branch (deterministically, in plain code,
// not left to an agent's judgment — that was unreliable in practice) and to name the
// branch Fix creates. One function, one definition of "the branch for this surface."
const slugify = (name) => name.toLowerCase().replace(/[^a-z0-9]+/g, '-')

const DISCOVER_SCHEMA = {
  type: 'object',
  required: ['queue'],
  properties: {
    queue: {
      type: 'array',
      items: {
        type: 'object',
        required: ['surface', 'canon_files', 'code_paths', 'status', 'polish_qa_slug'],
        properties: {
          surface: { type: 'string' },
          canon_files: { type: 'array', items: { type: 'string' } },
          code_paths: { type: 'array', items: { type: 'string' } },
          status: { type: 'string' },
          polish_qa_slug: { type: ['string', 'null'] },
        },
      },
    },
  },
}

const AUDIT_SCHEMA = {
  type: 'object',
  required: ['has_gap', 'brief_markdown', 'summary'],
  properties: {
    has_gap: { type: 'boolean' },
    brief_markdown: { type: 'string' },
    summary: { type: 'string' },
  },
}

const FIX_SCHEMA = {
  type: 'object',
  required: ['branch', 'commits', 'pushed', 'gap_closed', 'left_clean', 'notes'],
  properties: {
    branch: { type: 'string' },
    commits: { type: 'array', items: { type: 'string' } },
    pushed: { type: 'boolean' },
    gap_closed: { type: 'boolean' },
    left_clean: { type: 'boolean', description: 'checked out back to main, git status --porcelain empty, before finishing' },
    notes: { type: 'string' },
  },
}

const REVIEW_SCHEMA = {
  type: 'object',
  required: ['approved', 'findings'],
  properties: {
    approved: { type: 'boolean' },
    findings: {
      type: 'array',
      items: {
        type: 'object',
        required: ['severity', 'summary'],
        properties: { severity: { type: 'string' }, summary: { type: 'string' } },
      },
    },
  },
}

// ---- Preflight: the shared checkout is real infrastructure (Fix stage needs the
// live Metro/simulator environment, so it can't be moved into an isolated worktree
// the way Consolidate can). The one thing that already burned us is silently
// inheriting someone else's uncommitted work on a stray branch — so refuse to start
// at all unless the checkout is clean and on main. ----
phase('Preflight')
const preflight = await agent(`
Run, in ${APP}:
  git status --porcelain
  git branch --show-current
Report back: is the working tree completely clean (no modified/untracked files), and
is the current branch "main"? Return JSON: {"clean": boolean, "branch": "<name>",
"detail": "<git status output verbatim if not clean>"}.
`, {
  schema: {
    type: 'object',
    required: ['clean', 'branch', 'detail'],
    properties: { clean: { type: 'boolean' }, branch: { type: 'string' }, detail: { type: 'string' } },
  },
  label: 'preflight-clean-check',
})

if (!preflight || !preflight.clean || preflight.branch !== 'main') {
  log(`ABORTING — ${APP} is not clean on main (branch=${preflight && preflight.branch}, clean=${preflight && preflight.clean}). This almost certainly means real in-progress work is sitting in the shared checkout. Not touching it. Detail:\n${preflight && preflight.detail}`)
  return {
    aborted: true,
    reason: 'shared checkout was not clean on main at preflight',
    detail: preflight,
  }
}
log('Preflight OK — shared checkout is clean and on main.')

phase('Discover')
const discovery = await agent(`
Read ${REPO}/design/surface-manifest.yaml. Select every surface whose status is
"gap", "partial", or "unmapped" (skip "aligned" and "deferred"). Then run:
  python3 ${REPO}/scripts/canon-drift-check.py
and prioritize any surface that command flags as freshly stale.

For each selected surface, read ${APP}/scripts/polish-qa/surfaces.mjs (its
listSurfaces()/resolveSurface() exports) and find the matching registered slug that
run-polish-qa.mjs would accept for this surface. If nothing matches, set
polish_qa_slug to null — do not guess a slug.

Order the queue: drift-flagged surfaces first, then manifest order. Return the full
queue as structured output.
`, { schema: DISCOVER_SCHEMA, label: 'discover-queue' })

// Which surfaces already have work in flight — checked here in plain code, not left
// to an agent's judgment inside a larger prompt. That was tried (asking Discover to
// read git ls-remote and self-exclude) and didn't reliably hold: a prior run still
// re-picked two surfaces that already had open branches. A single deterministic
// string match against the same slugify() Fix uses to name branches can't drift.
const branchList = await agent(`
Run: git ls-remote --heads origin
Return every ref name under refs/heads/ as a plain list of branch names (e.g.
"design-align/costs", "main", "design-align/batch-1" — everything, unfiltered).
`, {
  schema: { type: 'object', required: ['branches'], properties: { branches: { type: 'array', items: { type: 'string' } } } },
  label: 'list-remote-branches',
})
const openSurfaceBranches = new Set(
  ((branchList && branchList.branches) || [])
    .filter(b => b.startsWith('design-align/') && !b.startsWith('design-align/batch-'))
)

const allCandidates = (discovery && discovery.queue) || []
const alreadyInFlight = allCandidates.filter(s => openSurfaceBranches.has(`design-align/${slugify(s.surface)}`))
if (alreadyInFlight.length) {
  log(`Skipping ${alreadyInFlight.length} surface(s) with an already-open branch from a prior run: ${alreadyInFlight.map(s => s.surface).join(', ')}`)
}
const notInFlight = allCandidates.filter(s => !openSurfaceBranches.has(`design-align/${slugify(s.surface)}`))
const queue = notInFlight.filter(s => s.polish_qa_slug).slice(0, LIMIT)
const skipped = notInFlight.filter(s => !s.polish_qa_slug)
if (skipped.length) {
  log(`Skipping ${skipped.length} surface(s) with no registered polish-qa slug (needs surfaces.mjs registration first, not auto-fixed): ${skipped.map(s => s.surface).join(', ')}`)
}
log(`Batch size ${queue.length} of ${allCandidates.length} candidate surface(s) this run (limit=${LIMIT}).`)

// ---- Audit + Fix: sequential across surfaces — Maestro owns a single simulator,
// so two surfaces' device-touching stages must never overlap in wall-clock time. ----
phase('Audit+Fix')
const auditedAndFixed = []
for (const surface of queue) {
  const audit = await agent(`
Surface: ${surface.surface}
Canon (read-only, under ${REPO}/design/vesper-canon-anchor/project/): ${surface.canon_files.join(', ')}
Current code: ${surface.code_paths.join(', ')}

1. Run: node ${APP}/scripts/polish-qa/run-polish-qa.mjs ${surface.polish_qa_slug} --before
   to capture the current on-device rendering.
2. Read the canon file(s) — self-contained JSX mockups describing every intended
   state/variant for this surface.
3. Compare state-by-state: does the code implement every variant the canon defines,
   with matching copy, layout, and state-handling logic (not just colors/spacing)?
   See design/code-alignment-brief-G1-stay-state-space.md for the format and rigor
   level this project expects — wrong composition used, missing state variants,
   hardcoded values that should be dynamic, and backend-gated fields that must be
   flagged rather than faked are the known gap shapes here.
4. Read and follow ~/.claude/skills/mvp-invariants/SKILL.md — in particular: never
   recommend fabricating data for a backend-gated field; flag it instead.
5. If there is a real, actionable gap, write a full brief in the exact structure of
   design/code-alignment-brief-G1-stay-state-space.md: numbered Task sections with
   file:line pointers, a "## Done" checklist, and the standing-rules block (git status
   first branch from main, one commit per task, typecheck+tests green, flag
   backend-gated items don't fake data). If the surface is already correctly aligned,
   set has_gap false and leave brief_markdown empty.

Return has_gap, brief_markdown, and a one-paragraph summary.
`, { schema: AUDIT_SCHEMA, phase: 'Audit+Fix', label: `audit:${surface.surface}` })

  if (!audit || !audit.has_gap) {
    log(`${surface.surface}: no gap found, nothing to fix.`)
    auditedAndFixed.push({ surface, audit, fix: null })
    continue
  }

  const branchSlug = slugify(surface.surface)
  const fix = await agent(`
${audit.brief_markdown}

Work inside ${APP}. First check whether design-align/${branchSlug} already exists on
origin (git ls-remote --heads origin design-align/${branchSlug}):

- If it does NOT exist: create and check out a new branch off main named
  design-align/${branchSlug}.
- If it DOES exist (a prior run left work here): fetch it, check it out, then rebase
  it onto the current origin/main (git fetch origin main && git rebase origin/main)
  BEFORE adding anything new. A branch that sits open across runs goes stale relative
  to main and gets correctly rejected by review for it — rebasing first is what
  prevents that. If the rebase is clean, continue and add this run's work on top of
  the (now current) existing commits. If the rebase produces real conflicts, STOP —
  do not attempt to resolve them yourself. Run "git rebase --abort", leave the
  existing remote branch untouched, and report gap_closed=false, pushed=false, with
  notes explaining the conflict so a human resolves it directly.

Implement every task in the brief above, following the standing rules exactly: git
status first, one commit per task, typecheck + relevant tests green before each
commit, never fake data for a backend-gated field (note it in the commit message and
move on — do not stub it as if real). Also read and follow
~/.claude/skills/mvp-invariants/SKILL.md throughout — especially rule 5 (use the
existing canonical mutation builder rather than adding a parallel path, if you touch
any proposal/booking/expense code) and rule 3 (never let a stub stand in for the real
thing).

Once every task is committed, run:
  node ${APP}/scripts/polish-qa/run-polish-qa.mjs ${surface.polish_qa_slug} --after
and re-compare against the same canon file(s) from the brief. Confirm every item in
the brief's "## Done" checklist is now true on screen (backend-gated items intentionally
flagged-not-fixed in the brief are expected to remain open — that is correct, not a
failure).

Push the branch to origin. If you rebased an existing branch above, the history was
rewritten, so a plain push will be rejected as non-fast-forward — use
"git push --force-with-lease -u origin design-align/${branchSlug}" in that case (safe
here because this branch is only ever written by this pipeline, never hand-edited).
If you created a fresh branch, a plain "git push -u origin design-align/${branchSlug}"
is enough. Do NOT open a PR and do NOT merge — that happens in a later, independent,
batched step.

Before you finish — this matters as much as the fix itself, because the next surface
in this batch starts its own work in this same shared checkout right after you:
checkout back to main (git checkout main) and run git status --porcelain. It must be
completely empty. If it isn't — a scratch file, a leftover node process artifact,
anything — clean it up (git checkout -- <file> / rm the stray file, as appropriate)
until it is. Do not leave the shared checkout in any state other than "clean, on main"
when you return.

Return: branch name, the list of commit messages, whether the push succeeded, whether
you confirmed the gap closed on-screen (gap_closed), whether you confirmed the checkout
is back on main with an empty git status --porcelain (left_clean), and any notes
(including any flagged backend-gated items still open by design).
`, { schema: FIX_SCHEMA, phase: 'Audit+Fix', label: `fix:${surface.surface}` })

  auditedAndFixed.push({ surface, audit, fix })

  if (fix && !fix.left_clean) {
    log(`ABORTING BATCH — ${surface.surface}'s fix agent did not confirm the shared checkout was left clean on main. Refusing to start the next surface against a checkout in an unknown state. Fix branch (${fix.branch}) is still pushed and safe; go look at ${APP} by hand before re-running.`)
    return {
      aborted: true,
      reason: `fix stage for ${surface.surface} did not leave the shared checkout clean`,
      auditedAndFixed,
    }
  }
}

const withFixes = auditedAndFixed.filter(x => x.fix)
log(`${withFixes.length} of ${queue.length} surface(s) had a real gap and produced a pushed branch.`)

// ---- Review: independent, adversarial. Sequential (not parallel) — worktree
// isolation isn't available in this session (the launch cwd isn't a git repo), so
// concurrent `git fetch`/`git diff` against the same shared checkout is a real race
// risk without it. Review calls are cheap; running them one at a time is the safe
// trade, not a meaningful slowdown. ----
phase('Review')
const reviewed = []
for (const x of withFixes) {
  const review = await agent(`
Independently and adversarially review the branch "${x.fix.branch}" for surface
${x.surface.surface} in ${APP}. From the existing checkout, run:
  git fetch origin ${x.fix.branch}
  git diff main...origin/${x.fix.branch}
and review that diff on its own merits — you did not write this code, do not assume it
is correct. Check specifically for: correctness bugs, any fabricated/faked value
standing in for a real one, a new parallel mutation path where a canonical builder
already exists, and anything that violates ~/.claude/skills/mvp-invariants/SKILL.md
(read it first). Default to NOT approved unless you can point to the specific diff
hunk that satisfies each task in this brief:

${x.audit.brief_markdown}

Return approved (boolean) and a findings list (severity + summary) for anything that
should block inclusion in the batch PR. An empty findings list with approved=true means
you found nothing blocking.
`, { schema: REVIEW_SCHEMA, phase: 'Review', label: `review:${x.surface.surface}` })
  reviewed.push({ ...x, review })
}

const results = reviewed.filter(Boolean)
const included = results.filter(r => r.review && r.review.approved && r.fix.gap_closed && r.fix.pushed)
const excluded = results.filter(r => !included.includes(r))

log(`${included.length} surface(s) approved for the batch PR; ${excluded.length} excluded (need individual attention).`)

// ---- Consolidate: one agent, one integration branch, ONE PR — the single human
// touchpoint for this whole batch. Never merges; that's the founder's click.
//
// This stage needs no Metro/simulator/node_modules — just git + gh — so unlike Fix,
// it gets REAL directory isolation: a self-managed `git worktree add` against the
// actual repo (not the harness's `isolation: 'worktree'` option, which fails in this
// session because the session's own launch directory isn't a git repo — see the
// design-alignment-loop postmortem). This keeps Consolidate's branch-juggling
// completely off the shared checkout Fix uses, at near-zero cost. ----
phase('Consolidate')
let consolidation = null
if (included.length > 0) {
  consolidation = await agent(`
You are consolidating ${included.length} independently-reviewed, already-pushed
branches into ONE batch PR against main. Do this work in a REAL git worktree, not the
shared ${APP} checkout (that checkout is Fix's territory and must stay untouched).

1. Pick an unused integration name: run "git -C ${APP} branch -r | grep design-align/batch-"
   and take the next free integer, e.g. design-align/batch-3.
2. Create a real worktree yourself (this is plain git, not the harness isolation
   option — it works regardless of where this session was launched from):
     git -C ${APP} fetch origin main
     git -C ${APP} worktree add ${REPO}/travel-app-consolidate-<n> -b design-align/batch-<n> origin/main
   Do all merging inside that new ${REPO}/travel-app-consolidate-<n> directory.
3. Merge each branch below into it, one at a time. If a real merge conflict occurs
   between two of these branches (both touched the same lines), resolve it by
   re-reading both surfaces' briefs and preserving the intent of both — if you cannot
   resolve it confidently, drop that branch from the batch, note it in the PR
   description as "excluded — merge conflict with <other branch>, needs manual
   consolidation," and continue with the rest.

Branches to merge in (each already passed independent review and on-screen verify):
${included.map(r => `- ${r.fix.branch} (surface: ${r.surface.surface}) — ${r.audit.summary}`).join('\n')}

4. Push the integration branch. Open ONE PR against main. In the description, include
   a table: surface | gap summary | commits | verify result | review verdict — one row
   per successfully-included surface — plus a clearly separated "Excluded from this
   batch — needs individual attention" section listing:
${excluded.map(r => `   - ${r.surface.surface}: branch ${r.fix ? r.fix.branch : '(none — audit found no gap or fix failed)'}, reason: ${!r.fix ? 'no fix produced' : !r.fix.pushed ? 'push failed' : !r.fix.gap_closed ? 'verify did not confirm gap closed' : 'independent review found blocking issues: ' + JSON.stringify(r.review && r.review.findings)}`).join('\n') || '   (none)'}
5. When done, remove the worktree so it doesn't linger: git -C ${APP} worktree remove
   ${REPO}/travel-app-consolidate-<n> (the branch itself stays on origin — only the
   local worktree directory is cleaned up).

Do NOT merge this PR — that is the founder's decision. Return the PR URL and the final
integration branch name.
`, { phase: 'Consolidate', label: 'consolidate-batch' })
} else {
  log('Nothing approved this run — no batch PR opened.')
}

return {
  queue: queue.map(q => q.surface),
  skipped_no_slug: skipped.map(s => s.surface),
  no_gap: auditedAndFixed.filter(x => !x.fix).map(x => x.surface.surface),
  included_in_batch: included.map(r => r.surface.surface),
  excluded_needs_attention: excluded.map(r => ({
    surface: r.surface.surface,
    branch: r.fix ? r.fix.branch : null,
  })),
  consolidation,
}
