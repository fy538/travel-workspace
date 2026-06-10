// ═══════════════════════════════════════════════════════════════
// BLOCK INTERACTION — the committed pattern. Tap → paper popover
// (quick + ask); tap title/image → full place page (deep).
// Reuses TH + Phone/TabBar + StyleRiso + RBlock/RDay/RefTopBar/DateRail.
// ═══════════════════════════════════════════════════════════════

// Faint spine behind the popover so it reads in context.
function SpineCtx() {
  return (
    <div style={{ padding: '14px 20px 0' }}>
      <RDay day="MON" date="20" weather="18°" today>
        <RBlock time="NOW · 10:14" title="Cemetery walk" state="now" last/>
      </RDay>
      <RDay day="TUE" date="21">
        <div style={{ display: 'grid', gridTemplateColumns: '15px 1fr', gap: 13 }}>
          <div style={{ display: 'flex', justifyContent: 'center', position: 'relative' }}>
            <span style={{ position: 'absolute', top: 11, bottom: -2, width: 1, background: TH.hairThin }}/>
            <span style={{ width: 8, height: 8, borderRadius: 999, marginTop: 6, background: TH.ink, boxShadow: '0 0 0 4px rgba(27,23,20,0.12)', zIndex: 1 }}/>
          </div>
          <div style={{ paddingBottom: 15 }}>
            <span style={{ fontFamily: TH.mono, fontSize: 8.5, color: TH.mute, letterSpacing: 1.2, fontWeight: 600 }}>MORNING</span>
            <div style={{ fontFamily: TH.serif, fontSize: 15.5, fontWeight: 500, color: TH.ink, letterSpacing: -0.2, marginTop: 3 }}>Belém, early</div>
          </div>
        </div>
        <RBlock time="OPEN" title="this afternoon is bare" state="gap" last/>
      </RDay>
    </div>
  );
}

