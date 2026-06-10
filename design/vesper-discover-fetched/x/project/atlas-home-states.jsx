// ═══════════════════════════════════════════════════════════════
// ATLAS HOME — the other states. The letter in Vesper's voice is the
// spine; in most states the hero is still that letter, it just has
// more (or different) to say. Never manufactures activity or nags.
// Reuses AtlasFrame, UtilHeader, Monogram, YearRibbonH, Postcard,
// ArtifactCard, Eyebrow, TabBar, Marks, T.
// ═══════════════════════════════════════════════════════════════

const sHair = `0.5px solid ${T.hairline}`;

// the asymmetric four-room shelf, parameterized
function ShelfRooms({ rooms, label = 'THE SHELF', right = 'FOUR ROOMS' }) {
  return (
    <div>
      <div style={{ margin: '40px 22px 12px', display: 'flex', alignItems: 'baseline', justifyContent: 'space-between' }}>
        <Eyebrow>{label}</Eyebrow>
        <span style={{ color: T.muteSoft, fontSize: 9.5, letterSpacing: 1.5, fontWeight: 600 }}>{right}</span>
      </div>
      <div style={{ margin: '0 16px', display: 'grid', gridTemplateColumns: '1.15fr 1fr', gap: 10 }}>
        <ArtifactCard mark={<Marks.Inbox size={66}/>} eyebrow={rooms[0].e} title={rooms[0].t} tail={rooms[0].s} accent={rooms[0].accent} tall heightOverride={172}/>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
          <ArtifactCard mark={<Marks.Map size={50}/>} eyebrow={rooms[1].e} title={rooms[1].t} tail={rooms[1].s} compact heightOverride={81}/>
          <ArtifactCard mark={<Marks.DNA size={50}/>} eyebrow={rooms[2].e} title={rooms[2].t} tail={rooms[2].s} compact heightOverride={81}/>
        </div>
      </div>
      <div style={{ margin: '10px 16px 0' }}>
        <ArtifactCard mark={<Marks.Postcard size={50}/>} eyebrow={rooms[3].e} title={rooms[3].t} tail={rooms[3].s} accent={rooms[3].accent} wide heightOverride={70}/>
      </div>
    </div>
  );
}

// rooms reduced to a quiet drawer (active-trip state)
function RoomsThin() {
  return (
    <div style={{ margin: '36px 22px 0', paddingTop: 16, borderTop: sHair, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
      {['Inbox', 'Map', 'DNA', 'Postcards'].map((r, i) => (
        <React.Fragment key={r}>
          <span style={{ fontFamily: T.serif, fontSize: 14, color: T.mute, letterSpacing: -0.1 }}>{r}</span>
          {i < 3 && <span style={{ color: T.muteSoft, fontSize: 10 }}>·</span>}
        </React.Fragment>
      ))}
    </div>
  );
}

function HeroLetter({ eyebrow, ec = T.goldDeep, salutation, children, cta }) {
  return (
    <div style={{ padding: '34px 24px 0' }}>
      <div style={{ marginBottom: salutation ? 9 : 15 }}><Eyebrow color={ec}>{eyebrow}</Eyebrow></div>
      {salutation && <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 17, color: T.goldDeep, marginBottom: 12 }}>{salutation}</div>}
      <p style={{ fontFamily: T.serif, fontSize: 26, fontWeight: 500, color: T.ink, lineHeight: 1.34, letterSpacing: -0.4, margin: 0 }}>{children}</p>
      {cta && <div style={{ marginTop: 16, display: 'inline-flex', alignItems: 'center', gap: 7 }}><span style={{ fontFamily: T.sans, fontSize: 13.5, fontWeight: 600, color: ec }}>{cta}</span><span style={{ color: ec }}>→</span></div>}
    </div>
  );
}

const RB = (dots, now, left, right) => ({ dots, now, leftLabel: left, rightLabel: right });
function Ribbon({ r }) { const items = (r.dots || []).map((d) => ({ dot: d })); return <div style={{ marginTop: 34 }}><YearRibbonBig items={items} now={r.now} height={44} alt={false} leftLabel={r.leftLabel} rightLabel={r.rightLabel}/></div>; }
function Shell({ children }) {
  return <AtlasFrame><UtilHeader left={<Monogram/>}/>{children}<div style={{ height: 116 }}/><TabBar active="atlas"/></AtlasFrame>;
}

