# Registration Proposal for kritva-program

| Property | Value |
|---|---|
| Document ID | KOS-MECH-REGISTRATION-PROPOSAL |
| Repository | `KritvaOS/kritva-mechanical` |
| Document Type | Proposal |
| Status | PROPOSED (task ROB-MECH-001 implemented as a draft; not reviewed, not accepted, not decided) |
| Owner | Dinesh (program owner) |
| Reviewer / Approver | Dinesh (decision); independent reviewer roles unresolved (PD-007) |
| Version | 0.1.0 |
| Last Updated | 2026-10-29 |
| Authority | PROPOSAL only. It decides nothing. Every program record it mentions changes only through kritva-program and the owner's decision |
| Related Tasks / Milestones | ROB-MECH-001 (this proposal), ROB-MECH-004, ROB-MECH-005, ROB-MECH-006; alignment batch B3 |
| Related Documents | [TASKS.md](TASKS.md), [MILESTONE.md](MILESTONE.md), [ACCEPTANCE_CRITERIA.md](ACCEPTANCE_CRITERIA.md), [CHANGELOG.md](CHANGELOG.md), [GIT_COMMIT_STEP.md](GIT_COMMIT_STEP.md), [External review](../reviews/2026-10-28-external-review-chatgpt.md), [README.md](../README.md) |

## Purpose

This proposal asks the program owner to register the robot-level mechanical repository in kritva-program: which workstream it reports under, which task prefix it uses, how its names relate to the actuator workstreams, and what the owner would change on the program side. It is read by the owner, who decides, and by the reviewer of ROB-MECH-001 to ROB-MECH-006.

It makes no change to kritva-program. Registering a repository gives it a place to report facts; it gives no task credit, no weight and no approval, and it does not lift the mechanical hold.

## 1. What exists today (read from a local copy of kritva-program)

The local program clone was at commit `ff6d33a`; it may be behind GitHub, so the owner should re-check these facts against `main` before deciding.

| Fact | Where | Consequence for this proposal |
|---|---|---|
| `MECHANICAL` is a workstream with `repo: null` and `hold: true` | `v2/tracking/workstreams.json` | The robot-level hold is still recorded; this proposal must not clear it |
| `ACT_S`, `ACT_M`, `ACT_L` are `EXECUTION_WORKSTREAM`s with their own repositories, `effort_owner: false`, and `rolls_up_to: ["MECHANICAL"]` | `workstreams.json` | There is an existing pattern: an execution workstream with its own repository that rolls up to a parent |
| `ACT_INT` rolls up to `INTEGRATION_SOFTWARE_VALIDATION`; `ACT_EMB` rolls up to `ACTUATION_CONTROLS` and `ELECTRICAL_POWER` | `workstreams.json` | The actuator interface and embedded work already have homes; robot mechanical work must not duplicate them |
| D-003 puts mechanical work on hold (CAD, actuators, BOM, quotes, procurement, fabrication, prototype, design freeze); D-052 lifts it only for `ACT_S`, `ACT_M`, `ACT_L`, `ACT_EMB` and `ACT_INT` | `v2/DECISIONS.md` | Robot-level work is not authorised by D-052 |
| Actuator repositories are registered in `repo-pipeline.json` with `workstream_id`, `task_prefix`, `depends_on`, approvals, checks, gates and `task_registry.type: program-inventory`, `baselined: false` | `v2/planning/repo-pipeline.json` | A registry entry shape exists to copy |
| `baseline.json` has `mechanical_hold_reopened_by_decision: null` and no mechanical tasks | `v2/tracking/baseline.json` | Nothing here may add a baseline task |
| `sources.json` lists CORE, COMMUNITY and CI_DEV_INFRA only | `v2/tracking/sources.json` | Source registration (ROB-MECH-006) is a later, separate program change |
| PD-002 (P6 reopening criteria), PD-004 (task ID and repo registry approval), PD-007 (reviewer roles) and PD-014 (repo-on-workstream registration pattern) are pending | `v2/planning/PENDING_DECISIONS.md` | The owner can decide this proposal together with PD-004 and PD-014, which are the same kind of change |

