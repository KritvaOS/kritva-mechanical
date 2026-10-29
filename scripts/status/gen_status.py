#!/usr/bin/env python3
"""Generate and check status/status.json (schema 2.0) from the task register (ROB-MECH-005).

Facts only. This report says what the register records about execution, Git
state and readiness. It says nothing about review, acceptance, credit, weights,
phases or gates; those belong to kritva-program (decision D-011).

Usage (run from anywhere inside the repository):
  python3 scripts/status/gen_status.py              print the report for HEAD
  python3 scripts/status/gen_status.py --write      write status/status.json from HEAD
  python3 scripts/status/gen_status.py --commit REV print or write for REV
  python3 scripts/status/gen_status.py --check      verify status/status.json

Inputs are read from the Git commit, not the working tree, so the same commit always
gives byte-identical output. `source.commit` is the commit the report was generated
from. A report cannot name the commit that contains it, so commit the register change
first, generate, then commit status/status.json in a second commit.

Fails closed: any problem is printed and the exit code is 1; nothing is written.
Exit codes: 0 ok; 1 a problem with the register, report or check; 2 usage or Git error.

Mapping from the register (planning/TASKS.md section 2) to schema 2.0:
  execution  NOT_STARTED -> NOT_STARTED; IN_PROGRESS, IMPLEMENTED, VERIFICATION_PENDING -> IN_PROGRESS;
             BLOCKED -> BLOCKED; COMPLETE -> COMPLETE; CANCELLED -> error (schema 2.0 has no value for it)
  git_sync   NOT_COMMITTED, COMMITTED, SYNCED map to themselves
  readiness  BLOCKED -> HARDWARE-BLOCKED; otherwise IMPLEMENTABLE when every dependency is
             IMPLEMENTED, VERIFICATION_PENDING or COMPLETE (or there are none), else PLANNABLE
  evidence   always empty until an evidence record format is approved
"""
import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SCHEMA_PATH = HERE / "status.schema.json"
TASKS_PATH = "planning/TASKS.md"
STATUS_PATH = "status/status.json"

# PROPOSED until the owner registers them in kritva-program (planning/REGISTRATION_PROPOSAL.md).
WORKSTREAM_ID = "ROB_MECH"
REPO = "KritvaOS/kritva-mechanical"

EXECUTION = {"NOT_STARTED", "IN_PROGRESS", "IMPLEMENTED", "VERIFICATION_PENDING", "BLOCKED", "COMPLETE", "CANCELLED"}
REVIEW = {"NOT_REVIEWED", "IN_REVIEW", "CHANGES_REQUESTED", "REVIEWED"}
ACCEPTANCE = {"NOT_RUN", "PASS", "FAIL", "WAIVED"}
GIT = {"NOT_COMMITTED", "COMMITTED", "SYNCED"}
EXEC_MAP = {
    "NOT_STARTED": "NOT_STARTED",
    "IN_PROGRESS": "IN_PROGRESS",
    "IMPLEMENTED": "IN_PROGRESS",
    "VERIFICATION_PENDING": "IN_PROGRESS",
    "BLOCKED": "BLOCKED",
    "COMPLETE": "COMPLETE",
}
READY_DEPS = {"IMPLEMENTED", "VERIFICATION_PENDING", "COMPLETE"}
TASK_ID = re.compile(r"^ROB-MECH-\d{3}$")
SHA = re.compile(r"^[0-9a-f]{40}$")
DATE_TIME = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")


class StatusError(Exception):
    """A problem that must stop generation (fail closed)."""

    def __init__(self, problems):
        self.problems = problems if isinstance(problems, list) else [problems]
        super().__init__("; ".join(self.problems))


# ---------------------------------------------------------------- register

