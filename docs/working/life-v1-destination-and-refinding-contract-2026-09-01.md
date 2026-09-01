---
doc_type: working
status: active
owner: product / frontend / backend
created: 2026-09-01
last_verified: 2026-09-01
expires: 2026-10-01
why_new: Closes the first Life v1 destination and refinding seam without prematurely building a generalized dossier system.
depends_on:
  - ../contracts/life-v1-experience.md
  - ../../travel-app/docs/surfaces/life-root/contract.md
  - ../working/life-v1-non-regrettable-engineering-execution-plan-2026-09-01.md
---

# Life v1 destination and refinding contract

Life rows are valuable only when they reopen the record that made them
meaningful. A row is therefore a canonical object handle first and a visual
line second. This document keeps the first internal root honest while the
full dossier family is still being built.

## Destination policy

The backend emits one `ResourceRef` (`kind`, `id`, optional `revision`, and
`canonical_path`). The mobile resolver is pure and allowlisted:

| Object family | Current destination | Disposition |
| --- | --- | --- |
| Plan, Occasion, Commitment, Outcome in Life Time | `/you/history?mode=time&record=<id>` | exact Life owner path; the history route may ignore an unknown focus until its dossier is ready |
| Place-like entity (`venue`, `site`, `place`, `experience`, `accommodation`) | canonical entity reader | exact Places owner path via `routeForEntity` |
| Artifact, source, reading without a native owner | `/you/memories` | truthful source fallback; never pretends to be an exact dossier |
| Safe `guide://you/...` path | corresponding allowlisted app path | exact guide handoff |
| `transport_hub`, unknown kind, malformed path | no navigation | explicit unsupported result; caller must not render a dead-end affordance |

The resolver never concatenates arbitrary server strings, pushes API paths, or
falls through to legacy Atlas by accident. Revision remains attached to the
original handle for readback and stale-state checks even when the current
destination is a fallback.

## Life root behavior

- The internal Life v1 root renders only entries with a supported or truthful
  fallback destination.
- The complete-record door opens the canonical time history, not a second
  archive implementation.
- A Return uses the same resolver as a row; it cannot invent a special route.
- Unsupported content remains visible only in an owner surface that can explain
  its limitation. No row asks the user to repair missing routing by entering
  data.

## Refinding requirements before promotion

The current history path is a safe owner landing, not the final dossier. Before
public Life promotion, each benchmark object needs a destination that can show:

1. canonical identity and its containing episode/occasion;
2. plan-versus-occurrence truth and source claims;
3. current authority, grants, withdrawal, and correction state;
4. a context-preserving Chat continuation door; and
5. a return path that restores the prior Life scroll position.

Until those conditions are met, the Life flag stays internal and the resolver's
`source_fallback` / `unsupported` dispositions remain part of the contract.
