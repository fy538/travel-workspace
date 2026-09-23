---
doc_type: working
status: active
owner: founder / product / design / content
created: 2026-09-21
last_verified: 2026-09-21
expires: 2026-10-21
why_new: The Voice Canon governs how Vesper sounds when Vesper is the only speaker. Social screens have four speakers, and no document says how they differ. This companion records the rules the founder approved by ear on 2026-09-21, the evidence behind them, and where each would be tuned at runtime. It is a proposal beside the Voice Canon, not a replacement for it.
supersedes: []
source_of_truth_for: []
---

# Social copy — a companion to the Voice Canon

## 1. Authority

The [Voice Canon](../../travel-agent/docs/product/Voice%20Canon.md) and the
[Editorial and Content Canon](../../travel-agent/docs/product/Vesper%20Editorial%20and%20Content%20Canon.md) §13 remain the authority.
Nothing here overrides them. Two of their rules do most of the work and are repeated because they were the ones broken:

- **The object-first rule** (Voice Canon): Vesper does not narrate its own intelligence, memory, restraint, or helpfulness. "If removing a sentence leaves the same useful object, the sentence probably does not belong."
- **Do not narrate the product** (Editorial Canon §13.3), and the negative oracle in §16.1: a candidate fails when "it explains Vesper's restraint, memory, or coherence instead of rendering the underlying state or contribution."

Status: the founder judged three rounds of the same six screens on 2026-09-20/21 (Claude Design project `caf916f9`, board `C1`) and preferred the third. That is the whole of the evidence for the social-specific rules in §3–§5. No user has seen any of it.

## 2. What went wrong, measured

Across eighteen exploratory boards, 39% of the words drawn inside phone frames were not product copy: 19% were boxed explanations addressed to a reviewer, 20% were mono footnotes stating what the product refuses to do. Those two lanes were over 50% negations and almost never contracted. People's own words were 7% of the text on a social exploration. After the pass: boxes 0%, mono notes 4% (provenance only), people 16%.

Four causes:

1. **Three audiences in one frame.** Commentary for the reviewer was set in the app's typography, so it read as the app speaking.
2. **The briefs are written as prohibitions, and the prohibitions were transcribed into the interface as reassurance** — "She is never told", "No count, no streak". Prominent privacy assurance lowers trust (Brough et al., 2022, the "bulletproof glass effect"), and a negation makes the reader simulate the negated thing first (Kaup's two-step model). A friend's app does not tell you nobody is watching.
3. **Default machine cadence**: "not X, but Y", "no x, no y, no z", aphoristic closers, no contractions. The first rewrite replaced these with a different tic — two short beats on every line — and with assistant reflexes such as "Got it."
4. **Internal vocabulary as labels** ("kept from", "outcome", "be reachable to each other"), vague nouns where the canon's good lines use proper ones, and British spellings in a New York cast.

## 3. Four voices, kept apart

| Voice | Whose | Grammar | Example |
| --- | --- | --- | --- |
| A person speaking | The author | As typed. Rendered in the shared reader (`OriginalReader`, density `open`): name and time once, side by side, then the words. Never tidied, never paraphrased. | "it sank 😭 still ate half of it" |
| A person acting | The user, first person | What they would say out loud. | "I'm in" · "Not this one" · "Remember Maya" |
| Vesper stating | Vesper | The state, with a name, a time, a number or a place in it. Then the one open thing. | "The Print Room closed at 3:00 today. You're meeting Maya there at 4:00." |
| Vesper advising | Vesper | "I'd ___. It ___." An opinion, then a consequence in the person's terms. Advice compares. | "I'd take this one. It's ten minutes on foot to town, which the other two aren't." |

The house pattern for the last two is already in `tools/eval/fixtures/vesper_voice_corpus.json`: "The morning is set. The only decision left is whether dinner stays in Alfama or moves west."

## 4. Rules a social product adds

1. **Vesper does not summarize people.** A headline that retells a friend's message in Vesper's voice spoils it and adds nothing (§16.1: paraphrase without outside evidence). On a screen with friends on it, Vesper's headline is about the day or the world.
2. **Beside a person's words, Vesper adds at most one line, and it is about the world** — tonight's showing, the walk, what changed. In the shared reader this is the place row.
3. **The person is the subject of the sentence.** "Maya's bringing the lemons", not "Maya added a contribution". The test from the prominence brief: replace the name with "someone"; if nothing is lost, the line is not social.
4. **Say a boundary with the everyday noun that already contains it.** "Surprise", "Just you", "Draft", "Until 5:00", "To Nora". Privacy is an address on an envelope, not a paragraph of reassurance. This is consistent with Brough et al.: the backfire weakens when the message reads as care.
5. **Absence is absent.** If there is no view count, there is no sentence about there being no view count. The decision is recorded in the design notes, where it can be argued with.
6. **State a consequence once, at the moment of action, verb first.** "Nora stops seeing it. Her reply stays hers." No ambient reassurance elsewhere.
7. **Provenance says what it is and when**: "LISTING · THU", "MAYA · THURSDAY". Never what was not done. This is the canon's trust footprint (§13), and it is the only job of a mono line inside a screen.
8. **Things have names.** Proper nouns, numerals for times, the unit people actually say.
9. **Negation is allowed when it states a fact about the object** — "Nothing saved here yet. Start with the place you would return to." — and never when it tells the person how to feel about the product.
10. **Warmer copy must not smuggle in claims.** Every Vesper sentence still needs a source the viewer is entitled to. (Caught in drafting: "They already have plans most Saturdays", an invented relationship inference.)

## 5. Three checks before a line ships

- **Read it aloud.** Would you say it to a friend across a table?
- **Find the noun.** Is there a name, a time, a number or a place in it? Concrete language is read as evidence of listening (Packard & Berger, 2021).
- **Remove it.** If the object is just as useful without the sentence, the sentence was describing the product.

## 6. Where each voice would be tuned at runtime

Verified in `travel-agent` on 2026-09-21: `backend/core/vesper_voice.py` is a deliberately narrow deterministic floor (spec `2026-08-01`, six banned words, six traits, two patterns); `backend/core/surfaces/schema.py` binds every surface to `voice_core_ref` and a per-surface `voice_overlay`; `tools/eval/vesper_voice.py` gates a 24-case corpus and states that "human and model-judge scoring belongs on top of this stable floor, not inside it."

| Source of words | Knob | Status |
| --- | --- | --- |
| Fixed interface copy (buttons, chips, empty states) | A versioned phrase pack. No model involved. | Not built; the Voice Canon lists "chrome phrase packs" as a phase target |
| Vesper's generated copy | Voice spec version → per-surface overlay → corpus; later a judge | Floor and overlays exist; the judge is blocked on "a human-scored sample set" |
| People's own words | Never generated, never tuned. The only parameter nearby is how much Vesper may add beside them (zero or one line). | A constraint to encode, not a dial |

The founder's verdicts are the first such sample set: six moments, three variants each, ranked, with reasons. They are stored as `tools/eval/fixtures/vesper_voice_preferences.json`, beside the floor corpus and not inside it. Nothing reads that file yet.

Two cautions from the canon. Keep voice tuning in overlays and out of the identity core and the group composer: the Voice Canon records the "privacy-suppressor paradox" three times from additive edits there, and "voice must never become a prose-only replacement for structural privacy controls." And voice cannot outrun data: "Tonight 7:15 at The Lantern" is only available to a system that has showtimes.

## 7. Open

- The shared reader wraps a person's words in curly quotes and sets them in serif, so a casual message reads like a pull-quote. A casual-message variant is a question for the shared-package owner. Its place row also shows a fork and knife for every kind of place (already in the package's extension queue).
- Is "Swap numbers" too light for a step that needs the other person's consent?
- Does saying nothing at all about an unanswered opening read as kind, or as evasive?
- Captions and review notes outside the phones are still in the reviewer-facing voice and still carry some of the old cadence. They were out of scope for this pass.

## 8. Sources

- Brough, Norton, Sciarappa & John, "The Bulletproof Glass Effect", *Journal of Marketing Research* 59(4), 2022 — https://journals.sagepub.com/doi/abs/10.1177/00222437211069093
- Packard & Berger, "How Concrete Language Shapes Customer Satisfaction", *Journal of Consumer Research* 47(5), 2021 — https://academic.oup.com/jcr/article/47/5/787/5873524
- Kelleher, "Conversational Voice, Communicated Commitment, and Public Relations Outcomes", *Journal of Communication*, 2009 — https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1460-2466.2008.01410.x
- "The Processing of Negation and Polarity: An Overview", *Journal of Psycholinguistic Research* — https://link.springer.com/article/10.1007/s10936-021-09817-9
- Apple Human Interface Guidelines, Writing — https://developers.apple.com/design/human-interface-guidelines/foundations/writing
- Wikipedia, "Signs of AI writing" — https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- Boards: Claude Design project `caf916f9-c0ce-466b-92ee-49ebefe1ca38`, board `C1 - Copy before and after`; crops in `docs/working/design-gen/multiplayer/copy-before-after/`
