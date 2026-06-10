// ═══════════════════════════════════════════════════════════════
// TRIP DETAIL PAGES — the four facet doorways, 4 variations each.
//   STAY (who-sleeps-where) · TRANSPORT (per-person arrivals) ·
//   COSTS (split ledger) · ROUTE (map / how you move).
// Reuses DR + StyleRiso + Ppl/CASTD.  Each fn = one full Phone screen.
// ═══════════════════════════════════════════════════════════════

const dk = (s = 13, c = DR.gold) => <svg width={s} height={s} viewBox="0 0 24 24" fill={c}><path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z"/></svg>;
function DHead({ kicker, title }) {
  return (
    <div style={{ padding: '12px 20px 0' }}>
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
        <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke={DR.soft} strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><path d="M14 6l-6 6 6 6"/></svg>
        <Ppl who={CASTD} size={21}/>
      </div>
      <div style={{ marginTop: 12 }}>
        <div style={{ fontSize: 9, letterSpacing: 2, color: DR.mute, fontWeight: 700 }}>{kicker}</div>
        <h1 style={{ fontFamily: DR.serif, fontSize: 28, fontWeight: 500, letterSpacing: -0.7, lineHeight: 1, color: DR.ink, margin: '5px 0 0' }}>{title}</h1>
      </div>
    </div>
  );
}
const PEEP = [['T', '#A0703A', 'You'], ['A', '#7C8F73', 'Ana'], ['M', '#3D5066', 'Mara']];
function Av({ i, c, s = 22 }) { return <div style={{ width: s, height: s, borderRadius: 999, background: c, color: '#fff', fontFamily: DR.serif, fontSize: s * 0.42, fontWeight: 500, display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0 }}>{i}</div>; }

