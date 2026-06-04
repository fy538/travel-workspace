// ═══════════════════════════════════════════════════════════════
// STAY · v2 redesign — itinerary-language spine, NO photos.
// A continuous night-spine on the left (dot + connecting rule), each
// accommodation a calm text block scoped to its nights, travelers as
// small avatars on the block. Mirrors the itinerary's quiet editorial feel.
// Reuses DR + Phone/TabBar.
// ═══════════════════════════════════════════════════════════════

const SPEEP = { T: '#A0703A', A: '#7C8F73', M: '#3D5066' };
function SAv({ who, s = 18, ring = '#F7F2E7' }) {
  return <div style={{ width: s, height: s, borderRadius: 999, background: SPEEP[who], color: '#fff', fontFamily: DR.serif, fontSize: s * 0.46, fontWeight: 500, display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0, border: `1.5px solid ${ring}` }}>{who}</div>;
}
function SAvStack({ who, ring }) {
  return <div style={{ display: 'flex' }}>{who.map((w, i) => <span key={w} style={{ marginLeft: i ? -5 : 0 }}><SAv who={w} ring={ring}/></span>)}</div>;
}
const sk = (s = 11, c = DR.gold) => <svg width={s} height={s} viewBox="0 0 24 24" fill={c}><path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z"/></svg>;

function SHead() {
  return (
    <div style={{ padding: '12px 24px 18px' }}>
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
        <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke={DR.soft} strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><path d="M14 6l-6 6 6 6"/></svg>
        <span style={{ fontSize: 9.5, letterSpacing: 2, color: DR.mute, fontWeight: 700 }}>STAY · 6 NIGHTS</span>
        <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke={DR.soft} strokeWidth="1.6" strokeLinecap="round"><path d="M12 5v14M5 12h14"/></svg>
      </div>
      <h1 style={{ fontFamily: DR.serif, fontSize: 28, fontWeight: 500, letterSpacing: -0.6, lineHeight: 1, color: DR.ink, margin: '14px 0 0' }}>Where you sleep</h1>
    </div>
  );
}

// A stay segment on the spine. `nights` e.g. ['18','20'] → "18–20 · 2 nts".
// `gap` = unbooked (dashed). `who` = avatars. `secondary` = a co-stay (split).
function Seg({ nights, name, area, price, who, gap, dotOnly }) {
  const span = `${nights[0]}–${nights[1]}`;
  const nts = (+nights[1]) - (+nights[0]);
  return (
    <div style={{ display: 'grid', gridTemplateColumns: '64px 1fr', gap: 14 }}>
      {/* spine: night range + dot + rule */}
      <div style={{ position: 'relative', textAlign: 'right', paddingRight: 16 }}>
        <div style={{ fontFamily: DR.serif, fontSize: 19, fontWeight: 500, color: DR.ink, letterSpacing: -0.4, lineHeight: 1 }}>{span}</div>
        <div style={{ fontFamily: DR.mono, fontSize: 8, color: DR.faint, letterSpacing: 0.8, fontWeight: 600, marginTop: 4 }}>{nts} {nts === 1 ? 'NIGHT' : 'NIGHTS'}</div>
        {/* dot on the rail */}
        <span style={{ position: 'absolute', right: -5, top: 4, width: 9, height: 9, borderRadius: 999, background: gap ? DR.paper : DR.ink, border: gap ? `1.5px solid ${DR.gold}` : 'none', zIndex: 1 }}/>
      </div>
      {/* accommodation block */}
      <div style={{ position: 'relative', paddingBottom: 22 }}>
        {/* connecting rule */}
        <span style={{ position: 'absolute', left: -16, top: 5, bottom: -5, width: 1, background: DR.hairThin }}/>
        {gap ? (
          <div style={{ borderRadius: 12, border: `1.2px dashed ${DR.gold}`, background: 'rgba(176,133,58,0.05)', padding: '13px 15px' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: 6, marginBottom: 5 }}>{sk(11)}<span style={{ fontSize: 8.5, letterSpacing: 1.4, color: DR.goldDeep, fontWeight: 700 }}>UNBOOKED · 1 OF 4 LEFT</span></div>
            <div style={{ fontFamily: DR.serif, fontSize: 16, color: DR.ink, letterSpacing: -0.2, lineHeight: 1.2 }}>Casa do Alecrim <span style={{ fontStyle: 'italic', color: DR.mute }}>— the one I’d hold</span></div>
            <div style={{ display: 'flex', gap: 14, marginTop: 9 }}><span style={{ fontSize: 12.5, fontWeight: 600, color: DR.blue }}>Hold it →</span><span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 12.5, color: DR.mute }}>see other two</span></div>
          </div>
        ) : (
          <div>
            <div style={{ display: 'flex', alignItems: 'flex-start', justifyContent: 'space-between', gap: 10 }}>
              <div style={{ minWidth: 0 }}>
                <div style={{ fontFamily: DR.serif, fontSize: 18, fontWeight: 500, color: DR.ink, letterSpacing: -0.3, lineHeight: 1.1 }}>{name}</div>
                <div style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 12.5, color: DR.mute, marginTop: 3 }}>{area}</div>
              </div>
              <SAvStack who={who} ring={DR.paper}/>
            </div>
            <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginTop: 9 }}>
              <span style={{ fontFamily: DR.mono, fontSize: 8.5, color: DR.mute, letterSpacing: 0.8, fontWeight: 600 }}>{price}</span>
              <span style={{ width: 3, height: 3, borderRadius: 3, background: DR.faint }}/>
              <span style={{ fontSize: 11, color: DR.blue, fontWeight: 600 }}>Confirmed</span>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

