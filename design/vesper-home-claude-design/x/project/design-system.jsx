// Shared tokens, phone bezel, icons, tab bar, and tiny line-art SVG marks.

const T = {
  // Surfaces
  bg:        '#EFEAE0',   // warm paper
  bgDeep:    '#E8E2D4',
  card:      '#F7F2E7',
  cardWarm:  '#FBF7EC',
  cardSoft:  '#F3EEE3',

  // Ink
  ink:       '#1B1714',
  inkSoft:   '#2C2622',
  mute:      '#86807A',
  muteSoft:  '#B5AFA5',
  hairline:  'rgba(27,23,20,0.10)',
  hairThin:  'rgba(27,23,20,0.06)',

  // Accent
  gold:      '#B0853A',
  goldDeep:  '#8A6628',
  goldSoft:  '#D9BD86',

  // Type
  serif:  '"Cormorant Garamond", "EB Garamond", Georgia, serif',
  sans:   '"DM Sans", -apple-system, system-ui, sans-serif',
  mono:   '"JetBrains Mono", ui-monospace, monospace',
};

// ─── iPhone bezel — 393×852 ────────────────────────────────────
function Phone({ children, bg = T.bg }) {
  return (
    <div style={{
      width: 393, height: 852, borderRadius: 54,
      background: bg, position: 'relative', overflow: 'hidden',
      boxShadow:
        '0 0 0 11px #0d0b09, 0 0 0 12px #2a2622, ' +
        '0 30px 60px -20px rgba(0,0,0,0.35), 0 8px 30px -10px rgba(0,0,0,0.2)',
      fontFamily: T.sans, color: T.ink,
    }}>
      {/* Status bar */}
      <div style={{
        position: 'absolute', top: 0, left: 0, right: 0, height: 54,
        display: 'flex', alignItems: 'center', justifyContent: 'space-between',
        padding: '18px 32px 0', zIndex: 30, pointerEvents: 'none',
      }}>
        <span style={{ fontFamily: '-apple-system, SF Pro Display, system-ui',
          fontWeight: 600, fontSize: 17, color: T.ink, letterSpacing: -0.2 }}>9:41</span>
        <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
          {/* signal */}
          <svg width="18" height="11" viewBox="0 0 18 11">
            <rect x="0"  y="6" width="3" height="5" rx="0.6" fill={T.ink}/>
            <rect x="5"  y="4" width="3" height="7" rx="0.6" fill={T.ink}/>
            <rect x="10" y="2" width="3" height="9" rx="0.6" fill={T.ink}/>
            <rect x="15" y="0" width="3" height="11" rx="0.6" fill={T.ink}/>
          </svg>
          {/* wifi */}
          <svg width="16" height="11" viewBox="0 0 16 11">
            <path d="M8 2.5c2.2 0 4.2 0.85 5.7 2.3l1.1-1.1C13 1.9 10.6 0.8 8 0.8S3 1.9 1.2 3.7l1.1 1.1C3.8 3.35 5.8 2.5 8 2.5Z" fill={T.ink}/>
            <path d="M8 6c1.3 0 2.5 0.5 3.4 1.4l1.1-1.1C11.3 5 9.7 4.3 8 4.3S4.7 5 3.5 6.3l1.1 1.1C5.5 6.5 6.7 6 8 6Z" fill={T.ink}/>
            <circle cx="8" cy="9.5" r="1.4" fill={T.ink}/>
          </svg>
          {/* battery */}
          <svg width="26" height="12" viewBox="0 0 26 12">
            <rect x="0.4" y="0.4" width="22" height="11.2" rx="3" fill="none" stroke={T.ink} strokeOpacity="0.4"/>
            <rect x="2" y="2" width="19" height="8" rx="1.5" fill={T.ink}/>
            <path d="M24 4v4c0.7-0.3 1.2-1.05 1.2-2S24.7 4.3 24 4Z" fill={T.ink} fillOpacity="0.45"/>
          </svg>
        </div>
      </div>
      {/* Dynamic island */}
      <div style={{
        position: 'absolute', top: 11, left: '50%', transform: 'translateX(-50%)',
        width: 124, height: 37, borderRadius: 24, background: '#000', zIndex: 31,
      }} />
      {/* Screen content */}
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54 }}>
        {children}
      </div>
    </div>
  );
}

