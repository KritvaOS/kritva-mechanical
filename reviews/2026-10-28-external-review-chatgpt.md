# External Review of kritva-mechanical (ChatGPT, 2026-10-28)

| Property | Value |
|---|---|
| Document ID | KOS-MECH-REVIEW-2026-10-28 |
| Repository | `KritvaOS/kritva-mechanical` |
| Document Type | Report |
| Status | DRAFT (recorded copy of an advisory review; dispositions pending the owner) |
| Owner | Dinesh (program owner) |
| Reviewer / Approver | Reviewer: ChatGPT (external, advisory only). Dispositions: Dinesh |
| Version | 0.1.0 |
| Last Updated | 2026-10-28 |
| Authority | EVIDENCE of an external review (role, not approval). Advisory only; it decides nothing and approves nothing |
| Related Tasks / Milestones | ROB-MECH-001 to ROB-MECH-006, ROB-MECH-010, ROB-MECH-011, ROB-MECH-017; alignment batch B3 |
| Related Documents | [README.md](../README.md), [planning/TASKS.md](../planning/TASKS.md), [planning/MILESTONE.md](../planning/MILESTONE.md), [planning/CHANGELOG.md](../planning/CHANGELOG.md), [planning/REVIEW_CHECKLIST.md](../planning/REVIEW_CHECKLIST.md) |

## Purpose

This file keeps a record of the external review of this repository that the owner requested from a ChatGPT session on 2026-10-28, so its findings can be traced to decisions and tasks. It is read by the owner and reviewers deciding what to fix first.

The review is advisory. Per kritva-program practice, a review by another AI tool does not decide or approve anything, and the owner decides every disposition. The findings below are ChatGPT's, summarised in our own words. The claims it makes about GitHub (ruleset, pull request state) were not checked by the person who recorded them (see section 2).

## 1. Scope and method

