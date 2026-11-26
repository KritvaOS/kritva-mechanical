# DA-02 — Requirements

| Property | Value |
|---|---|
| Document ID | KMECH-REQ-DA-02 |
| Repository | `KritvaOS/kritva-mechanical` |
| Document Type | Concept Requirements |
| Status | PROPOSED |
| Owner | Dinesh |
| Assigned Intern | INTERN-02 |
| Version | 0.2.0 |
| Last Updated | 2026-11-25 |
| Authority | Proposed concept requirements; subject to owner review |
| Related Documents | `README.md`, `ARCHITECTURE.md`, `MECHANICAL_ANALYSIS.md`, `ACTUATOR_ANALYSIS.md`, `MASS_BUDGET.md`, `feasibility/REQUIREMENTS_REGISTER.md` |

These are **proposed** concept requirements drafted from the DA-02 artwork and the preliminary paper work. None is approved. Values printed on the artwork are CONCEPT_TARGET (indicative, unapproved, not a requirement); where the owner has not resolved a value it stays `UNKNOWN` or `TBD` here and in the requirements register.

## 1. Scope

Concept ID/name: DA-02 — Humanoid Torso Dual-Arm

Intended application and demonstration objective: Kritva platform demonstration, with manipulation, pick-and-place, and research and development as the uses printed on the concept sheet. Fixed base plate, two 4-DOF arms on a humanoid torso, optional one-axis head. Upgrade to 5-DOF arms or a mobile base is a future path and is outside the study baseline.

## 2. Requirements Register

Priority is the intern's proposal for owner review (High, Medium, Low). Evidence type C = paper calculation, comparison or sketch. All statuses are PROPOSED.

