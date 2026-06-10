// ═══════════════════════════════════════════════════════════════
// ATLAS HOME — hero & hierarchy variations, quiet ("nothing new")
// state. The reframe: the home reports what's TRUE (your relationship
// with places), not what's NEW. Each establishes ONE hero, demotes
// the four rooms to a secondary drawer, and keeps its top edge clear
// of the header (no high-contrast block under the title).
// Holds the system: T tokens, Cormorant serif, single gold accent,
// riso line-art, the crown · year ribbon · four rooms.
// ═══════════════════════════════════════════════════════════════

const aHair = `0.5px solid ${T.hairline}`;

// the KEEPING FOR crown (held constant, top of every variation)
function Crown({ label = 'KEEPING FOR', name = 'Tiger', dim }) {
  return (
    <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '14px 22px 0' }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
        <div style={{ width: 30, height: 30, borderRadius: 999, background: dim ? T.cardWarm : T.goldDeep, border: dim ? `0.5px solid ${T.hairline}` : 'none', color: dim ? T.goldDeep : T.cardWarm, fontFamily: T.serif, fontWeight: 500, fontSize: 13, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>T</div>
        <div>
          <div style={{ fontSize: 9.5, color: T.muteSoft, letterSpacing: 1.6, fontWeight: 600, lineHeight: 1 }}>{label}</div>
          <div style={{ fontFamily: T.serif, fontSize: 14, color: T.ink, fontWeight: 500, lineHeight: 1.2, marginTop: 2 }}>{name}</div>
        </div>
      </div>
      <div style={{ display: 'flex', alignItems: 'center', gap: 16 }}>
        <Marks.Search s={18} c={T.inkSoft}/>
        <Marks.Plus s={18} c={T.inkSoft}/>
      </div>
    </div>
  );
}

// the four rooms, DEMOTED to a quiet drawer (shared across variants)
function RoomsDrawer({ rooms = [['01 · INBOX', 'Quiet'], ['02 · MAP', '14 cities'], ['03 · DNA', 'Coastal'], ['04 · POSTCARDS', '2 kept']] }) {
  return (
    <div style={{ margin: '0 22px', paddingTop: 15, borderTop: aHair }}>
      <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', marginBottom: 11 }}>
        <Eyebrow>THE SHELF</Eyebrow>
        <span style={{ color: T.muteSoft, fontSize: 9.5, letterSpacing: 1.5, fontWeight: 600 }}>FOUR ROOMS</span>
      </div>
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: 7 }}>
        {rooms.map(([eb, tail], i) => (
          <div key={i} style={{ padding: '11px 10px', background: T.cardWarm, borderRadius: 11, border: `0.5px solid ${T.hairline}` }}>
            <div style={{ fontFamily: T.mono, fontSize: 7.5, color: T.mute, letterSpacing: 0.8, fontWeight: 600 }}>{eb}</div>
            <div style={{ fontFamily: T.serif, fontSize: 13, color: T.ink, fontWeight: 500, letterSpacing: -0.2, marginTop: 6, lineHeight: 1 }}>{tail}</div>
          </div>
        ))}
      </div>
    </div>
  );
}

// a tall, scrolling frame (the home doesn't need to fit one viewport)
function AtlasFrame({ children }) {
  return (
    <div style={{ width: 393, borderRadius: 44, overflow: 'hidden', background: T.bg, position: 'relative', fontFamily: T.sans, color: T.ink, boxShadow: '0 0 0 11px #0d0b09, 0 0 0 12px #2a2622, 0 30px 60px -20px rgba(0,0,0,0.35)' }}>
      <div style={{ position: 'absolute', top: 18, left: 32, zIndex: 32 }}><span style={{ fontWeight: 600, fontSize: 17, color: T.ink }}>9:41</span></div>
      <div style={{ position: 'absolute', top: 11, left: '50%', transform: 'translateX(-50%)', width: 124, height: 37, borderRadius: 24, background: '#000', zIndex: 33 }}/>
      <div style={{ paddingTop: 54 }}>{children}</div>
    </div>
  );
}

