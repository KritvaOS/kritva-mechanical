# Review Checklist

| Property | Value |
|---|---|
| Document ID | KOS-MECH-REVIEW |
| Repository | `KritvaOS/kritva-mechanical` |
| Document Type | Procedure |
| Status | PROPOSED |
| Owner | Dinesh (program owner) |
| Reviewer / Approver | Dinesh; independent mechanical and safety reviewers not yet identified (program decision PD-007 pending) |
| Version | 0.1.0 |
| Last Updated | 2026-10-28 |
| Authority | AUTHORITATIVE for how this repository's changes, tasks and milestones are reviewed (role, not approval) |
| Related Tasks / Milestones | All tasks ROB-MECH-001 to ROB-MECH-042; ROB-M0 to ROB-M5 |
| Related Documents | [TASKS.md](TASKS.md), [MILESTONE.md](MILESTONE.md), [ACCEPTANCE_CRITERIA.md](ACCEPTANCE_CRITERIA.md), [GIT_COMMIT_STEP.md](GIT_COMMIT_STEP.md), [SANITY_PLAN.md](../verification/SANITY_PLAN.md), [REGRESSION_PLAN.md](../verification/REGRESSION_PLAN.md), [README.md](../README.md) |

## Purpose

This checklist tells a reviewer what to examine before approving a pull request, a task or a milestone in this repository. It is used by the owner, by the independent mechanical reviewer and by the safety reviewer, and by contributors who want to check their own work before asking for review.

A passing automated check is not a review. The program's report-only pull request gate and the sanity and regression checks help, but they approve nothing; a human reviewer records the decision against the exact commit.

## 1. How to use it

1. Copy the review record (section 14) into the pull request or the review file. Fill in the commit reviewed (the full 40-character SHA of the pull request head) before ticking anything.
2. Work through the sections that apply (section 2 says which). Tick an item only when you have checked it yourself. Write `N/A` with a reason for an item that does not apply; never tick an item you did not check.
3. Record each problem as a finding (section 13) with a severity and a disposition.
4. Record one outcome: APPROVE, CHANGES_REQUESTED or REJECT.
5. If the pull request head changes after your review, the review is stale. It does not count, and the reviewer must look again at what changed.

## 2. Which sections apply

| Change | Sections |
|---|---|
| Any pull request | 3, 4 |
| Planning or governance documents | 3, 4, 5, 6 |
| Requirements, load cases, interface tables | 3, 4, 5, 6, 7 |
| Calculations, studies, mass budget | 3, 4, 5, 6, 8 |
| CAD, drawings, BOM (after the hold is reopened) | 3, 4, 5, 8, 9 |
| Manufacturing, procurement, inspection or assembly documents | 3, 4, 5, 9, 10 |
| Anything involving hazards, assembly or physical operation | 3, 4, 10, 11 |
| Test procedures, results and evidence | 3, 4, 11, 12 |
| Status report changes | 3, 4, 12 |
| Changes that use actuator repository data | 3, 4, 7, 13 |
| Milestone closure | 3, 4 and every section the milestone touched, plus section 15 |

## 3. Every pull request

- [ ] The change has a stated purpose and matches the task it names; scope creep is split out.
- [ ] Every commit follows the commit format with exactly one `Task:` or `Tasks:` footer, or `Tasks: None (reason)` on a docs or chore commit only.
- [ ] The named task exists in [TASKS.md](TASKS.md) and is open for work; no unrelated or invented ID is used.
- [ ] No commit message or pull request text carries an AI-session trailer or link.
- [ ] The pull request description uses the template and says what is pending.
- [ ] The required checks ran on the exact head commit and passed; no check was skipped, silenced or allowlisted to pass.
- [ ] Any check that is NOT_IMPLEMENTED is reported as such, not as a pass.
- [ ] No secrets, credentials, tokens, keys, production data or personal data are present.
- [ ] Documentation and the changelog are updated where the change needs it.
- [ ] The author did not approve their own work; the reviewer holds the role the change requires.

## 4. Governance and program alignment

- [ ] The change edits no kritva-program record (baseline, approvals, gate closures, task weights, decision log). Proposals for such changes are documents, not edits.
- [ ] Existing task IDs, requirement IDs and criteria IDs are not removed, renumbered, reused or changed in meaning.
- [ ] Actuator task IDs and frozen program IDs are untouched.
- [ ] The `ROB-` namespace and `ROB-MECH` prefix are described as PROPOSED until registered.
- [ ] Program phases P0 to P8 and the actuator A0, A1, A2 lifecycle keep their meaning and are not renamed or reinterpreted.
- [ ] Hardware version and milestone association is not added to the status file unless the approved schema allows it.
- [ ] Milestones are described as accepted for planning and adjustable, not as program baseline entries, and carry no weight or credit.
- [ ] The mechanical hold (decision D-003) is respected: no CAD, BOM, quote, procurement, fabrication, assembly or prototype content appears without a recorded owner decision reopening robot mechanical work.
- [ ] The actuator hold lift (decision D-052) is not read as covering the robot mechanical scope.
- [ ] No approval, decision, review or test result is stated that is not recorded and linked.
- [ ] Dates are absent or labelled PROPOSED.

