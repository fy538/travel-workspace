// Shared helpers for the 03 · Artifact-first flow:
//   - ScreenHeader: a back-able screen header with eyebrow + title
//   - YearRibbonH: a compact horizontal year strip (the Almanac, distilled)
//   - YearRibbonV: a slim vertical year strip for use as a sidebar
//   - Postcard:   the keepsake postcard primitive, sized + posable
//   - Chip, Hairline, Eyebrow: tiny atoms

function ScreenHeader({ eyebrow, title, meta, onBack = true, right }) {
  return (
    <div style={{ padding: '14px 22px 0' }}>
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
        {onBack ? (
          <div style={{ display: 'flex', alignItems: 'center', gap: 6, color: T.inkSoft }}>
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke={T.inkSoft} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round">
              <path d="M14 6l-6 6 6 6"/>
            </svg>
            <span style={{ fontSize: 13, fontWeight: 500, color: T.inkSoft }}>Atlas</span>
          </div>
        ) : <div/>}
        <div style={{ display: 'flex', alignItems: 'center', gap: 14 }}>
          {right || <Marks.Search s={18} c={T.inkSoft}/>}
        </div>
      </div>
      <div style={{ marginTop: 18 }}>
        {eyebrow && (
          <div style={{ fontSize: 10.5, color: T.gold, letterSpacing: 2, fontWeight: 600, marginBottom: 8 }}>
            {eyebrow}
          </div>
        )}
        <h1 style={{
          fontFamily: T.serif, fontWeight: 500, fontSize: 36, lineHeight: 0.96,
          letterSpacing: -1, color: T.ink, margin: 0,
        }}>
          {title}
        </h1>
        {meta && (
          <div style={{ fontSize: 11.5, color: T.mute, marginTop: 8, fontFamily: T.serif }}>
            {meta}
          </div>
        )}
      </div>
    </div>
  );
}

function Eyebrow({ children, color = T.mute }) {
  return <div style={{ fontSize: 10.5, color, letterSpacing: 2, fontWeight: 600 }}>{children}</div>;
}

function Hairline({ m = '14px 0' }) {
  return <div style={{ margin: m, height: 0.5, background: T.hairline }}/>;
}

function Chip({ children, active, mono }) {
  return (
    <span style={{
      padding: '4px 9px', borderRadius: 999, fontSize: 10.5, fontWeight: 600,
      letterSpacing: mono ? 1.4 : 0.5, fontFamily: mono ? T.mono : T.sans,
      color: active ? T.ink : T.mute,
      background: active ? T.cardWarm : 'transparent',
      border: `0.6px solid ${active ? T.hairline : 'transparent'}`,
      textTransform: mono ? 'none' : 'none',
    }}>{children}</span>
  );
}