// utility-only header (no crown text) — search · +, optional left slot
function UtilHeader({ left }) {
  return (
    <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '14px 22px 0', minHeight: 30 }}>
      <div>{left || <div/>}</div>
      <div style={{ display: 'flex', alignItems: 'center', gap: 16 }}>
        <Marks.Search s={18} c={T.inkSoft}/>
        <Marks.Plus s={18} c={T.inkSoft}/>
      </div>
    </div>
  );
}

// the gold "T" monogram (for mode C)
const Monogram = () => <div style={{ width: 30, height: 30, borderRadius: 999, background: T.goldDeep, color: T.cardWarm, fontFamily: T.serif, fontWeight: 500, fontSize: 13, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>T</div>;

// the letter hero — optional "For Tiger —" salutation (mode A)
function LetterHero({ salutation }) {
  return (
    <div style={{ padding: '34px 24px 0' }}>
      <div style={{ marginBottom: salutation ? 9 : 15 }}><Eyebrow color={T.goldDeep}>VESPER · JUNE</Eyebrow></div>
      {salutation && <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 17, color: T.goldDeep, marginBottom: 12 }}>For Tiger —</div>}
      <p style={{ fontFamily: T.serif, fontSize: 26, fontWeight: 500, color: T.ink, lineHeight: 1.34, letterSpacing: -0.4, margin: 0 }}>
        Two places kept this year, both by the sea. <span style={{ color: T.mute }}>You keep returning to the coast — slow mornings, food first.</span> And Lisbon’s still unwritten.
      </p>
    </div>
  );
}

// the empty desk postcard
function DeskPostcard() {
  return (
    <div style={{ padding: '38px 22px 0' }}>
      <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', marginBottom: 12 }}>
        <Eyebrow>ON YOUR DESK</Eyebrow>
        <span style={{ fontSize: 9.5, color: T.muteSoft, letterSpacing: 1.5, fontWeight: 600 }}>VESPER · WAITING</span>
      </div>
      <div style={{ height: 196 }}>
        <Postcard blank stamp={false} title="A place you’ve loved" sub="tap to whisper one to Vesper" date="—·—·26" height="100%"/>
      </div>
    </div>
  );
}

// the original asymmetric four-room shelf — with an optional crown line above it (mode B)
function Shelf({ crownLine }) {
  return (
    <div>
      {crownLine ? (
        <div style={{ margin: '40px 22px 14px', paddingTop: 16, borderTop: aHair, display: 'flex', alignItems: 'center', gap: 10 }}>
          <Monogram/>
          <div>
            <div style={{ fontSize: 9.5, color: T.muteSoft, letterSpacing: 1.6, fontWeight: 600, lineHeight: 1 }}>KEEPING FOR</div>
            <div style={{ fontFamily: T.serif, fontSize: 15, color: T.ink, fontWeight: 500, lineHeight: 1.2, marginTop: 2 }}>Tiger</div>
          </div>
          <span style={{ marginLeft: 'auto', color: T.muteSoft, fontSize: 9.5, letterSpacing: 1.5, fontWeight: 600 }}>FOUR ROOMS</span>
        </div>
      ) : (
        <div style={{ margin: '40px 22px 12px', display: 'flex', alignItems: 'baseline', justifyContent: 'space-between' }}>
          <Eyebrow>THE SHELF</Eyebrow>
          <span style={{ color: T.muteSoft, fontSize: 9.5, letterSpacing: 1.5, fontWeight: 600 }}>FOUR ROOMS</span>
        </div>
      )}
      <div style={{ margin: '0 16px', display: 'grid', gridTemplateColumns: '1.15fr 1fr', gap: 10 }}>
        <ArtifactCard mark={<Marks.Inbox size={66}/>} eyebrow="01 · INBOX" title="All read" tail="nothing waiting" tall heightOverride={172}/>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
          <ArtifactCard mark={<Marks.Map size={50}/>} eyebrow="02 · MAP" title="14 cities" tail="7 countries" compact heightOverride={81}/>
          <ArtifactCard mark={<Marks.DNA size={50}/>} eyebrow="03 · DNA" title="Coastal soul" tail="6 rituals" compact heightOverride={81}/>
        </div>
      </div>
      <div style={{ margin: '10px 16px 0' }}>
        <ArtifactCard mark={<Marks.Postcard size={50}/>} eyebrow="04 · POSTCARDS" title="Two kept" tail="both coastal" wide heightOverride={70}/>
      </div>
    </div>
  );
}

