// ─── CHAT CARDS 9–15 ────────────────────────────────────────────

// 9 · RECOMMENDATION RATIONALE BLOCK ─────────────────────────────
// Not a bubble — a quiet block (the "why" expansion under a card).
// Most privacy-sensitive: personal taste in 1:1, depersonalised in group.
function RationaleBlock({ ctx = 'solo' }) {
  const group = ctx === 'group';
  const evidence = group
    ? ['3 of you saved quiet-alley stays', 'the group skews early mornings', 'two asked for non-touristy']
    : ['you saved Alfama, Yanaka, Ribeira', 'you star morning-light photos', 'you skip big hotels'];
  return (
    <div style={{
      borderLeft: `2px solid ${T.gold}`, paddingLeft: 14, paddingTop: 2, paddingBottom: 2,
    }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 6, marginBottom: 8 }}>
        <VesperMark s={11} c={T.gold}/>
        <span style={{ fontSize: 9, letterSpacing: 1.5, fontWeight: 700, color: T.goldDeep }}>
          {group ? 'WHY — FROM THE GROUP’S SAVES' : 'WHY — I CHOSE THIS FOR YOU'}
        </span>
      </div>
      <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
        {evidence.map((e, i) => (
          <div key={i} style={{ display: 'flex', gap: 8, alignItems: 'baseline' }}>
            <span style={{ width: 4, height: 4, borderRadius: 4, background: T.muteSoft, marginTop: 6, flexShrink: 0 }}/>
            <span style={{ fontFamily: T.serif, fontSize: 13.5, color: T.inkSoft, lineHeight: 1.35, letterSpacing: -0.05 }}>{e}</span>
          </div>
        ))}
      </div>
      {group && (
        <div style={{ marginTop: 9 }}><PrivacyTag>your personal taste stays in your 1:1</PrivacyTag></div>
      )}
      <div style={{ marginTop: 10, fontSize: 11, color: T.muteSoft, letterSpacing: 0.2, fontWeight: 600 }}>
        {group ? 'Based on shared saves · tap to adjust' : 'Tap any line to tune what I weigh'}
      </div>
    </div>
  );
}

// 10 · VOICE SEGMENT ─────────────────────────────────────────────
function VoiceSegmentCard({ ctx = 'solo' }) {
  const group = ctx === 'group';
  return (
    <ChatCard>
      <div style={{ padding: '13px 15px 13px' }}>
        <CardHead glyph={ChatGlyph.wave(T.ink)} kind={group ? 'VOICE · SHARED CLIP' : 'VOICE · WHAT I HEARD'} right="0:08"/>
        {/* waveform + play */}
        <div style={{ display: 'flex', alignItems: 'center', gap: 12, marginBottom: 11 }}>
          <div style={{
            width: 38, height: 38, borderRadius: 999, background: T.ink, color: T.cardWarm, flexShrink: 0,
            display: 'flex', alignItems: 'center', justifyContent: 'center',
          }}>
            <svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>
          </div>
          <div style={{ flex: 1, display: 'flex', alignItems: 'center', gap: 2, height: 30 }}>
            {[8,14,20,12,26,16,30,18,24,10,20,14,28,12,18,8,22,14,10,16,24,12].map((h,i)=>(
              <div key={i} style={{ flex: 1, height: h, background: i < 9 ? T.ink : T.muteSoft, opacity: i < 9 ? 0.8 : 0.4, borderRadius: 1 }}/>
            ))}
          </div>
        </div>
        <p style={{
          fontFamily: T.serif, fontStyle: 'italic', fontSize: 14.5, color: T.ink, margin: 0,
          lineHeight: 1.4, letterSpacing: -0.1,
        }}>
          “find me a ryokan near Yanaka, but quieter — nights five and six.”
        </p>
        {group && <div style={{ marginTop: 9 }}><PrivacyTag>only shared because you tapped “send clip”</PrivacyTag></div>}
        <div style={{ marginTop: 11 }}>
          <ChatActions ctx={ctx} primary={group ? 'Play' : 'Use this'}
            secondary={group ? ['Hide'] : ['edit transcript', 'redo']}/>
        </div>
      </div>
    </ChatCard>
  );
}

