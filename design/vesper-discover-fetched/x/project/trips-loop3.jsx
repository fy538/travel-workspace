// ═══════════════════════════════════════════════════════════════
// TRIPS · INTERACTIVE PATTERNS (live) — three more, on designed
// screens: dream-seed → draft (cold), urgent → resolve, notifs →
// clear. Same vote-in-place philosophy: state re-reads in place.
// ═══════════════════════════════════════════════════════════════
const OX3 = '#A04030';

// ── 1 · DREAM-SEED → DRAFT (cold start, live) ───────────────────
function DreamLoop() {
  const { useState } = React;
  const [added, setAdded] = useState([]);
  const seeds = [['Lisbon', 'in spring'], ['Tokyo', 'when the leaves turn']];
  return (
    <Phone bg={T.bg}>
      <TripsTopBar eyebrow="TRIPS · DREAMING"/>
      <div style={{ padding: '18px 22px 0' }}>
        <h1 style={{ fontFamily: T.serif, fontWeight: 500, fontSize: 34, lineHeight: 0.96, letterSpacing: -1.1, color: T.ink, margin: 0 }}>Where <span style={{ fontStyle: 'italic' }}>to?</span></h1>
      </div>
      <div style={{ padding: '20px 22px 0' }}>
        <div style={{ fontFamily: T.mono, fontSize: 8.5, letterSpacing: 1.6, color: T.muteSoft, fontWeight: 600 }}>OR, SOMEWHERE FOR YOUR TASTE</div>
        <div style={{ display: 'flex', gap: 8, marginTop: 10 }}>
          {seeds.map(([n, s]) => {
            const on = added.includes(n);
            return (
              <div key={n} onClick={() => setAdded((a) => on ? a.filter((x) => x !== n) : [...a, n])} style={{ cursor: 'pointer', flex: 1, padding: '12px 13px', background: T.cardWarm, borderRadius: 12, border: `0.5px solid ${on ? T.gold : T.hairline}` }}>
                <div style={{ fontFamily: T.serif, fontSize: 16, fontWeight: 500, color: T.ink, letterSpacing: -0.2 }}>{n}</div>
                <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 11.5, color: T.goldDeep, marginTop: 1 }}>{s}</div>
                <div style={{ fontFamily: T.mono, fontSize: 7.5, letterSpacing: 0.8, color: on ? '#3D7050' : T.muteSoft, fontWeight: 700, marginTop: 9 }}>{on ? 'ON THE TABLE ✓' : 'TAP TO KEEP'}</div>
              </div>
            );
          })}
        </div>
      </div>
      <div style={{ padding: '20px 22px 0' }}>
        <div style={{ fontFamily: T.mono, fontSize: 10, letterSpacing: 2, color: T.mute, fontWeight: 600 }}>ON THE TABLE · {added.length}</div>
        {added.length === 0
          ? <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13.5, color: T.muteSoft, margin: '10px 0 0' }}>nothing kept yet — tap a dream above to start one.</p>
          : <div style={{ marginTop: 10, display: 'flex', flexDirection: 'column', gap: 8 }}>
              {added.map((n) => (
                <div key={n} style={{ padding: '11px 13px', background: T.cardWarm, borderRadius: 12, border: `0.5px solid ${T.hairline}`, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
                  <div><TripPill kind="dreaming">DREAMING</TripPill><div style={{ fontFamily: T.serif, fontSize: 15, color: T.ink, fontWeight: 500, marginTop: 7 }}>{n}</div></div>
                  <Marks.ArrowR s={14} c={T.goldDeep}/>
                </div>
              ))}
            </div>}
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

// ── 2 · URGENT → RESOLVE (the alert calms the home, live) ───────
function UrgentLoop() {
  const { useState } = React;
  const [st, setSt] = useState('alert');
  return (
    <Phone bg={T.bg}>
      <TripsTopBar eyebrow={st === 'done' ? 'TRIPS · TOKYO IN 58 DAYS' : 'TRIPS · NEEDS YOU'} mute={st === 'done' ? T.mute : OX3}/>
      <div style={{ padding: '18px 22px 0' }}>
        <h1 style={{ fontFamily: T.serif, fontWeight: 500, fontSize: 33, lineHeight: 0.98, letterSpacing: -0.9, color: T.ink, margin: 0 }}>{st === 'done' ? 'Back to calm.' : 'One thing can’t wait.'}</h1>
      </div>
      {st === 'done' ? (
        <div style={{ margin: '16px 16px 0', padding: '16px 17px', background: 'rgba(61,112,80,0.08)', borderRadius: 16, border: `0.5px solid rgba(61,112,80,0.3)` }}>
          <div style={{ fontFamily: T.mono, fontSize: 9, color: '#3D7050', letterSpacing: 1.6, fontWeight: 700 }}>SORTED ✓</div>
          <div style={{ fontFamily: T.serif, fontSize: 20, fontWeight: 500, color: T.ink, letterSpacing: -0.4, marginTop: 8 }}>Vesper booked the 5:10 transfer.</div>
          <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13, color: '#3D7050', marginTop: 5 }}>You’ll make the connection with room to spare.</div>
        </div>
      ) : (
        <div style={{ margin: '16px 16px 0', padding: '16px 17px', background: T.cardWarm, borderRadius: 16, border: `0.5px solid ${T.hairline}`, boxShadow: '0 16px 34px -22px rgba(0,0,0,0.22)' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 7 }}>
            <span style={{ width: 7, height: 7, borderRadius: 7, background: OX3, boxShadow: `0 0 0 3px rgba(160,64,48,0.18)` }}/>
            <span style={{ fontFamily: T.mono, fontSize: 9, color: OX3, letterSpacing: 1.6, fontWeight: 700 }}>LISBON · FLIGHT MOVED</span>
          </div>
          <div style={{ fontFamily: T.serif, fontSize: 22, fontWeight: 500, color: T.ink, letterSpacing: -0.4, lineHeight: 1.1, marginTop: 9 }}>Your outbound shifted to 6:10am.</div>
          {st === 'alert' ? (
            <>
              <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13.5, color: T.soft, lineHeight: 1.4, marginTop: 6 }}>The transfer no longer makes it. Vesper found two ways to still arrive in time.</div>
              <div style={{ display: 'flex', gap: 8, marginTop: 14 }}>
                <div onClick={() => setSt('options')} style={{ cursor: 'pointer', flex: 1, textAlign: 'center', padding: '11px 0', borderRadius: 999, background: OX3, color: '#fff', fontFamily: T.sans, fontSize: 13.5, fontWeight: 600 }}>See the two</div>
                <div onClick={() => setSt('done')} style={{ cursor: 'pointer', flex: 1, textAlign: 'center', padding: '11px 0', borderRadius: 999, border: `0.5px solid ${T.hairline}`, color: T.inkSoft, fontFamily: T.sans, fontSize: 13.5, fontWeight: 500 }}>Not now</div>
              </div>
            </>
          ) : (
            <div style={{ marginTop: 12 }}>
              {[['Earlier transfer · 5:10am', '+€0 · arrives 5:55'], ['A taxi at 5:30am', '+€38 · arrives 6:05']].map(([t, s]) => (
                <div key={t} onClick={() => setSt('done')} style={{ cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '12px 0', borderTop: `0.5px solid ${T.hairThin}` }}>
                  <div><div style={{ fontFamily: T.serif, fontSize: 15, color: T.ink, fontWeight: 500 }}>{t}</div><div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12, color: T.mute, marginTop: 2 }}>{s}</div></div>
                  <Marks.ArrowR s={13} c={OX3}/>
                </div>
              ))}
            </div>
          )}
        </div>
      )}
      <div style={{ padding: '18px 22px 0', fontFamily: T.serif, fontStyle: 'italic', fontSize: 13.5, color: T.mute }}>{st === 'done' ? 'The rest of the table, as it was.' : '…and 4 other things on the table.'}</div>
      <TabBar active="trips"/>
    </Phone>
  );
}

