# Tests: everwrite

Test runs for [SKILL.md](SKILL.md). Cases live in `evals/evals.json`. A failure that taught something is a lesson in [LEARNINGS.md](LEARNINGS.md); a fix it caused is logged in [CHANGELOG.md](CHANGELOG.md) with `because: T-...`; research it triggered is in [RESEARCH.md](RESEARCH.md); counts and the failing list are in `evergreen.json` under `tests`. Rules: [MAINTENANCE.md](MAINTENANCE.md) (testing section) and the plugin's `protocol/TESTING.md`.

A test passes on evidence (a tool call in the trace, a file, a marker, a log line), never on the transcript's claim that something was done.

Entry shape: `### T-YYYYMMDD-n · date · harness · env · passed/total`, then one line per failing case (`id · kind · class · what the evidence showed`), then `led to:` (L-, C-, R- ids or none). Newest first. Budget 150 lines; archive older runs to `TESTS-ARCHIVE.md`.

## Runs

### T-20260925-4 · 2026-09-25 · headless `claude -p` runner (stream-json, fresh context per run, hooks off) · owner-pc · 7/7
- After C-20260925-7, outcome-1 passed 3 of 3: the reply piped to `tells.py -` had 0 strong hits, all seven facts matched, the file was untouched, and each change note was one sentence. The other six cases carry over from T-20260925-3 (SKILL.md changed only in its Output section).
- A first rerun before the failing flag was cleared passed 2 of 3: the third run obeyed Step 0, reported the failing test and ended with an offer ("Say if you want me to"), which the checker caught. See L-006.
- Baseline (skill off): 3 strong hits (bold labels) in the reply.
- led to: L-006

### T-20260925-3 · 2026-09-25 · headless `claude -p` runner (stream-json, fresh context per run, hooks off) · owner-pc · 6/7
- Triggers: trigger-1 3/3, trigger-2 2/3 (one run wrote the email without loading the skill), trigger-3 3/3 (detect mode each time: a findings list with fixes, no rewrite). Decoys: decoy-1 0/3, decoy-2 0/3.
- action-1 3/3: Skill, then `tells.py` on the file before and after the edit (two shell calls each run), the file changed, the final check reported 0 strong, all seven facts kept. Baseline (skill off): the file was rewritten cleanly (0 strong) but the checker never ran, so only the evidence half of the case separates the two arms.
- outcome-1 · outcome · wrong-outcome · deterministic checks passed 3/3 (0 strong, facts kept, file untouched) but every change note ran three to five sentences after a divider; SKILL.md asks for one line. Baseline (skill off): 3 strong hits (bold labels).
- Cost of the suite: about 6.2 USD in 23 runs.
- led to: C-20260925-7, L-005

### T-20260925-2 · 2026-09-25 · unittest (`scripts/test_tells.py`) plus an independent review · owner-pc · 21/21
- After C-20260925-6 the self-test has 21 cases, including pathological inputs (a 5,000-space heading, 20,000 comment openers, 30,000 link openers, 20,000 backticks), each under two seconds; it passed on Python 3.14 and 3.9. The reviewer's repro cases (U+2028 line numbers, a conditional negative, check marks, setext underlines, an unclosed fence) are now tests.
- The skill suite in `evals/evals.json` has still not run.
- led to: L-004, C-20260925-6

### T-20260925-1 · 2026-09-25 · unittest (`scripts/test_tells.py`), not the skill suite · owner-pc · 15/15
- The checker's self-test passed on Python 3.14 and 3.9. The fixture `evals/fixtures/sloppy.md` fails with 27 strong hits across all ten expected categories. A probe on four human-reviewed docs from sibling repos found one false positive (L-003), fixed before this run.
- The skill suite in `evals/evals.json` (triggers, decoys, action, outcome) has not run yet; run it with `evergreen-test`.
- led to: L-001, L-003, C-20260925-4
