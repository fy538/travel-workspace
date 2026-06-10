// ═══════════════════════════════════════════════════════════════
// ROUTE · the spatial surface. The illustrated map is the HERO, at three
// zooms — trip shape (far) · city (mid) · day's path (near) — plus the
// live you-are-here state. Styled-tile look (riso render layer) with
// editorial pins + Vesper annotations. Reuses DR + SPEEP.
// ═══════════════════════════════════════════════════════════════

const RPC = { T: '#A0703A', A: '#7C8F73', M: '#3D5066' };
const rsk = (s = 11, c = DR.gold) => <svg width={s} height={s} viewBox="0 0 24 24" fill={c}><path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z"/></svg>;

function RFrame({ children, dark }) {
  return <Phone bg={dark ? DR.ink : DR.paper}><div style={{ position: 'absolute', inset: 0, overflow: 'hidden', background: dark ? DR.ink : DR.paper }}>{children}</div><TabBar active="trips"/></Phone>;
}
// floating top controls over a map
function RControls({ zoom, onDark }) {
  const c = onDark ? '#fff' : DR.soft;
  const bg = onDark ? 'rgba(255,255,255,0.2)' : DR.card;
  return (
    <div style={{ position: 'absolute', top: 54, left: 16, right: 16, display: 'flex', alignItems: 'center', justifyContent: 'space-between', zIndex: 5 }}>
      <div style={{ width: 36, height: 36, borderRadius: 999, background: bg, backdropFilter: 'blur(8px)', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><path d="M14 6l-6 6 6 6"/></svg>
      </div>
      {/* zoom segmented */}
      <div style={{ display: 'inline-flex', background: bg, backdropFilter: 'blur(8px)', borderRadius: 999, padding: 3 }}>
        {[['trip', 'Trip'], ['city', 'City'], ['day', 'Day']].map(([k, l]) => (
          <span key={k} style={{ padding: '6px 13px', borderRadius: 999, fontSize: 12, fontWeight: zoom === k ? 600 : 500, color: zoom === k ? DR.ink : (onDark ? 'rgba(255,255,255,0.85)' : DR.mute), background: zoom === k ? (onDark ? 'rgba(255,255,255,0.92)' : DR.paper) : 'transparent', letterSpacing: -0.1 }}>{l}</span>
        ))}
      </div>
    </div>
  );
}
// a Vesper annotation card that floats at the bottom of the map
function RNote({ children, action }) {
  return (
    <div style={{ position: 'absolute', left: 16, right: 16, bottom: 96, background: DR.paper, borderRadius: 16, padding: '13px 15px', border: `0.5px solid ${DR.hair}`, boxShadow: '0 12px 30px -14px rgba(0,0,0,0.3)', zIndex: 5 }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 6, marginBottom: 5 }}>{rsk(11)}<span style={{ fontSize: 8.5, letterSpacing: 1.4, color: DR.goldDeep, fontWeight: 700 }}>VESPER</span></div>
      <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 14.5, color: DR.ink, margin: 0, lineHeight: 1.4, letterSpacing: -0.1 }}>{children}</p>
      {action && <div style={{ marginTop: 9, fontSize: 12.5, color: DR.blue, fontWeight: 600 }}>{action}</div>}
    </div>
  );
}
// editorial pin
function Pin({ x, y, label, kind = 'saved', sub }) {
  const col = kind === 'stay' ? DR.blue : kind === 'now' ? '#3D7050' : DR.ink;
  return (
    <div style={{ position: 'absolute', left: x, top: y, transform: 'translate(-50%,-100%)', display: 'flex', flexDirection: 'column', alignItems: 'center', zIndex: 3 }}>
      <div style={{ background: DR.paper, borderRadius: 999, padding: '3px 9px', border: `0.5px solid ${DR.hair}`, boxShadow: '0 4px 10px -4px rgba(0,0,0,0.25)', whiteSpace: 'nowrap' }}>
        <span style={{ fontFamily: DR.serif, fontSize: 12, fontWeight: 500, color: DR.ink, letterSpacing: -0.1 }}>{label}</span>
        {sub && <span style={{ fontFamily: DR.mono, fontSize: 7.5, color: DR.mute, letterSpacing: 0.5, marginLeft: 5 }}>{sub}</span>}
      </div>
      <span style={{ width: 9, height: 9, borderRadius: 999, background: col, border: `2px solid ${DR.paper}`, marginTop: -1, boxShadow: kind === 'now' ? `0 0 0 5px rgba(61,112,80,0.25)` : kind === 'stay' ? `0 0 0 4px rgba(61,80,102,0.16)` : 'none' }}/>
    </div>
  );
}

