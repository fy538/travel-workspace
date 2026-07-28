---
doc_type: working
status: active
owner: founder / product
created: 2026-07-28
expires: 2026-08-27
why_new: The 2026-07-27 chat type fork settled a rule (one body role for every speaker; a byline signature) but no doc carries the implementation path. Verifying it against the code found three blockers that change the rule — recorded here.
promotes_to: travel-app/docs/surfaces/vesper-chat/contract.md (typography + attribution sections)
supersedes: []
source_of_truth_for:
  - chat-typography-implementation-plan
---

# Chat typography — implementation plan

> Four landings, smallest first, each shippable alone. Design source:
> Claude Design → Vesper → "Vesper Chat - Type Fork.html".
>
> **Read §0 first.** Verifying the adopted rule against the code found
> three blockers. One of them changes the rule itself.

---

## §0 — Blockers found while verifying (read before anything)

### B1 · The byline cannot be italic. It must be Roman.

The design board specifies "Vesper" in EB Garamond **italic**. That is
not implementable, and not by accident.

`constants/fonts.ts:18-21`:

> "Production is Roman-first: italic faces are **intentionally not
> registered yet**. If the product approves a limited italic register,
> add the face and named semantic role together; **never synthesize or
> register slant at an individual call site**."

Corroborating evidence:
- `hooks/useAppFonts.ts` loads only `EBGaramond_400Regular / _500Medium
  / _600SemiBold / _700Bold`. No italic face is bundled.
- `grep "fontStyle: 'italic'" components constants` → **0 hits.** The
  app has never used italic.
- `constants/fonts.ts:24-25` — even if registered, "**Italic, if ever
  registered, never below 17px**", so a 15px italic byline would fail
  the floor regardless.

Setting `fontStyle: 'italic'` on a Roman-only family gets you
synthesized oblique on Android and inconsistent behaviour on iOS —
which is exactly what "never synthesize" forbids.

**Resolution:** the byline is **EB Garamond Roman, 15px**. It still
reads as a signature against mono caps; the contrast doing the work is
*serif vs mono*, not *italic vs roman*.

