// ═══════════════════════════════════════════════════════════════
// THREE SYSTEMS · same 4 zones, three hands. Each is Sys?(phaseKey).
//   A · Editorial Folio — big cover, identity overlaid, serif Vesper line
//   B · Companion       — Vesper-forward; a predictive voice card leads
//   C · Quiet Index     — typographic, minimal imagery, scannable
// Locked order every phase: COVER · VESPER · SPINE · SIBLINGS.
// ═══════════════════════════════════════════════════════════════

// Shared: a Vesper voice block — kicker + forward line + one action chip.
function VBlock({ p, dark, big }) {
  return (
    <div>
      <div style={{ display: 'flex', alignItems: 'center', gap: 6, marginBottom: 6 }}>
        <svg width="13" height="13" viewBox="0 0 24 24" fill={dark?'#E5C16F':TH.gold}><path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z"/></svg>
        <span style={{ fontSize: 9, letterSpacing: 1.6, fontWeight: 700, color: dark?'#E5C16F':TH.goldDeep }}>{p.vKicker}</span>
      </div>
      <p style={{ margin: 0, fontFamily: TH.serif, fontStyle: 'italic', fontSize: big?17:15, color: dark?'rgba(255,255,255,0.95)':TH.ink, lineHeight: 1.4, letterSpacing: -0.1 }}>{p.vLine}</p>
      {p.vAction && (
        <div style={{ marginTop: 10, display: 'inline-flex', alignItems: 'center', gap: 6, padding: '7px 13px', borderRadius: 999, background: dark?'rgba(255,255,255,0.14)':TH.ink, color: dark?'#fff':'#fff', fontSize: 12, fontWeight: 600, letterSpacing: -0.1 }}>
          {p.vAction} <span style={{ opacity: 0.7 }}>→</span>
        </div>
      )}
    </div>
  );
}

