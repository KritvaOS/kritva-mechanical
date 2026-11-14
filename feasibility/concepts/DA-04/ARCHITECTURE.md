# DA-04 — Architecture and Mechanical Configuration (Week 2)

**Status:** PROPOSED — paper feasibility study; subject to owner review.

**HOLD:** Mechanical HOLD D-003 remains active.

**Evidence boundary:** Week 2 architecture documentation and preliminary mechanical assessment. No CAD, simulation, bench or physical evidence is claimed.

**Numeric classification:** Artwork values are `CONCEPT_TARGET`; unsupported quantities remain `TBD`/`UNKNOWN`; any qualitative rating is `ESTIMATE`.

| Field | Value |
|---|---|
| Concept | Humanoid Mobile Dual-Arm |
| Family / complexity | Dual-arm / High |
| Assigned intern | INTERN-01 |
| Study checkpoint | Week 2 / CP2 contribution |
| Source artwork | `docs/images/KMECH-CONCEPT-DA-04.png`; `docs/images/KMECH-CROSS-SECTION-DA-04.png` |
| Architecture maturity | Preliminary concept interpretation; not an approved architecture |

## 1. Configuration

Humanoid upper torso with fixed head, mounted on a differential-drive chassis. Two arms each have four baseline DOF (shoulder yaw, shoulder pitch, elbow pitch and wrist pitch). The base has two driven channels: left wheel pair and right wheel pair, with four physical wheels shown. The approved study baseline is 10 actuators (8 arm + 2 base); head pan is excluded and grippers are optional/not counted. A printed future path to five-DOF arms and an advanced mobile base is not part of the baseline.

The source artwork is illustrative, PROPOSED, maturity L0 and not to scale. The sheets are not CAD, manufacturing drawings or engineering evidence. The earlier concept README remains the primary transcribed record. This Week 2 update expands its architecture description and records unknowns; it does not approve dimensions or interfaces.

## 2. Published preliminary dimensions and targets

| Dimension / property | Published value | Source | Classification / note |
|---|---|---|---|
| Overall width, arm-to-arm | 1200 mm | Concept sheet and cross-section | CONCEPT_TARGET |
| Shoulder-to-shoulder spacing | 600 mm | Concept sheet | CONCEPT_TARGET |
| Total reach, left-to-right | 1200 mm | Concept sheet | CONCEPT_TARGET; pose/datum not defined |
| Torso width | 400 mm | Concept sheet and cross-section | CONCEPT_TARGET |
| Base dimensions (W × L) | 500 × 600 mm | Concept sheet and cross-section | CONCEPT_TARGET |
| Overall height with head | 1200 mm | Concept sheet and cross-section | CONCEPT_TARGET |
| Arm reach each side, shoulder-to-gripper | 450 mm | Concept sheet | CONCEPT_TARGET; pose/datum not defined |
| Target payload each arm | 0.5–1.0 kg (printed as est.) | Concept sheet | CONCEPT_TARGET; basis not provided |
| Target robot weight | 25–35 kg (printed as est.) | Concept sheet | CONCEPT_TARGET; basis not provided |
| Supply voltage | 24 V DC | Concept sheet and cross-section | CONCEPT_TARGET; investigation direction only |
| Power rails | 24 V input; 5 V and 12 V rails | Cross-section | CONCEPT_TARGET; electrical specification TBD |
| Battery | Not drawn or labelled; chemistry/capacity UNKNOWN | Neither sheet | NOT VERIFIABLE FROM CURRENT ARTWORK |

All artwork values remain `CONCEPT_TARGET`. They are not approved product requirements. Printed weight/payload values marked `(est.)` are recorded as printed targets only; they are not an independent estimate by INTERN-01. The artwork does not define a common origin, datum, coordinate frame, tolerance or pose for every dimension. Do not infer one.

## 3. Preliminary joint configuration and DOF

