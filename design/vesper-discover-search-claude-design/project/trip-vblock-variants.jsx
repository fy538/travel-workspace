// ═══════════════════════════════════════════════════════════════
// VESPER BLOCK VARIATIONS — five elegant treatments of the home's
// Vesper unit (replacing the big-button card), + an expanded slice.
// Reuses DR + StyleRiso + Ppl/CASTD.
// ═══════════════════════════════════════════════════════════════

const spark = (s = 14, c = DR.gold) => <svg width={s} height={s} viewBox="0 0 24 24" fill={c}><path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z"/></svg>;

// V1 · INLINE — Vesper writes on the page, no card. The action is a
// quiet underlined link inside the prose. Most editorial / least button.
function VB_Inline() {
  return (
    <div style={{ padding: '16px 22px 0' }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 7, marginBottom: 8 }}>
        {spark(13)}<span style={{ fontSize: 9, letterSpacing: 1.6, fontWeight: 700, color: DR.goldDeep }}>VESPER</span>
        <span style={{ marginLeft: 'auto', fontFamily: DR.mono, fontSize: 8.5, color: DR.faint, letterSpacing: 0.8 }}>1 OF 4 LEFT</span>
      </div>
      <p style={{ fontFamily: DR.serif, fontSize: 18, color: DR.ink, lineHeight: 1.4, margin: 0, letterSpacing: -0.15 }}>
        The last real gap is where you sleep nights 5–7. I’ve <span style={{ color: DR.blue, borderBottom: `1.5px solid ${DR.blue}`, fontWeight: 500 }}>shortlisted three</span> you’d like — or <span style={{ fontStyle: 'italic', color: DR.mute, borderBottom: `1px solid ${DR.faint}` }}>tell me more</span>.
      </p>
    </div>
  );
}

// V2 · QUIET LEDGER — left ochre rule, prose, a small text action row.
// Echoes the chat "rationale" block. No filled button.
function VB_Ledger() {
  return (
    <div style={{ padding: '16px 22px 0' }}>
      <div style={{ paddingLeft: 14, borderLeft: `2px solid ${DR.gold}` }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 7, marginBottom: 7 }}>
          {spark(12)}<span style={{ fontSize: 9, letterSpacing: 1.6, fontWeight: 700, color: DR.goldDeep }}>VESPER · 1 OF 4 LEFT</span>
        </div>
        <p style={{ fontFamily: DR.serif, fontSize: 16.5, color: DR.ink, lineHeight: 1.38, margin: 0, letterSpacing: -0.12, fontStyle: 'italic' }}>
          Where you sleep nights 5–7 is the last gap — three feel right.
        </p>
        <div style={{ display: 'flex', gap: 16, marginTop: 11 }}>
          <span style={{ fontSize: 13, fontWeight: 600, color: DR.blue, letterSpacing: -0.1 }}>See the three →</span>
          <span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 13, color: DR.mute }}>ask Vesper</span>
        </div>
      </div>
    </div>
  );
}

// V3 · OBJECT PEEK — echoes home "prepared" card: a thumbnail of the
// shortlist + title + chevron. The work is shown, not announced.
function VB_Object() {
  return (
    <div style={{ padding: '16px 20px 0' }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 7, marginBottom: 9, paddingLeft: 2 }}>
        {spark(13)}<span style={{ fontSize: 9, letterSpacing: 1.6, fontWeight: 700, color: DR.goldDeep }}>VESPER PREPARED · 1 OF 4 LEFT</span>
      </div>
      <div style={{ display: 'flex', alignItems: 'center', gap: 12, padding: '12px 13px', background: DR.card, borderRadius: 14, border: `0.5px solid ${DR.hair}` }}>
        {/* stacked thumbs */}
        <div style={{ position: 'relative', width: 56, height: 50, flexShrink: 0 }}>
          {[0,1,2].map(i => <div key={i} style={{ position: 'absolute', left: i*9, top: i*3, width: 38, height: 46, borderRadius: 6, overflow: 'hidden', border: `1.5px solid ${DR.card}`, boxShadow: '0 2px 6px -3px rgba(0,0,0,0.3)' }}><StyleRiso w={38} h={46}/></div>)}
        </div>
        <div style={{ flex: 1, minWidth: 0 }}>
          <div style={{ fontFamily: DR.serif, fontSize: 16, fontWeight: 500, color: DR.ink, letterSpacing: -0.2, lineHeight: 1.1 }}>Three stays for nights 5–7</div>
          <div style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 11.5, color: DR.mute, marginTop: 3 }}>quiet, on your slow-streets pattern</div>
        </div>
        <span style={{ color: DR.mute, fontSize: 18 }}>›</span>
      </div>
    </div>
  );
}

