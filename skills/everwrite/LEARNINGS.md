# Learnings: everwrite

Procedural lessons for [SKILL.md](SKILL.md). Research findings live in [RESEARCH.md](RESEARCH.md); every change is logged in [CHANGELOG.md](CHANGELOG.md); test runs in [TESTS.md](TESTS.md); state in `evergreen.json`. Format and write-time gate: [MAINTENANCE.md](MAINTENANCE.md) (LEARNINGS-FORMAT). Retired entries go to LEARNINGS-ARCHIVE.md with a reason.

Write an entry the moment a real signal happens: a user correction, the same error twice, a discovered workaround, an environment fact, a stated preference, a failed test or a failure in use. Check existing entries first, by meaning (`evergreen.py search "<the lesson>" --kinds learnings` finds near-duplicates in every registered unit): add / update / retire / none. Trigger and Hypothesis are required. Promote after three confirmations; retire when harmful > helpful.

## Active

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
- Trigger: `python tells.py FILE | Select-String ...` in Windows PowerShell showed em dashes as three odd characters.
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
