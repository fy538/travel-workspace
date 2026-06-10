// ═══════════════════════════════════════════════════════════════
// TRIPS · BLANK PAGE — the home IS the form.
// "Start with a blank page" (from Create) lands HERE, in a null
// single-trip home. You fill it by tapping a place / dates / who —
// any one, any order, none required. The home adapts to what's set.
// Native to the Trips token system (T / TR / Phone / Marks).
// ═══════════════════════════════════════════════════════════════

// Forming cover — identity comes from whatever's set so far.
function BlankCover({ place, dates }) {
  const has = !!place;
  return (
    <div style={{ position: 'relative', height: has ? 188 : 150, background: has ? TR.inkDeep : T.cardSoft, overflow: 'hidden' }}>
      {has && <div style={{ position: 'absolute', inset: 0, background: `linear-gradient(150deg, ${TR.ink}, ${TR.inkDeep})`, opacity: 0.96 }}/>}
      <div style={{ position: 'absolute', top: 16, left: 22, right: 22, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke={has ? 'rgba(255,255,255,0.9)' : T.inkSoft} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><path d="M14 6l-6 6 6 6"/></svg>
        <span style={{ fontFamily: T.mono, fontSize: 9, letterSpacing: 2.2, color: has ? 'rgba(255,255,255,0.8)' : T.mute, fontWeight: 600 }}>{has ? 'A NEW FOLIO' : 'NEW TRIP · DRAFT'}</span>
        <TripIcons.Dots s={18} c={has ? 'rgba(255,255,255,0.9)' : T.inkSoft}/>
      </div>
      <div style={{ position: 'absolute', left: 22, right: 22, bottom: 18 }}>
        {dates && <div style={{ fontFamily: T.mono, fontSize: 9, letterSpacing: 2, color: has ? 'rgba(255,255,255,0.85)' : T.goldDeep, fontWeight: 600, marginBottom: 6 }}>{dates}</div>}
        {has
          ? <h1 style={{ fontFamily: T.serif, fontSize: 38, fontWeight: 500, letterSpacing: -1.1, lineHeight: 0.95, color: '#fff', margin: 0 }}>{place}</h1>
          : <h1 style={{ fontFamily: T.serif, fontSize: 26, fontWeight: 500, fontStyle: 'italic', letterSpacing: -0.5, lineHeight: 1, color: T.muteSoft, margin: 0 }}>{dates ? 'where to?' : 'A trip, taking shape'}</h1>}
      </div>
    </div>
  );
}

function BlankVoice({ children }) {
  return (
    <div style={{ padding: '18px 24px 0' }}>
      <span style={{ fontFamily: T.mono, fontSize: 9, letterSpacing: 2.2, color: T.goldDeep, fontWeight: 600 }}>VESPER</span>
      <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 17.5, color: T.ink, lineHeight: 1.42, letterSpacing: -0.2, margin: '8px 0 0' }}>{children}</p>
    </div>
  );
}

function BlankSlot({ k, prompt, value, first }) {
  const set = !!value;
  return (
    <div style={{ display: 'grid', gridTemplateColumns: '74px 1fr 16px', gap: 12, alignItems: 'baseline', padding: '15px 0', borderTop: `0.5px solid ${first ? T.hairline : T.hairThin}` }}>
      <span style={{ fontFamily: T.mono, fontSize: 9, letterSpacing: 1.6, fontWeight: 600, color: set ? T.goldDeep : T.mute }}>{k}</span>
      <span style={{ fontFamily: T.serif, fontSize: 17, fontStyle: set ? 'normal' : 'italic', fontWeight: set ? 500 : 400, color: set ? T.ink : T.muteSoft, letterSpacing: -0.3, lineHeight: 1.2 }}>{set ? value : prompt}</span>
      {set
        ? <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#3D7050" strokeWidth="2.4" strokeLinecap="round" strokeLinejoin="round" style={{ alignSelf: 'center' }}><path d="M4 12l5 5L20 6"/></svg>
        : <Marks.ArrowR s={13} c={T.faint}/>}
    </div>
  );
}