// ─────────────── STAY · who sleeps where ───────────────
// S-A · timeline of stays by night, with who's in each
function StayA() {
  const stays = [['18–20', 'Casa do Alecrim', 'Alfama', 'all three'], ['20–22', '— to pick —', 'nights 5–7', '', true], ['22–24', 'Tivoli, river room', 'Cais', 'you + Ana']];
  return (
    <Phone bg={DR.paper}><div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
      <DHead kicker="STAY" title="Where you sleep"/>
      <div style={{ padding: '16px 20px 0' }}>
        {stays.map(([n, name, area, who, gap], i) => (
          <div key={i} style={{ display: 'flex', gap: 13, padding: '13px 0', borderTop: i ? `0.5px solid ${DR.hairThin}` : 'none', alignItems: 'center' }}>
            <div style={{ fontFamily: DR.mono, fontSize: 10, color: DR.mute, letterSpacing: 0.5, fontWeight: 600, width: 44, flexShrink: 0 }}>MAY<br/>{n}</div>
            {!gap && <div style={{ width: 46, height: 46, borderRadius: 8, overflow: 'hidden', flexShrink: 0 }}><StyleRiso w={46} h={46}/></div>}
            <div style={{ flex: 1, minWidth: 0 }}>
              <div style={{ fontFamily: DR.serif, fontSize: 16, fontWeight: 500, color: gap ? DR.goldDeep : DR.ink, fontStyle: gap ? 'italic' : 'normal', letterSpacing: -0.2 }}>{name}</div>
              <div style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 11.5, color: DR.mute, marginTop: 2 }}>{area}{who && ` · ${who}`}</div>
            </div>
            {gap ? <span style={{ padding: '6px 11px', background: DR.blue, color: '#fff', borderRadius: 999, fontSize: 11, fontWeight: 600 }}>Pick</span> : <span style={{ color: DR.faint }}>›</span>}
          </div>
        ))}
      </div>
    </div><TabBar active="trips"/></Phone>
  );
}
// S-B · per-person columns (who's where each night)
function StayB() {
  const nights = ['18', '19', '20', '21', '22', '23'];
  const plan = { T: [0,0,1,1,2,2], A: [0,0,1,1,2,2], M: [0,0,1,1,3,3] }; // stay index per night
  const homes = ['Casa do Alecrim', 'Casa do Alecrim', '— pick —', '— pick —', 'Tivoli', 'Solar dos Mouros'];
  return (
    <Phone bg={DR.paper}><div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
      <DHead kicker="STAY · BY PERSON" title="Not everyone’s together"/>
      <div style={{ padding: '16px 16px 0' }}>
        <div style={{ display: 'grid', gridTemplateColumns: '54px 1fr 1fr 1fr', gap: 0, alignItems: 'center' }}>
          <div/>
          {PEEP.map(([i, c]) => <div key={i} style={{ display: 'flex', justifyContent: 'center', paddingBottom: 8 }}><Av i={i} c={c} s={24}/></div>)}
          {nights.map((n, ni) => (
            <React.Fragment key={n}>
              <div style={{ fontFamily: DR.mono, fontSize: 9, color: DR.mute, letterSpacing: 0.5, fontWeight: 600, padding: '8px 0', borderTop: `0.5px solid ${DR.hairThin}` }}>MAY {n}</div>
              {['T','A','M'].map(p => {
                const idx = plan[p][ni]; const gap = homes[plan[p][ni]] && homes[plan[p][ni]].startsWith('—');
                return <div key={p} style={{ padding: '8px 3px', borderTop: `0.5px solid ${DR.hairThin}`, display: 'flex', justifyContent: 'center' }}>
                  <span style={{ width: 26, height: 9, borderRadius: 4, background: gap ? 'transparent' : ['#C9B79A','#C9B79A','#B5AFA5','#9FB0B6'][idx] || '#C9B79A', border: gap ? `1px dashed ${DR.gold}` : 'none' }}/>
                </div>;
              })}
            </React.Fragment>
          ))}
        </div>
        <div style={{ marginTop: 14, padding: '11px 13px', background: DR.cardSoft, borderRadius: 12, border: `0.8px solid rgba(176,133,58,0.4)` }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>{dk(11)}<span style={{ fontSize: 8.5, letterSpacing: 1.4, color: DR.goldDeep, fontWeight: 700 }}>VESPER</span></div>
          <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 13.5, color: DR.ink, margin: '5px 0 0', lineHeight: 1.35 }}>Nights 5–7 are unbooked for everyone — and Mara splits off on the 22nd.</p>
        </div>
      </div>
    </div><TabBar active="trips"/></Phone>
  );
}
// S-C · the recommended stay, rich (a single decision page)
function StayC() {
  return (
    <Phone bg={DR.ink}><div style={{ position: 'absolute', inset: 0, overflow: 'hidden', background: DR.paper }}>
      <div style={{ position: 'relative', height: 280 }}>
        <StyleRiso w={393} h={280}/>
        <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to bottom, rgba(20,14,9,0.34), rgba(20,14,9,0) 40%, rgba(20,14,9,0.7))' }}/>
        <div style={{ position: 'absolute', top: 54, left: 18 }}><svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="#fff" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d="M14 6l-6 6 6 6"/></svg></div>
        <div style={{ position: 'absolute', left: 20, right: 20, bottom: 16 }}>
          <span style={{ padding: '4px 9px', borderRadius: 999, background: 'rgba(20,14,9,0.5)', backdropFilter: 'blur(6px)', fontSize: 8.5, letterSpacing: 1.2, fontWeight: 700, color: '#fff' }}>VESPER’S PICK · NIGHTS 5–7</span>
          <h1 style={{ fontFamily: DR.serif, fontSize: 30, fontWeight: 500, letterSpacing: -0.6, lineHeight: 1, color: '#fff', margin: '8px 0 0' }}>Casa do Alecrim</h1>
        </div>
      </div>
      <div style={{ padding: '16px 20px 0' }}>
        <div style={{ display: 'flex', gap: 7, marginBottom: 13 }}>{['ALFAMA','€180/NT','FREE CANCEL','2 ROOMS'].map(m => <span key={m} style={{ padding: '4px 9px', fontFamily: DR.mono, fontSize: 8.5, color: DR.mute, letterSpacing: 0.8, fontWeight: 600, background: DR.card, border: `0.5px solid ${DR.hair}`, borderRadius: 999 }}>{m}</span>)}</div>
        <p style={{ fontFamily: DR.serif, fontSize: 15, color: DR.ink, lineHeight: 1.5, margin: 0, letterSpacing: -0.05 }}>A tiled house above the cemetery wall — mornings open to the river, the street goes quiet by nine. Fits the three of you, two rooms.</p>
      </div>
      <div style={{ position: 'absolute', bottom: 0, left: 0, right: 0, padding: '12px 18px 20px', background: 'rgba(247,242,231,0.92)', backdropFilter: 'blur(20px)', borderTop: `0.5px solid ${DR.hair}`, display: 'flex', gap: 10, alignItems: 'center' }}>
        <span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 13, color: DR.mute, flex: 1 }}>see the other two</span>
        <span style={{ padding: '11px 20px', background: DR.blue, color: '#fff', borderRadius: 999, fontSize: 13, fontWeight: 600 }}>Hold it</span>
      </div>
    </div><TabBar active="trips"/></Phone>
  );
}
// S-D · options list to choose from (3 candidates compared)
function StayD() {
  const opts = [['Casa do Alecrim', 'Alfama · quiet alley', '€180', true], ['Solar dos Mouros', 'Castelo · the view', '€210', false], ['Tivoli', 'Cais · river room', '€240', false]];
  return (
    <Phone bg={DR.paper}><div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
      <DHead kicker="STAY · 3 TO CHOOSE" title="Nights 5–7"/>
      <div style={{ padding: '16px 16px 0', display: 'flex', flexDirection: 'column', gap: 10 }}>
        {opts.map(([n, sub, price, pick], i) => (
          <div key={i} style={{ display: 'flex', gap: 12, padding: 11, background: DR.card, borderRadius: 14, border: `0.5px solid ${pick ? 'rgba(176,133,58,0.5)' : DR.hair}` }}>
            <div style={{ width: 64, height: 64, borderRadius: 9, overflow: 'hidden', flexShrink: 0 }}><StyleRiso w={64} h={64}/></div>
            <div style={{ flex: 1, minWidth: 0 }}>
              {pick && <div style={{ display: 'flex', alignItems: 'center', gap: 5, marginBottom: 3 }}>{dk(10)}<span style={{ fontSize: 8, letterSpacing: 1.2, color: DR.goldDeep, fontWeight: 700 }}>VESPER’S PICK</span></div>}
              <div style={{ fontFamily: DR.serif, fontSize: 16, fontWeight: 500, color: DR.ink, letterSpacing: -0.2, lineHeight: 1.05 }}>{n}</div>
              <div style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 11.5, color: DR.mute, marginTop: 2 }}>{sub}</div>
            </div>
            <div style={{ textAlign: 'right', display: 'flex', flexDirection: 'column', justifyContent: 'space-between' }}>
              <span style={{ fontFamily: DR.serif, fontSize: 15, fontWeight: 500, color: DR.ink }}>{price}</span>
              <span style={{ fontFamily: DR.mono, fontSize: 8, color: DR.mute }}>/NIGHT</span>
            </div>
          </div>
        ))}
      </div>
    </div><TabBar active="trips"/></Phone>
  );
}

