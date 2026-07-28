---
doc_type: working
status: active
owner: founder / product / engineering
created: 2026-07-27
expires: 2026-08-26
why_new: No existing document maps the full cross-repo ingestion surface (chat images, screenshots, booking extraction, Atlas photo-scan, place search, uploads) against a single proposed envelope model. Atlas system charter and the notification-attention roadmap each own one piece; this note is the first to compare them as candidate infrastructure for a general "import everything" system.
promotes_to: a `docs/systems/ingestion.md` system charter, plus a decision record on the inbound-item schema and first-slice scope
supersedes: []
source_of_truth_for:
  - unified-ingestion-research-and-recommendation-2026-07
---

# Vesper Unified "Import Everything" System — Research Report

> **Working research, not shipped canon.** Nothing here is implemented. Every
> code claim below was verified against the current repo state on 2026-07-27
> by direct file/line audit; every market/platform claim is cited to an
> official source with dates where available, and inference is labeled as
> such. Where evidence was incomplete, that gap is named rather than filled.

## 1. Executive recommendation

**Vesper already owns most of the hard, back-half infrastructure a unified
ingestion system needs — attention routing, mutation gateways, idempotency,
and privacy-safe composition — and owns almost none of the front-half
capture infrastructure — a real inbound envelope, share-sheet capture, URL
resolution, or a way to create a place that isn't already in the corpus.**
This is not a "build a new subsystem" problem. It is a "build one new
capture‑and‑extraction stage and route its output through four systems that
already exist" problem.

Decisive answers, expanded in the sections below:

1. **Do we already possess most of the infrastructure?** Mostly yes, for
   everything *after* extraction. No, for everything *before* it. Section 2
   and the capability matrix (§3) make this precise: the proposal gateway
   (idempotent preview/commit), the attention/notification type registry,
   the `vesper_action_receipts` ledger, `group_compose`'s privacy gate, and
   the receipt-OCR background-job pattern are all real, load-bearing, and
   directly reusable. What's missing is upstream: no share-extension/inbound
   surface on mobile (confirmed absent, not just unused — §2.10), no URL
   unfurling anywhere in the backend, no booking-email parsing, and no way
   to write a place into the corpus that isn't already catalogued.
2. **What exactly should be consolidated?** Four bespoke, one-off
   attachment patterns (chat images, trip photos, receipts, Atlas artifact
   photos — each its own table, its own FK, its own privacy rule) and two
   divergent extraction styles (synchronous in-turn LLM vision for chat/
   booking vs. an async job-queue with OCR for receipts) should converge on
   one ingestion envelope and one background-extraction job template — the
   receipt-OCR pipeline (`backend/workers/ocr_jobs.py`) is the best existing
   template for the latter.
3. **Do we need a new durable artifact/inbound-item abstraction?** Yes — a
   new `inbound_items` table — but it should **not** reuse `atlas_candidates`
   (that table is private-memory-scoped by design, has no group-visibility
   concept, and has no promotion path to Places, proposals, or the
   itinerary — reusing it would either break Atlas's privacy invariant or
   require bolting group-shaped behavior onto a table whose whole contract
   is "yours alone"). It should, however, **reuse the proven patterns** from
   `atlas_candidates`/`atlas_artifacts`: claim-first atomic approval,
   content-hash dedup, and a strict "review is read-only, only approval
   creates the canonical object" boundary.
4. **Where should uncertain imports appear?** Not a new Inbox tab, not a new
   Trip Room, not a new dashboard. Two existing surfaces, chosen by shape:
   **Places** for place-shaped candidates with no group decision required
   yet (this is exactly what the Places charter and the in-flight
   navigation migration already scope Places to own), and the existing
   **attention/"needs you" system** (`attention_cases` + `TYPE_REGISTRY`) for
   anything that needs a decision — a new `import_review` attention type,
   not a new inbox concept.
5. **How should receipts make this work visible?** Extend the work-receipt
   doc's four-move anatomy (input acknowledged → work done, with reason →
   constraint honored → what's outstanding) using the existing
   `vesper_action_receipts` public/private split and `group_compose` gate —
   but the work-receipt doc has a real gap for imports specifically: it
   never decides durable vs. ephemeral, and an import batch reviewed over
   hours or days needs a durable, revisitable receipt, which today has **zero
   working implementation** (`create_direct_edit_receipt` exists in code
   with zero call sites — confirmed by grep).
6. **What should Vesper build first?** **Share URL/text/screenshot → extract
   places → Places/attention → receipt.** Not booking import, not a unified
   photo-scan rewrite. Reasoning in §10.
7. **Table stakes vs. differentiator:** turning a link or screenshot into a
   place suggestion is now table stakes — it is commoditizing into
   single-purpose apps in real time (Stashed, Plotline, and others, per §4).
   The differentiator is not the capture; it's that an import in Vesper
   would land in the *same* attention, proposal, and receipt machinery as
   every other kind of trip change, instead of a bespoke unfiled-items queue
   (TripIt) or an opaque instant-itinerary (Mindtrip) — plus a two-tier
   privacy model on imported content that no competitor implements in a
   *group* trip context.

## 2. Current-state code map

All paths are absolute repo paths, verified 2026-07-27. Backend repo:
`travel-agent`; mobile repo: `travel-app`.

### 2.1 Chat image/file attachments

- Entry: `backend/api/routes/conversations.py:1209` (`send_message`),
  `:1344` (`send_message_stream`); trip-scoped mirror
  `backend/api/routes/chat.py:281-298,439-458`. `MessageImage` body field
  (not multipart) at `conversations.py:261-306`: base64, max 2.5MB, MIME
  regex-limited to jpeg/png/webp/gif. Mobile side: `components/chat/
  ComposerBar.tsx:294-406` — `expo-image-picker` → lazy base64 via
  `expo-file-system/legacy` → inline in the send payload, max 4 images/msg.
- Storage: `backend/core/db/chat_images.py:63-116` writes to local disk
  (`$CHAT_IMAGE_STORAGE_DIR`, default `/tmp/...`); one row per image in
  `chat_images` (`backend/core/db/_tables/conversations.py:42-77`).
- Extraction: LLM vision, in-turn — the base64 block is forwarded directly
  into Anthropic's message history (`backend/concierge/agent.py:660-673`).
  No deterministic parser.
- Review: none — used immediately in the same turn.
- Canonical object: none automatically; only becomes durable if the LLM
  separately calls a write tool (see §2.3).
- Dedup: none. Failure: best-effort, swallowed
  (`backend/concierge/session.py:1093-1114`, logged and dropped).
- Completion state: silence — no receipt.

### 2.2 Screenshot interpretation

**Not found as a distinct path.** No screenshot-specific route, prompt, or
OCR call exists anywhere in `backend/` (grepped case-insensitively; the only
hits are unrelated docstrings). What exists instead is a generic
post-hoc vision summary, `backend/concierge/vision_summary.py::
summarize_image_for_history()` (lines 73-132) — one Haiku call per uploaded
image, result stored in `messages.metadata_['vision_summary']`, not a
structured table. Failure is swallowed (`vision_summary.py:122-124`).

### 2.3 Booking/confirmation extraction

- Entry: not a route — a **prompt instruction plus tool**.
  `backend/concierge/_prompts_skills.py:1806-1815` instructs the model, on
  seeing a booking/confirmation image, to read it, recite what it extracted
  back to the user for correction, then call `trip_accommodation_set`
  (handler `backend/concierge/tool_handlers/accommodations.py:59+`).
- Storage: `trip_accommodations`
  (`backend/core/db/_tables/users.py:200-284`) — `source` CHECK-constrained
  to `user_stated | booking_confirmed | inferred_from_gps | other`
  (line 284), `confidence` float default 0.8, `visibility` `group|private`.
- Extraction: pure LLM vision read-and-recite, no deterministic parser, no
  background job — synchronous, in-turn, same mechanism as §2.1.
- Review: conversational only — the model is instructed to recite details
  back before writing; not a structured UI approval step. Tool is
  `ToolEffect.COMMIT` with `ConfirmationPolicy.TRIP_EDIT_POLICY`
  (`backend/concierge/tool_contracts.py:241-249`).
- Dedup: none for the vision path; `superseded_by` self-FK exists for manual
  supersession chains only.
- Completion state: conversational reply only; no push/notification.
- **No email or PDF ingestion exists anywhere** — grepped for
  `inbound_email|forward.*email|mailgun|sendgrid.*inbound` across the whole
  backend, zero hits.

### 2.4 URL handling in chat

**Not found.** No link-unfurling, OpenGraph scraping, or URL-to-place
resolution exists for a URL a user pastes into chat. The only OpenGraph
code in the repo is **outbound** (Vesper generating its own share-card meta
tags: `story_landing.py:250-293`, `invite_landing.py:132,245-314`,
`proposal_landing.py:64-89`, `atlas_unpacked_landing.py:90-130`). The only
inbound scraping (`research_agent/tasks/seed_photos.py`,
`media/sources/venue_site.py`) belongs to the **city-onboarding content
pipeline**, not anything a user triggers. `search_web`
(`concierge/tool_handlers/web_search.py`) is agent-initiated factual lookup
and explicitly forbidden from being used for venue recommendations
(comment, lines 10-14) — it is not URL-paste resolution.

### 2.5 Trip-photo scanning — the Atlas candidate → artifact pipeline

This is the deepest existing analog to a general ingestion envelope, and it
matters enough to describe precisely — including where it does **not**
generalize.

**Tables** (`backend/core/db/_tables/atlas.py`):

- `atlas_candidates` (lines 53-142): `date_range_start/end`, `place_guess`,
  `place_count`, `photo_count`, `sample_photo_ids` (JSONB, opaque on-device
  PHAsset ids — **never image bytes**), `confidence` (`high|medium|low`,
  client-declared then server-validated), `candidate_type`
  (`trip|weekend|day_out|place_memory`), `source`
  (`atlas_scan|onboarding_diary`), `status` (`pending|approved|dismissed`),
  `cluster_fingerprint` (FNV-1a over sorted photo ids + date range),
  `artifact_id` (FK, filled on approval). Partial unique index
  `uq_atlas_candidates_user_fingerprint` on `(user_id, cluster_fingerprint)`.
- `atlas_artifacts` (lines 149-262): `source_candidate_id` (not a real FK —
  "Application enforces integrity," line 164-166, but backed by a real
  unique index `uq_atlas_artifacts_source_candidate` at lines 231-233 —
  DB-level exactly-once guarantee), `artifact_type`, `title`,
  `one_line_read`, `sections` (JSONB), `reflection` (user's own words,
  captured at approval), `signal_state`
  (`signals_on|signals_off|shareable` — **`shareable` is declared but has
  zero code paths reading or acting on it**, confirmed by grep — a dark
  placeholder, not a shipped mode), `state` (`composed|kept` only — no
  "rejected" state at the artifact level), `generation_status`
  (`pending|generating|ready|failed` — but **in current code an artifact
  row is never persisted in any state but `ready`**, confirmed by grep; the
  mock composer never fails, `atlas/composer.py:43-97`).
- `atlas_derived_signals` (lines 269-316): per-artifact taste signals with
  `confidence` and `user_state` (`active|disputed|forgotten`), FK'd to
  `observations.id` for cascade-revoke ("provenance contract," module
  docstring lines 9-12).

**Intake has no server-side vision call at all.** Clustering happens
**entirely client-side** on the device (`backend/atlas/clustering.py:1-17`
docstring: *"the backend never sees raw PhotoKit data"*). The client submits
a batch of cluster metadata to `POST /api/atlas/candidates`
(`backend/api/routes/atlas.py:1213-1251`), server-validates the client's
declared confidence against photo/cluster-count thresholds
(`clustering.py:83-99`), and persists via `insert_candidate()`
(`ON CONFLICT DO NOTHING` on `cluster_fingerprint` — idempotent resubmit).
**There is no `warnings` field anywhere on the model** — the closest analog
is the validated confidence tier plus free-text `cluster_reason`.

**Approval is claim-first atomic, and is the one real idempotency pattern
worth copying wholesale:**

```python
# backend/core/db/atlas.py:137-160
def claim_candidate_for_approval(candidate_id, user_id) -> AtlasCandidate | None:
    # single UPDATE ... WHERE status='pending' -> 'approved' RETURNING *
    # eliminates the TOCTOU race from the old read-check-then-act pattern
```

