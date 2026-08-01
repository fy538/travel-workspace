# Vesper Organic Pair v1

Status: approved identity study, packaged for product validation. Not yet installed as the shipping app icon.

Frozen on 2026-08-01.

## Identity

- Concept: a traveler and a place/world in a close, responsive relationship.
- Geometry: two filled organic forms. Their paths and resting relationship are frozen.
- Primary palette: paper `#EFEAE0`, ink `#1B1714`.
- Gold is excluded from the icon direction.
- Primary app-icon artwork uses the enlarged optical placement: `translate(119 135) scale(6.4)` on a 1024 square.
- The artwork is intentionally shifted slightly down and right.

## Core files

- `vesper-organic-pair-master.svg` — transparent 120-unit geometry master.
- `vesper-app-icon-primary.svg` — enlarged ink-on-paper launcher artwork.
- `vesper-app-icon-reverse.svg` — paper-on-ink alternate.
- `vesper-impact-frame.svg` — approved connected silhouette at maximum collision compression.

## Motion files

- `motion/half-turn-return.svg` — 180° clockwise, hold, 180° counterclockwise home.
- `motion/two-half-turns.svg` — 180° clockwise, hold, another 180° clockwise home.
- `motion/full-turn.svg` — one uninterrupted 360° clockwise turn.
- `motion/soft-collision.svg` — separate, clash, compress into one connected silhouette, rebound; repeated twice in the review loop.

Review SVGs repeat to make comparison convenient. Production implementations must choose an explicit trigger and repetition policy. Respect Reduce Motion by showing the resting frame immediately.

## Product guidance

- Keep the core silhouettes flat and undecorated.
- Let context carry color; do not assign an arbitrary accent to one shape.
- Use the primary icon on light/paper surfaces and the reverse mark only on intentional ink fields.
- Do not morph the master paths. Motion may translate, rotate, or temporarily scale the shapes.
- Avoid spin for decorative ambience. A full turn belongs to a bounded loading or refresh state.
- The collision is appropriate for connection, match, group formation, or a shared moment.
- Wordmark typography shown in context studies remains provisional.

## Validation boundary

The package is a tracked design artifact. It does not replace `travel-app/assets/icon.png`, splash assets, app configuration, or production UI. Product installation requires platform exports and device visual QA.
