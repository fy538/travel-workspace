// ═══════════════════════════════════════════════════════════════
// ILLUSTRATION STYLE EXPLORATION — the same Lisbon rooftop scene
// rendered in four techniques, so the house style can be chosen on
// evidence. Each is approximated with SVG/CSS (real art would be drawn).
// Standalone-ish: relies only on T (design-system).
// ═══════════════════════════════════════════════════════════════

// Shared geometry: a rooftop skyline + dome + river, drawn once, restyled.
// `pal` = ordered ink list; render mode varies per style.

const SCN = {
  // a compact set of roof triangles + a dome, as normalized coords
  roofs: [
    [10,72,30,58,50,72],[44,70,64,54,84,70],[78,74,98,60,118,74],
    [112,70,132,56,152,70],[148,73,168,59,188,73],[182,70,202,55,222,70],
    [216,74,236,60,256,74],[250,71,270,57,290,71],[284,73,304,60,324,73],
  ],
};

// ── 1 · RISO — 2-3 spot inks, multiply overprint, offset, halftone grain ──
function StyleRiso({ w = 300, h = 200 }) {
  const ink1 = '#C2553E', ink2 = '#3E5C74', ink3 = '#E3A33A'; // brick / blue / amber
  return (
    <div style={{ position: 'relative', width: w, height: h, overflow: 'hidden', background: '#EDE3D0' }}>
      {/* amber sky layer, offset */}
      <svg width={w} height={h} viewBox="0 0 300 200" preserveAspectRatio="xMidYMid slice" style={{ position: 'absolute', inset: 0, mixBlendMode: 'multiply', transform: 'translate(1.5px,-1px)' }}>
        <rect width="300" height="120" fill={ink3} opacity="0.5"/>
        <circle cx="232" cy="46" r="26" fill={ink3} opacity="0.7"/>
      </svg>
      {/* blue river + shadow layer, offset other way */}
      <svg width={w} height={h} viewBox="0 0 300 200" preserveAspectRatio="xMidYMid slice" style={{ position: 'absolute', inset: 0, mixBlendMode: 'multiply', transform: 'translate(-1.5px,1px)' }}>
        <rect y="120" width="300" height="80" fill={ink2} opacity="0.55"/>
        {SCN.roofs.map((r,i)=>(i%2===0)&&<path key={i} d={`M${r[0]} ${r[1]} L${r[2]} ${r[3]} L${r[4]} ${r[5]} Z`} fill={ink2} opacity="0.4"/>)}
      </svg>
      {/* brick rooftops main */}
      <svg width={w} height={h} viewBox="0 0 300 200" preserveAspectRatio="xMidYMid slice" style={{ position: 'absolute', inset: 0, mixBlendMode: 'multiply' }}>
        {SCN.roofs.map((r,i)=><path key={i} d={`M${r[0]} ${r[1]} L${r[2]} ${r[3]} L${r[4]} ${r[5]} Z`} fill={ink1} opacity="0.82"/>)}
        <ellipse cx="210" cy="60" rx="22" ry="20" fill={ink1} opacity="0.82"/>
        <rect x="204" y="38" width="12" height="16" fill={ink1} opacity="0.82"/>
      </svg>
      {/* halftone dot grain */}
      <div style={{ position: 'absolute', inset: 0, opacity: 0.5, mixBlendMode: 'multiply', backgroundImage: 'radial-gradient(rgba(60,40,24,0.55) 0.7px, transparent 0.8px)', backgroundSize: '3px 3px' }}/>
      <div style={{ position: 'absolute', inset: 0, opacity: 0.25, backgroundImage: 'radial-gradient(rgba(255,250,235,0.8) 0.6px, transparent 0.7px)', backgroundSize: '4px 4px', backgroundPosition: '1px 1px' }}/>
    </div>
  );
}

// ── 2 · ETCHING — monochrome ink, fine hatched shading ──
function StyleEtch({ w = 300, h = 200 }) {
  const ink = '#2A2018';
  return (
    <div style={{ position: 'relative', width: w, height: h, overflow: 'hidden', background: '#EFE7D6' }}>
      <svg width={w} height={h} viewBox="0 0 300 200" preserveAspectRatio="xMidYMid slice">
        <defs>
          <pattern id="hatchA" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(40)"><line x1="0" y1="0" x2="0" y2="5" stroke={ink} strokeWidth="0.6"/></pattern>
          <pattern id="hatchB" width="3.4" height="3.4" patternUnits="userSpaceOnUse" patternTransform="rotate(-35)"><line x1="0" y1="0" x2="0" y2="3.4" stroke={ink} strokeWidth="0.6"/></pattern>
        </defs>
        <rect width="300" height="200" fill="#EFE7D6"/>
        <rect y="120" width="300" height="80" fill="url(#hatchA)" opacity="0.5"/>
        <circle cx="232" cy="46" r="26" fill="none" stroke={ink} strokeWidth="0.8"/>
        {SCN.roofs.map((r,i)=>(
          <g key={i}>
            <path d={`M${r[0]} ${r[1]} L${r[2]} ${r[3]} L${r[4]} ${r[5]} Z`} fill={i%2?'url(#hatchB)':'url(#hatchA)'} stroke={ink} strokeWidth="0.7"/>
          </g>
        ))}
        <ellipse cx="210" cy="60" rx="22" ry="20" fill="url(#hatchB)" stroke={ink} strokeWidth="0.8"/>
        <rect x="204" y="38" width="12" height="16" fill="none" stroke={ink} strokeWidth="0.8"/>
        <path d="M0 120 H300" stroke={ink} strokeWidth="0.6"/>
      </svg>
    </div>
  );
}

