# Area Audit: <Area Name>

Date: 2026-05-21  
Agent: <Cursor agent/session name if available>  
Scope: <files, routes, screens, hooks, docs inspected>  
Mode: Audit only. No product-code changes unless explicitly noted.

## Executive Summary

- Dogfood risk: <Low / Medium / High / Blocked>
- Highest-risk finding: <one sentence>
- Checks run: `<command>` -> <pass/fail/not run>
- Residual uncertainty: <what was not verified>

## Findings

### P0 — <Title>

Status: <Confirmed / Suspected / Needs repro>  
User impact: <what a dogfood tester would experience>  
Product promise affected: <privacy / invite loop / concierge trust / plan coherence / deployment / etc.>

References:

- `path/to/file.ext:123` — <what this line does>
- `path/to/file.ext:456` — <what this line does>

Why it matters:

<Short explanation grounded in the dogfood journey.>

Repro or deterministic test idea:

1. <step>
2. <step>
3. Expected: <expected>
4. Current likely/observed: <actual>

Suggested fix direction:

<Conservative fix direction. Do not over-prescribe implementation if uncertain.>

Related bug class:

<auth/rate-limit gap, mock-real drift, private-data leak, async DB in event loop, sibling inconsistency, etc.>

Confidence: <High / Medium / Low>

## Non-Findings / Things Ruled Out

- <Useful negative result with files inspected.>

## Suggested Follow-Up Checks

- <Small deterministic test, lint, grep, or command that would prevent recurrence.>