## 2. Names proposed

All names below are PROPOSED. None is registered.

| Item | Proposed value | Notes |
|---|---|---|
| Repository | `KritvaOS/kritva-mechanical` | Exists; planning only today |
| Workstream ID | `ROB_MECH` | Matches the schema pattern `^[A-Z][A-Z0-9_]*$` (underscores allowed, hyphens not) |
| Workstream kind | `EXECUTION_WORKSTREAM`, `effort_owner: false` | Same as `ACT_S`, `ACT_M`, `ACT_L` |
| Rolls up to | `MECHANICAL` | The hold stays on `MECHANICAL`; the roll-up means robot-level work inherits it |
| Task prefix | `ROB-MECH` | Tasks are `ROB-MECH-NNN`; 42 exist in [TASKS.md](TASKS.md) |
| Namespace | `ROB-` | Reserved for robot-level artefacts: `ROB-MECH-NNN` tasks, `ROB-M0` to `ROB-M5` milestones, `ROB-A0` and `ROB-A1` robot hardware baselines |
| Repository registry code | `MECH` | Needs the owner's confirmation that it does not clash with an existing code |
| Registry kind | to be chosen by the owner | The actuator repositories use `hardware-interface`; this repository is robot-level mechanical planning, so the owner should say whether that kind fits or a new one is needed |

Why a new `ROB_MECH` workstream rather than giving `MECHANICAL` a repository: `MECHANICAL` is the parent that `ACT_S`, `ACT_M` and `ACT_L` already roll up to. Setting its `repo` would make the parent also an execution workstream and blur the line between robot-level work and actuator work, which is the double-counting the external review warned about (ER-03). A child workstream keeps the existing pattern and the hold on the parent.

Alternative (not recommended): set `MECHANICAL.repo` to `KritvaOS/kritva-mechanical`. It needs one fewer record, but the status report would then speak for the whole parent and the roll-up from the actuator workstreams would sit awkwardly beside it. The owner may choose it; the rest of this proposal then reads with `MECHANICAL` in place of `ROB_MECH`.

### 2.1 Why the names do not collide

| Existing name family | Used for | Relation to `ROB-` |
|---|---|---|
| `KF-CORE-R10`, `KOS-I2` to `KOS-I4`, `KRP-ENG` | Baselined program tasks | Different prefix; no overlap |
| `ACT-INT`, `ACT-EMB`, `ACT-S`, `ACT-M`, `ACT-L` (task prefixes) | Actuator tasks and milestones, owned by the actuator repositories | Different prefix. Robot tasks may depend on actuator values but never restate or re-plan them |
| Program phases P0 to P8, actuator milestones A0 to A2, Gates A, B, C | Program and actuator planning | Left untouched. `ROB-M0` to `ROB-M5` and `ROB-A0`, `ROB-A1` are separate namespaces. B0 to B4 are alignment batches, not milestones |

## 3. Relationship to the actuator workstreams

| Workstream | Owns | `ROB_MECH` relation |
|---|---|---|
| `ACT_S`, `ACT_M`, `ACT_L` | Actuator mechanical design per variant | `ROB_MECH` consumes their published interface values (envelope, mass, torque, speed, limits) through the interface control document (ROB-MECH-010, 011). It never edits them |
| `ACT_INT` | Actuator interface and hardware-validation integration | `ROB_MECH` depends on it for mounting and interface definitions |
| `ACT_EMB` | Actuator embedded, electrical and control side | `ROB_MECH` depends on it for connector, cable and thermal inputs |
| `MECHANICAL` | Parent record with the hold | `ROB_MECH` rolls up to it; the hold applies |

Rules that follow:

1. Each piece of work has one home. Actuator internals stay in the actuator repositories; robot-level frame, mounting, kinematic layout and integration stay here.
2. A value that crosses the boundary is recorded once, in the interface control document, with the owning repository, exact revision, units and maturity.
3. Status reports from `ROB_MECH` list only `ROB-MECH-NNN` tasks. The consolidator already rejects reports whose tasks are not in the baseline, so no task is counted twice.

## 4. What this proposal does not change (AC-001-02)

| Program record | Changed by this proposal? |
|---|---|
| Baseline (`baseline.json`), task weights, milestones | No. No `ROB-MECH` task is proposed for the baseline in this step. Weights stay `null` until the owner uses the program's baseline freeze tooling |
| Approvals and gate records (`approvals.json`, `gate_closures.json`, `GATE_REGISTER.md`) | No |
| The mechanical hold (D-003, `MECHANICAL.hold`, `mechanical_hold_reopened_by_decision`) | No. Reopening needs its own recorded owner decision (see PD-002) |
| Phases P0 to P8, actuator milestones A0 to A2, Gates A to C | No |
| Status schema 2.0 | No. The status report will use only the fields the schema allows (`additionalProperties` is false); no phase, weight or acceptance field is added |
| Credit | None. Registration is not progress. Every `ROB-MECH` task stays NOT_STARTED, NOT_REVIEWED, NOT_RUN as recorded in [TASKS.md](TASKS.md) |

## 5. How this maps to the program's onboarding steps

Source: `v2/tracking/ONBOARDING.md` (D-017). Preconditions and steps are the program's; the right-hand column is this repository's current state.

| Onboarding item | Needed | State here |
|---|---|---|
| Precondition: repository exists with a workstream ID that has a real repo in `workstreams.json` | Program change (owner) | Repository exists; workstream not registered |
| Precondition: stable task IDs in the repository's own records | Done | 42 IDs in [TASKS.md](TASKS.md), never reused |
| Precondition: mechanical stays on hold until the owner reopens | Policy | Kept; [MILESTONE.md](MILESTONE.md) gate matrix blocks hold-dependent tasks |
| Step 1: status generator in the repository, schema 2.0, facts only, fails closed | ROB-MECH-005 | Not implemented |
| Step 2: tests and CI with the vendored schema and its SHA-256 | ROB-MECH-003, 004, 005 | Not implemented |
| Step 3: baseline entry by central decision, weights `null` | Program change (owner) | Not proposed in this step |
| Step 4: register source in `sources.json` (pinned ref) and an example under `examples/sources/` | ROB-MECH-006 | Not done; depends on 001 and 005 |
| Step 5: evidence SHAs resolved by the program tool, history snapshot | Program tooling | Not applicable until a report exists |

## 6. Program-side changes the owner would make

These are listed so the owner can review the exact change. This repository makes none of them. Each is a pull request in kritva-program, under that repository's own rules (branch, task footer, checks, owner approval, merge commit).

| # | Program file | Proposed change | Effect |
|---|---|---|---|
| 1 | `v2/tracking/workstreams.json` | Add `ROB_MECH`: name "Robot mechanical (kritva-mechanical)", `repo` `KritvaOS/kritva-mechanical`, `kind` `EXECUTION_WORKSTREAM`, `effort_owner` false, `rolls_up_to` `["MECHANICAL"]`. Leave `MECHANICAL` unchanged | Gives the repository a workstream; nothing is counted |
| 2 | `v2/planning/repo-pipeline.json` | Add a `kritva-mechanical` entry modelled on the actuator entries: `workstream_id` `ROB_MECH`, `task_prefix` `ROB-MECH`, `depends_on` the actuator repositories it consumes, `baselined` false, `on_hold` true, `task_registry.type` `program-inventory`, required checks `secret-scan` and `commit-message-check`, local gates `make check` and `make docs-check`, required approvals `REPO_CODE_OWNER` and `SAFETY_REVIEWER`, sequence after the actuator repositories | Records the repository, its checks and the approval path. `on_hold: true` keeps it out of the merge sequence's "ready" set |
| 3 | `v2/DECISIONS.md` (and the private record if the owner prefers) | A decision entry that approves items 1 and 2 and the `ROB-` namespace, states that the hold is unchanged and names the date and decider | The record that AC-001-03 needs |
| 4 | `v2/planning/PENDING_DECISIONS.md` source records | Mark PD-004 (and PD-014 if the owner treats it as the same pattern) as covering this repository, or leave them pending if the owner prefers a separate step | Keeps the pending list truthful |
| 5 | `v2/tracking/sources.json` and `examples/sources/` | Later, in ROB-MECH-006, only after the generator exists and its output validates | Makes the repository visible in consolidated status |

