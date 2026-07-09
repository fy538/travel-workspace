# Vesper — Content Contracts Audit

**Date:** 2026-07-08 · **Scope:** `travel-agent` (generation) + `travel-app` (render) · **Mode:** investigation only, no code changed.

This audit inventories every LLM-generated field that reaches the UI and grades it against the five Content-Contract principles (Separation, Containment, Legibility, Reversibility, Restraint), the 7-part per-field contract, and the "never model-authored" list. Findings are grounded in `file:line` reads of real prompt strings and component source. Where a repo area was large it was sampled and noted.

## Method

The backbone is `backend/core/surfaces/definitions.py` — a 75-entry `SurfaceDefinition` catalog that already indexes every LLM (and deliberately no-LLM) surface with a `generator="file:line"` reference and an `experience_type`. The audit covered the **user-facing** experience types (`LIVE`, `CACHED_ON_REQUEST`, `PREGEN_EVENT`, `HUMAN_GATED`) end-to-end (prompt → data path → render → contract), sampled the `INTERNAL_SIGNAL` surfaces that can leak to the UI (guards, classifiers), and traced the shared contract infrastructure. Six domain sweeps + a shared-infrastructure pass fed this synthesis.

---

## 1. Contract infrastructure — what already exists

There is a **real, partial implementation of this very contract**, which is the right foundation to extend:

- **§5 Restraint (length) — mature but partial.** `backend/core/content_contract.py` provides `FieldBudget`, `clamp_text` (word-boundary truncate + single-char ellipsis), `clamp_fields`, `prompt_guidance`, and a `CONTRACTS` registry of 11 named contracts. FE mirror `travel-app/constants/contentContract.ts` (`clampText`/`clampFields`/`CONTRACTS`) is kept in lockstep by tests on both sides. `core/cards/contract.py` re-exports the card entry.
  - **Registered + wired:** home_card, home_card_rail, itinerary_block, change_proposal, trip_hero, atlas_dna, concierge_lead_note, home_anchor_voice, recommendation, deck_judgment, invite_snapshot — clamp is actually called at `home/trip_note.py:226/272`, `home/compose.py:139`, `home/pick_judgment.py:162-181`, `home/concierge_feed.py:284/383-386`, `core/models/recommendation.py:66-72`, `concierge/invite_snapshot.py`.
  - **Not registered → zero length governance:** trip story (hero/subtitle/body), narration (live + prerender), takes body/caveats, all four digests, cross-trip thread, Atlas artifact/almanac/timeline/home-letter (raw slices, not clamp), discover synthesis, lookup answer, angle why-for-you, reflection, notes journal/member-brief, personal 1:1 chat reply.
  - **Key limitation:** the primitive governs **length only**. `guidance()` injects target/max chars but says nothing about facts-only / do-not-invent.

- **`call_llm` chokepoint — `backend/core/llm.py:251`.** Every surface routes through it (resolves model, honors `DISABLED_SURFACES` kill switch `:207-233`, `max_tokens` = token budget, A/B). It enforces **no** char budget, **no** confidence gate, and injects **no** global "do-not-invent" preamble (`llm.py:86,251`). This is the ideal place to add a shared facts-only wrapper + post-clamp.

- **§3 Legibility — brand components exist but are not confidence-linked.** FE has `components/brand/VesperAttribution.tsx`, `VesperNote.tsx`, `VesperSignature.tsx`; `chat/PrivateVesperNote.tsx`; `chat/group/GroupVesperNote.tsx`. Italic Vesper voice is a visual convention. **No component styles prose by confidence.** The one good exemplar of a low-confidence render state is `components/places/SpotTake.tsx:215/292` ("STILL FORMING A READ" sage treatment) — the pattern every other surface lacks. Confidence scores exist only inside internal classifiers/guards (`interrupt_classifier.py`, `content_safety.py:347-354`), never surfaced to render.

- **Fallback ladder — no shared resolver.** Each surface improvises. The common pattern is `... or raw` / `or title` (e.g. `home/compose.py:139`, `pick_judgment.py:162`), which falls back to the **un-clamped generated string**, not to a non-generated terminal rung — defeating the ladder's intent.

- **§4 Reversibility — no shared correction/propagation primitive.** No shared "regenerate / correct-fact / remove" path and no invalidation graph. Where correction exists it is per-surface and ad hoc (story sections, DNA phrases). `core/edit_policy.py:82`'s `low_confidence` flag gates *edit confirmation*, not render fallback.

---

## 2. Highest-risk findings (fabricated fact could reach a user or public share)

Ranked most-severe first. Severity weighs: does it move money / make a commitment, does it reach a **public/unauthenticated** surface, and is any enforcement actually on in prod.