// ─── Bottom tab bar (consistent across variants) ────────────────
function TabBar({ active = 'atlas' }) {
  const tab = (key, label, icon) => {
    const on = active === key;
    return (
      <div style={{
        flex: 1, display: 'flex', flexDirection: 'column', alignItems: 'center',
        gap: 3, color: on ? T.ink : T.muteSoft, position: 'relative',
      }}>
        {icon(on ? T.ink : T.muteSoft)}
        <span style={{ fontSize: 10.5, fontWeight: on ? 600 : 500, letterSpacing: 0.2 }}>{label}</span>
      </div>
    );
  };
  return (
    <div style={{
      position: 'absolute', left: 14, right: 14, bottom: 14,
      background: 'rgba(247,242,231,0.85)',
      backdropFilter: 'blur(20px) saturate(180%)',
      WebkitBackdropFilter: 'blur(20px) saturate(180%)',
      borderRadius: 32, padding: '12px 14px 16px',
      display: 'flex', alignItems: 'center', justifyContent: 'space-between',
      boxShadow: '0 1px 0 rgba(255,255,255,0.6) inset, 0 8px 24px -8px rgba(0,0,0,0.12)',
      border: '0.5px solid rgba(0,0,0,0.06)', zIndex: 25,
    }}>
      {tab('trips','Trips', (c) => (
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.5" strokeLinecap="round">
          <rect x="3.5" y="7" width="17" height="13" rx="2.5"/>
          <path d="M9 7V5.5A1.5 1.5 0 0 1 10.5 4h3A1.5 1.5 0 0 1 15 5.5V7"/>
        </svg>
      ))}
      <div style={{ position: 'relative', flex: 1, display: 'flex', justifyContent: 'center' }}>
        {tab('vesper','Vesper', (c) => (
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.5" strokeLinejoin="round">
            <path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8L12 3Z"/>
          </svg>
        ))}
        <div style={{
          position: 'absolute', top: -2, right: 'calc(50% - 26px)',
          background: T.ink, color: '#FBF7EC', fontSize: 9.5, fontWeight: 600,
          padding: '2px 6px', borderRadius: 10, minWidth: 18, textAlign: 'center',
          lineHeight: 1.1,
        }}>10</div>
      </div>
      {tab('discover','Discover', (c) => (
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round">
          <circle cx="12" cy="12" r="8.5"/>
          <path d="M15 9l-1.4 4.6L9 15l1.4-4.6L15 9Z" fill={c} fillOpacity="0.15"/>
        </svg>
      ))}
      {tab('atlas','Atlas', (c) => (
        <svg width="22" height="22" viewBox="0 0 24 24" fill={c}>
          <path d="M5 4.5A1.5 1.5 0 0 1 6.5 3H11v17.5L7 19l-2 1V4.5Z"/>
          <path d="M13 3h4.5A1.5 1.5 0 0 1 19 4.5V20l-2-1-4 1.5V3Z" fillOpacity="0.55"/>
        </svg>
      ))}
    </div>
  );
}

