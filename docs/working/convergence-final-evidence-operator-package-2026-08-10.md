---
doc_type: working
status: active
owner: engineering / product / privacy / evidence
created: 2026-08-10
last_verified: 2026-08-10
expires: 2026-09-09
why_new: Collects the remaining human, provider, controlled-device, physical-device, and build work in one fail-closed operator package after the Lisbon source and deployed-support work landed.
source_of_truth_for:
  - convergence-final-external-evidence-round-2026-08
related:
  - convergence-and-ai-decision-next-execution-plan-2026-08-10.md
  - convergence-ai-next-round-candidate-2026-08-10.json
  - lisbon-group-trip-staging-device-runbook-2026-08-10.md
  - ../journeys/EVIDENCE_MODEL.md
  - ../journeys/product-proofs.yaml
---

# Convergence final evidence operator package

## Decision and evidence boundary

The remaining work is no longer one undifferentiated engineering phase. It is
five independent gates. A pass in one gate must not promote another.

| Gate | Current result | What closes it |
| --- | --- | --- |
| Lisbon backend support | **support observed** | Canonical proposal apply and inverse-revert ran on the controlled two-member staging Trip. This is not live-provider, device, P05, or P07 evidence. |
| Controlled device | **doorway support observed** | Full two-account proposal, projection, private outcome, correction, and revert assertions on a clean pinned revision. |
| AI provider comparison | **observed; iterate** | The bounded A-layer run completed 16/16 cases with 8 acceptable and two hard-gate failures. It does not authorize shadow promotion. |
| Human anchors | **waived; absent** | The owner skipped review. No H evidence or calibration exists, so shadow promotion remains blocked. |
| Shadow telemetry retention | **source complete; not deployed** | Deploy backend `bb3a645bd`, then observe the scheduled 14-day raw-receipt sweep before runtime shadow can be considered. |
| Physical proof / new iOS build | **blocked** | Two provisioned physical devices and identities, then an exact-SHA build after EAS capacity is available. |

P05 and P07 remain dark. AI shadow remains off. No source, database, staging
support, simulator, or document result is physical evidence.

## Owner decisions recorded 2026-08-10

- **Telemetry:** approved as proposed: content-free metadata for 14 days and
  aggregates for 90 days, with no prompt, response, private rationale, tool
  arguments, or user-visible copy retained.
- **Provider comparison:** approved for Anthropic
  `claude-sonnet-4-6`, the backend registry's
  `concierge_conversation` model, with a hard USD 2 total ceiling.
- **Human anchors:** skipped because no reviewers are available. An AI judgment
  does not substitute for independent human review. The program therefore has
  no H evidence, the readiness decision remains `iterate`, and runtime shadow
  promotion remains blocked.
- **EAS:** wait for the quota reset rather than buying capacity now.
- **Physical:** no second iPhone is available. Two-device P05/P07 evidence
  remains blocked even after the build quota resets.

These decisions permitted the bounded synthetic model comparison. They do not
enable runtime shadow or change any journey/device claim.

## Completed controlled Lisbon support

The isolated Trip is `f47e582d-85a6-454e-8a2d-be3a199f0b09`, with organizer
`31ccbc41-123c-4fb3-b433-7be7f10f9bb2` and participant
`407332ba-42fa-49e3-bb02-85a331ecd14d`. The source block is
`660002d9-3f0d-5aab-947b-93344bef6adf`; the alternative is venue `8213`.

Backend `1abb5a951800c8aa853ee1c427508d209eba34e2` was deployed as Fly image
`deployment-01KZPAM17J5TZJVBQC9Z8R54YQ`, digest
`sha256:102646659b6ac835e7e60678bbc1d479041cc63b8b4247d109467e0ad8b5dbbf`,
at migration `receiptidem01`. A deliberately synthetic rain observation used
the production privacy validator and canonical weather-proposal writer. The
participant voted, the organizer applied, both viewers projected the changed
Plan, and canonical inverse proposal `c2414f6c-b2a5-430e-9377-2d3d49f37cc3`
restored the original site. Read-only verification reports `withdrawn`,
`apply_status=succeeded`, and `revert_mode=canonical_inverse`.

The global weather-rescue flag was turned off immediately afterward. Runtime
resolution is false for both the controlled Trip and the older shared Trip;
the allowlist contains only the controlled Trip. Because the observation was
synthetic and the source block had already passed, this is explicitly
`staging_support_not_live_provider_or_device`.

