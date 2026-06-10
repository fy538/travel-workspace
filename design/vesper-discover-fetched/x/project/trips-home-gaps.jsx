// ═══════════════════════════════════════════════════════════════
// TRIPS HOME · THE MISSING SURFACES.
// (1) Group/shared-trip overlay · (2) Urgent/needs-you home ·
// (3) Tap-a-trip handoff seam · (4) Loading / error / offline.
// Same card grammar — flat cardWarm, hairline, upright, one hero.
// Reuses Phone, TabBar, TripsTopBar, TripPill, TripIcons, Marks,
// HeroAliveTrip, DraftsScatter, T/TR.
// ═══════════════════════════════════════════════════════════════

const OX = '#A04030'; // oxblood — urgency only

// avatar stack
function Avatars({ people }) {
  return (
    <div style={{ display: 'flex' }}>
      {people.map(([i, c], n) => (
        <div key={n} style={{ width: 24, height: 24, borderRadius: 999, background: c, color: '#fff', display: 'flex', alignItems: 'center', justifyContent: 'center', fontFamily: T.serif, fontSize: 11, fontWeight: 500, marginLeft: n ? -7 : 0, boxShadow: `0 0 0 1.5px ${T.bg}` }}>{i}</div>
      ))}
    </div>
  );
}

// ─── 1 · GROUP / SHARED-TRIP OVERLAY ────────────────────────────
function GroupHome() {
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
      <HeroAliveTrip title="Lisbon, in June" days="Sat 6 → Sat 13" nights="7 NIGHTS" countdown="ALIVE · 4 GOING" scene="lisbon" next="2 group decisions waiting on you"/>
      {/* the overlay: open decisions */}
      <div style={{ padding: '16px 22px 0' }}>
        <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', marginBottom: 4 }}>
          <span style={{ fontFamily: T.mono, fontSize: 9, color: T.goldDeep, letterSpacing: 1.6, fontWeight: 700 }}>DECISIONS · 2 OPEN</span>
          <span style={{ fontFamily: T.mono, fontSize: 8.5, color: T.muteSoft, letterSpacing: 1.2, fontWeight: 600 }}>YOUR CALL</span>
        </div>
        {[['Where to stay', 'Ana proposed Casa do Alecrim', '3 of 4 in'], ['The day trip', 'Sintra vs Cascais — vote closing tonight', '2 votes']].map(([t, s, m], i) => (
          <div key={t} style={{ display: 'grid', gridTemplateColumns: '1fr auto', gap: 10, alignItems: 'center', padding: '12px 0', borderTop: `0.5px solid ${T.hairThin}` }}>
            <div style={{ minWidth: 0 }}>
              <div style={{ fontFamily: T.serif, fontSize: 15, color: T.ink, fontWeight: 500, letterSpacing: -0.2 }}>{t}</div>
              <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12, color: T.mute, marginTop: 2 }}>{s}</div>
            </div>
            <span style={{ fontFamily: T.mono, fontSize: 8, color: T.goldDeep, letterSpacing: 1, fontWeight: 700, border: `0.5px solid ${T.hairline}`, borderRadius: 999, padding: '5px 9px', whiteSpace: 'nowrap' }}>VOTE</span>
          </div>
        ))}
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

// ─── 2 · URGENT / NEEDS-YOU HOME ────────────────────────────────
function UrgentHome() {
  return (
    <Phone bg={T.bg}>
      <TripsTopBar eyebrow="TRIPS · NEEDS YOU" mute={OX}/>
      <div style={{ padding: '18px 22px 0' }}>
        <h1 style={{ fontFamily: T.serif, fontWeight: 500, fontSize: 34, lineHeight: 0.98, letterSpacing: -0.9, color: T.ink, margin: 0 }}>One thing can’t wait.</h1>
      </div>
      {/* the urgent hero — oxblood accent, dot not stripe */}
      <div style={{ margin: '16px 16px 0', padding: '16px 17px', background: T.cardWarm, borderRadius: 16, border: `0.5px solid ${T.hairline}`, boxShadow: '0 16px 34px -22px rgba(0,0,0,0.22)' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 7 }}>
          <span style={{ width: 7, height: 7, borderRadius: 7, background: OX, boxShadow: `0 0 0 3px rgba(160,64,48,0.18)` }}/>
          <span style={{ fontFamily: T.mono, fontSize: 9, color: OX, letterSpacing: 1.6, fontWeight: 700 }}>LISBON · FLIGHT MOVED</span>
        </div>
        <div style={{ fontFamily: T.serif, fontSize: 22, fontWeight: 500, color: T.ink, letterSpacing: -0.4, lineHeight: 1.1, marginTop: 9 }}>Your outbound shifted to 6:10am.</div>
        <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13.5, color: T.soft, lineHeight: 1.4, marginTop: 6 }}>The airport transfer no longer makes it. Vesper found two ways to still arrive in time.</div>
        <div style={{ display: 'flex', gap: 8, marginTop: 14 }}>
          <div style={{ flex: 1, textAlign: 'center', padding: '11px 0', borderRadius: 999, background: OX, color: '#fff', fontFamily: T.sans, fontSize: 13.5, fontWeight: 600 }}>See the two</div>
          <div style={{ flex: 1, textAlign: 'center', padding: '11px 0', borderRadius: 999, border: `0.5px solid ${T.hairline}`, color: T.inkSoft, fontFamily: T.sans, fontSize: 13.5, fontWeight: 500 }}>Not now</div>
        </div>
      </div>
      {/* everything else demoted */}
      <div style={{ padding: '18px 22px 0' }}>
        <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13.5, color: T.mute }}>…and 4 other things on the table — <span style={{ color: T.goldDeep }}>show the rest →</span></div>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

