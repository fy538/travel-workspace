// ═══════════════════════════════════════════════════════════════
// TRANSPORT · combined full pages (tall scroll). Three ways to compose
// the zones into ONE coherent page. No integration-heavy actions
// (no seat-change etc.) — changes route to Vesper; we surface status,
// timing, legs, the rental. Reuses DR + SPEEP + trip-transport bits.
// ═══════════════════════════════════════════════════════════════

function CAv({ who, s = 18, ring = '#EFEAE0' }) {
  return <div style={{ width: s, height: s, borderRadius: 999, background: SPEEP[who], color: '#fff', fontFamily: DR.serif, fontSize: s * 0.46, fontWeight: 500, display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0, border: `1.5px solid ${ring}` }}>{who}</div>;
}
const csk = (s = 11, c = DR.gold) => <svg width={s} height={s} viewBox="0 0 24 24" fill={c}><path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z"/></svg>;
const CMODE = { plane: <path d="M2 12l20-7-7 20-3-9-10-4z"/>, train: <><rect x="6" y="4" width="12" height="13" rx="3"/><path d="M6 11h12M9 20l-2 2M15 20l2 2"/></>, car: <><rect x="3" y="11" width="18" height="6" rx="2"/><circle cx="7" cy="18" r="1.5"/><circle cx="17" cy="18" r="1.5"/><path d="M5 11l2-4h10l2 4"/></>, cab: <><rect x="3" y="11" width="18" height="6" rx="2"/><circle cx="7" cy="18" r="1.5"/><circle cx="17" cy="18" r="1.5"/><path d="M9 7h6v4H9z"/></> };
function CMI({ m, s = 15, c = DR.soft }) { return <svg width={s} height={s} viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round">{CMODE[m]}</svg>; }

function CFrame({ children }) {
  return <Phone bg={DR.paper}><div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'auto', paddingBottom: 88 }}>{children}</div><TabBar active="trips"/></Phone>;
}
function CHead({ sub }) {
  return (
    <div style={{ padding: '6px 24px 14px' }}>
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
        <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke={DR.soft} strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><path d="M14 6l-6 6 6 6"/></svg>
        <span style={{ fontSize: 9.5, letterSpacing: 2, color: DR.mute, fontWeight: 700 }}>TRANSPORT</span>
        <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke={DR.soft} strokeWidth="1.6" strokeLinecap="round"><path d="M12 5v14M5 12h14"/></svg>
      </div>
      <h1 style={{ fontFamily: DR.serif, fontSize: 28, fontWeight: 500, letterSpacing: -0.6, lineHeight: 1, color: DR.ink, margin: '14px 0 0' }}>How you travel</h1>
      {sub && <div style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 13, color: DR.mute, marginTop: 6 }}>{sub}</div>}
    </div>
  );
}
function ZL({ children, note }) {
  return <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', padding: '0 24px 8px' }}>
    <span style={{ fontSize: 9, letterSpacing: 1.8, color: DR.mute, fontWeight: 700 }}>{children}</span>
    {note && <span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 11, color: DR.faint }}>{note}</span>}
  </div>;
}
function VLine({ children }) {
  return <div style={{ margin: '4px 24px 0', paddingLeft: 13, borderLeft: `2px solid ${DR.gold}` }}>
    <div style={{ display: 'flex', alignItems: 'center', gap: 6, marginBottom: 4 }}>{csk(11)}<span style={{ fontSize: 8.5, letterSpacing: 1.4, color: DR.goldDeep, fontWeight: 700 }}>VESPER</span></div>
    <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 14, color: DR.ink, margin: 0, lineHeight: 1.4, letterSpacing: -0.1 }}>{children}</p>
  </div>;
}
function Arr({ who, code, where, time, note, first }) {
  return <div style={{ display: 'grid', gridTemplateColumns: '52px 1fr', gap: 13, padding: '11px 24px', borderTop: first ? 'none' : `0.5px solid ${DR.hairThin}`, alignItems: 'center' }}>
    <div style={{ textAlign: 'right' }}><div style={{ fontFamily: DR.serif, fontSize: 15, fontWeight: 500, color: DR.ink, letterSpacing: -0.3, lineHeight: 1 }}>{time}</div><div style={{ fontFamily: DR.mono, fontSize: 7.5, color: DR.faint, letterSpacing: 0.8, fontWeight: 600, marginTop: 3 }}>{where}</div></div>
    <div style={{ display: 'flex', alignItems: 'center', gap: 9 }}><CAv who={who}/><div><div style={{ fontFamily: DR.serif, fontSize: 14.5, fontWeight: 500, color: DR.ink, letterSpacing: -0.1, lineHeight: 1.1 }}>{note}</div><div style={{ display: 'flex', alignItems: 'center', gap: 5, marginTop: 2 }}><CMI m="plane" s={10} c={DR.mute}/><span style={{ fontFamily: DR.mono, fontSize: 8.5, color: DR.mute }}>{code}</span></div></div></div>
  </div>;
}
function Leg({ from, to, m, detail, last }) {
  return <div style={{ display: 'grid', gridTemplateColumns: '16px 1fr', gap: 13, alignItems: 'flex-start', padding: '0 24px' }}>
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
      <div style={{ width: 28, height: 28, borderRadius: 999, background: DR.card, border: `0.5px solid ${DR.hair}`, display: 'flex', alignItems: 'center', justifyContent: 'center', marginLeft: -6 }}><CMI m={m} s={14}/></div>
      {!last && <span style={{ width: 1, flex: 1, minHeight: 18, background: DR.hairThin, marginLeft: -6 }}/>}
    </div>
    <div style={{ paddingBottom: 14, paddingTop: 3 }}><div style={{ fontFamily: DR.serif, fontSize: 15, fontWeight: 500, color: DR.ink, letterSpacing: -0.2 }}>{from} <span style={{ color: DR.faint }}>→</span> {to}</div><div style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 11.5, color: DR.mute, marginTop: 1 }}>{detail}</div></div>
  </div>;
}
function RentalCard() {
  return <div style={{ margin: '4px 22px 0', padding: '13px 15px', background: DR.card, borderRadius: 13, border: `0.5px solid ${DR.hair}` }}>
    <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 9 }}><CMI m="car" s={17} c={DR.ink}/><div><div style={{ fontFamily: DR.serif, fontSize: 15, fontWeight: 500, color: DR.ink, letterSpacing: -0.2 }}>Rental car</div><div style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 11, color: DR.mute, marginTop: 1 }}>Porto · May 22–24 · your name</div></div></div>
      <CAv who="T" s={20}/>
    </div>
    <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginTop: 9, paddingTop: 8, borderTop: `0.5px solid ${DR.hairThin}` }}><span style={{ fontFamily: DR.mono, fontSize: 8.5, color: DR.mute, letterSpacing: 0.8, fontWeight: 600 }}>€140 · SPLIT 3</span><span style={{ width: 3, height: 3, borderRadius: 3, background: DR.faint }}/><span style={{ fontSize: 11, color: DR.goldDeep, fontWeight: 600 }}>Pick-up at airport</span></div>
  </div>;
}
// Booked-status card — SCALES to any group size. A single proportion
// bar + overflowing avatar cluster + counts grouped by status (not one
// row per person). Reads the same for 3 travelers or 30.
function StatusCard({ booked = 7, oneway = 2, none = 1 }) {
  const total = booked + oneway + none;
  // demo avatar cluster (cap visible, overflow +N)
  const cluster = ['T', 'A', 'M', 'A', 'T'];
  const shown = cluster.slice(0, 4);
  const extra = total - shown.length;
  const pct = (n) => `${(n / total) * 100}%`;
  return (
    <div style={{ margin: '0 22px', padding: '15px 16px', background: DR.card, borderRadius: 14, border: `0.5px solid ${DR.hair}`, boxShadow: '0 1px 0 rgba(255,255,255,0.6) inset' }}>
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
        <div style={{ fontFamily: DR.serif, fontSize: 19, fontWeight: 500, color: DR.ink, letterSpacing: -0.3 }}>{booked} of {total} booked</div>
        <span style={{ fontSize: 11.5, color: DR.blue, fontWeight: 600 }}>By traveler →</span>
      </div>
      {/* single proportion bar — fills regardless of headcount */}
      <div style={{ display: 'flex', gap: 2, marginTop: 12, height: 6, borderRadius: 4, overflow: 'hidden' }}>
        <span style={{ width: pct(booked), background: '#3D7050' }}/>
        <span style={{ width: pct(oneway), background: DR.gold }}/>
        <span style={{ width: pct(none), background: 'rgba(27,23,20,0.10)' }}/>
      </div>
      {/* grouped counts + overflowing avatar cluster */}
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginTop: 12 }}>
        <div style={{ display: 'flex', gap: 13, fontSize: 10.5 }}>
          {[['#3D7050', `${booked} round trip`], [DR.goldDeep, `${oneway} one-way`], [DR.mute, `${none} not yet`]].map(([c, t]) => (
            <span key={t} style={{ display: 'flex', alignItems: 'center', gap: 5, color: DR.soft, fontWeight: 500 }}><span style={{ width: 7, height: 7, borderRadius: 7, background: c }}/>{t}</span>
          ))}
        </div>
        <div style={{ display: 'flex', alignItems: 'center' }}>
          {shown.map((w, i) => <span key={i} style={{ marginLeft: i ? -6 : 0 }}><CAv who={w} s={20} ring={DR.card}/></span>)}
          {extra > 0 && <span style={{ marginLeft: -6, width: 20, height: 20, borderRadius: 999, background: DR.cardSoft, border: `1.5px solid ${DR.card}`, display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: 8.5, fontWeight: 700, color: DR.mute }}>+{extra}</span>}
        </div>
      </div>
    </div>
  );
}

