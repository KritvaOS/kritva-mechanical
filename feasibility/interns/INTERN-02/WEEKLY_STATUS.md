# INTERN-02 — Weekly Feasibility Status

| Property | Value |
|---|---|
| Document ID | KMECH-WEEKLY-INTERN-02 |
| Repository | `KritvaOS/kritva-mechanical` |
| Document Type | Intern Weekly Status |
| Status | PROPOSED (Week 2 update, owner review pending) |
| Owner | Dinesh |
| Assigned Intern | INTERN-02 |
| Version | 0.2.0 |
| Last Updated | 2026-11-20 |
| Authority | Weekly progress report; subject to owner review |
| Related Documents | `feasibility/STUDY_PLAN.md`, `feasibility/INTERN_ASSIGNMENTS.md` |

Statuses used: COMPLETE, INCOMPLETE, NOT STARTED, BLOCKED (needs input from someone else), NOT_RUN. Each open item has one ID (W2-nn) and the same status everywhere it appears.

## 1. Reporting Period

- Intern: INTERN-02
- Week: 2
- Reporting dates: <<FILL: first and last day, YYYY-MM-DD>>
- Branch: `patch-1`
- Pull request: <<FILL: PR number>>
- Commit references: see the pull request (a commit cannot contain its own hash)
- Task linkage: <<FILL: ROB-MECH-NNN from planning/TASKS.md>>
- Hold status: D-003 remains active

## 2. Concepts Worked

Assigned concepts: QR-01, DA-02, DA-03, QR-05. Status in this table is the status of the feasibility assessment for that concept.

| Concept ID | Work this week | Status |
|---|---|---|
| QR-01 | Concept sheet and cross-section compared; dimensions and joints extracted; 3 discrepancies logged | INCOMPLETE (W2-05) |
| DA-02 | Concept sheet and cross-section compared; dimensions, joints and actuator count extracted; 4 discrepancies logged | INCOMPLETE (W2-05) |
| DA-03 | Concept sheet and cross-section compared; base drive, mast and arm joints extracted; 5 discrepancies logged | INCOMPLETE (W2-05) |
| QR-05 | Concept README (v0.3.0) written from the two sheets; configuration, printed values and cable routing recorded; sheet discrepancies D1 to D5 resolved by the regenerated cross-section, D6 still open; feasibility checklist not started | NOT STARTED (W2-06) |

## 3. Deliverables vs Plan

| Planned deliverable | Result | Status | Item |
|---|---|---|---|
| Configuration, joints, preliminary dimensions | Recorded from artwork for all four concepts with source labels (section 5.1) | COMPLETE | |
| Illustrative hand calculations | Three, labelled DERIVED and unvalidated (section 5.2) | COMPLETE | |
| Frame and dimension definitions | Conflicts logged, none resolved | BLOCKED | W2-01 |
| Width, reach, actuator-count, drive, mast and QR-05 interface (D6) questions | Logged in sections 5.3 and 5.4 | BLOCKED | W2-02 |
| Actuator data, link lengths, masses | Only printed total weight targets exist | BLOCKED | W2-03 |
| Torque, speed, tip-over and workspace checks | Need W2-01 and W2-03 | BLOCKED | W2-04 |
| Scored assessments (QR-01, DA-02, DA-03) | Findings recorded, not scored | INCOMPLETE | W2-05 |
| QR-05 feasibility assessment | README written; checklist in its section 11 not started | NOT STARTED | W2-06 |
| CP2 contribution | Partial coverage of assigned concepts | INCOMPLETE | W2-07 |
| CP2 architecture review | Not carried out by INTERN-02 | NOT_RUN | W2-08 |

## 4. Blocked and Incomplete Items

