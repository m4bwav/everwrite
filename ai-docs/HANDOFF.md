# Handoff

Updated 2026-10-17. Read this first, then [log.md](log.md); the skill's own history is in `skills/everwrite/` (CHANGELOG, LEARNINGS, TESTS, RESEARCH).

## Current state

- Public repository m4bwav/everwrite since 2026-09-25, version 1.0.0. CI (tests.yml) passes on Linux, macOS and Windows with Python 3.9 and 3.13.
- Skill suite: 7/7 (T-20260925-4) with a headless `claude -p` runner (LEARNINGS L-005). outcome-1 failed first (change note too long) and was fixed by C-20260925-7. trigger-2 (a short email) fell to 0 of 3 on 2026-10-17 and was tuned the same day (C-20261017-6): 3 of 3, decoys 0 of 3 (T-20261017-2). Trigger tests run against the installed user skill, not `--plugin-dir` (L-012).
- The older write-human skill is switched off in Claude Code (`skillOverrides`); its hosted copy still exists in the account.
- Evergreen: refreshed 2026-10-17 (m 0.6: OpenAI text watermark, dash tell retired on Wikipedia, new phrase and rhythm rules in tells.py), next due in `skills/everwrite/evergreen.json`. The changed checker is unreleased: plugin.json is still 1.0.0, and a version bump and tag wait for Mark.
- GitHub wiki live since 2026-10-03 (https://github.com/m4bwav/everwrite/wiki, 9 pages, wiki commit a86ebc1); run record in [notes/2026-10-03-wiki-run/](notes/2026-10-03-wiki-run/2026-10-03-github-wiki.md).
- Submitted to the Claude directory 2026-10-03 (see log.md); waiting for scan and review.

## Next single action

Nothing owed on the eval suite. The description change in C-20261017-6 ships with the next release, which waits for Mark.

After the directory review settles: README gets the HTTPS marketplace URL, the `gh skill install` route and the `--json`/`--wiki`/`--fix-hidden` options; bump plugin.json past 1.0.0 and tag a release; shorten the long decisions file name (it breaks Windows clones under deep paths without core.longpaths).
