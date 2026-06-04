// ─── CHAT-CARD CANVAS SECTIONS ──────────────────────────────────
// Renders, per card: one wide artboard with the 1:1 (Vesper-on-page)
// view beside the group (bubble + public card) view, plus a spec panel.
// Exported as <ChatSections/> — an array of <DCSection> for the canvas.

// 1:1 column — Vesper writes on the page, card full-width beneath.
function SoloDemo({ line, trailing, children }) {
  return (
    <ChatCol label="IN 1:1 · VESPER WRITES ON THE PAGE">
      <VesperSays trailing={trailing}>{line}</VesperSays>
      {children}
    </ChatCol>
  );
}

// Group column — bubbles, attribution, the card shared into the thread.
function GroupDemo({ pre, who = 'vesper', time = '10:14', children, post }) {
  return (
    <ChatCol label="IN GROUP · PUBLIC CARD IN A BUBBLE">
      {pre}
      <GroupTurn who={who} time={time}>{children}</GroupTurn>
      {post}
    </ChatCol>
  );
}

function CardPair({ children }) {
  return <div style={{ display: 'flex', gap: 22, justifyContent: 'center', padding: '8px 16px' }}>{children}</div>;
}

// Spec panel — the seven fields the brief asks for, per card.
function ChatSpec({ name, appears, contains, primary, secondary, solo, group, privacy, placement }) {
  const Row = ({ k, children, accent }) => (
    <div style={{ display: 'grid', gridTemplateColumns: '92px 1fr', gap: 11, padding: '8px 0', borderTop: `0.5px solid ${T.hairThin}` }}>
      <div style={{ fontSize: 8.5, letterSpacing: 1.3, color: accent ? T.goldDeep : T.mute, fontWeight: 700, paddingTop: 2 }}>{k}</div>
      <div style={{ fontSize: 11.5, color: T.inkSoft, lineHeight: 1.45 }}>{children}</div>
    </div>
  );
  return (
    <div style={{ width: 380, padding: '24px 24px', background: '#F1ECE2', borderRadius: 8 }}>
      <div style={{ fontSize: 10, letterSpacing: 2, color: T.gold, fontWeight: 600 }}>CHAT CARD · SPEC</div>
      <h3 style={{ fontFamily: T.serif, fontSize: 23, fontWeight: 500, letterSpacing: -0.5, color: T.ink, margin: '4px 0 10px' }}>{name}</h3>
      <Row k="APPEARS">{appears}</Row>
      <Row k="MUST HAVE">{contains}</Row>
      <Row k="PRIMARY" accent>{primary}</Row>
      <Row k="SECONDARY">{secondary}</Row>
      <Row k="IN 1:1">{solo}</Row>
      <Row k="IN GROUP">{group}</Row>
      <Row k="PRIVACY">{privacy}</Row>
      <Row k="PLACEMENT">{placement}</Row>
    </div>
  );
}

// One section = pair artboard + spec artboard.
function CardSection({ id, n, title, sub, pair, spec, pairW = 800, pairH = 520 }) {
  return (
    <DCSection id={id} title={`${n} · ${title}`} subtitle={sub}>
      <DCArtboard id={`${id}-pair`} label="1:1 vs group" width={pairW} height={pairH} bg="transparent">
        <CardPair>{pair}</CardPair>
      </DCArtboard>
      <DCArtboard id={`${id}-spec`} label="Spec" width={420} height={pairH} bg="transparent">
        {spec}
      </DCArtboard>
    </DCSection>
  );
}

