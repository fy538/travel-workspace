// ─────────────────────────────────────────────────────────────
// DISCOVER KIT — shared atoms for the Discover tab + Dossier page.
// Discover is OUTSIDE-IN: Vesper's read on the public world. Sibling
// to Atlas (inside-out memory), but editorial/intelligence, not archive.
//
// Per brief: parchment surfaces, restrained ink, gold/earth accents,
// and VIOLET reserved strictly for when Vesper is speaking / attributed.
// Reuses T (design-system), Phone/TabBar/Marks, PostcardScene.
// ─────────────────────────────────────────────────────────────

const D = {
  // Vesper's voice — restrained muted violet (only when Vesper speaks)
  vesper:     '#675BA0',
  vesperDeep: '#4C4178',
  vesperSoft: 'rgba(103,91,160,0.10)',
  vesperRule: 'rgba(103,91,160,0.30)',
  // earth accents
  earth:      '#A6703C',
};

// ─── EDITORIAL PHOTO PLATE ──────────────────────────────────────
// Warm duotone scene placeholders standing in for editorial photography.
// variant: rooftops | coast | alley | square | hills | tiles
function Plate({ variant = 'rooftops', style, children, dim = 0 }) {
  return (
    <div style={{ position: 'relative', overflow: 'hidden', background: '#E7D9C4', ...style }}>
      <PlateScene variant={variant}/>
      {/* fine grain */}
      <div style={{
        position: 'absolute', inset: 0, opacity: 0.5, pointerEvents: 'none',
        backgroundImage: 'radial-gradient(rgba(40,28,16,0.10) 0.5px, transparent 0.6px)',
        backgroundSize: '3px 3px',
      }}/>
      {dim > 0 && <div style={{ position: 'absolute', inset: 0, background: `rgba(30,20,12,${dim})` }}/>}
      {children}
    </div>
  );
}

