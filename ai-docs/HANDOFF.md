# Handoff

Updated 2026-09-25. Read this first, then [log.md](log.md); the skill's own history is in `skills/everwrite/` (CHANGELOG, LEARNINGS, TESTS, RESEARCH).

## Current state

- Public repository m4bwav/everwrite since 2026-09-25, version 1.0.0. CI (tests.yml) passed on Linux, macOS and Windows with Python 3.9 and 3.13.
- The skill replaces an older single-file skill named write-human that lived in a hosted skills store; that copy still exists there and should be removed so the two don't compete.
- Evergreen: refreshed 2026-09-25 (m 0.4), next due in `skills/everwrite/evergreen.json`. Three volatile claims registered.
- Checker self-test: 21 cases, including pathological-input speed cases. The skill eval suite (`evals/evals.json`, 7 cases) has not run.

## Next single action

Run the skill suite with evergreen-test (triggers, decoys, action-1 on the fixture, outcome-1) and record it with `evergreen.py tested`.
