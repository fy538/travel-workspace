// Shared atoms for the Trips redesign.
// Trips inherits Atlas's palette but adds an ink-blue accent for *planning*
// affordances (dates, active state, decisions) — so ochre stays as Vesper's
// signature voice and ink-blue becomes the "this is moving" voice.

const TR = {
  // ink-blue planning accent
  ink:       '#3D5066',
  inkDeep:   '#2A384B',
  inkSoft:   '#5C6E84',
  inkSurface:'#E4E0D4',  // a slightly cooler paper for trip surfaces

  // tag colors (used very sparingly)
  alive:     '#3D5066',
  dreaming:  '#7C8F73', // sage, for ideas
  needsYou:  '#B0853A',
};

// ─── Bell + ellipsis icons ──────────────────────────────────────
const TripIcons = {
  Bell: ({ s = 18, c = T.inkSoft }) => (
    <svg width={s} height={s} viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round">
      <path d="M6 9a6 6 0 0 1 12 0v4l1.5 3h-15L6 13V9Z"/>
      <path d="M10 19a2 2 0 0 0 4 0"/>
    </svg>
  ),
  Dots: ({ s = 18, c = T.inkSoft }) => (
    <svg width={s} height={s} viewBox="0 0 24 24" fill={c}>
      <circle cx="5" cy="12" r="1.5"/><circle cx="12" cy="12" r="1.5"/><circle cx="19" cy="12" r="1.5"/>
    </svg>
  ),
  Users: ({ s = 16, c = T.ink, n = 3, accent = TR.ink }) => (
    <svg width={s * 1.6} height={s} viewBox="0 0 32 20" fill="none">
      {Array.from({ length: Math.min(n, 3) }).map((_, i) => (
        <circle key={i} cx={6 + i * 8} cy="10" r="6" fill={i === 0 ? accent : T.cardWarm}
                stroke={i === 0 ? 'none' : c} strokeWidth="1"/>
      ))}
      {n > 3 && <text x="28" y="13" fontSize="6" fill={c} fontFamily="DM Sans">+{n - 3}</text>}
    </svg>
  ),
  Pin: ({ s = 14, c = T.ink }) => (
    <svg width={s} height={s} viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round">
      <path d="M12 3c-4 0-7 3-7 7 0 5 7 11 7 11s7-6 7-11c0-4-3-7-7-7Z"/>
      <circle cx="12" cy="10" r="2.5"/>
    </svg>
  ),
  Sparkle: ({ s = 14, c = T.gold }) => (
    <svg width={s} height={s} viewBox="0 0 24 24" fill={c}>
      <path d="M12 3l1.6 5L18 9.5l-4.4 1.5L12 16l-1.6-5L6 9.5l4.4-1.5L12 3Z"/>
    </svg>
  ),
  Calendar: ({ s = 14, c = T.ink }) => (
    <svg width={s} height={s} viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.5" strokeLinecap="round">
      <rect x="3.5" y="5" width="17" height="15" rx="2"/>
      <path d="M3.5 10h17M8 3v4M16 3v4"/>
    </svg>
  ),
  Decision: ({ s = 14, c = TR.needsYou }) => (
    <svg width={s} height={s} viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.6" strokeLinecap="round">
      <circle cx="12" cy="12" r="9"/>
      <path d="M9 9c0-2 1.5-3 3-3s3 1 3 3-3 2-3 4M12 17.5v.5"/>
    </svg>
  ),
};

// ─── Top bar used by all three Trips variants ───────────────────
function TripsTopBar({ eyebrow, mute }) {
  return (
    <div style={{
      display: 'flex', alignItems: 'center', justifyContent: 'space-between',
      padding: '14px 22px 0',
    }}>
      <div style={{ fontSize: 10.5, color: mute || T.mute, letterSpacing: 2, fontWeight: 600 }}>
        {eyebrow}
      </div>
      <div style={{ display: 'flex', alignItems: 'center', gap: 15 }}>
        <span style={{ fontFamily: T.mono, fontSize: 8.5, letterSpacing: 1.2, color: T.goldDeep, fontWeight: 600 }}>ALL TRIPS ›</span>
        <Marks.Plus s={19} c={T.inkSoft}/>
        <div style={{ position: 'relative', display: 'flex' }}>
          <TripIcons.Bell s={19} c={T.inkSoft}/>
          <span style={{
            position: 'absolute', top: -1, right: -1, width: 6, height: 6, borderRadius: 6,
            background: TR.needsYou, border: `1.5px solid ${T.bg}`, boxSizing: 'content-box',
          }}/>
        </div>
      </div>
    </div>
  );
}

