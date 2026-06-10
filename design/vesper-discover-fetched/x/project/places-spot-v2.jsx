// ═══════════════════════════════════════════════════════════════
// VESPER · PLACES v2 — spot screens, verdict-led & selective.
// Action layout = D: planning actions sit INLINE under the Take,
// no bottom bar; Save/Share/Hear live in the top util bar (SpotHero).
// Each: hero → Take → inline actions → 2–4 lead facts → collapsed
// "the details" → world links. Fields & confidence shrink rich→forming.
// ═══════════════════════════════════════════════════════════════

// inline decision actions, data-driven (under the Take) — layout D
const planBtnD = { flex: 1, border: 'none', display: 'inline-flex', alignItems: 'center', justifyContent: 'center', gap: 8, padding: '13px 0', background: INKBLUE, color: '#fff', borderRadius: 14, fontFamily: T.sans, fontSize: 14.5, fontWeight: 600, letterSpacing: -0.1, boxShadow: '0 8px 20px -12px rgba(61,80,102,0.7)' };
const askBtnD = { border: `0.8px solid ${T.gold}`, display: 'inline-flex', alignItems: 'center', justifyContent: 'center', gap: 6, padding: '13px 18px', background: 'rgba(176,133,58,0.10)', color: T.goldDeep, borderRadius: 14, fontFamily: T.sans, fontSize: 14, fontWeight: 600, flexShrink: 0 };
const bookBtnD = { border: `0.8px solid ${T.hairline}`, display: 'inline-flex', alignItems: 'center', justifyContent: 'center', gap: 6, padding: '13px 16px', background: T.cardWarm, color: T.inkSoft, borderRadius: 14, fontFamily: T.sans, fontSize: 14, fontWeight: 600, flexShrink: 0 };
const plusI = <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round"><path d="M12 5v14M5 12h14"/></svg>;
const bookI = <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><rect x="4" y="5" width="16" height="16" rx="2"/><path d="M4 9h16M8 3v4M16 3v4"/></svg>;

function InlineActions({ actions = ['add_to_plan', 'ask_concierge'] }) {
  const has = (a) => actions.includes(a);
  return (
    <div style={{ display: 'flex', gap: 8 }}>
      {has('add_to_plan') && <button style={planBtnD}>{plusI} Add to plan</button>}
      {has('book') && <button style={bookBtnD}>{bookI} Book</button>}
      {has('ask_concierge') && <button style={askBtnD}><VesperMark s={15}/> Ask</button>}
    </div>
  );
}

// floating actions — each button floats on its own shadow, NO container
// (like the global nav). Data-driven; pinned bottom.
const floPlan = { flex: 1, border: 'none', display: 'inline-flex', alignItems: 'center', justifyContent: 'center', gap: 8, padding: '14px 0', background: INKBLUE, color: '#fff', borderRadius: 15, fontFamily: T.sans, fontSize: 14.5, fontWeight: 600, letterSpacing: -0.1, boxShadow: '0 10px 26px -8px rgba(61,80,102,0.65), 0 2px 6px -2px rgba(0,0,0,0.18)' };
const floBook = { border: 'none', display: 'inline-flex', alignItems: 'center', justifyContent: 'center', gap: 6, padding: '14px 18px', background: T.cardWarm, color: T.inkSoft, borderRadius: 15, fontFamily: T.sans, fontSize: 14, fontWeight: 600, flexShrink: 0, boxShadow: '0 10px 26px -8px rgba(0,0,0,0.22), 0 0 0 0.5px rgba(27,23,20,0.06)' };
const floAsk = { border: 'none', display: 'inline-flex', alignItems: 'center', justifyContent: 'center', gap: 6, padding: '14px 18px', background: '#F2E6CC', color: T.goldDeep, borderRadius: 15, fontFamily: T.sans, fontSize: 14, fontWeight: 600, flexShrink: 0, boxShadow: '0 10px 26px -8px rgba(176,133,58,0.5), 0 0 0 0.5px rgba(176,133,58,0.4)' };
function FloatingActions({ actions = ['add_to_plan', 'ask_concierge'] }) {
  const has = (a) => actions.includes(a);
  return (
    <div style={{ position: 'absolute', left: 16, right: 16, bottom: 18, zIndex: 25, display: 'flex', gap: 8 }}>
      {has('add_to_plan') && <button style={floPlan}>{plusI} Add to plan</button>}
      {has('book') && <button style={floBook}>{bookI} Book</button>}
      {has('ask_concierge') && <button style={floAsk}><VesperMark s={15}/> Ask</button>}
    </div>
  );
}

