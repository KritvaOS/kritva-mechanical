# Regression Plan

| Property | Value |
|---|---|
| Document ID | KOS-MECH-REGRESSION |
| Repository | `KritvaOS/kritva-mechanical` |
| Document Type | Plan |
| Status | PROPOSED (nothing in this plan is implemented yet) |
| Owner | Dinesh (program owner) |
| Reviewer / Approver | Dinesh; independent mechanical reviewer not yet identified (program decision PD-007 pending) |
| Version | 0.1.0 |
| Last Updated | 2026-10-28 |
| Authority | AUTHORITATIVE for the regression checks and change-impact rules this repository requires (role, not approval) |
| Related Tasks / Milestones | ROB-MECH-004, ROB-MECH-005 (implementation); ROB-MECH-008 to ROB-MECH-042 (consumers) |
| Related Documents | [SANITY_PLAN.md](SANITY_PLAN.md), [ACCEPTANCE_CRITERIA.md](../planning/ACCEPTANCE_CRITERIA.md), [TASKS.md](../planning/TASKS.md), [MILESTONE.md](../planning/MILESTONE.md), [README.md](../README.md); kritva-program [acceptance standard](https://github.com/KritvaOS/kritva-program/blob/main/v2/planning/ACCEPTANCE_STANDARD.md) |

## Purpose

This plan defines the checks that prove a change has not broken previously accepted requirements, interfaces, calculations or evidence, and the rules that decide which checks a given change must run. It is read by whoever writes the checks, reviews a change or decides whether a change is safe to merge.

The sanity plan asks whether a change is well formed. This plan asks whether it still agrees with what was already accepted. It does not show that the design is correct, safe or fit for use.

## 1. Current state

Nothing in this plan is implemented. The repository has no Makefile, scripts, tests or workflows, and nothing has been accepted yet, so there is no accepted baseline to regress against. Every check below is NOT_IMPLEMENTED and must be reported that way. A regression suite with no accepted baseline reports NOT_APPLICABLE with the reason, never PASS.

The checks arrive in three stages, tied to the milestones in [MILESTONE.md](../planning/MILESTONE.md):

| Stage | Applies when | Suites |
|---|---|---|
| Stage 1: planning and analysis content | From ROB-M0, once requirements, load cases, interface tables and calculations are accepted | REG-001 to REG-008 |
| Stage 2: design content | Only after an owner decision reopens robot mechanical work and CAD, BOM and drawings exist | REG-020 to REG-025 |
| Stage 3: physical evidence | Only after fabrication authority and controlled test conditions exist (ROB-M4 and ROB-M5) | REG-030 and REG-031 |

## 2. Principles

1. **Regress against accepted baselines only.** A baseline is a set of reference inputs and results that a review accepted, with the commit, tolerance and reviewer recorded. Work in progress is not a baseline.
2. **The suite must pass unchanged before and after a change to a public interface.** The regression suite is not edited in the same change that alters the interface it protects, unless the change is a recorded, approved re-baseline.
3. **A fixed defect adds a test.** Every defect found after acceptance adds a regression case that would have caught it, and the case is recorded in [CHANGELOG.md](../planning/CHANGELOG.md).
4. **Results are tied to the commit tested.** A pass on an older commit never covers a newer one.
5. **Explicit results.** Each check ends in PASS, FAIL, NOT_IMPLEMENTED or NOT_APPLICABLE. NOT_IMPLEMENTED exits with code 3 and is never counted as a pass.
6. **Impact-driven, not all-or-nothing.** A change runs the suites its change-impact row requires (section 5). A change to a shared interface, sizing input or common requirement always triggers the full set across the affected variants and the embedded integration.
7. **No silent re-baselining.** Changing a reference value, tolerance or expected result needs a recorded decision, a new baseline version and a changelog entry. The old baseline is kept.
8. **Honest scope.** Software checks, calculations and simulation never stand in for physical verification.

## 3. Baselines and tolerances

A baseline record contains:

| Field | Meaning |
|---|---|
| Baseline ID and version | Stable ID with a version that increases on re-baselining; old versions remain |
| Inputs | The stored inputs with units and sources |
| Reference results | The accepted results with units |
| Tolerance | The allowed difference for each result, with its basis |
| Tool and version | The calculation tool, script or model version that produced the result |
| Accepted at | The commit SHA (40 characters), the date, the reviewer and the evidence type |
| Source repositories | For each external input, the repository and commit it came from |

Rules: tolerances are set by the task that creates the baseline, never loosened to make a check pass, and never invented here. A result outside tolerance is a FAIL until a reviewer decides whether the change or the baseline is wrong, and that decision is recorded.

## 4. Regression suite catalogue

Each suite has an ID, what it protects, the failure that blocks the merge and the owner task. The target column names the planned Makefile target; none exists yet.

### 4.1 Stage 1: planning and analysis content

| ID | Suite | What it protects | Blocks the merge when | Target | Owner task |
|---|---|---|---|---|---|
| REG-001 | Traceability | The trace from requirements to architecture, tasks, criteria and tests | A previously traced requirement loses its link; the number of untraced requirements rises; a link points to a removed or superseded item without a decision | `make test-regression` | Not yet assigned |
| REG-002 | ID stability | Accepted task, criterion, requirement, milestone and interface IDs | An accepted ID is removed, renumbered, reused or its meaning changed against the last accepted commit | `make test-regression` | Not yet assigned |
| REG-003 | Accepted-record immutability | Completion records, accepted criteria versions, closed evidence runs and released baselines | An accepted record is edited instead of superseded by a new version | `make test-regression` | Not yet assigned |
| REG-004 | Interface version compatibility | The robot-to-actuator interface control document | An interface changes without a version bump, a breaking change lacks a MAJOR bump, a decision and a changelog entry, or an existing consumer reference is left pointing at a removed value | `make test-regression` | Not yet assigned |
| REG-005 | Upstream value consistency | The table of actuator inputs and the interface values derived from it | A value differs from the actuator repository commit it cites, a cited commit no longer exists, or a pointer advances and the resulting differences are not reviewed | `make test-regression` | Not yet assigned |
| REG-006 | Status regression | `status/status.json` against the previous report and the register | An accepted task changes state without a recorded reason, a task disappears, or this repository edits a program record (baseline, approvals, gate closures, weights) | `make test-regression` | Not yet assigned |
| REG-007 | Calculation reproducibility | Approved reference load cases and calculations | A stored baseline does not recompute from its stored inputs within its tolerance | `make test-regression` | Not yet assigned |
| REG-008 | Mass budget | The mass budget and centre-of-mass target | A segment or total mass moves beyond tolerance without a recorded decision, or margin falls below the stated minimum | `make test-regression` | Not yet assigned |

### 4.2 Stage 2: design content (after the hold is reopened)

| ID | Suite | What it protects | Blocks the merge when | Target | Owner task |
|---|---|---|---|---|---|
| REG-020 | Geometry and clearance | Interference and clearance over the full range of motion | A new interference appears, or a clearance falls below its limit, relative to the accepted reference | `make test-regression` | Not yet assigned |
| REG-021 | Mounting and interface geometry | Mounting datums, envelopes and clearances for each actuator variant | Geometry departs from the interface control document beyond tolerance for any joint | `make test-regression` | Not yet assigned |
| REG-022 | BOM, mass and drawing deltas | The released BOM, mass properties and drawings | A part is added, removed or changed, or mass properties shift beyond tolerance, without a reviewed delta report; a drawing revision no longer matches its CAD revision | `make test-regression` | Not yet assigned |
| REG-023 | Impacted calculations | Strength, stiffness, fatigue, fastener, bearing and joint calculations | An input or geometry changed and the affected calculations were not rerun, or a rerun result leaves its margin | `make test-regression` | Not yet assigned |
| REG-024 | Cross-variant impact | Every joint that uses an actuator variant whose data or interface changed | A change to an S, M, L or embedded input does not rerun the affected joints' suites and cite the result | `make test-regression` | Not yet assigned |
| REG-025 | Manufacturing and inspection consistency | The manufacturing package, inspection plan and assembly procedure | A document refers to a superseded drawing revision or a changed tolerance | `make test-regression` | Not yet assigned |

### 4.3 Stage 3: physical evidence (controlled, not automated)

| ID | Suite | What it protects | Blocks the release or milestone when | Target | Owner task |
|---|---|---|---|---|---|
| REG-030 | Critical test repeat | Requirements already verified by a physical test | A design change affects a tested requirement and the test was not repeated on the new as-built revision; an older result is used for a newer revision | Procedure, not `make` | Not yet assigned |
| REG-031 | Inspection re-check | Critical dimensions after rework or replacement | A reworked or replaced part was not re-inspected against the inspection plan | Procedure, not `make` | Not yet assigned |

Physical regression runs under the controlled procedures and safety review of ROB-M5. Evidence is stored per exact revision as described in [ACCEPTANCE_CRITERIA.md](../planning/ACCEPTANCE_CRITERIA.md) section 8.

## 5. Change-impact rules

Each change type lists the suites it must run. A change touching several rows runs the union. When unsure, run more, never fewer, and record the reasoning in the pull request.

| Change | Required suites | Also required |
|---|---|---|
| Documentation only, with no accepted record touched | Sanity set | None |
| Edit to an accepted record or accepted criteria | REG-002, REG-003 | A new version instead of an edit; changelog entry |
| Requirement added, changed or removed | REG-001, REG-002, REG-006 | Review of every architecture element, task and criterion that traces to it |
| Load case changed | REG-001, REG-007 | Rerun of every dependent calculation (REG-023 in stage 2) |
| Actuator input or upstream pointer changed (S, M, L or embedded) | REG-005, REG-004, REG-007, REG-008; REG-024 in stage 2 | Reference to the actuator repository commit and its CI run; review of the differences |
| Interface control document changed | REG-004, REG-005; REG-021 in stage 2 | MAJOR bump, decision and changelog for any breaking change |
| Architecture changed | REG-001, REG-007, REG-008 | Updated mass budget and load-path study where affected |
| CAD geometry changed | REG-020, REG-021, REG-022, REG-023 | Updated drawings and BOM where affected |
| BOM, material or mass change | REG-008, REG-022, REG-023 | Mass roll-up and procurement list check |
| Drawing or tolerance changed | REG-022, REG-025 | Inspection plan update |
| Manufacturing or assembly procedure changed | REG-025 | Hazard record review |
| As-built rework, replacement or deviation | REG-031 and REG-030 where a tested requirement is affected | Deviation register update |
| Status generator, schema use or tooling changed | REG-006 plus the full sanity set | A test that exercises the changed behaviour |
| Program standard or commit standard changed | REG-002 and the sanity set | Review of every document that cites the standard |

Cross-repository rule. A mechanical-only change does not need the embedded firmware suites of another repository. A change to a shared interface, a sizing input or a common actuator requirement does trigger regression for every affected S, M and L variant and the embedded integration. Those suites run in the actuator repositories; this repository records the commit and CI run ID of each as evidence and never reports another repository's result as its own.

## 6. Running and reporting

Today no command exists. Planned behaviour, to be implemented under task ROB-MECH-004:

| Command | Effect | Result |
|---|---|---|
| `make test-regression` | check (read only): runs the suites selected by the change-impact rules | exit 0 if all selected suites pass; 1 on a failure; 3 if any required suite is NOT_IMPLEMENTED |
| `make test` | check (read only): unit, integration and regression together | same exit codes |

A run prints each suite ID with one result line, the baseline version used and the commit tested, then a summary by result. The pull request records the CI run ID. The selection of suites is driven by the paths changed and the table above, and is printed, so a reviewer can see what ran and why.

Suites are deterministic. A flaky suite is not accepted: it is fixed, or quarantined with an owner, an issue and an expiry, and while quarantined it is reported as QUARANTINED in the summary and does not count as a pass.

Scheduled full runs of every available suite are PROPOSED once suites exist; the cadence is decided by the owner and is not a commitment.

## 7. Failure handling

1. Decide whether the change or the baseline is wrong. Do not edit both in the same change without a recorded decision.
2. Fix the change if the change is wrong.
3. If the baseline is wrong, re-baseline through a recorded decision: new baseline version, reviewer, reason and changelog entry. Keep the old baseline.
4. A temporary exception is a structured waiver (approver, scope, rationale, expiry or review condition), reported as WAIVED and never as PASS.
5. A defect that escaped adds a regression case under the right suite before the fix is closed.

## 8. What regression proves

| It proves | It does not prove |
|---|---|
| A change keeps agreeing with what was already accepted, within recorded tolerances | That the accepted baseline was right |
| Affected calculations and interfaces were rechecked after a change | That the design is safe, strong, manufacturable or fit for use |
| Evidence tied to a revision was not silently reused for another revision | That untested conditions are covered |
| Cross-repository inputs were reviewed when they changed | That the other repository's own acceptance passed |

Software checks, calculations and simulation never prove physical safety, component suitability, design acceptance or readiness for human use. Physical regression (REG-030, REG-031) is controlled work under the ROB-M5 procedures and the independent safety review.

## 9. Maintenance

Add a suite by giving it the next REG ID and stating what it protects, its blocking condition, target and owner task, and record the addition in [CHANGELOG.md](../planning/CHANGELOG.md). IDs are never reused or renumbered; a retired suite stays in the catalogue as RETIRED with its reason. Changes to the change-impact table are reviewed against the last three escaped defects, if any, to confirm the table would have caught them. Re-baselining follows section 7.
