---
doc_type: decision
status: accepted
owner: founder / product / contribution / social design
created: 2026-09-27
decided: 2026-09-27
last_verified: 2026-09-27
why_new: The founder set the core loop and the single capture-and-share entrance in strategy review on September 26–27, 2026. The rulings change the contribution contract's Ask/Bring entry table, Chat ruling 04 and the September 26 audience list, and until now existed only in conversation.
supersedes: []
source_of_truth_for:
  - documenting-core-loop
  - one-composer-entrance
  - share-artifact-intent-audience-model
---

# Decision: Documenting is the core loop, entered through one composer

## Context

Between September 25 and 27, 2026 the founder and the orchestrating session
reviewed Vesper's identity against Meta's Muse and adjacent products. The review
drew on the repositories' docs, the Claude Design projects, code at the
`codex/home-value-delivery` lane (travel-agent `08b03fd14`), and web research
dated through September 25.

The founder's direction, in substance:

- Vesper is a personal AI built on ordinary personal and multiplayer sharing,
  grounded in time and place, organized by artifacts, reaching across a
  person's life, and useful from documenting.
- The mechanism is documenting what you encounter, not saving bookmarks. The
  core loop is documenting for yourself, or for your family or friends.
- Because people share, privately or with others, Vesper can do things from
  what was shared: plans, itineraries, drafts.
- Product design should favor immediate benefit, the least possible friction
  when sharing, and maximum satisfaction at the moment of sharing.
- Sharing, broadcasting and documenting should be one horizontal motion.

Four recorded rules pull against this:

- The [contribution contract](../systems/contribution-and-consequence.md) §3.2
  treats a Source that accompanies a question as a transient Ask.
- [Chat ruling 04](../working/claude-design-chat-rulings-and-handoffs-2026-09-14.md)
  sends carried-in context "with one question only."
- The [September 26 multiplayer direction](2026-09-26-multiplayer-direction.md),
  item 7, names no private audience.
- Share capture still leads with review, which contract §12 already records as
  non-conforming.

This record is consistent with the
[August 23 lived-world identity](2026-08-23-adopt-lived-world-product-identity.md),
the [August 29 contribution contract](2026-08-29-adopt-contribution-and-consequence-contract.md)
and [use grants](2026-08-29-adopt-contribution-use-grants.md) (except where named
below), the [September 8 capture lifecycle](2026-09-08-capture-candidate-lifecycle.md),
the [September 9 exact-original display](2026-09-09-exact-original-recipient-display.md),
and the September 26 multiplayer direction (items 1 and 7 are extended below). It
does not replace any of them.

## Decision

### The loop

1. **The experience is the center.** Attention is how it enters; the
   relationship between a person, their people and the world is what compounds.
   This clarifies the August 23 identity and does not supersede it.
2. **Documenting is the primary gesture.** A person shares what they encounter:
   a place, a photograph, a ticket, a menu, a screenshot, a friend's words. They
   share it for themselves, or for family or friends. The default audience is
   just me. Vesper is not a diary. It asks for no writing, prompts or streaks;
   the record is a by-product, and what comes back looks forward.
3. **The loop:**
   1. document;
   2. a standard artifact;
   3. threads, the person's own and shared;
   4. where threads meet, answers to "what's right for this?" and prepared
      actions (plans, itineraries, drafts);
   5. the person commits and lives it;
   6. what happened is documented.

   Vesper prepares; the person sends or commits. The retirement of booking
   execution is unchanged.
4. **Documenting and sharing are one act.** Documenting, sending to a person or
   group, and sharing with Friends differ only in audience. Sharing later is the
   same object given a wider audience, chosen explicitly by its author.

### One composer

5. **One composer, many doors.** The composer from September 26 item 1 is the
   only composer for capture and sharing. Every door opens it:
   - the OS share sheet (the primary door);
   - the in-app camera and photo picker;
   - the global add control;
   - the Chat composer;
   - Send or Keep on any existing object;
   - email forwarding.

   It is a horizontal capability: one component, one contract and one send-time
   payoff. Contribution and gesture resolution own it; no root does.