// ─── A · DEMOTE INTO THE LETTER (canonical) ─────────────────────
// The header carries only the admin door (gold "T" monogram, top-left)
// + quiet utility. The "For Tiger —" salutation makes identity content.
function AtlasA() {
  return (
    <AtlasFrame>
      <UtilHeader left={<Monogram/>}/>
      <LetterHero salutation/>
      <div style={{ marginTop: 38 }}>
        <YearRibbonBig items={[{}, { dot: 'past', label: 'Porto' }, {}, { dot: 'past', label: 'Lisbon' }, { dot: 'now' }, {}, {}, {}, { dot: 'planned', label: 'Tokyo' }, {}, {}, {}]} now={4} height={84} alt leftLabel="YOUR YEAR" rightLabel="2 KEPT" nowRead={{ tag: 'MAY · WHERE YOU ARE', line: 'Lisbon and Porto behind you — Tokyo waiting in the autumn.' }}/>
      </div>
      <DeskPostcard/>
      <Shelf/>
      <div style={{ height: 116 }}/>
      <TabBar active="atlas"/>
    </AtlasFrame>
  );
}

// ─── B · MOVE IT DOWN ───────────────────────────────────────────
// Header utility only; "KEEPING FOR · Tiger" becomes a quiet line
// that frames the shelf as Tiger's collection.
function AtlasB() {
  return (
    <AtlasFrame>
      <UtilHeader/>
      <LetterHero/>
      <div style={{ marginTop: 40 }}>
        <YearRibbonH dots={[null, 'past', null, null, 'now', null, null, 'past', null, null, null, null]} now={4} leftLabel="YOUR YEAR" rightLabel="2 KEPT"/>
      </div>
      <DeskPostcard/>
      <Shelf crownLine/>
      <div style={{ height: 116 }}/>
      <TabBar active="atlas"/>
    </AtlasFrame>
  );
}

// ─── C · SHRINK IN THE HEADER ───────────────────────────────────
// Just the gold "T" monogram top-left (no "KEEPING FOR" text); the
// phrase lives behind a profile tap.
function AtlasC() {
  return (
    <AtlasFrame>
      <UtilHeader left={<Monogram/>}/>
      <LetterHero/>
      <div style={{ marginTop: 40 }}>
        <YearRibbonH dots={[null, 'past', null, null, 'now', null, null, 'past', null, null, null, null]} now={4} leftLabel="YOUR YEAR" rightLabel="2 KEPT"/>
      </div>
      <DeskPostcard/>
      <Shelf/>
      <div style={{ height: 116 }}/>
      <TabBar active="atlas"/>
    </AtlasFrame>
  );
}

Object.assign(window, { Crown, UtilHeader, Monogram, LetterHero, DeskPostcard, Shelf, AtlasA, AtlasB, AtlasC });

// ═══════════════════════════════════════════════════════════════
// THE PERSONAL / ADMIN PAGE — what the header monogram opens.
// Identity-as-content lives on the home; this is the destination you
// go INTO to change things. Atlas-styled, scrolling.
// ═══════════════════════════════════════════════════════════════

function Initial({ name, c = T.goldDeep }) {
  return <div style={{ width: 30, height: 30, borderRadius: 999, background: T.cardWarm, border: `0.5px solid ${T.hairline}`, color: c, fontFamily: T.serif, fontWeight: 500, fontSize: 13, display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0 }}>{name}</div>;
}