### R1 — Receipt-OCR total drives a real group expense split, server-side, with no mandatory confirmation
`expenses/receipt_ocr.py:24-46` (vision prompt, **no anti-hallucination guard, no confidence output**) → `api/routes/expenses.py:925` `amount = body.amount if not None else ocr["total_amount"]`, `:950` date from `ocr["date"]`, then `async_create_expense` + `_compute_shares` splits **real money** across members. The FE `AddExpenseSheet` pre-fills editable fields, but **the API contract itself accepts a null amount and lets the model's number win** — any non-FE/programmatic caller, or a user who taps through, writes a hallucinated total into the settlement ledger. A model-minted price moving real money is the worst path in the audit. (Never-generated: price + date.)

### R2 — Trip-story public share broadcasts model-minted numeric facts with no fact verification
`tasks/trip_story.py:69` seeds the `hero_subtitle` with the exemplar **"Three days, four restaurants, one regret"** — instructing the model to mint a day-count and venue-count that are bound to no structured field. `build_public_story_payload` (`story_projection.py:170`) blanks the subtitle only on a **privacy** leak or a **known co-traveler name** — it performs **no factual verification**. The subtitle becomes `og:description` and the `.lede` on `GET /stories/{slug}` (`story_landing.py:59,178,191`), a **crawler-fetched, unauthenticated** page (`:137`). Section bodies render there as plain `<p>` (`:180`), also unclamped and unverified — `check_private_signal` (`privacy_signal.py:41`) catches health/finance/dietary keywords but **not** a minted date, price, count, or weather claim. And hero fields aren't owner-editable (§4), so a wrong preview can only be re-rolled. (Never-generated: counts/dates/prices on a public surface.)

### R3 — Restaurant-call transcript mints confirmation numbers and "confirmed" status
`booking_agent/agents/prompts.py:77-91` ("Extract the booking outcome" — **no "null if not stated" rule**) → `transcript_parser.py:93-102` → `restaurant_writeback.py:125-182`. A fabricated `confirmation_number` / `confirmed_datetime` is written to the block `booking_ref`, a booking-confirmation receipt (`core/receipts.py`), and a `booking.restaurant_confirmed` trip event; `was_successful` (model judgment) flips the block to `status="confirmed"`. The Duffel path uses the real API reference (`duffel.py:318`) — the LLM channel is the leaky one, and it reaches user-facing receipts. (Never-generated: confirmation number + availability/booking status.)

### R4 — Public invite page pulls the full itinerary and renders model venue names + LLM prose under real date stamps
`utils/inviteTimeline.ts:113-128` calls `api.getItinerary(trip.trip_id)` **unconditionally on the unauthenticated invite page**; `rowsFromItinerary` (`:88-110`) renders `firstBlock.title` (= model-authored `venue_name`) and `day_theme` (LLM) under a real derived date (`formatStamp`). This surfaces model-minted business names publicly **and contradicts the page's own privacy promise** ("Private notes, costs, and group details stay closed until you accept", `invite/[slug].tsx:620-622`). Note: the invite-snapshot *generator* (`invite_snapshot.py`) is itself clean (structured inputs only, hard no-invent `:174`, dual clamp, deterministic rung-5 fallback) — the leak is downstream in `inviteTimeline.ts`. **Depends on open question O1** (does `getItinerary` authorize non-members?).

### R5 — Concierge chat: unbacked operational facts ship prod-wide (fact guard is log-only)
`concierge/output_guards.py:1183` (`_check_factual_claims`) detects price/hours/closed-day/booking claims, and `:1048` (`_check_grounding`) detects confabulated venue names with a working regenerate path (`:1412`) — but both are **log-only in production**: `CONCIERGE_OUTPUT_GUARD_MODE=log` (`fly.toml:195`, `output_guards.py:1098-1100`). A confident "€40 a head / open till 2am / takes walk-ins" or a fictional venue name with no tool backing ships verbatim on the highest-volume surface. Enforcement exists but is switched off.

### R6 — Narration is entirely unguarded and spoken aloud
`concierge/narrator.py:309` and `guide/prerender.py:263` run **no grounding or factual guard at all** (`guard_reply` is chat-only). A fabricated date/price/identity in spoken prose is caught only by an advisory prompt line (`_prompts_skills.py:1632`) and a precision-biased post-hoc citation filter that **the FE never even renders** (`NarrationCard.tsx:207`; zero `fragment_index` consumers). Highest authority (voice), lowest enforcement, no length clamp (`narrator.py:282,312`).

### R7 — Lookup synthesizer asserts web-sourced facts, caches them 3h–7d, re-serves to other users
`lookup_agent/prompts.py:56-70` explicitly directs the model to state "current opening hours," "specific price points," "upcoming events with dates." Source is `web_data` (Tavily snippets), not typed data (`synthesizer.py:35-54,106`). The answer folds into the concierge reply with no confidence chrome and is **semantic-cached 3h–7d** (`definitions.py:212-224`) — a hallucinated "open until 11pm / €15 admission" is re-served to *other* users for up to a week. A `source="synthesized"` flag exists (`handlers.py:112`) but is not surfaced on FE.