// ─── Tiny line-art marks (geometric, restrained) ────────────────
const Marks = {
  Inbox: ({ size = 92, c = T.ink, accent = T.gold }) => (
    <svg width={size} height={size * 0.78} viewBox="0 0 120 94" fill="none">
      {/* tray */}
      <path d="M14 60 L60 78 L106 60 L106 76 Q106 80 102 81 L60 89 L18 81 Q14 80 14 76 Z"
            stroke={c} strokeWidth="1.2" strokeLinejoin="round"/>
      <path d="M14 60 L30 50 L30 18 Q30 14 34 14 L86 14 Q90 14 90 18 L90 50 L106 60"
            stroke={c} strokeWidth="1.2" strokeLinejoin="round"/>
      {/* letters peeking */}
      <rect x="38" y="22" width="44" height="28" rx="1" stroke={c} strokeWidth="1" opacity="0.55"/>
      <rect x="34" y="32" width="52" height="22" rx="1" stroke={c} strokeWidth="1"/>
      <path d="M34 32 L60 48 L86 32" stroke={c} strokeWidth="1"/>
      <circle cx="86" cy="20" r="3" fill={accent}/>
    </svg>
  ),
  Map: ({ size = 92, c = T.ink, accent = T.gold }) => (
    <svg width={size} height={size * 0.78} viewBox="0 0 120 94" fill="none">
      {/* folded panels */}
      <path d="M10 22 L40 14 L70 22 L100 14 L110 22 L110 76 L80 84 L50 76 L20 84 L10 76 Z"
            stroke={c} strokeWidth="1.2" strokeLinejoin="round" fill="none"/>
      <path d="M40 14 L40 76" stroke={c} strokeWidth="1" opacity="0.5"/>
      <path d="M70 22 L70 84" stroke={c} strokeWidth="1" opacity="0.5"/>
      <path d="M100 14 L100 76" stroke={c} strokeWidth="1" opacity="0.5"/>
      {/* contour lines */}
      <path d="M14 36 Q30 30 50 38 T108 32" stroke={c} strokeWidth="0.7" opacity="0.4"/>
      <path d="M14 50 Q34 44 56 52 T108 46" stroke={c} strokeWidth="0.7" opacity="0.4"/>
      <path d="M14 64 Q36 58 58 66 T108 60" stroke={c} strokeWidth="0.7" opacity="0.4"/>
      {/* route */}
      <path d="M28 70 Q40 50 56 56 Q74 62 86 40" stroke={accent} strokeWidth="1.4"
            strokeDasharray="2 3" strokeLinecap="round"/>
      <circle cx="28" cy="70" r="3" fill={accent}/>
      <circle cx="56" cy="56" r="3" fill={accent}/>
      <circle cx="86" cy="40" r="3" fill={accent}/>
    </svg>
  ),
  DNA: ({ size = 92, c = T.ink, accent = T.gold }) => (
    <svg width={size} height={size * 0.78} viewBox="0 0 120 94" fill="none">
      {/* fingerprint loops as concentric arcs */}
      <ellipse cx="60" cy="47" rx="22" ry="32" stroke={c} strokeWidth="1" fill="none"/>
      <ellipse cx="60" cy="47" rx="16" ry="24" stroke={c} strokeWidth="1" fill="none"/>
      <ellipse cx="60" cy="47" rx="10" ry="16" stroke={c} strokeWidth="1" fill="none"/>
      <ellipse cx="60" cy="47" rx="4"  ry="8"  stroke={c} strokeWidth="1" fill="none"/>
      {/* orbiting trace */}
      <path d="M26 18 Q14 50 28 78" stroke={c} strokeWidth="0.7" strokeDasharray="1 3" opacity="0.6"/>
      <path d="M94 18 Q106 50 92 78" stroke={c} strokeWidth="0.7" strokeDasharray="1 3" opacity="0.6"/>
      <circle cx="26" cy="18" r="2.5" fill={accent}/>
      <circle cx="94" cy="78" r="2.5" fill={accent}/>
      <circle cx="60" cy="47" r="1.6" fill={accent}/>
    </svg>
  ),
  Postcard: ({ size = 92, c = T.ink, accent = T.gold }) => (
    <svg width={size} height={size * 0.78} viewBox="0 0 120 94" fill="none">
      {/* back card */}
      <rect x="22" y="22" width="76" height="50" rx="2" transform="rotate(-6 60 47)"
            stroke={c} strokeWidth="1" fill="none" opacity="0.45"/>
      {/* front card */}
      <rect x="20" y="24" width="80" height="52" rx="2" transform="rotate(4 60 50)"
            stroke={c} strokeWidth="1.2" fill="none"/>
      {/* horizon */}
      <path d="M28 60 Q44 52 60 56 T96 52" stroke={c} strokeWidth="0.9" transform="rotate(4 60 50)"/>
      <path d="M28 64 L96 60" stroke={c} strokeWidth="0.5" opacity="0.5" transform="rotate(4 60 50)"/>
      {/* stamp */}
      <rect x="82" y="30" width="12" height="14" rx="0.5" transform="rotate(4 60 50)"
            stroke={c} strokeWidth="0.8" fill="none"/>
      <circle cx="88" cy="37" r="2" transform="rotate(4 60 50)" fill={accent}/>
      {/* mountain */}
      <path d="M40 60 L50 48 L58 55 L66 50 L72 60" stroke={c} strokeWidth="1" transform="rotate(4 60 50)" fill="none"/>
    </svg>
  ),

  // small inline glyphs
  ArrowR: ({ s = 14, c = T.ink }) => (
    <svg width={s} height={s} viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round">
      <path d="M5 12h14M13 6l6 6-6 6"/>
    </svg>
  ),
  Search: ({ s = 18, c = T.ink }) => (
    <svg width={s} height={s} viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.5" strokeLinecap="round">
      <circle cx="11" cy="11" r="6.5"/><path d="M16 16l4 4"/>
    </svg>
  ),
  Plus: ({ s = 16, c = T.ink }) => (
    <svg width={s} height={s} viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.6" strokeLinecap="round">
      <path d="M12 5v14M5 12h14"/>
    </svg>
  ),
  Stamp: ({ s = 18, c = T.ink }) => (
    <svg width={s} height={s} viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.4">
      <path d="M5 7c.6 0 1 .4 1 1s-.4 1-1 1V18h14V9c-.6 0-1-.4-1-1s.4-1 1-1V5H5Z"/>
    </svg>
  ),
};

Object.assign(window, { T, Phone, TabBar, Marks });
