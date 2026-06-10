// ═══════════════════════════════════════════════════════════════
// VESPER · CHAT — cross-surface moments + voice entry.
// Cross-surface: promote a standalone thread → a real trip (quiet
// "now planning {Trip}"); in-thread handoffs (add-to-trip, save-to-
// Atlas postcard, Open-in-Trips ink-blue). Voice: composer mic →
// Calm Listening (one-shot); long-press → Editorial Transcript
// (session); + return-to-thread. Reuses scaffold + card kit.
// ═══════════════════════════════════════════════════════════════

// ─── PROMOTE · standalone thread becomes a real trip ────────────
function PromoteToTrip() {
  return (
    <ChatScreen
      header={<ChatHeader title="Vesper" sub="JUST VESPER"/>}
      composer={<ChatComposer placeholder="Reply…"/>}
    >
      <UserPill time="2:31">ok this is actually happening — may, 8 days, tokyo</UserPill>
      <VesperProse>
        Then let’s make it real. I’ll keep everything we’ve said and start a trip around it — you stay right here.
      </VesperProse>

      {/* the quiet promotion banner */}
      <div style={{ display: 'flex', alignItems: 'center', gap: 11, padding: '12px 14px', borderRadius: 13, background: 'rgba(61,80,102,0.07)', border: `0.5px solid rgba(61,80,102,0.25)` }}>
        <span style={{ width: 30, height: 30, borderRadius: 8, background: TR.ink, color: '#fff', display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0 }}>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><path d="M12 6c-1.6-1-4-1.5-6.5-1.5V18C8 18 10.4 18.5 12 19.5 13.6 18.5 16 18 18.5 18V4.5C16 4.5 13.6 5 12 6z"/><path d="M12 6v13.5"/></svg>
        </span>
        <div style={{ flex: 1 }}>
          <div style={{ fontSize: 8.5, letterSpacing: 1.5, fontWeight: 700, color: TR.ink }}>NOW PLANNING</div>
          <div style={{ fontFamily: T.serif, fontSize: 15.5, color: T.ink, fontWeight: 500, letterSpacing: -0.2, marginTop: 1 }}>Tokyo, in May</div>
        </div>
        <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 12, color: TR.ink }}>view trip →</span>
      </div>

      <VesperProse time="2:32">
        It’s in your trips now. The ryokan and the dates carried over — want to keep going on the middle days?
      </VesperProse>
    </ChatScreen>
  );
}

// ─── HANDOFFS · add-to-trip · save-to-Atlas · Open-in-Trips ─────
function Handoffs() {
  return (
    <ChatScreen
      header={<ChatHeader title="Tokyo, in May" sub="PRIVATE · TRIP-LINKED"/>}
      composer={<ChatComposer/>}
    >
      {/* add-to-trip confirmation (ink-blue) */}
      <GroupEvent icon="cal" tint={TR.ink}>Kayaba Coffee added to Day 3 · Tokyo</GroupEvent>

      {/* save-a-moment → Atlas postcard */}
      <VesperProse>
        That afternoon in Yanaka is worth keeping — I made you a postcard for it.
      </VesperProse>
      <div style={{ marginTop: 1 }}><AtlasDraftCard ctx="solo"/></div>

      {/* Open-in-Trips — the ink-blue planning hand-off */}
      <VesperProse time="4:10">
        The full plan’s gotten rich enough to see properly. Open it in Trips when you want the map and the days together.
      </VesperProse>
      <div>
        <span style={{ display: 'inline-flex', alignItems: 'center', gap: 7, padding: '9px 15px', background: TR.ink, color: '#fff', borderRadius: 999, fontSize: 12.5, fontWeight: 600, letterSpacing: -0.05 }}>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><path d="M12 6c-1.6-1-4-1.5-6.5-1.5V18C8 18 10.4 18.5 12 19.5 13.6 18.5 16 18 18.5 18V4.5C16 4.5 13.6 5 12 6z"/><path d="M12 6v13.5"/></svg>
          Open in Trips
          <span style={{ opacity: 0.8 }}>→</span>
        </span>
      </div>
    </ChatScreen>
  );
}

