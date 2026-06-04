// ═══════════════════════════════════════════════════════════════
// POST-TRIP SINGLE-TRIP HOME — 3 small sketches. The trip is over;
// the home becomes a keepsake + close-out: remember · settle · hand
// off to Atlas. Logistics is gone; the pinned slot is the Atlas
// handoff, and cost finally surfaces as the settle-up.
// A · Keepsake-led · B · Close-out-led · C · The letter.
// Reuses DR, StyleRiso, ed, EdKick, SPARK, PFrame, TabBar.
// ═══════════════════════════════════════════════════════════════

const POST_NAV = <TabBar active="trips"/>;

function PostCover() {
  return (
    <div style={{ position: 'relative', height: 206, flexShrink: 0 }}>
      <div style={{ position: 'absolute', inset: 0, filter: 'saturate(0.82) brightness(0.84)' }}><StyleRiso w={393} h={206}/></div>
      <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to bottom, rgba(20,14,9,0.5) 0%, rgba(20,14,9,0.15) 42%, rgba(20,14,9,0.86) 100%)' }}/>
      <div style={{ position: 'absolute', top: 46, left: 20, right: 20, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,0.92)" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><path d="M14 6l-6 6 6 6"/></svg>
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,0.92)" strokeWidth="1.6" strokeLinecap="round"><circle cx="5" cy="12" r="1.4"/><circle cx="12" cy="12" r="1.4"/><circle cx="19" cy="12" r="1.4"/></svg>
      </div>
      <div style={{ position: 'absolute', left: 22, right: 22, bottom: 18 }}>
        <div style={{ fontFamily: DR.mono, fontSize: 9, letterSpacing: 2.4, color: 'rgba(255,255,255,0.82)', fontWeight: 600, marginBottom: 8 }}>SIX DAYS · NOVEMBER</div>
        <h1 style={{ fontFamily: DR.serif, fontSize: 38, fontWeight: 500, letterSpacing: -1, lineHeight: 0.96, color: '#fff', margin: 0 }}>Lisbon, <span style={{ fontStyle: 'italic' }}>kept</span></h1>
      </div>
    </div>
  );
}

function LookBack() {
  return (
    <div style={{ flexShrink: 0, padding: '18px 24px 0' }}>
      <div style={{ paddingLeft: 13, borderLeft: `2px solid ${DR.gold}` }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 7, marginBottom: 5 }}>
          <svg width="11" height="11" viewBox="0 0 24 24" fill={DR.gold}><path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z"/></svg>
          <span style={{ fontSize: 8.5, letterSpacing: 1.4, color: DR.goldDeep, fontWeight: 700 }}>VESPER · LOOKING BACK</span>
        </div>
        <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 16, color: DR.ink, margin: 0, lineHeight: 1.4, letterSpacing: -0.12 }}>Six days that ran slow in the best way — the mornings were the heart of it.</p>
      </div>
    </div>
  );
}

