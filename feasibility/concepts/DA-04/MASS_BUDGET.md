# DA-04 — Week 2 Mass Assumptions and Budget Framework

**Status:** PROPOSED — paper feasibility study; subject to owner review.

**HOLD:** Mechanical HOLD D-003 remains active.

**Evidence boundary:** Week 2 architecture documentation and preliminary mechanical assessment. No CAD, simulation, bench or physical evidence is claimed.

**Numeric classification:** Artwork values are `CONCEPT_TARGET`; unsupported quantities remain `TBD`/`UNKNOWN`; any qualitative rating is `ESTIMATE`.

## 1. Artwork mass target (not a derived mass estimate)

**Published target:** 25–35 kg printed target range (marked est.) on concept sheet; provenance remains CONCEPT_TARGET and no derivation is supplied.

This is a transcribed artwork target. Although the sheet prints `(est.)`, the repository requires source values to remain distinguished from independently derived estimates. No subsystem mass estimate has been calculated in this Week 2 document. The printed target is not a verified mass, requirement or acceptance limit.

## 2. Subsystem mass structure

| Subsystem category | Mass contribution | Reason / missing input |
|---|---|---|
| Primary chassis / base / torso | TBD | Geometry, material/grade and section thickness absent |
| Arms or leg links | TBD | Link lengths, cross-sections, material and process not selected |
| Joint modules, motors and gearboxes | TBD | S/M/L selection and source-controlled actuator mass unavailable |
| Wheels / feet / end effectors | TBD | Wheel/foot/gripper detail and component mass not established |
| Compute and motor controllers | TBD | Board models, outlines and masses unavailable |
| Power distribution / protection | TBD | Electrical architecture and component data unavailable |
| Battery | TBD / UNKNOWN | Concept-dependent: see specific note below |
| Sensors and mounting hardware | TBD | Optional modules and model selections unresolved |
| Harnesses, fasteners, bearings and covers | TBD | Routing, quantity and component specifications absent |

No allocation percentages or component masses are invented. The total mass remains `UNKNOWN` until traceable component masses or defensible geometry/material estimates are available.

## 3. Mass model to populate in Week 3

`m_total = m_structure + m_links + m_joint_modules + m_wheels_or_feet + m_end_effectors + m_compute + m_drivers + m_power + m_battery + m_sensors + m_harness + m_fasteners + m_covers`

The centre-of-mass location must be calculated from component masses and positions relative to a defined datum. No datum or subsystem coordinates are available, so `CG_x`, `CG_y`, `CG_z` and mass moments are `UNKNOWN`.

## 4. Concept-specific mass assumptions / unknowns

Battery not drawn or labelled; README explicitly says battery sizing is not part of this study. Unknown whether the printed range includes battery, fixed head/camera, optional sensors, grippers, all wheels/drives, cable harness and fasteners. Component masses and centre of mass are absent.

## 5. Required inputs

- Current concept geometry and datum/coordinate frame.
- Material and manufacturing options narrowed only when there is source evidence; no final selection.
- Component masses from the owning actuator/platform repositories with source commit/revision and maturity.
- Count and envelope of all baseline and optional components.
- Whether target mass includes battery, payload, cables, fasteners and sensors.
- Payload and its location relative to joint/body datums.
- Uncertainty ranges and confidence basis for every independently estimated contribution.

## 6. Status and next action

**Status:** INCOMPLETE for a numerical mass budget; Week 2 mass assumptions and missing inputs are recorded.

**Next action:** Collect the above inputs and create a subsystem-by-subsystem estimate with range, method, source and confidence in Week 3. Do not force the total to match the printed target.
