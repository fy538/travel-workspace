---
doc_type: working
status: active
owner: frontend / backend
created: 2026-07-28
expires: 2026-08-27
why_new: The workbench spec establishes the thread row but specifies no screen. History is the first build of that row — it needs none of the workbench's unresolved decisions — and no doc carries its edit surface, wire mapping, or landing sequence.
promotes_to: travel-app/docs/surfaces/vesper-home/contract.md (History section) plus a conversation-list API note
supersedes: []
source_of_truth_for:
  - vesper-history-implementation-plan
  - conversation-list-item-serializer-cut
---

# Vesper History — implementation plan

> Five landings, smallest first, each shippable alone. Design source:
> **Claude Design → Vesper → "Vesper Home - History.html"** (+
> `vesper-history.jsx`). Model: `vesper-home-workbench-2026-07-28.md`.
>
> **Read §0 first.** Verifying the design against the code found one
> prerequisite and two live bugs, one of which is unrelated to this work
> and will bite whoever touches the file next.

## Why this screen first

The workbench page has two unresolved dependencies — the Deck's
destination and the hero's grounding. **History has neither.** Every field
the row needs is on the wire today except two, which are a ~3-hour
serializer add. And it is broken in exactly the ways the row fixes.

It is also the first time any of this design would be **seen on a
device**. Nothing in the workbench has been. The one screenshot taken
during its design found two defects the code had not shown.

---

## §0 — Found while verifying (read before anything)

### P1 · `data/conversations.ts` has two duplicate map bodies

`useConversationHistory` maps inline (`:186-218`); `mapRawToSessions`
does the identical job (`:223-250`). **Editing one silently diverges the
hooks.** Every landing below touches this mapping.

**Do this first, as its own commit:** collapse to one function. It is a
prerequisite, not a cleanup — otherwise landing 1 lands half-applied and
the bug is invisible until someone opens the other entry point.

### P2 · `trip_title` is populated from the wrong field — pre-existing bug

`data/conversations.ts:237` sets `trip_title: c.title` — the
**conversation's** own title, not the trip's. The trip name that actually
renders is resolved client-side from `TripContext`
(`history.tsx:149-167`), so the bug is currently masked.

Unrelated to this work. Flagging because the row's kicker comes from trip
identity and the next person to reach for `trip_title` will get a
conversation title. Either fix it or delete the field.

### P3 · The untitled branch is dead code

`history.tsx:368-370` has a muted "New conversation" branch for untitled
threads. It can never fire: `mapRawToSessions:238` already coerces
`title ?? 'Conversation'`, so `null` never reaches the UI.

This matters for the row. `title` is a fire-and-forget Haiku call after
the first turn, so there **is** a real window where a thread has no title
— the design draws it ("Untitled — before the Haiku call lands"). To
render that honestly the coercion has to move: let `null` through and let
the row decide.

---

## The row — build values

Design: `vesper-history.jsx` → `HRow`. This is the **canonical**
definition; `vesper-workbench.jsx`'s `Row` should adopt it. One row, two
screens.

```
line 1   mono kicker · · · · · · · · · · mono stamp
line 2   TITLE, full width, up to two lines
line 3   state sentence · · · · · · · · · company
                                          └ chevron, centred right
```

| Element | Value |
|---|---|
| container | `padding: 14px 0`, `borderTop: 0.5px hairThin` (not on first) |
| kicker | mono 8 · ls 1.5 · `inkBody` · uppercase. Absent → `not in a trip` in `muteSoft` |
| stamp | mono 8.5 · ls 0.8 · `mute`. Replaced by `waiting` (inkBody) or gold pulse + `running` |
| unread dot | 6×6 · radius full · `gold` · precedes the title |
| title | sans 15 · weight 500 (**600 when unread**) · ls −0.2 · lh 1.28 · **2-line clamp** |
| state | sans 12.5 · `inkBody` · lh 1.4 · nowrap + ellipsis |
| facepile | 19×19 · overlap **−8** · ring `paper20` · sans 600 |
| group mark | two blanks, `paper30` + `paper40`, overlap −8 |
| chevron | 11px · `rgba(27,23,20,0.28)` · stroke 2.2 |

**Scope is the kicker and only the kicker.** No plate, no second material.
An earlier draft encoded it twice; at list scale that reads as two
components rather than as meaning.

**The chevron is a flex sibling of the whole three-line block** — it costs
~20px once, not per line. The first draft used a right-hand *rail*
stacking facepile + state word + chevron, which squeezed titles to about
twenty-four characters. That distinction is the entire reflow.

**Adopted from Trips.** The kicker sizing, the −8 overlap and the soft
chevron all match `trips-home-row-studies.jsx`. The three-line count is a
deliberate fork: a Trips queue row carries one *fact*; a Vesper row
carries a *name* and a *state*.

