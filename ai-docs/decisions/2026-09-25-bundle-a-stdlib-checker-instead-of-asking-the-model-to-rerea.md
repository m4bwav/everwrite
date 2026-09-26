---
title: Bundle a stdlib checker instead of asking the model to reread
kind: decision
status: active
date: 2026-09-25
verified: 2026-09-25
stale_after: 2027-03-24
tags: [checker, tokens, evidence, naming]
summary: why tells.py exists, what was rejected, why the skill was renamed and made public
---

# Bundle a stdlib checker instead of asking the model to reread

## Context

The original write-human skill asked the model to reread its draft and grep mentally for dashes, banned words and long sentences, then score it on five dimensions out of 50. The owner asked for token savings and for the skill to follow the evergreen protocol, whose testing rule wants proof outside the transcript.

## Decision

The skill ships a stdlib checker (`skills/everwrite/scripts/tells.py`) and tells the agent to run it on file output instead of rereading the draft for mechanical tells. The 50-point score is gone; two audit questions cover what a script can't see.

## Reasons

- Token cost: a reread of a long document costs the whole document again; the checker's output is a few lines.
- Evidence: the checker's exit code and summary line prove the check ran, for the action and outcome evals and for CI on the repo's own prose.
- Gap: none of the leading prose humanizer skills (blader/humanizer, stop-slop, no-ai-slop) ships one as of 2026-09-25 (skill RESEARCH.md R-20260925-4).

## Rejected

- Vale with a custom style: an extra binary on every machine and agent product; stdlib Python runs everywhere the skill does. Kept as an open question.
- Checking triads by regex: too noisy, lists of three are often real. Left to the Step 4 audit.
- Keeping the five-dimension score: reasoning tokens on every use with no artifact to check.

## Also decided

- Renamed write-human to everwrite to match the repository and the ever- family of skills. The old hosted copy should be replaced by this one so two skills don't compete for the same prompts.
- Public repository: the content names no people, hosts or private projects.

Related: see also [skills/everwrite/RESEARCH.md](../../skills/everwrite/RESEARCH.md), [skills/everwrite/CHANGELOG.md](../../skills/everwrite/CHANGELOG.md)
