Verify `$ARGUMENTS` (or the most recent substantive claim) against current code
and observable behavior before acting on it.

1. State the claim, affected revision and what evidence could falsify it.
2. Inspect the cited implementation, callers and safeguards. For a proposed fix,
   inspect the failure mechanism, required behavior and likely regressions.
3. Reproduce with a bounded test/probe when practical. Check both legitimate and
   violating cases; distinguish a product failure from failed tooling or setup.
4. Return **supported**, **refuted**, or **unresolved**, with file/line or command
   evidence and its limits. Uncertainty is unresolved, not a refutation.
5. Use independent review for consequential uncertainty when authorized and
   useful. Choose the number and lenses proportionally; no mandatory three-agent
   vote. Resolve disagreements using evidence, not majority or confidence scores.

A supported local reproduction is not proof of a production incident. A passing
checker certifies only its implemented boundary and the revision it actually ran.
