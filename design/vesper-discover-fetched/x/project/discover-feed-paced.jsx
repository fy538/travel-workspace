// ═══════════════════════════════════════════════════════════════
// DISCOVER · PACED FEED — the "read + feed" scroll, given rhythm so
// it stops reading monotone. Cadenced card shapes + Vesper interludes
// + lens chapters + one full-bleed punctuation. Reuses discover-kit /
// discover-feed / discover-read globals (ScrollFrame, FeedLead,
// FeedRow, FeedSection, BriefingMast, Plate, LensChip, D, T).
// ═══════════════════════════════════════════════════════════════

// a Vesper pull-quote interlude — a rest between sections, no card
function Interlude({ children }) {
  return (
    <div style={{ padding: '24px 30px 6px', textAlign: 'center' }}>
      <div style={{ fontFamily: T.mono, fontSize: 8.5, letterSpacing: 2, color: D.vesper, fontWeight: 700 }}>VESPER</div>
      <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 18, color: T.ink, lineHeight: 1.4, letterSpacing: -0.2, margin: '8px 0 0' }}>{children}</p>
    </div>
  );
}

// a full-bleed immersive punctuation card (the Desire-Engine beat)
function FullBleed({ v, lens, line }) {
  return (
    <div style={{ padding: '20px 16px 0' }}>
      <div style={{ position: 'relative', height: 200, borderRadius: 16, overflow: 'hidden' }}>
        <Plate variant={v} style={{ position: 'absolute', inset: 0 }} dim={0.5}/>
        <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to top, rgba(20,14,9,0.82), rgba(20,14,9,0.1) 60%)' }}/>
        <div style={{ position: 'absolute', left: 16, right: 16, bottom: 15 }}>
          <span style={{ display: 'inline-block', fontSize: 9, letterSpacing: 1.4, fontWeight: 700, color: 'rgba(255,255,255,0.85)', marginBottom: 8 }}>{lens.toUpperCase()}</span>
          <div style={{ fontFamily: T.serif, fontSize: 22, fontWeight: 500, color: '#fff', letterSpacing: -0.4, lineHeight: 1.1 }}>{line}</div>
        </div>
      </div>
    </div>
  );
}

// a side-by-side duo — two compact cards in a row (breaks the column)
function Duo({ items }) {
  return (
    <div style={{ display: 'flex', gap: 10 }}>
      {items.map(([v, lens, title]) => (
        <div key={title} style={{ flex: 1, background: T.cardWarm, borderRadius: 13, border: `0.5px solid ${T.hairline}`, overflow: 'hidden' }}>
          <Plate variant={v} style={{ height: 78 }}/>
          <div style={{ padding: '9px 11px 12px' }}>
            <div style={{ fontSize: 8.5, letterSpacing: 1.2, fontWeight: 700, color: D.vesper }}>{lens.toUpperCase()}</div>
            <div style={{ fontFamily: T.serif, fontSize: 13.5, fontWeight: 500, color: T.ink, letterSpacing: -0.2, lineHeight: 1.2, marginTop: 5 }}>{title}</div>
          </div>
        </div>
      ))}
    </div>
  );
}

// ─── A · CHAPTERED — masthead → lens chapters with interludes ───
function PacedFeedA() {
  return (
    <ScrollFrame>
      <BriefingMast/>
      <FeedSection label="WHY HERE" right="3 READS">
        <FeedLead v="rooftop" lens="Why here" title="Read the city from its miradouros" hook="the evening unfolds viewpoint to viewpoint — here’s the order I’d walk them."/>
        <FeedRow v="tiles" lens="Ritual" title="What the azulejos tell you" meta="4 MIN READ"/>
      </FeedSection>
      <Interlude>Lisbon rewards the slow — the best of it is off the monument trail.</Interlude>
      <FeedSection label="A DAY IN · ALFAMA">
        <Duo items={[['alley', 'A day in', 'Morning in Alfama'], ['table', 'Insider', 'Where locals lunch']]}/>
      </FeedSection>
      <FullBleed v="coast" lens="For the obsessed" line="Cascais, after the light goes amber."/>
      <FeedSection label="THE DEBATE" right="ONE TAKE">
        <FeedRow v="market" lens="The debate" title="Time Out Market — worth it, or not?" meta="VESPER’S CALL"/>
      </FeedSection>
    </ScrollFrame>
  );
}

// ─── B · DENSER — punchier cadence, full-bleed up high ──────────
function PacedFeedB() {
  return (
    <ScrollFrame>
      <BriefingMast/>
      <FullBleed v="rooftop" lens="Why here" line="The viewpoints are the plan."/>
      <FeedSection label="WORTH READING">
        <FeedRow v="tiles" lens="Ritual" title="What the azulejos tell you" meta="4 MIN"/>
        <FeedRow v="alley" lens="A day in" title="Morning in Alfama, hour by hour" meta="6 MIN"/>
      </FeedSection>
      <Interlude>Skip the castle queue. Spend that hour at a table instead.</Interlude>
      <FeedSection label="ONE TABLE TO BOOK">
        <FeedLead v="table" lens="Insider" title="The dinner I’d hold early" hook="book it for 7 — by 9 the room turns touristy."/>
      </FeedSection>
      <FeedSection label="STILL DECIDING">
        <Duo items={[['market', 'The debate', 'Time Out Market?'], ['coast', 'Detour', 'Cascais day trip?']]}/>
      </FeedSection>
    </ScrollFrame>
  );
}

// ─── C · TEXT-FORWARD — interludes lead, photos punctuate ───────
function PacedFeedC() {
  return (
    <ScrollFrame>
      <BriefingMast/>
      <Interlude>Three places worth the walk — and one to skip.</Interlude>
      <FeedSection label="WHY HERE">
        <FeedRow v="rooftop" lens="Why here" title="The miradouro order I’d walk" meta="5 MIN"/>
        <FeedRow v="tiles" lens="Ritual" title="Reading a building by its tiles" meta="4 MIN"/>
      </FeedSection>
      <FullBleed v="alley" lens="A day in" line="Alfama, before the trams wake."/>
      <FeedSection label="ONE TO BOOK">
        <FeedLead v="table" lens="Insider" title="Hold this table for 7pm" hook="the room turns by nine — go early, stay long."/>
      </FeedSection>
      <Interlude>Skip the market hall. The neighbourhood does it better.</Interlude>
      <FeedSection label="IF YOU HAVE A DAY">
        <Duo items={[['coast', 'Detour', 'Cascais by train'], ['market', 'The debate', 'Sintra, early']]}/>
      </FeedSection>
    </ScrollFrame>
  );
}

Object.assign(window, { PacedFeedA, PacedFeedB, PacedFeedC, Interlude, FullBleed, Duo });
