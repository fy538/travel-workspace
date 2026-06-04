// ═══════════════════════════════════════════════════════════════
// THE LIGHT PICKERS · variations — sleek/editorial, 3 takes each.
// All in the uniform iPhone frame (PFrame h=852). Reuses DR, ed,
// EdKick, StyleRiso, PHead, SectionLabel.
// ═══════════════════════════════════════════════════════════════

const PH = 852; // uniform screen height

// ───────────────────────── PLACE ─────────────────────────

// PLACE · A — taste list (refined): search + saved-place rows.
function PlaceList() {
  const picks = [['Lisbon', 'slow mornings, miradouros, tile light'], ['Mexico City', 'markets, mezcal, your kind of chaos'], ['Lofoten', 'the quiet you keep circling'], ['Kyoto', 'the temples you bookmarked in spring']];
  return (
    <PFrame h={PH}>
      <PHead kicker="A PLACE" title="Where to?"/>
      <div style={{ padding: '18px 24px 0' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 11, paddingBottom: 12, borderBottom: ed.rule }}>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke={DR.faint} strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>
          <span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 15.5, color: DR.faint }}>search anywhere…</span>
        </div>
      </div>
      <div style={{ padding: '20px 24px 0' }}>
        <SectionLabel>From what you save</SectionLabel>
        <div style={{ marginTop: 4 }}>
          {picks.map(([p, why], i) => (
            <div key={p} style={{ display: 'flex', alignItems: 'center', gap: 14, padding: '14px 0', borderTop: i ? ed.hair : ed.rule }}>
              <div style={{ width: 46, height: 46, borderRadius: 10, overflow: 'hidden', flexShrink: 0 }}><StyleRiso w={46} h={46}/></div>
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

// PLACE · B — gallery: full-bleed editorial plates, fewer & bigger.
function PlatePlace({ name, why, h = 150 }) {
  return (
    <div style={{ position: 'relative', height: h, borderRadius: 16, overflow: 'hidden', marginBottom: 12 }}>
      <StyleRiso w={345} h={h}/>
      <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to top, rgba(20,14,9,0.74), rgba(20,14,9,0) 62%)' }}/>
      <div style={{ position: 'absolute', left: 16, right: 16, bottom: 13 }}>
        <h3 style={{ fontFamily: DR.serif, fontSize: 25, fontWeight: 500, color: '#fff', margin: 0, letterSpacing: -0.5 }}>{name}</h3>
        <div style={{ display: 'flex', alignItems: 'flex-end', justifyContent: 'space-between', marginTop: 3 }}>
          <span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 13, color: 'rgba(255,255,255,0.88)', maxWidth: 240, lineHeight: 1.3 }}>{why}</span>
          <span style={{ color: '#fff', fontSize: 16 }}>→</span>
        </div>
      </div>
    </div>
  );
}
function PlaceGallery() {
  return (
    <PFrame h={PH}>
      <PHead kicker="A PLACE" title="Where to?"/>
      <div style={{ padding: '14px 24px 0' }}>
        <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 14.5, color: DR.mute, margin: '0 0 16px', lineHeight: 1.4 }}>Three I’d point you toward, from what you keep saving —</p>
        <PlatePlace name="Lisbon" why="slow mornings, miradouros, the tile light" h={166}/>
        <PlatePlace name="Mexico City" why="markets, mezcal, your kind of chaos" h={150}/>
        <PlatePlace name="Lofoten" why="the quiet you keep circling" h={150}/>
        <div style={{ display: 'flex', alignItems: 'center', gap: 11, paddingTop: 14, borderTop: ed.rule, marginTop: 2 }}>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke={DR.faint} strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>
          <span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 15, color: DR.faint }}>somewhere else…</span>
        </div>
      </div>
    </PFrame>
  );
}

