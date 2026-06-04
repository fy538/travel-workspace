// ─── Vesper Cards · canvas app ──────────────────────────────────
function Stage({ children, pad = 16 }) {
  return (
    <div style={{
      width: 393, background: T.bg, borderRadius: 20, padding: pad,
      border: `0.5px solid ${T.hairline}`,
      display: 'flex', alignItems: 'center', minHeight: 200,
    }}>
      <div style={{ width: '100%' }}>{children}</div>
    </div>
  );
}

function CardSpec({ name, anatomy, hierarchy, copy, actions, states, when, sheet }) {
  const Row = ({ k, children }) => (
    <div style={{ display: 'grid', gridTemplateColumns: '74px 1fr', gap: 12, padding: '9px 0', borderTop: `0.5px solid ${T.hairThin}` }}>
      <div style={{ fontSize: 9, letterSpacing: 1.4, color: T.mute, fontWeight: 700, paddingTop: 2 }}>{k}</div>
      <div style={{ fontSize: 12, color: T.inkSoft, lineHeight: 1.45 }}>{children}</div>
    </div>
  );
  return (
    <div style={{ width: 360, padding: '24px 24px', background: '#F1ECE2', borderRadius: 8 }}>
      <div style={{ fontSize: 10, letterSpacing: 2, color: T.gold, fontWeight: 600 }}>SPEC</div>
      <h3 style={{ fontFamily: T.serif, fontSize: 24, fontWeight: 500, letterSpacing: -0.5, color: T.ink, margin: '4px 0 10px' }}>{name}</h3>
      <Row k="ANATOMY">{anatomy}</Row>
      <Row k="HIERARCHY">{hierarchy}</Row>
      <Row k="COPY">{copy}</Row>
      <Row k="ACTIONS">{actions}</Row>
      <Row k="STATES">{states}</Row>
      <Row k="APPEARS">{when}</Row>
      <Row k="OPENS">{sheet}</Row>
    </div>
  );
}

function CBody({ children, w = 560, italic }) {
  return <p style={{ maxWidth: w, margin: '0 0 14px', fontSize: 13.5, lineHeight: 1.55, color: T.inkSoft, fontFamily: italic ? T.serif : T.sans, fontStyle: italic ? 'italic' : 'normal' }}>{children}</p>;
}
function CH2({ children }) {
  return <h2 style={{ fontFamily: T.serif, fontWeight: 500, fontSize: 34, letterSpacing: -0.9, lineHeight: 1.04, color: T.ink, margin: '8px 0 14px' }}>{children}</h2>;
}
function CEB({ children }) {
  return <div style={{ fontSize: 10.5, letterSpacing: 2, color: T.gold, fontWeight: 600 }}>{children}</div>;
}
function SpecHead({ children, mt }) {
  return <div style={{ fontSize: 10, letterSpacing: 1.8, color: T.mute, fontWeight: 700, marginTop: mt ? 18 : 0, marginBottom: 6 }}>{children}</div>;
}
function SpecLine({ k, children }) {
  return (
    <div style={{ display: 'grid', gridTemplateColumns: '92px 1fr', gap: 10, padding: '5px 0', borderTop: `0.5px solid ${T.hairThin}` }}>
      <span style={{ fontFamily: T.mono, fontSize: 9.5, color: T.goldDeep, letterSpacing: 0.5, fontWeight: 600, paddingTop: 1 }}>{k}</span>
      <span style={{ fontSize: 11.5, color: T.inkSoft, lineHeight: 1.4 }}>{children}</span>
    </div>
  );
}
const Center = ({ children }) => <div style={{ display: 'flex', justifyContent: 'center', paddingTop: 8 }}>{children}</div>;