**No serif anywhere.** Two live traps — italic is unimplementable (no face
bundled; the constants forbid synthesizing slant) and **serif below 15px
fails the CI ratchet**. A list row has no reading moment.

---

## Wire → row

| Field | Drives | Status |
|---|---|---|
| `trip_id` | the kicker (via `TripContext` lookup) | free |
| `title` | the title | free — but see P3 |
| `last_message_preview` / `_sender` | the state line | free |
| `last_message_at` | the stamp | free |
| `unread_count` | the gold dot + weight step | free |
| `conversation_type` | the group mark | free |
| `intent_state.phase` | richer state line | **the cut** |
| `intent_state.current_goal` | the state line, properly | **the cut** |
| `session_status` | "still open" sectioning | **the cut** |
| `participants[].name` / avatar | the named facepile | deferred |
| `agent_workflows` busy | the gold pulse + `running` | deferred |

**The facepile degrades honestly.** `ParticipantResponse` is
`{user_id, role, joined_at}` — no display name, no avatar. So a group can
be **marked** today but not **peopled**. Two blank overlapped seats say
"more than you" without inventing a roster.

---

## The serializer cut — ~3 hours

**Verified 2026-07-28: this is free at the database layer.**
`get_conversation_list_for_user` delegates to `get_conversations_for_user`
(`_crud.py:103-144`), which does `select(conversations)` — the **whole
table**. So `intent_state` (JSONB, same row, `NOT NULL DEFAULT '{}'`),
`session_status` and `last_active_at` are **already read off disk and
already hydrated** into the `Conversation` model. No query change, no
migration, no plan change.

Both enums are already CHECK-constrained in Postgres —
`session_status IN ('active','idle','closed')` and `intent_state->>'phase'`
pinned to the five values — so they can be typed as literals with the
database guaranteeing it.

### Edit surface

| Site | Change |
|---|---|
| `backend/api/routes/conversations.py:688-698` | add fields to `ConversationListItem` |
| `backend/api/routes/conversations.py:1898-1912` | the route indexes `row["key"]` **explicitly** — every new field needs a line here or it is a `KeyError`, not a `None` |
| `backend/core/db/conversations/_crud.py:337-351` | add keys to the output dict, reading from data already in memory |
| `tests/api/test_conversations_api.py:1326-1345` | `_make_enriched_row()` — **mandatory**, same `KeyError` reason |
| regen | `make export-openapi` → `scripts/project_app_openapi.py` → `npm run generate-api-types:snapshot` |
| `travel-app/types/chat.ts:717-742` | optional fields on `ConversationSession` |
| `travel-app/data/conversations.ts` | the single map body from P1 |
| `travel-app/utils/api/mock/trips.ts` | the `as APIConversationListItem[]` cast means missing fields **will not** fail tsc — silent mock/real drift |

**Project the scalars.** Do not expose raw `intent_state`: it nests
`planning_direction` → `PlanningNextStep[]`, and dumping it across fifty
rows bloats the payload for no benefit.

**Regen works.** Both snapshot checks pass; `ConversationListItem` is
fully generated. The `types.ts:1580` "hand-bridged" comment is scoped to
two types not emitted as named schemas — narrow it while you are there.

**Coverage gap:** there is **no DB-level test of
`get_conversation_list_for_user`** anywhere; existing coverage patches it
out. Landings 1–2 do not care. Anything that changes the *query* would
ship with zero SQL-level coverage.

---

## Landings

### Landing 0 · Collapse the duplicate map bodies
`data/conversations.ts`. No behaviour change. Prerequisite for everything
below.

**Landed 2026-07-28:** app `4ffe418d`.

### Landing 1 · The row, free fields only
Pure frontend. Replace `ThreadHistoryRow` (`history.tsx:468-546`) with
`HRow`. Delivers: the group mark, the unread dot and weight, the trip
kicker as the only scope signal, the soft chevron, and the reflow that
stops titles truncating. **Retires the hardcoded "V" avatar.**

Also move the title coercion out of the mapper (P3) so the untitled window
renders honestly.

Sectioning unchanged in this landing — the existing Active trips /
Standalone / Earlier buckets stay, so the row can be judged on its own.

**Landed 2026-07-28:** app `f74dbafb`.

### Landing 2 · The serializer cut
Backend + regen + mapper, per above. Delivers a real state line
(`current_goal`) and `phase`, and unlocks landing 3's "still open"
section.

**Landed 2026-07-28:** backend `0cda2748`, app `25a862bb`. The generated
contract also carries `session_status` and `last_active_at`; the app
mapper preserves all four scalars.

### Landing 3 · Sectioning — **RULED: A, state first** (2026-07-28)
Replace the trip-date bucketing (`history.tsx:172-218`) with state-first
grouping, using the **composite "open" definition** in the ruling below —
never bare `session_status`.

