// ═══════════════════════════════════════════════════════════════
// VESPER · PLACES — the Take, isolated as states (close-ups on a
// venue hero). Rebuilt on the structured TakeCard so the whole tab
// uses one Take component. rich · forming · cold (curator-only) ·
// loading. SpotBody pad small (no bottom bar — layout D).
// ═══════════════════════════════════════════════════════════════

function TakeStateShell({ kicker, kc = T.goldDeep, children }) {
  return (
    <Phone bg={T.bg}>
      <SpotBody pad={34}>
        <SpotHero variant="alley" name="O Velho Eurico" type="WINE BAR" hood="Alfama" city="Lisbon"/>
        <div style={{ padding: '20px 18px 0' }}>
          <div style={{ marginBottom: 12 }}><Eye c={kc}>{kicker}</Eye></div>
          {children}
        </div>
      </SpotBody>
    </Phone>
  );
}

// rich — confident, fact-rich verdict
function TakeRich() {
  return (
    <TakeStateShell kicker="STATE · RICH (HIGH CONFIDENCE)">
      <TakeCard
        opinion="loved" confidence="high" provenance="based on your last 3 trips"
        verdict="Go the first night — it sets the tone for the whole trip."
        body="The room you keep describing when you talk about a good night out: tiny, loud in the right way, a list that rewards trusting the staff."
        caveats={[{ severity: 'warning', reason: 'logistics', text: 'No reservations — go before 7:30 or wait.' }]}
        why={['you save list-led wine bars', 'food-first', 'walkable from your stay']}
      />
    </TakeStateShell>
  );
}

// forming — tentative, sparse
function TakeForming() {
  return (
    <TakeStateShell kicker="STATE · FORMING (LOW CONFIDENCE)" kc={SAGE}>
      <TakeCard
        opinion="conditional" confidence="low" provenance="I’ve only seen you save one place like this"
        verdict="Might be your kind of room — I’m not sure yet."
        body="It’s loud, no-reservations, wine-first. That’s a great night for some and a bad one for others, and I don’t know which you are here."
        caveats={[{ severity: 'note', reason: 'fit', text: 'Loud and tight — not for a quiet conversation.' }]}
        curator="A chef-run tasca turned natural-wine counter; plates around €9."
      />
    </TakeStateShell>
  );
}

// cold — curator-only, no personal verdict; invites a read
function TakeCold() {
  return (
    <TakeStateShell kicker="STATE · CURATOR-ONLY / COLD">
      <div style={{ padding: '19px 20px', background: T.cardWarm, borderRadius: 18, border: hp, boxShadow: '0 1px 0 rgba(255,255,255,0.6) inset, 0 14px 30px -22px rgba(0,0,0,0.3)' }}>
        <Eye c={T.goldDeep}>THE CURATOR’S READ</Eye>
        <p style={{ fontFamily: T.serif, fontSize: 21, fontWeight: 500, color: T.ink, lineHeight: 1.26, letterSpacing: -0.3, margin: '11px 0 0' }}>A tiny natural-wine counter that runs on instinct.</p>
        <p style={{ fontFamily: T.serif, fontSize: 15, color: T.inkSoft, lineHeight: 1.5, margin: '10px 0 0' }}>Chef-run, plates around €9, the list changes by the night. Locals lean on the staff to choose.</p>
        <div style={{ marginTop: 16, paddingTop: 14, borderTop: hpT, display: 'flex', alignItems: 'center', gap: 10 }}>
          <VesperMark s={15}/>
          <span style={{ flex: 1, fontFamily: T.serif, fontStyle: 'italic', fontSize: 13.5, color: T.mute, lineHeight: 1.4 }}>I don’t know your taste here yet — tell me one thing and I’ll start a read.</span>
        </div>
      </div>
    </TakeStateShell>
  );
}

// loading — curator instant, personal streaming in
function TakeLoadingScreen() {
  return (
    <TakeStateShell kicker="STATE · LOADING">
      <TakeLoading/>
    </TakeStateShell>
  );
}

Object.assign(window, { TakeStateShell, TakeRich, TakeForming, TakeCold, TakeLoadingScreen });
