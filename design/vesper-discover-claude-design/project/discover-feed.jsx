// ═══════════════════════════════════════════════════════════════
// DISCOVER FEED — the body below Vesper's Read. Curated, finite,
// context-tinted. Shown as a full tall scroll for two contexts.
// Reuses discover-kit (Plate, LensChip, VesperBy, FieldEyebrow, D,
// SectionLabel, DIcon, Spark, SegControl) + discover-read (DiscoverTop,
// ReadFrame, ReadLine, STANCE).
// ═══════════════════════════════════════════════════════════════

// A compact curated dossier card for the feed (row form).
function FeedRow({ v, lens, title, meta }) {
  return (
    <div style={{ display: 'flex', gap: 12, alignItems: 'center' }}>
      <Plate variant={v} style={{ width: 72, height: 72, borderRadius: 10, flexShrink: 0 }}/>
      <div style={{ flex: 1, minWidth: 0 }}>
        <div style={{ fontSize: 9, letterSpacing: 1.4, fontWeight: 700, color: D.vesper }}>{lens.toUpperCase()}</div>
        <div style={{ fontFamily: T.serif, fontSize: 14.5, fontWeight: 500, color: T.ink, letterSpacing: -0.2, lineHeight: 1.2, marginTop: 4 }}>{title}</div>
        <div style={{ marginTop: 5, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
          <span style={{ fontFamily: T.mono, fontSize: 8.5, color: T.muteSoft, letterSpacing: 1 }}>{meta}</span>
          <VesperBy/>
        </div>
      </div>
    </div>
  );
}

// A wide lead feed card (photo on top).
function FeedLead({ v, lens, title, hook }) {
  return (
    <div style={{ background: T.cardWarm, borderRadius: 14, border: `0.5px solid ${T.hairline}`, overflow: 'hidden', boxShadow: '0 1px 0 rgba(255,255,255,0.6) inset' }}>
      <Plate variant={v} style={{ height: 116 }} dim={0.05}>
        <div style={{ position: 'absolute', top: 10, left: 10 }}><LensChip lens={lens} onDark/></div>
      </Plate>
      <div style={{ padding: '12px 14px 14px' }}>
        <FieldEyebrow/>
        <div style={{ fontFamily: T.serif, fontSize: 17, fontWeight: 500, color: T.ink, letterSpacing: -0.3, lineHeight: 1.2, marginTop: 7 }}>{title}</div>
        <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12.5, color: T.mute, lineHeight: 1.35, marginTop: 5 }}>{hook}</div>
      </div>
    </div>
  );
}

function FeedSection({ label, right, children }) {
  return (
    <div style={{ padding: '20px 22px 0' }}>
      <SectionLabel right={right}>{label}</SectionLabel>
      <div style={{ marginTop: 12, display: 'flex', flexDirection: 'column', gap: 14 }}>{children}</div>
    </div>
  );
}

// ─── A tall scroll frame (phone-width, content-height, faux chrome) ──
function ScrollFrame({ children }) {
  return (
    <div style={{
      width: 393, background: T.bg, borderRadius: 30, overflow: 'hidden',
      border: `0.5px solid ${T.hairline}`, boxShadow: '0 30px 60px -30px rgba(0,0,0,0.3)',
      position: 'relative', paddingBottom: 8,
    }}>
      {/* faux status bar */}
      <div style={{ height: 40, display: 'flex', alignItems: 'flex-end', justifyContent: 'space-between', padding: '0 24px 4px' }}>
        <span style={{ fontFamily: '-apple-system, system-ui', fontWeight: 600, fontSize: 14, color: T.ink }}>9:41</span>
        <span style={{ fontSize: 10, color: T.muteSoft, letterSpacing: 1.2, fontWeight: 600 }}>SCROLL ↓</span>
      </div>
      {children}
      {/* end-of-feed marker — curated, finite */}
      <div style={{ padding: '22px 22px 18px', textAlign: 'center' }}>
        <div style={{ display: 'inline-flex', alignItems: 'center', gap: 8, color: T.muteSoft }}>
          <span style={{ width: 18, height: 1, background: T.muteSoft, opacity: 0.5 }}/>
          <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12, color: T.mute }}>that’s what matters here — not everything</span>
          <span style={{ width: 18, height: 1, background: T.muteSoft, opacity: 0.5 }}/>
        </div>
      </div>
    </div>
  );
}

