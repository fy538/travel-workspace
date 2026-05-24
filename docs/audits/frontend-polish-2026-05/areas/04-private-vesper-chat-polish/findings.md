# Private Vesper Chat Polish Findings

## Summary

Private Vesper chat is functional and has several strong lifecycle fixes: retry, stop generation, offline gating, image attach, and safer stream failure handling are all present. The polish gap is identity. The 1:1 experience still renders mostly as a generic assistant chat with a privacy label, while Vesper's own doctrine says the private channel should feel like an envelope: Vesper writes on the parchment page, the user speaks in an espresso bubble, and privacy is felt through substrate rather than badges.

No P0 issues found. The highest-risk dogfood issues are P1 identity/trust gaps: private Vesper prose is rendered through the old bubble renderer; private/group rationale handling is not cleanly split; and first-contact, streaming, and late-attachment states do not yet express the locked product relationship.

## Findings

### P1 - Private Vesper still renders as a chat-bubble participant, not the core relationship

The private screen delegates every non-voice item to `MessageBubble` with `isPrivate` (`Travel App/app/(tabs)/concierge/chat.tsx:65-80`). `MessageBubble` then renders an AI tag plus a "Private" badge (`Travel App/components/chat/MessageBubble.tsx:84-91`) and a purple AI bubble (`Travel App/components/chat/MessageBubble.tsx:99-127`, `Travel App/components/chat/MessageBubble.tsx:263-266`).

That directly conflicts with the locked decision that 1:1 chat is "prose on a parchment page, not a chat bubble" (`Travel App/docs/design-decisions/agent-chat.md:20-29`) and the propagated doctrine that "1:1 with Vesper = envelope" (`Travel App/docs/Design Language.md:230-236`). In dogfood, this makes the most important surface feel like a generic group/chatbot transcript with a privacy sticker rather than a composed concierge relationship.

### P1 - Substantive private prose uses UI-scale bubble typography instead of article-scale Vesper writing

The private AI body uses `react-native-markdown-display` with `typography.body` (`Travel App/components/chat/MessageBubble.tsx:347-363`) inside a max-width bubble (`Travel App/components/chat/MessageBubble.tsx:237-258`). The docs explicitly say substantial Vesper prose is reading content and should use article-scale Fraunces 17/27 (`Travel App/docs/page-specs/agent-chat.md:127-150`, `Travel App/docs/page-specs/agent-chat.md:254-260`; `Travel App/docs/Design Language.md:125-131`; `Travel App/docs/Brand Identity.md:96-126`).

This matters because private turns can be long, candid, and essay-shaped. A 600-token privacy-sensitive reply rendered as a small purple chat bubble will feel less calm, less trustworthy, and less premium than Vesper writing directly on the page.

### P1 - Recommendation rendering lacks an explicit private/group boundary

`RecommendationBlock` always renders `why_for_person` when present (`Travel App/components/chat/RecommendationBlock.tsx:21-29`, `Travel App/components/chat/RecommendationBlock.tsx:42-47`). Group chat's dispatcher also renders `RecommendationBlock` for group Vesper objects (`Travel App/components/chat/group/GroupThreadItem.tsx:152-156`, `Travel App/components/chat/group/GroupThreadItem.tsx:174-176`).

The doctrine says `why_for_person` is private-only and is never rendered in group context (`Travel App/docs/Design Language.md:217-228`). The backend may already omit the field in group payloads, but the UI component does not enforce that invariant. That is a trust-boundary footgun: one bad payload or mapper regression could expose private rationale in the group room.

### P1 - Streaming and late attachments still feel like backend events, not Vesper writing and handing over objects

The locked choreography is: prose streams, then a reserved dashed letterpress slot appears, then metadata resolves the card (`Travel App/docs/design-decisions/agent-chat.md:61-69`; `Travel App/docs/Design Language.md:253-261`). Current private chat instead appends a placeholder AI message, streams text into it, and invalidates history after metadata so tool-posted cards arrive on refetch (`Travel App/hooks/useConciergeChat.ts:383-424`, `Travel App/hooks/useConciergeChat.ts:563-618`).

The typing indicator also exposes backend-style status labels in the default private variant (`Travel App/hooks/useConciergeChat.ts:529-542`; `Travel App/components/chat/TypingIndicator.tsx:94-108`), while the page spec says the agent's machinery is doctrinally invisible (`Travel App/docs/page-specs/agent-chat.md:226-249`). This is not broken behavior, but it makes streaming feel operational instead of composed.

### P2 - First-contact and empty states are missing the trust-contract moment

The private FlatList empty state renders skeletons while loading, an error state on failure, and otherwise `null` (`Travel App/app/(tabs)/concierge/chat.tsx:874-897`). The composer supplies generic suggestions (`Travel App/app/(tabs)/concierge/chat.tsx:61`) and generic copy, `"Ask the Concierge..."` (`Travel App/app/(tabs)/concierge/chat.tsx:934-937`).

The brand copy contract says private 1:1 should say "Tell Vesper anything - just you" (`Travel App/docs/Brand Identity.md:230-235`) and first contact should establish the privacy contract with contextual suggestions, never generic prompts (`Travel App/docs/Brand Identity.md:244-253`; `Travel App/docs/Design Language.md:263-266`). The first week of dogfood is exactly when people decide whether they can say the quiet thing to Vesper; a blank/generic start weakens that trust.

