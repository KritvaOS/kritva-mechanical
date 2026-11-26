# QR-01 — Requirements

| Property | Value |
|---|---|
| Document ID | KMECH-REQ-QR-01 |
| Repository | `KritvaOS/kritva-mechanical` |
| Document Type | Concept Requirements |
| Status | PROPOSED |
| Owner | Dinesh |
| Assigned Intern | INTERN-02 |
| Version | 0.2.0 |
| Last Updated | 2026-11-25 |
| Authority | Proposed concept requirements; subject to owner review |
| Related Documents | `README.md`, `ARCHITECTURE.md`, `MECHANICAL_ANALYSIS.md`, `ACTUATOR_ANALYSIS.md`, `MASS_BUDGET.md`, `feasibility/REQUIREMENTS_REGISTER.md` |

These are **proposed** concept requirements drafted from the QR-01 artwork and the preliminary paper work. None is approved. Printed values are CONCEPT_TARGET (not requirements); unresolved values stay `UNKNOWN` or `TBD`.

## 1. Scope

Concept ID/name: QR-01 — Compact Quadruped

Intended application and demonstration objective: Kritva platform demonstration: standing, sitting, slow walking and basic locomotion on indoor and outdoor flat terrain (concept sheet).

## 2. Requirements Register

Priority is the intern's proposal. Evidence type C = paper calculation, comparison or sketch.

| ID | Requirement | Source | Priority | Verification method | Evidence type | Status | Notes |
|---|---|---|---|---|---|---|---|
| CREQ-001 | The concept shall be a compact quadruped: four symmetric legs on a rigid body, two DOF per leg (hip and knee flexion/extension in one plane), 8 actuators in total. | Both sheets; `README.md` | High | Review | C | PROPOSED | D1 resolved 2026-10-31. |
| CREQ-002 | Each leg shall end in a replaceable foot pad (rubber or TPU); spike or custom feet and foot force sensing are options for the owner to decide. | Both sheets | Low | Review | C | PROPOSED | |
| CREQ-003 | An optional top sensor module (camera) shall be possible; whether IMU and LiDAR are in the baseline shall be an owner decision. | Both sheets; D6 | Medium | Review | C | PROPOSED | LiDAR and IMU on the concept sheet only. |
| CREQ-004 | The study shall assess the concept against the printed size (body 300 mm × 250 mm × 200 mm; overall 420 mm × 400 mm) and explain how leg mounting gives the overall width. | Both sheets (CONCEPT_TARGET) | Medium | Review / calculation | C | PROPOSED | Overall width exceeds body width by 150 mm. |
| CREQ-005 | The study shall assess the printed weight target and payload per the owner's resolved values, and state the payload mounting position. | Concept sheet (CONCEPT_TARGET); D4 | High | Calculation | C | PROPOSED | Weight and payload UNKNOWN. |
| CREQ-006 | The study shall define the leg kinematics, joint ranges, foot workspace and stride for standing, sitting and slow walking. | `MECHANICAL_ANALYSIS.md` §5 | High | Sketch / calculation | C | PROPOSED | Link lengths not printed. |
| CREQ-007 | Each joint's torque, speed and range shall be derived independently for stated poses and loads, and compared with S/M/L data once supplied. The elbow reference values shall not be copied. | `ACTUATOR_ANALYSIS.md` | High | Calculation | C | PROPOSED | S/M/L mapping not started. |
| CREQ-008 | Static stability shall be assessed for standing and for a crawl gait with a stated stride, with the lack of lateral foot motion recognised. | `MECHANICAL_ANALYSIS.md` §5 | High | Calculation | C | PROPOSED | Dynamic gaits not assessed. |
| CREQ-009 | The study shall provide a mass estimate by subsystem, kept separate from the printed 2.5 – 4 kg. | `MASS_BUDGET.md` | Medium | Calculation | C | PROPOSED | Estimate about 6.3 kg; not a target. |
| CREQ-010 | The power direction shall be 24 V DC (investigation only) with 5 V and 12 V rails; battery capacity, placement, protection and charging are TBD, and runtime shall be estimated on paper. | Both sheets | High | Calculation | C | PROPOSED | No battery is drawn on the cross-section. |
| CREQ-011 | The body shall be assessed for housing Kritva Edge, motor drivers, the power board and the battery, and cooling shall be considered. | Cross-section sheet; `ARCHITECTURE.md` §4 | High | Sketch / review | C | PROPOSED | Cooling UNKNOWN. |
| CREQ-012 | The cable path through each hip, thigh and shank shall be listed with bend, twist and fatigue concerns. | Cross-section sheet; `README.md` §8 | Medium | Sketch / review | C | PROPOSED | No harness design implied. |
| CREQ-013 | Foot-ground contact (traction, impact, damping) shall be identified as an open item for flat indoor and outdoor terrain. | `MECHANICAL_ANALYSIS.md` §5 | Medium | Calculation / review | C | PROPOSED | Terrain data not given. |
| CREQ-014 | Safety hazards (falls, collapse on power loss, pinch at hip and knee, battery, emergency stop) shall be identified as open items; no safeguard is selected. | `MECHANICAL_ANALYSIS.md` §6 | High | Review | C | PROPOSED | No emergency stop is shown on either sheet. |
| CREQ-015 | Work shall remain paper-based under HOLD D-003. | HOLD D-003 | High | Review | C | PROPOSED | Constraint on the study. |

