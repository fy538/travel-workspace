// ═══════════════════════════════════════════════════════════════
// ADAPTIVE SINGLE-TRIP HOME — the home IS the creation surface.
// Tapping "start a new trip" (not via Vesper) lands you HERE, in a
// null state. You fill it by choosing a place, dates, or friends —
// any one, any order, none required. The home adapts to what's set.
// Plus the three light pickers each slot opens. Editorial language.
// Reuses DR, StyleRiso, PFrame, EdKick, ed, Ppl/CASTD.
// ═══════════════════════════════════════════════════════════════

// Forming cover — identity comes from whatever's been set so far.
function FCover2({ place, dates }) {
  const hasPlace = !!place;
  return (
    <div style={{ position: 'relative', height: hasPlace ? 220 : 152, marginTop: -40, transition: 'height .3s' }}>
      <div style={{ position: 'absolute', inset: 0, opacity: hasPlace ? 1 : 0.24 }}><StyleRiso w={393} h={hasPlace ? 220 : 152}/></div>
      <div style={{ position: 'absolute', inset: 0, background: hasPlace
        ? 'linear-gradient(to bottom, rgba(20,14,9,0.36) 0%, rgba(20,14,9,0) 32%, rgba(20,14,9,0) 50%, rgba(20,14,9,0.8) 100%)'
        : `linear-gradient(to bottom, rgba(239,234,224,0.15), ${DR.paper})` }}/>
      <div style={{ position: 'absolute', top: 50, left: 22, right: 22, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke={hasPlace ? 'rgba(255,255,255,0.92)' : DR.soft} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><path d="M14 6l-6 6 6 6"/></svg>
        <span style={{ fontFamily: DR.mono, fontSize: 9, letterSpacing: 2.4, color: hasPlace ? 'rgba(255,255,255,0.8)' : DR.mute, fontWeight: 600 }}>{hasPlace ? 'A NEW FOLIO' : 'NEW TRIP · DRAFT'}</span>
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke={hasPlace ? 'rgba(255,255,255,0.92)' : DR.soft} strokeWidth="1.6" strokeLinecap="round"><circle cx="5" cy="12" r="1.4"/><circle cx="12" cy="12" r="1.4"/><circle cx="19" cy="12" r="1.4"/></svg>
      </div>
      <div style={{ position: 'absolute', left: 22, right: 22, bottom: hasPlace ? 20 : 16 }}>
        {dates && <div style={{ fontFamily: DR.mono, fontSize: 9, letterSpacing: 2, color: hasPlace ? 'rgba(255,255,255,0.85)' : DR.goldDeep, fontWeight: 600, marginBottom: 7 }}>{dates}</div>}
        {hasPlace
          ? <h1 style={{ fontFamily: DR.serif, fontSize: 38, fontWeight: 500, letterSpacing: -1.1, lineHeight: 0.95, color: '#fff', margin: 0 }}>{place}</h1>
          : <h1 style={{ fontFamily: DR.serif, fontSize: 27, fontWeight: 500, fontStyle: 'italic', letterSpacing: -0.5, lineHeight: 1, color: DR.faint, margin: 0 }}>{dates ? 'where to?' : 'A trip, taking shape'}</h1>}
      </div>
    </div>
  );
}

// Vesper standfirst (no box).
function VLine({ children }) {
  return (
    <div style={{ padding: '20px 24px 0' }}>
      <EdKick c={DR.goldDeep}>Vesper</EdKick>
      <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 18, color: DR.ink, lineHeight: 1.42, letterSpacing: -0.2, margin: '9px 0 0' }}>{children}</p>
    </div>
  );
}

// A start slot — hairline row. Set = ink + check (tap to change); open = faint prompt + →.
function StartSlot({ k, prompt, value, first }) {
  const set = !!value;
  return (
    <div style={{ display: 'grid', gridTemplateColumns: '74px 1fr 16px', gap: 12, alignItems: 'baseline', padding: '15px 0', borderTop: first ? ed.rule : ed.hair }}>
      <EdKick c={set ? DR.goldDeep : DR.mute}>{k}</EdKick>
      <span style={{ fontFamily: DR.serif, fontSize: 17.5, fontStyle: set ? 'normal' : 'italic', fontWeight: set ? 500 : 400, color: set ? DR.ink : DR.faint, letterSpacing: -0.3, lineHeight: 1.2 }}>{set ? value : prompt}</span>
      {set
        ? <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#3D7050" strokeWidth="2.4" strokeLinecap="round" strokeLinejoin="round" style={{ alignSelf: 'center' }}><path d="M4 12l5 5L20 6"/></svg>
        : <span style={{ color: DR.faint, fontSize: 16, alignSelf: 'center' }}>→</span>}
    </div>
  );
}