### R8 — Research briefs mint structured facts that propagate into Takes and dossiers
`research_agent/agents/prompts.py:156-159` (SYNTHESIZE_BRIEF) emits `price_range`, `hours`, `admission_fee`, `capacity` as extracted JSON from the model's reading of free web sources. These become the `brief` consumed by both the curator take (`curator_prompt.py:80`) and dossiers. The groundedness gate (`generator.py:343`) validates only `past_trip`/`saved_entity` hypothesis refs — it does **not** validate any place-fact in prose or in these structured fields.

### R9 — Story-ready push quotes the raw, pre-guard hero title to the lock screen
`notifications/.../push.py:307`: `... "{hero_title}"`. `hero_title` is unclamped and passed **before** the public `safe_hero_title` guard (which lives only in the projection path). A title naming a hidden place or inventing a hook is delivered as a notification unfiltered.

### R10 — Model-authored availability caveats rendered as prominent warning pills
`core/prompts/takes/shared.py:238` (CAVEAT_RULES) tells the model to write "closed Mondays / no walk-ins / 30-min wait" verbatim, with no source binding, then `Caveats.tsx:91` renders them as the highest-emphasis (red/amber) element on the take card. A wrong "closed Mondays" actively misdirects a traveler.

**Latent (currently gated off, would escalate if flipped):** Atlas fabrication risk — `ATLAS_LLM_ENABLED` defaults false (`core/feature_flags.py:20-27`) and is unset in prod, so artifact/almanac/timeline/home-letter ship deterministic, data-grounded **mocks**. The LLM prompts that restate counts as free prose (`atlas/prompts.py:480-485,512-520`) become live fabrication vectors the moment the flag flips.

---

## 3. Field inventory

One row per user-facing generated field. `source`: generated | fact | mixed (facts interpolated). `trunc`: clamp (word-boundary) | hardCut (raw slice) | none. Blank cells = none/not-applicable.

### Live conversational + narration
| file:line | field | source | maxChars | trunc | loading | fallback | conf? | editable? | propagation |
|---|---|---|---|---|---|---|---|---|---|
| concierge/agent.py:1104 | chat reply | generated (facts tool-interpolated) | none | none; FE Markdown no clamp (PrivateVesperNote.tsx:99) | skeleton + 3-tier (TypingIndicator.tsx:30) | "Vesper didn't have a response here" | none (lazy_research "verify" pill only) | Share/Report, no edit | Report→review, no mutation |
| concierge/strict_compose.py:239 | group recovery reply | generated | GROUP_COPY_BUDGETS | clamp (group_compose.py:210) | suppressed | "[Composition skipped…]" | — | no | rolls back scaffolding |
| concierge/group_compose.py:917 | group message | generated (names stripped :741) | 220/140/160/100 by kind (:176) | clamp (:210) | TypingIndicator group | retry / silent omit FE | semantic privacy guard :1083 | no | rejected drafts never sent |
| concierge/narrator.py:309 | live narration | mixed (entity_name interpolated :275) | none (soft target :282) | **none** | lazy play + spinner (NarrationCard.tsx:217) | text always present | none | tone feedback only :354 | ephemeral |
| guide/prerender.py:263 | prerendered narration | mixed | none | none | status machine | status=failed | none | no | cache overwrite |
| concierge/bridge_generator.py:135 | voice↔narration bridge | generated | 25-word hard cap :174 | hardCut + "…" :176 | n/a | "Right, so as I was saying —" | none | no | no FE render (TTS inline) |
| concierge/reflection.py:335 | reflection + memory writes | generated (internal) | tokens 1024 | none | background | "No significant changes needed" | n/a | writes Personal Memory | feeds chat/narration lens |
| concierge/notes.py:152 | trip journal entry | generated | tokens 500 | none | background | "NO_UPDATE" | none | durable; no user edit UI | post-trip + agent continuity |
| concierge/notes.py:195 | member brief | generated | "200 words" prompt-only | none | background | unchanged brief | none | durable; no user edit UI | compose/planning context |
| concierge/vision_summary.py:100 | image summary | generated (vision) | 600 hard :73 | hardCut + "…" :151 | background | None ("forgets image") | none ("do NOT speculate" :54) | no | messages.metadata_ prefix |
| concierge/citation_extraction.py:147 | narration citations | generated (verbatim-substring validated :210) | claim ≤200 :109 | drop invalid | ~300ms post-pass | [] | none (:56) | no | **no FE render site** |

