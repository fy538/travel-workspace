// ═══════════════════════════════════════════════════════════════
// THE BLANK TRIP — 3 editorial takes on the genuinely empty state
// (the moment you tap +). Type-led, no form chrome. Reuses DR,
// StyleRiso, PFrame, EdKick, ed.
// ═══════════════════════════════════════════════════════════════

const caret = <span style={{ display: 'inline-block', width: 2, height: '0.82em', background: DR.goldDeep, marginLeft: 2, verticalAlign: '-0.06em' }}/>;

// ─────────────────────────────────────────────────────────────────
// B1 · FRONTISPIECE (blank) — you name it first, like a journal cover.
// Structured-quiet. The colophon waits in faint italic.
// ─────────────────────────────────────────────────────────────────
function BlankFrontispiece() {
  return (
    <PFrame>
      <div style={{ position: 'relative', height: 132, marginTop: -40 }}>
        <div style={{ position: 'absolute', inset: 0, opacity: 0.22 }}><StyleRiso w={393} h={132}/></div>
        <div style={{ position: 'absolute', inset: 0, background: `linear-gradient(to bottom, rgba(239,234,224,0.1), ${DR.paper})` }}/>
        <div style={{ position: 'absolute', top: 50, left: 22, right: 22, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke={DR.soft} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><path d="M18 6 6 18M6 6l12 12"/></svg>
          <span style={{ fontFamily: DR.mono, fontSize: 9, letterSpacing: 2.6, color: DR.mute, fontWeight: 600 }}>A NEW FOLIO</span>
          <div style={{ width: 20 }}/>
        </div>
      </div>
      <div style={{ padding: '8px 26px 0', textAlign: 'center' }}>
        <EdKick c={DR.goldDeep}>Vesper</EdKick>
        <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 17, color: DR.mute, margin: '13px 0 30px', lineHeight: 1.4 }}>Every trip begins with a name.</p>
        <h1 style={{ fontFamily: DR.serif, fontSize: 33, fontWeight: 500, letterSpacing: -0.8, lineHeight: 1, color: DR.faint, margin: 0, fontStyle: 'italic' }}>Name a place…{caret}</h1>
      </div>
      <div style={{ padding: '40px 26px 0' }}>
        <div style={{ borderTop: ed.rule, borderBottom: ed.rule }}>
          {[['WHEN', 'the dates'], ['WITH', 'who’s coming'], ['THE FEEL', 'a tone']].map(([k, v], i) => (
            <div key={k} style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', padding: '13px 0', borderTop: i ? ed.hair : 'none' }}>
              <EdKick>{k}</EdKick>
              <span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 15.5, color: DR.faint }}>{v}</span>
            </div>
          ))}
        </div>
      </div>
      <div style={{ padding: '28px 26px 0', textAlign: 'center' }}>
        <span style={{ fontFamily: DR.serif, fontSize: 18, fontWeight: 500, color: DR.faint, letterSpacing: -0.2, borderBottom: `1.5px solid ${DR.hair}`, paddingBottom: 3 }}>Open the folio</span>
        <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 14, color: DR.mute, margin: '20px 0 0' }}>— or just tell me about it →</p>
      </div>
    </PFrame>
  );
}

