# DA-01 — Architecture and Mechanical Configuration (Week 2)

**Status:** PROPOSED — paper feasibility study; subject to owner review.

**HOLD:** Mechanical HOLD D-003 remains active.

**Evidence boundary:** Week 2 architecture documentation and preliminary mechanical assessment. No CAD, simulation, bench or physical evidence is claimed.

**Numeric classification:** Artwork values are `CONCEPT_TARGET`; unsupported quantities remain `TBD`/`UNKNOWN`; any qualitative rating is `ESTIMATE`.

| Field | Value |
|---|---|
| Concept | Fixed Tabletop Dual-Arm |
| Family / complexity | Dual-arm / Low |
| Assigned intern | INTERN-01 |
| Study checkpoint | Week 2 / CP2 contribution |
| Source artwork | `docs/images/KMECH-CONCEPT-DA-01.png`; `docs/images/KMECH-CROSS-SECTION-DA-01.png` |
| Architecture maturity | Preliminary concept interpretation; not an approved architecture |

## 1. Configuration

Two symmetric 3-DOF arms mounted on opposite sides of a fixed central base/torso enclosure and base plate. The central enclosure contains the conceptual compute, power-distribution and left/right motor-driver blocks. There is no mobile base. Two-finger parallel grippers are optional and may be passive or powered; powered-gripper motion is not part of the six-actuator baseline. The cross-section shows an optional adjustable camera mast; its inclusion in the baseline is not authorized.

The source artwork is illustrative, PROPOSED, maturity L0 and not to scale. The sheets are not CAD, manufacturing drawings or engineering evidence. The earlier concept README remains the primary transcribed record. This Week 2 update expands its architecture description and records unknowns; it does not approve dimensions or interfaces.

## 2. Published preliminary dimensions and targets

| Dimension / property | Published value | Source | Classification / note |
|---|---|---|---|
| Base plate / base dimensions (W × D) | 300 × 250 mm | Concept sheet and cross-section | CONCEPT_TARGET |
| Overall width, arm-to-arm | 700 mm | Concept sheet and cross-section | CONCEPT_TARGET |
| Overall height | 400 mm | Concept sheet and cross-section | CONCEPT_TARGET |
| Arm reach, each side, shoulder-to-gripper | 350 mm | Concept sheet | CONCEPT_TARGET; pose/datum not defined |
| Total reach, left-to-right | 700 mm | Concept sheet | CONCEPT_TARGET; pose/datum not defined |
| Torso width | 300 mm | Cross-section only | CONCEPT_TARGET; OWNER_DECISION / artwork discrepancy |
| Target payload, each arm | 0.1–0.2 kg (printed as est.) | Concept sheet | CONCEPT_TARGET; basis not provided |
| Target robot weight | 5–8 kg (printed as est.) | Concept sheet | CONCEPT_TARGET; basis not provided |
| Supply voltage | 24 V DC | Concept sheet | CONCEPT_TARGET; investigation direction only |
| Power rails | 24 V input; 5 V and 12 V rails | Cross-section | CONCEPT_TARGET; electrical specification TBD |

All artwork values remain `CONCEPT_TARGET`. They are not approved product requirements. Printed weight/payload values marked `(est.)` are recorded as printed targets only; they are not an independent estimate by INTERN-01. The artwork does not define a common origin, datum, coordinate frame, tolerance or pose for every dimension. Do not infer one.

## 3. Preliminary joint configuration and DOF

