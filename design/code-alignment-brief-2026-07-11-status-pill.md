# Code Alignment Brief: Status Pill

Date: 2026-07-11

## Canon

`status-pill.jsx` defines `VStatusPill` as the shared sans status shell for Proposal Detail and Trip Settings:

- height `22`
- radius `11`
- horizontal padding `10`
- sans label, `11px`, weight `600`, letter spacing `-0.1`
- caller owns the per-surface `status -> { bg, color }` map

## API Choice

Use `components/ui/StatusPill.tsx`, not `Badge`.

`Badge` remains the broader dynamic badge primitive with variants, status shorthand, count behavior, and proportional padding. `VStatusPill` is narrower: one fixed shell canon explicitly merges across Proposal Detail and Trip Settings while leaving tone maps outside the primitive. A dedicated `StatusPill` keeps that contract small and avoids making `Badge` carry a one-off fixed-height mode.

## Implementation

Proposal Detail wraps `ui/StatusPill` with `proposalStatusTone(label)` and preserves its existing labels and colors, including the `maxWidth={128}` header clamp.

Trip Settings wraps the same shell in `TripStatusPill`, preserving its local tone map and casing. The leading dot is kept as `dot` on the shared primitive because Trip Settings had an intentional status marker; it is an optional add-on around the same h22/r11 shell, not a second pill species.

## Adjudication Leftovers

- Booking chips/tone pills and People `RolePill` stay out of this pass. Canon calls them separate species.
- Trip Settings dot is sanctioned as an optional marker prop on `StatusPill`; Proposal Detail does not use it.
- Trip Settings uppercase remains an optional prop so the shell can support that surface without changing Proposal Detail sentence-case labels.