// 1 · COLD START — an invitation, not a letter
function HomeCold() {
  return (
    <Shell>
      <div style={{ padding: '34px 24px 0' }}>
        <div style={{ marginBottom: 14 }}><Eyebrow color={T.goldDeep}>WELCOME, TIGER</Eyebrow></div>
        <p style={{ fontFamily: T.serif, fontSize: 26, fontWeight: 500, color: T.ink, lineHeight: 1.34, letterSpacing: -0.4, margin: 0 }}>
          Your atlas is <span style={{ fontStyle: 'italic' }}>almost empty</span> — which is the best way to begin.
        </p>
      </div>
      <div style={{ padding: '26px 22px 0' }}>
        <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', marginBottom: 12 }}>
          <Eyebrow>ON YOUR DESK</Eyebrow><span style={{ fontSize: 9.5, color: T.muteSoft, letterSpacing: 1.5, fontWeight: 600 }}>VESPER · WAITING</span>
        </div>
        <div style={{ height: 200 }}><Postcard blank stamp={false} title="A place you’ve loved" sub="tap to whisper one to Vesper" date="—·—·26" height="100%"/></div>
      </div>
      <Ribbon r={RB([null, null, 'now', null, null, null, null, null, null, null, null, null], 2, 'START YOUR YEAR', 'MARCH ’26')}/>
      <ShelfRooms label="THE SHELF" right="FOUR EMPTY ROOMS" rooms={[
        { e: '01 · INBOX', t: 'Save a memory', s: 'Vesper will hold it', accent: true },
        { e: '02 · MAP', t: 'Drop a pin', s: 'where have you been?' },
        { e: '03 · DNA', t: 'A reading awaits', s: 'after a few entries' },
        { e: '04 · POSTCARDS', t: 'No shelf yet', s: 'starts with your first' },
      ]}/>
    </Shell>
  );
}

// 2 · VESPER HAS A DRAFT READY — the one state with a gentle CTA
function HomeDraft() {
  return (
    <Shell>
      <HeroLetter eyebrow="VESPER · READY" cta="Review it">
        I drafted something — <span style={{ color: T.mute }}>ten photos from Sintra that wanted to be a postcard.</span> It needs your eye.
      </HeroLetter>
      <Ribbon r={RB([null, 'past', null, null, 'now', null, null, 'past', null, null, null, null], 4, 'YOUR YEAR', '2 KEPT')}/>
      <ShelfRooms rooms={[
        { e: '01 · INBOX', t: 'One draft', s: 'Sintra, waiting', accent: true },
        { e: '02 · MAP', t: '12 places', s: '5 trips' },
        { e: '03 · DNA', t: 'Coastal soul', s: '6 rituals' },
        { e: '04 · POSTCARDS', t: 'Two kept', s: 'both coastal' },
      ]}/>
    </Shell>
  );
}

// 3 · A MEMORY JUST KEPT — the populated postcard on the shelf
function HomeKept() {
  return (
    <Shell>
      <HeroLetter eyebrow="VESPER · JUNE">
        Kept. <span style={{ color: T.mute }}>Sintra’s on your shelf now — that’s three this year, and the year’s not half over.</span>
      </HeroLetter>
      <div style={{ padding: '30px 22px 0' }}>
        <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', marginBottom: 12 }}>
          <Eyebrow>ON YOUR SHELF</Eyebrow><span style={{ fontSize: 9.5, color: T.goldDeep, letterSpacing: 1.5, fontWeight: 600 }}>KEPT · MEMORY</span>
        </div>
        <div style={{ height: 200 }}><Postcard scene="porto" title="Sintra, in the mist" sub="kept just now · a slow day" date="06·02·26" height="100%"/></div>
      </div>
      <Ribbon r={RB([null, 'past', null, null, 'now', 'past', null, 'past', null, null, null, null], 4, 'YOUR YEAR', '3 KEPT')}/>
      <ShelfRooms rooms={[
        { e: '01 · INBOX', t: 'All read', s: 'nothing waiting' },
        { e: '02 · MAP', t: '12 places', s: '5 trips' },
        { e: '03 · DNA', t: 'Coastal soul', s: '6 rituals' },
        { e: '04 · POSTCARDS', t: 'Three kept', s: 'newest: Sintra', accent: true },
      ]}/>
    </Shell>
  );
}