// ─── 3 · TAP-A-TRIP HANDOFF SEAM ────────────────────────────────
function TapHandoff() {
  return (
    <Phone bg={T.bg}>
      <TripsTopBar eyebrow="TRIPS · 3 · MARCH ’26"/>
      <div style={{ padding: '18px 22px 0' }}>
        <h1 style={{ fontFamily: T.serif, fontWeight: 500, fontSize: 36, lineHeight: 0.96, letterSpacing: -1, color: T.ink, margin: 0 }}>Your planning table.</h1>
      </div>
      {/* the hero, pressed — mid-tap */}
      <div style={{ position: 'relative', transform: 'scale(0.975)', transition: 'transform .2s' }}>
        <HeroAliveTrip title="Tokyo, in May" days="Sat 14 → Fri 22" nights="8 NIGHTS" countdown="ALIVE · 58 DAYS OUT" scene="tokyo" next="Pick a ryokan for nights 5–7"/>
        <div style={{ position: 'absolute', inset: '0 16px', borderRadius: 18, background: 'rgba(27,23,20,0.04)', pointerEvents: 'none' }}/>
      </div>
      <div style={{ padding: '14px 22px 0', textAlign: 'center' }}>
        <div style={{ fontFamily: T.mono, fontSize: 8, color: T.muteSoft, letterSpacing: 1.2, fontWeight: 600 }}>TAP THE TRIP · OPENS ITS OWN HOME</div>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

// ─── 4 · LOADING / ERROR / OFFLINE ──────────────────────────────
function HomeLoading() {
  const bar = (w, mt) => <div style={{ height: 11, width: w, borderRadius: 6, background: T.cardSoft, marginTop: mt }}/>;
  return (
    <Phone bg={T.bg}>
      <TripsTopBar eyebrow="TRIPS · 3 · MARCH ’26"/>
      <div style={{ padding: '18px 22px 0' }}>
        <h1 style={{ fontFamily: T.serif, fontWeight: 500, fontSize: 36, lineHeight: 0.96, letterSpacing: -1, color: T.ink, margin: 0 }}>Your planning table.</h1>
      </div>
      {/* loading hero — editorial copy, skeleton, no spinner */}
      <div style={{ margin: '16px 16px 0', padding: '16px 17px', background: T.cardWarm, borderRadius: 16, border: `0.5px solid ${T.hairline}` }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 7 }}>
          <TripIcons.Sparkle s={13}/>
          <span style={{ fontFamily: T.mono, fontSize: 9, color: T.goldDeep, letterSpacing: 1.6, fontWeight: 700 }}>VESPER IS SHAPING THIS…</span>
        </div>
        {bar('70%', 16)}{bar('92%', 10)}{bar('55%', 10)}
        <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12.5, color: T.muteSoft, marginTop: 14 }}>a moment — pulling your saves and the week’s weather.</div>
      </div>
      {/* offline / error — quiet hairline row */}
      <div style={{ padding: '18px 22px 0' }}>
        <div style={{ paddingTop: 14, borderTop: `0.5px solid ${T.hairline}`, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
          <div style={{ minWidth: 0 }}>
            <div style={{ fontFamily: T.mono, fontSize: 8.5, color: T.mute, letterSpacing: 1.4, fontWeight: 700 }}>OFFLINE</div>
            <div style={{ fontFamily: T.serif, fontSize: 14, color: T.ink, marginTop: 3, letterSpacing: -0.1 }}>Showing your last view. <span style={{ fontStyle: 'italic', color: T.mute }}>Vesper will catch up when you’re back.</span></div>
          </div>
          <span style={{ fontFamily: T.mono, fontSize: 8, color: T.goldDeep, letterSpacing: 1, fontWeight: 700, border: `0.5px solid ${T.hairline}`, borderRadius: 999, padding: '5px 10px' }}>RETRY</span>
        </div>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

Object.assign(window, { GroupHome, UrgentHome, TapHandoff, HomeLoading });