### Home + notifications
| file:line | field | source | maxChars | trunc | loading | fallback | conf? | editable? | propagation |
|---|---|---|---|---|---|---|---|---|---|
| home/compose.py:124 | anchor voice_line | mixed | 140 + tokens 128 | clamp (:139) | trip-home skeleton | fallback_voice_line (rung4) | none | NO | none |
| home/compose.py:187 | hero voice_line | mixed | **none** (tokens 80) | **none** (raw strip :208) | HeroVoice fade | fallback_hero_voice_line | none | NO | none |
| home/pick_judgment.py:98 | glance_title / glance_body | generated | 80 / 160 | clamp (:162/163) | Deck-on-tap | deterministic glance | none | NO | home card + Deck |
| home/pick_judgment.py:98 | reasoning / tradeoff | generated | 300 / 140 | clamp BE :180; **FE no numberOfLines** (DeckPickFace.tsx:126/140) | " | None | none | NO | Deck focus |
| notifications/channel_dispatch.py:1080 | card eyebrow/title/body/cta | mixed (re-render of upstream chat content) | 40/80/160/32 | clamp :1106 | card absent until upsert | fail-open skip | none | "not now" suppress only :990 | durable vesper_cards row |
| notifications/triage.py:342 | triage intent/reasoning | generated (internal directive) | tokens | parse-or-skip | n/a | silence | `worth` send-gate | n/a | Tier-3 turn |
| notifications/group_interjection.py:352 | interjection intent/reason | generated (internal) | tokens | fail→wait | n/a | wait | none | n/a | interjection turn |
| api/routes/conversations.py:86 | conversation title | generated | 80 slice | **hardCut mid-word** :106 | untitled until set | untitled | none | **YES** (history.tsx:216) | conversations.title |

### Discover / takes / search / dossiers
| file:line | field | source | maxChars | trunc | loading | fallback | conf? | editable? | propagation |
|---|---|---|---|---|---|---|---|---|---|
| core/takes/generator.py:75 (personal) | take body/headline/verdict/caveats | mixed (grounded evidence_refs) | headline 200; **body none** | none | SpotTake.tsx shimmer + caret | curator → brief | yes (drives rich/forming :215) | no | cached artifact |
| core/takes/generator.py:121 (curator) | curator take body/verdict/caveats | generated (brief+dossier) | headline 200; body none | none | shimmer | brief | verdict.confidence | no | cached artifact |
| models/takes.py:82 → Caveats.tsx:85 | caveat.text + reason | generated | **none** | none | — | present-only | severity | no | none |
| core/personalization/angle_rank.py:92 | why_for_you | generated | 18 words prompt-only | none | empty→nothing (WhyForYouCallout.tsx:33) | "" | none | no | nothing durable |
| concierge/angle_query_seeder.py:118 | angle title/question/why_interesting | generated | ≤8 words prompt | none | — | distinctiveness ≥0.5 gate; pending_review :215 | distinctiveness_score | human-gated | inserts place_angles |
| core/personalization/discover_synthesizer.py:159 | observation.content | generated (behavior signals) | 60 words prompt | none | — | importance-validated :195 | no | no | → personal_memory → future Takes |
| lookup_agent/synthesizer.py:96 | answer | mixed→generated (DB + web) | 2-4 sent prompt-only | none | — | web→db json→"couldn't summarize" :129 | none surfaced | no | **semantic cache 3h-7d** |
| research_agent/agents/dossier_profiles.py:137 | dossier thesis/content/claims | generated | 200-1100 words prompt | none | app/dossier/[id].tsx:286 skeleton | quality gate; FE empty :411 | coverage_depth (not surfaced) | no | durable, **shareable** asset |
| research_agent/agents/prompts.py:141 | brief + structured_data (price/hours/admission) | mixed | 60-100 words prompt | none | — | confidence float | yes (float) | no | feeds Takes + dossiers |
| app/dossier/[id].tsx:194 → DossierFormats.tsx:193 | ExperienceFacts WHEN/WHERE/MOVE/BOOK BY | generated | none | none | skeleton | present-only | none | no | — |