// ─── TAP · PAPER POPOVER (quick) ────────────────────────────────
function PopPaper() {
  return (
    <Phone bg={TH.paper}>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
        <RefTopBar/><DateRail/>
        <div style={{ position: 'relative' }}>
          <SpineCtx/>
          <div style={{ position: 'absolute', left: 40, right: 16, top: 120 }}>
            <div style={{ position: 'absolute', top: -6, left: 26, width: 12, height: 12, background: TH.card, transform: 'rotate(45deg)', border: `0.5px solid ${TH.hair}`, borderBottom: 'none', borderRight: 'none' }}/>
            <div style={{ position: 'relative', background: TH.card, borderRadius: 16, border: `0.5px solid ${TH.hair}`, boxShadow: '0 18px 40px -16px rgba(0,0,0,0.28)', overflow: 'hidden' }}>
              <div style={{ display: 'flex', gap: 11, padding: 12 }}>
                <div style={{ width: 56, height: 56, borderRadius: 9, overflow: 'hidden', flexShrink: 0 }}><StyleRiso w={56} h={56}/></div>
                <div style={{ flex: 1, minWidth: 0 }}>
                  <span style={{ fontFamily: TH.mono, fontSize: 8, color: TH.mute, letterSpacing: 1 }}>TUE 21 · MORNING</span>
                  <div style={{ fontFamily: TH.serif, fontSize: 17, fontWeight: 500, color: TH.ink, letterSpacing: -0.3, lineHeight: 1.05, marginTop: 2 }}>Belém, early</div>
                  <div style={{ fontFamily: TH.serif, fontStyle: 'italic', fontSize: 11.5, color: TH.mute, marginTop: 3 }}>beat the crowd · €</div>
                </div>
              </div>
              <div style={{ margin: '0 12px', display: 'flex', alignItems: 'center', gap: 8, padding: '9px 12px', background: TH.paper, borderRadius: 999, border: `0.5px solid ${TH.hair}` }}>
                <svg width="13" height="13" viewBox="0 0 24 24" fill={TH.gold}><path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z"/></svg>
                <span style={{ flex: 1, fontFamily: TH.serif, fontStyle: 'italic', fontSize: 13, color: TH.faint }}>“make this later, somewhere quieter…”</span>
              </div>
              <div style={{ display: 'flex', gap: 0, marginTop: 11, borderTop: `0.5px solid ${TH.hairThin}` }}>
                {[['Move','#2C2622'],['Book','#2C2622'],['Remove','#A04030']].map(([l,c],i)=>(
                  <div key={l} style={{ flex: 1, textAlign: 'center', padding: '11px 0', borderLeft: i?`0.5px solid ${TH.hairThin}`:'none', fontFamily: TH.sans, fontSize: 12.5, fontWeight: 600, color: c }}>{l}</div>
                ))}
              </div>
            </div>
          </div>
        </div>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

// ─── TAP TITLE · FULL PLACE PAGE (deep) ─────────────────────────
function BlockC() {
  return (
    <Phone bg={TH.ink}>
      <div style={{ position: 'absolute', inset: 0, overflow: 'hidden', background: TH.paper }}>
        <div style={{ position: 'relative', height: 300 }}>
          <div style={{ position: 'absolute', inset: 0 }}><StyleRiso w={393} h={300}/></div>
          <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to bottom, rgba(20,14,9,0.34), rgba(20,14,9,0) 38%, rgba(20,14,9,0.72))' }}/>
          <div style={{ position: 'absolute', top: 54, left: 18, width: 38, height: 38, borderRadius: 999, background: 'rgba(255,255,255,0.2)', backdropFilter: 'blur(8px)', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
            <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="#fff" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d="M15 5l-7 7 7 7"/></svg>
          </div>
          <div style={{ position: 'absolute', left: 22, right: 22, bottom: 18 }}>
            <div style={{ fontFamily: TH.mono, fontSize: 9, color: 'rgba(255,255,255,0.82)', letterSpacing: 1.2 }}>ON YOUR ITINERARY · TUE 21</div>
            <h1 style={{ fontFamily: TH.serif, fontSize: 31, fontWeight: 500, letterSpacing: -0.6, lineHeight: 1.02, color: '#fff', margin: '5px 0 0' }}>Belém</h1>
          </div>
        </div>
        <div style={{ padding: '18px 22px 0' }}>
          <p style={{ fontFamily: TH.serif, fontStyle: 'italic', fontSize: 16, color: TH.ink, lineHeight: 1.45, margin: 0, letterSpacing: -0.1 }}>Go at 8:30, straight for the monastery cloister — the tarts will still be warm after.</p>
          <div style={{ marginTop: 13, display: 'flex', gap: 6, flexWrap: 'wrap' }}>
            {['8:30 BEST','20 MIN TRAM','€','2HR'].map(m=>(<span key={m} style={{ padding: '4px 9px', fontFamily: TH.mono, fontSize: 8.5, color: TH.mute, letterSpacing: 1, fontWeight: 600, background: TH.card, border: `0.5px solid ${TH.hair}`, borderRadius: 999 }}>{m}</span>))}
          </div>
          <p style={{ fontFamily: TH.serif, fontSize: 14.5, color: TH.soft, lineHeight: 1.55, margin: '14px 0 0' }}>The Jerónimos cloister is the reason to come — limestone lacework, quietest right at opening. Pastéis de Belém two doors down does the original custard tart; take it standing at the counter, not the queue.</p>
        </div>
        {/* sticky action bar */}
        <div style={{ position: 'absolute', bottom: 0, left: 0, right: 0, padding: '12px 18px 20px', background: 'rgba(247,242,231,0.92)', backdropFilter: 'blur(20px)', borderTop: `0.5px solid ${TH.hair}`, display: 'flex', alignItems: 'center', gap: 12 }}>
          <span style={{ display: 'inline-flex', alignItems: 'center', gap: 6, color: TH.ink, fontSize: 13, fontWeight: 600 }}>
            <svg width="15" height="15" viewBox="0 0 24 24" fill={TH.gold}><path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z"/></svg> Ask to change
          </span>
          <span style={{ marginLeft: 'auto', display: 'flex', gap: 10 }}>
            <span style={{ padding: '9px 14px', background: TH.card, border: `0.5px solid ${TH.hair}`, borderRadius: 999, fontSize: 12.5, fontWeight: 600, color: TH.soft }}>Move</span>
            <span style={{ padding: '9px 16px', background: TH.blue, color: '#fff', borderRadius: 999, fontSize: 12.5, fontWeight: 600 }}>Book</span>
          </span>
        </div>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

Object.assign(window, { PopPaper, BlockC });
