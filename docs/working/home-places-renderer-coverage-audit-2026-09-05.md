---
doc_type: working
status: active
owner: strategy integration
created: 2026-09-05
last_verified: 2026-09-05
expires: 2026-10-05
why_new: Names the actual Home and Places semantic-to-native promotion boundary before more design or server kinds are enabled.
source_of_truth_for:
  - I4 semantic kind and native renderer coverage
depends_on:
  - complete-system-integration-roadmap-2026-09-05.md
  - ../decisions/2026-09-05-amend-home-composition-canon.md
---

# Home / Places renderer coverage audit

The backend contract is intentionally broader than the current native
promotion set. The generated TypeScript union is a transport vocabulary, not a
promise that every kind is renderable. The client must continue to reject an
unknown or unpromoted kind rather than route it through a generic card.

## Current promotion boundary

The Home transport union now contains 35 semantic kinds. Four kinds were
admitted by the September 5 composition-canon amendment because they are
legitimate product forms, not because their production or native rendering is
complete. They are explicitly dark at this boundary:

- `horizon_prepared_alternatives`
- `horizon_world_fact_row`
- `people_authored_region`
- `now_sample_demonstration`

### Home

The three chrome kinds are rendered by dedicated Home components:

- `world_read`
- `root_shell`
- `week_shape`

The explicit native unit registry promotes 13 additional kinds:

- `now_commitment_instrument`, `now_recovery_instrument`,
  `now_prepared_possibility`, `now_invitation`
- `motion_occasion_row`, `motion_loose_end_row`, `motion_all_plans_door`
- `horizon_editorial_passage`, `horizon_aperture_row`
- `people_note_door`
- `continuity_capability_field`, `continuity_since_you_looked`,
  `continuity_life_door`

The backend currently defines additional Home semantic kinds that remain dark:
`now_decision`, `now_temporal_posture`, `now_annotated_evidence`,
`now_attributed_comparison`, `now_merged_into_read`, `horizon_mechanism_row`,
`horizon_hidden_system`, `people_participants_row`, `people_waiting_row`,
`people_authorized_door`, `people_gathering`, `people_status_aperture`,
`continuity_settling`, `continuity_voice_horizon`, and
`continuity_reconstruction`. Alongside those historical dark kinds, the four
canon-admitted forms above require a producer, evidence/revision contract,
and deliberate native review. Their presence in the schema does not authorize
server emission to the foreground Home path.

### Places

The current semantic Places renderer promotes ten kinds:

- `scope_handle`, `search_map_affordance`
- `field_lead_composition`, `field_branch`, `field_returned_understanding`,
  `field_continuity_doors`, `field_balanced_fallback`, `field_browse_shelf`,
  `field_editorial_cover`
- `social_attributed_evidence`

The backend also defines Focus, Path, Live, and additional social kinds. They
remain available to the transport contract but are not yet a native Places v2
promotion. Places v2 is still an internal inspection renderer while the mature
Places workspace remains canonical; promotion must preserve the map/field,
Focus, Path, current-condition, handoff, and `From friends` contracts as one
experience rather than create a second feed.

## Evidence already present

- Home renderer and Home experience suites pass: 21 tests.
- Places v2 screen and Places root experience suites pass: 9 tests.
- App TypeScript check passes on the current checkout.
- Backend OpenAPI, the committed app projection, and generated mobile types
  agree on the 35-kind Home transport union; this is a contract receipt only,
  not a renderer-promotion receipt.
- `utils/rootProjectionV2Conformance.ts` deliberately treats an unregistered
  Home kind as a contract error, and the Places screen filters through its
  explicit registry.

These are deterministic/native conformance receipts only. They do not certify
editorial novelty, real-data coverage, current-world feasibility, or final
visual design.

## Next promotion rule

Promote a new kind only when all four pieces are present in one bounded change:

1. a backend candidate producer with owner/evidence/revision and a real value
   reason;
2. an explicit native renderer and accessibility/interaction behavior;
3. an envelope/conformance and fallback test covering unknown, unavailable,
   stale, revoked, and exact-return states; and
4. product review showing that the kind adds value rather than a new section,
   input demand, or duplicate interpretation.

Until then, keep the kind dark and let Home/Places deliver value through the
already-promoted families. Do not solve schema breadth by adding a renderer
that merely prints the semantic kind name.
