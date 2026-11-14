# QR-04 — Architecture and Mechanical Configuration (Week 2)

**Status:** PROPOSED — paper feasibility study; subject to owner review.

**HOLD:** Mechanical HOLD D-003 remains active.

**Evidence boundary:** Week 2 architecture documentation and preliminary mechanical assessment. No CAD, simulation, bench or physical evidence is claimed.

**Numeric classification:** Artwork values are `CONCEPT_TARGET`; unsupported quantities remain `TBD`/`UNKNOWN`; any qualitative rating is `ESTIMATE`.

| Field | Value |
|---|---|
| Concept | Agile Long-Leg Quadruped |
| Family / complexity | Legged / High |
| Assigned intern | INTERN-01 |
| Study checkpoint | Week 2 / CP2 contribution |
| Source artwork | `docs/images/KMECH-CONCEPT-QR-04.png`; `docs/images/KMECH-CROSS-SECTION-QR-04.png` |
| Architecture maturity | Preliminary concept interpretation; not an approved architecture |

## 1. Configuration

Four symmetric long-leg assemblies on a central rigid body; three joints per leg: hip abduction/adduction, hip flexion/extension and knee flexion/extension. Baseline is 12 actuators. No ankle or foot actuator is in the current baseline. Feet are conceptually rubber/PU or interchangeable rubber/TPU; optional top RGB-D/IMU sensor module is height adjustable in the cross-section only. The cross-section also shows an indicative 4 × M5 / 2 × Ø5 mm dowel body mounting interface that requires owner review.

The source artwork is illustrative, PROPOSED, maturity L0 and not to scale. The sheets are not CAD, manufacturing drawings or engineering evidence. The earlier concept README remains the primary transcribed record. This Week 2 update expands its architecture description and records unknowns; it does not approve dimensions or interfaces.

## 2. Published preliminary dimensions and targets

| Dimension / property | Published value | Source | Classification / note |
|---|---|---|---|
| Body length (L) | 450 mm | Concept sheet and cross-section | CONCEPT_TARGET |
| Body width (W) | 280 mm | Concept sheet and cross-section | CONCEPT_TARGET |
| Body height (H) | 320 mm | Concept sheet and cross-section | CONCEPT_TARGET |
| Overall length with leg extension | 620 mm | Concept sheet | CONCEPT_TARGET; sheet-specific / not independently cross-checked |
| Overall width with leg extension | 520 mm | Concept sheet and cross-section | CONCEPT_TARGET |
| Target robot weight | 5–7 kg (printed as est.) | Concept sheet | CONCEPT_TARGET; basis not provided |
| Target payload | 0.5–1.0 kg (printed as est.) | Concept sheet | CONCEPT_TARGET; basis not provided |
| Supply voltage | 24 V DC | Concept sheet and cross-section | CONCEPT_TARGET; investigation direction only |
| Power rails | 24 V input; 5 V and 12 V rails | Cross-section | CONCEPT_TARGET; electrical specification TBD |
| Indicative body mount | 4 × M5 holes + 2 × Ø5 mm dowels | Cross-section only | Indicative concept; OWNER_DECISION; not an approved interface |

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

Optional or excluded elements: Optional top sensor module: RGB-D camera and IMU on adjustable mount; USB/MIPI are shown as sensor interfaces. Replaceable rubber/TPU or rubber/PU foot; no ankle/foot actuator in baseline. Cross-section-only body mount remains indicative and unresolved.

Joint range, zero position, axis unit vectors, coordinate frames, hard stops, allowable speed, duty cycle, gear ratio and output interface details are `TBD` unless specified in the source. Do not infer axes from the rendered motor orientation.

## 4. Major assemblies and load-path context

