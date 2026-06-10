// ═══════════════════════════════════════════════════════════════
// EDITORIAL TRIP HOME — type-led, magazine/field-note language.
// No boxed facet tiles, no shadowed cards: full-bleed riso, big
// Cormorant headlines, hairline rules, marginalia, Vesper as prose.
// Live + Memory phases, and two editorial trip-creation surfaces.
// Reuses DR, StyleRiso, Ppl/CASTD, PFrame.
// ═══════════════════════════════════════════════════════════════

const ed = {
  rule: `0.5px solid ${DR.hair}`,
  hair: `0.5px solid ${DR.hairThin}`,
};
// small-caps mono label (the field-journal margin voice)
const EdKick = ({ children, c = DR.mute }) => <div style={{ fontFamily: DR.mono, fontSize: 9, letterSpacing: 2.2, color: c, fontWeight: 600, textTransform: 'uppercase' }}>{children}</div>;

// Editorial cover — image breathes, restrained chrome, masthead low.
function EdCover({ phase, kicker, title, ital }) {
  const memory = phase === 'memory';
  return (
    <div style={{ position: 'relative', height: 312, marginTop: -40 }}>
      <div style={{ position: 'absolute', inset: 0, filter: memory ? 'saturate(0.8) brightness(0.9)' : 'none' }}><StyleRiso w={393} h={312}/></div>
      <div style={{ position: 'absolute', inset: 0, background: memory
        ? 'linear-gradient(to bottom, rgba(20,14,9,0.45) 0%, rgba(20,14,9,0.05) 38%, rgba(20,14,9,0.9) 100%)'
        : 'linear-gradient(to bottom, rgba(20,14,9,0.34) 0%, rgba(20,14,9,0) 30%, rgba(20,14,9,0) 52%, rgba(20,14,9,0.82) 100%)' }}/>
      {/* restrained top: just a back chevron + the trip wordmark, hairline under */}
      <div style={{ position: 'absolute', top: 50, left: 20, right: 20, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,0.92)" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><path d="M14 6l-6 6 6 6"/></svg>
        <span style={{ fontFamily: DR.mono, fontSize: 9, letterSpacing: 2.4, color: 'rgba(255,255,255,0.78)', fontWeight: 600 }}>LISBON · Nº 1</span>
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,0.92)" strokeWidth="1.6" strokeLinecap="round"><circle cx="5" cy="12" r="1.4"/><circle cx="12" cy="12" r="1.4"/><circle cx="19" cy="12" r="1.4"/></svg>
      </div>
      {/* masthead low */}
      <div style={{ position: 'absolute', left: 22, right: 22, bottom: 22 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 9 }}>
          <span style={{ fontFamily: DR.mono, fontSize: 9.5, letterSpacing: 2.6, color: 'rgba(255,255,255,0.85)', fontWeight: 600 }}>{kicker}</span>
          <span style={{ flex: 1, height: 0.5, background: 'rgba(255,255,255,0.35)' }}/>
          <Ppl who={CASTD} size={20} onDark/>
        </div>
        <h1 style={{ fontFamily: DR.serif, fontSize: 46, fontWeight: 500, letterSpacing: -1.4, lineHeight: 0.9, color: '#fff', margin: 0 }}>{title}<span style={{ fontStyle: 'italic', fontWeight: 400 }}>{ital}</span></h1>
      </div>
    </div>
  );
}

// Vesper as a standfirst — a drop-style opener, no box.
function EdStandfirst({ children, drop }) {
  return (
    <p style={{ fontFamily: DR.serif, fontSize: 19, fontWeight: 400, color: DR.ink, lineHeight: 1.42, letterSpacing: -0.2, margin: 0, fontStyle: 'italic' }}>
      {drop && <span style={{ fontStyle: 'normal', fontWeight: 500, float: 'left', fontSize: 52, lineHeight: 0.74, paddingRight: 9, paddingTop: 5, color: DR.goldDeep }}>{drop}</span>}
      {children}
    </p>
  );
}

