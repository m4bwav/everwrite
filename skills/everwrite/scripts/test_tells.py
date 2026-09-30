#!/usr/bin/env python3
"""Self-test for tells.py. Standard library only: python test_tells.py"""

import io
import json
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import tells  # noqa: E402

FIXTURE = HERE.parent / "evals" / "fixtures" / "sloppy.md"


def cats(text, **kw):
    hits, _ = tells.check_text(text, **kw)
    return {(h["category"], h["severity"]) for h in hits}


def categories(text, **kw):
    return {c for c, _ in cats(text, **kw)}


class Rules(unittest.TestCase):
    def test_dashes(self):
        self.assertIn(("dash", "strong"), cats("It works \u2014 mostly."))
        self.assertIn(("dash", "strong"), cats("Pages 3\u20135 cover it."))
        self.assertIn(("dash", "strong"), cats("It works -- mostly."))
        self.assertNotIn("dash", categories("A well-known flag: --verbose is fine."))
        self.assertNotIn("dash", categories("It works \u2014 mostly.", allow_dashes=True))

    def test_residue(self):
        for s in ("Great question! It runs daily.", "I hope this helps.", "Let me know if you need more.",
                  "In conclusion, it works.", "It's important to note that it runs daily.", "Feel free to ask."):
            self.assertIn(("residue", "strong"), cats(s), s)

    def test_contrast(self):
        self.assertIn(("contrast", "strong"), cats("It's not just a tool but a way of life."))
        self.assertIn(("contrast", "strong"), cats("It's not a bug, it's a feature."))
        self.assertIn(("contrast", "strong"), cats("No setup. No config. Just results."))
        self.assertIn(("contrast", "strong"), cats("This doesn't mean every choice is equal. It means none is checked."))
        self.assertIn(("contrast", "strong"), cats("Harbor isn't just an update, it's a new way to ship."))
        self.assertIn(("contrast", "weak"), cats("The fix is not the parser. It is the cache."))
        self.assertNotIn("contrast", categories("The build does not cache results between runs."))

    def test_vocabulary_cluster(self):
        self.assertIn(("vocabulary", "weak"), cats("The parser is robust to bad input."))
        self.assertIn(("vocabulary", "strong"), cats("We delve into a robust pipeline."))

    def test_setup_inflation_rider(self):
        self.assertIn(("setup", "strong"), cats("Here's the thing: it breaks."))
        self.assertIn(("setup", "strong"), cats("The best part: it learns."))
        self.assertIn(("inflation", "strong"), cats("The launch marks a pivotal moment for the team."))
        self.assertIn(("rider", "strong"), cats("The cache moved to Redis, ensuring teams stay aligned."))

    def test_markdown_structure(self):
        self.assertIn(("bold-label", "strong"), cats("- **Speed:** builds are faster."))
        self.assertIn(("emoji", "strong"), cats("Shipped \U0001F680"))
        self.assertIn(("title-case", "weak"), cats("## Release Notes For Harbor"))
        self.assertNotIn("title-case", categories("## Release notes for Harbor"))
        self.assertIn(("divider", "weak"), cats("a\n\n---\n\nb\n\n---\n\nc"))

    def test_long_sentence_and_openings(self):
        long = " ".join(["word"] * 35) + "."
        hits, words = tells.check_text(long)
        self.assertEqual(words, 35)
        self.assertEqual([h["category"] for h in hits], ["long-sentence"])
        self.assertNotIn("long-sentence", categories(long, max_words=40))
        self.assertIn("repeated-opening", categories("She ran. She hid. She waited."))

    def test_markup_residue_sees_urls(self):
        self.assertIn(("markup", "strong"), cats("See [x](https://example.com/a?utm_source=chatgpt.com)."))
        self.assertIn(("markup", "strong"), cats("It rose 4% citeturn0search3 last year."))