**Landed 2026-07-28:** app `b9138405`. The two-day recency fallback
backs unread and exploring/drafting state; `session_status` is not an
input. The dormant transition was verified in the re-engagement path
before landing.

### Landing 4 · The remaining states
Empty, loading skeletons in the row's own shape, and the no-results copy
that says what search actually covers. Search itself already exists
(`history.tsx:332-341`, filtering `title` / `trip_title` /
`last_message_preview` at `:132-143`).

**Landed 2026-07-28:** app `27a009d8`.

### Deferred, deliberately
- **Named facepile** — needs display name + avatar on `ParticipantResponse`.
- **The running pulse** — needs the `agent_workflows` flag: no index on
  `conversation_id`, and the real cost is an invalidation channel the list
  does not have. A row claiming "working…" about something that finished
  forty seconds ago is worse than no row. `phase == 'drafting'` is the free
  approximation.
- **Rename / archive sheets** — the behaviour exists
  (`history.tsx:440-458`, `useUpdateConversation:222-292`, optimistic
  `hiddenSessionIds:128`) but is undrawn in any board.

---

## The sectioning ruling — A, state first

> **RATIFIED 2026-07-28 (founder — program queue F4)**, with one binding
> condition found by verifying the recommendation in code.

The comparison, kept for the record:

| | A · State first ✅ | B · Scope first |
|---|---|---|
| Grouping | still open → earlier this week → month | by trip, "Not in a trip" last |
| Needs | the composite open definition below | free today |
| Argues | the surface is about what is still alive | the surface is an archive |
| Cost | — | a thread you were mid-sentence in sits under a trip heading you may not be thinking about |

Three reasons, in strength order: **today's screen is a broken version of
B** (trip-date buckets), and its observed defect — a March thread above
yesterday's live one — is B's structural weakness already seen in the
wild. **Scope-first retrieval already has a home** — the trip page owns
its own chat surface — while state-first has no other home in the
product. And B's one advantage (no serializer dependency) is moot under
the program's sequencing, where the cut (step 1) precedes sectioning
(step 3).

### The binding condition — the composite "open" definition

Verified in code 2026-07-28: **`session_status` is an infrastructure
fact, not a product fact.** `update_session_state` writes `'active'` on
every agent turn (`_crud.py:502-523`); `'closed'` is written only when
the **in-memory server session object is evicted**
(`concierge/session.py:2151-2162`, `_persist_closed_status`); and
**nothing anywhere sets `'idle'`.** Gate "still open" on it naively and
the section balloons toward everything — A degenerates into a recency
list wearing a section header.

Landing 3 must implement:

```
open  :=  waiting (open_questions / pending votes)
       OR unread_count > 0
       OR intent_state.phase ∈ {exploring, drafting}
       OR last_active_at within N days
never :=  session_status alone
```

This degrades sanely even if phase transitions prove patchy — unread and
recency are already reliable. One thing to verify while building: that
`phase = 'dormant'` transitions actually fire; if they never do, the
recency window is carrying the definition and N should be chosen
accordingly.

---

## Acceptance

Judged on a device, not in a mock.

1. **A group thread is legible as a group without tapping it.** Today the
   only difference between a four-person thread and a solo one is what
   happens after the tap.
2. **Unread is visible to eyes, not only to VoiceOver.** Smallest fix on
   the list and the most obviously missing.
3. **A loose thought reads as loose.** The absent kicker has to carry that
   on real titles — precisely what a mock cannot settle.
4. **Titles stop truncating.** Verify against the longest real titles in
   the fixture set, not the board's.
5. **It survives Dynamic Type.** `components/ui/Text.tsx` declares no
   `maxFontSizeMultiplier`, so RN's unbounded default applies. The
   two-line clamp at the largest setting is the case to check.
6. **Nothing reflows when data lands** — which is why the skeleton is the
   row's own shape.

**Accepted on device 2026-07-28:** app fixture/evidence landing
`7f36afe2`; maximum-Dynamic-Type correction `b4b4e745`. Normal and
`accessibility-extra-extra-extra-large` captures plus focused Maestro
results are recorded in
`docs/audits/home-surfaces-step3-2026-07-28/`.

## References

- `docs/working/vesper-home-workbench-2026-07-28.md` — the model
- Claude Design → Vesper → **"Vesper Home - History.html"** + `vesper-history.jsx`
- Claude Design → Vesper → `trips-home-row-studies.jsx` — the shared row spine
- `travel-app/app/(tabs)/concierge/history.tsx` (655) — the screen
- `travel-app/data/conversations.ts` — the mapper, and P1/P2
- `travel-agent/backend/api/routes/conversations.py:677-698, 1898-1912`
- `travel-agent/backend/core/db/conversations/_crud.py:103-144, 337-351`
