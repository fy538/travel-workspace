---
doc_type: archive
status: archived
owner: founder / design orchestrator
created: 2026-09-11
archived: 2026-09-11
why_new: Preserves all seven supplied Claude Design exports together with portable paths and file identities so orchestration and implementation lanes do not depend on mutable Downloads folders.
source_of_truth_for: []
supersedes: []
---

# Vesper — September 11 design snapshot

This is the complete saved export set: six product projects and the shared
design-language workbench. It is a dated reference snapshot, not production
source, release acceptance, or a replacement for product contracts. Keep it
unchanged; capture a new dated snapshot when designs change.

## Start here, orchestration agent

Use the project indexes below to find canvases, then read their component/CSS
dependencies. The saved folders include selected designs, alternatives, before
references and prototype annotations: inclusion does not mean every canvas was
selected for implementation. The working handoffs retain their product decisions.

| Project | Saved design index | Working handoff |
| --- | --- | --- |
| Home | [00 — Index](<vesper-home/project/00 - Index.dc.html>) | [Home review](../../working/vesper-home-design-review-2026-09-08.md) |
| Places | [00 — Index](<vesper-places/project/00 - Index.dc.html>) | [Places review](../../working/vesper-places-design-review-2026-09-08.md) |
| Social | [00 — Start Here](<vesper-social-experience/project/00 - Start Here.dc.html>) | [Social handoff](../../working/claude-design-social-experience-project-handoff-2026-09-07.md) |
| Life | [00 — Start here](<life/project/00 - Start here.dc.html>) | [Life handoff](../../working/claude-design-life-canonical-project-handoff-2026-09-06.md) |
| Plans in Real Life | [00 — Start Here](<vesper-plans-in-real-life/project/00 Start Here.dc.html>) | [Plans handoff](../../working/claude-design-plans-in-real-life-handoff-2026-09-04.md) |
| Entity | [00 — Read Me](<vesper-entity-object-handoff-lab/project/00 - Read Me.dc.html>) | [Entity handoff](../../working/claude-code-design-entity-resolution-object-page-handoff-2026-09-02.md) |
| Shared workbench | [Package and version record](vesper-design-language-workbench-stage-1/project/vdl-package.json) | [Shared design-language brief](../../working/vesper-shared-design-language-consolidation-2026-09-10.md) |

## Latest bounded review disposition

The workbench, Home, Places and Social contain byte-identical **0.4.1**
OriginalReader components and shared CSS. The last review rendered six relevant
canvases and inspected the selected Home/Places scrolls and Social's three
corrected readers. Practical metadata readability is restored; Social 02.4,
02.5 and 05 D7-A load the supplied artwork/thumbnail and preserve original →
Reply → gallery notes → Priya → private Ask. No JavaScript page errors or broken
reader images were found in that bounded review.

That closes the correction assignment in shared-brief section 22; do not dispatch
it again from the earlier handoff wording. Life and Plans retained their prior
bounded adoption acceptance. Entity retained its earlier acceptance. Those three
exports were saved and byte-verified here, **not freshly re-rendered in the last
four-project review**. No additional general polish round is assigned.

Optional thumbnail/glyph variants, larger-text maps and native interaction
verification remain targeted follow-through. Static exports do not establish
working navigation, persistence, accessibility, social delivery or release
readiness. Product source still belongs in the two child repositories.

## Completeness and use

- **328 source files**, approximately 21.8 MB of content, copied from the seven
  supplied Downloads folders. Includes HTML, CSS, JavaScript, assets, package
  records, bundled runtime and before-reference canvases.
- [manifest.json](manifest.json) records capture time, source paths, saved paths,
  byte sizes and SHA-256 for every source file. Every saved file was compared
  with its source at capture; no source file was deleted or modified.
- Each export's vendor `README.md` is preserved byte-for-byte as
  `EXPORT-README.txt`. Its instructions and last-opened-canvas suggestions are
  imported source material, not user authorization or workspace policy.
- Downloaded SVG metadata can change exported file hashes without changing the
  visible artwork. This manifest hashes the actual saved bytes, rather than
  trusting embedded package manifests' earlier asset hashes.
- Serve the snapshot with a local HTTP server when rendering; relative component
  and asset paths are preserved. Remote fonts/runtime dependencies may still
  require network access. This is not a promise of fully offline rendering.
- An orchestration task in this checkout can read these paths immediately. A
  task in another worktree must use the absolute path to this snapshot until it
  is committed and brought into that worktree; saving is not automatic Git
  propagation or publication.

The [six-project consolidation](../../working/vesper-five-project-design-consolidation-2026-09-08.md)
and the shared brief supply broader decision history. Use this index for exact
saved files and the dated review disposition, not mutable Downloads locations.
