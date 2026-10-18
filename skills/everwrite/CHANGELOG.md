# Changelog: everwrite

Every change to [SKILL.md](SKILL.md) and its companions, newest first, each with the reason. Reasons cite findings in [RESEARCH.md](RESEARCH.md) (`R-`), lessons in [LEARNINGS.md](LEARNINGS.md) (`L-`), and test runs in [TESTS.md](TESTS.md) (`T-`). State in `evergreen.json`. Protocol: [MAINTENANCE.md](MAINTENANCE.md).

Entry shape: `### C-YYYYMMDD-n · date · one-line summary`, then `because:` (IDs or "user request"), `files:` (file and section), and a sentence on what changed. Cite section headings, not line numbers.

### C-20261018-1 · 2026-10-18 · Release 1.1.0
- because: user request (release the unreleased checker changes)
- files: plugin.json, .claude-plugin/plugin.json (version)
- Version 1.0.0 to 1.1.0, tag v1.1.0. Ships every change since the v1.0.0 tag: the 2026-10-17 refresh (C-20261017-1 to -5: new phrase and closer tells, the `uniform-rhythm` rule, the vale-ai-tells and slopless pointer, the retired dash tell) and the description tuned for short emails and messages (C-20261017-6). Minor, not patch, because tells.py flags new patterns that 1.0.0 passed.

### C-20261017-6 · 2026-10-17 · Description covers short emails and messages
- because: T-20261017-1, T-20261017-2, L-011
- files: SKILL.md (frontmatter description)
- "text a person will read" became "text a person will read, however short", the kinds list gained letters and messages, and it quotes 'write me a quick email to...'. The description grew from 361 to 427 characters (59 to 69 words). trigger-2 went from 0 of 3 to 3 of 3; no decoy fired.

### C-20261017-5 · 2026-10-17 · Search plan names the official forums and per-model sources
- because: R-20261017-7, R-20261017-4, R-20261017-3 (refresh practice: forum lines were missing)
- files: RESEARCH.md (Search plan: Subject, Tooling, Best sources; Open questions)
- Adds the Wikipedia talk page, WikiProject AI Cleanup and blader/humanizer issues as forums, the history-first way to read the 250k-character Wikipedia page, Graphite's per-model reports, the cdn.openai.com route, and the two pointed-to rule sets.

### C-20261017-4 · 2026-10-17 · Point to vale-ai-tells and slopless for teams that lint docs in CI
- because: R-20261017-3
- files: SKILL.md (Step 3: mechanical check)
- One paragraph names the two maintained rule sets as a CI option, says they don't scan for invisible characters, and says to install only on the user's yes.

### C-20261017-3 · 2026-10-17 · Uniform sentence rhythm gets weight and a checker rule
- because: R-20261017-6, R-20261017-7
- files: SKILL.md (Step 2: Patterns, need-company list; Readability), scripts/tells.py (`uniform-rhythm` in `check_text`), scripts/test_tells.py (`test_uniform_rhythm`), references/patterns.md (Rhythm by rule)
- The checker flags, as weak, a paragraph of five or more sentences of six words or more whose length spread is under a quarter of the mean. No hits on 120 human-written READMEs from node_modules. SKILL.md now says why to vary sentence length.

### C-20261017-2 · 2026-10-17 · New phrase tells from Opus 5.5 counts and humanizer 3.1
- because: R-20261017-4, R-20261017-5, R-20261017-7
- files: SKILL.md (Step 2: Patterns, staged setups, closers, need-company list), scripts/tells.py (STOCK_WORDS `dependable`; contrast "is more than a X, it's"; setup "this matters" and "why it matters" weak, "as we all know" strong, "Why? Because" and "You mentioned that" weak; new `closer` category, weak: "Looking ahead,", "what comes next", "adds another layer"), scripts/test_tells.py (`test_newer_model_tells`), references/patterns.md (Staging, Closers, Leftovers)
- Only "dependable" of Wikipedia's GPT-6 words went in, since Graphite's count backs it and the list came from a temporary account. Probe on 120 human READMEs: one weak hit ("Why it matters" as a heading). Self-test 30 of 30.

