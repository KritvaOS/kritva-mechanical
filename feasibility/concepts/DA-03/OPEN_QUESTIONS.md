# DA-03 — Open Questions and Dependencies

| Property | Value |
|---|---|
| Document ID | KMECH-OQ-DA-03 |
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

Track missing inputs, unresolved assumptions, dependencies and owner decisions for DA-03 (Mobile Dual-Arm). Nothing here approves a value. Risk register IDs are `RISK-TBD` until the register is checked. In this document "printed" means printed on the concept artwork sheets; 3D-printed parts are always written "3D-printed".

**Status terms used in this register** (`INCOMPLETE` and `BLOCKED` are as used in `feasibility/README.md`; the definitions below match those in DA-02): `UNKNOWN` = no value or source exists; `TBD` = a decision or value is pending; `INCOMPLETE` = partial data exists but is not enough; `BLOCKED` = waiting on an external input that this study cannot supply, such as `kritva-actuator` data.

## 2. Open Questions

| ID | Question / missing input | Category | Status | Impact | Required action / dependency | Owner |
|---|---|---|---|---|---|---|
| OQ-001 | D5: 350 mm reach, 800 mm overall width and 800 mm total reach cannot be reconciled with a 300 mm torso. What do the widths refer to, and what is the shoulder spacing? The study assumes ±150 mm (S1), while the printed 800 mm overall width with 350 mm reach would imply a spacing near 100 mm; results that depend on spacing are valid only for the ±150 mm case. | Technical | INCOMPLETE | High | Owner to clarify | Dinesh |
| OQ-002 | Required payload, reach, weight and runtime. Printed values are CONCEPT_TARGET with no stated basis. | Data | UNKNOWN | High | Owner decision (CREQ-008, CREQ-009, CREQ-013) | Dinesh |
| OQ-003 | What work surface height must the robot serve ("tabletop-height")? The assumed gripper range is about 225 – 575 mm with no floor reach, and shoulder height is an assumption. | Technical | TBD | High | Owner decision (CREQ-007) | Dinesh |
| OQ-004 | `kritva-actuator` source, revision and maturity, and the S/M/L mapping of arm joints and wheel drives. | Data | BLOCKED | High | Owner to supply traceable data (CREQ-010, CREQ-011) | Dinesh |
| OQ-005 | Battery capacity, protection, charging and battery safety approach. Capacity is not stated on the sheets. | Data / safety | UNKNOWN | High | Owner decision (CREQ-013, CREQ-016) | Dinesh |
| OQ-006 | Wheel, tyre, gear ratio, floor friction, speed and slope targets, and the turning strategy (turning in place sets the drive size). | Technical | TBD | High | Owner input (CREQ-011) | Dinesh / INTERN-02 |
| OQ-007 | Safety approach: emergency stop (red button unlabelled), pinch and base collision protection, arm droop and roll-away on power loss. | Safety | TBD | High | Owner decision (CREQ-016) | Dinesh |
| OQ-008 | D3 wrist terminology (rotation or pitch), D4 LiDAR in the baseline, D6 torso width and adjustable mast. | Technical | TBD | Medium | Owner decision (CREQ-004, CREQ-005) | Dinesh |
| OQ-009 | Interface list, Kritva Edge dimensions, EtherCAT provisions, and whether S/M/L modules integrate drivers. | Technical / data | UNKNOWN | Medium | Create `INTERFACES.md`; owner to supply data (CREQ-014) | Dinesh / INTERN-02 |
| OQ-010 | Powered or passive grippers; joint ranges and duty; cost basis for Kritva Edge, actuators and battery. | Technical / cost | TBD | Medium | Owner decision or input | Dinesh |
| OQ-011 | Housekeeping: `FREQ`/`U`/`RISK` IDs; CALC-DA03-01 to -03 are to be filed. | Documentation | TBD | Low | Intern updates IDs and files calculations | INTERN-02 |
| OQ-012 | Basis for the 20 N accidental tip load (an intern assumption used for margin checks). | Technical / safety | UNKNOWN | Medium | Owner to confirm or replace | Dinesh |
| OQ-013 | Self-collision limits: arm-to-arm, arm-to-torso and arm-to-wheel envelopes and clearances. | Technical | TBD | Medium | Owner input; intern to define envelopes (CREQ-007) | Dinesh / INTERN-02 |
| OQ-014 | Verification criteria: what result counts as feasible for each CREQ (see 2.1 of `REQUIREMENTS.md`). | Process | TBD | Medium | Owner decision | Dinesh |
| OQ-015 | Applicable safety standards for a mobile robot with arms and a Li-ion battery. | Safety | UNKNOWN | High | Owner to name standards, if any | Dinesh |
| OQ-016 | Review owner for CALC-DA03-01 to -03 once filed. | Process | TBD | Low | Owner to assign | Dinesh |
| OQ-017 | Basis of the sideways tipping angle of about 41° in `MECHANICAL_ANALYSIS.md` §4: which arm pose? A check with the CoM at x = 0 gives about 44°. | Technical | UNKNOWN | Low | Author or owner to state the pose; document to be corrected or the basis added | Dinesh / INTERN-02 |

