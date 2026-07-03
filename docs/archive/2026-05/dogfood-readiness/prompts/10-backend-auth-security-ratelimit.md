# Prompt 10 — Backend Auth, Route Security, Rate Limits, And Redaction

```text
You are a Cursor Cloud agent auditing Travel Workspace for dogfood readiness.

Use the common rules in:
docs/audits/dogfood-readiness-2026-05/prompts/00-common-instructions.md

Area:
Backend API auth, membership checks, admin/debug gates, rate limits, upload limits, secret/token redaction.

Output:
docs/audits/dogfood-readiness-2026-05/areas/10-backend-auth-security-ratelimit.md

Product promise:
Dogfood backend routes should not expose user data, LLM spend, raw tokens, debug internals, or write access without correct auth, membership, and rate limiting.

Inspect:
- Travel Agent backend/api routes, dependencies, auth utilities, route decorators.
- Debug/admin/metrics/health endpoints.
- Upload/media routes and multipart limits.
- LLM-cost routes, embedding/search routes, concierge/message routes.
- Logging/event payloads for raw token or PII leakage.
- Existing route-auth/static lint scripts.

Start with:
- Travel Agent/docs/operations/Auth Modes.md
- Travel Agent/docs/operations/Configuration.md
- Travel Agent/backend/api/FEATURE.md
- Travel Agent/scripts/check_route_auth.py if present
- Travel Agent/tests/api/

Audit questions:
1. Does every non-public route require current user/admin/curator auth or documented noauth reason?
2. Does every trip/user write route verify membership or ownership?
3. Are LLM, embedding, TTS, upload, and provider-cost routes rate-limited?
4. Are debug and metrics routes admin-gated?
5. Are raw invite tokens, JWTs, device tokens, phone/email, private text, and traces redacted?
6. Are release defaults secure when env vars are missing?
7. Are file uploads bounded by size/type/path safety?

Run if cheap:
- targeted route/security tests
- route auth/static checks if available
- make contract-check

Deliver:
Prioritize concrete exploit or dogfood-trust paths. Also list missing structural gates that would prevent recurrence.
```