// a collapsed "the details" stub — the long tail, tucked away
function DetailsTucked({ lines }) {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 11 }}>
      <DetailsHeader open={false}/>
      <div style={{ fontFamily: T.serif, fontSize: 13, fontStyle: 'italic', color: T.muteSoft, lineHeight: 1.5, paddingLeft: 2 }}>{lines}</div>
    </div>
  );
}

// the EXPANDED long tail (shown in the full-scroll sketch)
function DietaryGrid({ rows = [['Vegetarian', 'ok'], ['Vegan', 'limited'], ['Gluten-free', 'on request']] }) {
  return (
    <div style={{ display: 'flex', gap: 8 }}>
      {rows.map(([k, v]) => (
        <div key={k} style={{ flex: 1, padding: '10px 8px', background: T.card, borderRadius: 10, border: `0.5px solid ${T.hairline}`, textAlign: 'center' }}>
          <div style={{ fontSize: 8.5, letterSpacing: 1, fontWeight: 700, color: T.mute }}>{k.toUpperCase()}</div>
          <div style={{ fontFamily: T.serif, fontSize: 13, color: v === 'limited' ? PINK : T.ink, marginTop: 4 }}>{v}</div>
        </div>
      ))}
    </div>
  );
}
function DetailsExpanded() {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 13 }}>
      <DetailsHeader open/>
      <DietaryGrid/>
      <div style={{ padding: '12px 14px', background: T.card, borderRadius: 12, border: `0.5px solid ${T.hairline}` }}>
        <Eye>THE ENERGY</Eye>
        <div style={{ marginTop: 10 }}><EnergyMarks/></div>
      </div>
      <div style={{ padding: '2px 0' }}>
        <FactRow label="SEQUENCE" accent={T.inkSoft}>Best after dark · pairs with a river walk · don’t plan anything after.</FactRow>
        <FactRow label="GROUP FIT">Two to four. A big group loses the counter.</FactRow>
        <FactRow label="ACCESS">Street level; tight inside, no step-free route to the back.</FactRow>
        <FactRow label="HOURS">Tue–Sun · 7pm–12 · kitchen to 11.</FactRow>
      </div>
    </div>
  );
}

const worldBlock = (
  <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
    <Eye>IN VESPER’S WORLD</Eye>
    <WorldLinks/>
  </div>
);

// ─── VENUE · RICH (high confidence, fact-rich) ──────────────────
function VenueRich() {
  return (
    <Phone bg={T.bg}>
      <SpotBody pad={92}>
        <SpotHero variant="alley" name="O Velho Eurico" type="WINE BAR" hood="Alfama" city="Lisbon"/>
        <div style={{ padding: '20px 18px 0', display: 'flex', flexDirection: 'column', gap: 18 }}>
          <TakeCard
            opinion="loved" confidence="high" provenance="based on your last 3 trips"
            verdict="Go the first night — it sets the tone for the whole trip."
            body="The room you keep describing when you talk about a good night out: tiny, loud in the right way, a list that rewards trusting the staff."
            caveats={[
              { severity: 'warning', reason: 'logistics', text: 'No reservations — go before 7:30 or wait.' },
              { severity: 'note', reason: 'dietary', text: 'Little for vegans; great if you eat fish.' },
            ]}
            why={['you save list-led wine bars', 'food-first', 'walkable from your stay']}
          />
          <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
            <OrderSkip order="The bitoque, whatever’s open by the glass, tinned fish to start." skip="The cocktails — it’s a wine room."/>
            <LeadFacts items={[
              { label: 'PEAK', value: <span style={{ color: T.goldDeep, fontWeight: 600 }}>Memorable — the kind of night you retell.</span> },
              { label: 'GREAT FOR', value: 'A first night, two to four, trusting the counter.' },
            ]}/>
          </div>
          <DetailsTucked lines="dietary grid · hours · accessibility · the energy bars · sequencing · group fit — tap to open."/>
          {worldBlock}
        </div>
      </SpotBody>
      <FloatingActions actions={['add_to_plan', 'book', 'ask_concierge']}/>
    </Phone>
  );
}

