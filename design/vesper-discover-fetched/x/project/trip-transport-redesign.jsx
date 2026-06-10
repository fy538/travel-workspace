// ═══════════════════════════════════════════════════════════════
// TRANSPORT · redesigned — same itinerary spine language as Stay.
// Owns: getting-there (per-person arrivals/departures), inter-city legs,
// and the rental car (a date-range object like a stay). NO photos.
// Three zones, adaptive. Reuses DR + Phone/TabBar + SPEEP/SAv.
// ═══════════════════════════════════════════════════════════════

function TAv({ who, s = 18, ring = '#EFEAE0' }) {
  return <div style={{ width: s, height: s, borderRadius: 999, background: SPEEP[who], color: '#fff', fontFamily: DR.serif, fontSize: s * 0.46, fontWeight: 500, display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0, border: `1.5px solid ${ring}` }}>{who}</div>;
}
const tsk = (s = 11, c = DR.gold) => <svg width={s} height={s} viewBox="0 0 24 24" fill={c}><path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z"/></svg>;
const MODE = {
  plane: <path d="M2 12l20-7-7 20-3-9-10-4z"/>,
  train: <><rect x="6" y="4" width="12" height="13" rx="3"/><path d="M6 11h12M9 20l-2 2M15 20l2 2"/></>,
  car: <><rect x="3" y="11" width="18" height="6" rx="2"/><circle cx="7" cy="18" r="1.5"/><circle cx="17" cy="18" r="1.5"/><path d="M5 11l2-4h10l2 4"/></>,
  cab: <><rect x="3" y="11" width="18" height="6" rx="2"/><circle cx="7" cy="18" r="1.5"/><circle cx="17" cy="18" r="1.5"/><path d="M9 7h6v4H9z"/></>,
};
function MIcon({ m, s = 15, c = DR.soft }) { return <svg width={s} height={s} viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round">{MODE[m]}</svg>; }

function THead() {
  return (
    <div style={{ padding: '12px 24px 16px' }}>
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
        <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke={DR.soft} strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><path d="M14 6l-6 6 6 6"/></svg>
        <span style={{ fontSize: 9.5, letterSpacing: 2, color: DR.mute, fontWeight: 700 }}>TRANSPORT</span>
        <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke={DR.soft} strokeWidth="1.6" strokeLinecap="round"><path d="M12 5v14M5 12h14"/></svg>
      </div>
      <h1 style={{ fontFamily: DR.serif, fontSize: 28, fontWeight: 500, letterSpacing: -0.6, lineHeight: 1, color: DR.ink, margin: '14px 0 0' }}>How you travel</h1>
    </div>
  );
}
function ZoneLabel({ children, note }) {
  return (
    <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', padding: '4px 0 10px' }}>
      <span style={{ fontSize: 9, letterSpacing: 1.8, color: DR.mute, fontWeight: 700 }}>{children}</span>
      {note && <span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 11.5, color: DR.faint }}>{note}</span>}
    </div>
  );
}

// Zone 1 — per-person arrivals on the spine
function ArrivalRow({ who, when, mode, code, note, first }) {
  return (
    <div style={{ display: 'grid', gridTemplateColumns: '54px 1fr auto', gap: 13, padding: '12px 0', borderTop: first ? 'none' : `0.5px solid ${DR.hairThin}`, alignItems: 'center' }}>
      <div style={{ textAlign: 'right' }}>
        <div style={{ fontFamily: DR.serif, fontSize: 16, fontWeight: 500, color: DR.ink, letterSpacing: -0.3, lineHeight: 1 }}>{when[1]}</div>
        <div style={{ fontFamily: DR.mono, fontSize: 7.5, color: DR.faint, letterSpacing: 0.8, fontWeight: 600, marginTop: 3 }}>{when[0]}</div>
      </div>
      <div style={{ display: 'flex', alignItems: 'center', gap: 9, minWidth: 0 }}>
        <TAv who={who}/>
        <div style={{ minWidth: 0 }}>
          <div style={{ fontFamily: DR.serif, fontSize: 14.5, fontWeight: 500, color: DR.ink, letterSpacing: -0.1, lineHeight: 1.1 }}>{note}</div>
          <div style={{ display: 'flex', alignItems: 'center', gap: 5, marginTop: 2 }}><MIcon m={mode} s={11} c={DR.mute}/><span style={{ fontFamily: DR.mono, fontSize: 8.5, color: DR.mute, letterSpacing: 0.5 }}>{code}</span></div>
        </div>
      </div>
    </div>
  );
}