const BlankLabel = ({ children, right }) => (
  <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', paddingBottom: 2 }}>
    <span style={{ fontFamily: T.mono, fontSize: 9, letterSpacing: 1.8, color: T.mute, fontWeight: 600 }}>{children}</span>
    {right && <span style={{ fontFamily: T.mono, fontSize: 8.5, letterSpacing: 1.4, color: T.muteSoft, fontWeight: 600 }}>{right}</span>}
  </div>
);

// ── 1 · BLANK — nothing set ──
function BlankNull() {
  return (
    <Phone bg={T.bg}>
      <BlankCover/>
      <BlankVoice>Start anywhere — a place, some dates, or who’s coming. I’ll shape the rest around it.</BlankVoice>
      <div style={{ padding: '20px 24px 0' }}>
        <BlankLabel>BEGIN WITH</BlankLabel>
        <BlankSlot k="A PLACE" prompt="where are we going?" first/>
        <BlankSlot k="DATES" prompt="when?"/>
        <BlankSlot k="WHO" prompt="who’s coming?"/>
      </div>
      <div style={{ padding: '20px 24px 0' }}>
        <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13.5, color: T.mute, margin: 0, lineHeight: 1.5, paddingTop: 15, borderTop: `0.5px solid ${T.hairThin}` }}>Nothing’s required — it’s already saved as a draft. Or <span style={{ color: T.goldDeep }}>tell me about it →</span></p>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

// ── 2 · PLACE ONLY ──
function BlankPlace() {
  return (
    <Phone bg={T.bg}>
      <BlankCover place="Lisbon"/>
      <BlankVoice>Lisbon — lovely. Tell me when, and I’ll start finding the shape of it.</BlankVoice>
      <div style={{ padding: '20px 24px 0' }}>
        <BlankLabel>THE TRIP SO FAR</BlankLabel>
        <BlankSlot k="A PLACE" value="Lisbon, Portugal" first/>
        <BlankSlot k="DATES" prompt="add when"/>
        <BlankSlot k="WHO" prompt="just you — invite the others"/>
      </div>
      <div style={{ padding: '20px 24px 0' }}>
        <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13.5, color: T.mute, margin: 0, lineHeight: 1.5, paddingTop: 15, borderTop: `0.5px solid ${T.hairThin}` }}>Your itinerary appears once there’s a place and a few days to fill.</p>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

// ── 3 · DATES ONLY ──
function BlankDates() {
  return (
    <Phone bg={T.bg}>
      <BlankCover dates="EARLY JUNE · 5 NIGHTS"/>
      <BlankVoice>Five slow days in June. Where shall we point them?</BlankVoice>
      <div style={{ padding: '20px 24px 0' }}>
        <BlankLabel>THE TRIP SO FAR</BlankLabel>
        <BlankSlot k="A PLACE" prompt="where to?" first/>
        <BlankSlot k="DATES" value="Jun 2–7 · 5 nights"/>
        <BlankSlot k="WHO" prompt="just you — invite the others"/>
      </div>
      <div style={{ padding: '20px 24px 0' }}>
        <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13.5, color: T.mute, margin: 0, lineHeight: 1.5, paddingTop: 15, borderTop: `0.5px solid ${T.hairThin}` }}>Pick a place and the days start filling. Want ideas for early June? <span style={{ color: T.goldDeep }}>→</span></p>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

