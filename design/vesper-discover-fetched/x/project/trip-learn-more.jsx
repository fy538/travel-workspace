// ═══════════════════════════════════════════════════════════════
// LEARN MORE · CONNECTED — the committed flow:
//   block (V1) → popover w/ tappable why-teaser header → personalized
//   place page ("why this, for you, on this trip") → links to general dossier.
// Reuses TH + Phone/TabBar + StyleRiso + RefTopBar/DateRail + BlockStd/Connector.
// ═══════════════════════════════════════════════════════════════

// ─── The connecting popover — header is the door to the page ────
function PopConnected() {
  return (
    <Phone bg={TH.paper}>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
        <RefTopBar/><DateRail/>
        <div style={{ position: 'relative', padding: '18px 20px 0' }}>
          <div style={{ display: 'grid', gridTemplateColumns: '50px 1fr', gap: 14 }}>
            <div style={{ textAlign: 'center', paddingTop: 2 }}>
              <div style={{ fontSize: 8, letterSpacing: 1, color: TH.mute, fontWeight: 700 }}>TUE</div>
              <div style={{ fontFamily: TH.serif, fontSize: 30, fontWeight: 500, color: TH.ink, lineHeight: 0.9, marginTop: 3 }}>21</div>
            </div>
            <div style={{ paddingTop: 6 }}>
              <BlockStd time="MORNING" title="Belém, early" place="Belém" dur="·2h" thumb state="booked" last/>
            </div>
          </div>
          {/* popover tethered to the block */}
          <div style={{ position: 'absolute', left: 56, right: 16, top: 96 }}>
            <div style={{ position: 'absolute', top: -6, left: 26, width: 12, height: 12, background: TH.card, transform: 'rotate(45deg)', border: `0.5px solid ${TH.hair}`, borderBottom: 'none', borderRight: 'none' }}/>
            <div style={{ position: 'relative', background: TH.card, borderRadius: 16, border: `0.5px solid ${TH.hair}`, boxShadow: '0 18px 42px -16px rgba(0,0,0,0.3)', overflow: 'hidden' }}>
              {/* TAPPABLE HEADER = the door (B + C) */}
              <div style={{ display: 'flex', gap: 11, padding: 12, background: 'rgba(176,133,58,0.05)', borderBottom: `0.5px solid ${TH.hairThin}` }}>
                <div style={{ width: 50, height: 50, borderRadius: 9, overflow: 'hidden', flexShrink: 0 }}><StyleRiso w={50} h={50}/></div>
                <div style={{ flex: 1, minWidth: 0 }}>
                  <div style={{ fontFamily: TH.serif, fontSize: 16, fontWeight: 500, color: TH.ink, letterSpacing: -0.2, lineHeight: 1 }}>Belém, early</div>
                  <div style={{ fontFamily: TH.serif, fontStyle: 'italic', fontSize: 11.5, color: TH.mute, marginTop: 4, lineHeight: 1.3 }}>Ana wanted the cloister — here’s why it works for you</div>
                  <div style={{ display: 'inline-flex', alignItems: 'center', gap: 4, marginTop: 6, color: TH.goldDeep, fontSize: 10.5, fontWeight: 700, letterSpacing: 0.2 }}>
                    <svg width="11" height="11" viewBox="0 0 24 24" fill={TH.gold}><path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z"/></svg>
                    WHY IT’S HERE
                    <span style={{ color: TH.goldDeep }}>→</span>
                  </div>
                </div>
              </div>
              {/* ask field */}
              <div style={{ margin: '11px 12px 0', display: 'flex', alignItems: 'center', gap: 8, padding: '9px 12px', background: TH.paper, borderRadius: 999, border: `0.5px solid ${TH.hair}` }}>
                <svg width="13" height="13" viewBox="0 0 24 24" fill={TH.gold}><path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z"/></svg>
                <span style={{ flex: 1, fontFamily: TH.serif, fontStyle: 'italic', fontSize: 13, color: TH.faint }}>“make this later, somewhere quieter…”</span>
              </div>
              <div style={{ display: 'flex', gap: 0, marginTop: 11, borderTop: `0.5px solid ${TH.hairThin}` }}>
                {[['Move','#2C2622'],['Book','#2C2622'],['Remove','#A04030']].map(([l,c],i)=>(
                  <div key={l} style={{ flex: 1, textAlign: 'center', padding: '11px 0', borderLeft: i?`0.5px solid ${TH.hairThin}`:'none', fontFamily: TH.sans, fontSize: 12.5, fontWeight: 600, color: c }}>{l}</div>
                ))}
              </div>
            </div>
          </div>
        </div>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

// ─── The personalized place page — "why this, for you, this trip" ──
function PlaceForYou() {
  return (
    <Phone bg={TH.ink}>
      <div style={{ position: 'absolute', inset: 0, overflow: 'hidden', background: TH.paper }}>
        {/* hero */}
        <div style={{ position: 'relative', height: 264 }}>
          <div style={{ position: 'absolute', inset: 0 }}><StyleRiso w={393} h={264}/></div>
          <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to bottom, rgba(20,14,9,0.3), rgba(20,14,9,0) 36%, rgba(20,14,9,0.76))' }}/>
          <div style={{ position: 'absolute', top: 54, left: 18, width: 38, height: 38, borderRadius: 999, background: 'rgba(255,255,255,0.2)', backdropFilter: 'blur(8px)', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
            <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="#fff" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d="M15 5l-7 7 7 7"/></svg>
          </div>
          <div style={{ position: 'absolute', left: 22, right: 22, bottom: 18 }}>
            <div style={{ fontFamily: TH.mono, fontSize: 9, color: 'rgba(255,255,255,0.82)', letterSpacing: 1.2 }}>ON YOUR ITINERARY · TUE 21 · MORNING</div>
            <h1 style={{ fontFamily: TH.serif, fontSize: 31, fontWeight: 500, letterSpacing: -0.6, lineHeight: 1.02, color: '#fff', margin: '5px 0 0' }}>Belém</h1>
          </div>
        </div>

        <div style={{ overflow: 'hidden' }}>
          {/* WHY THIS, FOR YOU — personalized */}
          <div style={{ padding: '18px 22px 0' }}>
            <div style={{ paddingLeft: 13, borderLeft: `2px solid ${TH.gold}` }}>
              <div style={{ fontSize: 9, letterSpacing: 1.6, fontWeight: 700, color: TH.goldDeep, marginBottom: 6 }}>WHY THIS, FOR YOU THREE</div>
              <p style={{ fontFamily: TH.serif, fontStyle: 'italic', fontSize: 16, color: TH.ink, lineHeight: 1.45, margin: 0, letterSpacing: -0.1 }}>
                Ana wanted one grand morning, and you all travel slow — so Vesper set Belém early, before the buses, with nothing booked after. It’s the calm anchor of the trip.
              </p>
              <div style={{ marginTop: 10, display: 'inline-flex', alignItems: 'center', gap: 6 }}>
                <span style={{ width: 16, height: 16, borderRadius: 999, background: '#7C8F73', color: '#fff', fontFamily: TH.serif, fontSize: 8.5, fontWeight: 500, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>A</span>
                <span style={{ fontSize: 10.5, color: TH.mute, fontStyle: 'italic', fontFamily: TH.serif }}>added by Ana · kept by Vesper</span>
              </div>
            </div>
          </div>

          {/* HOW IT FITS — mini spine around it */}
          <div style={{ padding: '18px 22px 0' }}>
            <div style={{ fontSize: 9, letterSpacing: 1.6, color: TH.mute, fontWeight: 700, marginBottom: 11 }}>HOW IT FITS YOUR DAY</div>
            <div style={{ display: 'flex', flexDirection: 'column', gap: 0 }}>
              {[['8:30','Belém','here',true],['11:00','open · lunch nearby?','',false],['AFT.','back to Alfama, slow','',false]].map(([t,l,h,on],i)=>(
                <div key={i} style={{ display: 'grid', gridTemplateColumns: '46px 14px 1fr', gap: 10, alignItems: 'center', padding: '7px 0' }}>
                  <span style={{ fontFamily: TH.mono, fontSize: 9, color: on?TH.goldDeep:TH.faint, letterSpacing: 0.5, fontWeight: 600, textAlign: 'right' }}>{t}</span>
                  <div style={{ display: 'flex', justifyContent: 'center', position: 'relative' }}>
                    {i<2 && <span style={{ position: 'absolute', top: 10, bottom: -14, width: 1, background: TH.hairThin }}/>}
                    <span style={{ width: on?9:6, height: on?9:6, borderRadius: 999, background: on?TH.gold:TH.faint, boxShadow: on?'0 0 0 3px rgba(176,133,58,0.18)':'none', zIndex: 1 }}/>
                  </div>
                  <span style={{ fontFamily: TH.serif, fontSize: 14, fontStyle: on?'normal':'italic', fontWeight: on?500:400, color: on?TH.ink:TH.mute, letterSpacing: -0.1 }}>{l}</span>
                </div>
              ))}
            </div>
          </div>

          {/* FACTS — scoped to your trip */}
          <div style={{ padding: '16px 22px 0' }}>
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 0, border: `0.5px solid ${TH.hair}`, borderRadius: 12, overflow: 'hidden' }}>
              {[['FROM YOUR STAY','Tram 15 · 20 min'],['BEST FOR YOU','8:30, at opening'],['HOW LONG','~2 hours'],['COST','€ · tarts €1.40']].map(([k,v],i)=>(
                <div key={k} style={{ padding: '11px 13px', borderTop: i>1?`0.5px solid ${TH.hairThin}`:'none', borderLeft: i%2?`0.5px solid ${TH.hairThin}`:'none' }}>
                  <div style={{ fontSize: 8.5, letterSpacing: 1.3, color: TH.faint, fontWeight: 700 }}>{k}</div>
                  <div style={{ fontFamily: TH.serif, fontSize: 14, color: TH.ink, fontWeight: 500, marginTop: 3, letterSpacing: -0.1 }}>{v}</div>
                </div>
              ))}
            </div>
          </div>

          {/* NEARBY IF YOU HAVE TIME (from P2) */}
          <div style={{ padding: '18px 22px 0' }}>
            <div style={{ fontSize: 9, letterSpacing: 1.6, color: TH.mute, fontWeight: 700, marginBottom: 10 }}>NEARBY, IF YOU HAVE TIME</div>
            <div style={{ display: 'flex', gap: 10 }}>
              {[['coast','MAAT museum','6 MIN'],['square','Belém tower','9 MIN']].map(([v,t,m])=>(
                <div key={t} style={{ flex: 1 }}>
                  <div style={{ height: 62, borderRadius: 9, overflow: 'hidden' }}><StyleRiso w={150} h={62}/></div>
                  <div style={{ fontFamily: TH.serif, fontSize: 13, fontWeight: 500, color: TH.ink, marginTop: 6, letterSpacing: -0.1 }}>{t}</div>
                  <div style={{ fontFamily: TH.mono, fontSize: 8, color: TH.faint, letterSpacing: 0.5, marginTop: 2 }}>{m} WALK</div>
                </div>
              ))}
            </div>
          </div>

          {/* DOOR TO GENERAL DOSSIER — the two-layer link */}
          <div style={{ padding: '18px 22px 22px' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: 11, padding: '12px 14px', background: TH.cardSoft, borderRadius: 12, border: `0.5px solid ${TH.hair}` }}>
              <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke={TH.soft} strokeWidth="1.5"><circle cx="11" cy="11" r="7"/><path d="M16 16l5 5" strokeLinecap="round"/></svg>
              <div style={{ flex: 1 }}>
                <div style={{ fontFamily: TH.serif, fontSize: 14, fontWeight: 500, color: TH.ink, letterSpacing: -0.1 }}>The full story of Belém</div>
                <div style={{ fontSize: 10.5, color: TH.mute, marginTop: 1 }}>read the dossier in Discover</div>
              </div>
              <span style={{ color: TH.mute, fontSize: 13 }}>→</span>
            </div>
          </div>
        </div>

        {/* sticky bar */}
        <div style={{ position: 'absolute', bottom: 0, left: 0, right: 0, padding: '12px 18px 20px', background: 'rgba(247,242,231,0.94)', backdropFilter: 'blur(20px)', borderTop: `0.5px solid ${TH.hair}`, display: 'flex', alignItems: 'center', gap: 12 }}>
          <span style={{ display: 'inline-flex', alignItems: 'center', gap: 6, color: TH.ink, fontSize: 13, fontWeight: 600 }}>
            <svg width="15" height="15" viewBox="0 0 24 24" fill={TH.gold}><path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z"/></svg> Ask Vesper
          </span>
          <span style={{ marginLeft: 'auto', display: 'flex', gap: 9 }}>
            <span style={{ padding: '9px 14px', background: TH.card, border: `0.5px solid ${TH.hair}`, borderRadius: 999, fontSize: 12.5, fontWeight: 600, color: TH.soft }}>Move</span>
            <span style={{ padding: '9px 16px', background: TH.blue, color: '#fff', borderRadius: 999, fontSize: 12.5, fontWeight: 600 }}>Book</span>
          </span>
        </div>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

// ─── Flow strip — block → popover → page → dossier ──────────────
function LearnFlow() {
  const step = (n, t, d) => (
    <div style={{ display: 'flex', gap: 12, alignItems: 'flex-start', padding: '12px 0', borderTop: n>1?`0.5px solid ${TH.hairThin}`:'none' }}>
      <div style={{ width: 22, height: 22, borderRadius: 999, background: TH.ink, color: '#fff', fontFamily: TH.serif, fontSize: 12, fontWeight: 500, display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0 }}>{n}</div>
      <div><div style={{ fontFamily: TH.serif, fontSize: 15.5, fontWeight: 500, color: TH.ink, letterSpacing: -0.2 }}>{t}</div><div style={{ fontSize: 12, color: TH.mute, marginTop: 3, lineHeight: 1.45 }}>{d}</div></div>
    </div>
  );
  return (
    <div style={{ width: 420, padding: '34px 28px', background: '#F1ECE2', borderRadius: 8, color: TH.soft }}>
      <div style={{ fontSize: 10.5, letterSpacing: 2, color: TH.gold, fontWeight: 600 }}>NAVIGATION</div>
      <h2 style={{ fontFamily: TH.serif, fontWeight: 500, fontSize: 27, letterSpacing: -0.7, lineHeight: 1.05, color: TH.ink, margin: '8px 0 16px' }}>Glance → why → understand.</h2>
      <div style={{ borderTop: `0.5px solid ${TH.hair}`, paddingTop: 4 }}>
        {step(1,'Tap a block','The paper popover opens — quick actions (ask · move · book · remove) for when you just want to act.')}
        {step(2,'Tap the popover header','The header shows a riso thumb + a personalized teaser (“Ana wanted the cloister — why it works for you”) and a WHY IT’S HERE → door. Tapping it opens the page.')}
        {step(3,'The personalized place page','Why this, for you three · how it fits your day · facts from your stay · nearby if you have time. Not a venue page — a rationale-and-fit page.')}
        {step(4,'Door to the general dossier','For the place’s full story, a quiet link hands off to its Discover dossier — the audience-neutral version. Two layers, composed.')}
      </div>
      <div style={{ marginTop: 14, padding: 12, background: '#FBF7EC', borderRadius: 8, fontSize: 11.5, color: TH.mute, lineHeight: 1.5 }}>
        <b style={{ color: TH.ink }}>The split:</b> the itinerary page = <i>your</i> Belém, on <i>this</i> trip, for <i>this</i> group. The Discover dossier = Belém for everyone. The trip page links out; it never duplicates.
      </div>
    </div>
  );
}

Object.assign(window, { PopConnected, PlaceForYou, LearnFlow });
