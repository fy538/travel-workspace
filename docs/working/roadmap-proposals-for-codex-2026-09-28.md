---
doc_type: working
status: active
owner: Claude orchestrator, for the program roadmap owner (Codex lane)
created: 2026-09-28
last_verified: 2026-09-28
expires: 2026-10-12
why_new: The program roadmap belongs to the codex/home-value-delivery lane, and other sessions do not edit it directly. These are proposed changes from the September 24–28 strategy thread, for the lane owner to accept, adapt or decline.
promotes_to: docs/working/vesper-program-roadmap.md (by the lane owner)
supersedes: []
source_of_truth_for: []
---

# Roadmap proposals for the Codex lane (September 28)

**Scope.** These proposals were checked against the roadmap as it stood in
`travel-workspace--home-value-delivery` at workspace `47c91b3` on September 28:
queue items 0–3, with the capture/share package active. They are proposals. The
lane owner decides, and the founder rules where a proposal needs a ruling.

**Background.** The reasoning is in
[product direction, September 24–28](product-direction-2026-09-28.md). Two
decisions are new since the roadmap was rebaselined:
- [Collections are the spine](../decisions/2026-09-28-collections-are-the-spine.md)
- [One way in: doors, things and a connected inbox](../decisions/2026-09-28-ingestion-and-connected-inbox.md)

## 1. Bring the two September 28 decisions into the capture/share boundaries

The roadmap's "Capture/share package boundaries" already follow the September
26 and 27 records. The two new records change these parts:

- **The email door is a connected inbox.**
  - Forwarding stays as the fallback where no API exists (iCloud Mail) and for
    people who prefer it. The current forwarded-email Keep work is therefore
    still useful. Finish it as the fallback, and do not grow forwarding UI
    beyond that.
  - The connected-inbox adapter is new work:
    - OAuth;
    - filter before reading;
    - keep only matches;
    - a visible log;
    - disconnect deletes what was read but not kept.
  - A booking is filed as the person's only when it names them. Use
    schema.org reservation markup (`underName`) where the email carries it.
  - Partial scope grants from Google's granular consent must work.
  - Until Google's policy on showing Gmail-derived items to others is
    confirmed, inbox-found things stay private, even in shared collections.
  - The adapter depends on Google verification (§5).
- **Doors and things are separate.** Replace the six-door map with this door
  list: the OS share sheet, inside Vesper (camera, photos, add, Keep/Send on an
  object), Chat, the connected inbox, and a friend. A Wallet pass arrives
  through the share sheet.
- **One thing through two doors is one artifact.** It merges and lists its
  sources. This belongs in the shared intake contract, not in each door.
- **Where things land.**
  - A kept thing joins its kind collection silently, with Undo.
  - It enters a shared collection only when its author adds it.
  - Membership is many-to-many between Capture's typed artifacts and a
    collection owner. No owner exists yet; identify it in the implementation
    map rather than improvising it in a root.
- **Where people hear.**
  - Found items arrive as one grouped notification.
  - Friends' actions arrive as notifications.
  - There is no Updates feed.

  A notifications surface is therefore a dependency of the package's "refound
  and later value" conditions. Its policy (batching, quiet hours, push versus
  in-app) is still pending a founder ruling, so build the owner and hold the
  policy.

The friction proposal (save on share, "why · Change" instead of questions, *Not
yet placed*, a "Filed quietly" group) is being drawn on I0 and I1 and is not
ruled. It is worth keeping in mind for the share extension's receipt, because it
would remove the in-sheet Keep tap.

Still excluded, as the roadmap already says:
- R1–R5;
- the friction proposal;
- the ingestion defaults drawn on I0;
- whether Vesper may add to shared collections on its own.

## 2. Make the send-time payoff a measured finish condition

The core loop depends on the author seeing their thing recognized where they
are, in about two seconds. As of September 27, capture reached semantics and
anchors through a once-a-minute pipeline.

**Proposed:**
- Add p50 and p95 time-to-payoff for five share types to the capture/share
  finish condition: a place link, a screenshot, a photographed menu, a ticket
  and a book.
- Measure on the lane API before choosing between a synchronous recognition
  path and a designed waiting state.
- Record the numbers in the package's receipt.

## 3. Narrow Home's remaining gaps to what the loop needs

The roadmap already keeps Home's residuals (recovery option comparison, social
hierarchy, recurring supply) from blocking capture/share. **Proposed:** state
the Home exit the MVP needs, which is that Home shows what came back, from real
data, on a device. Treat full-scroll design parity and sustained supply as
later gates, not MVP gates.

## 4. Build profile and trust fixes before anyone else uses it

- **A dogfood build profile.**
  - The new shell is on by default and the legacy surfaces are hidden.
  - Trips, booking, Atlas and Discover are hidden, not deleted.
  - Include Sentry and PostHog.
  - On September 26 no EAS profile turned the four-root flags on; re-check.
- **The consent bug.** The newer composition path ignores `inference="none"`.
  Fix it before any friend's material reaches composition. A separate task was
  already suggested for this.
- **The booking default.** Set `BOOKING_EXECUTION_RETIRED=true` in deployed
  configuration. It was unset in `fly.toml` on September 26.
- **Background AI cost caps.** The product map found paid loops that
  `DISABLE_LLM_BACKGROUND_LOOPS` does not stop. Cap them before the next
  production deploy.

## 5. External prerequisites to start now

These need the founder. They are listed here so the queue does not wait on them
silently.

- **iOS signing and provisioning** for the in-place share extension. The Xcode
  team `QNZ5K23A74` differs from the local identity `J6ZKHAT2H7`, and the
  extension needs its App Group and Keychain entitlements.
- **Google OAuth verification for Gmail's restricted read scope,** including the
  annual CASA assessment.
  - The lane can draft the scope justification and the data-handling
    description.
  - Until verification, Google shows an unverified-app warning and caps the
    app at 100 new users (Google Cloud help, accessed September 28). That could
    carry a 20–30 person cohort through the warning screen.
- **The founder setup (about 45 minutes):**
  - the workspace CI token;
  - branch protection for a solo founder;
  - GitHub billing;
  - an Anthropic spend cap.

## 6. Ship path

**Date-based checks.** They begin failing on September 29 and block pushes, then
again on October 5, 6, 8, 9 and 12. Renew or convert to reports whatever has
not already been handled.

**Delivery closeout (queue item 0).** Close the published PRs, then deploy with
a rehearsed migration. Production ran August 14 code on September 26.

**Documentation size.** The roadmap was 217 lines on September 26 and is 399
lines on September 28. The proposal is to keep one evidence summary in H1 and
to stop committing docs after every slice, as the roadmap's own maintenance rule
already asks.

## 7. Landing note

Both this branch (`codex/product-direction-2026-09-28`) and the Home lane add:
- the September 26 and September 27 decision files, which are byte-identical;
- rows for them at the top of `docs/decisions/README.md`.

Identical files merge cleanly. The README table and its `last_verified` line
will conflict for whichever branch lands second. The fix is to keep both sets of
rows, newest first.