| ID | Requirement | Source | Priority | Verification method | Evidence type | Status | Notes |
|---|---|---|---|---|---|---|---|
| CREQ-001 | The concept shall be a fixed-base humanoid-torso dual-arm: two symmetric arms of 4 DOF each (shoulder yaw, shoulder pitch, elbow pitch, wrist pitch) on a fixed torso and base plate, with no mobility. | Concept and cross-section sheets; `README.md` §3 | High | Review | C | PROPOSED | Axis directions are taken from sheet labels (vertical yaw, horizontal pitch axes assumed, `MECHANICAL_ANALYSIS.md` S1). |
| CREQ-002 | The baseline shall have 8 arm actuators (4 per arm); the optional head pan shall add 1, giving 9 when fitted. | `README.md` §10 D6 (resolved by owner 2026-10-31) | High | Review | C | PROPOSED | Gripper actuator count is separate and TBD. |
| CREQ-003 | Each arm shall carry a two-finger parallel gripper; whether it is powered (servo or BLDC) or passive shall be an owner decision. | Concept and cross-section sheets; `README.md` §16 | Medium | Review / calculation | C | PROPOSED | Preliminary grip force about 2 – 4 N per finger for 0.2 kg by friction (`MECHANICAL_ANALYSIS.md` §3). |
| CREQ-004 | The concept shall allow an optional one-axis pan head carrying an RGB-D or stereo camera; whether it is fitted in the study configuration shall be decided by the owner. | Concept sheet; cross-section sheet; `README.md` §16 | Low | Review | C | PROPOSED | Head is not analysed for loads yet. |
| CREQ-005 | The study shall assess the concept against the printed indicative envelope (550 mm height, 800 mm overall width, 300 mm × 250 mm torso and base) and report where it does not fit. | Concept and cross-section sheets (CONCEPT_TARGET) | Medium | Review / calculation | C | PROPOSED | Printed values are not approved requirements. Width inconsistency noted under D5. |
| CREQ-006 | The study shall define each arm's usable workspace from the joint ranges and reach, including the arm overlap zone and table-level reach. | Concept sheet; `MECHANICAL_ANALYSIS.md` §4 | High | Calculation | C | PROPOSED | Reach itself is UNKNOWN (Section 3); printed 350 mm is CONCEPT_TARGET. |
| CREQ-007 | The study shall assess the printed payload target per arm and state the payload location used. | Concept sheet (CONCEPT_TARGET) | High | Calculation | C | PROPOSED | Payload is UNKNOWN until the owner resolves it. |
| CREQ-008 | The study shall provide a mass estimate by subsystem with stated assumptions, kept separate from the printed target mass. | `README.md` §11; `MASS_BUDGET.md` | Medium | Calculation | C | PROPOSED | Estimate about 10.0 kg baseline (range about 5.8 – 14.3 kg); not a requirement. |
| CREQ-009 | Each joint's torque, speed and range shall be derived independently for a stated payload and pose, and compared with S/M/L data once supplied. The elbow discussion reference values shall not be copied to other joints. | `ACTUATOR_ANALYSIS.md` §2 – §3 | High | Calculation | C | PROPOSED | S/M/L mapping not started. |
| CREQ-010 | The actuator direction shall be BLDC/PMSM with S/M/L compatibility assessed per joint. | Concept sheet; study direction | High | Review / calculation | C | PROPOSED | No `kritva-actuator` data supplied yet; maturity UNKNOWN. |
| CREQ-011 | The power direction shall be 24 V DC (investigation only), with 5 V and 12 V rails shown inside the torso, and no electrical interface shall be treated as confirmed. | Concept and cross-section sheets | Medium | Review | C | PROPOSED | Electrical requirements TBD. |
| CREQ-012 | The torso shall be assessed for housing Kritva Edge, motor drivers (left and right stacks), the power distribution board and the IMU, and the interface list shall be defined. | Cross-section sheet; `ARCHITECTURE.md` §4 | High | Sketch / review | C | PROPOSED | Packaging in 300 mm × 250 mm not assessed. EtherCAT provisions not shown on the sheets (TBD). |
| CREQ-013 | The study shall assess base loading and tipping margin for the extended-arm case and the need to fix the base. | `README.md` §9; `MECHANICAL_ANALYSIS.md` §4 | High | Calculation | C | PROPOSED | Preliminary margins about 1.3 – 1.7 for an assumed 20 N disturbance (not a requirement). |
| CREQ-014 | The study shall assess inter-arm and arm-to-torso interference using defined link and gripper envelopes. | `MECHANICAL_ANALYSIS.md` §4 | Medium | Sketch / calculation | C | PROPOSED | Envelopes not defined. |
| CREQ-015 | The cable path through each shoulder, joint, the torso and the head neck shall be listed with bend, twist and pinch concerns, and service access shall be identified. | Cross-section sheet; `README.md` §8 | Medium | Sketch / review | C | PROPOSED | No harness design implied. |
| CREQ-016 | Pinch and crush hazards, power-off droop and unresolved safety questions shall be identified and carried as open items; no safeguard is selected in this study. | `MECHANICAL_ANALYSIS.md` §6 | Medium | Review | C | PROPOSED | Safety requirements for people nearby are not defined. |
| CREQ-017 | Work shall remain paper-based (calculations, comparison tables, sketches, cited datasheets) under HOLD D-003. | HOLD D-003 | High | Review | C | PROPOSED | Constraint on the study. |

## 3. Assumptions and Constraints

- Payload: UNKNOWN. Printed CONCEPT_TARGET 0.1 – 0.2 kg per arm (est.), no stated basis.
- Reach: UNKNOWN. Printed CONCEPT_TARGET 350 mm shoulder to gripper.
- Target mass: UNKNOWN. Printed CONCEPT_TARGET 8 – 12 kg (est.), no stated basis.
- Joint torque and speed: TBD. Preliminary estimates exist in `ACTUATOR_ANALYSIS.md` (for example shoulder pitch about 2.6 N·m holding) and use assumed values; they are not requirements.
- Power direction: 24V DC investigation only
- Actuator direction: BLDC/PMSM, S/M/L; compatibility TBD
- Other constraints:
  - Fixed base plate, no mobility; 5-DOF arms and mobile base are future path only.
  - Evidence type C only; no CAD, quotations or procurement (HOLD D-003).
  - The elbow reference of 24 V, 10 N·m continuous and 20 N·m peak is not a universal specification.
  - Printed envelope and masses are indicative and unapproved.

## 4. Requirement Traceability

Study-level IDs (`FREQ-xxx`) and open items (`U-xxx`) are TBD because `feasibility/REQUIREMENTS_REGISTER.md` was not available when this draft was prepared. They are to be added when the register is checked.