// A proper time-spine arrival — time runs down a left axis with a dot on
// a continuous rail; not anchored to a single date header.
function ArrSpine({ time, day, who, note, code, where, first, last }) {
  return (
    <div style={{ display: 'grid', gridTemplateColumns: '58px 1fr', gap: 14, padding: '0 24px' }}>
      <div style={{ position: 'relative', textAlign: 'right', paddingRight: 16 }}>
        <div style={{ fontFamily: DR.serif, fontSize: 16, fontWeight: 500, color: DR.ink, letterSpacing: -0.3, lineHeight: 1 }}>{time}</div>
        <div style={{ fontFamily: DR.mono, fontSize: 7.5, color: DR.faint, letterSpacing: 0.8, fontWeight: 600, marginTop: 3 }}>{day}</div>
        <span style={{ position: 'absolute', right: -5, top: 4, width: 9, height: 9, borderRadius: 999, background: DR.ink, zIndex: 1 }}/>
      </div>
      <div style={{ position: 'relative', paddingBottom: 16 }}>
        {!last && <span style={{ position: 'absolute', left: -16, top: 6, bottom: -6, width: 1, background: DR.hairThin }}/>}
        <div style={{ display: 'flex', alignItems: 'center', gap: 9 }}>
          <CAv who={who}/>
          <div><div style={{ fontFamily: DR.serif, fontSize: 14.5, fontWeight: 500, color: DR.ink, letterSpacing: -0.1, lineHeight: 1.1 }}>{note}</div>
          <div style={{ display: 'flex', alignItems: 'center', gap: 5, marginTop: 2 }}><CMI m="plane" s={10} c={DR.mute}/><span style={{ fontFamily: DR.mono, fontSize: 8.5, color: DR.mute }}>{code} · {where}</span></div></div>
        </div>
      </div>
    </div>
  );
}