function ChatSections() {
  return (
    <React.Fragment>

      {/* COVER */}
      <DCSection id="chat-cover" title="Chat cards" subtitle="Conversation artifacts — distinct from the proactive Home cards. The system, then fifteen card types in 1:1 and group.">
        <DCArtboard id="chat-brief" label="The chat-card system" width={680} height={620} bg="#F1ECE2">
          <div style={{ padding: '40px 36px', fontFamily: T.sans, color: T.inkSoft, fontSize: 13.5, lineHeight: 1.55 }}>
            <div style={{ fontSize: 10.5, letterSpacing: 2, color: T.gold, fontWeight: 600 }}>VESPER · CHAT CARDS</div>
            <h1 style={{ fontFamily: T.serif, fontSize: 42, lineHeight: 0.98, letterSpacing: -1.2, fontWeight: 500, margin: '8px 0 14px', color: T.ink }}>
              What Vesper <em>makes</em>,<br/>inside a conversation.
            </h1>
            <p style={{ margin: '0 0 18px', maxWidth: 560 }}>
              Home cards are <b>proactive work objects</b> on the Vesper tab. Chat cards are
              <b> conversation artifacts</b> — the structured things Vesper produces after you ask,
              or as it works. Same paper language; different rules for where they sit.
            </p>
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 16 }}>
              <div style={{ padding: 16, background: '#FBF7EC', borderRadius: 10, border: `0.5px solid ${T.hairline}` }}>
                <div style={{ fontSize: 9.5, letterSpacing: 1.6, color: T.goldDeep, fontWeight: 700, marginBottom: 8 }}>IN 1:1</div>
                <p style={{ margin: 0, fontSize: 12.5, lineHeight: 1.5 }}>
                  Vesper <b>writes on the page</b>. A <code>+ VESPER</code> note in serif, then the card
                  full-width beneath — <i>no bubble</i>. Actions are typographic with one quiet primary.
                  It reads like a letter, not a chat log.
                </p>
              </div>
              <div style={{ padding: 16, background: '#FBF7EC', borderRadius: 10, border: `0.5px solid ${T.hairline}` }}>
                <div style={{ fontSize: 9.5, letterSpacing: 1.6, color: TR.inkDeep, fontWeight: 700, marginBottom: 8 }}>IN GROUP</div>
                <p style={{ margin: 0, fontSize: 12.5, lineHeight: 1.5 }}>
                  Explicit <b>bubbles + attribution</b>. Cards are <i>public objects</i> shared into the
                  thread, with avatars, votes, and split-aware copy. Actions become real buttons.
                  Private fields are softened or withheld.
                </p>
              </div>
            </div>
            <div style={{ borderTop: `0.5px solid ${T.hairline}`, marginTop: 18, paddingTop: 14 }}>
              <div style={{ fontSize: 10, letterSpacing: 2, color: T.mute, fontWeight: 600, marginBottom: 8 }}>PLACEMENT — THREE WAYS A CARD SITS</div>
              <ul style={{ margin: 0, padding: 0, listStyle: 'none', display: 'grid', gap: 6, fontSize: 12.5 }}>
                <li><b>Below a Vesper note</b> — most cards in 1:1. The note sets up the object.</li>
                <li><b>Full-width object</b> — itinerary, route, comparison, receipt; they own the row.</li>
                <li><b>Inside a bubble</b> — group only; the card is attributed to a sender.</li>
              </ul>
            </div>
          </div>
        </DCArtboard>
      </DCSection>

      {/* 1 · VENUE */}
      <CardSection id="cc1" n="01" title="Venue / Place"
        sub="When Vesper surfaces a specific place — after a query, or mid-plan."
        pair={<>
          <SoloDemo line="Here’s the one I meant — quiet, and on your way." trailing="FOUND IT">
            <VenueCard ctx="solo"/>
          </SoloDemo>
          <GroupDemo pre={<UserBubble who="ana" time="10:12">anywhere good for coffee near the ryokan?</UserBubble>}>
            <VenueCard ctx="group"/>
          </GroupDemo>
        </>}
        spec={<ChatSpec name="Venue / Place"
          appears="After a place query, or when Vesper recommends a specific spot mid-plan."
          contains="Name, type, neighborhood, one-line why, hours + price tier, a thumbnail or map dot."
          primary="Save (1:1) / Add to trip (group)."
          secondary="Directions · more like this."
          solo="Below a Vesper note; warm rationale (‘the morning light you keep noticing’)."
          group="Public card in a bubble, answering whoever asked; neutral descriptor."
          privacy="Personal taste rationale → neutral descriptor. Price tier softened to ¥¥."
          placement="Below a Vesper note (1:1) · inside a bubble (group)."/>}/>

      {/* 2 · ITINERARY */}
      <CardSection id="cc2" n="02" title="Itinerary / Day Plan"
        sub="When a day or trip takes shape — Vesper lays out the stops."
        pair={<>
          <SoloDemo line="Day three, kept slow — you’ve got the morning to wander." trailing="DRAFTED">
            <ItineraryCard ctx="solo"/>
          </SoloDemo>
          <GroupDemo>
            <ItineraryCard ctx="group"/>
          </GroupDemo>
        </>}
        spec={<ChatSpec name="Itinerary / Day Plan"
          appears="When Vesper assembles or revises a day; after enough stops are saved."
          contains="Day header, 3–5 time-stamped stops, who-added (group), a way into the full plan."
          primary="Open full plan / Open shared plan."
          secondary="Adjust · reflow times · suggest a stop (group)."
          solo="Full-width object under a note; no author chips."
          group="Collaborative — each stop shows the avatar who added it."
          privacy="Private notes on a stop are hidden; only the public stop name shows."
          placement="Full-width object."/>}/>

      {/* 3 · ROUTE */}
      <CardSection id="cc3" n="03" title="Map / Route"
        sub="When movement matters — a walk, a route between stops."
        pair={<>
          <SoloDemo line="It’s mostly downhill if you start at the café." trailing="A ROUTE">
            <RouteCard ctx="solo"/>
          </SoloDemo>
          <GroupDemo>
            <RouteCard ctx="group"/>
          </GroupDemo>
        </>}
        spec={<ChatSpec name="Map / Route"
          appears="When a route/walk is relevant, or the user asks how to get between places."
          contains="Illustrated route, ordered stops, distance + time, start/end."
          primary="Walk me through (1:1) / Open in maps (group)."
          secondary="Reverse · add a stop · save."
          solo="Full-width; shows your private ‘stay’ pin as a reference."
          group="Public route; the private home/stay pin is removed."
          privacy="Home / accommodation pins hidden in group."
          placement="Full-width object."/>}/>

      {/* 4 · COMPARISON */}
      <CardSection id="cc4" n="04" title="Comparison"
        sub="When Vesper narrows options and shows the tradeoffs."
        pair={<>
          <SoloDemo line="Three I’d actually book. I lean Sawanoya." trailing="COMPARING">
            <ComparisonCard ctx="solo"/>
          </SoloDemo>
          <GroupDemo>
            <ComparisonCard ctx="group"/>
          </GroupDemo>
        </>}
        spec={<ChatSpec name="Comparison"
          appears="When 2–3 viable options exist and a choice is needed."
          contains="Options as columns, 3–4 attribute rows, Vesper’s pick marked."
          primary="Pick (1:1) / Cast your vote (group)."
          secondary="Why this one · see all."
          solo="Vesper’s pick highlighted in ochre; opinion is explicit."
          group="Pick replaced by a live tally; per-column votes with counts."
          privacy="Budget/price row softened to tier; personal-fit reasoning withheld."
          placement="Full-width object."/>}/>

      {/* 5 · DECISION / VOTE */}
      <CardSection id="cc5" n="05" title="Decision / Vote"
        sub="When a single call is needed — yours, or the group’s."
        pair={<>
          <SoloDemo line="Your call on dates — I’ve a lean, but it’s yours." trailing="ONE CHOICE">
            <DecisionVoteCard ctx="solo"/>
          </SoloDemo>
          <GroupDemo pre={<UserBubble who="theo" time="09:50">when are we actually going??</UserBubble>}>
            <DecisionVoteCard ctx="group"/>
          </GroupDemo>
        </>}
        spec={<ChatSpec name="Decision / Vote"
          appears="A binary/short choice; group scheduling; a fork in planning."
          contains="The question, 2–4 options, Vesper’s lean (1:1) or live tally (group)."
          primary="Choose (1:1) / Vote (group)."
          secondary="Hold · ask a person · add option (group)."
          solo="No tally — just options + Vesper’s gentle lean. It’s your decision."
          group="Live vote with voter avatars; sage accent; ‘add option’ open."
          privacy="In 1:1 no one sees your choice; in group, voter identity can be set to anonymous."
          placement="Full-width (group) · below a note (1:1)."/>}/>

      {/* 6 · BOOKING PROPOSAL */}
      <CardSection id="cc6" n="06" title="Booking Proposal"
        sub="Before money moves — Vesper proposes exactly what it will book."
        pair={<>
          <SoloDemo line="Ready when you are — free to cancel for a week." trailing="PROPOSED">
            <BookingProposalCard ctx="solo"/>
          </SoloDemo>
          <GroupDemo>
            <BookingProposalCard ctx="group"/>
          </GroupDemo>
        </>}
        spec={<ChatSpec name="Booking Proposal"
          appears="When a bookable option is agreed and Vesper needs approval to commit."
          contains="Item, dates, price (total or per-person), cancellation terms, hold window."
          primary="Approve & book (1:1) / Approve my share (group)."
          secondary="Adjust · not now."
          solo="Shows full total + terms; one-tap approve."
          group="Per-person split; ‘approve my share’; payment method never shown."
          privacy="Payment method hidden; exact total → per-person estimate in group."
          placement="Full-width object."/>}/>

      {/* 7 · RECEIPT */}
      <CardSection id="cc7" n="07" title="Booking Confirmation / Receipt"
        sub="After it’s booked — the artifact you keep."
        pair={<>
          <SoloDemo line="Done. You’re in for the 18th." trailing="CONFIRMED">
            <ReceiptCard ctx="solo"/>
          </SoloDemo>
          <GroupDemo>
            <ReceiptCard ctx="group"/>
          </GroupDemo>
        </>}
        spec={<ChatSpec name="Confirmation / Receipt"
          appears="Immediately after a successful booking."
          contains="Item, dates, confirmation #, amount + method, address, check-in."
          primary="Add to calendar."
          secondary="View · forward."
          solo="Full receipt incl. confirmation number + masked card."
          group="‘Booked by you for the group’; confirmation # + payment hidden behind ‘on request’."
          privacy="Confirmation number, amount, and card masked/withheld in group."
          placement="Full-width object; perforated like a ticket."/>}/>

      {/* 8 · CHANGE APPLIED */}
      <CardSection id="cc8" n="08" title="Change Applied"
        sub="After Vesper edits the plan — a small, undoable diff."
        pair={<>
          <SoloDemo line="Did it — less back-and-forth across the city." trailing="CHANGED">
            <ChangeAppliedCard ctx="solo"/>
          </SoloDemo>
          <GroupDemo>
            <ChangeAppliedCard ctx="group"/>
          </GroupDemo>
        </>}
        spec={<ChatSpec name="Change Applied"
          appears="Right after Vesper mutates an itinerary, booking, or list."
          contains="What changed (was → now), why in one line, undo."
          primary="Keep it (1:1) / See plan (group)."
          secondary="Undo · show both."
          solo="‘I made the change’ — first person, with undo."
          group="‘Vesper updated the plan’ — attributed; everyone can undo/see."
          privacy="Minimal; the diff is about shared plan state, not personal data."
          placement="Below a Vesper note; compact, not full object."/>}/>

      {/* 9 · RATIONALE */}
      <CardSection id="cc9" n="09" title="Recommendation Rationale"
        sub="The ‘why’ expansion — the most privacy-sensitive block."
        pair={<>
          <SoloDemo line="Want the reasoning? Here’s what I weighed." trailing="WHY">
            <RationaleBlock ctx="solo"/>
          </SoloDemo>
          <GroupDemo>
            <RationaleBlock ctx="group"/>
          </GroupDemo>
        </>}
        spec={<ChatSpec name="Recommendation Rationale"
          appears="On demand (‘why this?’) beneath a venue/comparison/booking card."
          contains="2–4 evidence lines, what Vesper weighed, a tune affordance."
          primary="— (it’s an explanation, not an action)."
          secondary="Tune what I weigh."
          solo="Personal: ‘you saved Alfama, Yanaka…’ — names your own taste."
          group="Depersonalised: ‘the group skews early mornings’ — no individual’s taste exposed."
          privacy="MOST sensitive. Personal taste signals never shown in group; stay in 1:1."
          placement="A quiet left-ruled block under the card it explains — never a bubble."/>}/>

      {/* 10 · VOICE SEGMENT */}
      <CardSection id="cc10" n="10" title="Voice Segment"
        sub="A clip from voice mode, rendered as a chat artifact."
        pair={<>
          <SoloDemo line="Caught that — here’s what I heard." trailing="VOICE">
            <VoiceSegmentCard ctx="solo"/>
          </SoloDemo>
          <GroupDemo post={<div style={{ fontSize: 10, color: T.muteSoft, fontStyle: 'italic', fontFamily: T.serif, paddingLeft: 34 }}>shared only because you tapped “send clip”</div>}>
            <VoiceSegmentCard ctx="group"/>
          </GroupDemo>
        </>}
        spec={<ChatSpec name="Voice Segment"
          appears="After a voice prompt, or when a clip is referenced in the thread."
          contains="Waveform, duration, transcript text, play control."
          primary="Use this (1:1) / Play (group)."
          secondary="Edit transcript · redo · hide."
          solo="‘What I heard’ — editable transcript, private by default."
          group="Only present if explicitly shared; labelled as a shared clip."
          privacy="Voice is private. Never auto-posts to group; opt-in ‘send clip’ only."
          placement="Full-width object; below a note in 1:1."/>}/>

      {/* 11 · NARRATION */}
      <CardSection id="cc11" n="11" title="Narration / Guide"
        sub="Vesper guiding in the moment — prose with a soft audio control."
        pair={<>
          <SoloDemo line="" trailing="GUIDING">
            <NarrationCard ctx="solo"/>
          </SoloDemo>
          <GroupDemo>
            <NarrationCard ctx="group"/>
          </GroupDemo>
        </>}
        spec={<ChatSpec name="Narration / Guide"
          appears="During a trip / live walk; when Vesper narrates a place or route."
          contains="Guide prose, an audio scrubber, duration, continue control."
          primary="Continue (1:1) / Play for all (group)."
          secondary="Read instead · pause guiding."
          solo="Second-person, intimate (‘that’s the one you want’)."
          group="Shared guide; ‘play for all’; rarer, opt-in."
          privacy="Location-aware narration stays in 1:1 unless shared."
          placement="Full-width object; reads as prose, not a widget."/>}/>

      {/* 12 · ATLAS DRAFT */}
      <CardSection id="cc12" n="12" title="Memory / Atlas Draft"
        sub="A keepsake Vesper drafts — the handoff to Atlas."
        pair={<>
          <SoloDemo line="From your last trip — keep it if it’s right." trailing="FOR ATLAS">
            <AtlasDraftCard ctx="solo"/>
          </SoloDemo>
          <GroupDemo>
            <AtlasDraftCard ctx="group"/>
          </GroupDemo>
        </>}
        spec={<ChatSpec name="Memory / Atlas Draft"
          appears="After a trip, or when a moment is worth keeping."
          contains="Postcard preview, title, one-line caption, Atlas destination."
          primary="Keep it (1:1) / Add to album (group)."
          secondary="Refine · not this time · preview."
          solo="Personal memory; routes to your private Atlas."
          group="Routes to a shared trip album; caption depersonalised."
          privacy="Personal reflections softened; only the shared-album version posts to group."
          placement="Full-width object; the postcard is the hero."/>}/>

      {/* 13 · RESEARCH */}
      <CardSection id="cc13" n="13" title="Research Progress / Result"
        sub="Vesper working in the thread — progress, then results."
        pair={<>
          <SoloDemo line="On it — give me a couple of minutes." trailing="WORKING">
            <ResearchCard ctx="solo"/>
          </SoloDemo>
          <GroupDemo>
            <ResearchCard ctx="group"/>
          </GroupDemo>
        </>}
        spec={<ChatSpec name="Research Progress / Result"
          appears="When Vesper kicks off a longer task inside the conversation."
          contains="Ordered steps with state, a progress bar, ETA, result entry."
          primary="Watch it work."
          secondary="Notify me · finish without me · notify all (group)."
          solo="First-person (‘I’m looking into it’)."
          group="Attributed (‘Vesper is researching for the group’); notify-all option."
          privacy="Search terms tied to private prefs are summarised, not shown verbatim, in group."
          placement="Full-width object; collapses to a result card when done."/>}/>

      {/* 14 · PRIVACY HANDOFF */}
      <CardSection id="cc14" n="14" title="Privacy / Private-Handoff"
        sub="Moving a sensitive thread from the group into 1:1."
        pair={<>
          <SoloDemo line="" trailing="PRIVATE">
            <PrivacyHandoffCard ctx="solo"/>
          </SoloDemo>
          <GroupDemo>
            <PrivacyHandoffCard ctx="group"/>
          </GroupDemo>
        </>}
        spec={<ChatSpec name="Privacy / Private-Handoff"
          appears="When a topic (budget, a surprise, personal constraints) shouldn’t be public."
          contains="What’s sensitive, the offer to continue privately, a clear stay/move choice."
          primary="Continue privately (group) / Got it (1:1)."
          secondary="Keep in group."
          solo="Reassurance: ‘only you can see this’."
          group="Violet lock accent; offers to move the thread to your 1:1 with Vesper."
          privacy="THIS IS the privacy control. Nothing sensitive is shown until the user chooses."
          placement="Full-width object; violet-tinted, the one place violet appears."/>}/>

      {/* 15 · ERROR */}
      <CardSection id="cc15" n="15" title="Error / Recovery"
        sub="When something fails — calm, honest, with a way forward."
        pair={<>
          <SoloDemo line="" trailing="HEADS UP">
            <ErrorCard ctx="solo"/>
          </SoloDemo>
          <GroupDemo>
            <ErrorCard ctx="group"/>
          </GroupDemo>
        </>}
        spec={<ChatSpec name="Error / Recovery"
          appears="A booking fails, a hold expires, a service is unreachable."
          contains="What happened, reassurance (nothing charged), 1–2 ways forward."
          primary="Try again (1:1) / Re-hold for all (group)."
          secondary="Find two alike · leave it."
          solo="Plain and calm; first-person ownership."
          group="States the failure without exposing private detail; reassures no one was charged."
          privacy="Never expose payment/personal cause in group; just the shared-relevant fact."
          placement="Full-width object; oxblood tint, never a red alarm."/>}/>

    </React.Fragment>
  );
}

window.ChatSections = ChatSections;
