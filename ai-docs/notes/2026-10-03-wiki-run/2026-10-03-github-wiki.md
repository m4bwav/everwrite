---
title: GitHub wiki written and published for everwrite 1.0.0 (master 0673975)
kind: note
date: 2026-10-03
verified: 2026-10-03
stale_after: 2027-04-03
tags: [wiki, docs, 1.0.0, github]
summary: "the everwrite wiki's pages, where the working copy is, how every example was verified against a fresh GitHub clone, facts found, inaccuracies in the shipped docs, and how to update the wiki"
---

# GitHub wiki for everwrite 1.0.0

This folder sits outside the everwrite repository on purpose: on 2026-10-03 another session was submitting everwrite to the Claude plugin directory from `master`, and every commit there triggers re-validation. Move these four files into `everwrite/ai-docs/notes/` (and add a HANDOFF line and a log entry) once that submission settles.

## Summary

Written with the wikiwright skill. Nine pages plus sidebar and footer, wiki commit `a86ebc1` on https://github.com/m4bwav/everwrite/wiki, pushed over Mark's placeholder Home page (plain fast-forward). `wikiwright.py live`: 9 pages, 0 failures, sidebar and footer render, 11 anchor links fine. `check`: 0 errors. `outputs`: 28 checked, 0 missing, 5 skipped (Claude Code commands and hand-run transcripts). `snippets`: 1 block checked, 3 commands. `tells.py --wiki`: 0 strong, 3 weak.

Pages: Home, Getting-Started, How-The-Skill-Works, What-The-Checker-Flags, Commands, Recipes, Versions-and-Upgrading, FAQ, Development, _Sidebar, _Footer.

Page set: no tested wikiwright set exists for an agent skill or plugin. Used the command-line tool set (Commands) plus a behaviour page for the skill (How-The-Skill-Works) and one for the checker (What-The-Checker-Flags), no API reference.

## Where the pages are

`../everwrite.wiki`, branch `master`, remote https://github.com/m4bwav/everwrite.wiki.git. LF, no BOM.

## Updating the wiki later

1. `git -C ../everwrite.wiki pull --ff-only`.
2. Fresh clone: `git clone https://github.com/m4bwav/everwrite.git <scratch>/src`, then `python 2026-10-03-wiki-verify.py <scratch>/src > new.txt` and the same with a Python 3.9 interpreter as the second argument. `wikiwright.py diffout 2026-10-03-wiki-verify.out.txt new.txt --skip installed`.
3. `wikiwright.py outputs <wiki> new.txt new39.txt`, `wikiwright.py snippets <wiki> 2026-10-03-wiki-verify.py`, `wikiwright.py check <wiki> --version <v>`, `python skills/everwrite/scripts/tells.py --wiki <wiki>`.
4. Commit, push, `wikiwright.py live m4bwav/everwrite <wiki>`.

Pages naming the version or commit: _Footer (1.0.0, 0673975, date), Home (last paragraph), Versions-and-Upgrading (table), What-The-Checker-Flags (commit 0673975), Getting-Started and FAQ (Claude Code 2.1.281, gh 2.100.0), Development (28 tests, 8 weak / 1583 words in the prose check).

## How the examples were verified

`2026-10-03-wiki-verify.py` copies `skills/`, README.md and AGENTS.md from a fresh GitHub clone (0673975) into a new temp folder per case, writes fixture files, and runs each command through Git Bash with stdin closed, printing `$ command`, output with stderr merged, and `echo $?`. Ran on Windows 11 with Python 3.14.6 and 3.9.25: identical apart from the version line and test timing. Self-test 28/28 on both.

By hand, not in the script: `claude plugin marketplace add https://github.com/m4bwav/everwrite.git` and `claude plugin install everwrite@everwrite` in an isolated `CLAUDE_CONFIG_DIR` (Claude Code 2.1.281): installed, version 1.0.0, enabled. `gh skill install m4bwav/everwrite everwrite --dir <scratch>` (gh 2.100.0): installed. Not tested: macOS and Linux, Copilot/Codex/Cursor loading the skill, `--agent/--scope` form of gh, uninstall and update commands, the CI YAML recipe, a real `git commit` through the hook.

## Facts verified while writing (not in the README)

- `claude plugin marketplace add m4bwav/everwrite` cloned over SSH on this machine and failed with "SSH host key is not in your known_hosts file"; the HTTPS URL worked.
- With a config folder 119 characters deep, the marketplace clone failed on Windows with "Filename too long" because of `ai-docs/decisions/2026-09-25-bundle-a-stdlib-checker-instead-of-asking-the-model-to-rerea.md` (74 characters); `core.longpaths=true` (via a scratch `GIT_CONFIG_GLOBAL`) fixed it.
- `gh skill install` rewrites the installed SKILL.md frontmatter, adding a `metadata` block (repo, path, ref, tree SHA) used by `gh skill update`.
- Directory scans print `docs\draft.md` on Windows.
- Usage and error messages go to stderr; exit 2 for bad input.
- `plugin.json` has said 1.0.0 since 2026-09-25 although the checker gained hidden-char, odd-space, repeated-heading, repeated-text, `--fix-hidden` and `--wiki` after it. No tags or releases.
- evals.json has 8 cases; the last run (T-20260925-4) covered 7; `action-2` has never run.

## Inaccuracies and gaps in the shipped docs

1. README: no mention of `--wiki`, `--fix-hidden` or `--json` in its usage block (only the file and `--list`). Gap, not an error.
2. README install: only the `m4bwav/everwrite` shorthand; it fails on machines without GitHub's SSH host key. Suggest also giving the HTTPS URL.
3. README: no `gh skill install` route.
4. plugin.json version 1.0.0 does not distinguish the post-1.0.0 checker; suggest 1.1.0 or 1.2.0 with a release/tag.
5. The ai-docs decision file name (74 characters) can break the plugin clone on Windows under deep paths; suggest a shorter name.
6. The README links the skill's changelog nowhere; the repo has no root CHANGELOG.

## Gotchas

- Quoted heredocs in Git Bash turned `\\n` into a newline inside the Python verify script; edit it with the editor tools.
- wikiwright `outputs` reads a yaml block after a line ending in a colon as output; end the lead-in with a period.
- wikiwright `snippets` needs a sh script held in a Python string to start on its own line (`"""\` then `#!/bin/sh`).

Related: see also the wiki itself, https://github.com/m4bwav/everwrite/wiki.
