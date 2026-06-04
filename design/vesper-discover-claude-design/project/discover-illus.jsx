// ═══════════════════════════════════════════════════════════════
// VESPER ILLUSTRATIONS — a house illustration style that gives every
// place a "face", shared with the Atlas cards. The read becomes a
// captioned field-sketch: an illustration carries the feeling, a few
// annotated pins carry the meaning (each opens a lensed dossier).
// Reuses discover-kit (D, Spark, DIcon, SegControl) + DiscoverTop.
// ═══════════════════════════════════════════════════════════════

// A crafted Lisbon scene in Vesper's house style — warm, layered,
// hand-inked, gold accents. Tonal bands (no loud gradient) + grain.
function VesperScene({ w = 360, h = 220, time = 'amber' }) {
  const pal = time === 'amber'
    ? { s1: '#E9B98C', s2: '#E8A98A', s3: '#D98A78', hill: '#B66B45', hill2: '#9C5436', roof: '#C2724A', river: '#C9A98B', ink: '#4A3526', glow: '#F4D08A' }
    : { s1: '#D7CBB0', s2: '#CFC4A8', s3: '#C3B59A', hill: '#A98C66', hill2: '#8E7252', roof: '#B08A5E', river: '#A9B4AE', ink: '#4A3D2C', glow: '#E6D29A' };
  return (
    <div style={{ position: 'relative', width: w, height: h, overflow: 'hidden', background: pal.s1 }}>
      <svg width="100%" height="100%" viewBox="0 0 360 220" preserveAspectRatio="xMidYMid slice">
        {/* sky bands */}
        <rect width="360" height="220" fill={pal.s1}/>
        <rect y="44" width="360" height="44" fill={pal.s2}/>
        <rect y="88" width="360" height="34" fill={pal.s3}/>
        {/* sun glow */}
        <circle cx="278" cy="52" r="30" fill={pal.glow} opacity="0.55"/>
        <circle cx="278" cy="52" r="18" fill={pal.glow} opacity="0.7"/>
        {/* river */}
        <rect y="120" width="360" height="26" fill={pal.river} opacity="0.8"/>
        <path d="M0 132 H360" stroke="#fff" strokeWidth="0.5" opacity="0.3"/>
        {/* far hill of houses */}
        {Array.from({ length: 7 }).map((_, r) => (
          <g key={r}>
            {Array.from({ length: 11 }).map((_, c) => {
              const x = c * 34 + (r % 2 ? 14 : -6), y = 96 - r * 4 + (c % 3) * 2, hh = 16 + (c % 3) * 5;
              if (y > 118) return null;
              return <rect key={c} x={x} y={y - hh + 16} width="22" height={hh} fill={r % 2 ? pal.hill : pal.hill2} opacity="0.9"/>;
            })}
          </g>
        ))}
        {/* a dome */}
        <g>
          <ellipse cx="150" cy="74" rx="17" ry="15" fill={pal.roof}/>
          <rect x="145" y="56" width="10" height="12" fill={pal.roof}/>
          <circle cx="150" cy="53" r="2.5" fill={pal.ink}/>
        </g>
        {/* foreground rooftops */}
        {Array.from({ length: 9 }).map((_, c) => {
          const x = c * 44 - 10;
          return <path key={c} d={`M${x} 146 L${x + 22} 124 L${x + 44} 146 Z`} fill={c % 2 ? pal.roof : pal.hill2} opacity="0.95"/>;
        })}
        <rect y="144" width="360" height="76" fill={pal.hill2} opacity="0.96"/>
        {/* warm windows */}
        {Array.from({ length: 46 }).map((_, i) => (
          <rect key={i} x={(i * 53) % 352 + 4} y={150 + ((i * 31) % 60)} width="3.5" height="5" rx="0.5" fill={pal.glow} opacity="0.85"/>
        ))}
        {/* foreground miradouro railing */}
        <g stroke={pal.ink} strokeWidth="1.4" opacity="0.85">
          <path d="M0 206 H360"/>
          {Array.from({ length: 19 }).map((_, i) => <path key={i} d={`M${i * 20 + 6} 206 V218`}/>)}
          <path d="M0 200 H360" strokeWidth="2"/>
        </g>
        {/* parasol pine */}
        <g>
          <path d="M40 200 V150" stroke={pal.ink} strokeWidth="2"/>
          <ellipse cx="40" cy="142" rx="30" ry="13" fill={pal.hill2}/>
          <ellipse cx="40" cy="136" rx="20" ry="10" fill={pal.hill}/>
        </g>
        {/* a tram */}
        <g transform="translate(300 182)">
          <rect width="34" height="16" rx="2" fill={pal.glow}/>
          <rect x="3" y="3" width="9" height="6" fill={pal.ink} opacity="0.6"/>
          <rect x="15" y="3" width="9" height="6" fill={pal.ink} opacity="0.6"/>
          <circle cx="8" cy="17" r="2" fill={pal.ink}/><circle cx="26" cy="17" r="2" fill={pal.ink}/>
        </g>
      </svg>
      {/* grain */}
      <div style={{ position: 'absolute', inset: 0, opacity: 0.5, pointerEvents: 'none', backgroundImage: 'radial-gradient(rgba(40,28,16,0.12) 0.5px, transparent 0.6px)', backgroundSize: '3px 3px' }}/>
    </div>
  );
}

