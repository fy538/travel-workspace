// ═══════════════════════════════════════════════════════════════
// TRIPS · THE CORE LOOP — interactive, built on the DESIGNED group
// home (GroupHome). No new paradigm: it's the shared-trip home we
// already drew — collaborators row, alive hero, the "DECISIONS ·
// N OPEN" overlay — with the votes made live. Tap a choice and the
// hero + decisions re-read; both decided → settled.
// Reuses Phone, TabBar, TripsTopBar, HeroAliveTrip, Avatars, T/TR.
// ═══════════════════════════════════════════════════════════════
function TripsLoop() {
  const { useState } = React;
  const [votes, setVotes] = useState({ stay: null, day: null });
  const open = (votes.stay ? 0 : 1) + (votes.day ? 0 : 1);
  const D = [
    { k: 'stay', t: 'Where to stay', s: 'Ana proposed Casa do Alecrim · 3 of 4 in', opts: ['Casa do Alecrim', 'A place in Baixa'] },
    { k: 'day', t: 'The day trip', s: 'Sintra vs Cascais · vote closing tonight', opts: ['Sintra', 'Cascais'] },
  ];
  return (
    <Phone bg={T.bg}>
      <TripsTopBar eyebrow="TRIPS · LISBON · 4 GOING"/>
      <div style={{ padding: '18px 22px 0' }}>
        <h1 style={{ fontFamily: T.serif, fontWeight: 500, fontSize: 36, lineHeight: 0.96, letterSpacing: -1, color: T.ink, margin: 0 }}>The Lisbon table.</h1>
        <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginTop: 10 }}>
          <Avatars people={[['Y', TR.ink], ['A', '#A0703A'], ['M', '#7C8F73'], ['J', '#9A6B4F']]}/>
          <span style={{ fontFamily: T.serif, fontSize: 13, color: T.mute, fontStyle: 'italic' }}>you + 3 · planning together</span>
        </div>
      </div>
      <HeroAliveTrip title="Lisbon, in June" days="Sat 6 → Sat 13" nights="7 NIGHTS" countdown="ALIVE · 4 GOING" scene="lisbon" compact next={open ? `${open} group decision${open > 1 ? 's' : ''} waiting on you` : 'all settled — Vesper will lock it in'}/>
      <div style={{ padding: '16px 22px 0' }}>
        <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', marginBottom: 2 }}>
          <span style={{ fontFamily: T.mono, fontSize: 9, color: open ? T.goldDeep : '#3D7050', letterSpacing: 1.6, fontWeight: 700 }}>{open ? `DECISIONS · ${open} OPEN` : 'DECISIONS · ALL IN'}</span>
          <span style={{ fontFamily: T.mono, fontSize: 8.5, color: T.muteSoft, letterSpacing: 1.2, fontWeight: 600 }}>YOUR CALL</span>
        </div>
        {D.map((d) => {
          const chosen = votes[d.k];
          return (
            <div key={d.k} style={{ padding: '12px 0', borderTop: `0.5px solid ${T.hairThin}` }}>
              <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between' }}>
                <span style={{ fontFamily: T.serif, fontSize: 15, color: T.ink, fontWeight: 500, letterSpacing: -0.2 }}>{d.t}</span>
                {chosen && <span style={{ fontFamily: T.mono, fontSize: 8, color: '#3D7050', letterSpacing: 1, fontWeight: 700 }}>VOTED ✓</span>}
              </div>
              <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12.5, color: T.mute, marginTop: 2 }}>{d.s}</div>
              {chosen ? (
                <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginTop: 9 }}>
                  <span style={{ fontFamily: T.serif, fontSize: 14.5, color: T.ink }}>Your pick: <b style={{ fontWeight: 600 }}>{chosen}</b></span>
                  <span onClick={() => setVotes((v) => ({ ...v, [d.k]: null }))} style={{ cursor: 'pointer', fontFamily: T.mono, fontSize: 8, color: T.mute, letterSpacing: 1, fontWeight: 700 }}>CHANGE</span>
                </div>
              ) : (
                <div style={{ display: 'flex', gap: 8, marginTop: 10 }}>
                  {d.opts.map((o) => (
                    <div key={o} onClick={() => setVotes((v) => ({ ...v, [d.k]: o }))} style={{ cursor: 'pointer', flex: 1, textAlign: 'center', padding: '10px 8px', borderRadius: 12, background: T.cardWarm, border: `0.5px solid ${T.hairline}`, fontFamily: T.serif, fontSize: 13.5, color: T.ink, fontWeight: 500, lineHeight: 1.15 }}>{o}</div>
                  ))}
                </div>
              )}
            </div>
          );
        })}
        {open === 0 && (
          <div style={{ marginTop: 14, padding: '12px 14px', background: 'rgba(61,112,80,0.08)', borderRadius: 13, border: `0.5px solid rgba(61,112,80,0.3)` }}>
            <div style={{ fontFamily: T.serif, fontSize: 14.5, color: '#2F5740', fontWeight: 500 }}>Settled — the group can see it.</div>
            <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12.5, color: '#3D7050', marginTop: 3 }}>Casa do Alecrim · {votes.day}. Vesper will lock it in.</div>
          </div>
        )}
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

Object.assign(window, { TripsLoop });
