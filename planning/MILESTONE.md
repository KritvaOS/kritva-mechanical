# Robot Mechanical Milestones

| Property | Value |
|---|---|
| Document ID | KOS-MECH-MILESTONE |
| Repository | `KritvaOS/kritva-mechanical` |
| Document Type | Plan |
| Status | PROPOSED (accepted by the owner as a working planning baseline on 2026-10-28; owner statement made in a working session, not yet recorded in kritva-program) |
| Owner | Dinesh (program owner) |
| Reviewer / Approver | Dinesh for planning acceptance; independent mechanical reviewer not yet identified (program reviewer roles are pending decision PD-007) |
| Version | 0.1.0 |
| Last Updated | 2026-10-28 |
| Authority | AUTHORITATIVE for this repository's milestone definitions (role, not approval). Not a program baseline entry. |
| Related Tasks / Milestones | ROB-M0 to ROB-M5; tasks are defined in `TASKS.md` (PLANNED) |
| Related Documents | [README.md](../README.md); kritva-program [acceptance standard](https://github.com/KritvaOS/kritva-program/blob/main/v2/planning/ACCEPTANCE_STANDARD.md), [gate register](https://github.com/KritvaOS/kritva-program/blob/main/v2/GATE_REGISTER.md), [decision log](https://github.com/KritvaOS/kritva-program/blob/main/v2/DECISIONS.md) |

## Purpose

This document defines the sequence of milestones for the mechanical design of the complete Kritva robot above the actuator level, the evidence each one needs, and the rules for changing them. It is read by the repository owner, reviewers and contributors who need to know what comes next, what must be true before work starts, and what proves it is finished.

It is a planning document. A milestone listed here is not complete, funded, scheduled or authorised for physical work merely because it is listed. Every date is absent or labelled PROPOSED.

## 1. Working policy

The owner accepted all proposed milestones as working planning baselines on 2026-10-28 and expects to adjust them as the work teaches us more. The following rules apply while that policy stands.

1. **Accepted for planning only.** Tasks, owners, dependencies and reviews may be planned against these milestones now. Nothing waits for further formal re-approval of the milestone list itself.
2. **Adjustable.** Milestones may be added, split, merged, reordered or rescheduled under section 7. IDs are never reused.
3. **The program baseline is frozen and separate.** These milestones are planning inventory. They carry no weight and no credit and are never written into kritva-program `baseline.json` by this repository. Existing task IDs, weights, approvals and accepted progress are not rewritten. Changes that touch them follow the program's append-only, commit-bound approval process.
4. **Planning is not completion.** An accepted milestone does not mean its tasks are done, its evidence verified or its criteria passed.
5. **Gates stay enforced.** Accepting the plan does not clear the mechanical hold (decision D-003), any safety review, any fabrication authorisation or any physical-test requirement. Section 5 states which milestone work each gate blocks.
6. **One reporting contract.** Task status, evidence, commits, CI results and human reviews follow the kritva-program status contract (schema 2.0). This repository reports facts and does not declare program acceptance.

## 2. Naming and scope

| Name | Meaning | Owner |
|---|---|---|
| ROB-A0, ROB-A1 and so on | A robot hardware baseline: one named, frozen robot configuration. The first is ROB-A0. A later baseline is a separate configuration with its own tasks, never an edit of an earlier one. | this repository (PROPOSED namespace) |
| ROB-M0 to ROB-M5 | Robot mechanical milestones, defined below. They apply to a hardware baseline; ROB-A0 is the first one they are planned against. | this repository (PROPOSED namespace) |
| P0 to P8 | Frozen program phases. Never redefined or renamed here. | kritva-program |
| A0, A1, A2 and Gates A, B, C | The actuator family's own lifecycle and release gates. Not robot hardware versions and not robot milestones. | kritva-actuator |
| B0 to B4 | Proposed program-alignment batches (section 6). They describe the order of alignment work across repositories, not hardware milestones. | alignment plan |

The `ROB-` namespace is PROPOSED. It must be registered with kritva-program before tasks that use it can earn program credit, and a prefix collision with an existing ID is resolved in the program's favour.

**In scope:** frame and structure, torso, arms, hands, legs, feet, robot-level assemblies, the robot side of actuator mounting, mass properties, load cases, drawings, bill of materials, assembly and inspection procedures, mechanical verification.

**Out of scope:** actuator internals (owned by the actuator repositories), electronics and firmware, software, power and compute design, and any change to the program baseline.

## 3. Milestone summary

All milestones are NOT_STARTED. No percentage or count of completion is recorded here; the program status view is the place for derived progress.

| ID | Title | Objective | Exit evidence (summary) | Depends on | Authorisation beyond planning |
|---|---|---|---|---|---|
| ROB-M0 | Requirements baseline | Freeze the ROB-A0 configuration and mechanical requirements | Approved requirements, load cases, first interface control document, initial risk register | Registered workstream and ID prefix | None needed for document work |
| ROB-M1 | Architecture | Settle the frame, torso, limb and joint architecture | Reviewed architecture documents, interface definitions, mass budget; CAD skeleton once the hold allows | ROB-M0 | CAD skeleton needs the hold reopened |
| ROB-M2 | Detailed design | Complete the initial mechanical design | Released CAD, drawings, BOM and engineering calculations | ROB-M1 | Needs the hold reopened |
| ROB-M3 | Fabrication readiness | Establish manufacturing and assembly readiness | Approved manufacturing package, tolerances, procurement list, inspection plan | ROB-M2 | Needs the hold reopened and explicit authority to procure and fabricate |
| ROB-M4 | Assembly and inspection | Assemble the authorised prototype and inspect it | Inspection records, dimensional results, deviation register | ROB-M3, actuator inputs | Needs fabrication authority and open safety gates handled |
| ROB-M5 | Mechanical verification | Verify the assembly against its requirements | Test records, defect closure, independent acceptance | ROB-M4 | Needs controlled test fixture, procedures and independent safety review |

## 4. Milestone records

Evidence types are labelled throughout: **S** software check, **C** calculation, **Sim** simulation, **B** bench measurement, **P** independently accepted physical test. Software, calculation and simulation evidence is never reported as physical verification.

Every milestone closes only through an approved `COMPLETION_RECORD.md` built from the program template. A merge, a passing run, a tag or a task marked complete does not close a milestone.

### ROB-M0 Requirements baseline

**Objective.** Fix what the first robot configuration (ROB-A0) must do mechanically, in measurable terms, before any architecture or CAD starts.

**In scope.**
- Define the ROB-A0 configuration: body segments, degrees of freedom per joint and the intended use, with numeric targets (height, mass, payload, reach, speed, range of motion) each carrying a unit and a source.
- Mechanical requirements with stable IDs, a verification method each and traceability to the program requirements (`PRS.md` and `REQUIREMENT_TRACEABILITY.md` in kritva-program).
- Load cases: standing, walking, lifting a payload, and any impact or fall case the owner decides to include, each with its basis.
- First robot-to-actuator interface control document, listing the candidate S, M or L actuator for each joint and the data each actuator repository must supply.
- Initial risk and dependency register for the milestone.

**Out of scope.** CAD, drawings, BOM, quotes, procurement, fabrication, any physical work.

**Prerequisites and dependencies.** The mechanical workstream and task prefix are registered (or a written plan to register them exists) and the program hold reading in the README section 13 is confirmed by the owner. Actuator repositories supply preliminary dimensions, mass and limits; where those are still preliminary they are labelled so.

**Entry criteria.**
1. Owner confirms the ROB-A0 intent in writing.
2. The task register exists with at least the ROB-M0 tasks.
3. Actuator inputs needed are identified, with their state (ESTABLISHED, PROPOSED, UNVERIFIED).

**Deliverables.** `requirements/`, a load-case document, the interface control document v0.1, the risk register, and the ROB-M0 acceptance criteria.

**Exit criteria (all measurable).**
1. Every requirement has an ID, a unit where numeric, a verification method and a traced parent; none is untestable as written.
2. Every load case states its inputs, source and how its result will be checked.
3. The interface control document names, for every joint, the actuator variant, mounting datum, envelope, mass, torque and speed limits used, and the revision or commit of each source; any placeholder or unverified value is labelled.
4. The risk register names an owner and a response for each risk.
5. Review recorded against the closing commit by the owner and an independent reviewer.

**Evidence.** S (document and link checks), review records. No C, Sim, B or P evidence is expected.

**Approvals.** Owner; independent reviewer (role pending PD-007).

**Gate status.** No hold work. Planning documents only.

### ROB-M1 Architecture

**Objective.** Decide how the robot is structured and divided, and what each interface carries, so detailed design can begin without rework.

**In scope.**
- Frame, torso, limb and joint architecture: segment layout, joint axes, load paths, material and process options considered.
- Interface definitions between segments and to each actuator, versioned.
- Mass budget by segment and a centre-of-mass target.
- Wiring and service-access envelopes (the physical space reserved, not the electrical design).
- A CAD skeleton (reference geometry only) once the hold allows it.

**Out of scope.** Detailed part design, drawings, BOM, procurement, fabrication.

**Prerequisites.** ROB-M0 complete. Actuator interface data at least PROPOSED with its state labelled.

**Entry criteria.** ROB-M0 completion record approved; open ROB-M0 deviations logged.

**Deliverables.** `architecture/` documents; interface control document v1.0 candidate; mass budget; CAD skeleton (blocked until the hold is reopened).

**Exit criteria.**
1. Every requirement from ROB-M0 maps to an architectural element or is recorded as deferred with a decision.
2. The mass budget closes within the ROB-M0 target with stated margin, or the shortfall is recorded as a decision.
3. Every interface is versioned and agreed with the actuator repository that owns the other side, evidenced by a reference to its commit.
4. Architecture reviewed, with findings closed or deferred by decision.
5. If a CAD skeleton exists: it parses without errors, datums and units are valid, and it matches the interface documents (checked per `verification/SANITY_PLAN.md`).

**Evidence.** S, C (mass and load-path estimates), Sim where used (labelled). No P evidence.

**Approvals.** Owner; independent mechanical reviewer.

**Gate status.** Architecture documents are planning work. The CAD skeleton is mechanical CAD and stays blocked until an owner decision reopens robot mechanical work.

### ROB-M2 Detailed design

**Objective.** Produce a complete, reviewable mechanical design for ROB-A0.

**In scope.** Part and assembly CAD, drawings with tolerances, BOM with identifiable parts, engineering calculations (strength, stiffness, fatigue where applicable, fasteners, bearings, joints), mass properties, interference and clearance checks.

**Out of scope.** Quotes, ordering, manufacturing, assembly.

**Prerequisites.** ROB-M1 complete; hold reopened for robot mechanical scope; CAD tool and file-storage convention approved.

**Entry criteria.** ROB-M1 completion record approved; the owner's reopening decision recorded in kritva-program.

**Deliverables.** Released CAD and drawings (with revision identifiers or checksums), BOM, calculation set, mass-properties report.

**Exit criteria.**
1. Every part in the BOM has a drawing or a purchase specification and a unique identifier.
2. Calculations cover every load case from ROB-M0 and meet the stated margins, with inputs traceable to the requirements and actuator data.
3. No unresolved interference or clearance failure in the assembly check.
4. Mass properties are within budget or the deviation is a recorded decision.
5. Design review held; findings closed or deferred by decision; reviewer and revision recorded against the closing commit.

**Evidence.** S, C, Sim (labelled). Design acceptance is not physical validation.

**Approvals.** Owner; independent mechanical reviewer. Safety review where the design touches safety-gated functions.

**Gate status.** Needs the hold reopened.

### ROB-M3 Fabrication readiness

**Objective.** Show the design can be made, bought, assembled and inspected before any money or material is committed.

**In scope.** Manufacturing package, tolerance and surface requirements, process selection, procurement list and supplier options, assembly sequence, inspection plan and measurement methods, fixture needs, cost and lead-time estimates.

**Out of scope.** Placing orders, fabricating parts, assembly.

**Prerequisites.** ROB-M2 complete; explicit owner authority covering quotes and procurement.

**Entry criteria.** ROB-M2 completion record approved; written authority to request quotes.

**Deliverables.** Approved manufacturing package, procurement list, inspection plan, assembly procedure draft, and a fabrication authorisation request for the owner.

**Exit criteria.**
1. Every manufactured part has a process, tolerance and inspection method; every purchased part has a source or alternatives.
2. The inspection plan defines instruments, accuracy and acceptance limits for every critical dimension.
3. The assembly procedure is reviewed against the design and the actuator mounting contracts.
4. Safety and handling risks for assembly are recorded with controls.
5. The owner decides whether to authorise fabrication; that decision is recorded in kritva-program. Fabrication does not start on the strength of this milestone closing.

**Evidence.** S, C, review records, supplier quotes where obtained.

**Approvals.** Owner (including fabrication authority); independent reviewer; safety review for assembly hazards.

**Gate status.** Needs the hold reopened and explicit authority to procure and fabricate.

### ROB-M4 Assembly and inspection

**Objective.** Build the authorised prototype and record what was actually built.

**In scope.** Part receipt and inspection, assembly to the approved procedure, dimensional inspection, deviation and non-conformance records, as-built configuration record, integration with actuators.

**Out of scope.** Loaded or powered testing beyond what the assembly procedure explicitly permits.

**Prerequisites.** ROB-M3 complete; fabrication authorised; actuator inputs at their required maturity; controlled workspace and handling controls in place; open safety gates reviewed.

**Entry criteria.** ROB-M3 completion record approved; fabrication authority recorded; actuator release gates relevant to the assembly reviewed and their state recorded.

**Deliverables.** Inspection records (instrument IDs and calibration), as-built BOM, deviation register, assembly record with dates and personnel.

**Exit criteria.**
1. Every critical dimension is measured and within tolerance, or the deviation is dispositioned by decision.
2. The as-built configuration is recorded against the released revision; every difference is listed.
3. The deviation register has no open item without an owner and a disposition.
4. Assembly record reviewed independently.

**Evidence.** B (inspection), review records. No functional or load claim is made.

**Approvals.** Owner; independent reviewer; safety reviewer where hazards were identified.

**Gate status.** Needs fabrication authority; physical activities remain subject to the open safety gates in README section 13.

### ROB-M5 Mechanical verification

**Objective.** Show by test that the assembled hardware meets its mechanical requirements.

**In scope.** Test procedures, controlled fixtures, instrumented load and range-of-motion tests, defect tracking and closure, independent acceptance.

**Prerequisites.** ROB-M4 complete; approved test procedures; a controlled test fixture; safety review of the test plan.

**Entry criteria.** ROB-M4 completion record approved; test plan approved; safe-state and stop procedures verified.

**Deliverables.** Test records tied to the exact as-built revision (immutable per-run evidence with manifest, environment, log, summary and checksums), defect register, verification summary, independent acceptance record.

**Exit criteria.**
1. Every requirement with a physical verification method has a recorded result against the exact tested revision.
2. Every failed or inconclusive test has a defect with an owner and a disposition.
3. Independent acceptance is recorded.
4. A result from an older revision is never used to certify a newer one.

**Evidence.** B and P, with C and Sim as supporting only.

**Approvals.** Owner; independent mechanical reviewer; independent safety review.

**Gate status.** Physical testing is controlled by the safety and release gates; closing this milestone does not by itself release the hardware.

## 5. Gate and authorisation matrix

These are PROPOSED planning gates for this repository, not entries in the program gate register.

| Milestone | May proceed now | Blocked until |
|---|---|---|
| ROB-M0 | Yes: documents and requirements only | Nothing beyond registering the workstream and prefix before credit is sought |
| ROB-M1 | Architecture documents: yes. CAD skeleton: no | Owner decision reopening robot mechanical work (hold D-003; MECHANICAL workstream `hold: true`) |
| ROB-M2 | No | Reopening decision; approved CAD tool and storage convention |
| ROB-M3 | Planning of the package only, no quotes | Reopening decision and written authority to obtain quotes and procure |
| ROB-M4 | No | Fabrication authority; relevant actuator gates reviewed; P6 LAB & ROBOT entry decision |
| ROB-M5 | No | Controlled fixture, approved test plan, independent safety review |

The hold was lifted by decision D-052 for the five actuator workstreams only. That authorisation is not read as covering the robot mechanical scope.

## 6. Relationship to the program alignment batches

| Batch | Meaning | Link to this document |
|---|---|---|
| B0 Governance | Reconcile hold state, freeze the common task, status, commit and evidence contract, define baseline registration | Prerequisite for registering ROB workstream and prefix |
| B1 Actuator parent and embedded | Refresh task records and reports, reconcile interfaces and gate ownership | Supplies interface inputs to ROB-M0 and ROB-M1 |
| B2 S/M/L variants | Validate sizing inputs and variant checks | Supplies geometry, mass and limits for the interface control document |
| B3 Robot mechanical | Approve ownership and naming, establish this planning set, register the repository and workstream | This repository's planning set is the B3 deliverable |
| B4 End-to-end validation | Run full consolidation, verify CI evidence and traceability, audit | Checks that the ROB milestones are reported accurately |

Batches B0 to B4 are alignment work, not approved program milestones, and do not take the place of ROB-M0 to ROB-M5.

## 7. Adjustment policy

A milestone may change when the work shows it should. The change is recorded so that nothing is silently rewritten.

| Change | Rule |
|---|---|
| Add | Give it the next unused ID. State objective, entry and exit criteria, evidence and approvals before tasks are assigned to it. |
| Split | Keep the original ID for the part that continues; give new IDs to the new parts; record where each criterion went. |
| Merge | Retire the absorbed ID and record it as merged, not deleted. |
| Reorder | Update the dependencies and the summary table together and record the reason. |
| Reschedule | Dates are PROPOSED until the owner approves them. Record the old and new value and the reason. |
| Change criteria | Add a new criteria version. Do not edit criteria that an accepted milestone was judged against. |

Each change is one entry in `CHANGELOG.md` with the date, what changed, why, and its baseline impact. Changes that touch frozen program records (baseline, approvals, gate closures, task weights) are made only through the program's change process. After a milestone is closed, its definition is not edited; later changes go into a new milestone or a recorded amendment.

## 8. Status

| Milestone | Status | Review | Notes |
|---|---|---|---|
| ROB-M0 | NOT_STARTED | NOT_REVIEWED | Needs registration of workstream and prefix |
| ROB-M1 | NOT_STARTED | NOT_REVIEWED | CAD skeleton blocked by hold |
| ROB-M2 | NOT_STARTED | NOT_REVIEWED | Blocked by hold |
| ROB-M3 | NOT_STARTED | NOT_REVIEWED | Blocked by hold and procurement authority |
| ROB-M4 | NOT_STARTED | NOT_REVIEWED | Blocked by fabrication authority and safety gates |
| ROB-M5 | NOT_STARTED | NOT_REVIEWED | Blocked by fixture and safety review |

Allowed status values: NOT_STARTED, IN_PROGRESS, BLOCKED, VERIFICATION_PENDING, COMPLETE. COMPLETE means the milestone's completion record is approved; it does not imply program credit.

## 9. Open decisions

These need an owner answer before the dependent work can be planned in detail.

1. **Registration.** Which program workstream ID and task prefix register this repository (the existing `MECHANICAL` workstream has no repository; `ROB-MECH` is the proposed prefix).
2. **Hold.** Whether and when robot mechanical work is reopened, and whether planning-document work under this repository is confirmed as permitted while it is held.
3. **ROB-A0 definition.** The intended robot configuration and its numeric targets.
4. **Reviewers.** Who is the independent mechanical reviewer and the safety reviewer (program decision PD-007 is pending).
5. **CAD and storage convention.** Which CAD tool, file format, revision identifiers and artifact storage the repository uses.
6. **Dates.** Whether and when to propose target dates; none exist today.
7. **Visibility.** The repository's visibility class decision.

## 10. Completion record

On closing a milestone, a `COMPLETION_RECORD.md` is written from the program template, naming the milestone ID, scope, merge and release commits, test runs, the disposition of each criterion (PASS, WAIVED with an approval reference, or NOT_APPLICABLE with an approval reference), deferred work and its deferring decision, approvals and immutable evidence references. A waiver is a structured record and is never reported as PASS.