function PlateScene({ variant }) {
  const sky = '#E9DAC0', warm = '#C98A57', deep = '#9E5C36', ink = '#4A3526', sea = '#9DAEA8';
  if (variant === 'coast') {
    return (
      <svg width="100%" height="100%" viewBox="0 0 300 200" preserveAspectRatio="xMidYMid slice">
        <rect width="300" height="200" fill={sky}/>
        <rect y="70" width="300" height="70" fill={sea}/>
        <rect y="135" width="300" height="65" fill="#D8C7AC"/>
        <path d="M0 135 H300" stroke={ink} strokeWidth="0.5" opacity="0.3"/>
        {/* far promenade figures */}
        {[30,55,80,120,150,180,210,250,275].map((x,i)=>(<rect key={i} x={x} y={120-(i%3)} width="2.4" height={10+(i%3)*2} fill={ink} opacity="0.5"/>))}
        <circle cx="245" cy="42" r="16" fill="#EBC98F" opacity="0.7"/>
      </svg>
    );
  }
  if (variant === 'alley') {
    return (
      <svg width="100%" height="100%" viewBox="0 0 300 200" preserveAspectRatio="xMidYMid slice">
        <rect width="300" height="200" fill={sky}/>
        <path d="M0 0 H120 V200 H0Z" fill={warm}/>
        <path d="M300 0 H180 V200 H300Z" fill={deep}/>
        <path d="M120 0 L150 40 L150 200 L120 200Z" fill="#B5763F"/>
        <path d="M180 0 L150 40 L150 200 L180 200Z" fill="#7E4A2C"/>
        {/* windows */}
        {[40,80,120,160].map((y,i)=>(<g key={i}><rect x="30" y={y} width="20" height="26" fill={ink} opacity="0.5"/><rect x="240" y={y+10} width="20" height="26" fill={ink} opacity="0.55"/></g>))}
        <rect x="146" y="150" width="8" height="50" fill={ink} opacity="0.4"/>
      </svg>
    );
  }
  if (variant === 'square') {
    return (
      <svg width="100%" height="100%" viewBox="0 0 300 200" preserveAspectRatio="xMidYMid slice">
        <rect width="300" height="200" fill={sky}/>
        <rect y="110" width="300" height="90" fill="#D9C297"/>
        {/* paving */}
        {[40,90,140,190,240].map((x,i)=>(<path key={i} d={`M${x} 110 L${x-30} 200`} stroke="#C2A777" strokeWidth="0.8"/>))}
        <path d="M0 150 H300" stroke="#C2A777" strokeWidth="0.8"/>
        {/* arch facade */}
        <rect x="0" y="60" width="300" height="50" fill={warm}/>
        {[20,70,120,170,220,270].map((x,i)=>(<rect key={i} x={x} y="74" width="22" height="36" rx="11" fill={ink} opacity="0.45"/>))}
        {/* figures */}
        {[80,110,150,200,230].map((x,i)=>(<rect key={i} x={x} y={150-(i%2)*3} width="3" height={13+(i%2)*3} fill={ink} opacity="0.6"/>))}
      </svg>
    );
  }
  if (variant === 'hills') {
    return (
      <svg width="100%" height="100%" viewBox="0 0 300 200" preserveAspectRatio="xMidYMid slice">
        <rect width="300" height="200" fill="#D98C6A"/>
        <rect width="300" height="90" fill="#C9706A"/>
        <circle cx="230" cy="46" r="20" fill="#F0C98A" opacity="0.6"/>
        {/* hillside houses stacked */}
        {Array.from({length:7}).map((_,r)=>(
          <g key={r}>
            {Array.from({length:9}).map((_,c)=>{
              const x=c*34+(r%2?12:0)-10, y=70+r*18;
              return <rect key={c} x={x} y={y} width="26" height="18" fill={r%2?'#B86A45':'#9E5236'} opacity={0.85}/>;
            })}
          </g>
        ))}
        {/* warm windows */}
        {Array.from({length:30}).map((_,i)=>(<rect key={i} x={(i*37)%290+6} y={80+((i*23)%100)} width="3" height="4" fill="#F2CE86" opacity="0.8"/>))}
      </svg>
    );
  }
  if (variant === 'tiles') {
    return (
      <svg width="100%" height="100%" viewBox="0 0 300 200" preserveAspectRatio="xMidYMid slice">
        <rect width="300" height="200" fill="#C7B79A"/>
        {Array.from({length:8}).map((_,r)=>Array.from({length:12}).map((_,c)=>(
          <g key={`${r}-${c}`} transform={`translate(${c*26} ${r*26})`}>
            <rect width="26" height="26" fill={(r+c)%2?'#B7C4C9':'#9FB0B6'} opacity="0.9"/>
            <path d="M13 4 L22 13 L13 22 L4 13Z" fill="#7E9197" opacity="0.7"/>
          </g>
        )))}
      </svg>
    );
  }
  // rooftops (default)
  return (
    <svg width="100%" height="100%" viewBox="0 0 300 200" preserveAspectRatio="xMidYMid slice">
      <rect width="300" height="200" fill={sky}/>
      <rect y="120" width="300" height="80" fill={sea} opacity="0.5"/>
      {/* terracotta rooftops */}
      {Array.from({length:5}).map((_,r)=>(
        <g key={r}>
          {Array.from({length:8}).map((_,c)=>{
            const x=c*40+(r%2?18:-6), y=70+r*26;
            return <path key={c} d={`M${x} ${y+18} L${x+18} ${y} L${x+40} ${y+18}Z`} fill={r%2?warm:deep} opacity="0.92"/>;
          })}
        </g>
      ))}
      {/* dome */}
      <ellipse cx="210" cy="64" rx="22" ry="20" fill="#CBA86E"/>
      <rect x="204" y="40" width="12" height="14" fill="#CBA86E"/>
      {/* river band figures */}
      <path d="M0 120 H300" stroke={ink} strokeWidth="0.5" opacity="0.25"/>
    </svg>
  );
}

