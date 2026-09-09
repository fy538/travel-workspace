---
doc_type: working
status: active
owner: founder / Strategy task
created: 2026-09-09
last_verified: 2026-09-09
expires: 2026-10-09
why_new: Turns the first end-to-end practical judgment seam into a small product acceptance and producer decision packet without adding a second Places composer or changing Chat/Life.
supersedes: []
---

# Practical judgment — producer and acceptance brief

## Why this exists

The September 9 implementation proves that an explicit, target-bound request can
reach a useful result:

`explicit place + time window + duration → exact owner reads → place.fit_window → RootUnit → Home/Places semantic renderer`

That is an architectural proof, not yet a user behavior. The current caller is
an API-level seam. Ordinary cards do not infer intent, and no Chat or native
control has been added. This brief keeps the next decision small: decide what
should legitimately produce the request before authorizing another implementation
lane.

## Recommended product position

Keep Chat as the canonical input surface for an explicit practical question when
its input model is ready. Do not add a second mini-composer or intention form in
Places. Places should remain the field that answers a named question with local
evidence; Home may receive the resulting judgment as one useful piece of value.

The current Claude designs already show the intended aperture. Places opens an
exact place with **Ask Vesper privately** or a typed journey-frame question;
Home's **Why this** sheet has **Ask about this**; Chat receives the object as
context and answers without mutating Home until the person explicitly asks for a
change. Reuse that pattern. Do not add a global “check a visit” form, a second
Places composer, or a persistent practical-intention profile.

Until that producer is selected, keep the current seam dark except for fixtures,
contract tests and owner-read verification. A developer fixture is not a launch
experience and must not be represented as ordinary personalized supply.

This preserves the product grammar:

- **Chat:** the person gives a thing, asks a question, or states a purpose.
- **Places:** the world-facing field grounds the answer in exact places and
  conditions.
- **Home:** the result can return as a useful, low-demand consequence alongside
  other value.
- **Life:** no new record is created merely because a practical question was
  asked.

## First user-facing composition

The first composition should be designed across the existing Claude projects as
one target-preserving turn:

1. **Entry from the object:** on a canonical Place page or a consequential
   Place unit, the person taps **Ask Vesper privately** / **Ask about this**.
2. **Seeded question:** Chat opens with the exact Place, current scope and a
   compact prompt such as “Can I fit this between 3–5pm for 90 minutes?” The
   user may edit the words; no profile or setup step appears.
3. **Bounded read:** the producer sends only the explicit place, window and
   duration to the existing Places v2 seam. If a required field is genuinely
   missing, ask one clarifying question in Chat; never infer it from the card.
4. **Answer:** Chat returns one concise supported / does-not-fit / cannot-tell
   judgment with the evidence boundary. The original Place explanation,
   destination and independent value remain intact.
5. **Optional consequence:** a supported result may be visible on the originating
   Home/Places unit on return. Nothing is booked, arranged, written to Life,
   notified or watched unless a later, separately authorized action says so.

The Places project’s “journey frame” and constrained-afternoon boards are visual
references for the result, not permission to create another interaction surface.
The Home project’s “one Chat aperture per page” and “Home is unchanged until
asked” rules are the continuity contract. The exact visual composition remains
with Claude Design; this brief defines behavior and evidence only.

## Concrete acceptance cases

The examples below are deliberately ordinary and should be judged for value,
not just route correctness.

### 1. A bounded afternoon

**Request:** “Can I spend 90 minutes at this museum between 3:00 and 5:00?”

**Required input:** exact place identity, explicit start/end, and visit duration.

**Supported result:** a concise supported/unsupported judgment grounded in the
  current exact place read and any exact commitment evidence. The reason should
  tell the person what the evidence supports (for example, that the visit fits
  the stated window), not ask the person to complete a checklist.

**Independent value that must survive:** the museum’s existing explanation,
  source, destination and other Places material remain available even when the
  fit claim is unknown or unsupported.

### 2. Heat or walking concern

**Request:** “Is this realistic if I am walking and it is very hot?”

