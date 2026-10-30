# Acceptance Criteria: kritva-mechanical

| Property | Value |
|---|---|
| Document ID | KOS-MECH-AC |
| Repository | `KritvaOS/kritva-mechanical` |
| Document Type | Specification |
| Status | PROPOSED (criteria version 0.1.1; version 0.1.0 was accepted as a working planning baseline on 2026-10-28, the 0.1.1 additions for tasks 043 to 052 are PROPOSED and not yet accepted; not an approved program acceptance record) |
| Owner | Dinesh (program owner) |
| Reviewer / Approver | Dinesh; independent mechanical reviewer not yet identified (program decision PD-007 pending) |
| Version | 0.1.1 |
| Last Updated | 2026-10-30 |
| Authority | AUTHORITATIVE for this repository's acceptance criteria (role, not approval). Criteria never grant program credit. |
| Related Tasks / Milestones | ROB-MECH-001 to ROB-MECH-052; ROB-M0 to ROB-M5 |
| Related Documents | [TASKS.md](TASKS.md), [MILESTONE.md](MILESTONE.md), [SANITY_PLAN.md](../verification/SANITY_PLAN.md), [REGRESSION_PLAN.md](../verification/REGRESSION_PLAN.md), [REVIEW_CHECKLIST.md](REVIEW_CHECKLIST.md); kritva-program [acceptance standard](https://github.com/KritvaOS/kritva-program/blob/main/v2/planning/ACCEPTANCE_STANDARD.md) and [criteria template](https://github.com/KritvaOS/kritva-program/blob/main/v2/planning/templates/ACCEPTANCE_CRITERIA.template.md) |

## Purpose

This document states, in objective and uniquely identified form, what evidence makes each task and milestone in this repository acceptable. Reviewers use it to decide, contributors use it to know what to deliver, and the status generator uses its IDs to link evidence to tasks.

A criterion that cannot be tested yet is listed in section 10, not invented. Every result column starts at NOT_RUN. Nothing here is a claim that any criterion has passed.

## 1. Purpose and scope

The repository owns the mechanical design, planning and verification of the complete Kritva robot above the actuator level (see the [README](../README.md) section 1). These criteria cover the setup tasks (alignment batch B3), milestones ROB-M0 to ROB-M5 and their tasks.

Excluded: actuator internals and their acceptance (owned by the actuator repositories), electronics, firmware, software, and program-level acceptance, task weights and credit (owned by kritva-program).

## 2. Normative dependencies

| Dependency | Version or pin | Note |
|---|---|---|
| kritva-program acceptance standard | `v2/planning/ACCEPTANCE_STANDARD.md`, status PROPOSED; commit pin to be recorded when the owner approves the standard | Where it differs from the pinned engineering contract (D-023), the contract wins |
| kritva-program commit standard | D-053; checker `scripts/security/check_commit_format.py` | Adoption for this repository is PROPOSED |
| kritva-program status contract | Schema 2.0 | No hardware-version or phase fields unless the schema allows them |
| Actuator repositories | Commit SHAs pinned in the interface control document when it is written (task ROB-MECH-011) | Values may be PROPOSED or placeholder and are labelled |
| `ROB-MECH` prefix and `ROB-` namespace | PROPOSED | Registration is task ROB-MECH-001 |

## 3. Functional criteria

Evidence types: S software check, C calculation, Sim simulation, B bench measurement, P independently accepted physical test, R review record. Every R requires a reviewer, a date and the commit reviewed. Result values: NOT_RUN, PASS, FAIL, WAIVED (structured approval record; never reported as PASS).

### 3.1 Setup

| ID | Criterion (testable) | Verified by | Result |
|---|---|---|---|
| AC-001-01 | The proposal names the workstream ID, the `ROB-MECH` prefix, the `ROB-` namespace and how they relate to `MECHANICAL` and `ACT_INT`, `ACT_EMB`, `ACT_S`, `ACT_M`, `ACT_L` | R | NOT_RUN |
| AC-001-02 | The proposal states that it changes no baseline, task weight, approval or gate record and adds no unrecognised status fields | R | NOT_RUN |
| AC-001-03 | The owner's decision on the proposal is recorded with a reference | R | NOT_RUN |
| AC-002-01 | `AGENTS.md`, `SECURITY.md`, `CONTRIBUTING.md`, `.github/CODEOWNERS` and `.github/PULL_REQUEST_TEMPLATE.md` exist and each is linked from the README | S (README check and link check) | NOT_RUN |
| AC-002-02 | `AGENTS.md` states authority, what agents must not change without an owner decision, validation steps and commit rules consistent with D-053 | R | NOT_RUN |
| AC-002-03 | `SECURITY.md` gives a reporting route and contains no vulnerability details, secrets or personal data | R, S (secret scan) | NOT_RUN |
| AC-002-04 | `CODEOWNERS` names the owner and covers every path | S (pattern check), R | NOT_RUN |
| AC-003-01 | `secret-scan` and `commit-message-check` run on every push and pull request | S (CI run IDs) | NOT_RUN |
| AC-003-02 | A seeded fake secret on a test branch makes `secret-scan` fail; the test branch is not merged | S (CI run ID) | NOT_RUN |
| AC-003-03 | `commit-message-check` rejects a message with no `Task:` footer and accepts a valid one | S (CI run IDs) | NOT_RUN |
| AC-003-04 | No allowlist entry is added to silence a scan | R | NOT_RUN |
| AC-004-01 | The Makefile defines `check`, `lint`, `test-unit`, `test-integration`, `test-regression`, `test`, `docs-check` and `acceptance` | S | NOT_RUN |
| AC-004-02 | Each unimplemented target prints `NOT_IMPLEMENTED` and exits with code 3 (verified by running it) | S | NOT_RUN |
| AC-004-03 | The command table in the README matches the Makefile exactly | S, R | NOT_RUN |
| AC-005-01 | `status/status.json` validates against schema 2.0 with the program validator | S | NOT_RUN |
| AC-005-02 | `source.commit` is the full 40-character SHA of the commit the report was generated from | S | NOT_RUN |
| AC-005-03 | Every task ID in the report exists in `TASKS.md` and every registered task appears in the report | S | NOT_RUN |
| AC-005-04 | Regenerating from the same inputs gives byte-identical output | S | NOT_RUN |
| AC-006-01 | The program pull request adding the source is merged by the program's approved process | R, CI run ID | NOT_RUN |
| AC-006-02 | The program's consolidation check passes with the source present | S (program command output) | NOT_RUN |
| AC-006-03 | The workstream no longer shows as UNVERIFIED for lack of a source, and no baseline record was edited | S, R | NOT_RUN |

### 3.2 ROB-M0 Requirements baseline

| ID | Criterion (testable) | Verified by | Result |
|---|---|---|---|
| AC-007-01 | The configuration document states segments, degrees of freedom per joint and intended use | R | NOT_RUN |
| AC-007-02 | Every numeric target has a unit and a source; none is copied from another repository without a citation | R | NOT_RUN |
| AC-007-03 | The owner's confirmation of the ROB-A0 intent is recorded | R | NOT_RUN |
| AC-008-01 | Every requirement has a unique ID, a statement, a unit where numeric, a verification method (C, Sim, B or P) and a traced parent | S (schema or script check), R | NOT_RUN |
| AC-008-02 | A reviewer can state the pass or fail condition of every requirement from its text alone | R | NOT_RUN |
| AC-008-03 | All trace links resolve and no ID is duplicated | S | NOT_RUN |
| AC-009-01 | Every load case has an ID, description, inputs with units, a source and a result check | S, R | NOT_RUN |
| AC-009-02 | Standing, walking and payload-lift cases exist; the decision on impact and fall cases is recorded either way | R | NOT_RUN |
| AC-009-03 | At least one case has a hand-calculated known answer that the stored inputs reproduce within the stated tolerance | C | NOT_RUN |
| AC-010-01 | The table gives, for each actuator variant and the embedded board, each value with unit, source repository, commit SHA and a maturity label (ESTABLISHED, PROPOSED, PLACEHOLDER or UNVERIFIED) | R | NOT_RUN |
| AC-010-02 | No placeholder or unverified value appears without its label | R, S (label check) | NOT_RUN |
| AC-010-03 | Gaps are listed with the repository that owns each | R | NOT_RUN |
| AC-011-01 | For every joint: actuator variant, mounting datum, envelope, mass, torque limit and speed limit, each with a source | R | NOT_RUN |
| AC-011-02 | The document has a version and a change history | S | NOT_RUN |
| AC-011-03 | Each value traces to a requirement or an actuator source | R | NOT_RUN |
| AC-011-04 | Open items are listed with an owner | R | NOT_RUN |
| AC-012-01 | Each risk has an ID, description, the likelihood and impact scale in use, an owner and a response | R | NOT_RUN |
| AC-012-02 | Each dependency names its owner and the milestone that needs it | R | NOT_RUN |
| AC-012-03 | The mechanical hold and actuator input maturity appear as risks | R | NOT_RUN |
| AC-013-01 | The completion record follows the program template and cites 40-character SHAs | S, R | NOT_RUN |
| AC-013-02 | Every ROB-M0 milestone criterion (section 4) has a disposition: PASS, WAIVED with approval reference or NOT_APPLICABLE with approval reference | R | NOT_RUN |
| AC-013-03 | Approvals by the owner and an independent reviewer are recorded against the closing commit | R | NOT_RUN |
| AC-013-04 | Deferred work is listed with the deferring decision | R | NOT_RUN |

### 3.3 ROB-M1 Architecture

| ID | Criterion (testable) | Verified by | Result |
|---|---|---|---|
| AC-014-01 | The architecture identifies segments, joints, joint axes and load paths | R | NOT_RUN |
| AC-014-02 | Every ROB-M0 requirement maps to an architectural element or to a recorded deferral decision | S (trace check), R | NOT_RUN |
| AC-014-03 | Options considered and the reason for the choice are recorded | R | NOT_RUN |
| AC-015-01 | Assumptions are stated and inputs are stored with the study | R | NOT_RUN |
| AC-015-02 | Results recompute from the stored inputs within the stated tolerance | C, S | NOT_RUN |
| AC-015-03 | Results are compared to the requirements, with each shortfall recorded | C, R | NOT_RUN |
| AC-016-01 | Mass per segment has a source and an uncertainty | C, R | NOT_RUN |
| AC-016-02 | The total is within the ROB-M0 target with stated margin, or the shortfall is a recorded decision | C, R | NOT_RUN |
| AC-016-03 | The centre-of-mass target is stated and recomputable from stored inputs | C, S | NOT_RUN |
| AC-017-01 | Each interface has a version | S | NOT_RUN |
| AC-017-02 | Each interface cites the commit of its actuator repository source | S, R | NOT_RUN |
| AC-017-03 | The counterpart owner's agreement is recorded in a review or pull request | R | NOT_RUN |
| AC-018-01 | Each envelope has dimensions, units and datums | R | NOT_RUN |
| AC-018-02 | Envelopes do not conflict with the architecture (a check is run once CAD exists) | S, R | NOT_RUN |
| AC-018-03 | The document says envelopes reserve space and are not the electrical design | R | NOT_RUN |
| AC-019-01 | The proposal compares options against stated criteria: tool and version, license terms, binary storage method, revision scheme and neutral export format | R | NOT_RUN |
| AC-019-02 | The owner's decision is recorded | R | NOT_RUN |
| AC-020-01 | The skeleton opens and exports in the approved tool without errors | S | NOT_RUN |
| AC-020-02 | Units, coordinate system and required datums are valid | S | NOT_RUN |
| AC-020-03 | Geometry matches the interface documents within the stated tolerance | S, R | NOT_RUN |
| AC-020-04 | A revision identifier or checksum is recorded and the decision reopening robot mechanical work is cited | S, R | NOT_RUN |
| AC-021-01 | The completion record follows the program template and cites 40-character SHAs | S, R | NOT_RUN |
| AC-021-02 | Each ROB-M1 milestone criterion has a disposition; task 020 may be deferred only by recorded decision | R | NOT_RUN |
| AC-021-03 | Approvals by the owner and an independent mechanical reviewer are recorded against the closing commit | R | NOT_RUN |

### 3.4 ROB-M2 Detailed design

All criteria in this group are blocked by the mechanical hold.

| ID | Criterion (testable) | Verified by | Result |
|---|---|---|---|
| AC-022-01 | Every part and assembly in the BOM exists in the CAD | S | NOT_RUN |
| AC-022-02 | Units and material properties are consistent across the assembly | S | NOT_RUN |
| AC-022-03 | Each file carries a revision identifier or checksum recorded in the review | S, R | NOT_RUN |
| AC-022-04 | The assembly opens and exports with no errors | S | NOT_RUN |
| AC-023-01 | Each drawing carries part ID, revision, units, tolerances, material and finish | R | NOT_RUN |
| AC-023-02 | Each drawing matches the CAD revision it was released from | S, R | NOT_RUN |
| AC-023-03 | Critical dimensions are flagged for inspection | R | NOT_RUN |
| AC-024-01 | Every BOM line has a unique identifier | S | NOT_RUN |
| AC-024-02 | Every line links to a drawing or a purchase specification | S | NOT_RUN |
| AC-024-03 | Quantities agree with the assembly | S | NOT_RUN |
| AC-024-04 | The mass roll-up agrees with the mass-properties report within the stated tolerance | S, C | NOT_RUN |
| AC-025-01 | Every ROB-M0 load case has a calculation | R | NOT_RUN |
| AC-025-02 | Margins are stated and met, or each deviation is a recorded decision | C, R | NOT_RUN |
| AC-025-03 | Inputs trace to requirements and actuator data; results recompute from stored inputs within the stated tolerance | C, S | NOT_RUN |
| AC-025-04 | Each critical calculation is independently checked by hand or by a second method | C, R | NOT_RUN |
| AC-026-01 | Mass properties are within budget or the deviation is a recorded decision | C, R | NOT_RUN |
| AC-026-02 | The interference check ran and has zero unresolved failures | S, Sim | NOT_RUN |
| AC-026-03 | Clearances over the full range of motion are reported | Sim, R | NOT_RUN |
| AC-027-01 | The completion record follows the program template and cites 40-character SHAs | S, R | NOT_RUN |
| AC-027-02 | A design review was held; findings are closed or deferred by decision; reviewer and revision are recorded | R | NOT_RUN |
| AC-027-03 | Approvals by the owner and an independent mechanical reviewer, and the safety reviewer where safety-gated functions are touched | R | NOT_RUN |

### 3.5 ROB-M3 Fabrication readiness

All criteria in this group are blocked by the mechanical hold and procurement authority.

| ID | Criterion (testable) | Verified by | Result |
|---|---|---|---|
| AC-028-01 | Each manufactured part has a process, tolerance, material specification and inspection method | R | NOT_RUN |
| AC-028-02 | The package matches the released drawing revisions | S, R | NOT_RUN |
| AC-028-03 | Manufacturability findings are closed or deferred by decision | R | NOT_RUN |
| AC-029-01 | Each purchased part has a source or alternatives, a lead-time estimate and a dated cost estimate | R | NOT_RUN |
| AC-029-02 | No quote was requested before the written authority was recorded | R | NOT_RUN |
| AC-029-03 | Totals agree with the BOM | S | NOT_RUN |
| AC-030-01 | Each critical dimension has an instrument, an accuracy and acceptance limits | R | NOT_RUN |
| AC-030-02 | Each instrument is identified with its calibration requirement | R | NOT_RUN |
| AC-030-03 | Instrument accuracy is stated against tolerance, with the ratio used | C, R | NOT_RUN |
| AC-031-01 | Steps are ordered and specify tools, fasteners and torques | R | NOT_RUN |
| AC-031-02 | Hazards and controls are recorded | R | NOT_RUN |
| AC-031-03 | The procedure is consistent with the actuator mounting contracts | R | NOT_RUN |
| AC-032-01 | The request states scope, cost, schedule, risks, open gates and supporting evidence | R | NOT_RUN |
| AC-032-02 | The request states that it does not itself authorise fabrication | R | NOT_RUN |
| AC-032-03 | The owner's decision is recorded separately in kritva-program | R | NOT_RUN |
| AC-033-01 | The completion record follows the program template and cites 40-character SHAs | S, R | NOT_RUN |
| AC-033-02 | Each ROB-M3 milestone criterion has a disposition | R | NOT_RUN |
| AC-033-03 | Approvals by the owner (including fabrication authority) and independent reviewers, and the safety reviewer for assembly hazards | R | NOT_RUN |

### 3.6 ROB-M4 Assembly and inspection

All criteria in this group are blocked by fabrication authority and open safety gates.

| ID | Criterion (testable) | Verified by | Result |
|---|---|---|---|
| AC-034-01 | Each received part was inspected against the inspection plan; the record has the instrument ID and its calibration date | B, R | NOT_RUN |
| AC-034-02 | Non-conforming parts are quarantined and logged | R | NOT_RUN |
| AC-035-01 | Assembly followed the approved procedure and deviations are logged | B, R | NOT_RUN |
| AC-035-02 | The assembly record has dates and personnel | R | NOT_RUN |
| AC-035-03 | No powered or loaded operation took place beyond what the approved procedure permits | R | NOT_RUN |
| AC-036-01 | Every difference between the as-built and the released revision is listed | B, R | NOT_RUN |
| AC-036-02 | Each deviation has an owner and a disposition | R | NOT_RUN |
| AC-036-03 | The record was reviewed independently | R | NOT_RUN |
| AC-037-01 | Mounting fit for each actuator is measured against the interface control document and recorded | B | NOT_RUN |
| AC-037-02 | The state of the relevant actuator gates is recorded | R | NOT_RUN |
| AC-037-03 | Clearances are checked over the range of motion the procedure permits | B, R | NOT_RUN |
| AC-038-01 | The completion record follows the program template and cites 40-character SHAs | S, R | NOT_RUN |
| AC-038-02 | Each ROB-M4 milestone criterion has a disposition; no open deviation lacks an owner and a disposition | R | NOT_RUN |
| AC-038-03 | Approvals by the owner and independent reviewers, and the safety reviewer where hazards were identified | R | NOT_RUN |

### 3.7 ROB-M5 Mechanical verification

All criteria in this group are blocked by the controlled fixture, an approved test plan and independent safety review.

| ID | Criterion (testable) | Verified by | Result |
|---|---|---|---|
| AC-039-01 | A procedure exists for every requirement whose method is B or P, and the plan maps to the requirements with no gap | S (trace check), R | NOT_RUN |
| AC-039-02 | The fixture definition includes a safe state and a stop procedure that were verified | B, R | NOT_RUN |
| AC-039-03 | The safety review of the plan is recorded | R | NOT_RUN |
| AC-039-04 | Instruments and acceptance limits are stated for every test | R | NOT_RUN |
| AC-040-01 | Each run has a manifest (task ID, source commit and as-built revision, test plan version, tool version, configuration, result, timestamp, artifact checksums), an environment record, a command or step log and a summary | S, R | NOT_RUN |
| AC-040-02 | Each result names the exact tested revision | S | NOT_RUN |
| AC-040-03 | A run is PASS only if its limit is met; an inconclusive run is recorded as inconclusive | R | NOT_RUN |
| AC-040-04 | Run records are immutable once reviewed; a rerun is a new run | S, R | NOT_RUN |
| AC-041-01 | Each failure has a defect with an owner and a disposition | R | NOT_RUN |
| AC-041-02 | Evidence for a fixed defect is a new run, not an edit of the old one | S, R | NOT_RUN |
| AC-041-03 | No blocking defect is open at closure; any exception is a structured waiver | R | NOT_RUN |
| AC-042-01 | Independent acceptance is recorded by the independent mechanical and safety reviewers | R | NOT_RUN |
| AC-042-02 | Every requirement with a physical method has a recorded result | S, R | NOT_RUN |
| AC-042-03 | The completion record is approved; it states that it does not release the hardware | R | NOT_RUN |

### 3.8 Feasibility study (paper only, PROPOSED in version 0.1.1)

These criteria cover tasks 043 to 052. They use evidence types C and R (and S for file and link checks) only; simulation, bench and physical evidence are not part of this study and are never claimed from it.

| ID | Criterion (testable) | Verified by | Result |
|---|---|---|---|
| AC-043-01 | Every file listed in the study README index exists and every local link in the `feasibility/` Markdown files resolves | S | NOT_RUN |
| AC-043-02 | Every `feasibility/` document states status PROPOSED and states that mechanical hold D-003 remains in effect; no `cad/`, BOM, quote or procurement artefact exists in the folder | S, R | NOT_RUN |
| AC-043-03 | No document gives a numeric value for payload, reach, mass, torque, speed or cost without a source, or labels it ESTIMATE, TBD or UNKNOWN | R | NOT_RUN |
| AC-043-04 | The owner review is recorded against the exact commit | R | NOT_RUN |
| AC-044-01 | Each of the four INTERN-01 concepts has the documents required by `feasibility/DESIGN_GUIDELINES.md` section 4, or each missing item is marked BLOCKED or INCOMPLETE with a reason | S, R | NOT_RUN |
| AC-044-02 | Every joint torque and speed requirement shows formula, inputs, units and assumptions, or is marked TBD | C, R | NOT_RUN |
| AC-044-03 | S/M/L compatibility is derived per joint and is not copied from the elbow reference | R | NOT_RUN |
| AC-044-04 | Every numeric value is labelled sourced, ESTIMATE or UNKNOWN, and the evidence type is stated as C; no simulation, bench or physical evidence is claimed | R | NOT_RUN |
| AC-045-01 | Each of the four INTERN-02 concepts has the documents required by `feasibility/DESIGN_GUIDELINES.md` section 4, or each missing item is marked BLOCKED or INCOMPLETE with a reason | S, R | NOT_RUN |
| AC-045-02 | Every joint torque and speed requirement shows formula, inputs, units and assumptions, or is marked TBD | C, R | NOT_RUN |
| AC-045-03 | S/M/L compatibility is derived per joint and is not copied from the elbow reference | R | NOT_RUN |
| AC-045-04 | Every numeric value is labelled sourced, ESTIMATE or UNKNOWN, and the evidence type is stated as C; no simulation, bench or physical evidence is claimed | R | NOT_RUN |
| AC-046-01 | Each of the four INTERN-03 concepts has the documents required by `feasibility/DESIGN_GUIDELINES.md` section 4, or each missing item is marked BLOCKED or INCOMPLETE with a reason | S, R | NOT_RUN |
| AC-046-02 | Every joint torque and speed requirement shows formula, inputs, units and assumptions, or is marked TBD | C, R | NOT_RUN |
| AC-046-03 | S/M/L compatibility is derived per joint and is not copied from the elbow reference | R | NOT_RUN |
| AC-046-04 | Every numeric value is labelled sourced, ESTIMATE or UNKNOWN, and the evidence type is stated as C; no simulation, bench or physical evidence is claimed | R | NOT_RUN |
| AC-047-01 | Criteria CP2-01 to CP2-09 each have a result (PASS, FAIL, BLOCKED or NOT REVIEWED) with evidence | R | NOT_RUN |
| AC-047-02 | All 12 concepts appear with a status; none is omitted silently | R | NOT_RUN |
| AC-047-03 | The review record cites the 40-character reviewed commit | S, R | NOT_RUN |
| AC-048-01 | Criteria CP3-01 to CP3-11 each have a result with evidence | R | NOT_RUN |
| AC-048-02 | All 12 concepts appear with a status and the cross-intern consistency of calculations is reviewed | R | NOT_RUN |
| AC-048-03 | The review record cites the 40-character reviewed commit | S, R | NOT_RUN |
| AC-049-01 | Criteria CP4-01 to CP4-12 each have a result with evidence | R | NOT_RUN |
| AC-049-02 | Hard gates HG-01 to HG-04 are recorded separately from weighted scores; an unresolved gate is not shown as passed | R | NOT_RUN |
| AC-049-03 | Outstanding owner decisions are listed and the record states that a PASS does not authorise implementation | R | NOT_RUN |
| AC-050-01 | Every scorecard shows all seven criteria; a criterion with UNKNOWN evidence is NOT SCORED, weights are not renormalised, and scored and unscored weight are reported | R | NOT_RUN |
| AC-050-02 | A weight sensitivity check is recorded and the proposed weights were not changed after scoring | C, R | NOT_RUN |
| AC-050-03 | Cost values are labelled ESTIMATE or UNKNOWN, are compared with the planning ceiling only as estimates, and no quotation is represented | R | NOT_RUN |
| AC-051-01 | The recommendation names two dual-arm and two legged candidates, or documents the shortfall | R | NOT_RUN |
| AC-051-02 | It states evidence limits, unresolved hard gates and NOT SCORED criteria, and states that it does not authorise CAD, BOM, quotes, procurement, fabrication or physical testing | R | NOT_RUN |
| AC-052-01 | The decision record states the decision, date, decider and the evidence reviewed | R | NOT_RUN |
| AC-052-02 | CAD and BOM tasks stay BLOCKED unless the record explicitly reopens robot mechanical work and the matching decision is recorded in kritva-program | R | NOT_RUN |

## 4. Milestone acceptance criteria

A milestone closes only through an approved completion record. The exit criteria themselves are in [MILESTONE.md](MILESTONE.md); this table sets the evidence required. Tasks 043 to 052 are not part of any milestone's required evidence unless the owner decides so (see MILESTONE.md open decision 8).

| Milestone | Required evidence | Result |
|---|---|---|
| ROB-M0 | Tasks 007 to 012 each at PASS; completion record (task 013) with owner and independent approvals | NOT_RUN |
| ROB-M1 | Tasks 014 to 019 at PASS; task 020 at PASS or deferred by decision; completion record (task 021) | NOT_RUN |
| ROB-M2 | Tasks 022 to 026 at PASS; design review recorded; completion record (task 027) | NOT_RUN |
| ROB-M3 | Tasks 028 to 031 at PASS; request (task 032) delivered; completion record (task 033); fabrication decision recorded separately | NOT_RUN |
| ROB-M4 | Tasks 034 to 037 at PASS; completion record (task 038) | NOT_RUN |
| ROB-M5 | Tasks 039 to 041 at PASS; independent acceptance and completion record (task 042) | NOT_RUN |

## 5. Interface and compatibility

A robot-to-actuator interface is valid only if it states units, coordinate frames and datums, versions, tolerances and the source revision of every value, and says which values are PROPOSED or placeholder. A change to an interface is a new version, never an edit of an accepted version. A breaking change needs a MAJOR version, a changelog entry and a recorded decision, and triggers the regression checks in [REGRESSION_PLAN.md](../verification/REGRESSION_PLAN.md). A change in an actuator repository's value is picked up only when the interface cites the new commit.

## 6. Test gates

| Gate | Command | Required result | Today |
|---|---|---|---|
| Structure and planning files | `make check` | all pass | NOT_IMPLEMENTED (no Makefile; task 004) |
| Static checks | `make lint` | all pass | NOT_IMPLEMENTED |
| Unit | `make test-unit` | all pass | NOT_IMPLEMENTED |
| Integration | `make test-integration` | all pass | NOT_IMPLEMENTED |
| Regression | `make test-regression` | all pass, unchanged suite | NOT_IMPLEMENTED |
| Combined | `make test` | all pass | NOT_IMPLEMENTED |
| Documentation | `make docs-check` | links and generated documents current | NOT_IMPLEMENTED |
| Acceptance | `make acceptance` | all automatable criteria pass | NOT_IMPLEMENTED |

An unimplemented gate exits non-zero and is never counted as a pass. A gate is NOT_APPLICABLE only through a structured, approved disposition. The tests behind each gate are planned in [SANITY_PLAN.md](../verification/SANITY_PLAN.md) and [REGRESSION_PLAN.md](../verification/REGRESSION_PLAN.md).

## 7. Specialised gates

| Gate | Applies to | Requirement |
|---|---|---|
| Calculation reproducibility | Tasks 009, 015, 016, 025, 026, 044 to 046, 048, 050 | Inputs are stored with the result and the result recomputes within the stated tolerance |
| Dimensional inspection | Tasks 030, 034, 036 | Instruments are identified and calibrated; accuracy is stated against tolerance |
| Mass and balance | Tasks 016, 024, 026 | Mass roll-ups agree across BOM, CAD and the budget within the stated tolerance |
| Physical test | Tasks 039 to 042 | Controlled procedure and fixture, evidence per exact revision, independent acceptance |
| Safety review | Any task touching a safety-gated function, and M3 to M5 | Recorded against the commit; required human reviews are never replaced by software checks |
| Paper-only study | Tasks 043 to 052 | No CAD, BOM, quote, procurement, fabrication or physical test is produced; evidence is C and R only |
| Hold and authorisation | Tasks 020 to 042 | The matching decision is recorded in kritva-program before the task starts |

Software checks, calculations and simulation never stand in for physical verification, and a physical-test criterion is never marked PASS from them.

## 8. Evidence requirements

- Evidence points to immutable references: commit SHAs (40 characters), CI run IDs, review records and checksums. A branch name or an unversioned path is not evidence.
- Every PASS names the exact revision tested. A result from an older commit does not certify a newer design.
- Evidence type (S, C, Sim, B, P, R) is stated beside every result.
- Test and inspection evidence for physical work is stored as `results/ROB-MECH-NNN/RUN-ID/` containing `manifest.json`, `environment.json`, `command.log` (or a step log), `summary.json` and `artifacts/`. Large CAD exports, waveforms or logs may use approved external storage with a stable reference and a checksum recorded in the repository.
- Records are append-only. A correction is a new record that refers to the old one.

## 9. Definition of Done

A task is done only when all of these hold (program acceptance standard section 1):

1. It has a stable ID and the testable criteria above.
2. The change merged through the approved pull request process.
3. Every required check passed on the exact closing commit.
4. Required reviews, including any security or safety approval, are recorded against that commit.
5. Documentation and the changelog are updated.
6. Evidence points to immutable references.
7. No blocking issue was converted into a pass. A waiver is a structured record with approver, scope, rationale and expiry or review condition, and is never reported as PASS.
8. Status is reported from the canonical status record, not from commit counts.

Stricter rules for this repository: a task that needs a hold-reopening or fabrication decision cannot start before that decision is recorded; physical-test tasks additionally need the independent safety review; and a milestone closes only through an approved completion record.

## 10. Known limitations and exclusions

| Item | State | Approving decision |
|---|---|---|
| No Makefile, scripts, tests or workflows exist, so no gate is runnable | Accepted limitation until tasks 002 to 004 | None needed; stated here |
| The `ROB-MECH` prefix and the `ROB-` namespace are unregistered | Criteria are PROPOSED until task 001 is decided | Pending owner decision |
| The independent mechanical and safety reviewer roles are unfilled | Criteria that need them cannot reach PASS | Program decision PD-007 pending |
| Numeric targets, margins, tolerances and instrument accuracy are not yet fixed | Each is set when its task defines it; none is invented here | Set by the owning task |
| Actuator source values may be placeholder or PROPOSED | Labelled in the interface control document | Actuator repository records |
| Physical criteria cannot be tested until robot mechanical work is reopened | Blocked | Pending owner decision |

## 11. Change control

Criteria change by versions, not by edits to accepted ones.

- Add a criterion with the next unused ID for that task. Never reuse an ID.
- Revise a criterion by adding a new version number to this document and a new ID; keep the old one with a status of SUPERSEDED and a reference to its replacement.
- Never edit a criterion against which a task or milestone has already been judged. Evidence that was accepted against the old text stays valid for the old text.
- Every change is an entry in [CHANGELOG.md](CHANGELOG.md) with date, reason and baseline impact, and passes review before merging.
- Criteria changes that affect frozen program records go through the program's change process and are not made here.
