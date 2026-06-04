// ═══════════════════════════════════════════════════════════════
// RICHER BLOCKS — variations that cure the "empty" feel by giving
// each block one more layer of texture. Plus travel connectors.
// Reuses TH + Phone/TabBar + StyleRiso + RefTopBar/DateRail.
// ═══════════════════════════════════════════════════════════════

// Travel connector — the gap between blocks, made legible.
function Connector({ mode = 'walk', label }) {
  const ico = mode==='walk'
    ? <path d="M13 4a1.5 1.5 0 1 0 0-.01M11 8l-2 5 2 2 1 5M11 13l-3-1M12 8l3 2 3-1"/>
    : <><rect x="6" y="4" width="12" height="13" rx="2"/><path d="M6 10h12M9 21l-2-3M15 21l2-3"/><circle cx="9" cy="14" r="1"/><circle cx="15" cy="14" r="1"/></>;
  return (
    <div style={{ display: 'grid', gridTemplateColumns: '16px 1fr', gap: 15 }}>
      <div style={{ display: 'flex', justifyContent: 'center', position: 'relative' }}>
        <span style={{ position: 'absolute', top: -6, bottom: -6, width: 1, borderLeft: `1px dotted ${TH.faint}` }}/>
      </div>
      <div style={{ padding: '5px 0', display: 'flex', alignItems: 'center', gap: 6, color: TH.faint }}>
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke={TH.faint} strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round">{ico}</svg>
        <span style={{ fontFamily: TH.mono, fontSize: 8.5, letterSpacing: 1, fontWeight: 600 }}>{label}</span>
      </div>
    </div>
  );
}

// V1 · STANDARD+ — thumbnail + duration·place meta line. The workhorse.
function BlockStd({ time, title, place, dur, thumb, state, by, last }) {
  const dot = state==='now'?TH.gold:state==='booked'?TH.blue:TH.soft;
  return (
    <div style={{ display: 'grid', gridTemplateColumns: '16px 1fr', gap: 15 }}>
      <div style={{ display: 'flex', justifyContent: 'center', position: 'relative' }}>
        {!last && <span style={{ position: 'absolute', top: 16, bottom: -10, width: 1, background: TH.hairThin }}/>}
        <span style={{ width: state==='now'?10:7, height: state==='now'?10:7, borderRadius: 999, marginTop: 8, background: dot, boxShadow: state==='now'?'0 0 0 4px rgba(176,133,58,0.18)':'none', zIndex: 1 }}/>
      </div>
      <div style={{ paddingBottom: last?2:18, display: 'flex', gap: 12 }}>
        <div style={{ flex: 1, minWidth: 0 }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 7, marginBottom: 5 }}>
            <span style={{ fontFamily: TH.mono, fontSize: 8.5, color: state==='now'?TH.goldDeep:TH.mute, letterSpacing: 1.4, fontWeight: 600 }}>{time}</span>
            {state==='booked' && <span style={{ fontSize: 7.5, letterSpacing: 1.2, fontWeight: 700, color: TH.blue }}>BOOKED</span>}
            {state==='now' && <span style={{ fontSize: 7.5, letterSpacing: 1.2, fontWeight: 700, color: TH.goldDeep }}>NOW</span>}
          </div>
          <div style={{ fontFamily: TH.serif, fontSize: 16.5, fontWeight: 500, color: TH.ink, letterSpacing: -0.2, lineHeight: 1.2 }}>{title}</div>
          <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginTop: 5 }}>
            <span style={{ fontFamily: TH.sans, fontSize: 11, color: TH.mute, fontWeight: 500 }}>{place}</span>
            <span style={{ width: 3, height: 3, borderRadius: 3, background: TH.faint }}/>
            <span style={{ fontFamily: TH.sans, fontSize: 11, color: TH.mute }}>{dur}</span>
          </div>
        </div>
        {thumb && <div style={{ width: 54, height: 54, borderRadius: 9, overflow: 'hidden', flexShrink: 0 }}><StyleRiso w={54} h={54}/></div>}
      </div>
    </div>
  );
}