// ─────────────────────────────────────────────────────────────────
// B2 · THE OPENING QUESTION (blank) — conversation-first. Vesper asks,
// offers a few evocative openings, composer waits below.
// ─────────────────────────────────────────────────────────────────
function BlankQuestion() {
  const whispers = ['a long weekend somewhere warm', 'the one we keep putting off', 'back to Lisbon, slower'];
  return (
    <PFrame>
      <div style={{ position: 'relative', height: 86, marginTop: -40, display: 'flex', alignItems: 'flex-end', justifyContent: 'space-between', padding: '0 22px' }}>
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke={DR.soft} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><path d="M18 6 6 18M6 6l12 12"/></svg>
        <span style={{ fontFamily: DR.mono, fontSize: 9, letterSpacing: 2.6, color: DR.mute, fontWeight: 600, paddingBottom: 4 }}>A NEW FOLIO</span>
        <div style={{ width: 20 }}/>
      </div>
      <div style={{ padding: '30px 26px 0' }}>
        <EdKick c={DR.goldDeep}>Vesper</EdKick>
        <div style={{ height: 14 }}/>
        <h1 style={{ fontFamily: DR.serif, fontSize: 30, fontWeight: 500, letterSpacing: -0.6, lineHeight: 1.12, color: DR.ink, margin: 0 }}>Where shall we begin?</h1>
        <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 15.5, color: DR.mute, margin: '10px 0 0', lineHeight: 1.45 }}>A place, a feeling, who’s coming — anything at all, and I’ll start the folio.</p>
      </div>
      {/* evocative openings — editorial lines, not chips */}
      <div style={{ padding: '26px 26px 0' }}>
        <EdKick>Or pick up a thread</EdKick>
        <div style={{ marginTop: 6 }}>
          {whispers.map((w, i) => (
            <div key={i} style={{ display: 'flex', alignItems: 'baseline', gap: 10, padding: '13px 0', borderTop: i ? ed.hair : ed.rule }}>
              <span style={{ fontFamily: DR.serif, fontSize: 16, color: DR.faint }}>—</span>
              <span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 17, color: DR.soft, letterSpacing: -0.2 }}>{w}</span>
            </div>
          ))}
        </div>
      </div>
      {/* composer */}
      <div style={{ padding: '24px 24px 0' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 12, paddingTop: 15, borderTop: ed.rule }}>
          <span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 15, color: DR.faint, flex: 1 }}>say it however you like…</span>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke={DR.goldDeep} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/></svg>
        </div>
      </div>
    </PFrame>
  );
}

// ─────────────────────────────────────────────────────────────────
// B3 · THE THRESHOLD (blank) — image-first, cinematic. A dim
// atmospheric cover with one line and a single hairline input.
// ─────────────────────────────────────────────────────────────────
function BlankThreshold() {
  return (
    <div style={{ width: 393, borderRadius: 30, overflow: 'hidden', border: `0.5px solid ${DR.hair}`, boxShadow: '0 30px 60px -30px rgba(0,0,0,0.3)', position: 'relative', height: 720, background: DR.ink }}>
      <div style={{ position: 'absolute', inset: 0, filter: 'saturate(0.85) brightness(0.7)' }}><StyleRiso w={393} h={720}/></div>
      <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to bottom, rgba(20,14,9,0.5) 0%, rgba(20,14,9,0.15) 40%, rgba(20,14,9,0.88) 100%)' }}/>
      {/* top chrome */}
      <div style={{ position: 'absolute', top: 50, left: 22, right: 22, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,0.9)" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><path d="M18 6 6 18M6 6l12 12"/></svg>
        <span style={{ fontFamily: DR.mono, fontSize: 9, letterSpacing: 2.6, color: 'rgba(255,255,255,0.7)', fontWeight: 600 }}>A NEW FOLIO</span>
        <div style={{ width: 20 }}/>
      </div>
      {/* the line, low */}
      <div style={{ position: 'absolute', left: 26, right: 26, bottom: 130 }}>
        <span style={{ fontFamily: DR.mono, fontSize: 9.5, letterSpacing: 2.6, color: 'rgba(255,255,255,0.75)', fontWeight: 600 }}>VESPER</span>
        <h1 style={{ fontFamily: DR.serif, fontSize: 40, fontWeight: 500, fontStyle: 'italic', letterSpacing: -0.8, lineHeight: 1.0, color: '#fff', margin: '12px 0 0' }}>Begin somewhere.</h1>
      </div>
      {/* hairline input */}
      <div style={{ position: 'absolute', left: 26, right: 26, bottom: 60 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 12, paddingBottom: 11, borderBottom: '0.5px solid rgba(255,255,255,0.4)' }}>
          <span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 17, color: 'rgba(255,255,255,0.6)', flex: 1 }}>a place, or a feeling…{caret}</span>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,0.85)" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/></svg>
        </div>
        <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 13.5, color: 'rgba(255,255,255,0.55)', margin: '14px 0 0' }}>— or let Vesper suggest one →</p>
      </div>
    </div>
  );
}

Object.assign(window, { BlankFrontispiece, BlankQuestion, BlankThreshold });
