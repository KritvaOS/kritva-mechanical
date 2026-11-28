# DA-01 — Suggested README updates (sections 11, 13–16)

Copy or merge only after owner review into the concept README’s intern-owned sections. Preserve the source overview, artwork references and version history. These are proposed paper-study updates; they do not change the concept baseline or release HOLD D-003.

## 11. Feasibility Activity (Week 3/4 update)

Week 3/4 evidence is a paper-only estimate contribution to ROB-MECH-044. Acceptance remains separate from analysis.

- Joint torque screens and actuator comparisons: ACTUATOR_ANALYSIS.md and calculations/CALC-DA01-01_joint_torque.md.
- Mass and cost scenarios: MASS_BUDGET.md and COST_MODEL.md; current nominal is 6.33 kg and ₹112,773, with explicit low/high cases and no supplier quotes.
- Mechanical/stability scenario: MECHANICAL_ANALYSIS.md; optimistic whole-mass support-edge calculation only, not a pass/fail test.
- Requirements and common traceability: REQUIREMENTS.md and ../../REQUIREMENTS_REGISTER.md. Relevant IDs include FREQ-002, FREQ-004–008, FREQ-012–013, FREQ-015, FREQ-019–020, FREQ-026–028 and FREQ-032–034.
- Week 2 architecture and D-003 guardrails remain linked in WEEK2_README_SECTIONS.md, ARCHITECTURE.md, calculations/WEEK2_ARCHITECTURE_CHECKS.md and reviews/WEEK2_CONCEPT_REVIEW.md.
- Central estimate method and bibliography: ../../interns/INTERN-01/WEEK3_ESTIMATE_METHOD.md and ../../interns/INTERN-01/WEEK3_SOURCE_REGISTER.md.

The proposed family spec assigns S to wrist/neck, M to elbow/reference and L to hip/knee; S/L values are draft placeholders. No actuator is selected. No CAD, final BOM, quotation, procurement, fabrication, assembly or physical testing is authorized under HOLD D-003.

## 13. Folder Contents (current source tree)

| File / folder | Purpose | Current status |
|---|---|---|
| README.md | Existing concept overview and study tracking | Preserve source baseline and history. |
| REQUIREMENTS.md | Concept targets, FREQ links and requirement status | Estimate targets remain distinct from approved requirements. |
| ARCHITECTURE.md | Configuration, dimensions, joints, DOF and assemblies | Proposed concept record; Week 2 baseline retained. |
| INTERFACES.md | Mechanical, compute, power, sensor, communication and cable provisions | Concept-level interface description. |
| MECHANICAL_ANALYSIS.md | Load paths, packaging, stability and serviceability | Scenario screen; no structural or stability verification. |
| ACTUATOR_ANALYSIS.md | Per-joint torque and product-family comparison | Estimate only; no selection. |
| MASS_BUDGET.md | Artwork target and low/nominal/high mass cases | Nominal 6.33 kg; estimate, not measured. |
| COST_MODEL.md | Preliminary component categories and ₹2 lakh study-ceiling check | Nominal ₹112,773; no quotes or landed cost. |
| OPEN_QUESTIONS.md | Bounded owner choices and review actions | Scenarios explicit; no approval inferred. |
| WEEK2_README_SECTIONS.md | Week 2 scope, guardrails, traceability and original section proposal | Retained for context. |
| README_SECTIONS_11_13_16.md | Proposed README text for sections 11 and 13–16 | Draft only; not merged into concept README. |
| calculations/ | Calculation notes | CALC-DA01-01_joint_torque.md and WEEK2_ARCHITECTURE_CHECKS.md. |
| references/ | Concept-level source register | SOURCE_REGISTER.md; central Week 3 source list is in ../../interns/INTERN-01/WEEK3_SOURCE_REGISTER.md. |
| reviews/ | Concept review record | WEEK2_CONCEPT_REVIEW.md; review state is separate from estimate status. |
| sketches/ | Paper sketches | WEEK2_CONCEPT_SKETCH.svg and WEEK3_CONCEPT_MOCKUP.svg; neither is CAD. |

No cad/ directory is permitted under HOLD D-003.

## 14. Current Assessment

| Aspect | Status |
|---|---|
| Configuration and DOF | Three-axis baseline interpreted; shoulder-pitch and wrist-axis alternatives remain explicit. |
| Torque and speed | Paper estimates; 1.33 Nm elbow, 1.03 Nm shoulder-yaw, 0.31 Nm wrist-pitch and 4.77 Nm conditional shoulder-pitch screens at 1.5×. |
| Mass | 4.53 / 6.33 / 8.74 kg low/nominal/high; nominal within printed 5–8 kg target. |
| Cost | ₹112,773 economy scenario below ₹2 lakh ceiling; foreign landed cost excluded. |
| S/M/L | Proposed wrist/neck S, elbow/reference M and hip/knee L roles are stated; no hardware compatibility or selection approved. |
| Stability | Optimistic scenario only: 7.76 Nm whole-mass restoring bound vs 4.99 Nm for two extended conditional arm branches; no stability pass claimed. |
| Comparative status | All seven criteria provisionally scored for four assigned concepts; ranking is partial across 4 of 12, not a final recommendation. |

## 15. Checkpoint Progress

- CP2 work remains in its prior record; this estimate does not change its acceptance status.
- CP3 contribution: ../../interns/INTERN-01/CP3_CONTRIBUTION.md, including scoring method and Week 2/FREQ traceability.
- CP4: full 12-concept review and owner decisions remain outside this four-concept estimate. HOLD D-003 remains active.

## 16. Decision and Review Boundary

The source README’s 10-channel baseline statement is retained as source text. This proposal does not claim that the date or decision ID has been independently verified; no new approval record is invented. Review the explicit axis, camera/mast and gripper branches in OPEN_QUESTIONS.md before revising the baseline. The highest provisional score is not a recommendation or selection before CP4.