// ─── small marks ────────────────────────────────────────────────
const DIcon = {
  settings: (c = T.inkSoft) => <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.6" strokeLinecap="round"><path d="M5 7h9M18 7h1M5 12h1M10 12h9M5 17h5M14 17h5"/><circle cx="16" cy="7" r="2"/><circle cx="8" cy="12" r="2"/><circle cx="12" cy="17" r="2"/></svg>,
  saved: (c = T.inkSoft) => <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><path d="M7 4h10v16l-5-3.5L7 20z"/></svg>,
  search: (c = T.mute) => <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.7" strokeLinecap="round"><circle cx="11" cy="11" r="6.5"/><path d="M16 16l4 4"/></svg>,
  read: (c = T.ink) => <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"><path d="M4 5h7v15H5a1 1 0 0 1-1-1zM20 5h-7v15h6a1 1 0 0 0 1-1z"/></svg>,
  back: (c = T.ink) => <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d="M14 6l-6 6 6 6"/></svg>,
  save: (c = T.ink) => <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><path d="M7 4h10v16l-5-3.5L7 20z"/></svg>,
  share: (c = T.ink) => <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><path d="M12 3v13M8 7l4-4 4 4M5 13v6a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-6"/></svg>,
};

// ─── Vesper spark (violet) — Discover's attribution mark ────────
function Spark({ s = 13, c = D.vesper }) {
  return (
    <svg width={s} height={s} viewBox="0 0 24 24" fill={c}>
      <path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z"/>
      <path d="M18.5 15 L19.1 17.4 L21.5 18 L19.1 18.6 L18.5 21 L17.9 18.6 L15.5 18 L17.9 17.4 Z" opacity="0.85"/>
    </svg>
  );
}

// "+ Vesper" attribution (violet) — used on field-note cards.
function VesperBy({ label = 'Vesper' }) {
  return (
    <span style={{ display: 'inline-flex', alignItems: 'center', gap: 4, color: D.vesper, fontSize: 12.5, fontWeight: 600, letterSpacing: -0.1 }}>
      <span style={{ fontSize: 14, lineHeight: 1, marginRight: -1 }}>+</span> {label}
    </span>
  );
}

// FIELD NOTE eyebrow (violet dot).
function FieldEyebrow({ children = 'FIELD NOTE', c = D.vesper }) {
  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: 7 }}>
      <span style={{ width: 5, height: 5, borderRadius: 5, background: c }}/>
      <span style={{ fontSize: 9.5, letterSpacing: 1.8, fontWeight: 700, color: T.mute }}>{children}</span>
    </div>
  );
}

// Lens chip — the dossier type (Why here, A day in, For the obsessed, …)
function LensChip({ lens, onDark }) {
  return (
    <span style={{
      display: 'inline-flex', alignItems: 'center', gap: 5,
      fontSize: 9.5, letterSpacing: 1.6, fontWeight: 700,
      color: onDark ? 'rgba(255,255,255,0.92)' : D.vesperDeep,
      padding: '4px 9px', borderRadius: 999,
      background: onDark ? 'rgba(255,255,255,0.16)' : D.vesperSoft,
      backdropFilter: onDark ? 'blur(6px)' : 'none',
      textTransform: 'uppercase',
    }}>
      <Spark s={10} c={onDark ? 'rgba(255,255,255,0.92)' : D.vesper}/>
      {lens}
    </span>
  );
}

