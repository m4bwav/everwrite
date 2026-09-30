# Log

Append-only. One line per operation: `## [YYYY-MM-DD] op | title` where op is one of add, update, supersede, verify, verify-failed, prune, handoff, index. Newest at the bottom. Never edited, only appended; this is the history the entries themselves do not carry.

## [2026-09-25] init | scaffolded
## [2026-09-25] add | decision: Bundle a stdlib checker instead of asking the model to reread
## [2026-09-25] handoff | 14 lines
## [2026-09-25] add | published m4bwav/everwrite 1.0.0 (public), converted from write-human: evergreen pointer-mode unit, tells.py checker with 21-case self-test, CI green on 3 OS x Python 3.9/3.13; skill eval suite not yet run
## [2026-09-25] handoff | 14 lines
## [2026-09-25] update | skill suite 7/7 via headless claude -p runner (T-20260925-3 6/7, tune C-20260925-7, T-20260925-4); L-005, L-006
## [2026-09-28] update | watermark research (R-20260928-1..6; Claude text watermarked since 2026-08-02, lower limit is entropy not length); tells.py hidden-char/odd-space scan and --fix-hidden, self-test 27/27; eval action-2 added, not run; uncommitted
## [2026-09-28] index | rebuilt (1 entries)
