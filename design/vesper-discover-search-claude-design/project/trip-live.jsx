// ═══════════════════════════════════════════════════════════════
// LIVE HOME · during the trip — editorial, in-the-moment. The home
// stops being a planner and becomes a companion for the next hour:
// reads the clock + place, one thing at a time, voice + "save a
// moment" the two gestures, logistics demoted to a whisper.
// Three postures: The Hour · The Dispatch · The Margin.
// Reuses DR, StyleRiso, EdKick, ed, Ppl/CASTD, PFrame.
// ═══════════════════════════════════════════════════════════════

const LH = 852;
const LIVE_ICON = {
  back: <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,0.92)" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><path d="M14 6l-6 6 6 6"/></svg>,
  backDk: <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#2C2622" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><path d="M14 6l-6 6 6 6"/></svg>,
  dots: (c) => <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.6" strokeLinecap="round"><circle cx="5" cy="12" r="1.4"/><circle cx="12" cy="12" r="1.4"/><circle cx="19" cy="12" r="1.4"/></svg>,
  mic: (c) => <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/></svg>,
  save: (c) => <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><path d="M6 4h12v17l-6-4-6 4z"/></svg>,
};

// Two editorial gestures (not big buttons): ask + save.
function Gestures({ tone = 'paper' }) {
  const dark = tone === 'dark';
  const bd = dark ? 'rgba(255,255,255,0.32)' : DR.hair;
  const tx = dark ? 'rgba(255,255,255,0.92)' : DR.ink;
  const ic = dark ? 'rgba(255,255,255,0.85)' : DR.goldDeep;
  const Pill = ({ icon, label }) => (
    <div style={{ flex: 1, display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 8, padding: '12px 10px', borderRadius: 999, border: `0.5px solid ${bd}` }}>
      {icon}<span style={{ fontFamily: DR.serif, fontSize: 14.5, color: tx, letterSpacing: -0.1 }}>{label}</span>
    </div>
  );
  return (
    <div style={{ display: 'flex', gap: 10 }}>
      <Pill icon={LIVE_ICON.mic(ic)} label="Ask Vesper"/>
      <Pill icon={LIVE_ICON.save(ic)} label="Save this moment"/>
    </div>
  );
}

// ─────────────────────────────────────────────────────────────────
// A · THE HOUR — the whole screen is "now". Full-bleed moment, one
// big line, a single next-hour recommendation, gestures, whispers.
// ─────────────────────────────────────────────────────────────────
function LiveHour({ evening }) {
  return (
    <PFrame h={LH}>
      <div style={{ position: 'relative', height: 404, marginTop: -40 }}>
        <div style={{ position: 'absolute', inset: 0, filter: evening ? 'saturate(0.9) brightness(0.7)' : 'none' }}><StyleRiso w={393} h={404}/></div>
        <div style={{ position: 'absolute', inset: 0, background: evening
          ? 'linear-gradient(to bottom, rgba(20,14,9,0.5) 0%, rgba(20,14,9,0.18) 38%, rgba(20,14,9,0.92) 100%)'
          : 'linear-gradient(to bottom, rgba(20,14,9,0.4) 0%, rgba(20,14,9,0) 30%, rgba(20,14,9,0) 50%, rgba(20,14,9,0.82) 100%)' }}/>
        <div style={{ position: 'absolute', top: 50, left: 20, right: 20, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
          {LIVE_ICON.back}
          <span style={{ fontFamily: DR.mono, fontSize: 9, letterSpacing: 2.2, color: 'rgba(255,255,255,0.82)', fontWeight: 600 }}>DAY 3 · TUE · {evening ? '7:40' : '4:30'}</span>
          {LIVE_ICON.dots('rgba(255,255,255,0.9)')}
        </div>
        <div style={{ position: 'absolute', left: 24, right: 24, bottom: 22 }}>
          <span style={{ fontFamily: DR.mono, fontSize: 9.5, letterSpacing: 2.4, color: 'rgba(255,255,255,0.8)', fontWeight: 600 }}>LISBON</span>
          <h1 style={{ fontFamily: DR.serif, fontSize: 38, fontWeight: 500, letterSpacing: -1, lineHeight: 0.96, color: '#fff', margin: '10px 0 0' }}>{evening ? <>The evening’s <span style={{ fontStyle: 'italic' }}>yours</span></> : <>The city tips <span style={{ fontStyle: 'italic' }}>gold</span></>}</h1>
        </div>
      </div>
      <div style={{ padding: '22px 24px 0' }}>
        <EdKick c={DR.goldDeep}>Vesper · right now</EdKick>
        <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 18.5, color: DR.ink, lineHeight: 1.4, letterSpacing: -0.2, margin: '10px 0 0' }}>
          {evening
            ? 'Alfama empties after six. Ramiro’s holding a table at eight — walk the long way, down through the tiles.'
            : 'You’re due the light at Graça — ten minutes on foot, and the bench on the left stays empty till five.'}
        </p>
        <div style={{ marginTop: 18 }}><Gestures/></div>
        <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 14, color: DR.mute, margin: '20px 0 0', lineHeight: 1.5, paddingTop: 15, borderTop: ed.rule }}>
          {evening ? 'Later — a nightcap if you like; tomorrow, Belém early.' : 'Later — dinner loose; tomorrow, Belém before the crowd.'}
        </p>
        <p style={{ fontFamily: DR.mono, fontSize: 9.5, letterSpacing: 1, color: DR.faint, margin: '12px 0 0', fontWeight: 600 }}>TONIGHT · CASA DO ALECRIM   ·   €42 TODAY   ·   THE 28 OUTSIDE</p>
      </div>
    </PFrame>
  );
}