## 5. Document quality

- [ ] The header block is present and complete (document ID, repository, type, status, owner, reviewer, version, last updated, authority, related tasks, related documents) on every human-maintained document; generated files carry their generator marker instead.
- [ ] Status is honest: nothing is APPROVED without a recorded approval, and a draft says DRAFT or PROPOSED.
- [ ] Relative links resolve and external links are marked as current links where the other record controls.
- [ ] No stale numbers (task counts, percentages, test counts, gate states) are written into documents that are not generated.
- [ ] No placeholder text, unfilled fields or unexplained abbreviations remain.
- [ ] Unknowns are labelled UNVERIFIED, PROPOSED, PLANNED or NOT YET IMPLEMENTED, not stated as fact.
- [ ] The README commands exist, match the Makefile and carry an effect label.
- [ ] The README structure check passes and a human confirmed that the content is accurate (the check proves structure only).

## 6. Task and criteria review

- [ ] The task has an ID, a deliverable, dependencies, an owner or UNASSIGNED, an evidence type and a reviewer.
- [ ] The acceptance criteria are measurable: a reviewer can state the pass or fail condition from the text alone.
- [ ] Every criterion has a unique ID and a verification method.
- [ ] Status vocabulary is used correctly: IMPLEMENTED does not imply accepted, and COMPLETE is claimed only with the review recorded.
- [ ] BLOCKED tasks name the gate that blocks them.
- [ ] Changes to criteria are new versions, not edits of criteria an accepted task was judged against.
- [ ] Dependencies are correct and the critical path is still accurate.
- [ ] A waiver, where used, is a structured record with approver, scope, rationale and expiry, and is reported as WAIVED.

## 7. Requirements and interface review

- [ ] Each requirement has an ID, a statement, units where numeric, a verification method and a traced parent.
- [ ] Each requirement is testable and unambiguous; no requirement hides a design choice.
- [ ] Every numeric target has a unit and a source.
- [ ] Interface tables state units, coordinate frames, datums, versions, tolerances and the source commit of each value.
- [ ] Placeholder, PROPOSED or unverified actuator values are labelled and none is presented as established.
- [ ] A change to an interface is a new version; a breaking change has a MAJOR bump, a recorded decision and a changelog entry.
- [ ] The counterpart repository's owner has agreed to the interface and the agreement is recorded.

## 8. Calculations, analysis and design data

- [ ] Assumptions, inputs (with units and sources), method and tool versions are stated and stored.
- [ ] The result recomputes from the stored inputs within the stated tolerance.
- [ ] Units are consistent throughout, and conversions are explicit.
- [ ] Margins are stated against the requirement and are met, or each shortfall is a recorded decision.
- [ ] At least the critical calculations were independently checked by hand or by a second method.
- [ ] Simulation results state model, mesh or discretisation, boundary conditions and validation status; a simulation is not described as physical evidence.
- [ ] The mass budget and centre-of-mass figures agree with the BOM and CAD where those exist.
- [ ] Stage 2 only: CAD opens and exports without errors, units and datums are valid, interference and clearance checks ran over the range of motion, and revision identifiers or checksums are recorded.

## 9. Design, manufacturing and procurement (after the hold is reopened)

- [ ] The owner's decision reopening robot mechanical work is cited and recorded in kritva-program.
- [ ] Every BOM line has a unique identifier and a drawing or purchase specification; quantities agree with the assembly.
- [ ] Drawings carry part ID, revision, units, tolerances, material and finish, and match the CAD revision.
- [ ] Manufacturing processes, tolerances and inspection methods are defined for each manufactured part.
- [ ] The inspection plan names instruments, accuracy against tolerance and acceptance limits for every critical dimension.
- [ ] No quote was requested, nothing was ordered and nothing was fabricated before the written authority was recorded.
- [ ] Fabrication authorisation is a separate recorded owner decision; a fabrication request is not an authorisation.

## 10. Safety review

- [ ] Hazards for the work in scope (assembly, handling, powered or loaded operation, pinch points, stored energy, mass, falls) are identified, with controls.
- [ ] A safe state and a stop procedure exist and were verified before any powered or loaded operation.
- [ ] Safety-gated functions have the required human safety review recorded against the commit.
- [ ] The open-gate summary in the README is accurate and the change respects what each open gate prohibits.
- [ ] The actuator release gates relevant to the work (A, B, C) have their state recorded; closing one input did not close a parent gate.
- [ ] No software check, calculation or simulation is used as a substitute for a required physical verification or safety approval.
- [ ] Any physical operation is limited to what an approved procedure permits.