| Requirement | Related FREQ / open item | Concept-specific evidence or calculation |
|---|---|---|
| CREQ-001 | FREQ-TBD | Concept and cross-section sheets; `ARCHITECTURE.md` §3 |
| CREQ-002 | FREQ-TBD; D6 resolved | `README.md` §6 and §10; `ARCHITECTURE.md` §3 |
| CREQ-003 | FREQ-TBD; open decision on powered grippers | CALC-DA02-03 §1 (`MECHANICAL_ANALYSIS.md` §3) |
| CREQ-004 | FREQ-TBD; open decision on head | `ARCHITECTURE.md` §2; D6 follow-up |
| CREQ-005 | FREQ-TBD; D5 | `ARCHITECTURE.md` §1; `MASS_BUDGET.md` §4 |
| CREQ-006 | FREQ-TBD; U-TBD (joint ranges) | CALC-DA02-03; `MECHANICAL_ANALYSIS.md` §4 |
| CREQ-007 | FREQ-TBD; U-TBD (payload) | CALC-DA02-01; `ACTUATOR_ANALYSIS.md` §2 |
| CREQ-008 | FREQ-TBD; U-TBD (mass basis) | CALC-DA02-02; `MASS_BUDGET.md` |
| CREQ-009 | FREQ-TBD | CALC-DA02-01; `ACTUATOR_ANALYSIS.md` §2 – §3 |
| CREQ-010 | FREQ-TBD; U-TBD (S/M/L data) | `ACTUATOR_ANALYSIS.md` §4 |
| CREQ-011 | FREQ-TBD | Cross-section sheet; `README.md` §7 |
| CREQ-012 | FREQ-TBD; U-TBD (interfaces, EtherCAT) | `ARCHITECTURE.md` §4 |
| CREQ-013 | FREQ-TBD | CALC-DA02-03; `MECHANICAL_ANALYSIS.md` §4 |
| CREQ-014 | FREQ-TBD | `MECHANICAL_ANALYSIS.md` §4 |
| CREQ-015 | FREQ-TBD | `README.md` §8; `ARCHITECTURE.md` §4 |
| CREQ-016 | FREQ-TBD | `MECHANICAL_ANALYSIS.md` §6 |
| CREQ-017 | HOLD D-003 | All documents |

CALC-DA02-01, -02 and -03 are referenced and still to be filed in `calculations/`.

## 5. Open Requirements

| Item | Missing information | Dependency / action |
|---|---|---|
| Payload per arm | UNKNOWN: required value and payload location | Owner decision; drives CREQ-007, CREQ-009 |
| Reach and workspace | UNKNOWN: required reach, joint ranges, table-level reach need | Owner decision; kinematic sketch (CREQ-006) |
| Target mass | UNKNOWN: required or limit value | Owner decision; `MASS_BUDGET.md` (CREQ-008) |
| Joint torque, speed and duty | TBD: required values, duty cycle | S/M/L data and owner input (CREQ-009) |
| Shoulder-to-shoulder spacing (D5) | INCOMPLETE: 600 mm on concept sheet only; width inconsistency | Owner to clarify; affects CREQ-005, -006, -013, -014 |
| Head fitted | TBD | Owner decision (CREQ-004) |
| Grippers powered | TBD | Owner decision (CREQ-003) |
| Actuator source data and S/M/L mapping | BLOCKED: no `kritva-actuator` revision supplied | Owner to provide source and maturity (CREQ-010) |
| Base fixing and stability criterion | TBD: fixing method, acceptable margin | Owner decision (CREQ-013) |
| Interface list and EtherCAT provisions | TBD: not shown on the sheets | `INTERFACES.md` to be created (CREQ-012) |
| Whether S/M/L modules integrate motor drivers | UNKNOWN | `kritva-actuator` data |
| Safety requirements | TBD: safeguards, power-off behaviour, people nearby | Owner decision (CREQ-016) |
| Service access | TBD | `ARCHITECTURE.md` follow-up (CREQ-015) |
| Study-level IDs (FREQ, U) | TBD | Check `feasibility/REQUIREMENTS_REGISTER.md` |

## 6. HOLD D-003

Requirements definition and paper analysis only. CAD, final BOM, quotations, procurement, fabrication, assembly and physical testing remain NOT STARTED and require explicit owner decision. This template does not authorize implementation.
