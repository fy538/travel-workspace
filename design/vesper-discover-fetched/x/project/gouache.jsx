// ═══════════════════════════════════════════════════════════════
// GOUACHE — matte, flat-wash place illustrations for onboarding.
// A painterly step up from the line-art riso: soft wobbled edges +
// chalk grain over flat Vesper-muted colour fields. Authored in
// fractional coords so any w/h works. SWAP-READY: drop a real
// gouache <img>/<image-slot> over any <GouacheScene> later.
// ═══════════════════════════════════════════════════════════════

const GC = {
  cream: '#EAE3D6', sky: '#DED6C6', skyWarm: '#E7C9A2', skyCool: '#CCD2C8',
  sand: '#E0CBA2', ochre: '#C2974A', gold: '#D2A24A', goldSoft: '#DDBE84',
  terra: '#B0704A', terraDeep: '#9A5C3C', ink: '#2C3A4B', blue: '#41566E',
  blueSoft: '#637А8E'.replace('А', 'A'), teal: '#5C8884', sage: '#7E9176',
  sageSoft: '#9CAB8E', snow: '#F4EFE3', plum: '#7C5A63',
};

// shape helpers (flat fills; the filter does the painterliness)
const _R = (x, y, w, h, f, k) => <rect key={k} x={x} y={y} width={w} height={h} fill={f}/>;
const _E = (cx, cy, rx, ry, f, k) => <ellipse key={k} cx={cx} cy={cy} rx={rx} ry={ry} fill={f}/>;
const _P = (pts, f, k) => <polygon key={k} points={pts} fill={f}/>;