| Joint instance | Intended motion / label | DOF | ROM / angle limits | Actuator technology shown | Week 2 disposition |
|---|---|---|---|---|---|
| Left shoulder yaw | Yaw / rotation | 1 | TBD — no approved range in source | BLDC/PMSM with gearbox, as shown | Baseline joint; torque/speed/S/M/L in ACTUATOR_ANALYSIS.md |
| Left shoulder pitch | Pitch | 1 | TBD — no approved range in source | BLDC/PMSM with gearbox, as shown | Baseline joint; torque/speed/S/M/L in ACTUATOR_ANALYSIS.md |
| Left elbow | Pitch | 1 | TBD — no approved range in source | BLDC/PMSM with gearbox, as shown | Baseline joint; torque/speed/S/M/L in ACTUATOR_ANALYSIS.md |
| Left wrist | Pitch | 1 | TBD — no approved range in source | BLDC/PMSM with gearbox, as shown | Baseline joint; torque/speed/S/M/L in ACTUATOR_ANALYSIS.md |
| Right shoulder yaw | Yaw / rotation | 1 | TBD — no approved range in source | BLDC/PMSM with gearbox, as shown | Baseline joint; torque/speed/S/M/L in ACTUATOR_ANALYSIS.md |
| Right shoulder pitch | Pitch | 1 | TBD — no approved range in source | BLDC/PMSM with gearbox, as shown | Baseline joint; torque/speed/S/M/L in ACTUATOR_ANALYSIS.md |
| Right elbow | Pitch | 1 | TBD — no approved range in source | BLDC/PMSM with gearbox, as shown | Baseline joint; torque/speed/S/M/L in ACTUATOR_ANALYSIS.md |
| Right wrist | Pitch | 1 | TBD — no approved range in source | BLDC/PMSM with gearbox, as shown | Baseline joint; torque/speed/S/M/L in ACTUATOR_ANALYSIS.md |
| Left wheel-pair drive | Drive rotation, one channel for left wheel pair | 1 | TBD — no approved range in source | BLDC with encoder; optional gearbox, as shown | Baseline joint; torque/speed/S/M/L in ACTUATOR_ANALYSIS.md |
| Right wheel-pair drive | Drive rotation, one channel for right wheel pair | 1 | TBD — no approved range in source | BLDC with encoder; optional gearbox, as shown | Baseline joint; torque/speed/S/M/L in ACTUATOR_ANALYSIS.md |

**DOF / actuator count check:** 10 baseline joint/channel rows are documented. DOF arithmetic is concept-level only; it does not prove actuator performance, independent-control suitability, torque capacity, speed, thermal capability or S/M/L compatibility.

Optional or excluded elements: Optional two-finger grippers, each may be servo/BLDC powered or passive; optional force sensors. Fixed head with camera; head pan has 0 DOF and is explicitly excluded. Concept sheet mentions camera/IMU/LiDAR space, cross-section shows head camera and torso IMU. Battery is not drawn and battery sizing is not part of the study per README.

Joint range, zero position, axis unit vectors, coordinate frames, hard stops, allowable speed, duty cycle, gear ratio and output interface details are `TBD` unless specified in the source. Do not infer axes from the rendered motor orientation.

## 4. Major assemblies and load-path context

