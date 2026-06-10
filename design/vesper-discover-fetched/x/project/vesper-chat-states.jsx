// ═══════════════════════════════════════════════════════════════
// VESPER · CHAT — every state. Cold-start · composing/optimistic ·
// attachments · thinking (escalating editorial copy) · streaming ·
// tool-result · suggested-next · error/retry · long thread.
// Reuses scaffold atoms + FoundRyokan.
// ═══════════════════════════════════════════════════════════════

// ─── COLD START · empty thread (standalone Vesper) ──────────────
function StateCold() {
  const starters = [
    ['Plan a quiet week somewhere', 'pin'],
    ['What should I do this weekend?', 'cal'],
    ['Somewhere warm, under 5 hours', 'route'],
    ['Read me something about Lisbon', 'guide'],
  ];
  return (
    <ChatScreen
      header={<ChatHeader title="Vesper" sub="JUST VESPER"/>}
      composer={<ChatComposer placeholder="Tell Vesper one place, or one mood…"/>}
      fade={false}
    >
      <div style={{ paddingTop: 28, textAlign: 'center' }}>
        <div style={{ display: 'inline-flex', width: 52, height: 52, borderRadius: 999, background: 'rgba(176,133,58,0.12)', alignItems: 'center', justifyContent: 'center', marginBottom: 16 }}>
          <VesperMark s={26} c={T.gold}/>
        </div>
        <h2 style={{ fontFamily: T.serif, fontSize: 25, fontWeight: 500, color: T.ink, letterSpacing: -0.5, lineHeight: 1.2, margin: 0 }}>
          Where are we going?
        </h2>
        <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 14.5, color: T.mute, lineHeight: 1.5, margin: '10px 28px 0' }}>
          A place, a mood, a half-formed idea — I’ll take it from anywhere.
        </p>
      </div>
      <div style={{ marginTop: 8, display: 'flex', flexDirection: 'column', gap: 9 }}>
        {starters.map(([t, g]) => (
          <div key={t} style={{ display: 'flex', alignItems: 'center', gap: 12, padding: '13px 15px', background: T.cardWarm, borderRadius: 14, border: `0.5px solid ${T.hairline}` }}>
            <span style={{ color: T.goldDeep, display: 'flex' }}>{ChatGlyph[g](T.goldDeep)}</span>
            <span style={{ flex: 1, fontFamily: T.serif, fontSize: 15.5, color: T.inkSoft, letterSpacing: -0.1 }}>{t}</span>
            <span style={{ color: T.muteSoft, fontSize: 13 }}>↑</span>
          </div>
        ))}
      </div>
    </ChatScreen>
  );
}

// ─── COMPOSING · typing + optimistic prior send + attachments ───
function StateComposing() {
  const photos = (
    <div style={{ display: 'flex', gap: 6, justifyContent: 'flex-end', marginBottom: 7 }}>
      {[0, 1, 2].map((i) => <div key={i} style={{ width: 54, height: 54, borderRadius: 10, border: `0.5px solid ${T.hairline}`, background: ['linear-gradient(135deg,#b9aa88,#8c7c5e)', 'linear-gradient(135deg,#c4b69c,#9a8a6c)', 'linear-gradient(135deg,#aa9c80,#7e6f54)'][i] }}/>)}
    </div>
  );
  return (
    <ChatScreen
      header={<ChatHeader title="Tokyo, in May" sub="PRIVATE · TRIP-LINKED"/>}
      composer={<ChatComposer state="typing" value="and somewhere near the fish market for breakfast" attachments={0}/>}
    >
      <VesperProse time="10:01 PM">
        Three I’d actually book — all quiet, all east. Want me to hold one while we look?
      </VesperProse>
      <UserPill time="" optimistic attach={photos}>
        these are the rooms I loved last time — anything like them?
      </UserPill>
    </ChatScreen>
  );
}

// ─── THINKING · escalating editorial "working" copy ─────────────
function ThinkingLine({ t, label, active, done }) {
  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
      <span style={{ fontFamily: T.mono, fontSize: 8.5, color: T.muteSoft, letterSpacing: 1, width: 26 }}>{t}</span>
      <span style={{ width: 6, height: 6, borderRadius: 6, background: done ? T.gold : (active ? T.gold : T.muteSoft), opacity: done ? 0.5 : 1 }}/>
      <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: active ? 15.5 : 13.5, color: active ? T.ink : T.muteSoft, lineHeight: 1.3 }}>{label}</span>
    </div>
  );
}
function StateThinking() {
  return (
    <ChatScreen
      header={<ChatHeader title="Tokyo, in May" sub="PRIVATE · TRIP-LINKED"/>}
      composer={<ChatComposer placeholder="Reply, or pick one above…"/>}
    >
      <UserPill time="10:14 PM">find a ryokan I’d actually want, nights 5–7</UserPill>
      <div>
        <VesperEyebrow/>
        <div style={{ marginTop: 12, display: 'flex', flexDirection: 'column', gap: 13 }}>
          <ThinkingLine t="0:02" label="Looking…" done/>
          <ThinkingLine t="0:09" label="Reading the ones that fit how you travel — this is worth getting right." active/>
        </div>
        <div style={{ marginTop: 16, paddingTop: 13, borderTop: `0.5px solid ${T.hairThin}` }}>
          <div style={{ fontSize: 8.5, color: T.muteSoft, letterSpacing: 1.6, fontWeight: 700, marginBottom: 7 }}>AT ~20s, IT DEEPENS — NEVER RAW TOOL CHATTER</div>
          <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 14, color: T.mute, lineHeight: 1.45, margin: 0 }}>
            “Still with it — comparing a few I almost didn’t include, because the obvious ones aren’t you.”
          </p>
        </div>
      </div>
    </ChatScreen>
  );
}

