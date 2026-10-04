# Learnings: everwrite

Procedural lessons for [SKILL.md](SKILL.md). Research findings live in [RESEARCH.md](RESEARCH.md); every change is logged in [CHANGELOG.md](CHANGELOG.md); test runs in [TESTS.md](TESTS.md); state in `evergreen.json`. Format and write-time gate: [MAINTENANCE.md](MAINTENANCE.md) (LEARNINGS-FORMAT). Retired entries go to LEARNINGS-ARCHIVE.md with a reason.

Write an entry the moment a real signal happens: a user correction, the same error twice, a discovered workaround, an environment fact, a stated preference, a failed test or a failure in use. Check existing entries first, by meaning (`evergreen.py search "<the lesson>" --kinds learnings` finds near-duplicates in every registered unit): add / update / retire / none. Trigger and Hypothesis are required. Promote after three confirmations; retire when harmful > helpful.

## Active

### L-010 · 2026-10-04 · Ghostwritten first person invents motives unless told not to
- Trigger: drafting two blog posts in Mark's name for markdavidrogers.com, the first draft said a question of his "was answered yes" and gave the whole month's work one motive. Neither was in any record; both were caught at the Step 4 reread, while every version number had been checked against the registries.
- Hypothesis: hard rule 2 reads as names, numbers and dates, so an agent checks those and still writes reasons, feelings and verdicts for the person, because a first-person blog asks for opinions.
- Rule: in first-person text written for someone, their reasons, feelings and verdicts are facts: use only what they said or their records show (logs, handoffs, notes), else write the plain version.
- Evidence: C-20261004-1; markdavidrogers-web PRs #32 and #33
- Scope: skill
- Status: promoted: C-20261004-1 · helpful 1 · harmful 0 · last_confirmed 2026-10-04

<!-- tells: off -->
### L-009 · 2026-10-04 · "The point is that" slipped past the checker
- Trigger: a blog draft had "The point is that the record lives on disk..."; `tells.py` passed it and only the reread caught the staging. The setup rules knew "the key point is" but not this form.
- Hypothesis: people also write "the point is", mostly as a purpose ("the point is to keep it small"); the staged form adds "that".
- Rule: "the (whole|main|real) point (here) is that" is a weak setup hit; the purpose form is not flagged. No hits on about 400 Markdown files across the Ai projects, so it adds no noise.
- Evidence: C-20261004-1 (`test_setup_inflation_rider`)
- Scope: skill
- Status: active · helpful 1 · harmful 0 · last_confirmed 2026-10-04
<!-- tells: on -->

### L-008 · 2026-09-30 · Saying the same thing twice in a row is a tell people don't make
- Trigger: Mark, looking at get-title-at-url's wiki: GitHub printed "Getting Started" from the file name, and the page's own `# Getting started` followed it. "Saying the same thing twice exactly is a mistake most humans wouldn't make" (2026-09-30). The wikiwright skill had taught it: its page-sets rule allowed a `#` heading repeating the title.
- Hypothesis: an agent writes each piece from its own template (a title, then a heading) and never sees the rendered page, so repeats the host or the previous block makes are invisible to it.
- Rule: never repeat the heading above, the title the host prints, or the paragraph before; `tells.py` flags them strong, with `--wiki` for wiki pages. Know what the host prints before writing the first line.
- Evidence: C-20260930-1; wikiwright C-20260930-4 (its `check` does the same for wikis)
- Scope: skill
- Status: promoted: C-20260930-1 · helpful 1 · harmful 0 · last_confirmed 2026-09-30

### L-007 · 2026-09-28 · Scripts that save tokens: let the checker find and fix invisible characters
- Trigger: Mark asked to record every net token-saving process and script for the skills in use.
- Hypothesis: invisible characters can't be seen when rereading a file, so an agent checking by eye spends tokens and still misses them; the script finds all of them in one pass.
- Rule: never hunt for hidden characters by reading; run `tells.py <file>` and, on a `hidden-char` or `odd-space` hit, `tells.py --fix-hidden <file>`, which rewrites and re-checks in one call. The existing savers still apply: the checker's summary line instead of a reread for dashes and stock words (C-20260925-3, C-20260925-4), `--json` piped to a filter when only one category matters, and a batch run over a folder instead of one file at a time.
- Evidence: C-20260928-1; test `test_fix_hidden_rewrites_file`
- Scope: skill
- Status: active · helpful 0 · harmful 0 · last_confirmed 2026-09-28

