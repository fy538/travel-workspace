// ═══════════════════════════════════════════════════════════════
// TRANSPORT · by-traveler view (final). "How you travel" title + a
// traveler rail (nothing selected by default → shows EVERYONE grouped
// by traveler as detailed journey spines). Tap a traveler → filters to
// just them; unclick → all again. Reuses DR + SPEEP-ish local palette.
// ═══════════════════════════════════════════════════════════════

const TPC = { T: '#A0703A', A: '#7C8F73', M: '#3D5066' };
const TPEEP = [['T', 'You', 'done'], ['A', 'Ana', 'partial'], ['M', 'Mara', 'none']];
function PAv({ who, s = 18, ring = '#EFEAE0', on }) {
  return <div style={{ width: s, height: s, borderRadius: 999, background: TPC[who] || '#888', color: '#fff', fontFamily: DR.serif, fontSize: s * 0.46, fontWeight: 500, display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0, border: on ? `2px solid ${DR.ink}` : `1.5px solid ${ring}` }}>{who}</div>;
}
const psk = (s = 11, c = DR.gold) => <svg width={s} height={s} viewBox="0 0 24 24" fill={c}><path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z"/></svg>;
const PMODE = { plane: <path d="M2 12l20-7-7 20-3-9-10-4z"/>, train: <><rect x="6" y="4" width="12" height="13" rx="3"/><path d="M6 11h12M9 20l-2 2M15 20l2 2"/></> };
function PMI({ m, s = 13, c = DR.soft }) { return <svg width={s} height={s} viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round">{PMODE[m]}</svg>; }
const STC = { done: '#3D7050', partial: DR.gold, none: DR.faint };
const STL = { done: 'Round trip booked', partial: 'One-way · return open', none: 'Nothing booked yet' };

// rich journey blocks per traveler
const JOURNEYS = {
  T: [
    { m: 'plane', day: 'MON 18', route: 'JFK → LIS', sub: 'TP 204 · 14:20–02:25+1 · seat 14C · T2' },
    { m: 'train', day: 'THU 22', route: 'Lisbon → Porto', sub: 'CP 1842 · 09:10–12:05 · coach 4' },
    { m: 'plane', day: 'SAT 24', route: 'OPO → JFK', sub: 'TP 205 · 18:55–22:40 · seat 9A' },
  ],
  A: [
    { m: 'plane', day: 'MON 18', route: 'CDG → LIS', sub: 'TP 1018 · 16:05–18:10 · seat 22F' },
    { m: 'train', day: 'THU 22', route: 'Lisbon → Porto', sub: 'CP 1842 · 09:10–12:05 · with group' },
    { m: 'plane', day: '—', route: 'Return', sub: 'not booked', open: true },
  ],
  M: [
    { m: 'plane', day: 'TUE 19', route: 'LHR → LIS', sub: 'a day after the group', open: true },
    { m: 'plane', day: '—', route: 'Return', sub: 'with you, the 24th · not booked', open: true },
  ],
};

function Spine({ who, compact }) {
  const legs = JOURNEYS[who];
  return (
    <div style={{ padding: '0 4px' }}>
      {legs.map((l, i) => (
        <div key={i} style={{ display: 'grid', gridTemplateColumns: '50px 16px 1fr', gap: 11, alignItems: 'flex-start' }}>
          <div style={{ textAlign: 'right', fontFamily: DR.mono, fontSize: 8.5, color: l.open && l.day === '—' ? DR.faint : DR.mute, letterSpacing: 0.5, fontWeight: 600, paddingTop: 4 }}>{l.day}</div>
          <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
            <div style={{ width: 28, height: 28, borderRadius: 999, background: l.open && l.day === '—' ? 'transparent' : DR.card, border: l.open && l.day === '—' ? `1.4px dashed ${DR.gold}` : `0.5px solid ${DR.hair}`, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>{!(l.open && l.day === '—') && <PMI m={l.m} s={13}/>}</div>
            {i < legs.length - 1 && <span style={{ width: 1, flex: 1, minHeight: compact ? 16 : 22, background: DR.hairThin }}/>}
          </div>
          <div style={{ paddingBottom: compact ? 14 : 18, paddingTop: 3 }}>
            <div style={{ fontFamily: DR.serif, fontSize: 15, fontWeight: 500, color: l.open && l.day === '—' ? DR.goldDeep : DR.ink, letterSpacing: -0.2 }}>{l.route}</div>
            <div style={{ fontFamily: l.open ? DR.serif : DR.mono, fontStyle: l.open ? 'italic' : 'normal', fontSize: l.open ? 12 : 8.5, color: DR.mute, marginTop: 2, letterSpacing: l.open ? -0.05 : 0.3 }}>{l.sub}</div>
            {l.open && l.day === '—' && <div style={{ fontSize: 11.5, color: DR.blue, fontWeight: 600, marginTop: 4 }}>Have Vesper find it →</div>}
          </div>
        </div>
      ))}
    </div>
  );
}

function PFrame({ children }) {
  return <Phone bg={DR.paper}><div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>{children}</div><TabBar active="trips"/></Phone>;
}
function Header() {
  return (
    <div style={{ padding: '0 22px' }}>
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
        <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke={DR.soft} strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><path d="M14 6l-6 6 6 6"/></svg>
        <span style={{ fontSize: 9.5, letterSpacing: 2, color: DR.mute, fontWeight: 700 }}>TRANSPORT</span>
        <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke={DR.soft} strokeWidth="1.6" strokeLinecap="round"><path d="M12 5v14M5 12h14"/></svg>
      </div>
      <h1 style={{ fontFamily: DR.serif, fontSize: 28, fontWeight: 500, letterSpacing: -0.6, lineHeight: 1, color: DR.ink, margin: '14px 0 0' }}>How you travel</h1>
    </div>
  );
}
function RailRow({ sel }) {
  return (
    <div style={{ display: 'flex', gap: 16, padding: '14px 22px 14px', overflow: 'hidden', borderBottom: `0.5px solid ${DR.hairThin}` }}>
      {TPEEP.map(([w, name, st]) => {
        const dim = sel && sel !== w;
        return (
          <div key={w} style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 5, opacity: dim ? 0.4 : 1 }}>
            <div style={{ position: 'relative' }}>
              <PAv who={w} s={40} on={w === sel}/>
              <span style={{ position: 'absolute', bottom: 0, right: 0, width: 11, height: 11, borderRadius: 11, background: STC[st], border: `2px solid ${DR.paper}` }}/>
            </div>
            <span style={{ fontSize: 10.5, fontWeight: w === sel ? 700 : 500, color: w === sel ? DR.ink : DR.mute }}>{name}</span>
          </div>
        );
      })}
    </div>
  );
}
// one traveler's grouped card (used in the "everyone" default)
function PersonCard({ who }) {
  const [, name, st] = TPEEP.find(p => p[0] === who);
  return (
    <div style={{ padding: '14px 18px 4px' }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 12 }}>
        <PAv who={who} s={26} ring={DR.paper}/>
        <span style={{ fontFamily: DR.serif, fontSize: 17, fontWeight: 500, color: DR.ink, letterSpacing: -0.2, flex: 1 }}>{name}</span>
        <span style={{ display: 'inline-flex', alignItems: 'center', gap: 5, fontSize: 9, letterSpacing: 0.8, color: st === 'done' ? '#3D7050' : st === 'partial' ? DR.goldDeep : DR.mute, fontWeight: 700 }}><span style={{ width: 6, height: 6, borderRadius: 6, background: STC[st] }}/>{STL[st].toUpperCase()}</span>
      </div>
      <Spine who={who} compact/>
    </div>
  );
}

