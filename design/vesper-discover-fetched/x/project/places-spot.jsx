// ═══════════════════════════════════════════════════════════════
// VESPER · PLACES — Spot detail (one template, three faces).
// Hero → the Take → type-specific details → world-model links →
// sticky action rail. Venue is the anchor; Experience & Stay inherit
// the skeleton and swap the middle.
// ═══════════════════════════════════════════════════════════════

// the spot utility bar — back · hear · save · share (consolidated up top)
function SpotUtilBar() {
  const c = 'rgba(255,255,255,0.95)';
  const pill = { width: 34, height: 34, borderRadius: 999, background: 'rgba(20,14,9,0.32)', backdropFilter: 'blur(8px)', display: 'flex', alignItems: 'center', justifyContent: 'center' };
  return (
    <div style={{ position: 'absolute', top: 54, left: 0, right: 0, zIndex: 20, display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '10px 18px' }}>
      <div style={pill}><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d="M14 6l-6 6 6 6"/></svg></div>
      <div style={{ display: 'flex', gap: 8 }}>
        <div style={pill}><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><path d="M3 10v4h4l5 4V6L7 10H3Z"/><path d="M16 9a4 4 0 0 1 0 6"/></svg></div>
        <div style={pill}><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><path d="M6 4h12v16l-6-4-6 4V4Z"/></svg></div>
        <div style={pill}><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><circle cx="6" cy="12" r="2.4"/><circle cx="17" cy="6" r="2.4"/><circle cx="17" cy="18" r="2.4"/><path d="M8.1 10.9l6.8-3.8M8.1 13.1l6.8 3.8"/></svg></div>
      </div>
    </div>
  );
}

// shared hero — full-bleed masthead: name set over a tall photo, no card.
function SpotHero({ variant = 'alley', name, type, hood, city, real }) {
  return (
    <div style={{ position: 'relative' }}>
      <div style={{ height: 360 }}>
        <Plate variant={variant} style={{ height: 360 }} dim={0.18}/>
        <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to bottom, rgba(20,14,9,0.34), rgba(20,14,9,0.05) 38%, rgba(20,14,9,0.62))' }}/>
      </div>
      <SpotUtilBar/>
      <div style={{ position: 'absolute', left: 22, right: 22, bottom: 22 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
          <Eye c="rgba(255,255,255,0.82)">{type}</Eye>
          <span style={{ color: 'rgba(255,255,255,0.5)', fontSize: 10 }}>·</span>
          <span style={{ fontSize: 11.5, color: '#fff', fontWeight: 600 }}>{hood}, {city} ↑</span>
        </div>
        <h1 style={{ fontFamily: T.serif, fontSize: 40, fontWeight: 500, color: '#fff', letterSpacing: -0.9, lineHeight: 0.98, margin: '9px 0 0' }}>{name}</h1>
      </div>
    </div>
  );
}

const linkIcons = {
  place: <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><path d="M12 21s7-6.4 7-11a7 7 0 1 0-14 0c0 4.6 7 11 7 11Z"/><circle cx="12" cy="10" r="2.4"/></svg>,
  read: <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><path d="M4 5h9a3 3 0 0 1 3 3v11a2.5 2.5 0 0 0-2.5-2.5H4V5Z"/><path d="M20 5h-2a3 3 0 0 0-3 3v8.5"/></svg>,
  similar: <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><circle cx="7" cy="7" r="3"/><circle cx="17" cy="17" r="3"/><path d="M10 7h4a3 3 0 0 1 3 3v4"/></svg>,
};

function WorldLinks() {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
      <WorldLink icon={linkIcons.place} label="Alfama" sub="the neighborhood it sits in · 14 spots" />
      <WorldLink icon={linkIcons.read} label="Where Lisbon drinks natural" sub="a Vesper read · 4 min" tint={T.goldDeep}/>
      <WorldLink icon={linkIcons.similar} label="Three more like this" sub="small, list-led, wine-first" tint={SAGE}/>
    </div>
  );
}

// ─── FACE 1 · VENUE (the anchor) ────────────────────────────────
function SpotVenue() {
  return (
    <Phone bg={T.bg}>
      <SpotBody>
        <SpotHero variant="alley" name="O Velho Eurico" type="WINE BAR" hood="Alfama" city="Lisbon"/>
        <div style={{ padding: '20px 18px 0', display: 'flex', flexDirection: 'column', gap: 18 }}>
          <TakeBlock
            state="rich"
            verdict="Go the first night — it sets the tone for the whole trip."
            body="It’s the room you keep describing when you talk about a good night out: tiny, loud in the right way, a list that rewards trusting the staff. You’ll over-order and not regret it."
            pill="WORTH REARRANGING A DAY FOR"
            curator="A chef-run tasca turned natural-wine counter; plates around €9, the list changes nightly."
            why={['you save list-led wine bars', 'you lean loud, food-first', 'walkable from your stay']}
          />

          <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
            <DetailsHeader/>
            <OrderSkip order="The bitoque, whatever’s open by the glass, the tinned fish to start." skip="The cocktails — it’s a wine room, drink the wine."/>
            <div style={{ padding: '2px 0' }}>
              <FactRow label="GREAT FOR">A first night, two to four, trusting the counter.</FactRow>
              <FactRow label="NOT IDEAL">A quiet conversation, or anyone who needs a reservation to relax.</FactRow>
              <FactRow label="PEAK"><span style={{ color: T.goldDeep, fontWeight: 600 }}>Memorable</span> — the kind of night you retell.</FactRow>
            </div>
            <div style={{ padding: '12px 14px', background: T.card, borderRadius: 13, border: `0.5px solid ${T.hairline}` }}>
              <Eye>THE ENERGY</Eye>
              <div style={{ marginTop: 10 }}><EnergyMarks/></div>
            </div>
            <div style={{ padding: '2px 0' }}>
              <FactRow label="SEQUENCE" accent={T.inkSoft}>Best after dark · pairs with a walk down to the river · don’t plan anything after.</FactRow>
              <FactRow label="DIETARY">Veg ok · little for vegan · GF on request.</FactRow>
              <FactRow label="KNOW">No reservations · 7pm–12 · cash kindest · ~1½ hrs.</FactRow>
            </div>
          </div>

          <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
            <Eye>IN VESPER’S WORLD</Eye>
            <WorldLinks/>
          </div>
        </div>
      </SpotBody>
      <ActionRail/>
    </Phone>
  );
}

