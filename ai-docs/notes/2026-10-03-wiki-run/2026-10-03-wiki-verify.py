"""Runs every example on the everwrite wiki against a fresh clone of github.com/m4bwav/everwrite.

Usage: python wiki-verify.py CLONE_DIR [PYTHON]
CLONE_DIR is a fresh `git clone https://github.com/m4bwav/everwrite.git`, never the working copy.
PYTHON (optional) is the interpreter that stands in for `python` in every command (to run on 3.9).
Each case copies the clone's skills/ folder into a new scratch folder, writes the case's files there,
then runs each command line through bash with stdin closed, printing `$ command`, its output with
stderr merged, and the exit code when the case asks for `echo $?`.
"""
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

CLONE = Path(sys.argv[1]).resolve()
PY = sys.argv[2] if len(sys.argv) > 2 else None
BASH = shutil.which("bash") or r"C:\Program Files\Git\bin\bash.exe"

DRAFT = """# Release notes

We're excited to announce version 2.0, which marks a pivotal shift for the project.
It's not just faster, it's smarter. Let me know if you have questions!
"""

FIXED = """# Release notes

Version 2.0 parses large files about twice as fast as 1.4.
Questions go in the issue tracker.
"""

WIKI_PAGE = """# Getting started

Install the package with the command below.
"""

HIDDEN = "Plain\u200b text with a zero-width space and a no-break\u00a0space.\n"

DASHED = "The fix was small \u2014 one line in the parser.\n"

LONG = ("This sentence keeps going with one clause after another because the writer never stopped "
        "to put a full stop anywhere in the middle of it at all, so the reader has to hold every part "
        "in mind.\n")

QUOTED = """Avoid openers like these:

<!-- tells: off -->
- I hope this helps!
- Let's dive in.
<!-- tells: on -->

The rest of the page is checked.
"""

STDIN_LINE = "Great question! Here's a quick overview."

HOOK = """\
#!/bin/sh
# .git/hooks/pre-commit: refuse a commit while a staged markdown file has a strong tell
files=$(git diff --cached --name-only --diff-filter=ACM -- '*.md')
[ -z "$files" ] && exit 0
python skills/everwrite/scripts/tells.py $files || {
  echo "everwrite: fix the strong tells above, then commit again"
  exit 1
}
"""

CASES = [
    ("home-first-check", {"draft.md": DRAFT}, """
python skills/everwrite/scripts/tells.py draft.md
echo $?
"""),
    ("home-after-fix", {"draft.md": FIXED}, """
python skills/everwrite/scripts/tells.py draft.md
echo $?
"""),
    ("cmd-usage-no-args", {}, """
python skills/everwrite/scripts/tells.py
echo $?
"""),
    ("cmd-missing-file", {}, """
python skills/everwrite/scripts/tells.py nothere.md
echo $?
"""),
    ("cmd-streams", {}, """
python skills/everwrite/scripts/tells.py nothere.md 2>/dev/null
echo $?
"""),
    ("cmd-stdin", {}, """
echo "Great question! Here's a quick overview." | python skills/everwrite/scripts/tells.py -
"""),
    ("cmd-json", {"draft.md": DRAFT}, """
python skills/everwrite/scripts/tells.py --json draft.md
"""),
    ("cmd-wiki", {"Getting-Started.md": WIKI_PAGE}, """
python skills/everwrite/scripts/tells.py Getting-Started.md
python skills/everwrite/scripts/tells.py --wiki Getting-Started.md
"""),
    ("cmd-fix-hidden", {"note.md": HIDDEN}, """
python skills/everwrite/scripts/tells.py note.md
python skills/everwrite/scripts/tells.py --fix-hidden note.md
"""),
    ("cmd-allow-dashes", {"note.md": DASHED}, """
python skills/everwrite/scripts/tells.py note.md
python skills/everwrite/scripts/tells.py --allow-dashes note.md
"""),
    ("cmd-max-words", {"note.md": LONG}, """
python skills/everwrite/scripts/tells.py note.md
python skills/everwrite/scripts/tells.py --max-words 40 note.md
"""),
    ("cmd-tells-off", {"style.md": QUOTED}, """
python skills/everwrite/scripts/tells.py style.md
"""),
    ("cmd-directory", {"docs/draft.md": DRAFT, "docs/notes.txt": FIXED, "docs/data.json": "{}\n"}, """
python skills/everwrite/scripts/tells.py docs
"""),
    ("cmd-list", {}, """
python skills/everwrite/scripts/tells.py --list | head -3
"""),
    ("recipe-json-filter", {"draft.md": DRAFT}, """
python skills/everwrite/scripts/tells.py --json draft.md | python -c "import json,sys; print(json.load(sys.stdin)['summary'])"
"""),
    ("recipe-hook", {"hook.sh": HOOK, "draft.md": DRAFT}, """
git init -q . && git add draft.md
sh hook.sh
echo $?
"""),
    ("dev-self-test", {}, """
python skills/everwrite/scripts/test_tells.py
"""),
    ("dev-prose-check", {}, """
python skills/everwrite/scripts/tells.py README.md AGENTS.md skills/everwrite/SKILL.md skills/everwrite/references
echo $?
"""),
]


def run_case(label, files, commands):
    print("== %s ==" % label)
    work = Path(tempfile.mkdtemp(prefix="ew-"))
    try:
        shutil.copytree(CLONE / "skills", work / "skills")
        for top in ("README.md", "AGENTS.md"):
            shutil.copy(CLONE / top, work / top)
        for name, text in files.items():
            path = work / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(text.encode("utf-8"))
        env = dict(os.environ, PYTHONUTF8="1")
        if PY:
            env["PATH"] = str(Path(PY).parent) + os.pathsep + env["PATH"]
        rc = 0
        for line in [c for c in commands.strip().splitlines() if c.strip()]:
            print("$ " + line)
            if line == "echo $?":
                print(rc)
                continue
            p = subprocess.run([BASH, "-c", "{ " + line + "; } 2>&1"], cwd=work, env=env, stdin=subprocess.DEVNULL,
                               stdout=subprocess.PIPE)
            sys.stdout.write(p.stdout.decode("utf-8", "replace").replace("\r\n", "\n"))
            rc = p.returncode
    finally:
        shutil.rmtree(work, ignore_errors=True)


def main():
    sys.stdout.reconfigure(encoding="utf-8", newline="\n")
    v = subprocess.run([PY or "python", "--version"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print("== installed ==")
    print("clone: %s" % subprocess.run(["git", "-C", str(CLONE), "log", "--format=%h %ad", "--date=short", "-1"],
                                         stdout=subprocess.PIPE).stdout.decode().strip())
    print(v.stdout.decode().strip())
    for case in CASES:
        run_case(*case)


main()
