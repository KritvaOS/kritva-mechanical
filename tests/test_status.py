"""Tests for the status generator and checker (ROB-MECH-005, AC-005-01 to AC-005-04).

Run: python3 -m unittest discover -s tests
All task data below is fake. Git tests build throwaway repositories in a temp folder.
"""
import copy
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts" / "status"))

import gen_status as gs  # noqa: E402

SHA = "a" * 40
STAMP = "2026-10-29T00:00:00Z"


def row(tid, deps="none", execution="NOT_STARTED", git="NOT_COMMITTED", title="Fake task"):
    return f"| ROB-MECH-{tid} | {title} | {deps} | UNASSIGNED | {execution} | NOT_REVIEWED | NOT_RUN | {git} | note |"


def register(*rows):
    head = "| ID | Task | Depends on | Owner | Execution | Review | Acceptance | Git | Notes |\n|---|---|---|---|---|---|---|---|---|"
    return "# T\n\n## 3. Task register\n\n" + head + "\n" + "\n".join(rows) + "\n\n## 4. Task definitions\n\n| ROB-MECH-999 | ignored |\n"


def report_for(text):
    return gs.build_report(gs.parse_register(text), SHA, STAMP)


class Register(unittest.TestCase):
    def test_real_register_parses_and_validates(self):  # AC-005-03
        text = (ROOT / "planning" / "TASKS.md").read_text(encoding="utf-8")
        tasks = gs.parse_register(text)
        ids = [t["task_id"] for t in tasks]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(ids[0], "ROB-MECH-001")
        self.assertEqual(gs.validate(gs.build_report(tasks, SHA, STAMP), gs.load_schema()), [])

    def test_rows_outside_section_3_are_ignored(self):
        ids = [t["task_id"] for t in gs.parse_register(register(row("001")))]
        self.assertEqual(ids, ["ROB-MECH-001"])

    def test_dependency_ranges(self):
        t = gs.parse_register(register(row("001"), row("002"), row("003"), row("004", deps="001 to 003")))
        self.assertEqual(t[3]["deps"], ["ROB-MECH-001", "ROB-MECH-002", "ROB-MECH-003"])

    def test_bad_registers_fail_closed(self):
        cases = {
            "duplicate": register(row("001"), row("001")),
            "unknown dependency": register(row("001", deps="009")),
            "self dependency": register(row("001", deps="001")),
            "cycle": register(row("001", deps="002"), row("002", deps="001")),
            "bad execution value": register(row("001", execution="DONE")),
            "bad git value": register(row("001", git="PUSHED")),
            "cancelled has no schema value": register(row("001", execution="CANCELLED")),
            "unreadable dependency": register(row("001", deps="see notes")),
            "backwards range": register(row("001"), row("002", deps="003 to 001")),
            "wrong column count": register("| ROB-MECH-001 | only | three |"),
            "no section": "# nothing\n",
            "empty section": register(),
        }
        for name, text in cases.items():
            with self.assertRaises(gs.StatusError, msg=name):
                gs.parse_register(text)