// PLACE · C — the index: typographic, no images, literary.
function PlaceIndex() {
  const rows = [['I', 'Lisbon', 'Portugal', 'slow mornings, tile light'], ['II', 'Mexico City', 'Mexico', 'markets, mezcal, chaos'], ['III', 'Lofoten', 'Norway', 'the quiet you circle'], ['IV', 'Kyoto', 'Japan', 'temples, in spring']];
  return (
    <PFrame h={PH}>
      <PHead kicker="A PLACE" title="Where to?"/>
      <div style={{ padding: '16px 24px 0' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 11, paddingBottom: 14, borderBottom: ed.rule }}>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke={DR.faint} strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>
          <span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 15.5, color: DR.faint }}>search anywhere…</span>
        </div>
        <div style={{ marginTop: 6 }}>
          <EdKick>From what you save</EdKick>
          <div style={{ marginTop: 8 }}>
            {rows.map(([n, name, region, why], i) => (
              <div key={name} style={{ display: 'grid', gridTemplateColumns: '26px 1fr', gap: 14, alignItems: 'baseline', padding: '16px 0', borderTop: i ? ed.hair : ed.rule }}>
                <span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 15, color: DR.goldDeep }}>{n}</span>
                <div>
                  <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between' }}>
                    <span style={{ fontFamily: DR.serif, fontSize: 23, fontWeight: 500, color: DR.ink, letterSpacing: -0.5, lineHeight: 1 }}>{name}</span>
                    <span style={{ fontFamily: DR.mono, fontSize: 8.5, letterSpacing: 1.6, color: DR.faint, fontWeight: 600 }}>{region.toUpperCase()}</span>
                  </div>
                  <div style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 13.5, color: DR.mute, marginTop: 3 }}>{why}</div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </PFrame>
  );
}

// ───────────────────────── DATES ─────────────────────────

// Shared mini month grid. tone: 'quiet' | 'paper'
function CalMonth({ paper }) {
  const days = Array.from({ length: 30 }, (_, i) => i + 1);
  const inRange = (d) => d >= 2 && d <= 7;
  return (
    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(7, 1fr)', gap: paper ? 3 : 2 }}>
      {['M', 'T', 'W', 'T', 'F', 'S', 'S'].map((d, i) => <div key={i} style={{ textAlign: 'center', fontFamily: DR.mono, fontSize: 8.5, letterSpacing: 0.5, color: DR.faint, fontWeight: 600, paddingBottom: 7 }}>{d}</div>)}
      {days.map((d) => {
        const sel = inRange(d), edge = d === 2 || d === 7;
        return (
          <div key={d} style={{ aspectRatio: '1', display: 'flex', alignItems: 'center', justifyContent: 'center', background: sel ? (edge ? DR.goldDeep : 'rgba(176,133,58,0.14)') : 'transparent', borderRadius: edge ? 999 : (sel ? 0 : 8) }}>
            <span style={{ fontFamily: DR.serif, fontSize: paper ? 16 : 14.5, color: edge ? '#fff' : (sel ? DR.goldDeep : DR.soft), fontWeight: edge ? 600 : 400 }}>{d}</span>
          </div>
        );
      })}
    </div>
  );
}

// DATES · A — quick shapes + quiet calendar.
function DatesShapes() {
  return (
    <PFrame h={PH}>
      <PHead kicker="DATES" title="When?"/>
      <div style={{ padding: '18px 24px 0' }}>
        {[['A weekend', 'Fri–Sun'], ['About a week', '5–7 nights'], ['I’m flexible', 'let Vesper find the cheapest window']].map(([t, s], i) => (
          <div key={t} style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', padding: '13px 0', borderTop: i ? ed.hair : ed.rule }}>
            <span style={{ fontFamily: DR.serif, fontSize: 17, color: DR.ink, letterSpacing: -0.2 }}>{t}</span>
            <span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 13, color: DR.mute }}>{s}</span>
          </div>
        ))}
      </div>
      <div style={{ padding: '22px 24px 0' }}>
        <SectionLabel right="JUNE 2026">Or pick exact dates</SectionLabel>
        <div style={{ marginTop: 10 }}><CalMonth/></div>
        <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 14, color: DR.ink, margin: '16px 0 0', textAlign: 'center' }}>Jun 2 – 7 · <span style={{ color: DR.mute }}>5 nights</span></p>
      </div>
    </PFrame>
  );
}