// ─────────────── TRANSPORT · per-person arrivals ───────────────
// T-A · arrivals board (when everyone lands)
function TransA() {
  const arr = [['You', '#A0703A', 'TP 204', 'MAY 18 · 14:20', 'from JFK'], ['Ana', '#7C8F73', 'TP 1018', 'MAY 18 · 16:05', 'from CDG'], ['Mara', '#3D5066', 'TP 442', 'MAY 19 · 09:30', 'from LHR · a day late']];
  return (
    <Phone bg={DR.paper}><div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
      <DHead kicker="TRANSPORT · ARRIVALS" title="When everyone lands"/>
      <div style={{ padding: '16px 20px 0' }}>
        {arr.map(([who, c, fl, when, note], i) => (
          <div key={i} style={{ display: 'flex', gap: 12, padding: '14px 0', borderTop: i ? `0.5px solid ${DR.hairThin}` : 'none', alignItems: 'center' }}>
            <Av i={who[0]} c={c} s={26}/>
            <div style={{ flex: 1 }}>
              <div style={{ fontFamily: DR.serif, fontSize: 16, fontWeight: 500, color: DR.ink, letterSpacing: -0.2 }}>{who} <span style={{ fontFamily: DR.mono, fontSize: 9, color: DR.mute, letterSpacing: 1 }}>· {fl}</span></div>
              <div style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 11.5, color: DR.mute, marginTop: 2 }}>{note}</div>
            </div>
            <div style={{ fontFamily: DR.mono, fontSize: 10, color: DR.ink, letterSpacing: 0.5, fontWeight: 600, textAlign: 'right' }}>{when.split(' · ')[1]}<br/><span style={{ color: DR.mute, fontSize: 8.5 }}>{when.split(' · ')[0]}</span></div>
          </div>
        ))}
        <div style={{ marginTop: 12, padding: '11px 13px', background: DR.cardSoft, borderRadius: 12, border: `0.8px solid rgba(176,133,58,0.4)` }}>
          <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 13.5, color: DR.ink, margin: 0, lineHeight: 1.35 }}>{dk(11)} You and Ana land 2 hrs apart — share a cab from the airport?</p>
        </div>
      </div>
    </div><TabBar active="trips"/></Phone>
  );
}
// T-B · timeline of all legs (getting there + within-trip)
function TransB() {
  const legs = [['MAY 18', 'Fly JFK → LIS', 'you · TP204', 'plane'], ['MAY 18', 'Airport → Alfama', 'cab, shared w/ Ana', 'car'], ['MAY 21', 'Lisbon → Sintra', 'train, 40 min', 'train'], ['MAY 24', 'LIS → JFK', 'you · TP205', 'plane']];
  const gl = { plane: <path d="M2 12l20-7-7 20-3-9-10-4z"/>, car: <><rect x="3" y="11" width="18" height="6" rx="2"/><circle cx="7" cy="18" r="1.5"/><circle cx="17" cy="18" r="1.5"/></>, train: <><rect x="6" y="4" width="12" height="13" rx="3"/><path d="M6 11h12M9 20l-2 2M15 20l2 2"/></> };
  return (
    <Phone bg={DR.paper}><div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
      <DHead kicker="TRANSPORT · ALL LEGS" title="How you move"/>
      <div style={{ padding: '18px 20px 0' }}>
        {legs.map(([d, t, sub, g], i) => (
          <div key={i} style={{ display: 'grid', gridTemplateColumns: '16px 1fr', gap: 13, alignItems: 'flex-start' }}>
            <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
              <div style={{ width: 30, height: 30, borderRadius: 999, background: DR.card, border: `0.5px solid ${DR.hair}`, display: 'flex', alignItems: 'center', justifyContent: 'center', marginLeft: -7 }}><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke={DR.soft} strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round">{gl[g]}</svg></div>
              {i < legs.length - 1 && <span style={{ width: 1, flex: 1, minHeight: 26, background: DR.hairThin, marginLeft: -7 }}/>}
            </div>
            <div style={{ paddingBottom: 18, paddingTop: 4 }}>
              <span style={{ fontFamily: DR.mono, fontSize: 8.5, color: DR.mute, letterSpacing: 1, fontWeight: 600 }}>{d}</span>
              <div style={{ fontFamily: DR.serif, fontSize: 15.5, fontWeight: 500, color: DR.ink, letterSpacing: -0.2, marginTop: 2 }}>{t}</div>
              <div style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 11.5, color: DR.mute, marginTop: 1 }}>{sub}</div>
            </div>
          </div>
        ))}
      </div>
    </div><TabBar active="trips"/></Phone>
  );
}
// T-C · per-person status (who's booked)
function TransC() {
  const ppl = [['You', '#A0703A', 'Round trip booked', true], ['Ana', '#7C8F73', 'Outbound booked · return open', null], ['Mara', '#3D5066', 'Nothing booked yet', false]];
  return (
    <Phone bg={DR.paper}><div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
      <DHead kicker="TRANSPORT · BY PERSON" title="Who’s sorted"/>
      <div style={{ padding: '18px 20px 0', display: 'flex', flexDirection: 'column', gap: 10 }}>
        {ppl.map(([who, c, status, done], i) => (
          <div key={i} style={{ display: 'flex', gap: 12, alignItems: 'center', padding: '13px 14px', background: DR.card, borderRadius: 13, border: `0.5px solid ${done === false ? 'rgba(176,133,58,0.4)' : DR.hair}` }}>
            <Av i={who[0]} c={c} s={28}/>
            <div style={{ flex: 1 }}>
              <div style={{ fontFamily: DR.serif, fontSize: 16, fontWeight: 500, color: DR.ink, letterSpacing: -0.2 }}>{who}</div>
              <div style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 12, color: done === false ? DR.goldDeep : DR.mute, marginTop: 2 }}>{status}</div>
            </div>
            <span style={{ width: 9, height: 9, borderRadius: 9, background: done ? '#3D7050' : done === false ? DR.gold : DR.faint }}/>
          </div>
        ))}
        <div style={{ marginTop: 4, textAlign: 'center', fontFamily: DR.serif, fontStyle: 'italic', fontSize: 12.5, color: DR.mute }}>nudge Mara to book →</div>
      </div>
    </div><TabBar active="trips"/></Phone>
  );
}
// T-D · single ticket (boarding-pass detail)
function TransD() {
  return (
    <Phone bg={DR.paper}><div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
      <DHead kicker="TRANSPORT · YOUR FLIGHT" title="Outbound"/>
      <div style={{ padding: '18px 18px 0' }}>
        <div style={{ background: DR.card, borderRadius: 16, border: `0.5px solid ${DR.hair}`, overflow: 'hidden', boxShadow: '0 1px 0 rgba(255,255,255,0.6) inset' }}>
          <div style={{ padding: '16px 18px', display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
            <div><div style={{ fontFamily: DR.serif, fontSize: 32, fontWeight: 500, color: DR.ink, letterSpacing: -0.5 }}>JFK</div><div style={{ fontFamily: DR.mono, fontSize: 9, color: DR.mute, letterSpacing: 1 }}>14:20</div></div>
            <div style={{ flex: 1, padding: '0 14px', display: 'flex', flexDirection: 'column', alignItems: 'center' }}><svg width="20" height="20" viewBox="0 0 24 24" fill={DR.gold}><path d="M2 12l20-7-7 20-3-9-10-4z"/></svg><span style={{ fontFamily: DR.mono, fontSize: 8, color: DR.mute, marginTop: 3 }}>7H 05M</span></div>
            <div style={{ textAlign: 'right' }}><div style={{ fontFamily: DR.serif, fontSize: 32, fontWeight: 500, color: DR.ink, letterSpacing: -0.5 }}>LIS</div><div style={{ fontFamily: DR.mono, fontSize: 9, color: DR.mute, letterSpacing: 1 }}>02:25 +1</div></div>
          </div>
          <div style={{ borderTop: `1px dashed ${DR.faint}`, margin: '0 16px' }}/>
          <div style={{ padding: '13px 18px', display: 'flex', justifyContent: 'space-between' }}>
            {[['FLIGHT', 'TP 204'], ['SEAT', '14C'], ['DATE', 'MAY 18']].map(([k, v]) => <div key={k}><div style={{ fontSize: 8, letterSpacing: 1.2, color: DR.mute, fontWeight: 700 }}>{k}</div><div style={{ fontFamily: DR.serif, fontSize: 15, color: DR.ink, fontWeight: 500, marginTop: 2 }}>{v}</div></div>)}
          </div>
        </div>
        <div style={{ marginTop: 12, textAlign: 'center', fontFamily: DR.serif, fontStyle: 'italic', fontSize: 12.5, color: DR.mute }}>Ana’s on the same arrival window →</div>
      </div>
    </div><TabBar active="trips"/></Phone>
  );
}

// ─────────────── COSTS · the split ───────────────
// C-A · balances (who owes whom)
function CostA() {
  return (
    <Phone bg={DR.paper}><div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
      <DHead kicker="COSTS" title="The split"/>
      <div style={{ padding: '16px 20px 0' }}>
        <div style={{ textAlign: 'center', padding: '8px 0 16px' }}>
          <div style={{ fontFamily: DR.serif, fontSize: 40, fontWeight: 500, color: DR.ink, letterSpacing: -1 }}>€1,420</div>
          <div style={{ fontFamily: DR.mono, fontSize: 9, color: DR.mute, letterSpacing: 1, marginTop: 2 }}>SO FAR · €473 EACH</div>
        </div>
        {[['You', '#A0703A', 'paid €820', '+€347', true], ['Ana', '#7C8F73', 'paid €600', '+€127', true], ['Mara', '#3D5066', 'paid €0', '−€473', false]].map(([who, c, paid, bal, pos], i) => (
          <div key={i} style={{ display: 'flex', gap: 12, alignItems: 'center', padding: '13px 0', borderTop: `0.5px solid ${DR.hairThin}` }}>
            <Av i={who[0]} c={c} s={26}/>
            <div style={{ flex: 1 }}><div style={{ fontFamily: DR.serif, fontSize: 15.5, fontWeight: 500, color: DR.ink }}>{who}</div><div style={{ fontFamily: DR.mono, fontSize: 9, color: DR.mute, letterSpacing: 0.5, marginTop: 2 }}>{paid}</div></div>
            <div style={{ fontFamily: DR.serif, fontSize: 16, fontWeight: 500, color: pos ? '#3D7050' : '#A04030' }}>{bal}</div>
          </div>
        ))}
        <div style={{ marginTop: 14, display: 'flex', gap: 8 }}><span style={{ flex: 1, textAlign: 'center', padding: '11px 0', background: DR.blue, color: '#fff', borderRadius: 999, fontSize: 13, fontWeight: 600 }}>Settle up</span><span style={{ padding: '11px 16px', background: DR.card, border: `0.5px solid ${DR.hair}`, borderRadius: 999, fontFamily: DR.serif, fontStyle: 'italic', fontSize: 13, color: DR.soft }}>add expense</span></div>
      </div>
    </div><TabBar active="trips"/></Phone>
  );
}
// C-B · expense feed (itemized)
function CostB() {
  const ex = [['Casa do Alecrim', 'you paid', '€360', 'STAY'], ['Flights, group fare', 'Ana paid', '€600', 'TRANSPORT'], ['Ramiro dinner', 'you paid', '€140', 'FOOD'], ['Sintra train ×3', 'you paid', '€38', 'TRANSPORT']];
  return (
    <Phone bg={DR.paper}><div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
      <DHead kicker="COSTS · EXPENSES" title="What’s been spent"/>
      <div style={{ padding: '16px 20px 0' }}>
        {ex.map(([t, who, amt, tag], i) => (
          <div key={i} style={{ display: 'flex', gap: 12, alignItems: 'center', padding: '13px 0', borderTop: i ? `0.5px solid ${DR.hairThin}` : 'none' }}>
            <div style={{ flex: 1 }}><div style={{ fontFamily: DR.serif, fontSize: 15, fontWeight: 500, color: DR.ink, letterSpacing: -0.2 }}>{t}</div><div style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 11.5, color: DR.mute, marginTop: 2 }}>{who} · split 3</div></div>
            <div style={{ textAlign: 'right' }}><div style={{ fontFamily: DR.serif, fontSize: 15, fontWeight: 500, color: DR.ink }}>{amt}</div><div style={{ fontFamily: DR.mono, fontSize: 7.5, color: DR.faint, letterSpacing: 1, marginTop: 2 }}>{tag}</div></div>
          </div>
        ))}
      </div>
    </div><TabBar active="trips"/></Phone>
  );
}
// C-C · by category (where money goes)
function CostC() {
  const cats = [['Stay', 620, '#C9B79A'], ['Transport', 638, '#9FB0B6'], ['Food', 162, '#C98A57']];
  const tot = 1420;
  return (
    <Phone bg={DR.paper}><div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
      <DHead kicker="COSTS · BY CATEGORY" title="Where it goes"/>
      <div style={{ padding: '18px 20px 0' }}>
        <div style={{ display: 'flex', height: 14, borderRadius: 999, overflow: 'hidden', marginBottom: 18 }}>{cats.map(([n, v, c]) => <div key={n} style={{ width: `${v / tot * 100}%`, background: c }}/>)}</div>
        {cats.map(([n, v, c], i) => (
          <div key={n} style={{ display: 'flex', gap: 11, alignItems: 'center', padding: '11px 0', borderTop: i ? `0.5px solid ${DR.hairThin}` : 'none' }}>
            <span style={{ width: 10, height: 10, borderRadius: 3, background: c }}/>
            <span style={{ flex: 1, fontFamily: DR.serif, fontSize: 15.5, color: DR.ink }}>{n}</span>
            <span style={{ fontFamily: DR.serif, fontSize: 15, fontWeight: 500, color: DR.ink }}>€{v}</span>
            <span style={{ fontFamily: DR.mono, fontSize: 9, color: DR.mute, width: 34, textAlign: 'right' }}>{Math.round(v / tot * 100)}%</span>
          </div>
        ))}
      </div>
    </div><TabBar active="trips"/></Phone>
  );
}
// C-D · add expense (input)
function CostD() {
  return (
    <Phone bg={DR.paper}><div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
      <DHead kicker="COSTS" title="Add an expense"/>
      <div style={{ padding: '18px 20px 0' }}>
        <div style={{ textAlign: 'center', padding: '6px 0 18px' }}><span style={{ fontFamily: DR.serif, fontSize: 46, fontWeight: 500, color: DR.faint }}>€0</span></div>
        {[['WHAT', 'Dinner at…'], ['WHO PAID', 'You'], ['SPLIT', 'Evenly · 3 ways']].map(([k, v], i) => (
          <div key={k} style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '14px 14px', background: DR.card, borderRadius: 12, border: `0.5px solid ${DR.hair}`, marginBottom: 8 }}>
            <span style={{ fontSize: 8.5, letterSpacing: 1.4, color: DR.mute, fontWeight: 700 }}>{k}</span>
            <span style={{ fontFamily: DR.serif, fontSize: 15, color: i ? DR.ink : DR.faint, letterSpacing: -0.1 }}>{v}</span>
          </div>
        ))}
        <div style={{ marginTop: 8, padding: '13px 0', textAlign: 'center', background: DR.blue, color: '#fff', borderRadius: 999, fontSize: 13.5, fontWeight: 600 }}>Add it</div>
      </div>
    </div><TabBar active="trips"/></Phone>
  );
}