The route (`backend/api/routes/atlas.py:1314-1327`) handles the losing
caller explicitly: if the claim fails because status is already
`approved`+`artifact_id` set, it fetches and returns the existing artifact
(idempotent replay); otherwise 409. LLM composition happens *after* the
claim, outside any DB transaction (it's an LLM call); if composition raises,
the claim is reverted back to `pending` (guarded on `artifact_id IS NULL`
so a fully-linked artifact is never reverted) and the client retries. The
DB-level unique index on `source_candidate_id` is a second, independent
backstop against duplicate artifact creation on races.

**Approving an Atlas candidate does not promote it into a Place, saved
place, or itinerary attachment — it stays Atlas-private, permanently.**
Trip linking (`atlas_artifacts.imported_trip_id`, set by
`backend/atlas/trip_link.py::resolve_imported_trip_id`) is a read-only
association for filtering/search — it never writes into a trip's itinerary
and never notifies the trip. Promotion to the taste graph
(`kept_place_affinity.py`) uses a deliberately separate entity-type
namespace (`entity_type="atlas_kept_place"`, `ATLAS_KEPT_PLACE_ENTITY_TYPE`)
specifically because *"there is no catalog venue/site entity to resolve
[Atlas's reverse-geocoded place_label] to"* (module docstring,
lines 12-34) — the module explicitly refuses to fabricate a venue id rather
than guess. This is the single most important structural fact for the
domain-model decision in §5: **Atlas's own code already ran into "we can't
promote an ambiguous place-string into the real place catalog" and chose to
create a parallel, lower-trust namespace rather than force it.** A general
ingestion system will hit the same wall for imported restaurant links and
needs a real answer, not a second parallel namespace.

**Privacy**: every route is user-scoped; candidates are never visible to
anyone but their owner; artifacts are never group-visible. The one
cross-user surface is the explicit, user-initiated "Unpacked" year-recap
share link, which is HMAC-token-gated and exposes **only aggregate counts**
— no raw photos, no candidate data, no artifact `sections`/`reflection`
(`atlas_unpacked_landing.py:8-12,60-168`).

**Inbox**: `GET /api/atlas/inbox/review`
(`backend/api/routes/atlas.py:1727-1796`) is a real, working "needs review"
queue, but its own docstring records that it used to fabricate synthetic
review items ("pattern checks, signal reviews... generated fresh each
request") and was deliberately stripped down to **only genuine `pending`
candidates** — i.e., the team already tried and reverted a "generic content
review queue" shape once. That is direct, first-party evidence against
building a second generic inbox for imports.

### 2.6 Upload and media-storage infrastructure

Three separate multipart upload endpoints, three different storage
strategies — this inconsistency is itself a finding:

| Endpoint | File:line | Storage | Dedup |
|---|---|---|---|
| `POST /api/trips/{id}/photos/upload` | `backend/api/routes/trip_photos.py:135-209` | S3 via `backend/media/rehost.py` (perceptual hash computed, `imagehash.phash`, but **never read/compared anywhere** — dead dedup signal) | None |
| `POST /api/atlas/artifacts/{id}/photos/upload` | `backend/api/routes/atlas.py:1906+` | S3 rehost, `atlas_artifact_photos` table | Real: `UniqueConstraint(artifact_id, source_photo_id)` with `ON CONFLICT DO UPDATE` — the **only** enforced content-level dedup in the whole media layer |
| `POST /api/trips/{id}/receipts/upload` | `backend/api/routes/expenses.py:1593-1687` | Local disk (`$_RECEIPT_STORAGE_DIR`), not S3 | Client `X-Idempotency-Key` header only |

15MB cap, image-only allowlist on all three. No table has a generic
content-hash unique constraint that would prevent the same photo landing
twice under two different upload calls.

### 2.7 Background jobs and extraction pipelines

Framework: `backend/core/job_queue.py` — Arq/Redis in production, inline
synchronous fallback in dev/test (lines 1-58). Worker modules live in
`backend/workers/`.

**The receipt-OCR pipeline is the best existing template for a unified
extraction stage**, and should be read as the reference implementation:

- Upload accepts an idempotency header (`expenses.py:1597,1613-1620`) so a
  client retry can't double-create a receipt or double-enqueue OCR.
- Enqueue uses Arq's own dedupe key: `enqueue(process_receipt_ocr,
  str(receipt_id), _job_id=f"ocr:{receipt_id}")` (`expenses.py:1673-1682`).
- Worker (`backend/workers/ocr_jobs.py::process_receipt_ocr`, lines 60-203)
  is idempotent at two levels (Arq job-id dedupe, plus a body-level
  short-circuit on `ocr_status` already `completed`/`failed`), wraps
  extraction in a 120s `asyncio.wait_for` timeout, and **always** marks the
  row `failed` on timeout or exception (lines 144-172) — no ambiguous
  half-state.
- A reaper (`backend/api/lifecycle.py`, `_run_ocr_reaper_loop`) flips any
  receipt stuck `pending` &gt;5 minutes to `failed`, so a crashed worker never
  leaves the client polling forever.
- Extraction (`backend/expenses/receipt_ocr.py::extract_receipt_data`,
  lines 55-121) is an LLM vision call with an explicit
  "omit fields not visible, never approximate" grounding instruction — this
  is the content-generation charter's grounding rule already implemented in
  code, and is exactly the posture an import extractor needs.
- Result is never trusted outright — the user reviews OCR output blended
  with manual corrections before an `expenses` row is created
  (`expenses.py:1761+`, comment lines 1785-1787).

**No equivalent job-queued, reviewed pipeline exists for booking
confirmations** (§2.3) — that path is synchronous, in-turn, LLM-vision-only,
with no job queue and no structured review UI beyond a chat reply. This gap
is one of the clearest, lowest-risk near-term consolidations available: port
booking extraction onto the same job/review pattern receipts already use.

### 2.8 Place search and adding a place

**There is no code path anywhere that lets a user or the agent introduce a
brand-new place not already in the `venues`/`sites`/`accommodations`/
`experiences` catalog tables.** Two writers exist, and both require an
existing catalog row:

- Personal save: `POST /api/users/{id}/saves` →
  `backend/core/db/saves.py::save_entity()` → `entity_saves` table
  (`backend/core/db/_tables/social.py:173-201`), `entity_type` CHECK-limited
  to `venue|accommodation|experience|site|neighborhood|trip_story`,
  `entity_id` must already resolve. Unique on
  `(user_id, entity_type, entity_id)` — duplicate saves 409.
- Itinerary add: tool `itinerary_block_add`
  (`backend/concierge/tool_handlers/itinerary_edit.py:945-1052+`) explicitly
  **rejects** a free-text name with no resolvable id to avoid a "ghost
  block" (comment, lines 1017-1021): *"venue_id {id} not found — use
  search_venues to find a valid id."*

This is the single most consequential gap for the whole ingestion design.
A restaurant link, a screenshot of a place Vesper has never heard of, or a
TikTok about a hole-in-the-wall has, today, **no legal destination** at the
*writer* level (`save_entity`, `itinerary_block_add`). Section 5 discusses
the fix — but see the correction below: the schema itself already has a
cheaper escape hatch than the fix originally proposed here.

**Correction (added after initial publication, prompted by a reviewer
question): the `itinerary_blocks` table already has a designed-for
unresolved-place mechanism; `itinerary_block_add` simply refuses to use
it.** `backend/core/db/_tables/itinerary.py:172-178,217-223`:

```python
Column("venue_id", Integer, ForeignKey("venues.id")),
Column("site_id", Integer, ForeignKey("sites.id")),
Column("experience_id", PG_UUID(as_uuid=True), ForeignKey("experiences.id")),
Column("title", Text, nullable=False),
...
# Whether this block's title names a venue/site id that couldn't be
# resolved to a real row at persist time (a "name-only" block — null FK,
# possibly-fabricated title). Null = unknown/legacy, or the block never
# named a venue/site to begin with (free_time, transit, interludes).
# True = unverified; render without a venue card / nav target.
Column("venue_unlinked", Boolean),
```

The check constraint `num_nonnulls(venue_id, site_id, experience_id) <= 1`
explicitly permits **zero** — a block can exist today with no linked
catalog entity, just a `title` and `venue_unlinked=True`, rendering
honestly as "unverified" per the column's own docstring. This is a
first-class, already-designed concept at the schema level. `
itinerary_block_add` (`concierge/tool_handlers/itinerary_edit.py:1017-1021`)
simply never exercises it — it hard-rejects any input that doesn't resolve
to an existing `venue_id`/`site_id`, rather than falling back to a
`venue_unlinked` write. That is a policy choice in one function, not an
architectural limitation, and it revises the Phase 0 recommendation in §11:
the minimal fix is **not** a new provisional-catalog concept in the corpus
— it's teaching the import path (and possibly `save_entity`, which has no
equivalent unlinked mode today and would need one) to write a
`venue_unlinked=True` block/save from imported title + address + lat/lng
when nothing resolves, rather than inventing new corpus-quality-gated
infrastructure.

The real cost of that cheaper path, stated plainly rather than glossed
over: a `venue_unlinked` block **permanently** renders without live
open/closed status, a map pin, or closed-hours conflict-checking (all of
which require a real venue row) unless a human later manually resolves it
to a catalog entry — there is no automatic promotion path today. The
heavier "provisional catalog row" design this report originally proposed
would preserve those features once verified; the `venue_unlinked` path
trades that capability away in exchange for being buildable with a small,
already-precedented change instead of new corpus infrastructure. Which
tradeoff is right is a product decision, not something this report resolves
— restated as an open question in §12.

### 2.9 Itinerary/place attachment writers

**No generic `attachment` concept exists** — grepped `tables.py` and every
file in `_tables/` for "attachment," zero hits. Each media type reimplements
its own bespoke FK back to its parent:

- `trip_photos.block_id` → `itinerary_blocks.id` (`SET NULL`), auto-tagged
  by EXIF time+GPS proximity, `tag_confidence` column (NULL = manual).
- `chat_images.message_id` → owning message.
- `receipts` ← `expenses.receipt_id`, plus `expenses.block_id` → block.
- `atlas_artifact_photos.artifact_id` → artifact (the one table with real
  dedup, see §2.6).

Four independent reimplementations of "this media belongs to that object,"
each with its own confidence/visibility/dedup semantics. A unified system
should not try to retrofit a single polymorphic `attachments` table over all
four (high blast radius, low near-term value) — it should add one **new**
table for inbound/imported content (§5) and leave these four as they are.

### 2.10 Mobile ingestion entry points

- **No OS-level share-sheet / Share Extension mechanism exists at all** —
  confirmed absent from `app.json`, `ios/TravelApp/Info.plist` (no
  `CFBundleDocumentTypes`), and `package.json` (no `expo-share-intent` or
  equivalent). The only inbound channel is two universal-link paths
  (`/invite`, `/stories`) matched by Expo Router — fundamentally different
  from OS share-sheet capture. There is no `Linking.addEventListener`
  anywhere in the codebase. **This is net-new native-module work, not a
  matter of wiring up dormant infrastructure.**
- Chat attachment UI: `components/chat/ComposerBar.tsx` (see §2.1).
- Camera/library entry points, all via `expo-image-picker` (no
  `expo-camera` package installed anywhere): chat attach, expense-receipt
  scan (`components/expense/AddExpenseSheet.tsx:372,388`), Trip Story photo
  slots, Atlas postcard-render source photo. `expo-media-library` (distinct
  from the picker) powers Atlas's full-library scan.
- Atlas scan/candidate/inbox screens live at `app/atlas/{scan,inbox,
  candidate/[id]}.tsx`; `app/you/atlas/*` are 1-line re-export shims post
  the in-flight nav migration (§2.11). `scan.tsx` offers "find memories from
  photos" (full scan) or "choose photos myself" (manual); `candidate/[id]
  .tsx` offers Keep / Refine / Not this time; `inbox.tsx` is single-purpose
  (photo candidates only) by explicit design comment (lines 5-7): *"other
  Atlas objects stay in their owning surfaces until they have durable,
  dismissible server-side review work of their own."*
- Places UI (`components/places/PlacesWorkspace.tsx`) is search-box only —
  **no URL/paste input anywhere in the app** (grepped for
  `isValidUrl`/`urlRegex`, zero hits). The only "paste a link" UI in the
  entire app is `app/invite-code.tsx` for accepting a trip invite — unrelated
  to content ingestion.
- The receipt-OCR pipeline (§2.7) has a complete, working mobile
  counterpart: `hooks/useUploadReceipt.ts` — client-side size/type guard,
  multipart upload, exponential-backoff poll (2s→30s, ~2min ceiling),
  idempotency-keyed retry, `AppState`-aware abort-on-background. This is the
  most mature end-to-end ingestion UX in the app today and should be the UX
  template for import status polling.
- `expo-clipboard` is present but **write-only everywhere** (copy-to-
  clipboard only; zero `getStringAsync`/paste usage anywhere in the repo).
  `expo-document-picker` is not installed; no PDF handling exists anywhere.

### 2.11 Canonical mutation gateways, attention system, and receipts

One correction to workspace docs first: `docs/systems/proposals-change-
studio.md` names `build_and_persist_proposal`, `plan_edit_preview.py`,
`plan_edit_commit.py`, and `plan_events` as the current implementation —
**none of these exist in code today.** They were superseded by an IR-08
rewrite. This report cites the actual current implementation; the charter
itself needs a correction pass independent of this ingestion work.

**Proposal gateway (current, real):**
`backend/core/itinerary_proposal_gateway.py:395`,
`create_itinerary_operation_proposal()`. All four proposal producers
(`itinerary_proposal_producer.py`) call this one function — the "one
creation path" invariant holds structurally. It writes `change_proposals`
and `itinerary_operation_proposals`, and records an `ActionChannel` enum
(`itinerary|map|discover|chat|background|provider`,
`core/models/itinerary_operations.py:167-173`) plus an `authorship_origin`
(`human_group|human_private_shielded|VESPER_AUTONOMOUS`) — **a source/origin
field already exists and an ingestion pipeline can extend the channel enum
rather than invent a new provenance field.** `plan_events` is confirmed
dead as a writer target (explicit code comment,
`core/db/_tables/itinerary.py:480-483`: *"New itinerary evidence is written
only to the canonical operation ledger... this table remains read-only"*).

**Direct edit path (current, real):**
`POST /api/trips/{id}/itinerary/operations/preview` →
`backend/api/routes/itinerary_operations.py:137`. Idempotency is a
**deterministic content hash**, not a random token —
`backend/core/itinerary_operation_preview.py:68`:

```python
def preview_hash(operation: NormalizedItineraryOperation) -> str:
    encoded = json.dumps(semantic_operation_payload(operation), sort_keys=True,
                          separators=(",", ":"), ensure_ascii=False).encode()
    return f"sha256:{hashlib.sha256(encoded).hexdigest()}"
```

10-minute TTL (`_PREVIEW_TTL`, line 33). Commit
(`itinerary_commit_gateway.py:137`) serializes on a Postgres advisory lock
keyed by `(trip_id, idempotency_key)`, and replays a **permanent** stored
result on key reuse (`load_idempotent_itinerary_operation_result`, no TTL)
provided the preview hash still matches. This content-hash-plus-replay
pattern is directly reusable for import dedup (§5, §7).

**Attention system (current, real, and mature):** `attention_cases` table
(`core/db/_tables/notifications.py:190-258`), unique on
`(attention_type, subject_type, subject_id, recipient_id)`. `TYPE_REGISTRY`
(`core/attention_type_registry.py:512`) — each entry declares
`decision_mode`, `attention_class`, `lifecycle_kind`, `audience_rule`,
`allowed_projections`, `home_primary_owner`, `expiry`, `dedupe_strategy`,
etc. Registering a new type is one more `_definition(...)` call. Section
membership on the Home "needs your attention" feed
(`backend/api/routes/_notifications_feed.py:589-594`) is deterministic on
lifecycle state when an `attention_cases` row backs the notification
(`work_state=="open" and truth_state=="current" and projection_state==
"active"`), falling back to an urgency+unread heuristic otherwise. **This is
the correct, existing home for "does this import need your attention" — not
a new inbox.**

**Trust receipt ledger (current, real, with a gap):**
`vesper_action_receipts` (`core/db/_tables/action_receipts.py:18-94`) —
`public_reasons`/`private_influences` JSONB columns already implement the
privacy split the work-receipt doc and the 2026-07-09 decision record
require. Writer `create_action_receipt()`
(`core/db/action_receipts.py:85`) is upsert-safe on `idempotency_key`.
**Gap found:** `create_direct_edit_receipt` (line 43) has **zero call
sites** anywhere in the codebase — the direct-edit commit path
(`itinerary_commit_gateway.py`) never calls it; its evidence trail is a
structurally different mechanism (`itinerary_operation_transitions
.evidence` JSONB). This is precisely the "two receipt primitives that don't
line up" problem the work-receipt doc is scoping around, and an ingestion
receipt must not become a third one.

**`group_compose` (current, real):**
`backend/concierge/group_compose.py::execute_compose_group_message()`
(line 822) is documented as *"the only sanctioned way to produce text
destined for a group conversation"* (module docstring). Layered privacy
pipeline: name-leak regex check → constraint-leak check → attribution-
stripped composition context → per-message-kind character clamp →
LLM-based semantic privacy guard with a regenerate-with-avoid-list retry.
A composition that can't pass is suppressed with a structured error, never
sent softened. **Any group-visible import receipt must route through this
function — no exceptions, per its own docstring.**

**Canonical place/booking writers:** see §2.8 for places. Booking has a
clean, already-named split worth reusing verbatim: the live-provider flow
(`booking_sessions`/`booking_offers`, Duffel-backed) vs.
`attest_external_handoff_completed()`
(`backend/core/booking_attestation_gateway.py:57`) — a **named, existing
concept** for *"the traveler told us this happened; we are not claiming
provider confirmation"* (module docstring, lines 1-5), which is exactly the
epistemic status of a booking screenshot or forwarded confirmation email.
An imported booking should write through this exact function, not a new one.

**Other idempotency conventions worth reusing:** `notification_dedup.py::
try_claim()` (line 39) — a cross-process, cross-Fly-worker claim table using
`INSERT ... ON CONFLICT DO NOTHING` with a 120-second stale-claim takeover
window, built specifically because in-process idempotency caches don't work
across workers. This is the right pattern for "don't double-process the
same shared link if two workers pick it up."

## 3. Capability / gap matrix

| Capability | Exists today? | Where | Reusable as-is for imports? |
|---|---|---|---|
| Idempotent content-hash dedup | ✅ | `itinerary_operation_preview.py::preview_hash` | Yes — pattern, not the function itself |
| Claim-first atomic approval | ✅ | `atlas.py::claim_candidate_for_approval` | Yes — pattern to copy for `inbound_items` |
| Cross-worker dedup claim table | ✅ | `notification_dedup.py::try_claim` | Yes — directly, for "don't double-ingest" |
| Attention/review routing | ✅ | `attention_cases` + `TYPE_REGISTRY` | Yes — add one new `notification_type` |
| Group-visible privacy composition | ✅ | `group_compose.py` | Yes — mandatory route for any group receipt |
| Public/private receipt split | ✅ | `vesper_action_receipts` | Yes, but direct-edit call site is missing — must not repeat the gap |
| Proposal mutation gateway w/ origin tracking | ✅ | `itinerary_proposal_gateway.py` + `ActionChannel` | Yes — extend the channel enum |
| Background job + review pattern | ✅ | receipt OCR (`ocr_jobs.py`) | Yes — template for import extraction |
| Named "unconfirmed/user-reported" booking concept | ✅ | `booking_attestation_gateway.py` | Yes — route imported bookings through it |
| Candidate → approval → canonical, private-only | ✅ (Atlas) | `atlas_candidates`/`atlas_artifacts` | Pattern only — table itself is wrong scope (private-memory, no promotion path) |
| Generic content-review inbox | ⚠️ tried, reverted | Atlas inbox docstring | No — evidence against building a second one |
| Uploads/media storage | ⚠️ exists 3x, inconsistent | trip photos (S3), receipts (disk), Atlas photos (S3+real dedup) | Partially — pick one pattern, don't add a 4th |
| Generic polymorphic attachment table | ❌ | — | No — 4 bespoke FKs exist; not worth retrofitting |
| Create a place not already catalogued | ❌ | — | **No — must build.** Blocking gap. |
| URL unfurling / link metadata resolution | ❌ | — | No — must build |
| Screenshot-specific structured extraction | ❌ | generic vision-summary only | No — must build |
| Booking-email parsing / inbound email | ❌ | — | No — must build (or explicitly defer, §12) |
| PDF ingestion | ❌ | — | No — must build (or defer) |
| iOS/Android share-sheet capture | ❌ confirmed absent | — | No — net-new native work, Expo SDK 55 experimental path exists (§4) |
| Clipboard paste-to-ingest | ❌ | — | No — trivial to add, low value alone |
| Durable (non-ephemeral) work receipt | ❌ | work-receipt doc is a spec, not code | No — must build |

## 4. Competitive and platform findings

All claims below are sourced; see §13 for the full citation list. Dates are
the source's own last-modified stamp where visible.

### 4.1 Product patterns

- **Mindtrip "Start Anywhere"** accepts articles, videos, photos, screenshots
  and PDFs via the OS share sheet and turns them into a chat, collection, or
  trip plan ([App Store listing](https://apps.apple.com/us/app/mindtrip-ai-travel-companion/id6503107567);
  [mindtrip.ai](https://mindtrip.ai/)). Notably, **bookings/receipts use a
  separate forwarding address** (`receipts@mindtrip.ai`) distinct from
  Start Anywhere — Mindtrip itself treats inspiration-capture and
  transaction-capture as different problems, which matches this report's
  recommendation to slice booking import separately from place import.
  UNVERIFIED anywhere official: whether there's a review/confirm step
  before content lands in a trip, or whether the original source is
  preserved.
- **Wanderlog** uses a **per-trip forwarding email alias**
  (`trip+123@wanderlog.com`) obtained from inside a specific trip — the
  routing decision is made by the user before sending, not resolved
  server-side ([Wanderlog Help, indexed ~2022-03-10](https://help.wanderlog.com/hc/en-us/articles/4625693334811-Add-flight-hotel-and-rental-car-details-by-forwarding-an-email)).
  Gmail auto-import is a gated Pro feature, scoped narrowly to
  flight/hotel confirmations only ([Wanderlog Help, ~2023-02-28](https://help.wanderlog.com/hc/en-us/articles/13302942899099-Is-it-safe-to-connect-my-Gmail-account-to-Wanderlog)).
  No documented review queue exists — content is stated to import directly.
- **TripIt** is the most instructive precedent and the only one with a real
  review queue: a single shared address (`plans@tripit.com`), with the
  user's registered sender addresses resolving identity
  ([TripIt Help](https://help.tripit.com/en/support/solutions/articles/103000063275-adding-travel-plans-to-tripit)).
  Unrecognized items land in **Unfiled Items** — documented as an
  **overflow/failure sink**, not a mandatory gate: successfully parsed items
  go straight into trips; only what the parser couldn't file waits for the
  user ([TripIt Help](https://help.tripit.com/en/support/solutions/articles/103000063393-unfiled-items)).
  TripIt's newest capability (TripIt Pro + Apple Intelligence, iOS 26+) does
  screenshot/PDF → structured plan extraction, and explicitly **presents
  the result for review and edit before saving**
  ([TripIt Help](https://help.tripit.com/en/support/solutions/articles/103000361047-tripit-pro-and-apple-intelligence))
  — the review gate exists specifically on the lowest-confidence modality
  (images/PDFs), not on email. **TripIt also tiers sensitivity within an
  imported item**: the itinerary skeleton is shareable at "view" permission,
  but confirmation numbers, cost, and attached documents require "edit"
  permission and are stripped from public share links entirely
  ([TripIt Help](https://help.tripit.com/en/support/solutions/articles/103000063367-trip-sharing-from-our-website)).
  This two-tier model is the single most transferable design in the sweep.
- **Google Maps** collaborative Lists support invite-based sharing with
  full identity exposure to viewers (no anonymous contribution mode) and
  emoji-based lightweight voting when a place is shared into a group
  ([Google Maps Help](https://support.google.com/maps/answer/7280933);
  [Google Blog, 2023-11-15](https://blog.google/products/maps/google-maps-updates-november-2023/)).
  **No import path into Lists is documented anywhere** — file import (CSV/
  KML/GPX) belongs to the separate My Maps product
  ([My Maps Help](https://support.google.com/mymaps/answer/3024836)); this
  is an inference from documented absence, not a confirmed limitation.
- **Partiful**'s relevant lesson is not "no login" — it's that **friction is
  deferred to the moment of commitment, not imposed at capture**: any link,
  any channel, no app or account needed to view an invite, but RSVP requires
  phone-number verification, and that verified number is the same asset
  that powers the host's broadcast channel
  ([Partiful Help](https://help.partiful.com/hc/en-us/articles/34230743189787-How-do-I-RSVP-to-an-event-on-Partiful)).
  This maps onto imports as: capture should cost nothing, but anything that
  becomes a group-visible commitment (a booking, a proposal) can reasonably
  ask for a confirming action.
- **Emerging category, worth naming as a competitive signal**: single-
  purpose "save a TikTok place to a map" apps (Stashed, Plotline, and
  several others) are shipping the exact "share sheet → extracted place"
  primitive as a standalone product, with **no collaboration or review
  layer** — the capture step is rapidly commoditizing.

### 4.2 Platform capabilities

- **iOS Share Extensions** hand data via `NSExtensionItem`/`NSItemProvider`;
  activation is declared with `NSExtensionActivationRule` keys or a
  predicate; there is **no direct IPC between an extension and the host
  app** — handoff requires an **App Group** shared container
  ([Apple: App Extension Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/Share.html);
  [Apple: Extension Overview](https://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/ExtensionOverview.html)).
  Apple documents that extensions cannot run long background tasks and
  **there is no supported way to launch the containing app directly from a
  share extension** except Today/Widgets, per an Apple Frameworks Engineer
  on the official Developer Forums, who also notes this "may require
  additional App Store review" ([Apple Developer Forums](https://developer.apple.com/forums/thread/773342)).
  Memory limits are not officially published (confirmed by a DTS engineer's
  forum answer); the commonly cited ~120MB ceiling is community lore, not
  documented fact.
- **Expo SDK 55 changes the build calculus materially**: `expo-sharing` now
  ships **first-party, experimental inbound sharing** — a config plugin
  adds an iOS `share-extension` target and Android intent-filters, delivers
  shares as deep links, and exposes a `useIncomingShare()` hook
  ([Expo SDK 55 changelog](https://expo.dev/changelog/sdk-55);
  [Expo `expo-sharing` docs](https://docs.expo.dev/versions/latest/sdk/sharing/)).
  It requires a dev client / EAS Build (not Expo Go), and **Expo's own docs
  disclose that its iOS implementation opens the main app instead of
  processing inside the extension — "not officially supported by Apple and
  may stop working in a future iOS release."** This is the exact pattern
  Apple's own forum post says has no supported path. Treat this as real,
  buildable infrastructure with a known, vendor-disclosed fragility risk,
  not as a solved problem.
- **Android** registers a share target via `ACTION_SEND`/`ACTION_SEND_MULTIPLE`
  intent filters with `CATEGORY_DEFAULT`; payload arrives via
  `EXTRA_TEXT`/`EXTRA_STREAM` ([Android: Receive simple data](https://developer.android.com/training/sharing/receive)).
  Large uploads after a share fall under Android 14+'s foreground-service-
  type requirements or, better, **User-Initiated Data Transfer jobs** —
  which require the transfer to be user-triggered, keep the user informed
  via notification, and are exempt from ordinary job quotas
  ([Android: Data transfer background task options](https://developer.android.com/about/versions/15/changes/datasync-migration)).
- **What actually arrives from specific apps is almost entirely
  undocumented** by the source apps themselves, with one clean exception:
  **Safari** supports a documented JS-preprocessing contract
  (`NSExtensionJavaScriptPreprocessingFile` + a global `ExtensionPreprocessingJS.run()`
  that calls `arguments.completionFunction({...})`, read back via
  `NSExtensionJavaScriptPreprocessingResultsKey`) that can hand back page
  title, canonical URL, and OpenGraph tags — a real, structured contract,
  not a bare URL ([Apple: Handling Common Scenarios](https://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/ExtensionScenarios.html)).
  Without that JS file, Safari hands over `public.url` and essentially
  nothing else — the compose UI *looks* like it has the title because
  `SLComposeServiceViewController` prefills it, but that title is not
  exposed as a readable attachment.
- **Apple Maps' coordinate removal is real, DTS-acknowledged, and its
  resolution status is unconfirmed as of this report.** Three Apple
  Developer Forums threads (Sept–Oct 2025) document that iOS 26 devices
  stopped sending the `com.apple.mapkit.map-item` attachment and switched
  to a coordinate-free short link (`https://maps.apple/p/...`) where iOS
  18.5 sent a long-form URL with `coordinate=...` inline
  ([thread 805396](https://developer.apple.com/forums/thread/805396)).
  Apple DTS replied in-thread that this was an unintended regression being
  rolled back ("you'll begin to see the payloads you were using in the past
  ... over the next day") and that the URL "is not intended to be a
  structured API or parsed out like this." **No 2026 follow-up confirms the
  rollback completed** — treat current Apple Maps share behavior as
  unverified and measure it directly on a real device before designing
  around either the old or new payload shape. Apple does officially
  document how to resolve the short form when it does appear: check for a
  `maps.apple` (no `.com`) host, then follow the documented HTTP 301
  redirect to recover the long-form URL and its `coordinate`/`place-id`
  parameters ([Adopting unified Maps URLs](https://developer.apple.com/documentation/mapkit/unified-map-urls)) —
  developers report this redirect is less reliable in practice than the
  docs imply, so instrument for an intermediate hop.
- **No supported path exists from a shared photo back to a `PHAsset`.**
  Apple staff have stated directly that an `NSItemProvider` image "does not
  have to be in the iOS Photo Library" and that filename-matching to a
  `PHAsset` "will not work on all iOS versions"
  ([Apple Developer Forums](https://developer.apple.com/forums/thread/68311)).
  Shared photos also frequently arrive HEIC-transcoded to JPEG on the fly,
  a known source of `NSItemProviderErrorDomain` failures, and Live Photos
  reportedly yield only the still frame — the `.mov` motion component has
  no working extraction path. **This means an imported photo must be
  treated and stored exactly like any other rehosted image (§2.6), never
  like an Atlas `sample_photo_ids` PHAsset reference (§2.5) — the two
  photo-ingestion mechanisms are structurally incompatible, not just
  differently scoped.**
- **Instagram and TikTok publish no outbound-share documentation
  whatsoever** — both vendors' developer docs only cover sharing *into*
  their apps. What arrives is, by community consensus (not vendor
  documentation), a bare tracking-laden URL: Instagram appends a per-share
  `igsh` token to `/reel/<code>/` or `/p/<code>/` links that must be
  stripped before using the shortcode as a dedup/content key (different
  shares of the same post carry different tokens); TikTok emits one of
  several short-link host/path shapes (`vm.tiktok.com/<id>`,
  `tiktok.com/t/<id>`, `vt.tiktok.com/...`) that must all be resolved
  server-side to a stable numeric video id, and that resolution itself
  round-trips through ByteDance's servers. **Any URL-normalization step in
  the extraction job (§6) must strip known tracking parameters and resolve
  to a stable id before computing `content_hash` (§5)**, or the same shared
  post will dedup-fail across two shares from different people.
- **Messages, WhatsApp, and Mail confirm the report's email conclusion from
  a different angle.** Apple's own support docs describe no share-sheet
  path for iOS Messages text at all (only in-app forward); WhatsApp's one
  officially documented structured export (**Export Chat**) does route
  through the OS share sheet and includes sender names and timestamps in
  a `.txt`/`.zip` payload, which is a viable low-priority future capture
  mode but is a deliberate user export action, not passive capture. Most
  importantly: **there is no share-sheet or API path to hand a real email
  message to a third-party app on either iOS Mail or Gmail** — third-party
  task apps (OmniFocus, Things) solve this exact problem with a forwarding
  address specifically *because* no share-sheet route exists, which is
  direct external validation of this report's own recommendation
  (§4.2, §11 Phase 3) to use a forwarding alias rather than chase a
  share-sheet path for booking-email capture that does not exist on either
  platform.
- **Inbound email forwarding** is a well-trodden technical pattern
  (SendGrid Inbound Parse, Mailgun Routes, Postmark Inbound, AWS SES
  receiving) — any of these can implement a per-user opaque alias on a
  dedicated subdomain, which is a **stronger design than TripIt's own
  shared-address-plus-sender-matching approach**
  ([Twilio SendGrid Inbound Parse](https://www.twilio.com/docs/sendgrid/for-developers/parsing-email/setting-up-the-inbound-parse-webhook)).
- **Gmail vs. Outlook OAuth is a real, decisive cost asymmetry.**
  `gmail.readonly` is a **restricted** scope requiring an annual, paid,
  third-party CASA security assessment with a ~6-week (not guaranteed)
  turnaround, and is **unavoidable for any architecture where email content
  reaches your server**
  ([Google: Restricted scope verification](https://developers.google.com/identity/protocols/oauth2/production-readiness/restricted-scope-verification)).
  Outlook's `Mail.Read` requires only a **free** publisher-verification
  step via a Partner Center account, no annual paid audit
  ([Microsoft: Publisher verification](https://learn.microsoft.com/en-us/entra/identity-platform/publisher-verification-overview)).
  Since most consumer booking email lives in Gmail, this asymmetry is a
  strong argument for the forwarding-alias approach over inbox OAuth as a
  first move — it sidesteps both regimes entirely, at the cost of asking
  the user to forward instead of granting silent access.

## 5. Recommended domain model

**Recommendation: add one new table, `inbound_items`, narrower than the
brief's proposed envelope, and route everything else through systems that
already exist.** Do not reuse `atlas_candidates` (wrong privacy scope, no
promotion path — §2.5). Do not build a polymorphic `attachments` table
(high blast radius across four working systems, no near-term payoff — §2.9).

```
inbound_items
  id                    uuid pk
  trip_id               uuid fk (nullable — a share can predate trip selection)
  owner_id              uuid fk users            -- who shared it in; always required
  audience              text check (private | group_pending | group_visible)
  source_kind           text check (share_url | share_text | share_image |
                                     chat_image | booking_screenshot | pdf |
                                     forwarded_email | photo_scan_batch)
  origin_channel        text  -- reuse ItineraryOperationProposal's ActionChannel
                                  enum where it fits (chat|share|forward|scan);
                                  extend the enum rather than fork a new one
  raw_ref               text  -- storage pointer: local disk path, S3 key, or
                                  message_id — never the payload itself
  mime_type             text
  content_hash          text  -- sha256 of raw bytes/text; the dedup key
  extracted_candidates  jsonb -- list of {kind, fields, confidence, warnings}
  extraction_confidence text check (high | medium | low)
  extraction_warnings   jsonb
  status                text check (received | extracting | needs_review |
                                     auto_routed | approved | dismissed | failed)
  attention_case_id     uuid fk attention_cases  -- nullable; set only when
                                                     status = needs_review
  promoted_refs         jsonb -- {place_ids: [...], proposal_id, booking_id,
                                  itinerary_block_ids: [...]}
  receipt_id            uuid fk vesper_action_receipts
  created_at, updated_at, failed_at, failure_detail
```

Key design decisions and why:

- **`content_hash` + a partial unique index on `(owner_id, content_hash)`**,
  mirroring `atlas_candidates.cluster_fingerprint` exactly — the same
  `ON CONFLICT DO NOTHING` idempotent-resubmit pattern applies verbatim.
- **`attention_case_id` is nullable and only set when review is needed** —
  this is the mechanism that makes "route into the existing attention
  system" real rather than aspirational. A high-confidence single-place
  link that auto-routes to Places never touches `attention_cases` at all.
- **No `warnings`-as-first-class-object invention** — Atlas already proved
  out "confidence tier + free-text reason" is sufficient; this report
  follows that precedent rather than the brief's more elaborate proposal.
- **`promoted_refs` is deliberately generic JSONB, not typed FK columns** —
  because a single import can fan out to zero, one, or many canonical
  objects (a screenshot with 6 restaurants promotes 6 place rows and 0
  proposals; a booking screenshot promotes exactly 1 `trip_accommodations`
  row via the attestation gateway). Forcing typed columns here would
  require a new column per canonical object type as the system grows.
- **`raw_ref` never stores the payload inline** — reuse the existing
  storage pattern from whichever media type applies (S3 rehost for photos,
  local disk for anything ephemeral/short-lived) rather than inventing a
  fourth storage strategy.
- **The missing "create a provisional place" writer (§2.8) is a
  prerequisite, not part of this table.** Recommend a `provisional` boolean
  or `status='provisional'` value on the existing venue/site creation path
  (exact mechanism is a backend design decision out of scope for this
  report — flagged as an open question in §12), so an extracted restaurant
  that isn't in the corpus gets a real venue row rather than dead-ending.
  This directly fixes the wall Atlas's `kept_place_affinity.py` hit and
  worked around with a parallel namespace (§2.5) — don't repeat that
  workaround for imports; fix the underlying gap once.

## 6. Proposed processing state machine

```
received
  → extracting            (background job enqueued, Arq job-id = f"ingest:{item_id}")
      → needs_review       (low/medium confidence, or multi-item batch,
                             or promotion target requires a decision)
          → approved       (user or auto-router promotes; writes canonical
                             object(s); writes receipt)
          → dismissed       (user rejects; no canonical write; receipt still
                             written — "received but not used" is itself
                             receipt-worthy per the work-receipt doc's
                             "what did it deliberately not change")
      → auto_routed         (high confidence, single unambiguous target,
                             reversible destination — e.g. one place → Places)
          → approved         (terminal; receipt written same-transaction)
      → failed              (extraction raised, or timed out — mirror the
                             OCR job's 120s wait_for + always-mark-failed
                             pattern, §2.7)
```

This mirrors the receipt-OCR job's state machine almost exactly
(`pending → processing → completed/failed`, §2.7) with two additions:
`needs_review` as a genuine terminal-until-acted state (borrowed from
Atlas's `pending`), and `auto_routed` as a distinct state from `approved` so
receipts can say "Vesper did this without asking" vs. "you approved this" —
a distinction the work-receipt doc's four-move anatomy requires (move 2,
"work done, with the reason").

Failure handling copies the OCR reaper: any row stuck in `extracting` past a
TTL (5 minutes, matching the OCR reaper's threshold) flips to `failed`
rather than hanging indefinitely.

## 7. Routing and review rules

Answering the brief's specific scenarios:

| Input | Auto-route? | Destination if not | Notes |
|---|---|---|---|
| Single restaurant link, resolves to one real place | Yes, if the place already exists in the corpus | — | If the place doesn't exist yet, this is where the provisional-place writer (§5) is required — otherwise this **cannot** auto-route today (§2.8 gap) |
| TikTok/Instagram share, incomplete metadata | No | `needs_review` → Places (as a provisional/low-confidence save) | Metadata gaps are exactly what `extraction_warnings` should record; never fabricate a missing field (Content Generation charter, §2.11) |
| Screenshot, one place | Maybe, if confidence is high and the place resolves | `needs_review` otherwise | Same resolution rule as the link case |
| Screenshot, several places | No | `needs_review`, presented as **one batch**, not N separate items | See batching note below |
| Map/list/article, many places | No | `needs_review` batch | Same as above; this is the "many imported items become one operation" case the brief asks about — batch at the `inbound_items` → attention-case level: one `attention_case` per batch, not per place |
| Booking screenshot | No — never auto-route money/booking-shaped content | `needs_review`, **private by default** | Route the confirmed write through `attest_external_handoff_completed` (§2.11), never a new booking writer |
| Forwarded confirmation email | No | `needs_review`, private | Same writer as above once parsed |
| PDF ticket/itinerary | No | `needs_review`, private | Out of scope for the first slice (§10); flagged non-goal for now (§12) |
| Batch of trip photos | Existing Atlas scan path is correct and should not be forced into this table | — | Atlas's private-memory scope is a deliberate, correct design (§2.5) — don't merge it into a group-shaped ingestion table |
| Duplicate/contradictory sources | Dedup via `content_hash` at ingestion; **contradiction** (two sources disagree on a fact) is not solvable by dedup — surface both in the same `needs_review` item and let the human pick, don't silently prefer one | | This is a real open question, not a solved one — flagged in §12 |
| Wrong-trip input | If `trip_id` is ambiguous or absent at share time, hold at `received` with `trip_id=NULL` until the user (or a lightweight disambiguation prompt) assigns one — never guess-assign to "the most recent trip" silently | | Mirrors TripIt's Unfiled Items exactly — this is the one place a TripIt-style "unfiled" holding state is the right pattern, scoped to trip assignment only, not general review |
| Private/sensitive content | `audience='private'` is the default for every new `inbound_items` row; promotion to `group_visible` requires an explicit action and routes any resulting text through `group_compose` | | Never default to group-visible |
| Parser can't understand it | `status='failed'`, `failure_detail` populated, still gets a receipt (per work-receipt doc: report what didn't happen too) | | |

**When does something enter "needs your attention" vs. Places vs. the
itinerary directly?**

- **Places**, not attention, for anything place-shaped with no group
  decision pending — this is the literal scope the Places charter and the
  in-flight navigation migration already assign it (§2.5's Places charter
  citation: *"Places should remain the home for uncommitted place ideas"*
  is already product doctrine, not a new decision this report is making).
- **Attention (`attention_cases` + a new `import_review` type)** for
  anything that needs a decision before it can be trusted: multi-item
  batches, low-confidence extractions, anything booking/money-shaped,
  anything that would otherwise need a new proposal.
- **The itinerary directly, via the existing proposal gateway**, only when
  an import's natural destination is a scheduled change (e.g., "add this to
  Thursday") — and even then, it goes through
  `create_itinerary_operation_proposal` like every other mutation, with
  `origin_channel` recording that it came from an import. It never gets a
  new, parallel write path.

**Should raw imports ever be group-visible?** No, by default, ever. The raw
screenshot/email/link is `audience='private'` unless and until a human
explicitly shares it forward — this matches the brief's own constraint and
every relevant charter (`graph-legibility-doctrine.md`'s keep-silent list,
`group-social.md`'s privacy rules, the Content Generation charter's "public
and group renderers receive only their privacy-safe projection").

**How does a user correct an extraction?** Reuse the Atlas candidate-review
UX pattern exactly: review is read-only except for two actions (approve
with edits / dismiss) — never a freeform edit form. If the extracted place
name is wrong, the correction is "dismiss, then add manually" (matching how
`itinerary_block_add` already refuses fabricated ids, §2.8) rather than
allowing an unverified free-text override to become canonical.

**How do multiple imported items become one batch operation?** One
`inbound_items` row per raw source, but **one `attention_cases` row per
batch** when a single share produces multiple candidates (a list/article
with 8 restaurants) — group the `inbound_items` rows by a `batch_id` and let
the attention projection render "8 places from this list" as a single
review card with per-item approve/dismiss, mirroring Atlas's `keep-all`
bulk-approval pattern (§2.5) rather than 8 separate attention cases.

**What happens on partial success?** Each candidate within a batch gets its
own `status`; the batch's attention case resolves only when every candidate
is terminal (approved/dismissed/failed) — and the receipt explicitly
reports the split ("4 saved to Places, 2 skipped as duplicates, 1 couldn't
be read"), matching the work-receipt doc's "what did it deliberately not
change" move.

## 8. Privacy / audience model

- **Default audience is always `private`.** This is non-negotiable per the
  brief's own constraints and is already how every comparable system in the
  codebase behaves (Atlas candidates/artifacts are user-scoped by default;
  `trip_accommodations.visibility` defaults conservatively; `group_compose`
  exists precisely because nothing reaches the group without passing
  through it).
- **No new privacy mechanism is needed — reuse `group_compose` for the text
  and the existing constraint-privacy model for the data.** An import
  receipt that needs to say anything in a group thread must call
  `execute_compose_group_message()`, full stop, matching its own docstring
  contract (§2.11). A raw source (the actual screenshot bytes, the email
  body) is never itself group-visible even when its *outcome* is — this
  mirrors TripIt's tiering (document attachments gated separately from the
  itinerary skeleton, §4.1) and Atlas's rule that `reflection` must be
  dropped from any hypothetical public projection (§2.5).
- **Graph-legibility applies to extraction, not just storage.** Per
  `docs/systems/graph-legibility-doctrine.md`'s two tests: a user pasting a
  link is a deliberately-authored signal (passes test 2) and the resulting
  place suggestion is a "show," not a "tell" — no "Vesper noticed you like
  X" chip should ever surface from an import; the felt result is just a
  better-curated Places list.
- **Money and public-share paths require explicit confirmation** — this is
  already a Content Generation charter invariant (§2.11) and applies
  directly: an imported booking or expense can never auto-write a
  confirmed state; it can only ever produce an `attest_external_handoff_
  completed` row (self-reported, not provider-confirmed) or a `needs_review`
  attention case, never a silent `confirmed` booking.
- **Wrong-trip / cross-trip leakage**: `inbound_items.trip_id` nullable-
  until-assigned (§7) is itself a privacy control, not just a UX
  convenience — an item shared before trip assignment must never be
  visible to any trip's members until a human assigns it.

## 9. Work-receipt specification and examples

The work-receipt doc (`docs/working/work-receipt-2026-07-26.md`) is a good
foundation and this report adopts its four-move anatomy and privacy rules
wholesale. Two critiques, both load-bearing for imports specifically:

1. **It never resolves durable vs. ephemeral, and imports need durable.**
   The doc's open-decisions list asks "should a receipt ever be durable...
   or does the trust-receipt ledger already cover that need?" For plan
   generation, ephemeral (a chat-turn reply) is fine because the user is
   present when it happens. For an import batch — someone shares 8 links
   at 11pm, the extraction runs in the background, and review happens the
   next morning — the receipt **must** be durable and revisitable, because
   the "return moment" the doc itself identifies as highest-value
   (*"the return moment is the highest-value placement... which is also
   what makes re-entry rewarding"*) is structurally guaranteed for imports
   in a way it isn't for a same-session plan reply. Recommendation: import
   receipts are always durable, stored as a `vesper_action_receipts` row
   (not the ephemeral chat-close variant), linked from `inbound_items
   .receipt_id`.
2. **It doesn't yet have a real second call site to prove the schema works
   outside the proposal path.** The direct-edit gap found in §2.11
   (`create_direct_edit_receipt` has zero callers) is a warning sign: a
   receipt schema that only one code path actually calls is at risk of
   silently rotting. An import receipt is a genuinely good second real
   consumer of `vesper_action_receipts` and should be built to actually
   exercise the `public_reasons`/`private_influences` split, not just cite
   it in a doc.

### Examples

**Successful link batch:**

> Organized the 6 restaurant links you shared. All 6 matched places already
> in Lisbon — added them to Places. Two were already saved from before, so
> nothing duplicated.

Receipt fields: `public_reasons=["6 links received", "6 resolved to
existing places", "2 already saved — skipped"]`, `promoted_refs.place_ids`
= 4 new saves, `status=approved` (auto-routed), audience=private (personal
save, no group action taken).

**Partial extraction:**

> Read the screenshot you sent — got the restaurant name and neighborhood,
> but couldn't make out the date. It's in Places; add the date whenever you
> have it.

`extraction_confidence=medium`, `extraction_warnings=["date field
unreadable"]`, `status=auto_routed` (place-shaped, low-stakes, no group
decision needed) but the receipt explicitly names what it didn't get —
per the doc's "no inferred flourishes" grounding rule.

**Duplicate detection:**

> The link you just shared is the same restaurant you saved on Tuesday from
> a different post — didn't add a second copy.

`content_hash` did not match (different source URL) but downstream entity
resolution matched the same `venue_id`; `status=dismissed` with
`failure_detail=null`, `public_reasons=["duplicate of existing save"]` —
this is a receipt for **not** acting, which the doc's move 3/4 explicitly
calls for.

**Booking import requiring private review:**

> Got your flight confirmation screenshot. Before I add it: confirm this is
> for the Lisbon trip, not the one in October — I see two upcoming trips
> and can't tell which from the image.

`audience=private` (booking content is never group-visible by default even
after approval, unless the user explicitly shares), `trip_id=NULL` pending
disambiguation, `status=needs_review`, `attention_case_id` set. This
receipt is a question, not a report — matching the brief's own "inputs that
belong to the wrong trip" scenario and TripIt's Unfiled Items precedent.

**Import that produces suggestions but no itinerary mutation:**

> Pulled 4 places out of the article you shared — they're in Places under
> Rome, not on your itinerary yet. Say the word if you want any of them
> scheduled.

`promoted_refs.place_ids` populated, `promoted_refs.proposal_id=null`,
explicit statement that no itinerary mutation happened — this is the
work-receipt doc's "what did it deliberately not change" move doing real
work.

**Import that changes a canonical itinerary after approval:**

> Added Thursday dinner at the place from your screenshot, right after the
> museum. Sent to the group as a proposal since it changes Thursday's plan.

This one does **not** stay in `inbound_items`'s own receipt — it hands off
to the existing proposal-created receipt
(`itinerary_proposal_gateway.py::_record_proposal_evidence`) with
`origin_channel` recording the import source, so there is exactly one
receipt for the itinerary change, not two competing ones. The import's own
receipt says "created a proposal from your screenshot" and links to the
proposal's receipt rather than duplicating its content — directly
implementing the trust-receipt-boundary decision's "stable references to
the changed artifact" rule (§2.11).

## 10. First vertical slice

**Recommendation: Share URL/text/screenshot → extract places → Places/
attention → receipt.** Not booking import; not a unified rewrite of the
Atlas photo-scan pipeline.

Reasoning, weighed against the other two candidates named in the brief:

- **vs. "Booking screenshot/email → private review → booking/itinerary →
  receipt":** booking import immediately hits money-adjacent rules
  (Content Generation charter's confirmation requirements),
  cross-trip-assignment ambiguity, and group-visibility edge cases on day
  one — higher stakes, more ways to ship something that erodes trust if
  wrong. It also depends on the harder, more expensive research bet
  (inbound email, or OAuth with the Gmail cost asymmetry from §4.2). Place
  import validates the riskiest *technical* unknown (mobile share capture)
  against the *lowest-stakes* content type.
- **vs. "Existing photo scan → unified artifact pipeline → receipt":** the
  Atlas photo-scan pipeline is private-memory-scoped by design and correctly
  so (§2.5) — folding it into a group-shaped ingestion table would be a
  regression, not a consolidation. There's no product reason to touch it
  first; it can adopt the receipt pattern later without needing the new
  `inbound_items` table at all.
- **Place import also forces the one blocking backend gap to get fixed
  regardless of what ships first**: the missing "create a provisional
  place" writer (§2.8, §5). That gap has to be closed before *any* import
  feature can promote an uncatalogued place, so building the place slice
  first means the hardest shared dependency gets built once, deliberately,
  instead of being rediscovered mid-implementation of a later slice.
- **It reuses the most infrastructure with the least new privacy surface**:
  `entity_saves`/Places is already a private-by-default, low-stakes write;
  the attention system is already mature; `group_compose` is only needed
  for the receipt text, not for the data itself (a place save has no
  inherent group dimension).

Scope for the first slice, concretely:

- Mobile: one new share-sheet target (Expo SDK 55 `expo-sharing`, dev
  client required) accepting URL or plain text only — **not images** in the
  first cut, to avoid the OCR/vision-extraction dependency entirely and
  ship the capture mechanism in isolation first.
- Backend: `inbound_items` table (§5) restricted to `source_kind IN
  (share_url, share_text)`; one new background job (Arq) that resolves the
  URL (server-side link resolution, not client-side parsing, per the Apple
  Maps finding in §4.2) and matches or creates a provisional place.
  Extraction is deterministic-first (URL → OpenGraph/canonical metadata),
  falling back to an LLM read of the page text only when metadata is
  insufficient — mirroring the receipt-OCR "omit what's not there" grounding
  rule (§2.7).
- Routing: single-place, high-confidence → auto-route to Places with a
  receipt. Multi-place or low-confidence → one `import_review` attention
  case.
- Receipt: durable `vesper_action_receipts` row per §9.

Screenshot ingestion (vision extraction) is the natural second slice —
it reuses everything from the first slice plus the existing chat-vision
mechanism (§2.1/§2.2), and can share the same `inbound_items` table and
routing rules without new schema.

## 11. Incremental migration plan

**Phase 0 — close the blocking gap (backend only, no user-visible
change).** ~~Two options (a) `venue_unlinked` cheap path vs (b) real
provisional-catalog concept~~ — **superseded: the founder ruled for the
debt-free posture on 2026-07-27; option (b) is the accepted design. See
§12.5 (Revision: debt-free build posture) for the binding version of this
phase and all phases below.** The original two-option framing is preserved
in §2.8's correction for provenance.

**Phase 1 — `inbound_items` table + URL/text share slice (§10).**
- Backend: new table + migration, one new background job, one new
  `attention_type` registry entry (`import_review`), extend `ActionChannel`
  with a `share`/`forward` value rather than inventing a parallel field.
- Mobile: Expo SDK 55 `expo-sharing` config plugin, dev client rebuild,
  `useIncomingShare()` wiring into a minimal capture screen (reuse the
  receipt-upload polling UX pattern from `useUploadReceipt.ts`, §2.10, for
  the "processing your share" state).
- Data migration: none — net-new table.
- API contract: new endpoints only (`POST /api/inbound-items`,
  `GET /api/inbound-items/{id}`); no existing contract changes.
- Privacy/authorization: `owner_id`-scoped like every other user-owned
  table in the codebase; no new privacy primitive needed (§8).
- Idempotency: `content_hash` unique index, `notification_dedup`-style
  claim table for the extraction job.
- Observability: reuse the OCR reaper pattern (§2.7) for stuck
  `extracting` rows; log `extraction_confidence` distribution from day one
  to calibrate the auto-route threshold before it's user-facing at scale.
- Device validation matrix: iOS share-from-Safari (has the documented
  JS-preprocessing contract, §4.2 — do this first, it's the highest-fidelity
  source, and confirm what arrives *without* the preprocessing file too,
  since that's the fallback for any host app that doesn't run it); iOS
  share-from-Apple-Maps (status is actively in flux per an unresolved
  Apple DTS thread, §4.2 — test on the actual iOS version the fleet is on
  rather than assuming either the old or new payload shape, and never let
  a missing coordinate silently fail — fall back to geocoding the place
  name); iOS share-from-Instagram/TikTok (strip tracking parameters and
  resolve the short link server-side before hashing, §4.2); Android
  share-from-Chrome (verify `EXTRA_TEXT` against Chromium's actual
  `text + " " + url` concatenation behavior, not a bare-URL assumption,
  §4.2); cold-launch-via-share (app not running) on both platforms; and a
  second-device/second-account pass only if any promoted object ever
  becomes group-visible (it doesn't in Phase 1).

**Phase 2 — screenshot ingestion.** Add `source_kind='share_image'` and
`chat_image`-sourced imports to the same table; reuse the existing chat-
vision extraction call (§2.1) as the extraction mechanism rather than
building a new one; add the batch/`batch_id` grouping (§7) since screenshots
are the modality most likely to contain multiple places.

**Phase 3 — booking import.** Only after Phases 1-2 have real usage data
on extraction confidence and review-completion rates (the work-receipt
doc's own "how we know it worked" instrumentation, §2.9's citation, applies
here too). Route confirmed writes through `attest_external_handoff_
completed` (§2.11) exclusively; decide the email-forwarding-vs-OAuth
question using §4.2's cost asymmetry (forwarding alias first; Gmail OAuth
only if forwarding proves insufficient, given the CASA cost).

**Explicitly out of scope for all three phases above** (see §12 for the
full non-goals list): PDF ingestion, full inbox OAuth, any new tab/screen
beyond what Places and the attention system already render, and any change
to Atlas's existing photo-scan pipeline.

## 12. Risks, unresolved questions, and explicit non-goals

**Unresolved questions (flagging missing evidence rather than assuming):**

- ~~**Which Phase 0 option to build is not decided here.**~~ **Decided
  2026-07-27: the provisional-catalog-row design (option b) is accepted —
  see §12.5.** The remaining open work from this bullet is now narrower:
  the corpus-filter audit (§12.5, Phase 0 scope) must enumerate every
  surface that reads venues/sites without a `verification_status` filter
  (Discover feed/search, planner search tools, editorial composition,
  Qdrant-indexed search) and add the filter — the Places charter's
  "asymmetric quality floor" (§2.5) becomes a status filter, not a gate
  that rejects provisional rows from existing.
- **Contradiction handling** (§7's "duplicate or contradictory sources" row)
  is named as unsolved, not solved — this report does not have a
  recommendation beyond "surface both, don't silently pick one."
- **Auto-route confidence threshold** is not calibrated — Phase 1's
  observability plan (§11) exists specifically because no data exists yet
  to set it correctly; shipping with an initially conservative threshold
  (bias toward `needs_review`) and tightening from real data is the
  recommended posture, not a specific number.
- **Whether Expo's experimental `expo-sharing` iOS mechanism will survive a
  future iOS release** is an open platform risk, not a design question —
  Expo's own docs flag it (§4.2). No amount of internal design mitigates
  this; it needs to be monitored against Expo's changelog.
- **Per-app share payloads are almost entirely undocumented by the source
  apps and confirmed version-fragile even where community-observed
  behavior exists** (Apple Maps' coordinate regression mid-rollback,
  Chrome's screenshot-in-`EXTRA_STREAM` behavior removed in 2015 but still
  cited in stale blog posts, Instagram's `igshid`→`igsh` rename). Do not
  hard-code assumptions about any single source app's payload shape;
  extraction must enumerate available type identifiers/extras and fall back
  gracefully (`public.url` → `public.plain-text` → regex-extract a URL from
  free text) rather than branching on one expected format. Budget an
  on-device "what did we actually receive" probe pass before writing the
  parser, not after.
- **Whether a group-visible import ever becomes necessary** (e.g., someone
  shares a link *into* a group planning conversation, not just to
  themselves) is not addressed by the Phase 1 scope, which is deliberately
  single-player. This is a real product question this report does not
  answer, only flags: does "sharing a link" ever need a `group_pending`
  audience state where a teammate's import shows up as a suggestion to the
  whole group before anyone approves it? The Phase 1 design supports this
  in the schema (`audience` enum already has `group_pending`) but nothing
  in this report designs the UX for it.

**Risks:**

- Building the mobile share extension is genuinely new native-module
  surface area for a codebase that has none today (§2.10) — treat the
  Phase 1 timeline as share-extension-risk-dominated, not
  backend-risk-dominated.
- The receipt-durability recommendation (§9) creates the second real
  consumer of `vesper_action_receipts`, which is good, but means any latent
  bug in that table's public/private split (untested by a second consumer
  until now) surfaces for the first time on import receipts.
- If Phase 1 ships with too aggressive an auto-route threshold, a wrong
  auto-routed place-save is low-stakes (personal Places list, easily
  removed) — this is a deliberate risk-scoping choice, not an oversight,
  and is exactly why booking import (higher-stakes wrong-auto-route) is
  Phase 3, not Phase 1.

**Explicit non-goals (do not build as part of this initiative):**

- A new Inbox tab, Trip Room, or generic activity feed — confirmed against
  the brief's own constraint and against Atlas's own reverted attempt at a
  generic review queue (§2.5).
- A polymorphic `attachments` table retrofitting the four existing bespoke
  attachment patterns (§2.9) — not worth the blast radius for the value.
- Full Gmail/Outlook inbox OAuth in the first three phases — the cost
  asymmetry in §4.2 argues for forwarding-alias first.
- PDF ingestion — no existing infrastructure touches PDFs anywhere in
  either repo; treat as a fully separate initiative if it's ever prioritized.
- Any change to the Atlas candidate/artifact pipeline's privacy scope —
  it should remain private-only; do not generalize it into the group-shaped
  `inbound_items` model.
- Reworking `docs/systems/proposals-change-studio.md`'s stale function
  names (§2.11) — flagged here because this research surfaced it, but it's
  a documentation-hygiene fix independent of the ingestion work.

## 12.5 Revision: debt-free build posture (accepted 2026-07-27)

> **This section supersedes §10's slice framing and §11's phasing where
> they conflict.** Context for the change: the founder reviewed the plan's
> debt profile and ruled that, pre-launch with no users and no
> compatibility constraints, the build should take the larger refactor and
> carry no deliberate dead-end states. Two band-aid risks identified in
> that review drove the redesign: (1) `venue_unlinked` imports would have
> no resolution/promotion path — the exact pattern that produced Atlas's
> permanent `atlas_kept_place` parallel-namespace debt (§2.5); (2) the
> same screenshot would get different guarantees depending on entry
> surface (share-sheet → envelope/review vs. chat → in-turn direct write,
> §2.3), a permanent behavioral fork.

### The structural center: imported places become real catalog rows

Extend `venues`/`sites` with `origin` (`curated | user_imported`) and
`verification_status` (`provisional | verified`), plus a
`merged_into_venue_id` resolution pointer. An imported place gets a real
row with a real id. Consequences, each of which removes a whole class of
special-casing:

- `entity_saves`, `itinerary_block_add`, and the map all work **unchanged**
  — the id resolves like any other. No ghost-block branch, no unlinked
  rendering mode for imports, no parallel save model.
- **Live status works**: the places linker already exposes
  `get_status_for_named_place(service, name, lat, lng)` (ad-hoc lazy
  provider discovery — `docs/systems/places.md`), so provisional rows can
  acquire real hours/open-now through the same machinery as curated
  venues.
- The corpus quality floor becomes a **filter, not a fork**: Discover,
  editorial surfaces, planner/global search, and Qdrant-backed retrieval
  filter to `verification_status='verified'`. Provisional rows surface
  only via explicit reference — the importer's saves, their trip's
  itinerary, import review. Phase 0 includes an audit of every
  venue/site-reading surface to install this filter.
- Resolution is a **merge**: provisional row later matched to an existing
  catalog venue → set `merged_into_venue_id`, re-point references. Genuinely
  new place → flip `verification_status`. No dead-end state exists.
- `itinerary_blocks.venue_unlinked` remains for its original purpose
  (planner name-only blocks) but **imports never write it**.
- Future (flagged, not scoped): Atlas's `atlas_kept_place` namespace
  (§2.5) gains a migration target for the first time.

### One extraction spine — chat is a capture surface, not a parallel path

Every structured extraction creates an `inbound_items` row regardless of
entry surface. A chat-uploaded booking screenshot keeps its conversational
in-turn reply, but the *write* routes through the envelope, and the user's
in-chat confirmation **is** the review action resolving the same state
machine the attention surface resolves — chat and the attention dropdown
are two review surfaces over one state. The existing in-turn
`trip_accommodation_set` direct-write flow (§2.3) is **migrated onto this
path in Phase 2, not preserved alongside it.**

### Storage and retention spec

Two layers, deliberately separated:

**Layer 1 — the envelope (`inbound_items` row): permanent, always.**
Created for every import and retained through every outcome including
`dismissed` and `failed` — dedup ("you already shared this and said no")
and receipt provenance ("which source supports this result") both require
rejection to be a record, not a deletion.

**Layer 2 — the raw payload, by type:**

| Input | Raw stored as | Where |
|---|---|---|
| Shared URL / text | Normalized string (tracking params stripped, §4.2) + small resolution snapshot (title, OG tags, canonical URL) | On the envelope row |
| Screenshot / shared image / chat image | Image bytes | S3 via the existing rehost path (perceptual-hash pipeline, §2.6) — `raw_ref` = key. Never Postgres, never local disk |
| Forwarded email (Phase 3) | Full parsed MIME, body + attachments | S3, `raw_ref` = key |

Deliberately **not** stored: full HTML of resolved pages (metadata snapshot
suffices; whole-page archiving is scraping/copyright liability with no
product use); any `PHAsset` reference for shared photos (no supported path
back to the library exists — §4.2; the received bytes are the artifact).

Why raw is kept at all: (1) re-extraction — stored sources can be re-run
through better extractors later; (2) trust and correction — "view
original" and "look again, that's wrong" require the original; (3)
verifiable dedup via `content_hash`.

Governance rules:

- **Raw payload is private to the importer, always** — even when the
  promoted result is group-visible. The group sees the outcome, never the
  source. (TripIt's two-tier pattern, §4.1, applied to a group context.)
- **Deleting the raw doesn't un-ring the bell**: promoted canonical
  objects remain (they are trip truth); the envelope survives as a
  tombstone so receipts degrade honestly ("source removed by owner")
  rather than dangling.
- **Account deletion cascades everything** — envelope, raw, S3 objects —
  through the existing RTBF path like any other user media.
- **Open question (Phase 3, do not default to keep-forever):** booking
  emails carry confirmation numbers, names, sometimes partial payment
  details — decide a bounded raw-MIME retention window (auto-purge raw
  after N days, retain envelope + extraction) before the email slice
  ships.

### Adjacent cleanup taken while it's free

- All import media through the S3 rehost path from day one; additionally,
  migrate chat images (§2.1) and expense receipts (§2.6) off local
  `/tmp`-style disk onto the same path — inherited storage debt that costs
  nearly nothing to fix pre-launch.
- The `audience` enum's speculative `group_pending` value (§5) is **cut**
  — added back only when the group-share import flow is actually designed.

### What debt-free deliberately does not mean

- No polymorphic `attachments` table — four bespoke FK columns with real
  DB constraints are sounder than one polymorphic table with none (§2.9's
  conclusion stands).
- No Gmail OAuth — a cost/compliance decision (§4.2), unchanged.
- Expo share-extension fragility (§4.2) is platform risk no refactor
  removes.
- Atlas's scan pipeline privacy scope is untouched.

### Revised roadmap (binding version)

- **Phase 0 — Place model:** `origin` + `verification_status` +
  `merged_into_venue_id` on venues/sites; corpus-filter audit + install
  across Discover/search/planner/Qdrant surfaces; provisional-place
  writer. Backend only.
- **Phase 1 — Capture + envelope:** `inbound_items`; Expo share extension
  (URL/text only); server-side resolution job (redirect-following +
  tracking-param normalization before `content_hash`); auto-route
  high-confidence single place to Places, else `import_review` attention
  case; durable `vesper_action_receipts` receipts.
- **Phase 2 — One extraction spine:** chat images become capture events on
  the envelope; migrate the booking-screenshot chat flow (chat reply as
  review surface); screenshot batches with per-batch attention cases;
  chat-image/receipt storage moves to S3.
- **Phase 3 — Booking email:** forwarding alias (per-user opaque alias on
  a dedicated subdomain) → envelope → the same extraction/resolution/
  routing spine Phases 1-2 already built → private review; decide the
  raw-MIME retention window before shipping. (Revised 2026-07-27, §12.7:
  the original text here named `attest_external_handoff_completed` as the
  write path — wrong premise, caught before implementation. That function
  is a manual self-report against a pre-existing "handed-off" itinerary
  block; a forwarded email has no such block to report against. §12.7 also
  documents the accommodation-routing fix this phase depends on.)

Honest cost statement: Phase 0 grows from days to a real workstream
(migration, corpus-filter audit across every venue-reading surface, merge
semantics), and Phase 2 migrates a tuned, working chat flow. That is the
price of no dead ends; pre-launch is the only cheap time to pay it.

## 12.6 Phase 2 concrete scope (drafted 2026-07-27, post Phase 1 device verification)

Phase 1 is shipped and device-verified (real Safari → share sheet →
`travel-app` → Places, real Postgres, real Haiku extraction — see the
Phase 1 commits: `travel-agent@859f93e7`, `29da1dde`; `travel-app@7ddc0204`,
`024deeaa`, `45d1b735`). That verification pass also surfaced two gaps
worth carrying forward as Phase 2 groundrules, not just Phase 1 fixes:
**an attention_case is not itself visible anywhere** —
`backend.notifications.delivery_spine.deliver()` is the only thing that
creates a `notification_deliveries` row the Activity feed actually reads —
and **an attention type's `default_destination` must be registered
explicitly** or it silently falls through to a contextless "open
concierge" tap target. Both apply again to whatever attention cases Phase
2's multi-candidate screenshots create.

This section makes §11's "screenshot ingestion" and §12.5's "one
extraction spine" concrete enough to build, at the same level of detail
Phase 0/1 got before implementation. It does not re-litigate the accepted
domain model (§5) or storage spec (§12.5) — both already scope this phase
correctly at the strategic level.

### Schema delta

`inbound_items` (Phase 1 migration `inbitem01`) needs, via a new Phase 2
migration:

- `raw_text` → **nullable**. An image share may carry no text at all (iOS
  share sheets pass an empty string, not null, for a captionless image
  share via `expo-share-intent` per §4.2 — normalize that to `NULL` at
  write time so "no caption" isn't confused with "empty string caption").
- `raw_ref TEXT NULL` — the S3 key for the rehosted image (§12.5's storage
  spec, Layer 2). Populated only for `share_image`/`chat_image` rows; the
  existing `content_hash` column already covers dedup (hash the image
  bytes, not the S3 key).
- `source_kind` CHECK constraint extended from `share_url | share_text` to
  add `share_image` (OS share sheet) and `chat_image` (migrated from the
  in-chat flow, §2.1/§2.3).
- `batch_id UUID NULL` + index — see "Open question: one candidate vs.
  many" below. Added now even though Phase 1 never populates it, so the
  migration doesn't need a second pass once the open question resolves.

`InboundItem` (`backend/core/models/inbound.py`) gains `raw_ref: str |
None` and `batch_id: UUID | None`; `raw_text` becomes `str | None`.
`InboundPlaceGuess` is unchanged — the vision extractor below still emits
the same shape, just possibly more than one per item.

### Mobile: image share capture

- `app.json`'s `expo-share-intent` plugin config (added in Phase 1,
  `travel-app@024deeaa`) currently sets only
  `NSExtensionActivationSupportsText` and the two `WebURL`/`WebPage`
  rules. Phase 2 adds `"NSExtensionActivationSupportsImageWithMaxCount":
  1` (single image only — multi-image share is an explicit non-goal
  below) and requires a `expo prebuild` + rebuild of the Share Extension
  target, same mechanism already proven working in Phase 1's device
  verification.
- `useShareIntent()`'s `shareIntent.files` array (README-documented shape:
  `{path, mimeType, fileName, size, width, height}`, confirmed in Phase
  1's package research) carries the image instead of `webUrl`/`text`.
  `components/sharing/ShareIntentHandler.tsx` (Phase 1,
  `travel-app@024deeaa`) branches on `shareIntent.files?.length` before
  falling back to its current `webUrl ?? text` check, and needs to read
  the file at `path` (a local `file://` URI in the share extension's App
  Group container) and base64-encode it — the same `expo-file-system`
  pattern `ComposerBar.tsx:294-406` (§2.1) already uses for chat image
  attachments, not a new file-reading mechanism.
- `/share-capture` (`app/share-capture/index.tsx`, Phase 1) gains an
  image-submit path alongside its existing `raw_text`/`item_id` params —
  submits base64 + mime type instead of `raw_text`. The existing
  submit → poll → terminal-state UI shape (§ Step 2 of the Phase 1 plan)
  is reused as-is; only the submit payload changes.
- Chat's existing image-attachment path (`ComposerBar.tsx`, §2.1) is
  **not** touched in the capture UI sense — it keeps working exactly as
  today. What changes is what happens server-side once an image lands in
  a turn where the model would have called `trip_accommodation_set`
  directly (see "Migrating the booking-screenshot flow" below).

### Backend: vision extraction, reusing the receipt-OCR shape

Phase 1's `backend/inbound/extraction.py::extract_place_guess` is
text-only (`call_llm_json`, no image content block — confirmed by
reading the current file). It cannot be reused as-is for images;
`call_llm_json`'s signature (`backend/core/llm.py:771`) takes `user: str |
RenderedPrompt`, not a multi-part message list, so it structurally cannot
carry an image block. The receipt-OCR pipeline
(`backend/expenses/receipt_ocr.py::extract_receipt_data`, lines 55-121,
already cited in §2.7) calls the lower-level `call_llm(...)` directly with
an explicit `messages=[{"role": "user", "content": [{"type": "image", ...},
{"type": "text", ...}]}]` — **this is the function signature Phase 2's
image extractor must follow**, not `call_llm_json`.

Concretely: a new `backend/inbound/extraction.py::extract_place_guesses_from_image`
(plural — see below), same file as the existing text extractor, following
`extract_receipt_data`'s exact `call_llm` invocation shape (base64 image
block + text instruction, `surface_key="vesper.inbound.place_extraction_image"`
— a new `SurfaceRegistry` entry, `backend/core/surfaces/definitions.py`,
alongside Phase 1's `vesper.inbound.place_extraction`), parses a JSON
**array** of the same `InboundPlaceGuess` shape rather than a single
object, and keeps the identical grounding rule from Phase 1's prompt
("omit what you cannot determine, never invent a city or coordinates") —
that instruction is content-type-agnostic and should not fork between the
text and image extractors.

Storage reuses the S3 rehost machinery (`backend/media/rehost.py`,
`backend/media/hashing.py::perceptual_hash`, `backend/media/variants.py`,
`backend/media/storage.py::upload_all`, all cited in §2.6/§12.5) but
**not** `rehost.py`'s own top-level orchestrator function, which assumes a
source URL to download (its module docstring: "turn a source URL into a
PhotoRecord... 1. download source bytes"). Phase 2's bytes arrive already
decoded from the mobile client (base64 in the POST body, matching
`MessageImage`'s existing 2.5MB base64 convention from §2.1 — not
multipart, for consistency with the rest of this endpoint's request
shape). The new worker step decodes, computes `perceptual_hash` for
`content_hash`, generates variants, and calls `upload_all` directly —
skipping only the "fetch from URL" step, reusing everything else.
`raw_ref` on the `inbound_items` row is the resulting S3 key.

The extraction call and the S3 rehost are independent of each other (one
needs the bytes for a vision call, the other needs them for permanent
storage) and should run concurrently in `_run_pipeline`
(`backend/workers/inbound_jobs.py`), not sequentially — matching the
existing function's `asyncio`-based shape.

### Migrating the booking-screenshot chat flow

§2.3's current path (`_prompts_skills.py:1806-1815` instructs the model to
read a booking image and call `trip_accommodation_set` directly,
synchronous, no job queue, no structured review) is the one piece of
existing, tuned, working behavior this phase migrates rather than adds
net-new. Concretely: the prompt instruction changes from "call
`trip_accommodation_set`" to "call a new tool that creates an
`inbound_items` row with `source_kind='chat_image'`, `origin_channel`
distinguishing it from a share-sheet import" — and the model's existing
in-turn "recite back what I read" reply becomes the review surface (per
§12.5's "chat and the attention dropdown are two review surfaces over one
state"), rather than the write happening synchronously off the recitation.
This is a `ToolEffect`/`ConfirmationPolicy` change in
`backend/concierge/tool_contracts.py` (currently `COMMIT` +
`TRIP_EDIT_POLICY`, cited §2.3) and a new tool handler alongside
`backend/concierge/tool_handlers/accommodations.py`, not a prompt-only
change — flagged here as a real migration cost, not a copy-paste.

### Open question: one candidate vs. many (not resolved here)

A screenshot can show one place (a single restaurant's Instagram post) or
many (a "Top 10" listicle screenshot, a Google Maps saved-list screenshot).
`extracted_candidates` is already a JSONB array on the `inbound_items` row
(Phase 1 schema), so the array itself needs no schema change to hold
multiple guesses. What's unresolved is **attention_case cardinality**:
one `attention_case` per inbound_item covering all candidates together
(simpler; matches the existing `uq_attention_cases_subject_recipient`
constraint on `(attention_type, subject_type, subject_id, recipient_id)`
with `subject_id = str(item_id)` unchanged from Phase 1), versus one case
per candidate (finer-grained review — dismiss the three you don't
recognize, keep the one you do — but requires `subject_id` to encode a
candidate index, e.g. `f"{item_id}:{i}"`, and the `batch_id` column above
exists specifically to let those per-candidate cases still group for a
single "3 more places from that screenshot" Activity summary). This
report added the `batch_id` column so either answer is buildable without
a second migration, but does not pick one — it's a product call about how
Activity should feel with a multi-place screenshot, not an engineering
constraint.

### Non-goals (Phase 2, explicit)

- Multi-image share (one screenshot at a time — `NSExtensionActivationSupportsImageWithMaxCount: 1`, matching this phase's own activation rule above).
- PDF/document screenshots (itinerary PDFs, boarding passes) — image only.
- Any change to Atlas's own photo-scan pipeline (§2.5) — this is a
  structurally separate system by design (client-side clustering, no
  server vision call, `atlas_kept_place` namespace) and §12.5 already
  rules out merging them.
- Video (Instagram Reels/TikTok often share as video, not image, on iOS —
  `expo-share-intent`'s Movie activation rule is a separate, unimplemented
  capability; a shared video with no frame extraction produces nothing
  usable today and should fail closed with an honest "can't read video
  yet" message rather than a silent no-op).

## 12.7 Phase 3 concrete scope (drafted 2026-07-27, post accommodation-routing fix)

### Prerequisite correction, already shipped

Researching this section surfaced a real regression in Phase 2's already-
shipped chat-flow migration: `_run_pipeline`/`_run_image_pipeline`
(`backend/workers/inbound_jobs.py`) auto-routed every high-confidence
candidate — hotel confirmations included — through the generic
`save_entity` Place write, so a migrated booking screenshot lost its
check-in/check-out dates entirely (the old direct `trip_accommodation_set`
chat path, §2.3, never had this problem — it wrote a real
`trip_accommodations` row). Left unfixed, Phase 3 would have inherited and
compounded the same loss for every emailed hotel confirmation.

Fixed ahead of Phase 3 proper: `InboundPlaceGuess` gained optional
`arrival_date`/`departure_date` (`backend/core/models/inbound.py`),
populated by both extraction prompts only when the source states them
explicitly (never inferred — same grounding discipline as the rest of
this pipeline). A new shared `_promote_confirmed_candidate` helper in
`inbound_jobs.py` now decides, for every high-confidence auto-route
(URL/text, screenshot, and — once shipped — email alike): if the
candidate's `venue_or_site_type` is lodging (`hotel | hostel | apartment |
resort`) **and** the item has a `trip_id`, write via
`create_accommodation` (`backend/core/db/trip_accommodations.py`) instead
of `save_entity`, using the guess's own dates or falling back to the
trip's `start_date`/`end_date`. Two defaults for this write were the
author's own reasoned extension of the "type-aware" decision, not
separately confirmed: `is_primary=False` (an unattended background job
must never silently reclaim a trip's primary stay) and
`visibility="private"` (an import defaults to owner-only, matching this
app's existing privacy-by-default posture for GPS-derived stays — the
user can reshare it to the group from the stay screen same as any other
personal stay). When neither the guess nor the trip supplies both dates,
the write falls back to the generic Place save rather than failing the
item — a hotel saved as a plain Place is a graceful degradation, not a
lost import. Covered by new tests in `tests/workers/test_inbound_jobs.py`
and `test_inbound_jobs_image.py` (dates from extraction, dates from trip
fallback, no dates anywhere, no `trip_id` — each exercising the shared
helper directly).

Consequence for this section: **Phase 3 needs no separate accommodation-
routing work.** Any email that resolves to a single high-confidence
lodging candidate with a `trip_id` gets a real stay for free, through the
same helper Phases 1-2 already exercise.

### Provider: SendGrid Inbound Parse

Chosen over building a raw MX-record + SMTP-receiver stack: Inbound Parse
terminates SMTP, parses the MIME message server-side, and POSTs the
result as a normal `multipart/form-data` request to a webhook URL — `to`,
`from`, `subject`, `text`, `html`, `envelope` (JSON, the raw SMTP
envelope), `attachments` (a count) plus one `attachment1`, `attachment2`,
... file field per attachment. No MIME-parsing library needed on our
side; the route handler reads form fields like any other multipart
upload. Setup is entirely in SendGrid's own dashboard (a domain/subdomain
→ webhook-URL mapping) plus one MX record on our side — there is no API
call that provisions it.

### Per-user opaque alias

New `user_email_aliases` table, migration alongside this phase:

```
id            uuid primary key
user_id       uuid not null references users(id) on delete cascade
alias_token   text not null unique   -- secrets.token_urlsafe(16)
created_at    timestamptz not null default now()
retired_at    timestamptz            -- null = active
```

One active alias per user, enforced the same way
`trip_accommodations.is_primary` enforces one active primary stay: a
partial unique index `ON user_email_aliases (user_id) WHERE retired_at IS
NULL`, not an application-level check — rotation (a leaked/spam-flooded
alias) retires the old row and inserts a new one in the same transaction,
mirroring `create_accommodation`'s retire-then-insert shape.

Token generation follows `trip_invites.py`/`trip_story_shares.py`'s exact
pattern: `secrets.token_urlsafe(16)`, DB unique constraint as the
collision backstop (no pre-check query). The alias address itself is
`{alias_token}@import.<app-domain>` — Inbound Parse binds to a whole
(sub)domain's MX record and forwards *every* address under it to one
webhook, so the token must live in the local part, not the domain; the
webhook resolves the recipient by parsing `to` out of the form body, not
by any header SendGrid signs.

### Webhook route

`POST /api/inbound-email/sendgrid/{webhook_secret}` (`backend/api/routes/`,
new file) — `# noauth:` (matching the convention already used across
`backend/api/routes/*.py` for provider-callback endpoints, e.g.
`revenuecat_webhooks.py`), rate-limited by client IP
(`backend/api/rate_limits.py`'s noauth-endpoint helper) rather than by
user, since there is no authenticated user on the request.

Inbound Parse has no per-request signature scheme (unlike RevenueCat's
`X-RevenueCat-Webhook-Signature` or Twilio/Bland's HMAC header, both
already patterns in this codebase) unless SendGrid's separate "Signed
Webhooks" feature is layered on top of a *different* SendGrid product —
Inbound Parse's own documented recommendation is a secret embedded in the
callback URL itself. Hence the `{webhook_secret}` path segment: a single
long random value from an env var, compared with `secrets.compare_digest`,
rejecting (secure-by-default) if the env var is unset — the same
fail-closed posture already established for Twilio/Bland verification in
this codebase, applied to a provider that only offers a URL-secret rather
than a header HMAC.

Handler shape:

1. Verify the path secret; reject early on mismatch.
2. Parse the multipart form: `to` (extract `alias_token` from the local
   part), `from`, `subject`, `text` (fall back to a stripped-tags version
   of `html` if `text` is empty — plenty of transactional booking emails
   are HTML-only).
3. Look up `user_email_aliases` by token; unknown/retired token → `202`
   (accept-and-drop, never bounce or leak which tokens are valid to an
   arbitrary SMTP sender).
4. Enforce a body size cap (reject oversized requests before reading the
   full multipart body into memory — matching the size-guard discipline
   already applied to the Phase 2 image-submission route).
5. Create an `inbound_items` row: `source_kind="email_forward"`,
   `owner_id` = the alias's user, `trip_id=NULL` (no trip context exists
   at forward time — see non-goals), `raw_text` = `subject` + blank line +
   body text, `content_hash` over that same string (a resend of the exact
   same email is deduped like any other re-share).
6. Store the full raw MIME (`envelope` + all parts, not just the parsed
   text) to S3 via the existing rehost path, `raw_ref` = key — per §12.5's
   Layer 2 spec, which already named this row in its table before this
   section existed.
7. Enqueue `process_inbound_item` exactly as Phases 1-2 do. No new job
   function: extraction dispatches on `source_kind`, and
   `source_kind="email_forward"` reuses the existing **text** extraction
   path (`extract_place_guess`) unchanged — booking confirmation emails
   from Booking.com/Airbnb/hotel direct-booking systems are structured
   HTML/text, not screenshots, so Phase 2's vision pipeline is not on the
   critical path here. `arrival_date`/`departure_date` extraction (this
   section's prerequisite fix) already applies to text extraction — a
   forwarded hotel confirmation gets dated stays without any further
   change once the fix above shipped.

### Why `trip_id` stays NULL at forward time (and what that costs)

Forwarding an email happens outside the app entirely — there is no
in-context "which trip is this for" the way a share-sheet import at least
has a foregrounded app to ask. Auto-attributing the trip by date-range
overlap (the extracted stay's dates against the user's active trips) is a
plausible future heuristic but is **out of scope for this phase** — it
would need to handle the ambiguous-overlap case (two trips, same window)
and is a product decision about how confident a guess needs to be before
silently attaching to a trip. Concretely, this means: even with the
accommodation-routing fix, an emailed hotel confirmation with no
`trip_id` still lands as a generic Place with an `import_review`
attention case, exactly like the pre-fix behavior — dates are extracted
and preserved in `extracted_candidates` (visible to the reviewer, and
available to whatever attaches the trip on approval) but not written to
`trip_accommodations` until a trip is known. Assigning the item to a trip
from the review surface is the same interaction as approving any other
`needs_review` item; no new UI is required for it to be *possible*, but
nothing in this phase makes it *convenient* (e.g. no "which trip?"
picker surfaced automatically) — flagged honestly as a rough edge, not
silently absorbed.

### Raw-MIME retention window

§12.5 flagged this as an open question to resolve before shipping, given
booking emails carry confirmation numbers and sometimes partial payment
detail. Decision: 30-day retention for the raw MIME S3 object, matching
this codebase's existing pattern for other short-lived sensitive raw
media (chat image originals) rather than inventing a new retention tier.
A scheduled purge job deletes the S3 object and clears `raw_ref` to NULL
after 30 days; the `inbound_items` envelope row, `extracted_candidates`,
and any promoted `trip_accommodations`/Place row are permanent per
§12.5's Layer 1 spec — only the raw source degrades, and it degrades to
an honest "source removed" state (§12.5's existing governance rule for
raw-payload deletion), not a dangling reference.

### The external dependency this report cannot close

Two things exist entirely outside this codebase and this session's
access: (1) a DNS MX record for the chosen subdomain (e.g.
`import.<app-domain>`) pointed at SendGrid's Inbound Parse mail servers —
requires the domain registrar/DNS provider the founder controls; (2) the
SendGrid account's own Inbound Parse dashboard configuration mapping that
subdomain to the webhook URL. Both are one-time, non-engineering setup
steps, but code-complete does not mean live: this phase's implementation
can be finished, tested (a synthetic multipart POST exercising the
webhook route directly, same spirit as this codebase's other webhook
tests), and merged, while real end-to-end "forward an email, see it show
up" verification stays blocked until those two steps happen — mirroring
exactly how Phase 1 Step 3's real-device share-sheet verification was
scoped and reported rather than assumed.

### Non-goals (Phase 3, explicit)

- Attachment/screenshot parsing within a forwarded email (a boarding pass
  PDF, a hotel confirmation sent as an image attachment rather than HTML
  body) — text body only this phase; §11's Phase 2 vision pipeline is
  reusable later but is not wired to the email path now.
- Automatic trip attribution by date-range overlap — see above.
- Multiple simultaneous active aliases per user, or a self-serve rotation
  UI — the schema supports rotation; no UI surfaces it yet.
- Calendar `.ics` attachment parsing.
- Bounce/delivery-failure handling back to the original sender — Inbound
  Parse is receive-only for this use; we never reply.
- Gmail/Outlook OAuth forwarding-rule automation — unchanged from §12.5's
  existing "no Gmail OAuth" non-goal; the user forwards manually.

## 13. Code references and web sources

### Code (all paths under `/Users/feihuyan/travel-workspace/`)

**Ingestion entry points:** `travel-agent/backend/api/routes/conversations.py:1209,1344,261-306`; `travel-agent/backend/api/routes/chat.py:86-111,281-298,439-458`; `travel-agent/backend/core/db/chat_images.py:63-116`; `travel-agent/backend/core/db/_tables/conversations.py:42-77`; `travel-agent/backend/concierge/agent.py:660-673`; `travel-agent/backend/concierge/session.py:1093-1114`; `travel-agent/backend/concierge/vision_summary.py:73-132`; `travel-agent/backend/concierge/_prompts_skills.py:1806-1815`; `travel-agent/backend/concierge/tool_handlers/accommodations.py:15-56,59+`; `travel-agent/backend/core/db/_tables/users.py:200-284`; `travel-agent/backend/concierge/tool_contracts.py:241-249`; `travel-agent/backend/concierge/tool_handlers/web_search.py:10-14`.

**Atlas candidate/artifact pipeline:** `travel-agent/backend/core/db/_tables/atlas.py:53-316,477-539`; `travel-agent/backend/core/db/_tables/atlas_artifact_photos.py`; `travel-agent/backend/core/db/atlas.py:60-180,1361-1391`; `travel-agent/backend/api/routes/atlas.py:1078-1428,1660-1796,1828+,1906+`; `travel-agent/backend/atlas/clustering.py:1-99`; `travel-agent/backend/atlas/composer.py:43-437`; `travel-agent/backend/atlas/trip_link.py:83-87`; `travel-agent/backend/atlas/kept_place_affinity.py:12-114`; `travel-agent/backend/atlas/significance.py`; `travel-agent/backend/atlas/discovery_reflection.py`; `travel-agent/backend/atlas/timeline_enrich.py:34-49`; `travel-agent/backend/atlas/artifact_acceptance.py:12-14`; `travel-agent/backend/api/routes/atlas_unpacked_landing.py:8-12,60-168`.

**Uploads/media/jobs:** `travel-agent/backend/api/routes/trip_photos.py:59-209`; `travel-agent/backend/media/rehost.py:48,118,276-302`; `travel-agent/backend/media/hashing.py:25`; `travel-agent/backend/core/models/photos.py:112`; `travel-agent/backend/api/routes/expenses.py:1593-1687,1761-1787`; `travel-agent/backend/core/job_queue.py:1-71`; `travel-agent/backend/workers/ocr_jobs.py:22-24,60-203`; `travel-agent/backend/expenses/receipt_ocr.py:39-121`; `travel-agent/backend/api/lifecycle.py` (`_run_ocr_reaper_loop`, ~1150).

**Place/booking writers:** `travel-agent/backend/core/db/saves.py:23-45`; `travel-agent/backend/api/routes/saves.py:34-55`; `travel-agent/backend/core/db/_tables/social.py:173-201`; `travel-agent/backend/concierge/tool_handlers/itinerary_edit.py:945-1052`; `travel-agent/backend/core/booking_attestation_gateway.py:1-65`; `travel-agent/backend/api/routes/trips.py:1489-1569`; `travel-agent/backend/core/db/_tables/booking.py:41-68`.

**Proposal gateway, attention, receipts, privacy:** `travel-agent/backend/core/itinerary_proposal_gateway.py:138-178,395,532-588`; `travel-agent/backend/core/itinerary_proposal_producer.py:35-533`; `travel-agent/backend/core/models/itinerary_operations.py:167-173,1213`; `travel-agent/backend/core/db/_tables/itinerary.py:480-483`; `travel-agent/backend/core/itinerary_operation_preview.py:33,68,100-116`; `travel-agent/backend/core/itinerary_commit_gateway.py:137-585`; `travel-agent/backend/api/routes/itinerary_operations.py:137-218`; `travel-agent/backend/core/db/_tables/notifications.py:190-258`; `travel-agent/backend/core/attention_type_registry.py:108-512`; `travel-agent/backend/api/routes/_notifications_feed.py:362-594`; `travel-agent/backend/api/services/notification_feed.py:18`; `travel-agent/backend/core/db/_tables/action_receipts.py:18-94`; `travel-agent/backend/core/db/action_receipts.py:43,85-138`; `travel-agent/backend/concierge/group_compose.py:210,467-1461`; `travel-agent/backend/core/db/notification_dedup.py:1-39`.

**Mobile:** `travel-app/app.json:38-63`; `travel-app/ios/TravelApp/Info.plist:25-30`; `travel-app/components/chat/ComposerBar.tsx:34-406`; `travel-app/components/chat/composerAddCapabilities.ts:4-32`; `travel-app/components/expense/AddExpenseSheet.tsx:357-403`; `travel-app/hooks/useUploadReceipt.ts:60-219`; `travel-app/utils/imageUploadGuard.ts:147-153`; `travel-app/app/atlas/scan.tsx:242-518`; `travel-app/app/atlas/candidate/[id].tsx:65-305`; `travel-app/app/atlas/inbox.tsx:5-218`; `travel-app/components/places/PlacesWorkspace.tsx:14-154`; `travel-app/components/search/UniversalSearchOverlay.tsx`; `travel-app/app/invite-code.tsx:37-80`; `travel-app/utils/inviteToken.ts`; `travel-app/types/notification.ts:98`; `travel-app/hooks/useNotificationActivity.ts:12-114`; `travel-app/app/notifications/index.tsx`.

**Workspace charters and decisions read in full:** `docs/systems/atlas.md`, `docs/systems/places.md`, `docs/systems/trips-folio.md`, `docs/systems/proposals-change-studio.md` (stale — see §2.11), `docs/systems/group-social.md`, `docs/systems/content-generation.md`, `docs/systems/graph-legibility-doctrine.md`, `docs/decisions/2026-07-09-trust-receipt-boundary.md`, `docs/decisions/2026-07-25-attention-identity-and-type-registry.md`, `docs/working/notification-attention-architecture-roadmap-2026-07.md`, `docs/working/global-navigation-ia-proposal-2026-07-25.md`, `docs/working/work-receipt-2026-07-26.md`.

### Web (official sources, cited inline above; consolidated here)

- Mindtrip: [App Store listing](https://apps.apple.com/us/app/mindtrip-ai-travel-companion/id6503107567); [mindtrip.ai](https://mindtrip.ai/); [PR Newswire, 2024-07-31](https://www.prnewswire.com/news-releases/mindtrip-launches-start-anywhere-a-powerful-new-way-to-build-travel-itineraries-from-any-point-of-inspiration-302210025.html)
- Wanderlog: [forwarding help, ~2022-03-10](https://help.wanderlog.com/hc/en-us/articles/4625693334811-Add-flight-hotel-and-rental-car-details-by-forwarding-an-email); [Gmail import, ~2023-02-28](https://help.wanderlog.com/hc/en-us/articles/13302942899099-Is-it-safe-to-connect-my-Gmail-account-to-Wanderlog); [extension](https://wanderlog.com/extension); [sharing](https://help.wanderlog.com/hc/en-us/articles/4625495771163-Add-friends-to-plan-together)
- TripIt: [adding travel plans](https://help.tripit.com/en/support/solutions/articles/103000063275-adding-travel-plans-to-tripit); [Unfiled Items](https://help.tripit.com/en/support/solutions/articles/103000063393-unfiled-items); [Apple Intelligence](https://help.tripit.com/en/support/solutions/articles/103000361047-tripit-pro-and-apple-intelligence); [documents](https://help.tripit.com/en/support/solutions/articles/103000063361-add-documents-to-a-trip); [attachments not supported via email](https://help.tripit.com/en/support/solutions/articles/103000063327-problem-with-your-tripit-submission); [Inbox Sync](https://help.tripit.com/en/support/solutions/articles/103000063336-authorizing-inbox-sync); [sharing/privacy](https://help.tripit.com/en/support/solutions/articles/103000063367-trip-sharing-from-our-website); [privacy](https://help.tripit.com/en/support/solutions/articles/103000063426-trip-privacy)
- Google Maps: [Lists help](https://support.google.com/maps/answer/7280933); [computer version](https://support.google.com/maps/answer/7546473); [Google Blog, 2023-11-15](https://blog.google/products/maps/google-maps-updates-november-2023/); [My Maps import](https://support.google.com/mymaps/answer/3024836)
- Partiful: [app download](https://help.partiful.com/hc/en-us/articles/27354346663963-Do-my-guests-need-to-download-the-app); [RSVP](https://help.partiful.com/hc/en-us/articles/34230743189787-How-do-I-RSVP-to-an-event-on-Partiful); [inviting without contact info](https://help.partiful.com/hc/en-us/articles/28140825325595-Do-I-need-to-have-my-guests-phone-numbers-or-emails-in-order-to-invite-them-to-a-Partiful-event); [why use Partiful](https://help.partiful.com/hc/en-us/articles/26526377667739-Why-use-Partiful)
- Other apps: [Layla App Store](https://apps.apple.com/us/app/layla-ai-trip-planner/id6758730467); [Stashed](https://apps.apple.com/us/app/stashed-save-tiktok-places/id6747645573); [Plotline](https://apps.apple.com/md/app/plotline-travel-map-planner/id6759443026)
- iOS platform: [App Extension Programming Guide: Share](https://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/Share.html); [Extension Overview](https://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/ExtensionOverview.html); [App Extension Keys](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/AppExtensionKeys.html); [Handling Common Scenarios](https://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/ExtensionScenarios.html); [Developer Forums: launching app from extension](https://developer.apple.com/forums/thread/773342); [Developer Forums: memory limits](https://developer.apple.com/forums/thread/763392); [jetsam event reports](https://developer.apple.com/documentation/xcode/identifying-high-memory-use-with-jetsam-event-reports); [background downloads](https://developer.apple.com/documentation/Foundation/downloading-files-in-the-background); [beginBackgroundTask](https://developer.apple.com/documentation/uikit/uiapplication/beginbackgroundtask(expirationhandler:)); [BGTaskScheduler](https://developer.apple.com/documentation/backgroundtasks/bgtaskscheduler); [App Groups config](https://developer.apple.com/documentation/Xcode/configuring-app-groups); [Apple Maps share forum reports](https://developer.apple.com/forums/thread/792298); [MailKit](https://developer.apple.com/documentation/mailkit/build-mail-app-extensions); [location metadata](https://support.apple.com/guide/personal-safety/manage-location-metadata-in-photos-ips0d7a5df82/web)
- Android platform: [Receive simple data](https://developer.android.com/training/sharing/receive); [grant-uri-permission](https://developer.android.com/guide/topics/manifest/grant-uri-permission-element); [foreground service types](https://developer.android.com/about/versions/14/changes/fgs-types-required); [data transfer migration](https://developer.android.com/about/versions/15/changes/datasync-migration); [background work](https://developer.android.com/develop/background-work/background-tasks/persistent/getting-started/define-work)
- Expo: [SDK 55 changelog](https://expo.dev/changelog/sdk-55); [SDK 55 beta changelog](https://expo.dev/changelog/sdk-55-beta); [expo-sharing docs](https://docs.expo.dev/versions/latest/sdk/sharing/); [App extensions](https://docs.expo.dev/build-reference/app-extensions/); [expo-share-intent](https://github.com/achorein/expo-share-intent); [expo-share-extension](https://github.com/MaxAst/expo-share-extension)
- Inbound email: [SendGrid Inbound Parse](https://www.twilio.com/docs/sendgrid/for-developers/parsing-email/setting-up-the-inbound-parse-webhook); [SendGrid Inbound Email](https://www.twilio.com/docs/sendgrid/for-developers/parsing-email/inbound-email); [Mailgun Routes](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/routes); [Mailgun receive/store](https://documentation.mailgun.com/docs/mailgun/user-manual/receive-forward-store/receive-http); [Postmark inbound](https://postmarkapp.com/developer/user-guide/inbound); [Postmark webhook](https://postmarkapp.com/developer/webhooks/inbound-webhook); [AWS SES receiving](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-concepts.html)
- OAuth: [Google restricted scopes](https://support.google.com/cloud/answer/13464325); [Gmail API scopes](https://developers.google.com/workspace/gmail/api/auth/scopes); [Google restricted scope verification](https://developers.google.com/identity/protocols/oauth2/production-readiness/restricted-scope-verification); [Google Cloud Console FAQ](https://support.google.com/cloud/answer/13463817); [Microsoft Graph permissions](https://learn.microsoft.com/en-us/graph/permissions-reference); [Microsoft publisher verification](https://learn.microsoft.com/en-us/entra/identity-platform/publisher-verification-overview); [Microsoft 365 App Certification](https://learn.microsoft.com/en-us/microsoft-365-app-certification/overview)

## Exit

Before 2026-08-26, choose one: promote the accepted build posture (§12.5 —
the binding version of the domain model and phasing, superseding §10/§11
where they conflict) into a decision record and a
`docs/systems/ingestion.md` charter as implementation begins; or archive
this as point-in-time research if priorities shift elsewhere before then. Either way, the `docs/systems/proposals-change-studio.md` staleness
found in §2.11 should get its own correction pass independent of whether
this initiative proceeds.
