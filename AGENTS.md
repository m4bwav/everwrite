# Agent rules for everwrite

Read [README.md](README.md) first. The skill is [skills/everwrite/SKILL.md](skills/everwrite/SKILL.md); its evidence, changes and lessons are the evergreen companions beside it (RESEARCH, CHANGELOG, LEARNINGS, TESTS, `evergreen.json`).

- Evergreen unit in pointer mode: before editing the skill read `skills/everwrite/evergreen.json`; if `next_due` has passed or `contradiction` is set, say so and refresh after the task. Every edit to SKILL.md or the checker gets a CHANGELOG entry with its reason; re-run `evals/evals.json` (evergreen-test) after SKILL.md changes.
- `scripts/tells.py` stays stdlib-only, Python 3.9 compatible and cross-platform (UTF-8 in and out). Every rule change gets a case in `scripts/test_tells.py`; probe a new strong rule on a few human-written docs before committing (LEARNINGS L-003).
- The repo's own prose must pass its checker: `python skills/everwrite/scripts/tells.py README.md AGENTS.md skills/everwrite/SKILL.md skills/everwrite/references` exits 0, and `python skills/everwrite/scripts/test_tells.py` passes. Quoted examples of tells go between lines holding only `<!-- tells: off -->` and `<!-- tells: on -->`.
- Public repository: no personal names beyond the author credit, no local paths, hostnames, credentials or private project names. Test environments are named `owner-pc`.
- No AI attribution in commits or files.

## everlast (session knowledge, load on demand)

- `ai-docs/INDEX.md` lists what past sessions learned here (solutions with verified commands, decisions with reasons, plans). At the start of a task, scan it and open only the entries whose title or tags match; read `ai-docs/HANDOFF.md` when continuing unfinished work (everlast-resume skill).
- Before finishing a task that hit a dead end, verified a non-obvious command, made a design choice, or taught you something about the user, record it (everlast-capture skill, or `everlast.py note` / `handoff`); rewrite `HANDOFF.md` when work is left unfinished. Say "nothing to record" when that is true.
- Anything naming a person, an internal host or name, a credential, or an opinion about people goes to the private sidecar (`--private`), never here. Lessons about the user or this machine go to the user tier (`--user`).
- Link documents together with relative markdown links: every markdown folder has an index that links its files, every entry links its index and the entries it builds on (a `Related:` line). No wikilinks in the repo.