// A co-stay that shares the previous segment's range (the split case).
function CoSeg({ name, area, who }) {
  return (
    <div style={{ display: 'grid', gridTemplateColumns: '64px 1fr', gap: 14, marginTop: -12 }}>
      <div style={{ position: 'relative', textAlign: 'right', paddingRight: 16 }}>
        <span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 11, color: DR.faint }}>also</span>
        <span style={{ position: 'absolute', right: -3.5, top: 4, width: 6, height: 6, borderRadius: 999, background: DR.faint, zIndex: 1 }}/>
      </div>
      <div style={{ position: 'relative', paddingBottom: 22 }}>
        <span style={{ position: 'absolute', left: -16, top: 5, bottom: -5, width: 1, background: DR.hairThin, borderLeft: `1px dotted ${DR.hairThin}` }}/>
        <div style={{ display: 'flex', alignItems: 'flex-start', justifyContent: 'space-between', gap: 10 }}>
          <div style={{ minWidth: 0 }}>
            <div style={{ fontFamily: DR.serif, fontSize: 16, fontWeight: 500, color: DR.soft, letterSpacing: -0.2, lineHeight: 1.1 }}>{name}</div>
            <div style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 12, color: DR.mute, marginTop: 3 }}>{area}</div>
          </div>
          <SAvStack who={who} ring={DR.paper}/>
        </div>
      </div>
    </div>
  );
}

// V1 · everyone together, with the unbooked gap
function StayNew1() {
  return (
    <Phone bg={DR.paper}><div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
      <SHead/>
      <div style={{ padding: '0 22px' }}>
        <Seg nights={['18','20']} name="Casa do Alecrim" area="Alfama · a tiled house above the wall" price="€180/NT" who={['T','A','M']}/>
        <Seg nights={['20','22']} gap/>
        <Seg nights={['22','24']} name="Tivoli" area="Cais · river rooms" price="€240/NT" who={['T','A','M']}/>
      </div>
    </div><TabBar active="trips"/></Phone>
  );
}

// V2 · the split — Mara peels off to her own stay for the middle nights
function StayNew2() {
  return (
    <Phone bg={DR.paper}><div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
      <SHead/>
      <div style={{ padding: '0 22px' }}>
        <Seg nights={['18','22']} name="Casa do Alecrim" area="Alfama · two rooms" price="€180/NT" who={['T','A']}/>
        <CoSeg name="Solar dos Mouros" area="Castelo · Mara wanted the view" who={['M']}/>
        <Seg nights={['22','24']} name="Tivoli" area="Cais · all three again" price="€240/NT" who={['T','A','M']}/>
      </div>
    </div><TabBar active="trips"/></Phone>
  );
}

// Ghost avatar — an undecided traveler (outline only).
function GhostAv({ who, s = 18 }) {
  return <div style={{ width: s, height: s, borderRadius: 999, background: 'transparent', color: SPEEP[who], fontFamily: DR.serif, fontSize: s * 0.46, fontWeight: 500, display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0, border: `1.2px dashed ${SPEEP[who]}`, opacity: 0.8 }}>{who}</div>;
}

