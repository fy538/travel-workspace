// ═══════════════════════════════════════════════════════════════
// DISCOVER SEARCH · THE BLEND (A + B) — general, context-aware.
// Search reaches EVERYTHING Vesper knows (places, reads, venues,
// guides) and understands a typed desire. Vesper routes by query:
//   · lookup/entity  → clean structured groups (A)
//   · fuzzy intent   → violet "I read this as" + meaning groups (B)
// Not scoped to the current place — a place is just one result kind;
// a small changeable context chip disambiguates intent. Ask Vesper
// is the violet hatch under every query.
// Reuses SearchField, SearchGroup, AskVesperRow, PlaceRow, VenueRow,
// ReadRow + T, D, Plate, Spark, VesperBy, LensChip, DIcon.
// ═══════════════════════════════════════════════════════════════

const bz = `0.5px solid ${T.hairline}`;
const bzT = `0.5px solid ${T.hairThin}`;

// Interpretation card (intent mode) with a changeable context chip.
function BlendInterpret({ read, context = 'Lisbon' }) {
  return (
    <div style={{ margin: '18px 22px 0', padding: '14px 16px', background: D.vesperSoft, borderRadius: 14, border: `0.5px solid ${D.vesperRule}` }}>
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 7 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 7 }}>
          <Spark s={13}/>
          <span style={{ fontSize: 9, letterSpacing: 1.6, fontWeight: 700, color: D.vesperDeep }}>I READ THIS AS</span>
        </div>
        <span style={{ display: 'inline-flex', alignItems: 'center', gap: 4, fontSize: 11, color: D.vesperDeep, fontWeight: 500, padding: '3px 9px', borderRadius: 999, border: `0.5px solid ${D.vesperRule}` }}>
          {context} <span style={{ fontSize: 8, opacity: 0.7 }}>▾</span>
        </span>
      </div>
      <p style={{ fontFamily: T.serif, fontSize: 16.5, fontStyle: 'italic', color: D.vesperDeep, lineHeight: 1.4, margin: 0, letterSpacing: -0.1 }}>{read}</p>
    </div>
  );
}

// ── EMPTY · general (recents + prompt) ──────────────────────────
function SearchX_Empty() {
  const intents = ['a quiet dinner, just us', 'fado but not touristy', 'somewhere good in the rain'];
  return (
    <Phone bg={T.bg}>
      <div style={{ paddingTop: 8 }}><SearchField query="" placeholder="Search anywhere, or just ask…" focused/></div>
      <div style={{ padding: '22px 22px 0', display: 'flex', alignItems: 'center', gap: 8 }}>
        <Spark s={13}/>
        <span style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 14, color: T.mute, lineHeight: 1.4 }}>
          A place, a read, a restaurant — or just the mood you’re in.
        </span>
      </div>
      <div style={{ padding: '20px 22px 0' }}>
        <SearchGroup right="CLEAR">RECENT</SearchGroup>
        <PlaceRow name="Tokyo" sub="read 3 days ago" glyph="hills"/>
        <div style={{ borderTop: bzT }}><ReadRow title="Where fado is grief, not nightlife" lens="The debate" place="Lisbon"/></div>
        <div style={{ borderTop: bzT }}><PlaceRow name="Mexico City" sub="saved" glyph="square"/></div>
      </div>
      <div style={{ padding: '20px 22px 0' }}>
        <SearchGroup>TRY ASKING</SearchGroup>
        <div style={{ display: 'flex', flexDirection: 'column' }}>
          {intents.map((t, i) => (
            <div key={t} style={{ display: 'flex', alignItems: 'center', gap: 11, padding: '12px 4px', borderTop: i ? bzT : 'none' }}>
              <span style={{ color: D.vesper, fontSize: 13 }}>“</span>
              <span style={{ flex: 1, fontFamily: T.serif, fontSize: 16.5, color: T.inkSoft, letterSpacing: -0.2 }}>{t}</span>
              <span style={{ color: T.muteSoft, fontSize: 13 }}>↑</span>
            </div>
          ))}
        </div>
      </div>
    </Phone>
  );
}