### P2 - Privacy is over-labeled and under-substrated

Private chat shows a lock-based header row (`Travel App/components/chat/ChatPrivacyBar.tsx:21-31`) and each Vesper message can show a "Private" badge (`Travel App/components/chat/MessageBubble.tsx:84-91`). The page spec explicitly calls current "Private badge + lock icon" the baseline to move beyond and says channel differentiation is a privacy contract, not a label (`Travel App/docs/page-specs/agent-chat.md:320-328`; `Travel App/docs/page-specs/agent-chat.md:273-283`).

Labels are still useful for accessibility and reassurance, but visual privacy should come from the envelope substrate: page prose, quieter chrome, private-only attribution, and no group-chat metaphors. The current layering risks saying "trust me" instead of letting the surface feel trustworthy.

### P2 - Shared chat primitives make private and group divergence harder than it should be

The group thread has already grown a dedicated dispatcher and Vesper prose renderer: `GroupThreadItem` routes messages by object type (`Travel App/components/chat/group/GroupThreadItem.tsx:1-24`, `Travel App/components/chat/group/GroupThreadItem.tsx:84-182`), and `VesperNote` renders Vesper as attributed article-scale prose (`Travel App/components/chat/group/VesperNote.tsx:1-17`, `Travel App/components/chat/group/VesperNote.tsx:110-148`). Private chat still goes through the older generic `MessageBubble` path (`Travel App/app/(tabs)/concierge/chat.tsx:65-80`).

The architecture is now inverted: group chat has the more doctrine-aligned Vesper prose component, while the core private relationship uses the legacy bubble. This makes future fixes likely to accrete flags like `isPrivate` instead of letting private and group evolve cleanly.

## Evidence

Internal doctrine and implementation anchors:

- Product is the concierge relationship, not a group chat tool: `Travel App/docs/Design Language.md:7-10`.
- Invisible privacy, visible care: `Travel App/docs/Design Language.md:22-25`.
- Purple is reserved for AI/concierge presence: `Travel App/docs/Design Language.md:84-88`.
- Article scale is for reading surfaces: `Travel App/docs/Design Language.md:125-131`.
- Minimum touch target is 44pt: `Travel App/docs/Design Language.md:153-154`.
- 1:1 envelope substrate is locked: `Travel App/docs/Design Language.md:230-236`.
- Streaming reserved-slot choreography is locked: `Travel App/docs/Design Language.md:253-261`.
- First-contact opener is locked but substrate-dependent: `Travel App/docs/Design Language.md:263-266`.

External platform/accessibility baseline:

- [Apple HIG - Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons): buttons need an approximately 44x44 pt hit region and a clear press state.
- [Apple HIG - Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility): iOS/iPadOS controls should meet the recommended minimum control size and preserve spacing between controls.
- [Material Design - Accessibility](https://m2.material.io/design/usability/accessibility.html): touch targets should generally be at least 48x48 dp, with padding around smaller icons.
- [WCAG 2.2 SC 2.5.8 Target Size Minimum](https://www.w3.org/TR/WCAG22/#target-size-minimum): pointer targets are at least 24x24 CSS px except for defined exceptions.

## Suggested Fix Direction

Split private chat from group chat at the rendering boundary:

- Add a private dispatcher, e.g. `PrivateThreadItem`, rather than continuing to route private Vesper through `MessageBubble`.
- Add `PrivateVesperNote`: `+ VESPER` fleuron attribution, article-scale Fraunces prose on the page, no purple bubble, no per-message "Private" badge.
- Keep `MessageBubble` for user messages, member messages, and compact system/send-failure states.
- Make `RecommendationBlock` context-aware: private can render `why_for_person`; group must drop it defensively even if the payload includes it.
- Treat `move` as headline prose, `what_to_notice` / `what_to_skip` as quiet notes, and `timing_note` as either italic operational note or inline CTA when it contains a phone number/deadline.
- Replace generic first-contact suggestions with contextual trust-contract chips and update private composer copy to the locked string.
- For streaming, implement the reserved-slot pattern for likely attachments and use ambient concern copy only when supported by safe `progress_signal` events; otherwise prefer quiet presence over raw tool chatter.

Render taxonomy for private Vesper:

- **Prose:** candid coaching, planning narrative, personal memory, nuanced tradeoff.
- **Note:** quiet operational status, privacy simplification, "I need a smaller bite" recovery, retry context.
- **Card:** venue, booking, plan change, map, image analysis result, anything the user can inspect or act on.
- **Inline action:** call, reserve, open map, accept/tweak/reject, retry send, stop generation.
- **Operational status:** connecting, reconnecting, offline, saving attachment, permission needed. Keep these outside Vesper's voice unless Vesper is actually speaking.

## Verification Ideas

- Screenshot-test private chat at 390pt width for: first contact, long candid Vesper reply, streaming at 1s/30s/complete, late venue attachment, send failure, offline send, reconnect, and image attached.
- Add a fixture where `recommendation.why_for_person` is accidentally present in a group message and verify group UI suppresses it.
- Run touch-target overlays for header controls, composer controls, suggestion chips, retry, attachment remove, and inline CTAs against Apple 44pt / Material 48dp guidance.
- Dogfood script: ask Vesper something private that should not go to the group, then compare private and group thread screenshots side-by-side. A new tester should understand the privacy boundary without reading the word "Private."
