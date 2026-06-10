// ═══════════════════════════════════════════════════════════════
// VESPER · CHAT — the card families living INSIDE a Vesper turn
// (1:1 / solo). Each is introduced by Vesper's prose, then the card
// renders full-width beneath — never standalone. Reuses the card
// components from vesper-chat-cards-a/b (ctx='solo').
//
// Cards that OWN THE BODY (render their own prose, need no intro):
// Narration, Atlas-draft, Rationale ("why this"), Voice-segment.
// All others sit BENEATH a one-line Vesper note.
// ═══════════════════════════════════════════════════════════════

// A Vesper turn: short prose lead + the card object beneath.
function CardTurn({ lead, children, owns }) {
  return (
    <div>
      {owns ? <VesperEyebrow/> : <VesperProse>{lead}</VesperProse>}
      <div style={{ marginTop: 11 }}>{children}</div>
    </div>
  );
}

// 1 · PREPARED — venue + day plan
function CardsPrepared() {
  return (
    <ChatScreen header={<ChatHeader title="Tokyo, in May" sub="PRIVATE · TRIP-LINKED"/>} composer={<ChatComposer/>}>
      <UserPill time="10:02">something near the cemetery for the morning?</UserPill>
      <CardTurn lead={<>The one I’d send you to — quiet, and the light is yours before eleven.</>}>
        <VenueCard ctx="solo"/>
      </CardTurn>
      <CardTurn lead={<>And here’s how the whole day could fall around it.</>}>
        <ItineraryCard ctx="solo"/>
      </CardTurn>
    </ChatScreen>
  );
}

// 2 · DECIDE — decision/vote + booking proposal
function CardsDecide() {
  return (
    <ChatScreen header={<ChatHeader title="Tokyo, in May" sub="PRIVATE · TRIP-LINKED"/>} composer={<ChatComposer/>}>
      <UserPill time="10:20">help me pick where to stay nights 5–7</UserPill>
      <CardTurn lead={<>Two real options — I lean Sawanoya, but you’d forgive either.</>}>
        <DecisionVoteCard ctx="solo"/>
      </CardTurn>
      <CardTurn lead={<>If Sawanoya’s the one, I can hold it — nothing charged until you say.</>}>
        <BookingProposalCard ctx="solo"/>
      </CardTurn>
    </ChatScreen>
  );
}

// 3 · CONFIRM — receipt + change-applied
function CardsConfirm() {
  return (
    <ChatScreen header={<ChatHeader title="Tokyo, in May" sub="PRIVATE · TRIP-LINKED"/>} composer={<ChatComposer/>}>
      <UserPill time="10:26">yes, book it</UserPill>
      <CardTurn lead={<>Done. Three nights at Sawanoya, river side.</>}>
        <ReceiptCard ctx="solo"/>
      </CardTurn>
      <CardTurn lead={<>I moved day 4 to match — nothing else shifted.</>}>
        <ChangeAppliedCard ctx="solo"/>
      </CardTurn>
    </ChatScreen>
  );
}

// 4 · LIVE / SENSE — route/map + research-verify
function CardsLive() {
  return (
    <ChatScreen header={<ChatHeader title="Tokyo, in May" sub="PRIVATE · TRIP-LINKED"/>} composer={<ChatComposer/>}>
      <UserPill time="11:40">how do we get between the two in the morning?</UserPill>
      <CardTurn lead={<>A short hop — or twelve minutes on foot if the morning’s good.</>}>
        <RouteCard ctx="solo"/>
      </CardTurn>
      <CardTurn lead={<>One thing worth a second look before you commit:</>}>
        <ResearchCard ctx="solo"/>
      </CardTurn>
    </ChatScreen>
  );
}

// 5 · MEMORY & VOICE — atlas draft (owns body) + voice segment (owns body)
function CardsMemory() {
  return (
    <ChatScreen header={<ChatHeader title="Tokyo, in May" sub="PRIVATE · TRIP-LINKED"/>} composer={<ChatComposer/>}>
      <CardTurn owns>
        <AtlasDraftCard ctx="solo"/>
      </CardTurn>
      <UserPill time="12:02">say that back to me while I walk</UserPill>
      <CardTurn owns>
        <VoiceSegmentCard ctx="solo"/>
      </CardTurn>
    </ChatScreen>
  );
}

// 6 · EXPLAIN — rationale (owns body) + comparison
function CardsExplain() {
  return (
    <ChatScreen header={<ChatHeader title="Tokyo, in May" sub="PRIVATE · TRIP-LINKED"/>} composer={<ChatComposer/>}>
      <UserPill time="10:31">why these three and not the famous ones?</UserPill>
      <CardTurn owns>
        <RationaleBlock ctx="solo"/>
      </CardTurn>
      <CardTurn lead={<>Side by side, if it helps you feel the difference:</>}>
        <ComparisonCard ctx="solo"/>
      </CardTurn>
    </ChatScreen>
  );
}

// 7 · NARRATE + CAREFUL — narration (owns) + privacy-handoff + error
function CardsCareful() {
  return (
    <ChatScreen header={<ChatHeader title="Tokyo, in May" sub="PRIVATE · TRIP-LINKED"/>} composer={<ChatComposer/>}>
      <CardTurn owns>
        <NarrationCard ctx="solo"/>
      </CardTurn>
      <CardTurn lead={<>This part’s just between us — I’ll keep it out of the group.</>}>
        <PrivacyHandoffCard ctx="solo"/>
      </CardTurn>
      <CardTurn lead={<>One booking didn’t take — here’s exactly where it stands.</>}>
        <ErrorCard ctx="solo"/>
      </CardTurn>
    </ChatScreen>
  );
}

Object.assign(window, {
  CardTurn, CardsPrepared, CardsDecide, CardsConfirm, CardsLive,
  CardsMemory, CardsExplain, CardsCareful,
});
