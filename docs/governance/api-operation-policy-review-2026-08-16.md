---
doc_type: current_status
status: active
owner: product-engineering
created: 2026-08-16
last_verified: 2026-08-16
why_new: Records the specific evidence used to resolve the expired API operation policy window; the policy JSON cannot carry that review narrative.
source_of_truth_for:
  - api-operation-policy-review-2026-08-16
---

# API operation policy review — 2026-08-16

The mobile OpenAPI projector correctly stopped on 2026-08-16 because 53
`retiring` entries had reached their 2026-08-15 review date. This was a policy
deadline, not evidence that any of those routes should be silently exposed.

## Review method

We compared every expired route against the current mobile transport and
product-call discovery using `scripts/api_contract_audit.py`'s
`discover_mobile_consumers` implementation. The review found:

- 3 routes have real product callers and are restored to `active` with their
  exact hook as the declared consumer: conversation invite list, create, and
  revoke.
- 50 routes have no discovered product caller. They remain `retiring`; their
  existing removal triggers remain unchanged and their next review is
  2026-09-15.

This is a control-plane correction only. It neither adds an API surface nor
changes deployment behavior. Each remaining retiring route still needs a
separate, evidence-backed remove-or-adopt decision at its next review.