// V4 · CHIP TAIL — a single warm sentence, then a row of pill chips
// (one primary-tinted). Echoes chat suggested-actions. Light, tappable.
function VB_Chips() {
  return (
    <div style={{ padding: '16px 22px 0' }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 7, marginBottom: 8 }}>
        {spark(13)}<span style={{ fontSize: 9, letterSpacing: 1.6, fontWeight: 700, color: DR.goldDeep }}>VESPER</span>
        <span style={{ marginLeft: 'auto', fontFamily: DR.mono, fontSize: 8.5, color: DR.faint, letterSpacing: 0.8 }}>1 OF 4 LEFT</span>
      </div>
      <p style={{ fontFamily: DR.serif, fontSize: 17, color: DR.ink, lineHeight: 1.35, margin: 0, letterSpacing: -0.12 }}>
        Nights 5–7 are the last gap — I’ve found three you’d like.
      </p>
      <div style={{ display: 'flex', gap: 7, marginTop: 12, flexWrap: 'wrap' }}>
        <span style={{ padding: '7px 13px', borderRadius: 999, background: 'rgba(61,80,102,0.10)', border: `0.6px solid rgba(61,80,102,0.3)`, fontSize: 12.5, fontWeight: 600, color: DR.blue, letterSpacing: -0.05 }}>See the three</span>
        <span style={{ padding: '7px 13px', borderRadius: 999, background: DR.card, border: `0.5px solid ${DR.hair}`, fontFamily: DR.serif, fontStyle: 'italic', fontSize: 12.5, color: DR.soft }}>somewhere quieter</span>
        <span style={{ padding: '7px 13px', borderRadius: 999, background: DR.card, border: `0.5px solid ${DR.hair}`, fontFamily: DR.serif, fontStyle: 'italic', fontSize: 12.5, color: DR.soft }}>ask</span>
      </div>
    </div>
  );
}

// V5 · POSTSCRIPT — Vesper signs a one-line note; the action is a small
// "→" affordance aligned right, like a letter's reply. Freeform, calm.
function VB_Note() {
  return (
    <div style={{ padding: '16px 22px 0' }}>
      <div style={{ background: DR.cardSoft, borderRadius: 16, padding: '15px 16px' }}>
        <p style={{ fontFamily: DR.serif, fontSize: 16.5, color: DR.ink, lineHeight: 1.4, margin: 0, letterSpacing: -0.12 }}>
          “One thing before you go — pick where you sleep nights 5–7. I set aside three you’d like.”
        </p>
        <div style={{ marginTop: 12, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
          <span style={{ display: 'flex', alignItems: 'center', gap: 6 }}>{spark(12)}<span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 13, color: DR.mute }}>Vesper · 1 of 4 left</span></span>
          <span style={{ display: 'inline-flex', alignItems: 'center', gap: 6, fontSize: 12.5, fontWeight: 600, color: DR.blue }}>See them <span style={{ fontSize: 14 }}>→</span></span>
        </div>
      </div>
    </div>
  );
}

