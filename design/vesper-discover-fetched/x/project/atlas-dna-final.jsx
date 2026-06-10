// ═══════════════════════════════════════════════════════════════
// ATLAS · DNA — canonical page (B nameplate) + 4 dimension pages.
// No scroll: nameplate + 2×2 tappable dimension tiles + declared
// line, with a floating "Talk to Vesper" button bottom-right.
// Each tile opens its own memory/setting page (learned = contestable).
// Reuses Phone, T, TabBar, Marks.
// ═══════════════════════════════════════════════════════════════

// floating talk-to-Vesper pill — bottom-right, above the tab bar
function TalkToVesper() {
  return (
    <div style={{ position: 'absolute', right: 16, bottom: 100, display: 'flex', alignItems: 'center', gap: 7, padding: '11px 16px', borderRadius: 999, background: T.goldDeep, color: T.cardWarm, boxShadow: '0 10px 24px -8px rgba(138,102,40,0.5)' }}>
      <svg width="13" height="13" viewBox="0 0 24 24" fill={T.cardWarm}><path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z"/></svg>
      <span style={{ fontFamily: T.sans, fontSize: 13, fontWeight: 600 }}>Talk to Vesper</span>
    </div>
  );
}

const DIMS = [
  { k: 'ENERGY',   v: 'Relaxed' },
  { k: 'BUDGET',   v: 'Considered' },
  { k: 'SOCIAL',   v: 'Small groups' },
  { k: 'PLANNING', v: 'Loose' },
];