class Skipping(unittest.TestCase):
    def test_code_frontmatter_comments_urls_off_regions(self):
        text = "\n".join([
            "---", "title: delve into a robust tapestry \u2014 x", "---",
            "Plain text here.",
            "```", "delve \u2014 robust -- tapestry", "```",
            "Run `delve --robust` now.",
            "<!-- I hope this helps -->",
            "Link: [docs](https://example.com/delve-robust-tapestry).",
            "<!-- tells: off -->", "In conclusion \u2014 delve into a robust tapestry.", "<!-- tells: on -->",
            "Done.",
        ])
        hits, _ = tells.check_text(text)
        self.assertEqual(hits, [])

    def test_line_numbers(self):
        hits, _ = tells.check_text("First line.\n\nSecond paragraph\ncontinues \u2014 here.")
        self.assertEqual([(h["line"], h["category"]) for h in hits], [(4, "dash")])

    def test_quoted_marker_does_not_switch_off(self):
        hits, _ = tells.check_text("Put `<!-- tells: off -->` on its own line.\n\nIt works \u2014 mostly.")
        self.assertEqual([h["category"] for h in hits], ["dash"])

    def test_only_newlines_split_lines(self):
        hits, _ = tells.check_text("a\u2028b\x0cc\n\nIt works \u2014 mostly.")
        self.assertEqual([(h["line"], h["category"]) for h in hits], [(3, "dash")])
        hits, _ = tells.check_text("First.\r\n\r\nIt works \u2014 mostly.\r\n")
        self.assertEqual([h["line"] for h in hits], [3])

    def test_setext_underline_is_not_a_divider(self):
        self.assertNotIn("divider", categories("Title\n---\n\nText.\n\nOther\n---\n\nMore."))

    def test_unclosed_fence_is_reported(self):
        self.assertIn(("input", "weak"), cats("Intro.\n\n```\ncode \u2014 here\n"))


class FalsePositives(unittest.TestCase):
    def test_conditional_negative_is_plain_prose(self):
        self.assertNotIn("contrast", categories("If the value is not set, it is treated as zero."))
        self.assertNotIn("contrast", categories("When it's not cached, it's fetched again."))

    def test_check_mark_is_not_emoji(self):
        self.assertNotIn("emoji", categories("| Linux | \u2713 |\n\nDone \u2714"))


class Hidden(unittest.TestCase):
    TAGS = "".join(chr(0xE0000 + ord(c)) for c in "hi")

    def test_covert_characters_are_strong(self):
        for s in ("Hello\u200bworld.", "soft\u00adhyphen", "a\u2060b", "left\u202eright", "x" + self.TAGS + "y",
                  "vs\U000E0100", "join\u200dme"):
            self.assertIn(("hidden-char", "strong"), cats(s), repr(s))

    def test_odd_spaces_are_weak(self):
        self.assertIn(("odd-space", "weak"), cats("10\u00a0km and 5\u202fkg."))
        self.assertNotIn("hidden-char", categories("10\u00a0km."))

    def test_plain_text_and_emoji_selector_are_clean(self):
        self.assertFalse({"hidden-char", "odd-space"} & categories("Plain words, plain spaces.\n\nDone."))
        self.assertNotIn("hidden-char", categories("Nice \u2764\ufe0f"))

    def test_seen_inside_code_and_named(self):
        hits, _ = tells.check_text("Text.\n\n```\nx = 1\u200b\u200b\n```\n")
        h = [h for h in hits if h["category"] == "hidden-char"]
        self.assertEqual(len(h), 1)
        self.assertEqual(h[0]["line"], 4)
        self.assertIn("U+200B ZERO WIDTH SPACE x2", h[0]["match"])

    def test_fix_hidden(self):
        fixed, n = tells.fix_hidden("a\u200bb\u00a0c" + self.TAGS + "\r\nd\u202fe")
        self.assertEqual(fixed, "ab c\r\nd e")
        self.assertEqual(n, 5)