// ─── VENUE · FORMING (low confidence, sparse) ───────────────────
function VenueForming() {
  return (
    <Phone bg={T.bg}>
      <SpotBody pad={92}>
        <SpotHero variant="alley" name="O Velho Eurico" type="WINE BAR" hood="Alfama" city="Lisbon"/>
        <div style={{ padding: '20px 18px 0', display: 'flex', flexDirection: 'column', gap: 18 }}>
          <TakeCard
            opinion="conditional" confidence="low" provenance="I’ve only seen you save one place like this"
            verdict="Might be your kind of room — I’m not sure yet."
            body="It’s loud, no-reservations, wine-first. That’s a great night for some and a bad one for others, and I don’t know which you are here."
            caveats={[{ severity: 'note', reason: 'fit', text: 'Loud and tight — not for a quiet conversation.' }]}
            curator="A chef-run tasca turned natural-wine counter; plates around €9, the list changes nightly."
          />
          <DetailsTucked lines="hours · what to order · dietary · accessibility — I’ll surface these once the read firms up."/>
          {worldBlock}
        </div>
      </SpotBody>
      <FloatingActions actions={['ask_concierge']}/>
    </Phone>
  );
}

// ─── EXPERIENCE · the distinctive axis is TIME ──────────────────
function ExperienceV2() {
  return (
    <Phone bg={T.bg}>
      <SpotBody pad={92}>
        <SpotHero variant="square" name="Fado at Mesa de Frades" type="EXPERIENCE · MUSIC" hood="Alfama" city="Lisbon"/>
        <div style={{ padding: '20px 18px 0', display: 'flex', flexDirection: 'column', gap: 18 }}>
          <TakeCard
            opinion="worthit" confidence="medium" provenance="you saved two fado reads, skipped the dinner-shows"
            verdict="The real one — but only if you’ll do it properly, and late."
            body="A tiled former chapel where the singing doesn’t start till the room is right. Take the 11pm seating, not the dinner one."
            caveats={[
              { severity: 'warning', reason: 'timing', text: 'Late start — the good seating runs 11pm–1am.' },
              { severity: 'warning', reason: 'logistics', text: 'Tiny room — book 2 days ahead.' },
            ]}
            why={['you skip dinner-and-show', 'you stay out late']}
          />
          <LeadFacts items={[
            { label: 'WHEN', value: <span>Nightly · two seatings, <b>9pm</b> & <b>11pm</b> · ~2 hrs.</span> },
            { label: 'FOR', value: 'Anyone who’ll sit in silence for a voice. Late people.' },
            { label: 'THE CALL', value: 'Worth rearranging the evening for — not the whole day.', accent: T.goldDeep },
          ]}/>
          <DetailsTucked lines="genre & activity tags · difficulty · where it happens (venue, address) · book link — tap to open."/>
          {worldBlock}
        </div>
      </SpotBody>
      <FloatingActions actions={['add_to_plan', 'book', 'ask_concierge']}/>
    </Phone>
  );
}

