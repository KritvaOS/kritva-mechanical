# Planning Changelog

| Property | Value |
|---|---|
| Document ID | KOS-MECH-CHANGELOG |
| Repository | `KritvaOS/kritva-mechanical` |
| Document Type | Record |
| Status | PROPOSED |
| Owner | Dinesh (program owner) |
| Reviewer / Approver | Dinesh |
| Version | 0.1.0 |
| Last Updated | 2026-10-29 |
| Authority | EVIDENCE for changes to this repository's planning baseline (role, not approval). Append only. |
| Related Tasks / Milestones | All tasks and milestones |
| Related Documents | [MILESTONE.md](MILESTONE.md), [TASKS.md](TASKS.md), [ACCEPTANCE_CRITERIA.md](ACCEPTANCE_CRITERIA.md), [REVIEW_CHECKLIST.md](REVIEW_CHECKLIST.md), [GIT_COMMIT_STEP.md](GIT_COMMIT_STEP.md), [SANITY_PLAN.md](../verification/SANITY_PLAN.md), [REGRESSION_PLAN.md](../verification/REGRESSION_PLAN.md), [README.md](../README.md) |

## Purpose

This file records material changes to the planning baseline of the robot mechanical repository, and why they were made, so that earlier baselines can always be reconstructed. It is read by reviewers and by anyone who needs to know when a milestone, task, criterion, check or rule changed.

This is the change record for the plan, not the program's change record. Nothing here changes a kritva-program baseline, approval, gate or task weight; those change only through the program's own process.

## 1. What is recorded here

| Change | Recorded |
|---|---|
| A milestone is added, split, merged, reordered, rescheduled or retired | Yes |
| A task is added, cancelled or its meaning changes | Yes |
| Acceptance criteria are added, superseded or versioned | Yes |
| A sanity or regression check is added, changed or retired, or a defect adds a regression case | Yes |
| The review checklist or commit procedure changes | Yes |
| A re-baseline of a reference value or tolerance | Yes (with the decision reference) |
| A change to the README that alters scope, ownership or the open-gate summary | Yes |
| Typo fixes and formatting with no change of meaning | No |

## 2. Rules

1. **Append only.** Add a new entry; do not edit or delete an earlier one. A correction is a new entry that refers to the old one.
2. **Newest first** within the table below, with the entry ID increasing.
3. **One entry per change** to the plan, in the same pull request as the change.
4. **Every entry names its baseline impact.** Say which program records, if any, the change touches and whether it needs the program's change process. Changes that affect frozen program records are made in kritva-program, not here.
5. **Record the reason.** The reason is the evidence or decision that prompted the change, not a restatement of the change.
6. **Reference the commit.** Once merged, add the 40-character merge commit in the commit column in a follow-up entry, not by editing the original.
7. **Never reuse an ID.** Retired milestones, tasks, criteria and checks stay in their documents marked retired, cancelled or superseded; this file records when and why.

## 3. Entry format

| Field | Meaning |
|---|---|
| ID | `CL-NNN`, increasing |
| Date | ISO date (`YYYY-MM-DD`) |
| Area | Milestone, task, criteria, sanity, regression, review, git, readme or other |
| Change | What changed |
| Reason | Why, with the decision or evidence reference |
| Baseline impact | The program records affected, or "None" |
| Commit | 40-character SHA once merged, otherwise "Pending" |
| Author and reviewer | Named people |

## 4. Change log