// ─── A status pill (alive, dreaming, needs-you, ready) ──────────
// shared seed/shape card — the rich dream-seed card (Cold start + Create)
function SeedCard({ title, sub, line, meta, w = 150 }) {
  return (
    <div style={{ width: w, flexShrink: 0, padding: '12px 13px', background: T.cardWarm, borderRadius: 12, border: `0.5px solid ${T.hairline}` }}>
      <div style={{ fontFamily: T.serif, fontSize: 16, fontWeight: 500, color: T.ink, letterSpacing: -0.2 }}>{title}</div>
      <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 11.5, color: T.goldDeep, marginTop: 1 }}>{sub}</div>
      <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 11.5, color: T.mute, lineHeight: 1.35, margin: '7px 0 0' }}>{line}</p>
      <div style={{ fontFamily: T.mono, fontSize: 7.5, letterSpacing: 0.8, color: T.muteSoft, fontWeight: 600, marginTop: 8 }}>{meta}</div>
    </div>
  );
}

function TripPill({ kind = 'alive', children }) {
  const colors = {
    alive:    { bg: 'rgba(61,80,102,0.10)', fg: TR.inkDeep, dot: TR.ink },
    dreaming: { bg: 'rgba(124,143,115,0.16)', fg: '#4D5E45', dot: TR.dreaming },
    needs:    { bg: 'rgba(176,133,58,0.16)', fg: T.goldDeep, dot: T.gold },
    ready:    { bg: 'rgba(27,23,20,0.06)',  fg: T.ink, dot: T.ink },
  };
  const c = colors[kind] || colors.alive;
  return (
    <span style={{
      display: 'inline-flex', alignItems: 'center', gap: 5,
      padding: '3px 8px', borderRadius: 999,
      fontSize: 9.5, letterSpacing: 1.4, fontWeight: 700,
      color: c.fg, background: c.bg,
    }}>
      <span style={{ width: 5, height: 5, borderRadius: 5, background: c.dot }}/>
      {children}
    </span>
  );
}

// ─── A "ticket" scene — used as trip thumbnail in some variants ─
function TripScene({ kind = 'tokyo', height = '100%' }) {
  return (
    <div style={{
      width: '100%', height, borderRadius: 4, overflow: 'hidden',
      background: T.cardSoft, position: 'relative',
    }}>
      <PostcardScene scene={kind}/>
    </div>
  );
}

// ─── A small "starter" card (city break, beach, etc.) ───────────
function StarterChip({ name, sub, glyph, accent }) {
  return (
    <div style={{
      flex: '0 0 auto', width: 124,
      padding: '14px 12px 12px', background: T.cardWarm, borderRadius: 14,
      border: accent ? `0.8px solid ${TR.ink}` : `0.5px solid ${T.hairline}`,
      boxShadow: '0 1px 0 rgba(255,255,255,0.6) inset',
    }}>
      <div style={{
        width: 30, height: 30, borderRadius: 8,
        background: accent ? 'rgba(61,80,102,0.10)' : T.cardSoft,
        display: 'flex', alignItems: 'center', justifyContent: 'center',
        marginBottom: 10,
      }}>{glyph}</div>
      <div style={{
        fontFamily: T.serif, fontSize: 15, fontWeight: 500, color: T.ink,
        letterSpacing: -0.2, lineHeight: 1,
      }}>{name}</div>
      <div style={{
        fontFamily: T.serif, fontSize: 11, color: T.mute,
        lineHeight: 1.3, marginTop: 4,
      }}>{sub}</div>
    </div>
  );
}

const StarterGlyphs = {
  City: ({ c = TR.ink }) => (
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.4" strokeLinecap="round">
      <rect x="4" y="9" width="6" height="11" rx="0.5"/>
      <rect x="14" y="5" width="6" height="15" rx="0.5"/>
      <path d="M6 12h2M6 15h2M6 18h2M16 8h2M16 11h2M16 14h2M16 17h2"/>
    </svg>
  ),
  Beach: ({ c = TR.ink }) => (
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.4" strokeLinecap="round">
      <circle cx="17" cy="7" r="2.5"/>
      <path d="M3 18q4 -3 8 -3 t8 3M3 21q4 -2 8 -2 t8 2"/>
    </svg>
  ),
  Mountain: ({ c = TR.ink }) => (
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.4" strokeLinecap="round" strokeLinejoin="round">
      <path d="M3 19l6 -9 4 5 3 -4 5 8z"/>
    </svg>
  ),
  Road: ({ c = TR.ink }) => (
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.4" strokeLinecap="round">
      <path d="M9 3l-3 18M15 3l3 18M12 4v2M12 10v2M12 16v2"/>
    </svg>
  ),
  Festival: ({ c = TR.ink }) => (
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.4" strokeLinecap="round">
      <path d="M9 17V8l3 -3l3 3v9"/>
      <path d="M5 17h14M7 17v3M17 17v3M11 17v3M13 17v3"/>
    </svg>
  ),
  Quiet: ({ c = TR.ink }) => (
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.4" strokeLinecap="round" strokeLinejoin="round">
      <path d="M5 18c0 -5 3 -8 7 -8s7 3 7 8"/>
      <path d="M3 18h18"/>
      <path d="M12 10V4"/>
    </svg>
  ),
};

Object.assign(window, { TR, TripIcons, TripsTopBar, TripPill, TripScene, StarterChip, StarterGlyphs });