// DATES · B — intent ribbon: roughly-when months + how-long, flexible-first.
function DatesRibbon() {
  const months = ['MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT'];
  return (
    <PFrame h={PH}>
      <PHead kicker="DATES" title="Roughly when?"/>
      <div style={{ padding: '16px 0 0' }}>
        <div style={{ padding: '0 24px' }}><EdKick>A month, to start</EdKick></div>
        <div style={{ display: 'flex', gap: 9, overflow: 'hidden', padding: '12px 24px 4px' }}>
          {months.map((m, i) => (
            <div key={m} style={{ flexShrink: 0, padding: '11px 16px', borderRadius: 999, border: `0.5px solid ${i === 1 ? DR.goldDeep : DR.hair}`, background: i === 1 ? DR.goldDeep : 'transparent' }}>
              <span style={{ fontFamily: DR.mono, fontSize: 10.5, letterSpacing: 1.4, fontWeight: 600, color: i === 1 ? '#fff' : DR.soft }}>{m}</span>
            </div>
          ))}
        </div>
      </div>
      <div style={{ padding: '24px 24px 0' }}>
        <SectionLabel>How long?</SectionLabel>
        <div style={{ marginTop: 4 }}>
          {[['A long weekend', '3 nights'], ['About a week', '5–7 nights', true], ['Two weeks', '14 nights']].map(([t, s, on], i) => (
            <div key={t} style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '13px 0', borderTop: i ? ed.hair : ed.rule }}>
              <span style={{ fontFamily: DR.serif, fontSize: 17, color: DR.ink, letterSpacing: -0.2 }}>{t}</span>
              <span style={{ display: 'flex', alignItems: 'center', gap: 9 }}>
                <span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 13, color: DR.mute }}>{s}</span>
                {on && <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#3D7050" strokeWidth="2.4" strokeLinecap="round" strokeLinejoin="round"><path d="M4 12l5 5L20 6"/></svg>}
              </span>
            </div>
          ))}
        </div>
        <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 14, color: DR.soft, margin: '20px 0 0', lineHeight: 1.5, paddingTop: 16, borderTop: ed.rule }}>A week in June, then. I’ll watch fares and nudge you toward the best stretch. <span style={{ color: DR.goldDeep }}>Pin exact dates →</span></p>
      </div>
    </PFrame>
  );
}

// DATES · C — paper spread: a single large editorial month.
function DatesPaper() {
  return (
    <PFrame h={PH}>
      <PHead kicker="DATES" title="When?"/>
      <div style={{ padding: '26px 26px 0' }}>
        <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', marginBottom: 18 }}>
          <h2 style={{ fontFamily: DR.serif, fontSize: 30, fontWeight: 500, fontStyle: 'italic', color: DR.ink, letterSpacing: -0.6, margin: 0 }}>June</h2>
          <span style={{ fontFamily: DR.mono, fontSize: 9.5, letterSpacing: 2, color: DR.faint, fontWeight: 600 }}>2026</span>
        </div>
        <CalMonth paper/>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginTop: 22, paddingTop: 16, borderTop: ed.rule }}>
          <div>
            <div style={{ fontFamily: DR.serif, fontSize: 19, fontWeight: 500, color: DR.ink, letterSpacing: -0.3 }}>Jun 2 – 7</div>
            <div style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 13, color: DR.mute, marginTop: 1 }}>five nights</div>
          </div>
          <span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 13.5, color: DR.goldDeep }}>flexible? →</span>
        </div>
      </div>
    </PFrame>
  );
}

// ───────────────────────── FRIENDS ─────────────────────────