| ID | Date | Area | Change | Reason | Baseline impact | Commit | Author and reviewer |
|---|---|---|---|---|---|---|---|
| CL-001 | 2026-10-28 | README | Replaced the one-line stub with a full repository README: purpose and scope, ecosystem position, structure with implementation labels, open-gate summary, status-reporting and git statements | Owner asked for the planning set to be implemented in line with the kritva-program README standard | None; no program record touched | Pending | Drafted by Claude; review pending (Dinesh) |
| CL-002 | 2026-10-28 | Milestone | Added milestones ROB-M0 to ROB-M5 as working planning baselines, with entry and exit criteria, a gate and authorisation matrix, an adjustment policy and the open decisions | Owner stated on 2026-10-28 that all proposed milestones are accepted for planning and will be adjusted as work proceeds (working-session statement, not yet a program decision record) | None; milestones are planning inventory with no weight or credit and are not written into the program baseline | Pending | Drafted by Claude; review pending (Dinesh) |
| CL-003 | 2026-10-28 | Task | Added task register ROB-MECH-001 to ROB-MECH-042 across setup (alignment batch B3) and ROB-M0 to ROB-M5, with dependencies, evidence types and gates; hold-dependent tasks marked BLOCKED | Needed to plan against the accepted milestones; follows the program's one-register and stable-ID rules | None; the `ROB-MECH` prefix is PROPOSED and unregistered, so no task has program weight or credit | Pending | Drafted by Claude; review pending (Dinesh) |
| CL-004 | 2026-10-28 | Criteria | Added acceptance criteria version 0.1.0: criteria AC-001-01 to AC-042-03, milestone evidence table, test gates, specialised gates, evidence rules, definition of done, limitations and change control | Program template and acceptance standard require measurable, uniquely identified criteria per task | None; criteria grant no credit | Pending | Drafted by Claude; review pending (Dinesh) |
| CL-005 | 2026-10-28 | Sanity | Added the sanity plan: stage 1 checks SAN-001 to SAN-016 and stage 2 mechanical checks SAN-020 to SAN-027, the shared test tiers T0 to T5, reporting and failure rules | Alignment plan requires a common minimum policy specialised for mechanical work | None | Pending | Drafted by Claude; review pending (Dinesh) |
| CL-006 | 2026-10-28 | Regression | Added the regression plan: suites REG-001 to REG-008, REG-020 to REG-025 and REG-030 to REG-031, baseline and tolerance rules, the change-impact table and the cross-repository rule | Alignment plan requires regression policy, including change-impact rules covering shared interfaces and sizing inputs | None | Pending | Drafted by Claude; review pending (Dinesh) |
| CL-007 | 2026-10-28 | Review | Added the review checklist: sections for governance, documents, tasks, requirements, calculations, design, safety, physical test, evidence, status and cross-repository review, a review record, findings rules and reviewer roles | Program checklists and the hardware rules in the README standard require explicit review items, including independent and safety review | None | Pending | Drafted by Claude; review pending (Dinesh) |
| CL-008 | 2026-10-28 | Git | Added the git commit step: proposed branch rule, commit format with valid and invalid examples, required sequence, pull request, check and approval rules, prohibited actions and git-state recording | Program commit standard (D-053) and the alignment plan require a consistent, task-linked commit and pull request sequence | None; adoption of D-053 for this repository remains PROPOSED | Pending | Drafted by Claude; review pending (Dinesh) |
| CL-009 | 2026-10-28 | Layout | Placed the planning set under `planning/` and the test plans under `verification/`, including `ACCEPTANCE_CRITERIA.md` under `planning/` | Owner chose to align the folder structure with the ChatGPT planning session. The kritva-program acceptance standard section 7 places `ACCEPTANCE_CRITERIA.md` at the repository root, so this is a recorded deviation | None here; the owner may later align with the standard or record the deviation as accepted | Pending | Drafted by Claude; review pending (Dinesh) |
| CL-010 | 2026-10-28 | Git | Aligned `GIT_COMMIT_STEP.md` with the ChatGPT planning session: added `mechanical` as the default commit scope and `actuator-*` scopes for interface work, added the `test(mechanical): add frame dimensional sanity checks` example, and added the seven-stage pull request acceptance sequence (task authorisation, commit validation, scope validation, automated checks, human review, merge and evidence, submodule update) | Owner asked for the git commit format to match the ChatGPT session | None; adoption of D-053 for this repository remains PROPOSED | Pending | Drafted by Claude; review pending (Dinesh) |
| CL-011 | 2026-10-28 | Review | Added `reviews/2026-10-28-external-review-chatgpt.md`, a recorded copy of the external ChatGPT review of this repository: eight findings (ER-01 to ER-08), the claims not yet verified by us, mapping to existing tasks and checks, and an empty disposition log | Owner asked for the audit to be added to the repository so its findings are traceable | None; the review is advisory evidence, not an approval, and creates no task or program record | Pending | Drafted by Claude; review pending (Dinesh) |
| CL-012 | 2026-10-29 | Task | Added `REGISTRATION_PROPOSAL.md` for task ROB-MECH-001: proposes a child workstream `ROB_MECH` rolling up to `MECHANICAL`, the `ROB-MECH` prefix and `ROB-` namespace, the relationship to `ACT_INT`, `ACT_EMB`, `ACT_S`, `ACT_M` and `ACT_L`, the program-side changes the owner would make, eight owner decisions and an empty decision log. ROB-MECH-001 moved to IMPLEMENTED (not accepted) | Owner asked to start with the registration proposal; external review findings ER-01 and ER-03 | None; no program record is changed and the hold is unchanged. The program-side changes are listed, not made | Pending | Drafted by Claude; review pending (Dinesh) |
| CL-013 | 2026-10-29 | Task | Added the governance files for ROB-MECH-002: `AGENTS.md`, `SECURITY.md`, `CONTRIBUTING.md`, `.github/CODEOWNERS` and `.github/PULL_REQUEST_TEMPLATE.md`; README structure, security and ownership text updated. ROB-MECH-002 moved to IMPLEMENTED (not accepted). The owner confirmed the CODEOWNERS login (@dineshannayya) on 2026-10-29; the security reporting route is still a draft for the owner to confirm | Setup task ROB-MECH-002; external review finding ER-02 | None; no program record is changed. Branch protection and required checks are not verified | Pending | Drafted by Claude; review pending (Dinesh) |
| CL-014 | 2026-10-29 | Task | Added the `secret-scan` and `commit-message-check` workflows, `.gitleaks.toml` (no allowlist), a byte-for-byte copy of the program's `check_commit_format.py` with `scripts/security/PROVENANCE.md`, and unit tests for the checker; README, git, sanity and regression texts updated to say these exist as drafts with no CI run. ROB-MECH-003 moved to IMPLEMENTED (not accepted); AC-003-01 to AC-003-03 stay NOT_RUN until CI runs | Setup task ROB-MECH-003; external review finding ER-02 | None; no program record is changed. Required status checks and branch protection are not verified | Pending | Drafted by Claude; review pending (Dinesh) |
| CL-015 | 2026-10-29 | Git | Recorded that the workflows `secret-scan` and `commit-message-check` (ROB-MECH-003) were merged, and the owner's statement that both are enabled as required checks on `main`. ROB-MECH-003 stays IMPLEMENTED, not accepted: AC-003-01 to AC-003-03 need recorded CI run IDs and the seeded-secret test | Owner reported the merge and the required-check setting on 2026-10-29 | None. The required-check setting is the owner's statement, not verified here | Pending | Drafted by Claude; review pending (Dinesh) |
| CL-016 | 2026-10-29 | Task | Added the `Makefile` with the eight standard gate targets, `scripts/gate.sh` (prints `NOT_IMPLEMENTED`, exits 3) and tests in `tests/test_gates.py`; added `make help` and `make test-tools`; README command table, sanity plan section 6 and AGENTS updated. ROB-MECH-004 moved to IMPLEMENTED (not accepted). Recorded that GNU make exits 2 where the script exits 3. Added `.gitignore` for Python caches; two `__pycache__` bytecode files were committed by mistake in the ROB-MECH-003 merge and are removed from tracking here | Setup task ROB-MECH-004; external review finding ER-02 and ER-07 | None; no program record is changed. No gate is implemented, so none can pass | Pending | Drafted by Claude; review pending (Dinesh) |