| Assembly / subsystem | Current concept interpretation | Evidence status |
|---|---|---|
| Primary body / base | Humanoid upper torso with fixed head, mounted on a differential-drive chassis. Two arms each have four baseline DOF (shoulder yaw, shoulder pitch, elbow pitch and wrist pitch). The base has two driven channels: left wheel pair and right wheel pair, with four physical wheels shown. The approved study baseline is 10 actuators (8 arm + 2 base); head pan is excluded and grippers are optional/not counted. A printed future path to five-DOF arms and an advanced mobile base is not part of the baseline. | Illustrative; not released |
| Joints / transmissions | Modular rotary joint housings; BLDC/PMSM motors, harmonic or planetary gearbox examples, output shaft and absolute/incremental encoder where shown. | Illustrative options; no specific model/ratio |
| Links / limbs | Concept-specific arms or legs; see concept artwork and material option register. | Illustrative; geometry not to scale |
| End effectors / feet | Optional two-finger grippers, each may be servo/BLDC powered or passive; optional force sensors. Fixed head with camera; head pan has 0 DOF and is explicitly excluded. Concept sheet mentions camera/IMU/LiDAR space, cross-section shows head camera and torso IMU. Battery is not drawn and battery sizing is not part of the study per README. | Optional elements remain owner decision / TBD |
| Kritva platform space | Conceptual space only for relevant Kritva Edge compute/control, power distribution/protection, motor drivers, sensors and communication. | Board dimensions, connectors, thermal and cable limits TBD |

**Qualitative load path / preliminary mechanical considerations:** Arm load path: payload/gripper → wrist → forearm → elbow → upper arm → shoulder → torso → base chassis → wheel contact patch/floor. Base drive load path: motor/gearbox → wheel hub → tyre/contact patch. Examine tall-body/arm-extension tipping, wheel reactions, base footprint, differential traction and turn envelope, arm-arm workspace/interference, stiffness of torso/shoulder mounts and cable passage across moving chassis. Printed target 25–35 kg and 1200 mm overall height are unverified concept targets, not a stability analysis.

## 5. Interface architecture

Wheel pair/base chassis and motor mount; torso-to-base structural/mobility interface; two shoulder mounts to torso; shoulder/elbow/wrist links; optional gripper mounts; fixed head/camera mount; torso compute/power/sensor/driver packaging; base drive-driver packaging; moving torso-to-base cable path. I/O labels include Ethernet, USB and GPIO; EtherCAT is the existing platform communication direction where relevant but no implementation/wiring is specified.

The interface breakdown is expanded in `INTERFACES.md`. Treat all interfaces as conceptual until a source-controlled drawing/specification exists and the relevant owner confirms it.

## 6. Material and process options (not selections)

Artwork shows differential-drive base with four wheels, left and right driven pairs, BLDC motor/encoder per side, optional gearbox, hub and rubber tyre; torso frame aluminium or carbon; arm links aluminium/CNC/3D-printed with composites as options; BLDC/PMSM joints with harmonic/planetary gearboxes, output shaft encoder and timing belt where used; rubber/TPU finger pads. No material/process selected.

The above are artwork options. No grade, heat treatment, layup, additive process, machining route, supplier or process capability is selected. Any later material comparison must cite source properties and distinguish handbook values from manufacturer data.

## 7. Cable routing and service access

Arm cables pass through shoulders, links, wrist and gripper; torso routing joins the base via a moving torso-to-base path. Consider compound bend/twist/strain at eight arm joints plus mobile chassis crossing, connector retention, strain relief, service access and potential pinch at rotating/moving interfaces. No harness design.

No cable harness design, connector selection, bend-radius value, routing dimensions or electrical design is created here. The study only reserves conceptual routes and records mechanical concerns.

## 8. Mass assumption boundary

25–35 kg printed target range (marked est.) on concept sheet; provenance remains CONCEPT_TARGET and no derivation is supplied.

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

- Existing concept record: `feasibility/concepts/DA-04/README.md`
- Study plan: `feasibility/STUDY_PLAN.md` sections 4, 6, 8 and 9.1.
- Design guidelines: `feasibility/DESIGN_GUIDELINES.md` sections 2–7.
- Requirements: `feasibility/REQUIREMENTS_REGISTER.md` FREQ-002 to FREQ-034.
- Artwork index and manifest: `docs/images/ARTWORK_INDEX.md`; `docs/images/ARTWORK_MANIFEST.json`.
- Concept-specific source register: `references/SOURCE_REGISTER.md`.
