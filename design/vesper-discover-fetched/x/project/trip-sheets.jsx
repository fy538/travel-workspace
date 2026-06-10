// ═══════════════════════════════════════════════════════════════
// INPUT SHEETS — light bottom sheets that rise over the folio so you
// never leave the trip you're shaping. One chrome, four contents.
// COSTS — the split ledger as a Vesper object, not a spreadsheet.
// Reuses TH + Phone + StyleRiso + People/CAST.
// ═══════════════════════════════════════════════════════════════

// A sheet shell rising over a dimmed folio.
function Sheet({ title, kicker, children, primary = 'Done', h = 420 }) {
  return (
    <Phone bg={TH.paper}>
      <div style={{ position: 'absolute', inset: 0, overflow: 'hidden' }}>
        {/* dimmed folio behind */}
        <div style={{ position: 'absolute', inset: 0 }}><StyleRiso w={393} h={852}/></div>
        <div style={{ position: 'absolute', inset: 0, background: 'rgba(20,14,9,0.5)' }}/>
        {/* sheet */}
        <div style={{ position: 'absolute', left: 0, right: 0, bottom: 0, height: h, background: TH.paper, borderRadius: '26px 26px 0 0', boxShadow: '0 -16px 40px -12px rgba(0,0,0,0.3)', overflow: 'hidden' }}>
          <div style={{ display: 'flex', justifyContent: 'center', paddingTop: 10 }}><div style={{ width: 36, height: 4, borderRadius: 4, background: TH.faint }}/></div>
          <div style={{ padding: '14px 22px 0' }}>
            {kicker && <div style={{ fontSize: 9.5, letterSpacing: 1.8, color: TH.goldDeep, fontWeight: 700, marginBottom: 6 }}>{kicker}</div>}
            <h2 style={{ fontFamily: TH.serif, fontSize: 25, fontWeight: 500, letterSpacing: -0.5, lineHeight: 1.1, color: TH.ink, margin: 0 }}>{title}</h2>
          </div>
          <div style={{ padding: '16px 22px 0' }}>{children}</div>
          <div style={{ position: 'absolute', left: 22, right: 22, bottom: 24 }}>
            <div style={{ padding: '13px 0', textAlign: 'center', background: TH.ink, color: '#fff', borderRadius: 999, fontSize: 14, fontWeight: 600, letterSpacing: -0.1 }}>{primary}</div>
          </div>
        </div>
      </div>
    </Phone>
  );
}

// 1 · DESTINATION — search + Vesper suggestions from taste.
function SheetDestination() {
  return (
    <Sheet kicker="WHERE TO" title="Where are you going?" primary="Set destination" h={500}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 10, padding: '12px 14px', background: TH.card, borderRadius: 12, border: `0.5px solid ${TH.hair}` }}>
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke={TH.mute} strokeWidth="1.7" strokeLinecap="round"><circle cx="11" cy="11" r="6.5"/><path d="M16 16l4 4"/></svg>
        <span style={{ fontFamily: TH.serif, fontStyle: 'italic', fontSize: 15, color: TH.mute }}>a city, a region, a coast…</span>
      </div>
      <div style={{ marginTop: 16, fontSize: 9.5, letterSpacing: 1.6, color: TH.mute, fontWeight: 700 }}>VESPER THINKS YOU’D LOVE</div>
      <div style={{ marginTop: 10, display: 'flex', flexDirection: 'column', gap: 8 }}>
        {[['Lisbon','slow, layered, coastal'],['Tbilisi','wine country, uncrowded'],['Naples','honest, intense, alive']].map(([n,d])=>(
          <div key={n} style={{ display: 'flex', alignItems: 'center', gap: 12, padding: '10px 12px', background: TH.card, borderRadius: 12, border: `0.5px solid ${TH.hair}` }}>
            <div style={{ width: 40, height: 40, borderRadius: 8, overflow: 'hidden', flexShrink: 0 }}><StyleRiso w={40} h={40}/></div>
            <div style={{ flex: 1 }}>
              <div style={{ fontFamily: TH.serif, fontSize: 16, fontWeight: 500, color: TH.ink, letterSpacing: -0.2 }}>{n}</div>
              <div style={{ fontFamily: TH.serif, fontStyle: 'italic', fontSize: 11.5, color: TH.mute, marginTop: 1 }}>{d}</div>
            </div>
            <span style={{ color: TH.gold, fontSize: 13 }}>+</span>
          </div>
        ))}
      </div>
    </Sheet>
  );
}