// ─── VOICE · Calm Listening (one-shot from composer mic) ────────
function VoiceCalm() {
  return (
    <Phone bg="#16120E">
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, display: 'flex', flexDirection: 'column' }}>
        {/* minimal header */}
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '14px 22px' }}>
          <span style={{ fontSize: 13, color: 'rgba(255,255,255,0.6)' }}>✕</span>
          <span style={{ fontSize: 8.5, letterSpacing: 2, fontWeight: 700, color: 'rgba(247,242,231,0.5)' }}>LISTENING</span>
          <span style={{ width: 14 }}/>
        </div>
        <div style={{ flex: 1, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', padding: '0 40px' }}>
          {/* breathing ring — gold, not an orb logo */}
          <div style={{ width: 96, height: 96, borderRadius: 999, border: `1.5px solid rgba(176,133,58,0.5)`, display: 'flex', alignItems: 'center', justifyContent: 'center', marginBottom: 30 }}>
            <div style={{ width: 64, height: 64, borderRadius: 999, background: 'rgba(176,133,58,0.16)', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
              <VesperMark s={30} c={T.goldSoft}/>
            </div>
          </div>
          <p style={{ fontFamily: T.serif, fontSize: 22, color: '#F7F2E7', textAlign: 'center', lineHeight: 1.35, margin: 0, letterSpacing: -0.2 }}>
            “find me a quiet ryokan for the last few nights…”
          </p>
          <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13.5, color: 'rgba(247,242,231,0.5)', marginTop: 16 }}>
            tap when you’re done — I’ll reply in the thread
          </p>
        </div>
        {/* waveform */}
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 3, height: 64 }}>
          {[10, 22, 14, 30, 20, 38, 16, 26, 12, 32, 18, 24, 10].map((h, i) => (
            <span key={i} style={{ width: 3, height: h, borderRadius: 3, background: 'rgba(217,189,134,0.7)' }}/>
          ))}
        </div>
        <div style={{ height: 40 }}/>
      </div>
    </Phone>
  );
}

// ─── VOICE · Editorial Transcript (session) + return to thread ──
function VoiceTranscript() {
  return (
    <Phone bg={T.bg}>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54 }}>
        <ChatHeader title="Walking with Vesper" sub="VOICE SESSION · 4:12" right="menu"/>
        <div style={{ padding: '18px 22px', display: 'flex', flexDirection: 'column', gap: 16, position: 'absolute', top: 96, bottom: 120, left: 0, right: 0, overflow: 'hidden' }}>
          <div style={{ textAlign: 'right' }}>
            <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 14, color: T.mute }}>“where am I, and what’s worth the detour?”</span>
          </div>
          <VesperProse>
            You’re at the top of Yanaka’s old stair — the one with the cats. If you turn left, there’s a sentō that’s been running ninety years; straight on, the cemetery cherry path. I’d turn left.
          </VesperProse>
          <div style={{ textAlign: 'right' }}>
            <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 14, color: T.mute }}>“tell me about the sentō as I walk”</span>
          </div>
          <VesperProse caret>
            It’s called Daikoku-yu. The owner’s grandmother ran it through the war, and the mural of Fuji gets repainted every
          </VesperProse>
          <div style={{ position: 'absolute', bottom: 0, left: 0, right: 0, height: 28, background: `linear-gradient(to top, ${T.bg}, rgba(239,234,224,0))`, pointerEvents: 'none' }}/>
        </div>
        {/* live voice bar + return-to-thread */}
        <div style={{ position: 'absolute', bottom: 40, left: 16, right: 16, display: 'flex', alignItems: 'center', gap: 10, padding: '10px 12px 10px 16px', background: '#16120E', borderRadius: 999 }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 2, flex: 1 }}>
            {[10, 18, 12, 22, 14, 20, 12, 16, 10, 14].map((h, i) => <span key={i} style={{ width: 2.5, height: h, borderRadius: 3, background: 'rgba(217,189,134,0.75)' }}/>)}
            <span style={{ marginLeft: 10, fontFamily: T.serif, fontStyle: 'italic', fontSize: 12.5, color: 'rgba(247,242,231,0.7)' }}>listening…</span>
          </div>
          <span style={{ fontSize: 9, letterSpacing: 1.2, fontWeight: 700, color: 'rgba(247,242,231,0.6)' }}>END · TO THREAD</span>
        </div>
      </div>
    </Phone>
  );
}

Object.assign(window, { PromoteToTrip, Handoffs, VoiceCalm, VoiceTranscript });
