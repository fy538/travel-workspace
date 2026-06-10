// + CREATE TRIP page + NOTIFICATIONS page.
// The + glyph on every Trips screen opens TripsCreate; the bell opens
// TripsNotifications. Both kept spare and editorial — one clear path,
// hairline rows, Vesper's voice as the texture (not badges).

// compact shape glyphs for the Create carousel
function ShapeIcon({ k }) {
  const P = {
    City: 'M4 21V9l5-3v15M9 21V12l6-3v12M15 21V13l5 2v6M3 21h18',
    Beach: 'M3 18q4.5-3 9 0t9 0',
    Mountain: 'M3 19l6-11 4 6 2-3 6 8z',
    Road: 'M9 21L11 3M15 21L13 3M4 21h16',
    Festival: 'M12 3l2 5 5 .5-4 3.5 1.5 5L12 14l-4.5 3 1.5-5L5 8.5 10 8z',
    Quiet: 'M20 14a8 8 0 1 1-9-10 6 6 0 0 0 9 10z',
  };
  return (
    <svg width="20" height="20" viewBox="0 0 24 24" fill={k === 'Beach' && false ? T.gold : 'none'} stroke={T.inkSoft} strokeWidth="1.4" strokeLinecap="round" strokeLinejoin="round">
      {k === 'Beach' && <circle cx="12" cy="8" r="3.2"/>}
      <path d={P[k]}/>
    </svg>
  );
}

function TripsCreate() {
  return (
    <Phone bg={T.bg}>
      {/* full page — back chevron top-left */}
      <div style={{ padding: '14px 22px 0' }}>
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke={T.inkSoft} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><path d="M14 6l-6 6 6 6"/></svg>
      </div>
      <div style={{ padding: '22px 22px 0' }}>
        <h1 style={{ fontFamily: T.serif, fontWeight: 500, fontSize: 40, letterSpacing: -1.1, lineHeight: 0.96, color: T.ink, margin: 0 }}>Begin a <span style={{ fontStyle: 'italic' }}>trip.</span></h1>
        <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 15, color: T.mute, lineHeight: 1.4, margin: '12px 0 0' }}>However you like to start — talk it through, a blank page, or a shape to riff on.</p>
      </div>
      <div style={{ padding: '24px 22px 0' }}>

        {/* the two real doors — horizontal pair */}
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 10, marginTop: 16 }}>
          <div style={{ padding: '15px 14px', background: T.cardWarm, borderRadius: 15, border: `0.8px solid ${T.gold}` }}>
            <TripIcons.Sparkle s={15}/>
            <div style={{ fontFamily: T.mono, fontSize: 8, letterSpacing: 1.4, color: T.goldDeep, fontWeight: 700, marginTop: 8 }}>RECOMMENDED</div>
            <div style={{ fontFamily: T.serif, fontSize: 19, fontWeight: 500, color: T.ink, letterSpacing: -0.3, lineHeight: 1.05, marginTop: 5 }}>Talk it through</div>
            <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12, color: T.mute, marginTop: 5, lineHeight: 1.35 }}>a place, a season — Vesper builds the shape.</div>
          </div>
          <div style={{ padding: '15px 14px', background: T.cardSoft, borderRadius: 15, border: `0.5px solid ${T.hairline}` }}>
            <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke={TR.ink} strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"><rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 9h6M9 13h6M9 17h3"/></svg>
            <div style={{ fontFamily: T.mono, fontSize: 8, letterSpacing: 1.4, color: T.mute, fontWeight: 700, marginTop: 8 }}>BLANK PAGE</div>
            <div style={{ fontFamily: T.serif, fontSize: 19, fontWeight: 500, color: T.ink, letterSpacing: -0.3, lineHeight: 1.05, marginTop: 5 }}>Start blank</div>
            <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12, color: T.mute, marginTop: 5, lineHeight: 1.35 }}>just a title — the home fills in as you go.</div>
          </div>
        </div>

        {/* footer — shapes + Discover, one quiet line */}
        <div style={{ paddingTop: 13, marginTop: 14, borderTop: `0.5px solid ${T.hairThin}` }}>
          <span style={{ fontFamily: T.mono, fontSize: 8.5, color: T.muteSoft, letterSpacing: 1.4, fontWeight: 600 }}>OR PICK A SHAPE TO START FROM</span>
          <div style={{ display: 'flex', gap: 8, overflowX: 'auto', margin: '10px -22px 0', padding: '0 22px 2px' }}>
            {[
              ['City', 'close, electric'],
              ['Beach', 'slow, warm'],
              ['Mountain', 'crisp, high'],
              ['Road', 'open-ended'],
              ['Festival', 'loud, alive'],
              ['Quiet', 'nothing planned'],
            ].map(([t, d]) => (
              <div key={t} style={{ width: 122, flexShrink: 0, padding: '11px 13px', background: T.cardWarm, borderRadius: 12, border: `0.5px solid ${T.hairline}` }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: 7 }}>
                  <ShapeIcon k={t}/>
                  <span style={{ fontFamily: T.serif, fontSize: 15, fontWeight: 500, color: T.ink, letterSpacing: -0.2 }}>{t}</span>
                </div>
                <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 10.5, color: T.mute, marginTop: 5 }}>{d}</div>
              </div>
            ))}
          </div>
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginTop: 12, paddingTop: 12, borderTop: `0.5px solid ${T.hairThin}` }}>
            <span style={{ fontFamily: T.serif, fontSize: 13.5, color: T.ink, letterSpacing: -0.1 }}>Build from <b style={{ fontWeight: 600 }}>12 places</b> saved in Discover</span>
            <Marks.ArrowR s={13} c={T.goldDeep}/>
          </div>
        </div>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