### Stories / digests / threads / memory
| file:line | field | source | maxChars | trunc | loading | fallback | conf? | editable? | propagation |
|---|---|---|---|---|---|---|---|---|---|
| tasks/trip_story.py:49 | hero_title | generated | **none** (FE numberOfLines=2) | none BE | Skeleton :185 | safe_hero_title → "A {dest} Trip" (public only) | none | regenerate only (not directly editable) | push :307, OG title, card.png |
| tasks/trip_story.py:69 | hero_subtitle | generated | **none** (FE numberOfLines=3) | none BE | " | blanked on privacy/name leak only | none | via regenerate | **OG description** + public .lede |
| tasks/trip_story.py:93 | section body | generated | **none** (BE + FE) | none | " | dropped on privacy/name leak; parser drops empty | none | yes (PATCH :464; mark-wrong/remove/restore :789) | public HTML `<p>` :180 |
| digest/engine/llm_calls.py:310 | overall_arc / what_worked / what_didnt | generated | **none** | none (FE row-slices) | memory.tsx fetch | sections hide when empty | none | **no** | GET /trips/{id}/summary to members; story + thread input |
| digest/engine/llm_calls.py:87 | day_arc turning_point/cohesion | generated | _truncate_subtitle (cards.py:232) | clamp | — | None | none | no | home morning_brief card subtitle |
| digest/engine/llm_calls.py:168 | planning_context | generated | tokens 1536 | none | — | {"status":"no_data"} | evidence_confidence (not surfaced) | no | planner prompt only (no FE render) |
| core/personalization/cross_trip_threading.py:313 | thread | generated | one-sentence prompt | none | — | {"threads":[]} | LLM self-gates | no | persisted + API but **no FE render (dead surface)** |
| concierge/refresh_memory.py:279 | DNA phrases[] | generated | **none** (3-8 words prompt) | none | post-fetch | reflection-phrase lookup table :339 | evidence_count≥3 gate | **yes (per-phrase dispute ✕** TravelDNACard.tsx:87) | Atlas letter hero, profile, chat |
| concierge/refresh_memory.py:225 | dna_essence | generated | **24** (atlas_dna) + ≤3 words :261 | validate-drop | — | None | word/char guard | no | Atlas shelf/profile subtitle |

### Atlas (LLM path currently dark — ships data-grounded mocks)
| file:line | field | source | maxChars | trunc | loading | fallback | conf? | editable? | propagation |
|---|---|---|---|---|---|---|---|---|---|
| atlas/composer.py:216 | artifact one_line_read | generated | none | none | artifact/[id].tsx skeleton | specificity gate → _mock_one_line | specificity gate :587 | **NO (delete-only)** | postcard/OG share |
| atlas/composer.py:216 | artifact title / section body | generated | none | none | skeleton | _mock_* | none | NO | — |
| atlas/almanac_generator.py:104/119 | almanac month/year title/body | generated | 120/500 slice (prompt says 120/160) | hardCut | **not rendered (orphaned?)** | _mock_*_summary | none | NO | none |
| atlas/timeline_generator.py:55 | timeline entry title/body | generated | 120/240 slice (prompt says 80/160) | hardCut | row | _mock_generated_copy | none | title rename only; body not editable | display title only |
| atlas/home_letter_generator.py | letter salutation/body | generated | 24/280 | hardCut | mock inline | _mock_letter | none | NO | none |

### Facts-heavy / never-generated risk
| file:line | field | source | maxChars | trunc | loading | fallback | conf? | editable? | propagation |
|---|---|---|---|---|---|---|---|---|---|
| concierge/invite_snapshot.py:249 | snapshot_text / question / og_* / chips | generated (clean: structured inputs, no-invent :174) | 320/80/60/120/30 | clamp | SkeletonCard | rung-5 deterministic (:235) + conv fallback | none | no (public RO) | cached; **OG meta** |
| planning_agent/agent.py:200 → prompts.py:201 | block title (= venue_name) | generated (**never reconciled to venues.name**) | 80 (trips.py:1620) | clamp | parent query | "Unknown" / "Untitled" | none | yes (ChangeStudioSheet) | plan_events |
| planning_agent/schemas.py:102 | price_per_person_cents → price_cents | generated ("planner-estimated", **undocumented in prompt**) | int | none | — | None | none | via edit | — |
| planning_agent/prompts.py:223 | travel_to_next.minutes / distance_km | generated | dict | none | TravelSegmentRow | omit if null | none | — | — |
| planning_agent/prompts.py:190 | day_narratives.opener | generated (prompt invites weather) | none | none | — | omit | none | no | — |
| booking_agent/agents/booking_graph.py:46 | ranked recommendation/pros/cons | generated | none | FE numberOfLines=1 | skeleton | section hidden | none | no | trade_offs |
| booking_agent/.../booking_graph.py:449 | cart_total_amount | **fact** (summed from price_amount) | — | — | — | 0.0 + per-currency | n/a | no | — |
| booking_agent/restaurant/transcript_parser.py:68 | confirmation_number / confirmed_datetime | generated (**no "null if not stated"**) | none | none | — | null | none | FE re-entry only | booking_ref, receipt, trip_event |
| expenses/receipt_ocr.py:90 | total_amount/date/merchant/currency | generated (vision, **no guard, no confidence**) | number | none | FE async poll | omit field | **none** | pre-fill (AddExpenseSheet) | **expense.amount + shares split** |
| social_state/genesis.py:111 | genesis markdown | generated (self-marks "hypothesis") | ~400 words soft | none | bg task | None | marked hypothesis | no (agent-facing) | trip_social_state |

---

## 4. Violations by principle