// ── 3 · NOTIFICATIONS → CLEAR (tap to read / mark all, live) ────
function NotifLoop() {
  const { useState } = React;
  const rows = [
    ['Cherry blossoms peaked overnight', 'Yoyogi is at 90% bloom.', 'VESPER · NOW'],
    ['Ana added a dinner pin', '“Den” — Wed 19:30, two seats.', 'ANA · 2H'],
    ['Vesper drafted three ryokans', 'kept the quiet ones.', 'VESPER · AM'],
    ['Ana said yes to Porto', 'the week of Jun 6–13.', 'ANA · YST'],
  ];
  const [read, setRead] = useState({});
  const allRead = rows.every((_, i) => read[i]);
  return (
    <Phone bg={T.bg}>
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '14px 22px 0' }}>
        <span style={{ fontSize: 10.5, color: T.mute, letterSpacing: 2, fontWeight: 600 }}>UPDATES</span>
        <span onClick={() => setRead(Object.fromEntries(rows.map((_, i) => [i, true])))} style={{ cursor: 'pointer', fontFamily: T.serif, fontStyle: 'italic', fontSize: 12.5, color: allRead ? T.muteSoft : T.goldDeep }}>{allRead ? 'all caught up' : 'Mark all'}</span>
      </div>
      <div style={{ padding: '18px 22px 0' }}>
        <h1 style={{ fontFamily: T.serif, fontWeight: 500, fontSize: 30, lineHeight: 0.98, letterSpacing: -0.8, color: T.ink, margin: 0 }}>What changed, <span style={{ fontStyle: 'italic' }}>since you looked.</span></h1>
      </div>
      <div style={{ padding: '10px 22px 0' }}>
        {rows.map(([t, s, m], i) => {
          const r = read[i];
          return (
            <div key={i} onClick={() => setRead((x) => ({ ...x, [i]: true }))} style={{ cursor: 'pointer', display: 'grid', gridTemplateColumns: '10px 1fr', gap: 11, alignItems: 'start', padding: '13px 0', borderTop: `0.5px solid ${T.hairThin}`, opacity: r ? 0.5 : 1 }}>
              <span style={{ width: 7, height: 7, borderRadius: 7, marginTop: 5, background: r ? 'transparent' : T.gold, border: r ? `1px solid ${T.faint}` : 'none' }}/>
              <div>
                <div style={{ fontFamily: T.serif, fontSize: 15, color: T.ink, fontWeight: 500, letterSpacing: -0.2 }}>{t}</div>
                <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12.5, color: T.mute, marginTop: 2 }}>{s}</div>
                <div style={{ fontFamily: T.mono, fontSize: 8.5, color: T.muteSoft, letterSpacing: 1.2, fontWeight: 600, marginTop: 5 }}>{m}</div>
              </div>
            </div>
          );
        })}
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

