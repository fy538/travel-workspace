# Vesper Design Canon — Session K1-R: Dedupe Remainder (2026-07-06)

Scope: the three K1 items honestly deferred as OPEN, now with the expensive verification PRE-DONE outside the session — every list below is verified against the live bundle; execute without re-deriving. Three items. K2 follows as the final session.

---

## 1. Dead-export purge — pre-verified kill list, zero live mounts each

All 30 names below were verified to have ZERO JSX mounts across every live jsx + html in the bundle. Remove each from its file's `Object.assign(window, …)` AND delete the component body (unless a body is referenced by a live component in the same file — none were found, but the console check below catches any miss):

- trip-document-canon.jsx: HeroV1, HeroV2, HeroV3, HeroV4, HeroV5, HeroAir, TwoTierDoc, DocAes, DeckClear, DeckDoc
- vesper-shared.jsx: VesperQuote, VES
- trips-shared.jsx: StarterChip, StarterGlyphs
- discover-kit.jsx: DossierBar, FieldEyebrow, VesperBy
- changes-kit.jsx: DelegationAnnotated
- onboarding-canon-seams.jsx: SeamForming
- onboarding-kit.jsx: ChatTop, UserSaid, PLast
- vesper-home-history.jsx: HistoryBoard · vesper-rail-variants.jsx: RailEdge, RailScene, RailBare (KEEP HistCombo, HistPhone, RailRow — live)
- Wherever defined: FoundRow, DevStrip, IllustratedRead, PlacePortrait
- KEEP: HomeLoading (deliberate unmounted rescue).
- Delete the two orphaned files: places-kit.jsx, places-composed.jsx (loaded by no page).
After the purge: open every touched page once and confirm console-clean (the K1 rename pass set this precedent — repeat it).

## 2. Invite-landing merge — structural diff pre-computed

The two ScreenInviteLanding versions (auth-invite-app 4.2k chars vs people-collab-app 2.7k) differ in exactly two meaningful ways:
- **Hero treatment:** auth uses AvatarCluster + PrimaryButton/GhostButton ("Join Lisbon"); people uses AvStack + **TripReceiptArtifact** (the trip rendered as a receipt artifact).
- **Escape hatch:** people has "Not now — set up Vesper" (a non-joining exit into onboarding); auth has none.
Auth & Invite owns the canonical screen. Merge decision to make (and record): which hero treatment wins — recommend **adopting people's TripReceiptArtifact into the auth version** (it's the more Vesper-flavored artifact and matches the receipt grammar elsewhere), and **keep the "Not now" escape** (a recipient who won't join is still a prospect — this is the wedge's consolation path). Then people-collab's copy becomes `ScreenInviteLandingRef` with the pointer caption.

## 3. Duplicate screen ownership — the *Ref treatment (the one real design task)

Per the recorded ruling: Chat owns ScreenGroupRoom / ScreenPrivateThread / GroupDecisionCard / GroupEventLine / MemberBubble; Places owns ScreenVenueDetail; Discover Detail owns ScreenDossier. In each NON-owner file (people-collab-app for the chat set; whichever of places-canon/discover-detail is the non-owner per screen):
- Rename the non-owner's components with the `Ref` suffix.
- Give each Ref artboard the one-line pointer caption: "Reference render — canonical version lives on [page]."
- Where the non-owner's rendition has visibly drifted from the owner's, do NOT reconcile the pixels — the caption plus the rename is the fix; the owner's version is simply true.
- People & Collab keeps its group-room frame for the privacy-seam narrative; Places keeps its dossier-read frame for the lens story — context stays, ownership becomes unambiguous at the definition site.

## Definition of done

Zero dead exports beyond HomeLoading + the named keeps · places-kit/places-composed gone · one canonical invite landing (with recorded hero + escape decisions) + Ref copy · all duplicate screens carry Ref names + captions in non-owner files · touched pages console-clean · honest OPEN row for anything skipped · export.