// V3 · partial — some committed, some still deciding (pending tray)
function StayNew3() {
  return (
    <Phone bg={DR.paper}><div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
      <SHead/>
      <div style={{ padding: '0 22px' }}>
        {/* committed stay — only You so far */}
        <div style={{ display: 'grid', gridTemplateColumns: '64px 1fr', gap: 14 }}>
          <div style={{ position: 'relative', textAlign: 'right', paddingRight: 16 }}>
            <div style={{ fontFamily: DR.serif, fontSize: 19, fontWeight: 500, color: DR.ink, letterSpacing: -0.4, lineHeight: 1 }}>18–22</div>
            <div style={{ fontFamily: DR.mono, fontSize: 8, color: DR.faint, letterSpacing: 0.8, fontWeight: 600, marginTop: 4 }}>4 NIGHTS</div>
            <span style={{ position: 'absolute', right: -5, top: 4, width: 9, height: 9, borderRadius: 999, background: DR.ink, zIndex: 1 }}/>
          </div>
          <div style={{ position: 'relative', paddingBottom: 16 }}>
            <span style={{ position: 'absolute', left: -16, top: 5, bottom: -5, width: 1, background: DR.hairThin }}/>
            <div style={{ display: 'flex', alignItems: 'flex-start', justifyContent: 'space-between', gap: 10 }}>
              <div><div style={{ fontFamily: DR.serif, fontSize: 18, fontWeight: 500, color: DR.ink, letterSpacing: -0.3, lineHeight: 1.1 }}>Casa do Alecrim</div><div style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 12.5, color: DR.mute, marginTop: 3 }}>Alfama · you’re in</div></div>
              <SAvStack who={['T']} ring={DR.paper}/>
            </div>
            <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginTop: 9 }}><span style={{ fontFamily: DR.mono, fontSize: 8.5, color: DR.mute, letterSpacing: 0.8, fontWeight: 600 }}>€180/NT</span><span style={{ width: 3, height: 3, borderRadius: 3, background: DR.faint }}/><span style={{ fontSize: 11, color: DR.blue, fontWeight: 600 }}>Confirmed · 1 room free</span></div>
          </div>
        </div>
        {/* pending tray — undecided travelers pooled */}
        <div style={{ display: 'grid', gridTemplateColumns: '64px 1fr', gap: 14, marginTop: -6 }}>
          <div style={{ position: 'relative', textAlign: 'right', paddingRight: 16 }}>
            <span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 11, color: DR.faint }}>same<br/>nights</span>
            <span style={{ position: 'absolute', right: -3.5, top: 4, width: 6, height: 6, borderRadius: 999, background: DR.paper, border: `1.2px dashed ${DR.faint}`, zIndex: 1 }}/>
          </div>
          <div style={{ paddingBottom: 22 }}>
            <div style={{ borderRadius: 12, border: `1.2px dashed ${DR.faint}`, padding: '13px 15px', background: 'rgba(27,23,20,0.015)' }}>
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: 9 }}>
                  <div style={{ display: 'flex' }}>{['A','M'].map((w, i) => <span key={w} style={{ marginLeft: i ? -5 : 0 }}><GhostAv who={w}/></span>)}</div>
                  <span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 13.5, color: DR.soft }}>Ana &amp; Mara haven’t picked</span>
                </div>
              </div>
              <div style={{ display: 'flex', gap: 14, marginTop: 11 }}>
                <span style={{ fontSize: 12, fontWeight: 600, color: DR.blue }}>Join your stay →</span>
                <span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 12, color: DR.mute }}>nudge them</span>
              </div>
            </div>
          </div>
        </div>
        {/* Vesper read on the indecision */}
        <div style={{ display: 'grid', gridTemplateColumns: '64px 1fr', gap: 14 }}>
          <div/>
          <div style={{ paddingLeft: 0 }}>
            <div style={{ paddingLeft: 13, borderLeft: `2px solid ${DR.gold}` }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: 6, marginBottom: 5 }}>{sk(11)}<span style={{ fontSize: 8.5, letterSpacing: 1.4, color: DR.goldDeep, fontWeight: 700 }}>VESPER</span></div>
              <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 14, color: DR.ink, margin: 0, lineHeight: 1.4, letterSpacing: -0.1 }}>Your room has a spare bed — if Ana joins, the split drops to €60 each.</p>
            </div>
          </div>
        </div>
      </div>
    </div><TabBar active="trips"/></Phone>
  );
}

Object.assign(window, { StayNew1, StayNew2, StayNew3 });