// 4 · POWER USER — the letter richer, the ribbon full
function HomePower() {
  return (
    <Shell>
      <HeroLetter eyebrow="VESPER · JUNE" salutation="For Tiger —">
        Your fourth summer of coastlines. <span style={{ color: T.mute }}>Nine countries kept now, and still you wake before the heat to walk the empty harbours.</span>
      </HeroLetter>
      <Ribbon r={RB(['past', 'past', 'planned', 'past', 'now', 'past', 'past', 'past', 'planned', 'past', 'past', 'past'], 4, 'YOUR YEAR', 'A FULL ONE')}/>
      <ShelfRooms rooms={[
        { e: '01 · INBOX', t: 'All read', s: 'you keep a clean desk' },
        { e: '02 · MAP', t: '31 places', s: '9 countries' },
        { e: '03 · DNA', t: 'Coastal soul', s: '11 rituals' },
        { e: '04 · POSTCARDS', t: '24 kept', s: 'a real shelf' },
      ]}/>
    </Shell>
  );
}

// 5 · UPCOMING TRIP — the hero turns forward, quietly
function HomeUpcoming() {
  return (
    <Shell>
      <HeroLetter eyebrow="VESPER · SOON">
        Lisbon in three weeks. <span style={{ color: T.mute }}>I’ve been keeping notes — the quiet corners, mostly, and one dinner worth the first night.</span>
      </HeroLetter>
      <Ribbon r={RB([null, 'past', null, null, 'now', null, 'planned', null, null, null, null, null], 4, 'YOUR YEAR', 'LISBON · JUL')}/>
      <ShelfRooms rooms={[
        { e: '01 · INBOX', t: 'Notes for Lisbon', s: 'six, so far', accent: true },
        { e: '02 · MAP', t: '12 places', s: 'Lisbon pinned' },
        { e: '03 · DNA', t: 'Coastal soul', s: '6 rituals' },
        { e: '04 · POSTCARDS', t: 'Two kept', s: 'both coastal' },
      ]}/>
    </Shell>
  );
}

// 6 · ACTIVE TRIP — a calm companion; the rooms recede
function HomeActive() {
  return (
    <Shell>
      <div style={{ padding: '34px 24px 0' }}>
        <div style={{ marginBottom: 14 }}><Eyebrow color={T.goldDeep}>VESPER · TODAY · LISBON</Eyebrow></div>
        <p style={{ fontFamily: T.serif, fontSize: 26, fontWeight: 500, color: T.ink, lineHeight: 1.34, letterSpacing: -0.4, margin: 0 }}>
          Day three. <span style={{ color: T.mute }}>A slow morning in Alfama, then down to the water before it’s warm.</span>
        </p>
        <div style={{ marginTop: 20, padding: '14px 16px', background: T.cardWarm, borderRadius: 14, border: sHair }}>
          <div style={{ fontFamily: T.mono, fontSize: 8, color: T.mute, letterSpacing: 1.2, fontWeight: 600 }}>NEXT · 1:30</div>
          <div style={{ fontFamily: T.serif, fontSize: 16, color: T.ink, fontWeight: 500, letterSpacing: -0.2, marginTop: 4 }}>Lunch at Ramiro</div>
          <div style={{ fontFamily: T.serif, fontSize: 12.5, color: T.mute, marginTop: 2 }}>a six-minute walk from where you are</div>
        </div>
      </div>
      <Ribbon r={RB([null, 'past', null, null, 'now', null, null, 'past', null, null, null, null], 4, 'YOUR YEAR', 'IN LISBON')}/>
      <RoomsThin/>
    </Shell>
  );
}

// 7 · JUST RETURNED — the bridge from travel → kept artifact
function HomeReturned() {
  return (
    <Shell>
      <HeroLetter eyebrow="VESPER · JUST BACK" cta="Draft the story">
        Ten days in Portugal. <span style={{ color: T.mute }}>Want me to draft the story while it’s still warm? I kept the best forty frames.</span>
      </HeroLetter>
      <Ribbon r={RB([null, 'past', null, null, 'past', 'now', null, 'past', null, null, null, null], 5, 'YOUR YEAR', 'JUST BACK')}/>
      <ShelfRooms rooms={[
        { e: '01 · INBOX', t: 'A trip to keep', s: 'Portugal, 10 days', accent: true },
        { e: '02 · MAP', t: '14 places', s: '6 trips' },
        { e: '03 · DNA', t: 'Coastal soul', s: '7 rituals' },
        { e: '04 · POSTCARDS', t: 'Story waiting', s: 'press to begin' },
      ]}/>
    </Shell>
  );
}

Object.assign(window, { ShelfRooms, RoomsThin, HeroLetter, Shell, HomeCold, HomeDraft, HomeKept, HomePower, HomeUpcoming, HomeActive, HomeReturned });