| Item | Value |
|---|---|
| Reviewer | ChatGPT, in the conversation "Kritva Mechanical Planning" |
| Request | "Please do an external review of https://github.com/KritvaOS/kritva-mechanical" |
| Date | 2026-10-28 |
| Reviewed | Repository structure, planning baseline, task decomposition, verification strategy, Git governance, safety boundaries, integration with kritva-program |
| Reported inputs | The public repository, the merged planning pull request (#1), the program source manifest and the actuator program-alignment contract |
| Reviewer's own limits | Read-only; did not run the repository's tests, did not verify the live GitHub ruleset with administrative access, did not validate designs (none exist) |
| Commit reviewed | Not stated by the reviewer; to be recorded when the owner dispositions the findings |

## 2. Verification status of the claims

| Claim by the reviewer | Checked by us? | Result |
|---|---|---|
| The planning set holds 42 unique task IDs and 135 unique criterion IDs, with no duplicates and no task without criteria | Yes, by script on the authored files before the review | Agrees |
| The README states that `status/status.json`, the Makefile, governance files and workflows are missing | Yes, by reading our README | Agrees |
| Acceptance criteria sit in `planning/`, while the program standard places them at the root, and the deviation is in the changelog | Yes | Agrees |
| Pull request #1 was merged into `main` on 2026-10-28 | No | UNVERIFIED |
| Pull request #1 has no recorded GitHub review | No | UNVERIFIED |
| `main` is protected, but the branch API shows no required status checks | No | UNVERIFIED; agents cannot read GitHub rulesets or settings |
| The program `sources.json` does not list this repository | Partly (the program workstream registry shows `MECHANICAL` with no repository); the live manifest was not re-read | Plausible; UNVERIFIED |

## 3. Overall assessment (reviewer's words, summarised)

A strong initial planning repository, but not yet ready for implementation under the program's complete reporting and review controls. The ownership boundary is good: robot-level mechanical engineering here, actuator internals in the actuator repositories, governance in kritva-program. The separation of planning from CAD, BOM and physical work is good practice. The key remaining work is to make the planning contract executable and connect it to the program's governance and status pipeline without weakening any hold or safety gate.

| Area | Reviewer's rating |
|---|---|
| Planning architecture | Good foundation |
| Program integration | Incomplete |
| Automated acceptance and regression | Planned, not implemented |
| Physical-work authorisation | Must remain separately gated |

## 4. Findings

Reviewer severities are kept. The ID column keeps the reviewer's number; the ER ID is this repository's stable reference. Every disposition is OPEN until the owner decides.

| ER ID | Reviewer ID | Severity | Finding | Reviewer's required action | Where we track it | Disposition |
|---|---|---|---|---|---|---|
| ER-01 | F-01 | High | The repository, its workstream and the `ROB-MECH` prefix are not registered in kritva-program, and there is no status source or `status/status.json` | Complete the registration proposal; settle workstream mapping and prefix; implement the schema 2.0 generator and validator; add the source through a reviewed program change; add no weights and claim no progress by registering | ROB-MECH-001, 005, 006; AC-001-01 to AC-006-03 | OPEN |
| ER-02 | F-02 | High | Required governance files, workflows and Makefile gates are not implemented; the external view does not establish that CI enforcement is active | Implement the setup tasks; verify the live GitHub ruleset and required checks; an unimplemented gate must fail closed as NOT_IMPLEMENTED | ROB-MECH-002, 003, 004; AC-002-01 to AC-004-03; [GIT_COMMIT_STEP.md](../planning/GIT_COMMIT_STEP.md) section 7 | OPEN |
| ER-03 | F-03 | High | The robot-level mechanical hold must stay unambiguous: the actuator lift (D-052) must not be read as authorising robot CAD, BOM, fabrication or test, and merging planning must not reopen the workstream | Keep the gate matrix; require an explicit recorded program-owner decision before hold-controlled work; resolve how the mechanical workstream relates to the actuator workstreams so work is not double-counted | [MILESTONE.md](../planning/MILESTONE.md) section 5; README section 13; ROB-MECH-001; SAN-014 | OPEN |
| ER-04 | F-04 | Medium | `ACCEPTANCE_CRITERIA.md` is under `planning/`, but the program standard lists it at the repository root | Either move it to the root and update links, or reconcile the deviation with the program standard; do not keep two independently edited copies | Changelog entry CL-009; open item 8 in the changelog | OPEN |
| ER-05 | F-05 | Medium | Independent mechanical and safety review are required by the plan but the roles are unresolved (PD-007), and the merged planning pull request has no recorded review, so the merge is not independent engineering approval | Settle reviewer roles and the approval path; owner approval may accept the milestones as a working planning baseline but must not substitute for independent engineering or safety acceptance later | [REVIEW_CHECKLIST.md](../planning/REVIEW_CHECKLIST.md) section 17; changelog open item 4 | OPEN |
| ER-06 | F-06 | Medium | The task register is Markdown and the reporting toolchain does not exist; the generator must keep execution, review, acceptance, Git and program credit apart | Implement the generator and validator with tests for missing tasks, duplicate IDs, stale source commits, malformed evidence references, unknown status values and non-deterministic output; never edit the generated report by hand | ROB-MECH-005; AC-005-01 to AC-005-04; SAN-002, SAN-011; REG-006 | OPEN |
| ER-07 | F-07 | Medium | The sanity and regression plans need concrete commands, input formats, units, tolerances, expected outputs and failure conditions; a valid CAD file does not prove structural adequacy and a reproducible calculation does not prove its assumptions | Implement in stages: documents and links, task and criteria validation, evidence integrity, status generation; add calculation tests once inputs and reference results are reviewed; physical verification stays later and separately authorised | ROB-MECH-004; [SANITY_PLAN.md](../verification/SANITY_PLAN.md); [REGRESSION_PLAN.md](../verification/REGRESSION_PLAN.md) | OPEN |
| ER-08 | F-08 | Medium | Robot-level design could consume a preliminary actuator value without its maturity being visible | Make the interface control document the controlled source: record owning repository, exact revision, units, maturity, limits and dependent decisions for each input; a shared-interface change triggers regression for every affected variant and the embedded integration | ROB-MECH-010, 011, 017; AC-010-01, AC-010-02; REG-004, REG-005, REG-024 | OPEN |

## 5. What the reviewer recommends preserving

1. ROB-M0 to ROB-M5 as the lifecycle.
2. Stable task IDs `ROB-MECH-001` to `ROB-MECH-042`, with no renumbering to reorganise documents.
3. Separation of robot milestones from program phases P0 to P8 and actuator milestones A0 to A2.
4. Evidence tied to revisions: commit SHAs, CI run IDs, reviewer records, checksums and per-run physical test evidence.
5. Separation of planning acceptance from authorisation of CAD under the hold, purchasing, fabrication, assembly and physical tests.
6. Adjustable planning, with material changes recorded in the changelog and the frozen program baseline never silently rewritten.

## 6. Reviewer's recommended sequence

Treat the repository as the start of alignment batch B3. These are steps in the working plan, not new approved program milestones.

| Step | Action | Output |
|---|---|---|
| 1 | Resolve the program contract: workstream, prefix registration, root versus nested acceptance file, relationship to the actuator workstreams; preserve the baseline and gate records | Reviewed program registration proposal |
| 2 | Complete repository governance and CI: policy files, code ownership, commit-message check, secret scan, pull request template, Makefile gates | An enforceable repository workflow |
| 3 | Implement task and status validation: generate and validate schema 2.0 status; test malformed reports, missing evidence, invalid references and reproducibility | Reportable status and repeatable local checks |
| 4 | Start ROB-M0 engineering work: configuration, requirements, load cases, actuator input inventory, interface control document, risk register; label unverified values; do not assume the hold is lifted | A reviewed requirements package |
| 5 | Verify end-to-end program consolidation: register the source through a program pull request, check freshness and evidence, verify cited CI runs, inspect the consolidated status; keep credit and safety gates unchanged | Auditable program visibility, not automatic task credit |

The reviewer's overall recommendation is to continue with the existing 42-task plan, beginning with registration and repository controls, rather than adding another large planning document or starting CAD work.

## 7. Mapping to the existing plan

All eight findings correspond to tasks, checks or open decisions already in the planning set. No finding needs a new task today. The first four steps of the reviewer's sequence match ROB-MECH-001 to 006 and ROB-M0 (tasks 007 to 013). Items that need an owner decision before work can proceed:

| Decision | Related findings |
|---|---|
| Register the workstream, the `ROB-MECH` prefix and the `ROB-` namespace | ER-01, ER-03 |
| Decide whether and when robot mechanical work is reopened | ER-03 |
| Keep `ACCEPTANCE_CRITERIA.md` in `planning/` or move it to the root | ER-04 |
| Fill the independent mechanical and safety reviewer roles (PD-007) | ER-05 |
| Verify the live GitHub ruleset and required checks (owner action; agents cannot read them) | ER-02 |

## 8. Disposition log

Append a row when the owner decides. Do not edit earlier rows.

| Date | ER ID | Disposition (ACCEPTED, DEFERRED, REJECTED, FIXED) | Decision or commit (40 characters) | Decided by |
|---|---|---|---|---|
| | | No disposition recorded yet | | |