// ─── STREAMING · prose arriving with a caret ────────────────────
function StateStreaming() {
  return (
    <ChatScreen
      header={<ChatHeader title="Tokyo, in May" sub="PRIVATE · TRIP-LINKED"/>}
      composer={<ChatComposer placeholder="Reply, or pick one above…"/>}
    >
      <UserPill time="10:14 PM">find a ryokan I’d actually want, nights 5–7</UserPill>
      <VesperProse caret>
        Three I’d actually book. <em>Sawanoya</em> in Yanaka is the slowest — an old
        house, mornings on the river. <em>Hatago</em> is the quietest alley I could
        find in Shibuya, and
      </VesperProse>
    </ChatScreen>
  );
}

// ─── TOOL RESULT · the found-card settled, with suggested next ──
function StateToolResult() {
  return (
    <ChatScreen
      header={<ChatHeader title="Tokyo, in May" sub="PRIVATE · TRIP-LINKED"/>}
      composer={<ChatComposer placeholder="Reply, or pick one above…"/>}
    >
      <UserPill time="10:14 PM">find a ryokan I’d actually want, nights 5–7</UserPill>
      <VesperProse>
        Three I’d actually book — all quiet, all east. The river mornings are the
        thread between them.
      </VesperProse>
      <FoundRyokan/>
      <SuggestChips items={['hold Sawanoya', 'show ¥ tier', 'why these three', 'somewhere quieter']}/>
      <div style={{ fontSize: 8.5, color: T.muteSoft, letterSpacing: 1.2, fontWeight: 600 }}>10:15 PM · VESPER</div>
    </ChatScreen>
  );
}

// ─── ERROR / RECOVERY · calm, named, with a way forward ─────────
function StateError() {
  return (
    <ChatScreen
      header={<ChatHeader title="Tokyo, in May" sub="PRIVATE · TRIP-LINKED"/>}
      composer={<ChatComposer placeholder="Reply, or try again…"/>}
    >
      <UserPill time="10:14 PM" optimistic>find a ryokan I’d actually want, nights 5–7</UserPill>
      <div>
        <VesperEyebrow/>
        <p style={{ fontFamily: T.serif, fontSize: 16, color: T.ink, lineHeight: 1.46, margin: '9px 0 0', letterSpacing: -0.1 }}>
          I lost the connection halfway through looking — nothing’s booked, and your
          message is safe. Want me to pick the search back up?
        </p>
        <div style={{ marginTop: 12, display: 'flex', alignItems: 'center', gap: 10 }}>
          <span style={{ padding: '7px 14px', fontSize: 12, fontWeight: 600, color: T.cardWarm, background: T.ink, borderRadius: 999, display: 'inline-flex', alignItems: 'center', gap: 6 }}>
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M4 12a8 8 0 1 1 2.3 5.6M4 12V7M4 17l2.3.6"/></svg>
            Try again
          </span>
          <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12.5, color: T.mute }}>edit the message</span>
        </div>
      </div>
    </ChatScreen>
  );
}

// ─── LONG THREAD · day dividers · load-earlier · scroll-to-latest ─
function StateLong() {
  return (
    <ChatScreen
      header={<ChatHeader title="Tokyo, in May" sub="PRIVATE · TRIP-LINKED"/>}
      composer={<ChatComposer placeholder="Reply…"/>}
    >
      <div style={{ textAlign: 'center' }}>
        <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12.5, color: T.mute, padding: '5px 14px', border: `0.5px solid ${T.hairline}`, borderRadius: 999, background: T.cardWarm }}>↑ load earlier · 3 days</span>
      </div>
      <DayDivider>Monday</DayDivider>
      <UserPill time="2:01 PM">is may actually a good time to go?</UserPill>
      <VesperProse time="2:02 PM">
        The best, quietly — before the rains, after the crowds. I’d lock the dates.
      </VesperProse>
      <DayDivider>Today</DayDivider>
      <UserPill time="10:14 PM">ok dates are set. now the ryokan.</UserPill>
      <VesperProse>
        Then this is the fun part. Three I’d actually book…
      </VesperProse>
      {/* scroll-to-latest pill floats above composer */}
      <div style={{ position: 'absolute', right: 4, bottom: 2, display: 'flex', alignItems: 'center', gap: 6, padding: '6px 12px', background: T.ink, color: T.cardWarm, borderRadius: 999, fontSize: 11, fontWeight: 600, boxShadow: '0 6px 16px -8px rgba(0,0,0,0.4)' }}>
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round"><path d="M6 9l6 6 6-6"/></svg>
        latest
      </div>
    </ChatScreen>
  );
}

Object.assign(window, {
  StateCold, StateComposing, StateThinking, StateStreaming,
  StateToolResult, StateError, StateLong,
});