The local iPhone 16 Pro simulator support flow passed with internal-build and
Group Trip flags enabled. Its immutable artifact is
`/Users/feihuyan/.maestro/tests/2026-08-10_132226`; flow SHA-256 is
`b9b6e2413b5e71fa79c700005fd47e71c733d7e68b2fd9e3c8808ec65364ed93`.
It proves only the production Plan doorway and private review-first handoff.
The receipt writer refused a pass receipt because the backend checkout had
concurrent staged changes; retain the artifact as support, not immutable proof.

## Human-anchor round

The frozen source is
`travel-agent/eval/ai_decision_learning/artifacts/private_grounded_disruption/v1/`.
It has 16 synthetic cases and zero human anchors. Do not edit the corpus or
protocol after reviewers see candidate outputs; any content change requires a
new corpus version.

Copy `ai-dl-human-anchor-review-template-v1.json` once per reviewer and keep the
completed copies outside the shared repo until adjudication. The checked-in
blank template is not H evidence.

1. Assign reviewer IDs outside the repo. Reviewers must work independently.
2. Give each reviewer the frozen corpus and protocol, but not the other
   reviewer's labels or a preferred model answer.
3. For every case, record all acceptable bounded actions plus correctness,
   privacy, usefulness, friction, and trust. Private free text is prohibited.
4. Hash both completed packets. Only then compare disagreements.
5. A third person adjudicates disagreements and records a bounded resolution
   reason code. Preserve both original labels.
6. Create a new adjudicated artifact version; never mutate v1 into apparent H
   evidence. Calibration and readiness are recomputed against the new version.

Validate the two completed copies with:

```bash
python3 scripts/check_ai_dl_human_reviews.py \
  --corpus travel-agent/eval/ai_decision_learning/artifacts/private_grounded_disruption/v1/corpus.json \
  --review /secure/path/reviewer-a.json \
  --review /secure/path/reviewer-b.json \
  --adjudication /secure/path/adjudication.json
```

Omit `--adjudication` on the first comparison. The command exits 2 and lists
the exact disagreement case IDs when adjudication is required. It rejects
incomplete packets, duplicate reviewers, prose reason fields, unbound
adjudication, and a reviewer acting as adjudicator.

Required owner input: two reviewer IDs and one adjudicator ID. The source
protocol requires at least two independent reviewers.

## Provider/model comparison round

The selected model was Anthropic `claude-sonnet-4-6`, matching the backend's
`concierge_conversation` registry role. The bounded runner used the sealed Fly
credential without retrieving or displaying it. Its no-cost preflight bound all
16 cases and reported a retry-inclusive worst-case cost below the USD 2 ceiling.

Approve these controls before implementing or running the adapter:

- one provider and one exact model revision;
- maximum 16 cases, one attempt per case, no retries;
- maximum 1,500 input tokens and 120 output tokens per case;
- hard total ceiling of USD 2.00 and per-call timeout of 10 seconds;
- JSON/typed `DecisionAction` output only;
- never retain free-form output, prompts, private prose, or reasoning;
- retain case ID, action kind, validation result, reason code, latency, token
  counts, estimated cost, policy/model versions, and hashes only;
- provider errors remain `unavailable`/`invalid`, never abstentions;
- no runtime shadow, mutation, notification, group output, or memory write.

The comparison report must keep acceptable rate, hard-gate failures, category
errors, abstentions, invalid/unavailable counts, latency, cost, and human
disagreements separate. A model judge cannot override privacy, authority,
freshness, scope, mutation, or receipt gates.

The first run cost USD 0.089409 but was discarded because the model placed prose
in `reason_code`, violating the approved retention boundary. The runner was
hardened to a closed reason-code vocabulary and the remote temporary package
was removed. The retained run cost USD 0.089499; total program spend was USD
0.178908.

Run from the backend checkout after setting `ANTHROPIC_API_KEY` in the process
environment (never in a command, artifact, or commit):

```bash
cd /Users/feihuyan/travel-workspace/travel-agent
PYTHONPATH=. .venv/bin/python scripts/run_ai_dl_provider_comparison.py \
  --run-live \
  --corpus eval/ai_decision_learning/artifacts/private_grounded_disruption/v1/corpus.json \
  --output eval/ai_decision_learning/artifacts/private_grounded_disruption/provider-run-2026-08-10.json
```

The runner disables Langfuse content export and VCR recording, forces a typed
tool action, records only content-free observations, refuses model/corpus drift,
and refuses to overwrite an existing artifact. The retained A-layer result is:

- 16/16 observed, zero invalid or unavailable;
- 8/16 acceptable;
- two hard-gate failures, both `evidence_scope_mismatch`;
- mean latency 2,299 ms;
- seven abstentions;
- readiness recommendation `iterate`.

