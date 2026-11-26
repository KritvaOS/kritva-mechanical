# DA-03 — Requirements

| Property | Value |
|---|---|
| Document ID | KMECH-REQ-DA-03 |
| Repository | `KritvaOS/kritva-mechanical` |
| Document Type | Concept Requirements |
| Status | PROPOSED |
| Owner | Dinesh |
| Assigned Intern | INTERN-02 |
| Version | 0.2.1 |
| Last Updated | 2026-11-26 |
| Authority | Proposed concept requirements; subject to owner review |
| Related Documents | `README.md`, `ARCHITECTURE.md`, `MECHANICAL_ANALYSIS.md`, `ACTUATOR_ANALYSIS.md`, `MASS_BUDGET.md`, `feasibility/REQUIREMENTS_REGISTER.md` |

These are **proposed** concept requirements drafted from the DA-03 artwork and the preliminary paper work. None is approved. Printed values are CONCEPT_TARGET (not requirements); unresolved values stay `UNKNOWN` or `TBD`. In this document "printed" means printed on the concept artwork sheets; 3D-printed parts are always written "3D-printed".

## 1. Scope

Concept ID/name: DA-03 — Mobile Dual-Arm

Intended application and demonstration objective: Kritva platform demonstration: compact tabletop-height mobile manipulation, pick-and-place, inspection and teleoperation (concept sheet). Indoor flat terrain; uneven terrain is a future extension only.

## 2. Requirements Register

Priority is the intern's proposal. Evidence type C = paper calculation, comparison or sketch.

| ID | Requirement | Source | Priority | Verification method | Evidence type | Status | Notes |
|---|---|---|---|---|---|---|---|
| CREQ-001 | The concept shall be a mobile dual-arm: a differential-drive base with four wheels (left pair, right pair, one drive channel per side), a fixed torso, and two symmetric arms of 3 DOF each (shoulder yaw, elbow pitch, wrist pitch). | Concept and cross-section sheets; `README.md` | High | Review | C | PROPOSED | D2 resolved by owner 2026-10-31. |
| CREQ-002 | The baseline shall have 8 actuators (6 arm and 2 base drive channels); grippers are counted separately. | Concept sheet; D2 | High | Review | C | PROPOSED | Gripper actuation optional, TBD. |
| CREQ-003 | Each arm shall carry a two-finger gripper; whether it is powered shall be an owner decision. | Both sheets | Medium | Review / calculation | C | PROPOSED | |
| CREQ-004 | The concept shall allow an optional sensor mast with an RGB-D or stereo camera; whether the mast is height-adjustable shall be an owner decision. | Both sheets; D6 | Low | Review | C | PROPOSED | |
| CREQ-005 | Whether LiDAR is in the baseline sensor set shall be an owner decision, and an IMU space shall be kept. | Concept sheet; D4 | Medium | Review | C | PROPOSED | LiDAR not drawn on the cross-section. |
| CREQ-006 | The study shall assess the concept against the printed envelope (800 mm overall width, 400 mm × 450 mm base, 650 mm height with mast). | Both sheets (CONCEPT_TARGET) | Medium | Review / calculation | C | PROPOSED | Width cannot be reconciled with reach and torso (D5). |
| CREQ-007 | The study shall define each arm's workspace, the working height range, the overlap zone and the orientation limits of a 3-DOF arm. | `MECHANICAL_ANALYSIS.md` §4 | High | Calculation / sketch | C | PROPOSED | Reach UNKNOWN; printed 350 mm is CONCEPT_TARGET. |
| CREQ-008 | The study shall assess the printed payload per arm and state its location. | Concept sheet (CONCEPT_TARGET) | High | Calculation | C | PROPOSED | Payload UNKNOWN. |
| CREQ-009 | The study shall provide a mass estimate by subsystem, kept separate from the printed 12 – 18 kg. | `MASS_BUDGET.md` | Medium | Calculation | C | PROPOSED | Estimate 15.72 kg; not a target. |
| CREQ-010 | Each arm joint's torque, speed and range shall be derived independently, and compared with S/M/L data once supplied. The elbow reference values shall not be copied to other joints. | `ACTUATOR_ANALYSIS.md` | High | Calculation | C | PROPOSED | S/M/L mapping not started. |
| CREQ-011 | Wheel drive torque and speed shall be derived for a stated mass, slope, acceleration, tyre and floor, including turning in place with paired wheels. | `ACTUATOR_ANALYSIS.md` §2 | High | Calculation | C | PROPOSED | Scrub dominates turning. |
| CREQ-012 | Static tipping margin shall be assessed with arms extended, on a slope and under accidental load, and base geometry stated. | `MECHANICAL_ANALYSIS.md` §4 | High | Calculation | C | PROPOSED | Dynamic effects not computed. |
| CREQ-013 | The study shall investigate 24 V DC from a 24 V Li-ion pack as the power direction; 24 V is not a requirement, capacity, protection and charging are TBD, and energy and runtime shall be estimated on paper. | Both sheets | High | Calculation | C | PROPOSED | Investigation only. No battery safety assessment in this study. |
| CREQ-014 | The base and torso shall be assessed for housing the battery, two drive drivers, six arm drivers, Kritva Edge and the power board, and the interface list shall be defined. | Cross-section sheet | High | Sketch / review | C | PROPOSED | EtherCAT provisions not shown (TBD). |
| CREQ-015 | Cable routing for a moving base shall be listed with strain relief, connector retention and vibration concerns. | Cross-section sheet; `README.md` §8 | Medium | Sketch / review | C | PROPOSED | |
| CREQ-016 | Safety hazards (emergency stop, pinch, moving-base collision, battery, arm droop on power loss) shall be identified as open items; no safeguard is selected. | `MECHANICAL_ANALYSIS.md` §6 | High | Review | C | PROPOSED | A red button appears on the concept render but is not labelled. |
| CREQ-017 | Work shall remain paper-based under HOLD D-003. | HOLD D-003 | High | Review | C | PROPOSED | Study process constraint, not a product requirement; kept here for traceability and a candidate to move to the study constraints (ID not changed). |