6. **Chat is a door, not the entrance.** Chat is the door for sharing with a
   question. It remains the destination for conversation with Vesper and for
   occasion rooms. Capture never requires Chat, which matches Chat's standing
   rule that it is not a mandatory gateway.
7. **The share model.** A share is artifact(s) + intent + audience, with an
   optional note and an optional question to Vesper.
   - **Artifact:** what the thing is, drawn from an open catalog of
     standardized types that keeps extending to fit people's interests — a
     menu, a ticket, a book, a golf scorecard, a baseball card. Each type holds
     the person's meaning in a standard form and tells the system what may and
     may not be inferred from it. The catalog's mechanism is R3 below.
   - **Intent:** one of the four kinds from September 26 item 1 (words and
     photos, a gathering invitation, "where I'll be", a place with what it is
     good for), inferred from what is attached.
   - **Audience:** just me, a named person, a named group, or Friends.

   This is the "new share and audience model" that the September 26 record says
   is needed. Its schema is not designed here.
8. **Decide as little as possible at send.**
   - Vesper infers artifact type, intent, time and place, and never shows a type
     picker (September 26 item 1 stands).
   - It proposes threads after the send, without blocking it.
   - Corrections take one tap, afterward.
   - Location precision toward others follows September 26 item 4.
9. **Audience is the one real choice.**
   - Just me is the default. It is added to the audiences in September 26
     item 7.
   - A wider audience takes one tap: recent people and groups appear as chips,
     alongside Friends.
   - Vesper may suggest a person. It never widens an audience itself.
10. **The control names the consequence:** *Keep* for just me, *Send* for a
    person or group, *Share* for Friends. The contract's gesture names (Bring,
    Keep, Share/Address) are unchanged internally.
11. **Keep first, correct after.**
    - Keeping is immediate and private, with Undo (September 26 item 16).
    - The review-first capture step leaves the path.
    - Interpretation stays provisional under contract §7 and never asserts
      occurrence, preference or meaning by implication.
    - The truth chain (§5) and the September 8 candidate lifecycle are
      unchanged.
12. **The send-time payoff belongs to the author.** Right after sending, the
    author sees their thing as a recognized artifact and where it went, for
    example "Kept · Lulu's · second time here." Nothing Vesper writes appears
    under a share that others see (September 26 item 3).
13. **The OS share sheet completes in place.** The share extension presents the
    composer and finishes without taking the person into the app.

### Asking with a share

14. **A deliberate share that carries a question is Bring plus Ask.** The shared
    Source is kept, privately and with Undo, and the question is answered.
    - This amends two rules:
      - contract §3.2's row "Source accompanying a question → Ask" for shares
        made through the composer;
      - Chat ruling 04 for attachments in the Chat composer. There, the keep
        state is visible, and one tap chooses *Ask only*, which keeps nothing.
    - The question and its answer keep the existing conversation-retention
      rules.
    - This record does not adopt casual-question continuity (contract §3.10).
15. **Note versus question.**
    - When the audience is just me, the note may carry a question, and Vesper
      answers privately.
    - When the audience includes other people, the note goes to them and Vesper
      does not answer inside it. A question to Vesper uses a separate private
      *Ask Vesper* control.
    - Vesper sends no words on the person's behalf, which is Chat's standing
      rule.

### Boundaries that do not move

- No inference of personality, preference or identity (contract §3.8 and §11).
- A friend's words and photographs stay within the audience they were sent to;
  places and links travel (September 26 item 8).
- Taking a share back removes the author's words everywhere (item 9).
- Vesper prepares and the person sends (September 9).
- AI use of a friend's words stays limited to September 26 item 19 until the
  use-grant contract is amended.

## Not decided here — founder ruling pending

These recommendations came out of the same review and are recorded so they are
not lost. Each needs its own ruling, and changes its named owner only once ruled.

- **R1 — Threads and intersections.**
  - Vesper proposes threads under the two-context evidence gate in
    [the Life engine design §6.3](../working/life-organization-and-composition-engine-system-design-2026-09-05.md),
    and the person accepts or renames them with one tap.
  - Intersections are computed from shared members: a place, a person, an
    artifact or a time window.
  - A prepared action is offered only where threads meet, once, and it expires.
  - This would amend the Threads definition in the
    [Life v1 contract](../contracts/life-v1-experience.md) and the working
    brief's "does not owe an action."
