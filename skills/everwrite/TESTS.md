# Tests: everwrite

Test runs for [SKILL.md](SKILL.md). Cases live in `evals/evals.json`. A failure that taught something is a lesson in [LEARNINGS.md](LEARNINGS.md); a fix it caused is logged in [CHANGELOG.md](CHANGELOG.md) with `because: T-...`; research it triggered is in [RESEARCH.md](RESEARCH.md); counts and the failing list are in `evergreen.json` under `tests`. Rules: [MAINTENANCE.md](MAINTENANCE.md) (testing section) and the plugin's `protocol/TESTING.md`.

A test passes on evidence (a tool call in the trace, a file, a marker, a log line), never on the transcript's claim that something was done.

Entry shape: `### T-YYYYMMDD-n · date · harness · env · passed/total`, then one line per failing case (`id · kind · class · what the evidence showed`), then `led to:` (L-, C-, R- ids or none). Newest first. Budget 150 lines; archive older runs to `TESTS-ARCHIVE.md`.

## Runs

### T-20260925-2 · 2026-09-25 · unittest (`scripts/test_tells.py`) plus an independent review · owner-pc · 21/21
- After C-20260925-6 the self-test has 21 cases, including pathological inputs (a 5,000-space heading, 20,000 comment openers, 30,000 link openers, 20,000 backticks), each under two seconds; it passed on Python 3.14 and 3.9. The reviewer's repro cases (U+2028 line numbers, a conditional negative, check marks, setext underlines, an unclosed fence) are now tests.
- The skill suite in `evals/evals.json` has still not run.
- led to: L-004, C-20260925-6

### T-20260925-1 · 2026-09-25 · unittest (`scripts/test_tells.py`), not the skill suite · owner-pc · 15/15
- The checker's self-test passed on Python 3.14 and 3.9. The fixture `evals/fixtures/sloppy.md` fails with 27 strong hits across all ten expected categories. A probe on four human-reviewed docs from sibling repos found one false positive (L-003), fixed before this run.
- The skill suite in `evals/evals.json` (triggers, decoys, action, outcome) has not run yet; run it with `evergreen-test`.
- led to: L-001, L-003, C-20260925-4