// each scene → array of shapes, authored in 0..W / 0..H px
const GUA = {
  island: (W, H) => [
    _R(-0.05 * W, -0.05 * H, 1.1 * W, 1.1 * H, GC.skyWarm, 'sky'),
    _E(0.74 * W, 0.30 * H, 0.13 * W, 0.13 * W, GC.gold, 'sun'),
    _E(0.16 * W, 0.55 * H, 0.34 * W, 0.10 * H, GC.sage, 'land'),
    _R(-0.05 * W, 0.56 * H, 1.1 * W, 0.22 * H, GC.teal, 'sea'),
    _R(-0.05 * W, 0.74 * H, 1.1 * W, 0.32 * H, GC.sand, 'beach'),
  ],
  city: (W, H) => [
    _R(-0.05 * W, -0.05 * H, 1.1 * W, 1.1 * H, GC.sky, 'sky'),
    _E(0.5 * W, 0.66 * H, 0.7 * W, 0.18 * H, GC.blue, 'hill'),
    _R(0.10 * W, 0.40 * H, 0.13 * W, 0.30 * H, GC.terra, 'b1'),
    _R(0.26 * W, 0.30 * H, 0.15 * W, 0.40 * H, GC.ochre, 'b2'),
    _R(0.45 * W, 0.46 * H, 0.12 * W, 0.24 * H, GC.terraDeep, 'b3'),
    _R(0.60 * W, 0.34 * H, 0.16 * W, 0.36 * H, GC.terra, 'b4'),
    _R(0.78 * W, 0.44 * H, 0.13 * W, 0.26 * H, GC.ochre, 'b5'),
    _R(-0.05 * W, 0.68 * H, 1.1 * W, 0.4 * H, GC.cream, 'grd'),
  ],
  food: (W, H) => [
    _R(-0.05 * W, -0.05 * H, 1.1 * W, 1.1 * H, GC.cream, 'bg'),
    _R(-0.05 * W, 0.60 * H, 1.1 * W, 0.5 * H, GC.terra, 'table'),
    _R(0.60 * W, 0.20 * H, 0.10 * W, 0.42 * H, GC.ink, 'bottle'),
    _E(0.60 * W, 0.20 * H, 0.05 * W, 0.05 * W, GC.ink, 'bottleTop'),
    _E(0.26 * W, 0.60 * H, 0.16 * W, 0.07 * H, GC.ochre, 'bowl1'),
    _E(0.50 * W, 0.61 * H, 0.12 * W, 0.055 * H, GC.sage, 'bowl2'),
    _E(0.74 * W, 0.61 * H, 0.13 * W, 0.06 * H, GC.goldSoft, 'bowl3'),
  ],
  wild: (W, H) => [
    _R(-0.05 * W, -0.05 * H, 1.1 * W, 1.1 * H, GC.skyCool, 'sky'),
    _P(`${-0.05 * W},${H} ${0.2 * W},${0.42 * H} ${0.4 * W},${0.78 * H} ${0.55 * W},${0.5 * H} ${0.78 * W},${0.86 * H} ${1.05 * W},${0.6 * H} ${1.05 * W},${H}`, GC.blue, 'mtn'),
    _P(`${0.2 * W},${0.42 * H} ${0.13 * W},${0.55 * H} ${0.28 * W},${0.55 * H}`, GC.snow, 'snow1'),
    _P(`${0.55 * W},${0.5 * H} ${0.48 * W},${0.62 * H} ${0.63 * W},${0.62 * H}`, GC.snow, 'snow2'),
    _E(0.5 * W, 1.02 * H, 0.7 * W, 0.22 * H, GC.sage, 'fg'),
  ],
  coast: (W, H) => [
    _R(-0.05 * W, -0.05 * H, 1.1 * W, 1.1 * H, GC.skyWarm, 'sky'),
    _R(-0.05 * W, 0.52 * H, 1.1 * W, 0.6 * H, GC.teal, 'sea'),
    _P(`${0.62 * W},${H} ${0.66 * W},${0.34 * H} ${0.82 * W},${0.30 * H} ${1.05 * W},${0.44 * H} ${1.05 * W},${H}`, GC.terra, 'cliff'),
    _E(0.74 * W, 0.32 * H, 0.18 * W, 0.08 * H, GC.sage, 'cliftop'),
  ],
  desert: (W, H) => [
    _R(-0.05 * W, -0.05 * H, 1.1 * W, 1.1 * H, GC.skyWarm, 'sky'),
    _E(0.30 * W, 0.30 * H, 0.11 * W, 0.11 * W, GC.gold, 'sun'),
    _E(0.30 * W, 0.66 * H, 0.7 * W, 0.16 * H, GC.ochre, 'dune1'),
    _E(0.80 * W, 0.78 * H, 0.6 * W, 0.16 * H, GC.sand, 'dune2'),
    _E(0.12 * W, 0.9 * H, 0.5 * W, 0.16 * H, GC.terra, 'dune3'),
  ],
  forest: (W, H) => [
    _R(-0.05 * W, -0.05 * H, 1.1 * W, 1.1 * H, GC.skyCool, 'sky'),
    _E(0.3 * W, 0.6 * H, 0.6 * W, 0.16 * H, GC.sageSoft, 'h1'),
    _E(0.8 * W, 0.66 * H, 0.6 * W, 0.16 * H, GC.sage, 'h2'),
    _P(`${0.3 * W},${0.32 * H} ${0.22 * W},${0.62 * H} ${0.38 * W},${0.62 * H}`, GC.ink, 't1'),
    _P(`${0.5 * W},${0.4 * H} ${0.43 * W},${0.66 * H} ${0.57 * W},${0.66 * H}`, GC.blue, 't2'),
    _P(`${0.7 * W},${0.34 * H} ${0.62 * W},${0.64 * H} ${0.78 * W},${0.64 * H}`, GC.ink, 't3'),
    _R(-0.05 * W, 0.74 * H, 1.1 * W, 0.4 * H, GC.sage, 'grd'),
  ],
  harbor: (W, H) => [
    _R(-0.05 * W, -0.05 * H, 1.1 * W, 1.1 * H, GC.sky, 'sky'),
    _R(-0.05 * W, 0.56 * H, 1.1 * W, 0.6 * H, GC.blue, 'water'),
    _R(0.30 * W, 0.20 * H, 0.012 * W, 0.34 * H, GC.ink, 'mast1'),
    _R(0.62 * W, 0.24 * H, 0.012 * W, 0.30 * H, GC.ink, 'mast2'),
    _P(`${0.2 * W},${0.56 * H} ${0.42 * W},${0.56 * H} ${0.37 * W},${0.66 * H} ${0.25 * W},${0.66 * H}`, GC.terra, 'hull1'),
    _P(`${0.54 * W},${0.56 * H} ${0.74 * W},${0.56 * H} ${0.70 * W},${0.65 * H} ${0.58 * W},${0.65 * H}`, GC.ochre, 'hull2'),
  ],
};

function GouacheScene({ scene = 'island', w = 320, h = 200 }) {
  const uid = React.useMemo(() => 'gua' + Math.random().toString(36).slice(2, 8), []);
  const build = GUA[scene] || GUA.island;
  return (
    <svg width="100%" height="100%" viewBox={`0 0 ${w} ${h}`} preserveAspectRatio="xMidYMid slice" style={{ display: 'block' }}>
      <defs>
        <filter id={uid + 'e'} x="-8%" y="-8%" width="116%" height="116%">
          <feTurbulence type="fractalNoise" baseFrequency="0.013 0.02" numOctaves="2" seed="4" result="n"/>
          <feDisplacementMap in="SourceGraphic" in2="n" scale="8" xChannelSelector="R" yChannelSelector="G"/>
        </filter>
        <filter id={uid + 'g'} x="0" y="0" width="100%" height="100%">
          <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" stitchTiles="stitch" result="g"/>
          <feColorMatrix in="g" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 0.7 0"/>
        </filter>
      </defs>
      <g filter={`url(#${uid}e)`}>{build(w, h)}</g>
      <rect x="0" y="0" width={w} height={h} filter={`url(#${uid}g)`} opacity="0.09" style={{ mixBlendMode: 'multiply' }}/>
    </svg>
  );
}

Object.assign(window, { GouacheScene });