| Assembly / subsystem | Current concept interpretation | Evidence status |
|---|---|---|
| Primary body / base | Four symmetric long-leg assemblies on a central rigid body; three joints per leg: hip abduction/adduction, hip flexion/extension and knee flexion/extension. Baseline is 12 actuators. No ankle or foot actuator is in the current baseline. Feet are conceptually rubber/PU or interchangeable rubber/TPU; optional top RGB-D/IMU sensor module is height adjustable in the cross-section only. The cross-section also shows an indicative 4 × M5 / 2 × Ø5 mm dowel body mounting interface that requires owner review. | Illustrative; not released |
| Joints / transmissions | Modular rotary joint housings; BLDC/PMSM motors, harmonic or planetary gearbox examples, output shaft and absolute/incremental encoder where shown. | Illustrative options; no specific model/ratio |
| Links / limbs | Concept-specific arms or legs; see concept artwork and material option register. | Illustrative; geometry not to scale |
| End effectors / feet | Optional top sensor module: RGB-D camera and IMU on adjustable mount; USB/MIPI are shown as sensor interfaces. Replaceable rubber/TPU or rubber/PU foot; no ankle/foot actuator in baseline. Cross-section-only body mount remains indicative and unresolved. | Optional elements remain owner decision / TBD |
| Kritva platform space | Conceptual space only for relevant Kritva Edge compute/control, power distribution/protection, motor drivers, sensors and communication. | Board dimensions, connectors, thermal and cable limits TBD |

**Qualitative load path / preliminary mechanical considerations:** Primary load path: body/chassis → hip joint → thigh link → knee joint → lower-leg link → foot pad → ground. Assess leg workspace, foot placement, ground/body clearance, stance support polygon, static stability, dynamic stability concerns for trotting/gait, ground impact/contact, joint loads and long-link bending/inertia. The cross-section's indicative body mount is not an approved mechanical interface. No gait/stability/strength result is demonstrated.

## 5. Interface architecture

Body-to-four hip mounts; joint modules to thigh and lower-leg links; lower leg to rubber/PU foot; cross-section-only indicative body mounting interface; optional adjustable sensor mount; Edge compute; power distribution/protection; four-leg motor-driver stack; sensor USB/MIPI; internal body and leg cable channels. No exact datums, hole coordinates, tolerances, fastener grade, preload or load rating may be inferred from the indicative mount.

The interface breakdown is expanded in `INTERFACES.md`. Treat all interfaces as conceptual until a source-controlled drawing/specification exists and the relevant owner confirms it.

## 6. Material and process options (not selections)

Artwork shows rigid body in aluminium or carbon; long legs with hip/thigh/lower-leg links; joint housings aluminium/CNC; BLDC/PMSM with harmonic/planetary gearbox and absolute/incremental encoder; rubber/PU foot pad. Carbon/aluminium link options are illustrative only. No grade, layup, process, supplier or selection.

The above are artwork options. No grade, heat treatment, layup, additive process, machining route, supplier or process capability is selected. Any later material comparison must cite source properties and distinguish handbook values from manufacturer data.

## 7. Cable routing and service access

Cables pass through body channels, hip, thigh and lower-leg links. Long legs increase path length and repeated flex cycles. Need bend radius, twist allowance, strain relief, connector retention, abrasion protection and service access from owners; none are dimensioned.

No cable harness design, connector selection, bend-radius value, routing dimensions or electrical design is created here. The study only reserves conceptual routes and records mechanical concerns.

## 8. Mass assumption boundary

5–7 kg printed target range (marked est.) on concept sheet; provenance remains CONCEPT_TARGET and no derivation is supplied.

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

- Existing concept record: `feasibility/concepts/QR-04/README.md`
- Study plan: `feasibility/STUDY_PLAN.md` sections 4, 6, 8 and 9.1.
- Design guidelines: `feasibility/DESIGN_GUIDELINES.md` sections 2–7.
- Requirements: `feasibility/REQUIREMENTS_REGISTER.md` FREQ-002 to FREQ-034.
- Artwork index and manifest: `docs/images/ARTWORK_INDEX.md`; `docs/images/ARTWORK_MANIFEST.json`.
- Concept-specific source register: `references/SOURCE_REGISTER.md`.
