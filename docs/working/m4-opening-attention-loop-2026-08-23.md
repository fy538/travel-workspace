---
doc_type: working
status: active
owner: founder / product / engineering
created: 2026-08-23
last_verified: 2026-08-23
expires: 2026-09-22
why_new: Records the first executable M4 attention loop before notification and physical-device delivery certification.
supersedes: []
promotes_to: null
source_of_truth_for: [m4-opening-attention-loop]
---

# M4 Opening and deliberate-silence loop

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

## Explicit release boundary

The first foreground attention loop is implemented, but M4 is not a push or
OS-delivery launch. The following remain deliberately open:

- convergence between graph Openings, Lived `OpeningRequest`, and the
  notification/Activity attention case without parallel writers;
- modify/snooze/mute/release actions and richer treatment-versus-silence policy;
- typed destinations and stale-payload resolution across every notification
  family;
- exposure, delivery, and owner-readback telemetry bound to one receipt; and
- physical iOS/Android presentation, lock-screen privacy, interruption-level,
  Doze/Focus, accessibility, and live delivery evidence.

Keep learned arbitration and the serving notification flag at their existing
defaults until those gates are certified. This M4 slice proves control over a
foreground Opening; it does not claim that a real push was delivered.