function CardsApp() {
  return (
    <DesignCanvas defaultZoom={0.5}>

      {/* ── COVER ── */}
      <DCSection id="cover" title="Vesper · the card system" subtitle="Cards designed by interaction family, not backend kind. Vesper's work objects — briefs, slips, drafts, notes.">
        <DCArtboard id="brief" label="What this is" width={640} height={860} bg="#F1ECE2">
          <div style={{ padding: '44px 36px', fontFamily: T.sans, color: T.inkSoft, fontSize: 13.5, lineHeight: 1.55 }}>
            <CEB>VESPER · CARD SYSTEM</CEB>
            <h1 style={{ fontFamily: T.serif, fontSize: 48, lineHeight: 0.96, letterSpacing: -1.3, fontWeight: 500, margin: '8px 0 16px', color: T.ink }}>
              Vesper’s work,<br/><em>made into objects.</em>
            </h1>
            <CBody>
              The Vesper tab is the live intelligence surface — <i>what Vesper is working on for me right now</i>.
              Not a chatbot inbox, not a dashboard. Every card is one of Vesper’s work objects with a single
              clear job, mapped to seven interaction families rather than the fourteen backend kinds.
            </CBody>
            <div style={{ borderTop: `0.5px solid ${T.hairline}`, paddingTop: 14, marginTop: 4 }}>
              <div style={{ fontSize: 10, letterSpacing: 2, color: T.mute, fontWeight: 600, marginBottom: 8 }}>SEVEN FAMILIES → FOURTEEN KINDS</div>
              {[
                ['Needs your call', 'urgent_trip_action · constraint_alert · group vote · pending decision'],
                ['Vesper prepared', 'planning_brief · itinerary · shortlist · retrospective · settlement · Atlas artifact'],
                ['Live companion', 'live_trip · daily_brief · weather · near_you · imminent_trip'],
                ['Signal / pattern', 'saved_cluster · memory_echo · taste pattern'],
                ['Capture / memory', 'capture_nudge · photo cluster · memory_echo'],
                ['Resume thread', 'trip_thread · last question'],
                ['Starter', 'starter · cold start · first prompt'],
              ].map(([a, b]) => (
                <div key={a} style={{ display: 'grid', gridTemplateColumns: '128px 1fr', gap: 10, padding: '7px 0', borderTop: `0.5px solid ${T.hairThin}` }}>
                  <div style={{ fontFamily: T.serif, fontSize: 14, color: T.ink, fontWeight: 500, letterSpacing: -0.1 }}>{a}</div>
                  <div style={{ fontFamily: T.mono, fontSize: 9.5, color: T.mute, letterSpacing: 0.3, lineHeight: 1.5 }}>{b}</div>
                </div>
              ))}
            </div>
            <div style={{ borderTop: `0.5px solid ${T.hairline}`, marginTop: 14, paddingTop: 14 }}>
              <div style={{ fontSize: 10, letterSpacing: 2, color: T.mute, fontWeight: 600, marginBottom: 8 }}>THE LANGUAGE · LOCKED</div>
              <ul style={{ margin: 0, padding: 0, listStyle: 'none', display: 'grid', gap: 7 }}>
                <li><b>Paper objects</b> — each card is a paper thing (docket, folder, slip, bookmark), told apart by shape + a line-art glyph.</li>
                <li><b>One voice colour</b> — <span style={{ color: T.goldDeep, fontWeight: 600 }}>ochre</span> marks Vesper-authored intelligence (the “sacred” signal). <span style={{ color: '#3D5066', fontWeight: 600 }}>Ink-blue</span> marks <i>your</i> call. <span style={{ color: '#A04030', fontWeight: 600 }}>Oxblood</span> only when it can’t wait.</li>
                <li><b>No coloured spines, no violet</b> — earlier Ledger/violet exploration is retired. Colour appears only where it carries meaning.</li>
              </ul>
            </div>
          </div>
        </DCArtboard>
      </DCSection>

      {/* ── THE SEVEN FAMILIES ── */}
      <DCSection id="families" title="The seven families" subtitle="One card per interaction family. Each spec covers anatomy, copy, actions, states, and when it appears.">
        <DCArtboard id="f1" label="1 · Needs your call" width={425} height={300} bg="transparent"><Center><Stage><CardCall/></Stage></Center></DCArtboard>
        <DCArtboard id="f1s" label="1 · spec" width={400} height={520} bg="transparent">
          <CardSpec name="Needs your call"
            anatomy="Docket card. Kind tag + deadline stamp · serif headline · one-line italic rationale · Why-this chip + primary."
            hierarchy="Decision verb leads. Deadline secondary but always visible. Body one line max."
            copy="“A ryokan for Tokyo, nights 5–7.” / “I narrowed forty-seven down to three.”"
            actions="Primary: Choose. Secondary: not now. Why-this opens reasoning."
            states="Loading: skeleton w/ spine. Empty: never shown empty — if nothing needs a call, absent."
            when="A real decision is pending with a deadline or blocking downstream planning. Max one in the Now slot."
            sheet="DECISION SHEET — needs deliberation."/>
        </DCArtboard>

        <DCArtboard id="f2" label="2 · Vesper prepared" width={425} height={340} bg="transparent"><Center><Stage><CardPrepared/></Stage></Center></DCArtboard>
        <DCArtboard id="f2s" label="2 · spec" width={400} height={520} bg="transparent">
          <CardSpec name="Vesper prepared"
            anatomy="Folder/dossier. File-tab header w/ kind tag + count · serif title · 3-line table-of-contents preview · open primary."
            hierarchy="Feels like a finished object. Preview proves the work exists. Title + contents over actions."
            copy="“Tokyo, in May — a quiet itinerary.” TOC: ‘Land soft · Yanaka, no alarms’…"
            actions="Primary: Open the draft. Secondary: skim, not now."
            states="Loading: ‘Vesper is drafting…’ w/ progress. Empty: folds into Starter."
            when="Vesper has produced a reviewable work product (brief, shortlist, retrospective, Atlas artifact)."
            sheet="DIRECTLY into the object — made to be viewed, not decided."/>
        </DCArtboard>

        <DCArtboard id="f3" label="3 · Live companion" width={425} height={320} bg="transparent"><Center><Stage><CardLive/></Stage></Center></DCArtboard>
        <DCArtboard id="f3s" label="3 · spec" width={400} height={520} bg="transparent">
          <CardSpec name="Live companion"
            anatomy="Present-tense card. Place + inline weather · serif headline about the moment · one situational suggestion · in/walk-me actions."
            hierarchy="Glanceable. The moment (open hour / weather shift) leads; suggestion supports."
            copy="“You have an open hour.” / “Kayaba Coffee is 8 minutes east…”"
            actions="Primary: I’m in. Secondary: walk me there, else?"
            states="Loading: place + time skeleton. Empty: shows daily brief when nothing situational."
            when="During a trip, or weather/time materially affects today. The Now card while travelling."
            sheet="DIRECTLY — it’s about acting now, not deliberating."/>
        </DCArtboard>

        <DCArtboard id="f4" label="4 · Signal / pattern" width={425} height={300} bg="transparent"><Center><Stage><CardSignal/></Stage></Center></DCArtboard>
        <DCArtboard id="f4s" label="4 · spec" width={400} height={520} bg="transparent">
          <CardSpec name="Signal / pattern"
            anatomy="Quiet interpretive card. Vesper mark + tag · larger serif observation · ‘What I saw’ chip + soft yes."
            hierarchy="The observation IS the card. No metrics, no charts. Explanation one tap away, never forced."
            copy="“You keep choosing quiet neighborhoods before the landmarks — Alfama, Yanaka, Ribeira.”"
            actions="Primary: Yes (lean in). Secondary: What I saw. Tune in sheet."
            states="Loading: rare — patterns precompute. Empty: absent until confidence threshold met."
            when="A taste pattern crosses a confidence threshold. Low frequency — at most one per session."
            sheet="DECISION SHEET — ‘Why this’ + ‘Tune’ live there."/>
        </DCArtboard>

        <DCArtboard id="f5" label="5 · Capture / memory" width={425} height={300} bg="transparent"><Center><Stage><CardCapture/></Stage></Center></DCArtboard>
        <DCArtboard id="f5s" label="5 · spec" width={400} height={520} bg="transparent">
          <CardSpec name="Capture / memory"
            anatomy="Photo-slip card. Tilted photo on the left · kind tag · serif title · italic count · keep/later."
            hierarchy="Emotionally soft. The image leads; copy gentle and optional. Never urgent."
            copy="“Williamsburg, sunday.” / “twelve photos — could become a postcard.”"
            actions="Primary: Keep it (→ Atlas). Secondary: later. Dismiss never destroys."
            states="Loading: photo shimmer. Empty: silent — only appears with real material."
            when="Just back from a trip, or a photo/place cluster forms. Hands off to Atlas."
            sheet="DIRECTLY to a light keep-flow; no heavy sheet."/>
        </DCArtboard>

        <DCArtboard id="f6" label="6 · Resume thread" width={425} height={300} bg="transparent"><Center><Stage><CardResume/></Stage></Center></DCArtboard>
        <DCArtboard id="f6s" label="6 · spec" width={400} height={520} bg="transparent">
          <CardSpec name="Resume thread"
            anatomy="Bookmark card. Kind tag + trip·time · a quoted last line on a left rule · ‘pick it up’."
            hierarchy="Continuity, not inbox. One quoted fragment stands in for the whole thread."
            copy="“…where to stay near Yanaka, somewhere quiet —” / ‘you left it mid-thought’"
            actions="Primary: Pick it up. No secondary — a single continuation."
            states="Loading: quote skeleton. Empty: absent if no open threads."
            when="An unfinished conversation exists and is still relevant (recent, trip live)."
            sheet="DIRECTLY back into the thread."/>
        </DCArtboard>

        <DCArtboard id="f7" label="7 · Starter" width={425} height={300} bg="transparent"><Center><Stage><CardStarter/></Stage></Center></DCArtboard>
        <DCArtboard id="f7s" label="7 · spec" width={400} height={520} bg="transparent">
          <CardSpec name="Starter / cold start"
            anatomy="Dashed invitation. Kind tag · generous serif prompt · 3 example chips + a voice chip."
            hierarchy="Generous, not homework. One ask: name a place. Examples lower the barrier."
            copy="“Tell me one place you’ve loved.” / “That’s all I need to begin.”"
            actions="Tap a chip, type, or say it (voice). No skip — nothing to skip."
            states="This IS the empty state for the whole surface. Loading: n/a."
            when="No trips, no history, or a deliberately cleared desk. The cold-start home."
            sheet="DIRECTLY to composer / voice."/>
        </DCArtboard>
      </DCSection>

      {/* ── NOW vs RAIL ── */}
      <DCSection id="nowrail" title="Now card vs Next Moves rail" subtitle="One full paper object up top, a glyph-led rail beneath. The recommended composition.">
        <DCArtboard id="nr-phone" label="Home composition" width={415} height={870} bg="transparent">
          <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100%' }}><NowAndRail/></div>
        </DCArtboard>
        <DCArtboard id="nr-notes" label="Now vs rail logic" width={460} height={870} bg="transparent">
          <div style={{ width: 420, padding: '36px 28px', background: '#F1ECE2', borderRadius: 8 }}>
            <CEB>NOW vs NEXT MOVES</CEB>
            <CH2>One object, then a rail.</CH2>
            <div style={{ borderTop: `0.5px solid ${T.hairline}`, paddingTop: 14 }}>
              <CBody><b>The Now card</b> is a single full paper object — whichever family is most urgent right now. Priority: <i>Needs-your-call</i> &gt; <i>Live</i> (if travelling) &gt; <i>Vesper prepared</i> &gt; everything else. Only ever one. It earns the width.</CBody>
              <CBody><b>Next Moves</b> is a horizontal rail of compact paper cards (see the four treatments — the left-spine is retired in favour of <b>glyph-led, ink-only</b> cards). Up to ~5, lazy-loaded. Mixed families, ordered by freshness × importance.</CBody>
              <CBody><b>The hybrid</b>: paper objects for the hero, glyph-led paper cards for the rail. No coloured spines — colour only appears where it means something (ochre = Vesper, ink-blue = your call).</CBody>
              <div style={{ marginTop: 12, padding: 12, background: '#FBF7EC', borderRadius: 8, fontSize: 11.5, color: T.mute }}>
                <b style={{ color: T.ink }}>Rules</b><br/>
                · Never two Needs-your-call in the Now slot — the second goes to the rail with a count.<br/>
                · Signal/pattern never takes the Now slot — too quiet to lead.<br/>
                · If nothing qualifies, the lead note + Starter fills the hero.
              </div>
            </div>
          </div>
        </DCArtboard>
      </DCSection>

      {/* ── RAIL CARD · CANONICAL ── */}
      <DCSection id="rail" title="Next Moves · the rail card" subtitle="Glyph-led, ink only. No coloured spine — the line-art glyph signals the kind; ochre sparkle marks Vesper-authored.">
        <DCArtboard id="rail-strip" label="The rail" width={720} height={230} bg="transparent">
          <div style={{ padding: '20px 16px' }}>
            <div style={{ fontSize: 9.5, letterSpacing: 2, color: T.mute, fontWeight: 700, marginBottom: 10 }}>NEXT MOVES</div>
            <RailStrip Comp={RailGlyph}/>
          </div>
        </DCArtboard>
        <DCArtboard id="rail-anatomy" label="Anatomy" width={400} height={400} bg="transparent">
          <div style={{ width: 380, padding: '28px 26px', background: '#F1ECE2', borderRadius: 8 }}>
            <CEB>RAIL CARD · ANATOMY</CEB>
            <CH2>One glyph, then the work.</CH2>
            <div style={{ borderTop: `0.5px solid ${T.hairline}`, paddingTop: 12 }}>
              <SpecLine k="GLYPH">Line-art kind mark, top-left, ink. The only kind signal.</SpecLine>
              <SpecLine k="MARK">Ochre sparkle, top-right — Vesper-authored only.</SpecLine>
              <SpecLine k="TITLE">Cormorant 15.5 / 500 — the work, one line.</SpecLine>
              <SpecLine k="META">Italic serif 11 — count or context.</SpecLine>
              <SpecLine k="ACTION">One verb + arrow, ink-soft, bottom.</SpecLine>
              <SpecLine k="SIZE">214 w · min 120 h · 12 radius · 8 gap.</SpecLine>
            </div>
            <div style={{ marginTop: 12, padding: 12, background: '#FBF7EC', borderRadius: 8, fontSize: 11.5, color: T.mute }}>
              No coloured left edge, no footer tint, no dog-ear. Colour stays out of the rail entirely — it only earns a place on the Now card and in the kind tag of the decision sheet.
            </div>
          </div>
        </DCArtboard>
      </DCSection>

      {/* ── DECISION SHEET ── */}
      <DCSection id="sheet" title="The decision sheet" subtitle="For cards that need deliberation. Six fixed zones — and the rule for which cards open it vs open directly.">
        <DCArtboard id="sheet-mock" label="Decision sheet" width={425} height={640} bg="transparent">
          <div style={{ display: 'flex', justifyContent: 'center', paddingTop: 10 }}><DecisionSheet/></div>
        </DCArtboard>
        <DCArtboard id="sheet-notes" label="Open direct vs sheet" width={460} height={640} bg="transparent">
          <div style={{ width: 420, padding: '36px 28px', background: '#F1ECE2', borderRadius: 8 }}>
            <CEB>OPEN BEHAVIOUR</CEB>
            <CH2>Sheet, or straight in.</CH2>
            <div style={{ borderTop: `0.5px solid ${T.hairline}`, paddingTop: 14 }}>
              <CBody>The sheet’s six zones: <b>I noticed</b> (the evidence) · <b>My read</b> (Vesper’s opinion) · <b>Best next step</b> (the primary) · then <b>Ask Vesper</b> · <b>Tune</b> · <b>Not now</b>. Explanation is present but never forced — you can act from the card without ever opening it.</CBody>
              <div style={{ marginTop: 6 }}>
                {[
                  ['Needs your call', 'SHEET', 'deliberation, tradeoffs'],
                  ['Signal / pattern', 'SHEET', 'why + tune live here'],
                  ['Vesper prepared', 'DIRECT', 'open the object'],
                  ['Live companion', 'DIRECT', 'act now'],
                  ['Capture / memory', 'DIRECT', 'light keep-flow'],
                  ['Resume thread', 'DIRECT', 'back into thread'],
                  ['Starter', 'DIRECT', 'composer / voice'],
                ].map(([a, b, c]) => (
                  <div key={a} style={{ display: 'grid', gridTemplateColumns: '120px 56px 1fr', gap: 8, padding: '8px 0', borderTop: `0.5px solid ${T.hairThin}`, alignItems: 'baseline' }}>
                    <span style={{ fontFamily: T.serif, fontSize: 13.5, color: T.ink, fontWeight: 500 }}>{a}</span>
                    <span style={{ fontSize: 9, letterSpacing: 1.2, fontWeight: 700, color: b === 'SHEET' ? TR.ink : T.goldDeep }}>{b}</span>
                    <span style={{ fontSize: 11, color: T.mute, fontStyle: 'italic', fontFamily: T.serif }}>{c}</span>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </DCArtboard>
      </DCSection>

      {/* ── STATES ── */}
      <DCSection id="states" title="Loading & empty" subtitle="Cards never show a hollow 'no data' state — they're either present with real work, loading, or absent.">
        <DCArtboard id="st-load" label="Loading" width={425} height={280} bg="transparent"><Center><Stage><CardLoading fam="call"/></Stage></Center></DCArtboard>
        <DCArtboard id="st-prep" label="Preparing (Vesper drafting)" width={425} height={280} bg="transparent">
          <Center><Stage>
            <CardShell fam="prepared" style={{ padding: 16 }}>
              <KindTag fam="prepared"/>
              <div style={{ marginTop: 12, display: 'flex', alignItems: 'center', gap: 10 }}>
                <div style={{ display: 'flex', gap: 3 }}>
                  {[0,1,2].map(i => <span key={i} style={{ width: 6, height: 6, borderRadius: 6, background: T.gold, opacity: 0.3 + i * 0.25 }}/>)}
                </div>
                <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 15, color: T.inkSoft }}>Vesper is drafting your Tokyo itinerary…</span>
              </div>
              <div style={{ marginTop: 12, fontFamily: T.mono, fontSize: 9, color: T.muteSoft, letterSpacing: 1.2 }}>~18 MIN · 3 OF 6 STOPS</div>
            </CardShell>
          </Stage></Center>
        </DCArtboard>
        <DCArtboard id="st-empty" label="Empty → Starter" width={425} height={280} bg="transparent"><Center><Stage><CardEmpty title="Nothing needs you right now." sub="I’ll surface things as they’re ready."/></Stage></Center></DCArtboard>
        <DCArtboard id="st-notes" label="State logic" width={400} height={280} bg="transparent">
          <div style={{ width: 380, padding: '28px 26px', background: '#F1ECE2', borderRadius: 8 }}>
            <CEB>STATES</CEB>
            <CH2>Present, loading, or gone.</CH2>
            <CBody>No hollow “no data” widgets. A card is <b>present</b> (real work), <b>loading</b> (skeleton with its spine colour), <b>preparing</b> (Vesper actively drafting, with progress), or <b>absent</b>. The only persistent empty state is the Starter — and that’s an invitation, not an error.</CBody>
          </div>
        </DCArtboard>
      </DCSection>

      {/* ── IMPLEMENTATION ── */}
      <DCSection id="impl" title="Implementation notes" subtitle="Sizes, type, colour, icon, motion.">
        <DCArtboard id="impl-card" label="Tokens & specs" width={900} height={560} bg="#F1ECE2">
          <div style={{ padding: 40, fontFamily: T.sans, color: T.inkSoft, fontSize: 13, lineHeight: 1.5 }}>
            <CEB>IMPLEMENTATION</CEB>
            <CH2>Build notes.</CH2>
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 26, marginTop: 8 }}>
              <div>
                <SpecHead>SIZE & SPACING</SpecHead>
                <SpecLine k="Now card">361 w (16 margins) · 14 radius · 16 pad</SpecLine>
                <SpecLine k="Rail card">214 w · min 120 h · 12 radius · 13–14 pad · 8 gap</SpecLine>
                <SpecLine k="Rail glyph">line-art kind mark, 19 px ink, top-left</SpecLine>
                <SpecLine k="Sheet">393 w · 28 radius top · zones 16 pad</SpecLine>
                <SpecLine k="Hit target">44 px min on all actions</SpecLine>
                <SpecHead mt>TYPE</SpecHead>
                <SpecLine k="Title">Cormorant 20–22 / 500 / -0.4</SpecLine>
                <SpecLine k="Body">Cormorant 13–14 italic for rationale</SpecLine>
                <SpecLine k="Kind tag">DM Sans 9 / 700 / 1.5 ls caps</SpecLine>
                <SpecLine k="Meta/date">JetBrains Mono 9 / 1.2 ls</SpecLine>
                <SpecLine k="Dynamic type">titles scale to 28; rail reflows to 1-up list past XL</SpecLine>
              </div>
              <div>
                <SpecHead>COLOUR</SpecHead>
                <SpecLine k="Paper">#EFEAE0 bg · #F7F2E7 card</SpecLine>
                <SpecLine k="Ink">#1B1714 / soft #2C2622 / mute #86807A</SpecLine>
                <SpecLine k="Call spine">ink-blue #3D5066</SpecLine>
                <SpecLine k="Vesper">ochre #B0853A — sparkle + authored cards</SpecLine>
                <SpecLine k="Pattern">sage #7C8F73 — used in tag dot only</SpecLine>
                <SpecLine k="Urgent">oxblood #A04030 — only true time-pressure</SpecLine>
                <SpecHead mt>ICON & MOTION</SpecHead>
                <SpecLine k="Glyphs">1.3–1.4 stroke line-art, 20 px, per kind</SpecLine>
                <SpecLine k="Vesper mark">sparkle only on Vesper-authored</SpecLine>
                <SpecLine k="Pressed">scale .98 + shadow collapse, 120 ms</SpecLine>
                <SpecLine k="Enter">8 px rise + fade, 200 ms, stagger 40 ms</SpecLine>
                <SpecLine k="Dismiss">slide + height collapse, never a destructive flash</SpecLine>
              </div>
            </div>
            <div style={{ borderTop: `0.5px solid ${T.hairline}`, marginTop: 20, paddingTop: 14, display: 'flex', gap: 12, flexWrap: 'wrap' }}>
              <a href="Vesper Home.html" style={{ padding: '7px 12px', background: '#FBF7EC', border: '0.5px solid rgba(27,23,20,0.10)', borderRadius: 999, color: T.ink, textDecoration: 'none', fontSize: 12, fontWeight: 500 }}>← Vesper home (modes)</a>
              <a href="Vesper Trips Full.html" style={{ padding: '7px 12px', background: '#FBF7EC', border: '0.5px solid rgba(27,23,20,0.10)', borderRadius: 999, color: T.ink, textDecoration: 'none', fontSize: 12, fontWeight: 500 }}>Trips · full system →</a>
            </div>
          </div>
        </DCArtboard>
      </DCSection>

      {/* ── HANDOFF SUMMARY ── */}
      <DCSection id="rec" title="The system · for handoff" subtitle="Locked decisions, in one place.">
        <DCArtboard id="rec-card" label="Locked" width={760} height={560} bg="#F1ECE2">
          <div style={{ padding: 40, fontFamily: T.sans, color: T.inkSoft, fontSize: 13.5, lineHeight: 1.55 }}>
            <CEB>FOR HANDOFF</CEB>
            <CH2>One language, locked.</CH2>
            <CBody w={640}>
              <b>Paper objects</b> everywhere — the Now card is a full paper object; the Next Moves rail
              is glyph-led paper cards. No coloured spines, no Ledger, no violet. Colour is meaning, not
              decoration.
            </CBody>
            <div style={{ borderTop: `0.5px solid ${T.hairline}`, marginTop: 6, paddingTop: 14 }}>
              <div style={{ fontSize: 10, letterSpacing: 2, color: T.mute, fontWeight: 600, marginBottom: 10 }}>DECISIONS</div>
              <ul style={{ margin: 0, padding: 0, listStyle: 'none', display: 'grid', gap: 8 }}>
                <li><b>Composition</b> — one lead note, one Now card, a glyph-led Next Moves rail (~5, lazy).</li>
                <li><b>Now priority</b> — Needs-your-call &gt; Live (if travelling) &gt; Vesper prepared &gt; rest. Never two calls; pattern never leads.</li>
                <li><b>Colour</b> — <span style={{ color: T.goldDeep, fontWeight: 600 }}>ochre</span> = Vesper voice · <span style={{ color: '#3D5066', fontWeight: 600 }}>ink-blue</span> = your call · <span style={{ color: '#A04030', fontWeight: 600 }}>oxblood</span> = time-pressure only. Everything else is ink on paper.</li>
                <li><b>Open behaviour</b> — Call &amp; Pattern open the decision sheet; Prepared, Live, Capture, Resume, Starter open directly.</li>
                <li><b>States</b> — present · loading · preparing (with progress) · absent. No hollow “no data”. Starter is the only standing empty state.</li>
              </ul>
            </div>
            <div style={{ borderTop: `0.5px solid ${T.hairline}`, marginTop: 14, paddingTop: 14 }}>
              <div style={{ fontSize: 10, letterSpacing: 2, color: T.mute, fontWeight: 600, marginBottom: 8 }}>IN ONE LINE</div>
              <p style={{ margin: 0, fontFamily: T.serif, fontSize: 18, color: T.ink, lineHeight: 1.4, letterSpacing: -0.2 }}>
                Paper hero, glyph rail, ochre for Vesper, ink-blue for your call, oxblood only when it can’t wait.
              </p>
            </div>
            <div style={{ borderTop: `0.5px solid ${T.hairline}`, marginTop: 14, paddingTop: 14, display: 'flex', gap: 12, flexWrap: 'wrap' }}>
              <a href="Vesper Home.html" style={{ padding: '7px 12px', background: '#FBF7EC', border: '0.5px solid rgba(27,23,20,0.10)', borderRadius: 999, color: T.ink, textDecoration: 'none', fontSize: 12, fontWeight: 500 }}>← Vesper home (modes)</a>
              <a href="Vesper Trips Full.html" style={{ padding: '7px 12px', background: '#FBF7EC', border: '0.5px solid rgba(27,23,20,0.10)', borderRadius: 999, color: T.ink, textDecoration: 'none', fontSize: 12, fontWeight: 500 }}>Trips · full system →</a>
            </div>
          </div>
        </DCArtboard>
      </DCSection>

      {/* ── CHAT CARDS — conversation artifacts (1:1 vs group) ── */}
      {ChatSections()}

    </DesignCanvas>
  );
}

ReactDOM.createRoot(document.getElementById('root')).render(<CardsApp/>);
