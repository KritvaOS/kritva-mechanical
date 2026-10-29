# Robot Mechanical Task Register

| Property | Value |
|---|---|
| Document ID | KOS-MECH-TASKS |
| Repository | `KritvaOS/kritva-mechanical` |
| Document Type | Plan |
| Status | PROPOSED (task IDs are provisional until the `ROB-MECH` prefix is registered with kritva-program) |
| Owner | Dinesh (program owner) |
| Reviewer / Approver | Dinesh; independent mechanical reviewer not yet identified (program decision PD-007 pending) |
| Version | 0.1.0 |
| Last Updated | 2026-10-28 |
| Authority | AUTHORITATIVE for this repository's local task records (role, not approval). INPUT to `status/status.json` once that exists. Not the program baseline. |
| Related Tasks / Milestones | ROB-MECH-001 to ROB-MECH-042; ROB-M0 to ROB-M5; alignment batch B3 |
| Related Documents | [MILESTONE.md](MILESTONE.md), [README.md](../README.md); kritva-program [acceptance standard](https://github.com/KritvaOS/kritva-program/blob/main/v2/planning/ACCEPTANCE_STANDARD.md) |

## Purpose

This is the single canonical local task register for the robot mechanical work. It lists every task, its order, its dependencies and what it must produce. It is read by whoever plans, performs, reviews or reports the work.

It is a planning inventory. Every task here is PROPOSED. A task has no program weight and earns no program credit until the `ROB-MECH` prefix is registered and the task is added to the approved baseline through the program's approval process. A task being listed, started, committed or marked complete locally does not make it accepted progress.

## 1. Rules for this register

1. **One register.** This file is the only local task database. Do not keep a second list in a spreadsheet, issue tracker or other file; derived views are generated from here.
2. **Stable IDs.** An ID has the form `ROB-MECH-NNN` and is never renumbered or reused. A retired task keeps its ID with status CANCELLED and a reason in the changelog.
3. **Existing IDs are untouched.** Actuator task IDs (`ACT-INT`, `ACT-EMB`, `ACT-S`, `ACT-M`, `ACT-L`) and all frozen program IDs are preserved and not reused here.
4. **Every commit names a task.** A commit that belongs to no task here needs a task created first (see `GIT_COMMIT_STEP.md`). Only a docs or chore commit that implements no task may use `Tasks: None (reason)`.
5. **Local status is a fact report, not acceptance.** Status values below describe implementation. Acceptance is decided by the program.
6. **Hold-blocked tasks stay BLOCKED.** Tasks that need mechanical CAD, BOM, quotes, procurement, fabrication or physical work stay BLOCKED until an owner decision reopens robot mechanical work. Planning them is allowed; doing them is not.
7. **Evidence type is always stated.** S software check, C calculation, Sim simulation, B bench measurement, P independently accepted physical test. Software, calculation and simulation evidence is never reported as physical verification.

## 2. Status vocabulary

| Column | Values | Meaning |
|---|---|---|
| Execution | NOT_STARTED, IN_PROGRESS, IMPLEMENTED, VERIFICATION_PENDING, BLOCKED, COMPLETE, CANCELLED | IMPLEMENTED means the document, CAD or code exists but is not accepted. COMPLETE means local acceptance criteria are met and the required review is recorded. |
| Review | NOT_REVIEWED, IN_REVIEW, CHANGES_REQUESTED, REVIEWED | Review state against the closing commit. |
| Acceptance | NOT_RUN, PASS, FAIL, WAIVED | Result of the task's criteria. WAIVED needs a structured approval record and is never reported as PASS. |
| Git | NOT_COMMITTED, COMMITTED, SYNCED | SYNCED means pushed and the commit SHA is recorded on the task. |

All tasks below start at NOT_STARTED / NOT_REVIEWED / NOT_RUN / NOT_COMMITTED unless a Notes entry says BLOCKED.

## 3. Task register

Owners are UNASSIGNED until the owner assigns them. "Gate" names what limits the task beyond planning (see [MILESTONE.md](MILESTONE.md) section 5).

### 3.1 Setup (alignment batch B3, needed before milestone work can be reported)

| ID | Task | Depends on | Owner | Execution | Review | Acceptance | Git | Notes |
|---|---|---|---|---|---|---|---|---|
| ROB-MECH-001 | Prepare the registration proposal for the mechanical workstream, task prefix and ROB- naming for kritva-program | none | UNASSIGNED | IMPLEMENTED | NOT_REVIEWED | NOT_RUN | NOT_COMMITTED | Proposal only; this repository does not edit the program baseline. Owner decision needed. Draft in [REGISTRATION_PROPOSAL.md](REGISTRATION_PROPOSAL.md); implemented, not accepted. |
| ROB-MECH-002 | Add repository governance files: `AGENTS.md`, `SECURITY.md`, `CONTRIBUTING.md`, `.github/CODEOWNERS`, `.github/PULL_REQUEST_TEMPLATE.md` | none | UNASSIGNED | IMPLEMENTED | NOT_REVIEWED | NOT_RUN | NOT_COMMITTED | No secrets; real license only. Drafts in place; implemented, not accepted. Owner confirmed the CODEOWNERS login (@dineshannayya) on 2026-10-29; the security route is still to be confirmed. |
| ROB-MECH-003 | Add CI workflows `secret-scan` and `commit-message-check` | 002 | UNASSIGNED | IMPLEMENTED | NOT_REVIEWED | NOT_RUN | NOT_COMMITTED | Do not add allowlist entries to silence the scan. Workflows, `.gitleaks.toml`, vendored checker and unit tests drafted; no CI run yet, so AC-003-01 to AC-003-03 are NOT_RUN. Implemented, not accepted. |
| ROB-MECH-004 | Add a Makefile exposing the standard gate targets, each unimplemented one exiting with code 3 `NOT_IMPLEMENTED` | 002 | UNASSIGNED | NOT_STARTED | NOT_REVIEWED | NOT_RUN | NOT_COMMITTED | An unimplemented gate is never a pass |
| ROB-MECH-005 | Generate `status/status.json` (schema 2.0) from this register and validate it | 001, 004 | UNASSIGNED | NOT_STARTED | NOT_REVIEWED | NOT_RUN | NOT_COMMITTED | Exact 40-character source commit; no unrecognised fields |
| ROB-MECH-006 | Register the status source in kritva-program and run the source refresh and consolidation check | 001, 005 | UNASSIGNED | NOT_STARTED | NOT_REVIEWED | NOT_RUN | NOT_COMMITTED | Done in kritva-program by the owner; registration alone grants no credit |

### 3.2 ROB-M0 Requirements baseline

| ID | Task | Depends on | Owner | Execution | Review | Acceptance | Git | Notes |
|---|---|---|---|---|---|---|---|---|
| ROB-MECH-007 | Define the ROB-A0 configuration and numeric targets | none | UNASSIGNED | NOT_STARTED | NOT_REVIEWED | NOT_RUN | NOT_COMMITTED | Owner confirms intent first |
| ROB-MECH-008 | Write mechanical requirements with stable IDs, units, verification methods and program traceability | 007 | UNASSIGNED | NOT_STARTED | NOT_REVIEWED | NOT_RUN | NOT_COMMITTED | |
| ROB-MECH-009 | Define load cases with inputs, sources and result checks | 007 | UNASSIGNED | NOT_STARTED | NOT_REVIEWED | NOT_RUN | NOT_COMMITTED | |
| ROB-MECH-010 | Inventory actuator inputs (S, M, L, embedded) and label the maturity of each value | 007 | UNASSIGNED | NOT_STARTED | NOT_REVIEWED | NOT_RUN | NOT_COMMITTED | Placeholder or unverified values stay labelled |
| ROB-MECH-011 | Draft robot-to-actuator interface control document v0.1 | 008, 009, 010 | UNASSIGNED | NOT_STARTED | NOT_REVIEWED | NOT_RUN | NOT_COMMITTED | |
| ROB-MECH-012 | Create the initial risk and dependency register | 008, 010 | UNASSIGNED | NOT_STARTED | NOT_REVIEWED | NOT_RUN | NOT_COMMITTED | |
| ROB-MECH-013 | ROB-M0 review and completion record | 007 to 012 | UNASSIGNED | NOT_STARTED | NOT_REVIEWED | NOT_RUN | NOT_COMMITTED | Independent reviewer needed |

### 3.3 ROB-M1 Architecture

| ID | Task | Depends on | Owner | Execution | Review | Acceptance | Git | Notes |
|---|---|---|---|---|---|---|---|---|
| ROB-MECH-014 | Write the frame, torso, limb and joint architecture | 013 | UNASSIGNED | NOT_STARTED | NOT_REVIEWED | NOT_RUN | NOT_COMMITTED | |
| ROB-MECH-015 | Joint axis and load-path study | 014 | UNASSIGNED | NOT_STARTED | NOT_REVIEWED | NOT_RUN | NOT_COMMITTED | Calculation evidence only |
| ROB-MECH-016 | Mass budget and centre-of-mass target | 014 | UNASSIGNED | NOT_STARTED | NOT_REVIEWED | NOT_RUN | NOT_COMMITTED | |
| ROB-MECH-017 | Interface definitions v1.0 candidate, agreed with the actuator repositories | 011, 014 | UNASSIGNED | NOT_STARTED | NOT_REVIEWED | NOT_RUN | NOT_COMMITTED | Cites the commit of each source |
| ROB-MECH-018 | Wiring and service-access envelopes (space reservation only) | 014 | UNASSIGNED | NOT_STARTED | NOT_REVIEWED | NOT_RUN | NOT_COMMITTED | Not the electrical design |
| ROB-MECH-019 | Prepare the CAD tool, file format, revision and artifact-storage convention for owner decision | 014 | UNASSIGNED | NOT_STARTED | NOT_REVIEWED | NOT_RUN | NOT_COMMITTED | |
| ROB-MECH-020 | Create the CAD skeleton (reference geometry only) | 017, 019 | UNASSIGNED | BLOCKED | NOT_REVIEWED | NOT_RUN | NOT_COMMITTED | BLOCKED by the mechanical hold |
| ROB-MECH-021 | ROB-M1 review and completion record | 014 to 020 | UNASSIGNED | NOT_STARTED | NOT_REVIEWED | NOT_RUN | NOT_COMMITTED | Task 020 may be recorded as deferred by decision |

### 3.4 ROB-M2 Detailed design (all BLOCKED by the mechanical hold)

| ID | Task | Depends on | Owner | Execution | Review | Acceptance | Git | Notes |
|---|---|---|---|---|---|---|---|---|
| ROB-MECH-022 | Part and assembly CAD | 021 | UNASSIGNED | BLOCKED | NOT_REVIEWED | NOT_RUN | NOT_COMMITTED | Hold |
| ROB-MECH-023 | Drawings with tolerances | 022 | UNASSIGNED | BLOCKED | NOT_REVIEWED | NOT_RUN | NOT_COMMITTED | Hold |
| ROB-MECH-024 | Bill of materials with unique part identifiers | 022 | UNASSIGNED | BLOCKED | NOT_REVIEWED | NOT_RUN | NOT_COMMITTED | Hold |
| ROB-MECH-025 | Engineering calculations covering every load case | 009, 022 | UNASSIGNED | BLOCKED | NOT_REVIEWED | NOT_RUN | NOT_COMMITTED | Hold |
| ROB-MECH-026 | Mass properties report and interference and clearance check | 022 | UNASSIGNED | BLOCKED | NOT_REVIEWED | NOT_RUN | NOT_COMMITTED | Hold |
| ROB-MECH-027 | ROB-M2 design review and completion record | 022 to 026 | UNASSIGNED | BLOCKED | NOT_REVIEWED | NOT_RUN | NOT_COMMITTED | Hold |

### 3.5 ROB-M3 Fabrication readiness (all BLOCKED by the mechanical hold and procurement authority)

| ID | Task | Depends on | Owner | Execution | Review | Acceptance | Git | Notes |
|---|---|---|---|---|---|---|---|---|
| ROB-MECH-028 | Manufacturing package and process selection | 027 | UNASSIGNED | BLOCKED | NOT_REVIEWED | NOT_RUN | NOT_COMMITTED | Hold |
| ROB-MECH-029 | Procurement list and supplier options | 024, 028 | UNASSIGNED | BLOCKED | NOT_REVIEWED | NOT_RUN | NOT_COMMITTED | No quotes without written authority |
| ROB-MECH-030 | Inspection plan with instruments, accuracy and acceptance limits | 023, 028 | UNASSIGNED | BLOCKED | NOT_REVIEWED | NOT_RUN | NOT_COMMITTED | Hold |
| ROB-MECH-031 | Assembly procedure draft | 028, 030 | UNASSIGNED | BLOCKED | NOT_REVIEWED | NOT_RUN | NOT_COMMITTED | Includes assembly hazard record |
| ROB-MECH-032 | Fabrication authorisation request for the owner | 029, 030, 031 | UNASSIGNED | BLOCKED | NOT_REVIEWED | NOT_RUN | NOT_COMMITTED | A request, never an authorisation |
| ROB-MECH-033 | ROB-M3 review and completion record | 028 to 032 | UNASSIGNED | BLOCKED | NOT_REVIEWED | NOT_RUN | NOT_COMMITTED | Hold |

### 3.6 ROB-M4 Assembly and inspection (all BLOCKED by fabrication authority and open safety gates)

| ID | Task | Depends on | Owner | Execution | Review | Acceptance | Git | Notes |
|---|---|---|---|---|---|---|---|---|
| ROB-MECH-034 | Receiving inspection of parts | 033 | UNASSIGNED | BLOCKED | NOT_REVIEWED | NOT_RUN | NOT_COMMITTED | Physical work |
| ROB-MECH-035 | Assemble the authorised prototype | 034 | UNASSIGNED | BLOCKED | NOT_REVIEWED | NOT_RUN | NOT_COMMITTED | Physical work |
| ROB-MECH-036 | As-built record and deviation register | 035 | UNASSIGNED | BLOCKED | NOT_REVIEWED | NOT_RUN | NOT_COMMITTED | |
| ROB-MECH-037 | Mechanical integration fit with the actuators | 035 | UNASSIGNED | BLOCKED | NOT_REVIEWED | NOT_RUN | NOT_COMMITTED | Needs actuator gate state recorded |
| ROB-MECH-038 | ROB-M4 review and completion record | 034 to 037 | UNASSIGNED | BLOCKED | NOT_REVIEWED | NOT_RUN | NOT_COMMITTED | |

### 3.7 ROB-M5 Mechanical verification (all BLOCKED by fixture and safety review)

| ID | Task | Depends on | Owner | Execution | Review | Acceptance | Git | Notes |
|---|---|---|---|---|---|---|---|---|
| ROB-MECH-039 | Test plan, procedures and controlled fixture | 038 | UNASSIGNED | BLOCKED | NOT_REVIEWED | NOT_RUN | NOT_COMMITTED | Safety review of the plan |
| ROB-MECH-040 | Execute mechanical tests and record results per revision | 039 | UNASSIGNED | BLOCKED | NOT_REVIEWED | NOT_RUN | NOT_COMMITTED | Physical work |
| ROB-MECH-041 | Defect closure | 040 | UNASSIGNED | BLOCKED | NOT_REVIEWED | NOT_RUN | NOT_COMMITTED | |
| ROB-MECH-042 | Independent acceptance and ROB-M5 completion record | 040, 041 | UNASSIGNED | BLOCKED | NOT_REVIEWED | NOT_RUN | NOT_COMMITTED | |

## 4. Task definitions

Each task is done only when the program definition of done holds (stable ID, testable criteria in [ACCEPTANCE_CRITERIA.md](ACCEPTANCE_CRITERIA.md), merged through the required review, required checks passed on the exact closing commit, reviews recorded against that commit, documentation updated, evidence pointing at immutable references). The tables give the specifics. Criteria IDs are written in `ACCEPTANCE_CRITERIA.md` in the form `AC-NNN-nn`, where NNN is the task number.

### 4.1 Setup

| Task | Deliverable | Evidence type | Reviewer | Gate |
|---|---|---|---|---|
| 001 | A short proposal naming the workstream, the `ROB-MECH` prefix, the `ROB-` namespace and the dependency on the actuator workstreams | S | Owner | Owner decision |
| 002 | The five governance files, consistent with the program's required files list | S | Owner | None |
| 003 | Two workflows that run on every push and pull request | S (workflow run) | Owner | None |
| 004 | A Makefile where each standard target runs or exits 3 | S | Owner | None |
| 005 | A generator and a schema-valid report that matches this register | S | Owner | Needs registration for credit |
| 006 | A merged program change registering the source; consolidation check passes | S | Owner | Program change process |

### 4.2 ROB-M0

| Task | Deliverable | Evidence type | Reviewer | Gate |
|---|---|---|---|---|
| 007 | ROB-A0 configuration document with numeric targets, units and sources | S, review | Owner | None |
| 008 | `requirements/` set with IDs, units, methods and traces | S, review | Owner and independent reviewer | None |
| 009 | Load-case document | C, review | Independent reviewer | None |
| 010 | Table of actuator inputs with source repository, commit and maturity label | S, review | Actuator repository owners where applicable | None |
| 011 | Interface control document v0.1 | S, review | Owner and independent reviewer | None |
| 012 | Risk and dependency register with owners and responses | S, review | Owner | None |
| 013 | Approved completion record | Review | Owner and independent reviewer | None |

### 4.3 ROB-M1

| Task | Deliverable | Evidence type | Reviewer | Gate |
|---|---|---|---|---|
| 014 | Architecture documents under `architecture/` | S, review | Independent reviewer | None |
| 015 | Load-path study with stated assumptions | C | Independent reviewer | None |
| 016 | Mass budget with margin and CoM target | C | Independent reviewer | None |
| 017 | Versioned interface definitions with actuator commit references | S, review | Owner and actuator owners | None |
| 018 | Envelope definitions for harness and service access | S, review | Independent reviewer | None |
| 019 | Convention proposal and decision record request | S | Owner | Owner decision |
| 020 | CAD skeleton parsing cleanly, matching interface documents | S | Independent reviewer | Mechanical hold |
| 021 | Approved completion record | Review | Owner and independent reviewer | None |

### 4.4 ROB-M2 to ROB-M5

| Task | Deliverable | Evidence type | Reviewer | Gate |
|---|---|---|---|---|
| 022 | Released CAD with revision identifiers or checksums | S, Sim | Independent reviewer | Hold |
| 023 | Released drawings | S, review | Independent reviewer | Hold |
| 024 | BOM with unique identifiers and sources | S | Independent reviewer | Hold |
| 025 | Calculation set with margins | C | Independent reviewer | Hold |
| 026 | Mass properties and interference report | S, Sim | Independent reviewer | Hold |
| 027 | Approved completion record | Review | Owner and independent reviewer | Hold |
| 028 | Manufacturing package | S, review | Independent reviewer | Hold |
| 029 | Procurement list | S, review | Owner | Hold; quote and procurement authority |
| 030 | Inspection plan | S, review | Independent reviewer | Hold |
| 031 | Assembly procedure and hazard record | S, review | Independent and safety reviewers | Hold |
| 032 | Request document for fabrication authority | Review | Owner | Owner decision |
| 033 | Approved completion record | Review | Owner and independent reviewer | Hold |
| 034 | Receiving inspection records | B | Independent reviewer | Fabrication authority |
| 035 | Assembly record | B, review | Independent reviewer | Fabrication authority; safety gates |
| 036 | As-built record and deviation register | B, review | Independent reviewer | Fabrication authority |
| 037 | Fit records and actuator gate state | B, review | Independent reviewer | Actuator gates |
| 038 | Approved completion record | Review | Owner and independent reviewer | Fabrication authority |
| 039 | Approved test plan and fixture record | S, review | Independent and safety reviewers | Safety review |
| 040 | Immutable per-run results with manifest, environment, log, summary and checksums | B, P | Independent reviewer | Safety gates |
| 041 | Defect register with dispositions | B, review | Independent reviewer | Safety gates |
| 042 | Independent acceptance record and completion record | P, review | Independent mechanical and safety reviewers | Safety gates |

## 5. Dependencies and critical path

```text
Setup:   001 -> 005 -> 006            002 -> 003 / 004 -> 005
M0:      007 -> 008, 009, 010 -> 011 -> 013      (012 after 008, 010)
M1:      013 -> 014 -> 015, 016, 018 ; 011 + 014 -> 017 ; 014 -> 019 ; 017 + 019 -> 020 (hold) -> 021
M2:      021 -> 022 -> 023, 024, 026 ; 009 + 022 -> 025 -> 027
M3:      027 -> 028 -> 029, 030 -> 031 -> 032 -> 033
M4:      033 -> 034 -> 035 -> 036, 037 -> 038
M5:      038 -> 039 -> 040 -> 041 -> 042
```

The critical path to the first reportable outcome runs 007 to 011 to 013. It does not need the hold to be lifted. Setup tasks 001 to 006 run in parallel and are needed before any of this progress can be reported to kritva-program.

External dependencies, owned elsewhere: actuator data and interface agreement (actuator repositories, supply to 010, 011, 017, 037), program registration (kritva-program, tasks 001 and 006), and owner decisions on the hold, fabrication authority and reviewer roles.

## 6. Task record format

A task here is a row. When a task needs more than a row, its detail goes into `tasks/ROB-MECH-NNN/TASK.md` and `ACCEPTANCE_CRITERIA.md` beside it, created only when the task is approved to start; no empty folders or placeholder tasks. A task record carries these fields:

| Field | Meaning |
|---|---|
| id | The stable task ID |
| title | One line outcome |
| workstream | The registered program workstream (not yet registered) |
| milestone | ROB-M0 to ROB-M5, or B3 for setup |
| status | The four columns in section 2 |
| owner | A named person, or UNASSIGNED |
| dependencies | Task IDs |
| acceptance criteria | The `AC-NNN-nn` IDs |
| verification | Sanity and regression tests that apply, and review requirements |
| evidence | Immutable references: commit SHAs and CI run IDs, never branch names |
| implementation commit | The 40-character SHA, once committed |
| review status | Review result and the commit reviewed |

This is a description of the fields, not a second database. The generator reads this register and the per-task files; nothing is maintained twice.

## 7. Reporting to kritva-program

Once registered, `status/status.json` reports the facts of each task in the program schema 2.0: implementation state, source commit, timestamps and evidence references. Hardware version and milestone association is carried in the approved task mapping or baseline metadata, not in unrecognised status fields. Program credit follows the program's rule: approved baseline task, passing evidence, recorded review, evidence commit and passing CI where applicable. A reported completion is not accepted progress.

## 8. Changes to this register

Add a task by taking the next unused number and giving it a milestone, dependencies, deliverable, evidence type and reviewer before work begins. Cancel a task by marking it CANCELLED with a reason. Record every change in [CHANGELOG.md](CHANGELOG.md). Do not alter the task list silently, and do not change a task's meaning after it has been accepted.