## 3. Assumptions Requiring Confirmation

- Payload: UNKNOWN (calculations use 0.2 kg worst case)
- Reach: UNKNOWN (printed 350 mm; link split 175 / 100 / 75 mm assumed)
- Target mass: UNKNOWN (estimate 15.72 kg, not a target)
- Joint torque and speed: TBD (elbow about 0.8 N·m, wrist about 0.2 N·m, wheel turning about 2.5 N·m per channel)
- Actuator S/M/L mapping: BLOCKED (waiting on `kritva-actuator` data, OQ-004)
- Dimensions and interfaces: TBD (shoulders at ±150 mm and 400 mm height; torso 250 mm deep and 300 mm tall; wheel contacts ±190 mm × ±150 mm)
- Cost and component availability: UNKNOWN
- Other assumptions: upper arm rigid and horizontal; 100 mm wheels; friction 0.5; 20 N accidental load; battery 10 Ah

## 4. Owner Decisions Required

| Decision | Reason | Related requirement / risk | Status |
|---|---|---|---|
| Clarify widths and shoulder spacing (D5) | Affects mounts, overlap and stability | OQ-001; CREQ-006, CREQ-007; RISK-TBD | OWNER DECISION REQUIRED |
| Set payload, reach, weight, runtime and work surface height | UNKNOWN in the register | OQ-002, OQ-003; CREQ-007 to CREQ-009, CREQ-013 | OWNER DECISION REQUIRED |
| Supply actuator source data and S/M/L approach | Blocks actuator compatibility | OQ-004; CREQ-010, CREQ-011 | OWNER DECISION REQUIRED |
| Battery and safety approach | Li-ion and moving-base hazards | OQ-005, OQ-007; CREQ-013, CREQ-016; RISK-TBD | OWNER DECISION REQUIRED |
| Resolve D3, D4 and D6 | Wrist, LiDAR, torso and mast definition | OQ-008; CREQ-004, CREQ-005 | OWNER DECISION REQUIRED |

## 5. Disposition

| Item | Disposition | Evidence | Date |
|---|---|---|---|
| D1 (no dimension or DOF disagreement) | NONE FOUND | `README.md` §10 | 2026-10-31 |
| D2 wheel arrangement | RESOLVED by owner: four wheels as two driven pairs, 2 base actuators | `README.md` §10 | 2026-10-31 |
| D3, D4, D6 | OPEN: see OQ-008 | `README.md` §10 | n/a |
| D5 reach and width | OPEN: see OQ-001 | `README.md` §10 | n/a |

## 6. HOLD D-003

Open questions tracking does not authorize CAD, final BOM, quotations, procurement, fabrication, assembly or physical testing. All remain NOT STARTED pending explicit owner decision under HOLD D-003.