This matches the deterministic baseline's 8/16 acceptable count, improves its
four hard-gate failures to two, and trails the local structured reference's
16/16 mock result. Human calibration was waived, so this is not promotion
authority. The immutable content-free artifact is
`travel-agent/eval/ai_decision_learning/artifacts/private_grounded_disruption/provider-run-2026-08-10.json`.

## Telemetry-retention decision and enforcement

Recommended initial policy for the private, content-free shadow only:

- collect no prompt, response, tool arguments, private evidence value, private
  rationale, or user-visible copy;
- retain per-observation metadata for 14 days and aggregates for 90 days;
- identifiers are keyed hashes scoped to the study, not reusable account IDs;
- access is limited to named engineering/evidence reviewers;
- deletion is automated and auditable; export and ad-hoc joins are disabled;
- kill switches and trip allowlists remain independent of telemetry approval;
- any schema expansion requires product/privacy review and a new policy version.

Approval authorizes observation only. It does not authorize a provider call,
visible output, a canary, a mutation, notification delivery, group behavior, or
durable inferred learning.

The owner approved this policy on 2026-08-10. Backend
`bb3a645bdcbd3d7a21ab01a144723d5daa0b5976` now enforces the raw-receipt side
in source: a nightly 03:35 UTC worker and the manual privacy purge delete only
`proactive_events` rows whose event type is `ai_decision_shadow` and trigger
source is `ai_decision_learning` after 14 days. The selector requires both
markers so it cannot erase unrelated proactive history. The sweep emits only
aggregate count and window telemetry.

There is no materialized shadow aggregate store today, so there is nothing to
age out at 90 days. The 90-day aggregate limit remains a ceiling for any future
aggregate schema or external sink configuration. Source completion is not
deployment evidence: runtime shadow stays off until this backend revision is
deployed and one scheduled sweep is observed.

## Full controlled-device and physical walks

The existing doorway flow cannot be stretched into P05/P07. A qualifying walk
must assert, with two identities:

1. organizer opens the fixed future Lisbon block and starts private review;
2. participant joins through real invite redemption and sees the same proposal;
3. participant votes and organizer accepts through canonical controls;
4. both observers converge on the same Plan, Map, Now, and proposal revision;
5. reject and expiry preserve the original; inverse revert restores it;
6. both people privately confirm outcomes; neither private verdict/rationale is
   group-visible;
7. correction changes only the correcting person's artifact;
8. changed-roster applicability withholds companion-fit reuse.

Controlled-device evidence uses a controlled backend and may use a simulator,
but must bind clean workspace/backend/app SHAs, build/deploy/migration/fixture,
flow and oracle hashes, identities, and fresh artifacts. Physical evidence adds
two unique hardware UDIDs and cannot be created by the current J04/J05/J10
runner until a governed P05/P07 flow set exists. Do not relabel its receipts.

## EAS and physical-device handoff

The existing dogfood host binary is EAS build
`aa524cdb-7b34-4f27-9864-425df19a2e47` with exact app OTA group
`a8ae572d-f59c-481c-b768-3359ecbc35b6`. It provisions only physical UDID
`00008140-001210CE2013C01C`, so it cannot support the required two-device walk.

After EAS iOS capacity resets or a paid build is authorized:

```bash
cd /Users/feihuyan/travel-workspace/travel-app
eas device:list --platform ios
eas build --platform ios --profile dogfood --non-interactive
eas update --platform ios --channel dogfood --message "Pin Lisbon P05/P07 evidence candidate"
```

Before building, register both physical UDIDs and confirm the build profile has
`EXPO_PUBLIC_IS_INTERNAL_BUILD=true` and
`EXPO_PUBLIC_GROUP_TRIP_MICRO_JOURNEY_ENABLED=true`. Record the build ID and
update group; do not reuse the old binary if provisioning or native dependencies
differ. Human OTP entry remains an operator action.

## Promotion sequence

1. Commit a clean, pinned candidate manifest.
2. Run a future-block, live-provider staging scenario without fabricating risk.
3. Run the complete controlled two-account device flow and record P05/P07 only
   for the assertions actually covered.
4. Build for two provisioned devices and run fresh physical assertions.
5. Deploy the retention source revision and observe one scheduled sweep.
6. Keep human calibration explicitly absent and the provider result at
   `iterate`; neither is a promotion pass.
7. Make separate decisions for Group Trip, shadow observation, the local second
   occasion, and any future private canary.

The remaining external actions are to wait for EAS capacity, obtain a second
physical iPhone and identity if P05/P07 physical proof is still required, and
provide a real future-block provider disruption. Human calibration remains
waived by owner decision. Engineering can deploy and observe the retention
sweep without weakening the evidence boundary, but cannot promote shadow from
the current `iterate` result.