// the cold-home dream seeds, made live — tap to keep (faithful enriched cards)
function DreamSeeds() {
  const { useState } = React;
  const [kept, setKept] = useState([]);
  const seeds = [
    ['Lisbon', 'in spring', 'Tile light, long lunches, the year’s first warm evenings out.', '5–6 DAYS · FOOD-LED'],
    ['Tokyo', 'when the leaves turn', 'Crisp mornings, ginkgo gold, the city at its most composed.', 'A WEEK · CITY'],
  ];
  return (
    <div style={{ display: 'flex', gap: 8, marginTop: 9 }}>
      {seeds.map(([p, w, line, meta]) => {
        const on = kept.includes(p);
        return (
          <div key={p} onClick={() => setKept((k) => on ? k.filter((x) => x !== p) : [...k, p])} style={{ cursor: 'pointer', flex: 1, padding: '12px 13px', background: T.cardWarm, borderRadius: 12, border: `0.5px solid ${on ? T.gold : T.hairline}` }}>
            <div style={{ fontFamily: T.serif, fontSize: 16, fontWeight: 500, color: T.ink, letterSpacing: -0.2 }}>{p}</div>
            <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 11.5, color: T.goldDeep, marginTop: 1 }}>{w}</div>
            <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 11.5, color: T.mute, lineHeight: 1.35, margin: '7px 0 0' }}>{line}</p>
            <div style={{ fontFamily: T.mono, fontSize: 7.5, letterSpacing: 0.8, color: on ? '#3D7050' : T.muteSoft, fontWeight: 600, marginTop: 8 }}>{on ? 'KEPT · ON THE TABLE ✓' : meta}</div>
          </div>
        );
      })}
    </div>
  );
}

Object.assign(window, { DreamLoop, UrgentLoop, NotifLoop, DreamSeeds });
