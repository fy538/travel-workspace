// ─────────────────────────────────────────────────────────────
// THE SEVEN FAMILY CARDS — rendered at full "Now card" width (~361).
// One language: paper objects, ochre for Vesper. One clear job per card.
// ─────────────────────────────────────────────────────────────

// 1 · NEEDS YOUR CALL — a decision docket. High confidence, clear primary.
function CardCall() {
  return (
    <CardShell fam="call" style={{ padding: 16 }}>
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
        <KindTag fam="call"/>
        <span style={{ fontFamily: T.mono, fontSize: 9, color: T.muteSoft, letterSpacing: 1.2, fontWeight: 600 }}>
          DECIDE BY FRI
        </span>
      </div>
      <h3 style={{
        fontFamily: T.serif, fontWeight: 500, fontSize: 21, color: T.ink,
        margin: '10px 0 4px', letterSpacing: -0.4, lineHeight: 1.1,
      }}>
        A ryokan for Tokyo, <span style={{ fontStyle: 'italic' }}>nights 5–7.</span>
      </h3>
      <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13, color: T.mute, margin: '0 0 12px', lineHeight: 1.35 }}>
        I narrowed forty-seven down to three that fit your week.
      </p>
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', gap: 8 }}>
        <WhyThis/>
        <ActionRow primary="Choose" secondary={['not now']}/>
      </div>
    </CardShell>
  );
}

// 2 · VESPER PREPARED — a work product. Reads like a folder/dossier.
function CardPrepared() {
  return (
    <CardShell fam="prepared" style={{ padding: 0 }}>
      {/* file tab */}
      <div style={{
        display: 'flex', alignItems: 'center', gap: 6,
        padding: '12px 16px 10px',
        borderBottom: `0.5px solid ${T.hairThin}`,
      }}>
        <KindTag fam="prepared"/>
        <span style={{ marginLeft: 'auto', fontFamily: T.mono, fontSize: 9, color: T.muteSoft, letterSpacing: 1.2, fontWeight: 600 }}>
          DRAFT · 6 STOPS
        </span>
      </div>
      <div style={{ padding: '12px 16px 16px' }}>
        <h3 style={{
          fontFamily: T.serif, fontWeight: 500, fontSize: 20, color: T.ink,
          margin: '0 0 10px', letterSpacing: -0.3, lineHeight: 1.1,
        }}>
          Tokyo, in May — <span style={{ fontStyle: 'italic' }}>a quiet itinerary.</span>
        </h3>
        {/* contents preview — like a table of contents */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: 5, marginBottom: 12 }}>
          {[
            ['01', 'Land soft · Yanaka, no alarms'],
            ['02', 'Shimokita morning, one bookshop'],
            ['03', 'Ryokan — picked with you'],
          ].map(([n, t]) => (
            <div key={n} style={{ display: 'grid', gridTemplateColumns: '20px 1fr', gap: 8, alignItems: 'baseline' }}>
              <span style={{ fontFamily: T.mono, fontSize: 9, color: T.muteSoft, letterSpacing: 1 }}>{n}</span>
              <span style={{ fontFamily: T.serif, fontSize: 13, color: T.inkSoft, letterSpacing: -0.1, lineHeight: 1.2 }}>{t}</span>
            </div>
          ))}
          <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 11, color: T.muteSoft, paddingLeft: 28 }}>
            + three more
          </div>
        </div>
        <ActionRow primary="Open the draft" primaryColor={T.goldDeep} secondary={['skim', 'not now']}/>
      </div>
    </CardShell>
  );
}

// 3 · LIVE COMPANION — present-tense, glanceable, situational.
function CardLive() {
  return (
    <CardShell fam="live" style={{ padding: 16 }}>
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
        <KindTag fam="live">RIGHT NOW · YANAKA</KindTag>
        <span style={{
          display: 'inline-flex', alignItems: 'center', gap: 5,
          fontFamily: T.mono, fontSize: 9, color: T.inkSoft, letterSpacing: 1, fontWeight: 600,
        }}>
          {/* tiny weather */}
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke={T.inkSoft} strokeWidth="1.6" strokeLinecap="round">
            <circle cx="12" cy="12" r="4"/><path d="M12 3v2M12 19v2M3 12h2M19 12h2M5.6 5.6l1.4 1.4M17 17l1.4 1.4"/>
          </svg>
          18° CLEAR
        </span>
      </div>
      <h3 style={{
        fontFamily: T.serif, fontWeight: 500, fontSize: 21, color: T.ink,
        margin: '10px 0 4px', letterSpacing: -0.4, lineHeight: 1.1,
      }}>
        You have an <span style={{ fontStyle: 'italic' }}>open hour.</span>
      </h3>
      <p style={{ fontFamily: T.serif, fontSize: 13.5, color: T.inkSoft, margin: '0 0 12px', lineHeight: 1.4, letterSpacing: -0.05 }}>
        Kayaba Coffee is 8 minutes east — pre-war kissaten, open till 11, the morning light you like.
      </p>
      <ActionRow primary="I’m in" secondary={['walk me there', 'else?']}/>
    </CardShell>
  );
}

