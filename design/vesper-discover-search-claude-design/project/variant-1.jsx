// Variant 1 — REFINED: premium iOS, generous spacing, intentional hierarchy.
// 2x2 grid feels tactile but restrained. Quiet metadata tells a story.

function VariantRefined() {
  return (
    <Phone bg={T.bg}>
      {/* ── Top bar ── */}
      <div style={{
        display: 'flex', alignItems: 'center', justifyContent: 'space-between',
        padding: '14px 24px 0',
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 6, color: T.mute, fontSize: 12, letterSpacing: 1.4, fontWeight: 500 }}>
          <svg width="11" height="11" viewBox="0 0 12 12" fill="none">
            <circle cx="6" cy="6" r="3.5" fill={T.gold}/>
          </svg>
          <span>VOL. III · SPRING ’26</span>
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: 14 }}>
          <Marks.Search s={20} c={T.inkSoft}/>
          <div style={{
            width: 30, height: 30, borderRadius: 999, background: T.goldDeep,
            color: T.cardWarm, fontFamily: T.serif, fontWeight: 500, fontSize: 14,
            display: 'flex', alignItems: 'center', justifyContent: 'center',
            letterSpacing: 0.5,
          }}>T</div>
        </div>
      </div>

      {/* ── Identity block ── */}
      <div style={{ padding: '38px 24px 6px' }}>
        <div style={{ color: T.mute, fontSize: 11, letterSpacing: 2.2, fontWeight: 600, marginBottom: 12 }}>
          TIGER’S ATLAS
        </div>
        <h1 style={{
          fontFamily: T.serif, fontWeight: 400, fontSize: 56, lineHeight: 0.95,
          letterSpacing: -1.2, color: T.ink, margin: 0,
        }}>
          A quieter<br/>
          <span style={{ fontStyle: 'italic', color: T.inkSoft }}>kind of week.</span>
        </h1>
        <p style={{
          fontFamily: T.serif, fontStyle: 'italic', fontSize: 16, color: T.mute,
          lineHeight: 1.4, margin: '22px 0 0', maxWidth: 280,
        }}>
          “You follow the neighborhood before the landmark.”
        </p>
        <div style={{
          display: 'flex', alignItems: 'center', gap: 8, marginTop: 10,
          color: T.muteSoft, fontSize: 10.5, letterSpacing: 1.6, fontWeight: 600,
        }}>
          <span>VESPER’S NOTE</span>
          <span style={{ width: 22, height: 1, background: T.muteSoft, opacity: 0.5 }}/>
          <span>03·14</span>
        </div>
      </div>

      {/* ── 2x2 grid ── */}
      <div style={{
        margin: '26px 16px 0', display: 'grid', gridTemplateColumns: '1fr 1fr',
        gap: 10,
      }}>
        {[
          { mark: <Marks.Inbox size={70}/>,   name: 'Inbox',     meta: '3 drafts',     hint: 'waiting for you' },
          { mark: <Marks.Map size={70}/>,     name: 'Map',       meta: '14 cities',    hint: 'across 7 countries' },
          { mark: <Marks.DNA size={70}/>,     name: 'Travel DNA',meta: '6 rituals',    hint: 'an early-morning soul' },
          { mark: <Marks.Postcard size={70}/>,name: 'Postcards', meta: '0 sent',       hint: 'shelf is bare' },
        ].map((it, i) => (
          <div key={i} style={{
            background: T.cardWarm, borderRadius: 22, padding: '18px 18px 16px',
            height: 180, position: 'relative', overflow: 'hidden',
            boxShadow: '0 0 0 0.5px rgba(27,23,20,0.05), 0 1px 0 rgba(255,255,255,0.7) inset',
          }}>
            <div style={{
              position: 'absolute', top: 18, left: '50%', transform: 'translateX(-50%)',
            }}>
              {it.mark}
            </div>
            <div style={{ position: 'absolute', bottom: 14, left: 18, right: 18 }}>
              <div style={{ fontFamily: T.serif, fontSize: 22, fontWeight: 500, color: T.ink, letterSpacing: -0.3, lineHeight: 1 }}>
                {it.name}
              </div>
              <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', marginTop: 6 }}>
                <span style={{ fontSize: 11, color: T.mute, fontWeight: 500 }}>{it.meta}</span>
                <span style={{ fontSize: 10, color: T.muteSoft, fontStyle: 'italic', fontFamily: T.serif }}>{it.hint}</span>
              </div>
            </div>
            {/* tiny corner mark — gold dot when fresh */}
            {i === 0 && (
              <div style={{ position: 'absolute', top: 16, right: 16, width: 6, height: 6, borderRadius: 6, background: T.gold }}/>
            )}
          </div>
        ))}
      </div>

      {/* ── Latest postcard row ── */}
      <div style={{ margin: '20px 24px 0', display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
        <span style={{ fontSize: 10.5, color: T.mute, letterSpacing: 2, fontWeight: 600 }}>LATEST POSTCARD</span>
        <span style={{ fontSize: 10.5, color: T.muteSoft, letterSpacing: 1.5, fontWeight: 500, display: 'flex', alignItems: 'center', gap: 6 }}>
          NONE YET <Marks.ArrowR s={11} c={T.muteSoft}/>
        </span>
      </div>
      <div style={{
        margin: '10px 16px 0', background: T.card, borderRadius: 20,
        padding: '18px 20px', display: 'flex', alignItems: 'center', gap: 14,
      }}>
        <div style={{
          width: 56, height: 70, borderRadius: 4, background: T.cardWarm,
          border: `0.5px solid ${T.hairline}`, position: 'relative', flexShrink: 0,
          boxShadow: '0 6px 14px -8px rgba(0,0,0,0.2)',
        }}>
          <div style={{ position: 'absolute', inset: 6, border: `0.5px dashed ${T.muteSoft}`, borderRadius: 2 }}/>
          <Marks.Plus s={14} c={T.mute}/>
          <div style={{ position: 'absolute', inset: 0, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
            <Marks.Plus s={14} c={T.muteSoft}/>
          </div>
        </div>
        <div style={{ flex: 1 }}>
          <div style={{ fontFamily: T.serif, fontSize: 17, color: T.ink, fontWeight: 500, lineHeight: 1.2 }}>
            Your first postcard will land here.
          </div>
          <div style={{ fontSize: 11.5, color: T.mute, marginTop: 4, lineHeight: 1.4 }}>
            Open Inbox when a memory feels worth keeping.
          </div>
        </div>
      </div>

      <TabBar active="atlas"/>
    </Phone>
  );
}

window.VariantRefined = VariantRefined;
