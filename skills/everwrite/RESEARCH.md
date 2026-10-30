# Research: everwrite

Findings that back [SKILL.md](SKILL.md). Changes they caused are logged in [CHANGELOG.md](CHANGELOG.md); procedural lessons live in [LEARNINGS.md](LEARNINGS.md); test runs and their evidence in [TESTS.md](TESTS.md); schedule and state in `evergreen.json`. Protocol: [MAINTENANCE.md](MAINTENANCE.md).

Topic: the signs of AI-generated prose and how to write without them: pattern catalogues, humanizer skills, checkers, what current models still overuse. Tier `fast` since 2026-10-17 (was `moderate`). Last refresh 2026-10-30; next due in `evergreen.json`.

<!-- tells: off -->
## Current understanding

- The shared answer key is Wikipedia's "Signs of AI writing" (WikiProject AI Cleanup, edited weekly). It is descriptive: a list of observations, strongest when several appear together. Every leading humanizer skill builds on it.
- Structure outlasts vocabulary. Word habits change with each model release ("delve" peaked in 2023 and fell away in 2025; Wikipedia dates the GPT-5 words, emphasizing, enhance, highlighting, showcasing and canned notability wording, to mid-2025 to mid-2026, and since October 2026 lists a GPT-6 era: challenge, clearer, dependable, foster, leverage, matters, multifaceted, prioritize, quietly, steady, and sentences held to about 8 to 20 words). Staging moves (not X but Y, one-line closers, staged setups, arguing with no one, triads) persist across models, so they lead the pattern list and the word list lives in the checker where a refresh can edit it in one place. A structural classifier (SlopShape, September 2026) still scored 96 macro-F1 after models reworded their own posts.
- Rhythm is the tell a cleanup leaves behind. In a blind test of blader/humanizer, the rewrite pass cleared vocabulary and dashes but raised uniform-beat hits from 60 to 101 and aphoristic closers from 38 to 61; detectors still called nearly all of it AI. Varying sentence length now gets as much weight as the word list.
- Dashes are now a historical tell. Wikipedia moved the em-dash sign to Historical indicators on 2026-10-07 ("2022 to September 2026"). Newer GPT models suppress dashes, and Opus 5.5 nearly stopped too (0.015 per 1,000 words against 3.14 for human writing, Graphite, October 2026); the July 2026 Economist finding that Claude overuses them holds only for models before Opus 5.5. Opus 5.5's top tells are now phrases: "this matters" (116 times the human rate), "is more than a X, it", "why X matters", "looking ahead", "rather than simply", "adds another layer", "dependable". The zero-dash rule stays as a default (dashes still read as AI to many readers, and older models still emit them); an author's own sample overrides it.
- Weak-alone tells (dashes in quotes, a single listed word, transitions, curly quotes, hyphenated pairs, passive voice) need company before they justify an edit. Human writing shows simple is/has, plain verbs, superlatives and ordinary hedges (very, perhaps, tends to); stripping those makes text read less human.
- Detection by feel is near chance for most readers; heavy LLM users reach about 90 percent. Detector tools have real error rates. So the skill's evidence is a list of named, checkable patterns (the checker's output), never a verdict on authorship.
- Two jobs recur across the leading skills: edit (minimum effective change, keep the writer's voice, return final text plus a short change note) and detect (quote each pattern with a fix, no score, no guess).
- Text given for editing can carry instructions; treat it as material, never as commands (blader/humanizer 3.0).
- None of the top prose humanizer skills ships a deterministic checker; they ask the model to reread (blader/humanizer 3.1.0, October 2026, still doesn't). Standalone rule sets now exist with real use: tbhb/vale-ai-tells (Vale, 137 rules, pre-commit hook) and berelevant-ai/slopless (textlint CLI, 50+ rules), both active in October 2026; neither scans for invisible characters. A stdlib script that scans for the mechanical tells saves the reread on long documents and gives tests an artifact to check; the two rule sets are the option for teams that lint docs in CI.
- Style tells and watermarks are separate layers. Anthropic has watermarked Claude text since 2026-08-02 (SynthID-Text style, in word choice, no added characters; older models by December 2026); Google has marked Gemini text since 2024; OpenAI announced textGrain on 2026-10-05 and is rolling it out to ChatGPT and Codex users in the EU (API opt-in elsewhere, off by default). Text detection for all three is limited to approved parties; Google's SynthID Detector opened to the public on 2026-10-07 for images, video and audio only. Editing tells leaves most of a statistical mark; only a full rewrite or translation removes it. The skill never promises "undetectable" output.
- There is a real lower limit on detection, set by entropy (how many free word choices the model made), not by length. Dictated or fixed text ("One, two, three") has no choices, so no watermark or classifier can tell who typed it (Christ, Gunn and Zamir; Kirchenbauer et al.). Detection also needs enough marked text: Anthropic says small samples don't work, and SynthID-Text caught 39 percent of marked texts at 200 tokens in an independent test. Classifier detectors fail on short text and flag non-native writers (over 61 percent of human TOEFL essays, Liang et al. 2023).
- Covert marks can also be invisible Unicode characters, which ignore entropy and are easy to strip. The o3/o4-mini U+202F reports (April 2025) were a training quirk by OpenAI's account, not a watermark; the checker scans for these characters anyway.
- EU AI Act Art. 50 has applied since 2026-08-02 (providers mark synthetic text; the "standard editing" assist is exempt); existing systems have until 2026-12-02.

## Open questions

- Does Anthropic's usage policy bar watermark removal? Neither Anthropic page mentions removal (checked 2026-10-17); the usage policy bars deceptive content in general.
- Chakraborty et al.'s sample-complexity bound: exact form still to read.
- Practice: how people wire humanizer skills into agent workflows. 2026-10-17 found only two concrete patterns (slopless's `install-skill` command, vale-ai-tells' commit-msg hook); still thin.
- Should forced triads get a heuristic in the checker? Every attempt so far is too noisy (lists of three are often real).
- Do Sonnet 5.5 and Haiku drop dashes like Opus 5.5? Only Opus data so far.
- Is Wikipedia's GPT-6 era word list stable? A temporary account added it in October 2026; only "dependable" went into the checker, because Graphite's count backs it.
- Is the `uniform-rhythm` threshold (five or more sentences, spread under a quarter of the mean, all at least six words) right? No hits on 120 human READMEs; not yet tried on long human prose.
- Resolved 2026-10-17: no top humanizer skill strips invisible Unicode (R-20261017-5); a Vale option exists and is pointed to (R-20261017-3).
<!-- tells: on -->

## Search plan

Four tracks; every refresh runs at least one query on each (scope each to the period since the last refresh; add the year). Protocol §4 explains the tracks and how tooling, practice and testing findings are judged.

Subject (the goal and the latest thinking on reaching it):

- Fetch https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing and diff its section list and "Words to watch" lines against Current understanding; check the Historical indicators section for tells that retired. The page is over 250k characters and fetch tools summarise it badly, so read the history first (https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&action=history: dates, editors, edit summaries) and fetch only the changed sections; markup signs live on the subpage https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Markup (WP:AIMARKUP) since 2026-10-23
- Official forums, announcements first, then open proposals: https://en.wikipedia.org/wiki/Wikipedia_talk:Signs_of_AI_writing, https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup, https://github.com/blader/humanizer/issues and its pull requests (proposed tells land there weeks before a release)
- Per-model counts: https://graphite.io/five-percent/research (dated per-model tell reports with raw data), Arena posts via news coverage; for OpenAI use the cdn.openai.com PDFs, since openai.com returns 403
- `"signs of AI writing" OR "AI writing tells" new patterns <year>`; `"em dash" Claude OR ChatGPT study <year>`
- `"AI vocabulary" overused words study <year> site:arxiv.org`

Tooling (skills, plugins, MCP servers, scripts, knowledge graphs built for this subject):

- `gh search repos humanizer --sort stars` and `gh search repos slop --sort stars`; then read the SKILL.md of the top three prose skills (blader/humanizer, hardikpandya/stop-slop, petergyang/no-ai-slop as of 2026-09-25) for version bumps and new patterns
- `gh search repos "ai writing" lint OR vale OR checker`, plus `textlint "AI tells"` and `vale style "AI tells"`, for deterministic checkers that could replace or feed `scripts/tells.py`; recheck tbhb/vale-ai-tells and berelevant-ai/slopless (pointed to since 2026-10-17) for new rules worth copying
- `path:SKILL.md "<topic>"` on GitHub code search, sorted by recently updated; `npx skills find "<topic>"` and skills.sh for install counts
- `https://registry.modelcontextprotocol.io/v0/servers?search=<topic>`; fallback `"<topic>" mcp server site:glama.ai OR site:pulsemcp.com`
- `"<topic>" skill OR plugin OR "mcp server" <year> site:github.com`
- Most used: skills.sh weekly and 24-hour installs for `<topic>` (never all-time; exclude meta and installer skills); `anthropics/claude-plugins-official` and `claude-plugins-community` searched for `<topic>` (record the tier)
- Practitioner test on every candidate: commit in the last 90 days, issues answered, no bundled `*.test.*` or `conftest.py` from an unknown author, author has other work in the area, ships `evals/` or paired results; `path:SKILL.md "<topic>" evals OR benchmark`
- Provenance tiebreaker: which model and reasoning setting wrote each candidate (`evals.json` / frontmatter `model`, README or changelog credit, commit messages); prefer the latest frontier model at its highest reasoning setting, read over inferred
- Supersession sweep: `"<topic>" skill deprecated OR superseded OR archived <year>`; archive flag on every tool already listed here

Most discussed and the converged thinking (comment volume over points; what the most-used and most-discussed sources agree on becomes a claim in Current understanding):

- `hn.algolia.com/api/v1/search_by_date?query=<topic>` and `site:reddit.com/r/ClaudeAI OR r/ClaudeCode "<topic>" <month>`
- OpenAlex `works?search=<topic> agent&sort=cited_by_count:desc&filter=from_publication_date:<last check>`; the two most-cited through Semantic Scholar

Practice (how others use AI agents on this goal, and everything in between):

- `"how I use" OR "my workflow" "<topic>" "claude code" OR codex OR cursor <year>`
- `site:arxiv.org "<topic>" agent "case study" OR empirical OR telemetry <year>`
- `"<topic>" site:simonwillison.net OR site:latent.space OR site:anthropic.com/engineering <year>`; hn.algolia.com `"<topic>" agent` sorted by date

Testing (how work on this subject is verified, and how skills for it are tuned):

- `"<topic>" verify OR validate OR "smoke test" OR checker agent <year>` (what evidence shows the job was done)
- `path:SKILL.md "<topic>" test OR eval OR evals` on GitHub; `"<topic>" evals OR "eval suite" OR regression "agent skill" <year>`
- `site:arxiv.org "<topic>" agent evaluation OR benchmark <year>`; promptfoo, Inspect or DeepEval docs for assertion types that fit this subject

Best sources (primary first): Wikipedia "Signs of AI writing" and its cited studies; https://raw.githubusercontent.com/blader/humanizer/main/SKILL.md; https://raw.githubusercontent.com/hardikpandya/stop-slop/main/SKILL.md; https://raw.githubusercontent.com/petergyang/no-ai-slop/HEAD/skills/no-ai-slop/SKILL.md; tropes.fyi (pattern directory linked from Wikipedia, not yet read); for watermarks, https://www.anthropic.com/news/claude-text-watermark, https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content, https://ai.google.dev/responsible/docs/safeguards/synthid, Wikipedia "Text watermarking", and `site:arxiv.org watermark "AI Act"` (openai.com returns 403 and Nature needs a login: use ar5iv or secondary quotes). Sources that proved noisy: "AI detector" and "undetectable AI" tool sites (they sell evasion, not writing quality); SEO listicles; aiindigo, theairankings and watermark-remover sites. skills.sh's `api/search?q=` gives all-time installs only.

## Findings log

Newest first. One entry per material finding; a quiet refresh gets one entry saying so. `Track` is subject, tooling, practice, or testing.

<!-- tells: off -->
### R-20261030-1 · 2026-10-30 · Subject: Wikipedia splits markup tells to WP:AIMARKUP and tags emoji-as-formatting historical

- Summary: 46 edits since 2026-10-17 (history read, sections not fetched). Markup signs moved to a subpage, WP:AIMARKUP (2026-10-23; the new mark-tag highlighting section moved there 10-29); "Emoji as formatting" tagged possibly historical (10-21); "Hedging disclaimers about source availability" broken down by timeframe; the non-native-English note deleted as no longer applying (10-20); the AI vocabulary density section flagged unsourced; new comment-specific indicators. No new prose tell the skill lacks; the no-emoji formatting rule stays (good style, not only a tell). Search plan now names WP:AIMARKUP. Tooling: blader/humanizer still 3.1.0 (one manifest fix). Testing: nothing new.
- Track: subject, tooling
- Sources: https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&action=history, https://github.com/blader/humanizer/releases
- Magnitude: 0.2
- applied: none (research and search plan only)

### R-20261017-9 · 2026-10-17 · Tooling: claudisms.ai, a public-domain banlist of Claude-leaning phrases
- Summary: claudisms.ai (CC0, /claudisms.md download, maintainer unnamed, from 2026-09-08) lists "this matters", "quietly", "doing the work", "compounds", "carry", "honestly", "most people", each with a reason and a replacement. A source to diff the word list against; too unvetted to copy wholesale.
- Track: tooling
- Sources: https://claudisms.ai/
- Magnitude: 0.15
- Applied: none (note)

### R-20261017-8 · 2026-10-17 · Testing: SlopShape, structure alone detects AI web posts
- Summary: arXiv 2609.15369 (v3, 2026-09-28) reports 97.0 macro-F1 from 176 structural features, 96.1 after each model reworded its own posts, and 68.6 percent attribution to the source model. Single author, vendor-affiliated, features applied by an LLM. Supports "structure outlasts vocabulary".
- Track: testing
- Sources: https://arxiv.org/abs/2609.15369
- Magnitude: 0.15
- Applied: none (backs Current understanding)

### R-20261017-7 · 2026-10-17 · Subject: Wikipedia retires the em-dash sign and adds a GPT-6 era
- Summary: On 2026-10-07 a temporary account moved "Overuse of em dashes" to Historical indicators (2022 to September 2026). "Words to watch" now ends the GPT-5 era at mid-2026 and adds "Mid-2026 and on (GPT-6)": challenge, clearer, dependable, echoed, foster, leverage, matters, multifaceted, practical, prioritize, quietly, steady, universally, with more periods and commas and sentences held to about 8 to 20 words. Also added since 10-06: canned user pages, placeholder text, unusual link formatting, comment-specific signs, hedging disclaimers. Open talk-page proposals: `<mark>` tags, "X rather than Y" source disclaimers, "X identified Y as Z" attribution.
- Track: subject
- Sources: https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing, https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&action=history, https://en.wikipedia.org/wiki/Wikipedia_talk:Signs_of_AI_writing
- Magnitude: 0.5
- Applied: C-20261017-2, C-20261017-3

### R-20261017-6 · 2026-10-17 · Testing: a humanizer pass clears words but makes rhythm more uniform
- Summary: blader/humanizer issue #229 (closed 2026-09-28; corpora and scripts in itsryanlenk/humanist) ran a blind test. The rewrite won 16 of 16 pairwise quality judgments, but the AI-detected share only moved from 100 to 98.6 percent (97.8 with a checker added) and Pangram 4.0 called every variant AI. Vocabulary hits went 70 to 0 and dash hits 60 to 0, while uniform-beat hits rose 60 to 101 and aphoristic closers 38 to 61. The add-on checker gave no measurable benefit. A check on sentence-length spread is the missing piece.
- Track: testing
- Sources: https://github.com/blader/humanizer/issues/229
- Magnitude: 0.35
- Applied: C-20261017-3

### R-20261017-5 · 2026-10-17 · Tooling: blader/humanizer 3.1.0 adds "writing for the wrong reader"
- Summary: blader/humanizer is at 3.1.0 (about 57.8k stars, pushed 2026-10-16). New section F covers re-explaining what the reader knows; pattern 25 now covers text describing itself; it states that beating detectors is not a goal (PR #294). Approved PR #308 adds four tells: a last line echoing the first, "In today's fast-paced world" and "As we all know", a question the next sentence answers ("Why? Because"), and a reply that restates the user ("You mentioned that"). No invisible-Unicode handling and no prose checker. hardikpandya/stop-slop (18.1k stars) has not been pushed since 2026-03-17; petergyang/no-ai-slop (12.5k) is unchanged since 2026-09-02. skills.sh all-time installs: op7418/humanizer-zh 53k, blader/humanizer 9.7k.
- Track: tooling
- Sources: https://raw.githubusercontent.com/blader/humanizer/main/SKILL.md, https://raw.githubusercontent.com/blader/humanizer/main/CHANGELOG.md, https://github.com/blader/humanizer/pull/308, https://skills.sh/api/search?q=humanizer
- Magnitude: 0.3
- Applied: C-20261017-2

### R-20261017-4 · 2026-10-17 · Subject: Opus 5.5 nearly stopped using em dashes; "this matters" is its top tell
- Summary: Graphite (marketing firm, not peer reviewed, raw data CC BY 4.0) compared 9,974 aligned topics. Opus 5.5 uses 0.015 em dashes per 1,000 words, against 2.92 for Opus 5 and 3.14 for human writing. Its top tells as multiples of the human rate: "this matters" 116x, "is more than a _ it" 98x, "why _ matters" 92x, "looking ahead the" 40x, "rather than simply" 32x, "adds another layer" 27x, "what comes next" 24x, "dependable" 23x. Arena found the same dash drop on 2026-09-26 (15.2 to 0.8 per 1,000 words). The Economist's July finding now holds only for older Claude models. The checker caught only "this (distinction|part|point) matters".
- Track: subject
- Sources: https://graphite.io/five-percent/research/ai-tells-opus-5-5-update, https://bleepingcomputer.com/news/artificial-intelligence/claude-opus-55-uses-95-percent-fewer-em-dashes-but-its-answers-are-getting-longer
- Magnitude: 0.5
- Applied: C-20261017-2

### R-20261017-3 · 2026-10-17 · Tooling: maintained deterministic prose checkers now exist
- Summary: tbhb/vale-ai-tells (MIT, 119 stars, v1.37.0, pushed 2026-10-17) is a Vale package of 137 rules with a commit-message style, a pre-commit hook and a false-positive test file. berelevant-ai/slopless (MIT, 335 stars, pushed 2026-10-17) is a textlint rule set with a CLI (`npx slopless "docs/**/*.md"`, exit 0/1/2, JSON) and `install-skill claude|codex`. Neither scans for invisible Unicode. The earlier claim that the only checker found had 3 stars is out of date; the claim that no top humanizer skill ships one still holds. Response: point, for teams already running Vale or textlint in CI.
- Track: tooling
- Sources: https://github.com/tbhb/vale-ai-tells, https://github.com/berelevant-ai/slopless
- Magnitude: 0.4
- Applied: C-20261017-4

### R-20261017-2 · 2026-10-17 · Subject: SynthID Detector opens to the public, not for text
- Summary: Google opened the SynthID Detector worldwide in English on 2026-10-07 for images, video and audio (sign-in, about 10 checks a day); it also reads OpenAI, NVIDIA and Kakao marks. The post says nothing about text. So text watermarks from Claude, Gemini and OpenAI still have no public checker.
- Track: subject
- Sources: https://blog.google/innovation-and-ai/models-and-research/google-deepmind/synth-id-ai-content/
- Magnitude: 0.2
- Applied: C-20261017-1

### R-20261017-1 · 2026-10-17 · Subject: OpenAI watermarks ChatGPT and Codex text in the EU (textGrain)
- Summary: OpenAI announced textGrain on 2026-10-05: a statistical watermark in word choice with no added characters (a keyed Gumbel coupling solved as optimal transport over vocabulary blocks, under an entropy budget). It rolls out over the following weeks to eligible ChatGPT and Codex users in the EU; API users anywhere can opt in for select models, off by default. Detection is limited to approved researchers. OpenAI's own numbers: swapping 10 percent of words for synonyms drops detection from about 92 to 66 percent, 25 percent drops it to 17. Short text, math and translations are harder. Replaces "ChatGPT text carries no watermark". Read from the technical report; openai.com returned 403.
- Track: subject
- Sources: https://cdn.openai.com/pdf/e9508624-d767-41b6-a26d-e34ca798ada6/textgrain-entropy-calibrated-watermarking-for-language-model-text.pdf, https://techcrunch.com/?p=3173997
- Magnitude: 0.6
- Applied: C-20261017-1

### R-20260928-6 · 2026-09-28 · Tooling: invisible-character marks; the checker had no Unicode scan
- Summary: Reports in April 2025 found U+202F in long o3/o4-mini answers; OpenAI called it a reinforcement-learning quirk, not a watermark, and a retest two days later found none. Characters used as covert marks or smuggling carriers: U+200B to U+200D, U+2060, U+FEFF, U+00AD, U+00A0, U+202F, bidi controls (U+202A to U+202E, U+2066 to U+2069), tag characters (U+E0000 to U+E007F) and variation selectors. Only web tools scan for them; `tells.py` did not.
- Track: tooling
- Sources: https://www.rumidocs.com/newsroom/new-chatgpt-models-seem-to-leave-watermarks-on-text, https://en.wikipedia.org/wiki/Tags_(Unicode_block)
- Magnitude: 0.4
- Applied: C-20260928-1

### R-20260928-5 · 2026-09-28 · Testing: classifier detectors on short and non-native text
- Summary: Seven detectors flagged over 61 percent of human TOEFL essays as AI (Liang et al., Patterns, 2023). Pangram advises against screening single sentences, lists, outlines or math. GPTZero's 250-character minimum and Binoculars' best length of about 256 tokens come from secondary pages (unverified).
- Track: testing
- Sources: https://arxiv.org/abs/2304.02819, https://www.pangram.com/blog/all-about-false-positives-in-ai-detectors, https://arxiv.org/abs/2401.12070
- Magnitude: 0.15
- Applied: none (backs Current understanding)

### R-20260928-4 · 2026-09-28 · Subject: how watermark detection works and where it stops
- Summary: Kirchenbauer et al. (2023) count "green" tokens and run a z-test; at z above 4 the false-positive rate is 3 in 100,000, and a mark shows in as few as 25 tokens when the text has entropy. They note that for low-entropy text, humans and machines give "similar if not identical" completions, so no test can tell them apart. Christ, Gunn and Zamir: low-entropy outputs are never watermarked in an undetectable scheme. Sadasivan et al. bound any detector's AUROC by 1/2 + TV - TV^2/2, and recursive paraphrase took one watermark from 99.8 to 1.3 percent AUROC. Zhang et al. (ICML 2024): strong watermarking is impossible against an attacker with quality and perturbation oracles. Mazor, Morgan and Pass (April 2026) need only constant entropy per token, still not zero. Answers Mark's question: the lower limit is entropy, not length.
- Track: subject
- Sources: https://ar5iv.labs.arxiv.org/html/2301.10226, https://arxiv.org/abs/2306.09194, https://arxiv.org/abs/2303.11156, https://arxiv.org/abs/2311.04378, https://arxiv.org/abs/2604.12051
- Magnitude: 0.2
- Applied: C-20260928-1

### R-20260928-3 · 2026-09-28 · Subject: EU AI Act Art. 50 and China's labelling rules
- Summary: Art. 50(2) (applies from 2026-08-02) makes providers mark synthetic text in a machine-readable way, exempting "an assistive function for standard editing". Art. 50(4) makes deployers disclose AI text on matters of public interest unless it had human review and editorial responsibility. About 190 organisations signed the Code of Practice, reportedly including Anthropic, Google, OpenAI, Meta, Microsoft and Mistral. The Digital Omnibus gives systems already on the market until 2026-12-02. China's Measures (2025-09-01) require visible and metadata labels.
- Track: subject
- Sources: https://artificialintelligenceact.eu/article/50/, https://digital-strategy.ec.europa.eu/en/news/commission-publishes-code-practice-marking-and-labelling-ai-generated-content, https://www.whitecase.com/insight-alert/eu-ai-omnibus-enters-force-amending-ai-act, https://www.chinalawtranslate.com/en/ai-labeling/
- Magnitude: 0.3
- Applied: C-20260928-1

### R-20260928-2 · 2026-09-28 · Subject: OpenAI and Google text watermarks
- Summary: OpenAI built a text watermark and shelved it in 2024. It said the mark resists local paraphrase but is easy to defeat by translation, rewording with another model, or inserting and deleting a character between words, and it cited stigma for non-native speakers. As of September 2026 ChatGPT text is unmarked and OpenAI "aims to" add marking (secondary sources; openai.com returned 403). Google has marked Gemini text with SynthID since 2024 and open-sourced SynthID-Text (HF Transformers 4.46+). Google says it is weaker on factual answers and after thorough rewriting or translation. The SynthID Detector portal is waitlist-only. An independent test (Nemecek et al., 2026-09-09) caught 39 percent of marked texts at 200 tokens, AUROC 0.55 to 0.57 on code, and found no public way to test the deployed systems.
- Track: subject
- Sources: https://techcrunch.com/2024/08/04/openai-says-its-taking-a-deliberate-approach-to-releasing-tools-that-can-detect-writing-from-chatgpt/, https://ai.google.dev/responsible/docs/safeguards/synthid, https://github.com/google-deepmind/synthid-text, https://arxiv.org/html/2609.09604v1
- Magnitude: 0.3
- Applied: C-20260928-1

### R-20260928-1 · 2026-09-28 · Subject: Anthropic watermarks Claude text
- Summary: Announced 2026-08-14: Claude text carries a statistical watermark based on SynthID-Text, applied when words are sampled. "Nothing is added to the text and there are no hidden characters." It covers models from 2026-08-02 (the support page lists Fable 5.1, Mythos 5.1, Opus 5.5, Sonnet 5.5 and Haiku 4.5), with earlier models added through December 2026. The detector is a private preview for eligible organisations under EU law. Anthropic's stated limits: short passages give too little signal; factual passages and code carry less; heavy editing, paraphrase, translation or mixing into other writing can lose it; "a complete rewrite where every word is replaced" removes it. Verified on both pages 2026-09-28. So text this skill writes on Claude carries the mark, and style edits do not remove it.
- Track: subject
- Sources: https://www.anthropic.com/news/claude-text-watermark, https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content
- Magnitude: 0.6
- Applied: C-20260928-1

### R-20260925-5 · 2026-09-25 · Verification: named patterns beat detectors
- Summary: Wikipedia's caveats cite 2025 studies: detector tools (GPTZero, Pangram) have non-trivial error rates and are fooled by paraphrase; most people detect AI text at chance, heavy LLM users about 90 percent. The skill therefore proves its work with the checker's named hits and a facts-preserved check, never a detector score. Practice track not searched this round (open question).
- Track: testing
- Sources: https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing (Caveats), https://aclanthology.org/2025.acl-long.267/
- Magnitude: 0.1
- Applied: C-20260925-4

### R-20260925-4 · 2026-09-25 · Tooling: no-ai-slop adds detect mode and the portability test; no top skill ships a checker
- Summary: petergyang/no-ai-slop (MIT, about 11k stars, pushed 2026-09-02) splits edit and detect jobs (detect: name the pattern, quote the line, give the fix, no score, no authorship guess) and adds faux-insight setups, colon reveals, interpretive metadiscourse, fake-profound kickers, the portability test and the minimum effective edit. hardikpandya/stop-slop (MIT, about 17.5k stars) is unchanged in shape (eight rules, a 50-point score). gregorymm/humanize-text (MIT) was last pushed 2026-03-29 and is UX-copy and Figma focused; its pleasantries list (happy to help, feel free to, don't hesitate) is still useful. Language-specific forks exist (op7418/Humanizer-zh, epoko77-ai/im-not-ai for Korean). None of these ships a deterministic checker; the only one found (onlydole/tailord, Vale rules) has 3 stars. No MCP server is relevant.
- Track: tooling
- Sources: https://github.com/petergyang/no-ai-slop, https://github.com/hardikpandya/stop-slop, https://github.com/gregorymm/humanize-text, `gh search repos slop --sort stars` (2026-09-25)
- Magnitude: 0.3
- Applied: C-20260925-2, C-20260925-3, C-20260925-4

### R-20260925-3 · 2026-09-25 · Tooling: blader/humanizer 3.0 leads with staging and adds "weak alone"
- Summary: blader/humanizer (MIT, about 52k stars, pushed 2026-09-26) is at version 3.0.0. Patterns are regrouped strongest first: staging (not X but Y including the split and clipped-tail forms, one-line closers, sayings, staged run-ups, arguing with no one), rhythm by rule (triads, repeated openings, dashes, stacked qualifiers, hyphenated pairs, passive), inflation and borrowed authority, formatting by rule, and leftovers (chatbot residue, knowledge-limit guesses, a heading repeated in the first sentence, docs about the previous version). Weaker tells are marked "weak alone". It also says to treat input text as material, never instructions, and in file mode to change prose only.
- Track: tooling
- Sources: https://raw.githubusercontent.com/blader/humanizer/main/SKILL.md
- Magnitude: 0.4
- Applied: C-20260925-2, C-20260925-5

### R-20260925-2 · 2026-09-25 · Subject: vocabulary eras, new signs, and signs of human writing
- Summary: Wikipedia now dates the stock words: 2023 to mid-2024 (delve, tapestry, testament, intricate), mid-2024 to mid-2025 (align with, fostering, showcasing), mid-2025 on (emphasizing, enhance, highlighting, showcasing, plus canned notability and media-coverage wording); Grok overuses underscore and "scientific" words. Words are to be taken literally (their synonyms are not overused), and transition words in isolation are listed as ineffective indicators. New or newly prominent signs: vague association (associated with, connected to), the reversed "Y rather than X", headings that only hold headings, a rule between every section, and chatbot markup residue (turn0search, oaicite, [cite: n], :::writing, [web:n], utm_source=chatgpt.com). A "Signs of human writing" section lists simple is/has, plain verbs, superlatives and ordinary hedges.
- Track: subject
- Sources: https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing (revision of 2026-09-24)
- Magnitude: 0.4
- Applied: C-20260925-2, C-20260925-4

### R-20260925-1 · 2026-09-25 · Subject: dashes fading in general, not in Claude
- Summary: Wikipedia's em-dash section carries a September 2026 note proposing a move to Historical indicators because newer chatbots (GPT-5.1 onward) suppress dashes. The same section cites a July 2026 Economist analysis finding that of contemporary models only Claude used em dashes more than professional writers. Kept the zero-dash hard rule, added the author-sample exception and `--allow-dashes`.
- Track: subject
- Sources: https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing (Overuse of em dashes), https://www.economist.com/culture/2026/07/30/how-to-spot-ai-writing
- Magnitude: 0.2
- Applied: C-20260925-2

### R-20260821-1 · 2026-08-21 · Initial research (migrated from write-human)
- Summary: The original write-human skill distilled the three most-starred humanizer skills at the time (blader/humanizer, hardikpandya/stop-slop, gregorymm/humanize-text), all built on Wikipedia's "Signs of AI writing", and added explicit density rules (sentence length, paragraph length, plain words, front-loading) that none of them had. Subject track only; tooling was the three skills themselves; no testing track.
- Track: subject
- Sources: https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing, https://github.com/blader/humanizer, https://github.com/hardikpandya/stop-slop, https://github.com/gregorymm/humanize-text
- Magnitude: n/a (initial)
- Applied: C-20260821-1
<!-- tells: on -->