// 11 · NARRATION / GUIDE ─────────────────────────────────────────
function NarrationCard({ ctx = 'solo' }) {
  const group = ctx === 'group';
  return (
    <ChatCard tint={T.cardSoft}>
      <div style={{ padding: '14px 16px 13px' }}>
        <CardHead glyph={ChatGlyph.guide(T.ink)} vesper={!group} kind={group ? 'GUIDE · SHARED' : 'WALKING WITH YOU'} right="3 MIN"/>
        <p style={{
          fontFamily: T.serif, fontSize: 15.5, color: T.ink, margin: '0 0 10px',
          lineHeight: 1.5, letterSpacing: -0.1,
        }}>
          As you leave the café, keep the cemetery wall on your left. The street
          narrows and the city goes quiet — <span style={{ fontStyle: 'italic' }}>that’s the one you want.</span>
        </p>
        <div style={{ display: 'flex', alignItems: 'center', gap: 12, padding: '8px 10px', background: T.cardWarm, borderRadius: 999, border: `0.5px solid ${T.hairline}` }}>
          <div style={{ width: 30, height: 30, borderRadius: 999, background: T.ink, color: T.cardWarm, display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0 }}>
            <svg width="11" height="11" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>
          </div>
          <div style={{ flex: 1, height: 3, background: T.hairline, borderRadius: 3, position: 'relative' }}>
            <div style={{ position: 'absolute', left: 0, top: 0, bottom: 0, width: '30%', background: T.gold, borderRadius: 3 }}/>
          </div>
          <span style={{ fontFamily: T.mono, fontSize: 9, color: T.mute, letterSpacing: 1 }}>0:54</span>
        </div>
        <div style={{ marginTop: 11 }}>
          <ChatActions ctx={ctx} primary={group ? 'Play for all' : 'Continue'}
            secondary={group ? [] : ['read instead', 'pause guiding']}/>
        </div>
      </div>
    </ChatCard>
  );
}

// 12 · MEMORY / ATLAS ARTIFACT DRAFT ─────────────────────────────
function AtlasDraftCard({ ctx = 'solo' }) {
  const group = ctx === 'group';
  return (
    <ChatCard>
      <div style={{ padding: 13 }}>
        <CardHead glyph={ChatGlyph.postcard(T.ink)} vesper={!group}
          kind={group ? 'FOR THE SHARED ALBUM' : 'A POSTCARD, DRAFTED'} right="ATLAS"/>
        <div style={{ display: 'flex', gap: 12 }}>
          <div style={{ width: 92, height: 112, transform: 'rotate(-2.5deg)', flexShrink: 0, marginLeft: 4, marginTop: 2 }}>
            <div style={{ width: '100%', height: '100%', background: T.cardWarm, borderRadius: 4, border: `0.5px solid ${T.hairline}`, boxShadow: '0 8px 18px -10px rgba(0,0,0,0.22)', padding: 5 }}>
              <div style={{ width: '100%', height: '100%', borderRadius: 2, overflow: 'hidden', border: `0.5px solid ${T.hairThin}` }}>
                <PostcardScene scene="lisbon"/>
              </div>
            </div>
          </div>
          <div style={{ flex: 1, minWidth: 0, paddingTop: 4 }}>
            <div style={{ fontFamily: T.serif, fontSize: 17, fontWeight: 500, color: T.ink, letterSpacing: -0.3, lineHeight: 1.1 }}>
              Lisbon, the slow way
            </div>
            <div style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12, color: T.mute, marginTop: 4, lineHeight: 1.35 }}>
              {group ? 'six days, as the group remembers them' : 'six days · Alfama, Ramiro, a fado room'}
            </div>
          </div>
        </div>
        <div style={{ marginTop: 12 }}>
          <ChatActions ctx={ctx} primaryColor={T.goldDeep} primary={group ? 'Add to album' : 'Keep it'}
            secondary={group ? ['Preview'] : ['refine', 'not this time']}/>
        </div>
      </div>
    </ChatCard>
  );
}