class Speed(unittest.TestCase):
    def test_pathological_lines_stay_fast(self):
        import time
        for text in ("# a" + " " * 5000 + "b", "<!-- " * 20000, "](" * 30000, "`" * 20000, "a `b` " * 20000,
                     ". " + " " * 50000 + "x", "- **" + "a" * 50000, "​" * 50000, "\U000E0041" * 50000):
            start = time.perf_counter()
            tells.check_text(text)
            self.assertLess(time.perf_counter() - start, 2.0, text[:20])


class Cli(unittest.TestCase):
    def run_cli(self, *args, stdin=None):
        return subprocess.run([sys.executable, str(HERE / "tells.py"), *args], input=stdin,
                              capture_output=True, text=True, encoding="utf-8")

    def test_fixture_fails_with_many_strong(self):
        r = self.run_cli(str(FIXTURE), "--json")
        self.assertEqual(r.returncode, 1)
        data = json.loads(r.stdout)
        found = {h["category"] for h in data["hits"]}
        for c in ("dash", "residue", "contrast", "inflation", "rider", "vocabulary", "bold-label", "emoji", "title-case", "long-sentence"):
            self.assertIn(c, found, c)
        self.assertGreaterEqual(data["summary"]["strong"], 15)

    def test_clean_stdin_passes(self):
        r = self.run_cli("-", stdin="Harbor 2.4 builds in 41 seconds, down from 95.\n")
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertIn("tells: 0 strong", r.stdout)

    def test_missing_file_and_list(self):
        self.assertEqual(self.run_cli("no-such-file.md").returncode, 2)
        r = self.run_cli("--list")
        self.assertEqual(r.returncode, 0)
        self.assertIn("Stock words", r.stdout)

    def test_fix_hidden_rewrites_file(self):
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "note.md"
            p.write_bytes("Harbor 2.4 builds in 41 seconds.​\r\n".encode("utf-8"))
            self.assertEqual(self.run_cli(str(p)).returncode, 1)
            r = self.run_cli(str(p), "--fix-hidden")
            self.assertEqual(r.returncode, 0, r.stdout)
            self.assertIn("fixed", r.stdout)
            self.assertEqual(p.read_bytes(), b"Harbor 2.4 builds in 41 seconds.\r\n")
            self.assertEqual(self.run_cli("-", "--fix-hidden", stdin="x").returncode, 2)

    def test_repeated_heading_and_text(self):
        # A GitHub wiki prints the file name as the page title; the page's own `# Getting started` repeated it
        # on get-title-at-url's wiki (2026-09-30, the maintainer's correction).
        page = "# Getting started\n\n## Install\n\nRun the installer.\n"
        self.assertIn(("repeated-heading", "strong"), cats(page, page_title="Getting Started"))
        self.assertNotIn("repeated-heading", categories(page))
        self.assertNotIn("repeated-heading", categories("Intro first.\n\n# Getting started\n", page_title="Getting Started"))
        self.assertNotIn("repeated-heading", categories("# get-title-at-url\n\nText.\n", page_title="Home"))
        self.assertIn(("repeated-heading", "strong"), cats("## Install\n\n### Install\n\nRun it.\n"))
        self.assertNotIn("repeated-heading", categories("## Install\n\nRun it.\n\n## Install\n\nAgain.\n"))
        self.assertIn(("repeated-text", "strong"), cats("Harbor builds in 41 seconds.\n\nHarbor builds in 41 seconds.\n"))
        self.assertNotIn("repeated-text", categories("Harbor builds fast.\n\nHarbor builds in 41 seconds.\n"))
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "Getting-Started.md"
            p.write_text(page, encoding="utf-8")
            self.assertEqual(self.run_cli(str(p)).returncode, 0)
            result = self.run_cli(str(p), "--wiki")
            self.assertEqual(result.returncode, 1)
            self.assertIn("repeated-heading", result.stdout)

    def test_main_in_process(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = tells.main(["--list"])
        self.assertEqual(code, 0)


if __name__ == "__main__":
    unittest.main(verbosity=1)