const Mono = ({ m, c, size = 38 }) => <div style={{ width: size, height: size, borderRadius: 999, background: c, display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#fff', fontFamily: DR.serif, fontSize: size * 0.42, fontWeight: 500, flexShrink: 0 }}>{m}</div>;
const PEOPLE = [['A', 'Ana', 'Lisbon together, twice', '#A0703A'], ['M', 'Marco', 'last spring in Rome', '#3D5066'], ['J', 'Jo', 'the road trip', '#7C8F73'], ['S', 'Sam', 'Tokyo, ’24', '#9A5B4C']];

// FRIENDS · A — companions list.
function FriendsList() {
  return (
    <PFrame h={PH}>
      <PHead kicker="WHO" title="Who’s coming?"/>
      <div style={{ padding: '14px 24px 0' }}>
        <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 15.5, color: DR.mute, margin: 0 }}>It’s just you for now. Add the people you travel with —</p>
      </div>
      <div style={{ padding: '18px 24px 0' }}>
        <SectionLabel>You usually travel with</SectionLabel>
        <div style={{ marginTop: 6 }}>
          {PEOPLE.map(([m, n, why, c], i) => (
            <div key={n} style={{ display: 'flex', alignItems: 'center', gap: 13, padding: '13px 0', borderTop: i ? ed.hair : ed.rule }}>
              <Mono m={m} c={c}/>
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

// FRIENDS · B — roster: faces forward, a forming guest line.
function FriendsRoster() {
  return (
    <PFrame h={PH}>
      <PHead kicker="WHO" title="Who’s coming?"/>
      {/* coming along — forming line */}
      <div style={{ padding: '18px 24px 0' }}>
        <EdKick>Coming along</EdKick>
        <div style={{ display: 'flex', alignItems: 'center', gap: -8, marginTop: 12 }}>
          <Mono m="You" c={DR.ink} size={48}/>
          <div style={{ marginLeft: 10 }}><Mono m="A" c="#A0703A" size={48}/></div>
          <span style={{ width: 48, height: 48, borderRadius: 999, border: `1.5px dashed ${DR.faint}`, display: 'flex', alignItems: 'center', justifyContent: 'center', color: DR.faint, fontSize: 24, fontWeight: 300, marginLeft: 10 }}>+</span>
        </div>
        <p style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 14, color: DR.mute, margin: '14px 0 0' }}>You and Ana so far.</p>
      </div>
      {/* tap to add */}
      <div style={{ padding: '22px 24px 0' }}>
        <div style={{ paddingBottom: 14, borderBottom: ed.rule }}><EdKick>Tap to add</EdKick></div>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: 16, marginTop: 16 }}>
          {PEOPLE.map(([m, n, , c]) => (
            <div key={n} style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 7 }}>
              <Mono m={m} c={c} size={54}/>
              <span style={{ fontFamily: DR.serif, fontSize: 13, color: DR.soft }}>{n}</span>
            </div>
          ))}
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: 11, marginTop: 24, paddingTop: 15, borderTop: ed.rule }}>
          <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke={DR.goldDeep} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><path d="M10 13a5 5 0 0 0 7 0l2-2a5 5 0 0 0-7-7l-1 1M14 11a5 5 0 0 0-7 0l-2 2a5 5 0 0 0 7 7l1-1"/></svg>
          <span style={{ fontFamily: DR.serif, fontSize: 16, color: DR.ink, letterSpacing: -0.2 }}>Share an invite link</span>
        </div>
      </div>
    </PFrame>
  );
}

// FRIENDS · C — editorial invite line: names as fill-in chips.
function FriendsInvite() {
  return (
    <PFrame h={PH}>
      <PHead kicker="WHO" title="Who’s in?"/>
      <div style={{ padding: '24px 26px 0' }}>
        <p style={{ fontFamily: DR.serif, fontSize: 23, fontWeight: 400, color: DR.soft, lineHeight: 1.6, letterSpacing: -0.3, margin: 0 }}>
          It’s <span style={{ fontWeight: 500, color: DR.ink }}>you</span>, and{' '}
          <span style={{ fontWeight: 500, color: DR.ink, borderBottom: `1.5px solid ${DR.goldDeep}`, paddingBottom: 1 }}>Ana</span>,{' '}
          <span style={{ fontStyle: 'italic', color: DR.faint, borderBottom: `1.5px solid ${DR.faint}`, paddingBottom: 1 }}>and whoever else…</span>
        </p>
      </div>
      <div style={{ padding: '30px 24px 0' }}>
        <div style={{ paddingBottom: 4 }}><EdKick>Add from your people</EdKick></div>
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: 9, marginTop: 12 }}>
          {PEOPLE.slice(1).map(([m, n, , c]) => (
            <span key={n} style={{ display: 'inline-flex', alignItems: 'center', gap: 8, padding: '8px 14px 8px 8px', borderRadius: 999, border: `0.5px solid ${DR.hair}`, background: DR.card }}>
              <Mono m={m} c={c} size={24}/>
              <span style={{ fontFamily: DR.serif, fontSize: 15, color: DR.ink }}>{n}</span>
              <span style={{ color: DR.faint, fontSize: 15, fontWeight: 300 }}>+</span>
            </span>
          ))}
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: 11, marginTop: 26, paddingTop: 16, borderTop: ed.rule }}>
          <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke={DR.goldDeep} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><path d="M10 13a5 5 0 0 0 7 0l2-2a5 5 0 0 0-7-7l-1 1M14 11a5 5 0 0 0-7 0l-2 2a5 5 0 0 0 7 7l1-1"/></svg>
          <span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 15, color: DR.soft }}>or share an invite link instead</span>
        </div>
      </div>
    </PFrame>
  );
}

Object.assign(window, {
  PlaceList, PlaceGallery, PlaceIndex,
  DatesShapes, DatesRibbon, DatesPaper,
  FriendsList, FriendsRoster, FriendsInvite,
});
