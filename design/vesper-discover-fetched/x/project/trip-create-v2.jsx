// ═══════════════════════════════════════════════════════════════
// CREATING A TRIP · rethought — 3 surfaces. The + can open any of
// these; all write to ONE trip object (sheets, canvas, and chat are
// the same trip being shaped). Reuses DR, StyleRiso, CIcon/CICO,
// Ppl/CASTD, PFrame.
// ═══════════════════════════════════════════════════════════════

// A faint "forming" cover — the folio before it has a place/photo.
function FormCover({ titled }) {
  return (
    <div style={{ position: 'relative', height: 168, marginTop: -40, background: '#E8E1D3' }}>
      {titled && <div style={{ position: 'absolute', inset: 0, opacity: 0.5 }}><StyleRiso w={393} h={168}/></div>}
      <div style={{ position: 'absolute', inset: 0, background: titled ? 'linear-gradient(to bottom, rgba(20,14,9,0.3), rgba(20,14,9,0) 40%, rgba(20,14,9,0.55))' : 'none' }}/>
      <div style={{ position: 'absolute', top: 46, left: 16, right: 16, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
        <div style={{ width: 34, height: 34, borderRadius: 999, background: titled ? 'rgba(255,255,255,0.2)' : DR.card, border: titled ? 'none' : `0.5px solid ${DR.hair}`, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke={titled ? '#fff' : DR.soft} strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d="M18 6 6 18M6 6l12 12"/></svg>
        </div>
        <span style={{ fontSize: 9, letterSpacing: 1.6, color: titled ? '#fff' : DR.mute, fontWeight: 700 }}>NEW TRIP</span>
        <div style={{ width: 34 }}/>
      </div>
      <div style={{ position: 'absolute', left: 20, right: 20, bottom: 16 }}>
        {titled
          ? <h1 style={{ fontFamily: DR.serif, fontSize: 32, fontWeight: 500, letterSpacing: -1, lineHeight: 0.98, color: '#fff', margin: 0 }}>Lisbon, <span style={{ fontStyle: 'italic' }}>slowly</span></h1>
          : <h1 style={{ fontFamily: DR.serif, fontSize: 30, fontWeight: 500, letterSpacing: -0.8, lineHeight: 1, color: DR.faint, margin: 0, fontStyle: 'italic' }}>Where to?</h1>}
      </div>
    </div>
  );
}

// Small labeled "slot" used by the composing canvas — filled or empty.
function Slot({ icon, label, value, empty }) {
  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: 12, padding: '13px 0', borderTop: `0.5px solid ${DR.hairThin}` }}>
      <span style={{ color: empty ? DR.faint : DR.soft, display: 'flex', width: 18 }}>{icon}</span>
      <div style={{ flex: 1 }}>
        <div style={{ fontSize: 8, letterSpacing: 1.3, color: DR.mute, fontWeight: 700 }}>{label}</div>
        <div style={{ fontFamily: DR.serif, fontSize: 16, fontWeight: 500, color: empty ? DR.faint : DR.ink, fontStyle: empty ? 'italic' : 'normal', letterSpacing: -0.2, marginTop: 2 }}>{value}</div>
      </div>
      <span style={{ fontSize: 18, color: DR.faint, fontWeight: 300 }}>{empty ? '+' : '›'}</span>
    </div>
  );
}
const CRI = {
  pin: <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"><path d="M12 21s-7-6-7-11a7 7 0 0 1 14 0c0 5-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/></svg>,
  cal: <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 9h18M8 3v4M16 3v4"/></svg>,
  ppl: <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"><circle cx="9" cy="8" r="3"/><path d="M3 20c0-3 2.7-5 6-5s6 2 6 5"/><path d="M16 6a3 3 0 0 1 0 6M21 20c0-2.4-1.4-4.2-3.5-4.8"/></svg>,
  tone: <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"><path d="M12 3v18M5 8l14 8M19 8 5 16"/></svg>,
};

// ─────────────────────────────────────────────────────────────────
// C1 · QUIET SHEETS — bottom sheet over the dimmed forming folio,
// one taste-led question at a time. Editorial, no form chrome.
// ─────────────────────────────────────────────────────────────────
function CreateSheets() {
  return (
    <PFrame>
      <div style={{ filter: 'brightness(0.82)' }}><FormCover/></div>
      <div style={{ height: 240 }}/>
      {/* dim scrim */}
      <div style={{ position: 'absolute', inset: 0, background: 'rgba(20,14,9,0.32)', borderRadius: 30 }}/>
      {/* sheet */}
      <div style={{ position: 'absolute', left: 0, right: 0, bottom: 0, background: DR.paper, borderTopLeftRadius: 26, borderTopRightRadius: 26, padding: '12px 22px 26px', boxShadow: '0 -20px 50px -20px rgba(0,0,0,0.4)' }}>
        <div style={{ width: 38, height: 4, borderRadius: 4, background: DR.hair, margin: '0 auto 18px' }}/>
        <div style={{ display: 'flex', alignItems: 'center', gap: 7, marginBottom: 8 }}>
          <svg width="12" height="12" viewBox="0 0 24 24" fill={DR.gold}><path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z"/></svg>
          <span style={{ fontSize: 9, letterSpacing: 1.5, color: DR.goldDeep, fontWeight: 700 }}>VESPER</span>
        </div>
        <p style={{ fontFamily: DR.serif, fontSize: 22, fontWeight: 500, color: DR.ink, margin: 0, letterSpacing: -0.4, lineHeight: 1.15 }}>Where are we going?</p>
        <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 14, color: DR.mute, margin: '6px 0 16px', lineHeight: 1.4 }}>From what you’ve been saving, three that feel like you right now —</p>
        {[['Lisbon', 'slow mornings, miradouros, tile light'], ['Mexico City', 'markets, mezcal, your kind of chaos'], ['Lofoten', 'the quiet you keep circling']].map(([p, why], i) => (
          <div key={p} style={{ display: 'flex', alignItems: 'center', gap: 13, padding: '12px 0', borderTop: i ? `0.5px solid ${DR.hairThin}` : `0.5px solid ${DR.hair}` }}>
            <div style={{ width: 44, height: 44, borderRadius: 10, overflow: 'hidden', flexShrink: 0 }}><StyleRiso w={44} h={44}/></div>
            <div style={{ flex: 1 }}>
              <div style={{ fontFamily: DR.serif, fontSize: 17, fontWeight: 500, color: DR.ink, letterSpacing: -0.2 }}>{p}</div>
              <div style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 12, color: DR.mute, marginTop: 1 }}>{why}</div>
            </div>
            <span style={{ fontSize: 16, color: DR.faint }}>›</span>
          </div>
        ))}
        <div style={{ marginTop: 16, display: 'flex', alignItems: 'center', gap: 10 }}>
          <div style={{ flex: 1, padding: '13px 16px', borderRadius: 999, background: DR.cardSoft, border: `0.5px solid ${DR.hair}`, fontFamily: DR.serif, fontStyle: 'italic', fontSize: 14, color: DR.mute }}>somewhere else…</div>
          <span style={{ width: 46, height: 46, borderRadius: 999, background: '#5B4B8A', display: 'flex', alignItems: 'center', justifyContent: 'center' }}><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#fff" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><rect x="9" y="3" width="6" height="12" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/></svg></span>
        </div>
      </div>
    </PFrame>
  );
}