// ─── Segmented control — For you / Vesper / Friends ─────────────
// variant: 'underline' (editorial) | 'rail' (refined pill)
function SegControl({ tabs = ['For you', 'Vesper', 'Friends'], active = 0, variant = 'underline' }) {
  if (variant === 'rail') {
    return (
      <div style={{ display: 'inline-flex', background: 'rgba(27,23,20,0.05)', borderRadius: 999, padding: 3 }}>
        {tabs.map((t, i) => (
          <span key={t} style={{
            padding: '7px 16px', borderRadius: 999, fontSize: 13, fontWeight: i === active ? 600 : 500,
            color: i === active ? T.ink : T.mute,
            background: i === active ? T.cardWarm : 'transparent',
            boxShadow: i === active ? '0 1px 3px rgba(0,0,0,0.08)' : 'none',
            letterSpacing: -0.1,
          }}>{t}</span>
        ))}
      </div>
    );
  }
  return (
    <div style={{ display: 'flex', gap: 22, borderBottom: `0.5px solid ${T.hairline}` }}>
      {tabs.map((t, i) => (
        <div key={t} style={{ paddingBottom: 9, position: 'relative' }}>
          <span style={{
            fontFamily: i === active ? T.serif : T.sans,
            fontSize: i === active ? 17 : 14, fontWeight: i === active ? 500 : 500,
            color: i === active ? T.ink : T.mute, letterSpacing: -0.2,
            fontStyle: i === active && t === 'Vesper' ? 'italic' : 'normal',
          }}>{t}</span>
          {i === active && <div style={{ position: 'absolute', bottom: -0.5, left: 0, right: 0, height: 1.5, background: t === 'Vesper' ? D.vesper : T.ink }}/>}
        </div>
      ))}
    </div>
  );
}

// ─── Dossier sticky action bar ──────────────────────────────────
// Save / Ask Vesper / Share. Ask Vesper is the violet continuation.
function DossierBar({ variant = 'editorial' }) {
  const askBtn = (
    <span style={{
      flex: 1, display: 'inline-flex', alignItems: 'center', justifyContent: 'center', gap: 6,
      padding: '12px 0', background: D.vesper, color: '#fff', borderRadius: 999,
      fontSize: 13.5, fontWeight: 600, letterSpacing: -0.1,
    }}>
      <Spark s={13} c="#fff"/> Ask Vesper
    </span>
  );
  const ico = (icon, label) => (
    <span style={{ display: 'inline-flex', flexDirection: 'column', alignItems: 'center', gap: 3, color: T.inkSoft, width: 52 }}>
      {icon}
      <span style={{ fontSize: 9.5, fontWeight: 600, letterSpacing: 0.2 }}>{label}</span>
    </span>
  );
  return (
    <div style={{
      position: 'absolute', bottom: 0, left: 0, right: 0,
      padding: '12px 18px calc(12px + 8px)',
      background: 'rgba(247,242,231,0.9)', backdropFilter: 'blur(20px) saturate(180%)',
      borderTop: `0.5px solid ${T.hairline}`,
      display: 'flex', alignItems: 'center', gap: 14,
    }}>
      {variant === 'editorial' ? (
        <>
          <span style={{ display: 'inline-flex', alignItems: 'center', gap: 7, color: T.ink, fontSize: 13.5, fontWeight: 600 }}>
            {DIcon.save(T.ink)} Save to your world
          </span>
          <span style={{ marginLeft: 'auto', display: 'flex', gap: 16, alignItems: 'center' }}>
            {askBtn}
            {DIcon.share(T.inkSoft)}
          </span>
        </>
      ) : (
        <>
          {ico(DIcon.save(T.inkSoft), 'Save')}
          {askBtn}
          {ico(DIcon.share(T.inkSoft), 'Share')}
        </>
      )}
    </div>
  );
}

// Section label (editorial).
function SectionLabel({ children, right }) {
  return (
    <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between' }}>
      <span style={{ fontSize: 10, letterSpacing: 2, color: T.mute, fontWeight: 700 }}>{children}</span>
      {right && <span style={{ fontSize: 10, letterSpacing: 1.4, color: T.muteSoft, fontWeight: 600 }}>{right}</span>}
    </div>
  );
}

Object.assign(window, { D, Plate, PlateScene, DIcon, Spark, VesperBy, FieldEyebrow, LensChip, SegControl, DossierBar, SectionLabel });
