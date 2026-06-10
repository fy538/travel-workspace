// ═══════════════════════════════════════════════════════════════
// VESPER · CHAT — the two thread layouts, fully fleshed.
//   Editorial Scroll (default) — the conversation as a serif column.
//   Document Edit (when iterating on a real draft) — the draft IS
//   the conversation; turns become inline edits + margin notes.
// Reuses scaffold atoms + VesperMark.
// ═══════════════════════════════════════════════════════════════

// Inline structured card (a tool result living in the prose flow).
function FoundRyokan() {
  const rows = [
    { n: 'Sawanoya', sub: 'Yanaka · an old house', tag: 'SLOW' },
    { n: 'Hatago', sub: 'Shibuya · quiet alley', tag: 'QUIET' },
    { n: 'Sukeroku', sub: 'Asakusa · morning light', tag: 'WARM' },
  ];
  return (
    <div style={{ padding: 12, background: T.cardWarm, borderRadius: 12, border: `0.5px solid ${T.hairline}` }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
        <VesperMark s={11}/>
        <span style={{ fontSize: 9, color: T.goldDeep, letterSpacing: 1.4, fontWeight: 700 }}>FOUND · 3 RYOKAN</span>
        <span style={{ marginLeft: 'auto', fontFamily: T.mono, fontSize: 8.5, color: T.muteSoft, letterSpacing: 1.1 }}>FROM 47 SEARCHED</span>
      </div>
      <div style={{ marginTop: 8, display: 'flex', flexDirection: 'column', gap: 6 }}>
        {rows.map((r, i) => (
          <div key={i} style={{ display: 'grid', gridTemplateColumns: '1fr auto auto', gap: 8, alignItems: 'center', padding: '8px 10px', background: T.bg, borderRadius: 8 }}>
            <div>
              <div style={{ fontFamily: T.serif, fontSize: 13.5, color: T.ink, fontWeight: 500, letterSpacing: -0.1, lineHeight: 1 }}>{r.n}</div>
              <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 11.5, color: T.mute, marginTop: 2 }}>{r.sub}</div>
            </div>
            <span style={{ padding: '2px 6px', background: 'rgba(176,133,58,0.10)', color: T.goldDeep, fontSize: 8, letterSpacing: 1.2, fontWeight: 700, borderRadius: 3 }}>{r.tag}</span>
            <span style={{ color: T.muteSoft, fontSize: 11 }}>→</span>
          </div>
        ))}
      </div>
    </div>
  );
}

// ─── 1 · EDITORIAL SCROLL (default) ─────────────────────────────
function ThreadEditorial() {
  return (
    <ChatScreen
      header={<ChatHeader title="Tokyo, in May" sub="PRIVATE · TRIP-LINKED"/>}
      composer={<ChatComposer placeholder="Reply, or pick one above…"/>}
    >
      <DayDivider>Yesterday</DayDivider>

      {/* an earlier, settled turn — reads quiet, compact */}
      <UserPill time="9:52 PM">What’s the trip actually missing right now?</UserPill>
      <VesperProse time="9:53 PM">
        Only the nights in the middle. Flights and the first two days are set —
        it’s 5–7 that are still open.
      </VesperProse>

      <DayDivider>Today</DayDivider>

      {/* the live exchange */}
      <UserPill time="9:59 PM">Find a ryokan I’d actually want, nights 5–7</UserPill>
      <VesperProse>
        Three I’d actually book. <em>Sawanoya</em> in Yanaka is the slowest — an
        old house, mornings on the river. <em>Hatago</em> is the quietest alley I
        could find in Shibuya, and Sukeroku has the morning light you keep saving.
      </VesperProse>
      <FoundRyokan/>
      <SuggestChips/>
      <div style={{ fontSize: 8.5, color: T.muteSoft, letterSpacing: 1.2, fontWeight: 600 }}>10:01 PM · VESPER</div>
    </ChatScreen>
  );
}