// ─────────────────────────────────────────────────────────────────
// C2 · COMPOSING CANVAS — no discrete sheets. The trip is ONE forming
// folio; destination/dates/people/tone are inline slots you fill in
// any order. "Talk to Vesper" sits right there as the other path.
// ─────────────────────────────────────────────────────────────────
function CreateCanvas() {
  return (
    <PFrame>
      <FormCover titled/>
      <div style={{ padding: '18px 22px 0' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 7, marginBottom: 4 }}>
          <svg width="11" height="11" viewBox="0 0 24 24" fill={DR.gold}><path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z"/></svg>
          <span style={{ fontSize: 8.5, letterSpacing: 1.4, color: DR.goldDeep, fontWeight: 700 }}>VESPER</span>
        </div>
        <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 15.5, color: DR.soft, margin: '0 0 6px', lineHeight: 1.4 }}>Lisbon — good. Fill in what you know; I’ll shape the rest as we go.</p>
        <Slot icon={CRI.pin} label="DESTINATION" value="Lisbon, Portugal"/>
        <Slot icon={CRI.cal} label="DATES" value="add when" empty/>
        <Slot icon={CRI.ppl} label="WHO" value="just you — invite people" empty/>
        <Slot icon={CRI.tone} label="THE FEEL" value="add a tone" empty/>
      </div>
      {/* the other path, pinned in flow */}
      <div style={{ margin: '20px 18px 0', padding: '14px 16px', background: DR.card, borderRadius: 14, border: `0.5px solid ${DR.hair}`, display: 'flex', alignItems: 'center', gap: 12 }}>
        <span style={{ width: 38, height: 38, borderRadius: 999, background: '#5B4B8A', display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0 }}><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="#fff" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d="M4 5h16v11H8l-4 4z"/></svg></span>
        <div style={{ flex: 1 }}>
          <div style={{ fontFamily: DR.serif, fontSize: 14.5, fontWeight: 500, color: DR.ink, letterSpacing: -0.2 }}>Or just tell me about it</div>
          <div style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 12, color: DR.mute, marginTop: 1 }}>“five quiet days, mostly Ana and me”</div>
        </div>
        <span style={{ fontSize: 16, color: DR.faint }}>›</span>
      </div>
      <div style={{ padding: '18px 18px 0' }}>
        <div style={{ padding: '14px', textAlign: 'center', background: DR.ink, color: '#fff', borderRadius: 999, fontSize: 13.5, fontWeight: 600, letterSpacing: -0.1 }}>Start the folio</div>
      </div>
    </PFrame>
  );
}

