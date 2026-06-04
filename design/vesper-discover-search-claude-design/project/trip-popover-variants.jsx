// ═══════════════════════════════════════════════════════════════
// POPOVER VARIATIONS — restyling the block-tap popover. Each keeps the
// committed structure (why-door header · ask · actions) but a distinct hand.
// Reuses TH + Phone/TabBar + StyleRiso + RefTopBar/DateRail + BlockStd.
// ═══════════════════════════════════════════════════════════════

const Spark = ({ s = 13, c = TH.gold }) => <svg width={s} height={s} viewBox="0 0 24 24" fill={c}><path d="M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z"/></svg>;

// Shared faint spine + the tapped block, so popovers read in place.
function PopStage({ children, tail = 26 }) {
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
            <div style={{ paddingTop: 6 }}><BlockStd time="MORNING" title="Belém, early" place="Belém" dur="·2h" thumb state="booked" last/></div>
          </div>
          <div style={{ position: 'absolute', left: 56, right: 16, top: 96 }}>
            <div style={{ position: 'absolute', top: -6, left: tail, width: 12, height: 12, background: children.tailBg || TH.card, transform: 'rotate(45deg)', border: children.tailBorder, borderBottom: 'none', borderRight: 'none', zIndex: 0 }}/>
            {children}
          </div>
        </div>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

// ─── A · LETTER — Vesper writes; header is prose, actions are quiet text ──
function PopLetter() {
  return (
    <PopStage>
      <div style={{ position: 'relative', background: TH.card, borderRadius: 16, border: `0.5px solid ${TH.hair}`, boxShadow: '0 18px 42px -16px rgba(0,0,0,0.3)', overflow: 'hidden' }}>
        <div style={{ padding: '14px 16px 13px' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 6, marginBottom: 9 }}>
            <Spark s={12}/><span style={{ fontSize: 9, letterSpacing: 1.6, fontWeight: 700, color: TH.goldDeep }}>WHY IT’S HERE</span>
          </div>
          <p style={{ fontFamily: TH.serif, fontSize: 15.5, color: TH.ink, lineHeight: 1.45, margin: 0, letterSpacing: -0.1 }}>
            Ana wanted the cloister, and you all travel slow — so I set it early, nothing booked after. <span style={{ color: TH.goldDeep, fontStyle: 'italic' }}>Read why →</span>
          </p>
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: 16, padding: '11px 16px', borderTop: `0.5px solid ${TH.hairThin}`, background: TH.cardSoft }}>
          <span style={{ fontFamily: TH.serif, fontSize: 14, fontWeight: 500, color: TH.ink }}>Change</span>
          <span style={{ fontFamily: TH.serif, fontSize: 14, color: TH.soft, fontStyle: 'italic' }}>move</span>
          <span style={{ fontFamily: TH.serif, fontSize: 14, color: TH.soft, fontStyle: 'italic' }}>book</span>
          <span style={{ marginLeft: 'auto', fontFamily: TH.serif, fontSize: 13, color: '#A04030', fontStyle: 'italic' }}>remove</span>
        </div>
      </div>
    </PopStage>
  );
}

// ─── B · ICON GRID — header door + a clean 4-icon action grid ──
function PopIconGrid() {
  const acts = [['change','Change',TH.gold,'M12 2.5 L13.4 9 L20 10.4 L13.4 11.8 L12 18.3 L10.6 11.8 L4 10.4 L10.6 9 Z',true],['move','Move',TH.blue,'M5 9l-3 3 3 3M12 2v20M2 12h20'],['book','Book',TH.blue,'M3 6h18v12H3z M3 10h18'],['remove','Remove','#A04030','M6 7h12M9 7V5h6M8 7l1 13h6l1-13']];
  return (
    <PopStage>
      <div style={{ position: 'relative', background: TH.card, borderRadius: 16, border: `0.5px solid ${TH.hair}`, boxShadow: '0 18px 42px -16px rgba(0,0,0,0.3)', overflow: 'hidden' }}>
        <div style={{ display: 'flex', gap: 11, padding: 13, borderBottom: `0.5px solid ${TH.hairThin}` }}>
          <div style={{ width: 46, height: 46, borderRadius: 9, overflow: 'hidden', flexShrink: 0 }}><StyleRiso w={46} h={46}/></div>
          <div style={{ flex: 1 }}>
            <div style={{ fontFamily: TH.serif, fontSize: 16, fontWeight: 500, color: TH.ink, letterSpacing: -0.2, lineHeight: 1 }}>Belém, early</div>
            <div style={{ display: 'inline-flex', alignItems: 'center', gap: 4, marginTop: 5, color: TH.goldDeep, fontSize: 10.5, fontWeight: 700 }}><Spark s={10}/> WHY IT’S HERE →</div>
          </div>
        </div>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4,1fr)' }}>
          {acts.map(([k,l,c,d,fill],i)=>(
            <div key={k} style={{ padding: '13px 4px 11px', textAlign: 'center', borderLeft: i?`0.5px solid ${TH.hairThin}`:'none' }}>
              <svg width="18" height="18" viewBox="0 0 24 24" fill={fill?c:'none'} stroke={fill?'none':c} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round" style={{ display: 'block', margin: '0 auto 6px' }}><path d={d}/></svg>
              <span style={{ fontSize: 10.5, fontWeight: 600, color: k==='remove'?'#A04030':TH.soft }}>{l}</span>
            </div>
          ))}
        </div>
      </div>
    </PopStage>
  );
}