// ── 4 · PLACE + DATES — becoming the real Folio ──
function BlankBoth() {
  return (
    <Phone bg={T.bg}>
      <BlankCover place="Lisbon" dates="IN 23 DAYS · JUN 2–7"/>
      <BlankVoice>Lisbon in June, the two of you. I’ve started a shape — six open days, ready when you are.</BlankVoice>
      <div style={{ padding: '18px 24px 0' }}>
        <BlankLabel>THE TRIP SO FAR</BlankLabel>
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: '4px 16px', padding: '12px 0', borderTop: `0.5px solid ${T.hairline}`, borderBottom: `0.5px solid ${T.hairThin}` }}>
          {['LISBON', 'JUN 2–7', 'YOU + ANA'].map((v) => (
            <span key={v} style={{ display: 'inline-flex', alignItems: 'center', gap: 6, fontFamily: T.serif, fontSize: 15.5, color: T.ink }}>
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#3D7050" strokeWidth="2.6" strokeLinecap="round" strokeLinejoin="round"><path d="M4 12l5 5L20 6"/></svg>{v}
            </span>
          ))}
        </div>
      </div>
      <div style={{ padding: '18px 24px 0' }}>
        <BlankLabel right="6 OPEN DAYS">THE DAYS</BlankLabel>
        <div style={{ marginTop: 4 }}>
          {['SAT 2', 'SUN 3', 'MON 4'].map((d, i) => (
            <div key={d} style={{ display: 'grid', gridTemplateColumns: '54px 1fr', gap: 12, alignItems: 'center', padding: '11px 0', borderTop: `0.5px solid ${i ? T.hairThin : T.hairline}` }}>
              <span style={{ fontFamily: T.mono, fontSize: 10, letterSpacing: 0.8, color: T.faint, fontWeight: 600 }}>{d}</span>
              <span style={{ fontFamily: T.serif, fontSize: 15, color: T.faint }}>open</span>
            </div>
          ))}
        </div>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginTop: 12, paddingTop: 13, borderTop: `0.5px solid ${T.hairline}` }}>
          <span style={{ fontFamily: T.serif, fontSize: 17, fontWeight: 500, color: T.ink, letterSpacing: -0.3 }}>Plan the days with Vesper</span>
          <Marks.ArrowR s={15} c={T.goldDeep}/>
        </div>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

// ═══════════ THE LIGHT PICKERS — what each slot opens ═══════════
const PickHead = ({ kicker, title }) => (
  <div style={{ padding: '16px 22px 0' }}>
    <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke={T.inkSoft} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><path d="M14 6l-6 6 6 6"/></svg>
      <span style={{ fontFamily: T.mono, fontSize: 9, letterSpacing: 2.2, color: T.mute, fontWeight: 600 }}>{kicker}</span>
      <span style={{ width: 20 }}/>
    </div>
    <h1 style={{ fontFamily: T.serif, fontSize: 32, fontWeight: 500, letterSpacing: -0.7, lineHeight: 1, color: T.ink, margin: '18px 0 0' }}>{title}</h1>
  </div>
);

function PickPlaceT() {
  const picks = [['Lisbon', 'slow mornings, miradouros, tile light'], ['Mexico City', 'markets, mezcal, your kind of chaos'], ['Lofoten', 'the quiet you keep circling']];
  return (
    <Phone bg={T.bg}>
      <PickHead kicker="A PLACE" title="Where to?"/>
      <div style={{ padding: '18px 22px 0' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 11, paddingBottom: 12, borderBottom: `0.5px solid ${T.hairline}` }}>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke={T.faint} strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>
          <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 15.5, color: T.faint }}>search anywhere…</span>
        </div>
      </div>
      <div style={{ padding: '18px 22px 0' }}>
        <BlankLabel>FROM WHAT YOU SAVE</BlankLabel>
        <div style={{ marginTop: 4 }}>
          {picks.map(([p, why], i) => (
            <div key={p} style={{ display: 'flex', alignItems: 'center', gap: 14, padding: '13px 0', borderTop: `0.5px solid ${i ? T.hairThin : T.hairline}` }}>
              <div style={{ width: 46, height: 46, borderRadius: 10, background: T.cardSoft, border: `0.5px solid ${T.hairline}`, flexShrink: 0 }}/>
              <div style={{ flex: 1 }}>
                <div style={{ fontFamily: T.serif, fontSize: 18, fontWeight: 500, color: T.ink, letterSpacing: -0.3 }}>{p}</div>
                <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13, color: T.mute, marginTop: 1 }}>{why}</div>
              </div>
              <Marks.ArrowR s={13} c={T.faint}/>
            </div>
          ))}
        </div>
        <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13.5, color: T.mute, margin: '15px 0 0', lineHeight: 1.5 }}>Not sure yet? <span style={{ color: T.goldDeep }}>Let me suggest somewhere for your taste →</span></p>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

