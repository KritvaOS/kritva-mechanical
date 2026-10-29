"""Tests for the vendored commit-format checker (ROB-MECH-003, AC-003-03).

Run: python3 -m unittest discover -s tests
These use obviously fake messages. The checker itself is a vendored copy of the
kritva-program script (see scripts/security/PROVENANCE.md).
"""
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts" / "security"))

import check_commit_format as ccf  # noqa: E402

REGISTRY = {"ROB-MECH-001", "ROB-MECH-002", "ROB-MECH-003"}


class CommitFormat(unittest.TestCase):
    def test_valid_with_task_footer(self):
        self.assertEqual(ccf.problems("docs(mechanical): add governance files\n\nTask: ROB-MECH-002\n", REGISTRY), [])

    def test_valid_multiple_tasks(self):
        self.assertEqual(ccf.problems("ci(mechanical): add workflows\n\nTasks: ROB-MECH-002, ROB-MECH-003\n", REGISTRY), [])

    def test_missing_footer_rejected(self):
        self.assertTrue(ccf.problems("docs(mechanical): add governance files\n", REGISTRY))

    def test_duplicate_footer_rejected(self):
        msg = "docs(mechanical): x\n\nTask: ROB-MECH-001\nTask: ROB-MECH-002\n"
        self.assertTrue(any("more than one" in p for p in ccf.problems(msg, REGISTRY)))

    def test_none_footer_only_on_docs_or_chore(self):
        self.assertEqual(ccf.problems("docs(mechanical): fix typo\n\nTasks: None (typo)\n", REGISTRY), [])
        self.assertTrue(ccf.problems("feat(mechanical): add frame\n\nTasks: None (nothing)\n", REGISTRY))

    def test_unknown_task_rejected(self):
        self.assertTrue(any("unknown task" in p for p in ccf.problems("docs(mechanical): x\n\nTask: ROB-MECH-999\n", REGISTRY)))

    def test_session_trailer_rejected(self):
        msg = "docs(mechanical): x\n\nTask: ROB-MECH-001\nClaude-Session: https://example.invalid/session\n"
        self.assertTrue(any("session" in p.lower() for p in ccf.problems(msg, REGISTRY)))

    def test_co_authored_by_allowed(self):
        msg = "docs(mechanical): x\n\nTask: ROB-MECH-001\nCo-Authored-By: Someone <someone@example.invalid>\n"
        self.assertEqual(ccf.problems(msg, REGISTRY), [])

    def test_long_summary_rejected(self):
        self.assertTrue(ccf.problems("docs(mechanical): " + "x" * 95 + "\n\nTask: ROB-MECH-001\n", REGISTRY))

    def test_merge_commit_skipped(self):
        self.assertEqual(ccf.problems("Merge pull request #3 from KritvaOS/docs/x\n", REGISTRY), [])


class WorkflowFilesPresent(unittest.TestCase):
    def test_no_gitleaks_allowlist(self):
        text = (ROOT / ".gitleaks.toml").read_text(encoding="utf-8")
        code = "\n".join(l for l in text.splitlines() if not l.lstrip().startswith("#"))
        self.assertIsNone(re.search(r"allowlist", code, re.IGNORECASE))


if __name__ == "__main__":
    unittest.main()
