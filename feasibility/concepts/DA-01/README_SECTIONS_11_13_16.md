# DA-01 — Suggested README updates (sections 11, 13–16)

Copy or merge into the concept README under the intern-owned sections. Preserve existing sections 1–10, artwork references and version history. This proposal does not change the concept baseline or release HOLD D-003.

## 11. Feasibility Activity (Week 3/4 update)

Week 3/4 engineering assessment is in progress at paper level; Task 044 acceptance remains pending owner/reviewer review.

- Joint torque and speed screens: ACTUATOR_ANALYSIS.md and calculations/CALC-DA01-01_joint_torque.md.
- Mass subsystem ranges and target comparison: MASS_BUDGET.md.
- Category cost estimate versus the INR 2 L planning ceiling: COST_MODEL.md; no quotes.
- Qualitative stability, structure and serviceability: MECHANICAL_ANALYSIS.md.
- Open decisions and risks: OPEN_QUESTIONS.md.
- Requirements and common FREQ traceability: REQUIREMENTS.md and the common feasibility/REQUIREMENTS_REGISTER.md, including FREQ-002, FREQ-004–008, FREQ-012–013, FREQ-015, FREQ-019–020, FREQ-026–028 and FREQ-032–034.
- Week 2 configuration, paper-only scope and HOLD D-003 guardrails remain documented in WEEK2_README_SECTIONS.md and the linked architecture/review records.

All numeric results are ESTIMATE / ASSUMED unless explicitly marked otherwise. S/M/L mapping remains blocked on controlled variant data. No simulation, bench or physical evidence is claimed; CAD, BOM, quotations, procurement, fabrication, assembly and physical testing remain NOT STARTED under HOLD D-003.

## 13. Folder Contents (current)

| File / folder | Purpose | Current status |
|---|---|---|
| README.md | Existing concept overview and study tracking | Preserve existing sections; review proposed updates |
| REQUIREMENTS.md | Concept targets, common FREQ references and requirement gaps | INCOMPLETE; owner review pending |
| ARCHITECTURE.md | Configuration, dimensions, joints, DOF and assemblies | Proposed concept record |
| MECHANICAL_ANALYSIS.md | Load paths, workspace, stability, stiffness and serviceability | Qualitative; stability margin TBD |
| ACTUATOR_ANALYSIS.md | Per-joint torque/speed and S/M/L screening status | ESTIMATE; axis/maturity gaps remain |
| INTERFACES.md | Mechanical, compute, power, sensor, communication and cable provisions | Concept-level; detailed interfaces TBD |
| MASS_BUDGET.md | Artwork target and subsystem mass estimates | ESTIMATE; plate/enclosure assumptions explicit |
| COST_MODEL.md | Preliminary cost categories and ceiling sensitivity | ESTIMATE; no quotes |
| OPEN_QUESTIONS.md | Decisions, unknowns, dependencies and risks | Open |
| WEEK2_README_SECTIONS.md | Week 2 scope, guardrails, traceability and original section proposal | Retained for context |
| README_SECTIONS_11_13_16.md | Week 3/4 suggested README updates | Draft only; not merged into the concept README |
| calculations/ | Calculation notes | CALC-DA01-01_joint_torque.md and WEEK2_ARCHITECTURE_CHECKS.md |
| references/ | Source register | SOURCE_REGISTER.md |
| reviews/ | Concept review record | WEEK2_CONCEPT_REVIEW.md; not reviewed |
| sketches/ | Paper sketches only | WEEK2_CONCEPT_SKETCH.svg and WEEK3_CONCEPT_MOCKUP.svg; not CAD |

No cad/ directory is permitted under HOLD D-003.

## 14. Current Assessment

| Aspect | Status |
|---|---|
| Configuration & DOF | Documented; shoulder-axis and wrist-axis questions remain |
| Torque / speed estimates | Paper estimates only; Task 044 review pending |
| Mass ranges | ESTIMATE; nominal 5.4 kg is within the printed 5–8 kg target, but confidence is low |
| Cost vs ceiling | Nominal estimate INR 1.41 L; no quotes or procurement approval |
| S/M/L mapping | BLOCKED on controlled variant data and owner review |
| Stability | Qualitative only; CoM, support and margin TBD |
| Comparative status | Partial four-concept input only; no final recommendation before CP4 |

## 15. Checkpoint Progress

- CP2 contribution: previously supplied for the INTERN-01 concept; review state is separate.
- CP3 contribution: see feasibility/interns/INTERN-01/CP3_CONTRIBUTION.md (partial four-concept input).
- CP4: not started; full 12-concept review and owner decisions required.

## 16. Open Decisions

See OPEN_QUESTIONS.md. Critical items include the DA-01 shoulder-axis count and wrist-axis direction, torso/mast scope, gripper actuation, and controlled actuator data. Existing decision identifiers and approval dates are not revised in this proposal pending confirmation against the decision record.
