# DA-04 — README section updates for Week 2

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

Concept-specific configuration: Humanoid upper torso with fixed head, mounted on a differential-drive chassis. Two arms each have four baseline DOF (shoulder yaw, shoulder pitch, elbow pitch and wrist pitch). The base has two driven channels: left wheel pair and right wheel pair, with four physical wheels shown. The approved study baseline is 10 actuators (8 arm + 2 base); head pan is excluded and grippers are optional/not counted. A printed future path to five-DOF arms and an advanced mobile base is not part of the baseline.

Open artwork / owner decisions: Resolve README heading/name inconsistency: its title says 'Advanced Dual-Arm', while concept name and assignment say 'Humanoid Mobile Dual-Arm'. Do not change artwork brief sections 1–12 without authorization.

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

- **OWNER_DECISION:** Resolve README heading/name inconsistency: its title says 'Advanced Dual-Arm', while concept name and assignment say 'Humanoid Mobile Dual-Arm'. Do not change artwork brief sections 1–12 without authorization.
- **OWNER_DECISION:** Confirm whether printed future path (5-DOF arms/advanced base) must stay clearly excluded from current study baseline.
- **UNKNOWN:** Define representative arm poses/payload centres, joint ranges, speed and duty cycle.
- **UNKNOWN:** Wheel radius, track/wheelbase, wheel loading, floor friction, slope, acceleration and travel speed.
- **UNKNOWN:** Mass distribution/centre of mass and battery envelope; battery is not shown and sizing is explicitly out of scope.
- **OWNER_DECISION:** Confirm optional grippers and sensor set; cross-section camera/torso IMU vs concept camera/IMU/LiDAR space.
- **TBD:** Clarify geometry datum/pose for 1200 mm overall width, 600 mm shoulder spacing, 450 mm reach per side and 1200 mm total reach.

All joint ROM, coordinate frames, torque, speed, duty cycle, actuator S/M/L mapping, interface datums/tolerances, subsystem masses, centre of mass, component costs and any unreported geometry remain TBD/UNKNOWN. These are not silently replaced with assumed values. D-003 remains active.
