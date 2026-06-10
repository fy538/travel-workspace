// ═══════════════════════════════════════════════════════════════
// TRIPS · INTERACTIVE — "the home is the form" (live).
// Built on the designed adaptive blank home (BlankCover/BlankVoice).
// Tap a slot to fill it; the cover gains a face, Vesper's line
// re-reads, and once place+dates are set the itinerary invite
// appears. No new paradigm — the designed screen, made live.
// ═══════════════════════════════════════════════════════════════
function AdaptiveLoop() {
  const { useState } = React;
  const [f, setF] = useState({ place: false, dates: false, who: false });
  const place = f.place ? 'Lisbon' : null;
  const dates = f.dates ? 'JUN 2–7 · 5 NIGHTS' : null;
  const both = f.place && f.dates;
  const line = (!f.place && !f.dates)
    ? 'Start anywhere — a place, some dates, or who’s coming. I’ll shape the rest around it.'
    : both
      ? `Lisbon in June${f.who ? ', the two of you' : ''}. I’ve started a shape — six open days, ready when you are.`
      : f.place
        ? 'Lisbon — lovely. Tell me when, and I’ll start finding the shape of it.'
        : 'Five slow days in June. Where shall we point them?';

  const Slot = ({ k, label, prompt, val, first }) => {
    const on = f[k];
    return (
      <div onClick={() => setF((s) => ({ ...s, [k]: !s[k] }))} style={{ cursor: 'pointer', display: 'grid', gridTemplateColumns: '74px 1fr 16px', gap: 12, alignItems: 'baseline', padding: '15px 0', borderTop: `0.5px solid ${first ? T.hairline : T.hairThin}` }}>
        <span style={{ fontFamily: T.mono, fontSize: 9, letterSpacing: 1.6, fontWeight: 600, color: on ? T.goldDeep : T.mute }}>{label}</span>
        <span style={{ fontFamily: T.serif, fontSize: 17, fontStyle: on ? 'normal' : 'italic', fontWeight: on ? 500 : 400, color: on ? T.ink : T.muteSoft, letterSpacing: -0.3, lineHeight: 1.2 }}>{on ? val : prompt}</span>
        {on
          ? <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#3D7050" strokeWidth="2.4" strokeLinecap="round" strokeLinejoin="round" style={{ alignSelf: 'center' }}><path d="M4 12l5 5L20 6"/></svg>
          : <Marks.ArrowR s={13} c={T.faint}/>}
      </div>
    );
  };

  return (
    <Phone bg={T.bg}>
      <BlankCover place={place} dates={dates}/>
      <BlankVoice>{line}</BlankVoice>
      <div style={{ padding: '20px 24px 0' }}>
        <div style={{ fontFamily: T.mono, fontSize: 9, letterSpacing: 1.8, color: T.mute, fontWeight: 600, paddingBottom: 2 }}>{both ? 'THE TRIP SO FAR' : 'BEGIN WITH'}</div>
        <Slot k="place" label="A PLACE" prompt="where are we going?" val="Lisbon, Portugal" first/>
        <Slot k="dates" label="DATES" prompt="when?" val="Jun 2–7 · 5 nights"/>
        <Slot k="who" label="WHO" prompt="who’s coming?" val="You + Ana"/>
      </div>
      {both ? (
        <div style={{ margin: '18px 24px 0', display: 'flex', alignItems: 'center', justifyContent: 'space-between', paddingTop: 15, borderTop: `0.5px solid ${T.hairline}` }}>
          <span style={{ fontFamily: T.serif, fontSize: 17, fontWeight: 500, color: T.ink, letterSpacing: -0.3 }}>Plan the days with Vesper</span>
          <Marks.ArrowR s={15} c={T.goldDeep}/>
        </div>
      ) : (
        <div style={{ padding: '20px 24px 0' }}>
          <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13.5, color: T.mute, margin: 0, lineHeight: 1.5, paddingTop: 15, borderTop: `0.5px solid ${T.hairThin}` }}>Nothing’s required — it’s already saved as a draft. Tap a row to fill it.</p>
        </div>
      )}
      <TabBar active="trips"/>
    </Phone>
  );
}

Object.assign(window, { AdaptiveLoop });
