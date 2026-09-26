# Patterns: examples and fixes

Before and after pairs for the patterns in [SKILL.md](../SKILL.md). Read this in edit mode and detect mode; a plain drafting task doesn't need it. The mechanical list (stock words, residue phrases, markup) lives in `scripts/tells.py` (`--list`), so it is not repeated here. Sources and the reasoning behind each entry: [RESEARCH.md](../RESEARCH.md).

<!-- tells: off -->
## Staging instead of stating

Not X but Y. The negative half names something nobody claimed so the positive half sounds bigger.
- Before: "Harbor isn't just a build tool, it's a new way to ship."
- After: "Harbor builds and deploys in one command."
- Split form. Before: "This doesn't mean every option is equal. It means no system ranks them." After: "No system ranks the options, though they still differ."
- Reversed form (common in Grok output): "prioritizing speed rather than purity". Keep "rather than" only when both halves carry information.

Staged setups and faux insight.
- Before: "Here's what most teams get wrong: the cache is the bottleneck."
- After: "The cache is the bottleneck."
- Colon reveal. Before: "The best part: it learns from each run." After: "It learns from each run."

Arguing with no one.
- Before: "A tempting approach would be to restart the service nightly, but that drops sessions. Tokens rotate in place."
- After: "Tokens rotate in place, so sessions survive."

Closers, fragments and kickers.
- Before: "Caching cuts repeat work.\n\nThat's the real win."
- After: "Caching cuts repeat work." (End there.)
- Before: "No setup. No config. Just results." After: "It runs with the defaults."
- Before: "Speed is the language of trust." After: "Users trust pages that load in under a second." (Only if the source says so.)

## Inflation and borrowed authority

Inflated significance.
- Before: "The institute was founded in 1989, marking a pivotal moment in the evolution of regional statistics."
- After: "The institute was founded in 1989."
- Stock section. Before: "Despite these challenges, the town continues to thrive." After: cut it, or state the real problem ("The town has recurring water shortages.").

Shallow -ing riders.
- Before: "The release adds file search, highlighting the team's commitment to productivity."
- After: "The release adds file search, so users find old drafts without leaving the editor." (Only if that is the actual effect.)

Borrowed authority.
- Before: "Experts believe the river plays a crucial role in the ecosystem."
- After: name who said it and what they said, or "Researchers study the river." Never invent the source.

Sales language.
- Before: "Nestled in the heart of the valley, the vibrant town boasts stunning natural beauty."
- After: "The town is in the valley."

## Rhythm by rule

Forced triads.
- Before: "Attendees can expect innovation, inspiration, and insights."
- After: "The talks cover the new API and the migration plan."

Avoiding is and has.
- Before: "Gallery 825 serves as the exhibition space and features four rooms."
- After: "Gallery 825 is the exhibition space. It has four rooms."

Synonym cycling.
- Before: "The agent reviews the draft. The assistant scores it. The tool suggests fixes."
- After: "The agent reviews the draft, scores it and suggests fixes."

Repeated openings.
- Before: "She noted the door. She noted the lock. She filed both away."
- After: "She noted the door and its lock, then filed both away."

Stacked qualifiers.
- Before: "It could potentially be argued that the policy might affect outcomes."
- After: "The policy may affect outcomes."

## Formatting by rule

Bold labels on every bullet.
- Before: "- **Speed:** Builds finish in 41 seconds.\n- **Caching:** The cache moved to Redis."
- After: "Builds finish in 41 seconds, and the cache moved to Redis."

Decorative headings: title case, emoji, arrows, a rule between every section, a top heading repeating the document title, a heading whose first sentence restates it. Use sentence case and let the title stand once.

## Leftovers from the chat and the draft

Chatbot residue wraps real content; remove the wrapper and keep the content.
- Before: "Great question! The revolution began in 1789. I hope this helps!"
- After: "The revolution began in 1789."

Knowledge-limit guesses.
- Before: "Details of her early life are not publicly available, suggesting she keeps a low profile. She likely grew up in a middle-class household."
- After: "Her early life isn't documented in the sources." (Or cut the section.)

Writing about the previous version (in docs, not changelogs).
- Before: "This function replaces the old approach of scanning every item."
- After: "This function looks items up in a hash map."

## Detect-mode report

One line per finding, strongest first:

```
12: not-X-but-Y: "isn't just a tool, it's a movement": say what it does
14: rider: ", highlighting its commitment": cut the tail
20: triad (weak, with 2 others in the paragraph): "fast, simple, and reliable": keep the two that are true
```

Then one sentence on how many strong and weak findings there were. No guess about who wrote it.
<!-- tells: on -->

Related: builds on [SKILL.md](../SKILL.md); see also [RESEARCH.md](../RESEARCH.md)
