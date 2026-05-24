# Summary

No P0 copy issues found. The app has several strong Vesper-native moments, especially destination-specific mock content and the private composer placeholder. The main dogfood risk is that high-traffic chrome still slips into generic product language: "Concierge", "proposal", "vote", "For You", "research team", "backend", "check your connection", and "start from scratch." That language makes Vesper feel like software managing travel data rather than a quietly opinionated travel companion.

Highest-leverage pre-dogfood copy work: tighten first-run / empty states, replace proposal mechanics with outcome language, reduce privacy overexplanation, and make Discover / Me copy more specific to the place, trip, or person.

# Copy Surfaces Reviewed

- Empty states: Trips, group chat, Discover, Me, constraints, saved venues, plan days.
- Error and loading messages: shared `ErrorState`, chat load failures, Discover failures, proposal review, photo attach.
- CTA labels: Trips start cards, Discover search/empty CTAs, proposal review actions, Me links.
- Chat composer placeholders: private Vesper chat, group chat, home concierge input.
- Permission prompts: photos, location, microphone, group-and-learn photo consent.
- Proposal/review language: proposal sheet, plan changes, group voting settings.
- Trip status / phase labels: plan empty days, plan update badges, trip status constants.
- Discover and Me copy: tab modules, empty states, section labels, trust/privacy surfaces.

# Findings

## P1 - Core concierge surfaces still use generic assistant/startup copy

The private relationship is the product, but the home entry points still use broad, chatbot-ish prompts. "Ask me anything about travel...", "Suggestions", "Plan my next trip", "Research a destination", "I’ll help you find the perfect destination", and "Deep dive on any city or region" could belong to almost any AI travel app. They do not show taste, place intelligence, or restraint.

Evidence:
- `Travel App/app/(tabs)/concierge/index.tsx:58-60` uses "Hey {name}" and "What are you thinking about?", which is warm but not travel-specific.
- `Travel App/app/(tabs)/concierge/index.tsx:84-86` uses "Ask me anything about travel..." / "Ask about travel".
- `Travel App/app/(tabs)/concierge/index.tsx:170-175` labels the rail "Suggestions" and offers generic prompts.
- `Travel App/app/(tabs)/trips/index.tsx:170-195` has a better Vesper intro, but the default prefill is still "let's plan something. Where should I start?"
- `Travel App/app/(tabs)/trips/index.tsx:253-275` uses generic archetypes and broad prefill copy like "best destinations right now."
- `Travel App/app/(tabs)/trips/index.tsx:299-310` uses "Something else" and "Start from scratch with the Concierge."

## P1 - Proposal/review copy exposes workflow mechanics instead of the travel decision

Proposal surfaces often speak in backend/product nouns: proposal type badges, approval modes, votes, neutral, group voting, organizer decision, apply status, revert change. This reads like a workflow tool. The Vesper doctrine wants approval UI around a concrete change: what is happening, who needs to act, and what the outcome will be.

Evidence:
- `Travel App/components/trip/ProposalReviewSheet.tsx:323-330` surfaces raw `proposal_type`, approval label, and status caption.
- `Travel App/components/trip/ProposalReviewSheet.tsx:715-734` renders "Votes", "approve · reject · neutral", "Your vote", "Neutral", and "Reject".
- `Travel App/components/trip/ProposalReviewSheet.tsx:741-755` says "Voting is off for this trip" and "when the backend supports it", which is internal and trust-eroding.
- `Travel App/components/trip/ProposalReviewSheet.tsx:758-788` uses "Accept change", "Decline", "Revert change", and "Undoes only the changes from this proposal."
- `Travel App/components/trip-plan/PlanChangeStrip.tsx:138-150` uses "Review proposal", "Review decision", "Needs organizer review."
- `Travel App/components/trip-plan/ChangeTimelineRow.tsx:20-31` maps user-visible status to terse workflow labels such as "Failed", "Replanned", "Updated", and "Booking started."
- `Travel App/app/trip-settings/index.tsx:215-230` labels the setting "Group voting on proposals."