// DEFAULT — everyone, grouped by traveler (nothing selected)
function ByTravelerAll() {
  return (
    <PFrame>
      <Header/>
      <div style={{ marginTop: 12 }}><RailRow sel={null}/></div>
      <div style={{ paddingTop: 4 }}>
        <PersonCard who="T"/>
        <div style={{ borderTop: `0.5px solid ${DR.hairThin}`, margin: '6px 18px 0' }}/>
        <PersonCard who="A"/>
        <div style={{ borderTop: `0.5px solid ${DR.hairThin}`, margin: '6px 18px 0' }}/>
        <PersonCard who="M"/>
      </div>
    </PFrame>
  );
}

// FILTERED — tapped a traveler (Ana); rail shows her selected, her detail only
function ByTravelerOne() {
  return (
    <PFrame>
      <Header/>
      <div style={{ marginTop: 12 }}><RailRow sel="A"/></div>
      <div style={{ padding: '16px 22px 8px', display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
        <h2 style={{ fontFamily: DR.serif, fontSize: 21, fontWeight: 500, letterSpacing: -0.3, color: DR.ink, margin: 0 }}>Ana</h2>
        <span style={{ fontSize: 11, color: DR.blue, fontWeight: 600 }}>✕ show everyone</span>
      </div>
      <div style={{ padding: '4px 20px 0' }}><Spine who="A"/></div>
      <div style={{ margin: '4px 20px 0', padding: '13px 15px', background: DR.cardSoft, borderRadius: 13, border: `0.8px solid rgba(176,133,58,0.4)` }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 6, marginBottom: 5 }}>{psk(11)}<span style={{ fontSize: 8.5, letterSpacing: 1.4, color: DR.goldDeep, fontWeight: 700 }}>VESPER</span></div>
        <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 14, color: DR.ink, margin: '0 0 11px', lineHeight: 1.4, letterSpacing: -0.1 }}>Ana’s outbound is set — her return’s still open. Want me to match it to yours on the 24th?</p>
        <span style={{ display: 'inline-block', padding: '10px 18px', background: DR.blue, color: '#fff', borderRadius: 999, fontSize: 13, fontWeight: 600 }}>Find her return</span>
      </div>
    </PFrame>
  );
}

Object.assign(window, { ByTravelerAll, ByTravelerOne });