// ─── canonical DNA page — nameplate + tappable tiles, no scroll ──
function DNAPage() {
  return (
    <Phone bg={T.bg}>
      <div style={{ padding: '14px 22px 0' }}>
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke={T.inkSoft} strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M15 5l-7 7 7 7"/></svg>
      </div>

      {/* B · archetype nameplate */}
      <div style={{ padding: '22px 24px 0' }}>
        <div style={{ fontSize: 10.5, color: T.gold, letterSpacing: 2, fontWeight: 600 }}>03 · TRAVEL DNA · YOUR ARCHETYPE</div>
        <h1 style={{ fontFamily: T.serif, fontWeight: 500, fontSize: 50, lineHeight: 0.92, letterSpacing: -1.6, color: T.ink, margin: '14px 0 0' }}>Coastal <span style={{ fontStyle: 'italic' }}>soul.</span></h1>
        <p style={{ fontFamily: T.serif, fontSize: 16.5, color: T.mute, lineHeight: 1.4, margin: '12px 0 0', maxWidth: 300 }}>You travel slow, and toward water — mornings first, the river before the museum.</p>
      </div>

      {/* the reading — B's pull-quote */}
      <div style={{ margin: '20px 24px 0', padding: '15px 0', borderTop: `0.5px solid ${T.hairline}`, borderBottom: `0.5px solid ${T.hairline}` }}>
        <p style={{ fontFamily: T.serif, fontSize: 15.5, color: T.ink, margin: 0, lineHeight: 1.42, letterSpacing: -0.12 }}>“You return to one step three times before you find the next — the neighborhood before the landmark, the river before the museum.”</p>
        <div style={{ marginTop: 9, fontFamily: T.mono, color: T.muteSoft, fontSize: 9, letterSpacing: 1.8, fontWeight: 600 }}>— VESPER, READING YOU</div>
      </div>

      {/* the four dimensions — quiet hairline rows (no plates), each opens its page */}
      <div style={{ padding: '16px 24px 0' }}>
        <div style={{ fontSize: 10.5, color: T.mute, letterSpacing: 2, fontWeight: 600 }}>HOW VESPER READS YOU</div>
        <div style={{ marginTop: 6, display: 'grid', gridTemplateColumns: '1fr 1fr', columnGap: 18 }}>
          {DIMS.map((d) => (
            <div key={d.k} style={{ padding: '14px 0', borderTop: `0.5px solid ${T.hairThin}` }}>
              <div style={{ fontFamily: T.mono, fontSize: 8, color: T.mute, letterSpacing: 1.2, fontWeight: 600 }}>{d.k}</div>
              <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between' }}>
                <span style={{ fontFamily: T.serif, fontSize: 16, color: T.ink, fontWeight: 500, letterSpacing: -0.2, marginTop: 2 }}>{d.v}</span>
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke={T.muteSoft} strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d="M9 6l6 6-6 6"/></svg>
              </div>
            </div>
          ))}
        </div>
        <div style={{ marginTop: 13, paddingTop: 12, borderTop: `0.5px solid ${T.hairline}`, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
          <div>
            <span style={{ fontFamily: T.mono, fontSize: 8, color: T.goldDeep, letterSpacing: 1.2, fontWeight: 700 }}>YOU’VE TOLD VESPER</span>
            <div style={{ fontFamily: T.serif, fontSize: 13.5, color: T.inkSoft, marginTop: 3 }}>Vegetarian · step-free · EN, PT</div>
          </div>
          <span style={{ fontFamily: T.mono, fontSize: 9, color: T.muteSoft, letterSpacing: 1.2, fontWeight: 600 }}>EDIT</span>
        </div>
      </div>

      <TalkToVesper/>
      <TabBar active="atlas"/>
    </Phone>
  );
}

// ─── a dimension memory/setting page (the tile destination) ─────
function DimPage({ k, title, body, trips }) {
  return (
    <Phone bg={T.bg}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 6, padding: '14px 22px 0', color: T.inkSoft }}>
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke={T.inkSoft} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><path d="M14 6l-6 6 6 6"/></svg>
      </div>

      <div style={{ padding: '22px 24px 0' }}>
        <div style={{ fontFamily: T.mono, fontSize: 9, color: T.goldDeep, letterSpacing: 1.8, fontWeight: 700 }}>{k} · LEARNED</div>
        <h1 style={{ fontFamily: T.serif, fontWeight: 500, fontSize: 36, lineHeight: 0.98, letterSpacing: -1, color: T.ink, margin: '12px 0 0' }}>{title}</h1>
        <p style={{ fontFamily: T.serif, fontSize: 16, color: T.soft, lineHeight: 1.46, margin: '14px 0 0' }}>{body}</p>
      </div>

      {/* the evidence */}
      <div style={{ padding: '20px 24px 0' }}>
        <div style={{ fontSize: 10, color: T.mute, letterSpacing: 1.8, fontWeight: 600 }}>WHAT TAUGHT VESPER THIS</div>
        {trips.map(([t, note], i) => (
          <div key={t} style={{ display: 'flex', alignItems: 'baseline', gap: 10, padding: '11px 0', borderTop: `0.5px solid ${T.hairThin}` }}>
            <span style={{ fontFamily: T.serif, fontSize: 15, color: T.ink, fontWeight: 500, width: 86, flexShrink: 0, letterSpacing: -0.2 }}>{t}</span>
            <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13, color: T.mute, lineHeight: 1.35 }}>{note}</span>
          </div>
        ))}
      </div>

      {/* contest — learned, so push back; never a form */}
      <div style={{ position: 'absolute', left: 24, right: 24, bottom: 116 }}>
        <div style={{ display: 'flex', gap: 10 }}>
          <div style={{ flex: 1, textAlign: 'center', padding: '13px 0', borderRadius: 999, background: T.goldDeep, color: T.cardWarm, fontFamily: T.sans, fontSize: 14, fontWeight: 600 }}>That’s me</div>
          <div style={{ flex: 1, textAlign: 'center', padding: '13px 0', borderRadius: 999, border: `0.5px solid ${T.hairline}`, color: T.inkSoft, fontFamily: T.sans, fontSize: 14, fontWeight: 500 }}>Not quite →</div>
        </div>
        <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12, color: T.muteSoft, textAlign: 'center', margin: '12px 0 0' }}>“Not quite” opens a note to Vesper — it re-reads, never just overwrites.</p>
      </div>

      <TabBar active="atlas"/>
    </Phone>
  );
}

