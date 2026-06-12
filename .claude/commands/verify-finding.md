Adversarially verify a finding, claim, bug report, or proposed diff before you
act on it. The model that produced a result must never be the one that grades
it — this command hands the claim to fresh skeptics whose job is to *refute* it.

**Input:** `$ARGUMENTS` is the claim to test (a bug description, an audit
finding, a proposed fix, a "this is safe to delete" assertion, etc.). If empty,
verify the most recent substantive finding in the current conversation.

## How to run it

Spawn **three independent skeptic subagents in parallel** (all Agent calls in a
single message). Give each the SAME claim but a DIFFERENT lens. Each skeptic is
instructed to *try to break the claim*, cite file:line evidence, and **default
to `refuted: true` when uncertain** — the burden of proof is on the claim, not
the skeptic.

Pick the three lenses that fit the claim. Defaults:

| If the claim is… | Lens 1 | Lens 2 | Lens 3 |
|---|---|---|---|
| a bug / audit finding | **Correctness** — is it actually true in the code? | **Reproduction** — does every cited file:line exist *now* and say what's claimed? | **Severity** — even if true, does it matter, or is it dead/guarded code? |
| a proposed fix / diff | **Correctness** — does it do what it claims? | **Regression** — what existing behavior or caller does it break? | **Security/side-effects** — auth, IDOR, commit/rollback, hidden coupling? |
| a "safe to delete / unused" | **Reachability** — prove something still references it | **Dynamic use** — string/registry/reflection callers a grep misses | **Test/CI coverage** — does removing it break a guard or eval? |

Each skeptic returns: `refuted` (bool), `confidence` (0–1), and a one-paragraph
`reason` with concrete evidence (file:line, not vibes).

## Verdict

- **≥2 of 3 refute** → the claim does NOT survive. Report it as suspect/killed,
  with the refuting evidence. Do not act on it without addressing the refutations.
- **0–1 refute** → the claim survives. Proceed, but surface any caveats the
  lone skeptic raised.

Always report the three verdicts honestly, even when they disagree — a split
vote is signal, not noise. Never soften a refutation to make the original claim
look better; the point is to catch plausible-but-wrong results before they cost
a session.

> For a large batch of findings (a full audit sweep), prefer the `Workflow`
> tool's pipeline pattern (review → verify-each) over running this command N
> times. This command is for verifying one claim, or a small handful, inline.