// ── 3 · LINOCUT — 2 colors, bold carved shapes, high contrast ──
function StyleLino({ w = 300, h = 200 }) {
  const ink = '#22201C', paper = '#E8C97A';
  return (
    <div style={{ position: 'relative', width: w, height: h, overflow: 'hidden', background: paper }}>
      <svg width={w} height={h} viewBox="0 0 300 200" preserveAspectRatio="xMidYMid slice">
        <rect width="300" height="200" fill={paper}/>
        {/* carved sky marks */}
        {[20,46,70,96,120].map((y,i)=><rect key={i} x={20+i*8} y={y/4} width={120-i*14} height="2.4" fill={ink} opacity="0.5"/>)}
        <circle cx="232" cy="44" r="24" fill="none" stroke={ink} strokeWidth="3"/>
        {/* bold rooftops as one carved mass */}
        <path d="M0 120 L10 72 L30 58 L50 72 L64 54 L84 70 L98 60 L118 74 L132 56 L152 70 L168 59 L188 73 L202 55 L222 70 L236 60 L256 74 L270 57 L290 71 L300 66 L300 200 L0 200 Z" fill={ink}/>
        {/* carved windows (paper-colored knockouts) */}
        {[40,90,140,190,240].map((x,i)=><rect key={i} x={x} y={100+(i%2)*12} width="5" height="9" fill={paper}/>)}
        <ellipse cx="210" cy="58" rx="20" ry="18" fill={ink}/>
        <rect x="180" y="120" width="3" height="80" fill={paper} opacity="0.4"/>
      </svg>
    </div>
  );
}

// ── 4 · GOUACHE — soft painterly washes, atmospheric ──
function StyleGouache({ w = 300, h = 200 }) {
  return (
    <div style={{ position: 'relative', width: w, height: h, overflow: 'hidden', background: '#EAD9BE' }}>
      <svg width={w} height={h} viewBox="0 0 300 200" preserveAspectRatio="xMidYMid slice">
        <defs>
          <radialGradient id="sun" cx="78%" cy="24%" r="40%"><stop offset="0%" stopColor="#F2C57C"/><stop offset="100%" stopColor="#EAD9BE" stopOpacity="0"/></radialGradient>
          <linearGradient id="sky2" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stopColor="#E9B98C"/><stop offset="100%" stopColor="#EAD9BE"/></linearGradient>
          <filter id="soft"><feGaussianBlur stdDeviation="1.1"/></filter>
        </defs>
        <rect width="300" height="130" fill="url(#sky2)"/>
        <rect width="300" height="200" fill="url(#sun)"/>
        <rect y="128" width="300" height="72" fill="#9FB0A8" opacity="0.7" filter="url(#soft)"/>
        <g filter="url(#soft)" opacity="0.88">
          {SCN.roofs.map((r,i)=><path key={i} d={`M${r[0]} ${r[1]} L${r[2]} ${r[3]} L${r[4]} ${r[5]} Z`} fill={i%2?'#C77A4E':'#A85A38'}/>)}
          <ellipse cx="210" cy="60" rx="22" ry="20" fill="#BE8A55"/>
        </g>
        <circle cx="232" cy="46" r="20" fill="#F4D08A" opacity="0.55" filter="url(#soft)"/>
      </svg>
    </div>
  );
}

const STYLES = [
  { key: 'riso',    name: 'Riso',     Comp: StyleRiso,    tag: 'overprinted spot inks · halftone grain', mood: 'warm, analog, crafted', risk: 'trendy; busy when tiny' },
  { key: 'etch',    name: 'Etching',  Comp: StyleEtch,    tag: 'fine ink hatching · monochrome',          mood: 'field-note, timeless',  risk: 'can read cold/technical' },
  { key: 'lino',    name: 'Linocut',  Comp: StyleLino,    tag: 'carved 2-color · high contrast',          mood: 'bold, scales tiny well', risk: 'folksy if not careful' },
  { key: 'gouache', name: 'Gouache',  Comp: StyleGouache, tag: 'soft painterly washes',                   mood: 'atmospheric, desire',   risk: 'mushy at thumbnail size' },
];

window.StyleRiso = StyleRiso;
window.StyleEtch = StyleEtch;
window.StyleLino = StyleLino;
window.StyleGouache = StyleGouache;
window.STYLES = STYLES;
