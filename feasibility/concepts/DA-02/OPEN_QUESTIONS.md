# DA-02 — Open Questions and Dependencies

| Property | Value |
|---|---|
| Document ID | KMECH-OQ-DA-02 |
| Repository | `KritvaOS/kritva-mechanical` |
| Document Type | Open Questions Register |
| Status | PROPOSED |
| Owner | Dinesh |
| Assigned Intern | INTERN-02 |
| Version | 0.2.1 |
| Last Updated | 2026-11-26 |
| Authority | Feasibility tracking; subject to owner review |
| Related Documents | `README.md`, `REQUIREMENTS.md`, `ARCHITECTURE.md`, `feasibility/REQUIREMENTS_REGISTER.md`, `feasibility/RISK_REGISTER.md` |

## 1. Purpose

Track missing inputs, unresolved assumptions, dependencies and owner decisions for DA-02 (Humanoid Torso Dual-Arm). Nothing here approves a value. Risk register IDs are `RISK-TBD` until the register is checked. In this document "printed" means printed on the concept artwork sheets; 3D-printed parts are written "3D-printed".

**Status terms used in this register** (`INCOMPLETE` and `BLOCKED` are as used in `feasibility/README.md`; the definitions below were written for this register): `UNKNOWN` = no value or source exists; `TBD` = a decision or value is pending; `INCOMPLETE` = partial data exists but is not enough; `BLOCKED` = waiting on an external input that this study cannot supply, such as `kritva-actuator` data.

## 2. Open Questions

| ID | Question / missing input | Category | Status | Impact | Required action / dependency | Owner |
|---|---|---|---|---|---|---|
| OQ-001 | Shoulder-to-shoulder spacing (D5): 600 mm is on the concept sheet only and looks inconsistent with a 300 mm torso width, 800 mm overall width and 350 mm reach. Also confirm what the sheet's 300 mm refers to: the README lists it as torso width, while torso height 300 mm is a separate intern assumption (OQ-008). Results that depend on D5 are valid only for the D5 case. | Technical | INCOMPLETE | High | Owner to clarify what each width refers to | Dinesh |
| OQ-002 | Required payload, reach and target mass (printed 0.1 – 0.2 kg, 350 mm and 8 – 12 kg). Printed values are CONCEPT_TARGET with no stated basis. | Data | UNKNOWN | High | Owner decision (CREQ-006 to CREQ-008) | Dinesh |
| OQ-003 | `kritva-actuator` source, revision and maturity, and the joint to S/M/L mapping. | Data | BLOCKED | High | Owner to supply traceable data (CREQ-009, CREQ-010) | Dinesh |
| OQ-004 | Joint ranges, speeds and duty cycle (90 °/s and 10 rad/s² are intern assumptions). | Technical | TBD | High | Owner input or confirmation of intern proposal | Dinesh / INTERN-02 |
| OQ-005 | Base fixing method (including whether the base is free-standing) and acceptable stability margin with arms extended. | Technical / safety | TBD | High | Owner decision (CREQ-013) | Dinesh |
| OQ-006 | Safety approach: pinch protection, power-off arm droop, holding strategy (brake or self-locking), emergency stop. | Safety | TBD | High | Owner decision (CREQ-016) | Dinesh |
| OQ-007 | Head pan fitted or not (the D6 count is resolved: 8 baseline, 9 with head, 2026-10-31), and powered or passive grippers. | Technical | TBD | Medium | Owner decision (CREQ-003, CREQ-004) | Dinesh |
| OQ-008 | Shoulder height and torso height (280 mm and 300 mm are intern assumptions); shoulder yaw and pitch axis offset. | Technical | TBD | Medium | Owner to confirm; intern to sketch | Dinesh / INTERN-02 |
| OQ-009 | Interface list, Kritva Edge dimensions, EtherCAT provisions, and whether S/M/L modules integrate drivers. | Technical / data | UNKNOWN | Medium | Create `INTERFACES.md`; owner to supply data (CREQ-012) | Dinesh / INTERN-02 |
| OQ-010 | Cost basis for Kritva Edge and S/M/L actuators, and component availability. | Cost / data | UNKNOWN | Medium | Owner to supply basis | Dinesh |
| OQ-011 | Housekeeping: stale "mast" wording in the earlier README (conflicts with resolved D3); `FREQ`/`U`/`RISK` IDs; CALC-DA02-01 to -03 are to be filed. | Documentation | TBD | Low | Owner confirms wording; intern updates IDs and files calculations | Dinesh / INTERN-02 |
| OQ-012 | Basis for the 20 N accidental tip load (an intern assumption used for margin checks). | Technical / safety | UNKNOWN | Medium | Owner to confirm or replace | Dinesh |
| OQ-013 | Self-collision limits: arm-to-arm and arm-to-torso envelopes and clearances. | Technical | TBD | Medium | Owner input; intern to define envelopes (CREQ-014) | Dinesh / INTERN-02 |
| OQ-014 | Verification criteria: what result counts as feasible for each CREQ (see 2.1 of `REQUIREMENTS.md`). | Process | TBD | Medium | Owner decision | Dinesh |
| OQ-015 | Applicable safety standards for a robot arm near people. | Safety | UNKNOWN | High | Owner to name standards, if any | Dinesh |
| OQ-016 | Review owner for CALC-DA02-01 to -03 once filed. | Process | TBD | Low | Owner to assign | Dinesh |
| OQ-017 | Power budget and cabling: supply current, harness routing through shoulders, wrist and neck. | Technical | UNKNOWN | Medium | Owner data; intern sketch (CREQ-011, CREQ-015) | Dinesh / INTERN-02 |
| OQ-018 | Camera mount: location, interface and field of view requirements for the head camera. | Technical | TBD | Low | Owner decision with OQ-007 | Dinesh |