// ── styled-tile map base (riso render layer over real-ish geography) ──
function MapBase({ variant = 'city', h = 'full' }) {
  // warm tonal land + cooler water + faint street grid → reads as a styled tile
  return (
    <svg width="100%" height="100%" viewBox="0 0 393 720" preserveAspectRatio="xMidYMid slice" style={{ position: 'absolute', inset: 0 }}>
      <rect width="393" height="720" fill="#E7DCC6"/>
      {/* water body */}
      <path d="M0 540 Q120 500 230 560 T393 540 L393 720 L0 720 Z" fill="#9DB0AC" opacity="0.6"/>
      <path d="M0 540 Q120 500 230 560 T393 540" stroke="#7E938E" strokeWidth="0.8" fill="none" opacity="0.5"/>
      {/* parks */}
      <ellipse cx="300" cy="200" rx="70" ry="50" fill="#B6C29A" opacity="0.5"/>
      <ellipse cx="70" cy="380" rx="46" ry="60" fill="#B6C29A" opacity="0.45"/>
      {/* street grid — faint, slightly organic */}
      <g stroke="#CBBA9C" strokeWidth="0.7" opacity="0.7" fill="none">
        {[60, 120, 180, 240, 300, 360, 420, 480].map((y, i) => <path key={`h${i}`} d={`M0 ${y} Q200 ${y - 12} 393 ${y}`}/>)}
        {[50, 110, 170, 230, 290, 350].map((x, i) => <path key={`v${i}`} d={`M${x} 40 Q${x + 10} 280 ${x} 520`}/>)}
      </g>
      {/* a couple of bolder avenues */}
      <path d="M30 80 Q160 240 250 520" stroke="#BDA77E" strokeWidth="2.4" fill="none" opacity="0.7"/>
      <path d="M0 300 Q200 270 393 330" stroke="#BDA77E" strokeWidth="2.4" fill="none" opacity="0.7"/>
      {/* grain */}
      <rect width="393" height="720" fill="url(#rgrain)" opacity="0.5"/>
      <defs><pattern id="rgrain" width="3" height="3" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r="0.4" fill="rgba(60,40,24,0.5)"/></pattern></defs>
    </svg>
  );
}

// ─── 1 · TRIP SHAPE (far zoom) — multi-city across a region ───
function RouteTrip() {
  return (
    <RFrame>
      <div style={{ position: 'absolute', inset: 0 }}>
        {/* region base — more abstract */}
        <svg width="100%" height="100%" viewBox="0 0 393 720" preserveAspectRatio="xMidYMid slice" style={{ position: 'absolute', inset: 0 }}>
          <rect width="393" height="720" fill="#E7DCC6"/>
          <path d="M0 0 L393 0 L393 300 Q250 340 150 300 Q60 270 0 320 Z" fill="#DED2B8" opacity="0.6"/>
          <path d="M0 560 Q200 520 393 580 L393 720 L0 720 Z" fill="#9DB0AC" opacity="0.55"/>
          <rect width="393" height="720" fill="url(#rgrain2)" opacity="0.5"/>
          <defs><pattern id="rgrain2" width="3" height="3" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r="0.4" fill="rgba(60,40,24,0.5)"/></pattern></defs>
        </svg>
        {/* trip line across cities */}
        <svg width="100%" height="100%" viewBox="0 0 393 720" preserveAspectRatio="xMidYMid slice" style={{ position: 'absolute', inset: 0 }}>
          <path d="M120 470 Q90 360 150 300 Q220 240 270 180" stroke={DR.gold} strokeWidth="2" strokeDasharray="2 5" fill="none" strokeLinecap="round"/>
        </svg>
        <Pin x="120" y="490" label="Lisbon" kind="stay" sub="4 NTS"/>
        <Pin x="150" y="320" label="Sintra" sub="DAY"/>
        <Pin x="270" y="200" label="Porto" kind="saved" sub="2 NTS"/>
      </div>
      <RControls zoom="trip"/>
      <RNote action="See the journey →">Three stops, north by train — Sintra’s a half-day off the Lisbon leg.</RNote>
    </RFrame>
  );
}