- **R2 — Voice.**
  - Vesper is opinionated about connections and usefulness, and silent about
    meaning.
  - Limit how often Vesper speaks, not how confidently.
  - This would amend the "the record noticed" register, and "recommends once" in
    the seven-sentences ruling only as it applies to intersections.
- **R3 — The artifact catalog's mechanism.**
  - One contract replaces the competing type vocabularies.
  - A small fixed set of meaning families sits above an open set of types.
    Types are defined as data, not code.
  - No one approves types, neither users nor the team. A share always lands at
    once in its family. A personal type forms automatically when a person's
    similar items recur, and only that person sees it. A shared type is
    promoted automatically when enough independent people have the same kind
    of thing and its fields agree; a shared spec holds structure, never
    content. Types anchor to outside catalogs where one exists, merge
    automatically when they overlap, and keep versions so kept items survive
    change. The team supervises through metrics (coverage, extraction accuracy,
    duplicate rate, correction rate), not by reviewing types.
  - Each type has one canonical shape, one optional judgment given by the
    person, a counted send-time payoff, and evidence rules for what it can
    prove.
  - This needs an architecture ruling: Product Model §1.2 rejects a universal
    artifact table, so the catalog is a type registry over Sources linked to
    canonical entities, not a new owner.
  - The candidate starting point is the expired grammar
    `travel-agent/docs/working/artifact-and-experience-anchor-grammar-v1-2026-08-21.md`.
  - The Stage 2 instrument language is the candidate register for payoffs and
    recaps.
- **R4 — Offers from a friend's status.**
  - A friend's time-bound "where I'll be" or place share may trigger a private
    offer to the recipient.
  - The offer uses only the place and the time, never the friend's words.
  - It extends September 26 item 19 and requires the use-grant amendment.
- **R5 — Sequencing.**
  - After Home H1, build one thin slice through both halves:
    - keep-first sharing;
    - sending to a person, credited;
    - the recipient's keep joining their record;
    - one offer where one person's thread meets another's share.
  - The roadmap owner decides.

## Consequences

- **Owner documents to update:**
  - Contract §3.2 (the entry table), §9 (name the composer as the horizontal
    capture owner) and §12 (alignment).
  - The product canon's primary-gesture wording, in
    [Product Thesis](../../travel-agent/docs/product/Product%20Thesis.md) and
    [Product Model](../../travel-agent/docs/product/Product%20Model.md).
  - The Chat rulings document, to note that ruling 04 is amended here.
  - The September 26 record, whose items 1 and 7 are read together with this one.
- **Engineering:**
  - one composer component in `travel-app`, used by every door;
  - a share extension that completes in the sheet (today
    `travel-app/ios/ShareExtension/ShareViewController.swift` redirects to the
    app);
  - the review-first step removed from `travel-app/app/share-capture/index.tsx`;
  - one backend share contract, extending intake submissions and relationship
    handoffs (the schema is not designed here);
  - the Chat composer rebuilt on the shared component.

  API changes follow the workspace OpenAPI sync.
- **Measures:**
  - the share of shares that later return as a connection or an action;
  - how often shares go beyond just me;
  - abandonment at the moment of sending.
- **Runtime:** this record changes no runtime behavior, flag or schema.
  Implementation needs a lane and Task Intake evidence.
- **Not decided here:**
  - the artifact type list;
  - notification policy;
  - guest identity (the guest-link proposal remains open);
  - retention periods and export;
  - where kept items surface beyond their existing owners.

## Revisit trigger

- **Reopen item 11** if keep-first capture produces interpretations that people
  routinely correct or remove.
- **Reopen item 9** if shares rarely go beyond just me and multiplayer stays
  unused.
- **Reopen item 14** if people are surprised that a share with a question was
  kept, or if Chat attachments that were kept become clutter people delete.
- **Reopen item 10** if the Keep, Send and Share labels confuse people in dogfood.

Do not rewrite this record if that happens; add a new decision and mark this one
`superseded`.