// small abstract map (lat/lng + walkability to the plan)
function MiniMap() {
  return (
    <div style={{ position: 'relative', height: 128, borderRadius: 13, overflow: 'hidden', border: hp, background: '#E7E0D2' }}>
      <svg width="100%" height="100%" viewBox="0 0 320 128" preserveAspectRatio="none">
        {[20, 52, 84, 116].map((y) => <line key={y} x1="0" y1={y} x2="320" y2={y} stroke="rgba(27,23,20,0.08)" strokeWidth="1"/>)}
        {[60, 130, 200, 270].map((x) => <line key={x} x1={x} y1="0" x2={x} y2="128" stroke="rgba(27,23,20,0.08)" strokeWidth="1"/>)}
        <path d="M150 70 L210 40" stroke={INKBLUE} strokeWidth="1.6" strokeDasharray="3 3"/>
        <path d="M150 70 L96 96" stroke={INKBLUE} strokeWidth="1.6" strokeDasharray="3 3"/>
      </svg>
      <div style={{ position: 'absolute', left: 150, top: 70, transform: 'translate(-50%,-100%)', color: T.gold }}>
        <svg width="22" height="22" viewBox="0 0 24 24" fill={T.gold} stroke="#fff" strokeWidth="1.2"><path d="M12 22s7-6.4 7-11a7 7 0 1 0-14 0c0 4.6 7 11 7 11Z"/><circle cx="12" cy="11" r="2.4" fill="#fff"/></svg>
      </div>
      {[[210, 40, '5 min'], [96, 96, '8 min']].map(([x, y, t], i) => (
        <div key={i} style={{ position: 'absolute', left: x, top: y, transform: 'translate(-50%,-50%)', display: 'flex', alignItems: 'center', gap: 4 }}>
          <span style={{ width: 9, height: 9, borderRadius: 999, background: INKBLUE, border: '1.5px solid #fff' }}/>
          <span style={{ fontFamily: T.mono, fontSize: 8.5, fontWeight: 600, color: INKBLUE, background: 'rgba(247,242,231,0.85)', padding: '1px 4px', borderRadius: 4 }}>{t}</span>
        </div>
      ))}
    </div>
  );
}

// ─── STAY · deliberately thin ───────────────────────────────────
function StayV2() {
  return (
    <Phone bg={T.bg}>
      <SpotBody pad={92}>
        <SpotHero variant="rooftops" name="Casa do Alecrim" type="STAY · GUESTHOUSE" hood="Príncipe Real" city="Lisbon"/>
        <div style={{ padding: '20px 18px 0', display: 'flex', flexDirection: 'column', gap: 18 }}>
          <TakeCard
            opinion="worthit" confidence="high" provenance="how you travel — out all day, back to sleep"
            verdict="The call: pay for the location, forgive the small rooms."
            body="Rooms are snug and there’s no lift — but you wake three minutes from the garden and ten from everything you’ve saved. For you, that’s the right trade."
            caveats={[{ severity: 'warning', reason: 'accessibility', text: 'No lift — three flights to the rooms.' }]}
          />
          <div style={{ display: 'flex', flexDirection: 'column', gap: 11 }}>
            <Eye>WHERE IT PUTS YOU</Eye>
            <MiniMap/>
            <LeadFacts items={[
              { label: 'NEAR PLANS', value: '6 of your saved spots within a 12-min walk.' },
              { label: 'DATES', value: <span>May 5 → 9 · <b>4 nights</b></span> },
            ]}/>
            <div style={{ display: 'flex', gap: 7 }}>
              <MiniChip tint={T.goldDeep}>★ Primary stay</MiniChip>
              <MiniChip>Visible to the group</MiniChip>
            </div>
          </div>
          <DetailsTucked lines="check-in 3pm / out 11am · room types · amenities · cancellation — tap to open."/>
        </div>
      </SpotBody>
      <FloatingActions actions={['add_to_plan', 'book', 'ask_concierge']}/>
    </Phone>
  );
}

// ─── SITE · minimal ─────────────────────────────────────────────
function SiteV2() {
  return (
    <Phone bg={T.bg}>
      <SpotBody pad={92}>
        <SpotHero variant="hills" name="Miradouro da Graça" type="SITE · VIEWPOINT" hood="Graça" city="Lisbon"/>
        <div style={{ padding: '20px 18px 0', display: 'flex', flexDirection: 'column', gap: 18 }}>
          <TakeCard
            opinion="loved" confidence="high" provenance="you end most Lisbon days at a view"
            verdict="Your end-of-day view — come for the light, not the landmark."
            body="The whole city tips gold from up here around five. A glass at the kiosk, the castle catching the last sun, and nowhere you need to be after."
            caveats={[{ severity: 'note', reason: 'timing', text: 'Best 5–7pm; midday is flat and hot.' }]}
          />
          <LeadFacts items={[
            { label: 'ACCESS', value: 'A steep ten minutes up, or tram 28 to the door.' },
            { label: 'GIVE IT', value: 'Forty minutes, a drink, no plan after.' },
          ]}/>
          {worldBlock}
        </div>
      </SpotBody>
      <FloatingActions actions={['add_to_plan', 'ask_concierge']}/>
    </Phone>
  );
}

