# Handoff

Updated 2026-09-25. Read this first, then [log.md](log.md); the skill's own history is in `skills/everwrite/` (CHANGELOG, LEARNINGS, TESTS, RESEARCH).

## Current state

- Public repository m4bwav/everwrite since 2026-09-25, version 1.0.0. CI (tests.yml) passes on Linux, macOS and Windows with Python 3.9 and 3.13.
- Skill suite: 7/7 (T-20260925-4) with a headless `claude -p` runner (LEARNINGS L-005). outcome-1 failed first (change note too long) and was fixed by C-20260925-7. trigger-2 (an email request) fired 2 of 3 runs, the weakest trigger.
- The older write-human skill is switched off in Claude Code (`skillOverrides`); its hosted copy still exists in the account.
- Evergreen: refreshed 2026-09-25, next due in `skills/everwrite/evergreen.json`.
- GitHub wiki live since 2026-10-03 (https://github.com/m4bwav/everwrite/wiki, 9 pages, wiki commit a86ebc1); run record in [notes/2026-10-03-wiki-run/](notes/2026-10-03-wiki-run/2026-10-03-github-wiki.md).
- Submitted to the Claude directory 2026-10-03 (see log.md); waiting for scan and review.

## Next single action

At the next refresh, rerun trigger-2 and consider a description phrase for everyday emails and messages if it drops below 2 of 3.

After the directory review settles: README gets the HTTPS marketplace URL, the `gh skill install` route and the `--json`/`--wiki`/`--fix-hidden` options; bump plugin.json past 1.0.0 and tag a release; shorten the long decisions file name (it breaks Windows clones under deep paths without core.longpaths).
