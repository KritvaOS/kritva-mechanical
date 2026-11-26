"""Tests for the local commit-msg hook and the preflight targets (same format rules as CI).

Run: python3 -m unittest discover -s tests
The hook only calls the vendored checker, scripts/security/check_commit_format.py, with the task IDs
from planning/TASKS.md. These tests fail if the hook starts to let a bad message through.
"""
import os
import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HOOK = ROOT / ".githooks" / "commit-msg"
TASK = sorted(set(re.findall(r"ROB-MECH-[0-9]{3}", (ROOT / "planning" / "TASKS.md").read_text(encoding="utf-8"))))[0]
GOOD = f"docs(feasibility): fix a filename\n\nTask: {TASK}\n"


def hook(message, name="msg"):
    with tempfile.TemporaryDirectory() as d:
        f = Path(d) / name
        f.write_text(message, encoding="utf-8")
        return subprocess.run(["sh", str(HOOK), str(f)], capture_output=True, text=True)


class CommitMsgHook(unittest.TestCase):
    def test_good_message_passes(self):
        self.assertEqual(hook(GOOD).returncode, 0)
        self.assertEqual(hook(f"docs(feasibility): fix\n\nTask: {TASK}\nCo-Authored-By: Claude <noreply@anthropic.com>\n").returncode, 0)
        self.assertEqual(hook("docs(feasibility): fix\n\nTasks: None (record correction)\n").returncode, 0)

    def test_bad_messages_fail_with_exit_1(self):
        bad = {
            "no scope colon": f"fix filenames\n\nTask: {TASK}\n",
            "unknown type": f"update(feasibility): fix\n\nTask: {TASK}\n",
            "no footer": "docs(feasibility): fix a filename\n",
            "two footers": f"docs(feasibility): fix\n\nTask: {TASK}\nTask: {TASK}\n",
            "unknown task id": "docs(feasibility): fix\n\nTask: ROB-MECH-999\n",
            "none on feat": "feat(feasibility): add\n\nTasks: None (no task)\n",
            "session trailer": GOOD + "Claude-Session: https://claude.ai/code/session_x\n",
            "session link": GOOD + "See https://claude.ai/code/session_x\n",
            "summary over 90 chars": "docs(feasibility): " + "x" * 91 + f"\n\nTask: {TASK}\n",
        }
        for name, msg in bad.items():
            r = hook(msg)
            self.assertEqual(r.returncode, 1, name)
            self.assertIn("Commit not created", r.stderr, name)

    def test_git_comment_and_verbose_diff_lines_are_ignored(self):
        msg = GOOD + "# Please enter the commit message\n# ------------------------ >8 ------------------------\n Task: ROB-MECH-999\n+Task: x\n"
        self.assertEqual(hook(msg).returncode, 0)

    def test_merge_and_fixup_commits_are_skipped(self):
        self.assertEqual(hook("Merge pull request #1 from x/y\n").returncode, 0)
        self.assertEqual(hook("fixup! docs(feasibility): fix\n").returncode, 0)

    def test_missing_argument_is_an_error_not_a_pass(self):
        r = subprocess.run(["sh", str(HOOK)], capture_output=True, text=True)
        self.assertEqual(r.returncode, 2)


@unittest.skipUnless(shutil.which("git"), "git not installed")
class RealGit(unittest.TestCase):
    """A real git repository with core.hooksPath set: a bad message must stop the commit."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self.tmp.name)
        for rel in (".githooks", "scripts/security", "planning/TASKS.md", "Makefile"):
            src = ROOT / rel
            dst = self.repo / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            if src.is_dir():
                shutil.copytree(src, dst, ignore=shutil.ignore_patterns("__pycache__"))
            else:
                shutil.copy2(src, dst)
        for h in (self.repo / ".githooks").iterdir():
            h.chmod(0o755)
        self.env = dict(os.environ, GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@example.com",
                        GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@example.com", GIT_CONFIG_GLOBAL="/dev/null")
        self.git("init", "-q", "-b", "main")
        self.git("config", "core.hooksPath", ".githooks")
        (self.repo / "a.txt").write_text("a\n")
        self.git("add", "a.txt")

    def tearDown(self):
        self.tmp.cleanup()

    def git(self, *args):
        return subprocess.run(["git", *args], cwd=self.repo, env=self.env, capture_output=True, text=True)

    def test_bad_message_blocks_the_commit(self):
        r = self.git("commit", "-q", "-m", "fix stuff")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("Commit not created", r.stderr)
        self.assertNotEqual(self.git("rev-parse", "--verify", "HEAD").returncode, 0)

    def test_good_message_commits(self):
        r = self.git("commit", "-q", "-m", GOOD.rstrip("\n"))
        self.assertEqual(r.returncode, 0, r.stderr)

    def test_no_verify_skips_the_hook(self):
        self.assertEqual(self.git("commit", "-q", "--no-verify", "-m", "fix stuff").returncode, 0)

    @unittest.skipUnless(shutil.which("make"), "make not installed")
    def test_preflight_commits_flags_a_bad_commit_in_the_range(self):
        self.git("commit", "-q", "--no-verify", "-m", "base")
        base = self.git("rev-parse", "HEAD").stdout.strip()
        (self.repo / "b.txt").write_text("b\n")
        self.git("add", "b.txt")
        self.git("commit", "-q", "--no-verify", "-m", "fix stuff")
        r = subprocess.run(["make", "--no-print-directory", "preflight-commits", f"PREFLIGHT_BASE={base}"],
                           cwd=self.repo, capture_output=True, text=True)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("header must be", r.stderr)
        (self.repo / "c.txt").write_text("c\n")
        self.git("add", "c.txt")
        self.git("commit", "-q", "--amend", "--no-verify", "-m", GOOD.rstrip("\n"))
        r = subprocess.run(["make", "--no-print-directory", "preflight-commits", f"PREFLIGHT_BASE={base}"],
                           cwd=self.repo, capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)

    @unittest.skipUnless(shutil.which("make"), "make not installed")
    def test_preflight_commits_without_base_branch_is_an_error(self):
        r = subprocess.run(["make", "--no-print-directory", "preflight-commits", "PREFLIGHT_BASE=origin/nonexistent"],
                           cwd=self.repo, capture_output=True, text=True)
        self.assertNotEqual(r.returncode, 0)


if __name__ == "__main__":
    unittest.main()