function SectionLabel({ children, right }) {
  return <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', padding: '0 0 4px' }}><EdKick>{children}</EdKick>{right && <EdKick>{right}</EdKick>}</div>;
}

// ── STATE 1 · BLANK — nothing set. Start anywhere. ──
function HomeNull() {
  return (
    <PFrame h={852}>
      <FCover2/>
      <VLine>Start anywhere — a place, some dates, or who’s coming. I’ll shape the rest around it.</VLine>
      <div style={{ padding: '22px 24px 0' }}>
        <SectionLabel>Begin with</SectionLabel>
        <StartSlot k="A PLACE" prompt="where are we going?" first/>
        <StartSlot k="DATES" prompt="when?"/>
        <StartSlot k="WHO" prompt="who’s coming?"/>
      </div>
      <div style={{ padding: '22px 24px 0' }}>
        <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 13.5, color: DR.mute, margin: 0, lineHeight: 1.5, paddingTop: 15, borderTop: ed.hair }}>Nothing’s required — this is already saved as a draft. Or <span style={{ color: DR.goldDeep }}>tell me about it →</span></p>
      </div>
    </PFrame>
  );
}

// ── STATE 2 · PLACE ONLY ──
function HomePlace() {
  return (
    <PFrame h={852}>
      <FCover2 place="Lisbon"/>
      <VLine>Lisbon — lovely. Tell me when, and I’ll start finding the shape of it.</VLine>
      <div style={{ padding: '22px 24px 0' }}>
        <SectionLabel>The trip so far</SectionLabel>
        <StartSlot k="A PLACE" value="Lisbon, Portugal" first/>
        <StartSlot k="DATES" prompt="add when"/>
        <StartSlot k="WHO" prompt="just you — invite the others"/>
      </div>
      <div style={{ padding: '22px 24px 0' }}>
        <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 13.5, color: DR.mute, margin: 0, lineHeight: 1.5, paddingTop: 15, borderTop: ed.hair }}>Your itinerary appears once there’s a place and a few days to fill.</p>
      </div>
    </PFrame>
  );
}

// ── STATE 3 · DATES ONLY (no place) ──
function HomeDates() {
  return (
    <PFrame h={852}>
      <FCover2 dates="EARLY JUNE · 5 NIGHTS"/>
      <VLine>Five slow days in June. Where shall we point them?</VLine>
      <div style={{ padding: '22px 24px 0' }}>
        <SectionLabel>The trip so far</SectionLabel>
        <StartSlot k="A PLACE" prompt="where to?" first/>
        <StartSlot k="DATES" value="Jun 2–7 · 5 nights"/>
        <StartSlot k="WHO" prompt="just you — invite the others"/>
      </div>
      <div style={{ padding: '22px 24px 0' }}>
        <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 13.5, color: DR.mute, margin: 0, lineHeight: 1.5, paddingTop: 15, borderTop: ed.hair }}>Pick a place and the days start filling. Want a few ideas for early June? <span style={{ color: DR.goldDeep }}>→</span></p>
      </div>
    </PFrame>
  );
}