function TripsNotifications() {
  return (
    <Phone bg={T.bg}>
      {/* Header */}
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '14px 22px 0' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke={T.inkSoft} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><path d="M14 6l-6 6 6 6"/></svg>
          <span style={{ fontSize: 13, color: T.inkSoft, fontWeight: 500 }}>Trips</span>
        </div>
        <span style={{ fontSize: 10.5, color: T.mute, letterSpacing: 2, fontWeight: 600 }}>UPDATES</span>
        <span style={{ fontFamily: T.serif, fontSize: 12.5, color: T.mute }}>Mark all</span>
      </div>

      {/* Title */}
      <div style={{ padding: '20px 24px 0' }}>
        <h1 style={{ fontFamily: T.serif, fontWeight: 500, fontSize: 31, lineHeight: 0.98, letterSpacing: -0.8, color: T.ink, margin: 0 }}>
          What changed, <span style={{ fontStyle: 'italic' }}>since you looked.</span>
        </h1>
      </div>

      <NotifSection label="LIVE · TOKYO" kicker="day 3 of 8">
        <NotifRow when="now" title="Cherry blossoms peaked overnight" sub="Yoyogi is at 90% bloom — a 12-minute walk." source="Vesper"/>
        <NotifRow when="2h" title="Ana added a dinner pin" sub="“Den” — Wed 19:30, two seats." source="Ana"/>
      </NotifSection>

      <NotifSection label="PLANNING · 2 TRIPS" kicker="3 waiting">
        <NotifRow when="this morning" title="Vesper drafted three ryokans for Tokyo" sub="kept the quiet ones, dropped the chain." source="Vesper"/>
        <NotifRow when="yesterday" title="Ana said yes to Porto" sub="picked the week of Jun 6–13." source="Ana"/>
        <NotifRow when="mar 12" title="Two friends are interested in the beach week" sub="a vote is open — your call." source="Group"/>
      </NotifSection>

      <NotifSection label="RETURNED · LISBON" kicker="2 days ago">
        <NotifRow when="mar 14" title="A postcard is on your desk" sub="“Lisbon, the slow way” — keep it, or refine?" source="Vesper" golden/>
        <NotifRow when="mar 13" title="41 entries kept in Atlas" sub="six places, three rituals, two patterns." source="Atlas"/>
      </NotifSection>

      <TabBar active="trips"/>
    </Phone>
  );
}

