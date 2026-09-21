---
doc_type: working
status: active
owner: strategy integration
created: 2026-09-05
last_verified: 2026-09-21
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

This audit was refreshed on 2026-09-21 against the current lane tuple:
workspace `3ba4e5e`, backend `bdc05c02f`, and app `242d309f0`.

## Current promotion boundary

The Home transport union now contains 36 semantic kinds. Four kinds were
admitted by the September 5 composition-canon amendment because they are
legitimate product forms, not because their production or native rendering is
complete. Two now have explicit native renderers; two remain dark. Production
and source admission are separate questions in either case:

- `horizon_prepared_alternatives`
- `horizon_world_fact_row`
- `people_authored_region`
- `now_sample_demonstration`

### Home

The three chrome kinds are rendered by dedicated Home components:

- `world_read`
- `root_shell`
- `week_shape`

The explicit native unit registry promotes 17 additional kinds:

- `now_commitment_instrument`, `now_recovery_instrument`,
  `now_prepared_possibility`, `now_invitation`, `people_original_delivery`
- `motion_occasion_row`, `motion_loose_end_row`, `motion_all_plans_door`
- `horizon_editorial_passage`, `horizon_mechanism_row`,
  `horizon_aperture_row`, `horizon_prepared_alternatives`
- `people_note_door`, `people_authored_region`
- `continuity_capability_field`, `continuity_since_you_looked`,
  `continuity_life_door`

The backend currently defines additional Home semantic kinds that remain dark:
`now_decision`, `now_temporal_posture`, `now_annotated_evidence`,
`now_attributed_comparison`, `now_merged_into_read`, `horizon_hidden_system`,
`people_participants_row`, `people_waiting_row`,
`people_authorized_door`, `people_gathering`, `people_status_aperture`,
`continuity_settling`, `continuity_voice_horizon`, and
`continuity_reconstruction`. The four canon-admitted forms above still require
a producer, evidence/revision contract, and deliberate native review before
they can be treated as foreground supply. Their presence in the schema does
not authorize server emission to the foreground Home path. The distinction
between a renderable kind and a source-admitted kind prevents the renderer
registry from being mistaken for a content supply guarantee.

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

- The focused Home renderer/experience packet passes **43 tests** (four
  suites), and the focused Places renderer/root packet passes **27 tests**
  (four suites), for **70 tests** total.
- App TypeScript check passes on the current checkout.
- Backend OpenAPI, the committed app projection, and generated mobile types
  agree on the 36-kind Home transport union; this is a contract receipt only,
  not a renderer-promotion receipt.
- The real-Postgres Save-owner integration reaches the governed Places runtime
  envelope after Home projection and Places owner reads; one focused integration
  test passes. The Save remains separately proven through its canonical owner and
  Home unit, while the runtime semantic admission does not yet include that
  newly saved card. This is wrapper/continuity evidence and an explicit
  admission gap, not Focus/Path recomposition or native/device evidence.
- `utils/rootProjectionV2Conformance.ts` deliberately treats an unregistered
  Home kind as a contract error, and the Places screen filters through its
  explicit registry.

These are deterministic/native conformance receipts only. They do not certify
editorial novelty, real-data coverage, current-world feasibility, or final
visual design.

The current implementation is therefore **renderer-complete for the promoted
Home/Places kinds, but not experience-complete**. The next proof must exercise
an existing owner-backed payload through canonical production composition and
return, rather than add another semantic kind or rely on an injected fixture.

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
that merely prints the semantic kind name. The immediate execution item is a
canonical Home runtime readback for an existing owner-backed sequence (with
exact source/depth/action destination, sparse/pending/failure handling, and
return behavior); if a safe supplied payload is unavailable, record that
boundary instead of manufacturing parity from fixtures.