// ─── FACE 2 · EXPERIENCE ────────────────────────────────────────
function SpotExperience() {
  return (
    <Phone bg={T.bg}>
      <SpotBody>
        <SpotHero variant="square" name="Fado at Mesa de Frades" type="EXPERIENCE · MUSIC" hood="Alfama" city="Lisbon"/>
        <div style={{ padding: '20px 18px 0', display: 'flex', flexDirection: 'column', gap: 18 }}>
          <TakeBlock
            state="rich"
            verdict="The real one — go, but go late and go in."
            body="A tiled former chapel where the singing doesn’t start till the room is right. You don’t love a ‘show,’ so take the 11pm seating, not the dinner one — that’s when it becomes the thing people mean."
            pill="ONLY IF YOU’LL DO IT PROPERLY"
            curator="Intimate fado in a former chapel; two seatings, the later one is for listening, not eating."
            why={['you skip the dinner-and-show', 'you stay out late', 'you saved two fado reads']}
          />

          <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
            <DetailsHeader/>
            <div style={{ padding: '2px 0' }}>
              <FactRow label="WHEN · WHERE">Nightly · two seatings, 9pm & 11pm · Rua dos Remédios.</FactRow>
              <FactRow label="FOR">Anyone who’ll sit in silence for a voice. Late people.</FactRow>
              <FactRow label="NOT FOR">An early night, or a big talkative group.</FactRow>
              <FactRow label="BOOK BY">Two days ahead for the late seating — it’s small.</FactRow>
              <FactRow label="THE CALL" accent={T.goldDeep}>Worth rearranging the evening for — not the whole day.</FactRow>
            </div>
          </div>

          <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
            <Eye>IN VESPER’S WORLD</Eye>
            <WorldLinks/>
          </div>
        </div>
      </SpotBody>
      <ActionRail book="Book"/>
    </Phone>
  );
}

// ─── FACE 3 · STAY ──────────────────────────────────────────────
function SpotStay() {
  return (
    <Phone bg={T.bg}>
      <SpotBody>
        <SpotHero variant="rooftops" name="Casa do Alecrim" type="STAY · GUESTHOUSE" hood="Príncipe Real" city="Lisbon"/>
        <div style={{ padding: '20px 18px 0', display: 'flex', flexDirection: 'column', gap: 18 }}>
          <TakeBlock
            state="rich"
            verdict="Pay for the location, forgive the small rooms."
            body="The tradeoff is honest: rooms are snug and there’s no lift, but you wake up three minutes from the garden and a good coffee, and ten from everything you’ve saved. For how you travel — out all day, back only to sleep — that’s the right trade."
            pill="THE RIGHT TRADE FOR YOU"
            curator="A seven-room guesthouse in Príncipe Real; central, characterful, not luxurious."
            why={['you’re out all day', 'you saved 6 spots nearby', 'you rank walkability over comfort']}
          />

          <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
            <DetailsHeader/>
            {/* the tradeoff, made visual */}
            <div style={{ padding: '14px', background: T.card, borderRadius: 13, border: `0.5px solid ${T.hairline}` }}>
              <Eye>THE TRADEOFF</Eye>
              <div style={{ marginTop: 11, display: 'flex', flexDirection: 'column', gap: 9 }}>
                {[['Location', 5, INKBLUE], ['Comfort', 2, T.mute], ['Price', 3, T.mute]].map(([k, n, c]) => (
                  <div key={k} style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
                    <span style={{ width: 64, fontSize: 11, color: T.mute, fontWeight: 500 }}>{k}</span>
                    <div style={{ display: 'flex', gap: 5 }}>{[1, 2, 3, 4, 5].map((i) => <span key={i} style={{ width: 7, height: 7, borderRadius: 999, background: i <= n ? c : 'rgba(27,23,20,0.12)' }}/>)}</div>
                  </div>
                ))}
              </div>
            </div>
            {/* walkability to your plans */}
            <div style={{ padding: '2px 0' }}>
              <FactRow label="PUTS YOU" accent={T.inkSoft}>3 min to the garden · 10 to Bairro Alto · 12 to the river.</FactRow>
              <FactRow label="NEAR PLANS">6 of your saved spots within a 12-min walk.</FactRow>
              <FactRow label="GROUP FIT">Best for two; the family room sleeps three, snugly.</FactRow>
              <FactRow label="KNOW">Check-in 3pm · out 11am · no lift · 4 nights held.</FactRow>
            </div>
          </div>

          <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
            <Eye>IN VESPER’S WORLD</Eye>
            <WorldLinks/>
          </div>
        </div>
      </SpotBody>
      <ActionRail book="Book"/>
    </Phone>
  );
}

Object.assign(window, { SpotHero, WorldLinks, SpotVenue, SpotExperience, SpotStay });