function PhotoStrip() {
  return (
    <div style={{ display: 'flex', gap: 7 }}>
      {[0, 1, 2, 3].map((i) => <div key={i} style={{ flex: 1, aspectRatio: '1', borderRadius: 9, overflow: 'hidden' }}><StyleRiso w={70} h={70}/></div>)}
      <div style={{ flex: 1, aspectRatio: '1', borderRadius: 9, background: DR.card, border: `0.5px solid ${DR.hair}`, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
        <span style={{ fontFamily: DR.serif, fontSize: 14, color: DR.mute, fontWeight: 500 }}>+138</span>
      </div>
    </div>
  );
}

function Record({ label = 'THE RECORD' }) {
  const items = [['I', 'The first miradouro, before the heat'], ['II', 'Ramiro, and the long table']];
  return (
    <div>
      <div style={{ fontFamily: DR.mono, fontSize: 9, letterSpacing: 2, color: DR.mute, fontWeight: 700, marginBottom: 6 }}>{label}</div>
      {items.map(([n, t], i) => (
        <div key={i} style={{ display: 'grid', gridTemplateColumns: '26px 1fr', gap: 13, alignItems: 'baseline', padding: '10px 0', borderTop: i ? `0.5px solid ${DR.hairThin}` : 'none' }}>
          <span style={{ fontFamily: DR.serif, fontSize: 15, fontStyle: 'italic', color: DR.goldDeep }}>{n}</span>
          <span style={{ fontFamily: DR.serif, fontSize: 15.5, color: DR.ink, letterSpacing: -0.2, lineHeight: 1.2 }}>{t}</span>
        </div>
      ))}
    </div>
  );
}

function AtlasHandoff() {
  return (
    <div style={{ flexShrink: 0, padding: '13px 22px 86px' }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 11, padding: '13px 16px', background: DR.card, borderRadius: 14, border: `0.5px solid ${DR.hair}` }}>
        <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke={DR.soft} strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.6 2.6 2.6 15.4 0 18M12 3c-2.6 2.6-2.6 15.4 0 18"/></svg>
        <div style={{ flex: 1 }}>
          <div style={{ fontFamily: DR.serif, fontSize: 15, fontWeight: 500, color: DR.ink, letterSpacing: -0.2 }}>Lisbon settles into your Atlas</div>
          <div style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 12, color: DR.mute, marginTop: 1 }}>kept for the next time you go back</div>
        </div>
        <span style={{ color: DR.faint, fontSize: 16 }}>→</span>
      </div>
    </div>
  );
}

// ── A · KEEPSAKE-LED ────────────────────────────────────────────
function PostA() {
  return (
    <PFrame h={852} bare>
      <div style={{ height: 852, display: 'flex', flexDirection: 'column' }}>
        <PostCover/>
        <LookBack/>
        <div style={{ flex: 1, padding: '18px 24px 0', overflow: 'hidden' }}>
          {/* the story — dominant */}
          <div style={{ borderRadius: 16, overflow: 'hidden', border: `0.5px solid ${DR.hair}` }}>
            <div style={{ height: 96, position: 'relative' }}>
              <StyleRiso w={345} h={96}/>
              <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to top, rgba(20,14,9,0.7), transparent 60%)' }}/>
              <div style={{ position: 'absolute', left: 15, right: 15, bottom: 11 }}>
                <div style={{ fontFamily: DR.mono, fontSize: 8.5, letterSpacing: 1.5, color: 'rgba(255,255,255,0.82)', fontWeight: 700, marginBottom: 4 }}>YOUR STORY IS READY</div>
                <div style={{ fontFamily: DR.serif, fontSize: 21, fontWeight: 500, color: '#fff', letterSpacing: -0.4 }}>Six slow days in Lisbon</div>
              </div>
            </div>
            <div style={{ padding: '12px 15px', background: DR.card, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
              <span style={{ fontFamily: DR.serif, fontSize: 14.5, color: DR.ink, fontWeight: 500 }}>Read the story</span>
              <span style={{ color: DR.goldDeep, fontSize: 15 }}>→</span>
            </div>
          </div>
          <div style={{ marginTop: 13 }}><PhotoStrip/></div>
          <div style={{ marginTop: 18, paddingTop: 14, borderTop: ed.rule }}><Record/></div>
        </div>
        <div style={{ flexShrink: 0, display: 'flex', alignItems: 'center', justifyContent: 'space-between', margin: '0 24px', paddingTop: 13, borderTop: ed.rule }}>
          <span style={{ fontFamily: DR.serif, fontSize: 14.5, color: DR.soft }}>You’re owed <span style={{ fontWeight: 600, color: DR.ink }}>€347</span></span>
          <span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 13.5, color: DR.goldDeep }}>settle up →</span>
        </div>
        <AtlasHandoff/>
      </div>
      {POST_NAV}
    </PFrame>
  );
}