## 11. Physical test review

- [ ] The test plan maps to every requirement whose method is B or P, with no gap.
- [ ] A controlled fixture, instruments and acceptance limits are defined before the test.
- [ ] Each run is tied to the exact as-built revision and the exact test plan version.
- [ ] A run is PASS only if its limit was met; inconclusive runs are recorded as inconclusive.
- [ ] Failures are defects with an owner and a disposition; fixed defects are re-tested as new runs.
- [ ] An older result is never used to certify a newer revision.
- [ ] Independent acceptance by the independent mechanical and safety reviewers is recorded before closure.

## 12. Evidence and status reporting

- [ ] Evidence points to immutable references: 40-character commit SHAs, CI run IDs, review records and checksums; no branch names.
- [ ] Every result carries an evidence type (S, C, Sim, B, P or R) and the scope it covers.
- [ ] Run records follow the manifest, environment, log, summary and artifacts layout and are append-only.
- [ ] `status/status.json` validates against schema 2.0, `source.commit` is the full SHA of the commit it was generated from, and its task IDs match the register exactly.
- [ ] The status report states facts only: no approval, acceptance or program credit is claimed.
- [ ] Execution, evidence, acceptance and release readiness are kept apart and not merged into one flag or percentage.
- [ ] A reported completion is not described as accepted progress.

## 13. Cross-repository review

- [ ] Every value taken from an actuator or other repository cites its repository and commit.
- [ ] When an upstream pointer advanced, the differences were reviewed and the affected suites run, and the other repository's CI run is cited.
- [ ] Another repository's result is never reported as this repository's evidence.
- [ ] Parent and child gate statements are described as summaries of the child's contribution, not as the gate authority.

## 14. Review record

Copy this block into the pull request or review file.

```text
Repository: KritvaOS/kritva-mechanical
Pull request or milestone: 
Task IDs: 
Commit reviewed (40 characters): 
Reviewer: 
Role (owner / independent mechanical / safety): 
Date (YYYY-MM-DD): 
Sections completed: 
Checks run and CI run IDs: 
Findings (IDs): 
Outcome (APPROVE / CHANGES_REQUESTED / REJECT): 
Conditions or follow-ups: 
```

## 15. Milestone closure review

In addition to the sections above, before a completion record is approved:

- [ ] Every exit criterion in [MILESTONE.md](MILESTONE.md) for this milestone has a disposition: PASS, WAIVED with approval reference or NOT_APPLICABLE with approval reference.
- [ ] Every task in the milestone is at PASS, deferred by a recorded decision or cancelled with a reason.
- [ ] The completion record follows the program template and cites 40-character SHAs, test runs, the disposition of each criterion, deferred work with its decision, approvals and immutable evidence.
- [ ] Approvals are by the owner and the independent reviewers the milestone requires, recorded against the closing commit.
- [ ] Open findings and deviations have an owner and a disposition; no blocking item was converted into a pass.
- [ ] The completion record states what closing the milestone does not do: it grants no program credit and authorises no later work.
- [ ] A merge, a passing run or a tag is not offered as the closing evidence.

## 16. Findings

Record each finding in the review.

| Field | Meaning |
|---|---|
| ID | `F-NNN` within the review |
| Severity | BLOCKER (must fix before merge or closure), MAJOR (fix before closure or defer by decision), MINOR (fix or accept), NOTE (informational) |
| Location | File and line, task or criterion ID |
| Finding | What is wrong and why it matters |
| Disposition | OPEN, FIXED (with commit), DEFERRED (with decision), ACCEPTED (with approver), REJECTED (with reason) |
| Owner | A named person |

An open BLOCKER prevents APPROVE. A DEFERRED or ACCEPTED finding needs a recorded decision and is never reported as fixed.

## 17. Reviewer roles and independence

| Role | Who | Required for |
|---|---|---|
| Owner | Dinesh | All pull requests under the program's ruleset; fabrication authority; hold decisions |
| Independent mechanical reviewer | Not yet identified (PD-007 pending) | Requirements, interfaces, calculations, design, manufacturing and test results; milestone closure |
| Safety reviewer | Not yet identified (PD-007 pending) | Hazards, assembly, powered or loaded operation, physical test, safety-gated functions |
| Actuator repository owners | Per repository | Agreement to interfaces and use of actuator data |

A reviewer must be different from the author of the change under review. With a single owner who also authors a pull request, GitHub does not count the author's own approval; the owner then asks for a second reviewer or uses the owner's merge bypass, as the program records. That is an owner decision, not a self-approval, and is noted in the review record. A criterion that needs an independent reviewer cannot reach PASS until that role is filled.

## 18. Maintenance

Add or change a checklist item by a pull request that names the reason, for example a defect that escaped review, and records it in [CHANGELOG.md](CHANGELOG.md). Never delete an item that an accepted review relied on; retire it with the version and reason. Review records already made stay as written.