// ─── 2 · DOCUMENT EDIT (iterating on a real draft) ──────────────
function ThreadDocument() {
  return (
    <ChatScreen
      header={<ChatHeader title="Tokyo, in May" sub="PRIVATE · TRIP-LINKED" draft="DRAFT · v4" right="menu"/>}
      composer={<ChatComposer placeholder="Edit the draft, or ask…"/>}
    >
      <div>
        <VesperEyebrow trailing="EDITING TOGETHER"/>
        <h2 style={{ fontFamily: T.serif, fontWeight: 500, fontSize: 27, color: T.ink, margin: '8px 0 0', letterSpacing: -0.6, lineHeight: 1.02 }}>
          Tokyo, in May — <span style={{ fontStyle: 'italic' }}>a quiet itinerary.</span>
        </h2>
      </div>

      {/* the draft body — edits shown inline */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
        <p style={{ fontFamily: T.serif, fontSize: 14.5, color: T.inkSoft, margin: 0, lineHeight: 1.5 }}>
          <b style={{ color: T.ink }}>Days 1–2.</b> Land soft. Yanaka, the old house. Sentō in the evening. <em>No alarms.</em>
        </p>
        <p style={{ fontFamily: T.serif, fontSize: 14.5, color: T.inkSoft, margin: 0, lineHeight: 1.5 }}>
          <b style={{ color: T.ink }}>Days 3–4.</b> Stay east — Yanaka mornings, Kuramae in the afternoon. <span style={{ background: 'rgba(176,133,58,0.18)', padding: '0 3px', borderRadius: 2, color: T.goldDeep }}>One long lunch, no plan after.</span>
        </p>
        <p style={{ fontFamily: T.serif, fontSize: 14.5, color: T.inkSoft, margin: 0, lineHeight: 1.5 }}>
          <b style={{ color: T.ink }}>Days 5–7.</b> <span style={{ textDecoration: 'underline', textDecorationColor: TR.ink, textUnderlineOffset: 3, textDecorationThickness: 1.5, color: T.ink }}>Ryokan — Sawanoya, booked.</span> Mornings by the river, evenings open.
        </p>
      </div>

      {/* margin annotation — the user's question, penciled in the margin */}
      <div style={{ padding: '2px 0 2px 14px', borderLeft: `2px solid ${TR.ink}` }}>
        <p style={{ margin: 0, fontFamily: T.serif, fontStyle: 'italic', fontSize: 14.5, color: T.ink, lineHeight: 1.4, letterSpacing: -0.05 }}>
          “can we skip days 3–4 and lean longer in Yanaka instead?”
        </p>
        <div style={{ marginTop: 5, fontSize: 8.5, color: T.muteSoft, letterSpacing: 1.4, fontWeight: 700 }}>— YOU · 10:14</div>
      </div>

      {/* Vesper's next-draft reply */}
      <div style={{ padding: '12px 14px', background: T.cardSoft, borderRadius: 12, border: `0.5px solid ${T.hairline}` }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
          <VesperMark s={11}/>
          <span style={{ fontSize: 9, color: T.goldDeep, letterSpacing: 1.4, fontWeight: 700 }}>REWROTE DAYS 3–4 · v5</span>
        </div>
        <p style={{ margin: '7px 0 9px', fontFamily: T.serif, fontSize: 13.5, color: T.inkSoft, lineHeight: 1.4, letterSpacing: -0.05 }}>
          Done — two more mornings in Yanaka, dropped the crossing. Same total nights.
        </p>
        <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
          <span style={{ padding: '6px 12px', fontSize: 11.5, fontWeight: 600, color: T.cardWarm, background: TR.ink, borderRadius: 999, letterSpacing: -0.05 }}>Keep the change</span>
          <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12, color: T.inkSoft }}>show me both</span>
          <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12, color: T.mute }}>undo</span>
        </div>
      </div>
    </ChatScreen>
  );
}

Object.assign(window, { FoundRyokan, ThreadEditorial, ThreadDocument });