function NotifSection({ label, kicker, children }) {
  return (
    <div style={{ padding: '20px 24px 0' }}>
      <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', marginBottom: 2 }}>
        <span style={{ fontFamily: T.mono, fontSize: 9, color: T.mute, letterSpacing: 1.8, fontWeight: 700 }}>{label}</span>
        <span style={{ fontFamily: T.serif, fontSize: 11.5, color: T.muteSoft }}>{kicker}</span>
      </div>
      {children}
    </div>
  );
}

function NotifRow({ when, title, sub, source, golden }) {
  const { useState } = React;
  const [read, setRead] = useState(false);
  const dot = (bg) => ({ width: 30, height: 30, borderRadius: 999, background: bg, border: `0.5px solid ${T.hairline}`, display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0 });
  let Icon;
  if (source === 'Vesper') Icon = <span style={dot('rgba(176,133,58,0.12)')}><TripIcons.Sparkle s={14} c={T.goldDeep}/></span>;
  else if (source === 'Atlas') Icon = <span style={dot(T.cardSoft)}><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke={T.goldDeep} strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"><rect x="3.5" y="6.5" width="17" height="11" rx="1.6"/><rect x="14.3" y="9" width="3.7" height="3.2" rx="0.5"/><path d="M6.5 10h5M6.5 13.5h7"/></svg></span>;
  else if (source === 'Group') Icon = <span style={dot(T.cardSoft)}><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke={T.inkSoft} strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"><circle cx="8.5" cy="9" r="2.6"/><circle cx="15.5" cy="9" r="2.6"/><path d="M4 18c0-2.5 2-4 4.5-4s4.5 1.5 4.5 4M13.2 17.4c.4-2 2-3.1 3.8-2.9"/></svg></span>;
  else Icon = <span style={{ width: 30, height: 30, borderRadius: 999, background: '#A0703A', color: '#fff', display: 'flex', alignItems: 'center', justifyContent: 'center', fontFamily: T.serif, fontSize: 13, fontWeight: 500, flexShrink: 0 }}>{source[0]}</span>;
  return (
    <div onClick={() => setRead(true)} style={{ cursor: 'pointer', display: 'grid', gridTemplateColumns: '30px 1fr auto', gap: 12, alignItems: 'center', padding: '13px 0', borderTop: `0.5px solid ${T.hairThin}`, opacity: read ? 0.45 : 1 }}>
      {Icon}
      <div style={{ minWidth: 0 }}>
        <div style={{ display: 'flex', alignItems: 'baseline', gap: 7 }}>
          {golden && <span style={{ width: 5, height: 5, borderRadius: 5, background: T.gold, flexShrink: 0 }}/>}
          <span style={{ fontFamily: T.serif, fontSize: 15, color: T.ink, fontWeight: 500, letterSpacing: -0.2, lineHeight: 1.2 }}>{title}</span>
        </div>
        <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12.5, color: T.mute, marginTop: 3, lineHeight: 1.3 }}>{sub}</div>
        <div style={{ fontFamily: T.mono, fontSize: 8.5, color: T.muteSoft, letterSpacing: 1.2, fontWeight: 600, marginTop: 5 }}>{source.toUpperCase()} · {when.toUpperCase()}</div>
      </div>
      {read ? <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#3D7050" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round"><path d="M4 12l5 5L20 6"/></svg> : <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke={golden ? T.goldDeep : T.muteSoft} strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d="M9 6l6 6-6 6"/></svg>}
    </div>
  );
}