function PickDatesT() {
  const days = Array.from({ length: 30 }, (_, i) => i + 1);
  const inRange = (d) => d >= 2 && d <= 7;
  return (
    <Phone bg={T.bg}>
      <PickHead kicker="DATES" title="When?"/>
      <div style={{ padding: '18px 22px 0' }}>
        {[['A weekend', 'Fri–Sun'], ['About a week', '5–7 nights'], ['I’m flexible', 'let Vesper find the cheapest window']].map(([t, s], i) => (
          <div key={t} style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', padding: '13px 0', borderTop: `0.5px solid ${i ? T.hairThin : T.hairline}` }}>
            <span style={{ fontFamily: T.serif, fontSize: 17, color: T.ink, letterSpacing: -0.2 }}>{t}</span>
            <span style={{ fontFamily: T.serif, fontSize: 13, color: T.mute }}>{s}</span>
          </div>
        ))}
      </div>
      <div style={{ padding: '20px 22px 0' }}>
        <BlankLabel right="JUNE 2026">OR PICK EXACT DATES</BlankLabel>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(7, 1fr)', gap: 2, marginTop: 10 }}>
          {['M', 'T', 'W', 'T', 'F', 'S', 'S'].map((d, i) => <div key={i} style={{ textAlign: 'center', fontFamily: T.mono, fontSize: 8.5, letterSpacing: 0.5, color: T.faint, fontWeight: 600, paddingBottom: 6 }}>{d}</div>)}
          {days.map((d) => {
            const sel = inRange(d), edge = d === 2 || d === 7;
            return (
              <div key={d} style={{ aspectRatio: '1', display: 'flex', alignItems: 'center', justifyContent: 'center', background: sel ? (edge ? T.goldDeep : 'rgba(176,133,58,0.14)') : 'transparent', borderRadius: edge ? 999 : (sel ? 0 : 8) }}>
                <span style={{ fontFamily: T.serif, fontSize: 14.5, color: edge ? '#fff' : (sel ? T.goldDeep : T.soft), fontWeight: edge ? 600 : 400 }}>{d}</span>
              </div>
            );
          })}
        </div>
        <p style={{ fontFamily: T.serif, fontSize: 14, color: T.ink, margin: '15px 0 0', textAlign: 'center' }}>Jun 2 – 7 · <span style={{ color: T.mute }}>5 nights</span></p>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

function PickFriendsT() {
  const people = [['A', 'Ana', 'Lisbon together, twice', '#A0703A'], ['M', 'Marco', 'last spring in Rome', '#3D5066'], ['J', 'Jo', 'the road trip', '#7C8F73']];
  return (
    <Phone bg={T.bg}>
      <PickHead kicker="WHO" title="Who’s coming?"/>
      <div style={{ padding: '14px 22px 0' }}>
        <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 15.5, color: T.mute, margin: 0 }}>It’s just you for now. Add the people you travel with —</p>
      </div>
      <div style={{ padding: '16px 22px 0' }}>
        <BlankLabel>YOU USUALLY TRAVEL WITH</BlankLabel>
        <div style={{ marginTop: 4 }}>
          {people.map(([m, n, why, c], i) => (
            <div key={n} style={{ display: 'flex', alignItems: 'center', gap: 13, padding: '12px 0', borderTop: `0.5px solid ${i ? T.hairThin : T.hairline}` }}>
              <div style={{ width: 38, height: 38, borderRadius: 999, background: c, display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#fff', fontFamily: T.serif, fontSize: 16, fontWeight: 500, flexShrink: 0 }}>{m}</div>
              <div style={{ flex: 1 }}>
                <div style={{ fontFamily: T.serif, fontSize: 17, fontWeight: 500, color: T.ink, letterSpacing: -0.2 }}>{n}</div>
                <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12.5, color: T.mute, marginTop: 1 }}>{why}</div>
              </div>
              <span style={{ width: 26, height: 26, borderRadius: 999, border: `1px solid ${T.hairline}`, display: 'flex', alignItems: 'center', justifyContent: 'center', color: T.soft, fontSize: 17, fontWeight: 300 }}>+</span>
            </div>
          ))}
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: 11, marginTop: 15, paddingTop: 14, borderTop: `0.5px solid ${T.hairline}` }}>
          <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke={T.goldDeep} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><path d="M10 13a5 5 0 0 0 7 0l2-2a5 5 0 0 0-7-7l-1 1M14 11a5 5 0 0 0-7 0l-2 2a5 5 0 0 0 7 7l1-1"/></svg>
          <span style={{ fontFamily: T.serif, fontSize: 16, color: T.ink, letterSpacing: -0.2 }}>Share an invite link</span>
        </div>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

Object.assign(window, { BlankNull, BlankPlace, BlankDates, BlankBoth, PickPlaceT, PickDatesT, PickFriendsT });