// ─── NEIGHBORHOOD · a Take entity (verdict on the area) ─────────
function NeighborhoodTake() {
  return (
    <Phone bg={T.bg}>
      <SpotBody pad={92}>
        <SpotHero variant="alley" name="Alfama" type="NEIGHBORHOOD · LISBON ↑" hood="Lisbon" city="Portugal"/>
        <div style={{ padding: '20px 18px 0', display: 'flex', flexDirection: 'column', gap: 18 }}>
          <TakeCard
            opinion="loved" confidence="high" provenance="14 saves here over 5 years"
            verdict="This is your Lisbon — lean all the way in."
            body="The oldest quarter: a knot of stairs and washing lines above the river, dense with fado and tiny restaurants. You come for the morning quiet before the trams fill."
            caveats={[{ severity: 'note', reason: 'logistics', text: 'All stairs — wear the right shoes.' }]}
            why={['you always end at the same view', 'food-first, plan-light']}
          />
          <LeadFacts items={[
            { label: 'WALKABILITY', value: <span><b>Very high</b> — nothing’s flat, but everything’s close.</span> },
            { label: 'BEST TIME', value: 'Early morning, and again at golden hour.' },
            { label: 'CHARACTER', value: 'Lived-in, vertical, song after dark.' },
          ]}/>
          <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
            <Eye>YOUR SPOTS IN ALFAMA · 14</Eye>
            <WorldLinks/>
          </div>
        </div>
      </SpotBody>
      <FloatingActions actions={['add_to_plan', 'ask_concierge']}/>
    </Phone>
  );
}

// ─── FULL SCROLL · the whole venue page, top to bottom ──────────
function TallFrame({ children }) {
  return (
    <div style={{ width: 393, borderRadius: 44, overflow: 'hidden', background: T.bg, position: 'relative', fontFamily: T.sans, color: T.ink, boxShadow: '0 0 0 11px #0d0b09, 0 0 0 12px #2a2622, 0 30px 60px -20px rgba(0,0,0,0.35)' }}>
      {/* faux status bar + notch */}
      <div style={{ position: 'absolute', top: 18, left: 32, zIndex: 32, pointerEvents: 'none' }}><span style={{ fontWeight: 600, fontSize: 17, color: '#fff' }}>9:41</span></div>
      <div style={{ position: 'absolute', top: 11, left: '50%', transform: 'translateX(-50%)', width: 124, height: 37, borderRadius: 24, background: '#000', zIndex: 33 }}/>
      {children}
    </div>
  );
}
function VenueFullScroll() {
  return (
    <TallFrame>
      <SpotHero variant="alley" name="O Velho Eurico" type="WINE BAR" hood="Alfama" city="Lisbon"/>
      <div style={{ padding: '20px 18px 30px', display: 'flex', flexDirection: 'column', gap: 18 }}>
        <TakeCard
          opinion="loved" confidence="high" provenance="based on your last 3 trips"
          verdict="Go the first night — it sets the tone for the whole trip."
          body="The room you keep describing when you talk about a good night out: tiny, loud in the right way, a list that rewards trusting the staff."
          caveats={[
            { severity: 'warning', reason: 'logistics', text: 'No reservations — go before 7:30 or wait.' },
            { severity: 'note', reason: 'dietary', text: 'Little for vegans; great if you eat fish.' },
          ]}
          why={['you save list-led wine bars', 'food-first', 'walkable from your stay']}
        />
        <OrderSkip order="The bitoque, whatever’s open by the glass, tinned fish to start." skip="The cocktails — it’s a wine room."/>
        <LeadFacts items={[
          { label: 'PEAK', value: <span style={{ color: T.goldDeep, fontWeight: 600 }}>Memorable — the kind of night you retell.</span> },
          { label: 'GREAT FOR', value: 'A first night, two to four, trusting the counter.' },
        ]}/>
        <DetailsExpanded/>
        {worldBlock}
      </div>
      <FloatingActions actions={['add_to_plan', 'book', 'ask_concierge']}/>
    </TallFrame>
  );
}

Object.assign(window, {
  InlineActions, DetailsTucked, DetailsExpanded, DietaryGrid,
  VenueRich, VenueForming, ExperienceV2, StayV2, SiteV2, NeighborhoodTake, MiniMap,
  TallFrame, VenueFullScroll,
});
