---
doc_type: working
status: active
owner: founder / product / engineering
created: 2026-08-23
last_verified: 2026-08-23
expires: 2026-09-22
why_new: Records the executable M4 attention loop plus the graph/Lived and typed-destination convergence boundary before notification and physical-device delivery certification.
supersedes: []
promotes_to: null
source_of_truth_for: [m4-opening-attention-loop]
---

# M4 Opening, delivery, and deliberate silence

## Closure boundary

This receipt closes the first M4 product loop, not the entire attention and
notification program. It makes the existing owner-scoped Opening authority
legible and actionable on the same Home/Places graph summary:

1. A viewer receives an active Opening with a source-bound subject and reason.
2. The viewer can inspect **Why this** without leaving the owning surface.
3. The viewer can choose **Open this**, **Not now**, or **Dismiss**.
4. Each choice uses the existing Opening status command, idempotency key, and
   action receipt; it never creates a Commitment, Occasion, Trip, or memory.
5. A mock read-after-write projection removes a silenced Opening from current
   attention without fabricating a notification delivery.

The product unit is therefore attention control, not push volume. Silence is a
successful outcome when the Opening has not earned another interruption.

## Canonical contract and destination convergence

The second M4 increment closes the vocabulary seam without creating another
durable writer:

- `backend/lived_experience/opening_contract.py` adapts a graph
  `OpeningCandidate` into the canonical `OpeningRequest` and a viewer-safe
  `CanonicalOpening` projection. It preserves graph ownership, derives a
  deterministic expiry for legacy nullable rows, marks stale/expired rows
  non-current, and exposes only controls the source can actually honor.
- The same projection wrapper accepts a Lived `OpeningRequest`, so graph and
  Lived producers share lifecycle/action vocabulary while their authorities
  remain distinct until a later migration can safely converge them.
- `backend/notifications/destination_contract.py` and the public feed schema
  now name `opening`, `occasion_invitation`, `decision`, `handoff`,
  `commitment`, and `receipt` destinations explicitly. The mobile mapper routes
  those typed identities to an owning projection or a deliberately safe
  fallback; it does not reconstruct a destination from copy or intent.
- No graph Opening is silently promoted to a Commitment, notification
  delivery, or domain completion. Existing action receipts remain the write
  boundary.

## Existing authority reused

- Backend `OpeningCandidate` remains the owner-scoped Opening authority.
- `/api/experience-graph/openings/{opening_id}/status` remains the mutation
  boundary for accepted, silenced, and dismissed responses.
- Opening expiry and action receipts remain server-owned; mobile supplies only
  the selected status and a fresh idempotency key.
- The Home and Places graph summary already consume the viewer-relative graph
  projection, so no second attention table or surface-specific opening writer
  was introduced.

## Mobile implementation

- `ExperienceGraphSurfaceSummary` now retains the Opening status so terminal or
  already-responded candidates do not expose an actionable control.
- `ExperienceGraphSummaryCard` mounts the response sheet and source-bound
  explanation for candidate/shown Openings.
- Mock graph state now persists the M4 opening and reads back status changes.
- `guide://dev/screenshot-mode?...&m4Demo=1` seeds the QA-only opening without
  changing production defaults.
- `.maestro/m4/attention-loop.yaml` covers receive → inspect → quiet and
  asserts the Opening disappears from the current projection after silence.

## Evidence

- Backend Opening/graph route, projection, and migration suite: **57 passed**.
- Mobile Opening summary, projection, and mock read-after-write suites:
  **3 suites / 16 tests passed**.
- Mobile TypeScript typecheck and targeted ESLint: **passed**.
- M4 Maestro YAML metadata and structure: **passed**.
- Canonical graph/Lived Opening adapter and typed destination regression suites,
  together with the notification Activity/graph/relationship regression set:
  **102 backend tests passed**.
- Mobile typed-destination routing and the focused M3/M4 regression set:
  **7 suites / 86 tests passed**; generated API types and TypeScript typecheck:
  **passed**.

## Explicit release boundary

The foreground loop and vocabulary convergence are implemented, but M4 is not
a push or OS-delivery launch. The following remain deliberately open:

- one persisted Opening authority across graph, Lived workflow, and the
  notification/Activity attention case; the current adapter is intentionally
  read-only and prevents parallel writers;
- modify/snooze/mute/release across every Opening surface; Activity already
  owns snooze/resume/dismiss for notification projections, while the graph
  foreground loop currently owns accept/silence/dismiss;
- stale-payload resolution for every new typed destination and destination
  owner, beyond the current safe mobile fallbacks;
- exposure, delivery, and owner-readback telemetry bound to one receipt; and
- physical iOS/Android presentation, lock-screen privacy, interruption-level,
  Doze/Focus, accessibility, and live delivery evidence.

Keep learned arbitration and the serving notification flag at their existing
defaults until those gates are certified. This M4 slice proves control over a
foreground Opening; it does not claim that a real push was delivered.
