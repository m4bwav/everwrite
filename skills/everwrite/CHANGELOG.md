# Changelog: everwrite

Every change to [SKILL.md](SKILL.md) and its companions, newest first, each with the reason. Reasons cite findings in [RESEARCH.md](RESEARCH.md) (`R-`), lessons in [LEARNINGS.md](LEARNINGS.md) (`L-`), and test runs in [TESTS.md](TESTS.md) (`T-`). State in `evergreen.json`. Protocol: [MAINTENANCE.md](MAINTENANCE.md).

Entry shape: `### C-YYYYMMDD-n · date · one-line summary`, then `because:` (IDs or "user request"), `files:` (file and section), and a sentence on what changed. Cite section headings, not line numbers.

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