// ─────────────────────────────────────────────────────────────────
// C3 · CONVERSATIONAL START — the + opens Vesper. You describe the
// trip; structured slots fill themselves into a forming card as you
// talk. "Fill it in yourself" drops to the canvas (C2).
// ─────────────────────────────────────────────────────────────────
function CreateChat() {
  return (
    <PFrame>
      <div style={{ position: 'relative', height: 60, marginTop: -40, display: 'flex', alignItems: 'flex-end', justifyContent: 'space-between', padding: '0 18px 0' }}>
        <div style={{ width: 34, height: 34, borderRadius: 999, background: DR.card, border: `0.5px solid ${DR.hair}`, display: 'flex', alignItems: 'center', justifyContent: 'center' }}><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke={DR.soft} strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d="M18 6 6 18M6 6l12 12"/></svg></div>
        <span style={{ fontSize: 9, letterSpacing: 1.6, color: DR.mute, fontWeight: 700, paddingBottom: 7 }}>NEW TRIP</span>
        <div style={{ width: 34 }}/>
      </div>
      <div style={{ padding: '22px 22px 0' }}>
        {/* Vesper opener */}
        <div style={{ display: 'flex', alignItems: 'center', gap: 7, marginBottom: 8 }}><svg width="12" height="12" viewBox="0 0 24 24" fill={DR.gold}><path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z"/></svg><span style={{ fontSize: 9, letterSpacing: 1.5, color: DR.goldDeep, fontWeight: 700 }}>VESPER</span></div>
        <p style={{ fontFamily: DR.serif, fontSize: 21, fontWeight: 500, color: DR.ink, margin: 0, letterSpacing: -0.4, lineHeight: 1.18 }}>Tell me about the trip you’re dreaming up.</p>
        <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 13.5, color: DR.mute, margin: '7px 0 0', lineHeight: 1.4 }}>A place, a feeling, who’s coming — whatever you’ve got. I’ll start the folio.</p>

        {/* user line */}
        <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: 20 }}>
          <div style={{ maxWidth: '82%', padding: '11px 15px', background: DR.card, borderRadius: '16px 16px 4px 16px', border: `0.5px solid ${DR.hair}`, fontFamily: DR.serif, fontSize: 14.5, color: DR.ink, lineHeight: 1.35 }}>Lisbon with Ana in early June. Five days, slow — good food, no rushing.</div>
        </div>

        {/* forming card Vesper is assembling */}
        <div style={{ marginTop: 18, borderRadius: 16, overflow: 'hidden', border: `0.5px solid ${DR.hair}`, background: DR.card }}>
          <div style={{ height: 78, position: 'relative' }}><StyleRiso w={345} h={78}/><div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to top, rgba(20,14,9,0.55), transparent)' }}/><div style={{ position: 'absolute', left: 14, bottom: 9 }}><div style={{ fontFamily: DR.serif, fontSize: 19, fontWeight: 500, color: '#fff', letterSpacing: -0.3 }}>Lisbon, <span style={{ fontStyle: 'italic' }}>slowly</span></div></div></div>
          <div style={{ padding: '6px 16px 12px' }}>
            {[[CRI.cal, 'Jun 2–7 · 5 nights'], [CRI.ppl, 'You + Ana'], [CRI.tone, 'Slow · food-led']].map(([ic, v], i) => (
              <div key={i} style={{ display: 'flex', alignItems: 'center', gap: 11, padding: '9px 0', borderTop: i ? `0.5px solid ${DR.hairThin}` : 'none' }}>
                <span style={{ color: '#3D7050', display: 'flex' }}><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#3D7050" strokeWidth="2.4" strokeLinecap="round" strokeLinejoin="round"><path d="M4 12l5 5L20 6"/></svg></span>
                <span style={{ color: DR.faint, display: 'flex' }}>{ic}</span>
                <span style={{ fontFamily: DR.serif, fontSize: 14.5, color: DR.ink, letterSpacing: -0.15 }}>{v}</span>
              </div>
            ))}
          </div>
        </div>
        <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 13, color: DR.mute, margin: '12px 2px 0', lineHeight: 1.4 }}>Got it — that’s enough to begin. Want me to draft a shape for the five days?</p>
      </div>
      {/* composer + escape hatch */}
      <div style={{ padding: '16px 18px 0' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
          <div style={{ flex: 1, padding: '13px 16px', borderRadius: 999, background: DR.cardSoft, border: `0.5px solid ${DR.hair}`, fontFamily: DR.serif, fontStyle: 'italic', fontSize: 14, color: DR.mute }}>add a detail…</div>
          <span style={{ width: 46, height: 46, borderRadius: 999, background: '#5B4B8A', display: 'flex', alignItems: 'center', justifyContent: 'center' }}><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#fff" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><rect x="9" y="3" width="6" height="12" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/></svg></span>
        </div>
        <div style={{ textAlign: 'center', marginTop: 12 }}><span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 12.5, color: DR.mute }}>or fill it in yourself →</span></div>
      </div>
    </PFrame>
  );
}

Object.assign(window, { CreateSheets, CreateCanvas, CreateChat });
