# QR-02 — Architecture and Mechanical Configuration (Week 2)

**Status:** PROPOSED — paper feasibility study; subject to owner review.

**HOLD:** Mechanical HOLD D-003 remains active.

**Evidence boundary:** Week 2 architecture documentation and preliminary mechanical assessment. No CAD, simulation, bench or physical evidence is claimed.

**Numeric classification:** Artwork values are `CONCEPT_TARGET`; unsupported quantities remain `TBD`/`UNKNOWN`; any qualitative rating is `ESTIMATE`.

| Field | Value |
|---|---|
| Concept | Standard Quadruped |
| Family / complexity | Legged / Medium |
| Assigned intern | INTERN-01 |
| Study checkpoint | Week 2 / CP2 contribution |
| Source artwork | `docs/images/KMECH-CONCEPT-QR-02.png`; `docs/images/KMECH-CROSS-SECTION-QR-02.png` |
| Architecture maturity | Preliminary concept interpretation; not an approved architecture |

## 1. Configuration

Four-legged robot with a central rigid/modular body and four symmetric three-joint legs. Each leg has hip abduction/adduction, hip flexion/extension and knee flexion/extension. Each leg ends in a replaceable foot pad; alternative feet and optional force-sensing/damping are not baseline selections. A top sensor module is optional. The concept sheet describes optional IMU/cameras; cross-section details differ and remain open.

The source artwork is illustrative, PROPOSED, maturity L0 and not to scale. The sheets are not CAD, manufacturing drawings or engineering evidence. The earlier concept README remains the primary transcribed record. This Week 2 update expands its architecture description and records unknowns; it does not approve dimensions or interfaces.

## 2. Published preliminary dimensions and targets

| Dimension / property | Published value | Source | Classification / note |
|---|---|---|---|
| Body length (L) | 350 mm | Concept sheet and cross-section | CONCEPT_TARGET |
| Body width (W) | 260 mm | Concept sheet and cross-section | CONCEPT_TARGET |
| Body height (H) | 250 mm | Concept sheet and cross-section | CONCEPT_TARGET |
| Overall length with leg extension | 520 mm | Concept sheet | CONCEPT_TARGET; sheet-specific / not independently cross-checked |
| Overall width with leg extension | 480 mm | Concept sheet and cross-section | CONCEPT_TARGET |
| Target robot weight | 4–6 kg (printed as est.) | Concept sheet | CONCEPT_TARGET; basis not provided |
| Target payload | 0.5–1.0 kg (printed as est.) | Concept sheet | CONCEPT_TARGET; basis not provided |
| Supply voltage | 24 V DC | Concept sheet and cross-section | CONCEPT_TARGET; investigation direction only |
| Power rails | 24 V input; 5 V and 12 V rails | Cross-section | CONCEPT_TARGET; electrical specification TBD |

All artwork values remain `CONCEPT_TARGET`. They are not approved product requirements. Printed weight/payload values marked `(est.)` are recorded as printed targets only; they are not an independent estimate by INTERN-01. The artwork does not define a common origin, datum, coordinate frame, tolerance or pose for every dimension. Do not infer one.

## 3. Preliminary joint configuration and DOF

| Joint instance | Intended motion / label | DOF | ROM / angle limits | Actuator technology shown | Week 2 disposition |
|---|---|---|---|---|---|
| Front-left hip abduction/adduction | Abduction / adduction | 1 | TBD — no approved range in source | BLDC/PMSM with gearbox, as shown | Baseline joint; torque/speed/S/M/L in ACTUATOR_ANALYSIS.md |
| Front-right hip abduction/adduction | Abduction / adduction | 1 | TBD — no approved range in source | BLDC/PMSM with gearbox, as shown | Baseline joint; torque/speed/S/M/L in ACTUATOR_ANALYSIS.md |
| Rear-left hip abduction/adduction | Abduction / adduction | 1 | TBD — no approved range in source | BLDC/PMSM with gearbox, as shown | Baseline joint; torque/speed/S/M/L in ACTUATOR_ANALYSIS.md |
| Rear-right hip abduction/adduction | Abduction / adduction | 1 | TBD — no approved range in source | BLDC/PMSM with gearbox, as shown | Baseline joint; torque/speed/S/M/L in ACTUATOR_ANALYSIS.md |
| Front-left hip flexion/extension | Flexion / extension (cross-section previously labelled thigh pitch; README records naming resolved) | 1 | TBD — no approved range in source | BLDC/PMSM with gearbox, as shown | Baseline joint; torque/speed/S/M/L in ACTUATOR_ANALYSIS.md |
| Front-right hip flexion/extension | Flexion / extension (cross-section previously labelled thigh pitch; README records naming resolved) | 1 | TBD — no approved range in source | BLDC/PMSM with gearbox, as shown | Baseline joint; torque/speed/S/M/L in ACTUATOR_ANALYSIS.md |
| Rear-left hip flexion/extension | Flexion / extension (cross-section previously labelled thigh pitch; README records naming resolved) | 1 | TBD — no approved range in source | BLDC/PMSM with gearbox, as shown | Baseline joint; torque/speed/S/M/L in ACTUATOR_ANALYSIS.md |
| Rear-right hip flexion/extension | Flexion / extension (cross-section previously labelled thigh pitch; README records naming resolved) | 1 | TBD — no approved range in source | BLDC/PMSM with gearbox, as shown | Baseline joint; torque/speed/S/M/L in ACTUATOR_ANALYSIS.md |
| Front-left knee | Flexion / extension | 1 | TBD — no approved range in source | BLDC/PMSM with gearbox, as shown | Baseline joint; torque/speed/S/M/L in ACTUATOR_ANALYSIS.md |
| Front-right knee | Flexion / extension | 1 | TBD — no approved range in source | BLDC/PMSM with gearbox, as shown | Baseline joint; torque/speed/S/M/L in ACTUATOR_ANALYSIS.md |
| Rear-left knee | Flexion / extension | 1 | TBD — no approved range in source | BLDC/PMSM with gearbox, as shown | Baseline joint; torque/speed/S/M/L in ACTUATOR_ANALYSIS.md |
| Rear-right knee | Flexion / extension | 1 | TBD — no approved range in source | BLDC/PMSM with gearbox, as shown | Baseline joint; torque/speed/S/M/L in ACTUATOR_ANALYSIS.md |