// Zone 2 — inter-city leg connector
function LegRow({ from, to, mode, detail, who, last }) {
  return (
    <div style={{ display: 'grid', gridTemplateColumns: '16px 1fr', gap: 13, alignItems: 'flex-start' }}>
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
        <div style={{ width: 30, height: 30, borderRadius: 999, background: DR.card, border: `0.5px solid ${DR.hair}`, display: 'flex', alignItems: 'center', justifyContent: 'center', marginLeft: -7 }}><MIcon m={mode}/></div>
        {!last && <span style={{ width: 1, flex: 1, minHeight: 22, background: DR.hairThin, marginLeft: -7 }}/>}
      </div>
      <div style={{ paddingBottom: 18, paddingTop: 4 }}>
        <div style={{ fontFamily: DR.serif, fontSize: 15.5, fontWeight: 500, color: DR.ink, letterSpacing: -0.2 }}>{from} <span style={{ color: DR.faint }}>→</span> {to}</div>
        <div style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 11.5, color: DR.mute, marginTop: 2 }}>{detail}</div>
      </div>
    </div>
  );
}

// V1 · getting there — per-person arrivals + return, with a Vesper timing read
function TransNew1() {
  return (
    <Phone bg={DR.paper}><div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
      <THead/>
      <div style={{ padding: '0 22px' }}>
        <ZoneLabel note="who lands when">GETTING THERE · MAY 18</ZoneLabel>
        <ArrivalRow first who="T" when={['JFK','14:20']} mode="plane" code="TP 204" note="You land first"/>
        <ArrivalRow who="A" when={['CDG','16:05']} mode="plane" code="TP 1018" note="Ana, 2 hrs after you"/>
        <ArrivalRow who="M" when={['LHR','MAY 19']} mode="plane" code="TP 442" note="Mara, a day late"/>
        <div style={{ marginTop: 12, paddingLeft: 13, borderLeft: `2px solid ${DR.gold}` }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 6, marginBottom: 4 }}>{tsk(11)}<span style={{ fontSize: 8.5, letterSpacing: 1.4, color: DR.goldDeep, fontWeight: 700 }}>VESPER</span></div>
          <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 14, color: DR.ink, margin: 0, lineHeight: 1.4, letterSpacing: -0.1 }}>You and Ana land 2 hrs apart — share a cab into Alfama?</p>
        </div>
      </div>
    </div><TabBar active="trips"/></Phone>
  );
}

// V2 · inter-city + rental car (the rental is a date-range object)
function TransNew2() {
  return (
    <Phone bg={DR.paper}><div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
      <THead/>
      <div style={{ padding: '0 22px' }}>
        <ZoneLabel note="the trip's legs">BETWEEN CITIES</ZoneLabel>
        <LegRow from="JFK" to="Lisbon" mode="plane" detail="May 18 · you + Ana"/>
        <LegRow from="Lisbon" to="Sintra" mode="train" detail="May 21 · day trip, 40 min"/>
        <LegRow from="Lisbon" to="Porto" mode="train" detail="May 22 · all three, 3 hr" last/>
        {/* rental car — a date-range object */}
        <div style={{ marginTop: 8, padding: '13px 15px', background: DR.card, borderRadius: 13, border: `0.5px solid ${DR.hair}` }}>
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: 9 }}><MIcon m="car" s={17} c={DR.ink}/><div><div style={{ fontFamily: DR.serif, fontSize: 15.5, fontWeight: 500, color: DR.ink, letterSpacing: -0.2 }}>Rental car</div><div style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 11.5, color: DR.mute, marginTop: 1 }}>Porto · May 22–24 · under your name</div></div></div>
            <TAv who="T" s={20}/>
          </div>
          <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginTop: 10, paddingTop: 9, borderTop: `0.5px solid ${DR.hairThin}` }}>
            <span style={{ fontFamily: DR.mono, fontSize: 8.5, color: DR.mute, letterSpacing: 0.8, fontWeight: 600 }}>€140 · SPLIT 3</span>
            <span style={{ width: 3, height: 3, borderRadius: 3, background: DR.faint }}/>
            <span style={{ fontSize: 11, color: DR.goldDeep, fontWeight: 600 }}>Pick-up at airport</span>
          </div>
        </div>
      </div>
    </div><TabBar active="trips"/></Phone>
  );
}

