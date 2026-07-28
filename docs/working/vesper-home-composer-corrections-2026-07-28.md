---
doc_type: working
status: active
owner: frontend
created: 2026-07-28
expires: 2026-08-27
why_new: Program step 3 requires four verified Vesper Home composer corrections, while ComposerBar is shared by Home, private chat, group chat, and conversation creation. This note fixes the edit boundary before changing that shared component.
promotes_to: travel-app/docs/surfaces/vesper-home/contract.md
supersedes: []
source_of_truth_for:
  - vesper-home-composer-corrections
---

# Vesper Home composer corrections

## Scope

This landing changes the **inline Vesper Home** composition only where
the shared component needs a capability switch. Private and group thread
composer geometry, keyboard ownership, and public/private routing do not
change.

## Decisions

1. **The leading mark becomes a real `+`, never a decorative target.**
   Inline mode renders the existing add control only when an image-capable
   send callback exists. Vesper Home gains that callback; a surface without
   a round-trippable add capability renders no leading control.
2. **Reuse the existing private handoff.** Home stages
   `{text, images}` through `pendingComposerTurn` and navigates with its
   small opaque key. Base64 never enters route params. The new thread
   consumes the turn only after its private conversation id exists.
   Navigation failure discards the staged payload and leaves ComposerBar's
   draft intact.
3. **The 17px field and readable placeholder are assertions, not new
   styling.** `typography.chatComposerInput` already supplies sans 17 with
   zero tracking; non-thread mode already uses `colors.surface.mute`.
   Tests pin both so later variants cannot regress them.
4. **The 64px dissolve belongs to FocusHome.** It is a pointer-transparent
   bottom scroll edge behind the pinned composer, always present. It does
   not enter ComposerBar: thread composers sit in normal layout flow so
   KeyboardAvoidingView can lift them, and already own separate transcript
   edge material.

## Proof

- Unit-test staging/consumption and navigation-failure cleanup.
- Component-test inline `+`, absence of the retired sparkle, 17px field,
  readable placeholder, and 64px pointer-transparent dissolve.
- Run typecheck and relevant Composer/Home suites.
- Capture Vesper Home on an iOS simulator before recording program step 3.

## Landed

Completed 2026-07-28 in app `8bde3c98`, with opaque-handoff coverage in
`06af07c9`. The attachment payload uses `pendingComposerTurn`; no base64
content enters route params. Private and group thread composer geometry
and routing remain unchanged.

Device evidence is recorded in
`docs/audits/home-surfaces-step3-2026-07-28/`. The inline Home composer,
attachment control, and screen passed focused Maestro assertions. The
64px dissolve is intentionally accessibility-hidden and
pointer-transparent, so its geometry is covered by the component test
and its appearance by the persisted Home capture.