| Joint instance | Intended motion / label | DOF | ROM / angle limits | Actuator technology shown | Week 2 disposition |
|---|---|---|---|---|---|
| Left shoulder | Yaw / rotation | 1 | TBD — no approved range in source | BLDC/PMSM with gearbox, as shown | Baseline joint; torque/speed/S/M/L in ACTUATOR_ANALYSIS.md |
| Left elbow | Flexion / extension; cross-section labels pitch | 1 | TBD — no approved range in source | BLDC/PMSM with gearbox, as shown | Baseline joint; torque/speed/S/M/L in ACTUATOR_ANALYSIS.md |
| Left wrist | Rotation / pitch ambiguity; cross-section says pitch | 1 | TBD — no approved range in source | BLDC/PMSM with gearbox, as shown | Baseline joint; torque/speed/S/M/L in ACTUATOR_ANALYSIS.md |
| Right shoulder | Yaw / rotation | 1 | TBD — no approved range in source | BLDC/PMSM with gearbox, as shown | Baseline joint; torque/speed/S/M/L in ACTUATOR_ANALYSIS.md |
| Right elbow | Flexion / extension; cross-section labels pitch | 1 | TBD — no approved range in source | BLDC/PMSM with gearbox, as shown | Baseline joint; torque/speed/S/M/L in ACTUATOR_ANALYSIS.md |
| Right wrist | Rotation / pitch ambiguity; cross-section says pitch | 1 | TBD — no approved range in source | BLDC/PMSM with gearbox, as shown | Baseline joint; torque/speed/S/M/L in ACTUATOR_ANALYSIS.md |

**DOF / actuator count check:** 6 baseline joint/channel rows are documented. DOF arithmetic is concept-level only; it does not prove actuator performance, independent-control suitability, torque capacity, speed, thermal capability or S/M/L compatibility.

Optional or excluded elements: Optional powered grippers: one separate open/close channel per gripper (up to two additional channels if both are powered); not in baseline six. Optional camera mast / RGB-D or stereo camera; concept sheet also mentions IMU space. Camera mast adjustability appears on cross-section only.

Joint range, zero position, axis unit vectors, coordinate frames, hard stops, allowable speed, duty cycle, gear ratio and output interface details are `TBD` unless specified in the source. Do not infer axes from the rendered motor orientation.

## 4. Major assemblies and load-path context

| Assembly / subsystem | Current concept interpretation | Evidence status |
|---|---|---|
| Primary body / base | Two symmetric 3-DOF arms mounted on opposite sides of a fixed central base/torso enclosure and base plate. The central enclosure contains the conceptual compute, power-distribution and left/right motor-driver blocks. There is no mobile base. Two-finger parallel grippers are optional and may be passive or powered; powered-gripper motion is not part of the six-actuator baseline. The cross-section shows an optional adjustable camera mast; its inclusion in the baseline is not authorized. | Illustrative; not released |
| Joints / transmissions | Modular rotary joint housings; BLDC/PMSM motors, harmonic or planetary gearbox examples, output shaft and absolute/incremental encoder where shown. | Illustrative options; no specific model/ratio |
| Links / limbs | Concept-specific arms or legs; see concept artwork and material option register. | Illustrative; geometry not to scale |
| End effectors / feet | Optional powered grippers: one separate open/close channel per gripper (up to two additional channels if both are powered); not in baseline six. Optional camera mast / RGB-D or stereo camera; concept sheet also mentions IMU space. Camera mast adjustability appears on cross-section only. | Optional elements remain owner decision / TBD |
| Kritva platform space | Conceptual space only for relevant Kritva Edge compute/control, power distribution/protection, motor drivers, sensors and communication. | Board dimensions, connectors, thermal and cable limits TBD |

**Qualitative load path / preliminary mechanical considerations:** Primary load path: gripper/payload → wrist → forearm/link → elbow → upper arm/link → shoulder → central torso/base → base plate → tabletop/support. Preliminary assessment must examine extended-arm overturning/sliding, base support and stiffness, link/joint deflection, left/right workspace overlap and collision, payload/reach pose assumptions, gripper mounting, and access to the central enclosure. The README itself warns that 350 mm per-side reach, 700 mm total reach and 700 mm overall width do not describe one posture without a stated pose. Do not infer a pose or geometry.

## 5. Interface architecture

Fixed base plate to tabletop/support; central enclosure to base plate; shoulder module to central body; shoulder/elbow/wrist modules to arm links; distal wrist to optional gripper mount; optional mast mount to body; internal compute/power/driver mounting; left/right arm harness paths. Artwork labels USB, Ethernet and power cabling on the mast but no fieldbus. Preserve EtherCAT as a platform architecture direction where relevant, without inventing a DA-01 fieldbus implementation.