## P1 - Privacy and permission copy overexplains internal mechanics

The privacy direction is correct, but several prompts are too long and too explicit about product mechanics. Phrases like "Selected Photos", "never stream raw mic audio anywhere otherwise", "Taste DNA dimensions that get richer", and "Vesper analyzes your photos" are defensible in settings, but heavy in first-run prompts. Vesper should feel trustworthy through concise promises, not legalistic bullets.

Evidence:
- `Travel App/components/ui/PermissionRationale.tsx:57-84` has generic permission titles and multi-bullet promises for every permission kind.
- `Travel App/components/chat/ComposerBar.tsx:255-256` says Vesper can identify "places, menus, or anything else you photograph", which is broad and slightly surveillance-adjacent.
- `Travel App/components/voice/MicPrivacyDisclosure.tsx:165-210` explains mic behavior in detail, including raw audio streaming and Ghost Mode.
- `Travel App/components/trip/GroupAndLearnConsentSheet.tsx:84-87` says "Let Vesper analyze your trip photos to refine your Taste DNA."
- `Travel App/components/trip/GroupAndLearnConsentSheet.tsx:111-115` exposes "Taste DNA dimensions that get richer."
- `Travel App/app/(tabs)/me/constraints.tsx:173-176`, `253-257`, `309-352` repeat "Concierge knows/share/data" framing.
- `Travel App/constants/mocks/profile.ts:55-59` privacy descriptions repeatedly say "Never shared", "Only the Concierge knows", and "Group can see..."

## P2 - Discover copy sometimes describes the content system, not the place

Discover is supposed to be an opinionated index of a city, but some labels describe internal taxonomy: "The index for", "Angles are short theses", "research team", "By Lens", "For You", "Based on your travel style", "traveler signal", and "Concierge team." The better lines are the concrete place hooks in mocks; the chrome around them is weaker.

Evidence:
- `Travel App/app/(tabs)/discover/index.tsx:705-718` uses generic search and "Cancel" chrome.
- `Travel App/app/(tabs)/discover/index.tsx:790-839` says "The index for", "Near me", and "No angles published yet for this place."
- `Travel App/app/(tabs)/discover/index.tsx:933-953` uses "All" / "By Lens" as primary view labels.
- `Travel App/app/(tabs)/discover/index.tsx:967-972` explains what angles are and references the "research team."
- `Travel App/app/(tabs)/discover/index.tsx:1069-1074` uses "Still learning your taste" and "tune recommendations."
- `Travel App/app/(tabs)/discover/index.tsx:1096-1098` says "Based on your travel style."
- `Travel App/app/(tabs)/discover/index.tsx:1426-1428` says "No picks making the rounds yet" and "the angles index has a full read."
- `Travel App/app/(tabs)/discover/index.tsx:1481-1505` uses "From the Concierge team" and "traveler signal."
- `Travel App/constants/mocks/discover.ts:61` and `71` use "The Concierge gets better..." / "has more ideas for you."

## P2 - Me tab mixes warm identity with admin/data vocabulary

Me has improved since the earlier audit, but it still oscillates between personal memory and settings console. "Library", "Settings & trust", "Constraints & Privacy", "Privacy audit", "What the Concierge knows", "Your data", "low confidence", and "Download my data" are clear, but they feel more SaaS than travel journal. Some of this belongs in settings; less of it should be first-level dogfood identity.

Evidence:
- `Travel App/app/(tabs)/me/index.tsx:153-160` uses "What Vesper knows", a useful but slightly uncanny label.
- `Travel App/app/(tabs)/me/index.tsx:195-210` groups personal surfaces under "Library" and "Your memory."
- `Travel App/app/(tabs)/me/index.tsx:251-360` uses section empties like "No co-travelers yet", "No friend activity yet", and "No saved venues yet."
- `Travel App/app/(tabs)/me/index.tsx:430-490` lists "Constraints & Privacy", "Privacy audit", "Angle Review", and "Send feedback."
- `Travel App/app/(tabs)/me/constraints.tsx:253-281` exposes learned facts, namespaces, and "low confidence."
- `Travel App/app/(tabs)/me/constraints.tsx:309-361` uses privacy/data control labels rather than traveler-centered language.
- `Travel App/app/(tabs)/me/delegation.tsx:34-76` uses admin-like labels: "Schedule changes", "Group proposals", "Act automatically", "safe limits."
- `Travel App/app/(tabs)/me/delegation.tsx:142-144` says "Control how much autonomy Vesper has for each type of decision."

