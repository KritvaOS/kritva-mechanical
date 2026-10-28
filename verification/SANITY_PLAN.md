# Sanity Plan

| Property | Value |
|---|---|
| Document ID | KOS-MECH-SANITY |
| Repository | `KritvaOS/kritva-mechanical` |
| Document Type | Plan |
| Status | PROPOSED (nothing in this plan is implemented yet) |
| Owner | Dinesh (program owner) |
| Reviewer / Approver | Dinesh; independent mechanical reviewer not yet identified (program decision PD-007 pending) |
| Version | 0.1.0 |
| Last Updated | 2026-10-28 |
| Authority | AUTHORITATIVE for the fast checks this repository requires on every pull request (role, not approval) |
| Related Tasks / Milestones | ROB-MECH-002 to ROB-MECH-005 (implementation); all ROB-M0 to ROB-M5 tasks (consumers) |
| Related Documents | [REGRESSION_PLAN.md](REGRESSION_PLAN.md), [ACCEPTANCE_CRITERIA.md](../planning/ACCEPTANCE_CRITERIA.md), [TASKS.md](../planning/TASKS.md), [README.md](../README.md); kritva-program [acceptance standard](https://github.com/KritvaOS/kritva-program/blob/main/v2/planning/ACCEPTANCE_STANDARD.md) |

## Purpose

This plan lists the fast checks that run on every pull request to catch malformed inputs, broken references, wrong units, unsafe commits and obvious errors before a human spends review time. It is read by whoever writes the checks, reviews pull requests or interprets a failure.

A sanity check answers "is this change well formed and internally consistent?" It does not answer "is the design correct?", "is it safe?" or "does it still meet accepted behaviour?" Those are the work of the regression plan, calculations, review and physical test.

## 1. Current state

Nothing in this plan is implemented. The repository has no Makefile, scripts, tests or workflows. Every check below is therefore NOT_IMPLEMENTED and must be reported that way, never as a pass. The implementing tasks are ROB-MECH-002 (governance files), ROB-MECH-003 (workflows), ROB-MECH-004 (Makefile) and ROB-MECH-005 (status generator).

The mechanical hold (program decision D-003) currently blocks CAD, BOM, drawings, procurement, fabrication and physical work for the robot scope. The checks are therefore introduced in two stages:

| Stage | Applies when | Checks |
|---|---|---|
| Stage 1: planning content | From the first implementation of tasks 002 to 005 | The repository-wide and document checks (SAN-001 to SAN-016) |
| Stage 2: design content | Only after an owner decision reopens robot mechanical work and the first CAD, BOM or drawing is committed | The mechanical checks (SAN-020 to SAN-027) |

A stage 2 check that has nothing to examine reports NOT_APPLICABLE with the reason, not PASS.

## 2. Principles

1. **Fast.** Every check runs on every pull request. The proposed time budget for the whole sanity set is 10 minutes; this is a target to be measured, not a commitment.
2. **Deterministic.** The same inputs give the same result. No check depends on network access, the clock or randomness, except the secret scan and the program commit checker where the tool requires it.
3. **Explicit results.** Each check ends in exactly one of PASS, FAIL, NOT_IMPLEMENTED or NOT_APPLICABLE. NOT_IMPLEMENTED exits with code 3 and is never counted as a pass. NOT_APPLICABLE needs a reason and, where the standard requires it, a structured approved disposition.
4. **Check the exact commit.** Results name the commit tested. A result from an older commit does not cover a newer one.
5. **Read-only.** A check never modifies repository content. Generators are separate commands whose output is then checked.
6. **No silencing.** A failing check is fixed, not skipped. Allowlist and ignore entries are proposed to the owner with a reason.
7. **Honest scope.** Each check states what it proves and what it does not.

## 3. Test tiers

This table is the common definition used by both verification plans.

| Tier | Name | Typical run | Merge or release policy |
|---|---|---|---|
| T0 | Static sanity | Every pull request | Required to pass; covered by this plan |
| T1 | Unit and reference regression | Every relevant pull request | Required to pass; covered by the regression plan |
| T2 | Integration and compatibility | Relevant pull requests and scheduled runs | Required for affected interfaces and milestones |
| T3 | Simulation and design verification | Design changes and milestone reviews | Required where acceptance criteria name it |
| T4 | Physical bench validation | Approved hardware milestones only | Controlled procedure, evidence and specialist sign-off |
| T5 | System-level acceptance | Robot integration and release | All subsystem gates and independent reviews |

This plan covers T0. T1 and T2 are in the regression plan. T3 to T5 are defined by the acceptance criteria of the milestones that use them (ROB-M2 to ROB-M5) and are blocked by the hold today.

## 4. Check catalogue

Each check has an ID, a purpose, the input it reads, the failure that blocks the merge, and the task that implements it. The command column names the planned Makefile target; none exists yet.

### 4.1 Repository-wide and document checks (stage 1)

| ID | Check | Inputs | Blocks the merge when | Planned target | Implemented by |
|---|---|---|---|---|---|
| SAN-001 | Required files exist | Repository tree | A required file is missing: README, LICENSE, `AGENTS.md`, `SECURITY.md`, `CONTRIBUTING.md`, CODEOWNERS, pull request template, workflows, and the planning and verification set | `make check` | 002, 004 |
| SAN-002 | Task register is well formed | `planning/TASKS.md` | An ID is not `ROB-MECH-NNN`, is duplicated or is renumbered; a dependency does not resolve or forms a cycle; a status value is outside the vocabulary; a BLOCKED task names no gate | `make check` | 004, 005 |
| SAN-003 | Acceptance criteria are consistent | `planning/ACCEPTANCE_CRITERIA.md`, task register | A criterion ID is not `AC-NNN-nn`, is duplicated or points to a missing task; a task has no criterion; a result value is invalid; a PASS has no evidence type | `make check` | 004 |
| SAN-004 | Milestone consistency | `planning/MILESTONE.md`, task register | A task names a milestone that does not exist; the summary table and the milestone records disagree on dependencies | `make check` | 004 |
| SAN-005 | Document headers | Human-maintained Markdown documents | A required header property is missing, the status is outside DRAFT, PROPOSED, APPROVED, DEPRECATED, the date is not ISO, or a document claims APPROVED with no recorded approval. Generated files are exempt and must carry their generator marker | `make docs-check` | 004 |
| SAN-006 | Local links resolve | All Markdown files | A relative link points to a file that does not exist | `make docs-check` | 004 |
| SAN-007 | README structure | `README.md` | The program README checker fails (required metadata, topics, links, no placeholder text) | `make docs-check` | 004 |
| SAN-008 | No placeholder text | Published documents | `TODO`, `TBD`, an unfilled angle-bracket field or lorem text appears outside code | `make docs-check` | 004 |
| SAN-009 | Secret scan | The change and history of the pull request | The scanner reports a finding. No allowlist entry is added to make it pass | workflow `secret-scan` | 003 |
| SAN-010 | Commit format and task footer | `origin/main..HEAD` | A commit lacks exactly one `Task:` or `Tasks:` footer, uses `Tasks: None` on a type other than docs or chore, names an unknown task ID, or carries an AI-session trailer or link | workflow `commit-message-check` | 003 |
| SAN-011 | Status report is valid and fresh | `status/status.json`, task register | The report fails schema 2.0, `source.commit` is not a full 40-character SHA, task IDs differ from the register, an unrecognised field appears, or regenerating gives different output | `make check` | 005 |
| SAN-012 | Evidence references are immutable | Result and completion records | A PASS cites a branch name instead of a 40-character commit SHA, lacks a CI run ID where one is required, or a run manifest is missing a required field or its checksums do not match | `make check` | 004 |
| SAN-013 | Evidence-type labels | Result and criteria files | A result has no evidence type, or a physical-test criterion is marked PASS with only S, C or Sim evidence | `make check` | 004 |
| SAN-014 | Hold guard | Paths controlled by the hold: `cad/`, `bom/`, `drawings/`, `assembly/`, `releases/` and procurement files | A change touches a hold-controlled path while no owner decision reopening robot mechanical work is cited in the owner's hold record | `make check` | 004 |
| SAN-015 | Prohibited and oversized files | The change | A binary design file lies outside the approved storage convention, a file exceeds the agreed size limit, or credentials or personal data appear | `make check` | 004 |
| SAN-016 | Structured-data sanity | Requirements, load cases, interface tables and any structured inputs | A numeric value lacks a unit, a physical quantity that must be positive is not, a unit is outside the approved set, or a source is missing | `make check` | 004 |

### 4.2 Mechanical checks (stage 2, only after the hold is reopened)

| ID | Check | Inputs | Blocks the merge when | Planned target | Implemented by |
|---|---|---|---|---|---|
| SAN-020 | CAD parse and export | Native CAD sources and neutral exports | A file cannot be opened or exported by the approved tool, or an export is stale against its source | `make check` | Not yet assigned |
| SAN-021 | Units, coordinate system and datums | CAD and interface tables | Units differ from the approved set, the coordinate system is undefined, or a required datum from the interface control document is absent | `make check` | Not yet assigned |
| SAN-022 | BOM and drawing integrity | BOM, drawings, CAD | A BOM identifier is duplicated, a BOM line has no drawing or purchase specification, a drawing revision does not match the CAD revision, or a quantity disagrees with the assembly | `make check` | Not yet assigned |
| SAN-023 | Mass and material values | Material table, BOM, mass-properties report | A mass or density is non-positive or outside plausible bounds for its material, a material is undefined, or the BOM roll-up and mass-properties report disagree beyond the stated tolerance | `make check` | Not yet assigned |
| SAN-024 | Calculation known-answer tests | Calculation scripts or sheets and their reference cases | A calculation does not reproduce a hand-computed known answer within its stated tolerance, which shows the calculation itself is wrong before it is used on design data | `make test-unit` | Not yet assigned |
| SAN-025 | Interface datum presence | CAD and interface control document | A mounting datum, envelope or clearance named in the interface document is missing from the CAD or differs beyond tolerance | `make check` | Not yet assigned |
| SAN-026 | Revision and checksum recorded | Released CAD, drawings, BOM | A released file lacks a revision identifier or checksum in its record | `make check` | Not yet assigned |
| SAN-027 | Naming and structure conventions | `cad/`, `drawings/`, `bom/` | A file name or folder breaks the approved naming and revision convention (decided in task ROB-MECH-019) | `make check` | Not yet assigned |

## 5. What each group proves

| Group | Proves | Does not prove |
|---|---|---|
| Document and register checks | The planning files are present, parse, link and agree with one another | That a requirement is correct or a plan is sound |
| Evidence checks | A record is traceable to an immutable revision and carries a type label | That the evidence is adequate or the test was valid |
| Hold guard | That design content was not committed without a recorded reopening decision | That the decision itself was right |
| Secret and commit checks | The change meets the commit and secret policies | That the change is correct |
| Mechanical checks | The model files and tables are valid and internally consistent | That the design is strong, safe, manufacturable or fit for use |
| Known-answer tests | The calculation tool reproduces a trusted answer | That its inputs are right or the answer governs the design |

Software checks, calculations and simulation never prove physical safety, component suitability, design acceptance or readiness for human use.

## 6. Running and reporting

Today no command exists. Planned behaviour, to be implemented in task ROB-MECH-004:

| Command | Effect | Result |
|---|---|---|
| `make check` | check (read only): structure, registers, evidence, hold guard, status | exit 0 if all pass; 1 on a failure; 3 if any required check is NOT_IMPLEMENTED |
| `make docs-check` | check (read only): documents, headers, links, README, placeholders | same exit codes |
| `make test-unit` | check (read only): known-answer tests and other unit tests | same exit codes |

Every check prints its ID and one result line, then a summary that lists counts by result. The pull request records the CI run ID and the tested commit. A failure message names the file, the rule and how to fix it. Local runs and CI runs use the same commands so a result can be reproduced.

Do not run a command here that modifies repository or remote state as part of a sanity run; generators such as the status generator are run first and their output is then checked.

## 7. When a check fails

1. Fix the cause. Do not weaken the check, skip it or silence a finding.
2. If the check itself is wrong, fix the check in a separate change with its own task and reviewer, and add a regression test for the mistake.
3. If a temporary exception is unavoidable, record a structured waiver: approver, scope, rationale and expiry or review condition. A waived check is reported as WAIVED, never as PASS.
4. A check that cannot run reports NOT_IMPLEMENTED or NOT_APPLICABLE with the reason; the pull request cannot claim a clean sanity result.

## 8. Maintenance

Add a check by giving it the next SAN ID, stating its input, failure condition, planned target and implementing task, and recording the addition in [CHANGELOG.md](../planning/CHANGELOG.md). Never reuse or renumber an ID. A check that is retired stays in the catalogue marked RETIRED with its reason. When a defect escapes because a check was missing or wrong, add or correct the check and add the regression case in [REGRESSION_PLAN.md](REGRESSION_PLAN.md).