| Item | Description | Status | Reason | Action |
|---|---|---|---|---|
| W2-01 | One coordinate frame and dimension-label definitions | BLOCKED | Sheets use conflicting frames and labels | Owner decision |
| W2-02 | Width and reach targets; actuator count; DA-03 drive and mast; QR-05 interface (D6) | BLOCKED | Printed values conflict or are silent | Owner decision |
| W2-03 | Actuator source data (owner, revision, maturity); link lengths; masses | BLOCKED | No controlled data supplied | Actuator owner and Dinesh |
| W2-04 | Torque, speed, tip-over and workspace checks | BLOCKED | Needs W2-01 and W2-03 | Week 3 |
| W2-05 | Scored assessments for QR-01, DA-02, DA-03 | INCOMPLETE | Waiting on W2-01 and W2-02 | INTERN-02 |
| W2-06 | QR-05 feasibility assessment (checklist in its README section 11) | NOT STARTED | README is written; no sketch or calculation done yet | INTERN-02 |
| W2-07 | CP2 contribution | INCOMPLETE | QR-05 assessment and scoring outstanding | INTERN-02 |
| W2-08 | CP2 architecture review | NOT_RUN | Outside INTERN-02 scope | Authorised reviewer |

## 5. Unknowns and Assumptions

### 5.1 Printed values (all `CONCEPT_TARGET`)

The sheets say their dimensions are indicative. No value here comes from another repository. Weights marked "est." are not subsystem estimates.

| Concept | Printed values | Source |
|---|---|---|
| QR-01 | Body 300 (L) × 250 (W) × 200 (H) mm; overall 420 × 400 mm; weight 2.5 to 4 kg (est.); payload 0.3 to 0.8 kg (est.); 24 V | `KMECH-CONCEPT-QR-01`, `KMECH-CROSS-SECTION-QR-01` |
| DA-02 | Width 800 mm; shoulder-to-shoulder 600 mm; torso 300 × 250 mm; height 550 mm; reach 350 mm per side; base 300 × 250 mm; weight 8 to 12 kg (est.); payload 0.1 to 0.2 kg per arm (est.); 24 V | `KMECH-CONCEPT-DA-02`, `KMECH-CROSS-SECTION-DA-02` |
| DA-03 | Width 800 mm; total reach 800 mm; reach 350 mm per side; base 400 (W) × 450 (L) mm; torso width 300 mm; height 650 mm with mast; weight 12 to 18 kg (est.); payload 0.1 to 0.2 kg per arm (est.); 24 V | `KMECH-CONCEPT-DA-03`, `KMECH-CROSS-SECTION-DA-03` |
| QR-05 | Body 420 (L) × 260 (W) × 250 (H) mm; overall 560 × 520 mm; 8 or 12 actuators (2 or 3 DOF per leg); weight 4 to 6 kg (est., with 12 DOF); payload 0.5 to 1.0 kg (est.); 24 V | `KMECH-CONCEPT-QR-05`, `KMECH-CROSS-SECTION-QR-05` |

### 5.2 Derived values (DERIVED, unvalidated)

| Value | Inputs | Result | Caveat |
|---|---|---|---|
| QR-01 foot offset | Foot at ±200 mm (half of overall width 400 mm); hip axes at ±125 mm (half of body width 250 mm, assumption A3, unapproved) | 75 mm | Body length 300 mm would give 50 mm. Assumes the 400 mm width is lateral. |
| QR-05 foot offset | Foot at ±260 mm (half of overall width 520 mm); hip axes at ±130 mm (half of body width 260 mm; assumption, intern-proposed, unapproved) | 130 mm | Uses body width 260 mm, not a 300 mm base. Assumes the 520 mm width is lateral. The 3-DOF module's abduction joint changes this offset in use. |
| Payload torque at shoulder (DA-02, DA-03) | 0.2 kg × 9.81 m/s² × 0.35 m | about 0.69 N·m | Excludes arm mass (unknown); not compared with any actuator |
| QR-01 foot load | 2.5 to 4 kg × 9.81 m/s²; 4 feet or 2 feet | about 6 to 10 N (4 feet); 12 to 20 N (2 feet) | Before payload and dynamics; leg lengths unknown |

### 5.3 Unreconciled targets

- DA-03: reach 350 mm per side, width 800 mm and total reach 800 mm cannot all hold. Fully extended, 800 mm means only a 100 mm shoulder spacing, which does not fit a 300 mm torso. The 800 mm values may assume an unstated arm pose.
- DA-02: width 800 mm, shoulder-to-shoulder 600 mm and reach 350 mm have the same problem.

### 5.4 Open questions for the owner (`OWNER_DECISION`)

