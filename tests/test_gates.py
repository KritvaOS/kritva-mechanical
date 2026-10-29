"""Tests for the Makefile gate targets (ROB-MECH-004, AC-004-01 to AC-004-03).

Run: python3 -m unittest discover -s tests
Every standard gate is NOT_IMPLEMENTED today. These tests fail if a gate starts
to pass without this file being updated by the task that implements it.
"""
import re
import shutil
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GATES = ["check", "lint", "test-unit", "test-integration", "test-regression", "test", "docs-check", "acceptance"]


def run(cmd):
    return subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)


class Gates(unittest.TestCase):
    def test_makefile_defines_all_standard_targets(self):  # AC-004-01
        text = (ROOT / "Makefile").read_text(encoding="utf-8")
        targets = set(re.findall(r"^([a-z][a-z-]*):", text, re.MULTILINE))
        for g in GATES:
            self.assertIn(g, targets)

    def test_gate_script_exits_3_for_every_gate(self):  # AC-004-02
        for g in GATES:
            r = run(["sh", "scripts/gate.sh", g])
            self.assertEqual(r.returncode, 3, g)
            self.assertIn("NOT_IMPLEMENTED", r.stderr, g)

    def test_gate_script_rejects_unknown_target(self):
        self.assertEqual(run(["sh", "scripts/gate.sh", "nonsense"]).returncode, 2)
        self.assertEqual(run(["sh", "scripts/gate.sh"]).returncode, 2)

    @unittest.skipUnless(shutil.which("make"), "make not installed")
    def test_make_gates_fail_and_say_not_implemented(self):  # AC-004-02
        for g in GATES:
            r = run(["make", "--no-print-directory", g])
            self.assertNotEqual(r.returncode, 0, g)
            self.assertIn("NOT_IMPLEMENTED", r.stderr, g)

    def test_readme_lists_every_gate(self):  # AC-004-03
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        for g in GATES:
            self.assertIn(f"`make {g}`", readme, g)


if __name__ == "__main__":
    unittest.main()