## 5. Open items carried from the planning set

These are not changes; they are decisions the plan is waiting on. Each becomes a changelog entry when it is made.

1. Registration of the mechanical workstream, the `ROB-MECH` prefix and the `ROB-` namespace in kritva-program (proposal drafted in [REGISTRATION_PROPOSAL.md](REGISTRATION_PROPOSAL.md); decision pending).
2. Whether and when robot mechanical work is reopened (decision D-003 and the `MECHANICAL` workstream hold).
3. Visibility class of this repository.
4. Filling the independent mechanical reviewer and safety reviewer roles (program decision PD-007).
5. The ROB-A0 configuration and its numeric targets.
6. The CAD tool, file format, revision scheme and artifact-storage convention (task ROB-MECH-019).
7. Formal adoption of the kritva-program commit standard for this repository, and the branch naming rule.
8. Whether `ACCEPTANCE_CRITERIA.md` stays under `planning/` or moves to the repository root as the program standard states.
9. Confirm the security reporting route drafted under ROB-MECH-002, and verify the live GitHub ruleset and required checks.
10. Record the CI run IDs of the ROB-MECH-003 workflows and verify the required-check setting on `main` (the owner states it is enabled; not verified here).
11. AC-004-02 says each unimplemented target exits 3, but GNU make exits 2 for a failed recipe; the code 3 is available from `scripts/gate.sh`. Owner to accept this wording or amend the criterion.
12. Whether `RISKS_AND_DEPENDENCIES.md` and the other files in the ChatGPT target structure should be added; they are not part of the nine requested files and are not created. (`AGENTS.md` was added later under ROB-MECH-002.)

## 6. Maintenance

Add an entry in the same pull request as each change. When the baseline changes materially, for example a milestone split or a re-baseline, also record the version of the affected document so the earlier text can be found in Git history. Do not remove entries, even for plans that were abandoned: mark the abandoned item in its own document and add the entry here.