// Masthead read cards (just the ReadFrame, for embedding in a scroll).
function BriefingMast() {
  return (
    <div style={{ padding: '4px 16px 0' }}>
      <ReadFrame place="Lisbon" kicker="VESPER’S READ · BEFORE YOU GO" updated="FOR MAY 18–24">
        <div style={{ padding: '10px 16px 4px' }}>
          <p style={{ fontFamily: T.serif, fontSize: 17, fontWeight: 500, color: T.ink, letterSpacing: -0.2, lineHeight: 1.3, margin: 0 }}>
            The city is read from its <span style={{ fontStyle: 'italic' }}>viewpoints</span>, not its monuments.
          </p>
        </div>
        <div style={{ padding: '2px 16px 12px' }}>
          <ReadLine tag="MATTERS" color={STANCE.matters} lens="Why here" first>Miradouro culture — plan your evenings around them.</ReadLine>
          <ReadLine tag="NOTICE" color={STANCE.notice} lens="Ritual">Tilework dates a building better than any plaque.</ReadLine>
          <ReadLine tag="TIMELY" color={STANCE.timely} lens="Insider">Santo António’s feast lands in your window.</ReadLine>
        </div>
      </ReadFrame>
    </div>
  );
}
function ProximityMast() {
  return (
    <div style={{ padding: '4px 16px 0' }}>
      <ReadFrame place="Alfama" kicker="VESPER’S READ · NEAR YOU NOW" updated="LIVE">
        <div style={{ padding: '12px 16px 0', display: 'flex', gap: 12, alignItems: 'center' }}>
          <Plate variant="alley" style={{ width: 78, height: 78, borderRadius: 12, flexShrink: 0 }}/>
          <div>
            <div style={{ display: 'inline-flex', alignItems: 'center', gap: 5, padding: '3px 9px', borderRadius: 999, background: 'rgba(61,80,102,0.10)', fontSize: 9, letterSpacing: 1.2, fontWeight: 700, color: '#3D5066' }}>
              <span style={{ width: 5, height: 5, borderRadius: 5, background: '#3D5066' }}/> 6 MIN ON FOOT
            </div>
            <p style={{ fontFamily: T.serif, fontSize: 16.5, fontWeight: 500, color: T.ink, letterSpacing: -0.2, lineHeight: 1.25, margin: '8px 0 0' }}>
              You’re a block from the one I’d send you to.
            </p>
          </div>
        </div>
        <div style={{ padding: '6px 16px 12px' }}>
          <ReadLine tag="NOW" color={STANCE.near} lens="Ritual" first>Bica at Pois, Café — before the 11am crowd.</ReadLine>
          <ReadLine tag="LIGHT" color={STANCE.notice} lens="Why here">Portas do Sol glows best in the next hour.</ReadLine>
        </div>
      </ReadFrame>
    </div>
  );
}

// Pinned tab bar (visual) for the scroll frame.
function ScrollTabs() {
  return (
    <div style={{ margin: '14px 16px 4px', background: 'rgba(247,242,231,0.92)', borderRadius: 26, border: `0.5px solid ${T.hairline}`, boxShadow: '0 8px 24px -8px rgba(0,0,0,0.12)', display: 'flex', justifyContent: 'space-between', padding: '11px 22px' }}>
      {['Trips','Vesper','Discover','Atlas'].map((t,i)=>(
        <span key={t} style={{ fontSize: 11, fontWeight: i===2?700:500, color: i===2?T.ink:T.muteSoft, letterSpacing: 0.2 }}>{t}</span>
      ))}
    </div>
  );
}