### §1 Separation (facts must come from data; prose may interpolate, never mint)
- **Prompts that instruct the model to author never-generated facts:** trip_story hero_subtitle exemplar mints counts (`trip_story.py:69`); daily digest asks for `estimated_actual_duration_min` + weather `context_notes` (`digest/prompts.py:70-91`); lookup asks for hours/price/events-with-dates (`lookup_agent/prompts.py:56-70`); SYNTHESIZE_BRIEF emits price/hours/admission JSON (`research_agent/agents/prompts.py:156-159`); take CAVEAT_RULES writes availability verbatim (`takes/shared.py:238`); DNA prompt invites minting specifics (`refresh_memory.py:214`).
- **Model facts persisted as record without reconciliation:** planner block `title` is always the model's `venue_name`, even when `venue_id` resolves to a real row (`itinerary_persistence.py:193`); planner `price_per_person_cents` persisted to `price_cents` unmarked (`schemas.py:102`); transcript confirmation number/datetime written to receipt+event (`restaurant_writeback.py:125-182`); OCR total/date become a real expense (`expenses.py:925,950`).
- **Weaker-than-peer guards:** home card re-render says "Extract" not "use only facts / do not invent" (`channel_dispatch.py:1092`); curator take omits the GROUNDING_RULES block that the personal take imports (`curator_prompt.py:16`).
- **Held well:** the FE never parses facts out of prose — all dates/prices/confirmation#/addresses arrive in typed attachment `data` fields (`BookingConfirmationCard` uses structured data only); the invite-snapshot generator uses structured inputs with hard no-invent rules; Atlas photos are attached deterministically, never model-assigned (`composer.py:130-147`).

### §2 Containment (generalize when unsure, never fabricate)
- `refresh_memory.py:217` **forbids** hedging ("no 'seems to' / 'tends to' / 'perhaps'") and demands stand-alone confident phrases — actively pushing a thin profile to assert specifics instead of generalizing.
- Transcript prompt has no "null if not explicitly stated" rule (`prompts.py:77-91`); OCR has only "omit if not visible," no "do not guess a total" (`receipt_ocr.py:41-46`).
- Lookup has "never invent" (`prompts.py:50`) but no low-grounding rung — `_fallback_answer` fires only on exception, not on thin data (`synthesizer.py:129`).
- Narration's containment is prompt-only with no runtime fallback if the model ignores it.

### §3 Legibility (low-confidence prose visually distinct; never fact-authority)
- **No user-facing surface styles prose by confidence.** Confidence signals that *are* computed are discarded at render: dossier `coverage_depth` and quality-gate scores (`app/dossier/[id].tsx`), citation grounding (no confidence field `citation_extraction.py:56`, and not rendered), planning-context `evidence_confidence`. A `surface`-depth dossier looks identical to `expert`.
- Public surfaces carry no inline voice marker: story section bodies render as plain `<p>` (`story_landing.py:180`), attribution only in a page footer.
- Home hero/anchor/pick render Vesper prose in the same ink/typography as factual chrome (`HeroVoice.tsx`, `DeckPickFace.tsx`), despite the canon that italic = Vesper voice.
- Digest home-card subtitle lifts a raw markdown body line, with the code admitting formatting can leak through (`home/cards.py:241-248`).
- **Exemplar to copy:** `SpotTake.tsx:215/292` renders low-confidence takes in a distinct "STILL FORMING A READ" state; `RecommendationBlock.tsx` gates `why_for_person` to the private channel (`:54`, fail-closed).

### §4 Reversibility (owner-editable/removable; corrections propagate)
- **No edit path** on: trip-story hero_title/subtitle (regenerate-only, which may rewrite edited sections `story.tsx:713`); trip-summary `overall_arc`/`what_worked` served to all members; Atlas artifact one_line_read/sections (delete-only) though the artifact is a shareable postcard; narration; home anchor/hero/pick; takes/angles/dossiers (read-only); digest home-card subtitles.
- **No propagation graph:** when a fact is corrected, nothing systematically re-generates downstream (story → OG image → push → Plan-Similar). Atlas rename invalidates only timeline queries.
- **Held well:** story sections (edit/remove/restore `story.tsx:789`); DNA phrases (per-phrase dispute `TravelDNACard.tsx:87`); conversation title (rename `history.tsx:216`); plan blocks + OCR fields (editable pre-commit).

### §5 Restraint (hard budget, graceful truncation)
- **No length governance** on the highest-exposure surfaces: trip-story hero/subtitle/body, narration (live + prerender), personal 1:1 chat reply, take body/caveats, all digest summary fields, cross-trip thread, DNA phrases. Ceiling is only `max_tokens` + FE `numberOfLines` (a visual clip with no ellipsis contract).
- **hardCut instead of graceful clamp:** conversation title `[:80]` mid-word (`conversations.py:106`); Atlas almanac/timeline/letter raw slices; and Atlas clamps exceed their own prompt budgets (timeline prompt 80/160 vs code 120/240; almanac prompt 120 vs code 500).
- FE gaps: `DeckPickFace` reasoning/tradeoff have no `numberOfLines`, relying 100% on the BE clamp.
- **Held well:** the facts-heavy domain (invite, plan blocks, recommendation) clamps at every chokepoint via `content_contract.py`; `home/cards.py:232` and `dna_essence` (24-char) are correct restraint examples.