// ─────────────────────────────────────────────────────────────────
// LIVE · editorial field-note page.
// ─────────────────────────────────────────────────────────────────
function EdLive() {
  const beats = [
    ['09.30', 'A slow start in Alfama', 'done'],
    ['13.00', 'The long lunch at Ramiro', 'done'],
    ['16.30', 'Graça, for the gold of it', 'now'],
    ['later', 'Nothing past the first glass', 'open'],
  ];
  return (
    <PFrame>
      <EdCover phase="live" kicker="DAY THREE · TUESDAY" title="Lisbon," ital=" today"/>
      <div style={{ padding: '22px 24px 0' }}>
        <EdKick c={DR.goldDeep}>Vesper · this hour</EdKick>
        <div style={{ height: 10 }}/>
        <EdStandfirst drop="Y">ou’re due the light at Graça by five — ten minutes on foot from lunch. I’ve kept the evening loose on purpose.</EdStandfirst>
      </div>
      {/* today, as a typographic column — hairlines, no boxes */}
      <div style={{ padding: '22px 24px 0' }}>
        <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', paddingBottom: 10, borderBottom: ed.rule }}>
          <EdKick>The day, as it stands</EdKick><EdKick>Lisbon</EdKick>
        </div>
        {beats.map(([t, txt, st], i) => {
          const now = st === 'now', done = st === 'done';
          return (
            <div key={i} style={{ display: 'grid', gridTemplateColumns: '13px 52px 1fr', gap: 12, alignItems: 'baseline', padding: '13px 0', borderBottom: ed.hair }}>
              <span style={{ alignSelf: 'center' }}>{now ? <span style={{ display: 'block', width: 7, height: 7, borderRadius: 7, background: DR.goldDeep }}/> : <span style={{ display: 'block', width: 5, height: 5, borderRadius: 5, border: `1px solid ${DR.faint}`, opacity: done ? 0.5 : 1 }}/>}</span>
              <span style={{ fontFamily: DR.mono, fontSize: 10, letterSpacing: 0.8, color: now ? DR.goldDeep : DR.faint, fontWeight: 600, paddingTop: 2 }}>{t}</span>
              <span style={{ fontFamily: DR.serif, fontSize: 18, fontWeight: now ? 500 : 400, fontStyle: now ? 'normal' : (done ? 'normal' : 'italic'), color: done ? DR.faint : DR.ink, letterSpacing: -0.3, lineHeight: 1.15 }}>{txt}</span>
            </div>
          );
        })}
        {/* marginalia — a single editorial run, not tiles */}
        <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 13.5, color: DR.mute, margin: '14px 0 0', lineHeight: 1.5 }}>
          Tonight, Casa do Alecrim · €42 spent today · the 28 runs past your door.
        </p>
      </div>
      {/* voice — a thin editorial line, not a button */}
      <div style={{ padding: '20px 24px 4px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 11, paddingTop: 15, borderTop: ed.rule }}>
          <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke={DR.goldDeep} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/></svg>
          <span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 15, color: DR.soft }}>Hold to tell Vesper something</span>
        </div>
      </div>
    </PFrame>
  );
}