// ─── COMBO A · STATUS-FIRST — scalable booked card, arrive + depart spines ───
function TransComboA() {
  return (
    <CFrame>
      <CHead sub="seven of ten sorted"/>
      <div style={{ padding: '4px 0 18px' }}><StatusCard/></div>
      <ZL note="who lands when">GETTING THERE</ZL>
      <ArrSpine first time="14:20" day="MON 18" who="T" note="You land first" code="TP 204" where="JFK"/>
      <ArrSpine time="16:05" day="MON 18" who="A" note="Ana, 2 hrs after" code="TP 1018" where="CDG"/>
      <ArrSpine last time="09:30" day="TUE 19" who="M" note="Mara, a day late" code="TP 442" where="LHR"/>
      <div style={{ height: 16 }}/>
      <ZL note="who leaves when">HEADING HOME</ZL>
      <ArrSpine first time="11:40" day="SAT 24" who="A" note="Ana, early flight" code="TP 1019" where="→ CDG"/>
      <ArrSpine last time="18:55" day="SAT 24" who="T" note="You + Mara, together" code="TP 205" where="→ JFK"/>
      <div style={{ height: 16 }}/>
      <ZL note="the trip’s legs">BETWEEN CITIES</ZL>
      <Leg from="Lisbon" to="Sintra" m="train" detail="May 21 · day trip"/>
      <Leg from="Lisbon" to="Porto" m="train" detail="May 22 · all three" last/>
      <RentalCard/>
    </CFrame>
  );
}

