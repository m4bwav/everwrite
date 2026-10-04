# everwrite

A skill for AI agents that makes their prose read like a person wrote it. It strips the patterns that mark text as machine-written and keeps sentences short enough to read in one pass. A small script checks the result, so the model doesn't have to reread its own draft.

It works in Claude Code, GitHub Copilot (VS Code and CLI), Codex, Cursor and any other agent that reads `SKILL.md` skills.

## What it does

- Writes and edits reports, docs, READMEs, emails and release notes without the usual tells. Those include dashes everywhere, stock words, "not X but Y" contrasts, staged setups, inflated significance, bold labels on every bullet and chatbot sign-offs.
- Never invents facts while rewriting. A vague true sentence beats a specific made-up one.
- Detect mode: asked "is this AI slop?", it lists each pattern with the line, a quote and a short fix, and doesn't guess who wrote the text.
- Ships `scripts/tells.py`, a checker that needs only Python 3.9 or later. It reads markdown or plain text, skips code, frontmatter, comments and URLs, prints one line per hit and exits 1 while a strong tell remains. The agent reads a few lines of output instead of rereading a long document, which saves tokens and leaves evidence that the check ran.

```
python skills/everwrite/scripts/tells.py draft.md
python skills/everwrite/scripts/tells.py --list      # every rule and the stock-word list
```

## Install

Claude Code, as a plugin:

```
/plugin marketplace add m4bwav/everwrite
/plugin install everwrite@everwrite
```

Any agent that reads personal skills: clone this repository and link or copy `skills/everwrite` into the agent's skills folder (`~/.claude/skills/everwrite`, `~/.agents/skills/everwrite` or `~/.copilot/skills/everwrite`). Hosted skill stores: zip the `skills/everwrite` folder and upload it.

## Evergreen

AI tells drift. Models get trained away from old habits and pick up new ones, so a fixed pattern list goes stale. This skill follows the [Evergreen Protocol](https://github.com/m4bwav/evergreen-protocol): it re-researches its sources on a schedule (`evergreen.json`), logs each finding (`RESEARCH.md`), each change with its reason (`CHANGELOG.md`) and each lesson (`LEARNINGS.md`), and carries the test cases that prove it triggers and acts (`TESTS.md`, `evals/evals.json`). Without the evergreen plugin installed the skill still works; `MAINTENANCE.md` says how to refresh it by hand.

## Layout

- [skills/everwrite/SKILL.md](skills/everwrite/SKILL.md): the skill.
- [skills/everwrite/references/patterns.md](skills/everwrite/references/patterns.md): before and after examples, read in edit and detect mode.
- [skills/everwrite/scripts/tells.py](skills/everwrite/scripts/tells.py): the checker; `test_tells.py` is its self-test.
- [skills/everwrite/RESEARCH.md](skills/everwrite/RESEARCH.md): what the rules rest on and when they were last checked.
- [ai-docs/INDEX.md](ai-docs/INDEX.md): notes left by past work sessions on this repository.

## Privacy

everwrite collects nothing. The skill is instructions for the agent, and its checker (`skills/everwrite/scripts/tells.py`) is a standard-library Python script that reads the files you point it at on your own machine. Neither one sends data anywhere, calls a server or keeps a copy of your text. Whatever your AI app does with the conversation is covered by that app's own privacy policy.

## Credits

The patterns come from Wikipedia's [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (WikiProject AI Cleanup) and from the ideas in [blader/humanizer](https://github.com/blader/humanizer), [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop), [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) and [gregorymm/humanize-text](https://github.com/gregorymm/humanize-text), all MIT licensed. The wording, the density rules and the checker are this project's own.

## License

MIT. See [LICENSE](LICENSE).