// ─── 2 · CITY (mid zoom) — your Lisbon, your pins ───
function RouteCity() {
  return (
    <RFrame>
      <div style={{ position: 'absolute', inset: 0 }}><MapBase variant="city"/></div>
      <Pin x="110" y="430" label="Casa do Alecrim" kind="stay" sub="STAY"/>
      <Pin x="230" y="300" label="Ramiro" kind="saved"/>
      <Pin x="300" y="380" label="Miradouro" kind="saved"/>
      <Pin x="180" y="520" label="Time Out" kind="saved"/>
      <RControls zoom="city"/>
      <RNote action="6 saved nearby →">Everything you’ve saved sits east of the river — your Lisbon is walkable in a day.</RNote>
    </RFrame>
  );
}

// ─── 3 · DAY'S PATH (near zoom) — today, in walking order + connectors ───
function RouteDay() {
  return (
    <RFrame>
      <div style={{ position: 'absolute', inset: 0 }}><MapBase variant="day"/></div>
      {/* walking path */}
      <svg width="100%" height="100%" viewBox="0 0 393 720" preserveAspectRatio="xMidYMid slice" style={{ position: 'absolute', inset: 0 }}>
        <path d="M90 470 Q150 420 200 360 Q250 300 300 250" stroke={DR.gold} strokeWidth="2.4" strokeDasharray="1 5" fill="none" strokeLinecap="round"/>
      </svg>
      <Pin x="90" y="490" label="Casa do Alecrim" kind="stay" sub="9:30"/>
      <Pin x="200" y="375" label="Kayaba" sub="10:00"/>
      <Pin x="300" y="265" label="Cemetery walk" sub="11:00"/>
      <RControls zoom="day"/>
      <RNote action="Walk me through →">Start at the café and go uphill — the long way’s prettier, and it’s mostly downhill home.</RNote>
    </RFrame>
  );
}

// ─── 4 · LIVE (in-trip you-are-here) ───
function RouteLive() {
  return (
    <RFrame dark>
      <div style={{ position: 'absolute', inset: 0 }}><MapBase variant="day"/><div style={{ position: 'absolute', inset: 0, background: 'rgba(20,14,9,0.12)' }}/></div>
      <svg width="100%" height="100%" viewBox="0 0 393 720" preserveAspectRatio="xMidYMid slice" style={{ position: 'absolute', inset: 0 }}>
        <path d="M150 430 Q220 380 300 300" stroke={DR.gold} strokeWidth="2.4" strokeDasharray="1 5" fill="none" strokeLinecap="round"/>
      </svg>
      {/* you-are-here */}
      <div style={{ position: 'absolute', left: 150, top: 430, transform: 'translate(-50%,-50%)', zIndex: 4 }}>
        <span style={{ display: 'block', width: 18, height: 18, borderRadius: 999, background: DR.blue, border: '3px solid #fff', boxShadow: '0 0 0 7px rgba(61,80,102,0.3)' }}/>
      </div>
      <Pin x="300" y="300" label="Kayaba" kind="now" sub="6 MIN"/>
      <RControls zoom="day" onDark/>
      <RNote action="Ana’s already there →">You’re 6 minutes from the café — next stop on today’s path.</RNote>
    </RFrame>
  );
}

Object.assign(window, { RouteTrip, RouteCity, RouteDay, RouteLive });