// 2 · DATES — a calendar moment, not a form.
function SheetDates() {
  const days = Array.from({ length: 35 }, (_, i) => i - 2);
  const inRange = (d) => d >= 18 && d <= 24;
  return (
    <Sheet kicker="WHEN" title="When are you going?" primary="Set May 18 – 24" h={460}>
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 12 }}>
        <span style={{ fontFamily: TH.serif, fontSize: 17, fontWeight: 500, color: TH.ink }}>May 2026</span>
        <span style={{ fontFamily: TH.mono, fontSize: 11, color: TH.mute, letterSpacing: 1 }}>6 NIGHTS</span>
      </div>
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(7,1fr)', gap: 4 }}>
        {['S','M','T','W','T','F','S'].map((d,i) => <div key={i} style={{ textAlign: 'center', fontSize: 9, color: TH.faint, fontWeight: 700, paddingBottom: 4 }}>{d}</div>)}
        {days.map((d, i) => {
          const valid = d >= 1 && d <= 31, on = inRange(d), edge = d === 18 || d === 24;
          return (
            <div key={i} style={{ aspectRatio: '1', display: 'flex', alignItems: 'center', justifyContent: 'center', fontFamily: TH.serif, fontSize: 14, color: !valid ? 'transparent' : on ? (edge ? '#fff' : TH.ink) : TH.soft, background: edge ? TH.gold : on ? 'rgba(176,133,58,0.16)' : 'transparent', borderRadius: edge ? 999 : on ? 0 : 999, fontWeight: edge ? 600 : 400 }}>{valid ? d : ''}</div>
          );
        })}
      </div>
    </Sheet>
  );
}