// ─── ALL TRIPS · the full index (a destination, not a home state) ──
// Home = "what's alive now"; this = the complete shelf. Atlas owns
// the past, so this lists Planning (dated) + Dreaming (drafts) and
// hands the past off to Atlas.
function TripsIndex() {
  const Row = ({ title, meta, who, scene, tag, tagC, faint, last }) => (
    <div style={{ display: 'flex', gap: 13, alignItems: 'center', padding: '13px 0', borderTop: `0.5px solid ${T.hairThin}`, borderBottom: last ? `0.5px solid ${T.hairThin}` : 'none' }}>
      <div style={{ width: 56, height: 42, borderRadius: 8, overflow: 'hidden', flexShrink: 0, opacity: faint ? 0.55 : 1, background: T.cardSoft, border: `0.5px solid ${T.hairline}` }}>
        {scene && <PostcardScene scene={scene}/>}
      </div>
      <div style={{ flex: 1, minWidth: 0 }}>
        <div style={{ display: 'flex', alignItems: 'baseline', gap: 8 }}>
          <span style={{ fontFamily: T.serif, fontSize: 18, fontWeight: 500, color: T.ink, letterSpacing: -0.3, lineHeight: 1.1 }}>{title}</span>
          {tag && <span style={{ fontFamily: T.mono, fontSize: 8, letterSpacing: 1.2, color: tagC, fontWeight: 700 }}>{tag}</span>}
        </div>
        <div style={{ fontFamily: T.serif, fontSize: 12.5, color: T.mute, marginTop: 2 }}>{meta}</div>
        {who && <div style={{ fontFamily: T.mono, fontSize: 8, letterSpacing: 1, color: T.muteSoft, fontWeight: 600, marginTop: 4 }}>{who}</div>}
      </div>
      <Marks.ArrowR s={13} c={T.faint}/>
    </div>
  );
  const Group = ({ label, count, children }) => (
    <div style={{ padding: '22px 24px 0' }}>
      <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', marginBottom: 4 }}>
        <span style={{ fontFamily: T.mono, fontSize: 9, color: T.mute, letterSpacing: 1.8, fontWeight: 700 }}>{label}</span>
        <span style={{ fontFamily: T.mono, fontSize: 8.5, color: T.muteSoft, letterSpacing: 1.4, fontWeight: 600 }}>{count}</span>
      </div>
      {children}
    </div>
  );
  return (
    <Phone bg={T.bg}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 6, padding: '14px 22px 0', color: T.inkSoft }}>
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke={T.inkSoft} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><path d="M14 6l-6 6 6 6"/></svg>
        <span style={{ fontSize: 13, fontWeight: 500 }}>Trips</span>
      </div>
      <div style={{ padding: '18px 24px 0' }}>
        <h1 style={{ fontFamily: T.serif, fontWeight: 500, fontSize: 34, letterSpacing: -1, color: T.ink, margin: 0 }}>All trips.</h1>
        <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13, color: T.mute, marginTop: 5 }}>Two in motion, three still dreaming — and five kept behind you.</div>
      </div>

      <Group label="PLANNING" count="2 DATED">
        <Row scene="tokyo" title="Tokyo, in May" meta="Sat 14 → Fri 22 · 58 days out" who="YOU + ANA · 8 NIGHTS" tag="ALIVE" tagC={TR.ink}/>
        <Row scene="porto" title="Porto, return" meta="September · pencilled in" who="JUST YOU" tag="PENCILLED" tagC={T.goldDeep} last/>
      </Group>

      <Group label="DREAMING" count="3 DRAFTS">
        <Row title="A weekend somewhere quiet" meta="no dates · just you" faint/>
        <Row scene="lisbon" title="Lisbon, in spring" meta="from a dream-seed · food-led" faint/>
        <Row scene="tokyo" title="Tokyo, when the leaves turn" meta="from a dream-seed · a week" faint last/>
      </Group>

      {/* the past hands off to Atlas */}
      <div style={{ position: 'absolute', left: 24, right: 24, bottom: 104 }}>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '14px 16px', background: T.cardWarm, borderRadius: 13, border: `0.5px solid ${T.hairline}` }}>
          <div>
            <div style={{ fontFamily: T.mono, fontSize: 8.5, color: T.goldDeep, letterSpacing: 1.4, fontWeight: 700 }}>PAST TRIPS</div>
            <div style={{ fontFamily: T.serif, fontSize: 15.5, color: T.ink, marginTop: 3, letterSpacing: -0.2 }}>Lisbon & 4 more live in <span style={{ fontStyle: 'italic' }}>Atlas</span></div>
          </div>
          <Marks.ArrowR s={15} c={T.goldDeep}/>
        </div>
      </div>

      <TabBar active="trips"/>
    </Phone>
  );
}

Object.assign(window, { TripsCreate, TripsNotifications, TripsIndex });
