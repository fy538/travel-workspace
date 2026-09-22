---
doc_type: working
status: active
owner: strategy integration
created: 2026-09-05
last_verified: 2026-09-22
expires: 2026-10-21
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

The renderer registry and server-kind coverage were rechecked by code
inspection on 2026-09-22 against the current isolated candidate: workspace
`0f182e6`, backend `5e6f1d174`, and app `93a9090de`. The backend child advance
is verification-only for the R02 release matrix; the app child advance retains
the supported private-audio reader. This refresh did not rerun the suites
listed below and does not promote either child to main or production.

## Current promotion boundary

The Home transport union contains 36 semantic kinds. Four kinds were admitted
by the September 5 composition-canon amendment because they are legitimate
product forms, not because their supply is complete. Three now have explicit
native renderers; one remains dark. Production and source admission are separate
questions in either case:

- `horizon_prepared_alternatives`
- `horizon_world_fact_row`
- `people_authored_region`
- `now_sample_demonstration`

### Home

The three chrome kinds are rendered by dedicated Home components:

- `world_read`
- `root_shell`
- `week_shape`

The explicit native unit registry promotes 18 semantic kinds:

- `now_commitment_instrument`, `now_recovery_instrument`,
  `now_prepared_possibility`, `now_invitation`, `now_sample_demonstration`,
  `people_original_delivery`
- `motion_occasion_row`, `motion_loose_end_row`, `motion_all_plans_door`
- `horizon_editorial_passage`, `horizon_mechanism_row`,
  `horizon_aperture_row`, `horizon_prepared_alternatives`
- `people_note_door`, `people_authored_region`
- `continuity_capability_field`, `continuity_since_you_looked`,
  `continuity_life_door`

The backend currently defines these 15 Home semantic kinds without an explicit
native renderer: `now_decision`, `now_temporal_posture`,
`now_annotated_evidence`, `now_attributed_comparison`, `now_merged_into_read`,
`horizon_hidden_system`, `horizon_world_fact_row`, `people_participants_row`,
`people_waiting_row`, `people_authorized_door`, `people_gathering`,
`people_status_aperture`,
`continuity_settling`, `continuity_voice_horizon`, and
`continuity_reconstruction`. Of the four canon-admitted forms, only
`horizon_world_fact_row` remains dark. A registered renderer does not prove a
producer, source admission, useful supply, or permission to emit the kind to
foreground Home. Keep renderer coverage distinct from product coverage.

### Places

The current semantic Places renderer promotes twelve kinds:

- `scope_handle`, `search_map_affordance`
- `field_lead_composition`, `field_branch`, `field_returned_understanding`,
  `field_continuity_doors`, `field_balanced_fallback`, `field_browse_shelf`,
  `field_editorial_cover`
- `path_evidence_apparatus`, `social_attributed_evidence`,
  `social_plural_comparison`

The backend also defines Focus, Path, Live, and additional social kinds. They
remain available to the transport contract but are not yet a native Places v2
promotion. Places v2 is still an internal inspection renderer while the mature
Places workspace remains canonical; promotion must preserve the map/field,
Focus, Path, current-condition, handoff, and `From friends` contracts as one
experience rather than create a second feed.

## Evidence already present

- The current code registry contains 18 Home semantic kinds and the current
  Places registry contains twelve; this refresh verified those source lists,
  not their live production frequency. The transport union remains broader by
  design, including reserved/deferred values that do not currently have an
  owner-backed producer and should not be treated as missing renderers.
- The 12-test Home renderer suite and app TypeScript check passed at app
  `6ae89c427`; app `93a9090de` retains that renderer boundary while adding the
  supported private-audio reader. The current refresh did not rerun these
  checks or capture a screenshot.
- The earlier audit recorded 43 focused Home and 27 focused Places tests on
  its then-current tuple. Those historical counts are not a full experience or
  native acceptance claim for the current candidate.
- Backend OpenAPI, the committed app projection, and generated mobile types
  have a 36-kind Home transport union; this is a contract receipt only, not a
  renderer-promotion or source-admission receipt.
- `utils/rootProjectionV2Conformance.ts` deliberately treats an unregistered
  Home kind as a contract error, and the Places screen filters through its
  explicit registry.

These are deterministic/native conformance receipts only. They do not certify
editorial novelty, real-data coverage, current-world feasibility, or final
visual design.

The current implementation is therefore **renderer-complete for the promoted
Home/Places kinds, but not experience-complete**. Home already reads ten
bounded owner families, accepts a current prepared private Source contribution
without generating during ordinary reads, and selects through its current
posture/region system. The current roadmap's next package is broader,
design-aligned Home composition using supported owners—not another renderer or
generation service. The Home/Places scrolls and named destination/return paths
remain scoped receipts, not proof of recurring content breadth or final visual
parity.

## Next promotion rule

Promote a new kind only when all four pieces are present in one bounded change:

1. a backend candidate producer with owner/evidence/revision and a real value
   reason;
2. an explicit native renderer and accessibility/interaction behavior;
3. an envelope/conformance and fallback test covering unknown, unavailable,
   stale, revoked, and exact-return states; and
4. product review showing that the kind adds value rather than a new section,
   input demand, or duplicate interpretation.

Until then, keep the kind source-dark and let Home/Places deliver value through
the already-promoted families. Do not solve schema breadth by adding a renderer
that merely prints the semantic kind name. The immediate execution item is the
Home composition package in the [program roadmap](vesper-program-roadmap.md):
map current design sections to owner-backed candidates and renderers, then
compose the genuinely useful coverage gaps into a coherent scroll with exact
destinations/return and sparse/pending/failure handling. Reconsider a new
semantic kind only if an intended user outcome cannot truthfully fit an
existing one; never manufacture design parity from fixtures.