**Wider blast radius — check before other work lands.** The
2026-07-27 trips-home stack model also specifies serif italic in
several places (the crowned read's emphasis phrase, the companion
thread quote, the H1's emphasis word). Those are subject to the same
rule and need the same correction — carry emphasis with **colour and
weight**, not slant. See `trips-home-promotion-model-2026-07-27.md`.

### B2 · `scale='byline'` today is sans 12, and one caller labels a human.

`VesperSignature` renders the byline branch as `VText variant="caption"`
plus `styles.labelByline`, and `labelByline` is only `{ flexShrink: 1 }`
(`VesperSignature.tsx:176-178`). `caption` is
`{ fontFamily: sans, fontSize: 12, color: text.secondary }`
(`textVariants.ts:63`). So the byline scale is **sans 12**, not serif.

My earlier "no new component API" claim was half-wrong: the *props*
exist, but the byline's rendering must change.

**And it cannot simply be mutated.** `scale='byline'` has two callers
outside the chat transcript:

| Site | Use |
|---|---|
| `components/discover/DiscoverAtoms.tsx:55` | Discover published-editorial voice, `tone='discover'` |
| `components/chat/GroupMemberAskingBanner.tsx:82` | `label={userName} suffix="asking Vesper…"` — **labels a human** |

Turning `byline` serif would render *a member's name* in Vesper's
signature face. That is a semantic regression, not a style tweak.

**Resolution:** add a distinct scale — `scale='signature'` — for the
agent's byline, and leave `byline` alone. `serifBody`
(`textVariants.ts:93`, serif 15/22) is exactly at the floor and is the
natural basis for the new role.

### B3 · No font-scaling policy exists.

`components/ui/Text.tsx` declares no `allowFontScaling` or
`maxFontSizeMultiplier`, so RN's default (scaling **on**, unbounded)
applies. Moving the transcript from 15/22 to 16/26 raises the base that
accessibility multipliers apply to. Not a blocker, but Landing 2 should
be looked at once at the largest Dynamic Type setting before it ships.

---

## The rule, corrected

**Body** — System Sans **16/26**, every speaker, both rooms. Identity
comes from two registers, never from type: the *agent register*
(Vesper — unbubbled prose + signature) and the *human register* (you
and every member — identical type, separated by alignment, avatar,
name).

**Signature** — Guiding Star mark + "Vesper" in **EB Garamond Roman
15px** (at the serif floor) + an addressee in group rooms set in
**sans 12** + a trailing mono stamp. **No hairline rule.**

Rejected, with reasons on the design page: scale asymmetry
(unconventional; collapses at a third speaker), mono-caps label (reads
as SYSTEM/DEBUG/APP), mark-with-no-label (fails in group), full-width
hairline (reads as a divider), serif message bodies (costs serif its
job marking bounded artifacts), **serif italic anything** (B1).

---

## Landing 1 — the leading regression — ✅ SHIPPED 2026-07-28

**Pure bug fix. No design dependency.**

**Root cause, as planned.** A wave-5 variant migration (`48d5d06d`,
2026-07-22) swapped the user turn from `typography.chatTranscript` to
`VText variant="bodyMd"`. Both are sans 15 regular, but `bodyMd`
(`textVariants.ts:51`) declares **no `lineHeight`**, so the user turn
fell back to the platform default (~1.20) while the assistant rendered
at `chatTranscript`'s 22 (1.47). Two registers in one thread, by
accident.

**The mechanism actually used differs from the original plan text
above ("route it through `typography.chatTranscript`") — recorded
here because Landings 2 and 3 build on the corrected version.**
`VText`'s `variant` prop is `keyof typeof textVariants`
(`constants/textVariants.ts`), a closed union — `typography.ts`
(where `chatTranscript` lives) is a *different, legacy* registry that
`VText` cannot reference directly. `Text.tsx`'s own doc comment states
the governing rule: *"If no variant fits, that's a real design
decision — add a variant deliberately, don't reach for a raw style
override instead."* Patching this with `style={{lineHeight: 22}}` on
`bodyMd` would have violated that rule.

**What shipped:**
1. Added a new variant, `chatTranscript`, to `constants/textVariants.ts`
   (sans 15/22/0, mirroring `typography.chatTranscript`'s current
   numbers exactly) — placed directly after `bodyMd`, with a doc
   comment cross-referencing both files and noting they must be kept
   numerically in sync by hand until the `typography.ts` migration
   reaches this role.
2. `bodyMd`'s own doc comment corrected — it advertised itself for
   "message bubbles," which was the root confusion; now points readers
   to `chatTranscript` instead.
3. `components/chat/MessageBubble.tsx:181` — `variant="bodyMd"` →
   `variant="chatTranscript"`. This single branch handles **both**
   self and other-member human turns (`isSelf ? paper : ink` is just a
   colour swap on the same element), so 1:1 and group are both fixed
   by one call site.
4. `components/chat/MessageBubble.tsx:360` stale comment ("ink fill,
   warm serif text") corrected to describe the sans transcript variant.
5. **Also fixed, found adjacent:** `serifProseCompact`'s doc comment in
   `textVariants.ts` labeled itself "(chat/conversational editorial
   copy)" — a leftover from the pre-07-22 serif-chat world. Confirmed
   via grep it has zero chat call sites (used by Atlas reflections,
   dossier thesis lines, `ChoosePlaceSheet`); corrected to say so and
   point to `chatTranscript` for chat.

**Explicitly did NOT** touch `bodyMd`'s style object. It has **29 call
sites** across `components/` and `app/`, unrelated to chat; adding
`lineHeight` there would have reflowed all of them.

**Verified:**
- `npm run typecheck` — clean.
- `npx jest --testPathPattern="chat"` — 678/679 passing. The one
  failure (`AtlasDraftCard.test.tsx`, a `/atlas/...` vs `/you/atlas/...`
  route-prefix mismatch) touches files this change never modified and
  is pre-existing, from the concurrent IA/routing work in the shared
  tree — confirmed via `git diff --stat` showing zero changes to that
  test or its component.
- `npx jest serifFloorContract` — 3/3 passing, baseline counts
  untouched (the new variant is sans, not serif).
- **Live-rendered** on the actual dev server (existing `localhost:8081`
  instance) in a real 1:1 thread ("Porto" trip chat): read computed
  `lineHeight` directly off the DOM for both a user turn ("What should
  we do tonight?", "Perfect 🙏") and an assistant turn ("There's a fado
  spot…", "Fado's booked…") — both report **15px / 22px**, confirming
  the fix in the running app, not just in source.

**Risk realized:** none. **Rollback:** revert the four edits; the new
variant is additive and inert if unused.

---

## Landing 2 — the body role — ✅ SHIPPED 2026-07-28

**Change.** Bumped **both** registries that carry the name
`chatTranscript` together:

- `constants/typography.ts:412` — `chatTranscript` **15/22 → 16/26**
- `constants/textVariants.ts` — the `chatTranscript` variant added in
  Landing 1, same bump

(1.63, inside the ~1.6 band recommended for long-form; the prior 1.47
was under the 1.5 floor.)

**Propagation.** `typography.chatTranscript` is referenced in exactly
three files (`markdownTheme.ts:143-154`, feeding `productiveProse()`
for the `private`/`group`/`bubble` markdown variants;
`MarkdownRenderBoundary.tsx:10-12`, the error fallback for the same
three; and its own definition). `textVariants.chatTranscript` has
exactly one consumer: `MessageBubble.tsx:181`. Four call sites total —
the whole surface, and all four moved together in one commit.

**Left `compact` alone**, as planned — it's the deliberately-quieter
preview register (`GroupVesperNote` collapsed state,
`MessageLongPressPreview`), untouched.

**Verified:**
- `npm run typecheck` — clean.
- `npx jest --testPathPattern="chat"` — 678/679, identical result to
  Landing 1 (same pre-existing, unrelated `AtlasDraftCard` route
  failure; nothing new broke from the size bump).
- Grepped `__tests__` for any hardcoded `chatTranscript` numbers before
  changing them — none exist, so no test needed updating.
- **Device verification, on the live app, not a snapshot:**
  1. **Streaming.** Sent a real message into the mock-backed 1:1 thread
     and watched a live streamed reply grow across two lines. Settled
     cleanly — no scroll-jump, no layout break at the tail. Read the
     settled reply's computed style directly: **16px/26px**, matching.
  2. **One-line bubble padding.** Checked the one-line user turns
     ("Perfect 🙏") at the new leading: 26px text + 8px top/bottom
     padding = 42px bubble, identical proportions to same-shaped turns
     before the change. Does not read as over-padded; no padding
     change needed.
  3. **Dynamic Type** — not exercised (would need a native simulator,
     not the web preview). Flagged as a residual check before this
     ships to a device build; low risk since the change only raises a
     base size RN's scaling multiplies against, it doesn't change the
     scaling policy itself.

**Risk realized:** none on the two checks that could be done in this
environment. **Rollback:** revert the two constants.

---

## Landing 3 — the signature — ✅ SHIPPED 2026-07-28

### 3a · Added the signature scale

`type Scale` in `components/brand/VesperSignature.tsx` extended from
`'eyebrow' | 'byline'` to `'eyebrow' | 'byline' | 'signature'`. The new
branch renders the label as `VText variant="serifBody"` (serif 15/22 —
exactly at the floor) in `signatureColor`, with a doc comment on the
branch spelling out the B1 constraint explicitly: *never italic —
production is Roman-first and no italic face is registered; never use
`signature` to label a human, that's what `byline` is for.* The
plus-mark sizing condition (`styles.plusByline`) was widened from
`scale === 'byline'` to `scale !== 'eyebrow'` so the mark sizes
correctly for the new scale too, and `labelSignature: { flexShrink: 1 }`
was added alongside the existing `labelByline`.

`scale='byline'` was **not** touched, as planned (B2): `DiscoverAtoms`
and `GroupMemberAskingBanner` still get their original sans-12
rendering unchanged.

**The suffix branch needed one small extension beyond the original
plan**, not zero changes: the condition gating the addressee
(`to`/`suffix`) render was `scale === 'byline' ? (...)` and had to
widen to `scale === 'byline' || scale === 'signature'` so "to the
group" renders for the new scale too. Once gated in, it renders exactly
as planned — `VText variant="caption"` at `colors.surface.mute`, sans
12 muted — with zero changes to that branch's contents.

### 3b · Chat call sites

Landed exactly as planned, plus one wrapper change the plan didn't
anticipate:

- `components/brand/VesperAttribution.tsx` — added `scale?: 'eyebrow' |
  'signature'` to its props (defaulted to `'eyebrow'`), passed through
  to `VesperSignature`. Needed because `VesperAttribution`, not
  `VesperSignature` directly, is what the chat call sites use — the
  original plan's table pointed at `VesperSignature` props that the
  wrapper didn't yet expose. The `'eyebrow'` default leaves the two
  untouched callers (`MessageLongPressPreview.tsx`,
  `app/dev/trip-creation-card.tsx`) behaviorally identical with zero
  edits to either file.
- `components/chat/PrivateVesperNote.tsx:119` — `<VesperAttribution
  rule />` → `<VesperAttribution scale="signature" />`.
- `components/chat/group/GroupVesperNote.tsx:135` (the exported
  `AttributionLine`) — `<VesperAttribution to={...} time={time} />` →
  `<VesperAttribution to={...} time={time} scale="signature" />`.

### 3c · The CI constraint

`serifFloorContract` stays green, **3/3, baselines untouched** — the
new scale renders at exactly 15px, on the floor, not under it.

**Verified:**
- `npm run typecheck` — clean.
- `npx jest --testPathPattern="chat"` — 678/679, same pre-existing
  `AtlasDraftCard` route-prefix failure as Landings 1–2, nothing new.
- **Full unscoped `npx jest` run** (not just the chat filter) surfaced
  one real regression: `markdownTheme.test.ts` had a test asserting
  `chatTranscript` as hardcoded `15`/`22` literals — stale since
  Landing 2's 16/26 bump, but invisible to the chat-path filter because
  the file lives under `__tests__/components/markdown/`, not a path
  containing "chat". Fixed by rewriting the test to destructure
  `const { fontSize, lineHeight } = typography.chatTranscript` and
  assert against those instead of literals, so it can't silently drift
  out of sync with the source constant again. Re-ran the full suite
  and diffed the two failure lists (`comm -3` on sorted output): exactly
  one suite moved FAIL → PASS, nothing else changed. The remaining 18
  failures are pre-existing, confirmed by sampling their actual error
  messages (not just filenames) to be entirely about header/chrome
  allowlist contracts and the concurrent session's `/you/`-prefixed
  route rename — nothing overlapping this change's files.
- **Live-rendered on the actual dev server**, both rooms:
  - **1:1 thread** ("Porto"): read computed style off the "Vesper"
    label directly — `fontFamily: EBGaramond_400Regular`, `fontSize:
    15px`, `fontStyle: normal`, confirming serif/Roman/on-floor, not
    italic, in the running app.
  - **Group thread** (same "Porto" trip, 3 travelers): the attribution
    line renders `+ Vesper to the group`. Read both text nodes'
    computed style — "Vesper" identical to the 1:1 case
    (EBGaramond_400Regular / 15px / normal); "to the group" renders
    `system-ui` (sans) / `12px` / `normal`, muted grey — confirming the
    addressee stays sans-12-muted exactly as planned, distinct from the
    signature.
  - No hairline rule visible under either signature, confirming the
    `rule` drop in `PrivateVesperNote.tsx` took effect.

**Risk realized:** the one caught above (stale test), fixed. No
regression reached the running app. **Rollback:** revert the four
source edits; the new scale and prop are additive and inert if unused.

---

## Landing 4 — the mark's micro cut — ✅ SHIPPED 2026-07-28

**Brand geometry, not chat. Landed as its own review** — the waist
value was chosen by rendering candidates at true attribution scale and
having the founder pick, rather than the plan author guessing.

**What shipped:**
1. `constants/brand/vesperMarkGeometry.ts` — the stale header comment
   ("the active geometry deliberately remains the existing two-point
   spark") corrected to describe reality (`guidingStar` is active;
   `twoPointSpark` is retained only so older artwork can render it
   explicitly).
2. `guidingStar.micro`'s waist widened from **1.4 → 2.2** units on the
   12-unit box (path `M6 0.5 L7.1 4.9 L11.5 6 L7.1 7.1 L6 11.5 L4.9 7.1
   L0.5 6 L4.9 4.9 Z`). **`master` is untouched** — still waist 1.4,
   confirmed byte-identical to before this change.

**How the value was chosen — not by this plan.** The design page's
fattened cut (waist 2.6) was explicit evidence the slot was worth
filling, not a proposed mark, so it wasn't shipped as-is. Instead: five
candidates (waist 1.4/1.8/2.2/2.6/3.0, `master`'s silhouette otherwise
identical) were rendered as an artifact at three scales — true 12px
attribution size, in context next to the "Vesper" label, and zoomed 8×
for silhouette inspection. The founder picked **C (2.2)** — the
moderate option, steadier than the original without departing far from
the silhouette.

**Verified:**
- `npm run typecheck` — clean.
- `npx jest --testPathPattern="vesperMark|VesperSignature|VesperAttribution|serifFloorContract|brand"`
  — 5/5 passing. `vesperMarkGeometry.test.ts` asserts structure
  (viewBox, path count, registry resolution) rather than exact path
  strings, so it needed no update for the new waist value.
- **Full unscoped `npx jest`** — 18 suites / 31 tests failing, an exact
  match to the pre-existing baseline established while verifying
  Landing 3 (header/chrome allowlist contracts and the concurrent
  session's `/you/`-prefixed route rename). None touch
  `brand/`, `VesperSignature`, or `VesperAttribution` — confirmed by
  filename. Zero new failures from this change.
- **Live-rendered** on the actual dev server, in the same "Porto" group
  thread used for Landing 3: read the rendered `<path d>` directly off
  the DOM for both on-screen instances of the mark (header avatar and
  attribution mark) — both report the new waist-2.2 path string
  verbatim, confirming the running app, not just the source, changed.
- **`master` untouched** — confirmed by diffing the file: the
  `guidingStar.master` path string is byte-identical to what it was
  before this edit. (Real screens that render `master` — the
  onboarding splash at `size=30` and the voice-assistant orb at
  `size=24`/`opticalSize="master"` — were identified but not
  screenshotted; the source-level guarantee that only the `micro`
  object's `d` string changed was treated as sufficient given `VesperGlyph`
  reads `master`/`micro` as two disjoint object keys, not a shared
  computation.)

**Risk realized:** none. **Rollback:** revert the waist value back to
1.4; the comment fix is independent and can stay either way.

---

## E vs E′ — ✅ DECIDED + SHIPPED 2026-07-28 — quiet tint (E′)

The user's own turn: dark pill (**E**) or quiet tint (**E′**). Both use
identical type, so this was purely a container decision, made after all
four landings above.

Decided in the **group room**, per the plan's own instruction — not the
1:1. With Priya, Dana and Sam on screen, the dark ink-fill pill made the
user's own turn the loudest object in a room where it usually isn't;
E′ puts it visually level with the other members' bubbles while
alignment (flex-end) still marks which turn is yours.

**What shipped**, both in `components/chat/MessageBubble.tsx` — one
shared branch, so this reads identically in the 1:1 and every group
thread, exactly like Landing 1's fix:
1. `styles.bubbleSelf.backgroundColor`: `colors.surface.ink` (solid dark
   fill) → `colors.tint.gold` (soft warm wash, an existing token already
   used for highlighted rows in `BookingOfferRow.tsx` and the trip
   memory screen — not a new color introduced for this).
2. The user-text color ternary (`isSelf ? colors.surface.paper :
   colors.surface.ink`) collapsed to a single `colors.surface.ink` —
   once both bubbles sit on light tints, both need dark ink text, so the
   conditional itself was dead weight. This is the concrete form of the
   rule stated earlier in this doc: *identity comes from the container,
   never from type.*
3. Corner radius (`borderRadius: 18`, uniform, no tail) is **unchanged**
   — the decision was about fill and text color only, not shape.

**Verified:**
- `npm run typecheck` — clean.
- `npx jest --testPathPattern="MessageBubble"` — 13/13 passing, no test
  asserted the old ink-fill/paper-text styling.
- **Live-rendered** in the same "Porto" group thread used for Landings
  3–4: read the self-turn bubble's computed style directly off the DOM
  — background `rgba(176, 133, 58, 0.12)` (exactly `colors.tint.gold` —
  gold60 at 12%), text `rgb(27, 23, 20)` (exactly `colors.surface.ink`),
  `borderRadius: 18px` confirming the shape held. Visually level with
  Sarah's and Mike's bubbles, distinguished by a warm-vs-neutral tint
  rather than by weight.

**Risk realized:** none. **Rollback:** revert `bubbleSelf.backgroundColor`
to `colors.surface.ink` and restore the text-color ternary.

---

## Sequencing

1. **Landing 1** — ✅ shipped 2026-07-28.
2. **Landing 2** — ✅ shipped 2026-07-28. Dynamic Type still unexercised
   (needs a native simulator — B3, still open).
3. **Landing 3** — ✅ shipped 2026-07-28.
4. **Landing 4** — ✅ shipped 2026-07-28.

**All four landings are shipped. Remaining before this doc can be
retired:** update the typography and attribution sections of
`travel-app/docs/surfaces/vesper-chat/contract.md` — that doc describes
shipped behaviour, and now this is. B3 (Dynamic Type / font-scaling
policy) still needs a native-simulator pass. E vs E′ (below) is still
undecided.

**Before any of it:** decide whether B1's italic correction should also
be applied to the trips-home spec, which currently specifies serif
italic in three places.

---

## References

- Claude Design → Vesper → **"Vesper Chat - Type Fork.html"** — the
  decision board: four 1:1 treatments, three group rooms, eight
  signatures, the mark ramp, the leading board, the practice board.
- `travel-app/docs/surfaces/vesper-chat/contract.md` — the 07-22
  all-sans decision this extends rather than reverses.
- Commits `7963b089`, `8ea41c27` (2026-07-22) — the unification;
  `48d5d06d` — the wave-5 migration that introduced the leading bug.
- `constants/fonts.ts` — Roman-first policy, the 15px serif floor, the
  17px italic floor.
- `__tests__/conventions/serifFloorContract.test.ts` — the ratchet.
- `docs/working/trips-home-promotion-model-2026-07-27.md` — the other
  spec affected by B1.