Not in this list on purpose: any change to `baseline.json`, `approvals.json`, `gate_closures.json`, `GATE_REGISTER.md` or the hold fields.

Whether `on_hold: true` is accepted by the pipeline schema for a repository whose parent workstream is on hold, and whether `HOLD` appears in the sequence tables the way it does for the actuator repositories, should be checked against the program's current tooling when the pull request is prepared. Nothing in this repository depends on the answer.

## 7. Owner decisions requested

Answer each with ACCEPT, CHANGE (say what) or DEFER. A deferral keeps the repository unregistered and the setup tasks that depend on registration waiting.

| # | Decision | Recommendation |
|---|---|---|
| D1 | Register a new child workstream `ROB_MECH` rolling up to `MECHANICAL`, instead of giving `MECHANICAL` a repository | Accept |
| D2 | Task prefix `ROB-MECH` and the `ROB-` namespace for tasks, milestones and robot hardware baselines | Accept |
| D3 | Registry code and kind for the repository (`MECH` and a kind to be chosen) | Owner to name |
| D4 | Repository dependencies in the registry: which actuator repositories to list in `depends_on` | Owner to confirm the list |
| D5 | Required approvals for the registry entry: `REPO_CODE_OWNER` and `SAFETY_REVIEWER`, noting both are currently the owner (D-047 interim, not independent) | Accept, with PD-007 still open |
| D6 | Keep the hold unchanged by this step | Accept |
| D7 | Visibility class of this repository | Owner to name |
| D8 | Combine with PD-004 and PD-014, or decide separately | Owner's choice |

## 8. Recording the decision (AC-001-03)

When the owner decides:

1. The decision is recorded in kritva-program as in section 6, item 3. That record is the authority; this file is not.
2. This repository then adds a row to the decision log below and a changelog entry in [CHANGELOG.md](CHANGELOG.md) that cites the decision reference and the merge commit.
3. [TASKS.md](TASKS.md) marks ROB-MECH-001 accepted only after review against AC-001-01 to AC-001-03. Until then it stays implemented, not accepted.

### Decision log

Append a row when the owner decides. Do not edit earlier rows.

| Date | Decision | Result (ACCEPT, CHANGE, DEFER) | Program reference (decision ID and commit) | Decided by |
|---|---|---|---|---|
| | No decision recorded yet | | | |

## 9. Criteria check (self-review, not acceptance)

| Criterion | Where met | Reviewer finding |
|---|---|---|
| AC-001-01: names the workstream ID, `ROB-MECH` prefix and `ROB-` namespace and their relation to `MECHANICAL`, `ACT_INT`, `ACT_EMB`, `ACT_S`, `ACT_M`, `ACT_L` | Sections 2 and 3 | Pending review |
| AC-001-02: changes no baseline, weight, approval or gate and adds no unrecognised status fields | Section 4 | Pending review |
| AC-001-03: the owner's decision is recorded with a reference | Section 8; log empty | Not met until the owner decides |

## 10. Limits

1. Facts about kritva-program come from a local clone that may be stale. They are not verified against GitHub.
2. The registry entry shape is copied from the actuator entries and has not been validated against the program's tooling.
3. The proposal does not say when robot mechanical work is reopened. That is a separate owner decision.
4. Several roles (independent mechanical and safety reviewer) are unresolved, so approvals listed here are interim, not independent.