// ── STATE 4 · PLACE + DATES (+people) — becoming the real Folio ──
function HomePlaceDates() {
  return (
    <PFrame h={852}>
      <FCover2 place="Lisbon" dates="IN 23 DAYS · JUN 2–7"/>
      <VLine>Lisbon in June, the two of you. I’ve started a shape — six open days, ready when you are.</VLine>
      <div style={{ padding: '20px 24px 0' }}>
        <SectionLabel>The trip so far</SectionLabel>
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: '4px 16px', padding: '13px 0', borderTop: ed.rule, borderBottom: ed.hair }}>
          {[['LISBON'], ['JUN 2–7'], ['YOU + ANA']].map(([v], i) => (
            <span key={i} style={{ display: 'inline-flex', alignItems: 'center', gap: 6, fontFamily: DR.serif, fontSize: 15.5, color: DR.ink }}>
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#3D7050" strokeWidth="2.6" strokeLinecap="round" strokeLinejoin="round"><path d="M4 12l5 5L20 6"/></svg>{v}
            </span>
          ))}
        </div>
      </div>
      {/* the itinerary invitation — empty spine, ready to plan */}
      <div style={{ padding: '20px 24px 0' }}>
        <SectionLabel right="6 OPEN DAYS">The days</SectionLabel>
        <div style={{ marginTop: 4 }}>
          {['SAT 2', 'SUN 3', 'MON 4'].map((d, i) => (
            <div key={i} style={{ display: 'grid', gridTemplateColumns: '54px 1fr', gap: 12, alignItems: 'center', padding: '12px 0', borderTop: i ? ed.hair : ed.rule }}>
              <span style={{ fontFamily: DR.mono, fontSize: 10, letterSpacing: 0.8, color: DR.faint, fontWeight: 600 }}>{d}</span>
              <span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 15, color: DR.faint }}>open</span>
            </div>
          ))}
        </div>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginTop: 13, paddingTop: 14, borderTop: ed.rule }}>
          <span style={{ fontFamily: DR.serif, fontSize: 18, fontWeight: 500, color: DR.ink, letterSpacing: -0.3 }}>Plan the days with Vesper</span>
          <span style={{ color: DR.goldDeep, fontSize: 17 }}>→</span>
        </div>
      </div>
    </PFrame>
  );
}

// ═══════════════════════════════════════════════════════════════
// THE LIGHT PICKERS — what each slot opens. Minimal, editorial.
// ═══════════════════════════════════════════════════════════════
const PHead = ({ kicker, title }) => (
  <>
    <div style={{ position: 'relative', height: 70, marginTop: -40, display: 'flex', alignItems: 'flex-end', justifyContent: 'space-between', padding: '0 22px' }}>
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke={DR.soft} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><path d="M14 6l-6 6 6 6"/></svg>
      <span style={{ fontFamily: DR.mono, fontSize: 9, letterSpacing: 2.4, color: DR.mute, fontWeight: 600, paddingBottom: 3 }}>{kicker}</span>
      <div style={{ width: 20 }}/>
    </div>
    <div style={{ padding: '20px 24px 0' }}>
      <h1 style={{ fontFamily: DR.serif, fontSize: 32, fontWeight: 500, letterSpacing: -0.7, lineHeight: 1, color: DR.ink, margin: 0 }}>{title}</h1>
    </div>
  </>
);

// ── PICK A PLACE — taste-led suggestions + freeform search ──
function PickPlace() {
  const picks = [['Lisbon', 'slow mornings, miradouros, tile light'], ['Mexico City', 'markets, mezcal, your kind of chaos'], ['Lofoten', 'the quiet you keep circling']];
  return (
    <PFrame>
      <PHead kicker="A PLACE" title="Where to?"/>
      <div style={{ padding: '18px 24px 0' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 11, paddingBottom: 12, borderBottom: ed.rule }}>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke={DR.faint} strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>
          <span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 15.5, color: DR.faint }}>search anywhere…</span>
        </div>
      </div>
      <div style={{ padding: '20px 24px 0' }}>
        <SectionLabel>From what you save</SectionLabel>
        <div style={{ marginTop: 6 }}>
          {picks.map(([p, why], i) => (
            <div key={p} style={{ display: 'flex', alignItems: 'center', gap: 14, padding: '14px 0', borderTop: i ? ed.hair : ed.rule }}>
              <div style={{ width: 48, height: 48, borderRadius: 10, overflow: 'hidden', flexShrink: 0 }}><StyleRiso w={48} h={48}/></div>
              <div style={{ flex: 1 }}>
                <div style={{ fontFamily: DR.serif, fontSize: 18, fontWeight: 500, color: DR.ink, letterSpacing: -0.3 }}>{p}</div>
                <div style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 13, color: DR.mute, marginTop: 1 }}>{why}</div>
              </div>
              <span style={{ color: DR.faint, fontSize: 16 }}>→</span>
            </div>
          ))}
        </div>
        <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 13.5, color: DR.mute, margin: '16px 0 0', lineHeight: 1.5 }}>Not sure yet? <span style={{ color: DR.goldDeep }}>Let me suggest somewhere for your taste →</span></p>
      </div>
    </PFrame>
  );
}

