# QR-04 — README section updates for Week 2

Apply only numbered sections 11, 13, 14, 15 and 16 in the existing concept README. Preserve all other sections, IDs, artwork references and version history. Review the diff before committing.

## 11. Feasibility Activity

Week 1 reference-study work and Week 2 architecture work are documented in the linked concept files. Week 2 scope is preliminary mechanical configuration, dimensions, joint layout, interfaces and mass assumptions.

- Architecture and configuration: `ARCHITECTURE.md`.
- Preliminary mechanical assessment, load paths, workspace/stability/stiffness/serviceability questions: `MECHANICAL_ANALYSIS.md`.
- Per-joint torque/speed/ROM/duty/S/M/L fields: `ACTUATOR_ANALYSIS.md`; all unavailable values remain `TBD` pending Week 3 inputs.
- Interface inventory and conceptual Kritva platform space provisions: `INTERFACES.md`.
- Published weight target isolated from unsupported subsystem mass contributions: `MASS_BUDGET.md`.
- Conceptual sketch: `sketches/WEEK2_CONCEPT_SKETCH.svg` (not to scale; not CAD).
- DOF and calculation readiness: `calculations/WEEK2_ARCHITECTURE_CHECKS.md`.
- Source traceability: `references/SOURCE_REGISTER.md`.
- Open questions and qualitative risks: `OPEN_QUESTIONS.md`.

No torque/speed, structural strength, stability, S/M/L compatibility, mass breakdown or cost result is claimed unless a traceable calculation is added. No simulation, bench or physical evidence is claimed. Mechanical HOLD D-003 remains active.

## 13. Folder Contents

| File / folder | Purpose | Week 2 status |
|---|---|---|
| `README.md` | Existing concept overview and study tracking | Sections 11 and 13–16 proposed for update |
| `REQUIREMENTS.md` | Concept requirements, assumptions and unknowns | Retain Week 1 register; update only if traceable |
| `ARCHITECTURE.md` | Configuration, dimension schedule, joints, DOF and assemblies | Updated for Week 2 |
| `MECHANICAL_ANALYSIS.md` | Load paths, workspace, stability, stiffness, serviceability | Preliminary qualitative assessment; calculations incomplete |
| `ACTUATOR_ANALYSIS.md` | Every joint's torque/speed/ROM/duty/S-M-L status | Joint instances listed; unavailable values marked TBD |
| `INTERFACES.md` | Mechanical, compute, power, sensors, communication and cable provisions | Concept-level inventory; detailed interfaces TBD |
| `MASS_BUDGET.md` | Mass assumptions and subsystem budget | Target transcribed; component contributions TBD |
| `COST_MODEL.md` | Preliminary cost categories | Week 3 activity; no prices/quotes |
| `OPEN_QUESTIONS.md` | Decisions, unknowns, dependencies and risks | Updated for Week 2 |
| `calculations/` | Calculation notes | `WEEK2_ARCHITECTURE_CHECKS.md`; no unsupported loads calculated |
| `references/` | Source register | `SOURCE_REGISTER.md` |
| `reviews/` | Concept-level review record | `WEEK2_CONCEPT_REVIEW.md`; not reviewed |
| `sketches/` | Paper sketches only | `WEEK2_CONCEPT_SKETCH.svg`; not CAD |

No `cad/` directory is permitted under HOLD D-003.

## 14. Current Assessment

**Week 2 state: IN_PROGRESS / NOT_REVIEWED.** The concept's mechanical configuration, available dimensions, joint instances, major assemblies, conceptual interfaces, published mass target and initial mechanical concerns are documented in the linked files. Every artwork quantity remains `CONCEPT_TARGET`; every unsupported joint range, torque, speed, mass contribution, interface dimension and centre-of-mass value remains TBD/UNKNOWN.

Concept-specific configuration: Four symmetric long-leg assemblies on a central rigid body; three joints per leg: hip abduction/adduction, hip flexion/extension and knee flexion/extension. Baseline is 12 actuators. No ankle or foot actuator is in the current baseline. Feet are conceptually rubber/PU or interchangeable rubber/TPU; optional top RGB-D/IMU sensor module is height adjustable in the cross-section only. The cross-section also shows an indicative 4 × M5 / 2 × Ø5 mm dowel body mounting interface that requires owner review.

Open artwork / owner decisions: Confirm disposition of cross-section-only 4 × M5 / 2 × Ø5 mm dowel body mount.

The preliminary mechanical assessment is qualitative. No strength, stiffness, stability, gait, workspace, collision, actuator compatibility or budget compliance has been proven.

## 15. Checkpoint Progress

| Week 2 item | Status | Evidence |
|---|---|---|
| Mechanical configuration | IMPLEMENTED IN OVERLAY; review pending | `ARCHITECTURE.md` |
| Available dimensions with units and source labels | IMPLEMENTED IN OVERLAY; owner review pending | `ARCHITECTURE.md` section 2 |
| DOF and joint instance mapping | IMPLEMENTED IN OVERLAY; ROM/frames TBD where absent | `ARCHITECTURE.md`, `ACTUATOR_ANALYSIS.md` |
| Major assemblies and conceptual interfaces | IMPLEMENTED IN OVERLAY; not released | `ARCHITECTURE.md`, `INTERFACES.md` |
| Preliminary mechanical assessment | IMPLEMENTED QUALITATIVELY; calculations incomplete | `MECHANICAL_ANALYSIS.md` |
| Mass assumptions | IMPLEMENTED AS TRACEABILITY / UNKNOWN REGISTER; no component mass estimate | `MASS_BUDGET.md` |
| Sketch | IMPLEMENTED IN OVERLAY; schematic only | `sketches/WEEK2_CONCEPT_SKETCH.svg` |
| CP2 contribution | DRAFTED for INTERN-01 concept only | `feasibility/interns/INTERN-01/CP2_CONTRIBUTION.md` |
| Week 3 torque/speed, structure, stability, mass and cost calculations | NOT STARTED / TBD | Requires source inputs and Week 3 work |
| Owner/reviewer acceptance | NOT RUN | Requires review against exact repository commit |

## 16. Open Decisions

See `OPEN_QUESTIONS.md` for the full concept-specific decision and dependency register. Key unresolved items:

- **OWNER_DECISION:** Confirm disposition of cross-section-only 4 × M5 / 2 × Ø5 mm dowel body mount.
- **OWNER_DECISION:** Confirm whether the cross-section-only adjustable sensor module is part of the baseline and whether it carries RGB-D plus IMU.
- **TBD:** Define leg link lengths, joint offsets/frames, joint ranges, standing pose, gait geometry and foot trajectory.
- **UNKNOWN:** Define representative terrain, friction/contact, body mass distribution, payload, gait/stride, speed and duty cycle.
- **UNKNOWN:** Battery location/capacity/protection/charging; concept sheet mentions space, cross-section does not show battery.
- **UNKNOWN:** Cooling path, compute/driver envelope and actuator mounting specifications.

All joint ROM, coordinate frames, torque, speed, duty cycle, actuator S/M/L mapping, interface datums/tolerances, subsystem masses, centre of mass, component costs and any unreported geometry remain TBD/UNKNOWN. These are not silently replaced with assumed values. D-003 remains active.