## P2 - Error and loading copy is reliable but generic

The app has done the right engineering work by distinguishing empty, loading, and error states. The copy layer now needs a brand pass. Defaults like "Something went wrong", "Check your connection and try again", "Try again", "Couldn’t load X", "Searching...", and "Load earlier messages" are trustworthy but ordinary.

Evidence:
- `Travel App/components/ui/ErrorState.tsx:42-47` defines generic defaults.
- `Travel App/components/ErrorBoundary.tsx:107-111` says "An unexpected error happened while rendering. Tap retry to try again."
- `Travel App/app/(tabs)/concierge/index.tsx:101-105`, `Travel App/components/trip/ProposalReviewSheet.tsx:308-313`, and `Travel App/app/(tabs)/discover/index.tsx:1188-1191` repeat "Check your connection and try again."
- `Travel App/app/(tabs)/discover/index.tsx:1182-1197` uses "Searching..." and "No results for..."
- `Travel App/app/(tabs)/trips/[tripId]/chat.tsx:363-367` uses "Nothing here yet."
- `Travel App/app/(tabs)/trips/[tripId]/chat.tsx:420-423` uses "Message the group..." while the locked convention says "Message the group" or "Talk to the group."
- `Travel App/app/(tabs)/concierge/chat.tsx:62` suggestions are generic: "Suggest a day plan", "Restaurant ideas", "What should I pack?"

# Evidence

The strongest contrast is inside the same codebase. Mock travel content is often specific and alive, while UI chrome is generic:

- Stronger: `Travel App/constants/mocks/profile.ts:49-51` names Taberna, Lisbon, Tokyo, and San Sebastián.
- Stronger: `Travel App/constants/mocks/discover.ts:75-89` includes concrete editorial hooks.
- Weaker: `Travel App/app/(tabs)/concierge/index.tsx:172-175`, `Travel App/app/(tabs)/discover/index.tsx:1069-1074`, and `Travel App/app/(tabs)/me/constraints.tsx:309-352` describe product mechanics rather than lived travel moments.

# Suggested Fix Direction

- Use "Vesper" in user-facing copy where the relationship matters; reserve "Concierge" for lower-level settings only if needed.
- Replace generic entry prompts with one or two concrete, opinionated examples seeded by current trip, location, season, or recent memory.
- Rewrite proposal surfaces around outcomes: "Move dinner to 8:30", "The group is split", "Sarah can make this call", "Put this in the plan."
- Reduce permission prompts to one concrete benefit plus one quiet privacy promise; move detailed mechanics to a secondary "Learn more" or settings surface.
- Rename Discover chrome away from taxonomy: "Angles" and "By Lens" can become place-native labels only after the user understands the city thesis.
- Keep Me’s first viewport about identity and memory; push audit/data/admin copy deeper into settings.
- Create a shared copy checklist: concrete place/person/trip noun, no backend nouns, no raw mechanics, no generic chatbot phrasing, one clear action verb.

# Verification Ideas

- Run a string audit that flags "Concierge", "proposal", "backend", "generic", "try again", "No .* yet", "Something went wrong", and "For You" in `app/**`, `components/**`, and `constants/**`.
- Dogfood script: create first trip, open private Vesper, open group chat, review one proposal, deny one permission, visit Discover with no content, and visit Me with no social data. Capture every visible sentence.
- For each empty state, require one answer: what does this say about this user, this trip, this place, or this moment?
- For each CTA, test whether a user can predict the next screen and whether Vesper would plausibly say it out loud.