### Never-generated list — every breach
| Class | Where minted |
|---|---|
| Prices/totals | receipt_ocr total (`receipt_ocr.py`); planner `price_per_person_cents` (`schemas.py:102`); lookup price prose (`lookup_agent/prompts.py:64`); SYNTHESIZE_BRIEF `price_range/admission_fee` (`prompts.py:156`); nothing prevents a story body/arc asserting a price |
| Dates/times | OCR `date`; transcript `confirmed_datetime`; lookup "events with dates"; no guard on story section-body dates |
| Counts/quantities | trip_story subtitle exemplar ("Three days, four restaurants"); daily `estimated_actual_duration_min`; travel `minutes/distance_km`; anchor few-shot count examples (`home/prompts.py:24,34`); Atlas LLM count restatement (latent) |
| Addresses/coords | dossier ExperienceFacts `WHERE` (`DossierFormats.tsx:193`) |
| Real business names not in trip data | planner block title unreconciled (`itinerary_persistence.py:193`); lookup "recommend top results" from web (`prompts.py:60`); confabulated names in chat (guard log-only); Atlas artifact prompt lacks a blunt "never name a venue not provided" |
| Availability / "open now" / booking status | take caveats ("closed Mondays" `shared.py:238`); lookup hours; transcript `was_successful` → `status="confirmed"` (`restaurant_writeback.py:109`) |
| Confirmation/reference numbers | transcript `confirmation_number` (`transcript_parser.py`) |
| Weather | daily digest `context_notes` (`digest/prompts.py:36`) → home card; story bodies unguarded |
| Identity ("who was with you") | story bodies can assert companions (input passes none; public projection only redacts *known* member names, can't catch a *fabricated* one) |
| Held well | Atlas explicitly bans "You went with Sarah" (`atlas/prompts.py:44`) and never model-assigns photos; FE never parses facts from prose |

---

## 5. Prioritized hardening plan

Ordered by (risk reduced ÷ effort). "Shared helper" flags where one primitive removes repeated per-surface work.

### Tier 0 — config + prompt flips (hours, no new code)
1. **Flip `CONCIERGE_OUTPUT_GUARD_MODE` off `log`** (`fly.toml:195`). The regenerate/block machinery already exists (`output_guards.py:1412`); prod just isn't using it. Directly closes **R5** and most of the chat side of the never-generated list. Decide `regenerate` (safe default) vs `block`. *(Confirm the log data supports the escalation — see O3.)*
2. **Add "null / omit if not explicitly stated" to the transcript and OCR prompts** (`booking_agent/agents/prompts.py:77-91`, `receipt_ocr.py:41-46`) and an explicit "do not estimate a total." Cheap partial mitigation for **R1/R3**.
3. **Rewrite the fact-shaped few-shot exemplars** that teach minting: trip_story hero_subtitle "Three days, four restaurants" (`trip_story.py:69`), anchor count examples (`home/prompts.py:24,34`), DNA "always finds the table locals eat at" (`refresh_memory.py:214`). Replace with interpolation-only or category-level exemplars. Mitigates **R2** and §1 broadly.

### Tier 1 — close the money/public-share paths (days)
4. **Require an explicit, non-null, human-confirmed amount for receipt→expense** (`expenses.py:925`). Reject a null `amount` at the API contract; treat OCR output as an *unconfirmed suggestion* that must be echoed back and confirmed before `async_create_expense`. Closes **R1** (the audit's worst path).
5. **Auth-gate or strip the invite itinerary fetch** (`inviteTimeline.ts:113-128`). Confirm `getItinerary` membership auth (**O1**); if it serves anon callers, restrict the invite page to the (clean) snapshot payload only. Closes **R4** and its privacy-promise contradiction.
6. **Add a fact-verification pass before public story projection** (`story_projection.py`): reject/blank hero_subtitle + section bodies whose numeric tokens (counts, dates, prices) don't appear in the structured input. And **run `safe_hero_title` before the push quote** (`push.py:307`), not only in the projection path. Closes **R2/R9**. *(Shared helper: a "numeric-tokens-must-appear-in-input" checker reusable by story, invite, digest.)*
7. **Reconcile planner block title to `venues.name`** when `venue_id` resolves (`itinerary_persistence.py:193`); keep the model string only for name-only blocks. Removes a persisted-wrong-name vector (**R2-adjacent**, part of R-list).

### Tier 2 — shared primitives (extend what exists)
8. **"Facts-only" prompt wrapper at the `call_llm` chokepoint** (`llm.py:251`) — inject the never-generated list + do-not-invent clause for surfaces flagged `renders_prose`, and fold it into `content_contract.guidance()` so length + facts guidance travel together. *(Shared helper: removes the copy-paste "don't invent" lines and the surfaces that lack them entirely — narration, curator take, home card render.)*
9. **Extend the length contract to the unregistered prose surfaces** (trip story, narration, take body, digests, DNA phrases): register budgets in `CONTRACTS` and call `clamp_text` at each generator. Closes the §5 gaps. Low risk (the primitive and FE mirror already exist).
10. **A confidence gate + one shared low-confidence render component.** Surface the confidence signals already computed (dossier `coverage_depth`, `evidence_confidence`, verdict confidence) and render low-confidence prose through a single component modeled on `SpotTake`'s "STILL FORMING A READ" state. Closes the §3 gaps (**R7/R8/R10** legibility side, dossier). *(Shared helper: one component + one `confidence >= threshold` gate, reused across takes, dossier, lookup, narration.)*
11. **A fallback resolver with a non-generated terminal rung.** Replace `... or raw` patterns (`home/compose.py:139`, `pick_judgment.py:162`) with a helper that walks the ladder to a rung-3-or-lower non-generated value. Ensures public surfaces never render un-clamped generated text as the "fallback."

### Tier 3 — reversibility + propagation (larger)
12. **Owner edit/remove on the durable, shared generated fields** that lack it: story hero_title/subtitle (direct edit, not just regenerate), trip-summary arc/what-worked, Atlas artifact one_line_read/sections. 
13. **A correction-invalidation graph:** when a source fact or a generated field is corrected, regenerate the known downstream outputs (story → OG/card → push; take → dossier). Today nothing propagates. Largest effort; do after the surfaces above are individually editable.

### Housekeeping (cheap, reduces surface area)
14. Decide the fate of **dead/orphaned generated surfaces** that still cost tokens: cross-trip threads (persisted + API-exposed, no FE consumer — O2), Atlas almanac summaries (generated, no render site found — Atlas O1), narration citations (generated, never rendered). Either ship the render or stop generating.

---

## 6. Open questions (need a human decision)

1. **`GET /api/getItinerary/{trip_id}` auth (O1, gates R4):** does it enforce trip membership? If it returns full itinerary blocks to an anonymous invite-token holder, R4 is a live privacy + fabricated-name leak, not just a UI concern.
2. **Receipt→expense caller set (gates R1 severity):** is `create_expense_from_receipt` ever called with `amount=None` by anything other than the FE (retries, agent, programmatic)? If the FE is the only caller and always sends the user-confirmed `parsedAmount`, R1 is latent; otherwise it is active.
3. **Output-guard mode intent:** is `CONCIERGE_OUTPUT_GUARD_MODE=log` a permanent posture or a pre-launch measurement phase? The code comment ("MEASURE… before deciding whether to escalate", `output_guards.py:1098`) implies the latter, but there's no dated plan to flip it.
4. **Contract intent for spoken narration §5:** is the soft word-target an accepted exception for spoken pacing, or should narration inherit a hard clamp like group_compose/bridge?
5. **Curator take grounding:** is the missing GROUNDING_RULES import (`curator_prompt.py:16`) intentional (editorial, brief-bounded) or an omission that lets it assert place-facts beyond its brief?
6. **`AUTO_PUBLISH_GREEN_DOSSIERS`** is False in prod (per project memory); dossiers hit a review queue. If flipped true, the "confidence discarded at render on a shareable asset" finding (R8/§3) escalates — confirm current state before prioritizing.
7. **Weather source:** does daily-digest `context_notes` weather ever join a real source, or is it always minted (`digest/prompts.py:36`)? If always minted, it must move to the never-generated path or be dropped.
8. **Atlas honesty fix in the shipped build:** the whole "don't fake a story" stance rests on `artifact/[id].tsx:157-233` gating the authored badge on `composed_by === 'llm'`. Confirm it's in the current release (project memory still lists it as an open bug), and note there's no second check if that one field is wrong at render.
9. **`price_per_person_cents`:** it's undocumented in the planner prompt YAML yet parsed and persisted (`schemas.py:102`). Remove it from the path, or document + mark it as a model estimate distinct from provider price?

---

*Scope caveats: `INTERNAL_SIGNAL` classifier/guard surfaces were sampled for leak-to-UI risk, not fully inventoried (they don't render prose). Some FE render claims for dead surfaces (cross-trip threads, narration citations) are "no render site found" after grep — recorded as findings, not proof of absence. The 858-file backend was navigated via the surface catalog, not read exhaustively.*
