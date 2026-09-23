---
doc_type: working
status: active
owner: founder / multiplayer design
created: 2026-09-20
last_verified: 2026-09-22
expires: 2026-10-20
why_new: Records how to reproduce the dated Multiplayer Shapes boards and their generator inputs without treating exploratory canvases as product decisions.
supersedes: []
source_of_truth_for: []
---

# Vesper — Multiplayer Shapes (brainstorm, Pass A and Pass A′)

Generators for Claude Design project `caf916f9-c0ce-466b-92ee-49ebefe1ca38`.
Brief: [Multiplayer product-shapes exploration](../../claude-design-multiplayer-product-shapes-exploration-2026-09-20.md),
originally written in an isolated lane.

- `mp_common.py` — board grammar. `HP` points at a local copy of the shared board kit;
  copy `docs/working/design-gen/social/hp/` next to these files before running.
- `gen_00.py`, `gen_d1.py` … `gen_d10.py` — Pass A, one board each. Run from the directory holding `hp/`.
- `mp_kit2.py`, `gen_e1.py` … `gen_e8.py` — Pass A′, the eight further directions, each held to the private-context test. `line()` is a row with no chevron, for descriptive lines that go nowhere.
- Corpus reading behind Pass A′: `docs/working/multiplayer-corpus-digest-2026-09-20/`.
- `measure.mjs` — two-pass ink measurement + overflow + unresolved-import check, run against the
  live project's serve URL (dc-import needs HTTP; file:// renders empty placeholders).
- `heights.json` — measured min-heights consumed by `hh()`.

Design language: components copied from workbench `c13ae951` at **vdl-stage1 0.4.1**
(OriginalReader, InviteCard, Notice, Ticket, PlaceHead, FactPair, SourceList, ActionGroup,
LocationFooter, PlaceIdentity + vdl.css + the kernel styles.css copy). Adoption is by copy,
not live sync. The workbench's newer **S2** library is deliberately NOT consumed: it is
undeclared in `vdl-package.json` and belongs to another lane.

At the time of this generator snapshot, Pass B (compare and simplify) and Pass C
(one coherent composition + a remote experience that never becomes a gathering)
were not done. The later [exploration response](../../multiplayer-shapes-exploration-response-2026-09-21.md)
records the delivered boards; this README is only reproduction guidance.

## Layout of the project (2026-09-21 cleanup)

`python3 build_all.py` generates everything and lays `out/` out the way the project is organized:

- top level: `00 - Start here` (the recommendation and the map), `01 - Decisions` (ten open decisions with a RULED line each), `02 - Six interactions` (`gen_b1.py`), `03 - One weekend and a return` (`gen_w1.py`), `04 - Far apart` (`gen_w2.py`)
- `directions/`: D1–D10, E1–E8
- `archive/`: `C1 - Copy before and after`, `A0 - Method and coverage` (`gen_a0.py`, the old index's analysis)

The runtime fetches components from the board's own folder (`COMPONENT_DIR = "."` in support.js), so `support.js`, `vdl.css`, `_ds/` and the five used components (OriginalReader, InviteCard, Notice, FactPair, SourceList) exist at the top level AND inside each folder. `gen_r1.py` is no longer a board: `gen_00.py` imports its tables. `paths.json` maps board keys to project paths for `measure.mjs`.

## 2026-09-21 revision (brief §§11–14, one assignment)

Response: lane copy of `multiplayer-shapes-exploration-response-2026-09-21.md` §12 (the main-workspace copy lacks §§11–12; reconcile before landing).

- `03` is now `An ordinary week between friends` (`gen_w1.py`); new `05 - One gathering different participation` (`gen_g5.py`) and `06 - Something that continues` (`gen_g6.py`).
- `repatch.py` — `apply(fname, new_funcs, offscreen)` swaps a direction generator's frame functions in place; how the twelve revised D/E boards were corrected.
- `gen_c1_frozen.py` + `frozen/copy/*.png` — C1's BEFORE column is images saved at the time. Never regenerate C1 from `gen_c1.py`: the frame functions it calls have since been rewritten, so its "before" silently becomes "after".
- `gen_r1.py` is tables only (imported by `gen_00.py`, `gen_a0.py`); it no longer emits a board.
- `build_all.py` rewrites `out/heights.json`; keep a copy of the measured file and restore it after each build.
- `copy_lint.py` — in-phone text classifier and lint; must end clean.
- playwright-core is loaded from the npx cache path inside the `.mjs` files; repoint if that cache is cleared.
- The serve token is never written to this folder.

## 2026-09-21 (evening) — started over from sharing: board `10 - Sharing` (`gen_s1.py`)

Founder reset: sharing first. Three shares side by side (words + picture · a gathering invitation · where I'll be, with the ticket), each written / received / as the sender sees it; then the quote into a chat with a person. One like, comment, quote. `Ticket.dc.html` copied from the Life project (`e72a2fd2`, admission mode); `InviteCard` is the Social 03 / Plans 04 card. Boards 00–06 are the earlier exploration and are not the current direction.
- `11 - Audience Keep ask link withdraw` (`gen_s2.py`, imports `gen_s1`): the audience picker (friends / a named group / one person; a group is an audience, not a chat), Keep as the fourth verb, an ask, a link, and taking a share back. Board 10 gained Keep and a three-picture grid at the same time.
- `12 - Passing on outside groups withdrawal` (`gen_s3.py`): the four edges with proposed rules — passing on (the thing travels in your words; the author's words only with the author's one-tap yes), a page not an app for people without Vesper, forward-only group membership, no private copies after withdrawal but your own note stays.

## 2026-09-21 — cleanup: the project is boards 10, 11, 12

Founder: "10, 11, 12 is where it's at… the foundation for social multiplayer." Root now holds only `10 - Sharing`, `11 - Audience Keep ask link withdraw`, `12 - Passing on outside groups withdrawal` and the components (incl. `Ticket` from Life). Everything earlier (00–06, the eighteen directions, A0, C1) lives under `archive/` and `archive/directions/`. `build_all.py` and `paths.json` reflect this.
- `13 - Between two people` (`gen_s4.py`): the two-person thread with ONE thing at the top (a plan → a list → a method), each moving to Life for both when the next begins; forms only on a yes; Vesper in the thread, to both, only to keep the top thing honest; frame 8 = nothing at the top.
- 2026-09-21 late: founder separated the private chat from the thing two people build. `13 - The chat` (`gen_s4.py`, rewritten) = a private chat, Vesper only as an ASK VESPER door, a one-line card when something the two own changes. `14 - Ours` (`gen_s5.py`) = the list two people own, as a page in Life: cover, title, faces, ledger (places · been · last together), entries in the adder's words with name+date, BEEN as a stated fact with date and who, both people's photos; a year on; sending it (fifth share kind); starting one from a place; the same page for a method and a things-to-do list. "A way better friend streak": nothing counts up, nothing decays, it grows by living.
- 2026-09-21 aesthetic pass over 10–14 (one kit change in `gen_s1.py`, imported by s2–s5): actions are four glyphs (heart, comment, quote, keep) on one quiet footer row with the location on the left, no words or arrows; the composer is `To ▸ audience` pill, words, attachment, one grey location line with ×, and a glyph toolbar (camera, mic, pin, calendar, place; gold = attached) with Send; every attachment card uses the Life ticket's treatment (`CARD_CSS`: paper, soft shadow, no border); explanations moved out of the phones into captions; feed posts separated by hairlines, not "Earlier" heads; pages get `page_bar` (back · label · ···) instead of search/map; your own avatar shows your initial; chat composer = gold spark (Ask Vesper) · field · round send, and Vesper's answer is always marked "asked by"; board 14's cover is a paper map (`paper_map`) and its doors are three soft pills.
- `15 - With Maya` (`gen_s6.py`, 2026-09-21): the thread and Life's "Shared with Maya" (Life project e72a2fd2, board 07) are one object. One page per person, reached from Life's People lens and from Chat: From her (boards 10–12) · Ours (board 14) · Together (Life 07's shared record) · the chat (board 13, a door) · only yours. Frames for this-time-last-year inside the page, "been" offered from the record, Maya's side, and the recommended ownership rule (each Ours entry is its adder's and leaves with them). Four decisions carry RULED — not yet — lines. `text.mjs` reads a served board as text. The Life project was not modified.
- 2026-09-21: `15` redrawn in Life's own grammar. `gen_s6.py` now reads `life/07.html` (Life e72a2fd2 board 07, downloaded verbatim) and uses its stylesheet, board shell, phone chrome, section heads, rows, chat strip and withdrawal wording; board 07's People-lens and opened-record panels are used verbatim with only the new parts inserted (an Ours row and section, her note as a post, a conversations row). Re-download `life/07.html` if Life 07 changes.
- `16 - With and deciding together` (`gen_s8.py`, 2026-09-21). WITH: a people icon in the composer names who you were with; the tagged person is asked once on Home ("I was there" / "Not me"); their name reaches your audience and the moment reaches their shared record only after a yes; a no is silent; either can remove it later; a line under the words, never a face tag. DECIDING TOGETHER: an options icon adds 2–3 options; everyone asked picks any that work and sees who picked what; "can't" goes to the host alone; the host decides in one tap and it becomes an invitation where those who picked it are already in. No group chat (ruled out 2026-09-21). The composer toolbar (`gen_s1.toolbar`) gained the two icons on every board. The Life frame reuses `gen_s6`'s Life helpers with Life 07's stylesheet injected into the board head.

## 2026-09-22 — threads and Life continuity handoff

Handoff: `docs/working/claude-design-multiplayer-threads-life-continuity-handoff-2026-09-22.md`; handback: `docs/working/multiplayer-threads-life-continuity-response-2026-09-22.md`.
- `16 - Getting together and with` (`gen_s8.py`, replaces `16 - With and deciding together`): voting demoted to an optional instrument; gathering = opening → replies → author settles → invitation; availability never becomes attendance (one exception: an explicit conditional commitment); "With" split into co-presence / visible association / entry into the shared record; presence as a bounded sentence that goes stale.
- `17 - Kept things` (`gen_s9.py`): personal collection from one item; possibilities vs supported history with a correction; private exploration selectively shared; small circle with uneven contributions, replies on the material, quiet, and later use.
Both inject Life 07's stylesheet (via `gen_s6.PREFIX`) so Life-grammar frames can sit on a kit board.
- `18 - The container` (`gen_s10.py`, 2026-09-22): the component board for anything people keep together. Cover composed from contents (map / mosaic / 2×2 of latest plates / title-on-paper for words only); one item grammar plate · words · name·date with the plate varying by kind (photo wide or 2-up, place row, link card, typographic plate for words, typed originals unchanged); rhythm from kinds with month hairlines; private = shared except faces/initials; one + and ···; list·map toggle only when there are places. Frames: empty, one, three mixed, twelve shared, words only, places private, places shared, map; plus plate sheet and cover rules.
- 2026-09-22 (later): the container settled in **Life's grammar**. `18 - The container` is now `gen_s12.py` (masthead → sections with counts: the things as riso-thumb rows, the drawer of wristbands/chips/tickets, the contact sheet, conversation, people, places, sources, one voice line). Board 17's Life and Places pages were rebuilt on it (`gen_s9.py` imports `gen_s12`). The card-based `18` and the `18b` colour-field version are retired to `archive/` on the project; their generators (`gen_s10.py`, `gen_s11.py`) are removed. `life/03.html` and `life/04.html` are the downloaded Life sources the grammar is lifted from.
- `19 - The container over time` (`gen_s13.py`, 2026-09-22): board 18's grammar and parts read as a timeline. One spine (mono dates left, hairline, a dot per thing), seasons as section heads with counts, each thing in its own form (small riso strip, wristband, ticket row, a friend's words, place with been), hollow dot + gold NOW line for what is ahead, gold dot for an open question, quiet stretches as dashed spine with one italic line. A BY KIND · OVER TIME switch in Life's lens-chip style under the masthead. Frames: Our New York, Nights out, Getting pasta right, quiet then back, one night kept on its own (times on the spine), and board 18's by-kind page for comparison.

## 2026-09-22 — cleanup to eight boards

Founder approved: board `14 - Ours` deleted (superseded by 15, 17, 18, 19); board `12` merged into `11` as its last row and rules (`gen_s2.py` imports `gen_s3.forward/by_link`); board 17 trimmed of three frames that duplicated 18 (Interesting stuff, the private pasta page, Our New York); unused top-level components FactPair, InviteCard, Notice, OriginalReader and SourceList deleted (the archive keeps its own copies); the retired card-based 18 and 18b deleted from `archive/`. Top level is now 10, 11, 13, 15, 16, 17, 18, 19 plus `Ticket`. `gen_s3.py` and `gen_s5.py` stay only as helper modules (imported by 11, 15 and 17); `build_all.py` no longer builds 12 or 14.
- `20 - Connecting` (`gen_s14.py`) and `21 - Receiving` (`gen_s15.py`), 2026-09-22. Connecting: invite by sending a real thing; the link page is enough to read and reply; joining connects you to the person and the thing; contacts asked once and only mutual-number matches; the only other suggestion is someone you were with, on the occasion's page; ignoring and stopping sharing are silent. Receiving: Home over a week — to you first, then things with a time (gone when it passes), then friends' shares compact, one row per person, capped, the rest behind a door; no counts; nothing piles up (the week lives in Life under each person); a quiet day says so; see less of someone is private and temporary.

## 2026-09-22 — Life skin across the project

`mp_kit2.py` now ends with a "Life skin" that every generator picks up through the kit: Life 07's stylesheet injected into the board head, the taupe board (`#D8D1C5`), Life's board header (eye, Review pill, serif title, note), a gold mono caption and serif title above each frame with the explanatory note moved below it, rounded `.cphone` frames around every kit phone and link page, riso placeholders (Life's six motifs) replacing the old figure illustrations in `illo`/`thumb`, and tag pills pruned to the ones that add information (NO APP, PROPOSED). It patches `gen_generous`, `gen_merge` and `gen_p2_common` in place, so the change is one block. `over.mjs` renders small whole-board snapshots for a project-level look.

To reproduce: copy `../social/hp/` to `hp/`, then run `python3 build_all.py` and `python3 copy_lint.py` from this folder. `out/` and the local `hp/` copy are ignored by Git. For overview screenshots, serve `out/` as a Claude Design project and run `over.mjs` with the serve base URL and quoted board names. Set `PLAYWRIGHT_CORE_MODULE` to a local `playwright-core` module path if it is not installed normally, `CHROME_EXECUTABLE` if the browser is not bundled, and `DESIGN_TOKEN` to the serve query string if required. Screenshots go to ignored `out/shots/`; never save a serve token in the repository.