function DiscoverScrollPretrip() {
  return (
    <ScrollFrame>
      <DiscoverTop place="Lisbon" context="Lisbon · in 3 weeks" active={1}/>
      <div style={{ height: 12 }}/>
      <BriefingMast/>
      <FeedSection label="WORTH THE WALK FROM ALFAMA" right="NEAR YOUR STAY">
        <FeedRow v="coast" lens="A day in" title="Graça, before the morning fills it" meta="LISBON · 4 MIN"/>
        <FeedRow v="square" lens="Insider" title="The cervejaria locals still queue for" meta="LISBON · 3 MIN"/>
      </FeedSection>
      <FeedSection label="THE DEBATE, THIS MONTH" right="VESPER">
        <FeedHero v="alley" lens="The debate" title="Is Intendente over, or just honest now?" hook="Vesper takes a side — and tells you what changed."/>
      </FeedSection>
      <FeedSection label="ONE TABLE TO BOOK NOW" right="FILLS EARLY">
        <FeedRow v="tiles" lens="Insider" title="The tasca that only takes a week's notice" meta="LISBON · BOOK BY MAY 11"/>
      </FeedSection>
      <FeedSection label="READ BEFORE YOU GO" right="3 NOTES">
        <FeedLead v="hills" lens="Why here" title="Why Lisbon rewards the slow walker" hook="The hills are the point, not the obstacle."/>
        <FeedRow v="coast" lens="Ritual" title="The bica, and the right way to take it" meta="2 MIN READ"/>
        <FeedRow v="square" lens="For the obsessed" title="Azulejo tilework, decoded by parish" meta="6 MIN READ"/>
      </FeedSection>
      <FeedSection label="IF YOU HAVE A SPARE DAY" right="DAY TRIP">
        <FeedLead v="coast" lens="A day in" title="Sintra, taken at half the usual pace" hook="Two palaces, not five — and the garden everyone skips."/>
      </FeedSection>
      <ScrollTabs/>
    </ScrollFrame>
  );
}

function DiscoverScrollInPlace() {
  return (
    <ScrollFrame>
      <DiscoverTop place="Lisbon" context="You’re in Alfama · 10:14" active={1}/>
      <div style={{ height: 12 }}/>
      <ProximityMast/>
      <FeedSection label="WITHIN 10 MINUTES" right="ON FOOT">
        <FeedRow v="square" lens="Ritual" title="Miradouro de Santa Luzia, quiet now" meta="4 MIN · UPHILL"/>
        <FeedRow v="tiles" lens="Insider" title="The tile museum nobody’s in before noon" meta="8 MIN"/>
      </FeedSection>
      <FeedSection label="WHILE THE LIGHT HOLDS" right="NEXT HOUR">
        <FeedLead v="hills" lens="Why here" title="Where Alfama glows from, just now" hook="Portas do Sol, before the tour groups reach it."/>
      </FeedSection>
      <FeedSection label="A SLOW LUNCH NEAR YOU" right="OPEN NOW">
        <FeedRow v="alley" lens="Insider" title="Grilled fish, no menu, eight euros" meta="3 MIN · NO BOOKING"/>
      </FeedSection>
      <FeedSection label="TONIGHT, NEARBY" right="OPENS 7PM">
        <FeedLead v="alley" lens="A day in" title="Where Alfama actually eats after dark" hook="Skip the fado-with-dinner rooms; this is the other one."/>
        <FeedRow v="square" lens="Ritual" title="A last glass, where the singers drink after" meta="6 MIN"/>
      </FeedSection>
      <ScrollTabs/>
    </ScrollFrame>
  );
}

Object.assign(window, { FeedRow, FeedLead, FeedSection, ScrollFrame, DiscoverScrollPretrip, DiscoverScrollInPlace });