// ─── C · DARK GLASS — one ink surface, clear gravity on the "why" ──
function PopGlass() {
  return (
    <PopStage>
      <div style={{ position: 'relative', background: 'rgba(27,23,20,0.97)', borderRadius: 18, boxShadow: '0 22px 48px -14px rgba(0,0,0,0.55)', overflow: 'hidden' }}>
        {/* identity line — small, demoted: thumb + name + place, one row */}
        <div style={{ display: 'flex', alignItems: 'center', gap: 10, padding: '14px 16px 0' }}>
          <div style={{ width: 34, height: 34, borderRadius: 8, overflow: 'hidden', flexShrink: 0 }}><StyleRiso w={34} h={34}/></div>
          <div style={{ flex: 1, minWidth: 0 }}>
            <div style={{ fontFamily: TH.serif, fontSize: 16, fontWeight: 500, color: '#fff', letterSpacing: -0.2, lineHeight: 1 }}>Belém, early</div>
          </div>
          <span style={{ fontFamily: TH.mono, fontSize: 8.5, color: 'rgba(255,255,255,0.4)', letterSpacing: 1 }}>TUE · 8:30</span>
        </div>

        {/* THE HERO — the why. Largest type, the gravity of the card. */}
        <div style={{ padding: '14px 16px 16px' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 6, marginBottom: 8 }}>
            <Spark s={11} c="#E5C16F"/><span style={{ fontSize: 8.5, letterSpacing: 1.8, fontWeight: 700, color: '#E5C16F' }}>WHY IT’S HERE</span>
          </div>
          <p style={{ fontFamily: TH.serif, fontSize: 17, color: 'rgba(255,255,255,0.95)', lineHeight: 1.4, margin: 0, letterSpacing: -0.1 }}>
            Ana wanted the cloister, and you travel slow — so it’s early, with nothing booked after.
          </p>
          <div style={{ display: 'inline-flex', alignItems: 'center', gap: 4, marginTop: 11, color: '#E5C16F', fontSize: 11.5, fontWeight: 600, letterSpacing: -0.05 }}>
            Read the full why <span>→</span>
          </div>
        </div>

        {/* actions — quietest layer, one divided row */}
        <div style={{ display: 'flex', gap: 0, borderTop: `0.5px solid rgba(255,255,255,0.12)` }}>
          {[['Change','#E5C16F'],['Move','rgba(255,255,255,0.82)'],['Book','rgba(255,255,255,0.82)'],['Remove','rgba(224,144,127,0.92)']].map(([l,c],i)=>(
            <div key={l} style={{ flex: 1, textAlign: 'center', padding: '13px 0', borderLeft: i?`0.5px solid rgba(255,255,255,0.1)`:'none', fontSize: 12, fontWeight: 600, color: c, letterSpacing: -0.1 }}>{l}</div>
          ))}
        </div>
      </div>
    </PopStage>
  );
}

// ─── D · TICKET — perforated stub; actions on a torn-off coupon ──
function PopTicket() {
  return (
    <PopStage>
      <div style={{ position: 'relative', background: TH.card, borderRadius: 14, border: `0.5px solid ${TH.hair}`, boxShadow: '0 18px 42px -16px rgba(0,0,0,0.3)', overflow: 'hidden' }}>
        <div style={{ height: 78, position: 'relative' }}>
          <StyleRiso w={300} h={78}/>
          <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to right, rgba(20,14,9,0.5), rgba(20,14,9,0.05))' }}/>
          <div style={{ position: 'absolute', left: 13, top: 12 }}>
            <div style={{ fontFamily: TH.mono, fontSize: 8, color: 'rgba(255,255,255,0.8)', letterSpacing: 1 }}>TUE 21 · MORNING</div>
            <div style={{ fontFamily: TH.serif, fontSize: 18, fontWeight: 500, color: '#fff', letterSpacing: -0.3, marginTop: 1 }}>Belém, early</div>
          </div>
        </div>
        {/* perforation */}
        <div style={{ position: 'relative', height: 1 }}>
          <div style={{ borderTop: `1px dashed ${TH.faint}`, margin: '0 12px' }}/>
          <div style={{ position: 'absolute', left: -6, top: -6, width: 12, height: 12, borderRadius: 999, background: TH.paper }}/>
          <div style={{ position: 'absolute', right: -6, top: -6, width: 12, height: 12, borderRadius: 999, background: TH.paper }}/>
        </div>
        <div style={{ padding: '11px 14px', display: 'flex', alignItems: 'center' }}>
          <div style={{ display: 'inline-flex', alignItems: 'center', gap: 5, color: TH.goldDeep, fontSize: 10.5, fontWeight: 700 }}><Spark s={11}/> WHY IT’S HERE →</div>
          <span style={{ marginLeft: 'auto', display: 'flex', gap: 12, fontFamily: TH.sans, fontSize: 12.5, fontWeight: 600 }}>
            <span style={{ color: TH.soft }}>Move</span><span style={{ color: TH.blue }}>Book</span>
          </span>
        </div>
      </div>
    </PopStage>
  );
}

Object.assign(window, { PopLetter, PopIconGrid, PopGlass, PopTicket });
