# INTERN-01 — CP3 contribution draft (Week 3/4)

| Property | Value |
|---|---|
| Status | PROPOSED — four-concept evidence contribution; not CP3 acceptance |
| Version | 0.3.0 |
| Last Updated | 2026-11-28 |
| Concepts | DA-01, QR-02, DA-04, QR-04 |
| HOLD | D-003 active |

This is an evidence handoff for four assigned concepts. It does not claim all-12 CP3 review or mark ROB-MECH-044 accepted. The package task map assigns ROB-MECH-044 to INTERN-01. Task acceptance and the repository task register remain separate from this estimate.

## 1. Evidence added or reconciled

- Replaced blanket placeholder fields in the four working requirement records with concept-target transcription, sourced scenarios, explicit calculation limits and review actions. No approved requirement or owner decision is invented.
- Added dated, source-linked low/nominal/high mass budgets, cost scenarios and actuator screens for DA-01, QR-02, DA-04 and QR-04.
- Re-ran DA-01 point-mass calculations using a sourced 0.240 kg wrist-module mass. Revised 1.5× screens are 1.33 Nm elbow, 0.31 Nm wrist pitch, 1.03 Nm shoulder-yaw inertia and 4.77 Nm conditional shoulder pitch.
- Reconciled QR-02 at 6.30 kg sensor-excluded nominal mass and QR-04 at 7.43 kg exact / 7.50 kg rounded mass. QR-02’s optional camera is +0.102 kg; it is not counted in the mass baseline. QR-04 moment arms use 0.1 mm rounding throughout.
- Re-ran DA-04 arm and wheel screens with explicit payload, link, acceleration, wheel-radius and slope assumptions. The highest 1.5× shoulder-pitch screen is 14.64 Nm at 1.0 kg payload.
- Added candidate product data and role mapping: S wrist/neck, M elbow/reference, L hip/knee. The family source labels S/L figures as placeholders; every comparison states voltage, role or evidence limitations.
- Added the source-backed cost ceiling from EVALUATION_CRITERIA.md EC-03 and FREQ-032, price bases, and alternative scenarios. No generic estimate is presented as a quote or procurement authorization. QR-02/QR-04 full L-role lower bounds use two 18 Nm AK10-9 modules per joint; their ideal torque addition is not mechanically validated; couplings, mounts and 48 V integration are excluded and the result exceeds the study ceiling.
- Updated the comparison matrix and note to a matching partial order: DA-01 (3.45), DA-04 (2.85), QR-02 (2.80), QR-04 (2.40). All seven proposed criteria contribute 100% of the weights for these four concepts; this remains partial across 4 of 12 concepts, not a CP4 ranking or final recommendation.
- Restored Week 2 architecture and D-003 traceability, plus explicit FREQ references in the DA-01 README overlay and concept requirement records.
- Corrected the DA-01 folder inventory, its target/cost summary and neutral recommendation wording. The source README’s decision-date statement is not repeated as a newly verified approval or assigned an invented decision ID.

## 2. ROB-MECH-044 evidence map (review pending)

| Criterion | Evidence in this contribution | Review status |
|---|---|---|
| AC-044-01 — concept requirement records | Four REQUIREMENTS.md files transcribe concept targets, applicable FREQs and estimate branches. | Files present; owner review is still required before requirements are accepted. |
| AC-044-02 — torque/speed formulas and inputs | Four calculation notes give formulas, units, source references, geometry/mass assumptions and static or inertial results. | Calculation screens are traceable; axis interpretation, pose and duty remain review constraints, not unfilled calculation rows. |
| AC-044-03 — S/M/L comparison | Each concept compares load screens with proposed S/M/L roles and sourced product references. | Role/load mismatches are identified; no variant is qualified or selected. |
| AC-044-04 — evidence labeling and claims | Paper/estimate status, sources, assumptions and non-validation limits are explicit. | Independent reviewer acceptance remains outstanding; no simulation, bench or physical result is claimed. |

## 3. Review actions

1. Have the concept owner confirm DA-01 axis alternatives, optional camera/mast scope and powered-gripper scope before baseline revision.
2. Review the sourced actuator variants, family roles, voltage differences, and load scenarios; do not infer continuous suitability from static torque alone.
3. Review the quadruped one-leg conservative load assumption, exact moment-arm scenarios and sensor/battery branches before any gait requirement is adopted.
4. Review DA-04’s battery/drive assumptions, mobile stability scenario and 24 V/48 V alternative.
5. Independently check the cost arithmetic, references and provisional scores before recording task acceptance.

## 4. Week 2 and downstream boundary

Week 2 architecture and HOLD D-003 references are retained in each concept’s WEEK2_README_SECTIONS.md, ARCHITECTURE.md, WEEK2_ARCHITECTURE_CHECKS.md and reviews/WEEK2_CONCEPT_REVIEW.md. FREQ traceability is linked through feasibility/REQUIREMENTS_REGISTER.md. No parent study baseline or task state is changed by this contribution.

The other eight concepts and cross-intern evidence are outside this assignment. CP2/CP3/CP4 acceptance and the final concept recommendation remain open for the full study. No CAD, final BOM, procurement, fabrication, assembly or physical test is authorized.