## 3. Assumptions and Constraints

- Payload: UNKNOWN (printed 0.3 – 0.8 kg, CONCEPT_TARGET)
- Reach: UNKNOWN (not applicable as an arm reach; leg workspace TBD)
- Target mass: UNKNOWN (printed 2.5 – 4 kg, CONCEPT_TARGET)
- Joint torque and speed: TBD (estimates exist in `ACTUATOR_ANALYSIS.md`, not requirements)
- Power direction: 24V DC investigation only
- Actuator direction: BLDC/PMSM, S/M/L; compatibility TBD
- Other constraints: planar 2-DOF legs only; flat indoor and outdoor terrain; runtime UNKNOWN; evidence type C only; the elbow reference of 24 V, 10 N·m continuous and 20 N·m peak is not a universal specification.

## 4. Requirement Traceability

`FREQ-xxx` and `U-xxx` IDs are TBD because `feasibility/REQUIREMENTS_REGISTER.md` was not available for this draft.

| Requirement | Related FREQ / open item | Concept-specific evidence |
|---|---|---|
| CREQ-001, -002, -003 | FREQ-TBD; D1 resolved, D6 open | `ARCHITECTURE.md` §2, §3 |
| CREQ-004 | FREQ-TBD | `ARCHITECTURE.md` §1 |
| CREQ-005, -009 | FREQ-TBD; D4 | CALC-QR01-02 |
| CREQ-006, -008 | FREQ-TBD; U-TBD (link lengths) | CALC-QR01-03 |
| CREQ-007 | FREQ-TBD | CALC-QR01-01 |
| CREQ-010, -011, -012 | FREQ-TBD; U-TBD (battery) | `ARCHITECTURE.md` §4 |
| CREQ-013, -014, -015 | FREQ-TBD; HOLD D-003 | `MECHANICAL_ANALYSIS.md` §5, §6 |

CALC-QR01-01, -02 and -03 are referenced and still to be filed in `calculations/`.

## 5. Open Requirements

| Item | Missing information | Dependency / action |
|---|---|---|
| Weight, payload and size targets | UNKNOWN | Owner decision (D4) |
| Sensor baseline (D6) | OPEN | Owner decision |
| Leg link lengths, hip height and joint ranges | TBD | Owner input or confirmation of intern proposal |
| Joint S/M/L mapping | BLOCKED: no `kritva-actuator` data | Owner to supply |
| Battery capacity, placement, protection, charging | TBD | Owner decision |
| Gait, turning and terrain expectations | TBD | Owner decision |
| Cooling and thermal limits | UNKNOWN | Owner / data |
| Interface list and EtherCAT | TBD | `INTERFACES.md` |
| Safety requirements | TBD | Owner decision |

## 6. HOLD D-003

Requirements definition and paper analysis only. CAD, final BOM, quotations, procurement, fabrication, assembly and physical testing remain NOT STARTED and require explicit owner decision. This template does not authorize implementation.