**Current truthful result:** unknown unless an admitted route/movement owner and
  relevant conditions supply the needed evidence. The system must not convert
  `open_now` into arrival feasibility, invent travel time, or imply accessibility
  from a missing source.

**Future dependency:** a separately admitted route/movement owner, with its own
  freshness, cost and viewer/authority contract. This is not a reason to add a
  route evaluator inside a Places card.

### 3. A commitment conflict

**Request:** “Could I do this before my exact dinner commitment?”

**Required behavior:** use only the exact admitted commitment reference. If the
  commitment read is missing, expired, or viewer-inaccessible, say that the fit
  is unknown and preserve the place’s independent value. Do not search a broad
  calendar, infer an obligation, or turn the question into a Plan.

### 4. No practical question

**Input:** a person opens Home or browses Places normally.

**Required behavior:** no `PracticalVisitIntent` is created. Ordinary cards may
show opening facts where already supported, but they must not silently become
future visit-fit judgments or a homework list.

## Design-state acceptance

Each state must be legible without making the person diagnose the system:

| State | What the person receives | What must not happen |
| --- | --- | --- |
| Supported | One useful fit statement, its exact evidence boundary, and the Place door | No checklist, booking prompt or forced Plan |
| Does not fit | The decisive conflict (for example, the stated window exceeds the supported hours) plus the unchanged Place value | No invented alternative or automatic reschedule |
| Cannot tell | A direct uncertainty statement naming the missing/stale evidence and preserving the Place read | No optimistic default, silent omission or request to fill a profile |
| Evidence changed/expired | A refreshed or clearly dated result, with the original scope preserved | No stale result presented as current |
| Return | Back to the exact Place/Home scope and original question context | No generic Chat landing or lost target |

## Acceptance bar for a real producer

A future producer lane is ready only when all of these are true:

1. **Explicitness:** target, window and duration come from an actual user request
   or an equally explicit existing command; no ordinary-card inference.
2. **Grounding:** the result names the exact owner evidence and carries its
   revision/expiry and viewer boundary.
3. **Useful completion:** the answer is understandable in one glance and offers
   a meaningful consequence (fits, does not fit, or cannot tell) without asking
   the person to do the reasoning Vesper claimed to do.
4. **Independent value:** unsupported practical evidence does not suppress an
   otherwise worthwhile explanation, comparison, human contribution or place
   destination.
5. **No accidental commitment:** asking does not create a Trip, Plan, Life item,
   notification, booking effect or background watch.
6. **Return:** if the result is opened from Home or Places, the exact target and
   original scope survive the return; changed/expired evidence is labeled rather
   than silently restored.
7. **Cost boundary:** the producer is request-scoped and metered. It does not
   turn root reads into generation, provider acquisition or a global catalog.

## What is already proven

- Backend `place.fit_window` handles exact place/commitment evidence, closure,
  expiry and viewer binding.
- Home adopted the complete Places contract and carries the assessment through
  root selection, OpenAPI serialization and existing Home/Places semantic
  renderers.
- Focused owner evidence is recorded in the [program roadmap](vesper-program-roadmap.md)
  and [complete-system integration roadmap](complete-system-integration-roadmap-2026-09-05.md).

## What is not proven

- No user-facing producer control or Chat producer exists yet.
- No populated provider, route-owner or native/device acceptance exists.
- The displayed note is a renderer-level expression, not a complete practical
  interaction design or a claim that every user will find the result valuable.
- Exact recipient-side original media, Life serving adoption and broader social
  consequences are unrelated dependencies and remain out of scope here.

## Next execution handoff

When the producer decision is accepted, dispatch one separate Luna xhigh lane
with this brief as its acceptance contract. That lane should implement only the
chosen producer and its narrow return path, then run native/populated evidence at
the appropriate boundary. It must not add a Places composer, redesign Chat,
change Life, add route/booking/provider infrastructure, or wake Integration
implicitly.

Until then, this thread remains the orchestration point: review the examples,
choose the producer authority, and decide whether the resulting UI copy feels
like received value rather than a feasibility worksheet.