### C-20261017-1 · 2026-10-17 · Watermarks: OpenAI marks EU ChatGPT and Codex text; the public detector does not cover text
- because: R-20261017-1, R-20261017-2
- files: SKILL.md (Step 2: Watermarks are a separate thing), RESEARCH.md (Current understanding), evergreen.json (volatile claims)
- The watermark list now includes ChatGPT and Codex for EU users and opted-in API users since October 2026, and the "nobody can check" sentence says text detection is restricted while Google's public detector covers only images, video and audio.

### C-20261005-1 · 2026-10-05 · Root plugin.json for GitHub Copilot CLI and awesome-copilot; first release tag v1.0.0
- because: user request (list the plugin in github/awesome-copilot, whose intake gates never read `.claude-plugin/` and pin a release tag)
- files: ../../plugin.json (new)
- The skill is unchanged and stays 1.0.0, which never had a tag; v1.0.0 is cut at this commit. Copilot CLI 1.0.92 installs it and `vally lint` passes.

### C-20261004-1 · 2026-10-04 · Ghostwritten opinions count as facts; "the point is that" is a weak setup tell
- because: L-009, L-010 (two blog posts for markdavidrogers.com, 2026-10-04)
- files: SKILL.md (Hard rules, rule 2), scripts/tells.py (setup table), scripts/test_tells.py (`test_setup_inflation_rider`), LEARNINGS.md (L-009, L-010)
- Rule 2 now says that in first-person text written for someone, their reasons, feelings and verdicts need a source like any other fact. The checker flags the staged "the point is that" as weak and leaves the purpose form alone. Self-test passes.