// ─────────────────────────────────────────────────────────────────
// MEMORY · editorial closing essay.
// ─────────────────────────────────────────────────────────────────
function EdMemory() {
  const record = [
    ['I', 'The first miradouro, before the heat came up'],
    ['II', 'Ramiro, and the table that ran long'],
    ['III', 'Belém at opening — the cloister, nearly alone'],
  ];
  return (
    <PFrame>
      <EdCover phase="memory" kicker="SIX DAYS · NOVEMBER" title="Lisbon," ital=" kept"/>
      <div style={{ padding: '24px 24px 0' }}>
        <h2 style={{ fontFamily: DR.serif, fontSize: 26, fontWeight: 500, fontStyle: 'italic', color: DR.ink, letterSpacing: -0.5, lineHeight: 1.12, margin: 0 }}>“Six days that ran slow in the best way.”</h2>
        <div style={{ height: 16 }}/>
        <EdKick c={DR.goldDeep}>Vesper · looking back</EdKick>
        <div style={{ height: 9 }}/>
        <p style={{ fontFamily: DR.serif, fontSize: 16, color: DR.soft, lineHeight: 1.5, margin: 0 }}>The mornings were the heart of it. I’ve written the trip up — it’s yours to read, or to let settle into Atlas.</p>
      </div>
      <div style={{ padding: '22px 24px 0' }}>
        <div style={{ paddingBottom: 10, borderBottom: ed.rule }}><EdKick>The record</EdKick></div>
        {record.map(([n, txt], i) => (
          <div key={i} style={{ display: 'grid', gridTemplateColumns: '30px 1fr', gap: 14, alignItems: 'baseline', padding: '13px 0', borderBottom: ed.hair }}>
            <span style={{ fontFamily: DR.serif, fontSize: 16, fontStyle: 'italic', color: DR.goldDeep }}>{n}</span>
            <span style={{ fontFamily: DR.serif, fontSize: 17.5, color: DR.ink, letterSpacing: -0.3, lineHeight: 1.2 }}>{txt}</span>
          </div>
        ))}
        <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 13.5, color: DR.mute, margin: '14px 0 0' }}>Six nights · four cities · €1.4k shared · 142 frames.</p>
      </div>
      <div style={{ padding: '20px 24px 4px' }}>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', paddingTop: 15, borderTop: ed.rule }}>
          <span style={{ fontFamily: DR.serif, fontSize: 18, fontWeight: 500, color: DR.ink, letterSpacing: -0.3 }}>Read the story</span>
          <span style={{ color: DR.goldDeep, fontSize: 17 }}>→</span>
        </div>
      </div>
    </PFrame>
  );
}

// ═══════════════════════════════════════════════════════════════
// CREATING A TRIP · editorial — two takes.
// ═══════════════════════════════════════════════════════════════

// E1 · FRONTISPIECE — you set the title of a new journal. The place
// is a display headline you write; the rest is a quiet colophon.
function EdFrontispiece() {
  return (
    <PFrame>
      {/* faint riso wash, mostly paper */}
      <div style={{ position: 'relative', height: 150, marginTop: -40 }}>
        <div style={{ position: 'absolute', inset: 0, opacity: 0.32 }}><StyleRiso w={393} h={150}/></div>
        <div style={{ position: 'absolute', inset: 0, background: `linear-gradient(to bottom, rgba(239,234,224,0.2), ${DR.paper})` }}/>
        <div style={{ position: 'absolute', top: 50, left: 22, right: 22, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke={DR.soft} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><path d="M18 6 6 18M6 6l12 12"/></svg>
          <span style={{ fontFamily: DR.mono, fontSize: 9, letterSpacing: 2.6, color: DR.mute, fontWeight: 600 }}>A NEW FOLIO</span>
          <div style={{ width: 20 }}/>
        </div>
      </div>
      <div style={{ padding: '4px 26px 0', textAlign: 'center' }}>
        <EdKick c={DR.goldDeep}>Vesper</EdKick>
        <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 17, color: DR.mute, margin: '12px 0 26px', lineHeight: 1.4 }}>Every trip starts with a name. What shall we call this one?</p>
        {/* the title you write */}
        <h1 style={{ fontFamily: DR.serif, fontSize: 40, fontWeight: 500, letterSpacing: -1.2, lineHeight: 0.98, color: DR.ink, margin: 0 }}>Lisbon<span style={{ display: 'inline-block', width: 2, height: 38, background: DR.goldDeep, marginLeft: 3, verticalAlign: 'middle', transform: 'translateY(-2px)' }}/></h1>
        <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 16, color: DR.faint, margin: '8px 0 0' }}>add a second word — “slowly”, “again”…</p>
      </div>
      {/* colophon — the rest, quiet, set as an editorial line */}
      <div style={{ padding: '34px 26px 0' }}>
        <div style={{ borderTop: ed.rule, borderBottom: ed.rule, padding: '4px 0' }}>
          {[['WHEN', 'add the dates', true], ['WITH', 'just you — invite the others', true], ['THE FEEL', 'name a tone', true]].map(([k, v], i) => (
            <div key={k} style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', padding: '12px 0', borderTop: i ? ed.hair : 'none' }}>
              <EdKick>{k}</EdKick>
              <span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 15.5, color: DR.faint }}>{v}</span>
            </div>
          ))}
        </div>
      </div>
      <div style={{ padding: '26px 26px 0', textAlign: 'center' }}>
        <span style={{ fontFamily: DR.serif, fontSize: 18, fontWeight: 500, color: DR.ink, letterSpacing: -0.2, borderBottom: `1.5px solid ${DR.goldDeep}`, paddingBottom: 3 }}>Open the folio</span>
        <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 14, color: DR.mute, margin: '20px 0 0' }}>— or just tell me about it →</p>
      </div>
    </PFrame>
  );
}