function AdminRow({ eyebrow, title, value, right = 'chevron', last }) {
  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: 14, padding: '15px 0', borderTop: aHair }}>
      <div style={{ flex: 1, minWidth: 0 }}>
        <div style={{ fontFamily: T.mono, fontSize: 8, color: T.mute, letterSpacing: 1.2, fontWeight: 600 }}>{eyebrow}</div>
        <div style={{ fontFamily: T.serif, fontSize: 16, color: T.ink, fontWeight: 500, letterSpacing: -0.2, marginTop: 4, lineHeight: 1.1 }}>{title}</div>
        {value && <div style={{ fontFamily: T.serif, fontSize: 12.5, color: T.mute, marginTop: 2 }}>{value}</div>}
      </div>
      {right === 'chevron' && <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke={T.muteSoft} strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d="M9 6l6 6-6 6"/></svg>}
      {right === 'toggle' && <div style={{ width: 38, height: 22, borderRadius: 999, background: T.goldDeep, position: 'relative' }}><div style={{ position: 'absolute', top: 2, right: 2, width: 18, height: 18, borderRadius: 999, background: '#fff' }}/></div>}
      {React.isValidElement(right) && right}
    </div>
  );
}

function AdminGroup({ label, children }) {
  return (
    <div style={{ margin: '26px 24px 0' }}>
      <Eyebrow>{label}</Eyebrow>
      <div style={{ marginTop: 4 }}>{children}</div>
    </div>
  );
}

function AtlasProfile() {
  return (
    <AtlasFrame>
      {/* back to Atlas */}
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '14px 22px 0' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 6, color: T.inkSoft }}>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke={T.inkSoft} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><path d="M14 6l-6 6 6 6"/></svg>
        </div>
        <span style={{ fontFamily: T.mono, fontSize: 8.5, color: T.muteSoft, letterSpacing: 1.4, fontWeight: 600 }}>YOU</span>
      </div>

      {/* masthead — the big monogram, the librarian framing */}
      <div style={{ padding: '24px 24px 0', display: 'flex', alignItems: 'center', gap: 16 }}>
        <div style={{ width: 60, height: 60, borderRadius: 999, background: T.goldDeep, color: T.cardWarm, fontFamily: T.serif, fontWeight: 500, fontSize: 26, display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0 }}>T</div>
        <div>
          <div style={{ fontFamily: T.mono, fontSize: 8.5, color: T.mute, letterSpacing: 1.4, fontWeight: 600 }}>KEEPING SINCE 2021</div>
          <h1 style={{ fontFamily: T.serif, fontSize: 28, fontWeight: 500, color: T.ink, letterSpacing: -0.5, margin: '3px 0 0', lineHeight: 1 }}>Tiger</h1>
        </div>
      </div>
      {/* standing line — prose, not a metric strip */}
      <div style={{ margin: '20px 24px 0', padding: '14px 0', borderTop: aHair, borderBottom: aHair }}>
        <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 16, color: T.soft, lineHeight: 1.4, margin: 0 }}>Twelve places, five trips, four who travel with you — and two kept this year.</p>
      </div>

      {/* flat list — identity & taste folded into Travel DNA; no section labels */}
      <div style={{ margin: '22px 24px 0' }}>
        <AdminRow eyebrow="TRAVEL DNA" title="Early-morning soul, coastal" value="how Vesper reads you — taste, pace, the quiet you like"/>
        <AdminRow eyebrow="WHO YOU TRAVEL WITH" title="Ana, Theo & 2 more" value="4 friends · your usual companions" right={<div style={{ display: 'flex' }}>{['A', 'T', 'M'].map((n, i) => <div key={n} style={{ marginLeft: i ? -8 : 0 }}><Initial name={n}/></div>)}</div>}/>
        <AdminRow eyebrow="PRIVACY" title="What you share" value="saves are private · trips shared with the group"/>
        <AdminRow eyebrow="NOTIFICATIONS" title="Quiet by default" value="only when something’s genuinely worth it" right="toggle"/>
        <AdminRow eyebrow="ACCOUNT" title="Vesper · member" value="manage devices & sign-in"/>
      </div>

      {/* sign out */}
      <div style={{ margin: '28px 24px 0', paddingTop: 16, borderTop: aHair }}>
        <span style={{ fontFamily: T.serif, fontSize: 15, color: T.mute }}>Sign out</span>
      </div>

      <div style={{ height: 116 }}/>
      <TabBar active="atlas"/>
    </AtlasFrame>
  );
}

Object.assign(window, { Initial, AdminRow, AdminGroup, AtlasProfile });