The interface breakdown is expanded in `INTERFACES.md`. Treat all interfaces as conceptual until a source-controlled drawing/specification exists and the relevant owner confirms it.

## 6. Material and process options (not selections)

Artwork shows a base plate in aluminium or steel; central enclosure; aluminium, CNC-machined or 3D-printed arm links; aluminium/CNC joint housings; harmonic or planetary gearbox examples; absolute or incremental encoder examples; rubber/TPU gripper pads. These are illustrative options, not selected materials or manufacturing processes.

The above are artwork options. No grade, heat treatment, layup, additive process, machining route, supplier or process capability is selected. Any later material comparison must cite source properties and distinguish handbook values from manufacturer data.

## 7. Cable routing and service access

Arm harnesses pass through shoulders, arm links and joints to wrist/gripper. Base routing passes through the base plate. Optional camera mast carries USB/Ethernet/power. Check bending, twist, pinch, service access and strain relief; no harness dimensions are supplied.

No cable harness design, connector selection, bend-radius value, routing dimensions or electrical design is created here. The study only reserves conceptual routes and records mechanical concerns.

## 8. Mass assumption boundary

5–8 kg printed target range (marked est.) on concept sheet; provenance remains CONCEPT_TARGET and no derivation is supplied.

Week 2 mass assumptions are documented in `MASS_BUDGET.md`. The published weight range has no supporting subsystem breakdown in the current concept material; do not distribute it among components or use it as verified mass. Centre of mass, mass moments and component masses remain `UNKNOWN` until traceable geometry/material/component sources are available.

## 9. Preliminary architecture assessment

- **Configuration identified:** Yes, at concept-artwork level.
- **Available dimensions transcribed:** Yes, with source and units; all remain `CONCEPT_TARGET`.
- **DOF/joint arrangement:** Counted and listed; axis frames and joint ranges remain incomplete where not specified.
- **Major assemblies/interfaces:** Identified conceptually; no released interface dimensions.
- **Mass assumptions:** Published target isolated from independently derived subsystem mass.
- **Mechanical assessment:** Qualitative only; structural/stability/clearance calculations carried to later analysis where inputs permit.
- **Open questions:** See `OPEN_QUESTIONS.md`.
- **Joint torque/speed and S/M/L:** Each joint listed in `ACTUATOR_ANALYSIS.md`; all values remain `TBD` pending Week 3 inputs.

## 10. CP2 status for this concept

| CP2 criterion | Contribution status | Evidence |
|---|---|---|
| CP2-02 Mechanical configuration | DOCUMENTED — draft | This file; concept sketch |
| CP2-03 DOF and joint configuration | DOCUMENTED — ranges/frames incomplete | Section 3; actuator matrix |
| CP2-04 Available dimensions with units | DOCUMENTED — source targets only | Section 2 |
| CP2-05 Major assemblies/interfaces | DOCUMENTED — conceptual | Sections 4–7; `INTERFACES.md` |
| CP2-06 Unknown specifications | DOCUMENTED | `OPEN_QUESTIONS.md`, `MASS_BUDGET.md`, `ACTUATOR_ANALYSIS.md` |
| CP2-07 Initial risks | DOCUMENTED — qualitative estimates | `OPEN_QUESTIONS.md` |

CP2-01 (all 12 concepts) and CP2-08 (team-wide assignment evidence) require the other two interns' contributions and reviewer consolidation. This file does not claim CP2 acceptance or task completion.

## 11. References

- Existing concept record: `feasibility/concepts/DA-01/README.md`
- Study plan: `feasibility/STUDY_PLAN.md` sections 4, 6, 8 and 9.1.
- Design guidelines: `feasibility/DESIGN_GUIDELINES.md` sections 2–7.
- Requirements: `feasibility/REQUIREMENTS_REGISTER.md` FREQ-002 to FREQ-034.
- Artwork index and manifest: `docs/images/ARTWORK_INDEX.md`; `docs/images/ARTWORK_MANIFEST.json`.
- Concept-specific source register: `references/SOURCE_REGISTER.md`.