def _split_row(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def _parse_deps(cell, task_id, problems):
    c = cell.strip().strip("`")
    if c.lower() == "none":
        return []
    out = []
    for part in c.split(","):
        part = part.strip()
        m = re.fullmatch(r"(\d{3}) to (\d{3})", part)
        if m:
            a, b = int(m.group(1)), int(m.group(2))
            if a > b:
                problems.append(f"{task_id}: dependency range {part!r} runs backwards")
            else:
                out.extend(f"ROB-MECH-{n:03d}" for n in range(a, b + 1))
        elif re.fullmatch(r"\d{3}", part):
            out.append(f"ROB-MECH-{part}")
        else:
            problems.append(f"{task_id}: cannot read dependency {part!r}")
    return out


def parse_register(text):
    """Return the task rows of planning/TASKS.md section 3 as a list of dicts, or raise StatusError."""
    lines = text.splitlines()
    try:
        start = next(i for i, l in enumerate(lines) if l.startswith("## 3. Task register"))
    except StopIteration:
        raise StatusError("section '## 3. Task register' not found in " + TASKS_PATH)
    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
    problems, tasks, seen = [], [], set()
    for line in lines[start:end]:
        if not line.startswith("| ROB-MECH-"):
            continue
        cells = _split_row(line)
        if len(cells) != 9:
            problems.append(f"row has {len(cells)} columns, expected 9: {line[:60]!r}")
            continue
        tid, title, deps, owner, execution, review, acceptance, git, notes = cells
        if not TASK_ID.match(tid):
            problems.append(f"bad task ID {tid!r}")
            continue
        if tid in seen:
            problems.append(f"duplicate task ID {tid}")
            continue
        seen.add(tid)
        for name, val, allowed in (("Execution", execution, EXECUTION), ("Review", review, REVIEW),
                                   ("Acceptance", acceptance, ACCEPTANCE), ("Git", git, GIT)):
            if val not in allowed:
                problems.append(f"{tid}: {name} value {val!r} is not in the vocabulary")
        if execution == "CANCELLED":
            problems.append(f"{tid}: CANCELLED has no schema 2.0 execution value; resolve it with the owner before generating")
        tasks.append({"task_id": tid, "deps": _parse_deps(deps, tid, problems),
                      "execution": execution, "git": git})
    if not tasks and not problems:
        problems.append("no task rows found in section 3")
    ids = {t["task_id"] for t in tasks}
    for t in tasks:
        for d in t["deps"]:
            if d == t["task_id"]:
                problems.append(f"{t['task_id']}: depends on itself")
            elif d not in ids:
                problems.append(f"{t['task_id']}: unknown dependency {d}")
    problems.extend(_cycles(tasks))
    if problems:
        raise StatusError(problems)
    return sorted(tasks, key=lambda t: t["task_id"])


def _cycles(tasks):
    graph = {t["task_id"]: [d for d in t["deps"] if d != t["task_id"]] for t in tasks}
    state, out = {}, []

    def visit(n, trail):
        state[n] = 1
        for d in graph.get(n, []):
            if state.get(d) == 1:
                out.append("dependency cycle: " + " -> ".join(trail + [n, d]))
            elif d in graph and state.get(d) is None:
                visit(d, trail + [n])
        state[n] = 2

    for n in graph:
        if state.get(n) is None:
            visit(n, [])
    return out


# ------------------------------------------------------------------ report

def build_report(tasks, commit, updated_at, branch=None, tag=None):
    by_id = {t["task_id"]: t for t in tasks}
    rows = []
    for t in tasks:
        ex = t["execution"]
        if ex == "BLOCKED":
            readiness = "HARDWARE-BLOCKED"
        elif all(by_id[d]["execution"] in READY_DEPS for d in t["deps"]):
            readiness = "IMPLEMENTABLE"
        else:
            readiness = "PLANNABLE"
        rows.append({"task_id": t["task_id"], "execution": EXEC_MAP[ex], "git_sync": t["git"],
                     "readiness": readiness, "evidence": []})
    return {
        "schema_version": "2.0",
        "workstream_id": WORKSTREAM_ID,
        "repo": REPO,
        "source": {"branch": branch, "commit": commit, "tag": tag},
        "tasks": rows,
        "updated_at": updated_at,
    }


def render(report):
    return json.dumps(report, indent=2, ensure_ascii=True) + "\n"


# ------------------------------------------------------- schema validation
# A small validator for the subset of JSON Schema that schema 2.0 uses, so CI needs no packages.

def _type_ok(value, name):
    return {"string": isinstance(value, str), "object": isinstance(value, dict),
            "array": isinstance(value, list), "null": value is None}.get(name, False)


def validate(instance, schema, path="$"):
    errors = []
    if "const" in schema and instance != schema["const"]:
        errors.append(f"{path}: must be {schema['const']!r}")
    if "enum" in schema and instance not in schema["enum"]:
        errors.append(f"{path}: {instance!r} is not one of {schema['enum']}")
    if "type" in schema:
        types = schema["type"] if isinstance(schema["type"], list) else [schema["type"]]
        if not any(_type_ok(instance, t) for t in types):
            errors.append(f"{path}: wrong type, expected {types}")
            return errors
    if isinstance(instance, str):
        if "pattern" in schema and not re.search(schema["pattern"], instance):
            errors.append(f"{path}: {instance!r} does not match {schema['pattern']}")
        if "minLength" in schema and len(instance) < schema["minLength"]:
            errors.append(f"{path}: shorter than {schema['minLength']}")
        if schema.get("format") == "date-time" and not DATE_TIME.match(instance):
            errors.append(f"{path}: {instance!r} is not an RFC 3339 UTC date-time")
    if isinstance(instance, dict):
        for key in schema.get("required", []):
            if key not in instance:
                errors.append(f"{path}: missing required property {key!r}")
        props = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            for key in instance:
                if key not in props:
                    errors.append(f"{path}: unrecognised property {key!r}")
        for key, sub in props.items():
            if key in instance:
                errors.extend(validate(instance[key], sub, f"{path}.{key}"))
    if isinstance(instance, list) and "items" in schema:
        for i, item in enumerate(instance):
            errors.extend(validate(item, schema["items"], f"{path}[{i}]"))
    return errors


def load_schema():
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


# --------------------------------------------------------------------- git

def _git(root, *args, check=True):
    r = subprocess.run(["git", *args], cwd=root, capture_output=True, text=True)
    if check and r.returncode:
        raise OSError(r.stderr.strip() or f"git {' '.join(args)} failed")
    return r


def resolve_commit(root, rev):
    r = _git(root, "rev-parse", "--verify", "--quiet", f"{rev}^{{commit}}", check=False)
    sha = r.stdout.strip()
    if r.returncode or not SHA.match(sha):
        raise StatusError(f"commit {rev!r} not found (a shallow clone lacks history; fetch full history)")
    return sha


def file_at(root, commit, path):
    r = _git(root, "show", f"{commit}:{path}", check=False)
    if r.returncode:
        raise StatusError(f"{path} not found at commit {commit[:10]}")
    return r.stdout


def commit_time_utc(root, commit):
    iso = _git(root, "show", "-s", "--format=%cI", commit).stdout.strip()
    return datetime.fromisoformat(iso).astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def generate(root, rev="HEAD"):
    commit = resolve_commit(root, rev)
    tasks = parse_register(file_at(root, commit, TASKS_PATH))
    report = build_report(tasks, commit, commit_time_utc(root, commit))
    problems = validate(report, load_schema())
    if problems:
        raise StatusError(problems)
    return render(report)


# ------------------------------------------------------------------- check

def check(root):
    """Return a list of problems with status/status.json (empty list means it is good)."""
    path = Path(root) / STATUS_PATH
    if not path.is_file():
        return [f"{STATUS_PATH} does not exist"]
    text = path.read_text(encoding="utf-8")
    try:
        report = json.loads(text)
    except ValueError as e:
        return [f"{STATUS_PATH} is not valid JSON: {e}"]
    problems = [f"schema: {p}" for p in validate(report, load_schema())]
    if problems:
        return problems
    if report["workstream_id"] != WORKSTREAM_ID or report["repo"] != REPO:
        problems.append("workstream_id or repo differs from this generator's constants")
    commit = report["source"]["commit"]
    try:
        resolve_commit(root, commit)
        regenerated = generate(root, commit)
    except StatusError as e:
        return problems + [f"cannot regenerate from source.commit: {p}" for p in e.problems]
    except OSError as e:
        return problems + [f"git error: {e}"]
    if regenerated != text:
        problems.append("report differs from a regeneration at source.commit (edited by hand, or generated with other inputs)")
    try:
        current = parse_register((Path(root) / TASKS_PATH).read_text(encoding="utf-8"))
    except StatusError as e:
        return problems + [f"current register: {p}" for p in e.problems]
    expected = render(build_report(current, commit, report["updated_at"], report["source"].get("branch"), report["source"].get("tag")))
    if expected != text:
        problems.append("stale: the register in the working tree differs from the report (commit the register change, "
                        "regenerate, then commit status/status.json)")
    return problems


# --------------------------------------------------------------------- cli

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--write", action="store_true", help="write status/status.json")
    g.add_argument("--check", action="store_true", help="verify status/status.json")
    ap.add_argument("--commit", default="HEAD", help="commit to generate from (default HEAD)")
    ap.add_argument("--root", default=str(ROOT), help="repository root")
    a = ap.parse_args(argv)
    root = Path(a.root)
    try:
        if a.check:
            problems = check(root)
            for p in problems:
                print(f"status check: {p}", file=sys.stderr)
            if problems:
                return 1
            print("status check ok")
            return 0
        text = generate(root, a.commit)
    except StatusError as e:
        for p in e.problems:
            print(f"status: {p}", file=sys.stderr)
        return 1
    except OSError as e:
        print(f"git error: {e}", file=sys.stderr)
        return 2
    if a.write:
        out = root / STATUS_PATH
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text, encoding="utf-8")
        print(f"wrote {STATUS_PATH}")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