// V3 · who's-sorted status (booked vs not, per person)
function TransNew3() {
  const ppl = [['T', 'You', 'Round trip booked', 'done'], ['A', 'Ana', 'Outbound booked · return open', 'partial'], ['M', 'Mara', 'Nothing booked yet', 'none']];
  return (
    <Phone bg={DR.paper}><div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
      <THead/>
      <div style={{ padding: '0 22px' }}>
        <ZoneLabel note="is everyone sorted?">STATUS</ZoneLabel>
        {ppl.map(([w, name, status, st], i) => (
          <div key={w} style={{ display: 'flex', alignItems: 'center', gap: 12, padding: '13px 0', borderTop: i ? `0.5px solid ${DR.hairThin}` : 'none' }}>
            <TAv who={w} s={28}/>
            <div style={{ flex: 1 }}><div style={{ fontFamily: DR.serif, fontSize: 16, fontWeight: 500, color: DR.ink, letterSpacing: -0.2 }}>{name}</div><div style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 12, color: st === 'none' ? DR.goldDeep : DR.mute, marginTop: 2 }}>{status}</div></div>
            <span style={{ width: 9, height: 9, borderRadius: 9, background: st === 'done' ? '#3D7050' : st === 'partial' ? DR.gold : DR.faint }}/>
          </div>
        ))}
        <div style={{ marginTop: 12, paddingLeft: 13, borderLeft: `2px solid ${DR.gold}` }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 6, marginBottom: 4 }}>{tsk(11)}<span style={{ fontSize: 8.5, letterSpacing: 1.4, color: DR.goldDeep, fontWeight: 700 }}>VESPER</span></div>
          <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 14, color: DR.ink, margin: 0, lineHeight: 1.4, letterSpacing: -0.1 }}>Mara’s fares jump after this week — want me to hold her flight?</p>
        </div>
      </div>
    </div><TabBar active="trips"/></Phone>
  );
}

// V4 · tap a leg → popover (over a dimmed transport page)
function TransNewTap() {
  return (
    <Phone bg={DR.paper}><div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
      <THead/>
      <div style={{ padding: '0 22px' }}>
        <ZoneLabel note="who lands when">GETTING THERE · MAY 18</ZoneLabel>
        <ArrivalRow first who="T" when={['JFK','14:20']} mode="plane" code="TP 204" note="You land first"/>
        <ArrivalRow who="A" when={['CDG','16:05']} mode="plane" code="TP 1018" note="Ana, 2 hrs after you"/>
      </div>
      <div style={{ position: 'absolute', inset: 0, background: 'rgba(20,14,9,0.34)' }}/>
      <div style={{ position: 'absolute', left: 20, right: 20, top: 220 }}>
        <div style={{ background: DR.card, borderRadius: 16, border: `0.5px solid ${DR.hair}`, overflow: 'hidden', boxShadow: '0 22px 48px -16px rgba(0,0,0,0.4)' }}>
          {/* boarding-pass style header */}
          <div style={{ padding: '14px 16px', borderBottom: `1px dashed ${DR.faint}`, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
            <div><div style={{ fontFamily: DR.serif, fontSize: 26, fontWeight: 500, color: DR.ink, letterSpacing: -0.5 }}>JFK</div><div style={{ fontFamily: DR.mono, fontSize: 8.5, color: DR.mute }}>14:20</div></div>
            <MIcon m="plane" s={18} c={DR.gold}/>
            <div style={{ textAlign: 'right' }}><div style={{ fontFamily: DR.serif, fontSize: 26, fontWeight: 500, color: DR.ink, letterSpacing: -0.5 }}>LIS</div><div style={{ fontFamily: DR.mono, fontSize: 8.5, color: DR.mute }}>02:25 +1</div></div>
          </div>
          {[['change', 'Ask Vesper to change', DR.goldDeep, true], ['seat', 'Change seat · 14C', DR.soft], ['share', 'Share a cab with Ana', DR.soft]].map(([k, l, c, first]) => (
            <div key={k} style={{ display: 'flex', alignItems: 'center', gap: 10, padding: '12px 16px', borderTop: first ? 'none' : `0.5px solid ${DR.hairThin}` }}>
              {first && tsk(13)}
              <span style={{ fontFamily: first ? DR.serif : DR.sans, fontStyle: first ? 'italic' : 'normal', fontSize: first ? 14.5 : 13.5, fontWeight: first ? 400 : 500, color: c, letterSpacing: -0.1 }}>{l}</span>
            </div>
          ))}
          <div style={{ padding: '12px 16px', borderTop: `0.5px solid ${DR.hairThin}`, display: 'flex', justifyContent: 'space-between' }}>
            <span style={{ fontSize: 13, color: DR.blue, fontWeight: 600 }}>See ticket →</span>
            <span style={{ fontSize: 13.5, color: '#A04030', fontWeight: 500 }}>Remove</span>
          </div>
        </div>
      </div>
    </div><TabBar active="trips"/></Phone>
  );
}

Object.assign(window, { TransNew1, TransNew2, TransNew3, TransNewTap });