// 4 · SIGNAL / PATTERN — interpretive, quiet, explainable.
function CardSignal() {
  return (
    <CardShell fam="signal" tint={T.cardSoft} style={{ padding: 16 }}>
      <KindTag fam="signal"/>
      <p style={{
        fontFamily: T.serif, fontSize: 17, color: T.ink, margin: '12px 0 0',
        lineHeight: 1.4, letterSpacing: -0.15,
      }}>
        You keep choosing <span style={{ fontStyle: 'italic' }}>quiet neighborhoods</span> before
        the landmarks — Alfama, Yanaka, Ribeira.
      </p>
      <div style={{
        marginTop: 12, display: 'flex', alignItems: 'center', justifyContent: 'space-between',
      }}>
        <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 11.5, color: T.mute }}>
          shall I lean into it?
        </span>
        <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
          <WhyThis label="What I saw"/>
          <span style={{ fontSize: 11, color: T.goldDeep, fontWeight: 600, letterSpacing: -0.05 }}>
            Yes →
          </span>
        </div>
      </div>
    </CardShell>
  );
}

// 5 · CAPTURE / MEMORY — soft, optional, Atlas handoff.
function CardCapture() {
  return (
    <CardShell fam="capture" style={{ padding: 14 }}>
      <div style={{ display: 'flex', gap: 12, alignItems: 'center' }}>
        {/* photo slip */}
        <div style={{ flexShrink: 0, position: 'relative', width: 76, height: 90 }}>
          <div style={{
            position: 'absolute', inset: 0, transform: 'rotate(-3deg)',
            background: T.cardWarm, borderRadius: 4, border: `0.5px solid ${T.hairline}`,
            boxShadow: '0 6px 14px -8px rgba(0,0,0,0.2)', padding: 4,
          }}>
            <div style={{ width: '100%', height: '100%', borderRadius: 2, overflow: 'hidden', border: `0.5px solid ${T.hairThin}` }}>
              <PostcardScene scene="porto"/>
            </div>
          </div>
        </div>
        <div style={{ flex: 1, minWidth: 0 }}>
          <KindTag fam="capture"/>
          <div style={{
            fontFamily: T.serif, fontWeight: 500, fontSize: 18, color: T.ink,
            letterSpacing: -0.3, lineHeight: 1.1, marginTop: 8,
          }}>
            Williamsburg, sunday
          </div>
          <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12, color: T.mute, marginTop: 4, lineHeight: 1.3 }}>
            twelve photos — could become a postcard.
          </div>
          <div style={{ marginTop: 10 }}>
            <ActionRow primary="Keep it" primaryColor={T.goldDeep} secondary={['later']}/>
          </div>
        </div>
      </div>
    </CardShell>
  );
}

// 6 · RESUME THREAD — continuity, not chat inbox. A dog-eared bookmark.
function CardResume() {
  return (
    <CardShell fam="resume" style={{ padding: 16 }}>
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
        <KindTag fam="resume"/>
        <span style={{ fontFamily: T.mono, fontSize: 9, color: T.muteSoft, letterSpacing: 1.2, fontWeight: 600 }}>
          TOKYO · 2H AGO
        </span>
      </div>
      <p style={{
        fontFamily: T.serif, fontStyle: 'italic', fontSize: 15.5, color: T.inkSoft,
        margin: '12px 0 0', lineHeight: 1.4, letterSpacing: -0.1,
        paddingLeft: 12, borderLeft: `2px solid ${T.hairline}`,
      }}>
        “…where to stay near Yanaka, somewhere quiet —”
      </p>
      <div style={{ marginTop: 12, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
        <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 11.5, color: T.muteSoft }}>
          you left it mid-thought
        </span>
        <span style={{ fontSize: 12, color: T.inkSoft, fontWeight: 600, letterSpacing: -0.05 }}>
          Pick it up →
        </span>
      </div>
    </CardShell>
  );
}

// 7 · STARTER / COLD START — generous, not homework.
function CardStarter() {
  return (
    <CardShell fam="starter" dashed style={{ padding: 16 }}>
      <KindTag fam="starter"/>
      <h3 style={{
        fontFamily: T.serif, fontWeight: 500, fontSize: 22, color: T.ink,
        margin: '10px 0 4px', letterSpacing: -0.4, lineHeight: 1.05,
      }}>
        Tell me <span style={{ fontStyle: 'italic' }}>one place</span> you’ve loved.
      </h3>
      <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13, color: T.mute, margin: '0 0 14px', lineHeight: 1.35 }}>
        That’s all I need to begin. We’ll build from there.
      </p>
      <div style={{ display: 'flex', gap: 6, flexWrap: 'wrap' }}>
        {['a city', 'a weekend', 'somewhere quiet'].map((c, i) => (
          <span key={c} style={{
            padding: '6px 11px', fontFamily: T.serif, fontStyle: 'italic',
            fontSize: 12.5, color: i === 0 ? T.cardWarm : T.inkSoft,
            background: i === 0 ? T.ink : 'transparent',
            borderRadius: 999, border: i === 0 ? 'none' : `0.5px solid ${T.hairline}`,
          }}>{c}</span>
        ))}
        <span style={{
          padding: '6px 11px', fontFamily: T.serif, fontStyle: 'italic',
          fontSize: 12.5, color: T.goldDeep, borderRadius: 999,
          border: `0.6px dashed ${T.gold}`, display: 'inline-flex', alignItems: 'center', gap: 5,
        }}>
          <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke={T.goldDeep} strokeWidth="1.8" strokeLinecap="round">
            <rect x="9" y="3" width="6" height="12" rx="3"/><path d="M5 11c0 4 3 7 7 7s7-3 7-7M12 18v3"/>
          </svg>
          say it
        </span>
      </div>
    </CardShell>
  );
}

Object.assign(window, {
  CardCall, CardPrepared, CardLive, CardSignal, CardCapture, CardResume, CardStarter,
});