// ─── Horizontal year ribbon ─────────────────────────────────────
// `dots` is 12 items: 'now' | 'past' | 'planned' | null
function YearRibbonH({ dots, now = 2, year = '’26', leftLabel = 'THIS YEAR', rightLabel }) {
  const months = ['J','F','M','A','M','J','J','A','S','O','N','D'];
  return (
    <div style={{ padding: '0 22px' }}>
      <div style={{
        display: 'flex', alignItems: 'baseline', justifyContent: 'space-between',
        marginBottom: 8,
      }}>
        <div style={{ display: 'flex', alignItems: 'baseline', gap: 8 }}>
          <Eyebrow>{leftLabel}</Eyebrow>
          <span style={{ fontFamily: T.serif, fontSize: 13, color: T.mute }}>{year}</span>
        </div>
        {rightLabel && (
          <span style={{ fontSize: 9.5, color: T.muteSoft, letterSpacing: 1.5, fontWeight: 600 }}>
            {rightLabel}
          </span>
        )}
      </div>
      <div style={{ position: 'relative' }}>
        {/* node zone — fixed height so every marker centers on one line */}
        <div style={{ position: 'relative', height: 14 }}>
          {/* the line, split at now — traveled (solid) vs ahead (dashed) — meeting exactly */}
          <div style={{ position: 'absolute', left: 2, top: '50%', height: 1.5, borderRadius: 2, background: T.inkSoft, opacity: 0.45, width: `calc(${((now + 0.5) / 12) * 100}% - 2px)`, transform: 'translateY(-50%)' }}/>
          <div style={{ position: 'absolute', left: `${((now + 0.5) / 12) * 100}%`, right: 2, top: '50%', borderTop: `1px dashed ${T.faint}`, transform: 'translateY(-50%)' }}/>
          <div style={{ position: 'absolute', inset: 0, display: 'grid', gridTemplateColumns: 'repeat(12, 1fr)' }}>
            {months.map((m, i) => {
              const d = dots[i];
              const cap = `0 0 0 3px ${T.bg}`;
              return (
                <div key={i} style={{ display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                  {d === 'now' && <div style={{ width: 9, height: 9, borderRadius: 999, background: T.gold, boxShadow: `${cap}, 0 0 0 6px rgba(176,133,58,0.16)` }}/>}
                  {d === 'past' && <div style={{ width: 6.5, height: 6.5, borderRadius: 999, background: T.inkSoft, boxShadow: cap }}/>}
                  {d === 'planned' && <div style={{ width: 8, height: 8, borderRadius: 999, border: `1.4px solid ${T.gold}`, background: T.bg, boxShadow: cap }}/>}
                  {!d && <div style={{ width: 2.5, height: 2.5, borderRadius: 999, background: T.faint, boxShadow: cap }}/>}
                </div>
              );
            })}
          </div>
        </div>
        {/* month initials — their own row, always aligned */}
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(12, 1fr)', marginTop: 7 }}>
          {months.map((m, i) => (
            <div key={i} style={{ textAlign: 'center', fontFamily: T.mono, fontSize: 8, color: dots[i] ? (dots[i] === 'now' ? T.ink : T.soft) : T.faint, fontWeight: 600, letterSpacing: 0.6 }}>{m}</div>
          ))}
        </div>
      </div>
    </div>
  );
}

// ─── Vertical year ribbon (for sidebars in detail screens) ──────
function YearRibbonV({ items, height = 360 }) {
  // items: [{ m: 'JAN', dot, label }]
  return (
    <div style={{
      position: 'relative', width: 110, height,
      display: 'flex', flexDirection: 'column', justifyContent: 'space-between',
    }}>
      <div style={{
        position: 'absolute', left: 32, top: 6, bottom: 6, width: 1,
        background: T.hairline,
      }}/>
      {items.map((it, i) => (
        <div key={it.m} style={{
          display: 'grid', gridTemplateColumns: '24px 14px 1fr',
          alignItems: 'center', gap: 4, position: 'relative',
        }}>
          <div style={{
            fontSize: 8.5, color: it.dot === 'now' ? T.ink : T.muteSoft,
            letterSpacing: 1.4, fontWeight: 600, textAlign: 'right',
          }}>{it.m}</div>
          <div style={{ display: 'flex', justifyContent: 'center', position: 'relative', zIndex: 1 }}>
            {it.dot === 'now' && (
              <div style={{
                width: 9, height: 9, borderRadius: 999, background: T.gold,
                boxShadow: `0 0 0 4px rgba(176,133,58,0.18)`,
              }}/>
            )}
            {it.dot === 'past' && (
              <div style={{ width: 6, height: 6, borderRadius: 999, background: T.inkSoft }}/>
            )}
            {it.dot === 'planned' && (
              <div style={{ width: 7, height: 7, borderRadius: 999, border: `1px solid ${T.gold}`, background: T.bg }}/>
            )}
            {!it.dot && <div style={{ width: 3, height: 3, borderRadius: 999, background: T.muteSoft, opacity: 0.55 }}/>}
          </div>
          <div style={{
            fontFamily: T.serif, fontStyle: it.dot === 'planned' ? 'italic' : 'normal',
            fontSize: 11, color: it.dot === 'now' ? T.ink : T.inkSoft,
            letterSpacing: -0.1, lineHeight: 1.1,
          }}>{it.label || ''}</div>
        </div>
      ))}
    </div>
  );
}

// ─── A stylized postcard primitive (the keepsake object) ────────
function Postcard({
  scene = 'lisbon', title, sub, date, rotate = 0,
  width = '100%', height = 200, stamp = true, blank = false,
}) {
  return (
    <div style={{
      width, height, background: T.cardWarm, borderRadius: 6,
      transform: `rotate(${rotate}deg)`, padding: 10,
      boxShadow: '0 16px 30px -14px rgba(0,0,0,0.22), 0 0 0 0.5px rgba(27,23,20,0.06)',
      display: 'flex', flexDirection: 'column', position: 'relative',
    }}>
      {/* scene */}
      <div style={{
        flex: 1, background: T.card, borderRadius: 3, position: 'relative',
        overflow: 'hidden', border: `0.5px solid ${T.hairThin}`,
      }}>
        {!blank && <PostcardScene scene={scene}/>}
        {blank && (
          <div style={{
            position: 'absolute', inset: 0, display: 'flex',
            alignItems: 'center', justifyContent: 'center',
            color: T.muteSoft, fontSize: 11, fontFamily: T.serif, fontStyle: 'italic',
            letterSpacing: 0.2, textAlign: 'center', padding: 10,
          }}>
            a place will land here
          </div>
        )}
        {stamp && (
          <div style={{
            position: 'absolute', top: 7, right: 7, width: 22, height: 28,
            background: T.cardWarm, border: `0.6px solid ${T.gold}`, borderRadius: 1,
            display: 'flex', alignItems: 'center', justifyContent: 'center',
          }}>
            <div style={{ width: 14, height: 14, borderRadius: 999, background: T.gold, opacity: 0.85 }}/>
          </div>
        )}
      </div>
      {(title || sub || date) && (
        <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', marginTop: 8 }}>
          <div>
            {title && (
              <div style={{ fontFamily: T.serif, fontSize: 16, color: T.ink, fontWeight: 500, letterSpacing: -0.2, lineHeight: 1 }}>
                {title}
              </div>
            )}
            {sub && (
              <div style={{ fontSize: 10.5, color: T.mute, marginTop: 3, fontFamily: T.serif }}>
                {sub}
              </div>
            )}
          </div>
          {date && (
            <div style={{ fontFamily: T.mono, fontSize: 9, color: T.muteSoft, letterSpacing: 1.1 }}>
              {date}
            </div>
          )}
        </div>
      )}
    </div>
  );
}

function PostcardScene({ scene }) {
  if (scene === 'lisbon') {
    return (
      <svg width="100%" height="100%" viewBox="0 0 300 160" preserveAspectRatio="xMidYMid slice">
        <rect width="300" height="160" fill={T.cardWarm}/>
        <rect y="80" width="300" height="80" fill={T.card}/>
        <circle cx="220" cy="60" r="18" fill={T.goldSoft} opacity="0.55"/>
        <path d="M0 110 L30 90 L40 95 L55 75 L80 95 L100 88 L120 102 L150 80 L170 92 L195 70 L215 88 L240 78 L260 95 L290 86 L300 92 L300 160 L0 160 Z" fill={T.inkSoft} opacity="0.85"/>
        <path d="M0 130 L40 122 L80 128 L130 118 L180 126 L230 116 L300 124 L300 160 L0 160 Z" fill={T.ink}/>
      </svg>
    );
  }
  if (scene === 'porto') {
    return (
      <svg width="100%" height="100%" viewBox="0 0 300 160" preserveAspectRatio="xMidYMid slice">
        <rect width="300" height="160" fill={T.cardSoft}/>
        <rect y="100" width="300" height="60" fill="#9CA89C" opacity="0.35"/>
        {/* bridge */}
        <path d="M30 100 Q150 60 270 100" stroke={T.ink} strokeWidth="1.2" fill="none"/>
        <path d="M30 105 L30 130 M270 105 L270 130" stroke={T.ink} strokeWidth="1.2"/>
        <path d="M30 130 L270 130" stroke={T.ink} strokeWidth="1"/>
        {/* houses */}
        <path d="M0 130 L20 120 L40 130 L60 118 L80 130 L100 122 L120 132 L0 132 Z" fill={T.ink} opacity="0.75"/>
      </svg>
    );
  }
  if (scene === 'tokyo') {
    return (
      <svg width="100%" height="100%" viewBox="0 0 300 160" preserveAspectRatio="xMidYMid slice">
        <rect width="300" height="160" fill={T.cardWarm}/>
        {/* moon */}
        <circle cx="240" cy="55" r="22" fill={T.cardSoft}/>
        <circle cx="234" cy="50" r="20" fill={T.cardWarm}/>
        {/* skyline */}
        <path d="M0 120 L20 90 L30 110 L50 80 L60 105 L80 95 L100 115 L120 90 L140 105 L160 100 L180 115 L210 95 L240 105 L260 100 L290 110 L300 105 L300 160 L0 160 Z" fill={T.ink} opacity="0.92"/>
        <path d="M70 95 L70 80 M170 100 L170 78" stroke={T.gold} strokeWidth="1"/>
      </svg>
    );
  }
  return null;
}

Object.assign(window, { ScreenHeader, Eyebrow, Hairline, Chip, YearRibbonH, YearRibbonV, Postcard, PostcardScene });