// 3 · PEOPLE — invite, not manage.
function SheetPeople() {
  return (
    <Sheet kicker="WHO’S COMING" title="Who’s on this trip?" primary="Send 2 invites" h={430}>
      <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
        {[['Ana','from Porto, May ’25','#7C8F73',true],['Theo','your usual co-pilot','#A0703A',true],['Mara','—','#3D5066',false]].map(([n,d,c,inv])=>(
          <div key={n} style={{ display: 'flex', alignItems: 'center', gap: 12, padding: '10px 12px', background: TH.card, borderRadius: 12, border: `0.5px solid ${TH.hair}` }}>
            <div style={{ width: 34, height: 34, borderRadius: 999, background: c, color: '#fff', fontFamily: TH.serif, fontSize: 15, fontWeight: 500, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>{n[0]}</div>
            <div style={{ flex: 1 }}>
              <div style={{ fontFamily: TH.serif, fontSize: 15.5, fontWeight: 500, color: TH.ink }}>{n}</div>
              <div style={{ fontFamily: TH.serif, fontStyle: 'italic', fontSize: 11.5, color: TH.mute }}>{d}</div>
            </div>
            <span style={{ padding: '5px 12px', borderRadius: 999, fontSize: 11, fontWeight: 600, background: inv ? TH.ink : 'transparent', color: inv ? '#fff' : TH.mute, border: inv ? 'none' : `0.5px solid ${TH.hair}` }}>{inv ? 'Invited' : 'Invite'}</span>
          </div>
        ))}
      </div>
    </Sheet>
  );
}

// 4 · BUDGET — a feeling + a split, not a number grid.
function SheetBudget() {
  return (
    <Sheet kicker="THE SHAPE OF IT" title="What kind of trip?" primary="Set the tone" h={420}>
      <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
        {[['Easy','watch the spend',false],['Comfortable','a few good splurges',true],['No ceiling','the trip decides',false]].map(([n,d,on])=>(
          <div key={n} style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '13px 15px', background: on ? 'rgba(176,133,58,0.10)' : TH.card, borderRadius: 12, border: `0.8px solid ${on ? 'rgba(176,133,58,0.4)' : TH.hair}` }}>
            <div>
              <div style={{ fontFamily: TH.serif, fontSize: 16.5, fontWeight: 500, color: TH.ink, letterSpacing: -0.2 }}>{n}</div>
              <div style={{ fontFamily: TH.serif, fontStyle: 'italic', fontSize: 12, color: TH.mute, marginTop: 1 }}>{d}</div>
            </div>
            {on && <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke={TH.goldDeep} strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M5 12l4 4L19 7"/></svg>}
          </div>
        ))}
      </div>
      <div style={{ marginTop: 14, display: 'flex', alignItems: 'center', gap: 8, justifyContent: 'center' }}>
        <People who={CAST} size={20}/>
        <span style={{ fontFamily: TH.serif, fontStyle: 'italic', fontSize: 12.5, color: TH.mute }}>split evenly three ways</span>
      </div>
    </Sheet>
  );
}

// COSTS — the split ledger as a calm object.
function CostsLedger() {
  return (
    <Phone bg={TH.paper}>
      <div style={{ position: 'absolute', inset: 0, overflow: 'hidden' }}>
        <ObjectHeader kicker="COSTS · SHARED" title="Lisbon, slowly"/>
        <div style={{ padding: '18px 22px 0' }}>
          {/* the one number that matters */}
          <div style={{ textAlign: 'center', padding: '6px 0 4px' }}>
            <div style={{ fontSize: 9.5, letterSpacing: 1.8, color: TH.mute, fontWeight: 700 }}>YOU’RE OWED, ON BALANCE</div>
            <div style={{ fontFamily: TH.serif, fontSize: 44, fontWeight: 500, color: TH.ink, letterSpacing: -1, lineHeight: 1, marginTop: 4 }}>€48<span style={{ fontSize: 22, color: TH.mute }}>.50</span></div>
            <div style={{ fontFamily: TH.serif, fontStyle: 'italic', fontSize: 13, color: TH.mute, marginTop: 4 }}>Vesper will settle it when you’re home</div>
          </div>
          {/* who owes whom — quiet rows */}
          <div style={{ marginTop: 16 }}>
            <Label right="3 OF YOU">THE SPLIT</Label>
            <div style={{ marginTop: 10, display: 'flex', flexDirection: 'column', gap: 7 }}>
              {[['Ana','owes you','€32',true],['Theo','owes you','€16.50',true],['You','paid','€194 of €388','']].map(([n,r,v,owe],i)=>(
                <div key={i} style={{ display: 'flex', alignItems: 'center', gap: 11, padding: '11px 13px', background: TH.card, borderRadius: 12, border: `0.5px solid ${TH.hair}` }}>
                  <div style={{ width: 28, height: 28, borderRadius: 999, background: CAST[i].c, color: '#fff', fontFamily: TH.serif, fontSize: 13, fontWeight: 500, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>{CAST[i].i}</div>
                  <div style={{ flex: 1 }}><span style={{ fontFamily: TH.serif, fontSize: 15, fontWeight: 500, color: TH.ink }}>{n}</span> <span style={{ fontSize: 12, color: TH.mute }}>{r}</span></div>
                  <span style={{ fontFamily: TH.mono, fontSize: 12.5, fontWeight: 600, color: owe ? '#3D7050' : TH.soft }}>{v}</span>
                </div>
              ))}
            </div>
          </div>
          {/* recent — editorial line items */}
          <div style={{ marginTop: 16 }}>
            <Label right="LATEST">WHAT YOU’VE SPENT</Label>
            <div style={{ marginTop: 8 }}>
              {[['Ramiro · dinner','€96','you'],['Ryokan hold','€72','Ana'],['Tram passes','€18','Theo']].map(([t,v,by],i)=>(
                <div key={i} style={{ display: 'flex', alignItems: 'center', gap: 10, padding: '9px 0', borderTop: `0.5px solid ${TH.hairThin}` }}>
                  <span style={{ flex: 1, fontFamily: TH.serif, fontSize: 14, color: TH.ink, letterSpacing: -0.1 }}>{t}</span>
                  <span style={{ fontFamily: TH.serif, fontStyle: 'italic', fontSize: 11, color: TH.mute }}>{by}</span>
                  <span style={{ fontFamily: TH.mono, fontSize: 11.5, color: TH.soft, fontWeight: 600 }}>{v}</span>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
      <TabBar active="trips"/>
    </Phone>
  );
}

Object.assign(window, { Sheet, SheetDestination, SheetDates, SheetPeople, SheetBudget, CostsLedger });