class Mapping(unittest.TestCase):
    def test_execution_and_readiness(self):
        text = register(
            row("001", execution="IMPLEMENTED", git="SYNCED"),
            row("002", deps="001"),                       # dependency implemented -> IMPLEMENTABLE
            row("003", deps="002"),                       # dependency not started -> PLANNABLE
            row("004", deps="001", execution="BLOCKED"),  # BLOCKED -> HARDWARE-BLOCKED
            row("005", execution="IN_PROGRESS"),
            row("006", execution="COMPLETE"),
        )
        t = {x["task_id"]: x for x in report_for(text)["tasks"]}
        self.assertEqual((t["ROB-MECH-001"]["execution"], t["ROB-MECH-001"]["git_sync"]), ("IN_PROGRESS", "SYNCED"))
        self.assertEqual(t["ROB-MECH-002"]["readiness"], "IMPLEMENTABLE")
        self.assertEqual(t["ROB-MECH-003"]["readiness"], "PLANNABLE")
        self.assertEqual(t["ROB-MECH-004"]["execution"], "BLOCKED")
        self.assertEqual(t["ROB-MECH-004"]["readiness"], "HARDWARE-BLOCKED")
        self.assertEqual(t["ROB-MECH-005"]["execution"], "IN_PROGRESS")
        self.assertEqual(t["ROB-MECH-006"]["execution"], "COMPLETE")

    def test_implemented_is_never_reported_complete(self):
        t = report_for(register(row("001", execution="IMPLEMENTED")))["tasks"][0]
        self.assertNotEqual(t["execution"], "COMPLETE")

    def test_report_has_no_credit_or_acceptance_fields(self):
        r = report_for(register(row("001")))
        self.assertEqual(set(r), {"schema_version", "workstream_id", "repo", "source", "tasks", "updated_at"})
        self.assertEqual(set(r["tasks"][0]), {"task_id", "execution", "git_sync", "readiness", "evidence"})
        self.assertEqual(r["tasks"][0]["evidence"], [])

    def test_output_is_deterministic(self):  # AC-005-04
        text = register(row("002"), row("001"))
        self.assertEqual(gs.render(report_for(text)), gs.render(report_for(text)))
        self.assertEqual([t["task_id"] for t in report_for(text)["tasks"]], ["ROB-MECH-001", "ROB-MECH-002"])


class Validator(unittest.TestCase):
    def setUp(self):
        self.schema = gs.load_schema()
        self.good = report_for(register(row("001")))

    def bad(self, mutate):
        r = copy.deepcopy(self.good)
        mutate(r)
        return gs.validate(r, self.schema)

    def test_good_report_passes(self):  # AC-005-01
        self.assertEqual(gs.validate(self.good, self.schema), [])

    def test_rejections(self):
        self.assertTrue(self.bad(lambda r: r.update(extra=1)))
        self.assertTrue(self.bad(lambda r: r.pop("updated_at")))
        self.assertTrue(self.bad(lambda r: r.update(schema_version="1.0")))
        self.assertTrue(self.bad(lambda r: r["source"].update(commit="abc")))
        self.assertTrue(self.bad(lambda r: r["source"].update(commit="A" * 40)))
        self.assertTrue(self.bad(lambda r: r["tasks"][0].update(execution="IMPLEMENTED")))
        self.assertTrue(self.bad(lambda r: r["tasks"][0].update(readiness="READY")))
        self.assertTrue(self.bad(lambda r: r["tasks"][0].update(acceptance="PASS")))
        self.assertTrue(self.bad(lambda r: r["tasks"][0].pop("evidence")))
        self.assertTrue(self.bad(lambda r: r.update(workstream_id="rob-mech")))
        self.assertTrue(self.bad(lambda r: r.update(updated_at="yesterday")))
        self.assertTrue(self.bad(lambda r: r["tasks"][0]["evidence"].append({"type": "software", "uri": "", "description": "x"})))

    def test_agrees_with_jsonschema_when_installed(self):
        try:
            import jsonschema
        except ImportError:
            self.skipTest("jsonschema not installed")
        for mutate in (lambda r: r.update(extra=1), lambda r: r["source"].update(commit="abc"),
                       lambda r: r["tasks"][0].update(execution="IMPLEMENTED"), lambda r: None):
            r = copy.deepcopy(self.good)
            mutate(r)
            theirs = not list(jsonschema.Draft202012Validator(self.schema).iter_errors(r))
            self.assertEqual(theirs, not gs.validate(r, self.schema))


def sh(cwd, *args):
    env = dict(os.environ, GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@example.invalid",
               GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@example.invalid",
               GIT_AUTHOR_DATE="2026-10-29T10:00:00+05:30", GIT_COMMITTER_DATE="2026-10-29T10:00:00+05:30")
    return subprocess.run(["git", *args], cwd=cwd, env=env, capture_output=True, text=True, check=True).stdout.strip()