// ─────────────────────────────────────────────────────────────────
// B · THE DISPATCH — Vesper writes a dated field-note, like a
// correspondent travelling with you. Prose-forward, intimate.
// ─────────────────────────────────────────────────────────────────
function LiveDispatch() {
  const day = [['done', '09.30', 'Alfama, before the heat'], ['done', '13.00', 'The long lunch at Ramiro'], ['now', '16.30', 'Graça, for the light'], ['open', 'eve', 'Nothing past the first glass']];
  return (
    <PFrame h={LH}>
      <div style={{ position: 'relative', height: 140, marginTop: -40 }}>
        <div style={{ position: 'absolute', inset: 0 }}><StyleRiso w={393} h={140}/></div>
        <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to bottom, rgba(20,14,9,0.34), rgba(20,14,9,0.05) 50%, rgba(20,14,9,0.5))' }}/>
        <div style={{ position: 'absolute', top: 50, left: 20, right: 20, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
          {LIVE_ICON.back}
          <span style={{ fontFamily: DR.mono, fontSize: 9, letterSpacing: 2.2, color: 'rgba(255,255,255,0.85)', fontWeight: 600 }}>DAY 3 · TUESDAY · LISBON</span>
          {LIVE_ICON.dots('rgba(255,255,255,0.9)')}
        </div>
      </div>
      <div style={{ padding: '22px 24px 0' }}>
        <EdKick c={DR.goldDeep}>Vesper · a note from the day</EdKick>
        <p style={{ fontFamily: DR.serif, fontSize: 19, color: DR.ink, lineHeight: 1.5, letterSpacing: -0.2, margin: '12px 0 0' }}>
          You had Alfama nearly to yourselves this morning, and lunch ran long the way the good ones do. <span style={{ fontStyle: 'italic', color: DR.soft }}>You’re due the light now — Graça’s ten minutes uphill, and it’s the best half-hour of the day.</span>
        </p>
        <div style={{ display: 'flex', alignItems: 'center', gap: 11, margin: '16px 0 0', padding: '13px 0', borderTop: ed.rule, borderBottom: ed.rule }}>
          <span style={{ width: 7, height: 7, borderRadius: 7, background: DR.goldDeep }}/>
          <span style={{ fontFamily: DR.mono, fontSize: 10, color: DR.goldDeep, fontWeight: 600, letterSpacing: 0.6 }}>16.30</span>
          <span style={{ fontFamily: DR.serif, fontSize: 17, fontWeight: 500, color: DR.ink, letterSpacing: -0.3, flex: 1 }}>Miradouro da Graça</span>
          <span style={{ color: DR.goldDeep, fontSize: 15 }}>→</span>
        </div>
      </div>
      <div style={{ padding: '18px 24px 0' }}>
        <EdKick>The day so far</EdKick>
        <div style={{ marginTop: 6 }}>
          {day.map(([st, t, txt], i) => {
            const now = st === 'now', done = st === 'done';
            return (
              <div key={i} style={{ display: 'grid', gridTemplateColumns: '46px 1fr', gap: 12, alignItems: 'baseline', padding: '10px 0', borderTop: i ? ed.hair : 'none' }}>
                <span style={{ fontFamily: DR.mono, fontSize: 9, letterSpacing: 0.5, color: now ? DR.goldDeep : DR.faint, fontWeight: 600 }}>{t}</span>
                <span style={{ fontFamily: DR.serif, fontSize: 15.5, fontWeight: now ? 600 : 400, fontStyle: done ? 'normal' : (now ? 'normal' : 'italic'), color: done ? DR.faint : DR.ink, textDecoration: done ? 'line-through' : 'none', textDecorationColor: DR.faint, letterSpacing: -0.2 }}>{txt}</span>
              </div>
            );
          })}
        </div>
        <div style={{ marginTop: 18 }}><Gestures/></div>
      </div>
    </PFrame>
  );
}

// ─────────────────────────────────────────────────────────────────
// C · THE MARGIN — an almost-empty calm page. Place + time set large,
// Vesper offers ONE thing from the foot; you pull for more.
// ─────────────────────────────────────────────────────────────────
function LiveMargin() {
  return (
    <PFrame h={LH}>
      <div style={{ position: 'relative', height: LH - 70, display: 'flex', flexDirection: 'column' }}>
        {/* top dateline */}
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '20px 24px 0' }}>
          {LIVE_ICON.backDk}
          <span style={{ fontFamily: DR.mono, fontSize: 9, letterSpacing: 2.2, color: DR.mute, fontWeight: 600 }}>DAY 3 · TUE · 4:30</span>
          {LIVE_ICON.dots(DR.soft)}
        </div>
        {/* the calm centre */}
        <div style={{ flex: 1, display: 'flex', flexDirection: 'column', justifyContent: 'center', padding: '0 30px' }}>
          <span style={{ fontFamily: DR.mono, fontSize: 10, letterSpacing: 2.6, color: DR.faint, fontWeight: 600 }}>YOU’RE IN</span>
          <h1 style={{ fontFamily: DR.serif, fontSize: 56, fontWeight: 500, letterSpacing: -1.8, lineHeight: 0.9, color: DR.ink, margin: '14px 0 0' }}>Lisbon</h1>
          <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 19, color: DR.mute, margin: '12px 0 0' }}>Tuesday, late afternoon.</p>
        </div>
        {/* one offering from the margin */}
        <div style={{ padding: '0 24px 4px' }}>
          <div style={{ borderTop: ed.rule, paddingTop: 16 }}>
            <EdKick c={DR.goldDeep}>Vesper</EdKick>
            <div style={{ display: 'flex', alignItems: 'flex-end', justifyContent: 'space-between', gap: 14, marginTop: 9 }}>
              <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 17.5, color: DR.ink, lineHeight: 1.38, letterSpacing: -0.2, margin: 0, flex: 1 }}>The light at Graça is best right now — ten minutes on foot.</p>
              <span style={{ color: DR.goldDeep, fontSize: 18, paddingBottom: 2 }}>→</span>
            </div>
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginTop: 16 }}>
              <span style={{ display: 'inline-flex', alignItems: 'center', gap: 8, fontFamily: DR.serif, fontStyle: 'italic', fontSize: 14, color: DR.mute }}>{LIVE_ICON.mic(DR.mute)} hold to ask</span>
              <span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 13.5, color: DR.faint }}>pull up for the day ↑</span>
            </div>
          </div>
        </div>
      </div>
    </PFrame>
  );
}

Object.assign(window, { LiveHour, LiveDispatch, LiveMargin });
