# Prompt 14 — Release, TestFlight, Deploy, And Mobile Platform

```text
You are a Cursor Cloud agent auditing Travel Workspace for dogfood readiness.

Use the common rules in:
docs/audits/dogfood-readiness-2026-05/prompts/00-common-instructions.md

Area:
Deployment, release configuration, TestFlight readiness, app store/privacy docs, mobile platform permissions.

Output:
docs/audits/dogfood-readiness-2026-05/areas/14-release-testflight-deploy-mobile.md

Product promise:
The team can produce a real TestFlight build that talks to a healthy backend with production auth, correct deep links, privacy disclosures, and rollback/smoke procedures.

Inspect:
- Workspace docs: Owner Action Items, Deploy & Rollback Runbook, Pre-Launch Deploy Surface, App Privacy Disclosures, Apple Review Notes, TestFlight onboarding.
- Travel App eas.json, app.json, release guards, runtime env checks, permissions, Sentry consent.
- Travel Agent fly.toml, Dockerfile, requirements, health/ready/external health, smoke scripts.
- Workspace Makefile release/preflight targets.

Start with:
- docs/Owner Action Items.md
- docs/Deploy & Rollback Runbook.md
- docs/Pre-Launch Deploy Surface.md
- docs/App Privacy Disclosures.md
- docs/TestFlight Tester Onboarding.md

Audit questions:
1. Does `make preflight-eas` pass or fail, and why?
2. Are EAS projectId, API URLs, Clerk keys, mock/skip-auth flags, and bundle IDs production-correct?
3. Are backend preview/production hosts reachable and returning `/health`?
4. Are AASA/Universal Links configured with real Apple Team/App Store IDs?
5. Are privacy disclosures aligned with implemented data collection, deletion, photos, location, push, and analytics?
6. Is rollback/smoke realistic for backend, worker, migrations, and TestFlight?
7. Are mobile permissions recoverable and not dead-end alerts?

Run:
- make doctor
- make contract-check
- make preflight-eas
- curl health checks for documented preview/production hosts only

Deliver:
This report should produce an owner/action checklist with exact commands and pass criteria. Separate code tasks from account/DNS/provider tasks.
```

