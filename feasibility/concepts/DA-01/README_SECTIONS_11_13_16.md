# DA-01 — Proposed README updates (sections 11, 13–16)

Draft only; merge into the concept README only after owner review. This update records evidence status and does not change the source artwork, establish requirements, or release HOLD D-003.

## 11. Feasibility Activity (Week 3/4)

The Week 3/4 contribution is a source-traceability and calculation-gap record, not a complete feasibility result.

- Per-joint loads and speeds: NOT DERIVED; calculations/CALC-DA01-01_joint_torque.md records why the source baseline lacks enough inputs for a numeric torque.
- Published mass target transcribed; subsystem masses and CoM UNKNOWN: MASS_BUDGET.md.
- Cost ceiling source and unpriced BOM scope recorded; no price totals or affordability claim: COST_MODEL.md.
- Qualitative configuration/load-path notes only; no stability margin or clamp recommendation: MECHANICAL_ANALYSIS.md.
- Open inputs and source decision references: OPEN_QUESTIONS.md.
- Week 2 source and HOLD guardrails: WEEK2_README_SECTIONS.md and calculations/WEEK2_ARCHITECTURE_CHECKS.md.
- Common requirements traceability: REQUIREMENTS.md and feasibility/REQUIREMENTS_REGISTER.md (FREQ-002, FREQ-004–008, FREQ-012–013, FREQ-015, FREQ-019–020, FREQ-026–028 and FREQ-032–034).

Printed targets remain CONCEPT_TARGET. Unsupported component masses, costs, geometry and motion inputs remain UNKNOWN/TBD. No CAD, BOM, quote, simulation, bench or physical evidence is claimed.

## 13. Folder Contents

| File / folder | Purpose | Evidence status |
|---|---|---|
| README.md | Existing concept overview, artwork transcription and open items | Source record; targets remain unapproved |
| REQUIREMENTS.md | Targets and common FREQ references | INCOMPLETE; no approved concept baseline |
| ARCHITECTURE.md | Configuration, joint count and dimensions | Concept-level; unspecified geometry remains TBD |
| MECHANICAL_ANALYSIS.md | Load path and stability evidence status | Qualitative; no margin or recommendation |
| ACTUATOR_ANALYSIS.md | Joint inventory, sourced family roles and missing requirements | Per-joint sizing TBD |
| INTERFACES.md | Compute, power, sensors, communication and cable provisions | Concept-level; detailed interfaces TBD |
| MASS_BUDGET.md | Printed target and subsystem evidence gaps | Total/component masses UNKNOWN |
| COST_MODEL.md | Quote-ready category scope and cost source | Prices/total UNKNOWN; EC-03 not scored |
| OPEN_QUESTIONS.md | Owner decisions and evidence needed | Open |
| WEEK2_README_SECTIONS.md | Week 2 scope and guardrails | Retained |
| README_SECTIONS_11_13_16.md | This proposed update | Draft only |
| calculations/ | Calculation notes | CALC-DA01-01_joint_torque.md and WEEK2_ARCHITECTURE_CHECKS.md |
| references/ | Source register | SOURCE_REGISTER.md |
| reviews/ | Concept review record | WEEK2_CONCEPT_REVIEW.md; review status unchanged |
| sketches/ | Concept mockups | WEEK2_CONCEPT_SKETCH.svg and WEEK3_CONCEPT_MOCKUP.svg; not to scale or CAD |

No cad/ directory is permitted under HOLD D-003.

## 14. Current Assessment

| Aspect | Status |
|---|---|
| Configuration and DOF | Transcribed from concept README/artwork; axis questions remain |
| Torque and speed | TBD; only a conditional payload-only calculation is documented |
| Mass and CoM | Printed target only; subsystem values and total UNKNOWN |
| Cost vs ceiling | No priced BOM; EC-03 NOT SCORED |
| S/M/L mapping | NOT SCORED; family roles are proposals, not assignment |
| Stability | UNKNOWN; no CoM/support inputs or clamp recommendation |
| Comparative status | NOT SCORED; no ranking or recommendation |

## 15. Checkpoint Progress

- CP2 source and architecture record: see CP2_CONTRIBUTION.md; global review remains separate.
- CP3 contribution: see feasibility/interns/INTERN-01/CP3_CONTRIBUTION.md; evidence gaps remain explicit.
- CP4: not started; all 12 concepts and required reviews remain outstanding.

## 16. Open Decisions

See OPEN_QUESTIONS.md. Do not revise decision IDs or approval dates without the controlling decision record. HOLD D-003 remains active.