- Frame: side-view legends are left-handed (X forward, Z up, Y right), and DA top views use different axes. QR-01 shows Y right in side view and Y left in top view. (W2-01)
- QR-01 labels: overall width 400 mm is drawn along the same axis as body length 300 mm, and body height 200 mm is defined differently on the two sheets. (W2-01)
- DA-02: 8 actuators on the concept sheet, 9 on the cross-section (head pan); gripper actuation not counted. (W2-02)
- DA-03: four wheels but only 2 base actuators in the total of 8, with no transmission shown; the mast is height adjustable but has no actuator; LiDAR is named but not drawn. (W2-02)
- QR-05: the body mounting interface (4 × M5 holes, 2 × Ø5 mm dowels) and the height-adjustable sensor module appear on the cross-section only and are labelled indicative (README discrepancy D6, open). (W2-02)
- Capability limits: DA-02 has no wrist roll, DA-03 has no shoulder pitch, QR-01 has no hip abduction.
- Still unknown: joint ranges and speeds, link lengths and masses, actuator ratings, centre of mass, battery capacity, QR-05 joint torque, speed and stride.

A1 to A5 in the QR-01 write-up are intern-proposed and unapproved. They are not used as reference values here, except A3 as named in section 5.2.

## 6. Risks Raised

| Risk ID | Description | Mitigation |
|---|---|---|
| I02-R01 | Conflicting frames and labels across sheets (W2-01) | Owner fixes one frame and the label definitions |
| I02-R02 | Actuator data missing (W2-03) | Keep torque figures labelled DERIVED until controlled data arrives |
| I02-R03 | DA-03 drive layout does not match the actuator count (W2-02) | Owner confirms 2 motors with transmission or 4 motors |
| I02-R04 | Arm and leg DOF limits may not cover the stated uses | Record as capability limits in the assessments (W2-05) |
| I02-R05 | QR-05 leg-module interface is undefined (D6); mass, stiffness and connector cost unknown | Sketch the interface concept in the QR-05 assessment (W2-06) |

The global risk register was not edited.

## 7. Next Actions

| Item | Action | Owner | Target | Status |
|---|---|---|---|---|
| W2-01 | Fix one coordinate frame and dimension definitions | Dinesh | Before Week 3 work | BLOCKED |
| W2-02 | Decide width, reach, actuator-count, drive, mast and QR-05 interface (D6) questions | Dinesh | Before Week 3 work | BLOCKED |
| W2-03 | Supply actuator data, link lengths and masses | Actuator owner and Dinesh | Week 3 | BLOCKED |
| W2-04 | Torque, speed, tip-over and workspace checks | INTERN-02 | Week 3 | BLOCKED |
| W2-05 | Complete scored assessments | INTERN-02 | CP2 | INCOMPLETE |
| W2-06 | Start the QR-05 feasibility assessment (README section 11 checklist) | INTERN-02 | Week 3 | NOT STARTED |
| W2-07 | Complete CP2 contribution | INTERN-02 | CP2 | INCOMPLETE |
| W2-08 | CP2 architecture review | Authorised reviewer | CP2 | NOT_RUN |

## 8. Repository Evidence

- Branch: `patch-1`
- Pull request: <<FILL: PR number>>. Related PR #19 rewrites the same file; relationship: <<FILL: supersedes / superseded by / closed>>
- Commit references: see section 1
- Relevant paths: this file and the QR-01 and QR-05 concept folders under `feasibility/`
- Source artwork: `KMECH-CONCEPT-DA-02`, `KMECH-CONCEPT-DA-03`, `KMECH-CONCEPT-QR-01`, `KMECH-CROSS-SECTION-DA-02`, `KMECH-CROSS-SECTION-DA-03`, `KMECH-CROSS-SECTION-QR-01`
- Review: owner review requested changes; this revision responds to them; approval pending

## 9. D-003 Compliance

This week's work was paper-only: artwork review, hand calculations and concept sketches. No CAD, final BOM, quotation, procurement, fabrication, assembly, physical testing or hardware integration was started.

- Intern confirmation: TBD
- Date: TBD
- Exceptions: TBD (set together with the confirmation)

Mechanical HOLD D-003 remains in effect. Any exception requires explicit owner review.
