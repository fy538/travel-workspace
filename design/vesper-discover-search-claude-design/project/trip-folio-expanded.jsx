// ═══════════════════════════════════════════════════════════════
// EXPANDED FOLIO — System 1, fleshed out as a full scrollable screen.
// Rebalanced: cover 220 · Vesper line · richer spine · status · tiles.
// Top-right: group (with unread dot) + settings. First viewport resolves;
// the spine + extras scroll below the fold.
// Reuses DR + Filmstrip/VLine/Ppl/CASTD/TGI/Cap + StyleRiso/StyleGouache.
// ═══════════════════════════════════════════════════════════════

// Glass icon button for the cover.
function GlassIco({ children, dot }) {
  return (
    <div style={{ position: 'relative', width: 36, height: 36, borderRadius: 999, background: 'rgba(255,255,255,0.2)', backdropFilter: 'blur(8px)', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
      {children}
      {dot && <span style={{ position: 'absolute', top: 4, right: 4, width: 8, height: 8, borderRadius: 8, background: DR.gold, border: '1.5px solid rgba(20,14,9,0.5)', boxSizing: 'content-box' }}/>}
    </div>
  );
}
const Ico = {
  back: (c='#fff') => <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d="M14 6l-6 6 6 6"/></svg>,
  chat: (c='#fff') => <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><path d="M4 5h16v11H8l-4 4z"/></svg>,
  gear: (c='#fff') => <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke={c} strokeWidth="1.6" strokeLinecap="round"><circle cx="12" cy="12" r="3"/><path d="M19 12a7 7 0 0 0-.1-1l2-1.5-2-3.5-2.4 1a7 7 0 0 0-1.7-1l-.4-2.5h-4l-.4 2.5a7 7 0 0 0-1.7 1l-2.4-1-2 3.5 2 1.5a7 7 0 0 0 0 2l-2 1.5 2 3.5 2.4-1a7 7 0 0 0 1.7 1l.4 2.5h4l.4-2.5a7 7 0 0 0 1.7-1l2.4 1 2-3.5-2-1.5a7 7 0 0 0 .1-1z"/></svg>,
};

// Richer spine row — riso thumb + title + meta, like the itinerary blocks.
function FolioBlock({ day, date, thumb, title, sub, gap, first }) {
  return (
    <div style={{ display: 'grid', gridTemplateColumns: '38px 1fr', gap: 13, padding: '12px 0', borderTop: first ? 'none' : `0.5px solid ${DR.hairThin}` }}>
      <div style={{ textAlign: 'center', paddingTop: 2 }}>
        <div style={{ fontSize: 8, letterSpacing: 0.8, color: DR.mute, fontWeight: 700 }}>{day}</div>
        <div style={{ fontFamily: DR.serif, fontSize: 20, fontWeight: 500, color: DR.ink, lineHeight: 1, marginTop: 1, letterSpacing: -0.4 }}>{date}</div>
      </div>
      <div style={{ display: 'flex', gap: 11, alignItems: 'center' }}>
        {thumb && <div style={{ width: 46, height: 46, borderRadius: 9, overflow: 'hidden', flexShrink: 0 }}><StyleRiso w={46} h={46}/></div>}
        <div style={{ flex: 1, minWidth: 0 }}>
          <div style={{ fontFamily: DR.serif, fontSize: 15.5, fontWeight: 500, color: gap ? DR.mute : DR.ink, fontStyle: gap ? 'italic' : 'normal', letterSpacing: -0.2, lineHeight: 1.15 }}>{title}</div>
          {sub && <div style={{ fontFamily: DR.serif, fontStyle: 'italic', fontSize: 11.5, color: DR.mute, marginTop: 3 }}>{sub}</div>}
        </div>
      </div>
    </div>
  );
}

// The expanded folio — tall, scrollable. `foldAt` draws a dashed "fold" guide.
function FolioExpanded({ showFold }) {
  return (
    <div style={{ width: 393, background: DR.paper, borderRadius: 30, overflow: 'hidden', border: `0.5px solid ${DR.hair}`, boxShadow: '0 30px 60px -30px rgba(0,0,0,0.3)', position: 'relative', paddingBottom: 8 }}>
      {/* status bar */}
      <div style={{ height: 40, display: 'flex', alignItems: 'flex-end', justifyContent: 'space-between', padding: '0 24px 4px' }}>
        <span style={{ fontFamily: '-apple-system, system-ui', fontWeight: 600, fontSize: 14, color: '#fff', mixBlendMode: 'difference' }}>9:41</span>
      </div>

      {/* ── ZONE 1 · COVER (220) ── */}
      <div style={{ position: 'relative', height: 220, marginTop: -40 }}>
        <div style={{ position: 'absolute', inset: 0 }}><StyleRiso w={393} h={220}/></div>
        <div style={{ position: 'absolute', inset: 0, background: 'linear-gradient(to bottom, rgba(20,14,9,0.42) 0%, rgba(20,14,9,0) 30%, rgba(20,14,9,0) 46%, rgba(20,14,9,0.72) 100%)' }}/>
        {/* top row: back + group/settings */}
        <div style={{ position: 'absolute', top: 46, left: 16, right: 16, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
          <GlassIco>{Ico.back()}</GlassIco>
          <div style={{ display: 'flex', gap: 9 }}>
            <GlassIco dot>{Ico.chat()}</GlassIco>
            <GlassIco>{Ico.gear()}</GlassIco>
          </div>
        </div>
        <div style={{ position: 'absolute', top: 92, left: 18 }}><Filmstrip truth={1} onDark/></div>
        {/* identity */}
        <div style={{ position: 'absolute', left: 20, right: 20, bottom: 16 }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 7 }}>
            <span style={{ padding: '3px 9px', borderRadius: 999, background: 'rgba(255,255,255,0.2)', backdropFilter: 'blur(6px)', fontSize: 9, letterSpacing: 1.4, fontWeight: 700, color: '#fff' }}>IN 23 DAYS</span>
            <Ppl who={CASTD} size={22} onDark/>
          </div>
          <h1 style={{ fontFamily: DR.serif, fontSize: 34, fontWeight: 500, letterSpacing: -1, lineHeight: 0.98, color: '#fff', margin: 0 }}>Lisbon, <span style={{ fontStyle: 'italic' }}>slowly</span></h1>
          <div style={{ fontFamily: DR.mono, fontSize: 9.5, color: 'rgba(255,255,255,0.85)', letterSpacing: 1, marginTop: 6 }}>MAY 18 – 24 · 6 NIGHTS</div>
        </div>
      </div>

      {/* ── ZONE 2 · VESPER LINE ── */}
      <div style={{ padding: '15px 20px 0' }}>
        <VLine>The only thing missing is where you sleep nights 5–7 — I’ve found three you’d like.</VLine>
        <div style={{ marginTop: 12, display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '11px 14px', background: DR.card, borderRadius: 12, border: `0.8px solid rgba(176,133,58,0.4)` }}>
          <div>
            <div style={{ fontSize: 9, letterSpacing: 1.4, color: DR.goldDeep, fontWeight: 700 }}>NEEDS YOU · 1 OF 4 DECISIONS</div>
            <div style={{ fontFamily: DR.serif, fontSize: 14.5, color: DR.ink, fontWeight: 500, marginTop: 2, letterSpacing: -0.1 }}>Pick a stay for nights 5–7</div>
          </div>
          <span style={{ padding: '7px 13px', background: DR.blue, color: '#fff', borderRadius: 999, fontSize: 11.5, fontWeight: 600 }}>Open →</span>
        </div>
      </div>

      {/* booking status strip */}
      <div style={{ padding: '14px 20px 0' }}>
        <div style={{ display: 'flex', gap: 8 }}>
          {[['FLIGHTS','Booked',true],['STAY','3 of 5 nights',false],['CAR','Not needed',null]].map(([k,v,done])=>(
            <div key={k} style={{ flex: 1, padding: '9px 11px', background: DR.cardSoft, borderRadius: 10, border: `0.5px solid ${DR.hairThin}` }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: 5 }}>
                <span style={{ width: 5, height: 5, borderRadius: 5, background: done ? '#3D7050' : done === false ? DR.gold : DR.faint }}/>
                <span style={{ fontSize: 8, letterSpacing: 1.2, color: DR.mute, fontWeight: 700 }}>{k}</span>
              </div>
              <div style={{ fontFamily: DR.serif, fontSize: 12.5, color: DR.ink, marginTop: 3, letterSpacing: -0.1 }}>{v}</div>
            </div>
          ))}
        </div>
      </div>

      {/* fold guide */}
      {showFold && (
        <div style={{ margin: '16px 0 0', display: 'flex', alignItems: 'center', gap: 8, padding: '0 20px' }}>
          <span style={{ flex: 1, height: 1, borderTop: `1px dashed ${DR.faint}` }}/>
          <span style={{ fontFamily: DR.mono, fontSize: 8.5, color: DR.faint, letterSpacing: 1.4 }}>FOLD · 852pt</span>
          <span style={{ flex: 1, height: 1, borderTop: `1px dashed ${DR.faint}` }}/>
        </div>
      )}

      {/* ── ZONE 3 · SPINE (richer, scrolls) ── */}
      <div style={{ padding: '16px 20px 0' }}>
        <Cap>THE DAYS, TAKING SHAPE</Cap>
        <FolioBlock first day="SAT" date="18" thumb title="Land soft, settle in Alfama" sub="no plans past the first coffee"/>
        <FolioBlock day="SUN" date="19" thumb title="Miradouros, east to west" sub="Ana’s walking list · 4 stops"/>
        <FolioBlock day="MON" date="20" title="a sparse day" sub="ask Vesper to fill it" gap/>
        <FolioBlock day="TUE" date="21" thumb title="Belém, early" sub="beat the crowd to the cloister"/>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginTop: 12, paddingTop: 12, borderTop: `0.5px solid ${DR.hairThin}` }}>
          <span style={{ fontFamily: DR.serif, fontSize: 14, fontWeight: 500, color: DR.ink, letterSpacing: -0.1 }}>Open the full itinerary</span>
          <span style={{ color: DR.blue, fontSize: 14 }}>→</span>
        </div>
      </div>

      {/* ── ZONE 4 · TILES ── */}
      <div style={{ padding: '18px 18px 8px' }}>
        <div style={{ display: 'flex', gap: 8 }}>
          {[[TGI.map,'Route','3 cities'],[TGI.costs,'Costs','€1.4k · split 3'],[TGI.group,'Group','12 new']].map(([g,l,m],i)=>(
            <div key={i} style={{ flex: 1, padding: '12px 12px', background: DR.card, borderRadius: 12, border: `0.5px solid ${DR.hair}` }}>
              <div style={{ color: DR.soft, marginBottom: 8 }}>{g}</div>
              <div style={{ fontFamily: DR.serif, fontSize: 13.5, fontWeight: 500, color: DR.ink, letterSpacing: -0.2, lineHeight: 1 }}>{l}</div>
              <div style={{ fontSize: 9.5, color: DR.mute, fontFamily: DR.mono, letterSpacing: 0.4, marginTop: 4 }}>{m}</div>
            </div>
          ))}
        </div>
        {/* share the trip */}
        <div style={{ marginTop: 10, display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 7, padding: '11px 0', borderRadius: 12, border: `0.5px solid ${DR.hair}`, color: DR.soft }}>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke={DR.soft} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><path d="M12 3v13M8 7l4-4 4 4M5 13v6a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-6"/></svg>
          <span style={{ fontFamily: DR.serif, fontSize: 13.5, fontWeight: 500, letterSpacing: -0.1 }}>Share the folio</span>
        </div>
      </div>
    </div>
  );
}

Object.assign(window, { FolioExpanded, FolioBlock, GlassIco, Ico });