// An annotation pin placed on the scene → opens a lensed dossier.
function Pin({ x, y, n, label, lens, side = 'right' }) {
  return (
    <div style={{ position: 'absolute', left: x, top: y, display: 'flex', flexDirection: side === 'left' ? 'row-reverse' : 'row', alignItems: 'center', gap: 7 }}>
      <div style={{ width: 20, height: 20, borderRadius: 999, background: 'rgba(255,255,255,0.92)', border: `1.5px solid ${D.vesper}`, display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0, boxShadow: '0 2px 6px rgba(0,0,0,0.2)' }}>
        <span style={{ fontFamily: T.serif, fontSize: 11, fontWeight: 600, color: D.vesperDeep }}>{n}</span>
      </div>
      <div style={{ background: 'rgba(255,255,255,0.92)', borderRadius: 8, padding: '4px 9px', boxShadow: '0 2px 8px rgba(0,0,0,0.16)', backdropFilter: 'blur(4px)' }}>
        <div style={{ fontFamily: T.serif, fontSize: 12.5, fontWeight: 500, color: T.ink, letterSpacing: -0.1, lineHeight: 1 }}>{label}</div>
        <div style={{ fontSize: 7.5, letterSpacing: 1, color: D.vesper, fontWeight: 700, marginTop: 2 }}>{lens.toUpperCase()} →</div>
      </div>
    </div>
  );
}

// ─── THE ILLUSTRATED READ ───────────────────────────────────────
function IllustratedRead() {
  return (
    <Phone bg={T.bg}>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
        <DiscoverTop place="Lisbon" context="Lisbon · in 3 weeks" active={1}/>
        <div style={{ padding: '16px 16px 0' }}>
          <div style={{ background: T.cardWarm, borderRadius: 16, border: `0.5px solid ${T.hairline}`, overflow: 'hidden', boxShadow: '0 1px 0 rgba(255,255,255,0.6) inset, 0 10px 26px -18px rgba(0,0,0,0.2)' }}>
            {/* illustration hero, annotated */}
            <div style={{ position: 'relative' }}>
              <VesperScene w={361} h={216} time="amber"/>
              <div style={{ position: 'absolute', top: 12, left: 12, display: 'flex', alignItems: 'center', gap: 6 }}>
                <Spark s={13} c="#fff"/>
                <span style={{ fontSize: 9.5, letterSpacing: 1.6, fontWeight: 700, color: '#fff' }}>VESPER’S READ</span>
              </div>
              <Pin x={150} y={40} n="1" label="the miradouros" lens="Why here"/>
              <Pin x={26} y={120} n="2" label="tilework" lens="Ritual"/>
              <Pin x={224} y={150} n="3" label="skip tram 28 at noon" lens="A day in"/>
            </div>
            {/* one line, not a paragraph */}
            <div style={{ padding: '13px 16px 14px' }}>
              <div style={{ fontSize: 10, letterSpacing: 1.4, color: D.earth, fontWeight: 700 }}>LISBON · FOR MAY 18–24</div>
              <p style={{ fontFamily: T.serif, fontSize: 18, fontWeight: 500, color: T.ink, letterSpacing: -0.3, lineHeight: 1.2, margin: '6px 0 0' }}>
                Read it <span style={{ fontStyle: 'italic' }}>from above</span> — three weeks to learn the city’s angles.
              </p>
            </div>
          </div>
          <div style={{ marginTop: 10, fontSize: 10.5, color: T.muteSoft, fontStyle: 'italic', fontFamily: T.serif, textAlign: 'center' }}>
            tap a mark on the sketch to open that read
          </div>
        </div>
      </div>
      <TabBar active="discover"/>
    </Phone>
  );
}

// ─── PLACE PORTRAIT — same house style as an Atlas-like card ────
function PlacePortrait() {
  return (
    <Phone bg={T.bg}>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
        <DiscoverTop place="Lisbon" context="Lisbon · Vesper’s own read" active={1}/>
        <div style={{ padding: '16px 16px 0' }}>
          {/* portrait card */}
          <div style={{ background: T.cardWarm, borderRadius: 16, border: `0.5px solid ${T.hairline}`, overflow: 'hidden', boxShadow: '0 1px 0 rgba(255,255,255,0.6) inset, 0 10px 26px -18px rgba(0,0,0,0.2)' }}>
            <VesperScene w={361} h={150} time="amber"/>
            <div style={{ padding: '14px 16px 15px' }}>
              <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between' }}>
                <h2 style={{ fontFamily: T.serif, fontSize: 30, fontWeight: 500, letterSpacing: -0.7, color: T.ink, margin: 0, lineHeight: 1 }}>Lisbon</h2>
                <span style={{ display: 'inline-flex', alignItems: 'center', gap: 4, fontSize: 10, color: D.vesperDeep, fontWeight: 700, letterSpacing: 1 }}><Spark s={11}/> THE CANON</span>
              </div>
              <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 14, color: T.mute, lineHeight: 1.35, margin: '8px 0 0' }}>
                A city that reads from above — and takes its fado closer to grief than to nightlife.
              </p>
              <div style={{ marginTop: 12, display: 'flex', gap: 6, flexWrap: 'wrap' }}>
                {[['Why here', D.vesper], ['The debate', '#A04030'], ['Insider', D.earth]].map(([l, c]) => (
                  <span key={l} style={{ display: 'inline-flex', alignItems: 'center', gap: 5, padding: '5px 10px', borderRadius: 999, background: T.bg, border: `0.5px solid ${T.hairline}`, fontFamily: T.serif, fontSize: 12.5, color: T.ink }}>
                    <span style={{ width: 5, height: 5, borderRadius: 5, background: c }}/>{l}
                  </span>
                ))}
              </div>
            </div>
          </div>
          <div style={{ marginTop: 14, padding: '0 6px' }}>
            <SectionLabel right="VESPER">THREE LENSES ON LISBON</SectionLabel>
          </div>
        </div>
      </div>
      <TabBar active="discover"/>
    </Phone>
  );
}

Object.assign(window, { VesperScene, Pin, IllustratedRead, PlacePortrait });