### 2.1 Acceptance Criteria (proposed)

Added for the requirements that had none. All thresholds are `TBD, owner decision`; no value is invented here. A criterion is met only when the result is filed, reproducible and reviewed by the owner.

| ID | Acceptance criterion | Threshold |
|---|---|---|
| CREQ-007 | The workspace result states the joint ranges used, the working height range, the overlap zone and the orientation limits, and can be reproduced from CALC-DA03-03 (to be filed). | Required reach, working height and joint ranges: TBD, owner decision |
| CREQ-008 | The payload value and its location are stated, and the joint torques can be reproduced from CALC-DA03-01 (to be filed). | Required payload: TBD, owner decision |
| CREQ-010 | Each arm joint has a torque, speed and range entry with its own stated payload and pose, none copied from the elbow reference, and a comparison against S/M/L data once supplied. | Torque, speed, range and duty margins: TBD, owner decision |
| CREQ-011 | Wheel drive torque and speed are stated for a stated mass, slope, acceleration, tyre and floor, including turning in place. | Required speed, slope and acceleration: TBD, owner decision |
| CREQ-012 | The tipping result covers arms extended, a slope and accidental load, with the base geometry stated, and dynamic cases are listed as not computed or computed. | Minimum acceptable stability margin: TBD, owner decision |

## 3. Assumptions and Constraints

- Payload: UNKNOWN (printed 0.1 – 0.2 kg per arm, CONCEPT_TARGET)
- Reach: UNKNOWN (printed 350 mm, CONCEPT_TARGET)
- Target mass: UNKNOWN (printed 12 – 18 kg, CONCEPT_TARGET)
- Joint torque and speed: TBD (estimates exist in `ACTUATOR_ANALYSIS.md`, not requirements)
- Power direction: 24 V DC, investigation only (not a requirement)
- Actuator direction: BLDC/PMSM, S/M/L; compatibility TBD
- Other constraints: indoor flat terrain; runtime UNKNOWN; battery capacity UNKNOWN; evidence type C only; the elbow reference of 24 V, 10 N·m continuous and 20 N·m peak is not a universal specification.

## 4. Requirement Traceability

Study-level IDs (`FREQ-xxx`) and open items (`U-xxx`) are taken from `feasibility/REQUIREMENTS_REGISTER.md` only where an entry is a clear match. Entries with no clear match stay `FREQ-TBD` or `U-TBD`. No ID was invented.

| Requirement | Related FREQ / open item | Concept-specific evidence |
|---|---|---|
| CREQ-001, -002 | FREQ-026; D2 resolved | `ARCHITECTURE.md` §3 |
| CREQ-003, -004, -005 | CREQ-003: FREQ-028; CREQ-004, -005: FREQ-TBD; D4, D6 | `ARCHITECTURE.md` §2 |
| CREQ-006, -007 | CREQ-006: FREQ-TBD, U-002; CREQ-007: FREQ-026, U-005; D5 | CALC-DA03-03 |
| CREQ-008, -010 | CREQ-008: FREQ-020, U-004; CREQ-010: FREQ-012, FREQ-013, U-007 | CALC-DA03-01 |
| CREQ-009 | FREQ-019; U-003 | CALC-DA03-02 |
| CREQ-011, -013 | CREQ-011: FREQ-012, U-007; CREQ-013: FREQ-011; U-TBD (battery) | CALC-DA03-01 |
| CREQ-012 | FREQ-027 | CALC-DA03-03 |
| CREQ-014, -015 | CREQ-014: FREQ-021, FREQ-022, FREQ-025; CREQ-015: FREQ-024; U-TBD (interfaces) | `ARCHITECTURE.md` §4 |
| CREQ-016, -017 | CREQ-016: FREQ-018; CREQ-017: FREQ-002; HOLD D-003 | `MECHANICAL_ANALYSIS.md` §6 |

CALC-DA03-01, -02 and -03 are referenced and still to be filed in `calculations/`.

## 5. Open Requirements

| Item | Missing information | Dependency / action |
|---|---|---|
| Payload, reach, mass, runtime | UNKNOWN | Owner decision |
| Working height and shoulder height | TBD: required work surface height | Owner decision; CREQ-007 |
| Reach, width and shoulder spacing (D5) | INCOMPLETE: not verifiable from the sheets | Owner to clarify |
| Wrist terminology (D3), LiDAR (D4), torso width and mast (D6) | TBD | Owner decision |
| Joint and wheel S/M/L mapping | BLOCKED: no `kritva-actuator` data | Owner to supply |
| Battery capacity, protection, charging | TBD | Owner decision; CREQ-013 |
| Wheel, tyre, floor and speed data | TBD | Owner input; CREQ-011 |
| Interface list and EtherCAT | TBD | `INTERFACES.md` |
| Safety requirements | TBD | Owner decision; CREQ-016 |

## 6. HOLD D-003

Requirements definition and paper analysis only. CAD, final BOM, quotations, procurement, fabrication, assembly and physical testing remain NOT STARTED and require explicit owner decision. This template does not authorize implementation.