// ── B · CLOSE-OUT-LED ───────────────────────────────────────────
function CloseRow({ label, value, done, action }) {
  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: 12, padding: '13px 0', borderTop: `0.5px solid ${DR.hairThin}` }}>
      <span style={{ width: 18, display: 'flex', flexShrink: 0 }}>
        {done
          ? <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#3D7050" strokeWidth="2.4" strokeLinecap="round" strokeLinejoin="round"><path d="M4 12l5 5L20 6"/></svg>
          : <span style={{ width: 7, height: 7, borderRadius: 7, background: DR.gold, display: 'block', margin: '0 auto' }}/>}
      </span>
      <span style={{ flex: 1, fontFamily: DR.serif, fontSize: 16, color: done ? DR.mute : DR.ink, letterSpacing: -0.2 }}>{label}</span>
      {value && <span style={{ fontFamily: DR.serif, fontSize: 14, color: DR.soft }}>{value}</span>}
      {action && <span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 13.5, color: DR.goldDeep }}>{action} →</span>}
    </div>
  );
}
function PostB() {
  return (
    <PFrame h={852} bare>
      <div style={{ height: 852, display: 'flex', flexDirection: 'column' }}>
        <PostCover/>
        <LookBack/>
        <div style={{ flex: 1, padding: '20px 24px 0', overflow: 'hidden' }}>
          <div style={{ fontFamily: DR.mono, fontSize: 9, letterSpacing: 2, color: DR.mute, fontWeight: 700, marginBottom: 4 }}>BEFORE IT BECOMES A MEMORY</div>
          <CloseRow label="Photos saved" value="142" done/>
          <CloseRow label="Your story is ready" action="read"/>
          <CloseRow label="You’re owed €347" action="settle"/>
          <div style={{ marginTop: 22, paddingTop: 16, borderTop: ed.rule }}>
            <div style={{ fontFamily: DR.mono, fontSize: 9, letterSpacing: 2, color: DR.mute, fontWeight: 700, marginBottom: 11 }}>THE KEEPSAKE</div>
            <PhotoStrip/>
          </div>
        </div>
        <AtlasHandoff/>
      </div>
      {POST_NAV}
    </PFrame>
  );
}

// ── C · THE LETTER ──────────────────────────────────────────────
function PostC() {
  return (
    <PFrame h={852} bare>
      <div style={{ height: 852, display: 'flex', flexDirection: 'column' }}>
        <PostCover/>
        <div style={{ flex: 1, padding: '26px 26px 0', overflow: 'hidden' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 7, marginBottom: 14 }}>
            <svg width="12" height="12" viewBox="0 0 24 24" fill={DR.gold}><path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z"/></svg>
            <span style={{ fontFamily: DR.mono, fontSize: 9, letterSpacing: 1.5, color: DR.goldDeep, fontWeight: 700 }}>VESPER</span>
          </div>
          <p style={{ fontFamily: DR.serif, fontSize: 19, color: DR.soft, lineHeight: 1.58, letterSpacing: -0.2, margin: 0 }}>
            Six days in Lisbon, the two of you — and the mornings were the heart of it. <span style={{ color: DR.ink }}>I kept 142 frames and wrote the trip up;</span> it’s ready when you want it. There’s <span style={{ color: DR.ink }}>€347 owed back to you</span> — say the word and I’ll settle it. Then I’ll fold Lisbon into your Atlas, for the next time.
          </p>
          <div style={{ display: 'flex', gap: 9, marginTop: 26, flexWrap: 'wrap' }}>
            {['Read the story', 'Settle €347', 'To Atlas'].map((a, i) => (
              <span key={i} style={{ padding: '9px 15px', borderRadius: 999, border: `0.5px solid ${i === 0 ? DR.goldDeep : DR.hair}`, fontFamily: DR.serif, fontSize: 13.5, color: i === 0 ? DR.goldDeep : DR.soft, background: i === 0 ? 'rgba(176,133,58,0.07)' : 'transparent' }}>{a}</span>
            ))}
          </div>
          <div style={{ marginTop: 30 }}><PhotoStrip/></div>
        </div>
        <div style={{ flexShrink: 0, height: 86 }}/>
      </div>
      {POST_NAV}
    </PFrame>
  );
}

Object.assign(window, { PostA, PostB, PostC });
