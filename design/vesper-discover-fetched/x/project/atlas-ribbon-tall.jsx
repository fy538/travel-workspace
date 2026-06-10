// ═══════════════════════════════════════════════════════════════
// ATLAS · YEAR RIBBON — taller, named. Brainstorm: relax the height
// so trips carry names (alternating above/below the line) and a
// Vesper "now-read" can sit beneath. Two heights to compare.
// Standalone module (not the shared thin YearRibbonH). Uses T.
// ═══════════════════════════════════════════════════════════════

function YearRibbonBig({ items, now = 4, height = 84, nowRead, leftLabel = 'YOUR YEAR', year = '’26', rightLabel, alt = true }) {
  const months = ['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D'];
  const cap = `0 0 0 3px ${T.bg}`;
  let markN = -1;
  return (
    <div style={{ padding: '0 22px' }}>
      <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', marginBottom: 10 }}>
        <div style={{ display: 'flex', alignItems: 'baseline', gap: 8 }}>
          <span style={{ fontSize: 10.5, color: T.mute, letterSpacing: 2, fontWeight: 600 }}>{leftLabel}</span>
          <span style={{ fontFamily: T.serif, fontSize: 13, fontStyle: 'italic', color: T.mute }}>{year}</span>
        </div>
        {rightLabel && <span style={{ fontFamily: T.mono, fontSize: 9, color: T.muteSoft, letterSpacing: 1.5, fontWeight: 600 }}>{rightLabel}</span>}
      </div>

      {/* node zone — taller, labels sit off the line */}
      <div style={{ position: 'relative', height }}>
        <div style={{ position: 'absolute', left: 2, top: '50%', height: 1.5, borderRadius: 2, background: T.inkSoft, opacity: 0.45, width: `calc(${((now + 0.5) / 12) * 100}% - 2px)`, transform: 'translateY(-50%)' }}/>
        <div style={{ position: 'absolute', left: `${((now + 0.5) / 12) * 100}%`, right: 2, top: '50%', borderTop: `1px dashed ${T.faint}`, transform: 'translateY(-50%)' }}/>
        <div style={{ position: 'absolute', inset: 0, display: 'grid', gridTemplateColumns: 'repeat(12, 1fr)' }}>
          {months.map((m, i) => {
            const it = items[i] || {};
            const d = it.dot;
            if (it.label) markN += 1;
            const above = alt ? markN % 2 === 0 : false;
            return (
              <div key={i} style={{ position: 'relative', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                {d === 'now' && <div style={{ width: 9, height: 9, borderRadius: 999, background: T.gold, boxShadow: `${cap}, 0 0 0 6px rgba(176,133,58,0.16)` }}/>}
                {d === 'past' && <div style={{ width: 6.5, height: 6.5, borderRadius: 999, background: T.inkSoft, boxShadow: cap }}/>}
                {d === 'planned' && <div style={{ width: 8, height: 8, borderRadius: 999, border: `1.4px solid ${T.gold}`, background: T.bg, boxShadow: cap }}/>}
                {!d && <div style={{ width: 2.5, height: 2.5, borderRadius: 999, background: T.faint, boxShadow: cap }}/>}
                {it.label && (
                  <div style={{ position: 'absolute', left: '50%', transform: 'translateX(-50%)', [above ? 'bottom' : 'top']: 'calc(50% + 11px)', textAlign: 'center', whiteSpace: 'nowrap' }}>
                    <div style={{ fontFamily: T.serif, fontSize: 13.5, fontWeight: 500, fontStyle: d === 'planned' ? 'italic' : 'normal', color: d === 'now' ? T.ink : T.inkSoft, letterSpacing: -0.2, lineHeight: 1 }}>{it.label}</div>
                    {it.sub && <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 10.5, color: T.muteSoft, marginTop: 2 }}>{it.sub}</div>}
                  </div>
                )}
              </div>
            );
          })}
        </div>
      </div>

      {/* month initials */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(12, 1fr)', marginTop: 7 }}>
        {months.map((m, i) => (
          <div key={i} style={{ textAlign: 'center', fontFamily: T.mono, fontSize: 8, color: items[i] && items[i].dot ? (items[i].dot === 'now' ? T.ink : T.soft) : T.faint, fontWeight: 600, letterSpacing: 0.6 }}>{m}</div>
        ))}
      </div>

      {/* the now-read — Vesper's one line tying the year together */}
      {nowRead && (
        <div style={{ marginTop: 14, paddingTop: 12, borderTop: `0.5px solid ${T.hairline}` }}>
          <span style={{ fontFamily: T.mono, fontSize: 8.5, color: T.goldDeep, letterSpacing: 1.4, fontWeight: 700 }}>{nowRead.tag}</span>
          <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 15, color: T.inkSoft, marginTop: 4, lineHeight: 1.35 }}>{nowRead.line}</div>
        </div>
      )}
    </div>
  );
}

const RB_ITEMS = [
  {}, { dot: 'past', label: 'Porto' }, {}, { dot: 'past', label: 'Lisbon' },
  { dot: 'now' }, {}, {}, {}, { dot: 'planned', label: 'Tokyo' }, {}, {}, {},
];

// a paper panel so the module is easy to read on the canvas
function RibbonPanel({ children, w = 393 }) {
  return <div style={{ width: w, background: T.bg, borderRadius: 22, padding: '30px 0', boxShadow: '0 1px 0 rgba(255,255,255,0.6) inset, 0 14px 34px -18px rgba(0,0,0,0.2)' }}>{children}</div>;
}

function RibbonNamed() {
  return <RibbonPanel><YearRibbonBig items={RB_ITEMS} now={4} height={62} alt={false} leftLabel="YOUR YEAR" rightLabel="2 KEPT"/></RibbonPanel>;
}
function RibbonFull() {
  return <RibbonPanel><YearRibbonBig items={RB_ITEMS} now={4} height={84} alt leftLabel="YOUR YEAR" rightLabel="2 KEPT" nowRead={{ tag: 'MAY · WHERE YOU ARE', line: 'Lisbon and Porto behind you — Tokyo waiting in the autumn.' }}/></RibbonPanel>;
}

Object.assign(window, { YearRibbonBig, RibbonNamed, RibbonFull });