// ── PICK DATES — quick shapes + a warm calendar range ──
function PickDates() {
  const days = Array.from({ length: 30 }, (_, i) => i + 1);
  const inRange = (d) => d >= 2 && d <= 7;
  return (
    <PFrame>
      <PHead kicker="DATES" title="When?"/>
      <div style={{ padding: '18px 24px 0' }}>
        {[['A weekend', 'Fri–Sun'], ['About a week', '5–7 nights'], ['I’m flexible', 'let Vesper find the cheapest window']].map(([t, s], i) => (
          <div key={t} style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', padding: '13px 0', borderTop: i ? ed.hair : ed.rule }}>
            <span style={{ fontFamily: DR.serif, fontSize: 17, color: DR.ink, letterSpacing: -0.2 }}>{t}</span>
            <span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 13, color: DR.mute }}>{s}</span>
          </div>
        ))}
      </div>
      {/* a quiet calendar */}
      <div style={{ padding: '22px 24px 0' }}>
        <SectionLabel right="JUNE 2026">Or pick exact dates</SectionLabel>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(7, 1fr)', gap: 2, marginTop: 10 }}>
          {['M', 'T', 'W', 'T', 'F', 'S', 'S'].map((d, i) => <div key={i} style={{ textAlign: 'center', fontFamily: DR.mono, fontSize: 8.5, letterSpacing: 0.5, color: DR.faint, fontWeight: 600, paddingBottom: 6 }}>{d}</div>)}
          {days.map((d) => {
            const sel = inRange(d), edge = d === 2 || d === 7;
            return (
              <div key={d} style={{ aspectRatio: '1', display: 'flex', alignItems: 'center', justifyContent: 'center', position: 'relative', background: sel ? (edge ? DR.goldDeep : 'rgba(176,133,58,0.14)') : 'transparent', borderRadius: edge ? 999 : (sel ? 0 : 8) }}>
                <span style={{ fontFamily: DR.serif, fontSize: 14.5, color: edge ? '#fff' : (sel ? DR.goldDeep : DR.soft), fontWeight: edge ? 600 : 400 }}>{d}</span>
              </div>
            );
          })}
        </div>
        <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 14, color: DR.ink, margin: '16px 0 0', textAlign: 'center' }}>Jun 2 – 7 · <span style={{ color: DR.mute }}>5 nights</span></p>
      </div>
    </PFrame>
  );
}

// ── INVITE FRIENDS — recent companions, invite-not-manage ──
function PickFriends() {
  const people = [['A', 'Ana', 'Lisbon together, twice', '#A0703A'], ['M', 'Marco', 'last spring in Rome', '#3D5066'], ['J', 'Jo', 'the road trip', '#7C8F73']];
  return (
    <PFrame>
      <PHead kicker="WHO" title="Who’s coming?"/>
      <div style={{ padding: '14px 24px 0' }}>
        <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 15.5, color: DR.mute, margin: 0 }}>It’s just you for now. Add the people you travel with —</p>
      </div>
      <div style={{ padding: '18px 24px 0' }}>
        <SectionLabel>You usually travel with</SectionLabel>
        <div style={{ marginTop: 6 }}>
          {people.map(([m, n, why, c], i) => (
            <div key={n} style={{ display: 'flex', alignItems: 'center', gap: 13, padding: '13px 0', borderTop: i ? ed.hair : ed.rule }}>
              <div style={{ width: 38, height: 38, borderRadius: 999, background: c, display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#fff', fontFamily: DR.serif, fontSize: 16, fontWeight: 500, flexShrink: 0 }}>{m}</div>
              <div style={{ flex: 1 }}>
                <div style={{ fontFamily: DR.serif, fontSize: 17, fontWeight: 500, color: DR.ink, letterSpacing: -0.2 }}>{n}</div>
                <div style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 12.5, color: DR.mute, marginTop: 1 }}>{why}</div>
              </div>
              <span style={{ width: 26, height: 26, borderRadius: 999, border: `1px solid ${DR.hair}`, display: 'flex', alignItems: 'center', justifyContent: 'center', color: DR.soft, fontSize: 17, fontWeight: 300 }}>+</span>
            </div>
          ))}
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: 11, marginTop: 16, paddingTop: 15, borderTop: ed.rule }}>
          <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke={DR.goldDeep} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><path d="M10 13a5 5 0 0 0 7 0l2-2a5 5 0 0 0-7-7l-1 1M14 11a5 5 0 0 0-7 0l-2 2a5 5 0 0 0 7 7l1-1"/></svg>
          <span style={{ fontFamily: DR.serif, fontSize: 16, color: DR.ink, letterSpacing: -0.2 }}>Share an invite link</span>
        </div>
      </div>
    </PFrame>
  );
}

Object.assign(window, { HomeNull, HomePlace, HomeDates, HomePlaceDates, PickPlace, PickDates, PickFriends });