## 3. Assumptions Requiring Confirmation

- Payload: UNKNOWN (calculations use 0.2 kg worst case)
- Reach: UNKNOWN (printed 350 mm; link split 175 / 100 / 75 mm assumed)
- Target mass: UNKNOWN (printed 8 – 12 kg has no stated basis; estimate 10.02 kg baseline, not a target)
- Joint torque and speed: TBD (shoulder pitch 2.64 N·m holding is the highest estimate)
- Actuator S/M/L mapping: BLOCKED (waiting on `kritva-actuator` data, OQ-003)
- Dimensions and interfaces: TBD (shoulder height 280 mm, torso height 300 mm assumed)
- Cost and component availability: UNKNOWN
- Other assumptions: vertical yaw axis and horizontal pitch axes; 20 N accidental load for margin checks; free-standing base

## 4. Owner Decisions Required

| Decision | Reason | Related requirement / risk | Status |
|---|---|---|---|
| Clarify shoulder spacing (D5) | Affects mounts, stability, arm overlap | OQ-001; CREQ-005, CREQ-006; RISK-TBD | OWNER DECISION REQUIRED |
| Set payload, reach and mass values | Still UNKNOWN in the register | OQ-002; CREQ-006 to CREQ-008 | OWNER DECISION REQUIRED |
| Supply actuator source data and S/M/L approach | Blocks actuator compatibility | OQ-003; CREQ-009, CREQ-010 | OWNER DECISION REQUIRED |
| Base fixing and safety approach | Thin tipping margin; arm droop and pinch hazards | OQ-005, OQ-006; CREQ-013, CREQ-016; RISK-TBD | OWNER DECISION REQUIRED |
| Head fitted and gripper actuation | Changes actuator count, mass and loads | OQ-007; CREQ-003, CREQ-004 | OWNER DECISION REQUIRED |

## 5. Disposition

| Item | Disposition | Evidence | Date |
|---|---|---|---|
| D1, D2, D3, D4 (height, base width, camera arrangement, head motion) | RESOLVED: sheets agree after regeneration | `README.md` §10 | 2026-10-31 |
| D6 actuator count | RESOLVED by owner: 8 baseline, 9 with head fitted | `README.md` §10 | 2026-10-31 |
| Head fitted or not | OPEN: see OQ-007 (separate from the D6 count) | `README.md` §10 | n/a |
| D5 shoulder-to-shoulder width | OPEN: see OQ-001 | `README.md` §10 | n/a |

## 6. HOLD D-003

Open questions tracking does not authorize CAD, final BOM, quotations, procurement, fabrication, assembly or physical testing. All remain NOT STARTED pending explicit owner decision under HOLD D-003.