// ─── SYSTEM A · EDITORIAL FOLIO ─────────────────────────────────
function SysA(phaseKey) {
  const p = PHASE[phaseKey];
  return (
    <Phone bg={p.art==='gouache'?TH.ink:TH.paper}>
      <div style={{ position: 'absolute', inset: 0, overflow: 'hidden', background: TH.paper }}>
        {/* ZONE 1 · COVER — full-bleed */}
        <div style={{ position: 'relative', height: p.cold?210:286 }}>
          {p.cold ? (
            <div style={{ position: 'absolute', inset: 12, top: 60, borderRadius: 16, border: `1.2px dashed ${TH.faint}`, background: TH.cardSoft, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
              <svg width="48" height="48" viewBox="0 0 56 56" fill="none" stroke={TH.faint} strokeWidth="1"><circle cx="28" cy="28" r="20"/><path d="M28 12 L31 28 L28 44 L25 28 Z" fill={TH.faint} stroke="none" opacity="0.5"/></svg>
            </div>
          ) : (
            <>
              <div style={{ position: 'absolute', inset: 0 }}><Art p={p} w={393} h={286}/></div>
              <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to bottom, rgba(20,14,9,0.26) 0%, rgba(20,14,9,0) 32%, rgba(20,14,9,0) 54%, rgba(20,14,9,0.66) 100%)' }}/>
            </>
          )}
          <div style={{ paddingTop: 54 }}><TripHeader onDark={!p.cold}/></div>
          <div style={{ position: 'absolute', top: 92, left: 22 }}><PhaseRibbon phase={p.ribbon} onDark={!p.cold}/></div>
          <div style={{ position: 'absolute', left: 22, right: 22, bottom: p.cold?'auto':18, top: p.cold?150:'auto' }}>
            {!p.cold && (
              <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 7 }}>
                <span style={{ padding: '3px 9px', borderRadius: 999, background: 'rgba(255,255,255,0.2)', backdropFilter: 'blur(6px)', fontSize: 9, letterSpacing: 1.4, fontWeight: 700, color: '#fff' }}>{p.countdown}</span>
                <People who={castOf(p)} onDark size={22}/>
              </div>
            )}
            <h1 style={{ fontFamily: TH.serif, fontSize: p.cold?28:36, fontWeight: 500, letterSpacing: -1, lineHeight: 0.98, color: p.cold?TH.ink:'#fff', margin: 0 }}>{p.title} <span style={{ fontStyle: 'italic' }}>{p.italic}</span></h1>
            <div style={{ fontFamily: TH.mono, fontSize: 9.5, color: p.cold?TH.mute:'rgba(255,255,255,0.85)', letterSpacing: 1, marginTop: 6 }}>{p.meta}</div>
          </div>
        </div>
        {/* ZONE 2 · VESPER */}
        <div style={{ padding: '16px 22px 0' }}><VBlock p={p}/></div>
        {/* ZONE 3 · SPINE */}
        {!p.cold && (
          <div style={{ padding: '16px 22px 0' }}>
            <Label right={p.meta.split('·')[0].trim()}>{p.spineLabel}</Label>
            <div style={{ marginTop: 12 }}>{p.spine.map((r,i)=><Node key={i} row={r} last={i===p.spine.length-1}/>)}</div>
            <Door label={phaseKey==='live'?'Open today’s plan':phaseKey==='memory'?'Revisit the trip':'Open the full itinerary'} meta={phaseKey==='memory'?'now a record':'6 days · 14 stops'}/>
          </div>
        )}
        {/* ZONE 4 · SIBLINGS */}
        <div style={{ padding: '16px 18px 0' }}><Tiles tiles={p.tiles}/></div>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

// ─── SYSTEM B · COMPANION (Vesper-forward) ──────────────────────
function SysB(phaseKey) {
  const p = PHASE[phaseKey];
  return (
    <Phone bg={TH.paper}>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
        {/* ZONE 1 · COVER — slim band */}
        <div style={{ padding: '6px 18px 0' }}>
          <div style={{ position: 'relative', height: 92, borderRadius: 14, overflow: 'hidden' }}>
            {p.cold ? <div style={{ position: 'absolute', inset: 0, background: TH.cardSoft, border: `1px dashed ${TH.faint}` }}/> : <div style={{ position: 'absolute', inset: 0 }}><Art p={p} w={357} h={92}/></div>}
            <div style={{ position: 'absolute', inset: 0, background: p.cold?'none':'linear-gradient(90deg, rgba(20,14,9,0.55), rgba(20,14,9,0.1))' }}/>
            <div style={{ position: 'absolute', left: 14, top: 0, bottom: 0, display: 'flex', flexDirection: 'column', justifyContent: 'center' }}>
              <PhaseRibbon phase={p.ribbon} onDark={!p.cold}/>
              <h1 style={{ fontFamily: TH.serif, fontSize: 22, fontWeight: 500, letterSpacing: -0.4, color: p.cold?TH.ink:'#fff', margin: '4px 0 0' }}>{p.title} <span style={{ fontStyle: 'italic' }}>{p.italic}</span></h1>
            </div>
            {!p.cold && <div style={{ position: 'absolute', right: 12, bottom: 10 }}><People who={castOf(p)} onDark size={20}/></div>}
          </div>
        </div>
        {/* ZONE 2 · VESPER — the hero. A predictive voice card. */}
        <div style={{ padding: '14px 18px 0' }}>
          <div style={{ background: 'rgba(27,23,20,0.97)', borderRadius: 18, padding: '16px 16px 14px', boxShadow: '0 18px 40px -16px rgba(0,0,0,0.4)' }}>
            <VBlock p={p} dark big/>
          </div>
        </div>
        {/* ZONE 3 · SPINE */}
        {!p.cold && (
          <div style={{ padding: '16px 22px 0' }}>
            <Label right={p.spineLabel==='TODAY'?'3 STOPS':p.spine.length+' SHOWN'}>{p.spineLabel}</Label>
            <div style={{ marginTop: 12 }}>{p.spine.map((r,i)=><Node key={i} row={r} last={i===p.spine.length-1} hideDate={phaseKey==='live'}/>)}</div>
            <Door label={phaseKey==='live'?'Open today’s plan':phaseKey==='memory'?'Revisit the trip':'Open the full itinerary'} meta="6 days · 14 stops"/>
          </div>
        )}
        {/* ZONE 4 · SIBLINGS */}
        <div style={{ padding: '16px 18px 0' }}><Tiles tiles={p.tiles}/></div>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

// ─── SYSTEM C · QUIET INDEX (typographic, scannable) ────────────
function SysC(phaseKey) {
  const p = PHASE[phaseKey];
  return (
    <Phone bg={TH.paper}>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
        {/* ZONE 1 · COVER — title row + small thumbnail */}
        <div style={{ padding: '10px 22px 0' }}>
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
            <PhaseRibbon phase={p.ribbon}/>
            <People who={castOf(p)} size={20}/>
          </div>
          <div style={{ display: 'flex', alignItems: 'flex-end', gap: 13, marginTop: 12 }}>
            <div style={{ width: 60, height: 60, borderRadius: 12, overflow: 'hidden', flexShrink: 0, border: `0.5px solid ${TH.hair}` }}>
              {p.cold ? <div style={{ width: '100%', height: '100%', background: TH.cardSoft, border: `1px dashed ${TH.faint}` }}/> : <Art p={p} w={60} h={60}/>}
            </div>
            <div style={{ flex: 1, minWidth: 0 }}>
              <h1 style={{ fontFamily: TH.serif, fontSize: 28, fontWeight: 500, letterSpacing: -0.7, lineHeight: 0.95, color: TH.ink, margin: 0 }}>{p.title} <span style={{ fontStyle: 'italic' }}>{p.italic}</span></h1>
              <div style={{ fontFamily: TH.mono, fontSize: 8.5, color: TH.mute, letterSpacing: 1, marginTop: 6 }}>{p.meta}</div>
            </div>
          </div>
        </div>
        <div style={{ padding: '14px 22px 0' }}><div style={{ height: 0.5, background: TH.hair }}/></div>
        {/* ZONE 2 · VESPER — one quiet line */}
        <div style={{ padding: '14px 22px 0' }}><VBlock p={p}/></div>
        <div style={{ padding: '14px 22px 0' }}><div style={{ height: 0.5, background: TH.hair }}/></div>
        {/* ZONE 3 · SPINE — clean index, the bulk of the page */}
        {!p.cold && (
          <div style={{ padding: '14px 22px 0' }}>
            <Label right={p.spineLabel==='TODAY'?'LIVE':p.spine.length+' OF 14'}>{p.spineLabel}</Label>
            <div style={{ marginTop: 14 }}>{p.spine.map((r,i)=><Node key={i} row={r} last={i===p.spine.length-1}/>)}</div>
            <div style={{ marginTop: 10, display: 'flex', alignItems: 'center', justifyContent: 'space-between', paddingTop: 12, borderTop: `0.5px solid ${TH.hair}` }}>
              <span style={{ fontFamily: TH.serif, fontStyle: 'italic', fontSize: 13, color: TH.mute }}>{phaseKey==='memory'?'revisit the whole trip':phaseKey==='live'?'see the rest of today':'open all six days'}</span>
              <span style={{ color: TH.ink, fontSize: 13, fontWeight: 600 }}>→</span>
            </div>
          </div>
        )}
        {/* ZONE 4 · SIBLINGS — compact text row */}
        <div style={{ padding: '16px 22px 0' }}>
          <div style={{ display: 'flex', gap: 0, borderTop: `0.5px solid ${TH.hair}`, paddingTop: 12 }}>
            {p.tiles.map((t,i)=>(
              <div key={i} style={{ flex: 1, textAlign: 'center', borderLeft: i?`0.5px solid ${TH.hairThin}`:'none' }}>
                <div style={{ color: t.accent?TH.goldDeep:TH.soft, display: 'flex', justifyContent: 'center', marginBottom: 5 }}>{t.g}</div>
                <div style={{ fontFamily: TH.serif, fontSize: 13, fontWeight: 500, color: TH.ink, letterSpacing: -0.1 }}>{t.l}</div>
                {t.m && <div style={{ fontFamily: TH.mono, fontSize: 7.5, color: TH.faint, letterSpacing: 0.5, marginTop: 2 }}>{t.m.toUpperCase()}</div>}
              </div>
            ))}
          </div>
        </div>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

Object.assign(window, { VBlock, SysA, SysB, SysC });