// V2 · RICH ANCHOR — bigger image, a Vesper note line, status. One per day.
function BlockRich({ time, title, place, note, status, last }) {
  return (
    <div style={{ display: 'grid', gridTemplateColumns: '16px 1fr', gap: 15 }}>
      <div style={{ display: 'flex', justifyContent: 'center', position: 'relative' }}>
        {!last && <span style={{ position: 'absolute', top: 16, bottom: -10, width: 1, background: TH.hairThin }}/>}
        <span style={{ width: 10, height: 10, borderRadius: 999, marginTop: 8, background: TH.gold, boxShadow: '0 0 0 4px rgba(176,133,58,0.18)', zIndex: 1 }}/>
      </div>
      <div style={{ paddingBottom: last?2:18 }}>
        <div style={{ background: TH.card, borderRadius: 14, border: `0.5px solid ${TH.hair}`, overflow: 'hidden', boxShadow: '0 1px 0 rgba(255,255,255,0.6) inset' }}>
          <div style={{ height: 104, position: 'relative' }}>
            <StyleRiso w={300} h={104}/>
            <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to bottom, rgba(20,14,9,0.05), rgba(20,14,9,0.42))' }}/>
            {status && <div style={{ position: 'absolute', top: 9, right: 9, padding: '3px 8px', borderRadius: 999, background: 'rgba(61,80,102,0.9)', fontSize: 8, letterSpacing: 1, fontWeight: 700, color: '#fff' }}>{status}</div>}
            <div style={{ position: 'absolute', left: 12, bottom: 10 }}>
              <span style={{ fontFamily: TH.mono, fontSize: 8.5, color: 'rgba(255,255,255,0.85)', letterSpacing: 1.2, fontWeight: 600 }}>{time} · {place}</span>
              <div style={{ fontFamily: TH.serif, fontSize: 19, fontWeight: 500, color: '#fff', letterSpacing: -0.3, lineHeight: 1.1, marginTop: 2 }}>{title}</div>
            </div>
          </div>
          {note && (
            <div style={{ padding: '10px 13px', display: 'flex', gap: 8, alignItems: 'flex-start' }}>
              <svg width="12" height="12" viewBox="0 0 24 24" fill={TH.gold} style={{ flexShrink: 0, marginTop: 2 }}><path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z"/></svg>
              <span style={{ fontFamily: TH.serif, fontStyle: 'italic', fontSize: 12.5, color: TH.soft, lineHeight: 1.35 }}>{note}</span>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

// V3 · LISTING — left meta column + text, no image. Densest, calm.
function BlockList({ time, title, place, dur, tag, state, last }) {
  const dot = state==='now'?TH.gold:state==='booked'?TH.blue:TH.soft;
  return (
    <div style={{ display: 'grid', gridTemplateColumns: '52px 16px 1fr', gap: 11 }}>
      <div style={{ textAlign: 'right', paddingTop: 7 }}>
        <div style={{ fontFamily: TH.mono, fontSize: 9.5, color: state==='now'?TH.goldDeep:TH.soft, letterSpacing: 0.5, fontWeight: 600 }}>{time}</div>
        {dur && <div style={{ fontFamily: TH.mono, fontSize: 8, color: TH.faint, marginTop: 2 }}>{dur}</div>}
      </div>
      <div style={{ display: 'flex', justifyContent: 'center', position: 'relative' }}>
        {!last && <span style={{ position: 'absolute', top: 14, bottom: -12, width: 1, background: TH.hairThin }}/>}
        <span style={{ width: state==='now'?9:6.5, height: state==='now'?9:6.5, borderRadius: 999, marginTop: 7, background: dot, boxShadow: state==='now'?'0 0 0 4px rgba(176,133,58,0.18)':'none', zIndex: 1 }}/>
      </div>
      <div style={{ paddingBottom: last?2:16 }}>
        <div style={{ fontFamily: TH.serif, fontSize: 16, fontWeight: 500, color: TH.ink, letterSpacing: -0.2, lineHeight: 1.2 }}>{title}</div>
        <div style={{ display: 'flex', alignItems: 'center', gap: 7, marginTop: 4 }}>
          <span style={{ fontSize: 11, color: TH.mute, fontWeight: 500 }}>{place}</span>
          {tag && <span style={{ fontSize: 8, letterSpacing: 1, fontWeight: 700, color: TH.blue, border: `0.5px solid ${TH.blue}`, opacity: 0.7, padding: '1px 5px', borderRadius: 4 }}>{tag}</span>}
        </div>
      </div>
    </div>
  );
}

// ─── Three full-screen comparison spines ───────────────────────
function richScreen(label, kids) {
  return (
    <Phone bg={TH.paper}>
      <div style={{ position: 'absolute', inset: 0, paddingTop: 54, overflow: 'hidden' }}>
        <RefTopBar/><DateRail/>
        <div style={{ padding: '18px 20px 0' }}>
          <div style={{ display: 'grid', gridTemplateColumns: '50px 1fr', gap: 14 }}>
            <div style={{ textAlign: 'center', paddingTop: 2 }}>
              <div style={{ fontSize: 8, letterSpacing: 1, color: TH.goldDeep, fontWeight: 700 }}>MON</div>
              <div style={{ fontFamily: TH.serif, fontSize: 30, fontWeight: 500, color: TH.gold, lineHeight: 0.9, marginTop: 3 }}>20</div>
              <div style={{ fontFamily: TH.mono, fontSize: 8, color: TH.faint, marginTop: 8 }}>18°</div>
            </div>
            <div style={{ paddingTop: 6 }}>{kids}</div>
          </div>
        </div>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

function RichV1() {
  return richScreen('std', <>
    <BlockStd time="9:30" title="Coffee at Kayaba" place="Yanaka" dur="·45m" thumb state="booked"/>
    <Connector mode="walk" label="8 MIN ON FOOT"/>
    <BlockStd time="NOW · 10:14" title="Cemetery walk, the slow way" place="Yanaka" dur="·1h" thumb state="now"/>
    <Connector mode="tram" label="TRAM 28 · 14 MIN"/>
    <BlockStd time="21:00" title="Fado, the quiet room" place="Alfama" dur="·2h" thumb state="booked" last/>
  </>);
}
function RichV2() {
  return richScreen('rich', <>
    <BlockStd time="9:30" title="Coffee at Kayaba" place="Yanaka" dur="·45m" thumb state="booked"/>
    <Connector mode="walk" label="8 MIN ON FOOT"/>
    <BlockRich time="NOW · 10:14" title="Cemetery walk" place="Yanaka" status="GOOD LIGHT NOW" note="Take the eastern path — it stays quiet till noon, and the camellias are out."/>
    <BlockStd time="21:00" title="Fado, the quiet room" place="Alfama" dur="·2h" thumb state="booked" last/>
  </>);
}
function RichV3() {
  return richScreen('list', <>
    <BlockList time="9:30" dur="45m" title="Coffee at Kayaba" place="Yanaka" state="booked"/>
    <BlockList time="10:14" dur="1h" title="Cemetery walk, the slow way" place="Yanaka" state="now"/>
    <BlockList time="13:00" dur="1h" title="Kamachiku, udon under the gingko" place="Yanaka" tag="NO BOOKING"/>
    <BlockList time="21:00" dur="2h" title="Fado, the quiet room" place="Alfama" state="booked" tag="BOOKED" last/>
  </>);
}

Object.assign(window, { Connector, BlockStd, BlockRich, BlockList, RichV1, RichV2, RichV3 });