class GitFlow(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        sh(self.root, "init", "-q", "-b", "main")
        (self.root / "planning").mkdir()
        self.write_register(register(row("001"), row("002", deps="001")))
        sh(self.root, "add", "-A")
        sh(self.root, "commit", "-q", "-m", "docs(x): register\n\nTasks: None (test)")

    def tearDown(self):
        self.tmp.cleanup()

    def write_register(self, text):
        (self.root / "planning" / "TASKS.md").write_text(text, encoding="utf-8")

    def commit_all(self, msg):
        sh(self.root, "add", "-A")
        sh(self.root, "commit", "-q", "-m", msg)
        return sh(self.root, "rev-parse", "HEAD")

    def test_source_commit_and_time(self):  # AC-005-02
        head = sh(self.root, "rev-parse", "HEAD")
        r = json.loads(gs.generate(self.root))
        self.assertEqual(r["source"]["commit"], head)
        self.assertRegex(r["source"]["commit"], r"^[0-9a-f]{40}$")
        self.assertEqual(r["updated_at"], "2026-10-29T04:30:00Z")

    def test_same_commit_gives_identical_bytes(self):  # AC-005-04
        self.assertEqual(gs.generate(self.root), gs.generate(self.root))

    def test_inputs_come_from_the_commit_not_the_working_tree(self):
        first = gs.generate(self.root)
        self.write_register(register(row("001", execution="COMPLETE")))  # uncommitted edit
        self.assertEqual(gs.generate(self.root), first)

    def test_two_commit_flow_passes_check(self):
        main = __import__("gen_status")
        self.assertEqual(main.main(["--root", str(self.root), "--write"]), 0)
        self.commit_all("chore(status): generate\n\nTasks: None (test)")
        self.assertEqual(gs.check(self.root), [])

    def test_check_detects_stale_register(self):  # AC-005-03
        gs.main(["--root", str(self.root), "--write"])
        self.commit_all("chore(status): generate\n\nTasks: None (test)")
        self.write_register(register(row("001", execution="IMPLEMENTED"), row("002", deps="001")))
        self.commit_all("docs(x): change register\n\nTasks: None (test)")
        self.assertTrue(any("stale" in p for p in gs.check(self.root)))

    def test_check_detects_hand_edit(self):
        gs.main(["--root", str(self.root), "--write"])
        path = self.root / "status" / "status.json"
        r = json.loads(path.read_text())
        r["tasks"][0]["execution"] = "COMPLETE"
        path.write_text(json.dumps(r, indent=2) + "\n")
        self.commit_all("chore(status): tamper\n\nTasks: None (test)")
        self.assertTrue(gs.check(self.root))

    def test_check_detects_unknown_commit_and_missing_file(self):
        self.assertTrue(any("does not exist" in p for p in gs.check(self.root)))
        gs.main(["--root", str(self.root), "--write"])
        path = self.root / "status" / "status.json"
        path.write_text(path.read_text().replace(json.loads(path.read_text())["source"]["commit"], "b" * 40))
        self.assertTrue(gs.check(self.root))

    def test_failed_generation_writes_nothing(self):
        self.write_register(register(row("001", deps="009")))
        self.commit_all("docs(x): bad\n\nTasks: None (test)")
        self.assertEqual(gs.main(["--root", str(self.root), "--write"]), 1)
        self.assertFalse((self.root / "status" / "status.json").exists())


class CommittedStatus(unittest.TestCase):
    def test_committed_report_is_good(self):
        if not (ROOT / "status" / "status.json").is_file():
            self.skipTest("status/status.json is not committed yet")
        if subprocess.run(["git", "rev-parse", "--git-dir"], cwd=ROOT, capture_output=True).returncode:
            self.skipTest("not a git checkout")
        self.assertEqual(gs.check(ROOT), [])


if __name__ == "__main__":
    unittest.main()