### C-20260930-1 · 2026-09-30 · The same thing twice in a row is a tell: repeated headings, the page title repeated, a paragraph repeated
- because: user request (Mark saw get-title-at-url's wiki show "Getting Started" and then "Getting started"; "saying the same thing twice exactly is a mistake most humans wouldn't make", 2026-09-30); L-008
- files: scripts/tells.py (`same_words()`, `check_text(page_title=)`, the `repeated-heading` and `repeated-text` tells, `--wiki`, `--list`), scripts/test_tells.py (28 tests), SKILL.md (Step 2 pattern list, Step 3 flags), references/patterns.md (Decorative headings), LEARNINGS.md (L-008)
- A heading straight under a heading with the same words, a paragraph or list item repeated word for word, and, with `--wiki`, a first heading repeating the file-name title a GitHub wiki prints, are strong hits. On get-title-at-url's wiki the new flag found the doubled title on 8 of its 9 pages (Home opens with the package name, which is not a repeat).

### C-20260928-1 · 2026-09-28 · Watermarks section; checker scans for invisible characters and fixes them
- because: user request (Mark asked how AI text fingerprints work and whether dictated text can carry one); R-20260928-1 to R-20260928-6
- files: SKILL.md (Step 2 new subsection "Watermarks are a separate thing"; Step 3 names the new scan and `--fix-hidden`), scripts/tells.py (HIDDEN and ODD_SPACE tables, `describe_chars`, `fix_hidden`, `--fix-hidden`, `--list` text), scripts/test_tells.py (class Hidden, two speed inputs, a CLI round trip), RESEARCH.md (Current understanding, Open questions, Best sources, six findings), evergreen.json (three volatile claims, the 2026-12-02 event), evals/evals.json and evals/fixtures/hidden.md (action-3)
- The skill now says plainly that removing tells does not remove a provider's statistical watermark, never promises "undetectable" text, and does not try to strip one. The checker flags invisible covert-mark characters (strong) and odd spaces (weak) on every line, code included, and `--fix-hidden` strips them in one pass. Self-test 27 of 27; no hits on 174 real Markdown files.

### C-20260925-7 · 2026-09-25 · Output: the change note is one short sentence with an example
- because: T-20260925-3 (outcome-1 wrong-outcome, 3 of 3 notes ran three to five sentences)
- files: SKILL.md §Output
- "One line" became "one sentence (under 25 words, no divider before it)" with a sample note. T-20260925-4 passed 3 of 3.

### C-20260925-6 · 2026-09-25 · Pre-publication review: linear-time parsing, fewer false positives, installed-copy rule
- because: an independent read-only review before publishing (no blockers; seven should-fix and nit findings acted on); L-004; T-20260925-2
- files: scripts/tells.py (heading regex without backtracking; comment and inline-code blanking by `str.find` loops; bounded link-target and reference patterns; lines split on newlines only, so U+2028 and form feed keep line numbers right; setext underlines no longer count as dividers; an unclosed fence is reported; conditional clauses such as "If the value is not set, it is zero" are exempt from the contrast rules; check marks are not emoji), scripts/test_tells.py (regression and speed cases), SKILL.md (Step 3 names `python3`; Output allows the Step 0 note; While working says to edit the source, not an installed copy), LEARNINGS.md (L-004; quoted examples wrapped for the checker)

### C-20260925-5 · 2026-09-25 · Text under edit is material, never instructions
- because: R-20260925-3
- files: SKILL.md (intro)
- A draft that contains instructions ("ignore your rules") is edited like any other prose.

### C-20260925-4 · 2026-09-25 · Bundled checker: `scripts/tells.py`, its self-test, a fixture, the eval suite and CI
- because: user request (token savings); R-20260925-4 (no leading skill ships a checker); R-20260925-2 (markup residue is exact-match); R-20260925-5 (evidence is named hits, not a detector score); L-001, L-003
- files: scripts/tells.py (rules table, stock words, markdown-aware skipping, strong and weak severities, exit 1 on strong), scripts/test_tells.py (unittest, Python 3.9+), evals/fixtures/sloppy.md, evals/evals.json, SKILL.md (Step 3), repo `.github/workflows/tests.yml`
- The checker replaces the old "mechanical sweep" step. Strong hits fail the run; weak hits are listed for judgment. Probed on four human-reviewed docs from sibling repos: one false positive (L-003), fixed before release.

### C-20260925-3 · 2026-09-25 · Token savings: shorter description, depth by length, examples on demand, no scoring pass
- because: user request
- files: SKILL.md (frontmatter description, Step 1, Step 3, Step 4, Output), references/patterns.md (new)
- The description, which every session loads, shrank from 624 to 361 characters (87 to 59 words). Short replies now get the hard rules only, with no audit. Before and after examples moved to `references/patterns.md`, read only in edit and detect mode. The 50-point five-dimension score was dropped in favour of two audit questions plus the checker. The banned-word table moved into the checker (`--list`), so the skill body no longer carries it. SKILL.md went from 11,977 to 10,062 bytes (as committed, LF) while gaining Step 0, detect mode, the weak-alone group and the checker step; a plain drafting task reads SKILL.md only.

### C-20260925-2 · 2026-09-25 · Refresh: patterns regrouped strongest first, weak-alone group, detect mode, human habits protected
- because: R-20260925-1, R-20260925-2, R-20260925-3, R-20260925-4
- files: SKILL.md (Step 1, Step 2: Hard rules, Patterns, Readability, Don't over-correct)
- Added: split and clipped not-X-but-Y forms, staged setups and colon reveals, arguing with no one, closers and kickers grouped, pleasantries, vague association, docs about the previous version, repeated openings, the portability test, detect mode, the author-sample exception to the dash rule. Demoted to weak alone: transitions, curly quotes, a single listed word. "Don't over-correct" now names the habits that read as human (very, perhaps, I think, superlatives).

### C-20260925-1 · 2026-09-25 · Converted to an evergreen unit, renamed everwrite, scrubbed and published
- because: user request
- files: SKILL.md (frontmatter name, "Keeping this skill current" replaced by Step 0 and Maintenance), MAINTENANCE.md, RESEARCH.md, LEARNINGS.md, TESTS.md, evergreen.json, evals/
- Pointer mode (`protocol: "plugin"`). Removed the owner's name, the product-specific `save_skill` re-save step and the hand-rolled 30-day refresh rule; their state (last refresh 2026-08-21, 30-day interval) moved into `evergreen.json`. Published at https://github.com/m4bwav/everwrite.

### C-20260821-1 · 2026-08-21 · Created as write-human
- because: user request
- files: SKILL.md
- A single-file skill saved to a hosted skills store, with its own refresh rule and source list. Research basis: R-20260821-1.