// 13 · RESEARCH PROGRESS / RESULT ────────────────────────────────
function ResearchCard({ ctx = 'solo' }) {
  const group = ctx === 'group';
  const steps = [
    { s: 'done', t: 'Pulled 47 ryokan near Yanaka' },
    { s: 'done', t: 'Filtered for quiet + morning light' },
    { s: 'now',  t: 'Writing one-line reads' },
  ];
  return (
    <ChatCard>
      <div style={{ padding: '13px 15px 13px' }}>
        <CardHead glyph={ChatGlyph.research(T.ink)} vesper={!group}
          kind={group ? 'VESPER IS RESEARCHING FOR THE GROUP' : 'I’M LOOKING INTO IT'} right="~2 MIN"/>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 6, marginBottom: 11 }}>
          {steps.map((r, i) => (
            <div key={i} style={{ display: 'grid', gridTemplateColumns: '16px 1fr', gap: 9, alignItems: 'center' }}>
              <div style={{ display: 'flex', justifyContent: 'center' }}>
                {r.s === 'done'
                  ? <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke={T.muteSoft} strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round"><path d="M4 12l5 5L20 6"/></svg>
                  : <span style={{ width: 9, height: 9, borderRadius: 999, background: T.gold, boxShadow: '0 0 0 3px rgba(176,133,58,0.18)' }}/>}
              </div>
              <span style={{ fontFamily: T.serif, fontSize: 13, color: r.s === 'now' ? T.ink : T.mute, fontStyle: r.s === 'now' ? 'italic' : 'normal', letterSpacing: -0.05 }}>{r.t}</span>
            </div>
          ))}
        </div>
        <div style={{ height: 3, background: T.hairline, borderRadius: 3, overflow: 'hidden', marginBottom: 11 }}>
          <div style={{ width: '66%', height: '100%', background: T.gold }}/>
        </div>
        <ChatActions ctx={ctx} primary={group ? 'Watch' : 'Watch it work'}
          secondary={group ? ['Notify all'] : ['notify me', 'finish without me']}/>
      </div>
    </ChatCard>
  );
}

// 14 · PRIVACY / PRIVATE-HANDOFF ─────────────────────────────────
// Moves a sensitive topic from group → 1:1. The whole card is the affordance.
function PrivacyHandoffCard({ ctx = 'group' }) {
  const group = ctx === 'group';
  return (
    <ChatCard tint="rgba(94,80,112,0.06)">
      <div style={{ padding: '14px 16px 14px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 7, marginBottom: 10 }}>
          {ChatGlyph.lock('#5E5070')}
          <span style={{ fontSize: 9, letterSpacing: 1.5, fontWeight: 700, color: '#5E5070' }}>
            {group ? 'BETWEEN YOU & VESPER' : 'THIS STAYS PRIVATE'}
          </span>
        </div>
        <p style={{ fontFamily: T.serif, fontSize: 15.5, color: T.ink, margin: 0, lineHeight: 1.4, letterSpacing: -0.1 }}>
          {group
            ? <>This one’s about <span style={{ fontStyle: 'italic' }}>your budget</span> — want to keep it just between us?</>
            : <>Only you can see this. Nothing here reaches the group.</>}
        </p>
        <div style={{ marginTop: 12 }}>
          <ChatActions ctx={ctx} primaryColor="#5E5070"
            primary={group ? 'Continue privately' : 'Got it'}
            secondary={group ? ['Keep in group'] : []}/>
        </div>
      </div>
    </ChatCard>
  );
}

// 15 · ERROR / RECOVERY ──────────────────────────────────────────
// Calm, never alarming. Names what happened + the way forward.
function ErrorCard({ ctx = 'solo' }) {
  const group = ctx === 'group';
  const ox = '#A04030';
  return (
    <ChatCard tint="rgba(160,64,48,0.06)">
      <div style={{ padding: '13px 15px 13px' }}>
        <CardHead glyph={ChatGlyph.alert(ox)} kind="COULDN’T FINISH" right="08:12"/>
        <p style={{ fontFamily: T.serif, fontSize: 15.5, color: T.ink, margin: 0, lineHeight: 1.4, letterSpacing: -0.1 }}>
          {group
            ? <>The Sawanoya hold <span style={{ fontStyle: 'italic' }}>expired</span> before everyone approved.</>
            : <>Sawanoya stopped responding while I held the room.</>}
        </p>
        <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12.5, color: T.mute, margin: '6px 0 0', lineHeight: 1.35 }}>
          {group ? 'No one was charged. I can re-hold for 24h, or find two more like it.' : 'Nothing was charged. I can try again, or show two alike.'}
        </p>
        <div style={{ marginTop: 12 }}>
          <ChatActions ctx={ctx} primaryColor={ox} primary={group ? 'Re-hold for all' : 'Try again'}
            secondary={group ? ['Find alike'] : ['find two alike', 'leave it']}/>
        </div>
      </div>
    </ChatCard>
  );
}

Object.assign(window, {
  RationaleBlock, VoiceSegmentCard, NarrationCard, AtlasDraftCard,
  ResearchCard, PrivacyHandoffCard, ErrorCard,
});