**DOF / actuator count check:** 12 baseline joint/channel rows are documented. DOF arithmetic is concept-level only; it does not prove actuator performance, independent-control suitability, torque capacity, speed, thermal capability or S/M/L compatibility.

Optional or excluded elements: Optional top RGB-D or stereo camera module; concept sheet also labels IMU/cameras optional. Cross-section includes an optional foot force sensor and elastomer damper. Replaceable rubber/TPU feet; spike or custom feet are options. Do not include optional sensor/foot actuator channels in the 12-joint baseline.

Joint range, zero position, axis unit vectors, coordinate frames, hard stops, allowable speed, duty cycle, gear ratio and output interface details are `TBD` unless specified in the source. Do not infer axes from the rendered motor orientation.

## 4. Major assemblies and load-path context

| Assembly / subsystem | Current concept interpretation | Evidence status |
|---|---|---|
| Primary body / base | Four-legged robot with a central rigid/modular body and four symmetric three-joint legs. Each leg has hip abduction/adduction, hip flexion/extension and knee flexion/extension. Each leg ends in a replaceable foot pad; alternative feet and optional force-sensing/damping are not baseline selections. A top sensor module is optional. The concept sheet describes optional IMU/cameras; cross-section details differ and remain open. | Illustrative; not released |
| Joints / transmissions | Modular rotary joint housings; BLDC/PMSM motors, harmonic or planetary gearbox examples, output shaft and absolute/incremental encoder where shown. | Illustrative options; no specific model/ratio |
| Links / limbs | Concept-specific arms or legs; see concept artwork and material option register. | Illustrative; geometry not to scale |
| End effectors / feet | Optional top RGB-D or stereo camera module; concept sheet also labels IMU/cameras optional. Cross-section includes an optional foot force sensor and elastomer damper. Replaceable rubber/TPU feet; spike or custom feet are options. Do not include optional sensor/foot actuator channels in the 12-joint baseline. | Optional elements remain owner decision / TBD |
| Kritva platform space | Conceptual space only for relevant Kritva Edge compute/control, power distribution/protection, motor drivers, sensors and communication. | Board dimensions, connectors, thermal and cable limits TBD |

**Qualitative load path / preliminary mechanical considerations:** Primary load path: body/chassis → hip module → thigh/link → knee module → lower-leg link → foot pad → ground. Evaluate four-leg support geometry, stance and lifted-leg cases, foot placement, support polygon, ground contact/traction/impact, body/ground clearance, leg workspace and joint range, link/joint stiffness and service access. A static margin or gait claim cannot be made because centre of mass, leg lengths, joint limits, contact/friction and stride are not specified.

## 5. Interface architecture

Body-to-four-hip structural mounts; hip/thigh/knee joint-to-link mounts; lower-leg-to-foot interface; optional top sensor mount; optional foot sensor/damper interface; internal compute/power/driver stack; battery space indicated by concept sheet; body cable channels and through-leg harness paths.

The interface breakdown is expanded in `INTERFACES.md`. Treat all interfaces as conceptual until a source-controlled drawing/specification exists and the relevant owner confirms it.

## 6. Material and process options (not selections)

Artwork shows central chassis in aluminium or carbon; hip/thigh/lower-leg links in aluminium (CNC) or 3D printed, with composite options named on concept sheet; joint housings in aluminium/CNC; harmonic or planetary gearbox; absolute or incremental encoder; rubber/TPU feet, optional force sensor and elastomer damper. All are illustrative options.

The above are artwork options. No grade, heat treatment, layup, additive process, machining route, supplier or process capability is selected. Any later material comparison must cite source properties and distinguish handbook values from manufacturer data.

## 7. Cable routing and service access

Harness passes through body channels and hips, then through hip, thigh and lower leg links to each joint. Hip abduction introduces combined cable bend and twist. No cable bend radius, twist allowance, connector, strain-relief or service-door dimensions are specified.

No cable harness design, connector selection, bend-radius value, routing dimensions or electrical design is created here. The study only reserves conceptual routes and records mechanical concerns.

## 8. Mass assumption boundary

4–6 kg printed target range (marked est.) on concept sheet; provenance remains CONCEPT_TARGET and no derivation is supplied.

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

- Existing concept record: `feasibility/concepts/QR-02/README.md`
- Study plan: `feasibility/STUDY_PLAN.md` sections 4, 6, 8 and 9.1.
- Design guidelines: `feasibility/DESIGN_GUIDELINES.md` sections 2–7.
- Requirements: `feasibility/REQUIREMENTS_REGISTER.md` FREQ-002 to FREQ-034.
- Artwork index and manifest: `docs/images/ARTWORK_INDEX.md`; `docs/images/ARTWORK_MANIFEST.json`.
- Concept-specific source register: `references/SOURCE_REGISTER.md`.