// ─────────────── ROUTE · map / how you move ───────────────
// R-A · illustrated city map with pins
function RouteA() {
  return (
    <Phone bg={DR.paper}><div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
      <DHead kicker="ROUTE" title="Your Lisbon"/>
      <div style={{ padding: '14px 16px 0' }}>
        <div style={{ height: 340, borderRadius: 16, overflow: 'hidden', position: 'relative', border: `0.5px solid ${DR.hair}` }}>
          <StyleRiso w={361} h={340}/>
          <div style={{ position: 'absolute', inset: 0, background: 'rgba(239,234,224,0.35)' }}/>
          <svg style={{ position: 'absolute', inset: 0, width: '100%', height: '100%' }} viewBox="0 0 361 340"><path d="M60 250 Q120 200 170 210 Q230 220 280 150" stroke={DR.gold} strokeWidth="1.6" strokeDasharray="2 4" fill="none"/></svg>
          {[[60, 250, 'Casa', true], [170, 210, 'Ramiro'], [280, 150, 'Belém'], [120, 110, 'Graça']].map(([x, y, l, p], i) => (
            <div key={i} style={{ position: 'absolute', left: x, top: y, transform: 'translate(-50%,-50%)', display: 'flex', alignItems: 'center', gap: 4 }}>
              <span style={{ width: p ? 11 : 8, height: p ? 11 : 8, borderRadius: 999, background: p ? DR.gold : DR.ink, boxShadow: p ? `0 0 0 4px rgba(176,133,58,0.2)` : 'none' }}/>
              <span style={{ fontFamily: DR.serif, fontSize: 12, fontWeight: 500, color: DR.ink, background: 'rgba(247,242,231,0.8)', padding: '1px 5px', borderRadius: 4 }}>{l}</span>
            </div>
          ))}
        </div>
      </div>
    </div><TabBar active="trips"/></Phone>
  );
}
// R-B · multi-city route (the trip's geography)
function RouteB() {
  const cities = [['Lisbon', 'May 18–22 · 4 nights', true], ['Sintra', 'May 21 · day trip', false], ['Porto', 'May 22–24 · 2 nights', false]];
  return (
    <Phone bg={DR.paper}><div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
      <DHead kicker="ROUTE · 3 STOPS" title="Where you go"/>
      <div style={{ padding: '18px 20px 0' }}>
        {cities.map(([c, sub, m], i) => (
          <div key={i} style={{ display: 'grid', gridTemplateColumns: '16px 1fr', gap: 14, alignItems: 'flex-start' }}>
            <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
              <span style={{ width: 12, height: 12, borderRadius: 999, background: m ? DR.gold : DR.card, border: `1.5px solid ${m ? DR.gold : DR.faint}`, marginTop: 3 }}/>
              {i < cities.length - 1 && <span style={{ width: 1, flex: 1, minHeight: 40, background: DR.hairThin }}/>}
            </div>
            <div style={{ paddingBottom: 22 }}>
              <div style={{ fontFamily: DR.serif, fontSize: 19, fontWeight: 500, color: DR.ink, letterSpacing: -0.3 }}>{c}</div>
              <div style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 12, color: DR.mute, marginTop: 2 }}>{sub}</div>
              <div style={{ marginTop: 8, height: 54, borderRadius: 8, overflow: 'hidden' }}><StyleRiso w={300} h={54}/></div>
            </div>
          </div>
        ))}
      </div>
    </div><TabBar active="trips"/></Phone>
  );
}
// R-C · a day's walking route (turn-by-turn-ish)
function RouteC() {
  const stops = [['09:30', 'Casa do Alecrim', 'start'], ['10:00', 'Coffee at Kayaba', '8 min walk'], ['11:00', 'Cemetery walk', '5 min'], ['13:00', 'Lunch · Ramiro', 'cab, 10 min']];
  return (
    <Phone bg={DR.paper}><div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
      <DHead kicker="ROUTE · MON 20" title="The day’s path"/>
      <div style={{ padding: '14px 16px 0' }}>
        <div style={{ height: 130, borderRadius: 12, overflow: 'hidden', position: 'relative', marginBottom: 14 }}><StyleRiso w={361} h={130}/><svg style={{ position: 'absolute', inset: 0, width: '100%', height: '100%' }} viewBox="0 0 361 130"><path d="M40 100 Q120 60 200 80 T330 40" stroke={DR.gold} strokeWidth="1.6" strokeDasharray="2 4" fill="none"/></svg></div>
        {stops.map(([t, name, sub], i) => (
          <div key={i} style={{ display: 'flex', gap: 12, alignItems: 'center', padding: '10px 0', borderTop: i ? `0.5px solid ${DR.hairThin}` : 'none' }}>
            <span style={{ fontFamily: DR.mono, fontSize: 9.5, color: DR.mute, letterSpacing: 0.5, fontWeight: 600, width: 38 }}>{t}</span>
            <div style={{ flex: 1 }}><div style={{ fontFamily: DR.serif, fontSize: 15, fontWeight: 500, color: DR.ink, letterSpacing: -0.2 }}>{name}</div></div>
            <span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 11, color: DR.mute }}>{sub}</span>
          </div>
        ))}
      </div>
    </div><TabBar active="trips"/></Phone>
  );
}
// R-D · live map (in-trip, you-are-here)
function RouteD() {
  return (
    <Phone bg={DR.ink}><div style={{ position: 'absolute', inset: 0, overflow: 'hidden' }}>
      <StyleRiso w={393} h={852}/>
      <div style={{ position: 'absolute', inset: 0, background: 'rgba(20,14,9,0.18)' }}/>
      <div style={{ position: 'absolute', top: 54, left: 18 }}><div style={{ width: 36, height: 36, borderRadius: 999, background: 'rgba(255,255,255,0.22)', backdropFilter: 'blur(8px)', display: 'flex', alignItems: 'center', justifyContent: 'center' }}><svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="#fff" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d="M14 6l-6 6 6 6"/></svg></div></div>
      {/* you-are-here */}
      <div style={{ position: 'absolute', left: '42%', top: '46%' }}><span style={{ display: 'block', width: 16, height: 16, borderRadius: 999, background: DR.blue, border: '2.5px solid #fff', boxShadow: '0 0 0 6px rgba(61,80,102,0.3)' }}/></div>
      {/* bottom sheet */}
      <div style={{ position: 'absolute', left: 0, right: 0, bottom: 0, background: DR.paper, borderRadius: '20px 20px 0 0', padding: '14px 20px 24px' }}>
        <div style={{ display: 'flex', justifyContent: 'center', marginBottom: 10 }}><div style={{ width: 34, height: 4, borderRadius: 4, background: DR.faint }}/></div>
        <div style={{ display: 'flex', alignItems: 'center', gap: 6, marginBottom: 6 }}>{dk(12)}<span style={{ fontSize: 9, letterSpacing: 1.4, color: DR.goldDeep, fontWeight: 700 }}>NEAR YOU NOW</span></div>
        <div style={{ fontFamily: DR.serif, fontSize: 18, fontWeight: 500, color: DR.ink, letterSpacing: -0.3 }}>You’re 6 min from Kayaba</div>
        <div style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 13, color: DR.mute, marginTop: 3 }}>the next stop on today’s path · Ana’s already there</div>
      </div>
    </div><TabBar active="trips"/></Phone>
  );
}

Object.assign(window, { StayA, StayB, StayC, StayD, TransA, TransB, TransC, TransD, CostA, CostB, CostC, CostD, RouteA, RouteB, RouteC, RouteD });