// E2 · THE OPENING LETTER — Vesper writes you an invitation with the
// trip's facts as underlined fill-ins inside the prose. Form + chat
// become one editorial gesture.
function Fill({ children, set }) {
  return <span style={{ fontStyle: set ? 'normal' : 'italic', fontWeight: set ? 500 : 400, color: set ? DR.ink : DR.faint, borderBottom: `1.5px solid ${set ? DR.goldDeep : DR.faint}`, paddingBottom: 1, whiteSpace: 'nowrap' }}>{children}</span>;
}
function EdLetter() {
  return (
    <PFrame>
      <div style={{ position: 'relative', height: 92, marginTop: -40, display: 'flex', alignItems: 'flex-end', justifyContent: 'space-between', padding: '0 22px 0' }}>
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke={DR.soft} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><path d="M18 6 6 18M6 6l12 12"/></svg>
        <span style={{ fontFamily: DR.mono, fontSize: 9, letterSpacing: 2.6, color: DR.mute, fontWeight: 600, paddingBottom: 4 }}>A NEW FOLIO</span>
        <div style={{ width: 20 }}/>
      </div>
      <div style={{ padding: '26px 26px 0' }}>
        <EdKick c={DR.goldDeep}>Vesper</EdKick>
        <div style={{ height: 16 }}/>
        {/* the letter — facts are underlined fill-ins */}
        <p style={{ fontFamily: DR.serif, fontSize: 23, fontWeight: 400, color: DR.soft, lineHeight: 1.62, letterSpacing: -0.3, margin: 0 }}>
          So — we’re going to <Fill set>Lisbon</Fill>,<br/>
          sometime in <Fill>early June</Fill>,<br/>
          for <Fill>five slow days</Fill>.<br/>
          It’s <Fill set>you and Ana</Fill>, and the mood is <Fill>still yours to name</Fill>.
        </p>
        <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 14.5, color: DR.mute, margin: '26px 0 0', lineHeight: 1.5 }}>Tap anything underlined to set it — or keep talking and I’ll fill it in as we go.</p>
      </div>
      {/* composer, kept as a thin editorial line */}
      <div style={{ padding: '30px 24px 0' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 12, paddingTop: 15, borderTop: ed.rule }}>
          <span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 15, color: DR.faint, flex: 1 }}>“five days, mostly food and walking”…</span>
          <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke={DR.goldDeep} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/></svg>
        </div>
      </div>
      <div style={{ padding: '24px 26px 0', textAlign: 'center' }}>
        <span style={{ fontFamily: DR.serif, fontSize: 18, fontWeight: 500, color: DR.ink, letterSpacing: -0.2, borderBottom: `1.5px solid ${DR.goldDeep}`, paddingBottom: 3 }}>Begin the folio</span>
      </div>
    </PFrame>
  );
}

Object.assign(window, { EdLive, EdMemory, EdFrontispiece, EdLetter });