// ─── COMBO B · TIMELINE-FIRST — one chronological spine, all modes ───
function TransComboB() {
  return (
    <CFrame>
      <CHead sub="the whole journey, in order"/>
      <ZL note="depart → return">THE JOURNEY</ZL>
      <Leg from="JFK" to="Lisbon" m="plane" detail="May 18 · you 14:20, Ana 16:05"/>
      <Leg from="airport" to="Alfama" m="cab" detail="May 18 · shared, you + Ana"/>
      <Leg from="Lisbon" to="Sintra" m="train" detail="May 21 · day trip, 40 min"/>
      <Leg from="Lisbon" to="Porto" m="train" detail="May 22 · all three, 3 hr"/>
      <Leg from="Porto" to="JFK" m="plane" detail="May 24 · return" last/>
      <div style={{ height: 6 }}/>
      <RentalCard/>
      <div style={{ height: 16 }}/>
      <VLine>Mara joins a day late — I left her Sintra seat open.</VLine>
    </CFrame>
  );
}

// ─── COMBO C · PER-PERSON — each traveler's full journey grouped ───
function PersonBlock({ who, name, lines, st }) {
  return (
    <div style={{ margin: '0 22px 10px', padding: '13px 15px', background: DR.card, borderRadius: 13, border: `0.5px solid ${DR.hair}` }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 9, marginBottom: 9 }}>
        <CAv who={who} s={24} ring={DR.card}/>
        <span style={{ fontFamily: DR.serif, fontSize: 16, fontWeight: 500, color: DR.ink, letterSpacing: -0.2, flex: 1 }}>{name}</span>
        <span style={{ width: 8, height: 8, borderRadius: 8, background: st === 'done' ? '#3D7050' : st === 'partial' ? DR.gold : DR.faint }}/>
      </div>
      {lines.map(([m, t], i) => (
        <div key={i} style={{ display: 'flex', alignItems: 'center', gap: 9, padding: '5px 0', borderTop: i ? `0.5px solid ${DR.hairThin}` : 'none' }}>
          <CMI m={m} s={13} c={DR.mute}/><span style={{ fontFamily: DR.serif, fontSize: 13.5, color: DR.soft, letterSpacing: -0.1 }}>{t}</span>
        </div>
      ))}
    </div>
  );
}
function TransComboC() {
  return (
    <CFrame>
      <CHead sub="each of you, end to end"/>
      <ZL note="tap to see a journey">BY TRAVELER</ZL>
      <PersonBlock who="T" name="You" st="done" lines={[['plane', 'JFK → Lisbon · May 18, 14:20'], ['train', 'Sintra + Porto, with the group'], ['plane', 'Porto → JFK · May 24']]}/>
      <PersonBlock who="A" name="Ana" st="partial" lines={[['plane', 'CDG → Lisbon · May 18, 16:05'], ['train', 'Sintra + Porto, with the group'], ['plane', 'return open']]}/>
      <PersonBlock who="M" name="Mara" st="none" lines={[['plane', 'LHR → Lisbon · May 19, a day late'], ['plane', 'nothing else booked']]}/>
      <VLine>Mara’s fares jump after this week — want me to hold her flights?</VLine>
    </CFrame>
  );
}

Object.assign(window, { TransComboA, TransComboB, TransComboC });
