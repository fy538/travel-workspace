// ═══════════════════════════════════════════════════════════════
// VESPER · CHAT — Group room. Members speak in avatar pills; Vesper
// writes prose TO the group (no bubble). Object-types: member
// message · public question to Vesper · a decision · a plan-change ·
// a booking event · the dignified-exception (a private turn
// referenced without exposing it). Header: trip + member stack.
// Reuses GroupTurn, UserBubble, Avatar, MemberStack, card kit.
// ═══════════════════════════════════════════════════════════════

// A quiet system event line (plan-change, booking) — centered, calm.
function GroupEvent({ icon = 'check', children, tint = T.mute }) {
  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: 9, justifyContent: 'center', padding: '2px 0' }}>
      <span style={{ flex: 1, height: 1, background: T.hairThin }}/>
      <span style={{ display: 'inline-flex', alignItems: 'center', gap: 6, fontSize: 11, color: tint, fontStyle: 'italic', fontFamily: T.serif }}>
        {ChatGlyph[icon] ? ChatGlyph[icon](tint) : null}
        {children}
      </span>
      <span style={{ flex: 1, height: 1, background: T.hairThin }}/>
    </div>
  );
}

// Vesper writing TO the group — prose, attributed, never a bubble.
function GroupVesperProse({ time = '10:16', children, to = 'the group' }) {
  return (
    <div style={{ display: 'flex', gap: 8, alignItems: 'flex-start' }}>
      <Avatar who="vesper"/>
      <div style={{ flex: 1, minWidth: 0 }}>
        <div style={{ display: 'flex', alignItems: 'baseline', gap: 8, marginBottom: 4 }}>
          <span style={{ fontSize: 12, fontWeight: 600, color: T.goldDeep, letterSpacing: -0.1 }}>Vesper</span>
          <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 10.5, color: T.muteSoft }}>to {to}</span>
          <span style={{ fontFamily: T.mono, fontSize: 8.5, color: T.muteSoft, letterSpacing: 1 }}>{time}</span>
        </div>
        <p style={{ fontFamily: T.serif, fontSize: 15, color: T.ink, lineHeight: 1.42, margin: 0, letterSpacing: -0.1 }}>{children}</p>
      </div>
    </div>
  );
}

// THE DIGNIFIED EXCEPTION — a private turn referenced, never exposed.
function DignifiedException() {
  return (
    <div style={{ display: 'flex', gap: 8, alignItems: 'flex-start' }}>
      <Avatar who="vesper"/>
      <div style={{ flex: 1 }}>
        <div style={{ display: 'flex', alignItems: 'baseline', gap: 8, marginBottom: 5 }}>
          <span style={{ fontSize: 12, fontWeight: 600, color: T.goldDeep }}>Vesper</span>
          <span style={{ fontFamily: T.mono, fontSize: 8.5, color: T.muteSoft, letterSpacing: 1 }}>10:18</span>
        </div>
        <div style={{ padding: '11px 13px', borderRadius: 12, background: T.cardSoft, border: `0.5px dashed ${T.muteSoft}` }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 7, marginBottom: 6 }}>
            <PrivacyTag>handled privately</PrivacyTag>
          </div>
          <p style={{ fontFamily: T.serif, fontSize: 13.5, color: T.inkSoft, lineHeight: 1.4, margin: 0, fontStyle: 'italic' }}>
            One of you asked me something just for them — sorted, and it doesn’t change the plan. Carry on.
          </p>
        </div>
      </div>
    </div>
  );
}

// ─── FULL GROUP ROOM ────────────────────────────────────────────
function GroupRoom() {
  return (
    <ChatScreen
      header={<ChatHeader title="Tokyo · 4 of us" sub="GROUP · MAY 5–13" right="members" members={<MemberStack/>}/>}
      composer={<ChatComposer placeholder="Message the group…"/>}
    >
      <DayDivider>Today</DayDivider>

      {/* member message */}
      <UserBubble who="ana" time="10:12">can we lock the ryokan tonight? prices are creeping</UserBubble>

      {/* public question to Vesper */}
      <UserBubble who="theo" time="10:13">@Vesper what are our actual options for nights 5–7?</UserBubble>

      {/* Vesper prose to the group */}
      <GroupVesperProse time="10:14">
        Two that fit all four of you — both quiet, both east. Sawanoya’s the slower one; Hatago’s the closer-in. Worth a quick vote before they move.
      </GroupVesperProse>

      {/* a decision — public vote card */}
      <GroupTurn who="vesper" time="10:14">
        <DecisionVoteCard ctx="group"/>
      </GroupTurn>

      {/* member reactions */}
      <UserBubble who="tiger" time="10:15">sawanoya for me</UserBubble>

      {/* a plan-change event */}
      <GroupEvent icon="diff" tint={TR.ink}>Ana moved day 4 to stay east — everyone’s itinerary updated</GroupEvent>

      {/* a booking event */}
      <GroupEvent icon="check" tint="#3D7050">Sawanoya booked · 3 nights · split 4 ways</GroupEvent>

      {/* the dignified exception */}
      <DignifiedException/>
    </ChatScreen>
  );
}

// ─── GROUP · object-type study (a second screen) ────────────────
function GroupObjects() {
  return (
    <ChatScreen
      header={<ChatHeader title="Tokyo · 4 of us" sub="GROUP · MAY 5–13" right="members" members={<MemberStack/>}/>}
      composer={<ChatComposer placeholder="Message the group…"/>}
    >
      <GroupEvent icon="cal">Theo added a stop to Day 3</GroupEvent>
      <UserBubble who="theo" time="9:40">found a udon place near the cemetery, adding it</UserBubble>
      <GroupVesperProse time="9:41">
        Good call — it’s a five-minute walk from Kayaba, so the morning still flows. I slotted it at one.
      </GroupVesperProse>
      <GroupTurn who="vesper" time="9:41">
        <ItineraryCard ctx="group"/>
      </GroupTurn>
      <GroupEvent icon="card" tint="#3D7050">Theo paid ¥9,200 · udon · added to the split</GroupEvent>
      <UserBubble who="ana" time="9:44">love it</UserBubble>
    </ChatScreen>
  );
}

Object.assign(window, {
  GroupEvent, GroupVesperProse, DignifiedException, GroupRoom, GroupObjects,
});