// ── TYPED · LOOKUP (entity) — structured groups, global ─────────
function SearchX_Lookup() {
  return (
    <Phone bg={T.bg}>
      <div style={{ paddingTop: 8 }}><SearchField query="tok" focused={false}/></div>
      <div style={{ padding: '18px 22px 0', display: 'flex', alignItems: 'center', gap: 8 }}>
        <span style={{ fontFamily: T.mono, fontSize: 9, color: T.mute, letterSpacing: 1, fontWeight: 600 }}>EVERYWHERE VESPER READS</span>
        <span style={{ flex: 1, borderBottom: bzT }}/>
      </div>
      <div style={{ padding: '14px 22px 0' }}>
        <SearchGroup>PLACES</SearchGroup>
        <PlaceRow name="Tokyo" sub="Japan · you read this 3 days ago" glyph="hills"/>
        <div style={{ borderTop: bzT }}><PlaceRow name="Tokushima" sub="Shikoku · the whirlpools & Awa dance" glyph="coast"/></div>
      </div>
      <div style={{ padding: '18px 22px 0' }}>
        <SearchGroup>READS</SearchGroup>
        <ReadRow title="Tokyo without the checklist" lens="Why here" place="Tokyo"/>
        <div style={{ borderTop: bzT }}><ReadRow title="The city’s last great kissaten" lens="For the obsessed" place="Tokyo"/></div>
      </div>
      <div style={{ padding: '18px 22px 0' }}>
        <SearchGroup>PLACES TO GO</SearchGroup>
        <VenueRow name="Toki, in Sangenjaya" kind="IZAKAYA" hook="Eight seats, no sign, counter only" glyph="alley"/>
      </div>
      <div style={{ padding: '20px 22px 0' }}><AskVesperRow q="tok"/></div>
    </Phone>
  );
}

// ── TYPED · INTENT (fuzzy) — interpretation + meaning groups ────
function SearchX_Intent() {
  return (
    <Phone bg={T.bg}>
      <div style={{ paddingTop: 8 }}><SearchField query="fado but not touristy" focused={false}/></div>
      <BlendInterpret read="The real thing — a small house where locals still go to listen, not a dinner-and-show." context="Lisbon"/>
      <div style={{ padding: '20px 22px 0' }}>
        <SearchGroup>I’D START HERE</SearchGroup>
        <div style={{ borderRadius: 16, overflow: 'hidden', border: bz, background: T.card }}>
          <Plate variant="alley" style={{ height: 128 }} dim={0.08}>
            <div style={{ position: 'absolute', top: 11, left: 11 }}><LensChip lens="Insider" onDark/></div>
          </Plate>
          <div style={{ padding: '13px 15px' }}>
            <div style={{ fontFamily: T.serif, fontSize: 19, fontWeight: 500, color: T.ink, letterSpacing: -0.3, lineHeight: 1.1 }}>A Tasca do Chico, late</div>
            <p style={{ fontFamily: T.serif, fontStyle: 'italic', fontSize: 13.5, color: T.mute, lineHeight: 1.4, margin: '6px 0 0' }}>
              No stage, no cover. The singing starts when someone feels like it — usually after eleven.
            </p>
            <div style={{ marginTop: 10, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
              <VesperBy/>
              <span style={{ fontFamily: T.mono, fontSize: 9, color: T.muteSoft, letterSpacing: 1 }}>ALFAMA · 6 MIN WALK</span>
            </div>
          </div>
        </div>
      </div>
      <div style={{ padding: '20px 22px 0' }}>
        <SearchGroup>PLACES THAT MATCH</SearchGroup>
        <VenueRow name="Mesa de Frades" kind="FADO" hook="A tiled former chapel; book the late seating" glyph="tiles"/>
        <div style={{ borderTop: bzT }}><VenueRow name="Sr. Fado" kind="FADO" hook="Family-run; the owners sing" glyph="alley"/></div>
      </div>
      <div style={{ padding: '20px 22px 0' }}><AskVesperRow q="fado but not touristy"/></div>
    </Phone>
  );
}

// ── NO RESULTS · honest reframe ─────────────────────────────────
function SearchX_NoResults() {
  return (
    <Phone bg={T.bg}>
      <div style={{ paddingTop: 8 }}><SearchField query="michelin stars under €20" focused={false}/></div>
      <div style={{ margin: '24px 22px 0', padding: '20px', background: D.vesperSoft, borderRadius: 16, border: `0.5px solid ${D.vesperRule}` }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 10 }}>
          <Spark s={15}/>
          <span style={{ fontSize: 9.5, letterSpacing: 1.6, fontWeight: 700, color: D.vesperDeep }}>HONESTLY</span>
        </div>
        <p style={{ fontFamily: T.serif, fontSize: 18, color: D.vesperDeep, lineHeight: 1.5, margin: 0, letterSpacing: -0.1 }}>
          That exact thing doesn’t really exist — but the <span style={{ fontStyle: 'italic' }}>feeling</span> you’re after does: extraordinary food, almost nothing spent.
        </p>
      </div>
      <div style={{ padding: '20px 22px 0' }}>
        <SearchGroup>WHAT I’D POINT YOU TO INSTEAD</SearchGroup>
        <VenueRow name="O Velho Eurico" kind="TASCA" hook="Chef-run tasca, plates around €9" glyph="alley"/>
        <div style={{ borderTop: bzT }}><VenueRow name="Cervejaria Ramiro" kind="MARISCO" hook="The seafood worth the splurge — still honest" glyph="square"/></div>
      </div>
      <div style={{ padding: '22px 22px 0' }}><AskVesperRow q="cheap but extraordinary"/></div>
    </Phone>
  );
}

Object.assign(window, { SearchX_Empty, SearchX_Lookup, SearchX_Intent, SearchX_NoResults });