const DimEnergy = () => <DimPage k="ENERGY" title={<>You travel <span style={{ fontStyle: 'italic' }}>relaxed.</span></>} body="You start late and end slow — unhurried mornings, no dawn alarms, long lunches that run." trips={[['Lisbon', 'first coffee at ten, never before'], ['Porto', 'two-hour lunches, no rush to the next'], ['CDMX', 'mornings kept empty on purpose'], ['Tokyo', 'planned — late starts pencilled in']]}/>;
const DimBudget = () => <DimPage k="BUDGET" title={<>You spend with <span style={{ fontStyle: 'italic' }}>care.</span></>} body="Mid-range stays, one meal worth splurging on, the rest spent on time rather than things." trips={[['Lisbon', 'a guesthouse, one dinner at Ramiro'], ['Porto', 'modest room, the river for free'], ['CDMX', 'one tasting menu, market food otherwise']]}/>;
const DimSocial = () => <DimPage k="SOCIAL" title={<>You travel <span style={{ fontStyle: 'italic' }}>close.</span></>} body="Two or three people, rarely solo, never a crowd — and the same few names keep recurring." trips={[['Lisbon', 'with Ana — sixth trip together'], ['Porto', 'just you and Theo'], ['CDMX', 'three of you, no more']]}/>;
const DimPlanning = () => <DimPage k="PLANNING" title={<>You leave <span style={{ fontStyle: 'italic' }}>room.</span></>} body="A spine, then space — you book the anchors and let the rest of the day find itself." trips={[['Lisbon', 'two dinners held, days left loose'], ['Porto', 'no itinerary past the first morning'], ['CDMX', 'one fixed plan a day, never more']]}/>;

// ─── declared prefs — the editable half (tap "YOU'VE TOLD VESPER") ──
function DeclaredEdit() {
  const Chip = ({ on, add, children }) => (
    <span style={{ display: 'inline-flex', alignItems: 'center', gap: 5, padding: '8px 14px', borderRadius: 999, fontFamily: T.serif, fontSize: 13.5, fontWeight: 500, background: on ? T.cardWarm : 'transparent', border: on ? `0.5px solid ${T.gold}` : `0.5px solid ${T.hairline}`, color: on ? T.goldDeep : (add ? T.mute : T.soft) }}>
      {add && <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke={T.mute} strokeWidth="2" strokeLinecap="round"><path d="M12 5v14M5 12h14"/></svg>}
      {children}
    </span>
  );
  const Group = ({ label, children }) => (
    <div style={{ marginTop: 20 }}>
      <div style={{ fontFamily: T.mono, fontSize: 8.5, color: T.mute, letterSpacing: 1.4, fontWeight: 600, marginBottom: 9 }}>{label}</div>
      <div style={{ display: 'flex', flexWrap: 'wrap', gap: 7 }}>{children}</div>
    </div>
  );
  return (
    <Phone bg={T.bg}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 6, padding: '14px 22px 0', color: T.inkSoft }}>
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke={T.inkSoft} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><path d="M14 6l-6 6 6 6"/></svg>
      </div>

      <div style={{ padding: '22px 24px 0' }}>
        <div style={{ fontFamily: T.mono, fontSize: 9, color: T.goldDeep, letterSpacing: 1.8, fontWeight: 700 }}>DECLARED · YOURS TO SET</div>
        <h1 style={{ fontFamily: T.serif, fontWeight: 500, fontSize: 33, lineHeight: 0.98, letterSpacing: -0.9, color: T.ink, margin: '12px 0 0' }}>What you’ve told <span style={{ fontStyle: 'italic' }}>Vesper.</span></h1>
        <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 14, color: T.mute, lineHeight: 1.4, margin: '11px 0 0' }}>The hard facts Vesper plans around — yours to set, anytime.</p>
      </div>

      <div style={{ padding: '8px 24px 0' }}>
        <Group label="DIETARY">
          <Chip on>Vegetarian</Chip><Chip>Vegan</Chip><Chip>Pescatarian</Chip><Chip>Gluten-free</Chip><Chip>Dairy-free</Chip><Chip add>add</Chip>
        </Group>
        <Group label="ACCESS">
          <Chip on>Step-free where it matters</Chip><Chip add>add</Chip>
        </Group>
        <Group label="LANGUAGES">
          <Chip on>English</Chip><Chip on>Português</Chip><Chip>Español</Chip><Chip add>add</Chip>
        </Group>
      </div>

      {/* the boundary back to the learned half */}
      <div style={{ position: 'absolute', left: 24, right: 24, bottom: 116, paddingTop: 14, borderTop: `0.5px solid ${T.hairline}` }}>
        <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13, color: T.muteSoft, lineHeight: 1.4, margin: 0 }}>Everything else — your pace, budget, the kind of quiet you like — Vesper <span style={{ color: T.goldDeep }}>learns from how you travel.</span></p>
      </div>

      <TabBar active="atlas"/>
    </Phone>
  );
}

Object.assign(window, { DeclaredEdit });

Object.assign(window, { DNAPage, DimPage, DimEnergy, DimBudget, DimSocial, DimPlanning, TalkToVesper });