### L-006 · 2026-09-25 · Clear `tests.failing` before re-running the failed case
- Trigger: the first rerun of outcome-1 after the fix still listed outcome-1 as failing in `evergreen.json`; one of three runs followed Step 0, reported it and ended with an offer, which failed the checker.
- Hypothesis: Step 0 is part of the skill, so the unit's own state is part of every test prompt.
- Rule: after a fix, clear the flag (`evergreen.py flag <unit> --clear-failing <id>`) before the confirming rerun, and record the run with `tested` afterwards.
- Evidence: T-20260925-4, confirmed 2026-09-25
- Scope: skill
- Status: active · helpful 1 · harmful 0 · last_confirmed 2026-09-25

### L-005 · 2026-09-25 · A headless `claude -p` runner tests this skill on native Windows, including shell cases
- Trigger: `claude plugin eval` refuses shell-granting cases on native Windows (evergreen-protocol:L-019), and action-1 needs a shell to run the checker.
- Hypothesis: plain `claude -p` has no sandbox requirement; an allowlist limits the shell to Python.
- Rule: stage a fresh folder per run, then run headless Claude Code with the prompt as its standard input: `claude -p --output-format stream-json --verbose --max-turns N --settings '{"disableAllHooks":true}' --allowedTools Skill Read Glob Grep Edit Write "Bash(python:*)"`, read `tool_use` events for Skill and the `tells.py` calls, and run the checker on the result yourself. A baseline adds `"skillOverrides":{"everwrite":"off"}` to the same settings. About 0.3 USD per action or outcome run, 0.2 per trigger run.
- Evidence: T-20260925-3, T-20260925-4
- Scope: env:windows
- Status: active · helpful 2 · harmful 0 · last_confirmed 2026-09-25

### L-004 · 2026-09-25 · Every regex in the checker gets a pathological-input test
- Trigger: the pre-publication review timed the first heading regex at 45 seconds on a 3,000-character line, and the comment and link-target substitutions went quadratic on 100 KB of repeated openers.
- Hypothesis: lazy groups followed by optional trailers (`(.*?)\s*#*\s*$`) and unbounded negated classes rescanned from every start position.
- Rule: bound repeated classes, prefer `str.find` loops for delimiters, and add each new rule's worst case to `Speed.test_pathological_lines_stay_fast`.
- Evidence: C-20260925-6, T-20260925-2, confirmed 2026-09-25
- Scope: skill
- Status: active · helpful 1 · harmful 0 · last_confirmed 2026-09-25

<!-- tells: off -->
### L-003 · 2026-09-25 · A negative sentence followed by "It ..." is usually a real list, not a contrast
- Trigger: the first version flagged "It does not trigger on the user's phrasing. It triggers and narrates..." in a human-reviewed README as a strong not-X-but-Y.
- Hypothesis: the split contrast is only reliable when the same framing verb repeats ("doesn't mean X. It means Y"); other verbs repeat for ordinary reasons.
- Rule: keep split-contrast rules strong only for the "mean" frame; any other repeated verb is weak. Probe every new strong rule on a few human-reviewed docs before release.
- Evidence: C-20260925-4, confirmed 2026-09-25
- Scope: skill
- Status: active · helpful 1 · harmful 0 · last_confirmed 2026-09-25

### L-002 · 2026-09-25 · Mojibake in piped PowerShell output is the console, not the checker
- Trigger: piping `python tells.py FILE` into `Select-String` in Windows PowerShell showed em dashes as three odd characters.
- Hypothesis: PowerShell decodes a native command's piped stdout with the console code page; the script writes UTF-8 correctly (it reconfigures stdout).
- Rule: read the checker's output directly or with `--json`; don't pipe it through PowerShell cmdlets when the matches matter.
- Evidence: same run printed correctly unpiped, 2026-09-25
- Scope: env:windows-powershell
- Status: active · helpful 1 · harmful 0 · last_confirmed 2026-09-25

### L-001 · 2026-09-25 · Off and on markers count only on their own line
- Trigger: SKILL.md mentions the marker in inline code; a review of the first checker version before its first run on SKILL.md found it would read that mention as a real marker and skip the rest of the file.
- Hypothesis: markers were matched before inline code was blanked.
- Rule: a marker switches the checker only when it is the whole line; a test covers the quoted case.
- Evidence: C-20260925-4 (`test_quoted_marker_does_not_switch_off`), confirmed 2026-09-25
- Scope: skill
- Status: active · helpful 1 · harmful 0 · last_confirmed 2026-09-25
<!-- tells: on -->