// ── Elaborate intelligence slice — text-forward, more per day, less art.
// Each day carries a couple of time-stamped sub-beats; one small scene chip
// at the header only. Informative preview, still capped + routes to full page.
function SliceRich() {
  const D2 = [
    { d: 'SAT 18', items: [['09:30', 'Land, drop bags in Alfama'], ['eve', 'Wander, no plans past first coffee']] },
    { d: 'SUN 19', items: [['morning', 'Miradouros east→west · Ana’s list'], ['13:00', 'Lunch at Ramiro']] },
    { d: 'MON 20', items: [['—', 'still open'], ], gap: true },
    { d: 'TUE 21', items: [['08:30', 'Belém, early for the cloister'], ['noon', 'Pastéis, standing at the counter']] },
  ];
  return (
    <div style={{ padding: '18px 20px 0' }}>
      <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', marginBottom: 12 }}>
        <span style={{ fontSize: 9, letterSpacing: 2, color: DR.mute, fontWeight: 700 }}>THE DAYS, IN DETAIL</span>
        <span style={{ fontSize: 9, letterSpacing: 1.2, color: DR.mute, fontWeight: 600 }}>4 OF 6 PLANNED</span>
      </div>
      {D2.map((day, di) => (
        <div key={di} style={{ display: 'grid', gridTemplateColumns: '56px 1fr 14px', gap: 12, padding: '11px 0', borderTop: di ? `0.5px solid ${DR.hairThin}` : 'none', alignItems: 'center' }}>
          <div style={{ fontFamily: DR.serif, fontSize: 15, fontWeight: 500, color: DR.ink, letterSpacing: -0.3, paddingTop: 1, alignSelf: 'start' }}>{day.d.split(' ')[1]}<span style={{ display: 'block', fontFamily: DR.mono, fontSize: 7.5, color: DR.mute, letterSpacing: 1, fontWeight: 600, marginTop: 2 }}>{day.d.split(' ')[0]}</span></div>
          <div>
            {day.items.map(([t, txt], ii) => (
              <div key={ii} style={{ display: 'flex', gap: 9, alignItems: 'baseline', marginTop: ii ? 6 : 0 }}>
                <span style={{ fontFamily: DR.mono, fontSize: 8.5, color: DR.faint, letterSpacing: 0.5, fontWeight: 600, width: 38, flexShrink: 0, textAlign: 'right' }}>{t}</span>
                <span style={{ fontFamily: DR.serif, fontSize: 13.5, color: day.gap ? DR.mute : DR.ink, fontStyle: day.gap ? 'italic' : 'normal', letterSpacing: -0.1, lineHeight: 1.25 }}>{txt}</span>
              </div>
            ))}
          </div>
          <span style={{ color: DR.faint, fontSize: 13, alignSelf: 'center' }}>›</span>
        </div>
      ))}
      <div style={{ marginTop: 12, textAlign: 'center' }}>
        <span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 12.5, color: DR.mute, letterSpacing: -0.05 }}>tap any day to open the itinerary</span>
      </div>
    </div>
  );
}
function SliceRichOld() {
  const beats = [
    { d: 'SAT 18', t: 'Land soft, settle in Alfama', tag: 'arrival' },
    { d: 'SUN 19', t: 'Miradouros east-to-west', tag: 'Ana’s list' },
    { d: 'MON 20', t: 'still open', tag: 'gap', gap: true },
    { d: 'TUE 21', t: 'Belém, early for the cloister', tag: 'set' },
  ];
  return (
    <div style={{ padding: '18px 20px 0' }}>
      <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', marginBottom: 11 }}>
        <span style={{ fontSize: 9, letterSpacing: 2, color: DR.mute, fontWeight: 700 }}>THE SHAPE SO FAR</span>
        <span style={{ fontSize: 9, letterSpacing: 1.2, color: DR.mute, fontWeight: 600 }}>4 OF 6 DAYS PLANNED</span>
      </div>
      {/* scene strip */}
      <div style={{ display: 'flex', gap: 6, marginBottom: 13 }}>
        {[0,1,2].map(i => <div key={i} style={{ flex: 1, height: 56, borderRadius: 8, overflow: 'hidden' }}><StyleRiso w={108} h={56}/></div>)}
      </div>
      {/* beats */}
      <div>
        {beats.map((b, i) => (
          <div key={i} style={{ display: 'grid', gridTemplateColumns: '54px 1fr auto', gap: 11, padding: '10px 0', borderTop: i ? `0.5px solid ${DR.hairThin}` : 'none', alignItems: 'center' }}>
            <span style={{ fontFamily: DR.mono, fontSize: 9.5, color: DR.mute, letterSpacing: 0.6, fontWeight: 600 }}>{b.d}</span>
            <span style={{ fontFamily: DR.serif, fontSize: 14.5, fontWeight: 500, color: b.gap ? DR.mute : DR.ink, fontStyle: b.gap ? 'italic' : 'normal', letterSpacing: -0.15 }}>{b.t}</span>
            <span style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 10.5, color: b.gap ? DR.goldDeep : DR.faint }}>{b.tag}</span>
          </div>
        ))}
      </div>
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginTop: 12, paddingTop: 12, borderTop: `0.5px solid ${DR.hairThin}` }}>
        <span style={{ fontFamily: DR.serif, fontSize: 14, fontWeight: 500, color: DR.ink, letterSpacing: -0.1 }}>Open the full itinerary</span>
        <span style={{ color: DR.blue, fontSize: 14 }}>→</span>
      </div>
    </div>
  );
}

// A stage to show a single block variation on paper.
function VBStage({ children, label }) {
  return (
    <div>
      <div style={{ fontFamily: DR.mono, fontSize: 9, letterSpacing: 1.2, color: DR.goldDeep, fontWeight: 600, marginBottom: 8 }}>{label}</div>
      <div style={{ width: 393, background: DR.paper, borderRadius: 20, border: `0.5px solid ${DR.hair}`, paddingBottom: 18 }}>{children}</div>
    </div>
  );
}

Object.assign(window, { VB_Inline, VB_Ledger, VB_Object, VB_Chips, VB_Note, SliceRich, VBStage });
